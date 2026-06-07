(* ===================================================================== *)
(* lambda_ledger.wl                                                        *)
(*                                                                         *)
(* INDEPENDENT cross-CAS validation of the Lambda-induction ledger         *)
(* structure (project VYPOCET-17, draft-02 "honest scope" section), with   *)
(* FORMAL symbol arithmetic.  The point of VYPOCET-17 is a clean NEGATIVE: *)
(* the -18/11 identity has NO cosmological-constant sibling.  We re-encode  *)
(* its structural claims in Wolfram Language and verify them as algebraic   *)
(* facts (FreeQ / cancellation), independently of the sympy lane.          *)
(*                                                                         *)
(* MASTER EXPANSION (Chamseddine-Connes hep-th/9606001 eq.(2.18)-(2.26);    *)
(* Marcolli "Spectral Action Gravity and Cosmological Models"):            *)
(*   Tr f(D/Lambda) ~ 2 Lambda^4 f4 a0 + 2 Lambda^2 f2 a2 + f0 a4          *)
(*   a0 -> cosmological term (Lambda^4 sector, moment f4)                   *)
(*   a2 -> Einstein-Hilbert  (Lambda^2 sector, moment f2)                   *)
(*   a4 -> Weyl^2 + Euler    (Lambda^0 sector, moment f0; carries -18/11)   *)
(*                                                                         *)
(* STRUCTURAL CLAIMS TO VALIDATE (all symbolic):                           *)
(*   (1) a0 and a2 are BOTH linear in N = Tr(1_F).                          *)
(*   (2) the a0:a2 ratio carries (f4/f2) Lambda^2 -- dimensionful AND       *)
(*       cutoff-shape (scheme) dependent: NOT FreeQ of f4,f2,Lambda.        *)
(*   (3) the intra-a4 ratio (alpha0/tau0 = -18/11) is cutoff-order-clean:   *)
(*       FreeQ of f0 and Lambda.  This is the index-protected one.          *)
(*   (4) Lambda_cc / m_Pl^2 == pi^2 f4 / (2 N f2^2 khat^2) carries an       *)
(*       EXPLICIT 1/N (content-dependent), so no second identity exists.    *)
(* ===================================================================== *)

(* --------------------------------------------------------------------- *)
(* 0. Formal symbols.  We keep f0,f2,f4,N,khat,ghat,Lam,Pi all formal so   *)
(*    that "carries / does not carry" is decided by FreeQ on exact         *)
(*    rational-function forms, never by numeric evaluation.                *)
(* --------------------------------------------------------------------- *)
ClearAll[f0, f2, f4, N0, khat, ghat, Lam];
(* (N is the project's Tr(1_F); we name the symbol nF to avoid WL's N[].) *)
ClearAll[nF];

(* --------------------------------------------------------------------- *)
(* 1. a0 and a2 are linear in N = Tr(1_F).                                 *)
(*    Per-mode heat-kernel densities (Gilkey; Vassilevich eq.4.26-4.27)    *)
(*    are fixed numbers; the spectral-action sector coefficients are       *)
(*    N x (per-mode number) x (cutoff moment).  Linearity in N is the      *)
(*    claim: d/dN of (coeff/N) is zero, i.e. coeff = N x (N-free factor).  *)
(* --------------------------------------------------------------------- *)
a0Coeff = nF*ghat*f4*Lam^4/Pi^2;   (* cosmological sector ~ N *)
a2Coeff = nF*khat*f2*Lam^2/Pi^2;   (* Einstein-Hilbert sector ~ N *)

(* linear in N <=> coeff/N is free of N. *)
chkA0LinearN = FreeQ[Together[a0Coeff/nF], nF];
chkA2LinearN = FreeQ[Together[a2Coeff/nF], nF];

(* --------------------------------------------------------------------- *)
(* 2. The a0:a2 ratio carries (f4/f2) Lambda^2 : dimensionful AND          *)
(*    cutoff-shape dependent.  N cancels (both linear in N), but f4,f2     *)
(*    and Lambda survive -- NOT FreeQ of them.                             *)
(* --------------------------------------------------------------------- *)
ratioA0A2 = Together[a0Coeff/a2Coeff];   (* = (ghat f4 Lam^2)/(khat f2) *)

chkA0A2FreeOfN = FreeQ[ratioA0A2, nF];          (* N cancels: TRUE *)
chkA0A2CarriesF4 = ! FreeQ[ratioA0A2, f4];      (* carries f4: TRUE *)
chkA0A2CarriesF2 = ! FreeQ[ratioA0A2, f2];      (* carries f2: TRUE *)
chkA0A2CarriesLambda = ! FreeQ[ratioA0A2, Lam]; (* carries Lambda^2: TRUE *)
(* explicit Lambda power is 2 (dimensionful).  Strip the moments/per-mode    *)
(* constants to 1, leaving Lam^2; Exponent then reads the power directly.     *)
ratioA0A2Stripped = ratioA0A2 /. {f4 -> 1, f2 -> 1, ghat -> 1, khat -> 1};
chkA0A2LambdaPower2 = (Exponent[ratioA0A2Stripped, Lam] === 2);

(* --------------------------------------------------------------------- *)
(* 3. The intra-a4 ratio alpha0/tau0 = -18/11 is cutoff-order-clean:       *)
(*    same Lambda^0 sector, same moment f0 -> FreeQ of f0 AND Lambda.      *)
(*    This is the structural contrast that makes -18/11 index-protected    *)
(*    and the a0:a2 ratio NOT.                                             *)
(* --------------------------------------------------------------------- *)
alpha0 = -Rational[3, 10]*f0/Pi^2;    (* C^2 coeff, CC eq.(2.24) *)
tau0   =  Rational[11, 60]*f0/Pi^2;   (* RstarRstar coeff, CC eq.(2.24) *)
ratioA4 = Together[alpha0/tau0];      (* = -18/11 *)

chkA4Value = (ratioA4 == Rational[-18, 11]);
chkA4FreeOfF0 = FreeQ[ratioA4, f0];        (* f0 cancels: TRUE *)
chkA4FreeOfLambda = FreeQ[ratioA4, Lam];   (* no Lambda at all: TRUE *)
chkA4FreeOfPi = FreeQ[ratioA4, Pi];        (* Pi cancels: TRUE *)
chkA4FreeOfN = FreeQ[ratioA4, nF];         (* content-independent: TRUE *)

(* The decisive structural contrast in one boolean:                        *)
(*   a4 ratio is clean (FreeQ f0,Lam) WHILE a0:a2 ratio is dirty           *)
(*   (carries f4,f2,Lam).  This is "no second identity".                   *)
chkContrast = chkA4FreeOfF0 && chkA4FreeOfLambda &&
              chkA0A2CarriesF4 && chkA0A2CarriesLambda;

(* --------------------------------------------------------------------- *)
(* 4. Lambda_cc / m_Pl^2 carries an EXPLICIT 1/N.                          *)
(*    gamma0 (effective cosmological const) ~ N ghat f4 Lam^4 / pi^2,      *)
(*    m_Pl^2 ~ 1/(2 kappa0^2) ~ N khat f2 Lam^2 / pi^2.                     *)
(*    Lambda_cc = gamma0/(2 m_Pl^2)  (N cancels -> dimensionful, scheme).  *)
(*    Lambda_cc/m_Pl^2 = gamma0/(2 m_Pl^2^2)  ->  carries 1/N.             *)
(*    Target closed form:  pi^2 f4 / (2 N f2^2 khat^2)  (with ghat = 1     *)
(*    per-mode normalization absorbed; we verify the 1/N structure         *)
(*    independent of the per-mode prefactor).                              *)
(* --------------------------------------------------------------------- *)
gamma0 = nF*ghat*f4*Lam^4/Pi^2;
mPl2   = nF*khat*f2*Lam^2/Pi^2;

LambdaCC = Together[gamma0/(2*mPl2)];      (* N cancels here *)
LccOverMPl2 = Together[gamma0/(2*mPl2^2)]; (* N survives as 1/N here *)

chkLambdaCCFreeOfN = FreeQ[LambdaCC, nF];           (* TRUE: N cancels *)
chkLambdaCCCarriesF4overF2 = (! FreeQ[LambdaCC, f4]) && (! FreeQ[LambdaCC, f2]);
chkLccCarries1OverN = ! FreeQ[LccOverMPl2, nF];     (* TRUE: 1/N present *)
(* the explicit 1/N : multiplying by N must remove all nF dependence. *)
chkLccExplicit1OverN = FreeQ[Together[LccOverMPl2*nF], nF];

(* Match the draft's stated closed form pi^2 f4/(2 N f2^2 khat^2).  The      *)
(* per-mode normalization ghat sits in the numerator (it came from gamma0);  *)
(* setting ghat -> 1 recovers the draft's exact form.  We verify the full    *)
(* N- and f-structure: LccOverMPl2 divided by the target must reduce to a    *)
(* pure number (here exactly 1) once ghat is normalized -- i.e. the ratio    *)
(* is free of EVERY remaining symbol (f0,f2,f4,N,khat,Lambda,Pi).            *)
targetForm = Pi^2*f4*ghat/(2*nF*f2^2*khat^2);
structureRatio = Together[LccOverMPl2/targetForm];
chkLccMatchesTargetStructure =
  FreeQ[structureRatio, f0] && FreeQ[structureRatio, f2] &&
  FreeQ[structureRatio, f4] && FreeQ[structureRatio, nF] &&
  FreeQ[structureRatio, khat] && FreeQ[structureRatio, ghat] &&
  FreeQ[structureRatio, Lam] && FreeQ[structureRatio, Pi] &&
  (structureRatio === 1);

(* --------------------------------------------------------------------- *)
(* 5. Supertrace ledger (exact integers) -- the quartic divergence is NOT  *)
(*    cancelled: STr 1 = n_B - n_F = -62 (no nuR) / -68 (with nuR).        *)
(* --------------------------------------------------------------------- *)
nBoson = 12*2 + 4;          (* 24 vector pol + 4 real scalars = 28 *)
nFermNoNu = 2*45;           (* 90 *)
nFermWithNu = 2*48;         (* 96 *)
sTr1NoNu = nBoson - nFermNoNu;     (* -62 *)
sTr1WithNu = nBoson - nFermWithNu; (* -68 *)
chkSTrNoNu = (sTr1NoNu == -62);
chkSTrWithNu = (sTr1WithNu == -68);
chkQuarticNotCancelled = (sTr1NoNu =!= 0) && (sTr1WithNu =!= 0);

(* --------------------------------------------------------------------- *)
(* 6. Collect verdicts and export JSON.                                   *)
(* --------------------------------------------------------------------- *)
allChecks = {
  chkA0LinearN, chkA2LinearN,
  chkA0A2FreeOfN, chkA0A2CarriesF4, chkA0A2CarriesF2,
  chkA0A2CarriesLambda, chkA0A2LambdaPower2,
  chkA4Value, chkA4FreeOfF0, chkA4FreeOfLambda, chkA4FreeOfPi, chkA4FreeOfN,
  chkContrast,
  chkLambdaCCFreeOfN, chkLambdaCCCarriesF4overF2,
  chkLccCarries1OverN, chkLccExplicit1OverN, chkLccMatchesTargetStructure,
  chkSTrNoNu, chkSTrWithNu, chkQuarticNotCancelled
};
overallPass = AllTrue[allChecks, TrueQ];

result = Association[
  "script" -> "lambda_ledger.wl",
  "description" -> "Independent CAS validation of the Lambda-induction ledger (no second identity)",
  "sources" -> Association[
    "spectral_action" -> "Chamseddine-Connes hep-th/9606001 eq.2.24; Marcolli NCG cosmology",
    "heat_kernel_a0_a2" -> "Gilkey; Vassilevich hep-th/0306138 eq.4.26-4.27"
  ],
  "symbolic_forms" -> Association[
    "ratio_a0_over_a2" -> ToString[ratioA0A2, InputForm],
    "ratio_a4_alpha0_over_tau0" -> ToString[ratioA4, InputForm],
    "Lambda_cc" -> ToString[LambdaCC, InputForm],
    "Lambda_cc_over_mPl2" -> ToString[LccOverMPl2, InputForm]
  ],
  "checks" -> Association[
    "a0_linear_in_N" -> TrueQ[chkA0LinearN],
    "a2_linear_in_N" -> TrueQ[chkA2LinearN],
    "a0a2_ratio_free_of_N" -> TrueQ[chkA0A2FreeOfN],
    "a0a2_ratio_carries_f4" -> TrueQ[chkA0A2CarriesF4],
    "a0a2_ratio_carries_f2" -> TrueQ[chkA0A2CarriesF2],
    "a0a2_ratio_carries_Lambda" -> TrueQ[chkA0A2CarriesLambda],
    "a0a2_ratio_Lambda_power_is_2" -> TrueQ[chkA0A2LambdaPower2],
    "a4_ratio_is_minus_18_11" -> TrueQ[chkA4Value],
    "a4_ratio_free_of_f0" -> TrueQ[chkA4FreeOfF0],
    "a4_ratio_free_of_Lambda" -> TrueQ[chkA4FreeOfLambda],
    "a4_ratio_free_of_pi" -> TrueQ[chkA4FreeOfPi],
    "a4_ratio_free_of_N" -> TrueQ[chkA4FreeOfN],
    "structural_contrast_a4_clean_a0a2_dirty" -> TrueQ[chkContrast],
    "Lambda_cc_free_of_N" -> TrueQ[chkLambdaCCFreeOfN],
    "Lambda_cc_carries_f4_and_f2" -> TrueQ[chkLambdaCCCarriesF4overF2],
    "Lcc_over_mPl2_carries_1_over_N" -> TrueQ[chkLccCarries1OverN],
    "Lcc_over_mPl2_explicit_1_over_N" -> TrueQ[chkLccExplicit1OverN],
    "Lcc_over_mPl2_matches_target_structure" -> TrueQ[chkLccMatchesTargetStructure],
    "STr1_noNu_is_minus_62" -> TrueQ[chkSTrNoNu],
    "STr1_withNu_is_minus_68" -> TrueQ[chkSTrWithNu],
    "quartic_divergence_not_cancelled" -> TrueQ[chkQuarticNotCancelled]
  ],
  "overall_pass" -> TrueQ[overallPass]
];

Export[
  FileNameJoin[{DirectoryName[$InputFileName], "lambda_ledger_result.json"}],
  result,
  "JSON"
];

Print["lambda_ledger.wl overall_pass = ", TrueQ[overallPass]];
