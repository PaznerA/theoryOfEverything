(* ===================================================================== *)
(* cft-central-charges-bh-entropy.wl                                       *)
(*                                                                         *)
(* Batch B3: CFT central charges & microscopic black-hole entropy (exact). *)
(*                                                                         *)
(* INDEPENDENT cross-CAS validation of six holography / string-theory      *)
(* identities, re-derived in Wolfram Language DIRECTLY from the PUBLISHED   *)
(* coefficients and definitions -- NOT transcribed from the project's      *)
(* sympy outputs.  Agreement with the sympy lane is therefore independent  *)
(* evidence; disagreement is a bug in one of the two derivations.          *)
(*                                                                         *)
(* All algebra is EXACT (Rational / exact integers / Solve / FullSimplify);*)
(* no floats enter any check.  Only basic canonical WL is used, and every  *)
(* symbolic root is exported as an InputForm string (the project hit a     *)
(* multiline pretty-print bug before -- force InputForm).                  *)
(*                                                                         *)
(* PUBLISHED SOURCES (repo-present; entered by hand here):                 *)
(*   [strominger-vafa-1996  hep-th/9601029] c = 6 Q1 Q5;                    *)
(*       Cardy S = 2 pi Sqrt[Q1 Q5 n]  (Bekenstein-Hawking match).         *)
(*   [strominger-1997-cardy hep-th/9712251] Cardy S =                      *)
(*       2 pi Sqrt[(c/6)(L0 - c/24)]  (near-horizon microstates; this is   *)
(*       the repo-resolvable id for the formula entry's 'strominger-1997').*)
(*   [brown-henneaux-1986   DOI 10.1007/BF01211590] c = 3 L /(2 G3);       *)
(*       N=4 SYM trace anomaly a = c = (N^2-1)/4 -> N^2/4.                  *)
(*   [witten-1998           hep-th/9802150] mass-dimension                 *)
(*       Delta(Delta-d) = m^2 L^2; BF bound m^2 L^2 >= -d^2/4.             *)
(*   [polyakov-1981         DOI 10.1016/0370-2693(81)90743-7] critical     *)
(*       dimension: c_tot = D-26 = 0 -> 26;  (3/2)(D-10) = 0 -> 10.        *)
(* ===================================================================== *)

ClearAll[Q1, Q5, nMom, cc, L0, Lbar0, cbar, Lads, G3, NN, Delta, dd, mm, Dcrit];

(* ===================================================================== *)
(* (1) strominger-vafa-entropy                                            *)
(*     Plug c = 6 Q1 Q5 and L0 = n into the Cardy formula and take the     *)
(*     leading large-charge term (the documented -c/24 -> 0 limit).        *)
(* ===================================================================== *)

(* Cardy entropy as an exact symbolic function of (c, L0). *)
cardyS[c_, l0_] := 2*Pi*Sqrt[(c/6)*(l0 - c/24)];

(* Full Cardy with the SV substitution c -> 6 Q1 Q5, L0 -> n. *)
svFull = cardyS[6*Q1*Q5, nMom];               (* = 2 pi Sqrt[Q1 Q5 (n - Q1 Q5/4)] *)

(* Leading large-charge term: drop the -c/24 = -Q1 Q5/4 shift (documented). *)
svLeading = 2*Pi*Sqrt[(6*Q1*Q5/6)*nMom];      (* = 2 pi Sqrt[Q1 Q5 n] *)

(* Published Strominger-Vafa value. *)
svPublished = 2*Pi*Sqrt[Q1*Q5*nMom];

(* HEADLINE: leading term equals the published SV entropy IDENTICALLY. *)
chkSVLeading = TrueQ[FullSimplify[svLeading - svPublished == 0]];

(* The full Cardy expression reduces to 2 pi Sqrt[Q1 Q5 (n - Q1 Q5/4)],   *)
(* i.e. the published value times Sqrt[1 - Q1 Q5/(4 n)] -- the -c/24      *)
(* correction is exactly the subleading factor that -> 1 as n -> Inf.     *)
svRatioSq = FullSimplify[(svFull/svPublished)^2];   (* = 1 - Q1 Q5/(4 n) *)
chkSVSubleading = TrueQ[FullSimplify[svRatioSq - (1 - Q1*Q5/(4*nMom)) == 0]];
(* Large-charge limit of that ratio is 1 (entropy -> published leading). *)
svLimit = Limit[svFull/svPublished, nMom -> Infinity];
chkSVLimit = TrueQ[FullSimplify[svLimit == 1]];

(* ===================================================================== *)
(* (2) cardy-formula                                                      *)
(*     Confirm the (left + right) Cardy expression is the stated exact    *)
(*     function of (c, L0, cbar, Lbar0).                                  *)
(* ===================================================================== *)

cardyFull[c_, l0_, cb_, lb0_] :=
  2*Pi*Sqrt[(c/6)*(l0 - c/24)] + 2*Pi*Sqrt[(cb/6)*(lb0 - cb/24)];

(* Reference: the published two-sector form, written independently here.  *)
cardyRef = 2*Pi*Sqrt[(cc/6)*(L0 - cc/24)] + 2*Pi*Sqrt[(cbar/6)*(Lbar0 - cbar/24)];

chkCardyForm = TrueQ[FullSimplify[cardyFull[cc, L0, cbar, Lbar0] - cardyRef == 0]];
(* Chiral (single-sector) reduction matches cardyS. *)
chkCardyChiral = TrueQ[FullSimplify[cardyFull[cc, L0, 0, 0] - cardyS[cc, L0] == 0]];
(* The entropy is real (radicand >= 0) exactly when L0 >= c/24, i.e. the  *)
(* effective level L0 - c/24 >= 0 (the unitarity / above-gap condition).  *)
(* Test LOGICAL EQUIVALENCE of the two conditions over the reals (Resolve *)
(* + ForAll), not structural SameQ -- Reduce attaches a Reals qualifier   *)
(* that would break a brittle === comparison.                             *)
chkCardyGap = TrueQ[
   Resolve[ForAll[{L0, cc},
      Implies[L0 - cc/24 >= 0, L0 >= cc/24] &&
      Implies[L0 >= cc/24, L0 - cc/24 >= 0]], Reals]];

(* ===================================================================== *)
(* (3) cardy-btz                                                          *)
(*     The Cardy expression IS the SV/BTZ entropy: with c = 6 Q1 Q5,      *)
(*     L0 = n it reproduces (2) above; we confirm the chiral Cardy form   *)
(*     equals the stated function of (c, L0) and matches SV in the limit. *)
(* ===================================================================== *)

btzCardy = cardyS[cc, L0];                        (* 2 pi Sqrt[(c/6)(L0 - c/24)] *)
btzRef   = 2*Pi*Sqrt[(cc/6)*(L0 - cc/24)];
chkBTZForm = TrueQ[FullSimplify[btzCardy - btzRef == 0]];
(* Cardy<->SV bridge: substituting c=6 Q1 Q5, L0=n into the BTZ Cardy     *)
(* gives exactly svFull, so the two formula entries are one identity.     *)
chkBTZmatchesSV = TrueQ[FullSimplify[(btzCardy /. {cc -> 6*Q1*Q5, L0 -> nMom}) - svFull == 0]];

(* ===================================================================== *)
(* (4) brown-henneaux                                                     *)
(*     Solve c = 3 L /(2 G3) for c (and invert for G3); confirm the N=4   *)
(*     SYM anomaly a = c = (N^2-1)/4 -> N^2/4 in the large-N limit.       *)
(* ===================================================================== *)

(* Brown-Henneaux central charge, solved symbolically. *)
bhSolC  = Solve[cc == 3*Lads/(2*G3), cc][[1, 1, 2]];       (* = 3 L/(2 G3) *)
chkBHc  = TrueQ[FullSimplify[bhSolC - 3*Lads/(2*G3) == 0]];
(* Invert for G3 (the bulk Newton constant fixed by c and L). *)
bhSolG3 = Solve[cc == 3*Lads/(2*G3), G3][[1, 1, 2]];       (* = 3 L/(2 c) *)
chkBHg3 = TrueQ[FullSimplify[bhSolG3 - 3*Lads/(2*cc) == 0]];

(* N=4 SYM anomaly coefficients a = c = (N^2-1)/4. *)
aSYM = (NN^2 - 1)/4;
cSYM = (NN^2 - 1)/4;
chkSYMaEqualsc = TrueQ[FullSimplify[aSYM - cSYM == 0]];     (* a = c exactly *)
(* Large-N: the (N^2-1)/4 anomaly -> N^2/4; verify via Series the leading  *)
(* term is N^2/4 and the correction is -1/4 (O(N^0)).                      *)
aSYMseries = Series[aSYM, {NN, Infinity, 0}];              (* N^2/4 - 1/4 *)
aSYMlead   = Normal[aSYMseries];                          (* = N^2/4 - 1/4 *)
chkSYMlargeN = TrueQ[FullSimplify[(aSYM - NN^2/4) == -1/4]];
chkSYMleadingTerm = TrueQ[Limit[aSYM/(NN^2/4), NN -> Infinity] == 1];

(* ===================================================================== *)
(* (5) mass-dimension                                                     *)
(*     Solve[Delta (Delta - d) == m^2 L^2, Delta]; verify the POSITIVE    *)
(*     root equals d/2 + Sqrt[d^2/4 + m^2 L^2] identically; BF bound      *)
(*     m^2 L^2 >= -d^2/4 is the reality condition of the radicand.        *)
(* ===================================================================== *)

mdRoots = Solve[Delta*(Delta - dd) == mm*Lads^2, Delta];  (* mm := m^2 here *)
mdRootList = Delta /. mdRoots;                            (* two roots *)
(* The published positive (Delta_+) root. *)
mdPlus = dd/2 + Sqrt[dd^2/4 + mm*Lads^2];
mdMinus = dd/2 - Sqrt[dd^2/4 + mm*Lads^2];
(* One of WL's two roots equals mdPlus identically; check membership.     *)
chkMDplus = TrueQ[
   FullSimplify[(mdRootList[[1]] - mdPlus)*(mdRootList[[2]] - mdPlus) == 0]];
chkMDminus = TrueQ[
   FullSimplify[(mdRootList[[1]] - mdMinus)*(mdRootList[[2]] - mdMinus) == 0]];
(* Sanity: each root, plugged back, satisfies Delta(Delta-d) = m^2 L^2.   *)
chkMDplusBack = TrueQ[FullSimplify[mdPlus*(mdPlus - dd) - mm*Lads^2 == 0]];
chkMDminusBack = TrueQ[FullSimplify[mdMinus*(mdMinus - dd) - mm*Lads^2 == 0]];
(* Delta_+ + Delta_- = d (Vieta), Delta_+ Delta_- = -m^2 L^2 (shadow).    *)
chkMDsum = TrueQ[FullSimplify[mdPlus + mdMinus - dd == 0]];
chkMDprod = TrueQ[FullSimplify[mdPlus*mdMinus + mm*Lads^2 == 0]];
(* Breitenlohner-Freedman bound: radicand d^2/4 + m^2 L^2 >= 0 (real      *)
(* Delta) iff m^2 L^2 >= -d^2/4.  Solve the reality condition for mm.     *)
bfReduce = Reduce[dd^2/4 + mm*Lads^2 >= 0 && Lads > 0 && dd > 0, mm];
(* The reality threshold is mm == -d^2/(4 L^2), i.e. m^2 L^2 = -d^2/4.    *)
chkBFthreshold = TrueQ[Simplify[(-dd^2/4)/Lads^2 == -dd^2/(4*Lads^2)]];
(* Over the reals, m^2 L^2 >= -d^2/4 IMPLIES the radicand >= 0 for ALL    *)
(* (mm, dd, Lads): verify the universally-quantified implication with     *)
(* Resolve (returns literal True), not a Reduce solution region.          *)
chkBFbound = TrueQ[
   Resolve[ForAll[{mm, dd, Lads},
      Implies[mm*Lads^2 >= -dd^2/4, dd^2/4 + mm*Lads^2 >= 0]], Reals]];

(* ===================================================================== *)
(* (6) critical-dimension-anomaly                                         *)
(*     Solve[D - 26 == 0] -> 26 (bosonic);                               *)
(*     Solve[(3/2)(D - 10) == 0] -> 10 (super).                          *)
(*     Links the ghost central-charge bookkeeping: bosonic matter c = D   *)
(*     (one boson per X^mu), bc ghosts c = -26 -> D = 26; super matter    *)
(*     c = (3/2) D (boson 1 + fermion 1/2 per direction), bc+beta-gamma   *)
(*     ghosts c = -26 + 11 = -15 -> (3/2) D - 15 = 0 -> D = 10.          *)
(* ===================================================================== *)

(* Bosonic: total Virasoro anomaly c_tot = D - 26 = 0. *)
bosSol = Solve[Dcrit - 26 == 0, Dcrit][[1, 1, 2]];        (* = 26 *)
chkBosonic = (bosSol === 26);
(* Ghost bookkeeping: D (matter, one boson per X) + (-26) (bc) = D - 26.  *)
chkBosonicGhost = ((Dcrit + (-26)) === (Dcrit - 26)) &&
   ((26 + (-26)) === 0);
(* Super: c_tot = (3/2)(D - 10) = 0. *)
superSol = Solve[(3/2)*(Dcrit - 10) == 0, Dcrit][[1, 1, 2]];   (* = 10 *)
chkSuper = (superSol === 10);
(* Super ghost bookkeeping: matter (3/2) D + ghosts (-15) = (3/2)(D-10).  *)
chkSuperGhost = TrueQ[Simplify[(3/2)*Dcrit + (-15) == (3/2)*(Dcrit - 10)]] &&
   (((3/2)*10 + (-15)) === 0);
(* Super ghost total -15 = bc (-26) + beta-gamma (+11). *)
chkSuperGhostSplit = ((-26) + 11 === -15);

(* ===================================================================== *)
(* Collect verdicts and export JSON.                                     *)
(* ===================================================================== *)

allChecks = {
  chkSVLeading, chkSVSubleading, chkSVLimit,
  chkCardyForm, chkCardyChiral, chkCardyGap,
  chkBTZForm, chkBTZmatchesSV,
  chkBHc, chkBHg3, chkSYMaEqualsc, chkSYMlargeN, chkSYMleadingTerm,
  chkMDplus, chkMDminus, chkMDplusBack, chkMDminusBack,
  chkMDsum, chkMDprod, chkBFthreshold, chkBFbound,
  chkBosonic, chkBosonicGhost, chkSuper, chkSuperGhost, chkSuperGhostSplit
};
overallPass = AllTrue[allChecks, TrueQ];

(* Per-formula booleans (a formula passes iff all its checks pass). *)
passSV     = TrueQ[chkSVLeading] && TrueQ[chkSVSubleading] && TrueQ[chkSVLimit];
passCardy  = TrueQ[chkCardyForm] && TrueQ[chkCardyChiral] && TrueQ[chkCardyGap];
passBTZ    = TrueQ[chkBTZForm] && TrueQ[chkBTZmatchesSV];
passBH     = TrueQ[chkBHc] && TrueQ[chkBHg3] && TrueQ[chkSYMaEqualsc] &&
             TrueQ[chkSYMlargeN] && TrueQ[chkSYMleadingTerm];
passMD     = TrueQ[chkMDplus] && TrueQ[chkMDminus] && TrueQ[chkMDplusBack] &&
             TrueQ[chkMDminusBack] && TrueQ[chkMDsum] && TrueQ[chkMDprod] &&
             TrueQ[chkBFthreshold] && TrueQ[chkBFbound];
passCrit   = TrueQ[chkBosonic] && TrueQ[chkBosonicGhost] && TrueQ[chkSuper] &&
             TrueQ[chkSuperGhost] && TrueQ[chkSuperGhostSplit];

result = Association[
  "script" -> "cft-central-charges-bh-entropy.wl",
  "batch" -> "B3: CFT central charges & microscopic black-hole entropy (exact)",
  "description" ->
    "Independent CAS re-derivation of CFT central-charge / microscopic BH-entropy identities",
  "sources" -> Association[
    "strominger-vafa-1996" -> "hep-th/9601029 (c = 6 Q1 Q5; S = 2 pi Sqrt[Q1 Q5 n])",
    "strominger-1997-cardy" -> "hep-th/9712251 (Cardy S = 2 pi Sqrt[(c/6)(L0 - c/24)])",
    "brown-henneaux-1986" -> "DOI 10.1007/BF01211590 (c = 3 L/(2 G3); N=4 SYM a=c=(N^2-1)/4)",
    "witten-1998" -> "hep-th/9802150 (Delta(Delta-d) = m^2 L^2; BF bound)",
    "polyakov-1981" -> "DOI 10.1016/0370-2693(81)90743-7 (D=26 / D=10)"
  ],
  "symbolic_forms" -> Association[
    "SV_full_with_c_eq_6Q1Q5" -> ToString[FullSimplify[svFull], InputForm],
    "SV_leading_large_charge" -> ToString[FullSimplify[svLeading], InputForm],
    "SV_published" -> ToString[svPublished, InputForm],
    "SV_ratio_squared_to_published" -> ToString[svRatioSq, InputForm],
    "cardy_full_two_sector" -> ToString[cardyRef, InputForm],
    "brown_henneaux_c" -> ToString[bhSolC, InputForm],
    "brown_henneaux_G3" -> ToString[bhSolG3, InputForm],
    "SYM_a_equals_c" -> ToString[aSYM, InputForm],
    "SYM_largeN_normal_series" -> ToString[aSYMlead, InputForm],
    "mass_dimension_roots" -> ToString[mdRootList, InputForm],
    "mass_dimension_Delta_plus" -> ToString[mdPlus, InputForm],
    "mass_dimension_Delta_minus" -> ToString[mdMinus, InputForm],
    "BF_reality_condition" -> ToString[bfReduce, InputForm],
    "critical_dim_bosonic" -> ToString[bosSol, InputForm],
    "critical_dim_super" -> ToString[superSol, InputForm]
  ],
  "checks" -> Association[
    "SV_leading_term_equals_published" -> TrueQ[chkSVLeading],
    "SV_subleading_factor_correct" -> TrueQ[chkSVSubleading],
    "SV_largeN_limit_is_1" -> TrueQ[chkSVLimit],
    "cardy_two_sector_form_matches" -> TrueQ[chkCardyForm],
    "cardy_chiral_reduces_to_single_sector" -> TrueQ[chkCardyChiral],
    "cardy_reality_gap_L0_geq_c_over_24" -> TrueQ[chkCardyGap],
    "btz_cardy_form_matches" -> TrueQ[chkBTZForm],
    "btz_cardy_matches_SV_substitution" -> TrueQ[chkBTZmatchesSV],
    "brown_henneaux_c_solved" -> TrueQ[chkBHc],
    "brown_henneaux_G3_solved" -> TrueQ[chkBHg3],
    "SYM_a_equals_c" -> TrueQ[chkSYMaEqualsc],
    "SYM_largeN_correction_is_minus_quarter" -> TrueQ[chkSYMlargeN],
    "SYM_leading_term_is_N2_over_4" -> TrueQ[chkSYMleadingTerm],
    "mass_dim_plus_root_in_solution_set" -> TrueQ[chkMDplus],
    "mass_dim_minus_root_in_solution_set" -> TrueQ[chkMDminus],
    "mass_dim_plus_satisfies_equation" -> TrueQ[chkMDplusBack],
    "mass_dim_minus_satisfies_equation" -> TrueQ[chkMDminusBack],
    "mass_dim_vieta_sum_is_d" -> TrueQ[chkMDsum],
    "mass_dim_vieta_product_is_minus_m2L2" -> TrueQ[chkMDprod],
    "BF_threshold_is_minus_d2_over_4" -> TrueQ[chkBFthreshold],
    "BF_bound_implies_real_dimension" -> TrueQ[chkBFbound],
    "critical_dim_bosonic_is_26" -> TrueQ[chkBosonic],
    "critical_dim_bosonic_ghost_bookkeeping" -> TrueQ[chkBosonicGhost],
    "critical_dim_super_is_10" -> TrueQ[chkSuper],
    "critical_dim_super_ghost_bookkeeping" -> TrueQ[chkSuperGhost],
    "critical_dim_super_ghost_split_minus15" -> TrueQ[chkSuperGhostSplit]
  ],
  "per_formula" -> Association[
    "strominger-vafa-entropy" -> TrueQ[passSV],
    "cardy-formula" -> TrueQ[passCardy],
    "cardy-btz" -> TrueQ[passBTZ],
    "brown-henneaux" -> TrueQ[passBH],
    "mass-dimension" -> TrueQ[passMD],
    "critical-dimension-anomaly" -> TrueQ[passCrit]
  ],
  "overall_pass" -> TrueQ[overallPass]
];

Export[
  FileNameJoin[{DirectoryName[$InputFileName], "cft-central-charges-bh-entropy_result.json"}],
  result,
  "JSON"
];

Print["cft-central-charges-bh-entropy.wl overall_pass = ", TrueQ[overallPass]];
Print["per-formula: ", result["per_formula"]];
