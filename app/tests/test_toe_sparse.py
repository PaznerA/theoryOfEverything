# -*- coding: utf-8 -*-
"""Tests for the v0.3.0 SPARSE / ITERATIVE path (large-N SJ + SSEE).

The sparse path provides a matrix-FREE Hermitian Pauli-Jordan operator
(``toe.causet.idelta_operator_2d``), a top-k iterative SJ state
(``toe.sj.sj_state_sparse`` via ``scipy.sparse.linalg.eigsh``), and a truncated
SSEE from the k-mode data (``toe.entropy.ssee_sparse``). It lets the SJ + SSEE
pipelines reach N ~ 1e4 (sprinkling density rho ~ 1e3-1e4 in 2D) without
materialising a dense float iDelta -- needed by H5g-2 (A/4 cap) and the
VYPOCET-19 Part-3 tracial probe.

VALIDATION (the heart of the task) -- at OVERLAP sizes N in {1000, 2000} the
sparse path must MATCH the dense path:
  * top-k eigenvalues:    rel diff < 1e-8   (we get ~1e-14 with float64);
  * truncated SSEE S:     rel diff < 1e-6   (we get ~1e-13 with float64);
  * +/- pairing invariant of the operator (apply to random vectors).
Plus ONE scaling smoke: N=8000 2D diamond, k=600 eigsh completes < 120 s and the
top eigenvalue follows the dense N<=2000 trend (loose).

The dense reference uses the NULL-COORD causal order (the ssee-diamond /
sj-vn-type convention) via toe.entropy._causal_from_null, exactly as the
existing test_toe_entropy.py does, so the committed-convention S values match.
The sparse operator sorts points by the first null coordinate; sub-region
indices are mapped through the returned ``perm`` so the comparison is
permutation-consistent.

All tests run under MPLBACKEND=Agg. Total runtime target: < 90 s.
"""

import time

import numpy as np
import pytest

from toe.causet import (
    sprinkle_diamond2d,
    green_retarded_2d,
    pauli_jordan,
    causal_blocks_2d,
    idelta_operator_2d,
)
from toe.entropy import _causal_from_null, kappa_2d, ssee, ssee_sparse
from toe.sj import sj_state, sj_state_sparse, SJStateSparse


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _dense_reference(N, seed):
    """Dense (iDelta, W, coords, kappa, sub_idx) in the NULL-COORD convention."""
    rng = np.random.default_rng(seed)
    coords = sprinkle_diamond2d(N, rng)
    C = _causal_from_null(coords)
    iD = pauli_jordan(green_retarded_2d(C))
    st = sj_state(iD)
    kap = kappa_2d(N)
    sub = np.where((np.abs(coords[:, 0]) <= 0.5)
                   & (np.abs(coords[:, 1]) <= 0.5))[0]
    return iD, st.W, coords, kap, sub


def _sparse_sj(coords, k, *, dtype, eig_seed, tol):
    """Build the matrix-free operator and the top-k sparse SJ state.

    Returns (sj_sparse, perm, coords_perm)."""
    op, perm = idelta_operator_2d(coords, dtype=dtype)
    rng = np.random.default_rng(eig_seed)
    sjs = sj_state_sparse(op, k, rng=rng, tol=tol)
    return sjs, perm, coords[perm]


# These overlap sizes are the smallest convincing pair (kappa-mode counts 124 /
# 178; k captures them with margin). Both run in a couple of seconds each.
_OVERLAP = [(1000, 256), (2000, 320)]
_SEED = 7_000_000


# ---------------------------------------------------------------------------
# 1. Matrix-free operator: shape, Hermiticity, +/- pairing
# ---------------------------------------------------------------------------

class TestOperator:
    def test_blocks_match_dense_causal_order(self):
        """causal_blocks_2d reproduces the null-coord causal matrix (up to the
        u-sort permutation)."""
        N = 600
        coords = sprinkle_diamond2d(N, np.random.default_rng(_SEED + N))
        C_dense = _causal_from_null(coords)
        C_blk, perm = causal_blocks_2d(coords, dtype=np.float64)
        # apply the same permutation to the dense reference
        C_perm = C_dense[np.ix_(perm, perm)]
        assert np.array_equal(C_blk, C_perm)

    def test_operator_is_hermitian(self):
        """<y, A x> == conj(<x, A y>) for random complex vectors (machine prec)."""
        N = 800
        coords = sprinkle_diamond2d(N, np.random.default_rng(_SEED + N))
        op, _ = idelta_operator_2d(coords, dtype=np.float64)
        gen = np.random.default_rng(3)
        x = gen.standard_normal(N) + 1j * gen.standard_normal(N)
        y = gen.standard_normal(N) + 1j * gen.standard_normal(N)
        lhs = np.vdot(y, op.matvec(x))
        rhs = np.conj(np.vdot(x, op.matvec(y)))
        assert abs(lhs - rhs) < 1e-9

    def test_plus_minus_pairing_invariant(self):
        """The operator's top spectrum is exactly +/- paired (antisymmetry of
        Delta is exact in float). Apply eigsh and check w + reversed(w) ~ 0 and
        the captured trace ~ 0."""
        N = 800
        coords = sprinkle_diamond2d(N, np.random.default_rng(_SEED + N))
        op, _ = idelta_operator_2d(coords, dtype=np.float64)
        sjs = sj_state_sparse(op, 200, rng=np.random.default_rng(11), tol=0)
        w = np.sort(sjs.eigvals)
        max_abs = np.max(np.abs(w))
        pairing_rel = np.max(np.abs(w + w[::-1])) / max_abs
        assert pairing_rel < 1e-10
        # balanced ends -> captured sub-trace vanishes
        assert abs(np.sum(w)) / max_abs < 1e-10

    def test_pairing_on_random_vectors_real_quadratic_form(self):
        """<x, A x> is REAL for the Hermitian operator (the +/- pairing makes the
        quadratic form real on any random vector)."""
        N = 700
        coords = sprinkle_diamond2d(N, np.random.default_rng(_SEED + N))
        op, _ = idelta_operator_2d(coords, dtype=np.float64)
        gen = np.random.default_rng(5)
        for _ in range(4):
            x = gen.standard_normal(N) + 1j * gen.standard_normal(N)
            q = np.vdot(x, op.matvec(x))
            assert abs(q.imag) < 1e-9 * (abs(q) + 1.0)


# ---------------------------------------------------------------------------
# 2. Determinism: eigsh v0 derived from the rng -> reproducible restarts
# ---------------------------------------------------------------------------

class TestDeterminism:
    def test_equal_seed_identical_spectrum(self):
        """Two calls with equal-seed generators give bit-identical eigenvalues."""
        N = 1000
        coords = sprinkle_diamond2d(N, np.random.default_rng(_SEED + N))
        op, _ = idelta_operator_2d(coords, dtype=np.float64)
        a = sj_state_sparse(op, 200, rng=np.random.default_rng(42), tol=0)
        b = sj_state_sparse(op, 200, rng=np.random.default_rng(42), tol=0)
        assert np.array_equal(a.eigvals, b.eigvals)
        assert np.array_equal(a.eigvecs, b.eigvecs)

    def test_k_ge_N_rejected(self):
        N = 200
        coords = sprinkle_diamond2d(N, np.random.default_rng(_SEED + N))
        op, _ = idelta_operator_2d(coords, dtype=np.float64)
        with pytest.raises(ValueError):
            sj_state_sparse(op, N, rng=np.random.default_rng(0))


# ---------------------------------------------------------------------------
# 3. OVERLAP validation: sparse top-k eigenvalues match dense (< 1e-8)
# ---------------------------------------------------------------------------

class TestEigenvalueOverlap:
    @pytest.mark.parametrize("N,k", _OVERLAP)
    def test_topk_eigenvalues_match_dense(self, N, k):
        iD, _, coords, _, _ = _dense_reference(N, _SEED + 1000 * N)
        w_dense = np.linalg.eigvalsh(iD)
        # top-k by magnitude of the dense spectrum
        idx = np.argsort(np.abs(w_dense))[::-1][:k]
        top_dense = np.sort(w_dense[idx])

        sjs, _, _ = _sparse_sj(coords, k, dtype=np.float64,
                               eig_seed=12345, tol=0)
        top_sparse = np.sort(sjs.eigvals)

        max_abs = np.max(np.abs(top_dense))
        rel = np.max(np.abs(top_sparse - top_dense)) / max_abs
        assert rel < 1e-8, f"N={N} k={k}: top-k eig rel diff {rel:.2e}"

    @pytest.mark.parametrize("N,k", _OVERLAP)
    def test_topk_captures_above_kappa(self, N, k):
        """The captured top-k set must contain ALL |lambda| > kappa modes, else
        the truncated SSEE would under-count."""
        iD, _, coords, kap, _ = _dense_reference(N, _SEED + 1000 * N)
        w_dense = np.linalg.eigvalsh(iD)
        n_above = int(np.sum(np.abs(w_dense) > kap))
        # k must capture > n_above modes (with the +/- balance, k/2 per side)
        assert k > n_above
        sjs, _, _ = _sparse_sj(coords, k, dtype=np.float64,
                               eig_seed=12345, tol=0)
        # smallest captured magnitude must be below kappa (so the cut is inside)
        assert np.min(np.abs(sjs.eigvals)) < kap


# ---------------------------------------------------------------------------
# 4. OVERLAP validation: truncated SSEE matches dense (< 1e-6)
# ---------------------------------------------------------------------------

class TestSSEEOverlap:
    @pytest.mark.parametrize("N,k", _OVERLAP)
    def test_truncated_ssee_matches_dense(self, N, k):
        iD, W, coords, kap, sub = _dense_reference(N, _SEED + 1000 * N)
        S_dense = ssee(W, iD, sub, kappa=kap).value

        sjs, perm, coords_p = _sparse_sj(coords, k, dtype=np.float64,
                                         eig_seed=12345, tol=0)
        sub_p = np.where((np.abs(coords_p[:, 0]) <= 0.5)
                         & (np.abs(coords_p[:, 1]) <= 0.5))[0]
        meas = ssee_sparse(sjs, sub_p, kappa=kap)
        S_sparse = meas.value

        rel = abs(S_sparse - S_dense) / abs(S_dense)
        assert rel < 1e-6, f"N={N} k={k}: S_trunc rel diff {rel:.2e}"
        assert meas.n > 0

    def test_returns_measurement_shape(self):
        N, k = 1000, 256
        _, _, coords, kap, _ = _dense_reference(N, _SEED + 1000 * N)
        sjs, perm, coords_p = _sparse_sj(coords, k, dtype=np.float64,
                                         eig_seed=1, tol=0)
        sub_p = np.where((np.abs(coords_p[:, 0]) <= 0.5)
                         & (np.abs(coords_p[:, 1]) <= 0.5))[0]
        meas = ssee_sparse(sjs, sub_p, kappa=kap)
        assert hasattr(meas, "value") and hasattr(meas, "se")
        assert meas.se == 0.0

    def test_n_max_rank_truncation_runs(self):
        """The n_max rank-cut branch of ssee_sparse produces a finite entropy."""
        N, k = 2000, 320
        _, _, coords, _, _ = _dense_reference(N, _SEED + 1000 * N)
        sjs, perm, coords_p = _sparse_sj(coords, k, dtype=np.float64,
                                         eig_seed=2, tol=0)
        sub_p = np.where((np.abs(coords_p[:, 0]) <= 0.5)
                         & (np.abs(coords_p[:, 1]) <= 0.5))[0]
        meas = ssee_sparse(sjs, sub_p, n_max=80,
                           kappa=kappa_2d(N))
        assert np.isfinite(meas.value)


# ---------------------------------------------------------------------------
# 5. Carrier type
# ---------------------------------------------------------------------------

class TestCarrier:
    def test_sjstatesparse_fields(self):
        N, k = 1000, 200
        _, _, coords, _, _ = _dense_reference(N, _SEED + 1000 * N)
        sjs, _, _ = _sparse_sj(coords, k, dtype=np.float64, eig_seed=0, tol=0)
        assert isinstance(sjs, SJStateSparse)
        assert sjs.k == k
        assert sjs.eigvecs.shape == (N, k)
        # eigvals ascending; pos_spectrum descending
        assert np.all(np.diff(sjs.eigvals) >= -1e-12)
        assert np.all(np.diff(sjs.pos_spectrum) <= 1e-12)
        # +/- balance: about half positive
        assert abs((sjs.eigvals > 0).sum() - k // 2) <= 2


# ---------------------------------------------------------------------------
# 6. SCALING SMOKE: N=8000, k=600 eigsh < 120 s, top-eig follows the trend
# ---------------------------------------------------------------------------

class TestScalingSmoke:
    def test_N8000_k600_under_120s_and_trend(self):
        """N=8000 2D diamond, k=600 eigsh completes < 120 s (float32 operator)
        and the top eigenvalue follows the dense small-N trend (loose).

        Trend: the top |lambda| of the 2D diamond iDelta grows ~linearly in N
        (max|lambda| ~ 0.21 N empirically: 210 at N=1000, 429 at N=2000). So at
        N=8000 we expect the top eigenvalue to be O(1e3) and clearly above the
        N=2000 value -- a loose monotone-trend check, not a precise number.
        """
        # dense small-N anchor for the trend (N=2000)
        iD2, _, _, _, _ = _dense_reference(2000, _SEED + 1000 * 2000)
        top2000 = float(np.max(np.abs(np.linalg.eigvalsh(iD2))))

        N, k = 8000, 600
        coords = sprinkle_diamond2d(N, np.random.default_rng(_SEED + 1000 * N))
        op, _ = idelta_operator_2d(coords, dtype=np.float32)

        t0 = time.time()
        sjs = sj_state_sparse(op, k, rng=np.random.default_rng(7),
                              tol=1e-9)
        elapsed = time.time() - t0

        assert elapsed < 120.0, f"N=8000 k=600 eigsh took {elapsed:.1f}s"
        top8000 = float(np.max(np.abs(sjs.eigvals)))
        # loose trend: 8000-point top eig well above the 2000-point one and in
        # the right ballpark (max|lambda| ~ 0.21 N -> ~1700 at N=8000).
        assert top8000 > 2.0 * top2000
        assert 800.0 < top8000 < 3000.0
        assert sjs.eigvecs.shape == (N, k)
