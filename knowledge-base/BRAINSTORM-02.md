# Brainstorming 02: Druhé kolo (2026-06-06)

> **Status oproti BRAINSTORM-01:** první kolo bylo *bez kontroly proti literatuře* —
> confidence vyjadřovala jen vnitřní oporu v `core-data/`. Druhé kolo staví na
> **tvrdých datech**: šest novelty-checků proti arXiv (`core-data/novelty-checks.json`),
> vyřešený d_s rozpor (probe-dependence potvrzena), **čtyři dokončené výpočty**
> (`knowledge-base/vypocty/VYPOCET-01…04`), tři dossiery
> (`knowledge-base/hypotezy/H01…H03`) a dvě eseje (`knowledge-base/eseje/`).
> Confidence zde už zohledňuje **i** verdikt novelty-checku a výsledek výpočtu —
> je proto kalibrovanější a místy nemilosrdnější než v prvním kole.

---

## Co se změnilo od BRAINSTORM-01

Jediná tabulka: pro každý klastr verdikt novelty-checku **a** výsledek výpočtu, který
ho mezitím prošel (nebo zatím neprošel).

| Klastr (hypotéza) | Novelty verdikt | Doporučení | Výpočet | Co výpočet udělal | Nový status |
|---|---|---|---|---|---|
| **d_s** (L3-1+L2-5+L5-5) | partially-known | reframe | **VYPOCET-01** ✓ | Symbolicky ověřil master `d_s^UV = D/γ`; 12/12 numerických kontrol; probe-dependence doložena (CST: d'Alembert→2 vs. random-walk→>D) | **PŘERÁMOVÁNO + POTVRZENO** (jako klasifikace, ne objev vzorce) |
| **a_4** (L1-1+L2-4+L5-4) | partially-known | **pursue** | **VYPOCET-02** ✓ | Fermionový sektor `c/(−a)=−18/11` EXAKTNÍ (45 i 48 fermionů); plná SM s bosony **falzifikována** (−0,853 vs. −1,636) | **ROZDVOJENO**: jádro potvrzeno, silná verze mrtvá |
| **Λ ~ 1/√V** (L1-2+L3-2+L2-2) | partially-known | reframe | **VYPOCET-03** ✓ | Prefaktory κ se liší **140×** (Sorkin 0,21 vs. EDT 1,5·10⁻³), neslučitelné konvencí; CosMIn nemá κ | **SILNÁ VERZE VYVRÁCENA**; přežívá jen falzifik. prefaktor-test + reframe |
| **Entropie/crossed-product** (L2-3+L3-4+L4-4) | partially-known | **pursue** | **VYPOCET-04** ✓ | SSEE: volume-law 95,2 → truncace → area/log 1,58; cutoff škáluje `ε~ρ^(−1/2)` (p=0,519±0,007), **vylučuje** ρ^(−1/4) na 39 σ | **MECHANICKY PODPOŘENO** (2D); 4D + γ-identifikace zbývá |
| **Cardy-LQG** (L1-3 / H01) | partially-known | reframe | dossier **H01** | Jádro `c=6k` je known (Carlip 1410.5763); zbývají 2 body: γ↔c=6Q₁Q₅ a log-fixace γ; **blocker: Senova IR-univerzalita** | **OSLABENO**: priorita dolů, blocker identifikován |
| **SJ-Kerr** (L5-3 / H02) | partially-known | reframe | dossier **H02** | SJ pro Kerr/SdS = **nepokryté území**; Kay-Wald no-go SJ neblokuje (nevyžaduje symetrii); 3 strategie, doporučen 2D analog | **OTEVŘENO, ŽIVÉ** — žádná prior art na rotující ČD |
| **BMV-diskriminátor** (L4-5/L4-6 / H03) | partially-known | reframe | dossier **H03** | Framing „diskriminátor přístupů, ne Q vs. C" je nový; AS korekce ~10⁻⁶⁰ neměřitelná; **Oppenheim postkvant** je jediný principiálně odlišitelný (π-fázový posun) | **PŘEFORMULOVÁNO**: binary test je mrtvý, diskriminace přístupů žije |
| **No-global-sym vs. AS** (L4-2) | partially-known | reframe | — | Basile et al. 2502.12290 už konflikt mapují; nové je jen konkrétní FRG koeficient | čeká na výpočet |
| **NCG↔Liouville** (L2-1) | partially-known | reframe | — | Dvoustranná NCG↔Liouville publikována (Khalkhali); trojstranné NCG=GFT=CDT chybí; různé Dirac-modely = různé třídy | čeká na výpočet |
| **WGC vs. d_s→2** (L4-6) | partially-known | (nový výpočet) | — | 1/p⁴ AS propagátor do Hamada-Noumi-Shiu = nepublikovaný výpočet znaménka δ(Q/M) | čeká na výpočet |

**Klíčové posuny v narativu:**
1. **„Konvergence" je mrtvá jako sjednocující motiv.** Tři ze čtyř výpočtů (01, 02, 03)
   shodně ukazují, že zdánlivé shody jsou buď **klasifikace** (d_s podle γ a sondy),
   **podshody jednoho sektoru** (a_4 jen ve fermionech), nebo **intrinsicky různá čísla**
   (Λ-prefaktory 140×). Projekt by měl přestat hledat „velké sjednocení" a začít
   prodávat **přesné diskriminátory a falzifikace**.
2. **Probe/observer/cutoff jako klasifikační osa** je nově doložená napříč výpočty 01 a 04
   — to je nejsilnější emergentní motiv druhého kola (formalizováno níže jako H2g-1).
3. **Falzifikace je výsledek, ne selhání.** VYPOCET-03 (140×) a VYPOCET-02 (plná SM)
   jsou *publikovatelné negativní* výsledky — v literatuře nikdo to srovnání neudělal.

---

## Vyhodnocení výpočtů

Nemilosrdně poctivě: co každý výpočet *udělal* s hypotézou.

### VYPOCET-01 (d_s klasifikace) — PŘERÁMOVAL a ČÁSTEČNĚ POTVRDIL
**Co udělal:** master `d_s^UV = D/γ` je symbolicky verifikovaný (sympy) a všech 12
numerických kontrol prošlo (tol 0,06). Reprodukuje Hořavu (z=2→5/2, z=3→2), Stelle (2),
AS (2), causal-set d'Alembertián (2 univerzálně) i random-walk (>D). **Zdánlivá
univerzalita „d_s→2" je optický klam** — shoda podtřídy γ=2 (propagátor ~k⁴); GR (4),
Hořava z=2 (5/2) a random-walk (>D) ji explicitně porušují.
**Poctivé omezení:** novelty-check je tvrdý — **vzorec d_s=1+D/z je publikován od 2009
(Hořava)**, takže hypotéza NEMŮŽE být objev vzorce. Co zbývá nové: (a) jednotný
formalismus P(σ) přes 4 přístupy najednou, (b) **sonda jako třetí osa** (doloženo
tím, že CST dává 2 i >D ze stejné teorie — to zároveň řeší rozpor connections 657 vs.
1777), (c) interpretace jako diskriminátor. **Random-walk hodnota „8" je ilustrativní**
(Eichhorn-Mizera nezveřejnili konstantu) — robustní je jen „roste", ne velikost.
**Verdikt:** hypotéza přežívá v přerámované, defenzivně poctivé podobě. Hodnota je
systematičnost + probe-osa, ne nový vzorec.

### VYPOCET-02 (a_4 anomaly-matching) — ROZDVOJIL hypotézu chirurgicky
**Co udělal:** poměr koef(C²)/koef(Euler) spektrální akce = **−18/11** (Chamseddine-Connes,
verbatim z PDF) je **PŘESNĚ** roven anomálnímu c/(−a) Weylova fermionu — oba sestupují
z téhož Diracova a_4. To je netriviální **pozitivní** potvrzení fermionového jádra.
Exaktní pro 45 i 48 fermionů (ν_R irelevantní). **Bonus:** faktor 11 se objevuje v
obou (spektrální Euler 11/60, anomálie a_Weyl=11/720).
**Co zabil:** plná SM (s bosony) dává −0,853 (bez ν_R) resp. −0,866 (s ν_R) vs. cíl
−1,636 → **silná verze jednoznačně falzifikována**. Bosony mají c/(−a) = −3 a −18/31,
což shodu rozbíjí. Zajímavost: ν_R posouvá plnou shodu *blíž* (0,784→0,771), i když ji
neuzavře.
**Verdikt:** novelty-check říká **pursue** a výpočet to ospravedlnil — fermionová
identifikace je čistá a nová, plná-SM verze je čistě mrtvá. Obě s plně dokumentovanou
konvencí. To je **nejlepší výsledek druhého kola**: ostrá hranice mezi tím, co platí
a co ne.

### VYPOCET-03 (Λ prefaktory) — VYVRÁTIL silnou hypotézu, vyrobil negativní novum
**Co udělal:** poprvé postavil tři κ vedle sebe v jedné konvenci. κ_Sorkin=0,2136,
κ_EDT=1,53·10⁻³, κ_CosMin(eff)=2,45. Poměr **κ_Sorkin/κ_EDT = 139,6 ≈ 140**, a tato
neshoda **nezmizí** žádnou volbou c_V (Sorkin a EDT mají různý funkcionální charakter
Λ–V). CosMIn nemá fundamentální κ vůbec (fixní číslo).
**Verdikt:** silná sjednocující hypotéza (jedna statistika δΛ~1/√N) je **vyvrácena**.
Sdílí se jen dimenzionální kostra Λ~H². **Ale**: toto srovnání nikdo v literatuře
neudělal → publikovatelný negativní výsledek. ESEJ-02 navíc nabízí formalizovatelné
čtení faktoru 140 jako „směnného kurzu mezi definicemi atomu" (l_cs/l_P≈7,7) — viz H2g-4.

### VYPOCET-04 (SSEE na diamantu) — MECHANICKY PODPOŘIL jádro, opravil predikci
**Co udělal:** SSEE bez truncace = 95,2 (volume-law, type-III-like divergence) → s
dvojitou truncací (κ=√N/4π) = 1,58 (area/log-law, type-II-like). Entropický cutoff
škáluje jako rank **~ N^0,519±0,007 → ε~ρ^(−1/2)**, což **potvrzuje** předpověď zadání
(ε~ρ^(−1/d) v 2D) a **vylučuje** alternativu ρ^(−1/4) z novelty-checku na **39 σ**.
2D log-slope b=0,49 (správné znaménko/řád vůči 1/3).
**Poctivé omezení:** **jen 2D, bezhmotný skalár**; hypotéza je o 4D (LQG area gap).
Entropický cutoff je *imposovaný* (κ z literatury), ne odvozený ab initio. Identifikace
ε s area gapem Δ=4√3πγl_P² zůstává nadcházejícím krokem (potřebuje 4D + normalizaci γ).
**Verdikt:** novelty-check říká **pursue**, výpočet mechanicky potvrdil, že truncace
JE regularizace měnící volume→area, a *kvantitativně disambiguoval* škálování cutoffu.
Trojcestná identifikace (SSEE=crossed-product=area gap) zatím není dokázána, ale poprvé
má numerický háček. **Doporučení: opravit entropy-cluster.md ř. 66 z ρ^(−1/4) na ρ^(−1/2).**

### Dossiery (H01–H03) — nepřinesly výpočet, ale zaostřily rizika
- **H01 (Cardy-γ):** jádro c=6k je **known** (Carlip 1410.5763, Ghosh-Pranzetti 1405.7056).
  Kritický **blocker: Senova IR-univerzalita** (1205.0971) — log-korekce jsou určeny jen
  IR daty, jsou přístupově-nezávislé, a *nemohou* fixovat UV parametr γ. Komplexní γ=±i
  (1212.4060) navíc podkopává smysl fixace reálného γ≈0,274. **Priorita dolů.**
- **H02 (SJ-Kerr):** SJ pro Kerr/SdS je **skutečně nepokryté území**. Kay-Wald no-go
  SJ neblokuje (SJ nevyžaduje Killing-symetrii); SJ-nehadamardovskost je u Kerru *feature*,
  ne bug. Nejlevnější test: 2D ekvatoriální řez / rotující BTZ. **Živé, čisté území.**
- **H03 (BMV):** binary „kvantovost gravitace" test je vyřešen (konsensus 2025: klasická
  gravitace entanglement nezprostředkovává). AS korekce ~10⁻⁶⁰ = neměřitelná. **Jediný
  principiálně odlišitelný** přístup je Oppenheimova postkvantová teorie (π-fázový posun
  bez superpozice). Nový framing „diskriminátor přístupů" žije.

---

## Hypotézy druhé generace

Pět až deset zostřených/nových hypotéz. Každá: tvrzení, opora (vč. čísel z výpočtů),
proč nová (cituje novelty verdikt), první test, confidence. Nápady z esejí značeny
původem **(esej)**.

### H2g-1 — Probe/observer-dependence je generický klasifikační princip, ne kuriozita d_s
**(esej — ESEJ-01 „princip relačnosti geometrie", formalizace falzifikací F1/F5)**
**Confidence: medium-high.**
- **Tvrdí:** závislost geometrické veličiny na *sondě/pozorovateli* (která vyřešila
  rozpor d_s v CST: VYPOCET-01) a na *cutoffu/pozorovateli* (která mění volume→area
  entropii: VYPOCET-04) jsou **dvě instance jednoho zákona**: žádná geometrická veličina
  (dimenze, entropie) není atribut oblasti, ale odpověď na dvojici (otázka, sonda). De
  Vuyst et al. (2412.15502) dokázali, že **QRF a crossed product jsou totéž** — přidat
  pozorovatele = vzít crossed product = zkonstruovat entropii.
- **Opora (čísla):** VYPOCET-01 — CST dává d_s=2 (d'Alembertián) i >D (random walk) ze
  stejné teorie; master `d_s=D/γ` činí sondu (γ) explicitním parametrem. VYPOCET-04 —
  SSEE 95,2 (bez cutoffu) vs. 1,58 (s cutoffem ε~ρ^(−1/2)); type-III bez stopy → type-II
  s konečnou stopou *teprve po* přidání pozorovatele.
- **Proč nová:** novelty-check d_s **přímo** doporučil „probe jako třetí klasifikační
  parametr d_s(z,D,probe)" jako jednu ze tří nepokrytých věcí; entropy-cluster
  doporučil **pursue** pro identifikaci truncace s observer/modulárním cutoffem. Žádný
  novelty-check ale **negeneralizoval** probe-dependence napříč veličinami — to je nové.
- **První test (F1/F5):** systematický sken sond na *téže* sprinklované mikrostruktuře:
  najít **druhou** veličinu (mimo d_s), která dá kvalitativně protichůdné odpovědi pro
  různé sondy — kandidát: efektivní Hausdorffova vs. spektrální dimenze, nebo geodetická
  vs. kauzální vzdálenost. Pokud *všechny* rozumné sondy dají tutéž geometrii, princip
  padá a VYPOCET-01 je izolovaná kuriozita.
- **Riziko (esej §8/F6):** **Senova IR-univerzalita** (H01) je tvrdá hranice — některé
  veličiny (log-korekce entropie) jsou určeny jen IR daty a *žádná* sonda jimi nehne.
  Princip musí ostře rozlišit UV-relační od IR-univerzálních veličin, jinak je
  formulován příliš hrubě.

### H2g-2 — Fermionový a_4 je čistý NCG↔anomálie most; bosony jsou „falešný kámen"
**Confidence: high** (výpočet hotový, hranice ostrá).
- **Tvrdí:** identifikace „a_4 jako společný rodič NCG spektrální akce a (a,c) anomálie"
  platí **přesně a jen v Diracově/fermionovém sektoru**; bosonový sektor ji rozbíjí, a to
  *není* normalizační artefakt, ale strukturální fakt (bosony mají jiné c/(−a)).
- **Opora (čísla):** VYPOCET-02 — `koef(C²)/koef(Euler) = −18/11` spektrální akce =
  c/(−a) Weylova fermionu, **EXAKTNĚ**, pro 45 i 48 fermionů. Plná SM: −0,853 (bez ν_R)
  / −0,866 (s ν_R) vs. cíl −1,636 → falzifikováno. Faktor 11 sdílen (Euler 11/60,
  a_Weyl=11/720).
- **Proč nová:** novelty-check a_4 = **pursue** — dvoustranné vazby jsou publikované
  (Andrianov-Lizzi, Kurkov-Lizzi 2010–13), ale **explicitní anomaly-matching test pro
  C⊕H⊕M₃(C) s porovnáním (a,c) vs. C² koeficientem nebyl proveden**. Náš výsledek tu
  mezeru vyplnil — a navíc ji ostře rozdělil na „platí (fermiony) / neplatí (bosony)".
- **První test:** ověřit, zda je fermionová shoda −18/11 *vynucená* Diracovým operátorem
  (tj. zda jakákoli spektrální trojice s fermiony nutně dává −18/11) nebo specifická pro
  C⊕H⊕M₃(C). Druhý krok: prozkoumat, zda **gravitační/Weyl sektor** (graviton c/(−a))
  mění bilanci — možná plná shoda vyžaduje i graviton, ne jen SM bosony.
- **Pozn.:** toto je nejpevnější hypotéza druhého kola — uzavřený výpočet, plně
  dokumentovaná konvence, čistý pozitivní i čistý negativní výsledek.

### H2g-3 — SSEE truncační cutoff = modulární cutoff crossed-productu (4D test s exponentem 3/4)
**Confidence: medium.**
- **Tvrdí:** entropický cutoff ε z VYPOCET-04 JE modulární/observer cutoff crossed-product
  konstrukce type-III→type-II; ve 2D škáluje jako ρ^(−1/2), **ve 4D musí dát ρ^(−3/4)**
  (area-law ansatz n_max~N^(3/4)). Identifikace s LQG area gapem Δ=4√3πγl_P² je třetí
  vrchol, kde γ je renormalizační konstanta vázající causet/type-II stopu na A/4.
- **Opora (čísla):** VYPOCET-04 — `ε~ρ^(−0,519±0,007)`, p=1/2 v 2D potvrzeno na 3 %,
  ρ^(−1/4) vyloučeno na 39 σ; volume→area přechod 95,2→1,58 mechanicky doložen.
- **Proč nová:** entropy-cluster novelty = **pursue**; trojcestná syntéza (SSEE
  truncace = crossed-product cutoff = LQG area gap) v literatuře chybí (sousední 2601.07915,
  2510.26911 se nepřekrývají). VYPOCET-04 ji poprvé numericky nahlodal.
- **První test (esej F2/F3):** **4D sprinkling** kauzálního diamantu, spočítat SSEE,
  změřit škálovací exponent entropického cutoffu — **predikce: p=3/4**, ne 1/2. Pokud
  vyjde p≠3/4 mimo chybu, mechanismus „cutoff=ρ^(−(d−1)/d)" padá. Druhý krok: spočítat
  **typ von Neumannovy algebry** implikovaný každým ze tří počítání — musí být všechny
  type II_∞ se stejnou stopou (jinak identifikace padá).
- **Riziko:** vnitřní nejednoznačnost (γ vs. Δ vs. ε jako cutoff) + Immirzi-normalizace
  je sama sporná (log −1/2 vs. −3/2, viz H01). Toto je v **napětí s H2g-7**.

### H2g-4 — Faktor 140 (Sorkin/EDT) je směnný kurz mezi definicemi „atomu prostoročasu"
**(esej — ESEJ-02 „Co kdyby I", formalizace falzifikace #3).**
**Confidence: low-medium.**
- **Tvrdí:** poměr κ_Sorkin/κ_EDT = 140 není šum ani pouhá neshoda, ale *měření* —
  kóduje kvadrát poměru definičních délek atomu prostoročasu v obou přístupech. Sorkin
  počítá kauzální linky o velikosti l_cs≈7,67 l_P; EDT simpliciální buňky; poměr má
  rozměr (škála)², jako α∝(l_P/l_cs)².
- **Opora (čísla):** VYPOCET-03 — κ_Sorkin=0,2136 (α=0,0085 → l_cs/l_P≈7,67),
  κ_EDT=1,53·10⁻³, poměr 139,6. √140≈11,8; 140≈(7,67)²·2,4.
- **Proč nová:** Λ-cluster novelty = reframe — mezipilířové srovnání prefaktorů **nebylo
  nikdy provedeno** (VYPOCET-03 ho udělal). Čtení rozdílu jako směnného kurzu je o krok
  dál a v literatuře zcela chybí.
- **První test (esej #3):** nezávisle změřit l_cs ze **swerves** (difúze hybnosti částic
  na causetu, Dowker-Henson-Sorkin gr-qc/0311055) a ověřit, zda horní meze na difúzní
  parametr k z kosmického záření dávají l_cs slučitelné s 7,7 l_P. Dvě úplně různá
  pozorování, jedna délka — buď se potkají, nebo vize padá.
- **Pozn.:** poctivě low-medium — VYPOCET-03 vyvrátil *silnou* unifikaci; tohle je
  spekulativní záchrana přes „informativní rozdíl". Cenná jen pokud swerves-most projde.

### H2g-5 — Everpresent Λ je swampland-kompatibilní de Sitter BEZ kvintesenčního pole
**(esej — ESEJ-02 „Co kdyby IV", most causal sets ↔ swampland).**
**Confidence: medium.**
- **Tvrdí:** swampland zakazuje *pevný* de Sitter; Sorkinova fluktuující Λ *nikdy není
  pevná* (kolísá kolem nuly, je vnitřně dynamická), takže splňuje ducha de Sitter
  conjecture **bez** skalárního pole. „Konečnost zakazuje pevnost": konstanta navázaná
  na konečný počet věcí (√N Poisson) nemůže být konstantní, stejně jako detektor s
  konečným počtem elektronů nemůže mít nulový šum.
- **Opora (čísla):** Λ~1/√V~1/√N~10⁻¹²² pro N~10²⁴⁰; pozorováno Λl_P²=2,9·10⁻¹²².
  DESI DR1/DR2 náznak vyvíjejícího se w(z) na 2,8–4,2 σ. VYPOCET-03 potvrzuje dimenzionální
  kostru Λ~H² (i když ne unifikaci prefaktorů).
- **Proč nová:** Λ-cluster novelty — most CST↔swampland je „barely" hrana; KB ho označuje
  „sotva prozkoumáno". Žádná publikace neztotožňuje swampland-zákaz dS s Poissonovou
  fluktuací počtu.
- **První test (esej F1):** odvodit predikovanou **mezioblastní varianci Ω_Λ napříč
  směry oblohy** (kterou kvintesence i CosMIn striktně **zakazují** a jen Sorkinův šum
  povoluje) a kvantifikovat amplitudu ~1/√V(z) vůči citlivosti SKAO / vysoké-z SNIa.
  Druhý krok: odvodit w(z) stochastický vs. kvintesenční hladký drift a srovnat s DESI DR2.
- **Riziko:** strunový swampland a diskrétní causety spolu formálně nemluví; most je
  „přes propast bez lana". Confidence drží jen společný motiv „konečnost zakazuje pevnost".

### H2g-6 — SJ vakuum jako kanonický bezparametrický stav pro rotující černé díry
**Confidence: medium** (čisté nepokryté území, ale náročný výpočet).
- **Tvrdí:** Sorkin-Johnstonova konstrukce dává **kanonický, bezparametrický** vstupní
  stav tam, kde hadamardovská rodina selhává (Kay-Wald no-go zakazuje symetrické Hadamardovy
  stavy na Kerru kvůli superradianci). SJ symetrii nevyžaduje → no-go ho neblokuje; jeho
  nehadamardovskost je u Kerru *feature*.
- **Opora:** H02 dossier — Kay-Wald, Fewster-Verch omezeny na ultrastatic slab; Kerr tam
  nespadá. SJ-nehadamardovskost prokázána na 1+1D diamantu (2212.10592). Superradiance
  (záporná KG-norma up-módů) nebrání definici A=iΔ na L²(M').
- **Proč nová:** preprint-checks novelty — **„SJ stav nebyl nikdy zkonstruován pro Kerr
  ani SdS v žádné nalezené práci; je to genuinely open territory."** Nejčistší „nepokryté
  území" celého korpusu.
- **První test (H02 strategie II):** adaptovat numerický SJ kód (1906.07952) na **rotující
  BTZ nebo ekvatoriální řez Kerru** (θ=π/2): sestavit retardovaný Green + Pauli-Jordanovu
  matici pro 2D oblast, diagonalizovat, ověřit, zda superradiantní módy přispívají
  **kladnými** vlastními čísly do A_+.
- **Výsledek by dal:** kanonický stav pro ⟨N_out⟩ superradiantního zesílení, alternativu k
  Unruhovu stavu, kovariantní spacetime entanglement entropy pro rotující ČD.

### H2g-7 — Log-korekce (−1/2 vs −3/2 ln A) je IR-univerzální, takže γ NELZE fixovat z CFT
**Confidence: medium-high** (jako *negativní* tvrzení).
- **Tvrdí:** opak naivní Cardy-LQG naděje — Senova IR-univerzalita (1205.0971) říká, že
  log-korekce entropie ČD jsou určeny **pouze** nízkoenergetickým spektrem bezhmotných polí,
  jsou přístupově-nezávislé, a **proto NEMOHOU fixovat UV parametr jako γ**. Cardy-LQG
  hypotéza (H01/L1-3) je tím fyzikálně oslabena: log-matching γ≈0,274 je buď trivial, nebo
  neplatný.
- **Opora:** H01 dossier — koeficienty se napříč přístupy neshodují (U(1) −1/2, SU(2)
  −3/2, Cardy −3/2, Sen ≈−2); každý má jiný mechanismus. Komplexní γ=±i (1212.4060) navíc
  činí fixaci reálného γ irelevantní.
- **Proč nová:** Cardy-LQG novelty = reframe; jádro c=6k je known. Co je *nové* je
  **explicitní artikulace blokátoru**: že IR-univerzalita strukturálně brání UV-fixaci γ.
  To je důležitější než pozitivní hypotéza, protože **rozhoduje o platnosti H2g-3 a celého
  Immirzi-renormalizačního programu**.
- **První test:** extrahovat C_KM(γ) z Engle-Noui-Perez (1006.0634 §4–6) a ověřit, zda
  konstantní člen O(1) v log-expanzi (ne log-koeficient) **přece jen** nese UV informaci o
  γ — to je jediná Senem-nepokrytá štěrbina (H01 next step). Pokud i konstantní člen je
  IR-určen, γ-fixace z CFT je definitivně mrtvá.
- **Pozn.:** **přímo v napětí s H2g-3** (Immirzi jako renormalizační konstanta). Tyto dvě
  je nutné testovat společně — výsledek H2g-7 rozhoduje o H2g-3.

### H2g-8 — BMV/QGEM diskriminuje POSTKVANTOVOU gravitaci, ne kvantovou vs. klasickou
**Confidence: medium.**
- **Tvrdí:** binary test „je gravitace kvantová?" je vyřešen (konsensus 2025). Jediná
  experimentálně **principiálně odlišitelná** alternativa od graviton-EFT/AS je
  **Oppenheimova postkvantová teorie**: předpovídá nulový GIE, ale charakteristický
  **π-fázový posun v křížových korelacích** pohybu oscilátorů — experiment *jiného typu*
  (mechanické oscilátory, bez superpozice). Verlindeho emergentní gravitace by byla
  detekcí GIE vyloučena.
- **Opora (čísla):** H03 dossier — AS korekce (l_Pl/d)²~10⁻⁶⁰ na BMV škálách (35 µm,
  10⁻¹⁴ kg) = neměřitelná; GUP/min-délka ~β·10⁻⁵² pod prahem i pro β~10³⁴.
- **Proč nová:** preprint-checks novelty — framing „AS graviton spektrální funkce vs.
  Verlinde entropický mediátor, **ne** Q vs. C" je legitimně nový a má být zdůrazněn.
- **První test (H03 next step):** odvodit explicitní AS korekci k entanglamentní fázi
  Bonanno-Reuterovým G(r)=G₀r²/(r²+γG₀) a kvantifikovat δφ/φ pro plánované parametry
  (podklad pro H03-vypocet.py). Paralelně: spočítat predikovaný π-fázový posun Oppenheimovy
  teorie jako *pozitivní* diskriminační signál.
- **Pozn.:** hodnota je v identifikaci, že BMV nemá diskriminační sílu mezi EFT-přístupy
  (10⁻⁶⁰), ale **má** ji proti postkvantové/emergentní gravitaci — to mění design experimentu.

---

## Výpočetní fronta

Seřazeno podle (decisiveness × proveditelnost × novost), s odhadem náročnosti.

| # | Výpočet | Hypotéza | Náročnost | Co rozhodne |
|---|---|---|---|---|
| 1 | **4D SSEE sprinkling**: změřit škálovací exponent entropického cutoffu | H2g-3 | **dny–týden** | Predikce p=3/4 (ne 1/2). Posune entropy-cluster z 2D sanity-check na 4D test area gapu. Nejvyšší poměr výnos/riziko. |
| 2 | **a_4 s graviton sektorem**: zahrnout Weyl/graviton c/(−a) do plné bilance C⊕H⊕M₃(C) | H2g-2 | **hodiny** | Uzavřený heat-kernel počet. Rozhodne, zda plnou shodu zachrání graviton (ne jen SM bosony). Nejlevnější, navazuje na hotový VYPOCET-02. |
| 3 | **C_KM(γ) konstantní člen** z Engle-Noui-Perez 1006.0634; test Senovy IR-univerzality | H2g-7 (→H2g-3) | **hodiny–dny** | Rozhodne, zda γ lze vůbec fixovat z CFT, nebo je IR-univerzalita absolutní blocker. Rozhoduje o celém Immirzi-programu. |
| 4 | **vN algebra typ** pro SSEE-truncaci / crossed-product / LQG area-counting (tři počítání) | H2g-3 | **dny** | Musí dát všechny type II_∞ se stejnou stopou, jinak trojcestná identifikace padá. |
| 5 | **2D SJ na rotujícím BTZ / ekvatoriálním Kerru**: A=iΔ matice, kladnost A_+ superradiantních módů | H2g-6 | **týden–týdny** | První SJ stav na rotující ČD vůbec. Čisté nepokryté území; náročnější numerika. |
| 6 | **Ω_Λ sky-patch variance** + stochastický w(z) z everpresent Λ; srovnání s DESI DR2 / SKAO citlivostí | H2g-5 | **dny** | Pozorovatelný diskriminátor Sorkin-šum vs. kvintesence vs. ΛCDM. |
| 7 | **swerves ↔ l_cs most**: meze na difúzní parametr k vs. l_cs/l_P=7,7 z temné energie | H2g-4 | **dny** | Test, zda dvě nezávislá pozorování dají jednu délku atomu. Záchrana/pohřeb faktoru 140. |
| 8 | **AS δφ/φ BMV** Bonanno-Reuter G(r) + π-posun Oppenheim | H2g-8 | **dny** | Kvantifikuje (ne)měřitelnost a pozitivní diskriminátor postkvantové gravitace. |
| 9 | **FRG global-charge koeficient** ve fixed pointu AS (L4-2) | (BS-01) | **týdny** | Decisive, ale náročný FRG počet; Basile et al. už konflikt mapují. |
| 10 | **1/p⁴ AS propagátor → δ(Q/M)** v Hamada-Noumi-Shiu WGC (L4-6) | (BS-01) | **dny–týden** | Znaménko WGC korekce; nepublikovaný výpočet. |

**Doporučené pořadí pro nejbližší kolo:** #1, #2, #3 (paralelně — různá náročnost, vysoká
decisiveness), pak #4 (rozhoduje o H2g-3 spolu s #1).

---

## Strategický pohled

### Kde má projekt největší šanci na skutečný objev

**1. a_4 fermionová identifikace (H2g-2) — nejpevnější aktivum.** VYPOCET-02 dal **čistý
pozitivní výsledek** (−18/11 exaktní) i **čistý negativní** (plná SM falzifikována),
oba s plně dokumentovanou konvencí, a novelty-check potvrdil, že **anomaly-matching test
pro C⊕H⊕M₃(C) nikdo neudělal**. Toto je nejblíž publikovatelnému výsledku: ostrá hranice
mezi platným a neplatným, uzavřený počet, nová mezera vyplněná. Další krok (#2, graviton
sektor) je levný a může identifikaci buď rozšířit, nebo definitivně ohraničit.

**2. Probe/observer jako klasifikační osa (H2g-1) — nejhlubší motiv.** Dvě nezávislé
linie (VYPOCET-01 d_s, VYPOCET-04 entropie) konvergují na *strukturně stejném* zjištění:
geometrická veličina je odpověď na (otázka, sonda), ne atribut. Podpořeno externě tím, že
QRF = crossed product (2412.15502). To je **nejproduktivnější smiřovací princip** — pokud
část mezipřístupových konfliktů jsou konflikty sond (jako vyřešený rozpor 657 vs. 1777),
projekt může „rozpustit" konflikty místo aby je překonával. Riziko: musí přežít Senovu
IR-univerzalitu (ne všechno je relační).

**3. SJ na rotujících černých dírách (H2g-6) — nejčistší nepokryté území.** Novelty-check
explicitně: „genuinely open territory". Vysoký objevný strop (kanonický stav pro Kerr,
alternativa k Unruhovu stavu), ale náročnější numerika a delší horizont.

**4. Everpresent Λ jako šum + swampland (H2g-5) — nejvyšší fyzikální dopad, pokud vyjde.**
Pozorovatelně testovatelné (DESI/SKAO sky-patch variance), řeší problém kosmologické
konstanty *i* koincidence jako statistickou nutnost. Ale: silná unifikace už **mrtvá**
(VYPOCET-03), most na swampland je „bez lana". Vysoké riziko, vysoký výnos.

### Co opustit nebo degradovat

- **Silná Λ-unifikace (Sorkin=EDT=CosMIn jedna statistika)** — **VYVRÁCENA** (140×,
  VYPOCET-03). Opustit jako pozitivní hypotézu; přežívá jen jako (a) falzifikovatelný
  prefaktor-test (hotovo), (b) spekulativní „směnný kurz" H2g-4 podmíněný swerves-mostem.
- **Cardy-LQG fixace reálného γ≈0,274 (L1-3 silná verze)** — degradovat. Jádro c=6k je
  **known** (Carlip), a Senova IR-univerzalita (H2g-7) je pravděpodobně **fatální blocker**
  pro UV-fixaci γ z CFT. Investovat jen do levného testu #3, který blocker rozhodne; pokud
  IR-univerzalita drží i pro konstantní člen, celý Immirzi-renormalizační program (vč.
  H2g-3 třetího vrcholu) ztrácí jednoznačnost.
- **Plná-SM verze a_4 identifikace** — opuštěna výpočtem; ponechat jen jako dokumentovanou
  falzifikaci, ne jako živou hypotézu.
- **BMV jako binary Q-vs-C test** — vyřešeno konsensem 2025; opustit. Přesunout veškerou
  energii do diskriminace přístupů (H2g-8), kde je AS korekce sice neměřitelná, ale
  Oppenheim/Verlinde rozlišitelné.
- **„d_s objev vzorce"** — opustit definitivně (vzorec publikován 2009). Prodávat jen
  systematičnost + probe-osu + diskriminační interpretaci.

### Meta-závěr druhého kola

Tři ze čtyř výpočtů **falzifikovaly silnou verzi** své hypotézy (Λ unifikace, plná-SM a_4)
nebo ji **přerámovaly z objevu na klasifikaci** (d_s). To není neúspěch — je to **kalibrace**:
projekt přestal věřit ve „velké sjednocení napříč přístupy" a získal místo toho dvě
publikovatelná aktiva (fermionový a_4, prefaktor-test) a jeden hluboký organizační princip
(probe/observer-relačnost). **Nejproduktivnější strategie pro třetí kolo:** přestat hledat,
kde se přístupy shodují, a začít přesně měřit, *kde a proč se liší* — protože právě tyto
rozdíly (−18/11 vs. bosony, 140× Λ, p=1/2 vs. 3/4, sonda vs. sonda) jsou tím, co je v
literatuře nepokryté.

---

*Anchory: `core-data/novelty-checks.json`; `knowledge-base/vypocty/VYPOCET-01…04`;
`knowledge-base/hypotezy/H01-gamma-cardy.md`, `H02-sj-kerr.md`, `H03-bmv-diskriminator.md`;
`knowledge-base/eseje/ESEJ-01-dimenze-jako-otazka.md`, `ESEJ-02-vesmir-ktery-se-pocita.md`;
`knowledge-base/BRAINSTORM-01.md`; `verification/novelty/*.md`.*

---

## Výsledky rozhodujícího kola (2026-06-06)

Rozhodující kolo uzavřelo čtení γ–Cardy blocku a přidalo tři nové výpočty (VYPOCET-05, VYPOCET-06, VYPOCET-07) plus registr nálezů (findings.json, 8 položek).

### Souhrnná tabulka

| Položka | Výsledek | Dopad na hypotézu |
|---|---|---|
| **γ–Cardy rozhodující čtení** (H01 decisive) | Verdikt `program-dead`: konstantní člen O(1) v ENP 1006.0634 nebyl explicitně publikován — Tvrzení B z §2.2 je technicky nové, ale fyzikálně nemotivované. Sen 1205.0971 dokazuje, že log-koeficienty jsou IR-určeny a přístupově-nezávislé; LQG dává −2, Eukleidovská gravitace +1,71 — koeficienty nesouhlasí, porovnávat konstantní člen nemá smysl. Carlip 1410.5763 explicitně říká, že γ₀ pochází z „obscure combinatorial problem", ne z Cardyho formule. | **H2g-7 (Sen blocker): POSÍLENA** až na úroveň definitivního závěru. **H01 (Cardy-LQG): ZABITA** (program dead). **H2g-3** (Immirzi-renormalizace přes CFT): ztrácí motivaci v CFT větvi; zbývá jen causet/type-II větev. |
| **VYPOCET-05 — SJ stav v rotujícím BTZ ergoregionu** | Úspěch. SJ stav plně konstruovatelný uvnitř ergoregionu (r=0,974, M=1, J=0,6): 796+/796− eigenvalue v přesných párech, reziduál 4,6×10⁻¹⁶ (strojová přesnost). Statický řez tam NENÍ Lorentzův (diskriminant −0,192). Kauzální asymetrie A_caus = +1,000 uvnitř vs. +0,007 vně (statika), nulový sklon mizí přesně na r_erg=1,0. Wightmanova asymetrie opačného znaménka než kauzálně-početní (feature, ne bug). | **H2g-6 (SJ rotující ČD): SILNĚ POSÍLENA** — 2D analog numericky dokončen, strojově přesně; superradiantní signatura v eigenvektorech/W potvrzena. Nasměrování pro 4D: hledat signaturu v eigenvektorech, ne v hrubém spektru. |
| **VYPOCET-06 — 4D SSEE cutoff scaling test (p=3/4 predikce)** | Predikce p=3/4 NEPOTVRZENA jako robustní spektrální exponent. Naměřený exponent závisí na volbě cutoffu (0,65–0,98); p=3/4 trefuje jen arbitrární 10%-λ_max cutoff náhodou; literaturní slope-knee dává ~N¹. Sekundárně: 4D SSEE na nested diamantu dává VOLUME law (R²=0,998), ne area law — přesně dle literatury (2008.07697, 1712.04227). | **H2g-3 (SSEE/crossed-product 4D test): OSLABENA** — jednoduchá 2D→4D extrapolace „změř p ze spektra" selhává; 4D Pauli-Jordanovo spektrum z link-matice není mocninové; p=3/4 je literaturní ansatz, ne emergentní exponent. Trojcestná identifikace nutně přehodnotit. |
| **VYPOCET-07 — BMV AS fázová korekce** | AS korekce δφ/φ ≈ 6,2×10⁻²⁸ při d=100 µm (bez ħ — klasický RG efekt); EFT korekce ≈ 3,4×10⁻⁶² (jednosmyčkový kvantový efekt, obsahuje ħ). Poměr AS/EFT ≈ 1,82×10³⁴. Obě korekce 24 resp. 59 řádů pod dosažitelností. Binární diskriminátor (GIE ano/ne) dostupný do 2030–2035; Oppenheimův křížový korelační experiment principiálně přístupný. | **H2g-8 (BMV diskriminátor): POSÍLENA** — kvantitativně zpřesněna; AS a EFT mají odlišnou dimensionální strukturu (AS: klasický, EFT: kvantový), což upřesňuje fyzikální interpretaci. Oppenheimova varianta potvrzena jako jediná realistická kontinuální diskriminace. |
| **findings.json (8 nálezů)** | Pokrývají všechna 5 požadovaná témata: klasifikační tabulka d_s(z,D,probe) s probe-dependencí (F-001, F-002), exaktní shoda −18/11 ve fermionovém sektoru + falzifikace plné SM (F-003, F-004), prefaktor ~140× neshoda Sorkin vs. EDT (F-005), potvrzení ρ^(−1/2) a vyloučení ρ^(−1/4) na 39σ (F-006, F-007, F-008). | Dokumentuje stav registru; každý nález rozlišuje reprodukci literatury od projektově-originálního přínosu. Slouží jako podklad pro případnou publikaci. |

### Status hypotéz druhé generace po rozhodujícím kole

| Hypotéza | Status po kole 2 | Poznámka |
|---|---|---|
| **H2g-3** — SSEE truncace = crossed-product cutoff (4D, p=3/4) | **OSLABENA** | VYPOCET-06 vyvrátil p=3/4 jako robustní exponent; volume-law místo area-law v nested diamantu; CFT větev Immirziho identifikace bez motivace (viz H2g-7 verdikt) |
| **H2g-6** — SJ vakuum pro rotující ČD | **POSÍLENA** | VYPOCET-05 numericky dokončen; 2D BTZ analog strojově přesně; nasměrování pro 4D Teukolského výpočet |
| **H2g-7** — Log-korekce jsou IR-univerzální, γ NELZE fixovat z CFT | **POSÍLENA (definitivní)** | Rozhodující čtení potvrdilo, že Sen blocker platí na úrovni log-koeficientu; konstantní člen nemotivován; H01 uzavřena jako mrtvá |
| **H2g-8** — BMV diskriminuje postkvantovou gravitaci | **POSÍLENA** | VYPOCET-07 kvantitativně zpřesnil; AS vs. EFT dimensionální struktura nově doložena |

### Reziduální stopa (doporučená)

Bianchi arXiv:1204.5122 — entropie nekomplexního ČD z LQG smyček pro γ = i, kde γ-závislost mizí; srovnání může mít principiální základ. Okrajový výzkumný přínos, nízká priorita.

*Anchory rozhodujícího kola: `core-data/calculations/VYPOCET-05/`, `VYPOCET-06/`, `VYPOCET-07/`; `core-data/findings.json`; `knowledge-base/hypotezy/H01-gamma-cardy.md` (verdict: program-dead).*
