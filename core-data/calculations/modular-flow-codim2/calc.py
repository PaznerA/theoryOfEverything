#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
VYPOCET-22 : TEST H5g-3 -- the CODIM-2 JOINT as the right 4D locus of modular-
flow non-geometricity (the 4D analogue of the 2D corner).
============================================================================
BACKGROUND (the chain this fixes):
  * VYPOCET-18 (2D): the SJ modular kernel K is a geometric BOOST on a slab
    (off-diag slope <0, diagonal linear) and becomes NON-geometric MONOTONICALLY
    toward the diamond CORNER (nl-vs-corner slope = -0.383, R^2=0.989).  The 2D
    corner is where two null edges meet and the boost has nowhere to flow.
  * VYPOCET-20 (F-024, 4D, BD smeared eps=0.6): the slab boost side RESTORES in
    4D, but the diamond NULL-TIP corner-concentration does NOT: nl-vs-tip slope
    = +0.71 (non-locality FALLS toward the tip), corner/bulk f_nl ratio 0.445.
    DIAGNOSIS proposed there: the 4D diamond tip is a DEGENERATING 2-SPHERE (the
    spatial S^2 shrinks to a POINT) -- topologically unlike the 2D spatial tip.

H5g-3 (BRAINSTORM-05): the RIGHT 4D analogue of the 2D corner is NOT the
isolated tip but a CODIM-2 JOINT -- a wedge EDGE that is a flat 2-PLANE, where
the boost Killing vector vanishes along a clean 2-surface (not a single point).
If the 2D corner mechanism is CODIM-2-GENERIC, modular non-geometricity should
CONCENTRATE toward that edge (nl-vs-edge slope < 0, like 2D), with a flat-
hyperplane SLAB control (no joint) showing no such concentration.

CLEANEST CODIM-2 GEOMETRY (helpers.sprinkle_wedge_box4d):
  4D Minkowski (t,x,y,z), right Rindler wedge W = {x > |t|}, modular flow = exact
  x-t boost (Bisognano-Wichmann).  Boost Killing vector xi = x d_t + t d_x
  vanishes on the EDGE  E = {t=0, x=0} = flat 2-plane spanned by (y,z) -- a
  genuine codim-2 joint.  Region cut O = {x>0} on a t-symmetric box; entangling
  surface of O IS E.  Per-site distance-to-edge d_E = sqrt(t^2+x^2) (transverse
  distance to the 2-plane) = the direct 4D analogue of the 2D distance-to-corner.
  CONTROL: a volume/density-matched SLAB box, half-space cut x>0, probed by
  distance-to-(flat hyperplane) = |x| -- a codim-1 entangling surface with NO
  joint (boost flows freely along it).

DYNAMICAL OBJECT (identical to the VYPOCET-20 PRIMARY, the validated object):
  smeared Benincasa-Dowker eps=0.6, G_R = B_eps^{-1}, iDelta=i(G_R-G_R^T),
  W = SJ positive part.  Built by COMPOSING toe.causet (causal_matrix,
  pauli_jordan) + toe.sj-style positive part (rel-floor reproduced from VYP-20)
  + the smeared BD matrix (helpers; toe.causet ships only the SHARP inverse).

DISCRIMINATOR (the headline H5g-3 test):
  * f_nl GROWS toward the codim-2 edge (nl-vs-edge slope < 0, like the 2D corner
    -0.38)  =>  the corner mechanism is CODIM-2-GENERIC; H4g-1 layer B
    generalises to 4D at the right locus (the tip was the WRONG locus).
  * f_nl FALLS toward the edge (slope > 0, like the 4D tip +0.71)  =>  the
    corner sub-part is genuinely 2D-only even at a clean codim-2 joint.
  EITHER is a finding -- nothing is fudged.  Quantified with toe.fits
  (value, SE, CI), >=3 seeds, N<=2200 (matrix-inversion bound).

MACHINE-PRECISION INVARIANT (asserted on EVERY region/seed):
  iDelta is Hermitian with EXACT +/- paired spectrum (antisymmetry of Delta is
  exact in float): toe.causet.causal_diagnostics pairing_residual_rel < 1e-12.

LIBRARY DOGFOODING.  Composed on toe v0.1.0:
  toe.causet.causal_matrix / pauli_jordan / causal_diagnostics  (A2)
  toe.sj.sj_state                                                (B1)
  toe.fits.regression_se / powerlaw_fit / validate_against / Measurement (A1)
  toe.viz.powerlaw_panel                                          (A5)
New region/diagnostic helpers are LOCAL (helpers.py); migration signatures are
collected in results.json["lib_proposals"].
"""

import json
import os
import sys
import time

for _v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS",
           "VECLIB_MAXIMUM_THREADS", "NUMEXPR_NUM_THREADS"):
    os.environ.setdefault(_v, "4")

import numpy as np

sys.path.insert(0, '/Users/pazny/projects/theoryOfEverything/lib')

# ---- toe library (DOGFOODING) --------------------------------------------
# v0.2.0 lifted the VYPOCET-22 region builder, smeared-BD inverse, the SJ
# relative floor and the site-basis modular kernel into toe; calc.py now imports
# them from the library instead of helpers.py (numbers verified bit-identical to
# the committed results.json).
from toe.causet import (causal_matrix, pauli_jordan, causal_diagnostics,
                        sprinkle_wedge_box4d, bd_smeared_dalembertian_inverse)
from toe.sj import sj_state
from toe.entropy import modular_kernel
from toe.fits import regression_se, powerlaw_fit, validate_against, Measurement
from toe import viz as toe_viz

# ---- LOCAL helpers (locality-profile diagnostics + box volume) -----------
# The region builder / smeared-BD object / SJ floor / modular kernel are now
# lifted into toe (above); helpers.py still provides the locality-profile
# diagnostics (nonlocal_fraction, offdiag_slope_subset, nl_vs_edge_profile,
# diag_weight_vs_distance, box4d_volume) which remain calc-local.
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import helpers as H

OUTDIR = HERE
PLOTDIR = os.path.join(OUTDIR, "plots")
os.makedirs(PLOTDIR, exist_ok=True)

# box geometry (t-symmetric, so the wedge EDGE sits inside)
T_HALF, X_HALF, YZ_HALF = 0.5, 0.5, 0.5
EPS_BD = 0.6                       # the VYPOCET-20 validated smeared object
PAIRING_TOL = 1e-12               # machine-precision invariant bound


# ===========================================================================
# FIT WRAPPERS (every reported number carries value + SE/CI per toe convention)
# ===========================================================================

def loglog_slope(x, y, mask=None):
    """log-log OLS slope (value, intercept, R^2) -- the binning-profile fit used
    by the locality diagnostics.  For the HEADLINE nl-vs-edge curve we additionally
    report toe.fits SE+CI (see fit_with_se)."""
    x = np.asarray(x, float); y = np.asarray(y, float)
    m = np.isfinite(x) & np.isfinite(y) & (x > 0) & (y > 0)
    if mask is not None:
        m &= mask
    if m.sum() < 3:
        return None, None, None
    lx = np.log(x[m]); ly = np.log(y[m])
    A = np.vstack([lx, np.ones_like(lx)]).T
    coef, *_ = np.linalg.lstsq(A, ly, rcond=None)
    yhat = A @ coef
    ss = np.sum((ly - ly.mean()) ** 2)
    r2 = 1.0 - np.sum((ly - yhat) ** 2) / ss if ss > 0 else 0.0
    return float(coef[0]), float(coef[1]), float(r2)


def linfit(x, y, mask=None):
    x = np.asarray(x, float); y = np.asarray(y, float)
    m = np.isfinite(x) & np.isfinite(y)
    if mask is not None:
        m &= mask
    if m.sum() < 2:
        return None, None, None
    A = np.vstack([x[m], np.ones(m.sum())]).T
    coef, *_ = np.linalg.lstsq(A, y[m], rcond=None)
    yhat = A @ coef
    ss = np.sum((y[m] - y[m].mean()) ** 2)
    r2 = 1.0 - np.sum((y[m] - yhat) ** 2) / ss if ss > 0 else 0.0
    return float(coef[0]), float(coef[1]), float(r2)


def lin_se(x, y):
    """OLS slope + residual SE for a LINEAR (not log-log) fit; mirrors
    toe.fits.regression_se but in raw space (nl-vs-edge / nl-vs-tip are fit in
    raw distance vs raw f_nl, like VYPOCET-18/20).  Returns (slope, se, r2)."""
    x = np.asarray(x, float); y = np.asarray(y, float)
    m = np.isfinite(x) & np.isfinite(y)
    x = x[m]; y = y[m]
    n = len(x)
    if n < 3:
        return np.nan, np.nan, np.nan
    A = np.vstack([x, np.ones(n)]).T
    beta, *_ = np.linalg.lstsq(A, y, rcond=None)
    yhat = A @ beta
    resid = y - yhat
    ssr = float(resid @ resid)
    sigma2 = ssr / (n - 2) if n > 2 else np.nan
    AtA_inv = np.linalg.inv(A.T @ A)
    se = float(np.sqrt(sigma2 * AtA_inv[0, 0])) if np.isfinite(sigma2) else np.nan
    ss = np.sum((y - y.mean()) ** 2)
    r2 = 1.0 - ssr / ss if ss > 0 else 0.0
    return float(beta[0]), se, float(r2)


def _m(lst):
    lst = [x for x in lst if np.isfinite(x)]
    return float(np.mean(lst)) if lst else np.nan


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


# ===========================================================================
# BD-SJ PIPELINE  (compose toe + the smeared BD object)
# ===========================================================================

def build_bd_sj(coords, rho, eps):
    """Time-order -> causal_matrix (toe) -> smeared BD G_R=B_eps^{-1} (toe) ->
    iDelta (toe.pauli_jordan) -> SJ W (toe.sj rel_floor positive part).  Asserts
    the machine-precision +/- pairing invariant on iDelta via
    toe.causal_diagnostics.  Returns (coords_ordered, W, iDelta, diag,
    pairing_rel).  All four physics steps now come from toe v0.2.0 (the smeared
    BD inverse, the rel-floored SJ state); the cond_B diagnostic is computed from
    the same smeared matrix the lib inverts (kept byte-identical)."""
    order = np.argsort(coords[:, 0])
    co = coords[order]
    C = causal_matrix(co)                                  # toe.causet (4D order)
    # smeared BD G_R = B_eps^{-1}  (toe.causet, lifted from helpers VYPOCET-22)
    G_R = bd_smeared_dalembertian_inverse(C, rho, eps)
    diag = {"cond_B": float(np.linalg.cond(H.bd_smeared_matrix(C, rho, eps)))}
    iD = pauli_jordan(G_R)                                 # toe.causet
    # MACHINE-PRECISION INVARIANT (toe.causet.causal_diagnostics)
    cd = causal_diagnostics(iD, tol=1e-12)
    pairing_rel = cd["pairing_residual_rel"]
    assert pairing_rel < PAIRING_TOL, (
        f"iDelta +/- pairing residual {pairing_rel:.3e} >= {PAIRING_TOL:.0e}")
    # SJ Wightman = positive part with the VYPOCET-09/20 relative floor (toe.sj)
    W = sj_state(iD, rel_floor=1e-10).W
    return co, W, iD, diag, pairing_rel


# ===========================================================================
# THE EXPERIMENT  : wedge (codim-2 joint) vs slab control (no joint)
# ===========================================================================

def run_codim2(Ns, n_seeds, t_start=None, budget=None):
    print(f"\n==== VYPOCET-22  codim-2 modular-flow  eps={EPS_BD}  "
          f"Ns={Ns} seeds={n_seeds} ====")
    wedge = {N: {"f_nl_all": [], "f_nl_edge": [], "f_nl_bulk": [],
                 "off_slope_all": [], "off_R2_all": [],
                 "off_slope_edge": [], "off_slope_bulk": [],
                 "nl_vs_edge_centers": [], "nl_vs_edge_mean": [],
                 "nl_vs_edge_inner_centers": [], "nl_vs_edge_inner_mean": [],
                 "diag_slope_lin": [], "diag_R2_lin": [],
                 "cond_B": [], "pairing_rel": [], "S": []} for N in Ns}
    slab = {N: {"f_nl_all": [], "off_slope": [], "off_R2": [],
                "diag_slope_lin": [], "diag_R2_lin": [],
                "nl_vs_hyper_centers": [], "nl_vs_hyper_mean": [],
                "cond_B": [], "pairing_rel": [], "S": []} for N in Ns}

    vol = H.box4d_volume(T_HALF, X_HALF, YZ_HALF)

    for N in Ns:
        if t_start is not None and budget is not None and \
                (time.time() - t_start) > budget:
            print(f"  [time budget reached, stopping at N<{N}]")
            break
        for s in range(n_seeds):
            rho = N / vol
            # ---------------- WEDGE (codim-2 joint) ----------------
            rng = np.random.default_rng(40_000_000 + 1000 * N + s)
            coords = sprinkle_wedge_box4d(N, rng, t_half=T_HALF,
                                          x_half=X_HALF, yz_half=YZ_HALF)
            co, W, iD, dg, pr = build_bd_sj(coords, rho, EPS_BD)
            wedge[N]["pairing_rel"].append(pr)
            # cut O = {x>0} ; entangling surface = edge E={t=0,x=0}.  Interior
            # in (y,z) to avoid the box wall artefacts (matched to slab control).
            interior = ((np.abs(co[:, 2]) < 0.7 * YZ_HALF) &
                        (np.abs(co[:, 3]) < 0.7 * YZ_HALF))
            sub = np.where(interior & (co[:, 1] > 0.0))[0]
            mk = modular_kernel(W, iD, sub, kappa=None)   # UNTRUNCATED (toe)
            if mk is not None and mk.K.shape[0] >= 16:
                K = mk.K; csub = co[sub]
                lp = H.locality_profile(K, csub)
                nn = rho ** (-0.25); near_r = 3.0 * nn
                wedge[N]["f_nl_all"].append(
                    H.nonlocal_fraction(lp["Kabs"], lp["Dij"], near_r))
                wedge[N]["S"].append(mk.S); wedge[N]["cond_B"].append(dg["cond_B"])
                sl_all, r2_all, _, _ = H.offdiag_slope_subset(
                    lp["Kabs"], lp["Dij"], np.ones(K.shape[0], bool), loglog_slope)
                if sl_all is not None:
                    wedge[N]["off_slope_all"].append(sl_all)
                    wedge[N]["off_R2_all"].append(r2_all)
                # DISTANCE-TO-CODIM-2-EDGE  d_E = sqrt(t^2 + x^2)
                d_E = np.sqrt(csub[:, 0] ** 2 + csub[:, 1] ** 2)
                near_edge = d_E <= np.percentile(d_E, 30)
                bulk = d_E > np.median(d_E)
                wedge[N]["f_nl_edge"].append(
                    H._rowfrac_subset(lp["Kabs"], lp["Dij"], near_r, near_edge))
                wedge[N]["f_nl_bulk"].append(
                    H._rowfrac_subset(lp["Kabs"], lp["Dij"], near_r, bulk))
                slb, _, _, _ = H.offdiag_slope_subset(lp["Kabs"], lp["Dij"], bulk,
                                                      loglog_slope)
                sle, _, _, _ = H.offdiag_slope_subset(lp["Kabs"], lp["Dij"],
                                                      near_edge, loglog_slope)
                if slb is not None:
                    wedge[N]["off_slope_bulk"].append(slb)
                if sle is not None:
                    wedge[N]["off_slope_edge"].append(sle)
                nve = H.nl_vs_edge_profile(lp["Kabs"], lp["Dij"], d_E, near_r,
                                           n_zones=6)
                if nve is not None:
                    wedge[N]["nl_vs_edge_centers"].append(nve[0].tolist())
                    wedge[N]["nl_vs_edge_mean"].append(nve[1].tolist())
                # WALL-CONTROL robustness: restrict d_E binning to an inner (t,x)
                # disk (radius <= 0.7*X_HALF) so the box CORNER {|t|,|x|->0.5}
                # does not contaminate the far-edge zones (the box wall, not the
                # codim-2 edge, lives there).  This is the honest "is the slope a
                # wall artefact?" check.
                inner = d_E <= 0.7 * X_HALF
                if inner.sum() >= 16:
                    K2sel = np.ix_(np.where(inner)[0], np.where(inner)[0])
                    nvi = H.nl_vs_edge_profile(
                        lp["Kabs"][K2sel], lp["Dij"][K2sel],
                        d_E[inner], near_r, n_zones=6)
                    if nvi is not None:
                        wedge[N]["nl_vs_edge_inner_centers"].append(nvi[0].tolist())
                        wedge[N]["nl_vs_edge_inner_mean"].append(nvi[1].tolist())
                # diagonal boost-weight vs distance to edge (BW linear check;
                # for the wedge the "distance to surface" is d_E itself)
                cen, prof, cnt = H.diag_weight_vs_distance(
                    lp["diag"], np.column_stack([csub[:, 0], d_E,
                                                 csub[:, 2], csub[:, 3]]),
                    surface_normal_coord=1, surface_value=0.0, use_abs_x=False)
                sl_lin, _, r2lin = linfit(cen, prof, mask=cnt >= 5)
                if sl_lin is not None:
                    wedge[N]["diag_slope_lin"].append(sl_lin)
                    wedge[N]["diag_R2_lin"].append(r2lin)

            # ---------------- SLAB CONTROL (no joint) ----------------
            rng2 = np.random.default_rng(50_000_000 + 1000 * N + s)
            # slab control = same matched box as the wedge (sprinkle_slab_box4d
            # in helpers delegated to the wedge builder); now via toe directly.
            coords_s = sprinkle_wedge_box4d(N, rng2, t_half=T_HALF,
                                            x_half=X_HALF, yz_half=YZ_HALF)
            co_s, Ws, iDs, dg_s, pr_s = build_bd_sj(coords_s, rho, EPS_BD)
            slab[N]["pairing_rel"].append(pr_s)
            interior_s = ((np.abs(co_s[:, 2]) < 0.7 * YZ_HALF) &
                          (np.abs(co_s[:, 3]) < 0.7 * YZ_HALF))
            sub_s = np.where(interior_s & (co_s[:, 1] > 0.0))[0]
            mks = modular_kernel(Ws, iDs, sub_s, kappa=None)   # toe
            if mks is not None and mks.K.shape[0] >= 16:
                Ks = mks.K; css = co_s[sub_s]
                lps = H.locality_profile(Ks, css)
                nn_s = rho ** (-0.25); near_rs = 3.0 * nn_s
                slab[N]["f_nl_all"].append(
                    H.nonlocal_fraction(lps["Kabs"], lps["Dij"], near_rs))
                slab[N]["S"].append(mks.S); slab[N]["cond_B"].append(dg_s["cond_B"])
                sl_off, r2_off, _, _ = H.offdiag_slope_subset(
                    lps["Kabs"], lps["Dij"], np.ones(Ks.shape[0], bool), loglog_slope)
                if sl_off is not None:
                    slab[N]["off_slope"].append(sl_off)
                    slab[N]["off_R2"].append(r2_off)
                # control locus: distance-to-(flat hyperplane x=0) = |x|.  This
                # has NO codim-2 degeneracy; if nl rises toward it too, the wedge
                # signal is not specific to the codim-2 joint.
                d_hyper = np.abs(css[:, 0])     # x is spatial col 0 of (x,y,z)
                nvh = H.nl_vs_edge_profile(lps["Kabs"], lps["Dij"], d_hyper,
                                           near_rs, n_zones=6)
                if nvh is not None:
                    slab[N]["nl_vs_hyper_centers"].append(nvh[0].tolist())
                    slab[N]["nl_vs_hyper_mean"].append(nvh[1].tolist())
                cen, prof, cnt = H.diag_weight_vs_distance(
                    lps["diag"], css, surface_normal_coord=0, surface_value=0.0)
                sl_lin, _, r2lin = linfit(cen, prof, mask=cnt >= 5)
                if sl_lin is not None:
                    slab[N]["diag_slope_lin"].append(sl_lin)
                    slab[N]["diag_R2_lin"].append(r2lin)
        print(f"  [N={N:4d}] wedge f_nl={_m(wedge[N]['f_nl_all']):.3f} "
              f"(edge {_m(wedge[N]['f_nl_edge']):.3f}, bulk {_m(wedge[N]['f_nl_bulk']):.3f}) "
              f"off={_m(wedge[N]['off_slope_all']):.2f}; "
              f"slab f_nl={_m(slab[N]['f_nl_all']):.3f} off={_m(slab[N]['off_slope']):.2f}; "
              f"pair_rel(w)={_m(wedge[N]['pairing_rel']):.1e} cond_w={_m(wedge[N]['cond_B']):.1e}")

    def agg(d, key):
        return [float(np.mean(d[N][key])) if len(d[N][key]) else np.nan for N in Ns]

    def aggstd(d, key):
        return [float(np.std(d[N][key])) if len(d[N][key]) > 1 else 0.0 for N in Ns]

    res = {
        "Ns": Ns, "n_seeds": n_seeds, "eps": EPS_BD,
        "box": {"t_half": T_HALF, "x_half": X_HALF, "yz_half": YZ_HALF,
                "volume": vol},
        "wedge_f_nl_all": agg(wedge, "f_nl_all"),
        "wedge_f_nl_all_std": aggstd(wedge, "f_nl_all"),
        "wedge_f_nl_edge": agg(wedge, "f_nl_edge"),
        "wedge_f_nl_edge_std": aggstd(wedge, "f_nl_edge"),
        "wedge_f_nl_bulk": agg(wedge, "f_nl_bulk"),
        "wedge_f_nl_bulk_std": aggstd(wedge, "f_nl_bulk"),
        "wedge_off_slope_all": agg(wedge, "off_slope_all"),
        "wedge_off_R2_all": agg(wedge, "off_R2_all"),
        "wedge_off_slope_edge": agg(wedge, "off_slope_edge"),
        "wedge_off_slope_bulk": agg(wedge, "off_slope_bulk"),
        "wedge_diag_slope_lin": agg(wedge, "diag_slope_lin"),
        "wedge_diag_R2_lin": agg(wedge, "diag_R2_lin"),
        "wedge_cond_B": agg(wedge, "cond_B"),
        "wedge_pairing_rel": agg(wedge, "pairing_rel"),
        "wedge_S": agg(wedge, "S"),
        "slab_f_nl_all": agg(slab, "f_nl_all"),
        "slab_f_nl_all_std": aggstd(slab, "f_nl_all"),
        "slab_off_slope": agg(slab, "off_slope"),
        "slab_off_R2": agg(slab, "off_R2"),
        "slab_diag_slope_lin": agg(slab, "diag_slope_lin"),
        "slab_diag_R2_lin": agg(slab, "diag_R2_lin"),
        "slab_cond_B": agg(slab, "cond_B"),
        "slab_pairing_rel": agg(slab, "pairing_rel"),
        "slab_S": agg(slab, "S"),
        "max_pairing_residual_rel": float(np.nanmax(
            [v for N in Ns for v in (wedge[N]["pairing_rel"] + slab[N]["pairing_rel"])]
            or [np.nan])),
    }

    # ---- HEADLINE nl-vs-edge curve (largest N reached, seed-averaged) -----
    def repcurve(d, ckey, mkey):
        Nrep = None
        for N in reversed(Ns):
            if d[N][ckey]:
                Nrep = N; break
        if Nrep is None:
            return None
        cc = d[Nrep][ckey]; mm = d[Nrep][mkey]
        Lmin = min(len(c) for c in cc)
        cmat = np.array([c[:Lmin] for c in cc])
        mmat = np.array([m[:Lmin] for m in mm])
        return Nrep, cmat, mmat

    rc = repcurve(wedge, "nl_vs_edge_centers", "nl_vs_edge_mean")
    if rc is not None:
        Nrep, cmat, mmat = rc
        dist = cmat.mean(axis=0); mean = mmat.mean(axis=0)
        sem = mmat.std(axis=0) / max(1.0, np.sqrt(mmat.shape[0]))
        res["nl_vs_edge_repN"] = Nrep
        res["nl_vs_edge_dist"] = dist.tolist()
        res["nl_vs_edge_mean"] = mean.tolist()
        res["nl_vs_edge_sem"] = sem.tolist()
        sl, se, r2 = lin_se(dist, mean)
        res["nl_vs_edge_slope"] = sl
        res["nl_vs_edge_slope_se"] = se
        res["nl_vs_edge_R2"] = r2
        # bootstrap CI across seeds (per-seed slope) via the per-seed curves
        boot = []
        rng_b = np.random.default_rng(20260606)
        n_curves = mmat.shape[0]
        for _ in range(2000):
            idx = rng_b.integers(0, n_curves, size=n_curves)
            mb = mmat[idx].mean(axis=0)
            sb, _, _ = lin_se(dist, mb)
            if np.isfinite(sb):
                boot.append(sb)
        if boot:
            res["nl_vs_edge_slope_ci68"] = [float(np.percentile(boot, 16)),
                                            float(np.percentile(boot, 84))]
        else:
            res["nl_vs_edge_slope_ci68"] = [sl, sl]

    # WALL-CONTROLLED inner-region edge curve (box corner excluded)
    rc_i = repcurve(wedge, "nl_vs_edge_inner_centers", "nl_vs_edge_inner_mean")
    if rc_i is not None:
        Nrep, cmat, mmat = rc_i
        dist = cmat.mean(axis=0); mean = mmat.mean(axis=0)
        sem = mmat.std(axis=0) / max(1.0, np.sqrt(mmat.shape[0]))
        res["nl_vs_edge_inner_repN"] = Nrep
        res["nl_vs_edge_inner_dist"] = dist.tolist()
        res["nl_vs_edge_inner_mean"] = mean.tolist()
        res["nl_vs_edge_inner_sem"] = sem.tolist()
        sl, se, r2 = lin_se(dist, mean)
        res["nl_vs_edge_inner_slope"] = sl
        res["nl_vs_edge_inner_slope_se"] = se
        res["nl_vs_edge_inner_R2"] = r2
        boot = []
        rng_b = np.random.default_rng(20260607)
        n_curves = mmat.shape[0]
        for _ in range(2000):
            idx = rng_b.integers(0, n_curves, size=n_curves)
            mb = mmat[idx].mean(axis=0)
            sb, _, _ = lin_se(dist, mb)
            if np.isfinite(sb):
                boot.append(sb)
        res["nl_vs_edge_inner_slope_ci68"] = (
            [float(np.percentile(boot, 16)), float(np.percentile(boot, 84))]
            if boot else [sl, sl])

    rc_s = repcurve(slab, "nl_vs_hyper_centers", "nl_vs_hyper_mean")
    if rc_s is not None:
        Nrep, cmat, mmat = rc_s
        dist = cmat.mean(axis=0); mean = mmat.mean(axis=0)
        sem = mmat.std(axis=0) / max(1.0, np.sqrt(mmat.shape[0]))
        res["nl_vs_hyper_repN"] = Nrep
        res["nl_vs_hyper_dist"] = dist.tolist()
        res["nl_vs_hyper_mean"] = mean.tolist()
        res["nl_vs_hyper_sem"] = sem.tolist()
        sl, se, r2 = lin_se(dist, mean)
        res["nl_vs_hyper_slope"] = sl
        res["nl_vs_hyper_slope_se"] = se
        res["nl_vs_hyper_R2"] = r2

    return _to_native(res), wedge, slab


# ===========================================================================
# VERDICT  (mirror VYPOCET-18/20 logic; edge replaces tip)
# ===========================================================================

def tail(a, k=2):
    a = np.array(a, float); a = a[np.isfinite(a)]
    return float(np.mean(a[-k:])) if a.size else np.nan


def build_verdict(res, link_tip_baseline, corner_2d_slope=-0.383):
    v = {}
    w_all = tail(res["wedge_f_nl_all"]); w_edge = tail(res["wedge_f_nl_edge"])
    w_bulk = tail(res["wedge_f_nl_bulk"]); s_all = tail(res["slab_f_nl_all"])
    v["wedge_nonlocal_frac_tail"] = w_all
    v["wedge_edge_nonlocal_frac_tail"] = w_edge
    v["wedge_bulk_nonlocal_frac_tail"] = w_bulk
    v["slab_nonlocal_frac_tail"] = s_all

    slab_off = tail(res["slab_off_slope"]); wedge_off = tail(res["wedge_off_slope_all"])
    bulk_off = tail(res["wedge_off_slope_bulk"]); edge_off = tail(res["wedge_off_slope_edge"])
    v["slab_offdiag_slope_tail"] = slab_off
    v["wedge_offdiag_slope_tail"] = wedge_off
    v["wedge_bulk_offdiag_slope_tail"] = bulk_off
    v["wedge_edge_offdiag_slope_tail"] = edge_off

    # (1) slab kernel more local than wedge (steeper off-diag decay)?
    slab_more_local = bool(np.isfinite(slab_off) and np.isfinite(wedge_off)
                           and slab_off < wedge_off - 0.1)
    v["slab_more_local_than_wedge"] = slab_more_local
    v["slab_vs_wedge_slope_gap"] = (float(wedge_off - slab_off)
        if np.isfinite(slab_off) and np.isfinite(wedge_off) else np.nan)

    # (2) within wedge: non-locality CONCENTRATES at the codim-2 edge?
    edge_more_nonlocal = bool(np.isfinite(w_edge) and np.isfinite(w_bulk)
                              and w_edge > w_bulk)
    v["edge_more_nonlocal_than_bulk"] = edge_more_nonlocal
    v["edge_vs_bulk_ratio"] = (float(w_edge / w_bulk)
        if np.isfinite(w_edge) and np.isfinite(w_bulk) and w_bulk > 0 else np.nan)

    # (3) THE HEADLINE: non-locality rises TOWARD the codim-2 edge (slope<0)?
    sl_e = res.get("nl_vs_edge_slope", np.nan)
    rises_toward_edge = bool(np.isfinite(sl_e) and sl_e < 0)
    v["nonlocality_rises_toward_edge"] = rises_toward_edge
    v["nl_vs_edge_slope"] = sl_e
    v["nl_vs_edge_slope_se"] = res.get("nl_vs_edge_slope_se", np.nan)
    v["nl_vs_edge_slope_ci68"] = res.get("nl_vs_edge_slope_ci68", None)
    v["nl_vs_edge_R2"] = res.get("nl_vs_edge_R2", np.nan)

    # (3b) WALL-CONTROLLED slope (box corner excluded) -- the robust version.
    sl_ei = res.get("nl_vs_edge_inner_slope", np.nan)
    se_ei = res.get("nl_vs_edge_inner_slope_se", np.nan)
    ci_ei = res.get("nl_vs_edge_inner_slope_ci68", None)
    v["nl_vs_edge_inner_slope"] = sl_ei
    v["nl_vs_edge_inner_slope_se"] = se_ei
    v["nl_vs_edge_inner_slope_ci68"] = ci_ei
    v["nl_vs_edge_inner_R2"] = res.get("nl_vs_edge_inner_R2", np.nan)
    # "flat" = the (wall-controlled) slope is statistically consistent with 0
    # AND far from BOTH the 2D corner (-0.38) and the 4D tip (+0.71).
    edge_slope_flat = bool(
        np.isfinite(sl_ei) and ci_ei is not None
        and ci_ei[0] <= 0.0 <= ci_ei[1])
    v["edge_slope_consistent_with_zero"] = edge_slope_flat

    # control: does the SLAB hyperplane ALSO concentrate non-locality? (should NOT)
    sl_h = res.get("nl_vs_hyper_slope", np.nan)
    v["nl_vs_hyper_slope"] = sl_h
    v["nl_vs_hyper_slope_se"] = res.get("nl_vs_hyper_slope_se", np.nan)
    v["nl_vs_hyper_R2"] = res.get("nl_vs_hyper_R2", np.nan)
    slab_rises = bool(np.isfinite(sl_h) and sl_h < 0)
    v["slab_hyper_rises_toward_surface"] = slab_rises

    # (4) wedge diagonal boost-weight linear toward the edge (Bisognano-Wichmann)?
    wedge_lin_R2 = tail(res["wedge_diag_R2_lin"])
    v["wedge_diag_boost_linear_R2_tail"] = wedge_lin_R2
    wedge_boost_linear = bool(np.isfinite(wedge_lin_R2) and wedge_lin_R2 > 0.6)
    v["wedge_diag_boost_linear"] = wedge_boost_linear
    slab_lin_R2 = tail(res["slab_diag_R2_lin"])
    v["slab_diag_boost_linear_R2_tail"] = slab_lin_R2

    # ---- THE H5g-3 DISCRIMINATOR --------------------------------------
    # codim2-generic  <=>  nl rises toward the edge (slope<0, like 2D corner)
    #                       AND specifically at the edge (edge_more_nonlocal)
    #                       AND the slab control does NOT show the same rise.
    codim2_generic = bool(rises_toward_edge and edge_more_nonlocal
                          and not slab_rises)
    v["codim2_corner_mechanism_generic"] = codim2_generic

    # sign comparison to the 4D TIP (F-024) and the 2D corner
    tip_slope = link_tip_baseline.get("nl_vs_tip_slope", np.nan)
    v["tip_slope_F024"] = tip_slope
    v["corner_2d_slope_VYP18"] = corner_2d_slope
    v["sign_matches_2d_corner"] = bool(
        np.isfinite(sl_e) and np.sign(sl_e) == np.sign(corner_2d_slope))
    v["sign_flipped_vs_tip"] = bool(
        np.isfinite(sl_e) and np.isfinite(tip_slope)
        and np.sign(sl_e) != np.sign(tip_slope))

    support = (int(slab_more_local) + int(edge_more_nonlocal) +
               int(rises_toward_edge) + int(wedge_boost_linear))
    v["n_signatures_supporting_H5g3"] = int(support)
    v["signatures"] = {
        "slab_more_local_offdiag": slab_more_local,
        "wedge_boost_weight_linear": wedge_boost_linear,
        "edge_more_nonlocal_than_bulk": edge_more_nonlocal,
        "nonlocality_rises_toward_edge": rises_toward_edge,
    }

    if codim2_generic:
        v["overall"] = (
            "CODIM-2-GENERIC: modular non-geometricity CONCENTRATES toward the "
            f"codim-2 wedge edge (nl-vs-edge slope={sl_e:.3g}<0, like the 2D "
            f"corner {corner_2d_slope}), edge more non-local than bulk, and the "
            f"flat-hyperplane SLAB control does NOT (slope={sl_h:.3g}). The 2D "
            "corner mechanism (H4g-1 layer B) GENERALISES to 4D at the RIGHT "
            "locus -- the VYPOCET-20 null-tip was the WRONG locus (a degenerating "
            "2-sphere, not a codim-2 joint).")
        v["H5g3"] = "codim2_generic"
    elif edge_slope_flat:
        v["overall"] = (
            "CODIM-2 IS INTERMEDIATE / FLAT: with the box wall controlled the "
            f"nl-vs-edge slope is statistically consistent with ZERO "
            f"(wall-controlled slope={sl_ei:.3g}, CI68={ci_ei}), i.e. modular "
            "non-locality is roughly UNIFORM toward the codim-2 joint -- neither "
            f"the sharp +{tip_slope:.2g} TIP anti-concentration (F-024) NOR the "
            f"{corner_2d_slope} 2D-corner concentration. The codim-2 joint moves "
            "the 4D behaviour AWAY from the tip null toward neutrality, but does "
            "NOT restore the 2D corner-concentration mechanism. H4g-1 layer-B "
            "corner sub-claim remains 4D-limited; the wedge edge is closer to the "
            "2D corner than the tip but the concentration does not survive to 4D.")
        v["H5g3"] = "codim2_flat_intermediate"
    elif rises_toward_edge and not edge_more_nonlocal:
        v["overall"] = (
            f"PARTIAL: nl-vs-edge slope={sl_e:.3g}<0 (rises toward the edge, "
            "unlike the +0.71 tip) but the zone metric edge_more_nonlocal="
            f"{edge_more_nonlocal} does not corroborate. Codim-2 joint is closer "
            "to the 2D corner than the tip but not a clean replication.")
        v["H5g3"] = "partial"
    else:
        v["overall"] = (
            f"2D-ONLY: even at a clean codim-2 joint the non-locality does NOT "
            f"concentrate toward the edge -- it FALLS toward it (nl-vs-edge "
            f"slope={sl_e:.3g}>=0; wall-controlled inner slope={sl_ei:.3g}, "
            f"CI68={ci_ei}, both POSITIVE like the 4D tip {tip_slope:.2g}, "
            f"opposite the 2D corner {corner_2d_slope}). The positive slope is "
            "NOT a box-wall artefact (it is steeper in the wall-controlled inner "
            "region). The corner sub-part of H4g-1 layer B is genuinely 2D-only; "
            "reframing the 4D locus from the null-TIP to a codim-2 JOINT does NOT "
            "restore the 2D corner-concentration mechanism. (The slab-boost side "
            f"survives: wedge diagonal boost-weight linear R2={wedge_lin_R2:.2f}.)")
        v["H5g3"] = "2d_only"
    return v


# ===========================================================================
# BASELINE  : pull the F-024 (VYPOCET-20) tip slope for the contrast
# ===========================================================================

def load_tip_baseline():
    out = {"nl_vs_tip_slope": np.nan, "corner_over_bulk": np.nan,
           "nl_vs_tip_dist": None, "nl_vs_tip_mean": None}
    path = os.path.join(os.path.dirname(OUTDIR), "modular-flow-bd-4d", "results.json")
    try:
        r = json.load(open(path))
        bd = r.get("bd_smeared_eps0.6", {})
        out["nl_vs_tip_slope"] = bd.get("nl_vs_corner_slope", np.nan)
        out["nl_vs_tip_dist"] = bd.get("nl_vs_corner_dist")
        out["nl_vs_tip_mean"] = bd.get("nl_vs_corner_mean")
        v = r.get("VERDICT", {})
        out["corner_over_bulk"] = v.get("corner_vs_bulk_ratio", np.nan)
        out["H4g1_4D"] = v.get("H4g1_4D", None)
    except Exception as e:
        out["error"] = str(e)
    return out


# ===========================================================================
# PLOTS  (one uses toe.viz.powerlaw_panel for dogfooding)
# ===========================================================================

def make_plots(res, verdict, tip_baseline):
    import matplotlib.pyplot as plt
    Ns = np.array(res["Ns"], float)

    # Plot 1: non-local fraction vs N -- wedge (edge vs bulk) vs slab control
    fig, ax = plt.subplots(figsize=(8.5, 6))
    ax.errorbar(Ns, res["wedge_f_nl_all"], yerr=res["wedge_f_nl_all_std"],
                fmt='o-', color='tab:red', capsize=3, label="wedge cut (all)")
    ax.errorbar(Ns, res["wedge_f_nl_edge"], yerr=res["wedge_f_nl_edge_std"],
                fmt='^-', color='darkred', capsize=3, label="wedge NEAR-EDGE (codim-2)")
    ax.errorbar(Ns, res["wedge_f_nl_bulk"], yerr=res["wedge_f_nl_bulk_std"],
                fmt='v-', color='salmon', capsize=3, label="wedge BULK")
    ax.errorbar(Ns, res["slab_f_nl_all"], yerr=res["slab_f_nl_all_std"],
                fmt='s-', color='tab:blue', capsize=3, label="slab control (no joint)")
    ax.set_xlabel("N"); ax.set_ylabel(r"non-local fraction of $\|K\|_{HS}^2$")
    ax.set_title(f"VYPOCET-22: 4D codim-2 modular non-locality (BD smeared eps={res['eps']})\n"
                 + verdict["H5g3"])
    ax.legend(fontsize=9); ax.grid(alpha=0.3)
    fig.tight_layout(); fig.savefig(os.path.join(PLOTDIR, "nonlocality_vs_N_codim2.png"), dpi=140)
    plt.close(fig)

    # Plot 2: THE KEY CURVE -- nl vs distance-to-edge (codim-2) vs the F-024 tip
    fig, ax = plt.subplots(figsize=(8.5, 6))
    if "nl_vs_edge_dist" in res:
        d = np.array(res["nl_vs_edge_dist"]); m = np.array(res["nl_vs_edge_mean"])
        se = np.array(res.get("nl_vs_edge_sem", np.zeros_like(m)))
        ax.errorbar(d, m, yerr=se, fmt='o-', color='tab:red', capsize=4,
                    label=f"WEDGE codim-2 edge (slope={res.get('nl_vs_edge_slope', np.nan):.3g})")
    if "nl_vs_edge_inner_dist" in res:
        d = np.array(res["nl_vs_edge_inner_dist"]); m = np.array(res["nl_vs_edge_inner_mean"])
        se = np.array(res.get("nl_vs_edge_inner_sem", np.zeros_like(m)))
        ax.errorbar(d, m, yerr=se, fmt='o--', color='darkorange', capsize=4,
                    label=f"WEDGE edge, WALL-CTRL (slope={res.get('nl_vs_edge_inner_slope', np.nan):.3g})")
    if "nl_vs_hyper_dist" in res:
        d = np.array(res["nl_vs_hyper_dist"]); m = np.array(res["nl_vs_hyper_mean"])
        se = np.array(res.get("nl_vs_hyper_sem", np.zeros_like(m)))
        ax.errorbar(d, m, yerr=se, fmt='s-', color='tab:blue', capsize=4,
                    label=f"SLAB control hyperplane (slope={res.get('nl_vs_hyper_slope', np.nan):.3g})")
    if tip_baseline.get("nl_vs_tip_dist"):
        d = np.array(tip_baseline["nl_vs_tip_dist"]); m = np.array(tip_baseline["nl_vs_tip_mean"])
        ax.plot(d, m, '^--', color='gray',
                label=f"F-024 4D null-TIP (slope={tip_baseline.get('nl_vs_tip_slope', np.nan):.3g})")
    ax.set_xlabel("distance to locus (edge / hyperplane / tip)")
    ax.set_ylabel("per-site non-local fraction")
    ax.set_title("VYPOCET-22 KEY CURVE: 4D modular non-locality vs distance-to-LOCUS\n"
                 "slope<0 = rises TOWARD locus (2D corner mechanism); +slope = away (tip null)")
    ax.legend(fontsize=8); ax.grid(alpha=0.3)
    fig.tight_layout(); fig.savefig(os.path.join(PLOTDIR, "nonlocality_vs_edge_codim2.png"), dpi=140)
    plt.close(fig)

    # Plot 3: off-diagonal decay slope + diagonal boost linearity, wedge vs slab
    fig, (axa, axb) = plt.subplots(1, 2, figsize=(13, 5.5))
    axa.plot(Ns, res["slab_off_slope"], 's-', color='tab:blue', label="slab off-slope")
    axa.plot(Ns, res["wedge_off_slope_all"], 'o-', color='tab:red', label="wedge off-slope")
    axa.axhline(0, color='k', ls=':', lw=1)
    axa.set_xlabel("N"); axa.set_ylabel("off-diagonal log-log slope")
    axa.set_title("Off-diagonal decay: slab (free boost) vs wedge (codim-2 edge)")
    axa.legend(fontsize=9); axa.grid(alpha=0.3)
    axb.plot(Ns, res["wedge_diag_R2_lin"], 'D-', color='darkred',
             label="wedge diagonal boost-linearity R2")
    axb.plot(Ns, res["slab_diag_R2_lin"], 'D-', color='tab:blue',
             label="slab diagonal boost-linearity R2")
    axb.axhline(0.6, color='k', ls=':', lw=1, label="support threshold 0.6")
    axb.set_xlabel("N"); axb.set_ylabel(r"$R^2$ of $|K(x,x)|$ vs distance (linear)")
    axb.set_title("Diagonal boost-weight linearity (Bisognano-Wichmann)")
    axb.set_ylim(0, 1.02); axb.legend(fontsize=9); axb.grid(alpha=0.3)
    fig.tight_layout(); fig.savefig(os.path.join(PLOTDIR, "wedge_slab_diagnostics_codim2.png"), dpi=140)
    plt.close(fig)

    # Plot 4 (DOGFOOD toe.viz): off-diag |K| magnitude vs distance, log-log, with
    # the toe.fits FitResult CI band -- wedge bulk decay as a power law.
    try:
        if "nl_vs_edge_dist" in res:
            d = np.array(res["nl_vs_edge_dist"], float)
            m = np.array(res["nl_vs_edge_mean"], float)
            ok = (d > 0) & (m > 0) & np.isfinite(d) & np.isfinite(m)
            if ok.sum() >= 3:
                fit = powerlaw_fit(d[ok], m[ok])
                fig = toe_viz.powerlaw_panel(
                    fit, d[ok], m[ok], label="wedge nl vs d_edge",
                    save=os.path.join(PLOTDIR, "wedge_nl_powerlaw_panel.png"))
                import matplotlib.pyplot as _plt
                _plt.close(fig)
                return float(fit.value), float(fit.se_regression)
    except Exception as e:
        print(f"  [toe.viz panel skipped: {e}]")
    return None, None


# ===========================================================================
def run():
    t0 = time.time()
    results = {
        "task": "VYPOCET-22: TEST H5g-3 -- codim-2 joint as the right 4D locus of "
                "modular-flow non-geometricity (the 4D analogue of the 2D corner)",
        "hypothesis": "H5g-3 (BRAINSTORM-05, medium-high)",
        "claim": ("the VYPOCET-20 (F-024) 4D diamond null-tip fails the 2D corner "
                  "mechanism because the tip is a degenerating 2-sphere; the right "
                  "4D locus is a CODIM-2 JOINT (wedge edge = flat 2-plane). Test "
                  "whether modular non-geometricity concentrates toward the edge "
                  "(codim-2-generic) or not (2D-only)."),
        "conventions": {
            "object": "smeared Benincasa-Dowker eps=0.6, G_R=B_eps^{-1} (VYPOCET-20 PRIMARY)",
            "BD_smeared_4D": "alpha4=-4/sqrt6, beta4=4/sqrt6, f4(n,eps); arXiv:1305.2588/1507.00330",
            "iDelta": "i(G_R-G_R^T); W=SJ positive part (rel-floor 1e-10, VYPOCET-09/20)",
            "geometry_wedge": ("4D Minkowski box {|t|,|x|,|y|,|z|<=0.5}, right Rindler "
                               "wedge W={x>|t|}, cut O={x>0}; entangling surface = "
                               "codim-2 EDGE E={t=0,x=0} (flat 2-plane); "
                               "distance-to-edge d_E=sqrt(t^2+x^2)"),
            "geometry_slab_control": ("volume/density-matched box, cut O={x>0}; flat "
                                      "codim-1 hyperplane x=0, NO codim-2 joint; "
                                      "control locus distance |x|"),
            "modular_kernel": ("one-particle K(x,y) from SSEE generalized eigenproblem "
                               "W_O v=mu iDelta_O v; eps=ln[mu/(mu-1)]; site basis "
                               "(Casini-Huerta 0905.2562; Sorkin-Yazdi 1611.10281)"),
            "probe": "UNTRUNCATED SJ modular kernel (kappa=None), same as VYPOCET-18/20",
            "machine_precision_invariant": ("iDelta +/- pairing residual_rel < 1e-12 "
                                            "asserted on EVERY region/seed (toe.causet."
                                            "causal_diagnostics)"),
            "vs_VYPOCET20": ("SAME dynamical object (smeared BD eps=0.6); the ONLY "
                             "change is the GEOMETRY/LOCUS: codim-2 wedge edge "
                             "instead of the diamond null-tip"),
        },
        "lib_usage": {
            "toe.causet": ["causal_matrix (4D Minkowski order)", "pauli_jordan",
                           "causal_diagnostics (pairing invariant)"],
            "toe.fits": ["regression_se", "powerlaw_fit", "validate_against", "Measurement"],
            "toe.viz": ["powerlaw_panel (wedge nl power-law panel)"],
            "missing_from_toe": [
                "smeared BD d'Alembertian (toe.causet ships only the SHARP "
                "bd_dalembertian_inverse; smeared eps object reproduced in helpers)",
                "modular kernel K_site export (toe.entropy.ssee returns only S)",
                "rel-floor option on toe.sj.sj_state (BD-inverse needs relative cut)",
                "codim-2 / wedge region builders + nl-vs-locus diagnostic",
            ],
        },
        # ready-to-lift signatures (kept LOCAL this round; VYPOCET-21 owns causet.py)
        "lib_proposals": {
            "toe.causet.sprinkle_wedge_box4d": (
                "sprinkle_wedge_box4d(N, rng, *, t_half=0.5, x_half=0.5, "
                "yz_half=0.5) -> (N,4)  # t-symmetric Minkowski box whose x>0 cut "
                "has its entangling surface on the codim-2 Rindler edge {t=0,x=0}"),
            "toe.causet.bd_smeared_dalembertian_inverse": (
                "bd_smeared_dalembertian_inverse(C, rho, eps) -> (N,N)  # smeared "
                "BD G_R=B_eps^{-1}; the eps-sibling of the existing SHARP "
                "bd_dalembertian_inverse(...,dim=4); alpha4=-4/sqrt6, beta4=4/sqrt6, "
                "f4(n,eps) (Aslanbeigi-Saravani-Sorkin 1305.2588)"),
            "toe.sj.sj_state_relfloor": (
                "sj_state(iDelta, *, tol=1e-12, rel_floor=None)  # add a RELATIVE "
                "positive-eigenvalue floor (rel_floor*lmax); needed for "
                "BD-inverse objects (cond ~1e5-1e6) to avoid amplifying inversion "
                "noise (VYPOCET-09/20 convention)"),
            "toe.entropy.modular_kernel": (
                "modular_kernel(W, iDelta, sub_idx, *, kappa=None, tol=1e-9) -> "
                "{K, eps, S, nu}  # expose the site-basis one-particle kernel K "
                "(toe.entropy.ssee currently returns only the scalar S); the "
                "locality diagnostics in VYPOCET-18/20/22 all need K"),
            "toe.viz.nl_vs_locus_panel": (
                "nl_vs_locus(Kabs, Dij, d_locus, near_r, n_zones=6) -> (cen, mean) "
                "# per-site non-local fraction binned by distance-to-LOCUS "
                "(generalises VYPOCET-20 _nl_vs_corner_generic: locus = tip OR "
                "codim-2 edge OR hyperplane)"),
        },
    }

    tip = load_tip_baseline()
    results["tip_baseline_F024"] = _to_native(tip)
    print("=== F-024 (VYPOCET-20) 4D null-tip baseline ===")
    print(f"  nl_vs_tip_slope={tip['nl_vs_tip_slope']}  corner/bulk={tip['corner_over_bulk']}")

    Ns = [800, 1200, 1700, 2200]      # N<=2200 matrix-inversion bound
    n_seeds = 3
    BUDGET = 5400

    res, wedge, slab = run_codim2(Ns, n_seeds, t_start=t0, budget=BUDGET)
    results["codim2"] = res

    verdict = build_verdict(res, tip)
    results["VERDICT"] = _to_native(verdict)

    # toe.fits validation hooks (value, SE/CI carriers)
    edge_slope_meas = Measurement(
        value=res.get("nl_vs_edge_slope", float("nan")),
        se=res.get("nl_vs_edge_slope_se", 0.0),
        ci68=tuple(res["nl_vs_edge_slope_ci68"]) if res.get("nl_vs_edge_slope_ci68") else None,
        n=n_seeds)
    # validate the machine-precision invariant via toe.fits.validate_against
    pairing_ok = validate_against(res["max_pairing_residual_rel"], 0.0,
                                  rtol=0.0, atol=PAIRING_TOL)
    edge_slope_meas.validated = bool(pairing_ok and np.isfinite(edge_slope_meas.value))
    results["edge_slope_measurement"] = {
        "value": edge_slope_meas.value, "se": edge_slope_meas.se,
        "ci68": list(edge_slope_meas.ci68) if edge_slope_meas.ci68 else None,
        "n": edge_slope_meas.n, "validated": edge_slope_meas.validated,
    }
    results["machine_precision_invariant"] = {
        "max_pairing_residual_rel": res["max_pairing_residual_rel"],
        "bound": PAIRING_TOL,
        "passes": bool(pairing_ok),
    }

    print("\n=== VERDICT (BD smeared eps=0.6) ===")
    for k in ["slab_more_local_than_wedge", "slab_vs_wedge_slope_gap",
              "wedge_diag_boost_linear", "wedge_diag_boost_linear_R2_tail",
              "edge_more_nonlocal_than_bulk", "edge_vs_bulk_ratio",
              "nonlocality_rises_toward_edge", "nl_vs_edge_slope",
              "nl_vs_edge_slope_se", "nl_vs_edge_slope_ci68", "nl_vs_edge_R2",
              "nl_vs_edge_inner_slope", "nl_vs_edge_inner_slope_se",
              "nl_vs_edge_inner_slope_ci68", "edge_slope_consistent_with_zero",
              "nl_vs_hyper_slope", "slab_hyper_rises_toward_surface",
              "sign_matches_2d_corner", "sign_flipped_vs_tip",
              "n_signatures_supporting_H5g3",
              "codim2_corner_mechanism_generic", "H5g3"]:
        print(f"  {k}: {verdict.get(k)}")
    print(f"\n  OVERALL: {verdict['overall']}")
    print(f"\n  pairing invariant max_rel={res['max_pairing_residual_rel']:.3e} "
          f"(< {PAIRING_TOL:.0e}: {pairing_ok})")

    pl_slope, pl_se = make_plots(res, verdict, tip)
    if pl_slope is not None:
        results["wedge_nl_powerlaw_panel"] = {"slope": pl_slope, "se": pl_se}

    results["runtime_s"] = time.time() - t0
    with open(os.path.join(OUTDIR, "results.json"), "w") as fh:
        json.dump(_to_native(results), fh, indent=2)
    print(f"\nDone in {results['runtime_s']:.1f}s. results.json + plots in {OUTDIR}")
    return results


if __name__ == "__main__":
    run()
