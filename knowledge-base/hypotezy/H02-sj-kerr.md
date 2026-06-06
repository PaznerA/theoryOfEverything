# H02 — SJ stav na Kerrově prostoročase

**Status:** PLAUSIBLY-NOVEL (dle preprint-checks.md, bod c)
**Datum:** 2026-06-06
**Relevantní věta novosti:** Žádný existující výsledek explicitně nekonstruuje SJ stav pro Kerrovo pozadí (rotující černá díra). Pracuje se zatím pouze se statickými (Schwarzschild, de Sitter) nebo konformně plochými prostoročasy.

---

## 1. Co přesně SJ konstrukce potřebuje a co je k dispozici pro Kerr

### 1a. Ingredience SJ konstrukce (obecně)

SJ (Sorkin-Johnston) stav je definován *výhradně* ze struktury prostoročasu — nepotřebuje symetrie ani Killingův vektorový dvodbod. Postup:

1. **Pauli-Jordanova funkce** (komutátorová funkce) `Δ(x,y) = G_ret(x,y) - G_adv(x,y)` — antisymetrické bisolution Kleinovy-Gordonovy rovnice.
2. **Omezená oblast:** Pro každou kompaktní, relativně kompaktní podmnožinu M' ⊂ M globálně hyperbolického prostoročasu tvoří integrální operátor `A = iΔ` omezený samoadjungovaný operátor na L²(M', dvol).
3. **Spektrální rozklad:** `A = Σ_k λ_k |ψ_k⟩⟨ψ_k|`, kde `λ_k ∈ ℝ`, `⟨ψ_k, ψ_l⟩_L² = δ_{kl}`.
4. **Kladná část:** `A_+ = (1/2)(|A| + A)`, tedy suma přes kladná vlastní čísla λ_k > 0.
5. **Wightmanova funkce SJ stavu:** `W_SJ(x,y) = Σ_{λ_k > 0} λ_k ψ_k(x) ψ_k*(y)`.

Výsledný stav je **čistý quasi-volný stav** (pure quasifree state) určený jedinečně oblastí a polem — bez jakéhokoli dodatečného vstupu o symetriích.

Podmínky existence:
- M' je relativně kompaktní v globálně hyperbolickém M.
- `A = iΔ` je omezený na L²(M'): garantováno kompaktností oblasti.
- Vlastní čísla a vektory musí tvořit úplnou bázi L²(M') — splněno samoadjungovaností A.

### 1b. Co je k dispozici pro Kerr

**Teukolskyho módy:** Pro skalární pole na subextrémním Kerru (|a| < M) lze separovat Kleinovu-Gordonovu rovnici v Boyer-Lindquistových souřadnicích: `Φ = Σ_{lm} R_{lm}(r) S_{lm}(θ) e^{imφ} e^{-iωt}`. Radiální část R_{lm}(r) řeší Teukolskyho rovnici — kompletní sada řešení je výborně prozkoumána (viz Dafermos-Rodnianski, 2007–2023).

**Retardovaný a advancovaný Greenův operátor:** Existuje pro subextrémní Kerr na exteriorou (r > r_+) i v kombinaci s blízkým interiorem (Dafermos-Holzegel-Rodnianski, Dyatlov). Pauli-Jordanova funkce `Δ = G_ret - G_adv` je tedy k dispozici ve smyslu distribučního kernel.

**Superradiance jako problém pro standardní konstrukce:** V superradiantním pásmu `0 < ω < mΩ_H` (kde `Ω_H = a/(r_+^2 + a^2)` je úhlová rychlost horizontu) se „up-módy" (přicházející z minulého horizontu) chovají nestandardně: jejich norma Kleinovy-Gordonovy symplektické formy je záporná, i když ω > 0. Konkrétně:

- Pro `ω > mΩ_H`: up-mód má standardní pozitivní KG-normu.
- Pro `0 < ω < mΩ_H`: up-mód má **zápornou** KG-normu — tzv. superradiantní mód.
- Výsledek: nelze globálně rozložit pole na kladné a záporné frekvence konzistentním způsobem respektujícím symetrii Killingova pole `∂_t` a izotermičnost horizontu.

Tato překážka **přímo** brání definici Hartle-Hawkingova, Boulwareova i standardního vakua: žádný z nich nemá přímý analog na Kerru (Balakumar 2023; Kay-Wald 1991).

**SJ stav tuto překážku obchází:** SJ konstrukce nevyžaduje rozklad na pozitivní/záporné frekvence pomocí Killingova pole. Místo toho požaduje pouze samoadjungovanost operátoru A = iΔ na L²(M') pro omezenou oblast M'. Superradiance (jako globální vlastnost spojená s ergosférikou) nebrání definici A ani jeho spektrálnímu rozkladu lokálně vně horizontu.

---

## 2. Proč Kay-Wald a Fewster-Verch no-go věty SJ přímozakazují

### 2a. Kay-Waldova věta (1991)

**Přesné znění (relevantní část):** Na Kerrově maximálně rozšířeném prostoročase neexistuje quasi-volný stav, který by byl:
(i) invariantní pod Killingovými isometriemi `∂_t` a `∂_φ`,
(ii) Hadamardovský v blízkosti horizontu,
(iii) globálně definovaný.

Klíčový předpoklad: **isometrická invariance**. SJ stav tuto podmínku nevyžaduje. SJ stav na Kerru by **nebyl** invariantní pod `∂_φ` (a pravděpodobně ani pod `∂_t`), protože SJ je definován oblastí, nikoliv Killingovou symetrií. Ergo: Kay-Wald věta na SJ stav **přímo nedopadá**.

Dodatečný komentář: Kay-Wald věta říká, že pokud takový symetrický stav existuje, pak je termální při Hawkingově teplotě vně horizontu. Neříká nic o stavech bez symetrie.

### 2b. Fewster-Verchova věta o dynamické lokalitě (2012–2013)

**Fewster-Verch no-go (nutnost Hadamardovy podmínky, arXiv:1307.5242):** Ve třídě ultrastatic slab prostoročasů s kompaktním Cauchyho povrchem: kvadratické fluktuace Wickova čtverce `⟨(∂_t Φ)²⟩²_ω - ⟨(∂_t Φ)²⟩_ω²` jsou konečné **jedině pokud** stav ω je Hadamardovský (relativně k Wickově normálnímu pořadí danému Hadamardovým stavem). SJ stavy **obecně nesplňují** Hadamardovu podmínku, a proto v tomto smyslu selhávají.

**Proč to pro nás není fatální — SJ ≠ Hadamard je feature, ne bug:**

1. Fewster-Verch pracuje **explicitně** s ultrastatic slab geometriemi s kompaktním Cauchyho povrchem. Kerr (a dokonce ani bounded exterior region vně horizontu) do této kategorie nespadá.
2. Na Kerru Hadamardovy stavy s požadovanými symetriemi **neexistují** (Kay-Wald). SJ tedy poskytuje stav i tam, kde Hadamardova rodina selhává jako celek. SJ je **unique fallback**.
3. Infrarelná diverzence Wickova čtverce v SJ stavu je spojena s hranicí domény M', nikoliv s interiorovou fyzikou. Pro výpočty uvnitř oblasti (entropie, superradiance) nemusí vadit.
4. **Softenovaný SJ stav** (Jubb-Surya 2022, arXiv:2212.10592) — drobná modifikace, která obnoví Hadamardovu vlastnost za cenu ztráty striktní jedinečnosti — může být alternativní volbou pro observabily.

**Fewster-Verchova věta o přirozených stavech (2012):** Pokud lokálně kovariantní teorie připouští „přirozený stav" (natural state) a splňuje dynamickou lokalitu + extendovanou lokalitu, pak je algebra triviální. Tato věta říká, že neexistuje žádný přirozený (funktorový) stav pro celou třídu prostoročasů najednou — ale SJ stav na jednotlivé omezené oblasti M' přirozený **je** (Sorkin, Bernal-Sanchez). Věta tedy nejenže nezakazuje SJ, ale přímo vysvětluje, proč musíme volit oblast-specifický přístup jako SJ.

---

## 3. Tři konkrétní strategie útoku

### Strategie I (nejlevnější): Numerický sprinkling do Kerrova konformního diagramu

**Myšlenka:** Provést Poissonův sprinkling do ohraničené oblasti M' vně horizontu Kerru a numericky zkonstruovat matici Pauli-Jordanovy funkce, poté diagonalizovat a získat SJ stav.

**Technický postup:**

1. **Volba oblasti M':** Ohraničená podmnožina externího komunikačního domény Kerru: `{r_+ + ε ≤ r ≤ r_max, t_1 ≤ t ≤ t_2, θ ∈ [0,π], φ ∈ [0,2π)}` v Boyer-Lindquistových souřadnicích. Tato oblast je relativně kompaktní a globálně hyperbolická (kauzální struktura BL souřadnic je dobře prozkoumána; Penroseův diagram exteriorní oblasti Kerru je isomorfní s exteriorní oblastí Schwarzschildu).

2. **Sprinkling:** Generovat N bodů dle Poissonova procesu s hustotou ρ = N/Vol(M') ve flat Lebesgue míře na (t,r,θ,φ); pak reweightovat dle √(-g) dV kde pro Kerr v BL souřadnicích `√(-g) = Σ sin θ` (`Σ = r² + a²cos²θ`).

3. **Kauzální relace:** Pro každý pár (x,y) v M': určit kauzální pořadí numericky. Algoritmus z Glaser-Reid-Surya (arXiv:0811.4235) pro Schwarzschild rozšířit na Kerr (přidáme azimutální propletení; nutno integrovat nulové geodetiky v Kerr metrice — netriviální, leč přímočaré). Výsledek: binární matice C_{ij} = 1 pokud x_i ≺ x_j.

4. **Retardovaný Greenův operátor:** V diskrétním případě `G_ret = (C_{ij}/ρ)` (retardovaný propagátor na kauzální množině po kalibraci). Pak `Δ_{ij} = G_ret_{ij} - G_adv_{ij}`.

5. **Diagonalizace:** Matice `A = iΔ` (N×N hermitovská) — numericky diagonalizovat. Vybrat vlastní vektory k kladným vlastním číslům a sestavit `W_SJ = Σ_{λ_k > 0} λ_k v_k ⊗ v_k†`.

**Klíčová otevřená otázka pro Kerr:** Dostatečná hustota sprinkling pro zachycení struktury superradiantních módů — tyto módy mají charakteristické prostorové vzory poblíž ergosféry a horizontu. Pravděpodobně bude potřeba N ~ 10^4–10^5 bodů a selektivní zahušťování poblíž r_+.

**Dostupné nástroje:** Algoritmus kauzálních relací na Schwarzschild (Glaser 2008), numerický SJ pro 2D kauzální diamant (Mathur-Surya 2019, arXiv:1906.07952), kód pro sprinkling v de Sitter (Surya skupina). Rozšíření na Kerr představuje kombinaci těchto existujících komponent.

**Odhadovaná pracnost:** 2–4 týdny pro skalární pole, s dostupným Python/numpy toolchain.

---

### Strategie II (2D analog): Rotující BTZ nebo Kerrův ekvatoriální řez

**Myšlenka:** Místo plného 4D Kerru pracovat s nižšedimenzionálním analogem, kde je analytická kontrola lepší.

**Varianta A — Rotující BTZ (2+1D):**

BTZ černá díra v anti-de Sitter prostoru (2+1D) má rotující variantu popsanou `ds² = -(N^0)² dt² + (N^0)^{-2} dr² + r²(dφ + N^φ dt)²` s horizontem při `r = r_+`. Horní (superradiance) analogicky existuje pro `ω < mΩ_+` (kde `Ω_+ = J/(2Mr_+²)`). Výhody:
- Prostoročas je lokálně AdS₃ — lze použít známé Greenovy funkce.
- 2+1D: matice Δ_{ij} pro N~1000 je snadno diagonalizovatelná.
- Rotace je přítomna, ergoregion existuje.
- Srovnání: statický BTZ je analog Schwarzschildu; rotující BTZ je analog Kerru.

**Varianta B — Kerrův ekvatoriální řez:**

V ekvatoriálním řezu θ = π/2 se Kerrova metrika stává efektivně 2D:
`ds²|_{θ=π/2} = -(1 - 2M/r + a²/r²) dt² - 2(2Ma/r) dt dφ + ...`

Integrací azimutálního φ lze obdržet efektivní (1+1)D teorii (Frolov-Thorne vakuum vychází z podobného rozkladu). Pro SJ stav: pracovat s 2D oblastí `(t,r)` v ekvatoriálním řezu, považovat φ-odezvu jako sumační faktor. Tato redukce je standardní pro výpočty Hawkingova záření u Kerru.

**Proč tento krok:** Pokud SJ spektrum rotujícího BTZ nebo ekvatoriálního řezu vykazuje charakteristické rysy superradiance (anomálie v distribuci vlastních čísel při ω ~ mΩ_H), poskytuje to silný důkaz pro plný 4D výpočet.

**Odhadovaná pracnost:** 1–2 týdny (BTZ: analytičtější; ekvatoriální řez: lze adaptovat 1906.07952 kód).

---

### Strategie III (plná modová konstrukce): Analytický SJ stav přes Teukolskyho módy

**Myšlenka:** Provést SJ konstrukci analyticky v Teukolskyho bázových módech a zkontrolovat konvergenci a pozitivnost.

**Postup:**

1. Rozvinout skalární pole `Φ = Σ_{lmω} φ_{lmω}(r,θ) e^{imφ} e^{-iωt}`.
2. Zapsat Pauli-Jordanovu funkci jako modální součet:
   `Δ(x,x') = Σ_{lm} ∫ dω [u^in_{lmω}(x) u^in*_{lmω}(x') - c.c.] + [up-módy]`
   kde `u^in`, `u^up` jsou standardní Teukolskyho in/up-módy.
3. Omezit integraci na oblast M' = [r_+, r_max] × [t_1, t_2] imes S² a vzít L²(M') integrální jádro.
4. Identifikovat operátor `A = iΔ` jako operátor na L²(M') a formálně zapsat jeho spektrální rozklad přes modální bázi.
5. Klíčová otázka: přispívají superradiantní módy (0 < ω < mΩ_H) kladnými nebo zápornými vlastními čísly? Odpověď závisí na znaménku „váhové funkce" v integrální formě A.

**Klíčová technická výzva:** Teukolskyho up-módy v superradiantním pásmu mají zápornou symplektickou normu, ale operátor A = iΔ je definován s ohledem na L²-normu, nikoliv KG-normu. Spektrum A tedy není a priori negativní pro superradiantní módy — to je jádro novosti hypotézy: SJ stav může poskytnout dobře definovaný stav i v superradiantním pásmu, přičemž záporná KG-norma se „překryje" pozitivní L²-hmotností oblasti.

**Výsledek (pokud se podaří):** Explicitní Wightmanova funkce
`W_SJ(x,y) = Σ_{lm} ∫_{λ_k > 0} dω_k ψ_k(x) ψ_k*(y)`
jako funkcionál závislý pouze na parametrech M, a, r_max a volbě skalárního pole (masové číslo m_φ).

**Odhadovaná pracnost:** 2–4 měsíce, vyžaduje pokročilou analýzu operátorů na nekonečnědimenzionálních prostorech.

---

## 4. Co by výsledek znamenal

### 4a. SJ stav jako vstup pro studium superradiance

Superradiantní zesílení vlnových balíků u Kerru je kvantitativně popsáno reflexním koeficientem `|R_{lm}|² > 1` pro ω ∈ (0, mΩ_H). Standardní kvantový výpočet superradiance vyžaduje specifikaci vstupního kvantového stavu. Přirozené volby (Boulware, Hartle-Hawking) neexistují na Kerru. SJ stav by poskytl **kanonický, bezparametrický vstupní stav** pro výpočty:
- Středního počtu superradiantně emitovaných kvant: `⟨N_{out}⟩_SJ`
- Kvantových fluktuací superradiantního záření
- Entropia párů emitovaných a absorbovaných kvant

### 4b. SJ stav a Hawkingovo záření Kerru

Hawkingovo záření u Kerru je formálně popsáno Unrahovým stavem (arXiv:2602.09796 prokázal jeho existenci a Hadamardovskost pro Teukolskyho pole). SJ stav by byl **alternativní** (a kanoničtější) vstupní stav; srovnání `W_SJ` vs. `W_Unruh` by odhalilo:
- Zda je Hawkingovo záření pozorovatelné bez ohledu na volbu stavu (universalita)
- Jak je entanglementová struktura záření závislá na volbě stavu

### 4c. Entropie černé díry a SJ spektrum

Spektrální entropie definovaná přes SJ Wightmanovu funkci (Spectral Spacetime Entropy, SSE; arXiv:2602.16782) poskytuje kovariantní definici spacetime entanglement entropy. Pro Kerr by SJ stav umožnil:
- Definovat SSE pro rotující černou díru bez ad hoc volby stavu
- Porovnat s Bekenstein-Hawkingovou entropií `S_BH = A/(4l_P²)`
- Zkontrolovat, zda SSE respektuje Pageovu křivku (jak naznačuje arXiv:2406.13949 pro rotující Kerr)

### 4d. Kanonická QFT na rotující ČD jako základ pro gravitační korekce

SJ stav je jedinečně určen oblasti M' — nepotřebuje fixovat asymptoticku strukturu. To ho činí přirozeným kandidátem pro **semiclassical backreaction** u Kerru: výpočet `T_μν` v SJ stavu jako vstup pro Einsteinovy rovnice. Toto je nezbytný krok k porozumění dynamiky rotující černé díry s kvantovými efekty (superradiantní nestabilita, kvantové vlasy).

---

## 5. Bibliografická mapa

| Odkaz | Relevance |
|-------|-----------|
| Afshordi-Aslanbeigi-Sorkin, arXiv:1205.1296 | Původní SJ konstrukce pro kontinuum |
| Jubb-Surya, arXiv:2212.10592 | Non-Hadamard SJ v 1+1D; softened SJ |
| Mathur-Surya, arXiv:1906.07952 | Numerický SJ v 2D kauzálním diamantu |
| Glaser, arXiv:0811.4235 | Algoritmus sprinkle pro Schwarzschild |
| Kay-Wald, Phys. Rep. 207 (1991) | No-go pro symetrické Hadamardovy stavy na Kerru |
| Balakumar, arXiv:2303.13488 | Superradiance a kvantové stavy na ČD |
| Dafermos-Luk 2602.09796 | Unruhův stav pro Teukolskyho pole — Hadamardovský na Kerru |
| Fewster-Verch, arXiv:1307.5242 | Nutnost Hadamardovy podmínky (ultrastatic slab) |
| Fewster-Verch, arXiv:1106.4785 | Dynamická lokalita — no-go pro přirozené stavy |
| Dafermos-Rodnianski, arXiv:2007.07211 | Ohraničenost Teukolskyho rovnice na Kerru |

---

## 6. Shrnutí

SJ stav na Kerru je:
- **Matematicky přípustný:** omezená oblast vně horizontu splňuje všechny podmínky SJ konstrukce; superradiance nebrání samoadjungovanosti A = iΔ na L²(M').
- **Mimo dosah existujících no-go:** Kay-Wald zakazuje symetrické Hadamardovy stavy; Fewster-Verch pracuje s ultrastatic slab — ani jedna věta se na SJ pro Kerr nevztahuje.
- **Potenciálně unikátní stav:** V oblasti (rotující ČD), kde jiné přirozené volby selhávají, dává SJ kanonický, oblastně určený stav.
- **Fyzikálně bohatý:** Přímé vstupy pro výpočty superradiance, Hawkingova záření, SSE a backreaction.

Nejmenší první krok: implementace Strategie II (rotující BTZ nebo ekvatoriální řez Kerru) v prostředí numerické kauzální množiny — navazuje přímočaře na dostupný kód z arXiv:1906.07952.
