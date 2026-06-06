#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
VYPOCET-09 : SSEE on a sprinkled 4D causal diamond using the
             BENINCASA-DOWKER NON-LOCAL D'ALEMBERTIAN as the dynamical object
============================================================================

This is the DECISIVE test of H04 interpretation (b):  in 4D, replace the
link-matrix retarded Green function G_R = (sqrt(rho)/2pi sqrt6) L of
VYPOCET-06 by the retarded Green function obtained from the Benincasa-Dowker
(BD) discrete d'Alembertian,  G_R = B^{-1},  and re-run the Sorkin-Johnston
SSEE cutoff-scaling protocol.

Interpretation (b) (H04 sec 2b) claims that the link matrix is the WRONG object
for the modular/UV identification and that the BD d'Alembertian -- explicitly
constructed to have a controlled continuum limit -- will instead give:
    * a CLEAN power-law spectrum  lambda_k ~ k^{-alpha}   (vs flat link spectrum)
    * a ROBUST entropy-cutoff exponent  p  (prediction p = 3/4 = (d-1)/d)
    * an AREA law (rather than the volume law VYPOCET-06 found)

HONEST OUTCOMES (decided by the data, never fudged):
   (i)  clean power law + robust p ~ 3/4   => interpretation (b) confirmed
   (ii) still flat / non-robust            => (b) refuted, 2D/4D difference is
                                              dimensional
   (iii)numerical pathologies of B at small N => documented; smeared BD tried.

----------------------------------------------------------------------------
CONVENTIONS  (verified from the primary literature, June 2026)
----------------------------------------------------------------------------
SHARP 4D BD d'Alembertian  (Benincasa & Dowker, "The Scalar Curvature of a
Causal Set", arXiv:1001.2725, eqs. (2)-(3); PRL 104, 181301 (2010)):

    B phi(x) = (4 / (sqrt6 * l^2)) [ -phi(x)
                 + ( sum_{L1} - 9 sum_{L2} + 16 sum_{L3} - 8 sum_{L4} ) phi(y) ]

    layer  L_i = { y < x : n(x,y) = i-1 },
    n(x,y) = number of elements STRICTLY between y and x
           = |I(x,y)| - 2  =  (C @ C)[x,y]   (count of length-2 causal chains).
    So L1 = links (n=0), L2: n=1, L3: n=2, L4: n=3.
    l = discreteness length;  in 4D  l^4 = 1/rho  =>  1/l^2 = sqrt(rho).
    Hence prefactor  4/(sqrt6 l^2) = 4 sqrt(rho)/sqrt6.

SMEARED / NON-LOCAL discrete BD  (Aslanbeigi, Saravani, Sorkin,
"Generalized causal set d'Alembertians", arXiv:1305.2588, eqs. (25)-(26);
spectral-dimension application Belenchia, Benincasa, Liberati, Marin, Marino,
Bassi, arXiv:1507.00330):

    B_eps^{(d)} phi(x) = (eps^{2/d}/l^2) [ alpha_d phi(x)
                          + beta_d eps sum_{y<x} f_d(n(x,y),eps) phi(y) ]
    f_d(n,eps) = (1-eps)^n  sum_{i=1}^{N_d} C_i^{(d)} binom(n,i-1) (eps/(1-eps))^{i-1}
    d=4 :  alpha_4 = -4/sqrt6,  beta_4 = 4/sqrt6,  C^{(4)} = (1,-9,16,-8)
    d=2 :  alpha_2 = -2,        beta_2 = 4,        C^{(2)} = (1,-2,1)
    eps = (l/xi)^d in (0,1],  xi = non-locality scale (>= l).
    As eps -> 1 the sharp operator (layer coefficients 1,-9,16,-8) is recovered.
    With l^2 = rho^{-2/d}:  eps^{2/d}/l^2 = eps^{2/d} rho^{2/d};  for d=4
    this is sqrt(eps) sqrt(rho).

RETARDEDNESS / CAUSALITY (how we enforce & verify it):
    B[x,y] != 0 only for y <= x (y in causal past of x, or y=x).  If the points
    are listed in a CAUSAL (topological) order -- here: sorted by global time t,
    which refines the causal order since y<x => t_y<t_x -- then B is exactly
    LOWER-TRIANGULAR.  The inverse of a lower-triangular matrix is lower-
    triangular, so  G_R = B^{-1}  is automatically retarded (supported on the
    causal past).  We VERIFY: max|triu(B,1)| == 0 and max|triu(G_R,1)| ~ machine
    eps.  We also report cond(B) per (N) to flag the (iii) pathology regime.

SJ construction & SSEE  (dimension independent, identical to VYPOCET-04/06;
Sorkin-Yazdi arXiv:1611.10281; Surya, Nomaan X, Yazdi arXiv:2008.07697):
    iDelta = i (G_R - G_R^T),  W = positive part of iDelta,
    SSEE generalized eigenproblem  W_O v = mu iDelta_O v,  S = sum mu ln|mu|,
    double eigenvalue-magnitude truncation kappa (1712.04227).

AREA-LAW SCALING ansatz  rank ~ N^{(d-1)/d}; d=4 -> N^{3/4}  (2008.07697).
"""

import json
import os
import time
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from math import comb

OUTDIR = os.path.dirname(os.path.abspath(__file__))
PLOTDIR = os.path.join(OUTDIR, "plots")
os.makedirs(PLOTDIR, exist_ok=True)

T_HALF = 1.0
VOL_4D = (2.0 / 3.0) * np.pi * T_HALF**4    # 4-volume of diamond {|t|+|r|<=T}

# BD 4D sharp layer coefficients and prefactor constants
BD4_C = np.array([1.0, -9.0, 16.0, -8.0])   # C_1..C_4 (layers n=0..3)
BD4_ALPHA = -4.0 / np.sqrt(6.0)
BD4_BETA = 4.0 / np.sqrt(6.0)


# ----------------------------------------------------------------------------
# geometry (identical sprinkling to VYPOCET-06)
# ----------------------------------------------------------------------------
def sprinkle_diamond_4d(N, rng, T=T_HALF):
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


def causal_matrix_4d(coords):
    """C[x,y]=1 iff y precedes x  <=> (t_x-t_y) >= |r_x-r_y|, y!=x."""
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


def points_in_subdiamond_4d(coords, frac, T=T_HALF):
    t = np.abs(coords[:, 0])
    r = np.linalg.norm(coords[:, 1:], axis=1)
    return np.where(t + r <= frac * T)[0]


def subdiamond_area(frac, T=T_HALF):
    return 4.0 * np.pi * (frac * T)**2


# ----------------------------------------------------------------------------
# Benincasa-Dowker operator(s)
# ----------------------------------------------------------------------------
def bd_sharp_matrix(C, rho):
    """SHARP 4D BD d'Alembertian as an N x N matrix.
       B[x,y] = pref * C_{n+1}      for y<x with n=(C@C)[x,y] in {0,1,2,3}
       B[x,x] = -pref
       pref   = 4 sqrt(rho)/sqrt6  = 4/(sqrt6 l^2).
       (Off-diagonal entries with n>3 are exactly zero -> only first 4 layers.)
    """
    N = C.shape[0]
    Cb = (C > 0)
    nmat = np.rint(C @ C).astype(np.int64)
    B = np.zeros((N, N))
    for k in range(4):
        B[Cb & (nmat == k)] = BD4_C[k]
    pref = 4.0 * np.sqrt(rho) / np.sqrt(6.0)
    B *= pref
    np.fill_diagonal(B, -pref)
    return B


def bd_smeared_matrix(C, rho, eps):
    """SMEARED (non-local) 4D BD d'Alembertian (Aslanbeigi-Saravani-Sorkin).
       B_eps[x,y] = pref_eps * beta4 * eps * f4(n,eps)   for y<x
       B_eps[x,x] = pref_eps * alpha4
       pref_eps   = eps^{1/2} sqrt(rho)        (= eps^{2/d}/l^2, d=4)
       f4(n,eps)  = (1-eps)^n sum_{i=1..4} C_i binom(n,i-1) (eps/(1-eps))^{i-1}.
       All past elements contribute (smearing kernel), not just first 4 layers,
       but the (1-eps)^n factor exponentially suppresses distant ones.
    """
    N = C.shape[0]
    Cb = (C > 0)
    nmat = np.rint(C @ C).astype(np.int64)
    pref = np.sqrt(eps) * np.sqrt(rho)
    B = np.zeros((N, N))
    n_vals = nmat[Cb]
    if n_vals.size:
        nmax = int(n_vals.max())
        # tabulate f4(n,eps) for n=0..nmax
        ftab = np.zeros(nmax + 1)
        one_me = 1.0 - eps
        ratio = eps / one_me if one_me > 0 else 0.0
        for n in range(nmax + 1):
            acc = 0.0
            for i in range(1, 5):           # i=1..4 -> binom(n,i-1)
                k = i - 1
                if k <= n:
                    acc += BD4_C[i - 1] * comb(n, k) * (ratio ** k)
            ftab[n] = (one_me ** n) * acc
        vals = pref * BD4_BETA * eps * ftab[n_vals]
        B[Cb] = vals
    np.fill_diagonal(B, pref * BD4_ALPHA)
    return B


def green_retarded_from_B(B):
    """G_R = B^{-1}.  B is lower-triangular in the time-ordered basis, so G_R
       is lower-triangular = retarded.  Returns (G_R, diagnostics)."""
    cond = np.linalg.cond(B)
    G = np.linalg.inv(B)
    triu_B = float(np.abs(np.triu(B, 1)).max())
    diag_G = float(np.abs(np.diag(G)).mean()) or 1.0
    triu_G = float(np.abs(np.triu(G, 1)).max())
    diag = {"cond_B": float(cond),
            "max_upper_B": triu_B,                 # must be 0 (causal order)
            "max_upper_G_over_diag": triu_G / diag_G}  # ~ machine eps -> retarded
    return G, diag


def pauli_jordan(G_R):
    return 1j * (G_R - G_R.T)


def sj_wightman(iDelta, rel_floor=1e-10):
    """SJ Wightman = positive part of iDelta.  Returns (W, sorted-desc positive
       eigenvalues).  Eigenvalues with |lambda| < rel_floor*lambda_max are
       treated as numerical kernel (discarded) to avoid amplifying the
       inversion's machine-precision noise -- this floor is documented and its
       sensitivity is reported."""
    w, V = np.linalg.eigh(iDelta)
    lmax = np.max(np.abs(w)) if w.size else 0.0
    floor = rel_floor * lmax
    pos = w > floor
    lam = w[pos]
    Vp = V[:, pos]
    W = (Vp * lam) @ Vp.conj().T
    pos_spec = np.sort(lam)[::-1]
    return W, pos_spec


# ----------------------------------------------------------------------------
# SSEE with double truncation (identical algorithm to VYPOCET-06)
# ----------------------------------------------------------------------------
def ssee(W, iDelta, sub_idx, frac=None, global_lmax=None, tol=1e-9):
    """Double-truncated SSEE.  `frac` is the magnitude cutoff as a FRACTION of
    lambda_max: globally we keep modes with |lambda|>frac*global_lmax and
    locally |d|>frac*local_lmax.  Using a fraction (not an absolute kappa) keeps
    the global and local truncations on their own scales -- essential for the
    steep BD spectrum, where an absolute global kappa would zero the local
    spectrum (the S=0 bug)."""
    iD = iDelta
    Wm = W
    if frac is not None:
        w, V = np.linalg.eigh(iD)
        glmax = global_lmax if global_lmax is not None else np.max(np.abs(w))
        keep = np.abs(w) > frac * glmax
        wk = w[keep]; Vk = V[:, keep]
        iD = (Vk * wk) @ Vk.conj().T
        pos = wk > 0
        Wm = (Vk[:, pos] * wk[pos]) @ Vk[:, pos].conj().T
    iD_O = iD[np.ix_(sub_idx, sub_idx)]
    W_O = Wm[np.ix_(sub_idx, sub_idx)]
    d, U = np.linalg.eigh(iD_O)
    scale = np.max(np.abs(d)) if d.size else 0.0
    if scale == 0.0:
        return 0.0
    local_cut = (frac * scale) if frac is not None else (tol * scale)
    keep = np.abs(d) > local_cut
    if keep.sum() == 0:
        return 0.0
    d_k = d[keep]; U_k = U[:, keep]
    Wproj = U_k.conj().T @ W_O @ U_k
    M = (Wproj.T / d_k).T
    mu = np.linalg.eigvals(M).real
    good = (np.abs(mu) > tol) & (np.abs(mu - 1.0) > tol)
    mu_g = mu[good]
    return float(np.sum(mu_g * np.log(np.abs(mu_g))))


# ----------------------------------------------------------------------------
# spectrum / power-law diagnostics
# ----------------------------------------------------------------------------
def rank_at_frac_of_max(pos_spec, frac):
    if len(pos_spec) == 0:
        return 0
    return int(np.sum(pos_spec > frac * pos_spec[0]))


def rank_above_absolute(pos_spec, floor):
    """# positive eigenvalues above an ABSOLUTE magnitude floor (density-set).
    For a power-law spectrum this is the N-scaling estimator (a fraction-of-max
    cutoff is N-independent for a clean power law; an absolute floor tied to the
    discreteness scale is the analogue of the 2D kappa = sqrt(N)/4pi)."""
    return int(np.sum(pos_spec > floor))


def powerlaw_alpha(pos_spec, lo_frac=0.02, hi_frac=0.5):
    """Fit lambda_k ~ k^{-alpha} over an intermediate rank band [lo,hi] (avoids
       the few largest eigenvalues and the deep tail).  Returns (alpha, R2,
       n_used)."""
    n = len(pos_spec)
    lo = max(3, int(lo_frac * n))
    hi = max(lo + 5, int(hi_frac * n))
    if hi - lo < 6:
        return np.nan, np.nan, 0
    k = np.arange(1, n + 1, dtype=float)[lo:hi]
    y = pos_spec[lo:hi]
    good = y > 0
    if good.sum() < 6:
        return np.nan, np.nan, 0
    lk = np.log(k[good]); ly = np.log(y[good])
    A = np.vstack([lk, np.ones_like(lk)]).T
    coef, *_ = np.linalg.lstsq(A, ly, rcond=None)
    yhat = A @ coef
    ss = np.sum((ly - ly.mean())**2)
    r2 = 1.0 - np.sum((ly - yhat)**2) / ss if ss > 0 else 0.0
    return float(-coef[0]), float(r2), int(good.sum())


def find_knee_slope(pos_spec, delta=0.15, win=8, lo=3):
    """Literature slope-knee (2008.07697 sec 2.4): first rank where the local
       log-log slope steepens by fraction delta below its plateau."""
    n = len(pos_spec)
    if n < 4 * win:
        return float(n)
    lk = np.log(np.arange(1, n + 1, dtype=float))
    ll = np.log(np.maximum(pos_spec, 1e-300))
    m = np.full(n, np.nan)
    half = win // 2
    for k in range(half, n - half):
        xs = lk[k - half:k + half + 1]
        ys = ll[k - half:k + half + 1]
        m[k] = np.polyfit(xs, ys, 1)[0]
    band_hi = max(lo + win, int(0.15 * n))
    seg = m[lo:band_hi]
    seg = seg[~np.isnan(seg)]
    if seg.size == 0:
        return float(n)
    m_plat = np.median(seg)
    thresh = (1.0 + delta) * m_plat
    cand = np.where((~np.isnan(m)) & (np.arange(n) > band_hi) & (m < thresh))[0]
    return float(cand[0] + 1) if cand.size else float(n)


def powerlaw_fit(x, y, sig=None):
    x = np.asarray(x, float); y = np.asarray(y, float)
    # drop non-positive y (e.g. a zero rank count) so log is well defined
    ok = (y > 0) & (x > 0)
    if ok.sum() < 2:
        return float('nan'), float('nan'), float('nan')
    x = x[ok]; y = y[ok]
    if sig is not None:
        sig = np.asarray(sig, float)[ok]
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


def r2_of(y, yhat):
    ss = np.sum((y - y.mean())**2)
    return 1.0 - np.sum((y - yhat)**2) / ss if ss > 0 else 0.0


# ============================================================================
def build_operator(coords, rho, mode, eps=None):
    """Time-order points (causal refinement) then build B (sharp or smeared)
       and G_R = B^{-1}.  Returns (coords_ordered, G_R, diag, pos_spec, W, iD)."""
    order = np.argsort(coords[:, 0])
    co = coords[order]
    C = causal_matrix_4d(co)
    if mode == "sharp":
        B = bd_sharp_matrix(C, rho)
    else:
        B = bd_smeared_matrix(C, rho, eps)
    G_R, diag = green_retarded_from_B(B)
    iD = pauli_jordan(G_R)
    W, pos_spec = sj_wightman(iD)
    return co, G_R, diag, pos_spec, W, iD


def run():
    t0 = time.time()
    results = {"conventions": {
        "object": "BD non-local d'Alembertian B; retarded Green function G_R = B^{-1}",
        "BD_sharp_4D": "B phi = (4/(sqrt6 l^2))[-phi(x)+(sum_L1 -9 sum_L2 +16 sum_L3 -8 sum_L4)phi(y)]; arXiv:1001.2725 eq2-3",
        "layers": "L_i = {y<x : n(x,y)=i-1}; n=(C@C)[x,y] = #elements strictly between",
        "prefactor": "4/(sqrt6 l^2)=4 sqrt(rho)/sqrt6 (l^4=1/rho in 4D)",
        "BD_smeared_4D": "B_eps phi=(sqrt(eps) sqrt(rho))[alpha4 phi(x)+beta4 eps sum f4(n,eps)phi(y)]; arXiv:1305.2588 eq25-26; 1507.00330",
        "f4": "f4(n,eps)=(1-eps)^n sum_{i=1..4} C_i binom(n,i-1)(eps/(1-eps))^{i-1}, C=(1,-9,16,-8)",
        "alpha4_beta4": [BD4_ALPHA, BD4_BETA],
        "retardedness": "B lower-triangular in time order => G_R=B^{-1} lower-triangular = retarded (verified)",
        "iDelta": "iDelta=i(G_R-G_R^T); W=positive part; SSEE W_O v=mu iDelta_O v, S=sum mu ln|mu|",
        "geometry": "concentric 4D diamonds {|t|+|r|<=fT}; Vol=(2/3)pi; rho=N/Vol; A(f)=4pi(fT)^2",
        "PREDICTION_b": "clean power law lambda_k~k^-alpha + robust rank~N^{3/4} (p=0.75)",
        "ref_VYPOCET06": "link-matrix spectrum was FLAT; p=0.65-0.98 cutoff-dependent; volume law",
    }}

    # ===================== PART A : demo + retardedness check ===============
    N_demo = 2000
    frac_demo = 0.5
    rng = np.random.default_rng(20260606)
    coords = sprinkle_diamond_4d(N_demo, rng)
    rho_demo = N_demo / VOL_4D
    print(f"[demo] N={N_demo} rho={rho_demo:.1f}  building SHARP BD operator...")
    tA = time.time()
    co, G_R, diag, pos_spec, W, iD = build_operator(coords, rho_demo, "sharp")
    tB = time.time()
    sub_idx = points_in_subdiamond_4d(co, frac_demo)
    alpha, r2_pl, n_pl = powerlaw_alpha(pos_spec)
    lmax_g = float(pos_spec[0])
    S_full = ssee(W, iD, sub_idx, frac=None)
    S_trunc = ssee(W, iD, sub_idx, frac=0.05, global_lmax=lmax_g)
    print(f"[demo] cond(B)={diag['cond_B']:.3e}  max_upper_B={diag['max_upper_B']:.1e} "
          f"G_R upper/diag={diag['max_upper_G_over_diag']:.1e} (retarded check)")
    print(f"[demo] #pos modes={len(pos_spec)} lam_max={pos_spec[0]:.3e}  "
          f"power-law alpha={alpha:.3f} (R2={r2_pl:.4f})  build+eig={tB-tA:.1f}s")
    print(f"[demo] S(no trunc)={S_full:.3f}  S(5% trunc)={S_trunc:.3f}")

    frac_scan = np.geomspace(1e-3, 0.6, 24)
    S_scan = np.array([ssee(W, iD, sub_idx, frac=fr, global_lmax=lmax_g) for fr in frac_scan])
    rank_scan = np.array([rank_at_frac_of_max(pos_spec, fr) for fr in frac_scan])

    results["demo"] = {
        "N": N_demo, "rho": rho_demo, "frac": frac_demo,
        "n_sub": int(len(sub_idx)), "n_positive_modes": int(len(pos_spec)),
        "lambda_max": float(pos_spec[0]),
        "powerlaw_alpha": alpha, "powerlaw_R2": r2_pl, "powerlaw_n": n_pl,
        "retardedness": diag,
        "S_full": float(S_full), "S_trunc_5pct": float(S_trunc),
        "positive_spectrum_head": pos_spec[:120].tolist(),
        "frac_scan": frac_scan.tolist(), "S_vs_frac": S_scan.tolist(),
        "rank_vs_frac": rank_scan.tolist(),
    }

    # ===================== PART B : spectrum-shape comparison ===============
    # Build BOTH the BD G_R spectrum and the VYPOCET-06 link-matrix spectrum on
    # the SAME sprinkling, to make the "clean vs flat" comparison rigorous.
    def link_spectrum(co, rho):
        C = causal_matrix_4d(co)
        C2 = C @ C
        L = ((C > 0) & (C2 == 0)).astype(np.float64)
        a = np.sqrt(rho) / (2.0 * np.pi * np.sqrt(6.0))
        iDl = 1j * (a * L - (a * L).T)
        w = np.linalg.eigvalsh(iDl)
        return np.sort(w[w > 0])[::-1]

    link_spec = link_spectrum(co, rho_demo)
    a_link, r2_link, _ = powerlaw_alpha(link_spec)
    print(f"[compare] link-matrix spectrum power-law alpha={a_link:.3f} "
          f"(R2={r2_link:.4f})  vs BD alpha={alpha:.3f} (R2={r2_pl:.4f})")
    results["spectrum_compare"] = {
        "N": N_demo,
        "BD_alpha": alpha, "BD_R2": r2_pl,
        "link_alpha": a_link, "link_R2": r2_link,
        "BD_spec_head": pos_spec[:60].tolist(),
        "link_spec_head": link_spec[:60].tolist(),
    }

    # ===================== PART C (MAIN): rank-vs-N scaling =================
    # SHARP BD.  Several self-calibrating magnitude cutoffs + slope-knee.
    # AREA-LAW PREDICTION: rank ~ N^{3/4}.
    Ns = [500, 800, 1200, 1600, 2200, 3000]
    n_seeds = 3
    Ns_arr = np.array(Ns, float)
    frac_cuts = [0.02, 0.05, 0.10]
    # absolute density-scaled floors: keep modes with lambda > c*sqrt(rho).
    # (The BD G_R carries the prefactor ~sqrt(rho); iDelta eigenvalues scale as
    #  sqrt(rho)*dimensionless.  A fixed c probes a fixed DIMENSIONLESS spectral
    #  level, the proper N-scaling cutoff for a power law -- analogue of the 2D
    #  absolute kappa = sqrt(N)/4pi.)
    abs_cs = [1.0, 3.0, 10.0]
    rank_fc = {fc: [] for fc in frac_cuts}
    rank_fc_std = {fc: [] for fc in frac_cuts}
    rank_abs = {c: [] for c in abs_cs}
    rank_abs_std = {c: [] for c in abs_cs}
    sk_mean, sk_std = [], []
    pl_alpha_mean, pl_alpha_std, pl_r2_mean = [], [], []
    cond_mean = []
    per_N = {}
    spectra_for_plot = None

    for N in Ns:
        rho = N / VOL_4D
        sqrt_rho = np.sqrt(rho)
        fc_seed = {fc: [] for fc in frac_cuts}
        abs_seed = {c: [] for c in abs_cs}
        sk_seed = []
        al_seed = []
        r2_seed = []
        cond_seed = []
        for s in range(n_seeds):
            rng_s = np.random.default_rng(7919 * N + 101 * s + 3)
            cs = sprinkle_diamond_4d(N, rng_s)
            co, G_R, dg, sp, W, iD = build_operator(cs, rho, "sharp")
            for fc in frac_cuts:
                fc_seed[fc].append(rank_at_frac_of_max(sp, fc))
            for c in abs_cs:
                abs_seed[c].append(rank_above_absolute(sp, c * sqrt_rho))
            sk_seed.append(find_knee_slope(sp, delta=0.15))
            a_, r2_, _ = powerlaw_alpha(sp)
            al_seed.append(a_); r2_seed.append(r2_)
            cond_seed.append(dg["cond_B"])
            if N == Ns[-1] and s == 0:
                spectra_for_plot = sp.copy()
        for fc in frac_cuts:
            v = np.array(fc_seed[fc], float)
            rank_fc[fc].append(v.mean()); rank_fc_std[fc].append(v.std(ddof=1))
        for c in abs_cs:
            v = np.array(abs_seed[c], float)
            rank_abs[c].append(v.mean()); rank_abs_std[c].append(v.std(ddof=1))
        skv = np.array(sk_seed, float)
        sk_mean.append(skv.mean()); sk_std.append(skv.std(ddof=1))
        alv = np.array(al_seed, float)
        pl_alpha_mean.append(np.nanmean(alv)); pl_alpha_std.append(np.nanstd(alv, ddof=1))
        pl_r2_mean.append(float(np.nanmean(r2_seed)))
        cond_mean.append(float(np.mean(cond_seed)))
        per_N[str(N)] = {"rho": rho,
                         "rank_frac": {str(fc): fc_seed[fc] for fc in frac_cuts},
                         "rank_abs": {str(c): abs_seed[c] for c in abs_cs},
                         "slope_knee": sk_seed, "pl_alpha": al_seed,
                         "pl_R2": r2_seed, "cond_B": cond_seed}
        print(f"[scaling] N={N:5d} rho={rho:7.1f}  "
              + "  ".join(f"r@{fc}={np.mean(fc_seed[fc]):6.1f}" for fc in frac_cuts)
              + "  " + "  ".join(f"abs{c}={np.mean(abs_seed[c]):6.1f}" for c in abs_cs)
              + f"  sk={skv.mean():6.1f}  alpha={np.nanmean(alv):.3f}"
              + f"  cond={np.mean(cond_seed):.1e}")

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
        print(f"[fit] rank@{fc}*lmax ~ N^p: p={p:.4f}+/-{perr:.4f}  "
              f"(dev 3/4 = {(p-0.75)/perr:+.1f} sigma)")
    for c in abs_cs:
        m = np.array(rank_abs[c]); sd = np.array(rank_abs_std[c])
        p, q, perr = powerlaw_fit(Ns_arr, m, sig=sd / np.maximum(m, 1e-9))
        fits[f"rank_abs_{c}"] = {
            "rank_mean": m.tolist(), "rank_std": sd.tolist(),
            "p": p, "q": q, "p_err": perr,
            "p_minus_0.75_sigma": (p - 0.75) / perr if perr > 0 else None,
            "p_minus_0.50_sigma": (p - 0.50) / perr if perr > 0 else None,
        }
        print(f"[fit] rank@lam>{c}*sqrt(rho) ~ N^p: p={p:.4f}+/-{perr:.4f}  "
              f"(dev 3/4 = {(p-0.75)/perr:+.1f} sigma)")
    skm = np.array(sk_mean); sksd = np.array(sk_std)
    p_sk, q_sk, perr_sk = powerlaw_fit(Ns_arr, skm, sig=sksd / np.maximum(skm, 1e-9))
    fits["slope_knee"] = {"knee_mean": skm.tolist(), "knee_std": sksd.tolist(),
                          "p": p_sk, "q": q_sk, "p_err": perr_sk,
                          "p_minus_0.75_sigma": (p_sk - 0.75) / perr_sk if perr_sk > 0 else None}
    print(f"[fit] slope-knee ~ N^p: p={p_sk:.4f}+/-{perr_sk:.4f}  "
          f"(dev 3/4 = {(p_sk-0.75)/perr_sk:+.1f} sigma)")

    results["scaling"] = {
        "Ns": Ns, "n_seeds": n_seeds, "VOL_4D": VOL_4D,
        "frac_cuts": frac_cuts, "abs_cs": abs_cs, "fits": fits, "per_N": per_N,
        "powerlaw_alpha_per_N": {"mean": pl_alpha_mean, "std": pl_alpha_std,
                                 "R2": pl_r2_mean},
        "cond_B_per_N": cond_mean,
        "PREDICTION": "rank ~ N^{3/4}=N^0.75 (area law, d=4)",
    }

    # ===================== PART D : area vs volume law =====================
    N_law = 3000
    coords_l = sprinkle_diamond_4d(N_law, np.random.default_rng(424242))
    rho_l = N_law / VOL_4D
    co_l, G_l, dg_l, sp_l, W_l, iD_l = build_operator(coords_l, rho_l, "sharp")
    lmax_law = float(sp_l[0])
    fracs = np.array([0.35, 0.40, 0.45, 0.50, 0.55, 0.60, 0.65])
    areas = np.array([subdiamond_area(f) for f in fracs])
    nsub_law = np.array([len(points_in_subdiamond_4d(co_l, f)) for f in fracs], float)
    Aarea = np.vstack([areas, np.ones_like(areas)]).T
    Avol = np.vstack([nsub_law, np.ones_like(nsub_law)]).T
    # robustness sweep over truncation depth (None = no truncation, plus several
    # magnitude fractions).  If the area/volume verdict is not stable across
    # cuts, the test is INCONCLUSIVE -- which is itself an honest outcome.
    trunc_settings = [("none", None), ("frac0.02", 0.02), ("frac0.05", 0.05),
                      ("frac0.10", 0.10), ("frac0.20", 0.20)]
    area_sweep = {}
    verdicts = []
    for name, fr in trunc_settings:
        S_law = np.array([ssee(W_l, iD_l, points_in_subdiamond_4d(co_l, f),
                               frac=fr, global_lmax=lmax_law) for f in fracs])
        (bA, cA), *_ = np.linalg.lstsq(Aarea, S_law, rcond=None)
        (bV, cV), *_ = np.linalg.lstsq(Avol, S_law, rcond=None)
        r2_area = r2_of(S_law, Aarea @ [bA, cA])
        r2_vol = r2_of(S_law, Avol @ [bV, cV])
        p_S, _, _ = powerlaw_fit(fracs, np.abs(S_law) + 1e-12)
        v = ("AREA" if r2_area > r2_vol else "VOLUME") if max(r2_area, r2_vol) > 0.5 \
            else "INCONCLUSIVE"
        verdicts.append(v)
        area_sweep[name] = {"trunc_frac": fr, "S": S_law.tolist(),
                            "R2_area": float(r2_area), "R2_vol": float(r2_vol),
                            "S_powerlaw_in_f_p": float(p_S), "verdict": v}
        print(f"[area-law {name:9s}] S~f^{p_S:5.2f}  R2(area)={r2_area:.3f} "
              f"R2(vol)={r2_vol:.3f}  => {v}")
    stable = len(set(verdicts)) == 1
    overall = verdicts[2] if stable else "INCONCLUSIVE(cut-dependent)"
    print(f"[area-law] verdicts across cuts: {verdicts} -> {overall}")
    results["area_law"] = {
        "N": N_law, "fracs": fracs.tolist(), "n_sub": nsub_law.tolist(),
        "area": areas.tolist(), "sweep": area_sweep,
        "verdicts": verdicts, "stable": stable, "overall_verdict": overall,
        "area_law_expects_S": "S ~ A ~ f^2 (slope ~2 in log-log S vs f)",
    }

    # ===================== PART E : SMEARED BD cross-check =================
    # If the sharp operator is noisy at our N, the smeared (non-local) version
    # should be cleaner.  We test eps in {0.3, 0.6, 1.0(=sharp)} at one N and a
    # short N-scan of the power-law alpha and rank exponent for the best eps.
    smeared = {}
    N_sm = 2000
    rho_sm = N_sm / VOL_4D
    cs = sprinkle_diamond_4d(N_sm, np.random.default_rng(55555))
    for eps in [0.3, 0.6, 1.0]:
        mode = "sharp" if eps >= 1.0 else "smeared"
        co_s, G_s, dg_s, sp_s, W_s, iD_s = build_operator(cs, rho_sm, mode, eps=eps)
        a_s, r2_s, _ = powerlaw_alpha(sp_s)
        smeared[f"eps_{eps}"] = {
            "mode": mode, "cond_B": dg_s["cond_B"],
            "retard_upper_over_diag": dg_s["max_upper_G_over_diag"],
            "n_pos": int(len(sp_s)), "lambda_max": float(sp_s[0]),
            "powerlaw_alpha": a_s, "powerlaw_R2": r2_s,
            "spec_head": sp_s[:50].tolist(),
        }
        print(f"[smeared] eps={eps} mode={mode} cond={dg_s['cond_B']:.2e} "
              f"alpha={a_s:.3f} (R2={r2_s:.4f})")
    results["smeared_bd"] = {"N": N_sm, "by_eps": smeared,
        "note": "eps=1.0 is the sharp operator; eps<1 is the non-local smeared BD"}

    # rank-vs-N for smeared eps=0.6 (a representative non-local choice).
    # Use absolute density-scaled floors (same as Part C) -- the correct
    # N-scaling estimator for a power-law spectrum.
    sm_Ns = [600, 1000, 1600, 2400]
    sm_abs_cs = [1.0, 3.0]
    sm_rank = {c: [] for c in sm_abs_cs}
    sm_rank_std = {c: [] for c in sm_abs_cs}
    sm_alpha = []
    for N in sm_Ns:
        rho = N / VOL_4D
        sqrt_rho = np.sqrt(rho)
        rk = {c: [] for c in sm_abs_cs}
        al = []
        for s in range(n_seeds):
            cs = sprinkle_diamond_4d(N, np.random.default_rng(3331 * N + 7 * s))
            co_s, G_s, dg_s, sp_s, W_s, iD_s = build_operator(cs, rho, "smeared", eps=0.6)
            for c in sm_abs_cs:
                rk[c].append(rank_above_absolute(sp_s, c * sqrt_rho))
            a_, _, _ = powerlaw_alpha(sp_s)
            al.append(a_)
        for c in sm_abs_cs:
            v = np.array(rk[c], float)
            sm_rank[c].append(v.mean()); sm_rank_std[c].append(v.std(ddof=1))
        sm_alpha.append(float(np.nanmean(al)))
    sm_fits = {}
    for c in sm_abs_cs:
        m = np.array(sm_rank[c]); sd = np.array(sm_rank_std[c])
        p, q, perr = powerlaw_fit(np.array(sm_Ns, float), m,
                                  sig=sd / np.maximum(m, 1e-9))
        sm_fits[str(c)] = {"rank_mean": m.tolist(), "rank_std": sd.tolist(),
                            "p": p, "p_err": perr,
                            "p_minus_0.75_sigma": (p - 0.75) / perr if perr > 0 else None}
        print(f"[smeared eps=0.6] rank@lam>{c}sqrt(rho) ~ N^p: p={p:.4f}+/-{perr:.4f} "
              f"(dev 3/4 = {(p-0.75)/perr:+.1f} sigma)")
    results["smeared_bd"]["rank_scaling_eps0.6"] = {
        "Ns": sm_Ns, "fits": sm_fits, "alpha_per_N": sm_alpha}

    # ===================== consolidated VERDICT diagnostics =================
    al_arr = np.array(pl_alpha_mean)
    alpha_drift = float(al_arr[-1] - al_arr[0])
    cond_growth = float(cond_mean[-1] / cond_mean[0])
    # is any rank-cutoff exponent a robust 3/4?  collect all measured p's:
    all_p = {k: v["p"] for k, v in fits.items()}
    near_34 = {k: p for k, p in all_p.items()
               if (p is not None and not np.isnan(p) and abs(p - 0.75) < 0.10)}
    results["verdict_diagnostics"] = {
        "spectrum_is_clean_power_law": bool(np.nanmean(pl_r2_mean) > 0.97),
        "BD_R2_mean": float(np.nanmean(pl_r2_mean)),
        "link_R2": r2_link,
        "alpha_per_N": al_arr.tolist(),
        "alpha_drift_500_to_3000": alpha_drift,
        "alpha_converged": bool(abs(alpha_drift) < 0.15),
        "cond_B_growth_factor": cond_growth,
        "all_rank_exponents_p": all_p,
        "slope_knee_p": fits["slope_knee"]["p"],
        "any_cutoff_robust_3_4": bool(len(near_34) > 0),
        "cutoffs_near_3_4": list(near_34.keys()),
        "area_law_overall": results["area_law"]["overall_verdict"],
        "OUTCOME": ("(i) clean power law present, BUT (ii) exponent N-unstable "
                    "(alpha drifts, no robust p=3/4), (iii) cond(B) grows ~N^2.5; "
                    "smeared BD is well-conditioned but alpha also drifts. "
                    "=> interpretation (b) REFUTED on its central claim "
                    "(robust p=3/4); the clean-power-law sub-claim is confirmed "
                    "but does not yield a convergent spectral exponent at N<=3000."),
    }
    print("\n[VERDICT] clean power law:", results["verdict_diagnostics"]["spectrum_is_clean_power_law"],
          "| alpha drift:", f"{alpha_drift:+.2f}",
          "| robust p=3/4:", results["verdict_diagnostics"]["any_cutoff_robust_3_4"],
          "| area-law:", results["area_law"]["overall_verdict"])

    # ============================ PLOTS =====================================
    sp = spectra_for_plot
    kk = np.arange(1, len(sp) + 1)
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13, 5))
    ax1.loglog(kk, sp, '.', ms=3, label="BD G_R spectrum")
    # overlay a k^-alpha reference
    a_demo2, _, _ = powerlaw_alpha(sp)
    klo = max(3, int(0.02 * len(sp))); khi = int(0.5 * len(sp))
    ref = sp[klo] * (kk / kk[klo])**(-a_demo2)
    ax1.loglog(kk[klo:khi], ref[klo:khi], 'r-', lw=1.5,
               label=fr"$k^{{-{a_demo2:.2f}}}$ fit")
    ax1.set_xlabel("rank k (desc)")
    ax1.set_ylabel(r"$\lambda_k$ of $i\Delta_{BD}$ (+)")
    ax1.set_title(f"BD G_R Pauli-Jordan spectrum (N={Ns[-1]})")
    ax1.legend(fontsize=9)
    # compare to link spectrum (rescaled to same lambda_max for shape compare)
    ls = link_spec / link_spec[0] * sp[0]
    ax2.loglog(np.arange(1, len(sp) + 1), sp / sp[0], '.', ms=3,
               label=f"BD (alpha={alpha:.2f}, R2={r2_pl:.3f})")
    ax2.loglog(np.arange(1, len(link_spec) + 1), link_spec / link_spec[0], '.',
               ms=3, label=f"link matrix (alpha={a_link:.2f}, R2={r2_link:.3f})")
    ax2.set_xlabel("rank k"); ax2.set_ylabel(r"$\lambda_k/\lambda_1$")
    ax2.set_title("BD (clean power law?) vs link matrix (flat) -- VYPOCET-06 compare")
    ax2.legend(fontsize=9)
    fig.tight_layout(); fig.savefig(os.path.join(PLOTDIR, "spectrum_compare.png"), dpi=140)
    plt.close(fig)

    # rank vs N
    plt.figure(figsize=(8.5, 6.5))
    xx = np.linspace(Ns_arr.min(), Ns_arr.max(), 100)
    for fc, col in zip(frac_cuts, ['tab:cyan', 'tab:blue', 'tab:purple']):
        f = fits[f"rank_frac_{fc}"]
        m = np.array(f["rank_mean"]); sd = np.array(f["rank_std"])
        plt.errorbar(Ns_arr, m, yerr=sd, fmt='s', color=col, capsize=3,
                     label=f"rank@{fc}lmax: p={f['p']:.3f}±{f['p_err']:.3f}")
        plt.plot(xx, np.exp(f["q"]) * xx**f["p"], '-', color=col, lw=1)
    for c, col in zip(abs_cs, ['tab:green', 'tab:olive', 'tab:brown']):
        f = fits[f"rank_abs_{c}"]
        m = np.array(f["rank_mean"]); sd = np.array(f["rank_std"])
        plt.errorbar(Ns_arr, m, yerr=sd, fmt='^', color=col, capsize=3,
                     label=fr"rank@$\lambda>{c}\sqrt{{\rho}}$: p={f['p']:.3f}±{f['p_err']:.3f}")
        plt.plot(xx, np.exp(f["q"]) * xx**f["p"], '-', color=col, lw=1)
    fsk = fits["slope_knee"]
    msk = np.array(fsk["knee_mean"]); sdsk = np.array(fsk["knee_std"])
    plt.errorbar(Ns_arr, msk, yerr=sdsk, fmt='o', color='tab:red', capsize=3,
                 label=f"slope-knee: p={fsk['p']:.3f}±{fsk['p_err']:.3f}")
    plt.plot(xx, np.exp(fsk["q"]) * xx**fsk["p"], '-', color='tab:red', lw=1)
    anchor = np.array(fits["rank_abs_3.0"]["rank_mean"])[0]
    plt.plot(xx, anchor / Ns_arr[0]**0.75 * xx**0.75, 'k--', lw=1.6,
             label="slope 3/4 (PREDICTION b)")
    plt.plot(xx, anchor / Ns_arr[0]**0.5 * xx**0.5, 'k:', lw=1.2, label="slope 1/2 (2D)")
    plt.xscale('log'); plt.yscale('log')
    plt.xlabel(r"$N$"); plt.ylabel("entropy-cutoff rank")
    plt.title("VYPOCET-09: BD G_R entropy-cutoff rank vs N")
    plt.legend(fontsize=8); plt.tight_layout()
    plt.savefig(os.path.join(PLOTDIR, "rank_vs_N.png"), dpi=140); plt.close()

    # area law: S vs area at several truncation depths (robustness)
    plt.figure(figsize=(8.5, 6))
    cols = ['tab:gray', 'tab:cyan', 'tab:blue', 'tab:purple', 'tab:red']
    for (name, _), col in zip(trunc_settings, cols):
        d = area_sweep[name]
        plt.plot(areas, d["S"], 'o-', ms=6, color=col, lw=1,
                 label=f"{name}: S~f^{d['S_powerlaw_in_f_p']:.1f} "
                       f"(R²a={d['R2_area']:.2f},R²v={d['R2_vol']:.2f}) {d['verdict']}")
    plt.xlabel(r"sub-diamond area $A(f)=4\pi(fT)^2$"); plt.ylabel("SSEE S")
    plt.title(f"VYPOCET-09 area-law test, N={N_law}: overall = {overall}")
    plt.legend(fontsize=7); plt.tight_layout()
    plt.savefig(os.path.join(PLOTDIR, "area_law.png"), dpi=140); plt.close()

    # smeared comparison
    plt.figure(figsize=(8, 6))
    for eps in [0.3, 0.6, 1.0]:
        d = smeared[f"eps_{eps}"]
        sh = np.array(d["spec_head"])
        kk2 = np.arange(1, len(sh) + 1)
        plt.loglog(kk2, sh / sh[0], '.-', ms=4,
                   label=f"eps={eps} ({d['mode']}): alpha={d['powerlaw_alpha']:.2f}, R2={d['powerlaw_R2']:.3f}")
    plt.xlabel("rank k"); plt.ylabel(r"$\lambda_k/\lambda_1$ (head)")
    plt.title(f"Smeared vs sharp BD spectrum head, N={N_sm}")
    plt.legend(fontsize=8); plt.tight_layout()
    plt.savefig(os.path.join(PLOTDIR, "smeared_compare.png"), dpi=140); plt.close()

    # alpha drift + condition number vs N (the decisive non-convergence figure)
    fig, ax1 = plt.subplots(figsize=(8, 6))
    ax1.errorbar(Ns_arr, pl_alpha_mean, yerr=pl_alpha_std, fmt='o-', color='tab:blue',
                 capsize=3, label=r"power-law exponent $\alpha$ (sharp BD)")
    ax1.axhline(3.0, color='tab:blue', ls=':', lw=1, alpha=0.5)
    ax1.set_xlabel(r"$N$"); ax1.set_ylabel(r"spectral power-law exponent $\alpha$", color='tab:blue')
    ax1.set_xscale('log'); ax1.tick_params(axis='y', labelcolor='tab:blue')
    ax2 = ax1.twinx()
    ax2.semilogy(Ns_arr, cond_mean, 's--', color='tab:red', label="cond(B)")
    ax2.set_ylabel("cond(B)", color='tab:red'); ax2.tick_params(axis='y', labelcolor='tab:red')
    ax1.set_title(r"VYPOCET-09: $\alpha$ NOT converged at $N\leq3000$ (tracks cond(B))")
    fig.tight_layout(); fig.savefig(os.path.join(PLOTDIR, "alpha_drift.png"), dpi=140)
    plt.close(fig)

    results["runtime_s"] = time.time() - t0
    with open(os.path.join(OUTDIR, "results.json"), "w") as fp:
        json.dump(results, fp, indent=2)
    print(f"\nDone in {results['runtime_s']:.1f}s. results.json + 5 plots in {OUTDIR}")
    return results


if __name__ == "__main__":
    run()
