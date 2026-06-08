# -*- coding: utf-8 -*-
"""Validation tests for the VYPOCET-27 library extension
``toe.causet.horizon_molecules_codim2`` -- the CORRECTED Dou-Sorkin codim-2
horizon-molecule count that fixes the ``A_mol ~ rho^{1.77}`` codim-1-worldtube
artefact of VYPOCET-25 / ``compute/drivers/ds_cap_4d.py:horizon_link_count_4d``.

Targets:

* basic correctness on a tiny hand-checkable causal set (a single straddling
  link inside the tube is one molecule; a long near-null straddle is excluded);
* the molecule count is a STRICT subset of the raw codim-1 worldtube
  straddling-link count (the convention audit ratio mol/raw < 1);
* SCALING: on ``sprinkle_ds_static_patch4d`` the codim-2 count scales as
  ``rho^{~0.5-0.7}`` (proper area), DECISIVELY below the raw ``rho^{1.77}``.

Runtime budget: << 30 s (largest matrix N ~ 1900, three densities, 3 seeds).
Seeds are passed explicitly everywhere (np.random.default_rng).
"""

import numpy as np
import pytest

from toe import causet as cs


def _proper_volume(l, rstar_box, t_extent, x_perp_half):
    return (2.0 * t_extent) * (l * np.tanh(rstar_box / l)) * (2.0 * x_perp_half) ** 2


# ---------------------------------------------------------------------------
# basic correctness: a tiny, fully hand-checkable causal set
# ---------------------------------------------------------------------------

def test_codim2_basic_single_molecule_in_tube():
    """Two points straddling r*=r_cut, a short timelike link through t=0, both
    within the proper tube -> exactly one molecule. A third far-future point on
    the same side adds NO molecule (no straddle)."""
    # coords = (t, r*, x1, x2); r_cut = 1.0, eps = 0.5, k_tube = 1.5 -> radius 0.75
    # Points 0,1 straddle the cut with a clearly TIMELIKE link (dt=0.3 > dr*=0.1).
    coords = np.array([
        [-0.15, 0.95, 0.0, 0.0],   # 0: in O (r* < 1), just below cut, t<0
        [+0.15, 1.05, 0.0, 0.0],   # 1: in O^c (r* > 1), just above cut, t>0
        [+5.00, 0.90, 0.0, 0.0],   # 2: far-future, in O (no straddle with 0)
    ])
    C = cs.causal_matrix(coords)
    n = cs.horizon_molecules_codim2(coords, C, r_cut=1.0, eps=0.5, k_tube=1.5)
    assert n == 1


def test_codim2_excludes_long_near_null_straddle():
    """A straddling link whose endpoints are FAR from the codim-2 2-surface in
    the (t, r*) normal plane (a long near-null link reaching across a big
    transverse gap) is NOT a codim-2 molecule, even though it crosses the cut."""
    coords = np.array([
        [-0.40, 0.95, 0.00, 0.0],   # 0: in O, but |t| large vs tube radius
        [+0.40, 1.05, 0.90, 0.0],   # 1: in O^c, big transverse x1 (near-null link)
    ])
    C = cs.causal_matrix(coords)
    # raw worldtube straddle counts this link; codim-2 (tube radius 0.75) does not
    n, diag = cs.horizon_molecules_codim2(
        coords, C, r_cut=1.0, eps=0.5, k_tube=1.5, return_diagnostics=True)
    assert n == 0
    assert diag["n_raw_worldtube_links"] >= n


def test_codim2_accepts_causal_or_link_matrix():
    """Passing the causal matrix or the pre-reduced link matrix gives the same
    molecule count (the routine reduces C internally; an L is used as-is)."""
    rng = np.random.default_rng(3)
    coords = cs.sprinkle_ds_static_patch4d(
        400, rng, l=1.0, rstar_box=4.0, t_extent=0.5, x_perp_half=1.0)
    C = cs.causal_matrix(coords)
    L = cs.link_matrix(C)
    n_from_C = cs.horizon_molecules_codim2(coords, C, r_cut=1.0, eps=0.3, k_tube=1.5)
    n_from_L = cs.horizon_molecules_codim2(coords, L, r_cut=1.0, eps=0.3, k_tube=1.5)
    assert n_from_C == n_from_L


# ---------------------------------------------------------------------------
# convention audit: molecules are a STRICT subset of the raw worldtube count
# ---------------------------------------------------------------------------

def test_codim2_is_subset_of_raw_worldtube():
    """The corrected codim-2 molecule count must be <= the raw codim-1 worldtube
    straddling-link count (it is a tube-confined subset), and strictly smaller in
    a dense 4D patch (the worldtube carries far more bulk straddles)."""
    rng = np.random.default_rng(7)
    coords = cs.sprinkle_ds_static_patch4d(
        1900, rng, l=1.0, rstar_box=4.3, t_extent=0.5, x_perp_half=1.0)
    C = cs.causal_matrix(coords)
    n_mol, diag = cs.horizon_molecules_codim2(
        coords, C, r_cut=1.0, eps=480.0 ** -0.25, k_tube=1.5,
        return_diagnostics=True)
    assert n_mol <= diag["n_raw_worldtube_links"]
    assert n_mol < diag["n_raw_worldtube_links"]      # strict in a dense patch
    assert 0.0 < diag["mol_over_raw"] < 1.0


# ---------------------------------------------------------------------------
# THE decisive scaling: codim-2 ~ rho^{~0.5}, far below raw rho^{1.77}
# ---------------------------------------------------------------------------

def test_codim2_scaling_is_area_like_not_worldtube():
    """On the 4D dS static patch the codim-2 molecule count scales as a proper
    AREA (exponent ~0.4-0.8, target rho^{0.5}), DECISIVELY below the raw codim-1
    worldtube link count (~rho^{1.77}). This is the VYPOCET-27 convention fix."""
    l, Rbox, t_extent, x_perp_half, r_cut = 1.0, 4.3, 0.5, 1.0, 1.0
    rhos = [120.0, 240.0, 480.0]
    mol_means, raw_means = [], []
    for rho in rhos:
        N = int(round(rho * _proper_volume(l, Rbox, t_extent, x_perp_half)))
        eps = rho ** -0.25
        mols, raws = [], []
        for s in range(3):
            rng = np.random.default_rng(900 + 100 * int(rho) + s)
            coords = cs.sprinkle_ds_static_patch4d(
                N, rng, l=l, rstar_box=Rbox, t_extent=t_extent,
                x_perp_half=x_perp_half)
            C = cs.causal_matrix(coords)
            n_mol, diag = cs.horizon_molecules_codim2(
                coords, C, r_cut=r_cut, eps=eps, k_tube=1.5,
                return_diagnostics=True)
            mols.append(n_mol)
            raws.append(diag["n_raw_worldtube_links"])
        mol_means.append(np.mean(mols))
        raw_means.append(np.mean(raws))

    lr = np.log(rhos)
    p_mol = np.polyfit(lr, np.log(mol_means), 1)[0]
    p_raw = np.polyfit(lr, np.log(raw_means), 1)[0]
    # raw worldtube count reproduces the rho^{1.77} artefact (well above 1.4)
    assert p_raw > 1.4
    # codim-2 molecule count is area-like: comfortably in (0.3, 0.95),
    # and DECISIVELY below the raw worldtube exponent
    assert 0.3 < p_mol < 0.95
    assert p_mol < p_raw - 0.7


if __name__ == "__main__":  # pragma: no cover
    raise SystemExit(pytest.main([__file__, "-v"]))
