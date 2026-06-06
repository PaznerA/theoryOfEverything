export const meta = {
  name: 'qg-round-05',
  description: 'Kolo 5: VYPOCET-11 graviton sektor + index test (odblokování draft-02), VYPOCET-12 vN typ SJ truncace (test H3g-3), finalizace draft-01 v0.2, úklid',
  phases: [
    { title: 'Jádro kola', detail: '2 výpočty + finalizace draftu-01 paralelně' },
    { title: 'Úklid', detail: 'findings, PROGRESS, INDEX', model: 'sonnet' },
  ],
}

const ROOT = '/Users/pazny/projects/theoryOfEverything'
const CD = ROOT + '/core-data'
const KB = ROOT + '/knowledge-base'
const DATE = (args && args.date) || '2026-06-06'

const CALC_RESULT = {
  type: 'object',
  properties: {
    name: { type: 'string' },
    status: { type: 'string', description: 'success | partial | failed' },
    keyNumbers: { type: 'string' },
    verdictForHypothesis: { type: 'string', description: 'Czech, 2-4 sentences' },
    files: { type: 'array', items: { type: 'string' } },
  },
  required: ['name', 'status', 'keyNumbers', 'verdictForHypothesis', 'files'],
}

const NOTE_RESULT = {
  type: 'object',
  properties: {
    file: { type: 'string' },
    keyPoints: { type: 'array', items: { type: 'string' }, description: 'Czech' },
  },
  required: ['file', 'keyPoints'],
}

const CALC_COMMON = `You are a computational physics agent at ${ROOT}. Environment: python3 + numpy/scipy/sympy/matplotlib (Agg). Verify all conventions against literature (ToolSearch "select:WebFetch,WebSearch"). NEVER fudge results — clean mismatches are first-class findings. Deliverables: <dir>/calc.py, <dir>/results.json (EN), plots, Czech writeup in ${KB}/vypocty/.

YOUR TASK: `

phase('Jádro kola')
log('Spouštím graviton test, vN-typ test a finalizaci draftu-01…')

const batch = await parallel([
  // --- VYPOCET-11: graviton sector + index test (unblocks draft-02) ---
  () => agent(CALC_COMMON + `VYPOCET-11 — the two blockers of draft-02 per BRAINSTORM-03 (read its "Výpočetní fronta" items #1 and #7, plus ${KB}/BRAINSTORM-03.md section on H3g-4, ${KB}/vypocty/VYPOCET-02-a4-matching.md, and ${ROOT}/papers/draft-02-a4-fermionic-identity/draft.md + TODO.md):
PART 1 — GRAVITON SECTOR: hypothesis H3g-4 says the spectral action is fermion-induced gravity, so bosons (incl. graviton) are NOT part of the a₄ identity. Test: compute with sympy exact rationals the trace-anomaly (a,c) contribution of the GRAVITON itself (known literature values — verify against Christensen-Duff Nucl.Phys.B 1980 / Duff 2003.02688: graviton a,c in 4D) and of the SM gauge+Higgs bosons; show explicitly: (i) what c/(−a) the graviton has, (ii) whether ANY consistent assignment of "induced" vs "fundamental" sectors can restore the −18/11 identity for the full theory, or whether the identity strictly delimits the Dirac sector (which is the H3g-4 claim — gravity+bosons live on the INDUCED side of the ledger, fermions are the only fundamental loops). (iii) Sakharov consistency check: in induced-gravity logic the graviton does NOT run in the loops that induce the action — formalize what that predicts for the anomaly ledger and whether it is internally consistent.
PART 2 — INDEX-THEOREM CROSS-CHECK: the −18/11 identity should have an index-theoretic shadow: the a₄ coefficient of the Dirac operator relates to the Â-genus/Gauss-Bonnet densities. Verify with sympy: express a₄(D²) for the Dirac operator in the standard basis {C², E₄, R², □R}, confirm the −18/11 emerges from the Â-genus structure, and check against the Atiyah-Singer index density (the E₄ coefficient must reproduce the index theorem normalization — a nontrivial consistency lock). Document which parts are textbook and which constitute the note's added value. Deliverables dir: ${CD}/calculations/a4-graviton-index/; writeup VYPOCET-11-graviton-index.md. If results strengthen/weaken draft-02, append a short dated note to its TODO.md.`,
    { label: 'calc:a4-graviton-index', phase: 'Jádro kola', model: 'opus', schema: CALC_RESULT }),

  // --- VYPOCET-12: von Neumann type diagnostics of SJ truncation (H3g-3) ---
  () => agent(CALC_COMMON + `VYPOCET-12 — numerical von Neumann TYPE diagnostics of the SSEE truncation (test of H3g-3, see ${KB}/BRAINSTORM-03.md and ${KB}/hypotezy/H04-entropy-cluster-reframe.md; data+code: ${CD}/calculations/ssee-diamond/ for clean 2D). CLAIM under test: the truncation that converts volume-law → area-law IS a type III₁ → type II transition (the discreteness scale = modular/observer cutoff). Since "type" is an infinite-dimensional notion, design HONEST finite-N proxies and measure their N-scaling — the signature is in the TREND: (1) TRACE DIVERGENCE: Tr over the SJ-restricted two-point operator (untruncated) should grow without bound with N (III-like, no trace) while the truncated one converges (II-like finite trace) — measure both vs N; (2) MODULAR SPECTRUM: for the reduced Gaussian state on a subdiamond, compute the modular Hamiltonian spectrum (h = ln[(1+...)/...] from the covariance eigenvalues — use the standard Gaussian-state formalism, verify formulas via Sorkin 1611.10281 / Casini-Huerta reviews); type III₁ signature = modular spectrum filling all of R densely with flat Connes-invariant density (S(M)=R₊), type II = integrable density; measure the spectral density evolution with N, before vs after truncation; (3) CENTRAL SEQUENCES proxy: independence of the truncated algebra's entropy from boundary microstructure across seeds (factor-like behavior). For each proxy: clear prediction, measurement, error bars across ≥4 seeds, N=400..1800 (2D — the clean case). VERDICT: does the truncation behave like III→II in ALL proxies, some, none? This is the first numerical probe of the crossed-product picture on causal sets — negative/mixed results equally valuable. Deliverables dir: ${CD}/calculations/sj-vn-type/; writeup VYPOCET-12-vn-typ-truncace.md.`,
    { label: 'calc:sj-vn-type', phase: 'Jádro kola', model: 'opus', schema: CALC_RESULT }),

  // --- draft-01 finalization v0.2 ---
  () => agent(`You are an editorial physics agent (ECONOMY MODE) at ${ROOT}. VYPOCET-10 just SOLVED the weakest points of papers/draft-01-sj-rotating-spacetimes/ (mechanism of opposite signs verified ~99%; superradiant eigenvector signature with exact static zero; ~45° subspace rotation at <2% spectrum change) and appended a "Mechanism" v0.2 subsection. Read: the current draft.md + TODO.md, ${KB}/vypocty/VYPOCET-10-superradiance-eigenvektory.md, ${CD}/calculations/sj-eigenvector-superradiance/results.json.
TASKS: (1) EDIT draft.md into a coherent v0.2: integrate the mechanism + superradiance results into Abstract, Results and Discussion (not just an appended subsection); update the title if the superradiance result deserves it (e.g. "...numerical construction through the ergoregion and an eigenvector signature of superradiance"); keep the line-1 NOT-submitted directive, bump to "DRAFT v0.2". (2) Update TODO.md: mark items resolved by VYPOCET-10 as ✅ DONE (with pointer), re-rank what remains (convergence study, φ-periodicity, citation verification against PDFs, human re-derivation, ethics note). (3) Verify internal consistency: every number quoted in the draft must match results.json sources — fix discrepancies, list any you found. Return structured result (file = draft path, keyPoints in Czech: co se změnilo, co zbývá).`,
    { label: 'paper:draft-01-v02', phase: 'Jádro kola', model: 'sonnet', schema: NOTE_RESULT }),
])

const calc11 = batch[0]
const calc12 = batch[1]
const draft01v2 = batch[2]
log('Jádro hotovo (graviton: ' + (calc11 ? calc11.status : 'N/A') + ', vN-typ: ' + (calc12 ? calc12.status : 'N/A') + '). Úklid…')

phase('Úklid')

const hkData = JSON.stringify({
  calc11: calc11 ? { status: calc11.status, keyNumbers: calc11.keyNumbers, verdict: calc11.verdictForHypothesis } : null,
  calc12: calc12 ? { status: calc12.status, keyNumbers: calc12.keyNumbers, verdict: calc12.verdictForHypothesis } : null,
  draft01v2: draft01v2,
}, null, 2)

const housekeeping = await agent(`You are the housekeeping agent at ${ROOT}. Today ${DATE}. Czech prose / English data. ECONOMY MODE. Round-5 results:
${hkData}

TASK 1: Update ${CD}/findings.json — append round-5 findings (graviton/index outcome for the a₄ identity; vN-type proxy verdicts for SSEE truncation; draft-01 v0.2). Conservative wording, evidence paths.
TASK 2: Update ${ROOT}/PROGRESS.md (Read first, preserve): log entry round 5; "Aktuální stav"; "Další kroky" — reflect what VYPOCET-11 means for draft-02 release readiness and what VYPOCET-12 means for H3g-3.
TASK 3: Update ${KB}/00-INDEX.md: add VYPOCET-11/12 + draft-01 v0.2 note.
Return 3-line Czech confirmation.`,
  { label: 'final:round5-writeup', phase: 'Úklid', model: 'sonnet' })

return {
  calc11: calc11 ? { status: calc11.status, keyNumbers: calc11.keyNumbers } : null,
  calc11Verdict: calc11 ? calc11.verdictForHypothesis : null,
  calc12: calc12 ? { status: calc12.status, keyNumbers: calc12.keyNumbers } : null,
  calc12Verdict: calc12 ? calc12.verdictForHypothesis : null,
  draft01v2: draft01v2,
  housekeeping: housekeeping,
}