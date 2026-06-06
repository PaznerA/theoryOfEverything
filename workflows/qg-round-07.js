export const meta = {
  name: 'qg-round-07',
  description: 'Kolo 7: BRAINSTORM-04 (čtvrtá generace), SYNTEZA-02 (mapa po šesti kolech), VYPOCET-15 far-zone scan E vs S, VYPOCET-16 vN-typ na 4D slabu (dokončení entropy-cluster programu)',
  phases: [
    { title: 'Jádro kola', detail: 'BRAINSTORM-04 + SYNTEZA-02 + 2 výpočty paralelně' },
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

const CALC_COMMON = `You are a computational physics agent at ${ROOT}. Environment: python3 + numpy/scipy/sympy/matplotlib (Agg). Verify conventions (ToolSearch "select:WebFetch,WebSearch"). NEVER fudge results. Deliverables: <dir>/calc.py, <dir>/results.json (EN), plots, Czech writeup in ${KB}/vypocty/.

YOUR TASK: `

const STATE = `PROJECT STATE AFTER 6 ROUNDS (17 findings in ${CD}/findings.json): (1) −18/11 fermionic a₄ identity EXACT + index-theorem-protected (Atiyah-Singer/Rohlin lock); graviton cannot rescue it at any multiplicity → spectral action = fermion-induced gravity [VYPOCET-02,11; draft-02 scientifically closed]. (2) SJ states in rotating spacetimes: exist through ergoregions (BTZ+Kerr, machine precision), rotation lives in eigenvectors (~45° subspace rotation, <2% spectrum change), superradiant wedge weight W_sr ~ Ω(r)^B controlled by LOCAL frame-dragging (ΔAIC 230-4200 vs ergosphere-threshold model), opposite-sign asymmetry mechanism verified ~99% (cone aperture vs squeezed-null-direction correlations) [VYPOCET-05,08,10,14; draft-01 v0.2]. (3) SSEE/entropy: 2D clean cutoff ρ^(−1/2) (39σ); 4D volume law was DIAMOND-CORNER artifact — slab half-space gives clean AREA law S~L^2.00, non-Hadamard anomaly localized at corners [VYPOCET-04,06,09,13]; first numerical evidence of III₁→II crossed-product transition (trace collapse 80×, modular spectrum flat-dense→integrable with IR edge; 2/3 proxies, 2D) [VYPOCET-12]. (4) Killed cleanly: γ–Cardy program (Sen IR-universality), naive Λ~1/√V unification (~140× prefactor mismatch), continuous BMV discriminators (24-72 orders below reach). (5) d_s(z,D,probe) classification: one validated engine, probe as third axis [VYPOCET-01; draft-03]. (6) Emerging THROUGH-LINE: spacetime properties are answers to questions (probe, observer, region geometry, state regularity), not attributes.`

phase('Jádro kola')
log('Spouštím BRAINSTORM-04, SYNTEZA-02 a dva výpočty…')

const batch = await parallel([
  // --- BRAINSTORM-04 ---
  () => agent(`You are the fourth-round brainstorm synthesizer at ${ROOT}. ${STATE}
Read selectively: ${KB}/BRAINSTORM-03.md, ${CD}/findings.json, ${KB}/vypocty/VYPOCET-11..14 writeups (skim), ${KB}/hypotezy/H04.
Write ${KB}/BRAINSTORM-04.md IN CZECH:
# Brainstorming 04 (${DATE})
## Bilance po šesti kolech            ← tabule: všechny programy/hypotézy se statusem a evidencí (čísla!)
## Jednotící nit                       ← rozpracuj through-line "vlastnosti = odpovědi na otázky": je to jedna hypotéza? Jak by se formalizovala (relační/QRF jazyk, modulární teorie)? Co by ji vyvrátilo?
## Hypotézy čtvrté generace            ← 5-8; očekávám mj.: (a) korelace rohové non-Hadamardovosti s modulární teorií (roh = místo, kde selhává boost-flow); (b) Ω(r)^B zákon — co určuje exponent B (4.2 Kerr vs 1.7 BTZ — dimenze? asymptotika? spin počítání?); (c) fermionová indukce → co předpovídá pro kosmologickou konstantu (f₀ moment a Λ); (d) III→II přechod na 4D slabu (běží jako VYPOCET-16); každá: tvrzení, opora, test, confidence
## Výpočetní fronta v3                 ← seřazená s odhady
## Publikační stav                     ← draft-01 v0.2 / draft-02 closed / draft-03 v0.1: co zbývá k lidské revizi; doporuč draft-04 kandidáty (vN-typ III→II evidence? slab/corner geometrie?)
Return Czech summary: top 3 hypotézy + nejlepší další tah.`,
    { label: 'brainstorm-04:synth', phase: 'Jádro kola', model: 'opus' }),

  // --- SYNTEZA-02 ---
  () => agent(`You are the synthesis agent at ${ROOT}. The original ${KB}/SYNTEZA.md predates ALL our calculations. ${STATE}
Write ${KB}/SYNTEZA-02.md IN CZECH — "Mapa po šesti kolech" (do NOT modify SYNTEZA.md — this is the sequel):
# Syntéza 02: Mapa kvantové gravitace po vlastním výzkumu (${DATE})
## Co se změnilo od Syntézy 01        ← which white spaces from SYNTEZA.md we actually entered, and what we found there
## Mapa vztahů — aktualizace          ← Mermaid diagram: the original pillar map ENRICHED with our own findings as new edges (e.g. causal-sets↔von-neumann-algebras edge now has DATA: III→II proxies; NCG↔emergent-gravity edge: −18/11 index lock; mark our contributions distinctly, e.g. thick edges)
## Vlastní příspěvky na mapě          ← per finding: which inter-pillar connection it establishes/strengthens/kills (cite findings.json ids F-001..F-017)
## Zbývající bílá místa               ← what remains barely explored AFTER our work; re-rank the hunting grounds (read ${CD}/connections.json + ${CD}/_digest.md for the current barely-list)
## Strategický výhled                 ← where the project should go in the next 10 rounds: compute, read, or write?
Dense, honest. Cite paths. Return 5-line Czech summary.`,
    { label: 'synteza-02', phase: 'Jádro kola', model: 'opus' }),

  // --- VYPOCET-15: far-zone E vs S ---
  () => agent(CALC_COMMON + `VYPOCET-15 — close the residual ambiguity of VYPOCET-14 (read ${KB}/vypocty/VYPOCET-14-threshold-scan.md; reuse ${CD}/calculations/sj-threshold-scan/calc.py): for Kerr a=0.6 the linear correlation slightly favored Model E (1/(r−r_erg)) over Model S (Ω(r)^B) because the two are correlated near the ergosphere. Run the FAR-ZONE scan r = 5M..20M (≥10 radii, ≥4 seeds, N≈1600) where the models diverge cleanly: Model S predicts W_sr ~ Ω(r)^B ~ r^(−3B) falling as a power law; Model E predicts much faster decay tied to (r−r_erg). Also measure A_W in the far zone (toy model predicts A_W ~ shear ~ Ω(r), so |A_W| ~ r^(−3)). Fit both models on far-zone data only + jointly with VYPOCET-14 near-zone data; report AIC/BIC and the cleanest single-plot evidence (log-log W_sr vs Ω). If conclusive, append a dated note to ${KB}/vypocty/VYPOCET-14-threshold-scan.md (korekce/doplněk section) and to papers/draft-01-sj-rotating-spacetimes/TODO.md. Deliverables dir: ${CD}/calculations/sj-far-zone/; writeup VYPOCET-15-far-zone.md.`,
    { label: 'calc:sj-far-zone', phase: 'Jádro kola', model: 'sonnet', schema: CALC_RESULT }),

  // --- VYPOCET-16: vN-type on 4D slab ---
  () => agent(CALC_COMMON + `VYPOCET-16 — COMPLETE the entropy-cluster program: re-run the von Neumann TYPE proxies (VYPOCET-12 protocol, read ${KB}/vypocty/VYPOCET-12-vn-typ-truncace.md + reuse ${CD}/calculations/sj-vn-type/calc.py) on the 4D SLAB half-space geometry that VYPOCET-13 just validated as clean (read VYPOCET-13 writeup + reuse sprinkling/cut code from ${CD}/calculations/ssee-slab-4d/calc.py). Protocol: 4D slab, half-space cut x₁>0 (interior cut away from box walls — the cleaner variant per VYPOCET-13), link-matrix iΔ, N=800..3500, ≥4 seeds: (1) PROXY1 trace divergence: untruncated entropy growth vs N (expect volume-like divergence ~ N? or already area — document!) vs truncated saturation; (2) PROXY2 modular spectrum: flat+dense (III₁) before vs integrable with IR edge (II) after truncation — measure density evolution with N; (3) the truncation rank scaling in this geometry: does the clean 4D geometry now give a robust exponent (the p=3/4 question returns — area-law rank ~ N^(3/4) in 4D)? THE STAKES: if III→II signatures + robust rank scaling hold in 4D slab, the crossed-product identification (H3g-3/H2g-3) is supported in the physical dimension with the right geometry — draft-04 material. If not, the 2D result stays 2D. Deliverables dir: ${CD}/calculations/vn-type-slab-4d/; writeup VYPOCET-16-vn-typ-slab-4d.md.`,
    { label: 'calc:vn-type-slab-4d', phase: 'Jádro kola', model: 'opus', schema: CALC_RESULT }),
])

const brainstorm4 = batch[0]
const synteza2 = batch[1]
const calc15 = batch[2]
const calc16 = batch[3]
log('Jádro hotovo (far-zone: ' + (calc15 ? calc15.status : 'N/A') + ', vN-slab: ' + (calc16 ? calc16.status : 'N/A') + '). Úklid…')

phase('Úklid')

const hkData = JSON.stringify({
  calc15: calc15 ? { status: calc15.status, keyNumbers: calc15.keyNumbers, verdict: calc15.verdictForHypothesis } : null,
  calc16: calc16 ? { status: calc16.status, keyNumbers: calc16.keyNumbers, verdict: calc16.verdictForHypothesis } : null,
  brainstorm4: brainstorm4,
  synteza2: synteza2,
}, null, 2)

const housekeeping = await agent(`You are the housekeeping agent at ${ROOT}. Today ${DATE}. Czech prose / English data. ECONOMY MODE. Round-7 results:
${hkData}

TASK 1: Update ${CD}/findings.json — append round-7 findings (far-zone E-vs-S resolution; vN-type 4D slab verdict incl. the p=3/4 question). Conservative wording, evidence paths.
TASK 2: Update ${ROOT}/PROGRESS.md (Read first, preserve): log entry round 7 (BRAINSTORM-04, SYNTEZA-02, VYPOCET-15/16); "Aktuální stav"; "Další kroky" from BRAINSTORM-04 fronta v3.
TASK 3: Update ${KB}/00-INDEX.md: add BRAINSTORM-04, SYNTEZA-02, VYPOCET-15/16.
Return 3-line Czech confirmation.`,
  { label: 'final:round7-writeup', phase: 'Úklid', model: 'sonnet' })

return {
  brainstorm4Summary: brainstorm4,
  synteza2Summary: synteza2,
  calc15: calc15 ? { status: calc15.status, keyNumbers: calc15.keyNumbers } : null,
  calc15Verdict: calc15 ? calc15.verdictForHypothesis : null,
  calc16: calc16 ? { status: calc16.status, keyNumbers: calc16.keyNumbers } : null,
  calc16Verdict: calc16 ? calc16.verdictForHypothesis : null,
  housekeeping: housekeeping,
}