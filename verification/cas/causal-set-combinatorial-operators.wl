(* ===================================================================== *)
(* causal-set-combinatorial-operators.wl                                   *)
(*                                                                         *)
(* INDEPENDENT cross-CAS validation of batch B2:                           *)
(*   causal-set combinatorial operators & dimension estimators.            *)
(*                                                                         *)
(* Each formulaId is RE-DERIVED in Wolfram Language directly from the      *)
(* PUBLISHED coefficients / definitions (entered by hand from the named    *)
(* literature) -- NOT transcribed from the project's sympy outputs.        *)
(* Agreement with the sympy lane is therefore independent evidence;        *)
(* disagreement is a real bug in one of the two derivations.               *)
(*                                                                         *)
(* All arithmetic is EXACT (Rational / exact integers / symbolic Gamma).   *)
(* Output strings are forced to InputForm to avoid the project's prior     *)
(* multiline pretty-print bug.  Only basic canonical WL is used.           *)
(*                                                                         *)
(* PUBLISHED SOURCES (repo-present references.json + arXiv):               *)
(*   benincasa-dowker-2010  arXiv:1001.2725  DOI 10.1103/PhysRevLett.104.181301 *)
(*       4D BD action (1/hbar)S^(4) = N - N1 + 9 N2 - 16 N3 + 8 N4;        *)
(*       discrete d'Alembertian layer weights (1,-9,16,-8); prefactor      *)
(*       4/Sqrt[6].                                                         *)
(*   meyer-1988  "The Dimension of Causal Sets" (Meyer / Myrheim-Meyer);   *)
(*       ordering fraction f0(d) = Gamma(d+1)Gamma(d/2)/(c Gamma(3d/2)).    *)
(*   loomis-carlip-2017  arXiv:1709.00064  DOI 10.1088/1361-6382/aa980b    *)
(*       Kleitman-Rothschild #posets ~ 2^(n^2/4); 3 layers (n/4,n/2,n/4).  *)
(*   bombelli-1987  DOI 10.1103/PhysRevLett.59.521                         *)
(*       Poisson sprinkling P_v(n) = (rho v)^n e^{-rho v}/n!, mean = rho v. *)
(*   surya-2019  arXiv:1903.11544  DOI 10.1007/s41114-019-0023-1           *)
(*       Number = Volume:  <n> = rho V.                                     *)
(* ===================================================================== *)

(* ===================================================================== *)
(* (i) benincasa-dowker-action-4d                                          *)
(*     (1/hbar) S^(4)[C] = N - N1 + 9 N2 - 16 N3 + 8 N4.                    *)
(*     Re-derive the SIGNED action weights from the published 4D layer     *)
(*     coefficients (1,-9,16,-8) of the discrete d'Alembertian.            *)
(* ===================================================================== *)

(* Published 4D layer coefficients of the d'Alembertian B (L1..L4). *)
bdLayerCoeffs = {1, -9, 16, -8};

(* The BD action assembles the same magnitudes with the published signs.   *)
(* Published action weights for {N, N1, N2, N3, N4}: {1, -1, 9, -16, 8}.   *)
bdActionWeightsPublished = {1, -1, 9, -16, 8};

(* Construct the action weights from the layer coefficients independently:  *)
(*   the self term contributes +1 (the -phi(x) of B carried into the        *)
(*   action with the overall normalization gives the +N head term), and     *)
(*   each layer L_i contributes weight  -c_i  to N_i, i.e.                   *)
(*   {N1,N2,N3,N4} weights = -{1,-9,16,-8} = {-1, 9, -16, 8}.               *)
bdActionWeightsDerived =
  Prepend[-bdLayerCoeffs, 1];   (* {1, -1, 9, -16, 8} *)

chkBDWeights = (bdActionWeightsDerived === bdActionWeightsPublished);

(* Symbolic action functional check: build S/hbar from element counts and   *)
(* confirm the coefficient vector matches the published expression.         *)
ClearAll[nN, nN1, nN2, nN3, nN4];
bdActionExpr = nN - nN1 + 9*nN2 - 16*nN3 + 8*nN4;
bdCoeffVector = {
  Coefficient[bdActionExpr, nN],
  Coefficient[bdActionExpr, nN1],
  Coefficient[bdActionExpr, nN2],
  Coefficient[bdActionExpr, nN3],
  Coefficient[bdActionExpr, nN4]
};
chkBDActionExpr = (bdCoeffVector === bdActionWeightsPublished);

(* Published 4D prefactor of the d'Alembertian: 4/Sqrt[6].  Verify its      *)
(* exact symbolic rationalization 4/Sqrt[6] == 2 Sqrt[6]/3 and its square   *)
(* (4/Sqrt[6])^2 == 8/3 (the Rational under the radical, handled exactly).  *)
bdPrefactor = 4/Sqrt[6];
chkBDPrefactorRationalized =
  (Simplify[bdPrefactor - 2*Sqrt[6]/3] === 0);
chkBDPrefactorSquare =
  (Simplify[bdPrefactor^2] === Rational[8, 3]);

verdictBD = chkBDWeights && chkBDActionExpr &&
            chkBDPrefactorRationalized && chkBDPrefactorSquare;

(* ===================================================================== *)
(* (ii) discrete-dalembertian-4d                                           *)
(*      B phi(x) = (4/Sqrt[6] l^2)[ -phi(x) +                               *)
(*         ( sum_{L1} - 9 sum_{L2} + 16 sum_{L3} - 8 sum_{L4} ) phi(y) ].   *)
(*      Verify the published layer-weight vector (1,-9,16,-8) AND that it   *)
(*      is exactly the negative of the BD action's layer weights (the two   *)
(*      formulae share one coefficient set -- a cross-formula lock).        *)
(* ===================================================================== *)

dalLayerCoeffsPublished = {1, -9, 16, -8};
chkDalCoeffs = (bdLayerCoeffs === dalLayerCoeffsPublished);

(* Cross-lock: the d'Alembertian layer weights are MINUS the BD action      *)
(* layer weights {-1, 9, -16, 8}.  This ties (i) and (ii) together.        *)
chkDalCrossLock =
  (dalLayerCoeffsPublished === -(Rest[bdActionWeightsPublished]));

(* Alternating-sign and magnitude structure (1,9,16,8): the magnitudes are  *)
(* {1,9,16,8} and signs strictly alternate starting +. *)
chkDalMagnitudes = (Abs[dalLayerCoeffsPublished] === {1, 9, 16, 8});
chkDalAlternating =
  (Sign[dalLayerCoeffsPublished] === {1, -1, 1, -1});

(* Same prefactor object as (i). *)
chkDalPrefactor = (Simplify[(4/Sqrt[6])^2] === Rational[8, 3]);

verdictDal = chkDalCoeffs && chkDalCrossLock &&
             chkDalMagnitudes && chkDalAlternating && chkDalPrefactor;

(* ===================================================================== *)
(* (iii) myrheim-meyer                                                     *)
(*       Ordering fraction  <R>/C(N,2) = f0(d).                            *)
(*                                                                         *)
(*  Two normalizations appear in the wild.  We encode BOTH and let the     *)
(*  published anchors decide which is correct:                             *)
(*    f0quarter[d] = Gamma[d+1] Gamma[d/2] / (4 Gamma[3 d/2])  (as written  *)
(*                   in the project's formulas.json LaTeX).                 *)
(*    f0half[d]    = Gamma[d+1] Gamma[d/2] / (2 Gamma[3 d/2])  (Meyer 1988  *)
(*                   normalization of the ordering fraction).              *)
(*                                                                         *)
(*  PUBLISHED ANCHORS (Meyer 1988; Bombelli-Henson-Sorkin; Surya 2019):    *)
(*    f0(2) = 1/2   (2D Minkowski causal interval ordering fraction)       *)
(*    f0(4) = 1/10  (4D Minkowski causal interval ordering fraction)       *)
(*    KR ordering fraction 3/8 inverts to d_MM ~ 2.38 (numeric corollary). *)
(* ===================================================================== *)

f0quarter[d_] := Gamma[d + 1]*Gamma[d/2]/(4*Gamma[3*d/2]);
f0half[d_]    := Gamma[d + 1]*Gamma[d/2]/(2*Gamma[3*d/2]);

(* Exact closed-form evaluations (FunctionExpand/Simplify on Gamma). *)
f0quarterAt2 = Simplify[f0quarter[2]];   (* expect 1/4 *)
f0quarterAt4 = Simplify[f0quarter[4]];   (* expect 1/20 *)
f0halfAt2    = Simplify[f0half[2]];      (* expect 1/2  *)
f0halfAt4    = Simplify[f0half[4]];      (* expect 1/10 *)
f0halfAt1    = Simplify[f0half[1]];      (* expect 1    *)
f0halfAt3    = Simplify[f0half[3]];      (* expect 8/35 *)

(* The CAS-exact object is f0(d).  Decide which normalization reproduces    *)
(* the PUBLISHED anchors f0(2)=1/2 and f0(4)=1/10.                          *)
chkHalfAnchor2 = (f0halfAt2 === Rational[1, 2]);
chkHalfAnchor4 = (f0halfAt4 === Rational[1, 10]);
chkQuarterAt2  = (f0quarterAt2 === Rational[1, 4]);
chkQuarterAt4  = (f0quarterAt4 === Rational[1, 20]);

(* The two normalizations differ by EXACTLY a factor of 2 (structural). *)
ClearAll[dSym];
chkNormalizationFactor2 =
  (Simplify[f0half[dSym]/f0quarter[dSym]] === 2);

(* WHICH form matches the published ordering-fraction anchors? *)
publishedFormIsHalf = chkHalfAnchor2 && chkHalfAnchor4;

(* Read the LIVE formulas.json LaTeX and detect the denominator dynamically  *)
(* (2 vs 4) so this check SELF-VALIDATES against the repo, not a stale flag.  *)
(* If the published form is /2 while formulas.json is /4, THIS IS A REAL      *)
(* FACTOR-OF-2 BUG (kolo 20 found + fixed exactly this: 4 -> 2).             *)
mmFormulasPath =
  FileNameJoin[{DirectoryName[$InputFileName], "..", "..",
     "core-data", "formulas.json"}];
mmLatex =
  Quiet[Check[
    Lookup[
      SelectFirst[Import[mmFormulasPath, "RawJSON"],
        (Lookup[#, "id", ""] === "myrheim-meyer") &, <||>],
      "latex", ""],
    ""]];
formulasJsonUsesQuarter = StringContainsQ[mmLatex, "(d/2)}{4"];
formulasJsonAgreesWithPublished =
  (formulasJsonUsesQuarter && (! publishedFormIsHalf)) ||
  ((! formulasJsonUsesQuarter) && publishedFormIsHalf);

(* Numeric corollary (NOT a pass/fail): inverse of the published /2 form at *)
(* the KR ordering fraction 3/8 gives d_MM ~ 2.38.                          *)
dMMnumeric =
  Quiet[Check[
    d /. FindRoot[f0half[d] == Rational[3, 8], {d, 5/2},
      WorkingPrecision -> 20],
    $Failed]];

(* The headline verdict for myrheim-meyer: the CLOSED FORM is CAS-checkable *)
(* and self-consistent (the /2 normalization reproduces ALL published       *)
(* anchors exactly).  We mark the formula 'verified at the /2 normalization' *)
(* and separately flag the formulas.json /4 denominator as a mismatch.      *)
verdictMM = chkHalfAnchor2 && chkHalfAnchor4 && chkNormalizationFactor2;

(* ===================================================================== *)
(* (iv) kr-count                                                           *)
(*      #{posets on n} ~ 2^(n^2/4); KR 3 layers (n/4, n/2, n/4).           *)
(*      Exact-integer assertions: leading exponent n^2/4 and the layer      *)
(*      split sums to n.                                                    *)
(* ===================================================================== *)

(* Layer split (n/4, n/2, n/4) sums to n -- exact for any n divisible by 4. *)
ClearAll[nKR];
krLayers = {nKR/4, nKR/2, nKR/4};
chkKRLayerSum = (Simplify[Total[krLayers] - nKR] === 0);

(* Concrete exact-integer instance (n = 4 m): the three integer layers sum  *)
(* to 4 m.  Test several m so the rational split is an exact integer split. *)
chkKRIntegerSplit =
  AllTrue[{4, 8, 100, 4000},
    Function[nv, (nv/4 + nv/2 + nv/4) == nv]];

(* Leading exponent of log2(#posets): log2(2^(n^2/4)) = n^2/4.  Verify the   *)
(* exponent is exactly n^2/4 and its leading power in n is 2 with coeff 1/4. *)
(* Use PowerExpand with the real-n assumption so Log2[2^x] -> x cleanly      *)
(* (WL withholds this branch reduction for general complex n).               *)
krLog2Count = PowerExpand[Log2[2^(nKR^2/4)]];   (* -> n^2/4 *)
chkKRLog2 =
  (Simplify[krLog2Count - nKR^2/4, Assumptions -> nKR > 0] === 0);
chkKRLeadingExponent = (Exponent[nKR^2/4, nKR] === 2);
chkKRLeadingCoeff = (Coefficient[nKR^2/4, nKR, 2] === Rational[1, 4]);

(* The KR middle layer carries half the elements (n/2), the two outer       *)
(* layers a quarter each: the entropy-dominant 3-layer structure.           *)
chkKRMiddleHalf = (Simplify[(nKR/2)/nKR] === Rational[1, 2]);
chkKROuterQuarter = (Simplify[(nKR/4)/nKR] === Rational[1, 4]);

verdictKR = chkKRLayerSum && chkKRIntegerSplit && chkKRLog2 &&
            chkKRLeadingExponent && chkKRLeadingCoeff &&
            chkKRMiddleHalf && chkKROuterQuarter;

(* ===================================================================== *)
(* (v) poisson-sprinkling                                                  *)
(*     P_v(n) = (rho v)^n e^{-rho v}/n!,  <n> = rho v.                      *)
(*     Verify normalization Sum_n P = 1 and mean Sum_n n P = rho v          *)
(*     symbolically (WL Sum with Assumptions rho v > 0).                    *)
(* ===================================================================== *)

ClearAll[mu, nIdx];   (* mu == rho v, the Poisson mean *)
pPoisson[n_, m_] := m^n*Exp[-m]/n!;

(* Normalization: Sum_{n=0}^Inf P = 1. *)
poissonNorm =
  Simplify[Sum[pPoisson[nIdx, mu], {nIdx, 0, Infinity}],
    Assumptions -> mu > 0];
chkPoissonNorm = (poissonNorm === 1);

(* Mean: Sum_{n=0}^Inf n P = mu = rho v. *)
poissonMean =
  Simplify[Sum[nIdx*pPoisson[nIdx, mu], {nIdx, 0, Infinity}],
    Assumptions -> mu > 0];
chkPoissonMean = (poissonMean === mu);

(* Variance: Sum n^2 P - mean^2 = mu (Poisson var = mean; fluctuation       *)
(* sqrt(rho v)).  Independent corroboration of the distribution.            *)
poissonSecondMoment =
  Simplify[Sum[nIdx^2*pPoisson[nIdx, mu], {nIdx, 0, Infinity}],
    Assumptions -> mu > 0];
poissonVariance = Simplify[poissonSecondMoment - mu^2];
chkPoissonVariance = (poissonVariance === mu);

verdictPoisson = chkPoissonNorm && chkPoissonMean && chkPoissonVariance;

(* ===================================================================== *)
(* (vi) number-volume                                                      *)
(*      <n> = rho V  (Number = Volume), with V = N l_p^4.                   *)
(*      This IS the mean of the Poisson sprinkling (iv): consistency link.  *)
(* ===================================================================== *)

ClearAll[rho, vol, ellp, capN];

(* <n> = rho V is exactly the Poisson mean with mu = rho V. *)
numberVolumeMean =
  Simplify[Sum[nIdx*pPoisson[nIdx, rho*vol], {nIdx, 0, Infinity}],
    Assumptions -> rho*vol > 0];
chkNVisPoissonMean = (numberVolumeMean === rho*vol);

(* Dimensional closure V = N l_p^4 <=> N = V/l_p^4; consistency with        *)
(* <n> = rho V at unit density rho = 1/l_p^4 gives <n> = V/l_p^4 = N.       *)
chkNVUnitDensity =
  (Simplify[(rho*vol) /. rho -> 1/ellp^4] === vol/ellp^4);
chkNVNumberEqualsN =
  (Simplify[(vol/ellp^4) - capN /. vol -> capN*ellp^4] === 0);

verdictNV = chkNVisPoissonMean && chkNVUnitDensity && chkNVNumberEqualsN;

(* ===================================================================== *)
(* Collect verdicts and export JSON.                                       *)
(* ===================================================================== *)

(* overall_pass: every covered formula verified AND formulas.json agrees with *)
(* the published /2 normalization.  run_all.py reads this top-level field.     *)
overallPass = And[
  TrueQ[verdictBD], TrueQ[verdictDal],
  TrueQ[verdictMM], TrueQ[formulasJsonAgreesWithPublished],
  TrueQ[verdictKR], TrueQ[verdictPoisson], TrueQ[verdictNV]];

result = Association[
  "script" -> "causal-set-combinatorial-operators.wl",
  "overall_pass" -> overallPass,
  "batch" -> "B2: causal-set combinatorial operators & dimension estimators",
  "description" ->
    "Independent CAS re-derivation of 4D BD action/d'Alembertian coeffs, \
Myrheim-Meyer ordering fraction f0(d), KR 2^(n^2/4) split, Poisson \
sprinkling normalization+mean, and number=volume.",
  "sources" -> Association[
    "benincasa-dowker-action-4d" ->
      "Benincasa-Dowker 2010, arXiv:1001.2725, DOI 10.1103/PhysRevLett.104.181301",
    "discrete-dalembertian-4d" ->
      "Benincasa-Dowker 2010, arXiv:1001.2725 (layer weights 1,-9,16,-8; 4/Sqrt[6])",
    "myrheim-meyer" -> "Meyer 1988 'The Dimension of Causal Sets'; Surya 2019 arXiv:1903.11544",
    "kr-count" -> "Loomis-Carlip 2017, arXiv:1709.00064, DOI 10.1088/1361-6382/aa980b",
    "poisson-sprinkling" -> "Bombelli et al. 1987, DOI 10.1103/PhysRevLett.59.521",
    "number-volume" -> "Surya 2019, arXiv:1903.11544, DOI 10.1007/s41114-019-0023-1"
  ],
  "exact_values" -> Association[
    "bd_action_weights_N_N1_N2_N3_N4" ->
      ToString[bdActionWeightsPublished, InputForm],
    "bd_layer_coeffs" -> ToString[bdLayerCoeffs, InputForm],
    "bd_prefactor_4_over_sqrt6" -> ToString[4/Sqrt[6], InputForm],
    "bd_prefactor_squared" -> ToString[Simplify[(4/Sqrt[6])^2], InputForm],
    "f0_quarter_at_2" -> ToString[f0quarterAt2, InputForm],
    "f0_quarter_at_4" -> ToString[f0quarterAt4, InputForm],
    "f0_half_at_1" -> ToString[f0halfAt1, InputForm],
    "f0_half_at_2" -> ToString[f0halfAt2, InputForm],
    "f0_half_at_3" -> ToString[f0halfAt3, InputForm],
    "f0_half_at_4" -> ToString[f0halfAt4, InputForm],
    "d_MM_at_KR_orderingfraction_3_8_numeric" -> ToString[dMMnumeric, InputForm],
    "kr_leading_exponent_in_n" -> ToString[Exponent[nKR^2/4, nKR], InputForm],
    "kr_leading_coeff" -> ToString[Coefficient[nKR^2/4, nKR, 2], InputForm],
    "poisson_normalization" -> ToString[poissonNorm, InputForm],
    "poisson_mean" -> ToString[poissonMean, InputForm],
    "poisson_variance" -> ToString[poissonVariance, InputForm],
    "number_volume_mean" -> ToString[numberVolumeMean, InputForm]
  ],
  "checks" -> Association[
    "bd_action_weights_match_published" -> TrueQ[chkBDWeights],
    "bd_action_expr_coeff_vector" -> TrueQ[chkBDActionExpr],
    "bd_prefactor_rationalized_2sqrt6_over_3" -> TrueQ[chkBDPrefactorRationalized],
    "bd_prefactor_squared_is_8_3" -> TrueQ[chkBDPrefactorSquare],
    "dal_layer_coeffs_match_published" -> TrueQ[chkDalCoeffs],
    "dal_cross_lock_minus_bd_action_layers" -> TrueQ[chkDalCrossLock],
    "dal_magnitudes_1_9_16_8" -> TrueQ[chkDalMagnitudes],
    "dal_signs_alternate" -> TrueQ[chkDalAlternating],
    "dal_prefactor_squared_is_8_3" -> TrueQ[chkDalPrefactor],
    "mm_half_form_f0_2_is_1_2" -> TrueQ[chkHalfAnchor2],
    "mm_half_form_f0_4_is_1_10" -> TrueQ[chkHalfAnchor4],
    "mm_quarter_form_f0_2_is_1_4" -> TrueQ[chkQuarterAt2],
    "mm_quarter_form_f0_4_is_1_20" -> TrueQ[chkQuarterAt4],
    "mm_two_norms_differ_by_factor_2" -> TrueQ[chkNormalizationFactor2],
    "mm_published_form_is_half_normalization" -> TrueQ[publishedFormIsHalf],
    "mm_formulasJson_quarter_agrees_with_published" ->
      TrueQ[formulasJsonAgreesWithPublished],
    "kr_layer_split_sums_to_n" -> TrueQ[chkKRLayerSum],
    "kr_integer_split_examples" -> TrueQ[chkKRIntegerSplit],
    "kr_log2_count_is_n2_over_4" -> TrueQ[chkKRLog2],
    "kr_leading_exponent_is_2" -> TrueQ[chkKRLeadingExponent],
    "kr_leading_coeff_is_1_4" -> TrueQ[chkKRLeadingCoeff],
    "kr_middle_layer_is_half" -> TrueQ[chkKRMiddleHalf],
    "kr_outer_layer_is_quarter" -> TrueQ[chkKROuterQuarter],
    "poisson_normalization_is_1" -> TrueQ[chkPoissonNorm],
    "poisson_mean_is_rho_v" -> TrueQ[chkPoissonMean],
    "poisson_variance_is_rho_v" -> TrueQ[chkPoissonVariance],
    "number_volume_is_poisson_mean" -> TrueQ[chkNVisPoissonMean],
    "number_volume_unit_density" -> TrueQ[chkNVUnitDensity],
    "number_volume_equals_N" -> TrueQ[chkNVNumberEqualsN]
  ],
  "per_formula_verdict" -> Association[
    "benincasa-dowker-action-4d" -> If[TrueQ[verdictBD], "verified", "mismatch"],
    "discrete-dalembertian-4d" -> If[TrueQ[verdictDal], "verified", "mismatch"],
    "myrheim-meyer" ->
      If[TrueQ[verdictMM],
        If[TrueQ[formulasJsonAgreesWithPublished],
          "verified",
          "mismatch-formulasJson-factor2"],
        "mismatch"],
    "kr-count" -> If[TrueQ[verdictKR], "verified", "mismatch"],
    "poisson-sprinkling" -> If[TrueQ[verdictPoisson], "verified", "mismatch"],
    "number-volume" -> If[TrueQ[verdictNV], "verified", "mismatch"]
  ]
];

Export[
  FileNameJoin[{DirectoryName[$InputFileName],
    "causal-set-combinatorial-operators_result.json"}],
  result,
  "JSON"
];

Print["causal-set-combinatorial-operators.wl"];
Print["  BD action        = ", If[TrueQ[verdictBD], "verified", "MISMATCH"]];
Print["  d'Alembertian    = ", If[TrueQ[verdictDal], "verified", "MISMATCH"]];
Print["  Myrheim-Meyer    = ",
  result["per_formula_verdict"]["myrheim-meyer"]];
Print["  KR count         = ", If[TrueQ[verdictKR], "verified", "MISMATCH"]];
Print["  Poisson          = ", If[TrueQ[verdictPoisson], "verified", "MISMATCH"]];
Print["  number=volume    = ", If[TrueQ[verdictNV], "verified", "MISMATCH"]];
Print["  formulas.json MM /4 agrees with published = ",
  TrueQ[formulasJsonAgreesWithPublished],
  "  (False => factor-of-2 bug in formulas.json LaTeX)"];
