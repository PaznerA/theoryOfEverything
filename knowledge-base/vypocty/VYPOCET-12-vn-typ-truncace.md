# VYPOCET-12: von-Neumannovy TYPE-diagnostiky SSEE truncace — numerický test crossed-product obrazu (H3g-3)

**Datum:** 2026-06-06  
**Soubory:** `core-data/calculations/sj-vn-type/calc.py`, `results.json`, `proxy1_trace.png`, `proxy2_modular_density.png`, `proxy2_modular_trends.png`, `proxy3_central_seq.png`  
**Status:** Dokončeno  
**Hypotéza:** H3g-3 (BRAINSTORM-03 §H3g-3; H04 §1; pilíř 19 otevřený problém #6)  
**Cluster:** entropy-cluster × von-Neumann (modular-hamiltonian TOP HUB)

---

## Testované tvrzení

H3g-3 tvrdí, že **dvojitá truncace** v Sorkinově SSEE — operace, která mění objemový zákon (volume law) na plošný/logaritmický (area/log law) — **JE přechod typu III₁ → typ II** podkladové lokální von-Neumannovy algebry. Diskrétní škála (magnitudový cutoff κ = √N/(4π)) má hrát roli **modulárního / pozorovatelského (crossed-product) cutoffu**, jenž regularizuje jinak bezstopovou algebru typu III₁.

Toto je **první numerická sonda crossed-product obrazu na kauzálních množinách** (pilíř 19: hrana causal-sets → von-Neumann je „sotva prozkoumána"; otevřený problém #6: „odvodit truncaci a vztáhnout ji k regulované entropii typu II").

### Metodologický problém: „typ" je nekonečně-dimenzionální pojem

Na konečné kauzální množině je každý operátor konečná matice a každá algebra je triviálně typu I_n (= B(ℂⁿ)). **Typ nelze měřit přímo.** Proto jsem navrhl tři **poctivé konečné-N proxy**, jejichž signatura je v **TRENDU** s N (N = 400…1800, 2D — čistý případ), s chybovými úsečkami přes **8 seedů** (požadavek ≥ 4 splněn). Každý proxy: jasná predikce → měření → N-škálování.

---

## Konvence (ověřené proti literatuře)

Identické se SJ konstrukcí z VYPOCET-04 (`ssee-diamond`):

- **G_R = (½)C**, C_xy = 1 pokud y ≺ x. *(Sorkin-Yazdi 1611.10281)*
- **iΔ = i(G_R − G_Rᵀ)**, hermitovský, vlastní čísla v párech ±|λ|.
- **W_SJ = pozitivní část iΔ.**
- **SSEE:** W_O v = μ (iΔ_O) v na koncentrickém subdiamantu (frac = 0.5); S = Σ μ ln|μ|; páry (μ, 1−μ).
- **Dvojitá truncace:** zahodit |λ| ≤ κ s κ = √N/(4π) globálně i lokálně. *(1712.04227)*

**Modulární Hamiltonián z Gaussova stavu** (standardní bosonová korelátorová metoda, ověřeno přes Casini-Huerta 0905.2562 a arXiv:2501.09669, červen 2026):
z korelátorů C = √(X·P) plynou symplektická vlastní čísla ν_k ≥ ½, modulární energie

> **ε_k = ln[(ν_k + ½)/(ν_k − ½)]**, &nbsp; entropie S = Σ [(ν+½)ln(ν+½) − (ν−½)ln(ν−½)].

V kovariantní SJ řeči nese tutéž fyziku zobecněné vlastní číslo μ (páry μ, 1−μ). Jeden bosonový mód s obsazením n má ρ ∼ e^(−ε n); pár (μ, 1−μ) s μ > 1 (= ν + ½) dává

> **ε = ln[μ/(μ−1)]**, &nbsp; ε ∈ (0, ∞), &nbsp; ν = μ − ½.

ε → 0 znamená μ → ∞ (silně obsazený, „objemový" mód); ε → ∞ znamená μ → 1⁺ (UV-věrný mód blízko continua). **Connesův modulární invariant S(M) se staví právě z tohoto modulárního spektra.** Poznámka: Jones-Yazdi „Spectral Spacetime Entropy for Quasifree Theories" (arXiv:2602.16782, 2026) nezávisle propojuje SSEE s kovariančně-maticovým modulárním formalismem — přímá literární opora pro tuto identifikaci.

---

## Tři proxy: predikce, měření, výsledek

### PROXY 1 — Divergence stopy (bezstopová = III; konečná stopa = II)

**Klíčové rozlišení dvou „stop":**

**(A) Entropická stopa S = −Tr(ρ ln ρ)** — skutečný von-Neumannův stopový funkcionál. Typ III: žádná konečná stopa → diverguje. Typ II: konečná stopa → saturuje.

| veličina | exponent a (S ∼ Nᵃ) | chování |
|---|---|---|
| S_full (netruncovaná) | **a = 1.04** | objemový zákon, R²(vs n_sub) = 0.9993 → **divergentní stopa (III)** |
| S_trunc (truncovaná) | **a = 0.17** (saturuje 1.30 → 1.70) | area/log zákon, S ∼ 0.256 ln N → **konečná stopa (II)** |

Při N = 1800 truncace kolabuje stopu **80×** (135.9 → 1.70). Toto je **přímá entropická signatura III → II**.

**(B) Pauli-Jordanova nukleární norma Tr\|iΔ_O\| = Σ|eig(iΔ_O)|** — kinematický objekt (symplektická forma), kontrola:

| veličina | exponent a | 
|---|---|
| Tr\|iΔ_O\| full | a = 1.20 |
| Tr\|iΔ_O\| trunc | a = 1.14 (poměr trunc/full ≈ 0.78 = konstantní) |

**Poctivé zjištění:** PJ nukleární norma roste ∼N pro full I trunc — magnitudový cutoff κ odebírá jen **konstantních ~20 %**, NIKOLIV divergenci. Typová signatura tedy NENÍ v symplektické formě, ale **ve stavu/entropii**. (To je správné: typ je vlastnost stavu na algebře, ne kinematiky.)

**Verdikt proxy 1 (na rozhodující entropické stopě): III → II ✓**

### PROXY 2 — Modulární spektrum (S(M) = ℝ₊ plochá hustá = III₁; integrabilní = II)

Modulární spektrum {ε_k} = ln[μ_k/(μ_k − 1)] na subdiamantu, před vs. po truncaci.

**Connesova III₁ signatura:** spektrum vyplňuje ℝ husté s **plochou** (škálově-invariantní) hustotou, jež NEINTEGRUJE — počet módů u ε = 0 roste bez meze. **Typ II signatura:** integrabilní hustota, konečný UV-věrný počet módů, ostrá hrana.

| veličina | full (netruncovaná) | trunc (truncovaná) |
|---|---|---|
| počet modulárních módů | 47 → 217 (**∼N¹, husté**) | 8 → 20 (pomalý/log růst, **integrabilní**) |
| pile-up u ε < 0.5 (exponent) | **∼N^1.14** (roste, hromadí se u ε = 0) | **přesně 0** (žádný pile-up) |
| podíl módů s ε < 0.5 | ~0.09 (stabilní, plochá hustota) | 0 (kompaktní nosič nad ε ≳ 1.6) |
| UV hrana ε_max | ~5.4 → 6.4 (slabě, ∼ln N) | ~5.5 → 6.8 (slabě) |

Obrázek `proxy2_modular_density.png` je nejčistší vizuál celého výpočtu: **vlevo (netruncovaná)** modulární hustota je **plochá od ε = 0 do ε ~ 6 s hromaděním u ε = 0** — přesně Connesova flat-density III₁ signatura S(M) = ℝ₊. **Vpravo (truncovaná)** spektrum má **nulovou váhu pod ε ~ 1.6** (ostrá hrana/mezera), všechny módy stlačeny k O(1) hodnotám = **integrabilní, kompaktně-nesené spektrum typu II.**

**Verdikt proxy 2: III₁ → II ✓** (nejsilnější, nejjednoznačnější proxy).

### PROXY 3 — Centrální sekvence / faktorová proxy (faktor = triviální centrum = seed-nezávislost)

Faktor typu II₁/III₁ má triviální centrum: bulk veličiny jsou nezávislé na okrajové mikrostruktuře. Proxy: relativní seed-to-seed rozptyl CV = std/mean truncované SSEE má klesat s N (self-averaging).

| N | 400 | 600 | 800 | 1000 | 1200 | 1500 | 1800 |
|---|---|---|---|---|---|---|---|
| CV(S_trunc) | 0.079 | 0.059 | 0.049 | 0.045 | 0.031 | 0.028 | 0.030 |
| CV(S_full) | 0.078 | 0.067 | 0.043 | 0.033 | 0.040 | 0.034 | 0.025 |

- **Self-averaging POTVRZENO:** CV(S_trunc) klesá na ~3 % při N = 1800 (faktorové, malé fluktuace).
- **ALE rozlišovací trend NENÍ signifikantní:** mocninový exponent CV(S_trunc) ∼ N^(−0.71 ± 0.78) je konzistentní s nulou; CV(S_full) klesá podobně (−0.50 ± 0.78). Truncovaná entropie NENÍ při 8 seedech statisticky více self-averaging než netruncovaná.

**Verdikt proxy 3: faktor-like self-averaging POTVRZENO, ale jako ROZLIŠOVACÍ signatura III→II NEROZHODNUTO** (proxy nediskriminuje trunc vs. full při tomto počtu seedů). Honest verdikt: ✗ (nepotvrzeno jako *rozlišovací* signál).

---

## VERDIKT

| Proxy | Predikce III → II | Výsledek |
|---|---|---|
| **1 — divergence stopy** | full diverguje, trunc saturuje | **✓ ANO** (entropická stopa: 80× kolaps, a: 1.04 → 0.17) |
| **2 — modulární spektrum** | full plochá hustá (III₁), trunc integrabilní (II) | **✓ ANO** (pile-up ∼N^1.14 → 0; husté ∼N → integrabilní) |
| **3 — centrální sekvence** | trunc více self-averaging | **✗ NEROZHODNUTO** (self-averaging ano, ale nediskriminuje) |

> ### **CELKOVÝ VERDIKT: SMÍŠENÝ — 2/3 proxy konzistentní s III₁ → II.**

**Dvě nezávislé, fyzikálně rozhodující proxy (entropická stopa + modulární spektrum) jednoznačně podpírají identifikaci truncace s přechodem III₁ → II.** Třetí proxy potvrzuje faktorové self-averaging truncované algebry, ale při 8 seedech ji nelze použít jako *rozlišovací* test (full i trunc se chovají self-averaging podobně — což samo o sobě není proti hypotéze, jen je to slabě informativní proxy).

**Nejdůležitější dílčí výsledky:**

1. **Modulární spektrum dává nejpřímější algebraický důkaz.** Netruncovaný SJ stav na subdiamantu má **plochou, hustou, neintegrabilní modulární hustotu hromadící se u ε = 0** — to JE definiční Connesova vlastnost typu III₁ (S(M) = ℝ₊). Truncace ji převádí na **kompaktně-nesené integrabilní spektrum** s ostrou IR hranou — definiční vlastnost typu II. **První numerická realizace Connesova modulárního invariantu na kauzální množině.**

2. **Typová signatura je ve STAVU, ne v kinematice.** Pauli-Jordanova nukleární norma (symplektická forma) roste ∼N nezávisle na truncaci; jen **entropie** (von-Neumannův stopový funkcionál na stavu) rozlišuje III od II. To je teoreticky správné a metodicky důležité — naivní „stopa operátoru iΔ" by hypotézu falešně zamítla.

3. **κ = √N/(4π) funguje jako modulární cutoff.** Magnitudový cutoff přesně odřízne objemové (ε → 0, μ → ∞) módy a ponechá UV-věrné (ε = O(1)) — to je operačně přesně to, co crossed-product regularizace dělá s divergentní entropií typu III.

---

## Limity a další kroky

- **Proxy 3 potřebuje víc seedů** (~30–50) pro rozlišení trendu CV; při 8 seedech je rozptyl příliš velký. Levný follow-up.
- **Pouze 2D, bezhmotný skalár.** Ve 4D je SSEE objemová i po truncaci (VYPOCET-06/09) — modulární-spektrum proxy by tam nejspíš NEukázalo čistou II hranu. Test ve 4D je přirozené pokračování, ale H04 už ukazuje, že 4D je objektově/dimenzně komplikované. Identifikace III→II je tedy zatím **2D výrok** (konzistentní s tím, že 2D SJ stav je blíže Hadamardovu, H04 §2c).
- **Connesův λ-invariant (III_λ vs III₁)** nelze z konečného N rozlišit jemně; měřím jen „plochá hustá vs. integrabilní", což odpovídá „III-like vs. II-like", ne přesné určení λ = 1. UV hrana ε_max ~ 6 roste jen logaritmicky, konzistentní s ℝ₊-limitou, ale plný důkaz S(M) = [0,∞) je mimo konečné N.
- **Nefudgováno:** proxy 1 odhalila, že kinematická PJ stopa hypotézu nepodpírá (roste ∼N pro full i trunc); to je zachováno jako poctivá kontrola, ne zameteno. Proxy 3 je honestně označena jako nerozhodnutá.

---

## Dopad na hypotézu H3g-3

| Před | Po VYPOCET-12 |
|---|---|
| H3g-3 „medium confidence": most strukturně doložen pilířem 19, kvantitativní identifikace zbývá | **2D numerický pilíř DODÁN pro 2 ze 3 proxy.** Modulární spektrum SJ stavu je III₁-like (plochá hustá hustota), truncace ho převádí na II-like (integrabilní). Entropická stopa: 80× kolaps III→II. |

H3g-3 se posouvá z „strukturně doloženo, číselně nezpracováno" na **„2D numericky podpořeno (entropická stopa + modulární spektrum), 4D otevřené, proxy centrálních sekvencí nerozhodnuta"**. Trojcestná identifikace (SSEE truncace = crossed-product cutoff = LQG area gap) získává svůj **první přímý algebraický numerický doklad** na causal setu — byť zatím jen ve 2D. Negativní část (PJ-stopa nerozlišuje, proxy 3 nerozhodnuta) je stejně cenná: ukazuje, že signatura žije v entropii/modulárním spektru, ne v každém operátorovém invariantu.

---

## Reference (klíčové pro tento výpočet)

- **1611.10281** — Sorkin, Yazdi: SSEE, dvojitá truncace, W_O v = μ iΔ_O v.
- **1712.04227** — causet SSEE, κ = √N/(4π) magnitudový cutoff.
- **2008.07697** — Surya, Nomaan X, Yazdi: SSEE truncace, knee.
- **0905.2562** — Casini, Huerta: review, bosonová korelátorová metoda, ε = ln[(ν+½)/(ν−½)].
- **2501.09669** — modulární Hamiltonián z dvoubodových funkcí (potvrzení formule).
- **2602.16782** — Jones, Yazdi: „Spectral Spacetime Entropy for Quasifree Theories" (SSEE ↔ kovarianční modulární formalismus).
- **2206.10780** — Chandrasekaran-Longo-Penington-Witten: crossed-product, III₁ → II, S_gen.
- **2112.12828** — Witten: gravity and the crossed product.
- Connes 1973 — klasifikace III_λ, modulární invariant S(M) = ∩ Sp(Δ_φ); III₁ ⟺ S(M) = [0,∞).
- pilíř 19 (`foundations/19-von-neumann-algebras.md`) — otevřený problém #6 (zdůvodnění SSEE truncace ↔ typ II).
