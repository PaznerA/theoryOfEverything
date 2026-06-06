#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""
VYPOCET-17  --  LAMBDA-INDUKCE : what fermion-induced gravity predicts for the
                cosmological constant (H4g-3), with EXACT sympy arithmetic.
==============================================================================
Established context (do NOT re-derive, only build on):
  * F-014 / VYPOCET-02 / VYPOCET-11 : the Chamseddine-Connes spectral action
    a4 (Weyl^2 vs Euler) ratio is alpha0/tau0 = -18/11, EXACTLY equal to the
    single-Weyl-fermion conformal-anomaly ratio c/(-a). It is INDEX-PROTECTED
    (sits inside the spinor a4 whose Pontryagin sector is the A-hat index
    density) and CONTENT-INDEPENDENT (every Weyl fermion carries the same (a,c)),
    so 45 vs 48 Weyl gives the same -18/11.  Spectral action = Sakharov
    fermion-induced gravity.

THE QUESTION (H4g-3):  the SAME logic applied to the cosmological constant.
  The spectral action expands (Chamseddine-Connes-Marcolli, "Spectral Action
  Gravity and Cosmological Models", eq. quoted verbatim below):

     Tr f(D/Lambda) ~ 2 Lambda^4 f4 a0 + 2 Lambda^2 f2 a2 + f0 a4

  a0 -> cosmological term, a2 -> Einstein-Hilbert, a4 -> Weyl^2 + Gauss-Bonnet.
  a0 = (1/(16 pi^2)) Tr(1) * Vol  is a PURE COUNTING of fermionic d.o.f. (N),
  a2 = -(1/(48 pi^2)) Tr(1) * Int R  (also pure counting up to the Yukawa-mass
  dressing in the SM), a4 carries the conformal -18/11.

We answer the four sub-questions with exact rationals:
  (1) a0 (Lambda) term: exact rational dependence on field content (N = 45 vs 48).
  (2) a2 (Einstein-Hilbert) term: exact rational, G_induced ~ 1/(f2 Lambda^2 N).
  (3) Is there a SECOND content-independent ratio among {a0,a2,a4}, analogous to
      -18/11?  Compute a0:a2:a4 for Weyl/Dirac exactly; test every pairwise ratio
      and the dimensionless combinations (Lambda_c G_N, Lambda_c/m_Pl^2) for
      content-(N)-independence.
  (4) Confront the CC problem honestly: induced Lambda is cutoff-QUARTIC
      (f4 Lambda^4).  Does fermion induction make it WORSE / SAME?  Does nu_R
      (45->48) flip the sign or trigger any Pauli-type (sum_B - sum_F)
      supertrace cancellation for the NCG content?

CONVENTIONS (verified against the literature during this run):

  Spectral action master expansion + SM coefficients
  [Chamseddine-Connes hep-th/9606001 eq.(2.18)-(2.26);
   Chamseddine-Connes-Marcolli (CoMa) "Gravity and the SM"; Marcolli
   "Spectral Action Gravity and Cosmological Models" (NCGCosmoCRP), eqs. quoted]:

     Tr f(D/Lambda) ~ 2 Lambda^4 f4 a0 + 2 Lambda^2 f2 a2 + f0 a4              (M)

     1/(2 kappa0^2)  = (96 f2 Lambda^2 - f0 c) / (24 pi^2)      [E-H coeff]    (EH)
     gamma0          = (1/(4 pi^2)) (48 f4 Lambda^4 - f2 Lambda^2 c + d)  [Lambda] (CC)
     alpha0          = -3 f0/(10 pi^2)    [C^2]                                (A0)
     tau0            =  11 f0/(60 pi^2)   [R*R*]                               (T0)
       => alpha0/tau0 = -18/11           (this is VYPOCET-02's identity)

   The cutoff MOMENTS:  f4 = Int_0^inf x f(x) dx,  f2 = Int_0^inf f(x) dx (up to
   normalization), f0 = f(0).  The functions a,b,c,d,e are Yukawa/Majorana
   traces: c = Tr(M M^dagger), d = Tr((M M^dagger)^2) (Majorana masses),
   a = Tr(...Yukawa...).  In the MASSLESS/free limit (M->0, Y->0) c=d=0 and the
   gravitational sector is PURE COUNTING:  1/(2 kappa0^2) = 96 f2 Lambda^2/(24 pi^2)
   = 4 f2 Lambda^2/pi^2  PER unit Tr(1_F), and gamma0 = 48 f4 Lambda^4/(4 pi^2)
   = 12 f4 Lambda^4/pi^2  PER unit Tr(1_F).  These per-d.o.f. numbers ARE the
   heat-kernel a0 and a2 of one Dirac/Weyl mode.

  Heat-kernel a0, a2 of a Laplace-type operator P = -(D^2)
  [Gilkey; Vassilevich hep-th/0306138 eqs.(4.26),(4.27)]:
     a0(x) = (4 pi)^{-2} tr_V(1)
     a2(x) = (4 pi)^{-2} (1/6) tr_V(6 E + R)       (E = endomorphism)
  For the Dirac square (Lichnerowicz)  E = -R/4, tr_V(1)=4:
     a2 ~ (4 pi)^{-2}(1/6) tr_V(R - 6R/4) = (4 pi)^{-2}(1/6)*4*(-R/2)
        = -(4 pi)^{-2} R/3      (sign/normalization tracked below).

  Trace-anomaly central charges (for the a4 / -18/11 cross-check)
  [Duff arXiv:2003.02688 Table 1]:
     scalar (a,c)=(1/360,1/120); Weyl (11/720,1/40); vector (31/180,1/10).

  Pauli / supertrace cancellation of the quartic vacuum energy
  [Pauli 1951; Zeldovich; Visser arXiv:1610.07264 "Lorentz invariance and the
   zero-point stress-energy tensor"; Akhmedov hep-th/0204048]:
     Sum_bosons (-1)^{2J}(2J+1) - Sum_fermions ... ;  the Lambda^4 divergence
     cancels iff  sum_B 1 = sum_F 1 (equal boson/fermion counts), the Lambda^2
     iff sum (-1)^F m^2 = 0, the log iff sum (-1)^F m^4 = 0 (the three
     supertrace conditions  STr M^0 = STr M^2 = STr M^4 = 0).

All numbers are EXACT sympy rationals.  No fudge: a clean negative (no second
identity; induced Lambda has the standard quartic fine-tuning; fermion counting
does NOT help) is a full result.
"""

import sympy as sp
import json
import os

R = sp.Rational
pi = sp.pi
OUT = os.path.dirname(os.path.abspath(__file__)) + "/"

results = {"meta": {
    "title": "VYPOCET-17: cosmological constant from fermion-induced gravity (H4g-3)",
    "date": "2026-06-06",
    "hypothesis": "H4g-3: if spectral action = fermion-induced (Sakharov) gravity "
                  "(F-014, -18/11 index-protected), what does the SAME logic predict "
                  "for Lambda?  Is there a SECOND content-independent ratio?",
    "builds_on": ["F-003", "F-014", "VYPOCET-02", "VYPOCET-11"],
    "sources": {
        "spectral_action": "Chamseddine-Connes hep-th/9606001; CCM hep-th/0610241; "
                           "Marcolli 'Spectral Action Gravity and Cosmological Models' "
                           "(NCGCosmoCRP), master expansion + SM coefficients quoted verbatim",
        "heat_kernel_a0_a2": "Gilkey; Vassilevich hep-th/0306138 eqs.(4.26-4.27)",
        "anomaly_a4": "Duff arXiv:2003.02688 Table 1",
        "pauli_supertrace": "Pauli 1951; Visser arXiv:1610.07264; Akhmedov hep-th/0204048"}}}

# ============================================================================
#  FIELD-CONTENT COUNTING  (fermionic d.o.f.)
# ============================================================================
# NCG SM content (per VYPOCET-02):
#   N_W_noNuR = 45  (15 Weyl/gen * 3),  N_W_withNuR = 48  (16 Weyl/gen * 3).
# A 2-component Weyl fermion = 2 real d.o.f. on-shell (1 complex).  In the
# spectral action Tr(1_F) counts the dimension of the finite Hilbert space:
# CC count it as 4 (Dirac, with particle/antiparticle & 2 spin) per "Weyl";
# the K-O-dimension doubling gives 2*16*3 = 96 etc.  Because a0,a2 scale
# LINEARLY in Tr(1_F)=N, every ratio depends on N only through the SAME overall
# factor; the *relative* content dependence is what we test.  We use the Weyl
# COUNT (45 vs 48) as the content label and keep the per-mode (a,c) for a4.
N_W_noNuR = 45
N_W_withNuR = 48
results["content"] = {"N_Weyl_noNuR_45": N_W_noNuR, "N_Weyl_withNuR_48": N_W_withNuR,
                      "delta_nuR": N_W_withNuR - N_W_noNuR}

# ============================================================================
#  (1) + (2)  a0 (Lambda) and a2 (Einstein-Hilbert) coefficients  -- EXACT
# ============================================================================
# Cutoff moments as free symbols (the spectral action is universal in f0,f2,f4):
f0, f2, f4 = sp.symbols('f0 f2 f4', positive=True)
Lam = sp.Symbol('Lambda', positive=True)          # cutoff scale
N = sp.Symbol('N', positive=True)                  # Tr(1_F) overall multiplicity

# --- Heat-kernel a0, a2 of ONE Dirac mode (Gilkey/Vassilevich) --------------
# a0(x) = (4 pi)^{-2} tr_V(1).  Dirac tr_V(1)=4.
inv16pi2 = R(1, 16) / pi**2                          # (4 pi)^{-2} = 1/(16 pi^2)
a0_dirac_density = inv16pi2 * 4                       # = 1/(4 pi^2)
# a2(x) = (4 pi)^{-2}(1/6) tr_V(6E + R).  Dirac E=-R/4, tr_V(1)=4:
#   tr_V(6E+R) = 4*(6*(-1/4)+1)*R = 4*(-1/2)*R = -2 R.
Rsym = sp.Symbol('R')
a2_dirac_density = inv16pi2 * R(1, 6) * (4 * (6 * R(-1, 4) + 1)) * Rsym  # = -R/(48 pi^2)
a2_dirac_coeff_of_R = sp.nsimplify(a2_dirac_density / Rsym)             # = -1/(48 pi^2)

# --- Tie to the spectral-action SM coefficients (massless/free limit) --------
# Marcolli/CCM:  1/(2 kappa0^2) = (96 f2 Lambda^2 - f0 c)/(24 pi^2).  With c=0
# (massless) and Tr(1_F) factored as N:  the E-H coefficient PER d.o.f. is the
# heat-kernel a2 times f2 Lambda^2.  CC normalize so that for the FULL SM
# (Tr(1_F)=96 in their K-O doubled count) the 96 appears.  We keep the structure:
# 1/(2 kappa0^2) = (1/(2 kappa^2)) and gamma0 the effective Lambda.
c_yuk = sp.Symbol('c_yuk', nonnegative=True)         # Tr(M M^dag) Majorana, runs
d_yuk = sp.Symbol('d_yuk', nonnegative=True)         # Tr((M M^dag)^2)
half_kappa_inv = (96 * f2 * Lam**2 - f0 * c_yuk) / (24 * pi**2)   # = 1/(2 kappa0^2)
gamma0 = (48 * f4 * Lam**4 - f2 * Lam**2 * c_yuk + d_yuk) / (4 * pi**2)  # eff. Lambda
alpha0 = -R(3, 10) * f0 / pi**2                      # C^2
tau0 = R(11, 60) * f0 / pi**2                        # R*R*
assert sp.nsimplify(alpha0 / tau0) == R(-18, 11)     # VYPOCET-02 lock

# Pure-counting (massless) limit:  c_yuk=d_yuk=0.
half_kappa_inv_free = half_kappa_inv.subs(c_yuk, 0)  # = 4 f2 Lambda^2/pi^2 (per Tr=96 norm)
gamma0_free = gamma0.subs({c_yuk: 0, d_yuk: 0})      # = 12 f4 Lambda^4/pi^2

# The cosmological term in the action is gamma0 * Int sqrt(g); the standard
# "cosmological constant"  Lambda_cc  is  gamma0 * kappa0^2  (so that it appears
# as  (1/(2k^2)) Int(R) + gamma0 Int(1) = (1/(2k^2)) Int(R - 2 Lambda_cc) ),
# i.e.  Lambda_cc = gamma0 * kappa0^2 = gamma0 / (2 * (1/(2 kappa0^2))).
Lambda_cc = gamma0 / (2 * half_kappa_inv)            # exact symbolic
Lambda_cc_free = sp.simplify(gamma0_free / (2 * half_kappa_inv_free))

results["Q1_a0_cosmological_term"] = {
    "master_expansion": "Tr f(D/Lambda) ~ 2 Lambda^4 f4 a0 + 2 Lambda^2 f2 a2 + f0 a4",
    "a0_is_pure_counting": "a0 = (4 pi)^{-2} Tr(1_F) ; the Lambda^4 prefactor is "
                           "2 f4 Lambda^4 * a0  -> SCALES LINEARLY in N = Tr(1_F)",
    "a0_dirac_density_coeff": str(a0_dirac_density),            # 1/(4 pi^2)
    "gamma0_effective_cosmological_const": str(sp.nsimplify(gamma0)),
    "gamma0_massless_free_limit": str(sp.nsimplify(gamma0_free)),  # 12 f4 Lambda^4/pi^2
    "Lambda_cc_symbolic": str(sp.nsimplify(Lambda_cc)),
    "Lambda_cc_massless": str(sp.nsimplify(Lambda_cc_free)),
    "content_dependence": "LINEAR in N (overall Tr(1_F) factor). 45 vs 48 changes the "
                          "OVERALL magnitude by 48/45 = 16/15, NOT the structure.",
    "ratio_48_over_45": str(R(48, 45))}

results["Q2_a2_einstein_hilbert"] = {
    "a2_dirac_coeff_of_R": str(a2_dirac_coeff_of_R),           # -1/(48 pi^2)
    "half_inverse_kappa_sq": str(sp.nsimplify(half_kappa_inv)),
    "half_inverse_kappa_sq_massless": str(sp.nsimplify(half_kappa_inv_free)),
    "G_induced": "1/(16 pi G) = 1/(2 kappa0^2) ~ f2 Lambda^2 * N  => "
                 "G_induced ~ 1/(f2 Lambda^2 N): LINEAR in N (counting).",
    "content_dependence": "LINEAR in N, same overall factor as a0."}

# ============================================================================
#  (3)  IS THERE A SECOND CONTENT-INDEPENDENT RATIO among {a0,a2,a4}?
# ============================================================================
# The a4 (-18/11) is content-independent because every Weyl fermion carries the
# SAME (a,c) per mode: the ratio of two a4-pieces cancels N.  For a0 and a2 the
# per-mode densities are also fixed numbers, so per-mode ratios are N-free too.
# The QUESTION is whether any DIMENSIONFUL ratio (the physical one: Lambda_cc,
# G_N) is content-free.  Decompose into per-mode densities and check N-cancellation.

# Per-mode (single Dirac) heat-kernel densities, stripped of curvature symbols:
#   a0 density  ~  (4 pi)^{-2} * 4            = 1/(4 pi^2)          [Lambda^4 sector]
#   a2 density  ~  (4 pi)^{-2} * (-1/3)*... R -> coeff -1/(48 pi^2) [Lambda^2 sector]
#   a4 density  ~  the (a,c) pair  (11/720, 1/40) per Weyl          [Lambda^0 sector]
a_weyl, c_weyl = R(11, 720), R(1, 40)
a_scalar, c_scalar = R(1, 360), R(1, 120)
a_vector, c_vector = R(31, 180), R(1, 10)

# Build the three Dirac/Weyl coefficients as PURE NUMBERS (drop pi, curvature):
A0 = a0_dirac_density                     # 1/(4 pi^2)
A2 = sp.Abs(a2_dirac_coeff_of_R)          # 1/(48 pi^2)
A4_c = c_weyl                             # 1/40  (the C^2 / c-anomaly piece, per Weyl)
A4_a = a_weyl                             # 11/720 (the Euler / a-anomaly piece)

# Pairwise per-mode ratios (all manifestly N-free since each is per single mode):
ratio_a0_a2 = sp.nsimplify(A0 / A2)       # = 12
ratio_a2_a4c = sp.nsimplify(A2 / (A4_c / pi**2))  # keep pi for honesty
ratio_a4 = sp.nsimplify(A4_c / (-A4_a))   # = -18/11 (re-confirm)
assert ratio_a4 == R(-18, 11)

# The DECISIVE test: the PHYSICAL dimensionless combination that the induced
# action predicts.  Lambda_cc (mass^2) and m_Pl^2 = 1/G.  Their ratio in the
# induced theory:
#   Lambda_cc        = gamma0 / (2 * (1/(2 kappa0^2)))   [from above]
#   m_Pl^2  ~  1/(8 pi G_eff) = 1/(2 kappa0^2) = half_kappa_inv
# So  Lambda_cc / m_Pl^2  =  gamma0 / (2 * half_kappa_inv^2).
mPl2 = half_kappa_inv                                  # ~ f2 Lambda^2 * (counting)
Lcc_over_mPl2 = sp.simplify(gamma0 / (2 * mPl2**2))
Lcc_over_mPl2_free = sp.simplify(gamma0_free / (2 * half_kappa_inv_free**2))

# Now: is Lambda_cc itself (massless) N-INDEPENDENT?  Re-instate the explicit
# Tr(1_F)=N multiplicity that the per-mode densities omit.  Both gamma0 and
# half_kappa_inv scale as N (each is N * per-mode-density * cutoff-moment):
#   gamma0          = N * g_hat * f4 Lambda^4 / pi^2     (g_hat per-mode number)
#   half_kappa_inv  = N * k_hat * f2 Lambda^2 / pi^2
g_hat, k_hat = sp.symbols('g_hat k_hat', positive=True)   # per-mode pure numbers
gamma0_N = N * g_hat * f4 * Lam**4 / pi**2
mPl2_N = N * k_hat * f2 * Lam**2 / pi**2
Lambda_cc_N = sp.simplify(gamma0_N / (2 * mPl2_N))         # N CANCELS in this ratio
Lcc_over_mPl2_N = sp.simplify(gamma0_N / (2 * mPl2_N**2))  # N SURVIVES (1/N)

Lambda_cc_is_N_free = (sp.simplify(sp.diff(Lambda_cc_N, N)) == 0)
Lcc_over_mPl2_is_N_free = (sp.simplify(sp.diff(Lcc_over_mPl2_N, N)) == 0)

results["Q3_second_index_identity"] = {
    "per_mode_a0_density": str(A0),
    "per_mode_a2_density_coeff_of_R": str(a2_dirac_coeff_of_R),
    "per_mode_a4_pieces_(a,c)_per_Weyl": [str(A4_a), str(A4_c)],
    "ratio_a0_over_a2_per_mode": str(ratio_a0_a2),          # 12  (pure number!)
    "ratio_a4_c_over_minus_a": str(ratio_a4),               # -18/11
    "Lambda_cc_over_mPl2_symbolic": str(sp.nsimplify(Lcc_over_mPl2)),
    "Lambda_cc_over_mPl2_massless": str(sp.nsimplify(Lcc_over_mPl2_free)),
    "Lambda_cc_(massless,with_N)": str(Lambda_cc_N),
    "Lambda_cc_is_N_independent": bool(Lambda_cc_is_N_free),
    "Lambda_cc_N_independence_is_DEGENERATE": "Lambda_cc = (f4/f2) Lambda^2 g_hat/(2 k_hat): "
        "N cancels ONLY because numerator (gamma0) and denominator (m_Pl^2) carry the SAME "
        "overall Tr(1_F)=N. This is NOT index protection: the result still carries (f4/f2) "
        "and Lambda^2 -- it is DIMENSIONFUL and CUTOFF-SHAPE-DEPENDENT (scheme-dependent), "
        "unlike the dimensionless, f-independent -18/11.",
    "Lcc_over_mPl2_(with_N)": str(Lcc_over_mPl2_N),
    "Lcc_over_mPl2_is_N_independent": bool(Lcc_over_mPl2_is_N_free),
    "Lcc_over_mPl2_carries_explicit_1_over_N": True,
    "VERDICT": None  # filled below
}

# ----------------------------------------------------------------------------
# KEY ANALYSIS for Q3:
# a0:a2 per-mode ratio = 12 is a clean rational, BUT it is NOT an index ratio:
#   it relates the Lambda^4 and Lambda^2 SECTORS, which carry DIFFERENT powers
#   of the cutoff (f4 Lambda^4 vs f2 Lambda^2) and DIFFERENT cutoff moments
#   (f4 vs f2).  Unlike -18/11 (a ratio WITHIN a4, same Lambda^0, same f0, so
#   f0 and Lambda CANCEL leaving a pure number), the a0/a2 ratio carries
#   f4 Lambda^4/(f2 Lambda^2) = (f4/f2) Lambda^2 -- it is DIMENSIONFUL and
#   CUTOFF-FUNCTION-DEPENDENT.  So '12' is NOT a convention-free invariant.
# The physical dimensionless ratio Lambda_cc/m_Pl^2 ~ (f4/f2^... ) Lambda^2 ... :
#   it depends on f4, f2 (cutoff shape) AND on 1/N -> it is BOTH scheme-dependent
#   AND content-dependent.  There is NO second -18/11-type identity.
# The ONLY genuinely content-independent, scheme-robust ratio in the whole
# expansion is the a4-internal alpha0/tau0 = -18/11, precisely because it is the
# ratio of two terms at the SAME order (f0, Lambda^0) -> the index-protected one.
# ----------------------------------------------------------------------------
second_identity_exists = False
results["Q3_second_index_identity"]["VERDICT"] = (
    "NO second index-like identity. The a0:a2 per-mode ratio is a clean rational "
    "(12) but is NOT convention-free: a0 and a2 sit at DIFFERENT cutoff orders "
    "(f4 Lambda^4 vs f2 Lambda^2), so their ratio carries (f4/f2) Lambda^2 -- "
    "dimensionful and cutoff-shape-dependent. Only -18/11 (a ratio WITHIN a4, "
    "same f0 and Lambda^0) is scheme-robust and index-protected. The physical "
    "Lambda_cc/m_Pl^2 depends on f4, f2 AND on 1/N (content), so it is neither "
    "scheme-free nor content-free. The -18/11 identity does NOT have a "
    "cosmological-constant sibling.")

# ============================================================================
#  (4)  CONFRONT THE COSMOLOGICAL CONSTANT PROBLEM
# ============================================================================
# (4a) Cutoff scaling of the induced Lambda.
#   gamma0 ~ 48 f4 Lambda^4 / (4 pi^2)  = 12 f4 Lambda^4/pi^2 (massless).
#   This is the STANDARD quartic vacuum-energy divergence (Lambda^4), exactly
#   the cosmological-constant disaster.  At Lambda ~ M_Planck ~ 1.2e19 GeV and
#   observed rho_Lambda ~ (2.3e-3 eV)^4, the ratio is ~10^120 (well-known).
LambdaPl_GeV = sp.Rational(122089, 100) * sp.Integer(10)**16   # 1.22089e19 GeV (M_Pl)
rho_obs_GeV4 = (sp.Rational(23, 10) * sp.Integer(10)**(-12))**4  # (2.3e-3 eV)^4 in GeV^4
# induced (order of magnitude, f4~O(1)): rho_ind ~ Lambda^4 ~ M_Pl^4
rho_ind_GeV4 = LambdaPl_GeV**4
mismatch_orders = sp.floor(sp.log(rho_ind_GeV4 / rho_obs_GeV4, 10))

# (4b) Does fermion induction make it WORSE, SAME, or cancel?
#   The induced gamma0 is purely fermionic (the spectral action loop is the
#   Dirac sea).  Sign: f4 = Int x f(x) dx > 0 for a positive cutoff profile, so
#   gamma0 > 0 -- a POSITIVE (de Sitter-like) induced cosmological constant, but
#   of Planckian magnitude.  Adding nu_R (45->48) MULTIPLIES gamma0 by 48/45 =
#   16/15 > 1: it makes the induced Lambda LARGER, never cancels it, and never
#   changes its sign (all fermions add with the SAME sign in Tr f(D/Lambda)).
gamma0_45_over_48 = R(45, 48)            # ratio of magnitudes (no nu_R)/(with nu_R)
nuR_makes_lambda = "LARGER" if R(48, 45) > 1 else "smaller"

# (4c) Pauli-type supertrace cancellation condition for the NCG content.
#   The quartic divergence cancels iff bosonic and fermionic d.o.f. counts are
#   EQUAL (STr 1 = 0): n_B - n_F = 0.  Count the NCG SM on-shell d.o.f.:
#   FERMIONS (Weyl, 2 real each) :  45 Weyl (no nuR) or 48 (with nuR)
#       -> n_F = 2 * N_W  (on-shell real d.o.f.).
#   BOSONS: gauge  SU(3)xSU(2)xU(1): 8+3+1 = 12 massless vectors * 2 pol = 24;
#       Higgs complex doublet = 4 real scalars.  -> n_B = 24 + 4 = 28.
n_F_45 = 2 * 45
n_F_48 = 2 * 48
n_B = 24 + 4                              # 28
STr1_45 = n_B - n_F_45                    # 28 - 90 = -62
STr1_48 = n_B - n_F_48                    # 28 - 96 = -68
pauli_cancels_45 = (STr1_45 == 0)
pauli_cancels_48 = (STr1_48 == 0)
# nuR moves n_F from 90 to 96 -> STr1 from -62 to -68: makes the boson/fermion
# IMBALANCE WORSE (more negative), i.e. drives the quartic divergence further
# from cancellation, not toward it.

# The three Pauli/supertrace conditions (STr M^0, M^2, M^4) for finiteness:
#   STr 1   = 0  (quartic),  STr M^2 = 0 (quadratic),  STr M^4 = 0 (log).
#   NCG content has STr 1 != 0 -> quartic NOT cancelled.  (Even SUSY, which
#   sets STr 1 = 0, leaves Lambda^2/log unless masses are degenerate.)
supertrace = {
    "STr_1_45_noNuR": STr1_45, "STr_1_48_withNuR": STr1_48,
    "quartic_cancels_45": bool(pauli_cancels_45),
    "quartic_cancels_48": bool(pauli_cancels_48),
    "nuR_effect_on_STr1": "STr 1 goes -62 -> -68: nu_R makes the boson/fermion "
                          "imbalance WORSE (more fermions), driving the quartic "
                          "divergence FURTHER from the Pauli cancellation, not toward it."}

results["Q4_cosmological_constant_problem"] = {
    "induced_Lambda_cutoff_scaling": "gamma0 ~ 12 f4 Lambda^4 / pi^2 : QUARTIC in the "
        "cutoff -- the standard cosmological-constant divergence.",
    "induced_Lambda_sign": "f4 = Int x f(x) dx > 0 for a positive cutoff -> gamma0 > 0 "
        "(positive / de Sitter-like), Planckian magnitude.",
    "naive_mismatch_orders_of_magnitude": int(mismatch_orders),  # ~120
    "fermion_induction_makes_it": "SAME-as-standard (quartic). Fermion induction does "
        "NOT soften it: the Dirac sea contributes the full Lambda^4. It makes it "
        "marginally LARGER per fermion, never cancels.",
    "nuR_effect": {
        "magnitude_ratio_noNuR_over_withNuR": str(gamma0_45_over_48),  # 45/48=15/16
        "nuR_makes_induced_Lambda": nuR_makes_lambda,                  # LARGER
        "nuR_flips_sign": False,
        "reason": "All fermions enter Tr f(D/Lambda) with the SAME sign (it is a trace "
                  "over the positive-definite fermionic Hilbert space); nu_R adds, never "
                  "subtracts. 45->48 multiplies gamma0 by 48/45 = 16/15."},
    "pauli_supertrace_cancellation": supertrace,
    "verdict": "Induced Lambda is cutoff-QUARTIC (standard disaster). Fermion induction "
               "does NOT help and nu_R makes the boson/fermion count imbalance WORSE "
               "(STr 1 = -62 -> -68). No supertrace condition is met by the NCG SM "
               "content. The cosmological-constant fine-tuning problem is UNTOUCHED by "
               "the -18/11 fermion-induction logic."}

# ============================================================================
#  VERDICTS
# ============================================================================
verdict = {
    "a0_a2_scale_linearly_in_N": True,
    "no_second_content_independent_ratio": bool(not second_identity_exists),
    "only_minus_18_11_is_index_protected": True,
    "Lambda_cc_over_mPl2_depends_on_cutoff_and_N": True,
    "induced_Lambda_is_cutoff_quartic": True,
    "fermion_induction_does_NOT_solve_CC_problem": True,
    "nuR_45_to_48_makes_imbalance_worse_not_cancel": bool(STr1_48 < STr1_45 < 0),
    "H4g-3_clean_negative_closes_draft02_last_risk": True,
}
results["VERDICT"] = verdict

# ============================================================================
#  PRINT + SAVE
# ============================================================================
def P(*a):
    print(*a)

P("=" * 78)
P(" VYPOCET-17  --  LAMBDA-INDUKCE : cosmological constant from fermion-induction")
P("=" * 78)
P("\n[Q1+Q2  a0 (Lambda) and a2 (Einstein-Hilbert) coefficients]")
P(f"  master:  Tr f(D/Lambda) ~ 2 Lambda^4 f4 a0 + 2 Lambda^2 f2 a2 + f0 a4")
P(f"  a0 density (Dirac) = {a0_dirac_density}   (= Tr(1)/(16 pi^2), pure counting)")
P(f"  a2 coeff of R      = {a2_dirac_coeff_of_R}")
P(f"  gamma0 (eff Lambda, massless) = {sp.nsimplify(gamma0_free)}")
P(f"  1/(2 kappa0^2)     (massless) = {sp.nsimplify(half_kappa_inv_free)}")
P(f"  alpha0/tau0 = {sp.nsimplify(alpha0/tau0)}   (VYPOCET-02 lock holds)")
P(f"  => a0, a2 scale LINEARLY in N; 45->48 is overall x 48/45 = 16/15")

P("\n[Q3  second content-independent ratio?]")
P(f"  per-mode a0/a2 ratio = {ratio_a0_a2}  (clean rational BUT cross-order: carries (f4/f2)Lambda^2)")
P(f"  a4 ratio c/(-a)      = {ratio_a4}  (the index-protected -18/11)")
P(f"  Lambda_cc N-independent?     {Lambda_cc_is_N_free}")
P(f"  Lambda_cc/m_Pl^2 N-independent? {Lcc_over_mPl2_is_N_free}  (1/N -> content-DEPENDENT)")
P(f"  VERDICT: NO second -18/11-type identity for Lambda.")

P("\n[Q4  cosmological constant problem]")
P(f"  induced gamma0 ~ 12 f4 Lambda^4/pi^2 : QUARTIC (standard disaster)")
P(f"  naive mismatch ~ 10^{int(mismatch_orders)}")
P(f"  Pauli STr 1 (n_B - n_F): 45 -> {STr1_45},  48 -> {STr1_48}   (never 0)")
P(f"  nu_R makes the boson/fermion imbalance WORSE (-62 -> -68), no cancellation.")

P("\n[VERDICT]")
for k, v in verdict.items():
    P(f"  {k}: {v}")

with open(OUT + "results.json", "w") as fh:
    json.dump(results, fh, indent=2, ensure_ascii=False)
P("\nWrote results.json")

# ============================================================================
#  PLOTS
# ============================================================================
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# --- Plot 1: the three sectors a0,a2,a4 -- cutoff scaling & what is protected --
fig, ax = plt.subplots(figsize=(10, 5.4))
sectors = ["a0\n(cosmological)", "a2\n(Einstein-Hilbert)", "a4\n(Weyl^2 / Euler)"]
cutoff_power = [4, 2, 0]
moment = ["f4", "f2", "f0"]
content_scaling = ["~ N", "~ N", "~ N (cancels in ratio)"]
protected = ["NO", "NO", "YES (-18/11)"]
xs = range(len(sectors))
bars = ax.bar(xs, cutoff_power, color=["C3", "C1", "C0"], alpha=0.85)
ax.set_xticks(list(xs)); ax.set_xticklabels(sectors)
ax.set_ylabel("cutoff power  $\\Lambda^{4-k}$")
for i, b in enumerate(bars):
    ax.text(b.get_x() + b.get_width()/2, cutoff_power[i] + 0.08,
            f"moment {moment[i]}\n{content_scaling[i]}\nindex-protected: {protected[i]}",
            ha="center", va="bottom", fontsize=8.5)
ax.set_ylim(0, 5.4)
ax.set_title("VYPOCET-17: only $a_4$ carries a content-independent, index-protected\n"
             "ratio ($-18/11$). $a_0$ (cosmological) is cutoff-QUARTIC and content-LINEAR "
             "-- no second identity.")
ax.grid(axis="y", alpha=0.3)
fig.tight_layout()
fig.savefig(OUT + "sector_ledger.png", dpi=140)
P("Wrote sector_ledger.png")

# --- Plot 2: Pauli supertrace STr 1 vs nu_R, and the quartic CC mismatch -------
fig2, (axA, axB) = plt.subplots(1, 2, figsize=(12, 5.0))
# (A) boson/fermion count balance
labels = ["no $\\nu_R$ (45 Weyl)", "with $\\nu_R$ (48 Weyl)"]
nF = [n_F_45, n_F_48]
nBb = [n_B, n_B]
x = range(2)
axA.bar([i - 0.2 for i in x], nBb, width=0.4, label="bosons $n_B$=28", color="C0")
axA.bar([i + 0.2 for i in x], nF, width=0.4, label="fermions $n_F$", color="C3")
for i in x:
    axA.text(i, max(nF[i], n_B) + 2, f"STr 1 = {n_B - nF[i]}", ha="center", fontsize=10)
axA.set_xticks(list(x)); axA.set_xticklabels(labels)
axA.set_ylabel("on-shell real d.o.f.")
axA.set_title("Pauli quartic-cancellation needs $n_B=n_F$ (STr 1 = 0)\n"
              "$\\nu_R$ makes the imbalance WORSE: $-62 \\to -68$")
axA.legend(); axA.grid(axis="y", alpha=0.3)
# (B) the quartic CC mismatch (orders of magnitude)
axB.bar(["induced\n$\\sim M_{Pl}^4$", "observed\n$\\rho_\\Lambda$"],
        [int(mismatch_orders), 0], color=["C3", "C2"])
axB.set_ylabel("$\\log_{10}$ (vacuum energy density / observed)")
axB.set_title(f"Induced $\\Lambda$ is cutoff-quartic: mismatch $\\sim 10^{{{int(mismatch_orders)}}}$\n"
              "fermion induction does NOT soften it")
axB.text(0, int(mismatch_orders) * 0.5, f"$10^{{{int(mismatch_orders)}}}$",
         ha="center", fontsize=14, color="white", fontweight="bold")
axB.grid(axis="y", alpha=0.3)
fig2.tight_layout()
fig2.savefig(OUT + "pauli_and_quartic.png", dpi=140)
P("Wrote pauli_and_quartic.png")
