# Brainstorming 01: Kandidáti na nenalezené souvislosti (2026-06-05)

## Metodologie

Pět analytických čoček (lenses) bylo aplikováno nad lokálním korpusem `core-data/`
(`connections.json`, `formulas.json`, `open-problems.json`, `concept-graph.json`,
fragmenty pillarů a `_digest.md`). **Bez přístupu na web** a bez kontroly proti
publikované literatuře.

Pět čoček:
1. **SHARED MATH** — stejná matematická struktura (rovnice / spektrální rozvoj /
   statistické rozdělení / fixed-point vzorec) opakující se ve 2+ pilířích, aniž by
   pro ni existovala hrana v `connections.json` (nebo jen hrana hodnocená „barely").
2. **WHITE SPACES** — těžba 112 „barely" hran proti 143 otevřeným problémům.
3. **CONVERGENCES** — zdánlivé konvergence, kde hlubší společný princip dovoluje
   buď sjednocení, nebo přesnou klasifikaci rozdílů.
4. **CONFLICTS AS SIGNAL** — zostření skutečných cross-approach rozporů do
   rozhodujícího (decisive) výpočtu/pozorování.
5. **METHOD TRANSFER** — přenos zralé techniky z jednoho pilíře na zaseknutý
   otevřený problém v jiném.

> **DŮLEŽITÉ — status:** Tyto hypotézy **NEJSOU ověřené proti literatuře.**
> Tvrzení typu „v `connections.json` se slovo *Cardy* nevyskytuje" je ověřitelné
> v našich datech (a já je ověřil — viz níže), ale **neimplikuje**, že daná
> souvislost není v literatuře známá. Novelty-check proti arXiv je samostatný
> krok (Fáze 2). Confidence skóre vyjadřuje *vnitřní* sílu opory v `core-data` +
> odhad proveditelnosti prvního testu, **nikoli** pravděpodobnost, že jde
> o skutečně neobjevený výsledek.

Ověřeno přímo v datech během syntézy (sanity-check grounding):
- `cardy` v `connections.json`: **0 výskytů** (potvrzeno `grep -c`), přitom
  `cardy-formula` a `cardy-btz` ve `formulas.json` existují.
- Vnitřní rozpor o směru běhu spektrální dimenze v causal sets: `connections.json`
  ř. 657 („**drops** at short scales, sometimes to ~2") vs. ř. 1777
  („**increases** in causal sets at short scales"). Reálná, rozhodnutelná
  nekonzistence v našich vlastních datech.
- Všechna citovaná formula-ID i open-problem-ID v níže uvedených hypotézách byla
  ověřena, že ve `formulas.json` / `open-problems.json` skutečně existují.

---

## Top hypotézy

Pořadí = (potenciál objevu × síla opory v datech × proveditelnost prvního testu).
**Deduplikace:** několik hypotéz se objevilo nezávisle ve více čočkách — to je
samo o sobě signál (sbíhavost čoček) a zvyšuje prioritu. Sloučené klastry to
explicitně uvádějí.

### #1 — Spektrální dimenze d_s NENÍ univerzálně 2: je to klasifikační otisk propagátoru
**Čočka:** CONVERGENCES (+ nezávisle WHITE SPACES „spin-foam/CST fixed point"
a METHOD TRANSFER „Wetterich na BD operátor" — **3 čočky, sloučeno**).
**Confidence: high.**

- **Co tvrdí:** Údajná univerzální konvergence „d_s → 2 v UV" (AS, CDT, LQG, NCG,
  causal sets) ve skutečnosti zaznamenává *různá* čísla: AS přesně 2
  (z η_N = −2, propagátor 1/p⁴), CDT efektivně 4 → 3/2, κ-Minkowski/NCG ~ 2–3,
  causal sets sporně (data si protiřečí — viz výše). Všechna čísla mají plynout
  z jediného master-vzorce: malo-časový rozvoj heat-kernel návratové
  pravděpodobnosti P(s) ~ s^(−d_s/2), určený UV škálováním inverzního propagátoru
  G(p)⁻¹ ~ p^(2z). Tj. zdánlivá konvergence je ve skutečnosti **přesná
  klasifikace** podle exponentu z.
- **Opora v datech:** `connections.json` ř. 137 (η_N=−2 → d_s=2), 157 (1/p⁴),
  7 & 417 (CDT 4→1.80), 467 (NCG 2–3), 657 vs. 1777 (sporný směr v CST);
  formula `spectral-dimension-flow`, `graviton-anomalous-dim`; hub-uzel
  `spectral-dimension` (degree 28); open-problems `dimension-selection`,
  `planck-signature-access`.
- **Proč to nejspíš nikdo neudělal:** každá hrana se spektrální dimenzí je
  hodnocena „partially"/„barely" a popsána *párově*; nikde není heat-kernel-
  z-propagátoru vzorec použit k *odvození* různých čísel ze společného výrazu.
  Narativ zdůrazňuje sdílené d_s≈2 a mezeru 3/2 vs. 2 bere jako „nevyřešený
  rozpor", ne jako *predikci* z exponentu propagátoru.
- **První test:** napsat pro každý přístup UV inverzní propagátor (AS p⁴ → z=2;
  CDT Hořava-typ z=3; κ-Minkowski deformovaný Casimir; CST nelokální □) a spočítat
  d_s = lim_{s→0} −2 d ln P(s)/d ln s z P(s)=Tr e^(−s G⁻¹). Ověřit, zda jediný
  uzavřený vzorec d_s(z,D) reprodukuje 2 (AS) a zda Hořava z=3 dává CDT 3/2.
- **Proč #1:** nejvyšší confidence napříč panelem, hub-uzel s největším počtem
  hran, a hypotéza obsahuje **rozhodnutelný rozpor přímo v našich datech**
  (657 vs. 1777) — první test ho zároveň vyřeší.

### #2 — Seeley-DeWitt koeficient a_4 jako společný rodič: NCG spektrální akce = Sakharov = (a,c) anomálie stopy
**Čočka:** SHARED MATH (+ nezávisle WHITE SPACES „spektrální akce dokončuje
Sakharova" a METHOD TRANSFER „spektrální akce → swampland finiteness" —
**3 čočky, sloučeno**). **Confidence: medium.**

- **Co tvrdí:** Tentýž heat-kernel koeficient a_4 (= C² Weyl² + Gauss-Bonnet E_4)
  současně řídí (i) Λ⁰ člen NCG spektrální akce (`heat-kernel-action` → `gravity-terms`),
  (ii) C² členy generované integrací matter v Sakharovově indukované gravitaci
  (`sakharov-induced-action`) a (iii) koeficienty konformní anomálie stopy a, c
  (`trace-anomaly-4d`). Není to analogie, ale *týž koeficient* na D² vs. matter-
  Laplacián. Predikce: Connesova konečná algebra C+H+M₃(C) musí reprodukovat
  naměřené centrální náboje a, c Standardního modelu → falzifikovatelný
  anomaly-matching test „skoro-unikátní algebry". **Rozšíření (Lens 5):** týž a_4 /
  species-scale Λ_sp = M_Pl/√N váže NCG finiteness na swampland finiteness.
- **Opora v datech:** `heat-kernel-action`, `gravity-terms`, `spectral-action-formula`
  (NCG); `sakharov-induced-action` (emergent-gravity); `trace-anomaly-4d`,
  `noise-kernel-formula` (semiclassical); `species-scale-formula` (swampland);
  open-problems `induced-G-sign-and-cc`, `uniqueness-finite-algebra`,
  `first-principles-derivation`. Hrany emergent↔NCG, semiclassical↔NCG, NCG↔swampland
  všechny „barely".
- **Proč to nejspíš nikdo neudělal:** tři komunity používají různou notaci
  (Seeley-DeWitt a_k vs. Connesovy Wodzicki-residue momenty vs. anomálie a,c).
  Jediná hrana NCG↔emergent („barely") mluví o minimální délce, ne o sdíleném a_4.
- **První test:** spočítat a, c z NCG algebry C+H+M₃(C) standardním vážením
  a = (1/360)(N_s + 11 N_f + 62 N_v)/… a porovnat s C² koeficientem, který
  spektrální akce přiřazuje témuž spektru. Neshoda → identita zlomena v jedné
  smyčce; shoda → nové anomaly-matching omezení na přípustné NCG algebry.
- **Pozn. k honest-rankingu:** medium, ne high — anomaly-matching váhy a normalizace
  spektrální akce jsou notoricky závislé na konvenci; „shoda" může být artefakt
  normalizace. Test je ale plně uzavřený (heat-kernel počet), proto vysoká priorita.

### #3 — Λ ~ ±1/√V jako jedna fluktuačně-počítací statistika (causal sets = EDT/CDT běžící Λ = CosMIn)
**Čočka:** SHARED MATH (+ nezávisle CONVERGENCES „Λ konjugovaná k 4-objemu"
a WHITE SPACES „CST everpresent-Λ = swampland dynamical DE" — **3 čočky, sloučeno**).
**Confidence: medium.**

- **Co tvrdí:** Causal sets Λ ~ ±1/√V (`sorkin-lambda-fluctuation`), CDT/EDT
  kvadraticky běžící Λ ~ Λ₀ + c H² (`dark-energy-running-lambda`) a emergent
  CosMIn N=4π (`cosmin-lambda`) jsou *táž* statistika: Λ je dána √N Poissonovými
  fluktuacemi počtu fundamentálních buněk v Hubbleově 4-objemu, protože
  V_Hubble ~ H⁻⁴ dělá 1/√V ~ H² (= EDT běh) a N_horizon ~ (H L_P)⁻² redukuje
  CosMIn 4π/N na totéž škálování. Hlubší princip (Lens 3): Λ je termodynamicky
  konjugovaná 4-objemu (unimodulární gravitace), takže její fluktuace je dána
  number-statistikou dΛ ~ 1/√N. Navíc (Lens 2): tento drift Λ(V(t)) je *dynamická*
  temná energie → test proti swampland de Sitter bound a DESI DR2.
- **Opora v datech:** `lambda-prediction`, `sorkin-lambda-fluctuation`,
  `poisson-sprinkling`, `number-volume` (causal-sets); `dark-energy-running-lambda`
  (CDT); `cosmin-lambda`, `padmanabhan-emergence-cosmic-space` (emergent);
  swampland `refined-de-sitter`, `tcc-bound`, `sdual-quintessence-desi-2025`;
  open-problems `cosmological-constant`, `dark-energy-from-qg`. Hrany
  causal-sets↔swampland, CDT↔swampland, emergent↔swampland všechny „barely";
  digest explicitně „No direct comparison of the two dark-energy mechanisms exists."
- **Proč to nejspíš nikdo neudělal:** tři pilíře jsou drženy odděleně; každá Λ
  predikce je pod svým pilířem bez cross-hrany. Unimodulární Λ-V konjugace je
  v *jiné* hraně (supergravity/unimodular) a nebyla použita jako most.
- **První test:** dosadit V = c_H/H⁴ do Sorkinova 1/√V a ověřit, zda indukované
  Λ(H) ~ H² reprodukuje EDT koeficient c do O(1); nezávisle invertovat CosMIn
  N=4π/(H L_P)² a ověřit týž prefaktor na 10⁻¹²². Shoda *prefaktorů* (ne jen řádu)
  = jedna statistika; neshoda falzifikuje sjednocení.
- **Pozn.:** medium. Tři čočky souhlasí na *struktuře* (number-fluctuation), ale
  shoda na 10⁻¹²⁰ je notoricky náchylná k cherry-pickingu prefaktorů — test
  vyžaduje prefaktor, ne řád, jinak je výsledek bezcenný.

### #4 — Crossed-product type-II entropie = LQG area gap = causal-set SSEE truncation (jedna regularizace stopy)
**Čočka:** WHITE SPACES (+ nezávisle CONVERGENCES „LQG horizon entropy = type-II vN"
a CONFLICTS „SSEE volume vs. area = mirage test" — **3 čočky, sloučeno**).
**Confidence: medium.**

- **Co tvrdí:** Dvě (resp. tři) nezávisle motivované operace činící divergentní
  gravitační entropii konečnou a area-law jsou *táž* operace: (1) Sorkin-Yazdi SSEE
  na causal setu má **volume-law** a kolabuje na A/4 jen po *ad hoc* UV truncaci
  spektra Pauli-Jordan operátoru; (2) algebraický crossed-product A⋊ℝ převádí
  type-III₁ algebru na type-II s konečnou vN entropií S_gen=⟨A⟩/4G+S_out;
  (3) LQG počítá A/4 z diskrétního area-spektra. Hypotéza: diskrétní škála
  (area gap Δ = 4√3 π γ l_P²) **JE** modulární/observer cutoff crossed-productu,
  a Barbero-Immirzi γ je renormalizační konstanta vázající LQG stopu na type-II
  stopu. Navíc (Lens 4): area-law je „intermediate-entanglement" okno (mirage
  teorém) — truncace selektuje geometrické stavy z generických.
- **Opora v datech:** `ssee`, `pauli-jordan` (causal-sets); `crossed-product-entropy`,
  `jlms-eq` (entanglement); `bh-entropy`, `area-spectrum` (LQG); open-problems
  `area-vs-volume-entropy`, `immirzi-parameter-status`, `entropy-interpretation-observer`.
  Hub `bekenstein-hawking-entropy` (degree 37). Hrany BH-info↔LQG, entanglement↔NCG,
  causal-sets↔holography všechny „barely"; digest „Big opportunity: compare LQG
  horizon entropy with generalized / von Neumann-algebra entropy."
- **Proč to nejspíš nikdo neudělal:** causal-set a von-Neumann-algebra komunity
  sdílejí slova „modular" a „Pauli-Jordan/KMS", ale nikdy neztotožnily truncaci
  s crossed-productem. SSEE↔RT je v digestu označeno „candidate gold connection".
- **První test:** na sprinklovaném diamantu spočítat SSEE eigenvalues μ_i z (W, iΔ);
  zvlášť modelovat type-III→II crossed product modulárním Hamiltoniánem s observer-
  clock rozlišením ε. Ověřit, zda truncační rank dávající S=A/4 odpovídá
  modulárnímu cutoffu ε danému sprinkling hustotou ρ (N_truncated ~ A·ρ ?).
- **Pozn.:** medium. Atraktivní, ale tři verze se liší v tom, *co* hraje roli
  cutoffu (γ vs. Δ vs. ε), a Immirzi-normalizace je v LQG sama nejednoznačná
  (−1/2 vs. −3/2 log) — viz konflikt #7 níže, který je s touto hypotézou v napětí.

### #5 — Cardyho S = 2π√(cL₀/6) realizovaná v LQG/spin-foam černých dírách přes horizon SU(2) Chern-Simons CFT
**Čočka:** SHARED MATH. **Confidence: medium.**

- **Co tvrdí:** Cardyho formule je „matematické jádro všech mikroskopických výpočtů
  BH entropie" (BTZ, Strominger-Vafa c=6 Q1 Q5). LQG počítá horizont z area-spektra
  a ladí γ na A/4. Ale LQG isolated-horizon boundary teorie JE SU(2)/U(1)
  Chern-Simons s levelem k ~ A/(4π γ l_P²) → efektivní centrální náboj. Hypotéza:
  LQG BH entropie je skrytě Cardyho počet s c daným CS levelem; γ je LQG analogie
  string c=6 Q1 Q5. Predikce: LQG log-korekce −1/2 ln A se rovná univerzálnímu
  Cardy/CS log členu −3/2 ln c jen pro specifické γ → CFT-výběr Immirziho parametru.
- **Opora v datech:** `cardy-formula`, `cardy-btz`, `brown-henneaux`,
  `strominger-vafa-entropy`, `bh-entropy`, `area-spectrum`; open-problem
  `immirzi-parameter-status`. **`cardy` v `connections.json`: 0 výskytů (ověřeno).**
- **Proč to nejspíš nikdo neudělal:** Cardy/centrální náboj je v grafu hran
  *zcela* nepřítomen; všechny tři LQG entropy hrany řeší γ-fixing nebo tensor
  networks, nikdy horizon-CFT centrální náboj.
- **První test:** vzít k = A/(4π γ l_P²), spočítat WZW/Cardy efektivní c a vedoucí
  degeneraci přes S=2π√(cL₀/6); ověřit, zda reprodukuje γ₀ ~ 0.274 (SU(2)) a
  −1/2 log korekci. Match pinuje γ z CFT dat.
- **Pozn.:** medium. „Cardy=0 v connections" je silný *interní* signál, ale Cardy-
  forma LQG entropie je v literatuře pravděpodobně známá (ENP, Agulló et al.) —
  **nejvyšší riziko, že novelty-check ji vyřadí.** Proto #5, ne výš.

---

## Kompletní tabulka všech hypotéz

| # | Název (zkráceně) | Čočka | Conf. | První test |
|---|---|---|---|---|
| L1-1 | a_4 = NCG spektrální akce = Sakharov = (a,c) anomálie | SHARED MATH | medium | Spočítat a,c z C+H+M₃(C) a porovnat s C² koef. spektrální akce |
| L1-2 | 3× Λ~1/√V (Sorkin / EDT H² / CosMIn 4π) = táž statistika | SHARED MATH | medium | Dosadit V=c_H/H⁴; ověřit prefaktor EDT c a CosMIn na 10⁻¹²² |
| L1-3 | Cardy S=2π√(cL₀/6) v LQG přes horizon SU(2) CS CFT | SHARED MATH | medium | k=A/(4πγl_P²) → Cardy c, ověřit γ₀~0.274 a −1/2 log |
| L1-4 | Stochastic noise kernel = Verlinde-Zurek geontropy = swerves | SHARED MATH | low | ⟨ΔK²⟩ z QFTCS kernelu na boost generátoru → ⟨ΔL²⟩~l_Pl L |
| L1-5 | Melonic/Gurau = matrix genus = NCG Dirac ensembles (free, ne safe) | SHARED MATH | medium | Leading 1/N free energy fuzzy geometrie + znaménko β |
| L2-1 | Liouville/Painlevé I univerzální třída: NCG=GFT=CDT (double scaling) | WHITE SPACES | medium | γ_str / c v double-scaling pro Dirac ensemble, 2-matrix, 2D CDT |
| L2-2 | CST everpresent-Λ = swampland dynamical DE (1/√V drift vs. dS bound) | WHITE SPACES | medium | Λ(t)=ξ/√V(t), odvodit w(z) a |∇V|/V, test dS bound + DESI |
| L2-3 | CST SSEE = crossed-product type-II (Pauli-Jordan truncace = observer/clock) | WHITE SPACES | medium | SSEE μ_i na diamantu vs. modulární cutoff ε ~ ρ |
| L2-4 | NCG spektrální akce = kovariantní completion Sakharova (sign/Λ) | WHITE SPACES | low | G~1/(f₂Λ²) = ΣcᵢΛ²; znaménko f₂a₂ pro C+H+M₃(C) |
| L2-5 | Spin-foam coarse-graining = CST BD = jeden Reuter fixed point (d_s sign) | WHITE SPACES | medium | d_s z BD □ na velkých sprinklingách: klesá k 2, nebo roste? |
| L2-6 | Twistor self-duality = LQG self-dual Ashtekar (spin sítě = twistor kohomologie) | WHITE SPACES | low | Self-dual (γ=i) Wilson loop vs. twistor kontur. integrál |
| L3-1 | d_s NENÍ univ. 2 — klasifikační otisk propagátoru G(p)⁻¹~p^(2z) | CONVERGENCES | **high** | d_s=lim −2 dlnP/dlns z P(s)=Tr e^(−sG⁻¹) pro každý přístup |
| L3-2 | Λ konjugovaná k 4-objemu: dΛ~1/√N sjednocuje CST/EDT/emergent | CONVERGENCES | medium | Poisson N=ρ_Pl V → dΛ; reprodukuje Sorkin i EDT běh? |
| L3-3 | Bounce při stejném ρ_c (LQC/GFT/AS) = jeden max-curvature bound | CONVERGENCES | medium | H²=(8πG/3)ρ(1−ρ/ρ_c); vyjádřit ρ_c/ρ_Pl přes min. plochu |
| L3-4 | LQG horizon entropy = crossed-product type-II (area gap = modul. cutoff) | CONVERGENCES | medium | Typ algebry punktur vs. crossed product; γ shoda na A/4 |
| L3-5 | Minimální délka (AS/NCG/T-dualita) = zakřivení momentového prostoru, jeden β₀ | CONVERGENCES | low | Born-reciproc. metrika l_min → p⁻⁴, [x,x], R↔1/R; extrahovat β₀ |
| L3-6 | „Area z volume" (CST/AS/NCG) = jeden UV-truncation princip | CONVERGENCES | low | Truncace f modů → S=A/4; stejný cutoff per Planck area? |
| L4-1 | 2D Hausdorff d_H (2 vs 4) odděluje CDT od string worldsheet (Liouville) | CONFLICTS | **high** | Přidat topology-change g do 2D-CDT transfer matice; d_H(g) interpoluje 2→4? |
| L4-2 | No-global-symmetries je absolutní swampland kritérium, AS ho porušuje | CONFLICTS | **high** | FRG flow global-charge operátoru: koef. = 0 ve fixed pointu? |
| L4-3 | Log-korekce koef. (−1/2 vs −3/2 ln A) odděluje LQG od emergent univerzality | CONFLICTS | **high** | LQG log v U(1) i SU(2); produkuje Jacobson nějaký ln A? |
| L4-4 | CST SSEE volume-vs-area = mirage teorém (UV truncace = výběr geom. stavů) | CONFLICTS | medium | SSEE vs. holographic entropy cone (monogamie MI) ve scaling okně |
| L4-5 | BMV/QGEM diskriminuje PŘÍSTUPY (emergent vs. graviton-based), ne jen Q vs C | CONFLICTS | medium | Entangling rate: AS graviton spektr. fce vs. Verlinde mediator |
| L4-6 | d_s→2 oslabuje gravitaci → napětí s WGC „gravity weakest" (δ(Q/M)) | CONFLICTS | medium | Vložit 1/p⁴ do Hamada-Noumi-Shiu; znaménko δ(Q/M) |
| L5-1 | Gurau 1/N + melonic-Schwarzian → Page curve bez bulk gravitace | METHOD TRANSFER | medium | Klebanov-Tarnopolsky O(N)³, Rényi přes ω=1, turnover v Page time? |
| L5-2 | CHY scattering equations → causal-set konečný Lorentz-inv. S-matrix | METHOD TRANSFER | low | 1+1 diamant: iΔ SJ báze → diskrétní scattering eq., počet řešení |
| L5-3 | SJ Pauli-Jordan stav → chybějící Hadamard stav pro Kerr / SdS | METHOD TRANSFER | medium | 1+1 dS: SJ 2-bod. fce vs. Bunch-Davies, wavefront set odchylka |
| L5-4 | Connes spektrální akce → swampland finiteness/which-WGC (D-spektrum = tower) | METHOD TRANSFER | medium | Λ_sp=M_Pl/√N vs. spektr. akce cutoff; stejné škálování? |
| L5-5 | Wetterich FRG → CST Benincasa-Dowker □ (fixed point řeší nonlocality) | METHOD TRANSFER | low | B_ε(k) jako Γ_k^(2), β-fce nelok. bumpu, decoupling ghost modů? |

---

## Jak dál (doporučený postup Fáze 2)

### A. Pořadí prověřování (priorita = sbíhavost čoček × proveditelnost × decisiveness)

1. **d_s klastr (L3-1 + L2-5 + L5-5)** — nejdřív. Obsahuje **rozhodnutelný rozpor
   přímo v našich datech** (connections 657 vs. 1777). První krok je *čistě
   datový*: rozhodnout správné znaménko běhu CST spektrální dimenze; pak
   master-vzorec d_s(z,D). High confidence, hub-uzel.
2. **Čtyři „high" konflikty (L4-1, L4-2, L4-3)** — každý je formulován jako jeden
   binární diskriminátor s uzavřeným prvním testem (d_H order-parametr;
   FRG global-charge koef.; log-korekce koef.). Decisive a levné.
3. **a_4 klastr (L1-1 + L2-4 + L5-4)** — heat-kernel počet, plně uzavřený;
   sbíhavost tří čoček na témž koeficientu. Vysoká hodnota, střední riziko
   normalizačního artefaktu.
4. **Λ ~ 1/√V klastr (L1-2 + L3-2 + L2-2)** — algebra + kosmologie, bez simulace;
   sbíhavost tří čoček. Pozor na prefaktor vs. řád.
5. **Entropie/crossed-product klastr (L2-3 + L3-4 + L4-4)** — vyžaduje sprinkling
   výpočet SSEE; nejnáročnější, ale tři čočky a hub degree 37.
6. **Zbytek** podle confidence; nejníže low-confidence single-lens (L1-4, L3-5,
   L5-2, L2-6).

### B. Co ověřit proti literatuře (novelty-check, arXiv/web — Fáze 2)

Priority pro novelty-check (riziko, že už existuje, je nepřímo úměrné „objevnosti"):
- **L1-3 (Cardy v LQG)** — NEJVYŠŠÍ riziko, že je známé (Engle-Noui-Perez horizon
  CS, Agulló et al. log-korekce). „Cardy=0 v *našich* connections" ≠ neexistuje
  v literatuře. Ověřit dřív, než se investuje do výpočtu.
- **L2-1 (Liouville univerzální třída)** — grounding sám cituje
  Hessam-Khalkhali-Pagliaroli 2022 (Dirac→Liouville) a Khalkhali-Pagliaroli 2023;
  **dvojstranná NCG↔GFT část je tedy částečně publikovaná** — novum je pouze
  *trojstranné* tvrzení (+ CDT). Ověřit, co přesně už existuje.
- **L4-2 (no-global-symmetries vs. AS)** — grounding cituje Basile-Knorr-Platania-
  Schiffer 2025 (2502.12290); ověřit, zda už dělají přesně tento závěr.
- **L4-5 / L4-6 (BMV diskriminátor; d_s vs. WGC)** — citují Pawlowski-Reichert-
  Wessely 2025 a Hamada-Noumi-Shiu; ověřit existující δ(Q/M) v AS.
- **L5-3 (SJ stav pro Kerr/SdS)** — ověřit Kay-Wald no-go a existující SJ-vs-
  Hadamard srovnání (Fewster-Verch); novum je aplikace na rotující/multi-horizon.
- Pro **L1-1, L1-2, L3-1** je novelty-check sekundární — i kdyby byly části známé,
  *trojstranné* sjednocení / master-vzorec je pravděpodobně nové.

### C. Které výpočty lze zkusit rovnou (bez nové fyziky, uzavřené)

- **L3-1**: P(s)=Tr e^(−sG⁻¹) pro 4 zadané propagátory → d_s(z,D). Symbolicky/
  numericky, minuty.
- **L4-1**: 2D-CDT transfer matice Ĥ=−L∂²_L+λL + topology-change g; d_H(g) z V(r)~r^d_H.
- **L4-3**: LQG log-koef. v U(1) i SU(2) pro tentýž isolated horizon; Jacobson
  first-variation geodetické koule → ln A člen?
- **L1-1 / L5-4**: heat-kernel a_4 a a_2 pro C+H+M₃(C); a,c vs. C² koef.; Λ_sp vs. cutoff.
- **L1-2 / L3-2**: V=c_H/H⁴ do 1/√V; N=ρ_Pl V → dΛ; porovnat EDT c a CosMIn prefaktor.
- **L1-5**: leading 1/N free energy publikovaného fuzzy-geometry multimatrix integrálu
  + jednosmyčková β-fce kvartiku (znaménko).

Tyto „rovnou" výpočty jsou ideální vstup pro Fázi 2 i bez webu — slouží jako
rychlý filtr: hypotéza, jejíž uzavřený test selže, odpadá bez nutnosti novelty-checku.

---

## Honest ranking — kde je to slabé / kde se čočky neshodují

- **Napětí mezi hypotézami:** klastr **#4 (crossed-product = area gap)** předpokládá
  *jednoznačnou* Immirzi-normalizaci γ, ale konflikt **L4-3** ukazuje, že LQG log-
  korekce je sama schématicky nejednoznačná (−1/2 vs. −3/2). Pokud je γ
  schéma-závislá, identifikace area-gap ↔ modulární cutoff ztrácí jednoznačnost.
  **Tyto dvě hypotézy je nutné testovat společně** — výsledek L4-3 přímo
  rozhoduje o platnosti #4 a #5.
- **Vnitřní rozpor v datech:** směr běhu CST d_s (657 vs. 1777) — nutno vyřešit
  *před* jakoukoli „d_s konvergence" hypotézou; jinak L2-5 i L3-1 stojí na písku.
- **Slabé single-lens low-confidence:** L1-4 (noise kernel = geontropy = swerves),
  L3-5 (jeden β₀), L5-2 (CHY na causal sets) — atraktivní analogie, ale grounding
  je tenký a první testy nejsou plně uzavřené. Nízká priorita.
- **Riziko „přeprodaného" sjednocení:** L1-2/L3-2 (Λ~1/√V) — shoda na 10⁻¹²⁰ je
  notoricky náchylná k cherry-pickingu prefaktorů. Hypotéza má cenu **jen** pokud
  test trvá na shodě *prefaktoru*, ne řádu velikosti.

---

## Shrnutí — top 5 hypotéz (jedna věta každá)

1. **Spektrální dimenze d_s není univerzálně 2** — její hodnota (2 vs. 3/2 vs. rostoucí) je predikovatelný otisk UV exponentu propagátoru z, a údajná konvergence je ve skutečnosti přesná klasifikace; navíc obsahuje rozhodnutelný rozpor přímo v našich datech (CONVERGENCES, high).
2. **Seeley-DeWitt koeficient a_4 je společný rodič NCG spektrální akce, Sakharovovy indukované gravitace a (a,c) anomálie stopy** — týž koeficient, ne analogie, dává falzifikovatelný anomaly-matching test pro Connesovu „skoro-unikátní" algebru C+H+M₃(C) (SHARED MATH, medium).
3. **Tři predikce Λ ~ ±1/√V (Sorkin, EDT běh H², CosMIn 4π) jsou táž number-fluktuační statistika** konjugovaná k 4-objemu, takže jejich prefaktory musí být vzájemně predikovatelné, ne tři náhody na 10⁻¹²⁰ (SHARED MATH, medium).
4. **Causal-set SSEE truncace Pauli-Jordan operátoru, LQG area gap a algebraický crossed-product type-II jsou táž regularizace** divergentní stopy — diskrétní škála hraje roli observer/modulárního cutoffu a Immirzi γ je renormalizační konstanta (WHITE SPACES, medium; v napětí s konfliktem o log-korekci).
5. **Cardyho formule S=2π√(cL₀/6) je skrytě realizována v LQG černých dírách přes horizon SU(2) Chern-Simons CFT** — Immirzi γ je LQG analogie string centrálního náboje c=6 Q1 Q5; slovo „Cardy" se v `connections.json` nevyskytuje ani jednou (SHARED MATH, medium; nejvyšší riziko, že novelty-check ji vyřadí).

---

## Novelty check (2026-06-06)

Provedeno 6 sond přes arXiv literaturu + oprava datového rozporu d_s v CST.
Všechny klastry dostaly verdikt **partially-known** — žádný není zcela nový ani zcela pokrytý.

### Oprava datového rozporu d_s (CST)

Vnitřní rozpor v `connections.json` (ř. 657 vs. 1777 — „drops" vs. „increases" d_s v CST) byl vyřešen. Výsledek: **obě hrany zachycovaly část pravdy, ale generalizovaly ze špatné sondy.** Eichhorn–Mizera (arXiv:1311.2530, CQG 2014) ukázali, že náhodná procházka na diskrétním kauzálním grafu dává _rostoucí_ d_s na krátkých škálách kvůli lorentzovské nelokálnosti. Belenchia et al. (arXiv:1507.00330, PRD 2016) ukázali, že d'Alembertiánová sonda dává universální pokles k d_s ~ 2 ve všech dimenzích. Oba výsledky jsou správné a komplementární: spektrální dimenze v CST je **probe-dependent**.

Implikace pro d_s klastr: probe-dependence v CST je přímým empirickým potvrzením jádra hypotézy L3-1. Master-vzorec musí mít tvar **d_s(z, D, probe)** — sonda je třetí klasifikační parametr vedle exponentu z a dimenze D.

### Přehledová tabulka

| Klastr | Verdikt | Doporučení | Klíčová prior art |
|---|---|---|---|
| d_s klastr (L3-1 + L2-5 + L5-5) | partially-known | reframe | Hořava 0902.3657 (d_s=1+D/z); Sotiriou-Visser-Weinfurtner 1105.6098; Calcagni 1708.07445 (srovnávací tabulka bez P(s) frameworku) |
| a_4 klastr (L1-1 + L2-4 + L5-4) | partially-known | **pursue** | Andrianov-Kurkov-Lizzi 1103.0478 (NCG↔anomálie 2-cestně); Kurkov-Lizzi 1311.6979 (Sakharov↔spektrální akce); trojstranná identifikace a anomaly-matching test pro C⊕H⊕M₃(C) chybí |
| Λ klastr (L1-2 + L3-2 + L2-2) | partially-known | reframe | Sorkin astro-ph/0209274 + 0710.1675 (pilíř 1 kompletní); Padmanabhan 1302.3226 (CosMIn); Dai-Laiho 2408.08963 (EDT); mezipilířové srovnání prefaktorů chybí |
| Entropie klastr (L2-3 + L3-4 + L4-4) | partially-known | **pursue** | Sorkin-Yazdi 1611.10281 (SSEE); Chandrasekaran-Penington-Witten 2206.10780 (crossed-product); Perez 1405.7287 (LQG entropie); trojcestná syntéza SSEE-truncation = crossed-product cutoff = LQG area gap chybí |
| Cardy-LQG (L1-3) | partially-known | reframe | Carlip 1410.5763 (c=6k explicitně); Ghosh-Pranzetti 1405.7056 (WZW/horizon CFT); Engle-Noui-Perez 0905.3168 (SU(2) CS); γ↔c=6Q₁Q₅ analogie a CFT log-fixing γ~0.274 chybí |
| Preprint checks (L4-2, L4-5/L4-6, L5-3, L2-1) | partially-known | reframe | Basile et al. 2502.12290 (AS vs. swampland tension mapována); Aziz-Howl Nature 2025 + 3 rebuttal arXivy ověřeny; Hessam-Khalkhali 2204.14206 (NCG↔Liouville publikováno); SJ pro Kerr/SdS nepokryto |

### Klíčové závěry po klastru

**d_s klastr — reframe.** Formule d_s = 1 + D/z je v literatuře explicitní od roku 2009 (Hořava) a zobecněná od roku 2011 (Sotiriou et al.) — hypotéza L3-1 NEMŮŽE být prezentována jako nový objev vzorce. Zbývají tři nepokryté prvky: (1) jednotný P(s) = Tr e^{−sG^{−1}} formalizmus aplikovaný systematicky přes AS/CDT/LQG/CST, (2) probe-dependence jako explicitní třetí klasifikační parametr d_s(z, D, probe), (3) interpretace výsledku jako diskriminátoru mezi přístupy, ne důkazu konvergence. Priorita klastru zůstává vysoká, ale výchozí bod výpočtu se posouvá: místo „odvodit vzorec" jde o „sestavit klasifikační tabulku s jednotnou metodou a přidat probe jako parametr". Carlipův přehled (1705.05417) přiblížení d_s ~ 2 jako „almost universal" sám uznává výjimky — naše přidaná hodnota je systematičnost a klasifikační interpretace.

**a_4 klastr — pursue.** Dvoustranné vazby (spektrální akce ↔ Weyl anomálie, spektrální akce ↔ Sakharov) jsou pokryty pracemi Andrianova-Lizziho a Kurkova-Lizziho (2010–2013). Jádro hypotézy — explicitní trojstranná identifikace přes a_4 s porovnáním normalizací a konkrétní anomaly-matching test pro algebru C⊕H⊕M₃(C) (výpočet a,c z NCG spektra, srovnání s C² koeficientem spektrální akce) — v literatuře chybí. Výpočet je uzavřený (čistě heat-kernel), riziko je normalizační artefakt. Tento klastr povyšuje na **nové #1 priority** pro výpočetní fázi společně s entropickým klastrem.

**Λ klastr — reframe.** Základní matematika (Λ–V konjugace, Poissonovy fluktuace) je v literatuře etablována od roku 2004 a tři pilíře jsou zcela nezávisle publikovány a fenomenologicky testovány. Přidaná hodnota leží výhradně v mezipilířovém prefaktorovém testu — tento test nebyl dosud navržen ani proveden. Hypotézu je třeba reformulovat jako „falzifikovatelný prefaktorový test tří nezávislých Λ~1/√V mechanismů", nikoli jako objev principu konjugace. Priorita zůstává, ale framing se zásadně mění.

**Entropie klastr — pursue.** Všechny dvoucestné mosty existují odděleně (SSEE truncace; crossed-product type-II od 2022; LQG area gap jako cutoff nastíněn Perezem). Trojcestná syntéza — identifikace SSEE Pauli-Jordan truncačního ranku s modulárním cutoffem crossed-productu a ztotožnění s LQG area gap, s Immirzi γ jako renormalizační konstantou — v literatuře chybí. Nová práce 2601.07915 (2026) a 2510.26911 (2025) jsou sousední, ale nepřekrývají se v tomto konkrétním bodě. Největší riziko je vnitřní nejednoznačnost (γ vs. Δ vs. ε jako cutoff). Doporučený první krok: numerický SSEE test na sprinklovaném diamantu.

**Cardy-LQG — reframe.** Jádro hypotézy (c = 6k z CS levelu, Cardyho formule v LQG) je explicitně publikováno Carlipem (arXiv:1410.5763) a Ghosh–Pranzettiho (arXiv:1405.7056) — hypotéza je v aktuální formulaci z velké části „known". Zbývají dva nepokryté prvky: (1) γ ↔ c = 6Q₁Q₅ jako analogie přes LQG/string hranici, (2) CFT log-matching podmínka fixující reálné γ ~ 0.274 bez fenomenologického vstupu. Hypotézu je třeba přeformulovat tak, aby se soustředila výhradně na tyto dva body. Priorita klesá z #5 na spodní třetinu — výpočetní přínos je malý, riziko rediscovery vysoké.

**Preprint checks — reframe.** Basile et al. (2502.12290) již konflikt AS vs. no-global-symmetries mapují jako otevřenou otázku — přidaná hodnota L4-2 je konkrétní FRG výpočet. Všechny citace L4-5 ověřeny (tři arXivy + Nature 2025). Framing L4-5 (AS graviton spectral function vs. Verlinde entropic mediator, ne Q vs. C) je legitimně nový. L4-6 (1/p⁴ propagátor do Hamada-Noumi-Shiu) je nový výpočet. L5-3 (SJ stav pro Kerr/SdS) je otevřené území — přidat Fewster-Verch a Kay-Wald jako sousední literaturu. Pro L2-1 odlišit publikovanou NCG↔Liouville část od nepublikované trojstranné syntézy a ověřit universální třídu GFT modelu.
