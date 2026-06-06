#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
VYPOCET-20 : Fix the 4D NULL of VYPOCET-18 with the BENINCASA-DOWKER object
============================================================================
VYPOCET-18 tested H4g-1 (unifying thread, layer B): the diamond-CORNER non-
Hadamard anomaly (VYPOCET-13) marks EXACTLY where the SJ state's modular flow
stops being a geometric boost.  In 2D it REPLICATED (slab boost-local; modular
non-locality rises monotonically toward the diamond corner, slope -0.38,
R2=0.99).  In 4D, using the LINK MATRIX  G_R = (sqrt(rho)/2pi sqrt6) L  as the
SJ Green function, it did NOT replicate: corner f_nl < bulk f_nl (opposite sign
to 2D), nl-vs-corner slope +0.75 (rises AWAY from the corner), slab/diamond
integrated ratio 0.996 (no discrimination).  The suspected cause (stated in
VYPOCET-18 limits): the 4D link matrix is SPARSE with a FLAT/non-power-law
spectrum (~N^0.65, R2~0.92 in VYPOCET-06/09) -- the WRONG dynamical object for
a modular/locality identification.

THIS CALCULATION swaps the dynamical object.  Instead of the link matrix it
uses the BENINCASA-DOWKER (BD) discrete d'Alembertian B and its retarded Green
function  G_R = B^{-1}  -- the SAME object that in VYPOCET-09 FIXED the 4D
spectrum shape (clean power law lambda_k ~ k^{-alpha}, R2 ~ 0.99, vs the flat
link spectrum R2 ~ 0.92).  We re-run the EXACT VYPOCET-18 modular-kernel
geometricity diagnostics with this BD G_R on a 4D slab AND a 4D diamond:

  (1) build G_R = B^{-1} -> iDelta = i(G_R - G_R^T) -> SJ Wightman W on
      4D slab (half-space cut, expect geometric boost) and 4D diamond
      (concentric sub-diamond cut, expect corner non-geometricity).
      N <= 2200 (matrix-inversion bound), >= 3 seeds.
  (2) re-run the modular-kernel diagnostics of VYPOCET-18:
        * off-diagonal decay slope  |K(x,y)| vs |x-y|, slab vs diamond;
        * per-site non-locality vs distance-to-corner (diamond, the KEY curve);
        * diagonal boost-linearity on the slab half-space cut (Bisognano-W.).
  (3) VERDICT: does the BD object RESTORE the 2D mechanism in 4D (corner-
      concentrated non-geometricity), or does 4D genuinely LACK it (then
      H4g-1 is dimension-limited and the through-line's layer B needs
      reformulation)?  EITHER answer is a finding -- nothing is fudged.

----------------------------------------------------------------------------
CONVENTIONS (verified from primary literature, June 2026)
----------------------------------------------------------------------------
SHARP 4D BD d'Alembertian (Benincasa & Dowker, arXiv:1001.2725, eqs 2-3;
PRL 104, 181301 (2010)):
    B phi(x) = (4/(sqrt6 l^2))[ -phi(x)
                + (sum_L1 -9 sum_L2 +16 sum_L3 -8 sum_L4) phi(y) ]
    layer L_i = {y<x : n(x,y)=i-1}, n=(C@C)[x,y]=#elements strictly between.
    l^4 = 1/rho in 4D => prefactor 4/(sqrt6 l^2) = 4 sqrt(rho)/sqrt6.
    Layer coeffs C^(4) = (1,-9,16,-8).
SMEARED / NON-LOCAL BD (Aslanbeigi-Saravani-Sorkin, arXiv:1305.2588 eqs 25-26;
Belenchia et al arXiv:1507.00330):
    B_eps phi(x) = (eps^{1/2} sqrt(rho))[ alpha4 phi(x)
                    + beta4 eps sum_{y<x} f4(n,eps) phi(y) ]
    f4(n,eps) = (1-eps)^n sum_{i=1..4} C_i binom(n,i-1) (eps/(1-eps))^{i-1}
    alpha4 = -4/sqrt6, beta4 = 4/sqrt6, eps=(l/xi)^4 in (0,1]; eps->1 -> sharp.
RETARDEDNESS: B is lower-triangular in time order (y<x => t_y<t_x), so
    G_R = B^{-1} is lower-triangular = retarded.  Verified: max|triu(G_R,1)|/diag
    ~ machine eps.  cond(B) reported per N to flag the conditioning regime.
SJ + modular kernel (dimension-independent, IDENTICAL to VYPOCET-18):
    iDelta = i(G_R - G_R^T), W = positive part of iDelta (SJ Wightman).
    One-particle modular Hamiltonian K(x,y) on region O from the SSEE
    generalized eigenproblem W_O v = mu iDelta_O v, eps_k = ln[mu_k/(mu_k-1)],
    spectral resolution lifted to the site basis (Peschel; Casini-Huerta
    0905.2562; Sorkin-Yazdi 1611.10281).  PROBE uses the UNTRUNCATED SJ kernel
    (the genuine modular flow whose geometricity Bisognano-Wichmann predicts) --
    same methodological choice as VYPOCET-18.

WHY THIS IS THE RIGHT RETRY (not a re-run of the same thing):
    VYPOCET-18 (4D) and VYPOCET-20 differ ONLY in the SJ Green function:
    link matrix L  vs  BD G_R = B^{-1}.  Everything downstream (iDelta, W, the
    modular kernel K, the locality probes, the slab/diamond geometries, the
    corner binning) is byte-for-byte the same algorithm.  So any change in the
    4D verdict is attributable to the dynamical object, isolating the
    VYPOCET-18 hypothesis that link-matrix sparseness/flat spectrum -- not the
    dimension -- killed the corner signature.
"""

import json
import os
import time
from math import comb

for _v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS",
           "VECLIB_MAXIMUM_THREADS", "NUMEXPR_NUM_THREADS"):
    os.environ.setdefault(_v, "4")

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

OUTDIR = os.path.dirname(os.path.abspath(__file__))
PLOTDIR = os.path.join(OUTDIR, "plots")
os.makedirs(PLOTDIR, exist_ok=True)

# BD 4D constants
BD4_C = np.array([1.0, -9.0, 16.0, -8.0])
BD4_ALPHA = -4.0 / np.sqrt(6.0)
BD4_BETA = 4.0 / np.sqrt(6.0)

T_HALF = 1.0
VOL_4D = (2.0 / 3.0) * np.pi * T_HALF**4


# ============================================================================
# GEOMETRY (identical sprinkling to VYPOCET-06/09/18)
# ============================================================================

def sprinkle_diamond_4d(N, rng, T=T_HALF):
    N = int(N)
    U = rng.random(N)
    s = T * U**0.25
    sign = rng.choice([-1.0, 1.0], size=N)
    t = sign * (T - s)
    dirs = rng.normal(size=(N, 3))
    dirs /= np.linalg.norm(dirs, axis=1, keepdims=True)
    V = rng.random(N)
    rr = s * V**(1.0 / 3.0)
    return np.column_stack([t, dirs * rr[:, None]])


def sprinkle_slab_4d(N, rng, T, L):
    N = int(N)
    t = rng.random(N) * T
    x = (rng.random((N, 3)) * 2.0 - 1.0) * L
    return np.column_stack([t, x])


def causal_matrix_4d(coords):
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


# ============================================================================
# BENINCASA-DOWKER operator(s)  (reused verbatim from ssee-bd-4d / VYPOCET-09)
# ============================================================================

def bd_sharp_matrix(C, rho):
    """SHARP 4D BD d'Alembertian as an N x N matrix; layer coeffs (1,-9,16,-8),
       prefactor 4 sqrt(rho)/sqrt6 = 4/(sqrt6 l^2)."""
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
       prefactor sqrt(eps) sqrt(rho); f4(n,eps)=(1-eps)^n sum C_i binom(eps...)."""
    N = C.shape[0]
    Cb = (C > 0)
    nmat = np.rint(C @ C).astype(np.int64)
    pref = np.sqrt(eps) * np.sqrt(rho)
    B = np.zeros((N, N))
    n_vals = nmat[Cb]
    if n_vals.size:
        nmax = int(n_vals.max())
        ftab = np.zeros(nmax + 1)
        one_me = 1.0 - eps
        ratio = eps / one_me if one_me > 0 else 0.0
        for n in range(nmax + 1):
            acc = 0.0
            for i in range(1, 5):
                k = i - 1
                if k <= n:
                    acc += BD4_C[i - 1] * comb(n, k) * (ratio ** k)
            ftab[n] = (one_me ** n) * acc
        B[Cb] = pref * BD4_BETA * eps * ftab[n_vals]
    np.fill_diagonal(B, pref * BD4_ALPHA)
    return B


def green_retarded_from_B(B):
    """G_R = B^{-1}.  B lower-triangular in time order => G_R retarded.
       Returns (G_R, diagnostics)."""
    cond = float(np.linalg.cond(B))
    G = np.linalg.inv(B)
    triu_B = float(np.abs(np.triu(B, 1)).max())
    diag_G = float(np.abs(np.diag(G)).mean()) or 1.0
    triu_G = float(np.abs(np.triu(G, 1)).max())
    return G, {"cond_B": cond, "max_upper_B": triu_B,
               "max_upper_G_over_diag": triu_G / diag_G}


def pauli_jordan(G_R):
    return 1j * (G_R - G_R.T)


def sj_wightman(iDelta, rel_floor=1e-10):
    """SJ Wightman = positive part of iDelta.  Eigenvalues below rel_floor*lmax
       are treated as numerical kernel (avoids amplifying inversion noise) --
       same floor convention as VYPOCET-09."""
    w, V = np.linalg.eigh(iDelta)
    lmax = np.max(np.abs(w)) if w.size else 0.0
    floor = rel_floor * lmax
    pos = w > floor
    W = (V[:, pos] * w[pos]) @ V[:, pos].conj().T
    return W, w, V


def build_bd_sj(coords, rho, mode, eps=None):
    """Time-order (causal refinement), build B (sharp/smeared), G_R=B^{-1},
       iDelta, SJ W.  Returns (coords_ordered, G_R, diag, W, iDelta)."""
    order = np.argsort(coords[:, 0])
    co = coords[order]
    C = causal_matrix_4d(co)
    B = bd_sharp_matrix(C, rho) if mode == "sharp" else bd_smeared_matrix(C, rho, eps)
    G_R, diag = green_retarded_from_B(B)
    iD = pauli_jordan(G_R)
    W, w, V = sj_wightman(iD)
    return co, G_R, diag, W, iD


# ============================================================================
# MODULAR HAMILTONIAN K(x,y)  --  COPIED VERBATIM from VYPOCET-18
# (one-particle K from the SSEE generalized eigenproblem; the only thing that
#  changes vs VYPOCET-18 is the iDelta fed in -- BD instead of link matrix)
# ============================================================================

def modular_kernel_ssee(W, iDelta, sub_idx, kappa=None, tol=1e-9,
                        global_trunc=True):
    iD = iDelta
    Wm = W
    if kappa is not None and global_trunc:
        w, V = np.linalg.eigh(iD)
        keep = np.abs(w) > kappa
        wk = w[keep]; Vk = V[:, keep]
        iD = (Vk * wk) @ Vk.conj().T
        pos = wk > 0
        Wm = (Vk[:, pos] * wk[pos]) @ Vk[:, pos].conj().T

    iD_O = iD[np.ix_(sub_idx, sub_idx)]
    W_O = Wm[np.ix_(sub_idx, sub_idx)]
    n = len(sub_idx)

    d, U = np.linalg.eigh(iD_O)
    scale = np.max(np.abs(d)) if d.size else 0.0
    if scale == 0.0:
        return None
    local_cut = kappa if (kappa is not None) else tol * scale
    keep = np.abs(d) > local_cut
    if keep.sum() < 2:
        return None
    d_k = d[keep]; U_k = U[:, keep]
    Wproj = U_k.conj().T @ W_O @ U_k
    M = (Wproj.T / d_k).T
    mu_all, R = np.linalg.eig(M)
    muR = mu_all.real
    good = (muR > 1.0 + tol) & np.isfinite(muR)
    if good.sum() < 1:
        return None
    mu = muR[good]
    eps = np.log(mu / (mu - 1.0))
    nu = mu - 0.5
    S = float(np.sum((nu + 0.5) * np.log(nu + 0.5) - (nu - 0.5) * np.log(nu - 0.5)))

    with np.errstate(divide='ignore', invalid='ignore'):
        muf, Rf = np.linalg.eig(M)
        zf = muf / (muf - 1.0)
        epsf = np.log(np.abs(zf)) * np.sign(muf.real - 0.5)
        epsf = np.where(np.isfinite(epsf), epsf, 0.0)
        Kdiag = np.diag(epsf.astype(complex))
        try:
            Rf_inv = np.linalg.inv(Rf)
            Km = Rf @ Kdiag @ Rf_inv
        except np.linalg.LinAlgError:
            Km = U_k.conj().T @ U_k * 0.0
    K_site = U_k @ Km @ U_k.conj().T
    K_site = 0.5 * (K_site + K_site.conj().T)
    return {"K": K_site, "eps": np.sort(eps), "S": S, "nu": np.sort(nu),
            "n": n, "n_modes": int(good.sum())}


# ============================================================================
# LOCALITY PROFILE  --  COPIED VERBATIM from VYPOCET-18
# ============================================================================

def locality_profile(K, coords_sub, n_dist_bins=18):
    n = K.shape[0]
    Kabs = np.abs(K)
    xs = coords_sub[:, 1:]
    diff = xs[:, None, :] - xs[None, :, :]
    Dij = np.sqrt(np.einsum('ijk,ijk->ij', diff, diff))
    iu = np.triu_indices(n, k=1)
    dvals = Dij[iu]
    kvals = Kabs[iu]
    dmax = np.percentile(dvals, 99) if dvals.size else 1.0
    bins = np.linspace(0, dmax, n_dist_bins + 1)
    centers = 0.5 * (bins[:-1] + bins[1:])
    idx = np.digitize(dvals, bins)
    prof = np.full(n_dist_bins, np.nan)
    cnt = np.zeros(n_dist_bins, int)
    for b in range(1, n_dist_bins + 1):
        m = idx == b
        cnt[b - 1] = m.sum()
        if m.sum() > 0:
            prof[b - 1] = np.mean(kvals[m])
    diag = np.real(np.diag(K))
    return {"dist_centers": centers, "offdiag_mean": prof, "offdiag_count": cnt,
            "Dij": Dij, "Kabs": Kabs, "diag": diag, "xs": xs}


def nonlocal_fraction(Kabs, Dij, near_radius):
    n = Kabs.shape[0]
    off = ~np.eye(n, dtype=bool)
    K2 = Kabs**2
    tot = K2[off].sum()
    if tot <= 0:
        return np.nan
    far = off & (Dij > near_radius)
    return float(K2[far].sum() / tot)


def _rowfrac_subset(Kabs, Dij, near_r, mask):
    K2 = Kabs**2
    np.fill_diagonal(K2, 0.0)
    rowtot = K2.sum(axis=1)
    farmask = (Dij > near_r)
    np.fill_diagonal(farmask, False)
    rowfar = (K2 * farmask).sum(axis=1)
    with np.errstate(divide='ignore', invalid='ignore'):
        nl = np.where(rowtot > 0, rowfar / rowtot, np.nan)
    sel = nl[mask]
    sel = sel[np.isfinite(sel)]
    return float(np.mean(sel)) if sel.size else np.nan


def offdiag_slope_subset(Kabs, Dij, row_mask, n_bins=16):
    rows = np.where(row_mask)[0]
    if rows.size < 3:
        return None, None, None, None
    dsub = Dij[rows][:, :]
    ksub = Kabs[rows][:, :]
    dv = dsub.ravel(); kv = ksub.ravel()
    keep = dv > 1e-9
    dv = dv[keep]; kv = kv[keep]
    if dv.size < 10:
        return None, None, None, None
    dmax = np.percentile(dv, 97)
    bins = np.linspace(0, dmax, n_bins + 1)
    centers = 0.5 * (bins[:-1] + bins[1:])
    idx = np.digitize(dv, bins)
    prof = np.full(n_bins, np.nan); cnt = np.zeros(n_bins, int)
    for b in range(1, n_bins + 1):
        m = idx == b
        cnt[b - 1] = m.sum()
        if m.sum() > 0:
            prof[b - 1] = np.mean(kv[m])
    sl, _, r2v = loglog_slope(centers, prof, mask=cnt >= 8)
    return sl, r2v, centers, prof


def _nl_vs_corner_generic(Kabs, Dij, dcorn, near_r, n_zones=6):
    K2 = Kabs**2
    np.fill_diagonal(K2, 0.0)
    rowtot = K2.sum(axis=1)
    farmask = (Dij > near_r)
    np.fill_diagonal(farmask, False)
    rowfar = (K2 * farmask).sum(axis=1)
    with np.errstate(divide='ignore', invalid='ignore'):
        nl = np.where(rowtot > 0, rowfar / rowtot, np.nan)
    good = np.isfinite(nl)
    dc = dcorn[good]; nlv = nl[good]
    if dc.size < n_zones:
        return None
    qs = np.linspace(0, 1, n_zones + 1)
    edges = np.quantile(dc, qs)
    edges[0] -= 1e-9; edges[-1] += 1e-9
    cen, mn = [], []
    for b in range(n_zones):
        m = (dc >= edges[b]) & (dc < edges[b + 1])
        if m.sum() == 0:
            continue
        cen.append(float(np.mean(dc[m]))); mn.append(float(np.mean(nlv[m])))
    return np.array(cen), np.array(mn)


def diag_weight_vs_distance(diag, coords_sub, surface_normal_coord=1,
                            surface_value=0.0, n_bins=14, use_abs_x=True):
    xcoord = coords_sub[:, surface_normal_coord]
    dist = np.abs(xcoord - surface_value) if use_abs_x else (xcoord - surface_value)
    order = np.argsort(dist)
    dist = dist[order]; w = np.abs(diag)[order]
    bins = np.linspace(dist.min(), np.percentile(dist, 98), n_bins + 1)
    centers = 0.5 * (bins[:-1] + bins[1:])
    idx = np.digitize(dist, bins)
    prof = np.full(n_bins, np.nan); cnt = np.zeros(n_bins, int)
    for b in range(1, n_bins + 1):
        m = idx == b
        cnt[b - 1] = m.sum()
        if m.sum() > 0:
            prof[b - 1] = np.mean(w[m])
    return centers, prof, cnt


# ============================================================================
# FIT HELPERS  (verbatim)
# ============================================================================

def r2(y, yhat):
    y = np.asarray(y, float)
    ss = np.sum((y - y.mean())**2)
    return 1.0 - np.sum((y - yhat)**2) / ss if ss > 0 else 0.0


def loglog_slope(x, y, mask=None):
    x = np.asarray(x, float); y = np.asarray(y, float)
    m = np.isfinite(x) & np.isfinite(y) & (x > 0) & (y > 0)
    if mask is not None:
        m &= mask
    if m.sum() < 3:
        return None, None, None
    lx = np.log(x[m]); ly = np.log(y[m])
    A = np.vstack([lx, np.ones_like(lx)]).T
    coef, *_ = np.linalg.lstsq(A, ly, rcond=None)
    return float(coef[0]), float(coef[1]), float(r2(ly, A @ coef))


def linfit(x, y, mask=None):
    x = np.asarray(x, float); y = np.asarray(y, float)
    m = np.isfinite(x) & np.isfinite(y)
    if mask is not None:
        m &= mask
    if m.sum() < 2:
        return None, None, None
    A = np.vstack([x[m], np.ones(m.sum())]).T
    coef, *_ = np.linalg.lstsq(A, y[m], rcond=None)
    return float(coef[0]), float(coef[1]), float(r2(y[m], A @ coef))


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


# ============================================================================
# 4D EXPERIMENT with the BD object:  slab vs diamond, bulk vs corner
# The ONLY difference vs VYPOCET-18 run_4d is build_bd_sj (BD G_R) replacing
# green_retarded_4d(link_matrix(C), rho).  All probes are identical.
# ============================================================================

def run_4d_bd(mode, eps, Ns, n_seeds, time_budget_s, t_start, tag):
    print(f"\n==== 4D BD modular-flow geometricity ({tag}) "
          f"mode={mode} eps={eps} ====")
    diamond = {N: {"f_nl_all": [], "f_nl_bulk": [], "f_nl_corner": [],
                   "off_slope_all": [], "off_R2_all": [],
                   "off_slope_bulk": [], "off_slope_corner": [],
                   "nl_vs_corner_centers": [], "nl_vs_corner_mean": [],
                   "cond_B": [], "S": []} for N in Ns}
    slab = {N: {"f_nl_all": [], "off_slope": [], "off_R2": [],
                "diag_slope_lin": [], "diag_R2_lin": [], "cond_B": [], "S": []}
            for N in Ns}
    T_slab, L_slab = 0.5, 0.85
    f = 0.6   # concentric sub-diamond fraction (same as VYPOCET-18)

    for N in Ns:
        if t_start is not None and (time.time() - t_start) > time_budget_s:
            print(f"  [time budget reached, stopping 4D at N<{N}]")
            break
        for s in range(n_seeds):
            # ---------------- DIAMOND ----------------
            rng = np.random.default_rng(20_000_000 + 1000 * N + s)
            coords = sprinkle_diamond_4d(N, rng, T_HALF)
            rho = N / VOL_4D
            co, G_R, dg, W, iD = build_bd_sj(coords, rho, mode, eps)
            tt = np.abs(co[:, 0]); rr = np.linalg.norm(co[:, 1:], axis=1)
            sub = np.where(tt + rr <= f * T_HALF)[0]
            mk = modular_kernel_ssee(W, iD, sub, kappa=None)   # UNTRUNCATED probe
            if mk is not None and mk["K"].shape[0] >= 16:
                K = mk["K"]; csub = co[sub]
                lp = locality_profile(K, csub)
                nn = rho**(-0.25)
                near_r = 3.0 * nn
                diamond[N]["f_nl_all"].append(
                    nonlocal_fraction(lp["Kabs"], lp["Dij"], near_r))
                diamond[N]["S"].append(mk["S"])
                diamond[N]["cond_B"].append(dg["cond_B"])
                sl_all, r2_all, _, _ = offdiag_slope_subset(
                    lp["Kabs"], lp["Dij"], np.ones(K.shape[0], bool))
                if sl_all is not None:
                    diamond[N]["off_slope_all"].append(sl_all)
                    diamond[N]["off_R2_all"].append(r2_all)
                # distance-to-corner: proximity to the null tip (t->f, r->0)
                rsub = np.linalg.norm(csub[:, 1:], axis=1)
                tsub = np.abs(csub[:, 0])
                dcorn = np.sqrt((tsub - f)**2 + rsub**2)
                near_corn = dcorn <= np.percentile(dcorn, 30)
                bulk = dcorn > np.median(dcorn)
                diamond[N]["f_nl_corner"].append(
                    _rowfrac_subset(lp["Kabs"], lp["Dij"], near_r, near_corn))
                diamond[N]["f_nl_bulk"].append(
                    _rowfrac_subset(lp["Kabs"], lp["Dij"], near_r, bulk))
                slb, _, _, _ = offdiag_slope_subset(lp["Kabs"], lp["Dij"], bulk)
                slc, _, _, _ = offdiag_slope_subset(lp["Kabs"], lp["Dij"], near_corn)
                if slb is not None:
                    diamond[N]["off_slope_bulk"].append(slb)
                if slc is not None:
                    diamond[N]["off_slope_corner"].append(slc)
                nvc = _nl_vs_corner_generic(lp["Kabs"], lp["Dij"], dcorn,
                                            near_r, n_zones=6)
                if nvc is not None:
                    diamond[N]["nl_vs_corner_centers"].append(nvc[0].tolist())
                    diamond[N]["nl_vs_corner_mean"].append(nvc[1].tolist())

            # ---------------- SLAB ----------------
            rng2 = np.random.default_rng(30_000_000 + 1000 * N + s)
            vol_s = T_slab * (2 * L_slab)**3
            coords_s = sprinkle_slab_4d(N, rng2, T_slab, L_slab)
            rho_s = N / vol_s
            co_s, G_s, dg_s, Ws, iDs = build_bd_sj(coords_s, rho_s, mode, eps)
            interior = ((np.abs(co_s[:, 2]) < 0.7 * L_slab) &
                        (np.abs(co_s[:, 3]) < 0.7 * L_slab))
            sub_s = np.where(interior & (co_s[:, 1] > 0.0))[0]
            mks = modular_kernel_ssee(Ws, iDs, sub_s, kappa=None)  # UNTRUNCATED
            if mks is not None and mks["K"].shape[0] >= 16:
                Ks = mks["K"]; css = co_s[sub_s]
                lps = locality_profile(Ks, css)
                nn_s = rho_s**(-0.25)
                near_rs = 3.0 * nn_s
                slab[N]["f_nl_all"].append(
                    nonlocal_fraction(lps["Kabs"], lps["Dij"], near_rs))
                slab[N]["S"].append(mks["S"])
                slab[N]["cond_B"].append(dg_s["cond_B"])
                sl_off, r2_off, _, _ = offdiag_slope_subset(
                    lps["Kabs"], lps["Dij"], np.ones(Ks.shape[0], bool))
                if sl_off is not None:
                    slab[N]["off_slope"].append(sl_off)
                    slab[N]["off_R2"].append(r2_off)
                cen, prof, cnt = diag_weight_vs_distance(
                    lps["diag"], css, surface_normal_coord=1, surface_value=0.0)
                sl_lin, _, r2lin = linfit(cen, prof, mask=cnt >= 5)
                if sl_lin is not None:
                    slab[N]["diag_slope_lin"].append(sl_lin)
                    slab[N]["diag_R2_lin"].append(r2lin)
        print(f"  [N={N:4d}] diamond f_nl={_m(diamond[N]['f_nl_all']):.3f} "
              f"(bulk {_m(diamond[N]['f_nl_bulk']):.3f}, corner {_m(diamond[N]['f_nl_corner']):.3f}) "
              f"off={_m(diamond[N]['off_slope_all']):.2f}; "
              f"slab f_nl={_m(slab[N]['f_nl_all']):.3f} off={_m(slab[N]['off_slope']):.2f} "
              f"diagR2={_m(slab[N]['diag_R2_lin']):.2f}; "
              f"cond_dia={_m(diamond[N]['cond_B']):.1e}")

    def agg(d, key):
        return [float(np.mean(d[N][key])) if len(d[N][key]) else np.nan for N in Ns]

    def aggstd(d, key):
        return [float(np.std(d[N][key])) if len(d[N][key]) > 1 else 0.0 for N in Ns]

    res = {
        "mode": mode, "eps": eps, "Ns": Ns, "n_seeds": n_seeds,
        "diamond_f_nl_all": agg(diamond, "f_nl_all"),
        "diamond_f_nl_all_std": aggstd(diamond, "f_nl_all"),
        "diamond_f_nl_bulk": agg(diamond, "f_nl_bulk"),
        "diamond_f_nl_bulk_std": aggstd(diamond, "f_nl_bulk"),
        "diamond_f_nl_corner": agg(diamond, "f_nl_corner"),
        "diamond_f_nl_corner_std": aggstd(diamond, "f_nl_corner"),
        "diamond_off_slope_all": agg(diamond, "off_slope_all"),
        "diamond_off_R2_all": agg(diamond, "off_R2_all"),
        "diamond_off_slope_bulk": agg(diamond, "off_slope_bulk"),
        "diamond_off_slope_corner": agg(diamond, "off_slope_corner"),
        "diamond_cond_B": agg(diamond, "cond_B"),
        "slab_f_nl_all": agg(slab, "f_nl_all"),
        "slab_f_nl_all_std": aggstd(slab, "f_nl_all"),
        "slab_off_slope": agg(slab, "off_slope"),
        "slab_off_R2": agg(slab, "off_R2"),
        "slab_diag_slope_lin": agg(slab, "diag_slope_lin"),
        "slab_diag_R2_lin": agg(slab, "diag_R2_lin"),
        "slab_cond_B": agg(slab, "cond_B"),
    }
    # representative nl-vs-corner curve (largest N reached, seed-averaged)
    Nrep = None
    for N in reversed(Ns):
        if diamond[N]["nl_vs_corner_centers"]:
            Nrep = N; break
    if Nrep is not None:
        cc = diamond[Nrep]["nl_vs_corner_centers"]
        mm = diamond[Nrep]["nl_vs_corner_mean"]
        Lmin = min(len(c) for c in cc)
        cmat = np.array([c[:Lmin] for c in cc])
        mmat = np.array([m[:Lmin] for m in mm])
        res["nl_vs_corner_repN"] = Nrep
        res["nl_vs_corner_dist"] = cmat.mean(axis=0).tolist()
        res["nl_vs_corner_mean"] = mmat.mean(axis=0).tolist()
        res["nl_vs_corner_sem"] = (mmat.std(axis=0) /
                                   max(1, np.sqrt(mmat.shape[0]))).tolist()
        sl_c, _, r2_c = linfit(cmat.mean(axis=0), mmat.mean(axis=0))
        res["nl_vs_corner_slope"] = sl_c
        res["nl_vs_corner_R2"] = r2_c
    return _to_native(res)


# ============================================================================
# VERDICT LOGIC  (the 4D geometricity signatures, mirroring VYPOCET-18)
# ============================================================================

def build_verdict(res, link_baseline):
    """res = BD 4D result block (primary, e.g. smeared eps=0.6).
       link_baseline = the VYPOCET-18 link-matrix 4D numbers (for the
       did-the-object-matter comparison)."""
    v = {}
    Ns = res["Ns"]

    def tail(a, k=2):
        a = np.array(a, float); a = a[np.isfinite(a)]
        return float(np.mean(a[-k:])) if a.size else np.nan

    d_all = tail(res["diamond_f_nl_all"])
    d_bulk = tail(res["diamond_f_nl_bulk"])
    d_corn = tail(res["diamond_f_nl_corner"])
    s_all = tail(res["slab_f_nl_all"])
    v["diamond_nonlocal_frac_tail"] = d_all
    v["diamond_bulk_nonlocal_frac_tail"] = d_bulk
    v["diamond_corner_nonlocal_frac_tail"] = d_corn
    v["slab_nonlocal_frac_tail"] = s_all

    slab_off = tail(res["slab_off_slope"])
    dia_off = tail(res["diamond_off_slope_all"])
    bulk_off = tail(res["diamond_off_slope_bulk"])
    corn_off = tail(res["diamond_off_slope_corner"])
    v["slab_offdiag_slope_tail"] = slab_off
    v["diamond_offdiag_slope_tail"] = dia_off
    v["diamond_bulk_offdiag_slope_tail"] = bulk_off
    v["diamond_corner_offdiag_slope_tail"] = corn_off

    # (1) slab kernel more local than diamond (steeper off-diagonal decay)?
    slab_more_local = bool(np.isfinite(slab_off) and np.isfinite(dia_off)
                           and slab_off < dia_off - 0.1)
    v["slab_more_local_than_diamond"] = slab_more_local
    v["slab_vs_diamond_slope_gap"] = (float(dia_off - slab_off)
        if np.isfinite(slab_off) and np.isfinite(dia_off) else np.nan)
    v["slab_vs_diamond_fnl_ratio"] = (float(s_all / d_all)
        if np.isfinite(s_all) and np.isfinite(d_all) and d_all > 0 else np.nan)

    # (2) within diamond: non-locality CONCENTRATES at corner?
    corner_flatter = bool(np.isfinite(corn_off) and np.isfinite(bulk_off)
                          and corn_off > bulk_off)
    corner_more_nonlocal = bool(np.isfinite(d_corn) and np.isfinite(d_bulk)
                                and d_corn > d_bulk)
    v["corner_offdiag_flatter_than_bulk"] = corner_flatter
    v["corner_more_nonlocal_than_bulk"] = corner_more_nonlocal
    v["corner_vs_bulk_ratio"] = (float(d_corn / d_bulk)
        if np.isfinite(d_corn) and np.isfinite(d_bulk) and d_bulk > 0 else np.nan)

    # (3) non-locality rises TOWARD the corner (negative slope vs dist-to-corner)
    sl_c = res.get("nl_vs_corner_slope", np.nan)
    rises_toward_corner = bool(np.isfinite(sl_c) and sl_c < 0)
    v["nonlocality_rises_toward_corner"] = rises_toward_corner
    v["nl_vs_corner_slope"] = sl_c
    v["nl_vs_corner_R2"] = res.get("nl_vs_corner_R2", np.nan)

    # (4) slab diagonal boost-weight linear (Bisognano-Wichmann)?
    slab_lin_R2 = tail(res["slab_diag_R2_lin"])
    v["slab_diag_boost_linear_R2_tail"] = slab_lin_R2
    slab_boost_linear = bool(np.isfinite(slab_lin_R2) and slab_lin_R2 > 0.6)
    v["slab_diag_boost_linear"] = slab_boost_linear

    # HONEST NULL checks (identical logic to VYPOCET-18)
    tiny_gap = (np.isfinite(v["slab_vs_diamond_slope_gap"]) and
                abs(v["slab_vs_diamond_slope_gap"]) < 0.08)
    flat_corner = (np.isfinite(v["corner_vs_bulk_ratio"]) and
                   0.92 < v["corner_vs_bulk_ratio"] < 1.08 and not corner_flatter)
    v["null_discreteness_dominates"] = bool(tiny_gap and flat_corner)
    v["null_no_corner_structure"] = bool(
        not corner_more_nonlocal and not corner_flatter
        and not rises_toward_corner and not slab_more_local)

    # geometricity signature count (same 5 as VYPOCET-18, minus cross-corner)
    support = (int(slab_more_local) + int(corner_flatter) +
               int(corner_more_nonlocal) + int(rises_toward_corner) +
               int(slab_boost_linear))
    v["n_signatures_supporting_H4g1"] = int(support)
    corner_score = (int(corner_flatter) + int(corner_more_nonlocal) +
                    int(rises_toward_corner))
    v["corner_structure_score"] = int(corner_score)
    v["signatures"] = {
        "slab_more_local_offdiag": slab_more_local,
        "slab_boost_weight_linear": slab_boost_linear,
        "corner_offdiag_flatter": corner_flatter,
        "corner_more_nonlocal": corner_more_nonlocal,
        "nonlocality_rises_toward_corner": rises_toward_corner,
    }

    # CORNER-CONCENTRATION REPLICATION TEST (the headline VYPOCET-20 question):
    #   does the BD object restore the 2D mechanism (corner-concentrated
    #   non-geometricity)?  Requires BOTH the corner-zone metric (corner more
    #   non-local than bulk) AND the monotonic curve (nl rises toward corner).
    corner_concentration_replicates = bool(corner_more_nonlocal and
                                            rises_toward_corner)
    v["corner_concentration_replicates"] = corner_concentration_replicates

    # did swapping the object actually change the corner verdict vs VYPOCET-18?
    lb = link_baseline
    v["link_baseline"] = lb
    v["corner_sign_flipped_vs_link"] = bool(
        np.isfinite(sl_c) and np.isfinite(lb.get("nl_vs_corner_slope", np.nan))
        and np.sign(sl_c) != np.sign(lb["nl_vs_corner_slope"]))

    if corner_concentration_replicates:
        v["overall"] = (
            "BD OBJECT RESTORES the 2D mechanism in 4D: modular non-geometricity "
            "is corner-concentrated (corner more non-local than bulk AND nl rises "
            "toward the corner). H4g-1 layer B extends to 4D with the BD G_R; the "
            "VYPOCET-18 4D null was a LINK-MATRIX artefact (sparse/flat spectrum).")
        v["H4g1_4D"] = "restored"
    elif slab_boost_linear and not v["null_no_corner_structure"]:
        v["overall"] = (
            "4D PARTIAL with BD: slab boost-weight is recovered "
            f"(linear R2={slab_lin_R2:.2f}) but the corner-concentration of "
            "non-geometricity does NOT cleanly replicate (corner_more_nonlocal="
            f"{corner_more_nonlocal}, nl_rises_toward_corner={rises_toward_corner}). "
            "Slab geometricity is dimension-robust; the corner sub-claim is not "
            "restored by the BD object alone at N<=2200.")
        v["H4g1_4D"] = "partial"
    else:
        v["overall"] = (
            "4D GENUINELY LACKS the 2D corner mechanism even with the BD object: "
            f"corner_more_nonlocal={corner_more_nonlocal}, "
            f"nl_vs_corner_slope={sl_c:.3g} (>=0 means rises AWAY from corner). "
            "Swapping link->BD did not restore corner concentration => H4g-1 "
            "layer B is DIMENSION-LIMITED; the through-line's layer B needs "
            "reformulation in 4D.")
        v["H4g1_4D"] = "dimension_limited"
    return v


# ============================================================================
# PLOTS
# ============================================================================

def make_plots(bd_primary, bd_sharp, link_baseline, verdict):
    # Plot 1: non-local fraction vs N -- slab vs diamond (bulk vs corner), BD
    for res, tag, fname in [(bd_primary, f"BD smeared eps={bd_primary['eps']}",
                             "nonlocality_vs_N_bd_4d.png")]:
        Ns = np.array(res["Ns"], float)
        fig, ax = plt.subplots(figsize=(8.5, 6))
        ax.errorbar(Ns, res["diamond_f_nl_all"], yerr=res["diamond_f_nl_all_std"],
                    fmt='o-', color='tab:red', capsize=3, label="diamond cut (all)")
        ax.errorbar(Ns, res["diamond_f_nl_corner"], yerr=res["diamond_f_nl_corner_std"],
                    fmt='^-', color='darkred', capsize=3, label="diamond NEAR-CORNER")
        ax.errorbar(Ns, res["diamond_f_nl_bulk"], yerr=res["diamond_f_nl_bulk_std"],
                    fmt='v-', color='salmon', capsize=3, label="diamond BULK")
        ax.errorbar(Ns, res["slab_f_nl_all"], yerr=res["slab_f_nl_all_std"],
                    fmt='s-', color='tab:blue', capsize=3, label="slab half-space cut")
        ax.set_xlabel("N"); ax.set_ylabel(r"non-local fraction of $\|K\|_{HS}^2$")
        ax.set_title(f"VYPOCET-20: 4D BD modular non-locality ({tag})\n"
                     + verdict["H4g1_4D"])
        ax.legend(fontsize=9); ax.grid(alpha=0.3)
        fig.tight_layout(); fig.savefig(os.path.join(PLOTDIR, fname), dpi=140)
        plt.close(fig)

    # Plot 2: nl vs distance-to-corner -- BD primary vs BD sharp vs link baseline
    fig, ax = plt.subplots(figsize=(8.5, 6))
    for res, col, lab in [
            (bd_primary, 'tab:red',
             f"BD smeared eps={bd_primary['eps']} (slope={bd_primary.get('nl_vs_corner_slope', np.nan):.3g})"),
            (bd_sharp, 'tab:purple',
             f"BD sharp (slope={bd_sharp.get('nl_vs_corner_slope', np.nan):.3g})")]:
        if "nl_vs_corner_dist" in res:
            d = np.array(res["nl_vs_corner_dist"]); m = np.array(res["nl_vs_corner_mean"])
            se = np.array(res.get("nl_vs_corner_sem", np.zeros_like(m)))
            ax.errorbar(d, m, yerr=se, fmt='o-', color=col, capsize=4, label=lab)
    if link_baseline.get("nl_vs_corner_dist"):
        d = np.array(link_baseline["nl_vs_corner_dist"])
        m = np.array(link_baseline["nl_vs_corner_mean"])
        ax.plot(d, m, 's--', color='gray',
                label=f"VYPOCET-18 link matrix (slope={link_baseline.get('nl_vs_corner_slope', np.nan):.3g})")
    ax.set_xlabel("distance to diamond corner/tip")
    ax.set_ylabel("per-site non-local fraction")
    ax.set_title("VYPOCET-20 KEY CURVE: 4D modular non-locality vs distance-to-corner\n"
                 "negative slope = rises TOWARD corner (2D mechanism); +slope = away (VYPOCET-18 null)")
    ax.legend(fontsize=8); ax.grid(alpha=0.3)
    fig.tight_layout(); fig.savefig(os.path.join(PLOTDIR, "nonlocality_vs_corner_bd_4d.png"), dpi=140)
    plt.close(fig)

    # Plot 3: slab diagnostics -- off-diagonal slope and diagonal boost linearity
    fig, (axa, axb) = plt.subplots(1, 2, figsize=(13, 5.5))
    Ns = np.array(bd_primary["Ns"], float)
    axa.plot(Ns, bd_primary["slab_off_slope"], 's-', color='tab:blue', label="slab off-slope (BD)")
    axa.plot(Ns, bd_primary["diamond_off_slope_all"], 'o-', color='tab:red', label="diamond off-slope (BD)")
    axa.axhline(0, color='k', ls=':', lw=1)
    axa.set_xlabel("N"); axa.set_ylabel("off-diagonal log-log slope")
    axa.set_title("Off-diagonal decay: slab (local boost) vs diamond")
    axa.legend(fontsize=9); axa.grid(alpha=0.3)
    axb.plot(Ns, bd_primary["slab_diag_R2_lin"], 'D-', color='tab:green',
             label="slab diagonal boost-linearity R2")
    axb.axhline(0.6, color='k', ls=':', lw=1, label="support threshold 0.6")
    axb.set_xlabel("N"); axb.set_ylabel(r"$R^2$ of $|K(x,x)|$ vs distance (linear)")
    axb.set_title("Slab diagonal boost weight linearity (Bisognano-Wichmann)")
    axb.set_ylim(0, 1.02)
    axb.legend(fontsize=9); axb.grid(alpha=0.3)
    fig.tight_layout(); fig.savefig(os.path.join(PLOTDIR, "slab_diagnostics_bd_4d.png"), dpi=140)
    plt.close(fig)

    # Plot 4: object comparison -- corner/bulk f_nl ratio, BD vs link
    fig, ax = plt.subplots(figsize=(8, 6))
    labels, ratios, cols = [], [], []
    for res, lab, col in [(bd_primary, "BD smeared", 'tab:red'),
                          (bd_sharp, "BD sharp", 'tab:purple')]:
        def tail(a):
            a = np.array(a, float); a = a[np.isfinite(a)]
            return float(np.mean(a[-2:])) if a.size else np.nan
        c = tail(res["diamond_f_nl_corner"]); b = tail(res["diamond_f_nl_bulk"])
        labels.append(lab); ratios.append(c / b if b > 0 else np.nan); cols.append(col)
    lb = link_baseline
    if np.isfinite(lb.get("corner_over_bulk", np.nan)):
        labels.append("link (VYP-18)"); ratios.append(lb["corner_over_bulk"]); cols.append('gray')
    ax.bar(labels, ratios, color=cols)
    ax.axhline(1.0, color='k', ls='--', lw=1.5, label="corner = bulk (no concentration)")
    ax.axhline(1.15, color='tab:green', ls=':', lw=1.5, label="2D value 1.15 (corner-concentrated)")
    ax.set_ylabel("corner f_nl / bulk f_nl  (>1 = corner-concentrated)")
    ax.set_title("VYPOCET-20: does the BD object concentrate non-geometricity at the corner?")
    ax.legend(fontsize=9); ax.grid(alpha=0.3, axis='y')
    fig.tight_layout(); fig.savefig(os.path.join(PLOTDIR, "corner_concentration_object_compare.png"), dpi=140)
    plt.close(fig)


# ============================================================================
def load_link_baseline():
    """Pull the VYPOCET-18 link-matrix 4D numbers from its results.json for the
       object-comparison (so the contrast is exact, not transcribed)."""
    path = os.path.join(os.path.dirname(OUTDIR), "modular-flow-corner", "results.json")
    out = {"nl_vs_corner_slope": np.nan, "corner_over_bulk": np.nan,
           "nl_vs_corner_dist": None, "nl_vs_corner_mean": None}
    try:
        r = json.load(open(path))
        p4 = r.get("part_4d", {})
        out["nl_vs_corner_slope"] = p4.get("nl_vs_corner_slope", np.nan)
        out["nl_vs_corner_dist"] = p4.get("nl_vs_corner_dist")
        out["nl_vs_corner_mean"] = p4.get("nl_vs_corner_mean")
        cd = r["VERDICT"].get("d4_corner_nonlocal_tail", np.nan)
        bd = r["VERDICT"].get("d4_bulk_nonlocal_tail", np.nan)
        out["corner_nonlocal_tail"] = cd
        out["bulk_nonlocal_tail"] = bd
        out["slab_vs_diamond_fnl_ratio"] = r["VERDICT"].get("d4_slab_vs_diamond_fnl_ratio", np.nan)
        out["corner_over_bulk"] = float(cd / bd) if (np.isfinite(cd) and np.isfinite(bd) and bd > 0) else np.nan
    except Exception as e:
        out["error"] = str(e)
    return out


def run():
    t0 = time.time()
    results = {
        "task": "VYPOCET-20: fix the 4D null of VYPOCET-18 with the BD object (H4g-1)",
        "claim": ("the diamond-corner non-Hadamard anomaly marks exactly where "
                  "the SJ modular flow stops being a geometric boost; test whether "
                  "the BD G_R=B^{-1} restores this 2D mechanism in 4D where the "
                  "link matrix failed"),
        "conventions": {
            "object": "BD discrete d'Alembertian B; retarded Green function G_R=B^{-1}",
            "BD_sharp_4D": "layers (1,-9,16,-8), prefactor 4 sqrt(rho)/sqrt6; arXiv:1001.2725",
            "BD_smeared_4D": "alpha4=-4/sqrt6, beta4=4/sqrt6, f4(n,eps); arXiv:1305.2588/1507.00330",
            "iDelta": "i(G_R-G_R^T); W=positive part (SJ)",
            "modular_kernel": ("one-particle K(x,y) from SSEE generalized eigenproblem "
                               "W_O v=mu iDelta_O v; eps=ln[mu/(mu-1)]; spectral resolution "
                               "lifted to site basis (Peschel; Casini-Huerta 0905.2562)"),
            "probe": "UNTRUNCATED SJ modular kernel (kappa=None), same as VYPOCET-18",
            "geometry": "4D diamond {|t|+|r|<=fT}, f=0.6 sub-cut; slab {0<t<0.5,|x|<0.85} half-space",
            "vs_VYPOCET18": ("ONLY the 4D Green function changes: link matrix L -> BD G_R=B^{-1}; "
                             "all downstream probes byte-for-byte identical"),
        }}

    link_baseline = load_link_baseline()
    results["link_baseline_VYPOCET18"] = _to_native(link_baseline)
    print("=== VYPOCET-18 link-matrix 4D baseline (for object comparison) ===")
    print(f"  nl_vs_corner_slope={link_baseline['nl_vs_corner_slope']}  "
          f"corner/bulk={link_baseline['corner_over_bulk']}  "
          f"slab/diamond f_nl={link_baseline.get('slab_vs_diamond_fnl_ratio')}")

    # N<=2200 matrix-inversion bound; >=3 seeds (task spec)
    Ns = [800, 1200, 1700, 2200]
    n_seeds = 3
    BUDGET = 5400

    # PRIMARY: smeared eps=0.6 (well-conditioned: cond(B)~1e5-1e6 on the diamond,
    # vs sharp ~1e8-1e9; the spectrum-fixing BD object with controlled inversion).
    bd_primary = run_4d_bd("smeared", 0.6, Ns, n_seeds, BUDGET, t0, "PRIMARY smeared eps=0.6")
    results["bd_smeared_eps0.6"] = bd_primary

    # CROSS-CHECK: sharp BD (eps=1.0).  Higher cond(B) but exactly the documented
    # (1,-9,16,-8) operator; confirms the verdict is not a smearing artefact.
    bd_sharp = run_4d_bd("sharp", 1.0, Ns, n_seeds, BUDGET, t0, "CROSS-CHECK sharp BD")
    results["bd_sharp"] = bd_sharp

    verdict = build_verdict(bd_primary, link_baseline)
    verdict_sharp = build_verdict(bd_sharp, link_baseline)
    results["VERDICT"] = _to_native(verdict)
    results["VERDICT_sharp_crosscheck"] = _to_native(verdict_sharp)

    # consistency between the two BD operators
    results["bd_consistency"] = {
        "smeared_corner_concentration_replicates": verdict["corner_concentration_replicates"],
        "sharp_corner_concentration_replicates": verdict_sharp["corner_concentration_replicates"],
        "smeared_nl_vs_corner_slope": verdict["nl_vs_corner_slope"],
        "sharp_nl_vs_corner_slope": verdict_sharp["nl_vs_corner_slope"],
        "agree": bool(verdict["corner_concentration_replicates"] ==
                      verdict_sharp["corner_concentration_replicates"]),
    }

    print("\n=== VERDICT (BD smeared eps=0.6, PRIMARY) ===")
    for k in ["slab_more_local_than_diamond", "slab_diag_boost_linear",
              "slab_diag_boost_linear_R2_tail", "corner_more_nonlocal_than_bulk",
              "corner_vs_bulk_ratio", "nonlocality_rises_toward_corner",
              "nl_vs_corner_slope", "nl_vs_corner_R2", "n_signatures_supporting_H4g1",
              "corner_concentration_replicates", "corner_sign_flipped_vs_link",
              "H4g1_4D"]:
        print(f"  {k}: {verdict[k]}")
    print(f"\n  OVERALL: {verdict['overall']}")
    print(f"\n  sharp cross-check corner_concentration_replicates="
          f"{verdict_sharp['corner_concentration_replicates']} "
          f"(slope={verdict_sharp['nl_vs_corner_slope']:.3g}); "
          f"agree={results['bd_consistency']['agree']}")

    make_plots(bd_primary, bd_sharp, link_baseline, verdict)

    results["runtime_s"] = time.time() - t0
    with open(os.path.join(OUTDIR, "results.json"), "w") as fh:
        json.dump(_to_native(results), fh, indent=2)
    print(f"\nDone in {results['runtime_s']:.1f}s. results.json + plots in {OUTDIR}")
    return results


if __name__ == "__main__":
    run()
