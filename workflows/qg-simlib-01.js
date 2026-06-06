export const meta = {
  name: 'qg-simlib-01',
  description: 'Krok 3 roadmapy: kombinovatelná simulační knihovna lib/toe/ z verifikovaných calc.py + formulas.json, s validačními testy proti results.json',
  phases: [
    { title: 'Architektura', detail: 'API spec, konvence, validační cíle', model: 'opus' },
    { title: 'Implementace A', detail: 'fits, causet, spectral, ncg, viz (nezávislé moduly)' },
    { title: 'Implementace B', detail: 'sj (závisí na causet)' },
    { title: 'Implementace C', detail: 'entropy, vntype (závisí na sj)' },
    { title: 'Integrace', detail: 'celá test suite, exporty, README, PROGRESS', model: 'opus' },
  ],
}

const ROOT = '/Users/pazny/projects/theoryOfEverything'
const CD = ROOT + '/core-data'
const LIB = ROOT + '/lib'
const DATE = (args && args.date) || '2026-06-06'

const ARCH = {
  type: 'object',
  properties: {
    modules: {
      type: 'array',
      items: {
        type: 'object',
        properties: {
          file: { type: 'string' },
          functions: { type: 'array', items: { type: 'string' }, description: 'signatures' },
          validationTargets: { type: 'array', items: { type: 'string' } },
        },
        required: ['file', 'functions', 'validationTargets'],
      },
    },
    notes: { type: 'string' },
  },
  required: ['modules', 'notes'],
}

const BUILD = {
  type: 'object',
  properties: {
    module: { type: 'string' },
    functions: { type: 'array', items: { type: 'string' } },
    testFile: { type: 'string' },
    testsPassed: { type: 'boolean' },
    testRuntimeSeconds: { type: 'number' },
    notes: { type: 'string' },
  },
  required: ['module', 'functions', 'testFile', 'testsPassed', 'testRuntimeSeconds', 'notes'],
}

const NOTE = {
  type: 'object',
  properties: {
    file: { type: 'string' },
    keyPoints: { type: 'array', items: { type: 'string' }, description: 'Czech' },
  },
  required: ['file', 'keyPoints'],
}

// ---------------- phase 1: architecture ----------------
phase('Architektura')
log('Architekt navrhuje API knihovny toe…')

const arch = await agent(`You are the library architect at ${ROOT}. The project is building roadmap step 3: a COMPOSABLE simulation library distilled from 20 verified calc.py scripts (all bit-reproducible, see reports/2026-06-06-review.md §f). Code + identifiers ENGLISH (project policy); README prose will be Czech (not your job).

READ FIRST: reports/2026-06-06-review.md section "(g)" (the architectural principle: physics-parameter inputs, (value, SE/bootstrap-CI) outputs, validated flag); skim ${CD}/formulas.json (247 formulas with ids — functions must reference formula ids in docstrings); skim these calc.py for existing conventions: ${CD}/calculations/sj-rotating-btz/calc.py, ${CD}/calculations/sj-vn-type/calc.py (+ calc_uncertainty.py — the validated SE/bootstrap approach), ${CD}/calculations/ds-classification/calc.py, ${CD}/calculations/a4-anomaly-matching/calc.py.

DESIGN the package ${LIB}/toe/ with EXACTLY these modules (smallest composable units; dependency layers A: independent, B: needs causet, C: needs sj):
A1 toe/fits.py — powerlaw_fit(x, y) -> FitResult(value, se_regression, ci68_bootstrap(>=1000 resamples), r2); aic_compare(models...); follows sj-vn-type/calc_uncertainty.py exactly.
A2 toe/causet.py — sprinkle_* region builders (diamond2d, slab2d, box4d, slab4d, ds_static_patch2d with sech^2 proper measure), causal_matrix, link_matrix, retarded Green G_R (link convention sqrt(rho)/(2*pi*sqrt(6))*L and BD d'Alembertian inverse), pauli_jordan iDelta = G_R - G_R^T; seeds explicit args everywhere.
A3 toe/spectral.py — heat-kernel return probability P(sigma), spectral dimension d_s(sigma), the classifier d_s_uv(z, D, probe/convention) reproducing the ds-classification master table.
A4 toe/ncg.py — exact sympy: a4 heat-kernel coefficients per field content, a4_ratio(...) == Rational(-18,11) for SM fermions, sector ledger, STr counting, Lambda-induction ledger (from a4-anomaly-matching, a4-graviton-index, lambda-induced).
A5 toe/viz.py — small matplotlib(Agg) helpers: powerlaw panel with CI band, spectrum plot, radial-scan plot; figures returned, optional save path.
B1 toe/sj.py — SJ state from iDelta (positive spectral part), Wightman W, asymmetry observables A_caus, A_W, superradiant weight W_sr (eigenvector-overlap construction from sj-eigenvector-superradiance).
C1 toe/entropy.py — SSEE via the generalized eigenproblem on a region/complement cut, truncation n_max (incl. the 2*N^(3/4) prescription), entropy scaling vs region size.
C2 toe/vntype.py — von Neumann type proxies: entropy-trace scaling, modular spectrum eps=ln(mu/(mu-1)), pile-up measure, truncated-entropy saturation discriminator (II_1 vs II_infinity, from sj-desitter-type).

WRITE ${LIB}/toe/ARCHITECTURE.md (English, the contract for the builder agents) with: (1) exact function signatures + return types per module (a common lightweight Result convention: plain dataclasses with value/se/ci68/validated fields where applicable); (2) docstring convention: each public function cites formula ids from formulas.json + the VYPOCET evidence; (3) VALIDATION TARGETS per module — concrete numbers from the committed ${CD}/calculations/*/results.json the tests must reproduce: exact equality for sympy modules (ncg: -18/11; spectral: master-table values), machine-precision invariants (causet: iDelta +/- eigenvalue pairing ~1e-13), and SMALL-N smoke targets with generous tolerance for stochastic modules so each module's test runs <60 s (state exact target values you read from the results.json files — do not guess); (4) import-dependency rules (C imports B imports A; no cycles); (5) test file naming app/tests/test_toe_<module>.py and the conftest sys.path shim. ALSO WRITE: ${ROOT}/app/tests/conftest.py (adds ${LIB} to sys.path) and an EMPTY placeholder ${LIB}/toe/__init__.py (integrator fills exports later).
Return modules (file, signatures, validationTargets) + notes.`,
  { label: 'architect', phase: 'Architektura', model: 'opus', schema: ARCH })

log('Architektura hotova (' + arch.modules.length + ' modulů). Stavím vrstvu A (5 modulů paralelně)…')

// ---------------- builder prompt factory ----------------
function builderPrompt(spec) {
  return `You are a library builder at ${ROOT}. Code + comments ENGLISH. NEVER fudge numbers; validation targets come from committed results.json files.

CONTRACT: Read ${LIB}/toe/ARCHITECTURE.md FIRST and implement YOUR module exactly per its signatures and validation targets.

YOUR MODULE: ${spec.module}
SOURCE MATERIAL (extract + refactor from these verified scripts — do NOT modify them): ${spec.sources}
${spec.extra || ''}

REQUIREMENTS:
- Smallest composable functions; physics-parameter inputs; explicit seed args for anything stochastic; no global state; numpy/scipy/sympy only (+ matplotlib Agg for viz).
- Docstrings cite formula ids from ${CD}/formulas.json and VYPOCET evidence per ARCHITECTURE.md convention.
- Write ${ROOT}/app/tests/test_toe_${spec.shortName}.py implementing the module's validation targets from ARCHITECTURE.md. Keep total test runtime UNDER 60 s (reduce N, fix seeds; tolerance per contract).
- RUN your tests via Bash until green: cd ${ROOT} && MPLBACKEND=Agg python3 -m pytest app/tests/test_toe_${spec.shortName}.py -v (report the runtime).
- Touch ONLY your module file + your test file.
Return module, functions, testFile, testsPassed, testRuntimeSeconds, notes.`
}

// ---------------- phase 2: layer A ----------------
phase('Implementace A')

const layerA = [
  { module: LIB + '/toe/fits.py', shortName: 'fits', sources: CD + '/calculations/sj-vn-type/calc_uncertainty.py (the validated SE+bootstrap approach), ' + CD + '/calculations/sj-threshold-scan/calc.py (AIC model comparison)' },
  { module: LIB + '/toe/causet.py', shortName: 'causet', sources: CD + '/calculations/ssee-diamond/calc.py (2D diamond sprinkling, iDelta), ' + CD + '/calculations/ssee-slab-4d/calc.py + vn-type-slab-4d/calc.py (4D box/slab, link matrix), ' + CD + '/calculations/ssee-bd-4d/calc.py (BD d Alembertian with coefficients (1,-9,16,-8), prefactor 4*sqrt(rho)/sqrt(6), smeared variant), ' + CD + '/calculations/sj-desitter-type/calc.py (dS static patch sech^2 measure)', extra: 'CRITICAL invariant test: iDelta eigenvalues come in +/- pairs to machine precision (~1e-13) on every region builder.' },
  { module: LIB + '/toe/spectral.py', shortName: 'spectral', sources: CD + '/calculations/ds-classification/calc.py (P(sigma) engine + master table d_s_uv(z,D))', extra: 'Exact targets: the master-table values in ds-classification/results.json (12 published values reproduced by the engine). Mind the D vs D_space convention documented in papers/draft-03 (Horava rows use D_space=3).' },
  { module: LIB + '/toe/ncg.py', shortName: 'ncg', sources: CD + '/calculations/a4-anomaly-matching/calc.py (a4 sector ledger), ' + CD + '/calculations/a4-graviton-index/calc.py (graviton ledger, index protection), ' + CD + '/calculations/lambda-induced/calc.py (Lambda induction ledger, STr counting)', extra: 'Exact sympy targets: a4_ratio for SM fermion content == Rational(-18,11); STr(1) == -62 (no nu_R) / -68 (with nu_R).' },
  { module: LIB + '/toe/viz.py', shortName: 'viz', sources: 'plotting patterns across ' + CD + '/calculations/*/calc.py (Agg backend); keep helpers generic', extra: 'Tests: figures render to a tmp path without error; no numeric validation needed.' },
]

const resA = await parallel(layerA.map(s => () =>
  agent(builderPrompt(s), { label: 'build:' + s.shortName, phase: 'Implementace A', model: s.shortName === 'causet' ? 'opus' : 'sonnet', schema: BUILD })))

const failedA = resA.filter(r => !r || !r.testsPassed)
if (failedA.length) log('POZOR: vrstva A má ' + failedA.length + ' nehotových modulů — integrátor je musí dořešit.')

// ---------------- phase 3: layer B ----------------
phase('Implementace B')
log('Vrstva A hotova. Stavím sj.py (vrstva B)…')

const resB = await agent(builderPrompt({
  module: LIB + '/toe/sj.py', shortName: 'sj',
  sources: CD + '/calculations/sj-rotating-btz/calc.py (SJ construction, A_caus/A_W asymmetries, BTZ conformal trick G_R = C/2), ' + CD + '/calculations/sj-kerr-equatorial/calc.py (Kerr equatorial sections), ' + CD + '/calculations/sj-eigenvector-superradiance/calc.py (W_sr eigenvector-overlap weight)',
  extra: 'Import toe.causet (layer A is built). Smoke target: on a small 2D diamond (N~300, fixed seed) the SJ state satisfies the +/- pairing invariant and W >= 0 spectrally; BTZ small-N: A_W < 0 outside (sign target from sj-rotating-btz/results.json — read the exact recorded signs).',
}), { label: 'build:sj', phase: 'Implementace B', model: 'opus', schema: BUILD })

// ---------------- phase 4: layer C ----------------
phase('Implementace C')
log('sj.py hotov. Stavím entropy.py + vntype.py (vrstva C paralelně)…')

const layerC = [
  { module: LIB + '/toe/entropy.py', shortName: 'entropy', sources: CD + '/calculations/ssee-diamond/calc.py (SSEE generalized eigenproblem, 2D), ' + CD + '/calculations/ssee-slab-4d/calc.py (4D slab cut), ' + CD + '/calculations/sj-vn-type/calc.py (truncation n_max prescriptions)', extra: 'Imports toe.causet + toe.sj + toe.fits. Smoke target: 2D diamond small-N SSEE runs and entropy decreases under truncation; rank/N^((d-1)/d) prescription wiring per VYPOCET-04 (exact small-N targets per ARCHITECTURE.md).' },
  { module: LIB + '/toe/vntype.py', shortName: 'vntype', sources: CD + '/calculations/sj-vn-type/calc.py (proxies 1-3), ' + CD + '/calculations/vn-type-slab-4d/calc.py (4D), ' + CD + '/calculations/sj-desitter-type/calc.py (II_1 vs II_infinity saturation discriminator)', extra: 'Imports toe.causet + toe.sj + toe.fits. Smoke targets: modular spectrum eps=ln(mu/(mu-1)) computed on small 2D diamond; truncated pile-up == 0 exactly (the sharp IR edge result, per sj-vn-type/results.json); saturation discriminator returns opposite trends on tiny dS-vs-flat pair (qualitative, generous tolerance).' },
]

const resC = await parallel(layerC.map(s => () =>
  agent(builderPrompt(s), { label: 'build:' + s.shortName, phase: 'Implementace C', model: 'sonnet', schema: BUILD })))

// ---------------- phase 5: integration ----------------
phase('Integrace')

const buildSummary = JSON.stringify({
  A: resA.filter(Boolean).map(r => ({ m: r.module, ok: r.testsPassed, t: r.testRuntimeSeconds })),
  B: resB ? { m: resB.module, ok: resB.testsPassed, t: resB.testRuntimeSeconds } : null,
  C: resC.filter(Boolean).map(r => ({ m: r.module, ok: r.testsPassed, t: r.testRuntimeSeconds })),
}, null, 1)

const integration = await agent(`You are the integration agent at ${ROOT}. Today ${DATE}. Czech prose / English code. Build summary of lib/toe/ (8 modules, layered A/B/C):
${buildSummary}

TASKS in order:
1. Write ${LIB}/toe/__init__.py: clean public exports per module (read each module's public functions), __version__ = '0.1.0', short module map docstring.
2. Run the FULL suite: cd ${ROOT} && MPLBACKEND=Agg python3 -m pytest app/tests -v. FIX any failures (imports, small bugs — but NEVER weaken a validation target to make a test pass; if a target is genuinely unreachable, mark the test xfail with reason + document). Also verify the pre-existing tests (test_environment, test_reproduction fast set) still pass.
3. Write ${LIB}/README.md IN CZECH: účel (krok 3 roadmapy — kombinovatelné funkce podporující/vyvracející teze), mapa modulů s vrstvami A/B/C, princip (fyzikální vstupy, (hodnota, SE/CI) výstupy, validated flag, formula-id docstringy), jak spouštět testy (host i docker compose run --rm test), 2-3 příklady kompozice (code snippets: e.g. sprinkle -> iDelta -> sj_state -> ssee -> powerlaw_fit; a4_ratio; ds_uv classifier).
4. Write ONE runnable example ${LIB}/examples/demo_pipeline.py (English code): end-to-end small-N pipeline (2D diamond N~500: sprinkle -> SJ -> truncated SSEE -> powerlaw_fit -> viz panel saved to ${LIB}/examples/demo_output.png), runtime < 60 s. Run it to verify.
5. Update ${ROOT}/PROGRESS.md (Read first, preserve): banner -> krok 3 zahájen/hotová první verze lib/toe v0.1.0 (8 modulů, testy zelené); log entry with key facts; roadmap item 3 status.
6. Update ${ROOT}/knowledge-base/00-INDEX.md: Infrastruktura section — add lib/toe + examples.
Return file (lib/README.md path) + keyPoints (Czech, include final pytest tally and any xfails).`,
  { label: 'integrate', phase: 'Integrace', model: 'opus', schema: NOTE })

return {
  architecture: { modules: arch.modules.map(m => m.file), notes: arch.notes },
  builds: { A: resA, B: resB, C: resC },
  integration: integration,
}
