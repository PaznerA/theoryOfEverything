"""Markdown -> HTML rendering with math protection and internal-link rewriting.

Two hard problems this module solves so the rest of the build stays trivial:

1. python-markdown happily mangles LaTeX (``$...$``, ``$$...$$``): underscores
   become ``<em>``, backslashes vanish, ``*`` becomes emphasis. We therefore
   *protect* every math span behind an opaque placeholder BEFORE markdown runs
   and restore the raw LaTeX AFTER, so KaTeX (loaded in the browser) receives
   pristine delimiters.

2. Internal repo links (``../core-data/findings.json``,
   ``./VYPOCET-01-...md``) must point at the generated ``.html`` routes, and
   bare arXiv ids should auto-link to arxiv.org. External ``http(s)`` links are
   left untouched.
"""

from __future__ import annotations

import html
import re
from typing import Callable

import markdown
from markupsafe import Markup

# --------------------------------------------------------------------------
# Math protection
# --------------------------------------------------------------------------
# Order matters: $$...$$ (display) must be matched before $...$ (inline).
# We deliberately do not try to be clever about escaped \$ inside prose — the
# corpus is scientific markdown where $ is always a math delimiter.
_DISPLAY_RE = re.compile(r"\$\$(.+?)\$\$", re.DOTALL)
_INLINE_RE = re.compile(r"(?<!\$)\$(?!\$)(.+?)(?<!\$)\$(?!\$)", re.DOTALL)

# Fenced/indented code must be shielded from math protection too, otherwise a
# stray ``$`` in a code block would be swallowed. We protect fenced code first.
# We capture the optional language hint (```python) and the body separately so
# that on restore we can emit a *real* ``<pre><code>`` element instead of
# dumping the raw backtick fence back into the rendered HTML (which python-
# markdown never sees, so it would otherwise survive verbatim as literal text).
_FENCE_RE = re.compile(
    r"```[ \t]*([A-Za-z0-9_+-]*)[ \t]*\r?\n(.*?)\r?\n[ \t]*```",
    re.DOTALL,
)

_PLACEHOLDER = "\x00MATHPROTECT{idx}\x00"
_PLACEHOLDER_RE = re.compile(r"\x00MATHPROTECT(\d+)\x00")
_CODE_PLACEHOLDER = "\x00CODEPROTECT{idx}\x00"
_CODE_PLACEHOLDER_RE = re.compile(r"\x00CODEPROTECT(\d+)\x00")


def _protect(text: str) -> tuple[str, list[str], list[str]]:
    """Replace code fences and math spans with placeholders.

    Returns the protected text plus the lists needed to restore each kind.
    """
    code_store: list[str] = []
    math_store: list[str] = []

    def _stash_code(m: re.Match) -> str:
        # Render the fence into a real ``<pre><code>`` block now, while we still
        # have the raw body. We store the finished HTML (not the markdown
        # fence) so that _restore_code reinserts genuine code markup instead of
        # literal triple-backtick text into the rendered page.
        lang, body = m.group(1), m.group(2)
        cls = f' class="language-{lang}"' if lang else ""
        code_store.append(
            f"<pre><code{cls}>{html.escape(body)}\n</code></pre>"
        )
        # Wrap the placeholder in blank lines so markdown always treats it as
        # its own block — even when the source fence is immediately followed by
        # prose with no separating blank line (otherwise the placeholder is
        # glued into that paragraph, yielding invalid ``<p><pre>`` nesting).
        return "\n\n" + _CODE_PLACEHOLDER.format(idx=len(code_store) - 1) + "\n\n"

    text = _FENCE_RE.sub(_stash_code, text)

    def _stash_math(m: re.Match) -> str:
        math_store.append(m.group(0))
        return _PLACEHOLDER.format(idx=len(math_store) - 1)

    # Display first, then inline on whatever remains.
    text = _DISPLAY_RE.sub(_stash_math, text)
    text = _INLINE_RE.sub(_stash_math, text)
    return text, math_store, code_store


def _restore_math(htmltext: str, math_store: list[str]) -> str:
    def _put(m: re.Match) -> str:
        return math_store[int(m.group(1))]

    return _PLACEHOLDER_RE.sub(_put, htmltext)


def _restore_code(text: str, code_store: list[str]) -> str:
    def _put(m: re.Match) -> str:
        return code_store[int(m.group(1))]

    # python-markdown wraps a standalone placeholder line in its own ``<p>``.
    # A block ``<pre>`` may not live inside ``<p>`` (the browser would close
    # the paragraph early, producing stray empty <p></p>), so unwrap the
    # paragraph when it contains nothing but the code placeholder.
    text = re.sub(
        r"<p>\s*(\x00CODEPROTECT\d+\x00)\s*</p>",
        r"\1",
        text,
    )
    return _CODE_PLACEHOLDER_RE.sub(_put, text)


# --------------------------------------------------------------------------
# arXiv auto-linking (operates on rendered HTML, outside of math/code)
# --------------------------------------------------------------------------
# New-style (1507.00330) and old-style (hep-th/0508202) arxiv ids, optionally
# prefixed with "arXiv:". We only touch bare occurrences in text nodes, so we
# run this on the final HTML but skip anything already inside a tag/href by
# requiring the id not to be immediately preceded by ``/`` or ``"``.
_ARXIV_RE = re.compile(
    r"(?<![\w/\".:])(?:arXiv:)?"
    r"((?:\d{4}\.\d{4,5})(?:v\d+)?|(?:[a-z-]+(?:\.[A-Z]{2})?/\d{7}))"
    r"(?![\w/])"
)


def _autolink_arxiv(htmltext: str) -> str:
    # Don't autolink inside existing anchor tags, code/pre blocks, or attribute
    # values. We split on tags so substitution only happens in text segments.
    # Code/pre must be skipped because fenced blocks are already real
    # ``<pre><code>`` markup by this point: an arXiv id printed in a command or
    # snippet is literal text, not a citation to hyperlink.
    parts = re.split(r"(<[^>]+>)", htmltext)
    out: list[str] = []
    in_anchor = False
    code_depth = 0
    for part in parts:
        if part.startswith("<"):
            low = part.lower()
            if low.startswith("<a "):
                in_anchor = True
            elif low.startswith("</a"):
                in_anchor = False
            elif low.startswith(("<code", "<pre")):
                code_depth += 1
            elif low.startswith(("</code", "</pre")):
                code_depth = max(0, code_depth - 1)
            out.append(part)
            continue
        if in_anchor or code_depth > 0 or "\x00" in part:
            out.append(part)
            continue
        out.append(
            _ARXIV_RE.sub(
                lambda m: (
                    f'<a href="https://arxiv.org/abs/{m.group(1)}" '
                    f'rel="external">{html.escape(m.group(0))}</a>'
                ),
                part,
            )
        )
    return "".join(out)


# --------------------------------------------------------------------------
# Internal link rewriting
# --------------------------------------------------------------------------


def math_markup(latex: str) -> Markup:
    """Return ``latex`` as safe markup with its raw math operators intact.

    The formulas registry injects LaTeX directly into a ``$$...$$`` block in
    the template. Under jinja2 autoescape, comparison operators (``<``, ``>``)
    would become ``&lt;``/``&gt;`` in the emitted source. KaTeX would still
    render them (it reads decoded DOM text), but the HTML *source* would carry
    escaped entities inside math delimiters — the very thing the prose pipeline
    avoids by protecting math from markdown. We mirror that here: only ``&`` is
    neutralised (so a literal ``&`` can never start a stray entity); ``<``/``>``
    stay raw, exactly as :func:`render` emits them for prose math.
    """
    return Markup((latex or "").replace("&", "&amp;"))


def make_md(extensions=None) -> markdown.Markdown:
    return markdown.Markdown(
        extensions=extensions or ["extra", "toc", "tables"],
        output_format="html5",
    )


def render(
    text: str,
    link_rewriter: Callable[[str], str] | None = None,
    repo_root: str | None = None,
) -> str:
    """Render markdown ``text`` to an HTML fragment.

    ``link_rewriter`` maps a raw href found in the source markdown to its final
    relative href in the built site (or returns it unchanged for externals).

    ``repo_root`` (if given) is stripped from any absolute on-disk paths that
    survive into the rendered prose / code blocks, so the *public artifact*
    never leaks the developer machine path (``/Users/.../theoryOfEverything``).
    The source markdown stays untouched — it remains the single source of
    truth; only the built HTML is sanitised.
    """
    text = _sanitize_paths(text, repo_root)
    protected, math_store, code_store = _protect(text)

    md = make_md()
    out = md.convert(protected)

    out = _restore_code(out, code_store)
    out = _drop_orphan_fences(out)
    if link_rewriter is not None:
        out = _rewrite_links(out, link_rewriter)
    out = _autolink_arxiv(out)
    out = _restore_math(out, math_store)
    return out


# An *unbalanced* ``` line in the source (a closing fence with no opener — a
# data typo) is not matched by _FENCE_RE and so survives markdown as a literal
# backtick artifact. Two shapes occur: a fence on its own line becomes
# ``<p>```</p>``; a fence right after prose is glued onto that paragraph as
# ``...text\n```</p>``. Strip the stray fence in both shapes so no raw ```
# delimiter ever reaches the page. Well-formed fences are already real
# <pre><code> by this point (their backticks were consumed) and are untouched.
_ORPHAN_FENCE_SOLO_RE = re.compile(r"<p>\s*`{3,}\s*</p>")
_ORPHAN_FENCE_TAIL_RE = re.compile(r"\n`{3,}[ \t]*(</p>)")


def _drop_orphan_fences(htmltext: str) -> str:
    htmltext = _ORPHAN_FENCE_SOLO_RE.sub("", htmltext)
    htmltext = _ORPHAN_FENCE_TAIL_RE.sub(r"\1", htmltext)
    return htmltext


def _sanitize_paths(text: str, repo_root: str | None) -> str:
    """Replace absolute ``repo_root`` paths with repo-relative ones.

    ``<root>/core-data/x`` -> ``core-data/x`` and a bare ``<root>`` -> ``.`` so
    shell snippets like ``cd <root>`` read as ``cd .``. Operates on the raw
    markdown (before protection) so it reaches text, inline code and fenced
    blocks alike.
    """
    if not repo_root:
        return text
    root = repo_root.rstrip("/")
    text = text.replace(root + "/", "")
    # Bare root with no trailing component (e.g. ``cd <root>``): use ``.``.
    text = re.sub(re.escape(root) + r"(?![\w/])", ".", text)
    return text


# Sentinel: a rewriter returns this when the target has no servable
# destination in the built site. The whole anchor is then unwrapped to its
# inner text so the page carries no broken link.
DEAD = "\x00DEADLINK\x00"

# Full anchors (so we can unwrap dead ones), then bare img src attributes.
_ANCHOR_RE = re.compile(
    r'<a\b([^>]*?)\bhref="([^"]*)"([^>]*)>(.*?)</a>',
    re.IGNORECASE | re.DOTALL,
)
_SRC_RE = re.compile(r'(<img\b[^>]*?\bsrc=")([^"]*)(")', re.IGNORECASE)


def _rewrite_links(htmltext: str, rewriter: Callable[[str], str]) -> str:
    def _anchor(m: re.Match) -> str:
        pre, href, post, inner = m.groups()
        new = rewriter(href)
        if new is DEAD or new == DEAD:
            # Unwrap to plain text: keep the (markdown-rendered) inner content.
            return inner
        return f'<a{pre}href="{new}"{post}>{inner}</a>'

    def _src(m: re.Match) -> str:
        new = rewriter(m.group(2))
        if new is DEAD or new == DEAD:
            # An image with no asset: drop to an empty src is worse than a
            # broken file ref, so just keep the original (rare; images that
            # resolve are mapped to assets earlier).
            return m.group(0)
        return m.group(1) + new + m.group(3)

    htmltext = _ANCHOR_RE.sub(_anchor, htmltext)
    htmltext = _SRC_RE.sub(_src, htmltext)
    return htmltext


def extract_title(text: str, fallback: str) -> str:
    """First level-1 (``# ``) heading, else the fallback.

    The returned title is *plain text*: any inline LaTeX is flattened via
    :func:`strip_latex`, because the title is consumed only in non-math
    contexts — the sidebar nav, the breadcrumb trail and the ``<title>`` tag —
    none of which KaTeX ever renders (auto-render is scoped to ``#main``). A
    raw ``$...$`` there would surface as literal dollar signs.
    """
    for line in text.splitlines():
        s = line.strip()
        if s.startswith("# "):
            return strip_latex(s[2:].strip())
    return strip_latex(fallback)


# Common LaTeX control sequences that appear in our titles, mapped to a plain
# unicode/text rendering so the *navigation* label stays readable. The page
# body still carries the original ``#`` heading verbatim, which KaTeX renders.
_LATEX_REPLACEMENTS = [
    (r"\to", "→"),
    (r"\rightarrow", "→"),
    (r"\sim", "~"),
    (r"\times", "×"),
    (r"\infty", "∞"),
    (r"\sqrt", "√"),
    (r"\,", " "),
    (r"\;", " "),
]
_TEXT_CMD_RE = re.compile(r"\\(?:text|mathrm|mathbf|mathit|operatorname)\s*\{([^{}]*)\}")
_BRACE_GROUP_RE = re.compile(r"[\^_]\{([^{}]*)\}")
_LEFTOVER_CMD_RE = re.compile(r"\\[A-Za-z]+")


def strip_latex(s: str) -> str:
    """Flatten inline LaTeX in ``s`` to a readable plain-text approximation.

    Used for titles that feed the sidebar / breadcrumbs / ``<title>`` — places
    KaTeX never touches, so a literal ``$`` would otherwise leak through. We do
    not aim for typographic fidelity, only for a label with no stray ``$`` or
    backslash commands.
    """
    if "$" not in s and "\\" not in s:
        return s

    def _flatten(math: str) -> str:
        math = _TEXT_CMD_RE.sub(r"\1", math)
        for cmd, rep in _LATEX_REPLACEMENTS:
            math = math.replace(cmd, rep)
        # ``x^{ab}`` / ``x_{ab}`` -> ``xab``; bare ``x_1`` -> ``x1``.
        math = _BRACE_GROUP_RE.sub(r"\1", math)
        math = math.replace("^", "").replace("_", "")
        math = _LEFTOVER_CMD_RE.sub("", math)
        math = math.replace("{", "").replace("}", "")
        return math.strip()

    # Replace every $...$ / $$...$$ span by its flattened inner text.
    s = re.sub(r"\$\$(.+?)\$\$", lambda m: _flatten(m.group(1)), s, flags=re.DOTALL)
    s = re.sub(r"\$(.+?)\$", lambda m: _flatten(m.group(1)), s, flags=re.DOTALL)
    # Any residual bare $ (unbalanced) is dropped so nav text stays clean.
    return s.replace("$", "")
