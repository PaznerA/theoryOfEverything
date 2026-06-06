export const meta = {
  name: 'qg-round-11',
  description: 'Kolo 11 (konsolidace): toe v0.2.0 — povýšení 5 lib_proposals z VYPOCET-22; dS sekce do draftu-04 (rozhodnutí H5g-6 z F-023+F-025); web rebuild',
  phases: [
    { title: 'Konsolidace', detail: 'toe v0.2.0 + draft-04 dS sekce paralelně', model: 'opus' },
    { title: 'Úklid', detail: 'PROGRESS, INDEX, web rebuild', model: 'sonnet' },
  ],
}

const ROOT = '/Users/pazny/projects/theoryOfEverything'
const CD = ROOT + '/core-data'
const LIB = ROOT + '/lib'
const DATE = (args && args.date) || '2026-06-06'

const RESULT = {
  type: 'object',
  properties: {
    status: { type: 'string', description: 'success | partial | failed' },
    keyPoints: { type: 'array', items: { type: 'string' }, description: 'Czech' },
    testsTally: { type: 'string' },
    files: { type: 'array', items: { type: 'string' } },
  },
  required: ['status', 'keyPoints', 'testsTally', 'files'],
}

phase('Konsolidace')
log('toe v0.2.0 (5 migrací z VYPOCET-22) + draft-04 dS sekce…')

const batch = await parallel([
  // --- A: toe v0.2.0 ---
  () => agent(`You are the library maintainer at ${ROOT}. Code+comments ENGLISH. Task: lift the 5 ready-to-lift migration proposals from VYPOCET-22 into ${LIB}/toe v0.2.0. Read first: ${CD}/calculations/modular-flow-codim2/results.json key "lib_proposals" (signatures) + ${CD}/calculations/modular-flow-codim2/helpers.py (the working local implementations) + ${LIB}/toe/ARCHITECTURE.md (conventions: Formula/Evidence/Conventions docstrings, explicit rng, Result dataclasses, layer rules A/B/C).

MIGRATIONS (respect layers; follow the proposal signatures unless they violate ARCHITECTURE.md — then adapt and note):
1. toe.causet.sprinkle_wedge_box4d — 4D wedge region with a flat codim-2 joint + matched no-joint slab control (layer A).
2. toe.causet.bd_smeared_dalembertian_inverse — the smeared eps BD d'Alembertian (VYPOCET-20-validated object; sharp variant already exists).
3. toe.sj.sj_state rel_floor parameter — relative spectral floor for ill-conditioned BD inverses (cond~1e5); default must keep ALL existing behavior bit-identical (default None/old path — prove via the existing test suite).
4. toe.entropy.modular_kernel — expose the site-basis modular kernel K (not just scalar S) for locality diagnostics (layer C).
5. toe.viz.nl_vs_locus — non-locality vs distance-to-locus panel (layer A, imports only toe.fits).

REQUIREMENTS: each migration gets validation tests in app/tests/ (new test files or extend test_toe_<module>.py): wedge builder must satisfy the iDelta +/- pairing invariant < 1e-12; bd_smeared must reproduce a committed number from modular-flow-bd-4d/results.json or modular-flow-codim2/results.json (read and pick a real target, generous tolerance, < 60 s); modular_kernel must be consistent with ssee's scalar S on the same cut (trace relation). Refactor ${CD}/calculations/modular-flow-codim2/calc.py to import the lifted functions from toe instead of helpers.py ONLY IF the numbers stay identical (run it and diff results.json — if anything shifts, leave calc.py untouched and report why). Bump ${LIB}/toe/__init__.py __version__='0.2.0', update exports, append a CHANGELOG section to ${LIB}/README.md (Czech) and ARCHITECTURE.md (English, brief). FULL suite must stay green: cd ${ROOT} && MPLBACKEND=Agg python3 -m pytest app/tests -q. Return status, keyPoints (Czech), testsTally, files.`,
    { label: 'lib:toe-v0.2', phase: 'Konsolidace', model: 'opus', schema: RESULT }),

  // --- B: draft-04 dS section ---
  () => agent(`You are a scientific-draft editor at ${ROOT}. Draft text ENGLISH (it is a paper draft); TODO/REVIZE notes follow existing bilingual style. NEVER invent arXiv IDs; cite only IDs already in the repo. The paper is an INTERNAL AI-assisted draft — line 1 banner must stay intact.

TASK: implement the H5g-6 decision (round 10): add a DE SITTER section to ${ROOT}/papers/draft-04-type-transition-causal-sets/draft.md (NOT a standalone draft-05). Sources to read first: ${CD}/findings.json entries F-023 + F-025 (statuses + caveats — the section must not overstate them), knowledge-base/vypocty/VYPOCET-19-desitter-II1.md + VYPOCET-21-desitter-4d-area-law.md, ${CD}/calculations/sj-desitter-type/results.json + sj-desitter-4d/results.json (exact numbers), and the existing draft.md structure (where the section fits — likely after the 4D slab section).

CONTENT (conservative, statuses verbatim from findings): (a) motivation: CLPW predicts the dS static-patch algebra is II_1 (normalizable trace) vs II_infinity for black-hole/flat cases — a sharper target than the bare III->II transition; (b) 2D result (F-023, supported): content-tracking quantities saturate on the bounded patch (N_total cap 480.1, R2=1.000; S_full saturates-and-turns-over) vs flat control growth — the discrete SJ probe SEES the II_1/II_infinity distinction; honest limit: 2D truncated SSEE is log-flat in both, distinction lives in content; Part-3 tracial probe honest null with documented rho~1e3-1e4 scaling; (c) 4D result (F-025, partial): truncated area-law SSEE rises ~3x shallower on dS (exponent 0.27 vs 0.52) — a real 4D-specific signal absent in 2D — but full saturation NOT reached at N<=2500 (dense-eigh bound); content discriminator lifts cleanly to 4D; S_trunc~N^0.717+-0.029 at fixed region (above the 0.5 slab target — dS radial geometry steepens the area law; the matched-control reproduction a=0.58 vs committed 0.547 validates the pipeline); (d) conformal-weight caveat stated plainly (4D massless scalar not conformally invariant; the construction preserves causal structure + measure, not the exact propagator); (e) outlook: sparse eigensolvers rho~1e3-1e4 for clean saturation + the A/4 cap question (H5g-2, cite as open).

ALSO: update the section map/abstract mention if the draft has one; extend ${ROOT}/papers/draft-04-type-transition-causal-sets/TODO.md with the new section's human-verification checkboxes (re-derive the saturating fits from results.json, verify the conformal caveat wording, check F-023/F-025 statuses match findings.json); add the matching checkbox row to ${ROOT}/papers/REVIZE-PRO-CLOVEKA.md draft-04 block + bump its revision-time estimate; note in both that the section is round-10/11 provenance. Do NOT touch any numbers outside the new section. Return status, keyPoints (Czech), testsTally='n/a', files.`,
    { label: 'draft04:ds-section', phase: 'Konsolidace', model: 'opus', schema: RESULT }),
])

const lib = batch[0]
const draft = batch[1]
log('Konsolidace hotova (lib: ' + (lib ? lib.status : 'N/A') + ', draft: ' + (draft ? draft.status : 'N/A') + '). Úklid + web rebuild…')

phase('Úklid')

const hk = await agent(`You are the housekeeping agent at ${ROOT}. Today ${DATE}. Czech prose / English data. ECONOMY MODE. Round-11 results:
${JSON.stringify({ lib: lib ? { status: lib.status, keyPoints: lib.keyPoints, tests: lib.testsTally } : null, draft: draft ? { status: draft.status, keyPoints: draft.keyPoints } : null }, null, 1)}

TASK 1: Verify full suite: cd ${ROOT} && MPLBACKEND=Agg python3 -m pytest app/tests -q (report tally; do not weaken anything).
TASK 2: Rebuild the site so it reflects round 11: python3 ${ROOT}/web/build.py (report page count).
TASK 3: Update ${ROOT}/PROGRESS.md (Read first, preserve): log entry kolo 11 (toe v0.2.0 — 5 migrací z VYPOCET-22; draft-04 dS sekce per H5g-6); banner one-liner update.
TASK 4: Update ${ROOT}/knowledge-base/00-INDEX.md where relevant (lib version, draft-04 anotace o dS sekci).
Return 4-line Czech confirmation.`,
  { label: 'final:round11', phase: 'Úklid', model: 'sonnet' })

return { lib: lib, draft: draft, housekeeping: hk }
