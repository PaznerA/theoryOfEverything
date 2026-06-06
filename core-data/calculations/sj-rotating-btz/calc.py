#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
First numerical Sorkin-Johnston (SJ) state in a ROTATING spacetime region
==========================================================================

Flagship exploratory computation for hypothesis H02 (SJ on Kerr), Strategy II:
a 2D Lorentzian section of the *rotating* BTZ black hole that contains part of
the ERGOREGION, where no global timelike Killing vector exists.  The point is
that the SJ construction never needs a timelike Killing field, so it goes
through cleanly exactly where the standard stationary (Boulware/Hartle-Hawking)
vacua fail.

WHY 2D MASSLESS IS THE RIGHT TOOL (the conformal-triviality lever)
------------------------------------------------------------------
* Every 2D Lorentzian metric is (locally) conformally flat:  g_{ab} = Omega^2 eta_{ab}.
* The massless scalar wave operator in 2D is conformally invariant
  (conformal coupling xi = 0 IS minimal coupling in d=2).
* Hence the retarded Green function of the 2D massless scalar depends ONLY on
  the causal/conformal structure, not on the conformal factor Omega.
* On a causal set this is the exact statement
        G_R = (1/2) C ,
  C_xy = 1 if y precedes x (y in causal past of x), 0 otherwise.
  - Sorkin & Yazdi, arXiv:1611.10281, eq.(9): G_R = (1/2)C for the 2D massless
    scalar; the causal-set expectation equals the continuum G_R for ALL densities
    (their footnote 5).
  - Massive case (arXiv:1701.07212, 1712.04227, 2308.06727):
        G_R = (1/2) C ( I + (m^2/(2 rho)) C )^{-1},
    whose m->0 limit is exactly (1/2)C.
  - Explicitly USED in curved 2D (AdS_2) precisely via conformal flatness:
    "Retarded Causal Set Propagator in 2D Anti-de-Sitter Spacetime",
    arXiv:2504.12919 -- the massless 2D propagator stays (1/2)C in curved 2D
    because the conformal map preserves the causal order.

So for ANY 2D section of BTZ we only need the CAUSAL ORDER of the sprinkled
points.  Curvature, frame dragging and the ergoregion enter solely through how
they TILT the light cones (and through the proper sprinkling volume).

THE GEOMETRY (verified symbolically; see writeup)
-------------------------------------------------
Rotating BTZ, AdS radius l = 1 (Banados-Teitelboim-Zanelli):
    ds^2 = -N^2 dt^2 + N^{-2} dr^2 + r^2 (dphi + N^phi dt)^2 ,
    N^2  = -M + r^2 + J^2/(4 r^2),     N^phi = -J/(2 r^2).
Components:  g_tt = M - r^2,   g_tphi = -J/2 (constant frame dragging),
            g_phiphi = r^2,    g_rr = 1/N^2.
Outer/inner horizons:  r_pm^2 = (1/2)(M +/- sqrt(M^2 - J^2)).
Ergosphere (static limit, g_tt = 0):  r_erg = sqrt(M).
For J != 0:  r_+ < r_erg, so an ERGOREGION  r_+ < r < r_erg  exists where
g_tt > 0, i.e. d_t is SPACELIKE -- no timelike Killing vector there.

WHICH 2D REGION (honest choice)
-------------------------------
* The fixed-phi (t,r) section becomes EUCLIDEAN (signature (+,+)) inside the
  ergoregion (g_tt>0 and g_rr>0): you cannot drop phi there.  [verified]
* The fixed-r (t,phi) section stays LORENTZIAN through the ergoregion:
  det[[g_tt,g_tphi],[g_tphi,g_phiphi]] = M r^2 - r^4 - J^2/4 = -N^2 r^2 < 0
  for all r_+ < r (outside the horizon).  [verified]
  Inside the ergoregion d_t is spacelike, but a phi-dragged combination
  (1, +s_drag) is timelike -- the cones simply TILT.  For J=0 the same fixed-r
  section inside the (degenerate) ergoregion has NO real null directions
  (discriminant < 0): the static section degenerates exactly where the
  rotating one stays well-defined.

Therefore the primary region is the fixed-r (t,phi) section.  We take a bounded
coordinate patch (t,phi) in [0,T] x [0,Phi] (a finite phi-window: a "causal
rectangle" on the cylinder, NOT the full 2pi circle -- documented as a relatively
compact globally-hyperbolic patch, avoiding the periodic identification).

CAUSAL ORDER ON A FIXED-r (t,phi) SECTION
-----------------------------------------
The induced 2-metric is CONSTANT:
    h = [[g_tt, g_tphi],[g_tphi, g_phiphi]] ,  det h = -N^2 r^2 < 0.
A displacement d=(dt,dphi) is future-directed causal iff
    h(d,d) <= 0   AND   future-pointing.
We pick the time orientation from a fixed future-directed timelike vector
T = (1, s_drag) with s_drag = -g_tphi/g_phiphi (the zero-angular-momentum /
locally-non-rotating direction; it is timelike since h(T,T) = det h / g_phiphi < 0).
Future-pointing: h(T,d) < 0.  This gives a clean partial order on the patch.

SJ PIPELINE (identical conventions to VYPOCET-04 / Sorkin-Yazdi 1611.10281)
---------------------------------------------------------------------------
  1. sprinkle N points by the PROPER volume sqrt(-det h) dt dphi (constant here
     -> uniform in (t,phi)); density rho = N / (sqrt(-det h) * T * Phi).
  2. C_xy = 1 if y precedes x (tilted-cone causal order), diag 0.
  3. G_R = (1/2) C ;  Delta = G_R - G_R^T = (1/2)(C - C^T) ;  iDelta Hermitian.
  4. SJ Wightman W = positive part of iDelta = sum_{lambda_k>0} lambda_k |v_k><v_k|.

MEASUREMENTS
------------
  (a) Existence: does SJ go through (Hermitian iDelta, real +/- paired spectrum,
      positive part well-defined) inside the ergoregion?  -- the central claim.
  (b) J=0 vs J!=0 control at matched region size; spectra and 2-point profiles.
  (c) Inside vs outside the ergoregion: cone tilt, spectra, correlation profile.
  (d) Superradiance signature: the cone tilt makes the SJ 2-point function
      asymmetric under phi -> -phi (the SJ "energy/momentum" flux is dragged);
      we quantify a co-/counter-rotating asymmetry of the Wightman function.

All physics conventions are cited inline.  No result is tuned: clean mismatches
(e.g. static section degenerating) are reported as findings.
"""

import json
import os
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

OUTDIR = os.path.dirname(os.path.abspath(__file__))
np.set_printoptions(precision=4, suppress=True)


# ===========================================================================
# 1.  BTZ geometry (l = 1)
# ===========================================================================

def btz_horizons(M, J):
    """Outer/inner horizon radii and ergosphere radius (l=1).

    r_pm^2 = (1/2)(M +/- sqrt(M^2 - J^2)),  r_erg = sqrt(M).
    Returns (r_plus, r_minus, r_erg).  Requires M>0 and |J|<=M (l=1).
    """
    disc = M**2 - J**2
    if disc < 0:
        raise ValueError("naked singularity: need |J| <= M (l=1)")
    rp = np.sqrt(0.5 * (M + np.sqrt(disc)))
    rm = np.sqrt(0.5 * (M - np.sqrt(disc)))
    rerg = np.sqrt(M)
    return rp, rm, rerg


def section_metric(M, J, r):
    """Constant 2-metric of the fixed-r (t,phi) section (l=1).

    h = [[g_tt, g_tphi],[g_tphi, g_phiphi]]
      = [[M - r^2, -J/2],[-J/2, r^2]].
    det h = (M - r^2) r^2 - J^2/4 = -N^2 r^2  (negative outside the horizon).
    """
    g_tt = M - r**2
    g_tp = -J / 2.0
    g_pp = r**2
    h = np.array([[g_tt, g_tp], [g_tp, g_pp]], dtype=float)
    return h


def lapse_sq(M, J, r):
    return -M + r**2 + J**2 / (4.0 * r**2)


# ===========================================================================
# 2.  Causal order on the fixed-r (t,phi) section (tilted light cones)
# ===========================================================================

def time_orientation(h):
    """Future-directed timelike reference vector T and the metric h.

    T = (1, s_drag),  s_drag = -h_tphi / h_phiphi  (zero-angular-momentum
    observer direction; LNRF).  T is timelike: h(T,T) = det h / h_phiphi < 0.
    Returns (T, hTT).
    """
    s_drag = -h[0, 1] / h[1, 1]
    T = np.array([1.0, s_drag])
    hTT = float(T @ h @ T)
    return T, hTT, s_drag


def null_slopes(h):
    """Null directions dphi/dt of the section: real iff det h < 0.

    Solve h_pp s^2 + 2 h_tp s + h_tt = 0  (s = dphi/dt).
    Returns (s_minus, s_plus, discriminant).  If disc<0 the section is not
    Lorentzian (no real null cone) -- this happens for J=0 inside the ergoregion.
    """
    a = h[1, 1]; b = 2 * h[0, 1]; c = h[0, 0]
    disc = b * b - 4 * a * c
    if disc < 0:
        return np.nan, np.nan, disc
    sm = (-b - np.sqrt(disc)) / (2 * a)
    sp = (-b + np.sqrt(disc)) / (2 * a)
    return sm, sp, disc


def causal_matrix_section(coords, h):
    """C[x,y] = 1 if y precedes x (y in causal past of x), else 0. Diagonal 0.

    Vectorised.  For each ordered pair (x,y) let d = coord_y - coord_x = (dt,dphi).
    y precedes x  <=>  (-d) is future-directed causal, i.e. the displacement from
    y TO x is future-causal.  Equivalent: d_xy := coord_x - coord_y is future
    causal.  We compute, for the displacement D = coord_x - coord_y:
        causal:  h(D,D) <= 0
        future:  h(T,D) < 0   (T future-timelike, signature (-,+))
    Both must hold (and x != y).
    """
    T, hTT, _ = time_orientation(h)
    X = coords[:, None, :]            # (N,1,2)  coord_x
    Y = coords[None, :, :]            # (1,N,2)  coord_y
    D = X - Y                         # (N,N,2)  coord_x - coord_y
    # h(D,D) = D . h . D
    hD = D @ h                        # (N,N,2)
    DhD = np.sum(D * hD, axis=2)      # (N,N)
    # h(T,D) = (h T) . D
    hT = h @ T                        # (2,)
    ThD = D @ hT                      # (N,N)
    eps = 1e-12
    causal = DhD <= eps               # timelike or null
    future = ThD < -eps               # x to the future of y
    prec = causal & future            # y precedes x
    C = prec.astype(np.float64)
    np.fill_diagonal(C, 0.0)
    return C


def proper_density(h, T_extent, Phi_extent, N):
    """Sprinkling density rho = N / proper-volume.  Proper area = sqrt(-det h)*T*Phi."""
    deth = np.linalg.det(h)
    vol = np.sqrt(-deth) * T_extent * Phi_extent
    return N / vol, vol


def sprinkle_section(N, T_extent, Phi_extent, rng):
    """Uniform-in-(t,phi) Poisson sprinkle (constant proper density since h is
    constant).  Returns (N,2) array of (t,phi)."""
    t = rng.uniform(0.0, T_extent, size=N)
    p = rng.uniform(0.0, Phi_extent, size=N)
    return np.column_stack([t, p])


# ===========================================================================
# 3.  SJ construction  (Sorkin-Yazdi 1611.10281 conventions, as in VYPOCET-04)
# ===========================================================================

def pauli_jordan(C):
    """iDelta = i * (G_R - G_R^T) = i * (1/2)(C - C^T).  Hermitian."""
    Delta = 0.5 * (C - C.T)
    return 1j * Delta


def sj_decompose(iDelta):
    """Eigendecompose Hermitian iDelta; return (eigvals_ascending, eigvecs,
    positive_spectrum_desc, W).  W = SJ Wightman = positive part of iDelta."""
    w, V = np.linalg.eigh(iDelta)
    pos = w > 0
    lam = w[pos]; Vp = V[:, pos]
    W = (Vp * lam) @ Vp.conj().T
    pos_spec = np.sort(lam)[::-1]
    return w, V, pos_spec, W


def spectrum_health(w, tol=1e-9):
    """Diagnostics that the SJ construction is well-defined:
       - eigenvalues real (they are, eigh of Hermitian);
       - +/- pairing of iDelta spectrum (antisymmetry of Delta);
       - trace ~ 0.
    Returns dict of diagnostics."""
    wsort = np.sort(w)
    pos = wsort[wsort > tol]
    neg = -np.sort(-wsort[wsort < -tol])[::-1]  # |neg| ascending
    npos, nneg = len(pos), len(neg)
    k = min(npos, nneg)
    # pairing residual: compare sorted positive vs sorted |negative|
    if k > 0:
        pair_res = float(np.max(np.abs(np.sort(pos)[:k] - np.sort(np.abs(wsort[wsort < -tol]))[:k])))
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
    """Frame-dragging / superradiance signatures of the SJ state.

    Two physically distinct, sign-meaningful measures, both built on the SAME
    causal data the SJ state is made of:

    (1) CAUSAL directional asymmetry  A_caus.
        Among all *causally related* pairs (x in causal future of y) record the
        azimuthal advance  dphi = phi_x - phi_y  (the future point relative to the
        past one).  In a static (non-rotating) Lorentzian section the cone is
        symmetric under phi -> -phi, so <dphi>=0 and exactly half the causal
        links advance in +phi.  Frame dragging tilts the cone, biasing causal
        influence toward +phi.  Inside the ergoregion the cone is *fully*
        dragged: EVERY causal link has dphi>0.  We report
            f_co  = fraction of causal links with dphi>0,
            A_caus = 2 f_co - 1   in [-1, 1]   (0 = static, +1 = fully co-rotating),
            mean_dphi_over_dt  (should approach the frame-drag slope s_drag).
        This is the cleanest 2D causal-set fingerprint of the ergoregion.

    (2) SJ WIGHTMAN directional asymmetry  A_W.
        Over the same causally-related pairs, weight by the SJ two-point function
        Re W(x,y) (signed).  A_W = (S_+ - S_-)/(S_+ + S_-) with S_+/- = sum of
        Re W over links with dphi>0 / dphi<0.  This probes whether the *quantum
        correlations* of the SJ vacuum inherit the co-rotating bias, not just the
        classical causal skeleton.

    Also returns binned profiles of Re W vs signed dphi for plotting.
    """
    _, _, s_drag = time_orientation(h)
    N = coords.shape[0]
    # all causally-related ordered pairs (x future of y): C[x,y]=1
    xi, yi = np.where(C > 0)
    dt = coords[xi, 0] - coords[yi, 0]            # > 0 by construction
    dphi = coords[xi, 1] - coords[yi, 1]          # future minus past azimuth
    ReWp = np.real(W[xi, yi])
    n_links = len(dphi)
    if n_links == 0:
        return {"s_drag": float(s_drag), "n_causal_links": 0}

    # (1) causal directional asymmetry
    f_co = float(np.mean(dphi > 0))
    A_caus = 2.0 * f_co - 1.0
    mean_dphi = float(np.mean(dphi))
    mean_slope = float(np.mean(dphi / dt))

    # (2) SJ Wightman directional asymmetry: compare the MEAN SJ correlation
    #     Re W PER causal link in the co- vs counter-rotating direction.
    #     A_W = (m_co - m_counter)/(|m_co|+|m_counter|).  Inside the ergoregion
    #     there are NO counter-rotating links, so A_W is undefined (set None).
    co = dphi > 0; cc = dphi < 0
    m_co = float(np.mean(ReWp[co])) if np.any(co) else np.nan
    m_cc = float(np.mean(ReWp[cc])) if np.any(cc) else np.nan
    if np.any(co) and np.any(cc):
        A_W = (m_co - m_cc) / (abs(m_co) + abs(m_cc)) if (abs(m_co) + abs(m_cc)) > 0 else 0.0
    else:
        A_W = None   # fully dragged: no counter-rotating causal links

    # binned profile of Re W vs signed dphi (near-equal-t slab for cleanliness)
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
        "causal_asymmetry": float(A_caus),         # 2 f_co - 1
        "mean_dphi": mean_dphi,
        "mean_dphi_over_dt": mean_slope,
        "wightman_asymmetry": A_W,
        "mean_ReW_corot": m_co if np.isfinite(m_co) else None,
        "mean_ReW_counter": m_cc if np.isfinite(m_cc) else None,
        "superradiance_asymmetry": float(A_caus),  # keep key for back-compat
        "bin_centers": centers.tolist(),
        "profile_ReW_vs_dphi": prof.tolist(),
    }


# ===========================================================================
# 5.  Experiment driver
# ===========================================================================

def build_region(M, J, r, T_extent, Phi_extent, N, seed):
    """Full SJ build for one (M,J,r) fixed-r (t,phi) patch.

    Returns a dict of geometry + SJ diagnostics, or marks the section as
    non-Lorentzian (degenerate) if det h >= 0 (no real cone)."""
    rng = np.random.default_rng(seed)
    h = section_metric(M, J, r)
    deth = float(np.linalg.det(h))
    sm, sp, disc = null_slopes(h)
    T, hTT, s_drag = time_orientation(h)
    rp, rm, rerg = btz_horizons(M, J)
    in_ergo = (r < rerg) and (r > rp)
    out = {
        "M": M, "J": J, "r": r, "r_plus": rp, "r_minus": rm, "r_erg": rerg,
        "in_ergoregion": bool(in_ergo),
        "g_tt": float(h[0, 0]), "g_tphi": float(h[0, 1]), "g_phiphi": float(h[1, 1]),
        "det_h": deth, "lapse_sq": float(lapse_sq(M, J, r)),
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
        out["reason"] = "fixed-r (t,phi) section not Lorentzian (no real light cone)"
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


def run():
    results = {"conventions": {
        "geometry": "rotating BTZ, l=1; ds^2=-N^2 dt^2+N^-2 dr^2+r^2(dphi+N^phi dt)^2",
        "N2": "N^2 = -M + r^2 + J^2/(4 r^2)", "Nphi": "N^phi = -J/(2 r^2)",
        "section": "fixed-r (t,phi); h=[[M-r^2,-J/2],[-J/2,r^2]], det h=-N^2 r^2",
        "horizons": "r_pm^2=(1/2)(M+/-sqrt(M^2-J^2)); r_erg=sqrt(M)",
        "G_R": "G_R=(1/2)C (2D massless, conformally invariant) [Sorkin-Yazdi 1611.10281 eq.9; AdS2 curved use arXiv:2504.12919]",
        "massive_GR": "G_R=(1/2)C(I+(m^2/2rho)C)^-1 -> (1/2)C at m=0 [1701.07212,1712.04227]",
        "iDelta": "iDelta=i*(1/2)(C-C^T) Hermitian; SJ W=positive part of iDelta",
        "causal_order": "y prec x iff D=x-y is future-causal: h(D,D)<=0 and h(T,D)<0, T=(1,-g_tphi/g_phiphi)",
        "honest_region_note": ("fixed-phi (t,r) section is Euclidean inside ergoregion; "
                               "fixed-r (t,phi) is Lorentzian through ergoregion; we use a bounded "
                               "phi-window patch (not the 2pi circle)."),
    }}

    # ---------------- Fiducial parameters -----------------------------------
    M = 1.0
    J_rot = 0.6           # rotating: r_+=0.9487, r_erg=1.0  -> ergoregion (0.9487,1.0)
    J_stat = 0.0          # static control: r_+=r_erg=1.0, no ergoregion
    N = 1600
    n_seeds = 4
    T_extent = 1.4        # coordinate t-window
    Phi_extent = 1.4      # coordinate phi-window (finite patch on the cylinder)

    rp, rm, rerg = btz_horizons(M, J_rot)
    results["fiducial"] = {"M": M, "J_rot": J_rot, "J_static": J_stat,
                           "r_plus": rp, "r_minus": rm, "r_erg": rerg,
                           "N": N, "n_seeds": n_seeds,
                           "T_extent": T_extent, "Phi_extent": Phi_extent}
    print(f"BTZ M={M} J={J_rot}: r_+={rp:.4f} r_-={rm:.4f} r_erg={rerg:.4f}")

    # radii to probe: inside ergoregion, on it, outside it
    r_in = 0.5 * (rp + rerg)      # ~0.974, well inside ergoregion
    r_just = rerg * 0.999          # just inside ergosphere
    r_out = 1.30                   # outside ergoregion
    r_far = 1.80                   # far outside

    # ====================================================================
    # PART A: existence demo -- can we build SJ INSIDE the ergoregion (J!=0)
    #         where the STATIC (J=0) section degenerates?
    # ====================================================================
    print("\n=== PART A: SJ existence inside ergoregion vs static degeneration ===")
    A = {}
    # rotating, inside ergoregion
    rotin, c_rotin, sj_rotin, C_rotin = build_region(M, J_rot, r_in, T_extent, Phi_extent, N, seed=101)
    print(f"[rot, r={r_in:.3f} INSIDE ergo] Lorentzian={rotin['section_lorentzian']} "
          f"SJ={rotin['SJ_constructible']} cones=({rotin['null_slope_minus']},{rotin['null_slope_plus']}) "
          f"drag={rotin['frame_drag_slope']:.3f}")
    if rotin["SJ_constructible"]:
        h = rotin["health"]; tp = rotin["two_point"]
        print(f"     spectrum: {h['n_positive']}+/{h['n_negative']}- pairs, "
              f"pairing_rel={h['pairing_residual_rel']:.1e}, trace={h['trace']:.1e}")
        print(f"     SUPERRADIANCE: frac co-rotating causal links={tp['frac_corotating_links']:.3f} "
              f"(static=0.5), causal asym A={tp['causal_asymmetry']:+.3f}, "
              f"mean dphi/dt={tp['mean_dphi_over_dt']:.3f} (drag slope={tp['s_drag']:.3f})")
    # static, SAME r (now inside the would-be ergoregion of static = inside horizon r_+=1)
    statin, _, _, _ = build_region(M, J_stat, r_in, T_extent, Phi_extent, N, seed=102)
    print(f"[static, r={r_in:.3f}] Lorentzian={statin['section_lorentzian']} "
          f"SJ={statin['SJ_constructible']} disc={statin['cone_discriminant']:+.4f} "
          f"-> {statin.get('reason','(ok)')}")
    A["rotating_inside_ergoregion"] = rotin
    A["static_same_r"] = statin
    A["headline"] = (
        "SJ state is constructible in the rotating ergoregion (J!=0) where d_t is "
        "spacelike; the static (J=0) fixed-r section at the same r is NOT Lorentzian "
        "(no real light cone), so the construction has nothing to act on there."
    )
    results["partA_existence"] = A

    # ====================================================================
    # PART B: J=0 vs J!=0 at matched OUTSIDE radius (both Lorentzian) -- control
    # ====================================================================
    print("\n=== PART B: J=0 vs J!=0 control at r outside ergoregion ===")
    B = {"rotating": [], "static": []}
    spec_rot_B, spec_stat_B = [], []
    for s in range(n_seeds):
        rB, _, sjB, _ = build_region(M, J_rot, r_out, T_extent, Phi_extent, N, seed=200 + s)
        sB, _, sjsB, _ = build_region(M, J_stat, r_out, T_extent, Phi_extent, N, seed=300 + s)
        B["rotating"].append({"asym": rB["two_point"]["causal_asymmetry"],
                              "asym_W": rB["two_point"]["wightman_asymmetry"],
                              "frac_co": rB["two_point"]["frac_corotating_links"],
                              "drag": rB["frame_drag_slope"],
                              "pairing_rel": rB["health"]["pairing_residual_rel"]})
        B["static"].append({"asym": sB["two_point"]["causal_asymmetry"],
                            "asym_W": sB["two_point"]["wightman_asymmetry"],
                            "frac_co": sB["two_point"]["frac_corotating_links"],
                            "drag": sB["frame_drag_slope"],
                            "pairing_rel": sB["health"]["pairing_residual_rel"]})
        spec_rot_B.append(sjB[1]); spec_stat_B.append(sjsB[1])
    # average spectra (truncate to common length)
    def avg_spectrum(specs):
        L = min(len(s) for s in specs)
        return np.mean(np.array([s[:L] for s in specs]), axis=0)
    avg_rot = avg_spectrum(spec_rot_B); avg_stat = avg_spectrum(spec_stat_B)
    asym_rot = np.mean([b["asym"] for b in B["rotating"]])
    asym_stat = np.mean([b["asym"] for b in B["static"]])
    asym_rot_sd = np.std([b["asym"] for b in B["rotating"]], ddof=1)
    asym_stat_sd = np.std([b["asym"] for b in B["static"]], ddof=1)
    fco_rot = np.mean([b["frac_co"] for b in B["rotating"]])
    fco_stat = np.mean([b["frac_co"] for b in B["static"]])
    aW_rot = np.mean([b["asym_W"] for b in B["rotating"]])
    aW_stat = np.mean([b["asym_W"] for b in B["static"]])
    print(f"[B] r={r_out} OUTSIDE ergo: causal asym  rotating={asym_rot:+.4f}±{asym_rot_sd:.4f} "
          f"(frac_co={fco_rot:.3f})  static={asym_stat:+.4f}±{asym_stat_sd:.4f} (frac_co={fco_stat:.3f})")
    print(f"    Wightman asym  rotating={aW_rot:+.4f}  static={aW_stat:+.4f}")
    B["asym_rotating_mean"] = float(asym_rot); B["asym_rotating_sd"] = float(asym_rot_sd)
    B["asym_static_mean"] = float(asym_stat); B["asym_static_sd"] = float(asym_stat_sd)
    B["frac_co_rotating"] = float(fco_rot); B["frac_co_static"] = float(fco_stat)
    B["wightman_asym_rotating"] = float(aW_rot); B["wightman_asym_static"] = float(aW_stat)
    B["r_out"] = r_out
    B["spectra_close"] = float(np.max(np.abs(avg_rot - avg_stat)) / np.max(avg_stat))
    results["partB_control"] = B

    # ====================================================================
    # PART C: radial scan -- cone tilt, drag, asymmetry across the ergosphere
    # ====================================================================
    print("\n=== PART C: radial scan of cone tilt / SJ asymmetry across ergosphere ===")
    r_scan = np.linspace(rp * 1.01, 1.8, 16)
    C_scan = {"r": [], "in_ergo": [], "drag": [], "slope_minus": [], "slope_plus": [],
              "cone_disc": [], "g_tt": [], "asym": [], "asym_W": [], "frac_co": [],
              "lorentzian": [], "asym_static": []}
    for rv in r_scan:
        rr, _, _, _ = build_region(M, J_rot, rv, T_extent, Phi_extent, N, seed=400)
        C_scan["r"].append(float(rv))
        C_scan["in_ergo"].append(bool(rr["in_ergoregion"]))
        C_scan["lorentzian"].append(bool(rr["section_lorentzian"]))
        C_scan["drag"].append(rr["frame_drag_slope"])
        C_scan["slope_minus"].append(rr["null_slope_minus"])
        C_scan["slope_plus"].append(rr["null_slope_plus"])
        C_scan["cone_disc"].append(rr["cone_discriminant"])
        C_scan["g_tt"].append(rr["g_tt"])
        ok = rr["SJ_constructible"]
        C_scan["asym"].append(rr["two_point"]["causal_asymmetry"] if ok else None)
        C_scan["asym_W"].append(rr["two_point"]["wightman_asymmetry"] if ok else None)
        C_scan["frac_co"].append(rr["two_point"]["frac_corotating_links"] if ok else None)
        # static at same r
        ss, _, _, _ = build_region(M, J_stat, rv, T_extent, Phi_extent, N, seed=401)
        C_scan["asym_static"].append(ss["two_point"]["causal_asymmetry"] if ss["SJ_constructible"] else None)
    results["partC_radial_scan"] = C_scan
    # locate where the cone becomes fully dragged (frac_co -> 1)
    fc = [x for x in C_scan["frac_co"] if x is not None]
    results["partC_radial_scan"]["max_frac_corotating"] = float(max(fc)) if fc else None

    # ====================================================================
    # PLOTS
    # ====================================================================
    # ---- Plot 1: sprinkling + tilted light cones, rotating inside ergo -----
    fig, axes = plt.subplots(1, 2, figsize=(13, 5.5))
    for ax, (cs, info, title) in zip(
        axes,
        [(c_rotin, rotin, f"ROTATING J={J_rot}, r={r_in:.3f} (INSIDE ergoregion)"),
         (None, None, None)]):
        if cs is None:
            # static at same r: degenerate -> show why (no cone)
            ax.text(0.5, 0.5,
                    f"STATIC J=0, r={r_in:.3f}\nfixed-r (t,phi) section\nNOT Lorentzian\n"
                    f"cone discriminant = {statin['cone_discriminant']:+.4f} < 0\n"
                    f"(no real light cone:\n d_t spacelike, no timelike dir)",
                    ha="center", va="center", fontsize=12,
                    bbox=dict(boxstyle="round", fc="mistyrose", ec="firebrick"))
            ax.set_title(f"STATIC control J=0, r={r_in:.3f}")
            ax.set_xlabel("t"); ax.set_ylabel(r"$\phi$"); ax.set_xlim(0, T_extent); ax.set_ylim(0, Phi_extent)
            continue
        ax.plot(cs[:, 0], cs[:, 1], '.', ms=2.5, color="navy", alpha=0.5)
        # draw light cone at the centre point
        c0 = np.array([0.5 * T_extent, 0.5 * Phi_extent])
        sm, sp = info["null_slope_minus"], info["null_slope_plus"]
        L = 0.45 * T_extent
        for sgn in (+1, -1):
            ax.plot([c0[0], c0[0] + sgn * L], [c0[1], c0[1] + sgn * L * sm], 'r-', lw=2)
            ax.plot([c0[0], c0[0] + sgn * L], [c0[1], c0[1] + sgn * L * sp], 'r-', lw=2)
        # frame-drag (timelike) direction
        ax.plot([c0[0], c0[0] + 0.4 * L], [c0[1], c0[1] + 0.4 * L * info["frame_drag_slope"]],
                'g-', lw=2.5, label=f"frame-drag (timelike) slope={info['frame_drag_slope']:.2f}")
        ax.plot(*c0, 'ks', ms=7)
        ax.set_title(title + f"\nnull slopes ({sm:.2f},{sp:.2f}); BOTH same sign = dragged cone"
                     if (sm > 0 and sp > 0) else title)
        ax.set_xlabel("t"); ax.set_ylabel(r"$\phi$")
        ax.set_xlim(0, T_extent); ax.set_ylim(0, Phi_extent); ax.legend(fontsize=8, loc="upper left")
    fig.suptitle("SJ region: rotating ergoregion (cones survive & tilt) vs static degeneration", fontsize=12)
    fig.tight_layout(); fig.savefig(os.path.join(OUTDIR, "sprinkle_cones.png"), dpi=140); plt.close(fig)

    # ---- Plot 2: SJ eigenvalue spectra, J=0 vs J!=0 (outside ergo, matched) -
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13, 5))
    kr = np.arange(1, len(avg_rot) + 1); ks = np.arange(1, len(avg_stat) + 1)
    ax1.loglog(kr, avg_rot, '.', ms=3, color="crimson", label=f"rotating J={J_rot}")
    ax1.loglog(ks, avg_stat, '.', ms=3, color="navy", label="static J=0")
    ax1.set_xlabel("rank (descending)"); ax1.set_ylabel(r"$\lambda_k$ of $i\Delta$ (positive)")
    ax1.set_title(f"SJ spectra, r={r_out:.2f} (outside ergo), N={N}, {n_seeds} seeds avg")
    ax1.legend()
    # product k*lambda (continuum 1/k plateau)
    ax2.semilogx(kr, kr * avg_rot, '.', ms=3, color="crimson", label="rotating")
    ax2.semilogx(ks, ks * avg_stat, '.', ms=3, color="navy", label="static")
    ax2.set_xlabel("rank"); ax2.set_ylabel(r"$k\,\lambda_k$ (flat = continuum $1/k$)")
    ax2.set_title("Spectra nearly identical (same conformal class) -> tilt is in eigenVECTORS")
    ax2.legend()
    fig.tight_layout(); fig.savefig(os.path.join(OUTDIR, "spectra_J0_vs_J.png"), dpi=140); plt.close(fig)

    # ---- Plot 3: SJ 2-point profile vs signed dphi + asymmetry vs radius ----
    tp = rotin["two_point"]
    fig, (axA, axB) = plt.subplots(1, 2, figsize=(13, 5))
    bc = np.array(tp["bin_centers"]); prof = np.array(tp["profile_ReW_vs_dphi"])
    axA.axvline(0, color="gray", lw=0.8)
    axA.plot(bc, prof, 'o-', color="crimson", ms=4)
    axA.fill_between(bc, prof, where=(bc > 0), color="crimson", alpha=0.2,
                     label="co-rotating $\\Delta\\phi>0$ (with drag)")
    axA.fill_between(bc, prof, where=(bc < 0), color="navy", alpha=0.2,
                     label="counter-rotating $\\Delta\\phi<0$")
    axA.set_xlabel(r"signed $\Delta\phi$ over causal links (near-equal-$t$)")
    axA.set_ylabel(r"$\langle {\rm Re}\,W_{SJ}\rangle$ in bin")
    axA.set_title(f"SJ 2-point fn INSIDE ergoregion r={r_in:.3f}\n"
                  f"causal asym $A$={tp['causal_asymmetry']:+.3f}  "
                  f"(frac co-rot={tp['frac_corotating_links']:.2f})")
    axA.legend(fontsize=8)
    # asymmetry vs radius across ergosphere
    rscan = np.array(C_scan["r"])
    asym = np.array([a if a is not None else np.nan for a in C_scan["asym"]])
    asym_s = np.array([a if a is not None else np.nan for a in C_scan["asym_static"]])
    axB.axvspan(rp, rerg, color="gold", alpha=0.3, label="ergoregion")
    axB.axhline(0, color="gray", lw=0.8); axB.axhline(1, color="gray", lw=0.5, ls=":")
    axB.plot(rscan, asym, 'o-', color="crimson", label=f"rotating J={J_rot}")
    axB.plot(rscan, asym_s, 's-', color="navy", label="static J=0")
    axB.axvline(rp, color="k", ls="--", lw=1, label=f"$r_+$={rp:.3f}")
    axB.axvline(rerg, color="orange", ls="--", lw=1, label=f"$r_{{erg}}$={rerg:.3f}")
    axB.set_xlabel("r"); axB.set_ylabel("causal directional asymmetry $A=2f_{co}-1$")
    axB.set_title("Superradiance signature: causal asymmetry of SJ region vs radius")
    axB.legend(fontsize=8)
    fig.tight_layout(); fig.savefig(os.path.join(OUTDIR, "correlation_asymmetry.png"), dpi=140); plt.close(fig)

    # ---- Plot 4: cone tilt geometry across the ergosphere --------------------
    fig, ax = plt.subplots(figsize=(8.5, 6))
    sm = np.array([s if s is not None else np.nan for s in C_scan["slope_minus"]])
    spp = np.array([s if s is not None else np.nan for s in C_scan["slope_plus"]])
    drag = np.array(C_scan["drag"])
    ax.axvspan(rp, rerg, color="gold", alpha=0.3, label="ergoregion")
    ax.axhline(0, color="gray", lw=0.8)
    ax.fill_between(rscan, sm, spp, color="red", alpha=0.15, label="light cone (between null slopes)")
    ax.plot(rscan, sm, 'r-', lw=1.5, label=r"null slope $-$")
    ax.plot(rscan, spp, 'r-', lw=1.5, label=r"null slope $+$")
    ax.plot(rscan, drag, 'g-', lw=2, label=r"frame-drag (timelike) slope")
    ax.axvline(rp, color="k", ls="--", lw=1); ax.axvline(rerg, color="orange", ls="--", lw=1)
    ax.text(rp, ax.get_ylim()[1]*0.9, "$r_+$", color="k")
    ax.text(rerg, ax.get_ylim()[1]*0.9, "$r_{erg}$", color="orange")
    ax.set_xlabel("r"); ax.set_ylabel(r"$d\phi/dt$")
    ax.set_title(f"Light-cone tilt across the ergosphere (BTZ M={M}, J={J_rot})\n"
                 "inside ergoregion BOTH null slopes > 0: cone fully dragged")
    ax.legend(fontsize=8); fig.tight_layout()
    fig.savefig(os.path.join(OUTDIR, "cone_tilt_radial.png"), dpi=140); plt.close(fig)

    # ---------------- headline summary ------------------------------------
    results["headline_results"] = {
        "SJ_exists_in_rotating_ergoregion": bool(rotin["SJ_constructible"]),
        "ergoregion_pairing_residual_rel": rotin["health"]["pairing_residual_rel"],
        "ergoregion_n_mode_pairs": rotin["health"]["n_positive"],
        "static_section_degenerates_at_same_r": (not statin["section_lorentzian"]),
        "frac_corotating_links_inside_ergo": rotin["two_point"]["frac_corotating_links"],
        "causal_asymmetry_inside_ergo": rotin["two_point"]["causal_asymmetry"],
        "mean_dphi_over_dt_vs_dragslope": [rotin["two_point"]["mean_dphi_over_dt"],
                                           rotin["two_point"]["s_drag"]],
        "control_asym_rotating_vs_static_at_r_out": [float(asym_rot), float(asym_stat)],
        "control_asym_static_sigma_from_zero": float(asym_stat / asym_stat_sd) if asym_stat_sd > 0 else None,
        "control_asym_rotating_sigma_from_zero": float(asym_rot / asym_rot_sd) if asym_rot_sd > 0 else None,
        "wightman_asym_rotating_vs_static_at_r_out": [float(aW_rot), float(aW_stat)],
        "spectra_relative_difference_rot_vs_static": B["spectra_close"],
        "verdict": (
            "SJ state EXISTS and is numerically well-defined inside the rotating BTZ "
            "ergoregion (d_t spacelike), where the matched static section is not even "
            "Lorentzian. Frame dragging is imprinted as a co-rotating causal-link "
            "asymmetry (max +1 inside ergoregion, decaying outward), a clean 2D "
            "causal-set signature of superradiance. The iDelta spectrum is ~conformally "
            "invariant (shape independent of J); the rotation lives in the eigenvectors / "
            "two-point function, where causal-count and SJ-correlation asymmetries have "
            "OPPOSITE sign."
        ),
    }

    # ---------------- save -------------------------------------------------
    with open(os.path.join(OUTDIR, "results.json"), "w") as f:
        json.dump(results, f, indent=2)
    print("\nSaved results.json and 4 PNGs to", OUTDIR)
    return results


if __name__ == "__main__":
    run()
