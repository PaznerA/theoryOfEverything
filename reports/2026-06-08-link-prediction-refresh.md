# Refresh predikce vazeb po propagaci datově aktivovaných hran (2026-06-08)

## Co se dělalo

Exploratory Engine navrhl pět **datově podložených aktivovaných hran** (finding-backed) +
čtyři spekulativní kandidáty. Pět podložených hran bylo propagováno do fragmentů
(`core-data/fragments/*.json`), poté přegenerovány registry přes
`workflows/consolidate.py` a znovu spuštěna predikce vazeb
(`workflows/qg-link-prediction.py`). Předchozí běh byl 2026-06-07.

**Důležité (provenience):** žádná hrana nebyla nově *přidána* — všech pět cílových hran
v grafu **už existovalo**. Editace upravily jejich `description` (přidaly citace nálezů
F-009..F-035 + VYPOCET writeupy + české anotace) a u jediné hrany `explored` rating.
Čtyři spekulativní `newCandidates` se do fragmentů **nezapisují** (jsou to návrhy pro
editora, viz sekce níže) — drží se proveniencní politika.

## Propagované hrany (5 podložených)

| idx | hrana | typ | rating před → po | nález(y) |
|-----|-------|-----|------------------|----------|
| 61  | causal-sets ↔ noncommutative-geometry | shared-math | barely → **barely** (anotace, ne upgrade) | F-033, F-034 |
| 289 | von-neumann-algebras ↔ causal-sets | shared-math | partially → **partially** (rozšíření) | +F-029, F-031, F-032 |
| 59  | causal-sets ↔ black-holes-information | conjecture | partially → **partially** (rozšíření) | +F-029, F-031 |
| 65  | causal-sets ↔ cosmological-constant-fluctuation | conjecture | partially → **partially** (rozšíření) | F-005, F-035 |
| 212 | semiclassical-gravity ↔ causal-sets | shared-structure | barely → **partially** (UPGRADE) | F-009, F-013, F-017, F-018, F-030 |

Jediný ratingový pohyb: **semiclassical-gravity ↔ causal-sets** barely → partially
(hustá SJ-rotující/superradiance datová linie přes pět nálezů, dosud nezakreslená v žádné
hraně). Hrana causal-sets ↔ noncommutative-geometry **záměrně zůstává barely**:
metrická osa je čistý negativ (F-033, Connesova vzdálenost vs geodetická R²=0.0095),
KMS osa jen kvalitativní pozitiv (F-034) — informovaný negativ se nenafukuje na partially.

## Statistiky registrů (po consolidate)

| metrika | 2026-06-07 | 2026-06-08 |
|---------|-----------|-----------|
| connections.json (hrany) | 292 | 292 |
| explored = barely | 114 | **113** |
| explored = partially | 112 | **113** |
| explored = well | 66 | 66 |
| concept-graph nodes | 626 | 626 |
| concept-graph edges (raw) | 2481 | 2481 |

Posun barely 114→113, partially 112→113 odpovídá přesně jednomu ratingovému upgradu
(idx 212). Počet hran beze změny — neměnily se topologie, jen popisy/ratingy existujících hran.

## Predikce vazeb — výsledky

| metrika | 2026-06-07 | 2026-06-08 |
|---------|-----------|-----------|
| AUC (mean) | 0.9034 | **0.9034** |
| AUC (std) | 0.0176 | 0.0176 |
| AUC (min / max) | 0.8763 / 0.9308 | 0.8763 / 0.9308 |
| P@50 (mean) | 0.9975 | 0.9975 |
| dedup hran (do predikce) | 1632 | 1632 |
| top kandidátů | 50 | 50 |
| cross-pillar | 17 | 17 |
| pillar-pair | 17 | 17 |

## Top movers vs 2026-06-07: ŽÁDNÉ

Seznam top-50 kandidátů je **bajt-identický** (pořadí i skóre na 6 desetinných míst).
Žádný nový kandidát se neobjevil, žádný nevypadl, žádný se neposunul v pořadí.

**Proč:** algoritmus predikce vazeb (ensemble pěti klasických heuristik + spektrální
embedding normalizovaného Laplaciánu, d=32) pracuje **čistě nad topologií grafu**
(adjacenční matice + multiplicita hran). Je slepý vůči textu `description` i vůči
ratingu `explored`. Protože jsme nepřidali ani neodebrali žádnou hranu, dedup-graf
zůstal identický (1632 hran, 626 uzlů) → spektrální embedding i všechny heuristiky
vrací identická skóre.

Jediná naměřená odchylka: per-komponentní `spectral` AUC 0.9297 → 0.9295 (Δ = −0.0002),
což je zaokrouhlovací šum seedované eigendekompozice, nikoli signál.

**Důsledek pro budoucí běhy:** ratingové/anotační propagace samy o sobě top movery
nezmění. Pohnout predikcí může až přidání *nové* hrany (nová `connection` ve fragmentu
mezi dvěma uzly, které dosud spojeny nebyly) — tj. realizace některého ze čtyř
spekulativních kandidátů níže po editorské validaci.

## Spekulativní kandidáti (NEzapsáno do fragmentů — návrhy pro editora)

Tyto čtyři hrany Exploratory navrhl jako *nové* (dosud v grafu neexistující), ale
**nejsou podloženy přímým nálezem na dané dvojici pilířů** — jen sdílenou matematikou.
Drží se proveniencní politika: zapisují se sem jako návrhy, do fragmentů až po
editorském/výzkumném rozhodnutí.

1. **cosmological-constant-fluctuation → experimental-tests** — boost-invariance Var(N)
   Poissonova sprinklingu (F-035) je táž vlastnost jako Lorentz-invariance chránící CST
   před LIV/birefringence testy (idx 119). Everpresent-Λ test (SNe/CMB) a swerve
   fenomenologie = dvě pozorovatelné téhož Poissonova procesu. Most v grafu chybí.
2. **noncommutative-geometry → semiclassical-gravity** — F-034 instancuje Connes-Rovelliho
   tepelný čas (gr-qc/9406019) na diskrétní struktuře: SJ modulární tok = pravý KMS tok
   (β_KMS=1). Most přes thermal-time relaci (Connes cocycle) zatím není datová hrana.
3. **von-neumann-algebras → cosmological-constant-fluctuation** — skrytá sdílená matematika
   "bounded-region → finite count/trace": je δΛ~1/√V (F-035) projevem téže konečnosti
   trace, která dělá algebru typu II₁ (CLPW dS static patch, F-023/F-025 cap=480)?
4. **semiclassical-gravity → black-holes-information** — SJ superradiantní linie
   (F-030/F-017/F-018, W_sr~Ω(r)^B, A_W<0) je o extrakci energie/informace z rotujících
   horizontů (superradiance ↔ Penrose ↔ informační tok). Hrana semiclassical↔black-holes
   je v jádru literatury `well`, ale SJ-superradiance datová specifikace v ní chybí.

Pozn.: kandidáti 1 a 3 by po realizaci do grafu přidali **cross-pillar** hranu, která
by jako jediná mohla reálně pohnout top-50 predikce — proto jsou nejzajímavější pro
další kolo.

## Soubory

- Editované fragmenty: `core-data/fragments/causal-sets.json`,
  `core-data/fragments/von-neumann-algebras.json`,
  `core-data/fragments/semiclassical-gravity.json`
- Přegenerováno: `core-data/connections.json`, `core-data/concept-graph.json`,
  `core-data/references.{json,bib}`, `core-data/formulas.json`,
  `core-data/open-problems.json`, `core-data/_digest.md`
- Predikce: `core-data/link-predictions.json` (generated 2026-06-08)
- Skript date-stamp: `workflows/qg-link-prediction.py` (GENERATED_DATE 2026-06-07 → 2026-06-08)
