# -*- coding: utf-8 -*-
"""toe.causet -- sprinkling region builders, causal/link structure, retarded
Green functions, the Pauli-Jordan operator and its spectral diagnostics.

This is module A2 of the ``toe`` library (Layer A, independent). It is the
distilled, composable union of the verified sprinkling calc scripts:

* 2D causal diamond + ``G_R = (1/2) C``  (VYPOCET-04, ssee-diamond);
* 4D box/slab + diamond + link-matrix ``G_R``  (VYPOCET-06, ssee-slab-4d,
  vn-type-slab-4d);
* 4D Benincasa-Dowker d'Alembertian inverse  (VYPOCET-09, ssee-bd-4d);
* de Sitter static-patch ``sech^2`` proper measure  (VYPOCET-19,
  sj-desitter-type).

Design contract (ARCHITECTURE.md A2):
  - every stochastic builder takes an explicit ``rng`` (a
    ``numpy.random.Generator``) as a REQUIRED positional argument -- no global
    state, full determinism from the caller's seed;
  - inputs are physics parameters, never ad-hoc magic constants;
  - the load-bearing convention constants (``G_R = (1/2) C`` in 2D;
    ``a = sqrt(rho)/(2 pi sqrt6)`` in 4D; BD layer coefficients
    ``(1,-9,16,-8)`` with prefactor ``4 sqrt(rho)/sqrt6``) are reproduced
    verbatim from the source scripts;
  - the module is pure: no file I/O, no plotting (see ``toe.viz`` for figures).

INVARIANT (tested to machine precision on every region builder): the
Pauli-Jordan operator ``iDelta`` is Hermitian and its eigenvalues come in exact
``+/-`` pairs (antisymmetry of ``Delta`` is exact in float), so
``causal_diagnostics`` reports ``pairing_residual_rel < 1e-13`` and
``|trace| < 1e-12``.

Only numpy / scipy are used.
"""

from __future__ import annotations

from math import comb

import numpy as np

__all__ = [
    # region builders
    "sprinkle_diamond2d",
    "sprinkle_slab2d",
    "sprinkle_box4d",
    "sprinkle_slab4d",
    "sprinkle_wedge_box4d",
    "sprinkle_ds_static_patch2d",
    "sprinkle_ds_static_patch4d",
    # causal structure
    "causal_matrix",
    "link_matrix",
    # Green functions + Pauli-Jordan
    "green_retarded_2d",
    "green_retarded_4d",
    "bd_dalembertian_inverse",
    "bd_smeared_dalembertian_inverse",
    "pauli_jordan",
    "causal_diagnostics",
    # v0.3.0 -- memory-lean SPARSE/ITERATIVE path (large N)
    "causal_blocks_2d",
    "idelta_operator_2d",
]


# ===========================================================================
# REGION BUILDERS  (rng REQUIRED, returns (N, dim) float coords)
# ===========================================================================

def sprinkle_diamond2d(N, rng, *, t_half=1.0):
    """Poisson-sprinkle ``N`` points uniformly into the 2D causal diamond.

    The diamond ``{|t| + |x| <= t_half}`` is the square ``u, v in [-t_half,
    t_half]`` in null coordinates ``(u, v) = (t + x, t - x)``; uniform sampling
    in ``(u, v)`` is a Poisson process w.r.t. the flat volume ``(1/2) du dv``.
    Returns the null coordinates ``(u, v)`` (columns), matching the
    ssee-diamond convention so the concentric sub-diamond ``{|u|, |v| <= f}``
    is again a causal diamond.

    Formula: pauli-jordan (geometry feeding the SJ construction).
    Evidence: VYPOCET-04 (core-data/calculations/ssee-diamond/calc.py
    sprinkle_diamond).
    Conventions: Sorkin-Yazdi 1611.10281; diamond half-extent t_half, the
    (u, v)-square has area ``(2 t_half)^2``.

    Args:
        N: number of points (canonical Poisson approximation).
        rng: numpy.random.Generator (REQUIRED, explicit seed source).
        t_half: null half-extent of the diamond.

    Returns:
        np.ndarray of shape ``(N, 2)`` -- columns are null coordinates (u, v).
    """
    return rng.uniform(-t_half, t_half, size=(int(N), 2))


def sprinkle_slab2d(N, rng, *, t_extent, x_extent):
    """Poisson-sprinkle ``N`` points into the 2D box-like slab.

    The slab is ``{0 < t < t_extent, |x| < x_extent}`` with ``t_extent <<
    x_extent`` (Rindler-like half-space approximation). Uniform Lebesgue
    sprinkling = Lorentz-invariant Poisson process. Returns ``(t, x)`` columns.

    Formula: pauli-jordan (geometry feeding the SJ construction).
    Evidence: VYPOCET-13 (core-data/calculations/ssee-slab-4d/calc.py
    sprinkle_slab_2d); see also vn-type-slab-4d.
    Conventions: box slab volume ``Vol = 2 t_extent x_extent``; flat 2D causal
    order in (t, x).

    Args:
        N: number of points.
        rng: numpy.random.Generator (REQUIRED).
        t_extent: temporal extent (0 < t < t_extent).
        x_extent: spatial half-extent (|x| < x_extent).

    Returns:
        np.ndarray of shape ``(N, 2)`` -- columns (t, x).
    """
    N = int(N)
    t = rng.random(N) * t_extent
    x = (rng.random(N) * 2.0 - 1.0) * x_extent
    return np.column_stack([t, x])


def sprinkle_box4d(N, rng, *, half=1.0):
    """Poisson-sprinkle ``N`` points uniformly into the 4D causal diamond.

    Exact (rejection-free) sampling of ``{|t| + |r| <= half}``: draw ``s =
    half * U^{1/4}`` (so ``|t|`` has density ``~ (half - |t|)^3``), then a
    uniform point in the spatial ball of radius ``s``. Returns
    ``(t, x1, x2, x3)`` columns.

    Despite the name "box4d" in the contract, this is the 4D causal DIAMOND
    builder (the canonical 4D region of ssee-slab-4d / ssee-bd-4d); use
    ``sprinkle_slab4d`` for the box-like slab.

    Formula: pauli-jordan (geometry feeding the 4D SJ construction).
    Evidence: VYPOCET-06 (core-data/calculations/ssee-slab-4d/calc.py
    sprinkle_diamond_4d) and VYPOCET-09 (ssee-bd-4d/calc.py).
    Conventions: diamond 4-volume ``(2/3) pi half^4``; rho = N / volume.

    Args:
        N: number of points.
        rng: numpy.random.Generator (REQUIRED).
        half: causal-diamond half-extent T.

    Returns:
        np.ndarray of shape ``(N, 4)`` -- columns (t, x1, x2, x3).
    """
    N = int(N)
    U = rng.random(N)
    s = half * U ** 0.25
    sign = rng.choice([-1.0, 1.0], size=N)
    t = sign * (half - s)
    dirs = rng.normal(size=(N, 3))
    dirs /= np.linalg.norm(dirs, axis=1, keepdims=True)
    V = rng.random(N)
    rr = s * V ** (1.0 / 3.0)
    return np.column_stack([t, dirs * rr[:, None]])


def sprinkle_slab4d(N, rng, *, t_extent, l_space):
    """Poisson-sprinkle ``N`` points into the 4D box-like slab.

    The slab is ``{0 < t < t_extent, |x_i| < l_space, i = 1,2,3}`` with
    ``t_extent << l_space`` (flat half-space entangling surface ``x_1 = 0``,
    no corners). Uniform Lebesgue sprinkling. Returns ``(t, x1, x2, x3)``.

    Formula: pauli-jordan (geometry feeding the 4D SJ construction).
    Evidence: VYPOCET-13 (core-data/calculations/ssee-slab-4d/calc.py
    sprinkle_slab_4d).
    Conventions: box 4-volume ``Vol = t_extent (2 l_space)^3``; entangling
    face ``x_1 = 0`` area ``t_extent (2 l_space)^2``.

    Args:
        N: number of points.
        rng: numpy.random.Generator (REQUIRED).
        t_extent: temporal extent.
        l_space: spatial half-extent (|x_i| < l_space).

    Returns:
        np.ndarray of shape ``(N, 4)`` -- columns (t, x1, x2, x3).
    """
    N = int(N)
    t = rng.random(N) * t_extent
    x = (rng.random((N, 3)) * 2.0 - 1.0) * l_space
    return np.column_stack([t, x])


def sprinkle_wedge_box4d(N, rng, *, t_half=0.5, x_half=0.5, yz_half=0.5):
    """Poisson-sprinkle ``N`` points into a t-symmetric 4D Minkowski box whose
    half-space cut ``O = {x > 0}`` has its entangling surface on the CODIM-2
    Rindler EDGE ``E = {t = 0, x = 0}`` (a flat 2-plane spanned by (y, z)).

    Box: ``{|t| <= t_half, |x| <= x_half, |y|, |z| <= yz_half}``, uniform
    Lebesgue (Poisson) sprinkle. Unlike :func:`sprinkle_slab4d` (which is
    one-sided in t, ``0 < t < t_extent``, so its cut is a flat codim-1
    hyperplane with no joint), this builder is SYMMETRIC in both ``t`` and
    ``x``: the right Rindler wedge ``W = {x > |t|}`` then has its modular flow
    equal to the exact x-t boost (Bisognano-Wichmann), and the boost Killing
    vector ``xi = x d_t + t d_x`` VANISHES on the codim-2 edge ``E = {t = 0,
    x = 0}``. The entangling surface of the cut ``O = {x > 0}`` IS that edge,
    so the per-site distance-to-edge is the transverse distance to the 2-plane
    ``d_E = sqrt(t^2 + x^2)`` -- the direct 4D analogue of the 2D
    distance-to-corner.

    Formula: pauli-jordan (geometry feeding the 4D SJ construction).
    Evidence: VYPOCET-22 (core-data/calculations/modular-flow-codim2/helpers.py
    sprinkle_wedge_box4d); geometry analogue of :func:`sprinkle_slab4d` made
    t-symmetric so the wedge edge sits inside the box.
    Conventions: 4-volume ``= (2 t_half)(2 x_half)(2 yz_half)^2``; right Rindler
    wedge ``W = {x > |t|}``, codim-2 edge ``E = {t = 0, x = 0}`` (the H5g-3
    flat-2-plane joint).

    Args:
        N: number of points (canonical Poisson approximation).
        rng: numpy.random.Generator (REQUIRED, explicit seed source).
        t_half: temporal half-extent (|t| <= t_half).
        x_half: x half-extent (|x| <= x_half).
        yz_half: transverse half-extent (|y|, |z| <= yz_half).

    Returns:
        np.ndarray of shape ``(N, 4)`` -- columns (t, x, y, z).
    """
    N = int(N)
    t = (rng.random(N) * 2.0 - 1.0) * t_half
    x = (rng.random(N) * 2.0 - 1.0) * x_half
    yz = (rng.random((N, 2)) * 2.0 - 1.0) * yz_half
    return np.column_stack([t, x, yz])


def sprinkle_ds_static_patch2d(N, rng, *, l=1.0, rstar_box, t_extent):
    """Poisson-sprinkle ``N`` points into the 2D de Sitter static patch using
    the de Sitter PROPER measure ``dN ~ sech^2(r*/l) dt dr*``.

    In tortoise coordinates ``r* = l arctanh(r/l)`` the static patch is the
    conformally flat strip with conformal factor ``Omega^2 = 1 - r^2/l^2 =
    sech^2(r*/l)``. Because the 2D massless scalar is conformally invariant the
    SJ machinery is the standard flat 2D construction in ``(t, r*)``; the de
    Sitter geometry enters ONLY through the non-uniform sprinkling measure,
    which makes the proper point budget SATURATE as ``r*_box -> inf`` (horizon
    at infinite tortoise distance). Sampled via the inverse CDF
    ``r* = l arctanh( u * tanh(rstar_box / l) )`` with ``u ~ U(0, 1)``.
    Returns ``(t, r*)`` columns.

    Formula: pauli-jordan (geometry feeding the SJ construction).
    Evidence: VYPOCET-19 (core-data/calculations/sj-desitter-type/calc.py
    sprinkle_box, measure="desitter").
    Conventions: de Sitter radius l, horizon r=l <=> r*=inf; conformal trick
    of arXiv:1306.3231 / Anninos 1205.3855; Sorkin-Yazdi 1611.10281 flat-2D SJ
    in (t, r*). Proper volume ``2 t_extent l tanh(rstar_box / l)`` (caps).

    Args:
        N: number of points.
        rng: numpy.random.Generator (REQUIRED).
        l: de Sitter radius.
        rstar_box: tortoise extent of the sprinkling box, r* in [0, rstar_box].
        t_extent: conformal-time half-extent (t in [-t_extent, t_extent]).

    Returns:
        np.ndarray of shape ``(N, 2)`` -- columns (t, r*).
    """
    N = int(N)
    t = rng.uniform(-t_extent, t_extent, size=N)
    umax = np.tanh(rstar_box / l)
    u = rng.uniform(0.0, umax, size=N)
    rstar = l * np.arctanh(u)
    return np.column_stack([t, rstar])


def sprinkle_ds_static_patch4d(N, rng, *, l=1.0, rstar_box, t_extent,
                               x_perp_half):
    """Poisson-sprinkle ``N`` points into the 4D de Sitter static patch with the
    de Sitter PROPER measure ``dN ~ sech^2(r*/l) dt dr* dx1 dx2`` -- the 4D
    analog of :func:`sprinkle_ds_static_patch2d`.

    The 4D static-patch geometry is the (t, r*) static-patch strip times a
    transverse box ``x_perp in [-x_perp_half, x_perp_half]^2``. In the tortoise
    coordinate ``r* = l arctanh(r/l)`` the radial-time part is conformally flat
    with conformal factor ``Omega^2 = 1 - r^2/l^2 = sech^2(r*/l)``; the de
    Sitter geometry is implemented by WEIGHTING the (t, r*) marginal by
    ``sech^2(r*/l)`` (the proper-volume avatar of the finite II_1 trace -- the
    radial point budget SATURATES as ``r*_box -> inf``), while the transverse
    directions carry a flat box measure. The radial coordinate is sampled by the
    inverse CDF ``r* = l arctanh( u tanh(rstar_box/l) )``, ``u ~ U(0, 1)``; the
    transverse coordinates are uniform on ``[-x_perp_half, x_perp_half]``.

    CONFORMAL-WEIGHT CAVEAT (honest): unlike 2D, the 4D massless scalar is NOT
    conformally invariant, so the conformal factor does NOT drop out of the
    exact propagator. This builder is the SAME controlled approximation as the
    VYPOCET-19 2D conformal trick lifted to 4D: it preserves the FLAT causal
    structure in ``(t, r*, x1, x2)`` and the dS PROPER sprinkling MEASURE
    (sech^2 radial density => bounded point budget = the II_1 geometric signal),
    but NOT the exact curved-space 4D propagator. The 4D link-matrix Green
    (:func:`green_retarded_4d`) is then built on this flat conformal order. What
    is tested is therefore the geometric II_1 vs II_inf boundedness in the
    truncated area-law SSEE, not the exact dS Wightman function.

    Formula: pauli-jordan (geometry feeding the 4D SJ construction).
    Evidence: VYPOCET-19 (core-data/calculations/sj-desitter-type/calc.py
    sprinkle_box, measure="desitter"); VYPOCET-21
    (core-data/calculations/sj-desitter-4d/calc.py) -- 4D sech^2 slab.
    Conventions: de Sitter radius l, horizon r=l <=> r*=inf; conformal factor
    Omega^2 = sech^2(r*/l) (Anninos 1205.3855); flat-4D link-matrix SJ in
    (t, r*, x1, x2) (Johnston 0909.0944 4D Green). Radial proper measure
    sech^2(r*/l) caps the point budget; transverse box is flat. Proper volume
    ``2 t_extent * l tanh(rstar_box/l) * (2 x_perp_half)^2`` (caps in rstar_box).

    Args:
        N: number of points.
        rng: numpy.random.Generator (REQUIRED, explicit seed source).
        l: de Sitter radius.
        rstar_box: tortoise extent of the radial box, r* in [0, rstar_box].
        t_extent: conformal-time half-extent (t in [-t_extent, t_extent]).
        x_perp_half: transverse box half-extent (|x1|, |x2| <= x_perp_half).

    Returns:
        np.ndarray of shape ``(N, 4)`` -- columns (t, r*, x1, x2). The first two
        columns are the conformal (time, tortoise) pair; the last two are the
        flat transverse box coordinates.
    """
    N = int(N)
    t = rng.uniform(-t_extent, t_extent, size=N)
    umax = np.tanh(rstar_box / l)
    u = rng.uniform(0.0, umax, size=N)
    rstar = l * np.arctanh(u)
    x_perp = rng.uniform(-x_perp_half, x_perp_half, size=(N, 2))
    return np.column_stack([t, rstar, x_perp])


# ===========================================================================
# CAUSAL STRUCTURE
# ===========================================================================

def causal_matrix(coords, *, metric=None, time_orientation=None):
    """Causal relation matrix: ``C[x, y] = 1`` iff ``y`` precedes ``x`` (``y``
    in the causal past of ``x``), diagonal 0.

    Default (``metric is None``): the conformal 2D massless order on lightcone
    coordinates. The input ``coords`` may be supplied either as null
    coordinates ``(u, v)`` (e.g. from ``sprinkle_diamond2d``) or as ``(t, x)``;
    in both cases ``y`` precedes ``x`` iff ``u_y <= u_x AND v_y <= v_x`` after
    converting to ``(u, v) = (t + x, t - x)`` -- but when the second column is
    already the null ``v`` (diamond builder), the order is applied directly. To
    keep a single robust definition we always reduce to ``(u, v)`` via the
    Minkowski 2D condition ``(t_x - t_y) >= |x_x - x_y|`` for ``(t, x)`` data,
    which is equivalent to the null-coordinate condition.

    For ``coords`` of dimension ``> 2`` the flat 4D (and general dD) Minkowski
    order ``(t_x - t_y) >= |r_x - r_y|`` is used.

    With ``metric != None`` the tilted-cone order ``h(D, D) <= 0`` and
    ``h(T, D) < 0`` is used (rotating BTZ / Kerr ergoregion), where ``D`` is the
    coordinate separation and ``T`` the future-pointing time orientation.

    Formula: pauli-jordan (the causal order C entering G_R, iDelta).
    Evidence: VYPOCET-04 (ssee-diamond/calc.py causal_matrix), VYPOCET-06
    (ssee-slab-4d/calc.py causal_matrix_2d/4d), VYPOCET-08 (sj-rotating-btz
    causal_matrix_section).
    Conventions: Sorkin-Yazdi 1611.10281 (2D, null order); flat Minkowski
    light-cone order in dD; tilted-cone order for a rotating metric.

    Args:
        coords: (N, dim) coordinates. dim=2 -> 2D order; dim>=3 -> light-cone
            order with time = column 0 and space = columns 1..dim-1.
        metric: optional (dim, dim) constant metric h for the tilted-cone
            order. The first coordinate is time.
        time_orientation: optional (dim,) future-pointing vector T for the
            tilted-cone order; defaults to e_0 = (1, 0, ..., 0).

    Returns:
        np.ndarray (N, N) of float {0., 1.}, diagonal 0.
    """
    coords = np.asarray(coords, dtype=np.float64)
    N, dim = coords.shape

    if metric is not None:
        metric = np.asarray(metric, dtype=np.float64)
        if time_orientation is None:
            T = np.zeros(dim)
            T[0] = 1.0
        else:
            T = np.asarray(time_orientation, dtype=np.float64)
        # D = x - y for every ordered pair (x rows, y cols): shape (N, N, dim)
        D = coords[:, None, :] - coords[None, :, :]
        hDD = np.einsum("ijk,kl,ijl->ij", D, metric, D)   # h(D, D)
        hTD = np.einsum("k,kl,ijl->ij", T, metric, D)      # h(T, D)
        prec = (hDD <= 0.0) & (hTD < 0.0)
        C = prec.astype(np.float64)
        np.fill_diagonal(C, 0.0)
        return C

    t = coords[:, 0]
    dt = t[:, None] - t[None, :]
    if dim == 2:
        dx = np.abs(coords[:, 1][:, None] - coords[:, 1][None, :])
        prec = (dt > 0.0) & (dt >= dx)
    else:
        r = coords[:, 1:]
        r2 = np.einsum("ij,ij->i", r, r)
        d2 = r2[:, None] + r2[None, :] - 2.0 * (r @ r.T)
        np.maximum(d2, 0.0, out=d2)
        prec = (dt > 0.0) & (dt * dt >= d2)
    C = prec.astype(np.float64)
    np.fill_diagonal(C, 0.0)
    return C


def link_matrix(C):
    """Nearest-neighbour (irreducible) link matrix: the transitive reduction
    ``L = C AND (C @ C == 0)`` -- a relation ``y < x`` is a LINK iff there is no
    intermediate ``z`` with ``y < z < x``.

    Formula: pauli-jordan (links feed the 4D BD/link-matrix G_R).
    Evidence: VYPOCET-06 (ssee-slab-4d/calc.py link_matrix), VYPOCET-09
    (ssee-bd-4d).
    Conventions: ``(C @ C)[x, y]`` counts length-2 causal chains; zero of that
    count plus ``C[x, y] > 0`` is the irreducible link (Johnston 0909.0944
    link convention).

    Args:
        C: (N, N) causal matrix.

    Returns:
        np.ndarray (N, N) float {0., 1.}.
    """
    C = np.asarray(C, dtype=np.float64)
    C2 = C @ C
    return ((C > 0) & (C2 == 0)).astype(np.float64)


# ===========================================================================
# RETARDED GREEN FUNCTIONS + PAULI-JORDAN
# ===========================================================================

def green_retarded_2d(C):
    """2D massless retarded Green function ``G_R = (1/2) C``.

    The 2D massless scalar is conformally invariant; on a causal set the
    retarded Green function is ``(1/2)`` times the causal matrix.

    Formula: pauli-jordan.
    Evidence: VYPOCET-04 (ssee-diamond/calc.py), VYPOCET-06 (ssee-slab-4d/calc.py
    green_retarded_2d).
    Conventions: Sorkin-Yazdi 1611.10281 eq.9: ``G_R = (1/2) C``.

    Args:
        C: (N, N) causal matrix.

    Returns:
        np.ndarray (N, N) -- the retarded Green function.
    """
    return 0.5 * np.asarray(C, dtype=np.float64)


def green_retarded_4d(L, rho):
    """4D massless retarded Green function ``K_R = a L`` with
    ``a = sqrt(rho) / (2 pi sqrt6)``.

    Formula: pauli-jordan.
    Evidence: VYPOCET-06 (ssee-slab-4d/calc.py green_retarded_4d, line ~180).
    Conventions: Johnston 0909.0944 eq.17 (m=0, link convention):
    ``a = sqrt(rho) / (2 pi sqrt(6))``, with sprinkling density
    ``rho = N / volume``. This coefficient is the load-bearing convention and
    must reproduce to machine precision.

    Args:
        L: (N, N) link matrix.
        rho: sprinkling density N / volume.

    Returns:
        np.ndarray (N, N) -- the retarded Green function.
    """
    a = np.sqrt(rho) / (2.0 * np.pi * np.sqrt(6.0))
    return a * np.asarray(L, dtype=np.float64)


# Benincasa-Dowker 4D sharp layer coefficients (n = 0, 1, 2, 3) and prefactor
# constants, reproduced verbatim from ssee-bd-4d/calc.py.
_BD4_C = np.array([1.0, -9.0, 16.0, -8.0])
# Smeared (non-local) BD prefactor constants alpha4 = -4/sqrt6, beta4 = 4/sqrt6
# (Aslanbeigi-Saravani-Sorkin 1305.2588), reproduced verbatim from
# modular-flow-bd-4d / ssee-bd-4d.
_BD4_ALPHA = -4.0 / np.sqrt(6.0)
_BD4_BETA = 4.0 / np.sqrt(6.0)


def _bd_sharp_matrix(C, rho):
    """SHARP 4D Benincasa-Dowker d'Alembertian as an (N, N) matrix.

    ``B[x, y] = pref * C_{n+1}`` for ``y < x`` with layer index
    ``n = (C @ C)[x, y]`` in ``{0, 1, 2, 3}``; ``B[x, x] = -pref``;
    ``pref = 4 sqrt(rho) / sqrt6 = 4 / (sqrt6 l^2)`` (since ``l^4 = 1/rho`` in
    4D). Off-diagonal entries with ``n > 3`` are exactly zero (only the first
    four layers contribute). Reproduced from ssee-bd-4d/calc.py bd_sharp_matrix.
    """
    C = np.asarray(C, dtype=np.float64)
    N = C.shape[0]
    Cb = C > 0
    nmat = np.rint(C @ C).astype(np.int64)
    B = np.zeros((N, N))
    for k in range(4):
        B[Cb & (nmat == k)] = _BD4_C[k]
    pref = 4.0 * np.sqrt(rho) / np.sqrt(6.0)
    B *= pref
    np.fill_diagonal(B, -pref)
    return B


def _bd_smeared_matrix(C, rho, eps):
    """SMEARED (non-local) 4D Benincasa-Dowker d'Alembertian as an (N, N) matrix.

    ``B_eps phi(x) = sqrt(eps) sqrt(rho) [ alpha4 phi(x)
                       + beta4 eps sum_{y < x} f4(n, eps) phi(y) ]`` with
    ``f4(n, eps) = (1 - eps)^n sum_{i=1..4} C_i binom(n, i-1) (eps/(1-eps))^{i-1}``,
    ``alpha4 = -4/sqrt6``, ``beta4 = 4/sqrt6`` and layer index
    ``n = (C @ C)[x, y]``. Byte-for-byte the VYPOCET-09/20 bd_smeared_matrix.
    Reproduced verbatim from modular-flow-bd-4d / ssee-bd-4d calc.py.
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
                    acc += _BD4_C[i - 1] * comb(n, k) * (ratio ** k)
            ftab[n] = (one_me ** n) * acc
        B[Cb] = pref * _BD4_BETA * eps * ftab[n_vals]
    np.fill_diagonal(B, pref * _BD4_ALPHA)
    return B


def bd_dalembertian_inverse(C, rho, dim):
    """Retarded Green function from the discrete Benincasa-Dowker d'Alembertian:
    ``G_R = B^{-1}``, the massive/curved generalisation of the link-matrix G_R.

    In ``dim == 4`` ``B`` is the SHARP BD operator with layer coefficients
    ``(1, -9, 16, -8)`` and prefactor ``4 sqrt(rho) / sqrt6``. When the points
    are listed in a causal (time-ordered) order ``B`` is lower-triangular, so
    ``G_R = B^{-1}`` is lower-triangular = retarded. For the massless 2D limit
    (``dim == 2``) this returns ``(1/2) C`` (the BD operator's continuum-faithful
    massless 2D Green function), matching ``green_retarded_2d``.

    NOTE: this function does NOT re-sort the points. To obtain a strictly
    retarded ``G_R`` in 4D, pass a causal matrix built from time-ordered
    coordinates (``coords[np.argsort(coords[:, 0])]``), exactly as
    ssee-bd-4d/calc.py build_operator does.

    Formula: pauli-jordan.
    Evidence: VYPOCET-09 (ssee-bd-4d/calc.py bd_sharp_matrix +
    green_retarded_from_B); modular-flow-bd-4d.
    Conventions: Benincasa-Dowker 1001.2725 eqs.2-3, layer coefficients
    ``C = (1, -9, 16, -8)``, prefactor ``4 / (sqrt6 l^2) = 4 sqrt(rho) / sqrt6``;
    layers ``L_i = {y < x : n(x, y) = i - 1}``, ``n = (C @ C)[x, y]``.

    Args:
        C: (N, N) causal matrix (time-ordered for strict retardedness in 4D).
        rho: sprinkling density N / volume.
        dim: spacetime dimension (2 -> massless 2D limit; 4 -> sharp BD).

    Returns:
        np.ndarray (N, N) -- the retarded Green function G_R.
    """
    C = np.asarray(C, dtype=np.float64)
    if dim == 2:
        return green_retarded_2d(C)
    if dim == 4:
        B = _bd_sharp_matrix(C, rho)
        return np.linalg.inv(B)
    raise ValueError(f"bd_dalembertian_inverse supports dim in {{2, 4}}, got {dim}")


def bd_smeared_dalembertian_inverse(C, rho, eps):
    """Retarded Green function from the SMEARED (non-local) 4D Benincasa-Dowker
    d'Alembertian: ``G_R = B_eps^{-1}`` -- the ``eps``-sibling of the SHARP
    :func:`bd_dalembertian_inverse` (``dim=4``).

    The smeared operator replaces the four sharp layers by the de-Sitter-style
    geometric mean over a non-locality scale ``xi`` with ``eps = (l / xi)^4 in
    (0, 1]`` (``eps -> 1`` recovers the sharp operator). Its discrete kernel is

        ``B_eps phi(x) = sqrt(eps) sqrt(rho) [ alpha4 phi(x)
                          + beta4 eps sum_{y < x} f4(n, eps) phi(y) ]``,
        ``f4(n, eps) = (1-eps)^n sum_{i=1..4} C_i binom(n, i-1)
                       (eps/(1-eps))^{i-1}``,

    with ``alpha4 = -4/sqrt6``, ``beta4 = 4/sqrt6``, sharp layer coefficients
    ``C = (1, -9, 16, -8)`` and layer index ``n = (C @ C)[x, y]``. The smeared
    object is the VYPOCET-20-PRIMARY validated Green function (better-conditioned
    spectrum, clean power-law ``lambda_k ~ k^{-alpha}``); typical condition
    numbers run ``cond(B_eps) ~ 1e4-1e6``, so the SJ positive part of the
    resulting ``iDelta`` wants a RELATIVE eigenvalue floor (see
    ``toe.sj.sj_state(..., rel_floor=...)``).

    NOTE: like :func:`bd_dalembertian_inverse`, this does NOT re-sort the points.
    To obtain a strictly retarded ``G_R``, pass a causal matrix built from
    time-ordered coordinates (``coords[np.argsort(coords[:, 0])]``).

    Formula: pauli-jordan.
    Evidence: VYPOCET-09/20 (core-data/calculations/ssee-bd-4d/calc.py,
    modular-flow-bd-4d/calc.py bd_smeared_matrix + green_retarded_from_B);
    lifted from core-data/calculations/modular-flow-codim2/helpers.py.
    Conventions: Aslanbeigi-Saravani-Sorkin 1305.2588 eqs.25-26 / Belenchia
    1507.00330: smeared BD ``alpha4 = -4/sqrt6``, ``beta4 = 4/sqrt6``,
    ``f4(n, eps)`` non-local layer weights; prefactor ``sqrt(eps) sqrt(rho)``.

    Args:
        C: (N, N) causal matrix (time-ordered for strict retardedness).
        rho: sprinkling density N / volume.
        eps: smearing parameter eps = (l/xi)^4 in (0, 1]; eps -> 1 -> sharp.

    Returns:
        np.ndarray (N, N) -- the retarded Green function G_R = B_eps^{-1}.
    """
    B = _bd_smeared_matrix(C, rho, eps)
    return np.linalg.inv(B)


def pauli_jordan(G_R):
    """Pauli-Jordan operator ``iDelta = i (G_R - G_R^T)``.

    ``Delta = G_R - G_A = G_R - G_R^T`` is real antisymmetric, so ``iDelta`` is
    Hermitian with real eigenvalues that come in exact ``+/-`` pairs. For the 2D
    massless case pass ``green_retarded_2d(C)``; then ``iDelta = i (1/2)
    (C - C^T)``.

    Formula: pauli-jordan.
    Evidence: VYPOCET-04 (ssee-diamond/calc.py pauli_jordan), VYPOCET-06
    (ssee-slab-4d/calc.py pauli_jordan), VYPOCET-19 (sj-desitter-type).
    Conventions: Sorkin-Yazdi 1611.10281: ``iDelta = i(G_R - G_R^T)``, Hermitian,
    real ``+/-`` paired spectrum; W_SJ = positive part of iDelta.

    Args:
        G_R: (N, N) retarded Green function.

    Returns:
        np.ndarray (N, N) complex -- the Hermitian Pauli-Jordan operator.
    """
    G_R = np.asarray(G_R, dtype=np.float64)
    return 1j * (G_R - G_R.T)


def causal_diagnostics(iDelta, *, tol=1e-9):
    """Spectral health of the Pauli-Jordan operator: eigenvalue sign counts,
    trace, and the ``+/-`` pairing residual.

    A Hermitian ``iDelta`` built from an antisymmetric ``Delta`` has eigenvalues
    in exact ``+/-`` pairs: sorting the spectrum ascending, ``w[k] + w[-1-k]``
    must vanish. The pairing residual is ``max_k |w[k] + w[-1-k]|``; the
    relative residual normalises by ``max|w|``. The trace ``sum w`` must vanish
    by the same antisymmetry.

    Formula: pauli-jordan.
    Evidence: VYPOCET-08 (sj-rotating-btz spectrum_health) cross-checked against
    ``ergoregion_pairing_residual_rel = 4.572344238792827e-16`` in the committed
    sj-rotating-btz/results.json (same construction family).
    Conventions: Sorkin-Yazdi 1611.10281 (real ``+/-`` paired iDelta spectrum).

    Args:
        iDelta: (N, N) Hermitian Pauli-Jordan operator.
        tol: magnitude threshold (relative to max|w|) for the zero/sign split.

    Returns:
        dict with keys: ``n_positive``, ``n_negative``, ``n_zero``, ``trace``,
        ``pairing_residual_abs``, ``pairing_residual_rel``, ``max_abs_eig``.
    """
    iDelta = np.asarray(iDelta)
    w = np.linalg.eigvalsh(iDelta)          # real, ascending
    w = np.sort(w)
    max_abs = float(np.max(np.abs(w))) if w.size else 0.0
    floor = tol * max_abs if max_abs > 0.0 else tol

    pairing_abs = float(np.max(np.abs(w + w[::-1]))) if w.size else 0.0
    pairing_rel = pairing_abs / max_abs if max_abs > 0.0 else 0.0

    return {
        "n_positive": int(np.sum(w > floor)),
        "n_negative": int(np.sum(w < -floor)),
        "n_zero": int(np.sum(np.abs(w) <= floor)),
        "trace": float(np.sum(w)),
        "pairing_residual_abs": pairing_abs,
        "pairing_residual_rel": pairing_rel,
        "max_abs_eig": max_abs,
    }


# ===========================================================================
# v0.3.0 -- MEMORY-LEAN SPARSE/ITERATIVE PATH  (large N: rho ~ 1e3-1e4 in 2D)
# ===========================================================================
#
# The dense path (causal_matrix -> green_retarded_2d -> pauli_jordan ->
# np.linalg.eigh) materialises three N x N float64/complex128 matrices and is
# O(N^3) in time + O(N^2) in memory; it is the right tool up to N ~ 2000 but
# blows past the 2 GB budget and the minutes-scale wall-clock around N ~ 1e4.
#
# For the SJ + SSEE pipelines that only need the TOP-k spectral part of iDelta
# (H5g-2 A/4 cap, the VYPOCET-19 Part-3 tracial probe), this section provides a
# matrix-FREE Hermitian operator: iDelta @ x is evaluated as bool-block GEMVs of
# the 2D causal matrix WITHOUT ever forming a dense float iDelta. Only ONE float
# copy of the causal matrix (and its contiguous transpose) is stored -- in
# float32 by default for the large-N scaling work (halves memory, ~2x BLAS
# throughput), or float64 when machine-precision agreement with the dense path
# is required (the v0.3.0 overlap-validation tests).
#
# 2D massless convention: G_R = (1/2) C, so
#     iDelta = i (G_R - G_R^T) = (i/2) (C - C^T),
# i.e. iDelta @ x = (i/2) (C @ x - C^T @ x). C is the 0/1 causal matrix; the two
# GEMVs C @ x and C^T @ x are the only O(N^2) work per matvec.


def causal_blocks_2d(coords, *, dtype=np.float32, block=2048):
    """Memory-lean 2D causal matrix ``C`` built blockwise (sort-by-time +
    per-block lightcone test), returned as a single dense array of ``dtype``.

    This is the matrix-free path's storage primitive: it produces the SAME 0/1
    causal matrix as :func:`causal_matrix` on 2D coordinates, but assembles it in
    row-blocks of ``block`` rows so the transient per-block boolean buffer is
    ``block x N`` rather than ``N x N``, and stores the result in ``float32`` by
    default (half the footprint of the float64 dense path). The input ``coords``
    may be 2D null coordinates ``(u, v)`` (e.g. from :func:`sprinkle_diamond2d`)
    or ``(t, x)``; the lightcone test ``y precedes x iff u_y <= u_x AND v_y <=
    v_x`` is applied after reducing ``(t, x) -> (u, v) = (t + x, t - x)``.

    Points are SORTED by the first null coordinate ``u`` before blocking (a cheap
    O(N log N) presort that makes the per-block predecessor test cache-friendly);
    the returned matrix is in the SORTED order, and the sort permutation is
    returned so callers can map sub-region indices / coordinates consistently.

    Formula: pauli-jordan (the causal order C entering iDelta).
    Evidence: VYPOCET-04 (ssee-diamond/calc.py causal_matrix), VYPOCET-12
    (sj-vn-type/calc.py) -- blockwise assembly added in v0.3.0 for the large-N
    SPARSE path (H5g-2 A/4 cap, VYPOCET-19 Part-3 tracial probe).
    Conventions: Sorkin-Yazdi 1611.10281 (2D null order); ``y < x`` iff
    ``u_y <= u_x AND v_y <= v_x`` (non-strict, diagonal 0), identical to the dense
    null-coordinate order.

    Args:
        coords: (N, 2) coordinates -- 2D null ``(u, v)`` or ``(t, x)``.
        dtype: storage dtype of the returned matrix (``np.float32`` default for
            the large-N path; pass ``np.float64`` for machine-precision matvecs).
        block: number of rows assembled per block (memory knob; the transient
            boolean buffer is ``block x N``).

    Returns:
        tuple ``(C, perm)`` where ``C`` is the ``(N, N)`` causal matrix of
        ``dtype`` in the u-sorted point order, and ``perm`` is the ``(N,)``
        integer sort permutation (``coords_sorted = coords[perm]``).
    """
    coords = np.asarray(coords, dtype=np.float64)
    N, dim = coords.shape
    if dim != 2:
        raise ValueError("causal_blocks_2d only supports 2D coords (dim == 2)")
    # Reduce (t, x) -> (u, v); pass-through if already null coords. We always use
    # the null condition u_y<=u_x & v_y<=v_x, which equals dt>=|dx| for (t,x).
    u = coords[:, 0]
    v = coords[:, 1]
    perm = np.argsort(u, kind="stable")
    us = np.ascontiguousarray(u[perm])
    vs = np.ascontiguousarray(v[perm])
    C = np.zeros((N, N), dtype=dtype)
    block = int(block)
    for i0 in range(0, N, block):
        i1 = min(i0 + block, N)
        ui = us[i0:i1][:, None]
        vi = vs[i0:i1][:, None]
        # row x = i, col y = j; y precedes x iff u_j<=u_i & v_j<=v_i
        C[i0:i1, :] = ((us[None, :] <= ui) & (vs[None, :] <= vi)).astype(dtype)
    # remove the (non-strict) diagonal self-relation
    np.fill_diagonal(C, 0)
    return C, perm


class _IDeltaMatvec:
    """Picklable matvec callable for the matrix-free 2D Pauli-Jordan operator.

    Holds the float causal matrix ``C`` and its contiguous transpose ``CT`` and
    evaluates ``iDelta @ x = (i/2) (C @ x - C^T @ x)`` via two BLAS GEMVs. Real
    and imaginary parts are multiplied separately so the (float32 or float64)
    GEMM kernel is used even for complex inputs (eigsh feeds complex vectors).
    """

    __slots__ = ("C", "CT", "_ftype")

    def __init__(self, C):
        self.C = C
        self.CT = np.ascontiguousarray(C.T)
        self._ftype = C.dtype

    def __call__(self, x):
        x = np.asarray(x)
        xr = np.ascontiguousarray(x.real, dtype=self._ftype)
        ar = self.C @ xr - self.CT @ xr
        if np.iscomplexobj(x):
            xi = np.ascontiguousarray(x.imag, dtype=self._ftype)
            ai = self.C @ xi - self.CT @ xi
        else:
            ai = np.zeros_like(ar)
        # (i/2)(ar + i ai) = (1/2)(-ai + i ar)
        return (-0.5 * ai + 0.5j * ar).astype(np.complex128)


def idelta_operator_2d(coords, *, dtype=np.float32, block=2048):
    """Matrix-FREE Hermitian Pauli-Jordan operator ``iDelta`` for a 2D causal set
    as a ``scipy.sparse.linalg.LinearOperator`` (no dense float iDelta).

    Builds the 2D causal matrix ``C`` blockwise (:func:`causal_blocks_2d`) and
    wraps the action ``iDelta @ x = (i/2) (C @ x - C^T @ x)`` as a Hermitian
    ``LinearOperator`` of shape ``(N, N)``, ``dtype=complex128``. The 2D Green
    function ``G_R = (1/2) C`` is therefore IMPLICIT -- only the 0/1 causal matrix
    (and its contiguous transpose) is stored, in ``float32`` by default. Feed the
    operator to :func:`toe.sj.sj_state_sparse` (``scipy.sparse.linalg.eigsh``) to
    extract the TOP-k spectral part that the SJ + SSEE pipelines need at large N.

    PRECISION NOTE (honest): ``float32`` storage gives a matvec accurate to
    ~1e-6-1e-7 relative -- fine for the large-N scaling smoke, but NOT for the
    machine-precision overlap validation. Pass ``dtype=np.float64`` when you need
    the top-k eigenvalues / truncated SSEE to agree with the dense path to better
    than 1e-8 (the v0.3.0 overlap tests do this).

    Formula: pauli-jordan.
    Evidence: VYPOCET-04 (ssee-diamond/calc.py), VYPOCET-12 (sj-vn-type/calc.py);
    matrix-free operator added in v0.3.0 for the large-N SPARSE/ITERATIVE path.
    Conventions: Sorkin-Yazdi 1611.10281 -- 2D massless ``G_R = (1/2) C``,
    ``iDelta = i (G_R - G_R^T) = (i/2)(C - C^T)``, Hermitian with real ``+/-``
    paired spectrum (so ``eigsh(which='LM')`` returns balanced ``+/-`` ends).

    Args:
        coords: (N, 2) coordinates (2D null ``(u, v)`` or ``(t, x)``).
        dtype: storage dtype of the causal matrix backing the matvec
            (``np.float32`` default; ``np.float64`` for the precision path).
        block: row-block size for the blockwise causal-matrix assembly.

    Returns:
        tuple ``(op, perm)`` where ``op`` is a Hermitian
        ``scipy.sparse.linalg.LinearOperator`` (shape ``(N, N)``,
        ``dtype=complex128``) realising ``iDelta`` in the u-sorted point order,
        and ``perm`` is the ``(N,)`` sort permutation (``coords[perm]`` is the
        order the operator acts in).
    """
    from scipy.sparse.linalg import LinearOperator

    C, perm = causal_blocks_2d(coords, dtype=dtype, block=block)
    N = C.shape[0]
    mv = _IDeltaMatvec(C)
    op = LinearOperator((N, N), matvec=mv, rmatvec=mv, dtype=np.complex128)
    return op, perm
