#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
SSEE on a sprinkled 4D causal diamond  (Sorkin-Johnston prescription)
=====================================================================

VYPOCET-06: decisive follow-up of VYPOCET-04 (2D).  We test the AREA-LAW
prediction for the entropy-cutoff rank:

      rank_at_kappa  ~  N^{(d-1)/d}

In 2D (VYPOCET-04) we measured p = 0.519 +/- 0.007, i.e. p = 1/2 = (d-1)/d.
Here d=4, so the PREDICTION UNDER TEST is

      p = 3/4 = 0.75      (vs 2D's 1/2)

and, secondarily, whether the double-truncated SSEE obeys an area law
S ~ A/ell^2 with A the area of the equatorial 2-sphere of the sub-diamond.

Conventions verified against the literature
-------------------------------------------
* S. Johnston, "Feynman Propagator for a Free Scalar Field on a Causal Set",
  arXiv:0909.0944 (PRL 103, 180401 (2009)):
    - Retarded Green function of the *massless* scalar on a 4D causal set is
      proportional to the LINK matrix L (transitive reduction of the causal
      relation), eq. (17) in the m=0 limit:
          K_R^{(4)} = a L ,   a = sqrt(rho) / (2 pi sqrt(6)).
      The link matrix L_xy = 1 iff x is a *nearest-neighbour* (covering
      relation) cause of y: x precedes y and no w with x < w < y.
    - 2D: K_R^{(2)} = (1/2) C  (causal matrix, no density factor) -- the
      convention used in VYPOCET-04.
    - High-density limit:  sqrt(rho/6) <L_0(x,x')> -> theta(x0-x0') delta(tau^2)
      = 2 pi G_0^{(4)}(x,x'),  i.e.  G_R^{(4)} = (1/2pi) sqrt(rho/6) L.
      (Nomaan X, Dowker, Surya, "Scalar Field Green Functions on Causal Sets",
       arXiv:1701.07212, eq. (17); spectral-geometry review arXiv:1611.09947.)

* Sorkin-Johnston construction (dimension-independent), as in VYPOCET-04
  (Sorkin & Yazdi arXiv:1611.10281; Surya, Nomaan X, Yazdi arXiv:2008.07697):
    - Pauli-Jordan operator  iDelta = i (G_R - G_R^T),  Hermitian, real +/-
      paired eigenvalues.
    - SJ Wightman  W = positive part of iDelta.
    - SSEE generalized eigenproblem  W_O v = mu (iDelta_O) v,  S = sum mu ln|mu|.
    - Double truncation by eigenvalue magnitude kappa (1712.04227) to remove
      sub-discreteness modes and restore the area law.

* Entropy / area-law cutoff scaling (Surya, Nomaan X, Yazdi arXiv:2008.07697):
    n_max = alpha N^{(d-1)/d};  d=4 -> N^{3/4}.  This is the AREA LAW we test.

UV eigenvalue cutoff kappa in 4D
--------------------------------
In 2D the entropy cutoff is kappa = sqrt(N)/(4 pi) (1712.04227).  The cited
literature does not give a clean closed-form kappa for the 4D *diamond* SSEE,
so we DO NOT hard-code a 2D-style formula.  Instead we use the dimension-
independent, geometry-agnostic definition of the entropy cutoff that the
area-law ansatz fixes: keep the n_max largest-|lambda| modes with

      n_max = number of modes on the continuum 1/k^? plateau,

operationalised as the eigenvalue-magnitude knee.  Crucially, for the SCALING
test we measure the rank at a FIXED FRACTION of the spectral plateau (a
self-calibrating, density-independent magnitude cutoff) and check its
N-scaling.  We report the exponent for several cutoff definitions so the
conclusion does not hinge on one arbitrary constant.  See find_* below.
"""

import json
import os
import time
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

OUTDIR = os.path.dirname(os.path.abspath(__file__))

# ----------------------------------------------------------------------------
# 4D causal-diamond geometry.
#
# Minkowski coords x = (t, rx, ry, rz), signature (-,+,+,+).  The causal
# diamond between tips (-T,0,0,0) and (+T,0,0,0) is
#       D = { x : |t| + |r| <= T },   r = sqrt(rx^2+ry^2+rz^2).
# Sprinkling uniformly in the Lebesgue measure dt d^3r over D is the (Lorentz
# invariant) Poisson process.  Its 4-volume:
#       Vol(D) = pi/3 * T^4 / 2 ... computed below exactly.
# A point y precedes x  (y in causal past of x)  iff
#       (t_x - t_y) >= |r_x - r_y|     (timelike-or-null, future-directed).
# Density rho = N / Vol(D).
#
# CONCENTRIC sub-diamond of linear size f: D_f = { |t| + |r| <= f*T }, the
# causal diamond between (-fT,0,..) and (+fT,0,..) sharing the centre.  Its
# equatorial bifurcation 2-surface is the sphere t=0, |r|=fT, of area
#       A(f) = 4 pi (f T)^2.
# An area law for the SSEE reads  S ~ A(f)/ell^2 ~ (f T)^2.
# ----------------------------------------------------------------------------

T_HALF = 1.0   # null/time half-extent of the big diamond (tip at t=+/-T_HALF)


def diamond_volume(T):
    """4-volume of the 4D causal diamond {|t|+|r|<=T}.
    Integral over t in [-T,T] of (4/3) pi (T-|t|)^3 dt = (4/3) pi * 2 * T^4/4
    = (2/3) pi T^4.  (Two cones base-to-base; each cone volume (1/3) area*height
    integrated -> standard result (2/3) pi T^4 for the bicone.)"""
    return (2.0 / 3.0) * np.pi * T**4


VOL_4D = diamond_volume(T_HALF)   # = (2/3) pi for T=1


def sprinkle_diamond_4d(N, rng, T=T_HALF):
    """Poisson-sprinkle N points uniformly (Lebesgue) in the 4D diamond
    {|t|+|r|<=T}.  Returns array (N,4): columns (t,rx,ry,rz).

    Rejection sampling from the bounding box t in [-T,T], r-box [-T,T]^3 is
    very wasteful (acceptance ~ Vol/(2T)^4 = (2/3)pi/16 ~ 0.13... times the
    fraction with |r|<=T-|t|).  We sample exactly instead:
      1. pick |t| with density proportional to the spatial-ball volume
         (4/3)pi (T-|t|)^3, i.e. CDF ~ 1-(1-|t|/T)^4 on each side;
      2. pick a point uniformly in the spatial ball of radius (T-|t|).
    N fixed (canonical approximation); density rho = N/Vol.
    """
    N = int(N)
    # 1. sample t.  Let s = T-|t| in (0,T], weight ~ s^3.  pdf(s) ~ s^3 ->
    #    CDF(s) = (s/T)^4, so s = T * U^{1/4}; sign of t is +/- with p=1/2.
    U = rng.random(N)
    s = T * U**0.25                     # = T - |t|
    sign = rng.choice([-1.0, 1.0], size=N)
    t = sign * (T - s)
    rmax = s                            # spatial ball radius at this t
    # 2. uniform point in ball of radius rmax: direction isotropic, radius
    #    with pdf ~ r^2 -> r = rmax * V^{1/3}.
    dirs = rng.normal(size=(N, 3))
    dirs /= np.linalg.norm(dirs, axis=1, keepdims=True)
    V = rng.random(N)
    rr = rmax * V**(1.0 / 3.0)
    space = dirs * rr[:, None]
    coords = np.column_stack([t, space])
    return coords


def causal_matrix_4d(coords):
    """C[x,y] = 1 if y precedes x (y in causal past of x), else 0. Diagonal 0.

    y precedes x  <=>  (t_x - t_y) >= |r_x - r_y|  and  y != x.
    Vectorised with numpy broadcasting.  For N up to a few thousand this is an
    N x N float build; the dominant cost downstream is the link matrix matmul
    and the eigendecomposition.
    """
    t = coords[:, 0]
    r = coords[:, 1:]
    dt = t[:, None] - t[None, :]                 # t_x - t_y
    # squared spatial distance via Gram trick (faster, less memory churn)
    r2 = np.einsum('ij,ij->i', r, r)
    d2 = r2[:, None] + r2[None, :] - 2.0 * (r @ r.T)
    np.maximum(d2, 0.0, out=d2)
    prec = (dt > 0) & (dt * dt >= d2)            # strictly future + causal
    C = prec.astype(np.float64)
    np.fill_diagonal(C, 0.0)
    return C


def link_matrix(C):
    """Transitive reduction (covering relation) of the causal matrix.

    L[x,y] = 1 iff y precedes x (C[x,y]=1) and there is NO intermediate w with
    y < w < x, i.e. no w with C[x,w]=1 and C[w,y]=1.  The count of such
    intermediates is (C @ C)[x,y].  Hence

        L = C  AND  (C @ C == 0).

    C @ C is a boolean-style matmul over the float C (entries = #2-step paths).
    Vectorised; this matmul is the runtime bottleneck (O(N^3)).
    """
    C2 = C @ C                       # (C2)[x,y] = number of length-2 chains x<-w<-y
    L = ((C > 0) & (C2 == 0)).astype(np.float64)
    return L


def green_retarded_4d(L, rho):
    """Massless 4D retarded Green function on the causal set (Johnston):
        K_R = a L,   a = sqrt(rho) / (2 pi sqrt(6)).
    (arXiv:0909.0944 eq.17 m=0; 1701.07212; 1611.09947.)
    """
    a = np.sqrt(rho) / (2.0 * np.pi * np.sqrt(6.0))
    return a * L


def pauli_jordan(G_R):
    """iDelta = i (G_R - G_R^T), Hermitian. Real eigenvalues in +/- pairs."""
    Delta = G_R - G_R.T
    return 1j * Delta


def sj_wightman(iDelta):
    """SJ Wightman = positive part of iDelta. Returns (W, sorted-desc positive
    eigenvalues of iDelta)."""
    w, V = np.linalg.eigh(iDelta)
    pos = w > 0
    lam = w[pos]
    Vp = V[:, pos]
    W = (Vp * lam) @ Vp.conj().T
    pos_spec = np.sort(lam)[::-1]
    return W, pos_spec


def points_in_subdiamond_4d(coords, frac, T=T_HALF):
    """Indices inside the CONCENTRIC sub-diamond {|t|+|r| <= frac*T}."""
    t = np.abs(coords[:, 0])
    r = np.linalg.norm(coords[:, 1:], axis=1)
    return np.where(t + r <= frac * T)[0]


def subdiamond_area(frac, T=T_HALF):
    """Area of the equatorial 2-sphere of the sub-diamond: A = 4 pi (fT)^2."""
    return 4.0 * np.pi * (frac * T)**2


# ----------------------------------------------------------------------------
# SSEE with double truncation (dimension independent; identical algorithm to
# VYPOCET-04).
# ----------------------------------------------------------------------------

def ssee(W, iDelta, sub_idx, kappa=None, tol=1e-9):
    """SSEE for sub-region sub_idx, double eigenvalue-magnitude truncation kappa.
    Returns (S, mu_values)."""
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
        return 0.0, np.array([])
    local_cut = kappa if kappa is not None else tol * scale
    keep = np.abs(d) > local_cut
    if keep.sum() == 0:
        return 0.0, np.array([])
    d_k = d[keep]; U_k = U[:, keep]
    Wproj = U_k.conj().T @ W_O @ U_k
    M = (Wproj.T / d_k).T
    mu = np.linalg.eigvals(M).real
    good = (np.abs(mu) > tol) & (np.abs(mu - 1.0) > tol)
    mu_g = mu[good]
    S = float(np.sum(mu_g * np.log(np.abs(mu_g))))
    return S, mu


# ----------------------------------------------------------------------------
# Spectral knee / cutoff-rank estimators (same family as VYPOCET-04).
#
# In the continuum the massless iDelta eigenvalues fall off as a power law in
# rank; the product P_k = k * lambda_k forms a plateau (2D) or a smooth curve
# whose departure from the continuum marks the discreteness knee.  For the
# AREA-LAW (entropy) cutoff we use a SELF-CALIBRATING magnitude cutoff: keep
# modes with lambda > c * lambda_typ, where lambda_typ is a robust spectral
# scale (the plateau median).  This is density-independent by construction, so
# its N-scaling directly probes (d-1)/d without importing a 2D-only constant.
# ----------------------------------------------------------------------------

def _plateau_value(pos_spec, lo=3, hi_frac=0.10):
    n = len(pos_spec)
    hi = max(lo + 3, int(hi_frac * n))
    P = np.arange(1, n + 1, dtype=float) * pos_spec
    return float(np.median(P[lo:hi])), P


def rank_at_magnitude(pos_spec, kappa):
    """# positive eigenvalues of iDelta above magnitude cutoff kappa."""
    return int(np.sum(pos_spec > kappa))


def rank_at_frac_of_max(pos_spec, frac):
    """Self-calibrating cutoff: rank where lambda_k > frac * lambda_max.
    Density-independent magnitude cutoff (lambda_max sets the scale)."""
    if len(pos_spec) == 0:
        return 0
    return int(np.sum(pos_spec > frac * pos_spec[0]))


def find_knee(pos_spec, tol=0.10, lo=3, hi_frac=0.10):
    """Intrinsic discreteness knee: 1-based rank where P_k=k*lambda_k first
    drops `tol` below the continuum plateau A.  Interpolated."""
    n = len(pos_spec)
    if n < 8:
        return float(n)
    A, P = _plateau_value(pos_spec, lo, hi_frac)
    thresh = (1.0 - tol) * A
    below = np.where(P[lo:] < thresh)[0]
    if below.size == 0:
        return float(n)
    j = below[0] + lo
    if j >= 1 and P[j - 1] != P[j]:
        f = (P[j - 1] - thresh) / (P[j - 1] - P[j])
        return (j - 1) + 1 + f
    return float(j + 1)


def find_knee_slope(pos_spec, delta=0.15, win=8, lo=3):
    """Literature 'knee' (Surya, Nomaan X, Yazdi arXiv:2008.07697, sec 2.4):
    the rank where the local log-log slope of lambda_k vs k drops (steepens)
    by a fractional amount `delta = (m - m')/m` below its plateau value m.

    We compute smoothed local slopes m_k = d ln(lambda)/d ln(k), take the
    plateau slope as the median over the early stable region, and return the
    first rank where the smoothed slope falls below (1+delta)*m_plateau (more
    negative -> steeper).  Returns the 1-based knee rank.
    """
    n = len(pos_spec)
    if n < 4 * win:
        return float(n)
    lk = np.log(np.arange(1, n + 1, dtype=float))
    ll = np.log(np.maximum(pos_spec, 1e-300))
    # smoothed local slope via moving linear fit over a window
    m = np.full(n, np.nan)
    half = win // 2
    for k in range(half, n - half):
        xs = lk[k - half:k + half + 1]
        ys = ll[k - half:k + half + 1]
        m[k] = np.polyfit(xs, ys, 1)[0]
    valid = ~np.isnan(m)
    # plateau slope: median over an early stable band (ranks ~ [lo, 0.15 n])
    band_hi = max(lo + win, int(0.15 * n))
    m_plat = np.median(m[lo:band_hi][~np.isnan(m[lo:band_hi])])
    # knee: slope steepens past (1+delta)*m_plat (m_plat is negative)
    thresh = (1.0 + delta) * m_plat
    cand = np.where(valid & (np.arange(n) > band_hi) & (m < thresh))[0]
    if cand.size == 0:
        return float(n)
    return float(cand[0] + 1)


def ssee_rank_truncated(W, iDelta, sub_idx, n_max, tol=1e-9):
    """SSEE with literature-faithful fixed-RANK double truncation
    (Surya, Nomaan X, Yazdi arXiv:2008.07697, eq.15):

      1. GLOBAL: keep the n_max LARGEST-|lambda| eigenvalues of iDelta, zero the
         rest; rebuild W as the positive part of the truncated iDelta.
      2. Restrict to the sub-region.
      3. LOCAL: keep the n_max largest-|lambda| eigenvalues of the restricted
         iDelta_O (or all if it has fewer than n_max non-kernel modes).
      4. Generalized eigenproblem, S = sum mu ln|mu|.

    n_max is the number of POSITIVE+NEGATIVE pairs?  Following the paper we cut
    the spectrum of iDelta (which has +/- pairs) keeping the n_max largest by
    magnitude; since they come in pairs this keeps ~n_max/2 positive modes.
    Here n_max counts kept eigenvalues of iDelta total.
    """
    w, V = np.linalg.eigh(iDelta)
    order = np.argsort(-np.abs(w))           # descending |lambda|
    keepg = order[:min(n_max, len(w))]
    wg = w[keepg]; Vg = V[:, keepg]
    iD = (Vg * wg) @ Vg.conj().T
    posg = wg > 0
    Wm = (Vg[:, posg] * wg[posg]) @ Vg[:, posg].conj().T

    iD_O = iD[np.ix_(sub_idx, sub_idx)]
    W_O = Wm[np.ix_(sub_idx, sub_idx)]
    d, U = np.linalg.eigh(iD_O)
    scale = np.max(np.abs(d)) if d.size else 0.0
    if scale == 0.0:
        return 0.0
    # local rank truncation: keep n_max largest |d| (and drop kernel via tol)
    nz = np.abs(d) > tol * scale
    d = d[nz]; U = U[:, nz]
    if d.size == 0:
        return 0.0
    ordl = np.argsort(-np.abs(d))[:min(n_max, d.size)]
    d_k = d[ordl]; U_k = U[:, ordl]
    Wproj = U_k.conj().T @ W_O @ U_k
    M = (Wproj.T / d_k).T
    mu = np.linalg.eigvals(M).real
    good = (np.abs(mu) > tol) & (np.abs(mu - 1.0) > tol)
    mu_g = mu[good]
    return float(np.sum(mu_g * np.log(np.abs(mu_g))))


# ----------------------------------------------------------------------------
def powerlaw_fit(x, y, sig=None):
    """Weighted LSQ fit log y = p log x + q.  Returns (p, q, p_err)."""
    lx = np.log(x); ly = np.log(y)
    A = np.vstack([lx, np.ones_like(lx)]).T
    if sig is None:
        w = np.ones_like(lx)
    else:
        pos = sig[sig > 0]
        floor = np.min(pos) if pos.size else 1.0
        sl = np.where(sig > 0, sig, floor)
        w = 1.0 / sl**2
    AW = A * w[:, None]
    cov = np.linalg.inv(A.T @ AW)
    coef = cov @ (AW.T @ ly)
    return float(coef[0]), float(coef[1]), float(np.sqrt(cov[0, 0]))


# ============================================================================
def run():
    t0 = time.time()
    results = {"conventions": {
        "dimension": 4,
        "G_R_massless_4D": "K_R = a L, a = sqrt(rho)/(2 pi sqrt6); L=link matrix (Johnston 0909.0944 eq.17 m=0)",
        "link_matrix": "L[x,y]=1 iff C[x,y]=1 and (C@C)[x,y]==0 (transitive reduction / covering relation)",
        "causal_4D": "y precedes x iff (t_x-t_y) >= |r_x - r_y|",
        "iDelta": "iDelta = i (G_R - G_R^T), Hermitian, real +/- paired eigenvalues",
        "W_SJ": "positive part of iDelta",
        "SSEE": "W_O v = mu iDelta_O v ; S = sum mu ln|mu| (1611.10281; 2008.07697)",
        "double_truncation": "zero |lambda|<=kappa in spec(iD) and spec(iD|_O) (1712.04227)",
        "area_law_ansatz": "n_max ~ N^{(d-1)/d}; d=4 -> N^{3/4} (2008.07697)",
        "geometry": "concentric 4D causal diamonds {|t|+|r|<=fT}; Vol=(2/3)pi T^4; rho=N/Vol",
        "subdiamond_area": "A(f)=4 pi (fT)^2",
        "PREDICTION_UNDER_TEST": "entropy-cutoff rank ~ N^{3/4} (p=0.75)",
    }}

    rng = np.random.default_rng(20260606)

    # ---- sanity: Green function normalisation in the continuum limit --------
    # Check sqrt(rho/6) <L> -> 2 pi G is consistent by verifying our 'a' value.
    a_demo = 1.0  # placeholder; a is folded in per-N below.

    # ---- Part A: demo spectrum at the largest feasible N -------------------
    N_demo = 3000
    frac_demo = 0.5
    print(f"[demo] sprinkling N={N_demo} in 4D diamond, Vol={VOL_4D:.4f}")
    coords = sprinkle_diamond_4d(N_demo, rng)
    rho_demo = N_demo / VOL_4D
    tC = time.time()
    C = causal_matrix_4d(coords)
    tL = time.time()
    L = link_matrix(C)
    tG = time.time()
    G_R = green_retarded_4d(L, rho_demo)
    iDelta = pauli_jordan(G_R)
    W, pos_spec = sj_wightman(iDelta)
    tE = time.time()
    sub_idx = points_in_subdiamond_4d(coords, frac_demo)
    link_density = L.sum() / N_demo
    print(f"[demo] timings: C={tL-tC:.1f}s L(matmul)={tG-tL:.1f}s eig={tE-tG:.1f}s")
    print(f"[demo] mean links/point={link_density:.2f}  n_sub={len(sub_idx)}  "
          f"#pos modes={len(pos_spec)}")

    knee = find_knee(pos_spec, tol=0.10)
    print(f"[demo] intrinsic knee (dev10%) = {knee:.0f}")

    S_full, _ = ssee(W, iDelta, sub_idx, kappa=None)
    # choose a demo magnitude cutoff at a fixed fraction of lambda_max
    frac_cut = 0.05
    kappa_demo = frac_cut * pos_spec[0]
    rank_demo = rank_at_magnitude(pos_spec, kappa_demo)
    S_trunc, _ = ssee(W, iDelta, sub_idx, kappa=kappa_demo)
    print(f"[demo] S(no trunc)={S_full:.3f}  S(double-trunc @5%max, rank={rank_demo})={S_trunc:.3f}")

    # S vs eigenvalue cutoff scan (for S_vs_rank plot)
    kappa_scan = np.geomspace(pos_spec[0] * 1e-3, pos_spec[0] * 0.8, 26)
    S_scan = np.array([ssee(W, iDelta, sub_idx, kappa=k)[0] for k in kappa_scan])
    rank_scan = np.array([rank_at_magnitude(pos_spec, k) for k in kappa_scan])

    results["demo"] = {
        "N": N_demo, "rho": rho_demo, "frac": frac_demo,
        "n_sub": int(len(sub_idx)), "n_positive_modes": int(len(pos_spec)),
        "mean_links_per_point": float(link_density),
        "lambda_max": float(pos_spec[0]),
        "intrinsic_knee_dev10": float(knee),
        "S_full_no_truncation": float(S_full),
        "S_double_truncation_5pctmax": float(S_trunc),
        "rank_at_5pct_max": int(rank_demo),
        "kappa_scan": kappa_scan.tolist(),
        "S_vs_kappa": S_scan.tolist(),
        "rank_vs_kappa": rank_scan.tolist(),
        "positive_spectrum_head": pos_spec[:80].tolist(),
        "timing_s": {"C": tL - tC, "L_matmul": tG - tL, "eig": tE - tG},
    }

    # ---- Part C (MAIN): entropy-cutoff rank scaling with N -----------------
    # Fixed diamond (Vol=(2/3)pi), rho=N/Vol.  Vary N; several seeds.
    # Measure rank for several self-calibrating magnitude cutoffs and the
    # intrinsic knee.  AREA-LAW PREDICTION: rank ~ N^{3/4}.
    Ns = [500, 800, 1200, 1800, 2600, 3600, 5000]
    n_seeds = 4
    Ns_arr = np.array(Ns, float)
    rho_arr = Ns_arr / VOL_4D

    # cutoff definitions (fractions of lambda_max) + intrinsic knee
    frac_cuts = [0.02, 0.05, 0.10]
    knee_tols = [0.10, 0.20]

    # storage
    rank_fc = {fc: [] for fc in frac_cuts}        # per-N lists of seed means
    rank_fc_std = {fc: [] for fc in frac_cuts}
    knee_means = {tl: [] for tl in knee_tols}
    knee_stds = {tl: [] for tl in knee_tols}
    slopeknee_mean, slopeknee_std = [], []        # literature slope-knee (2008.07697)
    spectra_for_plot = None
    all_seed_data = {}

    for N in Ns:
        rho = N / VOL_4D
        fc_seed = {fc: [] for fc in frac_cuts}
        knee_seed = {tl: [] for tl in knee_tols}
        sk_seed = []
        for s in range(n_seeds):
            rng_s = np.random.default_rng(7919 * N + 101 * s + 3)
            cs = sprinkle_diamond_4d(N, rng_s)
            C = causal_matrix_4d(cs)
            L = link_matrix(C)
            G_R = green_retarded_4d(L, rho)
            _, sp = sj_wightman(pauli_jordan(G_R))
            for fc in frac_cuts:
                fc_seed[fc].append(rank_at_frac_of_max(sp, fc))
            for tl in knee_tols:
                knee_seed[tl].append(find_knee(sp, tol=tl))
            sk_seed.append(find_knee_slope(sp, delta=0.15))
            if N == Ns[-1] and s == 0:
                spectra_for_plot = sp.copy()
        for fc in frac_cuts:
            v = np.array(fc_seed[fc], float)
            rank_fc[fc].append(v.mean()); rank_fc_std[fc].append(v.std(ddof=1))
        for tl in knee_tols:
            v = np.array(knee_seed[tl], float)
            knee_means[tl].append(v.mean()); knee_stds[tl].append(v.std(ddof=1))
        skv = np.array(sk_seed, float)
        slopeknee_mean.append(skv.mean()); slopeknee_std.append(skv.std(ddof=1))
        all_seed_data[str(N)] = {
            "rho": rho,
            "rank_frac": {str(fc): fc_seed[fc] for fc in frac_cuts},
            "knee": {str(tl): knee_seed[tl] for tl in knee_tols},
            "slope_knee": sk_seed,
        }
        print(f"[scaling] N={N:5d} rho={rho:7.1f}  "
              + "  ".join(f"r@{fc}={np.mean(fc_seed[fc]):6.1f}" for fc in frac_cuts)
              + f"  slopeknee={skv.mean():6.1f}")

    # fits
    fits = {}
    for fc in frac_cuts:
        m = np.array(rank_fc[fc]); sd = np.array(rank_fc_std[fc])
        p, q, perr = powerlaw_fit(Ns_arr, m, sig=sd / np.maximum(m, 1e-9))
        fits[f"rank_frac_{fc}"] = {
            "rank_mean": m.tolist(), "rank_std": sd.tolist(),
            "p": p, "q": q, "p_err": perr,
            "p_minus_0.75_sigma": (p - 0.75) / perr if perr > 0 else None,
            "p_minus_0.50_sigma": (p - 0.50) / perr if perr > 0 else None,
        }
        print(f"[fit] rank@{fc}*lmax ~ N^p:  p={p:.4f} +/- {perr:.4f}  "
              f"(pred 3/4=0.75; 2D was 1/2)")
    for tl in knee_tols:
        m = np.array(knee_means[tl]); sd = np.array(knee_stds[tl])
        p, q, perr = powerlaw_fit(Ns_arr, m, sig=sd / np.maximum(m, 1e-9))
        fits[f"knee_tol_{tl}"] = {
            "knee_mean": m.tolist(), "knee_std": sd.tolist(),
            "p": p, "q": q, "p_err": perr,
            "p_minus_0.75_sigma": (p - 0.75) / perr if perr > 0 else None,
        }
        print(f"[fit] intrinsic knee tol={tl} ~ N^p:  p={p:.4f} +/- {perr:.4f}")

    # literature slope-knee fit (the genuine spectral discreteness feature)
    skm = np.array(slopeknee_mean); sksd = np.array(slopeknee_std)
    p_sk, q_sk, perr_sk = powerlaw_fit(Ns_arr, skm, sig=sksd / np.maximum(skm, 1e-9))
    fits["slope_knee"] = {
        "knee_mean": skm.tolist(), "knee_std": sksd.tolist(),
        "p": p_sk, "q": q_sk, "p_err": perr_sk,
        "p_minus_0.75_sigma": (p_sk - 0.75) / perr_sk if perr_sk > 0 else None,
        "method": "slope drop delta=0.15 (Surya Nomaan-X Yazdi 2008.07697 sec2.4)",
    }
    print(f"[fit] slope-knee (2008.07697) ~ N^p:  p={p_sk:.4f} +/- {perr_sk:.4f}  (pred 3/4)")

    results["scaling"] = {
        "Ns": Ns, "rho": rho_arr.tolist(), "n_seeds": n_seeds,
        "VOL_4D": VOL_4D, "frac_cuts": frac_cuts, "knee_tols": knee_tols,
        "fits": fits,
        "per_N": all_seed_data,
        "PREDICTION": "area law rank ~ N^{(d-1)/d} = N^{3/4}=N^0.75 in d=4",
        "comparison_2D": "VYPOCET-04 measured p=0.519+/-0.007 = 1/2",
    }

    # ---- Part D: AREA LAW S vs sub-diamond area ----------------------------
    # S ~ A(f)/ell^2 ~ (f T)^2 ?  Fit S = beta * A(f) + const, A=4pi(fT)^2.
    N_law = 5000
    coords_l = sprinkle_diamond_4d(N_law, np.random.default_rng(424242))
    rho_l = N_law / VOL_4D
    C = causal_matrix_4d(coords_l)
    L = link_matrix(C)
    iD_l = pauli_jordan(green_retarded_4d(L, rho_l))
    W_l, sp_l = sj_wightman(iD_l)
    kappa_law = 0.05 * sp_l[0]
    fracs = np.array([0.35, 0.40, 0.45, 0.50, 0.55, 0.60, 0.65])
    S_law, nsub_law, areas = [], [], []
    for f in fracs:
        idx = points_in_subdiamond_4d(coords_l, f)
        nsub_law.append(len(idx)); areas.append(subdiamond_area(f))
        S_law.append(ssee(W_l, iD_l, idx, kappa=kappa_law)[0])
    S_law = np.array(S_law); areas = np.array(areas); nsub_law = np.array(nsub_law)
    # area-law fit: S vs A
    Aarea = np.vstack([areas, np.ones_like(areas)]).T
    (beta_A, c_A), *_ = np.linalg.lstsq(Aarea, S_law, rcond=None)
    # competing volume-law fit: S vs n_sub (number of points ~ volume)
    Avol = np.vstack([nsub_law.astype(float), np.ones_like(nsub_law, float)]).T
    (beta_V, c_V), *_ = np.linalg.lstsq(Avol, S_law, rcond=None)
    # quality: R^2 for each
    def r2(y, yhat):
        ss = np.sum((y - y.mean())**2)
        return 1.0 - np.sum((y - yhat)**2) / ss if ss > 0 else 0.0
    r2_area = r2(S_law, Aarea @ [beta_A, c_A])
    r2_vol = r2(S_law, Avol @ [beta_V, c_V])
    # power-law S ~ f^q
    p_S, q_S, perr_S = powerlaw_fit(fracs, np.abs(S_law) + 1e-12)
    print(f"[area-law] S vs A: beta={beta_A:.4f} R2={r2_area:.3f} | "
          f"S vs Vol(n): R2={r2_vol:.3f} | S ~ f^{p_S:.2f} (area=>2)")
    results["area_law"] = {
        "N": N_law, "rho": rho_l, "kappa": float(kappa_law),
        "fracs": fracs.tolist(), "n_sub": nsub_law.tolist(),
        "area": areas.tolist(), "S": S_law.tolist(),
        "fit_S_vs_area": {"beta": float(beta_A), "c": float(c_A), "R2": float(r2_area)},
        "fit_S_vs_volume": {"beta": float(beta_V), "c": float(c_V), "R2": float(r2_vol)},
        "S_powerlaw_in_f": {"p": p_S, "p_err": perr_S, "area_law_expects": 2.0},
        "note": ("shallow magnitude truncation: literature (2008.07697, 1712.04227) says "
                 "4D nested diamonds give a VOLUME law unless rank-truncated at n_max~N^{3/4}"),
    }

    # ---- Part E: LITERATURE-FAITHFUL rank truncation n_max = alpha N^{3/4} ---
    # (Surya, Nomaan X, Yazdi arXiv:2008.07697 eq.15, alpha=1,2.)
    # Does the area law S ~ A(f) ~ f^2 emerge when we impose the area-law rank?
    alphas = [1.0, 2.0]
    arealaw_imposed = {}
    for alpha in alphas:
        n_max = int(round(alpha * N_law**0.75))
        S_rt = []
        for f in fracs:
            idx = points_in_subdiamond_4d(coords_l, f)
            S_rt.append(ssee_rank_truncated(W_l, iD_l, idx, n_max))
        S_rt = np.array(S_rt)
        # fit S vs A (area) and S vs n_sub (volume), compare R^2
        (bA, cA), *_ = np.linalg.lstsq(Aarea, S_rt, rcond=None)
        (bV, cV), *_ = np.linalg.lstsq(Avol, S_rt, rcond=None)
        r2A = r2(S_rt, Aarea @ [bA, cA]); r2V = r2(S_rt, Avol @ [bV, cV])
        pS, _, peS = powerlaw_fit(fracs, np.abs(S_rt) + 1e-12)
        arealaw_imposed[f"alpha_{alpha}"] = {
            "n_max": n_max, "S": S_rt.tolist(),
            "fit_S_vs_area": {"beta": float(bA), "c": float(cA), "R2": float(r2A)},
            "fit_S_vs_volume": {"beta": float(bV), "c": float(cV), "R2": float(r2V)},
            "S_powerlaw_in_f_p": pS, "S_powerlaw_p_err": peS,
        }
        print(f"[area-law imposed alpha={alpha}] n_max={n_max}  "
              f"S~f^{pS:.2f}  R2(area)={r2A:.3f} R2(vol)={r2V:.3f}  "
              f"verdict={'AREA' if r2A>r2V else 'VOLUME'}")
    results["area_law_imposed_rank"] = {
        "method": "rank truncation n_max=alpha N^{3/4} (2008.07697 eq.15)",
        "N": N_law, "fracs": fracs.tolist(), "area": areas.tolist(),
        "n_sub": nsub_law.tolist(), "by_alpha": arealaw_imposed,
    }

    # ============================ PLOTS =====================================
    # Plot 1: spectrum + knee (largest N)
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
    sp = spectra_for_plot
    kk = np.arange(1, len(sp) + 1)
    ax1.loglog(kk, sp, '.', ms=3)
    knee_p = find_knee(sp, tol=0.10)
    ax1.axvline(knee_p, color='r', ls='--', label=f"intrinsic knee={knee_p:.0f}")
    for fc, col in zip(frac_cuts, ['c', 'b', 'm']):
        rk = rank_at_frac_of_max(sp, fc)
        ax1.axvline(rk, color=col, ls='-.', lw=1, label=f"rank@{fc}lmax={rk}")
    ax1.set_xlabel("rank (desc)"); ax1.set_ylabel(r"$\lambda_k$ of $i\Delta$ (+)")
    ax1.set_title(f"4D Pauli-Jordan spectrum, N={Ns[-1]}"); ax1.legend(fontsize=7)
    A, P = _plateau_value(sp)
    ax2.semilogx(kk, P, '.', ms=3)
    ax2.axhline(A, color='g', ls=':', label=f"plateau A={A:.2f}")
    ax2.axvline(knee_p, color='r', ls='--', label=f"knee={knee_p:.0f}")
    ax2.set_xlabel("rank"); ax2.set_ylabel(r"$k\,\lambda_k$")
    ax2.set_title("Spectral plateau & knee (4D)"); ax2.legend(fontsize=8)
    fig.tight_layout(); fig.savefig(os.path.join(OUTDIR, "spectrum_knee.png"), dpi=140)
    plt.close(fig)

    # Plot 2: S vs kept rank (truncation)
    fig, ax = plt.subplots(figsize=(7.5, 5))
    ax.semilogx(rank_scan, S_scan, 'o-', ms=4)
    ax.axvline(rank_demo, color='b', ls='-.', label=f"5% lmax -> rank {rank_demo}")
    ax.axhline(S_full, color='g', ls=':', label=f"no truncation S={S_full:.2f}")
    ax.set_xlabel(r"kept rank (modes with $\lambda>\kappa$)")
    ax.set_ylabel("SSEE  S")
    ax.set_title(f"4D SSEE vs truncation, N={N_demo}, sub frac={frac_demo}")
    ax.legend(); fig.tight_layout()
    fig.savefig(os.path.join(OUTDIR, "S_vs_rank.png"), dpi=140); plt.close(fig)

    # Plot 3: THE MEASUREMENT -- entropy-cutoff rank vs N (log-log)
    plt.figure(figsize=(8, 6))
    xx = np.linspace(Ns_arr.min(), Ns_arr.max(), 100)
    cols = ['tab:cyan', 'tab:blue', 'tab:purple']
    for fc, col in zip(frac_cuts, cols):
        f = fits[f"rank_frac_{fc}"]
        m = np.array(f["rank_mean"]); sd = np.array(f["rank_std"])
        plt.errorbar(Ns_arr, m, yerr=sd, fmt='s', color=col, capsize=3,
                     label=f"rank@{fc}lmax: p={f['p']:.3f}±{f['p_err']:.3f}")
        plt.plot(xx, np.exp(f["q"]) * xx**f["p"], '-', color=col, lw=1)
    # literature slope-knee (the genuine spectral discreteness feature)
    fsk = fits["slope_knee"]
    msk = np.array(fsk["knee_mean"]); sdsk = np.array(fsk["knee_std"])
    plt.errorbar(Ns_arr, msk, yerr=sdsk, fmt='o', color='tab:red', capsize=3,
                 label=f"slope-knee (2008.07697): p={fsk['p']:.3f}±{fsk['p_err']:.3f}")
    plt.plot(xx, np.exp(fsk["q"]) * xx**fsk["p"], '-', color='tab:red', lw=1)
    # reference slopes anchored at the 5% curve first point
    anchor = np.array(fits["rank_frac_0.05"]["rank_mean"])[0]
    plt.plot(xx, anchor / Ns_arr[0]**0.75 * xx**0.75, 'k--', lw=1.5,
             label="slope 3/4 (4D area-law PREDICTION)")
    plt.plot(xx, anchor / Ns_arr[0]**0.5 * xx**0.5, 'k:', lw=1.2,
             label="slope 1/2 (2D)")
    plt.xscale('log'); plt.yscale('log')
    plt.xlabel(r"$N$  ($\rho=N/\mathrm{Vol}$)"); plt.ylabel("entropy-cutoff rank")
    plt.title("THE MEASUREMENT: 4D entropy-cutoff rank vs N")
    plt.legend(fontsize=8); plt.tight_layout()
    plt.savefig(os.path.join(OUTDIR, "rank_vs_N.png"), dpi=140); plt.close()

    # Plot 4: area law -- S vs area A(f), shallow cutoff vs imposed-rank cutoff
    plt.figure(figsize=(8, 6))
    plt.plot(areas, S_law, 'o', ms=7, color='tab:gray',
             label=f"shallow mag. cut: S~f^{p_S:.1f} (R²area={r2_area:.2f})")
    xa = np.linspace(areas.min(), areas.max(), 50)
    plt.plot(xa, beta_A * xa + c_A, ':', color='tab:gray')
    for alpha, mk, col in zip(alphas, ['s', '^'], ['tab:green', 'tab:blue']):
        d = arealaw_imposed[f"alpha_{alpha}"]
        Srt = np.array(d["S"])
        bA = d["fit_S_vs_area"]["beta"]; cA = d["fit_S_vs_area"]["c"]
        plt.plot(areas, Srt, mk, ms=7, color=col,
                 label=(f"imposed n_max={alpha:g}N^3/4={d['n_max']}: "
                        f"S~f^{d['S_powerlaw_in_f_p']:.1f} "
                        f"(R²area={d['fit_S_vs_area']['R2']:.2f})"))
        plt.plot(xa, bA * xa + cA, '-', color=col, lw=1)
    plt.xlabel(r"sub-diamond area $A(f)=4\pi(fT)^2$"); plt.ylabel("SSEE  S")
    plt.title(f"4D area law test, N={N_law}: shallow cut (volume) vs imposed N^3/4 rank")
    plt.legend(); plt.tight_layout()
    plt.savefig(os.path.join(OUTDIR, "area_law.png"), dpi=140); plt.close()

    results["runtime_s"] = time.time() - t0
    with open(os.path.join(OUTDIR, "results.json"), "w") as f:
        json.dump(results, f, indent=2)
    print(f"\nDone in {results['runtime_s']:.1f}s. Saved results.json + 4 PNGs to {OUTDIR}")
    return results


if __name__ == "__main__":
    run()
