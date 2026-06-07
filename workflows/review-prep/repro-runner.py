#!/usr/bin/env python3
"""Deterministic reproduction runner for the big review (zero LLM tokens).

For every dir in core-data/calculations/ with calc.py + results.json:
copy to /tmp/qg-repro/<name> (without plots/), re-run calc.py there,
numerically diff the regenerated results.json against the committed one.
Progressive output: workflows/review-prep/repro-results.json + repro.log.
"""
import json, os, shutil, subprocess, sys, time

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
CALC = os.path.join(ROOT, 'core-data', 'calculations')
OUTD = os.path.join(ROOT, 'workflows', 'review-prep')
TMP = '/tmp/qg-repro'
PER_CALC_TIMEOUT = 1800  # s

LOG = open(os.path.join(OUTD, 'repro.log'), 'a', buffering=1)

def log(msg):
    line = f"[{time.strftime('%H:%M:%S')}] {msg}"
    print(line)
    LOG.write(line + '\n')

def compare(a, b, path=''):
    """Recursive diff; returns list of (path, kind, detail)."""
    diffs = []
    if isinstance(a, dict) and isinstance(b, dict):
        for k in a:
            if k not in b:
                diffs.append((f'{path}/{k}', 'missing-in-new', None))
            else:
                diffs += compare(a[k], b[k], f'{path}/{k}')
        for k in b:
            if k not in a:
                diffs.append((f'{path}/{k}', 'new-key', None))
    elif isinstance(a, list) and isinstance(b, list):
        if len(a) != len(b):
            diffs.append((path, 'len-change', f'{len(a)}->{len(b)}'))
        for i, (x, y) in enumerate(zip(a, b)):
            diffs += compare(x, y, f'{path}[{i}]')
    elif isinstance(a, bool) or isinstance(b, bool):
        if a != b:
            diffs.append((path, 'verdict-flip', f'{a!r}->{b!r}'))
    elif isinstance(a, (int, float)) and isinstance(b, (int, float)):
        if a != b:
            # Noise floor: machine-precision residuals (pairing, traces, ...)
            # are "equal" whenever both sides sit below the floor — comparing
            # 4e-16 vs 7e-16 relatively would report a meaningless 43% dev.
            if abs(a) < 1e-10 and abs(b) < 1e-10:
                return diffs
            denom = max(abs(a), abs(b), 1e-300)
            rel = abs(a - b) / denom
            if rel > 1e-9:
                diffs.append((path, 'num', rel))
    else:
        if a != b:
            diffs.append((path, 'value-change', f'{a!r}->{b!r}'[:200]))
    return diffs

def classify(diffs):
    flips = [d for d in diffs if d[1] == 'verdict-flip']
    nums = [d for d in diffs if d[1] == 'num']
    structural = [d for d in diffs if d[1] in ('missing-in-new', 'new-key', 'len-change', 'value-change')]
    max_rel = max((d[2] for d in nums), default=0.0)
    if flips:
        status = 'VERDICT-FLIP'
    elif structural:
        status = 'structural-diff'
    elif max_rel == 0.0 and not nums:
        status = 'identical'
    elif max_rel < 1e-6:
        status = 'reproduced-exact'
    elif max_rel < 0.05:
        status = 'reproduced-tolerance'
    else:
        status = 'DEVIATES'
    return status, max_rel, flips, structural, nums

def main():
    os.makedirs(TMP, exist_ok=True)
    results_path = os.path.join(OUTD, 'repro-results.json')
    results = {}
    dirs = sorted(d for d in os.listdir(CALC) if os.path.isdir(os.path.join(CALC, d)))
    log(f'START repro run over {len(dirs)} calculation dirs')
    for d in dirs:
        src = os.path.join(CALC, d)
        if not (os.path.exists(os.path.join(src, 'calc.py')) and os.path.exists(os.path.join(src, 'results.json'))):
            results[d] = {'status': 'skipped', 'reason': 'missing calc.py or results.json'}
            log(f'{d}: SKIPPED (missing files)')
            json.dump(results, open(results_path, 'w'), indent=1)
            continue
        dst = os.path.join(TMP, d)
        shutil.rmtree(dst, ignore_errors=True)
        shutil.copytree(src, dst, ignore=shutil.ignore_patterns('plots'))
        orig = json.load(open(os.path.join(src, 'results.json')))
        env = dict(os.environ, OMP_NUM_THREADS='4', MPLBACKEND='Agg', PYTHONHASHSEED='0')
        t0 = time.time()
        log(f'{d}: running calc.py ...')
        try:
            proc = subprocess.run([sys.executable, 'calc.py'], cwd=dst, env=env,
                                  capture_output=True, text=True, timeout=PER_CALC_TIMEOUT)
        except subprocess.TimeoutExpired:
            results[d] = {'status': 'timeout', 'runtime_s': round(time.time() - t0)}
            log(f'{d}: TIMEOUT after {PER_CALC_TIMEOUT}s')
            json.dump(results, open(results_path, 'w'), indent=1)
            continue
        rt = round(time.time() - t0)
        if proc.returncode != 0:
            results[d] = {'status': 'run-error', 'runtime_s': rt,
                          'stderr_tail': proc.stderr[-1500:]}
            log(f'{d}: RUN-ERROR rc={proc.returncode} ({rt}s)')
            json.dump(results, open(results_path, 'w'), indent=1)
            continue
        new_path = os.path.join(dst, 'results.json')
        if not os.path.exists(new_path):
            results[d] = {'status': 'no-output', 'runtime_s': rt}
            log(f'{d}: NO results.json produced ({rt}s)')
            json.dump(results, open(results_path, 'w'), indent=1)
            continue
        try:
            new = json.load(open(new_path))
        except Exception as e:
            results[d] = {'status': 'bad-output', 'runtime_s': rt, 'error': str(e)}
            log(f'{d}: BAD results.json ({e})')
            json.dump(results, open(results_path, 'w'), indent=1)
            continue
        diffs = compare(orig, new)
        status, max_rel, flips, structural, nums = classify(diffs)
        top_nums = sorted(nums, key=lambda x: -x[2])[:10]
        results[d] = {
            'status': status, 'runtime_s': rt,
            'n_diffs': len(diffs), 'max_rel_dev': max_rel,
            'verdict_flips': [list(x) for x in flips][:20],
            'structural': [list(x) for x in structural][:20],
            'top_numeric_devs': [[p, round(r, 6)] for p, _, r in top_nums],
        }
        log(f'{d}: {status} (max_rel={max_rel:.2e}, diffs={len(diffs)}, {rt}s)')
        json.dump(results, open(results_path, 'w'), indent=1)
    summary = {}
    for d, r in results.items():
        summary.setdefault(r['status'], []).append(d)
    log('DONE. Summary: ' + json.dumps({k: len(v) for k, v in summary.items()}))
    json.dump({'results': results, 'summary': summary},
              open(results_path, 'w'), indent=1)

if __name__ == '__main__':
    main()
