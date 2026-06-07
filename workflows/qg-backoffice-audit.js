export const meta = {
  name: 'qg-backoffice-audit',
  description: 'Revize backoffice před dalším dnem výzkumu: deliverables vs. disk (vč. qg-knowledge-foundation), datová pipeline fragments↔registry, infra (app/lib/compute/CI), zakódování provozních poučení + guard testy',
  phases: [
    { title: 'Audity', detail: '4 paralelní: deliverables, data pipeline, infra, procesní poučení' },
    { title: 'Opravy', detail: 'bezpečné opravy nálezů (podmíněně)', model: 'sonnet' },
    { title: 'Syntéza', detail: 'audit report + CLAUDE.md konvence + PROGRESS + commit', model: 'opus' },
  ],
}

const ROOT = '/Users/pazny/projects/theoryOfEverything'
const DATE = (args && args.date) || '2026-06-07'

const AUDIT = {
  type: 'object',
  properties: {
    area: { type: 'string' },
    findings: {
      type: 'array',
      items: {
        type: 'object',
        properties: {
          severity: { type: 'string', description: 'blocker | major | minor | info' },
          what: { type: 'string', description: 'Czech' },
          where: { type: 'string' },
          suggestedFix: { type: 'string', description: 'Czech; "none" if informational' },
          safeToAutofix: { type: 'boolean' },
        },
        required: ['severity', 'what', 'where', 'suggestedFix', 'safeToAutofix'],
      },
    },
    checksPassed: { type: 'array', items: { type: 'string' }, description: 'Czech' },
    filesWritten: { type: 'array', items: { type: 'string' } },
  },
  required: ['area', 'findings', 'checksPassed', 'filesWritten'],
}

const NOTE = {
  type: 'object',
  properties: {
    file: { type: 'string' },
    keyPoints: { type: 'array', items: { type: 'string' }, description: 'Czech' },
  },
  required: ['file', 'keyPoints'],
}

phase('Audity')
log('4 paralelní audity backoffice…')

const audits = await parallel([
  // ---- 1: deliverables vs disk ----
  () => agent(`You are a deliverables auditor at ${ROOT}. Czech findings. The user noticed the FIRST workflow (workflows/qg-knowledge-foundation.js) may not have completed fully. AUDIT EVERY archived workflow script in ${ROOT}/workflows/*.js: read each, extract the output files its agent prompts promise (markdown paths, JSON paths, calc dirs, reports), and CHECK THE DISK: file exists, non-trivially sized, valid JSON where applicable (python3 -c json.load for each registry/fragment).
SPECIFICALLY for qg-knowledge-foundation: all 18 pillar md files (approaches/cross-cutting/foundations/phenomenology naming per kbFile()), all 18 core-data/fragments/*.json, verification/<slug>.md reports (count them — pipeline stage 2 may have died for some pillars on the session-limit day), SYNTEZA.md, the 4 registries, 00-INDEX.md. NOTE: knowledge-base has a 19th pillar (19-von-neumann-algebras) added later — not a gap.
Also check: every Workflow invocation from PROGRESS.md log has its script archived in workflows/ (cross-reference round numbers 03..12 + special ones); flag scripts whose prompts embed machine-absolute paths that LEAK into portable artifacts (the known antipattern — informational, scripts themselves run locally).
Do NOT fix anything. Return findings (one per missing/thin/invalid artifact) + checksPassed.`,
    { label: 'audit:deliverables', phase: 'Audity', model: 'sonnet', schema: AUDIT }),

  // ---- 2: data pipeline ----
  () => agent(`You are a data-pipeline auditor at ${ROOT}. Czech findings. The pipeline contract: core-data/fragments/*.json are the SOURCE OF TRUTH; workflows/consolidate.py deterministically regenerates the registries (concept-graph.json, references.json + .bib, formulas.json, open-problems.json, connections.json, _digest.md).
CHECKS:
1. STALENESS: copy fragments + consolidate.py to /tmp/audit-consolidate/, run it there, diff regenerated registries against committed ones (python json compare, ignore ordering where the script itself is order-stable). Any drift = someone edited registries directly (violation) or consolidate wasn't re-run after fragment edits.
2. COVERAGE of recent work: findings.json has F-001..F-028 — do the corresponding NEW results have any representation in fragments/connections where appropriate (e.g. dS entropy cap F-028, codim-2 refutation F-026)? Missing = the graph no longer reflects the research frontier (recommendation-level, not autofix).
3. INTEGRITY: every finding's evidence paths exist on disk (ls); every calculations/<dir> with results.json has a matching VYPOCET writeup in knowledge-base/vypocty/ and vice versa; counts claimed in 00-INDEX.md/PROGRESS banner (28 nálezů, 22→24 výpočtů, registry stats) match reality.
4. fragments/*.json all valid JSON; no fragment exists without its pillar md and vice versa (except documented exceptions).
Do NOT fix anything. Return findings + checksPassed.`,
    { label: 'audit:data-pipeline', phase: 'Audity', model: 'opus', schema: AUDIT }),

  // ---- 3: infra ----
  () => agent(`You are an infrastructure auditor at ${ROOT}. Czech findings. Areas:
1. TESTS: run cd ${ROOT} && MPLBACKEND=Agg python3 -m pytest app/tests -q — full suite must be green; report tally + runtime.
2. lib/toe: __version__ vs ARCHITECTURE.md CHANGELOG vs lib/README.md agree; __init__ exports match module publics (spot-check); no module imports violating layer rules (viz test exists — run it).
3. compute/ drivers: each of the 3 accepts its documented CLI (run --help); CONTRACT compliance spot-check (checkpointing field names, host fingerprint, status values); the known UX trap "default params = smoke run" — is it WARNED about in compute/README.md and --help epilogs? The ds_cap_4d driver SKIPS cells above --n-max instead of falling back to sparse for S_full (dense-bound channel) — verify this limitation is DOCUMENTED honestly in the module docstring (it should be after round-12; flag if not).
4. .github/workflows: 4 yaml files parse (python3 -c yaml); repro.yml — the special-case branch treating the 4 'new dirs' (ds-entropy-cap, ds-tracial-probe, modular-flow-codim2, sj-desitter-4d) as exit-5 'skipped' is OBSOLETE now they are in SLOW_CALCS (test_reproduction.py) — check and flag; ci.yml uses requirements-ci.txt and pins match app/requirements.txt for the compute stack.
5. docker: docker compose config -q in app/ (if docker available); requirements pins consistent across requirements.txt/requirements-ci.txt.
6. web: python3 web/build.py runs clean; page count reported; test_web_build passes (covered by suite).
Do NOT fix anything (except nothing). Return findings + checksPassed.`,
    { label: 'audit:infra', phase: 'Audity', model: 'opus', schema: AUDIT }),

  // ---- 4: process lessons -> encoded guards ----
  () => agent(`You are a process auditor at ${ROOT}. Czech findings. The project accumulated operational lessons that must be ENCODED IN THE REPO (tests/docs/contracts), not live in session memory. Lessons list:
(a) ABSOLUTE PATHS: machine-absolute paths (/Users/...) in calc.py/compute/lib code broke CI twice (OUTDIR batch + lib imports batch).
(b) Driver defaults are smoke configs — full runs need explicit args.
(c) calc.py sandbox/reproduction needs: run-order dependencies (sj-far-zone<-sj-threshold-scan, modular-flow-bd-4d<-modular-flow-corner, modular-flow-codim2<-modular-flow-bd-4d, ds-entropy-cap<-ssee-diamond), PYTHONPATH for lib/toe calcs.
(d) Cross-platform tolerance philosophy: noise floor 1e-10, core <10%, diagnostics <500%, documented-pathological sections excluded (area_law_imposed_rank).
(e) Workflow-agent hygiene: agents must get __file__-relative path instructions for portable code; agents writing results must use schema (clean fail on session limit).
YOUR TASKS:
1. WRITE the guard test ${ROOT}/app/tests/test_portability_guards.py: (i) NO machine-absolute path string (regex /Users/ or /home/<user>) in any *.py under core-data/calculations/, compute/, lib/, web/ (allow comments? NO — forbid everywhere in those .py files) and none in app/tests; (ii) every compute/drivers/*.py contains the string '--max-hours' and 'smoke' in its --help epilog source; (iii) every calc dir with results.json has a writeup match (glob knowledge-base/vypocty/VYPOCET-*); keep it < 5 s, pure filesystem checks. RUN it; it must PASS against the current tree (if it fails, the failures are real findings — report them, fix trivial ones like stray comments yourself ONLY if mechanical).
2. CHECK each lesson (a)-(e) has a durable home: CLAUDE.md conventions section, REVIZE §4.3, compute/README, ARCHITECTURE.md. Report which lessons are NOT yet written down anywhere durable and propose exact wording (Czech for CLAUDE.md).
3. Inventory workflows/review-prep/ and /tmp dependencies: anything the next research day needs that lives only in /tmp (artifacts analyses)? Flag.
Return findings + checksPassed + filesWritten.`,
    { label: 'audit:process', phase: 'Audity', model: 'opus', schema: AUDIT }),
])

const labels = ['deliverables', 'data-pipeline', 'infra', 'process']
const all = audits.map((a, i) => a || { area: labels[i], findings: [{ severity: 'major', what: 'audit agent failed', where: labels[i], suggestedFix: 'rerun', safeToAutofix: false }], checksPassed: [], filesWritten: [] })
const flat = all.flatMap(a => a.findings.map(f => ({ ...f, area: a.area })))
const autofixable = flat.filter(f => f.safeToAutofix && (f.severity === 'blocker' || f.severity === 'major' || f.severity === 'minor'))
log('Audity hotové: ' + flat.length + ' nálezů (' + flat.filter(f => f.severity === 'blocker').length + ' blocker, ' + flat.filter(f => f.severity === 'major').length + ' major), ' + autofixable.length + ' safe-to-autofix.')

phase('Opravy')
let fixes = null
if (autofixable.length > 0) {
  fixes = await agent(`You are the backoffice fixer at ${ROOT}. Czech notes. Apply ONLY these safe-to-autofix findings from the audit (do exactly the suggestedFix, nothing more adventurous):
${JSON.stringify(autofixable, null, 1)}
After fixing: cd ${ROOT} && MPLBACKEND=Agg python3 -m pytest app/tests -q must stay green (report tally). Do not weaken any test. Return file + keyPoints.`,
    { label: 'fix:backoffice', phase: 'Opravy', model: 'sonnet', schema: NOTE })
} else {
  log('Žádné safe-to-autofix nálezy.')
}

phase('Syntéza')
const synthesis = await agent(`You are the audit-synthesis agent at ${ROOT}. Today ${DATE}. Czech prose / English data.
AUDIT RESULTS (4 areas):
${JSON.stringify(all.map(a => ({ area: a.area, findings: a.findings, checksPassed: a.checksPassed, filesWritten: a.filesWritten })), null, 1)}
FIXES APPLIED: ${fixes ? JSON.stringify(fixes.keyPoints) : 'none needed'}

TASKS:
1. Write ${ROOT}/reports/2026-06-07-backoffice-audit.md IN CZECH: (a) executive summary — je backoffice připravená na další den výzkumu? (verdikt + top rizika); (b) tabulka nálezů podle oblasti a závažnosti (co opraveno hned / co je doporučení); (c) stav qg-knowledge-foundation deliverables (odpověď na původní otázku uživatele — co přesně chybělo/nechybělo); (d) zakódovaná poučení (guard testy, dokumentace) vs. zbývající; (e) doporučený checklist pro start dalšího výzkumného dne.
2. Update ${ROOT}/CLAUDE.md: add/extend a "## Provozní konvence (naučené)" section with the durable lessons the process auditor proposed (portability rule — žádné absolutní cesty v portovatelném kódu, __file__-relativní bootstrap; driver defaults = smoke; pořadí reprodukce + PYTHONPATH; tolerance filozofie; schema povinné pro workflow agenty). Keep CLAUDE.md concise — bullet points, not essays.
3. Update ${ROOT}/PROGRESS.md (Read first): log entry backoffice audit + one-line banner addition.
4. Rebuild web: python3 ${ROOT}/web/build.py (report pages). Then git add -A && git -c user.name=pazny -c user.email=pazny.develop@gmail.com commit -m "Backoffice audit: findings, guard tests, encoded conventions" with Co-Authored-By: Claude Opus 4.8 (1M context) <noreply@anthropic.com> as last line. Do NOT push.
Return file + keyPoints (Czech, include the verdict + commit hash).`,
  { label: 'final:audit-synthesis', phase: 'Syntéza', model: 'opus', schema: NOTE })

return {
  findings: flat,
  checksPassed: all.flatMap(a => a.checksPassed.map(c => a.area + ': ' + c)),
  fixes: fixes,
  synthesis: synthesis,
}
