export const meta = {
  name: 'qg-round-06',
  description: 'Kolo 6: VYPOCET-13 SSEE geometrie slab/Rindler 4D (interpretace a vs c), VYPOCET-14 threshold scan superradiance, draft-03 d_s klasifikace, ESEJ-03 gravitace jako stín fermionů, úklid',
  phases: [
    { title: 'Jádro kola', detail: '2 výpočty + draft-03 + esej paralelně' },
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

const CALC_COMMON = `You are a computational physics agent at ${ROOT}. Environment: python3 + numpy/scipy/sympy/matplotlib (Agg). Verify conventions against literature (ToolSearch "select:WebFetch,WebSearch"). NEVER fudge results. Deliverables: <dir>/calc.py, <dir>/results.json (EN), plots, Czech writeup in ${KB}/vypocty/.

YOUR TASK: `

phase('Jádro kola')
log('Spouštím geometrický test SSEE, threshold scan, draft-03 a esej…')

const batch = await parallel([
  // --- VYPOCET-13: SSEE geometry test 4D (interpretation a vs c) ---
  () => agent(CALC_COMMON + `VYPOCET-13 — decide between H04 interpretations (a) [2D-only cleanliness] and (c) [volume law = real signal of SJ non-Hadamardness on diamonds] (read ${KB}/hypotezy/H04-entropy-cluster-reframe.md, ${KB}/vypocty/VYPOCET-06-ssee-4d.md, VYPOCET-09, VYPOCET-12). The 4D nested-DIAMOND gave volume law; the question: is that the GEOMETRY's fault (diamond corners / non-Hadamard SJ on diamonds) or genuinely 4D? TEST: change the region geometry at fixed dimension. (1) Build a 4D causal SLAB: sprinkle into a box-like region {0<t<T, |x_i|<L} with T<<L (approximating a Rindler-like/half-space entangling surface — document edge effects honestly); restrict to the sub-slab x_1>0 and compute the SSEE of the half-space cut with the link-matrix iΔ (validated object; BD does not change scaling per VYPOCET-09). Does the half-space cut give AREA law where nested diamonds gave volume? (2) Same protocol in 2D as control (slab vs diamond — both should be clean). (3) Hadamard diagnostic: measure the short-distance behavior of the SJ Wightman W(x,y) along the entangling surface vs deep inside — does W have the Minkowski/Hadamard 1/sigma form inside but anomalous behavior near the diamond's corners (supporting interpretation c)? Compare diamond vs slab. N up to ~3000-4000 4D, >=3 seeds. OUTCOMES: slab area law + diamond corner anomaly => (c) confirmed, geometry-specific, hypothesis lives in 4D with right region; slab also volume => 4D problem is real, (a) wins. Deliverables dir: ${CD}/calculations/ssee-slab-4d/; writeup VYPOCET-13-ssee-slab-4d.md.`,
    { label: 'calc:ssee-slab-4d', phase: 'Jádro kola', model: 'opus', schema: CALC_RESULT }),

  // --- VYPOCET-14: superradiance threshold scan (H3g-1) ---
  () => agent(CALC_COMMON + `VYPOCET-14 — superradiant THRESHOLD scan (test of H3g-1, see ${KB}/BRAINSTORM-03.md; reuse code+data from ${CD}/calculations/sj-eigenvector-superradiance/ and read VYPOCET-10 writeup). VYPOCET-10 showed the SJ positive subspace acquires weight in the wedge ω(ω−kΩ)<0, growing toward the ergosphere. Now resolve WHERE the effect turns on and WHAT controls it: (1) fine radial scan (Kerr equatorial a=0.6, 0.9: 12+ radii from far zone to just outside r_+) of (i) the wedge weight, (ii) A_W, (iii) the (ω,k)-resolved occupation map; (2) the discriminating question: does the onset track the ERGOSPHERE r_erg=2M (geometry; frame-dragging of cones) or the mode-wise SUPERRADIANT CONDITION ω<kΩ(r) with local Ω(r)=−g_tφ/g_φφ (state/frequency content)? These differ quantitatively away from the horizon — fit both models to the onset curve and report which wins (AIC/BIC or chi2); (3) does A_W's SIGN ever flip across the scan, or only its magnitude grows (VYPOCET-10's toy model predicts: sign fixed by shear direction, magnitude tracks shear strength — verify); (4) BTZ cross-check at one matching set. Same N≈1600, ≥3 seeds. The answer sharpens the 4D Teukolsky prediction in draft-01 §4.2 — if conclusive, append a dated note to papers/draft-01-sj-rotating-spacetimes/TODO.md. Deliverables dir: ${CD}/calculations/sj-threshold-scan/; writeup VYPOCET-14-threshold-scan.md.`,
    { label: 'calc:sj-threshold-scan', phase: 'Jádro kola', model: 'sonnet', schema: CALC_RESULT }),

  // --- draft-03: d_s classification note ---
  () => agent(`You are a theoretical-physics paper-writing agent. Write the project's THIRD draft IN ENGLISH: a review-note positioning the spectral dimension as a CLASSIFIER, not a universal constant. Sources: ${KB}/vypocty/VYPOCET-01-ds-klasifikace.md + ${CD}/calculations/ds-classification/results.json + ${ROOT}/verification/novelty/ds-cluster.md + ${ROOT}/verification/ds-contradiction.md. PRIOR ART TO POSITION AGAINST HONESTLY (this is the note's referee risk — overlap is HIGH): Hořava 0902.3657 (d_s=1+D/z), Sotiriou-Visser-Weinfurtner 1105.6098, Calcagni-Oriti-Thürigen 1311.3340, Calcagni 1708.07445, Carlip 1705.05417, Eichhorn-Mizera 1311.2530, Belenchia et al. 1507.00330. The note's claimed contributions (per the novelty check): (1) ONE return-probability engine P(σ)=∫d^Dk e^{−σF(k)} numerically validated across GR/Hořava/Stelle/AS/CST simultaneously (12/12 checks); (2) PROBE as an explicit third classification axis — same theory (CST) yields d_s→2 (d'Alembertian) vs d_s>D (random walk), so "the UV dimension" is ill-posed without naming the probe; (3) the discriminator interpretation: apparent universality of d_s→2 is a subclass artifact (UV k⁴ propagators), explicitly violated by GR(4), Hořava z=2 (5/2), random-walk probes.
Write ${ROOT}/papers/draft-03-ds-classifier/draft.md (line 1: "DRAFT v0.1 — generated ${DATE}, internal research draft, NOT submitted, requires human review."): title candidate "The UV spectral dimension is a fingerprint, not a constant: a (z, D, probe) classification across quantum-gravity approaches" (improve if you can); abstract; the master table as the centerpiece; the probe-dependence section built on the CST resolution; honest "Relation to prior work" section EARLY (not buried); limitations. TODO.md: referee attacks (esp. "this is Calcagni's program repackaged" — prepare the defense: simultaneous validated engine + probe axis + discriminator framing; and "probe-dependence is obvious" — counter with the published contradiction we found and fixed in our own database). Return Czech 4-line summary.`,
    { label: 'paper:draft-03-ds', phase: 'Jádro kola', model: 'opus' }),

  // --- ESEJ-03 ---
  () => agent(`You are an essayist-physicist at ${ROOT}. The user explicitly wants imagination UNLEASHED in prose. Write IN CZECH: ${KB}/eseje/ESEJ-03-gravitace-jako-stin.md — "Gravitace jako stín fermionů". Header line: "⚠️ SPEKULATIVNÍ ESEJ — fantazie odbrzděná, fakta citována, extrapolace značeny". Interleave "Co víme" (cited) and "Co kdyby" (unleashed); end with "Co by muselo být pravda" (falsifiable core).
Material to draw on (read): ${KB}/vypocty/VYPOCET-02-a4-matching.md, VYPOCET-11-graviton-index.md, ${ROOT}/papers/draft-02-a4-fermionic-identity/draft.md, ${KB}/BRAINSTORM-03.md (H3g-4), ${KB}/approaches/09-emergent-gravity.md (Sakharov), ${KB}/approaches/07-noncommutative-geometry.md.
The thread: the −18/11 identity holds EXACTLY for fermions and for nothing else; the graviton cannot be added at any multiplicity; the ratio is protected by the Atiyah-Singer index theorem. Co kdyby: gravity is not a force but the renormalization shadow cast by fermionic matter on the spectral geometry it inhabits — Sakharov's "metric elasticity" made exact; bosons are bookkeeping of fermion bilinears; the index theorem as the deepest layer (gravity's couplings counted by topology, not dynamics); what this would mean for quantization of gravity (nothing to quantize — only fermions are fundamental), for the cosmological constant, for why the graviton resists QFT. Wild but grounded extrapolations, clearly marked. 400-700 lines.`,
    { label: 'esej:gravitace-stin', phase: 'Jádro kola', model: 'opus' }),
])

const calc13 = batch[0]
const calc14 = batch[1]
const draft03 = batch[2]
const esej03 = batch[3]
log('Jádro hotovo (slab: ' + (calc13 ? calc13.status : 'N/A') + ', threshold: ' + (calc14 ? calc14.status : 'N/A') + '). Úklid…')

phase('Úklid')

const hkData = JSON.stringify({
  calc13: calc13 ? { status: calc13.status, keyNumbers: calc13.keyNumbers, verdict: calc13.verdictForHypothesis } : null,
  calc14: calc14 ? { status: calc14.status, keyNumbers: calc14.keyNumbers, verdict: calc14.verdictForHypothesis } : null,
  draft03: draft03,
  esej03: esej03 ? 'ESEJ-03 written' : 'essay failed',
}, null, 2)

const housekeeping = await agent(`You are the housekeeping agent at ${ROOT}. Today ${DATE}. Czech prose / English data. ECONOMY MODE. Round-6 results:
${hkData}

TASK 1: Update ${CD}/findings.json — append round-6 findings (SSEE slab geometry verdict — which H04 interpretation won; superradiance onset: ergosphere vs mode threshold; draft-03 written). Conservative wording, evidence paths.
TASK 2: Update ${ROOT}/PROGRESS.md (Read first, preserve): log entry round 6; "Aktuální stav" (3 drafty, 16+ nálezů); "Další kroky" — reflect what calc13 means for the entropy-cluster program and calc14 for the 4D Kerr/Teukolsky strategy. If material has accumulated for BRAINSTORM-04 (it has: index-protection, vN-type evidence, slab verdict, threshold verdict), list it as the recommended next step.
TASK 3: Update ${KB}/00-INDEX.md: add VYPOCET-13/14, draft-03, ESEJ-03.
Return 3-line Czech confirmation.`,
  { label: 'final:round6-writeup', phase: 'Úklid', model: 'sonnet' })

return {
  calc13: calc13 ? { status: calc13.status, keyNumbers: calc13.keyNumbers } : null,
  calc13Verdict: calc13 ? calc13.verdictForHypothesis : null,
  calc14: calc14 ? { status: calc14.status, keyNumbers: calc14.keyNumbers } : null,
  calc14Verdict: calc14 ? calc14.verdictForHypothesis : null,
  draft03Summary: draft03,
  esej03: esej03 ? 'written' : null,
  housekeeping: housekeeping,
}