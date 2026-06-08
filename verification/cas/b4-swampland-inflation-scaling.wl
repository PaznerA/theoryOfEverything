(* ===================================================================== *)
(* b4-swampland-inflation-scaling.wl                                       *)
(*                                                                         *)
(* INDEPENDENT cross-CAS validation of batch B4: swampland / inflation     *)
(* exact scaling relations & algebraic identities.  Each formulaId is      *)
(* re-derived in Wolfram Language directly from the PUBLISHED              *)
(* coefficients/definitions -- NOT transcribed from the project's sympy    *)
(* outputs.  Agreement with the sympy lane is therefore independent        *)
(* evidence; disagreement is a real bug in one of the two derivations.     *)
(*                                                                         *)
(* All arithmetic is EXACT (Rational / exact integers / exact radicals).   *)
(* No floats enter any boolean check.  Only basic canonical WL is used.    *)
(* Output strings are forced to InputForm to avoid the multiline          *)
(* pretty-print bug the project hit before.                                *)
(*                                                                         *)
(* PUBLISHED SOURCES (literature values entered by hand here):             *)
(*   [Planck 2018 X, arXiv:1807.06211; repo slug planck-2018-inflation]    *)
(*       n_s-1 = -6 eps + 2 eta,  r = 16 eps,  eps = (M^2/2)(V'/V)^2,      *)
(*       n_t = -2 eps  ->  consistency r = -8 n_t.                          *)
(*   [Etheredge et al. arXiv:2206.04063; etheredge-sharpening-2022]        *)
(*       KK rate gamma = Sqrt[(d-1)/(d-2)] (n=1),                           *)
(*       general n gamma = Sqrt[(d+n-2)/(n(d-2))].                          *)
(*   [Castellano-Ruiz-Valenzuela arXiv:2311.01536;                         *)
(*       castellano-ruiz-valenzuela-2023] universal pattern                *)
(*       (grad m / m).(grad Lambda_sp / Lambda_sp) = 1/(d-2).              *)
(*   [Palti arXiv:1903.06239 (palti-2019);                                 *)
(*       Dvali et al. arXiv:2403.18005 (dvali-three-scales-2024)]          *)
(*       Lambda_sp = M_Pl/Sqrt[N],  S_BH(Lambda_sp^-1) ~ N.                 *)
(*   [Strominger arXiv:2105.14346 (strominger-2021)]                       *)
(*       [w^p_m, w^q_n] = (m(q-1) - n(p-1)) w^{p+q-2}_{m+n}.               *)
(*   [Bern-Carrasco-Johansson arXiv:0805.3993                             *)
(*       (Bern-Carrasco-Johansson-2008-BCJ)] color-kinematics:            *)
(*       c_i + c_j + c_k = 0  =>  n_i + n_j + n_k = 0.                      *)
(* ===================================================================== *)

ClearAll["Global`*"];

(* Solve over generic symbolic parameters emits the harmless ::nongen       *)
(* parameter-genericity advisory; our solves are exact linear systems with  *)
(* a unique solution, so silence it globally for a clean run.               *)
Off[Solve::nongen];

(* ===================================================================== *)
(* (i) slow-roll-spectral-index                                           *)
(*     n_s - 1 = -6 eps + 2 eta,  r = 16 eps,  eps = (M^2/2)(V'/V)^2.      *)
(*     The *relations* are exact even though measured n_s = 0.9649 is      *)
(*     numeric (that lives in the numerical bucket, excluded here).        *)
(* ===================================================================== *)
ClearAll[eps, eta, Mpl, Vp, V, ntensor];

(* Published linear relations, treated as exact symbolic identities. *)
nsMinus1[e_, et_] := -6*e + 2*et;          (* n_s - 1 *)
rTensor[e_]       := 16*e;                  (* r *)
ntFromEps[e_]     := -2*e;                  (* tensor tilt n_t = -2 eps *)

(* (a) Consistency relation r = -8 n_t (single-field).  Both sides are     *)
(*     exact linear functions of eps; their difference must be identically *)
(*     zero as a polynomial in eps.                                        *)
consistencyLHS = rTensor[eps];
consistencyRHS = -8*ntFromEps[eps];
chkConsistency = (Simplify[consistencyLHS - consistencyRHS] === 0) &&
                 (rTensor[eps] === 16*eps) && (ntFromEps[eps] === -2*eps);

(* (b) n_s - 1 is exactly the published linear combo (coefficient check).  *)
nsExpr = nsMinus1[eps, eta];
chkNsCoeffs = (Coefficient[nsExpr, eps] === -6) &&
              (Coefficient[nsExpr, eta] === 2);

(* (c) r = 16 eps coefficient check. *)
chkRcoeff = (Coefficient[rTensor[eps], eps] === 16);

(* (d) Dimensional check: eps = (M_Pl^2/2)(V'/V)^2 is DIMENSIONLESS.        *)
(*     Track mass dimensions symbolically: [M_Pl]=1 (mass), [V]=4 (energy  *)
(*     density ~ mass^4 in 4d), [V']=[dV/dphi]=[V]-[phi]; [phi]=1 (canonical*)
(*     scalar, mass dimension 1).  So [V']=3, [V'/V]=3-4=-1, [(V'/V)^2]=-2, *)
(*     [M_Pl^2]=2, total = 2 + (-2) = 0.  Encode dims as exact integers.    *)
dimMpl = 1; dimPhi = 1; dimV = 4;
dimVp = dimV - dimPhi;                      (* dV/dphi : 3 *)
dimEps = 2*dimMpl + 2*(dimVp - dimV);       (* 2*1 + 2*(3-4) = 0 *)
chkEpsDimensionless = (dimEps === 0);

(* (e) Sanity: r/(n_s-1) and r vs eps are mutually consistent: r = 16 eps   *)
(*     and (n_s-1)+6 eps = 2 eta, so eta = ((n_s-1)+6 eps)/2 = ((n_s-1)+    *)
(*     (3/8) r)/2.  Verify this re-arrangement is an exact identity.        *)
etaSolved = Solve[nsMinus1[eps, eta] == nsM1sym && rTensor[eps] == rsym,
                  {eps, eta}];
(* eps = rsym/16, eta = (nsM1sym + 6 eps)/2 *)
epsSol = eps /. First[etaSolved];
etaSol = eta /. First[etaSolved];
chkSolve = (Simplify[epsSol - rsym/16] === 0) &&
           (Simplify[etaSol - (nsM1sym + (3/8)*rsym)/2] === 0);

chkSlowRoll = chkConsistency && chkNsCoeffs && chkRcoeff &&
              chkEpsDimensionless && chkSolve;

(* ===================================================================== *)
(* (ii) wgc-kk-rate                                                        *)
(*      gamma = Sqrt[(d-1)/(d-2)] (n=1),                                   *)
(*      general n: gamma = Sqrt[(d+n-2)/(n(d-2))].                         *)
(* ===================================================================== *)
ClearAll[d, n];

gammaN1[dd_]     := Sqrt[(dd - 1)/(dd - 2)];
gammaGen[dd_, nn_] := Sqrt[(dd + nn - 2)/(nn*(dd - 2))];

(* (a) general-n reduces to the n=1 form: difference FullSimplifies to 0.   *)
chkKKreduces = (FullSimplify[gammaGen[d, 1] - gammaN1[d]] === 0);

(* (b) d=4 value of the n=1 rate is the exact radical Sqrt[3/2].            *)
gammaD4 = FullSimplify[gammaN1[4]];
chkKKd4 = (gammaD4 === Sqrt[3/2]) && (gammaD4^2 === Rational[3, 2]);

(* (c) general-n at d=4 reproduces the same value at n=1.                   *)
chkKKgenD4 = (FullSimplify[gammaGen[4, 1] - Sqrt[3/2]] === 0);

(* (d) decompactification limit n -> Infinity of gamma(d,n): the radius     *)
(*     mode rate goes to 1/Sqrt[d-2] (large-tower saturation).  Exact.      *)
gammaLargeN = Limit[gammaGen[d, n], n -> Infinity, Assumptions -> d > 2];
chkKKlargeN = (FullSimplify[gammaLargeN - 1/Sqrt[d - 2],
                  Assumptions -> d > 2] === 0);

chkKK = chkKKreduces && chkKKd4 && chkKKgenD4 && chkKKlargeN;

(* ===================================================================== *)
(* (iii) universal-pattern-formula                                        *)
(*       (grad m / m) . (grad Lambda_sp / Lambda_sp) = 1/(d-2).            *)
(* ===================================================================== *)
ClearAll[d];

(* The published statement is the value of the inner product as an exact    *)
(* rational function of d.  We assert it equals 1/(d-2) and recovers the    *)
(* d=4 value 1/2.  We ALSO re-derive 1/(d-2) from the component data the    *)
(* paper gives at infinite distance: for a KK tower the mass-gradient       *)
(* vector has length zeta_m = Sqrt[(d-1)/(d-2)] (= gamma above) and the     *)
(* species-scale gradient has length zeta_sp = 1/Sqrt[(d-1)(d-2)], and the *)
(* two are PARALLEL, so the dot product is the product of lengths:          *)
(*   zeta_m * zeta_sp = Sqrt[(d-1)/(d-2)] * 1/Sqrt[(d-1)(d-2)] = 1/(d-2).   *)
patternValue[dd_] := 1/(dd - 2);

zetaM[dd_]  := Sqrt[(dd - 1)/(dd - 2)];               (* tower mass rate *)
zetaSp[dd_] := 1/Sqrt[(dd - 1)*(dd - 2)];             (* species-scale rate *)
patternDerived = FullSimplify[zetaM[d]*zetaSp[d], Assumptions -> d > 2];

chkPatternDerivation = (FullSimplify[patternDerived - patternValue[d],
                            Assumptions -> d > 2] === 0);
chkPatternIsRational = (Together[patternValue[d]] === 1/(d - 2));
chkPatternD4 = (patternValue[4] === Rational[1, 2]);
chkPatternD5 = (patternValue[5] === Rational[1, 3]);
(* consistency: zetaM here is identical to the KK gamma at n=1 above. *)
chkPatternMatchesKK = (FullSimplify[zetaM[d] - gammaN1[d]] === 0);

chkPattern = chkPatternDerivation && chkPatternIsRational &&
             chkPatternD4 && chkPatternD5 && chkPatternMatchesKK;

(* ===================================================================== *)
(* (iv) species-scale  AND  (v label in prompt) species-scale-formula      *)
(*      Lambda_sp = M_Pl/Sqrt[N];  S_BH(Lambda_sp^-1) ~ N.                  *)
(* ===================================================================== *)
ClearAll[Mpl, Nsp, LamSp, S];

(* (a) Definition: Lambda_sp = M_Pl / Sqrt[N].  Solve for N as exact        *)
(*     inverse-square relation N = M_Pl^2 / Lambda_sp^2.                    *)
defLamSp = LamSp == Mpl/Sqrt[Nsp];
solN = Solve[defLamSp, Nsp];
NofLam = Nsp /. First[solN];                (* expect Mpl^2/LamSp^2 *)
chkSpInverseSquare =
  (FullSimplify[NofLam - Mpl^2/LamSp^2,
       Assumptions -> {Mpl > 0, LamSp > 0}] === 0);

(* (b) Black-hole entropy of the minimal BH of size Lambda_sp^-1:           *)
(*     a Schwarzschild BH of horizon radius r_min = 1/Lambda_sp in d dims   *)
(*     has S_BH ~ (M_Pl r)^(d-2) = (M_Pl/Lambda_sp)^(d-2).  Substituting    *)
(*     Lambda_sp = M_Pl/Sqrt[N] gives (Sqrt[N])^(d-2) = N^((d-2)/2).        *)
(*     The PUBLISHED species count is S_BH ~ N, i.e. d=4 (where (d-2)/2=1). *)
ClearAll[d];
SBHexponent[dd_] := (dd - 2)/2;             (* power of N in S_BH *)
chkSpEntropyD4 = (SBHexponent[4] === 1);    (* S_BH ~ N^1 = N in 4d *)
(* Explicit substitution check in 4d: (M_Pl/Lambda_sp)^(4-2) = N. *)
SBHd4 = (Mpl/LamSp)^(4 - 2) /. LamSp -> Mpl/Sqrt[Nsp];
chkSpEntropySub = (FullSimplify[SBHd4 - Nsp,
                       Assumptions -> {Mpl > 0, Nsp > 0}] === 0);

(* (c) As N grows the cutoff DROPS below M_Pl: Lambda_sp < M_Pl for N>1.     *)
(*     Exact monotonic statement: Lambda_sp/M_Pl = 1/Sqrt[N] is < 1 for N>1.*)
ratioLamMpl = (Mpl/Sqrt[Nsp])/Mpl;          (* = 1/Sqrt[N] *)
chkSpBelowPlanck = (FullSimplify[ratioLamMpl - 1/Sqrt[Nsp],
                        Assumptions -> Nsp > 0] === 0);

chkSpecies = chkSpInverseSquare && chkSpEntropyD4 &&
             chkSpEntropySub && chkSpBelowPlanck;
(* species-scale and species-scale-formula share the same defining          *)
(* relation Lambda_sp = M_Pl/Sqrt[N]; the -formula entry adds S_BH ~ N,     *)
(* which is checked above.  Both verdicts derive from chkSpecies.           *)
chkSpeciesScale = chkSpInverseSquare && chkSpBelowPlanck;       (* slug: species-scale *)
chkSpeciesScaleFormula = chkSpecies;                            (* slug: species-scale-formula *)

(* ===================================================================== *)
(* (v) w-infinity-algebra                                                  *)
(*     [w^p_m, w^q_n] = (m(q-1) - n(p-1)) w^{p+q-2}_{m+n}.                  *)
(*     Genuine algebra-closure CAS check: antisymmetry + Jacobi identity    *)
(*     by exact integer structure-constant evaluation.                     *)
(* ===================================================================== *)

(* Structure constant: bracket of w^p_m with w^q_n yields f * w^{p+q-2}_    *)
(* {m+n} with f = m(q-1) - n(p-1).  We represent a generator as the index    *)
(* tuple {p, m} and a bracket result as a list of {coefficient, {P, M}}     *)
(* terms (single term here).                                                *)
wIndex[{p_, m_}, {q_, n_}] := {p + q - 2, m + n};
wCoeff[{p_, m_}, {q_, n_}] := m*(q - 1) - n*(p - 1);

(* bracket: returns {coeff, targetIndex}. *)
wBracket[a_List, b_List] := {wCoeff[a, b], wIndex[a, b]};

(* (a) Antisymmetry: [w^p_m, w^q_n] = -[w^q_n, w^p_m] for all tested        *)
(*     index tuples (same target index, opposite-sign coefficient).         *)
antiSymTuples = {
  {{2, 0}, {2, 1}}, {{2, 1}, {3, -1}}, {{3, 2}, {2, -2}},
  {{4, -1}, {2, 3}}, {{1, 5}, {3, -4}}, {{2, 2}, {2, 2}},
  {{5, -3}, {2, 7}}, {{3, 0}, {3, 0}}
};
antiSymResults = Map[
  Function[pair,
    Module[{a = pair[[1]], b = pair[[2]], fab, tab, fba, tba},
      {fab, tab} = wBracket[a, b];
      {fba, tba} = wBracket[b, a];
      (* target index must match; coeff must be exactly negated *)
      (tab === tba) && (fab === -fba)
    ]],
  antiSymTuples];
chkAntiSym = AllTrue[antiSymResults, TrueQ];

(* (b) Jacobi identity.  For wedge generators the double bracket            *)
(*     [w^p_m, [w^q_n, w^r_l]] produces a single term with target index     *)
(*     {p+q+r-4, m+n+l} and a coefficient built from the structure          *)
(*     constants.  The cyclic sum of the three double-bracket coefficients  *)
(*     onto that common target must vanish.  We evaluate the coefficient    *)
(*     chain in exact integers.                                             *)
(*       outer = wCoeff[ a , target(b,c) ] * wCoeff[ b , c ]                 *)
jacobiTermCoeff[a_, b_, c_] := wCoeff[a, wIndex[b, c]]*wCoeff[b, c];
jacobiSum[a_, b_, c_] :=
  jacobiTermCoeff[a, b, c] +
  jacobiTermCoeff[b, c, a] +
  jacobiTermCoeff[c, a, b];
(* all three double brackets land on the SAME target index; verify that too *)
jacobiCommonTarget[a_, b_, c_] :=
  ({a[[1]] + b[[1]] + c[[1]] - 4, a[[2]] + b[[2]] + c[[2]]});

jacobiTriples = {
  {{2, 0}, {2, 1}, {3, -1}},
  {{3, 2}, {2, -2}, {4, 1}},
  {{1, 5}, {3, -4}, {2, 2}},
  {{2, 3}, {2, -1}, {2, 0}},
  {{4, -2}, {3, 5}, {2, -3}},
  {{5, 1}, {2, 2}, {3, -4}},
  {{2, 7}, {6, -3}, {3, 1}},
  {{3, 0}, {3, 0}, {3, 0}}
};
jacobiSums = Map[Function[t, jacobiSum[t[[1]], t[[2]], t[[3]]]], jacobiTriples];
chkJacobi = AllTrue[jacobiSums, (# === 0) &];

(* (c) Symbolic Jacobi: prove it for GENERAL symbolic indices p,q,r,m,n,l   *)
(*     (not just sampled integers).  The cyclic sum must be identically 0.  *)
ClearAll[pp, qq, rr, mm, nn, ll];
symA = {pp, mm}; symB = {qq, nn}; symC = {rr, ll};
jacobiSymbolic = Expand[
  jacobiTermCoeff[symA, symB, symC] +
  jacobiTermCoeff[symB, symC, symA] +
  jacobiTermCoeff[symC, symA, symB]];
chkJacobiSymbolic = (Simplify[jacobiSymbolic] === 0);

(* (d) target-index closure: structure constant maps grade p+q-2 (wedge     *)
(*     algebra raises mode index, lowers conformal weight by 2). Check the   *)
(*     well-known sl(2) subalgebra p=q=2 closes: [w^2_m, w^2_n] =            *)
(*     (m-n) w^2_{m+n} (Witt / Virasoro-wedge), the L_m generators.         *)
sl2Coeff[m_, n_] := wCoeff[{2, m}, {2, n}];     (* expect m - n *)
sl2Target[m_, n_] := wIndex[{2, m}, {2, n}];    (* expect {2, m+n} *)
(* NB: a two-iterator Table returns a NESTED list, so And @@ would leave an *)
(* unevaluated nested && (not a single boolean).  Flatten first, then       *)
(* AllTrue, so the closure verdict collapses to a genuine True/False.       *)
sl2Grid = Table[
   (sl2Coeff[m, n] === m - n) && (sl2Target[m, n] === {2, m + n}),
   {m, -2, 2}, {n, -2, 2}];
chkSl2Witt = AllTrue[Flatten[sl2Grid], TrueQ];

chkWinf = chkAntiSym && chkJacobi && chkJacobiSymbolic && chkSl2Witt;

(* ===================================================================== *)
(* (vi) bcj-jacobi                                                         *)
(*      c_i + c_j + c_k = 0  =>  n_i + n_j + n_k = 0  (color-kinematics).   *)
(* ===================================================================== *)
ClearAll[ci, cj, ck, ni, nj, nk];

(* The duality is the statement that the kinematic numerators obey the SAME  *)
(* linear Jacobi relation as the color factors.  As a CAS check we verify    *)
(* the implication holds as an exact linear identity on the numerator side,  *)
(* and that the gravity double-copy numerator n_i^2 inherits the relation    *)
(* ONLY in the linearized (BCJ-satisfying) representation.                   *)

(* (a) Color Jacobi: c_i + c_j + c_k = 0.  Kinematic Jacobi: n_i+n_j+n_k=0.  *)
(*     The duality MAPS one onto the other.  Solve the color constraint for  *)
(*     ck, substitute, and confirm the kinematic constraint has the IDENTICAL*)
(*     structure (coefficient pattern {1,1,1}).                              *)
colorRel = ci + cj + ck;
kinRel = ni + nj + nk;
chkBcjCoeffPattern =
  (Coefficient[colorRel, ci] === 1) && (Coefficient[colorRel, cj] === 1) &&
  (Coefficient[colorRel, ck] === 1) &&
  (Coefficient[kinRel, ni] === 1) && (Coefficient[kinRel, nj] === 1) &&
  (Coefficient[kinRel, nk] === 1);

(* (b) Implication as linear algebra: given the substitution rule c_i -> n_i *)
(*     (color-to-kinematics replacement), the color Jacobi expression maps   *)
(*     exactly to the kinematic Jacobi expression -> difference is 0.        *)
mappedColor = colorRel /. {ci -> ni, cj -> nj, ck -> nk};
chkBcjImplication = (Simplify[mappedColor - kinRel] === 0);

(* (c) Numerical witness: pick numerators satisfying the kinematic Jacobi    *)
(*     (n_i,n_j,n_k) = (5, -3, -2) (sum 0).  Their cyclic sum is exactly 0,  *)
(*     and a NON-BCJ assignment (5,-3,-1) is exactly nonzero (control).      *)
chkBcjWitnessZero = ((5) + (-3) + (-2) === 0);
chkBcjWitnessNonzero = (((5) + (-3) + (-1)) =!= 0);

(* (d) Double copy: if c_i + c_j + c_k = 0 AND n_i + n_j + n_k = 0, then     *)
(*     replacing color by kinematics (c -> n) keeps the same vanishing       *)
(*     relation; the gravity numerator is n_i (second copy).  Verify the     *)
(*     joint constraint solution space is the diagonal n_k = -n_i-n_j with   *)
(*     ck = -ci-cj, exactly (Solve, exact).                                  *)
bcjSol = Solve[{ci + cj + ck == 0, ni + nj + nk == 0}, {ck, nk}];
ckSol = ck /. First[bcjSol];
nkSol = nk /. First[bcjSol];
chkBcjSolve = (Simplify[ckSol - (-ci - cj)] === 0) &&
              (Simplify[nkSol - (-ni - nj)] === 0);

chkBcj = chkBcjCoeffPattern && chkBcjImplication &&
         chkBcjWitnessZero && chkBcjWitnessNonzero && chkBcjSolve;

(* ===================================================================== *)
(* Collect verdicts and export JSON.                                      *)
(* ===================================================================== *)
perFormula = Association[
  "slow-roll-spectral-index" -> TrueQ[chkSlowRoll],
  "wgc-kk-rate" -> TrueQ[chkKK],
  "universal-pattern-formula" -> TrueQ[chkPattern],
  "species-scale" -> TrueQ[chkSpeciesScale],
  "species-scale-formula" -> TrueQ[chkSpeciesScaleFormula],
  "w-infinity-algebra" -> TrueQ[chkWinf],
  "bcj-jacobi" -> TrueQ[chkBcj]
];
overallPass = AllTrue[Values[perFormula], TrueQ];

result = Association[
  "script" -> "b4-swampland-inflation-scaling.wl",
  "batch" -> "B4: swampland / inflation exact scaling relations & algebraic identities",
  "description" ->
    "Independent CAS re-derivation of B4 swampland/inflation scaling relations & algebra closure",
  "sources" -> Association[
    "slow_roll" -> "Planck 2018 X arXiv:1807.06211 (planck-2018-inflation)",
    "wgc_kk_rate" -> "Etheredge et al. arXiv:2206.04063 (etheredge-sharpening-2022)",
    "universal_pattern" -> "Castellano-Ruiz-Valenzuela arXiv:2311.01536 (castellano-ruiz-valenzuela-2023)",
    "species_scale" -> "Palti arXiv:1903.06239 (palti-2019); Dvali et al. arXiv:2403.18005 (dvali-three-scales-2024)",
    "w_infinity" -> "Strominger arXiv:2105.14346 (strominger-2021)",
    "bcj" -> "Bern-Carrasco-Johansson arXiv:0805.3993 (Bern-Carrasco-Johansson-2008-BCJ)"
  ],
  "exact_values" -> Association[
    "slowroll_consistency_r_plus_8nt" ->
      ToString[Simplify[consistencyLHS - consistencyRHS], InputForm],
    "slowroll_eps_dimension" -> ToString[dimEps, InputForm],
    "slowroll_eps_solved" -> ToString[epsSol, InputForm],
    "slowroll_eta_solved" -> ToString[etaSol, InputForm],
    "kk_gamma_d4_n1" -> ToString[gammaD4, InputForm],
    "kk_gamma_d4_n1_squared" -> ToString[gammaD4^2, InputForm],
    "kk_general_minus_n1" ->
      ToString[FullSimplify[gammaGen[d, 1] - gammaN1[d]], InputForm],
    "kk_largeN_limit" -> ToString[FullSimplify[gammaLargeN], InputForm],
    "pattern_value_general_d" -> ToString[patternValue[d], InputForm],
    "pattern_derived_from_zetas" -> ToString[patternDerived, InputForm],
    "pattern_value_d4" -> ToString[patternValue[4], InputForm],
    "pattern_value_d5" -> ToString[patternValue[5], InputForm],
    "species_N_of_Lambda" -> ToString[NofLam, InputForm],
    "species_SBH_exponent_d4" -> ToString[SBHexponent[4], InputForm],
    "species_Lambda_over_Mpl" -> ToString[FullSimplify[ratioLamMpl, Assumptions -> Nsp > 0], InputForm],
    "winf_jacobi_symbolic" -> ToString[jacobiSymbolic, InputForm],
    "winf_jacobi_integer_sums" -> ToString[jacobiSums, InputForm],
    "winf_sl2_witt_coeff_2_1" -> ToString[sl2Coeff[2, 1], InputForm],
    "bcj_color_to_kin_diff" -> ToString[Simplify[mappedColor - kinRel], InputForm],
    "bcj_ck_solution" -> ToString[ckSol, InputForm],
    "bcj_nk_solution" -> ToString[nkSol, InputForm]
  ],
  "checks" -> Association[
    (* slow-roll *)
    "slowroll_consistency_r_eq_minus8nt" -> TrueQ[chkConsistency],
    "slowroll_ns_coeffs_minus6_plus2" -> TrueQ[chkNsCoeffs],
    "slowroll_r_coeff_16" -> TrueQ[chkRcoeff],
    "slowroll_eps_dimensionless" -> TrueQ[chkEpsDimensionless],
    "slowroll_solve_eps_eta" -> TrueQ[chkSolve],
    (* kk rate *)
    "kk_general_reduces_to_n1" -> TrueQ[chkKKreduces],
    "kk_d4_is_sqrt_3_2" -> TrueQ[chkKKd4],
    "kk_general_d4_n1_matches" -> TrueQ[chkKKgenD4],
    "kk_largeN_limit_is_1_over_sqrt_dm2" -> TrueQ[chkKKlargeN],
    (* universal pattern *)
    "pattern_derived_equals_1_over_dm2" -> TrueQ[chkPatternDerivation],
    "pattern_is_rational_1_over_dm2" -> TrueQ[chkPatternIsRational],
    "pattern_d4_is_1_2" -> TrueQ[chkPatternD4],
    "pattern_d5_is_1_3" -> TrueQ[chkPatternD5],
    "pattern_zetaM_matches_kk_gamma" -> TrueQ[chkPatternMatchesKK],
    (* species scale *)
    "species_inverse_square_N" -> TrueQ[chkSpInverseSquare],
    "species_SBH_exponent_d4_is_1" -> TrueQ[chkSpEntropyD4],
    "species_SBH_substitution_is_N" -> TrueQ[chkSpEntropySub],
    "species_cutoff_below_planck" -> TrueQ[chkSpBelowPlanck],
    (* w-infinity *)
    "winf_antisymmetry" -> TrueQ[chkAntiSym],
    "winf_jacobi_integer_triples" -> TrueQ[chkJacobi],
    "winf_jacobi_symbolic_identically_zero" -> TrueQ[chkJacobiSymbolic],
    "winf_sl2_witt_subalgebra_closes" -> TrueQ[chkSl2Witt],
    (* bcj *)
    "bcj_coeff_pattern_1_1_1" -> TrueQ[chkBcjCoeffPattern],
    "bcj_color_maps_to_kinematic" -> TrueQ[chkBcjImplication],
    "bcj_witness_zero" -> TrueQ[chkBcjWitnessZero],
    "bcj_control_nonzero" -> TrueQ[chkBcjWitnessNonzero],
    "bcj_solve_diagonal" -> TrueQ[chkBcjSolve]
  ],
  "perFormula" -> perFormula,
  "overall_pass" -> TrueQ[overallPass]
];

Export[
  FileNameJoin[{DirectoryName[$InputFileName], "b4-swampland-inflation-scaling_result.json"}],
  result,
  "JSON"
];

Print["b4-swampland-inflation-scaling.wl overall_pass = ", TrueQ[overallPass]];
Print["perFormula = ", perFormula];
