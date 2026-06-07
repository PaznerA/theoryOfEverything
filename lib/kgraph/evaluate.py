# -*- coding: utf-8 -*-
"""Leave-k-out evaluation -- the honesty check that the scorer beats chance.

Procedure (seeded, reproducible):
  1. Hide a random ``frac`` (default 10%) of the existing undirected edges.
  2. Build a *training* graph with those edges removed.
  3. Score a candidate set = the hidden (positive) edges + an equal-or-larger
     sample of true non-edges (negatives), using ONLY the training graph.
  4. Report ranking quality:
       * AUC  -- probability a random positive outranks a random negative
                 (0.5 = chance). Computed exactly from the rank-sum statistic
                 (Mann-Whitney U), ties counted as half.
       * precision@k -- fraction of the top-k scored candidates that are
                 held-out positives.

This guards against the classic failure where a scorer looks impressive on the
training edges but cannot recover *removed* ones -- i.e. it does not generalize.
"""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np

from .scores import compute_scores, spectral_embedding


@dataclass
class EvalResult:
    method: str
    n_pos: int
    n_neg: int
    auc: float
    precision_at_k: float
    k: int
    component_auc: dict[str, float]

    def summary(self) -> str:
        return (
            f"{self.method}: AUC={self.auc:.3f}  "
            f"P@{self.k}={self.precision_at_k:.3f}  "
            f"(pos={self.n_pos}, neg={self.n_neg})"
        )


def _existing_edge_pairs(graph) -> np.ndarray:
    """Upper-triangular (i<j) index pairs of every existing edge."""
    a = graph.adjacency.tocoo()
    mask = a.row < a.col
    return np.column_stack([a.row[mask], a.col[mask]]).astype(np.int64)


def _sample_non_edges(graph, count: int, rng: np.random.Generator,
                      forbidden: set[tuple[int, int]]) -> np.ndarray:
    """Uniformly sample ``count`` (i<j) pairs that are NOT edges.

    ``forbidden`` is the set of held-out positives (which are absent from the
    training adjacency but must never be sampled as negatives).
    """
    n = graph.n
    a = graph.adjacency
    out: list[tuple[int, int]] = []
    seen: set[tuple[int, int]] = set()
    # Rejection sampling; the graph is extremely sparse so collisions are rare.
    attempts = 0
    max_attempts = count * 200 + 1000
    while len(out) < count and attempts < max_attempts:
        attempts += 1
        i = int(rng.integers(0, n))
        j = int(rng.integers(0, n))
        if i == j:
            continue
        if i > j:
            i, j = j, i
        key = (i, j)
        if key in seen or key in forbidden:
            continue
        if a[i, j] != 0:
            continue
        seen.add(key)
        out.append(key)
    return np.array(out, dtype=np.int64)


def auc_score(scores: np.ndarray, labels: np.ndarray) -> float:
    """Exact ROC-AUC from the rank-sum statistic; ties count as 0.5.

    ``labels`` is 1 for positives, 0 for negatives.
    """
    scores = np.asarray(scores, dtype=np.float64)
    labels = np.asarray(labels, dtype=np.int64)
    n_pos = int((labels == 1).sum())
    n_neg = int((labels == 0).sum())
    if n_pos == 0 or n_neg == 0:
        return float("nan")
    order = np.argsort(scores, kind="mergesort")
    ranks = np.empty(len(scores), dtype=np.float64)
    ranks[order] = np.arange(1, len(scores) + 1, dtype=np.float64)
    # Average ranks for ties so equal scores do not bias the statistic.
    _, inv, counts = np.unique(scores, return_inverse=True, return_counts=True)
    csum = np.cumsum(counts)
    starts = csum - counts
    avg = (starts + csum + 1) / 2.0  # 1-based mean rank
    ranks = avg[inv]
    sum_pos = ranks[labels == 1].sum()
    u = sum_pos - n_pos * (n_pos + 1) / 2.0
    return float(u / (n_pos * n_neg))


def precision_at_k(scores: np.ndarray, labels: np.ndarray, k: int) -> float:
    """Fraction of the top-k highest-scored candidates that are positives."""
    scores = np.asarray(scores, dtype=np.float64)
    labels = np.asarray(labels, dtype=np.int64)
    k = min(k, len(scores))
    if k == 0:
        return float("nan")
    top = np.argsort(-scores, kind="mergesort")[:k]
    return float(labels[top].sum() / k)


def leave_k_out(graph, frac: float = 0.10, seed: int = 0,
                neg_ratio: float = 1.0, k: int = 50,
                dim: int = 32) -> EvalResult:
    """Hide ``frac`` of edges, score positives vs. sampled negatives.

    Returns an :class:`EvalResult` with the ensemble AUC + precision@k and the
    per-component AUCs (so we can see which heuristic carries the signal).
    """
    rng = np.random.default_rng(seed)
    edges = _existing_edge_pairs(graph)
    m = len(edges)
    n_hide = max(1, int(round(frac * m)))
    hide_idx = rng.choice(m, size=n_hide, replace=False)
    positives = edges[hide_idx]

    forbidden = {(int(i), int(j)) for i, j in positives}
    train = graph.with_edges_removed([(int(i), int(j)) for i, j in positives])

    n_neg = int(round(neg_ratio * n_hide))
    negatives = _sample_non_edges(train, n_neg, rng, forbidden)

    cand = np.vstack([positives, negatives])
    labels = np.concatenate([
        np.ones(len(positives), dtype=np.int64),
        np.zeros(len(negatives), dtype=np.int64),
    ])

    # Score everything on the *training* graph only.
    embedding = spectral_embedding(train, dim=dim)
    sset = compute_scores(train, cand, dim=dim, embedding=embedding)

    auc = auc_score(sset.ensemble, labels)
    pk = precision_at_k(sset.ensemble, labels, k)

    comp_auc = {
        name: auc_score(vals, labels)
        for name, vals in sset.components.items()
    }

    return EvalResult(
        method="ensemble(rank-avg of 5 heuristics + spectral-cosine)",
        n_pos=len(positives),
        n_neg=len(negatives),
        auc=auc,
        precision_at_k=pk,
        k=min(k, len(cand)),
        component_auc=comp_auc,
    )
