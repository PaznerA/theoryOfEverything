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
    kms_temperature,
    KMSFit,
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


def test_kms_temperature_sj_modular_flow_is_beta1():
    """KMS fit of an SJ modular flow: for occupations n_k = mu_k - 1 and modular
    energies eps_k = ln[mu_k/(mu_k-1)] the detailed-balance n/(n+1) = e^{-eps}
    holds, so the KMS inverse-temperature is beta = 1 (Tomita-Takesaki /
    Casini-Huerta) and the residual at beta=1 is machine-zero."""
    rng = np.random.default_rng(0)
    mu = 1.0 + rng.uniform(0.05, 5.0, size=40)          # mu > 1 (occupied modes)
    eps = np.log(mu / (mu - 1.0))
    occ = mu - 1.0
    kf = kms_temperature(eps, occ)
    assert isinstance(kf, KMSFit)
    # KMS condition is satisfied at beta=1 to machine precision
    assert kf.resid_beta1 < 1e-9
    # the minimising beta is 1 (on the default grid spacing ~0.01)
    assert abs(kf.beta - 1.0) < 0.02
    assert kf.n_modes == 40
    assert len(kf.ts) == len(kf.g_re) == len(kf.g_im)


def test_kms_temperature_scales_with_beta():
    """A thermal spectrum at inverse-temperature b (n/(n+1) = e^{-b*eps}) is
    recovered as beta = b: rescaling the occupation law shifts the KMS minimum."""
    rng = np.random.default_rng(1)
    eps = rng.uniform(0.2, 3.0, size=50)
    b_true = 0.7
    occ = 1.0 / (np.exp(b_true * eps) - 1.0)            # Bose law at beta=b_true
    kf = kms_temperature(eps, occ, betas=np.linspace(0.3, 1.5, 241))
    assert abs(kf.beta - b_true) < 0.02


def test_kms_temperature_degenerate_returns_nan():
    """Fewer than two modes -> NaN beta, empty curves (clean partial output)."""
    kf = kms_temperature(np.array([1.0]), np.array([0.5]))
    assert kf.n_modes == 1
    assert np.isnan(kf.beta)
    assert kf.ts == [] and kf.g_re == []
