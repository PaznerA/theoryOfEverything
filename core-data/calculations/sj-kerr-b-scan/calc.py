#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
VYPOCET-26  --  KERR B-EXPONENT SCAN  (closes H5g-5)
            Is B in  W_sr ~ Omega(r)^B  a CONTINUOUS function of frame
            dragging / asymptotics, or the dimensional constant D-1 ?
==========================================================================

CONTEXT (do NOT redo this -- it is done):
  * VYPOCET-14 (sj-threshold-scan) + VYPOCET-15 (sj-far-zone) established that
    the superradiant-wedge weight follows Model S, W_sr = A * Omega(r)^B, over
    Model E (Lorentzian at r_erg): joint near+far DeltaAIC = +3894 (a=0.6),
    +4216 (a=0.9), +231 (BTZ J=0.9).  THAT decision is closed.
  * BUT the committed Model-S exponents B = 4.23 (a=0.6) / 3.82 (a=0.9) came
    from a BOUNDED scipy fit that HIT the upper amplitude bound A=100, so the
    absolute B values are only ORIENTATIONAL (see F-017 caveat).

THE OPEN PROBLEM (this is NEW):
  (1) RELIABLE B -- re-extract B for each configuration from an UNBOUNDED
      log-log regression  log W_sr = log A + B * log Omega  (B = slope; A
      unconstrained), on the near-zone points with W_sr>0.  Report B with a
      proper regression SE and a bootstrap CI across the 5 seeds.  Compare to
      the old bounded B and quantify how much the A=100 bound distorted it.

  (2) DENSE SPIN SCAN B(a) -- the decisive test.  Measure B at a grid of Kerr
      spins a (equatorial, N=1600, 5 seeds).  For each a: radial near-zone scan
      just outside r_erg=2M where W_sr>0; log-log B fit (SE + bootstrap CI).
      DISCRIMINATOR:
        * if B == D-1 = 3 (dimensional constant): B is CONSTANT in a;
        * if B varies smoothly with a: B is a CONTINUOUS function of frame
          dragging.
      Fit the B(a) trend (weighted linear regression) and report its slope +
      significance.

  (3) ASYMPTOTICS CONTRAST -- add BTZ J in {0.6, 0.9} (3D, Omega ~ 1/r^2 vs
      Kerr Omega ~ 1/r^3 asymptotics).  Does B(BTZ) sit on the same B(a) curve
      or off it?  This is dimension-vs-asymptotics evidence WITHOUT needing
      Kerr-AdS well-definedness.

CONVENTIONS: IDENTICAL to VYPOCET-14 / VYPOCET-15 / VYPOCET-10 / VYPOCET-08.
  * 2D massless scalar => G_R = (1/2) C (conformally invariant) [1611.10281 eq.9]
  * iDelta = i*(1/2)(C - C^T); SJ W = positive part of iDelta
  * Kerr equatorial h=[[-(1-2M/r),-2Ma/r],[-2Ma/r,r^2+a^2+2Ma^2/r]], r_erg=2M
  * BTZ h=[[M-r^2,-J/2],[-J/2,r^2]], r_erg=sqrt(M)
  * Omega = -g_tphi/g_phiphi (ZAMO angular velocity)
  * Superradiant wedge: w*(w-k*Omega) < 0; W_sr = weight in that wedge
  * N=1600, 5 seeds [101,202,303,404,505], T=Phi=1.4, NW=71, KMAX=35

SCHEMA / HYGIENE:
  * paths are __file__-relative (no machine-absolute paths)
  * results.json: fixed schema with a top-level "status" field; ATOMIC write
    (tmp + os.replace), so an interrupted run leaves a clean valid partial.
  * status transitions: "running" -> per-stage updates -> "complete"; each
    stage flushed to disk so a session-limit interrupt is recoverable.
"""

import json
import os
import time

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

OUTDIR = os.path.dirname(os.path.abspath(__file__))
PLOTDIR = os.path.join(OUTDIR, "plots")
os.makedirs(PLOTDIR, exist_ok=True)
RESULTS_PATH = os.path.join(OUTDIR, "results.json")
np.set_printoptions(precision=6, suppress=True)

# Old BOUNDED Model-S exponents committed by VYPOCET-14 (A hit bound 100),
# kept ONLY for the contrast plot/table -- they are orientational, not reliable.
OLD_BOUNDED_B = {"kerr_a0.6": 4.23, "kerr_a0.9": 3.82, "btz_J0.9": 1.71}

# ==========================================================================
# GEOMETRY  (identical to VYPOCET-14/15)
# ==========================================================================

def kerr_section(M, a, r):
    """Equatorial Kerr fixed-r (t,phi) 2-metric h."""
    g_tt = -(1.0 - 2.0 * M / r)
    g_tp = -2.0 * M * a / r
    g_pp = r**2 + a**2 + 2.0 * M * a**2 / r
    return np.array([[g_tt, g_tp], [g_tp, g_pp]], dtype=float)


def kerr_surfaces(M, a):
    """(r_+, r_-, r_erg) for Kerr."""
    rp = M + np.sqrt(M**2 - a**2)
    rm = M - np.sqrt(M**2 - a**2)
    return rp, rm, 2.0 * M


def omega_kerr_analytic(M, a, r):
    """Kerr ZAMO Omega(r) = 2Ma/(r^3 + a^2 r + 2Ma^2) ~ 2Ma/r^3 (large r)."""
    return 2.0 * M * a / (r**3 + a**2 * r + 2.0 * M * a**2)


def btz_section(M, J, r):
    """Rotating BTZ fixed-r (t,phi) 2-metric h."""
    return np.array([[M - r**2, -J / 2.0], [-J / 2.0, r**2]], dtype=float)


def btz_surfaces(M, J):
    """(r_+, r_-, r_erg) for BTZ."""
    disc = M**2 - J**2
    rp = np.sqrt(0.5 * (M + np.sqrt(disc)))
    rm = np.sqrt(0.5 * (M - np.sqrt(disc)))
    return rp, rm, np.sqrt(M)


def omega_btz_analytic(M, J, r):
    """BTZ ZAMO Omega(r) = (J/2)/r^2 ~ r^{-2} (large r) -- shallower falloff
    than Kerr's r^{-3}; this is the asymptotics contrast knob."""
    return (J / 2.0) / r**2


def drag_slope(h):
    """Omega = -g_tphi/g_phiphi (ZAMO angular velocity)."""
    return -h[0, 1] / h[1, 1]


def is_lorentzian(h):
    return float(np.linalg.det(h)) < 0


# ==========================================================================
# SJ PIPELINE  (identical to VYPOCET-14/15)
# ==========================================================================

def sprinkle(N, T_extent, Phi_extent, rng):
    return np.column_stack([rng.uniform(0, T_extent, N),
                            rng.uniform(0, Phi_extent, N)])


def causal_matrix(coords, h):
    """C[x,y]=1 iff y precedes x (tilted cones)."""
    s_drag = drag_slope(h)
    T = np.array([1.0, s_drag])
    X = coords[:, None, :]; Y = coords[None, :, :]
    D = X - Y
    DhD = np.sum((D @ h) * D, axis=2)
    ThD = D @ (h @ T)
    eps = 1e-12
    prec = (DhD <= eps) & (ThD < -eps)
    C = prec.astype(np.float64)
    np.fill_diagonal(C, 0.0)
    return C


def sj_positive(C):
    """(lambda_pos, V_pos) of iDelta = i*(1/2)(C-C^T)."""
    iDelta = 1j * 0.5 * (C - C.T)
    wv, V = np.linalg.eigh(iDelta)
    pos = wv > 1e-9
    return wv[pos], V[:, pos]


def occupation_map(coords, lam, Vp, ws, ks):
    """P(w,k) = sum_modes lambda * |<plane(w,k)|v>|^2, normalized to sum 1."""
    t = coords[:, 0]; ph = coords[:, 1]; N_pts = coords.shape[0]
    phase_t = np.exp(1j * np.outer(ws, t))
    phase_k = np.exp(-1j * np.outer(ks, ph))
    P = np.zeros((len(ws), len(ks)))
    for iw in range(len(ws)):
        phasewk = phase_k * phase_t[iw][np.newaxis, :]
        proj_wk = (phasewk @ Vp) / N_pts
        P[iw, :] = (np.abs(proj_wk) ** 2) @ lam
    tot = P.sum()
    return P / tot if tot > 0 else P


def superradiant_wedge_weight(P, ws, ks, Omega):
    """W_sr = weight of P in the wedge w*(w - k*Omega) < 0."""
    WW, KK = np.meshgrid(ws, ks, indexing="ij")
    sr_mask = WW * (WW - KK * Omega) < 0
    return float(P[sr_mask].sum())


def compute_Wsr_one(section_fn, par, r, seed, N, T, Phi, ws, ks):
    """Single (geometry, r, seed) -> (Omega, W_sr)."""
    rng = np.random.default_rng(seed)
    coords = sprinkle(N, T, Phi, rng)
    h = section_fn(*par, r)
    Omega = drag_slope(h)
    C = causal_matrix(coords, h)
    lam, Vp = sj_positive(C)
    P = occupation_map(coords, lam, Vp, ws, ks)
    W_sr = superradiant_wedge_weight(P, ws, ks, Omega)
    return float(Omega), float(W_sr)


# ==========================================================================
# UNBOUNDED LOG-LOG B FIT  (fixes the A=100 bound artefact)
# ==========================================================================

def loglog_B_fit(Omega_arr, Wsr_arr, Wsr_sd_arr):
    """Unbounded OLS/WLS of  log W_sr = log A + B log Omega.

    Returns the slope B (= the exponent in W_sr ~ Omega^B) and its regression
    standard error, with NO bound on the amplitude A -- this is exactly what the
    bounded scipy fit of VYPOCET-14 could not deliver (it hit A=100).  Weights
    are the propagated relative errors sd(W)/W (floored at 1%).  R^2 is in
    log-log space.

    Only points with Omega>0 AND W_sr>0 enter (a power law is only defined
    there).  Needs >=3 such points.
    """
    Omega_arr = np.asarray(Omega_arr, float)
    Wsr_arr = np.asarray(Wsr_arr, float)
    Wsr_sd_arr = np.asarray(Wsr_sd_arr, float)
    mask = (Omega_arr > 0) & (Wsr_arr > 0)
    n = int(mask.sum())
    if n < 3:
        return {"ok": False, "n": n, "reason": "fewer than 3 positive points"}
    lx = np.log(Omega_arr[mask])
    ly = np.log(Wsr_arr[mask])
    # relative error of log W = sd(W)/W
    rel = np.where(Wsr_arr[mask] > 0, Wsr_sd_arr[mask] / Wsr_arr[mask], 1.0)
    sig_ly = np.maximum(rel, 0.01)
    Wt = 1.0 / sig_ly**2

    X = np.column_stack([np.ones_like(lx), lx])
    XtWX = X.T @ (Wt[:, None] * X)
    XtWy = X.T @ (Wt * ly)
    try:
        params = np.linalg.solve(XtWX, XtWy)
        cov = np.linalg.inv(XtWX)
    except np.linalg.LinAlgError:
        return {"ok": False, "n": n, "reason": "singular normal equations"}
    log_A, B = params
    B_se = float(np.sqrt(cov[1, 1]))
    A_val = float(np.exp(log_A))

    ly_pred = log_A + B * lx
    ss_res = float(np.sum((ly - ly_pred) ** 2))
    ss_tot = float(np.sum((ly - np.mean(ly)) ** 2))
    R2 = 1.0 - ss_res / ss_tot if ss_tot > 0 else float("nan")
    # unweighted log-log Pearson corr (the VYPOCET-15 corr_loglog(S) analogue)
    corr = float(np.corrcoef(lx, ly)[0, 1]) if n >= 2 else float("nan")
    # chi2/dof of the weighted fit
    resid_w = (ly - ly_pred) / sig_ly
    chi2 = float(np.sum(resid_w**2))
    return {
        "ok": True, "n": n, "B": float(B), "B_se": B_se, "A": A_val,
        "R2_loglog": float(R2), "corr_loglog": corr,
        "chi2": chi2, "chi2_dof": chi2 / max(n - 2, 1),
    }


def bootstrap_B(Omega_arr, Wsr_per_seed, seeds, n_boot=2000, rng_seed=20260608):
    """Bootstrap CI for B by resampling SEEDS (not radii).

    Wsr_per_seed: (n_radii, n_seeds) array of W_sr.  For each bootstrap replicate
    we resample the seed columns with replacement, average to get a per-radius
    W_sr, and refit the log-log slope.  Returns the bootstrap mean, SE and the
    2.5/97.5 percentile CI of B.  This captures the (dominant) Monte-Carlo
    sprinkle uncertainty across seeds, which the single-fit regression SE alone
    does not.
    """
    Omega_arr = np.asarray(Omega_arr, float)
    Wsr_per_seed = np.asarray(Wsr_per_seed, float)  # (n_radii, n_seeds)
    n_seeds = Wsr_per_seed.shape[1]
    rng = np.random.default_rng(rng_seed)
    Bs = []
    for _ in range(n_boot):
        cols = rng.integers(0, n_seeds, size=n_seeds)
        Wmean = Wsr_per_seed[:, cols].mean(axis=1)
        Wsd = Wsr_per_seed[:, cols].std(axis=1, ddof=1) if n_seeds > 1 else np.zeros_like(Wmean)
        fit = loglog_B_fit(Omega_arr, Wmean, Wsd)
        if fit["ok"]:
            Bs.append(fit["B"])
    Bs = np.asarray(Bs)
    if Bs.size < 10:
        return {"ok": False, "n_boot_ok": int(Bs.size)}
    return {
        "ok": True, "n_boot": int(Bs.size),
        "B_boot_mean": float(np.mean(Bs)),
        "B_boot_se": float(np.std(Bs, ddof=1)),
        "B_ci95": [float(np.percentile(Bs, 2.5)),
                   float(np.percentile(Bs, 97.5))],
    }


# ==========================================================================
# PER-CONFIGURATION NEAR-ZONE SCAN + B EXTRACTION
# ==========================================================================

def scan_config(section_fn, par, omega_fn, omega_par, radii, r_erg, rp,
                seeds, N, T, Phi, ws, ks, label):
    """Near-zone radial scan for one configuration; returns per-radius records
    (Omega, W_sr per seed) restricted to Lorentzian radii strictly outside
    r_erg with at least one nonzero W_sr seed."""
    records = []
    for r in radii:
        h = section_fn(*par, r)
        if not is_lorentzian(h):
            continue
        if r <= r_erg + 1e-9 or r <= rp:
            continue
        per_seed = [compute_Wsr_one(section_fn, par, r, s, N, T, Phi, ws, ks)
                    for s in seeds]
        Omega = float(np.mean([d[0] for d in per_seed]))
        Wsr_vals = [d[1] for d in per_seed]
        rec = {
            "r": float(r),
            "Omega": Omega,
            "Omega_analytic": float(omega_fn(*omega_par, r)),
            "W_sr_mean": float(np.mean(Wsr_vals)),
            "W_sr_sd": float(np.std(Wsr_vals, ddof=1)) if len(Wsr_vals) > 1 else 0.0,
            "W_sr_per_seed": [float(v) for v in Wsr_vals],
            "n_seeds": len(seeds),
        }
        records.append(rec)
        print(f"  {label} r={r:.3f}: Omega={Omega:.5f} "
              f"W_sr={rec['W_sr_mean']:.5f}+/-{rec['W_sr_sd']:.5f}")
    return records


def extract_B(records, n_boot=2000):
    """Reliable B from a configuration's near-zone records (only W_sr>0 points)."""
    pos = [rec for rec in records if rec["W_sr_mean"] > 0]
    Omega = np.array([rec["Omega"] for rec in pos])
    Wmean = np.array([rec["W_sr_mean"] for rec in pos])
    Wsd = np.array([rec["W_sr_sd"] for rec in pos])
    fit = loglog_B_fit(Omega, Wmean, Wsd)
    out = {"fit": fit, "n_points_used": len(pos),
           "radii_used": [rec["r"] for rec in pos]}
    if fit["ok"]:
        Wps = np.array([rec["W_sr_per_seed"] for rec in pos])  # (n_radii, n_seeds)
        out["bootstrap"] = bootstrap_B(Omega, Wps, None, n_boot=n_boot)
    return out


# ==========================================================================
# B(a) TREND FIT
# ==========================================================================

def fit_Ba_trend(a_arr, B_arr, B_se_arr):
    """Weighted linear regression B(a) = B0 + slope * a.

    Reports slope, its SE, the z-significance of slope != 0, and -- the
    discriminator for H5g-5 -- the chi2 and per-point deviation of the data from
    the CONSTANT model B = D-1 = 3 (dimensional-constant hypothesis)."""
    a_arr = np.asarray(a_arr, float)
    B_arr = np.asarray(B_arr, float)
    B_se_arr = np.maximum(np.asarray(B_se_arr, float), 1e-6)
    n = len(a_arr)
    Wt = 1.0 / B_se_arr**2
    X = np.column_stack([np.ones_like(a_arr), a_arr])
    XtWX = X.T @ (Wt[:, None] * X)
    XtWy = X.T @ (Wt * B_arr)
    params = np.linalg.solve(XtWX, XtWy)
    cov = np.linalg.inv(XtWX)
    B0, slope = params
    B0_se = float(np.sqrt(cov[0, 0]))
    slope_se = float(np.sqrt(cov[1, 1]))
    slope_z = float(slope / slope_se) if slope_se > 0 else float("nan")

    # chi2 of the linear (sloped) model
    pred_lin = B0 + slope * a_arr
    chi2_lin = float(np.sum(((B_arr - pred_lin) / B_se_arr) ** 2))

    # chi2 of the constant-=3 (D-1) model, and best-fit constant
    chi2_const3 = float(np.sum(((B_arr - 3.0) / B_se_arr) ** 2))
    B_const = float(np.sum(Wt * B_arr) / np.sum(Wt))
    chi2_const_best = float(np.sum(((B_arr - B_const) / B_se_arr) ** 2))

    # weighted mean B over the Kerr grid and its spread
    return {
        "n_points": n,
        "B0_intercept": float(B0), "B0_se": B0_se,
        "slope": float(slope), "slope_se": slope_se, "slope_z": slope_z,
        "slope_significant_3sigma": bool(abs(slope_z) > 3.0),
        "chi2_linear": chi2_lin, "dof_linear": max(n - 2, 1),
        "chi2_const_eq_3": chi2_const3, "dof_const": max(n - 1, 1),
        "chi2_const_best": chi2_const_best,
        "B_weighted_mean": B_const,
        "delta_chi2_const3_minus_linear": chi2_const3 - chi2_lin,
        "B_range": [float(np.min(B_arr)), float(np.max(B_arr))],
    }


# ==========================================================================
# PLOT
# ==========================================================================

def plot_B_vs_spin(kerr_rows, btz_rows, trend, figname="B_vs_spin.png"):
    """B(a) curve with CI bars; BTZ points marked; D-1=3 line; old bounded B."""
    fig, ax = plt.subplots(figsize=(10, 7))

    a_arr = np.array([row["a"] for row in kerr_rows])
    B_arr = np.array([row["B"] for row in kerr_rows])
    Blo = np.array([row["B_ci95"][0] for row in kerr_rows])
    Bhi = np.array([row["B_ci95"][1] for row in kerr_rows])
    yerr = np.vstack([B_arr - Blo, Bhi - B_arr])
    ax.errorbar(a_arr, B_arr, yerr=yerr, fmt='o-', color='crimson', capsize=5,
                ms=8, lw=1.8, label="Kerr B(a), unbounded log-log fit (95% boot CI)",
                zorder=4)

    # B(a) trend line
    a_fine = np.linspace(a_arr.min() - 0.02, a_arr.max() + 0.02, 100)
    ax.plot(a_fine, trend["B0_intercept"] + trend["slope"] * a_fine,
            'r--', lw=1.4, alpha=0.7,
            label=(f"trend: B={trend['B0_intercept']:.2f}"
                   f"{trend['slope']:+.2f}*a "
                   f"(slope z={trend['slope_z']:.1f})"))

    # D-1 = 3 dimensional-constant line
    ax.axhline(3.0, color='black', ls='-', lw=1.6,
               label="D-1 = 3 (dimensional constant)")

    # old BOUNDED B values for contrast (A hit bound 100 -> orientational)
    ax.scatter([0.6, 0.9], [OLD_BOUNDED_B["kerr_a0.6"], OLD_BOUNDED_B["kerr_a0.9"]],
               marker='x', s=130, color='gray', zorder=5,
               label="old BOUNDED B (A=100 artefact; orientational)")

    # BTZ points (asymptotics contrast)
    for row in btz_rows:
        ax.errorbar([row["a_equiv"]], [row["B"]],
                    yerr=[[row["B"] - row["B_ci95"][0]],
                          [row["B_ci95"][1] - row["B"]]],
                    fmt='s', color='steelblue', capsize=5, ms=10, zorder=6,
                    label=f"BTZ J={row['J']} (Omega~r^-2), B={row['B']:.2f}")

    ax.set_xlabel("Kerr spin a  (BTZ plotted at its J for visual contrast)",
                  fontsize=12)
    ax.set_ylabel(r"$B$  in  $W_{sr}\sim\Omega^B$", fontsize=13)
    ax.set_title("VYPOCET-26: superradiant exponent B vs spin\n"
                 "H5g-5: is B continuous in frame dragging, or the constant D-1=3?",
                 fontsize=12)
    ax.legend(fontsize=9, loc='best')
    ax.grid(True, alpha=0.3)
    fig.tight_layout()
    fig.savefig(os.path.join(PLOTDIR, figname), dpi=150)
    plt.close(fig)
    print(f"  Saved {figname}")


# ==========================================================================
# ATOMIC RESULTS WRITER
# ==========================================================================

def write_results(results):
    """Atomic JSON write: tmp + os.replace, so an interrupt leaves a clean file."""
    tmp = RESULTS_PATH + ".tmp"
    with open(tmp, "w") as f:
        json.dump(results, f, indent=2)
    os.replace(tmp, RESULTS_PATH)


# ==========================================================================
# MAIN
# ==========================================================================

def run(wall_clock_cap_min=25.0):
    t_start = time.time()
    M = 1.0
    N = 1600
    T = Phi = 1.4
    seeds = [101, 202, 303, 404, 505]
    KMAX = 35.0; NW = 71
    ws = np.linspace(-KMAX, KMAX, NW)
    ks = np.linspace(-KMAX, KMAX, NW)
    n_boot = 2000

    # Full Kerr spin grid (the discriminator).  If the wall-clock cap looms we
    # drop to the reduced grid and RECORD it.
    spin_grid_full = [0.3, 0.5, 0.6, 0.7, 0.8, 0.9, 0.95, 0.99]
    spin_grid_reduced = [0.3, 0.5, 0.6, 0.7, 0.8, 0.9]

    # Near-zone radii just outside r_erg=2M where W_sr>0 (validated by probe).
    kerr_radii = [2.02, 2.05, 2.10, 2.20, 2.40, 2.80]
    # BTZ near-zone radii just outside r_erg=1M.
    btz_radii = [1.02, 1.05, 1.10, 1.20, 1.35, 1.50, 1.80]

    results = {
        "task": "VYPOCET-26 KERR B-EXPONENT SCAN (closes H5g-5)",
        "status": "running",
        "question": ("Is B in W_sr ~ Omega(r)^B a CONTINUOUS function of frame "
                     "dragging/asymptotics, or the dimensional constant D-1=3?"),
        "conventions": {
            "lever": "2D massless => G_R=(1/2)C [1611.10281 eq.9]",
            "iDelta": "iDelta=i*(1/2)(C-C^T); SJ W=sum_{lam>0} lam v v^dagger",
            "Kerr_section": "h=[[-(1-2M/r),-2Ma/r],[-2Ma/r,r^2+a^2+2Ma^2/r]], r_erg=2M",
            "BTZ_section": "h=[[M-r^2,-J/2],[-J/2,r^2]], r_erg=sqrt(M)",
            "Omega": "Omega=-g_tphi/g_phiphi (ZAMO); Kerr~r^-3, BTZ~r^-2",
            "W_sr": "W_sr=P(w*(w-k*Omega)<0) superradiant wedge weight",
            "B_fit": ("UNBOUNDED log-log regression log W_sr = log A + B log Omega; "
                      "B=slope, A free (fixes VYPOCET-14 A=100 bound artefact); "
                      "regression SE + bootstrap-over-seeds 95% CI"),
            "params": {"M": M, "N": N, "T": T, "Phi": Phi, "seeds": seeds,
                       "kmax": KMAX, "nw": NW, "n_boot": n_boot},
            "old_bounded_B_orientational": OLD_BOUNDED_B,
            "inherited_from": ["VYPOCET-14 sj-threshold-scan",
                               "VYPOCET-15 sj-far-zone",
                               "VYPOCET-10 sj-eigenvector-superradiance"],
        },
        "kerr_b_scan": [],
        "btz_b_scan": [],
        "spin_grid_used": None,
        "Ba_trend": None,
        "verdict": None,
    }
    write_results(results)

    # =====================================================================
    # KERR B(a) SCAN  -- choose grid honoring the wall-clock cap
    # =====================================================================
    # estimate cost: per point ~ 1.5s; n_points ~ len(radii)*n_spins*n_seeds
    est_per_point = 1.6
    pts_full = len(kerr_radii) * len(spin_grid_full) * len(seeds)
    pts_btz = len(btz_radii) * 2 * len(seeds)
    est_full_min = est_per_point * (pts_full + pts_btz) / 60.0
    if est_full_min > 0.75 * wall_clock_cap_min:
        spin_grid = spin_grid_reduced
        grid_note = (f"REDUCED to {len(spin_grid)} spins: estimated full-grid "
                     f"time {est_full_min:.1f} min > 0.75*cap "
                     f"{0.75*wall_clock_cap_min:.1f} min.")
    else:
        spin_grid = spin_grid_full
        grid_note = (f"FULL {len(spin_grid)} spins: estimated time "
                     f"{est_full_min:.1f} min within cap {wall_clock_cap_min} min.")
    print(f"\n=== Kerr B(a) scan: spins={spin_grid} ===\n{grid_note}")
    results["spin_grid_used"] = {"spins": spin_grid, "note": grid_note}
    write_results(results)

    kerr_rows = []
    for a in spin_grid:
        # cap guard: stop adding spins if we are within 4 min of the cap
        elapsed_min = (time.time() - t_start) / 60.0
        if elapsed_min > wall_clock_cap_min - 4.0 and kerr_rows:
            results["spin_grid_used"]["interrupted_after"] = [row["a"] for row in kerr_rows]
            results["spin_grid_used"]["interrupt_note"] = (
                f"wall-clock guard: stopped before a={a} at {elapsed_min:.1f} min")
            print(f"  [cap guard] stopping before a={a} at {elapsed_min:.1f} min")
            break
        rp, rm, r_erg = kerr_surfaces(M, a)
        print(f"\n-- Kerr a={a} (r_+={rp:.3f}, r_erg={r_erg:.3f}) --")
        recs = scan_config(kerr_section, (M, a), omega_kerr_analytic, (M, a),
                           kerr_radii, r_erg, rp, seeds, N, T, Phi, ws, ks,
                           label=f"Kerr a={a}")
        bres = extract_B(recs, n_boot=n_boot)
        row = {
            "geometry": "Kerr", "a": float(a),
            "r_plus": float(rp), "r_erg": float(r_erg),
            "records": recs,
            "B_extraction": bres,
        }
        if bres["fit"]["ok"]:
            row["B"] = bres["fit"]["B"]
            row["B_se"] = bres["fit"]["B_se"]
            row["R2_loglog"] = bres["fit"]["R2_loglog"]
            row["corr_loglog"] = bres["fit"]["corr_loglog"]
            boot = bres.get("bootstrap", {})
            row["B_ci95"] = boot.get("B_ci95", [bres["fit"]["B"], bres["fit"]["B"]])
            row["B_boot_se"] = boot.get("B_boot_se")
            print(f"   => Kerr a={a}: B={row['B']:.3f}+/-{row['B_se']:.3f} "
                  f"(boot CI {row['B_ci95'][0]:.2f}..{row['B_ci95'][1]:.2f}), "
                  f"R2={row['R2_loglog']:.4f}, n={bres['n_points_used']}")
        kerr_rows.append(row)
        results["kerr_b_scan"] = kerr_rows
        write_results(results)  # progressive/atomic flush per spin

    # =====================================================================
    # BTZ ASYMPTOTICS CONTRAST  (J in {0.6, 0.9})
    # =====================================================================
    print("\n=== BTZ asymptotics contrast (Omega~r^-2 vs Kerr r^-3) ===")
    btz_rows = []
    for J in [0.6, 0.9]:
        rp, rm, r_erg = btz_surfaces(M, J)
        print(f"\n-- BTZ J={J} (r_+={rp:.3f}, r_erg={r_erg:.3f}) --")
        recs = scan_config(btz_section, (M, J), omega_btz_analytic, (M, J),
                           btz_radii, r_erg, rp, seeds, N, T, Phi, ws, ks,
                           label=f"BTZ J={J}")
        bres = extract_B(recs, n_boot=n_boot)
        row = {
            "geometry": "BTZ", "J": float(J), "a_equiv": float(J),
            "r_plus": float(rp), "r_erg": float(r_erg),
            "records": recs, "B_extraction": bres,
        }
        if bres["fit"]["ok"]:
            row["B"] = bres["fit"]["B"]
            row["B_se"] = bres["fit"]["B_se"]
            row["R2_loglog"] = bres["fit"]["R2_loglog"]
            row["corr_loglog"] = bres["fit"]["corr_loglog"]
            boot = bres.get("bootstrap", {})
            row["B_ci95"] = boot.get("B_ci95", [bres["fit"]["B"], bres["fit"]["B"]])
            row["B_boot_se"] = boot.get("B_boot_se")
            print(f"   => BTZ J={J}: B={row['B']:.3f}+/-{row['B_se']:.3f} "
                  f"(boot CI {row['B_ci95'][0]:.2f}..{row['B_ci95'][1]:.2f}), "
                  f"R2={row['R2_loglog']:.4f}, n={bres['n_points_used']}")
        btz_rows.append(row)
        results["btz_b_scan"] = btz_rows
        write_results(results)

    # =====================================================================
    # B(a) TREND FIT  + verdict
    # =====================================================================
    kerr_fit_rows = [r for r in kerr_rows if "B" in r]
    if len(kerr_fit_rows) >= 3:
        a_arr = [r["a"] for r in kerr_fit_rows]
        B_arr = [r["B"] for r in kerr_fit_rows]
        # use the bootstrap SE (dominant) where available, else regression SE
        B_se_arr = [r.get("B_boot_se") or r["B_se"] for r in kerr_fit_rows]
        trend = fit_Ba_trend(a_arr, B_arr, B_se_arr)
        results["Ba_trend"] = trend
        print("\n=== B(a) trend ===")
        print(f"  slope = {trend['slope']:+.3f} +/- {trend['slope_se']:.3f} "
              f"(z={trend['slope_z']:.2f}, 3sigma={trend['slope_significant_3sigma']})")
        print(f"  B range over Kerr grid = {trend['B_range']}")
        print(f"  chi2 vs constant B=3 (D-1) = {trend['chi2_const_eq_3']:.1f} "
              f"(dof {trend['dof_const']}); chi2 linear = {trend['chi2_linear']:.1f}")

        # verdict logic
        slope_sig = trend["slope_significant_3sigma"]
        const3_rejected = trend["chi2_const_eq_3"] / trend["dof_const"] > 4.0
        btz_B = [r["B"] for r in btz_rows if "B" in r]
        kerr_B_range = trend["B_range"]
        btz_below_kerr = bool(btz_B and min(btz_B) < kerr_B_range[0] - 0.3)

        if slope_sig:
            cont = ("B varies SMOOTHLY and SIGNIFICANTLY with Kerr spin a "
                    f"(slope {trend['slope']:+.2f}, z={trend['slope_z']:.1f}); "
                    "B is a CONTINUOUS function of frame dragging, NOT the "
                    "dimensional constant D-1=3.")
        else:
            cont = ("B(a) slope is not >3sigma over the measured grid; B may be "
                    "approximately constant in a within errors.")
        results["verdict"] = {
            "B_continuous_in_spin": bool(slope_sig),
            "D_minus_1_eq_3_refuted": bool(const3_rejected),
            "btz_off_kerr_curve": btz_below_kerr,
            "summary": cont,
            "kerr_B_range": kerr_B_range,
            "btz_B": btz_B,
            "note": ("If B were the dimensional constant D-1=3 it would be flat "
                     "in a AND identical for BTZ (also 3D->2D section). A "
                     "significant B(a) slope and/or a BTZ B far off the Kerr "
                     "curve favours a CONTINUOUS dependence on frame-dragging / "
                     "asymptotic falloff over a single dimensional constant."),
        }
    else:
        results["Ba_trend"] = {"error": "fewer than 3 Kerr B points"}
        results["verdict"] = {"error": "insufficient Kerr points for trend"}

    # =====================================================================
    # PLOT + finalize
    # =====================================================================
    print("\n=== Plot ===")
    if len(kerr_fit_rows) >= 2 and results.get("Ba_trend") and "slope" in results["Ba_trend"]:
        plot_B_vs_spin(kerr_fit_rows, [r for r in btz_rows if "B" in r],
                       results["Ba_trend"])

    results["status"] = "complete"
    results["wall_clock_min"] = float((time.time() - t_start) / 60.0)
    write_results(results)
    print(f"\nDONE in {results['wall_clock_min']:.1f} min. Wrote {RESULTS_PATH}")
    return results


if __name__ == "__main__":
    run()
