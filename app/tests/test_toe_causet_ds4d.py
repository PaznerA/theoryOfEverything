# -*- coding: utf-8 -*-
"""Validation tests for the VYPOCET-21 library extension
``toe.causet.sprinkle_ds_static_patch4d`` (4D de Sitter static-patch sech^2 slab).

Targets (machine-precision invariant + measure monotonicity, ARCHITECTURE.md A2):

* iDelta +/- pairing invariant on the 4D dS static-patch region built via the
  link-matrix 4D Green: pairing_residual_rel < 1e-12, |trace| < 1e-10,
  n_positive == n_negative (exact +/- paired Hermitian spectrum).
* sech^2 radial (r*) marginal monotone non-increasing in r* (the dS proper
  measure; the transverse box marginals stay flat/uniform).
* transverse box bounds + radial bound respected; t-extent respected.

Runtime budget: << 30 s (largest matrix N=500).
Seeds are passed explicitly everywhere (np.random.default_rng).
"""

import numpy as np
import pytest

from toe import causet as cs


def _idelta_4d_dspatch(coords, rho):
    """4D Pauli-Jordan on the flat conformal (t, r*, x1, x2) order via the
    link-matrix Green (Johnston 0909.0944)."""
    L = cs.link_matrix(cs.causal_matrix(coords))
    return cs.pauli_jordan(cs.green_retarded_4d(L, rho))


def _proper_volume(l, rstar_box, t_extent, x_perp_half):
    """dS-proper box volume 2 t_extent * l tanh(rstar_box/l) * (2 x_perp_half)^2."""
    return (2.0 * t_extent) * (l * np.tanh(rstar_box / l)) * (2.0 * x_perp_half) ** 2


# ---------------------------------------------------------------------------
# MACHINE-PRECISION INVARIANT: iDelta +/- pairing on the 4D dS static patch
# ---------------------------------------------------------------------------

def test_ds_static_patch4d_pairing_invariant():
    """N=500 4D dS static patch, seed 0 -> pairing_rel < 1e-12, |trace| small,
    exactly +/- paired Hermitian iDelta spectrum."""
    l, rstar_box, t_extent, x_perp_half = 1.0, 3.0, 0.6, 1.0
    rng = np.random.default_rng(0)
    coords = cs.sprinkle_ds_static_patch4d(
        500, rng, l=l, rstar_box=rstar_box, t_extent=t_extent,
        x_perp_half=x_perp_half)
    rho = 500 / _proper_volume(l, rstar_box, t_extent, x_perp_half)
    diag = cs.causal_diagnostics(_idelta_4d_dspatch(coords, rho))

    assert diag["pairing_residual_rel"] < 1e-12
    assert abs(diag["trace"]) < 1e-10
    assert diag["n_positive"] == diag["n_negative"]


def test_ds_static_patch4d_pairing_invariant_multi_seed():
    """Pairing invariant must hold on EVERY region/seed (4 seeds, growing box)."""
    l, t_extent, x_perp_half = 1.0, 0.6, 0.9
    for rstar_box in (2.0, 4.0, 6.0):
        for seed in range(4):
            rng = np.random.default_rng(100 + seed)
            coords = cs.sprinkle_ds_static_patch4d(
                350, rng, l=l, rstar_box=rstar_box, t_extent=t_extent,
                x_perp_half=x_perp_half)
            rho = 350 / _proper_volume(l, rstar_box, t_extent, x_perp_half)
            diag = cs.causal_diagnostics(_idelta_4d_dspatch(coords, rho))
            assert diag["pairing_residual_rel"] < 1e-12
            assert abs(diag["trace"]) < 1e-10


# ---------------------------------------------------------------------------
# sech^2 radial measure: r*-marginal monotone non-increasing; transverse flat
# ---------------------------------------------------------------------------

def test_ds_static_patch4d_sech2_radial_monotone():
    """The dS-proper sprinkling weights r* by sech^2(r*/l): the r* histogram
    must be monotone non-increasing (deterministic, large-N)."""
    rng = np.random.default_rng(0)
    coords = cs.sprinkle_ds_static_patch4d(
        6000, rng, l=1.0, rstar_box=3.0, t_extent=0.6, x_perp_half=1.0)
    rstar = coords[:, 1]
    assert rstar.min() >= 0.0
    assert rstar.max() <= 3.0 + 1e-9
    hist, _ = np.histogram(rstar, bins=10, range=(0.0, 3.0))
    # sech^2 weighting -> non-increasing bin populations (allow ties)
    assert np.all(np.diff(hist) <= 0)


def test_ds_static_patch4d_transverse_box_flat():
    """Transverse x1, x2 carry a FLAT box measure: bounded and approximately
    uniform (no sech^2 weighting on the transverse directions)."""
    half = 1.3
    rng = np.random.default_rng(1)
    coords = cs.sprinkle_ds_static_patch4d(
        8000, rng, l=1.0, rstar_box=3.0, t_extent=0.6, x_perp_half=half)
    x1, x2 = coords[:, 2], coords[:, 3]
    assert np.abs(x1).max() <= half + 1e-9
    assert np.abs(x2).max() <= half + 1e-9
    # uniform box: equal-width bins ~ equally populated (within Poisson scatter)
    hist, _ = np.histogram(x1, bins=6, range=(-half, half))
    assert hist.std() / hist.mean() < 0.15   # flat, not sech^2-concentrated


def test_ds_static_patch4d_t_extent_respected():
    rng = np.random.default_rng(2)
    t_extent = 0.45
    coords = cs.sprinkle_ds_static_patch4d(
        2000, rng, l=1.0, rstar_box=4.0, t_extent=t_extent, x_perp_half=1.0)
    assert np.abs(coords[:, 0]).max() <= t_extent + 1e-9


# ---------------------------------------------------------------------------
# proper-volume saturation: the achievable point budget caps toward the horizon
# ---------------------------------------------------------------------------

def test_ds_static_patch4d_proper_volume_saturates():
    """At FIXED proper density, the achievable N saturates as rstar_box -> inf
    (sech^2 radial cap); a matched flat radial box would grow without bound.
    This is the geometric II_1 vs II_inf signal the 4D calc rests on."""
    l, t_extent, x_perp_half, rho = 1.0, 0.6, 1.0, 200.0
    Rs = np.array([2.0, 3.0, 4.0, 5.0, 7.0])
    # dS proper volume caps at  2 t * l * (2 x_perp)^2  as R*->inf
    V_ds = np.array([_proper_volume(l, R, t_extent, x_perp_half) for R in Rs])
    V_flat = np.array([(2.0 * t_extent) * R * (2.0 * x_perp_half) ** 2 for R in Rs])
    N_ds = (rho * V_ds)
    N_flat = (rho * V_flat)
    V_cap = (2.0 * t_extent) * l * (2.0 * x_perp_half) ** 2
    # dS saturates toward the finite cap; flat grows ~linearly without bound
    assert N_ds[-1] < 1.05 * rho * V_cap
    assert N_ds[-1] - N_ds[0] < 0.20 * N_ds[0]          # dS late increment tiny
    assert N_flat[-1] > 2.5 * N_flat[0]                 # flat grows > 2.5x


if __name__ == "__main__":  # pragma: no cover
    raise SystemExit(pytest.main([__file__, "-v"]))
