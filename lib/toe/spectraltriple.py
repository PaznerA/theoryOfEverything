# -*- coding: utf-8 -*-
"""toe.spectraltriple -- finite spectral-triple primitives over a causal set:
a candidate Dirac operator built from a one-particle modular kernel, and the
Connes spectral distance.

This is a Layer-C composable module (it consumes the modular kernel produced by
:func:`toe.entropy.modular_kernel`). It is numpy/scipy only -- NOT the
exact-rational :mod:`toe.ncg` spectral-action module -- and holds no global
state, does no file I/O and no plotting.

The two units are:

  * :func:`dirac_from_kernel` -- the candidate Dirac operator
    ``D_K = sgn(K) sqrt(|K|)`` of a Hermitian one-particle modular kernel ``K``
    (the SJ / Bisognano-Wichmann modular Hamiltonian of a sub-region). Squaring
    recovers ``D_K^2 = |K|``, so ``D_K`` has the same eigenVECTORS as ``K`` and
    the spectral pair ``(spec K, spec D_K)`` is the symmetric-functional-calculus
    image; this is the "modular Dirac" candidate of the H5g-4 proof-of-concept.

  * :func:`connes_distance` -- the Connes spectral distance
    ``d_D(x, y) = sup { |a(x) - a(y)| : || [D, a] ||_op <= 1 }`` for a finite
    spectral triple, where the algebra is the COMMUTATIVE algebra of real
    diagonal functions ``a`` on the point set. ``[D, a]_{ij} = D_{ij}(a_j - a_i)``,
    and the operator norm is the largest singular value. The sup is a convex
    optimisation (linear objective, convex spectral-norm constraint) solved here
    by a projected supremum search.

Conventions / sources:
  Connes 'Noncommutative Geometry' (Academic Press, 1994) -- the spectral
  distance d(x,y) = sup{|a(x)-a(y)| : ||[D,a]|| <= 1} ("metric from the Dirac
  operator"); Connes-Rovelli gr-qc/9406019 ground the modular-flow-as-time
  (thermal time / Tomita-Takesaki) framing. The modular Dirac candidate is the
  functional-calculus square root of the one-particle modular Hamiltonian
  (Casini-Huerta 0905.2562 single-mode modular energies, Sorkin-Yazdi
  1611.10281 SJ state). Bisognano-Wichmann modular flow = boost (1712.04227,
  2008.07697 context).
  NOTE: gr-qc/9406019 is Connes-Rovelli "Von Neumann Algebra Automorphisms and
  Time-Thermodynamics Relation" -- it motivates modular flow as time, it is NOT
  the source of the spectral-distance formula (that is the 1994 book).
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Optional

import numpy as np

__all__ = [
    "dirac_from_kernel",
    "connes_commutator_norm",
    "connes_distance",
    "ConnesDistance",
    "kms_temperature",
    "KMSFit",
    "unruh_proper_law",
    "UnruhLawFit",
    "geometric_boost_dirac",
    "GeometricBoostDirac",
]


# ===========================================================================
# CANDIDATE DIRAC OPERATOR FROM A ONE-PARTICLE MODULAR KERNEL
# ===========================================================================

def dirac_from_kernel(K, *, hermitize=True):
    """Candidate Dirac operator ``D_K = sgn(K) sqrt(|K|)`` of a Hermitian
    one-particle modular kernel ``K``.

    Diagonalises the Hermitian ``K = U diag(lam) U^dagger`` and applies the
    symmetric functional calculus ``f(lam) = sign(lam) sqrt(|lam|)`` mode by
    mode, so ``D_K = U diag(f(lam)) U^dagger`` shares the eigenvectors of ``K``
    and satisfies ``D_K^2 = |K|`` (a positive operator) while ``D_K`` keeps the
    sign structure of the modular spectrum. This is the finite-spectral-triple
    Dirac candidate of the H5g-4 modular-flow proof of concept: ``K`` is the
    SJ/Bisognano-Wichmann one-particle modular Hamiltonian of a sub-region
    (from :func:`toe.entropy.modular_kernel`), and ``D_K`` is its
    square-root-modulus, the natural "modular Dirac" whose spectrum is the
    signed square root of the modular spectrum.

    Formula: modular-flow-def, modular-spectrum, spectral-action-formula.
    Evidence: H5g-4 (core-data/calculations/spectral-triple-modular/calc.py);
    modular kernel from :func:`toe.entropy.modular_kernel` (VYPOCET-18/20/22).
    Conventions: Connes 'Noncommutative Geometry' (1994, Dirac operator as
    metric data); Connes-Rovelli gr-qc/9406019 (modular flow as thermal time);
    Casini-Huerta 0905.2562 single-mode modular energies eps = ln[mu/(mu-1)];
    Sorkin-Yazdi 1611.10281 SJ modular flow. ``D_K = sgn(K) sqrt(|K|)`` via the
    symmetric functional calculus (so ``D_K^2 = |K|``, ``D_K`` Hermitian).

    Args:
        K: (n, n) Hermitian one-particle modular kernel (e.g.
            ``toe.entropy.modular_kernel(...).K``).
        hermitize: if True (default) symmetrise the input as
            ``(K + K^dagger)/2`` before diagonalising (guards against
            accumulated asymmetry from the upstream eigensolve).

    Returns:
        np.ndarray (n, n) complex Hermitian -- the candidate Dirac operator
        ``D_K``. Its eigenvalues are ``sign(lam) sqrt(|lam|)`` of the eigenvalues
        ``lam`` of ``K``.
    """
    K = np.asarray(K)
    if hermitize:
        K = 0.5 * (K + K.conj().T)
    lam, U = np.linalg.eigh(K)
    f = np.sign(lam) * np.sqrt(np.abs(lam))
    D = (U * f) @ U.conj().T
    return 0.5 * (D + D.conj().T)


# ===========================================================================
# CONNES SPECTRAL DISTANCE  d_D(x, y) = sup{ |a(x)-a(y)| : ||[D,a]||_op <= 1 }
# ===========================================================================

def connes_commutator_norm(D, a):
    """Operator norm (largest singular value) of the commutator ``[D, a]`` for a
    real diagonal function ``a`` on the point set.

    With ``a`` acting as the diagonal multiplication operator
    ``diag(a_0, ..., a_{n-1})`` the commutator has entries
    ``[D, a]_{ij} = D_{ij} (a_j - a_i)`` (the diagonal vanishes), and its norm
    is the largest singular value. This is the constraint functional of the
    Connes distance.

    Formula: spectral-action-formula.
    Evidence: H5g-4 (core-data/calculations/spectral-triple-modular/calc.py).
    Conventions: Connes 'Noncommutative Geometry' (1994) -- ``[D, a]`` is the
    discrete "gradient" of the function ``a``; its operator-norm bound is the
    Lipschitz constraint of the spectral distance.

    Args:
        D: (n, n) Hermitian Dirac operator.
        a: (n,) real diagonal function on the points.

    Returns:
        float -- the largest singular value of ``[D, a]``.
    """
    D = np.asarray(D)
    a = np.asarray(a, dtype=np.float64)
    comm = D * (a[None, :] - a[:, None])
    if comm.size == 0:
        return 0.0
    return float(np.linalg.norm(comm, ord=2))


@dataclass
class ConnesDistance:
    """Carrier for a Connes spectral-distance evaluation between two points.

    ``value`` is ``d_D(x, y)``; ``a`` is the optimal (Lipschitz-unit) function
    achieving it; ``commutator_norm`` is ``||[D, a]||_op`` of that optimiser
    (``<= 1`` up to the solver tolerance); ``i, j`` are the point indices;
    ``n_iter`` is the number of refinement steps used.
    """

    value: float
    a: np.ndarray
    commutator_norm: float
    i: int
    j: int
    n_iter: int = 0


def connes_distance(D, i, j, *, n_iter=60, seed=0, n_random=24,
                    return_carrier=False):
    """Connes spectral distance
    ``d_D(x_i, x_j) = sup { |a_i - a_j| : || [D, a] ||_op <= 1 }`` for a finite
    spectral triple over a point set.

    The algebra is the COMMUTATIVE algebra of real diagonal functions ``a`` on
    the ``n`` points; the Dirac operator ``D`` supplies the metric. The
    objective ``a_i - a_j`` is linear and the constraint
    ``|| [D, a] ||_op = sigma_max( D * (a_j - a_i) ) <= 1`` is convex (a spectral
    norm of a linear map of ``a``), so the supremum is attained on the unit
    ball. Because ``[D, a]`` is invariant under a constant shift of ``a`` and
    homogeneous of degree 1, the distance is the reciprocal of the smallest
    achievable commutator norm per unit of ``a_i - a_j``:

        ``d_D(i, j) = max_a (a_i - a_j) / || [D, a] ||_op``    (a not constant).

    This routine maximises that scale-invariant Rayleigh-like quotient by a
    direction search: it seeds candidate directions (the ``i``/``j`` indicator,
    its ``D``-smoothings, and random directions), then refines each by a
    projected-gradient ascent on ``g(a) = (a_i - a_j) / ||[D, a]||_op`` and keeps
    the best. The quotient is invariant to scaling so the returned optimiser is
    normalised to unit commutator norm. This is an honest numerical SUP (a lower
    bound that converges from below); the convexity guarantees no spurious local
    maxima trap it away from the true value when enough seeds are used.

    COST: each evaluation of ``g`` and its gradient does one ``n x n`` SVD
    (``O(n^3)``); with ``n_iter`` refinement steps and ``n_random + few`` seeds
    the per-pair cost is ``~(n_random) * n_iter`` SVDs, so keep ``n`` modest
    (<= ~300) for the per-pair budget.

    Formula: spectral-action-formula, modular-flow-def.
    Evidence: H5g-4 (core-data/calculations/spectral-triple-modular/calc.py).
    Conventions: Connes 'Noncommutative Geometry' (Academic Press, 1994) --
    ``d(x, y) = sup{ |a(x) - a(y)| : ||[D, a]|| <= 1 }``; the commutative
    diagonal algebra recovers the geodesic distance for the canonical Dirac
    operator on a manifold. (gr-qc/9406019 = Connes-Rovelli thermal-time, the
    modular-flow-as-time motivation, NOT the distance formula.)

    Args:
        D: (n, n) Hermitian Dirac operator.
        i: index of the first point.
        j: index of the second point.
        n_iter: refinement steps per seed direction (projected ascent).
        seed: RNG seed (REQUIRED for reproducibility) for the random seed
            directions.
        n_random: number of random seed directions in addition to the
            structured ones.
        return_carrier: if True, return a :class:`ConnesDistance`; otherwise the
            scalar distance.

    Returns:
        float distance (default) or :class:`ConnesDistance` if
        ``return_carrier`` is True.
    """
    D = np.asarray(D)
    n = D.shape[0]
    i = int(i)
    j = int(j)
    rng = np.random.default_rng(seed)

    e = np.zeros(n)
    e[i] = 1.0
    e[j] = -1.0

    def commnorm(a):
        comm = D * (a[None, :] - a[:, None])
        return float(np.linalg.norm(comm, ord=2))

    def quotient(a):
        a = a - a.mean()
        num = a[i] - a[j]
        if num <= 0:
            return -np.inf, a, np.inf
        cn = commnorm(a)
        if cn <= 1e-14:
            return -np.inf, a, np.inf
        return num / cn, a, cn

    # ---- seed directions --------------------------------------------------
    Dabs = np.abs(np.asarray(D))
    seeds = [e.copy()]
    # D-smoothings of the indicator (spread the +/- charge along the operator's
    # support -- these are good ascent starts on a local Dirac).
    s = e.copy()
    for _ in range(3):
        s = Dabs @ s
        s = e + 0.5 * (s / (np.max(np.abs(s)) + 1e-30))
        seeds.append(s.copy())
    # coordinate ramp seeds are not available without coords; use random.
    for _ in range(int(n_random)):
        seeds.append(e + 0.3 * rng.standard_normal(n))

    best_val = -np.inf
    best_a = e.copy()
    best_cn = np.inf

    for a0 in seeds:
        a = a0 - a0.mean()
        val, a, cn = quotient(a)
        # projected-gradient-style ascent on the scale-invariant quotient.
        step = 0.5
        for _ in range(int(n_iter)):
            # finite-difference ascent in a small random subspace + the e
            # direction (cheap, robust; the objective is concave on the cone).
            g = np.zeros(n)
            base, _, base_cn = quotient(a)
            if not np.isfinite(base):
                break
            # gradient estimate along e and a few random probes
            probes = [e] + [rng.standard_normal(n) for _ in range(4)]
            for p in probes:
                p = p - p.mean()
                nrm = np.linalg.norm(p)
                if nrm < 1e-30:
                    continue
                p = p / nrm
                h = 1e-3
                vp, _, _ = quotient(a + h * p)
                if np.isfinite(vp):
                    g += ((vp - base) / h) * p
            gnorm = np.linalg.norm(g)
            if gnorm < 1e-12:
                break
            g = g / gnorm
            improved = False
            for _ in range(8):
                trial = a + step * g
                vt, ta, _ = quotient(trial)
                if vt > base:
                    a = ta
                    improved = True
                    break
                step *= 0.5
            if not improved:
                step *= 0.5
                if step < 1e-6:
                    break
        val, a, cn = quotient(a)
        if val > best_val:
            best_val = val
            best_a = a.copy()
            best_cn = cn

    # normalise optimiser to unit commutator norm
    if np.isfinite(best_cn) and best_cn > 0:
        best_a = best_a / best_cn
        best_cn_norm = commnorm(best_a)
    else:
        best_cn_norm = float("nan")
    dist = float(best_val) if np.isfinite(best_val) else float("nan")

    if return_carrier:
        return ConnesDistance(value=dist, a=best_a, commutator_norm=best_cn_norm,
                              i=i, j=j, n_iter=int(n_iter))
    return dist


# ===========================================================================
# KMS INVERSE-TEMPERATURE of a one-particle modular flow
# ===========================================================================

@dataclass
class KMSFit:
    """Carrier for a KMS (thermal-time) fit of a one-particle modular flow.

    ``beta`` is the imaginary-modular-time period minimising the KMS residual of
    the modular two-point function; ``resid_beta1`` is the KMS residual evaluated
    at ``beta = 1`` (the Tomita-Takesaki / Casini-Huerta value, machine precision
    for a genuine SJ modular flow); ``resid_min`` is the residual at the best
    ``beta``. ``ts`` is the real-modular-time grid and ``g_re`` / ``g_im`` the
    real / imaginary parts of the modular two-point ``G(t)`` on that grid (for
    plotting). ``n_modes`` is the number of modular modes used.
    """

    beta: float
    resid_beta1: float
    resid_min: float
    ts: list
    g_re: list
    g_im: list
    n_modes: int = 0


def kms_temperature(eps, occ, *, n_t=9, t_span=2.0, betas=None):
    """KMS inverse-temperature ``beta`` of a one-particle modular flow from its
    modular energies ``eps`` and occupations ``occ``.

    For a one-particle modular flow ``sigma_t = e^{iKt}`` with mode modular
    energies ``eps_k`` and occupations ``n_k``, the (real-field) modular two-point
    function is

        ``G(t) = sum_k [ (n_k + 1) e^{-i eps_k t} + n_k e^{+i eps_k t} ]``,

    and the Kubo-Martin-Schwinger condition at inverse-temperature ``beta`` is the
    analyticity / periodicity ``G(t) = G(-t - i*beta)``. The analytic continuation
    ``t -> -t - i*beta`` reweights the two branches by ``e^{-/+ beta eps_k}``, so
    the scale-invariant residual

        ``R(beta) = || G(t) - G_cont(-t - i*beta) || / || G(t) ||``

    over a real-time grid has a single sharp minimum at the KMS inverse-
    temperature. For a SORKIN-JOHNSTON modular flow the SSEE eigenvalues give
    ``eps_k = ln[mu_k/(mu_k-1)]`` and ``n_k = mu_k - 1`` with ``n_k/(n_k+1) =
    e^{-eps_k}`` exactly, so ``beta = 1`` to machine precision (KMS at beta=1 in
    modular-energy units, the Tomita-Takesaki/Casini-Huerta value); the Unruh
    ``2*pi`` is the conversion to boost-rapidity time, NOT recoverable from the
    spectrum alone.

    Formula: modular-flow-def, modular-spectrum.
    Evidence: H6g-1 (core-data/calculations/modular-kms-thermal/calc.py).
    Conventions: Casini-Huerta 0905.2562 single-mode ``eps = ln[mu/(mu-1)]``,
    occupation ``n = mu - 1``; KMS condition (Kubo-Martin-Schwinger / Tomita-
    Takesaki). Modular flow as thermal time: Connes-Rovelli gr-qc/9406019.
    Bisognano-Wichmann boost / Unruh ``1/2pi`` (1712.04227).

    Args:
        eps: 1-D array of modular energies ``eps_k > 0`` (e.g.
            ``ln[mu_k/(mu_k-1)]``), PAIRED with ``occ`` mode by mode.
        occ: 1-D array of occupations ``n_k >= 0`` (e.g. ``mu_k - 1``).
        n_t: number of real-modular-time samples for the residual (odd, centred).
        t_span: half-width of the real-modular-time grid ``[-t_span, t_span]``.
        betas: optional 1-D grid of candidate ``beta`` (default a fine grid on
            ``[0.2, 2.0]`` around the SJ value 1).

    Returns:
        :class:`KMSFit` with ``beta``, ``resid_beta1``, ``resid_min``, the
        time grid ``ts`` and the two-point ``g_re`` / ``g_im``.
    """
    eps = np.asarray(eps, dtype=float)
    occ = np.asarray(occ, dtype=float)
    m = np.isfinite(eps) & np.isfinite(occ) & (eps > 0.0) & (occ >= 0.0)
    eps = eps[m]
    occ = occ[m]
    if eps.size < 2:
        return KMSFit(beta=float("nan"), resid_beta1=float("nan"),
                      resid_min=float("nan"), ts=[], g_re=[], g_im=[],
                      n_modes=int(eps.size))
    ts = np.linspace(-float(t_span), float(t_span), int(n_t))

    def G(t):
        return np.sum((occ + 1.0) * np.exp(-1j * eps * t)
                      + occ * np.exp(+1j * eps * t))

    def resid(beta):
        num = 0.0
        den = 0.0
        for t in ts:
            lhs = G(t)
            rhs = np.sum((occ + 1.0) * np.exp(+1j * eps * t) * np.exp(-eps * beta)
                         + occ * np.exp(-1j * eps * t) * np.exp(+eps * beta))
            num += abs(lhs - rhs) ** 2
            den += abs(lhs) ** 2
        return float(np.sqrt(num / den)) if den > 0 else float("inf")

    if betas is None:
        betas = np.linspace(0.2, 2.0, 181)
    betas = np.asarray(betas, dtype=float)
    rr = np.array([resid(b) for b in betas])
    beta = float(betas[int(np.argmin(rr))])
    resid_min = float(np.min(rr))
    resid_b1 = resid(1.0)
    Gc = np.array([G(t) for t in ts])
    return KMSFit(beta=beta, resid_beta1=resid_b1, resid_min=resid_min,
                  ts=ts.tolist(), g_re=np.real(Gc).tolist(),
                  g_im=np.imag(Gc).tolist(), n_modes=int(eps.size))


# ===========================================================================
# UNRUH TEMPERATURE LAW from the modular-kernel boost diagonal
# ===========================================================================

@dataclass
class UnruhLawFit:
    """Carrier for the Unruh-law fit of a one-particle modular kernel diagonal.

    On the 2D Rindler half-line (cut x>0, horizon at x=0) Bisognano-Wichmann
    gives the modular Hamiltonian ``K = 2*pi K_boost``, ``K_boost = integral x
    T_00 dx``, so the modular energy density along the diagonal grows LINEARLY in
    the proper distance to the horizon, ``|K(x,x)| ~ 2*pi x rho_E``: the Unruh /
    Tolman local inverse temperature is ``beta_local(x) = 2*pi x`` and the local
    temperature obeys the Unruh law ``T_local(x) = 1/(2*pi x)`` (exponent -1).

    ``law_exponent`` is the log-log slope ``p_E`` of ``|K(x,x)|`` vs the PROPER
    distance ``x`` (BW: ``p_E = +1``, the energy density linear in proper distance
    => ``T ~ 1/x``); ``law_r2`` is the log-log R^2. ``boost_slope`` /
    ``boost_r2`` are the LINEAR fit of ``|K(x,x)|`` vs proper distance.
    ``centers`` / ``prof`` / ``counts`` are the binned diagonal profile.

    HONEST CAVEAT: the SJ modular kernel is a SURROGATE in modular-energy units
    ``eps = ln[mu/(mu-1)]`` (Casini-Huerta 0905.2562); its log-compression makes
    the measured exponent SUB-linear (``p_E ~ 0.7 < 1``) and does NOT carry the
    boost-rapidity normalisation, so the ABSOLUTE ``2*pi`` is NOT recovered from
    this diagonal alone (F-034 / F-036). ``law_exponent`` measures the LAW SHAPE,
    not the absolute Unruh temperature.
    """

    law_exponent: float
    law_r2: float
    boost_slope: float
    boost_r2: float
    centers: list
    prof: list
    counts: list
    n_bins: int = 0


def unruh_proper_law(K, x_proper, *, x_lo, x_hi, n_bins=12, min_count=6):
    """Unruh temperature-law fit of a modular-kernel diagonal vs PROPER distance.

    Bins ``|K(x,x)|`` (the modular energy density) against the proper distance
    ``x`` to the horizon on the GEOMETRY-FIXED window ``[x_lo, x_hi]`` (fixed by
    the caller from the sprinkling geometry BEFORE any slope -- anti-circular),
    then returns the log-log exponent ``p_E`` (BW: ``+1`` => Unruh ``T ~ 1/x``)
    and the linear boost slope. The window bounds must be supplied by the caller
    (the proper-distance scale is the load-bearing anti-circularity convention --
    it is NEVER fitted to give ``2*pi``).

    Formula: modular-flow-def, modular-spectrum, bisognano-wichmann boost.
    Evidence: F-036 (core-data/calculations/ncg-kms-unruh/calc.py).
    Conventions: Bisognano-Wichmann modular flow = boost ``K = 2*pi K_boost``
    (1712.04227, context 2008.07697); Unruh local temperature ``1/(2*pi x)``
    (unruh1976notes); Connes-Rovelli modular-flow-as-thermal-time gr-qc/9406019;
    Casini-Huerta single-mode modular energies 0905.2562; Sorkin-Yazdi SJ state
    1611.10281.

    Args:
        K: (n, n) site-basis one-particle modular kernel (Hermitian); only the
            real diagonal is used.
        x_proper: (n,) proper distances of the kept sites to the horizon.
        x_lo: lower proper-distance window bound (GEOMETRY-FIXED, NOT tuned).
        x_hi: upper proper-distance window bound (GEOMETRY-FIXED, NOT tuned).
        n_bins: number of proper-distance bins.
        min_count: minimum sites per bin to keep the bin.

    Returns:
        :class:`UnruhLawFit` with the log-log ``law_exponent`` (BW: +1), its
        ``law_r2``, the linear ``boost_slope`` + ``boost_r2`` and the binned
        ``centers`` / ``prof`` / ``counts``. NaN fields on a degenerate window.
    """
    K = np.asarray(K)
    diag = np.abs(np.real(np.diag(K)))
    xp = np.abs(np.asarray(x_proper, dtype=float))
    bins = np.linspace(float(x_lo), float(x_hi), int(n_bins) + 1)
    centers = 0.5 * (bins[:-1] + bins[1:])
    idx = np.digitize(xp, bins)
    prof = np.full(int(n_bins), np.nan)
    cnt = np.zeros(int(n_bins), dtype=int)
    for b in range(1, int(n_bins) + 1):
        msk = idx == b
        cnt[b - 1] = int(msk.sum())
        if msk.sum() >= min_count:
            prof[b - 1] = float(np.mean(diag[msk]))
    g = np.isfinite(prof) & (centers > 0) & (prof > 0)
    if g.sum() >= 3:
        lp = np.polyfit(np.log(centers[g]), np.log(prof[g]), 1)
        law_exp = float(lp[0])
        pred = lp[0] * np.log(centers[g]) + lp[1]
        ss = float(np.sum((np.log(prof[g]) - np.mean(np.log(prof[g]))) ** 2))
        law_r2 = float(1.0 - np.sum((np.log(prof[g]) - pred) ** 2) / ss) if ss > 0 else 0.0
    else:
        law_exp = float("nan")
        law_r2 = float("nan")
    if g.sum() >= 2:
        A = np.vstack([centers[g], np.ones(int(g.sum()))]).T
        coef, *_ = np.linalg.lstsq(A, prof[g], rcond=None)
        boost_slope = float(coef[0])
        pred_lin = A @ coef
        ss = float(np.sum((prof[g] - prof[g].mean()) ** 2))
        boost_r2 = float(1.0 - np.sum((prof[g] - pred_lin) ** 2) / ss) if ss > 0 else 0.0
    else:
        boost_slope = float("nan")
        boost_r2 = float("nan")
    return UnruhLawFit(law_exponent=law_exp, law_r2=law_r2,
                       boost_slope=boost_slope, boost_r2=boost_r2,
                       centers=centers.tolist(), prof=prof.tolist(),
                       counts=cnt.tolist(), n_bins=int(n_bins))


# ===========================================================================
# GEOMETRIC / gamma_5-GRADED BOOST DIRAC  (an EVEN spectral triple from the
# Killing field, NOT the square-root-of-modulus of the modular eps-spectrum)
# ===========================================================================

# 2D real gamma matrices in the chiral basis (Clifford {gamma^a, gamma^b} = 2 eta):
#   gamma^0 = sigma_x = [[0,1],[1,0]],  gamma^1 = i sigma_y = [[0,-1],[1,0]].
# The chiral grading gamma_5 = gamma^0 gamma^1 = diag(-1, +1) anticommutes with
# each gamma^a (Clifford), so {D, Gamma5} = 0 EXACTLY for the massless Dirac
# D = -i gamma^a d_a -- the operator is an EVEN spectral triple.
_GBD_G0 = np.array([[0.0, 1.0], [1.0, 0.0]])
_GBD_G1 = np.array([[0.0, -1.0], [1.0, 0.0]])
_GBD_G5 = _GBD_G0 @ _GBD_G1                       # = diag(-1, +1)


@dataclass
class GeometricBoostDirac:
    """Carrier for the geometric / gamma_5-graded boost Dirac of a 2D Rindler
    sub-region (the EVEN spectral triple from the Killing field xi = x d_t + t d_x,
    the named missing ingredient of F-036).

    ``boost_weight`` is the CLASSICAL Killing-field boost weight
    ``w_boost = two_pi * rho_proper`` (Bisognano-Wichmann ``K = 2*pi K_boost``);
    ``rho_proper = sqrt(x^2 - t^2)`` is the proper distance to the horizon on the
    right Rindler wedge. ``op_boost_quantum`` is the OPERATOR-derived spectral
    boost-quantum ``median(|eig_k| * <rho>_k)`` of the discrete boost generator
    ``K_op = (1/2){xi^mu, p_mu}`` built from the causet's finite-difference
    structure (the non-tautological 2*pi route; BW continuum value 2*pi).

    The grading diagnostics certify the EVEN spectral triple: ``anticomm_residual``
    (``||{D, Gamma5}|| / ||D||``, machine-zero by the Clifford algebra),
    ``herm_residual``, ``gamma5_sq_residual`` (``||Gamma5^2 - I||``) and
    ``spectrum_symmetry`` (``||sort(spec D) + reverse(sort(spec D))|| / ||D||``,
    the +-paired chiral spectrum -- machine-zero when ``{D,Gamma5}=0``).

    HONEST CAVEAT: ``boost_weight`` carries 2*pi BY CONSTRUCTION of xi (a classical
    Killing-field consistency check, NOT a discovery); the GENUINE operator content
    is ``op_boost_quantum`` and the grading well-posedness. On an irregular finite
    sprinkling the discrete first-order ``K_op`` has a VANISHING diagonal
    (``op_diag_max ~ 0``: the boost weight is not a diagonal observable) and its
    spectral ``op_boost_quantum`` DRIFTS with the discretisation scale (not
    rho-invariant at finite N) -- it brackets 2*pi but does not converge to it
    (F-040 / VYPOCET-37).
    """

    boost_weight: np.ndarray       # (n,) classical Killing-field weight 2*pi rho
    rho_proper: np.ndarray         # (n,) proper distance sqrt(x^2 - t^2)
    op_boost_quantum: float        # operator spectral boost-quantum median|eig|<rho>
    op_boost_quantum_nmodes: int   # eigenmodes inside the proper-distance window
    op_diag_max: float             # max |K_op(x,x)| (vanishes: not a diagonal obs)
    anticomm_residual: float       # ||{D, Gamma5}|| / ||D||  (machine-zero)
    herm_residual: float           # ||D - D^dagger|| / ||D||
    gamma5_sq_residual: float      # ||Gamma5^2 - I||
    spectrum_symmetry: float       # +-paired chiral spectrum residual
    n: int = 0                     # sub-region size


def _gbd_antisym_derivatives(coords, k_nn=6):
    """Antisymmetric nearest-neighbour first-derivative stencils ``Dt, Dx``
    (``n x n``, real, ``Dmu^T = -Dmu``) so ``-i Dmu`` is Hermitian. Each point
    connects to its ``k_nn`` nearest Euclidean neighbours with a first-difference
    weight ``(coord_j - coord_i) / |dr|^2`` symmetrised to be exactly
    antisymmetric."""
    coords = np.asarray(coords, dtype=float)
    n = coords.shape[0]
    Dt = np.zeros((n, n)); Dx = np.zeros((n, n))
    diff = coords[:, None, :] - coords[None, :, :]      # (n,n,2) = (i - j)
    d2 = diff[:, :, 0] ** 2 + diff[:, :, 1] ** 2
    np.fill_diagonal(d2, np.inf)
    kk = int(min(k_nn, max(1, n - 1)))
    order = np.argsort(d2, axis=1)[:, :kk]
    for i in range(n):
        for j in order[i]:
            dr2 = d2[i, j]
            if not np.isfinite(dr2) or dr2 <= 0:
                continue
            Dt[i, j] += 0.5 * (coords[j, 0] - coords[i, 0]) / dr2
            Dx[i, j] += 0.5 * (coords[j, 1] - coords[i, 1]) / dr2
    Dt = 0.5 * (Dt - Dt.T)
    Dx = 0.5 * (Dx - Dx.T)
    return Dt, Dx


def geometric_boost_dirac(coords, *, two_pi=None, k_nn=6, x_lo=None, x_hi=None):
    """Geometric / gamma_5-graded boost Dirac of a 2D Rindler sub-region: the EVEN
    spectral triple built from the Killing boost ``xi = x d_t + t d_x``, the named
    missing ingredient of F-036 (the NON-surrogate Dirac, NOT ``sgn(K) sqrt(|K|)``
    of the modular eps-spectrum).

    Builds (i) the massless 2D Dirac ``D = -i(gamma^0 Dt + gamma^1 Dx)`` on the
    ``2n``-dim spinor bundle over the ``n`` points with the chiral grading
    ``Gamma5 = I_n (x) gamma_5`` (``{D, Gamma5} = 0`` exactly -- an EVEN spectral
    triple), certifying its well-posedness; (ii) the CLASSICAL Killing-field boost
    weight ``w_boost = 2*pi rho_proper`` (Bisognano-Wichmann ``K = 2*pi K_boost``,
    Unruh local temperature ``1/(2*pi rho)``); and (iii) the OPERATOR-derived
    spectral boost-quantum ``median(|eig_k| <rho>_k)`` of the discrete boost
    generator ``K_op = (1/2){xi^mu, p_mu}`` (``p_mu = -i d_mu``), the non-
    tautological absolute-2*pi route. The proper distance is ``rho_proper =
    sqrt(x^2 - t^2)`` on the right Rindler wedge (cut ``x > 0``, horizon ``x = 0``).

    Formula: modular-flow-def, bisognano-wichmann boost, spectral-action-formula.
    Evidence: F-040 (core-data/calculations/geometric-boost-dirac/calc.py),
    builds on F-036/F-033 surrogate diagnosis.
    Conventions: 2D Rindler boost Killing field ``xi = x d_t + t d_x``; Bisognano-
    Wichmann modular flow = boost ``K = 2*pi K_boost``, Unruh local temperature
    ``1/(2*pi rho)`` (bisognano1976duality, unruh1976notes); chiral grading
    ``gamma_5 = gamma^0 gamma^1`` (Connes 'Noncommutative Geometry' 1994, even
    spectral triple); Connes-Rovelli modular-flow-as-thermal-time gr-qc/9406019.

    HONEST: ``boost_weight`` carries 2*pi BY CONSTRUCTION of ``xi`` (a classical
    consistency check, NOT a discovery); the genuine operator content is
    ``op_boost_quantum`` (which DRIFTS with the discretisation, not rho-invariant
    at finite N) and the grading well-posedness. Args ``x_lo, x_hi`` are the
    GEOMETRY-FIXED proper-distance window for the operator boost-quantum (default
    ``0.06 * max(rho)`` and ``0.90 * max(rho)``, anti-circular -- NEVER tuned to
    2*pi).

    Args:
        coords: (n, 2) point coordinates (columns t, x) of the Rindler sub-region.
        two_pi: the BW coefficient for ``boost_weight`` (default ``2*pi``).
        k_nn: nearest-neighbour count for the finite-difference Dirac stencil.
        x_lo: lower proper-distance window bound for the operator boost-quantum
            (default ``0.06 * max(rho_proper)``).
        x_hi: upper proper-distance window bound (default ``0.90 * max(rho_proper)``).

    Returns:
        :class:`GeometricBoostDirac` with the classical ``boost_weight`` /
        ``rho_proper``, the operator ``op_boost_quantum`` (+ ``nmodes``,
        ``op_diag_max``) and the four grading-diagnostic residuals.
    """
    coords = np.asarray(coords, dtype=float)
    n = coords.shape[0]
    tp = (2.0 * np.pi) if two_pi is None else float(two_pi)
    t = coords[:, 0]; x = coords[:, 1]
    rho_proper = np.sqrt(np.maximum(x ** 2 - t ** 2, 0.0))
    w_boost = tp * rho_proper

    # --- gamma_5-graded geometric Dirac (even spectral triple) -------------
    Dt, Dx = _gbd_antisym_derivatives(coords, k_nn=k_nn)
    D = -1j * (np.kron(_GBD_G0, Dt) + np.kron(_GBD_G1, Dx))
    D = 0.5 * (D + D.conj().T)
    Gamma5 = np.kron(_GBD_G5, np.eye(n))
    scaleD = float(np.max(np.abs(D))) + 1e-30
    anti = D @ Gamma5 + Gamma5 @ D
    anti_res = float(np.max(np.abs(anti)) / scaleD)
    herm_res = float(np.max(np.abs(D - D.conj().T)) / scaleD)
    g5sq = float(np.max(np.abs(Gamma5 @ Gamma5 - np.eye(2 * n))))
    wD = np.linalg.eigvalsh(0.5 * (D + D.conj().T))
    sym = (float(np.max(np.abs(np.sort(wD) + np.sort(wD)[::-1]))
                 / (float(np.max(np.abs(wD))) + 1e-30)) if wD.size else float("nan"))

    # --- operator boost generator K_op = (1/2){xi^mu, p_mu} ----------------
    Kop = -1j * 0.5 * (np.diag(x) @ Dt + Dt @ np.diag(x)
                       + np.diag(t) @ Dx + Dx @ np.diag(t))
    Kop = 0.5 * (Kop + Kop.conj().T)
    wk, Vk = np.linalg.eigh(Kop)
    prob = np.abs(Vk) ** 2
    rhobar = (prob * rho_proper[:, None]).sum(0)
    if x_lo is None:
        x_lo = 0.06 * float(np.max(rho_proper)) if rho_proper.size else 0.0
    if x_hi is None:
        x_hi = 0.90 * float(np.max(rho_proper)) if rho_proper.size else 1.0
    m = (np.abs(wk) > 1e-6) & (rhobar > x_lo) & (rhobar < x_hi)
    op_bq = (float(np.median(np.abs(wk[m]) * rhobar[m])) if m.sum() >= 3
             else float("nan"))
    op_diag_max = float(np.max(np.abs(np.real(np.diag(Kop))))) if n else float("nan")

    return GeometricBoostDirac(
        boost_weight=w_boost, rho_proper=rho_proper,
        op_boost_quantum=op_bq, op_boost_quantum_nmodes=int(m.sum()),
        op_diag_max=op_diag_max, anticomm_residual=anti_res,
        herm_residual=herm_res, gamma5_sq_residual=g5sq,
        spectrum_symmetry=sym, n=int(n))
