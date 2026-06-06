#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
VYPOCET-13 : SSEE on a 4D causal SLAB vs nested DIAMOND
=======================================================
Deciding between H04 interpretations (a) [2D-only cleanliness] and (c)
[volume law on diamonds = real signal of SJ non-Hadamardness at the corners].

The 4D nested-diamond SSEE gave a VOLUME law (VYPOCET-06).  The question:
is that the GEOMETRY's fault (diamond corners, where the SJ state is provably
non-Hadamard, arXiv:2212.10592) or genuinely a 4D problem?

TEST: change the region geometry at FIXED dimension.

(1) 4D causal SLAB: sprinkle into a box-like region {0<t<T, |x_i|<L}, T<<L,
    approximating a Rindler-like / half-space entangling surface.  Cut at
    x_1 > 0 (a flat half-space entangling surface, no corners).  Compute the
    SSEE of that half-space cut with the link-matrix iDelta (the validated
    object; VYPOCET-09 showed BD does not change the scaling).  Does the
    half-space cut give an AREA law where nested diamonds gave VOLUME?

(2) Same protocol in 2D as a control (slab vs diamond -- both should be clean,
    since the 2D SJ state is Hadamard in the interior).

(3) Hadamard diagnostic: measure the short-distance behaviour of the SJ
    Wightman W(x,y) along the entangling surface vs deep inside.  4D Minkowski
    Hadamard form for the massless scalar (spacelike):
        W(x,y) ~ 1/(4 pi^2 sigma),   sigma = (1/2)(Delta x)^2 > 0 spacelike.
    2D Hadamard form:  W(x,y) ~ -1/(4 pi) ln|sigma|.
    Does W have the Minkowski/Hadamard 1/sigma (4D) / ln (2D) form deep inside
    but anomalous behaviour near the diamond's corners?  Compare diamond vs
    slab.  (Corner anomaly localised at u-v'=+-2L etc, arXiv:2212.10592.)

OUTCOMES:
  slab AREA law + diamond corner anomaly  => (c) confirmed, geometry-specific:
      H04 hypothesis lives in 4D with the right region.
  slab also VOLUME                        => 4D problem is real, (a) wins.

Conventions verified against the literature
-------------------------------------------
* G_R (massless 4D) = a L, a = sqrt(rho)/(2 pi sqrt6); L = link matrix.
  (Johnston arXiv:0909.0944 eq.17 m=0; Nomaan-X/Dowker/Surya 1701.07212.)
* G_R (massless 2D) = (1/2) C, C the causal matrix.
  (Sorkin-Yazdi 1611.10281 eq.9.)
* iDelta = i(G_R - G_R^T) Hermitian; W = positive part of iDelta.
* SSEE generalized eigenproblem W_O v = mu iDelta_O v, S = sum mu ln|mu|.
  (Sorkin-Yazdi 1611.10281; Surya/Nomaan-X/Yazdi 2008.07697.)
* Double truncation by eigenvalue magnitude kappa (1712.04227).
* de Sitter SLAB + Rindler-like wedge gives AREA law after truncation
  (Surya/Nomaan-X/Yazdi 2008.07697); nested diamonds give VOLUME.
* SJ state on the 1+1D diamond is NON-Hadamard at the corners
  (u-v'=+-2L, v-u'=+-2L), Hadamard in the interior (Yazdi/Mathur/Surya
  arXiv:2212.10592; Mathur-Surya 1906.07952).
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


# ============================================================================
# GEOMETRY: sprinkling
# ============================================================================

def diamond_volume_4d(T):
    """4-volume of the 4D causal diamond {|t|+|r|<=T} = (2/3) pi T^4."""
    return (2.0 / 3.0) * np.pi * T**4


def sprinkle_diamond_4d(N, rng, T=1.0):
    """Poisson-sprinkle N points uniformly (Lebesgue) in {|t|+|r|<=T}.
    Exact sampling (no rejection): |t| with density ~ (T-|t|)^3 -> s=T U^{1/4};
    uniform point in the spatial ball of radius s.  (Same as VYPOCET-06.)"""
    N = int(N)
    U = rng.random(N)
    s = T * U**0.25
    sign = rng.choice([-1.0, 1.0], size=N)
    t = sign * (T - s)
    rmax = s
    dirs = rng.normal(size=(N, 3))
    dirs /= np.linalg.norm(dirs, axis=1, keepdims=True)
    V = rng.random(N)
    rr = rmax * V**(1.0 / 3.0)
    return np.column_stack([t, dirs * rr[:, None]])


def sprinkle_slab_4d(N, rng, T, L):
    """Poisson-sprinkle N points uniformly in the BOX-LIKE slab
        S = {0 < t < T,  |x_i| < L,  i=1,2,3},   T << L.
    4-volume = T (2L)^3.  This is the box itself (the 'slab' is the box; we do
    NOT carve the causal diamond out of it).  Lorentz-invariant Poisson process
    = uniform Lebesgue sprinkling.  Columns (t, x1, x2, x3).

    EDGE-EFFECT NOTE: a finite box is NOT a globally hyperbolic region with a
    nice Cauchy surface the way the diamond is; its causal structure is the
    Minkowski one restricted to the box, so points near the spatial faces
    |x_i|~L have a truncated causal past/future (boundary/edge effects).  We
    keep T<<L so that the t-direction (which sets the causal depth) is short
    and the half-space entangling surface x_1=0 sits far (~L) from the spatial
    faces -- this is the Rindler-like / half-space approximation.  Edge effects
    are quantified below by an interior-only control.
    """
    N = int(N)
    t = rng.random(N) * T
    x = (rng.random((N, 3)) * 2.0 - 1.0) * L
    return np.column_stack([t, x])


def sprinkle_diamond_2d(N, rng, T=1.0):
    """2D causal diamond in null coords (u,v)=(t+x,t-x), square [-T,T]^2.
    Returns columns (t, x). Vol_{(t,x)} = 2 T^2 (the (u,v) square area 4T^2
    has Jacobian 1/2)."""
    N = int(N)
    u = (rng.random(N) * 2.0 - 1.0) * T
    v = (rng.random(N) * 2.0 - 1.0) * T
    t = 0.5 * (u + v)
    x = 0.5 * (u - v)
    return np.column_stack([t, x])


def sprinkle_slab_2d(N, rng, T, L):
    """2D box-like slab {0<t<T, |x|<L}, T<<L.  Columns (t,x). Vol=2 T L."""
    N = int(N)
    t = rng.random(N) * T
    x = (rng.random(N) * 2.0 - 1.0) * L
    return np.column_stack([t, x])


# ============================================================================
# CAUSAL / LINK MATRICES, GREEN FUNCTIONS, PAULI-JORDAN  (validated objects)
# ============================================================================

def causal_matrix_4d(coords):
    """C[x,y]=1 iff y precedes x: (t_x-t_y) >= |r_x-r_y|, y!=x."""
    t = coords[:, 0]
    r = coords[:, 1:]
    dt = t[:, None] - t[None, :]
    r2 = np.einsum('ij,ij->i', r, r)
    d2 = r2[:, None] + r2[None, :] - 2.0 * (r @ r.T)
    np.maximum(d2, 0.0, out=d2)
    prec = (dt > 0) & (dt * dt >= d2)
    C = prec.astype(np.float64)
    np.fill_diagonal(C, 0.0)
    return C


def causal_matrix_2d(coords):
    """2D: y precedes x iff (t_x-t_y) >= |x_x-x_y|, y!=x."""
    t = coords[:, 0]
    x = coords[:, 1]
    dt = t[:, None] - t[None, :]
    dx = np.abs(x[:, None] - x[None, :])
    prec = (dt > 0) & (dt >= dx)
    C = prec.astype(np.float64)
    np.fill_diagonal(C, 0.0)
    return C


def link_matrix(C):
    """Transitive reduction: L = C AND (C@C == 0)."""
    C2 = C @ C
    return ((C > 0) & (C2 == 0)).astype(np.float64)


def green_retarded_4d(L, rho):
    """G_R = a L, a = sqrt(rho)/(2 pi sqrt6) (Johnston 0909.0944, m=0)."""
    a = np.sqrt(rho) / (2.0 * np.pi * np.sqrt(6.0))
    return a * L


def green_retarded_2d(C):
    """G_R = (1/2) C (Sorkin-Yazdi 1611.10281 eq.9)."""
    return 0.5 * C


def pauli_jordan(G_R):
    """iDelta = i(G_R - G_R^T), Hermitian, real +/- paired eigenvalues."""
    return 1j * (G_R - G_R.T)


def sj_wightman(iDelta):
    """SJ Wightman = positive part of iDelta. Returns (W, sorted-desc pos spec,
    full eigenvalues w, eigenvectors V)."""
    w, V = np.linalg.eigh(iDelta)
    pos = w > 0
    lam = w[pos]
    Vp = V[:, pos]
    W = (Vp * lam) @ Vp.conj().T
    return W, np.sort(lam)[::-1], w, V


# ============================================================================
# SSEE with double truncation (dimension-independent, validated algorithm)
# ============================================================================

def ssee(W, iDelta, sub_idx, kappa=None, tol=1e-9):
    """SSEE for sub-region sub_idx, double eigenvalue-magnitude truncation kappa.
    Returns (S, n_modes_kept)."""
    iD = iDelta
    Wm = W
    if kappa is not None:
        w, V = np.linalg.eigh(iD)
        keep = np.abs(w) > kappa
        wk = w[keep]; Vk = V[:, keep]
        iD = (Vk * wk) @ Vk.conj().T
        pos = wk > 0
        Wm = (Vk[:, pos] * wk[pos]) @ Vk[:, pos].conj().T

    iD_O = iD[np.ix_(sub_idx, sub_idx)]
    W_O = Wm[np.ix_(sub_idx, sub_idx)]
    d, U = np.linalg.eigh(iD_O)
    scale = np.max(np.abs(d)) if d.size else 0.0
    if scale == 0.0:
        return 0.0, 0
    local_cut = kappa if kappa is not None else tol * scale
    keep = np.abs(d) > local_cut
    if keep.sum() == 0:
        return 0.0, 0
    d_k = d[keep]; U_k = U[:, keep]
    Wproj = U_k.conj().T @ W_O @ U_k
    M = (Wproj.T / d_k).T
    mu = np.linalg.eigvals(M).real
    good = (np.abs(mu) > tol) & (np.abs(mu - 1.0) > tol)
    mu_g = mu[good]
    S = float(np.sum(mu_g * np.log(np.abs(mu_g))))
    return S, int(good.sum())


# ============================================================================
# Area / volume diagnostics for a sub-region scan
# ============================================================================

def r2(y, yhat):
    y = np.asarray(y, float)
    ss = np.sum((y - y.mean())**2)
    return 1.0 - np.sum((y - yhat)**2) / ss if ss > 0 else 0.0


def area_vs_volume(S, area, vol):
    """Linear fits S ~ a*area+b and S ~ a*vol+b; return R2s and verdict."""
    S = np.asarray(S, float); area = np.asarray(area, float); vol = np.asarray(vol, float)
    Aa = np.vstack([area, np.ones_like(area)]).T
    Av = np.vstack([vol, np.ones_like(vol)]).T
    (ba, ca), *_ = np.linalg.lstsq(Aa, S, rcond=None)
    (bv, cv), *_ = np.linalg.lstsq(Av, S, rcond=None)
    r2a = r2(S, Aa @ [ba, ca]); r2v = r2(S, Av @ [bv, cv])
    return {"R2_area": float(r2a), "R2_vol": float(bv and r2v or r2v),
            "beta_area": float(ba), "beta_vol": float(bv),
            "verdict": "AREA" if r2a > r2v else "VOLUME"}


def powerlaw_fit(x, y):
    lx = np.log(np.asarray(x, float)); ly = np.log(np.asarray(y, float))
    A = np.vstack([lx, np.ones_like(lx)]).T
    coef, *_ = np.linalg.lstsq(A, ly, rcond=None)
    yhat = A @ coef
    return float(coef[0]), float(coef[1]), float(r2(ly, yhat))


# ============================================================================
# HADAMARD DIAGNOSTIC
# ============================================================================
# For the *real symmetric part* of the SJ Wightman, Re W(x,y), we measure the
# short-distance behaviour as a function of the invariant spacelike interval
#       sigma2 = (1/2)[ (Delta x)^2 - (Delta t)^2 ]  > 0  (spacelike)
# binned in |Delta x|.  Continuum Minkowski Hadamard predictions (massless):
#   4D:  Re W ~  1/(4 pi^2) * 1/(2 sigma2) = 1/(4 pi^2 s^2),  s=spacelike dist.
#        i.e. log|ReW| ~ -2 log s + const  (power -2).
#   2D:  Re W ~ -1/(4 pi) ln|s| + const    (logarithmic).
# We compare the EXPONENT (4D) / the LOG SLOPE (2D) measured (i) deep inside
# the region and (ii) along the entangling surface / near the corner.  An
# anomaly = the inside fit matches Minkowski but the corner/surface fit does
# NOT (different power / extra term).  We do diamond vs slab.
# ============================================================================

def hadamard_profile_4d(coords, ReW, ref_idx, dist_bins, max_pairs=400000, rng=None):
    """Bin Re W over spacelike pairs (i in ref_idx, all j) by spatial distance.
    Returns (centers, mean|ReW|, count) for spacelike-separated pairs."""
    if rng is None:
        rng = np.random.default_rng(0)
    t = coords[:, 0]; r = coords[:, 1:]
    refs = np.asarray(ref_idx)
    # subsample reference points if too many pairs
    npairs = len(refs) * coords.shape[0]
    if npairs > max_pairs:
        keep = rng.choice(len(refs), size=max(1, max_pairs // coords.shape[0]),
                          replace=False)
        refs = refs[keep]
    ds, ws = [], []
    for i in refs:
        dt = t[i] - t
        dr = r[i] - r
        sp = np.sqrt(np.einsum('ij,ij->i', dr, dr))    # spatial distance
        s2 = sp**2 - dt**2                              # spacelike if >0
        m = s2 > 1e-12
        ds.append(sp[m]); ws.append(np.abs(ReW[i, m]))
    ds = np.concatenate(ds); ws = np.concatenate(ws)
    centers, meanw, cnt = _bin(ds, ws, dist_bins)
    return centers, meanw, cnt


def hadamard_profile_2d(coords, ReW, ref_idx, dist_bins, max_pairs=400000, rng=None):
    if rng is None:
        rng = np.random.default_rng(0)
    t = coords[:, 0]; x = coords[:, 1]
    refs = np.asarray(ref_idx)
    npairs = len(refs) * coords.shape[0]
    if npairs > max_pairs:
        keep = rng.choice(len(refs), size=max(1, max_pairs // coords.shape[0]),
                          replace=False)
        refs = refs[keep]
    ds, ws = [], []
    for i in refs:
        dt = t[i] - t
        dx = np.abs(x[i] - x)
        s2 = dx**2 - dt**2
        m = s2 > 1e-12
        ds.append(dx[m]); ws.append(np.abs(ReW[i, m]))
    ds = np.concatenate(ds); ws = np.concatenate(ws)
    return _bin(ds, ws, dist_bins)


def _bin(d, w, bins):
    idx = np.digitize(d, bins)
    centers = 0.5 * (bins[:-1] + bins[1:])
    meanw = np.full(len(centers), np.nan)
    cnt = np.zeros(len(centers), int)
    for k in range(1, len(bins)):
        m = idx == k
        cnt[k - 1] = m.sum()
        if m.sum() > 0:
            meanw[k - 1] = np.mean(w[m])
    return centers, meanw, cnt


def fit_loglog_slope(centers, meanw, cnt, dmin, dmax, mincount=30):
    """Fit log|ReW| ~ slope*log(d)+c over [dmin,dmax] (4D: expect slope=-2)."""
    m = (centers >= dmin) & (centers <= dmax) & (cnt >= mincount) & np.isfinite(meanw) & (meanw > 0)
    if m.sum() < 3:
        return None, None, None
    lx = np.log(centers[m]); ly = np.log(meanw[m])
    A = np.vstack([lx, np.ones_like(lx)]).T
    coef, *_ = np.linalg.lstsq(A, ly, rcond=None)
    return float(coef[0]), float(coef[1]), float(r2(ly, A @ coef))


def fit_log_slope_2d(centers, meanw, cnt, dmin, dmax, mincount=30):
    """Fit |ReW| ~ slope*ln(d)+c over [dmin,dmax] (2D: expect slope=-1/4pi)."""
    m = (centers >= dmin) & (centers <= dmax) & (cnt >= mincount) & np.isfinite(meanw)
    if m.sum() < 3:
        return None, None, None
    lx = np.log(centers[m]); y = meanw[m]
    A = np.vstack([lx, np.ones_like(lx)]).T
    coef, *_ = np.linalg.lstsq(A, y, rcond=None)
    return float(coef[0]), float(coef[1]), float(r2(y, A @ coef))


# ============================================================================
# PART 1: 4D SLAB half-space cut vs DIAMOND nested cut -- AREA vs VOLUME
# ============================================================================

def part1_slab_4d(results):
    print("\n==== PART 1: 4D causal SLAB half-space cut ====")
    # Slab geometry.  T<<L.  Half-space cut x_1>0.  We vary the SUB-REGION by
    # restricting the cut to a finite slab strip 0<x_1<W (so the entangling
    # surface area scales with the transverse extent) and ALSO by the simple
    # half-space; both reported.  Area of the entangling surface x_1=0 inside
    # the box = T * (2L)^2 (the (t,x2,x3) face).  Volume of the cut half =
    # half the box.  To get a SCAN we vary L at fixed density and fixed T:
    # the half-space SSEE should scale with the entangling-surface AREA
    # A = T*(2L)^2 (area law) NOT with the half-volume V=T*(2L)^3/2 (volume).
    #
    # Crucially area ~ L^2 and volume ~ L^3, so a clean log-log fit S vs L
    # discriminates: AREA => slope 2, VOLUME => slope 3.
    # Calibration note (documented honestly): the slab's local causal depth is
    # set by T, so the link density per point ~ (rho)*(local diamond 4-vol ~T^4).
    # The strict T<<L limit at finite density gives a NEARLY ACAUSAL slab
    # (links/pt -> 0, e.g. T=0.2,L=1 -> 0.5 links/pt): the field theory becomes
    # trivial and the SSEE has too few modes (an honest sparsity/edge effect).
    # We therefore use a WIDE-but-causal slab: T fixed at a value giving a
    # healthy link density (~8 links/pt), and L > T so the entangling surface
    # x_1=0 is a FLAT plane (NO corners) -- the key geometric contrast with the
    # diamond.  T<<L is documented as the (unreachable-at-finite-density) ideal.
    T = 0.50
    Ls = [0.65, 0.75, 0.85, 0.95]   # N from ~1200 to ~3800 (eigh-feasible)
    rho_target = 1100.0     # density fixed across L (so N ~ L^3, vol scaling)
    n_seeds = 3
    kappa_frac = 0.05       # double-truncation at 5% lambda_max (as VYPOCET-06)

    per_L = {}
    S_mean, S_std, areas, vols, Ns = [], [], [], [], []
    for L in Ls:
        vol = T * (2.0 * L)**3
        N = int(round(rho_target * vol))
        area_ent = T * (2.0 * L)**2          # face x_1=0 area (t,x2,x3)
        vol_half = 0.5 * vol
        Svals = []
        nmodes = []
        for s in range(n_seeds):
            rng = np.random.default_rng(1000 * int(L * 100) + s + 1)
            coords = sprinkle_slab_4d(N, rng, T, L)
            rho = N / vol
            C = causal_matrix_4d(coords)
            Lk = link_matrix(C)
            iD = pauli_jordan(green_retarded_4d(Lk, rho))
            W, sp, _, _ = sj_wightman(iD)
            kappa = kappa_frac * sp[0]
            sub = np.where(coords[:, 1] > 0.0)[0]    # half-space x_1>0
            S, nm = ssee(W, iD, sub, kappa=kappa)
            Svals.append(S); nmodes.append(nm)
        Sm = float(np.mean(Svals)); Ss = float(np.std(Svals, ddof=1))
        S_mean.append(Sm); S_std.append(Ss)
        areas.append(area_ent); vols.append(vol_half); Ns.append(N)
        per_L[f"L={L}"] = {"N": N, "rho": N / vol, "area_ent": area_ent,
                           "vol_half": vol_half, "S_seeds": Svals,
                           "S_mean": Sm, "S_std": Ss, "modes": nmodes}
        print(f"  L={L:.2f} N={N:5d} S={Sm:8.3f}+/-{Ss:6.3f}  "
              f"A={area_ent:.3f} Vhalf={vol_half:.3f} modes~{int(np.mean(nmodes))}")

    # fits: S vs L (slope) and area/volume R2
    pL, _, r2L = powerlaw_fit(Ls, np.abs(S_mean))
    av = area_vs_volume(S_mean, areas, vols)
    # also S vs area power and S vs vol power
    pA, _, r2A = powerlaw_fit(areas, np.abs(S_mean))
    pV, _, r2V = powerlaw_fit(vols, np.abs(S_mean))
    print(f"  [4D slab] S ~ L^{pL:.2f} (R2={r2L:.3f}); area-law=>2, volume-law=>3")
    print(f"  [4D slab] S vs area R2={av['R2_area']:.3f}  S vs vol R2={av['R2_vol']:.3f}"
          f"  -> {av['verdict']}")

    results["part1_slab_4d"] = {
        "geometry": "box slab {0<t<T,|x_i|<L}, T<<L; half-space cut x_1>0",
        "T": T, "Ls": Ls, "rho_target": rho_target, "n_seeds": n_seeds,
        "kappa_frac": kappa_frac, "per_L": per_L,
        "S_mean": S_mean, "S_std": S_std, "areas": areas, "vols_half": vols, "Ns": Ns,
        "fit_S_vs_L": {"slope": pL, "R2": r2L,
                       "area_law_slope": 2.0, "volume_law_slope": 3.0},
        "fit_S_vs_area_pow": {"p": pA, "R2": r2A},
        "fit_S_vs_vol_pow": {"p": pV, "R2": r2V},
        "area_vs_volume": av,
        "edge_note": ("T<<L keeps entangling surface x_1=0 far from spatial "
                      "faces |x_i|~L; box has truncated causal past/future near "
                      "faces (edge effects). Interior-only control in part1b."),
    }
    return T, Ls, rho_target


def part1b_slab_interior_control(results, T, Ls, rho_target):
    """Edge-effect control: restrict the half-space cut to an INTERIOR strip
    0<x_1<L/2 AND |x_2|,|x_3|<L/2 (away from the box faces), so the entangling
    surface and the cut volume sit deep inside the box.  If the verdict is the
    same as the full half-space, edge effects are not driving it."""
    print("\n==== PART 1b: 4D slab interior-only control (edge effects) ====")
    n_seeds = 2          # control check (fewer seeds; main result is part1)
    kappa_frac = 0.05
    S_mean, areas, vols = [], [], []
    per_L = {}
    for L in Ls:
        vol = T * (2.0 * L)**3
        N = int(round(rho_target * vol))
        Svals = []
        for s in range(n_seeds):
            rng = np.random.default_rng(2000 * int(L * 100) + s + 7)
            coords = sprinkle_slab_4d(N, rng, T, L)
            rho = N / vol
            C = causal_matrix_4d(coords)
            Lk = link_matrix(C)
            iD = pauli_jordan(green_retarded_4d(Lk, rho))
            W, sp, _, _ = sj_wightman(iD)
            kappa = kappa_frac * sp[0]
            # interior strip: keep transverse |x2|,|x3| away from the box faces
            # (cut at 0.7L), and x_1>0 -> flat entangling surface deep inside.
            interior = (np.abs(coords[:, 2]) < 0.7 * L) & (np.abs(coords[:, 3]) < 0.7 * L)
            sub = np.where(interior & (coords[:, 1] > 0.0))[0]
            S, _ = ssee(W, iD, sub, kappa=kappa)
            Svals.append(S)
        Sm = float(np.mean(Svals))
        area_ent = T * (1.4 * L)**2          # interior face x_1=0, |x2,x3|<0.7L -> side 1.4L
        vol_half = 0.5 * T * (1.4 * L)**2 * L  # interior cut volume
        S_mean.append(Sm); areas.append(area_ent); vols.append(vol_half)
        per_L[f"L={L}"] = {"N": N, "S_mean": Sm, "area_ent": area_ent,
                           "vol_half": vol_half}
        print(f"  L={L:.2f} N={N:5d} S_interior={Sm:8.3f} A={area_ent:.3f}")
    pL, _, r2L = powerlaw_fit(Ls, np.abs(S_mean))
    av = area_vs_volume(S_mean, areas, vols)
    print(f"  [4D slab interior] S ~ L^{pL:.2f} (R2={r2L:.3f}) -> {av['verdict']}")
    results["part1b_slab_4d_interior"] = {
        "S_mean": S_mean, "areas": areas, "vols_half": vols,
        "fit_S_vs_L": {"slope": pL, "R2": r2L},
        "area_vs_volume": av,
    }


def part1c_diamond_4d_reference(results):
    """Reference: 4D nested DIAMOND, concentric sub-diamond scan (reproduces
    VYPOCET-06 volume law) with the SAME truncation, for a head-to-head with
    the slab.  Vary sub-diamond fraction f at fixed N."""
    print("\n==== PART 1c: 4D nested DIAMOND reference (volume law check) ====")
    N = 2500
    kappa_frac = 0.05
    rng = np.random.default_rng(909090)
    T = 1.0
    coords = sprinkle_diamond_4d(N, rng, T)
    vol = diamond_volume_4d(T); rho = N / vol
    C = causal_matrix_4d(coords)
    Lk = link_matrix(C)
    iD = pauli_jordan(green_retarded_4d(Lk, rho))
    W, sp, _, _ = sj_wightman(iD)
    kappa = kappa_frac * sp[0]
    fracs = [0.40, 0.45, 0.50, 0.55, 0.60, 0.65]
    S_d, area_d, vol_d, nsub = [], [], [], []
    tt = np.abs(coords[:, 0]); rr = np.linalg.norm(coords[:, 1:], axis=1)
    for f in fracs:
        sub = np.where(tt + rr <= f * T)[0]
        S, _ = ssee(W, iD, sub, kappa=kappa)
        S_d.append(S); area_d.append(4.0 * np.pi * (f * T)**2)
        vol_d.append(diamond_volume_4d(f * T)); nsub.append(len(sub))
    av = area_vs_volume(S_d, area_d, nsub)   # vol ~ n_sub (point count)
    pA, _, r2A = powerlaw_fit(fracs, np.abs(S_d))
    print(f"  [4D diamond] S~f^{pA:.2f} (area=>2, vol=>6); "
          f"R2_area={av['R2_area']:.3f} R2_vol={av['R2_vol']:.3f} -> {av['verdict']}")
    results["part1c_diamond_4d_ref"] = {
        "N": N, "fracs": fracs, "S": S_d, "area": area_d, "vol": vol_d,
        "n_sub": nsub, "S_powerlaw_in_f": pA, "area_vs_volume": av,
    }


# ============================================================================
# PART 2: 2D control -- slab vs diamond (both should be CLEAN)
# ============================================================================

def part2_2d_control(results):
    print("\n==== PART 2: 2D control (slab vs diamond) ====")
    kappa_of_N = lambda N: np.sqrt(N) / (4.0 * np.pi)   # 2D entropy cutoff
    n_seeds = 3

    # --- 2D SLAB: half-line cut x>0, scan L (area in 2D = #boundary pts ~ const
    #     so 'area law' in 1+1 is a LOG/CONST law; volume ~ L).  We instead test
    #     S vs L: 2D area law => S ~ const or log L; volume => S ~ L.
    T = 0.30
    Ls = [0.8, 1.1, 1.5, 1.9, 2.3]
    rho_target = 2500.0
    S_slab, Ns_slab = [], []
    for L in Ls:
        vol = 2.0 * T * L
        N = int(round(rho_target * vol))
        Svals = []
        for s in range(n_seeds):
            rng = np.random.default_rng(3000 * int(L * 100) + s + 3)
            coords = sprinkle_slab_2d(N, rng, T, L)
            C = causal_matrix_2d(coords)
            iD = pauli_jordan(green_retarded_2d(C))
            W, sp, _, _ = sj_wightman(iD)
            kappa = kappa_of_N(N)
            sub = np.where(coords[:, 1] > 0.0)[0]
            S, _ = ssee(W, iD, sub, kappa=kappa)
            Svals.append(S)
        S_slab.append(float(np.mean(Svals))); Ns_slab.append(N)
        print(f"  2D slab L={L:.2f} N={N:5d} S={np.mean(Svals):.3f}")
    pL_slab, _, r2_slab = powerlaw_fit(Ls, np.abs(S_slab))
    # log fit S ~ a ln L + b (2D area law for a half-line is log)
    A = np.vstack([np.log(Ls), np.ones(len(Ls))]).T
    coef_log, *_ = np.linalg.lstsq(A, np.array(S_slab), rcond=None)
    r2_log = r2(S_slab, A @ coef_log)
    print(f"  [2D slab] S~L^{pL_slab:.2f} (R2={r2_slab:.3f}); "
          f"S~{coef_log[0]:.3f}lnL+{coef_log[1]:.3f} (R2_log={r2_log:.3f})")

    # --- 2D DIAMOND: concentric sub-diamond scan (VYPOCET-04 regime; clean
    #     log/area law after truncation) ---
    N = 2400
    rng = np.random.default_rng(424243)
    coords = sprinkle_diamond_2d(N, rng, 1.0)
    C = causal_matrix_2d(coords)
    iD = pauli_jordan(green_retarded_2d(C))
    W, sp, _, _ = sj_wightman(iD)
    kappa = kappa_of_N(N)
    fracs = [0.40, 0.50, 0.60, 0.70, 0.80]
    u = coords[:, 0] + coords[:, 1]; v = coords[:, 0] - coords[:, 1]
    S_dia = []
    for f in fracs:
        sub = np.where((np.abs(u) <= f) & (np.abs(v) <= f))[0]
        S, _ = ssee(W, iD, sub, kappa=kappa)
        S_dia.append(S)
    A2 = np.vstack([np.log(fracs), np.ones(len(fracs))]).T
    coef_d, *_ = np.linalg.lstsq(A2, np.array(S_dia), rcond=None)
    r2_d_log = r2(S_dia, A2 @ coef_d)
    pf_d, _, r2_d_pow = powerlaw_fit(fracs, np.abs(S_dia))
    print(f"  [2D diamond] S~{coef_d[0]:.3f}ln(f)+{coef_d[1]:.3f} "
          f"(R2_log={r2_d_log:.3f}); S~f^{pf_d:.2f}")

    results["part2_2d_control"] = {
        "slab": {"T": T, "Ls": Ls, "Ns": Ns_slab, "S": S_slab,
                 "fit_S_vs_L_pow": {"p": pL_slab, "R2": r2_slab},
                 "fit_S_vs_lnL": {"a": float(coef_log[0]), "b": float(coef_log[1]),
                                  "R2": float(r2_log)},
                 "note": "2D half-line area law is logarithmic; volume law would be S~L"},
        "diamond": {"N": N, "fracs": fracs, "S": S_dia,
                    "fit_S_vs_lnf": {"a": float(coef_d[0]), "b": float(coef_d[1]),
                                     "R2": float(r2_d_log)},
                    "fit_S_vs_f_pow": {"p": pf_d, "R2": r2_d_pow}},
    }


# ============================================================================
# PART 3: HADAMARD DIAGNOSTIC -- W short-distance form, inside vs corner/surface
# ============================================================================

def part3_hadamard(results):
    print("\n==== PART 3: Hadamard diagnostic (W short-distance) ====")

    # ---------- 4D DIAMOND ----------
    N = 2800
    rng = np.random.default_rng(13131)
    T = 1.0
    coords = sprinkle_diamond_4d(N, rng, T)
    vol = diamond_volume_4d(T); rho = N / vol
    C = causal_matrix_4d(coords); Lk = link_matrix(C)
    iD = pauli_jordan(green_retarded_4d(Lk, rho))
    W, sp, _, _ = sj_wightman(iD)
    ReW = np.real(W)
    tt = np.abs(coords[:, 0]); rr = np.linalg.norm(coords[:, 1:], axis=1)
    radial = tt + rr               # 0 center .. T corner (null boundary)
    # deep inside: small radial; corner: near the null boundary tip (t~+-T)
    inside_idx = np.where(radial < 0.35 * T)[0]
    # corner = points near the tips (|t| large, r small) where SJ is non-Hadamard
    corner_idx = np.where((np.abs(coords[:, 0]) > 0.80 * T) & (rr < 0.25 * T))[0]
    # distance bins (4D): typical NN spacing ell ~ (1/rho)^{1/4}
    ell = rho**(-0.25)
    dbins = np.linspace(2 * ell, 0.5 * T, 22)
    c_in, w_in, n_in = hadamard_profile_4d(coords, ReW, inside_idx, dbins, rng=rng)
    c_co, w_co, n_co = hadamard_profile_4d(coords, ReW, corner_idx, dbins, rng=rng)
    fit_in = fit_loglog_slope(c_in, w_in, n_in, 3 * ell, 0.30 * T)
    fit_co = fit_loglog_slope(c_co, w_co, n_co, 3 * ell, 0.30 * T)
    print(f"  4D diamond: inside slope={fit_in[0]} (Mink=-2)  "
          f"corner slope={fit_co[0]}  (ell={ell:.4f})")

    # ---------- 4D SLAB ----------
    Ts = 0.50; Ls = 1.00
    vol_s = Ts * (2 * Ls)**3
    Ns = int(round(1100.0 * vol_s))
    rng2 = np.random.default_rng(14141)
    coords_s = sprinkle_slab_4d(Ns, rng2, Ts, Ls)
    rho_s = Ns / vol_s
    C_s = causal_matrix_4d(coords_s); Lk_s = link_matrix(C_s)
    iD_s = pauli_jordan(green_retarded_4d(Lk_s, rho_s))
    W_s, sp_s, _, _ = sj_wightman(iD_s)
    ReW_s = np.real(W_s)
    # inside the slab: deep (away from all faces); 'surface' = near entangling
    # plane x_1=0 (the flat half-space cut, NO corner)
    deep = ((np.abs(coords_s[:, 1]) < 0.5 * Ls) & (np.abs(coords_s[:, 2]) < 0.5 * Ls)
            & (np.abs(coords_s[:, 3]) < 0.5 * Ls)
            & (coords_s[:, 0] > 0.25 * Ts) & (coords_s[:, 0] < 0.75 * Ts))
    deep_idx = np.where(deep)[0]
    surf = ((np.abs(coords_s[:, 1]) < 0.15 * Ls)   # near x_1=0 plane
            & (np.abs(coords_s[:, 2]) < 0.5 * Ls) & (np.abs(coords_s[:, 3]) < 0.5 * Ls))
    surf_idx = np.where(surf)[0]
    ell_s = rho_s**(-0.25)
    dbins_s = np.linspace(2 * ell_s, 0.6 * Ls, 22)
    c_d, w_d, n_d = hadamard_profile_4d(coords_s, ReW_s, deep_idx, dbins_s, rng=rng2)
    c_su, w_su, n_su = hadamard_profile_4d(coords_s, ReW_s, surf_idx, dbins_s, rng=rng2)
    fit_d = fit_loglog_slope(c_d, w_d, n_d, 3 * ell_s, 0.5 * Ls)
    fit_su = fit_loglog_slope(c_su, w_su, n_su, 3 * ell_s, 0.5 * Ls)
    print(f"  4D slab: deep slope={fit_d[0]} (Mink=-2)  "
          f"flat-surface slope={fit_su[0]}  (ell={ell_s:.4f})")

    # ---------- 2D DIAMOND (corner is the analytically known anomaly site) ----
    N2 = 2500
    rng3 = np.random.default_rng(15151)
    cc2 = sprinkle_diamond_2d(N2, rng3, 1.0)
    C2 = causal_matrix_2d(cc2)
    iD2 = pauli_jordan(green_retarded_2d(C2))
    W2, sp2, _, _ = sj_wightman(iD2)
    ReW2 = np.real(W2)
    u2 = cc2[:, 0] + cc2[:, 1]; v2 = cc2[:, 0] - cc2[:, 1]
    rad2 = np.abs(u2) + np.abs(v2)   # not exactly; use max(|u|,|v|)
    cheb = np.maximum(np.abs(u2), np.abs(v2))
    inside2 = np.where(cheb < 0.4)[0]
    # corner = near a spatial tip: |x| large, |t| small => |u|~|v|~1 same sign?
    # left/right corners: u~+-1 AND v~-+1 (the u-v'=+-2L sites). Take x near +-1.
    corner2 = np.where(np.abs(cc2[:, 1]) > 0.80)[0]
    ell2 = np.sqrt(2.0 / N2)        # 2D spacing ~ (Vol/N)^{1/2}, Vol=2
    dbins2 = np.linspace(2 * ell2, 0.5, 22)
    c2i, w2i, n2i = hadamard_profile_2d(cc2, ReW2, inside2, dbins2, rng=rng3)
    c2c, w2c, n2c = hadamard_profile_2d(cc2, ReW2, corner2, dbins2, rng=rng3)
    fit2i = fit_log_slope_2d(c2i, w2i, n2i, 3 * ell2, 0.4)
    fit2c = fit_log_slope_2d(c2c, w2c, n2c, 3 * ell2, 0.4)
    print(f"  2D diamond: inside log-slope={fit2i[0]} (Mink=-1/4pi={-1/(4*np.pi):.4f})  "
          f"corner log-slope={fit2c[0]}")

    results["part3_hadamard"] = {
        "predictions": {
            "4D_Hadamard": "ReW ~ 1/(4 pi^2 s^2) spacelike => loglog slope -2",
            "2D_Hadamard": "ReW ~ -1/(4 pi) ln s => log-slope -1/(4pi)=%.4f" % (-1/(4*np.pi)),
            "non_Hadamard_site": "diamond corners (u-v'=+-2L), Yazdi/Mathur/Surya 2212.10592",
        },
        "diamond_4d": {
            "N": N, "ell": ell,
            "inside": {"centers": c_in.tolist(), "ReW": np.nan_to_num(w_in).tolist(),
                       "count": n_in.tolist(),
                       "slope": fit_in[0], "R2": fit_in[2]},
            "corner": {"centers": c_co.tolist(), "ReW": np.nan_to_num(w_co).tolist(),
                       "count": n_co.tolist(),
                       "slope": fit_co[0], "R2": fit_co[2]},
        },
        "slab_4d": {
            "N": Ns, "ell": ell_s,
            "deep": {"centers": c_d.tolist(), "ReW": np.nan_to_num(w_d).tolist(),
                     "count": n_d.tolist(), "slope": fit_d[0], "R2": fit_d[2]},
            "flat_surface": {"centers": c_su.tolist(), "ReW": np.nan_to_num(w_su).tolist(),
                             "count": n_su.tolist(), "slope": fit_su[0], "R2": fit_su[2]},
        },
        "diamond_2d": {
            "N": N2, "ell": ell2,
            "inside": {"centers": c2i.tolist(), "ReW": np.nan_to_num(w2i).tolist(),
                       "count": n2i.tolist(), "slope": fit2i[0], "R2": fit2i[2]},
            "corner": {"centers": c2c.tolist(), "ReW": np.nan_to_num(w2c).tolist(),
                       "count": n2c.tolist(), "slope": fit2c[0], "R2": fit2c[2]},
        },
    }
    # plot data stashed for plotting
    return {
        "d4_dia": (c_in, w_in, fit_in, c_co, w_co, fit_co),
        "d4_slab": (c_d, w_d, fit_d, c_su, w_su, fit_su),
        "d2_dia": (c2i, w2i, fit2i, c2c, w2c, fit2c),
    }


# ============================================================================
# PLOTS
# ============================================================================

def make_plots(results, had):
    # Plot 1: 4D slab S vs L (area vs volume slope)
    p1 = results["part1_slab_4d"]
    Ls = np.array(p1["Ls"], float); S = np.abs(np.array(p1["S_mean"]))
    Sstd = np.array(p1["S_std"])
    fig, ax = plt.subplots(figsize=(7.5, 6))
    ax.errorbar(Ls, S, yerr=Sstd, fmt='o', ms=8, capsize=4, color='tab:blue',
                label=f"4D slab half-space: S~L^{p1['fit_S_vs_L']['slope']:.2f}")
    xx = np.linspace(Ls.min(), Ls.max(), 50)
    a2 = S[0] / Ls[0]**2; a3 = S[0] / Ls[0]**3
    ax.plot(xx, a2 * xx**2, 'k--', lw=1.5, label="area law slope 2 (L^2)")
    ax.plot(xx, a3 * xx**3, 'r:', lw=1.5, label="volume law slope 3 (L^3)")
    # interior control
    if "part1b_slab_4d_interior" in results:
        Si = np.abs(np.array(results["part1b_slab_4d_interior"]["S_mean"]))
        ax.plot(Ls, Si, 's', ms=7, color='tab:green', alpha=0.7,
                label=f"interior-only: S~L^{results['part1b_slab_4d_interior']['fit_S_vs_L']['slope']:.2f}")
    ax.set_xscale('log'); ax.set_yscale('log')
    ax.set_xlabel("slab transverse half-extent L"); ax.set_ylabel("|SSEE| S")
    ax.set_title("4D causal SLAB half-space cut: AREA(2) vs VOLUME(3)")
    ax.legend(fontsize=8); fig.tight_layout()
    fig.savefig(os.path.join(PLOTDIR, "slab4d_area_vs_volume.png"), dpi=140)
    plt.close(fig)

    # Plot 2: 4D slab vs diamond head to head (S vs sub-region size, normalized)
    p1c = results["part1c_diamond_4d_ref"]
    fig, ax = plt.subplots(figsize=(7.5, 6))
    fr = np.array(p1c["fracs"]); Sd = np.abs(np.array(p1c["S"]))
    ax.plot(fr, Sd / Sd[0], 'o-', color='tab:red',
            label=f"4D DIAMOND nested: S~f^{p1c['S_powerlaw_in_f']:.1f} ({p1c['area_vs_volume']['verdict']})")
    # slab scaled by L
    ax.plot(Ls / Ls[0] * fr[0] / (Ls[0] / Ls[0]), np.nan * Ls, ' ')  # spacer
    ax.plot(fr, (fr / fr[0])**2, 'k--', label="area f^2")
    ax.plot(fr, (fr / fr[0])**6, 'b:', label="volume f^6 (4D diamond)")
    ax.set_yscale('log')
    ax.set_xlabel("sub-region linear fraction f"); ax.set_ylabel("S / S(f0)")
    ax.set_title("4D nested DIAMOND: volume law (reference, VYPOCET-06)")
    ax.legend(fontsize=8); fig.tight_layout()
    fig.savefig(os.path.join(PLOTDIR, "diamond4d_reference.png"), dpi=140)
    plt.close(fig)

    # Plot 3: 2D control
    p2 = results["part2_2d_control"]
    fig, (axa, axb) = plt.subplots(1, 2, figsize=(13, 5.5))
    Ls2 = np.array(p2["slab"]["Ls"]); S2 = np.array(p2["slab"]["S"])
    axa.plot(Ls2, S2, 'o-', color='tab:blue', label="2D slab half-line")
    lnf = p2["slab"]["fit_S_vs_lnL"]
    axa.plot(Ls2, lnf["a"] * np.log(Ls2) + lnf["b"], 'g--',
             label=f"S~{lnf['a']:.2f}lnL+{lnf['b']:.2f} (R2={lnf['R2']:.2f})")
    axa.plot(Ls2, S2[0] / Ls2[0] * Ls2, 'r:', label="volume law S~L")
    axa.set_xlabel("L"); axa.set_ylabel("S"); axa.set_title("2D SLAB control")
    axa.legend(fontsize=8)
    frd = np.array(p2["diamond"]["fracs"]); Sd2 = np.array(p2["diamond"]["S"])
    axb.plot(frd, Sd2, 'o-', color='tab:red', label="2D diamond nested")
    cd = p2["diamond"]["fit_S_vs_lnf"]
    axb.plot(frd, cd["a"] * np.log(frd) + cd["b"], 'g--',
             label=f"S~{cd['a']:.2f}ln(f)+{cd['b']:.2f} (R2={cd['R2']:.2f})")
    axb.set_xlabel("sub-diamond fraction f"); axb.set_ylabel("S")
    axb.set_title("2D DIAMOND control"); axb.legend(fontsize=8)
    fig.tight_layout(); fig.savefig(os.path.join(PLOTDIR, "control_2d.png"), dpi=140)
    plt.close(fig)

    # Plot 4: Hadamard diagnostic (4D diamond/slab, 2D diamond)
    fig, axs = plt.subplots(1, 3, figsize=(16, 5))
    # 4D diamond
    c_in, w_in, fit_in, c_co, w_co, fit_co = had["d4_dia"]
    axs[0].loglog(c_in, w_in, 'o', color='tab:blue', label=f"inside (slope {fit_in[0]:.2f})")
    axs[0].loglog(c_co, w_co, 's', color='tab:red', label=f"corner/tip (slope {fit_co[0]:.2f})")
    xr = np.array([c_in[np.isfinite(w_in)][0], c_in[np.isfinite(w_in)][-1]])
    w0 = w_in[np.isfinite(w_in)][0]
    axs[0].loglog(xr, w0 * (xr / xr[0])**(-2), 'k--', label="Minkowski slope -2")
    axs[0].set_title("4D DIAMOND: |ReW| vs spacelike dist")
    axs[0].set_xlabel("spatial distance"); axs[0].set_ylabel("|ReW|"); axs[0].legend(fontsize=7)
    # 4D slab
    c_d, w_d, fit_d, c_su, w_su, fit_su = had["d4_slab"]
    axs[1].loglog(c_d, w_d, 'o', color='tab:blue', label=f"deep (slope {fit_d[0]:.2f})")
    axs[1].loglog(c_su, w_su, 's', color='tab:green', label=f"flat surface (slope {fit_su[0]:.2f})")
    fin = np.isfinite(w_d)
    xr2 = np.array([c_d[fin][0], c_d[fin][-1]]); w0d = w_d[fin][0]
    axs[1].loglog(xr2, w0d * (xr2 / xr2[0])**(-2), 'k--', label="Minkowski slope -2")
    axs[1].set_title("4D SLAB: |ReW| vs spacelike dist (flat surface, no corner)")
    axs[1].set_xlabel("spatial distance"); axs[1].set_ylabel("|ReW|"); axs[1].legend(fontsize=7)
    # 2D diamond (semilog)
    c2i, w2i, fit2i, c2c, w2c, fit2c = had["d2_dia"]
    axs[2].semilogx(c2i, w2i, 'o', color='tab:blue', label=f"inside (logslope {fit2i[0]:.3f})")
    axs[2].semilogx(c2c, w2c, 's', color='tab:red', label=f"corner (logslope {fit2c[0]:.3f})")
    fin2 = np.isfinite(w2i)
    axs[2].semilogx(c2i[fin2], -1/(4*np.pi)*np.log(c2i[fin2]) + (w2i[fin2][0] + 1/(4*np.pi)*np.log(c2i[fin2][0])),
                    'k--', label="Minkowski -1/4pi ln")
    axs[2].set_title("2D DIAMOND: |ReW| vs spacelike dist (log axis)")
    axs[2].set_xlabel("spatial distance"); axs[2].set_ylabel("|ReW|"); axs[2].legend(fontsize=7)
    fig.tight_layout(); fig.savefig(os.path.join(PLOTDIR, "hadamard_diagnostic.png"), dpi=140)
    plt.close(fig)


# ============================================================================
def run():
    t0 = time.time()
    results = {"task": "VYPOCET-13 SSEE 4D slab vs diamond; Hadamard diagnostic",
               "conventions": {
                   "G_R_4D": "a L, a=sqrt(rho)/(2 pi sqrt6) (Johnston 0909.0944 m=0)",
                   "G_R_2D": "(1/2) C (Sorkin-Yazdi 1611.10281)",
                   "iDelta": "i(G_R-G_R^T); W=positive part",
                   "SSEE": "W_O v=mu iDelta_O v; S=sum mu ln|mu| (1611.10281;2008.07697)",
                   "truncation_4D": "double mag cutoff kappa=0.05 lambda_max (1712.04227)",
                   "truncation_2D": "kappa=sqrt(N)/(4 pi) (1712.04227)",
                   "validated_object": "link-matrix iDelta; BD does not change scaling (VYPOCET-09)",
                   "literature": {
                       "slab_area_law": "de Sitter slab+Rindler wedge => area law (2008.07697)",
                       "diamond_volume": "nested diamonds => volume law (2008.07697;1712.04227)",
                       "SJ_non_Hadamard_corner": "1+1D diamond SJ non-Hadamard at corners (2212.10592)",
                       "caveat": "2412.07832 / dS paper: EE behaviour and non-Hadamard likely NOT directly connected",
                   },
               }}

    T, Ls, rho_t = part1_slab_4d(results)
    part1b_slab_interior_control(results, T, Ls, rho_t)
    part1c_diamond_4d_reference(results)
    part2_2d_control(results)
    had = part3_hadamard(results)
    make_plots(results, had)

    results["runtime_s"] = time.time() - t0
    with open(os.path.join(OUTDIR, "results.json"), "w") as f:
        json.dump(results, f, indent=2)
    print(f"\nDone in {results['runtime_s']:.1f}s. results.json + plots in {OUTDIR}")
    return results


if __name__ == "__main__":
    run()
