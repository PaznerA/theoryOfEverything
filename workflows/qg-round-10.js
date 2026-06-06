export const meta = {
  name: 'qg-round-10',
  description: 'Kolo 10 (dogfooding lib/toe): VYPOCET-21 H5g-1 4D dS typový diskriminátor přes truncovanou area law; VYPOCET-22 H5g-3 codim-2 spoj jako 4D analog rohu; úklid',
  phases: [
    { title: 'Výpočty', detail: 'VYPOCET-21 + VYPOCET-22 paralelně (lib/toe konzumenti)', model: 'opus' },
    { title: 'Úklid', detail: 'findings F-025/26, PROGRESS, INDEX, BRAINSTORM-05 statusy', model: 'sonnet' },
  ],
}

const ROOT = '/Users/pazny/projects/theoryOfEverything'
const CD = ROOT + '/core-data'
const KB = ROOT + '/knowledge-base'
const LIB = ROOT + '/lib'
const DATE = (args && args.date) || '2026-06-06'

const CALC_RESULT = {
  type: 'object',
  properties: {
    name: { type: 'string' },
    status: { type: 'string', description: 'success | partial | failed' },
    keyNumbers: { type: 'string' },
    verdictForHypothesis: { type: 'string', description: 'Czech, 2-4 sentences' },
    libUsage: { type: 'string', description: 'which toe functions were used; what was missing; library extensions made' },
    files: { type: 'array', items: { type: 'string' } },
  },
  required: ['name', 'status', 'keyNumbers', 'verdictForHypothesis', 'libUsage', 'files'],
}

const CALC_COMMON = `You are a computational physics agent at ${ROOT}. Environment: python3 + numpy/scipy/sympy/matplotlib (Agg). NEVER fudge results; honest nulls are findings.

DOGFOODING MANDATE (this round exists to stress-test the new library): build your calc ON TOP of ${LIB}/toe (v0.1.0) — read ${LIB}/toe/ARCHITECTURE.md + ${LIB}/README.md first; import via sys.path.insert(0, '${LIB}'). Use toe.causet (sprinkling, iDelta, BD), toe.sj (sj_state), toe.entropy (ssee, n_max prescriptions), toe.vntype (modular_spectrum, pile_up, trace_scaling, saturation_discriminator), toe.fits (powerlaw_fit with SE+CI), toe.viz (panels). Where the library lacks a needed piece, follow YOUR extension rule given below. Every Measurement/FitResult you report should carry (value, SE/CI) per the library convention. Machine-precision invariant: iDelta +/- eigenvalue pairing < 1e-12 on every new region (assert it).

Deliverables: <dir>/calc.py (thin composition over toe), <dir>/results.json (EN), plots, Czech writeup in ${KB}/vypocty/. Runtime budget ~10-15 min per full run; N caps below.

YOUR TASK: `

phase('Výpočty')
log('Kolo 10: VYPOCET-21 (4D dS II₁ area-law diskriminátor) + VYPOCET-22 (codim-2 spoj) — první ostří konzumenti lib/toe…')

const batch = await parallel([
  // --- VYPOCET-21: H5g-1 ---
  () => agent(CALC_COMMON + `VYPOCET-21 — TEST H5g-1 (BRAINSTORM-05, high priority): in the 4D dS static patch the TRUNCATED area-law SSEE S~sqrt(N) should ITSELF separate type II_1 (saturates as the region exhausts the bounded patch) from II_infinity (grows on the flat control) — unlike 2D where only region content discriminated (F-023, VYPOCET-19; read ${KB}/vypocty/VYPOCET-19-desitter-II1.md + ${CD}/calculations/sj-desitter-type/calc.py for the validated 2D protocol and the sech^2 proper-measure convention).

PLAN: (1) Build a 4D sech^2-weighted slab region (t, r*, x_perp1, x_perp2): flat conformal causal order in (t, r*), transverse box, sprinkling measure carrying the sech^2(r*/l) proper-density factor — the 4D analog of toe.causet.sprinkle_ds_static_patch2d. LIBRARY EXTENSION RULE for you: ADD sprinkle_ds_static_patch4d (+ any helper) to ${LIB}/toe/causet.py following ARCHITECTURE.md conventions exactly (docstring Formula/Evidence/Conventions tags, explicit rng), plus validation tests appended as a NEW file ${ROOT}/app/tests/test_toe_causet_ds4d.py (pairing invariant + sech^2 marginal monotonicity; <30 s). You own causet.py this round — no one else edits it. Run that test + the existing test_toe_causet.py to prove no regression.
(2) iDelta via the 4D link-matrix Green (toe.causet.green_retarded_4d) on the conformal order — document the conformal-weight caveat honestly (4D massless scalar is NOT conformally invariant; this is the same controlled approximation as VYPOCET-19's 2D trick lifted to 4D, state it as such and cite what it preserves: causal structure + measure, not the exact propagator).
(3) Protocol: fixed proper density rho, box edge R*_box growing toward the horizon (>=6 steps), dS vs flat control at matched density; truncated SSEE with n_max = 2*N^(3/4) (toe.entropy, F-019 regulator); also track region content N_total and S_full as the VYPOCET-19 cross-check.
(4) DISCRIMINATOR: dS truncated-S late-slope -> 0 (saturation; fit via toe.fits.powerlaw_fit + saturating fit, compare AIC) vs flat late-slope > 0. Use toe.vntype.saturation_discriminator where it fits.
(5) Scaling cross-check at fixed region: S_trunc ~ N^a with a ~ 1/2 (4D area law, F-019) on the dS patch.
N <= 2500 dense eigh, >= 4 seeds (toe handles seeds explicitly). HONEST NULL: if the 4D truncated entropy does NOT separate types (e.g. transverse dilution kills the signal), quantify why and what N/geometry would be needed — that kills the strong H5g-1 and informs H5g-6 (draft-05 decision) either way.
Deliverables dir: ${CD}/calculations/sj-desitter-4d/; writeup VYPOCET-21-desitter-4d-area-law.md. In results.json include a "h5g6_input" key: one-paragraph EN assessment whether F-023+F-019+this result warrant a standalone draft-05 or a dS section in draft-04.`,
    { label: 'calc:desitter-4d', phase: 'Výpočty', model: 'opus', schema: CALC_RESULT }),

  // --- VYPOCET-22: H5g-3 ---
  () => agent(CALC_COMMON + `VYPOCET-22 — TEST H5g-3 (BRAINSTORM-05, medium-high): the 2D corner mechanism of H4g-1 fails at the 4D diamond null-tip (F-024, VYPOCET-20) because the tip is a degenerating 2-sphere; the right 4D locus of modular-flow non-geometricity should be a CODIM-2 JOINT (wedge edge), not an isolated tip. Read ${KB}/vypocty/VYPOCET-20-modularni-tok-bd-4d.md + ${CD}/calculations/modular-flow-bd-4d/calc.py (the BD smeared eps=0.6 object validated there, and the modular-kernel geometricity diagnostics: off-diagonal decay slope, per-site non-locality f_nl) and ${KB}/vypocty/VYPOCET-18-modularni-tok-roh.md (2D reference numbers: f_nl slope vs distance-to-corner = -0.383, R^2=0.989).

PLAN: (1) Build a 4D region with a genuine codim-2 joint: two half-space cuts intersecting along a codim-2 edge (wedge geometry W = {x1 > 0} cap {t < x1 tan(alpha)} style — design the cleanest version where the joint is a flat 2-plane, and a control slab with no joint at matched volume/density). LIBRARY EXTENSION RULE for you: keep ALL new region/diagnostic helpers LOCAL to your calc dir (calc.py or helpers.py) — do NOT edit ${LIB}/toe/*.py this round (VYPOCET-21 owns causet.py); instead propose migrations in your writeup + results.json "lib_proposals" key (signatures ready to lift).
(2) Object: BD smeared eps=0.6 iDelta (compose from toe.causet.bd_dalembertian_inverse / the VYPOCET-20 recipe); SJ state via toe.sj; modular kernel of the wedge cut.
(3) Diagnostics (mirror VYPOCET-18/20 so numbers are comparable): per-site non-locality f_nl vs distance-to-joint (the 2D corner signature was slope < 0, monotone growth toward the corner); off-diagonal kernel decay slope wedge vs slab control; diagonal boost-linearity along the wedge Rindler direction (Bisognano-Wichmann check away from the joint).
(4) DISCRIMINATOR: f_nl grows toward the codim-2 joint (slope < 0, like the 2D corner) => the corner mechanism is codim-2-generic and H4g-1 layer B generalizes to 4D; f_nl falls (like the 4D tip, slope +0.71 in F-024) => corner-subpart is genuinely 2D-only. Either is a finding; quantify with toe.fits (value, SE, CI) and >= 3 seeds, N <= 2200 (matrix-inversion bound).
Deliverables dir: ${CD}/calculations/modular-flow-codim2/; writeup VYPOCET-22-modularni-tok-codim2.md.`,
    { label: 'calc:codim2-joint', phase: 'Výpočty', model: 'opus', schema: CALC_RESULT }),
])

const calc21 = batch[0]
const calc22 = batch[1]
log('Výpočty hotovy (V21: ' + (calc21 ? calc21.status : 'N/A') + ', V22: ' + (calc22 ? calc22.status : 'N/A') + '). Úklid…')

phase('Úklid')

const hkData = JSON.stringify({
  calc21: calc21 ? { status: calc21.status, keyNumbers: calc21.keyNumbers, verdict: calc21.verdictForHypothesis, lib: calc21.libUsage } : null,
  calc22: calc22 ? { status: calc22.status, keyNumbers: calc22.keyNumbers, verdict: calc22.verdictForHypothesis, lib: calc22.libUsage } : null,
}, null, 2)

const housekeeping = await agent(`You are the housekeeping agent at ${ROOT}. Today ${DATE}. Czech prose / English data. ECONOMY MODE. Round-10 results (first lib/toe-powered research round):
${hkData}

TASK 1: Update ${CD}/findings.json — append F-025 (H5g-1 verdict: does 4D dS truncated area-law SSEE separate II_1 vs II_infinity?) and F-026 (H5g-3 verdict: codim-2 joint vs 2D-only corner mechanism). Conservative status wording per the audit conventions (supported/partial/refuted; caveats field; evidence paths must be REAL — verify with ls).
TASK 2: Verify the full test suite still passes: cd ${ROOT} && MPLBACKEND=Agg python3 -m pytest app/tests -q (VYPOCET-21 extended lib/toe/causet.py). If it fails, report precisely — do NOT weaken tests.
TASK 3: Update ${ROOT}/PROGRESS.md (Read first, preserve): log entry kolo 10; banner update (kolo 10 hotovo, libusage poznámka); "Další kroky" per outcomes (H5g-6 draft-05 decision input from calc21 results.json h5g6_input; lib_proposals from calc22).
TASK 4: Update ${KB}/00-INDEX.md (VYPOCET-21/22 do sekce výpočtů) and append short status notes to ${KB}/BRAINSTORM-05.md next to H5g-1 and H5g-3 (one line each: tested in round 10, verdict, finding id — follow the correction-note style used elsewhere in the file).
Return 4-line Czech confirmation.`,
  { label: 'final:round10', phase: 'Úklid', model: 'sonnet' })

return {
  calc21: calc21 ? { status: calc21.status, keyNumbers: calc21.keyNumbers, verdict: calc21.verdictForHypothesis, lib: calc21.libUsage } : null,
  calc22: calc22 ? { status: calc22.status, keyNumbers: calc22.keyNumbers, verdict: calc22.verdictForHypothesis, lib: calc22.libUsage } : null,
  housekeeping: housekeeping,
}
