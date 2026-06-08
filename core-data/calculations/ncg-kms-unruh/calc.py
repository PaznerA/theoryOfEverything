#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
NCG <-> SEMICLASSICAL : the UNRUH TEMPERATURE LAW from the SJ modular flow
==========================================================================
FLAGSHIP test of the most direct unexplored shared-math edge between
noncommutative-geometry (Connes-Rovelli thermal time, gr-qc/9406019) and
semiclassical-gravity (Unruh effect): does the SORKIN-JOHNSTON modular flow on a
2D Rindler causal set reproduce the UNRUH TEMPERATURE LAW

    T_local(x) = 1 / (2*pi * x_proper)        (Bisognano-Wichmann / Unruh / Tolman)

with the proper-distance normalisation FIXED INDEPENDENTLY from the geometry
(the causet sprinkling density / proper length) -- and NEVER tuned to a target?

WHY THIS IS THE NON-TAUTOLOGICAL TEST (lesson from F-034)
--------------------------------------------------------
F-034 (VYPOCET-30) found that beta_KMS = 1 and beta_occ = 1 are TAUTOLOGIES of
the SJ/Casini-Huerta construction: Tomita-Takesaki gives KMS at beta = 1 BY
CONSTRUCTION, so those numbers are not physics. The ONLY non-trivial geometric
invariant F-034 found was the rho-invariant boost-DIAGONAL slope (|K(x,x)| linear
in distance-to-horizon, slope ~27.84, R^2~0.95, CV 2.7%). But the ABSOLUTE Unruh
2*pi was NOT recovered (unruh_ratio = 0.786 vs 2*pi = 6.283) because the surrogate
kernel's modular-energy units eps = ln[mu/(mu-1)] do NOT carry the boost-rapidity
normalisation.

This calc isolates the GENUINELY geometric content and tests it against a
GEOMETRY-FIXED scale -- the anti-circularity is structural:

  * the proper-distance scale is fixed BEFORE any slope, from the sprinkling
    density (eps_disc = rho^{-1/2}, the discreteness proper length) and the slab
    proper length -- NEVER fitted to give 2*pi;
  * we measure (A) the LAW EXPONENT (Unruh T ~ x^{-p}; BW predicts the
    energy-density K(x,x) ~ 2*pi x rho_E linear in proper x, exponent p_E = +1,
    i.e. T_local ~ 1/x) and (B) the absolute 2*pi COEFFICIENT via the
    boost-quantum normalisation -- and report BOTH honestly.

OBSERVABLES (pre-registered)
----------------------------
(A) UNRUH LAW EXPONENT.  K(x,x) = |modular energy density| binned vs PROPER
    distance x to the horizon (cut x = 0). Log-log slope p_E of K(x,x) vs x_proper.
    BW/Unruh: p_E = +1 (energy density grows linearly in proper distance =>
    T_local(x) ~ 1/x, exponent -1). A robust, rho-invariant p_E ~ 1 = the Unruh
    1/x temperature LAW recovered from the modular flow (the SHAPE of the law).

(B) BOOST SLOPE vs PROPER DISTANCE.  Linear slope d K(x,x) / d x_proper, R^2, and
    rho-invariance (CV across rho). The F-034 linear diagonal, now measured vs the
    GEOMETRY-FIXED proper distance (not coordinate distance).

(C) ABSOLUTE 2*pi COEFFICIENT (the discriminator).  Three geometry-fixed routes,
    NONE tuned: (c1) boost-quantum product eps_k * <x>_k per modular eigenmode
    (BW: modular energy x localisation = the boost quantum, continuum 2*pi);
    (c2) the diagonal-slope-to-energy-density ratio (F-034 unruh_ratio,
    reproduced); (c3) the slope vs proper distance in discreteness units. We
    report the best-route coefficient and |coeff - 2*pi| / 2*pi.

(D) CONTROLS.  INTERVAL cut {0<x<x0} (BW invalid: modular Hamiltonian peaks at
    both ends, the 1/x-from-one-end law must FAIL) and SHUFFLE K' = Q K Q^T (Haar
    conjugation: spectrum preserved, geometry destroyed). The LAW + slope must
    collapse on both.

(E) STRETCH (budget permitting).  2D de Sitter static patch -> Gibbons-Hawking
    T_dS = 1/(2*pi*l): the 1/l law + 2*pi coefficient, the horizon analogue of
    Unruh. SKIP-with-note if over the wall.

DISCRIMINATOR (pre-registered)
------------------------------
correspondence = genuine-positive  iff  the Unruh LAW (p_E ~ 1, rho-invariant,
  R^2 high) AND the absolute 2*pi coefficient (|coeff-2pi|/2pi < 0.20) are BOTH
  recovered from geometry-fixed normalisation, controls clean.
correspondence = partial  iff  the LAW shape (p_E ~ 1, rho-invariant) is recovered
  and controls clean, but the absolute 2*pi coefficient is NOT (off by a finite
  factor) -- the SHAPE of Unruh emerges, the absolute temperature does not.
correspondence = tautology  iff  only the construction-tautological pieces survive
  (KMS beta=1, occupation beta=1) with no geometry-fixed LAW or coefficient.
correspondence = negative/refuted  iff  the law fails or a control also passes.

CAVEAT (honest, inherited): the SJ modular kernel is a SURROGATE Dirac in
modular-energy units eps = ln[mu/(mu-1)] (Casini-Huerta) lifted to the site basis;
beta_KMS = 1 is a Tomita-Takesaki tautology. 2D, massless, finite N <= 1500 dense:
we measure a TREND (rho-invariance), not the N->inf continuum value. Discrete
corrections O(1/sqrt N).

CONVENTIONS (verified repo-present / literature IDs only -- NEVER invented)
--------------------------------------------------------------------------
SJ state + modular kernel: iDelta = i(G_R - G_R^T); 2D massless G_R = (1/2) C
  (Sorkin-Yazdi 1611.10281). W = positive spectral part. One-particle modular
  Hamiltonian K(x,y) from W_O v = mu iDelta_O v, eps = ln[mu/(mu-1)]
  (Casini-Huerta 0905.2562). kappa=None = genuine SJ modular flow. Modular flow
  as thermal/physical time: Connes-Rovelli gr-qc/9406019. Bisognano-Wichmann
  modular flow = boost, Unruh temperature 1/2pi: 1712.04227 (context 2008.07697),
  references.bib bisognano1976duality + unruh1976notes. de Sitter static patch +
  Gibbons-Hawking 1/(2pi l): sprinkle_ds_static_patch2d (Anninos 1205.3855
  conformal trick, VYPOCET-19).

All paths __file__-relative (portability guard). results.json: fixed schema with
'status' + atomic write (tmp + os.replace), progressive per-seed flush.
"""

import json
import os
import sys
import time

for _v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS",
           "VECLIB_MAXIMUM_THREADS", "NUMEXPR_NUM_THREADS"):
    os.environ.setdefault(_v, "4")

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# --- __file__-relative paths (portability) ---------------------------------
OUTDIR = os.path.dirname(os.path.abspath(__file__))
PLOTDIR = os.path.join(OUTDIR, "plots")
os.makedirs(PLOTDIR, exist_ok=True)
_REPO_ROOT = os.path.abspath(os.path.join(OUTDIR, os.pardir, os.pardir, os.pardir))
_LIB = os.path.join(_REPO_ROOT, "lib")
if _LIB not in sys.path:
    sys.path.insert(0, _LIB)

from toe.causet import (sprinkle_slab2d, sprinkle_ds_static_patch2d,
                        causal_matrix, green_retarded_2d, pauli_jordan)
from toe.sj import sj_state
from toe.entropy import modular_kernel

# Optional new lib primitive (added in the same run); fall back to local copy.
try:
    from toe.spectraltriple import unruh_proper_law, UnruhLawFit
    _HAVE_LIB_UNRUH = True
except Exception:  # pragma: no cover
    _HAVE_LIB_UNRUH = False


# ===========================================================================
# CONFIG
# ===========================================================================
T_EXTENT = 0.30
X_EXTENT = 1.0
INTERVAL_X0 = 0.5 * X_EXTENT          # interval cut {0 < x < x0}: BW invalid
TWO_PI = 2.0 * np.pi
WALL_CAP_S = 25 * 60                  # 25 min total wall-clock cap
# proper-distance fit window (fraction of x_extent), fixed BEFORE the slope:
X_LO_FRAC = 0.06                      # avoid the horizon-edge discretisation pileup
X_HI_FRAC = 0.90                      # avoid the far slab boundary
N_BINS = 12


# ===========================================================================
# FIT HELPERS
# ===========================================================================

def r2(y, yhat):
    y = np.asarray(y, float)
    ss = np.sum((y - y.mean()) ** 2)
    return 1.0 - np.sum((y - yhat) ** 2) / ss if ss > 0 else 0.0


def linfit(x, y):
    x = np.asarray(x, float); y = np.asarray(y, float)
    m = np.isfinite(x) & np.isfinite(y)
    if m.sum() < 2:
        return float("nan"), float("nan"), float("nan")
    A = np.vstack([x[m], np.ones(m.sum())]).T
    coef, *_ = np.linalg.lstsq(A, y[m], rcond=None)
    return float(coef[0]), float(coef[1]), float(r2(y[m], A @ coef))


def _m(lst):
    lst = [x for x in lst if x is not None and np.isfinite(x)]
    return float(np.mean(lst)) if lst else float("nan")


def _sd(lst):
    lst = [x for x in lst if x is not None and np.isfinite(x)]
    return float(np.std(lst, ddof=1)) if len(lst) > 1 else float("nan")


def _to_native(o):
    if isinstance(o, dict):
        return {k: _to_native(v) for k, v in o.items()}
    if isinstance(o, (list, tuple)):
        return [_to_native(v) for v in o]
    if isinstance(o, (np.floating,)):
        return float(o)
    if isinstance(o, (np.integer,)):
        return int(o)
    if isinstance(o, (np.bool_,)):
        return bool(o)
    if isinstance(o, np.ndarray):
        return o.tolist()
    return o


def write_results_atomic(results, path):
    tmp = path + ".tmp"
    with open(tmp, "w") as fh:
        json.dump(_to_native(results), fh, indent=2)
    os.replace(tmp, path)


# ===========================================================================
# CORE OBSERVABLES
# ===========================================================================

def binned_diagonal(K, x_proper, *, x_lo, x_hi, n_bins=N_BINS, min_count=6):
    """Bin |K(x,x)| against PROPER distance x to the horizon and return
    (centers, profile, counts) on the geometry-fixed window [x_lo, x_hi]."""
    K = np.asarray(K)
    diag = np.abs(np.real(np.diag(K)))
    xp = np.abs(np.asarray(x_proper, float))
    bins = np.linspace(x_lo, x_hi, n_bins + 1)
    centers = 0.5 * (bins[:-1] + bins[1:])
    idx = np.digitize(xp, bins)
    prof = np.full(n_bins, np.nan); cnt = np.zeros(n_bins, int)
    for b in range(1, n_bins + 1):
        msk = idx == b
        cnt[b - 1] = int(msk.sum())
        if msk.sum() >= min_count:
            prof[b - 1] = float(np.mean(diag[msk]))
    return centers, prof, cnt


def unruh_law_and_slope(K, x_proper, *, x_lo, x_hi, n_bins=N_BINS):
    """The Unruh-law observables on a GEOMETRY-FIXED proper-distance window.

    Returns a dict with:
      * law_exponent  : log-log slope p_E of K(x,x) vs proper x. BW: K(x,x) ~
                        2*pi x rho_E => p_E = +1 (energy density linear in proper
                        distance => T_local ~ 1/x, Unruh exponent -1).
      * law_r2        : R^2 of the log-log fit.
      * boost_slope   : linear slope d K(x,x) / d x_proper (dimensionful).
      * boost_r2      : R^2 of the linear fit.
      * centers, prof : the binned profile (for plotting).
    """
    centers, prof, cnt = binned_diagonal(K, x_proper, x_lo=x_lo, x_hi=x_hi,
                                         n_bins=n_bins)
    g = np.isfinite(prof) & (centers > 0) & (prof > 0)
    if g.sum() >= 3:
        lp = np.polyfit(np.log(centers[g]), np.log(prof[g]), 1)
        law_exp = float(lp[0])
        law_pred = lp[0] * np.log(centers[g]) + lp[1]
        law_r2 = float(r2(np.log(prof[g]), law_pred))
    else:
        law_exp = float("nan"); law_r2 = float("nan")
    boost_slope, _, boost_r2 = linfit(centers[g], prof[g])
    return {
        "law_exponent": law_exp, "law_r2": law_r2,
        "boost_slope": boost_slope, "boost_r2": boost_r2,
        "centers": centers.tolist(), "prof": prof.tolist(),
        "counts": cnt.tolist(),
    }


def boost_quantum_2pi(K, x_proper, *, x_lo, x_hi):
    """Route (c1) to the absolute 2*pi: the boost-quantum product eps_k * <x>_k
    per modular EIGENMODE.

    BW: K = 2*pi K_boost, K_boost = integral x T_00 dx. A modular eigenmode of
    modular energy eps_k localised at proper distance <x>_k carries boost quantum
    eps_k * <x>_k -> 2*pi in the continuum (the modular energy x position = the
    boost generator's rapidity quantum). GEOMETRY-FIXED: <x>_k is the proper
    localisation, NEVER tuned. Returns (median product, n_modes_used).
    """
    K = np.real(np.asarray(K))
    w, V = np.linalg.eigh(K)
    prob = V ** 2
    xp = np.abs(np.asarray(x_proper, float))
    xbar = (prob * xp[:, None]).sum(0)
    absw = np.abs(w)
    m = (absw > 1e-6) & (xbar > x_lo) & (xbar < x_hi)
    if m.sum() < 3:
        return float("nan"), int(m.sum())
    return float(np.median(absw[m] * xbar[m])), int(m.sum())


def unruh_ratio_f034(K, x_proper, *, x_lo, x_hi, n_bins=N_BINS):
    """Route (c2): the F-034 unruh_ratio = boost_slope / e0 (through-origin energy
    density slope), reproduced for continuity. Geometry-fixed (proper distance)."""
    centers, prof, cnt = binned_diagonal(K, x_proper, x_lo=x_lo, x_hi=x_hi,
                                         n_bins=n_bins)
    g = np.isfinite(prof) & (centers > 0)
    if g.sum() < 2:
        return float("nan")
    sl, _, _ = linfit(centers[g], prof[g])
    denom = float(np.dot(centers[g], centers[g]))
    e0 = float(np.dot(centers[g], prof[g]) / denom) if denom > 0 else float("nan")
    return float(sl / e0) if (np.isfinite(sl) and np.isfinite(e0) and e0 != 0) \
        else float("nan")


def shuffle_kernel(K, seed):
    """Haar-orthogonal conjugation K' = Q K Q^T: spectrum preserved, site
    geometry destroyed (the shuffle control)."""
    K = np.real(np.asarray(K))
    n = K.shape[0]
    rng = np.random.default_rng(seed)
    Q, _ = np.linalg.qr(rng.standard_normal((n, n)))
    return Q @ K @ Q.T


# ===========================================================================
# ONE SEED  (Rindler slab)
# ===========================================================================

def run_seed_rindler(N, seed):
    rng = np.random.default_rng(seed)
    coords = sprinkle_slab2d(N, rng, t_extent=T_EXTENT, x_extent=X_EXTENT)
    C = causal_matrix(coords)
    iDelta = pauli_jordan(green_retarded_2d(C))
    W = sj_state(iDelta).W

    # GEOMETRY-FIXED proper-distance scale (fixed BEFORE any slope) -----------
    vol = 2.0 * T_EXTENT * X_EXTENT
    rho = N / vol
    eps_disc = rho ** -0.5                     # discreteness proper length
    x_lo = X_LO_FRAC * X_EXTENT
    x_hi = X_HI_FRAC * X_EXTENT

    out = {"N": int(N), "seed": int(seed), "rho": float(rho),
           "eps_disc": float(eps_disc), "x_lo": float(x_lo), "x_hi": float(x_hi)}

    # ---- RINDLER half-line cut O = {x > 0} (BW boost) ---------------------
    sub_R = np.where(coords[:, 1] > 0.0)[0]
    if sub_R.size < 8:
        return None
    mk_R = modular_kernel(W, iDelta, sub_R, kappa=None)
    if mk_R is None:
        return None
    K_R = np.real(mk_R.K)
    xp_R = coords[sub_R][:, 1]                  # proper distance to horizon (=x)

    if _HAVE_LIB_UNRUH:
        lf = unruh_proper_law(K_R, xp_R, x_lo=x_lo, x_hi=x_hi, n_bins=N_BINS)
        law = {"law_exponent": lf.law_exponent, "law_r2": lf.law_r2,
               "boost_slope": lf.boost_slope, "boost_r2": lf.boost_r2,
               "centers": lf.centers, "prof": lf.prof, "counts": lf.counts}
    else:
        law = unruh_law_and_slope(K_R, xp_R, x_lo=x_lo, x_hi=x_hi)

    bq, bq_n = boost_quantum_2pi(K_R, xp_R, x_lo=x_lo, x_hi=x_hi)
    ur = unruh_ratio_f034(K_R, xp_R, x_lo=x_lo, x_hi=x_hi)

    out["rindler"] = {
        "n_sub": int(sub_R.size), "n_modes": int(mk_R.n_modes), "S": float(mk_R.S),
        "law_exponent": law["law_exponent"], "law_r2": law["law_r2"],
        "boost_slope": law["boost_slope"], "boost_r2": law["boost_r2"],
        "boost_quantum_2pi": bq, "boost_quantum_nmodes": bq_n,
        "unruh_ratio_f034": ur,
    }

    # ---- CONTROL 1: INTERVAL {0 < x < x0} (BW does NOT apply) --------------
    sub_I = np.where((coords[:, 1] > 0.0) & (coords[:, 1] < INTERVAL_X0))[0]
    interval = None
    if sub_I.size >= 8:
        mk_I = modular_kernel(W, iDelta, sub_I, kappa=None)
        if mk_I is not None:
            K_I = np.real(mk_I.K); xp_I = coords[sub_I][:, 1]
            xhiI = X_HI_FRAC * INTERVAL_X0
            law_I = unruh_law_and_slope(K_I, xp_I, x_lo=X_LO_FRAC * X_EXTENT,
                                        x_hi=xhiI, n_bins=N_BINS)
            interval = {
                "n_sub": int(sub_I.size), "n_modes": int(mk_I.n_modes),
                "law_exponent": law_I["law_exponent"], "law_r2": law_I["law_r2"],
                "boost_slope": law_I["boost_slope"], "boost_r2": law_I["boost_r2"],
            }
    out["interval_control"] = interval

    # ---- CONTROL 2: SHUFFLE (spectrum preserved, geometry destroyed) -------
    K_sh = shuffle_kernel(K_R, seed + 7)
    law_sh = unruh_law_and_slope(K_sh, xp_R, x_lo=x_lo, x_hi=x_hi)
    out["shuffle_control"] = {
        "law_exponent": law_sh["law_exponent"], "law_r2": law_sh["law_r2"],
        "boost_slope": law_sh["boost_slope"], "boost_r2": law_sh["boost_r2"],
    }

    payload = {"centers": law["centers"], "prof": law["prof"],
               "counts": law["counts"], "x_lo": x_lo, "x_hi": x_hi,
               "law_exponent": law["law_exponent"], "boost_slope": law["boost_slope"]}
    return out, payload


# ===========================================================================
# STRETCH: 2D de Sitter static patch -> Gibbons-Hawking 1/(2 pi l)
# ===========================================================================

def run_seed_ds(N, seed, *, l=1.0, rstar_box=2.5, t_extent=0.30, r0=0.6):
    """de Sitter static patch: horizon at r* -> inf, Gibbons-Hawking
    T_dS = 1/(2*pi*l). The patch is ONE-SIDED in the tortoise r* (cut {r*>0} is
    the whole region => no complement => no kernel), so we take an INTERIOR
    horizon-like cut O = {r* > r0} leaving a complement {r* < r0}; the modular
    diagonal vs PROPER tortoise distance (r* - r0) should carry the same
    boost-linear structure (the horizon analogue of Unruh). Measures the law
    exponent + boost slope + the 2*pi boost-quantum."""
    rng = np.random.default_rng(seed)
    coords = sprinkle_ds_static_patch2d(N, rng, l=l, rstar_box=rstar_box,
                                        t_extent=t_extent)
    C = causal_matrix(coords)
    iDelta = pauli_jordan(green_retarded_2d(C))
    W = sj_state(iDelta).W
    rstar = coords[:, 1]
    sub = np.where(rstar > r0)[0]
    if sub.size < 8:
        return None
    mk = modular_kernel(W, iDelta, sub, kappa=None)
    if mk is None:
        return None
    K = np.real(mk.K)
    xp = rstar[sub] - r0                        # proper tortoise distance to dS sub-horizon
    span = rstar_box - r0
    x_lo = X_LO_FRAC * span; x_hi = X_HI_FRAC * span
    law = unruh_law_and_slope(K, xp, x_lo=x_lo, x_hi=x_hi)
    bq, bq_n = boost_quantum_2pi(K, xp, x_lo=x_lo, x_hi=x_hi)
    return {
        "N": int(N), "seed": int(seed), "l": float(l), "rstar_box": float(rstar_box),
        "r0": float(r0), "n_sub": int(sub.size), "n_modes": int(mk.n_modes),
        "law_exponent": law["law_exponent"], "law_r2": law["law_r2"],
        "boost_slope": law["boost_slope"], "boost_r2": law["boost_r2"],
        "boost_quantum_2pi": bq,
    }


# ===========================================================================
# PLOTS
# ===========================================================================

def plot_beta_vs_proper(payload, agg, path):
    centers = np.asarray(payload["centers"]); prof = np.asarray(payload["prof"])
    g = np.isfinite(prof) & (centers > 0) & (prof > 0)
    fig, axs = plt.subplots(1, 2, figsize=(11.8, 4.5))
    ax = axs[0]
    ax.plot(centers[g], prof[g], "s", ms=6, color="C0",
            label="|K(x,x)| modular energy density")
    sl = agg["rindler"]["boost_slope_mean"]
    if np.isfinite(sl) and g.sum() >= 2:
        xx = np.linspace(centers[g].min(), centers[g].max(), 50)
        b0 = np.mean(prof[g]) - sl * np.mean(centers[g])
        ax.plot(xx, sl * xx + b0, "r-", lw=1.4,
                label=f"BW linear, slope={sl:.1f}\nR²={agg['rindler']['boost_r2_mean']:.3f}")
    ax.set_xlabel("proper distance to horizon  $x_{proper}$")
    ax.set_ylabel(r"modular energy density $|K(x,x)|$")
    ax.set_title("(B) Boost diagonal vs GEOMETRY-FIXED proper distance")
    ax.legend(fontsize=8); ax.grid(alpha=0.3)
    # log-log law
    ax2 = axs[1]
    ax2.loglog(centers[g], prof[g], "o", ms=6, color="C2", label="K(x,x)")
    pe = agg["rindler"]["law_exponent_mean"]
    if np.isfinite(pe) and g.sum() >= 2:
        xx = np.logspace(np.log10(centers[g].min()), np.log10(centers[g].max()), 50)
        c = np.mean(np.log(prof[g])) - pe * np.mean(np.log(centers[g]))
        ax2.loglog(xx, np.exp(c) * xx ** pe, "r-", lw=1.4,
                   label=f"$K \\sim x^{{{pe:.2f}}}$ (BW: +1)")
    ax2.loglog(centers[g], centers[g] * (prof[g][0] / centers[g][0]), "k--", lw=1.0,
               alpha=0.6, label="exponent +1 (Unruh $T\\sim 1/x$)")
    ax2.set_xlabel("proper distance $x_{proper}$ (log)")
    ax2.set_ylabel("$|K(x,x)|$ (log)")
    ax2.set_title(f"(A) Unruh law exponent  $p_E$={pe:.2f}")
    ax2.legend(fontsize=8); ax2.grid(alpha=0.3, which="both")
    fig.tight_layout(); fig.savefig(path, dpi=115); plt.close(fig)


def plot_unruh_law(per_rho, agg, ds_agg, path):
    fig, axs = plt.subplots(1, 2, figsize=(11.8, 4.5))
    # left: rho-invariance of the law exponent + boost slope
    ax = axs[0]
    rhos = sorted(per_rho.keys(), key=lambda k: int(k))
    pe = [per_rho[k]["law_exponent_mean"] for k in rhos]
    bs = [per_rho[k]["boost_slope_mean"] for k in rhos]
    xr = [int(k) for k in rhos]
    ax.plot(xr, pe, "o-", color="C2", label="law exponent $p_E$")
    ax.axhline(1.0, color="k", ls="--", lw=1.0, alpha=0.6, label="BW $p_E=1$")
    ax.set_xlabel("N (rho sweep)")
    ax.set_ylabel("Unruh law exponent $p_E$")
    ax.set_title(f"(A) law exponent rho-invariance (CV={agg['law_exp_cv']:.2f})")
    ax.legend(fontsize=8); ax.grid(alpha=0.3)
    ax.set_ylim(0, 1.6)
    # right: 2pi coefficient routes
    ax2 = axs[1]
    R = agg["rindler"]
    routes = ["boost_quantum\n$\\epsilon_k\\langle x\\rangle_k$",
              "unruh_ratio\n(F-034)"]
    vals = [R["boost_quantum_2pi_mean"], R["unruh_ratio_f034_mean"]]
    errs = [R["boost_quantum_2pi_sd"], R["unruh_ratio_f034_sd"]]
    ax2.bar(range(len(vals)), vals, yerr=errs, color=["C0", "C1"], alpha=0.8,
            capsize=4)
    ax2.axhline(TWO_PI, color="r", ls="--", lw=1.4, label=f"$2\\pi$={TWO_PI:.3f}")
    ax2.set_xticks(range(len(routes))); ax2.set_xticklabels(routes, fontsize=8)
    ax2.set_ylabel("coefficient (geometry-fixed)")
    ax2.set_title("(C) absolute $2\\pi$ coefficient routes")
    ax2.legend(fontsize=8); ax2.grid(alpha=0.3, axis="y")
    if ds_agg is not None:
        ax2.text(0.5, 0.92, f"dS static patch $p_E$={ds_agg['law_exponent_mean']:.2f}",
                 transform=ax2.transAxes, fontsize=7, ha="center",
                 bbox=dict(boxstyle="round", fc="wheat", alpha=0.6))
    fig.tight_layout(); fig.savefig(path, dpi=115); plt.close(fig)


# ===========================================================================
# MAIN
# ===========================================================================

def main(argv=None):
    import argparse
    ap = argparse.ArgumentParser(
        description="NCG<->semiclassical Unruh temperature law from SJ modular flow.",
        epilog="smoke: python3 calc.py --smoke  (N=400, 2 seeds, single rho, no dS)")
    ap.add_argument("--smoke", action="store_true",
                    help="tiny run for CI/dev (N=400, 2 seeds, single rho, no dS).")
    ap.add_argument("--Ns", type=int, nargs="+", default=None,
                    help="rho sweep as N values (default 600 1000 1400).")
    ap.add_argument("--seeds", type=int, default=5)
    ap.add_argument("--no-ds", action="store_true", help="skip the dS stretch.")
    args = ap.parse_args(argv)

    t_start = time.time()
    if args.smoke:
        Ns = [400]; n_seeds = 2; do_ds = False
    else:
        Ns = args.Ns if args.Ns else [600, 1000, 1400]
        n_seeds = args.seeds; do_ds = not args.no_ds
    Ns = [min(int(N), 1500) for N in Ns]      # dense eigh cap (N<=1500)

    per_seed = []; payload_rep = None; rep_n_sub = -1; skipped = []
    for N in Ns:
        for s in range(n_seeds):
            if (time.time() - t_start) > WALL_CAP_S:
                skipped.append({"N": int(N), "seed": int(s), "reason": "wall cap"})
                continue
            res = run_seed_rindler(N, seed=1000 + 17 * s + N)
            if res is None:
                continue
            out, payload = res
            per_seed.append(out)
            if out["rindler"]["n_sub"] > rep_n_sub:
                rep_n_sub = out["rindler"]["n_sub"]; payload_rep = payload
            _flush_partial(per_seed, [], Ns, n_seeds, t_start, "running")

    # ---- dS STRETCH (budget permitting) -----------------------------------
    ds_seed = []; ds_skipped = False
    if do_ds:
        for N in Ns:
            for s in range(n_seeds):
                if (time.time() - t_start) > WALL_CAP_S * 0.92:
                    ds_skipped = True; break
                r = run_seed_ds(N, seed=2000 + 17 * s + N)
                if r is not None:
                    ds_seed.append(r)
                _flush_partial(per_seed, ds_seed, Ns, n_seeds, t_start, "running")
            if ds_skipped:
                break

    # ---- aggregate (Rindler) ----------------------------------------------
    def agg_block(key, sub):
        vals = [d[sub].get(key) for d in per_seed if d.get(sub)]
        return _m(vals), _sd(vals)

    aggregate = {"rindler": {}, "interval_control": {}, "shuffle_control": {}}
    rind_keys = ["law_exponent", "law_r2", "boost_slope", "boost_r2",
                 "boost_quantum_2pi", "unruh_ratio_f034", "n_sub", "n_modes", "S"]
    for k in rind_keys:
        mu, sd = agg_block(k, "rindler")
        aggregate["rindler"][k + "_mean"] = mu
        aggregate["rindler"][k + "_sd"] = sd
    for blk in ("interval_control", "shuffle_control"):
        for k in ["law_exponent", "law_r2", "boost_slope", "boost_r2"]:
            mu, sd = agg_block(k, blk)
            aggregate[blk][k + "_mean"] = mu
            aggregate[blk][k + "_sd"] = sd

    # per-rho (rho-invariance of law exponent + boost slope)
    per_rho = {}
    for N in sorted(set(Ns)):
        sub = [d for d in per_seed if d["N"] == N]
        if sub:
            per_rho[str(N)] = {
                "law_exponent_mean": _m([d["rindler"]["law_exponent"] for d in sub]),
                "boost_slope_mean": _m([d["rindler"]["boost_slope"] for d in sub]),
                "boost_r2_mean": _m([d["rindler"]["boost_r2"] for d in sub]),
                "boost_quantum_2pi_mean": _m([d["rindler"]["boost_quantum_2pi"] for d in sub]),
                "n_seeds": len(sub),
            }

    # CV of the law exponent and boost slope across rho (rho-invariance)
    pexps = [per_rho[k]["law_exponent_mean"] for k in per_rho
             if np.isfinite(per_rho[k]["law_exponent_mean"])]
    law_exp_cv = (float(np.std(pexps) / np.abs(np.mean(pexps)))
                  if len(pexps) >= 2 and np.mean(pexps) != 0 else float("nan"))
    slopes = [per_rho[k]["boost_slope_mean"] for k in per_rho
              if np.isfinite(per_rho[k]["boost_slope_mean"])]
    slope_cv = (float(np.std(slopes) / np.abs(np.mean(slopes)))
                if len(slopes) >= 2 and np.mean(slopes) != 0 else float("nan"))
    aggregate["law_exp_cv"] = law_exp_cv
    aggregate["boost_slope_cv"] = slope_cv

    # dS aggregate
    ds_agg = None
    if ds_seed:
        ds_agg = {
            "law_exponent_mean": _m([d["law_exponent"] for d in ds_seed]),
            "law_exponent_sd": _sd([d["law_exponent"] for d in ds_seed]),
            "law_r2_mean": _m([d["law_r2"] for d in ds_seed]),
            "boost_slope_mean": _m([d["boost_slope"] for d in ds_seed]),
            "boost_r2_mean": _m([d["boost_r2"] for d in ds_seed]),
            "boost_quantum_2pi_mean": _m([d["boost_quantum_2pi"] for d in ds_seed]),
            "n_seeds": len(ds_seed),
        }

    # ===================================================================
    # VERDICT (pre-registered)
    # ===================================================================
    R = aggregate["rindler"]; I = aggregate["interval_control"]
    SH = aggregate["shuffle_control"]
    v = {}
    # (A) Unruh LAW exponent ~ +1 (energy density linear in proper distance).
    # BW predicts EXACTLY +1; we require within 0.20 (exponent > 0.80) to count
    # the Unruh 1/x law shape as genuinely RECOVERED -- a 30% deficit (eps-units
    # log-compression of the surrogate) is NOT the Unruh law.
    v["law_exponent_dev_from_1"] = (abs(R["law_exponent_mean"] - 1.0)
                                    if np.isfinite(R["law_exponent_mean"]) else float("nan"))
    v["law_exponent_unruh"] = bool(np.isfinite(R["law_exponent_mean"])
        and abs(R["law_exponent_mean"] - 1.0) < 0.20 and R["law_r2_mean"] > 0.85)
    # the diagonal IS monotone-increasing & log-linear (the WEAKER, qualitative
    # boost-shape signal) even when the exponent misses +1:
    v["law_monotone_loglinear"] = bool(np.isfinite(R["law_exponent_mean"])
        and R["law_exponent_mean"] > 0.5 and R["law_r2_mean"] > 0.85)
    v["law_exponent_rho_invariant"] = bool(np.isfinite(law_exp_cv) and law_exp_cv < 0.20)
    # (B) boost geometry present, rho-invariant slope
    v["boost_geometry"] = bool(np.isfinite(R["boost_r2_mean"])
        and R["boost_r2_mean"] > 0.85 and (R["boost_slope_mean"] or 0) > 0)
    v["boost_slope_cv"] = slope_cv
    v["boost_rho_invariant"] = bool(np.isfinite(slope_cv) and slope_cv < 0.15)
    # (C) absolute 2*pi coefficient (best of the geometry-fixed routes)
    bq = R["boost_quantum_2pi_mean"]; ur = R["unruh_ratio_f034_mean"]
    route_errs = {}
    if np.isfinite(bq):
        route_errs["boost_quantum"] = abs(bq - TWO_PI) / TWO_PI
    if np.isfinite(ur):
        route_errs["unruh_ratio_f034"] = abs(ur - TWO_PI) / TWO_PI
    best_route = min(route_errs, key=route_errs.get) if route_errs else None
    best_err = route_errs[best_route] if best_route else float("nan")
    v["twopi_coefficient_routes"] = route_errs
    v["twopi_best_route"] = best_route
    v["twopi_best_rel_err"] = float(best_err)
    v["unruh_2pi_recovered"] = bool(np.isfinite(best_err) and best_err < 0.20)
    # (D) controls
    v["interval_law_fails"] = bool(I.get("law_r2_mean") is None
        or not np.isfinite(I.get("law_r2_mean", float("nan")))
        or I.get("boost_r2_mean", 1.0) < 0.5
        or abs(I.get("law_exponent_mean", 99) - 1.0) > 0.5)
    v["shuffle_law_fails"] = bool(not np.isfinite(SH["boost_r2_mean"])
        or SH["boost_r2_mean"] < 0.5)

    control_clean = v["interval_law_fails"] and v["shuffle_law_fails"]
    # STRICT law recovery: the Unruh exponent hits +1 (within 0.20), rho-invariant,
    # boost geometry present + rho-invariant, controls clean.
    law_recovered = (v["law_exponent_unruh"] and v["law_exponent_rho_invariant"]
                     and v["boost_geometry"] and v["boost_rho_invariant"]
                     and control_clean)
    # WEAK boost-shape signal: monotone log-linear diagonal, rho-invariant slope,
    # clean controls -- present even when the exponent misses +1 (eps-compression).
    boost_shape = (v["law_monotone_loglinear"] and v["boost_geometry"]
                   and v["boost_rho_invariant"] and control_clean)
    if law_recovered and v["unruh_2pi_recovered"]:
        correspondence = "genuine-positive"   # Unruh law shape + absolute 2*pi
    elif law_recovered:
        correspondence = "partial"            # Unruh LAW shape (exp~1), no abs 2*pi
    elif boost_shape:
        # boost geometry + monotone diagonal survive & fail controls, but the
        # absolute Unruh law (exponent +1) AND the 2*pi coefficient are BOTH
        # missed by the surrogate => the F-034 tautology persists (the only clean
        # invariant is the construction-driven boost diagonal, no absolute Unruh).
        correspondence = "tautology"
    else:
        correspondence = "negative"
    v["correspondence"] = correspondence
    v["law_recovered"] = bool(law_recovered)
    v["boost_shape_qualitative"] = bool(boost_shape)
    v["control_clean"] = bool(control_clean)

    elapsed = time.time() - t_start
    results = {
        "schema": "ncg-kms-unruh/v1",
        "status": "complete",
        "calc": ("NCG<->semiclassical: Unruh temperature law T=1/(2pi x) from the "
                 "SJ modular flow on a 2D Rindler causal set (geometry-fixed)"),
        "config": {
            "Ns": Ns, "n_seeds": n_seeds, "T_extent": T_EXTENT,
            "X_extent": X_EXTENT, "rindler_cut": "x>0 (half-line horizon at x=0)",
            "interval_cut": f"0<x<{INTERVAL_X0} (BW does not apply)",
            "shuffle": "Haar-orthogonal conjugation of K (spectrum preserved)",
            "kappa": None, "two_pi": TWO_PI, "wall_cap_s": WALL_CAP_S,
            "x_lo_frac": X_LO_FRAC, "x_hi_frac": X_HI_FRAC, "n_bins": N_BINS,
            "proper_distance_scale": "GEOMETRY-FIXED: eps_disc=rho^-1/2, x in [x_lo,x_hi] proper, fixed BEFORE slope",
            "ds_stretch": bool(do_ds), "ds_skipped": bool(ds_skipped),
            "lib_unruh_primitive": bool(_HAVE_LIB_UNRUH),
        },
        "references_verified": [
            "gr-qc/9406019", "1712.04227", "1611.10281", "0905.2562",
            "2008.07697", "1205.3855",
        ],
        "per_seed": per_seed,
        "per_rho": per_rho,
        "aggregate": aggregate,
        "ds_per_seed": ds_seed,
        "ds_aggregate": ds_agg,
        "verdict": v,
        "skipped": skipped,
        "caveat": ("The SJ modular kernel is a SURROGATE Dirac in modular-energy "
                   "units eps=ln[mu/(mu-1)] (Casini-Huerta 0905.2562) lifted to the "
                   "site basis; beta_KMS=1 is a Tomita-Takesaki TAUTOLOGY (F-034). "
                   "The proper-distance scale is GEOMETRY-FIXED (sprinkling density "
                   "+ slab proper length, fixed BEFORE the slope), NEVER tuned to "
                   "2*pi. The Unruh LAW SHAPE (exponent ~+1, T~1/x) is the "
                   "recoverable geometric content; the absolute 2*pi coefficient "
                   "requires the boost-rapidity normalisation the surrogate does NOT "
                   "carry -- reported via geometry-fixed routes, NOT claimed if off. "
                   "2D massless, finite N<=1500 dense: a TREND (rho-invariance), not "
                   "the N->inf value; discrete corrections O(1/sqrt N)."),
        "elapsed_s": float(elapsed),
    }
    write_results_atomic(results, os.path.join(OUTDIR, "results.json"))

    if payload_rep is not None:
        plot_beta_vs_proper(payload_rep, aggregate,
                            os.path.join(PLOTDIR, "beta_vs_proper_distance.png"))
        plot_unruh_law(per_rho, aggregate, ds_agg,
                       os.path.join(PLOTDIR, "unruh_law.png"))

    ds_msg = (f"  dS p_E={ds_agg['law_exponent_mean']:.2f}" if ds_agg
              else ("  dS=SKIPPED" if ds_skipped else "  dS=off"))
    print(f"[done] correspondence={correspondence}  "
          f"law_exp={R['law_exponent_mean']:.3f} (cv={law_exp_cv:.2f}, R2={R['law_r2_mean']:.3f})  "
          f"boost_slope={R['boost_slope_mean']:.2f} (cv={slope_cv:.3f}, R2={R['boost_r2_mean']:.3f})  "
          f"2pi: bq={bq:.2f} ur={ur:.3f} best_err={best_err:.2f} (2pi={TWO_PI:.3f})  "
          f"I_lawexp={I.get('law_exponent_mean', float('nan')):.2f} I_r2={I.get('boost_r2_mean', float('nan')):.2f} "
          f"SH_r2={SH['boost_r2_mean']:.3f}{ds_msg}  elapsed={elapsed:.1f}s")
    return results


def _flush_partial(per_seed, ds_seed, Ns, n_seeds, t_start, status):
    partial = {
        "schema": "ncg-kms-unruh/v1",
        "status": status,
        "calc": ("NCG<->semiclassical: Unruh temperature law from SJ modular flow "
                 "(2D Rindler causal set)"),
        "config": {"Ns": Ns, "n_seeds": n_seeds},
        "per_seed": per_seed,
        "ds_per_seed": ds_seed,
        "elapsed_s": float(time.time() - t_start),
    }
    write_results_atomic(partial, os.path.join(OUTDIR, "results.json"))


if __name__ == "__main__":
    main()
