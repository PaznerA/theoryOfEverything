# -*- coding: utf-8 -*-
"""kgraph -- link prediction over the Theory-of-Everything concept graph.

Knowledge *infrastructure*, deliberately kept separate from the ``toe`` physics
library: ``toe`` simulates quantum-gravity physics, whereas ``kgraph`` is a tiny
self-contained link-prediction toolkit operating on the project's own knowledge
graph (``core-data/concept-graph.json``). The project mission is to surface
yet-undiscovered connections between approaches; link prediction is exactly that
mission framed as a machine-learning task.

Design constraints (intentional):
  * NO new dependencies -- numpy + scipy only (no networkx, no torch). Every
    classical heuristic is implemented directly on a sparse adjacency matrix.
  * Deterministic and seeded; the evaluation is an honesty check that the
    scorer actually beats chance (AUC, precision@k on held-out edges).

Module map (import layers A -> B -> C; a module imports only from lower layers):

    Layer A
      loader    Parse concept-graph.json into a :class:`Graph` (undirected,
                weighted by edge multiplicity) with node metadata.
    Layer B
      scores    Classical heuristics (common neighbors, Jaccard, Adamic-Adar,
                resource allocation, preferential attachment) + a normalized-
                Laplacian spectral embedding (eigsh, d=32) with cosine
                similarity; ensemble = rank-average of the individual scores.
    Layer C
      evaluate  Leave-k-out evaluation: hide a fraction of existing edges,
                score candidate pairs, report AUC + precision@k.
      predict   Rank non-edges, flag cross-pillar (hunting-zone) pairs, and
                attach a human-readable explanation to each top candidate.

The package lives under ``lib/`` and is imported by path (the sys.path shim in
app/tests/conftest.py); there is no setup.py / pyproject.
"""

from __future__ import annotations

__version__ = "0.1.0"

from .loader import Graph, load_graph
from .scores import (
    ScoreSet,
    adamic_adar_scores,
    common_neighbor_scores,
    compute_scores,
    ensemble_scores,
    jaccard_scores,
    preferential_attachment_scores,
    resource_allocation_scores,
    spectral_embedding,
    spectral_scores,
)
from .evaluate import EvalResult, leave_k_out
from .predict import Candidate, predict_links

__all__ = [
    "Graph",
    "load_graph",
    "ScoreSet",
    "compute_scores",
    "common_neighbor_scores",
    "jaccard_scores",
    "adamic_adar_scores",
    "resource_allocation_scores",
    "preferential_attachment_scores",
    "spectral_embedding",
    "spectral_scores",
    "ensemble_scores",
    "EvalResult",
    "leave_k_out",
    "Candidate",
    "predict_links",
]
