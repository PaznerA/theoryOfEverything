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


# --------------------------------------------------------------------------
# Reference resolution + formula<->concept stem-matching
# --------------------------------------------------------------------------


def _ref_url(ref: dict) -> str:
    """Best available link for a reference.

    Prefer the explicit ``url`` field; fall back to an arXiv abstract URL when
    only the bare arXiv id is present, then a DOI URL. Empty string if nothing
    resolves (caller decides how to degrade gracefully).
    """
    url = (ref.get("url") or "").strip()
    if url:
        return url
    arxiv = (ref.get("arxiv") or "").strip()
    if arxiv:
        return f"https://arxiv.org/abs/{arxiv}"
    doi = (ref.get("doi") or "").strip()
    if doi:
        return f"https://doi.org/{doi}"
    return ""


def _ref_compact(ref: dict) -> dict:
    """The self-contained subset of a reference the UI needs."""
    return {
        "authors": (ref.get("authors") or "").strip(),
        "title": (ref.get("title") or "").strip(),
        "year": ref.get("year"),
        "url": _ref_url(ref),
    }


def build_reference_index(repo_root: str) -> dict:
    """Resolve a formula ``source`` (a reference slug OR a raw arXiv id) to a ref.

    Returns ``{key -> {authors, title, year, url}}`` keyed BOTH by reference
    slug and (when present) by arXiv id, so a formula whose ``source`` is a bare
    arXiv id still resolves. All access is defensive against missing keys.
    """
    refs = load_references(repo_root)
    if isinstance(refs, dict):
        refs = refs.get("references", [])
    index: dict[str, dict] = {}
    for r in refs:
        if not isinstance(r, dict):
            continue
        compact = _ref_compact(r)
        slug = (r.get("id") or "").strip()
        if slug:
            index[slug] = compact
        arxiv = (r.get("arxiv") or "").strip()
        if arxiv and arxiv not in index:
            index[arxiv] = compact
    return index


def _concept_for_formula(formula_id: str, concept_ids: list[str]) -> str | None:
    """Stem-match a formula id to a concept id.

    A formula ``F`` links to concept ``C`` iff one id is a substring of the
    other, the shorter id is longer than 4 chars, and the length difference is
    at most 12. Among all matches the *longest* concept id wins (most specific).
    """
    fid = formula_id or ""
    best: str | None = None
    best_len = -1
    for cid in concept_ids:
        if (cid in fid) or (fid in cid):
            shorter = min(len(cid), len(fid))
            if shorter > 4 and abs(len(cid) - len(fid)) <= 12:
                if len(cid) > best_len:
                    best, best_len = cid, len(cid)
    return best


def _formula_entry(f: dict, ref_index: dict) -> dict:
    """One formula, enriched with its resolved reference (or None)."""
    source = (f.get("source") or "").strip()
    ref = ref_index.get(source) if source else None
    return {
        "id": f.get("id", ""),
        "name": f.get("name", f.get("id", "")),
        "latex": f.get("latex", ""),
        "meaning": f.get("meaning", ""),
        "pillars": f.get("pillars", []) or [],
        "source": source,
        "ref": ref,
    }


def build_formula_tree(repo_root: str) -> list[dict]:
    """A pillar -> concept -> formula tree for the formulas registry page.

    Returns a list of pillar groups::

        [{pillar, color, concepts: [{concept_id, concept_name, formulas: [...]}],
          loose: [...]}]

    Formulas are grouped first by their primary pillar, then (within a pillar)
    by the concept their id stem-matches; formulas with no concept-stem fall
    into the pillar's ``loose`` bucket. Each formula carries its resolved
    reference (or ``None``). Defensive against missing keys throughout.
    """
    formulas = load_formulas(repo_root)
    ref_index = build_reference_index(repo_root)
    g = load_concept_graph(repo_root)
    concept_nodes = g.get("nodes", [])
    concept_ids = [n["id"] for n in concept_nodes if n.get("id")]
    concept_name = {n["id"]: n.get("name", n["id"]) for n in concept_nodes if n.get("id")}

    # pillar -> {"concepts": {concept_id: [entries]}, "loose": [entries]}
    groups: dict[str, dict] = {}
    for f in formulas:
        entry = _formula_entry(f, ref_index)
        pillars = entry["pillars"]
        primary = _primary_pillar(pillars)
        bucket = groups.setdefault(primary, {"concepts": {}, "loose": []})
        cid = _concept_for_formula(entry["id"], concept_ids)
        if cid:
            bucket["concepts"].setdefault(cid, []).append(entry)
        else:
            bucket["loose"].append(entry)

    # Materialise into a stable, sorted tree. Pillars ordered by formula count
    # (desc) then name; concepts and loose by formula name.
    def _pillar_size(p: str) -> int:
        b = groups[p]
        return sum(len(v) for v in b["concepts"].values()) + len(b["loose"])

    tree: list[dict] = []
    for pillar in sorted(groups, key=lambda p: (-_pillar_size(p), p)):
        bucket = groups[pillar]
        concepts_out = []
        for cid in sorted(bucket["concepts"],
                          key=lambda c: concept_name.get(c, c).lower()):
            entries = sorted(bucket["concepts"][cid],
                             key=lambda e: (e["name"] or e["id"]).lower())
            concepts_out.append({
                "concept_id": cid,
                "concept_name": concept_name.get(cid, cid),
                "formulas": entries,
            })
        loose = sorted(bucket["loose"],
                       key=lambda e: (e["name"] or e["id"]).lower())
        tree.append({
            "pillar": pillar,
            "color": PILLAR_COLORS.get(pillar, DEFAULT_PILLAR_COLOR),
            "concepts": concepts_out,
            "loose": loose,
            "formula_count": _pillar_size(pillar),
        })
    return tree


def load_link_predictions(repo_root: str) -> dict | None:
    """Predicted candidate edges, or None if the registry has not been built."""
    path = os.path.join(repo_root, CORE, "link-predictions.json")
    if not os.path.isfile(path):
        return None
    with open(path, encoding="utf-8") as fh:
        return json.load(fh)


def load_concept_depth(repo_root: str) -> dict | None:
    """Curated derivation-depth overrides, or None if not yet authored.

    The 3D concept-graph view positions nodes on a Z (depth) axis running from
    *synthesis* (front, near the viewer — the aspirational "TOE" apex) back to
    *foundational structures* (far — basic mathematical primitives/axioms).
    Until a curated ``core-data/concept-depth.json`` exists we derive a
    provisional depth heuristically (see :func:`provisional_depths`); this loader
    is the clean swap-point for the eventual authoritative data.

    Expected shape (all keys optional, depth a float in ``[0, 1]`` where
    ``0`` = front/synthesis, ``1`` = far/foundational)::

        {"meta": {...}, "depths": {"holographic-principle": 0.12, ...}}
    """
    path = os.path.join(repo_root, CORE, "concept-depth.json")
    if not os.path.isfile(path):
        return None
    with open(path, encoding="utf-8") as fh:
        data = json.load(fh)
    if isinstance(data, dict) and isinstance(data.get("depths"), dict):
        return data["depths"]
    if isinstance(data, dict):
        return {k: v for k, v in data.items() if isinstance(v, (int, float))}
    return None


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


# --------------------------------------------------------------------------
# Derivation-depth (Z axis of the 3D concept-graph view)
# --------------------------------------------------------------------------

# Front (layer 0, near the viewer) -> far (last layer). Labels are provisional
# and describe the *intended* stratification: the aspirational "TOE" apex /
# synthesis is nearest, basic mathematical structures recede into the distance.
# A future curated core-data/concept-depth.json supersedes the heuristic that
# assigns nodes to these bands (see load_concept_depth / provisional_depths).
DEPTH_BANDS = [
    "Syntéza (← TOE)",
    "Pilíře a rámce",
    "Mosty mezi přístupy",
    "Mechanismy",
    "Stavební bloky",
    "Základní struktury · axiomy",
]
N_DEPTH_BANDS = len(DEPTH_BANDS)


def _percentile_ranks(values: dict[str, float]) -> dict[str, float]:
    """Map ``{id: value}`` to ``{id: rank in [0, 1]}`` (0 = lowest value).

    Deterministic on ties (secondary sort by id). Spreads a skewed degree
    distribution evenly across the axis so strata stay visually legible.
    """
    order = sorted(values, key=lambda k: (values[k], k))
    n = len(order)
    if n <= 1:
        return {k: 0.0 for k in values}
    return {k: i / (n - 1) for i, k in enumerate(order)}


def provisional_depths(
    raw_nodes: list[dict],
    neighbors: dict[str, set[str]],
    override: dict | None = None,
) -> dict[str, float]:
    """Provisional per-node derivation depth in ``[0, 1]`` (0 front, 1 far).

    Heuristic, honest, and deterministic — a stand-in until depth is curated.
    A node is pulled *forward* (toward synthesis / the TOE apex) the more it
    behaves like a unifying hub, and *back* (toward foundational structures)
    the more peripheral it is:

    * ``degRank``   — percentile of undirected degree (connectivity / centrality);
    * ``crossRank`` — percentile of the number of distinct pillars reachable in
      the closed neighbourhood (breadth of unification across approaches).

    ``synthesis = 0.6·degRank + 0.4·crossRank``; ``depth = 1 − synthesis``.
    Node ``type`` then nudges the result: ``pillar`` frames pull slightly
    forward, underdeveloped ``stub`` nodes are pushed back. Any id present in
    ``override`` takes that curated value verbatim (clamped to ``[0, 1]``).
    """
    pillars_by_id = {n["id"]: set(n.get("pillars") or []) for n in raw_nodes}

    degree = {n["id"]: len(neighbors.get(n["id"], ())) for n in raw_nodes}
    cross = {}
    for n in raw_nodes:
        nid = n["id"]
        reach = set(pillars_by_id.get(nid, ()))
        for m in neighbors.get(nid, ()):
            reach |= pillars_by_id.get(m, set())
        cross[nid] = float(len(reach))

    deg_rank = _percentile_ranks(degree)
    cross_rank = _percentile_ranks(cross)

    out: dict[str, float] = {}
    for n in raw_nodes:
        nid = n["id"]
        if override and nid in override:
            try:
                out[nid] = min(1.0, max(0.0, float(override[nid])))
                continue
            except (TypeError, ValueError):
                pass
        synthesis = 0.6 * deg_rank[nid] + 0.4 * cross_rank[nid]
        depth = 1.0 - synthesis
        ntype = n.get("type", "concept")
        if ntype == "pillar":
            depth *= 0.78                      # named frameworks sit forward
        elif ntype == "stub":
            depth = 0.55 * depth + 0.45        # underdeveloped -> recede
        out[nid] = min(1.0, max(0.0, depth))
    return out


def _layer_for(depth: float) -> int:
    """Quantise a continuous depth in ``[0, 1]`` into a band index."""
    idx = int(round(depth * (N_DEPTH_BANDS - 1)))
    return min(N_DEPTH_BANDS - 1, max(0, idx))


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

    # Formula<->concept index (for per-node formulaIds + the modal's compact
    # formulas/references maps). Built once, shared by all nodes below.
    formulas = load_formulas(repo_root)
    ref_index = build_reference_index(repo_root)
    concept_ids = list(ids)
    # concept_id -> [formula_id, ...] (longest-stem first so the cap keeps the
    # most specific matches).
    concept_formulas: dict[str, list[str]] = {}
    formulas_map: dict[str, dict] = {}
    used_ref_slugs: set[str] = set()
    for f in formulas:
        fid = (f.get("id") or "").strip()
        if not fid:
            continue
        source = (f.get("source") or "").strip()
        ref_slug = source if source in ref_index else None
        if ref_slug:
            used_ref_slugs.add(ref_slug)
        formulas_map[fid] = {
            "name": f.get("name", fid),
            "latex": f.get("latex", ""),
            "refSlug": ref_slug,
        }
        cid = _concept_for_formula(fid, concept_ids)
        if cid:
            concept_formulas.setdefault(cid, []).append(fid)
    # Longest stem first within each concept bucket.
    for cid, fids in concept_formulas.items():
        fids.sort(key=len, reverse=True)

    references_map = {slug: ref_index[slug] for slug in used_ref_slugs}

    # Derivation-depth (Z axis): curated override if present, else provisional.
    depth_override = load_concept_depth(repo_root)
    depths = provisional_depths(raw_nodes, neighbors, depth_override)

    nodes_out: list[dict] = []
    for n in raw_nodes:
        nid = n["id"]
        pillars = n.get("pillars", []) or []
        primary = _primary_pillar(pillars)
        definition = (n.get("definition") or "").strip()
        if len(definition) > 600:
            definition = definition[:597] + "…"
        depth = round(depths.get(nid, 0.5), 4)
        nodes_out.append({
            "id": nid,
            "name": n.get("name", nid),
            "type": n.get("type", "concept"),
            "degree": len(neighbors[nid]),
            "pillars": pillars,
            "group": primary,
            "color": PILLAR_COLORS.get(primary, DEFAULT_PILLAR_COLOR),
            "definition": definition,
            # Z-axis position: 0 = front (synthesis / TOE), 1 = far (foundations).
            "depth": depth,
            "layer": _layer_for(depth),
            # Up to 12 formulas stem-matched to this concept (longest-stem first).
            "formulaIds": concept_formulas.get(nid, [])[:12],
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
        # Z-axis (derivation depth) metadata for the 3D view's strata + ruler.
        "depthSource": "override" if depth_override else "provisional-heuristic",
        "depthBands": [
            {"layer": i, "label": label} for i, label in enumerate(DEPTH_BANDS)
        ],
        "nodes": nodes_out,
        "links": edges_out,
        # Self-contained lookups for the node-click modal: every formula
        # referenced by any node's formulaIds, plus the references they cite.
        "formulas": formulas_map,
        "references": references_map,
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
