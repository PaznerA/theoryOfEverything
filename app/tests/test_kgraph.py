# -*- coding: utf-8 -*-
"""Sanity tests for the kgraph link-prediction package (lib/kgraph/).

These run on a tiny *synthetic* graph (a planted-partition / stochastic-block
toy) so they are fast and self-validating -- no dependence on the real
concept-graph.json. The contract:

  * the leave-k-out AUC on held-out within-cluster edges beats chance by a wide
    margin (> 0.8): the scorer recovers removed edges, not just memorizes them;
  * the local heuristics agree on an obvious triangle-completion;
  * the loader collapses parallel edges into a multiplicity weight;
  * the cross-pillar flag fires correctly.

Whole module must run in < 30 s.
"""

from __future__ import annotations

import time

import numpy as np
import pytest
import scipy.sparse as sp

from kgraph import (
    Graph,
    common_neighbor_scores,
    compute_scores,
    ensemble_scores,
    leave_k_out,
    predict_links,
)
from kgraph.loader import build_graph
from kgraph.scores import compute_scores  # noqa: F401  (re-export check)


# --------------------------------------------------------------------------
# Toy-graph fixtures
# --------------------------------------------------------------------------


def _planted_partition(n_clusters=4, per=16, p_in=0.75, p_out=0.01, seed=7):
    """Build a planted-partition Graph: dense within clusters, sparse across.

    A high-AUC link predictor should recover removed *within-cluster* edges,
    because those nodes share many common neighbors.
    """
    rng = np.random.default_rng(seed)
    n = n_clusters * per
    cluster = np.repeat(np.arange(n_clusters), per)
    nodes_json = []
    for i in range(n):
        # Encode the cluster as a single "pillar" so cross-pillar logic can be
        # exercised; two extra nodes get a shared pillar to test intersection.
        nodes_json.append({
            "id": f"n{i}",
            "name": f"Node {i}",
            "type": "concept",
            "definition": "",
            "aliases": [],
            "pillars": [f"c{cluster[i]}"],
        })
    edges_json = []
    for i in range(n):
        for j in range(i + 1, n):
            p = p_in if cluster[i] == cluster[j] else p_out
            if rng.random() < p:
                edges_json.append({"from": f"n{i}", "to": f"n{j}",
                                   "type": "related-concept"})
    g = build_graph(nodes_json, edges_json)
    return g, cluster


@pytest.fixture(scope="module")
def toy():
    return _planted_partition()


# --------------------------------------------------------------------------
# Loader
# --------------------------------------------------------------------------


def test_loader_collapses_parallel_edges_to_weight():
    nodes = [{"id": "a", "name": "A", "pillars": ["p"]},
             {"id": "b", "name": "B", "pillars": ["p"]},
             {"id": "c", "name": "C", "pillars": ["q"]}]
    # Three parallel records a-b (one reversed) + one a-c + a self-loop + a
    # dangling endpoint that must be dropped.
    edges = [
        {"from": "a", "to": "b"},
        {"from": "b", "to": "a"},
        {"from": "a", "to": "b"},
        {"from": "a", "to": "c"},
        {"from": "a", "to": "a"},          # self loop -> dropped
        {"from": "a", "to": "ghost"},      # dangling -> dropped
    ]
    g = build_graph(nodes, edges)
    assert g.n == 3
    ia, ib, ic = g.index["a"], g.index["b"], g.index["c"]
    assert g.adjacency[ia, ib] == 3.0      # multiplicity weight
    assert g.adjacency[ib, ia] == 3.0      # symmetric
    assert g.adjacency[ia, ic] == 1.0
    assert g.adjacency[ia, ia] == 0.0      # no self loop
    # Unweighted degree counts distinct neighbors.
    assert g.degree[ia] == 2
    assert g.weighted_degree[ia] == 4.0    # 3 (to b) + 1 (to c)


def test_loader_real_graph_shape():
    from kgraph import load_graph
    g = load_graph()
    assert g.n == 626
    # symmetric, zero diagonal
    diff = abs((g.adjacency - g.adjacency.T)).sum()
    assert diff == 0.0
    assert g.adjacency.diagonal().sum() == 0.0
    assert g.degree.max() > 0


# --------------------------------------------------------------------------
# Heuristics agree on an obvious triangle completion
# --------------------------------------------------------------------------


def test_triangle_completion_obvious():
    """u and v share many neighbors but no edge -> high common-neighbor score.

    The "missing" pair (u, v) must out-score a clearly unrelated pair on every
    local heuristic and on the ensemble.
    """
    nodes = [{"id": f"x{i}", "name": f"x{i}", "pillars": ["p"]}
             for i in range(8)]
    # u = x0, v = x1 share neighbors x2..x6 (5 common neighbors) but are not
    # connected. x7 is an isolated-ish distractor connected only to x2.
    edges = []
    for w in range(2, 7):
        edges.append({"from": "x0", "to": f"x{w}"})
        edges.append({"from": "x1", "to": f"x{w}"})
    edges.append({"from": "x7", "to": "x2"})
    g = build_graph(nodes, edges)

    iu, iv = g.index["x0"], g.index["x1"]
    i7, i2 = g.index["x7"], g.index["x2"]
    pairs = np.array([[iu, iv], [i7, iv]])  # good pair vs. weak pair

    cn = common_neighbor_scores(g, pairs)
    assert cn[0] == 5 and cn[0] > cn[1]

    sset = compute_scores(g, pairs, dim=4)
    for name in ("common_neighbors", "jaccard",
                 "adamic_adar", "resource_allocation"):
        assert sset[name][0] > sset[name][1], f"{name} disagreed"
    assert sset.ensemble[0] > sset.ensemble[1]


# --------------------------------------------------------------------------
# Leave-k-out beats chance on the planted partition
# --------------------------------------------------------------------------


def test_leave_k_out_beats_chance(toy):
    g, _ = toy
    res = leave_k_out(g, frac=0.10, seed=1, neg_ratio=1.0, k=20, dim=8)
    assert res.auc > 0.8, f"AUC only {res.auc:.3f} (expected > 0.8)"
    # Precision@k should also be clearly above the 0.5 base rate.
    assert res.precision_at_k > 0.6, f"P@k {res.precision_at_k:.3f} too low"
    # Every component AUC should be a real number in [0, 1].
    for name, a in res.component_auc.items():
        assert 0.0 <= a <= 1.0, f"{name} AUC out of range: {a}"


def test_leave_k_out_seed_reproducible(toy):
    g, _ = toy
    a = leave_k_out(g, frac=0.10, seed=42, dim=8)
    b = leave_k_out(g, frac=0.10, seed=42, dim=8)
    assert a.auc == b.auc
    assert a.precision_at_k == b.precision_at_k


# --------------------------------------------------------------------------
# predict_links: ranking, explanations, cross-pillar flag
# --------------------------------------------------------------------------


def test_predict_links_explanations_and_crosspillar():
    # Two pillars; a node from each shares a common neighbor -> a cross-pillar
    # candidate with a non-empty explanation.
    nodes = [
        {"id": "alpha", "name": "Alpha", "pillars": ["P"]},
        {"id": "beta", "name": "Beta", "pillars": ["Q"]},
        {"id": "hub1", "name": "Hub One", "pillars": ["P"]},
        {"id": "hub2", "name": "Hub Two", "pillars": ["Q"]},
        {"id": "gamma", "name": "Gamma", "pillars": ["P"]},
    ]
    # alpha-hub1, alpha-hub2, beta-hub1, beta-hub2 -> alpha & beta share two
    # neighbors but are not directly connected.
    edges = [
        {"from": "alpha", "to": "hub1"},
        {"from": "alpha", "to": "hub2"},
        {"from": "beta", "to": "hub1"},
        {"from": "beta", "to": "hub2"},
        {"from": "gamma", "to": "hub1"},
    ]
    g = build_graph(nodes, edges)
    cands = predict_links(g, top_n=10, dim=3, min_common=1)
    assert cands, "expected at least one candidate"

    # The alpha-beta pair must be present, cross-pillar, with shared neighbors
    # named in the explanation.
    ab = [c for c in cands if {c.a, c.b} == {"alpha", "beta"}]
    assert ab, "alpha-beta candidate missing"
    c = ab[0]
    assert c.cross_pillar is True
    assert c.n_common == 2
    assert "Hub" in c.explanation
    assert "cross-pillar" in c.explanation
    d = c.to_dict()
    assert d["crossPillar"] is True
    assert set(d.keys()) >= {"from", "to", "score", "commonNeighbors",
                             "explanation", "spectralCosine"}


def test_predict_skips_existing_edges():
    nodes = [{"id": f"q{i}", "name": f"q{i}", "pillars": ["P"]}
             for i in range(5)]
    # A 4-clique q0..q3; all those pairs are edges and must NOT be candidates.
    edges = []
    for i in range(4):
        for j in range(i + 1, 4):
            edges.append({"from": f"q{i}", "to": f"q{j}"})
    edges.append({"from": "q4", "to": "q0"})
    g = build_graph(nodes, edges)
    cands = predict_links(g, top_n=20, dim=3, min_common=1)
    for c in cands:
        i, j = g.index[c.a], g.index[c.b]
        assert g.adjacency[i, j] == 0.0, "predicted an existing edge"


# --------------------------------------------------------------------------
# Whole-module runtime budget
# --------------------------------------------------------------------------


def test_module_runtime_budget():
    """Smoke run that mirrors the heaviest path, asserting it is fast."""
    start = time.monotonic()
    g, _ = _planted_partition(n_clusters=4, per=16)
    leave_k_out(g, frac=0.10, seed=3, dim=8)
    predict_links(g, top_n=10, dim=8)
    assert time.monotonic() - start < 30.0
