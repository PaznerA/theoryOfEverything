export const meta = {
  name: 'qg-novelty-check',
  description: 'Fáze 2, krok 1: oprava datového rozporu d_s + novelty check 5 hypotézních klastrů a citovaných preprintů proti literatuře (vše sonnet, ekonomický režim)',
  phases: [
    { title: 'Oprava dat', detail: 'vyřešení rozporu o směru běhu spektrální dimenze v kauzálních množinách (hrany 501 vs 1539)', model: 'sonnet' },
    { title: 'Novelty check', detail: '6 paralelních kontrol proti literatuře: 5 hypotézních klastrů + ověření citovaných preprintů', model: 'sonnet' },
    { title: 'Zápis', detail: 'novelty-checks.json + aktualizace BRAINSTORM-01.md a PROGRESS.md', model: 'sonnet' },
  ],
}

const ROOT = '/Users/pazny/projects/theoryOfEverything'
const CD = ROOT + '/core-data'
const DATE = (args && args.date) || '2026-06-06'

const NOVELTY = {
  type: 'object',
  properties: {
    cluster: { type: 'string' },
    verdict: { type: 'string', description: 'known | partially-known | plausibly-novel' },
    priorArt: {
      type: 'array',
      items: {
        type: 'object',
        properties: {
          title: { type: 'string' },
          arxiv: { type: 'string' },
          year: { type: 'number' },
          relation: { type: 'string', description: 'how exactly it overlaps with the hypothesis' },
        },
        required: ['title', 'relation'],
      },
    },
    whatRemainsNovel: { type: 'string', description: 'the part of the hypothesis NOT covered by prior art, if any' },
    recommendation: { type: 'string', description: 'pursue | reframe | drop' },
    notes: { type: 'string', description: 'Czech, 2-4 sentences' },
  },
  required: ['cluster', 'verdict', 'priorArt', 'whatRemainsNovel', 'recommendation', 'notes'],
}

const FIX_RESULT = {
  type: 'object',
  properties: {
    resolution: { type: 'string', description: 'what the literature actually says about CST spectral dimension direction' },
    bothCorrect: { type: 'boolean', description: 'true if the two edges describe different probes/definitions and both are right' },
    fragmentsEdited: { type: 'array', items: { type: 'string' } },
    registriesRebuilt: { type: 'boolean' },
    note: { type: 'string', description: 'Czech, 2-3 sentences' },
  },
  required: ['resolution', 'bothCorrect', 'fragmentsEdited', 'registriesRebuilt', 'note'],
}

const ECON = `ECONOMY MODE: minimal reads (Grep/partial), no redundant fetches, no re-reads. `

// ---------- Fáze 1: oprava datového rozporu d_s ----------
phase('Oprava dat')
log('Řeším rozpor o směru běhu spektrální dimenze v causal sets…')

const dsFix = await agent(ECON + `You are a data-conflict resolver for a quantum-gravity knowledge base. Our concept graph contains two contradicting claims about the spectral dimension in causal set theory:

EDGE A (concept-graph edge 501, from fragment ${CD}/fragments/causal-sets.json): "Causal-set random walks / nonlocal d'Alembertians give a scale-dependent spectral dimension that DROPS at short scales (sometimes to ~2), echoing CDT, asymptotic safety..."
EDGE B (edge 1539, from fragment ${CD}/fragments/noncommutative-geometry.json): "...the spectral dimension runs oppositely (decreases in NCG, INCREASES in causal sets)".

STEP 0: ToolSearch "select:WebSearch,WebFetch".
STEP 1: Establish from the literature what is actually true. Key candidates to check: Eichhorn & Mizera (arXiv:1311.2530, random-walk spectral dimension on causal sets), Belenchia-Benincasa-Marciano-Modesto (nonlocal d'Alembertian spectral dimension), Carlip (arXiv:1506.08775, dimensional reduction in causal set gravity), Eichhorn-Mizera-Surya. Likely resolution: the answer is PROBE-DEPENDENT (random walk on the discrete order increases d_s; the nonlocal d'Alembertian / continuum-inspired probes give reduction toward 2) — but VERIFY this against the actual papers, do not assume.
STEP 2: Fix the source FRAGMENTS (not the generated registries): edit the relevant "connections" descriptions in ${CD}/fragments/causal-sets.json and ${CD}/fragments/noncommutative-geometry.json so both state the verified, probe-qualified truth with the correct citations. Keep JSON valid.
STEP 3: Rebuild registries: run with Bash, in this order: python3 ${ROOT}/workflows/consolidate.py && python3 ${ROOT}/workflows/consolidate.py --apply-merges
STEP 4: Write a short Czech note to ${ROOT}/verification/ds-contradiction.md (what was claimed, what the literature says, what was fixed; significance for hypothesis L3-1 — probe-dependence is exactly what it predicts).
Return the structured result.`,
  { label: 'fix:ds-contradiction', phase: 'Oprava dat', model: 'sonnet', schema: FIX_RESULT })

log(dsFix ? 'Rozpor d_s vyřešen: ' + (dsFix.bothCorrect ? 'oba údaje správně (závislost na sondě)' : 'jedna strana opravena') : '⚠️ fixer nedoběhl')

// ---------- Fáze 2: novelty check (6 paralelních sond) ----------
phase('Novelty check')
log('Spouštím 6 novelty sond proti literatuře (arXiv/INSPIRE)…')

const COMMON = ECON + `You are a NOVELTY CHECKER for a quantum-gravity research project. A brainstorm produced candidate hypotheses for yet-undiscovered connections; your job is to find out whether YOUR assigned hypothesis cluster is already known in the literature. Be adversarial: actively try to find prior art that kills it. A hypothesis survives only if its core claim is genuinely absent from the literature.

STEP 0: ToolSearch "select:WebSearch,WebFetch".
STEP 1: Read your hypothesis details: Grep ${ROOT}/knowledge-base/BRAINSTORM-01.md for your cluster ids and read the matching sections (NOT the whole file).
STEP 2: Run 6-10 targeted searches (arXiv listings, INSPIRE-HEP, Google Scholar via web search). Search both the obvious phrasings AND adjacent vocabularies the communities involved would use.
STEP 3: For each piece of prior art found, verify the arXiv ID resolves and note HOW it overlaps (same claim / special case / adjacent but different).
STEP 4: Write a Czech report to ${ROOT}/verification/novelty/<your-cluster-id>.md: hypotéza, co bylo nalezeno, verdikt, co zbývá nového, doporučení.
Return the structured result. Verdicts: "known" = core claim published; "partially-known" = pieces published, the specific synthesis/claim is not; "plausibly-novel" = nothing close found.

YOUR CLUSTER: `

const checks = await parallel([
  () => agent(COMMON + `ds-cluster (hypotheses L3-1 + L2-5 + L5-5): the claim that UV spectral dimension is NOT universally 2 but a predictable function of the UV propagator exponent z (a classification / master formula d_s(z,D) across approaches). Check especially: Carlip "Dimension and Dimensional Reduction in Quantum Gravity" (review), Eichhorn et al. on spectral dimension comparisons, Calcagni's multiscale/multifractional papers (he has published d_s formulas as functions of dispersion relations — HIGH overlap risk), Sotiriou-Visser-Weinfurtner. Context from our data fix: the CST direction question just got resolved as probe-dependent (see ${ROOT}/verification/ds-contradiction.md if it exists).`,
    { label: 'novelty:ds-cluster', phase: 'Novelty check', model: 'sonnet', schema: NOVELTY }),

  () => agent(COMMON + `a4-cluster (hypotheses L1-1 + L2-4 + L5-4): the claim that the Seeley-DeWitt coefficient a_4 is the common parent of (i) the NCG spectral action gravitational terms, (ii) Sakharov induced gravity, and (iii) the (a,c) trace anomaly — same coefficient, not analogy — with a falsifiable anomaly-matching test for the Standard Model algebra C+H+M3(C). Check: Chamseddine-Connes spectral action papers and their discussions of induced gravity; Visser "Sakharov's induced gravity: a modern perspective"; papers linking spectral action to anomalies (e.g. Andrianov-Lizzi, Kurkov-Lizzi-Vassilevich — HIGH overlap risk for the two-way links; the question is whether the THREE-way identification with the anomaly-matching test is published).`,
    { label: 'novelty:a4-cluster', phase: 'Novelty check', model: 'sonnet', schema: NOVELTY }),

  () => agent(COMMON + `lambda-cluster (hypotheses L1-2 + L3-2 + L2-2): the claim that three independent predictions of cosmological-constant fluctuations Lambda ~ +-1/sqrt(V) — Sorkin/causal sets (everpresent Lambda), Euclidean dynamical triangulations running of H^2, and Padmanabhan's CosMIn N=4pi — are the same number-fluctuation statistics conjugate to 4-volume, so their prefactors must be mutually predictable. Check: Sorkin's everpresent Lambda papers + Zwane-Afshordi-Sorkin phenomenology; Padmanabhan CosMIn papers; any published comparison/unification of these Lambda~1/sqrt(V) mechanisms (Barrow? Ng? unimodular gravity literature — volume-conjugate Lambda is a known theme there, HIGH overlap risk via unimodular route).`,
    { label: 'novelty:lambda-cluster', phase: 'Novelty check', model: 'sonnet', schema: NOVELTY }),

  () => agent(COMMON + `entropy-cluster (hypotheses L2-3 + L3-4 + L4-4): the claim that the Sorkin-Johnston entanglement entropy (SSEE) truncation in causal sets, the LQG area gap, and the crossed-product construction giving type-II von Neumann algebras are three faces of ONE regularization of the divergent entanglement trace, with the discrete scale playing the role of the observer/modular cutoff and the Immirzi parameter as a renormalization constant. Check: Sorkin-Yazdi-et al. SSEE papers; Chandrasekaran-Longo-Penington-Witten and follow-ups on crossed products; any paper connecting crossed-product type-II algebras to LQG area gap or to causal sets (this specific three-way bridge is the claim; two-way links may exist — e.g. discussions of area gap as entanglement cutoff by Bianchi, Perez).`,
    { label: 'novelty:entropy-cluster', phase: 'Novelty check', model: 'sonnet', schema: NOVELTY }),

  () => agent(COMMON + `cardy-lqg (hypothesis L1-3, FLAGGED HIGHEST RISK of being already known): the claim that the Cardy formula S = 2*pi*sqrt(c*L0/6) is hidden in LQG black-hole entropy via the horizon SU(2) Chern-Simons theory / boundary CFT, with the Immirzi parameter playing the role of central-charge normalization (analogous to c = 6*Q1*Q5 in the string D-brane counting). Check THOROUGHLY: Carlip's near-horizon conformal symmetry program (gr-qc/9812013 and successors); Ghosh-Pranzetti; Agullo-Barbero-Borja-Diaz-Polo-Villasenor; Frodden-Geiller-Noui-Perez "Black hole entropy from complex Ashtekar variables" and the gamma=i / conformal route; Han, Pranzetti-Sahlmann. If most of it is published, identify precisely which residual element (if any) is not.`,
    { label: 'novelty:cardy-lqg', phase: 'Novelty check', model: 'sonnet', schema: NOVELTY }),

  () => agent(COMMON + `preprint-checks (supporting verifications, several small items — report them all inside ONE structured result, using notes/priorArt to itemize): (a) L4-2: does the cited literature on the conflict "swampland no-global-symmetries vs asymptotic safety" exist and what does it claim (search: asymptotic safety global symmetries swampland, e.g. Eichhorn et al.)? (b) L4-5/L4-6: current status of BMV gravitationally-induced-entanglement debate — verify the 2025 rebuttal exchange we cite (arXiv:2511.07348, 2511.19242, Aziz & Howl Nature 2025) and whether our experimental-tests pillar's framing matches reality. (c) L5-3: has the Sorkin-Johnston state been constructed for Kerr or Schwarzschild-de Sitter (search SJ state black hole spacetimes)? (d) L2-1: how much of the NCG<->GFT "Dirac ensembles as special GFTs / Liouville universality" link is already published by Khalkhali and collaborators? Verdict/recommendation fields: summarize overall (verdict = partially-known is expected; recommendation = which items to update in our data).`,
    { label: 'novelty:preprint-checks', phase: 'Novelty check', model: 'sonnet', schema: NOVELTY }),
])

const checksDone = checks.filter(Boolean)
log('Novelty check hotov: ' + checksDone.length + '/6 sond. Zapisuji výsledky…')

// ---------- Fáze 3: zápis ----------
phase('Zápis')

const verdictsJson = JSON.stringify({ dsFix: dsFix, checks: checksDone }, null, 2)

const housekeeping = await agent(ECON + `You are the housekeeping agent for the quantum-gravity knowledge base at ${ROOT}. Today is ${DATE}. Work IN CZECH (prose) / ENGLISH (JSON data).

INPUT — results of the d_s data fix and 6 novelty checks (structured JSON):
${verdictsJson}

TASK 1: Write ${CD}/novelty-checks.json (ENGLISH): array of the check results verbatim (cluster, verdict, priorArt, whatRemainsNovel, recommendation), plus a "dsContradiction" entry summarizing the data fix. Pretty-printed, valid JSON.

TASK 2: Append to ${ROOT}/knowledge-base/BRAINSTORM-01.md a new section "## Novelty check (${DATE})" IN CZECH: a markdown table (klastr | verdikt | doporučení | klíčová prior art) + for each cluster 2-4 sentences: co literatura už zná, co zbývá nového, jak se mění priorita. Include the d_s resolution and its implication for the d_s cluster. Do not modify existing sections.

TASK 3: Update ${ROOT}/PROGRESS.md (Read first, preserve structure):
- Section "## Další kroky": re-rank the hypothesis priorities according to the verdicts (drop/reframe/pursue) — rewrite the "Prioritní hypotézy" subsection accordingly; mark the novelty-check subsection items as done with outcomes.
- Append a log entry under "### ${DATE}": novelty check 6 sond + oprava d_s rozporu (one compact bullet list with verdicts).
- Update "Aktuální stav" line: novelty check hotov, další krok = první výpočetní prověrky hypotéz s verdiktem pursue.

Return a Czech summary: for each cluster one line (verdikt + doporučení), plus which hypothesis now tops the priority list.`,
  { label: 'final:novelty-writeup', phase: 'Zápis', model: 'sonnet' })

return {
  dsFix: dsFix,
  checks: checksDone.map(c => ({ cluster: c.cluster, verdict: c.verdict, recommendation: c.recommendation })),
  checksDetail: checksDone,
  summary: housekeeping,
}