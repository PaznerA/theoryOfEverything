# H04 — Entropy-cluster reframe: co 2D potvrdilo, 4D zkomplikovalo, a co dál

> **Status:** Aktivní — po VYPOCET-13: interpretace (c) podpořena, (a) vyvrácena v silné formě  
> **Datum:** 2026-06-06  
> **Navazuje na:** VYPOCET-04 (2D, pozitivní), VYPOCET-06 (4D, komplikace), VYPOCET-09 (BD), VYPOCET-13 (slab vs diamant), BRAINSTORM-02 §H2g-3  
> **Rodičovská hypotéza:** H2g-3 — SSEE truncační cutoff = crossed-product modulární cutoff = LQG area gap  
> **Cluster:** entropy-cluster (L2-3 + L3-4 + L4-4)

---

## 1. Co přesně 2D potvrdilo a 4D zkomplikovalo

### 1.1 VYPOCET-04: 2D pozitivní výsledek (čísla)

Na sprinklovaném 2D kauzálním diamantu (Minkowski, bezhmotný skalár, Sorkin-Johnston konstrukce přes kauzální matici C) dala dvojitá truncace Pauli-Jordanova spektra robustní výsledek:

- **Škálování entropického cutoffu:** rank ~ N^(0.519 ± 0.007), kompatibilní s p = 1/2 = (d−1)/d pro d = 2.
- **Statistická síla:** odchylka od p = 1/4 (alternativní škálování ε ~ ρ^(−1/4)) je **39 σ** — vyloučeno.
- **Spektrum:** 2D Pauli-Jordanovo spektrum je **čistý mocninový zákon** λ_k ~ 1/k; součin k·λ_k tvoří ostré plató, pak prudký zlom — koleno je jednoznačně definované a cutoff-nezávislé.
- **SSEE:** objem-law hodnota S = 95.2 se po truncaci sníží na S = 1.58 (area/log law). Přechod objem→plocha je demonstrován, ne jen odhadnut.
- **Závěr:** V 2D existuje robustní, spektrálně čitelný UV cutoff ε ~ ρ^(−1/2), konzistentní s area-law exponentem (d−1)/d. Toto je přímý kandidát na identifikaci s modulárním cutoffem crossed-productu (Chandrasekaran-Penington-Witten 2206.10780) a nepřímo s LQG area gap.

### 1.2 VYPOCET-06: 4D komplikace (čísla)

Na sprinklovaném 4D kauzálním diamantu (T=1, Vol = 2π/3 ≈ 2.094, Johnston konstrukce přes link matici L, G_R = (√ρ / 2π√6)·L, arXiv:0909.0944) byl test **predikce p = 3/4 = (d−1)/d pro d = 4** neúspěšný jako robustní spektrální fakt:

| Cutoff definice | p (naměřeno) | Odchylka od 3/4 |
|-----------------|-------------|------------------|
| rank @ 2 % λ_max | 0.964 ± 0.003 | +69.7 σ |
| rank @ 5 % λ_max | 0.903 ± 0.005 | +32.0 σ |
| rank @ 10 % λ_max | **0.751 ± 0.007** | **+0.07 σ** (náhoda) |
| intrinsická kolena (k·λ plató) | 0.651 ± 0.022 | −4.4 σ |
| **slope-knee (literatura 2008.07697)** | **0.985 ± 0.001** | **+171 σ** (≈ N¹) |

Rozsah naměřených exponentů: **0.65 – 0.98** — plná dekáda nejistoty podle volby cutoffu. P = 3/4 trefuje jediný arbitrární cutoff (10 % λ_max), bez spektrálního zdůvodnění.

**Příčina: 4D Pauli-Jordanovo spektrum (z link matice) NENÍ čistý mocninový zákon.**

- Eigenvalues λ_k jsou téměř ploché přes ~3 dekády ranku (hodnoty 40–200 pro N = 3000), pak prudce klesají — žádné oblasti plochého k·λ_k plató.
- Součin k·λ_k monotónně roste k vrcholu u ranku ≈ 900, pak klesá. Ve 2D bylo plató horizontální.
- Mean links/point roste jako ~N^0.65; link matice je hustší než kauzální matice C, a to deformuje tvar spektra.
- Slope-knee (jediná fyzikálně motivovaná spektrální feature, 2008.07697 sek. 2.4) indikuje N^0.985, nikoli N^(3/4).

**Sekundárně: 4D SSEE na nested diamantu dává VOLUME law, ne area law.**

- Fit S vs. plocha A(f) = 4π(fT)²: R² = 0.962
- Fit S vs. počet bodů n_sub (∝ 4-objem): **R² = 0.998**, S ~ f^6.1
- Podmíněný test (N = 2000, tři různé cutoff definice): ve všech případech R²_vol > R²_area, stable = True, verdikt VOLUME — robustní, nezávislý na cutoffu.
- Literaturní fixed-rank truncace n_max = α·N^(3/4) (2008.07697 eq.15) je v single-N nested-diamond geometrii **numericky patologická** (S diverguje na 10⁴–10⁵, R² ≈ 0.05).

---

## 2. Tři interpretace

### 2a. Hypotéza platí jen pro konformně triviální 2D

**Tvrzení:** Čistá spektrální signatura (mocninový zákon λ_k ~ 1/k, robustní koleno, emergentní area-law exponent) je specifická pro d = 1+1, kde:

- 2D CFT je konfomě triviální (c je jediný parametr, OPE algebra uzavřená).
- Kauzální matice C v 1+1D je sparná a dobře podmíněná; retardovaná Greenova funkce G_R je přímo C bez prefaktoru (Johnston 0909.0944 eq.4), nikoli hustá link matice.
- Spektrum G_R v 1+1D zdědí jednoduchou strukturu kauzálního polouspořádání (binární matice).

Ve vyšších dimenzích (d ≥ 3) je obraz fundamentálně odlišný: spektrum je husté, koleno nevyhraněné, area-law musí být imposováno externě (slab geometrie, fixní rank ansatz), ne vychází emergentně. Modulární cutoff crossed-productu přes Type II_∞ algebru existuje, ale jeho identifikace s SSEE spektrálním kolenem je specificky 2D výrok. Pro d = 4 trojcestná identifikace (SSEE cutoff = crossed-product cutoff = LQG area gap) ztrácí svůj numerický pilíř.

**Síla:** Konzistentní s tím, co víme o CFT v nízké dimenzi; 4D komplikace jsou pochopitelné. Jasný, konzervativní verdikt.

**Slabost:** Posouvá hypotézu ze „zákona přírody" na „nízkorozměrnou kuriozitu", čímž ztrácí relevanci pro LQG (4D). Nevysvětluje, proč literatura (2008.07697) dosahuje area law ve 4D de Sitter slabu — tam tedy exponent existuje, ale byl implantován jinak.

**Rozhodující experiment (viz §3a).**

---

### 2b. Ve 4D je špatný objekt — link-matrix G_R není správný kandidát

**Tvrzení:** Identifikace G_R = (√ρ / 2π√6)·L (Johnston 0909.0944) je správná pro výpočet Wightmanovy funkce a SJ vakua, ale link matice L je **špatný objekt pro modulární/UV identifikaci** v kontextu entropy-cluster hypotézy. Konkrétně:

1. **Link matice je kombinatorický objekt**, ne kontinuum operátor. Hustá při rostoucím N (mean links/point ~ N^0.65), deformuje spektrum směrem od mocninového zákona. Kontinuální limita G_R^(4) = retarded Green function G₀ je dosažena teprve pro ρ → ∞ v průměru, ale spektrální distribuce vlastních čísel L konverguje ke svému vlastnímu spektrálnímu limitu — ne nutně k spektru G₀.

2. **Správný kandidát pro spektrální test modulárního cutoffu** je Pauli-Jordanova funkce zkonstruovaná z **nelokálního Benincasa-Dowker d'Alembertiánu** (BD-d'Alembertián), nebo přesněji z jeho 4D inverse — jak bylo odvozeno v Belenchia, Benincasa, Liberati, Marin, Marino, Bassi, **arXiv:1507.00330** (PRD 2016):

   Belenchia et al. ukazují, že spektrální dimenze causal setu měřená d'Alembertiánovou sondou vykazuje **universální pokles k d_s ~ 2** ve všech dimenzích — na rozdíl od náhodné procházky (kde d_s roste kvůli lorentzovské nelokálnosti). Klíčové: BD-d'Alembertián operátor v 4D je explicitně nelokalní s Gaussovým vahami přes délkové škály ~ ρ^(-1/4) (4D) nebo ρ^(-1/2) (2D) — a tato škála je přirozenou UV regulací s jasnou spektrální signaturou.

3. BD-d'Alembertián je **hermitovský operátor** na prostoru skalárních polí na causal setu, konstruovaný tak, aby dal v kontinuu □ + korekce ~ l²_P □². Jeho vlastní čísla, nikoliv vlastní čísla Pauli-Jordana z link matice, pravděpodobně dají čistší mocninový zákon — protože jsou explicitně navržena tak, aby se kontinuum-limita chovala rozumně.

4. **Konkrétně:** SSEE zkonstruovaná z BD Green function G_R^BD (ne z L) by měla být testována. Pauli-Jordan operátor iΔ^BD = i(G_R^BD − (G_R^BD)^T) má jiný tvar spektra — potenciálně čistší koleno a robustnější škálování — protože BD d'Alembertián tlumí vysokofrekvenční mody jiným způsobem než link matice.

**Síla:** Přesný mechanismus, testovatelný. BD d'Alembertián je dobře vyvinutý (Benincasa-Dowker 0911.2563; Belenchia et al. 1507.00330). Zachovává jádro hypotézy pro 4D, pouze opravuje volbu objektu.

**Slabost:** Výpočet G_R z BD d'Alembertiánu je výrazně náročnější než link matice — vyžaduje implementaci nelokalních Gaussových kernel operátorů, přičemž hustota musí být dostatečná pro jejich konvergenci. Pro N = 5000 v 4D to je náročné. Navíc: není a priori zaručeno, že BD spektrum bude čistší; je to motivovaná spekulace, ne dokázaná věc.

**Rozhodující experiment (viz §3b) = navrhovaný VYPOCET-09.**

---

### 2c. Volume law je skutečný fyzikální signál — SJ stav na diamantu není Hadamardův

**Tvrzení:** Volume law není numerická patologie ani příznak chybné truncace. Je to **správná fyzika SJ stavu**. SJ vakuum na kauzálním diamantu není Hadamardovský stav, a proto jeho entanglementová entropie nemusí být (a není) area law.

**Podpůrné argumenty:**

1. **Non-Hadamardovost SJ stavu je prokázána.** Johnston, Sorkin, Yazdi a spol. ukázali v 1+1D, že SJ Wightmanova funkce W_{SJ}(x,y) diverguje pro spacelike separaci x ↔ y jinak než standardní Hadamardova forma. Zvláště: práce Saravani, Aslanbeigi, Kempf, **arXiv:2212.10592** (2022), dokazuje explicitně, že SJ stav na 1+1D kauzálním diamantu **není Hadamardův** — jeho UV struktura dvoubodicové funkce se liší od Hadamardovy singularity o nenulové příspěvky z globální geometrie diamantu.

2. **Volume law jako důsledek non-Hadamardovosti:** Hadamardova podmínka je přesně podmínka, která zaručuje konečnost a area-law charakter entanglementové entropie v QFT (viz Hollands-Ruan, Verch-Werner). Pokud stav není Hadamardový, příspěvky k SSEE z globálně korelovaných modů (vzdálené části diamantu přispívají k redukované matici hustoty na sub-diamantu) nejsou potlačeny exponenciálně — a výsledkem je volume law. Viz Surya, Nomaan X, Yazdi (2008.07697), kteří přímo říkají: „volume law lze vystopovat k nelokálnosti inherentní v kauzálním setu."

3. **2D čistota SJ spektra jako výjimka:** Ve 2D je kauzální diamant konformě plochý a SJ stav se blíží Hadamardovu stavu rychleji než ve 4D (UV struktura je slabší; 2D logaritmická divergence vs. 4D kvadratická). 2D SSEE area law po truncaci (VYPOCET-04) je pak konzistentní: truncace odstraňuje zbývající non-Hadamardovské mody a obnoví area law.

4. Ve 4D je non-Hadamardovost silnější; objem-law je přitažlivý bod, ze kterého se magnitudová truncace (analogická 2D κ) nevymaní, protože neodpovídá povaze UV divergencí ve 4D. Pouze geometricky specifická truncace (de Sitter slab, Rindler) nebo externally imposovaný rank oddělí správné mody.

5. **Viz také Surya (2008.07697) a Brahma, Chandrasekaran, Watter (2008.07697 citace sítě):** Pro causal set stavy, které nejsou Hadamardovské, je objem-law genericky očekáván — není to problém, ale signál diskrétní struktury podkladového vakua.

**Důsledek pro H2g-3:** Trojcestná identifikace (SSEE truncační cutoff = crossed-product cutoff = LQG area gap) předpokládá, že existuje **jediný UV cutoff**, který obnoví area law. Pokud volume law vzniká z non-Hadamardovosti SJ stavu na diamantu (nikoli z chybějícího cutoffu), pak správnou otázkou není „co je cutoff?" ale „v jaké geometrii SJ stav Hadamardovský je, a jak tato geometrie odpovídá modulárnímu observeru crossed-productu?" Na flat Rindler klíně je vakuový stav Hadamardovský (= Unruhův stav). Na diamantu není. Toto je klíčový fakt.

**Síla:** Přímý fyzikální mechanismus. Non-Hadamardovost SJ stavu na diamantu je prokázaná vlastnost, ne spekulace. Vysvětluje, proč literaturní area law funguje jen v slab/Rindler geometrii.

**Slabost:** Pokud volume law ve 4D je nevyhnutelný kvůli non-Hadamardovosti, pak je celý program testování p = 3/4 na nested diamantu metodologicky vadný od počátku — a 2D úspěch byl produktem speciální symetrie, ne obecného principu.

---

## 3. Rozhodující experimenty

### 3a. Test interpretace 2a (2D-only hypotéza)

**Experiment:** SSEE na sprinklovaném **3D** kauzálním diamantu s Johnstonovým G_R^(3D) (přes kauzální matici C s 3D prefaktorem, viz Nomaan X, Dowker, Surya 1701.07212). Predikce 2a: žádný robustní exponent ani v 3D (spektrum bude rovněž ploché). Predikce zbývajících interpretací: exponent p = 2/3 je (d−1)/d pro d = 3 — pokud link matice ve 3D má čistší spektrum než ve 4D (přechodný případ), dostaneme p ≈ 2/3. Výsledek jasně odliší 2D-only hypotézu od geometrie-závislé interpretace.

**Proveditelnost:** 3D verze je numericky méně náročná než 4D (~5–10× méně bodů; 4D link matmul je hlavní bottleneck). Johnston 0909.0944 / Nomaan X 1701.07212 dávají prefaktor. Odhadovaný runtime při N ≤ 3000: ~100–300 s.

### 3b. Test interpretace 2b (BD d'Alembertián)

**Experiment (= navrhovaný VYPOCET-09):** Implementovat 4D Pauli-Jordanův operátor iΔ^BD z Benincasa-Dowker (BD) d'Alembertiánu (arXiv:0911.2563; Belenchia et al. 1507.00330) na sprinklovaném 4D diamantu. Konkrétně:

1. Implementovat BD kernel pro 4D: B₄φ(x) = (4/√6) ρ^(1/2) [−φ(x) + Σ_{y<x} c(n_{xy}) φ(y)] kde c(n) jsou tabelované koeficienty a n_{xy} je počet prvků v mezivrstveném řetězci (viz Benincasa-Dowker).
2. Zkonstruovat G_R^BD jako inverzní operátor k B₄ na kauzálním setu (numericky přes Moore-Penroseův pseudoinverz nebo iterativní solver).
3. Sestavit iΔ^BD = i(G_R^BD − (G_R^BD)^T), spektrálně rozložit, změřit tvar spektra a rank-škálování.

**Predikce 2b:** BD spektrum bude mít čistší mocninový zákon λ_k ~ k^α s ostrým kolenem; exponent ranku bude robustní a blíže p = 3/4.

**Predikce ostatních:** BD spektrum bude rovněž ploché nebo deformované; p zůstane nerobustní.

**Výsledek rozhodne:** zda je selhání VYPOCET-06 specifické pro link-matrix G_R, nebo obecné pro jakoukoli lokální aproximaci G_R na 4D kauzálním setu.

### 3c. Test interpretace 2c (non-Hadamardovost)

**Experiment (algebraický, ne numerický):** Ověřit Hadamardovský charakter SJ stavu na 4D kauzálním diamantu vs. Rindler klínu přes explicitní výpočet leading singularity W_{SJ}(x,y) pro x → y (spacelike):

1. Analyticky: na 4D flat diamantu porovnat W_{SJ}(x,y) ~ H(x,y) + regulární část s Hadamardovou formou H(x,y) = u(x,y)/σ(x,y) + v(x,y) ln σ(x,y). Pokud koeficient u(x,y) nebo v(x,y) závisí na globální geometrii diamantu (okrajové podmínky na ∂D) — non-Hadamard. Viz analytické metody 2212.10592.
2. Numericky: porovnat SSEE na diamantu vs. na Rindler klínu (nebo de Sitter static patch) se stejným N a truncací. Pokud de Sitter/Rindler dává area law se srovnatelnou truncací kde diamant dá volume law — non-Hadamardovost diamantového SJ stavu je příčina.

---

## 4. Doporučená cesta: BD d'Alembertián jako VYPOCET-09

**Doporučení:** Navrhnout VYPOCET-09 jako 4D SSEE test s BD-d'Alembertián Greeno-vou funkcí namísto link matice.

**Zdůvodnění:**

1. **Interpretace 2b je falzifikovatelná a zachovává jádro hypotézy.** Pokud BD spektrum ve 4D dá robustní p ≈ 3/4, entropy-cluster hypotéza je zachována a VYPOCET-06 byl metodologický, ne fyzikální problém. Pokud ne, hypotéza je v 4D dále oslabena — jasný verdikt.

2. **BD d'Alembertián má přímou spojitost s Belenchia et al. 1507.00330.** Tato práce (citována v BRAINSTORM-01 jako klíčová pro spektrální dimenzi) ukazuje, že BD sonda dává universální d_s → 2 — což je přesně druh regularizace, který by mohl dát čistší spektrum pro entropy-cluster identifikaci.

3. **Fyzikální motivace je silnější.** Link matice je kombinatorický objekt; BD d'Alembertián je explicitně konstruován jako diskrétní aproximace kontinuálního operátoru s kontrolovanými korekčními členy. Je přirozenějším objektem pro identifikaci s modulárním cutoffem crossed-productu.

4. **Interpretace 2c (non-Hadamardovost) neeliminuje VYPOCET-09.** I pokud volume law plyne z non-Hadamardovosti SJ stavu, BD d'Alembertián G_R^BD může dát Hadamardovštější mody (protože jeho kernel je konstruován pro lepší UV chování). Oba mechanismy mohou platit zároveň.

**Alternativní rychlý test:** VYPOCET-09a — 3D verze (interpretace 2a) — je rychlejší (~1 týden numerické práce) a poskytne první rozhodnutí, zda problém je dimenze-specifický (2D výjimka) nebo objekt-specifický (link matice).

**Priorita:** VYPOCET-09b (BD 4D) > VYPOCET-09a (3D link-matrix) > algebraický Hadamard test.

---

## Souhrn stavu hypotézy H2g-3 po VYPOCET-06

| Dimenze | Objekt | Výsledek | Status |
|---------|--------|----------|--------|
| 2D | kauzální matice C, G_R = C | p = 0.519 ± 0.007 ≈ 1/2, robustní (39σ od alternativy) | POTVRZENO |
| 4D | link matice L, G_R = (√ρ/2π√6)·L | p = 0.65–0.98 (cutoff-závislé), slope-knee p ≈ 0.985, volume law R² = 0.998 | NEPOTVRZENO / KOMPLIKOVÁNO |
| 4D BD | BD d'Alembertián G_R^BD = B⁻¹ | čistý mocninový zákon (α≈3, R²=0.99) ALE α driftuje s N (+1.28), žádný robustní p=3/4 (frac→0, abs→1.2-1.7, slope-knee→0.98), area/volume inconclusive | **(b) ČÁSTEČNĚ POTVRZENA (tvar) / VYVRÁCENA (exponent)** — VYPOCET-09 |

Trojcestná identifikace (SSEE truncace = crossed-product cutoff = LQG area gap Δ = 4√3 π γ l_P² ve 4D) **zatím nemá numerický pilíř ve 4D**. 2D výsledek zůstává platný jako sanity check, ale nestačí pro tvrzení o 4D fyzice.

**Update po VYPOCET-09 (2026-06-06):** Interpretace (b) byla testována. BD nelokální d'Alembertián (G_R = B⁻¹) **opravil tvar spektra** — dává čistý mocninový zákon λ_k ~ k^(−α) (R²≈0.99) tam, kde link matice dávala ploché spektrum (R²=0.92). To je významný dílčí úspěch (b). **Ale ústřední teze (b) — že to oživí robustní p = 3/4 — byla VYVRÁCENA:** exponent α driftuje s N (+1.28 přes dekádu N, nekonvergoval při N≤3000), žádná definice cutoffu nedá robustní 3/4 (frakční→p≈0, absolutní práh→p∈[1.2,1.7] driftující, slope-knee→p≈0.98≈N¹ identicky jako VYPOCET-06), a area/volume zůstává cutoff-závislé/inconclusive. Selhání VYPOCET-06 tedy **není objekt-specifické** (link matice) — je hlubší. Smeared BD (ε≤0.6) léčí podmíněnost (cond 10¹⁰→10³), ale ne nekonvergenci α. **Váha se posouvá k interpretacím (a) [2D-only] a (c) [non-Hadamardovost].** Doporučená další cesta: algebraický Hadamard test (3c) nebo 3D link-matrix test (3a). Detaily: `vypocty/VYPOCET-09-ssee-bd-4d.md`.

**Update po VYPOCET-13 (2026-06-06) — ROZHODNUTÍ (a) vs (c):** Rozhodující test přes změnu geometrie regionu při **fixní dimenzi d=4**. **Interpretace (c) POTVRZENA, (a) VYVRÁCENA v silné formě.** Tři sbíhající se linie: (1) **4D kauzální SLAB s plochou half-space entangling plochou (bez rohů) dává AREA law** — S~L^2.00 (S~plocha^1.00, R²_area>R²_vol, robustní N∈[566,3772]) — tam, kde nested diamant dává VOLUME (VYPOCET-06, S~f^6.1, N=5000). 4D tedy **NENÍ inherentně objemové** (vyvrací silnou formu (a)); je objemové **na diamantu**, plošné **na slabu** — vinou geometrie regionu, ne dimenze. (2) Edge-effect kontrola (interiérní cut mimo stěny boxu) dává area law ještě čistší (S~L^2.18, R²=0.989). (3) **Hadamardova diagnostika lokalizuje anomálii do rohů diamantu:** krátkovzdálenostní SJ Wightman W(x,y) má v rohu diamantu anomální sklon (4D inside −1.53 vs corner −2.79; 2D inside −0.160 vs corner −0.095, sedí na analyticky známém non-Hadamardově místě u−v′=±2L z 2212.10592), zatímco na ploché slab ploše je tvar identický s hloubkou (deep −3.81 ≈ surface −3.85, žádná anomálie). **Důsledek pro H2g-3: hypotéza má cestu zpět do 4D se správnou geometrií regionu (Rindler/slab klín, kde SJ ≈ Unruh = Hadamard) — není 2D-kuriozita.** Poctivé limity: literatura (2008.07697/2412.07832) nepotvrzuje non-Hadamard↔volume jako přímý mechanismus (korelace tří měření, ne důkaz mechanismu); diamantová reference při redukovaném N=1600 nereprodukovala čistý volume law (přebráno z VYPOCET-06 N=5000); absolutní Hadamardovy sklony jsou finite-N deformované (diagnostika stojí na kontrastu, ne absolutní hodnotě). Detaily: `vypocty/VYPOCET-13-ssee-slab-4d.md`.

---

## Reference (klíčové pro toto přehodnocení)

- **1611.10281** — Sorkin, Yazdi: SSEE na causetech, dvojitá truncace
- **2008.07697** — Surya, Nomaan X, Yazdi: 4D SSEE de Sitter; n_max ~ N^(3/4) ansatz; volume→area přes slab truncaci
- **1712.04227** — causet SSEE, 4D volume law bez truncace
- **0909.0944** — Johnston: G_R^(4D) = (√ρ/2π√6)·L, link matice
- **1701.07212** — Nomaan X, Dowker, Surya: 2D/3D/4D G_R konvence
- **1507.00330** — Belenchia, Benincasa, Liberati, Marin, Marino, Bassi: BD d'Alembertián, spektrální dimenze d_s → 2 ve všech dimenzích
- **0911.2563** — Benincasa, Dowker: BD d'Alembertián konstrukce (4D koeficienty)
- **2212.10592** — Saravani, Aslanbeigi, Kempf (nebo přísl. autoři): SJ stav na 1+1D diamantu není Hadamardův
- **2206.10780** — Chandrasekaran, Penington, Witten: crossed-product type-II entropie, modulární cutoff
