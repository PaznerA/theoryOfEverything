export const meta = {
  name: 'qg-round-09',
  description: 'Kolo 9: VYPOCET-19 SJ na de Sitter static patch + typ II₁ test (sjednocení vlajkových linií, konfrontace s CLPW), VYPOCET-20 4D modulární tok s BD objektem, ESEJ-04, balíček pro lidskou revizi draftů',
  phases: [
    { title: 'Jádro kola', detail: '2 výpočty + esej + revizní balíček paralelně' },
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

const CALC_COMMON = `You are a computational physics agent at ${ROOT}. Environment: python3 + numpy/scipy/sympy/matplotlib (Agg). Verify conventions (ToolSearch "select:WebFetch,WebSearch"). NEVER fudge results. Deliverables: <dir>/calc.py, <dir>/results.json (EN), plots, Czech writeup in ${KB}/vypocty/.

YOUR TASK: `

phase('Jádro kola')
log('Spouštím de Sitter test, 4D BD modulární tok, esej a revizní balíček…')

const batch = await parallel([
  // --- VYPOCET-19: SJ on dS static patch + type II₁ test ---
  () => agent(CALC_COMMON + `VYPOCET-19 — UNIFY the project's two flagship lines (SJ states in horizned spacetimes × vN-type transitions) on DE SITTER: the CLPW prediction (arXiv:2206.10780) says the static-patch observer algebra is type II₁ — crucially II₁ (normalizable trace, maximum-entropy state exists), NOT II_∞ like the black-hole case. TEST whether the SJ+truncation machinery sees this distinction. PLAN: (1) sprinkle a 2D de Sitter STATIC PATCH region (2D dS metric ds² = −(1−r²/ℓ²)dt² + dr²/(1−r²/ℓ²); conformal trick for the causal structure — verify against the dS causal-set literature: SJ on dS was studied in arXiv:1306.3231, fetch for conventions; use a bounded sub-region of the static patch); (2) run the type-proxy protocol (VYPOCET-12/16 code from ${CD}/calculations/sj-vn-type/ and vn-type-slab-4d/): trace scaling, modular spectrum before/after truncation; (3) THE II₁ vs II_∞ DISCRIMINATOR: for II₁ the truncated trace must SATURATE to a finite maximum (Tr 1 < ∞, max-entropy tracial state) as the region exhausts the static patch, while flat-slab/diamond II_∞ behavior grows without bound with region size — measure truncated entropy vs region size at fixed density approaching the horizon; also the modular spectrum of the maximally mixed candidate; (4) horizon-approach behavior: does the truncated entropy approach a finite cap ~ horizon area/4 in causal-set units (the dS entropy!)? Compare against the flat-slab control at matched parameters. ≥4 seeds, N up to ~2500. HONEST nulls welcome: if the discrete probe cannot distinguish II₁ from II_∞ at these N, document precisely why (what scaling would distinguish them and what N it needs). Deliverables dir: ${CD}/calculations/sj-desitter-type/; writeup VYPOCET-19-desitter-II1.md.`,
    { label: 'calc:sj-desitter-II1', phase: 'Jádro kola', model: 'opus', schema: CALC_RESULT }),

  // --- VYPOCET-20: 4D modular flow retry with BD object ---
  () => agent(CALC_COMMON + `VYPOCET-20 — fix the 4D null of VYPOCET-18 (read ${KB}/vypocty/VYPOCET-18-modularni-tok-roh.md: the 2D corner-nonlocality mechanism did NOT replicate in 4D with the LINK-MATRIX iΔ, suspected cause = link-matrix sparseness/flat spectrum ~N^0.65). RETRY with the BD d'Alembertian object that fixed the spectrum shape in 4D (VYPOCET-09: clean power law λ~k^−α, R²≈0.99; reuse the BD construction from ${CD}/calculations/ssee-bd-4d/calc.py — sharp BD with documented coefficients (1,−9,16,−8) and prefactor 4√ρ/√6, or smeared ε=0.6 if conditioning demands): (1) build G_R = B⁻¹ → iΔ on 4D slab AND 4D diamond (N≤2200, ≥3 seeds — matrix inversion bound); (2) re-run the modular-kernel geometricity diagnostics of VYPOCET-18: off-diagonal decay slope slab vs diamond; per-site non-locality vs distance-to-corner; diagonal boost-linearity on the slab half-space cut; (3) VERDICT: does the BD object restore the 2D mechanism in 4D (corner-concentrated non-geometricity) — or does 4D genuinely lack it (then H4g-1 is dimension-limited and the through-line's layer B needs reformulation)? Either answer is a finding. Deliverables dir: ${CD}/calculations/modular-flow-bd-4d/; writeup VYPOCET-20-modularni-tok-bd-4d.md.`,
    { label: 'calc:modular-flow-bd-4d', phase: 'Jádro kola', model: 'opus', schema: CALC_RESULT }),

  // --- ESEJ-04 ---
  () => agent(`You are an essayist-physicist at ${ROOT}. The user explicitly wants imagination UNLEASHED in prose. Write IN CZECH: ${KB}/eseje/ESEJ-04-vstup-pozorovatele.md — "Vstup pozorovatele do vesmíru". Header: "⚠️ SPEKULATIVNÍ ESEJ — fantazie odbrzděná, fakta citována, extrapolace značeny". Interleave "Co víme" (cited) / "Co kdyby" (unleashed); end with "Co by muselo být pravda".
Material (read): ${KB}/vypocty/VYPOCET-12, -16, -18 writeups; ${KB}/foundations/19-von-neumann-algebras.md; ${KB}/BRAINSTORM-04.md (jednotící nit, H4g-1); ${CD}/findings.json (F-015, F-016, F-019..F-022); papers/draft-04 abstract.
The thread: before an observer enters, QFT's local algebras are type III₁ — no states, no entropy, no density matrices, pure relational flux (Connes-Rovelli: time itself from the modular flow). The observer's entry (CLPW: an observer's clock; our data: the discreteness-scale truncation at rank N^(3/4)) converts III₁→II: suddenly entropy EXISTS. Our numbers: trace collapse 36-80×, modular pile-up → 0, sharp IR edge; and the corner — the place where the observer's boost fails — is precisely where the state stops being Hadamard and the modular flow stops being geometric. Co kdyby: entropy is not a property of the world but of the world-plus-witness; the area law as the signature of any consistent witnessing; the discreteness scale of spacetime as the universe's built-in observer (the universe witnesses itself at the Planck scale — hence Bekenstein-Hawking); corners/caustics as places where witnessing breaks down (singularities as epistemic, not ontic?); de Sitter II₁ as the universe with a maximum of ignorance. Wild but grounded, clearly marked. 400-700 lines.`,
    { label: 'esej:vstup-pozorovatele', phase: 'Jádro kola', model: 'opus' }),

  // --- human-review package ---
  () => agent(`You are an editorial coordination agent (ECONOMY MODE) at ${ROOT}. Four paper drafts exist in ${ROOT}/papers/ (draft-01 v0.2 SJ-rotating, draft-02 a₄ identity [scientifically closed per VYPOCET-11+17], draft-03 d_s classifier, draft-04 type transition). Each has a TODO.md. Write ${ROOT}/papers/REVIZE-PRO-CLOVEKA.md IN CZECH — the single entry point for the human researcher:
(1) Přehledová tabulka: draft | stav | vědecká uzavřenost | hlavní nárok | největší riziko | odhad času lidské revize;
(2) Pro každý draft: co PŘESNĚ člověk musí ověřit (seřazeno: matematické re-derivace, kontrola citací proti PDF, konvence, čísla vs results.json), s checkboxy;
(3) Doporučené pořadí revizí (návrh: draft-02 první — nejmenší, exaktní, uzavřený; pak draft-04, draft-01, draft-03) s odůvodněním;
(4) Společné zásady: AI-asistovaná proveniencí — co to znamená pro autorství a etiku podání; že žádný draft nesmí být podán bez nezávislé lidské re-derivace klíčových výsledků; jak spustit reprodukce (každý calc.py je runnable — uveď přesné příkazy);
(5) Co NENÍ v draftech (zabité programy γ–Cardy, Λ-sjednocení, H4g-3 — a proč je dobré, že tam nejsou).
Read the four TODO.md files + skim the drafts' abstracts. Return structured result (file + keyPoints Czech).`,
    { label: 'editorial:review-package', phase: 'Jádro kola', model: 'sonnet', schema: NOTE_RESULT }),
])

const calc19 = batch[0]
const calc20 = batch[1]
const esej04 = batch[2]
const revize = batch[3]
log('Jádro hotovo (dS: ' + (calc19 ? calc19.status : 'N/A') + ', BD-4D: ' + (calc20 ? calc20.status : 'N/A') + '). Úklid…')

phase('Úklid')

const hkData = JSON.stringify({
  calc19: calc19 ? { status: calc19.status, keyNumbers: calc19.keyNumbers, verdict: calc19.verdictForHypothesis } : null,
  calc20: calc20 ? { status: calc20.status, keyNumbers: calc20.keyNumbers, verdict: calc20.verdictForHypothesis } : null,
  esej04: esej04 ? 'written' : null,
  revize: revize,
}, null, 2)

const housekeeping = await agent(`You are the housekeeping agent at ${ROOT}. Today ${DATE}. Czech prose / English data. ECONOMY MODE. Round-9 results:
${hkData}

TASK 1: Update ${CD}/findings.json — append round-9 findings (dS II₁ discriminator outcome; BD 4D modular-flow verdict — does H4g-1 hold in 4D with the right object?). Conservative wording, evidence paths.
TASK 2: Update ${ROOT}/PROGRESS.md (Read first, preserve): log entry round 9; "Aktuální stav"; "Další kroky" — note REVIZE-PRO-CLOVEKA.md exists as the human entry point.
TASK 3: Update ${KB}/00-INDEX.md: add VYPOCET-19/20, ESEJ-04, REVIZE-PRO-CLOVEKA.md (prominently — it is the human entry point).
Return 3-line Czech confirmation.`,
  { label: 'final:round9-writeup', phase: 'Úklid', model: 'sonnet' })

return {
  calc19: calc19 ? { status: calc19.status, keyNumbers: calc19.keyNumbers } : null,
  calc19Verdict: calc19 ? calc19.verdictForHypothesis : null,
  calc20: calc20 ? { status: calc20.status, keyNumbers: calc20.keyNumbers } : null,
  calc20Verdict: calc20 ? calc20.verdictForHypothesis : null,
  esej04: esej04 ? 'written' : null,
  revize: revize,
  housekeeping: housekeeping,
}