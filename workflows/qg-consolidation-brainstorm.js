export const meta = {
  name: 'qg-consolidation-brainstorm',
  description: 'Úsporná dokončovací fáze: verifikace 5 pilířů (sonnet), deterministická konsolidace (python+haiku), syntéza (opus) a podmíněný hluboký brainstorming nad daty (opus panel)',
  phases: [
    { title: 'Verifikace', detail: '5 levných verifikátorů pro pilíře se zastaralou/chybějící verifikací', model: 'sonnet' },
    { title: 'Konsolidace', detail: 'python consolidate.py (deterministicky, ~0 tokenů) + judge slučování duplicitních konceptů', model: 'sonnet' },
    { title: 'Syntéza', detail: 'SYNTEZA.md — mapa souvislostí a bílá místa', model: 'opus' },
    { title: 'Brainstorming', detail: '5 hypotézních čoček nad daty (žádný web) + syntéza do BRAINSTORM-01.md — jen pokud předchozí fáze prošly', model: 'opus' },
    { title: 'Úklid', detail: '00-INDEX.md + aktualizace PROGRESS.md' },
  ],
}

const ROOT = '/Users/pazny/projects/theoryOfEverything'
const CD = ROOT + '/core-data'
const DATE = (args && args.date) || '2026-06-05'

const TO_VERIFY = [
  { slug: 'causal-sets', kb: ROOT + '/knowledge-base/approaches/05-causal-sets.md' },
  { slug: 'group-field-theory', kb: ROOT + '/knowledge-base/approaches/06-group-field-theory.md' },
  { slug: 'twistors-amplitudes', kb: ROOT + '/knowledge-base/approaches/08-twistors-amplitudes.md' },
  { slug: 'emergent-gravity', kb: ROOT + '/knowledge-base/approaches/09-emergent-gravity.md' },
  { slug: 'experimental-tests', kb: ROOT + '/knowledge-base/phenomenology/17-experimental-tests.md' },
]

const VERIFY_RESULT = {
  type: 'object',
  properties: {
    slug: { type: 'string' },
    referencesChecked: { type: 'number' },
    problemsFound: { type: 'number' },
    fixed: { type: 'number' },
    remainingConcerns: { type: 'array', items: { type: 'string' } },
  },
  required: ['slug', 'referencesChecked', 'problemsFound', 'fixed', 'remainingConcerns'],
}

const CONSOL_RESULT = {
  type: 'object',
  properties: {
    ok: { type: 'boolean' },
    statsOutput: { type: 'string', description: 'verbatim stdout of consolidate.py' },
    missingFiles: { type: 'array', items: { type: 'string' } },
  },
  required: ['ok', 'statsOutput', 'missingFiles'],
}

const JUDGE_RESULT = {
  type: 'object',
  properties: {
    mergedGroups: { type: 'number' },
    mergedIds: { type: 'number' },
    rejectedPairs: { type: 'number' },
    problemsMerged: { type: 'number' },
    note: { type: 'string' },
  },
  required: ['mergedGroups', 'mergedIds', 'rejectedPairs', 'problemsMerged', 'note'],
}

const LENS_RESULT = {
  type: 'object',
  properties: {
    lens: { type: 'string' },
    hypotheses: {
      type: 'array',
      items: {
        type: 'object',
        properties: {
          title: { type: 'string' },
          statement: { type: 'string', description: '3-6 precise sentences' },
          grounding: { type: 'string', description: 'concrete concept/formula/problem ids and files supporting it' },
          whyUnexplored: { type: 'string' },
          firstTest: { type: 'string', description: 'concrete first calculation/analysis' },
          confidence: { type: 'string', description: 'high | medium | low' },
        },
        required: ['title', 'statement', 'grounding', 'whyUnexplored', 'firstTest', 'confidence'],
      },
    },
  },
  required: ['lens', 'hypotheses'],
}

// ---------- Fáze 1: verifikace 5 pilířů (sonnet, úsporně) ----------
phase('Verifikace')
log('Verifikuji 5 pilířů se zastaralou/chybějící verifikací (sonnet, vzorek 8 referencí)…')

const verifications = await parallel(TO_VERIFY.map(p => () => agent(
`You are an adversarial verification agent in ECONOMY MODE. Verify the CURRENT files for pillar "${p.slug}":
- Czech prose: ${p.kb}
- English JSON fragment: ${CD}/fragments/${p.slug}.json
A verification report from an OLDER file version may exist at ${ROOT}/verification/${p.slug}.md — ignore its conclusions and overwrite it at the end.

STEP 0: call ToolSearch with query "select:WebFetch,WebSearch" (prefer WebFetch; use WebSearch only when a reference cannot be located directly).
STEP 1: Read both files once. If the JSON is invalid, fix it first.
STEP 2: Sample 8 references, weighted toward the ones carrying the strongest claims. For each, WebFetch https://arxiv.org/abs/ID (or the DOI) and verify the ID resolves AND title+authors+year match. Hunt for invented IDs and wrong attribution.
STEP 3: Check the 4 most important formulas (coefficients, signs).
STEP 4: Fix errors directly with Edit; DELETE unverifiable references (and their citations in prose); tag unverifiable claims with "⚠️ neověřeno". Keep the JSON valid.
STEP 5: Overwrite ${ROOT}/verification/${p.slug}.md with a brief Czech report.
Be economical: no redundant fetches, no repeated re-reads of large files. Return the structured result (remainingConcerns in Czech).`,
  { label: 'verify:' + p.slug, phase: 'Verifikace', model: 'sonnet', schema: VERIFY_RESULT })))

const verifyDone = verifications.filter(Boolean)
log('Verifikace hotová: ' + verifyDone.length + '/5 pilířů. Spouštím deterministickou konsolidaci…')

// ---------- Fáze 2: konsolidace — python (zdarma) + judge (sonnet) ----------
phase('Konsolidace')

const consolidator = await agent(
`Run this exact command with Bash: python3 ${ROOT}/workflows/consolidate.py
It deterministically consolidates ${CD}/fragments/*.json into unified registries (this re-run picks up edits just made by verification agents).
Then check that these files exist and are non-empty: ${CD}/concept-graph.json, ${CD}/references.json, ${CD}/references.bib, ${CD}/formulas.json, ${CD}/open-problems.json, ${CD}/connections.json, ${CD}/_digest.md, ${CD}/_review/concept-merge-candidates.json.
Return ok=true with the script's stdout verbatim in statsOutput and an empty missingFiles list (or ok=false with the error text and what is missing). Do NOT attempt to fix the script or the data.`,
  { label: 'consolidate.py', phase: 'Konsolidace', model: 'haiku', schema: CONSOL_RESULT })

const judge = consolidator && consolidator.ok ? await agent(
`You are a concept-merge judge for a quantum-gravity concept graph (ECONOMY MODE — read only what is listed).
1) Read ${CD}/_review/concept-merge-candidates.json — candidate near-duplicate concept pairs (id, name, definition, pillars).
2) Decide which pairs denote the SAME physical concept. Merely related concepts are NOT duplicates (e.g. "holographic-principle" vs "holography-of-information" stay separate; "bekenstein-hawking-entropy" vs "black-hole-entropy" are the same). When unsure, do NOT merge.
3) Write ${CD}/_review/merge-decisions.json — a JSON array of {"keep": "<canonical-community-id>", "merge": ["<id>", ...]} covering all accepted merges (group transitively).
4) Run with Bash: python3 ${ROOT}/workflows/consolidate.py --apply-merges  — and confirm from its output that merges applied and the digest regenerated.
5) Also read ${CD}/_review/problem-merge-candidates.json (a few fuzzy near-duplicate open-problem id pairs). For TRUE duplicates, merge the entries directly in ${CD}/open-problems.json with Edit (union "pillars", keep the better statement, drop the duplicate entry).
Return the structured result (note in Czech, 1-2 sentences).`,
  { label: 'judge:concept-merges', phase: 'Konsolidace', model: 'sonnet', schema: JUDGE_RESULT }) : null

log(consolidator && consolidator.ok ? 'Registry zkonsolidovány a deduplikovány. Jdu na syntézu…' : '⚠️ Konsolidace selhala — syntézu zkusím i tak, brainstorming se přeskočí.')

// ---------- Fáze 3: syntéza (opus — jediný drahý agent této části) ----------
phase('Syntéza')

const synteza = await agent(
`You are the synthesis agent for the quantum-gravity knowledge base at ${ROOT}. Project goal: structured context so AI can hunt yet-undiscovered connections between approaches. ECONOMY MODE: start from ${CD}/_digest.md (cheap pre-computed entry point), then read ${CD}/connections.json and ${CD}/open-problems.json; dip into ${CD}/concept-graph.json and the pillar files under ${ROOT}/knowledge-base/ only selectively (Grep, partial reads). No web research.

Write ${ROOT}/knowledge-base/SYNTEZA.md IN CZECH (English terms in parentheses at first use):

# Syntéza: Mapa kvantové gravitace
## Velký obraz                          ← kde dnes každý z 18 pilířů stojí, odstavec na pilíř max
## Mapa vztahů mezi přístupy            ← Mermaid diagram (graph LR) pilířů s hranami podle connections.json (prozkoumanost vyznač stylem hran: plná=well, čárkovaná=partially, tečkovaná=barely) + komentář
## Kde se přístupy shodují              ← konvergentní výsledky nezávislých přístupů (dimenzionální redukce v UV, minimální délka, entropie černých děr, bounce…)
## Kde si protiřečí                     ← skutečné konflikty a neslučitelné předpoklady (typ "conflict" v connections.json)
## Sdílené otevřené problémy            ← z open-problems.json, řazeno podle počtu pilířů
## Bílá místa: sotva prozkoumané souvislosti  ← JÁDRO: vyber ~15 nejzajímavějších ze 112 barely-explored hran; pro každou: co to je, proč je zajímavá, jaká data k ní máme (konkrétní soubory/id), konkrétní první krok
## Kandidátní hypotézy k prověření      ← 5-8 spekulativních, ale podložených kandidátů — každý s odůvodněním a testem, který by ho vyvrátil

Dense, honest, zero filler. Cite core-data files and pillar files by path. Return a 5-line Czech summary of the most promising white spaces.`,
  { label: 'synthesis:SYNTEZA.md', phase: 'Syntéza', model: 'opus' })

// ---------- Fáze 4: brainstorming (jen pokud nic nespadlo na limit) ----------
const healthy = !!(consolidator && consolidator.ok && judge && synteza && verifyDone.length >= 4)
let brainstorm = null
let lensResults = []

if (healthy) {
  phase('Brainstorming')
  log('Vše prošlo — spouštím hypotézní panel: 5 čoček nad dostupnými daty (žádný web)…')

  const LENS_COMMON = `You are one lens of a hypothesis-generation panel over the quantum-gravity knowledge base at ${ROOT}. GOAL: propose candidate YET-UNDISCOVERED connections between quantum-gravity approaches, grounded strictly in the collected data. NO web research — the whole point is mining OUR data. ECONOMY MODE: read ${CD}/_digest.md first, then ONLY your lens-specific files; use Grep and partial reads; never re-read.
A good hypothesis is: SPECIFIC (not "X relates to Y" but through which structure/quantity and why), GROUNDED (cites concrete concept/formula/problem ids and file paths), GENUINELY UNDER-EXPLORED (cross-check connections.json — an edge already rated "well" is not a discovery), FALSIFIABLE (a concrete first calculation or analysis). Quality over quantity. Output in English (core logic data). Return 4-6 hypotheses via structured output.

YOUR LENS: `

  lensResults = await parallel([
    () => agent(LENS_COMMON + `SHARED MATHEMATICAL STRUCTURES. Files: ${CD}/formulas.json, ${CD}/concept-graph.json, ${CD}/connections.json. Hunt for the same mathematical structure (equation form, algebraic structure, spectral behavior, fixed-point/RG pattern, statistical distribution) appearing in 2+ pillars WITHOUT a corresponding connections.json edge — or with one rated barely. Propose what identity or mapping the shared structure suggests.`,
      { label: 'lens:shared-math', phase: 'Brainstorming', model: 'opus', schema: LENS_RESULT }),
    () => agent(LENS_COMMON + `WHITE SPACES. Files: ${CD}/connections.json (focus explored="barely"), ${CD}/open-problems.json. From the 112 barely-explored edges pick the 5-6 with the highest discovery potential and develop each into a full hypothesis: what exactly the bridge would be, what it would imply for both pillars, and the first test.`,
      { label: 'lens:white-space', phase: 'Brainstorming', model: 'opus', schema: LENS_RESULT }),
    () => agent(LENS_COMMON + `CONVERGENCES. Files: ${CD}/_digest.md, ${CD}/open-problems.json, ${CD}/connections.json. Identify results that several INDEPENDENT approaches converge on (e.g. spectral dimension flowing to ~2 in the UV, minimal length, singularity-resolving bounce, entropy bounds, dimensional reduction). For each convergence: what single deeper principle would explain all instances at once, and how would one test that principle rather than the instances?`,
      { label: 'lens:convergence', phase: 'Brainstorming', model: 'opus', schema: LENS_RESULT }),
    () => agent(LENS_COMMON + `CONFLICTS AS SIGNAL. Files: ${CD}/connections.json (type="conflict" and entries with rating-disagreement notes), plus targeted Greps into ${ROOT}/knowledge-base/ pillar files. Sharpen each genuine contradiction between approaches into a decisive question: which calculation or observation would discriminate between them? A sharp contradiction is a discovery waiting to happen.`,
      { label: 'lens:conflict', phase: 'Brainstorming', model: 'opus', schema: LENS_RESULT }),
    () => agent(LENS_COMMON + `METHOD TRANSFER. Files: ${CD}/open-problems.json, ${CD}/formulas.json, ${CD}/concept-graph.json. Find pairs (mature technique/result in pillar A; stubborn open problem in pillar B) where the technique has plausibly never been applied to that problem. Propose concrete transplants: what maps to what, what breaks, what the first computation would be.`,
      { label: 'lens:transfer', phase: 'Brainstorming', model: 'opus', schema: LENS_RESULT }),
  ])

  const lenses = lensResults.filter(Boolean)
  const allHyps = JSON.stringify(lenses, null, 2)
  brainstorm = await agent(
`You are the synthesizer of a quantum-gravity hypothesis panel. Five lenses produced these candidate hypotheses (JSON):
${allHyps}

Write ${ROOT}/knowledge-base/BRAINSTORM-01.md IN CZECH (English terms in parentheses; ids/formulas stay English):
# Brainstorming 01: Kandidáti na nenalezené souvislosti (${DATE})
## Metodologie  ← stručně: 5 čoček nad core-data, bez webu; hypotézy NEJSOU ověřené proti literatuře — to je další krok
## Top hypotézy ← dedupuj překryvy mezi čočkami, seřaď podle (potenciál objevu × síla opory v datech); pro každou: co tvrdí, opora v datech (konkrétní id/soubory), proč to nejspíš nikdo neudělal, první test, confidence; uveď čočku původu
## Kompletní tabulka všech hypotéz  ← markdown tabulka: název | čočka | confidence | první test
## Jak dál  ← doporučený postup Fáze 2: pořadí prověřování, co ověřit proti literatuře (novelty check), které výpočty lze zkusit rovnou

Honest ranking — if a hypothesis is weak or two lenses disagree, say so. Return a Czech summary of the top 5 hypotheses (one line each).`,
    { label: 'brainstorm:synth', phase: 'Brainstorming', model: 'opus' })
} else {
  log('⚠️ Přeskakuji brainstorming (healthy=false) — některá předchozí fáze nedoběhla čistě.')
}

// ---------- Fáze 5: úklid — index + progress (sonnet) ----------
phase('Úklid')

const verifySummary = JSON.stringify(verifyDone, null, 2)
const judgeNote = judge ? JSON.stringify(judge) : 'null'
const statsOut = consolidator ? consolidator.statsOutput : '(konsolidace selhala)'

const housekeeping = await agent(
`You are the housekeeping agent for the quantum-gravity knowledge base at ${ROOT}. Today is ${DATE}. Work IN CZECH. ECONOMY MODE: enumerate files with Bash ls/Glob; read at most the first ~20 lines of a file when you need a hook.

TASK 1: write ${ROOT}/knowledge-base/00-INDEX.md — annotated index of every file under knowledge-base/, core-data/ and verification/. One line per file: relative link + jednověté lákadlo. Order: SYNTEZA.md${healthy ? ', BRAINSTORM-01.md' : ''}, core-data registry, pak pilíře po sekcích, verifikační reporty jen souhrnně odstavcem.

TASK 2: update ${ROOT}/PROGRESS.md (Read first; preserve structure):
- Fáze 1 (Základní rešerše): ✅ dokončeno ${DATE}. ${healthy ? 'Fáze 2 (Hledání souvislostí): 🟡 zahájena — první brainstorm hotov (BRAINSTORM-01.md), další krok = novelty check hypotéz proti literatuře.' : 'Fáze 2: připravena.'} Update "Aktuální stav" + tabulku fází accordingly.
- "## Statistiky": markdown table from this consolidate.py output (per-pillar counts + registry totals):
${statsOut}
  Plus verification summary (5 re-verified pillars): ${verifySummary}
  Plus concept-merge judge: ${judgeNote}
- "## Další kroky": ${healthy ? 'derive from BRAINSTORM-01.md section "Jak dál" (read it briefly)' : 'note that brainstorming was skipped and needs a re-run'}; plus standing items: doplnit chybějící témata, novelty check, průběžná aktualizace.
- Append log entry for ${DATE}: economy run — re-verification of 5 pillars, deterministic consolidation (python), dedup, synthesis${healthy ? ', first hypothesis brainstorm (BRAINSTORM-01.md)' : ''}.

Return a 3-line Czech confirmation.`,
  { label: 'final:index+progress', phase: 'Úklid', model: 'sonnet' })

return {
  verified: verifyDone.length + '/5',
  verifyDetails: verifyDone,
  consolidationOk: !!(consolidator && consolidator.ok),
  judge: judge,
  syntezaSummary: synteza,
  brainstormRan: healthy,
  lensCount: lensResults.filter(Boolean).length,
  brainstormTop: brainstorm,
  housekeeping: housekeeping,
}