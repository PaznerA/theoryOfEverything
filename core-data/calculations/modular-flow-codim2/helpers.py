# -*- coding: utf-8 -*-
"""
VYPOCET-22 helpers : LOCAL region builders + codim-2 modular-kernel diagnostics.

LIBRARY-EXTENSION RULE (this round): every new region / diagnostic helper lives
HERE, local to the calc dir.  We do NOT edit lib/toe/*.py (VYPOCET-21 owns
causet.py).  Functions that are ripe to migrate carry a ``# LIB-PROPOSAL`` tag
and a ready-to-lift signature; those are echoed in results.json["lib_proposals"].

The codim-2 question (H5g-3, BRAINSTORM-05): VYPOCET-20 (F-024) showed the 4D
diamond NULL-TIP fails the 2D corner mechanism (nl_vs_corner slope +0.71, non-
locality FALLS toward the tip) because the tip is a DEGENERATING 2-SPHERE -- a
point, not a clean codim-2 locus.  H5g-3 says the right 4D analogue of the 2D
corner is a CODIM-2 JOINT (a wedge EDGE = a flat 2-plane where the boost Killing
vector vanishes), NOT the isolated tip.  These helpers build the cleanest such
geometry and re-run the VYPOCET-18/20 diagnostics with "distance-to-tip"
replaced by "distance-to-(codim-2)-edge".

GEOMETRY DESIGN (cleanest codim-2 joint).
  Rindler double-wedge in 4D Minkowski (t, x, y, z):
      W = { x > |t| }   (right Rindler wedge).
  Its modular flow is the exact x-t BOOST (Bisognano-Wichmann); the boost
  Killing vector  xi = x d_t + t d_x  VANISHES on the EDGE
      E = { t = 0, x = 0 }  =  the flat 2-plane spanned by (y, z).
  E is a genuine codim-2 locus (2 of 4 coords pinned, 2 free) and it is FLAT
  (not a shrinking sphere) -- exactly the H5g-3 prediction.  We sprinkle a
  symmetric causal "double-diamond" box around the origin and cut the region
  O = { x > 0 } (the t=0 half-space whose causal domain is the right wedge);
  the entangling surface of O is the codim-2 edge E.  Per-site distance-to-edge
  is  d_E = sqrt(t^2 + x^2)  (transverse distance to the 2-plane {t=x=0}),
  the direct 4D analogue of the 2D distance-to-corner.

  CONTROL (no joint): a 4D SLAB  { 0 < t < T, |x_i| < L }  with the half-space
  cut x>0, matched to the wedge box in VOLUME and DENSITY.  The slab's
  entangling surface x=0 is a flat codim-1 hyperplane with NO codim-2 joint
  (the boost flows freely along it everywhere) -- the geometric "boost has
  somewhere to go" control, exactly as the slab was in VYPOCET-18/20.

DYNAMICAL OBJECT.  Identical to the VYPOCET-20 primary: the smeared
Benincasa-Dowker d'Alembertian eps=0.6, G_R = B_eps^{-1}, iDelta = i(G_R-G_R^T),
SJ Wightman W = positive part.  We compose this from toe.causet helpers where
they exist (causal_matrix, pauli_jordan) and reproduce the SMEARED BD matrix +
SJ-floor exactly from VYPOCET-20 (toe.causet only ships the SHARP BD inverse).

Only numpy is used here; toe does the SJ / fit / diagnostic primitives.
"""

from __future__ import annotations

from math import comb

import numpy as np

# ---------------------------------------------------------------------------
# Benincasa-Dowker SMEARED constants (Aslanbeigi-Saravani-Sorkin 1305.2588;
# Belenchia 1507.00330) -- identical to VYPOCET-20 / ssee-bd-4d.
# ---------------------------------------------------------------------------
BD4_C = np.array([1.0, -9.0, 16.0, -8.0])
BD4_ALPHA = -4.0 / np.sqrt(6.0)
BD4_BETA = 4.0 / np.sqrt(6.0)


# ===========================================================================
# REGION BUILDERS  (rng REQUIRED, returns (N, 4) coords (t, x, y, z))
# ===========================================================================

def sprinkle_wedge_box4d(N, rng, *, t_half=0.5, x_half=0.5, yz_half=0.5):
    """LIB-PROPOSAL  sprinkle_wedge_box4d(N, rng, *, t_half, x_half, yz_half)
    Symmetric causal box in 4D Minkowski centred on the origin, designed so the
    half-space cut O={x>0} has its entangling surface on the CODIM-2 EDGE
    E={t=0,x=0} of the right Rindler wedge W={x>|t|}.

    Box: { |t| <= t_half, |x| <= x_half, |y|,|z| <= yz_half }.  Uniform Lebesgue
    (Poisson) sprinkle.  Returns (t, x, y, z) columns.  The box is symmetric in
    t and x so the boost-orbit structure around E is sampled on both sides; the
    edge E is a flat 2-plane (the H5g-3 codim-2 joint).

    Evidence: NEW (VYPOCET-22); geometry analogue of sprinkle_slab4d
    (toe.causet) but t-symmetric so the wedge edge sits inside the box.
    Conventions: 4-volume = (2 t_half)(2 x_half)(2 yz_half)^2.
    """
    N = int(N)
    t = (rng.random(N) * 2.0 - 1.0) * t_half
    x = (rng.random(N) * 2.0 - 1.0) * x_half
    yz = (rng.random((N, 2)) * 2.0 - 1.0) * yz_half
    return np.column_stack([t, x, yz])


def sprinkle_slab_box4d(N, rng, *, t_half=0.5, x_half=0.5, yz_half=0.5):
    """LIB-PROPOSAL  sprinkle_slab_box4d(N, rng, *, t_half, x_half, yz_half)
    Volume/density-MATCHED control box with NO codim-2 joint: the half-space cut
    O={x>0} entangling surface x=0 is a flat codim-1 hyperplane along which the
    boost flows freely everywhere.  Same box shape as the wedge builder (so the
    matching is exact) but interpreted as the VYPOCET-18/20 slab control: the
    geometric "boost has somewhere to go" reference.

    The difference between this and ``sprinkle_wedge_box4d`` is NOT the sprinkle
    (they are identical boxes) but the DIAGNOSTIC: for the slab control we probe
    distance-to-(flat hyperplane) = |x|, which has no codim-2 degeneracy, whereas
    the wedge probes distance-to-(codim-2 edge) = sqrt(t^2+x^2).  Keeping the box
    identical makes the geometry/density matching airtight.

    Evidence: NEW (VYPOCET-22); same matched box, different entangling locus.
    """
    return sprinkle_wedge_box4d(N, rng, t_half=t_half, x_half=x_half,
                                yz_half=yz_half)


def box4d_volume(t_half, x_half, yz_half):
    """4-volume of the symmetric box (t,x in [-h,h], y,z in [-h,h])."""
    return (2.0 * t_half) * (2.0 * x_half) * (2.0 * yz_half) ** 2


# ===========================================================================
# SMEARED BENINCASA-DOWKER OBJECT  (reproduced from VYPOCET-20 / ssee-bd-4d)
# toe.causet ships only the SHARP BD inverse (bd_dalembertian_inverse); the
# VYPOCET-20 validated object is the SMEARED eps=0.6 one, reproduced here.
# ===========================================================================

def bd_smeared_matrix(C, rho, eps):
    """LIB-PROPOSAL  bd_smeared_matrix(C, rho, eps) -> (N,N)
    SMEARED (non-local) 4D BD d'Alembertian, prefactor sqrt(eps)*sqrt(rho),
    f4(n,eps)=(1-eps)^n sum_i C_i binom(n,i-1) (eps/(1-eps))^{i-1}.
    Byte-for-byte the VYPOCET-20 bd_smeared_matrix.  (toe.causet only has the
    sharp variant via bd_dalembertian_inverse(...,dim=4); this is the smeared
    sibling that should migrate next to it.)

    Evidence: VYPOCET-09/20 (ssee-bd-4d, modular-flow-bd-4d bd_smeared_matrix);
    Aslanbeigi-Saravani-Sorkin 1305.2588 eqs 25-26.
    """
    C = np.asarray(C, dtype=np.float64)
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
    """G_R = B^{-1} with retardedness / conditioning diagnostics (VYPOCET-20)."""
    cond = float(np.linalg.cond(B))
    G = np.linalg.inv(B)
    triu_B = float(np.abs(np.triu(B, 1)).max())
    diag_G = float(np.abs(np.diag(G)).mean()) or 1.0
    triu_G = float(np.abs(np.triu(G, 1)).max())
    return G, {"cond_B": cond, "max_upper_B": triu_B,
               "max_upper_G_over_diag": triu_G / diag_G}


def sj_wightman_floored(iDelta, rel_floor=1e-10):
    """SJ Wightman = positive part of iDelta with the VYPOCET-09/20 relative
    floor (eigenvalues below rel_floor*lmax treated as numerical kernel, so
    inversion noise is not amplified).  Returns (W, w, V).

    NOTE: toe.sj.sj_state uses an ABSOLUTE tol=1e-12 cut; for the BD-inverse
    object (cond ~1e5-1e6) the RELATIVE floor is the validated VYPOCET-20 choice,
    so we reproduce it locally.  (LIB-PROPOSAL: add rel_floor option to
    toe.sj.sj_state.)
    """
    w, V = np.linalg.eigh(iDelta)
    lmax = np.max(np.abs(w)) if w.size else 0.0
    floor = rel_floor * lmax
    pos = w > floor
    W = (V[:, pos] * w[pos]) @ V[:, pos].conj().T
    return W, w, V


# ===========================================================================
# MODULAR HAMILTONIAN K(x,y)  --  COPIED VERBATIM from VYPOCET-18/20
# (one-particle K from the SSEE generalized eigenproblem; the ONLY thing that
#  changes vs VYPOCET-20 is the region geometry fed in -- wedge vs tip)
# ===========================================================================

def modular_kernel_ssee(W, iDelta, sub_idx, kappa=None, tol=1e-9):
    """One-particle modular kernel K(x,y) on region O from the SSEE generalized
    eigenproblem W_O v = mu iDelta_O v, eps=ln[mu/(mu-1)], lifted to the site
    basis.  UNTRUNCATED probe (kappa=None) = the genuine SJ modular flow whose
    geometricity Bisognano-Wichmann predicts.  Verbatim VYPOCET-20.

    LIB-PROPOSAL: toe.entropy.ssee returns only S; the FULL kernel K_site (needed
    for locality diagnostics) should be exposed as e.g.
    toe.entropy.modular_kernel(W, iDelta, sub_idx, *, kappa, tol) -> {K, eps, S}.
    """
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
    S = float(np.sum((nu + 0.5) * np.log(nu + 0.5)
                     - (nu - 0.5) * np.log(nu - 0.5)))

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


# ===========================================================================
# LOCALITY PROFILE + DIAGNOSTICS  --  COPIED VERBATIM from VYPOCET-18/20
# (the SPATIAL distance here is the full 3-space distance; the only NEW thing
#  is _nl_vs_edge_generic / d_E built on distance-to-CODIM-2-EDGE)
# ===========================================================================

def locality_profile(K, coords_sub):
    n = K.shape[0]
    Kabs = np.abs(K)
    xs = coords_sub[:, 1:]                         # spatial (x,y,z)
    diff = xs[:, None, :] - xs[None, :, :]
    Dij = np.sqrt(np.einsum('ijk,ijk->ij', diff, diff))
    diag = np.real(np.diag(K))
    return {"Dij": Dij, "Kabs": Kabs, "diag": diag, "xs": xs}


def nonlocal_fraction(Kabs, Dij, near_radius):
    n = Kabs.shape[0]
    off = ~np.eye(n, dtype=bool)
    K2 = Kabs ** 2
    tot = K2[off].sum()
    if tot <= 0:
        return np.nan
    far = off & (Dij > near_radius)
    return float(K2[far].sum() / tot)


def _rowfrac_subset(Kabs, Dij, near_r, mask):
    K2 = Kabs ** 2
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


def offdiag_slope_subset(Kabs, Dij, row_mask, loglog_slope, n_bins=16):
    rows = np.where(row_mask)[0]
    if rows.size < 3:
        return None, None, None, None
    dv = Dij[rows].ravel(); kv = Kabs[rows].ravel()
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


def nl_vs_edge_profile(Kabs, Dij, d_edge, near_r, n_zones=6):
    """LIB-PROPOSAL  nl_vs_locus(Kabs, Dij, d_locus, near_r, n_zones) -> (cen, mean)
    Per-site non-local fraction binned by distance to a TARGET LOCUS d_locus.
    The VYPOCET-20 ``_nl_vs_corner_generic`` is the special case
    d_locus = distance-to-tip; here d_locus = distance-to-(codim-2 edge).
    Negative slope of mean-nl vs d_locus = non-locality CONCENTRATES at the locus
    (the 2D corner signature).  Verbatim binning logic from VYPOCET-20.
    """
    K2 = Kabs ** 2
    np.fill_diagonal(K2, 0.0)
    rowtot = K2.sum(axis=1)
    farmask = (Dij > near_r)
    np.fill_diagonal(farmask, False)
    rowfar = (K2 * farmask).sum(axis=1)
    with np.errstate(divide='ignore', invalid='ignore'):
        nl = np.where(rowtot > 0, rowfar / rowtot, np.nan)
    good = np.isfinite(nl)
    dc = d_edge[good]; nlv = nl[good]
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
    """Diagonal boost-weight |K(x,x)| vs distance to the entangling surface
    (Bisognano-Wichmann linear check).  Verbatim VYPOCET-20."""
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
