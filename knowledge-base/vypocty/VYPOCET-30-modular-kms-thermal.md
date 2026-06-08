# VYPOCET-30: Modulární KMS / tepelný čas SJ modulárního toku — tepelná osa causal-sets ↔ noncommutative-geometry (H6g-1)

**Datum:** 2026-06-08
**Soubory:** `core-data/calculations/modular-kms-thermal/calc.py`, `results.json`, `plots/{thermal_occupation_fit,kms_twopoint}.png`; knihovna `lib/toe/spectraltriple.py` (nový primitiv `kms_temperature` + `KMSFit`, test `app/tests/test_toe_spectraltriple.py`)
**Status:** Dokončeno
**Hypotéza:** H6g-1 (BRAINSTORM-06; hrana `causal-sets → noncommutative-geometry`, rating `barely`, INSTANCOVANÁ F-033 jako informovaný negativ na **metrice** — tepelná osa byla netknutá)
**Cluster:** modular-hamiltonian × KMS / thermal-time × Bisognano-Wichmann boost
**Navazuje:** VYPOCET-29 / F-033 (D_K reprodukuje BW boost lineární diagonálu $R^2=0{,}955$, ale Connesova vzdálenost NEsleduje kauzální vzdálenost — metrická osa selhala). H6g-1 testuje DRUHOU osu — tu, kterou F-033 označil za solidní (boostová / tepelně-časová).

---

## Programová otázka

F-033 (VYPOCET-29) ukázal, že surogátní modulární Dirac $D_K=\mathrm{sgn}(K)\sqrt{|K|}$ reprodukuje **boostovou** strukturu (lineární diagonála $K(x,x)$ vs vzdálenost k řezu, $R^2\approx0{,}96$, robustní), ale jeho Connesova vzdálenost **NEsleduje** kauzální vzdálenost (metrická osa SELHALA). H6g-1 se ptá na **tepelnou osu**:

> Reprodukuje SJ modulární struktura / modulární Dirac **tepelný (KMS / Unruhův) obsah**, který spojitá Bisognano-Wichmannova (BW) věta předpovídá — místo prostorové metriky? Na 2D Rindlerově slabu (řez $x>0$) je modulární tok $\sigma_t=e^{iKt}$ boost a SJ stav by měl být KMS (tepelný) na Unruhově teplotě $\beta=2\pi$ vůči boostovému generátoru.

Tento výpočet **instancuje tepelnou osu** téže hrany `causal-sets ↔ noncommutative-geometry`, kterou F-033 instancoval na metrice. Klíčová poctivá distinkce: SJ stav JE z konstrukce (Tomita-Takesaki / Casini-Huerta) KMS stav vůči svému *vlastnímu* modulárnímu Hamiltoniánu $K$ na $\beta=1$ v jednotkách modulární energie. **Dvě ze tří observable jsou proto na $\beta=1$ TAUTOLOGIE konstrukce** — konzistenční kontroly, ne geometrický důkaz. Jediný *netriviální* geometrický (BW/Unruh) obsah je převod na **boostový-rapidity čas** ($\beta=2\pi$), který závisí na normalizaci geometrického boostového generátoru.

---

## Setup (ověřené konvence)

| Vstup | Forma | Zdroj |
|-------|-------|-------|
| Geometrie | 2D slab $\{0<t<0{,}3,\ |x|<1\}$, $T\ll L$ (Rindler-like), `sprinkle_slab2d` | **1611.10281** |
| Kauzální řád + Green | $G_R=\tfrac12 C$ (2D bezhmotný), `causal_matrix`, `green_retarded_2d` | **1611.10281** |
| Pauli-Jordan + SJ stav | $i\Delta=i(G_R-G_R^{\mathsf T})$, $W=$ poz. spektrální část, `pauli_jordan`, `sj_state` | **1611.10281** |
| Řez (Rindler) | $O=\{x>0\}$ (half-line; modulární tok = boost) | BW **1712.04227** (kontext **2008.07697**) |
| Modulární kernel | $K(x,y)$ ze SSEE $W_O v=\mu\,i\Delta_O v$, $\varepsilon=\ln[\mu/(\mu-1)]$, $\kappa=$None (netruncovaný = pravý SJ tok) | Casini-Huerta **0905.2562**; `entropy.modular_kernel` |
| Obsazenost | $n_k=\mu_k-1$ párováno s $\varepsilon_k$ skrz **společné $\mu_k$** | **0905.2562** |
| KMS teplota | sken imag. periody $\beta$ minimalizující $\|G(t)-G(-t-i\beta)\|$ | KMS (Kubo-Martin-Schwinger), Connes-Rovelli **gr-qc/9406019** |
| Boostová diagonála | sklon $d|K(x,x)|/d|x|$, $R^2$, $\rho$-invariance | BW **1712.04227** |

**Kontroly (c):** (i) **interval** $O=\{0<x<0{,}5\}$ — BW NEplatí (intervalový modulární Hamiltonián vrcholí na OBOU koncích, ne lineárně ve vzdálenosti k jednomu konci); (ii) **shuffle** $K'=QKQ^{\mathsf T}$ Haar-ortogonální konjugace (spektrum zachované, geometrie zničena).

**Parametry:** sweep $\rho$ přes $N\in\{300,600,1200\}$ (mez husté `eigh` $\le1500$), 5 seedů/$\rho$ = 15 seedů; wall-clock cap 25 min, skutečný běh **9,9 s**. Schéma `modular-kms-thermal/v1`, atomický + progresivní zápis (per-seed flush).

**Oprava párování (kritická):** carrier `ModularKernel` třídí `eps` a `nu` **nezávisle** vzestupně; jelikož $\varepsilon=\ln[\mu/(\mu-1)]$ KLESÁ s $\mu$, párování `eps[k]`↔`nu[k]` je anti-korelované (corr $\approx-0{,}996$). Funkce `paired_modes` rekonstruuje $\mu=\nu+\tfrac12$ a páruje $\varepsilon_k,\,n_k$ přes společné $\mu_k$, čímž platí $n_k/(n_k+1)=e^{-\varepsilon_k}$ exaktně.

**KAVEAT (poctivý):** $\beta_{occ}=1$ a $\beta_{KMS}=1$ v $\varepsilon$-čase jsou **TAUTOLOGIE** SJ/Casini-Huerta konstrukce (KMS na $\beta=1$ z Tomity-Takesakiho), NIKOLI geometrický důkaz. Jen $\rho$-invariantní boostově-lineární diagonála (selhávající na kontrolách) nese BW geometrii. Surogát NEFIXUJE absolutní Unruhovu $2\pi$ normalizaci. $D_K$ dědí F-033 surogátní kaveat; $\beta=2\pi$ je spojitá hodnota, diskrétní korekce $O(1/\sqrt N)$.

---

## Výsledky

### (a) Tepelná obsazenost — Bose-Einstein, $\beta_{occ}=1$ (tautologie, konzistence)

Per-mód obsazenost $n_k=\mu_k-1$ vs modulární energie $\varepsilon_k=\ln[\mu_k/(\mu_k-1)]$ sleduje Bose-Einsteinův zákon $n(\varepsilon)=1/(e^{\beta\varepsilon}-1)$ na **$\beta_{occ}=1{,}00000$** ($R^2=1{,}000000$, sd$=0$ napříč všemi 15 seedy) — přes 8 dekád (viz `thermal_occupation_fit.png` vlevo). To je **tautologie** Casini-Huertova vztahu, slouží jako sanity check párování, ne jako důkaz.

### (b) KMS dvoubodová funkce — jediné konzistentní $\beta=1$ na strojovou přesnost

Modulární dvoubodová funkce $G(t)=\sum_k[(n_k+1)e^{-i\varepsilon_k t}+n_k e^{+i\varepsilon_k t}]$; sken imaginární periody KMS podmínky $G(t)=G(-t-i\beta)$:

| Veličina (15 seedů) | Hodnota |
|----------------------|---------|
| $\beta_{KMS}$ (minimum rezidua) | **1,00000** (sd $=0$) |
| KMS reziduum při $\beta=1$ | **$1{,}9\times10^{-16}$** |

KMS podmínka platí na **jediném konzistentním $\beta=1$ na strojovou přesnost** — modulární tok JE pravý jednoteplotní KMS (tepelný) tok. Detailní bilance $n/(n+1)=e^{-\beta_{KMS}\varepsilon}$ sedí na $\beta_{KMS}=1{,}0000$ přes 8 dekád (`kms_twopoint.png` vpravo). Primitiv `kms_temperature` nezávisle ověřen testem: na termálním spektru zadaném $\beta_{true}=0{,}7$ vrací $\beta=0{,}70$ — sken NENÍ degenerovaný na 1, hodnota je správná tam, kde má být jiná.

### (a') BW boostová geometrie — lineární, $\rho$-invariantní, ALE bez absolutní $2\pi$

Boostová diagonála $|K(x,x)|$ vs vzdálenost k řezu (klíčový netriviální geometrický signál):

| $\rho$ ($N$) | boost sklon | $R^2$ | $\beta_{KMS}$ | unruh_ratio |
|---|---|---|---|---|
| 500 ($N=300$) | 27,95 | 0,944 | 1,0000 | 0,785 |
| 1000 ($N=600$) | 28,68 | 0,960 | 1,0000 | 0,802 |
| 2000 ($N=1200$) | 26,88 | 0,955 | 1,0000 | 0,769 |
| **agregát** | **27,84 ± 1,35** | **0,953** | **1,0000** | **0,786 ± 0,039** |

Boostový sklon je **$\rho$-invariantní** (CV $=2{,}7\%$ napříč třemi $\rho$) s vysokým $R^2\approx0{,}95$ — geometrický boostový generátor je přítomen a robustní (přesně F-033 lineární diagonála). **Ale absolutní Unruhova $2\pi$ NENÍ obnovena:** `unruh_ratio` $=0{,}786$ (vs $2\pi\approx6{,}283$). Surogátní kernel nefixuje normalizaci boostového rapidity (jednotky $\varepsilon=\ln[\mu/(\mu-1)]$ + site-basis lift nejsou kanonicky $2\pi$-normalizované).

### (c) Kontroly — boostová geometrie SELHÁVÁ, tautologie přežívá

| Kontrola | boost $R^2$ | boost sklon | $\beta_{occ}$ |
|----------|-------------|-------------|---------------|
| **Rindler half-line** | **0,953** | **27,84** | 1,0000 |
| interval $\{0<x<0{,}5\}$ | **0,053** | 0,08 | 1,0000 |
| shuffle $QKQ^{\mathsf T}$ | **0,088** | 0,06 | 1,0000 |

**Diskriminátor čistý:** na obou kontrolách boostová linearita **kolabuje** ($R^2\approx0{,}05$–$0{,}09 \ll 0{,}95$), zatímco tautologická tepelná obsazenost $\beta_{occ}=1$ **přežívá** (spektrum zachované). To dokazuje, že tepelně-OBSAZENOSTNÍ fit je spektrální tautologie a geometrický obsah žije v boostové diagonále (eigenvektorech).

---

## Verdikt korespondence (tepelná osa): **partial** — kvalitativní tepelně-boostový obsah ANO, absolutní Unruhova teplota NE

Podle předregistrovaných kritérií:

| Subtest | Kritérium | Výsledek | Status |
|---------|-----------|----------|--------|
| (a) tepelná obsazenost $\beta_{occ}=1$ | $|\beta-1|<10^{-3}$, $R^2>0{,}999$ | 1,00000, 1,000000 | ✓ (tautologie) |
| (b) KMS jediné $\beta=1$ | $|\beta-1|<0{,}02$, reziduum $<10^{-6}$ | 1,00000, $1{,}9\!\times\!10^{-16}$ | **✓ PASS** |
| (a') boostová geometrie | $R^2>0{,}9$, sklon$>0$ | 0,953, +27,8 | **✓ PASS** |
| (a') boost $\rho$-invariantní | CV $<0{,}10$ | **0,027** | **✓ PASS** |
| (a') absolutní Unruh $2\pi$ | $|r-2\pi|/2\pi<0{,}20$ | 0,786 (ratio) | **✗ FAIL** |
| (c) interval boost selhává | $R^2<0{,}5$ | 0,053 | **✓ PASS** |
| (c) shuffle boost selhává | $R^2<0{,}5$ | 0,088 | **✓ PASS** |

**Souhrn:** SJ modulární tok na Rindlerově slabu **JE pravý jednoteplotní KMS (tepelný) tok** ($\beta_{KMS}=1$ na strojovou přesnost) s **$\rho$-invariantní geometrickou boostovou strukturou** (lineární diagonála $R^2=0{,}95$, CV $2{,}7\%$), která **čistě selhává na obou kontrolách** (interval $R^2=0{,}05$, shuffle $R^2=0{,}09$). To je **kvalitativní pozitiv na tepelně-časové ose** — komplementární k F-033 metrickému negativu. **ALE absolutní Unruhova teplota $2\pi$ NENÍ obnovena** (`unruh_ratio` $=0{,}79$, ne $6{,}28$), protože surogátní kernel nefixuje normalizaci boostového generátoru. Korespondence „SJ modulární tok ↔ NCG tepelný čas (Connes-Rovelli)" v této surogátní instanci **platí kvalitativně** (jednoteplotní KMS + boostová geometrie robustní, kontroly selhávají), ale **NE kvantitativně** (žádná měřená Unruhova $1/2\pi$).

### Proč to dává fyzikální smysl

SJ stav je tautologicky KMS na $\beta=1$ vůči svému $K$ (Tomita-Takesaki). To, co je *netriviální*, je že tento $K$ na Rindlerovsky řezaném slabu **je geometrický boost** (lineární diagonála, $\rho$-invariantní), kdežto na intervalu (BW neplatí) i na shufflu (geometrie zničena) lineární boostová struktura zmizí. Absolutní $2\pi$ je faktor mezi $K$ (modulární čas, $\beta=1$) a geometrickým boostovým generátorem (rapidity čas, $\beta=2\pi$); ten závisí na *normalizaci* boostového generátoru, kterou surogát $D_K$ (postavený z $\varepsilon=\ln[\mu/(\mu-1)]$, ne z geometrického Killingova boostu) nefixuje. Proto měříme, že tok **je tepelný a boostově-geometrický**, ale ne *na jaké absolutní teplotě* v rapidity jednotkách.

---

## Co to znamená pro hranu causal-sets ↔ noncommutative-geometry a pro program

**Hrana `causal-sets ↔ noncommutative-geometry`** (`barely`, F-033 informovaný negativ na metrice) má nyní **instancovanou i tepelnou osu**:

1. **Tepelná / KMS strana funguje kvalitativně:** SJ modulární tok JE jednoteplotní KMS tok ($\beta_{KMS}=1$ na strojovou přesnost) s $\rho$-invariantní geometrickou boostovou strukturou, čistě selhávající na non-Rindler kontrolách. To poprvé **podpírá daty** čtení modulárního toku jako Connes-Rovelliho tepelného času (gr-qc/9406019) na causetu — komplementárně k F-033 metrickému negativu.
2. **Kvantitativní Unruh NEfunguje:** absolutní teplota $1/2\pi$ se z surogátu nečte (unruh_ratio $0{,}79$, ne $2\pi$). Surogátní modulární Dirac nese *tepelně-boostovou strukturu*, ne *absolutní Unruhovu teplotu*.

**Doporučená změna hrany:** ponechat rating **`barely`**, ale **anotovat** o tested kvalitativní pozitiv: „SJ modulární tok na 2D Rindlerově slabu je jednoteplotní KMS tok ($\beta_{KMS}=1$ exaktně) s $\rho$-invariantní boostovou geometrií ($R^2=0{,}95$, CV $2{,}7\%$), selhávající na interval + shuffle kontrolách (VYPOCET-30) — tepelně-časová osa korespondence je daty podpořena KVALITATIVNĚ; absolutní Unruhova teplota $1/2\pi$ se ze surogátu nečte." Hrana zůstává `barely`, protože pozitiv je kvalitativní (jediný měřený absolutní invariant — $2\pi$ — selhal), ale je nyní **informovaný pozitiv na tepelné ose** vedle informovaného negativu na metrické (F-033).

**Pro draft „mapa selhání" (H6g-7):** F-033 + F-034 dávají koherentní dvouosý obraz: surogátní modulární Dirac nese **boostově/tepelně-časovou** geometrii (KMS jednoteplotní, boostová diagonála $\rho$-invariantní), ale ani **prostorovou metriku** (Connes, F-033), ani **absolutní Unruhovu teplotu** (F-034) — obojí vyžaduje non-surogátní Dirac postavený z kauzální/geometrické struktury samé. To NENÍ „nic nefunguje": tepelná OSA má kvalitativní datovou oporu, kterou metrická osa postrádá.

---

## Knihovní příspěvek

Nový composable primitiv v `lib/toe/spectraltriple.py` (vrstva C):

- `kms_temperature(eps, occ)` → `KMSFit(beta, resid_beta1, resid_min, ts, g_re, g_im, n_modes)`: KMS inverzní teplota jednočásticového modulárního toku ze sken imag. periody dvoubodové funkce $G(t)=\sum_k[(n_k+1)e^{-i\varepsilon_k t}+n_k e^{+i\varepsilon_k t}]$, minimalizace rezidua $\|G(t)-G(-t-i\beta)\|/\|G(t)\|$. Pro SJ tok vrací $\beta=1$ na strojovou přesnost; pro spektrum zadané $\beta_{true}$ vrací $\beta_{true}$ (ne degenerované na 1).

Tři nové testy v `app/tests/test_toe_spectraltriple.py`: (i) SJ tok ($n=\mu-1$, $\varepsilon=\ln[\mu/(\mu-1)]$) → $\beta=1$, reziduum $<10^{-9}$; (ii) termální spektrum $\beta_{true}=0{,}7$ → $\beta=0{,}70$ (sken je kalibrovaný, ne triviální); (iii) degenerovaný vstup ($<2$ módy) → NaN + prázdné křivky (čistý parciální výstup).

---

## Limity

- $\beta_{occ}=1$ a $\beta_{KMS}=1$ jsou **tautologie** SJ konstrukce, ne geometrický důkaz — jediný netriviální invariant je $\rho$-invariantní boostová diagonála (a ta absolutní $2\pi$ NEdává).
- Surogát $D_K$ nefixuje normalizaci geometrického boostového generátoru → absolutní Unruhova $1/2\pi$ není měřitelná z této konstrukce (dědí F-033 surogátní kaveat).
- Konečné $N$ porušuje spojitý modulární tok; měříme TREND ($\rho$-invarianci, $N\le1500$ dense), ne $N\to\infty$ hodnotu. Boostová diagonála saturuje na vzdáleném okraji slabu (konečná šířka).
- 2D slab, bezhmotný skalár; intervalová kontrola používá vzdálenost k $x=0$ (intervalový modulární Hamiltonián vrcholí na obou koncích — proto $R^2\approx0$ ve vzdálenosti k jednomu konci, korektní non-BW signál).

---

## Reference (ověřené tento běh / přítomné v repu)

- **1611.10281** Sorkin-Yazdi — SJ stav, Pauli-Jordan, $G_R=\tfrac12 C$.
- **1712.04227** Belenchia et al. — Bisognano-Wichmann modulární tok = boost (Unruhova teplota $1/2\pi$ kontext).
- **2008.07697** Surya et al. — SSEE truncace (kontext, $\kappa$).
- **0905.2562** Casini-Huerta — jednomódové $\varepsilon=\ln[\mu/(\mu-1)]$, obsazenost $n=\mu-1$ (repo-present, použito napříč lib + 18 calc dir).
- **gr-qc/9406019** Connes-Rovelli — *Von Neumann Algebra Automorphisms and Time-Thermodynamics Relation* (modulární tok = tepelný čas; motivace KMS čtení). Ověřeno tento běh.
- **1305.2588** Dowker-Glaser — causal-set d'Alembertiány (kontext BD objektů).
- Bisognano-Wichmann (references.bib `bisognano1976duality`, *On the Duality Condition for Quantum Fields*) + Unruh (`unruh1976notes`) — boostový modulární tok / Unruhova teplota $1/2\pi$ (klasické výsledky).
