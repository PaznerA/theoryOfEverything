"""Independent cross-CAS (Wolfram Language) validation lane -- pytest wiring.

Two layers:

  (1) ALWAYS-RUNNING filesystem guards (no Wolfram needed): the three .wl
      scripts and the runner exist, and none of them contains a
      machine-absolute path literal (the project portability convention --
      everything must resolve __file__-relative so it runs from any cwd / on
      any machine).

  (2) A Wolfram-gated end-to-end test: when ``wolframscript`` is on PATH, run
      verification/cas/run_all.py and assert the overall pass plus the
      headline -18/11 check.  Skipped cleanly when the Wolfram Engine is not
      installed (see verification/cas/README.md for the one-time setup).

All paths are resolved __file__-relative (this test tree is itself guarded
against absolute-path literals by test_portability_guards.py).
"""

import json
import os
import re
import shutil
import subprocess
import sys

import pytest

# This file lives at <repo>/app/tests/test_cas_validation.py.
_HERE = os.path.dirname(os.path.abspath(__file__))
REPO_ROOT = os.path.abspath(os.path.join(_HERE, os.pardir, os.pardir))
CAS_DIR = os.path.join(REPO_ROOT, "verification", "cas")

WL_SCRIPTS = ("a4_identity.wl", "ds_classifier.wl", "lambda_ledger.wl")
RUNNER = os.path.join(CAS_DIR, "run_all.py")

# Same machine-absolute-home pattern as test_portability_guards.py: a real
# /Users/<name>/ or /home/<name>/ prefix (user segment is word chars/dot/hyphen
# then a slash), which never trips on the bare prefixes or <placeholder> tokens.
_ABS_PATH_RE = re.compile(r"/(?:Users|home)/[\w.-]+/")

_WOLFRAM_MISSING = shutil.which("wolframscript") is None
_SKIP_REASON = "Wolfram Engine not installed -- see verification/cas/README.md"


# --------------------------------------------------------------------------
# (1) Always-running filesystem guards.
# --------------------------------------------------------------------------
def test_cas_scripts_exist():
    """The three .wl scripts and the runner are present in verification/cas/."""
    missing = [
        name
        for name in WL_SCRIPTS
        if not os.path.isfile(os.path.join(CAS_DIR, name))
    ]
    assert not missing, "missing .wl validation scripts: %s" % missing
    assert os.path.isfile(RUNNER), "missing runner: %s" % RUNNER


def test_cas_scripts_have_no_machine_absolute_paths():
    """No leaked /Users/<user>/ or /home/<user>/ literal in any .wl or runner.

    Portable scripts resolve their I/O paths relative to $InputFileName /
    __file__, so an absolute home path here would be a portability regression.
    """
    offenders = []
    targets = [os.path.join(CAS_DIR, n) for n in WL_SCRIPTS] + [RUNNER]
    for path in targets:
        with open(path, encoding="utf-8") as fh:
            for lineno, line in enumerate(fh, start=1):
                m = _ABS_PATH_RE.search(line)
                if m:
                    rel = os.path.relpath(path, REPO_ROOT)
                    offenders.append("%s:%d: %r" % (rel, lineno, m.group(0)))
    assert not offenders, (
        "machine-absolute path literal(s) in CAS scripts "
        "(resolve paths $InputFileName/__file__-relative instead):\n  "
        + "\n  ".join(offenders)
    )


def test_runner_signals_missing_wolfram_with_exit_code_2():
    """When wolframscript is absent the runner exits 2 (skip-able), not crash.

    We only assert this on the machine where Wolfram is genuinely missing;
    where it is installed the runner does real work and this contract does
    not apply.
    """
    if not _WOLFRAM_MISSING:
        pytest.skip("wolframscript present -- exit-code-2 contract not exercised")
    proc = subprocess.run(
        [sys.executable, RUNNER],
        capture_output=True,
        text=True,
    )
    assert proc.returncode == 2, (
        "runner should exit 2 when wolframscript is missing; got %d\nstderr:\n%s"
        % (proc.returncode, proc.stderr)
    )
    assert "wolframscript" in proc.stderr.lower()


# --------------------------------------------------------------------------
# (2) Wolfram-gated end-to-end validation.
# --------------------------------------------------------------------------
@pytest.mark.skipif(_WOLFRAM_MISSING, reason=_SKIP_REASON)
def test_cas_validation_overall_pass():
    """Run the independent CAS lane and assert every script's overall pass.

    The kolo-20 myrheim-meyer BLOCKER (formulas.json denominator 4 vs the
    published Meyer-1988 value 2) was FIXED: causal-sets fragment 4->2 +
    consolidate, and the WL script now reads the live formulas.json denominator.
    All 7 CAS scripts pass.
    """
    proc = subprocess.run(
        [sys.executable, RUNNER],
        capture_output=True,
        text=True,
    )
    assert proc.returncode == 0, (
        "run_all.py failed (rc=%d)\nstdout:\n%s\nstderr:\n%s"
        % (proc.returncode, proc.stdout, proc.stderr)
    )

    results_path = os.path.join(CAS_DIR, "results.json")
    assert os.path.isfile(results_path), "run_all.py did not write results.json"
    with open(results_path, encoding="utf-8") as fh:
        summary = json.load(fh)

    assert summary.get("overall_pass") is True, (
        "CAS lane overall_pass is not True:\n%s"
        % json.dumps(summary, indent=2)
    )
    for script in WL_SCRIPTS:
        entry = summary["scripts"].get(script, {})
        assert entry.get("overall_pass") is True, (
            "%s did not pass:\n%s" % (script, json.dumps(entry, indent=2))
        )


@pytest.mark.skipif(_WOLFRAM_MISSING, reason=_SKIP_REASON)
def test_cas_headline_minus_18_11_check_true():
    """The headline -18/11 check (single Weyl c/(-a)) is True in the CAS lane."""
    a4_json = os.path.join(CAS_DIR, "a4_identity_result.json")
    # The end-to-end test (or a prior run) produces this; run the lane if not.
    if not os.path.isfile(a4_json):
        subprocess.run([sys.executable, RUNNER], capture_output=True, text=True)
    assert os.path.isfile(a4_json), "a4_identity_result.json not produced"
    with open(a4_json, encoding="utf-8") as fh:
        payload = json.load(fh)
    checks = payload.get("checks", {})
    assert checks.get("single_weyl_is_minus_18_11") is True, (
        "the -18/11 headline check is not True:\n%s"
        % json.dumps(checks, indent=2)
    )
    assert payload.get("exact_rationals", {}).get("ratio_single_weyl") == "-18/11"
