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
