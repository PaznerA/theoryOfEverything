export const meta = {
  name: 'qg-deep-dive-02',
  description: 'Rozhodující kolo: SJ stav pro rotující BTZ (nové území), 4D SSEE test N^(3/4), AS×BMV fáze, rozhodující čtení γ–Cardy (Sen IR-univerzalita), registr findings.json',
  phases: [
    { title: 'Rozhodující kolo', detail: '3 výpočty + 1 rozhodující čtení + registr nálezů, paralelně' },
    { title: 'Úklid', detail: 'BRAINSTORM-02 dodatek, PROGRESS, INDEX', model: 'sonnet' },
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

const READ_RESULT = {
  type: 'object',
  properties: {
    verdict: { type: 'string', description: 'program-alive | program-dead | already-published' },
    constantTermComparisonExists: { type: 'boolean' },
    senKillsGammaFixing: { type: 'string', description: 'yes | no | partially — with one-line reason' },
    keyFindings: { type: 'array', items: { type: 'string' }, description: 'Czech' },
    nextStep: { type: 'string', description: 'Czech' },
  },
  required: ['verdict', 'constantTermComparisonExists', 'senKillsGammaFixing', 'keyFindings', 'nextStep'],
}

const FINDINGS_RESULT = {
  type: 'object',
  properties: {
    findingsCount: { type: 'number' },
    note: { type: 'string', description: 'Czech, 1-2 sentences' },
  },
  required: ['findingsCount', 'note'],
}

const CALC_COMMON = `You are a computational physics agent at ${ROOT}. Environment: python3 + numpy 2.4, matplotlib 3.10 (Agg, savefig), sympy 1.14, scipy 1.17. Write clean commented python, run via Bash, iterate until correct. Verify conventions against literature (ToolSearch "select:WebFetch,WebSearch" — web allowed). NEVER fudge results — clean mismatches are first-class findings. Deliverables: <dir>/calc.py, <dir>/results.json (EN), PNG plots, Czech writeup in ${KB}/vypocty/<writeup>.md (cíl, metoda, vstupy s citacemi, výsledky, interpretace, limity).

YOUR TASK: `

phase('Rozhodující kolo')
log('Spouštím 3 výpočty + rozhodující čtení + registr nálezů…')

const batch = await parallel([
  // --- decisive read: gamma-Cardy ---
  () => agent(`You are a decisive-reading agent (ECONOMY MODE). The γ–Cardy program (dossier ${KB}/hypotezy/H01-gamma-cardy.md) hinges on two questions. ToolSearch "select:WebFetch,WebSearch".
Q1: Has the constant-term/log-correction comparison already been published? READ CAREFULLY: Engle-Noui-Perez arXiv:1006.0634 (sections on the log expansion of SU(2) CS entropy — extract the exact form of the log + constant terms and their γ dependence) AND Carlip arXiv:1410.5763 sections 5-6 (does Carlip himself compare the constant/log term against the real-γ counting?).
Q2: Does Sen's IR-universality argument (arXiv:1205.0971 — log corrections are IR/one-loop, approach-independent) STRUCTURALLY forbid fixing the UV parameter γ from CFT log corrections? Read Sen's argument; consider the counter-position: γ enters the LQG microcanonical log term coefficient, but if Sen is right the coefficient is fixed by IR physics for ALL theories, so any γ-dependence must cancel — check what published LQG log coefficients actually depend on (γ? level k? ensemble choice?).
APPEND your findings as a dated section "## Rozhodující čtení (${DATE})" to ${KB}/hypotezy/H01-gamma-cardy.md (Czech). Be terminal: if the program is dead or already published, say so plainly — killing a hypothesis cleanly is success, not failure. Return structured result.`,
    { label: 'decisive:gamma-cardy', phase: 'Rozhodující kolo', model: 'sonnet', schema: READ_RESULT }),

  // --- CALC 5: SJ state on rotating BTZ / 2D ergoregion ---
  () => agent(CALC_COMMON + `FIRST NUMERICAL SJ STATE IN A ROTATING SPACETIME REGION — flagship novel computation (dossier ${KB}/hypotezy/H02-sj-kerr.md strategy II; novelty check: Kerr/SdS SJ = unexplored territory). Exploit 2D conformal triviality: for a MASSLESS scalar in ANY 2D spacetime, the causal-set retarded Green function is G_ret = (1/2)·C (causal matrix) — purely causal-structure data (verify against Johnston arXiv:0909.0944 / X. Nomaan-Surya conventions). PLAN: (1) take a 2D section of rotating BTZ (t-φ at fixed r near horizon, or better: the r-t plane with frame-dragging encoded via the proper light-cone tilting of the BTZ metric with J≠0 — choose the cleanest well-defined 2D Lorentzian region containing part of the ergoregion AND document the choice honestly); (2) sprinkle via proper volume √|g|, determine causal relations by integrating null geodesics or by the metric's light cones; (3) build iΔ = i(C−Cᵀ)/... per convention, eigendecompose the SJ problem in the standard way (Pauli-Jordan spectral decomposition: SJ state = positive part of iΔ); (4) MEASUREMENTS: does the SJ construction go through cleanly in a region with ergoregion/cone-tilting (it should — it never needs a timelike Killing vector — that is the point); compare the SJ mode structure / two-point function inside vs outside the ergoregion; look for signatures associated with superradiance (modes with reversed energy density sign?); compare against the same-size static (J=0) BTZ region as control. (5) plots: sprinkling + cones, eigenvalue spectra J=0 vs J≠0, correlation profiles. SCOPE HONESTY: this is a first exploratory probe — frame it as "SJ state exists and is computable where stationary constructions fail", not as a Kerr result. Dir: ${CD}/calculations/sj-rotating-btz/. Writeup: VYPOCET-05-sj-rotujici-btz.md.`,
    { label: 'calc:sj-rotating-btz', phase: 'Rozhodující kolo', model: 'opus', schema: CALC_RESULT }),

  // --- CALC 6: 4D SSEE scaling ---
  () => agent(CALC_COMMON + `4D SSEE CUTOFF SCALING TEST — decisive follow-up of VYPOCET-04 (read ${KB}/vypocty/VYPOCET-04-ssee-diamant.md and reuse its working code from ${CD}/calculations/ssee-diamond/calc.py as the starting point). In 2D we measured entropy-cutoff rank ~ N^(0.519±0.007) ⇒ general-d prediction rank ~ N^((d−1)/d) (area law). TEST d=4: Johnston's massless retarded Green function on 4D causal sets uses the LINK matrix: G_ret ∝ L with a known constant (fetch Johnston arXiv:0909.0944 / 1004.3220 for the exact prefactor 1/(2π√6) convention). Sprinkle N up to ~3000-5000 into a 4D causal diamond (watch runtime — link matrix computation is the bottleneck, vectorize with numpy boolean matmul; transitive reduction via C²: link iff causal and no intermediate), build iΔ, restrict to subdiamond, repeat the VYPOCET-04 protocol: spectrum knee, entropy-cutoff rank vs N fit. PREDICTION UNDER TEST: p = 3/4 (vs 2D's 1/2). Secondary: does double-truncated SSEE follow an area law S ∝ A/ℓ²? Multiple seeds, error bars, log-log fit plot. If 4D is computationally infeasible at meaningful N, do d=3 (p=2/3 prediction) — Johnston gives 3D conventions too — and say so. Dir: ${CD}/calculations/ssee-4d/. Writeup: VYPOCET-06-ssee-4d.md.`,
    { label: 'calc:ssee-4d', phase: 'Rozhodující kolo', model: 'opus', schema: CALC_RESULT }),

  // --- CALC 7: AS-corrected BMV phase ---
  () => agent(CALC_COMMON + `ASYMPTOTIC-SAFETY CORRECTION TO THE BMV ENTANGLEMENT PHASE — quantify the discriminator from dossier ${KB}/hypotezy/H03-bmv-diskriminator.md. (1) Fetch the Bonanno-Reuter RG-improved Newtonian potential (hep-th/0002196; also Donoghue's EFT quantum correction G(r) for comparison — the known -167/30π Gℏ/r³c³ term etc., verify exact coefficient from 9310024/0311082). (2) BMV phase: φ = G m² t / (ħ d) for two masses in superposition separation d; compute the AS and EFT corrections δφ/φ for realistic parameter sets: m = 1e-14 kg, d = 100-450 µm, t = 1-10 s, plus an aggressive future set (m = 1e-12 kg, d = 10 µm). (3) Also tabulate the BINARY discriminators (no mediator → no entanglement: classical/stochastic Oppenheim; emergent gravity ambiguity) vs CONTINUOUS ones (AS/EFT/GUP phase corrections) — for each, the required measurement precision. (4) Honest conclusion: which discriminations are realistic this century? Plot δφ/φ vs d for the models. Dir: ${CD}/calculations/bmv-as-phase/. Writeup: VYPOCET-07-bmv-as-faze.md.`,
    { label: 'calc:bmv-as-phase', phase: 'Rozhodující kolo', model: 'sonnet', schema: CALC_RESULT }),

  // --- findings registry ---
  () => agent(`You are a data agent (ECONOMY MODE) at ${ROOT}. Create the registry of PROJECT-ORIGINAL findings: ${CD}/findings.json (ENGLISH, machine-readable). Sources to read: ${KB}/vypocty/VYPOCET-01..04 writeups, ${CD}/calculations/*/results.json, ${ROOT}/verification/ds-contradiction.md, ${CD}/novelty-checks.json. Schema: array of { "id": "F-001"..., "statement": precise English claim, "status": "confirmed|refuted|supported|mixed", "evidence": [file paths], "date": "...", "relatedHypotheses": ["L3-1",...], "implications": "...", "noveltyStatus": "what novelty-check said about whether this was known" }. Include at least: the d_s(z,D,probe) classification table validation; the a4 fermion-sector EXACT -18/11 match; the a4 full-SM falsification; the Λ prefactor ~140x mismatch (strong unification refuted); the SSEE ρ^(-1/2) cutoff scaling (ρ^(-1/4) excluded 39σ); the CST probe-dependence resolution. Conservative wording — these are numerical/literature results of THIS project, distinguish "verified reproduction" from "new result". Return count + note.`,
    { label: 'data:findings-registry', phase: 'Rozhodující kolo', model: 'sonnet', schema: FINDINGS_RESULT }),
])

const decisive = batch[0]
const calcs = [batch[1], batch[2], batch[3]].filter(Boolean)
const findings = batch[4]
log('Rozhodující kolo: čtení ' + (decisive ? decisive.verdict : 'N/A') + ', výpočty ' + calcs.length + '/3, findings ' + (findings ? findings.findingsCount : 0) + '. Úklid…')

// ---------- Úklid ----------
phase('Úklid')

const roundSummary = JSON.stringify({ decisive: decisive, calcs: calcs.map(c => ({ name: c.name, status: c.status, keyNumbers: c.keyNumbers, verdict: c.verdictForHypothesis })), findings: findings }, null, 2)

const housekeeping = await agent(`You are the housekeeping agent for ${ROOT}. Today ${DATE}. Work IN CZECH. ECONOMY MODE. Results of the decisive round (JSON):
${roundSummary}

TASK 1: Append to ${KB}/BRAINSTORM-02.md a section "## Výsledky rozhodujícího kola (${DATE})": table (položka | výsledek | dopad na hypotézu) covering the γ–Cardy decisive read, VYPOCET-05/06/07, findings.json. For each second-generation hypothesis touched (H2g-3 SSEE/crossed-product, H2g-6 SJ rotating, H2g-7 Sen blocker, BMV discriminator), state plainly: posíleno / oslabeno / zabito / beze změny.
TASK 2: Update ${ROOT}/PROGRESS.md (Read first, preserve): log entry for ${DATE} (rozhodující kolo — one line per item), update "Další kroky" (remove done items, add follow-ups implied by the results), update "Aktuální stav".
TASK 3: Update ${KB}/00-INDEX.md: add VYPOCET-05/06/07, findings.json, new calculation dirs.
Return a Czech summary (5 lines max): which hypotheses survived the decisive round and the single best next move.`,
  { label: 'final:round-writeup', phase: 'Úklid', model: 'sonnet' })

return {
  decisiveRead: decisive,
  calcs: calcs.map(c => ({ name: c.name, status: c.status, keyNumbers: c.keyNumbers })),
  calcVerdicts: calcs.map(c => c.verdictForHypothesis),
  findingsCount: findings ? findings.findingsCount : 0,
  housekeeping: housekeeping,
}