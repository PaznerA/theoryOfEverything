export const meta = {
  name: 'qg-gh-compute',
  description: 'GH Actions výpočetní infrastruktura: parametrizované scaled drivery (compute/) nad lib/toe + repro.yml (cross-HW matrix 24 výpočtů) + compute.yml (manuální hodinové běhy); úklid',
  phases: [
    { title: 'Stavba', detail: 'drivery + GH workflows paralelně' },
    { title: 'Úklid', detail: 'README, PROGRESS, testy, commit', model: 'sonnet' },
  ],
}

const ROOT = '/Users/pazny/projects/theoryOfEverything'
const LIB = ROOT + '/lib'
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

// Shared CLI contract so both builders work in parallel against the same interface.
const CONTRACT = `DRIVER CLI CONTRACT (both agents build against this exactly):
compute/drivers/<name>.py with argparse:
  --rho (comma list of densities) / --patch-l (comma list) / --n-max (int cap) as appropriate per driver
  --seeds INT (default 4)
  --max-hours FLOAT (default 5.5) — graceful time budget: finish current cell, finalize, exit 0
  --out DIR (default compute/results) — writes <name>--<paramslug>--<runstamp>/results.json + plots/
Behavior: progressive checkpointing (rewrite results.json after EVERY (rho,l,seed) cell); results.json carries {driver, params, host: {platform, machine, python, numpy/scipy versions}, cells: [...], summary: {...}, status: 'complete'|'partial-time-budget'}; deterministic seeds; OMP_NUM_THREADS respected from env (do not override if set); memory guard: dense path only when N<=3000, sparse (toe v0.3.0) above; assert iDelta +/- pairing invariant per region.
DRIVERS (3):
1. ds_entropy_cap_2d — F-028 extension: tighten R_full constancy (target rho up to 3e4, l up to 2.5, more seeds); reuse the VYPOCET-23 protocol verbatim (anti-circularity: eps fixed from F-006 BEFORE ratio; read core-data/calculations/ds-entropy-cap/calc.py).
2. ds_cap_4d — THE open question (is the area-law coefficient c~7.57 dimension-dependent?): lift the VYPOCET-23 cap-ratio protocol to the 4D dS patch (toe.causet.sprinkle_ds_static_patch4d + sparse path; horizon 'area' = codim-2 surface molecule count in eps^2 units — derive and STATE the 4D discrete-area convention carefully, cite only repo-present refs, '⚠️ neověřeno' where the source is absent).
3. ds4d_saturation — F-025 completion: 4D dS truncated-entropy saturation with sparse path, N up to ~2e4 (the dense-eigh wall at 2500 was the round-10 blocker; sech^2 cap should now be reachable).`

phase('Stavba')
log('Stavím compute drivery + GH Actions workflows…')

const batch = await parallel([
  // --- A: compute drivers ---
  () => agent(`You are a computational-infrastructure builder at ${ROOT}. Code+comments ENGLISH; build ON ${LIB}/toe v0.3.0 (read lib/toe/ARCHITECTURE.md incl. §6 sparse, lib/README.md CHANGELOG; import via sys.path bootstrap relative to __file__ so drivers run from ANY cwd). NEVER fudge numbers.

${CONTRACT}

YOUR JOB: implement the 3 drivers under ${ROOT}/compute/drivers/ + a tiny shared ${ROOT}/compute/drivers/_common.py (arg parsing, host fingerprint, checkpoint writer, time-budget helper). CRITICAL context to read first: core-data/calculations/ds-entropy-cap/calc.py + results.json (VYPOCET-23 protocol: eps from F-006, saturating fits, R_full ratio), knowledge-base/vypocty/VYPOCET-23-ds-entropy-cap.md, sj-desitter-4d/calc.py (4D patch + the conformal-weight caveat wording), VYPOCET-24 writeup section about the (u,v) null-coordinate convention for toe sparse ops (LOAD-BEARING: causal_blocks_2d/idelta_operator_2d take EXPLICIT null coords (u,v)=(t-r*,t+r*), NOT (t,r*) — wrong coords give a silently wrong causal matrix).

REQUIREMENTS: (1) each driver runs a TINY smoke configuration in < 30 s (document the exact smoke invocation in --help epilog); (2) write app/tests/test_compute_drivers.py: for each driver run the smoke invocation via subprocess into a tmp out dir, assert results.json exists, status field present, >=1 cell, pairing invariant recorded, host fingerprint present (total < 90 s); (3) 4D discrete-area convention in ds_cap_4d documented in the module docstring (English) with the honest caveat block; (4) FULL suite green: cd ${ROOT} && MPLBACKEND=Agg python3 -m pytest app/tests -q. Return status, keyPoints (Czech), testsTally, files.`,
    { label: 'build:compute-drivers', phase: 'Stavba', model: 'opus', schema: RESULT }),

  // --- B: GH Actions workflows ---
  () => agent(`You are a CI/CD builder at ${ROOT}. The repo is PUBLIC at https://github.com/PaznerA/theoryOfEverything (Actions free for public repos; ubuntu-latest = 4 vCPU / 16 GB RAM; HARD job limit 360 min — use timeout-minutes: 350; ~20 concurrent jobs). Existing: .github/workflows/ci.yml (fast suite on push) + pages.yml. Pinned env: app/requirements-ci.txt.

${CONTRACT}

BUILD TWO WORKFLOWS:
1. ${ROOT}/.github/workflows/repro.yml — name 'Cross-HW reproduction'. Trigger: workflow_dispatch ONLY, with input 'target' (choice: all | <each of the 24 calc dir names>). Strategy: matrix over the 24 dirs in core-data/calculations/ (list them with Bash ls), fail-fast: false, max-parallel: 20; when target != all, run only the matching dir (use an if: condition on matrix value vs input, or a setup job computing the matrix JSON — choose the cleaner). Each job: checkout, setup-python 3.13 + pip cache, install app/requirements-ci.txt, run FULL_REPRO=1 MPLBACKEND=Agg PYTHONHASHSEED=0 python -m pytest 'app/tests/test_reproduction.py' -k '<dir>' -v (NOTE: read app/tests/test_reproduction.py first — fast calcs live in test_fast_reproduction, slow in test_full_reproduction; build the -k expression so each matrix job runs its one calc regardless of which list it is in; dependency dirs are handled inside the test via committed results). timeout-minutes: 350. Always upload /tmp/qg-repro-test/<dir>/results.json as artifact (if exists) + write pass/fail + max-rel-dev into GITHUB_STEP_SUMMARY. A final 'summary' job (needs: matrix, if: always()) aggregates job results into one summary table.
2. ${ROOT}/.github/workflows/compute.yml — name 'Scaled computation'. Trigger: workflow_dispatch with inputs: driver (choice: ds_entropy_cap_2d | ds_cap_4d | ds4d_saturation), args (string, default '' — extra CLI args appended verbatim), max_hours (string default '5.5'). Job: timeout-minutes: 355, checkout, python 3.13, install requirements-ci.txt, run python compute/drivers/\${{ inputs.driver }}.py --max-hours \${{ inputs.max_hours }} \${{ inputs.args }}, then ALWAYS (if: always()) upload compute/results/** as artifact named \${{ inputs.driver }}-run (retention 90 days) and append the results.json summary block into GITHUB_STEP_SUMMARY (python one-liner). Add OMP_NUM_THREADS: 4, MPLBACKEND: Agg, PYTHONHASHSEED: 0 env.
VALIDATE: python3 -c yaml.safe_load on both files (PyYAML may be absent — pip3 install --user pyyaml if needed). Also append a short '## Výpočty v GitHub Actions' section to ${ROOT}/app/README.md (Czech): how to trigger both workflows (UI + gh workflow run examples incl. passing args), the 6h/16GB limits, how to download artifacts (gh run download), and the cross-HW purpose (linux/x86 vs local macOS/arm64 — tolerance-based comparison, not bit-identity). Do NOT touch compute/drivers/ (another agent owns it). Return status, keyPoints (Czech), testsTally ('n/a' if no tests), files.`,
    { label: 'build:gh-workflows', phase: 'Stavba', model: 'opus', schema: RESULT }),
])

const drivers = batch[0]
const ghwf = batch[1]
log('Stavba hotova (drivery: ' + (drivers ? drivers.status : 'N/A') + ', workflows: ' + (ghwf ? ghwf.status : 'N/A') + '). Úklid…')

phase('Úklid')

const hk = await agent(`You are the housekeeping agent at ${ROOT}. Today ${DATE}. Czech prose / English data. ECONOMY MODE. Round results:
${JSON.stringify({ drivers: drivers ? { status: drivers.status, keyPoints: drivers.keyPoints, tests: drivers.testsTally } : null, ghwf: ghwf ? { status: ghwf.status, keyPoints: ghwf.keyPoints } : null }, null, 1)}

TASK 1: Write ${ROOT}/compute/README.md IN CZECH: účel (škálované běhy o řády výš + cross-HW verifikace na GH Actions), tabulka 3 driverů (co počítá, klíčové parametry, smoke invokace, vazba na F-025/F-028/H5g otázky), checkpointing + time-budget chování, kam padají výsledky (compute/results lokálně; artifacts na GH) a jak je po stažení začlenit (porovnat s committed results.json, případně nový VYPOCET zápis).
TASK 2: Verify FULL suite: cd ${ROOT} && MPLBACKEND=Agg python3 -m pytest app/tests -q — report tally.
TASK 3: Update ${ROOT}/PROGRESS.md (Read first, preserve; REPLACE the stale pause banner at top): nový banner — GH Actions výpočetní infrastruktura hotová (3 drivery, repro.yml matrix 24 výpočtů, compute.yml manuální trigger), repo public + Pages running; log entry.
TASK 4: Update ${ROOT}/knowledge-base/00-INDEX.md (Infrastruktura: compute/ + GH workflows). Rebuild site: python3 ${ROOT}/web/build.py (report pages). git add -A && git -c user.name=pazny -c user.email=pazny.develop@gmail.com commit with a concise message about the GH compute infrastructure (mention Co-Authored-By: Claude Opus 4.8 (1M context) <noreply@anthropic.com> as the last line). Do NOT push.
Return 4-line Czech confirmation incl. commit hash.`,
  { label: 'final:gh-compute', phase: 'Úklid', model: 'sonnet' })

return {
  drivers: drivers ? { status: drivers.status, keyPoints: drivers.keyPoints, tests: drivers.testsTally } : null,
  ghWorkflows: ghwf ? { status: ghwf.status, keyPoints: ghwf.keyPoints } : null,
  housekeeping: hk,
}
