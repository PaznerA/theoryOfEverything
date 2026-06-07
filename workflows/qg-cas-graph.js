export const meta = {
  name: 'qg-cas-graph',
  description: 'Lane W: Wolfram Language nezávislá CAS validace symbolických výsledků (a₄/−18/11, d_s, Λ ledger) připravená k aktivaci; Lane G: link prediction nad grafem konceptů (numpy/scipy) + interaktivní vizualizace grafu na webu',
  phases: [
    { title: 'Stavba', detail: 'lane W (CAS validace) + lane G (graf: predikce + vizualizace) paralelně', model: 'opus' },
    { title: 'Úklid', detail: 'PROGRESS, INDEX, testy, web rebuild, commit+push', model: 'sonnet' },
  ],
}

const ROOT = '/Users/pazny/projects/theoryOfEverything'
const DATE = (args && args.date) || '2026-06-07'

const RESULT = {
  type: 'object',
  properties: {
    status: { type: 'string', description: 'success | partial | failed' },
    keyPoints: { type: 'array', items: { type: 'string' }, description: 'Czech' },
    testsTally: { type: 'string' },
    files: { type: 'array', items: { type: 'string' } },
  },
  required: ['status', 'keyPoints', 'testsTally', 'files'],
}

phase('Stavba')
log('Lane W (Wolfram CAS validace) + Lane G (link prediction + graf vizualizace)…')

const batch = await parallel([
  // ---------- Lane W: Wolfram CAS validation ----------
  () => agent(`You are a symbolic-physics validation engineer at ${ROOT}. GOAL: an INDEPENDENT cross-CAS validation lane for the project's exact symbolic results — "cross-HW for symbolics": the same physics re-derived in Wolfram Language from the PUBLISHED coefficients (not transcribed from our sympy outputs), so agreement is evidence, disagreement is a bug in one of the two derivations. wolframscript is NOT installed on this machine — you cannot execute the scripts; therefore write them with EXTREME syntactic care using only basic, canonical WL constructs (Rational, exact integers, Together, Simplify-free arithmetic where possible, Association, Export JSON). Code+comments ENGLISH; READMEs Czech.

READ FIRST (the claims to validate + their sympy derivations): ${ROOT}/core-data/calculations/a4-anomaly-matching/calc.py (+ results.json), a4-graviton-index/calc.py, lambda-induced/calc.py, ds-classification/calc.py (+ results.json master table), papers/draft-02-a4-fermionic-identity/draft.md (the exact claims + published coefficient sources: Duff 2003.02688 Table 1, Vassilevich hep-th/0306138 eq 4.28, Chamseddine-Connes hep-th/9606001 eq 2.24).

WRITE ${ROOT}/verification/cas/:
1. a4_identity.wl — from the PUBLISHED per-field (a,c) trace-anomaly coefficients (real scalar (1/360,1/120)... use the exact convention draft-02 cites; define them as the literature values with a comment per source), derive: cOverMinusA for one Weyl fermion == -18/11 EXACTLY (Rational arithmetic); Dirac = 2x Weyl same ratio; the three-route consistency draft-02 claims (CC alpha0/tau0 route vs single-Weyl vs Dirac); SM fermion content check; conformal-graviton ratio == -398/261 (and != -18/11); STr(1) counts nB-nF = -62 (no nuR) / -68 (with nuR) from the SM multiplet table. Output: Export["a4_identity_result.json", Association[...]] with each check as True/False + the exact rationals as strings.
2. ds_classifier.wl — the d_s master values: isotropic d_s = D/gamma cases and Horava d_s = 1 + D_space/z rows from ds-classification/results.json master table (validate the ~6 exact rational entries incl. z=3,Dspace=3 -> 2 and z=2 -> 5/2; mind the D vs D_space convention note from draft-03 — read it). Same JSON output pattern.
3. lambda_ledger.wl — the Lambda-induction ledger structure from VYPOCET-17: a0 and a2 both linear in N=Tr(1_F); the a0:a2 ratio carries (f4/f2)*Lambda^2 (dimension/scheme-dependent) while the intra-a4 ratio is cutoff-order-clean; Lambda_cc/m_Pl^2 == pi^2 f4 / (2 N f2^2 khat^2) carries explicit 1/N. Validate symbolically with formal symbols f0,f2,f4,N,khat (define via formal Symbol arithmetic; check structural facts like FreeQ of the intra-a4 ratio from Lambda etc.). JSON output.
4. run_all.py — python runner: for each .wl, subprocess wolframscript -file <f>, collect the JSONs into verification/cas/results.json with overall pass/fail; graceful error if wolframscript missing (exit code 2 + message). Must run from any cwd (__file__-relative paths — project portability convention!).
5. ${ROOT}/app/tests/test_cas_validation.py — pytest: @pytest.mark.skipif(shutil.which("wolframscript") is None, reason="Wolfram Engine not installed — see verification/cas/README.md"); when present: run run_all.py, assert overall pass and the -18/11 check True. Also one ALWAYS-running test: the .wl files exist and contain no machine-absolute paths.
6. ${ROOT}/verification/cas/README.md IN CZECH: proč nezávislá CAS validace (symbolický ekvivalent cross-HW), co každý skript ověřuje a proti jakým publikovaným zdrojům, instalace: brew install --cask wolfram-engine, pak JEDNORÁZOVĚ interaktivně wolframscript -activate (vyžaduje Wolfram ID — doporuč uživateli spustit '! wolframscript -activate' přímo v session), pak python3 verification/cas/run_all.py; vazba na REVIZE-PRO-CLOVEKA (přidej do REVIZE draft-02 sekce jeden checkbox: nezávislá CAS validace připravena — spustit po instalaci Wolfram Engine).
RUN what you can: python syntax of run_all.py + the pytest file (pytest must pass with the skip on this machine): cd ${ROOT} && MPLBACKEND=Agg python3 -m pytest app/tests/test_cas_validation.py -v. Return status, keyPoints (Czech), testsTally, files.`,
    { label: 'lane:wolfram-cas', phase: 'Stavba', model: 'opus', schema: RESULT }),

  // ---------- Lane G: link prediction + graph viz ----------
  () => agent(`You are a graph-ML + visualization engineer at ${ROOT}. Two deliverables over the concept graph (core-data/concept-graph.json: ~626 nodes, ~2481 edges; core-data/connections.json: 292 cross-pillar connections with explored ratings). CONSTRAINT: NO new python dependencies (numpy/scipy only — no networkx, no torch); web stays no-build-chain (CDN libs only, like the existing KaTeX pattern). Code ENGLISH, reports Czech. The project mission: AI hunting for yet-undiscovered connections — link prediction IS the mission as an ML task, and the user wants the graph VISUALIZED on the web.

PART 1 — ${ROOT}/lib/kgraph/ mini-package (separate from toe — knowledge infra, not physics):
- loader.py: load concept-graph.json -> adjacency (undirected, weighted by edge multiplicity), node metadata (pillars, definition).
- scores.py: classical link-prediction heuristics implemented directly (common neighbors, Jaccard, Adamic-Adar, resource allocation, preferential attachment) + spectral embedding (normalized Laplacian, scipy.sparse.linalg.eigsh, d=32 dims) with cosine similarity; ensemble = rank-average of the individual scores.
- evaluate.py: leave-k-out evaluation (hide 10% random existing edges, score all candidate pairs, report AUC + precision@50) — the honesty check that the scorer beats chance; seeded rng.
- predict.py: rank NON-edges; boost/flag cross-pillar pairs (nodes whose pillar sets are disjoint) — those are the hunting-zone candidates; for each top candidate output an EXPLANATION (which common neighbors / similar embeddings drove it).
- app/tests/test_kgraph.py: tiny synthetic graph sanity (a planted-partition toy: AUC > 0.8 on held-out edges; heuristics agree on an obvious triangle-completion), runtime < 30 s.
PART 2 — RUN it on the real graph: leave-10%-out AUC (report it honestly — if near 0.5, say so), then full ranking; write core-data/link-predictions.json (EN: generated date ${DATE}, method, auc, top 50 candidates with scores+explanations+crossPillar flag) and reports/2026-06-07-link-prediction.md IN CZECH: metodika, AUC, top ~15 kandidátů s komentářem (kteří jsou fyzikálně zajímaví vs. trivialní artefakty hubů — be critical), jak s tím naloží příští brainstorm (kandidáti jsou NÁVRHY — do fragmentů je smí propsat až redakční/výzkumné rozhodnutí, provenance policy).
PART 3 — web visualization: extend ${ROOT}/web/build.py + templates to emit (a) dist/assets/graph-data.json (nodes: id, name, degree, pillars, group-color key; edges: from, to, type, explored; PLUS the top-50 predicted candidate edges marked predicted:true) and (b) /data/graph.html — interactive force-directed view via the force-graph CDN library (unpkg, canvas renderer; same CDN pattern as KaTeX): node size ~ degree, color by primary pillar, edge style by explored (well=solid, partially=dashed, barely=dotted, predicted=distinct color), controls: search box, pillar filter, explored-rating toggles, predicted-edges toggle; click node -> side panel (name, definition, pillars, top links). Add the page to the sidebar (Data section). Extend app/tests/test_web_build.py with asserts: graph.html exists, graph-data.json node count == concept-graph.json nodes count, page references the CDN lib + the data file. Keep the page self-contained and working from file:// AND under a subpath (relative links only).
RUN: full pytest (cd ${ROOT} && MPLBACKEND=Agg python3 -m pytest app/tests -q) + python3 web/build.py (report pages count). Return status, keyPoints (Czech, include the real AUC + 3 nejzajímavější kandidáti), testsTally, files.`,
    { label: 'lane:graph', phase: 'Stavba', model: 'opus', schema: RESULT }),
])

const w = batch[0]
const g = batch[1]
log('Stavba hotova (W: ' + (w ? w.status : 'N/A') + ', G: ' + (g ? g.status : 'N/A') + '). Úklid…')

phase('Úklid')
const hk = await agent(`You are the housekeeping agent at ${ROOT}. Today ${DATE}. Czech prose / English data. ECONOMY MODE. Results:
${JSON.stringify({ wolfram: w ? { status: w.status, keyPoints: w.keyPoints } : null, graph: g ? { status: g.status, keyPoints: g.keyPoints } : null }, null, 1)}

TASK 1: Verify full suite: cd ${ROOT} && MPLBACKEND=Agg python3 -m pytest app/tests -q (report tally; CAS tests must SKIP gracefully on this machine).
TASK 2: Rebuild web: python3 ${ROOT}/web/build.py (report pages; the graph page must be in the build).
TASK 3: Update ${ROOT}/PROGRESS.md (Read first): log entry (CAS validace připravena k aktivaci + link prediction AUC + graf vizualizace na webu); banner one-liner.
TASK 4: Update ${ROOT}/knowledge-base/00-INDEX.md: verification/cas/ + lib/kgraph + reports/2026-06-07-link-prediction.md + core-data/link-predictions.json + odkaz na /data/graph.html vizualizaci.
TASK 5: git add -A && git -c user.name=pazny -c user.email=pazny.develop@gmail.com commit (concise message: CAS validation lane + concept-graph link prediction + web graph viz) with Co-Authored-By: Claude Opus 4.8 (1M context) <noreply@anthropic.com> last line, then git push.
Return 4-line Czech confirmation incl. commit hash.`,
  { label: 'final:cas-graph', phase: 'Úklid', model: 'sonnet' })

return { wolfram: w, graph: g, housekeeping: hk }
