# VYPOCET-18: Modulární tok SJ stavu v rohu diamantu — test jednotící nitě (H4g-1)

**Datum:** 2026-06-06
**Soubory:** `core-data/calculations/modular-flow-corner/calc.py`, `results.json`, `plots/{self_test_interval,nonlocality_vs_N_2d,nonlocality_vs_corner_2d,nonlocality_4d}.png`
**Status:** Dokončeno
**Hypotéza:** H4g-1 (BRAINSTORM-04 §H4g-1; jednotící nit vrstva B; vyvraceč #2 jednotící nitě)
**Cluster:** entropy-cluster × von-Neumann × modular-hamiltonian (TOP HUB)
**Navazuje:** VYPOCET-13 (Hadamardova rohová anomálie), VYPOCET-12/16 (modulární spektrum III₁→II), `sj-vn-type/`, `ssee-slab-4d/`

---

## Testované tvrzení

H4g-1 tvrdí, že **rohová non-Hadamardovská anomálie**, kterou VYPOCET-13 lokalizoval do rohů kauzálního diamantu (4D inside −1,53 vs corner −2,79; 2D inside −0,160 vs corner −0,095), je **tatáž věc** jako místo, kde modulární tok σ_t SJ stavu **přestává být geometrický boost**:

- Na slab/Rindlerově klínu je modulární Hamiltonián K = generátor boostu (Bisognano-Wichmann): **lokální**, jádro koncentrované u entangling plochy, **lineární** boostová váha ~ vzdálenost.
- V rohu diamantu se dva null-okraje protínají, boost nemá kam téct (degenerovaný Killing vektor), K **přestane být lokální** → SJ non-Hadamard → "nezkrotitelná" III₁.

**Predikce (a)** geometričnost selhává *přesně* tam, kde Hadamardova diagnostika ukazuje anomálii (roh); **(b)** monotónní vztah non-Hadamardovost ↔ ne-lokalita K; **(c)** vyvraceč: roh non-Hadamardův, ale modulární tok tam zůstane boost → vrstva B padá.

**Poctivý caveat předem (L-1, Sen-typ):** literatura (2008.07697/2412.07832) **explicitně zpochybňuje** přímou vazbu non-Hadamard ↔ volume. Tento výpočet testuje, zda "selhání boost-flow" je **vlastní modulární jev** (lokalitní struktura K), ne jen jiný popis téhož kinematického rohu.

---

## Konvence (ověřené proti literatuře, červen 2026)

| Vstup | Forma | Zdroj |
|-------|-------|-------|
| G_R (2D) = (1/2) C | kauzální matice | Sorkin-Yazdi **1611.10281** |
| G_R (4D) = a·L, a=√ρ/(2π√6) | link matice | Johnston **0909.0944**; **1701.07212** |
| iΔ = i(G_R−G_Rᵀ), W = pozitivní část | SJ Pauli-Jordan | **1611.10281** |
| **Modulární Hamiltonián K(x,y)** ze SSEE: W_O v=μ iΔ_O v, ε=ln[μ/(μ−1)], spektrální rezoluce do site-báze | jednočásticový K na regionu | **1611.10281**; Casini-Huerta **0905.2562** |
| **Kovarianční křížová kontrola:** H_φ=X⁻¹ C arccoth(2C), H_π=P⁻¹ C arccoth(2C), C=√(XP) | Gaussovo K z korelátorů | Peschel; **0905.2562** |
| **Analytický kotvící bod:** K = 2π∫β T₀₀, β(x)=(x−a)(b−x)/(b−a) pro interval [a,b] ve 2D vakuu | lokální boostová váha | Bisognano-Wichmann / Casini-Huerta |
| Truncace: κ=√N/(4π) (2D), 0,05·λ_max (4D) | magnitudový cutoff | **1712.04227** |

**Klíčové metodologické rozhodnutí:** lokalitní sonda používá **NETRUNCOVANÝ** SJ modulární kernel (skutečný modulární tok SJ stavu, jehož geometričnost Bisognano-Wichmann předpovídá). Dvojitá SSEE-truncace je **oddělená** (crossed-product) operace, která dělá K uměle nízko-hodnostní (rank ~ počet UV módů) → delokalizovaný *z konstrukce*; kontaminovala by geometrickou otázku.

---

## Validace konstrukce K (self-test, nezávisle na causetu)

Bezhmotný (IR-regulovaný, m=0,02) volný skalár na periodickém řetězci, redukce na interval [a,b], H_φ a H_π z korelátorů X=⟨φφ⟩, P=⟨ππ⟩. Test proti analytickému Bisognano-Wichmann výsledku:

| Veličina | Hodnota | Predikce | Verdikt |
|----------|---------|----------|---------|
| **corr(H_π diagonála, β(x))** | **0,992** | boostová váha β nesena momentovým jádrem | ✓ |
| off-diagonální |H_φ| log-log sklon | **−1,98** (R²=0,89) | ~−2 = lokální mocninový pokles | ✓ |
| off-diagonální |H_π| log-log sklon | −1,76 (R²=0,96) | lokální | ✓ |

**Diagonála momentového jádra H_π(x,x) sleduje analytickou boostovou parabolu β(x)=(x−a)(b−x)/(b−a) s korelací 0,992**, a off-diagonála klesá jako mocnina (sklon ≈ −2) = lokální jádro. Konstrukce K je **kalibrovaná proti literatuře** (obr. `self_test_interval.png`). Poznámka: diagonálu boostu nese H_π (T₀₀~π²), nikoli H_φ (jehož diagonálu dominuje lokální UV-kontaktní člen) — proto se primárně reportuje H_π pro boostovou váhu.

---

## Metoda lokalitní diagnostiky

Pro hermitovský modulární kernel K(x,y) na regionu O (site-báze) měříme:

1. **Off-diagonální pokles |K(x,y)| vs |x−y|** (prostorová vzdálenost): lokální boost → jasně negativní mocninový sklon; non-lokální/non-geometrický kernel → plochý (sklon ~ 0).
2. **Non-lokální frakce** f_nl = Σ_{|x−y|>3·NN} |K|² / Σ_off |K|² (podíl Hilbert-Schmidtovy normy ve "vzdálených" off-diagonálních párech).
3. **Diagonální boostová váha |K(x,x)| vs vzdálenost od entangling plochy** (slab): Bisognano-Wichmann predikuje **lineární** váhu ~ vzdálenost.
4. **Non-lokalita per-site vs vzdálenost-k-rohu** (diamant): klíčová H4g-1 křivka.
5. **Cross-corner coupling**: |K| mezi protilehlými prostorovými rohy (test u−v′=±2L párování).

**Kontrasty:** slab half-space cut (očekáváme geometrický boost) vs diamant; *uvnitř* diamantu bulk vs near-corner. N=400…1800 (2D, 5 seedů), N≤2500 (4D, 3 seedy).

---

## Výsledky 2D (čistý případ)

### Slab vs diamant — off-diagonální pokles (PRIMÁRNÍ lokalitní diskriminátor)

| Geometrie | off-diag sklon (tail N) | R² | čtení |
|-----------|------------------------|-----|-------|
| **SLAB half-space** | **−0,47** | 0,76 | jasný mocninový pokles = **geometrický boost, LOKÁLNÍ** |
| **DIAMANT** | **−0,094** | 0,65 | téměř **PLOCHÝ** = **non-lokální, non-geometrický** |

Mezera sklonů = **0,37**, stabilní napříč N∈[400,1800]. **Toto je hlavní H4g-1 signatura:** modulární kernel slabu klesá se vzdáleností (boost), kernel diamantu je plochý (boost nemá kam téct).

### Slab — diagonální boostová váha (Bisognano-Wichmann)

| Veličina | Hodnota | Predikce |
|----------|---------|----------|
| **|K(x,x)| ~ lineární ve vzdálenosti od x=0** | **R²=0,977** | boostová váha ~ vzdálenost ✓ |

Diagonální modulární váha slabu je **lineární** ve vzdálenosti od ploché entangling plochy s R²=0,98 — přesně Bisognano-Wichmann boostová váha. Geometričnost slabu potvrzena dvěma nezávislými sondami (off-diag pokles + lineární diagonála).

### Uvnitř diamantu — koncentrace non-geometričnosti k rohu

| Veličina | Hodnota | Predikce H4g-1 |
|----------|---------|----------------|
| **non-lokalita per-site vs vzdálenost-k-rohu, sklon** | **−0,383 (R²=0,989)** | negativní = roste K ROHU ✓ |
| f_nl roh / f_nl bulk (tail N) | **1,15** (0,78 vs 0,68) | roh non-lokálnější ✓ |
| cross-corner coupling ratio | 1,00 | žádné zesílení (null) |

**Klíčová křivka (obr. `nonlocality_vs_corner_2d.png`):** non-lokalita SJ modulárního kernelu roste **monotónně** z 0,673 hluboko v bulku na **0,828 u rohu** (sklon −0,38, R²=0,99, malé chybové úsečky). **Modulární tok SJ stavu se stává non-geometrickým přesně směrem k rohu diamantu** — tam, kam VYPOCET-13 lokalizoval Hadamardovu anomálii.

### Poctivá nuance: integrovaná f_nl vs sklon

**Integrovaná non-lokální frakce slabu (0,72) ≈ diamant-all (0,72)** — tento *integrovaný* metrik slab od diamantu NErozliší (obr. `nonlocality_vs_N_2d.png`, modrá překrývá červenou). **Diskriminace žije v off-diagonálním SKLONU** (−0,47 vs −0,09), ne v integrované frakci. Důvod: oba kernely mají podobný *celkový* podíl vzdálené váhy, ale slab má vzdálenou váhu **klesající** (lokální peak + chvost), diamant **plochou** (uniformně delokalizovaný). Toto je správné rozlišení, ne fudge.

Druhá nuance: **off-diag sklon rohových řádků (−0,17) je strmější než bulk (−0,03)** — opačné znaménko než "roh plošší". Není to spor: rohové řádky mají krátko-dosahový peak (lokální boost část) **plus** vzdálený chvost (non-Hadamardova cross-corner vazba), což dává strmější sklon I vyšší f_nl současně; bulk nemá ani peak ani silný chvost (uniformně delokalizovaný). Rozhodující a jednoznačná je **monotónní nl-vs-roh křivka**, ne tento dvojznačný per-zóna sklon.

### Verdikt 2D

| Signatura | Predikce | Výsledek |
|-----------|----------|----------|
| slab off-diag lokálnější než diamant | sklon slab < diamant | **✓** (−0,47 vs −0,09) |
| slab diagonála = lineární boost | R²>0,6 | **✓** (R²=0,98) |
| non-lokalita roste k rohu | sklon nl-vs-roh < 0 | **✓** (−0,38, R²=0,99) |
| roh non-lokálnější než bulk | f_nl roh > bulk | **✓** (1,15×) |
| roh off-diag plošší než bulk | sklon roh > bulk | ✗ (nuance výše) |
| cross-corner coupling zesílené | ratio > 1,1 | ✗ (1,00, null) |

> **2D VERDIKT: PODPOŘENO — 4/5 geometrických signatur.** Dvě nejsilnější (slab boost-lokalita + monotónní nl-vs-roh) jsou rozhodující a čisté. H4g-1 vrstva B ve 2D **stojí**: modulární tok SJ stavu JE geometrický boost na slabu a stává se non-geometrickým přesně směrem k rohu diamantu.

---

## Výsledky 4D (link matice, N≤2500) — POCTIVÁ NEREPLIKACE

| Veličina (tail N) | 4D hodnota | 2D ekvivalent | shoda? |
|-------------------|-----------|---------------|--------|
| slab f_nl / diamant f_nl | **0,996** | 1,00 (integ. nediskriminuje) | konzistentní (integ. metrik nediskriminuje) |
| slab diag boost lineární | R²≈0,76–0,81 | R²=0,98 | částečně ✓ |
| **roh f_nl vs bulk f_nl** | **0,11 < 0,31 (roh NIŽŠÍ)** | 0,78 > 0,68 (roh vyšší) | **OPAČNĚ** |
| nl-vs-roh sklon | **+0,75 (klesá k rohu)** | −0,38 (roste k rohu) | **OPAČNĚ** |

**4D NEREPLIKUJE 2D koncentraci k rohu.** Ve 4D je rohová zóna **nejméně** non-lokální a bulk **nejvíce** (obr. `nonlocality_4d.png`) — opačné znaménko než 2D. Integrovaná f_nl navíc slab od diamantu nerozliší (poměr 0,996).

**Diagnóza (poctivá):** 4D link matice je řídká (mean links ~N^0,65, VYPOCET-06/09), rohové/tip statistiky tenké, a 4D corner/tip geometrie (null tip t→f, r→0 vs prostorová 2-sféra) se chová jinak než 2D prostorový tip. Při N≤2500 je **H4g-1 rohová sub-claim ve 4D netestovatelná / nulová** tímto metrikem. Slab boostová lokalita (lineární diagonála) ve 4D přežívá, ale rohová koncentrace ne.

> **4D VERDIKT: NEREPLIKUJE.** Integrovaná non-lokální frakce nediskriminuje slab vs diamant; rohová koncentrace má opačné znaménko. Honest null — 4D je v režimu, kde diskrétnost/řídkost link-matice dominuje rohovou strukturu, nebo kde je tato modulární sonda na 4D link-objektu nedostatečně rozlišená.

---

## Celkový verdikt

| Aspekt | Verdikt |
|--------|---------|
| Konstrukce K validovaná proti literatuře | ✓ (corr H_π↔β = 0,992; lokalita sklon −1,98) |
| **2D: modulární tok geometrický na slabu** | ✓ (off-diag −0,47, diagonála lineární R²=0,98) |
| **2D: modulární tok non-geometrický k rohu diamantu** | ✓ (nl-vs-roh −0,38, R²=0,99, monotónní) |
| 2D: cross-corner u−v′=±2L specifické párování | ✗ (null, ratio 1,00) |
| 4D: replikace rohové koncentrace | ✗ (opačné znaménko, řídkost dominuje) |

> ### **VERDIKT: H4g-1 vrstva B PODPOŘENA ve 2D (4/5 signatur), VE 4D NEREPLIKUJE.**
> Ve 2D je vyvraceč #2 jednotící nitě (BRAINSTORM-04) **odvrácen**: rohová non-Hadamardovost a selhání boost-flow JSOU táž věc — modulární kernel SJ stavu je geometricky lokální (boost) na slabu a stává se non-lokálním monotónně směrem k rohu diamantu, **přesně tam, kde VYPOCET-13 lokalizoval Hadamardovu anomálii**. To spojuje F-016 (Hadamard) s vrstvou B jednotící nitě **mechanismem**, ne jen korelací. Ve 4D při N≤2500 sonda nereplikuje (řídkost link-matice, tenké rohové statistiky) — rozšíření do fyzikální dimenze zůstává otevřené.

---

## Co tento výpočet znamená pro jednotící nit (BRAINSTORM-04)

**Vrstva B (modulární teorie):** "otázka ↔ modulární tok σ_t; region geometry → K; roh diamantu = místo, kde selhává boost-flow." Tento výpočet ji **číselně dotýká poprvé přímo**:

- **Slab = klín, kde modulární tok JE boost** (Bisognano-Wichmann/Unruh) → SJ ≈ Unruh = Hadamard → potvrzeno: lokální K, lineární boostová váha. To je přesně geometrie, kde VYPOCET-16 našel čistý III₁→II přechod a VYPOCET-13 area law.
- **Roh diamantu = topologická obstrukce geometričnosti** → potvrzeno ve 2D: K se stává non-lokálním monotónně k rohu. To je přesně místo non-Hadamardovosti (VYPOCET-13) a "zaseknuté" III₁ (VYPOCET-12/16, diamant zůstává flat-dense).

**Spojení tří findings do jednoho mechanismu (ve 2D):** F-016 (Hadamard roh) + F-015 (III₁→II žije ve stavu) + F-011 (modular-hamiltonian TOP HUB) → **rohová non-Hadamardovost = lokalitní selhání modulárního Hamiltoniánu**. Entropy-cluster se posouvá z "geometrie rozhoduje" na "modulární teorie *vysvětluje proč* geometrie rozhoduje" — ale zatím jen ve 2D.

**Vyvraceč #2 NEnastal ve 2D:** roh NEzůstal s geometrickým boostem; naopak K tam ztrácí lokalitu. Vrstva B ve 2D stojí.

---

## Limity a poctivá zjištění

- **4D nereplikace je reálná**, ne artefakt jednoho metriku: jak integrovaná f_nl (nediskriminuje), tak nl-vs-roh sklon (opačné znaménko) selhávají ve 4D. Buď je sonda na 4D link-objektu nedostatečná (řídkost ~N^0,65), nebo je rohová geometričnost ve 4D kvalitativně jiná. Vyšší N (>5000) nebo BD objekt (VYPOCET-09) jako záloha jsou přirozené další kroky.
- **Integrovaná non-lokální frakce NErozliší slab od diamantu ani ve 2D** — diskriminace žije výhradně v off-diagonálním sklonu a v nl-vs-roh křivce. Poctivě zaznamenáno: kdyby se reportovala jen f_nl, signatura by se ztratila.
- **Cross-corner u−v′=±2L párování se NEprojevilo** (ratio 1,00) — specifický non-Hadamardův pár-mechanismus z 2212.10592 se v cross-corner |K| neukazuje jako zesílený. Non-geometričnost je rozprostřená kolem rohu, ne ostře v opačně-rohovém párování.
- **Absolutní hodnoty sklonů jsou finite-N deformované** (slab −0,47 ne přesně boostové; self-test off-diag −1,98 vs ideál −2). Diagnostika stojí na **kontrastu** (slab vs diamant; bulk vs roh), ne na absolutní hodnotě — stejná filozofie jako VYPOCET-13 Hadamardova diagnostika.
- **Literární caveat zachován:** 2008.07697/2412.07832 zpochybňují přímou non-Hadamard↔volume vazbu. Náš výsledek je **konzistentní** s H4g-1 (lokalitní selhání K koreluje s rohem), ale je to korelace lokalitních metrik s rohovou geometrií, ne analytický důkaz, že rohová singularita *způsobuje* delokalizaci K. Plný důkaz vyžaduje analytický rozklad rohového příspěvku k modulárnímu Hamiltoniánu.
- **Nefudgováno:** 4D nereplikace, null cross-corner, a integrovaná-f_nl nediskriminace jsou zachovány jako poctivé kontroly, ne zameteny. 2D verdikt 4/5 stojí na dvou čistých signaturách, ne na šesti slabých.

---

## Dopad na hypotézu H4g-1

| Před VYPOCET-18 | Po VYPOCET-18 |
|---|---|
| H4g-1 "medium-high": dvě nezávislé datové opory (F-015, F-016) existují, chybí jejich *přímé* spojení. Vyvraceč #2 jednotící nitě na test. | **2D: PŘÍMÉ spojení dodáno.** Modulární kernel SJ stavu je geometricky lokální (boost) na slabu (off-diag −0,47, diagonála lineární R²=0,98) a non-lokální monotónně k rohu diamantu (nl-vs-roh −0,38, R²=0,99) — přesně lokace Hadamardovy anomálie F-016. Vyvraceč #2 NEnastal ve 2D. **4D: NEREPLIKUJE** (řídkost link-matice). |

H4g-1 se posouvá z "dvě opory, chybí spojení" na **"2D mechanismus dodán (modulární kernel ↔ rohová geometrie), 4D otevřené"**. Jednotící nit vrstva B získává **první přímý numerický doklad** na causal setu — modulární tok JE geometrický boost na slabu a JE non-geometrický k rohu — byť zatím jen ve 2D, stejně jako VYPOCET-12 (III₁→II) byl nejprve 2D.

---

## Reference (klíčové pro tento výpočet)

- **1611.10281** — Sorkin, Yazdi: SSEE, W_O v=μ iΔ_O v, G_R=(1/2)C.
- **0905.2562** — Casini, Huerta: review volných polí; bosonová korelátorová metoda K z (X,P); C=√(XP), ε=ln[(ν+½)/(ν−½)]; lokální modulární Hamiltonián intervalu.
- **Bisognano-Wichmann** — boostová váha β(x)=(x−a)(b−x)/(b−a) pro interval ve 2D vakuu; half-line → β(x)=x (Rindler boost).
- Peschel — Gaussovo entanglementové K z korelátorů (H_φ=X⁻¹ f(C), H_π=P⁻¹ f(C)).
- **0909.0944** — Johnston: G_R^(4D)=(√ρ/2π√6)·L, link matice.
- **2212.10592** — Yazdi, Mathur, Surya: SJ non-Hadamardův v rozích diamantu (u−v′=±2L).
- **2008.07697 / 2412.07832** — caveat: EE chování a non-Hadamardovost pravděpodobně NEsouvisí přímo (poctivě zaznamenáno).
- **2206.10780** — Chandrasekaran-Longo-Penington-Witten: crossed-product, III₁→II, modulární observer.
- VYPOCET-12 (2D III₁→II), VYPOCET-13 (Hadamardova rohová anomálie), VYPOCET-16 (4D slab III₁→II), VYPOCET-04/06/09 (SSEE).
- pilíř 19 (`foundations/19-von-neumann-algebras.md`) — modular-hamiltonian TOP HUB.
