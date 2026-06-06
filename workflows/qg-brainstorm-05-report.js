export const meta = {
  name: 'qg-brainstorm-05-report',
  description: 'BRAINSTORM-05: 5. generace hypotéz nad 24 nálezy (po kole 9) + závěrečná zpráva dne + úklid',
  phases: [
    { title: 'Brainstorm', detail: 'BRAINSTORM-05 nad 24 nálezy', model: 'opus' },
    { title: 'Zpráva', detail: 'závěrečná zpráva dne', model: 'sonnet' },
    { title: 'Úklid', detail: 'PROGRESS, INDEX', model: 'sonnet' },
  ],
}

const ROOT = '/Users/pazny/projects/theoryOfEverything'
const CD = ROOT + '/core-data'
const KB = ROOT + '/knowledge-base'
const DATE = (args && args.date) || '2026-06-06'

const BRAINSTORM_SCHEMA = {
  type: 'object',
  properties: {
    file: { type: 'string' },
    hypotheses: {
      type: 'array',
      items: {
        type: 'object',
        properties: {
          id: { type: 'string', description: 'H5g-N' },
          claim: { type: 'string', description: 'Czech, 1-2 sentences, falsifiable' },
          firstTest: { type: 'string', description: 'Czech, concrete calc sketch' },
          priority: { type: 'string', description: 'high | medium | low' },
        },
        required: ['id', 'claim', 'firstTest', 'priority'],
      },
    },
    reviewRecommendations: { type: 'array', items: { type: 'string' }, description: 'Czech — co má velké review zkontrolovat nejdřív' },
    keyPoints: { type: 'array', items: { type: 'string' }, description: 'Czech, 3-6 bullets' },
  },
  required: ['file', 'hypotheses', 'reviewRecommendations', 'keyPoints'],
}

const REPORT_SCHEMA = {
  type: 'object',
  properties: {
    file: { type: 'string' },
    keyPoints: { type: 'array', items: { type: 'string' }, description: 'Czech, 4-8 bullets' },
  },
  required: ['file', 'keyPoints'],
}

phase('Brainstorm')
log('BRAINSTORM-05: pátá generace hypotéz nad kompletními daty kol 1–9…')

const brainstorm = await agent(`You are the lead theorist of the QG knowledge-base project at ${ROOT}. Today ${DATE}. STRICT language policy: Czech prose, English identifiers/data; NEVER invent arXiv IDs (cite only IDs already present in project files or verified via WebSearch/WebFetch — ToolSearch "select:WebFetch,WebSearch" if needed).

TASK: Write ${KB}/BRAINSTORM-05.md — the 5th-generation hypothesis brainstorm, the capstone of rounds 1-9.

READ FIRST (in this order): ${CD}/findings.json (all 24 findings F-001..F-024); ${KB}/BRAINSTORM-04.md (4th-gen status: H4g-1 partial, H4g-3 killed, H4g-4 confirmed); ${KB}/SYNTEZA-02.md (through-line); ${KB}/vypocty/VYPOCET-19-desitter-II1.md + VYPOCET-20-modularni-tok-bd-4d.md (the freshest results); skim ${CD}/connections.json for explored:"barely" entries NOT yet touched by any VYPOCET (the hunting zone); optionally ${KB}/eseje/ESEJ-04-vstup-pozorovatele.md for the speculative thread.

CONTEXT — where rounds 1-9 left the program:
- Flagship line A (SJ states × horizons): SJ exists through ergoregions (BTZ, Kerr), superradiant onset driven by continuous Ω(r) (ΔAIC up to +4216); VYPOCET-19 just unified A with line B on de Sitter: content-tracking quantities SATURATE on the bounded static patch (II₁, finite Tr 1) vs grow on flat control (II_∞) — the discrete SJ probe SEES the CLPW distinction.
- Flagship line B (III₁→II type transition): 2D diamond 2/3 proxies, 4D slab 3/3, dS patch 2/3; N^(3/4) is a prescription (observer cutoff), not a spectral feature. Corner mechanism (H4g-1): robust in 2D (4/5), partial in 4D with BD object (3/5 — slab boost-geometricity robust, corner concentration does NOT replicate; dimensionally limited).
- Honest nulls/opens from VYPOCET-19: (i) in 2D, truncated SSEE is log-flat in BOTH dS and flat — the II₁/II_∞ distinction lives in region CONTENT, and a 4D dS patch (truncated S~sqrt(N) area law) would separate types directly; (ii) the tracial/max-entropy probe needs density rho~10^3-10^4 (documented scaling); (iii) does the saturated content cap map quantitatively onto horizon area/4 (the dS entropy)?
- Killed programs (do NOT resurrect without new mechanism): gamma-Cardy (Sen IR-universality), naive Lambda~1/sqrt(V) (~140x prefactor), H4g-3 second index identity for Lambda, continuous BMV discriminators (24-72 orders below reach).

WRITE the brainstorm with: (1) "Stav programu" — 1-page honest summary of where the two flagship lines converged; (2) "Hypotézy 5. generace" — 4-7 hypotheses H5g-1..N, each with: motivation traced to specific findings (F-IDs), falsifiable claim, concrete first test (sketch of calc: geometry, object, observable, expected discriminator, N/seeds feasible on this machine — matrix ops cap ~N 2500), priority, main risk. At least ONE hypothesis must come from the explored:"barely" hunting zone untouched by rounds 3-9 (cite the connection IDs). Natural candidates you should weigh (but think independently): 4D dS static patch type discriminator via truncated area law; entropy cap vs horizon area/4 quantitative match (the dS entropy from first principles?); corner-mechanism reformulation for 4D (what replaces corners — caustics? higher-codim wedges?); high-density tracial probe; whether F-023+F-019 together imply a draft-05 or extend draft-04. (3) "Doporučená fronta" — ordered queue with reasoning, marking which tests fit one afternoon vs need new machinery; (4) "Doporučení pro velké review" — the user plans a big data-correctness review + theoretical-link completion + repo cleanup next; list concretely what the review must check first (known weak points: placeholder a_err=0.776 in draft-04 uncertainties, unverified 2025-26 arXiv IDs, draft-03 D-convention ambiguity, illustrative value 8 in CST random walk — and whatever else you find in findings.json caveats), plus which theoretical links in the concept graph are missing/underspecified.

400-700 lines. Imagination allowed in clearly marked speculative asides; core claims rigorous with F-ID/file evidence trails.`,
  { label: 'brainstorm-05', phase: 'Brainstorm', model: 'opus', schema: BRAINSTORM_SCHEMA })

phase('Zpráva')
log('BRAINSTORM-05 hotov (' + brainstorm.hypotheses.length + ' hypotéz). Píšu závěrečnou zprávu dne…')

const report = await agent(`You are the project chronicler at ${ROOT}. Today ${DATE}. Czech prose, English identifiers. ECONOMY MODE — read only what is listed.

TASK: Write ${ROOT}/reports/2026-06-06-day-report.md (create the reports/ directory implicitly by writing the file) — the final report of the research day, the document the human reads with their morning coffee.

READ: ${ROOT}/PROGRESS.md (full log of rounds 3-9); ${CD}/findings.json (24 findings — pull exact key numbers from there, do not re-derive); ${ROOT}/papers/REVIZE-PRO-CLOVEKA.md (skim — overview table + high-risk items).

BRAINSTORM-05 just finished; its headline hypotheses (include in "Kam dál" section):
${JSON.stringify(brainstorm.hypotheses, null, 2)}
Its key points:
${brainstorm.keyPoints.map(p => '- ' + p).join('\n')}

STRUCTURE:
(1) "Executive summary" — 10-15 lines: what this day produced, in plain Czech;
(2) "Co bylo nalezeno" — the confirmed findings grouped by line (SJ×horizons incl. dS II₁ discrimination; type transition III₁→II incl. corner mechanism status; a₄ identity −18/11; d_s classifier), each with 1-3 key numbers and finding IDs;
(3) "Co bylo zabito a proč je to dobře" — gamma-Cardy, naive Lambda unification, H4g-3, BMV discriminators — one paragraph each, the epistemic value of clean kills;
(4) "Stav papers/" — table of 4 drafts (status, scientific closure, human-review estimate from REVIZE-PRO-CLOVEKA.md) + pointer to REVIZE-PRO-CLOVEKA.md as the entry point;
(5) "Statistiky dne" — rounds, calculations (VYPOCET-01..20), findings count, essays, brainstorms, syntheses (count from PROGRESS.md, do not invent);
(6) "Kam dál" — BRAINSTORM-05 headline hypotheses + the user's roadmap (big review → composable simulations/visualizations from formulas.json → minimalist web built from the file structure);
(7) "Provozní poučení" — token economy, prefix cache, session limits (from PROGRESS.md if recorded; keep short).

150-300 lines. Faithful to sources; no number without a source file.`,
  { label: 'day-report', phase: 'Zpráva', model: 'sonnet', schema: REPORT_SCHEMA },
  )

phase('Úklid')

const housekeeping = await agent(`You are the housekeeping agent at ${ROOT}. Today ${DATE}. Czech prose / English data. ECONOMY MODE.
Round results: BRAINSTORM-05 written to ${KB}/BRAINSTORM-05.md (${brainstorm.hypotheses.length} hypotheses: ${brainstorm.hypotheses.map(h => h.id).join(', ')}); day report written to ${ROOT}/reports/2026-06-06-day-report.md.
TASK 1: Update ${ROOT}/PROGRESS.md (Read first, preserve content): add log entry "BRAINSTORM-05 + závěrečná zpráva"; update "Aktuální stav" (basic research of Phase 2 COMPLETE — next per roadmap: velké review); in the resume banner at top, replace the round-9 banner with one line saying basic research done, day report at reports/2026-06-06-day-report.md, next step = velké review.
TASK 2: Update ${KB}/00-INDEX.md: add BRAINSTORM-05.md and reports/2026-06-06-day-report.md.
Return 2-line Czech confirmation.`,
  { label: 'final:housekeeping', phase: 'Úklid', model: 'sonnet' })

return {
  brainstorm: { file: brainstorm.file, hypotheses: brainstorm.hypotheses, keyPoints: brainstorm.keyPoints },
  reviewRecommendations: brainstorm.reviewRecommendations,
  report: report,
  housekeeping: housekeeping,
}
