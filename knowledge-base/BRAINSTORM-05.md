# Brainstorming 05 — capstone kol 1–9 (2026-06-06)

> **Status oproti BRAINSTORM-04:** čtvrté kolo dalo *jednotící nit* tři datové opory a algebraický
> jazyk (modular-hamiltonian TOP HUB). **Páté kolo** doběhlo VYPOCET-16…20 a poprvé **sjednotilo obě
> vlajkové linie**: VYPOCET-19 ukázal, že diskrétní SJ sonda + truncace **VIDÍ** CLPW rozdíl typu
> II₁ (ohraničená dS statická záplata, konečná stopa) vs. II_∞ (neohraničený plochý kontrol) —
> obsah-sledující veličiny saturují na dS, rostou na ploché kontrole (mezera net-změny 34,8,
> opačná znaménka). Linie A (SJ × horizonty) a linie B (III₁→II přechod) se potkaly na de Sitteru.
> Zároveň VYPOCET-20 **uzavřel diagnózu** rohového mechanismu: H4g-1 rohová podčást není artefakt
> link-matice (BD objekt ji neobnovil) — je to **reálná dimenzionální vlastnost**, vrstva B se štěpí
> na slab-podčást (4D-robustní) a roh-podčást (jen 2D). Tohle kolo je **capstone**: konsoliduje,
> kam program po devíti kolech došel, a definuje frontu pro velkou lidskou revizi.

---

## 1. Stav programu — kam se obě vlajkové linie sběhly

Devět kol vykrystalizovalo program do **dvou vlajkových linií, které se v kolech 8–9 protnuly na
de Sitteru**, plus betonové NCG identity stojící stranou jako index-chráněné jádro. Poctivé shrnutí:

### Linie A — SJ stavy × horizonty (kauzální množiny × semiklasika)

**Stav: ✓✓ robustní, draft-01 v0.2.** SJ stav existuje na strojové přesnosti uvnitř ergoregionů
napříč geometriemi (BTZ 2D, Kerr 4D ekvatoriální; ±-párování ~5e-16) [F-009]. Frame-dragging se
otiskuje **eigenvektorově** (~44,6° rotace podprostoru, cos²=0,507), ne spektrálně (<2 %) [F-013].
Superradiantní onset je řízen **lokálním ZAMO polem Ω(r)**, ne ergosférou jako prahem: Model S
(W_sr~Ω^B) decisivně poráží model vzdálenosti od ergosféry, ΔAIC +442/+4216/+231 (Kerr a=0,6/0,9,
BTZ J=0,9), v log-log prostoru corr=0,9992 vs. 0,942 [F-017, F-018]. A_W záporně-definitní v
65/65 měřeních; opačná znaménka A_caus>0/A_W<0 odvozena z prvních principů (toy-model korelace
0,95–0,97) [F-013].

### Linie B — III₁→II typový přechod (kauzální množiny × von Neumann)

**Stav: ✓ robustní 2D, ✓ podpořeno 4D (slab), draft-04 v0.1.** SSEE truncace nese signaturu
přechodu od bezstopové (III₁) k semifinitní (II) algebře: 2D diamant 2/3 proxy (80× kolaps stopy,
modulární spektrum flat-dense→integrabilní s IR hranou) [F-015]; 4D slab 3/3 proxy (36× kolaps,
IR hrana ε≈2,7, **N^(3/4) rank je operativní regulátor** — fixní-frakční cutoff selhává) [F-019].
Typ žije ve **stavu/entropii**, ne v kinematice (PJ nukleární norma typ nenese) [F-015]. Klíčově:
N^(3/4) **není** spektrální rys — slab nemá ostré koleno — je to **předpis** (observer/crossed-product
cutoff) [F-019].

### Sjednocení A×B na de Sitteru (VYPOCET-19, nejčerstvější výsledek)

**Stav: ✓ podpořeno, F-023.** Toto je capstone kola 8–9. Konformní trik (2D bezhmotný skalár
konformně invariantní → SJ plochá v želvích souřadnicích r*=ℓ arctanh(r/ℓ), horizont vstupuje jen
přes sech²(r*/ℓ) vlastní míru sprinklingu) udělal **ohraničenou** (typ II₁) geometrii diskrétně
dostupnou. Výsledek: obsah-sledující veličiny **SATURUJÍ** na dS (N_total 442→480 strop R²=1,0000;
S_full saturuje-a-překlápí) vs. **ROSTOU** na ploché kontrole (768→3360; S_full +21,7). Net-změna
S_full přes druhou polovinu sweepu: dS −13,1 vs. plochá +21,7, **mezera 34,8, opačná znaménka =
DISKRIMINOVÁNO** [F-023]. Diskrétní SJ sonda tedy SEES CLPW distinkci II₁ vs. II_∞, kterou
analyticky předpověděli (arXiv:2206.10780). Linie A (SJ na horizontu) a linie B (typový přechod)
jsou na de Sitteru tatáž věc.

### NCG identita — index-chráněné jádro stranou obou linií

**Stav: ✓✓ vědecky uzavřeno, draft-02.** Poměr Weyl²/Euler v Chamseddine-Connes a₄ je **přesně
−18/11**, shodný s c/(−a) Weylova fermionu; graviton identitu nezachrání na žádné násobnosti
(konformní graviton −398/261, nutná násobnost x=−143/32<0); identita index-chráněná
(Atiyah-Singer Â, Rohlinův zámek σ=16→ind=−2) [F-003, F-014]. Plná-SM verze falzifikována
(−1698/1991) [F-004]. Λ-sektor NEMÁ sesterskou identitu (a₀/a₂ cross-order, scheme-závislé;
H4g-3 falzifikováno) [F-020]. Toto je **otázko-nezávislé jádro** — protipól relační nitě.

### Co je mrtvé (NEvzkřísit bez nového mechanismu)

γ-Cardy (Sen IR-univerzalita) [F-010]; naivní Λ~1/√V (κ_Sorkin/κ_EDT=139,6) [F-005]; H4g-3 druhá
index-identita pro Λ [F-020]; spojité BMV diskriminátory (24–72 řádů pod dosahem). **Filtr je
kalibrovaný devíti koly:** co přežilo, přežilo opakované pokusy o popravu.

### Jednotící nit po kole 9 — kde se posunula

Through-line "vlastnosti = odpovědi na otázky" (vrstvy A relační/QRF, B modulární, C
index/anomálie jako otázko-nezávislé jádro) prošla **rozhodujícím testem vrstvy B** ve VYPOCET-18/20:

- **Vrstva B se štěpí na dvě dimenzionálně různé podčásti** [F-021, F-024]. **Slab-podčást**
  ("modulární tok = geometrický boost na klínu") je **4D-robustní**: BD objekt ji ve 4D ostře
  potvrzuje (off-diag sklon −1,10 vs. diamant −0,52, gap 0,58; diagonální boost-linearita R²=0,77),
  což link-matice neuměla. **Roh-podčást** ("roh = topologická obstrukce, K delokalizuje k rohu")
  je **jen 2D** — a protože spektrum-opravující BD objekt ji ve 4D NEOBNOVIL (roh/bulk f_nl 0,445<1,
  nl-vs-roh sklon +0,71 jako u link-matice), je to **reálná dimenzionální vlastnost, ne numerický
  artefakt**. Diagnóza VYPOCET-18 ("řídkost link-matice zabila signaturu") je **vyvrácena**.
- Důsledek: jednotící nit vrstva B platí **na slabu/klínu v každé dimenzi**, ale rohový mechanismus
  vyžaduje **reformulaci pro fyzikální dimenzi** — 4D null-tip diamantu (degenerující 2-sféra na bod)
  je jiný typ obstrukce než 2D prostorový tip (dvě protínající se null-přímky). To je hlavní háček
  pro páté kolo (viz H5g-3).
- **Vrstva C** dostala nový pozitivní datový bod: VYPOCET-19 ukázal, že rozdíl II₁/II_∞ je
  **obsah-saturace** (otázko-závislá, vrstva A/B), zatímco existence stopy je strukturální
  (vrstva C). Hranice mezi relačním a univerzálním je tak ostřejší než v kole 4.

---

## 2. Hypotézy 5. generace

Šest hypotéz. Pátá generace je *konsolidační a rozhodující*: po VYPOCET-19/20 jsou otevřené otázky
přesně lokalizované (4D dS truncovaná entropie; entropy cap vs. A/4; co nahrazuje rohy ve 4D;
tracialní probe; draft-05 kandidát). Každá: tvrzení (falzifikovatelné), opora (F-ID), test (geometrie/
objekt/observable/diskriminátor/N-proveditelnost — maticové ops strop ~N 2500), priorita, riziko.

### H5g-1 — 4D dS statická záplata: truncovaná area-law entropie sama oddělí II₁ od II_∞
> **[Kolo 10, VYPOCET-21, F-025] PARCIÁLNÍ:** reálný 4D-specifický separační signál potvrzen (flat/dS slope ratio 2.96, exponent 0.27 vs 0.52, N_total strop R²=1.000), ale plná saturace truncované S nedosažena při N≤2500 (dense eigh). Výsledek jde do draft-04 jako dS sekce. Plná saturace vyžaduje sparse solver + rho>~10³.
> **[Kolo 13, F-029] STATUS: SUPPORTED (rho=120 čistý), vyšší-rho compute-bound.** ds4d_saturation driver dokončil rho=120 (cap_dS=43.6 vs cap_flat=145.6, AIC favorizuje saturující model); rho=600 a rho=2000 nedoběhly (výpočetní limit). Driver budget/checkpoint fix aplikován (sub-cell BudgetExceeded + begin_cell/update_live). Čistá 4D saturace existuje při nižší hustotě; škálování přes rozsah hustot vyžaduje GH Actions s jemným checkpointingem nebo multi-job split.

**(jádro: přímý spektrální diskriminátor typu místo obsah-saturace; nejostřejší pokračování F-023)**
**Priorita: high.**

- **Tvrdí:** ve 4D dS statické záplatě (sech²-vážený slab, konformně-coupled bezhmotný skalár) bude
  **truncovaná** SSEE — na rozdíl od 2D — sama o sobě diskriminovat II₁ od II_∞: pro ohraničenou
  dS záplatu (II₁) truncovaná S~√N **saturuje** na konečný strop, jak oblast vyčerpává záplatu,
  zatímco pro neohraničenou plochou kontrolu (II_∞) truncovaná S~√N~L² **roste bez omezení**.
  Ve 2D je truncovaná SSEE log/area-flat v OBOU geometriích (diskriminoval jen obsah N_total,
  S_full); ve 4D area-law rank N^(3/4) dělá truncovanou entropii skutečnou plochou veličinou,
  která rozliší ohraničené od neohraničeného.
- **Opora (F-ID):** F-023 (VYPOCET-19) explicitně doporučuje 4D dS jako další krok a předpovídá
  rozlišení: *"Ve 4D by truncovaná typ-II SSEE byla S~√N~L² (area law), tj. rostla by s velikostí
  oblasti pro II_∞ a saturovala pro ohraničenou dS záplatu — tam by truncovaná entropie sama
  oddělila II₁ od II_∞."* F-019 (4D slab N^(3/4) rank = operativní regulátor, area law S~√N).
  F-016 (4D slab = čistý Hadamard, area law S~L^2.00).
- **Test:** **Geometrie** — 4D dS statická záplata, ds²=−(1−r²/ℓ²)dt²+... přepsaná do želvích
  souřadnic, ale 4D vyžaduje úhlovou část; nejlevnější prescription je **sech²-vážený 4D slab**
  (plochá iΔ konstrukce v (t,r*,x⊥), vlastní míra dN~sech²(r*/ℓ)) — přesně jak VYPOCET-19 navrhuje.
  **Objekt:** iΔ link-matice nebo BD smeared (BD lépe podmíněný a opravil 4D tvar spektra,
  VYPOCET-09/20). **Observable:** truncovaná SSEE s n_max=2N^(3/4) (validovaný regulátor z F-019),
  jako funkce R*_box→horizont, dS vs. plochá kontrola na shodné hustotě. **Diskriminátor:** dS
  truncovaná S saturuje (late-slope→0), plochá truncovaná S roste (late-slope>0) — opačná znaménka
  jako u F-023 obsahu, ale teď v TRUNCOVANÉ entropii. **N:** N≤2500 dense eigh; dS rozpočet
  saturuje kolem N~480–1000 při ρ~300, plochá roste — feasible na jedno odpoledne, 5 seedů.
- **Co by dalo:** povýšilo by F-023 z "obsah saturuje" na "**samotná regularizovaná gravitační
  entropie typu II rozlišuje II₁ od II_∞**" — to je nejpřímější diskrétní avatar CLPW věty a
  silný draft-05 materiál (4D je fyzikální dimenze). Spojilo by F-019 (4D area-law rank) s F-023
  (II₁/II_∞ obsah) do jednoho 4D výsledku.
- **Riziko:** sech²-vážený 4D slab může mít hrubou statistiku u horizontu (sech² koncentruje body
  do bulku, horizontová oblast řídne) → truncovaná S může být finite-N deformovaná dřív, než
  saturace nastane. Záloha: větší ℓ (rozprostře záplatu) nebo BD objekt (čistší spektrum). Pokud
  ani 4D truncovaná S neoddělí, padá na "II₁/II_∞ je jen obsah-saturace ve všech D" — stále
  publikovatelné, ale slabší.

### H5g-2 — Saturovaný obsah-strop dS záplaty se kvantitativně mapuje na A/4 (dS entropie z prvních principů?)

> **[Kolo 12, VYPOCET-23, F-028] PARCIÁLNÍ VERDIKT — correction note:** Slabá H5g-2 POTVRZENA: R_full = S_full_cap/A_mol = 0.1321 ± 1.3 % KONSTANTNÍ přes 5× hustotu ρ ∈ {240,600,1200} a 2× velikost záplaty ℓ ∈ {0.7,1.0,1.5} — kvantitativní area-zákon S_cap = A_horizon/(c·G), c ≈ 7.57. Silná H5g-2 VYVRÁCENA: c ≈ 7.57 ≠ 4 — geometrická O(1) normalizace 2D Dou-Sorkinova molekulového počtu vs. SSEE není fixována na 1/4. Anti-kruhovost respektována: ε ~ ρ^(−1/2) zafixováno z NEZÁVISLÉHO F-006 před měřením. Tracialní kanál (truncovaná SSEE): O(1), NEsleduje A_mol — není to A/4 kanál v 2D (F-027). Výsledky NEVYRACÍ hypotézu: proporcionální area-zákon stojí, ale přesná hodnota 1/4 pro 2D vyžaduje separátní kalibraci Dou-Sorkin koeficientu; 4D měření zůstává jako hlavní otevřená fronta.
> **[Kolo 13, F-029] STATUS 2D: CONFIRMED (rozšíření F-028).** Škálovaná kampaň ds_entropy_cap_2d (rho 240–1200, ℓ 0.7–2.5, n=10 buněk): R = 0.130 ± 0.0039 (CV 3.0 %), drift rho^{+0.007} ≈ nula, cross-HW reprodukce v rámci CV. 2D kvantitativní area-zákon je publikovatelně silný přes rozšířený rozsah parametrů. **STATUS 4D: CHYBÍ KONSTANTA — konvenční otázka otevřena.** c^{4D} roste 5.6 → 65.8 přes rho 60 → 1920; R^{4D} driftuje jako rho^{−0.72} — žádná čistá 4D area-konstantní neexistuje v testovaném rozsahu. Hlavní příčina: A_mol ~ rho^{1.77} (ne rho^{0.5}), S_full ~ rho^{1.05}. 4D A/4 claim oslaben, nikoli podpořen; pro 4D draft nutno nejprve vyřešit konvenční otázku diskretizace A_mol.
> **[Kolo 14, VYPOCET-27, F-031] STATUS 4D: KONVENČNÍ OTÁZKA VYŘEŠENA — 4D AREA-ZÁKON GENUINNĚ NEPŘÍTOMNÝ v této konstrukci.** Diagnóza rho^1.77: horizon_link_count_4d počítá kodim-1 SVĚTOČÁRU-TUBUS (t,x1,x2 se mění), NE kodim-2 entanglement 2-plochu. Korigovaná kodim-2 molekula (horizon_molecules_codim2, k_tube=1.5): A_mol^codim-2 ~ rho^(0.494±0.006) = přesně vlastní-plošný cíl rho^0.5 — konvenční artefakt vyřešen. Avšak i se správnou plochou R'=S_full/A_codim2 driftuje rho^+0.55 (CV 0.35), protože S_full škáluje objemově (~rho^0.997) zatímco plocha ~rho^0.5. ŽÁDNÝ poměr není rho-invariantní. 4D A/4 (ani area-zákon konstanta) v ploché-kauzální + dS-sech² konstrukci neexistuje. Konformně-váhový caveat (b) zůstává neotestovaný.

**(jádro: je dS entropie S=A/4 odvoditelná z diskrétního obsah-stropu? lovná zóna black-holes↔causal-sets)**
**Priorita: high (vysoký výnos, vysoké riziko).**

- **Tvrdí:** konečný strop, na který saturuje obsah-sledující entropie ohraničené dS statické
  záplaty (F-023: N_total cap=480, S_full saturuje), se po správné kalibraci **kvantitativně rovná
  Gibbons-Hawkingově entropii kosmologického horizontu A/4** — tj. maximálně-entropickému stavu
  algebry typu II₁ (CLPW: prázdný dS, S_max=A/4G). Konkrétně: poměr (saturovaná truncovaná S) /
  (vlastní obvod/plocha horizontu v jednotkách diskrétnosti) je konstanta nezávislá na ℓ a ρ, a
  tato konstanta je 1/4 (resp. její diskrétní analog). To by byl **diskrétní first-principles
  výpočet dS entropie** ze SJ+truncace machinerie.
- **Opora (F-ID):** F-023 (obsah saturuje na konečný strop, II₁ tracialní max-entropický stav
  existuje; Část 3 dokumentuje, že max-entropický strop S_dS~ln(horizont-area/4) je ve 2D O(1)
  číslo, dosažitelné při ρ~10³–10⁴). F-019 (4D area-law rank N^(3/4), truncovaná S~√N~A). Lovná
  zóna `black-holes-information→causal-sets` (barely): *"Sorkin spacetime entropy, S proportional
  to A, order-by-disorder counting of causal links across horizon"* — NEdotčeno žádným VYPOCETem.
  ESEJ-04 spekulativní jádro (bod 5): "A/4 = počet aktů svědectví přes horizont, 1/4 = směnný
  kurz plochy a svědectví" — zde se z eseje stává falzifikovatelný výpočet.
- **Test:** **Geometrie** — dS statická záplata (2D nejdřív, kde A/4 je O(1) a tedy dosažitelný;
  pak 4D). **Objekt:** SJ + truncace, vlastní (proper) plocha horizontu spočtená z sech² míry.
  **Observable:** (a) saturovaná truncovaná S vs. vlastní délka/plocha horizontu v jednotkách
  diskrétní škály ε~ρ^(−1/d); (b) jejich poměr jako funkce ρ a ℓ. **Diskriminátor:** poměr je
  konstantní (nezávislý na ρ, ℓ) → **mapuje na A/4**; poměr driftuje → nemapuje, jen kvalitativní
  saturace. **Predikce 1/4** je tvrdý falzifikátor: buď diskrétní konstanta konverguje k
  univerzální hodnotě (a porovná se s 1/4), nebo ne. **N:** F-023 dokumentuje, že tracialní limita
  vyžaduje ρ~10³–10⁴ — to je **za hranicí dense eigh při N~2500**; potřeba (i) větší ℓ s nižší ρ
  pro 2D obrys, NEBO (ii) řídké/iterativní řešiče (scipy.sparse.linalg.eigsh) na low-rank truncaci.
  **Není to jedno odpoledne** — vyžaduje novou numerickou mašinérii (sparse eigensolver).
- **Co by dalo:** kdyby poměr konvergoval k 1/4, byl by to **first-principles diskrétní výpočet
  Gibbons-Hawkingovy entropie** ze SJ+truncace — nejhlubší možný výsledek celé linie A×B,
  samostatný draft. Spojilo by `causal-sets`, `von-neumann-algebras`, `black-holes-information`,
  `holography-adscft` do jednoho čísla.
- **Riziko (vysoké):** (a) ρ~10³–10⁴ je výpočetně tvrdé (F-023 honest null v Části 3 přesně proto);
  (b) "kalibrace" diskrétní škály vs. vlastní plocha má volné konstanty (4π v κ, α v area-law rank)
  — poměr může vyjít 1/4 jen po vnucení správné kalibrace, což by byl kruh, ne predikce. Musí se
  předem zafixovat kalibrace z NEzávislého výpočtu (F-006 ε~ρ^(−1/2)) a teprve pak měřit poměr.
  Pokud se kalibrace tuninguje k 1/4, hypotéza je iluzorní (stejný filtr jako −18/11 scheme-robustnost).

### H5g-3 — Co nahrazuje rohy ve 4D: kaustiky / vyšší-kodimenzní hrany jako locus selhání boost-flow
> **[Kolo 10, VYPOCET-22, F-026] VYVRÁCENA:** codim-2 klínová hrana dává nl-vs-hrana sklon +0.115 (CI68 [0.106,0.124]) — kladné znaménko shodné s 4D null-tip, opačné než 2D roh; rohová podčást vrstva B čistě 2D (potvrzeno napříč 3 lokusy a 3 objekty). Slab/boost podčást BW přežívá (R²=0.92).

**(jádro: reformulace rohového mechanismu pro fyzikální dimenzi po VYPOCET-20 nulu)**
**Priorita: medium-high.**

- **Tvrdí:** 2D rohový mechanismus H4g-1 (boost nemá kam téct → K delokalizuje k rohu → non-Hadamard)
  **nepřežívá ve 4D na null-tipu diamantu** (F-024: BD i link dávají roh MÉNĚ non-lokální než bulk),
  protože 4D null-tip je **degenerující 2-sféra na bod**, ne dvě protínající se null-přímky. Správný
  4D locus selhání geometričnosti modulárního toku je **jiný geometrický objekt**: buď (i) **kaustika**
  (místo, kde se nulové geodetiky fokusují, konjugovaný bod), nebo (ii) **vyšší-kodimenzní hrana**
  (codim-2 "joint" mezi dvěma null-plochami, kde se setkávají dva boostové generátory — analog rohu,
  ale 2-rozměrný útvar, ne bod). Predikce: na 4D regionu s codim-2 spojem (např. dva protínající se
  Rindlerovy klíny / "cuspy" entangling plocha) modulární tok ztratí lokalitu **na tom spoji**, ne
  na izolovaném tipu — a to BD objekt v modulárně-lokalitní sondě UVIDÍ, na rozdíl od null-tipu.
- **Opora (F-ID):** F-024 (VYPOCET-20: rohová koncentrace NEREPLIKUJE ve 4D ani s BD objektem;
  diagnóza "link-matice" vyvrácena; *"4D null-tip diamantu je jiný typ obstrukce než 2D prostorový
  tip — degeneruje 2-sféra na bod"*). F-021 (2D roh mechanismus robustní, 4/5; slab boost-geometricita
  4D-robustní). F-016 (Hadamardova anomálie lokalizovaná v rozích 2D i 4D diamantu — ale to byla
  ENTROPICKÁ/Hadamardova sonda, ne modulárně-lokalitní; možná entropický roh ≠ modulární roh ve 4D).
- **Test:** **Geometrie** — 4D entangling region s **codim-2 spojem**: nejlevnější je "L-shaped"
  nebo "wedge-joint" region (dva slaby svírající úhel, sdílející codim-2 hranu), kde Bisognano-Wichmann
  předpovídá, že každý klín má svůj boost, ale na společné hraně se nemohou srovnat. Kontrola: jeden
  čistý slab (boost lokální všude, F-024 potvrzeno). **Objekt:** BD smeared (ε=0,6, dobře podmíněný,
  F-024 ho validoval na slabu). **Observable:** off-diagonální sklon modulárního kernelu + per-site
  f_nl gradient směrem ke codim-2 spoji (stejná sonda jako VYPOCET-18/20). **Diskriminátor:** f_nl
  roste ke spoji (sklon<0, jako 2D roh) → codim-2 hrana JE 4D analog rohu; f_nl klesá ke spoji
  (jako 4D null-tip) → ani codim-2 hrana to není, a vrstva B roh-podčást je čistě 2D fenomén.
  **N:** N≤2200 (mez BD inverze, F-024), 3 seedy — feasible na jedno odpoledne, je to varianta
  hotového VYPOCET-20 kódu s jinou geometrií regionu.
- **Co by dalo:** kdyby codim-2 spoj replikoval 2D rohový mechanismus, **zachránilo by to vrstvu B
  pro fyzikální dimenzi** (jen jsme testovali špatný geometrický objekt — null-tip místo spoje) a
  obnovilo by ESEJ-04 tezi "singularity = epistemické" jako 4D-životnou. Kdyby ne, je to čistý
  negativní výsledek: rohová obstrukce je 2D artefakt, vrstva B drží jen na hladkém klínu.
- **Riziko:** codim-2 spoj v causet sprinklingu má tenkou statistiku (codim-2 = nula-míra množina),
  podobně jako 4D null-tip. Pokud signál tone v šumu (F-024 nl-vs-roh R²=0,56 už ve 4D), nemusí
  rozhodnout. Záloha: kaustika (geodetický fokus) má codim-1 strukturu, lepší statistiku — ale
  obtížnější ji vyrobit na causetu (vyžaduje zakřivené pozadí, ne plochý diamant).

### H5g-4 — Spektrální triple ↔ Pauli-Jordan: NCG Diracův operátor rekonstruuje SJ modulární Hamiltonián (lovná zóna)

> **[Kolo 15, VYPOCET-29, F-033] GO-LIMITED / NO-MATCH NA METRICKÉ ÚROVNI.** Surogátní D_K=sgn(K)sqrt(|K|) na 2D slabu (N=1200, 5 seedů) reprodukuje BW boostovou strukturu (lineární diagonála R^2=0.955, robustní) ale jeho Connesova vzdálenost NEsleduje kauzální vzdálenost (korelace 0.319, R^2=0.10, 16 párů; kolo-21 reprodukční oprava committed 0.10 -> 0.319, verdikt no-match nezměněn). Hrana causal-sets <-> NCG (connections.json idx 61) INSTANCOVÁNA — zůstává barely jako **informovaný negativ**: korespondence SJ modulární Hamiltonián <-> NCG spektrální triple selhává na METRICKÉ úrovni; boostová/tepelně-časová osa (Connes-Rovelli) solidní.

**(jádro: nedotčená barely hrana `causal-sets↔noncommutative-geometry`, shared-math; spojí dvě vlajkové linie přes třetí pilíř)**
**Priorita: medium (vysoká novost, střední proveditelnost).**

- **Tvrdí:** spektrální triple NCG (Diracův operátor D, algebra A, Hilbertův prostor H) a SJ
  konstrukce na causetu (Pauli-Jordan iΔ, jeho pozitivní část W, modulární Hamiltonián K) jsou
  **dvě realizace téže spektrální rekonstrukce geometrie**. Konkrétní falzifikovatelná verze:
  lze zkonstruovat spektrální triple, jehož Diracův operátor reprodukuje modulární Hamiltonián K
  poloprostoru/slabu (Bisognano-Wichmann boost), a jeho **spektrální vzdálenost (Connesova distance
  formula)** se shoduje s entanglementovou metrikou (vzdálenost odvozená z modulárního toku). Most:
  oba pilíře "odmítají hladkou UV varietu a rekonstruují geometrii spektrálně" — NCG přes Dirac,
  causet přes Pauli-Jordan/SJ spektrum.
- **Opora (F-ID):** Lovná zóna `causal-sets→noncommutative-geometry` (barely, shared-math, NEdotčená
  žádným VYPOCETem): *"the spectral triple / Dirac operator of NCG parallels the Pauli-Jordan
  operator and SJ spectrum that encode geometry on causal sets. A direct correspondence between
  these spectral reconstructions [is unexplored]."* Posílena lovná zóna
  `entanglement-spacetime→noncommutative-geometry` (barely, shared-math): *"spectral triples ↔
  entanglement entropy [bridge unexplored]."* F-011 (modular-hamiltonian TOP HUB — přesně objekt,
  který by spektrální triple měl reprodukovat). F-003/F-014 (máme NCG Diracovu a₄ mašinérii ze
  draftu-02). F-019/F-016 (slab = poloprostor, kde K=boost je analyticky znám — čistý testbed).
  SYNTEZA-02 lovecký žebříček #4: tato hrana "vystoupala masivně" díky F-011.
- **Test:** **Geometrie** — 4D (nebo 2D) slab, kde modulární K je analyticky Bisognano-Wichmann
  boost. **Objekt:** (a) SJ modulární Hamiltonián K(x,y) z VYPOCET-18/20 (korelátorové K z W,iΔ);
  (b) kandidátní finite-dim spektrální triple s Diracem D postaveným nad causet (BD d'Alembertián
  jako D² je přirozený kandidát — VYPOCET-09 ho má). **Observable:** spektrum K vs. spektrum D;
  Connesova spektrální vzdálenost d(x,y)=sup{|a(x)−a(y)|: ‖[D,a]‖≤1} vs. modulární/kauzální
  vzdálenost na slabu. **Diskriminátor:** spektra/vzdálenosti se shodují (až na škálu) → spektrální
  triple JE NCG-jazyk SJ modulárního toku; neshodují → jsou to různé objekty a hrana zůstává
  barely. **N:** spektrum už máme (VYPOCET-09/18/20, N≤2200); Connesova distance je
  optimalizace (sup přes Lipschitz elementy) — netriviální, ale na malých N (~200–500) feasible
  jako proof-of-concept; full scan je nová mašinérie.
- **Co by dalo:** první **datová hrana `causal-sets↔NCG`** v grafu (dosud čistě barely shared-math),
  spojující obě vlajkové linie (linie A SJ + linie B von Neumann) přes třetí pilíř (NCG draftu-02).
  Pokud spektrální triple reprodukuje modulární K, sjednotí to algebraický jazyk celého programu
  pod jeden Diracův operátor — through-line vrstva B by dostala NCG formulaci.
- **Riziko:** konstrukce spektrálního triple, jehož D reprodukuje boost-modulární K, **nemusí
  existovat** v konečné dimenzi (modulární K je neohraničený, spektrální triple D má specifickou
  strukturu komutátorů). Connesova distance je notoricky drahá na výpočet. Toto je **read+think
  napřed, compute potom** — vyžaduje literaturní rešerši (existují spektrální triple pro modulární
  flow? Connes-Rovelli termální čas vs. spektrální triple) předtím, než se vůbec sáhne na causet.
  Pokud literatura ukáže, že korespondence je strukturálně nemožná, hypotéza padá při čtení.

### H5g-5 — Exponent B(Ω) je spojitá funkce strhávání, ne dimenzní konstanta (zostření H4g-2)
> **[Kolo 14, VYPOCET-26, F-030] UZAVŘENO — B(a) JE SPOJITÁ FUNKCE, konstantní model B=3 (D-1) rozhodně zamítnut.** Neomezený log-log fit (oprava artefaktu meze A=100 z F-017) dává monotónně klesající Kerr B(a): 6.10(a=0.3)→2.54(a=0.99), trend dB/da=-2.20 (z=-33.6), chi2_const=2473/7 vs chi2_linear=111/6. B=3 protíná křivku jen při a~0.75 — D-1=3 není privilegovaná hodnota. BTZ pod Kerr křivkou (gap -1.10/-0.55) — role asymptotiky potvrzena bez Kerr-AdS. Implikace pro draft-01 §4.2 uzavřena: predikce přechází na trend dB/da<0 + BTZ-Kerr polohu.

**(jádro: PROČ B=4,2 Kerr vs. 1,7 BTZ; rozhodnout dimenze vs. asymptotika; uzavírá draft-01 fyzikální predikci)**
**Priorita: medium.**

- **Tvrdí:** mocninový exponent B v W_sr~Ω(r)^B **není dimenzní konstanta** (D−1), ale **spojitá
  funkce lokálního strhávání a asymptotiky pádu Ω(r)**. Důkaz z dat: B klesá 4,23→3,82 se spinem
  a=0,6→0,9 při FIXNÍ dimenzi (4D Kerr) — kdyby B=(D−1)=3, byl by konstantní. Hypotéza: B je dán
  hustotou superradiantních módů v klínu ω(ω−kΩ)<0, která škáluje s asymptotikou metriky
  (Kerr Ω~1/r³ vs. BTZ Ω~1/r²) a se spinem. Falzifikovatelná forma: B(Kerr-AdS) ≠ B(Kerr) při
  STEJNÉ dimenzi (4D) ⟹ B závisí na asymptotice, ne na D.
- **Opora (F-ID):** F-017 (B=4,23/3,82/1,71 přes tři konfigurace; klesá se spinem při fixní D).
  F-018 (Ω(r) zákon robustní v log-log; A_W near-zone ~r^(−2,75)≈r^(−3) tracking |Ω|). F-013
  (W_sr roste monotónně se spinem). BRAINSTORM-04 H4g-2 už toto navrhl — H5g-5 ho zostřuje na
  "B je spojitá funkce, ne konstanta" jako primární tvrzení (BRAINSTORM-04 to mělo jako riziko).
- **Test:** **Geometrie** — Kerr-AdS (4D, ale Ω~1/r jiná asymptotika než plochý Kerr) izoluje
  dimenzi vs. asymptotiku. **Objekt:** SJ na ekvatoriální Kerr-AdS sekci (stejná mašinérie jako
  VYPOCET-08/14). **Observable:** W_sr~Ω^B radiální scan, fit B; A_W power-law. **Diskriminátor:**
  B(Kerr-AdS)≠B(Kerr) → asymptotika; B(Kerr-AdS)=B(Kerr) → dimenze. **Levnější alternativa:**
  hustší vzdálený scan r=5–20M na hotovém Kerru (BRAINSTORM-04 fronta #5) uzavře poslední Model
  E vs. S dvojznačnost u a=0,6. **N:** N=1600, 5 seedů jako VYPOCET-14 — feasible, ale Kerr-AdS
  vyžaduje ověřit well-definedness SJ s reflective AdS hranicí (jako φ-periodicita u draftu-01).
- **Co by dalo:** povýšilo by draft-01 z "Ω-zákon platí" na "Ω-zákon s **predikovatelným**
  exponentem" — falzifikovatelná predikce pro 4D Teukolsky (srovnání B se superradiantním
  zesilovacím koeficientem |R_lm|²). Rozdíl mezi fenomenologií a teorií.
- **Riziko:** fit B narážel na horní mez A=100 (Kerr); absolutní B jsou orientační, robustní je
  ΔAIC a relativní B. Kerr-AdS má jiné okrajové podmínky → SJ konstrukce může vyžadovat jinou
  prescription (well-definedness není zaručena). Pokud B je čistě spojitá funkce spinu bez
  dimenzního/asymptotického vzoru, je predikce slabá (jen "B roste s |Ω|").

### H5g-6 — Draft-05 kandidát: F-023+F-019 zakládají samostatný "II₁ vs II_∞ na de Sitteru" letter

**(meta-hypotéza o publikační strategii: rozšiřuje F-023+F-019 draft-04, nebo zakládá draft-05?)**
**Priorita: medium (strategická).**

- **Tvrdí:** F-023 (dS II₁ vs. II_∞ diskriminace) + F-019 (4D slab N^(3/4) area-law rank) +
  H5g-1 (pokud projde: 4D dS truncovaná entropie odděluje typy) tvoří **dostatečně samostatný a
  nový výsledek na vlastní letter (draft-05)**, ne jen na rozšíření draftu-04. Důvod: draft-04 je
  "III₁→II přechod" (jeden přechod, neohraničené geometrie, typ II_∞). F-023 přidává **druhou osu
  von Neumannovy klasifikace** (II₁ vs II_∞, ohraničené vs neohraničené), kterou žádná surveyovaná
  práce diskrétně netestovala, a kterou CLPW identifikovali jako klíčový rozdíl dS od černé díry.
  To je samostatný příběh: "diskrétní SJ sonda vidí CLPW II₁/II_∞ distinkci na de Sitteru".
- **Opora (F-ID):** F-023 (DISKRIMINOVÁNO, project-original: *"No prior publication has performed
  this test"*; sjednocuje obě vlajkové linie). F-019 (4D N^(3/4) rank, area-law). F-022 (draft-04
  je "III₁→II", neohraničené geometrie — F-023 je ortogonální osa). REVIZE-PRO-CLOVEKA: draft-04
  je "syntéza tří publikovaných výsledků" — F-023 přidává čtvrtý (CLPW II₁) a novou geometrii (dS).
- **Test (rozhodovací, ne výpočetní):** rozhodne **H5g-1** (4D dS truncovaná entropie). Pokud
  H5g-1 projde (4D truncovaná S sama oddělí II₁ od II_∞), je to silný samostatný letter (draft-05):
  "type II₁ vs II_∞ discrimination via SJ truncation on the de Sitter static patch", 2D obsah +
  4D truncovaná entropie. Pokud H5g-1 neprojde (jen 2D obsah-saturace), F-023 se **přilepí k
  draftu-04** jako jeho dS sekce ("the same machinery also resolves II₁ vs II_∞").
- **Co by dalo:** ujasnilo by publikační frontu. Draft-05 by byl **capstone obou vlajkových linií**
  (linie A SJ-horizont × linie B typový přechod, potkané na de Sitteru) — koncepčně nejcennější
  publikovatelný výstup celého programu.
- **Riziko:** F-023 je "supported", ne "confirmed" (2/3 proxy + obsah-diskriminace ve 2D; tracialní
  probe je honest null). Bez H5g-1 (4D) je to "jen 2D obsah-saturace", což je slabší letter. Riziko
  přefouknutí: II₁/II_∞ je asymptotický invariant, na konečném N měříme TRENDY (saturace vs. růst),
  ne typ sám — stejný caveat jako draft-04, musí být explicitní (jako v ESEJ-04 inventuře, bod 1).

---

## 3. Doporučená fronta

Seřazeno podle (decisiveness × proveditelnost × novost). Rozlišuji **[odpoledne]** (varianta
hotového kódu, dense eigh N≤2500) vs. **[nová mašinérie]** (sparse solver, spektrální triple,
nové pozadí) vs. **[read+think]**.

| # | Test | Hypotéza | Náročnost | Co rozhodne |
|---|------|----------|-----------|-------------|
| 1 | **4D dS statická záplata: truncovaná area-law S odděluje II₁/II_∞** (sech²-vážený 4D slab, n_max=2N^(3/4), dS vs. plochá kontrola) | H5g-1 | **[odpoledne]** varianta VYPOCET-19+16 | Oddělí 4D **truncovaná** entropie typy (ne jen obsah)? → draft-05. Nejostřejší pokračování F-023, fyzikální dimenze. |
| 2 | **Codim-2 spoj / wedge-joint: 4D analog rohu?** (dva svírající slaby, BD smeared, f_nl gradient ke spoji) | H5g-3 | **[odpoledne]** varianta VYPOCET-20 | Replikuje codim-2 hrana 2D rohový mechanismus? → zachrání/pohřbí vrstvu B roh-podčást ve 4D. Levné (hotový kód, jiná geometrie). |
| 3 | **Hustší vzdálený Kerr scan r=5–20M** (Model E vs. S u a=0,6) + **B(Kerr-AdS)** | H5g-5 | **[odpoledne]** scan / **[nová]** Kerr-AdS | Uzavře poslední dvojznačnost VYPOCET-14; izoluje dimenze vs. asymptotika exponentu B. |
| 4 | **Entropy-cap vs. A/4 poměr** (2D dS obrys nejdřív, kalibrace z F-006, poměr jako f(ρ,ℓ)) | H5g-2 | **[nová mašinérie]** sparse eigsh, ρ~10³–10⁴ | Mapuje saturovaný strop na A/4 (predikce 1/4)? → first-principles dS entropie. Nejvyšší výnos, nejvyšší riziko, NE jedno odpoledne. |
| 5 | **Spektrální triple ↔ modulární K** (slab, Connesova distance vs. modulární vzdálenost) | H5g-4 | **[read+think]** pak **[nová]** | Reprodukuje NCG Dirac SJ modulární tok? → datová hrana causal-sets↔NCG. Číst literaturu napřed. |
| 6 | **Proxy 3 vN typ s 30–50 seedy** (centrální sekvence, dorozhodnutí F-015/F-019/F-023) | H5g-6 | **[odpoledne]** re-run | Dorozhodne třetí proxy (při 5–8 seedech nesignifikantní napříč VYPOCET-12/16/19); levný follow-up. |

**Doporučené pořadí:** #1 a #2 **paralelně** (obě [odpoledne], obě varianty hotových kódů, obě
rozhodují draft-05 resp. vrstvu B) — to je nejvyšší ROI tohoto kola. Pak #3 (uzavře draft-01
fyzikální predikci). #4 (entropy-cap vs A/4) je **vlajkový, ale vyžaduje sparse solver** — zařadit,
jakmile #1 potvrdí 4D dS mašinérii (sdílí geometrii). #5 začít čtením (může padnout při rešerši).
#6 kdykoli jako levný plnič.

**Jedno odpoledne:** #1, #2, #3-scan, #6. **Nová mašinérie:** #4 (sparse eigsh), #5 (spektrální
triple + Connes distance), #3-KerrAdS (nové pozadí + well-definedness). **Read-first:** #5.

---

## 4. Doporučení pro velké review

Uživatel plánuje velké review: (A) data-correctness audit, (B) doplnění teoretických linků v
concept grafu, (C) repo cleanup. Co musí review zkontrolovat **nejdřív** — od nejtvrdších known
weak points k systematickým.

### 4A. Data-correctness — známé slabé body (zkontrolovat v tomto pořadí)

1. **Placeholder `a_err=0.775853...` v draftu-04 (KRITICKÉ).** Je to *seed-spread placeholder*
   zkopírovaný napříč mnoha poli, NE per-fit standardní chyba (draft-04 TODO.md ř. 83; REVIZE ř. 120).
   Doloženo i v datech: `core-data/calculations/ssee-slab-4d/results.json` ř. 488/567 nese
   `0.7765529868935468` na dvou místech. **Akce:** nahradit KAŽDOU nejistotu exponentu (i) regresní
   SE a (ii) across-seed bootstrap CI; pročistit hodnotu `a_err=0.776` z celého draftu-04. Bez toho
   jsou všechna "±" v draftu-04 nedefinovaná.

2. **Neověřené 2025–2026 arXiv ID (KRITICKÉ — riziko vymyšlených ID).** Projekt má striktní pravidlo
   "nikdy nevymýšlet arXiv ID". Nejrizikovější, výslovně označené jako neověřené:
   - `arXiv:2602.16782` (Jones–Yazdi) — draft-04 tvrdí verbatim z provenience, **neověřeno**
     (REVIZE ř. 138); podpírá identifikaci ε=ln[μ/(μ−1)].
   - `arXiv:2501.09669` (Fröb, atribuce z draft-04 v0.2) — nový (2025), draft-04, **potvrdit existenci a obsah** (REVIZE ř. 137).
   - `arXiv:2602.09796` (Häfner & Klein, Unruh na subextremálním Kerru — oprava 2026-06-08, draft-01 i REVIZE; dřívější atribuce Dafermos–Luk byla chybná) — draft-01, **potvrdit, že ID existuje a říká,
     co se tvrdí** (REVIZE ř. 31).
   - `arXiv:2504.12919`, `arXiv:2303.13488`, `arXiv:2601.07915`, `arXiv:2306.07323` — draft-01/04,
     potvrdit existenci.
   **Akce:** každé ID 2025–2026 ověřit přes WebFetch/WebSearch proti arxiv.org; neexistující smazat
   nebo označit ⚠️ neověřeno (per CLAUDE.md politika). Toto je **nejvyšší priorita** — vymyšlené ID
   diskredituje celý projekt.

3. **Ilustrativní hodnota 8 v CST random walk (draft-03).** Číslo 8=D+4 je *ilustrativní*, NE z
   Eichhorn–Mizera (1311.2530), který nedává univerzální asymptotickou konstantu (draft-03 TODO ř. 55,
   draft.md ř. 156/159/177; REVIZE). **Akce:** potvrdit, že tabulka a §6 nese label "REPRODUCE
   (qualitative)" a že 8 nelze číst jako kvantitativní nárok. Referee, který přečte 8 jako tvrzenou
   hodnotu, draft odmítne.

4. **D-konvence v Hořavově řádku (draft-03).** Je D v d_s=1+D/z spacetime nebo prostorová dimenze?
   Per-řádková konzistence celé tabulky není ověřena (REVIZE ř. 86, draft-03 TODO ř. 86). **Akce:**
   per-řádkový audit D vs. D_space v master `d_s=D/γ` i v anizotropním `1+D_space/z`.

5. **Caveaty v findings.json — systematický průchod.** Z findings.json přímo:
   - F-001/F-012: CST random-walk d_s "illustrative 8"; BD α-drift +1,28 nekonvergován při N≤3000;
     cond(B) roste do 2e10 — **žádné findings tvrzení nesmí být čteno jako konvergované**.
   - F-006: p=1/2 jen na 2,8σ (ne 5σ) — "consistent with", ne "equals".
   - F-015/F-019/F-023: **2/3 resp. 3/3 proxy, ale "supported", NE "confirmed"** — Proxy 3
     (centrální sekvence) je napříč VYPOCET-12/16/19 **nesignifikantní při 5–8 seedech** (REVIZE
     ř. 144: "2D verdikt je 2/3, nikoli 3/3 — summary to nesmí zmást"). Konečná matice = vždy
     triviálně typ I_n; měříme TRENDY, ne typ.
   - F-019/F-023: N^(3/4) je **předpis, ne spektrální rys** (slab nemá ostré koleno) — referee to
     napadne jako "vnucený exponent" (REVIZE ř. 14).
   - F-024: nl-vs-roh R²=0,56 (4D) — verdikt stojí na ZNAMÉNKU sklonu, ne hodnotě; nízké R².
   - F-016: literatura (2008.07697, 2412.07832) NEpotvrzuje non-Hadamard↔volume jako přímý
     mechanismus — náš výsledek je korelace, ne kauzální důkaz.
   **Akce:** každé "confirmed" v findings.json prověřit, zda nemaskuje "supported"; každý proxy-verdikt
   ověřit proti seed-počtu.

6. **Neověřené hodnoty v knowledge-base (mimo drafty).** Grep `⚠️ neověřeno` našel:
   - AS kritické exponenty: `λ*g*≈0,133/0,136` a `1/ν≈1,472` se NEpodařilo ověřit proti
     1301.4191/1410.4815 (approaches/03-asymptotic-safety.md ř. 83/89/155) — a `1/ν≈1,472` bylo
     původně chybně přiřazeno 1307.0765 (je od Nagye, ne Fallse).
   - LQG: `γ₀ jednospinový ln2/(π√3)≈0,127 ≠ skutečné SU(2) 0,274` (approaches/02 ř. 104) — pozor
     na záměnu naivního a plného počítání.
   - LQG spinová pěna: `Λ=6π/(ℓ_P²k)` neověřeno (ř. 132); NCG horizont kvantizace neověřeno
     (approaches/07 ř. 240); CDT↔BH entropie spojení neověřeno (approaches/04 ř. 264); ostrov
     ℓ_P√r_h bez citace (cross-cutting/12 ř. 175).
   **Akce:** tyto jsou už označené ⚠️ — review má potvrdit, že se nikam nepropsaly jako tvrzené
   hodnoty do draftů/findings.

7. **Re-run všech 12 calc.py a porovnání s results.json + findings.** Žádný výpočet neproběhl
   nezávisle mimo AI pipeline (REVIZE ř. 188–224 má přesné příkazy). **Akce:** spustit, porovnat
   headline čísla; každá neshoda je blokátor. Zvlášť ±-párovací rezidua (mají být ~1e-13–1e-16).

### 4B. Chybějící / nedostatečně specifikované teoretické linky v concept grafu

Z hunting-zone analýzy (114 barely hran, connections.json) — linky, které jsou nyní **pákové našimi
nástroji/daty, ale v grafu chybí nebo jsou jen "barely"**:

1. **`causal-sets↔von-neumann-algebras` — datová hrana CHYBÍ v connections.json.** Pilíř 19 přidal
   VNA do concept-graph.json/fragments, ale connections.json (288 hran) **nemá ani jednu VNA hranu**
   (ověřeno: 0 edges s von-neumann-algebras ve `from`/`to`). Přitom F-015/F-019/F-023 ji zakládají
   DATY (III₁→II, II₁/II_∞). **Akce:** doplnit do connections.json hranu `von-neumann-algebras↔causal-sets`
   (type: shared-structure, explored: partially, evidence: F-015/F-019/F-023, VYPOCET-12/16/19) a
   `von-neumann-algebras↔loop-quantum-gravity` (LQG area-gap jako crossed-product regulátor —
   třetí, NEOTESTOVANÁ noha trojúhelníku draftu-04, REVIZE ř. 240–242).

2. **`causal-sets↔noncommutative-geometry` (barely, shared-math) — H5g-4 lovná zóna.** Spektrální
   triple/Dirac ↔ Pauli-Jordan/SJ spektrum. **Nedotčená, vysoce páková** (máme NCG a₄ mašinérii
   draftu-02 + SJ mašinérii). **Akce:** označit jako prioritní hunting target; po H5g-4 (i kdyby
   negativní) doplnit status.

3. **`black-holes-information↔causal-sets` (barely) — H5g-2 lovná zóna.** Horizontová entropie
   S~A z počítání kauzálních linků (Dou-Sorkin). **Nedotčená**; přitom F-023 (dS obsah-strop) je
   přímo na ní. **Akce:** propojit s F-023 a H5g-2; je to most k A/4.

4. **`entanglement-spacetime↔noncommutative-geometry` (barely, shared-math).** Tomita-Takesaki,
   crossed-product, spektrální triple ↔ entanglement. **Pákové** přes F-011 (modular-hamiltonian
   TOP HUB) — graf to má jako barely, ale F-011/F-015 ji už fakticky aktivovaly. **Akce:** povýšit
   na partially, evidence F-011.

5. **`causal-sets↔asymptotic-safety` (barely) — SYNTEZA-02 lovecký #1.** BD path integral → AS-like
   fixní bod. **Nedotčená VYPOCETem**; máme spektrální engine (F-001) + BD spektrum (F-012). Pozor:
   F-012 α-drift může bránit konvergenci fixního bodu. **Akce:** označit jako otevřený compute
   target, ne chybějící link (je správně barely).

6. **Trojúhelník draftu-04 — třetí noha explicitně neúplná.** SSEE truncace = crossed-product cutoff
   (testováno) = **LQG area gap Δ=4√3πγℓ_P²** (NEOTESTOVÁNO, konjektura, REVIZE ř. 240). **Akce:**
   v grafu i draftu musí zůstat označená jako konjektura; review ověří, že není prezentována jako
   výsledek.

### 4C. Repo cleanup — co zkontrolovat

1. **Konzistence ID napříč soubory.** Findings F-001…F-024 (24 nálezů) — ověřit, že číslování v
   findings.json (pozor: pořadí je F-001…F-011, pak F-014, F-012, F-015, F-016, F-017…F-013 na konci —
   **NEseřazené**), PROGRESS.md, BRAINSTORM-04 (mluví o "17 findings", capstone je nyní 24) a
   SYNTEZA-02 ("17 nálezů") **souhlasí**. BRAINSTORM-04/SYNTEZA-02 byly psány při 17 findings —
   review má zkontrolovat, že odkazy na počty jsou aktualizované nebo datované.

2. **VYPOCET ↔ calc-directory mapování.** VYPOCET-12 = `sj-vn-type` NEBO `vn-type-*`? Názvy v
   knowledge-base/vypocty/ (VYPOCET-12-vn-typ-truncace.md) vs. core-data/calculations/ (VYPOCET-12/,
   sj-vn-type/, vn-type-slab-4d/) — REVIZE ř. 216–219 mapuje draft-04 na `ssee-diamond`,
   `vn-type-slab-4d`, `ssee-slab-4d`, `sj-vn-type`. **Akce:** ověřit, že každý VYPOCET-NN.md odkazuje
   na existující calc adresář a results.json.

3. **PROGRESS.md aktualizace.** Per CLAUDE.md "po každé dokončené fázi aktualizovat PROGRESS.md" —
   review má potvrdit, že PROGRESS.md odráží 24 findings, VYPOCET-20 a kolo 9 (capstone).

4. **Eseje vs. drafty — oddělení spekulace.** ESEJ-01…04 jsou spekulativní (⚠️ na ř. 1); review má
   ověřit, že žádné esejové tvrzení (ESEJ-04 "vesmír svědčí sám sobě", "A/4 = akty svědectví") se
   nepropsalo do findings/draftů jako fakt. ESEJ-04 bod 5 (typ II fundamentální vs. aproximace
   typu I) a H5g-2 (A/4 z prvních principů) sdílejí jádro — udržet hranici spekulace/výpočet ostrou.

---

## 5. Capstone shrnutí

Devět kol skončilo se **dvěma vlajkovými liniemi, které se na de Sitteru protnuly** (F-023:
diskrétní SJ sonda vidí CLPW II₁ vs II_∞), **jedním index-chráněným jádrem stranou** (−18/11,
draft-02 uzavřen), **čtyřmi čistými popravami** (γ-Cardy, naivní Λ, H4g-3 Λ-identita, spojité BMV)
a **jednotící nití, jejíž vrstva B prošla rozhodujícím testem**: slab-podčást je 4D-robustní
(VYPOCET-20), roh-podčást je reálně 2D (ne artefakt). Páté kolo je konsolidační: nejostřejší
otevřené otázky jsou lokalizované — **4D dS truncovaná entropie** (H5g-1, draft-05 rozhodnutí),
**entropy-cap vs A/4** (H5g-2, dS entropie z prvních principů, vlajkový-ale-drahý), **co nahrazuje
rohy ve 4D** (H5g-3, codim-2 spoj). Fronta: #1+#2 paralelně (obě jedno odpoledne, varianty hotových
kódů), pak A/4 a spektrální triple jako nová mašinérie. Velká revize musí začít u placeholderu
`a_err=0.776` a neověřených 2025–26 arXiv ID — to jsou jediné položky, které mohou diskreditovat
jinak kalibrovaný program.

---

*Anchory pátého kola: `core-data/findings.json` (F-001…F-024, 24 nálezů; F-023/F-024 nejčerstvější);
`knowledge-base/vypocty/VYPOCET-19-desitter-II1.md` (II₁ vs II_∞ diskriminace, sjednocení linií),
`VYPOCET-20-modularni-tok-bd-4d.md` (vrstva B štěpení, roh-podčást 2D); `knowledge-base/SYNTEZA-02.md`
(through-line, lovecký žebříček); `core-data/connections.json` (114 barely hran, hunting zone:
causal-sets↔NCG, BH↔causal-sets, causal-sets↔AS); `knowledge-base/eseje/ESEJ-04-vstup-pozorovatele.md`
(spekulativní jádro H5g-2); `papers/REVIZE-PRO-CLOVEKA.md` (revizní checklist, a_err=0.776,
arXiv ID); `papers/draft-04-type-transition-causal-sets/TODO.md` (placeholder defekt). Klíčová
literatura (vše už v projektu, ŽÁDNÉ nové ID): CLPW 2206.10780 (dS II₁), Witten 2112.12828 /
CPW 2209.10454 (II_∞), Kudler-Flam et al. 2309.15897 (S_gen = vN entropie na Killingově horizontu),
De Vuyst et al. 2412.15502 (QRF = crossed product), Surya-X-Yazdi 2008.07697 (area-law rank),
Sorkin-Yazdi 1611.10281 (SSEE), Benincasa-Dowker 1001.2725 (BD d'Alembertián), dS SJ 1306.3231,
Casini-Huerta 0905.2562 (modulární energie).*
