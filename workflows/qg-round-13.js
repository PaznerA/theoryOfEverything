export const meta = {
  name: 'qg-round-13',
  description: 'Kolo 13: VYPOCET-25 syntéza škálovaných GH běhů (2D R konstanta vs 4D c-drift, F-025 saturace) + F-029; oprava driver bugu (per-cell checkpoint + nevynucený --max-hours uvnitř buňky); úklid',
  phases: [
    { title: 'Analýza + driver fix', detail: 'VYPOCET-25 writeup + oprava ds4d driverů paralelně', model: 'opus' },
    { title: 'Úklid', detail: 'findings, PROGRESS, INDEX, web, commit+push', model: 'sonnet' },
  ],
}

const ROOT = '/Users/pazny/projects/theoryOfEverything'
const CD = ROOT + '/core-data'
const KB = ROOT + '/knowledge-base'
const ARCH = ROOT + '/compute/results-archive'
const DATE = (args && args.date) || '2026-06-08'

const RESULT = {
  type: 'object',
  properties: {
    status: { type: 'string', description: 'success | partial | failed' },
    keyNumbers: { type: 'string' },
    verdict: { type: 'string', description: 'Czech, 3-5 sentences' },
    files: { type: 'array', items: { type: 'string' } },
  },
  required: ['status', 'keyNumbers', 'verdict', 'files'],
}

const FIX = {
  type: 'object',
  properties: {
    status: { type: 'string' },
    keyPoints: { type: 'array', items: { type: 'string' }, description: 'Czech' },
    testsTally: { type: 'string' },
    files: { type: 'array', items: { type: 'string' } },
  },
  required: ['status', 'keyPoints', 'testsTally', 'files'],
}

const NOTE = {
  type: 'object',
  properties: { file: { type: 'string' }, keyPoints: { type: 'array', items: { type: 'string' } } },
  required: ['file', 'keyPoints'],
}

phase('Analýza + driver fix')
log('VYPOCET-25 syntéza + oprava driver checkpoint/time-budget bugu…')

const batch = await parallel([
  // ---- VYPOCET-25 writeup ----
  () => agent(`You are a computational physics analyst at ${ROOT}. Write VYPOCET-25 — the synthesis of the scaled GitHub-Actions compute campaign (rounds answering H5g-1/H5g-2 at scale). Czech prose writeup, English data. NEVER fudge; honest interpretation over clean story.

DATA (staged cloud artifacts — read them directly):
- ${ARCH}/ds_cap_4d-grid.json (4D cap-ratio, rho 60-960 x l 0.8-1.5, 6 seeds — dense, many low-R2 cells)
- ${ARCH}/ds_cap_4d-highN.json (4D, rho 960/1920, N up to 6144 — the decisive high-N follow-up)
- ${ARCH}/ds_entropy_cap_2d-rho30k.json (2D R constant, rho 240-1200 x l 0.7-2.5 reached before timeout; rho 3000/30000 cells present but null/incomplete)
- ${ARCH}/ds4d_saturation-rho120.json (4D F-025 saturation: rho=120 cell complete with "clean saturation", rho 600/2000 skipped/incomplete)
Also read for context: ${KB}/vypocty/VYPOCET-23-ds-entropy-cap.md (the committed 2D F-028 basis: R=0.1321, c=7.57), VYPOCET-21-desitter-4d-area-law.md (F-025 origin), ${CD}/findings.json F-023/F-025/F-028.

THE FINDINGS TO ESTABLISH (verify each against the JSON — pull EXACT numbers; if a cell has low fit R2 mark it):
1. **2D R constant CONFIRMED + EXTENDED**: across rho 240-1200 AND patch size l 0.7-2.5, R = S_full_cap/A_mol stays ~0.13 (compute the mean+CV from the valid cells; committed F-028 was 0.1321/1.3%/c=7.57 over the narrower l range). State honestly which high-rho cells did NOT complete (timeout).
2. **4D c is NOT constant — dimension-dependent in this convention**: R_full^4D DRIFTS as ~rho^(-0.52+/-0.30); c^4D grows 15 -> 66 as rho 240 -> 1920 (give the table). KEY interpretation (be rigorous, present THREE competing explanations and what would distinguish them):
   (a) DISCRETE-AREA CONVENTION: 2D horizon = a point (codim-2 in 2D = 0-dim, molecule count rho-independent), 4D horizon = codim-2 surface whose molecule count A_mol ~ rho^(1/2) grows with refinement; the rho^(-1/2) drift is ~exactly the inverse of this growth => S_full_cap is roughly rho-INDEPENDENT in 4D, i.e. the cap does not track the discretization the way 2D does. This is the LEADING explanation — show the rho^(-0.52) ~ -1/2 match quantitatively.
   (b) CONFORMAL-WEIGHT CAVEAT: the 4D scalar is not conformally invariant; our object (flat causal order + dS measure + Johnston link Green) is a controlled approximation, not the exact dS state — the drift could be the approximation, not physics.
   (c) GENUINE DIMENSION-DEPENDENCE of the entropy-area coefficient.
   The discriminator between (a) and (c): does S_full_cap itself (not the ratio) saturate to a rho-independent constant? Check this in the data and report.
3. **F-025 4D saturation**: rho=120 shows clean saturation (dS truncated-S late-slope -> 0 vs flat grows); the higher-rho confirmation is COMPUTE-BOUND (see the driver-bug finding) — state this as an honest limitation, not a result.
4. **Cross-HW**: note these ran on linux/x86_64 GH Actions, consistent with the macOS values where cells overlap (the 2D R matches committed within CV).

WRITE ${KB}/vypocty/VYPOCET-25-scaled-ds-entropy.md: header, motivation, the 4 findings with exact-number tables, the 3-way interpretation of the 4D drift with the quantitative rho^(-1/2) argument front and center, an honest "Compute limitations" section (per-cell checkpoint + unenforced max-hours => two 6h cloud runs and two 5h local runs produced ZERO higher-rho saturation cells; lesson for drivers), and "What this means for draft-04 dS section / a potential draft-05" (the 2D result is publishable-strength; the 4D needs the convention question resolved FIRST — likely (a), which would mean NO clean 4D area-law constant, weakening any 4D A/4 claim). Czech prose, cite JSON paths + finding ids.
ALSO: produce a single summary figure via matplotlib(Agg): R vs rho for 2D (flat line ~0.13) and 4D (declining ~rho^-0.5) on log-log, saved to ${CD}/calculations/ds-entropy-cap/plots/R_2d_vs_4d.png (read a calc dir's plotting style; keep it a standalone script you run).
Return status, keyNumbers (the headline 2D R + 4D c-range + drift exponent), verdict (Czech), files.`,
    { label: 'calc:vypocet-25', phase: 'Analýza + driver fix', model: 'opus', schema: RESULT }),

  // ---- driver bug fix ----
  () => agent(`You are a compute-infra engineer at ${ROOT}. Fix a REAL bug exposed today: the ds4d_saturation and ds_cap_4d drivers checkpoint per (rho,l) CELL and only check the --max-hours budget BETWEEN cells. When a single heavy 4D-sparse cell exceeds the budget (rho>=600, N up to ~2e4), the cell never completes => (i) the time budget is NEVER enforced (two local runs ran 5h+ past a 1.5h budget), and (ii) NO checkpoint is ever written => 6h cloud jobs and 5h local jobs produced ZERO artifacts.

READ FIRST: compute/drivers/_common.py (the checkpoint writer + time-budget helper), compute/drivers/ds4d_saturation.py and ds_cap_4d.py (find the per-cell loop and where max-hours is checked), compute/README.md.

FIX (minimal, correct, tested):
1. FINER CHECKPOINT GRANULARITY: write/append a partial checkpoint after each (rho, l, BOX) or at least after each (rho,l,seed) sub-step, not only after a full cell — so a killed/timed-out run keeps whatever boxes/seeds finished. Partial cells must be marked (e.g. cell status 'partial' with completed_boxes/completed_seeds counts) and the summary must tolerate partial cells.
2. ENFORCE --max-hours MID-CELL: check the wall-clock budget inside the box/seed loop too; on exceed, finalize the current partial checkpoint and exit 0 with status 'partial-time-budget'. A budget must NEVER be silently exceeded.
3. Keep the existing CLI contract and output schema backward-compatible (existing committed results.json must still be readable; add fields, don't rename). Both drivers share the pattern — factor the guard into _common.py if clean.
4. TESTS: extend app/tests/test_compute_drivers.py — a tiny run with an ABSURDLY small --max-hours (e.g. 0.0003 h ~ 1 s) on a non-trivial config must (a) exit 0, (b) write a results.json with status 'partial-time-budget', (c) the wall-clock must be within a small multiple of the budget (assert it did NOT run 10x over — this is the regression guard for the bug). Keep total test time < 90 s.
5. Document in compute/README.md (Czech): the checkpoint granularity + that --max-hours is now enforced mid-cell; and a one-line warning that heavy 4D cells at rho>=600 need either GH Actions with the finer checkpoint or a multi-job split (one rho per job).
RUN: cd ${ROOT} && MPLBACKEND=Agg python3 -m pytest app/tests/test_compute_drivers.py -v (must pass, including the new budget-enforcement test). Return status, keyPoints (Czech), testsTally, files.`,
    { label: 'fix:driver-budget', phase: 'Analýza + driver fix', model: 'opus', schema: FIX }),
])

const calc = batch[0]
const fix = batch[1]
log('Hotovo (VYPOCET-25: ' + (calc ? calc.status : 'N/A') + ', driver fix: ' + (fix ? fix.status : 'N/A') + '). Úklid…')

phase('Úklid')
const hk = await agent(`You are the housekeeping agent at ${ROOT}. Today ${DATE}. Czech prose / English data. ECONOMY MODE. Round-13 results:
${JSON.stringify({ calc: calc ? { keyNumbers: calc.keyNumbers, verdict: calc.verdict } : null, fix: fix ? { status: fix.status, keyPoints: fix.keyPoints } : null }, null, 1)}

TASK 1: Update ${CD}/findings.json — append F-029: the scaled campaign result (2D R constant confirmed/extended c~7.6; 4D c dimension-dependent / drifts rho^-0.52, leading explanation = discrete-area convention so the 4D cap likely has NO clean area-law constant; F-025 4D saturation clean at rho=120, higher-rho compute-bound). Conservative status 'partial' or 'supported' as the data warrants; caveats incl. the convention question + compute limitation; evidence paths = compute/results-archive/* + VYPOCET-25 writeup (verify exist).
TASK 2: Full suite: cd ${ROOT} && MPLBACKEND=Agg python3 -m pytest app/tests -q (report tally).
TASK 3: Update ${ROOT}/PROGRESS.md (Read first): log entry kolo 13 (VYPOCET-25 + driver budget fix + F-029); banner -> scaled campaign vyhodnocena, výpočetní fronta prázdná. Note the BRAINSTORM-05 H5g-1/H5g-2 status: H5g-1 4D saturation clean at rho=120 (supported, higher-rho compute-bound); H5g-2 2D quantitative area-law confirmed but 4D constant likely absent (convention) — append one-line status notes to BRAINSTORM-05.md next to H5g-1/H5g-2.
TASK 4: Update ${KB}/00-INDEX.md (VYPOCET-25). Rebuild web: python3 ${ROOT}/web/build.py (report pages). git add -A && git -c user.name=pazny -c user.email=pazny.develop@gmail.com commit (message: VYPOCET-25 scaled dS entropy synthesis + ds4d driver budget/checkpoint fix + F-029) with Co-Authored-By: Claude Opus 4.8 (1M context) <noreply@anthropic.com> last line, then git push.
Return 4-line Czech confirmation incl. commit hash + pytest tally.`,
  { label: 'final:round13', phase: 'Úklid', model: 'sonnet', schema: NOTE })

return { vypocet25: calc, driverFix: fix, housekeeping: hk }
