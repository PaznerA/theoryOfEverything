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
