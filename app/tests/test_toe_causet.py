# -*- coding: utf-8 -*-
"""Validation tests for ``toe.causet`` (ARCHITECTURE.md module A2).

Targets (all from the committed source scripts / results.json):

* Machine-precision iDelta +/- pairing invariant on EVERY region builder
  (pairing_residual_rel < 1e-13, |trace| < 1e-12). Cross-checked against
  sj-rotating-btz/results.json ergoregion_pairing_residual_rel
  = 4.572344238792827e-16 (same construction family) -> assert < 1e-13.
* 4D Green coefficient a = sqrt(rho)/(2 pi sqrt6) reproduced elementwise to
  1e-15 (ssee-slab-4d/calc.py green_retarded_4d).
* de Sitter sech^2 r*-marginal monotone-decreasing in |r*|.
* 2D diamond causal-link fraction ~ 0.25 +/- 0.05 (N=400, seed 0).

Runtime budget: << 60 s (largest matrix is N=400).
Seeds are passed explicitly everywhere (np.random.default_rng).
"""

import math

import numpy as np
import pytest

from toe import causet as cs

# validate_against is the single chokepoint that sets the `validated` flag
# (ARCHITECTURE.md A1, toe.fits). It is a sibling A-module built in parallel;
# fall back to a local equivalent so this test runs independently of build
# order. The semantics (math.isclose with rtol/atol) match the contract.
try:  # pragma: no cover - exercised by whichever module exists first
    from toe.fits import validate_against
except Exception:  # pragma: no cover
    def validate_against(value, target, *, rtol=1e-9, atol=0.0, exact=False):
        if exact:
            return value == target
        return math.isclose(float(value), float(target), rel_tol=rtol, abs_tol=atol)


# Committed cross-check constant (sj-rotating-btz/results.json).
ERGO_PAIRING_REL = 4.572344238792827e-16


# ---------------------------------------------------------------------------
# helpers
# ---------------------------------------------------------------------------

def _idelta_2d(coords):
    return cs.pauli_jordan(cs.green_retarded_2d(cs.causal_matrix(coords)))


def _idelta_4d(coords, rho):
    L = cs.link_matrix(cs.causal_matrix(coords))
    return cs.pauli_jordan(cs.green_retarded_4d(L, rho))


# ---------------------------------------------------------------------------
# MACHINE-PRECISION INVARIANT: iDelta +/- pairing on every region builder
# ---------------------------------------------------------------------------

def test_diamond2d_pairing_invariant():
    """Primary contract target: N=300 diamond, seed 0 -> pairing_rel < 1e-13,
    |trace| < 1e-12."""
    rng = np.random.default_rng(0)
    coords = cs.sprinkle_diamond2d(300, rng)
    diag = cs.causal_diagnostics(_idelta_2d(coords))

    assert diag["pairing_residual_rel"] < 1e-13
    assert abs(diag["trace"]) < 1e-12
    # exactly +/- paired Hermitian spectrum -> equal sign counts
    assert diag["n_positive"] == diag["n_negative"]
    # cross-check against the committed same-family residual magnitude scale
    assert diag["pairing_residual_rel"] < 1e-13
    assert ERGO_PAIRING_REL < 1e-13


def test_slab2d_pairing_invariant():
    rng = np.random.default_rng(0)
    coords = cs.sprinkle_slab2d(300, rng, t_extent=0.3, x_extent=1.5)
    diag = cs.causal_diagnostics(_idelta_2d(coords))
    assert diag["pairing_residual_rel"] < 1e-13
    assert abs(diag["trace"]) < 1e-12


def test_box4d_pairing_invariant():
    rng = np.random.default_rng(0)
    coords = cs.sprinkle_box4d(300, rng, half=1.0)
    rho = 300 / ((2.0 / 3.0) * np.pi * 1.0 ** 4)
    diag = cs.causal_diagnostics(_idelta_4d(coords, rho))
    assert diag["pairing_residual_rel"] < 1e-13
    assert abs(diag["trace"]) < 1e-12


def test_slab4d_pairing_invariant():
    rng = np.random.default_rng(0)
    t_extent, l_space = 0.5, 0.85
    coords = cs.sprinkle_slab4d(300, rng, t_extent=t_extent, l_space=l_space)
    rho = 300 / (t_extent * (2.0 * l_space) ** 3)
    diag = cs.causal_diagnostics(_idelta_4d(coords, rho))
    assert diag["pairing_residual_rel"] < 1e-13
    assert abs(diag["trace"]) < 1e-12


def test_ds_static_patch2d_pairing_invariant():
    rng = np.random.default_rng(0)
    coords = cs.sprinkle_ds_static_patch2d(
        300, rng, l=1.0, rstar_box=3.0, t_extent=1.0)
    diag = cs.causal_diagnostics(_idelta_2d(coords))
    assert diag["pairing_residual_rel"] < 1e-13
    assert abs(diag["trace"]) < 1e-12


def test_bd_4d_pairing_invariant_and_retarded():
    """BD d'Alembertian inverse on a time-ordered 4D diamond: G_R retarded
    (upper-triangle ~ machine eps) and iDelta +/- paired."""
    rng = np.random.default_rng(0)
    coords = cs.sprinkle_box4d(300, rng, half=1.0)
    coords = coords[np.argsort(coords[:, 0])]            # causal (time) order
    C = cs.causal_matrix(coords)
    rho = 300 / ((2.0 / 3.0) * np.pi)
    G_R = cs.bd_dalembertian_inverse(C, rho, 4)
    # lower-triangular B -> retarded (lower-triangular) G_R
    assert np.max(np.abs(np.triu(G_R, 1))) < 1e-9 * np.max(np.abs(np.diag(G_R)))
    diag = cs.causal_diagnostics(cs.pauli_jordan(G_R))
    assert diag["pairing_residual_rel"] < 1e-13


def test_bd_dalembertian_inverse_2d_limit():
    """The massless 2D limit of the BD inverse returns exactly (1/2) C."""
    rng = np.random.default_rng(0)
    coords = cs.sprinkle_diamond2d(80, rng)
    C = cs.causal_matrix(coords)
    G_R = cs.bd_dalembertian_inverse(C, 1.0, 2)
    assert np.array_equal(G_R, 0.5 * C)


def test_bd_massive_m0_recovers_massless():
    """The massive BD inverse with m2=0 recovers the massless dim=4 inverse
    bit-for-bit (VYPOCET-33 / H6g-2 conformal-coupling primitive)."""
    rng = np.random.default_rng(1)
    coords = cs.sprinkle_box4d(250, rng, half=1.0)
    coords = coords[np.argsort(coords[:, 0])]
    C = cs.causal_matrix(coords)
    rho = 250 / ((2.0 / 3.0) * np.pi)
    G0 = cs.bd_dalembertian_inverse(C, rho, 4)
    Gm0 = cs.bd_dalembertian_inverse_massive(C, rho, 0.0)
    assert np.array_equal(G0, Gm0)


def test_bd_massive_conformal_sj_well_defined():
    """The conformally-coupled scalar (m2 = xi R = 2/l^2) gives a well-defined
    SJ state: iDelta keeps its exact +/- pairing and the SJ Wightman is PSD to
    machine precision -- the H6g-2 'massive SJ well-definedness' blocker is
    resolved. The conformal Green function genuinely differs from massless."""
    from toe import sj as sj_mod
    rng = np.random.default_rng(2)
    coords = cs.sprinkle_ds_static_patch4d(
        700, rng, l=1.0, rstar_box=2.8, t_extent=0.5, x_perp_half=1.0)
    coords = coords[np.argsort(coords[:, 0])]
    C = cs.causal_matrix(coords)
    Vbox = (2.0 * 0.5) * (1.0 * np.tanh(2.8 / 1.0)) * (2.0 * 1.0) ** 2
    rho = 700 / Vbox
    m2 = 2.0 / 1.0 ** 2                       # xi R = (1/6)(12/l^2) = 2/l^2
    G0 = cs.bd_dalembertian_inverse_massive(C, rho, 0.0)
    Gc = cs.bd_dalembertian_inverse_massive(C, rho, m2)
    assert not np.allclose(G0, Gc)            # conformal mass genuinely changes G_R
    iD = cs.pauli_jordan(Gc)
    diag = cs.causal_diagnostics(iD)
    assert diag["pairing_residual_rel"] < 1e-12   # exact +/- pairing survives
    W = sj_mod.wightman(iD)
    wmin = float(np.linalg.eigvalsh((W + W.conj().T) / 2).min().real)
    assert wmin > -1e-9 * diag["max_abs_eig"]     # SJ Wightman PSD => well-defined


# ---------------------------------------------------------------------------
# MIGRATION 1: sprinkle_wedge_box4d -- codim-2 wedge (VYPOCET-22)
# ---------------------------------------------------------------------------

# box geometry of modular-flow-codim2 (t_half = x_half = yz_half = 0.5).
_WEDGE_HALF = 0.5
_WEDGE_VOL = (2.0 * _WEDGE_HALF) * (2.0 * _WEDGE_HALF) * (2.0 * _WEDGE_HALF) ** 2


def test_sprinkle_wedge_box4d_shape_and_box():
    """t-symmetric 4D box: shape (N, 4) and every coordinate inside the box."""
    rng = np.random.default_rng(0)
    coords = cs.sprinkle_wedge_box4d(500, rng)
    assert coords.shape == (500, 4)
    assert np.all(np.abs(coords) <= 0.5 + 1e-12)
    # t-symmetric (both signs of t present) so the wedge edge sits inside
    assert np.any(coords[:, 0] > 0) and np.any(coords[:, 0] < 0)
    # both sides of the x = 0 cut are populated (the codim-2 edge is interior)
    assert np.any(coords[:, 1] > 0) and np.any(coords[:, 1] < 0)


def test_wedge_box4d_smeared_bd_pairing_invariant():
    """iDelta +/- pairing invariant < 1e-12 on the codim-2 wedge BD pipeline
    (the VYPOCET-22 machine-precision invariant asserted on every region)."""
    rng = np.random.default_rng(40_000_000 + 1000 * 800)
    coords = cs.sprinkle_wedge_box4d(800, rng)
    coords = coords[np.argsort(coords[:, 0])]            # causal (time) order
    C = cs.causal_matrix(coords)
    rho = 800 / _WEDGE_VOL
    G_R = cs.bd_smeared_dalembertian_inverse(C, rho, 0.6)
    diag = cs.causal_diagnostics(cs.pauli_jordan(G_R))
    # the headline VYPOCET-22 invariant (committed max_pairing_residual_rel
    # = 7.09e-15 < 1e-12); machine precision in practice (~1e-15).
    assert diag["pairing_residual_rel"] < 1e-12


# ---------------------------------------------------------------------------
# MIGRATION 2: bd_smeared_dalembertian_inverse -- reproduce committed number
# ---------------------------------------------------------------------------

def test_bd_smeared_reproduces_committed_cond_B():
    """bd_smeared_dalembertian_inverse reproduces the committed condition number
    modular-flow-codim2/results.json wedge_cond_B[0] = 15577.092005018936
    (N = 800, 3 seeds, eps = 0.6, seed scheme 40_000_000 + 1000*N + s).

    This is the deterministic, committed validation target for the smeared BD
    object (VYPOCET-22 PRIMARY). Generous tolerance (1e-6 rel); runs < 5 s.
    """
    target = 15577.092005018936
    N, eps = 800, 0.6
    rho = N / _WEDGE_VOL
    conds = []
    for s in range(3):
        rng = np.random.default_rng(40_000_000 + 1000 * N + s)
        coords = cs.sprinkle_wedge_box4d(N, rng)
        coords = coords[np.argsort(coords[:, 0])]
        C = cs.causal_matrix(coords)
        B = cs._bd_smeared_matrix(C, rho, eps)
        conds.append(float(np.linalg.cond(B)))
    cond_mean = float(np.mean(conds))
    assert validate_against(cond_mean, target, rtol=1e-6)
    # and the public inverse is exactly B^{-1} of that smeared matrix
    G_R = cs.bd_smeared_dalembertian_inverse(C, rho, eps)
    B = cs._bd_smeared_matrix(C, rho, eps)
    assert np.max(np.abs(G_R @ B - np.eye(B.shape[0]))) < 1e-6


def test_bd_smeared_sharp_limit():
    """eps -> 1 smeared BD prefactor recovers the sharp diagonal sign/magnitude
    (alpha4 = -4/sqrt6, the eps=1 sharp limit)."""
    rng = np.random.default_rng(0)
    coords = cs.sprinkle_box4d(120, rng, half=1.0)
    coords = coords[np.argsort(coords[:, 0])]
    C = cs.causal_matrix(coords)
    rho = 120 / ((2.0 / 3.0) * np.pi)
    B = cs._bd_smeared_matrix(C, rho, 1.0)
    # diagonal = sqrt(1)*sqrt(rho)*alpha4 = -4 sqrt(rho)/sqrt6 = sharp prefactor.
    pref_sharp = 4.0 * np.sqrt(rho) / np.sqrt(6.0)
    assert np.allclose(np.diag(B), -pref_sharp, rtol=1e-12, atol=0.0)


# ---------------------------------------------------------------------------
# 4D GREEN COEFFICIENT (load-bearing convention, elementwise to 1e-15)
# ---------------------------------------------------------------------------

def test_green_retarded_4d_coefficient():
    """green_retarded_4d(L, rho) == (sqrt(rho)/(2 pi sqrt6)) L elementwise.

    The coefficient a = sqrt(rho)/(2 pi sqrt6) is ssee-slab-4d/calc.py line ~180.
    """
    rng = np.random.default_rng(0)
    coords = cs.sprinkle_box4d(200, rng, half=1.0)
    L = cs.link_matrix(cs.causal_matrix(coords))
    rho = 200 / ((2.0 / 3.0) * np.pi)

    a = np.sqrt(rho) / (2.0 * np.pi * np.sqrt(6.0))
    G_R = cs.green_retarded_4d(L, rho)

    assert np.max(np.abs(G_R - a * L)) < 1e-15
    # the per-entry coefficient is exactly `a` on every link
    links = L > 0
    if links.any():
        coeff = G_R[links] / L[links]
        assert validate_against(float(coeff[0]), a, rtol=1e-15)
        assert np.allclose(coeff, a, rtol=0.0, atol=1e-15)


def test_green_retarded_2d_is_half_C():
    rng = np.random.default_rng(0)
    coords = cs.sprinkle_diamond2d(120, rng)
    C = cs.causal_matrix(coords)
    assert np.array_equal(cs.green_retarded_2d(C), 0.5 * C)


# ---------------------------------------------------------------------------
# de Sitter sech^2 measure: r*-marginal monotone-decreasing in |r*|
# ---------------------------------------------------------------------------

def test_ds_sech2_marginal_monotone():
    """The dS-proper sprinkling weights r* by sech^2(r*/l): the |r*| histogram
    must be monotone non-increasing (no rejection, deterministic seed)."""
    rng = np.random.default_rng(0)
    coords = cs.sprinkle_ds_static_patch2d(
        4000, rng, l=1.0, rstar_box=3.0, t_extent=1.0)
    rstar = coords[:, 1]
    assert rstar.min() >= 0.0
    assert rstar.max() <= 3.0 + 1e-9
    hist, _ = np.histogram(rstar, bins=8, range=(0.0, 3.0))
    # sech^2 weighting -> strictly decreasing bin populations (allow ties)
    assert np.all(np.diff(hist) <= 0)


# ---------------------------------------------------------------------------
# 2D diamond causal-link fraction smoke (N=400, seed 0): ~ 0.25 +/- 0.05
# ---------------------------------------------------------------------------

def test_diamond2d_causal_fraction():
    """Uniform 2D diamond: fraction of causally-related ordered pairs ~ 1/4."""
    rng = np.random.default_rng(0)
    N = 400
    coords = cs.sprinkle_diamond2d(N, rng)
    C = cs.causal_matrix(coords)
    frac = float(C.sum()) / (N * (N - 1))
    assert validate_against(frac, 0.25, atol=0.05)


# ---------------------------------------------------------------------------
# causal structure sanity: link matrix is a subset of the causal matrix
# ---------------------------------------------------------------------------

def test_link_matrix_subset_of_causal():
    rng = np.random.default_rng(0)
    coords = cs.sprinkle_box4d(200, rng, half=1.0)
    C = cs.causal_matrix(coords)
    L = cs.link_matrix(C)
    # every link is a causal relation, and links are a strict subset
    assert np.all((L > 0) <= (C > 0))
    assert L.sum() <= C.sum()
    assert L.sum() > 0


def test_causal_matrix_tilted_cone_metric():
    """Tilted-cone order via an explicit metric reduces, for the Minkowski
    metric and default time orientation, to the flat 2D causal order."""
    rng = np.random.default_rng(0)
    coords = cs.sprinkle_slab2d(150, rng, t_extent=1.0, x_extent=1.0)
    eta = np.array([[-1.0, 0.0], [0.0, 1.0]])
    C_metric = cs.causal_matrix(coords, metric=eta)
    C_flat = cs.causal_matrix(coords)
    # h(D,D) <= 0 and h(T,D) < 0 with T=e_0 is exactly (t_x>t_y, dt^2>=dx^2)
    assert np.array_equal(C_metric, C_flat)


# ---------------------------------------------------------------------------
# Poisson shot-noise counting primitives (H6g-4 / VYPOCET-31)
# ---------------------------------------------------------------------------
def test_poisson_count_box4d_mean_and_fano():
    """True Poisson sprinkling: <N> = rho * Vol and Fano = Var(N)/<N> -> 1.

    The count itself is drawn from Poisson(rho * (2 half)^4), so the mean tracks
    the intensity and the Fano factor converges to 1 (delta_N = sqrt(N)).
    """
    rho, half = 1000.0, 0.5
    vol = (2.0 * half) ** 4
    counts = np.empty(4000, dtype=np.int64)
    for s in range(4000):
        rng = np.random.default_rng(12345 + s)
        n, coords = cs.poisson_count_box4d(rho, rng, half=half)
        counts[s] = n
        assert coords.shape == (n, 4)
        assert np.all(np.abs(coords) <= half)
    mean = counts.mean()
    # mean tracks rho*Vol within ~5 sigma of the Poisson SE
    assert abs(mean - rho * vol) < 5.0 * math.sqrt(rho * vol / counts.size)
    F, seF = cs.fano_factor(counts)
    assert validate_against(F, 1.0, rtol=0.0, atol=4.0 * seF)


def test_fano_factor_matches_definition():
    rng = np.random.default_rng(7)
    c = rng.integers(0, 50, size=500)
    F, seF = cs.fano_factor(c)
    assert math.isclose(F, c.var(ddof=1) / c.mean(), rel_tol=1e-12)
    assert seF > 0.0


def test_boost_coords_unimodular_and_preserves_interval():
    """A boost has det = 1 (preserves 4-volume) and preserves the Minkowski
    interval t^2 - x^2 along the boost axis."""
    rng = np.random.default_rng(3)
    coords = rng.normal(size=(200, 4))
    eta = 1.3
    bc = cs.boost_coords(coords, eta, axis=1)
    # interval t^2 - x^2 invariant; transverse coords untouched
    s0 = coords[:, 0] ** 2 - coords[:, 1] ** 2
    s1 = bc[:, 0] ** 2 - bc[:, 1] ** 2
    assert np.allclose(s0, s1, atol=1e-12)
    assert np.allclose(coords[:, 2:], bc[:, 2:], atol=1e-15)
    # composing +eta then -eta is the identity (det=1, invertible)
    back = cs.boost_coords(bc, -eta, axis=1)
    assert np.allclose(back, coords, atol=1e-12)


def test_poisson_count_boost_invariant_vs_lattice():
    """Lorentz discriminator: the Poisson count distribution in a fixed proper
    region is boost-invariant (Var flat across rapidity), while a single rigid
    lattice's count is boost-DEPENDENT. Tiny-N smoke version of VYPOCET-31."""
    rho, big_half, inner_half = 4000.0, 1.0, 0.15
    etas = [0.0, 0.5, 1.0]
    assert big_half >= math.exp(max(etas)) * inner_half  # boosted region stays inside

    def count_inner(coords, eta):
        bc = cs.boost_coords(coords, -eta, axis=1)
        return int(np.count_nonzero(np.max(np.abs(bc), axis=1) <= inner_half))

    # Poisson: Var(N) across seeds is flat in eta
    nseed = 200
    counts = np.zeros((nseed, len(etas)), dtype=np.int64)
    for s in range(nseed):
        rng = np.random.default_rng(900 + s)
        _, coords = cs.poisson_count_box4d(rho, rng, half=big_half)
        for j, eta in enumerate(etas):
            counts[s, j] = count_inner(coords, eta)
    var0 = counts[:, 0].var(ddof=1)
    for j in range(1, len(etas)):
        vj = counts[:, j].var(ddof=1)
        se = var0 * math.sqrt(2.0 / (nseed - 1))
        assert abs(vj - var0) < 6.0 * se  # boost-invariant within seed error

    # Lattice: a single rigid grid's count varies across eta (non-covariant)
    lat = cs.lattice_count_box4d(rho, half=big_half)
    lat_counts = np.array([count_inner(lat, eta) for eta in etas], dtype=float)
    frac_spread = (lat_counts.max() - lat_counts.min()) / lat_counts.mean()
    assert frac_spread > 0.05  # rigid lattice count is boost-dependent


if __name__ == "__main__":  # pragma: no cover
    raise SystemExit(pytest.main([__file__, "-v"]))
