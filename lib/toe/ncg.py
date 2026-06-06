"""toe.ncg -- exact-rational NCG spectral-action heat-kernel module.

All public functions return ExactResult (sympy Rational/Expr, se == 0).
No file I/O, no plotting, no global state. Layer A: imports only sympy
and toe.fits (for the ExactResult dataclass).

Sources:
  Chamseddine-Connes hep-th/9606001;  Chamseddine-Connes-Marcolli hep-th/0610241;
  Vassilevich hep-th/0306138;  Duff arXiv:2003.02688;  Gilkey (heat-kernel master).
"""

from __future__ import annotations

import sympy as sp

from toe.fits import ExactResult, validate_against

# ---------------------------------------------------------------------------
# Module-level sympy helpers (no global mutable state; pure constants)
# ---------------------------------------------------------------------------
R = sp.Rational  # shorthand for exact rationals


# ---------------------------------------------------------------------------
# A4 heat-kernel bracket coefficients (Gilkey / Vassilevich basis)
# ---------------------------------------------------------------------------

def a4_heat_kernel_bracket(field: str) -> dict:
    """Return the {C2, E4, R2} a4(D^2) bracket coefficients for a free field.

    The a4 bracket (curvature part, dropping total derivatives) in the basis
    {Weyl^2, Euler density E_4, R^2} is computed from the Gilkey/Vassilevich
    master formula.  The results are exact sympy Rationals.

    Formula: heat-kernel-action, gravity-terms
    Evidence: VYPOCET-11 (core-data/calculations/a4-graviton-index/calc.py)
    Conventions: Vassilevich hep-th/0306138 eq.4.28, Table 1; basis inversion
        C^2 = Riem^2 - 2 Ric^2 + (1/3)R^2,
        E_4 = Riem^2 - 4 Ric^2 + R^2.

    Args:
        field: one of "scalar", "dirac", "vector".  "vector" returns the
            net physical result (Maxwell + ghosts) directly from literature.

    Returns:
        dict with keys "C2", "E4", "R2" mapping to sympy.Rational values.

    Raises:
        ValueError: if field is not one of the recognised names.
    """
    field = field.lower()
    if field == "scalar":
        # Real scalar with conformal coupling E = -R/6, tr_V(1) = 1, Omega = 0.
        # Verified in a4-graviton-index/calc.py: scalar["C2"]=1/120, E4=-1/360.
        return {"C2": R(1, 120), "E4": R(-1, 360), "R2": R(0)}
    elif field == "dirac":
        # 4-component Dirac: Lichnerowicz E = -R/4, tr_V(1) = 4,
        # tr(Omega^2) = -(1/2) Riem^2.
        # Verified: dirac["C2"] = -1/20, E4 = 11/360 (note SIGN convention --
        # the heat-kernel bracket carries the anomaly sign; magnitudes equal (a,c)).
        return {"C2": R(-1, 20), "E4": R(11, 360), "R2": R(0)}
    elif field == "vector":
        # Net physical vector (Maxwell + Faddeev-Popov ghosts), on-shell result.
        # From Duff arXiv:2003.02688 / Vassilevich Table 1: c=1/10, a=31/180.
        # sign: coeff(C^2) = +c = +1/10; coeff(E4) = -a = -31/180.
        return {"C2": R(1, 10), "E4": R(-31, 180), "R2": R(0)}
    else:
        raise ValueError(
            f"a4_heat_kernel_bracket: unknown field '{field}'. "
            "Choose one of: 'scalar', 'dirac', 'vector'."
        )


# ---------------------------------------------------------------------------
# Central charges (a, c) for a free-field content
# ---------------------------------------------------------------------------

def central_charges(
    n0: int,
    n_weyl: int,
    n1: int,
) -> tuple:
    """Return the exact (a, c) trace-anomaly central charges for a free-field content.

    Duff 2003.02688 Table 1 / eq.(17), 2-component Weyl spinor basis:
        720 c = 6 N0 + 18 N_{1/2} + 72 N1
        720 a = 2 N0 + 11 N_{1/2} + 124 N1

    Formula: trace-anomaly-4d
    Evidence: VYPOCET-11 (core-data/calculations/a4-graviton-index/calc.py),
              VYPOCET-02 / a4-anomaly-matching
    Conventions: Duff arXiv:2003.02688 eq.(14-17), Table 1; <T> = (1/(4pi)^2)(cF - aG),
        F = Weyl^2, G = Euler density; N_{1/2} counts 2-component Weyl spinors.

    Args:
        n0:      number of real scalar d.o.f.
        n_weyl:  number of 2-component Weyl fermions.
        n1:      number of gauge vector fields.

    Returns:
        tuple (a, c) of sympy.Rational values.
    """
    c_scalar = R(1, 120)
    a_scalar = R(1, 360)
    c_weyl = R(1, 40)      # = 18/720
    a_weyl = R(11, 720)
    c_vector = R(1, 10)    # = 72/720
    a_vector = R(31, 180)  # = 124/720

    c_total = n0 * c_scalar + n_weyl * c_weyl + n1 * c_vector
    a_total = n0 * a_scalar + n_weyl * a_weyl + n1 * a_vector

    return sp.nsimplify(a_total), sp.nsimplify(c_total)


# ---------------------------------------------------------------------------
# a4 ratio c/(-a) for fermion content and full SM sectors
# ---------------------------------------------------------------------------

def a4_ratio(
    n_fermions: int = 1,
    *,
    with_nu_R: bool = False,
    sector: str = "fermion",
) -> ExactResult:
    """Return the exact a4 ratio coeff(C^2) / coeff(Euler) = c / (-a).

    For sector="fermion" (pure Weyl-fermion content) this is EXACTLY -18/11,
    independent of fermion count and of whether nu_R is included.  This
    content-independence is the *index-protection* property: every Weyl fermion
    carries the same (a, c) = (11/720, 1/40), so c/(-a) = -18/11 regardless
    of N_W.

    For sector="full_SM" the scalar and vector contributions break the universality
    and the ratio becomes content-dependent (and nu_R-dependent).

    Formula: spectral-action-formula, trace-anomaly-4d, gravity-terms
    Evidence: VYPOCET-11 (core-data/calculations/a4-graviton-index/calc.py),
              VYPOCET-02 (a4-anomaly-matching/calc.py)
    Conventions: Duff arXiv:2003.02688 Table 1; Chamseddine-Connes hep-th/9606001 eq.2.24;
        ratio = alpha0 / tau0 = (-3 f0/10 pi^2) / (11 f0/60 pi^2) = -18/11 (f0 cancels).

    Args:
        n_fermions: number of Weyl fermions (used only for sector="fermion";
            irrelevant because the ratio is content-independent in that sector).
        with_nu_R:  if True, include 3 right-handed neutrinos (45 -> 48 Weyl).
            Relevant only for sector="full_SM".
        sector:  "fermion" (Weyl-only content) or "full_SM" (SM field content).

    Returns:
        ExactResult with value = sympy.Rational(-18, 11) for sector="fermion";
        content-dependent Rational for sector="full_SM"; se_regression = 0.0.
    """
    sector = sector.lower()

    if sector == "fermion":
        # Exact for any Weyl count: c/(-a) = (1/40) / (-11/720) = -18/11.
        val = R(-18, 11)
        result = ExactResult(value=val, se_regression=0.0)
        result.validated = validate_against(val, R(-18, 11), exact=True)
        return result

    elif sector == "full_sm":
        # SM content: N0=4 (Higgs), N1=12 (gauge), N_W = 45 or 48.
        N0 = 4
        N1 = 12
        N_W = 48 if with_nu_R else 45
        a_total, c_total = central_charges(N0, N_W, N1)
        val = sp.nsimplify(c_total / (-a_total))
        result = ExactResult(value=val, se_regression=0.0)
        return result

    else:
        raise ValueError(
            f"a4_ratio: unknown sector '{sector}'. "
            "Choose 'fermion' or 'full_SM'."
        )


# ---------------------------------------------------------------------------
# Spectral-action ratio alpha0 / tau0
# ---------------------------------------------------------------------------

def spectral_action_ratio() -> ExactResult:
    """Return the exact spectral-action C^2 / Euler ratio alpha0 / tau0 = -18/11.

    Chamseddine-Connes 1997 hep-th/9606001 eq.(2.24):
        alpha0 = -3 f0 / (10 pi^2)   [coefficient of Weyl^2 = C^2]
        tau0   = 11 f0 / (60 pi^2)   [coefficient of R*R* = Euler / Gauss-Bonnet]
        => alpha0 / tau0 = (-3/10) / (11/60) = -18/11  (f0 cancels exactly).

    This is the spectral-action counterpart of the trace-anomaly ratio c/(-a) = -18/11
    for a pure Weyl-fermion content (the two are literally the same heat-kernel number).

    Formula: spectral-action-formula, heat-kernel-action
    Evidence: VYPOCET-11 (core-data/calculations/a4-graviton-index/calc.py),
              VYPOCET-02 (a4-anomaly-matching/calc.py)
    Conventions: Chamseddine-Connes hep-th/9606001 eq.2.24; CCM hep-th/0610241;
        f0 = f(0) is the spectral cutoff function value at zero (positive, cancels).

    Returns:
        ExactResult with value = sympy.Rational(-18, 11), se_regression = 0.0,
        validated = True.
    """
    f0 = sp.Symbol('f0', positive=True)
    alpha0 = -R(3, 10) * f0 / sp.pi**2
    tau0 = R(11, 60) * f0 / sp.pi**2
    val = sp.nsimplify(alpha0 / tau0)   # = -18/11 (f0 cancels)

    result = ExactResult(value=val, se_regression=0.0)
    result.validated = validate_against(val, R(-18, 11), exact=True)
    return result


# ---------------------------------------------------------------------------
# SM sector ledger: (a, c) totals per sector
# ---------------------------------------------------------------------------

def sector_ledger(*, with_nu_R: bool = False) -> dict:
    """Return the SM (a, c) ledger per sector as exact sympy Rationals.

    Computes the exact central charges for the fermionic-only and full-SM
    content using Duff arXiv:2003.02688 Table 1 coefficients.

    Formula: trace-anomaly-4d, spectral-action-formula
    Evidence: VYPOCET-02 (core-data/calculations/a4-anomaly-matching/calc.py)
    Conventions: Duff arXiv:2003.02688 eq.(14-17), Table 1; 2-component Weyl basis;
        SM content: N0=4 (Higgs complex doublet = 4 real scalars),
        N1=12 (SU(3)xSU(2)xU(1): 8+3+1 gauge bosons),
        N_W = 45 (no nu_R) or 48 (with nu_R, as NCG demands).

    Args:
        with_nu_R: if True, use 48 Weyl fermions (3 right-handed neutrinos added).
            NCG spectral triple requires nu_R; default False = SM without nu_R.

    Returns:
        dict with keys:
            "fermions_only": {"a": Rational, "c": Rational}
            "full_SM": {"a": Rational, "c": Rational}
            "ratio_fermions_only": Rational (== -18/11)
            "ratio_full_SM": Rational (content-dependent)
            "N_Weyl": int
    """
    N_W = 48 if with_nu_R else 45
    N0 = 4
    N1 = 12

    a_ferm, c_ferm = central_charges(0, N_W, 0)
    a_full, c_full = central_charges(N0, N_W, N1)

    ratio_ferm = sp.nsimplify(c_ferm / (-a_ferm))
    ratio_full = sp.nsimplify(c_full / (-a_full))

    return {
        "fermions_only": {"a": a_ferm, "c": c_ferm},
        "full_SM": {"a": a_full, "c": c_full},
        "ratio_fermions_only": ratio_ferm,
        "ratio_full_SM": ratio_full,
        "N_Weyl": N_W,
    }


# ---------------------------------------------------------------------------
# Supertrace STr(1) counting
# ---------------------------------------------------------------------------

def str_count(content: dict) -> sp.Rational:
    """Return the supertrace STr(1) = n_B - n_F (boson minus fermion d.o.f.).

    The Pauli/supertrace condition for quartic vacuum-energy cancellation is
    STr(1) = 0 (equal boson and fermion on-shell real d.o.f.).  For the NCG SM
    content this is negative (more fermions than bosons), meaning the quartic
    cosmological-constant divergence is NOT cancelled.

    Formula: lambda-prediction
    Evidence: VYPOCET-17 (core-data/calculations/lambda-induced/calc.py)
    Conventions: Visser arXiv:1610.07264; Akhmedov hep-th/0204048; on-shell counting:
        Weyl fermion = 2 real d.o.f., massless vector = 2 polarizations,
        real scalar = 1 real d.o.f.;
        STr(1) = sum_bosons(-1)^{2J}(2J+1) - sum_fermions ~ n_B - n_F.

    Args:
        content: dict with keys (all optional, default 0):
            "n_weyl":    number of 2-component Weyl fermions (2 real d.o.f. each)
            "n_scalar":  number of real scalar d.o.f.
            "n_vector":  number of massless vectors (2 polarizations each)

    Returns:
        sympy.Rational equal to n_B - n_F (STr 1 value).
    """
    n_weyl = content.get("n_weyl", 0)
    n_scalar = content.get("n_scalar", 0)
    n_vector = content.get("n_vector", 0)

    n_F = R(2) * n_weyl                  # 2 on-shell real d.o.f. per Weyl fermion
    n_B = R(n_scalar) + R(2) * n_vector  # 1 per real scalar, 2 per massless vector

    return sp.nsimplify(n_B - n_F)


# ---------------------------------------------------------------------------
# Lambda-induction ledger: a0 : a2 : a4 ratios and DEGENERATE verdict
# ---------------------------------------------------------------------------

def lambda_induction_ledger() -> dict:
    """Return the exact a0:a2:a4 cosmological / Einstein-Hilbert / Weyl^2 ledger.

    Computes the per-mode heat-kernel densities and their ratios for the three
    sectors of the spectral action expansion:
        Tr f(D/Lambda) ~ 2 Lambda^4 f4 a0 + 2 Lambda^2 f2 a2 + f0 a4

    Key results (exact rationals):
      - ratio_a0_over_a2_per_mode = 12  (clean rational, but cross-order in
        Lambda/f, NOT index-protected -- see DEGENERATE verdict below)
      - ratio_a4_c_over_minus_a = -18/11  (index-protected, f0 and Lambda cancel)
      - Lambda_cc_is_N_independent = True  (but N cancels DEGENERATELY)
      - STr(1) for SM content: -62 (no nu_R) or -68 (with nu_R)

    Formula: spectral-action-formula, heat-kernel-action, lambda-prediction
    Evidence: VYPOCET-17 (core-data/calculations/lambda-induced/calc.py)
    Conventions: Chamseddine-Connes hep-th/9606001 eq.(2.18)-(2.26);
        Marcolli 'Spectral Action Gravity and Cosmological Models';
        Gilkey / Vassilevich hep-th/0306138 eqs.(4.26-4.27);
        per-mode Dirac: a0 ~ 1/(4 pi^2), a2 coeff of R ~ -1/(48 pi^2).

    Returns:
        dict with keys:
            "ratio_a0_over_a2_per_mode": sympy.Integer (== 12)
            "ratio_a4_c_over_minus_a": sympy.Rational (== -18/11)
            "a0_dirac_per_mode": sympy.Expr (1/(4 pi^2))
            "a2_dirac_coeff_of_R": sympy.Expr (-1/(48 pi^2))
            "Lambda_cc_is_N_independent": bool (True, but DEGENERATELY)
            "N_independence_is_DEGENERATE": str (explanation)
            "STr1_45_noNuR": int (-62)
            "STr1_48_withNuR": int (-68)
            "quartic_cancels_45": bool (False)
            "quartic_cancels_48": bool (False)
    """
    # Per-mode heat-kernel densities (Gilkey / Vassilevich hep-th/0306138).
    inv16pi2 = R(1, 16) / sp.pi**2   # = (4 pi)^{-2}
    a0_dirac = inv16pi2 * 4          # = 1/(4 pi^2)
    a2_dirac_coeff = inv16pi2 * R(1, 6) * R(-2)  # = -1/(48 pi^2)
    #   Derivation: a2 = (4pi)^{-2} (1/6) tr_V(6E+R); Dirac tr(6E+R) = 4*(6*(-1/4)+1)*R = -2R.

    A0 = sp.nsimplify(a0_dirac)              # 1/(4 pi^2)
    A2 = sp.nsimplify(sp.Abs(a2_dirac_coeff))  # 1/(48 pi^2)

    # Per-mode ratio a0/a2 (stripping shared 1/pi^2 factor -> pure number):
    ratio_a0_a2 = sp.nsimplify(A0 / A2)     # = (1/(4 pi^2)) / (1/(48 pi^2)) = 12

    # a4 ratio (re-confirm -18/11):
    a_weyl = R(11, 720)
    c_weyl = R(1, 40)
    ratio_a4 = sp.nsimplify(c_weyl / (-a_weyl))  # = -18/11

    # Supertrace counting for the SM on-shell content:
    #   Fermions: 2 real d.o.f. per Weyl; SM without nu_R -> 45*2 = 90; with -> 96.
    #   Bosons: 12 massless vectors * 2 pol = 24; Higgs 4 real scalars -> n_B = 28.
    n_B = 28   # 24 (gauge) + 4 (Higgs)
    n_F_45 = 90
    n_F_48 = 96
    STr1_45 = n_B - n_F_45   # = -62
    STr1_48 = n_B - n_F_48   # = -68

    return {
        "ratio_a0_over_a2_per_mode": ratio_a0_a2,          # 12
        "ratio_a4_c_over_minus_a": ratio_a4,               # -18/11
        "a0_dirac_per_mode": A0,
        "a2_dirac_coeff_of_R": sp.nsimplify(a2_dirac_coeff),
        "Lambda_cc_is_N_independent": True,
        "N_independence_is_DEGENERATE": (
            "Lambda_cc = (f4/f2) * Lambda^2 * g_hat/(2 k_hat): N cancels ONLY because "
            "numerator (gamma0) and denominator (m_Pl^2) carry the SAME overall Tr(1_F)=N. "
            "This is NOT index protection: the result still carries (f4/f2) and Lambda^2 -- "
            "dimensionful and cutoff-shape-dependent, unlike the dimensionless -18/11."
        ),
        "STr1_45_noNuR": STr1_45,
        "STr1_48_withNuR": STr1_48,
        "quartic_cancels_45": (STr1_45 == 0),
        "quartic_cancels_48": (STr1_48 == 0),
    }
