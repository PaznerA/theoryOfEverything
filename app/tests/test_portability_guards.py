"""Portability / repo-encoding guard tests (pure filesystem, < 5 s).

These guards turn three hard-won operational lessons into CI contracts so they
can never silently regress back into session-only knowledge:

  (i)  NO machine-absolute path literal (``/Users/<user>/...`` or
       ``/home/<user>/...``) may appear in any *.py under the runnable code
       trees — core-data/calculations/, compute/, lib/, web/ — nor in the
       test tree app/tests/.  Comments and docstrings are NOT exempt: such a
       path broke CI twice (the OUTDIR batch and the lib-imports batch).
       Portable code resolves paths __file__-relative.

  (ii) Every driver under compute/drivers/ (a *.py with a ``__main__`` entry;
       the shared _common.py helper is not a driver) must advertise BOTH the
       ``--max-hours`` time-budget flag and a ``smoke`` invocation in its
       --help epilog source -- the smoke config is the documented tiny run.

  (iii) Every calculation dir under core-data/calculations/ that ships a
        results.json must have a prose writeup under
        knowledge-base/vypocty/VYPOCET-*.md that references it by slug --
        results without a writeup are undocumented findings.

Pure filesystem string checks: no imports of toe, no subprocess, no calc runs.
"""

import os
import re
import glob

import pytest

# This file lives at <repo>/app/tests/test_portability_guards.py.
_HERE = os.path.dirname(os.path.abspath(__file__))
REPO_ROOT = os.path.abspath(os.path.join(_HERE, os.pardir, os.pardir))

# Trees whose *.py must be free of machine-absolute path literals.
_GUARDED_PY_DIRS = (
    os.path.join("core-data", "calculations"),
    "compute",
    "lib",
    "web",
    os.path.join("app", "tests"),
)

# A machine-absolute home path: a macOS ``/Users/<name>/`` or Linux
# ``/home/<name>/`` prefix, where the user segment is a REAL account name
# (word chars, dot, hyphen) followed by a slash. Two deliberate properties:
#   * the trailing slash means the bare prefixes (the ones in this test's own
#     prose) and generic words like "home" never self-trip;
#   * restricting the user segment to [\w.-] means angle-bracket placeholders
#     (the literal "<user>"/"<name>" tokens documenting the pattern) and the
#     regex source itself do not match -- only a genuine leaked path does.
_ABS_PATH_RE = re.compile(r"/(?:Users|home)/[\w.-]+/")


def _iter_py_files(rel_dir):
    root = os.path.join(REPO_ROOT, rel_dir)
    for dirpath, dirnames, filenames in os.walk(root):
        # skip caches / vendored build output
        dirnames[:] = [
            d for d in dirnames
            if d not in ("__pycache__", ".pytest_cache", "node_modules")
        ]
        for fn in filenames:
            if fn.endswith(".py"):
                yield os.path.join(dirpath, fn)


def test_no_machine_absolute_paths_in_code():
    """(i) No /Users/<user>/ or /home/<user>/ literal in any guarded *.py."""
    offenders = []
    for rel_dir in _GUARDED_PY_DIRS:
        for path in _iter_py_files(rel_dir):
            with open(path, encoding="utf-8") as f:
                for lineno, line in enumerate(f, start=1):
                    m = _ABS_PATH_RE.search(line)
                    if m:
                        rel = os.path.relpath(path, REPO_ROOT)
                        offenders.append(f"{rel}:{lineno}: {m.group(0)!r}")
    assert not offenders, (
        "machine-absolute path literal(s) found in guarded .py "
        "(use __file__-relative resolution instead):\n  "
        + "\n  ".join(offenders)
    )


def _drivers():
    """Driver *.py files under compute/drivers/ (those with a __main__ entry).

    The shared helper _common.py has no CLI entry point and is excluded.
    """
    out = []
    for path in glob.glob(os.path.join(REPO_ROOT, "compute", "drivers", "*.py")):
        with open(path, encoding="utf-8") as f:
            src = f.read()
        if "__main__" in src:
            out.append((path, src))
    return out


def test_drivers_have_max_hours_and_smoke_in_help_epilog():
    """(ii) Every compute/drivers/ driver documents --max-hours and a smoke run."""
    drivers = _drivers()
    assert drivers, "no compute/drivers/*.py with a __main__ entry found"
    missing = []
    for path, src in drivers:
        rel = os.path.relpath(path, REPO_ROOT)
        problems = []
        if "--max-hours" not in src:
            problems.append("no '--max-hours'")
        if "smoke" not in src.lower():
            problems.append("no 'smoke' invocation in --help epilog")
        if problems:
            missing.append(f"{rel}: " + "; ".join(problems))
    assert not missing, (
        "driver CLI contract violation (every driver must expose --max-hours "
        "and a smoke config in its --help epilog):\n  " + "\n  ".join(missing)
    )


def test_every_results_json_has_a_writeup():
    """(iii) Every calc dir with results.json is referenced by a VYPOCET-* writeup."""
    calc_root = os.path.join(REPO_ROOT, "core-data", "calculations")
    writeup_glob = os.path.join(
        REPO_ROOT, "knowledge-base", "vypocty", "VYPOCET-*.md"
    )
    writeups = glob.glob(writeup_glob)
    assert writeups, f"no writeups matched {writeup_glob}"

    # Concatenate writeup bodies once; a slug is "documented" if it appears
    # in any writeup (the writeup filename is a Czech transliteration, so we
    # match on the English slug referenced inside the prose, not the filename).
    corpus = []
    for wp in writeups:
        with open(wp, encoding="utf-8") as f:
            corpus.append(f.read())
    corpus = "\n".join(corpus)

    orphans = []
    for entry in sorted(os.listdir(calc_root)):
        calc_dir = os.path.join(calc_root, entry)
        if not os.path.isdir(calc_dir):
            continue
        if not os.path.isfile(os.path.join(calc_dir, "results.json")):
            continue
        if entry not in corpus:
            orphans.append(entry)
    assert not orphans, (
        "calc dirs shipping results.json with NO knowledge-base/vypocty/"
        "VYPOCET-* writeup referencing their slug:\n  " + "\n  ".join(orphans)
    )
