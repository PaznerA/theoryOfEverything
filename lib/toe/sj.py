# -*- coding: utf-8 -*-
"""toe.sj -- the Sorkin-Johnston (SJ) state and its rotating-spacetime
observables.

Module B1 of the ``toe`` library (Layer B). It depends only on ``toe.causet``
(Layer A, the Pauli-Jordan / causal-structure machinery) and ``toe.fits`` (the
shared Result dataclasses). It does NOT import ``toe.entropy`` / ``toe.vntype``.

The SJ state is the distinguished Gaussian state whose Wightman function ``W``
is the POSITIVE spectral part of the Pauli-Jordan operator ``iDelta``
(Sorkin-Yazdi 1611.10281):

    iDelta = i (G_R - G_R^T)   (Hermitian, real +/- paired spectrum),
    W      = sum_{lambda_k > 0} lambda_k v_k v_k^dagger,
    W - W^dagger = iDelta,   W >= 0  (spectrally).

This is the *unique* state built from the causal/conformal data alone -- it
needs no timelike Killing vector, so it goes through cleanly inside a rotating
ergoregion where the stationary (Boulware/Hartle-Hawking) vacua fail.

The module collects, as smallest composable units:
  * ``sj_state`` / ``wightman`` -- the SJ construction from ``iDelta``;
  * ``asymmetry_causal`` / ``asymmetry_wightman`` -- the frame-dragging /
    superradiance directional asymmetries of the SJ two-point function over
    causal links (sj-rotating-btz two_point_profile);
  * ``superradiant_weight`` -- the eigenvector-overlap weight of the SJ positive
    subspace inside the superradiant wedge w(w - k Omega) < 0
    (sj-eigenvector-superradiance superradiance_weights);
  * ``positive_subspace_overlap`` -- the principal-angle (mean cos^2) overlap of
    two SJ positive subspaces (sj-eigenvector-superradiance subspace_overlap).

Design contract (ARCHITECTURE.md B1):
  - inputs are physics quantities (``iDelta`` / coords / causal matrix /
    omega / frequency grids), never ad-hoc magic constants;
  - every stochastic function takes an explicit ``seed`` (REQUIRED) -- no global
    RNG;
  - functions returning a ``(value, uncertainty)`` pair return a
    ``toe.fits.Measurement``; ``sj_state`` returns the small ``SJState`` carrier;
  - the module is pure: no file I/O, no plotting (see ``toe.viz``).

Only numpy / scipy are used.
"""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np

from toe.fits import Measurement

__all__ = [
    "SJState",
    "sj_state",
    "wightman",
    "asymmetry_causal",
    "asymmetry_wightman",
    "superradiant_weight",
    "positive_subspace_overlap",
    # v0.3.0 -- SPARSE/ITERATIVE path
    "SJStateSparse",
    "sj_state_sparse",
]


# ===========================================================================
# THE SJ STATE
# ===========================================================================

@dataclass
class SJState:
    """Carrier for the Sorkin-Johnston state of a Pauli-Jordan operator.

    Plain data object -- no physics behaviour beyond holding the spectral
    decomposition. ``W`` is the SJ Wightman matrix (positive part of iDelta);
    ``pos_spectrum`` is the positive eigenvalues sorted descending; ``eigvals`` /
    ``eigvecs`` are the full Hermitian decomposition (ascending eigenvalues).

    Conventions: Sorkin-Yazdi 1611.10281; W - W^dagger = iDelta, W >= 0.
    """

    eigvals: np.ndarray        # full real spectrum of iDelta, ascending
    eigvecs: np.ndarray        # corresponding eigenvectors (columns)
    pos_spectrum: np.ndarray   # positive eigenvalues, sorted descending
    W: np.ndarray              # SJ Wightman = positive spectral part of iDelta


def sj_state(iDelta, *, tol=1e-12, rel_floor=None):
    """SJ state from the Pauli-Jordan operator ``iDelta``.

    Eigendecomposes the Hermitian ``iDelta`` and forms the SJ Wightman function
    as its positive spectral part ``W = sum_{lambda_k > cut} lambda_k
    v_k v_k^dagger``. By antisymmetry of ``Delta`` the spectrum is exactly
    ``+/-`` paired, so ``W - W^dagger = iDelta`` (to machine precision) and ``W``
    is positive semidefinite.

    The positive-eigenvalue cut is by default the ABSOLUTE threshold ``tol``
    (``cut = tol``), which is the right choice for the well-conditioned
    link-matrix / sharp objects. For ILL-CONDITIONED objects -- notably the
    SMEARED Benincasa-Dowker inverse ``G_R = B_eps^{-1}`` whose spectrum spans
    ``cond ~ 1e4-1e6`` -- a RELATIVE floor is needed so that inversion noise in
    the small eigenvalues is not amplified into the Wightman function. Passing
    ``rel_floor`` (e.g. ``1e-10``) sets ``cut = rel_floor * max|lambda|``; the
    VYPOCET-09/20 convention used for all BD-inverse SJ states.

    Backwards compatibility: ``rel_floor=None`` (the default) keeps the original
    absolute-``tol`` code path bit-for-bit; the relative floor is opt-in.

    Formula: pauli-jordan, modular-polar-decomposition.
    Evidence: VYPOCET-12 (core-data/calculations/sj-vn-type/calc.py
    sj_wightman_from_eig), VYPOCET-08 (sj-rotating-btz/calc.py sj_decompose);
    rel_floor from VYPOCET-09/20 (modular-flow-codim2/helpers.py
    sj_wightman_floored, rel_floor=1e-10).
    Conventions: Sorkin-Yazdi 1611.10281 -- W = positive part of iDelta;
    W - W^dagger = iDelta, W >= 0 (the Tomita-Takesaki polar data of the SJ
    modular operator live in this positive part). Relative floor
    ``cut = rel_floor * max|lambda|`` for ill-conditioned BD inverses
    (Aslanbeigi-Saravani-Sorkin 1305.2588 smeared object).

    Args:
        iDelta: (N, N) Hermitian Pauli-Jordan operator (from
            ``toe.causet.pauli_jordan``).
        tol: ABSOLUTE magnitude threshold for the positive-eigenvalue cut
            (used when ``rel_floor is None``).
        rel_floor: optional RELATIVE positive-eigenvalue floor; when not None the
            cut becomes ``rel_floor * max|lambda|`` (the ill-conditioned
            BD-inverse convention). Default ``None`` reproduces the absolute-tol
            behaviour exactly.

    Returns:
        SJState with eigvals (ascending), eigvecs, pos_spectrum (descending),
        and the Wightman matrix W.
    """
    iDelta = np.asarray(iDelta)
    w, V = np.linalg.eigh(iDelta)
    if rel_floor is None:
        cut = tol
    else:
        lmax = float(np.max(np.abs(w))) if w.size else 0.0
        cut = rel_floor * lmax
    pos = w > cut
    lam = w[pos]
    Vp = V[:, pos]
    W = (Vp * lam) @ Vp.conj().T
    pos_spectrum = np.sort(lam)[::-1]
    return SJState(eigvals=w, eigvecs=V, pos_spectrum=pos_spectrum, W=W)


def wightman(iDelta, *, tol=1e-12, rel_floor=None):
    """SJ Wightman matrix ``W`` (positive spectral part of ``iDelta``).

    Convenience wrapper around :func:`sj_state` returning just ``W``.

    Formula: pauli-jordan, modular-polar-decomposition.
    Evidence: VYPOCET-12 (sj-vn-type/calc.py sj_wightman_from_eig).
    Conventions: Sorkin-Yazdi 1611.10281 -- W = positive part of iDelta.

    Args:
        iDelta: (N, N) Hermitian Pauli-Jordan operator.
        tol: ABSOLUTE positive-eigenvalue threshold (used when rel_floor None).
        rel_floor: optional RELATIVE floor ``rel_floor * max|lambda|`` for
            ill-conditioned BD-inverse objects. Default None = absolute tol.

    Returns:
        np.ndarray (N, N) complex -- the SJ Wightman matrix W.
    """
    return sj_state(iDelta, tol=tol, rel_floor=rel_floor).W


# ===========================================================================
# v0.3.0 -- SPARSE/ITERATIVE SJ STATE  (top-k spectral part at large N)
# ===========================================================================

@dataclass
class SJStateSparse:
    """Carrier for the TOP-k spectral part of a Sorkin-Johnston state.

    The sparse sibling of :class:`SJState`: instead of the full ``(N, N)``
    Wightman matrix it holds only the ``k`` eigenpairs of ``iDelta`` largest in
    MAGNITUDE (the dominant ``+/-`` paired modes), from which the truncated SJ
    Wightman / SSEE content is reconstructed on demand. By the ``+/-`` pairing the
    ``k`` returned modes split into the top ``~k/2`` positive and top ``~k/2``
    negative eigenvalues; ``pos_spectrum`` exposes the positive half (sorted
    descending), which is exactly the part SSEE keeps above the ``kappa`` cutoff.

    Field shapes match the dense :class:`SJState` where they overlap
    (``eigvals``/``eigvecs``/``pos_spectrum``), so downstream code can branch on
    type without reshaping. ``W`` is intentionally NOT materialised (it would be
    the dense ``N x N`` object the sparse path avoids); call
    :func:`toe.entropy.ssee_sparse` to get the truncated entropy from the modes.

    Conventions: Sorkin-Yazdi 1611.10281; W = positive part of iDelta. The k
    captured modes carry the full ``|lambda| > kappa`` content whenever
    ``k > 2 * #{|lambda| > kappa}`` (checked by the caller / tests).
    """

    eigvals: np.ndarray        # k eigenvalues of iDelta (ascending)
    eigvecs: np.ndarray        # (N, k) corresponding eigenvectors (columns)
    pos_spectrum: np.ndarray   # positive subset of eigvals, sorted descending
    k: int                     # number of captured modes
    which: str = "LM"          # eigsh selection rule used


def sj_state_sparse(idelta_op, k, *, rng, which="LM", tol=0, maxiter=None,
                    ncv=None):
    """Top-k Sorkin-Johnston spectral data from a matrix-FREE ``iDelta`` operator.

    Computes the ``k`` eigenpairs of the Hermitian Pauli-Jordan operator
    ``idelta_op`` (a ``scipy.sparse.linalg.LinearOperator``, e.g. from
    :func:`toe.causet.idelta_operator_2d`) largest in MAGNITUDE via
    ``scipy.sparse.linalg.eigsh(which='LM')``, WITHOUT materialising a dense
    iDelta. Because the iDelta spectrum is exactly ``+/-`` paired, ``which='LM'``
    returns a balanced set of the top ``~k/2`` positive and top ``~k/2`` negative
    eigenvalues -- i.e. the dominant SJ positive modes plus their negative
    partners, which is all the SSEE truncation (``|lambda| > kappa``) needs. The
    returned :class:`SJStateSparse` has the same ``eigvals`` / ``eigvecs`` /
    ``pos_spectrum`` shape as the dense :class:`SJState` top slice.

    DETERMINISM: ``eigsh`` is seeded by the starting vector ``v0``, which is
    derived deterministically from ``rng`` (a ``numpy.random.Generator``,
    REQUIRED): ``v0 = rng.standard_normal(N) + 1j rng.standard_normal(N)``. Two
    calls with equal-seed generators give bit-identical spectra (proven in the
    v0.3.0 tests), so restarts are reproducible.

    PRECISION: with a ``float64`` operator the top-k eigenvalues agree with the
    dense ``eigh`` top-k to ~1e-14 relative (overlap validation); a ``float32``
    operator is ~1e-6-1e-7 (large-N scaling smoke only).

    Formula: pauli-jordan, modular-polar-decomposition.
    Evidence: VYPOCET-12 (sj-vn-type/calc.py sj_wightman_from_eig) -- iterative
    top-k variant added in v0.3.0 for the large-N SPARSE path (H5g-2 A/4 cap,
    VYPOCET-19 Part-3 tracial probe).
    Conventions: Sorkin-Yazdi 1611.10281 -- W = positive part of iDelta; the SJ
    positive modes are the ``lambda > 0`` half of the ``+/-`` paired spectrum, so
    the top-k-by-magnitude set captures them symmetrically.

    Args:
        idelta_op: Hermitian ``scipy.sparse.linalg.LinearOperator`` realising
            ``iDelta`` (shape ``(N, N)``, ``dtype=complex128``).
        k: number of eigenpairs to extract (``few x N^{3/4}``; choose
            ``k > 2 * #{|lambda| > kappa}`` so the SSEE content is complete).
        rng: ``numpy.random.Generator`` (REQUIRED) seeding the deterministic
            ``eigsh`` starting vector ``v0``.
        which: ``eigsh`` selection rule (default ``"LM"`` -- largest magnitude;
            the right choice for the ``+/-`` paired iDelta spectrum).
        tol: ``eigsh`` convergence tolerance (``0`` = machine precision, used by
            the float64 overlap validation; loosen to ~1e-9 for the float32
            large-N smoke).
        maxiter: optional ``eigsh`` iteration cap (default None = scipy default).
        ncv: optional Lanczos basis size (default None = scipy default).

    Returns:
        SJStateSparse with eigvals (ascending), eigvecs ((N, k) columns),
        pos_spectrum (positive eigenvalues, descending), k, and which.
    """
    from scipy.sparse.linalg import eigsh

    N = idelta_op.shape[0]
    k = int(k)
    if k >= N:
        raise ValueError(
            f"sparse top-k needs k < N (got k={k}, N={N}); use the dense "
            f"sj_state for k close to N."
        )
    # Deterministic eigsh start vector from the explicit rng.
    v0 = rng.standard_normal(N) + 1j * rng.standard_normal(N)

    vals, vecs = eigsh(idelta_op, k=k, which=which, v0=v0, tol=tol,
                       maxiter=maxiter, ncv=ncv)
    order = np.argsort(vals)             # ascending, like np.linalg.eigh
    vals = vals[order]
    vecs = vecs[:, order]
    pos_spectrum = np.sort(vals[vals > 0])[::-1]
    return SJStateSparse(eigvals=vals, eigvecs=vecs, pos_spectrum=pos_spectrum,
                         k=k, which=which)


# ===========================================================================
# DIRECTIONAL ASYMMETRIES OVER CAUSAL LINKS  (frame dragging / superradiance)
# ===========================================================================

def _causal_pairs(C):
    """Indices ``(xi, yi)`` of all causally-related ordered pairs ``C[x, y] > 0``
    (x in the causal future of y)."""
    return np.where(np.asarray(C) > 0)


def asymmetry_causal(coords, C, *, axis=1):
    """Causal directional asymmetry ``A_caus = 2 f_co - 1`` of the SJ region.

    Over all causally-related ordered pairs (``x`` in the causal future of
    ``y``) record the advance ``d = coord_x[axis] - coord_y[axis]`` along the
    chosen spatial axis (the azimuth phi). ``f_co`` is the fraction of links with
    ``d > 0`` (co-rotating). In a static section the cone is symmetric so
    ``f_co = 1/2`` and ``A_caus = 0``; frame dragging tilts the cone toward
    ``+phi`` so ``A_caus > 0``, reaching ``+1`` inside a fully-dragged ergoregion
    (every causal link co-rotates).

    Formula: pauli-jordan.
    Evidence: VYPOCET-08 (core-data/calculations/sj-rotating-btz/calc.py
    two_point_profile, causal_asymmetry); VYPOCET-09 (sj-kerr-equatorial).
    Conventions: A_caus = 2 f_co - 1 in [-1, 1]; 0 = static, +1 = fully
    co-rotating (Sorkin-Yazdi 1611.10281 causal order).

    Args:
        coords: (N, dim) sprinkled coordinates; column 0 is time.
        C: (N, N) causal matrix (C[x, y] = 1 iff y precedes x).
        axis: coordinate column of the azimuth phi (default 1).

    Returns:
        Measurement with value = A_caus, n = number of causal links. ``se`` is
        the binomial std-error of ``2 f_co - 1`` over the links; the caller
        aggregates across seeds for a cross-seed SE.
    """
    coords = np.asarray(coords, dtype=np.float64)
    xi, yi = _causal_pairs(C)
    n_links = int(len(xi))
    if n_links == 0:
        return Measurement(value=float("nan"), se=0.0, n=0)
    dphi = coords[xi, axis] - coords[yi, axis]
    f_co = float(np.mean(dphi > 0))
    A_caus = 2.0 * f_co - 1.0
    # binomial SE of f_co propagated to A_caus = 2 f_co - 1
    se = 2.0 * np.sqrt(max(f_co * (1.0 - f_co), 0.0) / n_links)
    return Measurement(value=float(A_caus), se=float(se), n=n_links)


def asymmetry_wightman(W, coords, C, *, axis=1):
    """SJ Wightman directional asymmetry
    ``A_W = (m_co - m_counter) / (|m_co| + |m_counter|)``.

    Over the same causally-related pairs, compare the MEAN SJ two-point
    correlation ``Re W(x, y)`` per link in the co-rotating (``dphi > 0``) vs
    counter-rotating (``dphi < 0``) direction. ``A_W`` probes whether the
    quantum correlations of the SJ vacuum inherit the dragging bias.

    Inside a fully-dragged ergoregion there are NO counter-rotating links, so
    ``A_W`` is undefined -- the returned ``Measurement.value`` is ``NaN`` (the
    sj-rotating-btz convention stores ``None`` here). Outside the ergoregion
    ``A_caus > 0`` but ``A_W < 0`` (the documented opposite-sign phenomenon).

    Formula: pauli-jordan, modular-flow-def.
    Evidence: VYPOCET-08 (sj-rotating-btz/calc.py two_point_profile,
    wightman_asymmetry); VYPOCET-14/15 (sj-eigenvector-superradiance toy model).
    Conventions: A_W = (m_co - m_counter) / (|m_co| + |m_counter|); NaN when the
    region is fully dragged (no counter-rotating causal links).

    Args:
        W: (N, N) SJ Wightman matrix.
        coords: (N, dim) sprinkled coordinates; column 0 is time.
        C: (N, N) causal matrix.
        axis: coordinate column of the azimuth phi (default 1).

    Returns:
        Measurement with value = A_W (NaN if fully dragged), n = number of
        causal links.
    """
    coords = np.asarray(coords, dtype=np.float64)
    W = np.asarray(W)
    xi, yi = _causal_pairs(C)
    n_links = int(len(xi))
    if n_links == 0:
        return Measurement(value=float("nan"), se=0.0, n=0)
    dphi = coords[xi, axis] - coords[yi, axis]
    ReW = np.real(W[xi, yi])
    co = dphi > 0
    cc = dphi < 0
    if np.any(co) and np.any(cc):
        m_co = float(np.mean(ReW[co]))
        m_cc = float(np.mean(ReW[cc]))
        denom = abs(m_co) + abs(m_cc)
        A_W = (m_co - m_cc) / denom if denom > 0 else 0.0
    else:
        A_W = float("nan")   # fully dragged: no counter-rotating causal links
    return Measurement(value=float(A_W), se=0.0, n=n_links)


# ===========================================================================
# SUPERRADIANT EIGENVECTOR-OVERLAP WEIGHT
# ===========================================================================

def _occupation_map(coords, lam, Vp, ws, ks):
    """``P(w, k) = sum_modes lambda |<plane(w, k) | v>|^2`` normalized to sum 1.

    ``<plane | v> = (1/N) sum_n exp(+i w t_n - i k phi_n) v_n`` -- the
    Monte-Carlo L2 inner product of the plane wave ``e^{-i w t + i k phi}`` with
    each SJ positive eigenvector on the uniform sprinkle (occupation map of the
    positive-SJ subspace)."""
    t = coords[:, 0]
    ph = coords[:, 1]
    N = coords.shape[0]
    P = np.zeros((len(ws), len(ks)))
    for iw, wo in enumerate(ws):
        eiwt = np.exp(1j * wo * t)
        for ik, ko in enumerate(ks):
            pw = eiwt * np.exp(-1j * ko * ph)        # conj of e^{-iwt + ikphi}
            proj = (pw[None, :] @ Vp)[0] / N          # (n_modes,)
            P[iw, ik] = np.sum(lam * np.abs(proj) ** 2)
    tot = P.sum()
    return P / tot if tot > 0 else P


def superradiant_weight(coords, iDelta, *, omega, ws, ks, seed):
    """Weight of the SJ positive subspace inside the superradiant wedge
    ``w(w - k Omega) < 0``.

    Project the SJ positive eigenvectors of ``iDelta`` onto plane waves
    ``e^{-i w t + i k phi}`` (Monte-Carlo L2 overlap on the sprinkle), build the
    normalized (w, k) OCCUPATION MAP ``P(w, k) = sum_modes lambda
    |<plane | v>|^2``, and sum the weight that lands in the superradiant wedge
    ``w(w - k Omega) < 0`` (the co-rotating frequency ``w - k Omega`` has the
    opposite sign to ``w``). The static control ``Omega = 0`` has a measure-zero
    wedge so the weight is exactly zero; the weight grows monotonically with
    spin / drag ``Omega``.

    Formula: pauli-jordan, modular-flow-def.
    Evidence: VYPOCET-14/15 (core-data/calculations/sj-eigenvector-superradiance/
    calc.py occupation_map + superradiance_weights).
    Conventions: plane wave ``e^{-i w t + i k phi}``; overlap
    ``(1/N) sum exp(+i w t - i k phi) v_n``; superradiant wedge
    ``w(w - k Omega) < 0`` with the ZAMO/LNRF angular velocity
    ``Omega = -g_tphi / g_phiphi`` (the frame-drag slope).

    Args:
        coords: (N, dim) sprinkled coordinates; column 0 = t, column 1 = phi.
        iDelta: (N, N) Hermitian Pauli-Jordan operator on those coords.
        omega: frame-drag angular velocity Omega = -g_tphi / g_phiphi.
        ws: 1D array of frequencies w for the occupation grid.
        ks: 1D array of azimuthal numbers k for the occupation grid.
        seed: RNG seed (REQUIRED). It is not used to resample (the occupation
            map is deterministic given the coords/iDelta); it is recorded for
            provenance and reproducibility of the calling driver.

    Returns:
        Measurement with value = superradiant-wedge weight (>= 0), n = number of
        SJ positive modes. ``se = 0`` for the single map; the caller averages
        over seeds for the cross-seed SE.
    """
    # seed is required by contract for provenance; the map is deterministic in
    # (coords, iDelta), so we only record it (np.random.default_rng(seed) is the
    # caller's sprinkle source).
    _ = np.random.default_rng(seed)
    coords = np.asarray(coords, dtype=np.float64)
    ws = np.asarray(ws, dtype=np.float64)
    ks = np.asarray(ks, dtype=np.float64)

    st = sj_state(iDelta)
    lam = st.eigvals[st.eigvals > 1e-9]
    Vp = st.eigvecs[:, st.eigvals > 1e-9]
    P = _occupation_map(coords, lam, Vp, ws, ks)

    WW, KK = np.meshgrid(ws, ks, indexing="ij")
    superrad = WW * (WW - KK * omega) < 0
    sr = float(P[superrad].sum())
    return Measurement(value=sr, se=0.0, n=int(Vp.shape[1]))


# ===========================================================================
# POSITIVE-SUBSPACE (PRINCIPAL-ANGLE) OVERLAP
# ===========================================================================

def positive_subspace_overlap(iDeltaA, iDeltaB):
    """Mean ``cos^2`` of the principal angles between two SJ positive subspaces.

    Builds the SJ positive eigenvector bases ``V_A``, ``V_B`` of ``iDeltaA`` and
    ``iDeltaB`` and measures the principal-angle overlap of the two subspaces via
    the singular values of ``V_A^dagger V_B`` -- ``1`` for identical subspaces,
    ``-> 0`` for orthogonal ones. This isolates WHERE rotation lives: when two
    sections share a sprinkle and have nearly identical SJ eigenvalue spectra,
    the positive subspaces can still be strongly rotated (rotation lives in the
    eigenVECTORS). Self-overlap of a subspace with itself is exactly ``1``.

    Formula: pauli-jordan, modular-flow-def.
    Evidence: VYPOCET-14/15 (core-data/calculations/sj-eigenvector-superradiance/
    calc.py subspace_overlap); cross-checked against the committed
    ``sanity_static_vs_static_mean_cos2 = 1.0000000000000002``.
    Conventions: mean cos^2 of the principal angles = mean of the squared
    singular values of the cross-overlap matrix V_A^dagger V_B (truncated to the
    smaller subspace dimension).

    Args:
        iDeltaA: (N, N) Hermitian Pauli-Jordan operator (subspace A).
        iDeltaB: (N, N) Hermitian Pauli-Jordan operator (subspace B). Must act
            on the SAME sprinkle (same N) as A.

    Returns:
        Measurement with value = mean cos^2 of the principal angles in [0, 1],
        n = min(dim A, dim B) (the number of compared principal angles).
    """
    stA = sj_state(iDeltaA)
    stB = sj_state(iDeltaB)
    VA = stA.eigvecs[:, stA.eigvals > 1e-9]
    VB = stB.eigvecs[:, stB.eigvals > 1e-9]
    k = min(VA.shape[1], VB.shape[1])
    S = VA.conj().T @ VB
    sv = np.linalg.svd(S, compute_uv=False)
    mean_cos2 = float(np.mean(sv[:k] ** 2)) if k > 0 else float("nan")
    return Measurement(value=mean_cos2, se=0.0, n=int(k))
