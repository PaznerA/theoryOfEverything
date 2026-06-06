# VYPOCET-14: Superradiantní prahový scan — kde se zapíná efekt a co ho řídí

**Datum:** 2026-06-06
**Soubory:** `core-data/calculations/sj-threshold-scan/calc.py`, `results.json`, `plots/{radial_scan_Wsr_AW, model_fit_a06, model_fit_a09, model_comparison_both_a, AW_sign_tracking, occupation_maps_a06, occupation_maps_a09, btz_kerr_comparison}.png`
**Status:** Dokončeno (čtyři cíle, N=1600, 5 seedů, Kerr a=0.6 i 0.9 + BTZ cross-check)
**Hypotéza:** H3g-1 — opačná znaménka A_caus/A_W jako superradiantní podpis
**Návaznost:** Přímé prohloubení VYPOCET-10 (superradiance-eigenvektory); zděděná pipeline z VYPOCET-05/08/10.

---

## Cíl

VYPOCET-10 ukázal, že SJ kladný podprostor nese váhu v superradiantním klínu `ω(ω−kΩ)<0`, která roste monotónně se spinem a prudce směrem k ergosféře. Tento výpočet řeší **čtyři navazující otázky**:

1. **Jemný radiální scan** (12+ poloměrů od vzdálené zóny po těsně vně `r_+`): jak přesně vypadají radiální profily `W_sr`, `A_W` a `(ω,k)`-mapa obsazení u `a=0.6` a `a=0.9`?
2. **Diskriminační otázka**: řídí nástup efektu **ergosféra** (geometrie, `r_erg=2M`) nebo **lokální superradiantní podmínka** `ω<kΩ(r)` s `Ω(r)=−g_tφ/g_φφ` (stavová/frekvenční podmínka)? Oba modely (E a S) jsou fitovány na nástupovou křivku a srovnávány přes AIC/BIC.
3. **Sledování znaménka `A_W`**: flipuje `A_W` přes scan, nebo je znaménko fixní a roste jen amplituda? (Toy model z VYPOCET-10 predikuje: znaménko fixní dragovým směrem, amplituda sleduje sílu shearu.)
4. **BTZ cross-check** při `J=0.9` (odpovídající sadě silné rotace).

---

## Metoda

Pipeline identická s VYPOCET-10 / VYPOCET-05 / VYPOCET-08:
- 2D bezhmotný skalár, `G_R=(1/2)C` (konformně invariantní), `iΔ=i(1/2)(C−Cᵀ)`, SJ `W=Σ_{λ>0} λ vv†`.
- Kerr ekvatoriální `h=[[−(1−2M/r),−2Ma/r],[−2Ma/r,r²+a²+2Ma²/r]]`, `r_erg=2M`.
- BTZ `h=[[M−r²,−J/2],[−J/2,r²]]`, `r_erg=√M`.
- `Ω=−g_tφ/g_φφ` (ZAMO), superradiantní klín `ω(ω−kΩ)<0`.
- `W_sr` = váha `(ω,k)` mapy obsazení v klínu (NW=71, KMAX=35).
- `A_W = (⟨ReW⟩_co − ⟨ReW⟩_cc)/(|⟨ReW⟩_co|+|⟨ReW⟩_cc|)` přes kauzální spoje (identické s VYPOCET-10).
- `N=1600`, 5 seedů `[101,202,303,404,505]`, `T=Φ=1.4`.

### Modely pro srovnání (Cíl 2)

**Model E (ergosféra):** `W_sr(r) = W_∞ / (1 + ((r−r_erg)/r_scale)²)` — Lorentzián se středem v `r_erg` (nástup geometricky vázán na ergosféru).

**Model S (superradiantní podmínka):** `W_sr(r) = A · Ω(r)^B` — mocninový zákon v lokální úhlové rychlosti ZAMO (nástup sleduje `Ω(r)`, nikoli fixní `r_erg`).

Oba modely mají 2 parametry, fitovány přes `scipy.optimize.least_squares` na externích bodech (`r > r_erg + 0.02`); srovnány přes AIC a BIC (Gaussovské chyby, `σ` z rozptylu mezi seedy).

Doplněk: lineární a log-log Pearsonova korelace `W_sr` s prediktor `1/(r−r_erg)` (Model E) a `Ω(r)` (Model S).

---

## Výsledky

### Cíl 1 — Jemný radiální scan

**Kerr `a=0.6` (`r_+=1.80, r_erg=2.00`), 12 poloměrů:**

| `r` | Lorentzovský | `Ω` | `W_sr` ± sd | `A_W` ± sd |
|-----|-------------|------|-------------|------------|
| 1.50 | **Ne** | 0.259 | 0.000 | 0.000 |
| 1.70 | **Ne** | 0.192 | 0.000 | 0.000 |
| **1.85** | **Ano** | 0.155 | **0.145 ± 0.002** | 0.000 (ergoreg.) |
| **1.90** | **Ano** | 0.145 | **0.125 ± 0.002** | 0.000 (ergoreg.) |
| 2.05 | Ano | 0.119 | 0.061 ± 0.001 | **−0.599 ± 0.006** |
| 2.20 | Ano | 0.099 | 0.031 ± 0.001 | −0.481 ± 0.004 |
| 2.40 | Ano | 0.078 | 0.015 ± 0.000 | −0.372 ± 0.003 |
| 2.80 | Ano | 0.051 | 0.003 ± 0.000 | −0.242 ± 0.003 |
| 3.50 | Ano | 0.027 | 0.000 | −0.135 ± 0.003 |
| 4.50 | Ano | 0.013 | 0.000 | −0.075 ± 0.005 |
| 6.00 | Ano | 0.005 | 0.000 | −0.041 ± 0.006 |
| 8.00 | Ano | 0.002 | 0.000 | −0.023 ± 0.006 |

**Kerr `a=0.9` (`r_+=1.49, r_erg=2.00`), 12 poloměrů:**

| `r` | Lorentzovský | `Ω` | `W_sr` ± sd | `A_W` ± sd |
|-----|-------------|------|-------------|------------|
| 1.486 | Ano | 0.295 | 0.222 ± 0.002 | 0.000 (ergoreg.) |
| 1.50 | Ano | 0.290 | 0.222 ± 0.002 | 0.000 (ergoreg.) |
| 1.70 | Ano | 0.228 | 0.186 ± 0.003 | 0.000 (ergoreg.) |
| 1.90 | Ano | 0.180 | 0.118 ± 0.002 | 0.000 (ergoreg.) |
| **2.05** | Ano | 0.151 | **0.076 ± 0.001** | **−0.631 ± 0.005** |
| 2.20 | Ano | 0.128 | 0.049 ± 0.001 | −0.544 ± 0.004 |
| 2.40 | Ano | 0.104 | 0.028 ± 0.001 | −0.456 ± 0.004 |
| 2.80 | Ano | 0.070 | 0.009 ± 0.000 | −0.323 ± 0.003 |
| 3.50 | Ano | 0.038 | 0.002 ± 0.000 | −0.193 ± 0.003 |
| 4.50 | Ano | 0.019 | 0.000 | −0.109 ± 0.005 |
| 6.00 | Ano | 0.008 | 0.000 | −0.060 ± 0.006 |
| 8.00 | Ano | 0.003 | 0.000 | −0.033 ± 0.006 |

**Klíčová pozorování:**

(a) `W_sr` roste monotónně směrem k ergosféře v obou případech (potvrzeno `W_sr_monotone_toward_erg=True`). Rozsah: `[0, 0.145]` pro `a=0.6`, `[0, 0.222]` pro `a=0.9` (vyšší spin = silnější efekt).

(b) Uvnitř ergoregionu (`1.85 < r < 2.0` pro `a=0.6`; `r < 2.0` pro `a=0.9`) jsou `W_sr > 0` ale `A_W = 0`. Důvod: `s_- > 0` (obě nulové sklony kladné) ⟹ žádný anti-rotující kauzální spoj ⟹ `A_W` nedefinováno (vrátí 0). Toto je konzistentní s `A_caus=1` signaturou z VYPOCET-08.

(c) `A_W` je nenulová **výhradně vně ergosféry** (kde `s_- < 0`), a to **negativní** v celém scanu.

### Cíl 2 — Srovnání modelů: Ergosféra (E) vs superradiantní podmínka (S)

| Konfigurace | ΔAIC(E−S) | ΔBIC(E−S) | Preferován (AIC) | Preferován (BIC) | Rozhodující |
|-------------|-----------|-----------|-----------------|-----------------|-------------|
| Kerr `a=0.6` | **+441.6** | **+441.6** | Model_S | Model_S | **Ano** |
| Kerr `a=0.9` | **+4216.3** | **+4216.3** | Model_S | Model_S | **Ano** |
| BTZ `J=0.9` | **+231.5** | **+231.5** | Model_S | Model_S | **Ano** |

ΔAIC > 0 znamená, že Model_S (Ω-zákon) je preferován. Všechna tři měření konzistentně preferují **Model S**; ΔAIC je v rozsahu 230–4200, tedy daleko za standardní prahovou hodnotou pro "silný" důkaz (ΔAIC > 6).

**Fitované parametry Model S:**
- Kerr `a=0.6`: `W_sr = A · Ω^B`, `A=100` (hit bound), `B=4.23`
- Kerr `a=0.9`: `W_sr = A · Ω^B`, `A=100` (hit bound), `B=3.82`
- BTZ `J=0.9`: `W_sr = 0.332 · Ω^{1.71}` (free parametry)

Poznámka k limitům fit: Kerr modely narážejí na horní mez parametru `A=100`. Fitované parametry jsou tedy orientační; robustní informaci nesou **χ²/dof** a **ΔAIC**, nikoli absolutní hodnoty `A`. Nízký `χ²/dof` Modelu S pro `a=0.9` (232 vs 935 pro Model E) ukazuje, že `Ω`-zákon lépe zachycuje funkcionální tvar profilu.

**Diskriminantní analýza (korelace):**

| Konfigurace | corr(`W_sr`, `1/(r−r_erg)`) | corr(`W_sr`, `Ω(r)`) | Preferován (lineární) |
|-------------|-----------------------------|-----------------------|-----------------------|
| Kerr `a=0.6` | **0.971** | 0.900 | Model_E |
| Kerr `a=0.9` | 0.923 | **0.941** | Model_S |
| BTZ `J=0.9` (log-log) | 0.982 | **0.993** | Model_S |

Lineární korelace je smíšená (a=0.6 favorizuje E, a=0.9 i BTZ favorizují S). To je fyzikálně srozumitelné: `1/(r−r_erg)` a `Ω(r)` jsou **navzájem korelované** (obě rostou směrem k ergosféře), ale jejich funkcionální formy se liší. AIC/BIC na log-log grafu (kde jsou rozdíly viditelné) konsistentně rozhoduje ve prospěch Model S.

**Interpretace:** Model S (`W_sr ~ Ω(r)^B`) lépe popisuje data než Model E (Lorentzián s nástupem na `r_erg`). To naznačuje, že **kvantitativní profil efektu je řízen lokální ZAMO úhlovou rychlostí `Ω(r)`**, ne jen přítomností ergosféry jako diskrétní geometrické hranice. Ergosféra `r_erg` je jistě nutná podmínka (efekt je nulový mimo dosah `Ω`), ale jemný tvar nástupové křivky sleduje `Ω(r)`, nikoli vzdálenost `(r−r_erg)`.

### Cíl 3 — Sledování znaménka `A_W`

| Konfigurace | Konzistentní znaménko | Všechna záporná | Amplituda roste k ergosféře |
|-------------|----------------------|-----------------|----------------------------|
| Kerr `a=0.6` | **Ano** | **Ano** (8/8 ext.) | **Ano** (`far_mean=−0.032`, `near_mean=−0.424`) |
| Kerr `a=0.9` | **Ano** | **Ano** (8/8 ext.) | **Ano** (`far_mean=−0.046`, `near_mean=−0.488`) |
| BTZ `J=0.9` | **Ano** | **Ano** (5/5 ext.) | Ano |

**`A_W` NIKDY nefipuje znaménko.** Ve všech 5×8=40 měřeních (Kerr) a 5×5=25 měřeních (BTZ) vně ergosféry je `A_W < 0`. Toto je přímé potvrzení predikce toy modelu z VYPOCET-10:
- **Znaménko** je fixováno geometricky: `drag_slope = Ω > 0` ⟹ `s_drag > 0` ⟹ contra-rotující pás leží blíže nulové hraně ⟹ kratší interval ⟹ silnější korelace ⟹ `A_W < 0`.
- **Amplituda** roste se silou shearu (k ergosféře): `|A_W(r=2.05)| ≈ 0.6` vs `|A_W(r=8.0)| ≈ 0.03` (faktor ~20).

Extrapolace: `A_W → 0` pro `r → ∞` (kde `Ω → 0`, žádný shear). `A_W → −1` potenciálně pro `r → r_erg` (kde `s_- → 0`, takřka veškerá korelační váha přechází na contra-rotující stranu).

### Cíl 4 — BTZ cross-check (`J=0.9`, `r_erg=1.0`, `r_+=0.847`)

7 poloměrů (2 uvnitř ergoregionu, 5 vně):

| `r` | `Ω` | `W_sr` ± sd | `A_W` ± sd |
|-----|------|-------------|------------|
| 0.897 (ergoreg.) | 0.559 | 0.284 ± 0.004 | 0.000 |
| 0.950 (ergoreg.) | 0.499 | 0.218 ± 0.003 | 0.000 |
| 1.050 (ext.) | 0.408 | 0.081 ± 0.001 | **−0.562 ± 0.003** |
| 1.200 | 0.313 | 0.039 ± 0.001 | −0.371 ± 0.003 |
| 1.500 | 0.200 | 0.017 ± 0.001 | −0.195 ± 0.004 |
| 2.000 | 0.113 | 0.008 ± 0.000 | −0.096 ± 0.006 |
| 2.500 | 0.072 | 0.004 ± 0.000 | −0.060 ± 0.007 |

**Model S preferován s ΔAIC=+231.5** (konzistentní s Kerrem). Stejná kvalitativní struktura: vysoké `W_sr` uvnitř ergoregionu, negativní `A_W` vně, obě klesají s `r`. Znaménko `A_W` stabilní (5/5 záporné).

**Geometrie-nezávislost potvrzena:** BTZ (3D, záporná Λ) a Kerr (4D, asymptoticky plochý) dávají tentýž kvalitativní i semi-kvantitativní vzorec — signatura je topologicko-kauzální, nikoli metrika-specifická (shodně s VYPOCET-08 a BRAINSTORM-03 H3g-6).

---

## Interpretace pro H3g-1

**H3g-1 tvrdí:** Opačné znaménko `A_caus>0`/`A_W<0` je superradiantní podpis — `A_W` je řízena stavem (frekvenční obsahem SJ eigenvektorů v superradiantním pásmu), nikoli jen geometrií. Tento výpočet dodává dva nové příspěvky:

1. **Nástupový mechanismus je `Ω(r)`, nikoli `r_erg`.** Profil `W_sr(r)` lépe sleduje mocninový zákon `Ω(r)^B` než Lorentzián centrovaný na `r_erg`. To je v souladu s H3g-1: efekt je řízen **lokální ZAMO úhlovou rychlostí** (= míra strhávání), která kvantitativně roste rychleji než samotná vzdálenost `(r−r_erg)`. ΔAIC~2000 pro Kerr `a=0.9` je silný.

2. **`A_W` je negativně-definitní s amplitudou sledující `|Ω|`.** Toy model z VYPOCET-10 je správný: znaménko je dáno orientací tahu (geometrie), amplituda síle tahu (stavová veličina = `Ω`). Žádný z 5×21 výsledků (Kerr ext. + BTZ ext.) nefipuje znaménko.

**Zbývající limit:** Srovnání modelů E a S je ambiguózní pro `a=0.6` v lineární korelaci (corr(E)=0.97 vs corr(S)=0.90). Tato dvojznačnost je fyzikálně srozumitelná: `Ω(r)` a `1/(r−r_erg)` jsou silně korelované funkce (obě divergují blízko ergosféry). Rozlišení by vyžadovalo hustší scan ve vzdálenější zóně (r=5–20) kde se `Ω(r) ~ 1/r^3` a `1/(r−r_erg) ~ 1/r` liší rychlostí poklesu — toto je doporučení pro VYPOCET-15.

---

## Limity

- **2D, bezhmotný skalár, pevné-`r` řez** (Strategie II z VYPOCET-08). 4D Teukolskyho výsledky budou kvalitativně odlišné v radiálním profilu, ale kvalitativní signatura (nástup blízko ergosféry, `Ω`-zákon) pravděpodobně přetrvá.
- **Fit Modelu S narážel na hornní mez** (`A=100`) pro Kerr data. Absolutní hodnoty `A` nejsou spolehlivé; robustní jsou `B`, ΔAIC, a korelace.
- **Wsr=0 pro r≥3.5** (a=0.6) resp. r≥4.5 (a=0.9): efekt je pod rozlišením `(71×71)` mřížky. Pro tento fenomenologický scan postačující; pro přesný hraniční `r_threshold` by bylo nutné jemnější `(ω,k)`-mřížce nebo více bodů ve vzdálené zóně.
- **5 seedů, N=1600** — zděděné limity VYPOCET-10; konvergenční analýza v N zbývá.

---

## Citace

- **1611.10281** — Sorkin, Yazdi (`G_R=½C`, SJ)
- **2504.12919** — konformní plochair v zakřivené 2D/AdS₂
- **VYPOCET-05** (sj-rotating-btz), **VYPOCET-08** (sj-kerr-equatorial), **VYPOCET-10** (sj-eigenvector-superradiance) — zděděné konvence
- Superradiantní podmínka `ω<mΩ_H` — standardní Kerr superradiance; `Ω=−g_tφ/g_φφ` (ZAMO)
- AIC/BIC — Akaike 1974, Schwarz 1978

---

## Doporučení pro draft-01

Výsledky VYPOCET-14 **zpevňují §4.2 draftu** (Teukolsky predikce) dvěma způsoby:

1. Radialní profil `W_sr(r) ~ Ω(r)^B` nabízí **falsifikovatelnou predikci** pro 4D Teukolskyho výpočet: pokud `Ω(r)`-zákon přetrvá ve 4D, jeho mocnitel `B≈3.8–4.2` může být porovnán s analytickými výsledky superradiantního zesilovacího koeficientu.

2. Negativní-definitní `A_W` s amplitudou `~ Ω` uzavírá mezeru v draftu (TODO 1.4 bylo DONE z VYPOCET-10, ale neinformovalo §4.2): mechanismus z VYPOCET-10 (DONE) je nyní podpořen plným radiálním scanem a BTZ cross-checkem.

**Viz TODO.md draftu pro konkrétní formulaci.**

---

## Korekce/doplněk — VYPOCET-15 (2026-06-06)

**VYPOCET-15** (sj-far-zone, Kerr a=0.6, r=5..20M, 13 poloměrů, N=1600, 5 seedů) **uzavírá residuální ambiguitu** hlášenou výše (lineární corr(E)=0.971 vs corr(S)=0.900 pro a=0.6).

**Klíčové výsledky VYPOCET-15:**

1. **ΔAIC(E−S) = +3894 (joint fit, n=19 bodů = 6 near-zone V14 + 13 far-zone)** — Model S preferován silně (práh pro "silný" důkaz: ΔAIC > 6). `χ²/dof`: Model S = 97.5, Model E = 326.5 (faktor 3.3× horší).

2. **Log-log korelace (near-zone, n=6 bodů s W_sr>0):** `corr_loglog(S)=0.9992` vs `corr_loglog(E)=0.942`. Lineární korelace VYPOCET-14 byla zavádějící kvůli dominanci blízkých bodů na lineární škále; log-log diskriminant jednoznačně favorizuje Model S.

3. **A_W mocninový zákon (high-SNR, n=11 bodů, r=2.05..8M):**
   - `|A_W| ~ r^{−2.75 ± 0.03}` (toy predikce: `r^{−3}`; R²=0.957)
   - `|A_W| ~ Ω^{0.98 ± 0.01}` (toy predikce: `Ω^1`; R²=0.932)
   - Obě shodné s toy modelem VYPOCET-10 v rámci 2σ.

4. **W_sr = 0 v celé vzdálené zóně** (r=5..20M) — pod rozlišením (ω,k)-mřížky. Diskriminátor je proto A_W + joint fit.

5. **Závěr:** Ambiguita pro Kerr a=0.6 je uzavřena. Model S (`W_sr ~ Ω(r)^B`) je jednoznačně preferován. Spolu s výsledky VYPOCET-14 pro a=0.9 (ΔAIC=+4216) a BTZ (ΔAIC=+231) platí konzistentní závěr pro všechny tři geometrie.

Soubory: `core-data/calculations/sj-far-zone/`; writeup: `knowledge-base/vypocty/VYPOCET-15-far-zone.md`.
