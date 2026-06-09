"""Tests for the minimalist static-site builder (web/build.py).

These build the whole site into a temporary directory and assert structural
guarantees: enough pages, the key pages exist, every paper page carries the
internal-draft banner, internal links resolve, and the live findings count in
the JSON registry is faithfully reflected on the findings page.

The build must be fast (< 30 s) and have no third-party dependency beyond
markdown + jinja2, both of which the container ships.
"""

from __future__ import annotations

import json
import os
import re
import subprocess
import sys
import time

import pytest

_HERE = os.path.dirname(os.path.abspath(__file__))
REPO_ROOT = os.path.abspath(os.path.join(_HERE, os.pardir, os.pardir))
WEB_DIR = os.path.join(REPO_ROOT, "web")
BUILD_PY = os.path.join(WEB_DIR, "build.py")

BANNER = (
    "INTERNÍ AI-ASISTOVANÝ DRAFT — nepodáno, vyžaduje lidskou revizi "
    "(viz REVIZE-PRO-CLOVEKA)"
)


pytestmark = pytest.mark.skipif(
    not os.path.isfile(BUILD_PY), reason="web/build.py not present"
)


@pytest.fixture(scope="module")
def built_site(tmp_path_factory):
    """Build the site once into a tmp dir via the real CLI (--out)."""
    out = tmp_path_factory.mktemp("dist")
    start = time.monotonic()
    proc = subprocess.run(
        [sys.executable, BUILD_PY, "--out", str(out)],
        capture_output=True,
        text=True,
        cwd=REPO_ROOT,
        timeout=120,
    )
    elapsed = time.monotonic() - start
    assert proc.returncode == 0, (
        f"build.py failed (rc={proc.returncode})\n"
        f"STDOUT:\n{proc.stdout}\nSTDERR:\n{proc.stderr}"
    )
    # Runtime budget (generous CI ceiling; local runs are a few seconds).
    assert elapsed < 30, f"build too slow: {elapsed:.1f}s"
    return str(out)


def _read(path: str) -> str:
    with open(path, encoding="utf-8") as fh:
        return fh.read()


def _all_html(root: str):
    for dp, _dn, fns in os.walk(root):
        for fn in fns:
            if fn.endswith(".html"):
                yield os.path.join(dp, fn)


def test_minimum_page_count(built_site):
    pages = list(_all_html(built_site))
    assert len(pages) >= 80, f"only {len(pages)} pages built"


def test_key_pages_exist(built_site):
    for route in (
        "index.html",
        "progress.html",
        "data/findings.html",
        "data/connections.html",
        "data/formulas.html",
        "data/open-problems.html",
        "data/graph.html",
        "calculations.html",
        "static/style.css",
    ):
        assert os.path.isfile(os.path.join(built_site, route)), f"missing {route}"


def test_every_paper_page_has_banner(built_site):
    papers_dir = os.path.join(built_site, "papers")
    assert os.path.isdir(papers_dir), "no papers/ output"
    paper_pages = list(_all_html(papers_dir))
    assert paper_pages, "expected at least one generated paper page"
    for p in paper_pages:
        assert BANNER in _read(p), f"banner missing on {p}"


def test_banner_not_on_regular_pages(built_site):
    """The red draft banner must NOT leak onto knowledge-base / report pages."""
    for sub in ("knowledge-base", "reports"):
        d = os.path.join(built_site, sub)
        if not os.path.isdir(d):
            continue
        for p in _all_html(d):
            assert BANNER not in _read(p), f"banner leaked onto {p}"


def test_findings_count_matches_registry(built_site):
    with open(os.path.join(REPO_ROOT, "core-data", "findings.json"),
              encoding="utf-8") as fh:
        findings = json.load(fh)
    n = len(findings)

    html = _read(os.path.join(built_site, "data", "findings.html"))
    # Header count, e.g. "Findings (26)".
    m = re.search(r"Findings \((\d+)\)", html)
    assert m, "findings count header not found"
    assert int(m.group(1)) == n, f"header says {m.group(1)}, registry has {n}"

    # Every finding id must appear as a table-row anchor.
    for f in findings:
        fid = f.get("id")
        if fid:
            assert f'id="{fid}"' in html, f"finding {fid} missing from table"


def _resolve_links(html_path: str) -> list[str]:
    """Return the list of BROKEN local links found in one html file."""
    base = os.path.dirname(html_path)
    html = _read(html_path)
    broken = []
    for href in re.findall(r'(?:href|src)="([^"]+)"', html):
        if href.startswith(("http://", "https://", "mailto:", "#", "data:", "//")):
            continue
        target = href.split("#", 1)[0]
        if not target:
            continue
        full = os.path.normpath(os.path.join(base, target))
        if not os.path.exists(full):
            broken.append(href)
    return broken


def test_index_internal_links_resolve(built_site):
    broken = _resolve_links(os.path.join(built_site, "index.html"))
    assert not broken, f"broken links in index.html: {broken}"


def test_sidebar_links_resolve(built_site):
    """Sidebar is identical across pages; check it from a deep page too."""
    # Sample a handful of pages at different depths; their sidebars must all
    # have resolvable links.
    samples = [
        "index.html",
        "data/findings.html",
        "calculations.html",
    ]
    deep = os.path.join(built_site, "knowledge-base", "vypocty")
    if os.path.isdir(deep):
        for fn in sorted(os.listdir(deep)):
            if fn.endswith(".html"):
                samples.append(os.path.join("knowledge-base", "vypocty", fn))
                break

    for route in samples:
        path = os.path.join(built_site, route)
        if not os.path.isfile(path):
            continue
        # Extract just the <nav class="sidebar"> block and check its links.
        html = _read(path)
        m = re.search(r'<nav class="sidebar".*?</nav>', html, re.DOTALL)
        assert m, f"no sidebar in {route}"
        base = os.path.dirname(path)
        for href in re.findall(r'href="([^"]+)"', m.group(0)):
            if href.startswith(("http", "#", "mailto", "data:")):
                continue
            target = href.split("#", 1)[0]
            full = os.path.normpath(os.path.join(base, target))
            assert os.path.exists(full), f"broken sidebar link {href} on {route}"


def test_no_broken_links_anywhere(built_site):
    """Stronger guarantee: best-effort, no broken internal links site-wide."""
    offenders = {}
    for p in _all_html(built_site):
        broken = _resolve_links(p)
        if broken:
            offenders[os.path.relpath(p, built_site)] = broken
    assert not offenders, f"broken internal links: {offenders}"


def test_math_delimiters_preserved(built_site):
    """KaTeX delimiters survive markdown; no placeholder leakage."""
    formulas = _read(os.path.join(built_site, "data", "formulas.html"))
    assert "$$" in formulas, "display-math delimiters missing on formulas page"
    assert "MATHPROTECT" not in formulas, "math placeholder leaked into output"
    assert "auto-render.min.js" in formulas, "KaTeX auto-render not loaded"


def test_markdown_body_is_real_html_not_escaped(built_site):
    """Guard against jinja2 autoescaping mangling the rendered markdown body.

    A regression here would emit ``&lt;h1&gt;`` instead of ``<h1>`` for every
    prose page (and the sidebar), silently breaking the whole site.
    """
    index_path = os.path.join(built_site, "knowledge-base", "00-INDEX.html")
    if not os.path.isfile(index_path):
        pytest.skip("knowledge-base/00-INDEX page not present")
    html = _read(index_path)
    # The prose must contain a real heading element, not an escaped one.
    assert "<h1" in html, "prose body did not render real <h1>"
    assert "&lt;h1" not in html, "prose body was HTML-escaped (autoescape leak)"
    # The sidebar must be real markup, not escaped text.
    assert '<nav class="sidebar"' in html
    assert "&lt;ul&gt;" not in html, "sidebar was HTML-escaped (autoescape leak)"


def test_registry_json_links_route_to_pages(built_site):
    """Links to the four core-data registries resolve to their built pages."""
    index_path = os.path.join(built_site, "knowledge-base", "00-INDEX.html")
    if not os.path.isfile(index_path):
        pytest.skip("00-INDEX not present")
    html = _read(index_path)
    hrefs = re.findall(r'href="([^"]+)"', html)
    # findings.json is linked from the index; its HREF must point at the built
    # registry page, and no HREF may still point at the raw .json source.
    assert any(h.endswith("data/findings.html") for h in hrefs), \
        "findings registry link not rerouted to its page"
    assert not any("core-data/findings.json" in h for h in hrefs), \
        "an href still points at the raw registry .json source"


def test_calculations_gallery_has_cards_and_plots(built_site):
    html = _read(os.path.join(built_site, "calculations.html"))
    assert "calc-card" in html, "no calculation cards rendered"
    # At least one plot image points into the copied assets tree.
    m = re.search(r'src="((?:\.\./)*assets/[^"]+\.png)"', html)
    assert m, "no plot asset referenced on calculations page"
    base = os.path.join(built_site)
    target = os.path.normpath(os.path.join(base, m.group(1)))
    assert os.path.exists(target), f"plot asset missing on disk: {m.group(1)}"


# --------------------------------------------------------------------------
# Regression guards for the adversarial-review fixes
# --------------------------------------------------------------------------


def _sidebar_of(html: str) -> str:
    m = re.search(r'<nav class="sidebar".*?</nav>', html, re.DOTALL)
    assert m, "no sidebar block found"
    return m.group(0)


def test_fenced_code_renders_as_pre_code_not_literal_backticks(built_site):
    """Blocker regression: ``` fences must become real <pre><code> blocks.

    Previously mdrender restored the raw fence text into the already-rendered
    HTML, so triple-backtick fences survived verbatim inside <p> tags. Assert
    site-wide that (a) no literal ``` delimiter leaks into any page, (b) the
    placeholder sentinels never leak, (c) heavily-fenced pages carry the
    expected number of real code blocks, and (d) no invalid <p><pre> nesting.
    """
    pages = list(_all_html(built_site))
    assert pages, "no pages built"

    pre_total = 0
    for p in pages:
        html = _read(p)
        rel = os.path.relpath(p, built_site)
        assert "```" not in html, f"raw ``` fence leaked into {rel}"
        assert "MATHPROTECT" not in html, f"math placeholder leaked into {rel}"
        assert "CODEPROTECT" not in html, f"code placeholder leaked into {rel}"
        # A <pre> may never be wrapped in a <p> (browser would break the DOM).
        assert "<p><pre" not in html, f"invalid <p><pre> nesting in {rel}"
        pre_total += html.count("<pre><code")

    # The corpus has ~90 fenced blocks across 34 pages; require a healthy floor
    # so a future regression that drops fence rendering can't pass silently.
    assert pre_total >= 60, f"only {pre_total} <pre><code> blocks site-wide"

    # The three most fence-heavy pages must each carry their real code blocks.
    expectations = {
        "lib/architecture.html": 10,
        "knowledge-base/hypotezy/H01-gamma-cardy.html": 9,
        "lib/index.html": 8,
    }
    for route, n in expectations.items():
        path = os.path.join(built_site, *route.split("/"))
        if not os.path.isfile(path):
            continue
        count = _read(path).count("<pre><code")
        assert count >= n, f"{route}: {count} code blocks, expected >= {n}"


def test_no_raw_latex_dollars_in_sidebar_nav(built_site):
    """Major regression: titles with inline LaTeX must not leak ``$`` into nav.

    KaTeX auto-render is scoped to <main>; the sidebar nav is never rendered,
    so a ``$...$`` in a page title surfaced as literal dollar signs. Titles are
    now flattened to plain text for nav/breadcrumb/<title> contexts.
    """
    sampled = 0
    for p in _all_html(built_site):
        sidebar = _sidebar_of(_read(p))
        rel = os.path.relpath(p, built_site)
        assert "$" not in sidebar, f"raw $ (LaTeX) leaked into sidebar of {rel}"
        # The specific offenders flagged in review must be flattened.
        assert "\\sim" not in sidebar, f"raw LaTeX command in sidebar of {rel}"
        assert "\\text{" not in sidebar, f"raw LaTeX command in sidebar of {rel}"
        sampled += 1
    assert sampled >= 80, f"only sampled {sampled} sidebars"


def test_formula_math_has_no_escaped_entities(built_site):
    """Major regression: ``$$`` math must carry raw operators, not entities.

    The formulas template injected JSON latex under jinja2 autoescape, turning
    ``>``/``<`` into ``&gt;``/``&lt;`` *inside* the math delimiters. Assert the
    formula-math blocks now hold raw comparison operators and zero escaped
    entities, while at least one truly uses ``<`` or ``>``.
    """
    html = _read(os.path.join(built_site, "data", "formulas.html"))
    maths = re.findall(r'<div class="formula-math">(.*?)</div>', html, re.DOTALL)
    assert maths, "no formula-math blocks found"
    for m in maths:
        assert "&gt;" not in m, "escaped &gt; inside $$ math"
        assert "&lt;" not in m, "escaped &lt; inside $$ math"
        assert "&amp;" not in m, "escaped &amp; inside $$ math"
    # At least one formula legitimately needs a raw comparison operator.
    assert any("<" in m or ">" in m for m in maths), \
        "expected at least one formula with a raw < or > operator"


# --------------------------------------------------------------------------
# Concept-graph (force-directed) view
# --------------------------------------------------------------------------


def test_graph_page_and_data_exist(built_site):
    """The interactive graph page and its JSON data payload must be emitted."""
    assert os.path.isfile(os.path.join(built_site, "data", "graph.html"))
    assert os.path.isfile(
        os.path.join(built_site, "assets", "graph-data.json")
    )


def test_graph_data_node_count_matches_concept_graph(built_site):
    """graph-data.json node count must equal concept-graph.json node count."""
    with open(os.path.join(REPO_ROOT, "core-data", "concept-graph.json"),
              encoding="utf-8") as fh:
        cg = json.load(fh)
    n_nodes = len(cg.get("nodes", []))

    with open(os.path.join(built_site, "assets", "graph-data.json"),
              encoding="utf-8") as fh:
        payload = json.load(fh)
    assert payload["nodeCount"] == n_nodes
    assert len(payload["nodes"]) == n_nodes


def test_graph_data_includes_predicted_edges(built_site):
    """The top predicted candidate edges are present and marked predicted."""
    pred_path = os.path.join(REPO_ROOT, "core-data", "link-predictions.json")
    if not os.path.isfile(pred_path):
        pytest.skip("link-predictions.json not generated")
    with open(pred_path, encoding="utf-8") as fh:
        preds = json.load(fh)
    n_pred = len(preds.get("candidates", []))

    with open(os.path.join(built_site, "assets", "graph-data.json"),
              encoding="utf-8") as fh:
        payload = json.load(fh)
    predicted = [l for l in payload["links"] if l.get("predicted")]
    assert predicted, "no predicted edges in payload"
    assert len(predicted) == n_pred, (
        f"{len(predicted)} predicted edges, registry has {n_pred}"
    )
    # Predicted edges carry the distinct 'predicted' explored sentinel.
    for l in predicted:
        assert l.get("explored") == "predicted"


def test_graph_page_references_cdn_and_data_file(built_site):
    """The page loads the 3D force-graph CDN lib and points at its data file."""
    html = _read(os.path.join(built_site, "data", "graph.html"))
    assert "unpkg.com/3d-force-graph" in html, "3d-force-graph CDN not referenced"
    assert "graph-data.json" in html, "graph data file not referenced"
    # The data href must be RELATIVE (file:// + subpath safe), never absolute.
    m = re.search(r'DATA_URL = "([^"]+)"', html)
    assert m, "DATA_URL not found in page"
    href = m.group(1)
    assert not href.startswith("/"), f"data href is absolute: {href}"
    assert not href.startswith("http"), f"data href is absolute: {href}"
    # And it must resolve to the real file on disk from the page's directory.
    page_dir = os.path.join(built_site, "data")
    assert os.path.exists(os.path.normpath(os.path.join(page_dir, href)))


def test_graph_page_in_sidebar(built_site):
    """The graph page is wired into the Data section of the sidebar."""
    html = _read(os.path.join(built_site, "index.html"))
    sidebar = _sidebar_of(html)
    assert "data/graph.html" in sidebar, "graph page missing from sidebar"


def test_graph_modal_and_payload_maps(built_site):
    """The graph page exposes a modal element and the payload carries the
    self-contained formulas/references maps + per-node formulaIds."""
    html = _read(os.path.join(built_site, "data", "graph.html"))
    # The side panel is now a centered modal opened on node-click.
    assert 'id="graph-modal"' in html, "graph modal element missing"
    assert "gm-formulas-section" in html, "modal formulas section missing"
    # KaTeX must be loaded on the (math=False) graph page for the modal render.
    assert "katex.min.js" in html, "KaTeX not loaded on graph page"
    # Dismissable via Escape.
    assert "Escape" in html, "modal Escape handler missing"

    with open(os.path.join(built_site, "assets", "graph-data.json"),
              encoding="utf-8") as fh:
        payload = json.load(fh)
    # Self-contained lookups for the modal.
    assert isinstance(payload.get("formulas"), dict) and payload["formulas"], \
        "payload formulas map missing/empty"
    assert isinstance(payload.get("references"), dict) and payload["references"], \
        "payload references map missing/empty"
    # At least one node carries non-empty formulaIds, and each id resolves in
    # the formulas map; resolved refSlugs resolve in the references map.
    with_formulas = [n for n in payload["nodes"] if n.get("formulaIds")]
    assert with_formulas, "no node has a non-empty formulaIds list"
    sample = with_formulas[0]
    for fid in sample["formulaIds"]:
        assert fid in payload["formulas"], f"formula {fid} not in formulas map"
        slug = payload["formulas"][fid].get("refSlug")
        if slug is not None:
            assert slug in payload["references"], \
                f"refSlug {slug} not in references map"


def test_graph_payload_has_derivation_depth_axis(built_site):
    """The 3D view's Z axis: every node carries a depth in [0,1] + a band index,
    and the payload exposes the depth-band labels and their provenance."""
    with open(os.path.join(built_site, "assets", "graph-data.json"),
              encoding="utf-8") as fh:
        payload = json.load(fh)

    bands = payload.get("depthBands")
    assert isinstance(bands, list) and bands, "depthBands metadata missing"
    n_bands = len(bands)
    assert payload.get("depthSource") in ("override", "provisional-heuristic")

    layers_seen = set()
    for n in payload["nodes"]:
        d = n.get("depth")
        assert isinstance(d, (int, float)) and 0.0 <= d <= 1.0, \
            f"node {n['id']} depth out of range: {d!r}"
        lay = n.get("layer")
        assert isinstance(lay, int) and 0 <= lay < n_bands, \
            f"node {n['id']} layer out of range: {lay!r}"
        layers_seen.add(lay)
    # A meaningful stratification actually uses several distinct bands.
    assert len(layers_seen) >= 3, f"depth collapsed into {len(layers_seen)} band(s)"


def test_graph_page_is_3d_with_depth_controls(built_site):
    """The graph page is the 3D app: Three.js force-graph + depth-mode control."""
    html = _read(os.path.join(built_site, "data", "graph.html"))
    assert "ForceGraph3D" in html, "3D graph constructor not used"
    assert 'id="g3d-depthmode"' in html, "depth-mode control missing"
    assert 'id="g3d-fs"' in html, "fullscreen control missing"
    # The node-click modal must live INSIDE the stage so it shows in fullscreen:
    # the stage opens before the modal, and the muted help <p> closes after both.
    assert 'id="graph-modal"' in html
    assert html.index('class="g3d-stage"') < html.index('id="graph-modal"') \
        < html.index('<p class="muted"'), \
        "modal must be nested inside the 3D stage (for fullscreen rendering)"


def test_formulas_page_is_a_tree_with_reference_links(built_site):
    """The formulas registry is rendered as a <details> tree with at least one
    click-through reference link, and every formula carries a deep-link anchor."""
    html = _read(os.path.join(built_site, "data", "formulas.html"))
    # Collapsible tree structure (pillar -> concept) via <details>/<summary>.
    assert "<details" in html, "formulas page is not a <details> tree"
    assert 'class="ft-pillar"' in html, "pillar tree group missing"
    # At least one resolved reference rendered as a click-through link.
    assert re.search(r'<a href="https?://[^"]+" target="_blank"', html), \
        "no reference click-through link on formulas page"
    # Per-formula deep-link anchors for the graph modal / cross-page links.
    assert 'id="formula-' in html, "per-formula anchor id missing"
    # KaTeX still renders the math.
    assert "$$" in html, "display-math delimiters missing on formulas tree"


def test_no_absolute_machine_paths_in_artifact(built_site):
    """Minor regression: the dev machine path must not leak into the artifact.

    Absolute on-disk repo-root paths (in command examples and file references)
    are stripped to repo-relative at build time so the public output never
    carries the author's local filesystem layout.
    """
    needle = os.path.join(REPO_ROOT, "")  # repo root with trailing sep
    leakers = {}
    for p in _all_html(built_site):
        html = _read(p)
        if REPO_ROOT in html or needle in html:
            leakers[os.path.relpath(p, built_site)] = True
    assert not leakers, f"absolute machine path leaked into: {sorted(leakers)}"
