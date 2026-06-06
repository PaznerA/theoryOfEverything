# VYPOCET-17: Kosmologická konstanta z fermionově-indukované gravitace (H4g-3)

**Datum:** 2026-06-06
**Soubory:** `core-data/calculations/lambda-induced/{calc.py, results.json, sector_ledger.png, pauli_and_quartic.png}`
**Status:** Dokončeno (exaktní sympy aritmetika; konvence ověřeny proti literatuře v průběhu výpočtu — Chamseddine-Connes hep-th/9606001 + Marcolli „Spectral Action Gravity and Cosmological Models", citováno verbatim).
**Hypotéza:** H4g-3 — je-li spektrální akce fermionově-indukovaná (Sacharovova) gravitace (F-014, index-chráněné −18/11), předpovídá *tatáž* logika racionální fermion-počítací formu i pro kosmologickou konstantu? Existuje *druhá* index-chráněná identita analogická −18/11?
**Návaznost:** Uzavírá poslední riziko draftu-02 („interpretace musí přežít, že akce obsahuje i kosmologický člen"). Přímo navazuje na VYPOCET-02 (−18/11) a VYPOCET-11 (index-zámek).

---

## Cíl

Draft-02 stojí na exaktní identitě `koef(C²)/koef(Euler) = −18/11`, sdílené spektrální akcí a anomálním poměrem `c/(−a)` Weylova fermionu, a na čtení „spektrální akce = fermionově-indukovaná gravitace". Otevřené riziko: spektrální akce obsahuje i **kosmologický** (a₀) a **Einstein-Hilbertův** (a₂) člen. Pokud by *tatáž* fermionová indukce předpovídala racionální fermion-počítací formu pro Λ (druhou index-identitu), byl by to silný argument pro indukci jako *mechanismus*. Pokud žádný takový poměr není, hypotéza H4g-3 padá **čistě** — a to je plnohodnotný výsledek, který riziko uzavírá.

Čtyři podotázky (vše exaktní racionály):

1. **a₀ (Λ) člen** — kosmologický: jeho racionální závislost na obsahu polí (45 vs 48 Weylů).
2. **a₂ (Einstein-Hilbert)** — `G_indukované ~ 1/(f₂Λ²·N)`: exaktní racionály.
3. **Druhá index-identita?** — existuje mezi {a₀, a₂, a₄} obsah-nezávislý poměr jako −18/11? Spočítat a₀:a₂:a₄ exaktně; otestovat, zda `Λ_cc/m_Pl²` je obsah-nezávislé.
4. **Poctivá konfrontace s problémem kosmologické konstanty** — indukovaná Λ je cutoff-kvartická (standardní katastrofa). Dělá ji fermionová indukce HORŠÍ, STEJNOU, nebo se objeví kompenzace? Mění ν_R (45→48) znaménko/strukturu? Pauliho supertrace podmínka (ΣB − ΣF) pro NCG obsah.

---

## Metoda a konvence (ověřeno proti literatuře)

### Spektrální akce — Chamseddine-Connes hep-th/9606001; Marcolli (NCGCosmoCRP)

Asymptotická expanze (citováno verbatim z Marcolliho přehledu, rov. master):

```
Tr f(D/Λ) ~ 2 Λ⁴ f₄ a₀ + 2 Λ² f₂ a₂ + f₀ a₄
```

kde **a₀ → kosmologický člen**, **a₂ → Einstein-Hilbert**, **a₄ → Weyl² + Gauss-Bonnet**. Pro skoro-komutativní geometrii C⊕H⊕M₃(C) (Marcolli, rov. pro α₀, τ₀, γ₀):

```
1/(2κ₀²) = (96 f₂Λ² − f₀ c) / (24π²)              [E-H koeficient]
γ₀       = (1/(4π²)) (48 f₄Λ⁴ − f₂Λ² c + d)       [efektivní Λ]
α₀       = −3 f₀/(10π²)   [C²]
τ₀       =  11 f₀/(60π²)  [R*R*]   →  α₀/τ₀ = −18/11   (VYPOCET-02)
```

**Momenty cutoff-funkce:** `f₄ = ∫₀^∞ x f(x) dx`, `f₂ = ∫₀^∞ f(x) dx`, `f₀ = f(0)`. Funkce `c = Tr(MM†)`, `d = Tr((MM†)²)` jsou Yukawovy/Majoranovy stopy (Majoranovy hmoty pravotočivých neutrin), které **běhají** s energií. V bezhmotném/volném limitu (M→0) je `c = d = 0` a gravitační sektor je **čisté počítání** (Tr(1_F)).

### Heat-kernel a₀, a₂ — Gilkey; Vassilevich hep-th/0306138, rov. (4.26-4.27)

```
a₀(x) = (4π)⁻² tr_V(1)
a₂(x) = (4π)⁻² (1/6) tr_V(6E + R)
```

Pro Diracův čtverec (Lichnerowicz E = −R/4, tr_V(1) = 4): `a₀ = 1/(4π²)` (per Dirac), `a₂ = −R/(48π²)`.

### Pauliho/supertrace podmínky — Pauli 1951; Visser arXiv:1610.07264; Akhmedov hep-th/0204048

Kvartická vakuová divergence se ruší ⟺ `STr 1 = nB − nF = 0` (stejné počty bosonů/fermionů); kvadratická ⟺ `STr M² = 0`; logaritmická ⟺ `STr M⁴ = 0` (tři supertrace podmínky).

---

## Výsledky

### Q1 — a₀ (kosmologický) člen

- **a₀ je čistá Tr(1_F).** Λ⁴-prefaktor `2 f₄Λ⁴·a₀` škáluje **lineárně v N = Tr(1_F)** — počet fermionových stupňů volnosti.
- Efektivní kosmologická konstanta (bezhmotný limit): **`γ₀ = 12 f₄Λ⁴/π²`** per jednotka Tr(1_F).
- **Závislost na obsahu: LINEÁRNÍ v N.** Přidání ν_R (45→48) změní jen **celkovou magnitudu** faktorem 48/45 = 16/15, NE strukturu.

### Q2 — a₂ (Einstein-Hilbert) člen

- a₂ koeficient u R (per Dirac): **`−1/(48π²)`**.
- `1/(2κ₀²) = 4 f₂Λ²/π²` (bezhmotný limit) → **`G_indukované ~ 1/(f₂Λ²·N)`**, opět lineární v N, **tentýž celkový faktor jako a₀**.

### Q3 — druhá index-identita? **NE.**

| poměr | hodnota | obsah-nezávislý? | scheme-robustní? |
|---|---|---|---|
| a₀/a₂ (per mode) | **12** | ano (per mode) | **NE** — nese (f₄/f₂)·Λ² |
| a₄: c/(−a) | **−18/11** | **ano** | **ano** (index-chráněné) |
| Λ_cc (bezhmotné, s N) | (f₄/f₂)·Λ²·ĝ/(2k̂) | N se ruší — ale **degenerovaně** | **NE** — dimenzionální |
| Λ_cc/m_Pl² | π²f₄/(2N f₂²k̂²) | **NE** (explicitní 1/N) | NE |

**Klíčové rozlišení.** Poměr a₀/a₂ = 12 je čistý racionál, ALE **není** to konvence-nezávislý invariant: a₀ a a₂ sedí na **různých řádech cutoffu** (f₄Λ⁴ vs f₂Λ²), takže jejich poměr nese `(f₄/f₂)·Λ²` — je **dimenzionální** a **závislý na tvaru cutoff-funkce**. Naproti tomu −18/11 je poměr dvou členů na **témž řádu** (oba f₀, oba Λ⁰), takže f₀ i Λ se vykrátí a zbude čisté, scheme-robustní, index-chráněné číslo.

`Λ_cc` (bezhmotné) sice vyjde N-nezávislé, ale **degenerovaně**: N se vykrátí jen proto, že čitatel (γ₀) i jmenovatel (m_Pl²) nesou *tentýž* celkový faktor Tr(1_F). Výsledek pořád nese (f₄/f₂)·Λ² → dimenzionální, scheme-závislé, NE index-ochrana. Fyzikální bezrozměrný poměr `Λ_cc/m_Pl²` nese **explicitní 1/N** → je **obsah-závislý**.

**Verdikt Q3: žádná druhá identita typu −18/11 pro Λ neexistuje.** Jediný skutečně obsah-nezávislý, scheme-robustní poměr v celé expanzi je a₄-vnitřní α₀/τ₀ = −18/11, právě proto, že je to poměr členů na stejném řádu (= ten index-chráněný).

### Q4 — problém kosmologické konstanty: indukce NEPOMÁHÁ

- **Cutoff-škálování:** indukované `γ₀ ~ 12 f₄Λ⁴/π²` — **kvartické** v cutoffu = standardní katastrofa kosmologické konstanty. Naivní nesoulad při Λ ~ M_Pl: **~10¹²²** řádů.
- **Znaménko:** `f₄ = ∫ x f(x) dx > 0` pro kladný cutoff → `γ₀ > 0` (kladná, de Sitterovská), Planckova magnituda.
- **Dělá to fermionová indukce horší/stejné?** **STEJNÉ-jako-standardní** (kvartické). Diracovo moře přispívá plnou Λ⁴; indukce to neztlumí. Per fermion to dělá marginálně **větší**, nikdy neruší.
- **ν_R efekt:** všechny fermiony vstupují do `Tr f(D/Λ)` se **stejným znaménkem** (stopa přes pozitivně-definitní fermionový Hilbertův prostor). 45→48 násobí γ₀ faktorem 48/45 = 16/15. **ν_R znaménko NEMĚNÍ.**
- **Pauliho supertrace pro NCG obsah:**
  - Fermiony (Weyl, 2 reálné d.o.f. každý): nF = 90 (bez ν_R) / 96 (s ν_R).
  - Bosony: 12 bezhmotných vektorů × 2 polarizace = 24; Higgs komplexní dublet = 4 reálné skaláry → nB = 28.
  - **`STr 1 = nB − nF`: bez ν_R = 28 − 90 = −62; s ν_R = 28 − 96 = −68.** Nikdy 0.
  - **ν_R dělá nerovnováhu boson/fermion HORŠÍ** (−62 → −68, více fermionů), žene kvartickou divergenci **dál** od Pauliho kompenzace, ne blíž.

**Verdikt Q4:** indukovaná Λ je cutoff-kvartická (standardní problém). Fermionová indukce nepomáhá a ν_R nerovnováhu počtů zhoršuje. Žádná supertrace podmínka (STr 1 = STr M² = STr M⁴ = 0) NCG obsahem splněna není. Problém jemného ladění kosmologické konstanty je logikou −18/11 **nedotčen**.

---

## Interpretace pro hypotézu H4g-3

**H4g-3 je VYVRÁCENA jako pozitivní hypotéza — čistě a s plně dokumentovanými konvencemi. To je plnohodnotný výsledek: uzavírá poslední riziko draftu-02.**

1. **Žádná druhá index-identita.** −18/11 je výjimečné *právě proto*, že je to poměr **uvnitř** a₄ (stejný řád f₀Λ⁰), kde se cutoff i škála vykrátí a zbude index-chráněné číslo. a₀ (kosmologický) a a₂ (E-H) sedí na **různých** cutoff-řádech; jakýkoli jejich poměr je dimenzionální a scheme-závislý. Fermion-počítací forma pro Λ existuje, ale je **lineární v N** (triviální celková magnituda), ne racionální invariant.

2. **Asymetrie a₄ vs a₀/a₂ je strukturní, ne náhodná.** a₄ je konformní (R²-koeficient = 0, VYPOCET-11), jeho C²/Euler poměr je pravá anomálie s index-stínem (Â-genus). a₀, a₂ takový provázaný topologický objekt **nemají** — jsou to obyčejné heat-kernel objemové/skalárně-křivostní členy, jejichž absolutní hodnota nese cutoff-momenty f₄, f₂. Proto je −18/11 chráněné a Λ-poměr ne.

3. **Indukce neřeší CC problém — a poctivě to říká.** Indukovaná Λ je kvartická, ν_R ji zvětšuje a zhoršuje Pauliho nerovnováhu. Toto **NENÍ** v rozporu s draftem-02: draft tvrdí jen identitu *poměru* C²/Euler v Diracově sektoru, nic o Λ. VYPOCET-17 ukazuje, že tvrzení se **správně nerozšiřuje** na kosmologický člen — a to je přesně to, co recenzent potřebuje slyšet: identita −18/11 je ostře omezena na konformní a₄ sektor a NEimplikuje žádnou predikci pro Λ. Riziko „akce obsahuje i kosmologický člen" je tím uzavřeno: kosmologický člen je na indukované straně účetní knihy, lineární v počtu, bez chráněného poměru.

**Pro draft-02:** poslední výpočetní riziko uzavřeno. Recenzentovi lze odpovědět: „Ano, akce obsahuje a₀ (kosmologický) a a₂ (E-H) člen. Oba jsou fermionové vakuové momenty lineární v Tr(1_F), ale NEnesou druhou obsah-nezávislou identitu — pouze a₄ (konformní, index-chráněný) ji nese. Identita −18/11 se proto na kosmologickou konstantu nepřenáší a žádnou predikci Λ neslibuje." Žádný draft-04 kandidát z Λ; H4g-3 je čistá poprava.

---

## Limity výpočtu

- **Yukawovy/Majoranovy stopy.** Plné a₀, a₂ v SM dostávají dressing přes c = Tr(MM†), d = Tr((MM†)²) (Majoranovy hmoty ν_R). Použili jsme bezhmotný/volný limit (c = d = 0) pro čistou počítací formu; hmotné členy mění magnitudu, ne strukturní závěr (kvartické škálování, žádný chráněný poměr).
- **Tr(1_F) konvence.** CC počítají Tr(1_F) v K-O-zdvojené bázi (2·16·3 = 96), ne v 45/48 Weylově počtu. Protože a₀, a₂ škálují *lineárně* v Tr(1_F), je relativní obsahová závislost (45 vs 48) tatáž bez ohledu na konvenci celkového faktoru; všechny poměry závisí na N jen přes týž celkový faktor.
- **Scheme-závislost.** Na rozdíl od −18/11 (poměr na stejném řádu, f-nezávislý) Λ-koeficienty explicitně nesou f₄, f₂ → scheme-závislé. To je jádro negativního výsledku, ne jeho limit.
- **Pauliho počítání d.o.f.** Použity on-shell reálné stupně volnosti (vektor × 2 polarizace, Weyl × 2). Off-shell/gauge-fixed počítání mění absolutní čísla, ne závěr STr 1 ≠ 0 ani směr ν_R efektu (více fermionů → zápornější STr 1).

---

## Reprodukce

```
cd core-data/calculations/lambda-induced && python3 calc.py
# → results.json, sector_ledger.png, pauli_and_quartic.png
# Všechny VERDICT klíče = True; α₀/τ₀ = −18/11 lock projde.
```

**Zdroje (ověřeno během výpočtu):** Chamseddine-Connes hep-th/9606001 (spektrální akce, master expanze); CCM hep-th/0610241; Marcolli „Spectral Action Gravity and Cosmological Models" / NCGCosmoCRP (master expanze + SM koeficienty α₀, τ₀, γ₀, 1/2κ₀² citováno verbatim); Gilkey/Vassilevich hep-th/0306138 (a₀, a₂ heat-kernel); Duff arXiv:2003.02688 (anomálie (a,c)); Pauli 1951 / Visser arXiv:1610.07264 / Akhmedov hep-th/0204048 (supertrace podmínky).
```
