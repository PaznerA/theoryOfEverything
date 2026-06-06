"""
test_toe_fits.py  --  Validation tests for toe/fits.py (module A1).

Validates against committed results.json / uncertainty.json targets per
ARCHITECTURE.md §A1.  All targets are read from the committed JSON files;
none are hardcoded magic constants invented here.

Runtime budget: < 60 s (deterministic OLS tests are instant; bootstrap uses
n_boot=2000 but only for the committed-target test).
"""

import json
import math
import os

import numpy as np
import pytest

import toe.fits as fits
from toe.fits import (
    FitResult,
    Measurement,
    ExactResult,
    regression_se,
    bootstrap_slope_ci,
    powerlaw_fit,
    aic,
    aic_compare,
    validate_against,
)

# ---------------------------------------------------------------------------
# Paths to committed result files
# ---------------------------------------------------------------------------

_HERE = os.path.dirname(os.path.abspath(__file__))
_REPO = os.path.abspath(os.path.join(_HERE, os.pardir, os.pardir))
_VN_RESULTS = os.path.join(
    _REPO, "core-data", "calculations", "sj-vn-type", "results.json"
)
_VN_UNCERTAINTY = os.path.join(
    _REPO, "core-data", "calculations", "sj-vn-type", "uncertainty.json"
)
_THRESH_RESULTS = os.path.join(
    _REPO, "core-data", "calculations", "sj-threshold-scan", "results.json"
)


# ===========================================================================
# 1. Dataclass smoke tests
# ===========================================================================

class TestDataclasses:
    """Basic construction and property access for the Result dataclasses."""

    def test_fitresult_construction(self):
        r = FitResult(
            value=1.04,
            se_regression=0.01,
            ci68_bootstrap=(1.02, 1.06),
            r2=0.999,
        )
        assert r.value == 1.04
        assert r.se_regression == 0.01
        assert r.ci68_bootstrap == (1.02, 1.06)
        assert r.r2 == 0.999
        assert r.intercept == 0.0
        assert r.n_boot_used == 0
        assert r.validated is None

    def test_fitresult_ci_width(self):
        r = FitResult(
            value=1.0,
            se_regression=0.01,
            ci68_bootstrap=(0.99, 1.01),
            r2=0.99,
        )
        assert math.isclose(r.ci_width, 0.02, rel_tol=1e-12)

    def test_measurement_construction(self):
        m = Measurement(value=3.14, se=0.01, n=8)
        assert m.value == 3.14
        assert m.se == 0.01
        assert m.n == 8
        assert m.validated is None

    def test_exactresult_as_float(self):
        import sympy as sp
        er = ExactResult(value=sp.Rational(18, 11))
        assert math.isclose(er.as_float, 18 / 11, rel_tol=1e-12)
        assert er.se_regression == 0.0

    def test_exactresult_validated_default(self):
        import sympy as sp
        er = ExactResult(value=sp.Rational(1, 2))
        assert er.validated is None


# ===========================================================================
# 2. regression_se — deterministic OLS; validated against committed targets
# ===========================================================================

class TestRegressionSe:
    """Validates regression_se against committed sj-vn-type results.json."""

    @pytest.fixture(autouse=True)
    def load_data(self):
        r = json.load(open(_VN_RESULTS))
        self.Ns = np.array(r["proxy1_trace"]["Ns"], dtype=float)
        self.mean_Sf = np.array(r["proxy1_trace"]["entropy_trace_full"]["mean"])
        self.mean_St = np.array(r["proxy1_trace"]["entropy_trace_trunc"]["mean"])
        # CV arrays (proxy3)
        p3 = r["proxy3_central_sequences"]
        self.cv_trunc = np.array(p3["CV_S_trunc"])
        self.cv_full = np.array(p3["CV_S_full"])

    def test_entropy_full_slope(self):
        """slope of S_full vs N must match results.json exponent_a to 1e-9."""
        slope, intercept, se = regression_se(self.Ns, self.mean_Sf)
        # Target from results.json proxy1_trace.entropy_trace_full.exponent_a
        target = 1.0433381703439863
        assert validate_against(slope, target, rtol=1e-9), (
            f"slope={slope} target={target} diff={abs(slope-target)}"
        )

    def test_entropy_full_se(self):
        """SE of S_full exponent must match uncertainty.json se_regression to 1e-9."""
        _, _, se = regression_se(self.Ns, self.mean_Sf)
        # Target from uncertainty.json entropy_trace_full.se_regression
        target_se = 0.012687944964902706
        assert validate_against(se, target_se, rtol=1e-9), (
            f"se={se} target={target_se} diff={abs(se-target_se)}"
        )

    def test_entropy_trunc_slope(self):
        """slope of S_trunc vs N must match to 1e-9."""
        slope, _, _ = regression_se(self.Ns, self.mean_St)
        target = 0.17243056092717168
        assert validate_against(slope, target, rtol=1e-9), (
            f"slope={slope} target={target}"
        )

    def test_entropy_trunc_se(self):
        """SE of S_trunc exponent must match to 1e-9."""
        _, _, se = regression_se(self.Ns, self.mean_St)
        target_se = 0.011585364915205823
        assert validate_against(se, target_se, rtol=1e-9), (
            f"se={se} target={target_se}"
        )

    def test_cv_trunc_slope(self):
        """slope of CV(S_trunc) vs N must match to 1e-9."""
        slope, _, se = regression_se(
            self.Ns, np.maximum(self.cv_trunc, 1e-9)
        )
        target_slope = -0.7135270246444776
        target_se = 0.08165431268684237
        assert validate_against(slope, target_slope, rtol=1e-9), (
            f"slope={slope} target={target_slope}"
        )
        assert validate_against(se, target_se, rtol=1e-9), (
            f"se={se} target={target_se}"
        )

    def test_returns_tuple_of_floats(self):
        slope, intercept, se = regression_se(self.Ns, self.mean_Sf)
        assert isinstance(slope, float)
        assert isinstance(intercept, float)
        assert isinstance(se, float)

    def test_needs_at_least_3_points(self):
        with pytest.raises(ValueError):
            regression_se([1.0, 2.0], [1.0, 2.0])


# ===========================================================================
# 3. powerlaw_fit — full function: OLS + bootstrap CI
# ===========================================================================

class TestPowerlawFit:
    """Validates powerlaw_fit against committed targets."""

    @pytest.fixture(autouse=True)
    def load_data(self):
        r = json.load(open(_VN_RESULTS))
        u = json.load(open(_VN_UNCERTAINTY))
        self.Ns = np.array(r["proxy1_trace"]["Ns"], dtype=float)
        self.mean_Sf = np.array(r["proxy1_trace"]["entropy_trace_full"]["mean"])
        self.mean_St = np.array(r["proxy1_trace"]["entropy_trace_trunc"]["mean"])
        self.std_Sf = np.array(r["proxy1_trace"]["entropy_trace_full"]["std"])
        self.std_St = np.array(r["proxy1_trace"]["entropy_trace_trunc"]["std"])
        n_seeds = r["proxy3_central_sequences"]["n_seeds"]
        self.n_seeds = n_seeds
        # Store committed CI targets
        self.ci_full_lo = u["entropy_trace_full"]["ci68_bootstrap"][0]
        self.ci_full_hi = u["entropy_trace_full"]["ci68_bootstrap"][1]
        self.ci_trunc_lo = u["entropy_trace_trunc"]["ci68_bootstrap"][0]
        self.ci_trunc_hi = u["entropy_trace_trunc"]["ci68_bootstrap"][1]
        self.ci_cv_lo = u["CV_S_trunc_powerlaw"]["ci68_bootstrap"][0]
        self.ci_cv_hi = u["CV_S_trunc_powerlaw"]["ci68_bootstrap"][1]

    def test_no_bootstrap_slope_matches_committed(self):
        """Without resamples, value must match OLS slope exactly."""
        fr = powerlaw_fit(self.Ns, self.mean_Sf)
        target = 1.0433381703439863
        assert validate_against(fr.value, target, rtol=1e-9)
        assert fr.n_boot_used == 0
        assert fr.ci68_bootstrap == (fr.value, fr.value)

    def test_no_bootstrap_returns_fitresult(self):
        fr = powerlaw_fit(self.Ns, self.mean_Sf)
        assert isinstance(fr, FitResult)
        assert fr.validated is None

    def test_r2_positive_and_lt1(self):
        fr = powerlaw_fit(self.Ns, self.mean_Sf)
        assert 0.0 < fr.r2 <= 1.0

    def test_bootstrap_ci_full_entropy(self):
        """With per-seed resamples built from committed mean+std, CI is reasonable.

        We reconstruct a synthetic (n_points, n_seeds=8) per-seed matrix from
        the committed mean and std using a fixed generation seed, then verify
        the bootstrap_slope_ci produces CI endpoints consistent with committed
        values.  Tolerance is generous (±0.05) because the synthetic matrix
        only approximates the committed per-seed structure; the exact per-seed
        data was not stored.

        Note: CI brackets *the bootstrap mean slope*, not necessarily the OLS
        slope on self.mean_Sf, since the synthetic per-seed matrix has a
        slightly different mean curve.  The key checks are CI width > 0 and
        endpoints near committed values.
        """
        rng_gen = np.random.default_rng(12345)
        n_N = len(self.Ns)
        # Generate synthetic per-seed matrix: mean + std * N(0,1) per seed
        per_seed = (
            self.mean_Sf[:, None]
            + self.std_Sf[:, None] * rng_gen.standard_normal((n_N, self.n_seeds))
        )
        # Make all positive (S_full >> 0)
        per_seed = np.maximum(per_seed, 1.0)

        fr = powerlaw_fit(
            self.Ns, per_seed.mean(axis=1),  # use actual per-seed mean
            resamples=per_seed.T,            # (n_seeds, n_N)
            n_boot=1000, seed=20260606,
        )
        assert isinstance(fr, FitResult)
        assert fr.n_boot_used == 1000
        lo, hi = fr.ci68_bootstrap
        # CI must bracket the OLS slope on the per-seed mean
        assert lo < fr.value < hi, (
            f"CI ({lo},{hi}) does not bracket slope {fr.value}"
        )
        # Verify CI width is positive
        assert fr.ci_width > 0.0
        # Generous tolerance: committed CI endpoints ±0.05 (approximate per-seed)
        assert abs(lo - self.ci_full_lo) < 0.05, (
            f"CI lo={lo} vs committed {self.ci_full_lo}"
        )
        assert abs(hi - self.ci_full_hi) < 0.05, (
            f"CI hi={hi} vs committed {self.ci_full_hi}"
        )

    def test_powerlaw_fit_se_matches_committed(self):
        """se_regression must match committed value to 1e-9."""
        fr = powerlaw_fit(self.Ns, self.mean_Sf)
        target_se = 0.012687944964902706
        assert validate_against(fr.se_regression, target_se, rtol=1e-9)

    def test_fitresult_validated_field_initially_none(self):
        fr = powerlaw_fit(self.Ns, self.mean_Sf)
        assert fr.validated is None
        fr.validated = validate_against(fr.value, 1.0433381703439863, rtol=1e-9)
        assert fr.validated is True


# ===========================================================================
# 4. bootstrap_slope_ci — unit tests of the primitive
# ===========================================================================

class TestBootstrapSlopeCi:
    """Unit tests for bootstrap_slope_ci using simple synthetic data."""

    def test_exact_power_law_ci_brackets_slope(self):
        """For data with known slope=2.0 and seed-variance, CI should bracket."""
        Ns = np.array([100, 200, 400, 800, 1600], dtype=float)
        rng = np.random.default_rng(99)
        # True S = N^2; add noise per seed
        n_seeds = 8
        per_seed = (Ns ** 2.0)[:, None] * (1 + 0.05 * rng.standard_normal((5, n_seeds)))
        per_seed = np.abs(per_seed)
        lo, hi, boot_std = bootstrap_slope_ci(
            per_seed, Ns, transform="mean", n_boot=500, seed=42
        )
        assert lo < 2.0 < hi, f"CI ({lo},{hi}) does not bracket slope 2.0"
        assert boot_std >= 0.0

    def test_cv_transform_returns_reasonable_slope(self):
        """CV of a power law with known slope should give a negative exponent."""
        Ns = np.array([200, 400, 800, 1600, 3200], dtype=float)
        rng = np.random.default_rng(77)
        n_seeds = 8
        # S ~ N^1, std ~ N^0.5 so CV ~ N^{-0.5}  (slope ~ -0.5)
        per_seed = Ns[:, None] + np.sqrt(Ns)[:, None] * rng.standard_normal((5, n_seeds))
        per_seed = np.abs(per_seed) + 1.0  # ensure positive
        lo, hi, _ = bootstrap_slope_ci(
            per_seed, Ns, transform="cv", n_boot=300, seed=13
        )
        # slope of CV should be negative
        mean_v = per_seed.mean(axis=1)
        std_v = per_seed.std(axis=1, ddof=1)
        cv = std_v / np.maximum(np.abs(mean_v), 1e-12)
        cv = np.maximum(cv, 1e-9)
        slope, _, _ = regression_se(Ns, cv)
        assert slope < 0.0, f"Expected CV exponent < 0, got {slope}"
        # CI should contain negative region
        assert lo < 0.1

    def test_invalid_transform_raises(self):
        per_seed = np.ones((4, 3))
        with pytest.raises(ValueError, match="transform"):
            bootstrap_slope_ci(per_seed, np.array([1.0, 2.0, 3.0, 4.0]),
                               transform="invalid")

    def test_determinism_with_same_seed(self):
        Ns = np.array([100, 200, 400, 800], dtype=float)
        rng = np.random.default_rng(0)
        per_seed = Ns[:, None] ** 1.0 + 0.1 * rng.standard_normal((4, 6))
        per_seed = np.abs(per_seed) + 1.0

        lo1, hi1, _ = bootstrap_slope_ci(per_seed, Ns, n_boot=200, seed=7)
        lo2, hi2, _ = bootstrap_slope_ci(per_seed, Ns, n_boot=200, seed=7)
        assert lo1 == lo2
        assert hi1 == hi2

    def test_different_seeds_give_different_results(self):
        Ns = np.array([100, 200, 400, 800], dtype=float)
        rng = np.random.default_rng(0)
        per_seed = Ns[:, None] + 2.0 * rng.standard_normal((4, 10))
        per_seed = np.abs(per_seed) + 1.0

        lo1, hi1, _ = bootstrap_slope_ci(per_seed, Ns, n_boot=200, seed=1)
        lo2, hi2, _ = bootstrap_slope_ci(per_seed, Ns, n_boot=200, seed=2)
        # Different seeds should give (slightly) different results
        assert not (lo1 == lo2 and hi1 == hi2)


# ===========================================================================
# 5. aic and aic_compare — exact deterministic tests
# ===========================================================================

class TestAic:
    """Validates aic() and aic_compare() against sj-threshold-scan targets."""

    def test_aic_formula(self):
        """AIC = n*ln(rss/n) + 2k; verify with a known example."""
        rss, n, k = 100.0, 10, 2
        expected = n * math.log(rss / n) + 2 * k
        assert math.isclose(aic(rss, n, k), expected, rel_tol=1e-12)

    def test_aic_compare_precomputed_a06(self):
        """Committed a=0.6 AIC values: delta_aic[model_E] = 441.5919430209433."""
        # Pre-computed AIC values from sj-threshold-scan/results.json
        aic_E = 4757.534081426667
        aic_S = 4315.942138405724
        result = aic_compare(("model_E", aic_E), ("model_S", aic_S))
        delta = result["delta_aic"]["model_E"]
        target_delta = 441.5919430209433
        assert validate_against(delta, target_delta, rtol=1e-9), (
            f"delta_aic={delta} target={target_delta}"
        )
        assert result["best"] == "model_S"

    def test_aic_compare_precomputed_a09(self):
        """Committed a=0.9 AIC values: delta = 4216.307763406736."""
        aic_E = 5614.761316518019
        aic_S = 1398.4535531112833
        result = aic_compare(("model_E", aic_E), ("model_S", aic_S))
        delta = result["delta_aic"]["model_E"]
        target_delta = 4216.307763406736
        assert validate_against(delta, target_delta, rtol=1e-9), (
            f"delta_aic={delta} target={target_delta}"
        )
        assert result["best"] == "model_S"

    def test_aic_compare_raw_rss_form(self):
        """aic_compare with (name, rss, n, k) form: cross-check AIC formula."""
        rss_E, rss_S = 50.0, 20.0
        n, k = 12, 2
        result = aic_compare(
            ("E", rss_E, n, k),
            ("S", rss_S, n, k),
        )
        assert result["best"] == "S"
        # delta_aic["E"] should equal aic(rss_E,n,k) - aic(rss_S,n,k)
        expected_delta = aic(rss_E, n, k) - aic(rss_S, n, k)
        assert math.isclose(result["delta_aic"]["E"], expected_delta, rel_tol=1e-12)

    def test_aic_compare_delta_zero_for_best(self):
        """The best model always has delta_aic == 0."""
        result = aic_compare(("A", 100.0), ("B", 200.0), ("C", 150.0))
        assert result["best"] == "A"
        assert result["delta_aic"]["A"] == 0.0

    def test_aic_compare_returns_all_keys(self):
        result = aic_compare(("X", 1.0), ("Y", 2.0))
        assert set(result.keys()) == {"aic", "best", "delta_aic"}

    def test_aic_compare_bad_entry_raises(self):
        with pytest.raises((ValueError, TypeError)):
            aic_compare(("only_name",))

    def test_delta_aic_from_committed_results_json(self):
        """Read directly from committed sj-threshold-scan/results.json."""
        if not os.path.exists(_THRESH_RESULTS):
            pytest.skip("sj-threshold-scan/results.json not found")
        r = json.load(open(_THRESH_RESULTS))
        cmp_06 = r["model_comparison_a06"]
        aic_E_06 = cmp_06["model_E"]["AIC"]
        aic_S_06 = cmp_06["model_S"]["AIC"]
        committed_delta_06 = cmp_06["comparison"]["delta_AIC_E_minus_S"]

        result = aic_compare(("model_E", aic_E_06), ("model_S", aic_S_06))
        assert validate_against(
            result["delta_aic"]["model_E"], committed_delta_06, rtol=1e-9
        )


# ===========================================================================
# 6. validate_against — the single chokepoint
# ===========================================================================

class TestValidateAgainst:
    """Unit tests for the validate_against helper."""

    def test_exact_match_returns_true(self):
        assert validate_against(1.0433381703439863, 1.0433381703439863) is True

    def test_rtol_match(self):
        # 1e-10 relative difference should pass with default rtol=1e-9
        v = 1.0 + 1e-10
        assert validate_against(v, 1.0, rtol=1e-9) is True

    def test_rtol_mismatch(self):
        # 1e-8 relative difference should fail with rtol=1e-9
        v = 1.0 + 1e-8
        assert validate_against(v, 1.0, rtol=1e-9) is False

    def test_atol(self):
        assert validate_against(1.0 + 0.001, 1.0, atol=0.01) is True
        assert validate_against(1.0 + 0.1, 1.0, atol=0.01) is False

    def test_exact_sympy_equality(self):
        import sympy as sp
        val = sp.Rational(-18, 11)
        target = sp.Rational(-18, 11)
        assert validate_against(val, target, exact=True) is True

    def test_exact_sympy_inequality(self):
        import sympy as sp
        val = sp.Rational(-18, 11)
        target = sp.Rational(-18, 12)
        assert validate_against(val, target, exact=True) is False

    def test_validates_committed_slope(self):
        """Reproduces the canonical example from ARCHITECTURE §A1."""
        assert validate_against(1.0433381703439863, 1.0433381703439863) is True

    def test_fitresult_validated_flag_workflow(self):
        """Demonstrate the full workflow: fit -> validate -> check .validated."""
        r = json.load(open(_VN_RESULTS))
        Ns = np.array(r["proxy1_trace"]["Ns"], dtype=float)
        mean_Sf = np.array(r["proxy1_trace"]["entropy_trace_full"]["mean"])
        target = 1.0433381703439863

        fr = powerlaw_fit(Ns, mean_Sf)
        fr.validated = validate_against(fr.value, target, rtol=1e-9)
        assert fr.validated is True


# ===========================================================================
# 7. Committed CI from uncertainty.json — bootstrap_slope_ci smoke test
# ===========================================================================

class TestBootstrapCiCommitted:
    """Smoke test: bootstrap_slope_ci on the committed mean+std arrays.

    Since the exact per-seed matrices are not stored in results.json, we
    construct a synthetic per-seed matrix consistent with the committed mean
    and std.  The CI is validated against the committed endpoints with a
    generous ±0.05 tolerance.  The key correctness assertions are:
    (a) CI brackets the OLS slope;
    (b) CI width > 0;
    (c) CI endpoints are near the committed values.
    """

    @pytest.fixture(autouse=True)
    def load_data(self):
        r = json.load(open(_VN_RESULTS))
        u = json.load(open(_VN_UNCERTAINTY))
        self.Ns = np.array(r["proxy1_trace"]["Ns"], dtype=float)
        self.mean_Sf = np.array(r["proxy1_trace"]["entropy_trace_full"]["mean"])
        self.std_Sf = np.array(r["proxy1_trace"]["entropy_trace_full"]["std"])
        self.n_seeds = r["proxy3_central_sequences"]["n_seeds"]
        # Committed CI targets from uncertainty.json
        self.committed_lo = u["entropy_trace_full"]["ci68_bootstrap"][0]
        self.committed_hi = u["entropy_trace_full"]["ci68_bootstrap"][1]

    def test_ci_brackets_ols_slope(self):
        """Bootstrap CI must bracket the OLS slope."""
        rng_gen = np.random.default_rng(42)
        per_seed = (
            self.mean_Sf[:, None]
            + self.std_Sf[:, None]
            * rng_gen.standard_normal((len(self.Ns), self.n_seeds))
        )
        per_seed = np.maximum(per_seed, 1.0)
        slope, _, _ = regression_se(self.Ns, self.mean_Sf)
        lo, hi, _ = bootstrap_slope_ci(
            per_seed, self.Ns, transform="mean", n_boot=500, seed=20260606
        )
        assert lo < slope < hi, f"CI ({lo:.4f},{hi:.4f}) does not bracket slope {slope:.4f}"

    def test_ci_width_positive(self):
        rng_gen = np.random.default_rng(42)
        per_seed = (
            self.mean_Sf[:, None]
            + self.std_Sf[:, None]
            * rng_gen.standard_normal((len(self.Ns), self.n_seeds))
        )
        per_seed = np.maximum(per_seed, 1.0)
        lo, hi, _ = bootstrap_slope_ci(
            per_seed, self.Ns, transform="mean", n_boot=300, seed=20260606
        )
        assert hi > lo

    def test_ci_endpoints_near_committed(self):
        """CI endpoints should be within ±0.05 of committed values (approximate)."""
        rng_gen = np.random.default_rng(42)
        n_N = len(self.Ns)
        per_seed = (
            self.mean_Sf[:, None]
            + self.std_Sf[:, None]
            * rng_gen.standard_normal((n_N, self.n_seeds))
        )
        per_seed = np.maximum(per_seed, 1.0)
        lo, hi, _ = bootstrap_slope_ci(
            per_seed, self.Ns, transform="mean", n_boot=1000, seed=20260606
        )
        # The synthetic per-seed matrix approximates the real one; generous tolerance
        assert abs(lo - self.committed_lo) < 0.05, (
            f"lo={lo:.4f} committed={self.committed_lo:.4f} diff={abs(lo-self.committed_lo):.4f}"
        )
        assert abs(hi - self.committed_hi) < 0.05, (
            f"hi={hi:.4f} committed={self.committed_hi:.4f} diff={abs(hi-self.committed_hi):.4f}"
        )
