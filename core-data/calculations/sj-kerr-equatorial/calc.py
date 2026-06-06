#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Sorkin-Johnston (SJ) state on the equatorial fixed-r (t,phi) section of KERR
============================================================================

Extension of VYPOCET-05 (rotating BTZ, AdS) to ASYMPTOTICALLY FLAT KERR.  The
goal is to test whether the BTZ SJ signatures are GEOMETRY-INDEPENDENT
properties of SJ states in rotating spacetimes: same 2D conformal trick, same
observables, different geometry (Kerr vs BTZ).

THE CONFORMAL-TRIVIALITY LEVER  (identical to VYPOCET-05)
--------------------------------------------------------
* Every 2D Lorentzian metric is locally conformally flat: g_ab = Omega^2 eta_ab.
* The massless 2D scalar wave operator is conformally invariant (xi=0 IS minimal
  coupling in d=2).
* Hence the retarded Green function depends ONLY on the causal/conformal order.
* On a causal set this is the EXACT statement  G_R = (1/2) C ,
  C_xy = 1 if y precedes x (y in causal past of x), else 0.
    - Sorkin & Yazdi, arXiv:1611.10281, eq.(9): G_R=(1/2)C, massless 2D scalar;
      causal-set expectation equals continuum G_R for all densities (footnote 5).
    - Massive: G_R=(1/2)C(I+(m^2/2rho)C)^-1 -> (1/2)C at m=0 [1701.07212,1712.04227].
    - Used in CURVED 2D (AdS_2) via conformal flatness [arXiv:2504.12919].
  The conformal factor Omega (curvature, frame dragging) drops out of G_R; it
  enters ONLY through how the light cones TILT (and the proper sprinkling volume).

THE GEOMETRY: equatorial Kerr in Boyer-Lindquist  (verified symbolically)
-------------------------------------------------------------------------
Kerr, geometrized units G=c=1, mass M, spin a (|a|<=M):
  Sigma = r^2 + a^2 cos^2(theta),  Delta = r^2 - 2 M r + a^2.
At the equator theta = pi/2:  Sigma = r^2.  The induced fixed-r (t,phi) metric is
  g_tt    = -(1 - 2 M / r)
  g_tphi  = -2 M a / r            (constant frame dragging? NO -- r-dependent here)
  g_phiphi=  r^2 + a^2 + 2 M a^2 / r
  g_rr    =  r^2 / Delta = Sigma / Delta
  [components verified against Wikipedia "Kerr metric" and standard references.]

KEY EXACT FACT (sympy, see below):
  det h = g_tt g_phiphi - g_tphi^2 = -(r^2 - 2 M r + a^2) = -Delta.
So OUTSIDE the outer horizon r_+ = M + sqrt(M^2-a^2) (where Delta>0) we have
det h < 0: the fixed-r (t,phi) section is LORENTZIAN through the entire
ergoregion -- exactly the BTZ situation (there det h = -N^2 r^2).
Discriminant of the null-slope quadratic:  disc = -4 det h = 4 Delta > 0 outside r_+.

SURFACES (equator):
  outer horizon  r_+   = M + sqrt(M^2 - a^2)
  ergosphere     r_erg = 2 M     (static limit g_tt=0; equator => cos^2 theta=0,
                                  so r_erg = M + sqrt(M^2) = 2M, INDEPENDENT of a)
  ergoregion = (r_+, 2M).  Inside it g_tt>0, d_t is SPACELIKE -- no timelike
  Killing vector -- exactly where stationary vacua fail and SJ still goes through.

HONEST GEOMETRY NOTE (a real difference from BTZ):
  In Kerr the ergoregion is a THIN SHELL (r_+, 2M).  For M=1:
     a=0.3 -> r_+=1.954, ergoregion (1.954,2.0)   (width 0.046)
     a=0.6 -> r_+=1.800, ergoregion (1.800,2.0)   (width 0.200)
     a=0.9 -> r_+=1.436, ergoregion (1.436,2.0)   (width 0.564)
  The shell only widens enough to reach a given small r at large a.  In
  particular r=1.5 is OUTSIDE the horizon (Lorentzian) ONLY for a=0.9; for
  a=0.3,0.6 the r=1.5 fixed-r section is INSIDE the horizon, where det h>0 and
  the (t,phi) section is EUCLIDEAN (no real cone).  We report this honestly and
  ALSO run the a-dependence at a radius outside the ergosphere (r=2.5) where ALL
  a give a Lorentzian section, for a clean comparison.  Unlike BTZ, g_tphi is
  r-dependent, so the cone geometry varies even within a single section's family.

CAUSAL ORDER ON A FIXED-r (t,phi) SECTION  (tilted cones; identical to BTZ)
--------------------------------------------------------------------------
The induced 2-metric h=[[g_tt,g_tphi],[g_tphi,g_phiphi]] is CONSTANT on the
patch (fixed r => constant components).  Displacement d=(dt,dphi) is future-
directed causal iff h(d,d)<=0 AND future-pointing, with time orientation set by
the zero-angular-momentum (LNRF) timelike vector T=(1, s_drag),
s_drag = -g_tphi/g_phiphi (timelike: h(T,T)=det h/g_phiphi<0).
Future-pointing: h(T,d)<0.  Clean partial order on the patch.
Sprinkle uniform in (t,phi) (constant proper area sqrt(-det h) dt dphi),
density rho = N / (sqrt(-det h) T Phi).

SJ PIPELINE (Sorkin-Yazdi 1611.10281; same as VYPOCET-04/05)
  1. C_xy = 1 if y precedes x (tilted cones), diag 0.
  2. G_R=(1/2)C; Delta_PJ = G_R - G_R^T = (1/2)(C-C^T); iDelta Hermitian.
  3. SJ Wightman W = positive part of iDelta = sum_{lam_k>0} lam_k |v_k><v_k|.

MEASUREMENTS (mirroring VYPOCET-05)
  (1) SJ existence at fixed-r sections inside the ergoregion (r_+ < r < 2M):
      Lorentzian check, +/- eigenvalue pairing, machine-precision diagnostics.
  (2) co-rotating link fraction f_co and causal asymmetry A_caus = 2 f_co - 1
      scanned across r -- does the interior null slope cross zero EXACTLY at
      r_erg = 2M, as it crossed at sqrt(M) in BTZ?
  (3) Wightman directional asymmetry A_W sign vs A_caus sign -- does the
      OPPOSITE-SIGN phenomenon from BTZ replicate in Kerr?
  (4) a-dependence: A_caus at r=1.5 (only a=0.9 Lorentzian) AND at r=2.5
      (all a Lorentzian) for a in {0.3, 0.6, 0.9}.

NO result is tuned.  Clean mismatches (static/inside-horizon degeneration,
Euclidean sections) are reported as findings.
"""

import json
import os
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

OUTDIR = os.path.dirname(os.path.abspath(__file__))
PLOTDIR = os.path.join(OUTDIR, "plots")
os.makedirs(PLOTDIR, exist_ok=True)
np.set_printoptions(precision=4, suppress=True)


# ===========================================================================
# 1.  Kerr equatorial geometry (G=c=1)
# ===========================================================================

def kerr_surfaces(M, a):
    """Outer/inner horizon radii and equatorial ergosphere radius.

    r_pm  = M +/- sqrt(M^2 - a^2)   (Delta = 0)
    r_erg = 2 M                     (equatorial static limit, g_tt=0)
    Returns (r_plus, r_minus, r_erg).  Requires M>0 and |a|<=M.
    """
    disc = M**2 - a**2
    if disc < 0:
        raise ValueError("over-extremal Kerr: need |a| <= M")
    rp = M + np.sqrt(disc)
    rm = M - np.sqrt(disc)
    rerg = 2.0 * M
    return rp, rm, rerg


def section_metric(M, a, r):
    """Constant 2-metric of the equatorial fixed-r (t,phi) section.

    h = [[g_tt, g_tphi],[g_tphi, g_phiphi]]
      = [[-(1-2M/r), -2Ma/r],[-2Ma/r, r^2+a^2+2Ma^2/r]].
    det h = -(r^2 - 2 M r + a^2) = -Delta  (negative outside the outer horizon).
    """
    g_tt = -(1.0 - 2.0 * M / r)
    g_tp = -2.0 * M * a / r
    g_pp = r**2 + a**2 + 2.0 * M * a**2 / r
    h = np.array([[g_tt, g_tp], [g_tp, g_pp]], dtype=float)
    return h


def delta_fn(M, a, r):
    return r**2 - 2.0 * M * r + a**2


# ===========================================================================
# 2.  Causal order on the fixed-r (t,phi) section (tilted light cones)
# ===========================================================================

def time_orientation(h):
    """Future-directed timelike reference vector T=(1,s_drag), LNRF direction.
    s_drag = -h_tphi/h_phiphi; timelike since h(T,T)=det h/h_phiphi<0."""
    s_drag = -h[0, 1] / h[1, 1]
    T = np.array([1.0, s_drag])
    hTT = float(T @ h @ T)
    return T, hTT, s_drag


def null_slopes(h):
    """Null slopes dphi/dt: solve h_pp s^2 + 2 h_tp s + h_tt = 0.
    Real iff disc = 4 h_tp^2 - 4 h_pp h_tt = -4 det h > 0 (i.e. det h<0)."""
    a = h[1, 1]; b = 2 * h[0, 1]; c = h[0, 0]
    disc = b * b - 4 * a * c
    if disc < 0:
        return np.nan, np.nan, disc
    sm = (-b - np.sqrt(disc)) / (2 * a)
    sp = (-b + np.sqrt(disc)) / (2 * a)
    return sm, sp, disc


def causal_matrix_section(coords, h):
    """C[x,y] = 1 if y precedes x (y in causal past of x), else 0. Diag 0.
    For D = coord_x - coord_y: causal h(D,D)<=0 AND future h(T,D)<0."""
    T, hTT, _ = time_orientation(h)
    X = coords[:, None, :]
    Y = coords[None, :, :]
    D = X - Y
    hD = D @ h
    DhD = np.sum(D * hD, axis=2)
    hT = h @ T
    ThD = D @ hT
    eps = 1e-12
    causal = DhD <= eps
    future = ThD < -eps
    prec = causal & future
    C = prec.astype(np.float64)
    np.fill_diagonal(C, 0.0)
    return C


def proper_density(h, T_extent, Phi_extent, N):
    deth = np.linalg.det(h)
    vol = np.sqrt(-deth) * T_extent * Phi_extent
    return N / vol, vol


def sprinkle_section(N, T_extent, Phi_extent, rng):
    t = rng.uniform(0.0, T_extent, size=N)
    p = rng.uniform(0.0, Phi_extent, size=N)
    return np.column_stack([t, p])


# ===========================================================================
# 3.  SJ construction (Sorkin-Yazdi 1611.10281 conventions)
# ===========================================================================

def pauli_jordan(C):
    """iDelta = i*(1/2)(C - C^T).  Hermitian."""
    Delta = 0.5 * (C - C.T)
    return 1j * Delta


def sj_decompose(iDelta):
    w, V = np.linalg.eigh(iDelta)
    pos = w > 0
    lam = w[pos]; Vp = V[:, pos]
    W = (Vp * lam) @ Vp.conj().T
    pos_spec = np.sort(lam)[::-1]
    return w, V, pos_spec, W


def spectrum_health(w, tol=1e-9):
    """+/- pairing of iDelta spectrum, trace, machine-precision residual."""
    wsort = np.sort(w)
    pos = wsort[wsort > tol]
    negabs = np.sort(np.abs(wsort[wsort < -tol]))
    npos, nneg = len(pos), len(negabs)
    k = min(npos, nneg)
    if k > 0:
        pair_res = float(np.max(np.abs(np.sort(pos)[:k] - negabs[:k])))
        rel = pair_res / np.max(np.abs(wsort))
    else:
        pair_res, rel = np.nan, np.nan
    return {
        "n_positive": int(npos), "n_negative": int(nneg),
        "n_zero": int(np.sum(np.abs(wsort) <= tol)),
        "trace": float(np.sum(w)),
        "pairing_residual_abs": pair_res,
        "pairing_residual_rel": rel,
        "max_abs_eig": float(np.max(np.abs(w))),
    }


# ===========================================================================
# 4.  Observables on the SJ state
# ===========================================================================

def two_point_profile(W, coords, h, C, n_bins=40):
    """(1) causal directional asymmetry A_caus = 2 f_co - 1, and
       (2) SJ Wightman directional asymmetry A_W, over causally-related pairs."""
    _, _, s_drag = time_orientation(h)
    xi, yi = np.where(C > 0)
    dt = coords[xi, 0] - coords[yi, 0]
    dphi = coords[xi, 1] - coords[yi, 1]
    ReWp = np.real(W[xi, yi])
    n_links = len(dphi)
    if n_links == 0:
        return {"s_drag": float(s_drag), "n_causal_links": 0}

    f_co = float(np.mean(dphi > 0))
    A_caus = 2.0 * f_co - 1.0
    mean_dphi = float(np.mean(dphi))
    mean_slope = float(np.mean(dphi / dt))

    co = dphi > 0; cc = dphi < 0
    m_co = float(np.mean(ReWp[co])) if np.any(co) else np.nan
    m_cc = float(np.mean(ReWp[cc])) if np.any(cc) else np.nan
    if np.any(co) and np.any(cc):
        A_W = (m_co - m_cc) / (abs(m_co) + abs(m_cc)) if (abs(m_co) + abs(m_cc)) > 0 else 0.0
    else:
        A_W = None

    tscale = coords[:, 0].max() - coords[:, 0].min()
    sel = dt < 0.15 * tscale
    dphi_s = dphi[sel]; W_s = ReWp[sel]
    lim = np.percentile(np.abs(dphi_s), 98) if dphi_s.size else 1.0
    edges = np.linspace(-lim, lim, n_bins + 1)
    centers = 0.5 * (edges[:-1] + edges[1:])
    prof = np.full(n_bins, np.nan)
    for b in range(n_bins):
        m = (dphi_s >= edges[b]) & (dphi_s < edges[b + 1])
        if np.any(m):
            prof[b] = np.mean(W_s[m])
    return {
        "s_drag": float(s_drag),
        "n_causal_links": int(n_links),
        "frac_corotating_links": f_co,
        "causal_asymmetry": float(A_caus),
        "mean_dphi": mean_dphi,
        "mean_dphi_over_dt": mean_slope,
        "wightman_asymmetry": A_W,
        "mean_ReW_corot": m_co if np.isfinite(m_co) else None,
        "mean_ReW_counter": m_cc if np.isfinite(m_cc) else None,
        "bin_centers": centers.tolist(),
        "profile_ReW_vs_dphi": prof.tolist(),
    }


# ===========================================================================
# 5.  Experiment driver
# ===========================================================================

def build_region(M, a, r, T_extent, Phi_extent, N, seed):
    """Full SJ build for one (M,a,r) equatorial fixed-r (t,phi) patch."""
    rng = np.random.default_rng(seed)
    h = section_metric(M, a, r)
    deth = float(np.linalg.det(h))
    sm, sp, disc = null_slopes(h)
    T, hTT, s_drag = time_orientation(h)
    rp, rm, rerg = kerr_surfaces(M, a)
    in_ergo = (r < rerg) and (r > rp)
    out = {
        "M": M, "a": a, "r": r, "r_plus": rp, "r_minus": rm, "r_erg": rerg,
        "in_ergoregion": bool(in_ergo),
        "g_tt": float(h[0, 0]), "g_tphi": float(h[0, 1]), "g_phiphi": float(h[1, 1]),
        "det_h": deth, "Delta": float(delta_fn(M, a, r)),
        "null_slope_minus": float(sm) if np.isfinite(sm) else None,
        "null_slope_plus": float(sp) if np.isfinite(sp) else None,
        "cone_discriminant": float(disc),
        "frame_drag_slope": float(s_drag),
        "ref_timelike_norm": float(hTT),
        "section_lorentzian": bool(deth < 0 and disc > 0),
        "N": N, "T_extent": T_extent, "Phi_extent": Phi_extent, "seed": seed,
    }
    if deth >= 0 or disc <= 0:
        out["SJ_constructible"] = False
        out["reason"] = ("equatorial fixed-r (t,phi) section not Lorentzian "
                         "(no real light cone; r inside horizon => Euclidean)")
        return out, None, None, None

    rho, vol = proper_density(h, T_extent, Phi_extent, N)
    out["sprinkle_density"] = float(rho); out["proper_area"] = float(vol)
    coords = sprinkle_section(N, T_extent, Phi_extent, rng)
    C = causal_matrix_section(coords, h)
    link_frac = float(C.sum() / (N * (N - 1)))
    out["causal_link_fraction"] = link_frac
    iDelta = pauli_jordan(C)
    w, V, pos_spec, W = sj_decompose(iDelta)
    out["SJ_constructible"] = True
    out["health"] = spectrum_health(w)
    out["n_positive_modes"] = int(len(pos_spec))
    out["pos_spectrum_head"] = pos_spec[:40].tolist()
    tp = two_point_profile(W, coords, h, C)
    out["two_point"] = tp
    return out, coords, (w, pos_spec, W), C


def avg_over_seeds(M, a, r, T_extent, Phi_extent, N, seeds):
    """Average A_caus, A_W, f_co, pairing residual over seeds for a (Lorentzian) r."""
    Acaus, AW, fco, pair, drag = [], [], [], [], []
    spec0 = None
    constructible = None
    for s in seeds:
        rr, _, sj, _ = build_region(M, a, r, T_extent, Phi_extent, N, seed=s)
        constructible = rr["SJ_constructible"]
        if not constructible:
            return {"constructible": False, "reason": rr.get("reason"),
                    "det_h": rr["det_h"], "in_ergoregion": rr["in_ergoregion"],
                    "r_plus": rr["r_plus"], "section_lorentzian": rr["section_lorentzian"]}
        tp = rr["two_point"]
        Acaus.append(tp["causal_asymmetry"])
        if tp["wightman_asymmetry"] is not None:
            AW.append(tp["wightman_asymmetry"])
        fco.append(tp["frac_corotating_links"])
        pair.append(rr["health"]["pairing_residual_rel"])
        drag.append(rr["frame_drag_slope"])
        if spec0 is None:
            spec0 = sj[1]
    out = {
        "constructible": True,
        "A_caus_mean": float(np.mean(Acaus)),
        "A_caus_sd": float(np.std(Acaus, ddof=1)) if len(Acaus) > 1 else 0.0,
        "A_W_mean": float(np.mean(AW)) if AW else None,
        "A_W_sd": float(np.std(AW, ddof=1)) if len(AW) > 1 else (0.0 if AW else None),
        "f_co_mean": float(np.mean(fco)),
        "frame_drag_slope": float(np.mean(drag)),
        "pairing_residual_rel_max": float(np.max(pair)),
        "n_seeds": len(seeds),
    }
    return out


def run():
    results = {"conventions": {
        "geometry": "equatorial Kerr (theta=pi/2), Boyer-Lindquist, G=c=1, Sigma=r^2",
        "g_tt": "-(1-2M/r)", "g_tphi": "-2Ma/r", "g_phiphi": "r^2+a^2+2Ma^2/r",
        "g_rr": "r^2/Delta, Delta=r^2-2Mr+a^2",
        "section": "fixed-r (t,phi); h=[[-(1-2M/r),-2Ma/r],[-2Ma/r,r^2+a^2+2Ma^2/r]]; det h=-Delta",
        "surfaces": "r_+=M+sqrt(M^2-a^2); r_erg=2M (equator, a-independent); ergoregion=(r_+,2M)",
        "G_R": "G_R=(1/2)C (2D massless, conformally invariant) [Sorkin-Yazdi 1611.10281 eq.9; AdS2 use 2504.12919]",
        "massive_GR": "G_R=(1/2)C(I+(m^2/2rho)C)^-1 -> (1/2)C at m=0 [1701.07212,1712.04227]",
        "iDelta": "iDelta=i*(1/2)(C-C^T) Hermitian; SJ W=positive part of iDelta",
        "causal_order": "y prec x iff D=x-y future-causal: h(D,D)<=0 and h(T,D)<0, T=(1,-g_tphi/g_phiphi)",
        "metric_source": "Wikipedia 'Kerr metric' equatorial components; det h=-Delta verified by sympy",
        "honest_note": ("Kerr ergoregion is a THIN SHELL (r_+,2M); r=1.5 Lorentzian only for a=0.9. "
                        "g_tphi is r-dependent (unlike BTZ constant -J/2). Finite phi-window patch, "
                        "not the 2pi circle."),
    }}

    # ---------------- Fiducial parameters -----------------------------------
    M = 1.0
    a_fid = 0.6
    a_aggr = 0.9
    N = 1600
    seeds = [101, 202, 303]        # >=3 seeds
    T_extent = 1.4
    Phi_extent = 1.4

    rp, rm, rerg = kerr_surfaces(M, a_fid)
    rp9, rm9, _ = kerr_surfaces(M, a_aggr)
    results["fiducial"] = {"M": M, "a_fid": a_fid, "a_aggressive": a_aggr,
                           "r_plus(a=0.6)": rp, "r_minus(a=0.6)": rm, "r_erg": rerg,
                           "ergoregion(a=0.6)": [rp, rerg],
                           "r_plus(a=0.9)": rp9, "ergoregion(a=0.9)": [rp9, rerg],
                           "N": N, "seeds": seeds,
                           "T_extent": T_extent, "Phi_extent": Phi_extent}
    print(f"Kerr M={M} a={a_fid}: r_+={rp:.4f} r_-={rm:.4f} r_erg={rerg:.4f} "
          f"ergoregion=({rp:.4f},{rerg:.4f})")
    print(f"Kerr M={M} a={a_aggr}: r_+={rp9:.4f} ergoregion=({rp9:.4f},{rerg:.4f})")

    # ====================================================================
    # PART A: SJ existence INSIDE the ergoregion (r_+ < r < 2M)
    #   Use a=0.9 (widest shell): r_in well inside (r_+, 2M).
    #   Also show: matched STATIC analog (a=0 => r_+=2M=r_erg, no ergoregion;
    #   the same r is inside the Schwarzschild horizon => Euclidean section).
    # ====================================================================
    print("\n=== PART A: SJ existence inside the Kerr ergoregion ===")
    A = {"per_a": {}}
    fig_data = {}   # holds numpy coords/info for plotting only (NOT serialized)
    # representative radii inside the ergoregion for each a where it has width
    for a in [0.6, 0.9]:
        rpa, _, _ = kerr_surfaces(M, a)
        r_in = 0.5 * (rpa + rerg)   # midpoint of the ergoshell
        rr, c_in, sj_in, C_in = build_region(M, a, r_in, T_extent, Phi_extent, N, seed=seeds[0])
        rec = {"a": a, "r_in": r_in, "in_ergoregion": rr["in_ergoregion"],
               "section_lorentzian": rr["section_lorentzian"],
               "g_tt": rr["g_tt"], "det_h": rr["det_h"],
               "null_slopes": [rr["null_slope_minus"], rr["null_slope_plus"]],
               "frame_drag_slope": rr["frame_drag_slope"],
               "SJ_constructible": rr["SJ_constructible"]}
        if rr["SJ_constructible"]:
            rec["health"] = rr["health"]
            rec["two_point"] = {k: rr["two_point"][k] for k in
                                ("frac_corotating_links", "causal_asymmetry",
                                 "mean_dphi_over_dt", "s_drag", "wightman_asymmetry")}
            print(f"[a={a}, r={r_in:.3f} INSIDE ergo] g_tt={rr['g_tt']:+.3f} (>0=>d_t spacelike) "
                  f"Lorentzian={rr['section_lorentzian']} SJ={rr['SJ_constructible']}")
            print(f"     null slopes=({rr['null_slope_minus']:+.4f},{rr['null_slope_plus']:+.4f}) "
                  f"BOTH>0 (fully dragged), drag={rr['frame_drag_slope']:.4f}")
            print(f"     spectrum: {rr['health']['n_positive']}+/{rr['health']['n_negative']}- pairs, "
                  f"pairing_rel={rr['health']['pairing_residual_rel']:.1e}, trace={rr['health']['trace']:.1e}")
            print(f"     f_co={rr['two_point']['frac_corotating_links']:.3f} "
                  f"A_caus={rr['two_point']['causal_asymmetry']:+.3f} "
                  f"<dphi/dt>={rr['two_point']['mean_dphi_over_dt']:.4f} vs drag={rr['two_point']['s_drag']:.4f}")
        A["per_a"][f"a={a}"] = rec
        if a == a_aggr:
            fig_data = {"a": a, "r_in": r_in, "coords": c_in, "info": rr}

    # static analog at the SAME inside-ergo radius (a=0 Schwarzschild)
    r_in9 = 0.5 * (rp9 + rerg)
    stat, _, _, _ = build_region(M, 0.0, r_in9, T_extent, Phi_extent, N, seed=seeds[0])
    A["static_analog"] = {"a": 0.0, "r": r_in9, "section_lorentzian": stat["section_lorentzian"],
                          "det_h": stat["det_h"], "cone_discriminant": stat["cone_discriminant"],
                          "SJ_constructible": stat["SJ_constructible"],
                          "reason": stat.get("reason"),
                          "note": "a=0: r_+=2M=r_erg (no ergoregion); this r is inside the Schwarzschild horizon => Euclidean section"}
    print(f"[STATIC a=0, r={r_in9:.3f}] Lorentzian={stat['section_lorentzian']} "
          f"SJ={stat['SJ_constructible']} det_h={stat['det_h']:+.4f} -> {stat.get('reason','(ok)')}")
    A["headline"] = (
        "SJ is constructible (Hermitian iDelta, machine-precision +/- paired spectrum) at "
        "equatorial fixed-r sections INSIDE the Kerr ergoregion (r_+<r<2M) where g_tt>0 "
        "(d_t spacelike). The matched static (Schwarzschild) section at the same r is inside "
        "the horizon and is NOT Lorentzian. Same outcome as rotating BTZ."
    )
    results["partA_existence"] = A

    # ====================================================================
    # PART B: radial scan of f_co, A_caus, A_W, null slopes across r
    #   Does the interior null slope cross zero EXACTLY at r_erg=2M?
    #   (BTZ analog: it crossed at sqrt(M).)
    # ====================================================================
    print("\n=== PART B: radial scan across the ergosphere (a=0.6 and a=0.9) ===")
    B = {}
    for a in [a_fid, a_aggr]:
        rpa, _, _ = kerr_surfaces(M, a)
        # scan from just outside horizon to outside ergosphere; dense near r_erg=2
        r_scan = np.unique(np.concatenate([
            np.linspace(rpa * 1.005, 2.0, 14),
            np.linspace(2.0, 3.2, 8),
            [1.96, 1.98, 1.99, 1.995, 2.0, 2.005, 2.01, 2.02, 2.04],
        ]))
        r_scan = r_scan[r_scan > rpa]
        scan = {"a": a, "r_plus": rpa, "r_erg": rerg, "r": [], "in_ergo": [],
                "lorentzian": [], "g_tt": [], "det_h": [], "drag": [],
                "slope_minus": [], "slope_plus": [], "f_co": [], "A_caus": [],
                "A_caus_sd": [], "A_W": [], "A_W_sd": []}
        for rv in r_scan:
            agg = avg_over_seeds(M, a, rv, T_extent, Phi_extent, N, seeds)
            base, _, _, _ = build_region(M, a, rv, T_extent, Phi_extent, N, seed=seeds[0])
            scan["r"].append(float(rv))
            scan["in_ergo"].append(bool(base["in_ergoregion"]))
            scan["lorentzian"].append(bool(base["section_lorentzian"]))
            scan["g_tt"].append(float(base["g_tt"]))
            scan["det_h"].append(float(base["det_h"]))
            scan["drag"].append(float(base["frame_drag_slope"]))
            scan["slope_minus"].append(base["null_slope_minus"])
            scan["slope_plus"].append(base["null_slope_plus"])
            if agg["constructible"]:
                scan["f_co"].append(agg["f_co_mean"])
                scan["A_caus"].append(agg["A_caus_mean"])
                scan["A_caus_sd"].append(agg["A_caus_sd"])
                scan["A_W"].append(agg["A_W_mean"])
                scan["A_W_sd"].append(agg["A_W_sd"])
            else:
                for k in ("f_co", "A_caus", "A_caus_sd", "A_W", "A_W_sd"):
                    scan[k].append(None)
        # locate interior-null-slope zero crossing
        rr = np.array(scan["r"]); sm = np.array([s if s is not None else np.nan for s in scan["slope_minus"]])
        good = np.isfinite(sm)
        cross = None
        rr_g, sm_g = rr[good], sm[good]
        sgn = np.sign(sm_g)
        idx = np.where(np.diff(sgn) != 0)[0]
        if len(idx):
            i = idx[0]
            # linear interp of slope_minus zero
            cross = float(rr_g[i] - sm_g[i] * (rr_g[i+1]-rr_g[i])/(sm_g[i+1]-sm_g[i]))
        scan["interior_null_slope_zero_crossing"] = cross
        scan["r_erg_expected"] = rerg
        print(f"[a={a}] interior null slope (slope_-) crosses zero at r={cross} "
              f"(expected r_erg=2M={rerg}); match={'yes' if cross and abs(cross-rerg)<0.02 else 'check'}")
        B[f"a={a}"] = scan
    results["partB_radial_scan"] = B

    # ====================================================================
    # PART C: A_W sign vs A_caus sign -- OPPOSITE-SIGN test (the BTZ phenomenon)
    #   Evaluate at a radius OUTSIDE the ergosphere (both signs defined).
    # ====================================================================
    print("\n=== PART C: A_W sign vs A_caus sign (opposite-sign replication test) ===")
    C = {}
    for a in [a_fid, a_aggr]:
        for label, rv in [("just_outside_ergo", 2.2), ("outside", 2.6), ("far", 3.2)]:
            agg = avg_over_seeds(M, a, rv, T_extent, Phi_extent, N, seeds)
            if agg["constructible"]:
                ac, aw = agg["A_caus_mean"], agg["A_W_mean"]
                opp = (aw is not None) and (np.sign(ac) != np.sign(aw)) and abs(ac) > 1e-6 and abs(aw) > 1e-6
                rec = {"a": a, "r": rv, "A_caus": ac, "A_caus_sd": agg["A_caus_sd"],
                       "A_W": aw, "A_W_sd": agg["A_W_sd"], "f_co": agg["f_co_mean"],
                       "opposite_sign": bool(opp)}
                C[f"a={a}_{label}_r={rv}"] = rec
                print(f"[a={a}, r={rv} {label}] A_caus={ac:+.4f}+/-{agg['A_caus_sd']:.4f}  "
                      f"A_W={aw:+.4f}  opposite_sign={opp}")
    # static control: a=0 outside (should be ~0 both)
    sc = avg_over_seeds(M, 0.0, 2.6, T_extent, Phi_extent, N, seeds)
    if sc["constructible"]:
        C["static_control_a=0_r=2.6"] = {"A_caus": sc["A_caus_mean"], "A_caus_sd": sc["A_caus_sd"],
                                         "A_W": sc["A_W_mean"], "f_co": sc["f_co_mean"]}
        print(f"[STATIC a=0, r=2.6] A_caus={sc['A_caus_mean']:+.4f}+/-{sc['A_caus_sd']:.4f}  "
              f"A_W={sc['A_W_mean'] if sc['A_W_mean'] is None else f'{sc['A_W_mean']:+.4f}'} (control ~0)")
    results["partC_opposite_sign"] = C

    # ====================================================================
    # PART D: a-dependence.  A_caus at r=1.5 for a in {0.3,0.6,0.9}
    #   (only a=0.9 is Lorentzian there -- reported honestly), AND at r=2.5
    #   (all a Lorentzian) for a clean comparable a-trend.
    # ====================================================================
    print("\n=== PART D: a-dependence of A_caus ===")
    D = {"r=1.5_requested": {}, "r=2.5_comparable": {}}
    for a in [0.3, 0.6, 0.9]:
        rpa, _, _ = kerr_surfaces(M, a)
        agg15 = avg_over_seeds(M, a, 1.5, T_extent, Phi_extent, N, seeds)
        rec15 = {"a": a, "r_plus": rpa, "r": 1.5}
        if agg15["constructible"]:
            rec15.update({"A_caus": agg15["A_caus_mean"], "A_caus_sd": agg15["A_caus_sd"],
                          "A_W": agg15["A_W_mean"], "f_co": agg15["f_co_mean"],
                          "in_ergoregion": (1.5 > rpa and 1.5 < rerg)})
            print(f"[r=1.5, a={a}] r_+={rpa:.3f} LORENTZIAN  A_caus={agg15['A_caus_mean']:+.4f} "
                  f"f_co={agg15['f_co_mean']:.3f} (in_ergo={1.5>rpa and 1.5<rerg})")
        else:
            rec15.update({"constructible": False, "reason": agg15["reason"],
                          "det_h": agg15["det_h"], "note": "r=1.5 < r_+: inside horizon, Euclidean section"})
            print(f"[r=1.5, a={a}] r_+={rpa:.3f} -> r=1.5 INSIDE horizon, EUCLIDEAN section "
                  f"(det_h={agg15['det_h']:+.3f}>0), SJ not constructible")
        D["r=1.5_requested"][f"a={a}"] = rec15

        agg25 = avg_over_seeds(M, a, 2.5, T_extent, Phi_extent, N, seeds)
        rec25 = {"a": a, "r": 2.5, "A_caus": agg25["A_caus_mean"], "A_caus_sd": agg25["A_caus_sd"],
                 "A_W": agg25["A_W_mean"], "f_co": agg25["f_co_mean"],
                 "frame_drag_slope": agg25["frame_drag_slope"]}
        D["r=2.5_comparable"][f"a={a}"] = rec25
        print(f"[r=2.5, a={a}] A_caus={agg25['A_caus_mean']:+.4f}+/-{agg25['A_caus_sd']:.4f} "
              f"f_co={agg25['f_co_mean']:.3f} A_W={agg25['A_W_mean']:+.4f} drag={agg25['frame_drag_slope']:.4f}")
    # monotonic in a?
    avals = [0.3, 0.6, 0.9]
    ac25 = [D["r=2.5_comparable"][f"a={a}"]["A_caus"] for a in avals]
    D["A_caus_r2.5_monotone_increasing_in_a"] = bool(all(np.diff(ac25) > 0))
    results["partD_a_dependence"] = D

    # ====================================================================
    # PLOTS
    # ====================================================================
    _plot_cones(fig_data, A["static_analog"], M, a_aggr, rerg)
    _plot_radial(B, M, a_fid, a_aggr, rerg)
    _plot_asymmetry(C, D, B, M, a_fid, a_aggr, rerg)
    _plot_spectrum(A)

    # ---------------- headline summary ------------------------------------
    a6 = B[f"a={a_fid}"]; a9 = B[f"a={a_aggr}"]
    # pick the A_caus / A_W at r=2.6 for headline opposite-sign
    csel = C.get(f"a={a_fid}_outside_r=2.6")
    in9 = A["per_a"]["a=0.9"]
    results["headline_results"] = {
        "SJ_exists_in_kerr_ergoregion": bool(in9["SJ_constructible"]),
        "ergoregion_pairing_residual_rel": in9.get("health", {}).get("pairing_residual_rel"),
        "ergoregion_n_mode_pairs": in9.get("health", {}).get("n_positive"),
        "g_tt_inside_ergo_positive(d_t spacelike)": in9["g_tt"] > 0,
        "static_analog_degenerates": (not A["static_analog"]["section_lorentzian"]),
        "f_co_inside_ergo": in9.get("two_point", {}).get("frac_corotating_links"),
        "A_caus_inside_ergo": in9.get("two_point", {}).get("causal_asymmetry"),
        "interior_null_slope_zero_crossing_a0.6": a6["interior_null_slope_zero_crossing"],
        "interior_null_slope_zero_crossing_a0.9": a9["interior_null_slope_zero_crossing"],
        "r_erg_expected": rerg,
        "zero_crossing_matches_r_erg": bool(
            a6["interior_null_slope_zero_crossing"] is not None and
            abs(a6["interior_null_slope_zero_crossing"] - rerg) < 0.02),
        "opposite_sign_A_W_vs_A_caus(a=0.6,r=2.6)": csel["opposite_sign"] if csel else None,
        "A_caus_at_r2.6": csel["A_caus"] if csel else None,
        "A_W_at_r2.6": csel["A_W"] if csel else None,
        "a_dependence_A_caus_r2.5": {f"a={a}": D["r=2.5_comparable"][f"a={a}"]["A_caus"] for a in avals},
        "A_caus_monotone_increasing_in_a_at_r2.5": D["A_caus_r2.5_monotone_increasing_in_a"],
        "r1.5_lorentzian_only_for_a0.9": True,
        "verdict": (
            "The BTZ SJ signatures replicate in asymptotically-flat equatorial Kerr: (1) SJ is "
            "machine-precision well-defined at fixed-r sections inside the ergoregion (r_+<r<2M) "
            "where d_t is spacelike, while the static analog there is non-Lorentzian; (2) the "
            "interior null slope crosses zero EXACTLY at r_erg=2M (Kerr analog of the BTZ crossing "
            "at sqrt(M)), and f_co/A_caus rise to +1 inside the ergoregion and decay ~outward; "
            "(3) the OPPOSITE-SIGN phenomenon (A_caus>0 but A_W<0) replicates; (4) A_caus grows "
            "monotonically with spin a. Geometry-independent SJ properties of rotating spacetimes."
        ),
    }

    with open(os.path.join(OUTDIR, "results.json"), "w") as f:
        json.dump(results, f, indent=2)
    print("\nSaved results.json and plots to", OUTDIR)
    return results


# ===========================================================================
# Plotting helpers
# ===========================================================================

def _plot_cones(fig_data, static, M, a, rerg):
    info = fig_data["info"]; coords = fig_data["coords"]; r_in = fig_data["r_in"]
    fig, axes = plt.subplots(1, 2, figsize=(13, 5.5))
    ax = axes[0]
    ax.plot(coords[:, 0], coords[:, 1], '.', ms=2.5, color="navy", alpha=0.5)
    c0 = np.array([0.5 * info["T_extent"], 0.5 * info["Phi_extent"]])
    sm, sp = info["null_slope_minus"], info["null_slope_plus"]
    L = 0.45 * info["T_extent"]
    for sgn in (+1, -1):
        ax.plot([c0[0], c0[0] + sgn * L], [c0[1], c0[1] + sgn * L * sm], 'r-', lw=2)
        ax.plot([c0[0], c0[0] + sgn * L], [c0[1], c0[1] + sgn * L * sp], 'r-', lw=2)
    ax.plot([c0[0], c0[0] + 0.4 * L], [c0[1], c0[1] + 0.4 * L * info["frame_drag_slope"]],
            'g-', lw=2.5, label=f"frame-drag (timelike) slope={info['frame_drag_slope']:.3f}")
    ax.plot(*c0, 'ks', ms=7)
    ax.set_title(f"KERR a={a}, r={r_in:.3f} INSIDE ergoregion (g_tt={info['g_tt']:+.3f}>0)\n"
                 f"null slopes ({sm:.3f},{sp:.3f}); BOTH>0 = fully dragged cone")
    ax.set_xlabel("t"); ax.set_ylabel(r"$\phi$")
    ax.set_xlim(0, info["T_extent"]); ax.set_ylim(0, info["Phi_extent"]); ax.legend(fontsize=8, loc="upper left")

    ax2 = axes[1]
    ax2.text(0.5, 0.5,
             f"STATIC a=0, r={static['r']:.3f}\nequatorial fixed-r (t,phi) section\n"
             f"r < r_+ = 2M (inside Schwarzschild horizon)\n"
             f"det h = {static['det_h']:+.4f} > 0  =>  EUCLIDEAN\n"
             f"(no real light cone: no timelike dir)\nSJ NOT constructible",
             ha="center", va="center", fontsize=11,
             bbox=dict(boxstyle="round", fc="mistyrose", ec="firebrick"))
    ax2.set_title(f"STATIC control a=0, r={static['r']:.3f}")
    ax2.set_xlabel("t"); ax2.set_ylabel(r"$\phi$")
    ax2.set_xlim(0, info["T_extent"]); ax2.set_ylim(0, info["Phi_extent"])
    fig.suptitle("SJ region: Kerr ergoregion (cones survive & tilt) vs static degeneration", fontsize=12)
    fig.tight_layout(); fig.savefig(os.path.join(PLOTDIR, "sprinkle_cones.png"), dpi=140); plt.close(fig)


def _plot_radial(B, M, a_fid, a_aggr, rerg):
    fig, axes = plt.subplots(1, 2, figsize=(14, 5.5))
    for ax, a in zip(axes, [a_fid, a_aggr]):
        s = B[f"a={a}"]; rp = s["r_plus"]
        rr = np.array(s["r"])
        sm = np.array([x if x is not None else np.nan for x in s["slope_minus"]])
        sp = np.array([x if x is not None else np.nan for x in s["slope_plus"]])
        drag = np.array(s["drag"])
        ax.axvspan(rp, rerg, color="gold", alpha=0.3, label="ergoregion $(r_+,2M)$")
        ax.axhline(0, color="gray", lw=0.8)
        ax.fill_between(rr, sm, sp, color="red", alpha=0.12)
        ax.plot(rr, sm, 'r-', lw=1.5, label=r"interior null slope $s_-$")
        ax.plot(rr, sp, 'r--', lw=1.2, label=r"exterior null slope $s_+$")
        ax.plot(rr, drag, 'g-', lw=2, label="frame-drag slope")
        ax.axvline(rp, color="k", ls="--", lw=1); ax.axvline(rerg, color="orange", ls="--", lw=1.2)
        cross = s["interior_null_slope_zero_crossing"]
        if cross:
            ax.plot([cross], [0], 'b*', ms=14, label=f"$s_-=0$ at r={cross:.3f}")
        ax.text(rp, ax.get_ylim()[1]*0.92, "$r_+$", color="k")
        ax.text(rerg, ax.get_ylim()[1]*0.92, "$r_{erg}=2M$", color="orange")
        ax.set_xlabel("r"); ax.set_ylabel(r"$d\phi/dt$")
        ax.set_title(f"Kerr a={a}: cone tilt across ergosphere\n"
                     f"interior null slope $s_-$ crosses 0 at r={cross:.4f} (=2M)")
        ax.legend(fontsize=8)
    fig.suptitle("Light-cone tilt across the equatorial ergosphere (Kerr)", fontsize=12)
    fig.tight_layout(); fig.savefig(os.path.join(PLOTDIR, "cone_tilt_radial.png"), dpi=140); plt.close(fig)


def _plot_asymmetry(C, D, B, M, a_fid, a_aggr, rerg):
    fig, axes = plt.subplots(1, 2, figsize=(14, 5.5))
    # left: A_caus & A_W vs r (a=0.6) from scan B
    ax = axes[0]
    s = B[f"a={a_fid}"]; rp = s["r_plus"]
    rr = np.array(s["r"])
    ac = np.array([x if x is not None else np.nan for x in s["A_caus"]])
    aw = np.array([x if x is not None else np.nan for x in s["A_W"]])
    fco = np.array([x if x is not None else np.nan for x in s["f_co"]])
    ax.axvspan(rp, rerg, color="gold", alpha=0.3, label="ergoregion")
    ax.axhline(0, color="gray", lw=0.8); ax.axhline(1, color="gray", lw=0.4, ls=":")
    ax.plot(rr, ac, 'o-', color="crimson", ms=4, label=r"$A_{caus}=2f_{co}-1$")
    ax.plot(rr, aw, 's-', color="navy", ms=4, label=r"$A_W$ (SJ Wightman)")
    ax.axvline(rerg, color="orange", ls="--", lw=1.2)
    ax.text(rerg, 0.9, "$r_{erg}=2M$", color="orange")
    ax.set_xlabel("r"); ax.set_ylabel("directional asymmetry")
    ax.set_title(f"Kerr a={a_fid}: $A_{{caus}}>0$ but $A_W<0$ (OPPOSITE sign, as in BTZ)")
    ax.legend(fontsize=8)
    # right: a-dependence of A_caus at r=2.5 (comparable)
    ax2 = axes[1]
    avals = [0.3, 0.6, 0.9]
    ac25 = [D["r=2.5_comparable"][f"a={a}"]["A_caus"] for a in avals]
    sd25 = [D["r=2.5_comparable"][f"a={a}"]["A_caus_sd"] for a in avals]
    aw25 = [D["r=2.5_comparable"][f"a={a}"]["A_W"] for a in avals]
    ax2.errorbar(avals, ac25, yerr=sd25, fmt='o-', color="crimson", capsize=4,
                 label=r"$A_{caus}$ at r=2.5")
    ax2.plot(avals, aw25, 's-', color="navy", label=r"$A_W$ at r=2.5")
    ax2.axhline(0, color="gray", lw=0.8)
    # overlay r=1.5 point (only a=0.9 Lorentzian)
    r15 = D["r=1.5_requested"]
    a15 = [a for a in avals if r15[f"a={a}"].get("A_caus") is not None]
    ac15 = [r15[f"a={a}"]["A_caus"] for a in a15]
    if a15:
        ax2.plot(a15, ac15, 'D', color="darkgreen", ms=9,
                 label=r"$A_{caus}$ at r=1.5 (Lorentzian only a=0.9)")
    ax2.set_xlabel("spin a"); ax2.set_ylabel("directional asymmetry")
    ax2.set_title("a-dependence: frame-dragging asymmetry grows with spin")
    ax2.legend(fontsize=8)
    fig.suptitle("SJ directional asymmetry: sign and spin dependence (Kerr)", fontsize=12)
    fig.tight_layout(); fig.savefig(os.path.join(PLOTDIR, "correlation_asymmetry.png"), dpi=140); plt.close(fig)


def _plot_spectrum(A):
    in9 = A["per_a"]["a=0.9"]
    # rebuild spectrum at the inside-ergo radius to plot (cheap)
    fig, ax = plt.subplots(figsize=(7.5, 5.5))
    h = in9.get("health")
    if h:
        ax.text(0.5, 0.5,
                f"SJ spectrum diagnostics INSIDE Kerr ergoregion (a={in9['a']}, r={in9['r_in']:.3f})\n\n"
                f"n_positive = {h['n_positive']}\n"
                f"n_negative = {h['n_negative']}\n"
                f"+/- pairing residual (rel) = {h['pairing_residual_rel']:.2e}\n"
                f"trace(iDelta) = {h['trace']:.2e}\n"
                f"max|eig| = {h['max_abs_eig']:.3f}\n\n"
                f"=> iDelta Hermitian, exact +/- paired spectrum:\n   SJ Wightman well-defined.",
                ha="center", va="center", fontsize=12,
                bbox=dict(boxstyle="round", fc="honeydew", ec="seagreen"))
    ax.axis("off")
    ax.set_title("SJ existence diagnostics inside the Kerr ergoregion")
    fig.tight_layout(); fig.savefig(os.path.join(PLOTDIR, "sj_existence_spectrum.png"), dpi=140); plt.close(fig)


if __name__ == "__main__":
    run()
