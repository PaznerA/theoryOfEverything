# VYPOCET-09: SSEE na 4D kauzálním diamantu s Benincasa-Dowker nelokálním d'Alembertiánem — rozhodující test interpretace (b) z H04

**Datum:** 2026-06-06
**Soubory:** `core-data/calculations/ssee-bd-4d/calc.py`, `results.json`, `plots/{spectrum_compare,rank_vs_N,area_law,smeared_compare,alpha_drift}.png`
**Status:** Dokončeno
**Cluster:** entropy-cluster (navazuje na VYPOCET-04 2D, VYPOCET-06 4D link-matice; testuje H04 §2b)

---

## Cíl

Rozhodující test interpretace **(b)** hypotézy H04. VYPOCET-06 ukázal, že ve 4D s **link maticí** jako retardovanou Greenovou funkcí (Johnston 0909.0944) je SJ Pauli-Jordanovo spektrum **ploché** (ne mocninové), exponent škálování entropického cutoffu je cutoff-závislý (0.65–0.98), predikce p = 3/4 není robustní, a SSEE dává volume law. Interpretace (b) tvrdí, že link matice je **špatný objekt** a že **Benincasa-Dowker (BD) nelokální d'Alembertián** — explicitně konstruovaný tak, aby měl kontrolovanou kontinuum-limitu — dá:

1. **čistý mocninový zákon** λ_k ~ k^(−α) (oproti plochému link-spektru);
2. **robustní** exponent škálování ranku, blíže predikci p = 3/4;
3případně **area law** místo volume law.

Postup (dle zadání): (1) ověřit přesné BD koeficienty a normalizaci; (2) postavit B jako matici na sprinklovaném 4D diamantu; (3) získat G_R = B⁻¹ s ověřenou retardovaností; (4) spustit SSEE protokol.

---

## Vstupy s citacemi (ověřeno z primární literatury, červen 2026)

### Ostrý BD d'Alembertián ve 4D (Benincasa-Dowker, arXiv:1001.2725, rov. 2-3)

> Pozn.: H04 cituje "0911.2563" — to je překlep, správné arXiv ID je **1001.2725** ("The Scalar Curvature of a Causal Set", PRL 104, 181301 (2010)).

$$B\phi(x) = \frac{4}{\sqrt{6}\,l^2}\left[-\phi(x) + \left(\sum_{y\in L_1} - 9\sum_{y\in L_2} + 16\sum_{y\in L_3} - 8\sum_{y\in L_4}\right)\phi(y)\right]$$

- **Koeficienty vrstev:** (1, −9, 16, −8) — ověřeno přesně.
- **Vrstvy:** $L_i = \{y \prec x : n(x,y) = i-1\}$, kde $n(x,y)$ = počet prvků **striktně mezi** $y$ a $x$ = $|I(x,y)|-2$ = $(C\cdot C)[x,y]$ (počet 2-krokových kauzálních řetězců). $L_1$ = linky ($n=0$), $L_2$: $n=1$, $L_3$: $n=2$, $L_4$: $n=3$.
- **Prefaktor:** $4/(\sqrt6\,l^2)$; v 4D $l^4 = 1/\rho$, tedy $1/l^2 = \sqrt\rho$, takže prefaktor $= 4\sqrt\rho/\sqrt6$.

### Smeared (nelokální) BD (Aslanbeigi-Saravani-Sorkin, arXiv:1305.2588, rov. 25-26; spektrální dimenze Belenchia et al. 1507.00330)

$$B_\epsilon^{(d)}\phi(x) = \frac{\epsilon^{2/d}}{l^2}\left[\alpha_d\,\phi(x) + \beta_d\,\epsilon\sum_{y\prec x} f_d(n,\epsilon)\,\phi(y)\right],\quad f_d(n,\epsilon)=(1-\epsilon)^n\sum_{i=1}^{N_d}C_i^{(d)}\binom{n}{i-1}\left(\frac{\epsilon}{1-\epsilon}\right)^{i-1}$$

- d=4: $\alpha_4=-4/\sqrt6$, $\beta_4=4/\sqrt6$, $C^{(4)}=(1,-9,16,-8)$. d=2: $\alpha_2=-2$, $\beta_2=4$, $C^{(2)}=(1,-2,1)$.
- $\epsilon=(l/\xi)^d\in(0,1]$ je nelokální parametr; $\epsilon\to1$ obnoví ostrý operátor.

### Konstrukce G_R a SSEE

| Vstup | Forma | Zdroj |
|-------|-------|-------|
| G_R = B⁻¹ | inverze BD operátoru | tento výpočet (viz retardovanost níže) |
| iΔ = i(G_R − G_Rᵀ), W = pozitivní část | SJ Pauli-Jordan | 1611.10281; 2008.07697 |
| SSEE W_O v = μ iΔ_O v, S = Σ μ ln\|μ\| | dvojitá truncace κ | 1611.10281; 1712.04227 |
| rank ~ N^((d−1)/d) = N^(3/4) | area-law ansatz | 2008.07697 |

---

## Metoda a numerika

- **Geometrie a sprinkling:** identické s VYPOCET-06 (4D diamant {|t|+|r|≤T}, Vol = (2/3)π, ρ = N/Vol, přesné vzorkování bez rejection).
- **B jako matice:** $B[x,y]$ = prefaktor × koeficient vrstvy pro $y\prec x$ (ostrý) nebo prefaktor × $\beta_4\epsilon f_4(n,\epsilon)$ (smeared); diagonála $-$prefaktor (ostrý) resp. prefaktor × $\alpha_4$ (smeared). Vrstva se určí z $n=(C\cdot C)[x,y]$.
- **Retardovanost (jak je vynucena a ověřena):** body se seřadí **podle globálního času $t$**, což je kauzální zjemnění ($y\prec x \Rightarrow t_y<t_x$). V tomto pořadí je B **přesně dolní trojúhelníková** (ověřeno: max|triu(B,1)| = 0). Inverze dolní trojúhelníkové matice je dolní trojúhelníková ⇒ $G_R = B^{-1}$ je **automaticky retardovaná** (nesena na kauzální minulosti). Ověřeno: max|triu(G_R,1)|/diag ~ 10⁻¹¹ (strojová nula). Reziduum inverze ‖BG−I‖_max ~ 10⁻⁹.
- **N až 3000, 3 seedy.** Inverze + eigh jsou O(N³); celý běh 394 s. Eigenvalues iΔ ověřeny jako přesně ±-párované.
- **Klíčová oprava SSEE oproti VYPOCET-06:** lokální truncace musí být relativní k **lokální** spektrální škále, ne globální κ. Pro strmé BD spektrum (λ_max ~ 4·10⁵) by globální κ vynulovalo celé lokální spektrum (bug S=0). Truncace nyní jako **frakce λ_max** zvlášť globálně a lokálně.

---

## Výsledky

### 1. Tvar spektra — ČISTÝ MOCNINOVÝ ZÁKON (predikce (b) na tvaru POTVRZENA)

Klíčový pozitivní nález. Na **stejném sprinklingu** (N=3000):

| Objekt | Mocninový fit λ_k ~ k^(−α) | R² |
|--------|---------------------------|-----|
| **BD G_R = B⁻¹** | α ≈ 3.0–3.4 | **0.990–0.995** |
| link matice (VYPOCET-06) | α ≈ 0.58 | 0.924 |

BD spektrum je **čistá přímka přes ~6 dekád** v log-log (`spectrum_compare.png`, pravý panel — modrá), kdežto link matice má charakteristický plochý-pak-útes tvar (oranžová). Toto je **kvalitativně to, co interpretace (b) předpovídala**: BD objekt skutečně dává čistý mocninový zákon tam, kde link matice dávala ploché spektrum.

### 2. Exponent α NENÍ konvergovaný — drift s N (rozhodující komplikace)

Mocninový zákon je čistý **při každém N** (R²≈0.99), ale jeho **sklon α se systematicky mění s N**:

| N | 500 | 800 | 1200 | 1600 | 2200 | 3000 |
|---|-----|-----|------|------|------|------|
| α | 2.13 | 2.34 | 2.71 | 2.85 | 3.09 | 3.41 |
| cond(B) | 3.9e6 | 3.1e7 | 5.5e7 | 3.3e8 | 4.1e9 | 2.0e10 |

α monotónně roste o **+1.28** přes naši dekádu N a **sleduje cond(B)**, který roste o 4 řády (`alpha_drift.png`). Tedy: neexistuje jediný N-stabilní spektrální exponent, který by se dal identifikovat s cutoffem. Kontrola: i **dobře podmíněný smeared operátor** (ε=0.3, cond~10³) má drift α: 0.89 (N=800) → 1.00 (N=1500) → 1.12 (N=2500). Drift tedy **není čistě artefakt podmíněnosti** — finite-N BD spektrum konverguje ke kontinuum-limitě pomalu a při N≤3000 ještě nedosáhlo stabilního exponentu.

### 3. Škálování ranku — žádný robustní p ≈ 3/4 (predikce (b) na exponentu VYVRÁCENA)

| Cutoff definice | p | odchylka od 3/4 |
|-----------------|-----|------------------|
| rank @ 0.02·λmax | 0.106 ± 0.284 | −2.3 σ |
| rank @ 0.05·λmax | 0.281 ± 0.235 | −2.0 σ |
| rank @ 0.10·λmax | −0.176 ± 0.332 | −2.8 σ |
| rank @ λ>1·√ρ (absolutní práh) | 1.163 ± 0.019 | +21.7 σ |
| rank @ λ>3·√ρ | 1.473 ± 0.032 | +22.6 σ |
| rank @ λ>10·√ρ | 1.718 ± 0.066 | +14.7 σ |
| **slope-knee (2008.07697)** | **0.977 ± 0.007** | **+33.4 σ (≈ N¹)** |

**Žádná definice cutoffu nedává robustní 3/4.** Frakční cutoffy dávají p≈0 (přesně očekávané pro čistý mocninový zákon: pro λ_k = λ_1 k^(−α) je rank @ frac·λmax = frac^(−1/α), tedy **N-nezávislý**). Absolutní prahy dávají p ∈ [1.16, 1.72] **driftující s volbou prahu** (protože α driftuje). Slope-knee dává p ≈ 0.98 ≈ N¹ — **stejně jako VYPOCET-06** (tam 0.985). Hodnota 3/4 není trefena žádnou robustní spektrální feature.

### 4. Area vs volume law — INCONCLUSIVE (cutoff-závislé)

| Truncace | S ~ f^p | R²(area) | R²(vol) | verdikt |
|----------|---------|----------|---------|---------|
| žádná | f^3.92 | 0.989 | 0.942 | AREA (super-area) |
| frac 0.02 | f^0.43 | 0.028 | 0.022 | INCONCLUSIVE |
| frac 0.05 | f^0.30 | 0.002 | 0.001 | INCONCLUSIVE |
| frac 0.10 | f^8.94 | 0.534 | 0.646 | VOLUME |
| frac 0.20 | f^(−28.6) | 0.189 | 0.188 | INCONCLUSIVE |

Verdikt napříč cutoffy: [AREA, INCONCLUSIVE, INCONCLUSIVE, VOLUME, INCONCLUSIVE] → **INCONCLUSIVE (cutoff-závislé)**. Netruncovaná SSEE dává super-area law S~f^3.9 (R²area=0.989, mezi area f² a volume f⁶); jakákoli truncace ale verdikt rozhází — strmé spektrum + malý zachovaný rank činí SSEE necitlivou na geometrii. **Stejná metodologická lekce jako VYPOCET-06: výsledek visí na arbitrární volbě cutoffu.**

### 5. Smeared BD jako cross-check (interpretace (iii))

| ε | režim | cond(B) | α | R² |
|---|-------|---------|-----|-----|
| 0.3 | smeared | 1.6e3 | 1.09 | 0.979 |
| 0.6 | smeared | 4.6e5 | 1.98 | 0.991 |
| 1.0 | sharp | 3.8e8 | 3.15 | 0.994 |

Smeared operátor je dramaticky lépe podmíněný (ε=0.3: cond~10³ vs ostrý ~10⁸) a dává také čistý mocninový zákon — ale **menší α** a stejný N-drift. Smeared rank-škálování (ε=0.6) dá p ≈ 2.07–2.30 — opět ne 3/4. Smeared verze tedy **léčí podmíněnost, ale ne nekonvergenci exponentu**.

---

## Interpretace pro hypotézu

**Hlavní verdikt: interpretace (b) je VYVRÁCENA na své ústřední tezi (robustní p ≈ 3/4), ačkoli její dílčí predikce (čistý mocninový zákon) je POTVRZENA.**

Honest outcome je směs (i) + (ii) + (iii) ze zadání:

- **(i) potvrzeno částečně:** BD G_R **skutečně dává čistý mocninový zákon** λ_k ~ k^(−α) (R²≈0.99), kvalitativně odlišný od plochého link-spektra (R²=0.92 a charakteristický útes). Interpretace (b) měla pravdu, že link matice je „špatný objekt" pro tvar spektra — BD objekt dává to, co 2D čistota slibovala.

- **(ii) hlavní výsledek — vyvráceno:** Čistý tvar **nevede k robustnímu exponentu**. (a) Exponent α driftuje s N (+1.28 přes dekádu N) a nekonvergoval při N≤3000. (b) Žádný cutoff nedá robustní p≈3/4: frakční cutoffy → p≈0, absolutní prahy → p∈[1.2,1.7] driftující, slope-knee → p≈0.98≈N¹ (identicky jako VYPOCET-06). (c) Area vs volume zůstává cutoff-závislé/inconclusive. Predikce p = 3/4 = (d−1)/d tedy **nemá robustní spektrální protějšek ani s BD objektem**.

- **(iii) zdokumentováno:** Ostrý BD operátor je **numericky problematický** — cond(B) roste ~N^2.5 na 2·10¹⁰ při N=3000, λ_max ~ 4·10⁵ (G_R entries spaní 30 řádů: medián ~10⁻¹⁵, max ~10⁴; inverze koncentrovaná na řídký near-lightcone pás). Smeared BD (ε≤0.6) dramaticky zlepší podmíněnost (cond~10³), což vyloučí, že drift α je čistě podmíněnostní artefakt — drift přetrvává i pro dobře podmíněný smeared operátor. Drift je tedy **fyzikální pomalost kontinuum-limity**, ne jen numerika.

**Důsledek pro entropy-cluster / H2g-3:** Výměna link matice → BD d'Alembertián **opravila tvar spektra** (plochý → mocninový), ale **neoživila** predikci p = 3/4 ve 4D. Selhání VYPOCET-06 tedy **není** specifické pro link-matrix objekt (jak interpretace (b) tvrdila) — je obecnější: ani správně zkonstruovaný kontinuum-aproximující objekt (BD) nedá při dostupných N robustní area-law exponent. To posouvá váhu k **interpretaci (a)** (2D-only kuriozita: čistý exponent je specifický pro konformně triviální 1+1D) nebo **(c)** (volume law je skutečná non-Hadamardovská fyzika SJ stavu na diamantu). Trojcestná identifikace (SSEE cutoff = crossed-product cutoff = LQG area gap) **nadále nemá numerický pilíř ve 4D**.

**Co BD objekt přidal pozitivního:** Spektrální dimenze (Belenchia et al. 1507.00330) a čistý mocninový tvar naznačují, že **kdyby** se podařilo dosáhnout kontinuum-limity (ρ → ∞, kde α konverguje), mohl by existovat dobře definovaný spektrální exponent. To je testovatelné, ale vyžaduje N ≫ 3000 (limitované O(N³) inverzí + eigh) nebo analytický výpočet asymptotiky α(ρ). Otevřená cesta, ne potvrzení.

---

## Limity výpočtu

- **α nekonvergoval při N≤3000.** Hlavní limit: spektrální exponent driftuje s N a nedosáhl plató. Závěr „ne 3/4" je robustní pro dostupná N, ale konvergovaná hodnota α(∞) není známa. Vyžadovalo by N ~ 10⁴–10⁵ nebo analytickou asymptotiku.
- **cond(B) ostrého operátoru až 2·10¹⁰** při N=3000. Float64 (dynamický rozsah ~10¹⁶) inverzi zvládá (reziduum ~10⁻⁹), ale strmý tail spektra (λ až 10⁻¹⁵) je u nejmenších vlastních čísel na hranici strojové přesnosti — proto rel_floor=10⁻¹⁰·λ_max pro odříznutí inverzního šumu (dokumentováno, citlivost reportována). Smeared ε=0.3 (cond~10³) je čistá alternativa pro budoucí běhy.
- **Area-law degenerace.** Pro strmé spektrum zachová frakční truncace jen hrstku modů, takže SSEE je necitlivá na velikost subregionu → R²≈0. Není to bug, je to vlastnost strmého spektra; reportováno jako inconclusive napříč 5 cutoffy.
- **Pouze nested concentric diamanty** (jako VYPOCET-06), ne de Sitter slab / Rindler. Literatura (2008.07697) dosahuje area law jen ve slab geometrii — náš protokol ji netestuje (viz limity VYPOCET-06).
- **3 seedy** (oproti 4 ve VYPOCET-06) kvůli O(N³) inverzi navíc; statistická síla fitů je dostatečná pro kvalitativní závěr (drift, ne-3/4), ne pro přesné α(N).

---

## Souhrn pro H04

| Aspekt predikce (b) | Predikce | Výsledek | Verdikt |
|---------------------|----------|----------|---------|
| Tvar spektra | čistý mocninový zákon | α≈3, R²=0.99 (vs link R²=0.92) | **POTVRZENO** |
| N-stabilita exponentu | robustní α | α drift +1.28, nekonverg. | vyvráceno |
| Rank-škálování | p ≈ 3/4 | 0.1 / 1.2–1.7 / 0.98 (cutoff-záv.) | **VYVRÁCENO** |
| Area law | area místo volume | inconclusive (cutoff-záv.) | nepotvrzeno |
| Numerika | (b) předp. proveditelné | cond~2e10, smeared léčí podmíněnost | (iii) zdokumentováno |

**Závěr:** Interpretace (b) **správně předpověděla čistý mocninový tvar** BD spektra, ale **mýlila se v tom, že to oživí 4D hypotézu** — robustní p = 3/4 chybí i s BD objektem. Selhání VYPOCET-06 není objekt-specifické (link matice), nýbrž hlubší. Hypotéza H2g-3 ve 4D zůstává bez numerického pilíře; váha se posouvá k interpretacím (a) a (c). Doporučení: (a) algebraický Hadamard test SJ stavu na diamantu vs Rindler (interpretace (c)); (b) 3D link-matrix test (interpretace (a), rychlejší); (c) BD při N ~ 10⁴ pro konvergenci α (drahé).

---

## Citace (prohledané/použité arXiv IDs)

- **1001.2725** — Benincasa, Dowker, *The Scalar Curvature of a Causal Set* (PRL 104, 181301): ostrý 4D BD d'Alembertián, koeficienty (1,−9,16,−8), prefaktor 4/(√6 l²), vrstvy L_i = {n=i−1}. (H04 cituje chybně jako 0911.2563.)
- **1305.2588** — Aslanbeigi, Saravani, Sorkin, *Generalized causal set d'Alembertians*: smeared operátor B_ε, f_d(n,ε), α_d/β_d konstanty, ε=(l/ξ)^d.
- **1507.00330** — Belenchia, Benincasa, Liberati, Marin, Marino, Bassi, *Spectral Dimension from Nonlocal Dynamics on Causal Sets*: nelokální d'Alembertián, d_s → 2.
- **0909.0944** — Johnston: link-matrix G_R (VYPOCET-06 objekt, zde pro srovnání).
- **1611.10281** — Sorkin-Yazdi: SSEE formule, dvojitá truncace.
- **2008.07697** — Surya, Nomaan X, Yazdi: n_max ~ N^(3/4), slope-knee, area/volume.
- **1712.04227** — dvojitá truncace, 4D volume law.
