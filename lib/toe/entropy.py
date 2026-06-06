# -*- coding: utf-8 -*-
"""toe.entropy -- SSEE via the generalized eigenproblem on a causal-set region.

Module C1 of the ``toe`` library (Layer C). It depends on ``toe.sj`` (B1),
``toe.causet`` (A2) and ``toe.fits`` (A1). It does NOT import ``toe.vntype``
(sibling C2) -- shared helpers live in the lower layers.

The Sorkin-Johnston Spacetime Entanglement Entropy (SSEE) on a sub-region O is
defined via the generalized eigenproblem

    W_O v = mu iDelta_O v

on the KEPT subspace (global and local eigenvalue-magnitude truncation at
kappa), with

    S = sum_mu  mu ln|mu|

(Sorkin-Yazdi 1611.10281, Surya-Nomaan-X-Yazdi 2008.07697).

The module exposes:
  * ``kappa_2d`` / ``n_max_area_law`` -- the two UV-cutoff prescriptions;
  * ``rank_at_cutoff`` -- number of positive iDelta modes above the magnitude
    cutoff;
  * ``ssee`` -- the core generalized-eigenproblem SSEE computation;
  * ``ssee_scaling`` -- scaling driver (multiple N x seeds -> FitResult).

Design contract (ARCHITECTURE.md C1):
  - every function takes physics parameters (N, dim, frac, kappa ...);
  - stochastic functions take an explicit ``seed`` / ``seed_base`` -- no global
    RNG state;
  - pure: no file I/O, no matplotlib import (see ``toe.viz``).

Only numpy / scipy are used (+ ``toe.sj``, ``toe.causet``, ``toe.fits``).
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Optional, Callable

import numpy as np

from toe.fits import FitResult, Measurement, powerlaw_fit, validate_against
from toe.sj import sj_state
from toe.causet import causal_matrix, pauli_jordan, green_retarded_2d

__all__ = [
    "kappa_2d",
    "n_max_area_law",
    "rank_at_cutoff",
    "ssee",
    "ssee_scaling",
    "ModularKernel",
    "modular_kernel",
    # v0.3.0 -- SPARSE/ITERATIVE path
    "ssee_sparse",
]


# ===========================================================================
# CUTOFF PRESCRIPTIONS
# ===========================================================================

def kappa_2d(N: int) -> float:
    """Sorkin-Yazdi UV eigenvalue-magnitude cutoff for the 2D massless scalar.

    Formula: ssee, ssee-formula.
    Evidence: VYPOCET-04 (core-data/calculations/ssee-diamond/calc.py kappa_2d),
    VYPOCET-12 (sj-vn-type/calc.py kappa_2d).
    Conventions: Sorkin-Yazdi 1712.04227 -- kappa = sqrt(N) / (4 pi) for the 2D
    local massless scalar. Eigenvalues of iDelta with |lambda| <= kappa are
    discarded (they deviate from the continuum A/k spectrum). This is the
    magnitude cutoff (NOT a rank cut).

    Args:
        N: number of sprinkled points (= density rho * VOL_UV in the unit diamond).

    Returns:
        float kappa = sqrt(N) / (4 * pi).
    """
    return float(np.sqrt(N) / (4.0 * np.pi))


def n_max_area_law(N: int, dim: int, *, alpha: float = 2.0) -> int:
    """Rank cutoff ``n_max = alpha * N^{(dim-1)/dim}`` for the area-law truncation.

    This is the number-truncation ansatz from Surya-Nomaan-X-Yazdi 2008.07697:
    keep only the top ``n_max`` positive modes of iDelta. For dim=4 this gives
    ``2 * N^{3/4}`` (the 4D slab prescription validated in VYPOCET-06); for
    dim=2 it gives ``N^{1/2}`` (same scaling as the Sorkin-Yazdi kappa cut).

    Formula: crossed-product-entropy, crossed-product-def.
    Evidence: VYPOCET-06 (core-data/calculations/ssee-slab-4d/calc.py, rank
    truncation prescription), VYPOCET-04 (ssee-diamond/calc.py, 2D case).
    Conventions: Surya-Nomaan-X-Yazdi 2008.07697 eq. for n_max;
    observer/crossed-product cutoff interpretation (ARCHITECTURE.md C1 review
    §19).

    Args:
        N: number of sprinkled points.
        dim: spacetime dimension (2 or 4).
        alpha: coefficient (default 2.0, matching the 4D prescription).

    Returns:
        int n_max = round(alpha * N^{(dim-1)/dim}).
    """
    exponent = (dim - 1) / dim
    return int(round(alpha * (N ** exponent)))


def rank_at_cutoff(pos_spectrum: np.ndarray, kappa: float) -> int:
    """Number of positive iDelta eigenvalues above the magnitude cutoff kappa.

    This is the RANK implied by the Sorkin-Yazdi entropy cutoff |lambda| > kappa.

    Formula: ssee-formula.
    Evidence: VYPOCET-04 (core-data/calculations/ssee-diamond/calc.py
    rank_at_cutoff).
    Conventions: Sorkin-Yazdi 1712.04227 -- eigenvalues with |lambda| <= kappa
    are discarded; this is the count of the kept positive modes.

    Args:
        pos_spectrum: 1-D array of positive eigenvalues of iDelta (sorted
            descending or any order).
        kappa: magnitude cutoff.

    Returns:
        int -- number of entries with value > kappa.
    """
    return int(np.sum(np.asarray(pos_spectrum) > kappa))


# ===========================================================================
# CORE SSEE COMPUTATION
# ===========================================================================

def ssee(
    W: np.ndarray,
    iDelta: np.ndarray,
    sub_idx: np.ndarray,
    *,
    kappa: Optional[float] = None,
    n_max: Optional[int] = None,
    tol: float = 1e-10,
) -> Measurement:
    """Sorkin-Johnston SSEE for a sub-region via the generalized eigenproblem.

    Implements the double-truncation algorithm from Sorkin-Yazdi 1712.04227:
    1. GLOBAL truncation: if ``kappa`` is given, zero out eigenvalues of iDelta
       with |lambda| <= kappa; rebuild W as the positive part of the truncated
       iDelta. If ``n_max`` is given, keep only the top ``n_max`` positive modes
       (rank truncation, VYPOCET-06).
    2. Restrict truncated iDelta and W to the sub-region submatrices.
    3. LOCAL truncation: zero out eigenvalues of restricted iDelta_O with
       |lambda| <= kappa (same cutoff), project onto the kept modes.
    4. Generalized eigenproblem W_O v = mu iDelta_O v on the kept subspace.
    5. S = sum_mu  mu ln|mu|  (pairs mu, 1-mu contribute positively).

    If neither kappa nor n_max is given, no global truncation is applied
    (volume-law regime, may include spurious sub-discreteness modes).

    Formula: ssee, ssee-formula, crossed-product-entropy, type-ii-trace-entropy.
    Evidence: VYPOCET-04 (core-data/calculations/ssee-diamond/calc.py ssee),
    VYPOCET-06 (ssee-slab-4d/calc.py ssee),
    VYPOCET-12 (sj-vn-type/calc.py ssee_mu).
    Conventions: Sorkin-Yazdi 1611.10281 eq.(6-7); Surya-Nomaan-X-Yazdi
    2008.07697 double-truncation; eigenvalues pair (mu, 1-mu); S >= 0.

    Args:
        W: (N, N) SJ Wightman matrix (from ``toe.sj.wightman``).
        iDelta: (N, N) Hermitian Pauli-Jordan operator.
        sub_idx: 1-D integer index array of sub-region points.
        kappa: magnitude cutoff for global + local eigenvalue truncation.
            Overridden if ``n_max`` is also given (``n_max`` takes precedence for
            the global cut; kappa is still used for the local cut).
        n_max: rank cutoff -- keep only the top ``n_max`` positive modes of
            iDelta globally (VYPOCET-06 prescription). When ``None`` and
            ``kappa`` is not ``None``, kappa-based magnitude cut is used.
        tol: numerical tolerance for discarding near-zero generalized eigenvalues
            (and their complements near 1).

    Returns:
        Measurement with value = S (entropy), se = 0.0 (single sprinkle; the
        caller aggregates across seeds for a cross-seed SE). ``n`` = number of
        ``mu`` eigenvalues retained (the "good" mu count).
    """
    iD = np.asarray(iDelta, dtype=complex)
    Wm = np.asarray(W, dtype=complex)

    # ---- GLOBAL truncation ------------------------------------------------
    if n_max is not None:
        # Rank truncation: keep the top n_max positive modes of iDelta.
        w, V = np.linalg.eigh(iD)
        pos_mask = w > 0
        pos_idx = np.where(pos_mask)[0]
        # Sort positive eigenvalues descending to select the top n_max.
        pos_sorted = np.argsort(w[pos_idx])[::-1]
        keep_pos = pos_idx[pos_sorted[:n_max]]
        # Also keep the paired negative eigenvalues (spectrum is +/- paired).
        neg_mask = w < 0
        neg_idx = np.where(neg_mask)[0]
        neg_sorted = np.argsort(-w[neg_idx])[::-1]   # most negative first
        keep_neg = neg_idx[neg_sorted[:n_max]]
        keep = np.concatenate([keep_neg, keep_pos])
        wk = w[keep]
        Vk = V[:, keep]
        iD = (Vk * wk) @ Vk.conj().T
        pos_k = wk > 0
        Wm = (Vk[:, pos_k] * wk[pos_k]) @ Vk[:, pos_k].conj().T
    elif kappa is not None:
        # Magnitude truncation: keep |lambda| > kappa.
        w, V = np.linalg.eigh(iD)
        keep = np.abs(w) > kappa
        wk = w[keep]
        Vk = V[:, keep]
        iD = (Vk * wk) @ Vk.conj().T
        pos_k = wk > 0
        Wm = (Vk[:, pos_k] * wk[pos_k]) @ Vk[:, pos_k].conj().T

    # ---- Restrict to sub-region ------------------------------------------
    sub_idx = np.asarray(sub_idx, dtype=int)
    iD_O = iD[np.ix_(sub_idx, sub_idx)]
    W_O = Wm[np.ix_(sub_idx, sub_idx)]

    # ---- LOCAL truncation (diagonalise restricted iDelta_O) ---------------
    d, U = np.linalg.eigh(iD_O)
    scale = float(np.max(np.abs(d))) if d.size else 0.0
    if scale == 0.0:
        return Measurement(value=0.0, se=0.0, n=0)

    local_cut = kappa if kappa is not None else tol * scale
    keep_local = np.abs(d) > local_cut
    if keep_local.sum() == 0:
        return Measurement(value=0.0, se=0.0, n=0)

    d_k = d[keep_local]
    U_k = U[:, keep_local]

    # ---- Generalized eigenproblem in the kept basis -----------------------
    Wproj = U_k.conj().T @ W_O @ U_k
    M = (Wproj.T / d_k).T           # diag(1/d_k) @ Wproj
    mu = np.linalg.eigvals(M).real  # real (mu, 1-mu) pairs

    good = (np.abs(mu) > tol) & (np.abs(mu - 1.0) > tol)
    mu_g = mu[good]
    S = float(np.sum(mu_g * np.log(np.abs(mu_g))))

    return Measurement(value=S, se=0.0, n=int(good.sum()))


# ===========================================================================
# v0.3.0 -- SPARSE/ITERATIVE SSEE  (truncated entropy from k-mode SJ data)
# ===========================================================================

def ssee_sparse(
    sj_sparse,
    sub_idx: np.ndarray,
    *,
    kappa: Optional[float] = None,
    n_max: Optional[int] = None,
    tol: float = 1e-10,
) -> Measurement:
    """Truncated Sorkin-Johnston SSEE from the TOP-k sparse SJ spectral data.

    The sparse sibling of :func:`ssee`: instead of the dense ``(W, iDelta)`` pair
    it consumes a :class:`toe.sj.SJStateSparse` (the ``k`` dominant ``+/-`` paired
    eigenpairs of ``iDelta`` from :func:`toe.sj.sj_state_sparse`) and reconstructs
    the TRUNCATED operators on the sub-region directly from those modes:

    1. GLOBAL truncation -- keep the captured modes with ``|lambda| > kappa``
       (``kappa`` magnitude cut) or the top ``n_max`` positive modes (``n_max``
       rank cut). Form the dense ``(N, N)`` truncated ``iDelta`` and ``W`` from
       the kept modes ONLY (rank ``<= k << N``); these are exactly the truncated
       operators the dense :func:`ssee` builds, PROVIDED the sparse pass captured
       all modes above the cut (``k > 2 * #{|lambda| > kappa}``).
    2. Restrict to the sub-region, do the LOCAL truncation + generalized
       eigenproblem ``W_O v = mu iDelta_O v`` and ``S = sum_mu mu ln|mu|`` --
       identical to :func:`ssee` from step 2 onward.

    CORRECTNESS CONDITION (honest): the sparse SSEE equals the dense SSEE iff the
    cut ``|lambda| > kappa`` (resp. the top ``n_max`` modes) is fully inside the
    captured top-k set. With ``kappa = sqrt(N)/(4 pi)`` in 2D the number of modes
    above the cut grows like ``~N^{1/2}``, while ``k ~ few x N^{3/4}`` grows
    faster, so the condition holds with margin at large N (verified by the
    overlap-validation tests). If ``kappa`` is below the smallest captured
    ``|lambda|`` the truncation is incomplete and the result UNDER-counts -- the
    caller must size ``k`` accordingly.

    Formula: ssee, ssee-formula, crossed-product-entropy, type-ii-trace-entropy.
    Evidence: VYPOCET-04 (ssee-diamond/calc.py ssee), VYPOCET-12
    (sj-vn-type/calc.py ssee_mu); sparse k-mode variant added in v0.3.0 for the
    large-N path (H5g-2 A/4 cap, VYPOCET-19 Part-3 tracial probe).
    Conventions: Sorkin-Yazdi 1611.10281 eq.(6-7); 1712.04227 double truncation;
    eigenvalues pair ``(mu, 1-mu)``; ``S >= 0``. The reconstruction uses the
    ``+/-`` paired modes returned by ``eigsh(which='LM')``.

    Args:
        sj_sparse: :class:`toe.sj.SJStateSparse` -- the top-k SJ spectral data
            (``eigvals`` ascending, ``eigvecs`` columns) on the FULL point set.
            The point order must match ``sub_idx`` (i.e. the operator's order; if
            built via :func:`toe.causet.idelta_operator_2d` apply its ``perm`` to
            both coords and ``sub_idx``).
        sub_idx: 1-D integer index array of sub-region points (in the operator's
            point order).
        kappa: magnitude cutoff for global + local eigenvalue truncation.
        n_max: rank cutoff -- keep only the top ``n_max`` captured positive modes
            (and their negative partners). Takes precedence over ``kappa`` for the
            global cut; ``kappa`` is still used for the local cut.
        tol: tolerance for discarding near-zero generalized eigenvalues (and
            their complements near 1).

    Returns:
        Measurement with value = S (entropy), se = 0.0, n = number of retained
        ``mu`` eigenvalues. Same shape as :func:`ssee`.
    """
    w = np.asarray(sj_sparse.eigvals, dtype=float)
    V = np.asarray(sj_sparse.eigvecs)

    # ---- GLOBAL truncation from the captured k modes ----------------------
    if n_max is not None:
        pos_idx = np.where(w > 0)[0]
        neg_idx = np.where(w < 0)[0]
        # top n_max positive (largest) and their negative partners
        pos_keep = pos_idx[np.argsort(w[pos_idx])[::-1][:n_max]]
        neg_keep = neg_idx[np.argsort(-w[neg_idx])[::-1][:n_max]]
        keep = np.concatenate([neg_keep, pos_keep])
    elif kappa is not None:
        keep = np.where(np.abs(w) > kappa)[0]
    else:
        keep = np.arange(w.size)

    if keep.size == 0:
        return Measurement(value=0.0, se=0.0, n=0)

    wk = w[keep]
    Vk = V[:, keep]
    iD = (Vk * wk) @ Vk.conj().T
    pos_k = wk > 0
    Wm = (Vk[:, pos_k] * wk[pos_k]) @ Vk[:, pos_k].conj().T

    # ---- Restrict to sub-region -------------------------------------------
    sub_idx = np.asarray(sub_idx, dtype=int)
    iD_O = iD[np.ix_(sub_idx, sub_idx)]
    W_O = Wm[np.ix_(sub_idx, sub_idx)]

    # ---- LOCAL truncation + generalized eigenproblem ----------------------
    d, U = np.linalg.eigh(iD_O)
    scale = float(np.max(np.abs(d))) if d.size else 0.0
    if scale == 0.0:
        return Measurement(value=0.0, se=0.0, n=0)

    local_cut = kappa if kappa is not None else tol * scale
    keep_local = np.abs(d) > local_cut
    if keep_local.sum() == 0:
        return Measurement(value=0.0, se=0.0, n=0)

    d_k = d[keep_local]
    U_k = U[:, keep_local]

    Wproj = U_k.conj().T @ W_O @ U_k
    M = (Wproj.T / d_k).T
    mu = np.linalg.eigvals(M).real

    good = (np.abs(mu) > tol) & (np.abs(mu - 1.0) > tol)
    mu_g = mu[good]
    S = float(np.sum(mu_g * np.log(np.abs(mu_g))))

    return Measurement(value=S, se=0.0, n=int(good.sum()))


# ===========================================================================
# SITE-BASIS MODULAR KERNEL  K(x, y)
# ===========================================================================

@dataclass
class ModularKernel:
    """Carrier for the one-particle modular kernel of a sub-region.

    Plain data object (no physics behaviour). ``K`` is the site-basis
    one-particle modular Hamiltonian ``K(x, y)`` on the kept sub-region points;
    ``eps`` are its single-mode modular energies ``eps = ln[mu/(mu-1)]`` (sorted
    ascending); ``S`` is the scalar SSEE on the same cut (so it matches
    :func:`ssee`); ``nu = mu - 1/2`` are the occupation parameters; ``n`` is the
    sub-region size and ``n_modes`` the number of good ``mu`` modes.
    ``validated`` is None until the caller compares ``S`` against a target.

    Conventions: Casini-Huerta 0905.2562 single-mode K; Sorkin-Yazdi
    1611.10281 site-basis lift (Peschel resolution).
    """

    K: np.ndarray              # (n, n) site-basis modular kernel (Hermitian)
    eps: np.ndarray            # modular energies ln[mu/(mu-1)], ascending
    S: float                   # scalar SSEE on this cut (matches ssee().value)
    nu: np.ndarray             # occupation parameters mu - 1/2, ascending
    n: int = 0                 # sub-region size
    n_modes: int = 0           # number of retained mu modes
    validated: Optional[bool] = None


def modular_kernel(
    W: np.ndarray,
    iDelta: np.ndarray,
    sub_idx: np.ndarray,
    *,
    kappa: Optional[float] = None,
    tol: float = 1e-9,
) -> Optional["ModularKernel"]:
    """Site-basis one-particle modular kernel ``K(x, y)`` of a sub-region O,
    exposing the FULL kernel that :func:`ssee` collapses to the scalar ``S``.

    Solves the SSEE generalized eigenproblem ``W_O v = mu iDelta_O v`` on the
    kept sub-region subspace, forms the single-mode modular energies ``eps =
    ln[mu/(mu-1)]``, and lifts the spectral resolution back to the SITE basis to
    return the one-particle modular Hamiltonian ``K(x, y)``. This is the object
    the locality diagnostics in VYPOCET-18/20/22 need (off-diagonal decay,
    non-local fraction, distance-to-locus profiles); the scalar entropy ``S`` it
    also reports is, by construction, the same number :func:`ssee` returns on the
    same cut (``S = sum_mu mu ln|mu|`` rewritten via ``nu = mu - 1/2`` as
    ``sum (nu+1/2) ln(nu+1/2) - (nu-1/2) ln(nu-1/2)``).

    UNTRUNCATED probe ``kappa=None`` = the genuine SJ modular flow whose
    geometricity Bisognano-Wichmann predicts. Returns ``None`` when the kept
    sub-region carries fewer than two modes or no ``mu > 1`` survive (the cut is
    too small to define a kernel).

    Formula: ssee, ssee-formula, modular-flow-def, modular-spectrum.
    Evidence: VYPOCET-18/20/22 (modular-flow-codim2/helpers.py
    modular_kernel_ssee, modular-flow-bd-4d); lifted to expose K next to
    :func:`ssee` (which returns only the scalar S).
    Conventions: Casini-Huerta 0905.2562 single-mode ``eps = ln[mu/(mu-1)]``,
    ``nu = mu - 1/2``; Sorkin-Yazdi 1611.10281 SSEE; the site-basis K is the
    Peschel-style spectral resolution lifted through the kept-mode basis.

    Args:
        W: (N, N) SJ Wightman matrix.
        iDelta: (N, N) Hermitian Pauli-Jordan operator.
        sub_idx: 1-D integer index array of sub-region points.
        kappa: optional magnitude cutoff for global + local eigenvalue
            truncation. ``None`` (default) = untruncated SJ modular flow.
        tol: numerical tolerance for the local cut and the ``mu > 1`` selection.

    Returns:
        ModularKernel (K, eps, S, nu, n, n_modes) or ``None`` if the sub-region
        is too small to define a kernel.
    """
    iD = np.asarray(iDelta)
    Wm = np.asarray(W)
    if kappa is not None:
        w, V = np.linalg.eigh(iD)
        keep = np.abs(w) > kappa
        wk = w[keep]
        Vk = V[:, keep]
        iD = (Vk * wk) @ Vk.conj().T
        pos = wk > 0
        Wm = (Vk[:, pos] * wk[pos]) @ Vk[:, pos].conj().T

    sub_idx = np.asarray(sub_idx, dtype=int)
    iD_O = iD[np.ix_(sub_idx, sub_idx)]
    W_O = Wm[np.ix_(sub_idx, sub_idx)]
    n = len(sub_idx)

    d, U = np.linalg.eigh(iD_O)
    scale = float(np.max(np.abs(d))) if d.size else 0.0
    if scale == 0.0:
        return None
    local_cut = kappa if (kappa is not None) else tol * scale
    keep = np.abs(d) > local_cut
    if keep.sum() < 2:
        return None
    d_k = d[keep]
    U_k = U[:, keep]
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

    with np.errstate(divide="ignore", invalid="ignore"):
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
    return ModularKernel(K=K_site, eps=np.sort(eps), S=S, nu=np.sort(nu),
                         n=n, n_modes=int(good.sum()))


# ===========================================================================
# SCALING DRIVER
# ===========================================================================

def ssee_scaling(
    builder: Callable,
    Ns: list,
    *,
    frac: float = 0.5,
    n_seeds: int,
    seed_base: int,
    truncate: str = "kappa",
) -> FitResult:
    """Build sprinkle -> iDelta -> W -> SSEE across Ns x seeds; fit S vs N.

    Iterates over each N in ``Ns`` and ``n_seeds`` seeds, computing the SSEE of
    the concentric sub-region (fraction ``frac`` of the diamond's null
    half-extent) for each. The mean entropy S_mean(N) is then fit to a power law
    S ~ N^a via :func:`toe.fits.powerlaw_fit` with the across-seed bootstrap CI.

    The seed scheme mirrors VYPOCET-12 (sj-vn-type/calc.py):
        rng = np.random.default_rng(seed_base + 1000 * N + s)

    Formula: ssee-formula, crossed-product-entropy.
    Evidence: VYPOCET-04 (ssee-diamond/calc.py run, Part C),
    VYPOCET-12 (sj-vn-type/calc.py run).
    Conventions: Sorkin-Yazdi 1611.10281; kappa = sqrt(N)/(4 pi); sub-region =
    concentric diamond at fraction frac (|u|, |v| <= frac * t_half).

    Args:
        builder: a causet region builder callable, e.g.
            ``toe.causet.sprinkle_diamond2d``. Called as
            ``builder(N, rng)`` -- must return (N, 2) null coords (u, v) in the
            ssee-diamond convention (concentric sub-diamond at frac uses
            |u|, |v| <= frac).
        Ns: list of sprinkling sizes.
        frac: sub-region linear fraction of the diamond half-extent.
        n_seeds: number of random seeds per N.
        seed_base: base for the deterministic seed scheme
            ``seed_base + 1000 * N + s``.
        truncate: ``"kappa"`` (default) -- use kappa_2d(N) eigenvalue-magnitude
            cutoff; ``"none"`` -- no truncation (volume-law regime).

    Returns:
        FitResult with value = power-law exponent a, se_regression, ci68_bootstrap
        (across-seed bootstrap), r2. ``validated`` is None (the caller compares
        against results.json targets and calls ``validate_against``).
    """
    Ns_arr = np.array(Ns, dtype=float)
    # per_seed_S[i, s] = S for Ns[i], seed s
    per_seed_S = np.zeros((len(Ns), n_seeds))

    for i, N in enumerate(Ns):
        kap = kappa_2d(N) if truncate == "kappa" else None
        for s in range(n_seeds):
            rng = np.random.default_rng(seed_base + 1000 * N + s)
            coords = builder(N, rng)
            # Build causal matrix and Pauli-Jordan in the null-coord convention
            C = _causal_from_null(coords)
            iDelta_full = pauli_jordan(green_retarded_2d(C))
            st = sj_state(iDelta_full)
            # Sub-region: concentric diamond {|u|, |v| <= frac}
            sub_idx = _subdiamond_idx(coords, frac)
            meas = ssee(st.W, iDelta_full, sub_idx, kappa=kap)
            per_seed_S[i, s] = meas.value

    S_mean = per_seed_S.mean(axis=1)

    # Bootstrap CI: per_sample shape (n_points, n_seeds) = (len(Ns), n_seeds)
    fit = powerlaw_fit(
        Ns_arr,
        np.maximum(S_mean, 1e-9),
        resamples=per_seed_S,   # shape (len(Ns), n_seeds) -> passed as (n_points, n_seeds)
    )
    return fit


# ===========================================================================
# INTERNAL HELPERS
# ===========================================================================

def _causal_from_null(coords: np.ndarray) -> np.ndarray:
    """Build causal matrix from 2D null coordinates (u, v).

    Convention (ssee-diamond): coords columns are (u, v).
    y precedes x iff u_y <= u_x AND v_y <= v_x (and y != x).
    """
    u = coords[:, 0][:, None]    # (N, 1)
    v = coords[:, 1][:, None]
    uy = coords[:, 0][None, :]   # (1, N)
    vy = coords[:, 1][None, :]
    prec = (uy <= u) & (vy <= v)
    C = prec.astype(np.float64)
    np.fill_diagonal(C, 0.0)
    return C


def _subdiamond_idx(coords: np.ndarray, frac: float, t_half: float = 1.0) -> np.ndarray:
    """Indices of points inside the concentric sub-diamond of linear size frac.

    Sub-diamond = {|u| <= frac * t_half AND |v| <= frac * t_half}.
    """
    u = coords[:, 0]
    v = coords[:, 1]
    r = frac * t_half
    return np.where((np.abs(u) <= r) & (np.abs(v) <= r))[0]
