# Brainstorming 03 (2026-06-06)

> **Status oproti BRAINSTORM-02:** druhé kolo postavilo confidence na tvrdá data
> (novelty-checky + výpočty VYPOCET-01…04 + dossiery H01–H03) a uzavřelo rozhodující blok
> (VYPOCET-05…07, findings.json). **Třetí kolo** přidalo *geometrickou robustnost* (Kerr
> ekvatoriální SJ, VYPOCET-08), *přerámování objektu* (H04 entropy-cluster: link matrix →
> BD d'Alembertián), *konsolidaci grafu* (pilíř 19 von Neumannových algeber, 27 konceptů,
> 32 ověřených referencí; modular-hamiltonian je teď TOP HUB) a *první draft* k publikaci
> (papers/draft-01-sj-rotating-spacetimes/). Confidence zde už zohledňuje **tři kola
> selekce** — co přežilo, přežilo opakované pokusy o popravu.

---

## Bilance: co žije, co zemřelo

Tabule všech klastrů/hypotéz po třech kolech. Symboly: ✓✓ = silně potvrzeno + nepokryté
území; ✓ = potvrzené jádro; ⚠️ = přežívá oslabeno/podmíněně; ⚰️ = mrtvé (jako pozitivní
hypotéza); → = přeformulováno na něco testovatelnějšího.

| # | Klastr / hypotéza | Stav po 3 kolech | Co rozhodlo | Co zbývá živé |
|---|---|---|---|---|
| 1 | **SJ na rotujících ČD** (H02 → H2g-6) | **✓✓** | VYPOCET-05 (BTZ ergoregion, strojová přesnost) + **VYPOCET-08 (Kerr ekvatoriál)**: VŠECHNY čtyři BTZ signatury replikují na Kerru. SJ existuje strojově přesně uvnitř ergoregionu (787±/790± páry, rezid. ~5e-16) kde je statický řez Euklidovský; vnitřní null-slope mizí **EXAKTNĚ** na r_erg=2M (a=0,6 i 0,9); opačná znaménka A_caus>0 vs. A_W<0 na každém (a,r); A_caus roste monotónně se spinem (0,197/0,361/0,482 pro a=0,3/0,6/0,9). | **Geometrie-nezávislé SJ vlastnosti** ve strhávaných prostoročasech. Draft-01 napsán. Nepokryté území literatury. |
| 2 | **a₄ NCG ↔ anomálie** (L1-1 → H2g-2) | **✓ (fermiony) / ⚰️ (plná SM)** | VYPOCET-02: fermionový sektor `c/(−a)=−18/11` **EXAKTNÍ** (45 i 48 fermionů); plná SM s bosony falzifikována (−0,853 vs. −1,636). | Fermionová identita = nejpevnější aktivum, kandidát na draft-02 (krátká exaktní nota). |
| 3 | **SSEE / entropy-cluster** (H2g-3 → H04) | **✓ (2D) / ⚠️ (4D)** | VYPOCET-04: 2D čistý `ε~ρ^(−1/2)`, p=0,519±0,007, ρ^(−1/4) vyloučeno na **39σ**. VYPOCET-06: 4D **NEpotvrzeno** (volume law R²=0,998, p cutoff-závislé 0,65–0,98). | H04 reframe: 4D link-matrix spektrum ploché ⇒ interpretace (b): **špatný OBJEKT**, BD d'Alembertián je správný kandidát (VYPOCET-09). |
| 4 | **BMV diskriminátor** (H03 → H2g-8) | **→ binární** | VYPOCET-07: AS korekce ~6,2e-28, EFT ~3,4e-62 (24 resp. 59 řádů pod dosahem). | Binární test (GIE ano/ne) dosažitelný **2030–2035**; Oppenheim křížová korelace principiálně přístupná. Spojité diskriminátory mrtvé. |
| 5 | **SSEE 2D škálování** (samostatně) | **✓** | `ε~ρ^(−1/2)` na 39σ; čistý mocninový zákon λ_k~1/k; rozlišení entropy-cutoff (p=1/2) vs. discreteness-knee (p=1). | Kandidát na draft-02 (review-note o 2D škálování). |
| 6 | **d_s(z,D,probe) klasifikace** (L3-1 → H2g-1) | **⚠️ (jako klasifikace)** | VYPOCET-01: master `d_s=D/γ` symbolicky ověřen, 12/12; vzorec d_s=1+D/z je known od 2009. | Hodnota = jednotný formalismus + **probe jako třetí osa** + diskriminační interpretace. Tabulka d_s(z,D,probe) = kandidát na review-note. |
| 7 | **Cardy–LQG fixace γ** (L1-3 / H01 → H2g-7) | **⚰️** | Rozhodující čtení: verdikt `program-dead`. Senova IR-univerzalita (1205.0971): log-koeficienty IR-určené, přístupově-nezávislé; LQG dává −2, Eukleid +1,71 — nesouhlasí; Carlip: γ₀ z "obscure combinatorial problem", ne z Cardyho. | Pouze jako **definitivní negativní závěr** (H2g-7): IR-univerzalita strukturálně brání UV-fixaci γ z CFT. Zabíjí i CFT větev H2g-3. |
| 8 | **Λ ~ 1/√V sjednocení** (L1-2 → H2g-4/5) | **⚰️ (silná) / ⚠️ (reframe)** | VYPOCET-03: κ_Sorkin/κ_EDT = **139,6 ≈ 140**, neslučitelné konvencí; ~140× prefaktor mismatch. | Přežívá jen (a) falzifikovatelný prefaktor-test, (b) spekulativní "směnný kurz atomu" H2g-4 (podmíněn swerves-mostem), (c) everpresent Λ + swampland H2g-5. |
| 9 | **Probe/observer-relačnost** (H2g-1) | **⚠️ (hluboký motiv)** | Dvě linie (VYPOCET-01 d_s, VYPOCET-04 entropie) konvergují: geometrická veličina = odpověď na (otázka, sonda). Externí opora: QRF = crossed product (2412.15502). | Riziko: musí přežít Senovu IR-univerzalitu (ne vše je relační). Nyní lze formalizovat přes pilíř 19. |

**Tři klíčové posuny narativu třetího kola:**

1. **SJ-rotace přešla z "živého území" na "robustní jev s draftem".** VYPOCET-08 ukázal, že
   čtyři signatury z BTZ NEjsou artefakt 3D modelu — replikují na Kerru, kvantitativně,
   s exaktními nulami na ergosféře. To je **geometrie-nezávislost**, ne náhoda. Projekt má
   poprvé výsledek, který stojí samostatně bez vazby na "velké sjednocení".

2. **Volba objektu se stala metodickou osou.** H04 explicitně formuloval, že 4D selhání
   entropy-clusteru NENÍ selhání hypotézy, ale **selhání objektu** (link matrix vs. BD
   d'Alembertián). Tatáž logika rozhodla a₄ (fermiony vs. bosony) i Cardy-LQG (log-koeficient
   vs. konstantní člen — žádný z nich nenese γ). **"Měříš špatnou věc" je teď první otázka.**

3. **Pilíř 19 dal modulární teorii čísla a graf.** Po konsolidaci je `modular-hamiltonian`
   TOP HUB grafu (degree 27, 614 nodů / 2437 hran). Crossed-product hrana causal-sets →
   von-Neumann je teď doložena strukturně: SSEE truncace ↔ regularizace zkříženého součinu,
   area gap ↔ aditivní konstanta v S_gen. To dává H2g-3 i H2g-1 **algebraický jazyk**, který
   v kole 2 chyběl.

---

## Lekce z poprav

Tři kola zabila víc hypotéz, než potvrdila. To není neúspěch — je to **kalibrovaný filtr**.
Metodické poučky, které z poprav plynou a které je třeba aplikovat dopředu na hypotézy
třetí generace:

### L-1: Sen-typ univerzalitní argumenty jsou nejrychlejší filtr

Senova IR-univerzalita (1205.0971) zabila Cardy-LQG program *bez jediného výpočtu* — stačil
strukturní argument, že log-korekce jsou určeny IR daty a UV parametr (γ) jimi nelze fixovat.
**Poučka:** než spustíš výpočet, zeptej se, jestli cílová veličina není *chráněná
univerzalitním teorémem* (IR-univerzalita, anomaly-matching, index-teorémy, no-go věty). Pokud
ano, výpočet nemůže nést informaci, kterou hledáš — ať vyjde jakkoli. Tento filtr je levný a
**aplikuje se i na hypotézy třetí generace** (zvlášť na H3g-1: musíme předem vědět, zda opačná
znaménka A_caus/A_W jsou chráněná, nebo dynamická). Sen-typ argument je první obranná linie:
zabíjí dřív, než se utratí čas.

### L-2: Volba objektu rozhoduje — link matrix vs. BD d'Alembertián

Entropy-cluster 4D "selhal" — ale H04 ukázal, že selhal **objekt**, ne hypotéza. Link matice L
(Johnston G_R) je kombinatorický, hustne jako N^0,65, deformuje spektrum pryč od mocninového
zákona; Benincasa-Dowker d'Alembertián je explicitně konstruován pro kontrolované kontinuum-
korekce. Tatáž logika běží napříč korpusem: a₄ platí jen pro **Diracův operátor** (ne pro
plnou algebru s bosony); γ není v **log-koeficientu** (ani v konstantním členu). **Poučka:**
když výsledek nevyjde, ptej se NEJDŘÍV "počítal jsem správný objekt?" než "je hypotéza
mrtvá?". Špatný objekt vypadá jako falzifikace, ale je to jen špatně mířená sonda — což je
přímo H2g-1 (probe-dependence) aplikovaná na sebe sama.

### L-3: Prefaktor ≠ řád — a rozdíl prefaktorů může být měření

VYPOCET-03 ukázal κ_Sorkin/κ_EDT = 140×: sdílí se *dimenzionální kostra* (Λ~H²), ale prefaktory
jsou nesloučitelné. Stejně Λ~1/√V unifikace: dimenzionálně OK, prefaktorem 140× mimo. **Poučka:**
"shoda řádu" není shoda; je to nutná, ne postačující podmínka. A obráceně (H2g-4): pokud dvě
poctivě spočítaná čísla *systematicky* nesedí o pevný faktor, ten faktor sám může být fyzikální
veličina (poměr definičních délek atomu). **Aplikace dopředu:** každé "to zhruba sedí" musí
projít prefaktor-testem; a každý reprodukovatelný nesoulad je kandidát na nový pozorovatelný.

### L-4: Negativní výsledek s plně dokumentovanou konvencí JE aktivum

Tři ze čtyř výpočtů druhého kola falzifikovaly silnou verzi své hypotézy — a přesto jsou
**publikovatelné**, protože to srovnání nikdo v literatuře neudělal (140× Λ, plná-SM a₄, p=1/2
vs. 3/4). **Poučka:** ostrá hranice "platí X, neplatí Y, s touto konvencí" je cennější než vágní
pozitivní tvrzení. Nejlepší výsledek projektu (a₄ fermiony) je právě tohle: čistý pozitivní +
čistý negativní v jednom výpočtu.

---

## Hypotézy třetí generace

Šest zostřených/nových hypotéz. Každá: tvrzení, opora (s čísly z výpočtů), proč nová, test,
confidence. Hypotézy třetí generace jsou *uzší a testovatelnější* než druhá generace — tři kola
selekce zúžila prostor.

### H3g-1 — Opačná znaménka A_caus/A_W jsou superradiantní podpis: SJ vakuum kóduje strhávání v Wightmanově sektoru, ne v kauzálním

**(jádro: mechanismus opačných znamének — nejslabší bod draftu-01)**
**Confidence: medium-high** (jev robustní napříč a, r; mechanismus zatím spekulativní).

- **Tvrdí:** opačné znaménko kauzální asymetrie (A_caus > 0) a Wightmanovy asymetrie (A_W < 0)
  na Kerru/BTZ **není artefakt**, ale fyzikální podpis strhávání (frame-dragging). Konkrétně:
  A_caus měří asymetrii *kauzální* matice (retardovaný − advancovaný Green), která je dána
  geometrií null-kuželů a roste s ω (úhlovou rychlostí strhávání). A_W měří asymetrii *symetrizované
  dvoubodové* funkce SJ stavu, jejíž znaménko je řízeno **kladností SJ projektoru** A = iΔ na
  L²(M′) — a superradiantní módy (záporná KG-norma) vstupují do W s opačnou váhou než do Δ. SJ
  vakuum tedy "vidí" strhávání **dvakrát, s opačnými znaménky**: jednou jako kauzální orientaci,
  jednou jako spektrální obsazení.
- **Opora (čísla):** VYPOCET-08 — opačná znaménka na **každém** (a,r): a=0,6 r=2,6 dává
  +0,317/−0,296; a=0,9 dává +0,431/−0,382. A_caus roste monotónně se spinem (0,197/0,361/0,482).
  Vnitřní null-slope mizí EXAKTNĚ na r_erg=2M (a=0,6 i 0,9) — tj. přechod znaménka je vázán na
  geometrickou hranici ergosféry, ne na arbitrární škálu. VYPOCET-05 (BTZ): A_caus +1,000 uvnitř
  vs. +0,007 vně.
- **Proč nová:** SJ stav na rotující ČD je nepokryté území (preprint-check: "genuinely open
  territory"); opačná znaménka A_caus/A_W nebyla nikde popsána, natož vysvětlena. Draft-01
  self-assessment je explicitně označuje jako **nejslabší bod** — chybí mechanismus. Toto je
  první pokus o mechanismus.
- **Test:** (a) **Analytický model na 2D rotujícím toy-modelu** (Rindler-like s konstantní ω):
  spočítat A_caus a A_W v uzavřené formě a ověřit, zda znaménko A_W flipuje přesně tam, kde KG-
  norma up-módů mění znaménko (superradiantní práh Ω_H). (b) **Eigenvektorová dekompozice** (směr
  z VYPOCET-05): rozložit A_W do příspěvků jednotlivých SJ eigenvektorů a ukázat, že záporný
  příspěvek pochází *výhradně* od módů s ω < mΩ_H. Pokud A_W flipuje na superradiantním prahu a
  ne na ergosféře, mechanismus je potvrzen; pokud flipuje na ergosféře (jako A_caus null-slope),
  jde o tutéž geometrickou příčinu a hypotéza o "dvojím vidění" padá.
- **Co by dalo:** uzavřel by nejslabší bod draftu-01 a povýšil "pozorovaný jev" na "vysvětlený
  jev" — to je rozdíl mezi review-note a plnohodnotným paperem. Navíc: kovariantní entanglement
  entropie pro rotující ČD by zdědila znaménkovou strukturu superradiance.
- **Riziko (L-1):** musíme předem ověřit, že znaménko A_W není chráněno triviálním
  antisymetrickým argumentem (Δ je antisymetrický z definice). Pokud je opačné znaménko pouhý
  důsledek toho, že Δ = G_R − G_A je vždy antisymetrický, není to fyzika strhávání, ale algebra —
  Sen-typ filtr to musí vyloučit jako první krok.

### H3g-2 — BD d'Alembertián obnoví area-law spektrum ve 4D: entropy-cluster je objekt-specifický, ne dimenze-specifický

**(jádro: BD-objekt verze entropy-clusteru, H04 interpretace 2b → VYPOCET-09)**
**Confidence: medium** (motivovaná spekulace; výpočet náročný, výsledek nezaručený).

- **Tvrdí:** 4D selhání entropy-clusteru (volume law, ploché spektrum, p cutoff-závislé) je
  **specifické pro link matici L**, ne obecná vlastnost 4D kauzálních setů. Pauli-Jordanův operátor
  iΔ^BD zkonstruovaný z **Benincasa-Dowker d'Alembertiánu** (0911.2563; 1507.00330) — ne z link
  matice — dá ve 4D čistší mocninový zákon λ_k ~ k^α s ostrým kolenem a robustní rank-škálování
  blíže p = 3/4. Důvod: BD operátor je hermitovský, explicitně konstruovaný s Gaussovými vahami
  přes škálu ~ρ^(−1/4) (4D), tlumí vysokofrekvenční módy *kontrolovaně*, kdežto L jen kombinatoricky
  hustne.
- **Opora (čísla):** VYPOCET-04 (2D, kde G_R = C přímo, bez husté link matice): čisté `ε~ρ^(−1/2)`,
  p=0,519±0,007, 39σ. VYPOCET-06 (4D, link matrix): p rozptýleno 0,65–0,98 podle cutoffu, volume law
  R²=0,998 — **přesně to selhání, které BD má opravit**. Belenchia et al. 1507.00330: BD sonda dává
  univerzální d_s→2 ve **všech** dimenzích (na rozdíl od random-walk, který roste) — důkaz, že BD
  operátor má kvalitativně jiné, čistší spektrum než kombinatorické alternativy.
- **Proč nová:** entropy-cluster novelty = pursue; trojcestná identifikace (SSEE truncace =
  crossed-product cutoff = LQG area gap) v literatuře chybí. SSEE z BD Greenovy funkce ve 4D nebyla
  nikdy spočítána — H04 §2b ji navrhuje jako VYPOCET-09. Je to **přímá aplikace L-2** (volba objektu)
  na nejdražší otevřený výpočet projektu.
- **Test (= VYPOCET-09):** implementovat BD kernel B₄φ na 4D sprinklovaném diamantu, zkonstruovat
  G_R^BD = B₄⁻¹ (Moore-Penrose / iterativní solver), sestavit iΔ^BD = i(G_R^BD − (G_R^BD)^T),
  diagonalizovat, změřit tvar spektra a rank-škálování. **Predikce:** robustní p ≈ 3/4 s ostrým
  kolenem. Pokud BD spektrum zůstane ploché a p nerobustní → selhání je obecné pro 4D kauzální set,
  ne objekt-specifické, a hypotéza H2g-3 je ve 4D mrtvá (přežívá jen 2D sanity-check). Rychlejší
  předtest: VYPOCET-09a (3D link matrix) — pokud 3D dá čistší spektrum než 4D, problém je dimenze-
  gradient, ne binární 2D-výjimka.
- **Riziko (L-2 obráceně):** není a priori zaručeno, že BD spektrum bude čistší — je to motivovaná
  spekulace. Výpočet G_R^BD je výrazně náročnější než link matice (nelokální Gaussovy kernely, N≥5000
  pro konvergenci). Navíc interpretace 2c (volume law = non-Hadamardovost SJ stavu na diamantu, ne
  chybějící cutoff) může platit **zároveň** — pak BD nepomůže a správná otázka je geometrie (Rindler/
  slab místo diamantu).

### H3g-3 — SSEE truncace JE crossed-product modulární cutoff: type III₁ → type II přechod s konkrétními čísly z pilíře 19

**(jádro: modulární teorie × SSEE × SJ s daty pilíře 19; crossed-product hrana s čísly)**
**Confidence: medium** (most je teď strukturně doložen, ale kvantitativní identifikace zbývá).

- **Tvrdí:** geometrická truncace v Sorkinově SSEE (odstranění módů blízkých nule, jež mění
  volume→area law) **je tatáž operace** jako crossed-product regularizace, jež převádí lokální
  algebru typu III₁ (bezstopová, divergentní entropie) na typ II (stopa, konečná S_gen). Konkrétně:
  (a) entropy-cutoff rank p=1/2 ve 2D = škála, na níž SJ projektor A=iΔ ztrácí stopu; (b) přidání
  pozorovatele/hodin (L²(ℝ) = jeden stupeň volnosti) v crossed-productu = výběr modulárního cutoffu;
  (c) area gap LQG (ΔA ~ ℓ_Pl²) = aditivní konstanta v S_gen, kterou stopa typu II fixuje jen relativně.
- **Opora (čísla + pilíř 19):** VYPOCET-04 — truncace mění S = 95,2 (volume, type-III-like, divergentní
  stopa) → 1,58 (area/log, type-II-like, konečná stopa); entropy-cutoff p=1/2 vs. discreteness-knee p=1
  jsou **dvě fyzicky odlišné škály** (F-006 vs. F-007). Pilíř 19 (nově konsolidovaný): crossed-product
  hrana causal-sets → von-Neumann je strukturně doložena — `S_gen = ⟨A⟩/4G_N + S_out + const`, kde
  type II definuje entropii *jen až na aditivní konstantu*, a tato konstanta je "přesně regularizačně
  závislá konstanta v S_gen". Modular-hamiltonian je TOP HUB (degree 27). De Vuyst et al. 2412.15502:
  QRF = crossed product → entropie závislá na pozorovateli.
- **Proč nová:** otevřený problém #6 pilíře 19 explicitně: "Odvodit (ne jen předepsat) geometrickou
  truncaci nutnou pro plošný zákon SSEE a vztáhnout ji k regulované entropii typu II" — označeno jako
  **most k živé hypotéze**. Hrana von-Neumann → loop-quantum-gravity (area gap ↔ stopa typu II) je v
  digestu "sotva prozkoumáno / kandidát na nové propojení". Žádná práce neztotožňuje SSEE truncační rank
  s modulárním cutoffem **číselně**.
- **Test:** (a) **Algebraický:** spočítat *typ von Neumannovy algebry* implikovaný SJ projektorem před
  a po truncaci — predikce: III-like (bez stopy) → II_∞ (se stopou) přesně na entropy-cutoff rank p=1/2,
  ne na discreteness-knee p=1. (b) **Číselná identifikace:** porovnat aditivní konstantu v S_gen
  (z type-II stopy) s area gap normalizací — má-li most platit, musí truncační škála ε~ρ^(−1/2)
  odpovídat modulárnímu cutoffu crossed-productu se stejnou stopovou normalizací. (c) Test, zda
  *dvě různé sondy* (entropy-cutoff vs. discreteness-knee) odpovídají *dvěma různým QRF* (různé
  hodiny → různé algebry typu II → různé entropie, dle 2412.15502) — to by spojilo H3g-3 s H3g-5.
- **Co by dalo:** první číselný most mezi causal-set SSEE a crossed-product programem — dvě "sotva
  prozkoumané" hrany grafu najednou. Povýšilo by H2g-3 z "numericky nahlodáno" na "algebraicky
  identifikováno".
- **Riziko:** VYPOCET-06 oslabil 4D větev (volume law, p nerobustní); kvantitativní identifikace
  závisí na výsledku H3g-2 (BD objekt). Ve 4D může most platit jen v Rindler/slab geometrii (kde je
  SJ stav Hadamardův), ne na diamantu — pak je identifikace geometrie-podmíněná.

### H3g-4 — Fermionový a₄ podpis říká, že spektrální akce JE fermionově-indukovaná gravitace: bosony nejsou ve hře, protože gravitace se rodí z Diracova determinantu

**(jádro: a₄ fermionová identita — PROČ přesně fermionový sektor; spektrální akce jako fermionově-indukovaná gravitace)**
**Confidence: high** (výpočet uzavřený; interpretace nová, ale silně motivovaná).

- **Tvrdí:** to, že shoda `c/(−a) = −18/11` platí **přesně a jen** ve fermionovém sektoru (a bosony
  ji rozbíjejí), není slabina, ale **odhalení mechanismu**: NCG spektrální akce Tr f(D/Λ) je
  funkcí *výhradně Diracova operátoru D*, takže její gravitační členy (C², Euler) pocházejí z heat-
  kernelu D² — což je **fermionová smyčka**. Spektrální akce je tedy doslova **Sacharovova
  indukovaná gravitace s fermiony jako jediným zdrojem**: Einstein-Hilbert + Weyl² členy jsou
  vakuová polarizace Diracova moře, ne nezávislé pole. Bosony do C²/Euler nepřispívají, protože
  v NCG nejsou fundamentální — jsou to *fluktuace téhož D* (vnitřní fluktuace metriky), ne
  samostatná dynamická pole s vlastním a₄. Proto se shoda omezuje na fermiony **strukturně**, ne
  náhodou.
- **Opora (čísla):** VYPOCET-02 — `koef(C²)/koef(Euler) = −18/11` spektrální akce = c/(−a) Weylova
  fermionu, EXAKTNĚ, pro 45 i 48 fermionů. Faktor 11 sdílen v **obou** (spektrální Euler 11/60,
  anomálie a_Weyl=11/720) — to je otisk téhož Diracova a₄. Plná SM s bosony: −0,853/−0,866 vs.
  −1,636 → bosony mají c/(−a) = −3 (vektor) a −18/31 (skalár), tj. **jiný heat-kernel zdroj** →
  shodu rozbíjejí přesně proto, že nejsou fermionové smyčky.
- **Proč nová:** F-003 noveltyStatus — dvoustranné vazby (spektrální akce ↔ Weyl anomálie)
  publikovány (Andrianov-Lizzi, Kurkov-Lizzi), ale **interpretace fermionové výlučnosti jako
  důkazu Sacharovovy fermionově-indukované gravitace** nikde není. Digest: hrana
  noncommutative-geometry → emergent-gravity je "minimal-length/UV-cutoff resonance, almost no
  direct work links Jacobson/Sakharov". Toto ji vyplňuje s *koeficientovou* (ne analogickou)
  identitou.
- **Test:** (a) **Graviton/Weyl sektor** (levný, hodiny — navazuje na hotový VYPOCET-02): zahrnout
  c/(−a) gravitonu do bilance. Predikce: pokud je spektrální akce čistě fermionově-indukovaná,
  graviton **nesmí** plnou shodu zachránit (není v Diracově determinantu) — shoda zůstane jen
  fermionová. Pokud graviton shodu uzavře, hypotéza o čistě fermionovém původu padá. (b) **Index-
  teorém test (L-1):** ověřit, zda je −18/11 *vynucené* Diracovým operátorem obecně (jakákoli
  spektrální trojice s fermiony dá −18/11), nebo specifické pro C⊕H⊕M₃(C). Pokud univerzální →
  je to chráněná veličina (anomaly-matching) → spektrální akce nemůže být nic jiného než fermionová
  indukce.
- **Co by dalo:** povýšilo by F-003 z "zajímavá koincidence koeficientů" na "spektrální akce =
  fermionově-indukovaná gravitace, dokázáno přes a₄". To je **fyzikální tvrzení o původu gravitace
  v NCG**, ne jen numerická shoda — a je to kandidát na samostatnou exaktní notu (draft-02).
- **Riziko:** "indukovaná gravitace" má v NCG subtilní status (kosmologická konstanta, hierarchie
  škál Λ). Interpretace musí přežít, že spektrální akce obsahuje *i* kosmologický a Higgs člen, ne
  jen R + C².

### H3g-5 — Probe = QRF: dvě sondy téže geometrie jsou dva kvantové referenční rámce, a jejich neshoda je crossed-product, ne chyba

**(zostření H2g-1 daty pilíře 19)**
**Confidence: medium-high** (most teď doložen pilířem 19; čeká na druhý příklad mimo d_s).

- **Tvrdí:** probe-dependence (VYPOCET-01: d_s=2 d'Alembertiánem vs. >D random-walkem; VYPOCET-04:
  entropy-cutoff p=1/2 vs. discreteness-knee p=1) je **speciální případ** toho, že kvantový
  referenční rámec = zkřížený součin (De Vuyst et al. 2412.15502). Různá sonda = různý pozorovatel
  = různá algebra typu II = různá veličina. Neshoda dvou sond NENÍ chyba měření ani vnitřní rozpor
  korpusu, ale **kovariantní fakt**: invariantní je relativní entropie / relativní dimenze, ne
  absolutní hodnota. To "rozpouští" mezipřístupové konflikty, které jsou ve skutečnosti konflikty sond.
- **Opora (čísla + pilíř 19):** VYPOCET-01 — CST dává d_s=2 i >D ze stejné teorie (vyřešilo rozpor
  edge 501 vs. 1539, F-002). VYPOCET-04 — dvě fyzicky odlišné škály p=1/2 a p=1 z téhož spektra
  (F-006, F-007). Pilíř 19: "různé QRF → různé algebry typu II → různé entropie; gravitační entropie
  je závislá na pozorovateli; **invariantní je relativní entropie**" (otevřený problém #2: objektivní
  obsah gravitační entropie). Modular-hamiltonian TOP HUB dává tomu grafový základ.
- **Proč nová:** H2g-1 v kole 2 generalizovala probe-dependence napříč veličinami, ale **bez
  algebraického jazyka**. Pilíř 19 ho teď dodává: probe ↔ QRF ↔ crossed product je řetěz, který v
  kole 2 nebyl k dispozici. Žádná práce neztotožňuje *výpočetní volbu sondy* (d'Alembertián vs.
  random-walk) s *volbou QRF* v crossed-product smyslu.
- **Test:** (a) najít **třetí** veličinu (mimo d_s a SSEE), která dá protichůdné odpovědi pro různé
  sondy, a ukázat, že její dvě hodnoty jsou spojeny crossed-productem (relativní veličina invariantní).
  Kandidát: geodetická vs. kauzální vzdálenost na causetu, nebo Hausdorffova vs. spektrální dimenze.
  (b) Formálně: spočítat, zda dvě sondy d_s = D/γ pro různá γ odpovídají dvěma algebrám lišícím se
  modulárním tokem (tj. zda γ-volba = volba σ_t). Pokud ano, probe-osa je doslova modulární-tok-osa.
- **Riziko (L-1):** Senova IR-univerzalita je tvrdá hranice — některé veličiny (log-korekce) jsou
  IR-určené a **žádná** sonda jimi nehne. Hypotéza musí ostře oddělit UV-relační (sonda-závislé) od
  IR-univerzálních (sonda-nezávislé) veličin, jinak je formulována příliš hrubě a kolabuje na H2g-7.

### H3g-6 — Geometrie-nezávislost SJ vlastností je univerzální podpis strhávání, ne vlastnost konkrétní metriky

**(zobecnění VYPOCET-08)**
**Confidence: medium-high** (silně doloženo BTZ↔Kerr replikací; chybí třetí geometrie).

- **Tvrdí:** čtyři SJ signatury (existence uvnitř ergoregionu kde je statický řez Euklidovský;
  exaktní null-slope nula na ergosféře; opačná znaménka A_caus/A_W; monotónní růst A_caus se spinem)
  jsou **geometrie-nezávislé** — určené jen *přítomností strhávání* (ω ≠ 0), ne konkrétní metrikou.
  BTZ (3D, záporná Λ) a Kerr (4D, asymptoticky plochý) jsou maximálně odlišné rotující prostoročasy,
  a přesto dávají kvalitativně i kvantitativně tytéž signatury. To naznačuje, že SJ konstrukce
  detekuje **topologicko-kauzální** vlastnost strhávání (orientovaný null-kužel + superradiantní
  spektrum), ne lokální geometrii.
- **Opora (čísla):** VYPOCET-08 — všechny čtyři BTZ signatury replikují na Kerru; null-slope mizí
  EXAKTNĚ na r_erg=2M pro a=0,6 i 0,9 (ne přibližně — exaktně, vázáno na geometrickou hranici);
  A_caus monotónní 0,197/0,361/0,482 se spinem 0,3/0,6/0,9. VYPOCET-05 — BTZ baseline strojově přesně
  (787±/790± páry, rezid. ~5e-16).
- **Proč nová:** SJ na rotujících ČD je nepokryté území; *srovnání* dvou geometrií a tvrzení o
  geometrie-nezávislosti je o krok dál než kterýkoli jednotlivý výpočet. Draft-01 to dokumentuje,
  ale neformuluje jako univerzalitní tvrzení — to je zde.
- **Test:** **třetí geometrie** — rotující BTZ s jinou Λ, nebo Kerr-AdS, nebo Kerr-Newman (nabitý).
  Predikce: tytéž čtyři signatury, s null-slope nulou na ergosféře dané příslušnou metrikou. Pokud
  některá signatura zmizí nebo změní znaménko při změně asymptotiky (Λ, náboj), geometrie-nezávislost
  padá a jde o vlastnost specifické třídy. **Levnější test:** Kerr s extrémním spinem a→1 — chování
  signatur v limitě, kde ergosféra a horizont splývají.
- **Vazba na H3g-1:** geometrie-nezávislost činí mechanismus opačných znamének (H3g-1) *naléhavějším*
  — pokud je jev univerzální, musí mít univerzální příčinu (superradiantní práh), ne metrika-specifickou.
  Tyto dvě hypotézy je nutné testovat společně: H3g-1 dodá mechanismus, H3g-6 jeho univerzalitu.

---

## Výpočetní fronta v2

Seřazeno podle (decisiveness × proveditelnost × novost). **Běží v tomto kole:** VYPOCET-09 (BD 4D),
VYPOCET-10 (superradiance eigenvektory). Fronta určuje, co po nich.

| # | Výpočet | Hypotéza | Náročnost | Co rozhodne | Stav |
|---|---|---|---|---|---|
| — | **VYPOCET-09 — BD d'Alembertián 4D SSEE** | H3g-2 | týdny | Robustní p≈3/4 vs. ploché spektrum: objekt-specifické vs. dimenze-specifické selhání entropy-clusteru | **běží** |
| — | **VYPOCET-10 — superradiance eigenvektory** (A_W dekompozice) | H3g-1 | dny–týden | Flipuje A_W na superradiantním prahu (ω=mΩ_H) nebo na ergosféře? Mechanismus opačných znamének | **běží** |
| 1 | **a₄ + graviton/Weyl sektor** do C⊕H⊕M₃(C) bilance | H3g-4 | **hodiny** | Zda graviton zachrání plnou shodu (→ne fermionová indukce) nebo ne (→spektrální akce = fermionově-indukovaná gravitace). Nejlevnější, navazuje na VYPOCET-02. **Nejvyšší výnos/náklad.** | další |
| 2 | **Analytický 2D rotující toy-model** A_caus/A_W (Rindler s konstantní ω) | H3g-1 | dny | Uzavřená forma znamének; ověří mechanismus z VYPOCET-10 analyticky; odstraní L-1 riziko (antisymetrie Δ) | další |
| 3 | **vN algebra typ** SJ projektoru před/po truncaci (III→II přechod) | H3g-3 | dny | Type III (bez stopy) → II_∞ (se stopou) přesně na p=1/2 rank? Číselný most SSEE↔crossed-product | další |
| 4 | **VYPOCET-09a — 3D link-matrix SSEE** (předtest BD) | H3g-2 | dny | Dimenze-gradient vs. 2D-výjimka; rychlé rozhodnutí, zda je 4D selhání objekt- nebo dimenze-specifické | další |
| 5 | **Třetí geometrie SJ** (Kerr-AdS / Kerr-Newman / extrémní a→1) | H3g-6 | týden | Geometrie-nezávislost: přežijí signatury změnu Λ/náboje/extrémního spinu? | další |
| 6 | **Třetí probe-veličina** (geodetická vs. kauzální vzdálenost) + crossed-product test | H3g-5 | dny–týden | Druhý příklad probe=QRF mimo d_s; rozpustí mezipřístupový konflikt jako konflikt sond | další |
| 7 | **Index-teorém test −18/11** (univerzální vs. C⊕H⊕M₃(C)-specifické) | H3g-4 | dny | Zda je fermionová shoda chráněná (anomaly-matching) → spektrální akce nemůže být nic než fermionová indukce | další |
| 8 | **Aditivní konstanta S_gen ↔ area gap** normalizace | H3g-3 | dny | Číselná identifikace truncační škály s modulárním cutoffem; druhý vrchol trojcestné identifikace | další |

**Doporučené pořadí po doběhnutí 09/10:** #1 (hodiny, nejlevnější, rozhoduje H3g-4) a #2
(analytická opora pro VYPOCET-10) paralelně; pak #3 (algebraický most, navazuje na pilíř 19);
pak #4 nebo #5 podle výsledku VYPOCET-09.

---

## Strategie publikace

**Draft-01 hotov:** `papers/draft-01-sj-rotating-spacetimes/` (draft.md v0.1 + TODO.md).
Nejsilnější aktivum, nepokryté území, dvě geometrie. **Nejslabší bod (per self-assessment):
mechanismus opačných znamének A_caus/A_W chybí** — to řeší VYPOCET-10 + H3g-1. Draft-01 by se
neměl uzavírat, dokud VYPOCET-10 nedodá mechanismus; jinak recenzent narazí přesně na tu díru.

### Doporučení pro draft-02

Tři kandidáti, seřazeni podle (hotovost × novost × samostatnost):

1. **★ DOPORUČENO: a₄ fermionová identita — krátká exaktní nota.**
   **Proč:** nejpevnější aktivum projektu (VYPOCET-02 hotový, exaktní racionální aritmetika, čistý
   pozitivní −18/11 + čistý negativní plná-SM v jednom). Novelty-check potvrdil, že anomaly-matching
   pro C⊕H⊕M₃(C) nikdo neudělal (F-003/F-004). S H3g-4 navíc dostává **fyzikální interpretaci**
   (spektrální akce = fermionově-indukovaná gravitace), ne jen numerickou shodu. Formát exaktní noty
   sedí na uzavřený výpočet s plně dokumentovanou konvencí. **Blokátor:** rychle doběhnout výpočet #1
   (graviton sektor, hodiny) a #7 (index-teorém test) — uzavřou interpretaci a odolají recenzentově
   otázce "proč zrovna fermiony?".

2. **d_s(z,D,probe) klasifikační tabulka — review-note.**
   **Proč:** VYPOCET-01 hotový (12/12), jednotný formalismus přes 4+ přístupy, probe jako třetí osa
   je projektově-originální (F-001). Defenzivně poctivé (vzorec known od 2009, prodává se
   systematičnost + probe-osa + diskriminační čtení). Review-note formát sedí na "klasifikace, ne
   objev". **Riziko:** nižší novost (vzorec publikován); hodnota je v syntéze, ne v objevu — review,
   ne letter.

3. **SSEE 2D škálování — review-note nebo letter.**
   **Proč:** `ε~ρ^(−1/2)` na 39σ, čisté rozlišení entropy-cutoff (p=1/2) vs. discreteness-knee (p=1)
   je projektově-originální (F-006/F-007/F-008). **Riziko:** jen 2D, bezhmotný skalár; 4D zatím
   nerobustní (VYPOCET-06). Měl by čekat na VYPOCET-09 (BD 4D) — pokud BD dá 4D výsledek, nota se
   rozšíří z "2D sanity-check" na "2D čisté + 4D objekt-závislé"; pokud ne, zůstává poctivá 2D nota.

**Strategický závěr:** draft-02 = **a₄ fermionová nota** (nejhotovější, nejnovější, s novou
interpretací z H3g-4). draft-01 (SJ-rotace) uzavřít až po VYPOCET-10. d_s tabulka a SSEE 2D jako
draft-03/04 review-notes, SSEE až po VYPOCET-09.

---

*Anchory třetího kola: `core-data/calculations/VYPOCET-08/` (Kerr ekvatoriál); `VYPOCET-09/`
(BD 4D, běží), `VYPOCET-10/` (superradiance eigenvektory, běží); `knowledge-base/hypotezy/
H04-entropy-cluster-reframe.md`; `knowledge-base/foundations/19-von-neumann-algebras.md`;
`papers/draft-01-sj-rotating-spacetimes/`; `core-data/findings.json` (F-001…F-008);
`core-data/_digest.md` (modular-hamiltonian TOP HUB, 614 nodů/2437 hran).*
