# Numerická reprodukční coverage druhého oblouku (kola 13–20, F-029…F-039)

> Datum: 2026-06-09. Protějšek CAS revize (`2026-06-08-cas-formula-revision.md`): zatímco Wolfram ověřil *symbolické* vzorce, tato pasáž ověřuje *numerickou reprodukovatelnost* — re-run každého nového `calc.py` a srovnání s commitnutým `results.json` v `app/tests/test_reproduction.py` (dvoustupňová tolerance, deterministické seedy).

## Mezera

Druhý výzkumný oblouk přidal **8 calc adresářů mimo reprodukční coverage** (běžely jen jednou agentem) + **3 agenty-přidané, ale nikdy pod `FULL_REPRO` neověřené**. Celkem 11 calcs k ověření.

## Výsledek

**10 z 11 nyní v reprodukci a ověřeno PASS; 1 vyloučen s dokumentací.**

| Calc | F-ID | Stav | Pozn. |
|---|---|---|---|
| modular-kms-thermal | F-034 | ✅ PASS | ~10 s |
| ncg-kms-unruh | F-036 | ✅ PASS | ~54 s |
| index-charge-discrete | H-E probe | ✅ PASS | ~56 s |
| amol-anomaly-ee-coeff | F-039 | ✅ PASS | dep + plot-path opraveno |
| spectral-triple-modular | F-033 | ✅ PASS | **determinismus opraven** |
| sj-kerr-b-scan | F-030 | ✅ PASS | ~12,6 min |
| vn-type-proxy3-seeds | F-032 | ✅ PASS | ~15 min |
| lambda-shot-noise | F-035 | ✅ PASS | skrytě rozbitý → opraveno |
| ds-conformal-4d | F-037 | ✅ PASS | ~17 min |
| ds-molecule-fluctuation | F-038 | ✅ PASS | ~9 min |
| **ds-amol-convention** | F-031 | ⚪ VYLOUČEN | čte staged archiv `compute/results-archive/` mimo sandbox; re-analýza cross-HW ověřených cloud běhů |

## Nalezené a opravené problémy (hodnota této pasáže)

Stejně jako CAS revize našla Myrheim-Meyer factor-2 bug, numerická coverage našla reálné reprodukční defekty:

1. **`TIMING_FIELDS` mezera (3 calcs).** Nové calcs měří čas jako `elapsed_s` / `wall_clock_s` / `wall_clock_min`, ale reprodukce ignorovala jen `runtime_s`/`timing_s` → falešné fully. Rozšířeno (`+elapsed_s,+wall_clock`). Odhalilo, že **`lambda-shot-noise`** (už v `SLOW_CALCS` s `wall_clock_s`) byl **skrytě rozbitý** — nikdy neběžel pod `FULL_REPRO`, takže by spadl v CI.

2. **`spectral-triple-modular` NEdeterminismus (nosný nález).** Connesova pasáž měla wall-clock cap a ukládala jen *dokončené* páry (committed 14, závislé na rychlosti stroje). Oprava `t_start=None` (vždy 16 párů) → deterministické. **DŮSLEDEK: commitnutá korelace F-033 = 0,098 byla artefakt timing-truncovaného běhu; reprodukovatelná deterministická hodnota je 0,319 (R²=0,10).** Verdikt **no-match NEZMĚNĚN** (0,319 << 0,5 práh). F-033 + VYPOCET-29 opraveny na deterministická čísla + poznámka. *Toto je numerický protějšek Myrheim-Meyer nálezu — finding, jehož headline číslo pocházelo z nereprodukovatelného běhu.*

3. **`amol-anomaly-ee-coeff` dvě drobnosti.** (a) Čte F-029 c_EE z `ds-entropy-cap` → přidán do `deps` mapy (jako sj-far-zone→sj-threshold-scan). (b) `/plot` ukládal location-závislou cestu (repo-relativní vs. `/tmp`-relativní) → nový obecný `PATH_FIELDS` ignore (plot-cesty jsou metadata, ne fyzika; pomůže i budoucím calcs).

## Bilance

Reprodukční garda teď pokrývá **druhý oblouk deterministicky** (10/11 calcs, jeden vyloučen by-design). Jediná věcná oprava findingu (F-033 0,098→0,319) je honest analog CAS Myrheim-Meyer nálezu: nezměnila verdikt, ale opravila nereprodukovatelné číslo. 36 čistě numerických findings (fity/exponenty) zůstává ověřitelných jen re-runem svých calcs — což je teď garda zajišťuje.

**Commity:** `d09ee11` (TIMING_FIELDS + 3 levné), `83d81f2` (amol+spectral, determinismus + F-033 oprava), `242cfc1` (kerr+proxy3, ds-amol vyloučen).
