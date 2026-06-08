# -*- coding: utf-8 -*-
"""Validation tests for the VYPOCET-34 / H6g-6 library extension
``toe.causet.molecule_count_fluctuation`` -- the across-sprinkling DISTRIBUTION
of the codim-2 Dou-Sorkin horizon-molecule count (Sorkin "order-by-disorder" /
horizon-entropy-FLUCTUATION observable), as opposed to the MEAN count of
``horizon_molecules_codim2`` (VYPOCET-27 / F-031).

Targets:

* the helper draws ``n_seeds`` independent sprinklings and returns a per-seed
  count array plus consistent summary stats (mean/var/std/fano/s_fluc);
* the stats are internally consistent (std = sqrt(var), fano = var/mean,
  s_fluc = 0.5 ln(2 pi e var)) and match a direct recomputation;
* determinism: the same ``(seed0, stride)`` reproduces the same counts exactly;
* the per-seed counts equal calling ``horizon_molecules_codim2`` on the same
  rng stream (the helper is a thin loop, no hidden state);
* ``n_seeds < 2`` raises (a variance needs >= 2 samples).

Runtime budget: << 20 s (N ~ 480-960, a few dozen seeds).
Seeds are passed explicitly everywhere (np.random.default_rng).
"""

import math

import numpy as np
import pytest

from toe import causet as cs


def _mk(N):
    return lambda rng: cs.sprinkle_ds_static_patch4d(
        N, rng, l=1.0, rstar_box=4.3, t_extent=0.5, x_perp_half=1.0)


def test_fluctuation_stats_internally_consistent():
    """mean/var/std/fano/s_fluc are mutually consistent and match a direct
    recomputation from the returned per-seed count array."""
    counts, stats = cs.molecule_count_fluctuation(
        _mk(480), 24, r_cut=1.0, eps=120.0 ** -0.25, k_tube=1.5,
        seed0=34_000_000, stride=1)
    assert counts.shape == (24,)
    assert counts.dtype.kind in "iu"
    mu = counts.mean()
    var = counts.var(ddof=1)
    assert stats["mean"] == pytest.approx(mu)
    assert stats["var"] == pytest.approx(var)
    assert stats["std"] == pytest.approx(math.sqrt(var))
    assert stats["fano"] == pytest.approx(var / mu)
    assert stats["s_fluc"] == pytest.approx(0.5 * math.log(2 * math.pi * math.e * var))
    assert stats["var_se"] == pytest.approx(var * math.sqrt(2.0 / 23))
    assert stats["n_seeds"] == 24
    assert stats["min"] == int(counts.min())
    assert stats["max"] == int(counts.max())


def test_fluctuation_is_deterministic_from_seed():
    """The same (seed0, stride) reproduces the identical per-seed count array."""
    a, _ = cs.molecule_count_fluctuation(
        _mk(480), 12, r_cut=1.0, eps=120.0 ** -0.25, seed0=111, stride=7)
    b, _ = cs.molecule_count_fluctuation(
        _mk(480), 12, r_cut=1.0, eps=120.0 ** -0.25, seed0=111, stride=7)
    assert np.array_equal(a, b)


def test_fluctuation_matches_direct_molecule_count():
    """Each per-seed count equals horizon_molecules_codim2 evaluated on the same
    np.random.default_rng(seed0 + stride * i) stream -- the helper is a thin loop
    with no hidden state."""
    N, seed0, stride = 480, 555, 3
    counts, _ = cs.molecule_count_fluctuation(
        _mk(N), 6, r_cut=1.0, eps=240.0 ** -0.25, k_tube=1.5,
        seed0=seed0, stride=stride)
    for i in range(6):
        rng = np.random.default_rng(seed0 + stride * i)
        coords = cs.sprinkle_ds_static_patch4d(
            N, rng, l=1.0, rstar_box=4.3, t_extent=0.5, x_perp_half=1.0)
        C = cs.causal_matrix(coords)
        n = cs.horizon_molecules_codim2(
            coords, C, r_index=1, r_cut=1.0, eps=240.0 ** -0.25, k_tube=1.5)
        assert counts[i] == n


def test_fluctuation_requires_two_seeds():
    """A variance needs >= 2 samples; n_seeds < 2 raises ValueError."""
    with pytest.raises(ValueError):
        cs.molecule_count_fluctuation(
            _mk(480), 1, r_cut=1.0, eps=120.0 ** -0.25)


def test_fluctuation_is_super_poisson_in_4d():
    """The 4D codim-2 molecule count is super-Poisson (Fano = Var/mean > 1):
    near-null straddling links on the codim-2 surface cluster, so the variance
    exceeds the mean (the VYPOCET-34 / H6g-6 core finding -- this is why the
    fluctuation does NOT give a clean Poisson/area-law signal). Checked with a
    modest seed count, so the threshold is generous (Fano > 1.5)."""
    _, stats = cs.molecule_count_fluctuation(
        _mk(960), 40, r_cut=1.0, eps=240.0 ** -0.25, k_tube=1.5,
        seed0=34_000_000 + 99, stride=1)
    assert stats["fano"] > 1.5
    assert stats["var"] > stats["mean"]


if __name__ == "__main__":  # pragma: no cover
    raise SystemExit(pytest.main([__file__, "-v"]))
