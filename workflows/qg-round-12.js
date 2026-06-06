export const meta = {
  name: 'qg-round-12',
  description: 'Kolo 12 (H5g-2 + tracial retry): sparse mašinérie toe v0.3.0 (eigsh pipeline ρ~10³⁻⁴), VYPOCET-23 A/4 strop kalibrace na 2D dS, VYPOCET-24 vysokohustotní tracialní sonda',
  phases: [
    { title: 'Mašinérie', detail: 'toe v0.3.0: sparse/eigsh cesta + validace proti dense', model: 'opus' },
    { title: 'Výpočty', detail: 'VYPOCET-23 (A/4 strop) + VYPOCET-24 (tracialní sonda) paralelně', model: 'opus' },
    { title: 'Úklid', detail: 'findings, PROGRESS, INDEX, BRAINSTORM-05, web rebuild', model: 'sonnet' },
  ],
}

const ROOT = '/Users/pazny/projects/theoryOfEverything'
const CD = ROOT + '/core-data'
const KB = ROOT + '/knowledge-base'
const LIB = ROOT + '/lib'
const DATE = (args && args.date) || '2026-06-06'

const RESULT = {
  type: 'object',
  properties: {
    status: { type: 'string', description: 'success | partial | failed' },
    keyNumbers: { type: 'string' },
    verdict: { type: 'string', description: 'Czech, 2-4 sentences' },
    files: { type: 'array', items: { type: 'string' } },
  },
  required: ['status', 'keyNumbers', 'verdict', 'files'],
}

// ---------------- phase 1: sparse machinery ----------------
phase('Mašinérie')
log('Stavím sparse/eigsh cestu (toe v0.3.0) pro hustoty ρ~10³–10⁴…')

const machinery = await agent(`You are the library maintainer at ${ROOT}. Code+comments ENGLISH; ARCHITECTURE.md conventions (Formula/Evidence/Conventions docstrings, explicit rng, Result dataclasses, layers). GOAL: extend ${LIB}/toe to v0.3.0 with a SPARSE/ITERATIVE path so SJ+SSEE pipelines reach N~10^4 (sprinkling density rho~10^3-10^4 in 2D), needed by H5g-2 (A/4 cap) and the VYPOCET-19 Part-3 tracial probe. Read ${LIB}/toe/ARCHITECTURE.md + causet.py + sj.py + entropy.py + vntype.py first.

DESIGN (keep it minimal and validated, no premature generality):
1. toe.causet: memory-lean causal order for large N — sort-by-time + per-pair lightcone check done blockwise (numpy bool blocks, avoid the full N^2 python loop; target N=12000 2D diamond build < 60 s, < 2 GB). The 2D Green G_R = C/2 stays implicit: provide a LinearOperator-style matvec for iDelta = i(G_R - G_R^T) built from the causal blocks WITHOUT materializing a dense float matrix (bool blocks @ vector, scaled).
2. toe.sj: sj_state_sparse(idelta_op, k, ...) using scipy.sparse.linalg.eigsh on the Hermitian operator to get the TOP-k spectral part (k ~ few x N^(3/4)); returns the same SJState shape (eigenvalues, modes) as the dense path. Seed/determinism: eigsh v0 vector must be derived from the rng (deterministic restarts).
3. toe.entropy: ssee_sparse / truncated entropy from the k-mode SJ data on a region cut; n_max prescriptions reused.
4. VALIDATION (the heart of this task): at OVERLAP sizes (N in {1000, 2000}) the sparse path must match the dense path: top-k eigenvalues rel diff < 1e-8; truncated SSEE S_trunc rel diff < 1e-6; +/- pairing invariant on the operator (apply to random vectors). Write app/tests/test_toe_sparse.py covering these (< 90 s — pick smallest convincing sizes). Also ONE scaling smoke: N=8000 2D diamond, k=600 eigsh completes < 120 s and top eigenvalue matches the dense N=2000 trend (loose).
5. Bump __version__='0.3.0', exports, CHANGELOG in lib/README.md (Czech) + ARCHITECTURE.md §6 (English). FULL suite green: cd ${ROOT} && MPLBACKEND=Agg python3 -m pytest app/tests -q.
HONESTY: if eigsh on the implicit operator turns out ill-suited (e.g. needs too many iterations for interior eigenvalues), document the limitation and fall back to dense-blocked partial eigh via scipy.linalg.eigh(subset_by_index=...) on float32 blocks — choose what actually validates, report which path won and why. Return status, keyNumbers (timings, validation diffs), verdict (Czech), files.`,
  { label: 'lib:sparse-v0.3', phase: 'Mašinérie', model: 'opus', schema: RESULT })

log('Mašinérie: ' + machinery.status + '. Spouštím VYPOCET-23 + VYPOCET-24…')

// ---------------- phase 2: calculations ----------------
phase('Výpočty')

const CALC_COMMON = `You are a computational physics agent at ${ROOT}. python3 + numpy/scipy/sympy/matplotlib (Agg). NEVER fudge results; honest nulls are findings. Build on ${LIB}/toe v0.3.0 (read lib/toe/ARCHITECTURE.md §6 + the new sparse API in causet/sj/entropy; import via sys.path.insert(0,'${LIB}')). Machinery validation report: ${JSON.stringify(machinery.keyNumbers)}. Use the sparse path for N>2500, dense below; every reported number carries (value, SE/CI) via toe.fits. Assert the +/- pairing invariant on every region. Deliverables: <dir>/calc.py (thin over toe), <dir>/results.json (EN), plots, Czech writeup in ${KB}/vypocty/. Runtime budget ~25 min.

YOUR TASK: `

const batch = await parallel([
  // --- VYPOCET-23: H5g-2 A/4 cap ---
  () => agent(CALC_COMMON + `VYPOCET-23 — TEST H5g-2 (BRAINSTORM-05, high): does the finite cap that bounded-dS-patch entropy saturates to (F-023) map QUANTITATIVELY onto Gibbons-Hawking A/4 — i.e. a discrete first-principles dS entropy? 2D contour first (A/4 is O(1) there: the 2D 'horizon area' is a point pair, S_GH = A/4G -> dimensionless O(1) in causal-set units — work out the correct 2D statement carefully and STATE it; cite only repo-present references: 2206.10780 CLPW, gr-qc/0205058-style Gibbons-Hawking is NOT in repo — check references.json for the dS entropy source actually present and use that; if none, mark the formula source '⚠️ neověřeno' per policy and proceed with the dimensionless ratio).
ANTI-CIRCULARITY PROTOCOL (mandatory, from BRAINSTORM-05): FIX the discreteness-scale calibration epsilon ~ rho^(-1/2) from the INDEPENDENT F-006 result (ssee-diamond: SSEE cutoff rank ~ N^0.519, epsilon ~ rho^(-1/2); read ${CD}/calculations/ssee-diamond/results.json) BEFORE measuring the ratio — never tune epsilon to make the ratio 1/4.
PLAN: (1) 2D dS static patch (toe.causet.sprinkle_ds_static_patch2d), protocol of VYPOCET-19 Part 1 but at densities rho in {240, 10^3, 3x10^3, 10^4} (sparse path above N~2500); (2) measure the saturated cap of (a) content N_total and (b) truncated entropy S_trunc as the region exhausts the patch (saturating fit, toe.fits + AIC vs linear); (3) express the cap in horizon units: ratio R(rho, l) = S_cap / (horizon 'area' in epsilon units) with epsilon FIXED per the protocol; scan l (patch size) at fixed rho for >= 3 values; (4) DISCRIMINATOR: R constant across (rho, l) -> quantitative A/4-like law (report the constant with CI; is it ~1/4?); R drifts -> the cap is qualitative only (kill the strong H5g-2, document the drift law). >= 4 seeds at low rho, >= 2 at rho=10^4 (runtime). Deliverables dir: ${CD}/calculations/ds-entropy-cap/; writeup VYPOCET-23-ds-entropy-cap.md.`,
    { label: 'calc:ds-entropy-cap', phase: 'Výpočty', model: 'opus', schema: RESULT }),

  // --- VYPOCET-24: tracial probe retry ---
  () => agent(CALC_COMMON + `VYPOCET-24 — retry the HONEST NULL of VYPOCET-19 Part 3 (read ${KB}/vypocty/VYPOCET-19-desitter-II1.md + ${CD}/calculations/sj-desitter-type/results.json): the max-entropy TRACIAL state signature of type II_1 (untruncated modular-spectrum IR fraction should GROW toward the tracial accumulation as the bounded dS patch fills) was invisible at N<=2500; the documented scaling said rho~10^3-10^4 is needed. NOW WE HAVE IT (sparse path).
PLAN: (1) 2D dS static patch + flat control at matched density, rho in {10^3, 3x10^3, 10^4} (sparse eigsh: you need INTERIOR/small-eigenvalue info for the IR fraction — if eigsh struggles there, use the dense-blocked partial eigh fallback the machinery documented, or compute the IR fraction from moments/trace estimators (Hutchinson) honestly — explain the estimator and its error); (2) observables vs growing region: IR fraction of the modular spectrum (eps < 0.5), spectral weight near the maximally-mixed point, mode-count growth exponent; dS must SATURATE/accumulate vs flat must keep growing if the II_1 tracial signature is real; (3) verdict with CIs: does the tracial signature emerge at high density (closing the VYPOCET-19 Part-3 gap), or does the null persist (then the II_1 identification rests on content saturation alone — document what density/size WOULD be needed or why the discrete probe cannot see it in principle). >= 3 seeds at 10^3, >= 2 at 10^4. Deliverables dir: ${CD}/calculations/ds-tracial-probe/; writeup VYPOCET-24-ds-tracial-probe.md.`,
    { label: 'calc:tracial-probe', phase: 'Výpočty', model: 'opus', schema: RESULT }),
])

const calc23 = batch[0]
const calc24 = batch[1]
log('Výpočty hotovy (V23: ' + (calc23 ? calc23.status : 'N/A') + ', V24: ' + (calc24 ? calc24.status : 'N/A') + '). Úklid…')

// ---------------- phase 3: housekeeping ----------------
phase('Úklid')

const hk = await agent(`You are the housekeeping agent at ${ROOT}. Today ${DATE}. Czech prose / English data. ECONOMY MODE. Round-12 results:
${JSON.stringify({ machinery: machinery ? { status: machinery.status, keyNumbers: machinery.keyNumbers } : null, calc23: calc23 ? { status: calc23.status, keyNumbers: calc23.keyNumbers, verdict: calc23.verdict } : null, calc24: calc24 ? { status: calc24.status, keyNumbers: calc24.keyNumbers, verdict: calc24.verdict } : null }, null, 1)}

TASK 1: Update ${CD}/findings.json — F-027 (H5g-2 A/4 cap verdict) + F-028 (tracial probe at high density; closes or re-confirms the VYPOCET-19 Part-3 gap). Conservative statuses, caveats, REAL evidence paths (verify ls).
TASK 2: Full suite check: cd ${ROOT} && MPLBACKEND=Agg python3 -m pytest app/tests -q (toe v0.3.0 added sparse tests). Report tally.
TASK 3: Update ${ROOT}/PROGRESS.md (Read first): log entry kolo 12; banner. If V23/V24 results materially affect draft-04 §4.3 claims (e.g. tracial null closed), add a TODO note to papers/draft-04-.../TODO.md §7b instead of editing the draft.
TASK 4: ${KB}/00-INDEX.md (VYPOCET-23/24); BRAINSTORM-05.md status note u H5g-2 (correction-note style). Then rebuild the site: python3 ${ROOT}/web/build.py (report page count).
Return 4-line Czech confirmation.`,
  { label: 'final:round12', phase: 'Úklid', model: 'sonnet' })

return {
  machinery: machinery ? { status: machinery.status, keyNumbers: machinery.keyNumbers, verdict: machinery.verdict } : null,
  calc23: calc23 ? { status: calc23.status, keyNumbers: calc23.keyNumbers, verdict: calc23.verdict } : null,
  calc24: calc24 ? { status: calc24.status, keyNumbers: calc24.keyNumbers, verdict: calc24.verdict } : null,
  housekeeping: hk,
}
