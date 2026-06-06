export const meta = {
  name: 'qg-knowledge-foundation',
  description: 'Hloubková rešerše kvantové gravitace — 18 pilířů, verifikace citací, konsolidace do registrů, syntéza bílých míst',
  phases: [
    { title: 'Výzkum pilířů', detail: '18 paralelních výzkumných agentů, jeden na každý pilíř kvantové gravitace' },
    { title: 'Verifikace', detail: 'adversariální kontrola citací a vzorců, pilíř po pilíři (bez bariéry — startuje hned po dokončení pilíře)' },
    { title: 'Konsolidace', detail: 'sloučení JSON fragmentů do jednotných registrů: graf konceptů, reference, vzorce, problémy, souvislosti' },
    { title: 'Syntéza', detail: 'mapa souvislostí + bílá místa (SYNTEZA.md), completeness critic, index a progress tracker' },
  ],
}

const ROOT = '/Users/pazny/projects/theoryOfEverything'
const DATE = (args && args.date) || '2026-06-05'

const PILLARS = [
  { num: '01', dir: 'approaches', slug: 'string-theory', title: 'String Theory & M-theory', titleCz: 'Teorie strun a M-teorie',
    scope: 'Bosonic and superstring theory; the five superstring theories and their web of dualities (T/S/U); M-theory and 11D supergravity; D-branes; compactification (Calabi-Yau, flux compactifications, moduli stabilization); string field theory; matrix models (BFSS, IKKT); Hagedorn temperature and string thermodynamics; quantitative triumphs (Strominger-Vafa black hole microstate counting); current state of the field 2024-2026.' },
  { num: '02', dir: 'approaches', slug: 'loop-quantum-gravity', title: 'Loop Quantum Gravity & Spin Foams', titleCz: 'Smyčková kvantová gravitace a spinové pěny',
    scope: 'Canonical LQG: Ashtekar variables, holonomy-flux algebra, spin networks, discrete area and volume spectra, quantum geometry; covariant approach: spin foam models (EPRL-FK), semiclassical limit and graviton propagator; LQG black holes (isolated horizons, entropy counting, Barbero-Immirzi parameter); coarse-graining and renormalization of spin foams; numerical spin foams (effective dynamics); criticisms and open issues.' },
  { num: '03', dir: 'approaches', slug: 'asymptotic-safety', title: 'Asymptotic Safety', titleCz: 'Asymptotická bezpečnost',
    scope: 'Weinberg asymptotic safety conjecture; functional renormalization group and Wetterich equation; Reuter fixed point; Einstein-Hilbert truncation and higher-order truncations; critical exponents; matter-gravity systems and constraints on Standard Model field content; the Higgs mass retrodiction (Shaposhnikov-Wetterich); relation to lattice approaches and CDT; criticisms (unitarity, Lorentzian vs Euclidean, scheme dependence); state of the art 2024-2026.' },
  { num: '04', dir: 'approaches', slug: 'causal-dynamical-triangulations', title: 'Causal Dynamical Triangulations', titleCz: 'Kauzální dynamické triangulace',
    scope: 'Lattice quantum gravity via CDT: Regge calculus background, causal time-slicing, Monte Carlo simulations; phase diagram (phases A, B, C, C_b and phase transitions); emergence of 4D de Sitter-like universe; spectral dimension running from 4 to ~2 in UV; transfer matrix; relation to Horava-Lifshitz gravity and asymptotic safety; Euclidean dynamical triangulations history and why causality matters; recent results.' },
  { num: '05', dir: 'approaches', slug: 'causal-sets', title: 'Causal Set Theory', titleCz: 'Teorie kauzálních množin',
    scope: 'Causal set program (Bombelli-Lee-Meyer-Sorkin): order + number = geometry; kinematics (sprinkling, Hauptvermutung); discrete d Alembertian and Benincasa-Dowker action; classical sequential growth dynamics and quantum dynamics attempts; Sorkin prediction of cosmological constant fluctuations (Lambda ~ 1/sqrt(V)); nonlocality; entanglement entropy on causal sets; swerves and phenomenology; current state.' },
  { num: '06', dir: 'approaches', slug: 'group-field-theory', title: 'Group Field Theory & Tensor Models', titleCz: 'Group field theory a tenzorové modely',
    scope: 'GFT as quantum field theory on group manifolds; relation to spin foams and LQG; matrix models for 2D gravity and double-scaling limit; tensor models and colored tensor models (Gurau), 1/N expansion, melonic dominance; GFT condensate cosmology (emergent bounce, effective Friedmann equations); SYK model connection to tensor models; renormalization of GFTs; current state.' },
  { num: '07', dir: 'approaches', slug: 'noncommutative-geometry', title: 'Noncommutative Geometry', titleCz: 'Nekomutativní geometrie',
    scope: 'Connes spectral triples and reconstruction of geometry from algebra; spectral action principle and derivation of Standard Model coupled to gravity (Chamseddine-Connes); almost-commutative geometry and particle physics predictions; noncommutative spacetimes (Moyal plane, kappa-Minkowski); doubly/deformed special relativity; minimal length scenarios and generalized uncertainty principle (GUP); fuzzy spaces; current state.' },
  { num: '08', dir: 'approaches', slug: 'twistors-amplitudes', title: 'Twistor Theory & the Amplitudes Program', titleCz: 'Twistory a teorie amplitud',
    scope: 'Penrose twistor theory and nonlinear graviton; twistor string theory (Witten 2003); modern scattering amplitudes program: spinor-helicity, BCFW recursion, on-shell methods; amplituhedron and positive geometries (Arkani-Hamed-Trnka); double copy (BCJ duality: gravity = gauge squared), KLT relations; UV behavior of gravity amplitudes; celestial amplitudes and w(1+infinity) symmetry; self-dual sectors; how spacetime emergence is viewed from amplitudes; current state.' },
  { num: '09', dir: 'approaches', slug: 'emergent-gravity', title: 'Emergent & Entropic Gravity', titleCz: 'Emergentní a entropická gravitace',
    scope: 'Sakharov induced gravity; Jacobson thermodynamic derivation of Einstein equations (1995) and entanglement equilibrium (2015); Verlinde entropic gravity (2011) and emergent gravity with dark-matter-like effects (2016), observational tests; Padmanabhan thermodynamic gravity program; analog gravity: acoustic black holes, BEC analogues, Steinhauer Hawking radiation experiments, what analogues do and do not prove; gravity as hydrodynamics; condensed-matter-inspired views (Volovik, Hu); critiques.' },
  { num: '10', dir: 'approaches', slug: 'supergravity-uv', title: 'Supergravity & UV Behavior of Perturbative Gravity', titleCz: 'Supergravitace a UV chování kvantové gravitace',
    scope: 'Perturbative quantum gravity and nonrenormalizability (Goroff-Sagnotti two-loop divergence); gravity as effective field theory (Donoghue), reliable low-energy quantum predictions; supergravity N=1..8; N=8 supergravity UV finiteness through high loops, enhanced cancellations, current status of the finiteness question; higher-derivative gravity (Stelle, quadratic gravity, agravity) and the ghost problem; Horava-Lifshitz gravity; nonlocal ghost-free gravity; conformal gravity; unimodular gravity; shape dynamics.' },
  { num: '11', dir: 'cross-cutting', slug: 'holography-adscft', title: 'Holographic Principle & AdS/CFT', titleCz: 'Holografický princip a AdS/CFT',
    scope: 'Bekenstein bound and black hole entropy as origin of holography; t Hooft and Susskind holographic principle; covariant entropy bound (Bousso); AdS/CFT correspondence (Maldacena 1997), GKP-Witten dictionary, tests via integrability and localization; holographic RG flow; applications (quark-gluon plasma, condensed matter); the problem of de Sitter holography and dS/CFT; celestial holography for flat space; holography of information (Raju); status of holography beyond AdS; 2024-2026 developments.' },
  { num: '12', dir: 'cross-cutting', slug: 'black-holes-information', title: 'Black Hole Thermodynamics & the Information Paradox', titleCz: 'Černé díry a informační paradox',
    scope: 'Black hole thermodynamics (Bekenstein entropy, Hawking radiation, four laws); information paradox precise formulations; Page curve and Page time; black hole complementarity; firewalls (AMPS paradox); fuzzballs (Mathur); soft hair (Hawking-Perry-Strominger); the 2019-2020 breakthrough: quantum extremal surfaces, islands, replica wormholes (Penington; Almheiri-Engelhardt-Marolf-Maxfield), what it does and does not resolve; interior reconstruction, state dependence; complexity and black holes; remnants; evaporation endpoint; current debates 2024-2026.' },
  { num: '13', dir: 'cross-cutting', slug: 'entanglement-spacetime', title: 'Entanglement & Emergence of Spacetime (It from Qubit)', titleCz: 'Entanglement a emergence prostoročasu',
    scope: 'Ryu-Takayanagi and HRT holographic entanglement entropy, quantum corrections (FLM, QES); entanglement builds geometry (Van Raamsdonk); ER=EPR (Maldacena-Susskind); tensor networks: MERA, HaPPY code, holographic quantum error correction; bulk reconstruction and subregion duality; first law of entanglement and deriving linearized Einstein equations (Faulkner et al.); SYK model and near-AdS2 holography; complexity=volume and complexity=action conjectures; quantum focusing conjecture; emergent time; gravity from quantum information principles; criticisms and limits of the program.' },
  { num: '14', dir: 'cross-cutting', slug: 'swampland', title: 'Swampland Program & the String Landscape', titleCz: 'Swampland a krajina teorie strun',
    scope: 'String landscape statistics and the anthropic debate; swampland program: weak gravity conjecture (and proofs/evidence), distance conjecture, de Sitter conjectures, no global symmetries, completeness hypothesis, cobordism conjecture, emergent string conjecture, festina lente; status of de Sitter vacua (KKLT and its critics, 2024-2026 state); implications for inflation, dark energy, neutrino masses, cosmology; trans-Planckian censorship; sharpening vs falsification; relations to black hole physics and holography.' },
  { num: '15', dir: 'foundations', slug: 'semiclassical-gravity', title: 'QFT in Curved Spacetime & Semiclassical Gravity', titleCz: 'Semiklasická gravitace a QFT v zakřiveném prostoročase',
    scope: 'QFT in curved spacetime: Bogoliubov transformations, Unruh effect, Hawking radiation derivations and their robustness (trans-Planckian question), cosmological particle production; renormalized stress-energy tensor, trace anomaly; semiclassical Einstein equations, their validity limits and failure modes; stochastic gravity (Hu-Verdaguer); gravitationally induced decoherence; decoherence of spacetime superpositions; Wald entropy and gravitational entropy generally; algebraic QFT in curved spacetime; recent rigorous results.' },
  { num: '16', dir: 'foundations', slug: 'conceptual-problems', title: 'Conceptual Problems of Quantum Gravity', titleCz: 'Konceptuální problémy kvantové gravitace',
    scope: 'Problem of time (Wheeler-DeWitt, deparametrization, Page-Wootters relational time); background independence and what it demands; diffeomorphism-invariant observables (relational/dressed observables); singularity theorems and prospects of resolution; cosmological constant problem (Weinberg no-go); measurement problem in QG and role of the observer; quantum reference frames; gravitationally induced collapse (Penrose, Diosi) and its tests; locality vs unitarity tension; emergence of classicality; does gravity even need quantizing — arguments pro and con (Eppley-Hannah, Mari et al., recent debates).' },
  { num: '17', dir: 'phenomenology', slug: 'experimental-tests', title: 'Quantum Gravity Phenomenology & Experimental Tests', titleCz: 'Experimentální testy a fenomenologie kvantové gravitace',
    scope: 'Lorentz invariance violation bounds (Fermi GRB time-of-flight, UHECR, neutrinos); Planck-scale dispersion relations; tabletop quantum gravity: gravitationally induced entanglement proposals (Bose-Marletto-Vedral) and experimental roadmap, status 2024-2026; massive superposition experiments (optomechanics, levitated nanoparticles); atom interferometry (MAGIS-100); gravitational wave probes (echoes, ringdown spectroscopy, memory, stochastic background); Planck-scale holographic noise (holometer results); CMB imprints of quantum gravity; gravitational decoherence tests; minimal length phenomenology; honest assessment of what is testable.' },
  { num: '18', dir: 'phenomenology', slug: 'quantum-cosmology', title: 'Quantum Cosmology', titleCz: 'Kvantová kosmologie',
    scope: 'Wheeler-DeWitt equation and minisuperspace; Hartle-Hawking no-boundary proposal, Vilenkin tunneling; the no-boundary controversy (Feldbrugge-Lehners-Turok and responses); loop quantum cosmology: big bounce, effective dynamics, potential CMB signatures; string cosmology: string gas, pre-big-bang, ekpyrotic/cyclic; inflation and the trans-Planckian problem; eternal inflation and the measure problem; multiverse; dark energy from quantum gravity perspectives; quantum origin of structure; current observational constraints.' },
]

const PILLAR_SUMMARY = {
  type: 'object',
  properties: {
    slug: { type: 'string' },
    status: { type: 'string', description: 'ok | partial (partial = some scope areas could not be researched deeply)' },
    counts: {
      type: 'object',
      properties: {
        concepts: { type: 'number' },
        formulas: { type: 'number' },
        references: { type: 'number' },
        openProblems: { type: 'number' },
        connections: { type: 'number' },
      },
      required: ['concepts', 'formulas', 'references', 'openProblems', 'connections'],
    },
    keyInsights: { type: 'array', items: { type: 'string' }, description: '3-6 nejdůležitějších poznatků (česky)' },
  },
  required: ['slug', 'status', 'counts', 'keyInsights'],
}

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

const GRAPH_RESULT = {
  type: 'object',
  properties: {
    nodes: { type: 'number' },
    edges: { type: 'number' },
    mergedDuplicates: { type: 'number' },
    topHubs: { type: 'array', items: { type: 'string' }, description: '10 concept ids with the most edges' },
  },
  required: ['nodes', 'edges', 'mergedDuplicates', 'topHubs'],
}

const REF_RESULT = {
  type: 'object',
  properties: {
    total: { type: 'number' },
    afterDedup: { type: 'number' },
    withArxivOrDoi: { type: 'number' },
  },
  required: ['total', 'afterDedup', 'withArxivOrDoi'],
}

const FORMULA_RESULT = {
  type: 'object',
  properties: {
    total: { type: 'number' },
    afterDedup: { type: 'number' },
  },
  required: ['total', 'afterDedup'],
}

const PROBLEMS_RESULT = {
  type: 'object',
  properties: {
    problems: { type: 'number' },
    connections: { type: 'number' },
    barelyExplored: {
      type: 'array',
      items: {
        type: 'object',
        properties: {
          from: { type: 'string' },
          to: { type: 'string' },
          description: { type: 'string' },
        },
        required: ['from', 'to', 'description'],
      },
      description: 'top 15 cross-approach connections rated barely explored — the hunting ground',
    },
    sharedProblems: { type: 'array', items: { type: 'string' }, description: 'top 10 open problems shared by the most pillars' },
  },
  required: ['problems', 'connections', 'barelyExplored', 'sharedProblems'],
}

const CRITIC_RESULT = {
  type: 'object',
  properties: {
    gaps: {
      type: 'array',
      items: {
        type: 'object',
        properties: {
          what: { type: 'string' },
          why: { type: 'string' },
          priority: { type: 'string', description: 'high | medium | low' },
        },
        required: ['what', 'why', 'priority'],
      },
    },
    structuralIssues: { type: 'array', items: { type: 'string' } },
  },
  required: ['gaps', 'structuralIssues'],
}

// Pilíře, jejichž research agent v prvním běhu zapsal soubory, ale spadl na session limit
// před odevzdáním StructuredOutput → soubory na disku existují, journal cache je prázdná.
const FAILED_FIRST_RUN = new Set(['asymptotic-safety', 'causal-dynamical-triangulations', 'supergravity-uv', 'entanglement-spacetime', 'swampland', 'semiclassical-gravity', 'conceptual-problems', 'experimental-tests', 'quantum-cosmology'])

function kbFile(p) { return ROOT + '/knowledge-base/' + p.dir + '/' + p.num + '-' + p.slug + '.md' }
function fragFile(p) { return ROOT + '/core-data/fragments/' + p.slug + '.json' }

const ALL_SLUGS = PILLARS.map(p => p.slug).join(', ')

function pillarPrompt(p) {
  const resumeNote = FAILED_FIRST_RUN.has(p.slug)
    ? 'IMPORTANT — RESUMED RUN: A previous agent already researched this pillar and wrote BOTH output files described below, but crashed (session limit) before reporting its summary. Do NOT redo the research from scratch. Instead: (1) Read both existing output files; (2) audit them against EVERY requirement below (section structure, minimum counts, valid JSON, no truncation, citation format); (3) repair and complete whatever is missing, thin, or truncated — do targeted web research ONLY to fill those gaps; (4) return the structured summary with the true final counts of the files as they stand.\n\n'
    : ''
  return resumeNote + `You are a deep-research agent building a quantum-gravity knowledge base for a long-term research project whose goal is to accumulate maximal structured context data so that AI can later hunt for YET-UNDISCOVERED CONNECTIONS between approaches to quantum gravity.

YOUR PILLAR: ${p.title} (${p.titleCz})
SCOPE: ${p.scope}

STEP 0 — load web tools: call ToolSearch with query "select:WebSearch,WebFetch" before anything else.

STEP 1 — DEEP RESEARCH. Run at least 10-14 distinct web searches covering the whole scope; fetch and actually read key sources (arXiv abstracts, review articles, Living Reviews in Relativity, Scholarpedia, SEP — Stanford Encyclopedia of Philosophy, lecture notes). Prioritize: (a) foundational original papers, (b) authoritative modern reviews 2015-2026, (c) the newest developments 2023-2026, (d) exact formulas and quantitative results, (e) explicit statements of open problems, (f) explicitly discussed OR conspicuously missing links to other approaches. Today is ${DATE}.

STEP 2 — write OUTPUT FILE 1 (Czech prose) to: ${kbFile(p)}
Markdown, written IN CZECH (Czech physics terminology; the English original term in parentheses at first use; direct quotations kept in original English with a short Czech gloss). Structure:

# ${p.titleCz} (${p.title})
> **TL;DR** — 3-5 vět shrnutí.
## Přehled a historický kontext
## Klíčové koncepty            ← each concept with its English term; dense, factual
## Matematický rámec           ← display formulas as LaTeX in $$...$$ blocks, each followed by a Czech explanation of every symbol and the formula's significance
## Klíčové výsledky a milníky  ← with inline citations like [Strominger & Vafa 1996](https://arxiv.org/abs/hep-th/9601029)
## Současný stav (2024-2026)   ← what the field is actually doing NOW
## Otevřené problémy           ← numbered, precise statements, why each is hard
## Vztahy k ostatním přístupům ← explicit subsections per related approach; for each relation state HOW WELL EXPLORED it is (dobře / částečně / sotva prozkoumáno) — this matters most for the project
## Mapa konceptů               ← one Mermaid diagram (graph TD) of the pillar's internal concept relations
## Reference                   ← numbered, full citations with arXiv/DOI links

Quality bar: 350-700 lines, dense with facts, numbers, formulas and citations — zero filler. Every factual claim traceable to a reference. NEVER invent an arXiv ID or citation; cite only what you actually saw during research.

STEP 3 — write OUTPUT FILE 2 (English machine-readable core data) to: ${fragFile(p)}
A single valid JSON object, entirely in ENGLISH, with exactly this shape:

{
  "slug": "${p.slug}",
  "name": "${p.title}",
  "concepts":     [{ "id": "...", "name": "...", "definition": "...", "relatedTo": ["other-concept-ids"] }],
  "formulas":     [{ "id": "...", "name": "...", "latex": "...", "meaning": "...", "source": "ref-id" }],
  "references":   [{ "id": "...", "authors": "...", "title": "...", "year": 0, "arxiv": "...", "doi": "...", "url": "...", "significance": "..." }],
  "openProblems": [{ "id": "...", "statement": "...", "whyHard": "...", "attempts": "..." }],
  "connections":  [{ "from": "${p.slug}", "to": "...", "type": "duality|limit|shared-structure|shared-math|conflict|conjecture", "description": "...", "explored": "well|partially|barely" }]
}

Rules for the fragment:
- All ids kebab-case English. Concept ids must be GLOBALLY meaningful (e.g. "holographic-principle", "spectral-dimension", "page-curve") — other pillars will use the same ids, enabling cross-linking. Use the canonical community name for shared concepts.
- "connections.to" should name another pillar slug when the bridge targets a whole approach (known pillar slugs: ${ALL_SLUGS}) or a global concept id otherwise.
- The "connections" array is the most valuable output: record EVERY known or conjectured bridge from this pillar to other approaches/concepts, and honestly rate "explored". Connections rated "barely" are the gold this project mines for — include speculative-but-grounded ones and say in "description" what evidence exists.
- Minimums (more is better if real): 15 concepts, 10 formulas, 25 references, 6 openProblems, 8 connections.
- references: year as number; omit "arxiv"/"doi" fields rather than guessing; "significance" = one line on why this paper matters.

FINAL: return the structured summary (counts must match what you actually wrote; keyInsights in Czech).`
}

function verifyPrompt(p) {
  return `You are an adversarial verification agent. A research agent just produced two files for the pillar "${p.title}":
- Czech prose: ${kbFile(p)}
- English JSON fragment: ${fragFile(p)}

Your job: assume errors exist and hunt for them.

STEP 0: call ToolSearch with query "select:WebFetch,WebSearch" to load web tools.
STEP 1: Read both files. If the JSON is not valid JSON, fix it first.
STEP 2: Reference audit — sample at least 12 references (prioritize the ones supporting the strongest claims). For each, WebFetch the arXiv abstract page (https://arxiv.org/abs/ID) or DOI and verify: the ID resolves, AND title + authors + year actually match. Watch for: invented IDs, wrong author attribution, wrong year, title paraphrased into something that does not exist.
STEP 3: Formula audit — check at least 5 of the most important formulas against authoritative sources (correct coefficients, signs, conventions stated).
STEP 4: Consistency audit — concept ids referenced in "relatedTo"/"connections" exist or are plausible global ids; the Czech prose does not contradict the JSON; "explored" ratings are honest (a famous well-studied duality must not be rated "barely").
STEP 5: FIX problems directly with Edit: correct wrong metadata; DELETE unverifiable references (and their citations in prose); tag claims you could not verify with "⚠️ neověřeno". Keep JSON valid after edits.
STEP 6: Write a short verification report IN CZECH to ${ROOT}/verification/${p.slug}.md — what was checked, what was wrong, what was fixed, what remains uncertain.

Return the structured result (remainingConcerns in Czech).`
}

// ---------- Fáze 1+2: výzkum pilířů, verifikace hned jak pilíř doběhne (pipeline, žádná bariéra) ----------
phase('Výzkum pilířů')
log('Spouštím 18 výzkumných agentů — každý pilíř dostane vlastní hloubkovou rešerši…')

const pillarResults = await pipeline(
  PILLARS,
  (p) => agent(pillarPrompt(p), { label: 'research:' + p.slug, phase: 'Výzkum pilířů', schema: PILLAR_SUMMARY }),
  (summary, p) => agent(verifyPrompt(p), { label: 'verify:' + p.slug, phase: 'Verifikace', schema: VERIFY_RESULT })
    .then(v => ({ summary: summary, verify: v, slug: p.slug }))
)

const done = pillarResults.filter(Boolean)
const failed = PILLARS.filter(p => !done.some(d => d.slug === p.slug)).map(p => p.slug)
if (failed.length) log('⚠️ Nedokončené pilíře (vypadly z pipeline): ' + failed.join(', '))
log('Hotovo ' + done.length + '/18 pilířů. Konsoliduji fragmenty do jednotných registrů…')

// ---------- Fáze 3: konsolidace (bariéra je tu správně — mergery potřebují VŠECHNY fragmenty) ----------
phase('Konsolidace')

const FRAGMENT_LIST = PILLARS.map(p => fragFile(p)).join('\n')
const mergerIntro = `You are a data-consolidation agent for a quantum-gravity knowledge base. Read ALL of these JSON fragment files (skip gracefully any that are missing):\n${FRAGMENT_LIST}\n\nAll output is in ENGLISH. Write valid, pretty-printed JSON.`

const consolidation = await parallel([
  () => agent(mergerIntro + `

TASK: build the unified concept graph at ${ROOT}/core-data/concept-graph.json with shape:
{ "nodes": [{ "id", "name", "definition", "aliases": [], "pillars": ["slugs where it appears"] }],
  "edges": [{ "from", "to", "type", "description", "explored", "sourcePillars": [] }] }

- Merge duplicate concepts: the same physical concept under different ids becomes ONE canonical node (canonical community name as id; other ids go to "aliases"). Be aggressive about merging true duplicates, conservative about merging genuinely distinct concepts.
- Edges come from fragments' "connections" arrays AND from concepts' "relatedTo" links (type "shared-structure" with explored "well" unless evidence says otherwise). Deduplicate edges; union sourcePillars.
- EVERY concept from every fragment must end up in the graph (as node or alias). No silent drops.
Return the structured result.`, { label: 'merge:concept-graph', phase: 'Konsolidace', schema: GRAPH_RESULT }),

  () => agent(mergerIntro + `

TASK: build the unified bibliography.
1) ${ROOT}/core-data/references.json — array of { "id", "authors", "title", "year", "arxiv", "doi", "url", "significance", "pillars": [] }. Deduplicate by arXiv ID, then DOI, then near-identical title; union "pillars"; keep the best-written significance. Sort by year ascending.
2) ${ROOT}/core-data/references.bib — the same library as valid BibTeX (@article/@book/@misc, citekeys like strominger1996microscopic, include eprint/doi fields).
Return the structured result.`, { label: 'merge:references', phase: 'Konsolidace', schema: REF_RESULT }),

  () => agent(mergerIntro + `

TASK: build the unified formula registry at ${ROOT}/core-data/formulas.json — array of { "id", "name", "latex", "meaning", "pillars": [], "source" }. Deduplicate identical formulas across pillars (e.g. Bekenstein-Hawking entropy will appear many times — one entry, union pillars). Sanity-check LaTeX (balanced braces, no obvious mangling); fix trivial issues. Group the array ordered by pillar then importance.
Return the structured result.`, { label: 'merge:formulas', phase: 'Konsolidace', schema: FORMULA_RESULT }),

  () => agent(mergerIntro + `

TASK: build the two registries that matter most for hunting undiscovered connections.
1) ${ROOT}/core-data/open-problems.json — array of { "id", "statement", "whyHard", "attempts", "pillars": [] }. Merge duplicates (the same problem stated by several pillars — e.g. the cosmological constant problem — becomes one entry with all pillars). Order by number of pillars sharing the problem, descending.
2) ${ROOT}/core-data/connections.json — { "connections": [ every cross-pillar/cross-concept connection: { "from", "to", "type", "description", "explored", "sourcePillars": [] } ], "matrix": { pillar-slug: { pillar-slug: "well|partially|barely|none" } } }. Deduplicate; when two pillars rate the same connection differently, keep the more conservative (less explored) rating and note the disagreement in description.
Return the structured result (barelyExplored = the 15 most interesting barely-explored connections; sharedProblems = 10 problems shared by most pillars).`, { label: 'merge:problems-connections', phase: 'Konsolidace', schema: PROBLEMS_RESULT }),
])

const graph = consolidation[0]
const refs = consolidation[1]
const formulas = consolidation[2]
const problems = consolidation[3]
log('Registry hotové. Spouštím syntézu a completeness critic…')

// ---------- Fáze 4: syntéza ----------
phase('Syntéza')

const huntingGround = problems ? JSON.stringify(problems.barelyExplored, null, 2) : '[]'
const sharedProblems = problems ? JSON.stringify(problems.sharedProblems, null, 2) : '[]'
const topHubs = graph ? JSON.stringify(graph.topHubs) : '[]'

const synthesis = await parallel([
  () => agent(`You are the synthesis agent (run v2 — the previous run died on a session limit; ignore any half-finished SYNTEZA.md and rewrite it fully) for a quantum-gravity knowledge base at ${ROOT}. The project goal: accumulate structured context so AI can hunt for yet-undiscovered connections between approaches.

Inputs to read: ${ROOT}/core-data/connections.json, ${ROOT}/core-data/open-problems.json, ${ROOT}/core-data/concept-graph.json, and skim the pillar files under ${ROOT}/knowledge-base/. Pre-computed highlights — top concept hubs: ${topHubs}; barely-explored connections:\n${huntingGround}\nshared problems:\n${sharedProblems}

Write ${ROOT}/knowledge-base/SYNTEZA.md IN CZECH (English terms in parentheses at first use):

# Syntéza: Mapa kvantové gravitace
## Velký obraz                          ← kde dnes každý přístup stojí, jednou-dvěma odstavci
## Mapa vztahů mezi přístupy            ← Mermaid diagram (graph LR) všech 18 pilířů s hranami podle connections.json (sílu/prozkoumanost vyznač stylem hran) + komentář
## Kde se přístupy shodují              ← konvergentní výsledky nezávislých přístupů (např. dimenzionální redukce v UV, entropie černých děr…)
## Kde si protiřečí                     ← skutečné konflikty a neslučitelné předpoklady
## Sdílené otevřené problémy            ← z open-problems.json, čím víc pilířů, tím výš
## Bílá místa: sotva prozkoumané souvislosti  ← JÁDRO DOKUMENTU: pro každou barely-explored souvislost: co to je, proč je zajímavá, jaká data k ní v knowledge base máme, konkrétní první krok k prověření
## Kandidátní hypotézy k prověření      ← 5-10 spekulativních, ale podložených kandidátů na "nenalezené souvislosti" — každý s odůvodněním a testem, který by ho vyvrátil

Dense, honest, zero filler. Cite core-data files and pillar files by path. Return a 5-line Czech summary of the most promising white spaces.`, { label: 'synthesis:SYNTEZA.md', phase: 'Syntéza' }),

  () => agent(`You are a completeness critic for the quantum-gravity knowledge base at ${ROOT}. Inventory the whole tree (knowledge-base/, core-data/, verification/). The project goal: maximal structured context for AI to hunt undiscovered connections between quantum-gravity approaches.

Ask: what is MISSING?
- Topics/pillars not covered (e.g. specific research programs, mathematical tools like higher category theory / operads / von Neumann algebras type III, historical failed approaches worth mining, adjacent fields — quantum information, condensed matter dualities)?
- Data types missing (numerical datasets, tables of bounds/constraints, timelines, people/collaboration graphs, code/simulation resources)?
- Structural issues (inconsistent concept ids across fragments, broken cross-links, pillars whose connections arrays ignore each other asymmetrically)?
DO NOT modify any files. Return the structured result (gaps and structuralIssues in Czech).`, { label: 'critic:completeness', phase: 'Syntéza', schema: CRITIC_RESULT }),
])

const syntezaSummary = synthesis[0]
const critic = synthesis[1]

// statistiky pro PROGRESS.md
const statsRows = done.map(d => {
  const c = d.summary && d.summary.counts ? d.summary.counts : { concepts: 0, formulas: 0, references: 0, openProblems: 0, connections: 0 }
  const v = d.verify || { referencesChecked: 0, problemsFound: 0, fixed: 0 }
  return d.slug + ' | concepts:' + c.concepts + ' formulas:' + c.formulas + ' refs:' + c.references + ' problems:' + c.openProblems + ' connections:' + c.connections + ' | verified:' + v.referencesChecked + ' found:' + v.problemsFound + ' fixed:' + v.fixed
}).join('\n')
const gapsJson = critic ? JSON.stringify(critic.gaps, null, 2) : '[]'
const structJson = critic ? JSON.stringify(critic.structuralIssues, null, 2) : '[]'

const finalAgent = await agent(`You are the housekeeping agent (run v2 — the previous run died on a session limit; ignore any stale 00-INDEX.md) for the quantum-gravity knowledge base at ${ROOT}. Today is ${DATE}. Work IN CZECH.

TASK 1: write ${ROOT}/knowledge-base/00-INDEX.md — an annotated index of EVERY file under knowledge-base/, core-data/ and verification/ (use Glob/Bash ls to enumerate; Read files briefly where needed for a good hook). One line per file: link + jednověté lákadlo co uvnitř. Group by section, start with SYNTEZA.md and the core-data registries.

TASK 2: update ${ROOT}/PROGRESS.md (Read it first; preserve its structure):
- mark Fáze 1 as ✅ dokončeno with date ${DATE}; switch "Aktuální stav" accordingly; set Fáze 2 to "připraveno".
- fill "## Statistiky" with a markdown table built from these per-pillar rows:\n${statsRows}\n  plus totals${refs ? ' (references after dedup: ' + refs.afterDedup + ', with arXiv/DOI: ' + refs.withArxivOrDoi + ')' : ''}${graph ? ' (concept graph: ' + graph.nodes + ' nodes, ' + graph.edges + ' edges)' : ''}${formulas ? ' (formulas after dedup: ' + formulas.afterDedup + ')' : ''}${problems ? ' (open problems: ' + problems.problems + ', connections: ' + problems.connections + ')' : ''}.
- fill "## Další kroky" from the completeness critic output — gaps:\n${gapsJson}\nstructural issues:\n${structJson}\n  Order by priority; phrase as actionable steps for Fáze 2.
- append a log entry for ${DATE} completion${failed.length ? '; note that these pillars did not complete and need a re-run: ' + failed.join(', ') : ''}.

Return a 3-line Czech confirmation of what you wrote.`, { label: 'final:index+progress', phase: 'Syntéza' })

return {
  pillarsCompleted: done.length,
  pillarsFailed: failed,
  conceptGraph: graph,
  references: refs,
  formulas: formulas,
  problemsAndConnections: problems ? { problems: problems.problems, connections: problems.connections, barelyExplored: problems.barelyExplored, sharedProblems: problems.sharedProblems } : null,
  criticGaps: critic ? critic.gaps : [],
  syntezaSummary: syntezaSummary,
  finalNote: finalAgent,
}