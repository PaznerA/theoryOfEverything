# -*- coding: utf-8 -*-
"""Rank the non-edges and explain the top link-prediction candidates.

A *candidate* is an unordered pair of distinct concepts with no existing edge.
We score every candidate that has at least one common neighbor (pairs with zero
shared neighbors and zero spectral overlap are uninteresting and would explode
the candidate count to ``O(n^2)``), then rank by the ensemble score.

Cross-pillar flag: a pair whose two nodes have *disjoint* pillar membership sets
is a "hunting-zone" candidate -- a proposed bridge between approaches that are
not yet known to connect. That is the project's primary target, so such pairs
are flagged (and may be surfaced separately).

Explanation: for each top candidate we record *why* it scored highly --
the shared neighbors (by name, the ones with the strongest Adamic-Adar weight)
and the spectral cosine. These are leads for a human editor, never auto-applied
facts (see the provenance policy in the report).
"""

from __future__ import annotations

import math
from dataclasses import dataclass, field

import numpy as np

from .scores import compute_scores, spectral_embedding, spectral_scores


@dataclass
class Candidate:
    a: str
    b: str
    score: float
    cross_pillar: bool
    pillars_a: list[str]
    pillars_b: list[str]
    common_neighbors: list[str]            # node ids, strongest-AA first
    common_neighbor_names: list[str]
    n_common: int
    spectral_cosine: float
    components: dict[str, float] = field(default_factory=dict)
    explanation: str = ""

    def to_dict(self) -> dict:
        return {
            "from": self.a,
            "to": self.b,
            "score": round(float(self.score), 4),
            "crossPillar": bool(self.cross_pillar),
            "pillarsFrom": self.pillars_a,
            "pillarsTo": self.pillars_b,
            "commonNeighbors": self.common_neighbors,
            "nCommon": int(self.n_common),
            "spectralCosine": round(float(self.spectral_cosine), 4),
            "components": {k: round(float(v), 4)
                           for k, v in self.components.items()},
            "explanation": self.explanation,
        }


def _candidate_pairs(graph, min_common: int = 1) -> np.ndarray:
    """All non-edge (i<j) pairs sharing >= ``min_common`` neighbors.

    Computed as ``B = A_bin @ A_bin`` (B[i,j] = #common neighbors), then masked
    to remove the diagonal, existing edges, and the lower triangle.
    """
    import scipy.sparse as sp

    binA = (graph.adjacency > 0).astype(np.float64).tocsr()
    cn = (binA @ binA).tocsr()             # common-neighbor counts
    cn = sp.triu(cn, k=1).tocoo()          # i < j only

    keep = cn.data >= min_common
    rows = cn.row[keep]
    cols = cn.col[keep]

    # Drop pairs that are already edges.
    existing = graph.adjacency
    is_edge = np.array([existing[int(i), int(j)] != 0
                        for i, j in zip(rows, cols)])
    rows = rows[~is_edge]
    cols = cols[~is_edge]
    return np.column_stack([rows, cols]).astype(np.int64)


def _explain(cand: Candidate, top_names: list[str]) -> str:
    """Human-readable (English) explanation string for a candidate."""
    parts: list[str] = []
    if cand.n_common > 0:
        shown = ", ".join(top_names[:4])
        more = "" if cand.n_common <= 4 else f" (+{cand.n_common - 4} more)"
        parts.append(
            f"{cand.n_common} shared neighbor"
            f"{'s' if cand.n_common != 1 else ''}: {shown}{more}"
        )
    if cand.spectral_cosine >= 0.2:
        parts.append(f"high spectral similarity (cos={cand.spectral_cosine:.2f})")
    elif cand.spectral_cosine <= -0.1:
        parts.append(
            f"spectrally anti-correlated (cos={cand.spectral_cosine:.2f})"
        )
    if cand.cross_pillar:
        pa = "/".join(cand.pillars_a) or "?"
        pb = "/".join(cand.pillars_b) or "?"
        parts.append(f"cross-pillar bridge [{pa}] <-> [{pb}]")
    return "; ".join(parts) if parts else "weak signal"


def predict_links(graph, top_n: int = 50, dim: int = 32,
                  min_common: int = 1,
                  embedding: np.ndarray | None = None) -> list[Candidate]:
    """Rank non-edge candidates and return the top ``top_n`` as Candidates.

    Each carries the ensemble score, component scores, cross-pillar flag, the
    shared-neighbor explanation, and the spectral cosine.
    """
    pairs = _candidate_pairs(graph, min_common=min_common)
    if len(pairs) == 0:
        return []

    if embedding is None:
        embedding = spectral_embedding(graph, dim=dim)
    sset = compute_scores(graph, pairs, dim=dim, embedding=embedding)
    order = np.argsort(-sset.ensemble, kind="mergesort")

    # Precompute neighbor structures for explanation (Adamic-Adar weight ranks
    # the shared neighbors so the explanation names the most *specific* ones).
    binA = (graph.adjacency > 0).astype(np.float64).tocsr()
    deg = np.asarray(binA.sum(axis=1)).ravel()
    indptr, indices = binA.indptr, binA.indices
    with np.errstate(divide="ignore"):
        aa_w = 1.0 / np.log(deg)
    aa_w[~np.isfinite(aa_w)] = 0.0

    nodes = graph.nodes
    meta = graph.meta

    out: list[Candidate] = []
    for rank_pos in order[:top_n]:
        u, v = int(pairs[rank_pos][0]), int(pairs[rank_pos][1])
        au, bv = nodes[u], nodes[v]
        nu = indices[indptr[u]:indptr[u + 1]]
        nv = indices[indptr[v]:indptr[v + 1]]
        shared = np.intersect1d(nu, nv, assume_unique=True)
        # Sort shared neighbors by descending Adamic-Adar weight (specificity).
        shared_sorted = shared[np.argsort(-aa_w[shared], kind="mergesort")]
        shared_ids = [nodes[w] for w in shared_sorted]
        shared_names = [meta.get(nodes[w], {}).get("name", nodes[w])
                        for w in shared_sorted]

        pa = sorted(meta.get(au, {}).get("pillars", []) or [])
        pb = sorted(meta.get(bv, {}).get("pillars", []) or [])
        cross = bool(pa) and bool(pb) and not (set(pa) & set(pb))

        comp = {name: float(vals[rank_pos])
                for name, vals in sset.components.items()}

        cand = Candidate(
            a=au, b=bv,
            score=float(sset.ensemble[rank_pos]),
            cross_pillar=cross,
            pillars_a=pa, pillars_b=pb,
            common_neighbors=shared_ids,
            common_neighbor_names=shared_names,
            n_common=len(shared_ids),
            spectral_cosine=comp.get("spectral", 0.0),
            components=comp,
        )
        cand.explanation = _explain(cand, shared_names)
        out.append(cand)
    return out
