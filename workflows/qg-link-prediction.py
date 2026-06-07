# -*- coding: utf-8 -*-
"""Generate the link-prediction registry for the concept graph.

Runs the ``kgraph`` toolkit (lib/kgraph/) on ``core-data/concept-graph.json``:

  1. Leave-10%-out evaluation, averaged over several seeds (honest AUC report).
  2. Full ranking of non-edge candidates with explanations + cross-pillar flags.
  3. Writes ``core-data/link-predictions.json`` (English) with the generated
     date, method, AUC, and the top 50 candidates.

The candidates are PROPOSALS for a human/research editor, never auto-applied
facts (see the provenance policy in the report). numpy + scipy only.

Run (from the repo root):

    MPLBACKEND=Agg PYTHONPATH=lib python3 workflows/qg-link-prediction.py
"""

from __future__ import annotations

import json
import os
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
REPO_ROOT = os.path.abspath(os.path.join(HERE, os.pardir))
LIB = os.path.join(REPO_ROOT, "lib")
if LIB not in sys.path:
    sys.path.insert(0, LIB)

from kgraph import load_graph, leave_k_out, predict_links  # noqa: E402
from kgraph.scores import spectral_embedding  # noqa: E402

GENERATED_DATE = "2026-06-07"
TOP_N = 50
DIM = 32
N_SEEDS = 8
FRAC = 0.10
OUT_PATH = os.path.join(REPO_ROOT, "core-data", "link-predictions.json")


def evaluate(graph) -> dict:
    """Leave-frac-out over N_SEEDS seeds; return mean/std AUC + a per-seed log."""
    aucs, pks = [], []
    per_component: dict[str, list] = {}
    for seed in range(N_SEEDS):
        res = leave_k_out(graph, frac=FRAC, seed=seed, neg_ratio=1.0,
                          k=50, dim=DIM)
        aucs.append(res.auc)
        pks.append(res.precision_at_k)
        for name, val in res.component_auc.items():
            per_component.setdefault(name, []).append(val)
    comp_mean = {name: float(np.mean(vals))
                 for name, vals in per_component.items()}
    return {
        "leaveKOutFraction": FRAC,
        "seeds": N_SEEDS,
        "aucMean": round(float(np.mean(aucs)), 4),
        "aucStd": round(float(np.std(aucs)), 4),
        "aucMin": round(float(np.min(aucs)), 4),
        "aucMax": round(float(np.max(aucs)), 4),
        "precisionAt50Mean": round(float(np.mean(pks)), 4),
        "componentAucMean": {k: round(v, 4) for k, v in
                             sorted(comp_mean.items(), key=lambda x: -x[1])},
    }


def main() -> int:
    graph = load_graph()
    n_edges = int((graph.adjacency > 0).sum() // 2)

    evaluation = evaluate(graph)

    embedding = spectral_embedding(graph, dim=DIM)
    candidates = predict_links(graph, top_n=TOP_N, dim=DIM,
                               embedding=embedding)

    n_cross = sum(1 for c in candidates if c.cross_pillar)
    pillar_ids = {nid for nid, m in graph.meta.items()
                  if m["type"] == "pillar"}
    n_pillar_pair = sum(1 for c in candidates
                        if c.a in pillar_ids and c.b in pillar_ids)

    doc = {
        "generated": GENERATED_DATE,
        "source": "core-data/concept-graph.json",
        "nodeCount": graph.n,
        "edgeCount": n_edges,
        "method": (
            "Ensemble (rank-average) of five classical link-prediction "
            "heuristics (common neighbors, Jaccard, Adamic-Adar, resource "
            "allocation, preferential attachment) and a normalized-Laplacian "
            "spectral embedding (d=32, cosine similarity). Implemented directly "
            "on the sparse adjacency (numpy + scipy only; no networkx/torch). "
            "Edges are undirected and weighted by multiplicity."
        ),
        "evaluation": evaluation,
        "candidatePolicy": (
            "Candidates are PROPOSALS for a human/research editor. They are NOT "
            "facts and MUST NOT be written into knowledge-base fragments or "
            "connections.json without an explicit editorial/research decision "
            "(provenance policy). High-degree pillar-node pairs are flagged via "
            "node type and are largely hub artifacts, not novel physics."
        ),
        "topCount": len(candidates),
        "crossPillarCount": n_cross,
        "pillarPairCount": n_pillar_pair,
        "candidates": [c.to_dict() for c in candidates],
    }

    # Annotate each candidate with the node types so consumers can filter the
    # hub-artifact pillar-pairs out cheaply.
    for cd, c in zip(doc["candidates"], candidates):
        cd["typeFrom"] = graph.meta[c.a]["type"]
        cd["typeTo"] = graph.meta[c.b]["type"]
        cd["nameFrom"] = graph.meta[c.a]["name"]
        cd["nameTo"] = graph.meta[c.b]["name"]

    with open(OUT_PATH, "w", encoding="utf-8") as fh:
        json.dump(doc, fh, ensure_ascii=False, indent=2)
        fh.write("\n")

    print(f"Wrote {OUT_PATH}")
    print(f"  nodes={graph.n} edges={n_edges}")
    print(f"  AUC mean={evaluation['aucMean']} "
          f"std={evaluation['aucStd']} "
          f"(min {evaluation['aucMin']}, max {evaluation['aucMax']})")
    print(f"  P@50 mean={evaluation['precisionAt50Mean']}")
    print(f"  top candidates={len(candidates)} "
          f"(cross-pillar {n_cross}, pillar-pairs {n_pillar_pair})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
