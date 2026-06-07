#!/usr/bin/env python3
"""Shared infrastructure for the ``compute/drivers/`` computational drivers.

These drivers are thin orchestrators over the ``toe`` library (v0.3.0); this
module factors out everything that is NOT physics so every driver obeys the
SAME CLI contract and writes the SAME ``results.json`` shape:

  - :func:`bootstrap_toe`        -- put ``lib/`` on ``sys.path`` relative to THIS
                                    file, so drivers run from ANY cwd.
  - :func:`make_argparser`       -- the shared argparse skeleton (--rho / --patch-l
                                    / --n-max as requested per driver, plus the
                                    universal --seeds / --max-hours / --out).
  - :func:`host_fingerprint`     -- platform / machine / python + numpy/scipy
                                    versions, recorded once per run.
  - :func:`make_run_dir`         -- ``<out>/<name>--<paramslug>--<runstamp>/``.
  - :class:`Checkpointer`        -- progressive checkpoint writer: rewrites
                                    ``results.json`` after EVERY cell.
  - :class:`TimeBudget`          -- graceful wall-clock budget (``--max-hours``):
                                    finish the current cell, finalize, exit 0.

NEVER fudge numbers: the helpers only structure I/O; all physics stays in toe.
"""

from __future__ import annotations

import argparse
import json
import math
import os
import platform
import sys
import time
from datetime import datetime, timezone


# --------------------------------------------------------------------------- #
# (1) sys.path bootstrap -- relative to THIS file so drivers run from ANY cwd
# --------------------------------------------------------------------------- #
def repo_root() -> str:
    """Absolute repo root: this file lives at <repo>/compute/drivers/_common.py."""
    here = os.path.dirname(os.path.abspath(__file__))
    return os.path.abspath(os.path.join(here, os.pardir, os.pardir))


def bootstrap_toe() -> str:
    """Prepend ``<repo>/lib`` to ``sys.path`` (idempotent) and return it.

    The ``toe`` package ships no setup.py / pyproject -- it is imported by path
    (the test conftest does the same). Doing this relative to ``__file__`` lets
    a driver be launched from any working directory.
    """
    lib_dir = os.path.join(repo_root(), "lib")
    if lib_dir not in sys.path:
        sys.path.insert(0, lib_dir)
    return lib_dir


# --------------------------------------------------------------------------- #
# (2) shared argparse skeleton
# --------------------------------------------------------------------------- #
def _comma_floats(s: str) -> list:
    """Parse a comma-separated list of floats (argparse type)."""
    return [float(x) for x in str(s).split(",") if x.strip() != ""]


def make_argparser(
    name: str,
    description: str,
    *,
    epilog: str = "",
    rho: bool = False,
    patch_l: bool = False,
    n_max: bool = False,
) -> argparse.ArgumentParser:
    """Build the shared CLI per the DRIVER CLI CONTRACT.

    Universal flags (always present): ``--seeds`` (default 4), ``--max-hours``
    (default 5.5), ``--out`` (default ``compute/results``). The per-driver
    physics flags (``--rho`` comma list, ``--patch-l`` comma list, ``--n-max``
    int cap) are added only when requested.
    """
    p = argparse.ArgumentParser(
        prog=name,
        description=description,
        epilog=epilog,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    if rho:
        p.add_argument(
            "--rho", type=_comma_floats, default=None,
            help="comma-separated list of (proper) sprinkling densities rho.",
        )
    if patch_l:
        p.add_argument(
            "--patch-l", type=_comma_floats, default=None,
            help="comma-separated list of de Sitter patch sizes l.",
        )
    if n_max:
        p.add_argument(
            "--n-max", type=int, default=None,
            help="integer cap on the point budget N per cell (memory guard).",
        )
    p.add_argument("--seeds", type=int, default=4,
                   help="number of deterministic seeds per (rho, l) cell.")
    p.add_argument("--max-hours", type=float, default=5.5,
                   help="graceful wall-clock budget in hours; finish the "
                        "current cell, finalize, exit 0.")
    p.add_argument("--out", type=str,
                   default=os.path.join(repo_root(), "compute", "results"),
                   help="output directory (a per-run subdir is created inside).")
    return p


# --------------------------------------------------------------------------- #
# (3) host fingerprint
# --------------------------------------------------------------------------- #
def host_fingerprint() -> dict:
    """Platform / machine / python + numpy/scipy versions + thread env.

    Recorded once per run so a results.json is self-describing. Reads (does NOT
    set) the OMP/BLAS thread env so the run records what it actually used.
    """
    import numpy as np
    try:
        import scipy
        scipy_v = scipy.__version__
    except Exception:  # pragma: no cover - scipy is a hard dep of toe
        scipy_v = None
    bootstrap_toe()
    try:
        import toe
        toe_v = toe.__version__
    except Exception:  # pragma: no cover
        toe_v = None
    thread_env = {
        v: os.environ.get(v)
        for v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS",
                  "VECLIB_MAXIMUM_THREADS", "NUMEXPR_NUM_THREADS")
    }
    return {
        "platform": platform.platform(),
        "machine": platform.machine(),
        "processor": platform.processor(),
        "python": platform.python_version(),
        "numpy": np.__version__,
        "scipy": scipy_v,
        "toe": toe_v,
        "thread_env": thread_env,
    }


# --------------------------------------------------------------------------- #
# (4) run directory + param slug
# --------------------------------------------------------------------------- #
def _fmt_num(x) -> str:
    """Compact, filename-safe number formatting (e.g. 3e4 -> '30000', 2.5 ->
    '2p5')."""
    f = float(x)
    if f == int(f):
        return str(int(f))
    return ("%g" % f).replace(".", "p").replace("-", "m")


def param_slug(parts: dict) -> str:
    """Filename-safe slug from a small ordered dict of param -> value(s)."""
    chunks = []
    for key, val in parts.items():
        if val is None:
            continue
        if isinstance(val, (list, tuple)):
            joined = "_".join(_fmt_num(v) for v in val)
        else:
            joined = _fmt_num(val)
        chunks.append(f"{key}{joined}")
    return "-".join(chunks) if chunks else "default"


def make_run_dir(out_dir: str, name: str, slug: str) -> tuple:
    """Create ``<out>/<name>--<slug>--<runstamp>/`` (+ a ``plots/`` subdir).

    Returns ``(run_dir, results_json_path, plots_dir)``.
    """
    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    run_dir = os.path.join(out_dir, f"{name}--{slug}--{stamp}")
    plots_dir = os.path.join(run_dir, "plots")
    os.makedirs(plots_dir, exist_ok=True)
    return run_dir, os.path.join(run_dir, "results.json"), plots_dir


# --------------------------------------------------------------------------- #
# (5) JSON sanitiser (NaN/Inf -> null for valid JSON)
# --------------------------------------------------------------------------- #
def json_safe(obj):
    """Recursively convert numpy scalars/arrays and NaN/Inf into JSON-valid
    Python objects (NaN/Inf -> ``None``)."""
    import numpy as np
    if isinstance(obj, dict):
        return {k: json_safe(v) for k, v in obj.items()}
    if isinstance(obj, (list, tuple)):
        return [json_safe(v) for v in obj]
    if isinstance(obj, np.ndarray):
        return [json_safe(v) for v in obj.tolist()]
    if isinstance(obj, np.generic):
        obj = obj.item()
    if isinstance(obj, float):
        return obj if math.isfinite(obj) else None
    if isinstance(obj, (int, str, bool)) or obj is None:
        return obj
    return obj


# --------------------------------------------------------------------------- #
# (6) progressive checkpoint writer
# --------------------------------------------------------------------------- #
class Checkpointer:
    """Holds the live results dict and rewrites ``results.json`` on demand.

    The driver mutates ``self.cells`` / ``self.summary`` and calls
    :meth:`write` after EVERY (rho, l, seed) cell so a killed run still leaves a
    valid, up-to-date ``results.json`` with ``status='partial-time-budget'``.
    An atomic temp-file rename avoids a truncated file if interrupted mid-write.
    """

    def __init__(self, path: str, driver: str, params: dict, host: dict):
        self.path = path
        self.driver = driver
        self.params = params
        self.host = host
        self.cells: list = []
        self.summary: dict = {}
        self.status: str = "partial-time-budget"
        self._t0 = time.time()

    def add_cell(self, cell: dict) -> None:
        self.cells.append(cell)

    def _payload(self) -> dict:
        return {
            "driver": self.driver,
            "params": self.params,
            "host": self.host,
            "cells": self.cells,
            "summary": self.summary,
            "status": self.status,
            "runtime_s": time.time() - self._t0,
            "n_cells": len(self.cells),
        }

    def write(self) -> None:
        """Atomically (temp + rename) rewrite the results.json."""
        payload = json_safe(self._payload())
        tmp = self.path + ".tmp"
        with open(tmp, "w") as f:
            json.dump(payload, f, indent=2)
        os.replace(tmp, self.path)

    def finalize(self, status: str) -> dict:
        """Set the terminal status ('complete' | 'partial-time-budget') and
        write once more."""
        self.status = status
        self.write()
        return self._payload()


# --------------------------------------------------------------------------- #
# (7) graceful wall-clock budget
# --------------------------------------------------------------------------- #
class TimeBudget:
    """Wall-clock budget for ``--max-hours``.

    Pattern: check :meth:`exceeded` at the TOP of each (rho, l) cell loop; if
    true, stop launching new cells, finalize what completed as
    ``status='partial-time-budget'`` and exit 0. The current cell always
    finishes (we never kill mid-cell), so the checkpoint is always consistent.
    """

    def __init__(self, max_hours: float):
        self.max_seconds = float(max_hours) * 3600.0
        self._t0 = time.time()

    @property
    def elapsed(self) -> float:
        return time.time() - self._t0

    @property
    def remaining(self) -> float:
        return self.max_seconds - self.elapsed

    def exceeded(self) -> bool:
        return self.elapsed >= self.max_seconds


# --------------------------------------------------------------------------- #
# (8) small numeric helpers shared by the drivers
# --------------------------------------------------------------------------- #
def saturating_fit(x, y):
    """Fit ``y = cap - B exp(-x/xi)``; return ``(cap, B, xi, r2, rss)``.

    NaN-safe (drops non-finite points; <3 finite points -> the last finite
    value as a flat cap). Mirrors the VYPOCET-19/23 ``saturating_fit`` so the
    cap measurement is the SAME protocol as the committed calc.
    """
    import numpy as np
    from scipy.optimize import curve_fit
    x = np.asarray(x, float)
    y = np.asarray(y, float)
    fin = np.isfinite(x) & np.isfinite(y)
    if fin.sum() < 3:
        cap = float(y[fin][-1]) if fin.any() else float("nan")
        return cap, 0.0, 1.0, 0.0, 0.0
    x = x[fin]
    y = y[fin]
    p0 = [float(y[-1]), float(y[-1] - y[0]), 1.0]
    try:
        popt, _ = curve_fit(
            lambda t, cap, B, xi: cap - B * np.exp(-t / xi),
            x, y, p0=p0, maxfev=40000)
        cap, B, xi = popt
        yhat = cap - B * np.exp(-x / xi)
    except Exception:
        cap, B, xi = float(y[-1]), 0.0, 1.0
        yhat = np.full_like(y, cap)
    rss = float(np.sum((y - yhat) ** 2))
    sst = float(np.sum((y - y.mean()) ** 2))
    r2 = 1.0 - rss / sst if sst > 0 else 0.0
    return float(cap), float(B), float(xi), float(r2), rss


def null_coords_from_t_rstar(coords):
    """Convert ``(t, r*)`` rows to the EXPLICIT 2D null coordinates
    ``(u, v) = (t - r*, t + r*)`` that the toe v0.3.0 sparse builders require.

    LOAD-BEARING (VYPOCET-24): ``toe.causet.causal_blocks_2d`` /
    ``idelta_operator_2d`` interpret 2D coords DIRECTLY as null ``(u, v)`` -- they
    do NOT do the ``(t, x) -> (u, v)`` reduction that the dense ``causal_matrix``
    does internally. Feeding raw ``(t, r*)`` gives a SILENTLY WRONG causal matrix
    (matvec rel. error ~0.63). Passing ``uv = (t - r*, t + r*)`` makes the matvec
    machine-precise (rel. error ~3.9e-16).
    """
    import numpy as np
    coords = np.asarray(coords, float)
    t = coords[:, 0]
    rs = coords[:, 1]
    return np.column_stack([t - rs, t + rs])


def pairing_residual_rel_from_eigs(eigvals) -> float:
    """+/- pairing residual (relative) from a (sparse or dense) iDelta spectrum.

    Sorts the eigenvalues, pairs the largest-magnitude positive against the
    largest-magnitude negative, and returns ``max|pos - (-neg)| / max|pos|``.
    The iDelta spectrum is exactly +/- paired, so a healthy region gives ~0.
    """
    import numpy as np
    ev = np.sort(np.asarray(eigvals, float))
    n = ev.size // 2
    if n == 0:
        return 0.0
    pos = ev[-n:][::-1]
    neg = -ev[:n]
    denom = max(float(np.max(np.abs(pos))), 1e-300)
    return float(np.max(np.abs(pos - neg)) / denom)
