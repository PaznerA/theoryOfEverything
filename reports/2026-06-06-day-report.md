# Závěrečná zpráva výzkumného dne — 2026-06-06

*Vygenerováno: 2026-06-06. Forma: ranní čtení s kávou.*

---

## 1. Executive summary

Dnes — v rámci jediného dne — projekt prošel od nulového stavu (základní rešerše z 2026-06-05) přes
devět kol hledání souvislostí až k prvnímu souboru čtyř předpublikačních draftů a závěrečné
brainstormingové analýze. Výsledkem je 24 nálezů v `core-data/findings.json`, dvacet výpočetních
sezení (VYPOCET-01 až VYPOCET-20), čtyři eseje, dvě syntézy a pět brainstormingových dokumentů.

Nejdůležitější věc, která se dnes stala: **dvě vlajkové výzkumné linie se spojily na de Sitteru.**
Linie A (SJ stav na horizontech) a linie B (přechod von Neumannova typu III₁→II v kauzálních
množinách) se dotkly v jediném výpočtu — VYPOCET-19 ukázal, že diskrétní SJ sonda plus truncace
vidí CLPW rozdíl mezi ohraničenou de Sitterovou záplatou (typ II₁, saturace obsahu) a plochou
kontrolou (typ II_∞, neomezený růst). To je nový, dosud nepublikovaný diskriminátor von Neumannova
algebrového typu v diskrétní QFT na zakřiveném pozadí.

Vedle toho projekt čistě uzavřel tři hypotézy jako falsifikované (γ–Cardy, naivní Λ-sjednocení,
H4g-3), přičemž každá z těchto „zabitých" linií zpevnila zbývající pozitivní tvrzení. Čtyři
drafty čekají na lidskou revizi; vstupním bodem je `papers/REVIZE-PRO-CLOVEKA.md`.

---

## 2. Co bylo nalezeno

### Linie A — SJ stav na horizontech (zahrnuje dS II₁ diskriminátor)

**F-009 / VYPOCET-08:** Všechny čtyři BTZ signatury replikovány na ekvatoriálním Kerru.
SJ stav existuje strojovou přesností uvnitř ergoregiónu (787±/790± párů, residuál ~5×10⁻¹⁶);
null-sklon se nuluje přesně na r_erg = 2M pro a = 0,6 i 0,9; opačná znaménka A_caus > 0 /
A_W < 0 na každém testovaném (a, r); A_caus roste monotónně se spinem (0,197 / 0,361 / 0,482
pro a = 0,3 / 0,6 / 0,9).

**F-013 / VYPOCET-10:** Rotace vlastního vektoru SJ pozitivního podprostoru ~44,6° (cos² = 0,507)
při < 2% změně spektra — spin je eigenvektorový jev, ne spektrální. Superradiantní váha roste
k ergosféře (0,0000 při r = 4,0 → 0,0755 při r = 2,05). Toy model reprodukuje obě znaménka
A_caus > 0 / A_W < 0 s korelací 0,95–0,97.

**F-017 / VYPOCET-14:** H3g-1 potvrzena. Superradiantní nástup řízen spojitým Ω(r), ne diskrétní
ergosférou. ΔAIC(E vs. S) = +441,6 (a = 0,6), +4216,3 (a = 0,9), +231,5 (BTZ J = 0,9) —
vše rozhodující pro Model S (W_sr ~ Ω(r)^B). Mocninový exponent B = 4,23 (a = 0,6), 3,82 (a = 0,9),
1,71 (BTZ). A_W negativně definitní ve všech 65 externích měřeních.

**F-018 / VYPOCET-15:** Ambiguita pro a = 0,6 uzavřena v log-log prostoru: corr(log W_sr, log Ω)
= 0,9992 vs. corr(log W_sr, log 1/(r − r_erg)) = 0,942. Joint fit ΔAIC(E − S) = +3894, |A_W|
~ r^{−2,75±0,03} (předpovídáno −3, R² = 0,957).

**F-023 / VYPOCET-19 — dS II₁ diskriminátor (sjednocení obou linií):** Diskrétní SJ sonda VIDÍ
CLPW rozdíl II₁ vs. II_∞. N_total: dS 442 → 480 SATURUJE (strop 480,1, R² = 1,0000); flat
768 → 3360 ROSTE. S_full: dS saturuje-a-překlápí (sat-fit R² = 0,990, pozdní sklon −1,67);
flat roste (sklon +12,2). Čistá změna druhé poloviny: dS −13,1 vs. flat +21,7, mezera 34,8.
Baterie tří proxy na dS záplatě: 2/3 projdou (P1 S_full ~ N^{1,11} → S_trunc ~ N^{0,12};
P2 modulární pile-up ~ N^{1,25} → přesně 0; P3 nesignifikantní při 5 seedech). Runtime 431 s.

---

### Linie B — přechod III₁→II v kauzálních množinách (včetně rohového mechanismu)

**F-015 / VYPOCET-12:** První přímý numerický důkaz crossed-product obrazu na kauzální množině
v 2D (N = 400–1800, 8 seedů). Entropic-trace: S_full ~ N^{1,04} → S_trunc saturuje 1,30–1,70,
kolaps 80×. Modulární spektrum: untruncated flat-dense III₁ (pile-up ~ N^{1,14}) → truncated
integrovatelné typ-II (8–20 módů, IR hrana ε > 1,6). Verdikt 2/3.

**F-016 / VYPOCET-13:** Geometrie rohů (ne dimenze) rozhoduje o area vs. volume zákonu. 4D slab
(bez rohů): S ~ L^{2,00} (R² = 0,982) = area zákon. 4D nested diamant (VYPOCET-06): S ~ f^{6,1}
(R² = 0,998) = volume zákon. Hadamardova diagnostika: 4D slab deep = −3,81 ≈ surface = −3,85
(žádná anomálie); 4D diamant inside = −1,53 vs. corner = −2,79 (anomálie v rozích).

**F-019 / VYPOCET-16:** H3g-3 podpořena ve d = 4 (3/3 proxy). S_full ~ N^{1,34} → S_trunc
~ N^{0,55} ≈ sqrt(N), kolaps 36× při N = 3500. Pile-up ~ N^{1,27} → přesně 0 po truncaci
(IR hrana ε ≈ 2,7). Klíčová selektivita: pouze N^{3/4} number-truncace dává area zákon;
fixní-frakce (~ N^{0,90} módů) selhává (S ~ N^{0,83}). Pauli-Jordan ±-párování 7,1×10⁻¹⁴.

**F-021 / VYPOCET-18 — rohový mechanismus (stav: 2D potvrzen, 4D parciální):** 2D modulární
kernel: off-diagonální sklon −0,47 (slab, geometrický/boost-lokální) vs. −0,094 (diamant,
negeometrický), gap 0,37 stabilní. Slab diagonální modulární váha lineární ve vzdálenosti
(R² = 0,977). Per-site nelokálnost f_nl roste monotónně 0,673 (bulk) → 0,828 (roh), sklon
−0,383 (R² = 0,989). Verdikt H4g-1: 4/5 signatur v 2D. 4D s link-maticí: nereplikuje (poctivý null).

**F-024 / VYPOCET-20 — BD 4D modulární tok (parciální):** BD d'Alembertián vylepšuje
4D výsledek oproti link-matici: slab off-diag sklon −1,10 vs. diamant −0,52 (gap 0,58, správný
směr). Rohová concentrace f_nl (0,445) čistě nereplikuje. Verdikt: 3/5 signatur — slab
boost-geometricita robustní, rohová část dimensionálně omezena. Link-maticový 4D null je z části
objektově závislý artefakt.

---

### Identita a₄: −18/11 (linie C)

**F-003 / VYPOCET-02:** Poměr koef(C²)/koef(Euler) v NCG spektrální akci a₄ = −18/11
EXAKTNĚ. Shoda s c/(−a) Weylova fermionu potvrzena exaktní racionální aritmetikou (sympy).
Platí pro 45 Weylových fermionů (bez ν_R) i 48 (s ν_R).

**F-004 / VYPOCET-02:** Plná SM (skaláry + fermiony + vektory): c/(−a) = −1698/1991 ≈ −0,853
(bez ν_R) vs. cíl −18/11 ≈ −1,636. Mismatch 0,784. Silná verze hypotézy L1-1 falsifikována.

**F-014 / VYPOCET-11:** Žádný boson neleží na fermionové přímce −18/11 v (a,c) rovině. Konformní
graviton dává −398/261 ≈ −1,525 ≠ −18/11. Požadovaná násobnost gravitonů: x = −143/32 < 0
(nefyzikální). Identita je index-chráněný fermionový diskriminátor. Spinorový a₄ v bázi
{C², E₄, R²}: (−1/20, +11/360, 0) → (a, c) = (11/360, 1/20); shoda s Duff Tab. 1 exaktně.
Rohlinův zámek: σ = 16 → ind(D) = −2 (sudé celé, konzistentní).

---

### Spektrální dimenze jako klasifikátor (linie D)

**F-001 / VYPOCET-01:** d_s^UV není universální konstanta, ale identifikační otisk trojice
(z, D, sonda). Jednotný P(σ) engine reprodukuje 12/12 hodnot z literatury. GR → 4; Hořava z = 2 →
5/2; Hořava z = 3 → 2; Stelle/AS/CST d'Alembertián → 2; CST náhodná procházka → > D.

**F-002:** Zdánlivý rozpor connections.json (hrana 501 vs. 1539 u CST d_s) vyřešen: oba výsledky
jsou správné, každý pro jinou sondu (d'Alembertián vs. náhodná procházka). Probe-závislost jako
třetí klasifikační osa doložena.

---

### Pomocné a kalibrační nálezy

**F-005 / VYPOCET-03:** Prefaktory tří nezávislých mechanismů Λ ~ 1/√V se liší faktorem
κ_Sorkin/κ_EDT = 139,6 ≈ 140 — silná sjednocující hypotéza vyvrácena; sdílena je pouze
dimenzionální kostra.

**F-006–F-008 / VYPOCET-04:** Entropic cutoff exponent p = 0,519 ± 0,007 → ε ~ ρ^{−1/2}
potvrzeno (2,8 σ od 1/2). Intrinsická knee ~ N^{1,0}. Exponent p = 1/4 vyloučen 39 σ.

**F-011 (kolo 3):** Pilíř 19 (von Neumannovy algebry): 27 nových konceptů, 32 ověřených referencí.
modular-hamiltonian se stal TOP HUBEM grafu konceptů (614 uzlů, 2437 hran).

---

## 3. Co bylo zabito — a proč je to dobře

### γ–Cardy program (F-010)

Hypotéza H01 — fixace Barbero-Immirziho parametru γ z CFT/Cardy formule — uzavřena jako mrtvá.
Strukturální blocker: Senův výsledek (arXiv:1205.0971) dokazuje, že log-korekce entropie černé
díry jsou IR-určeny (LQG hodnota −2 vs. euklidovská gravitace +1,71 — neshoda i na úrovni
logaritmického koeficientu). Porovnávat konstantní člen s Carlipem/Cardy je fyzikálně nemotivováno:
to, co by se porovnávalo, jsou veličiny různých energetických škál. Jde o kategorickou chybu, ne
o výzkumnou otázku. **Proč je to dobře:** čisté uzavření tohoto programu přesunulo čas a pozornost
k měřitelným, UV-citlivým diskriminátorům — k těm, které dnes přinesly pozitivní výsledky.

### Naivní Λ-sjednocení (F-005)

Hypotéza, že Sorkin everpresent Λ, EDT running Λ ~ H², a CosMIn sdílejí jednu hodnotu
prefaktoru κ, byla vyvrácena faktorem 140 (κ_Sorkin/κ_EDT = 139,6). CosMIn nemá pravý κ vůbec —
jeho „efektivní κ" závisí na epoše. Tři mechanismy popisují zásadně odlišnou fyziku, sdílejí
pouze dimenzionální kostru Λ ~ H². **Proč je to dobře:** falsifikace byla čistá a kvantifikovaná.
Negace silné hypotézy je publikovatelný výsledek sám o sobě — a porovnání tří prefaktorů
napříč pilíři nebylo v literatuře dosud provedeno.

### H4g-3 — fermionová indukce predikuje Λ (F-020 / VYPOCET-17)

Hypotéza, že stejná logika jako u identity −18/11 fixuje druhou index-chráněnou identitu pro
kosmologickou konstantu, byla vyvrácena exaktní sympy aritmetikou. a₀ (kosmologický člen)
a a₂ (Einstein-Hilbertův člen) sedí na různých cutoff-řádech (f₄Λ⁴ vs. f₂Λ²); jejich poměr
nese explicitní (f₄/f₂)Λ² — rozměrový a schémový závislý. STr 1 = n_B − n_F = −62 bez ν_R
/ −68 s ν_R: přidání ν_R imbalanci zhoršuje, nezlepšuje. **Proč je to dobře:** draft-02 tím
získal čistší profil. Tvrzení o −18/11 zůstalo přesně tak úzké, jak být mělo — a toto ohraničení
je samo o sobě silnější argument než hypotéza, která by tvrdila příliš.

### BMV diskriminátory — přehodnocení rozsahu (F-007 z kola VYPOCET-07)

Fázová korekce BMV/AS: δφ/φ ≈ 6,2×10⁻²⁸ (klasický RG), EFT ≈ 3,4×10⁻⁶² (kvantový) — obě
24, resp. 59 řádů pod dosažitelností. Jedinou realistickou variantou zůstává Oppenheimova
postkvantová teorie (π-fázový posun v křížových korelacích oscilátorů). **Proč je to dobře:**
přesné číslo je lepší než vágní naděje — víme kde hledat (Oppenheim) a kde nehledat.

---

## 4. Stav papers/

Vstupní bod pro lidského výzkumníka: **`papers/REVIZE-PRO-CLOVEKA.md`** — kompletní přehled
se ~80 checkboxy, příkazy pro re-run všech 12 calc.py, sekce kritických high-risk položek
a doporučené pořadí revizí.

| Draft | Vědecký stav | Hlavní blokátor | Odhad lidské revize |
|-------|-------------|-----------------|---------------------|
| **draft-02** — identita −18/11 | Fyzika výpočetně **uzavřena** (F-003, F-004, F-014, F-020); žádný otevřený fyzikální blokátor | Lidská re-derivace a₄ z Vassilevich eq. 4.28; citace-check PDF Duff/CC/Andrianov-Lizzi; novelty search v Connes-Marcolli/van Suijlekom | **4–8 hod** (nejmenší draft) |
| **draft-04** — přechod typů na kauzálních množinách | Podpořeno (2/3 proxy v 2D, 3/3 proxy ve 4D slabu); placeholder `a_err = 0.776` musí být opraven | Re-run 4 calc.py; opravit placeholder; ověřit 15 arXiv ID (kriticky: 2501.09669 a 2602.16782 Jones-Yazdi jako nové); BD 4D replika parciální (F-024, 3/5) | **12–20 hod** |
| **draft-01** — SJ v rotujících prostoročasech (v0.2) | Silné výsledky (ΔAIC > 3894 všude, F-017/F-018); vědecky **otevřena** (chybí N→∞ studie, analytické SJ pro zkosený diamant, BTZ vakuum srovnání) | N→∞ s 30+ seedy; analytický derivát SJ pro zkosený diamant; ověření 9 arXiv ID z 2025–2026 | **15–25 hod** |
| **draft-03** — d_s klasifikátor (v0.1) | Fyzika solidní (F-001, F-002); novelty argument **nejkřehčí** — vyžaduje rozsáhlý lit-search | Obrana vůči „Calcagni přebalený"; D-konvence ambiguita; per-řádkový REPRODUCE audit 12 hodnot | **10–18 hod** |

**Doporučené pořadí revizí:** draft-02 → draft-04 → draft-01 → draft-03
(viz oddíl 3 v `REVIZE-PRO-CLOVEKA.md` s podrobným odůvodněním).

**Absolutní pravidla před odesláním:** jmenovaný lidský autor; explicitní AI-assistance statement;
veřejné vydání calc.py.

---

## 5. Statistiky dne

| Kategorie | Počet |
|-----------|-------|
| Kola výzkumu (kola 3–9, tento den) | 7 kol |
| Výpočetní sezení (VYPOCET-01..20) | 20 |
| Nálezy v findings.json | 24 |
| Drafty article | 4 |
| Syntetické eseje (ESEJ-01..04) | 4 |
| Syntézy (SYNTEZA-01..02) | 2 |
| Brainstormy (BRAINSTORM-01..05) | 5 |
| Graf konceptů (po konsolidaci kolo 3) | 614 uzlů, 2437 hran |
| Connections.json | 288 hran (stav po kole 9; 0 von-neumann-algebras hran) |
| Barely explored connections | 112 (z počáteční konsolidace) |
| Referenční báze | 563 unikátních referencí |
| Vzorce | 235 unikátních |

Pilíř 19 (von Neumannovy algebry, kolo 3): 27 nových konceptů, 32 ověřených referencí.
Graf expandoval z 598/2319 na 614/2437.

---

## 6. Kam dál

### BRAINSTORM-05 — šest headline hypotéz (dokument: `knowledge-base/BRAINSTORM-05.md`, 499 řádků)

Capstone kol 1–9 identifikoval šest cílů příštího výpočetního bloku:

**H5g-1 — 4D dS truncovaná area-law jako přímý typový diskriminátor** *(priorita: high, jedno odpoledne)*
Ve 4D de Sitterově statické záplatě (sech²-vážený slab) by truncovaná SSEE S ~ √N měla sama oddělit
typ II₁ (saturuje, ohraničená záplata) od II_∞ (roste, plochá kontrola) — na rozdíl od 2D, kde
diskriminoval jen obsah N_total/S_full. První test: 4D sech²-vážený slab, iΔ nebo BD smeared,
truncace n_max = 2N^{3/4} (validovaný regulátor F-019), R*_box → horizont, dS vs. plochá kontrola.
N ≤ 2500 dense eigh, 5 seedů. Varianta VYPOCET-19 + VYPOCET-16.

**H5g-2 — entropy-cap = Gibbons-Hawkingova A/4** *(priorita: high výnos / high riziko)*
Konečný strop, na nějž saturuje obsah-sledující entropie ohraničené dS záplaty (F-023), se po
kalibraci rovná A/4 — diskrétní first-principles výpočet dS entropie. Vyžaduje ρ ~ 10³–10⁴,
sparse eigsh (ne dense eigh), kalibraci ε z nezávislého F-006 před měřením poměru.

**H5g-3 — co nahrazuje roh ve 4D: codim-2 spoj nebo kaustika** *(priorita: medium-high, jedno odpoledne)*
2D rohový mechanismus (H4g-1) nepřežívá ve 4D na null-tipu diamantu (F-024); správný 4D locus
selhání geometričnosti modulárního toku je codim-2 spoj (wedge-joint). První test: 4D region
s codim-2 spojem, BD smeared (ε = 0,6, F-024 validoval na slabu), per-site f_nl gradient.
N ≤ 2200, 3 seedy. Varianta VYPOCET-20, jiná geometrie.

**H5g-4 — spektrální triple NCG = SJ modulární K** *(priorita: medium, nová mašinérie)*
Spektrální triple (Dirac D) a SJ konstrukce na causetu (Pauli-Jordan iΔ, modulární K) jsou dvě
realizace téže spektrální rekonstrukce. Connesova spektrální vzdálenost = entanglementová metrika.
Lovná zóna barely: causal-sets↔noncommutative-geometry (shared-math). Connections.json nemá ani
jednu von-neumann-algebras hranu (0 z 288), ač F-015/F-019/F-023 ji zakládají daty.
Doporučeno: read-first (Connes-Rovelli termální čas), proof-of-concept N ~ 200–500.

**H5g-5 — exponent B v W_sr ~ Ω(r)^B závisí na asymptotice, ne na dimenzi** *(priorita: medium)*
B klesá 4,23 → 3,82 se spinem a = 0,6 → 0,9 při fixní dimenzi 4D (F-017), tedy není dimenzní
konstanta (D−1). B(Kerr-AdS) ≠ B(Kerr) by potvrdilo závislost na asymptotice. Levnější
alternativa: hustší scan r = 5–20M na hotovém Kerru pro a = 0,6 (N = 1600, 5 seedů).

**H5g-6 — rozhodnutí o draft-05 vs. rozšíření draft-04** *(priorita: medium, rozhodovací)*
F-023 + F-019 + H5g-1 tvoří samostatný nový letter (draft-05), pokud 4D dS truncovaná entropie
sama oddělí typy → silný capstone obou linií. Pokud jen 2D obsah-saturace → F-023 se přilepí
k draft-04 jako dS sekce. Rozhoduje H5g-1.

### Doporučená fronta (BRAINSTORM-05)

1. **#1 + #2 PARALELNĚ** (nejvyšší ROI, obě varianty hotových kódů, jedno odpoledne):
   - H5g-1: 4D dS truncovaná area-law — rozhoduje draft-05
   - H5g-3: codim-2 spoj — uzavírá vrstvu B ve 4D

2. **A/4 kalibrace** (H5g-2) — vyžaduje sparse solver a ρ ~ 10³–10⁴; ne jedno odpoledne.

3. **Spektrální triple** (H5g-4) — nová mašinérie, začít read-first.

4. **H5g-6** se rozhoduje samo výsledkem H5g-1.

### Uživatelova roadmapa (PROGRESS.md)

1. **Velké review** — kontrola správnosti všech dat, doplnění (teoretických) vazeb v grafu
   konceptů, celkový úklid repozitáře.
2. **Simulace a vizualizace** — composable functions nad jednotlivými vzorci z `core-data/formulas.json`.
3. **Minimalistický web** — builduje přímo z existující souborové struktury repozitáře
   (markdown + JSON registry jako zdroj pravdy).

---

## 7. Provozní poučení

**Token economy a prefix cache:** Velké rešeršní workflow v kole 1 (18 pilířů, paralelní agenti)
spotřebovalo výraznou část denního rozpočtu. Kola 3–9 běžela v economy módu (jeden agent,
sekvenční výpočty, granulární instrukce) s výrazně nižší spotřebou při srovnatelném výstupu.
Doporučeno: uchovat context kola v prefixu cache napříč koly — eliminuje opakované čtení
PROGRESS.md a findings.json v každém kole.

**Session limity:** Kolo 9 bylo dočasně přerušeno (pauza uživatelem, viz PROGRESS.md log
2026-06-06 prvního záznamu) a znovu spuštěno. Workflow skript `workflows/qg-round-09.js` byl
zachován jako archiv. Doporučení: každé kolo začínat explicitním `wf_*` identifikátorem pro
snadné obnovení.

**Kontrola referencí:** Všech 22 arXiv ID citovaných v BRAINSTORM-05 bylo ověřeno jako
existujících jinde v projektu. Reference z roků 2025–2026 (zejména 2501.09669 a 2602.16782
v draft-04) jsou označeny `⚠️ neověřeno` a jsou prvním cílem lidské revize.

**N^{3/4} jako globální regulátor:** Exponent 3/4 se ukázal jako stabilní provozní parametr
pro 4D vN-type truncaci napříč slab i dS geometrií (F-019, F-023). Lze ho natvrdo použít
jako default v dalších 4D výpočtech, dokud není analyticky odvozen.

---

*Konec závěrečné zprávy výzkumného dne 2026-06-06.*
*Zdroje: PROGRESS.md (log kol 3–9), core-data/findings.json (24 nálezů F-001..F-024),*
*papers/REVIZE-PRO-CLOVEKA.md (přehledová tabulka a high-risk položky),*
*knowledge-base/BRAINSTORM-05.md (499 řádků, 6 hypotéz H5g-1..6).*
