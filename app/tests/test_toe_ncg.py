"""Tests for toe.ncg -- exact-rational NCG spectral-action module.

All assertions use exact sympy equality (se == 0.0, validated == True).
No stochastic elements; full test suite runs < 5 s.

Validation targets taken verbatim from ARCHITECTURE.md A4 section and
the committed calc.py scripts in core-data/calculations/.
"""

import sympy as sp
import pytest

from toe.ncg import (
    a4_heat_kernel_bracket,
    a4_ratio,
    central_charges,
    lambda_induction_ledger,
    sector_ledger,
    spectral_action_ratio,
    str_count,
)
from toe.fits import ExactResult

R = sp.Rational


# ---------------------------------------------------------------------------
# a4_heat_kernel_bracket
# ---------------------------------------------------------------------------

class TestA4HeatKernelBracket:
    """Exact bracket coefficients from Vassilevich hep-th/0306138 Table 1."""

    def test_scalar_C2(self):
        br = a4_heat_kernel_bracket("scalar")
        assert br["C2"] == R(1, 120), f"scalar C2: got {br['C2']}"

    def test_scalar_E4(self):
        br = a4_heat_kernel_bracket("scalar")
        assert br["E4"] == R(-1, 360), f"scalar E4: got {br['E4']}"

    def test_scalar_R2_zero(self):
        # Real scalar with conformal coupling is conformally invariant -> R2 = 0.
        br = a4_heat_kernel_bracket("scalar")
        assert br["R2"] == R(0), f"scalar R2: got {br['R2']}"

    def test_dirac_C2(self):
        # 4-component Dirac = 2 Weyl; C2 coeff = -2 * (1/40) from Weyl pairs.
        br = a4_heat_kernel_bracket("dirac")
        assert br["C2"] == R(-1, 20), f"dirac C2: got {br['C2']}"

    def test_dirac_E4(self):
        # Dirac E4 = 2 * (11/720) = 11/360.
        br = a4_heat_kernel_bracket("dirac")
        assert br["E4"] == R(11, 360), f"dirac E4: got {br['E4']}"

    def test_dirac_R2_zero(self):
        # Dirac is also conformally invariant -> R2 = 0.
        br = a4_heat_kernel_bracket("dirac")
        assert br["R2"] == R(0), f"dirac R2: got {br['R2']}"

    def test_dirac_magnitudes_equal_weyl_ac(self):
        # |C2_dirac| = 2 * c_weyl = 2/40 = 1/20; |E4_dirac| = 2 * a_weyl = 11/360.
        br = a4_heat_kernel_bracket("dirac")
        c_weyl = R(1, 40)
        a_weyl = R(11, 720)
        assert sp.Abs(br["C2"]) == 2 * c_weyl
        assert sp.Abs(br["E4"]) == 2 * a_weyl

    def test_vector_C2(self):
        br = a4_heat_kernel_bracket("vector")
        assert br["C2"] == R(1, 10), f"vector C2: got {br['C2']}"

    def test_vector_E4(self):
        br = a4_heat_kernel_bracket("vector")
        assert br["E4"] == R(-31, 180), f"vector E4: got {br['E4']}"

    def test_unknown_field_raises(self):
        with pytest.raises(ValueError):
            a4_heat_kernel_bracket("graviton")

    def test_case_insensitive(self):
        br_lower = a4_heat_kernel_bracket("scalar")
        br_upper = a4_heat_kernel_bracket("Scalar")
        assert br_lower == br_upper


# ---------------------------------------------------------------------------
# central_charges
# ---------------------------------------------------------------------------

class TestCentralCharges:
    """Exact (a, c) from Duff arXiv:2003.02688 Table 1."""

    def test_one_weyl_fermion(self):
        # central_charges(0, 1, 0) -> (11/720, 1/40)
        a, c = central_charges(0, 1, 0)
        assert a == R(11, 720), f"a: got {a}"
        assert c == R(1, 40), f"c: got {c}"

    def test_one_weyl_fermion_architecture_target(self):
        # ARCHITECTURE.md: central_charges(0, 1, 0) == (11/720, 1/40)
        a, c = central_charges(0, 1, 0)
        assert (a, c) == (R(11, 720), R(1, 40))

    def test_one_weyl_graviton_architecture_target(self):
        # ARCHITECTURE.md: central_charges(0, 1, 0) == (Rational(11,720), Rational(1,40))
        a, c = central_charges(0, 1, 0)
        assert a == R(11, 720)
        assert c == R(1, 40)

    def test_full_SM_with_nuR(self):
        # SM: N0=4 Higgs, 48 Weyl (with nu_R), N1=12 vectors.
        # ARCHITECTURE.md: central_charges(4, 48, 12) -> (253/90, 73/30)
        a, c = central_charges(4, 48, 12)
        assert a == R(253, 90), f"a (full SM + nuR): got {a}"
        assert c == R(73, 30), f"c (full SM + nuR): got {c}"

    def test_real_scalar_per_field(self):
        a, c = central_charges(1, 0, 0)
        assert a == R(1, 360)
        assert c == R(1, 120)

    def test_vector_per_field(self):
        a, c = central_charges(0, 0, 1)
        assert a == R(31, 180)
        assert c == R(1, 10)

    def test_additivity(self):
        # (a, c) of two scalars == 2 * one scalar
        a1, c1 = central_charges(1, 0, 0)
        a2, c2 = central_charges(2, 0, 0)
        assert a2 == 2 * a1
        assert c2 == 2 * c1

    def test_720a_counting_formula_scalar(self):
        # 720 a = 2 N0 -> a = 2/720 = 1/360
        a, _ = central_charges(1, 0, 0)
        assert 720 * a == 2

    def test_720c_counting_formula_scalar(self):
        # 720 c = 6 N0 -> c = 6/720 = 1/120
        _, c = central_charges(1, 0, 0)
        assert 720 * c == 6

    def test_720a_counting_formula_weyl(self):
        # 720 a = 11 N_{1/2}
        a, _ = central_charges(0, 1, 0)
        assert 720 * a == 11

    def test_720c_counting_formula_weyl(self):
        # 720 c = 18 N_{1/2}
        _, c = central_charges(0, 1, 0)
        assert 720 * c == 18


# ---------------------------------------------------------------------------
# a4_ratio -- the index-protected -18/11
# ---------------------------------------------------------------------------

class TestA4Ratio:
    """The index-protected -18/11 identity."""

    def test_fermion_sector_n1(self):
        result = a4_ratio(n_fermions=1, sector="fermion")
        assert isinstance(result, ExactResult)
        assert result.value == R(-18, 11)
        assert result.se_regression == 0.0

    def test_fermion_sector_n45(self):
        # Content-independence: same ratio for SM fermion count (no nu_R).
        result = a4_ratio(n_fermions=45, sector="fermion")
        assert result.value == R(-18, 11)

    def test_fermion_sector_n48(self):
        # Content-independence: same ratio with nu_R.
        result = a4_ratio(n_fermions=48, with_nu_R=True, sector="fermion")
        assert result.value == R(-18, 11)

    def test_fermion_sector_with_nu_R_false(self):
        result = a4_ratio(n_fermions=45, with_nu_R=False, sector="fermion")
        assert result.value == R(-18, 11)

    def test_fermion_sector_with_nu_R_true(self):
        result = a4_ratio(n_fermions=48, with_nu_R=True, sector="fermion")
        assert result.value == R(-18, 11)

    def test_fermion_sector_validated(self):
        result = a4_ratio(sector="fermion")
        assert result.validated is True

    def test_full_SM_no_nuR(self):
        # ARCHITECTURE.md: a4_ratio(sector="full_SM", with_nu_R=False).value == -1698/1991
        result = a4_ratio(sector="full_SM", with_nu_R=False)
        assert result.value == R(-1698, 1991), f"full SM no nuR: got {result.value}"

    def test_full_SM_with_nuR(self):
        # ARCHITECTURE.md: a4_ratio(sector="full_SM", with_nu_R=True).value == -219/253
        result = a4_ratio(sector="full_SM", with_nu_R=True)
        assert result.value == R(-219, 253), f"full SM with nuR: got {result.value}"

    def test_full_SM_se_zero(self):
        result = a4_ratio(sector="full_SM")
        assert result.se_regression == 0.0

    def test_exact_result_type(self):
        result = a4_ratio()
        assert isinstance(result, ExactResult)

    def test_as_float(self):
        result = a4_ratio()
        assert abs(result.as_float - (-18 / 11)) < 1e-14

    def test_unknown_sector_raises(self):
        with pytest.raises(ValueError):
            a4_ratio(sector="graviton")


# ---------------------------------------------------------------------------
# spectral_action_ratio
# ---------------------------------------------------------------------------

class TestSpectralActionRatio:
    """alpha0 / tau0 = -18/11 (f0 cancels)."""

    def test_value(self):
        result = spectral_action_ratio()
        assert result.value == R(-18, 11)

    def test_type(self):
        result = spectral_action_ratio()
        assert isinstance(result, ExactResult)

    def test_se_zero(self):
        result = spectral_action_ratio()
        assert result.se_regression == 0.0

    def test_validated(self):
        result = spectral_action_ratio()
        assert result.validated is True

    def test_matches_fermion_ratio(self):
        # spectral_action_ratio must equal a4_ratio for fermion sector.
        sr = spectral_action_ratio()
        fr = a4_ratio(sector="fermion")
        assert sr.value == fr.value

    def test_float(self):
        result = spectral_action_ratio()
        assert abs(result.as_float - (-18 / 11)) < 1e-14


# ---------------------------------------------------------------------------
# sector_ledger
# ---------------------------------------------------------------------------

class TestSectorLedger:
    """SM (a, c) ledger per sector."""

    def test_fermion_ratio_is_minus_18_11_no_nuR(self):
        ledger = sector_ledger(with_nu_R=False)
        assert ledger["ratio_fermions_only"] == R(-18, 11)

    def test_fermion_ratio_is_minus_18_11_with_nuR(self):
        ledger = sector_ledger(with_nu_R=True)
        assert ledger["ratio_fermions_only"] == R(-18, 11)

    def test_full_SM_ratio_no_nuR(self):
        ledger = sector_ledger(with_nu_R=False)
        assert ledger["ratio_full_SM"] == R(-1698, 1991)

    def test_full_SM_ratio_with_nuR(self):
        ledger = sector_ledger(with_nu_R=True)
        assert ledger["ratio_full_SM"] == R(-219, 253)

    def test_N_Weyl_no_nuR(self):
        ledger = sector_ledger(with_nu_R=False)
        assert ledger["N_Weyl"] == 45

    def test_N_Weyl_with_nuR(self):
        ledger = sector_ledger(with_nu_R=True)
        assert ledger["N_Weyl"] == 48

    def test_fermion_only_ac_no_nuR(self):
        # 45 Weyl: a = 45 * 11/720 = 495/720 = 11/16, c = 45 * 1/40 = 45/40 = 9/8
        ledger = sector_ledger(with_nu_R=False)
        assert ledger["fermions_only"]["a"] == R(11, 16)
        assert ledger["fermions_only"]["c"] == R(9, 8)

    def test_keys_present(self):
        ledger = sector_ledger()
        for key in ("fermions_only", "full_SM", "ratio_fermions_only",
                    "ratio_full_SM", "N_Weyl"):
            assert key in ledger, f"missing key: {key}"


# ---------------------------------------------------------------------------
# str_count
# ---------------------------------------------------------------------------

class TestStrCount:
    """STr(1) = n_B - n_F for the NCG SM content."""

    def test_SM_no_nuR(self):
        # n_F = 2*45 = 90, n_B = 2*12 + 4 = 28 -> STr1 = 28 - 90 = -62.
        content = {"n_weyl": 45, "n_scalar": 4, "n_vector": 12}
        result = str_count(content)
        assert result == R(-62), f"STr(1) no nuR: got {result}"

    def test_SM_with_nuR(self):
        # n_F = 2*48 = 96, n_B = 28 -> STr1 = 28 - 96 = -68.
        content = {"n_weyl": 48, "n_scalar": 4, "n_vector": 12}
        result = str_count(content)
        assert result == R(-68), f"STr(1) with nuR: got {result}"

    def test_zero_content(self):
        result = str_count({})
        assert result == R(0)

    def test_pure_fermions(self):
        # Only 5 Weyl: n_F = 10, n_B = 0 -> -10.
        result = str_count({"n_weyl": 5})
        assert result == R(-10)

    def test_pure_scalars(self):
        result = str_count({"n_scalar": 3})
        assert result == R(3)

    def test_pure_vectors(self):
        result = str_count({"n_vector": 3})
        assert result == R(6)  # 3 * 2 polarizations

    def test_return_type_rational(self):
        result = str_count({"n_weyl": 45, "n_scalar": 4, "n_vector": 12})
        assert isinstance(result, sp.Basic)


# ---------------------------------------------------------------------------
# lambda_induction_ledger
# ---------------------------------------------------------------------------

class TestLambdaInductionLedger:
    """ARCHITECTURE.md exact targets for the Lambda-induction ledger."""

    def setup_method(self):
        self.ledger = lambda_induction_ledger()

    def test_ratio_a0_over_a2_per_mode(self):
        # ARCHITECTURE.md: ["ratio_a0_over_a2_per_mode"] == 12
        assert self.ledger["ratio_a0_over_a2_per_mode"] == 12, (
            f"ratio_a0_over_a2_per_mode: got {self.ledger['ratio_a0_over_a2_per_mode']}"
        )

    def test_ratio_a4_c_over_minus_a(self):
        # ARCHITECTURE.md: ["ratio_a4_c_over_minus_a"] == Rational(-18, 11)
        assert self.ledger["ratio_a4_c_over_minus_a"] == R(-18, 11), (
            f"ratio_a4_c_over_minus_a: got {self.ledger['ratio_a4_c_over_minus_a']}"
        )

    def test_str1_45_noNuR(self):
        assert self.ledger["STr1_45_noNuR"] == -62

    def test_str1_48_withNuR(self):
        assert self.ledger["STr1_48_withNuR"] == -68

    def test_quartic_does_not_cancel_45(self):
        assert self.ledger["quartic_cancels_45"] is False

    def test_quartic_does_not_cancel_48(self):
        assert self.ledger["quartic_cancels_48"] is False

    def test_Lambda_cc_N_independent(self):
        assert self.ledger["Lambda_cc_is_N_independent"] is True

    def test_DEGENERATE_verdict_present(self):
        assert "N_independence_is_DEGENERATE" in self.ledger
        # The verdict string must explain the degenerate N-cancellation.
        msg = self.ledger["N_independence_is_DEGENERATE"]
        assert isinstance(msg, str) and len(msg) > 20
        # Check for key concepts: the key word DEGENERATE may be in the key
        # name itself; the string must mention index protection and cutoff.
        assert "index protection" in msg.lower() or "index-protected" in msg.lower()
        assert "cutoff" in msg.lower()

    def test_a0_dirac_per_mode_value(self):
        # a0 = 1/(4 pi^2) for one Dirac mode
        a0 = self.ledger["a0_dirac_per_mode"]
        expected = R(1, 4) / sp.pi**2
        assert sp.simplify(a0 - expected) == 0

    def test_a2_dirac_coeff_of_R_value(self):
        # a2 coeff of R = -1/(48 pi^2)
        a2 = self.ledger["a2_dirac_coeff_of_R"]
        expected = -R(1, 48) / sp.pi**2
        assert sp.simplify(a2 - expected) == 0


# ---------------------------------------------------------------------------
# ExactResult dataclass integration
# ---------------------------------------------------------------------------

class TestExactResultIntegration:
    """Cross-module: ncg functions return ExactResult with se == 0."""

    def test_spectral_action_ratio_se_zero(self):
        r = spectral_action_ratio()
        assert r.se_regression == 0.0

    def test_a4_ratio_fermion_se_zero(self):
        r = a4_ratio(sector="fermion")
        assert r.se_regression == 0.0

    def test_a4_ratio_full_sm_se_zero(self):
        r = a4_ratio(sector="full_SM")
        assert r.se_regression == 0.0

    def test_as_float_property(self):
        r = spectral_action_ratio()
        f = r.as_float
        assert isinstance(f, float)
        assert abs(f - (-18 / 11)) < 1e-12
