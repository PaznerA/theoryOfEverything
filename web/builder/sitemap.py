"""Content map: discover source files and assign them deterministic routes.

The route of every page mirrors the repository file structure, so the site is a
transparent view of the repo. A markdown file at ``knowledge-base/approaches/
asymptotic-safety.md`` becomes ``knowledge-base/approaches/asymptotic-safety.html``.

This module is the single source of truth for *which* files become pages and
*where* they land, so both the page builder and the internal-link rewriter agree.
"""

from __future__ import annotations

import os
from dataclasses import dataclass, field

# Repo-relative directories whose ``*.md`` files become pages, recursively.
# The directory tree is preserved in the output routes.
MARKDOWN_TREES = [
    "knowledge-base",
    "reports",
    "verification",
    "papers",
]

# Single markdown files (repo-relative) that become top-level pages.
SINGLE_MARKDOWN = {
    "PROGRESS.md": "progress.html",
    "lib/README.md": "lib/index.html",
    "lib/toe/ARCHITECTURE.md": "lib/architecture.html",
    "app/README.md": "app/index.html",
}

# Files under papers/** that must carry the internal-draft banner.
PAPERS_PREFIX = "papers" + os.sep


@dataclass
class Page:
    """A single generated HTML page."""

    src: str | None           # repo-relative source path (None for generated)
    route: str                # site-relative output path, e.g. "data/findings.html"
    title: str
    section: str              # top-level grouping key for the sidebar
    is_paper: bool = False
    md_text: str | None = None
    meta: dict = field(default_factory=dict)

    @property
    def depth(self) -> int:
        return self.route.count("/")

    def rel_to(self, other_route: str) -> str:
        """Relative href from a page at ``other_route`` to this page's route."""
        return relpath(other_route, self.route)


def relpath(from_route: str, to_route: str) -> str:
    """Relative path from one site route to another (POSIX, file://-safe)."""
    from_dir = os.path.dirname(from_route)
    rel = os.path.relpath(to_route, from_dir or ".")
    return rel.replace(os.sep, "/")


def _route_for_md(repo_rel: str) -> str:
    """Map a repo-relative markdown path to its site route."""
    if repo_rel in SINGLE_MARKDOWN:
        return SINGLE_MARKDOWN[repo_rel]
    base, _ = os.path.splitext(repo_rel)
    return base + ".html"


def discover_markdown(repo_root: str) -> list[tuple[str, str]]:
    """Return (repo_rel_path, route) for every markdown page source."""
    found: list[tuple[str, str]] = []

    for tree in MARKDOWN_TREES:
        root = os.path.join(repo_root, tree)
        if not os.path.isdir(root):
            continue
        for dirpath, dirnames, filenames in os.walk(root):
            # Skip noise.
            dirnames[:] = [
                d for d in sorted(dirnames)
                if d not in {"__pycache__", "plots", ".git"}
            ]
            for fn in sorted(filenames):
                if not fn.endswith(".md"):
                    continue
                abspath = os.path.join(dirpath, fn)
                repo_rel = os.path.relpath(abspath, repo_root)
                found.append((repo_rel, _route_for_md(repo_rel)))

    for repo_rel, route in SINGLE_MARKDOWN.items():
        if os.path.isfile(os.path.join(repo_root, repo_rel)):
            found.append((repo_rel, route))

    # Deterministic order.
    found.sort(key=lambda t: t[1])
    return found


def section_of(route: str) -> str:
    """Top-level sidebar section key for a route."""
    head = route.split("/", 1)[0]
    if route == "index.html":
        return "home"
    if route == "progress.html":
        return "progress"
    if head in {"knowledge-base", "reports", "verification", "papers",
                "lib", "app", "data"}:
        return head
    if route == "calculations.html":
        return "calculations"
    return head
