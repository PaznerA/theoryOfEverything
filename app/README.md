# app/ — Dockerizované výzkumné prostředí

Kontejnerizované prostředí pro research / testování / prezentaci projektu Theory of
Everything. Jeden image (`toe-research`), čtyři služby. Repozitář se mountuje do
`/workspace`, takže kontejnery pracují přímo nad živými daty projektu.

Verze knihoven jsou **pinované přesně na ty, kterými prošla deterministická
reprodukce 2026-06-06** (20/20 `calc.py` bitově identických — viz
`reports/2026-06-06-review.md` §f). Změna pinu = povinný re-run plné reprodukce.

## Služby

| Služba | Účel | Spuštění |
|---|---|---|
| `research` | Jupyter Lab nad celým repem (interaktivní výzkum, notebooky) | `docker compose up research` → <http://localhost:8888> (token `toe`) |
| `test` | pytest: smoke test prostředí + rychlá reprodukční sada (6 sub-sekundových výpočtů) | `docker compose run --rm test` |
| `repro` | Plná deterministická reprodukce všech 20 výpočtů (~50 min) | `docker compose run --rm repro` |
| `web` | Minimalistický statický site-builder (krok 4 roadmapy): builduje `web/dist/` (103 stránek) z markdown + JSON zdrojů repozitáře, pak servuje výsledek. Po změně requirements nutný rebuild image: `docker compose build`. | `docker compose --profile web up web` → <http://localhost:8080> |

Plnou reprodukci lze pustit i přes pytest s detailním reportem po výpočtech:

```bash
docker compose run --rm -e FULL_REPRO=1 test
```

## Konvence

- **Pořadí spouštění výpočtů** (skryté závislosti, viz `papers/REVIZE-PRO-CLOVEKA.md` §4.3):
  `sj-threshold-scan` před `sj-far-zone`; `modular-flow-corner` před `modular-flow-bd-4d`;
  po `sj-vn-type/calc.py` ještě `calc_uncertainty.py`. Testy v `app/tests/` to respektují.
- Determinismus: `OMP_NUM_THREADS=4`, `PYTHONHASHSEED=0`, `MPLBACKEND=Agg` (nastaveno
  v image i compose). Na ověřeném hostu (macOS/arm64) jsou běhy bitově identické;
  v kontejneru (linux) testy tolerují <5% relativní odchylku BLAS.
- Budoucí složky (krok 3–4 roadmapy): kombinovatelné simulační funkce a site-builder
  přibydou jako další služby/příkazy tady v `app/`.

## Výpočty v GitHub Actions

Repozitář je **veřejný**, takže GitHub Actions běží zdarma. Runnery jsou
`ubuntu-latest` = **4 vCPU / 16 GB RAM / linux/x86_64**, s **tvrdým limitem 6 h na
job** (workflowy proto cílí na `timeout-minutes` 350–355 a výpočetní drivery mají
měkký časový rozpočet `--max-hours`, který se dokončí a ukončí čistě před tím).

Obě workflow se spouští **ručně** (`workflow_dispatch`) — z webového UI
(záložka *Actions* → vyber workflow → *Run workflow*) nebo přes `gh`.

### 1. `Cross-HW reproduction` (`.github/workflows/repro.yml`)

Přepočítá committed kalkulace na linuxovém runneru a porovná proti
`core-data/calculations/<dir>/results.json` toleranční metodou (žádné překlopení
verdiktu, žádné strukturální rozdíly, max. relativní numerická odchylka < 5 %).
Matice běží paralelně přes všech 24 adresářů (`max-parallel: 20`,
`fail-fast: false`); vstup `target` umožní pustit jen jeden.

```bash
# všech 24 kalkulací
gh workflow run repro.yml -f target=all

# jen jedna kalkulace
gh workflow run repro.yml -f target=sj-far-zone
```

Pozn.: čtyři adresáře (`ds-entropy-cap`, `ds-tracial-probe`,
`modular-flow-codim2`, `sj-desitter-4d`) zatím nemají reprodukční test —
jejich job se reportuje jako **skipped** (pytest exit 5), ne jako chyba.

### 2. `Scaled computation` (`.github/workflows/compute.yml`)

Spustí jeden výpočetní driver (`compute/drivers/<driver>.py`) ve velkém.
Vstupy: `driver` (`ds_entropy_cap_2d` | `ds_cap_4d` | `ds4d_saturation`),
`args` (extra CLI argumenty doslova přidané za příkaz) a `max_hours`
(měkký časový rozpočet, default `5.5`). Driver průběžně checkpointuje
(`results.json` se přepisuje po každé buňce), takže i job, který narazí na časový
strop, nahraje `results.json` se `status: partial-time-budget`.

```bash
# 2D dS entropy cap, vyšší hustoty a víc seedů
gh workflow run compute.yml \
  -f driver=ds_entropy_cap_2d \
  -f args="--rho 1e4,3e4 --patch-l 2.0,2.5 --seeds 8" \
  -f max_hours=5.5

# 4D otevřená otázka (dimenzní závislost koeficientu area-law)
gh workflow run compute.yml -f driver=ds_cap_4d -f args="--n-max 20000"
```

Job nastavuje `OMP_NUM_THREADS=4`, `MPLBACKEND=Agg`, `PYTHONHASHSEED=0`. Sumář
ze `summary` bloku `results.json` se vypisuje do *Job summary*.

### Stažení artefaktů

Oba workflowy nahrávají výstupy jako artefakty (`repro-<dir>` s přepočteným
`results.json`; `<driver>-run` s celým `compute/results/**`, retence 90 dní).

```bash
gh run list --workflow=compute.yml          # zjisti RUN_ID
gh run download <RUN_ID>                     # všechny artefakty běhu
gh run download <RUN_ID> -n ds_cap_4d-run    # jen jeden artefakt
```

### Smysl cross-HW běhu

Ověřený host je **macOS/arm64** (tam jsou běhy bitově identické). GitHub runner je
**linux/x86_64** — jiný BLAS a zaokrouhlování. Cílem proto **není** bitová shoda, ale
**tolerance-based** porovnání (verdikt stabilní, max. rel. odchylka < 5 %): potvrzuje
přenositelnost výsledků napříč architekturami, ne bit-identitu.
