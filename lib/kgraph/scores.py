# -*- coding: utf-8 -*-
"""Link-prediction scores: classical heuristics + a spectral embedding.

All heuristics are implemented directly on the sparse adjacency matrix (no
networkx). Each ``*_scores`` function takes a :class:`~kgraph.loader.Graph` and a
list of candidate index pairs and returns a numpy array of scores aligned with
the pairs. Higher = more likely to be a (missing) edge.

Heuristics (using neighbor sets ``N(u)``, degree ``k(u)``):
  * common neighbors        ``|N(u) & N(v)|``
  * Jaccard                 ``|N(u) & N(v)| / |N(u) | N(v)|``
  * Adamic-Adar             ``sum_{w in N(u)&N(v)} 1/log k(w)``
  * resource allocation     ``sum_{w in N(u)&N(v)} 1/k(w)``
  * preferential attachment ``k(u) * k(v)``

Spectral embedding: eigenvectors of the normalized graph Laplacian
``L = I - D^{-1/2} A D^{-1/2}`` for the ``d`` smallest non-trivial eigenvalues
(``scipy.sparse.linalg.eigsh``), giving each node a ``d``-dim coordinate; the
score of a pair is the cosine similarity of their embeddings. This captures
*global* structure the local heuristics miss (two nodes with no common neighbor
can still be spectrally close).

Ensemble: rank-average of the individual scores -- each score is converted to a
rank in ``[0, 1]`` and the ranks are averaged. Rank-averaging is scale-free, so
the wildly different score magnitudes (counts vs. cosines) combine sanely.
"""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np
import scipy.sparse as sp
import scipy.sparse.linalg as spla

Pairs = np.ndarray  # shape (m, 2), int index pairs


# --------------------------------------------------------------------------
# Neighbor bookkeeping
# --------------------------------------------------------------------------


def _binary_adj(graph) -> sp.csr_matrix:
    """Unweighted (0/1) adjacency: heuristics count neighbors, not weights."""
    a = (graph.adjacency > 0).astype(np.float64)
    return a.tocsr()


def _as_pairs(pairs) -> Pairs:
    arr = np.asarray(pairs, dtype=np.int64)
    if arr.ndim != 2 or arr.shape[1] != 2:
        raise ValueError("pairs must have shape (m, 2)")
    return arr


# --------------------------------------------------------------------------
# Local heuristics
# --------------------------------------------------------------------------


def _common_neighbor_matrix(pairs: Pairs, binA: sp.csr_matrix) -> list[np.ndarray]:
    """For each pair return the array of *shared* neighbor indices."""
    indptr = binA.indptr
    indices = binA.indices
    out: list[np.ndarray] = []
    for u, v in pairs:
        nu = indices[indptr[u]:indptr[u + 1]]
        nv = indices[indptr[v]:indptr[v + 1]]
        out.append(np.intersect1d(nu, nv, assume_unique=True))
    return out


def common_neighbor_scores(graph, pairs) -> np.ndarray:
    pairs = _as_pairs(pairs)
    binA = _binary_adj(graph)
    shared = _common_neighbor_matrix(pairs, binA)
    return np.array([len(s) for s in shared], dtype=np.float64)


def jaccard_scores(graph, pairs) -> np.ndarray:
    pairs = _as_pairs(pairs)
    binA = _binary_adj(graph)
    deg = np.asarray(binA.sum(axis=1)).ravel()
    shared = _common_neighbor_matrix(pairs, binA)
    out = np.zeros(len(pairs), dtype=np.float64)
    for idx, ((u, v), s) in enumerate(zip(pairs, shared)):
        union = deg[u] + deg[v] - len(s)
        out[idx] = len(s) / union if union > 0 else 0.0
    return out


def adamic_adar_scores(graph, pairs) -> np.ndarray:
    pairs = _as_pairs(pairs)
    binA = _binary_adj(graph)
    deg = np.asarray(binA.sum(axis=1)).ravel()
    # 1/log(k); degree-1 neighbors (log 1 = 0) contribute nothing -> weight 0.
    with np.errstate(divide="ignore"):
        w = 1.0 / np.log(deg)
    w[~np.isfinite(w)] = 0.0
    shared = _common_neighbor_matrix(pairs, binA)
    return np.array([w[s].sum() for s in shared], dtype=np.float64)


def resource_allocation_scores(graph, pairs) -> np.ndarray:
    pairs = _as_pairs(pairs)
    binA = _binary_adj(graph)
    deg = np.asarray(binA.sum(axis=1)).ravel()
    with np.errstate(divide="ignore"):
        w = 1.0 / deg
    w[~np.isfinite(w)] = 0.0
    shared = _common_neighbor_matrix(pairs, binA)
    return np.array([w[s].sum() for s in shared], dtype=np.float64)


def preferential_attachment_scores(graph, pairs) -> np.ndarray:
    pairs = _as_pairs(pairs)
    binA = _binary_adj(graph)
    deg = np.asarray(binA.sum(axis=1)).ravel()
    return np.array([deg[u] * deg[v] for u, v in pairs], dtype=np.float64)


# --------------------------------------------------------------------------
# Spectral embedding
# --------------------------------------------------------------------------


def spectral_embedding(graph, dim: int = 32) -> np.ndarray:
    """Embed nodes via the smallest non-trivial normalized-Laplacian modes.

    Returns an ``(n, d)`` array. ``d`` is clamped below ``n`` (eigsh needs
    ``k < n``). Isolated nodes (degree 0) get a zero row. The trivial constant
    eigenvector (eigenvalue ~0) is discarded.
    """
    binA = _binary_adj(graph)
    n = binA.shape[0]
    deg = np.asarray(binA.sum(axis=1)).ravel()

    safe = deg.copy()
    safe[safe == 0] = 1.0  # avoid div-by-zero; isolated rows zeroed below
    dinv_sqrt = 1.0 / np.sqrt(safe)
    D = sp.diags(dinv_sqrt)
    # Normalized Laplacian L = I - D^{-1/2} A D^{-1/2}.
    norm_adj = D @ binA @ D
    L = sp.identity(n, format="csr") - norm_adj

    # Need k+1 smallest (drop the trivial mode); eigsh requires k < n.
    k = min(dim + 1, n - 1)
    if k < 1:
        return np.zeros((n, max(dim, 1)), dtype=np.float64)
    # 'SM' is unstable; shift-invert via sigma=0 on the symmetric PSD Laplacian
    # reliably finds the smallest eigenvalues.
    try:
        vals, vecs = spla.eigsh(L, k=k, sigma=0.0, which="LM")
    except Exception:
        # Fallback for tiny / singular toy graphs.
        vals, vecs = spla.eigsh(L, k=k, which="SM")
    order = np.argsort(vals)
    vecs = vecs[:, order]
    # Drop the first (trivial, eigenvalue ~ 0) mode.
    emb = vecs[:, 1:dim + 1]
    if emb.shape[1] < dim:
        pad = np.zeros((n, dim - emb.shape[1]), dtype=np.float64)
        emb = np.hstack([emb, pad])
    emb[deg == 0] = 0.0
    return emb


def spectral_scores(graph, pairs, embedding: np.ndarray | None = None,
                    dim: int = 32) -> np.ndarray:
    """Cosine similarity of node embeddings for each candidate pair."""
    pairs = _as_pairs(pairs)
    if embedding is None:
        embedding = spectral_embedding(graph, dim=dim)
    norms = np.linalg.norm(embedding, axis=1)
    out = np.zeros(len(pairs), dtype=np.float64)
    for idx, (u, v) in enumerate(pairs):
        nu, nv = norms[u], norms[v]
        if nu == 0.0 or nv == 0.0:
            out[idx] = 0.0
        else:
            out[idx] = float(embedding[u] @ embedding[v]) / (nu * nv)
    return out


# --------------------------------------------------------------------------
# Ensemble (rank-average)
# --------------------------------------------------------------------------


def _to_rank01(values: np.ndarray) -> np.ndarray:
    """Average-rank transform into [0, 1] (ties share their mean rank)."""
    v = np.asarray(values, dtype=np.float64)
    m = len(v)
    if m == 0:
        return v
    order = np.argsort(v, kind="mergesort")
    ranks = np.empty(m, dtype=np.float64)
    ranks[order] = np.arange(m, dtype=np.float64)
    # Resolve ties to their average rank so equal scores rank-average equally.
    _, inv, counts = np.unique(v, return_inverse=True, return_counts=True)
    csum = np.cumsum(counts)
    starts = csum - counts
    avg = (starts + csum - 1) / 2.0  # mean of [start, end-1]
    ranks = avg[inv]
    if m == 1:
        return np.zeros(1, dtype=np.float64)
    return ranks / (m - 1)


# The individual scorers combined by the ensemble. Spectral is handled
# separately because it needs the shared embedding.
_LOCAL_SCORERS = (
    ("common_neighbors", common_neighbor_scores),
    ("jaccard", jaccard_scores),
    ("adamic_adar", adamic_adar_scores),
    ("resource_allocation", resource_allocation_scores),
    ("preferential_attachment", preferential_attachment_scores),
)


@dataclass
class ScoreSet:
    """All component scores for a fixed list of candidate pairs."""

    pairs: np.ndarray
    components: dict[str, np.ndarray]
    ensemble: np.ndarray

    def __getitem__(self, key: str) -> np.ndarray:
        return self.components[key]


def compute_scores(graph, pairs, dim: int = 32,
                   embedding: np.ndarray | None = None) -> ScoreSet:
    """Compute every component score plus the rank-average ensemble."""
    pairs = _as_pairs(pairs)
    components: dict[str, np.ndarray] = {}
    for name, fn in _LOCAL_SCORERS:
        components[name] = fn(graph, pairs)
    if embedding is None:
        embedding = spectral_embedding(graph, dim=dim)
    components["spectral"] = spectral_scores(graph, pairs, embedding=embedding)

    if len(pairs) == 0:
        ensemble = np.zeros(0, dtype=np.float64)
    else:
        rank_stack = np.vstack([_to_rank01(components[name])
                                for name in components])
        ensemble = rank_stack.mean(axis=0)
    return ScoreSet(pairs=pairs, components=components, ensemble=ensemble)


def ensemble_scores(graph, pairs, dim: int = 32,
                    embedding: np.ndarray | None = None) -> np.ndarray:
    """Convenience: just the ensemble score array."""
    return compute_scores(graph, pairs, dim=dim, embedding=embedding).ensemble
