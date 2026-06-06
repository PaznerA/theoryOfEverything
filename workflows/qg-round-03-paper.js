export const meta = {
  name: 'qg-round-03-paper',
  description: 'Kolo 3: Kerr ekvatoriální SJ výpočet, první draft článku (SJ v rotujících prostoročasech, EN), přeformulování entropy-clusteru po 4D výsledku, nový pilíř von Neumannových algeber, BRAINSTORM-03',
  phases: [
    { title: 'Rozšíření', detail: 'VYPOCET-08 Kerr ekvatoriální SJ + reframe entropy-clusteru + pilíř 19 von Neumann algebry' },
    { title: 'Draft článku', detail: 'PAPER-DRAFT-01: SJ stav v rotujících prostoročasech (EN, papers/)', model: 'opus' },
    { title: 'Brainstorm 03', detail: 'třetí generace hypotéz nad výsledky rozhodujícího kola', model: 'opus' },
    { title: 'Úklid', detail: 'findings.json update, PROGRESS, INDEX, konsolidace', model: 'sonnet' },
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
    keyPoints: { type: 'array', items: { type: 'string' }, description: 'Czech, 3-5 items' },
  },
  required: ['file', 'keyPoints'],
}

phase('Rozšíření')
log('Spouštím Kerr výpočet, reframe entropy-clusteru a nový pilíř…')

const ext = await parallel([
  // --- VYPOCET-08: Kerr equatorial SJ ---
  () => agent(`You are a computational physics agent at ${ROOT}. Environment: python3 + numpy/scipy/sympy/matplotlib (Agg). Verify conventions via ToolSearch "select:WebFetch,WebSearch". NEVER fudge results.

TASK: EXTEND the rotating-BTZ SJ construction (read ${KB}/vypocty/VYPOCET-05-sj-rotujici-btz.md and reuse the working code ${CD}/calculations/sj-rotating-btz/calc.py) to the KERR equatorial fixed-r (t,φ) section — the same 2D conformal trick (massless 2D: G_R = (1/2)C). Kerr in Boyer-Lindquist, equatorial plane θ=π/2: induced (t,φ) metric at fixed r has g_tt = -(1-2Mr/Σ)... use the standard equatorial Kerr metric components (verify formulas; Σ=r², so g_tt=-(1-2M/r), g_tφ=-2Ma/r, g_φφ=r²+a²+2Ma²/r). Pick M=1, a=0.6 (and a=0.9 aggressive): ergosphere at r_erg=2M (equatorial), horizon r_+=1+√(1-a²). MEASUREMENTS mirroring VYPOCET-05: (1) SJ existence at fixed-r sections inside the ergoregion (r_+ < r < 2M) — Lorentzian section check, ± eigenvalue pairing; (2) co-rotating link fraction f_co and causal asymmetry A_caus scan across r (does the interior null slope cross zero exactly at r_erg=2M as in BTZ?); (3) Wightman directional asymmetry A_W sign vs A_caus sign — does the OPPOSITE-SIGN phenomenon from BTZ replicate in Kerr? (4) a-dependence: A_caus(r=1.5) for a ∈ {0.3, 0.6, 0.9}. Same N≈1600, ≥3 seeds. The goal: establish the BTZ signatures as GEOMETRY-INDEPENDENT properties of SJ states in rotating spacetimes (asymptotically flat Kerr vs AdS BTZ). Deliverables: ${CD}/calculations/sj-kerr-equatorial/{calc.py,results.json,plots}, Czech writeup ${KB}/vypocty/VYPOCET-08-sj-kerr-ekvatorialni.md.`,
    { label: 'calc:sj-kerr-equatorial', phase: 'Rozšíření', model: 'opus', schema: CALC_RESULT }),

  // --- entropy-cluster reframe ---
  () => agent(`You are a hypothesis-maintenance agent (ECONOMY MODE) at ${ROOT}. The entropy-cluster hypothesis (H2g-3: SSEE truncation = crossed-product modular cutoff = LQG area gap) just received a complication: VYPOCET-06 (read ${KB}/vypocty/VYPOCET-06-ssee-4d.md + ${CD}/calculations/ssee-4d/results.json) found that in 4D the link-matrix Pauli-Jordan spectrum is NOT a clean power law, the cutoff exponent is non-robust (0.65–0.98), and nested diamonds give a VOLUME law — while 2D was clean (ρ^(−1/2), 39σ). Write ${KB}/hypotezy/H04-entropy-cluster-reframe.md IN CZECH: (1) co přesně 2D potvrdilo a 4D zkomplikovalo (čísla); (2) tři možné interpretace: (a) hypotéza platí jen pro konformně triviální 2D, (b) ve 4D je špatný OBJEKT — link-matrix G_R není to, co odpovídá modulárnímu cutoffu; správný kandidát = Pauli-Jordan z nelokálního BD d'Alembertiánu (Belenchia et al. 1507.00330) s lepším spektrem, (c) volume law je skutečný signál (SJ stav na diamantu není Hadamardův — cituj 2212.10592 — a volume law je jeho důsledek, viz též literaturu 2008.07697); (3) rozhodující experiment pro každou interpretaci; (4) doporučená cesta: BD-d'Alembertián verze 4D testu jako VYPOCET-09 kandidát. Honest, dense. Return structured result.`,
    { label: 'reframe:entropy-cluster', phase: 'Rozšíření', model: 'sonnet', schema: NOTE_RESULT }),

  // --- new pillar 19: von Neumann algebras ---
  () => agent(`You are a deep-research agent extending the quantum-gravity knowledge base at ${ROOT} with a NEW PILLAR (the completeness critic and three live hypotheses demand it). ToolSearch "select:WebSearch,WebFetch". Follow the EXACT conventions of existing pillars (look at ${KB}/foundations/16-conceptual-problems.md structure briefly and ${CD}/fragments/conceptual-problems.json schema).

PILLAR: Von Neumann Algebras & Modular Theory in Quantum Gravity (Von Neumannovy algebry a modulární teorie v kvantové gravitaci)
SCOPE: type I/II/III classification and physical meaning; Tomita-Takesaki modular theory, modular Hamiltonian, KMS; type III₁ of local QFT (Buchholz, Fredenhagen, Haag); Connes cocycle; crossed products and the 2022+ revolution: Chandrasekaran-Longo-Penington-Witten observer algebras, type II entropy = generalized entropy, JLMS; Connes-Rovelli thermal time hypothesis; modular inclusions and emergent geometry; half-sided modular inclusions; quantum reference frames ↔ crossed products (2412.15502 and related); applications to de Sitter, black holes, subregions; relation to our live hypotheses (SSEE truncation, SJ states, generalized entropy).

Deep research (8-12 searches, primary sources), then write BOTH files:
1. ${KB}/foundations/19-von-neumann-algebras.md — Czech prose, same structure as other pillars (TL;DR, Přehled, Klíčové koncepty, Matematický rámec with LaTeX, Klíčové výsledky a milníky with citations, Současný stav 2024-2026, Otevřené problémy, Vztahy k ostatním přístupům with explored ratings, Mapa konceptů mermaid, Reference). 350-700 lines, dense.
2. ${CD}/fragments/von-neumann-algebras.json — English, exact schema of other fragments (slug "von-neumann-algebras", concepts/formulas/references/openProblems/connections; globally meaningful concept ids — reuse existing ids like "crossed-product", "generalized-entropy", "tomita-takesaki" where the graph already has them; min 15/10/25/6/8). Connections to: entanglement-spacetime, black-holes-information, holography-adscft, semiclassical-gravity, conceptual-problems, causal-sets (SSEE!), loop-quantum-gravity (area gap), noncommutative-geometry (Connes!). NEVER invent arXiv IDs.
Return (structured): {file: fragment path, keyPoints: 3-5 Czech}`,
    { label: 'pillar:von-neumann', phase: 'Rozšíření', model: 'opus', schema: NOTE_RESULT }),
])

const kerr = ext[0]
const reframe = ext[1]
const pillar19 = ext[2]
log('Rozšíření hotovo (Kerr: ' + (kerr ? kerr.status : 'N/A') + '). Píšu draft článku…')

// ---------- Draft článku ----------
phase('Draft článku')

const kerrSummary = kerr ? JSON.stringify({ status: kerr.status, keyNumbers: kerr.keyNumbers, verdict: kerr.verdictForHypothesis }, null, 2) : 'Kerr calculation unavailable — write the draft from BTZ results alone and note the Kerr extension as in-progress.'

const paper = await agent(`You are a theoretical-physics paper-writing agent. Write the project's first paper draft IN ENGLISH (this is core logic output, not prose for the user). Sources: ${KB}/vypocty/VYPOCET-05-sj-rotujici-btz.md, ${CD}/calculations/sj-rotating-btz/results.json, ${KB}/hypotezy/H02-sj-kerr.md, and the fresh Kerr extension:
${kerrSummary}
(plus ${KB}/vypocty/VYPOCET-08-sj-kerr-ekvatorialni.md + ${CD}/calculations/sj-kerr-equatorial/results.json if they exist).

Write ${ROOT}/papers/draft-01-sj-rotating-spacetimes/draft.md — a complete arXiv-style draft:
- Title: e.g. "Sorkin-Johnston vacua in rotating spacetimes: numerical construction through the ergoregion" (improve if you can)
- Abstract (150-200 words), Introduction (the gap: no canonical vacuum for rotating BHs — Kay-Wald; SJ needs no timelike Killing vector — the point), Method (causal sets, 2D conformal trick G_R=C/2 with proper citations, BTZ + Kerr equatorial sections, sprinkling, SJ prescription), Results (existence inside ergoregions with machine-precision pairing; static control fails; null-slope zero exactly at r_erg; co-rotating link fraction; the opposite-sign asymmetry phenomenon A_caus vs A_W; conformal-invariance of spectrum → rotation lives in eigenvectors; BTZ↔Kerr universality if confirmed), Discussion (path to full 4D Kerr via Teukolsky/eigenvector signatures; relation to superradiance; limitations — 2D sections, modest N, SJ non-Hadamard caveats with citations), References (real, verified — pull from the writeups; NEVER invent).
- Mark clearly on line 1: "DRAFT v0.1 — generated ${DATE}, internal research draft, NOT submitted, requires human review."
Also write ${ROOT}/papers/draft-01-sj-rotating-spacetimes/TODO.md (EN): what a referee would attack + what must be strengthened before this could ever be real (larger N, more seeds, convergence study, analytic cross-checks, proper treatment of φ-periodicity, comparison to known BTZ vacua, authorship/ethics note that this is AI-assisted exploratory work).
Return a Czech 5-line summary: co draft tvrdí, co je nejsilnější, co je nejslabší.`,
  { label: 'paper:draft-01', phase: 'Draft článku', model: 'opus' })

// ---------- BRAINSTORM-03 ----------
phase('Brainstorm 03')

const roundData = JSON.stringify({
  gammaCardy: 'PROGRAM DEAD: Sen IR-universality — log coefficients disagree (LQG −2 vs Euclidean +1.71), constant-term comparison physically unmotivated. See hypotezy/H01 + decisive read.',
  sjBtz: kerr ? 'BTZ success + Kerr extension: ' + kerr.keyNumbers : 'BTZ success (VYPOCET-05); Kerr extension failed/unavailable',
  ssee4d: '4D: p=3/4 NOT robust (0.65–0.98 cutoff-dependent), volume law in nested diamonds; 2D clean ρ^(−1/2) does not naively generalize. See H04 reframe.',
  bmv: 'Continuous discriminators dead (AS 24, EFT 58, GUP 72 orders below reach; AS/EFT ratio = 1/ħ ≈ 10³⁴ dimensional finding). Binary discriminators (GIE yes/no) reachable 2030-35.',
  newPillar: pillar19 ? 'Pillar 19 von Neumann algebras added: ' + JSON.stringify(pillar19.keyPoints) : 'pillar 19 unavailable',
}, null, 2)

const brainstorm3 = await agent(`You are the third-round brainstorm synthesizer at ${ROOT}. The project now has: 8 calculations (VYPOCET-01..08), a killed program (γ–Cardy), a paper draft (papers/draft-01), a reframed entropy cluster (${KB}/hypotezy/H04-entropy-cluster-reframe.md), a new pillar (foundations/19-von-neumann-algebras.md), findings registry (${CD}/findings.json). Round summary:
${roundData}

Read selectively: BRAINSTORM-02.md (incl. its decisive-round section), H04, the new pillar's connections, findings.json. Write ${KB}/BRAINSTORM-03.md IN CZECH:
# Brainstorming 03 (${DATE})
## Bilance: co žije, co zemřelo   ← poctivá tabule všech hypotéz H2g-* + klastrů: status po kole 3
## Lekce z poprav                  ← co nás γ–Cardy smrt a 4D komplikace naučily o metodě (Sen-typ univerzalitní argumenty jako rychlý zabiják; volba objektu — link matrix vs BD d'Alembertián)
## Hypotézy třetí generace         ← 5-8 nových/zostřených; každá: tvrzení, opora (čísla!), proč nová, první test, confidence. Zahrň: opposite-sign asymetrie SJ stavu jako fyzikální jev (co znamená?); BD-d'Alembertián 4D SSEE (H04 cesta b); von Neumann pilíř → nové hrany (SSEE↔crossed product přes modulární teorii — teď s daty)
## Výpočetní fronta v2             ← seřazená; očekávám nahoře: VYPOCET-09 BD-d'Alembertián 4D, VYPOCET-10 SJ eigenvector superradiance analýza, plný Kerr program
## Strategie publikace             ← draft-01 je první; co může být draft-02 (kandidáti: d_s klasifikační tabulka jako review-note; a₄ fermionová identita; Λ prefactor neshoda jako krátká poznámka)
Return Czech summary: top 3 hypotézy třetí generace + nejlepší další tah.`,
  { label: 'brainstorm-03:synth', phase: 'Brainstorm 03', model: 'opus' })

// ---------- Úklid ----------
phase('Úklid')

const hkData = JSON.stringify({ kerr: kerr ? { status: kerr.status, keyNumbers: kerr.keyNumbers } : null, reframe: reframe, pillar19: pillar19, paper: paper, brainstorm3: brainstorm3 }, null, 2)

const housekeeping = await agent(`You are the housekeeping agent at ${ROOT}. Today ${DATE}. Czech prose / English data. ECONOMY MODE. Round-3 results:
${hkData}

TASK 1: Run with Bash: python3 ${ROOT}/workflows/consolidate.py && python3 ${ROOT}/workflows/consolidate.py --apply-merges  (the new pillar fragment von-neumann-algebras.json must flow into the registries; confirm node/edge counts grew).
TASK 2: Update ${CD}/findings.json: append findings from the decisive round + round 3 (γ–Cardy program killed by Sen IR-universality; SJ existence in rotating BTZ ergoregion + opposite-sign asymmetry; 4D SSEE non-robustness + volume law; BMV feasibility bounds incl. AS/EFT=1/ħ; Kerr extension result). Keep schema, conservative wording.
TASK 3: Update ${ROOT}/PROGRESS.md (Read first, preserve): log entry ${DATE} round 3 (one line per item: Kerr, reframe, pilíř 19, draft-01, BRAINSTORM-03); "Aktuální stav" → první draft článku hotov, čeká lidskou revizi; "Další kroky" from BRAINSTORM-03's výpočetní fronta v2.
TASK 4: Update ${KB}/00-INDEX.md: add papers/, VYPOCET-08, H04, pillar 19, BRAINSTORM-03.
Return 3-line Czech confirmation incl. new registry counts.`,
  { label: 'final:round3-writeup', phase: 'Úklid', model: 'sonnet' })

return {
  kerr: kerr ? { status: kerr.status, keyNumbers: kerr.keyNumbers } : null,
  kerrVerdict: kerr ? kerr.verdictForHypothesis : null,
  reframe: reframe,
  pillar19: pillar19,
  paperSummary: paper,
  brainstorm3Summary: brainstorm3,
  housekeeping: housekeeping,
}