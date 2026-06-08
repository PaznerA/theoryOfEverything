# VYPOCET-32: Unruhův teplotní zákon z SJ modulárního toku — vlajková loď hrany noncommutative-geometry ↔ semiclassical-gravity

**Datum:** 2026-06-08
**Soubory:** `core-data/calculations/ncg-kms-unruh/calc.py`, `results.json`, `plots/{beta_vs_proper_distance,unruh_law}.png`; knihovna `lib/toe/spectraltriple.py` (nový primitiv `unruh_proper_law` + `UnruhLawFit`, čtyři testy v `app/tests/test_toe_spectraltriple.py`)
**Status:** Dokončeno
**Slug:** `ncg-kms-unruh`
**Hypotéza:** nejpřímější neprozkoumaná sdílená-matematika hrany `noncommutative-geometry ↔ semiclassical-gravity` — Connes-Rovelliho tepelný čas (modulární tok = fyzikální/tepelný čas, gr-qc/9406019) ↔ Unruhův jev (semiklasická teplota $T=1/(2\pi x)$).
**Cluster:** modular-flow / KMS thermal time × Bisognano-Wichmann boost × Unruh/Tolman lokální teplota
**Navazuje:** VYPOCET-30 / F-034 (SJ modulární tok JE jednoteplotní KMS tok s $\rho$-invariantní boostovou diagonálou, ale absolutní Unruhova $2\pi$ se z surogátu nečte — `unruh_ratio` $=0{,}786$).

---

## Programová otázka

F-034 ukázal, že na 2D Rindlerově slabu (řez $x>0$) je SJ modulární tok jednoteplotní KMS tok ($\beta_{KMS}=1$ na strojovou přesnost) s $\rho$-invariantní lineární boostovou diagonálou $|K(x,x)|$ vs vzdálenost k řezu (sklon $\approx27{,}84$, $R^2\approx0{,}95$). **Klíčová lekce F-034:** $\beta_{KMS}=1$ a $\beta_{occ}=1$ jsou **TAUTOLOGIE** SJ/Casini-Huertovy konstrukce (Tomita-Takesaki dává KMS na $\beta=1$ *z konstrukce*) — NEjsou to fyzika. Jediný netriviální invariant byl sklon boostové diagonály, a **absolutní Unruhova $2\pi$ se NEobnovila**.

Tento výpočet pokládá **netautologickou otázku**:

> Obnoví SJ modulární tok **Unruhův teplotní zákon** $T_{\text{local}}(x)=1/(2\pi\,x_{\text{proper}})$ — tedy lineární růst modulární energetické hustoty s **PROPER vzdáleností** k horizontu (Bisognano-Wichmann: $K=2\pi K_{\text{boost}}$, $|K(x,x)|\sim 2\pi\,x\,\rho_E$, exponent $+1$) — s normalizací proper vzdálenosti **fixovanou NEZÁVISLE z geometrie** (hustota sprinkling, proper délka), a **NIKDY** laděnou k cíli $2\pi$?

**Antikruhovost (strukturální):** scale proper vzdálenosti je fixovaný PŘED jakýmkoli sklonem — z hustoty sprinkling ($\varepsilon_{\text{disc}}=\rho^{-1/2}$, diskretizační proper délka) a proper okna $[x_{lo},x_{hi}]=[0{,}06,\,0{,}90]\cdot x_{\text{extent}}$. Měříme dvě věci a obě reportujeme poctivě: **(A) EXPONENT zákona** (log-log sklon $p_E$ z $|K(x,x)|$ vs proper $x$; BW předpovídá $p_E=+1$) a **(C) absolutní koeficient $2\pi$** (přes geometrii-fixované routy, NIKDY laděno).

---

## Setup (ověřené konvence)

| Vstup | Forma | Zdroj |
|-------|-------|-------|
| Geometrie | 2D slab $\{0<t<0{,}3,\ |x|<1\}$, $T\ll L$ (Rindler-like), `sprinkle_slab2d` | **1611.10281** |
| Kauzální řád + Green | $G_R=\tfrac12 C$ (2D bezhmotný), `causal_matrix`, `green_retarded_2d` | **1611.10281** |
| Pauli-Jordan + SJ stav | $i\Delta=i(G_R-G_R^{\mathsf T})$, $W=$ poz. spektrální část, `pauli_jordan`, `sj_state` | **1611.10281** |
| Řez (Rindler) | $O=\{x>0\}$ (half-line; modulární tok = boost, horizont $x=0$) | BW **1712.04227** (kontext **2008.07697**) |
| Modulární kernel | $K(x,y)$ ze SSEE $W_O v=\mu\,i\Delta_O v$, $\varepsilon=\ln[\mu/(\mu-1)]$, $\kappa=$None (netruncovaný SJ tok) | Casini-Huerta **0905.2562**; `entropy.modular_kernel` |
| Unruhův zákon | log-log sklon $p_E$ z $|K(x,x)|$ vs PROPER $x$ na geometrii-fixovaném okně | BW **1712.04227** / Unruh `unruh1976notes` / Tolman |
| Modulární tok = tepelný čas | KMS / Tomita-Takesaki framing | Connes-Rovelli **gr-qc/9406019** |
| dS static patch (stretch) | tortoise $r^*$, sech²-měřítko, interní řez $r^*>r_0$, $T_{dS}=1/(2\pi l)$ | `sprinkle_ds_static_patch2d`; Anninos **1205.3855** |

**Kontroly:** (i) **interval** $O=\{0<x<0{,}5\}$ — BW NEplatí (modulární Hamiltonián vrcholí na OBOU koncích); (ii) **shuffle** $K'=QKQ^{\mathsf T}$ Haar-ortogonální konjugace (spektrum zachované, geometrie zničena).

**Parametry:** sweep $\rho$ přes $N\in\{600,1000,1400\}$ (mez husté `eigh` $\le1500$), 5 seedů/$\rho$ = 15 seedů (+15 dS). Wall-clock cap 25 min, skutečný běh **53,7 s**. Schéma `ncg-kms-unruh/v1`, atomický + progresivní zápis (per-seed flush).

**KAVEAT (poctivý, zděděný):** SJ modulární kernel je **SUROGÁTNÍ** Dirac v modulárně-energetických jednotkách $\varepsilon=\ln[\mu/(\mu-1)]$ (Casini-Huerta), liftnutý do site-basis; $\beta_{KMS}=1$ je Tomita-Takesaki tautologie. Log-komprese $\varepsilon$ činí měřený exponent **SUB-lineárním** ($p_E\approx0{,}72<1$) a nenese normalizaci boostového rapidity, takže absolutní $2\pi$ se z této diagonály nečte. Měříme TREND ($\rho$-invarianci, $N\le1500$ dense), ne $N\to\infty$.

---

## Výsledky

### (A) Unruhův exponent zákona — $p_E=0{,}72$, NE BW $+1$ (deficit 28 %)

Log-log sklon $|K(x,x)|$ vs proper vzdálenost na geometrii-fixovaném okně:

| $N$ | $p_E$ (law exponent) | $p_E$ R² | boost sklon | boost R² | $2\pi$ boost-quantum |
|---|---|---|---|---|---|
| 600 | 0,735 | — | 29,81 | — | 10,32 |
| 1000 | 0,729 | — | 29,22 | — | 8,89 |
| 1400 | 0,695 | — | 28,58 | — | 9,52 |
| **agregát** | **0,720 ± 0,040** | **0,988** | **29,20 ± 0,87** | **0,969** | **9,58 ± 1,49** |

Exponent je **$\rho$-invariantní** (CV $=2{,}4\%$) a log-lineární fit má vysoké $R^2=0{,}988$ — diagonála JE monotónně rostoucí log-lineární funkcí proper vzdálenosti (boostová geometrie přítomná). **ALE exponent je $0{,}72$, ne BW $+1$** (28% deficit, robustní napříč okny — testováno na $[0{,}06,0{,}9]$, $[0{,}04,0{,}5]$, $[0{,}04,0{,}35]$, exponent stabilně $0{,}56$–$0{,}72$, blíž k horizontu KLESÁ, ne saturuje). Deficit je **artefakt surogátních jednotek** (log-komprese $\varepsilon=\ln[\mu/(\mu-1)]$ stlačuje velké modulární energie), NE Unruhův zákon. Zákonný *tvar* (T~1/x, exponent $-1$) **NENÍ čistě obnoven**.

### (B) Boostová diagonála vs proper vzdálenost — lineární, $\rho$-invariantní

Boost sklon $29{,}20\pm0{,}87$ ($R^2=0{,}969$, CV $=1{,}7\%$) reprodukuje F-034 ($\approx27{,}84$) na proper vzdálenosti — geometrický boostový generátor je robustně přítomný a $\rho$-invariantní.

### (C) Absolutní $2\pi$ koeficient — NEobnoven (nejlepší routa off o 52 %)

| Routa (geometrie-fixovaná, NIKDY laděna) | hodnota | $|{\cdot}-2\pi|/2\pi$ |
|---|---|---|
| boost-quantum $\varepsilon_k\langle x\rangle_k$ (modulární energie × proper lokalizace) | **9,58 ± 1,49** | **52 %** |
| unruh_ratio (F-034 sklon/energie-hustota) | 0,790 ± 0,038 | 87 % |
| — | — | (cíl $2\pi=6{,}283$) |

Nejlepší routa (boost-quantum) dává **9,58, off o 52 %** od $2\pi$. **Absolutní Unruhova $2\pi$ se z geometrie-fixované normalizace NEčte** — surogátní kernel nenese normalizaci boostového rapidity, přesně jak F-034 předpověděl.

### (D) Kontroly — čistě selhávají

| Kontrola | law exponent | boost R² |
|---|---|---|
| **Rindler half-line** | **0,720** | **0,969** |
| interval $\{0<x<0{,}5\}$ | 0,043 | **0,038** |
| shuffle $QKQ^{\mathsf T}$ | $-0{,}001$ | **0,065** |

Diskriminátor čistý: na obou kontrolách boostová struktura **kolabuje** ($R^2\approx0{,}04$–$0{,}07\ll0{,}97$). Geometrický obsah žije v boostové diagonále, ne ve spektru.

### (E) Stretch: 2D de Sitter static patch → Gibbons-Hawking $1/(2\pi l)$

Interní horizont-like řez $r^*>r_0=0{,}6$ uvnitř static patche (jednostranný v tortoise $r^*$, proto interní řez s komplementem). 15 seedů:

| veličina | hodnota |
|---|---|
| law exponent $p_E$ | **0,618 ± 0,038** ($R^2=0{,}992$) |
| boost sklon | 8,18 ($R^2=0{,}981$) |
| $2\pi$ boost-quantum | 2,55 |

dS nese **stejný sub-lineární deficit** ($p_E=0{,}62$, ne $+1$) a Gibbons-Hawkingova $2\pi$ se rovněž NEčte ($2\pi$-bq $=2{,}55$, jiná hodnota než Rindler $9{,}58$ — žádný univerzální $2\pi$). Konzistentní s Rindlerovým obrazem.

---

## Verdikt korespondence: **tautology** — F-034 tautologie přežívá

Podle předregistrovaných kritérií:

| Subtest | Kritérium | Výsledek | Status |
|---------|-----------|----------|--------|
| (A) Unruhův exponent $p_E\to+1$ | $|p_E-1|<0{,}20$, $R^2>0{,}85$ | 0,720 (dev 0,28) | **✗ FAIL** |
| (A) exponent monotónní log-lineární | $p_E>0{,}5$, $R^2>0{,}85$ | 0,720, 0,988 | ✓ (slabý signál) |
| (A) exponent $\rho$-invariantní | CV $<0{,}20$ | 0,024 | ✓ |
| (B) boostová geometrie | $R^2>0{,}85$, sklon$>0$ | 0,969, +29,2 | ✓ |
| (B) boost $\rho$-invariantní | CV $<0{,}15$ | 0,017 | ✓ |
| (C) absolutní $2\pi$ | $|{\cdot}-2\pi|/2\pi<0{,}20$ | 0,524 (best) | **✗ FAIL** |
| (D) interval selhává | $R^2<0{,}5$ | 0,038 | ✓ |
| (D) shuffle selhává | $R^2<0{,}5$ | 0,065 | ✓ |

**Souhrn:** SJ modulární tok na 2D Rindlerově slabu nese **$\rho$-invariantní monotónní boostovou diagonálu** (sklon $29{,}2$, $R^2=0{,}97$, CV $1{,}7\%$), která **čistě selhává na obou kontrolách**. ALE ani **Unruhův zákonný TVAR** (exponent $0{,}72$, ne BW $+1$ — 28% deficit z log-komprese surogátu), ani **absolutní koeficient $2\pi$** (nejlepší routa $9{,}58$, off o 52 %) se z geometrie-fixované normalizace NEobnovují. dS stretch dává tentýž obraz ($p_E=0{,}62$, Gibbons-Hawkingova $2\pi$ nečtena).

To je **netautologický test, který selhal na netautologické straně**: jediný čistý invariant zůstává konstrukcí-řízená boostová diagonála (F-034), bez absolutního Unruhova zákona. **Korespondence „SJ modulární tok ↔ Unruhova teplota" v této surogátní instanci NEplatí kvantitativně** — F-034 tautologie přežívá. Hrana zůstává `barely`.

### Proč to dává fyzikální smysl

Modulární Hamiltonián $K$ je z konstrukce KMS na $\beta=1$ vůči svému vlastnímu modulárnímu času (Tomita-Takesaki). Bisognano-Wichmannovo $2\pi$ je faktor mezi $K$ (modulárně-energetické jednotky $\varepsilon=\ln[\mu/(\mu-1)]$) a **geometrickým boostovým generátorem** (rapidity jednotky). Surogátní kernel postavený z $\varepsilon$ **nefixuje** tuto normalizaci — a navíc jeho log-komprese stlačuje velké modulární energie tak, že i *exponent* zákona je sub-lineární ($0{,}72$ místo $+1$). Měříme tedy, že tok **je boostově-geometrický** (lineární diagonála, $\rho$-invariantní, kontroly selhávají), ale **ani Unruhův zákonný tvar, ani jeho $2\pi$ koeficient** se z této konstrukce nečtou. Obnova $2\pi$ by vyžadovala **non-surogátní Dirac** postavený přímo z geometrického Killingova boostu, ne z $\varepsilon$-spektra.

---

## Co to znamená pro hranu noncommutative-geometry ↔ semiclassical-gravity

Hrana `noncommutative-geometry ↔ semiclassical-gravity` (Connes-Rovelliho tepelný čas ↔ Unruh) má nyní **vlajkový test**:

1. **Connes-Rovelliho framing (modulární tok = tepelný čas) drží KVALITATIVNĚ:** boostová diagonála je $\rho$-invariantní a selhává na kontrolách — modulární tok JE čitelný jako tepelný/boostový čas na causetu.
2. **Unruhova teplota (semiklasická strana) se NEobnovuje:** ani zákonný tvar $T\sim1/x$ (exponent $0{,}72$, ne $-1$ z energie-hustoty exponentu $+1$), ani absolutní $1/(2\pi)$. Most NCG↔semiklasika je v této surogátní instanci **most struktury, ne teploty**.

**Doporučená změna hrany:** ponechat rating **`barely`** a **anotovat** informovaným negativem: „SJ modulární tok na 2D Rindlerově slabu nese $\rho$-invariantní boostovou diagonálu (sklon $29{,}2$, $R^2=0{,}97$, CV $1{,}7\%$, selhává na interval+shuffle), ALE z geometrie-fixované normalizace se NEčte ani Unruhův zákonný tvar (exponent $p_E=0{,}72$, ne BW $+1$), ani absolutní koeficient $2\pi$ (nejlepší routa $9{,}58$, off o 52 %); dS static patch dává tentýž obraz (VYPOCET-32). Most NCG↔semiklasika je v surogátní instanci most struktury (boostová geometrie), NE absolutní Unruhovy/Gibbons-Hawkingovy teploty — F-034 tautologie přežívá."

Hrana zůstává `barely` (vlajkový netautologický test selhal kvantitativně na obou nezávislých invariantech). Příští krok, pokud se hrana znovu otevře: **non-surogátní Dirac** postavený z geometrického boostového generátoru (Killingův vektor $\xi=x\partial_t+t\partial_x$), ne z $\varepsilon$-spektra — to je jediná cesta k absolutnímu $2\pi$, kterou tento surogát ze své podstaty nemůže vydat.

---

## Knihovní příspěvek

Nový composable primitiv v `lib/toe/spectraltriple.py` (vrstva C):

- `unruh_proper_law(K, x_proper, *, x_lo, x_hi, n_bins, min_count)` → `UnruhLawFit(law_exponent, law_r2, boost_slope, boost_r2, centers, prof, counts, n_bins)`: Unruhův teplotní zákon z modulárně-kernelové diagonály vs **PROPER** vzdálenost na **volajícím dodaném** (geometrie-fixovaném, antikruhovém) okně. Vrací log-log exponent $p_E$ (BW: $+1$), jeho $R^2$, lineární boost sklon a binovaný profil. Docstring nese poctivý kaveat o surogátní log-kompresi (exponent sub-lineární, $2\pi$ nečtena).

Čtyři nové testy v `app/tests/test_toe_spectraltriple.py`: (i) konstruovaný BW kernel $|K(x,x)|=2\pi\,x$ → exponent $+1$ na pár %, sklon $=2\pi$; (ii) **antikruhovost** — pod-okno téhož kernelu dává tentýž exponent $+1$ a sklon (výsledek nezávisí na laděném okně); (iii) degenerované okno (vše v jednom binu) → NaN + profil NaNů (čistý parciální výstup).

---

## Limity

- Surogátní $K$ v jednotkách $\varepsilon=\ln[\mu/(\mu-1)]$: log-komprese činí exponent sub-lineárním ($0{,}72$, ne $+1$) a nefixuje boostové rapidity → absolutní $2\pi$ neměřitelná z této konstrukce (dědí F-033/F-034 surogátní kaveat).
- $\beta_{KMS}=1$ je Tomita-Takesaki tautologie (proto se v tomto výpočtu NEměří jako důkaz — jen netautologický exponent a $2\pi$).
- 2D, bezhmotný skalár, konečné $N\le1500$ dense: měříme TREND ($\rho$-invarianci), ne $N\to\infty$. Diskrétní korekce $O(1/\sqrt N)$.
- dS static patch je jednostranný v tortoise $r^*$, proto interní řez $r^*>r_0$ s komplementem (ne $r^*>0$, který je celá oblast bez komplementu); 2D conformal trick (Anninos 1205.3855), ne exaktní zakřivený propagátor.

---

## Reference (ověřené tento běh / přítomné v repu)

- **1611.10281** Sorkin-Yazdi — SJ stav, Pauli-Jordan, $G_R=\tfrac12 C$.
- **1712.04227** Belenchia et al. — Bisognano-Wichmann modulární tok = boost ($K=2\pi K_{\text{boost}}$, Unruhova teplota $1/2\pi$).
- **2008.07697** Surya et al. — SSEE truncace (kontext).
- **0905.2562** Casini-Huerta — jednomódové $\varepsilon=\ln[\mu/(\mu-1)]$, obsazenost $n=\mu-1$.
- **gr-qc/9406019** Connes-Rovelli — *Von Neumann Algebra Automorphisms and Time-Thermodynamics Relation* (modulární tok = tepelný čas).
- **1205.3855** Anninos — de Sitter conformal trick (kontext dS static patch sprinkling).
- Bisognano-Wichmann (references.bib `bisognano1976duality`) + Unruh (`unruh1976notes`) — boostový modulární tok / Unruhova teplota $1/2\pi$ (klasické výsledky).
