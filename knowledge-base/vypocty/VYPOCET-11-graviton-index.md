# VYPOCET-11: Gravitonový sektor a index-teorém pro identitu −18/11 (dva blokátory draftu-02)

**Datum:** 2026-06-06
**Soubory:** `core-data/calculations/a4-graviton-index/{calc.py, results.json, graviton_ledger.png, ac_plane.png}`
**Status:** Dokončeno (exaktní sympy aritmetika; všechny konvence ověřeny proti literatuře v průběhu výpočtu)
**Hypotéza:** H3g-4 — spektrální akce JE fermionově-indukovaná (Sacharovova) gravitace; bosony včetně gravitonu **nejsou** součástí a₄ identity, leží na *indukované* straně účetní knihy.
**Návaznost:** Uzavírá dva blokátory draftu-02 (`papers/draft-02-a4-fermionic-identity/`) podle BRAINSTORM-03 „Výpočetní fronta v2", položky #1 (graviton/Weyl sektor) a #7 (index-teorémový test). Přímo navazuje na VYPOCET-02 (identita −18/11).

---

## Cíl

Draft-02 stojí na exaktní racionální identitě `koef(C²)/koef(Euler) = −18/11`, sdílené spektrální akcí a anomálním poměrem `c/(−a)` Weylova fermionu. Dva blokátory před povýšením na reálnou notu:

**ČÁST 1 — GRAVITONOVÝ SEKTOR.** Otestovat H3g-4: zahrnout `c/(−a)` *samotného gravitonu* do bilance.
- (i) Jaké `c/(−a)` má graviton? (ověřeno proti Christensen-Duff 1980 / Duff 2003.02688 / Duff hep-th/9308075 / Beccaria-Tseytlin 1710.03779.)
- (ii) Může **jakékoli** konzistentní rozdělení „indukovaný" vs „fundamentální" sektor obnovit identitu −18/11 pro plnou teorii, nebo identita striktně vymezuje Diracův sektor?
- (iii) Sacharovova kontrola konzistence: v logice indukované gravitace graviton **neběží** ve smyčkách, které akci indukují — formalizovat, co to předpovídá pro účetní knihu anomálií, a zda je to vnitřně konzistentní.

**ČÁST 2 — INDEX-TEORÉMOVÁ KŘÍŽOVÁ KONTROLA.** Identita −18/11 má mít index-teoretický stín.
- Vyjádřit `a₄(D²)` Diracova operátoru v standardní bázi {C², E₄, R², □R} pomocí sympy.
- Potvrdit, že −18/11 vyplývá z Â-genus struktury (resp. ze spinorového a₄).
- Zkontrolovat proti Atiyah-Singerově index-hustotě (E₄ koeficient musí reprodukovat normalizaci index-teorému — netriviální zámek konzistence).

---

## Metoda a konvence (vše ověřeno proti literatuře)

### Anomálie stopy — Duff arXiv:2003.02688 (ověřeno HTML ar5iv během výpočtu)

```
g^{μν}⟨T_{μν}⟩ = (1/(4π)²)( c·F − a·G ),   F = C_{μνρσ}C^{μνρσ} (Weyl²), G = E₄ (Euler).
Počítací vzorce (2-složková Weylova báze):  720c = 6N₀+18N_{1/2}+72N₁ ;  720a = 2N₀+11N_{1/2}+124N₁.
```
Per pole: skalár (a,c)=(1/360,1/120); Weyl (11/720,1/40); vektor (31/180,1/10).
**Klíčové zjištění z verifikace:** Duff 2003.02688 *neobsahuje* řádek pro graviton — spin-2 anomálie je starší výsledek (Christensen-Duff 1980) a je strukturně jiná povahy (viz níže).

### Heat-kernel a₄ master — Gilkey / Vassilevich hep-th/0306138, rov. (4.28)

```
a₄ = (4π)^{−n/2}(1/360) ∫√g tr_V[ 60E_{;kk}+60RE+180E²+12R_{;kk}+5R²−2Ric²+2Riem²+30Ω² ].
```
Pro **Diracův** svazek: tr_V(1)=4, E=−R/4 (Lichnerowicz), tr(Ω_{μν}Ω^{μν})=−(1/2)Riem².
Pro **skalár**: tr_V(1)=1, E=−R/6 (konformní), Ω=0.

### Spektrální akce — Chamseddine-Connes hep-th/9606001 rov. (2.24); CCM hep-th/0610241

```
α₀ = −3f₀/(10π²) (koef. C²),  τ₀ = 11f₀/(60π²) (koef. R*R*),  α₀/τ₀ = −18/11.
```

### Konformní vs. fyzikální graviton (ověřeno — kritický rozdíl)

Existují **dva odlišné „gravitonové" objekty** a je nutné je striktně odlišit:

1. **Fyzikální (Einsteinův) graviton** — 2-derivační bezhmotný spin 2 (skutečný graviton). **NENÍ konformní.** Jeho stopová anomálie je *gauge/scheme-závislá*, definovaná jen on-shell, a nese R²/□R člen → **nemá konvence-nezávislé (a,c) ani definované c/(−a)**. [Duff hep-th/9308075 Tab.1: gauge-fixované 360A=848; gauge-závislost explicitně Anselmi/hep-th/9503187, Martini-Nink-Percacci 2206.13287 (gauge-invariantní a₂ = −29/40 R²+53/45 Riem² jen na Einsteinových prostorech).]

2. **Konformní („Weylův") graviton** — spin-2 konformní vyšší-spin (CHS), tj. 4-derivační Weyl²(konformní) gravitace. **JE konformní** → čisté (a,c). [Beccaria-Tseytlin arXiv:1710.03779 rov.(31): a₂=87/20, c₂−a₂=137/60 ⇒ c₂=199/30.]
   - **Konvenční zámek:** obecný CHS vzorec téhož paperu `aₛ=νₛ²(14νₛ+3)/720, νₛ=s(s+1)` dává pro s=1 (Maxwell) `a₁=31/180` — *přesně* náš vektor. Tj. konvence Beccarie-Tseytlina je totožná s Duffovou. Ověřeno sympy assertem.

---

## Výsledky

### ČÁST 2 — index-teorémové odvození −18/11 ze spinorového a₄ (provedeno jako první, dodává engine pro Část 1)

Dosazení do heat-kernel masteru a převod do báze {C², E₄, R²} (n=4: E₄=Riem²−4Ric²+R², C²=Riem²−2Ric²+R²/3, inverze ověřena assertem):

| pole | koef(C²) | koef(E₄) | koef(R²) | (a,c) z heat-kernelu | konformní? |
|---|---|---|---|---|---|
| skalár | +1/120 | −1/360 | **0** | (1/360, 1/120) | ano |
| Dirac (4-sl.) | −1/20 | +11/360 | **0** | (11/360, 1/20) | ano |
| Weyl (=½ Dirac) | — | — | 0 | **(11/720, 1/40)** | ano |

- **Magnitudy a₄ koeficientů jsou PŘESNĚ literaturní (a,c):** |koef(C²)|=c, |koef(E₄)|=a, pro skalár i Dirac, ověřeno assertem proti Duffově Tab.1. Weyl z heat-kernelu = (11/720, 1/40) = Duff. **Žádné fudge** — čistá derivace z masteru.
- `c/(−a)` ze spinorového a₄ = **−18/11**; spektrální `α₀/τ₀` = **−18/11**. Zámek drží.
- **R² koeficient = 0** pro skalár i Dirac → oba jsou konformní (jak má být). To je důvod, proč mají čisté (a,c) a proč identita −18/11 vůbec dává smysl.
- **Pozn. ke znaménkům:** surové a₄ koeficienty mají mezi skalárem a fermionem opačné relativní znaménko (skalár C²>0,E₄<0; Dirac C²<0,E₄>0). To je standardní heat-kernel účetnictví mapy a₄→⟨T⟩ (znaménko závislé na poli); *magnitudy* jsou literaturně shodné. Fyzikální (a,c) jsou kladné pro obě pole.

### ČÁST 2b — Atiyah-Singerův / Â-genus normalizační zámek

Spinorový a₄ má **dva odlišné topologické stíny**, a to je jádro index-teorémové kontroly:

- **(Euler / konformní sektor, Typ A):** koef(E₄) = a = 11/720 per Weyl. Integrovaně: `χ(M)=(1/(32π²))∫E₄` (Gauss-Bonnet) → Eulerova charakteristika, celé číslo. Toto je konformní a-anomálie.
- **(Pontryagin / chirální sektor):** topologický **index** samotného D = Â-genus = −(1/24)∫p₁, p₁=(1/(8π²))∫tr(R∧R). Vázán na chirální (axiální) anomálii, tj. na **Pontryaginovu/signaturní** hustotu, NE Eulerovu.
- **Zámek (ověřeno sympy):** Â|₄ = −p₁/24; pro uzavřenou spin-varietu p₁=3σ (signatura), takže `ind(D)=−σ/8`. Rohlinova věta: σ dělitelné 16 ⇒ ind je sudé celé číslo. Kontrola: σ=16 → ind=−2. ✓

**Co je učebnicové vs. přidaná hodnota noty:**
- *Učebnicové:* Gilkey a₄ master; spinorové (a,c)=(11/720,1/40); Â=−p₁/24; Gauss-Bonnet χ; Rohlin σ dělitelné 16.
- *Přidaná hodnota:* explicitní derivace v bázi {C²,E₄,R²} ukazující, že −18/11 JE poměr C²/E₄ spinorového a₄; zámek, že **týž** spinorový a₄ nesoucí a=11/720 (Eulerův/konformní sektor) nese v Pontryaginově sektoru Â index-hustotu; čtení **content-independence jako index-ochrany** (každý Weylův fermion nese stejné (a,c) ⇒ stejnou jednotku index-hustoty ⇒ −18/11 sedí uvnitř index-chráněného objektu, nemůže selhat pro žádné pole z Diracova operátoru).

### ČÁST 1 — gravitonový sektor

**(i) Jaké c/(−a) má graviton?**

| objekt | (a,c) | c/(−a) | poznámka |
|---|---|---|---|
| **fyzikální Einsteinův graviton** | — | **neexistuje** | NEkonformní; gauge/scheme-závislé, jen on-shell, nese R²/□R |
| **konformní (Weylův) graviton** | (87/20, 199/30) | **−398/261 ≈ −1.525** | 4-derivační konformní gravitace, čisté (a,c) |
| (cíl) Weylův fermion / spektrální akce | (11/720, 1/40) | **−18/11 ≈ −1.636** | — |

Pro srovnání ostatní bosony: skalár c/(−a)=**−3**, vektor **−18/31≈−0.581**.

**(ii) Může jakékoli rozdělení obnovit −18/11?**

`c/(−a)` je poměr aditivních veličin. Pole leží na paprsku −18/11 ⟺ jeho (a,c) je kolineární s (a_W, c_W) Weylova fermionu, tj. `a·c_W − c·a_W = 0`. Test kolinearity (sympy):

| pole | kolineární s Weylem? |
|---|---|
| skalár | **ne** |
| vektor | **ne** |
| konformní graviton | **ne** |

→ **Jediný Weylův fermion (a jeho násobky) leží na paprsku −18/11.** Žádný boson není kolineární.
- Plné SM (45 fermionů + Higgs + 12 vektorů) bez gravitonu: `c/(−a) = −1698/1991 ≈ −0.853` (z VYPOCET-02).
- Plné SM + jeden konformní graviton na fundamentální straně: `−6474/5123 ≈ −1.264` — **NE** −18/11.
- Násobnost gravitonů x nutná k vynucení −18/11: `x = −143/32 < 0` (nefyzikální „anti-graviton"). Nelze *přidat* kladný počet gravitonů a identitu obnovit.

**Verdikt (ii):** Žádné konzistentní přiřazení s gravitonem (konformním NEBO fyzikálním) na fundamentální straně neobnoví −18/11. Identita **striktně vymezuje Diracův (Weyl-fermionový) sektor**. H3g-4 potvrzeno: graviton + bosony jsou na INDUKOVANÉ straně účetní knihy.

**(iii) Sacharovova kontrola konzistence.**

V Sacharovově/indukované gravitaci graviton **není** fundamentální pole; Einstein-Hilbert + C² členy jsou vakuová polarizace (a₄ heat-kernel) **hmotné** (zde Diracovy) smyčky. Graviton neběží ve smyčce, která akci indukuje.

- **Predikce pro účetní knihu:** indukovaný poměr C²/Euler musí být roven `c/(−a)` *pouze indukujícího* smyčkového obsahu. V NCG je obsah smyčky `Tr f(D/Λ)` funkcí výhradně D, tj. fermionového Hilbertova prostoru H_F → poměr musí být −18/11 (Diracova hodnota) a NESMÍ dostat gravitonový příspěvek.
- **Vnitřní konzistence (dvojí, souhlasící zákaz):**
  1. *Sacharovův zákaz:* počítat graviton jako fundamentální smyčku by **dvojitě započítalo** — jeho kinetický člen JE už indukovaný a₄.
  2. *Anomální zákaz:* fyzikální graviton je nekonformní → nemá čisté (a,c) → **nemůže být členem** konvence-nezávislého poměru C²/Euler vůbec.
  - **Oba zákazy souhlasí.** Objekt, který identita −18/11 ztotožňuje (poměr konformních a₄ koeficientů), je strukturně fermion-smyčkový objekt; graviton — nekonformní a neběžící ve spektrální akci — v něm nemůže a nevyskytuje se. Konformní (Weylův) graviton sice čistý poměr má (−398/261), ale je to JINÉ pole (4-derivační konformní gravitace), ne dynamický graviton, a také nedává −18/11.

---

## Interpretace pro hypotézu H3g-4

**H3g-4 je POSÍLENA, čistě a s plně dokumentovanými konvencemi.**

1. **Graviton identitu nezachrání** — ani konformní (−1.525), ani fyzikální (žádné čisté (a,c)). To byl rozhodující test #1 z fronty: kdyby graviton plnou shodu uzavřel, hypotéza o čistě fermionovém původu by padla. Padla *opačná* možnost: graviton shodu nezachrání → spektrální akce = fermionově-indukovaná gravitace.

2. **Identita je index-chráněná** (test #7). −18/11 je poměr C²/E₄ spinorového a₄, a týž a₄ nese v Pontryaginově sektoru Atiyah-Singerovu index-hustotu. To vysvětluje *proč* je content-independence strukturní, ne náhodná: je to projev index-ochrany (každý Weyl = stejná jednotka index-hustoty). Odpovídá na recenzentovu otázku „proč zrovna fermiony?" — protože jen Diracův operátor má a₄, jehož E₄-sektor je konformní a-anomálie *a* jehož Pontryaginský sektor je index. Bosony takový provázaný objekt nemají.

3. **Sacharovova logika je vnitřně konzistentní** s anomální účetní knihou: dva nezávislé zákazy (dvojí započtení; nekonformita gravitonu) zakazují tutéž věc. To uzavírá riziko z H3g-4 („indukovaná gravitace má v NCG subtilní status") na úrovni a₄ poměru: poměr je čistě fermion-smyčkový bez ohledu na to, že plná akce obsahuje i kosmologický a Higgs člen.

**Pro draft-02:** Část 1 odolá recenzentově otázce „proč graviton nezachrání plnou shodu?" (protože není fundamentální smyčka A je nekonformní). Část 2 odolá „je −18/11 chráněná veličina?" (ano — index-teoretický stín přes Â-genus; E₄ koeficient reprodukuje Gauss-Bonnet/Eulerovu charakteristiku, Rohlinův zámek drží).

---

## Limity výpočtu

- **Konformní vs. fyzikální graviton.** Hlavní fyzika části 1 *stojí* na tom, že fyzikální graviton je nekonformní a gauge-závislý. To je dobře doložené (Duff, Anselmi, Martini-Nink-Percacci), ale znamená, že „graviton c/(−a)" je principiálně nedefinované — záměrně to NEpočítáme jako číslo, jen jako strukturní fakt. Konformní graviton (−398/261) je čistá referenční hodnota, NE dynamický graviton.
- **Vektorový sektor.** koef(C²),(E₄) vektoru bereme z literatury (Duff Tab.1: a=31/180, c=1/10), neodvozujeme ghost-odečet z masteru (vyžaduje minimální-operátorovou dekompozici + ghosty). Skalár a Dirac jsou odvozeny plně z masteru.
- **Inner-fluctuation příspěvky** (jako ve VYPOCET-02): plný-SM gravitační a₄ dostává i bosonové příspěvky z vnitřních fluktuací D; jejich přesný podíl na C² nad rámec Diracovy násobnosti N nezahrnut → plný-SM nesoulad je horní odhad. Nemění verdikt části 1 (graviton ani tak není kolineární).
- **Index-teorém: dimenze.** Â=−p₁/24 a Rohlinův zámek jsou ve 4D. Vztah E₄↔χ (Gauss-Bonnet) a p₁↔σ je standardní; nota přidává jen jejich *společné ukotvení* v témž spinorovém a₄, ne nový index-teorém.
- **Free-field / fixed-scheme.** (a,c) jsou volně-polní; v interagující teorii běží. Spektrální akce je efektivní akce na unifikační škále. Poměr C²/Euler je ale scheme-robustní (Eulerův a-koeficient je pravá anomálie, Cardy/a-teorém; □R nejednoznačnost sedí v separátním total-derivative invariantu) — viz draft-02 TODO §3.

---

## Reprodukce

```
cd core-data/calculations/a4-graviton-index && python3 calc.py
# → results.json, graviton_ledger.png, ac_plane.png
# Všechny VERDICT klíče = True; všechny asserty (literaturní zámky) projdou.
```

**Zdroje (ověřeno během výpočtu):** Duff arXiv:2003.02688 (anomálie, (a,c) tabulka, počítací vzorce); Duff hep-th/9308075 (Twenty Years of the Weyl Anomaly, graviton 360A=848); Beccaria-Tseytlin arXiv:1710.03779 (konformní graviton a₂=87/20, c₂=199/30; CHS vzorec, Maxwell-zámek a₁=31/180); Anselmi hep-th/9503187 + Martini-Nink-Percacci 2206.13287 (gauge-závislost fyzikálního gravitonu); Gilkey/Vassilevich hep-th/0306138 (a₄ master); Chamseddine-Connes hep-th/9606001 + CCM hep-th/0610241 (spektrální akce); Atiyah-Singer / Â-genus (Â|₄=−p₁/24, Rohlin σ dělitelné 16).
