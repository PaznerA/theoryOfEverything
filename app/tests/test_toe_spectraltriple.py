# -*- coding: utf-8 -*-
"""Validation tests for toe.spectraltriple (finite spectral-triple primitives).

Targets (all small-N, < 30 s total):

  * dirac_from_kernel: D_K = sgn(K) sqrt(|K|) is Hermitian and squares to |K|
    to machine precision; its spectrum equals sign(lam) sqrt(|lam|) of the
    eigenvalues lam of K (the symmetric functional calculus).

  * connes_commutator_norm: equals the largest singular value of the explicit
    [D, a]_ij = D_ij (a_j - a_i) matrix, and vanishes for a constant function.

  * connes_distance on a CANONICAL 1D nearest-neighbour Dirac chain
    D = i(S - S^T) (off-diagonal coupling 1): the spectral distance between
    ADJACENT sites is exactly 1, and the distance is monotone non-decreasing in
    index separation along the chain (the Connes distance reproduces the lattice
    metric of a 1D Dirac operator).

References (verified): Connes 'Noncommutative Geometry' (1994) -- spectral
distance; Casini-Huerta 0905.2562 / Sorkin-Yazdi 1611.10281 (the modular-kernel
context the Dirac candidate is built from).
"""

import numpy as np

from toe.spectraltriple import (
    dirac_from_kernel,
    connes_commutator_norm,
    connes_distance,
    ConnesDistance,
)


def _hermitian(n, seed):
    rng = np.random.default_rng(seed)
    A = rng.standard_normal((n, n)) + 1j * rng.standard_normal((n, n))
    return A + A.conj().T


def test_dirac_from_kernel_squares_to_abs_K():
    """D_K = sgn(K) sqrt(|K|): Hermitian, D_K^2 == |K|, spec matches f(lam)."""
    K = _hermitian(10, seed=0)
    D = dirac_from_kernel(K)
    # Hermitian
    assert np.max(np.abs(D - D.conj().T)) < 1e-12
    # D^2 == |K| (positive operator with same eigenvectors as K)
    lam, U = np.linalg.eigh(0.5 * (K + K.conj().T))
    absK = (U * np.abs(lam)) @ U.conj().T
    assert np.max(np.abs(D @ D - absK)) < 1e-10
    # spectrum equals sign(lam) sqrt(|lam|)
    lamD = np.linalg.eigvalsh(D)
    target = np.sort(np.sign(lam) * np.sqrt(np.abs(lam)))
    assert np.max(np.abs(np.sort(lamD) - target)) < 1e-12


def test_commutator_norm_formula_and_constant():
    """connes_commutator_norm == sigma_max([D,a]); zero for constant a."""
    D = _hermitian(8, seed=1)
    a = np.linspace(-1.0, 2.0, 8)
    comm = D * (a[None, :] - a[:, None])
    expected = float(np.linalg.norm(comm, ord=2))
    got = connes_commutator_norm(D, a)
    assert abs(got - expected) < 1e-10
    # constant function -> zero commutator
    assert connes_commutator_norm(D, np.full(8, 3.14)) < 1e-12


def test_connes_distance_1d_chain_adjacent_is_one():
    """Canonical 1D Dirac chain: adjacent-site Connes distance == 1 (lattice
    metric), and distance is monotone in index separation."""
    n = 8
    S = np.zeros((n, n))
    for k in range(n - 1):
        S[k, k + 1] = 1.0
    D = 1j * (S - S.T)              # Hermitian nearest-neighbour Dirac
    # adjacent sites: exact spectral distance is 1 for coupling-1 chain
    d01 = connes_distance(D, 0, 1, seed=3, n_random=16, n_iter=50)
    assert abs(d01 - 1.0) < 0.05
    # monotone non-decreasing along the chain
    ds = [connes_distance(D, 0, j, seed=3, n_random=16, n_iter=50)
          for j in range(1, n)]
    for a, b in zip(ds, ds[1:]):
        assert b >= a - 0.05
    # the far end is genuinely farther than the near neighbour
    assert ds[-1] > ds[0] + 0.5


def test_connes_distance_carrier_unit_commutator():
    """return_carrier gives a ConnesDistance whose optimiser has unit commutator
    norm (Lipschitz-tight) and the distance matches the scalar call."""
    n = 6
    S = np.zeros((n, n))
    for k in range(n - 1):
        S[k, k + 1] = 1.0
    D = 1j * (S - S.T)
    c = connes_distance(D, 0, 3, seed=5, n_random=16, n_iter=50,
                        return_carrier=True)
    assert isinstance(c, ConnesDistance)
    assert c.i == 0 and c.j == 3
    # optimiser normalised to (approximately) unit commutator norm
    assert abs(c.commutator_norm - 1.0) < 0.1
    scalar = connes_distance(D, 0, 3, seed=5, n_random=16, n_iter=50)
    assert abs(c.value - scalar) < 1e-9
