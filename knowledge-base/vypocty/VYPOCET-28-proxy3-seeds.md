# VYPOCET-28: proxy3 (centrální sekvence / self-averaging) při vysokém počtu seedů — rozhodnutí verdiktu 2D diamantu 2/3 vs 3/3

**Datum:** 2026-06-08
**Soubory:** `core-data/calculations/vn-type-proxy3-seeds/calc.py`, `results.json`, `cv_trunc_vs_N.png`
**Status:** Dokončeno
**Navazuje na:** VYPOCET-12 (`sj-vn-type`), nález F-015 (2D diamant 2/3 proxy)
**Hypotéza:** H3g-3 (truncace SSEE = crossed-product modulární cutoff, III₁ → II)
**Slug:** `vn-type-proxy3-seeds`

---

## Otázka

VYPOCET-12 uzavřel 2D diamant verdiktem **2/3 proxy** pro přechod typu III₁ → II. Třetí proxy — **centrální sekvence / faktorová self-averaging signatura** (seed-to-seed CV truncované SSEE má pro faktor typu II klesat s N) — byla u 8 seedů (VYPOCET-12), 5 seedů (VYPOCET-19) i jako nezapočítaná u 4D slabu (VYPOCET-16) **NESIGNIFIKANTNÍ**: mocninový sklon CV(S_trunc) ∼ N^(−0.71 ± 0.78) byl konzistentní s nulou.

`type_proxies` v `lib/toe/vntype.py` označí proxy3 jako `factor_like` jen při splnění VŠECH tří podmínek:
(a) `self_avg`: `cv_trunc[-1] < 0.05`; (b) `cv_fit.value < 0` (CV klesá = self-averaging); (c) `cv_sig`: `|sklon|/se > 2`. Při 5–8 seedech je odhad CV příliš zašuměný pro (c). **Tento výpočet rozhoduje: stačí 30–50 seedů na překročení signifikance, nebo proxy3 zůstává nulová i při vysokém počtu seedů?**

Konvence převzaty verbatim z VYPOCET-12: builder `toe.causet.sprinkle_diamond2d`, `frac = 0.5`, `seed_base = 7 000 000`, seed = `seed_base + 1000·N + s`, κ = √N/(4π), S = Σ μ ln|μ|.

---

## Důležité metodické zjištění: sklon i SE závisí na N-gridu

Zadaný N-grid byl `[300, 500, 800, 1200, 1700]` (5 bodů, **NOVÝ grid**). VYPOCET-12 ovšem použil `[400, 600, 800, 1000, 1200, 1500, 1800]` (7 bodů, **PŮVODNÍ grid**). Protože sklon CV-vs-N i jeho reziduální SE silně závisí na gridu, **měřil jsem proxy3 na OBOU gridech** při 8 i 50 seedech, abych oddělil efekt počtu seedů od volby gridu. Bez toho by „8 vs 40 seedů side-by-side" zaměňoval dvě proměnné.

### Srovnávací tabulka (CV(S_trunc) ∼ N^sklon)

| Grid | seedů | sklon ± SE | t = \|sklon\|/se | sig (t>2) | self_avg | factor_like |
|---|---|---|---|---|---|---|
| **NOVÝ** [300..1700] | 8 | −0.649 ± 0.121 | 5.37 | ✓ | ✓ | ✓ |
| **NOVÝ** [300..1700] | 50 | −0.377 ± 0.086 | 4.38 | ✓ | ✓ | ✓ |
| **VYPOCET-12** [400..1800] | 8 | −0.280 ± 0.190 | **1.48** | **✗** | ✗ (cv[-1]=0.052) | **✗** |
| **VYPOCET-12** [400..1800] | 30 | −0.198 ± 0.092 | 2.15 | ✓ | ✓ | ✓ |
| **VYPOCET-12** [400..1800] | 50 | −0.224 ± 0.069 | 3.25 | ✓ | ✓ | ✓ |

Bootstrap 68% CI sklonu (2000 resamplů přes seedy) při vysokém počtu seedů **vylučuje nulu** na obou gridech: NOVÝ grid [−0.45, −0.31], VYPOCET-12 grid [−0.30, −0.15].

### Výklad

1. **Počet seedů JE skutečný hybatel** — na původním gridu: 8 seedů t=1.48 (nesignifikantní, reprodukuje nulu VYPOCET-12), 30 seedů t=2.15 (těsně překračuje), 50 seedů t=3.25 (jednoznačně signifikantní). To je **poctivý seed-count upgrade na témž gridu** — ne artefakt.
2. **NOVÝ grid nafukuje signifikanci při nízkém počtu seedů** (8 seedů → t=5.37), protože začíná u N=300 s velkým CV (~0.10) a je více log-uniformní, což dává čistší monotónní pokles a menší reziduální SE. Číslo „8 seedů" z nového gridu proto NENÍ srovnatelné s VYPOCET-12 a nesmí se přeceňovat.
3. Self-averaging je robustně potvrzen: `cv_trunc[-1]` ~ 0.03–0.05 (faktorové, malé fluktuace) a sklon je vždy záporný.

**Rozhodovací kritérium (robustní):** proxy3 se počítá jako signifikantní jen je-li signifikantní při vysokém počtu seedů na OBOU gridech. To je splněno. Poctivým rozhodovatelem je dvojice na VYPOCET-12 gridu, kde 8 seedů bylo nesignifikantních a vysoký počet seedů je skutečný test.

---

## Re-potvrzení proxy1 a proxy2 při vysokém počtu seedů (50)

| Proxy | metrika | hodnota | verdikt III→II |
|---|---|---|---|
| **1 — entropická stopa** | a_full / a_trunc | 1.091 / 0.146 | ✓ (objemový → saturující) |
| **2 — modulární pile-up** | exp_full / exp_trunc | 1.198 / 0.000 | ✓ (hustý → ostrá IR hrana) |

Obě rozhodující proxy zůstávají stabilní a jednoznačné při 50 seedech (konzistentní s VYPOCET-12: a_full≈1.04, exp_full≈1.14).

---

## VERDIKT

> ### **2D diamant je nyní 3/3** — proxy3 (self-averaging) je při vysokém počtu seedů SIGNIFIKANTNÍ na novém i původním gridu; diamant prochází všemi třemi proxy.

**Klíčová výhrada (zachována poctivě):** na původním VYPOCET-12 gridu byla proxy3 při 8 seedech NEsignifikantní (t=1.48) a signifikance přišla až s počtem seedů (50 seedů t=3.25) — to je skutečný seed-count upgrade. Nový 5-bodový grid nafukuje nízko-seedový t-stat, takže headline je **shoda při vysokém počtu seedů napříč dvěma gridy**, NIKOLIV nové-gridové 8-seedové číslo. Tento výpočet je přesně follow-up navržený v BRAINSTORM-05 (priorita #6: „Proxy 3 vN typ s 30–50 seedy … při 5–8 seedech nesignifikantní napříč VYPOCET-12/16/19"). Výsledek tu poznámku **upřesňuje, nevyvrací**: u 8 seedů na původním gridu byla proxy3 skutečně nerozhodnutá (genuinní nula při daném počtu seedů), teprve ≥30 seedů ji rozliší.

### Dopad na nálezy

- **F-015 (2D diamant):** status `supported` zůstává; verdikt se posouvá z **2/3 → 3/3** s tím, že rozhodnutí proxy3 vyžaduje ≥30 seedů (8 nestačí). Caveat „měříme N-trendy, ne typ" trvá: na konečné kauzální množině je každá algebra triviálně typu I_n; self-averaging je signatura **faktoriality (triviální centrum)**, ne přímé měření typu II.
- **F-019 (4D slab):** beze změny (tam byly tři procházející proxy entropická-stopa + modulární-spektrum + rank-scaling; proxy centrálních sekvencí nebyla mezi nimi). VYPOCET-28 ukazuje, že self-averaging proxy lze v 2D dotáhnout k signifikanci — re-run ve 4D slabu při ≥30 seedech je přirozený levný follow-up, ne ovšem nutný pro F-019.
- **F-023 (2D de Sitter):** tam byla proxy3 nesignifikantní při 5 seedech; analogicky lze očekávat, že ≥30 seedů ji vyřeší. To je samostatný follow-up (jiná geometrie, jiný grid); F-023 zatím necháváme 2/3 s touto poznámkou.

Caveat „measuring trends not type" zůstává v platnosti u všech tří nálezů: výsledek je o **N-trendu self-averaging signatury**, ne o přímém určení von-Neumannova typu.

---

## Provozní poznámky

- **Wall-clock:** 1068 s (~17,8 min) na dvojici gridů × 50 seedů × dvou-gridový bootstrap (2000 resamplů). Pod 20min capem, ale těsně — druhý grid zdvojnásobil eigensolve náklady. Single-gridová varianta (50 seedů) běží ~12 min.
- **Schéma/atomicita:** `results.json` zapisováno atomicky (temp + `os.replace`) s polem `status` (`running` → `complete`); přerušení by zanechalo validní částečný výstup.
- **Přenositelnost:** cesty odvozeny `__file__`-relativně; `lib/` na `sys.path` přes `os.path.normpath(...)`. Žádná machine-absolutní cesta.
- **Reprodukce:** `vn-type-proxy3-seeds` NENÍ v `SLOW_CALCS` v `test_reproduction.py` (nový experiment, nezasahuje committed baseline VYPOCET-12). Pro re-run: `PYTHONPATH=lib MPLBACKEND=Agg python3 core-data/calculations/vn-type-proxy3-seeds/calc.py`.

---

## Reference

- **1611.10281** — Sorkin, Yazdi: SSEE, dvojitá truncace, W_O v = μ iΔ_O v.
- **1712.04227** — causet SSEE, κ = √N/(4π) magnitudový cutoff.
- **2206.10780** — Chandrasekaran-Longo-Penington-Witten: crossed-product, III₁ → II.
- VYPOCET-12 (`sj-vn-type`) — původní tříproxy baterie 2D diamantu (2/3).
- BRAINSTORM-05 (priorita #6) — návrh re-runu proxy3 s 30–50 seedy (dorozhodnutí F-015/F-019/F-023).
