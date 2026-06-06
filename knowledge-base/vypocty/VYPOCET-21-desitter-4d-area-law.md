# VYPOCET-21: 4D de Sitterova statická záplata — odděluje truncovaná area-law SSEE $S\sim\sqrt{N}$ sama typ II₁ od II_∞? (test H5g-1)

**Datum:** 2026-06-06
**Soubory:** `core-data/calculations/sj-desitter-4d/calc.py`, `results.json`, `plots/{part1_discriminator,part2_area_law_scaling}.png`
**Status:** Dokončeno
**Hypotéza (H5g-1, BRAINSTORM-05, vysoká priorita):** ve 4D dS statické záplatě by **truncovaná** area-law SSEE $S\sim\sqrt{N}$ měla **sama o sobě** oddělit typ II₁ (saturuje, jak oblast vyčerpává ohraničenou záplatu) od II_∞ (roste na ploché kontrole) — na rozdíl od 2D (F-023, VYPOCET-19), kde rozlišoval **jen obsah oblasti**.
**Cluster:** entropy-cluster × von-Neumann (typový přechod) × horizon-SJ × de Sitter
**Navazuje:** VYPOCET-19 / F-023 (2D dS, II₁ vs II_∞ jen v obsahu), VYPOCET-06 / vn-type-slab-4d / F-019 (4D area law $S\sim\sqrt{N}$)
**Knihovna (dogfooding):** postaveno na `toe` v0.1.0; rozšíření `toe.causet.sprinkle_ds_static_patch4d` přidáno tento běh (vlastnictví `causet.py` tento round).

---

## Cíl a motivace

VYPOCET-19 (2D, F-023) ukázal, že rozdíl CLPW (Chandrasekaran-Longo-Penington-Witten, **arXiv:2206.10780**) mezi typem **II₁** (de Sitterova statická záplata, normalizovatelná stopa $\mathrm{Tr}\,1<\infty$) a **II_∞** (černá díra / Rindler, semifinitní stopa) je ve 2D nesen **obsahem oblasti** ($N_{\rm total}$, plná SSEE $S_{\rm full}$), **nikoli truncovanou** (typ-II regularizovanou) entropií — protože 2D typ-II area law je log/area zákon téměř nezávislý na velikosti boxu v **obou** geometriích.

Vlastní limita-sekce 2D writeupu udělala explicitní predikci pro 4D: truncovaná typ-II SSEE je tam **area law** $S\sim\sqrt{N}\sim L^2$, který **roste** s oblastí pro neohraničenou (II_∞) geometrii a **saturuje** pro ohraničenou dS záplatu (II₁). Tedy ve 4D by **truncovaná entropie sama** měla oddělit typy. To je přesně H5g-1.

---

## Geometrie: 4D dS statická záplata jako $\mathrm{sech}^2$-vážený slab

Statická záplata 4D ve želvích (tortoise) + transverzálních souřadnicích $(t, r^*, x_1, x_2)$, $r^* = \ell\,\mathrm{arctanh}(r/\ell)$, konformní faktor $\Omega^2 = 1 - r^2/\ell^2 = \mathrm{sech}^2(r^*/\ell)$. Sprinklujeme **vlastní (proper) dS mírou**

$$dN \sim \mathrm{sech}^2(r^*/\ell)\,dt\,dr^*\,dx_1\,dx_2$$

(radiální $\mathrm{sech}^2$ váha, transverzální plochý box) přes nové knihovní rozšíření `toe.causet.sprinkle_ds_static_patch4d`. **Shodná plochá kontrola** (II_∞) sprinkluje uniformní radiální box (bez $\mathrm{sech}^2$) se stejným transverzálním boxem a stejnou vlastní hustotou — jediný rozdíl je radiální míra, přesně jako VYPOCET-19.

### Konformně-váhový caveat (poctivě, předem)

Na rozdíl od 2D **4D bezhmotný skalár NENÍ konformně invariantní**, takže konformní faktor z přesného propagátoru **nevypadne**. Toto je **stejná řízená aproximace** jako 2D konformní trik VYPOCET-19, **zvednutá do 4D**: zachovává se **plochá kauzální struktura** v $(t, r^*, x_1, x_2)$ a **vlastní dS míra** ($\mathrm{sech}^2$ radiální hustota ⇒ ohraničený rozpočet bodů = geometrická signatura II₁), **nikoli** přesná zakřivená 4D Wightmanova funkce. Retardovaná Greenova funkce se staví 4D link-matrix konstrukcí (Johnston **0909.0944**) na tomto plochém konformním uspořádání. Testuje se tedy **geometrická ohraničenost II₁ vs II_∞ v truncované area-law SSEE**, ne přesný dS propagátor. (Stejný status jako VYPOCET-19.)

### 4D typ-II area-law truncace (F-019)

Rank truncace $n_{\max} = \alpha N^{(d-1)/d}$, $d=4 \Rightarrow n_{\max} = 2N^{3/4}$ (Surya-Nomaan-X-Yazdi **2008.07697**; validováno ve VYPOCET-06 / vn-type-slab-4d jako 4D area law $S\sim\sqrt{N}=L^2$). Knihovní implementace: `toe.entropy.ssee(..., n_max=...)` (zachová top $n_{\max}$ pozitivních módů $i\Delta$ + párované negativní).

---

## Konvence (knihovna `toe`)

| Vstup | Forma | Zdroj |
|---|---|---|
| sprinkling 4D dS | $dN\sim\mathrm{sech}^2(r^*/\ell)\,dt\,dr^*\,dx_1\,dx_2$ | `sprinkle_ds_static_patch4d` (VYPOCET-21) |
| kauzální matice $C$ | plochá 4D světelný kužel v $(t, r^*, x_1, x_2)$ | `causal_matrix` (1611.10281) |
| link matice $L$ | tranzitivní redukce $C$ | `link_matrix` (Johnston 0909.0944) |
| $G_R = aL$, $a=\sqrt{\rho}/(2\pi\sqrt6)$ | 4D retardovaná Greenova fce | `green_retarded_4d` (0909.0944) |
| $i\Delta = i(G_R - G_R^\top)$ | Pauli-Jordan, hermitovský, ±párovaný | `pauli_jordan` (1611.10281) |
| SSEE $W_O v=\mu\,i\Delta_O v$, $S=\sum\mu\ln|\mu|$ | spacetime entanglement | `ssee` (1611.10281) |
| $n_{\max}=2N^{3/4}$ | 4D area-law rank truncace | `n_max_area_law` (2008.07697) |
| $\varepsilon=\ln[\mu/(\mu-1)]$ | modulární energie | `modular_spectrum` (0905.2562) |

**Strojová přesnost (±-párování $i\Delta$):** asertováno na **každé** nové oblasti, `pairing_residual_rel` $< 10^{-12}$. Naměřeno: $2.9\cdot10^{-15}$ (Part 1), $6.8\cdot10^{-15}$ (Part 2) — $i\Delta$ správně antisymetrický. Invariant testován i v nové testovací sadě `app/tests/test_toe_causet_ds4d.py`.

---

## Metoda a numerika

Dvě části, 4 seedy, $N\le2500$ (dense `eigh`), runtime ~290 s (thread-cap 4):

- **Část 1 (diskriminátor H5g-1):** fixní vlastní hustota $\rho=120$; radiální hrana boxu $R^*_{\rm box}$ roste k horizontu (6 kroků, $R^*_{\rm box}\in[1.6, 5.2]\,\ell$, omezeno tak, aby shodná plochá kontrola zůstala $N\le2496$). Truncovaná SSEE ($n_{\max}=2N^{3/4}$) přes **rostoucí** řez (entangling plocha $x_1=0$, transverzální interior $|x_2|<0.7\,x_\perp$, radiální rozsah $= 0.5\cdot R^*_{\rm box}$ — sleduje oblast k horizontu). Současně sledováno $N_{\rm total}$ a $S_{\rm full}$ jako křížová kontrola VYPOCET-19. Diskriminátor: truncovaná-$S$ pozdní sklon dS $\to$ 0 (saturace; saturační vs lineární fit, AIC) vs plochá $>0$. Knihovní `toe.vntype.saturation_discriminator` poskytuje pomocný verdikt o saturaci/růstu $N_{\rm total}$.
- **Část 2 (scaling cross-check při fixní oblasti):** rostoucí hustota ($N=434\to2407$) při FIXNÍ dS pod-oblasti; truncovaná SSEE musí sledovat 4D area law $S_{\rm trunc}\sim N^a$, $a\sim1/2$ (F-019). `toe.fits.powerlaw_fit` s reziduální SE + bootstrap CI.

---

## Část 1 — Diskriminátor H5g-1 (jádro)

| veličina (hrana $R^*_{\rm box}$: 1.6 → 5.2 ℓ) | de Sitter | plochá kontrola |
|---|---|---|
| **$N_{\rm total}$** (kardinalita) | **442 → 480, SATURUJE** (strop=480, $R^2=1.000$) | **768 → 2496, ROSTE** (sklon 480/jedn. $r^*$) |
| **$S_{\rm trunc}$** (truncovaná, $n_{\max}=2N^{3/4}$) | **30.6 → 45.0** (pozdní sklon +4.6, powerlaw $a=0.27$) | **43.0 → 76.6** (pozdní sklon +7.1, powerlaw $a=0.52$) |
| $S_{\rm full}$ (plná, sleduje obsah) | 30.7 → 39.0 (saturuje) | 45.1 → 117.5 (roste) |

**Klíčové pozorování:** truncovaná dS SSEE roste **mnohem mělčeji** než plochá kontrola:
- poměr plného sklonu plochá/dS = **2.96** (plochá roste ~3× rychleji),
- dS area-law exponent v $R^*_{\rm box}$ je $a=0.27$ vs plochá $a=0.52$ (přibližně poloviční).

Toto je **reálný 4D-specifický separační signál v truncované entropii, který ve 2D NEEXISTOVAL** (F-023: truncovaná $S$ box-nezávislá v obou geometriích). Mechanismus: $\mathrm{sech}^2$ vlastní plocha rostoucího řezu v dS saturuje, takže její area-law entropie roste pomaleji než u neohraničené ploché kontroly.

**Ale dS truncovaná $S$ při dostupných $N$ plně NESATURUJE** (stále stoupá ~poloviční rychlostí ploché). Důvod je poctivý a kvantifikovaný: **rostoucí entangling řez při fixní hustotě stále přidává dS pod-oblasti body** ($|sub|$: 108 → 163 přes sweep) — radiální růst řezu přebíjí $\mathrm{sech}^2$ saturaci v rozpočtu pod-oblasti. Čistá saturace-vs-růst (silné H5g-1) tedy není dosažena.

**Verdikt Části 1: ČÁSTEČNÉ H5g-1.** Truncovaná area-law SSEE ukazuje genuinní separaci (poměr sklonů 2.96, exponent poloviční), ale ne plnou saturaci. Křížová kontrola obsahu ($N_{\rm total}$ strop=480, $R^2=1.000$ vs lineární růst ploché) odděluje II₁ od II_∞ **rozhodujícím způsobem**, přesně jako 2D F-023.

---

## Část 2 — 4D area-law scaling na dS záplatě (F-019 cross-check)

Při fixní dS pod-oblasti a rostoucím $N$ (434 → 2407):

| veličina | dS exponent $a$ ($S\sim N^a$) | charakter |
|---|---|---|
| $S_{\rm full}$ (netruncovaná) | $a=1.017\pm0.018$ ($R^2=0.999$) | objemová/divergentní stopa (III) |
| $S_{\rm trunc}$ ($n_{\max}=2N^{3/4}$) | $a=0.717\pm0.029$ (CI68 [0.70, 0.74], $R^2=0.993$) | regularizovaná (II), **ale nad cílem 0.5** |
| pile-up $\varepsilon<0.5$ (full) | 6.0 → 32.2 (roste) | III₁ hustá flat signatura |
| pile-up $\varepsilon<0.5$ (trunc) | 0.2 → 0 | typ II (ostrá IR mezera) |

**Poctivé zjištění:** truncovaný exponent vyšel $a=0.72$, **ne** čistých F-019 $a\sim0.5$. Důvod: dS **radiální geometrie strmí** area law oproti čistému plochému slabu (vn-type-slab-4d dosáhl $a=0.547$ s ploškou entangling plochou $x_1=0$ ve slabu $T<L$; dS přidává neohraničený-ish radiální směr $r^*$, který přidává objemovou složku). Modulární pile-up nicméně jednoznačně potvrzuje III→II (full roste $6\to32$, trunc $=0$). Plná SSEE $a\approx1.0$ je objemová (III), přesně dle očekávání.

**Verdikt Části 2:** truncace JE operativní regularizátor (III→II v pile-upu, $S_{\rm full}$ objemová vs $S_{\rm trunc}$ subobjemová), ale 4D area-law exponent $a\sim0.5$ není čistě vyřešen při $N\le2500$ s touto dS-radiální geometrií.

---

## VERDIKT

> ### **CELKOVÝ VERDIKT: ČÁSTEČNÉ H5g-1 (PARTIAL).**
> Ve 4D truncovaná area-law SSEE **ukazuje reálnou, 4D-specifickou separaci** typů, která ve 2D (F-023) neexistovala — dS truncovaná $S$ stoupá ~3× mělčeji než plochá kontrola (dS exponent $a=0.27$ vs plochá $0.52$), což odráží $\mathrm{sech}^2$ strop vlastní plochy. **NEDOSAHUJE však plné saturace** při dostupných $N\le2500$ (dense eigh), protože rostoucí entangling řez při fixní hustotě stále přidává dS body — čistá saturace-vs-růst silného H5g-1 není dosažena. **Křížová kontrola obsahu ($N_{\rm total}$, $S_{\rm full}$) odděluje II₁ od II_∞ rozhodujícím způsobem, přesně jako 2D F-023.**

| Část | Predikce (silné H5g-1) | Výsledek |
|---|---|---|
| **1 — truncovaná-$S$ diskriminátor** | dS saturuje, plochá roste | **ČÁSTEČNÉ** (dS ~3× mělčí sklon, ale neúplná saturace) |
| **1 — obsah ($N_{\rm total}$) cross-check** | dS strop, plochá růst | **✓ DISKRIMINOVÁNO** (strop 480 $R^2=1.000$ vs lineární 480/r*) |
| **2 — 4D area law** | $S_{\rm trunc}\sim N^{0.5}$ | **ČÁSTEČNÉ** ($a=0.72$; III→II potvrzeno pile-upem, ale exponent strmí) |

**Strojový invariant:** ±-párování $i\Delta$ $< 7\cdot10^{-15}$ na všech oblastech ✓.

---

## Poctivá zjištění a co by silné H5g-1 vyřešilo

1. **Truncovaná entropie ve 4D NESE nový signál (oproti 2D), ale ne čistou saturaci při $N\le2500$.** Poměr sklonů plochá/dS = 2.96 a poloviční dS exponent jsou reálné — to je kvalitativní posun oproti F-023, kde byla truncovaná $S$ box-nezávislá v obou geometriích. Ale dS $S_{\rm trunc}$ stále stoupá.

2. **Proč neúplná saturace:** rostoucí entangling řez ($r^* < 0.5\,R^*_{\rm box}$) při FIXNÍ hustotě stále přidává dS pod-oblasti body, protože radiální růst řezu předbíhá $\mathrm{sech}^2$ saturaci rozpočtu. Co by čistou saturaci dosáhlo: (a) **fixní-plochá entangling řez** s **hustším radiálním sweepem k horizontu** a větším $\ell$; (b) **vyšší vlastní hustota** $\rho\gtrsim10^3$ (za hranicí dense `eigh` při $N\sim2500$ — vyžaduje řídké/iterativní eigensolvery); (c) tenčí časový slab + entangling plocha čistě 2-rozměrná (jako vn-type-slab-4d $T<L$), aby area law dosáhl $a\sim0.5$.

3. **4D area-law exponent $a=0.72$ (ne 0.5):** dS radiální geometrie strmí area law oproti čistému plochému slabu. Není to chyba SSEE kompozice — kontrolní reprodukce přesné vn-type-slab-4d geometrie přes knihovnu `toe` dala $a=0.58$ (cíl 0.547), takže kompozice je správná; rozdíl je geometrický (dS radiální směr přidává objem).

4. **Nefudgováno.** Verdikt je tří-cestný (STRONG / PARTIAL / NULL); výsledek je poctivě PARTIAL. Booleovské kritérium silného H5g-1 (plná saturace + poměr sklonů > 2.5 + $a_{\rm trunc}\sim0.5$) selhalo na úplnosti saturace, ne na separačním signálu.

---

## Vstup pro rozhodnutí H5g-6 (draft-05 vs sekce v draft-04)

F-023 (2D: rozlišuje jen obsah) + F-019 (4D area law $S\sim\sqrt{N}$) + **tento výsledek** podporují **dS SEKCI v draft-04** (crossed-product / vN-typový draft), **nikoli zatím samostatný draft-05**. 4D truncovaná area-law SSEE ukazuje **genuinní novou separaci** chybějící ve 2D (dS ~3× mělčí než plochá; dS $R^*$-exponent 0.27 vs plochá 0.52), a obsahový diskriminátor ($N_{\rm total}$ strop $R^2=1.000$ vs lineární růst) **čistě zvedá F-023 do 4D**. Ale truncovaná entropie **plně NESATURUJE** při dense-eigh-dostupných $N\le2500$. Rozhodnutí: prezentovat jako **dS sekci v draft-04**, párovat 2D+4D obsahový diskriminátor s ČÁSTEČNÝM 4D truncovaným-entropie signálem, a označit test čisté saturace jako vyžadující větší $N$ (řídké/iterativní eigensolvery, $\rho\gtrsim10^3$, větší $\ell$, nebo fixní-plochou entangling řez s hustším radiálním horizontovým sweepem) jako budoucí práci, než může nést samostatný draft-05. **Konformně-váhový caveat** (4D skalár není konformně invariantní; zachována kauzální struktura + míra, ne přesný propagátor) musí být uveden poctivě tak jako tak.

---

## Knihovna `toe` — použití a rozšíření (dogfooding)

**Použité funkce:** `toe.causet` (`sprinkle_ds_static_patch4d` [nové], `causal_matrix`, `link_matrix`, `green_retarded_4d`, `pauli_jordan`, `causal_diagnostics`), `toe.sj.sj_state`, `toe.entropy` (`ssee` s `n_max`, `n_max_area_law`), `toe.vntype` (`modular_spectrum`, `pile_up`, `saturation_discriminator`), `toe.fits` (`powerlaw_fit` s SE+CI, `aic_compare`, `validate_against`).

**Rozšíření (pravidlo round: vlastnictví `causet.py`):**
- `toe.causet.sprinkle_ds_static_patch4d` — 4D $\mathrm{sech}^2$-vážený dS slab $(t, r^*, x_1, x_2)$ (radiální $\mathrm{sech}^2$, transverzální plochý box), s docstringem Formula/Evidence/Conventions a explicitním `rng` dle ARCHITECTURE.md A2.
- Nová testovací sada `app/tests/test_toe_causet_ds4d.py` (6 testů): ±-párovací invariant ($<10^{-12}$, multi-seed multi-box), $\mathrm{sech}^2$ radiální marginál monotónní, transverzální box plochý, $t$-rozsah, saturace vlastního objemu. Re-export v `toe/__init__.py`.
- **Regrese:** všech 247 `toe` testů prošlo (1 očekávaný xfail), včetně `test_toe_imports.py` (vrstevní pravidla) a původního `test_toe_causet.py` — žádná regrese.

**Co knihovně chybělo:** pouze 4D dS sprinkler (přidán). 4D area-law SSEE řetězec (`link_matrix` → `green_retarded_4d` → `pauli_jordan` → `ssee(n_max=...)`) byl plně přítomen; reprodukoval vn-type-slab-4d area law ($a=0.58$ vs commit 0.547) jako kontrolu kompozice. Plotting nakreslen lokálně (toe.viz je orientovaný na 2D-fit panely).

---

## Reference (klíčové)

- **2206.10780** — Chandrasekaran, Longo, Penington, Witten: dS statická záplata typu II₁ (vs černo-děrové II_∞).
- **2008.07697** — Surya, X, Yazdi: dS horizont SSEE; area-law rank $n_{\max}=\alpha N^{(d-1)/d}$, $d=4\to N^{3/4}$.
- **0909.0944** — Johnston: 4D causal-set retardovaná Greenova fce $G_R=aL$, $a=\sqrt{\rho}/(2\pi\sqrt6)$.
- **1611.10281** — Sorkin, Yazdi: SSEE, dvojitá truncace, $W_O v=\mu\,i\Delta_O v$.
- **1205.3855** — Anninos: dS statická záplata, želví souřadnice, $\Omega^2=\mathrm{sech}^2$.
- **0905.2562** — Casini, Huerta: bosonová modulární energie.
- VYPOCET-19 / F-023 (2D dS: II₁ vs II_∞ jen v obsahu), VYPOCET-06 / vn-type-slab-4d / F-019 (4D area law $S\sim\sqrt{N}$).
