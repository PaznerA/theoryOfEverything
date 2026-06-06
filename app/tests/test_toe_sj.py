# -*- coding: utf-8 -*-
"""Validation tests for toe.sj (module B1, the Sorkin-Johnston state).

Implements the ARCHITECTURE.md B1 validation targets:

  * Machine-precision SJ invariant: from a 2D diamond (N=300, seed 0) the SJ
    Wightman ``W`` reproduces ``iDelta`` via ``W - W^T = iDelta`` to 1e-12 and
    ``W`` is positive semidefinite (min eigenvalue > -1e-10).
  * Fully-dragged BTZ ergoregion smoke (M=1, J=0.6, r=0.974, N~800, seed 101):
    ``asymmetry_causal`` value ~ 1.0 (committed
    sj-rotating-btz/results.json: frac_corotating_links_inside_ergo = 1.0,
    causal_asymmetry_inside_ergo = 1.0); ``asymmetry_wightman`` is NaN
    (fully dragged, no counter-rotating links -- committed
    wightman_asymmetry = null).
  * Self-overlap sanity: ``positive_subspace_overlap(iD, iD).value`` ~ 1.0
    (committed sanity_static_vs_static_mean_cos2 = 1.0000000000000002).
  * Superradiant-weight monotonicity smoke (Kerr r=2.6, small N): weight grows
    with spin a; weight(a=0) ~ 0 (measure-zero wedge), weight(a=0.6) > weight(a=0).

Each test passes explicit seeds, uses the SMALL-N smoke configuration, and
asserts via toe.fits.validate_against; total runtime stays well under 60 s.

NOTE on the SJ identity. ``W`` is the POSITIVE spectral part of the Hermitian
``iDelta`` and is itself Hermitian, so ``W - W^dagger = 0`` trivially. The
load-bearing, machine-precision SJ relation (Sorkin-Yazdi 1611.10281) is
``iDelta = W - W^*`` with ``W^* = W^T`` (since W is Hermitian), i.e.
``W - W^T = iDelta``. The ARCHITECTURE wording ``W - W.conj().T`` is the
Hermitian-conjugate typo for this transpose relation; we assert the physically
correct, reproducible invariant.
"""

import json
import math
import os

import numpy as np
import pytest

from toe import causet, sj
from toe.fits import Measurement, validate_against

# --------------------------------------------------------------------------- #
# committed results.json targets                                              #
# --------------------------------------------------------------------------- #

_REPO = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir, os.pardir))
_BTZ_JSON = os.path.join(
    _REPO, "core-data", "calculations", "sj-rotating-btz", "results.json"
)
_SR_JSON = os.path.join(
    _REPO,
    "core-data",
    "calculations",
    "sj-eigenvector-superradiance",
    "results.json",
)


def _load(path):
    with open(path) as f:
        return json.load(f)


# --------------------------------------------------------------------------- #
# BTZ / Kerr fixed-r (t,phi) section metrics (from the verified calc scripts) #
# --------------------------------------------------------------------------- #

def _btz_section(M, J, r):
    """Rotating BTZ fixed-r (t,phi) 2-metric h (sj-rotating-btz section_metric)."""
    return np.array([[M - r ** 2, -J / 2.0], [-J / 2.0, r ** 2]], dtype=float)


def _kerr_section(M, a, r):
    """Equatorial Kerr fixed-r (t,phi) 2-metric h (sj-kerr-equatorial section_metric)."""
    g_tt = -(1.0 - 2.0 * M / r)
    g_tp = -2.0 * M * a / r
    g_pp = r ** 2 + a ** 2 + 2.0 * M * a ** 2 / r
    return np.array([[g_tt, g_tp], [g_tp, g_pp]], dtype=float)


def _drag(h):
    """Frame-drag / ZAMO slope s_drag = -g_tphi / g_phiphi."""
    return -h[0, 1] / h[1, 1]


def _time_orientation(h):
    return np.array([1.0, _drag(h)])


def _btz_surfaces(M, J):
    disc = M ** 2 - J ** 2
    rp = math.sqrt(0.5 * (M + math.sqrt(disc)))
    rm = math.sqrt(0.5 * (M - math.sqrt(disc)))
    return rp, rm, math.sqrt(M)


def _sprinkle_section(N, T_extent, Phi_extent, rng):
    """Uniform-in-(t,phi) sprinkle (constant proper density on a fixed-r patch)."""
    t = rng.uniform(0.0, T_extent, size=N)
    p = rng.uniform(0.0, Phi_extent, size=N)
    return np.column_stack([t, p])


def _build_section_idelta(h, coords):
    """Tilted-cone causal matrix -> G_R = (1/2) C -> iDelta for a fixed-r section."""
    C = causet.causal_matrix(coords, metric=h, time_orientation=_time_orientation(h))
    iD = causet.pauli_jordan(causet.green_retarded_2d(C))
    return C, iD


# =========================================================================== #
# 1. Machine-precision SJ invariant (2D diamond, N=300, seed 0)               #
# =========================================================================== #

def test_sj_wightman_invariant_and_psd_diamond2d():
    rng = np.random.default_rng(0)
    coords = causet.sprinkle_diamond2d(300, rng)
    C = causet.causal_matrix(coords)
    iD = causet.pauli_jordan(causet.green_retarded_2d(C))

    state = sj.sj_state(iD)
    W = state.W

    # W is Hermitian (positive spectral part of a Hermitian operator)
    assert np.max(np.abs(W - W.conj().T)) < 1e-12

    # The SJ identity: iDelta = W - W^* = W - W^T (W Hermitian) -- machine precision.
    resid = float(np.max(np.abs((W - W.T) - iD)))
    assert resid < 1e-12

    # W positive semidefinite (SJ Wightman is a state)
    min_eig = float(np.linalg.eigvalsh(W).min())
    assert min_eig > -1e-10

    # pos_spectrum is the positive eigenvalues, sorted descending
    ps = state.pos_spectrum
    assert ps.size > 0
    assert np.all(np.diff(ps) <= 1e-12)
    assert np.all(ps > 0)


def test_wightman_convenience_matches_state():
    rng = np.random.default_rng(0)
    coords = causet.sprinkle_diamond2d(300, rng)
    C = causet.causal_matrix(coords)
    iD = causet.pauli_jordan(causet.green_retarded_2d(C))
    W1 = sj.wightman(iD)
    W2 = sj.sj_state(iD).W
    assert np.max(np.abs(W1 - W2)) == 0.0


# =========================================================================== #
# 2. Fully-dragged BTZ ergoregion (M=1, J=0.6, r=0.974, N~800, seed 101)      #
# =========================================================================== #

def test_btz_ergoregion_fully_dragged_causal_asymmetry():
    btz = _load(_BTZ_JSON)
    target_asym = btz["headline_results"]["causal_asymmetry_inside_ergo"]      # 1.0
    target_fco = btz["headline_results"]["frac_corotating_links_inside_ergo"]  # 1.0
    assert target_asym == 1.0 and target_fco == 1.0

    M, J = 1.0, 0.6
    rp, rm, rerg = _btz_surfaces(M, J)
    r_in = 0.5 * (rp + rerg)   # ~0.9743, well inside the ergoregion
    h = _btz_section(M, J, r_in)

    rng = np.random.default_rng(101)
    coords = _sprinkle_section(800, 1.4, 1.4, rng)
    C, iD = _build_section_idelta(h, coords)

    meas = sj.asymmetry_causal(coords, C, axis=1)
    assert isinstance(meas, Measurement)
    assert meas.n > 0
    # fully-dragged ergoregion: every causal link co-rotates -> A_caus = +1
    assert meas.value > 0.95
    meas.validated = validate_against(meas.value, target_asym, rtol=0.0, atol=0.05)
    assert meas.validated is True

    # the SJ construction is well-defined inside the ergoregion (paired spectrum)
    diag = causet.causal_diagnostics(iD)
    assert diag["pairing_residual_rel"] < 1e-13
    assert abs(diag["trace"]) < 1e-12


def test_btz_ergoregion_wightman_asymmetry_is_nan_when_fully_dragged():
    btz = _load(_BTZ_JSON)
    # committed: two_point.wightman_asymmetry is null (no counter-rotating links)
    assert btz["partA_existence"]["rotating_inside_ergoregion"]["two_point"][
        "wightman_asymmetry"
    ] is None

    M, J = 1.0, 0.6
    rp, rm, rerg = _btz_surfaces(M, J)
    r_in = 0.5 * (rp + rerg)
    h = _btz_section(M, J, r_in)
    rng = np.random.default_rng(101)
    coords = _sprinkle_section(800, 1.4, 1.4, rng)
    C, iD = _build_section_idelta(h, coords)

    W = sj.wightman(iD)
    aw = sj.asymmetry_wightman(W, coords, C, axis=1)
    assert isinstance(aw, Measurement)
    assert math.isnan(aw.value)   # fully dragged: A_W undefined (None in JSON)
    assert aw.n > 0


def test_btz_outside_ergoregion_opposite_sign_asymmetries():
    """Outside the ergoregion A_caus > 0 but A_W < 0 (the opposite-sign signature).

    Committed sj-rotating-btz/results.json at r_out=1.3 (N=1600, 4 seeds):
    asym_rotating_mean=+0.227, wightman_asym_rotating=-0.211. Small-N smoke
    reproduces the SIGNS (A_caus > 0, A_W < 0), generous tolerance.
    """
    btz = _load(_BTZ_JSON)
    assert btz["partB_control"]["asym_rotating_mean"] > 0
    assert btz["partB_control"]["wightman_asym_rotating"] < 0

    M, J, r_out = 1.0, 0.6, 1.3
    h = _btz_section(M, J, r_out)
    # average a few seeds at small N to stabilise the signs
    acs, aws = [], []
    for s in (200, 201, 202):
        rng = np.random.default_rng(s)
        coords = _sprinkle_section(800, 1.4, 1.4, rng)
        C, iD = _build_section_idelta(h, coords)
        W = sj.wightman(iD)
        acs.append(sj.asymmetry_causal(coords, C, axis=1).value)
        aws.append(sj.asymmetry_wightman(W, coords, C, axis=1).value)
    assert np.mean(acs) > 0.0    # more co-rotating causal links (counting)
    assert np.mean(aws) < 0.0    # stronger counter-rotating SJ correlation


# =========================================================================== #
# 3. Self-overlap sanity (positive subspace vs itself == 1)                   #
# =========================================================================== #

def test_positive_subspace_self_overlap_is_one():
    sr = _load(_SR_JSON)
    target = sr["goalA1_eigenvector_overlap"]["sanity_static_vs_static_mean_cos2"]
    assert target > 0.999  # committed 1.0000000000000002

    # build an iDelta on a small Kerr section (any Lorentzian section works)
    M, a, r = 1.0, 0.9, 2.6
    h = _kerr_section(M, a, r)
    rng = np.random.default_rng(101)
    coords = _sprinkle_section(420, 1.4, 1.4, rng)
    _, iD = _build_section_idelta(h, coords)

    ov = sj.positive_subspace_overlap(iD, iD)
    assert isinstance(ov, Measurement)
    assert ov.n > 0
    assert ov.value > 0.999
    ov.validated = validate_against(ov.value, 1.0, rtol=0.0, atol=1e-3)
    assert ov.validated is True


def test_positive_subspace_overlap_rotating_below_one():
    """Rotating vs static positive subspaces are rotated: mean cos^2 < 1.

    Committed kerr_a0.9_vs_a0_r2.6 mean_cos2_principal ~ 0.507 (full run);
    small-N smoke only asserts the qualitative drop below the static self-overlap.
    """
    M, r = 1.0, 2.6
    rng = np.random.default_rng(303)
    coords = _sprinkle_section(420, 1.4, 1.4, rng)   # SHARED sprinkle
    h_rot = _kerr_section(M, 0.9, r)
    h_stat = _kerr_section(M, 1e-9, r)
    _, iD_rot = _build_section_idelta(h_rot, coords)
    _, iD_stat = _build_section_idelta(h_stat, coords)
    ov = sj.positive_subspace_overlap(iD_rot, iD_stat)
    assert ov.value < 0.999   # subspaces measurably rotated by frame dragging


# =========================================================================== #
# 4. Superradiant-weight monotonicity smoke (Kerr r=2.6, small N)             #
# =========================================================================== #

# coarse (w,k) occupation grid -> fast; the trend/sign is robust to grid density
_KMAX = 35.0
_NW = 41
_WS = np.linspace(-_KMAX, _KMAX, _NW)
_KS = np.linspace(-_KMAX, _KMAX, _NW)


def _kerr_weight(a, *, M=1.0, r=2.6, N=420, seed=101):
    h = _kerr_section(M, max(a, 1e-9), r)
    Omega = _drag(h)
    rng = np.random.default_rng(seed)
    coords = _sprinkle_section(N, 1.4, 1.4, rng)
    _, iD = _build_section_idelta(h, coords)
    return sj.superradiant_weight(coords, iD, omega=Omega, ws=_WS, ks=_KS, seed=seed)


def test_superradiant_weight_static_is_zero():
    sr = _load(_SR_JSON)
    target = sr["goalA3_superradiance"]["vs_spin_r2.6"]["a=0.0"][
        "superrad_wedge_weight"
    ]
    assert target == 0.0  # committed: measure-zero wedge -> exactly 0

    m0 = _kerr_weight(0.0)
    assert isinstance(m0, Measurement)
    assert m0.n > 0
    # static control: measure-zero superradiant wedge -> ~0
    assert abs(m0.value) < 1e-3
    m0.validated = validate_against(m0.value, 0.0, rtol=0.0, atol=1e-3)
    assert m0.validated is True


def test_superradiant_weight_increases_with_spin():
    sr = _load(_SR_JSON)
    vs = sr["goalA3_superradiance"]["vs_spin_r2.6"]
    # committed full-run trend: a=0 -> 0, a=0.3 -> 0.00121, a=0.6 -> 0.00622
    assert vs["a=0.0"]["superrad_wedge_weight"] < vs["a=0.6"]["superrad_wedge_weight"]

    w0 = _kerr_weight(0.0).value
    w6 = _kerr_weight(0.6).value
    assert w6 > w0
    assert w6 > 1e-4    # a genuine, non-zero co-rotating superradiant weight


def test_superradiant_weight_monotone_small_grid():
    """Weight is monotone non-decreasing in spin a across {0, 0.3, 0.6}."""
    weights = [_kerr_weight(a).value for a in (0.0, 0.3, 0.6)]
    assert all(np.diff(weights) > -1e-9)
    assert weights[0] < weights[-1]


# ---------------------------------------------------------------------------
# MIGRATION 3: rel_floor parameter on sj_state (VYPOCET-22)
# ---------------------------------------------------------------------------

def _idelta_2d_diamond(N=300, seed=0):
    rng = np.random.default_rng(seed)
    coords = causet.sprinkle_diamond2d(N, rng)
    return causet.pauli_jordan(causet.green_retarded_2d(causet.causal_matrix(coords)))


def test_sj_state_rel_floor_default_is_bit_identical():
    """rel_floor=None (default) keeps the absolute-tol code path BIT-IDENTICAL.

    The default must reproduce the old behaviour exactly: W, eigvals, eigvecs and
    pos_spectrum must be bit-for-bit equal whether rel_floor is omitted or
    explicitly passed as None.
    """
    iD = _idelta_2d_diamond()
    st_old = sj.sj_state(iD)                 # no rel_floor argument at all
    st_none = sj.sj_state(iD, rel_floor=None)
    assert np.array_equal(st_old.W, st_none.W)
    assert np.array_equal(st_old.eigvals, st_none.eigvals)
    assert np.array_equal(st_old.eigvecs, st_none.eigvecs)
    assert np.array_equal(st_old.pos_spectrum, st_none.pos_spectrum)
    # and wightman() wrapper default is bit-identical too
    assert np.array_equal(sj.wightman(iD), sj.wightman(iD, rel_floor=None))


def test_sj_state_rel_floor_reproduces_floored_helper():
    """rel_floor=1e-10 reproduces the VYPOCET-09/20 sj_wightman_floored W on an
    ill-conditioned smeared-BD iDelta (the use case the parameter exists for)."""
    rng = np.random.default_rng(40_000_000 + 1000 * 800)
    coords = causet.sprinkle_wedge_box4d(800, rng)
    coords = coords[np.argsort(coords[:, 0])]
    C = causet.causal_matrix(coords)
    vol = (2 * 0.5) * (2 * 0.5) * (2 * 0.5) ** 2
    rho = 800 / vol
    G_R = causet.bd_smeared_dalembertian_inverse(C, rho, 0.6)
    iD = causet.pauli_jordan(G_R)

    # reference: the local floored construction (helpers.sj_wightman_floored)
    w, V = np.linalg.eigh(iD)
    lmax = np.max(np.abs(w))
    pos = w > 1e-10 * lmax
    W_ref = (V[:, pos] * w[pos]) @ V[:, pos].conj().T

    W_lib = sj.sj_state(iD, rel_floor=1e-10).W
    assert np.array_equal(W_lib, W_ref)


def test_sj_state_rel_floor_discards_subfloor_modes():
    """A constructed Hermitian iDelta with a tiny positive eigenvalue between the
    absolute tol (1e-12) and the relative floor (1e-10*lmax): the rel_floor path
    DROPS that noise mode while the absolute-tol default keeps it. Proves the
    relative floor genuinely changes behaviour when the spectrum demands it."""
    n = 6
    rng = np.random.default_rng(7)
    Q, _ = np.linalg.qr(rng.standard_normal((n, n)))
    # +/- paired spectrum with one sub-floor positive mode (1e-11 vs lmax=10)
    lam = np.array([-10.0, -3.0, -1e-11, 1e-11, 3.0, 10.0])
    iD = (Q * lam) @ Q.conj().T
    iD = 0.5 * (iD + iD.conj().T)

    st_abs = sj.sj_state(iD)                    # absolute tol=1e-12 keeps 1e-11
    st_rel = sj.sj_state(iD, rel_floor=1e-10)   # floor = 1e-9 drops 1e-11
    assert st_abs.pos_spectrum.size == 3        # 1e-11, 3, 10
    assert st_rel.pos_spectrum.size == 2        # 3, 10 only
    # the two W differ only by the dropped sub-floor (~1e-11) mode
    wdiff = np.max(np.abs(st_abs.W - st_rel.W))
    assert 1e-12 < wdiff < 1e-10


if __name__ == "__main__":   # pragma: no cover
    raise SystemExit(pytest.main([__file__, "-v"]))
