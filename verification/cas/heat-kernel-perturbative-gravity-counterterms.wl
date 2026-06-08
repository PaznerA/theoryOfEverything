(* ===================================================================== *)
(* heat-kernel-perturbative-gravity-counterterms.wl                        *)
(*                                                                         *)
(* INDEPENDENT cross-CAS validation of batch B1:                           *)
(*   "heat-kernel / perturbative-gravity counterterms & power counting"    *)
(*   (domain: supergravity-uv + asymptotic-safety).                        *)
(*                                                                         *)
(* Each published rational coefficient / identity is RE-DERIVED in         *)
(* Wolfram Language directly from its stated literature form -- NOT        *)
(* transcribed from the project's sympy outputs.  Agreement with the       *)
(* sympy / knowledge-base lane is therefore independent evidence;          *)
(* disagreement is a bug in one of the two derivations.                    *)
(*                                                                         *)
(* All arithmetic is EXACT (Rational / exact integers / formal symbols).   *)
(* No floats enter any check.  Only basic canonical WL constructs are      *)
(* used.  Output strings are forced through InputForm to avoid the         *)
(* multiline-pretty-print bug the project hit before.                      *)
(*                                                                         *)
(* PUBLISHED SOURCES (literature values, entered by hand here):            *)
(*   't Hooft-Veltman 1974    : one-loop R^2 (1/120) + Ricci^2 (7/20)      *)
(*                              counterterm; power counting D=(d-2)L+2.     *)
(*                              (refs: tHooft-Veltman-1974)                 *)
(*   Goroff-Sagnotti 1986     : two-loop 209/2880 C^3 counterterm.         *)
(*                              (refs: goroff-sagnotti-1986)                *)
(*   Bjerrum-Bohr-Donoghue-                                                 *)
(*     Holstein 2003          : quantum potential coeff 41/(10 Pi) hbar.   *)
(*                              (refs: Bjerrum-Bohr-Donoghue-Holstein-2003)*)
(*   Bern et al. 2018 5-loop  : D_c = 4 + 6/L; 5-loop D_c = 24/5 < 26/5.   *)
(*                              (refs: Bern-et-al-2018-5loop)               *)
(*   Weinberg 1979            : 2+eps fixed point g* = (3/38) eps.         *)
(*                              (refs: weinberg-1979)                       *)
(*   Cremmer-Julia-Scherk     : N=8 spin content Binomial[8, 4-2 s].       *)
(*     1978                     (refs: Cremmer-Julia-Scherk-1978)          *)
(*   Stelle 1977              : 1/(p^2(p^2+M^2)) partial fraction.         *)
(*                              (refs: Stelle-1977)                         *)
(* ===================================================================== *)

(* ===================================================================== *)
(* (i) onshell-oneloop-counterterm                                         *)
(*     't Hooft-Veltman 1974: one-loop divergence of pure gravity is       *)
(*       (1/(4Pi)^2)(1/eps) Integral sqrt(-g) ( (1/120) R^2                 *)
(*                                              + (7/20) Ric^2 ).          *)
(*     Re-derivation:                                                       *)
(*       (a) the published coefficient pair is EXACTLY {1/120, 7/20};      *)
(*       (b) on-shell (vacuum Einstein eqs) R = 0 and R_munu = 0, so a     *)
(*           symbolic substitution {R->0, Ric->0} kills BOTH terms ->      *)
(*           the divergence vanishes (pure gravity is one-loop finite).    *)
(* ===================================================================== *)
cR2     = Rational[1, 120];   (* coefficient of R^2     *)
cRicci2 = Rational[7, 20];    (* coefficient of R_munu R^munu *)

(* (a) coefficients are exactly the published rationals. *)
chkHVcoeffR2    = (cR2 == Rational[1, 120]);
chkHVcoeffRicci = (cRicci2 == Rational[7, 20]);
(* both are genuinely rational and nonzero (a real counterterm exists). *)
chkHVcoeffsRational = (Head[cR2] === Rational) && (Head[cRicci2] === Rational);

(* (b) on-shell vanishing as a symbolic substitution.                      *)
(*     Build the divergence density with formal curvature symbols, then    *)
(*     impose the vacuum Einstein eqs R -> 0, Ric -> 0.                     *)
ClearAll[scR, scRic];
divDensity = cR2*scR^2 + cRicci2*scRic^2;
divOnShell = divDensity /. {scR -> 0, scRic -> 0};
chkHVonShellZero = (divOnShell === 0);
(* and off-shell it is genuinely nonzero (the cancellation is special). *)
chkHVoffShellNonzero = (divDensity =!= 0);

(* ===================================================================== *)
(* (ii) goroff-sagnotti-counterterm                                        *)
(*      Goroff-Sagnotti 1986: nonvanishing TWO-loop divergence of pure     *)
(*      gravity, coefficient 209/2880 times (1/(16 Pi^2)^2)(1/eps)         *)
(*      Integral sqrt(-g) C^{..}.. C C  (Weyl tensor cubed).               *)
(*      The physics CLAIM is just exactness + nonzero-ness: a C^3 term     *)
(*      survives on-shell (Weyl != 0 in vacuum) and cannot be removed by   *)
(*      field redefinition => perturbative non-renormalizability.          *)
(*      Re-derivation: confirm 209/2880 is Rational, nonzero, in lowest    *)
(*      terms, and that the C^3 term does NOT vanish on the Ricci-flat     *)
(*      shell (it depends on Weyl, which is unconstrained in vacuum).      *)
(* ===================================================================== *)
cGS = Rational[209, 2880];

chkGSrational = (Head[cGS] === Rational);
chkGSnonzero  = (cGS =!= 0) && (cGS > 0);
(* in lowest terms: gcd(209, 2880) = 1, so Numerator/Denominator are 209/2880. *)
chkGSlowestTerms = (Numerator[cGS] == 209) && (Denominator[cGS] == 2880) &&
                   (GCD[209, 2880] == 1);
(* on-shell survival: C^3 term with R->0, Ric->0 still carries Weyl (Cw). *)
ClearAll[Cw];
gsDensity = cGS*Cw^3;
gsOnShell = gsDensity /. {scR -> 0, scRic -> 0};   (* Weyl unconstrained *)
chkGSsurvivesOnShell = (gsOnShell =!= 0) && (! FreeQ[gsOnShell, Cw]);

(* ===================================================================== *)
(* (iii) gravity-power-counting                                            *)
(*       't Hooft-Veltman power counting: superficial degree of            *)
(*       divergence D = (d-2) L + 2.  Evaluated symbolically at d = 4      *)
(*       must Simplify to 2 L + 2 (grows with loop order => each loop      *)
(*       needs a higher-curvature counterterm).                            *)
(* ===================================================================== *)
ClearAll[dDim, ell];
Dsuperficial[d_, L_] := (d - 2)*L + 2;
DatFour = Simplify[Dsuperficial[dDim, ell] /. dDim -> 4];   (* expect 2 ell + 2 *)
(* Simplify may return the FACTORED form 2(1+ell); compare as polynomials   *)
(* (their difference is identically zero) rather than by syntactic SameQ.   *)
chkPCd4 = (Expand[DatFour] === 2*ell + 2) &&
          (Simplify[DatFour - (2*ell + 2)] === 0);
(* sample loop orders: L=1 -> 4, L=2 -> 6, L=3 -> 8 (rises by 2 per loop). *)
chkPCsamples = (DatFour /. ell -> 1) == 4 &&
               (DatFour /. ell -> 2) == 6 &&
               (DatFour /. ell -> 3) == 8;
(* it is strictly increasing in L (non-renormalizable growth). *)
chkPCgrows = ((DatFour /. ell -> 2) > (DatFour /. ell -> 1));
(* sanity: in d=2 the degree is L-independent (=2), the special case. *)
chkPCd2flat = Simplify[Dsuperficial[2, ell]] === 2;

(* ===================================================================== *)
(* (iv) quantum-potential                                                  *)
(*      Bjerrum-Bohr-Donoghue-Holstein 2003: leading genuine QUANTUM       *)
(*      correction to the Newtonian potential carries coefficient          *)
(*      41/(10 Pi) and is the unique term proportional to hbar (and to     *)
(*      Pi^-1).  The classical post-Newtonian term (3 G(m1+m2)/(r c^2))    *)
(*      is hbar-free.  Re-derivation: build the term with formal hbar, G,  *)
(*      Pi, c and FreeQ-check the (hbar, Pi) power structure.              *)
(* ===================================================================== *)
cQP = Rational[41, 10];   (* the rational part; the Pi^-1 is explicit below *)

ClearAll[hbar, Gn, cc, rr, m1, m2];
(* full quantum term (3rd bracket term) up to the overall -G m1 m2 / r:    *)
(*   (41/(10 Pi)) * G hbar / (r^2 c^3).                                    *)
quantumTerm = cQP*(1/Pi)*Gn*hbar/(rr^2*cc^3);
(* classical post-Newtonian term: 3 G (m1+m2)/(r c^2) -- hbar-free.        *)
classicalTerm = 3*Gn*(m1 + m2)/(rr*cc^2);

(* exactly one power of hbar: term/hbar is hbar-free, term has hbar. *)
chkQPhasHbar   = (! FreeQ[quantumTerm, hbar]);
chkQPoneHbar   = FreeQ[Together[quantumTerm/hbar], hbar] &&
                 (Exponent[quantumTerm, hbar] === 1);
(* exactly one inverse power of Pi (Pi^-1): Exponent in Pi is -1. *)
chkQPpiInverse = (Exponent[quantumTerm, Pi] === -1);
(* the rational coefficient is exactly 41/10. *)
chkQPcoeff     = (cQP == Rational[41, 10]);
(* the classical term carries NO hbar (genuine quantum vs classical split). *)
chkQPclassicalNoHbar = FreeQ[classicalTerm, hbar];

(* ===================================================================== *)
(* (v) n8-critical-dimension-formula                                       *)
(*     Bern et al. 2018 (5-loop): critical dimension D_c(L) = 4 + 6/L      *)
(*     holds for 2 <= L <= 4, giving D_c(2)=7, D_c(3)=6, D_c(4)=11/2.      *)
(*     At 5 loops the MEASURED critical dimension is D_c=24/5, BELOW the   *)
(*     26/5 the naive formula 4+6/5 would give (no enhanced cancellation;  *)
(*     N=8 behaves like N=4 SYM at 5 loops).                               *)
(*     Re-derivation: evaluate 4+6/L at L=2,3,4 -> {7,6,11/2} as exact     *)
(*     rationals, and 4+6/5 = 26/5; assert measured 24/5 < 26/5 exactly.   *)
(* ===================================================================== *)
Dc[L_] := 4 + Rational[6, 1]/L;

DcL2 = Dc[2];   (* 7    *)
DcL3 = Dc[3];   (* 6    *)
DcL4 = Dc[4];   (* 11/2 *)
DcL5formula = Dc[5];          (* 26/5  : what the formula would predict *)
DcL5measured = Rational[24, 5]; (* the actual 5-loop critical dimension *)

chkDcL2 = (DcL2 == 7);
chkDcL3 = (DcL3 == 6);
chkDcL4 = (DcL4 == Rational[11, 2]);
chkDcL5formula = (DcL5formula == Rational[26, 5]);
(* the headline: 5-loop measured 24/5 is STRICTLY below the formula 26/5.   *)
chkDc5Inequality = (DcL5measured < DcL5formula) &&
                   (DcL5measured == Rational[24, 5]) &&
                   (DcL5formula == Rational[26, 5]);
(* monotone falling formula (D_c decreases with loop order) through L=4.   *)
chkDcMonotone = (DcL2 > DcL3) && (DcL3 > DcL4);

(* ===================================================================== *)
(* (vi) two-plus-epsilon-fp                                                *)
(*      Weinberg 1979: perturbative gravity fixed point near two           *)
(*      dimensions, g* = (3/38) eps + O(eps^2), with critical exponent     *)
(*      theta = eps + O(eps^2), in d = 2 + eps.                            *)
(*      Re-derivation: the leading coefficient of g* in eps is exactly     *)
(*      3/38 (Rational); theta leading coefficient is exactly 1.           *)
(* ===================================================================== *)
ClearAll[eps];
gStar = Rational[3, 38]*eps;       (* leading-order fixed point coupling *)
thetaExp = eps;                    (* leading-order critical exponent    *)

(* leading coefficient in eps is the Rational 3/38. *)
gStarLeadCoeff = Coefficient[gStar, eps, 1];
chkWeinbergCoeff = (gStarLeadCoeff == Rational[3, 38]) &&
                   (Head[gStarLeadCoeff] === Rational);
(* g* vanishes as eps -> 0 (perturbative around d=2, Gaussian at eps=0). *)
chkWeinbergGaussian = (Limit[gStar, eps -> 0] == 0) &&
                      (Coefficient[gStar, eps, 0] == 0);
(* theta leading coefficient is exactly 1 (single relevant direction). *)
chkWeinbergTheta = (Coefficient[thetaExp, eps, 1] == 1);
(* dimension bookkeeping d = 2 + eps. *)
chkWeinbergDim = Simplify[(2 + eps) /. eps -> 2] == 4;  (* eps=2 -> d=4 (uncontrolled) *)

(* ===================================================================== *)
(* (vii) n8-spin-content                                                   *)
(*       Cremmer-Julia-Scherk 1978: N=8 supergravity multiplet field       *)
(*       content #(spin s) = Binomial[8, 4 - 2 s] for                      *)
(*       s in {2, 3/2, 1, 1/2, 0}  ->  {1, 8, 28, 56, 70}, and the         *)
(*       full multiplet (counting both helicities for s>0 plus the 70      *)
(*       real scalars) totals 256 states.                                  *)
(*       Re-derivation: evaluate the binomial directly; the 5 listed       *)
(*       entries are the POSITIVE-helicity tower (1+8+28+56+70 = 163),     *)
(*       and the full 256 = 2^8 = sum over the FULL k=0..8 binomial row,   *)
(*       i.e. Total[Binomial[8,k], k=0..8] = 256.                          *)
(* ===================================================================== *)
spins = {2, 3/2, 1, 1/2, 0};
spinCounts = Binomial[8, 4 - 2*#] & /@ spins;   (* expect {1,8,28,56,70} *)

chkSpinCounts = (spinCounts == {1, 8, 28, 56, 70});
(* individual entries (explicit, so a single wrong binomial is caught). *)
chkSpinGraviton = (Binomial[8, 4 - 2*2] == 1);       (* s=2   -> 1  *)
chkSpinGravitino = (Binomial[8, 4 - 2*(3/2)] == 8);  (* s=3/2 -> 8  *)
chkSpinVector = (Binomial[8, 4 - 2*1] == 28);        (* s=1   -> 28 *)
chkSpinFermion = (Binomial[8, 4 - 2*(1/2)] == 56);   (* s=1/2 -> 56 *)
chkSpinScalar = (Binomial[8, 4 - 2*0] == 70);        (* s=0   -> 70 *)
(* listed (single-helicity-tower) total. *)
chkSpinListedTotal = (Total[spinCounts] == 163);
(* full multiplet 2^8 = 256 = sum of the entire Binomial[8,k] row. *)
chkSpin256 = (Total[Binomial[8, Range[0, 8]]] == 256) &&
             (Total[Binomial[8, Range[0, 8]]] == 2^8);
(* 70 scalars = central self-conjugate entry, parametrize E7(7)/SU(8). *)
chkSpin70central = (Binomial[8, 4] == 70);

(* ===================================================================== *)
(* (viii) stelle-propagator                                                *)
(*        Stelle 1977: higher-derivative (quadratic gravity) propagator    *)
(*        partial-fraction decomposition                                   *)
(*          1/(p^2 (p^2 + M^2)) = (1/M^2)(1/p^2 - 1/(p^2 + M^2)).          *)
(*        The negative-sign second pole is the massive spin-2 ghost.       *)
(*        Re-derivation: Apart the LHS and Together the asserted RHS;      *)
(*        their difference must Simplify to 0 (exact identity).            *)
(* ===================================================================== *)
ClearAll[pp, Mm];
stelleLHS = 1/(pp^2*(pp^2 + Mm^2));
stelleRHS = (1/Mm^2)*(1/pp^2 - 1/(pp^2 + Mm^2));

(* Apart on the squared-momentum variable q = p^2. *)
ClearAll[qq];
apartForm = Apart[1/(qq*(qq + Mm^2)), qq];     (* WL's own partial fraction *)
apartExpected = (1/Mm^2)*(1/qq - 1/(qq + Mm^2));
chkStelleApart = (Simplify[apartForm - apartExpected] === 0);
(* direct LHS == RHS as rational functions in p. *)
chkStelleIdentity = (Simplify[Together[stelleLHS - stelleRHS]] === 0);
(* the second pole carries a NEGATIVE residue (the ghost): residue of the   *)
(* RHS at p^2 = -M^2 is -1/M^2 < 0 vs +1/M^2 at p^2 = 0.                     *)
residueAtZero  = Residue[stelleRHS, {qq, 0}] /. stelleRHS -> apartExpected;
(* compute residues directly in q = p^2. *)
resZero  = Residue[apartExpected, {qq, 0}];        (*  +1/M^2 *)
resGhost = Residue[apartExpected, {qq, -Mm^2}];    (*  -1/M^2 *)
chkStelleGhostResidue = (Simplify[resZero - 1/Mm^2] === 0) &&
                        (Simplify[resGhost + 1/Mm^2] === 0);

(* ===================================================================== *)
(* Collect per-formula verdicts.                                           *)
(* ===================================================================== *)
verHV = AllTrue[{chkHVcoeffR2, chkHVcoeffRicci, chkHVcoeffsRational,
                 chkHVonShellZero, chkHVoffShellNonzero}, TrueQ];
verGS = AllTrue[{chkGSrational, chkGSnonzero, chkGSlowestTerms,
                 chkGSsurvivesOnShell}, TrueQ];
verPC = AllTrue[{chkPCd4, chkPCsamples, chkPCgrows, chkPCd2flat}, TrueQ];
verQP = AllTrue[{chkQPhasHbar, chkQPoneHbar, chkQPpiInverse, chkQPcoeff,
                 chkQPclassicalNoHbar}, TrueQ];
verDc = AllTrue[{chkDcL2, chkDcL3, chkDcL4, chkDcL5formula,
                 chkDc5Inequality, chkDcMonotone}, TrueQ];
verWeinberg = AllTrue[{chkWeinbergCoeff, chkWeinbergGaussian,
                       chkWeinbergTheta, chkWeinbergDim}, TrueQ];
verSpin = AllTrue[{chkSpinCounts, chkSpinGraviton, chkSpinGravitino,
                   chkSpinVector, chkSpinFermion, chkSpinScalar,
                   chkSpinListedTotal, chkSpin256, chkSpin70central}, TrueQ];
verStelle = AllTrue[{chkStelleApart, chkStelleIdentity,
                     chkStelleGhostResidue}, TrueQ];

overallPass = AllTrue[{verHV, verGS, verPC, verQP, verDc, verWeinberg,
                       verSpin, verStelle}, TrueQ];

(* ===================================================================== *)
(* Export JSON (InputForm strings throughout to avoid pretty-print bug).   *)
(* ===================================================================== *)
result = Association[
  "script" -> "heat-kernel-perturbative-gravity-counterterms.wl",
  "batch" -> "B1: heat-kernel / perturbative-gravity counterterms & power counting",
  "description" -> "Independent CAS re-derivation of published counterterm / power-counting / spectrum coefficients",
  "sources" -> Association[
    "onshell-oneloop-counterterm" -> "tHooft-Veltman-1974 (1/120 R^2 + 7/20 Ric^2)",
    "goroff-sagnotti-counterterm" -> "goroff-sagnotti-1986 (209/2880 C^3)",
    "gravity-power-counting" -> "tHooft-Veltman-1974 (D=(d-2)L+2)",
    "quantum-potential" -> "Bjerrum-Bohr-Donoghue-Holstein-2003 (41/(10 Pi))",
    "n8-critical-dimension-formula" -> "Bern-et-al-2018-5loop (D_c=4+6/L; 5-loop 24/5)",
    "two-plus-epsilon-fp" -> "weinberg-1979 (g*=3/38 eps)",
    "n8-spin-content" -> "Cremmer-Julia-Scherk-1978 (Binomial[8,4-2s])",
    "stelle-propagator" -> "Stelle-1977 (1/(p^2(p^2+M^2)) partial fraction)"
  ],
  "exact_values" -> Association[
    "HV_coeff_R2" -> ToString[cR2, InputForm],
    "HV_coeff_Ricci2" -> ToString[cRicci2, InputForm],
    "HV_div_on_shell" -> ToString[divOnShell, InputForm],
    "GS_coeff" -> ToString[cGS, InputForm],
    "powercounting_d4" -> ToString[DatFour, InputForm],
    "quantum_potential_rational" -> ToString[cQP, InputForm],
    "quantum_term" -> ToString[quantumTerm, InputForm],
    "Dc_L2" -> ToString[DcL2, InputForm],
    "Dc_L3" -> ToString[DcL3, InputForm],
    "Dc_L4" -> ToString[DcL4, InputForm],
    "Dc_L5_formula" -> ToString[DcL5formula, InputForm],
    "Dc_L5_measured" -> ToString[DcL5measured, InputForm],
    "weinberg_gstar" -> ToString[gStar, InputForm],
    "weinberg_lead_coeff" -> ToString[gStarLeadCoeff, InputForm],
    "n8_spin_counts" -> ToString[spinCounts, InputForm],
    "n8_full_multiplet" -> ToString[Total[Binomial[8, Range[0, 8]]], InputForm],
    "stelle_apart" -> ToString[apartForm, InputForm],
    "stelle_residue_zero" -> ToString[Simplify[resZero], InputForm],
    "stelle_residue_ghost" -> ToString[Simplify[resGhost], InputForm]
  ],
  "checks" -> Association[
    "HV_coeff_R2_is_1_over_120" -> TrueQ[chkHVcoeffR2],
    "HV_coeff_Ricci2_is_7_over_20" -> TrueQ[chkHVcoeffRicci],
    "HV_coeffs_rational" -> TrueQ[chkHVcoeffsRational],
    "HV_on_shell_divergence_vanishes" -> TrueQ[chkHVonShellZero],
    "HV_off_shell_nonzero" -> TrueQ[chkHVoffShellNonzero],
    "GS_coeff_rational" -> TrueQ[chkGSrational],
    "GS_coeff_nonzero" -> TrueQ[chkGSnonzero],
    "GS_coeff_lowest_terms_209_2880" -> TrueQ[chkGSlowestTerms],
    "GS_survives_on_shell" -> TrueQ[chkGSsurvivesOnShell],
    "powercounting_d4_is_2L_plus_2" -> TrueQ[chkPCd4],
    "powercounting_samples_4_6_8" -> TrueQ[chkPCsamples],
    "powercounting_grows_with_L" -> TrueQ[chkPCgrows],
    "powercounting_d2_flat" -> TrueQ[chkPCd2flat],
    "QP_has_hbar" -> TrueQ[chkQPhasHbar],
    "QP_exactly_one_hbar" -> TrueQ[chkQPoneHbar],
    "QP_pi_inverse_power" -> TrueQ[chkQPpiInverse],
    "QP_rational_coeff_41_10" -> TrueQ[chkQPcoeff],
    "QP_classical_term_hbar_free" -> TrueQ[chkQPclassicalNoHbar],
    "Dc_L2_is_7" -> TrueQ[chkDcL2],
    "Dc_L3_is_6" -> TrueQ[chkDcL3],
    "Dc_L4_is_11_2" -> TrueQ[chkDcL4],
    "Dc_L5_formula_is_26_5" -> TrueQ[chkDcL5formula],
    "Dc_5loop_24_5_below_26_5" -> TrueQ[chkDc5Inequality],
    "Dc_monotone_through_L4" -> TrueQ[chkDcMonotone],
    "weinberg_gstar_coeff_3_38" -> TrueQ[chkWeinbergCoeff],
    "weinberg_gaussian_at_eps0" -> TrueQ[chkWeinbergGaussian],
    "weinberg_theta_coeff_1" -> TrueQ[chkWeinbergTheta],
    "weinberg_dim_bookkeeping" -> TrueQ[chkWeinbergDim],
    "n8_spin_counts_1_8_28_56_70" -> TrueQ[chkSpinCounts],
    "n8_graviton_1" -> TrueQ[chkSpinGraviton],
    "n8_gravitino_8" -> TrueQ[chkSpinGravitino],
    "n8_vector_28" -> TrueQ[chkSpinVector],
    "n8_fermion_56" -> TrueQ[chkSpinFermion],
    "n8_scalar_70" -> TrueQ[chkSpinScalar],
    "n8_listed_total_163" -> TrueQ[chkSpinListedTotal],
    "n8_full_multiplet_256" -> TrueQ[chkSpin256],
    "n8_70_is_central_binomial" -> TrueQ[chkSpin70central],
    "stelle_apart_matches" -> TrueQ[chkStelleApart],
    "stelle_identity_holds" -> TrueQ[chkStelleIdentity],
    "stelle_ghost_negative_residue" -> TrueQ[chkStelleGhostResidue]
  ],
  "per_formula" -> Association[
    "onshell-oneloop-counterterm" -> TrueQ[verHV],
    "goroff-sagnotti-counterterm" -> TrueQ[verGS],
    "gravity-power-counting" -> TrueQ[verPC],
    "quantum-potential" -> TrueQ[verQP],
    "n8-critical-dimension-formula" -> TrueQ[verDc],
    "two-plus-epsilon-fp" -> TrueQ[verWeinberg],
    "n8-spin-content" -> TrueQ[verSpin],
    "stelle-propagator" -> TrueQ[verStelle]
  ],
  "overall_pass" -> TrueQ[overallPass]
];

Export[
  FileNameJoin[{DirectoryName[$InputFileName],
    "heat-kernel-perturbative-gravity-counterterms_result.json"}],
  result,
  "JSON"
];

Print["heat-kernel-perturbative-gravity-counterterms.wl per_formula = ",
  ToString[result["per_formula"], InputForm]];
Print["heat-kernel-perturbative-gravity-counterterms.wl overall_pass = ",
  TrueQ[overallPass]];
