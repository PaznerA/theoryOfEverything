# VYPOCET-05: První numerický Sorkin-Johnstonův stav v rotujícím prostoročase (rotující BTZ, ergoregion)

**Datum:** 2026-06-06
**Soubory:** `core-data/calculations/sj-rotating-btz/calc.py`, `results.json`, `sprinkle_cones.png`, `cone_tilt_radial.png`, `correlation_asymmetry.png`, `spectra_J0_vs_J.png`
**Status:** Dokončeno (první exploratorní sonda)
**Hypotéza:** H02 — SJ stav na Kerrově prostoročase, **Strategie II** (`knowledge-base/hypotezy/H02-sj-kerr.md`, ř. 100–121)
**Novost:** SJ konstrukce na *rotujícím* (Kerr/BTZ/SdS) pozadí je dle novelty-checku neprozkoumané území; existující SJ práce se omezují na statické nebo konformně ploché prostoročasy.

---

## Cíl

Provést **vůbec první numerický Sorkin-Johnstonův (SJ) stav v rotujícím prostoročase** a ukázat klíčovou tezi hypotézy H02: SJ konstrukce nikdy nepotřebuje časupodobný Killingův vektor, a proto projde čistě právě tam, kde stacionární konstrukce vakua (Boulware, Hartle-Hawking) selhávají — uvnitř **ergoregionu**, kde je `∂_t` prostorupodobný.

Konkrétní měřitelné otázky:

1. **Existence.** Lze SJ stav zkonstruovat v ohraničené 2D Lorentzově oblasti, která obsahuje část ergoregionu rotující BTZ černé díry? (Mělo by ano — SJ potřebuje jen samoadjungovanost `iΔ` na `L²(M')`.)
2. **Kontrola J=0 vs J≠0.** Srovnat SJ spektrum a dvoubodovou funkci uvnitř i vně ergoregionu proti stejně velké statické (J=0) oblasti.
3. **Signatura superradiance.** Hledat ve struktuře SJ stavu otisk strhávání souřadnic (frame dragging) / superradiance.

Toto je **explorativní první krok**, nikoli Kerrův výsledek: rámujeme jako „SJ stav existuje a je spočitatelný tam, kde stacionární konstrukce selhávají", ne jako 4D Kerrovo tvrzení.

---

## Metoda

### Páka: konformní trivialita 2D bezhmotného skaláru

Celá konstrukce stojí na jednom přesném faktu:

> Pro **bezhmotný** skalár v **libovolném** 2D prostoročase je retardovaná Greenova funkce na kauzální množině
> `G_R = (1/2) C`,  kde `C_xy = 1` právě když `y` předchází `x` (`y` v kauzální minulosti `x`), jinak 0.

Důvod (ověřeno proti literatuře):
- Každá 2D Lorentzova metrika je (lokálně) konformně plochá: `g_ab = Ω² η_ab`.
- Bezhmotný skalární vlnový operátor je v 2D **konformně invariantní** (konformní vazba `ξ = 0` JE v d=2 minimální vazba).
- Retardovaná Greenova funkce proto závisí **pouze na kauzální/konformní struktuře**, ne na konformním faktoru `Ω`.

Na kauzální množině je to přesná identita `G_R = (1/2)C` (Sorkin–Yazdi); střední hodnota na sprinklingu se rovná kontinuovému `G_R` pro **všechny** hustoty. Pro masivní pole platí `G_R = (1/2)C (I + (m²/2ρ)C)^{-1}`, jehož limita `m→0` dává přesně `(1/2)C`. Použití přesně tohoto v zakřivené 2D (AdS₂) — díky konformní plochosti — je explicitně provedeno v arXiv:2504.12919.

**Důsledek pro nás:** Pro libovolný 2D řez BTZ potřebujeme **pouze kauzální uspořádání** sprinklovaných bodů. Křivost, strhávání souřadnic i ergoregion vstupují **výhradně** přes naklonění světelných kuželů (a přes míru správného objemu pro sprinkling).

### Geometrie: volba 2D řezu (poctivě dokumentováno)

Rotující BTZ (Bañados–Teitelboim–Zanelli), AdS poloměr `l = 1`:
```
ds² = -N² dt² + N⁻² dr² + r²(dφ + N^φ dt)²,
N² = -M + r² + J²/(4r²),   N^φ = -J/(2r²).
```
Složky: `g_tt = M - r²`, `g_tφ = -J/2` (konstantní strhávání), `g_φφ = r²`, `g_rr = 1/N²`.
Horizonty: `r_±² = (1/2)(M ± √(M²-J²))`. Ergosféra (statická mez, `g_tt = 0`): `r_erg = √M`.
Pro `J ≠ 0` je `r_+ < r_erg`, takže **existuje ergoregion** `r_+ < r < r_erg`, kde `g_tt > 0`, tj. `∂_t` je prostorupodobný — žádný časupodobný Killingův vektor.

**Která 2D oblast?** (ověřeno symbolicky, `sympy`)
- Řez `(t,r)` při pevném `φ` se **uvnitř ergoregionu stává Euklidovským** (signatura `(+,+)`, neboť `g_tt > 0` i `g_rr > 0`): `φ` tam nelze vypustit.
- Řez `(t,φ)` při pevném `r` zůstává **Lorentzův skrz celý ergoregion**:
  `det[[g_tt,g_tφ],[g_tφ,g_φφ]] = M r² - r⁴ - J²/4 = -N² r² < 0` pro všechna `r > r_+`.
  Uvnitř ergoregionu je `∂_t` prostorupodobný, ALE φ-stržená kombinace `(1, +s_drag)` je časupodobná — kužely se prostě **naklánějí**.

Proto je primární oblastí řez `(t,φ)` při pevném `r`. Bereme **ohraničený souřadnicový patch** `(t,φ) ∈ [0,T]×[0,Φ]` (konečné φ-okno: kauzální obdélník na válci, NIKOLI plná kružnice `2π` — relativně kompaktní globálně hyperbolický patch, který se vyhýbá periodické identifikaci `φ ~ φ+2π`).

### Kauzální uspořádání na řezu `(t,φ)` (naklonené kužely)

Indukovaná 2-metrika `h = [[g_tt,g_tφ],[g_tφ,g_φφ]]` je **konstantní** (kužely jsou uniformní). Posunutí `D = x - y` je do budoucnosti směřující kauzální právě když:
- kauzální: `h(D,D) ≤ 0`,
- do budoucnosti: `h(T,D) < 0`, kde `T = (1, s_drag)`, `s_drag = -g_tφ/g_φφ` je směr nulového momentu hybnosti (LNRF), časupodobný neboť `h(T,T) = det h / g_φφ < 0`.

To dává čisté částečné uspořádání na patchi. Sprinkling: rovnoměrný v `(t,φ)` (konstantní správný objem `√(-det h) dt dφ`), hustota `ρ = N / (√(-det h)·T·Φ)`.

### SJ pipeline (konvence identické s VYPOCET-04 / Sorkin–Yazdi 1611.10281)

1. `C_xy = 1` když `y` předchází `x` (naklonené kužely), diagonála 0.
2. `G_R = (1/2)C`; `Δ = G_R - G_Rᵀ = (1/2)(C - Cᵀ)`; `iΔ` hermitovský.
3. SJ Wightman `W = kladná část iΔ = Σ_{λ_k>0} λ_k |v_k⟩⟨v_k|`.

### Měřená pozorovatelná: signatura superradiance

Dvě fyzikálně odlišná, znaménkově smysluplná měřítka, obě postavená na týchž kauzálních datech:

- **(1) Kauzální směrová asymetrie `A_caus = 2 f_co - 1`.** Mezi všemi kauzálně příbuznými páry (`x` v budoucnosti `y`) zaznamenat azimutální postup `dφ = φ_x - φ_y`. Ve statickém řezu je kužel symetrický pod `φ → -φ`, takže `f_co = 0.5`, `A_caus = 0`. Strhávání souřadnic naklání kužel a zvýhodňuje `+φ`. Uvnitř ergoregionu je kužel **plně stržen**: KAŽDÝ kauzální spoj má `dφ > 0`. (Nejčistší 2D causal-set otisk ergoregionu.)
- **(2) SJ Wightmanova směrová asymetrie `A_W`.** Přes tytéž páry vážit střední hodnotou `Re W(x,y)` na spoj v co- vs. proti-rotujícím směru. Probuje, zda **kvantové korelace** SJ vakua dědí stržení.

---

## Vstupy s citacemi

| Vstup | Hodnota / forma | Zdroj |
|-------|-----------------|-------|
| Rotující BTZ metrika, `N²`, `N^φ` | `N²=-M+r²+J²/4r²`, `N^φ=-J/2r²` | Bañados-Teitelboim-Zanelli; ověřeno proti arXiv:gr-qc/0003097, 1707.08133 |
| `g_tt=M-r²`, `g_tφ=-J/2`, `g_φφ=r²` | (strhávací člen ruší J² v g_tt) | symbolické ověření (sympy), tento výpočet |
| Horizonty `r_±²=(1/2)(M±√(M²-J²))`; ergosféra `r_erg=√M` | `l=1` | arXiv:1707.08133 ("ergoregion pro `r_+<r<r_erg=ℓ√M`") |
| Ergoregion existuje ⟺ `J≠0` (jinak `r_+=r_erg`) | — | tamtéž; ověřeno numericky |
| `G_R = (1/2)C` (2D bezhmotný, konformně invariantní) | faktor ½ | Sorkin-Yazdi **1611.10281** eq. 9; footnote 5 (přesné pro všechna ρ) |
| Masivní `G_R=(1/2)C(I+(m²/2ρ)C)⁻¹` → `(1/2)C` při m=0 | — | Johnston; **1701.07212**, **1712.04227** |
| Konformní plochost ⇒ `G_R=(1/2)C` i v zakřivené 2D (AdS₂) | — | **2504.12919** (Retarded Causal Set Propagator in 2D AdS) |
| `iΔ=i(1/2)(C-Cᵀ)` hermitovský; SJ W = kladná část iΔ | spektrální | Sorkin-Yazdi **1611.10281**; Afshordi-Aslanbeigi-Sorkin **1205.1296** |
| Konvence zděděné z VYPOCET-04 (`ssee-diamond`) | — | tento projekt |

---

## Výsledky

### Fiduciální parametry
`M=1, J=0.6` (rotující) → `r_+=0.9487, r_-=0.3162, r_erg=1.0000`; ergoregion `(0.9487, 1.0)`. Statická kontrola `J=0` → `r_+=r_erg=1.0`, žádný ergoregion. `N=1600` bodů, `T=Φ=1.4`, 4 seedy.

### A — Existence uvnitř ergoregionu vs. degenerace statického řezu (HLAVNÍ VÝSLEDEK)

| Veličina | Rotující (J=0.6), `r=0.974` UVNITŘ ergoregionu | Statický (J=0), totéž `r` |
|----------|--------------------------------------------------|----------------------------|
| Řez Lorentzův? | **Ano** (det h<0, disc>0) | **Ne** (disc=−0.192<0, žádný reálný kužel) |
| SJ konstruovatelný? | **Ano** | **Ne** (není na čem) |
| Nulové sklony kuželu `dφ/dt` | `(+0.100, +0.532)` — OBA kladné, plně stržený | — (žádné reálné) |
| Spektrum `iΔ` | **796 kladných / 796 záporných** přesných ± párů | — |
| Párový reziduál (rel.) | **4.6×10⁻¹⁶** (strojová přesnost) | — |
| `Tr(iΔ)` | 2.3×10⁻¹³ | — |
| Podíl co-rotujících kauzálních spojů `f_co` | **1.000** (statika by dala 0.5) | — |
| `A_caus` | **+1.000** | — |
| `⟨dφ/dt⟩` vs. strhávací sklon | 0.306 vs. 0.316 ✓ | — |

**SJ stav je tedy plně dobře definovaný uvnitř rotujícího ergoregionu**, kde je `∂_t` prostorupodobný — a stejný statický řez při témže `r` není ani Lorentzův. Toto je přímá numerická demonstrace teze H02.

### B — Kontrola J=0 vs J≠0 vně ergoregionu (`r=1.30`, oba Lorentzovy, 4 seedy)

| Veličina | Rotující J=0.6 | Statický J=0 |
|----------|----------------|--------------|
| `A_caus` (kauzální směrová asymetrie) | **+0.227 ± 0.007** (33.8σ od nuly) | **+0.007 ± 0.009** (0.74σ, konzistentní s 0) |
| podíl co-rotujících spojů | 0.614 | 0.503 |
| `A_W` (SJ Wightmanova asymetrie) | **−0.211** | −0.008 (≈ 0) |
| rel. rozdíl SJ spekter | 3.4 % | (referenční) |

Statická kontrola sedí přesně na nule; rotace dává jasný 34σ signál. **Pozoruhodné:** kauzálně-početní asymetrie (`+0.227`, více spojů co-rotuje) a SJ-korelační asymetrie (`−0.211`, na spoj jsou korelace silnější proti-rotujícně) mají **opačná znaménka** — netriviální vlastnost SJ vakua ve strženém prostoročase.

### C — Radiální profil přes ergosféru (`J=0.6`)

| r | v ergoregionu | `f_co` | `A_caus` | `A_W` | sklon− | sklon+ |
|---|---------------|--------|----------|-------|--------|--------|
| 0.958 | ano | 1.000 | +1.000 | N/A | +0.194 | +0.459 |
| 1.014 | ne | 0.923 | +0.846 | −0.607 | **−0.045** | +0.628 |
| 1.070 | ne | 0.770 | +0.539 | −0.449 | −0.181 | +0.704 |
| 1.30 | ne | 0.605 | +0.210 | −0.195 | −0.481 | +0.839 |
| 1.80 | ne | 0.534 | +0.068 | −0.061 | −0.727 | +0.929 |

Monotónní a fyzikálně transparentní: uvnitř ergoregionu `f_co = 1` (plně stržený kužel); **přesně na ergosféře `r_erg=1.0` prochází vnitřní nulový sklon nulou** (`sklon− ≈ −0.045` hned za `r_erg`) — hrana kuželu se zarovná s φ-osou právě na statické mezi, učebnicový cross-check. Vně asymetrie hladce klesá k nule jako strhávání `~1/r²`. (Plot `cone_tilt_radial.png`, `correlation_asymmetry.png`.)

### Kde NEsedí očekávání: spektrum iΔ je téměř konformně invariantní

Plot `spectra_J0_vs_J.png` ukazuje, že SJ **eigenvalue spektra** rotujícího a statického řezu (při shodném `r` vně ergoregionu) jsou téměř identická (rel. rozdíl 3.4 %), `k·λ_k` má stejné kontinuové plató `1/k`. Přímý test na **týchž** sprinklovaných bodech (oddělí náhodnost sprinklingu): spektra se liší jen na úrovni ~1.8 %, a to jen proto, že naklonění kuželu mění, **které** páry jsou kauzálně příbuzné (link fraction driftuje 0.1795→0.1818). Tvar (1/k zákon) je stejná konformní třída.

**Interpretace:** Rotace se NEnachází v bulk spektru `iΔ` (to je řízeno konformní třídou), ale v **eigenvektorech** a tedy v dvoubodové funkci `W(x,y)` — což je přesně to, co naše korelační-asymetrické pozorovatelné detekují, zatímco samotné spektrum ne.

---

## Interpretace pro hypotézu H02

1. **Teze H02 numericky potvrzena (2D sonda).** SJ stav existuje a je strojově přesně dobře definovaný uvnitř rotujícího ergoregionu, kde je `∂_t` prostorupodobný a kde stacionární vakua nemají analog. Stejně velký statický řez tam degeneruje. SJ konstrukce skutečně **nepotřebuje časupodobný Killingův vektor** — to je celá pointa.

2. **Strhávání souřadnic má čistou 2D causal-set signaturu.** Podíl co-rotujících kauzálních spojů `f_co` roste z 0.5 (statika) na 1.0 (plně stržený kužel uvnitř ergoregionu); `A_caus` vrcholí na +1 v ergoregionu a hladce klesá vně. Vnitřní nulový sklon prochází nulou přesně na ergosféře. To je 2D causal-set otisk superradiantního pásma (uvnitř ergoregionu nelze poslat kauzální vliv proti rotaci).

3. **Netriviální nález o SJ vakuu:** kauzálně-početní a SJ-korelační asymetrie mají opačná znaménka (`+0.227` vs `−0.211`). Stržení tedy nepůsobí na klasický kauzální skelet a na kvantové korelace stejně — to je vlastnost, kterou by standardní modová analýza (vázaná na Killingovy symetrie) těžko zachytila.

4. **Most ke Strategii III (4D Teukolsky):** Klíčová otázka H02 — přispívají superradiantní módy (0<ω<mΩ_H) v SJ kladnými či zápornými vlastními čísly — zde v 2D nemá přímý analog (spektrum je konformně invariantní, rotace je v eigenvektorech). To naznačuje, že ve 4D bude superradiantní signatura SJ stavu pravděpodobně rovněž ve **struktuře eigenvektorů / W**, nikoli v hrubém spektru `iΔ` — užitečný cíl pro plný výpočet.

---

## Limity výpočtu

- **Pouze 2D, bezhmotný skalár, BTZ (ne Kerr).** Toto je 2D analog (Strategie II), explicitní první sonda, NE 4D Kerrův výsledek. 4D Kerr (Strategie I/III) zůstává otevřený; tam `G_R ≠ (1/2)C` (4D není konformně triviální), takže bude potřeba integrovat nulové geodetiky / Teukolskyho módy.
- **Pevné-r řez má uniformní kužely.** Indukovaná 2-metrika je konstantní, takže neobsahuje radiální gradient v jediné oblasti; r-závislost zkoumáme skenem oddělených pevných-r oblastí (Část C), ne jedinou 2D oblastí pokrývající `r`. Oblast pokrývající `r` skrz ergoregion by nutně byla 3D (φ nelze vypustit, viz Euklidovská degenerace `(t,r)` řezu) — mimo rozsah této sondy.
- **Konečné φ-okno, ne plný válec.** Bereme kauzální obdélník `(t,φ)∈[0,T]×[0,Φ]`, abychom se vyhli periodické identifikaci `φ~φ+2π` a měli relativně kompaktní globálně hyperbolický patch. Plný válec (s periodicitou) by vyžadoval ošetření wrap-around kauzality — `∂_φ` je vždy prostorupodobný (`g_φφ=r²>0`), takže CTC z φ-kružnic nehrozí, ale je to samostatná úloha.
- **Fixní N (kanonická aproximace), ne pravý Poissonův proces** s fluktuujícím N. Pro směrové asymetrie a existenci je rozdíl O(1/N) zanedbatelný.
- **Hadamardovskost neřešena.** SJ stavy obecně nejsou Hadamardovské (Fewster-Verch); zde se na to neptáme — měříme existenci a směrové signatury, ne UV strukturu. Softened-SJ (Jubb-Surya 2212.10592) by byl logickým rozšířením.
- **`A_W` uvnitř ergoregionu nedefinováno** (nejsou proti-rotující spoje, `n_cc=0`); reportujeme jen `A_caus=+1`. To je korektní, ne chyba — odráží plné stržení.

---

## Citace (prohledané/použité)

- **1611.10281** — Sorkin, Yazdi, *Entanglement Entropy in Causal Set Theory* (`G_R=½C`, iΔ, SJ W = kladná část)
- **1701.07212** — Johnston ad., *Scalar Field Green Functions on Causal Sets* (masivní `G_R`, limita m→0)
- **1712.04227** — *On the Entanglement Entropy of Quantum Fields in Causal Sets* (`G_R=½C`, konvence)
- **2504.12919** — *Retarded Causal Set Propagator in 2D Anti-de-Sitter Spacetime* (konformní plochost ⇒ `½C` v zakřivené 2D)
- **1205.1296** — Afshordi, Aslanbeigi, Sorkin, *A distinguished vacuum state...* (SJ kontinuum)
- **1906.07952** — Mathur, Surya, *SJ vacuum for massive scalar in 2D causal diamond* (numerický SJ toolchain)
- **gr-qc/0003097, 1707.08133** — rotující BTZ metrika, horizonty, ergoregion `r_+<r<ℓ√M`
- **H02-sj-kerr.md** (tento projekt) — Strategie II
- **VYPOCET-04 / ssee-diamond** (tento projekt) — zděděné SJ konvence a kód
