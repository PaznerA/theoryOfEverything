export const meta = {
  name: 'qg-round-04',
  description: 'Kolo 4: BRAINSTORM-03 (dohnání po limitu), VYPOCET-09 BD-d\'Alembertián 4D SSEE, VYPOCET-10 superradiance v SJ eigenvektorech + mechanismus opačných znamének, draft-02 a₄ nota, úklid',
  phases: [
    { title: 'Jádro kola', detail: 'BRAINSTORM-03 + 2 výpočty + draft-02 paralelně' },
    { title: 'Úklid', detail: 'findings.json, PROGRESS, INDEX — dohnání kola 3 + zápis kola 4', model: 'sonnet' },
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

const ROUND3 = `ROUND-3 RESULTS (for context): (1) Kerr equatorial SJ (VYPOCET-08): ALL four BTZ signatures replicate on Kerr — SJ exists machine-precision inside ergoregion (787±/790± pairs, residual ~5e-16) where static section is Euclidean; interior null slope zeroes EXACTLY at r_erg=2M for a=0.6 and 0.9; opposite signs A_caus>0 vs A_W<0 at every a,r (a=0.6 r=2.6: +0.317/−0.296; a=0.9: +0.431/−0.382); A_caus grows monotonically with spin (0.197/0.361/0.482 at a=0.3/0.6/0.9) ⇒ geometry-independent SJ properties in dragged spacetimes. (2) H04 entropy-cluster reframe written: 4D link-matrix spectrum flat ⇒ interpretation (b): wrong OBJECT — BD d'Alembertián is the right candidate (VYPOCET-09). (3) Pillar 19 von Neumann algebras added (27 concepts, 32 verified refs); after consolidation modular-hamiltonian is now a TOP HUB of the concept graph (614 nodes/2437 edges). (4) papers/draft-01-sj-rotating-spacetimes/ written (draft.md v0.1 + TODO.md); weakest point per self-assessment: the opposite-sign A_caus vs A_W phenomenon lacks a mechanism/analytic model. (5) γ–Cardy program killed by Sen IR-universality (round 2). (6) BMV: continuous discriminators unreachable (AS 24 orders below), binary reachable 2030-35. (7) a₄: fermion sector EXACT −18/11 match, full SM falsified. (8) Λ~1/√V unification refuted (~140× prefactor mismatch). (9) SSEE 2D clean ρ^(−1/2) (39σ), 4D non-robust + volume law.`

phase('Jádro kola')
log('Spouštím BRAINSTORM-03, dva výpočty a draft-02 paralelně…')

const batch = await parallel([
  // --- BRAINSTORM-03 (dohnání) ---
  () => agent(`You are the third-round brainstorm synthesizer at ${ROOT}. ${ROUND3}
Read selectively: ${KB}/BRAINSTORM-02.md (incl. decisive-round section), ${KB}/hypotezy/H04-entropy-cluster-reframe.md, ${KB}/foundations/19-von-neumann-algebras.md (Vztahy section), ${CD}/findings.json, ${CD}/_digest.md (fresh — pillar 19 included, modular-hamiltonian is now a top hub).
Write ${KB}/BRAINSTORM-03.md IN CZECH:
# Brainstorming 03 (${DATE})
## Bilance: co žije, co zemřelo      ← tabule všech hypotéz/klastrů po 3 kolech (γ–Cardy ⚰️, Λ-sjednocení ⚰️, a₄ → fermionová identita ✓, SSEE 2D ✓/4D ⚠️, SJ-rotace ✓✓, BMV → binární)
## Lekce z poprav                     ← metodické poučky (Sen-typ univerzalitní argumenty jako rychlý filtr; volba objektu rozhoduje — link matrix vs BD; prefaktor ≠ řád)
## Hypotézy třetí generace            ← 5-8: zahrň minimálně (a) mechanismus opačných znamének A_caus/A_W jako fyzikální jev — co říká o SJ stavech v strhávaných prostoročasech; (b) BD-objekt verzi entropy-clusteru; (c) modulární teorie × SSEE × SJ nyní s daty pilíře 19 (crossed-product hrana s čísly!); (d) a₄ fermionová identita — PROČ přesně fermionový sektor a co to říká o spektrální akci jako fermionově-indukované gravitaci; každá: tvrzení, opora, proč nová, test, confidence
## Výpočetní fronta v2                ← seřazená (VYPOCET-09 BD 4D, VYPOCET-10 superradiance eigenvektory běží v tomto kole — co dál?)
## Strategie publikace                ← draft-01 hotov; doporuč draft-02 (kandidáti: a₄ fermionová identita — krátká exaktní nota; d_s(z,D,probe) tabulka — review-note; SSEE 2D škálování)
Return Czech summary: top 3 hypotézy + doporučený draft-02.`,
    { label: 'brainstorm-03:synth', phase: 'Jádro kola', model: 'opus' }),

  // --- VYPOCET-09: BD d'Alembertián 4D SSEE ---
  () => agent(`You are a computational physics agent at ${ROOT}. Environment: python3 + numpy/scipy/sympy/matplotlib (Agg). Verify conventions via ToolSearch "select:WebFetch,WebSearch". NEVER fudge results.

TASK — VYPOCET-09, the decisive test of H04 interpretation (b) (read ${KB}/hypotezy/H04-entropy-cluster-reframe.md and ${KB}/vypocty/VYPOCET-06-ssee-4d.md first): in 4D, replace the link-matrix retarded Green function with the BENINCASA-DOWKER NONLOCAL D'ALEMBERTIAN object and re-run the SSEE cutoff-scaling protocol. Steps: (1) fetch the BD 4D d'Alembertian B(f(x)) = (4/√6 l_P²)[−f(x) + (Σ over 4 'layers' with coefficients 1,−9,16,−8 of nearest/next/... IF-past elements f(y))] — verify exact coefficients and normalization from Benincasa-Dowker arXiv:0911.2563 (and smeared version Belenchia et al. 1507.00330 if the sharp one is too noisy at our N); (2) build B as a matrix on the sprinkled 4D diamond (reuse sprinkling code from ${CD}/calculations/ssee-4d/calc.py); (3) obtain the retarded Green function as the matrix inverse G_R = B⁻¹ (with appropriate boundary/causality handling — G_R must be lower-triangular in a causal ordering; document how you enforce/verify retardedness) — then iΔ = G_R − G_R^T etc.; (4) run the SSEE protocol: spectrum shape (is it now a clean power law λ_k ~ k^(−α)? compare to flat link-matrix spectrum), entropy-cutoff rank vs N fit (prediction: robust p — is it 3/4?), subdiamond entropy: area vs volume law. N up to ~2000-3000 (matrix inversion is O(N³) — manageable), ≥3 seeds. HONEST outcomes: (i) clean power law + robust p≈3/4 ⇒ interpretation (b) confirmed, hypothesis revived in 4D; (ii) still flat/non-robust ⇒ (b) refuted, the 2D/4D difference is dimensional; (iii) numerical pathologies of B at small N ⇒ document, try smeared BD. Deliverables: ${CD}/calculations/ssee-bd-4d/{calc.py,results.json,plots}, Czech writeup ${KB}/vypocty/VYPOCET-09-ssee-bd-4d.md.`,
    { label: 'calc:ssee-bd-4d', phase: 'Jádro kola', model: 'opus', schema: CALC_RESULT }),

  // --- VYPOCET-10: superradiance in SJ eigenvectors + opposite-sign mechanism ---
  () => agent(`You are a computational physics agent at ${ROOT}. Environment: python3 + numpy/scipy/matplotlib (Agg). ToolSearch "select:WebFetch,WebSearch" for conventions. NEVER fudge.

TASK — VYPOCET-10, two coupled goals on the rotating-SJ front (reuse code+data from ${CD}/calculations/sj-rotating-btz/ and ${CD}/calculations/sj-kerr-equatorial/; read both writeups in ${KB}/vypocty/):
GOAL A — WHERE DOES ROTATION LIVE IN THE SJ STATE? The iΔ spectrum was ~conformally invariant (rotation invisible in eigenvalues); show it lives in eigenvectors/W: (1) for matched rotating vs static regions (outside ergoregion where both exist), compute the SJ Wightman W = Σ_{λ>0} λ v v†; (2) frequency-analyze SJ modes: project eigenvectors onto approximate plane waves e^{−iωt+ikφ} (least-squares on the sprinkled points), build the (ω, k) occupation map of the positive-SJ subspace; (3) SUPERRADIANCE SIGNATURE: in dragged frames, look for modes where the SJ 'positive' subspace contains co-rotating contributions with ω(ω − k·Ω) < 0 (the discrete analog of superradiant mixing) — quantify their weight vs spin a and vs r relative to ergosphere; static control must show ~zero weight.
GOAL B — MECHANISM OF THE OPPOSITE SIGNS (A_caus>0 vs A_W<0 — the weakest point of papers/draft-01): build the analytic toy model: a 2D diamond under a boost/shear (frame dragging tilts cones) — compute analytically (or semi-analytically) how cone-tilting affects (i) causal-pair COUNTING asymmetry (more co-rotating links — geometric effect) vs (ii) the PHASE/correlation asymmetry of the massless Wightman function W₀(x,y) = −(1/4π)ln(...) on tilted intervals (does the correlation asymmetry flip sign because correlations are STRONGER along the squeezed null direction and counting is LARGER along the stretched one?). Verify the toy model against the measured numbers (BTZ +0.317/−0.296; Kerr +0.431/−0.382). If the model works: append a "Mechanism" subsection draft (EN) to ${ROOT}/papers/draft-01-sj-rotating-spacetimes/draft.md (marked "v0.2 addition") and update TODO.md.
Deliverables: ${CD}/calculations/sj-eigenvector-superradiance/{calc.py,results.json,plots}, Czech writeup ${KB}/vypocty/VYPOCET-10-superradiance-eigenvektory.md.`,
    { label: 'calc:sj-superradiance', phase: 'Jádro kola', model: 'opus', schema: CALC_RESULT }),

  // --- draft-02: a4 fermionic identity note ---
  () => agent(`You are a theoretical-physics paper-writing agent. Write the project's SECOND draft IN ENGLISH: a short, sharp note from the exact a₄ result. Sources: ${KB}/vypocty/VYPOCET-02-a4-matching.md + ${CD}/calculations/a4-anomaly-matching/results.json + ${ROOT}/verification/novelty/a4-cluster.md (novelty: the three-way identification was never published; two-way links: Andrianov-Lizzi 1001.2036, Kurkov-Lizzi-Vassilevich 1106.3263 — cite them prominently and position the note as completing their triangle).
Write ${ROOT}/papers/draft-02-a4-fermionic-identity/draft.md:
- Title candidate: "The Weyl-to-Euler coefficient ratio −18/11: an exact fermionic identity linking the spectral action, induced gravity, and the trace anomaly" (improve if you can)
- Content: the exact statement (coeff(C²)/coeff(Euler) = −18/11 both in the Chamseddine-Connes spectral action a₄ term AND in the (c,−a) anomaly ratio of a single Weyl fermion — hence of ANY purely fermionic content, 45 or 48 Weyl fermions alike); why this is a theorem not a coincidence (both descend from the same Dirac-operator heat kernel — make the derivation explicit, 1 page); the sharp falsification of the naive full-SM version (bosons break it: −0.853 vs −1.636) and what that teaches (the spectral action is fermion-induced gravity à la Sakharov — bosonic loops are NOT part of the a₄ identity); the ν_R observation (moves full-SM closer but fermionic identity is content-independent); implications + outlook (anomaly-matching as a constraint on almost-commutative geometries).
- Line 1: "DRAFT v0.1 — generated ${DATE}, internal research draft, NOT submitted, requires human review."
- TODO.md: referee attacks (convention dependence! — document Duff 2003.02688 + Vassilevich hep-th/0306138 conventions used; is the identity 'trivial' to an expert? — address why nobody stated it; scheme dependence of a₄), AI-assisted ethics note.
Return Czech 4-line summary: co nota tvrdí, síla, slabina, doporučení.`,
    { label: 'paper:draft-02-a4', phase: 'Jádro kola', model: 'opus' }),
])

const brainstorm3 = batch[0]
const calc9 = batch[1]
const calc10 = batch[2]
const draft02 = batch[3]
log('Jádro hotovo (VYPOCET-09: ' + (calc9 ? calc9.status : 'N/A') + ', VYPOCET-10: ' + (calc10 ? calc10.status : 'N/A') + '). Úklid…')

// ---------- Úklid ----------
phase('Úklid')

const hkData = JSON.stringify({
  round3CatchUp: 'Round-3 housekeeping was killed by session limit — you must catch up on it too. ' + ROUND3,
  round4: {
    calc9: calc9 ? { status: calc9.status, keyNumbers: calc9.keyNumbers, verdict: calc9.verdictForHypothesis } : null,
    calc10: calc10 ? { status: calc10.status, keyNumbers: calc10.keyNumbers, verdict: calc10.verdictForHypothesis } : null,
    draft02: draft02,
    brainstorm3: brainstorm3,
  },
}, null, 2)

const housekeeping = await agent(`You are the housekeeping agent at ${ROOT}. Today ${DATE}. Czech prose / English data. ECONOMY MODE. Data (round-3 catch-up + round-4 results):
${hkData}

TASK 1: Update ${CD}/findings.json — append entries for BOTH rounds: (round 3) Kerr replication of all BTZ SJ signatures (geometry-independence); γ–Cardy program killed (Sen IR-universality); pillar-19/modular-hamiltonian became top hub after consolidation; (round 4) VYPOCET-09 BD-d'Alembertián outcome; VYPOCET-10 superradiance/mechanism outcome. Keep schema, conservative wording, evidence file paths.
TASK 2: Update ${ROOT}/PROGRESS.md (Read first, preserve): log entries for round 3 (Kerr, H04, pilíř 19, draft-01) and round 4 (BRAINSTORM-03, VYPOCET-09, VYPOCET-10, draft-02); "Aktuální stav" → 2 drafty článků čekají lidskou revizi, výzkum pokračuje; "Další kroky" from BRAINSTORM-03 fronta.
TASK 3: Update ${KB}/00-INDEX.md: add papers/draft-01 + draft-02, VYPOCET-08/09/10, H04, pilíř 19, BRAINSTORM-03.
TASK 4: Note for registry freshness: consolidate.py was already re-run manually after pillar 19 (614 nodes/2437 edges) — only re-run it (python3 ${ROOT}/workflows/consolidate.py && python3 ${ROOT}/workflows/consolidate.py --apply-merges) IF any fragment file changed in round 4 (check mtimes vs registries).
Return 4-line Czech confirmation.`,
  { label: 'final:catch-up-writeup', phase: 'Úklid', model: 'sonnet' })

return {
  brainstorm3Summary: brainstorm3,
  calc9: calc9 ? { status: calc9.status, keyNumbers: calc9.keyNumbers } : null,
  calc9Verdict: calc9 ? calc9.verdictForHypothesis : null,
  calc10: calc10 ? { status: calc10.status, keyNumbers: calc10.keyNumbers } : null,
  calc10Verdict: calc10 ? calc10.verdictForHypothesis : null,
  draft02Summary: draft02,
  housekeeping: housekeeping,
}