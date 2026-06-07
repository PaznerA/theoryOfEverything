(* ===================================================================== *)
(* ds_classifier.wl                                                        *)
(*                                                                         *)
(* INDEPENDENT cross-CAS validation of the d_s master values of            *)
(* draft-03-ds-classifier, re-derived in Wolfram Language from the two     *)
(* PUBLISHED closed-form limits (NOT transcribed from the project's        *)
(* numerical engine outputs).  The numerical engine (calc.py) integrates   *)
(* return probabilities; here we re-check the EXACT rational limits that    *)
(* those integrals must converge to, so the two lanes are independent.     *)
(*                                                                         *)
(* TWO MASTER FORMULAE:                                                     *)
(*   (A) isotropic   d_s^UV = D / gamma        for F(k) ~ k^(2 gamma).      *)
(*   (B) anisotropic d_s    = 1 + D_space / z  (Horava-Lifshitz).          *)
(*                                                                         *)
(* CONVENTION (draft-03 sec.5.1 table note):  D denotes the SPACETIME      *)
(* dimension throughout (D = 4).  Isotropic rows use D = 4 in D/gamma.      *)
(* Horava rows use D_space = D - 1 = 3 in 1 + D_space/z.  This matches      *)
(* Horava arXiv:0902.3657 (3+1 spacetime; headline z=3 -> d_s=2).          *)
(*                                                                         *)
(* SOURCES:                                                                 *)
(*   Horava arXiv:0902.3657              (1 + D_space/z)                    *)
(*   Stelle; Calcagni et al. 1408.0199   (UV d_s = 2)                       *)
(*   Lauscher-Reuter hep-th/0508202,                                       *)
(*       Reuter-Saueressig 1110.5224     (AS: eta=-2 -> 1/p^4 -> d_s=2)     *)
(*   Belenchia et al. 1507.00330         (causal-set d'Alembertian d_s=2)   *)
(*   Calcagni 1304.2709                  (multifractional UV pick d_s=2)    *)
(* ===================================================================== *)

(* --------------------------------------------------------------------- *)
(* 0. Convention constants (exact integers).                              *)
(* --------------------------------------------------------------------- *)
dSpacetime = 4;                 (* D : spacetime dimension *)
dSpace = dSpacetime - 1;        (* D_space = 3 (spatial dims, Horava) *)

(* --------------------------------------------------------------------- *)
(* 1. Master formulae as exact rational functions.                        *)
(* --------------------------------------------------------------------- *)
dsIsotropic[d_, gamma_] := Rational[1, 1]*d/gamma;   (* d_s^UV = D/gamma *)
dsHorava[dsp_, z_] := 1 + dsp/z;                     (* d_s = 1 + D_space/z *)

(* --------------------------------------------------------------------- *)
(* 2. The ~6 exact rational master entries from the results.json table.   *)
(*    Each is recomputed from the closed form, then compared to the        *)
(*    published exact value (entered here by hand from the literature).    *)
(* --------------------------------------------------------------------- *)

(* (a) GR : isotropic, gamma = 1 -> d_s = D = 4 (UV = IR, no flow). *)
dsGR = dsIsotropic[dSpacetime, 1];
chkGR = (dsGR == 4);

(* (b) Stelle quadratic gravity : UV F ~ k^4 -> gamma = 2 -> d_s = D/2 = 2. *)
dsStelle = dsIsotropic[dSpacetime, 2];
chkStelle = (dsStelle == 2);

(* (c) Asymptotic Safety : eta_* = 2 - D = -2 -> UV propagator 1/p^4 ->     *)
(*     effective gamma = 2 -> d_s = D/2 = 2. *)
etaStar = 2 - dSpacetime;            (* = -2 *)
gammaAS = 1 - etaStar/2;             (* = 2 *)
dsAS = dsIsotropic[dSpacetime, gammaAS];
chkAS = (etaStar == -2) && (gammaAS == 2) && (dsAS == 2);

(* (d) Causal-set d'Alembertian : universal UV d_s = 2 in all D            *)
(*     (effective UV power D -> gamma = D/2 -> D/(D/2) = 2). *)
dsCST = dsIsotropic[dSpacetime, dSpacetime/2];
chkCST = (dsCST == 2);

(* (e) Multifractional (canonical UV pick) : gamma = D/2 -> d_s = 2. *)
dsMulti = dsIsotropic[dSpacetime, dSpacetime/2];
chkMulti = (dsMulti == 2);

(* (f) Horava z = 2 : d_s = 1 + D_space/z = 1 + 3/2 = 5/2. *)
dsHz2 = dsHorava[dSpace, 2];
chkHz2 = (dsHz2 == Rational[5, 2]);

(* (g) Horava z = 3 : d_s = 1 + 3/3 = 2 (the canonical UV = 2). *)
dsHz3 = dsHorava[dSpace, 3];
chkHz3 = (dsHz3 == 2);

(* (h) Horava IR limit z = 1 : d_s = 1 + 3/1 = 4 (recovers spacetime D). *)
dsHz1 = dsHorava[dSpace, 1];
chkHz1IR = (dsHz1 == 4);

(* (i) Horava headline case from the paper itself : D_space = 3, z = 3      *)
(*     -> d_s = 2 (this is Horava's 3+1 spacetime headline result). *)
dsHoravaHeadline = dsHorava[3, 3];
chkHoravaHeadline = (dsHoravaHeadline == 2);

(* --------------------------------------------------------------------- *)
(* 3. Convention sanity: the two families agree where they must.          *)
(*    GR (isotropic gamma=1) == Horava IR (z=1): both d_s = D = 4.         *)
(* --------------------------------------------------------------------- *)
chkConventionConsistent = (dsGR == dsHz1) && (dsGR == 4);

(* All isotropic UV = 2 cases coincide (the gamma=2 subclass artifact). *)
chkGamma2Subclass = (dsStelle == 2) && (dsAS == 2) &&
                    (dsCST == 2) && (dsMulti == 2) && (dsHz3 == 2);

(* --------------------------------------------------------------------- *)
(* 4. Collect verdicts and export JSON.                                   *)
(* --------------------------------------------------------------------- *)
allChecks = {
  chkGR, chkStelle, chkAS, chkCST, chkMulti,
  chkHz2, chkHz3, chkHz1IR, chkHoravaHeadline,
  chkConventionConsistent, chkGamma2Subclass
};
overallPass = AllTrue[allChecks, TrueQ];

result = Association[
  "script" -> "ds_classifier.wl",
  "description" -> "Independent CAS re-derivation of the d_s master table limits",
  "convention" -> "D = spacetime = 4; D_space = D-1 = 3 for Horava (arXiv:0902.3657)",
  "sources" -> Association[
    "horava" -> "arXiv:0902.3657 (d_s = 1 + D_space/z)",
    "stelle" -> "Calcagni-Modesto-Nardelli arXiv:1408.0199 (UV d_s = 2)",
    "asymptotic_safety" -> "Lauscher-Reuter hep-th/0508202; Reuter-Saueressig 1110.5224",
    "causal_set_dalembertian" -> "Belenchia et al. arXiv:1507.00330",
    "multifractional" -> "Calcagni arXiv:1304.2709"
  ],
  "exact_values" -> Association[
    "GR" -> ToString[dsGR],
    "Stelle" -> ToString[dsStelle],
    "AsymptoticSafety" -> ToString[dsAS],
    "CausalSet_dAlembertian" -> ToString[dsCST],
    "Multifractional" -> ToString[dsMulti],
    "Horava_z2" -> ToString[dsHz2],
    "Horava_z3" -> ToString[dsHz3],
    "Horava_IR_z1" -> ToString[dsHz1],
    "Horava_headline_Dspace3_z3" -> ToString[dsHoravaHeadline]
  ],
  "checks" -> Association[
    "GR_ds_is_4" -> TrueQ[chkGR],
    "Stelle_ds_is_2" -> TrueQ[chkStelle],
    "AS_eta_minus2_ds_is_2" -> TrueQ[chkAS],
    "CST_dAlembertian_ds_is_2" -> TrueQ[chkCST],
    "Multifractional_ds_is_2" -> TrueQ[chkMulti],
    "Horava_z2_ds_is_5_2" -> TrueQ[chkHz2],
    "Horava_z3_ds_is_2" -> TrueQ[chkHz3],
    "Horava_IR_z1_ds_is_4" -> TrueQ[chkHz1IR],
    "Horava_headline_Dspace3_z3_ds_is_2" -> TrueQ[chkHoravaHeadline],
    "convention_GR_equals_Horava_IR" -> TrueQ[chkConventionConsistent],
    "gamma2_subclass_all_equal_2" -> TrueQ[chkGamma2Subclass]
  ],
  "overall_pass" -> TrueQ[overallPass]
];

Export[
  FileNameJoin[{DirectoryName[$InputFileName], "ds_classifier_result.json"}],
  result,
  "JSON"
];

Print["ds_classifier.wl overall_pass = ", TrueQ[overallPass]];
