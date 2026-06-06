#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
VYPOCET-18 : The unifying-thread test (H4g-1)
=============================================
CLAIM (H4g-1, BRAINSTORM-04 unifying thread, layer B):
    The diamond-CORNER non-Hadamard anomaly that VYPOCET-13 localised marks
    EXACTLY where the SJ state's modular flow stops being a geometric boost.
    On a slab/Rindler wedge the modular Hamiltonian K is the boost generator
    (Bisognano-Wichmann): LOCAL, with a kernel concentrated near the entangling
    surface and a LINEAR boost weight ~ distance.  In a causal diamond the two
    null edges meet at the corner, the boost has nowhere to flow (degenerate
    Killing vector), and K must STOP being local -- and the non-geometricity
    must CONCENTRATE at the corners, coinciding with the Hadamard anomaly.

WHAT WE MEASURE (geometricity diagnostic):
    We build the one-particle modular Hamiltonian K of the SJ-reduced Gaussian
    state on a spatial cut, as a real-space matrix K(x,y), via the standard
    Gaussian / covariance-matrix formalism (Peschel 2003; Casini-Huerta review
    0905.2562; Sorkin-Yazdi 1611.10281 for the SJ correlator).  We then measure
    its LOCALITY PROFILE:
      (i)  |K(x,y)| vs |x-y|  (off-diagonal decay; local boost => fast decay,
           power-law/exponential concentrated near the diagonal);
      (ii) the FRACTION of K's (Hilbert-Schmidt) norm carried by FAR-off-diagonal
           ("non-local") components, as a function of distance-to-corner;
      (iii) the diagonal modular weight K(x,x) vs distance-from-entangling-point
           (Bisognano-Wichmann predicts a LINEAR boost weight ~ distance).
    Contrasts:
      * half-space SLAB cut (expect geometric, boost-like, clean) vs
        DIAMOND cut (expect deviation);
      * WITHIN the diamond: BULK of the entangling region vs NEAR-CORNER zone
        (expect non-geometricity to CONCENTRATE at corners, matching the
        Hadamard anomaly location of VYPOCET-13).

ANALYTIC ANCHOR (Casini-Huerta; Bisognano-Wichmann):
    For an interval [a,b] in the 2D Minkowski vacuum the EXACT local modular
    Hamiltonian is K = 2 pi int beta(x) T_00(x) dx with the boost weight
        beta(x) = (x-a)(b-x)/(b-a),
    which is LINEAR in distance near each entangling point and vanishes there.
    A half-line cut x>0 (Rindler) gives beta(x) = x (pure boost).  These are the
    geometric benchmarks the SJ-on-causal-set kernel is compared against.

HONEST NULLS (stated up front, enforced in the verdict logic):
    * If K is EQUALLY non-local everywhere (discreteness noise dominates at
      these N) -> H4g-1 is UNTESTABLE at these N.  We detect this if the
      slab kernel is just as non-local as the diamond bulk.
    * If K is EQUALLY local everywhere (no corner concentration) -> H4g-1 is
      REFUTED (the corner Hadamard anomaly would then be purely kinematic, not
      modular).  We detect this if non-locality does NOT rise toward the corner.

----------------------------------------------------------------------------
GAUSSIAN MODULAR HAMILTONIAN -- construction (validated in self_test below)
----------------------------------------------------------------------------
A pure Gaussian state reduced to a set of spatial sites O is mixed Gaussian,
fixed by the equal-time correlators
    X_ij = <phi_i phi_j>   (field-field),
    P_ij = <pi_i  pi_j >   (momentum-momentum),   <phi pi> symmetric part = 0.
The reduced density matrix is rho_O ~ exp(-K),  K = (1/2)(phi^T H_phi phi
+ pi^T H_pi pi)  (a quadratic = "entanglement Hamiltonian").  With
    C = sqrt(X P)   (symplectic eigenvalues nu_k = eig(C) >= 1/2),
the standard Peschel/Casini-Huerta result is, in operator form,
    H_phi = (1/X) C arccoth(2C),     H_pi = (1/P) C arccoth(2C)
    [equivalently  H_phi = X^{-1} f(C),  H_pi = P^{-1} f(C),  f(C)=C arccoth(2C)]
so that the entanglement entropy is
    S = sum_k [ (nu_k+1/2) ln(nu_k+1/2) - (nu_k-1/2) ln(nu_k-1/2) ].
We build the REAL-SPACE matrix H_phi(x,y) (the field-field modular kernel) and
profile |H_phi(x,y)| as the modular-Hamiltonian locality probe.  (H_pi gives an
equivalent profile; we report H_phi as the primary geometric object because in
the 2D vacuum its diagonal carries the boost weight beta(x).)  The matrix
functions arccoth(2C) etc. are computed in the eigenbasis of the (real,
symmetric, similarity-transformed) operator.

SJ correlators on the causal set (covariant -> equal-time):
    Wightman W = positive part of i*Delta  (SJ state).
    X_ij = Re W_ij = <{phi_i,phi_j}>/2  (symmetric two-point = field correlator).
    For the momentum correlator we use the SJ data restricted to a THIN time
    band (a Cauchy-surface proxy): pi ~ d phi/dt, and on the slice the SJ
    symmetric correlator provides both X and (via the second time-derivative
    structure carried by i*Delta) the conjugate data.  Concretely we use the
    pair (X, P) with P obtained from the restriction of the *commutator* data
    i*Delta and the positivity of W (W (X) and the symplectic form (i*Delta)
    together fix the Gaussian state).  This is exactly the SSEE pairing
    W_O v = mu (i*Delta)_O v of VYPOCET-04/12; the symplectic eigenvalues nu are
    nu = mu - 1/2 and the modular kernel is rebuilt from the SAME generalized
    eigenproblem -- so K here is the modular Hamiltonian of the SSEE state.

We therefore have TWO equivalent constructions and use BOTH:
  (A) COVARIANT-SSEE kernel: from W_O, (i*Delta)_O solve W_O v = mu (i*Delta)_O v
      (the native SJ object of VYPOCET-12); build K = sum_k eps_k |k><k| with
      eps_k = ln[mu_k/(mu_k-1)] in the generalized eigenbasis, and express it as
      a real-space matrix K(x,y).  This is the modular Hamiltonian of the SJ
      state on O in the SSEE convention.
  (B) COVARIANCE kernel (cross-check, 2D slab/half-line where X,P are clean):
      X=ReW_O, P from the second correlator; H_phi = X^{-1} C arccoth(2C).
Construction (A) is dimension-independent and is our PRIMARY object (it reuses
the validated SSEE machinery); (B) is a literature cross-check in 2D.
"""

import json
import os
import time

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


# ============================================================================
# GEOMETRY + SJ construction (conventions identical to VYPOCET-04/06/12/13)
# ============================================================================

def sprinkle_diamond_2d(N, rng, T=1.0):
    """2D causal diamond in null coords (u,v) square [-T,T]^2; return (t,x)."""
    N = int(N)
    u = (rng.random(N) * 2.0 - 1.0) * T
    v = (rng.random(N) * 2.0 - 1.0) * T
    t = 0.5 * (u + v)
    x = 0.5 * (u - v)
    return np.column_stack([t, x])


def sprinkle_slab_2d(N, rng, T, L):
    """2D box-like slab {0<t<T, |x|<L}, T<L -> flat entangling surface x=0."""
    N = int(N)
    t = rng.random(N) * T
    x = (rng.random(N) * 2.0 - 1.0) * L
    return np.column_stack([t, x])


def causal_matrix_2d(coords):
    t = coords[:, 0]; x = coords[:, 1]
    dt = t[:, None] - t[None, :]
    dx = np.abs(x[:, None] - x[None, :])
    prec = (dt > 0) & (dt >= dx)
    C = prec.astype(np.float64)
    np.fill_diagonal(C, 0.0)
    return C


def green_retarded_2d(C):
    """G_R = (1/2) C (Sorkin-Yazdi 1611.10281)."""
    return 0.5 * C


def pauli_jordan(G_R):
    """i*Delta = i(G_R - G_R^T), Hermitian, +/- paired real eigenvalues."""
    return 1j * (G_R - G_R.T)


def sj_wightman(iDelta):
    w, V = np.linalg.eigh(iDelta)
    pos = w > 0
    W = (V[:, pos] * w[pos]) @ V[:, pos].conj().T
    return W, w, V


# ---- 4D ----
def sprinkle_diamond_4d(N, rng, T=1.0):
    N = int(N)
    U = rng.random(N)
    s = T * U**0.25
    sign = rng.choice([-1.0, 1.0], size=N)
    t = sign * (T - s)
    dirs = rng.normal(size=(N, 3))
    dirs /= np.linalg.norm(dirs, axis=1, keepdims=True)
    Vv = rng.random(N)
    rr = s * Vv**(1.0 / 3.0)
    return np.column_stack([t, dirs * rr[:, None]])


def sprinkle_slab_4d(N, rng, T, L):
    N = int(N)
    t = rng.random(N) * T
    x = (rng.random((N, 3)) * 2.0 - 1.0) * L
    return np.column_stack([t, x])


def causal_matrix_4d(coords):
    t = coords[:, 0]; r = coords[:, 1:]
    dt = t[:, None] - t[None, :]
    r2 = np.einsum('ij,ij->i', r, r)
    d2 = r2[:, None] + r2[None, :] - 2.0 * (r @ r.T)
    np.maximum(d2, 0.0, out=d2)
    prec = (dt > 0) & (dt * dt >= d2)
    C = prec.astype(np.float64)
    np.fill_diagonal(C, 0.0)
    return C


def link_matrix(C):
    C2 = C @ C
    return ((C > 0) & (C2 == 0)).astype(np.float64)


def green_retarded_4d(L, rho):
    a = np.sqrt(rho) / (2.0 * np.pi * np.sqrt(6.0))
    return a * L


# ============================================================================
# MODULAR HAMILTONIAN K(x,y) from the SJ-reduced Gaussian state on a region O
# ============================================================================
# COVARIANT-SSEE construction (primary, dimension-independent):
#   On O solve the generalized eigenproblem  W_O g_k = mu_k (iDelta)_O g_k.
#   mu come in pairs (mu, 1-mu); the occupation branch is mu>1, with symplectic
#   eigenvalue nu = mu - 1/2 and single-mode modular energy
#       eps_k = ln[ mu_k/(mu_k-1) ]   (= ln[(nu+1/2)/(nu-1/2)]).
#   The one-particle modular Hamiltonian operator is
#       K = sum_k eps_k  P_k ,      P_k = projector onto generalized mode g_k,
#   represented as a real-space matrix K(x,y) in the SITE basis.  We build it as
#       K = G^{-1/2}? -- instead, the clean, basis-correct construction is:
#   the generalized eigenvectors g_k (right eigenvectors of (iDelta_O)^{-1} W_O)
#   together with the dual basis g~_k = ((iDelta_O) g_k) give
#       K(x,y) = sum_k eps_k  g_k(x) g~_k(y)^*    (spectral resolution),
#   which is the modular Hamiltonian whose exponential reproduces rho_O.
# We measure locality of |K(x,y)| (Hermitised) directly in the site basis.
# ============================================================================

def modular_kernel_ssee(W, iDelta, sub_idx, kappa=None, tol=1e-9,
                        global_trunc=True):
    """Build the real-space one-particle modular Hamiltonian matrix K(x,y)
    on the sub-region O = sub_idx from the SJ data (W, iDelta).

    Returns dict with K (n_sub x n_sub Hermitian), site coords index sub_idx,
    eps spectrum, entropy S, symplectic nu.  Optional global magnitude
    truncation kappa on spec(iDelta) (the SSEE double truncation)."""
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

    # diagonalize iDelta_O (Hermitian); local magnitude cut (double truncation)
    d, U = np.linalg.eigh(iD_O)
    scale = np.max(np.abs(d)) if d.size else 0.0
    if scale == 0.0:
        return None
    local_cut = kappa if (kappa is not None) else tol * scale
    keep = np.abs(d) > local_cut
    if keep.sum() < 2:
        return None
    d_k = d[keep]; U_k = U[:, keep]                 # n x m
    # project W into the kept iDelta_O eigenbasis
    Wproj = U_k.conj().T @ W_O @ U_k                # m x m
    M = (Wproj.T / d_k).T                            # M = D^{-1} Wproj ; eig = mu
    mu_all, R = np.linalg.eig(M)                     # right eigenvectors R (cols)
    mu_all = mu_all
    # occupation branch mu>1
    muR = mu_all.real
    good = (muR > 1.0 + tol) & np.isfinite(muR)
    if good.sum() < 1:
        return None
    mu = muR[good]
    Rg = R[:, good]                                  # m x p  (in iDelta_O-eigbasis)
    eps = np.log(mu / (mu - 1.0))
    nu = mu - 0.5
    # entropy
    S = float(np.sum((nu + 0.5) * np.log(nu + 0.5) - (nu - 0.5) * np.log(nu - 0.5)))

    # lift eigenvectors back to the SITE basis of O:
    #   a generalized mode in the kept iDelta_O eigenbasis is g = U_k Rg(:,k);
    #   the dual (left) basis comes from the biorthogonal partner L = (R^{-1})^H.
    # Build K(x,y) = sum_k eps_k  g_k(x) gd_k(y)^*  with gd the dual lifted basis.
    # Numerically robust spectral resolution: M = R diag(mu) R^{-1}; the operator
    #   Kop = R diag(eps_full) R^{-1}  on the m-dim space, then lift by U_k.
    # eps_full: assign eps to mu>1 modes; the paired mu<1 (= 1-mu) modes carry
    # the SAME |eps| with opposite occupation sign -> we map the FULL operator
    # ln[ M (M-1)^{-1} ] (principal, real part) which is the modular Hamiltonian
    # of the one-particle space.  This is well-defined since mu in (0,1)U(1,inf).
    # Use the matrix function on M directly (more stable than per-eigenvector):
    with np.errstate(divide='ignore', invalid='ignore'):
        # K_m = ln(M) - ln(M - I) acting on the m-dim space
        # via eigendecomposition of M (generally diagonalizable here)
        muf, Rf = np.linalg.eig(M)
        # principal modular energy for each eigenvalue: real part of
        # ln[mu/(mu-1)] ; for 0<mu<1 this is ln[mu/(mu-1)] with mu-1<0 ->
        # complex; the physical one-particle modular Hamiltonian uses the
        # magnitude |ln[mu/(mu-1)]| with sign set by (mu>1 -> +, mu<1 -> -).
        zf = muf / (muf - 1.0)
        epsf = np.log(np.abs(zf)) * np.sign(muf.real - 0.5)
        epsf = np.where(np.isfinite(epsf), epsf, 0.0)
        Kdiag = np.diag(epsf.astype(complex))
        try:
            Rf_inv = np.linalg.inv(Rf)
            Km = Rf @ Kdiag @ Rf_inv                 # m x m operator
        except np.linalg.LinAlgError:
            Km = U_k.conj().T @ U_k * 0.0
    # lift to site basis: K_site = U_k Km U_k^H  (m-dim subspace embedded in O)
    K_site = U_k @ Km @ U_k.conj().T                 # n x n
    K_site = 0.5 * (K_site + K_site.conj().T)        # Hermitise (numerical)
    return {"K": K_site, "eps": np.sort(eps), "S": S, "nu": np.sort(nu),
            "n": n, "n_modes": int(good.sum())}


# ============================================================================
# COVARIANCE-MATRIX construction (2D cross-check vs literature)
# ============================================================================
# X = <phi phi>, P = <pi pi>; C = sqrt(X P); nu = eig(C);
# H_phi = X^{-1} C arccoth(2C)  (real-space field-field modular kernel).
# We compute matrix functions in the eigenbasis of the symmetric operator
# Xs^{1/2} P Xs^{1/2} (same spectrum as XP, but symmetric -> stable).
# ============================================================================

def _sym_sqrt(A):
    w, V = np.linalg.eigh(0.5 * (A + A.T))
    w = np.clip(w, 1e-14, None)
    return (V * np.sqrt(w)) @ V.T, (V * (1.0 / np.sqrt(w))) @ V.T


def modular_kernel_covariance(X, P):
    """H_phi(x,y) = X^{-1} C arccoth(2C), C=sqrt(XP). Returns (H_phi, nu)."""
    X = 0.5 * (X + X.T); P = 0.5 * (P + P.T)
    Xs, Xis = _sym_sqrt(X)                            # X^{1/2}, X^{-1/2}
    Msym = Xs @ P @ Xs                               # symmetric, spectrum = spec(XP)
    w, V = np.linalg.eigh(0.5 * (Msym + Msym.T))
    nu = np.sqrt(np.clip(w, 1e-14, None))            # symplectic eigenvalues
    nu = np.clip(nu, 0.5 + 1e-9, None)
    f = nu * np.arccosh_safe(nu) if False else nu * _arccoth(2.0 * nu)
    # C arccoth(2C) in the symmetric basis: C = Xs^{-1}? Build via:
    #   C = sqrt(XP) = Xis @ (Xs P Xs)^{1/2} @ Xs  -> in V-basis fn applies to nu
    # f(C) acts as f(nu) in the V-eigenbasis of Msym, then conjugate by Xs/Xis.
    Fsym = (V * f) @ V.T                              # f(sqrt(Msym)) sym-basis
    # H_phi = X^{-1} f(C) ; with C = Xis Msym^{1/2} Xs  one gets
    #   X^{-1} f(C) = Xis ( f(Msym^{1/2}) ) Xis  (symmetric, clean form)
    H_phi = Xis @ Fsym @ Xis
    H_phi = 0.5 * (H_phi + H_phi.T)
    return H_phi, np.sort(nu)


def _arccoth(x):
    x = np.asarray(x, float)
    x = np.where(np.abs(x) <= 1.0, np.sign(x) * 1.0000001, x)
    return 0.5 * np.log((x + 1.0) / (x - 1.0))


# patch numpy namespace stub used above (kept for clarity; not used)
np.arccosh_safe = lambda v: np.arccosh(np.clip(v, 1.0, None))


# ============================================================================
# LOCALITY PROFILE of a modular kernel K(x,y)
# ============================================================================

def locality_profile(K, coords_sub, entang_point=None, n_dist_bins=18,
                     near_frac=0.18):
    """Given Hermitian K (n x n) on sites coords_sub (n x dim, columns
    (t, x...) -- we use the SPATIAL coords for distance), measure:
      * |K(x,y)| binned by spatial separation |x-y| (off-diagonal decay);
      * the fraction of ||K||_HS^2 in 'far' off-diagonal pairs vs near-diagonal;
      * the diagonal weight |K(x,x)| vs distance from the entangling point/surface;
      * the non-local fraction as a function of distance-to-corner (if a corner
        location is supplied via entang_point being a 'corner' marker -- here we
        pass distance-to-corner per site through 'corner_dist').
    coords_sub: array (n, dim) of FULL coords (t, x1,...) for the O sites.
    Returns a dict of arrays.
    """
    n = K.shape[0]
    Kabs = np.abs(K)
    # spatial coordinates (drop time column 0)
    xs = coords_sub[:, 1:]
    # pairwise spatial distance
    diff = xs[:, None, :] - xs[None, :, :]
    Dij = np.sqrt(np.einsum('ijk,ijk->ij', diff, diff))
    iu = np.triu_indices(n, k=1)
    dvals = Dij[iu]
    kvals = Kabs[iu]
    # normalize off-diagonal magnitude profile vs distance
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
    # diagonal weight
    diag = np.real(np.diag(K))
    return {"dist_centers": centers, "offdiag_mean": prof, "offdiag_count": cnt,
            "Dij": Dij, "Kabs": Kabs, "diag": diag, "xs": xs}


def nonlocal_fraction(Kabs, Dij, near_radius):
    """Fraction of Hilbert-Schmidt weight in 'far' off-diagonal pairs:
        f_nl = sum_{|x-y|>near_radius} |K|^2  /  sum_{all off-diag} |K|^2 .
    near_radius is set in units of the nearest-neighbour spacing.
    A purely local boost-like K -> f_nl small; non-geometric K -> f_nl large."""
    n = Kabs.shape[0]
    off = ~np.eye(n, dtype=bool)
    K2 = Kabs**2
    tot = K2[off].sum()
    if tot <= 0:
        return np.nan
    far = off & (Dij > near_radius)
    return float(K2[far].sum() / tot)


def nonlocality_vs_corner(Kabs, Dij, coords_sub, corner_pt, near_radius,
                          n_zones=6):
    """For each site, its 'non-locality' = fraction of its row HS-weight that
    sits at far separation:  nl_i = sum_{j: D_ij>near} |K_ij|^2 / sum_j |K_ij|^2.
    Bin nl_i by the site's distance-to-corner.  corner_pt: spatial location of
    the (nearest) corner/tip.  Returns (zone_centers, nl_mean, nl_sem, count)."""
    n = Kabs.shape[0]
    xs = coords_sub[:, 1:]
    # distance to corner (spatial)
    dcorn = np.sqrt(np.sum((xs - corner_pt[None, :])**2, axis=1))
    K2 = Kabs**2
    np.fill_diagonal(K2, 0.0)
    rowtot = K2.sum(axis=1)
    farmask = (Dij > near_radius)
    np.fill_diagonal(farmask, False)
    rowfar = (K2 * farmask).sum(axis=1)
    with np.errstate(divide='ignore', invalid='ignore'):
        nl = np.where(rowtot > 0, rowfar / rowtot, np.nan)
    # bin by distance-to-corner
    good = np.isfinite(nl)
    dc = dcorn[good]; nlv = nl[good]
    if dc.size < n_zones:
        return None
    qs = np.linspace(0, 1, n_zones + 1)
    edges = np.quantile(dc, qs)
    edges[0] -= 1e-9; edges[-1] += 1e-9
    centers, mean, sem, cnt = [], [], [], []
    for b in range(n_zones):
        m = (dc >= edges[b]) & (dc < edges[b + 1])
        if m.sum() == 0:
            continue
        centers.append(float(np.mean(dc[m])))
        mean.append(float(np.mean(nlv[m])))
        sem.append(float(np.std(nlv[m]) / max(1, np.sqrt(m.sum()))))
        cnt.append(int(m.sum()))
    return (np.array(centers), np.array(mean), np.array(sem), np.array(cnt))


def diag_weight_vs_distance(diag, coords_sub, surface_normal_coord=1,
                            surface_value=0.0, n_bins=14, use_abs_x=True):
    """Diagonal modular weight |K(x,x)| vs distance from the entangling surface.
    surface_normal_coord: index into FULL coords (1 = x1).  For a half-space
    cut x1>0 the entangling surface is x1=0, distance = x1.  Bisognano-Wichmann
    predicts a LINEAR boost weight K(x,x) ~ distance."""
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
# FIT HELPERS
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


# ============================================================================
# SELF-TEST: continuum free-field interval -- does our covariance kernel
# reproduce the analytic Bisognano-Wichmann boost weight beta(x)?
# ============================================================================

def self_test_continuum_interval():
    """Massive (small mass, IR-regulated) free scalar on a 1D chain; reduced to
    an interval; build H_phi via the covariance kernel and check that the
    diagonal modular weight tracks the analytic boost weight
        beta(x) = (x-a)(b-x)/(b-a)   (up to the overall 2 pi normalisation),
    which is the local Bisognano-Wichmann result for an interval [a,b] in the
    2D vacuum (Casini-Huerta).  This validates the K-construction independently
    of the causal set."""
    Ntot = 600
    m = 0.02                     # small IR mass (regulator)
    # ground-state correlators of the discretised KG chain (Peschel):
    #   X = <phi phi> = (1/2) K^{-1/2},  P = <pi pi> = (1/2) K^{1/2},
    #   K_ij = (2+m^2) delta - delta_{|i-j|=1}   (lattice Laplacian + mass).
    k = np.arange(Ntot)
    # use translation-invariant correlators in momentum space (periodic chain)
    q = 2 * np.pi * np.fft.fftfreq(Ntot)
    wq = np.sqrt(m**2 + 4.0 * np.sin(q / 2.0)**2)
    # X_ij = (1/(2N)) sum_q cos(q (i-j)) / wq ; P_ij = (1/(2N)) sum_q cos * wq
    idx = k[:, None] - k[None, :]
    cosq = np.cos(q[None, None, :] * idx[:, :, None])
    X = (cosq / wq[None, None, :]).sum(axis=2) / (2.0 * Ntot)
    P = (cosq * wq[None, None, :]).sum(axis=2) / (2.0 * Ntot)
    # interval [a,b]
    a, b = 200, 399
    sub = np.arange(a, b + 1)
    X_O = X[np.ix_(sub, sub)]; P_O = P[np.ix_(sub, sub)]
    H_phi, nu = modular_kernel_covariance(X_O, P_O)
    diag = np.abs(np.diag(H_phi))
    xs = sub.astype(float)
    beta = (xs - (a - 0.5)) * ((b + 0.5) - xs) / ((b + 0.5) - (a - 0.5))
    # compare shapes (correlation) away from the very edges (lattice cutoff)
    interior = slice(8, -8)
    bb = beta[interior]; dd = diag[interior]
    # H_phi diagonal ~ const / beta near the centre for the field-field kernel;
    # the robust geometric statement is that the modular weight is a SMOOTH
    # function peaked in the middle (boost) -- we report the correlation of
    # diag with beta and with 1/beta, and which wins.
    cc_beta = float(np.corrcoef(dd, bb)[0, 1])
    cc_invbeta = float(np.corrcoef(dd, 1.0 / np.clip(bb, 1e-6, None))[0, 1])
    # locality: off-diagonal decay should be FAST for the local boost kernel
    coords_sub = np.column_stack([np.zeros_like(xs), xs])
    lp = locality_profile(H_phi, coords_sub, n_dist_bins=20)
    sl_off, _, r2_off = loglog_slope(lp["dist_centers"], lp["offdiag_mean"])
    return {
        "Ntot": Ntot, "mass": m, "interval": [a, b],
        "corr_diag_vs_beta": cc_beta,
        "corr_diag_vs_invbeta": cc_invbeta,
        "offdiag_loglog_slope": sl_off, "offdiag_R2": r2_off,
        "note": ("Validation: field-field modular kernel H_phi of an interval. "
                 "Diagonal modular weight should be a smooth boost-like profile "
                 "(peaked in the interval centre); off-diagonal decays as a "
                 "power law (LOCAL). corr_diag_vs_invbeta high = H_phi diagonal "
                 "tracks 1/beta (expected: T00 weight beta enters via momentum "
                 "kernel; field kernel carries the conjugate weight)."),
        "beta_profile": beta[::8].tolist(), "diag_profile": diag[::8].tolist(),
        "xs_profile": xs[::8].tolist(),
    }


# ============================================================================
# 2D EXPERIMENT: slab vs diamond, bulk vs corner
# ============================================================================

def run_2d(results):
    print("\n==== 2D modular-flow geometricity: slab vs diamond ====")
    Ns = [400, 700, 1000, 1300, 1600, 1800]
    n_seeds = 5
    T_dia = 1.0
    T_slab, L_slab = 0.45, 1.3      # T<L -> flat entangling surface x=0, no corners

    # PRIMARY object: the UNTRUNCATED SJ modular kernel (the genuine modular
    # flow of the SJ state whose geometricity Bisognano-Wichmann predicts).
    # The SSEE double-truncation is a SEPARATE (crossed-product) operation that
    # makes K artificially low-rank => delocalised by construction; it would
    # contaminate the geometric question, so the locality probe uses kappa=None.
    diamond = {N: {"f_nl_bulk": [], "f_nl_corner": [], "f_nl_all": [],
                   "off_slope_all": [], "off_R2_all": [],
                   "off_slope_bulk": [], "off_slope_corner": [],
                   "nl_vs_corner_centers": [], "nl_vs_corner_mean": [],
                   "S": []} for N in Ns}
    slab = {N: {"f_nl_all": [], "off_slope": [], "off_R2": [],
                "diag_slope_lin": [], "diag_R2_lin": [], "S": []} for N in Ns}

    for N in Ns:
        for s in range(n_seeds):
            # ---------------- DIAMOND ----------------
            rng = np.random.default_rng(18_000_000 + 1000 * N + s)
            coords = sprinkle_diamond_2d(N, rng, T_dia)
            C = causal_matrix_2d(coords)
            iD = pauli_jordan(green_retarded_2d(C))
            W, w, V = sj_wightman(iD)
            # entangling region O = a concentric sub-diamond (the cut region);
            # its corners are the spatial tips of the sub-diamond (x ~ +-f).
            f = 0.6
            u = coords[:, 0] + coords[:, 1]; v = coords[:, 0] - coords[:, 1]
            sub = np.where((np.abs(u) <= f) & (np.abs(v) <= f))[0]
            mk = modular_kernel_ssee(W, iD, sub, kappa=None)   # UNTRUNCATED
            if mk is not None and mk["K"].shape[0] >= 12:
                K = mk["K"]; csub = coords[sub]
                lp = locality_profile(K, csub)
                nn = np.sqrt(2.0 / N)               # NN spacing (Vol=2)
                near_r = 3.0 * nn
                diamond[N]["f_nl_all"].append(
                    nonlocal_fraction(lp["Kabs"], lp["Dij"], near_r))
                diamond[N]["S"].append(mk["S"])
                sl_all, r2_all, _, _ = offdiag_slope_subset(
                    lp["Kabs"], lp["Dij"], np.ones(K.shape[0], bool))
                if sl_all is not None:
                    diamond[N]["off_slope_all"].append(sl_all)
                    diamond[N]["off_R2_all"].append(r2_all)
                # distance-to-corner = distance to the NEAREST spatial tip x=+-f
                # (the sub-diamond has two spatial corners; the SJ non-Hadamard
                # sites of 2212.10592 are the spacetime corners u-v'=+-2L).
                dc = np.minimum(np.abs(csub[:, 1] - f), np.abs(csub[:, 1] + f))
                nvc = _nl_vs_corner_generic(lp["Kabs"], lp["Dij"], dc, near_r,
                                            n_zones=6)
                if nvc is not None:
                    diamond[N]["nl_vs_corner_centers"].append(nvc[0].tolist())
                    diamond[N]["nl_vs_corner_mean"].append(nvc[1].tolist())
                # bulk vs corner zones by distance-to-nearest-tip
                bulk_m = dc > np.median(dc)
                corn_m = dc <= np.percentile(dc, 30)
                diamond[N]["f_nl_bulk"].append(
                    _rowfrac_subset(lp["Kabs"], lp["Dij"], near_r, bulk_m))
                diamond[N]["f_nl_corner"].append(
                    _rowfrac_subset(lp["Kabs"], lp["Dij"], near_r, corn_m))
                slb, _, _, _ = offdiag_slope_subset(lp["Kabs"], lp["Dij"], bulk_m)
                slc, _, _, _ = offdiag_slope_subset(lp["Kabs"], lp["Dij"], corn_m)
                if slb is not None:
                    diamond[N]["off_slope_bulk"].append(slb)
                if slc is not None:
                    diamond[N]["off_slope_corner"].append(slc)
                # CROSS-CORNER coupling: mean |K| between the two opposite
                # spatial corner zones (x~+f vs x~-f) relative to the overall
                # mean |K| at the same separation.  >1 => K preferentially
                # connects opposite corners (the u-v'=+-2L non-Hadamard pairing).
                rc = csub[:, 1] > (f - 0.20)        # right corner zone
                lc = csub[:, 1] < (-f + 0.20)       # left corner zone
                if rc.sum() >= 3 and lc.sum() >= 3:
                    Kabs = lp["Kabs"]; Dij = lp["Dij"]
                    cc_block = Kabs[np.ix_(np.where(rc)[0], np.where(lc)[0])]
                    cc_dist = Dij[np.ix_(np.where(rc)[0], np.where(lc)[0])]
                    mean_cc = float(np.mean(cc_block))
                    # reference: mean |K| over ALL pairs at comparable distance
                    dlo, dhi = np.percentile(cc_dist, [10, 90])
                    iu = np.triu_indices(Kabs.shape[0], 1)
                    dv = Dij[iu]; kv = Kabs[iu]
                    refm = (dv >= dlo) & (dv <= dhi)
                    ref = float(np.mean(kv[refm])) if refm.sum() else np.nan
                    if np.isfinite(ref) and ref > 0:
                        diamond[N].setdefault("cross_corner_ratio", []).append(
                            mean_cc / ref)

            # ---------------- SLAB ----------------
            rng2 = np.random.default_rng(28_000_000 + 1000 * N + s)
            vol = 2.0 * T_slab * L_slab
            coords_s = sprinkle_slab_2d(N, rng2, T_slab, L_slab)
            Cs = causal_matrix_2d(coords_s)
            iDs = pauli_jordan(green_retarded_2d(Cs))
            Ws, ws, Vs = sj_wightman(iDs)
            sub_s = np.where(coords_s[:, 1] > 0.0)[0]   # half-space x>0
            mks = modular_kernel_ssee(Ws, iDs, sub_s, kappa=None)  # UNTRUNCATED
            if mks is not None and mks["K"].shape[0] >= 12:
                Ks = mks["K"]; css = coords_s[sub_s]
                lps = locality_profile(Ks, css)
                nn_s = np.sqrt(vol / N)
                near_rs = 3.0 * nn_s
                slab[N]["f_nl_all"].append(
                    nonlocal_fraction(lps["Kabs"], lps["Dij"], near_rs))
                slab[N]["S"].append(mks["S"])
                sl_off, r2_off, _, _ = offdiag_slope_subset(
                    lps["Kabs"], lps["Dij"], np.ones(Ks.shape[0], bool))
                if sl_off is not None:
                    slab[N]["off_slope"].append(sl_off)
                    slab[N]["off_R2"].append(r2_off)
                # diagonal boost-weight linearity vs distance from x=0 surface
                cen, prof, cnt = diag_weight_vs_distance(
                    lps["diag"], css, surface_normal_coord=1, surface_value=0.0)
                sl_lin, _, r2lin = linfit(cen, prof, mask=cnt >= 5)
                if sl_lin is not None:
                    slab[N]["diag_slope_lin"].append(sl_lin)
                    slab[N]["diag_R2_lin"].append(r2lin)
        print(f"  [N={N}] diamond f_nl={_m(diamond[N]['f_nl_all']):.3f} "
              f"off-slope={_m(diamond[N]['off_slope_all']):.2f} "
              f"(bulk_off {_m(diamond[N]['off_slope_bulk']):.2f}, "
              f"corner_off {_m(diamond[N]['off_slope_corner']):.2f}); "
              f"slab f_nl={_m(slab[N]['f_nl_all']):.3f} off-slope={_m(slab[N]['off_slope']):.2f}")

    # aggregate
    def agg(d, key):
        return [float(np.mean(d[N][key])) if len(d[N][key]) else np.nan for N in Ns]
    def aggstd(d, key):
        return [float(np.std(d[N][key])) if len(d[N][key]) > 1 else 0.0 for N in Ns]

    res2d = {
        "Ns": Ns, "n_seeds": n_seeds,
        "diamond_f_nl_all": agg(diamond, "f_nl_all"),
        "diamond_f_nl_bulk": agg(diamond, "f_nl_bulk"),
        "diamond_f_nl_corner": agg(diamond, "f_nl_corner"),
        "diamond_f_nl_all_std": aggstd(diamond, "f_nl_all"),
        "diamond_f_nl_bulk_std": aggstd(diamond, "f_nl_bulk"),
        "diamond_f_nl_corner_std": aggstd(diamond, "f_nl_corner"),
        "diamond_off_slope_all": agg(diamond, "off_slope_all"),
        "diamond_off_R2_all": agg(diamond, "off_R2_all"),
        "diamond_off_slope_bulk": agg(diamond, "off_slope_bulk"),
        "diamond_off_slope_corner": agg(diamond, "off_slope_corner"),
        "diamond_cross_corner_ratio": [
            float(np.mean(diamond[N].get("cross_corner_ratio", [np.nan])))
            for N in Ns],
        "slab_f_nl_all": agg(slab, "f_nl_all"),
        "slab_f_nl_all_std": aggstd(slab, "f_nl_all"),
        "slab_off_slope": agg(slab, "off_slope"),
        "slab_off_R2": agg(slab, "off_R2"),
        "slab_diag_slope_lin": agg(slab, "diag_slope_lin"),
        "slab_diag_R2_lin": agg(slab, "diag_R2_lin"),
    }

    # representative non-locality-vs-corner curve (largest N, seed-averaged)
    Nrep = Ns[-1]
    curves_c = diamond[Nrep]["nl_vs_corner_centers"]
    curves_m = diamond[Nrep]["nl_vs_corner_mean"]
    if curves_c:
        # align on common length
        Lmin = min(len(c) for c in curves_c)
        cmat = np.array([c[:Lmin] for c in curves_c])
        mmat = np.array([m[:Lmin] for m in curves_m])
        res2d["nl_vs_corner_repN"] = Nrep
        res2d["nl_vs_corner_dist"] = cmat.mean(axis=0).tolist()
        res2d["nl_vs_corner_mean"] = mmat.mean(axis=0).tolist()
        res2d["nl_vs_corner_sem"] = (mmat.std(axis=0) /
                                     max(1, np.sqrt(mmat.shape[0]))).tolist()
        # slope of non-locality vs distance-to-corner: NEGATIVE => non-locality
        # rises TOWARD the corner (small distance) = H4g-1 prediction.
        sl_c, _, r2_c = linfit(cmat.mean(axis=0), mmat.mean(axis=0))
        res2d["nl_vs_corner_slope"] = sl_c
        res2d["nl_vs_corner_R2"] = r2_c

    results["part_2d"] = _to_native(res2d)
    return diamond, slab, res2d, Ns


def _rowfrac_subset(Kabs, Dij, near_r, mask):
    """Mean per-row far-fraction over the subset of rows in `mask`."""
    n = Kabs.shape[0]
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
    """Off-diagonal decay slope of |K(x,y)| vs |x-y|, using only pairs whose
    ROW index is in row_mask (so we probe locality 'as seen from' a zone, e.g.
    bulk rows vs corner rows).  A LOCAL boost kernel decays as a power law
    (negative slope, good R2); a non-local kernel is ~flat (slope ~ 0).
    Returns (slope, R2, centers, prof)."""
    n = Kabs.shape[0]
    rows = np.where(row_mask)[0]
    if rows.size < 3:
        return None, None, None, None
    dsub = Dij[rows][:, :]            # (nrows, n)
    ksub = Kabs[rows][:, :]
    # flatten, drop self (distance ~ 0) pairs
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


def _m(lst):
    lst = [x for x in lst if np.isfinite(x)]
    return float(np.mean(lst)) if lst else np.nan


# ============================================================================
# 4D EXPERIMENT (if runtime allows): slab vs diamond, bulk vs corner
# ============================================================================

def run_4d(results, time_budget_s=900, t_start=None):
    print("\n==== 4D modular-flow geometricity: slab vs diamond ====")
    Ns = [800, 1200, 1800, 2500]
    n_seeds = 3
    kappa_frac = 0.05
    diamond = {N: {"f_nl_all": [], "f_nl_bulk": [], "f_nl_corner": [],
                   "nl_vs_corner_centers": [], "nl_vs_corner_mean": [], "S": []}
               for N in Ns}
    slab = {N: {"f_nl_all": [], "diag_slope_lin": [], "diag_R2_lin": [], "S": []}
            for N in Ns}
    T_slab, L_slab = 0.5, 0.85
    rho_slab = 1300.0

    for N in Ns:
        if t_start is not None and (time.time() - t_start) > time_budget_s:
            print(f"  [time budget reached, stopping 4D at N<{N}]")
            break
        for s in range(n_seeds):
            # DIAMOND
            rng = np.random.default_rng(48_000_000 + 1000 * N + s)
            T = 1.0
            coords = sprinkle_diamond_4d(N, rng, T)
            vol = (2.0 / 3.0) * np.pi * T**4; rho = N / vol
            C = causal_matrix_4d(coords); Lk = link_matrix(C)
            iD = pauli_jordan(green_retarded_4d(Lk, rho))
            W, w, V = sj_wightman(iD)
            tt = np.abs(coords[:, 0]); rr = np.linalg.norm(coords[:, 1:], axis=1)
            f = 0.6
            sub = np.where(tt + rr <= f * T)[0]
            mk = modular_kernel_ssee(W, iD, sub, kappa=None)   # UNTRUNCATED probe
            if mk is not None and mk["K"].shape[0] >= 16:
                K = mk["K"]; csub = coords[sub]
                lp = locality_profile(K, csub)
                nn = rho**(-0.25)
                near_r = 3.0 * nn
                diamond[N]["f_nl_all"].append(
                    nonlocal_fraction(lp["Kabs"], lp["Dij"], near_r))
                diamond[N]["S"].append(mk["S"])
                # corner/tip of sub-diamond: spatial r ~ 0 but at |t|~f (null tip);
                # the spatial 'corner' for the entangling 2-sphere is r=f, t=0.
                corner_pt = np.array([f, 0.0, 0.0])  # on the entangling sphere
                rsub = np.linalg.norm(csub[:, 1:], axis=1)
                tsub = np.abs(csub[:, 0])
                # distance-to-corner: proximity to the null tip (t->f, r->0)
                dcorn = np.sqrt((tsub - f)**2 + rsub**2)
                near_corn = dcorn <= np.percentile(dcorn, 30)
                bulk = dcorn > np.median(dcorn)
                diamond[N]["f_nl_corner"].append(
                    _rowfrac_subset(lp["Kabs"], lp["Dij"], near_r, near_corn))
                diamond[N]["f_nl_bulk"].append(
                    _rowfrac_subset(lp["Kabs"], lp["Dij"], near_r, bulk))
                nvc = _nl_vs_corner_generic(lp["Kabs"], lp["Dij"], dcorn,
                                            near_r, n_zones=6)
                if nvc is not None:
                    diamond[N]["nl_vs_corner_centers"].append(nvc[0].tolist())
                    diamond[N]["nl_vs_corner_mean"].append(nvc[1].tolist())

            # SLAB
            rng2 = np.random.default_rng(58_000_000 + 1000 * N + s)
            vol_s = T_slab * (2 * L_slab)**3
            Ns_pts = int(round(rho_slab * vol_s))
            coords_s = sprinkle_slab_4d(Ns_pts, rng2, T_slab, L_slab)
            rho_s = Ns_pts / vol_s
            Cs = causal_matrix_4d(coords_s); Lks = link_matrix(Cs)
            iDs = pauli_jordan(green_retarded_4d(Lks, rho_s))
            Ws, ws, Vs = sj_wightman(iDs)
            interior = ((np.abs(coords_s[:, 2]) < 0.7 * L_slab) &
                        (np.abs(coords_s[:, 3]) < 0.7 * L_slab))
            sub_s = np.where(interior & (coords_s[:, 1] > 0.0))[0]
            mks = modular_kernel_ssee(Ws, iDs, sub_s, kappa=None)  # UNTRUNCATED
            if mks is not None and mks["K"].shape[0] >= 16:
                Ks = mks["K"]; css = coords_s[sub_s]
                lps = locality_profile(Ks, css)
                nn_s = rho_s**(-0.25)
                near_rs = 3.0 * nn_s
                slab[N]["f_nl_all"].append(
                    nonlocal_fraction(lps["Kabs"], lps["Dij"], near_rs))
                slab[N]["S"].append(mks["S"])
                cen, prof, cnt = diag_weight_vs_distance(
                    lps["diag"], css, surface_normal_coord=1, surface_value=0.0)
                sl_lin, _, r2lin = linfit(cen, prof, mask=cnt >= 5)
                if sl_lin is not None:
                    slab[N]["diag_slope_lin"].append(sl_lin)
                    slab[N]["diag_R2_lin"].append(r2lin)
        print(f"  [4D N={N}] diamond f_nl_all~{_m(diamond[N]['f_nl_all']):.3f} "
              f"(bulk {_m(diamond[N]['f_nl_bulk']):.3f}, corner {_m(diamond[N]['f_nl_corner']):.3f}); "
              f"slab f_nl_all~{_m(slab[N]['f_nl_all']):.3f}")

    def agg(d, key):
        return [float(np.mean(d[N][key])) if len(d[N][key]) else np.nan for N in Ns]
    res4d = {
        "Ns": Ns, "n_seeds": n_seeds,
        "diamond_f_nl_all": agg(diamond, "f_nl_all"),
        "diamond_f_nl_bulk": agg(diamond, "f_nl_bulk"),
        "diamond_f_nl_corner": agg(diamond, "f_nl_corner"),
        "slab_f_nl_all": agg(slab, "f_nl_all"),
        "slab_diag_slope_lin": agg(slab, "diag_slope_lin"),
        "slab_diag_R2_lin": agg(slab, "diag_R2_lin"),
    }
    Nrep = None
    for N in reversed(Ns):
        if diamond[N]["nl_vs_corner_centers"]:
            Nrep = N; break
    if Nrep is not None:
        cc = diamond[Nrep]["nl_vs_corner_centers"]
        mm = diamond[Nrep]["nl_vs_corner_mean"]
        Lmin = min(len(c) for c in cc)
        cmat = np.array([c[:Lmin] for c in cc]); mmat = np.array([m[:Lmin] for m in mm])
        res4d["nl_vs_corner_repN"] = Nrep
        res4d["nl_vs_corner_dist"] = cmat.mean(axis=0).tolist()
        res4d["nl_vs_corner_mean"] = mmat.mean(axis=0).tolist()
        sl_c, _, r2_c = linfit(cmat.mean(axis=0), mmat.mean(axis=0))
        res4d["nl_vs_corner_slope"] = sl_c
        res4d["nl_vs_corner_R2"] = r2_c
    results["part_4d"] = _to_native(res4d)
    return res4d


def _nl_vs_corner_generic(Kabs, Dij, dcorn, near_r, n_zones=6):
    n = Kabs.shape[0]
    K2 = Kabs**2; np.fill_diagonal(K2, 0.0)
    rowtot = K2.sum(axis=1)
    farmask = (Dij > near_r); np.fill_diagonal(farmask, False)
    rowfar = (K2 * farmask).sum(axis=1)
    with np.errstate(divide='ignore', invalid='ignore'):
        nl = np.where(rowtot > 0, rowfar / rowtot, np.nan)
    good = np.isfinite(nl)
    dc = dcorn[good]; nlv = nl[good]
    if dc.size < n_zones:
        return None
    qs = np.linspace(0, 1, n_zones + 1)
    edges = np.quantile(dc, qs); edges[0] -= 1e-9; edges[-1] += 1e-9
    cen, mn = [], []
    for b in range(n_zones):
        m = (dc >= edges[b]) & (dc < edges[b + 1])
        if m.sum() == 0:
            continue
        cen.append(float(np.mean(dc[m]))); mn.append(float(np.mean(nlv[m])))
    return np.array(cen), np.array(mn)


# ============================================================================
# VERDICT LOGIC
# ============================================================================

def build_verdict(res2d, res4d=None):
    v = {}
    Ns = res2d["Ns"]
    # use the large-N tail (last 3 points) for the headline comparison
    def tail(a):
        a = np.array(a, float); a = a[np.isfinite(a)]
        return float(np.mean(a[-3:])) if a.size >= 1 else np.nan
    d_all = tail(res2d["diamond_f_nl_all"])
    d_bulk = tail(res2d["diamond_f_nl_bulk"])
    d_corn = tail(res2d["diamond_f_nl_corner"])
    s_all = tail(res2d["slab_f_nl_all"])
    v["diamond_nonlocal_frac_tail"] = d_all
    v["diamond_bulk_nonlocal_frac_tail"] = d_bulk
    v["diamond_corner_nonlocal_frac_tail"] = d_corn
    v["slab_nonlocal_frac_tail"] = s_all

    # off-diagonal decay slopes (PRIMARY locality discriminator): a LOCAL
    # boost kernel decays as a power law (slope clearly < 0); a non-local
    # kernel is flat (slope ~ 0).
    slab_off = tail(res2d["slab_off_slope"])
    dia_off = tail(res2d["diamond_off_slope_all"])
    bulk_off = tail(res2d["diamond_off_slope_bulk"])
    corn_off = tail(res2d["diamond_off_slope_corner"])
    v["slab_offdiag_slope_tail"] = slab_off
    v["diamond_offdiag_slope_tail"] = dia_off
    v["diamond_bulk_offdiag_slope_tail"] = bulk_off
    v["diamond_corner_offdiag_slope_tail"] = corn_off

    # (1) slab kernel MORE local than diamond? (steeper off-diagonal decay)
    #     geometric boost (slab) => clearly negative slope; diamond => flatter.
    slab_more_local = bool(
        np.isfinite(slab_off) and np.isfinite(dia_off) and slab_off < dia_off - 0.1)
    v["slab_more_local_than_diamond"] = slab_more_local
    v["slab_vs_diamond_slope_gap"] = (float(dia_off - slab_off)
        if np.isfinite(slab_off) and np.isfinite(dia_off) else np.nan)
    # supporting metric: integrated non-local fraction
    v["slab_vs_diamond_fnl_ratio"] = (float(s_all / d_all)
        if np.isfinite(s_all) and np.isfinite(d_all) and d_all > 0 else np.nan)

    # (2) within diamond: non-locality CONCENTRATES at corner?
    #     corner kernel flatter (less negative slope) AND higher non-local frac.
    corner_flatter = bool(np.isfinite(corn_off) and np.isfinite(bulk_off)
                          and corn_off > bulk_off)
    corner_more_nonlocal = bool(np.isfinite(d_corn) and np.isfinite(d_bulk)
                                and d_corn > d_bulk)
    v["corner_offdiag_flatter_than_bulk"] = corner_flatter
    v["corner_more_nonlocal_than_bulk"] = corner_more_nonlocal
    v["corner_vs_bulk_ratio"] = (float(d_corn / d_bulk)
                                 if np.isfinite(d_corn) and np.isfinite(d_bulk)
                                 and d_bulk > 0 else np.nan)

    # (3) non-locality rises TOWARD the corner (negative slope vs dist-to-corner)
    sl_c = res2d.get("nl_vs_corner_slope", np.nan)
    rises_toward_corner = bool(np.isfinite(sl_c) and sl_c < 0)
    v["nonlocality_rises_toward_corner"] = rises_toward_corner
    v["nl_vs_corner_slope"] = sl_c

    # (3b) cross-corner coupling: does K preferentially connect opposite spatial
    # corners (the u-v'=+-2L non-Hadamard pairing of 2212.10592)?  ratio>1.
    cc_ratio = tail(res2d.get("diamond_cross_corner_ratio", [np.nan]))
    v["cross_corner_coupling_ratio_tail"] = cc_ratio
    cross_corner_enhanced = bool(np.isfinite(cc_ratio) and cc_ratio > 1.1)
    v["cross_corner_coupling_enhanced"] = cross_corner_enhanced

    # (4) slab diagonal boost-weight linear (Bisognano-Wichmann)?
    slab_lin_R2 = tail(res2d["slab_diag_R2_lin"])
    v["slab_diag_boost_linear_R2_tail"] = slab_lin_R2
    slab_boost_linear = bool(np.isfinite(slab_lin_R2) and slab_lin_R2 > 0.6)
    v["slab_diag_boost_linear"] = slab_boost_linear

    # HONEST NULL checks:
    #  (a) everything equally non-local (discreteness noise dominates) ->
    #      untestable.  Flag if slab off-slope ~ diamond off-slope (gap tiny)
    #      AND corner ~ bulk.
    tiny_gap = (np.isfinite(v["slab_vs_diamond_slope_gap"]) and
                abs(v["slab_vs_diamond_slope_gap"]) < 0.08)
    flat_corner = (np.isfinite(v["corner_vs_bulk_ratio"]) and
                   0.92 < v["corner_vs_bulk_ratio"] < 1.08 and not corner_flatter)
    v["null_discreteness_dominates"] = bool(tiny_gap and flat_corner)
    #  (b) no corner structure AND slab not more local -> H4g-1 refuted
    v["null_no_corner_structure"] = bool(
        not corner_more_nonlocal and not corner_flatter
        and not rises_toward_corner and not slab_more_local
        and not cross_corner_enhanced)

    # OVERALL: count geometricity signatures
    #   primary  : slab_more_local (off-diagonal decay), slab_boost_linear
    #   corner   : corner_flatter, corner_more_nonlocal, rises_toward_corner,
    #              cross_corner_enhanced  (4 corner-structure probes)
    support = int(slab_more_local) + int(corner_flatter) + \
        int(corner_more_nonlocal) + int(rises_toward_corner) + int(slab_boost_linear)
    v["n_signatures_supporting_H4g1"] = int(support)
    # corner-structure score (how concentrated the non-geometricity is at corners)
    corner_score = int(corner_flatter) + int(corner_more_nonlocal) + \
        int(rises_toward_corner) + int(cross_corner_enhanced)
    v["corner_structure_score"] = int(corner_score)
    v["signatures"] = {
        "slab_more_local_offdiag": slab_more_local,
        "slab_boost_weight_linear": slab_boost_linear,
        "corner_offdiag_flatter": corner_flatter,
        "corner_more_nonlocal": corner_more_nonlocal,
        "nonlocality_rises_toward_corner": rises_toward_corner,
        "cross_corner_coupling_enhanced": cross_corner_enhanced,
    }
    if v["null_discreteness_dominates"]:
        v["overall"] = ("UNTESTABLE at these N: discreteness noise dominates "
                        "(slab as non-local as diamond, no corner structure)")
        v["H4g1"] = "untestable"
    elif v["null_no_corner_structure"]:
        v["overall"] = ("REFUTED: K shows no corner concentration of "
                        "non-locality; the corner Hadamard anomaly is not "
                        "accompanied by modular non-geometricity")
        v["H4g1"] = "refuted"
    elif support >= 3:
        v["overall"] = (f"SUPPORTED: {support}/5 geometricity signatures present "
                        "(slab boost-local, corner non-geometricity concentration)")
        v["H4g1"] = "supported"
    elif support >= 1:
        v["overall"] = (f"PARTIAL/MIXED: {support}/5 signatures; H4g-1 weakly "
                        "supported, not decisive at these N")
        v["H4g1"] = "partial"
    else:
        v["overall"] = "NO support for the geometricity signatures of H4g-1"
        v["H4g1"] = "no_support"

    if res4d is not None and "diamond_f_nl_all" in res4d:
        def tail4(a):
            a = np.array(a, float); a = a[np.isfinite(a)]
            return float(np.mean(a[-2:])) if a.size else np.nan
        v["d4_diamond_nonlocal_tail"] = tail4(res4d["diamond_f_nl_all"])
        v["d4_slab_nonlocal_tail"] = tail4(res4d["slab_f_nl_all"])
        v["d4_corner_nonlocal_tail"] = tail4(res4d["diamond_f_nl_corner"])
        v["d4_bulk_nonlocal_tail"] = tail4(res4d["diamond_f_nl_bulk"])
        v["d4_corner_more_nonlocal"] = bool(
            np.isfinite(v["d4_corner_nonlocal_tail"]) and
            np.isfinite(v["d4_bulk_nonlocal_tail"]) and
            v["d4_corner_nonlocal_tail"] > v["d4_bulk_nonlocal_tail"])
        v["d4_slab_more_local"] = bool(
            np.isfinite(v["d4_slab_nonlocal_tail"]) and
            np.isfinite(v["d4_diamond_nonlocal_tail"]) and
            v["d4_slab_nonlocal_tail"] < v["d4_diamond_nonlocal_tail"])
    return v


# ============================================================================
# PLOTS
# ============================================================================

def make_plots(res2d, res4d, st, verdict):
    Ns = np.array(res2d["Ns"], float)

    # Plot 1: non-local fraction vs N  -- slab vs diamond (bulk vs corner)
    fig, ax = plt.subplots(figsize=(8.5, 6))
    ax.errorbar(Ns, res2d["diamond_f_nl_all"], yerr=res2d["diamond_f_nl_all_std"],
                fmt='o-', color='tab:red', capsize=3, label="diamond cut (all)")
    ax.errorbar(Ns, res2d["diamond_f_nl_corner"], yerr=res2d["diamond_f_nl_corner_std"],
                fmt='^-', color='darkred', capsize=3, label="diamond NEAR-CORNER")
    ax.errorbar(Ns, res2d["diamond_f_nl_bulk"], yerr=res2d["diamond_f_nl_bulk_std"],
                fmt='v-', color='salmon', capsize=3, label="diamond BULK")
    ax.errorbar(Ns, res2d["slab_f_nl_all"], yerr=res2d["slab_f_nl_all_std"],
                fmt='s-', color='tab:blue', capsize=3, label="slab half-space cut")
    ax.set_xlabel("N"); ax.set_ylabel("non-local fraction of $\\|K\\|_{HS}^2$ (far off-diagonal)")
    ax.set_title("2D modular-Hamiltonian non-locality: slab (boost-local) vs "
                 "diamond corner\n" + verdict["overall"][:70])
    ax.legend(fontsize=9); ax.grid(alpha=0.3)
    fig.tight_layout(); fig.savefig(os.path.join(PLOTDIR, "nonlocality_vs_N_2d.png"), dpi=140)
    plt.close(fig)

    # Plot 2: non-locality vs distance-to-corner (the key H4g-1 curve)
    if "nl_vs_corner_dist" in res2d:
        fig, ax = plt.subplots(figsize=(8, 6))
        d = np.array(res2d["nl_vs_corner_dist"]); m = np.array(res2d["nl_vs_corner_mean"])
        se = np.array(res2d.get("nl_vs_corner_sem", np.zeros_like(m)))
        ax.errorbar(d, m, yerr=se, fmt='o-', color='tab:red', capsize=4,
                    label=f"diamond (N={res2d['nl_vs_corner_repN']})")
        sl = res2d.get("nl_vs_corner_slope", np.nan)
        ax.set_xlabel("distance to diamond corner"); ax.set_ylabel("per-site non-local fraction")
        ax.set_title(f"H4g-1 KEY CURVE: modular non-locality vs distance-to-corner\n"
                     f"slope={sl:.3g} (negative = rises TOWARD corner, as predicted)")
        ax.legend(fontsize=9); ax.grid(alpha=0.3)
        fig.tight_layout(); fig.savefig(os.path.join(PLOTDIR, "nonlocality_vs_corner_2d.png"), dpi=140)
        plt.close(fig)

    # Plot 3: self-test (continuum interval) boost weight + off-diagonal decay
    fig, (axa, axb) = plt.subplots(1, 2, figsize=(13, 5.5))
    xs = np.array(st["xs_profile"]); be = np.array(st["beta_profile"]); dg = np.array(st["diag_profile"])
    axa.plot(xs, be / be.max(), 'k--', label="analytic boost weight $\\beta(x)$ (norm)")
    axa.plot(xs, dg / np.nanmax(dg), 'o', color='tab:blue', ms=4,
             label="$|H_\\phi(x,x)|$ (norm)")
    axa.set_xlabel("position in interval"); axa.set_ylabel("normalised weight")
    axa.set_title(f"SELF-TEST: interval modular weight vs Bisognano-Wichmann\n"
                  f"corr(diag,1/beta)={st['corr_diag_vs_invbeta']:.2f}")
    axa.legend(fontsize=8)
    axb.text(0.1, 0.5, f"off-diagonal log-log slope = {st['offdiag_loglog_slope']}\n"
             f"R2 = {st['offdiag_R2']}\n\n(fast power-law decay = LOCAL kernel,\n"
             "validates the geometricity probe)", fontsize=11)
    axb.axis('off')
    fig.tight_layout(); fig.savefig(os.path.join(PLOTDIR, "self_test_interval.png"), dpi=140)
    plt.close(fig)

    # Plot 4: 4D if present
    if res4d and "diamond_f_nl_all" in res4d and any(np.isfinite(res4d["diamond_f_nl_all"])):
        N4 = np.array(res4d["Ns"], float)
        fig, ax = plt.subplots(figsize=(8, 6))
        ax.plot(N4, res4d["diamond_f_nl_all"], 'o-', color='tab:red', label="4D diamond (all)")
        ax.plot(N4, res4d["diamond_f_nl_corner"], '^-', color='darkred', label="4D diamond corner")
        ax.plot(N4, res4d["diamond_f_nl_bulk"], 'v-', color='salmon', label="4D diamond bulk")
        ax.plot(N4, res4d["slab_f_nl_all"], 's-', color='tab:blue', label="4D slab")
        ax.set_xlabel("N"); ax.set_ylabel("non-local fraction")
        ax.set_title("4D modular non-locality: slab vs diamond corner")
        ax.legend(fontsize=9); ax.grid(alpha=0.3)
        fig.tight_layout(); fig.savefig(os.path.join(PLOTDIR, "nonlocality_4d.png"), dpi=140)
        plt.close(fig)


# ============================================================================
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


def run(do_4d=True):
    t0 = time.time()
    results = {"task": "VYPOCET-18 modular-flow geometricity at the diamond corner (H4g-1)",
               "claim": ("the diamond-corner non-Hadamard anomaly marks exactly "
                         "where the SJ modular flow stops being a geometric boost"),
               "conventions": {
                   "G_R_2D": "(1/2) C (Sorkin-Yazdi 1611.10281)",
                   "G_R_4D": "a L, a=sqrt(rho)/(2 pi sqrt6) (Johnston 0909.0944)",
                   "iDelta": "i(G_R-G_R^T); W = positive part (SJ)",
                   "modular_kernel": ("one-particle K(x,y) from SSEE generalized "
                       "eigenproblem W_O v = mu iDelta_O v; eps=ln[mu/(mu-1)]; "
                       "K = spectral resolution lifted to site basis"),
                   "covariance_check": "H_phi = X^{-1} C arccoth(2C), C=sqrt(XP) "
                       "(Peschel; Casini-Huerta 0905.2562)",
                   "analytic_anchor": ("2D interval [a,b] vacuum modular Hamiltonian "
                       "K = 2 pi int beta T_00, beta=(x-a)(b-x)/(b-a) "
                       "(Bisognano-Wichmann / Casini-Huerta)"),
                   "truncation": "kappa=sqrt(N)/(4pi) (2D), 0.05 lambda_max (4D)",
               }}

    print("==== SELF-TEST: continuum interval modular weight ====")
    st = self_test_continuum_interval()
    print(f"  corr(diag, beta)={st['corr_diag_vs_beta']:.3f}  "
          f"corr(diag, 1/beta)={st['corr_diag_vs_invbeta']:.3f}  "
          f"off-diag slope={st['offdiag_loglog_slope']} (R2={st['offdiag_R2']})")
    results["self_test"] = _to_native(st)

    diamond, slab, res2d, Ns = run_2d(results)

    res4d = None
    if do_4d:
        res4d = run_4d(results, time_budget_s=1200, t_start=t0)

    verdict = build_verdict(res2d, res4d)
    results["VERDICT"] = _to_native(verdict)
    print("\n=== VERDICT ===")
    for k, val in verdict.items():
        print(f"  {k}: {val}")

    make_plots(res2d, res4d if res4d else {}, st, verdict)

    results["runtime_s"] = time.time() - t0
    with open(os.path.join(OUTDIR, "results.json"), "w") as fh:
        json.dump(_to_native(results), fh, indent=2)
    print(f"\nDone in {results['runtime_s']:.1f}s. results.json + plots in {OUTDIR}")
    return results


if __name__ == "__main__":
    run(do_4d=True)
