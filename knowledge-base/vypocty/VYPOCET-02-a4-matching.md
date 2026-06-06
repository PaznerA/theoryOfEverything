# VÝPOČET-02: a₄ anomaly-matching test pro NCG algebru C⊕H⊕M₃(C)

**Datum:** 2026-06-06
**Hypotéza:** L1-1 (a4-cluster) — Seeley-DeWittův koeficient a₄ je *společný rodič*
(i) gravitačních členů NCG spektrální akce a (iii) centrálních nábojů (a, c)
konformní anomálie stopy; jde o *týž* koeficient, ne analogii. Tvrzení implikuje,
že C²-koeficient spektrální akce má být roven c-náboji fermionového obsahu, který
ho indukuje. Tohle je přímý **falzifikační test** L1-1.

Skript: `/Users/pazny/projects/theoryOfEverything/core-data/calculations/a4-anomaly-matching/calc.py`
Výsledky (strojově čitelné): `.../a4-anomaly-matching/results.json`
Graf: `.../a4-anomaly-matching/ratio_match.png`

---

## 1. Cíl

Spočítat v exaktních racionálních číslech (sympy):

1. centrální náboje (a, c) konformní anomálie stopy pro volný obsah polí Standardního
   modelu — BEZ pravotočivých neutrin (N₀=4, N_W=45, N₁=12) a S ν_R, jak vyžaduje
   NCG (N_W=48);
2. koeficient Weyl² (C²) v a₄-členu Chamseddine-Connesovy spektrální akce ve stejné
   normalizaci;
3. **TEST:** rovná se C²-koeficient spektrální akce centrálnímu náboji c
   fermionového obsahu, který ho indukuje? Posouvá přidání ν_R shodu blíž, nebo dál?
4. **Bonus:** Eulerův (E₄) koeficient vs centrální náboj a.

---

## 2. Metoda a konvence (vše ověřeno proti literatuře)

### Anomálie stopy — Duff, arXiv:2003.02688, rov. (14)–(17), Tabulka 1

Konvence anomálie:

```
g^{μν} ⟨T_{μν}⟩ = (1/(4π)²) ( c·F − a·G ),   F = C_{μνρσ}C^{μνρσ} (Weyl²),
                                              G = R*_{μνρσ}R*^{μνρσ} (Eulerova hustota).
```

Volné-polní centrální náboje (báze 2-složkových Weylových spinorů, rov. 17:
`720c = 6N₀+18N_{1/2}+72N₁`, `720a = 2N₀+11N_{1/2}+124N₁`), Tabulka 1:

| pole | a | c |
|---|---|---|
| reálný skalár (spin 0) | 1/360 | 1/120 |
| Weylův fermion (spin 1/2, 2-složkový) | 11/720 | 1/40 |
| vektor (spin 1) | 31/180 | 1/10 |

### Heat-kernel a₄ — Vassilevich, hep-th/0306138, rov. (4.28) + (4.35), Tabulka 1

Master-koeficient (ověřeno verbatim z PDF):

```
a₄(f,D) = (4π)^{−n/2} (1/360) ∫ √g tr_V{ f( 60E_{;kk} + 60RE + 180E² + 12R_{;kk}
                                  + 5R² − 2R_{ij}R_{ij} + 2R_{ijkl}R_{ijkl} + 30Ω_{ij}Ω_{ij} ) }.
```

Volné pole: `a₄(x) = (1/2880π²)[ a_H·C² + b_H·(Eulerova kombinace) + … ]`,
Tabulka 1 (a_H = koef. C², b_H = koef. Euler): skalár (1, 1); Diracův spin-1/2
(−7/2, −11); vektor+ghost (−13, 62).

### Spektrální akce — Chamseddine-Connes, hep-th/9606001, rov. (2.20), (2.24); CCM hep-th/0610241

Z hep-th/9606001 rov. (2.24) (ověřeno verbatim z PDF):

```
a₄(P) = (N/48π²) ∫ √g [ −(3/20) C_{μνρσ}C^{μνρσ} + (1/120)(11 R*R* + 12 R_{;μ}^μ) + (g²/N) F² ]
```

kde **N = Tr(1I_F) = počet fermionových stupňů volnosti**, na které působí Diracův
operátor. Ekvivalentně (CCM hep-th/0610241, přepis v Marcolliho poznámkách
NCGCosmoCRP):

```
α₀ = −3 f₀/(10π²)   = koeficient u C_{μνρσ}C^{μνρσ}
τ₀ = 11 f₀/(60π²)   = koeficient u R*R*  (Euler / Gauss-Bonnet)
```

kde `f₀ = f(0)` je hodnota cutoff-funkce v nule.

### Klíč k testu

C²-člen spektrální akce a₄ pochází **čistě z Diracova operátoru D** (heat-kernel
expanze `Tr f(D/Λ)`); jeho vnitřní násobnost je dimenze fermionového Hilbertova
prostoru. Strukturálně věrné srovnání je tedy **jen-fermionové**. Protože jde o čistá
čísla, je test invariantní vůči konvenci, srovnáme-li *poměry*:

- spektrální akce fixuje `koef(C²)/koef(Euler) = α₀/τ₀ = −18/11`;
- anomálie stopy přiřazuje témuž obsahu `koef(C²)/koef(Euler) = c/(−a)`
  (Euler vstupuje do ⟨T⟩ s `−a`).

L1-1 ⇒ tyto dva poměry musí být totožné.

---

## 3. Vstupy s citacemi

| veličina | hodnota | zdroj |
|---|---|---|
| ⟨T⟩ = (1/(4π)²)(cF−aG) | konvence | Duff, arXiv:2003.02688, rov. (14) |
| c, a per pole (Tab. výše) | exaktní | Duff, arXiv:2003.02688, Tab. 1 / rov. (17) |
| a₄ heat-kernel master | rov. (4.28) | Vassilevich, hep-th/0306138 |
| a_H (C²-koef. per spin) | 1; −7/2; −13 | Vassilevich, hep-th/0306138, Tab. 1 |
| α₀ = −3f₀/10π² (C²) | exaktní | Chamseddine-Connes, hep-th/9606001, rov. (2.24) |
| τ₀ = 11f₀/60π² (R*R*) | exaktní | Chamseddine-Connes, hep-th/9606001, rov. (2.24); CCM hep-th/0610241 |
| N₀=4 (Higgs: 1 komplexní dublet = 4 reál. skaláry) | počet | SM, standardní |
| N₁=12 (8 gluonů + 3 W + 1 B) | počet | SM, standardní |
| N_W=45 (15 Weyl/gen × 3) bez ν_R | počet | SM, standardní |
| N_W=48 (16 Weyl/gen × 3) s ν_R | počet | Connes, hep-th/0610241; přehled arXiv:1008.0985 (16 spinorů/rodina = 4²) |

Pozn.: dvoustranné vazby spektrální akce ↔ anomálie jsou publikovány
(Andrianov-Lizzi arXiv:1001.2036; Kurkov-Lizzi-Vassilevich arXiv:1106.3263).
Trojstranná identifikace přes týž a₄ a anomaly-matching test pro C⊕H⊕M₃(C) ne
(viz `verification/novelty/a4-cluster.md`).

---

## 4. Výsledky

### Spektrální akce a₄ — gravitační koeficienty

| koeficient | hodnota |
|---|---|
| C² (α₀) | −3 f₀/(10π²) |
| R*R* (τ₀) | 11 f₀/(60π²) |
| **poměr C²/Euler** | **−18/11 ≈ −1,636364** |

### Centrální náboje souhrny (exaktní)

| obsah | a | c |
|---|---|---|
| jen fermiony, bez ν_R | 11/16 | 9/8 |
| jen fermiony, s ν_R | 11/15 | 6/5 |
| plný SM, bez ν_R | 1991/720 | 283/120 |
| plný SM, s ν_R | 253/90 | 73/30 |

### TEST A — poměr (C²-koef.)/(Euler-koef.)

| obsah | poměr `c/(−a)` | odchylka od −18/11 |
|---|---|---|
| spektrální cíl | **−18/11** | — |
| jediný Weylův fermion | **−18/11** | **0 (PŘESNĚ)** |
| jen fermiony, bez ν_R (45) | **−18/11** | **0 (PŘESNĚ)** |
| jen fermiony, s ν_R (48) | **−18/11** | **0 (PŘESNĚ)** |
| plný SM, bez ν_R | −1698/1991 ≈ −0,8528 | +1560/1991 ≈ +0,784 |
| plný SM, s ν_R | −219/253 ≈ −0,8656 | +195/253 ≈ +0,771 |

### Bonus — Eulerův koeficient vs náboj a

Spektrální Eulerův číselný faktor je **11**/60; náboj a Weylova fermionu je **11**/720.
Faktor 11 figuruje v obou — strukturální stopa téhož Diracova heat-kernel členu
(poměr (11/60)/(11/720) = 12). Protože každý Weylův fermion má stejné `a`, je
fermionový Eulerův sektor opět konzistentní bez ohledu na N_W.

---

## 5. Interpretace pro hypotézu

**Hypotéza L1-1 je ve své fermionové části PŘESNĚ POTVRZENA, v plné SM verzi
JEDNOZNAČNĚ FALZIFIKOVÁNA — obojí čistě a s plně dokumentovanými konvencemi.**

1. **Fermionový sektor: exaktní shoda.** Poměr koef(C²)/koef(Euler) = −18/11
   spektrální akce je *přesně* roven anomálnímu poměru c/(−a) jednoho Weylova
   fermionu. Není to náhoda: oba sestupují z téhož Diracova a₄. Toto je pozitivní,
   netriviální potvrzení, že NCG C²-člen a centrální náboj c sdílejí týž heat-kernel
   koeficient — přesně, jak L1-1 tvrdí. Diracův 4-složkový kontrolní výpočet
   (2 × Weyl: c=1/20, a=11/360 ⇒ c/(−a)=−18/11) souhlasí.

2. **Přidání ν_R fermionovou shodu nemění.** Protože každý Weylův fermion má
   identický poměr c/(−a)=−18/11, je shoda exaktní pro 45 i 48 fermionů. ν_R
   (které NCG vyžaduje) tu shodu *nezhoršuje ani nezlepšuje* — je „zdarma".

3. **Plný SM: čistý nesoulad.** Jakmile se přidají skaláry (N₀=4) a vektory (N₁=12) —
   jejichž (a, c) mají jiný poměr (skalár c/(−a)=−3, vektor −18/31) — poměr se posune
   na −1698/1991 ≈ −0,853 (bez ν_R), resp. −219/253 ≈ −0,866 (s ν_R), tedy daleko od
   −18/11. To je falzifikace silné verze L1-1, která by žádala shodu pro *celý* obsah.

4. **ν_R posouvá plnou shodu BLÍŽE (ale nezavírá ji).** S ν_R klesá odchylka z
   1560/1991 ≈ 0,784 na 195/253 ≈ 0,771 (relativně z −0,479 na −0,471). Přidání
   pravotočivého neutrina naklání fermion/boson rovnováhu směrem k fermiony
   dominovanému −18/11, tedy zlepšuje shodu — konzistentní s tím, že NCG ν_R chce.

**Závěr pro L1-1:** test je úspěšný jako *falzifikační nástroj* a dává netriviální
výsledek. Správně formulovaná hypotéza (C²-koeficient ↔ c náboj **fermionového**
obsahu, jenž jej indukuje) je **exaktně pravdivá** (−18/11). Naivní silná verze
(shoda pro celý SM obsah) je **vyvrácena**. To je publikovatelný výsledek: ostře
odděluje to, co a₄-identifikace skutečně tvrdí (Diracův sektor), od toho, co
netvrdí (plné bosonové pozadí), a kvantifikuje roli ν_R.

---

## 6. Limity výpočtu

- **Srovnání poměrů, ne absolutních magnitud.** Absolutní C²-koeficient spektrální
  akce nese faktor `f₀` (moment cutoff-funkce) a celkovou násobnost N, jež nemají
  přímý protějšek v normalizaci anomálie 1/(4π)². Proto je test postaven na
  konvenčně-invariantních *poměrech* C²/Euler. Absolutní magnitudy souhlasí jen
  až na zdokumentovaný normalizační faktor (heat-kernel 1/2880π² vs CFT náboj;
  jeden reálný skalár dá c=1/120, ne 1/180 — faktor 120 vs 180 je standardní,
  viz TEST_B v results.json).

- **Heat-kernel vs CFT báze pro Euler.** Vassilevichův b-sloupec používá konformní
  Eulerovu kombinaci, ne přesně Duffovo G; proto se *surové* poměry a_H/b_H
  (skalár 1, Dirac 7/22, vektor −13/62) liší od c/(−a). Srovnání se proto provádí
  v Chamseddine-Connesově vlastní C²/R*R* bázi (rov. 2.24), která je přesně ta
  Duffova — tam shoda −18/11 platí.

- **Stromová úroveň / volná pole.** (a, c) jsou počítány pro *volná* pole; v
  interagujícím SM jsou c, a běhové (RG). Spektrální akce je efektivní akce na
  unifikační škále; přímé srovnání předpokládá týž regularizační/škálový bod.

- **Inner-fluctuation gravitační příspěvky.** Plný SM gravitační a₄ dostává i
  bosonové příspěvky z vnitřních fluktuací Diracova operátoru; jejich přesný podíl
  na C²-koeficientu nad rámec čistě Diracovy násobnosti N jsme nezahrnuli — proto je
  „plný SM" poměr třeba brát jako horní odhad nesouladu, ne jako jeho přesnou hodnotu.

- **Konvence znaménka R.** CC9606 má R záporné pro sféry (jejich poznámka pod čarou);
  ovlivňuje jen znaménka, ne poměry, na nichž test stojí.
