"""
test_toe_spectral.py  --  Validation tests for toe/spectral.py.

Targets from ds-classification/results.json (12 published values) plus the
ARCHITECTURE.md validation contract for module A3.

All tests must complete in < 60 s total.  Numeric flows use a coarse sigma
grid (30 points instead of 90) to stay well within budget while still
reaching the UV/IR asymptotes.
"""

import numpy as np
import pytest
import sympy as sp

from toe.spectral import (
    ds_master_symbolic,
    return_probability,
    spectral_dimension,
    spectral_dimension_flow,
    d_s_uv,
    _make_gr,
    _make_stelle,
    _make_as,
    _make_cst_dalembert,
    _make_cst_randomwalk,
    _RW_SENTINEL,
)
from toe.fits import ExactResult, validate_against


# ---------------------------------------------------------------------------
# Helper: UV and IR endpoints from a flow array (matches calc.py convention:
# sigmas ordered IR -> UV, so UV is the LAST element, IR is the FIRST)
# ---------------------------------------------------------------------------
def uv_ir(flow):
    return float(flow[-1]), float(flow[0])


# Coarse sigma grid: 30 points, same range (6 -> -10 in log10) for speed
SIGMAS_COARSE = np.logspace(6, -10, 30)

FLOW_TOL = 0.06   # same tolerance as the source calc.py close()


# ===========================================================================
# 1.  Symbolic master formula  d_s^UV = D/gamma
# ===========================================================================

class TestDsMasterSymbolic:
    def test_simplifies_to_D_over_gamma(self):
        """ds_master_symbolic() must simplify to D/gamma (two positive symbols)."""
        expr = ds_master_symbolic()
        D, gamma = sp.symbols("D gamma", positive=True)
        # The expression should equal D/gamma after sympy simplification
        diff = sp.simplify(expr - D / gamma)
        assert diff == 0, f"Expected D/gamma but got {expr!r}; diff={diff}"


# ===========================================================================
# 2.  Exact classifier  d_s_uv(z, D) — sympy.Rational targets
# ===========================================================================

class TestDsUvClassifier:
    """Exact rational values from ds-classification/results.json."""

    # --- GR ---
    def test_gr_z1_D4(self):
        """GR z=1, D=4 -> d_s^UV = 4 (exact rational)."""
        res = d_s_uv(1, 4)
        assert isinstance(res, ExactResult)
        assert res.se_regression == 0.0
        assert res.value == sp.Rational(4, 1), f"Got {res.value}"

    # --- Horava anisotropic ---
    def test_horava_z2_D4_anisotropic(self):
        """Horava z=2, D=4 (D_space=3) -> d_s^UV = 5/2."""
        res = d_s_uv(2, 4, convention="anisotropic")
        assert res.value == sp.Rational(5, 2), f"Got {res.value}"
        assert res.se_regression == 0.0

    def test_horava_z3_D4_anisotropic(self):
        """Horava z=3, D=4 (D_space=3) -> d_s^UV = 2."""
        res = d_s_uv(3, 4, convention="anisotropic")
        assert res.value == sp.Rational(2, 1), f"Got {res.value}"

    def test_horava_ir_is_4(self):
        """Horava IR (z=1, isotropic) -> d_s^UV = 4."""
        res = d_s_uv(1, 4)
        assert res.value == sp.Rational(4, 1)

    # --- Stelle / AS / CST d'Alembertian / multifractional -> gamma=2 -> d_s=2 ---
    def test_stelle_z2_D4(self):
        """Stelle UV gamma=2 (z=2) -> d_s^UV = 2."""
        res = d_s_uv(2, 4)
        assert res.value == sp.Rational(2, 1), f"Got {res.value}"

    def test_as_gamma2_D4(self):
        """Asymptotic Safety UV gamma=2 -> d_s^UV = 2."""
        res = d_s_uv(2, 4)
        assert res.value == sp.Rational(2, 1)

    def test_cst_dalembert_z2_D4(self):
        """CST d'Alembertian universal UV d_s=2 -> classifier z=2, D=4."""
        res = d_s_uv(2, 4)
        assert res.value == sp.Rational(2, 1)

    def test_multifractional_z2_D4(self):
        """Multifractional UV d_s=2 -> classifier z=2, D=4."""
        res = d_s_uv(2, 4)
        assert res.value == sp.Rational(2, 1)

    # --- CST random-walk (qualitative sentinel) ---
    def test_cst_randomwalk_sentinel(self):
        """CST random-walk probe returns the '>D (increases)' sentinel."""
        res = d_s_uv(1, 4, probe="random_walk")
        assert res.value == _RW_SENTINEL, f"Got {res.value!r}"

    def test_cst_randomwalk_as_float_is_D_plus_4(self):
        """CST random-walk .as_float returns 8.0 for D=4 (illustrative D+4)."""
        res = d_s_uv(1, 4, probe="random_walk")
        assert res.as_float == 8.0, f"Got {res.as_float}"

    # --- validate_against for exact rationals ---
    def test_validate_against_exact(self):
        """validate_against with exact=True uses sympy == comparison."""
        res = d_s_uv(1, 4)
        ok = validate_against(res.value, sp.Rational(4, 1), exact=True)
        assert ok is True

    def test_validate_against_horava(self):
        res = d_s_uv(2, 4, convention="anisotropic")
        ok = validate_against(res.value, sp.Rational(5, 2), exact=True)
        assert ok is True


# ===========================================================================
# 3.  Numeric flow smoke tests (±0.06 tolerance, coarse grid, < 60 s)
# ===========================================================================

class TestSpectralDimensionFlow:
    """Numeric d_s flows match published values within FLOW_TOL = 0.06."""

    def test_gr_uv_approx_4(self):
        """GR (F=k^2): UV d_s ≈ 4.0."""
        flow = spectral_dimension_flow(_make_gr(D=4), 4, sigmas=SIGMAS_COARSE)
        uv, ir = uv_ir(flow)
        assert abs(uv - 4.0) < FLOW_TOL, f"GR UV={uv}, expected ≈4.0"
        assert abs(ir - 4.0) < FLOW_TOL, f"GR IR={ir}, expected ≈4.0"

    def test_stelle_uv_approx_2_ir_approx_4(self):
        """Stelle (F=k^2(1+k^2/m^2)): UV d_s ≈ 2.0, IR d_s ≈ 4.0."""
        flow = spectral_dimension_flow(_make_stelle(), 4, sigmas=SIGMAS_COARSE)
        uv, ir = uv_ir(flow)
        assert abs(uv - 2.0) < FLOW_TOL, f"Stelle UV={uv}, expected ≈2.0"
        assert abs(ir - 4.0) < FLOW_TOL, f"Stelle IR={ir}, expected ≈4.0"

    def test_horava_z3_uv_approx_2_ir_approx_4(self):
        """Horava z=3, D_space=3: UV d_s ≈ 2.0, IR d_s ≈ 4.0."""
        from toe.spectral import _ds_horava
        # Use a coarse grid subset for speed
        sigs = SIGMAS_COARSE
        flow = np.array([_ds_horava(s, 3, 3) for s in sigs])
        uv, ir = uv_ir(flow)
        assert abs(uv - 2.0) < FLOW_TOL, f"Horava z=3 UV={uv}, expected ≈2.0"
        assert abs(ir - 4.0) < FLOW_TOL, f"Horava z=3 IR={ir}, expected ≈4.0"

    def test_horava_z2_uv_approx_2p5_ir_approx_4(self):
        """Horava z=2, D_space=3: UV d_s ≈ 2.5, IR d_s ≈ 4.0."""
        from toe.spectral import _ds_horava
        sigs = SIGMAS_COARSE
        flow = np.array([_ds_horava(s, 3, 2) for s in sigs])
        uv, ir = uv_ir(flow)
        assert abs(uv - 2.5) < FLOW_TOL, f"Horava z=2 UV={uv}, expected ≈2.5"
        assert abs(ir - 4.0) < FLOW_TOL, f"Horava z=2 IR={ir}, expected ≈4.0"

    def test_cst_rw_uv_above_D(self):
        """CST random-walk: UV d_s > 4.1 (increases above D)."""
        flow = spectral_dimension_flow(_make_cst_randomwalk(D=4), 4, sigmas=SIGMAS_COARSE)
        uv, ir = uv_ir(flow)
        assert uv > 4.1, f"CST rw UV={uv}, expected > 4.1"


# ===========================================================================
# 4.  return_probability and spectral_dimension API
# ===========================================================================

class TestReturnProbabilityAPI:
    def test_return_probability_positive(self):
        """P(sigma) is a positive float for GR."""
        F = _make_gr(D=4)
        p = return_probability(1.0, F, 4)
        assert p > 0.0
        assert np.isfinite(p)

    def test_spectral_dimension_gr_mid_sigma(self):
        """For GR, d_s ≈ 4.0 at any sigma (no flow)."""
        F = _make_gr(D=4)
        ds = spectral_dimension(1.0, F, 4)
        assert abs(ds - 4.0) < FLOW_TOL, f"Got d_s={ds}"

    def test_spectral_dimension_stelle_uv(self):
        """For Stelle, d_s ≈ 2.0 at very small sigma (UV)."""
        F = _make_stelle()
        ds = spectral_dimension(1e-9, F, 4)
        assert abs(ds - 2.0) < FLOW_TOL, f"Got d_s={ds} at sigma=1e-9"

    def test_spectral_dimension_stelle_ir(self):
        """For Stelle, d_s ≈ 4.0 at large sigma (IR)."""
        F = _make_stelle()
        ds = spectral_dimension(1e6, F, 4)
        assert abs(ds - 4.0) < FLOW_TOL, f"Got d_s={ds} at sigma=1e6"


# ===========================================================================
# 5.  ExactResult dataclass contract (se=0, as_float)
# ===========================================================================

class TestExactResultContract:
    def test_se_is_zero(self):
        """All d_s_uv results must have se_regression == 0.0."""
        for z, D, kw in [(1, 4, {}), (2, 4, {}), (3, 4, {}),
                         (2, 4, {"convention": "anisotropic"}),
                         (3, 4, {"convention": "anisotropic"}),
                         (1, 4, {"probe": "random_walk"})]:
            res = d_s_uv(z, D, **kw)
            assert res.se_regression == 0.0, f"z={z},D={D},kw={kw}: se={res.se_regression}"

    def test_as_float_for_rational(self):
        """ExactResult.as_float works for sympy.Rational values."""
        res = d_s_uv(2, 4, convention="anisotropic")  # 5/2
        assert abs(res.as_float - 2.5) < 1e-12

    def test_validated_initially_none(self):
        """ExactResult.validated starts as None."""
        res = d_s_uv(1, 4)
        assert res.validated is None


# ===========================================================================
# 6.  Results.json 12-value master table cross-check
# ===========================================================================

class TestMasterTableValues:
    """Cross-check each of the 12 rows in results.json against the classifier."""

    # GR  UV=4, IR=4
    def test_gr_exact_uv(self):
        assert d_s_uv(1, 4).value == sp.Rational(4)

    # Horava z=2 UV=5/2, IR=4
    def test_horava_z2_uv(self):
        assert d_s_uv(2, 4, convention="anisotropic").value == sp.Rational(5, 2)

    def test_horava_z2_ir(self):
        assert d_s_uv(1, 4).value == sp.Rational(4)

    # Horava z=3 UV=2, IR=4
    def test_horava_z3_uv(self):
        assert d_s_uv(3, 4, convention="anisotropic").value == sp.Rational(2)

    def test_horava_z3_ir(self):
        assert d_s_uv(1, 4).value == sp.Rational(4)

    # Stelle UV=2, IR=4
    def test_stelle_uv(self):
        assert d_s_uv(2, 4).value == sp.Rational(2)

    # AS UV=2, IR=4
    def test_as_uv(self):
        assert d_s_uv(2, 4).value == sp.Rational(2)

    # CST d'Alembertian UV=2, IR=4
    def test_cst_dal_uv(self):
        assert d_s_uv(2, 4).value == sp.Rational(2)

    # CST random-walk UV => ">D (increases)", IR=4
    def test_cst_rw_sentinel(self):
        res = d_s_uv(1, 4, probe="random_walk")
        assert res.value == _RW_SENTINEL

    def test_cst_rw_ir_is_4(self):
        """Random-walk IR: isotropic z=1 gives d_s = D = 4."""
        assert d_s_uv(1, 4).value == sp.Rational(4)

    # Multifractional UV=2, IR=4
    def test_multifrac_uv(self):
        assert d_s_uv(2, 4).value == sp.Rational(2)

    def test_multifrac_ir(self):
        assert d_s_uv(1, 4).value == sp.Rational(4)
