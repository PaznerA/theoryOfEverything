# VYPOCET-08: SJ stav na ekvatoriálním řezu Kerrovy černé díry — BTZ signatury jako geometricky-nezávislé vlastnosti

**Datum:** 2026-06-06
**Soubory:** `core-data/calculations/sj-kerr-equatorial/calc.py`, `results.json`, `plots/{sprinkle_cones,cone_tilt_radial,correlation_asymmetry,sj_existence_spectrum}.png`
**Status:** Dokončeno (replikační/rozšiřující sonda k VYPOCET-05)
**Hypotéza:** H02 — SJ stav na Kerrově prostoročase, **Strategie II** (`knowledge-base/hypotezy/H02-sj-kerr.md`)
**Návaznost:** Přímé rozšíření VYPOCET-05 (rotující BTZ, AdS) na **asymptoticky plochý Kerr**. Stejná 2D konformní páka, stejné pozorovatelné, jiná geometrie.

---

## Cíl

VYPOCET-05 ukázal čtyři signatury SJ stavu na rotujícím (AdS) BTZ pozadí. Otázka: jsou to **vlastnosti BTZ geometrie**, nebo **geometricky-nezávislé vlastnosti SJ stavů v rotujících prostoročasech**? Tento výpočet je testuje na zcela odlišném pozadí — **asymptoticky plochém Kerrovi** v ekvatoriální rovině — s identickou metodikou.

Konkrétní měřené otázky (zrcadlo VYPOCET-05):

1. **Existence.** Lze SJ stav zkonstruovat na ekvatoriálním pevném-`r` řezu `(t,φ)` **uvnitř ergoregionu** Kerra (`r_+ < r < 2M`), kde je `∂_t` prostorupodobný? Kontrola Lorentzovskosti řezu, ± párování spektra `iΔ`.
2. **Radiální profil `f_co` a `A_caus`.** Sken přes `r`: prochází vnitřní nulový sklon nulou **přesně na ergosféře** `r_erg = 2M` (jako v BTZ na `√M`)?
3. **Znaménko `A_W` vs. `A_caus`.** Replikuje se **OPAČNÉ-ZNAMÉNKO** z BTZ (`A_caus > 0`, ale `A_W < 0`)?
4. **Závislost na `a`.** `A_caus(r=1.5)` pro `a ∈ {0.3, 0.6, 0.9}`, plus srovnatelný sken na `r=2.5`.

---

## Metoda

### Páka: konformní trivialita 2D bezhmotného skaláru (identicky jako VYPOCET-05)

Pro **bezhmotný** skalár v **libovolném** 2D prostoročase je retardovaná Greenova funkce na kauzální množině `G_R = (1/2) C`, kde `C_xy = 1` právě když `y` předchází `x`. Důvod: každá 2D Lorentzova metrika je lokálně konformně plochá, 2D bezhmotný vlnový operátor je konformně invariantní (`ξ=0` JE minimální vazba v `d=2`), takže `G_R` závisí jen na kauzální struktuře, ne na konformním faktoru. Křivost, strhávání souřadnic i ergoregion vstupují **výhradně** přes naklonění světelných kuželů. (Sorkin–Yazdi 1611.10281 eq. 9; masivní limita `m→0` z 1701.07212; zakřivená 2D AdS₂ explicitně v 2504.12919.)

### Geometrie: ekvatoriální Kerr v Boyer-Lindquistových souřadnicích (ověřeno)

Kerr, geometrizované jednotky `G=c=1`, hmota `M`, spin `a` (`|a|≤M`):
```
Σ = r² + a² cos²θ,   Δ = r² - 2Mr + a².
```
V ekvatoriální rovině `θ = π/2`: `Σ = r²`. Indukovaná pevné-`r` metrika `(t,φ)`:
```
g_tt    = -(1 - 2M/r)
g_tφ    = -2Ma/r          (NA ROZDÍL od BTZ je r-závislé!)
g_φφ    = r² + a² + 2Ma²/r
g_rr    = r²/Δ = Σ/Δ
```
Složky ověřeny proti standardní literatuře (Wikipedia „Kerr metric", ekvatoriální tvar; konzistentní s Ali-Haïmoud GR lecture notes).

**Klíčový přesný fakt (sympy):**
```
det h = g_tt g_φφ - g_tφ² = -(r² - 2Mr + a²) = -Δ.
```
Vně vnějšího horizontu (`Δ > 0`) je `det h < 0`: pevné-`r` řez `(t,φ)` je **Lorentzův skrz celý ergoregion** — přesně situace BTZ (tam `det h = -N²r²`). Diskriminant nulové kvadratiky: `disc = -4 det h = 4Δ > 0` vně `r_+`.

**Povrchy (ekvátor):**
- vnější horizont `r_+ = M + √(M²-a²)`,
- ergosféra `r_erg = 2M` (statická mez `g_tt=0`; na ekvátoru `cos²θ=0`, takže `r_erg = M + √(M²) = 2M`, **nezávislé na `a`**),
- ergoregion `(r_+, 2M)`. Uvnitř `g_tt > 0`, `∂_t` je **prostorupodobný** — žádný časupodobný Killingův vektor.

### Poctivá geometrická poznámka (skutečný rozdíl od BTZ)

V Kerrovi je ergoregion **tenká slupka** `(r_+, 2M)`. Pro `M=1`:

| `a` | `r_+` | ergoregion | šířka |
|-----|-------|-----------|-------|
| 0.3 | 1.954 | (1.954, 2.0) | 0.046 |
| 0.6 | 1.800 | (1.800, 2.0) | 0.200 |
| 0.9 | 1.436 | (1.436, 2.0) | 0.564 |

Slupka se rozšíří natolik, aby dosáhla daného malého `r`, jen pro velký `a`. Speciálně **`r=1.5` je vně horizontu (Lorentzův) JEN pro `a=0.9`**; pro `a=0.3, 0.6` je `r=1.5` uvnitř horizontu, kde `det h > 0` a řez `(t,φ)` je **Euklidovský** (žádný reálný kužel). To reportujeme poctivě (Část D) a doplňujeme srovnatelný sken na `r=2.5`, kde dají Lorentzův řez **všechny** `a`. Druhý rozdíl od BTZ: `g_tφ` je v Kerrovi **`r`-závislé** (BTZ má konstantní `-J/2`), takže kuželová geometrie se mění i v rámci jediné rodiny řezů.

### SJ pipeline (konvence identické s VYPOCET-04/05)

1. Kauzální uspořádání z naklonených kuželů: `y ≺ x` ⟺ `D=x-y` budoucnostně-kauzální (`h(D,D)≤0` a `h(T,D)<0`, `T=(1, -g_tφ/g_φφ)` = LNRF/nulová moment hybnosti).
2. `C_xy = 1` když `y ≺ x`; `G_R = (1/2)C`; `Δ_PJ = (1/2)(C-Cᵀ)`; `iΔ` hermitovský.
3. SJ Wightman `W = kladná část iΔ`.
4. Pozorovatelné: `A_caus = 2 f_co - 1` (kauzální směrová asymetrie), `A_W` (SJ Wightmanova směrová asymetrie přes tytéž páry).

**Parametry:** `M=1`, `a=0.6` (fiduciální), `a=0.9` (agresivní), `N=1600`, **3 seedy** (101, 202, 303), `T=Φ=1.4`.

---

## Výsledky

### A — SJ existence uvnitř Kerrova ergoregionu (HLAVNÍ VÝSLEDEK)

| Veličina | Kerr `a=0.6`, `r=1.900` UVNITŘ ergo | Kerr `a=0.9`, `r=1.718` UVNITŘ ergo | Statický analog `a=0`, totéž `r` |
|----------|---------------------------------------|---------------------------------------|----------------------------------|
| `g_tt` | **+0.053** (`∂_t` prostorupodobný) | **+0.164** (`∂_t` prostorupodobný) | — |
| Řez Lorentzův? | **Ano** (`det h<0`) | **Ano** | **Ne** (`det h=+0.485>0`, Euklidovský) |
| SJ konstruovatelný? | **Ano** | **Ano** | **Ne** (`r<r_+`, uvnitř Schwarzschildova horizontu) |
| Nulové sklony `dφ/dt` | `(+0.050, +0.240)` OBA kladné | `(+0.102, +0.344)` OBA kladné | — |
| Spektrum `iΔ` | **787+ / 787−** přesných ± párů | **790+ / 790−** | — |
| Párový reziduál (rel.) | **4.7×10⁻¹⁶** | **5.3×10⁻¹⁶** | — |
| `Tr(iΔ)` | 0.0 | −2.3×10⁻¹³ | — |
| `f_co` | **1.000** | **1.000** | — |
| `A_caus` | **+1.000** | **+1.000** | — |
| `⟨dφ/dt⟩` vs. strhávací sklon | 0.143 vs. 0.145 ✓ | 0.219 vs. 0.223 ✓ | — |

**SJ stav je plně dobře definovaný (strojová přesnost) uvnitř Kerrova ergoregionu**, kde je `∂_t` prostorupodobný — a matchovaný statický (Schwarzschildův) řez při témže `r` (uvnitř horizontu `r_+=2M`) **není ani Lorentzův**. Identický výsledek jako rotující BTZ ve VYPOCET-05.

### B — Radiální profil přes ergosféru: nulový sklon prochází nulou přesně na `r_erg=2M`

Sken `a=0.6` (3 seedy, výběr řádků):

| `r` | v ergo | `g_tt` | sklon− | sklon+ | `f_co` | `A_caus` | `A_W` |
|-----|--------|--------|--------|--------|--------|----------|-------|
| 1.809 | ano | +0.106 | +0.135 | +0.194 | 1.000 | +1.000 | N/A |
| 1.897 | ano | +0.054 | +0.052 | +0.239 | 1.000 | +1.000 | N/A |
| 1.990 | ano | +0.005 | +0.004 | +0.253 | 1.000 | +1.000 | N/A |
| **2.000** | **ne** | **−0.000** | **0.000** | +0.254 | 1.000 | +1.000 | N/A |
| 2.005 | ne | −0.002 | **−0.002** | +0.255 | 0.991 | +0.982 | **−0.667** |
| 2.171 | ne | −0.079 | −0.056 | +0.261 | 0.814 | +0.628 | −0.502 |
| 2.514 | ne | −0.205 | −0.116 | +0.253 | 0.677 | +0.354 | −0.326 |
| 3.200 | ne | −0.375 | −0.155 | +0.224 | 0.587 | +0.173 | −0.170 |

**Interní nulový sklon `s_-` prochází nulou PŘESNĚ na `r=2.0 = r_erg = 2M`** (lineární interpolace dává `2.0000` pro `a=0.6` i `a=0.9`) — Kerrův analog BTZ přechodu na `√M`. Uvnitř ergoregionu je kužel **plně stržen** (`f_co=1`, `A_caus=+1`, oba nulové sklony kladné); vně asymetrie hladce klesá jako strhávání `~1/r²` (učebnicová superradiantní hrana). Plot `cone_tilt_radial.png` ukazuje křížení s ⭐ na `r=2M` pro oba spiny.

### C — `A_W` vs. `A_caus`: OPAČNÉ ZNAMÉNKO replikuje

| `a` | `r` | poloha | `A_caus` | `A_W` | opačné znaménko? |
|-----|-----|--------|----------|-------|-------------------|
| 0.6 | 2.2 | těsně vně ergo | +0.591 ± 0.001 | **−0.482** | **ano** |
| 0.6 | 2.6 | vně | +0.317 ± 0.002 | **−0.296** | **ano** |
| 0.6 | 3.2 | daleko | +0.173 ± 0.003 | **−0.170** | **ano** |
| 0.9 | 2.2 | těsně vně ergo | +0.714 ± 0.001 | **−0.545** | **ano** |
| 0.9 | 2.6 | vně | +0.431 ± 0.001 | **−0.382** | **ano** |
| 0.9 | 3.2 | daleko | +0.248 ± 0.002 | **−0.237** | **ano** |
| **0 (stat.)** | 2.6 | kontrola | +0.001 ± 0.003 | +0.000 | — (≈0) |

**Opačné-znaménko BTZ jevu se plně replikuje:** kauzálně-početní asymetrie je kladná (více spojů co-rotuje), ale SJ-korelační asymetrie je záporná (na spoj jsou korelace silnější proti-rotujícně) — pro **každé** `a`, **každý** `r` vně ergoregionu. Statická kontrola (`a=0`) sedí přesně na nule v obou. Toto byl ve VYPOCET-05 nejméně očekávaný nález; jeho replikace na zcela jiné (ploché) geometrii ho povyšuje z artefaktu BTZ na **vlastnost SJ vakua ve strženém prostoročase**.

### D — Závislost na spinu `a`

**`r=1.5` (přímý dotaz zadání):**

| `a` | `r_+` | řez na `r=1.5` | `A_caus` |
|-----|-------|------------------|----------|
| 0.3 | 1.954 | **Euklidovský** (uvnitř horizontu, `det h=+0.66>0`) | nedefinováno |
| 0.6 | 1.800 | **Euklidovský** (uvnitř horizontu, `det h=+0.39>0`) | nedefinováno |
| 0.9 | 1.436 | **Lorentzův** (uvnitř ergoregionu!) | **+1.000** |

Pro `a=0.9` je `r=1.5` uvnitř ergoregionu (`1.436 < 1.5 < 2.0`), takže `A_caus = +1` (plně stržený). Pro `a=0.3, 0.6` je `r=1.5` uvnitř horizontu — řez je Euklidovský, SJ nedefinovaný. **To není chyba, ale geometrie: Kerrova ergo-slupka je tenká.**

**`r=2.5` (srovnatelný sken, všechna `a` Lorentzova):**

| `a` | `A_caus` | `A_W` | `f_co` | strhávací sklon |
|-----|----------|-------|--------|------------------|
| 0.3 | +0.197 ± 0.003 | −0.190 | 0.598 | 0.037 |
| 0.6 | +0.361 ± 0.001 | −0.332 | 0.681 | 0.070 |
| 0.9 | +0.482 ± 0.001 | −0.418 | 0.741 | 0.093 |

`A_caus` **roste monotónně se spinem `a`** (a `A_W` symetricky klesá; opačné znaménko platí pro všechna `a`). Strhávací sklon roste přibližně lineárně s `a`, jak má. Plot `correlation_asymmetry.png` (pravý panel).

---

## Interpretace pro hypotézu H02

1. **BTZ signatury jsou geometricky nezávislé.** Všechny čtyři nálezy VYPOCET-05 se replikují na asymptoticky plochém Kerrovi:
   - existence SJ uvnitř ergoregionu (strojově přesné ± párování, `g_tt>0`), zatímco statický analog degeneruje;
   - `f_co → 1`, `A_caus → +1` uvnitř ergoregionu, vnitřní nulový sklon nuluje **přesně na `r_erg`** (`√M` v BTZ ↔ `2M` v Kerrovi);
   - **opačné znaménko** `A_caus > 0` vs. `A_W < 0`;
   - monotónní růst asymetrie se spinem.

   Tyto signatury tedy nezávisí na asymptotice (AdS vs. plochá), na hodnotě křivosti, ani na tom, zda je `g_tφ` konstantní (BTZ) či `r`-závislé (Kerr). Jsou to **vlastnosti SJ stavu řízené pouze kauzální/konformní strukturou strženého řezu** — přesně to, co konformní páka předpovídá.

2. **Teze H02 potvrzena na druhém pozadí.** SJ konstrukce nikdy nepotřebuje časupodobný Killingův vektor; projde čistě uvnitř ergoregionu, kde stacionární vakua nemají analog. Kerr to ukazuje stejně čistě jako BTZ.

3. **Most ke 4D Strategii I/III.** Stejně jako v BTZ: rotace nesedí v **bulk spektru** `iΔ` (konformní třída), ale v **eigenvektorech / dvoubodové funkci** `W` (kde žijí směrové asymetrie a opačné znaménko). Robustnost opačného znaménka napříč dvěma geometriemi naznačuje, že ve 4D Kerrovi (kde `G_R ≠ (1/2)C`) bude superradiantní otisk SJ stavu rovněž ve struktuře `W`, nikoli v hrubém spektru — užitečný cíl pro plný Teukolskyho výpočet.

---

## Limity výpočtu

- **Pouze 2D ekvatoriální řez, bezhmotný skalár.** Strategie II (2D analog), ne 4D Kerrův výsledek. 4D (`G_R ≠ ½C`, prostoročas není konformně triviální) zůstává otevřený.
- **Pevné-`r` řez má uniformní kužely** (konstantní indukovaná 2-metrika). `r`-závislost zkoumáme skenem oddělených pevných-`r` oblastí (Část B/C/D), ne jedinou 2D oblastí pokrývající `r`. Oblast pokrývající `r` skrz ergoregion by byla 3D (`φ` nelze vypustit — pevné-`φ` `(t,r)` řez je uvnitř ergoregionu Euklidovský, stejně jako v BTZ).
- **Tenká ergo-slupka Kerra.** Na rozdíl od BTZ je `(r_+, 2M)` úzká pro malý `a`; `r=1.5` je Lorentzův jen pro `a=0.9`. Reportujeme poctivě a doplňujeme srovnatelný `r=2.5` sken.
- **Konečné `φ`-okno, ne plný válec** (kauzální obdélník `(t,φ)∈[0,T]×[0,Φ]`, vyhýbáme se periodické identifikaci). `∂_φ` je vždy prostorupodobný (`g_φφ>0` vně `r_+`), takže CTC z `φ`-kružnic nehrozí.
- **Fixní N** (kanonická aproximace), 3 seedy. Pro směrové asymetrie a existenci je rozdíl `O(1/√N)` zanedbatelný (statistické chyby `A_caus` ~ 0.001–0.003).
- **`A_W` uvnitř ergoregionu nedefinováno** (`n_cc=0`, žádné proti-rotující spoje) — korektní, ne chyba; odráží plné stržení. Stává se definovaným přesně při překročení `r_erg=2M`.
- **Hadamardovskost neřešena** (SJ stavy obecně nejsou Hadamardovské; měříme existenci a směrové signatury, ne UV strukturu).

---

## Citace (prohledané/použité)

- **Kerrova ekvatoriální metrika** (`g_tt=-(1-2M/r)`, `g_tφ=-2Ma/r`, `g_φφ=r²+a²+2Ma²/r`, `r_+=M+√(M²-a²)`, `r_erg=2M` na ekvátoru) — ověřeno proti Wikipedia „Kerr metric" a standardním GR poznámkám; `det h = -Δ` ověřeno symbolicky (sympy)
- **1611.10281** — Sorkin, Yazdi (`G_R=½C`, `iΔ`, SJ W = kladná část)
- **1701.07212, 1712.04227** — masivní `G_R`, limita `m→0`
- **2504.12919** — konformní plochost ⇒ `½C` v zakřivené 2D (AdS₂)
- **1208.2422** — Afshordi-Aslanbeigi-Sorkin (SJ kontinuum)
- **H02-sj-kerr.md** (tento projekt) — Strategie II
- **VYPOCET-05** (sj-rotating-btz) — replikované BTZ signatury, zděděné konvence
- **VYPOCET-04** (ssee-diamond) — zděděný SJ toolchain
