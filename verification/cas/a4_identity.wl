(* ===================================================================== *)
(* a4_identity.wl                                                          *)
(*                                                                         *)
(* INDEPENDENT cross-CAS validation of the -18/11 fermionic identity       *)
(* (project draft-02-a4-fermionic-identity), re-derived in Wolfram         *)
(* Language directly from the PUBLISHED per-field coefficients -- NOT      *)
(* transcribed from the project's sympy outputs.  Agreement with the       *)
(* sympy lane is therefore independent evidence; disagreement is a bug in  *)
(* one of the two derivations.                                             *)
(*                                                                         *)
(* All arithmetic is EXACT (Rational / exact integers).  No floats enter   *)
(* any check.  Only basic canonical WL constructs are used.                *)
(*                                                                         *)
(* PUBLISHED SOURCES (literature values, entered by hand here):            *)
(*   [Duff arXiv:2003.02688, Table 1 / eq.(17)] trace-anomaly (a,c) in the  *)
(*       2-component Weyl basis, normalization <T>=(1/(4pi)^2)(c F - a G).  *)
(*   [Vassilevich hep-th/0306138, eq.(4.28)] heat-kernel a4 master.         *)
(*   [Chamseddine-Connes hep-th/9606001, eq.(2.24)] spectral-action        *)
(*       alpha0 = -3 f0/(10 pi^2) (C^2), tau0 = 11 f0/(60 pi^2) (RstarRstar). *)
(*   [Beccaria-Tseytlin arXiv:1710.03779, eq.(31)] conformal (Weyl)         *)
(*       graviton (a,c) = (87/20, 199/30).                                  *)
(* ===================================================================== *)

(* --------------------------------------------------------------------- *)
(* 1. PUBLISHED per-field trace-anomaly central charges (a, c).           *)
(*    Duff arXiv:2003.02688 Table 1, 2-component Weyl spinor basis.        *)
(*    Equivalent counting form: 720 c = 6 N0 + 18 N12 + 72 N1,             *)
(*                              720 a = 2 N0 + 11 N12 + 124 N1.            *)
(* --------------------------------------------------------------------- *)
aScalar = Rational[1, 360];   cScalar = Rational[1, 120];   (* real scalar  *)
aWeyl   = Rational[11, 720];  cWeyl   = Rational[1, 40];    (* Weyl fermion *)
aVector = Rational[31, 180];  cVector = Rational[1, 10];    (* gauge vector *)

(* Self-consistency vs. the published counting coefficients (exact). *)
chkScalarCount = (720*cScalar == 6) && (720*aScalar == 2);
chkWeylCount   = (720*cWeyl == 18)  && (720*aWeyl == 11);
chkVectorCount = (720*cVector == 72) && (720*aVector == 124);

(* --------------------------------------------------------------------- *)
(* 2. The convention-free C^2-vs-Euler ratio is c/(-a) because the Euler  *)
(*    density enters <T> with sign -a.  All ratios computed exactly.      *)
(* --------------------------------------------------------------------- *)
cOverMinusA[a_, c_] := c/(-a);

ratioSingleWeyl = cOverMinusA[aWeyl, cWeyl];          (* expect -18/11 *)
ratioDirac      = cOverMinusA[2*aWeyl, 2*cWeyl];      (* Dirac = 2 x Weyl *)

(* HEADLINE check: a single Weyl fermion gives EXACTLY -18/11. *)
chkSingleWeyl = (ratioSingleWeyl == Rational[-18, 11]);
(* Dirac control: 2 x Weyl is the SAME ratio (N cancels). *)
chkDiracSameAsWeyl = (ratioDirac == ratioSingleWeyl) &&
                     (ratioDirac == Rational[-18, 11]);

(* --------------------------------------------------------------------- *)
(* 3. Three-route consistency the draft claims:                           *)
(*    (i)  Chamseddine-Connes spectral action  alpha0/tau0                 *)
(*    (ii) single-Weyl  c/(-a)                                             *)
(*    (iii) Dirac (2 x Weyl)  c/(-a)                                       *)
(*    must ALL equal -18/11.  f0 is a formal symbol; it must cancel.       *)
(* --------------------------------------------------------------------- *)
(* Keep pi as the WL symbol Pi and f0 formal; the ratio must be free of    *)
(* both.  We use Together so the cancellation is purely algebraic.         *)
alpha0 = -Rational[3, 10]*f0/Pi^2;   (* coeff of C^2,  CC eq.(2.24) *)
tau0   =  Rational[11, 60]*f0/Pi^2;  (* coeff of RstarRstar, CC eq.(2.24) *)

ratioSpectral = Together[alpha0/tau0];   (* expect -18/11, f0 and Pi gone *)

chkSpectral = (ratioSpectral == Rational[-18, 11]);
chkSpectralFreeOfF0 = FreeQ[ratioSpectral, f0];
chkSpectralFreeOfPi = FreeQ[ratioSpectral, Pi];
chkThreeRoute = (ratioSpectral == ratioSingleWeyl) &&
                (ratioSpectral == ratioDirac);

(* "11" fingerprint: spectral Euler factor 11/60 and Weyl a = 11/720       *)
(* both carry the prime 11; their ratio is the exact integer 12.           *)
chkEleven = ((Rational[11, 60])/(Rational[11, 720]) == 12);

(* --------------------------------------------------------------------- *)
(* 4. Standard-Model fermion content check (content-independence).        *)
(*    Every Weyl fermion carries the SAME (a,c), so the purely fermionic   *)
(*    ratio is -18/11 for ANY count: 45 (no nuR) or 48 (with nuR).         *)
(* --------------------------------------------------------------------- *)
nWnoNu   = 45;   (* 15 Weyl/gen x 3 gen *)
nWwithNu = 48;   (* 16 Weyl/gen x 3 gen, NCG with right-handed neutrinos *)

aFermNoNu   = nWnoNu*aWeyl;     cFermNoNu   = nWnoNu*cWeyl;
aFermWithNu = nWwithNu*aWeyl;   cFermWithNu = nWwithNu*cWeyl;

ratioFermNoNu   = cOverMinusA[aFermNoNu, cFermNoNu];
ratioFermWithNu = cOverMinusA[aFermWithNu, cFermWithNu];

chkSMfermNoNu   = (ratioFermNoNu == Rational[-18, 11]);
chkSMfermWithNu = (ratioFermWithNu == Rational[-18, 11]);
chkContentIndependent = (ratioFermNoNu == ratioFermWithNu);

(* Full SM (fermions + 4 real scalars + 12 vectors) BREAKS the identity:   *)
(* the draft's documented falsification, exact value -1698/1991.           *)
n0Scalars = 4;    (* one complex Higgs doublet = 4 real scalars *)
n1Vectors = 12;   (* 8 gluon + 3 W + 1 B *)
aFullNoNu = n0Scalars*aScalar + nWnoNu*aWeyl + n1Vectors*aVector;
cFullNoNu = n0Scalars*cScalar + nWnoNu*cWeyl + n1Vectors*cVector;
ratioFullNoNu = cOverMinusA[aFullNoNu, cFullNoNu];
chkFullSMbreaks = (ratioFullNoNu == Rational[-1698, 1991]) &&
                  (ratioFullNoNu =!= Rational[-18, 11]);

(* --------------------------------------------------------------------- *)
(* 5. Conformal-graviton ratio.  Beccaria-Tseytlin arXiv:1710.03779       *)
(*    eq.(31): (a,c) = (87/20, 199/30).  c/(-a) = -398/261, and it is NOT  *)
(*    -18/11 (the graviton does not restore the identity).                *)
(* --------------------------------------------------------------------- *)
aConfGrav = Rational[87, 20];   cConfGrav = Rational[199, 30];
ratioConfGrav = cOverMinusA[aConfGrav, cConfGrav];
chkConfGrav = (ratioConfGrav == Rational[-398, 261]);
chkConfGravNot1811 = (ratioConfGrav =!= Rational[-18, 11]);

(* Conformal-HS cross-lock (same paper): a_s = nu^2 (14 nu + 3)/720, with  *)
(* nu = s(s+1).  s=1 -> a = 31/180 (vector); s=2 -> a = 87/20 (graviton).  *)
aSpinHS[s_] := Module[{nu = s*(s + 1)}, Rational[nu^2*(14*nu + 3), 720]];
chkHSvector   = (aSpinHS[1] == aVector);
chkHSgraviton = (aSpinHS[2] == aConfGrav);

(* --------------------------------------------------------------------- *)
(* 6. STr(1) supertrace counts n_B - n_F from the SM multiplet table       *)
(*    (Pauli quartic-cancellation condition STr 1 = 0).                    *)
(*    Bosons: 12 massless vectors x 2 pol = 24, + 4 real scalars = 28.     *)
(*    Fermions: 2 real d.o.f. per Weyl -> 90 (no nuR) / 96 (with nuR).     *)
(* --------------------------------------------------------------------- *)
nB     = 12*2 + 4;       (* = 28 *)
nFnoNu   = 2*nWnoNu;     (* = 90 *)
nFwithNu = 2*nWwithNu;   (* = 96 *)
sTr1noNu   = nB - nFnoNu;     (* = -62 *)
sTr1withNu = nB - nFwithNu;   (* = -68 *)
chkSTrNoNu   = (sTr1noNu == -62);
chkSTrWithNu = (sTr1withNu == -68);
(* nuR makes the imbalance worse (more negative), never cancels it. *)
chkSTrWorse  = (sTr1withNu < sTr1noNu) && (sTr1noNu < 0);

(* --------------------------------------------------------------------- *)
(* 7. Collect verdicts and export JSON.                                   *)
(* --------------------------------------------------------------------- *)
allChecks = {
  chkScalarCount, chkWeylCount, chkVectorCount,
  chkSingleWeyl, chkDiracSameAsWeyl,
  chkSpectral, chkSpectralFreeOfF0, chkSpectralFreeOfPi, chkThreeRoute,
  chkEleven,
  chkSMfermNoNu, chkSMfermWithNu, chkContentIndependent, chkFullSMbreaks,
  chkConfGrav, chkConfGravNot1811, chkHSvector, chkHSgraviton,
  chkSTrNoNu, chkSTrWithNu, chkSTrWorse
};
overallPass = AllTrue[allChecks, TrueQ];

result = Association[
  "script" -> "a4_identity.wl",
  "description" -> "Independent CAS re-derivation of the -18/11 fermionic identity",
  "sources" -> Association[
    "anomaly_ac" -> "Duff arXiv:2003.02688 Table 1",
    "heat_kernel" -> "Vassilevich hep-th/0306138 eq.4.28",
    "spectral_action" -> "Chamseddine-Connes hep-th/9606001 eq.2.24",
    "conformal_graviton" -> "Beccaria-Tseytlin arXiv:1710.03779 eq.31"
  ],
  "exact_rationals" -> Association[
    "ratio_single_weyl" -> ToString[ratioSingleWeyl, InputForm],
    "ratio_dirac" -> ToString[ratioDirac, InputForm],
    "ratio_spectral_alpha0_over_tau0" -> ToString[ratioSpectral, InputForm],
    "ratio_ferm_SM_noNu" -> ToString[ratioFermNoNu, InputForm],
    "ratio_ferm_SM_withNu" -> ToString[ratioFermWithNu, InputForm],
    "ratio_full_SM_noNu" -> ToString[ratioFullNoNu, InputForm],
    "ratio_conformal_graviton" -> ToString[ratioConfGrav, InputForm],
    "STr1_noNu" -> ToString[sTr1noNu, InputForm],
    "STr1_withNu" -> ToString[sTr1withNu, InputForm]
  ],
  "checks" -> Association[
    "scalar_counting_coeffs" -> TrueQ[chkScalarCount],
    "weyl_counting_coeffs" -> TrueQ[chkWeylCount],
    "vector_counting_coeffs" -> TrueQ[chkVectorCount],
    "single_weyl_is_minus_18_11" -> TrueQ[chkSingleWeyl],
    "dirac_equals_weyl_ratio" -> TrueQ[chkDiracSameAsWeyl],
    "spectral_alpha0_over_tau0_is_minus_18_11" -> TrueQ[chkSpectral],
    "spectral_ratio_free_of_f0" -> TrueQ[chkSpectralFreeOfF0],
    "spectral_ratio_free_of_pi" -> TrueQ[chkSpectralFreeOfPi],
    "three_route_consistency" -> TrueQ[chkThreeRoute],
    "eleven_fingerprint_ratio_is_12" -> TrueQ[chkEleven],
    "SM_fermions_noNu_is_minus_18_11" -> TrueQ[chkSMfermNoNu],
    "SM_fermions_withNu_is_minus_18_11" -> TrueQ[chkSMfermWithNu],
    "content_independent_45_eq_48" -> TrueQ[chkContentIndependent],
    "full_SM_breaks_identity_minus_1698_1991" -> TrueQ[chkFullSMbreaks],
    "conformal_graviton_is_minus_398_261" -> TrueQ[chkConfGrav],
    "conformal_graviton_not_minus_18_11" -> TrueQ[chkConfGravNot1811],
    "HS_formula_reproduces_vector" -> TrueQ[chkHSvector],
    "HS_formula_reproduces_graviton" -> TrueQ[chkHSgraviton],
    "STr1_noNu_is_minus_62" -> TrueQ[chkSTrNoNu],
    "STr1_withNu_is_minus_68" -> TrueQ[chkSTrWithNu],
    "nuR_makes_imbalance_worse" -> TrueQ[chkSTrWorse]
  ],
  "overall_pass" -> TrueQ[overallPass]
];

Export[
  FileNameJoin[{DirectoryName[$InputFileName], "a4_identity_result.json"}],
  result,
  "JSON"
];

Print["a4_identity.wl overall_pass = ", TrueQ[overallPass]];
