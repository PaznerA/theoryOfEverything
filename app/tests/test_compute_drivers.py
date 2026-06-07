"""Smoke tests for the compute/drivers/ computational drivers.

Each of the three drivers (ds_entropy_cap_2d, ds_cap_4d, ds4d_saturation) is run
via its documented TINY smoke invocation as a SUBPROCESS into a tmp out dir, and
the written results.json is asserted to satisfy the DRIVER CLI CONTRACT:

  - results.json exists and is valid JSON;
  - a ``status`` field is present (and is a terminal status);
  - at least one cell was computed (``cells`` non-empty, ``n_cells >= 1``);
  - the iDelta +/- pairing invariant was RECORDED on a cell;
  - the host fingerprint is present (platform/machine/python + numpy/scipy).

The drivers are launched from the REPO ROOT cwd here, but they bootstrap toe
relative to their own __file__, so they also run from any cwd. Total budget for
this module is < 90 s (each smoke is < 30 s; see each driver's --help epilog).
"""

import json
import os
import subprocess
import sys

import pytest

_HERE = os.path.dirname(os.path.abspath(__file__))
_REPO_ROOT = os.path.abspath(os.path.join(_HERE, os.pardir, os.pardir))
_DRIVERS_DIR = os.path.join(_REPO_ROOT, "compute", "drivers")

# (driver module file, smoke argv) -- the smoke invocation documented in each
# driver's --help epilog (TINY config, < 30 s each).
SMOKES = {
    "ds_entropy_cap_2d": [
        "--rho", "120", "--patch-l", "1.0", "--seeds", "1", "--max-hours", "0.01",
    ],
    "ds_cap_4d": [
        "--rho", "30", "--patch-l", "1.0", "--seeds", "1", "--max-hours", "0.01",
    ],
    "ds4d_saturation": [
        "--rho", "40", "--patch-l", "1.0", "--seeds", "1", "--max-hours", "0.01",
        "--n-max", "600",
    ],
}

_TERMINAL_STATUS = {"complete", "partial-time-budget"}


def _run_driver(name, argv, out_dir):
    """Run a driver smoke via subprocess; return (results_dict, results_path)."""
    script = os.path.join(_DRIVERS_DIR, f"{name}.py")
    assert os.path.isfile(script), f"driver script missing: {script}"
    env = dict(os.environ)
    env["MPLBACKEND"] = "Agg"
    cmd = [sys.executable, script, *argv, "--out", out_dir]
    proc = subprocess.run(
        cmd, cwd=_REPO_ROOT, env=env, capture_output=True, text=True,
        timeout=120)
    assert proc.returncode == 0, (
        f"{name} smoke exited {proc.returncode}\n"
        f"STDOUT:\n{proc.stdout[-3000:]}\nSTDERR:\n{proc.stderr[-3000:]}")
    # locate the single per-run subdir's results.json
    subdirs = [d for d in os.listdir(out_dir)
               if d.startswith(f"{name}--") and
               os.path.isdir(os.path.join(out_dir, d))]
    assert len(subdirs) == 1, (
        f"{name}: expected exactly one run dir, got {subdirs}")
    results_path = os.path.join(out_dir, subdirs[0], "results.json")
    assert os.path.isfile(results_path), (
        f"{name}: results.json not written at {results_path}")
    with open(results_path) as f:
        data = json.load(f)
    return data, results_path


def _find_pairing(cells):
    """Return the first recorded pairing residual across the cells, or None."""
    for c in cells:
        if "pairing_residual_rel_max" in c:
            return c["pairing_residual_rel_max"]
    return None


@pytest.mark.parametrize("name", sorted(SMOKES))
def test_driver_smoke_contract(name, tmp_path):
    out_dir = str(tmp_path / name)
    os.makedirs(out_dir, exist_ok=True)
    data, results_path = _run_driver(name, SMOKES[name], out_dir)

    # (1) results.json exists (already asserted in _run_driver) + valid JSON
    assert isinstance(data, dict)

    # (2) driver / params / status fields present
    assert data.get("driver") == name
    assert "params" in data and isinstance(data["params"], dict)
    assert "status" in data, "results.json missing 'status'"
    assert data["status"] in _TERMINAL_STATUS, (
        f"{name}: unexpected status {data['status']!r}")

    # (3) >= 1 cell computed
    assert "cells" in data and isinstance(data["cells"], list)
    assert len(data["cells"]) >= 1, f"{name}: no cells computed"
    assert data.get("n_cells", 0) >= 1

    # (4) pairing invariant recorded on a cell (and is a tiny non-negative float)
    pairing = _find_pairing(data["cells"])
    assert pairing is not None, (
        f"{name}: no cell recorded a pairing residual (iDelta +/- invariant)")
    assert pairing >= 0.0
    assert pairing < 1e-6, (
        f"{name}: pairing residual {pairing:.2e} unexpectedly large "
        "(iDelta should be +/- paired)")

    # (5) host fingerprint present with the required keys
    host = data.get("host")
    assert isinstance(host, dict), f"{name}: host fingerprint missing"
    for key in ("platform", "machine", "python", "numpy", "scipy"):
        assert key in host and host[key], (
            f"{name}: host fingerprint missing/empty key {key!r}")

    # (6) summary present (driver-specific verdict block)
    assert "summary" in data and isinstance(data["summary"], dict)


def test_driver_smoke_runtime_under_budget(tmp_path):
    """Belt-and-suspenders: the three smokes together finish well under 90 s.

    (The per-driver subprocess timeout in _run_driver is 120 s; this aggregate
    check documents the < 90 s module budget from the task contract.)
    """
    import time

    t0 = time.time()
    for name in sorted(SMOKES):
        out_dir = str(tmp_path / f"rt_{name}")
        os.makedirs(out_dir, exist_ok=True)
        _run_driver(name, SMOKES[name], out_dir)
    elapsed = time.time() - t0
    assert elapsed < 90.0, (
        f"three driver smokes took {elapsed:.1f}s (budget < 90 s)")
