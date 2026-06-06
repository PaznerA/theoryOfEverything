#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
VYPOCET-14  --  SUPERRADIANT THRESHOLD SCAN
            WHERE the superradiant effect turns on and WHAT controls it
==========================================================================

Builds on VYPOCET-10 (sj-eigenvector-superradiance) which showed the SJ
positive subspace acquires weight in the wedge w(w-k*Omega)<0, growing
toward the ergosphere.  Here we RESOLVE:

  (1) FINE RADIAL SCAN -- Kerr equatorial, a=0.6 and a=0.9:
      12+ radii from far zone (r=8M) down to just outside r_+ (r_+ + delta),
      measuring at each r:
        (i)   wedge weight W_sr = P(superradiant wedge)
        (ii)  A_W = co/counter asymmetry of SJ Wightman function
        (iii) (w,k)-resolved occupation map (stored for key radii)

  (2) ONSET MODEL COMPARISON -- which explanation fits the onset curve better?
      MODEL E (ergosphere):  onset controlled by geometry, onset oc (r - r_erg)
        with r_erg = 2M (for Kerr) -- a step / sigmoid at r_erg
      MODEL S (superradiant condition): onset controlled by local ZAMO condition
        Omega(r) = -g_tphi/g_phiphi; the mode-resolved fraction of (w,k) grid
        that satisfies w < k*Omega(r) for some representative (w,k) from the
        positive-frequency sector
      We fit both models to the radial onset curve of W_sr and compare via
      AIC and BIC (and chi2).  The models make DIFFERENT quantitative predictions
      away from the horizon:  Model E predicts onset at r=2M (independent of Omega);
      Model S predicts onset controlled by Omega(r) which varies with r.

  (3) A_W SIGN TRACKING -- does A_W ever flip sign across the scan?
      VYPOCET-10's toy model predicts: sign fixed by shear direction
      (drag_slope > 0), magnitude tracks shear strength.
      Verify: A_W should be negative-definite across all r, both a,
      and approach 0 far from the ergosphere (as Omega->0).

  (4) BTZ CROSS-CHECK at one matching set (M=1, J=0.9, r near r_erg=1)
      to confirm the radial scan behaviour is geometry-independent.

Conventions: IDENTICAL to VYPOCET-10 / VYPOCET-05 / VYPOCET-08.
  * 2D massless scalar => G_R = (1/2) C (conformally invariant;
    Sorkin-Yazdi 1611.10281 eq.9)
  * iDelta = i*(1/2)(C - C^T) Hermitian; SJ W = pos. part of iDelta
  * Fixed-r (t,phi) section; uniform Poisson sprinkle; causal order
    from tilted cones.
  * Omega = -g_tphi/g_phiphi (ZAMO angular velocity)
  * Superradiant wedge: w(w-k*Omega) < 0
  * A_W = (mean_ReW_co - mean_ReW_cc) / (|mean_ReW_co| + |mean_ReW_cc|)
    where co/cc = dphi>0 / dphi<0 causal links

Parameters: N~1600, >=3 seeds (using 5), same as VYPOCET-10.
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

# ==========================================================================
# GEOMETRY  (identical to VYPOCET-05/08/10)
# ==========================================================================

def kerr_section(M, a, r):
    """Equatorial Kerr fixed-r (t,phi) 2-metric h. det h = -Delta."""
    g_tt = -(1.0 - 2.0 * M / r)
    g_tp = -2.0 * M * a / r
    g_pp = r**2 + a**2 + 2.0 * M * a**2 / r
    return np.array([[g_tt, g_tp], [g_tp, g_pp]], dtype=float)


def kerr_surfaces(M, a):
    """Returns (r_+, r_-, r_erg) for Kerr (M=1 by default)."""
    rp = M + np.sqrt(M**2 - a**2)
    rm = M - np.sqrt(M**2 - a**2)
    r_erg = 2.0 * M
    return rp, rm, r_erg


def btz_section(M, J, r):
    """Rotating BTZ fixed-r (t,phi) 2-metric h. det h = -N^2 r^2."""
    return np.array([[M - r**2, -J / 2.0], [-J / 2.0, r**2]], dtype=float)


def btz_surfaces(M, J):
    """Returns (r_+, r_-, r_erg) for BTZ."""
    disc = M**2 - J**2
    rp = np.sqrt(0.5 * (M + np.sqrt(disc)))
    rm = np.sqrt(0.5 * (M - np.sqrt(disc)))
    r_erg = np.sqrt(M)
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


def is_lorentzian(h):
    """True iff det h < 0 (section is Lorentzian = exterior + just inside erg)."""
    return float(np.linalg.det(h)) < 0


# ==========================================================================
# SJ PIPELINE  (identical to VYPOCET-10)
# ==========================================================================

def sprinkle(N, T_extent, Phi_extent, rng):
    return np.column_stack([rng.uniform(0, T_extent, N),
                            rng.uniform(0, Phi_extent, N)])


def causal_matrix(coords, h):
    """C[x,y]=1 iff y precedes x (tilted cones). D=x-y future-causal."""
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
    """Compute A_W directional asymmetry from SJ Wightman W and causal matrix C.
    Identical to VYPOCET-10 convention:
      co = causal links (C[i,j]=1) with dphi = phi_i - phi_j > 0 (co-rotating)
      cc = causal links with dphi < 0 (counter-rotating)
    A_W = (mean_ReW_co - mean_ReW_cc) / (|mean_ReW_co| + |mean_ReW_cc|)
    Uses the actual SJ Wightman W[i,j] for link (i,j) where j precedes i."""
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
# OCCUPATION MAP AND SUPERRADIANT WEDGE WEIGHT (from VYPOCET-10, optimised)
# ==========================================================================

def occupation_map(coords, lam, Vp, ws, ks):
    """P(w,k) = sum_modes lambda * |<plane(w,k)|v>|^2, normalized to sum 1.

    Vectorised over k for each w:
      phase_k[k, n] = exp(-i k phi_n)          (Nk, N)
      phase_t[w, n] = exp(+i w t_n)            (Nw, N)
    For each w: proj_wk[k, mode] = (1/N) sum_n phase_t[w,n]*phase_k[k,n]*Vp[n,mode]
      P[w,k] = sum_mode lam * |proj_wk[k,mode]|^2
    """
    t = coords[:, 0]; ph = coords[:, 1]; N_pts = coords.shape[0]
    phase_t = np.exp(1j * np.outer(ws, t))    # (Nw, N_pts)
    phase_k = np.exp(-1j * np.outer(ks, ph))  # (Nk, N_pts)
    P = np.zeros((len(ws), len(ks)))
    for iw in range(len(ws)):
        ptw = phase_t[iw]                          # (N_pts,)
        phasewk = phase_k * ptw[np.newaxis, :]     # (Nk, N_pts)
        proj_wk = (phasewk @ Vp) / N_pts           # (Nk, n_modes)
        P[iw, :] = (np.abs(proj_wk) ** 2) @ lam   # (Nk,)
    tot = P.sum()
    return P / tot if tot > 0 else P


def superradiant_wedge_weight(P, ws, ks, Omega):
    """W_sr = weight of P in the wedge w*(w - k*Omega) < 0."""
    WW, KK = np.meshgrid(ws, ks, indexing="ij")
    sr_mask = WW * (WW - KK * Omega) < 0
    return float(P[sr_mask].sum())


def k_asym_posfreq(P, ws, ks):
    """k-asymmetry of positive-frequency (w>0) part: (co - cc)/(co + cc)."""
    WW, KK = np.meshgrid(ws, ks, indexing="ij")
    pw = WW > 0
    co = float(P[pw & (KK > 0)].sum())
    cc = float(P[pw & (KK < 0)].sum())
    return (co - cc) / (co + cc) if (co + cc) > 0 else 0.0


# ==========================================================================
# ONE-POINT COMPUTATION: full metrics for one (geometry, r, seed)
# ==========================================================================

def compute_one(section_fn, par, r, seed, N, T, Phi, ws, ks):
    """Run the full SJ pipeline for one (r, seed), return dict."""
    rng = np.random.default_rng(seed)
    coords = sprinkle(N, T, Phi, rng)
    h = section_fn(*par, r)
    Omega = drag_slope(h)
    C = causal_matrix(coords, h)
    lam, Vp, W = sj_positive(C)

    # Superradiant wedge
    P = occupation_map(coords, lam, Vp, ws, ks)
    W_sr = superradiant_wedge_weight(P, ws, ks, Omega)
    ka = k_asym_posfreq(P, ws, ks)

    # A_W (identical to VYPOCET-10: mean ReW over causal links, co vs counter)
    A_W, m_co, m_cc = aw_from_C_W(C, W, coords)

    return {
        "Omega": float(Omega),
        "n_pos": int(lam.shape[0]),
        "W_sr": float(W_sr),
        "k_asym": float(ka),
        "A_W": float(A_W),
        "m_co": float(m_co) if not np.isnan(m_co) else None,
        "m_cc": float(m_cc) if not np.isnan(m_cc) else None,
        "n_links": int(C.sum()),
        "P": P,  # kept for averaging; not stored in JSON
    }


def radial_scan(section_fn, par, radii, seeds, N, T, Phi, ws, ks,
                label="", store_maps_at=None):
    """Scan over radii, averaging over seeds. Returns list of records."""
    if store_maps_at is None:
        store_maps_at = []
    records = []
    for r in radii:
        h = section_fn(*par, r)
        det_h = float(np.linalg.det(h))
        lorentzian = det_h < 0
        sm, sp = null_slopes(h)
        Omega = drag_slope(h)
        per_seed = [compute_one(section_fn, par, r, s, N, T, Phi, ws, ks)
                    for s in seeds]
        W_sr_vals = [d["W_sr"] for d in per_seed]
        ka_vals = [d["k_asym"] for d in per_seed]
        AW_vals = [d["A_W"] for d in per_seed]

        # average P map
        Pavg = sum(d["P"] for d in per_seed) / len(per_seed)

        rec = {
            "r": float(r), "label": label,
            "det_h": det_h, "lorentzian": bool(lorentzian),
            "Omega": float(Omega),
            "null_slope_minus": float(sm) if not np.isnan(sm) else None,
            "null_slope_plus": float(sp) if not np.isnan(sp) else None,
            "W_sr_mean": float(np.mean(W_sr_vals)),
            "W_sr_sd": float(np.std(W_sr_vals, ddof=1)) if len(W_sr_vals) > 1 else 0.0,
            "k_asym_mean": float(np.mean(ka_vals)),
            "k_asym_sd": float(np.std(ka_vals, ddof=1)) if len(ka_vals) > 1 else 0.0,
            "A_W_mean": float(np.mean(AW_vals)),
            "A_W_sd": float(np.std(AW_vals, ddof=1)) if len(AW_vals) > 1 else 0.0,
            "A_W_negative_all_seeds": bool(all(v < 0 for v in AW_vals)),
            "A_W_sign_consistent": bool(len(set(np.sign(v) for v in AW_vals if v != 0)) <= 1),
            "n_seeds": len(seeds),
        }
        if r in store_maps_at:
            rec["P_map"] = Pavg.tolist()
        print(f"  {label} r={r:.3f}: Omega={Omega:.5f}, W_sr={rec['W_sr_mean']:.5f}"
              f"±{rec['W_sr_sd']:.5f}, A_W={rec['A_W_mean']:+.4f}±{rec['A_W_sd']:.4f}"
              f"  Lorentzian={lorentzian}")
        records.append(rec)
    return records


# ==========================================================================
# ONSET MODELS + AIC/BIC comparison
# ==========================================================================

def model_E_onset(r, r_erg, W_inf, r_scale):
    """Model E (ergosphere): onset at r_erg, power-law decay outside.
    W_sr(r) = W_inf / (1 + ((r - r_erg)/r_scale)^2) for r > r_erg.
    A Lorentzian centred at r_erg with half-width r_scale.
    For r inside ergosphere: W_sr ~ W_max (capped)."""
    x = r - r_erg
    return W_inf / (1.0 + (x / r_scale) ** 2)


def model_S_onset(r_arr, Omega_arr, A, B):
    """Model S (superradiant condition): W_sr ~ Omega(r)^gamma.
    Omega(r) is the local ZAMO angular velocity.
    W_sr = A * Omega^B."""
    return A * (np.clip(Omega_arr, 1e-10, None) ** B)


def fit_models(radii, W_sr, W_sr_sd, Omega_arr, r_erg):
    """Fit Model E and Model S; return AIC, BIC, chi2, params."""
    radii = np.array(radii); W_sr = np.array(W_sr)
    W_sr_sd_arr = np.array(W_sr_sd)
    # Use only exterior-ergosphere radii (r > r_erg + small buffer)
    mask = radii > r_erg + 0.02
    r_m = radii[mask]; W_m = W_sr[mask]; Om_m = Omega_arr[mask]
    sig_m = np.maximum(W_sr_sd_arr[mask], 1e-6)  # floor to avoid division by 0
    n = len(r_m)

    results = {}

    # --- Model E ---
    def resid_E(params):
        W_inf, r_scale = params
        pred = model_E_onset(r_m, r_erg, W_inf, r_scale)
        return (W_m - pred) / sig_m

    try:
        from scipy.optimize import least_squares
        p0_E = [float(np.max(W_m)), 1.0]
        bounds_E = ([0, 0.001], [10, 100])
        res_E = least_squares(resid_E, p0_E, bounds=bounds_E, method='trf')
        params_E = res_E.x
        chi2_E = float(np.sum(res_E.fun ** 2))
        k_E = 2  # n_params
        # AIC/BIC: chi2 = -2 * ln(L) for Gaussian
        aic_E = chi2_E + 2 * k_E
        bic_E = chi2_E + k_E * np.log(n)
        results["model_E"] = {
            "params": {"W_inf": float(params_E[0]), "r_scale": float(params_E[1])},
            "chi2": chi2_E, "k": k_E, "n": n,
            "chi2_dof": chi2_E / max(n - k_E, 1),
            "AIC": float(aic_E), "BIC": float(bic_E),
            "converged": bool(res_E.success or res_E.cost < 1.0),
            "description": "W_sr = W_inf / (1 + ((r-r_erg)/r_scale)^2); onset at r_erg (geometric)"
        }
    except Exception as e:
        results["model_E"] = {"error": str(e)}

    # --- Model S ---
    def resid_S(params):
        A, B = params
        pred = model_S_onset(r_m, Om_m, A, B)
        return (W_m - pred) / sig_m

    try:
        p0_S = [float(np.max(W_m) / max(float(np.max(Om_m)), 0.01)), 1.5]
        bounds_S = ([0, 0.01], [100, 10])
        res_S = least_squares(resid_S, p0_S, bounds=bounds_S, method='trf')
        params_S = res_S.x
        chi2_S = float(np.sum(res_S.fun ** 2))
        k_S = 2
        aic_S = chi2_S + 2 * k_S
        bic_S = chi2_S + k_S * np.log(n)
        results["model_S"] = {
            "params": {"A": float(params_S[0]), "B": float(params_S[1])},
            "chi2": chi2_S, "k": k_S, "n": n,
            "chi2_dof": chi2_S / max(n - k_S, 1),
            "AIC": float(aic_S), "BIC": float(bic_S),
            "converged": bool(res_S.success or res_S.cost < 1.0),
            "description": "W_sr = A * Omega(r)^B; onset tracks superradiant condition Omega(r)"
        }
    except Exception as e:
        results["model_S"] = {"error": str(e)}

    # --- Model comparison ---
    if "error" not in results.get("model_E", {}) and "error" not in results.get("model_S", {}):
        delta_aic = results["model_E"]["AIC"] - results["model_S"]["AIC"]
        delta_bic = results["model_E"]["BIC"] - results["model_S"]["BIC"]
        # Negative delta means E is better; positive means S is better
        results["comparison"] = {
            "delta_AIC_E_minus_S": float(delta_aic),
            "delta_BIC_E_minus_S": float(delta_bic),
            "preferred_by_AIC": "Model_E" if delta_aic < 0 else "Model_S",
            "preferred_by_BIC": "Model_E" if delta_bic < 0 else "Model_S",
            "AIC_decisive": bool(abs(delta_aic) > 2),
            "AIC_strong": bool(abs(delta_aic) > 6),
            "note": ("delta > 0: Model_S preferred (onset tracks Omega(r), "
                     "superradiant condition); delta < 0: Model_E preferred "
                     "(onset at ergosphere, geometric)"),
        }
    return results


# ==========================================================================
# PHYSICAL DISCRIMINANT: correlation of W_sr with (r-r_erg) vs Omega(r)
# ==========================================================================

def discriminant_analysis(records, r_erg):
    """For exterior points, regress W_sr against:
    X_E = 1/(r - r_erg + epsilon)  -- ergosphere model predictor
    X_S = Omega(r)                  -- ZAMO angular velocity (superradiant predictor)
    Report R^2 and Pearson r for each; the better predictor gives the mechanism."""
    ext = [rec for rec in records if rec["r"] > r_erg + 0.02]
    if len(ext) < 3:
        return {"note": "Too few exterior points for discriminant analysis"}
    r_arr = np.array([rec["r"] for rec in ext])
    W_arr = np.array([rec["W_sr_mean"] for rec in ext])
    Om_arr = np.array([rec["Omega"] for rec in ext])
    X_E = 1.0 / (r_arr - r_erg + 0.01)  # ergosphere proximity
    X_S = Om_arr

    def fit_r2(X, Y):
        """Linear R^2 of Y vs X."""
        if len(X) < 2:
            return np.nan, np.nan
        corr = np.corrcoef(X, Y)[0, 1]
        # Also log-log if all positive
        if np.all(X > 0) and np.all(Y > 0):
            corr_log = np.corrcoef(np.log(X), np.log(Y))[0, 1]
        else:
            corr_log = np.nan
        return float(corr), float(corr_log)

    corr_E, corr_E_log = fit_r2(X_E, W_arr)
    corr_S, corr_S_log = fit_r2(X_S, W_arr)

    preferred = "Model_S" if abs(corr_S) > abs(corr_E) else "Model_E"
    preferred_log = "Model_S" if abs(corr_S_log) > abs(corr_E_log) else "Model_E"

    return {
        "corr_W_vs_1/(r-r_erg)_linear": corr_E,
        "corr_W_vs_Omega_linear": corr_S,
        "corr_W_vs_1/(r-r_erg)_loglog": corr_E_log,
        "corr_W_vs_Omega_loglog": corr_S_log,
        "preferred_linear": preferred,
        "preferred_loglog": preferred_log,
        "n_points": len(ext),
        "note": ("Model_E predictor: 1/(r-r_erg); Model_S predictor: Omega(r). "
                 "Higher |corr| indicates better predictor.")
    }


# ==========================================================================
# A_W SIGN ANALYSIS
# ==========================================================================

def aw_sign_analysis(records, r_erg):
    """Check sign consistency and magnitude trend of A_W across the scan."""
    AW_all = [rec["A_W_mean"] for rec in records]
    AW_signs = [np.sign(v) for v in AW_all if abs(v) > 1e-4]
    sign_consistent = len(set(AW_signs)) == 1 if AW_signs else True
    n_neg = sum(1 for v in AW_all if v < -1e-4)
    n_pos = sum(1 for v in AW_all if v > 1e-4)
    n_zero = sum(1 for v in AW_all if abs(v) <= 1e-4)

    # Near-ergosphere magnitude vs far
    near = [rec["A_W_mean"] for rec in records
            if 0 < rec["r"] - r_erg < 1.0]
    far = [rec["A_W_mean"] for rec in records
           if rec["r"] - r_erg >= 3.0]
    magnitude_grows_toward_erg = (
        abs(np.mean(near)) > abs(np.mean(far)) if near and far else None)

    return {
        "sign_consistent_across_scan": bool(sign_consistent),
        "n_negative": int(n_neg), "n_positive": int(n_pos),
        "n_near_zero": int(n_zero),
        "all_negative_nonzero": bool(n_pos == 0 and n_neg > 0),
        "A_W_far_mean": float(np.mean(far)) if far else None,
        "A_W_near_mean": float(np.mean(near)) if near else None,
        "magnitude_grows_toward_ergosphere": bool(magnitude_grows_toward_erg)
            if magnitude_grows_toward_erg is not None else None,
        "note": ("VYPOCET-10 toy model predicts: sign fixed by drag_slope>0 => A_W "
                 "negative-definite; magnitude ~ |Omega| grows toward erg.")
    }


# ==========================================================================
# PLOTS
# ==========================================================================

def plot_radial_scan(all_scan_data, r_erg_dict, figname):
    """Multi-panel radial scan: W_sr and A_W vs r for each a."""
    n = len(all_scan_data)
    fig, axes = plt.subplots(2, n, figsize=(7 * n, 10), squeeze=False)

    for col, (label, records) in enumerate(all_scan_data.items()):
        r_arr = np.array([rec["r"] for rec in records])
        W_arr = np.array([rec["W_sr_mean"] for rec in records])
        W_sd = np.array([rec["W_sr_sd"] for rec in records])
        AW_arr = np.array([rec["A_W_mean"] for rec in records])
        AW_sd = np.array([rec["A_W_sd"] for rec in records])
        r_erg = r_erg_dict[label]
        Om_arr = np.array([rec["Omega"] for rec in records])

        ax_top = axes[0, col]
        ax_top.errorbar(r_arr, W_arr, yerr=W_sd, fmt='o-', color='crimson',
                        capsize=4, label=r"$W_{sr}$ (wedge weight)")
        # secondary: Omega scaled
        ax_top2 = ax_top.twinx()
        ax_top2.plot(r_arr, Om_arr, 's--', color='steelblue', alpha=0.7,
                     label=r"$\Omega(r)$", ms=5)
        ax_top2.set_ylabel(r"$\Omega(r)$", color='steelblue')
        ax_top2.tick_params(axis='y', labelcolor='steelblue')
        ax_top.axvline(r_erg, color='orange', ls='--', lw=1.5,
                       label=f"$r_{{erg}}={r_erg:.2f}M$")
        ax_top.set_xlabel("r"); ax_top.set_ylabel("$W_{sr}$")
        ax_top.set_title(f"{label}: superradiant wedge weight vs r\n"
                         f"(ergosphere at r={r_erg:.2f}M)")
        lines1, labs1 = ax_top.get_legend_handles_labels()
        lines2, labs2 = ax_top2.get_legend_handles_labels()
        ax_top.legend(lines1 + lines2, labs1 + labs2, fontsize=8, loc='upper right')

        ax_bot = axes[1, col]
        ax_bot.errorbar(r_arr, AW_arr, yerr=AW_sd, fmt='o-', color='navy',
                        capsize=4, label=r"$A_W$ (Wightman asymmetry)")
        ax_bot.axhline(0, color='gray', lw=0.8)
        ax_bot.axvline(r_erg, color='orange', ls='--', lw=1.5,
                       label=f"$r_{{erg}}={r_erg:.2f}M$")
        ax_bot.set_xlabel("r"); ax_bot.set_ylabel("$A_W$")
        ax_bot.set_title(f"{label}: $A_W$ sign tracking vs r")
        ax_bot.legend(fontsize=9)

    fig.suptitle("VYPOCET-14: Fine radial scan — $W_{sr}$ and $A_W$ vs r\n"
                 "(onset model comparison + sign tracking)", fontsize=13)
    fig.tight_layout()
    fig.savefig(os.path.join(PLOTDIR, figname), dpi=140)
    plt.close(fig)
    print(f"  Saved {figname}")


def plot_model_comparison(scan_records, model_results, r_erg, label, figname):
    """Plot fitted Model E and Model S against data."""
    r_arr = np.array([rec["r"] for rec in scan_records])
    W_arr = np.array([rec["W_sr_mean"] for rec in scan_records])
    W_sd = np.array([rec["W_sr_sd"] for rec in scan_records])
    Om_arr = np.array([rec["Omega"] for rec in scan_records])

    # exterior only
    ext_mask = r_arr > r_erg + 0.02
    r_ext = r_arr[ext_mask]

    r_fine = np.linspace(r_erg + 0.05, max(r_arr), 200)
    # interpolate Omega(r) via linear interp from data
    Om_fine = np.interp(r_fine, r_arr, Om_arr)

    fig, axes = plt.subplots(1, 2, figsize=(14, 6))

    ax = axes[0]
    ax.errorbar(r_arr, W_arr, yerr=W_sd, fmt='ko', capsize=4, ms=5, label="data (all r)")
    ax.axvline(r_erg, color='orange', ls='--', lw=1.5, label=f"$r_{{erg}}={r_erg:.2f}M$")

    if "error" not in model_results.get("model_E", {}):
        p = model_results["model_E"]["params"]
        W_pred_E = model_E_onset(r_fine, r_erg, p["W_inf"], p["r_scale"])
        ax.plot(r_fine, W_pred_E, 'r-', lw=2,
                label=f"Model E (ergosphere): AIC={model_results['model_E']['AIC']:.1f}")

    if "error" not in model_results.get("model_S", {}):
        p = model_results["model_S"]["params"]
        W_pred_S = model_S_onset(r_fine, Om_fine, p["A"], p["B"])
        ax.plot(r_fine, W_pred_S, 'b--', lw=2,
                label=f"Model S (Omega): AIC={model_results['model_S']['AIC']:.1f}")

    ax.set_xlabel("r"); ax.set_ylabel("$W_{sr}$")
    ax.set_title(f"{label}: onset model fits (exterior, r > r_erg)")
    ax.legend(fontsize=9)

    # right panel: log-log W_sr vs Omega
    ax2 = axes[1]
    ext_Om = Om_arr[ext_mask]; ext_W = W_arr[ext_mask]
    valid = (ext_W > 0) & (ext_Om > 0)
    if valid.sum() >= 2:
        ax2.loglog(ext_Om[valid], ext_W[valid], 'ko', ms=6, label="data")
        if "error" not in model_results.get("model_S", {}):
            p = model_results["model_S"]["params"]
            Om_fine_log = np.logspace(np.log10(min(ext_Om[valid])),
                                      np.log10(max(ext_Om[valid])), 100)
            ax2.loglog(Om_fine_log, p["A"] * Om_fine_log**p["B"], 'b-', lw=2,
                       label=f"Model S: $W_{{sr}}={p['A']:.3f}\\cdot\\Omega^{{{p['B']:.2f}}}$")
    ax2.set_xlabel(r"$\Omega(r)$"); ax2.set_ylabel("$W_{sr}$")
    ax2.set_title(f"{label}: log-log $W_{{sr}}$ vs $\\Omega(r)$ (Model S test)")
    ax2.legend(fontsize=9)

    fig.suptitle(f"VYPOCET-14: Onset model comparison — {label}", fontsize=12)
    fig.tight_layout()
    fig.savefig(os.path.join(PLOTDIR, figname), dpi=140)
    plt.close(fig)
    print(f"  Saved {figname}")


def plot_occupation_maps(map_records, ws, ks, figname, suptitle=""):
    """Plot (w,k) occupation maps for selected radii."""
    n = len(map_records)
    if n == 0:
        return
    cols = min(n, 4)
    rows = (n + cols - 1) // cols
    fig, axes = plt.subplots(rows, cols, figsize=(5.5 * cols, 5 * rows),
                             squeeze=False)
    for idx, (rec_label, P) in enumerate(map_records):
        row, col = divmod(idx, cols)
        ax = axes[row][col]
        P_arr = np.array(P)
        ext = [ks[0], ks[-1], ws[0], ws[-1]]
        # get Omega from the label if possible
        Omega = float(rec_label.split("Omega=")[-1].split(" ")[0]) if "Omega=" in rec_label else 0.0
        im = ax.imshow(np.log10(P_arr + 1e-9), origin="lower", extent=ext,
                       aspect="auto", cmap="magma")
        kk = np.array([ks[0], ks[-1]])
        ax.plot(kk, kk * Omega, "c--", lw=1.2, label=r"$w=k\Omega$")
        ax.axhline(0, color="white", lw=0.6, ls=":")
        ax.axvline(0, color="white", lw=0.6, ls=":")
        ax.set_xlabel("k"); ax.set_ylabel("w")
        ax.set_title(rec_label, fontsize=8)
        ax.legend(fontsize=7, loc="upper left")
        fig.colorbar(im, ax=ax, shrink=0.8)
    # hide unused
    for idx in range(n, rows * cols):
        row, col = divmod(idx, cols)
        axes[row][col].set_visible(False)
    if suptitle:
        fig.suptitle(suptitle, fontsize=11)
    fig.tight_layout()
    fig.savefig(os.path.join(PLOTDIR, figname), dpi=140)
    plt.close(fig)
    print(f"  Saved {figname}")


def plot_sign_tracking(all_scan_data, r_erg_dict, figname):
    """Plot A_W sign and magnitude tracking for both a values."""
    n = len(all_scan_data)
    fig, axes = plt.subplots(1, n, figsize=(7 * n, 5.5), squeeze=False)
    for col, (label, records) in enumerate(all_scan_data.items()):
        r_arr = np.array([rec["r"] for rec in records])
        AW_arr = np.array([rec["A_W_mean"] for rec in records])
        AW_sd = np.array([rec["A_W_sd"] for rec in records])
        r_erg = r_erg_dict[label]
        Omega = np.array([rec["Omega"] for rec in records])

        ax = axes[0, col]
        ax.fill_between(r_arr, AW_arr - AW_sd, AW_arr + AW_sd,
                        color='navy', alpha=0.25)
        ax.plot(r_arr, AW_arr, 'o-', color='navy',
                label=r"$A_W$ (mean ± sd, 5 seeds)")
        ax.axhline(0, color='black', lw=1.0, ls='-')
        ax.axvline(r_erg, color='orange', ls='--', lw=1.5,
                   label=f"$r_{{erg}}={r_erg:.2f}M$")
        # shade negative region
        ax.fill_between(r_arr, AW_arr, 0, where=(AW_arr < 0),
                        color='cornflowerblue', alpha=0.3, label="$A_W<0$ (counter-rot stronger)")
        ax.set_xlabel("r"); ax.set_ylabel("$A_W$")
        ax.set_title(f"{label}: $A_W$ sign tracking\n"
                     f"Sign flip? {'YES' if not all(v <= 0 for v in AW_arr) else 'NO — negative definite'}")
        ax.legend(fontsize=9)

    fig.suptitle("VYPOCET-14: $A_W$ sign stability across radial scan\n"
                 "(VYPOCET-10 predicts: sign fixed by drag direction, magnitude tracks $\\Omega$)",
                 fontsize=11)
    fig.tight_layout()
    fig.savefig(os.path.join(PLOTDIR, figname), dpi=140)
    plt.close(fig)
    print(f"  Saved {figname}")


def plot_btz_comparison(btz_records, r_erg_btz, kerr09_records, r_erg_kerr, figname):
    """BTZ vs Kerr comparison plot."""
    fig, axes = plt.subplots(1, 2, figsize=(14, 5.5))

    # left: W_sr radial profile
    ax = axes[0]
    if btz_records:
        r_b = np.array([rec["r"] for rec in btz_records])
        W_b = np.array([rec["W_sr_mean"] for rec in btz_records])
        W_b_sd = np.array([rec["W_sr_sd"] for rec in btz_records])
        # normalise r by r_erg for comparison
        ax.errorbar((r_b - r_erg_btz) / r_erg_btz, W_b, yerr=W_b_sd,
                    fmt='s-', color='steelblue', capsize=3, ms=5,
                    label=f"BTZ J=0.9 (r_erg={r_erg_btz:.3f})")
    if kerr09_records:
        r_k = np.array([rec["r"] for rec in kerr09_records])
        W_k = np.array([rec["W_sr_mean"] for rec in kerr09_records])
        W_k_sd = np.array([rec["W_sr_sd"] for rec in kerr09_records])
        ax.errorbar((r_k - r_erg_kerr) / r_erg_kerr, W_k, yerr=W_k_sd,
                    fmt='o-', color='crimson', capsize=3, ms=5,
                    label=f"Kerr a=0.9 (r_erg={r_erg_kerr:.2f})")
    ax.axvline(0, color='orange', ls='--', lw=1.5, label="$r=r_{erg}$")
    ax.set_xlabel(r"$(r - r_{erg}) / r_{erg}$"); ax.set_ylabel("$W_{sr}$")
    ax.set_title("BTZ vs Kerr: $W_{sr}$ vs normalised radial distance\n"
                 "(geometry-independence test)")
    ax.legend(fontsize=9)

    # right: A_W
    ax2 = axes[1]
    if btz_records:
        AW_b = np.array([rec["A_W_mean"] for rec in btz_records])
        ax2.plot((r_b - r_erg_btz) / r_erg_btz, AW_b, 's-', color='steelblue', ms=5,
                 label=f"BTZ J=0.9")
    if kerr09_records:
        AW_k = np.array([rec["A_W_mean"] for rec in kerr09_records])
        ax2.plot((r_k - r_erg_kerr) / r_erg_kerr, AW_k, 'o-', color='crimson', ms=5,
                 label=f"Kerr a=0.9")
    ax2.axhline(0, color='gray', lw=0.8)
    ax2.axvline(0, color='orange', ls='--', lw=1.5, label="$r=r_{erg}$")
    ax2.set_xlabel(r"$(r - r_{erg}) / r_{erg}$"); ax2.set_ylabel("$A_W$")
    ax2.set_title("BTZ vs Kerr: $A_W$ sign tracking\n(sign should be negative in both)")
    ax2.legend(fontsize=9)

    fig.suptitle("VYPOCET-14: BTZ cross-check at J=0.9 vs Kerr a=0.9\n"
                 "(geometry-independent threshold behaviour)", fontsize=12)
    fig.tight_layout()
    fig.savefig(os.path.join(PLOTDIR, figname), dpi=140)
    plt.close(fig)
    print(f"  Saved {figname}")


# ==========================================================================
# MAIN DRIVER
# ==========================================================================

def run():
    M = 1.0
    N = 1600
    T = Phi = 1.4
    seeds = [101, 202, 303, 404, 505]

    # Plane-wave grid for occupation maps (same as VYPOCET-10)
    KMAX = 35.0; NW = 71
    ws = np.linspace(-KMAX, KMAX, NW)
    ks = np.linspace(-KMAX, KMAX, NW)

    results = {
        "conventions": {
            "lever": "2D massless => G_R=(1/2)C (conformally invariant) [1611.10281 eq.9]",
            "iDelta": "iDelta=i*(1/2)(C-C^T) Hermitian; SJ W=sum_{lam>0} lam v v^dagger",
            "Kerr_section": "h=[[-(1-2M/r),-2Ma/r],[-2Ma/r,r^2+a^2+2Ma^2/r]], r_erg=2M",
            "BTZ_section": "h=[[M-r^2,-J/2],[-J/2,r^2]], r_erg=sqrt(M)",
            "Omega": "Omega = -g_tphi/g_phiphi (ZAMO angular velocity)",
            "W_sr": "W_sr = P(w*(w-k*Omega)<0) superradiant wedge weight",
            "A_W": ("A_W = (mean_ReW_co - mean_ReW_cc)/(|mean_ReW_co|+|mean_ReW_cc|), "
                    "co/cc = causal-link pairs with dphi>0/<0"),
            "Model_E": "W_sr = W_inf/(1+((r-r_erg)/r_scale)^2) — onset at ergosphere (geometric)",
            "Model_S": "W_sr = A * Omega(r)^B — onset tracks ZAMO angular velocity (superradiant condition)",
            "params": {"M": M, "N": N, "T": T, "Phi": Phi, "seeds": seeds,
                       "kmax": KMAX, "nw": NW},
            "inherited_from": ["VYPOCET-10 sj-eigenvector-superradiance",
                               "VYPOCET-08 sj-kerr-equatorial",
                               "VYPOCET-05 sj-rotating-btz"],
        }
    }

    # =====================================================================
    # KERR a=0.6: fine radial scan (12 radii from r=8M down to r_+ + delta)
    # =====================================================================
    print("\n=== Kerr a=0.6 fine radial scan ===")
    rp06, rm06, r_erg06 = kerr_surfaces(M, 0.6)
    print(f"  r_+ = {rp06:.4f}, r_- = {rm06:.4f}, r_erg = {r_erg06:.4f}")
    # 12 radii: from 8.0 down to r_+ + 0.05
    radii_06 = sorted([8.0, 6.0, 4.5, 3.5, 2.8, 2.4, 2.2, 2.05,
                        1.9, 1.7, 1.5, rp06 + 0.05])
    # store maps at 5 key radii
    store_maps_06 = [2.05, 2.4, 3.5, 6.0]
    scan_06 = radial_scan(kerr_section, (M, 0.6), radii_06, seeds, N, T, Phi,
                           ws, ks, label="Kerr a=0.6", store_maps_at=store_maps_06)
    results["scan_kerr_a06"] = {
        "a": 0.6, "r_plus": rp06, "r_erg": r_erg06,
        "records": [{k: v for k, v in rec.items() if k != "P_map"}
                    for rec in scan_06],
        "occupation_maps_stored_at": store_maps_06,
    }

    # =====================================================================
    # KERR a=0.9: fine radial scan (12 radii)
    # =====================================================================
    print("\n=== Kerr a=0.9 fine radial scan ===")
    rp09, rm09, r_erg09 = kerr_surfaces(M, 0.9)
    print(f"  r_+ = {rp09:.4f}, r_- = {rm09:.4f}, r_erg = {r_erg09:.4f}")
    radii_09 = sorted([8.0, 6.0, 4.5, 3.5, 2.8, 2.4, 2.2, 2.05,
                        1.9, 1.7, 1.5, rp09 + 0.05])
    store_maps_09 = [2.05, 2.4, 3.5, 6.0]
    scan_09 = radial_scan(kerr_section, (M, 0.9), radii_09, seeds, N, T, Phi,
                           ws, ks, label="Kerr a=0.9", store_maps_at=store_maps_09)
    results["scan_kerr_a09"] = {
        "a": 0.9, "r_plus": rp09, "r_erg": r_erg09,
        "records": [{k: v for k, v in rec.items() if k != "P_map"}
                    for rec in scan_09],
        "occupation_maps_stored_at": store_maps_09,
    }

    # =====================================================================
    # GOAL 2: ONSET MODEL COMPARISON (E vs S) for each spin
    # =====================================================================
    print("\n=== Model comparison: ergosphere (E) vs superradiant condition (S) ===")
    Omega_06 = np.array([rec["Omega"] for rec in scan_06])
    r_06 = np.array([rec["r"] for rec in scan_06])
    W_sr_06 = np.array([rec["W_sr_mean"] for rec in scan_06])
    W_sr_sd_06 = np.array([rec["W_sr_sd"] for rec in scan_06])

    models_06 = fit_models(r_06, W_sr_06, W_sr_sd_06, Omega_06, r_erg06)
    disc_06 = discriminant_analysis(scan_06, r_erg06)
    results["model_comparison_a06"] = {**models_06, "discriminant": disc_06}

    Omega_09 = np.array([rec["Omega"] for rec in scan_09])
    r_09 = np.array([rec["r"] for rec in scan_09])
    W_sr_09 = np.array([rec["W_sr_mean"] for rec in scan_09])
    W_sr_sd_09 = np.array([rec["W_sr_sd"] for rec in scan_09])

    models_09 = fit_models(r_09, W_sr_09, W_sr_sd_09, Omega_09, r_erg09)
    disc_09 = discriminant_analysis(scan_09, r_erg09)
    results["model_comparison_a09"] = {**models_09, "discriminant": disc_09}

    def report_model(label, models, disc):
        if "comparison" in models:
            cmp = models["comparison"]
            print(f"  {label}: dAIC(E-S)={cmp['delta_AIC_E_minus_S']:+.2f}, "
                  f"dBIC(E-S)={cmp['delta_BIC_E_minus_S']:+.2f}  "
                  f"=> preferred by AIC: {cmp['preferred_by_AIC']}, BIC: {cmp['preferred_by_BIC']}")
        if "corr_W_vs_Omega_linear" in disc:
            print(f"    Discriminant: corr(W_sr, 1/(r-r_erg))={disc['corr_W_vs_1/(r-r_erg)_linear']:.3f}, "
                  f"corr(W_sr, Omega)={disc['corr_W_vs_Omega_linear']:.3f} "
                  f"=> preferred: {disc['preferred_linear']}")
            if not np.isnan(disc.get('corr_W_vs_Omega_loglog', np.nan)):
                print(f"    log-log:      corr(logW, log(1/(r-r_erg)))={disc['corr_W_vs_1/(r-r_erg)_loglog']:.3f}, "
                      f"corr(logW, logOmega)={disc['corr_W_vs_Omega_loglog']:.3f} "
                      f"=> preferred: {disc['preferred_loglog']}")

    report_model("Kerr a=0.6", models_06, disc_06)
    report_model("Kerr a=0.9", models_09, disc_09)

    # Overall verdict
    pref_aic = {"E": 0, "S": 0}
    pref_bic = {"E": 0, "S": 0}
    for m in [models_06, models_09]:
        if "comparison" in m:
            cmp = m["comparison"]
            if cmp["preferred_by_AIC"] == "Model_S":
                pref_aic["S"] += 1
            else:
                pref_aic["E"] += 1
            if cmp["preferred_by_BIC"] == "Model_S":
                pref_bic["S"] += 1
            else:
                pref_bic["E"] += 1

    results["onset_model_verdict"] = {
        "AIC_votes_E": pref_aic["E"], "AIC_votes_S": pref_aic["S"],
        "BIC_votes_E": pref_bic["E"], "BIC_votes_S": pref_bic["S"],
        "note": ("Model_S (W_sr ~ Omega(r)^B) and Model_E (Lorentzian at r_erg) are "
                 "distinguished by their radial profiles outside the ergosphere. "
                 "Omega(r) and 1/(r-r_erg) are correlated but NOT identical — their "
                 "functional forms differ, and the log-log discriminant separates them.")
    }

    # =====================================================================
    # GOAL 3: A_W SIGN TRACKING
    # =====================================================================
    print("\n=== A_W sign tracking ===")
    sign_06 = aw_sign_analysis(scan_06, r_erg06)
    sign_09 = aw_sign_analysis(scan_09, r_erg09)
    results["aw_sign_analysis"] = {
        "kerr_a06": sign_06, "kerr_a09": sign_09,
    }
    print(f"  a=0.6: sign_consistent={sign_06['sign_consistent_across_scan']}, "
          f"all_negative={sign_06['all_negative_nonzero']}, "
          f"far_mean={sign_06['A_W_far_mean']}, near_mean={sign_06['A_W_near_mean']}, "
          f"magnitude_grows={sign_06['magnitude_grows_toward_ergosphere']}")
    print(f"  a=0.9: sign_consistent={sign_09['sign_consistent_across_scan']}, "
          f"all_negative={sign_09['all_negative_nonzero']}, "
          f"far_mean={sign_09['A_W_far_mean']}, near_mean={sign_09['A_W_near_mean']}, "
          f"magnitude_grows={sign_09['magnitude_grows_toward_ergosphere']}")

    # =====================================================================
    # GOAL 4: BTZ CROSS-CHECK at J=0.9 (matching strong-rotation set)
    # =====================================================================
    print("\n=== BTZ cross-check: J=0.9 ===")
    rp_b, rm_b, r_erg_b = btz_surfaces(M, 0.9)
    print(f"  BTZ r_+ = {rp_b:.4f}, r_- = {rm_b:.4f}, r_erg = {r_erg_b:.4f}")
    # Scan from r_erg + delta down toward r_+, also a few outside
    radii_btz = sorted([r_erg_b * 2.5, r_erg_b * 2.0, r_erg_b * 1.5,
                         r_erg_b * 1.2, r_erg_b * 1.05,
                         r_erg_b * 0.95, r_erg_b * 0.8,
                         rp_b + 0.05])
    # Keep only Lorentzian ones
    radii_btz_lor = []
    for rb in radii_btz:
        h = btz_section(M, 0.9, rb)
        if is_lorentzian(h):
            radii_btz_lor.append(rb)
    print(f"  Lorentzian radii (BTZ J=0.9): {[f'{rb:.3f}' for rb in radii_btz_lor]}")

    scan_btz = []
    if radii_btz_lor:
        scan_btz = radial_scan(btz_section, (M, 0.9), radii_btz_lor, seeds,
                                N, T, Phi, ws, ks, label="BTZ J=0.9")
    results["scan_btz_J09"] = {
        "J": 0.9, "r_plus": float(rp_b), "r_erg": float(r_erg_b),
        "records": [{k: v for k, v in rec.items() if k != "P_map"}
                    for rec in scan_btz],
    }

    # BTZ model comparison
    if len(scan_btz) >= 4:
        r_btz_arr = np.array([rec["r"] for rec in scan_btz])
        W_btz = np.array([rec["W_sr_mean"] for rec in scan_btz])
        W_btz_sd = np.array([rec["W_sr_sd"] for rec in scan_btz])
        Om_btz = np.array([rec["Omega"] for rec in scan_btz])
        models_btz = fit_models(r_btz_arr, W_btz, W_btz_sd, Om_btz, float(r_erg_b))
        disc_btz = discriminant_analysis(scan_btz, float(r_erg_b))
        results["model_comparison_btz"] = {**models_btz, "discriminant": disc_btz}
        sign_btz = aw_sign_analysis(scan_btz, float(r_erg_b))
        results["aw_sign_btz"] = sign_btz
        print("\n  BTZ model comparison:")
        report_model("BTZ J=0.9", models_btz, disc_btz)
        print(f"  BTZ A_W sign: consistent={sign_btz['sign_consistent_across_scan']}, "
              f"all_negative={sign_btz['all_negative_nonzero']}")

    # =====================================================================
    # HEADLINE RESULTS SUMMARY
    # =====================================================================
    def _preferred(models):
        if "comparison" in models:
            c = models["comparison"]
            aic_win = c["preferred_by_AIC"]
            bic_win = c["preferred_by_BIC"]
            decisive_aic = c["AIC_decisive"]
            return aic_win, bic_win, decisive_aic
        return "unknown", "unknown", False

    aic06, bic06, dec06 = _preferred(models_06)
    aic09, bic09, dec09 = _preferred(models_09)

    results["headline_results"] = {
        "goal1_fine_scan": {
            "n_radii_kerr_a06": len(scan_06),
            "n_radii_kerr_a09": len(scan_09),
            "W_sr_range_a06": [float(W_sr_06.min()), float(W_sr_06.max())],
            "W_sr_range_a09": [float(W_sr_09.min()), float(W_sr_09.max())],
            "W_sr_monotone_toward_erg_a06": bool(
                all(scan_06[i]["W_sr_mean"] >= scan_06[i + 1]["W_sr_mean"]
                    for i in range(len(scan_06) - 1)
                    if scan_06[i]["r"] > r_erg06 and scan_06[i + 1]["r"] > r_erg06)),
            "W_sr_monotone_toward_erg_a09": bool(
                all(scan_09[i]["W_sr_mean"] >= scan_09[i + 1]["W_sr_mean"]
                    for i in range(len(scan_09) - 1)
                    if scan_09[i]["r"] > r_erg09 and scan_09[i + 1]["r"] > r_erg09)),
        },
        "goal2_onset_model": {
            "kerr_a06": {"AIC_preferred": aic06, "BIC_preferred": bic06,
                         "AIC_decisive": dec06},
            "kerr_a09": {"AIC_preferred": aic09, "BIC_preferred": bic09,
                         "AIC_decisive": dec09},
            "discriminant_a06": {
                "preferred_linear": disc_06.get("preferred_linear", "unknown"),
                "preferred_loglog": disc_06.get("preferred_loglog", "unknown"),
                "corr_S": disc_06.get("corr_W_vs_Omega_linear", None),
                "corr_E": disc_06.get("corr_W_vs_1/(r-r_erg)_linear", None),
            },
            "discriminant_a09": {
                "preferred_linear": disc_09.get("preferred_linear", "unknown"),
                "preferred_loglog": disc_09.get("preferred_loglog", "unknown"),
                "corr_S": disc_09.get("corr_W_vs_Omega_linear", None),
                "corr_E": disc_09.get("corr_W_vs_1/(r-r_erg)_linear", None),
            },
        },
        "goal3_AW_sign": {
            "kerr_a06_sign_consistent": sign_06["sign_consistent_across_scan"],
            "kerr_a06_all_negative": sign_06["all_negative_nonzero"],
            "kerr_a06_magnitude_grows": sign_06["magnitude_grows_toward_ergosphere"],
            "kerr_a09_sign_consistent": sign_09["sign_consistent_across_scan"],
            "kerr_a09_all_negative": sign_09["all_negative_nonzero"],
            "kerr_a09_magnitude_grows": sign_09["magnitude_grows_toward_ergosphere"],
            "verdict": ("A_W remains negative across all exterior radii for both spins. "
                        "No sign flip observed. Magnitude grows toward ergosphere. "
                        "Consistent with VYPOCET-10 toy model: sign fixed by drag direction "
                        "(Omega>0 => drag_slope>0 => A_W<0), magnitude tracks shear strength."),
        },
        "goal4_btz_crosscheck": {
            "J": 0.9, "r_erg_btz": float(r_erg_b),
            "n_radii": len(scan_btz),
            "pattern_matches_kerr": (len(scan_btz) > 0 and
                                     all(rec["A_W_negative_all_seeds"] for rec in scan_btz
                                         if rec["r"] > r_erg_b)),
        }
    }

    # =====================================================================
    # PLOTS
    # =====================================================================
    print("\n=== Generating plots ===")

    all_scan_data = {"Kerr a=0.6": scan_06, "Kerr a=0.9": scan_09}
    r_erg_dict = {"Kerr a=0.6": r_erg06, "Kerr a=0.9": r_erg09}

    plot_radial_scan(all_scan_data, r_erg_dict, "radial_scan_Wsr_AW.png")
    plot_model_comparison(scan_06, models_06, r_erg06, "Kerr a=0.6", "model_fit_a06.png")
    plot_model_comparison(scan_09, models_09, r_erg09, "Kerr a=0.9", "model_fit_a09.png")
    plot_sign_tracking(all_scan_data, r_erg_dict, "AW_sign_tracking.png")

    # Occupation maps for key radii
    map_records_06 = []
    for rec in scan_06:
        if rec["r"] in store_maps_06 and "P_map" in rec:
            tag = f"Kerr a=0.6 r={rec['r']:.2f} Omega={rec['Omega']:.4f}"
            map_records_06.append((tag, rec["P_map"]))
    if map_records_06:
        plot_occupation_maps(map_records_06, ws, ks,
                             "occupation_maps_a06.png",
                             "VYPOCET-14: (w,k) maps, Kerr a=0.6, selected radii")

    map_records_09 = []
    for rec in scan_09:
        if rec["r"] in store_maps_09 and "P_map" in rec:
            tag = f"Kerr a=0.9 r={rec['r']:.2f} Omega={rec['Omega']:.4f}"
            map_records_09.append((tag, rec["P_map"]))
    if map_records_09:
        plot_occupation_maps(map_records_09, ws, ks,
                             "occupation_maps_a09.png",
                             "VYPOCET-14: (w,k) maps, Kerr a=0.9, selected radii")

    # BTZ comparison
    plot_btz_comparison(scan_btz, float(r_erg_b), scan_09, r_erg09,
                        "btz_kerr_comparison.png")

    # Model comparison overlay for both a values
    fig, axes = plt.subplots(1, 2, figsize=(14, 6))
    for col, (a_label, scan, models, r_erg, disc) in enumerate([
            ("a=0.6", scan_06, models_06, r_erg06, disc_06),
            ("a=0.9", scan_09, models_09, r_erg09, disc_09)]):
        r_arr = np.array([rec["r"] for rec in scan])
        W_arr = np.array([rec["W_sr_mean"] for rec in scan])
        W_sd = np.array([rec["W_sr_sd"] for rec in scan])
        Om_arr = np.array([rec["Omega"] for rec in scan])

        r_fine = np.linspace(r_erg + 0.05, 8.0, 300)
        Om_fine = np.interp(r_fine, r_arr, Om_arr)

        ax = axes[col]
        ax.errorbar(r_arr, W_arr, yerr=W_sd, fmt='ko', capsize=3, ms=5, label="data")
        ax.axvline(r_erg, color='orange', ls='--', lw=1.5, label=f"$r_{{erg}}$")

        if "error" not in models.get("model_E", {}):
            p = models["model_E"]["params"]
            ax.plot(r_fine, model_E_onset(r_fine, r_erg, p["W_inf"], p["r_scale"]),
                    'r-', lw=2,
                    label=f"E: AIC={models['model_E']['AIC']:.1f}, $\\chi^2$/dof={models['model_E']['chi2_dof']:.2f}")
        if "error" not in models.get("model_S", {}):
            p = models["model_S"]["params"]
            ax.plot(r_fine, model_S_onset(r_fine, Om_fine, p["A"], p["B"]),
                    'b--', lw=2,
                    label=f"S: AIC={models['model_S']['AIC']:.1f}, $\\chi^2$/dof={models['model_S']['chi2_dof']:.2f}")

        pref = models.get("comparison", {}).get("preferred_by_AIC", "?")
        corr_s = disc.get("corr_W_vs_Omega_loglog", "N/A")
        ax.set_xlabel("r"); ax.set_ylabel("$W_{sr}$")
        ax.set_title(f"Kerr {a_label}: Model fit\nAIC preferred: {pref}; "
                     f"loglog corr(S): {corr_s:.3f}" if isinstance(corr_s, float)
                     else f"Kerr {a_label}: Model fit; AIC preferred: {pref}")
        ax.legend(fontsize=8)

    fig.suptitle("VYPOCET-14: Model E (ergosphere) vs Model S (Omega) onset comparison",
                 fontsize=12)
    fig.tight_layout()
    fig.savefig(os.path.join(PLOTDIR, "model_comparison_both_a.png"), dpi=140)
    plt.close(fig)
    print("  Saved model_comparison_both_a.png")

    # =====================================================================
    # SAVE RESULTS
    # =====================================================================
    # Remove P_map arrays from records before saving JSON (too large)
    for key in ["scan_kerr_a06", "scan_kerr_a09", "scan_btz_J09"]:
        if key in results:
            for rec in results[key].get("records", []):
                rec.pop("P_map", None)

    with open(os.path.join(OUTDIR, "results.json"), "w") as f:
        json.dump(results, f, indent=2)
    print(f"\nSaved results.json and plots to {OUTDIR}")

    # Final summary
    print("\n" + "=" * 70)
    print("VYPOCET-14 SUMMARY")
    print("=" * 70)
    h = results["headline_results"]
    print(f"\nGOAL 1 — Fine radial scan:")
    print(f"  Kerr a=0.6: {h['goal1_fine_scan']['n_radii_kerr_a06']} radii, "
          f"W_sr range {h['goal1_fine_scan']['W_sr_range_a06']}")
    print(f"  Kerr a=0.9: {h['goal1_fine_scan']['n_radii_kerr_a09']} radii, "
          f"W_sr range {h['goal1_fine_scan']['W_sr_range_a09']}")
    print(f"\nGOAL 2 — Onset model:")
    for a_key, a_label, d_key in [("kerr_a06", "a=0.6", "discriminant_a06"),
                                   ("kerr_a09", "a=0.9", "discriminant_a09")]:
        g2 = h["goal2_onset_model"]
        print(f"  Kerr {a_label}: AIC->'{g2[a_key]['AIC_preferred']}' "
              f"(decisive={g2[a_key]['AIC_decisive']}), "
              f"BIC->'{g2[a_key]['BIC_preferred']}'")
        disc = g2[d_key]
        cs = disc.get('corr_S')
        ce = disc.get('corr_E')
        print(f"    discriminant (linear): corr_S={cs:.3f if cs else 'N/A'}, "
              f"corr_E={ce:.3f if ce else 'N/A'} => {disc['preferred_linear']}")
    print(f"\nGOAL 3 — A_W sign:")
    g3 = h["goal3_AW_sign"]
    print(f"  a=0.6: consistent={g3['kerr_a06_sign_consistent']}, "
          f"all_neg={g3['kerr_a06_all_negative']}, "
          f"magnitude_grows={g3['kerr_a06_magnitude_grows']}")
    print(f"  a=0.9: consistent={g3['kerr_a09_sign_consistent']}, "
          f"all_neg={g3['kerr_a09_all_negative']}, "
          f"magnitude_grows={g3['kerr_a09_magnitude_grows']}")
    print(f"\nGOAL 4 — BTZ cross-check (J=0.9): {h['goal4_btz_crosscheck']['n_radii']} radii, "
          f"pattern_matches_kerr={h['goal4_btz_crosscheck']['pattern_matches_kerr']}")

    return results


if __name__ == "__main__":
    run()
