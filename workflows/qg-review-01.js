export const meta = {
  name: 'qg-review-01',
  description: 'Velké review 1: verifikace 150 arXiv ID proti arxiv.org, audit findings.json, opravy draftů (a_err, draft-03), doplnění vN vazeb do grafu, opravy referencí, syntéza',
  phases: [
    { title: 'Verifikace + audity', detail: '10 batchů arXiv ID (export API) + 4 audit agenti paralelně' },
    { title: 'Opravy referencí', detail: 'fan-out podle vadných ID', model: 'sonnet' },
    { title: 'Syntéza', detail: 'consolidate.py + review report + PROGRESS', model: 'sonnet' },
  ],
}

const ROOT = '/Users/pazny/projects/theoryOfEverything'
const CD = ROOT + '/core-data'
const KB = ROOT + '/knowledge-base'
const WL = ROOT + '/workflows/review-prep/verify-worklist.json'
const DATE = (args && args.date) || '2026-06-06'

// ---------- schemas ----------
const VERIFY = {
  type: 'object',
  properties: {
    results: {
      type: 'array',
      items: {
        type: 'object',
        properties: {
          id: { type: 'string' },
          verdict: { type: 'string', description: 'ok | mismatch | not-found | ambiguous' },
          claimedTitle: { type: 'string' },
          actualTitle: { type: 'string', description: 'title returned by arxiv.org, or "" if not found' },
          note: { type: 'string' },
        },
        required: ['id', 'verdict', 'claimedTitle', 'actualTitle', 'note'],
      },
    },
  },
  required: ['results'],
}

const AUDIT = {
  type: 'object',
  properties: {
    changes: {
      type: 'array',
      items: {
        type: 'object',
        properties: {
          finding: { type: 'string' },
          change: { type: 'string' },
          reason: { type: 'string' },
        },
        required: ['finding', 'change', 'reason'],
      },
    },
    unchanged: { type: 'number' },
    notes: { type: 'string' },
  },
  required: ['changes', 'unchanged', 'notes'],
}

const NOTE = {
  type: 'object',
  properties: {
    file: { type: 'string' },
    keyPoints: { type: 'array', items: { type: 'string' }, description: 'Czech' },
  },
  required: ['file', 'keyPoints'],
}

const FIXCALC = {
  type: 'object',
  properties: {
    status: { type: 'string', description: 'success | partial | failed' },
    keyNumbers: { type: 'string' },
    filesEdited: { type: 'array', items: { type: 'string' } },
    verdict: { type: 'string', description: 'Czech, 2-3 sentences' },
  },
  required: ['status', 'keyNumbers', 'filesEdited', 'verdict'],
}

const GRAPH = {
  type: 'object',
  properties: {
    addedConnections: { type: 'array', items: { type: 'string' } },
    addedConcepts: { type: 'array', items: { type: 'string' } },
    notes: { type: 'string' },
  },
  required: ['addedConnections', 'addedConcepts', 'notes'],
}

const FIXES = {
  type: 'object',
  properties: {
    fixes: {
      type: 'array',
      items: {
        type: 'object',
        properties: {
          id: { type: 'string' },
          action: { type: 'string', description: 'replaced-id | fixed-title | marked-unverified | removed | kept-ok | other' },
          newId: { type: 'string', description: 'replacement arXiv ID if any, else ""' },
          note: { type: 'string' },
          filesEdited: { type: 'array', items: { type: 'string' } },
        },
        required: ['id', 'action', 'newId', 'note', 'filesEdited'],
      },
    },
  },
  required: ['fixes'],
}

// ---------- phase 1: verification batches + audits in one parallel ----------
phase('Verifikace + audity')
log('Spouštím 10 verifikačních batchů + 4 audity (findings, draft-03, a_err, graf)…')

const batchDefs = []
for (let s = 0; s < 120; s += 15) batchDefs.push({ key: 'recent', start: s, end: Math.min(s + 15, 120) })
for (let s = 0; s < 30; s += 15) batchDefs.push({ key: 'sample_old', start: s, end: Math.min(s + 15, 30) })

function verifyPrompt(b) {
  return `You are a reference-verification agent (ECONOMY MODE) at ${ROOT}. STRICT project policy: never invent arXiv IDs; unverifiable references get flagged.

Read ${WL}. Take items of array "${b.key}" at 0-based indices ${b.start}..${b.end - 1} (inclusive). Each item: {id, claimed:{title,authors,year}|null, files, n_files}.

VERIFY against arXiv: first ToolSearch "select:WebFetch". Then ONE call: WebFetch http://export.arxiv.org/api/query?id_list=<comma-separated ids of your batch>&max_results=25 with prompt "List for each entry: the arXiv id, exact title, authors, year". The Atom feed has one entry per existing ID; non-existent IDs are absent or yield an error entry. For any ID that is absent/unclear, do a fallback WebFetch of https://arxiv.org/abs/<id> before concluding not-found.

For each item decide:
- ok — ID exists and title/authors are consistent with item.claimed (minor formatting/casing/abbreviation differences are fine). If claimed is null, Read or Grep ONE of item.files around the ID occurrence to learn what we cite it as, then compare with that context.
- mismatch — ID exists but it is a DIFFERENT paper than what we claim (report actualTitle).
- not-found — ID does not exist on arXiv (after fallback check).
- ambiguous — cannot decide; explain in note.

Do NOT edit any project files. Return ALL ${b.end - b.start} items in results.`
}

const thunks = batchDefs.map(b => () =>
  agent(verifyPrompt(b), { label: 'verify:' + b.key + ':' + b.start, phase: 'Verifikace + audity', model: 'sonnet', schema: VERIFY }))

// audit A: findings.json honesty audit
thunks.push(() => agent(`You are the findings auditor at ${ROOT}. Czech prose values stay Czech, English data stays English. Audit ${CD}/findings.json (24 findings F-001..F-024) for STATUS-LANGUAGE HONESTY.

Known weak points (from BRAINSTORM-05 review recommendations — verify each, do not assume):
- Proxy 3 (central sequences / self-averaging) is statistically insignificant at 5-8 seeds across VYPOCET-12/16/19 — any finding counting it as passed must read 2/3, not 3/3; status language must not overstate.
- N^(3/4) truncation is a PRESCRIPTION (observer/crossed-product cutoff), not a discovered spectral feature — wording must not imply the spectrum selects it.
- F-006: p=1/2 significance is only ~2.8 sigma — status should reflect that.
- F-024: verdict rests on the SIGN of a slope contrast, not its value (R^2=0.56) — wording must say partial/sign-level.
- F-023: 'supported', not 'confirmed' (Part-3 tracial probe is an honest null).

PROCEDURE: for EVERY finding F-001..F-024: (1) read its evidence writeup in ${KB}/vypocty/ (status fields, caveats); (2) check the finding's status ('confirmed'/'supported'/'partial'/'refuted') is warranted by the recorded statistics; downgrade wording where not (confirmed->supported, supported->partial) — NEVER upgrade; (3) ensure a caveats field faithfully lists the main limitation(s); (4) verify the evidence file paths exist (ls/Glob). Edit ${CD}/findings.json in place (valid JSON!). Do NOT alter numbers, do NOT delete findings. Return every change made + count of findings left unchanged.`,
  { label: 'audit:findings', phase: 'Verifikace + audity', model: 'opus', schema: AUDIT }))

// audit B: draft-03 labels + conventions
thunks.push(() => agent(`You are a draft auditor (ECONOMY MODE) at ${ROOT}. Target: ${ROOT}/papers/draft-03-ds-classifier/ (draft.md + TODO.md).
TASK 1: The illustrative value 8 for the CST random-walk spectral dimension is NOT from a paper (not from Eichhorn-Mizera 1311.2530). Find every occurrence in draft.md; ensure each is unambiguously labeled as illustrative/qualitative (e.g. footnote "illustrative value, not from literature") so it cannot be read as a quantitative claim. Fix labels where missing.
TASK 2: Per-row audit of the master table's dimension conventions: D vs D_space ambiguity, especially the Horava row (d_s = 1 + D/z holds with D = number of SPATIAL dimensions in D+1 anisotropic scaling). Check each row's (z, D) entry states which convention it uses; add a single table-wide convention note if absent; fix inconsistent rows.
TASK 3: Update TODO.md: mark what you fixed (dated ${DATE}), keep remaining human-verification items.
English draft text stays English; TODO notes bilingual as in the existing file. Return file + keyPoints (Czech).`,
  { label: 'audit:draft-03', phase: 'Verifikace + audity', model: 'sonnet', schema: NOTE }))

// audit C: a_err placeholder fix (computation)
thunks.push(() => agent(`You are a computational physics agent at ${ROOT}. Environment: python3 + numpy/scipy. NEVER fudge results.
DEFECT TO FIX: ${CD}/calculations/sj-vn-type/results.json contains the placeholder uncertainty 0.775853511479044 copied across multiple fields (lines ~56, ~79, ~205, ~341, ~343 — grep for "0.775853"). Per ${ROOT}/papers/draft-04-type-transition-causal-sets/TODO.md (line ~83) it is a seed-spread placeholder, NOT a per-fit standard error — so the corresponding "+/-" values in draft-04 are currently not meaningful.
TASK: (1) Read ${CD}/calculations/sj-vn-type/calc.py + results.json; identify which exponent fits the placeholder fields belong to. (2) Recompute PROPER uncertainties for each affected exponent: (a) the regression standard error of the log-log fit slope, and (b) an across-seed bootstrap CI (>=1000 resamples) — if per-seed/per-N data needed for this is not stored in results.json, write calc_uncertainty.py in the same dir (minimal re-run of just the needed pipeline pieces with the SAME seeds/parameters as calc.py; set OMP_NUM_THREADS=4; runtime budget ~10 min) and run it. (3) REPLACE each placeholder with the real values (two fields: *_se_regression, *_ci68_bootstrap; keep JSON valid) — DO NOT change any central values. (4) Update the corresponding +/- numbers in draft-04 draft.md, and replace the TODO.md line-83 defect note with a dated resolution note (${DATE}). (5) Update the matching checkbox in ${ROOT}/papers/REVIZE-PRO-CLOVEKA.md (mark resolved, one-line note). Return status, key numbers (old placeholder -> new SE/CI per exponent), files edited, Czech verdict.`,
  { label: 'fix:a-err', phase: 'Verifikace + audity', model: 'opus', schema: FIXCALC }))

// audit D: concept graph / connections completion
thunks.push(() => agent(`You are the knowledge-graph curator at ${ROOT}. STRICT: English data/IDs; never invent arXiv IDs (only ones already present in the repo).
PROBLEM (from BRAINSTORM-05): ${CD}/connections.json has 288 cross-approach connections but ZERO involving von-neumann-algebras — although the project's own findings F-015/F-019/F-023 establish vNA<->causal-sets links by data. The registries are GENERATED by ${ROOT}/workflows/consolidate.py from ${CD}/fragments/*.json — so fixes belong in FRAGMENTS, not in connections.json directly.
TASK: (1) Read workflows/consolidate.py enough to learn the exact fragment schema for connections (and concepts). (2) Read ${CD}/fragments/von-neumann-algebras.json + causal-sets.json. (3) ADD to the appropriate fragment(s), following the existing schema exactly:
- von-neumann-algebras <-> causal-sets (evidence: project findings F-015/F-019/F-023 — SSEE truncation realizes III1->II transition; explored: partially);
- von-neumann-algebras <-> holography-adscft (CPW crossed product, arXiv:2209.10454; explored: partially);
- von-neumann-algebras <-> quantum-cosmology (CLPW dS static patch II1, arXiv:2206.10780 + our F-023; explored: partially);
- causal-sets <-> noncommutative-geometry (shared spectral-reconstruction math: Dirac operator/spectral triple vs Pauli-Jordan/SJ modular Hamiltonian — H5g-4 hunting zone; explored: barely);
- black-holes-information <-> causal-sets (entropy cap vs horizon area A/4 — H5g-2 bridge; explored: barely).
(4) Check concept NODES exist in fragments for: sorkin-johnston-state, benincasa-dowker-operator, modular-hamiltonian/modular-flow, crossed-product, type-iii-factor / type-ii-factor, ssee. Add missing ones as concepts per schema (with latex where natural). (5) Do NOT run consolidate.py (synthesis step does). Return added connections + concepts + notes.`,
  { label: 'graph:vna-links', phase: 'Verifikace + audity', model: 'opus', schema: GRAPH }))

const all = await parallel(thunks)
const nB = batchDefs.length
const verifyRes = all.slice(0, nB).filter(Boolean).flatMap(r => r.results)
const findingsAudit = all[nB]
const draft03 = all[nB + 1]
const aerr = all[nB + 2]
const graph = all[nB + 3]

const bad = verifyRes.filter(r => r.verdict !== 'ok')
log('Verifikace: ' + verifyRes.length + ' ID zkontrolováno, problémových ' + bad.length + '. Audity: findings ' + (findingsAudit ? findingsAudit.changes.length + ' změn' : 'N/A') + ', a_err ' + (aerr ? aerr.status : 'N/A') + ', graf +' + (graph ? graph.addedConnections.length : 0) + ' vazeb.')

// ---------- phase 2: fix bad references ----------
phase('Opravy referencí')
let fixes = []
if (bad.length > 0) {
  const chunks = []
  for (let i = 0; i < bad.length; i += 5) chunks.push(bad.slice(i, i + 5))
  const fixResults = await parallel(chunks.map((chunk, ci) => () =>
    agent(`You are a reference-fixing agent at ${ROOT}. STRICT policy: never invent arXiv IDs — a replacement ID may ONLY come from an arxiv.org API/abs response you fetched yourself. Registries (references.json, .bib, connections.json, concept-graph.json) are GENERATED from ${CD}/fragments/*.json by workflows/consolidate.py — durable fixes go into FRAGMENTS and prose/calc files; do NOT edit the generated registries (a later step regenerates them).

PROBLEM REFERENCES (verdicts from verification against arxiv.org):
${JSON.stringify(chunk, null, 1)}

For EACH problem ID:
1. Grep the WHOLE repo for the ID (Grep tool, all file types) to find every occurrence.
2. Determine the INTENDED paper from the claimed title/context. ToolSearch "select:WebFetch" then search arXiv: WebFetch http://export.arxiv.org/api/query?search_query=ti:%22<url-encoded claimed title>%22&max_results=5 (or all:%22...%22 with author surname).
3. Decide:
   - Found the real paper (title+authors match the claim) -> action replaced-id: replace the wrong ID with the real ID in ALL occurrences (fragments, knowledge-base prose, verification/, calc.py comments, papers drafts). Keep claimed metadata, correct year if needed.
   - verdict was mismatch and the claimed metadata is what is wrong (the ID's actual paper IS plausibly what the context intends) -> action fixed-title: correct title/authors in fragments to the actual paper.
   - Cannot find/verify -> per project policy: in fragments either REMOVE the reference entry (if it is load-bearing nowhere) or set its arxiv field to null and append " [unverified arXiv ID removed ${DATE}]" to its significance/note field; in Czech prose mark the citation with "⚠️ neověřeno"; in calc.py comments append "(arXiv ID unverified)". action marked-unverified or removed.
   - ambiguous verdicts: investigate deeper (fallback https://arxiv.org/abs/<id>); if still undecidable, marked-unverified (never delete silently).
4. NEVER touch the numeric content of findings/calculations.
Return one fixes entry per ID with files edited.`,
      { label: 'fix:refs:' + ci, phase: 'Opravy referencí', model: 'sonnet', schema: FIXES })))
  fixes = fixResults.filter(Boolean).flatMap(r => r.fixes)
} else {
  log('Žádné vadné reference — přeskakuji opravnou fázi.')
}

// ---------- phase 3: synthesis ----------
phase('Syntéza')

const summary = {
  verification: {
    checked: verifyRes.length,
    ok: verifyRes.filter(r => r.verdict === 'ok').length,
    bad: bad.map(b => ({ id: b.id, verdict: b.verdict, note: b.note })),
  },
  fixes: fixes,
  findingsAudit: findingsAudit,
  draft03: draft03,
  aerr: aerr ? { status: aerr.status, keyNumbers: aerr.keyNumbers, verdict: aerr.verdict } : null,
  graph: graph,
}

const synthesis = await agent(`You are the review-synthesis agent at ${ROOT}. Today ${DATE}. Czech prose / English data. ECONOMY MODE.

REVIEW RESULTS (phase 1+2 of the big review):
${JSON.stringify(summary, null, 1)}

TASKS, in order:
1. Run via Bash: cd ${ROOT} && python3 workflows/consolidate.py — regenerates registries from fragments (references.json, .bib, concept-graph.json, connections.json, _digest.md). Capture the printed stats. Then verify with Grep that connections.json now contains von-neumann-algebras edges; report new totals (nodes/edges/references/connections + how many barely).
2. Write ${ROOT}/reports/2026-06-06-review.md IN CZECH — report of the big review, part 1: sections (a) rozsah review (co bylo kontrolováno a proč — 150/652 arXiv ID: všech 120 z 2024+, vzorek 30 starších; audit findings; opravy draftů; doplnění grafu); (b) verifikace referencí — statistika, tabulka problémových ID a co se s nimi stalo; (c) audit findings.json — tabulka změn statusů s důvody; (d) opravy draftů (a_err rekonstrukce nejistot, draft-03 konvence); (e) doplnění grafu konceptů (nové vazby vč. explored ratingů, nové uzly) + nové statistiky registrů; (f) "Část 2 běží" — deterministická reprodukce všech 20 calc.py běží lokálně (workflows/review-prep/repro-results.json), výsledek bude doplněn; (g) doporučení pro fázi 3 roadmapy (simulace/vizualizace) — co z review plyne pro stavbu kombinovatelných funkcí (např. které výpočty mají nejčistší rozhraní vzorec->kód).
3. Update ${ROOT}/PROGRESS.md (Read first, preserve): top banner -> "Velké review část 1 hotova, část 2 (reprodukce) běží"; add log entry with the same key facts; keep roadmap section.
4. Update ${KB}/00-INDEX.md: add reports/2026-06-06-review.md.
Return: file + keyPoints (Czech) — include the regenerated registry stats.`,
  { label: 'final:review-report', phase: 'Syntéza', model: 'sonnet', schema: NOTE })

return {
  verification: { checked: verifyRes.length, ok: summary.verification.ok, bad: summary.verification.bad },
  fixes: fixes.map(f => ({ id: f.id, action: f.action, newId: f.newId })),
  findingsChanges: findingsAudit ? findingsAudit.changes : null,
  draft03: draft03 ? draft03.keyPoints : null,
  aerr: summary.aerr,
  graph: graph,
  synthesis: synthesis,
}
