export const meta = {
  name: 'qg-round-08',
  description: 'Kolo 8: VYPOCET-17 fermionová indukce → Λ (H4g-3), VYPOCET-18 modulární tok slab vs roh diamantu (H4g-1, test jednotící nitě), draft-04 vN-typ III→II nota (2D+4D), úklid',
  phases: [
    { title: 'Jádro kola', detail: '2 výpočty + draft-04 paralelně' },
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

const CALC_COMMON = `You are a computational physics agent at ${ROOT}. Environment: python3 + numpy/scipy/sympy/matplotlib (Agg). Verify conventions (ToolSearch "select:WebFetch,WebSearch"). NEVER fudge results — clean mismatches are first-class findings. Deliverables: <dir>/calc.py, <dir>/results.json (EN), plots, Czech writeup in ${KB}/vypocty/.

YOUR TASK: `

phase('Jádro kola')
log('Spouštím Λ-moment výpočet, modulární tok a draft-04…')

const batch = await parallel([
  // --- VYPOCET-17: fermionic induction → Λ (H4g-3) ---
  () => agent(CALC_COMMON + `VYPOCET-17 — H4g-3: if the spectral action is fermion-induced gravity (established: F-014, index-protected −18/11, see ${KB}/vypocty/VYPOCET-02-a4-matching.md + VYPOCET-11-graviton-index.md + ${KB}/BRAINSTORM-04.md H4g-3 section), what does the SAME logic predict for the cosmological constant? Exact sympy work: (1) the spectral action's Λ term: a₀ coefficient — Λ_spectral ~ f₄Λ_cutoff⁴ multiplied by the heat-kernel a₀ = Tr(1) = COUNTING of fermionic degrees of freedom (45 vs 48 Weyl) — extract the exact rational dependence on field content from Chamseddine-Connes (hep-th/9606001 eq. 2.24 area — verify); (2) the a₂ term (Einstein-Hilbert): G_induced ~ f₂Λ²·(content counting) — exact rationals; (3) THE QUESTION: is there a SECOND index-like identity — a content-independent RATIO analogous to −18/11 — among {a₀, a₂, a₄} coefficients of the Dirac sector? Compute the ratios a₀:a₂:a₄-pieces for Weyl/Dirac fermions exactly; check whether any combination (e.g. Λ·G_N or Λ/m_Pl² as predicted by the induced action) is content-count-free; (4) confront honestly with the cosmological constant problem: the induced Λ is cutoff-quartic (the standard disaster) — does fermion-induction make it WORSE, SAME, or does any cancellation structure appear for the NCG SM content (45 vs 48: does ν_R change the sign/structure of induced Λ?); also check the famous Pauli-type cancellation condition (ΣB − ΣF statements, supertrace conditions) for the NCG content. A clean negative ("no second identity; induced Λ has the standard fine-tuning problem, fermion counting does not help") is a full result that closes the last risk of draft-02. Deliverables dir: ${CD}/calculations/lambda-induced/; writeup VYPOCET-17-lambda-indukce.md. Append a dated note to papers/draft-02-a4-fermionic-identity/TODO.md with the outcome.`,
    { label: 'calc:lambda-induced', phase: 'Jádro kola', model: 'opus', schema: CALC_RESULT }),

  // --- VYPOCET-18: modular flow at the corner (H4g-1) ---
  () => agent(CALC_COMMON + `VYPOCET-18 — H4g-1, the unifying-thread test (read ${KB}/BRAINSTORM-04.md H4g-1 + ${KB}/vypocty/VYPOCET-13-ssee-slab-4d.md Hadamard diagnostics + VYPOCET-12/16 modular-spectrum protocol; reuse code from ${CD}/calculations/sj-vn-type/ and ssee-slab-4d/): CLAIM — the diamond-corner non-Hadamard anomaly marks exactly where the SJ state's modular flow stops being a geometric boost. TEST in 2D first (clean, cheap), then 4D slab-vs-diamond if runtime allows: (1) construct the modular Hamiltonian K of the SJ-reduced Gaussian state on the cut (standard Gaussian formalism: K from covariance-matrix log — verify formulas via Casini-Huerta reviews / Sorkin 1611.10281); (2) GEOMETRICITY DIAGNOSTIC: Bisognano-Wichmann/Rindler predicts K is LOCAL with kernel concentrated near the entangling surface and linear (boost) weighting ~distance; measure the locality profile of |K(x,y)| vs |x−y| and vs distance from the entangling point, separately for: half-space cut in slab (expect geometric boost-like) vs diamond cut (expect deviation), and WITHIN the diamond: bulk of the entangling region vs near-corner zone (expect the non-geometricity to CONCENTRATE at corners, matching the Hadamard anomaly location of VYPOCET-13); (3) quantify: fraction of K's norm in non-local (far-off-diagonal) components, as function of distance-to-corner; compare against the known analytic modular Hamiltonian of the 2D diamond (Casini-Huerta have exact local results for intervals in the Minkowski vacuum — our SJ-on-causal-set should deviate from locality near corners if H4g-1 holds, while matching it in the bulk); (4) honest nulls: if K is equally non-local everywhere (discreteness noise dominates) or equally local everywhere, H4g-1 is refuted/untestable at these N — say so. N=400..1800 2D (≥5 seeds), 4D slab N≤2500 if feasible. Deliverables dir: ${CD}/calculations/modular-flow-corner/; writeup VYPOCET-18-modularni-tok-roh.md.`,
    { label: 'calc:modular-flow-corner', phase: 'Jádro kola', model: 'opus', schema: CALC_RESULT }),

  // --- draft-04: vN-type note ---
  () => agent(`You are a theoretical-physics paper-writing agent. Write the project's FOURTH draft IN ENGLISH: the crossed-product/type-transition evidence note — now justified as a 2D+4D letter by VYPOCET-16 (3/3 proxies in 4D). Sources: ${KB}/vypocty/VYPOCET-12-vn-typ-truncace.md, VYPOCET-16-vn-typ-slab-4d.md, VYPOCET-04-ssee-diamant.md, VYPOCET-13-ssee-slab-4d.md, ${CD}/calculations/{sj-vn-type,vn-type-slab-4d,ssee-diamond,ssee-slab-4d}/results.json, ${ROOT}/verification/novelty/entropy-cluster.md (novelty: the three-way synthesis unpublished; prior art: CLPW 2206.10780, CPW 2209.10454, Sorkin-Yazdi 1611.10281, Surya et al. 2008.07697 — position prominently).
Write ${ROOT}/papers/draft-04-type-transition-causal-sets/draft.md (line 1: "DRAFT v0.1 — generated ${DATE}, internal research draft, NOT submitted, requires human review."): title candidate "Numerical signatures of a type III₁ → II crossed-product transition on causal sets" (improve if you can). Content: setup (SJ Gaussian state, link-matrix iΔ, Sorkin-Yazdi truncation); the three finite-N type proxies with their predictions; 2D results (trace collapse 80×, modular pile-up →0, ρ^(−1/2) cutoff); 4D slab results (trace 36× collapse N^1.34→N^0.55, sharp IR edge ε≈2.7, N^(3/4) as the OPERATIVE regulator vs failing fixed-fraction — the selectivity argument is the strongest point); the geometry caveat (diamond corners spoil it — connect to the Hadamard-anomaly localization); interpretation: discreteness scale acts as the observer/modular cutoff of the crossed-product construction (cite CLPW line of work), with the honest gap: no analytic derivation, finite-N proxies only, LQG-area-gap leg of the triangle untested. TODO.md: referee attacks (proxies ≠ types — address head-on with the N-scaling trends argument; prescription vs spectral feature of N^(3/4); Gaussian-state limitation), AI-assisted ethics note, human verification gates. Return Czech 4-line summary.`,
    { label: 'paper:draft-04-type', phase: 'Jádro kola', model: 'opus' }),
])

const calc17 = batch[0]
const calc18 = batch[1]
const draft04 = batch[2]
log('Jádro hotovo (Λ: ' + (calc17 ? calc17.status : 'N/A') + ', modulární tok: ' + (calc18 ? calc18.status : 'N/A') + '). Úklid…')

phase('Úklid')

const hkData = JSON.stringify({
  calc17: calc17 ? { status: calc17.status, keyNumbers: calc17.keyNumbers, verdict: calc17.verdictForHypothesis } : null,
  calc18: calc18 ? { status: calc18.status, keyNumbers: calc18.keyNumbers, verdict: calc18.verdictForHypothesis } : null,
  draft04: draft04,
}, null, 2)

const housekeeping = await agent(`You are the housekeeping agent at ${ROOT}. Today ${DATE}. Czech prose / English data. ECONOMY MODE. Round-8 results:
${hkData}

TASK 1: Update ${CD}/findings.json — append round-8 findings (Λ-induction outcome incl. whether a second index-identity exists; modular-flow corner verdict for H4g-1/through-line; draft-04 written). Conservative wording, evidence paths.
TASK 2: Update ${ROOT}/PROGRESS.md (Read first, preserve): log entry round 8; "Aktuální stav" (4 drafty, 20+ nálezů); "Další kroky" — what calc17 means for draft-02 finality and calc18 for the unifying thread.
TASK 3: Update ${KB}/00-INDEX.md: add VYPOCET-17/18, draft-04.
Return 3-line Czech confirmation.`,
  { label: 'final:round8-writeup', phase: 'Úklid', model: 'sonnet' })

return {
  calc17: calc17 ? { status: calc17.status, keyNumbers: calc17.keyNumbers } : null,
  calc17Verdict: calc17 ? calc17.verdictForHypothesis : null,
  calc18: calc18 ? { status: calc18.status, keyNumbers: calc18.keyNumbers } : null,
  calc18Verdict: calc18 ? calc18.verdictForHypothesis : null,
  draft04Summary: draft04,
  housekeeping: housekeeping,
}