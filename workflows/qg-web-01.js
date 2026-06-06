export const meta = {
  name: 'qg-web-01',
  description: 'Krok 4 roadmapy: minimalistický web framework (web/build.py) buildící statický web přímo ze souborové struktury repa (markdown + JSON registry = zdroj pravdy)',
  phases: [
    { title: 'Stavba', detail: 'framework + templates + build + testy', model: 'opus' },
    { title: 'Revize', detail: 'adversariální kontrola buildu (odkazy, math, disclaimery)', model: 'sonnet' },
    { title: 'Opravy', detail: 'fix nálezů revize (jen pokud nějaké jsou)' },
    { title: 'Úklid', detail: 'PROGRESS, INDEX, app/README', model: 'sonnet' },
  ],
}

const ROOT = '/Users/pazny/projects/theoryOfEverything'
const DATE = (args && args.date) || '2026-06-06'

const BUILD_RESULT = {
  type: 'object',
  properties: {
    files: { type: 'array', items: { type: 'string' } },
    pagesBuilt: { type: 'number' },
    testsPassed: { type: 'boolean' },
    pytestTally: { type: 'string' },
    notes: { type: 'string' },
  },
  required: ['files', 'pagesBuilt', 'testsPassed', 'pytestTally', 'notes'],
}

const REVIEW_RESULT = {
  type: 'object',
  properties: {
    issues: {
      type: 'array',
      items: {
        type: 'object',
        properties: {
          severity: { type: 'string', description: 'blocker | major | minor' },
          what: { type: 'string' },
          where: { type: 'string' },
        },
        required: ['severity', 'what', 'where'],
      },
    },
    checksPassed: { type: 'array', items: { type: 'string' } },
    notes: { type: 'string' },
  },
  required: ['issues', 'checksPassed', 'notes'],
}

const NOTE = {
  type: 'object',
  properties: {
    file: { type: 'string' },
    keyPoints: { type: 'array', items: { type: 'string' }, description: 'Czech' },
  },
  required: ['file', 'keyPoints'],
}

// ---------------- phase 1: build ----------------
phase('Stavba')
log('Stavím minimalistický site-builder (web/)…')

const build = await agent(`You are the web-framework builder at ${ROOT}. Roadmap step 4: a MINIMALIST static-site framework that builds a presentation site DIRECTLY from the repo's existing file structure — markdown + JSON registries are the single source of truth; the site is a VIEW, never a copy that can drift. Czech UI prose / English identifiers+code (project policy). Host has python3 + markdown 3.10.2 + jinja2 3.1.6 installed.

HARD CONSTRAINTS (minimalism):
- Pure-python build: ONE entry point web/build.py (+ small modules under web/builder/ if needed), jinja2 templates under web/templates/, one CSS file under web/static/ (clean, readable, light/dark via prefers-color-scheme; no CSS framework). NO node, NO JS build chain. Math: KaTeX via CDN (auto-render for $$...$$ and inline $...$); code highlighting NOT needed (plain <pre>).
- Deterministic output to web/dist/ (delete+rebuild each run). Relative links only — the site must work from file:// AND http.server.
- ABSOLUTE RULE for papers: every page generated from ${ROOT}/papers/** carries a prominent red banner: "⚠️ INTERNÍ AI-ASISTOVANÝ DRAFT — nepodáno, vyžaduje lidskou revizi (viz REVIZE-PRO-CLOVEKA)". The site is local presentation, NOT publication.

CONTENT MAP (build from these sources; routes mirror the file structure):
1. Home (index.html): rendered from README.md + a generated dashboard strip: counts pulled LIVE from core-data registries (26 findings, 652→587 references, 247 formulas, 292 connections incl. barely count, 22 calculations, 4 drafts) + odkazy na klíčové stránky.
2. PROGRESS.md -> /progress.html; reports/*.md -> /reports/...; knowledge-base/**/*.md -> /knowledge-base/... (approaches, cross-cutting, foundations, phenomenology, brainstormy, syntézy, eseje, hypotézy, vypocty — keep the directory tree); papers/*/draft.md + TODO.md + REVIZE-PRO-CLOVEKA.md -> /papers/... (WITH the banner); lib/README.md + lib/toe/ARCHITECTURE.md -> /lib/...; app/README.md -> /app/...
3. JSON registry pages (generated, not hand-written): /data/findings.html — table of all findings from core-data/findings.json (id, status badge with color, statement, evidence links, caveats collapsible); /data/connections.html — the connections matrix from connections.json grouped by explored rating (barely first = lovná zóna, with description); /data/formulas.html — formulas.json rendered with KaTeX (id, name, latex, meaning, pillars); /data/open-problems.html — open-problems.json grouped by pillar.
4. Calculations gallery: /calculations.html — one card per core-data/calculations/* dir: name, headline numbers (pull a few keys from results.json safely), links to plots (PNG copied into dist/assets/), link to the matching VYPOCET writeup page.
5. Navigation: a single sidebar (generated from the content map) + breadcrumbs; markdown internal links between repo files rewritten to the corresponding .html routes (best-effort; leave external links untouched; arXiv ids auto-linked to arxiv.org/abs/).

IMPLEMENTATION NOTES: python-markdown with extensions ['extra', 'toc', 'tables']; protect $...$/$$...$$ from markdown mangling (e.g. a pre/post placeholder pass) so KaTeX gets clean delimiters; UTF-8 everywhere (Czech diacritics); skip dirs: workflows/, web/, app/ internals except README, core-data/fragments (registries suffice), .git-like noise.

TESTS: write ${ROOT}/app/tests/test_web_build.py — builds the site into a tmp dir (build.py must accept --out), asserts: >=80 pages built; index/progress/findings/formulas/calculations pages exist; every generated paper page contains the banner string; a sample of internal links in index.html and the sidebar resolve to existing files; findings count in findings.html matches findings.json. Runtime < 30 s.
ALSO: add 'markdown>=3.8' and 'jinja2>=3.1' to ${ROOT}/app/requirements.txt (web building inside the container), and update the web service in ${ROOT}/app/docker-compose.yml: command becomes build-then-serve dist (sh -c "python web/build.py && python -m http.server 8080 --directory web/dist") and the volume needs WRITE access (drop :ro) — note the image rebuild requirement in your notes.
RUN: python3 web/build.py (real build into web/dist/ — report page count), then cd ${ROOT} && MPLBACKEND=Agg python3 -m pytest app/tests -q (FULL suite must stay green).
Write a short ${ROOT}/web/README.md IN CZECH (jak buildit, jak servírovat, jak přidat obsah = prostě přidat soubor do repa).
Return files, pagesBuilt, testsPassed, pytestTally, notes.`,
  { label: 'build:web-framework', phase: 'Stavba', model: 'opus', schema: BUILD_RESULT })

log('Build hotov: ' + build.pagesBuilt + ' stránek, testy ' + (build.testsPassed ? 'zelené' : 'ČERVENÉ') + '. Adversariální revize…')

// ---------------- phase 2: adversarial review ----------------
phase('Revize')

const review = await agent(`You are an adversarial reviewer of the freshly built static site at ${ROOT}/web/dist/ (builder: web/build.py; ${build.pagesBuilt} pages). Your job: find what is broken or violates project rules BEFORE the human sees it. Do NOT fix anything — only report.

CHECKS (be concrete, cite file paths):
1. Rebuild from scratch yourself: python3 ${ROOT}/web/build.py — does it run clean and deterministic (run twice, diff page count)?
2. LINK INTEGRITY: sample >=30 internal links across sidebar, index, 5 knowledge-base pages, 2 reports, findings/connections/formulas/calculations pages — every href must resolve to an existing file in dist/ (relative paths). Check plot images in the calculations gallery actually exist in dist/assets/.
3. MATH: pick 3 pages with heavy LaTeX (a vypocty writeup, formulas.html, a paper draft) — verify $$ delimiters survived the markdown pass intact (no mangled \\\\ or escaped $ visible in HTML source) and the KaTeX CDN include is present.
4. POLICY: every page under dist/papers/ carries the red internal-draft banner; Czech prose pages render diacritics correctly (UTF-8 meta); no absolute file:///Users/... or /Users/... links anywhere (grep dist/).
5. DATA FIDELITY: findings.html row count == findings.json entries; connections.html barely-group count == connections.json barely entries; formulas.html count == formulas.json; calculations gallery card count == number of calc dirs with results.json.
6. Sidebar/navigation: every major repo area reachable (reports, brainstormy, vypocty, eseje, papers, data pages, lib); no orphan top-level md (PROGRESS, README) missing.
Return issues (severity blocker/major/minor, what, where) + checksPassed list. Empty issues list ONLY if everything genuinely passes.`,
  { label: 'review:adversarial', phase: 'Revize', model: 'sonnet', schema: REVIEW_RESULT })

// ---------------- phase 3: fixes (conditional) ----------------
phase('Opravy')
const blockers = review.issues.filter(i => i.severity === 'blocker' || i.severity === 'major')
let fixes = null
if (review.issues.length > 0) {
  log('Revize našla ' + review.issues.length + ' problémů (' + blockers.length + ' blocker/major). Opravuji…')
  fixes = await agent(`You are the web-framework fixer at ${ROOT}. The adversarial review of web/ found these issues — fix ALL of them (blockers/major first; minors too unless they conflict with minimalism):
${JSON.stringify(review.issues, null, 1)}

Rules: edit web/build.py / templates / css; keep the minimalist constraints (pure python, relative links, KaTeX CDN, papers banner). After fixing: rebuild (python3 web/build.py), re-run cd ${ROOT} && MPLBACKEND=Agg python3 -m pytest app/tests -q — full suite green. Strengthen test_web_build.py with a regression assert for each blocker-class issue you fixed.
Return files, pagesBuilt, testsPassed, pytestTally, notes.`,
    { label: 'fix:web', phase: 'Opravy', model: 'opus', schema: BUILD_RESULT })
} else {
  log('Revize bez nálezů — opravy přeskočeny.')
}

// ---------------- phase 4: housekeeping ----------------
phase('Úklid')

const hk = await agent(`You are the housekeeping agent at ${ROOT}. Today ${DATE}. Czech prose / English data. ECONOMY MODE.
Round result: roadmap step 4 done — minimalist web framework web/build.py, ${(fixes || build).pagesBuilt} pages in web/dist/, tests ${(fixes || build).pytestTally}; review found ${review.issues.length} issues (${blockers.length} blocker/major), ${fixes ? 'fixed' : 'none needed'}.
TASK 1: Update ${ROOT}/PROGRESS.md (Read first, preserve): banner -> všechny 4 kroky roadmapy mají první verzi hotovou (research ✅, review ✅, lib/toe v0.1.0 ✅, web ✅); roadmap item 4 status line; log entry (web framework: zdroje pravdy, počty stránek, jak spustit: python3 web/build.py + docker compose --profile web up web).
TASK 2: Update ${ROOT}/knowledge-base/00-INDEX.md: Infrastruktura section + web/README.md entry.
TASK 3: Append to ${ROOT}/app/README.md services table note: web service now builds web/dist and serves it (image rebuild needed after requirements change: docker compose build).
Return 3-line Czech confirmation.`,
  { label: 'final:web-housekeeping', phase: 'Úklid', model: 'sonnet' })

return {
  build: { pages: build.pagesBuilt, tests: build.pytestTally },
  review: { issues: review.issues, checksPassed: review.checksPassed },
  fixes: fixes ? { pages: fixes.pagesBuilt, tests: fixes.pytestTally, notes: fixes.notes } : null,
  housekeeping: hk,
}
