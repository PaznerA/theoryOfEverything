#!/usr/bin/env python3
"""Theory of Everything — minimalist static-site builder.

Builds a *presentation view* of the repository directly from its existing
markdown files and JSON registries. The site is never a copy that can drift:
markdown + JSON registries are the single source of truth; every run deletes
``web/dist/`` and rebuilds it deterministically.

Usage
-----
    python web/build.py [--out DIR]

Pure python: python-markdown + jinja2 + a single hand-written CSS file. Math is
rendered in the browser by KaTeX (loaded from CDN). No node, no JS build chain.
All output links are relative, so the site works from ``file://`` and from
``python -m http.server``.
"""

from __future__ import annotations

import argparse
import datetime
import os
import shutil
import sys

# Make ``web/builder`` importable whether run as ``python web/build.py`` or
# from inside the repo root.
HERE = os.path.dirname(os.path.abspath(__file__))
REPO_ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)

from jinja2 import Environment, FileSystemLoader, select_autoescape  # noqa: E402

from builder import data as datamod  # noqa: E402
from builder import mdrender, sitemap  # noqa: E402
from builder.mdrender import DEAD  # noqa: E402

TEMPLATES_DIR = os.path.join(HERE, "templates")
STATIC_DIR = os.path.join(HERE, "static")
DEFAULT_OUT = os.path.join(HERE, "dist")

BUILD_DATE = datetime.date.today().isoformat()


# --------------------------------------------------------------------------
# Internal-link rewriting
# --------------------------------------------------------------------------


class LinkResolver:
    """Rewrites repo-relative markdown links to built ``.html`` routes.

    Best-effort: external (http/https/mailto) links and anchors are untouched;
    links into ``core-data/calculations`` PNGs are pointed at the copied
    assets; the four core-data registries are pointed at their generated
    registry pages. Repo links with NO corresponding page or asset (raw
    ``.json``/``.bib``/``.py`` source, intentionally-skipped files, stale
    references) cannot be served from ``dist/``, so the resolver returns the
    sentinel :data:`DEAD` and the link is unwrapped to plain text — the site
    stays self-contained and works identically from ``file://`` and http.
    """

    #: repo-relative source files that map to a generated registry page.
    REGISTRY_PAGES = {
        "core-data/findings.json": "data/findings.html",
        "core-data/connections.json": "data/connections.html",
        "core-data/formulas.json": "data/formulas.html",
        "core-data/open-problems.json": "data/open-problems.html",
    }

    def __init__(self, page_src: str | None, page_route: str,
                 route_set: set[str], asset_map: dict[str, str]):
        self.page_src = page_src
        self.page_route = page_route
        self.route_set = route_set
        self.asset_map = asset_map  # repo_rel_png -> dist asset route

    def __call__(self, href: str) -> str:
        if not href or href.startswith(("http://", "https://", "mailto:",
                                        "#", "data:", "//")):
            return href

        # Split off any anchor fragment.
        anchor = ""
        if "#" in href:
            href, anchor = href.split("#", 1)
            anchor = "#" + anchor
        if not href:
            return anchor or "#"

        # Resolve relative to the source file's directory, into a repo-rel path.
        repo_rel = self._to_repo_rel(href)
        if repo_rel is None:
            # Escapes above repo root: cannot exist in dist -> unwrap.
            return DEAD

        repo_rel_norm = repo_rel.replace(os.sep, "/")

        # Image / plot asset?
        if repo_rel_norm in self.asset_map:
            return sitemap.relpath(self.page_route, self.asset_map[repo_rel_norm]) + anchor

        # Known registry source file -> its generated registry page.
        if repo_rel_norm in self.REGISTRY_PAGES:
            return sitemap.relpath(self.page_route,
                                   self.REGISTRY_PAGES[repo_rel_norm]) + anchor

        # Markdown -> route mapping.
        target_route = self._route_for(repo_rel_norm)
        if target_route and target_route in self.route_set:
            return sitemap.relpath(self.page_route, target_route) + anchor

        # Speculative .md -> .html even if that page was not built.
        if repo_rel_norm.endswith(".md"):
            guess = repo_rel_norm[:-3] + ".html"
            if guess in self.route_set:
                return sitemap.relpath(self.page_route, guess) + anchor

        # No page and no asset exists for this repo path (raw source file,
        # skipped file, or stale/renamed reference). It cannot be served from
        # dist/, so signal the renderer to unwrap the anchor to plain text
        # rather than emit a link that 404s from file:// and http alike.
        return DEAD

    def _to_repo_rel(self, href: str) -> str | None:
        base_dir = os.path.dirname(self.page_src) if self.page_src else ""
        combined = os.path.normpath(os.path.join(base_dir, href))
        # Reject escapes above repo root.
        if combined.startswith(".."):
            return None
        return combined

    @staticmethod
    def _route_for(repo_rel_norm: str) -> str | None:
        if repo_rel_norm in sitemap.SINGLE_MARKDOWN:
            return sitemap.SINGLE_MARKDOWN[repo_rel_norm]
        if repo_rel_norm.endswith(".md"):
            return repo_rel_norm[:-3] + ".html"
        return None


# --------------------------------------------------------------------------
# Sidebar generation
# --------------------------------------------------------------------------

SECTION_LABELS = {
    "home": "Domů",
    "progress": "PROGRESS",
    "knowledge-base": "Knowledge base",
    "reports": "Reporty",
    "verification": "Verifikace",
    "papers": "Drafty (papers)",
    "lib": "Knihovna lib/",
    "app": "Prostředí app/",
    "data": "Registry (data)",
    "calculations": "Výpočty",
}

SECTION_ORDER = [
    "home", "progress", "data", "calculations",
    "knowledge-base", "papers", "reports", "verification", "lib", "app",
]


def build_sidebar(pages: list[sitemap.Page], current_route: str) -> str:
    """Render the single sidebar as nested HTML, grouped by section + subdir."""
    by_section: dict[str, list[sitemap.Page]] = {}
    for p in pages:
        by_section.setdefault(p.section, []).append(p)

    def href(route: str) -> str:
        return sitemap.relpath(current_route, route)

    parts: list[str] = ["<ul>"]

    # Fixed top entries.
    parts.append(_li("index.html", "Domů", current_route, href))

    # Registry data group.
    if "data" in by_section:
        parts.append('<li><details open><summary>Registry (data)</summary><ul class="nested">')
        for p in sorted(by_section["data"], key=lambda x: x.route):
            parts.append(_li(p.route, p.title, current_route, href))
        parts.append("</ul></details></li>")

    parts.append(_li("calculations.html", "Galerie výpočtů", current_route, href))
    parts.append(_li("progress.html", "PROGRESS", current_route, href))

    # Tree-structured markdown sections.
    for section in ["knowledge-base", "papers", "reports", "verification", "lib", "app"]:
        sec_pages = by_section.get(section)
        if not sec_pages:
            continue
        label = SECTION_LABELS.get(section, section)
        is_open = current_route.startswith(section + "/")
        parts.append(
            f'<li><details{" open" if is_open else ""}>'
            f"<summary>{label}</summary>"
            f'<ul class="nested">'
        )
        parts.append(_render_tree(sec_pages, section, current_route, href))
        parts.append("</ul></details></li>")

    parts.append("</ul>")
    return "".join(parts)


def _li(route: str, label: str, current_route: str, href) -> str:
    cls = ' class="current"' if route == current_route else ""
    return f'<li><a{cls} href="{href(route)}">{_esc(label)}</a></li>'


def _render_tree(sec_pages, section, current_route, href) -> str:
    """Render one section's pages, grouping by their immediate subdirectory."""
    prefix = section + "/"
    direct: list[sitemap.Page] = []
    subgroups: dict[str, list[sitemap.Page]] = {}
    for p in sorted(sec_pages, key=lambda x: x.route):
        rest = p.route[len(prefix):] if p.route.startswith(prefix) else p.route
        if "/" in rest:
            sub = rest.split("/", 1)[0]
            subgroups.setdefault(sub, []).append(p)
        else:
            direct.append(p)

    out: list[str] = []
    for p in direct:
        out.append(_li(p.route, p.title, current_route, href))
    for sub in sorted(subgroups):
        group = subgroups[sub]
        is_open = current_route.startswith(prefix + sub + "/")
        out.append(
            f'<li><details{" open" if is_open else ""}>'
            f"<summary>{_esc(sub)}</summary>"
            f'<ul class="nested">'
        )
        for p in sorted(group, key=lambda x: x.route):
            out.append(_li(p.route, p.title, current_route, href))
        out.append("</ul></details></li>")
    return "".join(out)


def _esc(s: str) -> str:
    return (s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;"))


# --------------------------------------------------------------------------
# Breadcrumbs
# --------------------------------------------------------------------------


def breadcrumbs_for(route: str) -> list[dict]:
    if route == "index.html":
        return []
    crumbs = [{"label": "Domů", "href": _rel(route, "index.html")}]
    parts = route.split("/")
    acc = ""
    for i, part in enumerate(parts):
        acc = part if not acc else acc + "/" + part
        last = i == len(parts) - 1
        label = part[:-5] if part.endswith(".html") else part
        if last:
            crumbs.append({"label": label, "href": None})
        else:
            crumbs.append({"label": label, "href": None})
    return crumbs


def _rel(from_route: str, to_route: str) -> str:
    return sitemap.relpath(from_route, to_route)


# --------------------------------------------------------------------------
# Build
# --------------------------------------------------------------------------


def _write(out_dir: str, route: str, html: str) -> None:
    path = os.path.join(out_dir, route)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(html)


def build(out_dir: str = DEFAULT_OUT, verbose: bool = True) -> int:
    """Build the whole site into ``out_dir``. Returns the page count."""
    # 1. Clean.
    if os.path.exists(out_dir):
        shutil.rmtree(out_dir)
    os.makedirs(out_dir)

    env = Environment(
        loader=FileSystemLoader(TEMPLATES_DIR),
        autoescape=select_autoescape(["html"]),
        trim_blocks=True,
        lstrip_blocks=True,
    )
    # LaTeX injected straight into a ``$$...$$`` block (the formulas registry)
    # must keep its raw comparison operators (``<``, ``>``): jinja2 autoescape
    # would turn them into ``&lt;``/``&gt;`` in the *source*, which both
    # violates the "no escaped entities in source" guarantee and diverges from
    # how the prose pipeline (mdrender) emits math. This filter preserves the
    # raw delimiters exactly as the markdown math-protection path does.
    env.filters["mathraw"] = mdrender.math_markup

    # 2. Copy static CSS.
    os.makedirs(os.path.join(out_dir, "static"), exist_ok=True)
    shutil.copy2(
        os.path.join(STATIC_DIR, "style.css"),
        os.path.join(out_dir, "static", "style.css"),
    )

    # 3. Discover markdown pages.
    md_sources = sitemap.discover_markdown(REPO_ROOT)
    pages: list[sitemap.Page] = []
    for repo_rel, route in md_sources:
        with open(os.path.join(REPO_ROOT, repo_rel), encoding="utf-8") as fh:
            text = fh.read()
        fallback = os.path.splitext(os.path.basename(repo_rel))[0]
        title = mdrender.extract_title(text, fallback)
        is_paper = repo_rel.replace(os.sep, "/").startswith("papers/")
        pages.append(sitemap.Page(
            src=repo_rel, route=route, title=title,
            section=sitemap.section_of(route), is_paper=is_paper, md_text=text,
        ))

    # 4. Generated pages (home + registries + calculations).
    home = sitemap.Page(src="README.md", route="index.html",
                        title="Domů", section="home")
    with open(os.path.join(REPO_ROOT, "README.md"), encoding="utf-8") as fh:
        home.md_text = fh.read()
    pages.append(home)

    generated_routes = {
        "data/findings.html": "Findings",
        "data/connections.html": "Souvislosti",
        "data/formulas.html": "Vzorce",
        "data/open-problems.html": "Otevřené problémy",
        "data/graph.html": "Graf konceptů",
        "calculations.html": "Galerie výpočtů",
    }
    for route, title in generated_routes.items():
        pages.append(sitemap.Page(src=None, route=route, title=title,
                                  section=sitemap.section_of(route)))

    route_set = {p.route for p in pages}

    # 5. Copy calculation plots into dist/assets and build the asset map.
    calcs = datamod.discover_calculations(REPO_ROOT)
    asset_map: dict[str, str] = {}
    all_png: set[str] = set()
    for c in calcs:
        for png in c["plots"]:
            all_png.add(png)
    for png in sorted(all_png):
        asset_route = "assets/" + png.replace("core-data/calculations/", "")
        asset_route = asset_route.replace(os.sep, "/")
        asset_map[png] = asset_route
        dst = os.path.join(out_dir, asset_route)
        os.makedirs(os.path.dirname(dst), exist_ok=True)
        shutil.copy2(os.path.join(REPO_ROOT, png), dst)

    stats = datamod.dashboard_stats(REPO_ROOT)
    page_count_holder = {"n": len(pages)}

    def common_ctx(page: sitemap.Page, math: bool) -> dict:
        return {
            "title": page.title,
            "rel": lambda r, _pr=page.route: sitemap.relpath(_pr, r),
            "sidebar": build_sidebar(pages, page.route),
            "breadcrumbs": breadcrumbs_for(page.route),
            "is_paper": page.is_paper,
            "source_path": page.src,
            "math": math,
            "build_date": BUILD_DATE,
            "page_count": page_count_holder["n"],
        }

    # 6. Render markdown pages.
    page_tpl = env.get_template("page.html")
    home_tpl = env.get_template("home.html")
    for page in pages:
        if page.md_text is None:
            continue
        resolver = LinkResolver(page.src, page.route, route_set, asset_map)
        body = mdrender.render(page.md_text, link_rewriter=resolver,
                               repo_root=REPO_ROOT)
        ctx = common_ctx(page, math=True)
        ctx["body"] = body
        if page.route == "index.html":
            ctx["stats"] = stats
            html = home_tpl.render(**ctx)
        else:
            html = page_tpl.render(**ctx)
        _write(out_dir, page.route, html)

    # 7. Registry + gallery pages.
    _render_registries(env, out_dir, pages, route_set, asset_map,
                       common_ctx, calcs)

    if verbose:
        print(f"Built {len(pages)} pages into {out_dir}")
        print(f"  markdown pages: {sum(1 for p in pages if p.md_text)}")
        print(f"  generated pages: {len(generated_routes)}")
        print(f"  plot assets copied: {len(asset_map)}")
    return len(pages)


def _page_by_route(pages, route):
    for p in pages:
        if p.route == route:
            return p
    raise KeyError(route)


def _render_registries(env, out_dir, pages, route_set, asset_map,
                       common_ctx, calcs):
    # --- findings ---
    findings = datamod.load_findings(REPO_ROOT)
    fpage = _page_by_route(pages, "data/findings.html")

    def evidence_href(e: str, _route="data/findings.html") -> str | None:
        norm = e.replace(os.sep, "/")
        if norm in asset_map:
            return sitemap.relpath(_route, asset_map[norm])
        guess = norm[:-3] + ".html" if norm.endswith(".md") else None
        if guess and guess in route_set:
            return sitemap.relpath(_route, guess)
        if norm in sitemap.SINGLE_MARKDOWN and sitemap.SINGLE_MARKDOWN[norm] in route_set:
            return sitemap.relpath(_route, sitemap.SINGLE_MARKDOWN[norm])
        return None

    ctx = common_ctx(fpage, math=False)
    ctx.update(findings=findings, status_class=datamod.status_class,
               evidence_href=evidence_href)
    _write(out_dir, fpage.route, env.get_template("findings.html").render(**ctx))

    # --- connections ---
    conns = datamod.load_connections(REPO_ROOT)
    groups: dict[str, list] = {r: [] for r in datamod.RATING_ORDER}
    for c in conns:
        groups.setdefault(c.get("explored", "barely"), []).append(c)
    cpage = _page_by_route(pages, "data/connections.html")
    ctx = common_ctx(cpage, math=False)
    ctx.update(groups=groups, total=len(conns),
               rating_order=datamod.RATING_ORDER,
               rating_label=datamod.RATING_LABEL,
               rating_desc=datamod.RATING_DESC)
    _write(out_dir, cpage.route,
           env.get_template("connections.html").render(**ctx))

    # --- formulas (tree: pillar -> concept -> formula, with ref click-through) ---
    formulas = datamod.load_formulas(REPO_ROOT)
    formula_tree = datamod.build_formula_tree(REPO_ROOT)
    fopage = _page_by_route(pages, "data/formulas.html")
    ctx = common_ctx(fopage, math=True)
    ctx.update(tree=formula_tree, formula_count=len(formulas))
    _write(out_dir, fopage.route,
           env.get_template("formulas.html").render(**ctx))

    # --- open problems (grouped by pillar) ---
    problems = datamod.load_open_problems(REPO_ROOT)
    pgroups: dict[str, list] = {}
    for p in problems:
        pillars = p.get("pillars") or ["(bez pilíře)"]
        for pillar in pillars:
            pgroups.setdefault(pillar, []).append(p)
    pillar_order = sorted(pgroups, key=lambda k: (-len(pgroups[k]), k))
    oppage = _page_by_route(pages, "data/open-problems.html")
    ctx = common_ctx(oppage, math=True)
    ctx.update(groups=pgroups, pillar_order=pillar_order, total=len(problems))
    _write(out_dir, oppage.route,
           env.get_template("open-problems.html").render(**ctx))

    # --- concept graph (force-directed view + its data payload) ---
    import json as _json

    payload = datamod.build_graph_payload(REPO_ROOT)
    payload_json = _json.dumps(payload, ensure_ascii=False)

    # Canonical JSON payload (consumed programmatically + by the test suite).
    data_route = "assets/graph-data.json"
    data_path = os.path.join(out_dir, data_route)
    os.makedirs(os.path.dirname(data_path), exist_ok=True)
    with open(data_path, "w", encoding="utf-8") as fh:
        fh.write(payload_json)

    # Browser loader: the SAME payload assigned to a global via a <script src>.
    # ``fetch()`` cannot read file:// URLs in modern browsers, so the page loads
    # the data with a plain <script> tag (the KaTeX pattern) -- this keeps the
    # view working from file:// AND under any subpath with only relative links.
    js_route = "assets/graph-data.js"
    js_path = os.path.join(out_dir, js_route)
    with open(js_path, "w", encoding="utf-8") as fh:
        fh.write("window.__TOE_GRAPH__ = " + payload_json + ";\n")

    gpage = _page_by_route(pages, "data/graph.html")
    ctx = common_ctx(gpage, math=False)
    # Relative hrefs from the graph page to its data files (file://-safe).
    ctx.update(
        data_href=sitemap.relpath(gpage.route, data_route),
        data_js_href=sitemap.relpath(gpage.route, js_route),
        node_count=payload["nodeCount"],
        edge_count=payload["edgeCount"],
        predicted=payload["predicted"],
        legend=payload["legend"],
    )
    _write(out_dir, gpage.route,
           env.get_template("graph.html").render(**ctx))

    # --- calculations gallery ---
    capage = _page_by_route(pages, "calculations.html")

    def asset_href(repo_png: str, _route="calculations.html") -> str:
        norm = repo_png.replace(os.sep, "/")
        if norm in asset_map:
            return sitemap.relpath(_route, asset_map[norm])
        return norm

    ctx = common_ctx(capage, math=False)
    ctx.update(calcs=calcs, asset_href=asset_href)
    _write(out_dir, capage.route,
           env.get_template("calculations.html").render(**ctx))


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--out", default=DEFAULT_OUT,
                        help="output directory (default: web/dist)")
    parser.add_argument("-q", "--quiet", action="store_true")
    args = parser.parse_args(argv)
    n = build(out_dir=os.path.abspath(args.out), verbose=not args.quiet)
    return 0 if n > 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
