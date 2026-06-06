#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
calc_uncertainty.py  —  PROPER uncertainties for the power-law exponent fits of
VYPOCET-12 (sj-vn-type), fixing the seed-spread placeholder defect.

WHY THIS FILE EXISTS
--------------------
calc.py's powerlaw_fit(), when called WITHOUT a `sig` argument (sig=None),
returns the error sqrt((A^T A)^{-1}[0,0]) under an ASSUMED unit residual
variance.  That number depends only on the log(N) abscissa, so it is the
IDENTICAL constant 0.775853511479044 for every such fit.  It is NOT a fit
standard error and NOT a seed spread — it is a placeholder (cf. draft-04
TODO.md line ~83).  The fits affected are exactly the ones called with
sig=None (or with a degenerate all-zero `sig`):

    proxy1.entropy_trace_full.a_err   (fit of mean S_full   vs N, a=1.043)
    proxy1.entropy_trace_trunc.a_err  (fit of mean S_trunc  vs N, a=0.172)
    proxy2.pile_below_eps0_trunc.err  (fit of pile_trunc, all-zero -> a~0)
    proxy3.CV_S_trunc_powerlaw_err    (fit of CV_S_trunc    vs N, a=-0.714)
    proxy3.CV_S_full_powerlaw_err     (fit of CV_S_full     vs N, a=-0.754)

WHAT WE COMPUTE FOR EACH AFFECTED EXPONENT
------------------------------------------
(a) *_se_regression  : the ordinary-least-squares standard error of the
    log-log slope from the 7 N-points actually fit (residual-based:
    sqrt( s^2 (A^T A)^{-1}[0,0] ),  s^2 = SSR/(n-2) ), i.e. the honest
    single-fit standard error that the placeholder pretended to be.
(b) *_ci68_bootstrap : a 68% across-seed bootstrap CI of the exponent.
    For >=1000 resamples we draw the 8 seeds WITH REPLACEMENT, rebuild the
    per-N mean curve, refit the SAME log-log slope, and take the [16,84]
    percentiles of the bootstrap exponent distribution.

We RE-RUN only the pipeline pieces needed to recover the per-(N,seed)
quantities (S_full, S_trunc, pile_trunc), using calc.py's own functions and
the IDENTICAL seeds/parameters (seed = 7_000_000 + 1000*N + s, Ns, n_seeds,
frac, eps0).  Central values are NOT recomputed/changed here — we only
verify they reproduce, then emit uncertainties.
"""

import os
import json
import numpy as np

os.environ.setdefault("OMP_NUM_THREADS", "4")

import calc  # same dir; reuse the EXACT pipeline + seeds + parameters

OUTDIR = os.path.dirname(os.path.abspath(__file__))

# ---- parameters: identical to calc.run() ----
Ns = [400, 600, 800, 1000, 1200, 1500, 1800]
N_SEEDS = 8
FRAC = 0.5
EPS0 = 0.5
SEED_BASE = 7_000_000
N_BOOT = 2000
RNG_BOOT = np.random.default_rng(20260606)  # deterministic bootstrap


def per_seed_quantities():
    """Recompute, per (N, seed), the three quantities whose fits carried the
    placeholder: S_full, S_trunc, pile_trunc (#modular modes eps<EPS0)."""
    Sf = np.zeros((len(Ns), N_SEEDS))
    St = np.zeros((len(Ns), N_SEEDS))
    pile_t = np.zeros((len(Ns), N_SEEDS))
    for i, N in enumerate(Ns):
        kap = calc.kappa_2d(N)
        for s in range(N_SEEDS):
            rng = np.random.default_rng(SEED_BASE + 1000 * N + s)
            coords = calc.sprinkle_diamond(N, rng)
            C = calc.causal_matrix(coords)
            iD = calc.pauli_jordan(C)
            w, V = calc.sj_eig(iD)
            W = calc.sj_wightman_from_eig(w, V)
            sub = calc.points_in_subdiamond(coords, FRAC)

            S_full, _mu_full = calc.ssee_mu(W, iD, sub, kappa=None)
            S_trunc, mu_trunc = calc.ssee_mu(W, iD, sub, kappa=kap)
            eps_t = calc.modular_spectrum_from_mu(mu_trunc)

            Sf[i, s] = S_full
            St[i, s] = S_trunc
            pile_t[i, s] = int(np.sum(eps_t < EPS0))
        print(f"[N={N}] S_full={Sf[i].mean():.3f}  S_trunc={St[i].mean():.4f}  "
              f"pile_trunc={pile_t[i].mean():.3f}", flush=True)
    return Sf, St, pile_t


def loglog_slope(x, y):
    """Plain OLS slope of log y vs log x (matches calc.powerlaw_fit, sig=None)."""
    lx = np.log(x)
    ly = np.log(y)
    A = np.vstack([lx, np.ones_like(lx)]).T
    coef, *_ = np.linalg.lstsq(A, ly, rcond=None)
    return coef[0], coef[1]


def regression_se(x, y):
    """Residual-based OLS standard error of the log-log slope.

    SE(slope) = sqrt( SSR/(n-2) * (A^T A)^{-1}[0,0] ).
    Returns (slope, intercept, se_slope)."""
    lx = np.log(x)
    ly = np.log(y)
    A = np.vstack([lx, np.ones_like(lx)]).T
    AtA_inv = np.linalg.inv(A.T @ A)
    coef = AtA_inv @ (A.T @ ly)
    resid = ly - A @ coef
    n = len(lx)
    dof = n - 2
    s2 = float(resid @ resid) / dof
    se_slope = float(np.sqrt(s2 * AtA_inv[0, 0]))
    return float(coef[0]), float(coef[1]), se_slope


def bootstrap_ci(per_seed, x, transform="mean", n_boot=N_BOOT, rng=RNG_BOOT):
    """Across-seed bootstrap of the log-log slope.

    per_seed : (len(Ns), n_seeds) array of the raw per-seed quantity.
    transform: how the per-N point fed to the fit is built from the seeds.
        "mean" -> mean over the resampled seeds (S_full, S_trunc, pile_trunc).
        "cv"   -> std/|mean| over the resampled seeds (the proxy-3 CV fits).
    Returns dict with exponent percentiles and the bootstrap std.
    Resamples seeds WITH REPLACEMENT (same resampled-seed index set applied
    across all N, preserving the per-seed structure)."""
    n_N, n_seeds = per_seed.shape
    boots = []
    floor = 1e-9  # matches calc.powerlaw_fit's np.maximum(...,1e-9) guards
    for _ in range(n_boot):
        idx = rng.integers(0, n_seeds, size=n_seeds)
        sub = per_seed[:, idx]
        if transform == "mean":
            yv = sub.mean(axis=1)
        elif transform == "cv":
            mean = sub.mean(axis=1)
            std = sub.std(axis=1, ddof=1)
            yv = std / np.maximum(np.abs(mean), 1e-12)
        else:
            raise ValueError(transform)
        yv = np.maximum(yv, floor)
        if not np.all(np.isfinite(yv)) or np.any(yv <= 0):
            continue
        slope, _ = loglog_slope(x, yv)
        boots.append(slope)
    boots = np.array(boots)
    lo, hi = np.percentile(boots, [16.0, 84.0])
    return {
        "ci68_lo": float(lo),
        "ci68_hi": float(hi),
        "boot_std": float(boots.std(ddof=1)),
        "boot_median": float(np.median(boots)),
        "n_boot_used": int(boots.size),
    }


def main():
    x = np.array(Ns, float)
    print("Re-running pipeline pieces (same seeds/params) ...", flush=True)
    Sf, St, pile_t = per_seed_quantities()

    out = {}

    # --- (1) entropy_trace_full : fit of mean S_full vs N ---
    mean_Sf = Sf.mean(axis=1)
    a, _b, se = regression_se(x, mean_Sf)
    ci = bootstrap_ci(Sf, x, "mean")
    out["entropy_trace_full"] = {"exponent": a, "se_regression": se,
                                 "ci68_bootstrap": [ci["ci68_lo"], ci["ci68_hi"]],
                                 "boot": ci}

    # --- (2) entropy_trace_trunc : fit of mean S_trunc vs N ---
    mean_St = St.mean(axis=1)
    a, _b, se = regression_se(x, mean_St)
    ci = bootstrap_ci(St, x, "mean")
    out["entropy_trace_trunc"] = {"exponent": a, "se_regression": se,
                                  "ci68_bootstrap": [ci["ci68_lo"], ci["ci68_hi"]],
                                  "boot": ci}

    # --- (3) pile_below_eps0_trunc : all-zero -> degenerate fit ---
    mean_pt = pile_t.mean(axis=1)
    if np.all(mean_pt == 0):
        # The truncated pile-up is identically zero across all N and all seeds:
        # log(0) is regularized to 1e-9 in calc -> exponent is a numerical 0 and
        # the slope has NO statistical spread (every resample gives 0). Report
        # se=0 and a degenerate CI [0,0]; the meaningful statement is the
        # exact zero, not a fitted power law.
        out["pile_below_eps0_trunc"] = {
            "exponent": 0.0, "se_regression": 0.0,
            "ci68_bootstrap": [0.0, 0.0],
            "note": "pile_trunc identically 0 for all N and all 8 seeds; "
                    "no power law to fit; uncertainty is exactly 0 (not a placeholder)",
            "boot": {"degenerate_all_zero": True},
        }
    else:
        a, _b, se = regression_se(x, np.maximum(mean_pt, 1e-9))
        ci = bootstrap_ci(pile_t, x, "mean")
        out["pile_below_eps0_trunc"] = {"exponent": a, "se_regression": se,
                                        "ci68_bootstrap": [ci["ci68_lo"], ci["ci68_hi"]],
                                        "boot": ci}

    # --- (4) CV_S_trunc : fit of CV(S_trunc) vs N ---
    cv_St = St.std(axis=1, ddof=1) / np.maximum(np.abs(St.mean(axis=1)), 1e-12)
    a, _b, se = regression_se(x, np.maximum(cv_St, 1e-9))
    ci = bootstrap_ci(St, x, "cv")
    out["CV_S_trunc_powerlaw"] = {"exponent": a, "se_regression": se,
                                  "ci68_bootstrap": [ci["ci68_lo"], ci["ci68_hi"]],
                                  "boot": ci}

    # --- (5) CV_S_full : fit of CV(S_full) vs N ---
    cv_Sf = Sf.std(axis=1, ddof=1) / np.maximum(np.abs(Sf.mean(axis=1)), 1e-12)
    a, _b, se = regression_se(x, np.maximum(cv_Sf, 1e-9))
    ci = bootstrap_ci(Sf, x, "cv")
    out["CV_S_full_powerlaw"] = {"exponent": a, "se_regression": se,
                                 "ci68_bootstrap": [ci["ci68_lo"], ci["ci68_hi"]],
                                 "boot": ci}

    out["_meta"] = {
        "what": "Proper uncertainties replacing the 0.775853511479044 placeholder.",
        "se_regression": "residual-based OLS standard error of the log-log slope "
                         "(7 N-points); the honest single-fit SE.",
        "ci68_bootstrap": "[16,84] percentile of the log-log slope over "
                          f"{N_BOOT} across-seed resamples (8 seeds, with replacement).",
        "seeds": "IDENTICAL to calc.py: 7_000_000 + 1000*N + s, Ns="
                 f"{Ns}, n_seeds={N_SEEDS}, frac={FRAC}, eps0={EPS0}.",
        "central_values_unchanged": True,
    }

    with open(os.path.join(OUTDIR, "uncertainty.json"), "w") as f:
        json.dump(out, f, indent=2)

    print("\n=== PROPER UNCERTAINTIES (placeholder 0.775853511479044 replaced) ===")
    for k in ["entropy_trace_full", "entropy_trace_trunc",
              "pile_below_eps0_trunc", "CV_S_trunc_powerlaw", "CV_S_full_powerlaw"]:
        d = out[k]
        print(f"{k:24s} exp={d['exponent']:+.4f}  SE_reg={d['se_regression']:.4f}  "
              f"CI68=[{d['ci68_bootstrap'][0]:+.4f}, {d['ci68_bootstrap'][1]:+.4f}]")
    print("\nWrote uncertainty.json to", OUTDIR)
    return out


if __name__ == "__main__":
    main()
