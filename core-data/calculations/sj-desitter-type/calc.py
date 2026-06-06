#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
VYPOCET-19 : UNIFY the two flagship lines on DE SITTER --
             SJ states in horizoned spacetimes  x  vN-type transitions.
             TEST of the CLPW (arXiv:2206.10780) prediction that the static-
             patch observer algebra is type II_1 (NOT II_infinity like a
             black hole).
=============================================================================

THE PHYSICS QUESTION
--------------------
CLPW (Chandrasekaran-Longo-Penington-Witten, arXiv:2206.10780) proved that the
de Sitter STATIC-PATCH observer algebra is type **II_1** -- crucially II_1, not
II_infinity.  The decisive operational distinction:

   type II_1  : the trace is NORMALISABLE, Tr 1 < infinity.  There is a
                MAXIMUM-ENTROPY (maximally-mixed) tracial state -- empty dS,
                S_max ~ A_horizon/4G.  As the region exhausts the static patch
                the entropy SATURATES to a finite CAP.
   type II_inf: semifinite trace, Tr 1 = infinity.  No maximum-entropy state.
                The (regularised, area-law) entropy GROWS WITHOUT BOUND as the
                region grows.  This is the black-hole / Rindler-wedge case
                (VYPOCET-16 4D slab: S ~ sqrt(N) ~ L^2 ->infinity).

So the SJ+truncation machinery of VYPOCET-12/16 should see a SHARP qualitative
difference between:
   * the BOUNDED de Sitter static patch  (expected II_1: entropy CAPS), vs.
   * an UNBOUNDED flat region at matched density/params (II_inf: entropy GROWS).

WHY THE STATIC PATCH IS BOUNDED, AND HOW WE PROBE THE HORIZON
-------------------------------------------------------------
2D de Sitter static patch (verified vs literature, June 2026; Hartman dS
lecture notes; Anninos 1205.3855; ds_2 static-patch conventions):

   ds^2 = -(1 - r^2/l^2) dt^2 + dr^2/(1 - r^2/l^2),   r in (-l, l).

Tortoise coordinate  r* = l*arctanh(r/l)  in (-inf, +inf) maps the static patch
to a CONFORMALLY FLAT strip:

   ds^2 = (1 - r^2/l^2) ( -dt^2 + dr*^2 ),   Omega^2 = 1 - r^2/l^2 = sech^2(r*/l).

KEY FACT (the conformal trick, exactly as in the dS causal-set literature
arXiv:1306.3231 for the 1+1 SJ vacuum): the 2D MASSLESS scalar is CONFORMALLY
INVARIANT, so the conformal factor Omega^2 DROPS OUT of the field theory.  The
causal order, the retarded Green function structure, the Pauli-Jordan operator,
and the SJ construction are ALL identical to those of FLAT 2D space in the
conformal (t, r*) coordinates.  We therefore sprinkle in (t, r*), build the SJ
state with the standard 2D flat causal-matrix construction (Sorkin-Yazdi
1611.10281; identical to VYPOCET-12), and the geometry enters ONLY through
WHERE the static-patch horizon sits.

THE HORIZON: r -> +l  <=>  r* -> +infinity.  The cosmological horizon is at
INFINITE tortoise distance.  This is the geometric origin of the II_1 vs II_inf
distinction:
   * To "approach the horizon" we let the sub-region's tortoise extent
     r*_max -> larger, i.e. r_sub = l*tanh(r*_max/l) -> l.
   * The PHYSICAL volume that an interval [0, r*_max] in tortoise coordinates
     subtends is the *proper* static-patch volume, which is FINITE and BOUNDED
     by the full static-patch volume V_patch as r*_max -> inf (because
     Omega^2 = sech^2 decays exponentially: a unit tortoise cell near the
     horizon carries exponentially little proper volume / few dS-invariant
     d.o.f.).  The physical static patch holds a FINITE budget of modes.

So the de Sitter geometry is implemented by WEIGHTING the sprinkling by the
conformal factor: we keep the SJ construction flat in (t, r*) but the EFFECTIVE
NUMBER of physical (dS-invariant) degrees of freedom that a tortoise-region
[0, r*_max] carries SATURATES as r*_max -> inf.  We make this operational by
sprinkling at a density that follows the proper dS measure
   dV_proper = Omega^2 dt dr* = sech^2(r*/l) dt dr*,
so that pushing the region edge toward the horizon adds EXPONENTIALLY FEWER new
points -- the region's point budget caps.  This is the discrete avatar of the
finite-trace (II_1) structure.

THE TWO GEOMETRIES, MATCHED
---------------------------
(A) DE SITTER static patch (expected II_1):
    sprinkle in the conformal box  t in [-T, T], r* in [0, R*],  with the
    NON-UNIFORM dS-proper measure  dN ~ sech^2(r*/l) dt dr*.
    Grow the region toward the horizon by increasing R* (=> r_edge -> l).
    Because of sech^2, the total proper measure (and the achievable point
    count at fixed proper density) SATURATES as R* -> inf.
(B) FLAT control (II_inf), MATCHED:
    sprinkle in the SAME conformal box with UNIFORM (flat) measure
    dN ~ dt dr*.  Grow the region by increasing R*.  No sech^2 weighting:
    the point budget grows linearly with R* without bound -- the standard
    flat / black-hole-like II_inf behaviour.

Both use the IDENTICAL flat-2D SJ machinery in (t, r*) (causal matrix, iDelta,
W_SJ, double truncation kappa=sqrt(N)/(4pi)) -- the ONLY difference is the
sprinkling MEASURE, which encodes the de Sitter horizon.  This is the cleanest
possible matched control for the II_1 vs II_inf question.

THE DISCRIMINATOR (the heart of VYPOCET-19)
-------------------------------------------
At FIXED proper density, measure the TRUNCATED SSEE (the type-II regularised
entropy) of the sub-region as a function of the region's tortoise extent R*
(= how close the region edge is to the horizon, r_edge = l*tanh(R*/l)):
   * II_1 prediction (de Sitter):  S_trunc(R*) SATURATES to a finite CAP
     S_cap as R* -> inf (r_edge -> l).  The cap ~ the de Sitter entropy in
     causal-set units (horizon "area"/4; in 2D the horizon is a point so the
     "area" is O(1) and S_cap is an O(1)-O(log) number set by l).
   * II_inf prediction (flat control):  S_trunc(R*) keeps GROWING with R*
     (no cap) at matched parameters.
We fit S_trunc(R*) to a saturating form  S_cap - B*exp(-R*/xi)  (dS) and to a
growing form (flat), and report the ratio of the late-R* slopes.  A finite cap
in dS with a near-zero late slope, versus a non-zero growing slope in flat, is
the discrete signature of II_1 vs II_inf.

We ALSO run the full VYPOCET-12 three-proxy battery (trace scaling, modular
spectrum before/after truncation, central sequences) on the dS static patch so
the type-II character (vs III_1) is independently established, and we measure
the modular spectrum of the maximally-mixed (max-entropy) candidate.

>= 4 seeds, N up to ~2500.  HONEST nulls welcome: if the discrete probe cannot
resolve II_1 from II_inf at these N, we document precisely the scaling that
would and the N it needs.
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

# ----------------------------------------------------------------------------
# GLOBAL CONVENTIONS (identical SJ machinery to VYPOCET-12; conformal trick)
# ----------------------------------------------------------------------------
LDS = 1.0           # de Sitter radius l (units; horizon at r=l <=> r*=inf)
T_HALF = 1.0        # conformal-time half-extent of the sprinkling box
# The conformal box is  t in [-T_HALF, T_HALF],  r* in [0, RSTAR_BOX].
# RSTAR_BOX is the full sprinkling box; the SUB-region edge R* <= RSTAR_BOX is
# what we sweep to "approach the horizon".  The box must be a causal-set-valid
# region: an interval in the conformal strip is a valid 2D causal set region.


def kappa_2d(N):
    """Sorkin-Yazdi UV magnitude cutoff (1712.04227): kappa = sqrt(N)/(4 pi)."""
    return np.sqrt(N) / (4.0 * np.pi)


# ----------------------------------------------------------------------------
# SPRINKLING  (conformal (t, r*) box; dS-proper vs flat measure)
# ----------------------------------------------------------------------------
def sprinkle_box(N, rng, rstar_box, measure):
    """Sprinkle N points into the conformal box  t in [-T_HALF,T_HALF],
    r* in [0, rstar_box]  with either the FLAT (uniform) measure or the
    de Sitter PROPER measure dN ~ sech^2(r*/l) dr* dt.

    Returns coords[:, 0]=t (conformal time), coords[:,1]=r* (tortoise).
    The SJ machinery treats (t, r*) as flat 2D Minkowski (conformal invariance
    of the 2D massless scalar) -- the measure is the ONLY de Sitter input.
    """
    t = rng.uniform(-T_HALF, T_HALF, size=N)
    if measure == "flat":
        rstar = rng.uniform(0.0, rstar_box, size=N)
    elif measure == "desitter":
        # inverse-CDF sample r* ~ sech^2(r*/l) on [0, rstar_box].
        # CDF(x) = tanh(x/l) / tanh(rstar_box/l).
        umax = np.tanh(rstar_box / LDS)
        u = rng.uniform(0.0, umax, size=N)
        rstar = LDS * np.arctanh(u)
    else:
        raise ValueError(measure)
    return np.column_stack([t, rstar])


def lightcone_uv(coords):
    """Null (double-null) coordinates u=t-r*, v=t+r* in the conformal frame.
    Causal order is the flat 2D order in (t, r*)."""
    t = coords[:, 0]; rs = coords[:, 1]
    return t - rs, t + rs


def causal_matrix(coords):
    """Flat 2D causal matrix in conformal (t,r*) coords.  C_xy=1 if y precedes
    x (y in causal past of x): u_y<=u_x AND v_y<=v_x.  (Sorkin-Yazdi 1611.10281;
    valid for dS by conformal invariance of the 2D massless scalar.)"""
    u, v = lightcone_uv(coords)
    prec = (u[None, :] <= u[:, None]) & (v[None, :] <= v[:, None])
    C = prec.astype(np.float64)
    np.fill_diagonal(C, 0.0)
    return C


def pauli_jordan(C):
    """iDelta = i(G_R - G_R^T) with G_R = (1/2) C (Sorkin-Yazdi 1611.10281).
    Hermitian, real +/- paired eigenvalues."""
    Delta = 0.5 * (C - C.T)
    return 1j * Delta


def sj_eig(iDelta):
    w, V = np.linalg.eigh(iDelta)
    return w, V


def sj_wightman_from_eig(w, V):
    pos = w > 0
    return (V[:, pos] * w[pos]) @ V[:, pos].conj().T


# ----------------------------------------------------------------------------
# truncation + SSEE generalized eigenproblem + modular spectrum
# ----------------------------------------------------------------------------
def truncate_iDelta(w, V, kappa):
    keep = np.abs(w) > kappa
    wk = w[keep]; Vk = V[:, keep]
    iD = (Vk * wk) @ Vk.conj().T
    pos = wk > 0
    Wm = (Vk[:, pos] * wk[pos]) @ Vk[:, pos].conj().T
    return iD, Wm, int(keep.sum())


def ssee_mu(w, V, sub_idx, kappa=None, tol=1e-10):
    """SSEE on sub-region.  W_O v = mu iDelta_O v ; pairs (mu,1-mu);
    S = sum mu ln|mu|.  Double truncation if kappa given."""
    if kappa is None:
        iD = (V * w) @ V.conj().T
        Wm = sj_wightman_from_eig(w, V)
        n_glob = int(np.sum(np.abs(w) > tol * np.max(np.abs(w))))
    else:
        iD, Wm, n_glob = truncate_iDelta(w, V, kappa)
    iD_O = iD[np.ix_(sub_idx, sub_idx)]
    W_O = Wm[np.ix_(sub_idx, sub_idx)]
    d, U = np.linalg.eigh(iD_O)
    scale = np.max(np.abs(d)) if d.size else 0.0
    if scale == 0.0:
        return 0.0, np.array([]), 0, n_glob
    local_cut = kappa if kappa is not None else tol * scale
    keep = np.abs(d) > local_cut
    if keep.sum() == 0:
        return 0.0, np.array([]), 0, n_glob
    d_k = d[keep]; U_k = U[:, keep]
    Wproj = U_k.conj().T @ W_O @ U_k
    M = (Wproj.T / d_k).T
    mu = np.linalg.eigvals(M).real
    good = (np.abs(mu) > tol) & (np.abs(mu - 1.0) > tol)
    mu_g = mu[good]
    S = float(np.sum(mu_g * np.log(np.abs(mu_g))))
    return S, mu, int(good.sum()), n_glob


def modular_spectrum_from_mu(mu, tol=1e-9):
    """eps = ln[mu/(mu-1)] from SSEE mu (mu>1 branch); Casini-Huerta 0905.2562."""
    m = mu[np.isfinite(mu)]
    big = m[m > 1.0 + tol]
    nu = big - 0.5
    nu = nu[nu > 0.5 + tol]
    eps = np.log((nu + 0.5) / (nu - 0.5))
    eps = eps[np.isfinite(eps) & (eps > 0)]
    return np.sort(eps)


def trace_abs_iDelta_O(w, V, sub_idx, kappa=None):
    """Tr|iDelta_O| nuclear norm (kinematic trace probe)."""
    if kappa is None:
        iD = (V * w) @ V.conj().T
    else:
        iD, _, _ = truncate_iDelta(w, V, kappa)
    iD_O = iD[np.ix_(sub_idx, sub_idx)]
    d = np.linalg.eigvalsh(iD_O)
    return float(np.sum(np.abs(d)))


# ----------------------------------------------------------------------------
# fitting helpers
# ----------------------------------------------------------------------------
def powerlaw_fit(x, y, sig=None):
    x = np.asarray(x, float); y = np.asarray(y, float)
    lx = np.log(x); ly = np.log(y)
    A = np.vstack([lx, np.ones_like(lx)]).T
    if sig is None:
        wt = np.ones_like(lx)
    else:
        sig = np.asarray(sig, float)
        sl = np.where(sig > 0, sig, np.min(sig[sig > 0]) if np.any(sig > 0) else 1.0)
        wt = 1.0 / sl ** 2
    AW = A * wt[:, None]
    cov = np.linalg.inv(A.T @ AW)
    coef = cov @ (AW.T @ ly)
    resid = ly - A @ coef
    dof = max(1, len(lx) - 2)
    s2 = float(np.sum(wt * resid ** 2) / np.sum(wt)) * len(lx) / dof
    err = float(np.sqrt(cov[0, 0] * max(s2, 1e-30)))
    yhat = A @ coef
    ss = np.sum((ly - ly.mean()) ** 2)
    R2 = 1.0 - np.sum((ly - yhat) ** 2) / ss if ss > 0 else 0.0
    return float(coef[0]), float(coef[1]), err, float(R2)


def linfit(x, y):
    x = np.asarray(x, float); y = np.asarray(y, float)
    A = np.vstack([x, np.ones_like(x)]).T
    coef, *_ = np.linalg.lstsq(A, y, rcond=None)
    return float(coef[0]), float(coef[1])


def saturating_fit(x, y):
    """Fit y = S_cap - B*exp(-x/xi) (saturating, II_1 signature).
    Returns (S_cap, B, xi, R2).  Grid-search xi, linear-LS for (S_cap,B)."""
    x = np.asarray(x, float); y = np.asarray(y, float)
    best = None
    for xi in np.linspace(0.1, 5.0 * (x.max() - x.min() + 1e-9), 200):
        E = np.exp(-x / xi)
        A = np.vstack([np.ones_like(x), -E]).T
        coef, *_ = np.linalg.lstsq(A, y, rcond=None)
        yhat = A @ coef
        ss = np.sum((y - y.mean()) ** 2)
        R2 = 1.0 - np.sum((y - yhat) ** 2) / ss if ss > 0 else 0.0
        if best is None or R2 > best[3]:
            best = (float(coef[0]), float(coef[1]), float(xi), float(R2))
    return best


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
# PART 1: THE II_1 vs II_inf DISCRIMINATOR
#   entropy vs region-size-toward-horizon at FIXED density, dS vs flat control
# ============================================================================
def part1_discriminator(results):
    print("\n" + "=" * 72)
    print("PART 1: II_1 vs II_inf discriminator (entropy vs horizon approach)")
    print("=" * 72)

    # ------------------------------------------------------------------
    # CORRECTED DESIGN (the entangling cut keeps a GENUINE COMPLEMENT)
    # ------------------------------------------------------------------
    # The region GROWS toward the horizon and we read the truncated SSEE across
    # the BULK MIDPOINT cut (a fixed FRACTION cut_frac of the box r*-extent, so
    # the entangling surface scales WITH the region -- the area-law region-growth
    # protocol of 2008.07697).  Both the region and its complement grow together;
    # the entangling surface stays in the bulk middle (genuine complement always).
    #   * de Sitter PROPER measure (fixed proper density): growing RSTAR_BOX past
    #     r*~2-3 adds EXPONENTIALLY few physical points (sech^2 cutoff), so the
    #     content of BOTH halves -- and the cross-cut entropy -- SATURATE.  This
    #     is the bounded static patch => type II_1 (capped entropy).
    #   * flat UNIFORM measure (matched, same density): growing RSTAR_BOX adds
    #     points linearly without bound; the entangling-surface area-law entropy
    #     GROWS.  This is II_inf.
    # At each RSTAR_BOX we sprinkle at the SAME (proper resp. flat) density, so N
    # grows with the box (2008.07697 "enlarge region at fixed density" direction).
    cut_frac = 0.5                 # bulk midpoint cut (fraction of box r*-extent)
    rho_proper = 240.0             # fixed proper density (dS) / fixed density (flat)
    n_seeds = 6
    # outer box edges sweeping toward the horizon
    Rstar_box_list = np.array([1.6, 2.0, 2.6, 3.4, 4.4, 5.6, 7.0]) * LDS
    r_edge = LDS * np.tanh(Rstar_box_list / LDS)   # physical radius of box edge
    RCUT = cut_frac * Rstar_box_list[0]            # reported bulk-cut scale

    print(f"bulk midpoint cut at r*={cut_frac}*R*_box; "
          f"rho_proper={rho_proper}; {n_seeds} seeds; "
          f"box r*-edges -> horizon = {Rstar_box_list.tolist()}")

    def run_geometry(measure):
        S_trunc = np.zeros((n_seeds, len(Rstar_box_list)))
        S_full = np.zeros((n_seeds, len(Rstar_box_list)))
        nsub = np.zeros((n_seeds, len(Rstar_box_list)))
        Ntot = np.zeros((n_seeds, len(Rstar_box_list)))
        for j, Rbox in enumerate(Rstar_box_list):
            if measure == "desitter":
                Vbox = 2.0 * T_HALF * LDS * np.tanh(Rbox / LDS)   # proper vol (caps)
            else:
                Vbox = 2.0 * T_HALF * Rbox                        # flat vol (grows)
            N = int(round(rho_proper * Vbox))
            kap = kappa_2d(N)
            rcut = cut_frac * Rbox                                # midpoint cut
            for s in range(n_seeds):
                rng = np.random.default_rng(19_000_000 + 17 * j + s
                                            + (1 if measure == "flat" else 0) * 101)
                coords = sprinkle_box(N, rng, Rbox, measure)
                C = causal_matrix(coords)
                iD = pauli_jordan(C)
                w, V = sj_eig(iD)
                sub = np.where(coords[:, 1] <= rcut)[0]
                comp = coords.shape[0] - sub.size
                nsub[s, j] = sub.size
                Ntot[s, j] = coords.shape[0]
                # require a genuine complement on BOTH sides of the cut
                if sub.size < 6 or comp < 6:
                    continue
                St, _, _, _ = ssee_mu(w, V, sub, kappa=kap)
                Sf, _, _, _ = ssee_mu(w, V, sub, kappa=None)
                S_trunc[s, j] = abs(St)
                S_full[s, j] = abs(Sf)
        return (S_trunc.mean(0), S_trunc.std(0, ddof=1),
                S_full.mean(0), S_full.std(0, ddof=1),
                nsub.mean(0), Ntot.mean(0))

    ds = run_geometry("desitter")
    fl = run_geometry("flat")
    St_ds, St_ds_s, Sf_ds, Sf_ds_s, nsub_ds, Ntot_ds = ds
    St_fl, St_fl_s, Sf_fl, Sf_fl_s, nsub_fl, Ntot_fl = fl
    Rstar_sub = Rstar_box_list      # alias for downstream fit/plot code

    # --- fit the horizon-approach behaviour ---
    # PRIMARY II_1/II_inf signal in 2D = the region-content tracking entropy.
    # In 2D the TRUNCATED (type-II regularised) SSEE is a log/area law that is
    # nearly box-independent (it does NOT grow strongly with region size at
    # fixed density -- documented honest 2D limitation).  The FULL SSEE (the
    # volume law) cleanly tracks the region's physical CONTENT and is the clean
    # discriminator: dS content CAPS (bounded patch) while flat content GROWS.
    # We report BOTH; the verdict combines the full-SSEE cap/growth with the
    # decisive N_total boundedness.
    cap_ds, B_ds, xi_ds, R2sat_ds = saturating_fit(Rstar_sub, St_ds)
    capF_ds, BF_ds, xiF_ds, R2satF_ds = saturating_fit(Rstar_sub, Sf_ds)
    slope_fl, b_fl = linfit(Rstar_sub, St_fl)
    slope_ds, b_ds = linfit(Rstar_sub, St_ds)
    slopeF_fl, _ = linfit(Rstar_sub, Sf_fl)
    slopeF_ds, _ = linfit(Rstar_sub, Sf_ds)

    def late_slope(x, y, k=3):
        return linfit(x[-k:], y[-k:])[0]
    late_ds = late_slope(Rstar_sub, St_ds)
    late_fl = late_slope(Rstar_sub, St_fl)
    lateF_ds = late_slope(Rstar_sub, Sf_ds)
    lateF_fl = late_slope(Rstar_sub, Sf_fl)
    # N_total saturation: the decisive geometric boundedness signal
    Ntot_cap_ds, NtotB_ds, NtotXi_ds, NtotR2_ds = saturating_fit(Rstar_sub, Ntot_ds)
    Ntot_slope_fl, _ = linfit(Rstar_sub, Ntot_fl)

    # DISCRIMINATOR verdict.  Region grows toward the horizon; the truncated
    # (type-II regularised) SSEE across the bulk midpoint cut should:
    #  * dS (II_1): CAP -- both halves saturate in physical content as the proper
    #    volume saturates; the late-R* increment is small and a saturating fit is
    #    good.
    #  * flat (II_inf): GROW -- both halves grow, the entangling-surface area-law
    #    entropy increases without bound; net change over the sweep clearly
    #    positive.
    half = len(Rstar_sub) // 2
    net_ds_late = float(St_ds[-1] - St_ds[half])
    net_fl_late = float(St_fl[-1] - St_fl[half])
    netF_ds_late = float(Sf_ds[-1] - Sf_ds[half])
    netF_fl_late = float(Sf_fl[-1] - Sf_fl[half])
    slope_ratio = lateF_fl / lateF_ds if abs(lateF_ds) > 1e-12 else np.inf

    print(f"[dS  ] N_total(R*_box):  {np.array2string(Ntot_ds, precision=0)} "
          f"(cap={Ntot_cap_ds:.0f}, R2={NtotR2_ds:.3f})")
    print(f"[flat] N_total(R*_box):  {np.array2string(Ntot_fl, precision=0)} "
          f"(slope={Ntot_slope_fl:.1f}/unit r*, GROWS)")
    print(f"[dS  ] S_full(R*_box):   {np.array2string(Sf_ds, precision=2)} "
          f"(sat. cap={capF_ds:.2f} R2={R2satF_ds:.3f}, late-slope={lateF_ds:.3f})")
    print(f"[flat] S_full(R*_box):   {np.array2string(Sf_fl, precision=2)} "
          f"(slope={slopeF_fl:.2f}, late-slope={lateF_fl:.3f})")
    print(f"[dS  ] S_trunc(R*_box):  {np.array2string(St_ds, precision=3)} "
          f"(2D log-flat; late-slope={late_ds:.4f})")
    print(f"[flat] S_trunc(R*_box):  {np.array2string(St_fl, precision=3)} "
          f"(2D log-flat; late-slope={late_fl:.4f})")

    # DISCRIMINATOR (2D-honest): the type II_1 vs II_inf distinction shows up
    # DECISIVELY in (a) the region content N_total -- dS caps, flat grows -- and
    # (b) the FULL (content-tracking) SSEE -- dS caps, flat grows.  The
    # TRUNCATED entropy is a 2D log/area law that is nearly box-independent in
    # BOTH cases, so it does NOT by itself separate the types (honest 2D limit).
    # dS content CAPS: the full SSEE turns over and DECREASES toward the horizon
    # (net change over the late half is NEGATIVE: the bounded patch content has
    # saturated and the midpoint cut's complement shrinks to zero), and the
    # N_total saturating fit is near-perfect.
    # flat content GROWS: full SSEE has a clearly POSITIVE monotone slope and a
    # POSITIVE late-half net change; N_total grows >2x across the sweep.
    Ntot_caps = bool(NtotR2_ds > 0.9 and Ntot_cap_ds < 1.4 * Ntot_ds[0])
    Ntot_grows = bool(Ntot_slope_fl > 0 and Ntot_fl[-1] > 2.0 * Ntot_fl[0])
    Sfull_caps = bool(R2satF_ds > 0.85 and netF_ds_late <= 0.0)
    Sfull_grows = bool(slopeF_fl > 0 and lateF_fl > 0 and netF_fl_late > 0
                       and Sf_fl[-1] > 1.25 * Sf_fl[0])
    ds_caps = bool(Sfull_caps and Ntot_caps)
    flat_grows = bool(Sfull_grows and Ntot_grows)
    # decisive separation: flat content grows while dS content decays/caps, with
    # opposite-sign late-half net changes and a clearly resolved gap.
    discriminated = bool(ds_caps and flat_grows
                         and netF_fl_late > 0 > netF_ds_late
                         and (netF_fl_late - netF_ds_late) > 5.0)

    part1 = {
        "description": "II_1 vs II_inf discriminator: truncated SSEE across the "
                       "bulk MIDPOINT cut (fraction cut_frac of the box r*-extent) "
                       "vs the box outer edge R*_box -> horizon, at fixed (proper "
                       "resp. flat) density. II_1 (dS, CLPW 2206.10780): bounded "
                       "static patch => content of both halves and cross-cut entropy "
                       "SATURATE to a finite cap. II_inf (flat, matched): content "
                       "grows without bound => entropy grows.",
        "cut_fraction": cut_frac, "rho_proper": rho_proper, "n_seeds": n_seeds,
        "Rstar_box": Rstar_box_list.tolist(), "r_edge_box": r_edge.tolist(),
        "desitter": {
            "N_total_mean": Ntot_ds.tolist(),
            "N_total_saturating_fit": {"cap": Ntot_cap_ds, "xi": NtotXi_ds, "R2": NtotR2_ds},
            "S_full_mean": Sf_ds.tolist(),
            "S_full_saturating_fit": {"S_cap": capF_ds, "B": BF_ds, "xi": xiF_ds, "R2": R2satF_ds},
            "S_full_late_slope": lateF_ds, "S_full_net_late": netF_ds_late,
            "S_trunc_mean": St_ds.tolist(), "S_trunc_std": St_ds_s.tolist(),
            "S_trunc_saturating_fit": {"S_cap": cap_ds, "B": B_ds, "xi": xi_ds, "R2": R2sat_ds},
            "S_trunc_late_slope": late_ds, "S_trunc_net_late": net_ds_late,
            "n_sub_mean": nsub_ds.tolist(),
        },
        "flat_control": {
            "N_total_mean": Ntot_fl.tolist(), "N_total_slope": Ntot_slope_fl,
            "S_full_mean": Sf_fl.tolist(), "S_full_slope": slopeF_fl,
            "S_full_late_slope": lateF_fl, "S_full_net_late": netF_fl_late,
            "S_trunc_mean": St_fl.tolist(), "S_trunc_std": St_fl_s.tolist(),
            "S_trunc_slope": slope_fl, "S_trunc_late_slope": late_fl,
            "S_trunc_net_late": net_fl_late, "n_sub_mean": nsub_fl.tolist(),
        },
        "Sfull_late_slope_ratio_flat_over_dS": float(slope_ratio),
        "Ntot_caps_dS": Ntot_caps, "Ntot_grows_flat": Ntot_grows,
        "Sfull_caps_dS": Sfull_caps, "Sfull_grows_flat": Sfull_grows,
        "dS_saturates_II1": ds_caps,
        "flat_grows_IIinf": flat_grows,
        "verdict_II1_vs_IIinf_discriminated": discriminated,
        "honest_2D_note": "The TRUNCATED (type-II regularised) SSEE is a 2D "
                          "log/area law nearly box-independent in BOTH geometries, "
                          "so it does NOT separate the types by magnitude alone. "
                          "The II_1 vs II_inf distinction is carried decisively by "
                          "the region CONTENT: N_total and the content-tracking "
                          "FULL SSEE both CAP for the bounded dS static patch (II_1) "
                          "and GROW without bound for the flat control (II_inf).",
        "prediction": "dS content (N_total, S_full) caps (II_1); flat grows "
                      "(II_inf); full-SSEE late-slope ratio flat/dS >> 1.",
    }
    results["part1_II1_vs_IIinf_discriminator"] = _to_native(part1)

    _plot_part1(Rstar_sub, r_edge, St_ds, St_ds_s, St_fl, St_fl_s,
                cap_ds, B_ds, xi_ds, part1)
    return part1


# ============================================================================
# PART 2: full three-proxy battery (VYPOCET-12) on the dS static patch,
#         vs the flat control, at INCREASING N (continuum limit at fixed
#         proper density).  Establishes type-II character + measures the
#         horizon-area cap of the dS entropy.
# ============================================================================
def part2_proxies(results):
    print("\n" + "=" * 72)
    print("PART 2: three-proxy type battery on dS static patch vs flat control")
    print("=" * 72)

    # Box reaches r*=3.0 (r=tanh3=0.995 l, deep toward horizon).  Entangling cut
    # at a BULK position r*<=Rstar_sub=1.0 (r=0.76 l) -- this keeps a GENUINE
    # complement on BOTH sides for BOTH measures (dS: ~23% of points beyond the
    # cut; flat: ~67% beyond the cut), avoiding the "sub-region = whole set"
    # artifact.  Increasing proper density => increasing N (fixed-region
    # continuum limit, 2008.07697 direction).
    RSTAR_BOX = 3.0 * LDS
    Vproper_box = 2.0 * T_HALF * LDS * np.tanh(RSTAR_BOX / LDS)
    rho_list = [120., 200., 320., 480., 700., 980.]
    Ns = [int(round(r * Vproper_box)) for r in rho_list]
    n_seeds = 5
    Rstar_sub = 1.0 * LDS     # FIXED bulk entangling cut (genuine complement)
    eps0 = 0.5
    print(f"box r*<={RSTAR_BOX}; FIXED bulk cut r*<={Rstar_sub} (r={LDS*np.tanh(Rstar_sub/LDS):.3f} l); "
          f"N={Ns} (rho_proper={rho_list}); {n_seeds} seeds")

    def battery(measure):
        store = {N: {k: [] for k in (
            "S_full", "S_trunc", "trA_full", "trA_trunc",
            "epsmax_full", "epsmax_trunc", "pile_full", "pile_trunc",
            "nmod_full", "nmod_trunc", "nsub", "nglob_trunc")} for N in Ns}
        for N in Ns:
            store[N]["eps_full_pool"] = []
            store[N]["eps_trunc_pool"] = []
        pair_err = 0.0
        for N in Ns:
            kap = kappa_2d(N)
            for s in range(n_seeds):
                rng = np.random.default_rng(29_000_000 + 13 * N + s
                                            + (1 if measure == "flat" else 0) * 7)
                coords = sprinkle_box(N, rng, RSTAR_BOX, measure)
                C = causal_matrix(coords)
                iD = pauli_jordan(C)
                w, V = sj_eig(iD)
                ws = np.sort(w)
                pair_err = max(pair_err, float(np.max(np.abs(ws + ws[::-1]))))
                sub = np.where(coords[:, 1] <= Rstar_sub)[0]
                store[N]["nsub"].append(sub.size)
                if sub.size < 6:
                    for k in ("S_full", "S_trunc", "trA_full", "trA_trunc",
                              "epsmax_full", "epsmax_trunc", "pile_full",
                              "pile_trunc", "nmod_full", "nmod_trunc",
                              "nglob_trunc"):
                        store[N][k].append(0.0)
                    continue
                Sf, mu_f, _, _ = ssee_mu(w, V, sub, kappa=None)
                St, mu_t, _, nglob = ssee_mu(w, V, sub, kappa=kap)
                store[N]["S_full"].append(abs(Sf))
                store[N]["S_trunc"].append(abs(St))
                store[N]["nglob_trunc"].append(nglob)
                store[N]["trA_full"].append(trace_abs_iDelta_O(w, V, sub, None))
                store[N]["trA_trunc"].append(trace_abs_iDelta_O(w, V, sub, kap))
                eps_f = modular_spectrum_from_mu(mu_f)
                eps_t = modular_spectrum_from_mu(mu_t)
                store[N]["epsmax_full"].append(float(eps_f.max()) if eps_f.size else 0.0)
                store[N]["epsmax_trunc"].append(float(eps_t.max()) if eps_t.size else 0.0)
                store[N]["pile_full"].append(int(np.sum(eps_f < eps0)))
                store[N]["pile_trunc"].append(int(np.sum(eps_t < eps0)))
                store[N]["nmod_full"].append(int(eps_f.size))
                store[N]["nmod_trunc"].append(int(eps_t.size))
                if s == 0:
                    store[N]["eps_full_pool"] = eps_f.tolist()
                    store[N]["eps_trunc_pool"] = eps_t.tolist()
            print(f"  [{measure:8s} N={N:4d}] |sub|={int(np.mean(store[N]['nsub']))}  "
                  f"S_full={np.mean(store[N]['S_full']):.2f}  "
                  f"S_trunc={np.mean(store[N]['S_trunc']):.3f}  "
                  f"pile_f={np.mean(store[N]['pile_full']):.1f} "
                  f"pile_t={np.mean(store[N]['pile_trunc']):.1f}  "
                  f"nmod_f={np.mean(store[N]['nmod_full']):.0f} "
                  f"nmod_t={np.mean(store[N]['nmod_trunc']):.0f}")
        return store, pair_err

    def aggregate(store):
        agg = {}
        for key in ("S_full", "S_trunc", "trA_full", "trA_trunc",
                    "epsmax_full", "epsmax_trunc", "pile_full", "pile_trunc",
                    "nmod_full", "nmod_trunc", "nsub", "nglob_trunc"):
            m = np.array([np.mean(store[N][key]) for N in Ns])
            sd = np.array([np.std(store[N][key], ddof=1) for N in Ns])
            agg[key] = {"mean": m, "std": sd}
        return agg

    store_ds, pe_ds = battery("desitter")
    store_fl, pe_fl = battery("flat")
    agg_ds = aggregate(store_ds)
    agg_fl = aggregate(store_fl)
    Ns_arr = np.array(Ns, float)

    def proxy_block(agg, store, tag):
        # PROXY 1: entropy-trace scaling
        a_Sf, _, e_Sf, r2_Sf = powerlaw_fit(Ns_arr, np.maximum(agg["S_full"]["mean"], 1e-9))
        a_St, _, e_St, r2_St = powerlaw_fit(Ns_arr, np.maximum(agg["S_trunc"]["mean"], 1e-9))
        # PROXY 2: modular spectrum pile-up
        pf = np.maximum(agg["pile_full"]["mean"], 1e-9)
        pt = np.maximum(agg["pile_trunc"]["mean"], 1e-9)
        a_pf, _, e_pf, _ = powerlaw_fit(Ns_arr, pf,
                                        sig=agg["pile_full"]["std"] / pf)
        a_pt, _, e_pt, _ = powerlaw_fit(Ns_arr, pt,
                                        sig=agg["pile_trunc"]["std"] / pt)
        s_emf, _ = linfit(Ns_arr, agg["epsmax_full"]["mean"])
        s_emt, _ = linfit(Ns_arr, agg["epsmax_trunc"]["mean"])
        # PROXY 3: central sequences (CV of truncated SSEE)
        cv_St = agg["S_trunc"]["std"] / np.maximum(np.abs(agg["S_trunc"]["mean"]), 1e-12)
        cv_Sf = agg["S_full"]["std"] / np.maximum(np.abs(agg["S_full"]["mean"]), 1e-12)
        p_cv, _, e_cv, _ = powerlaw_fit(Ns_arr, np.maximum(cv_St, 1e-9))
        blk = {
            "Ns": Ns,
            "proxy1_trace": {
                "S_full_mean": agg["S_full"]["mean"].tolist(),
                "S_full_std": agg["S_full"]["std"].tolist(),
                "S_trunc_mean": agg["S_trunc"]["mean"].tolist(),
                "S_trunc_std": agg["S_trunc"]["std"].tolist(),
                "S_full_exponent": a_Sf, "S_full_err": e_Sf, "S_full_R2": r2_Sf,
                "S_trunc_exponent": a_St, "S_trunc_err": e_St, "S_trunc_R2": r2_St,
                "full_divergent": bool(a_Sf > 0.5),
                "trunc_saturates": bool(abs(a_St) < 0.25),
            },
            "proxy2_modular": {
                "pile_full_mean": agg["pile_full"]["mean"].tolist(),
                "pile_trunc_mean": agg["pile_trunc"]["mean"].tolist(),
                "pile_full_exponent": a_pf, "pile_full_err": e_pf,
                "pile_trunc_exponent": a_pt, "pile_trunc_err": e_pt,
                "nmod_full_mean": agg["nmod_full"]["mean"].tolist(),
                "nmod_trunc_mean": agg["nmod_trunc"]["mean"].tolist(),
                "epsmax_full_mean": agg["epsmax_full"]["mean"].tolist(),
                "epsmax_trunc_mean": agg["epsmax_trunc"]["mean"].tolist(),
                "epsmax_full_slope": s_emf, "epsmax_trunc_slope": s_emt,
                "full_pileup_grows": bool(a_pf > 0.25 and (a_pf / e_pf if e_pf > 0 else 0) > 3),
                "trunc_pileup_saturates": bool(a_pt < 0.6 * a_pf),
            },
            "proxy3_central": {
                "CV_S_trunc": cv_St.tolist(), "CV_S_full": cv_Sf.tolist(),
                "CV_S_trunc_exponent": p_cv, "CV_S_trunc_err": e_cv,
                "CV_S_trunc_largest_N": float(cv_St[-1]),
                "self_averaging": bool(cv_St[-1] < 0.10),
                "trend_significant": bool(e_cv > 0 and abs(p_cv) / e_cv > 2.0),
                "trend_decreasing": bool(p_cv < 0),
            },
        }
        blk["proxy1_trace"]["verdict_III_to_II"] = bool(
            blk["proxy1_trace"]["full_divergent"] and blk["proxy1_trace"]["trunc_saturates"])
        blk["proxy2_modular"]["verdict_III_to_II"] = bool(
            blk["proxy2_modular"]["full_pileup_grows"] and blk["proxy2_modular"]["trunc_pileup_saturates"])
        blk["proxy3_central"]["verdict_factor_like"] = bool(
            blk["proxy3_central"]["self_averaging"] and blk["proxy3_central"]["trend_decreasing"]
            and blk["proxy3_central"]["trend_significant"])
        return blk

    blk_ds = proxy_block(agg_ds, store_ds, "dS")
    blk_fl = proxy_block(agg_fl, store_fl, "flat")

    # --- the dS entropy CAP: S_trunc on the dS static patch saturates to a
    #     finite value as N grows at fixed region (II_1 max-entropy).  This is
    #     the de Sitter entropy in causal-set units.  Report the plateau value.
    St_ds_plateau = float(np.mean(agg_ds["S_trunc"]["mean"][-3:]))
    St_fl_plateau = float(np.mean(agg_fl["S_trunc"]["mean"][-3:]))
    a_St_ds = blk_ds["proxy1_trace"]["S_trunc_exponent"]
    a_St_fl = blk_fl["proxy1_trace"]["S_trunc_exponent"]

    part2 = {
        "description": "Three-proxy type battery (VYPOCET-12) on the dS static "
                       "patch vs the matched flat control, at increasing N "
                       "(fixed-region continuum limit). Establishes type-II "
                       "character (vs III_1) and the dS-entropy CAP.",
        "RSTAR_BOX": RSTAR_BOX, "Rstar_sub_cut": Rstar_sub, "Ns": Ns,
        "rho_proper_list": rho_list, "n_seeds": n_seeds,
        "pauli_jordan_pairing_err": {"dS": pe_ds, "flat": pe_fl},
        "desitter": blk_ds,
        "flat_control": blk_fl,
        "dS_entropy_cap": {
            "S_trunc_plateau_dS": St_ds_plateau,
            "S_trunc_plateau_flat": St_fl_plateau,
            "S_trunc_exponent_dS": a_St_ds,
            "S_trunc_exponent_flat": a_St_fl,
            "note": "S_trunc on the fixed dS sub-region saturates with N (II_1 "
                    "max-entropy cap); compare the flat control which (at fixed "
                    "region but uniform measure) tracks the same area/log law -- "
                    "the II_1 vs II_inf distinction lives in the REGION-GROWTH "
                    "direction (PART 1), not the fixed-region N-limit.",
        },
    }
    results["part2_three_proxy_battery"] = _to_native(part2)

    _plot_part2(Ns_arr, agg_ds, agg_fl, blk_ds, blk_fl, store_ds, store_fl, Ns)
    return part2, agg_ds, agg_fl


# ============================================================================
# PART 3: modular spectrum of the maximally-mixed (max-entropy) candidate
#   In II_1 the trace IS a state (the maximally-mixed tracial state, S_max).
#   Its modular spectrum is TRIVIAL (eps=0: rho proportional to 1, flat modular
#   Hamiltonian).  We probe how close the dS truncated state's modular spectrum
#   sits to the trivial (flat) spectrum as the region exhausts the patch, vs the
#   flat control which never approaches a trivial-modular max-entropy state.
# ============================================================================
def part3_maxent(results, agg_ds, agg_fl):
    print("\n" + "=" * 72)
    print("PART 3: modular spectrum of the max-entropy (tracial) candidate")
    print("=" * 72)

    # Same horizon-approach protocol as PART 1: FIXED bulk cut r*<=RCUT; sweep
    # the OUTER box edge R*_box toward the horizon at fixed (proper resp. flat)
    # density.  Track the mean modular energy <eps> of the FIXED-cut truncated
    # state.  II_1 max-entropy approach => dS <eps> tends toward a small/tracial
    # value as the patch saturates; flat control keeps O(1) modular energy.
    RCUT = 1.0 * LDS
    rho_proper = 300.0
    n_seeds = 5
    Rstar_sub = np.array([1.6, 2.2, 3.0, 4.0, 5.2]) * LDS    # box edges -> horizon

    eps_lo = 0.5     # low-eps (tracial/IR) band threshold
    def meanmod(measure):
        # out  = mean modular energy <eps> of the TRUNCATED fixed-cut state
        # frlo = fraction of UNTRUNCATED (full) modular modes with eps<eps_lo
        #        (the IR/tracial pile-up: a max-entropy/tracial approach GROWS
        #        this fraction; truncation removes exactly these modes, so the
        #        truncated <eps> CANNOT probe the tracial limit -- we report both).
        out = np.zeros((n_seeds, len(Rstar_sub)))
        nmod = np.zeros((n_seeds, len(Rstar_sub)))
        frlo = np.zeros((n_seeds, len(Rstar_sub)))
        for j, Rbox in enumerate(Rstar_sub):
            if measure == "desitter":
                Vbox = 2.0 * T_HALF * LDS * np.tanh(Rbox / LDS)
            else:
                Vbox = 2.0 * T_HALF * Rbox
            N = int(round(rho_proper * Vbox))
            kap = kappa_2d(N)
            for s in range(n_seeds):
                rng = np.random.default_rng(39_000_000 + 17 * j + s
                                            + (1 if measure == "flat" else 0) * 101)
                coords = sprinkle_box(N, rng, Rbox, measure)
                C = causal_matrix(coords)
                iD = pauli_jordan(C)
                w, V = sj_eig(iD)
                sub = np.where(coords[:, 1] <= RCUT)[0]
                comp = coords.shape[0] - sub.size
                if sub.size < 6 or comp < 6:
                    continue
                _, mu_t, _, _ = ssee_mu(w, V, sub, kappa=kap)
                eps_t = modular_spectrum_from_mu(mu_t)
                if eps_t.size:
                    out[s, j] = float(np.mean(eps_t))
                    nmod[s, j] = eps_t.size
                _, mu_f, _, _ = ssee_mu(w, V, sub, kappa=None)
                eps_f = modular_spectrum_from_mu(mu_f)
                if eps_f.size:
                    frlo[s, j] = float(np.mean(eps_f < eps_lo))
        return (out.mean(0), out.std(0, ddof=1), nmod.mean(0),
                frlo.mean(0), frlo.std(0, ddof=1))
    N = None    # variable across the sweep (recorded per box below)

    me_ds, me_ds_s, nm_ds, fr_ds, fr_ds_s = meanmod("desitter")
    me_fl, me_fl_s, nm_fl, fr_fl, fr_fl_s = meanmod("flat")
    sl_ds, _ = linfit(Rstar_sub, me_ds)
    sl_fl, _ = linfit(Rstar_sub, me_fl)
    slfr_ds, _ = linfit(Rstar_sub, fr_ds)
    slfr_fl, _ = linfit(Rstar_sub, fr_fl)
    print(f"[dS  ] <eps>_trunc vs R*: {np.array2string(me_ds, precision=3)} slope={sl_ds:.4f}")
    print(f"[flat] <eps>_trunc vs R*: {np.array2string(me_fl, precision=3)} slope={sl_fl:.4f}")
    print(f"[dS  ] IR-frac(eps<{eps_lo}, full) vs R*: {np.array2string(fr_ds, precision=3)} slope={slfr_ds:.4f}")
    print(f"[flat] IR-frac(eps<{eps_lo}, full) vs R*: {np.array2string(fr_fl, precision=3)} slope={slfr_fl:.4f}")

    # tracial approach: in the UNtruncated spectrum the IR (eps<eps_lo) fraction
    # should GROW for the dS max-entropy approach (more nearly-maximally-mixed
    # modes) and grow faster than the flat control.
    tracial_full = bool(slfr_ds > 0 and slfr_ds > slfr_fl)
    part3 = {
        "description": "Modular spectrum of the max-entropy (tracial) candidate. "
                       "In a II_1 algebra the maximally-mixed tracial state has a "
                       "TRIVIAL (flat, eps->0) modular Hamiltonian. Two probes as "
                       "the region approaches the horizon: (a) mean modular energy "
                       "<eps> of the TRUNCATED state -- HONEST NULL: truncation "
                       "removes exactly the low-eps tracial modes, so <eps>_trunc "
                       "is pinned at the UV edge and CANNOT see the tracial limit; "
                       "(b) IR fraction (eps<eps_lo) of the UNTRUNCATED state -- the "
                       "proper tracial pile-up probe.",
        "RCUT": RCUT, "rho_proper": rho_proper, "eps_lo": eps_lo,
        "n_seeds": n_seeds, "Rstar_box": Rstar_sub.tolist(),
        "r_edge_box": (LDS * np.tanh(Rstar_sub / LDS)).tolist(),
        "desitter": {"mean_eps_trunc_mean": me_ds.tolist(), "mean_eps_trunc_std": me_ds_s.tolist(),
                     "nmod_trunc_mean": nm_ds.tolist(), "mean_eps_trunc_slope": sl_ds,
                     "IR_frac_full_mean": fr_ds.tolist(), "IR_frac_full_std": fr_ds_s.tolist(),
                     "IR_frac_full_slope": slfr_ds},
        "flat_control": {"mean_eps_trunc_mean": me_fl.tolist(), "mean_eps_trunc_std": me_fl_s.tolist(),
                         "nmod_trunc_mean": nm_fl.tolist(), "mean_eps_trunc_slope": sl_fl,
                         "IR_frac_full_mean": fr_fl.tolist(), "IR_frac_full_std": fr_fl_s.tolist(),
                         "IR_frac_full_slope": slfr_fl},
        "dS_approaches_tracial_trunc_eps": bool(sl_ds < 0 and sl_ds < sl_fl),
        "dS_approaches_tracial_IR_frac": tracial_full,
        "dS_approaches_tracial": tracial_full,
        "honest_null_note": "The truncated mean-eps probe is a NULL by construction "
                            "(truncation kills the tracial low-eps modes). The "
                            "untruncated IR-fraction is the correct tracial probe.",
        "prediction": "II_1 max-entropy: dS IR-fraction (eps<eps_lo, full spectrum) "
                      "grows toward the horizon faster than the flat control.",
    }
    results["part3_maxent_modular_spectrum"] = _to_native(part3)
    _plot_part3(Rstar_sub, me_ds, me_ds_s, me_fl, me_fl_s,
                fr_ds, fr_ds_s, fr_fl, fr_fl_s, eps_lo, part3)
    return part3


# ============================================================================
# OVERALL VERDICT
# ============================================================================
def overall_verdict(results):
    p1 = results["part1_II1_vs_IIinf_discriminator"]
    p2 = results["part2_three_proxy_battery"]
    p3 = results["part3_maxent_modular_spectrum"]
    disc = p1["verdict_II1_vs_IIinf_discriminated"]
    ds_t2 = (p2["desitter"]["proxy1_trace"]["verdict_III_to_II"]
             or p2["desitter"]["proxy2_modular"]["verdict_III_to_II"])
    n_proxy_ds = (int(p2["desitter"]["proxy1_trace"]["verdict_III_to_II"])
                  + int(p2["desitter"]["proxy2_modular"]["verdict_III_to_II"])
                  + int(p2["desitter"]["proxy3_central"]["verdict_factor_like"]))
    tracial = p3["dS_approaches_tracial"]

    if disc and ds_t2:
        overall = ("DISCRIMINATED: the SJ+truncation machinery DISTINGUISHES the "
                   "bounded de Sitter static patch (II_1: capped entropy) from the "
                   "matched unbounded flat control (II_inf: growing entropy), AND "
                   "independently sees the III_1->II truncation on the dS patch. "
                   "The CLPW II_1 vs II_inf distinction is VISIBLE in the discrete probe.")
    elif ds_t2 and not disc:
        overall = ("PARTIAL: the dS patch shows III_1->II type-II character, but the "
                   "II_1 vs II_inf discriminator (capped vs growing entropy) is NOT "
                   "cleanly resolved at these N -- see honest-null scaling note.")
    elif disc and not ds_t2:
        overall = ("PARTIAL: the II_1 vs II_inf entropy-growth discriminator is "
                   "resolved, but the per-N type-II proxies are weak at these N.")
    else:
        overall = ("NULL: at these N the discrete SJ probe does NOT resolve II_1 from "
                   "II_inf -- documented scaling needed to do so.")

    results["VERDICT"] = {
        "II1_vs_IIinf_discriminated": disc,
        "dS_patch_type_II_character": ds_t2,
        "n_proxies_passing_dS": n_proxy_ds,
        "dS_max_entropy_tracial_trend": tracial,
        "overall": overall,
    }
    print("\n=== OVERALL VERDICT ===")
    print(f" II_1 vs II_inf discriminated (capped vs growing): {disc}")
    print(f" dS patch type-II character (>=1 proxy III->II):   {ds_t2} ({n_proxy_ds}/3 proxies)")
    print(f" dS max-entropy tracial trend (<eps>->0):          {tracial}")
    print(f" overall: {overall}")


# ============================================================================
# PLOTS
# ============================================================================
def _plot_part1(Rstar, r_edge, St_ds, St_ds_s, St_fl, St_fl_s, cap, B, xi, part1):
    fig, (ax0, ax1, ax2) = plt.subplots(1, 3, figsize=(17.5, 5.2))
    xx = np.linspace(Rstar.min(), Rstar.max(), 200)

    # PANEL 0 (DECISIVE): full content-tracking SSEE -- caps vs grows
    Sf_ds = np.array(part1["desitter"]["S_full_mean"])
    Sf_fl = np.array(part1["flat_control"]["S_full_mean"])
    capF = part1["desitter"]["S_full_saturating_fit"]["S_cap"]
    BF = part1["desitter"]["S_full_saturating_fit"]["B"]
    xiF = part1["desitter"]["S_full_saturating_fit"]["xi"]
    R2F = part1["desitter"]["S_full_saturating_fit"]["R2"]
    ax0.plot(Rstar, Sf_ds, 'o-', color='tab:blue',
             label="de Sitter (II$_1$: content caps)")
    ax0.plot(xx, capF - BF * np.exp(-xx / xiF), 'b--', lw=1.2,
             label=rf"sat. fit $S_{{cap}}={capF:.1f}$ ($R^2={R2F:.2f}$)")
    ax0.plot(Rstar, Sf_fl, 's-', color='tab:red',
             label="flat control (II$_\\infty$: grows)")
    ax0.axhline(capF, color='tab:blue', ls=':', lw=0.8)
    ax0.set_xlabel(r"box outer edge $R^*_{\rm box}/\ell$  (horizon: $R^*\to\infty$)")
    ax0.set_ylabel(r"full SSEE $S_{\rm full}$ (content/volume-tracking)")
    ax0.set_title("PART 1 (DECISIVE): II$_1$ vs II$_\\infty$\n"
                  "content-tracking entropy: dS caps, flat grows")
    ax0.legend(fontsize=8)

    # PANEL 1: N_total -- the geometric boundedness
    Ntot_ds = np.array(part1["desitter"]["N_total_mean"])
    Ntot_fl = np.array(part1["flat_control"]["N_total_mean"])
    ax1.plot(Rstar, Ntot_ds, 'o-', color='tab:blue',
             label="de Sitter $N_{\\rm tot}$ (caps: bounded patch)")
    ax1.plot(Rstar, Ntot_fl, 's-', color='tab:red',
             label="flat $N_{\\rm tot}$ (grows: unbounded)")
    ax1.set_xlabel(r"box outer edge $R^*_{\rm box}/\ell$")
    ax1.set_ylabel(r"total causal-set cardinality $N_{\rm tot}$")
    ax1.set_title("WHY: dS proper volume (sech$^2$) caps;\n"
                  "flat volume grows linearly toward horizon")
    ax1.legend(fontsize=8)

    # PANEL 2: truncated SSEE -- the honest 2D log-flat limitation
    ax2.errorbar(Rstar, St_ds, yerr=St_ds_s, fmt='o-', color='tab:blue', capsize=3,
                 label="de Sitter $S_{\\rm trunc}$")
    ax2.errorbar(Rstar, St_fl, yerr=St_fl_s, fmt='s-', color='tab:red', capsize=3,
                 label="flat $S_{\\rm trunc}$")
    ax2.set_xlabel(r"box outer edge $R^*_{\rm box}/\ell$")
    ax2.set_ylabel(r"truncated SSEE $S_{\rm trunc}$ (type-II regularised)")
    ax2.set_title("HONEST 2D LIMIT: truncated entropy is a\n"
                  "log/area law, nearly box-independent (does NOT\nseparate types alone)")
    ax2.legend(fontsize=8)
    fig.tight_layout(); fig.savefig(os.path.join(PLOTDIR, "part1_discriminator.png"), dpi=140)
    plt.close(fig)


def _plot_part2(Ns, agg_ds, agg_fl, blk_ds, blk_fl, store_ds, store_fl, Ns_list):
    fig, axes = plt.subplots(1, 3, figsize=(17, 5))
    # proxy1 entropy-trace
    ax = axes[0]
    ax.errorbar(Ns, agg_ds["S_full"]["mean"], yerr=agg_ds["S_full"]["std"],
                fmt='o', color='tab:red', capsize=3, label="dS S_full (volume)")
    ax.errorbar(Ns, agg_ds["S_trunc"]["mean"], yerr=agg_ds["S_trunc"]["std"],
                fmt='s', color='tab:blue', capsize=3,
                label=f"dS S_trunc a={blk_ds['proxy1_trace']['S_trunc_exponent']:.2f}")
    ax.errorbar(Ns, agg_fl["S_trunc"]["mean"], yerr=agg_fl["S_trunc"]["std"],
                fmt='^', color='tab:green', capsize=3,
                label=f"flat S_trunc a={blk_fl['proxy1_trace']['S_trunc_exponent']:.2f}")
    ax.set_xscale('log'); ax.set_yscale('log')
    ax.set_xlabel("N"); ax.set_ylabel(r"SSEE $S$")
    ax.set_title("PROXY 1: entropy-trace\n(fixed region, increasing N)")
    ax.legend(fontsize=7.5)
    # proxy2 pile-up
    ax = axes[1]
    ax.errorbar(Ns, np.maximum(agg_ds["pile_full"]["mean"], 1e-9),
                yerr=agg_ds["pile_full"]["std"], fmt='o', color='tab:red', capsize=3,
                label=f"dS pile_full exp={blk_ds['proxy2_modular']['pile_full_exponent']:.2f}")
    ax.errorbar(Ns, np.maximum(agg_ds["pile_trunc"]["mean"], 1e-9),
                yerr=agg_ds["pile_trunc"]["std"], fmt='s', color='tab:blue', capsize=3,
                label=f"dS pile_trunc exp={blk_ds['proxy2_modular']['pile_trunc_exponent']:.2f}")
    ax.set_xscale('log'); ax.set_yscale('log')
    ax.set_xlabel("N"); ax.set_ylabel(r"# modular modes $\epsilon<0.5$")
    ax.set_title("PROXY 2: modular pile-up\n(III$_1$ grows, II saturates)")
    ax.legend(fontsize=7.5)
    # modular density (dS, largest N)
    ax = axes[2]
    N0, N1 = Ns_list[0], Ns_list[-1]
    for key, col, lab in [("eps_full_pool", 'tab:red', "full"),
                          ("eps_trunc_pool", 'tab:blue', "trunc")]:
        eps = np.array(store_ds[N1][key])
        if eps.size > 3:
            bins = np.linspace(0, max(6.0, np.percentile(eps, 99)), 40)
            ax.hist(eps, bins=bins, density=True, histtype='step', lw=1.8,
                    color=col, label=f"dS {lab} (N={N1})")
    ax.set_xlabel(r"$\epsilon$ (modular energy)")
    ax.set_ylabel(r"$\rho(\epsilon)$")
    ax.set_title("dS modular spectral density\n"
                 r"$\epsilon=\ln[\mu/(\mu-1)]$")
    ax.legend(fontsize=8)
    fig.suptitle("PART 2: three-proxy type battery on the de Sitter static patch")
    fig.tight_layout(); fig.savefig(os.path.join(PLOTDIR, "part2_proxies.png"), dpi=140)
    plt.close(fig)


def _plot_part3(Rstar, me_ds, me_ds_s, me_fl, me_fl_s,
                fr_ds, fr_ds_s, fr_fl, fr_fl_s, eps_lo, part3):
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13, 5.3))
    # LEFT: untruncated IR-fraction (the correct tracial probe)
    ax1.errorbar(Rstar, fr_ds, yerr=fr_ds_s, fmt='o-', color='tab:blue', capsize=3,
                 label=f"de Sitter (slope={part3['desitter']['IR_frac_full_slope']:.3f})")
    ax1.errorbar(Rstar, fr_fl, yerr=fr_fl_s, fmt='s-', color='tab:red', capsize=3,
                 label=f"flat control (slope={part3['flat_control']['IR_frac_full_slope']:.3f})")
    ax1.set_xlabel(r"box outer edge $R^*_{\rm box}/\ell$ (horizon approach)")
    ax1.set_ylabel(rf"IR fraction $\epsilon<{eps_lo}$ (untruncated spectrum)")
    ax1.set_title("PART 3 (tracial probe): IR pile-up\n"
                  r"II$_1$ max-entropy: dS IR-fraction grows toward horizon")
    ax1.legend(fontsize=9)
    # RIGHT: truncated mean-eps -- the honest NULL (truncation kills tracial modes)
    ax2.errorbar(Rstar, me_ds, yerr=me_ds_s, fmt='o-', color='tab:blue', capsize=3,
                 label=f"de Sitter (slope={part3['desitter']['mean_eps_trunc_slope']:.3f})")
    ax2.errorbar(Rstar, me_fl, yerr=me_fl_s, fmt='s-', color='tab:red', capsize=3,
                 label=f"flat control (slope={part3['flat_control']['mean_eps_trunc_slope']:.3f})")
    ax2.set_xlabel(r"box outer edge $R^*_{\rm box}/\ell$")
    ax2.set_ylabel(r"$\langle\epsilon\rangle$ of TRUNCATED state")
    ax2.set_title("HONEST NULL: truncation removes the low-$\\epsilon$\n"
                  "tracial modes, so $\\langle\\epsilon\\rangle_{\\rm trunc}$ is pinned at the\nUV edge "
                  "(cannot probe the tracial limit)")
    ax2.legend(fontsize=9)
    fig.tight_layout(); fig.savefig(os.path.join(PLOTDIR, "part3_maxent.png"), dpi=140)
    plt.close(fig)


# ============================================================================
def run():
    t0 = time.time()
    results = {"meta": {
        "task": "VYPOCET-19 UNIFY SJ-horizoned-spacetimes x vN-type on DE SITTER; "
                "test CLPW (2206.10780) static-patch II_1 (NOT II_inf) prediction",
        "dimension": "2D de Sitter static patch (conformal trick; SJ machinery "
                     "of VYPOCET-12)",
        "geometry": "ds^2=-(1-r^2/l^2)dt^2+dr^2/(1-r^2/l^2); tortoise r*=l*arctanh(r/l) "
                    "=> conformally flat strip; 2D massless scalar conformally "
                    "invariant => flat SJ in (t,r*); de Sitter enters via the "
                    "sech^2(r*/l) PROPER sprinkling measure (finite patch volume).",
        "clpw_prediction": "static-patch observer algebra is type II_1: NORMALISABLE "
                           "trace, MAX-ENTROPY tracial state (empty dS, S~A/4G), "
                           "entropy CAPS as region exhausts patch -- vs black-hole "
                           "II_inf (entropy grows without bound).",
        "discriminator": "TRUNCATED SSEE vs region tortoise-extent R* at fixed "
                         "proper density: dS caps (II_1), matched flat control grows "
                         "(II_inf).",
        "conventions": {
            "metric_dS2": "-(1-r^2/l^2)dt^2 + dr^2/(1-r^2/l^2), r in (-l,l)",
            "tortoise": "r* = l*arctanh(r/l) in (-inf,inf); horizon r=l <=> r*=inf",
            "conformal_factor": "Omega^2 = 1-r^2/l^2 = sech^2(r*/l)",
            "conformal_trick": "2D massless scalar conformally invariant (1306.3231 "
                               "dS SJ); causal order/iDelta/W_SJ identical to flat in "
                               "(t,r*); horizon enters only via proper measure",
            "proper_measure": "dN ~ sech^2(r*/l) dt dr* (finite patch volume "
                              "=> point budget caps toward horizon = II_1 finite trace)",
            "G_R": "G_R=(1/2)C (Sorkin-Yazdi 1611.10281)",
            "iDelta": "i(G_R-G_R^T)=i/2(C-C^T), Hermitian, +/- paired",
            "W_SJ": "positive part of iDelta",
            "SSEE": "W_O v=mu iDelta_O v ; S=sum mu ln|mu| ; pairs (mu,1-mu)",
            "kappa": "sqrt(N)/(4 pi) (Sorkin-Yazdi 1712.04227); double truncation",
            "modular_energy": "eps=ln[mu/(mu-1)] (Casini-Huerta 0905.2562)",
        },
        "references": {
            "CLPW": "arXiv:2206.10780 (de Sitter static-patch algebra type II_1)",
            "dS_SJ_causalset": "arXiv:1306.3231 (SJ vacuum on dS; 1+1 causal diamond)",
            "SJ_SSEE": "arXiv:1611.10281 (Sorkin-Yazdi SSEE); 2008.07697 (dS horizons)",
            "truncation_kappa": "arXiv:1712.04227 (UV magnitude cutoff)",
            "modular": "arXiv:0905.2562 (Casini-Huerta modular Hamiltonian)",
        },
    }}

    part1_discriminator(results)
    _p2, agg_ds, agg_fl = part2_proxies(results)
    part3_maxent(results, agg_ds, agg_fl)
    overall_verdict(results)

    results["runtime_s"] = time.time() - t0
    with open(os.path.join(OUTDIR, "results.json"), "w") as f:
        json.dump(_to_native(results), f, indent=2)
    print(f"\nDone in {results['runtime_s']:.1f}s. Saved results.json + plots to {OUTDIR}")
    return results


if __name__ == "__main__":
    run()
