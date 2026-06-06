# VYPOCET-03: Srovnání prefaktorů Λ ~ 1/√V

**Datum:** 2026-06-06  
**Soubory:** `core-data/calculations/lambda-prefactors/calc.py`, `results.json`, `lambda_prefactor_comparison.png`  
**Status:** Dokončeno

---

## Cíl

Porovnat dimenzionless prefaktor κ v relaci **Λ l_P² = κ / √(V/l_P⁴)** pro tři nezávislé přístupy ke kvantové gravitaci, které všechny predikují Λ ~ 1/√V nebo Λ ~ H²:

1. **Sorkin everpresent Λ** (causal sets / unimodulární gravitace)
2. **EDT running vacuum** Λ(H) = Λ₀ + 3ν H²  (Euclidean Dynamical Triangulations)
3. **CosMIn** N = 4π  (Padmanabhanovy „kosmické módy")

Motivace: hypotéza projektu tvrdí, že všechny tři mechanismy jsou realizací téže fluktuační statistiky δΛ ~ 1/√N sdružené ke 4-objemu. Pokud ano, jejich prefaktory musí souhlasit. Tento výpočet tuto shodu explicitně testuje — což je srovnání v literatuře dosud nepublikované.

---

## Metoda

**Konvence:** Λ l_P² = κ / √(V/l_P⁴), kde V = c_V / H₀⁴ je past 4-objem v Planckových jednotkách, c_V = 1 (Sorkinův minimální odhad: V ~ H⁻⁴, viz astro-ph/0209274 Eq. 2 a 3).

Z každého přístupu je extrahováno číslo κ (nebo „efektivní κ"):
- Sorkin: κ = 8πα, kde α je fenomenologický parametr fluktuací
- EDT: κ = 3ν, kde ν je dimenzionless kouplování běhu Λ
- CosMIn: κ_eff = Λ_CosMIn l_P² × √V (závislé na epoše — viz níže)

---

## Vstupy s citacemi

### Fyzikální konstanty

| Veličina | Hodnota | Zdroj |
|----------|---------|-------|
| l_P = √(ħG/c³) | 1.6163 × 10⁻³⁵ m | NIST CODATA 2018 |
| H₀ | 67.4 km/s/Mpc = 2.184 × 10⁻¹⁸ s⁻¹ | Planck 2018, arXiv:1807.06209 |
| Ω_Λ | 0.6889 | Planck 2018 |
| Λ l_P² (pozorovaná) | 2.866 × 10⁻¹²² | Planck 2018 (vypočteno z H₀, Ω_Λ) |
| V = H₀⁻⁴ (Planck j.) | 5.20 × 10²⁴³ | astro-ph/0209274 Eq. 2 |

### Zdroj A — Sorkin everpresent Λ

**Formule** (arXiv:2304.03819 Eq. 3.6, 3.9):
```
δΛ l_P² = 8π α / √(V / l_P⁴)
α ≡ (1/2) (l_P / l_cs)²
```
kde l_cs je Lorentzova diskrétní škála causal setu.

| Veličina | Hodnota | Zdroj |
|----------|---------|-------|
| α_obs (MCMC fit Bayesian průměr) | 0.0085 ± 0.0017 | arXiv:2307.13743 (Aspects II) |
| κ_Sorkin = 8πα | 0.2136 | tento výpočet |
| l_cs / l_P | 7.67 | z α: l_cs = l_P / √(2α) |

### Zdroj B — EDT running vacuum

**Formule** (arXiv:2408.08963 Eq. 75):
```
Λ(H) = Λ₀ + 3ν H²
```
kde ν se logaritmicky mění s objemem: ν = A′ / log(B′ √V₄).

| Veličina | Hodnota | Zdroj |
|----------|---------|-------|
| ν(Λ₀,phys) | (5.1 ± 1.3) × 10⁻⁴ | arXiv:2408.08963 Eq. 83 |
| A′ | 0.146 ± 0.039 (stat+syst) | arXiv:2408.08963 Table VII |
| B′ | 0.138 ± 0.010 | arXiv:2408.08963 Table VII |
| κ_EDT = 3ν | 1.53 × 10⁻³ | tento výpočet |

### Zdroj C — CosMIn

**Formule** (arXiv:1302.3226 Eq. 2):
```
Λ L_P² = (3/4) exp(−24π² µ),    µ ≡ N_c / (4π)
N_c = 4π  →  Λ L_P² = 3.4 × 10⁻¹²²
```

| Veličina | Hodnota | Zdroj |
|----------|---------|-------|
| Λ L_P² | 3.4 × 10⁻¹²² | arXiv:1302.3226 (citováno přímo) |
| N_c = 4π | ~ 12.57 | arXiv:1302.3226 Eq. 1–2 |
| κ_CosMIn (efektivní, t₀) | 2.452 | tento výpočet (Λ_CosMIn × √V — epochově závislé!) |

---

## Výsledky

### Tabulka prefaktorů

| Zdroj | κ | Charakter |
|-------|---|-----------|
| Sorkin (α = 0.0085) | **0.2136** | stochastická σ(δΛ), α fitován z pozorování |
| EDT (ν = 5.1 × 10⁻⁴) | **1.53 × 10⁻³** | deterministický koeficient H² |
| CosMIn (N_c = 4π) | **2.45** (efektivní, viz níže) | fixní Λ; žádný skutečný κ |

*(Konvence: Λ l_P² = κ / √(V/l_P⁴), V = H₀⁻⁴ v Planckových jednotkách, c_V = 1)*

### Poměry κ

| Poměr | Hodnota | log₁₀ |
|-------|---------|--------|
| κ_Sorkin / κ_EDT | **139.6** | +2.15 |
| κ_Sorkin / κ_CosMIn(eff) | 0.087 | −1.06 |
| κ_EDT / κ_CosMIn(eff) | 6.2 × 10⁻⁴ | −3.21 |

### Konvenční ambiguita

Konvence V = c_V / H⁴ s c_V = 1 sjednotí CosMIn a Sorkin jen pro c_V = 7.6 × 10⁻³ — fyzikálně nezdůvodnitelná hodnota. Pro CosMIn = EDT: c_V = 3.9 × 10⁻⁷. Sorkin a EDT se liší faktorem ~140 **nezávisle na volbě c_V** — jejich relace Λ-V mají různý funkcionální charakter.

---

## Interpretace pro hypotézu

Hypotéza projektu tvrdí, že Sorkin, EDT a CosMIn jsou realizací téže statistiky δΛ ~ 1/√N. **Tento výpočet tuto hypotézu v silné podobě vyvrací:**

1. **Sorkin vs. EDT: faktor 140.** Prefaktory se neshodují. Sorkin's α = 0.0085 (fenomenologicky fitovaný) a EDT's ν = 5.1 × 10⁻⁴ (z mřížkové simulace) dávají κ lišící se o dva řády. To není způsobeno volbou c_V — je to intrinsická neshoda.

2. **CosMIn nemá žádný κ.** CosMIn je jednorázová predikce fixního čísla Λ L_P² = 3.4 × 10⁻¹²² a neposkytuje dynamiku v V. „Efektivní κ" závisí na epoše (mění se s H(z)), takže porovnání s κ_Sorkin nebo κ_EDT je podmíněné na konkrétní epoše, nikoli fundamentálním vztahem.

3. **Funkcionální charakter se liší fundamentálně:**
   - Sorkin: Λ je **stochastická** proměnná s σ ∝ 1/√V — každá Hubbleova oblast realizuje jinou hodnotu
   - EDT: Λ je **deterministická** hladká funkce H(z) — Λ se mění se zkonmétrickým průměrem
   - CosMIn: Λ je **konstanta** — pouze jedna hodnota pro celý vesmír

4. **Slabší forma hypotézy zůstává otevřená:** Všechny tři predikují Λ ~ H² (Sorkin: δΛ ~ H²; EDT: ΔΛ = 3ν H²; CosMIn: Λ = (3/4)exp(−24π²)H_inf²/H₀²). Sdílení dimenzionální struktury H² je konzistentní s tím, že Hubbleova škála řídí vakuovou energii — ale numerické koeficienty jsou zcela různé.

---

## Limity výpočtu

1. **Volba c_V = 1:** Přesná numerická hodnota V závisí na kosmologické historii. Ahmed et al. (astro-ph/0209274) počítají V explicitně jako past light-cone integral (Eq. 3) a dostávají V ~ H⁻⁴ jako asymptotické přiblížení. Přesná hodnota numerického prefaktoru c_V by posunula κ_CosMIn(eff) o faktor ≲ 10, ale neshodou Sorkin–EDT to neovlivní.

2. **Sorkin α a selekční efekt:** α = 0.0085 je fitován tak, aby model byl kompatibilní s Ω_Λ ~ 0.7 dnes. Jde o podmíněnou hodnotu — nativní hodnota z causal-set teorie by se lišila. Z Aspects II (2307.13743) je α Bayesovsky průměrováno přes 90 000 seeds.

3. **EDT ν je z Planck-scale simulací:** Extrapolace ν od Planckových škál (několik l_P³) na kosmologické škály předpokládá logaritmický běh (Eq. 65 v 2408.08963). Tato extrapolace přes 61 řádů délky je velká.

4. **CosMIn "efektivní κ" závisí na epoše:** κ_CosMIn(eff) = Λ l_P² × √(V/l_P⁴) roste jako 1/H(z)² (klesá s rostoucím z), takže porovnání je platné jen pro z = 0.

5. **Nevyřešená otázka l_cs:** Aspects I/II nespecifikují numerickou hodnotu l_cs/l_P z prvních principů — α je fenomenologický parametr. Pokud by teorie kauzálních setů dávala l_cs ~ l_P (tedy α ~ 1/2), byl by κ_Sorkin ~ 4π ~ 12.6, a situace by se sice kvantitativně změnila, ale srovnání s κ_EDT (1.53 × 10⁻³) by zůstávalo neshodou o tři řády.

---

## Observační rozlišení tří scénářů

| Test | Sorkin | EDT | CosMIn |
|------|--------|-----|--------|
| w(z) | stochastické výkyvy kolem w = −1 | hladce roste s z: w ≈ −1 + ν Ω_m(z)/Ω_Λ | w = −1 přesně |
| Variance Ω_Λ v různých směrech | ANO — mezioblastní rozptyl | NE | NE |
| Odchylka od ΛCDM | O(0.5) v Ω_Λ histogramu | O(10⁻³) v w(z) | nulová |
| Hubbleova napětí | stochastická anizotropie H₀ | uniformní korekce | žádné |
| Rozhodující experiment | SKAO sky-patch variance, vysoké-z SNIa variance | DESI/Euclid w₀-wₐ na 0.1 % | jakákoliv detekce Λ-variation vyvrátí |

---

## Klíčové reference

| arXiv | Autoři | Rok | Co poskytuje |
|-------|--------|-----|-------------|
| astro-ph/0209274 | Ahmed, Dodelson, Greene, Sorkin | 2004 | Everpresent Λ originál; α parametr (Eq. 5); V ~ H⁻⁴ (Eq. 2–3) |
| 2304.03819 | Afshordi et al. | 2023 | Aspects I; δΛ = 4π(l_P/l_cs)²/√V (Eq. 3.6); α = (1/2)(l_P/l_cs)² (Eq. 3.9) |
| 2307.13743 | Afshordi et al. | 2023 | Aspects II; α = 0.0085 ± 0.0017 (Bayesian MCMC Pantheon+SH0ES) |
| 2408.08963 | Dai, Freeman, Laiho, Schiffer, Unmuth-Yockey | 2024 | EDT; Λ(H) = Λ₀ + 3νH²; ν = (5.1±1.3)×10⁻⁴ (Eq. 83); A′=0.146, B′=0.138 (Table VII) |
| 1302.3226 | H. Padmanabhan, T. Padmanabhan | 2013 | CosMIn; Λ L_P² = (3/4)exp(−24π²µ) (Eq. 2); N_c = 4π → Λ L_P² = 3.4×10⁻¹²² |
| 1807.06209 | Planck Collaboration | 2018 | H₀ = 67.4 km/s/Mpc, Ω_Λ = 0.6889 |
