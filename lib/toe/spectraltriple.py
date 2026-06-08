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
