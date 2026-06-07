"""Live loaders for the core-data registries and the calculations gallery.

Everything here reads the repo's JSON registries at build time, so the
dashboard counts and registry pages can never drift from the source data.
All access is defensive: a missing key never aborts the build.
"""

from __future__ import annotations

import json
import os
import re

CORE = "core-data"


def _load(repo_root: str, *parts) -> object:
    path = os.path.join(repo_root, *parts)
    with open(path, encoding="utf-8") as fh:
        return json.load(fh)


def load_findings(repo_root: str) -> list[dict]:
    return _load(repo_root, CORE, "findings.json")


def load_connections(repo_root: str) -> list[dict]:
    data = _load(repo_root, CORE, "connections.json")
    if isinstance(data, dict):
        return data.get("connections", [])
    return data


def load_formulas(repo_root: str) -> list[dict]:
    return _load(repo_root, CORE, "formulas.json")


def load_open_problems(repo_root: str) -> list[dict]:
    return _load(repo_root, CORE, "open-problems.json")


def load_references(repo_root: str) -> list[dict]:
    return _load(repo_root, CORE, "references.json")


def load_concept_graph(repo_root: str) -> dict:
    """The raw concept graph ({'nodes': [...], 'edges': [...]})."""
    return _load(repo_root, CORE, "concept-graph.json")


def load_link_predictions(repo_root: str) -> dict | None:
    """Predicted candidate edges, or None if the registry has not been built."""
    path = os.path.join(repo_root, CORE, "link-predictions.json")
    if not os.path.isfile(path):
        return None
    with open(path, encoding="utf-8") as fh:
        return json.load(fh)


# --------------------------------------------------------------------------
# Force-directed graph payload (web/dist/assets/graph-data.json)
# --------------------------------------------------------------------------

# Stable, colorblind-aware palette for the 19 pillars (+ a default). Keyed by
# pillar slug so the same approach always gets the same color across rebuilds.
PILLAR_COLORS = {
    "asymptotic-safety": "#e6194B",
    "black-holes-information": "#3cb44b",
    "causal-dynamical-triangulations": "#ffe119",
    "causal-sets": "#4363d8",
    "conceptual-problems": "#f58231",
    "emergent-gravity": "#911eb4",
    "entanglement-spacetime": "#42d4f4",
    "experimental-tests": "#f032e6",
    "group-field-theory": "#bfef45",
    "holography-adscft": "#fabed4",
    "loop-quantum-gravity": "#469990",
    "noncommutative-geometry": "#dcbeff",
    "quantum-cosmology": "#9A6324",
    "semiclassical-gravity": "#fffac8",
    "string-theory": "#800000",
    "supergravity-uv": "#aaffc3",
    "swampland": "#808000",
    "twistors-amplitudes": "#ffd8b1",
    "von-neumann-algebras": "#000075",
}
DEFAULT_PILLAR_COLOR = "#9aa0a6"


def _primary_pillar(pillars: list[str]) -> str:
    """The pillar used for node coloring: first listed (deterministic)."""
    return pillars[0] if pillars else "_none"


def build_graph_payload(repo_root: str) -> dict:
    """Assemble the JSON the force-directed web view consumes.

    Nodes carry id, name, degree, pillars, the color-group key and a (trimmed)
    definition for the side panel. Edges carry from/to, type, and explored
    rating. The top predicted candidate edges are appended with
    ``predicted: true`` and a distinct ``explored`` sentinel so the UI can style
    and toggle them separately. Degree counts distinct neighbors over the
    *undirected, de-duplicated* edge set (parallel records collapse).
    """
    g = load_concept_graph(repo_root)
    raw_nodes = g.get("nodes", [])
    raw_edges = g.get("edges", [])

    ids = {n["id"] for n in raw_nodes}

    # Undirected de-duplicated adjacency for honest degree counts.
    neighbors: dict[str, set[str]] = {n["id"]: set() for n in raw_nodes}
    seen_pairs: set[tuple[str, str]] = set()
    edges_out: list[dict] = []
    for e in raw_edges:
        a, b = e.get("from"), e.get("to")
        if a not in ids or b not in ids or a == b:
            continue
        neighbors[a].add(b)
        neighbors[b].add(a)
        key = (a, b) if a < b else (b, a)
        if key in seen_pairs:
            continue
        seen_pairs.add(key)
        edges_out.append({
            "from": a,
            "to": b,
            "type": e.get("type", "related-concept"),
            "explored": e.get("explored") or "unrated",
            "predicted": False,
        })

    nodes_out: list[dict] = []
    for n in raw_nodes:
        nid = n["id"]
        pillars = n.get("pillars", []) or []
        primary = _primary_pillar(pillars)
        definition = (n.get("definition") or "").strip()
        if len(definition) > 600:
            definition = definition[:597] + "…"
        nodes_out.append({
            "id": nid,
            "name": n.get("name", nid),
            "type": n.get("type", "concept"),
            "degree": len(neighbors[nid]),
            "pillars": pillars,
            "group": primary,
            "color": PILLAR_COLORS.get(primary, DEFAULT_PILLAR_COLOR),
            "definition": definition,
        })

    # Predicted candidate edges (top-N), distinctly marked.
    preds = load_link_predictions(repo_root)
    predicted_meta = {"available": False}
    if preds:
        predicted_meta = {
            "available": True,
            "generated": preds.get("generated"),
            "auc": preds.get("evaluation", {}).get("aucMean"),
            "count": 0,
        }
        added = 0
        for c in preds.get("candidates", []):
            a, b = c.get("from"), c.get("to")
            if a not in ids or b not in ids or a == b:
                continue
            edges_out.append({
                "from": a,
                "to": b,
                "type": c.get("type", "predicted-link"),
                "explored": "predicted",
                "predicted": True,
                "score": c.get("score"),
                "crossPillar": c.get("crossPillar", False),
                "explanation": c.get("explanation", ""),
            })
            added += 1
        predicted_meta["count"] = added

    # Pillar legend: only pillars actually present as a primary group.
    present = sorted({n["group"] for n in nodes_out if n["group"] != "_none"})
    legend = [
        {"pillar": p, "color": PILLAR_COLORS.get(p, DEFAULT_PILLAR_COLOR)}
        for p in present
    ]

    return {
        "generated": (preds or {}).get("generated"),
        "nodeCount": len(nodes_out),
        "edgeCount": sum(1 for e in edges_out if not e["predicted"]),
        "predicted": predicted_meta,
        "legend": legend,
        "nodes": nodes_out,
        "links": edges_out,
    }


# --------------------------------------------------------------------------
# Dashboard counts (pulled LIVE — never hard-coded)
# --------------------------------------------------------------------------


def dashboard_stats(repo_root: str) -> dict:
    findings = load_findings(repo_root)
    connections = load_connections(repo_root)
    formulas = load_formulas(repo_root)
    references = load_references(repo_root)
    problems = load_open_problems(repo_root)
    calcs = discover_calculations(repo_root)
    papers = [
        d for d in sorted(os.listdir(os.path.join(repo_root, "papers")))
        if os.path.isdir(os.path.join(repo_root, "papers", d))
    ] if os.path.isdir(os.path.join(repo_root, "papers")) else []

    barely = sum(1 for c in connections if c.get("explored") == "barely")

    return {
        "findings": len(findings),
        "references": len(references),
        "formulas": len(formulas),
        "connections": len(connections),
        "connections_barely": barely,
        "open_problems": len(problems),
        "calculations": len(calcs),
        "papers": len(papers),
    }


# --------------------------------------------------------------------------
# Calculations gallery
# --------------------------------------------------------------------------

# Map calc-dir name -> VYPOCET markdown route, derived by scanning each
# writeup for the core-data/calculations/<dir> path it documents.
_CALC_REF_RE = re.compile(r"core-data/calculations/([a-z0-9-]+)")


def _vypocet_index(repo_root: str) -> dict[str, str]:
    """{calc_dir_name: 'knowledge-base/vypocty/VYPOCET-...html'}."""
    out: dict[str, str] = {}
    vdir = os.path.join(repo_root, "knowledge-base", "vypocty")
    if not os.path.isdir(vdir):
        return out
    for fn in sorted(os.listdir(vdir)):
        if not fn.endswith(".md"):
            continue
        with open(os.path.join(vdir, fn), encoding="utf-8") as fh:
            text = fh.read()
        m = _CALC_REF_RE.search(text)
        if m:
            route = f"knowledge-base/vypocty/{fn[:-3]}.html"
            out.setdefault(m.group(1), route)
    return out


def _headline_numbers(results: object, limit: int = 6) -> list[tuple[str, str]]:
    """Pull a few scalar key/value pairs from results.json, safely.

    We prefer top-level scalars and one level of nesting; everything is
    stringified and truncated so the card never explodes.
    """
    pairs: list[tuple[str, str]] = []

    def _scalar(v) -> str | None:
        if isinstance(v, bool):
            return "ano" if v else "ne"
        if isinstance(v, (int, float, str)):
            s = str(v)
            return s if len(s) <= 80 else s[:77] + "…"
        return None

    # Boring keys we only fall back to when nothing more interesting exists.
    _LOW_PRIORITY = {"meta", "inputs", "conventions", "fiducial",
                     "spacetime_dimension_D", "formalism"}

    if isinstance(results, dict):
        # Pass 1: top-level scalars.
        for k, v in results.items():
            s = _scalar(v)
            if s is not None:
                pairs.append((k, s))
            if len(pairs) >= limit:
                return pairs

        # Pass 2: one level into "interesting" nested dicts (verdicts,
        # headline results, tests), skipping pure-metadata blocks first.
        def _walk(only_interesting: bool) -> None:
            for k, v in results.items():
                if len(pairs) >= limit:
                    return
                if not isinstance(v, dict):
                    continue
                if only_interesting and k in _LOW_PRIORITY:
                    continue
                if not only_interesting and k not in _LOW_PRIORITY:
                    continue
                for k2, v2 in v.items():
                    s = _scalar(v2)
                    if s is not None:
                        pairs.append((f"{k}.{k2}", s))
                    if len(pairs) >= limit:
                        return

        _walk(only_interesting=True)
        if len(pairs) < limit:
            _walk(only_interesting=False)
    return pairs[:limit]


def discover_calculations(repo_root: str) -> list[dict]:
    """One record per ``core-data/calculations/<dir>``."""
    base = os.path.join(repo_root, CORE, "calculations")
    if not os.path.isdir(base):
        return []
    vidx = _vypocet_index(repo_root)
    out: list[dict] = []
    for name in sorted(os.listdir(base)):
        cdir = os.path.join(base, name)
        if not os.path.isdir(cdir):
            continue
        results = None
        rpath = os.path.join(cdir, "results.json")
        if os.path.isfile(rpath):
            try:
                with open(rpath, encoding="utf-8") as fh:
                    results = json.load(fh)
            except (json.JSONDecodeError, OSError):
                results = None

        title = name
        if isinstance(results, dict):
            for key in ("title", "name"):
                if isinstance(results.get(key), str):
                    title = results[key]
                    break

        # Collect PNG plots (recursively: some live under plots/).
        plots: list[str] = []
        for dp, dns, fns in os.walk(cdir):
            dns[:] = [d for d in dns if d != "__pycache__"]
            for fn in sorted(fns):
                if fn.lower().endswith(".png"):
                    plots.append(
                        os.path.relpath(os.path.join(dp, fn), repo_root)
                    )
        plots.sort()

        out.append(
            {
                "name": name,
                "title": title,
                "headline": _headline_numbers(results),
                "plots": plots,
                "vypocet_route": vidx.get(name),
                "has_results": results is not None,
            }
        )
    return out


# --------------------------------------------------------------------------
# Connection-rating descriptions (Czech UI prose)
# --------------------------------------------------------------------------

RATING_ORDER = ["barely", "partially", "well"]

RATING_LABEL = {
    "barely": "barely — lovná zóna",
    "partially": "partially — částečně prozkoumáno",
    "well": "well — dobře prozkoumáno",
}

RATING_DESC = {
    "barely": (
        "Sotva prozkoumané souvislosti. Toto je primární lovná zóna projektu: "
        "místa, kde AI hledá dosud nenalezené spoje mezi přístupy."
    ),
    "partially": (
        "Částečně prozkoumané souvislosti — existuje literatura, ale "
        "kvantitativní propojení zůstává otevřené."
    ),
    "well": (
        "Dobře prozkoumané, etablované souvislosti mezi přístupy."
    ),
}

STATUS_BADGE = {
    "supported": "ok",
    "confirmed": "ok",
    "partial": "warn",
    "tentative": "warn",
    "preliminary": "warn",
    "speculative": "warn",
    "open": "warn",
    "refuted": "bad",
    "contradicted": "bad",
    "retracted": "bad",
}


def status_class(status: str | None) -> str:
    return STATUS_BADGE.get((status or "").lower(), "neutral")
