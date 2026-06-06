export const meta = {
  name: 'qg-deep-dive-01',
  description: 'Hluboké kolo Fáze 2: 4 testovací výpočty hypotéz (d_s klasifikace, a4 anomaly matching, Λ prefaktory, SSEE diamant) + 3 hypotézní dossiery + 2 spekulativní eseje + BRAINSTORM-02',
  phases: [
    { title: 'Výpočty', detail: '4 výpočetní agenti: python/numpy/sympy, výsledky + grafy do core-data/calculations/' },
    { title: 'Hluboký výzkum', detail: '3 dossiery k přeživším hypotézám (γ↔Cardy, SJ stav pro Kerr, BMV diskriminátor)', model: 'sonnet' },
    { title: 'Eseje', detail: '2 spekulativní eseje v češtině — fantazie odbrzděná, zřetelně značená', model: 'opus' },
    { title: 'Brainstorm 02', detail: 'syntéza nového kola hypotéz nad výpočty a verdikty', model: 'opus' },
    { title: 'Úklid', detail: 'index + progress tracker', model: 'sonnet' },
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
    keyNumbers: { type: 'string', description: 'the headline quantitative results, compact' },
    verdictForHypothesis: { type: 'string', description: 'what the calculation says about the hypothesis (Czech, 2-4 sentences)' },
    files: { type: 'array', items: { type: 'string' } },
  },
  required: ['name', 'status', 'keyNumbers', 'verdictForHypothesis', 'files'],
}

const DOSSIER_RESULT = {
  type: 'object',
  properties: {
    id: { type: 'string' },
    file: { type: 'string' },
    keyFindings: { type: 'array', items: { type: 'string' }, description: 'Czech, 3-5 items' },
    nextStep: { type: 'string', description: 'the single most concrete next action (Czech)' },
  },
  required: ['id', 'file', 'keyFindings', 'nextStep'],
}

const CALC_COMMON = `You are a computational physics agent for a quantum-gravity research project at ${ROOT}. Environment ready: python3 with numpy 2.4, matplotlib 3.10 (use Agg backend, savefig only), sympy 1.14, scipy 1.17. Work standalone: write a clean, commented python script, run it with Bash, iterate until correct.
RULES: (1) verify every physics convention against the literature (ToolSearch "select:WebFetch,WebSearch" — web IS allowed for convention checks and fetching published values); (2) exact rationals where possible (sympy/Fraction); (3) NEVER fudge a result to match expectation — a clean mismatch is a publishable-grade finding for us; (4) deliverables: <dir>/calc.py (runnable), <dir>/results.json (English, machine-readable), plot PNG(s) where meaningful, and a Czech writeup in ${KB}/vypocty/<writeup>.md: cíl, metoda, vstupy s citacemi, výsledky (tabulka), interpretace pro hypotézu, limity výpočtu. Cite every input number's source with arXiv ID.

YOUR TASK: `

// ---------- Fáze 1+2: výpočty a dossiery současně ----------
phase('Výpočty')
log('Spouštím 4 testovací výpočty a 3 dossiery paralelně…')

const batch = await parallel([
  // --- CALC 1: d_s classification (opus) ---
  () => agent(CALC_COMMON + `Build the d_s^UV(z, D, probe) CLASSIFICATION TABLE — the reframed hypothesis L3-1 (see ${KB}/BRAINSTORM-01.md and ${ROOT}/verification/novelty/ds-cluster.md). Known prior art to REPRODUCE first as validation: Hořava d_s = 1 + D/z (arXiv:0902.3657), Sotiriou-Visser-Weinfurtner (1105.6098). Then the NEW part: one unified return-probability formalism P(σ) = ∫ d^Dk e^{-σ F(k)} with d_s(σ) = -2 dlnP/dlnσ, applied NUMERICALLY to all of: (a) GR F=k²; (b) Hořava z=2,3; (c) Stelle quadratic gravity F = k²(1+k²/m²); (d) asymptotic safety: propagator with running anomalous dimension (UV fixed-point value η=-2 → verify published claim d_s^UV=2, cite Lauscher-Reuter hep-th/0508202 or Reuter-Saueressig 1110.5224 — fetch to confirm convention); (e) causal sets BOTH probes: d'Alembertian probe via Belenchia-Benincasa-Marciano-Modesto (1507.00330) asymptotics, and the random-walk probe direction per Eichhorn-Mizera (1311.2530) — at least qualitatively with the published asymptotics; (f) multifractional comparison value (Calcagni). Produce: master table (approach | probe | z_eff | d_s^UV | d_s^IR | source/validation) in results.json + Czech writeup, AND a single plot ds_flow.png of d_s(σ) flows overlaid. State explicitly which rows reproduce literature and which combinations/columns (probe as classification axis!) are our contribution. Dir: ${CD}/calculations/ds-classification/. Writeup: VYPOCET-01-ds-klasifikace.md.`,
    { label: 'calc:ds-classification', phase: 'Výpočty', model: 'opus', schema: CALC_RESULT }),

  // --- CALC 2: a4 anomaly matching (opus) ---
  () => agent(CALC_COMMON + `a₄ ANOMALY-MATCHING TEST for the NCG Standard Model algebra C⊕H⊕M₃(C) — hypothesis L1-1 (see ${ROOT}/verification/novelty/a4-cluster.md: the three-way identification is unpublished; two-way links are in Andrianov-Lizzi 1001.2036, Kurkov-Lizzi-Vassilevich 1106.3263). COMPUTE with sympy exact rationals: (i) trace-anomaly central charges (a,c) for free field content — standard coefficients per scalar / Weyl fermion / vector (verify against Duff hep-th/9308075 or Vassilevich hep-th/0306138); evaluate for SM WITHOUT right-handed neutrinos (N₀=4, N_W=45, N₁=12) and WITH ν_R as NCG demands (N_W=48). (ii) The Weyl-squared (C²) coefficient in the Chamseddine-Connes spectral action a₄ term — fetch the published coefficient (hep-th/9606001 and/or the review 1008.0985) and express it in the same normalization. (iii) TEST: does the spectral-action C² coefficient equal the c central charge of the fermionic content that induces it? Including: does adding ν_R move the match closer or further? (iv) Bonus if smooth: the E₄ (Euler) coefficient vs central charge a. Report match/mismatch as exact rationals + numerically. A clean mismatch with documented conventions is a real result — the hypothesis claims identity, so this is its direct falsification test. Dir: ${CD}/calculations/a4-anomaly-matching/. Writeup: VYPOCET-02-a4-matching.md.`,
    { label: 'calc:a4-matching', phase: 'Výpočty', model: 'opus', schema: CALC_RESULT }),

  // --- CALC 3: Lambda prefactors (sonnet) ---
  () => agent(CALC_COMMON + `Λ ~ 1/√V PREFACTOR COMPARISON — reframed lambda-cluster (see ${ROOT}/verification/novelty/lambda-cluster.md: the cross-comparison was never published). FETCH the actual numbers: (a) everpresent Λ fluctuation amplitude/prefactor from Ahmed-Dodelson-Greene-Sorkin (astro-ph/0209274) and Aspects I/II (2304.03819, 2307.13743) — how big is δΛ in Planck units vs 1/√V; (b) EDT: the coefficient of the H² term in Λ(H) from Dai-Laiho et al. (2408.08963) — extract their fitted value; (c) CosMIn: Λ L_P² ≈ 3.4e-122 from N=4π (1302.3226) — express as prefactor κ in Λ = κ/√V given their V convention. CONVERT all three to one convention: Λ·l_P² = κ/√(V/l_P⁴) with V = past 4-volume ≈ c_V/H⁴ (state and justify c_V per source). COMPARE: table of κ values + ratios. If conventions make a comparison genuinely ambiguous, document the ambiguity precisely (which choice would make them agree?) — that itself is the result. Also state what observational H(z) data would distinguish the three (stochastic vs deterministic Λ(H)). Dir: ${CD}/calculations/lambda-prefactors/. Writeup: VYPOCET-03-lambda-prefaktory.md.`,
    { label: 'calc:lambda-prefactors', phase: 'Výpočty', model: 'sonnet', schema: CALC_RESULT }),

  // --- CALC 4: SSEE sprinkled diamond (opus) ---
  () => agent(CALC_COMMON + `SSEE ON A SPRINKLED 2D CAUSAL DIAMOND — first test of the entropy-cluster hypothesis (see ${ROOT}/verification/novelty/entropy-cluster.md, recommended first step). Follow the Sorkin-Johnston prescription (Sorkin-Yazdi 1611.10281; Surya et al. 2008.07697 — fetch to confirm the exact entropy formula and the massless 2D Pauli-Jordan construction: iΔ from retarded minus advanced, retarded Green function of 2D massless scalar on a causal set = (1/2)·causal matrix). PLAN: (1) Poisson-sprinkle N≈500–1500 points into a 2D diamond; (2) build iΔ; (3) restrict to a subdiamond; (4) solve the generalized eigenproblem of the SJ entropy formula S = Σ μ ln|μ| over solutions of iΔ v = μ W v (W = Pauli-Jordan restricted — verify exact prescription from the papers!); (5) reproduce the known result: S follows the 2D log-law S ≈ (1/3)ln(ℓ/ℓ_UV)? only AFTER truncating the eigenvalue spectrum at the 'knee'; (6) THE NEW MEASUREMENT: how does the knee position scale with sprinkling density ρ — fit knee ~ ρ^p and compare p with the hypothesis prediction (modular/discreteness cutoff; in 2D expect ε ~ ρ^(-1/2)); (7) plots: eigenvalue spectrum with knee, S vs truncation rank, knee vs ρ fit. Several seeds for error bars. Keep N modest (runtime minutes, not hours). Dir: ${CD}/calculations/ssee-diamond/. Writeup: VYPOCET-04-ssee-diamant.md.`,
    { label: 'calc:ssee-diamond', phase: 'Výpočty', model: 'opus', schema: CALC_RESULT }),

  // --- DOSSIER 1: gamma-Cardy (sonnet) ---
  () => agent(`You are a research-dossier agent (ECONOMY MODE: targeted reads/searches only). Project: quantum-gravity knowledge base at ${ROOT}. Novelty check verdict (${ROOT}/verification/novelty/cardy-lqg.md): core is KNOWN (Carlip 1410.5763: c=6k; Ghosh-Pranzetti; Frodden et al. γ=±i); the unpublished residue = (a) explicit γ ↔ c=6Q₁Q₅ string-analogy, (b) the prediction that matching the LQG log-correction (-1/2 U(1) vs -3/2 SU(2)) to Cardy's universal -3/2 ln c term uniquely fixes real γ. ToolSearch "select:WebSearch,WebFetch". Build the deep dossier ${KB}/hypotezy/H01-gamma-cardy.md IN CZECH: (1) přehled VŠECH publikovaných log-korekcí entropie ČD napříč přístupy (LQG U(1)/SU(2), string/Cardy, AS, semiklasika — Sen 1205.0971 je klíčová křížová reference: log korekce jsou IR, přístupově univerzální!); (2) přesná formulace zbývajícího tvrzení + co přesně spočítat (krok za krokem); (3) rizika (Senova univerzalita může tvrzení zabít — pokud jsou log korekce čistě IR, nemohou fixovat γ; toto poctivě rozeber); (4) verdikt: stojí výpočet za to? Return structured result.`,
    { label: 'dossier:gamma-cardy', phase: 'Hluboký výzkum', model: 'sonnet', schema: DOSSIER_RESULT }),

  // --- DOSSIER 2: SJ state for Kerr (sonnet) ---
  () => agent(`You are a research-dossier agent (ECONOMY MODE). Project at ${ROOT}. Novelty verdict (${ROOT}/verification/novelty/preprint-checks.md, item c): SJ state for Kerr/SdS = PLAUSIBLY-NOVEL territory. ToolSearch "select:WebSearch,WebFetch". Build ${KB}/hypotezy/H02-sj-kerr.md IN CZECH: (1) co přesně SJ konstrukce potřebuje (Pauli-Jordan funkce, bounded region, spektrální rozklad) a co je pro Kerr k dispozici (Teukolsky módy, superradiance — jak rozbíjí pozitivní frekvence); (2) proč to Kay-Wald a Fewster-Verch no-go věty přímo nezakazují (SJ ≠ Hadamard obecně — to je pro nás feature: unikátní stav i tam, kde Hadamard selhává); (3) tři konkrétní strategie útoku, od nejlevnější: (i) numerický sprinkling do Kerrova konformního diagramu (BL souřadnice, omezená oblast vně horizontu), (ii) 2D analog (rotující BTZ? Kerr equatorial slice?), (iii) plná modová konstrukce; (4) co by výsledek znamenal (stav pro QFT na rotující ČD = vstup pro superradianci, entropii, Hawkingovo záření Kerr). Return structured result.`,
    { label: 'dossier:sj-kerr', phase: 'Hluboký výzkum', model: 'sonnet', schema: DOSSIER_RESULT }),

  // --- DOSSIER 3: BMV discriminator (sonnet) ---
  () => agent(`You are a research-dossier agent (ECONOMY MODE). Project at ${ROOT}. Novelty verdict (${ROOT}/verification/novelty/preprint-checks.md, item b): the framing "BMV/GIE as discriminator BETWEEN quantum-gravity approaches (not just quantum-vs-classical)" is plausibly novel; the 2025 Aziz-Howl/Marletto-Oppenheim-Vedral exchange is verified live. ToolSearch "select:WebSearch,WebFetch". Build ${KB}/hypotezy/H03-bmv-diskriminator.md IN CZECH: (1) stručná mapa aktuální debaty (Aziz-Howl Nature 2025; 2511.07348; 2511.19242; 2511.20717) — kdo co tvrdí; (2) JÁDRO: tabulka predikcí entanglement fáze/visibility pro BMV setup podle přístupu — perturbativní graviton EFT (standard), AS s běžícím G(k) a η (modifikuje potenciál na krátkých škálách?), emergentní/entropická gravitace (Verlinde — existuje mediátor?), stochastická/klasická gravitace (Oppenheim), minimal-length/GUP modifikace — pro každý: kvalitativní předpověď a škála, kde se odchylka objeví; (3) jaké parametry experimentu (hmotnost, separace, čas) by odchylky rozlišily — srovnej s plánovanými experimenty (masy ~1e-14 kg, separace ~100 µm); (4) verdikt: je diskriminace realistická, nebo jsou rozdíly za hranicí měřitelnosti? Return structured result.`,
    { label: 'dossier:bmv-discriminator', phase: 'Hluboký výzkum', model: 'sonnet', schema: DOSSIER_RESULT }),
])

const calcs = batch.slice(0, 4).filter(Boolean)
const dossiers = batch.slice(4).filter(Boolean)
log('Výpočty: ' + calcs.length + '/4, dossiery: ' + dossiers.length + '/3. Spouštím eseje…')

const calcSummary = JSON.stringify(calcs.map(c => ({ name: c.name, status: c.status, keyNumbers: c.keyNumbers, verdict: c.verdictForHypothesis })), null, 2)
const dossierSummary = JSON.stringify(dossiers, null, 2)

// ---------- Fáze 3: eseje — fantazie odbrzděná ----------
phase('Eseje')

const ESSAY_COMMON = `You are an essayist-physicist writing for a quantum-gravity research project at ${ROOT}. The user EXPLICITLY asked to "release the brakes on imagination" in prose. Write IN CZECH, beautiful and bold — vivid metaphors, daring extrapolations, genuine intellectual excitement — while staying anchored: every speculative leap must start from a real result in our knowledge base and be clearly marked (the document carries a header "⚠️ SPEKULATIVNÍ ESEJ — fantazie odbrzděná, fakta citována, extrapolace značeny"). Sections may interleave "Co víme" (cited, sober) and "Co kdyby" (unleashed). End with "Co by muselo být pravda" — the falsifiable core of the vision. 600-900 lines is fine if the material carries it. Fresh inputs you may draw on — calculation results just computed:
${calcSummary}
And hypothesis dossiers:
${dossierSummary}

YOUR ESSAY: `

const essays = await parallel([
  () => agent(ESSAY_COMMON + `${KB}/eseje/ESEJ-01-dimenze-jako-otazka.md — "Dimenze jako otázka, kterou prostoročasu položíš". Core thread: probe-dependence není chyba, ale ontologie — táž kauzální množina odpoví random-walkerovi "dimenze roste" a d'Alembertiánu "dimenze klesá k 2" (viz verification/ds-contradiction.md a VYPOCET-01); SSEE entropie existuje jen po volbě cutoffu (VYPOCET-04); crossed-product algebry potřebují pozorovatele, aby entropie vůbec byla definována. Co kdyby "vlastnosti prostoročasu" byly vždy relační — odpovědi na otázky, ne atributy? Dotáhni do důsledků: co je pak "dimenze vesmíru", co znamená UV-kompletnost, jak by vypadala teorie, kde je sonda součástí definice geometrie (quantum reference frames!). Read additionally: ${KB}/SYNTEZA.md (bílá místa), relevant pillar files selectively.`,
    { label: 'esej:dimenze', phase: 'Eseje', model: 'opus' }),
  () => agent(ESSAY_COMMON + `${KB}/eseje/ESEJ-02-vesmir-ktery-se-pocita.md — "Vesmír, který se počítá: temná energie jako šum diskrétnosti". Core thread: tři nezávislé komunity předpověděly Λ ~ ±1/√V (Sorkin causal sets, EDT mřížka, Padmanabhanův CosMIn) — a naše VYPOCET-03 právě porovnal jejich prefaktory. Co kdyby temná energie byla doslova Poissonův výstřelový šum atomů prostoročasu — vesmír "počítá" své elementy a Λ je odmocninová chyba toho sčítání? Dotáhni: everpresent Λ které kolísá (testovatelné v H(z) datech!), co to dělá s kosmologickou konstantou jako "problémem" (rozpouští ho — 10⁻¹²² není jemné ladění ale √N statistika), vztah k unimodulární gravitaci a swampland zákazům, divoká ale značená extrapolace: jaké další "konstanty" by mohly být šumem počítání? Read additionally: ${KB}/approaches/05-causal-sets.md, ${KB}/phenomenology/18-quantum-cosmology.md selectively.`,
    { label: 'esej:vesmir-pocita', phase: 'Eseje', model: 'opus' }),
])

log('Eseje hotové: ' + essays.filter(Boolean).length + '/2. Brainstorm 02…')

// ---------- Fáze 4: BRAINSTORM-02 ----------
phase('Brainstorm 02')

const brainstorm2 = await agent(`You are the second-round brainstorm synthesizer for the quantum-gravity project at ${ROOT}. Build on EVERYTHING new since BRAINSTORM-01: novelty verdicts (${CD}/novelty-checks.json if present, else ${ROOT}/verification/novelty/*.md), the d_s contradiction resolution (probe-dependence confirmed), four fresh calculations (summaries below + writeups in ${KB}/vypocty/), three dossiers (${KB}/hypotezy/), and the two essays (${KB}/eseje/ — mine them for ideas worth formalizing).

Calculation results:
${calcSummary}
Dossiers:
${dossierSummary}

Write ${KB}/BRAINSTORM-02.md IN CZECH:
# Brainstorming 02: Druhé kolo (${DATE})
## Co se změnilo od BRAINSTORM-01   ← verdikty novelty checku + výsledky výpočtů v jedné tabulce
## Vyhodnocení výpočtů              ← co každý výpočet UDĚLAL s hypotézou (potvrdil/zranil/přerámoval); buď nemilosrdně poctivý
## Hypotézy druhé generace          ← 5-10 nových/zostřených hypotéz; každá: tvrzení, opora (vč. čísel z výpočtů!), proč nová (cituj novelty verdikt), první test, confidence. Zahrň formalizovatelné nápady z esejí (značené původem "esej")
## Výpočetní fronta                 ← seřazená fronta dalších výpočtů s odhadem náročnosti (hodiny/dny/týdny)
## Strategický pohled               ← kde má projekt největší šanci na skutečný objev; co opustit

Return a Czech summary: top 5 second-generation hypotheses, one line each + the single most promising next calculation.`,
  { label: 'brainstorm-02:synth', phase: 'Brainstorm 02', model: 'opus' })

// ---------- Fáze 5: úklid ----------
phase('Úklid')

const housekeeping = await agent(`You are the housekeeping agent for ${ROOT}. Today ${DATE}. Work IN CZECH. ECONOMY MODE.
New artifacts this round: ${KB}/vypocty/ (4 writeups), ${CD}/calculations/ (4 dirs with calc.py/results.json/plots), ${KB}/hypotezy/ (3 dossiers), ${KB}/eseje/ (2 essays), ${KB}/BRAINSTORM-02.md.
TASK 1: update ${KB}/00-INDEX.md — add the new sections (Výpočty, Hypotézní dossiery, Eseje, BRAINSTORM-02) with one-line hooks; keep existing entries.
TASK 2: update ${ROOT}/PROGRESS.md (Read first; it was recently updated by the novelty-check workflow — preserve all of that): "Aktuální stav" → deep-dive kolo 1 hotovo; append log entry for ${DATE} (4 výpočty + 3 dossiery + 2 eseje + BRAINSTORM-02, with one-line outcome per calculation from: ${calcSummary}); add/extend "Další kroky" from BRAINSTORM-02's "Výpočetní fronta" (read it).
Return 3-line Czech confirmation.`,
  { label: 'final:index+progress', phase: 'Úklid', model: 'sonnet' })

return {
  calcs: calcs.map(c => ({ name: c.name, status: c.status, keyNumbers: c.keyNumbers })),
  calcVerdicts: calcs.map(c => c.verdictForHypothesis),
  dossiers: dossiers.map(d => ({ id: d.id, nextStep: d.nextStep })),
  essaysWritten: essays.filter(Boolean).length,
  brainstorm2Summary: brainstorm2,
  housekeeping: housekeeping,
}