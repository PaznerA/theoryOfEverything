#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Independent cross-CAS validation runner for the project's exact symbolics.

This is the "cross-HW for symbolics" lane: each .wl script re-derives a
published exact result in Wolfram Language *from the literature coefficients*
(not transcribed from the project's sympy outputs).  Running both lanes and
comparing is independent evidence; a disagreement is a bug in one derivation.

The runner:
  * locates the .wl scripts next to this file (``__file__``-relative, so it
    runs from any working directory -- project portability convention);
  * invokes ``wolframscript -file <script>`` for each;
  * collects each script's exported ``*_result.json`` into one
    ``results.json`` with an overall pass/fail;
  * exits gracefully (code 2 + message pointing to the README) when
    ``wolframscript`` is not installed, so CI / pytest can skip cleanly.

Exit codes:
    0  all scripts ran and every overall_pass is True
    1  wolframscript ran but at least one check / script failed
    2  wolframscript is not installed (nothing was validated)
"""

import json
import os
import shutil
import subprocess
import sys

# This file lives at <repo>/verification/cas/run_all.py.  Resolve everything
# relative to it so the runner is cwd-independent (portability convention).
HERE = os.path.dirname(os.path.abspath(__file__))

# (.wl script, the JSON it exports) -- the export name is fixed inside each .wl.
SCRIPTS = [
    ("a4_identity.wl", "a4_identity_result.json"),
    ("ds_classifier.wl", "ds_classifier_result.json"),
    ("lambda_ledger.wl", "lambda_ledger_result.json"),
]

WOLFRAM = "wolframscript"


def _missing_wolfram_message():
    return (
        "wolframscript not found on PATH -- the independent CAS validation "
        "lane was NOT run.\n"
        "Install the (free) Wolfram Engine and activate it once:\n"
        "    brew install --cask wolfram-engine\n"
        "    wolframscript -activate        # interactive, needs a Wolfram ID\n"
        "then re-run:\n"
        "    python3 verification/cas/run_all.py\n"
        "See verification/cas/README.md for details."
    )


def main():
    if shutil.which(WOLFRAM) is None:
        # Graceful, well-signposted exit -- nothing could be validated.
        print(_missing_wolfram_message(), file=sys.stderr)
        return 2

    summary = {
        "lane": "independent cross-CAS (Wolfram Language) validation of exact symbolics",
        "wolframscript": shutil.which(WOLFRAM),
        "scripts": {},
        "overall_pass": True,
    }

    any_failure = False

    for script, out_json in SCRIPTS:
        script_path = os.path.join(HERE, script)
        out_path = os.path.join(HERE, out_json)

        entry = {"ran": False, "overall_pass": False}

        if not os.path.isfile(script_path):
            entry["error"] = "script file missing: %s" % script_path
            any_failure = True
            summary["scripts"][script] = entry
            continue

        # Remove any stale result so we never read a previous run's JSON.
        if os.path.isfile(out_path):
            try:
                os.remove(out_path)
            except OSError:
                pass

        proc = subprocess.run(
            [WOLFRAM, "-file", script_path],
            cwd=HERE,
            capture_output=True,
            text=True,
        )
        entry["ran"] = True
        entry["returncode"] = proc.returncode
        if proc.stdout.strip():
            entry["stdout"] = proc.stdout.strip()
        if proc.stderr.strip():
            entry["stderr"] = proc.stderr.strip()

        if proc.returncode != 0:
            entry["error"] = "wolframscript exited non-zero"
            any_failure = True
            summary["scripts"][script] = entry
            continue

        if not os.path.isfile(out_path):
            entry["error"] = "expected result JSON not produced: %s" % out_json
            any_failure = True
            summary["scripts"][script] = entry
            continue

        try:
            with open(out_path, encoding="utf-8") as fh:
                payload = json.load(fh)
        except (OSError, ValueError) as exc:
            entry["error"] = "could not read result JSON: %s" % exc
            any_failure = True
            summary["scripts"][script] = entry
            continue

        script_pass = bool(payload.get("overall_pass", False))
        entry["overall_pass"] = script_pass
        entry["checks"] = payload.get("checks", {})
        entry["result_json"] = out_json
        if not script_pass:
            any_failure = True

        summary["scripts"][script] = entry

    summary["overall_pass"] = not any_failure

    results_path = os.path.join(HERE, "results.json")
    with open(results_path, "w", encoding="utf-8") as fh:
        json.dump(summary, fh, indent=2, ensure_ascii=False)

    print("Wrote %s" % results_path)
    print("overall_pass = %s" % summary["overall_pass"])
    for script, entry in summary["scripts"].items():
        print("  %-20s pass=%s" % (script, entry.get("overall_pass")))

    return 0 if summary["overall_pass"] else 1


if __name__ == "__main__":
    sys.exit(main())
