# -*- coding: utf-8 -*-
"""End-to-end small-N SSEE pipeline demo for the ``toe`` library.

Composes the smallest public units across all three layers into the canonical
Sorkin-Johnston Spacetime Entanglement Entropy (SSEE) scaling experiment in a
2D causal diamond, then fits the truncated entropy-vs-N power law and renders a
log-log panel.  This is the worked example referenced by ``lib/README.md``.

Pipeline (each arrow is one public function):

    sprinkle_diamond2d  (A2)  ->  null coords (u, v)
    causal_matrix       (A2)  ->  C
    green_retarded_2d   (A2)  ->  G_R = (1/2) C
    pauli_jordan        (A2)  ->  iDelta = i (G_R - G_R^T)
    sj_state            (B1)  ->  SJ Wightman W (positive part of iDelta)
    kappa_2d / ssee     (C1)  ->  truncated SSEE S(N) on a concentric sub-diamond
    powerlaw_fit        (A1)  ->  FitResult: S ~ N^a with bootstrap CI
    powerlaw_panel      (A5)  ->  PNG figure

Physics expectation (Sorkin-Yazdi 1712.04227 double truncation): after the
UV magnitude cut kappa = sqrt(N)/(4 pi) the volume-law (type-III_1) SSEE turns
into a saturating area/log-law (type-II) trend, so the fitted exponent ``a`` is
small (|a| well below the untruncated ~1 volume-law slope).

Run (host):

    cd /Users/pazny/projects/theoryOfEverything
    MPLBACKEND=Agg PYTHONPATH=lib python3 lib/examples/demo_pipeline.py

Runtime target: < 60 s on the verified host (N grid peaks at ~500).
"""

from __future__ import annotations

import os
import time

import numpy as np

# The library lives under lib/; allow running this file directly by ensuring
# lib/ is importable (no editable install). When PYTHONPATH=lib is already set
# this is a harmless no-op.
import sys

_THIS = os.path.dirname(os.path.abspath(__file__))
_LIB = os.path.abspath(os.path.join(_THIS, os.pardir))
if _LIB not in sys.path:
    sys.path.insert(0, _LIB)

from toe.causet import (
    sprinkle_diamond2d,
    causal_matrix,
    green_retarded_2d,
    pauli_jordan,
)
from toe.sj import sj_state
from toe.entropy import kappa_2d, ssee
from toe.fits import powerlaw_fit
from toe.viz import powerlaw_panel


# ---------------------------------------------------------------------------
# Configuration (small-N, deterministic)
# ---------------------------------------------------------------------------
NS = [120, 200, 320, 500]      # sprinkle sizes (N grid)
N_SEEDS = 4                    # seeds per N (for the across-seed bootstrap CI)
FRAC = 0.5                    # concentric sub-diamond linear fraction
SEED_BASE = 7_000_000         # VYPOCET-12 seed scheme: seed_base + 1000*N + s
OUTPUT_PNG = os.path.join(_THIS, "demo_output.png")


def _sub_diamond_idx(coords: np.ndarray, frac: float) -> np.ndarray:
    """Indices of points inside the concentric sub-diamond {|u|, |v| <= frac}.

    The 2D diamond builder returns null coordinates (u, v) in [-1, 1]^2, so the
    concentric sub-diamond at linear fraction ``frac`` is the |u|, |v| <= frac
    square (itself a causal diamond).
    """
    u, v = coords[:, 0], coords[:, 1]
    return np.where((np.abs(u) <= frac) & (np.abs(v) <= frac))[0]


def _causal_from_null(coords: np.ndarray) -> np.ndarray:
    """Causal matrix in the null-coordinate convention (u, v).

    ``causal_matrix`` reduces 2D (t, x) data to the same null order; here the
    diamond builder already emits (u, v), so we apply the order directly:
    ``y`` precedes ``x`` iff ``u_y <= u_x AND v_y <= v_x``.
    """
    u = coords[:, 0][:, None]
    v = coords[:, 1][:, None]
    uy = coords[:, 0][None, :]
    vy = coords[:, 1][None, :]
    C = ((uy <= u) & (vy <= v)).astype(np.float64)
    np.fill_diagonal(C, 0.0)
    return C


def run_pipeline() -> None:
    t0 = time.time()
    print("toe demo pipeline -- 2D diamond SSEE scaling (truncated)")
    print(f"  Ns = {NS},  n_seeds = {N_SEEDS},  frac = {FRAC}")

    per_seed_S = np.zeros((len(NS), N_SEEDS))

    for i, N in enumerate(NS):
        kappa = kappa_2d(N)                      # C1: UV magnitude cutoff
        for s in range(N_SEEDS):
            rng = np.random.default_rng(SEED_BASE + 1000 * N + s)
            coords = sprinkle_diamond2d(N, rng)  # A2: Poisson sprinkle (u, v)
            C = _causal_from_null(coords)        # A2: causal order
            G_R = green_retarded_2d(C)           # A2: G_R = (1/2) C
            iDelta = pauli_jordan(G_R)           # A2: i (G_R - G_R^T)
            state = sj_state(iDelta)             # B1: SJ Wightman W
            sub_idx = _sub_diamond_idx(coords, FRAC)
            meas = ssee(state.W, iDelta, sub_idx, kappa=kappa)  # C1: truncated SSEE
            per_seed_S[i, s] = abs(meas.value)
        print(
            f"  N={N:4d}  kappa={kappa:7.4f}  "
            f"S_mean={per_seed_S[i].mean():.4f}  (+/- {per_seed_S[i].std():.4f})"
        )

    # A1: power-law fit S ~ N^a with the across-seed bootstrap CI.
    Ns_arr = np.array(NS, dtype=float)
    S_mean = np.maximum(per_seed_S.mean(axis=1), 1e-9)
    fit = powerlaw_fit(Ns_arr, S_mean, resamples=per_seed_S, n_boot=1000)

    print("\n  --- truncated SSEE scaling fit  S ~ N^a ---")
    print(f"  exponent a      = {fit.value:.4f}  (SE {fit.se_regression:.4f})")
    print(f"  68% bootstrap CI= [{fit.ci68_bootstrap[0]:.4f}, "
          f"{fit.ci68_bootstrap[1]:.4f}]  (n_boot={fit.n_boot_used})")
    print(f"  R^2             = {fit.r2:.4f}")
    print("  expectation: |a| small (saturating type-II), NOT ~1 volume law.")

    # A5: render the log-log panel with the fit line + CI band.
    powerlaw_panel(
        fit, Ns_arr, S_mean,
        save=OUTPUT_PNG,
        label="truncated SSEE",
    )
    dt = time.time() - t0
    print(f"\n  saved panel -> {OUTPUT_PNG}")
    print(f"  total runtime: {dt:.1f} s")


if __name__ == "__main__":
    run_pipeline()
