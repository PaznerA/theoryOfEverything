# -*- coding: utf-8 -*-
"""Load ``concept-graph.json`` into an undirected, multiplicity-weighted graph.

The concept graph stores directed-looking edge records, but the relations
(``related-concept``, ``shared-structure``, ``duality``, ...) are conceptually
symmetric, so we collapse them to an undirected graph. Parallel edges between
the same pair (the JSON has up to multiplicity 3) become an integer *weight*:
how many source records connect the two concepts. That weight is a mild signal
of connection strength used by the weighted heuristics.

Output is a :class:`Graph` carrying:
  * ``nodes``      -- list of node ids in a fixed (file) order;
  * ``index``      -- id -> integer row/column index;
  * ``adjacency``  -- ``scipy.sparse`` CSR matrix (symmetric, zero diagonal,
                      integer multiplicity weights);
  * ``meta``       -- id -> {name, type, definition, aliases, pillars}.

No physics here -- pure graph bookkeeping. numpy + scipy only.
"""

from __future__ import annotations

import json
import os
from dataclasses import dataclass, field
from typing import Iterable

import numpy as np
import scipy.sparse as sp


@dataclass
class Graph:
    """An undirected, multiplicity-weighted concept graph with node metadata."""

    nodes: list[str]
    index: dict[str, int]
    adjacency: sp.csr_matrix          # (n, n) symmetric, zero diagonal
    meta: dict[str, dict] = field(default_factory=dict)

    # -- basic accessors ---------------------------------------------------

    @property
    def n(self) -> int:
        return len(self.nodes)

    @property
    def degree(self) -> np.ndarray:
        """Unweighted degree (number of distinct neighbors) per node."""
        binar = (self.adjacency > 0).astype(np.int8)
        return np.asarray(binar.sum(axis=1)).ravel()

    @property
    def weighted_degree(self) -> np.ndarray:
        """Sum of edge weights (multiplicities) incident on each node."""
        return np.asarray(self.adjacency.sum(axis=1)).ravel()

    def neighbors(self, i: int) -> np.ndarray:
        """Integer indices of the neighbors of node ``i``."""
        row = self.adjacency.getrow(i)
        return row.indices.copy()

    def pillars_of(self, node_id: str) -> set[str]:
        """Set of pillar slugs a node belongs to (empty if unknown)."""
        return set(self.meta.get(node_id, {}).get("pillars", []) or [])

    def has_edge(self, i: int, j: int) -> bool:
        return self.adjacency[i, j] != 0

    def with_edges_removed(self, pairs: Iterable[tuple[int, int]]) -> "Graph":
        """Return a copy of the graph with the given undirected edges zeroed.

        Used by leave-k-out evaluation: hidden edges must vanish from the
        adjacency the scorers see, without mutating the original graph.
        """
        a = self.adjacency.tolil(copy=True)
        for i, j in pairs:
            a[i, j] = 0
            a[j, i] = 0
        return Graph(
            nodes=self.nodes,
            index=self.index,
            adjacency=a.tocsr(),
            meta=self.meta,
        )


def _collapse_edges(records: list[dict], index: dict[str, int]):
    """Collapse directed records into undirected (i, j, weight) triples.

    Self-loops and edges touching unknown node ids are dropped. Parallel
    records accumulate into an integer multiplicity weight.
    """
    from collections import Counter

    counts: Counter[tuple[int, int]] = Counter()
    for e in records:
        a = e.get("from")
        b = e.get("to")
        if a is None or b is None:
            continue
        ia = index.get(a)
        ib = index.get(b)
        if ia is None or ib is None or ia == ib:
            continue
        key = (ia, ib) if ia < ib else (ib, ia)
        counts[key] += 1
    return counts


def build_graph(nodes_json: list[dict], edges_json: list[dict]) -> Graph:
    """Build a :class:`Graph` from the parsed nodes/edges JSON arrays."""
    nodes = [n["id"] for n in nodes_json]
    index = {nid: i for i, nid in enumerate(nodes)}
    n = len(nodes)

    meta: dict[str, dict] = {}
    for rec in nodes_json:
        meta[rec["id"]] = {
            "name": rec.get("name", rec["id"]),
            "type": rec.get("type", "concept"),
            "definition": rec.get("definition", ""),
            "aliases": rec.get("aliases", []) or [],
            "pillars": rec.get("pillars", []) or [],
        }

    counts = _collapse_edges(edges_json, index)
    if counts:
        ii = np.fromiter((k[0] for k in counts), dtype=np.int64, count=len(counts))
        jj = np.fromiter((k[1] for k in counts), dtype=np.int64, count=len(counts))
        ww = np.fromiter(counts.values(), dtype=np.float64, count=len(counts))
        # Symmetrize: add both (i,j) and (j,i).
        rows = np.concatenate([ii, jj])
        cols = np.concatenate([jj, ii])
        data = np.concatenate([ww, ww])
        adjacency = sp.coo_matrix((data, (rows, cols)), shape=(n, n)).tocsr()
    else:
        adjacency = sp.csr_matrix((n, n), dtype=np.float64)
    adjacency.setdiag(0)
    adjacency.eliminate_zeros()

    return Graph(nodes=nodes, index=index, adjacency=adjacency, meta=meta)


def load_graph(path: str | None = None) -> Graph:
    """Load and build the concept graph from ``concept-graph.json``.

    With no ``path`` argument the canonical ``core-data/concept-graph.json`` is
    located relative to this file (``lib/kgraph/`` -> repo root -> core-data).
    """
    if path is None:
        here = os.path.dirname(os.path.abspath(__file__))
        repo_root = os.path.abspath(os.path.join(here, os.pardir, os.pardir))
        path = os.path.join(repo_root, "core-data", "concept-graph.json")
    with open(path, encoding="utf-8") as fh:
        doc = json.load(fh)
    return build_graph(doc.get("nodes", []), doc.get("edges", []))
