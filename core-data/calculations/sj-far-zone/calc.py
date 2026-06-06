#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
VYPOCET-15  --  FAR-ZONE SCAN: MODEL E vs MODEL S DISAMBIGUATION
            Kerr a=0.6, r = 5M..20M (>=10 radii, >=4 seeds, N~1600)
==========================================================================

MOTIVATION (from VYPOCET-14):
  For Kerr a=0.6 the linear correlation slightly favoured Model E
  (1/(r-r_erg)) over Model S (Omega(r)^B) because the two predictors are
  strongly correlated near the ergosphere (r in [2M, 5M]).  In the far zone
  r=5M..20M the models DIVERGE:
    * Model S: W_sr ~ Omega(r)^B ~ r^{-3B}  (r^{-3} from Kerr Omega ~ Ma/r^3)
    * Model E: W_sr ~ 1/(r-r_erg) ~ 1/r     (since r >> r_erg=2M)
  The log-log slopes are -3B (Model S, with B~4 => slope~-12) vs -1 (Model E).
  These are completely separated: the far-zone data can cleanly distinguish them.

ADDITIONAL GOALS:
  (a) Measure A_W in the far zone: toy model (VYPOCET-10) predicts
      |A_W| ~ shear ~ Omega(r) ~ r^{-3}, i.e. a clean power law.
  (b) Joint fit: far-zone data combined with VYPOCET-14 near-zone records
      for Kerr a=0.6 (loaded from results.json); joint AIC/BIC verdict.
  (c) Single clearest plot: log-log W_sr vs Omega(r) with both model fits
      and the far-zone / near-zone split clearly labeled.

CONVENTIONS: IDENTICAL to VYPOCET-14 / VYPOCET-10 / VYPOCET-08.
  * 2D massless scalar => G_R = (1/2) C (conformally invariant)
  * iDelta = i*(1/2)(C - C^T); SJ W = positive part of iDelta
  * Kerr equatorial h=[[-(1-2M/r),-2Ma/r],[-2Ma/r,r^2+a^2+2Ma^2/r]], r_erg=2M
  * Omega = -g_tphi/g_phiphi (ZAMO angular velocity)
  * Superradiant wedge: w*(w-k*Omega) < 0
  * A_W = (mean_ReW_co - mean_ReW_cc)/(|mean_ReW_co|+|mean_ReW_cc|)
  * N=1600, >=4 seeds, T=Phi=1.4 (inherited from VYPOCET-14)

EXPECTED PHYSICS:
  In the far zone Omega(r) = 2Ma/r^3 -> 0 as r -> infinity.
  W_sr ~ Omega^B means W_sr is very small here but nonzero.
  We need to detect W_sr > 0 at these radii — this requires a sufficiently
  fine (w,k) grid.  We use NW=71, KMAX=35 (same as VYPOCET-14).
  Note: W_sr ~ 0 at r>=3.5 in VYPOCET-14 with this grid; in the far zone we
  may measure W_sr=0 but that itself is evidence — Model E (1/(r-r_erg))
  would predict ~1/(r-2) which still should produce non-zero W_sr at r=5,6,...
  If W_sr=0 for r>=5 under both models, we use A_W as the discriminator.
"""

import json
import os
import warnings
import numpy as np
import scipy.optimize as opt
import scipy.stats as stats
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm

OUTDIR = os.path.dirname(os.path.abspath(__file__))
PLOTDIR = os.path.join(OUTDIR, "plots")
os.makedirs(PLOTDIR, exist_ok=True)
np.set_printoptions(precision=6, suppress=True)

# Path to VYPOCET-14 results for joint fit
V14_RESULTS = os.path.join(
    os.path.dirname(OUTDIR), "sj-threshold-scan", "results.json")

# ==========================================================================
# GEOMETRY  (identical to VYPOCET-14)
# ==========================================================================

def kerr_section(M, a, r):
    """Equatorial Kerr fixed-r (t,phi) 2-metric h."""
    g_tt = -(1.0 - 2.0 * M / r)
    g_tp = -2.0 * M * a / r
    g_pp = r**2 + a**2 + 2.0 * M * a**2 / r
    return np.array([[g_tt, g_tp], [g_tp, g_pp]], dtype=float)


def kerr_surfaces(M, a):
    """Returns (r_+, r_-, r_erg) for Kerr."""
    rp = M + np.sqrt(M**2 - a**2)
    rm = M - np.sqrt(M**2 - a**2)
    r_erg = 2.0 * M
    return rp, rm, r_erg


def null_slopes(h):
    """Null slopes dphi/dt: g_pp s^2 + 2 g_tp s + g_tt = 0."""
    A = h[1, 1]; B = 2 * h[0, 1]; Cc = h[0, 0]
    disc = B * B - 4 * A * Cc
    if disc < 0:
        return np.nan, np.nan
    sm = (-B - np.sqrt(disc)) / (2 * A)
    sp = (-B + np.sqrt(disc)) / (2 * A)
    return sm, sp


def drag_slope(h):
    """Omega = -g_tphi/g_phiphi (ZAMO angular velocity)."""
    return -h[0, 1] / h[1, 1]


def omega_kerr_analytic(M, a, r):
    """Kerr ZAMO: Omega(r) = 2Ma / (r^3 + a^2*r + 2Ma^2) ~ 2Ma/r^3 for large r."""
    return 2.0 * M * a / (r**3 + a**2 * r + 2.0 * M * a**2)


# ==========================================================================
# SJ PIPELINE  (identical to VYPOCET-14)
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
    """Return (lambda_pos, V_pos, W) of iDelta = i*(1/2)(C-C^T)."""
    iDelta = 1j * 0.5 * (C - C.T)
    wv, V = np.linalg.eigh(iDelta)
    pos = wv > 1e-9
    lam = wv[pos]; Vp = V[:, pos]
    W = (Vp * lam) @ Vp.conj().T
    return lam, Vp, W


def aw_from_C_W(C, W, coords):
    """Compute A_W directional asymmetry from SJ Wightman W and causal matrix C."""
    xi, yi = np.where(C > 0)
    if len(xi) < 10:
        return 0.0, np.nan, np.nan
    dphi_links = coords[xi, 1] - coords[yi, 1]
    ReW_links = np.real(W[xi, yi])
    co = dphi_links > 0; cc = dphi_links < 0
    if co.sum() == 0 or cc.sum() == 0:
        return 0.0, np.nan, np.nan
    m_co = float(np.mean(ReW_links[co])); m_cc = float(np.mean(ReW_links[cc]))
    denom = abs(m_co) + abs(m_cc)
    A_W = (m_co - m_cc) / denom if denom > 1e-12 else 0.0
    return float(A_W), float(m_co), float(m_cc)


# ==========================================================================
# OCCUPATION MAP AND SUPERRADIANT WEDGE WEIGHT
# ==========================================================================

def occupation_map(coords, lam, Vp, ws, ks):
    """P(w,k) = sum_modes lambda * |<plane(w,k)|v>|^2, normalized to sum 1."""
    t = coords[:, 0]; ph = coords[:, 1]; N_pts = coords.shape[0]
    phase_t = np.exp(1j * np.outer(ws, t))    # (Nw, N_pts)
    phase_k = np.exp(-1j * np.outer(ks, ph))  # (Nk, N_pts)
    P = np.zeros((len(ws), len(ks)))
    for iw in range(len(ws)):
        ptw = phase_t[iw]
        phasewk = phase_k * ptw[np.newaxis, :]
        proj_wk = (phasewk @ Vp) / N_pts
        P[iw, :] = (np.abs(proj_wk) ** 2) @ lam
    tot = P.sum()
    return P / tot if tot > 0 else P


def superradiant_wedge_weight(P, ws, ks, Omega):
    """W_sr = weight of P in the wedge w*(w - k*Omega) < 0."""
    WW, KK = np.meshgrid(ws, ks, indexing="ij")
    sr_mask = WW * (WW - KK * Omega) < 0
    return float(P[sr_mask].sum())


# ==========================================================================
# ONE-POINT + RADIAL SCAN
# ==========================================================================

def compute_one(r, seed, N, T, Phi, ws, ks, M=1.0, a=0.6):
    """Run the full SJ pipeline for one (r, seed)."""
    rng = np.random.default_rng(seed)
    coords = sprinkle(N, T, Phi, rng)
    h = kerr_section(M, a, r)
    Omega = drag_slope(h)
    C = causal_matrix(coords, h)
    lam, Vp, W = sj_positive(C)

    P = occupation_map(coords, lam, Vp, ws, ks)
    W_sr = superradiant_wedge_weight(P, ws, ks, Omega)

    A_W, m_co, m_cc = aw_from_C_W(C, W, coords)

    return {
        "Omega": float(Omega),
        "W_sr": float(W_sr),
        "A_W": float(A_W),
        "m_co": float(m_co) if not np.isnan(m_co) else None,
        "m_cc": float(m_cc) if not np.isnan(m_cc) else None,
        "n_links": int(C.sum()),
        "n_pos": int(lam.shape[0]),
    }


def radial_scan_farzone(radii, seeds, N, T, Phi, ws, ks, M=1.0, a=0.6):
    """Far-zone radial scan for Kerr a=0.6 (r=5M..20M)."""
    rp, rm, r_erg = kerr_surfaces(M, a)
    records = []
    for r in radii:
        h = kerr_section(M, a, r)
        Omega_analytic = omega_kerr_analytic(M, a, r)
        Omega_metric = drag_slope(h)
        per_seed = [compute_one(r, s, N, T, Phi, ws, ks, M=M, a=a)
                    for s in seeds]
        W_sr_vals = [d["W_sr"] for d in per_seed]
        AW_vals = [d["A_W"] for d in per_seed]

        rec = {
            "r": float(r),
            "r_over_rerg": float(r / r_erg),
            "Omega": float(Omega_metric),
            "Omega_analytic": float(Omega_analytic),
            "log10_Omega": float(np.log10(max(Omega_metric, 1e-15))),
            "log10_r": float(np.log10(r)),
            "W_sr_mean": float(np.mean(W_sr_vals)),
            "W_sr_sd": float(np.std(W_sr_vals, ddof=1)) if len(W_sr_vals) > 1 else 0.0,
            "W_sr_all": W_sr_vals,
            "A_W_mean": float(np.mean(AW_vals)),
            "A_W_sd": float(np.std(AW_vals, ddof=1)) if len(AW_vals) > 1 else 0.0,
            "A_W_all": AW_vals,
            "n_seeds": len(seeds),
            "zone": "far",
        }
        print(f"  r={r:.2f}M: Omega={Omega_metric:.6f}, W_sr={rec['W_sr_mean']:.6f}"
              f"±{rec['W_sr_sd']:.6f}, A_W={rec['A_W_mean']:+.5f}±{rec['A_W_sd']:.5f}")
        records.append(rec)
    return records


# ==========================================================================
# LOAD VYPOCET-14 NEAR-ZONE DATA FOR JOINT FIT
# ==========================================================================

def load_v14_nearzone(path, a_label="scan_kerr_a06", r_erg=2.0, r_max_nearzone=5.0):
    """Load VYPOCET-14 Kerr a=0.6 records for r in (r_erg, r_max_nearzone)."""
    if not os.path.exists(path):
        print(f"  WARNING: VYPOCET-14 results not found at {path}")
        return []
    with open(path) as f:
        v14 = json.load(f)
    scan = v14.get(a_label, {}).get("records", [])
    # Keep only exterior-ergosphere radii in near zone
    near = [rec for rec in scan
            if rec["r"] > r_erg + 0.02 and rec["r"] < r_max_nearzone]
    print(f"  Loaded {len(near)} near-zone records from VYPOCET-14 (r in [{r_erg:.2f}, {r_max_nearzone:.1f}])")
    return near


# ==========================================================================
# POWER-LAW FIT IN LOG-LOG SPACE
# ==========================================================================

def powerlaw_fit_loglog(x_arr, y_arr, y_sd_arr, label=""):
    """Fit log(y) = log(A) + B*log(x) by weighted least squares.
    Returns (A, B, A_err, B_err, chi2_dof, R2)."""
    mask = (x_arr > 0) & (y_arr > 0)
    if mask.sum() < 3:
        return None
    lx = np.log(x_arr[mask])
    ly = np.log(y_arr[mask])
    # Weights: dy/y propagated from y_sd
    sig_y = y_sd_arr[mask]
    sig_ly = np.where(y_arr[mask] > 0, sig_y / y_arr[mask], 1.0)
    sig_ly = np.maximum(sig_ly, 0.01)  # floor at 1%

    # Design matrix for log(A) + B*log(x)
    X = np.column_stack([np.ones_like(lx), lx])
    W = 1.0 / sig_ly**2
    XtWX = X.T @ (W[:, None] * X)
    XtWy = X.T @ (W * ly)
    try:
        params, _, _, _ = np.linalg.lstsq(XtWX, XtWy, rcond=None)
    except np.linalg.LinAlgError:
        return None
    log_A, B = params
    A = np.exp(log_A)

    # Residuals and chi2
    ly_pred = log_A + B * lx
    resid = (ly - ly_pred) / sig_ly
    n = len(lx)
    chi2 = float(np.sum(resid**2))
    chi2_dof = chi2 / max(n - 2, 1)

    # Covariance
    try:
        cov = np.linalg.inv(XtWX)
        B_err = float(np.sqrt(cov[1, 1]))
        A_err = A * float(np.sqrt(cov[0, 0]))
    except Exception:
        B_err = np.nan
        A_err = np.nan

    # R^2 in log-log space
    ss_tot = float(np.sum((ly - np.mean(ly))**2))
    ss_res = float(np.sum((ly - ly_pred)**2))
    R2 = 1.0 - ss_res / ss_tot if ss_tot > 0 else np.nan

    return {
        "A": float(A), "B": float(B),
        "A_err": float(A_err), "B_err": float(B_err),
        "chi2": float(chi2), "chi2_dof": float(chi2_dof),
        "R2_loglog": float(R2),
        "n_points": int(n),
        "label": label,
    }


# ==========================================================================
# ONSET MODEL FITS (reuse from VYPOCET-14)
# ==========================================================================

def model_E_onset(r, r_erg, W_inf, r_scale):
    """Model E: Lorentzian at r_erg."""
    x = r - r_erg
    return W_inf / (1.0 + (x / r_scale) ** 2)


def model_S_onset(Omega_arr, A, B):
    """Model S: W_sr = A * Omega(r)^B."""
    return A * (np.clip(Omega_arr, 1e-15, None) ** B)


def fit_aic_bic(r_arr, W_arr, W_sd_arr, Omega_arr, r_erg, label=""):
    """Fit Models E and S; return AIC, BIC, comparison dict."""
    from scipy.optimize import least_squares
    mask = r_arr > r_erg + 0.02
    r_m = r_arr[mask]; W_m = W_arr[mask]; Om_m = Omega_arr[mask]
    sig_m = np.maximum(W_sd_arr[mask], 1e-7)
    n = len(r_m)
    if n < 3:
        return {"error": f"Too few points ({n}) for fit"}

    results = {}

    # --- Model E ---
    def resid_E(params):
        W_inf, r_scale = params
        pred = model_E_onset(r_m, r_erg, W_inf, r_scale)
        return (W_m - pred) / sig_m

    try:
        p0_E = [max(float(np.max(W_m)), 1e-6), 1.0]
        bounds_E = ([0, 0.001], [10, 100])
        res_E = least_squares(resid_E, p0_E, bounds=bounds_E, method='trf')
        params_E = res_E.x
        chi2_E = float(np.sum(res_E.fun ** 2))
        k_E = 2
        aic_E = chi2_E + 2 * k_E
        bic_E = chi2_E + k_E * np.log(n)
        results["model_E"] = {
            "params": {"W_inf": float(params_E[0]), "r_scale": float(params_E[1])},
            "chi2": chi2_E, "chi2_dof": chi2_E / max(n - k_E, 1),
            "k": k_E, "n": n,
            "AIC": float(aic_E), "BIC": float(bic_E),
            "converged": bool(res_E.success or res_E.cost < 1.0),
        }
    except Exception as e:
        results["model_E"] = {"error": str(e)}

    # --- Model S ---
    def resid_S(params):
        A, B = params
        pred = model_S_onset(Om_m, A, B)
        return (W_m - pred) / sig_m

    try:
        p0_S = [max(float(np.max(W_m) / max(float(np.max(Om_m)), 1e-6)), 1e-6), 3.0]
        bounds_S = ([0, 0.01], [1e8, 20])
        res_S = least_squares(resid_S, p0_S, bounds=bounds_S, method='trf')
        params_S = res_S.x
        chi2_S = float(np.sum(res_S.fun ** 2))
        k_S = 2
        aic_S = chi2_S + 2 * k_S
        bic_S = chi2_S + k_S * np.log(n)
        results["model_S"] = {
            "params": {"A": float(params_S[0]), "B": float(params_S[1])},
            "chi2": chi2_S, "chi2_dof": chi2_S / max(n - k_S, 1),
            "k": k_S, "n": n,
            "AIC": float(aic_S), "BIC": float(bic_S),
            "converged": bool(res_S.success or res_S.cost < 1.0),
        }
    except Exception as e:
        results["model_S"] = {"error": str(e)}

    if "error" not in results.get("model_E", {}) and "error" not in results.get("model_S", {}):
        delta_aic = results["model_E"]["AIC"] - results["model_S"]["AIC"]
        delta_bic = results["model_E"]["BIC"] - results["model_S"]["BIC"]
        results["comparison"] = {
            "delta_AIC_E_minus_S": float(delta_aic),
            "delta_BIC_E_minus_S": float(delta_bic),
            "preferred_by_AIC": "Model_E" if delta_aic < 0 else "Model_S",
            "preferred_by_BIC": "Model_E" if delta_bic < 0 else "Model_S",
            "AIC_decisive": bool(abs(delta_aic) > 2),
            "AIC_strong": bool(abs(delta_aic) > 6),
            "label": label,
        }
    return results


# ==========================================================================
# DISCRIMINANT: log-log correlation W_sr vs Omega vs 1/(r-r_erg)
# ==========================================================================

def discriminant_loglog(records, r_erg):
    """For records with W_sr > 0, compute log-log Pearson corr vs Omega and 1/(r-r_erg)."""
    ext = [rec for rec in records
           if rec.get("r", 0) > r_erg + 0.02 and rec.get("W_sr_mean", 0) > 0]
    if len(ext) < 3:
        return {"note": "Too few non-zero W_sr points for log-log discriminant",
                "n_points": len(ext)}
    r_arr = np.array([rec["r"] for rec in ext])
    W_arr = np.array([rec["W_sr_mean"] for rec in ext])
    Om_arr = np.array([rec["Omega"] for rec in ext])
    X_E = 1.0 / (r_arr - r_erg + 0.01)
    X_S = Om_arr

    def corr_loglog(X, Y):
        if np.all(X > 0) and np.all(Y > 0):
            return float(np.corrcoef(np.log(X), np.log(Y))[0, 1])
        return np.nan

    c_E = corr_loglog(X_E, W_arr)
    c_S = corr_loglog(X_S, W_arr)
    pref = "Model_S" if abs(c_S) > abs(c_E) else "Model_E"

    # Also linear
    c_E_lin = float(np.corrcoef(X_E, W_arr)[0, 1])
    c_S_lin = float(np.corrcoef(X_S, W_arr)[0, 1])
    pref_lin = "Model_S" if abs(c_S_lin) > abs(c_E_lin) else "Model_E"

    return {
        "corr_loglog_E": c_E, "corr_loglog_S": c_S,
        "corr_linear_E": c_E_lin, "corr_linear_S": c_S_lin,
        "preferred_loglog": pref, "preferred_linear": pref_lin,
        "n_points": len(ext),
    }


# ==========================================================================
# A_W POWER-LAW: fit |A_W| ~ r^gamma
# ==========================================================================

def aw_powerlaw(records, r_erg, snr_threshold=3.0):
    """Fit |A_W| ~ r^gamma in log-log for exterior records with |A_W| > 0.
    Also fits restricted to SNR >= snr_threshold for robustness."""
    ext = [rec for rec in records
           if rec.get("r", 0) > r_erg + 0.02 and abs(rec.get("A_W_mean", 0)) > 1e-4]
    if len(ext) < 3:
        return {"note": "Too few non-zero A_W points", "n_points": len(ext)}
    r_arr = np.array([rec["r"] for rec in ext])
    AW_arr = np.abs(np.array([rec["A_W_mean"] for rec in ext]))
    AW_sd = np.array([rec["A_W_sd"] for rec in ext])
    Om_arr = np.array([rec["Omega"] for rec in ext])

    # SNR-weighted selection
    snr = np.where(AW_sd > 0, AW_arr / AW_sd, 0.0)
    hi_mask = snr >= snr_threshold

    # Fit 1: |A_W| ~ r^gamma (all)
    fit_r = powerlaw_fit_loglog(r_arr, AW_arr, AW_sd, label="|A_W| vs r (all)")
    # Fit 2: |A_W| ~ Omega^delta (all)
    fit_om = powerlaw_fit_loglog(Om_arr, AW_arr, AW_sd, label="|A_W| vs Omega (all)")
    # Fit 3: |A_W| ~ r^gamma (high-SNR)
    fit_r_hi = powerlaw_fit_loglog(r_arr[hi_mask], AW_arr[hi_mask], AW_sd[hi_mask],
                                    label=f"|A_W| vs r (SNR>={snr_threshold})") if hi_mask.sum() >= 3 else None
    # Fit 4: |A_W| ~ Omega^delta (high-SNR)
    fit_om_hi = powerlaw_fit_loglog(Om_arr[hi_mask], AW_arr[hi_mask], AW_sd[hi_mask],
                                     label=f"|A_W| vs Omega (SNR>={snr_threshold})") if hi_mask.sum() >= 3 else None

    # Toy model predicts: |A_W| ~ Omega ~ r^{-3}, so gamma=-3, delta=1
    return {
        "fit_r": fit_r,
        "fit_Omega": fit_om,
        "fit_r_highSNR": fit_r_hi,
        "fit_Omega_highSNR": fit_om_hi,
        "snr_threshold": float(snr_threshold),
        "n_highSNR": int(hi_mask.sum()),
        "toy_model_prediction_gamma_r": -3.0,
        "toy_model_prediction_delta_Omega": 1.0,
        "note": ("Toy model (VYPOCET-10): |A_W| ~ shear ~ Omega(r) ~ r^{-3} in far zone. "
                 "Fit gamma_r should be ~ -3; delta_Omega ~ 1. "
                 "High-SNR subset is more reliable for the far-zone tail."),
        "n_points": len(ext),
    }


# ==========================================================================
# JOINT FIT: near-zone (V14) + far-zone (V15) combined
# ==========================================================================

def joint_fit(near_records, far_records, r_erg, M=1.0, a=0.6):
    """Fit Model E and Model S on combined near+far zone data."""
    all_records = []
    for rec in near_records:
        # Normalize field names (V14 format)
        all_records.append({
            "r": rec["r"],
            "W_sr_mean": rec["W_sr_mean"],
            "W_sr_sd": max(rec.get("W_sr_sd", 1e-5), 1e-7),
            "Omega": rec["Omega"],
            "zone": "near",
        })
    for rec in far_records:
        all_records.append({
            "r": rec["r"],
            "W_sr_mean": rec["W_sr_mean"],
            "W_sr_sd": max(rec.get("W_sr_sd", 1e-5), 1e-7),
            "Omega": rec["Omega"],
            "zone": "far",
        })
    # Sort by r
    all_records.sort(key=lambda x: x["r"])
    r_all = np.array([rec["r"] for rec in all_records])
    W_all = np.array([rec["W_sr_mean"] for rec in all_records])
    W_sd_all = np.array([rec["W_sr_sd"] for rec in all_records])
    Om_all = np.array([rec["Omega"] for rec in all_records])

    result = fit_aic_bic(r_all, W_all, W_sd_all, Om_all, r_erg,
                         label="Joint near+far zone")
    result["n_near"] = len(near_records)
    result["n_far"] = len(far_records)
    result["n_total"] = len(all_records)
    result["r_range"] = [float(r_all.min()), float(r_all.max())]
    return result, all_records


# ==========================================================================
# PLOTS
# ==========================================================================

def plot_key_loglog_Wsr_vs_Omega(near_records, far_records, models_far, models_near,
                                  models_joint, r_erg, M=1.0, a=0.6, figname="key_loglog_Wsr_vs_Omega.png"):
    """THE CLEAREST SINGLE PLOT: log-log W_sr vs Omega(r), both zones, both model fits."""
    fig, axes = plt.subplots(1, 2, figsize=(15, 6.5))

    # Collect data with zone labels
    near_Om = np.array([rec["Omega"] for rec in near_records if rec["W_sr_mean"] > 0])
    near_W  = np.array([rec["W_sr_mean"] for rec in near_records if rec["W_sr_mean"] > 0])
    near_Wsd= np.array([rec["W_sr_sd"] for rec in near_records if rec["W_sr_mean"] > 0])

    far_Om  = np.array([rec["Omega"] for rec in far_records if rec["W_sr_mean"] > 0])
    far_W   = np.array([rec["W_sr_mean"] for rec in far_records if rec["W_sr_mean"] > 0])
    far_Wsd = np.array([rec["W_sr_sd"] for rec in far_records if rec["W_sr_mean"] > 0])

    # ---- LEFT PANEL: log-log W_sr vs Omega ----
    ax = axes[0]
    if len(near_Om) > 0:
        ax.errorbar(near_Om, near_W, yerr=near_Wsd, fmt='o', color='crimson',
                    capsize=3, ms=6, label="Near zone (V14, r=2..5M)", zorder=3)
    if len(far_Om) > 0:
        ax.errorbar(far_Om, far_W, yerr=far_Wsd, fmt='s', color='steelblue',
                    capsize=3, ms=6, label="Far zone (V15, r=5..20M)", zorder=3)

    # Predicted lines from joint fit
    all_Om = np.concatenate([near_Om, far_Om]) if len(near_Om) > 0 and len(far_Om) > 0 else (near_Om if len(near_Om) > 0 else far_Om)
    if len(all_Om) > 0:
        Om_fine = np.logspace(np.log10(max(all_Om.min(), 1e-5)),
                              np.log10(all_Om.max()), 200)
        if "comparison" in models_joint and "error" not in models_joint.get("model_S", {}):
            p = models_joint["model_S"]["params"]
            ax.loglog(Om_fine, model_S_onset(Om_fine, p["A"], p["B"]),
                      'b-', lw=2.5, zorder=2,
                      label=f"Model S (joint): $A\\cdot\\Omega^{{{p['B']:.2f}}}$, "
                            f"AIC={models_joint['model_S']['AIC']:.1f}")
        if "comparison" in models_joint and "error" not in models_joint.get("model_E", {}):
            # Model E in terms of Omega: need r(Omega) inversion
            # For display: plot E model vs r, shown on same axes with Omega as proxy
            pass  # skip E on Omega axis, it's shown on right panel

        # Reference power laws (expected slopes)
        Om_ref = Om_fine
        # Model S slope ~ Omega^B: if B~4 this is steep in Omega
        # Model E: 1/(r-r_erg) ~ 1/r, but Omega ~ r^{-3}, so r ~ Om^{-1/3}
        # => Model E: W ~ r^{-1} ~ Om^{1/3}  (much shallower)
        # Draw reference slopes
        Om_mid = np.exp(0.5 * (np.log(Om_fine[0]) + np.log(Om_fine[-1])))
        W_ref_val = 1e-3  # arbitrary normalization for reference lines
        # Model S slope ~ Om^B: pick B=4
        ax.loglog(Om_fine,
                  W_ref_val * (Om_fine / Om_mid)**4.0,
                  'b:', lw=1.2, alpha=0.6, label="ref slope $\\Omega^4$ (Model S, B=4)")
        # Model E slope in Omega coords ~ Om^{1/3}
        ax.loglog(Om_fine,
                  W_ref_val * (Om_fine / Om_mid)**(1/3),
                  'r:', lw=1.2, alpha=0.6, label=r"ref slope $\Omega^{1/3}$ (Model E equiv.)")

    ax.set_xscale('log'); ax.set_yscale('log')
    ax.set_xlabel(r"$\Omega(r)$ [ZAMO angular velocity]", fontsize=12)
    ax.set_ylabel(r"$W_{sr}$ [superradiant wedge weight]", fontsize=12)
    ax.set_title("VYPOCET-15: log-log $W_{sr}$ vs $\\Omega(r)$\n"
                 "Far zone cleanly separates Model S vs Model E slopes", fontsize=11)
    ax.legend(fontsize=9)
    ax.grid(True, which='both', alpha=0.3)

    # ---- RIGHT PANEL: W_sr vs r (all zones) with both model fits ----
    ax2 = axes[1]
    near_r = np.array([rec["r"] for rec in near_records if rec["W_sr_mean"] > 0])
    near_W2 = np.array([rec["W_sr_mean"] for rec in near_records if rec["W_sr_mean"] > 0])
    near_Wsd2 = np.array([rec["W_sr_sd"] for rec in near_records if rec["W_sr_mean"] > 0])
    far_r = np.array([rec["r"] for rec in far_records if rec["W_sr_mean"] > 0])
    far_W2 = np.array([rec["W_sr_mean"] for rec in far_records if rec["W_sr_mean"] > 0])
    far_Wsd2 = np.array([rec["W_sr_sd"] for rec in far_records if rec["W_sr_mean"] > 0])

    if len(near_r) > 0:
        ax2.errorbar(near_r, near_W2, yerr=near_Wsd2, fmt='o', color='crimson',
                     capsize=3, ms=6, label="Near zone (V14)")
    if len(far_r) > 0:
        ax2.errorbar(far_r, far_W2, yerr=far_Wsd2, fmt='s', color='steelblue',
                     capsize=3, ms=6, label="Far zone (V15)")

    all_r_pts = np.concatenate([near_r, far_r]) if len(near_r) > 0 and len(far_r) > 0 else (near_r if len(near_r) > 0 else far_r)
    if len(all_r_pts) > 0:
        r_fine = np.logspace(np.log10(max(all_r_pts.min(), r_erg + 0.1)),
                             np.log10(all_r_pts.max()), 300)
        Om_fine_r = np.array([omega_kerr_analytic(M, a, rv) for rv in r_fine])

        if "comparison" in models_joint:
            if "error" not in models_joint.get("model_S", {}):
                p = models_joint["model_S"]["params"]
                ax2.loglog(r_fine, model_S_onset(Om_fine_r, p["A"], p["B"]),
                           'b-', lw=2.5, label=f"Model S (joint): B={p['B']:.2f}, "
                                               f"AIC={models_joint['model_S']['AIC']:.1f}")
            if "error" not in models_joint.get("model_E", {}):
                p = models_joint["model_E"]["params"]
                W_E = model_E_onset(r_fine, r_erg, p["W_inf"], p["r_scale"])
                ax2.loglog(r_fine, np.maximum(W_E, 1e-12), 'r--', lw=2.5,
                           label=f"Model E (joint): AIC={models_joint['model_E']['AIC']:.1f}")

    ax2.axvline(r_erg, color='orange', ls='--', lw=1.5, label=f"$r_{{erg}}={r_erg}M$")
    ax2.set_xscale('log'); ax2.set_yscale('log')
    ax2.set_xlabel(r"$r/M$", fontsize=12)
    ax2.set_ylabel(r"$W_{sr}$", fontsize=12)
    ax2.set_title(f"Kerr a={a}: $W_{{sr}}$ vs r (log-log)\n"
                  "Model S falls as $r^{{-3B}}$; Model E falls as $r^{{-1}}$", fontsize=11)
    ax2.legend(fontsize=9)
    ax2.grid(True, which='both', alpha=0.3)

    fig.suptitle(f"VYPOCET-15: Far-zone model discrimination (Kerr a={a})\n"
                 "Key: Model S slope >> Model E slope in log-log — far zone resolves ambiguity",
                 fontsize=12)
    fig.tight_layout()
    fig.savefig(os.path.join(PLOTDIR, figname), dpi=150)
    plt.close(fig)
    print(f"  Saved {figname}")


def plot_AW_farzone(records_near, records_far, r_erg, a=0.6, figname="AW_farzone_powerlaw.png"):
    """Plot |A_W| vs r and vs Omega in log-log with power-law fits."""
    fig, axes = plt.subplots(1, 2, figsize=(14, 6))

    # Combine all exterior records
    all_ext = []
    for rec in records_near:
        if rec.get("r", 0) > r_erg + 0.02 and abs(rec.get("A_W_mean", 0)) > 1e-4:
            all_ext.append({"r": rec["r"], "Omega": rec["Omega"],
                            "AW": abs(rec["A_W_mean"]), "AW_sd": rec.get("A_W_sd", 0.0),
                            "zone": "near"})
    for rec in records_far:
        if rec.get("r", 0) > r_erg + 0.02 and abs(rec.get("A_W_mean", 0)) > 1e-4:
            all_ext.append({"r": rec["r"], "Omega": rec["Omega"],
                            "AW": abs(rec["A_W_mean"]), "AW_sd": rec.get("A_W_sd", 0.0),
                            "zone": "far"})
    if len(all_ext) < 3:
        plt.close(fig)
        return

    r_near = np.array([d["r"] for d in all_ext if d["zone"] == "near"])
    AW_near = np.array([d["AW"] for d in all_ext if d["zone"] == "near"])
    AW_sd_near = np.array([d["AW_sd"] for d in all_ext if d["zone"] == "near"])
    r_far = np.array([d["r"] for d in all_ext if d["zone"] == "far"])
    AW_far = np.array([d["AW"] for d in all_ext if d["zone"] == "far"])
    AW_sd_far = np.array([d["AW_sd"] for d in all_ext if d["zone"] == "far"])
    Om_near = np.array([d["Omega"] for d in all_ext if d["zone"] == "near"])
    Om_far = np.array([d["Omega"] for d in all_ext if d["zone"] == "far"])

    r_all = np.array([d["r"] for d in all_ext])
    AW_all = np.array([d["AW"] for d in all_ext])
    AW_sd_all = np.array([d["AW_sd"] for d in all_ext])
    Om_all = np.array([d["Omega"] for d in all_ext])

    # Fit power laws
    fit_r = powerlaw_fit_loglog(r_all, AW_all, AW_sd_all, label="|A_W| vs r")
    fit_Om = powerlaw_fit_loglog(Om_all, AW_all, AW_sd_all, label="|A_W| vs Omega")

    ax = axes[0]
    if len(r_near) > 0:
        ax.errorbar(r_near, AW_near, yerr=AW_sd_near, fmt='o', color='crimson',
                    capsize=3, ms=6, label="Near zone (V14)")
    if len(r_far) > 0:
        ax.errorbar(r_far, AW_far, yerr=AW_sd_far, fmt='s', color='steelblue',
                    capsize=3, ms=6, label="Far zone (V15)")
    if fit_r:
        r_fine = np.logspace(np.log10(r_all.min()), np.log10(r_all.max()), 200)
        ax.loglog(r_fine, fit_r["A"] * r_fine**fit_r["B"], 'k-', lw=2,
                  label=f"Fit: $|A_W|\\propto r^{{{fit_r['B']:.2f}\\pm{fit_r['B_err']:.2f}}}$\n"
                        f"(toy model pred.: $r^{{-3}}$)")
    # Reference r^{-3}
    r_mid = np.exp(0.5*(np.log(r_all.min()) + np.log(r_all.max())))
    AW_mid = np.exp(np.interp(np.log(r_mid), np.log(np.sort(r_all)), np.log(AW_all[np.argsort(r_all)])))
    r_fine2 = np.logspace(np.log10(r_all.min()), np.log10(r_all.max()), 200)
    ax.loglog(r_fine2, AW_mid * (r_fine2 / r_mid)**(-3), 'g:', lw=1.5, alpha=0.7,
              label=r"reference $r^{-3}$ (toy model)")
    ax.set_xscale('log'); ax.set_yscale('log')
    ax.set_xlabel("r/M"); ax.set_ylabel(r"$|A_W|$")
    ax.set_title(r"$|A_W|$ vs r: power-law fit (toy predicts $r^{-3}$)")
    ax.legend(fontsize=9); ax.grid(True, which='both', alpha=0.3)

    ax2 = axes[1]
    if len(Om_near) > 0:
        ax2.errorbar(Om_near, AW_near, yerr=AW_sd_near, fmt='o', color='crimson',
                     capsize=3, ms=6, label="Near zone (V14)")
    if len(Om_far) > 0:
        ax2.errorbar(Om_far, AW_far, yerr=AW_sd_far, fmt='s', color='steelblue',
                     capsize=3, ms=6, label="Far zone (V15)")
    if fit_Om:
        Om_fine = np.logspace(np.log10(Om_all.min()), np.log10(Om_all.max()), 200)
        ax2.loglog(Om_fine, fit_Om["A"] * Om_fine**fit_Om["B"], 'k-', lw=2,
                   label=f"Fit: $|A_W|\\propto\\Omega^{{{fit_Om['B']:.2f}\\pm{fit_Om['B_err']:.2f}}}$\n"
                         f"(toy model pred.: $\\Omega^1$)")
    ax2.set_xscale('log'); ax2.set_yscale('log')
    ax2.set_xlabel(r"$\Omega(r)$"); ax2.set_ylabel(r"$|A_W|$")
    ax2.set_title(r"$|A_W|$ vs $\Omega$: power-law fit (toy predicts $\Omega^1$)")
    ax2.legend(fontsize=9); ax2.grid(True, which='both', alpha=0.3)

    fig.suptitle(f"VYPOCET-15: $|A_W|$ far-zone power law (Kerr a={a})\n"
                 "Toy model: $|A_W| \\sim \\Omega(r) \\sim r^{{-3}}$", fontsize=12)
    fig.tight_layout()
    fig.savefig(os.path.join(PLOTDIR, figname), dpi=150)
    plt.close(fig)
    print(f"  Saved {figname}")


def plot_farzone_summary(near_records, far_records, models_near_fit, models_far_fit,
                          models_joint, r_erg, a=0.6, figname="farzone_summary.png"):
    """4-panel summary plot for VYPOCET-15."""
    fig, axes = plt.subplots(2, 2, figsize=(14, 11))

    # Aggregate data
    def _extract(recs):
        r = np.array([x["r"] for x in recs])
        W = np.array([x["W_sr_mean"] for x in recs])
        Wsd = np.array([x.get("W_sr_sd", 0.0) for x in recs])
        AW = np.array([x["A_W_mean"] for x in recs])
        AWsd = np.array([x.get("A_W_sd", 0.0) for x in recs])
        Om = np.array([x["Omega"] for x in recs])
        return r, W, Wsd, AW, AWsd, Om

    nr, nW, nWsd, nAW, nAWsd, nOm = _extract(near_records)
    fr, fW, fWsd, fAW, fAWsd, fOm = _extract(far_records)

    # Panel 1: W_sr vs r (linear scale)
    ax = axes[0, 0]
    if len(nr) > 0:
        ax.errorbar(nr, nW, yerr=nWsd, fmt='o-', color='crimson', capsize=3,
                    ms=5, label="Near zone (V14)", lw=1.2)
    if len(fr) > 0:
        ax.errorbar(fr, fW, yerr=fWsd, fmt='s-', color='steelblue', capsize=3,
                    ms=5, label="Far zone (V15)", lw=1.2)
    ax.axvline(r_erg, color='orange', ls='--', lw=1.5, label=f"$r_{{erg}}={r_erg}M$")
    ax.set_xlabel("r/M"); ax.set_ylabel("$W_{sr}$")
    ax.set_title("$W_{sr}$ vs r (all zones, linear)")
    ax.legend(fontsize=9)

    # Panel 2: W_sr vs r (log-log) with fits
    ax2 = axes[0, 1]
    nr_pos = nr[nW > 0]; nW_pos = nW[nW > 0]; nWsd_pos = nWsd[nW > 0]
    fr_pos = fr[fW > 0]; fW_pos = fW[fW > 0]; fWsd_pos = fWsd[fW > 0]
    if len(nr_pos) > 0:
        ax2.errorbar(nr_pos, nW_pos, yerr=nWsd_pos, fmt='o', color='crimson',
                     capsize=3, ms=5, label="Near zone (V14)")
    if len(fr_pos) > 0:
        ax2.errorbar(fr_pos, fW_pos, yerr=fWsd_pos, fmt='s', color='steelblue',
                     capsize=3, ms=5, label="Far zone (V15)")
    # Joint model fits
    r_min = min(list(nr_pos) + list(fr_pos)) if len(nr_pos) + len(fr_pos) > 0 else r_erg + 0.1
    r_max = max(list(nr_pos) + list(fr_pos)) if len(nr_pos) + len(fr_pos) > 0 else 20.0
    r_fine = np.logspace(np.log10(max(r_min, r_erg + 0.1)), np.log10(r_max), 300)
    Om_fine = np.array([omega_kerr_analytic(1.0, a, rv) for rv in r_fine])
    if "comparison" in models_joint:
        if "error" not in models_joint.get("model_S", {}):
            p = models_joint["model_S"]["params"]
            ax2.loglog(r_fine, np.maximum(model_S_onset(Om_fine, p["A"], p["B"]), 1e-12),
                       'b-', lw=2, label=f"Model S (joint B={p['B']:.2f})")
        if "error" not in models_joint.get("model_E", {}):
            p = models_joint["model_E"]["params"]
            ax2.loglog(r_fine, np.maximum(model_E_onset(r_fine, r_erg, p["W_inf"], p["r_scale"]), 1e-12),
                       'r--', lw=2, label="Model E (joint)")
    ax2.axvline(r_erg, color='orange', ls='--', lw=1.5)
    ax2.set_xscale('log'); ax2.set_yscale('log')
    ax2.set_xlabel("r/M"); ax2.set_ylabel("$W_{sr}$")
    ax2.set_title("$W_{sr}$ vs r (log-log) + joint fits")
    ax2.legend(fontsize=9); ax2.grid(True, which='both', alpha=0.3)

    # Panel 3: A_W vs r
    ax3 = axes[1, 0]
    if len(nr) > 0:
        ax3.errorbar(nr, nAW, yerr=nAWsd, fmt='o-', color='crimson', capsize=3,
                     ms=5, label="Near zone (V14)", lw=1.2)
    if len(fr) > 0:
        ax3.errorbar(fr, fAW, yerr=fAWsd, fmt='s-', color='steelblue', capsize=3,
                     ms=5, label="Far zone (V15)", lw=1.2)
    ax3.axhline(0, color='gray', lw=0.8)
    ax3.axvline(r_erg, color='orange', ls='--', lw=1.5)
    ax3.set_xlabel("r/M"); ax3.set_ylabel("$A_W$")
    ax3.set_title("$A_W$ sign tracking (should remain negative)")
    ax3.legend(fontsize=9)

    # Panel 4: |A_W| vs Omega in log-log (near + far)
    ax4 = axes[1, 1]
    nAW_ext = np.abs(nAW[nr > r_erg + 0.02])
    nOm_ext = nOm[nr > r_erg + 0.02]
    fAW_ext = np.abs(fAW[fr > r_erg + 0.02])
    fOm_ext = fOm[fr > r_erg + 0.02]
    if len(nAW_ext[nAW_ext > 1e-4]) > 0:
        ax4.scatter(nOm_ext[nAW_ext > 1e-4], nAW_ext[nAW_ext > 1e-4],
                    c='crimson', marker='o', s=40, label="Near zone", zorder=3)
    if len(fAW_ext[fAW_ext > 1e-4]) > 0:
        ax4.scatter(fOm_ext[fAW_ext > 1e-4], fAW_ext[fAW_ext > 1e-4],
                    c='steelblue', marker='s', s=40, label="Far zone", zorder=3)
    # Reference slope 1 (toy prediction)
    all_Om_ext = np.concatenate([nOm_ext, fOm_ext])
    all_AW_ext = np.concatenate([nAW_ext, fAW_ext])
    mask_valid = all_AW_ext > 1e-4
    if mask_valid.sum() >= 2:
        Om_fit_arr = all_Om_ext[mask_valid]
        AW_fit_arr = all_AW_ext[mask_valid]
        Om_fine_aw = np.logspace(np.log10(Om_fit_arr.min()), np.log10(Om_fit_arr.max()), 100)
        # Fit slope in loglog
        lfit = powerlaw_fit_loglog(Om_fit_arr, AW_fit_arr, 0.1 * AW_fit_arr, "AW_vs_Om")
        if lfit:
            ax4.loglog(Om_fine_aw, lfit["A"] * Om_fine_aw**lfit["B"], 'k-', lw=2,
                       label=f"Fit: $\\Omega^{{{lfit['B']:.2f}}}$ (pred. $\\Omega^1$)")
    ax4.set_xscale('log'); ax4.set_yscale('log')
    ax4.set_xlabel(r"$\Omega(r)$"); ax4.set_ylabel(r"$|A_W|$")
    ax4.set_title(r"$|A_W|$ vs $\Omega$: toy model predicts $|A_W| \propto \Omega^1$")
    ax4.legend(fontsize=9); ax4.grid(True, which='both', alpha=0.3)

    fig.suptitle(f"VYPOCET-15: Far-zone scan summary — Kerr a={a}\n"
                 f"Joint fit ΔAIC(E-S)={models_joint.get('comparison', {}).get('delta_AIC_E_minus_S', 'N/A')}",
                 fontsize=12)
    fig.tight_layout()
    fig.savefig(os.path.join(PLOTDIR, figname), dpi=150)
    plt.close(fig)
    print(f"  Saved {figname}")


# ==========================================================================
# MAIN DRIVER
# ==========================================================================

def run():
    M = 1.0
    a = 0.6
    N = 1600
    T = Phi = 1.4
    seeds = [101, 202, 303, 404, 505]  # >=4, same as V14

    rp, rm, r_erg = kerr_surfaces(M, a)
    print(f"Kerr a={a}: r_+={rp:.4f}, r_-={rm:.4f}, r_erg={r_erg:.4f}")

    # Plane-wave grid (same as VYPOCET-14)
    KMAX = 35.0; NW = 71
    ws = np.linspace(-KMAX, KMAX, NW)
    ks = np.linspace(-KMAX, KMAX, NW)

    results = {
        "task": "VYPOCET-15 FAR-ZONE SCAN — MODEL E vs MODEL S DISAMBIGUATION",
        "conventions": {
            "lever": "2D massless => G_R=(1/2)C [1611.10281 eq.9]",
            "iDelta": "iDelta=i*(1/2)(C-C^T); SJ W=sum_{lam>0} lam v v^dagger",
            "Kerr_section": "h=[[-(1-2M/r),-2Ma/r],[-2Ma/r,r^2+a^2+2Ma^2/r]], r_erg=2M",
            "Omega": "Omega=-g_tphi/g_phiphi (ZAMO); Omega_Kerr=2Ma/(r^3+a^2*r+2Ma^2)",
            "W_sr": "W_sr=P(w*(w-k*Omega)<0) superradiant wedge weight",
            "A_W": "A_W=(mean_ReW_co - mean_ReW_cc)/(|..|+|..|), co/cc=dphi>0/<0",
            "Model_E": "W_sr=W_inf/(1+((r-r_erg)/r_scale)^2), onset at r_erg",
            "Model_S": "W_sr=A*Omega(r)^B, onset tracks Omega(r)",
            "params": {"M": M, "a": a, "N": N, "T": T, "Phi": Phi, "seeds": seeds,
                       "kmax": KMAX, "nw": NW},
            "inherited_from": ["VYPOCET-14 sj-threshold-scan", "VYPOCET-10", "VYPOCET-08"],
            "far_zone_physics": {
                "Model_S_prediction": "W_sr ~ Omega^B ~ r^{-3B}; for B~4 slope ~ r^{-12}",
                "Model_E_prediction": "W_sr ~ 1/(r-r_erg) ~ r^{-1} for r >> r_erg=2M",
                "log_log_slopes_differ_by": "factor ~ 12 in r-exponent => cleanly resolvable",
                "A_W_prediction": "|A_W| ~ shear ~ Omega ~ r^{-3} (toy model VYPOCET-10)",
            }
        }
    }

    # =========================================================================
    # FAR-ZONE RADIAL SCAN: r = 5M..20M, >=10 radii
    # =========================================================================
    print("\n=== FAR-ZONE SCAN: Kerr a=0.6, r=5..20M ===")
    # 12 radii logarithmically spaced from 5M to 20M + a few boundary points
    radii_far = sorted([
        5.0, 6.0, 7.0, 8.0, 9.0, 10.0, 12.0, 14.0, 16.0, 18.0, 20.0,
        # add 5.5 and 15.0 for density
        5.5, 15.0
    ])
    print(f"  Far-zone radii: {radii_far}")
    print(f"  Omega at these radii:")
    for rv in radii_far:
        Om = omega_kerr_analytic(M, a, rv)
        print(f"    r={rv:.1f}: Omega={Om:.7f}")

    far_records = radial_scan_farzone(radii_far, seeds, N, T, Phi, ws, ks, M=M, a=a)

    results["scan_far"] = {
        "a": a, "r_erg": r_erg, "r_range": [min(radii_far), max(radii_far)],
        "n_radii": len(radii_far), "seeds": seeds,
        "records": far_records,
    }

    # =========================================================================
    # LOAD VYPOCET-14 NEAR-ZONE DATA (Kerr a=0.6)
    # =========================================================================
    print("\n=== Loading VYPOCET-14 near-zone data ===")
    near_records_raw = load_v14_nearzone(V14_RESULTS, a_label="scan_kerr_a06",
                                          r_erg=r_erg, r_max_nearzone=5.0)
    # Normalize: add zone label, ensure fields
    near_records = []
    for rec in near_records_raw:
        near_records.append({
            "r": rec["r"],
            "Omega": rec["Omega"],
            "W_sr_mean": rec["W_sr_mean"],
            "W_sr_sd": rec.get("W_sr_sd", 0.0),
            "A_W_mean": rec["A_W_mean"],
            "A_W_sd": rec.get("A_W_sd", 0.0),
            "zone": "near",
            "source": "VYPOCET-14",
        })

    results["near_zone_v14"] = {
        "n_records": len(near_records),
        "r_values": [rec["r"] for rec in near_records],
        "source": "VYPOCET-14 results.json scan_kerr_a06",
    }

    # =========================================================================
    # MODEL FITS: FAR ZONE ONLY
    # =========================================================================
    print("\n=== Model fits: FAR ZONE ONLY ===")
    r_far = np.array([rec["r"] for rec in far_records])
    W_far = np.array([rec["W_sr_mean"] for rec in far_records])
    Wsd_far = np.array([rec["W_sr_sd"] for rec in far_records])
    Om_far = np.array([rec["Omega"] for rec in far_records])

    models_far = fit_aic_bic(r_far, W_far, Wsd_far, Om_far, r_erg, label="Far zone only")
    results["model_fits_far_only"] = models_far

    if "comparison" in models_far:
        c = models_far["comparison"]
        print(f"  Far zone: dAIC(E-S)={c['delta_AIC_E_minus_S']:+.2f}, "
              f"preferred={c['preferred_by_AIC']}, decisive={c['AIC_decisive']}")
    if "model_S" in models_far and "error" not in models_far["model_S"]:
        p = models_far["model_S"]["params"]
        print(f"  Model S far: A={p['A']:.4f}, B={p['B']:.4f}")
    if "model_E" in models_far and "error" not in models_far["model_E"]:
        p = models_far["model_E"]["params"]
        print(f"  Model E far: W_inf={p['W_inf']:.6f}, r_scale={p['r_scale']:.4f}")

    # Power-law fit in log-log for far zone W_sr
    Wsd_far_floor = np.maximum(Wsd_far, 1e-6)
    pw_far_Omega = powerlaw_fit_loglog(Om_far, W_far, Wsd_far_floor, label="W_sr vs Omega (far)")
    pw_far_r = powerlaw_fit_loglog(r_far, W_far, Wsd_far_floor, label="W_sr vs r (far)")
    results["powerlaw_fits_far"] = {
        "W_sr_vs_Omega": pw_far_Omega,
        "W_sr_vs_r": pw_far_r,
        "expected_slope_Omega_Model_S": "~ B (from VYPOCET-14 B~4.23 => slope~4.23)",
        "expected_slope_r_Model_S": "~ -3B (from Omega~r^{-3} => slope~-12.7)",
        "expected_slope_Omega_Model_E": "~ 1/3 (from W_E~1/r~Om^{1/3})",
        "expected_slope_r_Model_E": "~ -1 (from W_E~1/r for r>>r_erg)",
    }
    if pw_far_Omega:
        print(f"  PL fit (W_sr vs Omega, far): B={pw_far_Omega['B']:.3f}±{pw_far_Omega['B_err']:.3f}, "
              f"chi2/dof={pw_far_Omega['chi2_dof']:.3f}, R2={pw_far_Omega['R2_loglog']:.4f}")
    if pw_far_r:
        print(f"  PL fit (W_sr vs r, far):     slope={pw_far_r['B']:.3f}±{pw_far_r['B_err']:.3f}")

    # =========================================================================
    # MODEL FITS: JOINT (near + far)
    # =========================================================================
    print("\n=== Model fits: JOINT (near + far) ===")
    models_joint, all_joint_records = joint_fit(near_records, far_records, r_erg, M=M, a=a)
    results["model_fits_joint"] = models_joint

    if "comparison" in models_joint:
        c = models_joint["comparison"]
        print(f"  Joint: dAIC(E-S)={c['delta_AIC_E_minus_S']:+.2f}, "
              f"preferred={c['preferred_by_AIC']}, decisive={c['AIC_decisive']}, "
              f"strong={c['AIC_strong']}")
        print(f"  n_near={models_joint.get('n_near')}, n_far={models_joint.get('n_far')}, "
              f"n_total={models_joint.get('n_total')}")
    if "model_S" in models_joint and "error" not in models_joint["model_S"]:
        p = models_joint["model_S"]["params"]
        print(f"  Model S joint: A={p['A']:.6f}, B={p['B']:.4f}, "
              f"chi2/dof={models_joint['model_S']['chi2_dof']:.3f}")
    if "model_E" in models_joint and "error" not in models_joint["model_E"]:
        p = models_joint["model_E"]["params"]
        print(f"  Model E joint: W_inf={p['W_inf']:.6f}, r_scale={p['r_scale']:.4f}, "
              f"chi2/dof={models_joint['model_E']['chi2_dof']:.3f}")

    # Also fit near zone only for comparison
    print("\n=== Model fits: NEAR ZONE ONLY (from V14 data) ===")
    if len(near_records) >= 3:
        r_near = np.array([rec["r"] for rec in near_records])
        W_near = np.array([rec["W_sr_mean"] for rec in near_records])
        Wsd_near = np.array([max(rec["W_sr_sd"], 1e-7) for rec in near_records])
        Om_near = np.array([rec["Omega"] for rec in near_records])
        models_near = fit_aic_bic(r_near, W_near, Wsd_near, Om_near, r_erg, label="Near zone only")
        results["model_fits_near_only"] = models_near
        if "comparison" in models_near:
            c = models_near["comparison"]
            print(f"  Near zone only: dAIC(E-S)={c['delta_AIC_E_minus_S']:+.2f}, "
                  f"preferred={c['preferred_by_AIC']}")
    else:
        models_near = {}

    # =========================================================================
    # DISCRIMINANT ANALYSIS
    # =========================================================================
    print("\n=== Discriminant analysis ===")
    disc_far = discriminant_loglog(far_records, r_erg)
    disc_near = discriminant_loglog(near_records, r_erg)
    disc_joint = discriminant_loglog(all_joint_records, r_erg)
    results["discriminant"] = {
        "far_only": disc_far,
        "near_only": disc_near,
        "joint": disc_joint,
    }
    print(f"  Far only: corr_loglog(E)={disc_far.get('corr_loglog_E', 'N/A')}, "
          f"corr_loglog(S)={disc_far.get('corr_loglog_S', 'N/A')}, "
          f"preferred={disc_far.get('preferred_loglog', 'N/A')}")
    print(f"  Near only: corr_loglog(E)={disc_near.get('corr_loglog_E', 'N/A')}, "
          f"corr_loglog(S)={disc_near.get('corr_loglog_S', 'N/A')}, "
          f"preferred={disc_near.get('preferred_loglog', 'N/A')}")
    print(f"  Joint:     corr_loglog(E)={disc_joint.get('corr_loglog_E', 'N/A')}, "
          f"corr_loglog(S)={disc_joint.get('corr_loglog_S', 'N/A')}, "
          f"preferred={disc_joint.get('preferred_loglog', 'N/A')}")

    # =========================================================================
    # A_W POWER-LAW ANALYSIS
    # =========================================================================
    print("\n=== A_W power-law analysis ===")
    aw_pl = aw_powerlaw(far_records + near_records, r_erg, snr_threshold=3.0)
    results["AW_powerlaw"] = aw_pl
    if aw_pl.get("fit_r"):
        fr_fit = aw_pl["fit_r"]
        print(f"  |A_W| ~ r^gamma (all, n={fr_fit['n_points']}): gamma={fr_fit['B']:.3f}±{fr_fit['B_err']:.3f} "
              f"(pred: -3), R2={fr_fit['R2_loglog']:.4f}")
    if aw_pl.get("fit_Omega"):
        fOm_fit = aw_pl["fit_Omega"]
        print(f"  |A_W| ~ Omega^delta (all, n={fOm_fit['n_points']}): delta={fOm_fit['B']:.3f}±{fOm_fit['B_err']:.3f} "
              f"(pred: +1), R2={fOm_fit['R2_loglog']:.4f}")
    if aw_pl.get("fit_r_highSNR"):
        fhi = aw_pl["fit_r_highSNR"]
        print(f"  |A_W| ~ r^gamma (high-SNR, n={fhi['n_points']}): gamma={fhi['B']:.3f}±{fhi['B_err']:.3f}, R2={fhi['R2_loglog']:.4f}")
    if aw_pl.get("fit_Omega_highSNR"):
        fhi2 = aw_pl["fit_Omega_highSNR"]
        print(f"  |A_W| ~ Omega^delta (high-SNR, n={fhi2['n_points']}): delta={fhi2['B']:.3f}±{fhi2['B_err']:.3f}, R2={fhi2['R2_loglog']:.4f}")

    # =========================================================================
    # VERDICT
    # =========================================================================
    print("\n=== Computing verdict ===")

    # Determine if far-zone data is conclusive
    cmp_far = models_far.get("comparison", {})
    cmp_joint = models_joint.get("comparison", {})

    daic_far = cmp_far.get("delta_AIC_E_minus_S", 0.0)
    daic_joint = cmp_joint.get("delta_AIC_E_minus_S", 0.0)
    pref_far = cmp_far.get("preferred_by_AIC", "unknown")
    pref_joint = cmp_joint.get("preferred_by_AIC", "unknown")
    disc_far_loglog_pref = disc_far.get("preferred_loglog", "unknown")
    disc_joint_loglog_pref = disc_joint.get("preferred_loglog", "unknown")

    # Power-law slope check
    slope_S = pw_far_Omega["B"] if pw_far_Omega else None
    slope_r = pw_far_r["B"] if pw_far_r else None

    # v14 near-zone linear correlation was E-favorable (corr_E=0.971 vs corr_S=0.90)
    # This calculation resolves the ambiguity

    conclusive = (
        abs(daic_joint) > 6 and
        pref_joint == "Model_S" and
        disc_joint_loglog_pref == "Model_S"
    )

    verdict = {
        "VYPOCET_14_ambiguity": {
            "issue": ("For Kerr a=0.6, linear corr(W_sr, 1/(r-r_erg))=0.971 > "
                      "corr(W_sr, Omega)=0.900 in near zone (r=2..5M). "
                      "Models E and S are correlated there."),
            "resolution": "Far zone r=5..20M: Omega ~ r^{-3} while 1/(r-r_erg) ~ r^{-1} => "
                          "log-log slopes differ by factor ~12.",
        },
        "far_zone_AIC": {"delta_AIC_E_minus_S": daic_far, "preferred": pref_far,
                         "decisive": bool(abs(daic_far) > 6)},
        "joint_AIC": {"delta_AIC_E_minus_S": daic_joint, "preferred": pref_joint,
                      "decisive": bool(abs(daic_joint) > 6)},
        "loglog_discriminant_far": disc_far_loglog_pref,
        "loglog_discriminant_joint": disc_joint_loglog_pref,
        "powerlaw_slope_W_vs_Omega": slope_S,
        "powerlaw_slope_W_vs_r": slope_r,
        "expected_slope_S": {"vs_Omega": "~+B (~4.2)", "vs_r": "~-3B (~-12.7)"},
        "expected_slope_E": {"vs_Omega": "~+1/3", "vs_r": "~-1"},
        "CONCLUSIVE": conclusive,
        "CONCLUSION": (
            "Model S (W_sr ~ Omega^B) confirmed by far-zone data. "
            "The near-zone ambiguity (VYPOCET-14, Kerr a=0.6) is resolved: "
            "the log-log slope in the far zone matches Omega^B, NOT 1/(r-r_erg)."
        ) if conclusive else (
            "Far-zone data available but AIC/discriminant not decisive. "
            "Check W_sr values — if W_sr=0 for all far-zone radii, "
            "Model E also predicts zero (1/(r-r_erg)>0 but W_sr resolution limit). "
            "In that case the A_W power law provides the discriminator."
        ),
    }
    results["verdict"] = verdict
    print(f"\n  VERDICT: conclusive={conclusive}")
    print(f"  Far-zone ΔAIC(E-S)={daic_far:+.2f} => {pref_far}")
    print(f"  Joint    ΔAIC(E-S)={daic_joint:+.2f} => {pref_joint}")

    # =========================================================================
    # GENERATE PLOTS
    # =========================================================================
    print("\n=== Generating plots ===")

    plot_key_loglog_Wsr_vs_Omega(
        near_records, far_records, models_far, models_near, models_joint,
        r_erg, M=M, a=a, figname="key_loglog_Wsr_vs_Omega.png")

    plot_AW_farzone(near_records, far_records, r_erg, a=a, figname="AW_farzone_powerlaw.png")

    plot_farzone_summary(near_records, far_records, models_near, models_far, models_joint,
                          r_erg, a=a, figname="farzone_summary.png")

    # =========================================================================
    # SAVE RESULTS
    # =========================================================================
    outpath = os.path.join(OUTDIR, "results.json")
    with open(outpath, "w") as f:
        json.dump(results, f, indent=2)
    print(f"\nSaved results.json to {OUTDIR}")
    print(f"Saved plots to {PLOTDIR}")

    # =========================================================================
    # SUMMARY PRINT
    # =========================================================================
    print("\n" + "=" * 70)
    print("VYPOCET-15 SUMMARY")
    print("=" * 70)
    print(f"\nFar-zone radii: {len(radii_far)} (r={min(radii_far)}..{max(radii_far)}M)")
    n_nonzero_W = sum(1 for rec in far_records if rec["W_sr_mean"] > 0)
    print(f"Radii with W_sr > 0: {n_nonzero_W} / {len(radii_far)}")

    if pw_far_Omega:
        print(f"\nPower-law W_sr vs Omega (far): slope B = {pw_far_Omega['B']:.3f} "
              f"(Model S pred: ~{4.23:.2f}; Model E pred: ~{1/3:.2f})")
    if pw_far_r:
        print(f"Power-law W_sr vs r (far): slope = {pw_far_r['B']:.3f} "
              f"(Model S pred: ~{-3*4.23:.1f}; Model E pred: ~-1)")
    print(f"\nModel comparison (far only): ΔAIC={daic_far:+.2f} => {pref_far}")
    print(f"Model comparison (joint):    ΔAIC={daic_joint:+.2f} => {pref_joint}")
    print(f"\nCONCLUSIVE: {conclusive}")
    print(f"  {verdict['CONCLUSION']}")

    aw_far = [rec["A_W_mean"] for rec in far_records if abs(rec["A_W_mean"]) > 1e-4]
    if aw_far:
        all_neg = all(v < 0 for v in aw_far)
        print(f"\nA_W far zone: {len(aw_far)} non-zero values, all_negative={all_neg}")
        if aw_pl.get("fit_r_highSNR"):
            f_hi = aw_pl["fit_r_highSNR"]
            print(f"  |A_W| ~ r^{f_hi['B']:.3f}±{f_hi['B_err']:.3f} "
                  f"(toy pred: r^{{-3}}; high-SNR R2={f_hi['R2_loglog']:.3f}, n={f_hi['n_points']})")
        elif aw_pl.get("fit_r"):
            print(f"  |A_W| ~ r^{aw_pl['fit_r']['B']:.3f} "
                  f"(toy pred: r^{{-3}}; fit R2={aw_pl['fit_r']['R2_loglog']:.3f})")
        if aw_pl.get("fit_Omega_highSNR"):
            f_hi2 = aw_pl["fit_Omega_highSNR"]
            print(f"  |A_W| ~ Omega^{f_hi2['B']:.3f}±{f_hi2['B_err']:.3f} "
                  f"(toy pred: Omega^1; high-SNR R2={f_hi2['R2_loglog']:.3f}, n={f_hi2['n_points']})")
    else:
        print(f"\nA_W: {sum(1 for rec in far_records if abs(rec['A_W_mean']) > 1e-4)} "
              f"non-zero in far zone")

    return results


if __name__ == "__main__":
    run()
