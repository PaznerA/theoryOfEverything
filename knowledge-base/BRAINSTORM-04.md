# Brainstorming 04 (2026-06-06)

> **Status oproti BRAINSTORM-03:** třetí kolo dalo projektu *robustní jev s draftem*
> (SJ-rotace, draft-01), *přerámování objektu* (H04: link → BD d'Alembertián) a *algebraický
> jazyk* (pilíř 19, modular-hamiltonian TOP HUB). **Čtvrté kolo** běh VYPOCET-11…14 a uzavřelo
> tři velké otevřené body: (i) draft-02 je **vědecky uzavřen** — graviton identitu −18/11
> nezachrání na žádné násobnosti, identita je index-teorémem chráněná (Atiyah-Singer/Rohlin);
> (ii) 4D entropy-cluster **přežil** — volume law byl artefakt *rohů* diamantu, slab dává čistý
> area law S~L^2.00, non-Hadamardovost lokalizovaná Hadamardovou diagnostikou; (iii) první
> numerický doklad **III₁→II přechodu** přes SSEE truncaci (2/3 proxy, 2D). Confidence zde
> zohledňuje **čtyři kola selekce** — a poprvé se objevuje *jednotící nit*, která stojí nad
> jednotlivými klastry.

---

## Bilance po šesti kolech

Tabule všech programů/hypotéz se statusem a tvrdou evidencí (čísla z 17 findings.json
F-001…F-017). Symboly: ✓✓ = silně potvrzeno + nepokryté území; ✓ = potvrzené jádro;
⚠️ = přežívá oslabeno/podmíněně; ⚰️ = mrtvé jako pozitivní hypotéza; → = přeformulováno.

| # | Program / hypotéza | Stav | Rozhodující evidence (čísla) | Co žije |
|---|---|---|---|---|
| 1 | **a₄ fermionová identita** (L1-1 → H3g-4) | **✓✓ / draft-02 CLOSED** | `koef(C²)/koef(Euler) = −18/11` EXAKTNĚ (sympy racionál), shoduje se s `c/(−a)` Weylova fermionu (45 i 48 fermionů). Graviton NEZACHRÁNÍ: konformní graviton −398/261, fyzikální nemá čisté (a,c); kolinearita na (a,c)-rovině: **jen Weyl leží na paprsku −18/11**; nutná násobnost gravitonů `x=−143/32<0` (nefyzikální). Index-zámek: spinorové (a,c)=(11/360,1/20)=Duff Tab.1; Â=−p₁/24, ind(D)=−σ/8, Rohlin σ∣16 → ind=−2 sudé ✓ [F-003, F-004, F-014; VYPOCET-02, 11] | Vědecky uzavřeno. Zbývá jen lidská revize + framing. Spektrální akce = Sacharovova **fermionově-indukovaná gravitace**. |
| 2 | **SJ na rotujících ČD** (H02 → H2g-6, H3g-1, H3g-6) | **✓✓ / draft-01 v0.2** | Všechny 4 BTZ signatury replikují na Kerru, strojová přesnost (787±/790± párů, rezid. ~5e-16); null-slope mizí EXAKTNĚ na r_erg=2M; opačná znaménka A_caus>0/A_W<0 na každém (a,r). Frame-dragging žije v **eigenvektorech**: ~44,6° rotace podprostoru (cos²=0,507), spektrum mění <2%, link-frac 0,6%. W_sr ~ **Ω(r)^B** (lokální ZAMO), ΔAIC 230–4200 vs. ergosféra-práh model; B=4,23 (Kerr a=0,6), 3,82 (a=0,9), 1,71 (BTZ). A_W záporně-definitní v 65/65 měřeních. Toy-model reprodukuje A_caus i A_W (korelace 0,95–0,97) [F-009, F-013, F-017; VYPOCET-05/08/10/14] | Nejsilnější nepokryté území. Mechanismus opačných znamének **vysvětlen** (VYPOCET-10/14). Zbývá φ-periodicita + lidská re-derivace. |
| 3 | **SSEE / entropy-cluster** (H2g-3 → H04) | **✓ (2D) / ✓ (4D, geometrie!)** | 2D: čistý cutoff ε~ρ^(−1/2), p=0,519±0,007, p=1/4 vyloučeno na **39σ**; entropy-cutoff (p=1/2) ≠ discreteness-knee (p=1). 4D **NEBYL** dimenzní selhání: volume law byl **rohový artefakt** diamantu — slab half-space dává AREA: S~L^2.00 (R²=0,982; vyšší N přesně 2,00), S~plocha^1.00; interiérní kontrola S~L^2.18. Hadamardova diagnostika lokalizuje anomálii do **rohů**: 4D diamant inside −1,53 vs corner −2,79; slab deep −3,81 ≈ surface −3,85 (žádná anomálie) [F-006/07/08/16; VYPOCET-04/06/09/13] | 4D **žije** se správnou geometrií (Rindler/slab klín = Unruh = Hadamard). BD objekt (VYPOCET-09) opravil tvar spektra, ne exponent → selhání nebylo objekt-specifické, bylo **geometrie-specifické**. |
| 4 | **vN typ III→II přechod** (H3g-3) | **✓ (2D, 2/3 proxy)** | První numerický doklad III₁→II přes SSEE truncaci. Proxy 1 (entropická stopa): S_full~N^1.04 (volume) → S_trunc saturuje 1,30–1,70, **80× kolaps** stopy. Proxy 2 (modulární spektrum ε=ln[μ/(μ−1)]): full plochá hustá (47→217 módů, pile-up ~N^1.14) = Connes III₁; trunc integrabilní (8→20 módů, nulový pile-up, IR hrana ε>1,6) = typ II. Proxy 3 (centrální sekvence): self-averaging ano, ale nerozhoduje. PJ nukleární norma škáluje ~N^1.20→1.14 (jen −20%): **typ žije ve stavu/entropii, ne v kinematice** [F-015; VYPOCET-12] | Nejhlubší nový výsledek. Modular-hamiltonian TOP HUB (614 nodů/2437 hran) dal algebraický jazyk. 4D otevřené (běží jako VYPOCET-16). |
| 5 | **d_s(z,D,probe) klasifikace** (L3-1 → H2g-1) | **⚠️ / draft-03 v0.1** | Master `d_s=D/γ`, 12/12 numerických kontrol (tol. 0,06); reprodukuje GR=4, Hořava z=2 → 5/2, z=3 → 2, Stelle/AS/CST-dAlembert → 2, CST-random-walk > D. Vyřešen interní rozpor edge 501 vs. 1539 (CST probe-závislé) [F-001, F-002; VYPOCET-01] | Hodnota = jednotný formalismus + **probe jako třetí osa** + diskriminační čtení (vzorec known od 2009 — prodává se syntéza). Review-note. |
| 6 | **Cardy–LQG fixace γ** (H01 → H2g-7) | **⚰️** | Senova IR-univerzalita (1205.0971): log-koeficienty IR-určené, UV parametr γ jimi nelze fixovat; LQG −2 vs. Eukleid +1,71 nesouhlasí [F-010] | Definitivní negativní závěr. Zabíjí i CFT větev H2g-3. **Sen-typ filtr = první obranná linie.** |
| 7 | **Λ ~ 1/√V sjednocení** (L1-2 → H2g-4/5) | **⚰️ (silná) / ⚠️ (reframe)** | κ_Sorkin/κ_EDT = **139,6 ≈ 140×**, neslučitelné konvencí; CosMIn nemá pravé κ (epocha-závislé) [F-005] | Přežívá jen falzifikovatelný prefaktor-test + spekulativní "směnný kurz atomu". |
| 8 | **BMV diskriminátor** (H03 → H2g-8) | **→ binární** | AS korekce ~6,2e-28, EFT ~3,4e-62 (24 resp. 59 řádů pod dosahem) | Spojité diskriminátory mrtvé; binární GIE test 2030–2035. |
| 9 | **Probe/observer-relačnost** (H2g-1 → H3g-5) | **⚠️ → jednotící nit** | Dvě linie konvergují: d_s(probe) + entropy-cutoff vs. discreteness-knee. Externí opora: QRF = crossed product (De Vuyst 2412.15502). Pilíř 19 dodal algebraický jazyk | **Povýšeno na samostatnou sekci** (viz níže). Riziko: musí přežít Sen IR-univerzalitu. |

**Skóre šesti kol:** 2 aktiva na úrovni draftu-CLOSED/v0.2 (a₄, SJ-rotace); 1 program zachráněný geometrií (4D entropy); 1 nový hluboký výsledek (III→II); 1 klasifikace (d_s); 4 čisté popravy (Cardy, Λ-unifikace, BMV-spojitý, naivní d_s-univerzalita). **Filtr je kalibrovaný:** co přežilo čtyři kola, přežilo opakované pokusy o popravu.

---

## Jednotící nit: "vlastnosti = odpovědi na otázky"

Šest kol vykrystalizovalo through-line, který v kolech 1–3 byl jen tušený a teď má **tři nezávislé datové opory + algebraický jazyk**. Formulace:

> **Vlastnosti prostoročasu nejsou atributy, ale odpovědi na otázky.** Spektrální dimenze, entanglementová entropie, znaménko asymetrie, typ algebry — žádná z nich není "ta, co prostoročas má". Každá je *trojicí* (struktura, sonda/pozorovatel, region) → číslo. Změň sondu, dostaneš jinou odpověď — a to není chyba měření, je to **kovariantní fakt**.

### Je to jedna hypotéza?

Ano — a teď ji lze formulovat jako jedno **testovatelné** tvrzení, ne jen jako narativní motiv. Tři klastry, které vypadaly jako oddělené, jsou tři **realizace téže struktury**:

1. **d_s(z,D,probe)** [F-001/02]: tatáž CST teorie dá d_s=2 (d'Alembertián) i d_s>D (random-walk). Sonda = otázka. Rozpor edge 501 vs. 1539 byl *zdánlivý* — každá hrana generalizovala z jedné sondy.
2. **Entropie(region geometry)** [F-016]: tatáž dimenze d=4, tentýž objekt (iΔ link), táž truncace — diamant dá volume, slab dá area. **Region = otázka.** Volume law nebyl vlastnost 4D, byl odpověď na "ptáš-li se na region s rohy".
3. **Entropie(state regularity)** [F-016 Hadamard]: roh diamantu = místo, kde SJ stav přestává být Hadamardův. Regularita stavu = otázka. Mimo rohy (slab) je odpověď čistá.
4. **Typ algebry(stav, ne kinematika)** [F-015]: PJ nukleární norma (kinematika) typ nenese; jen entropie/modulární spektrum (stav) rozlišuje III od II. **"Na co se ptáš" rozhoduje, jakou strukturu vidíš.**

Společný jmenovatel: **invariantní není absolutní hodnota, ale relativní** (relativní entropie, relativní dimenze). To je přesně struktura, kterou crossed-product (QRF) dává: různý pozorovatel → různá algebra typu II → různá entropie, ale relativní entropie invariantní (2412.15502, pilíř 19 otevřený problém #2).

### Jak by se formalizovala?

Tři vrstvy, od slabé k silné:

- **(A) Relační/QRF jazyk.** Každá veličina V je funktor (struktura S, referenční rámec R) → ℝ. "Pozorovatel" R je crossed-product faktor (L²(G) pro grupu symetrií). Probe-volba = volba R. Predikce: dvě sondy téže S jsou spojeny *vnitřním automorfismem* algebry, takže relativní veličina (V_R₁ − V_R₂ vůči společnému referentu) je invariant.
- **(B) Modulární teorie.** Nejsilnější vrstva, protože ji pilíř 19 a VYPOCET-12 už *číselně dotýkají*. Otázka ↔ modulární tok σ_t. "Region geometry" → modulární Hamiltonián K = −ln ρ region. Roh diamantu = **místo, kde selhává boost-flow** (modulární tok není geometricky lokální → non-Hadamard → divergentní stopa → typ III₁). Slab = klín, kde modulární tok JE boost (Bisognano-Wichmann/Unruh) → typ III₁ regularizovatelný na II. **Through-line = tvrzení o tom, kde je modulární tok geometrický a kde ne.**
- **(C) Index/anomálie jako "otázko-nezávislé jádro".** Sen IR-univerzalita říká: *některé* veličiny otázko-nezávislé jsou (log-koeficienty, anomálie, indexy). −18/11 je takový objekt: index-chráněný, nezávislý na poli z Diracova operátoru [F-014]. Through-line tedy NENÍ "všechno je relační" — je to **ostrá hranice mezi relačním (UV, sonda-závislým) a univerzálním (IR/topologickým, sonda-nezávislým)**.

### Co by ji vyvrátilo?

Toto je klíčové — through-line musí být falzifikovatelná, jinak je to jen narativ:

1. **Kdyby dvě sondy téže struktury daly veličiny, které NEJSOU spojeny crossed-productem** (tj. relativní veličina není invariant) → relační formalizace (A) padá; jde o dvě fyzikálně různé teorie, ne dvě otázky o jedné.
2. **Kdyby non-Hadamardovost rohu NEkorelovala s modulárním tokem** (roh by byl non-Hadamardův, ale modulární tok by tam zůstal geometrický/boost) → vrstva (B) padá; rohová anomálie by byla čistě kinematická diskrétnost, ne modulární jev. **Toto je přesně test H4g-1 níže.**
3. **Kdyby se našla veličina, kterou Sen-typ univerzalita chrání, a přesto by reagovala na změnu sondy** → hranice (C) je špatně nakreslená; through-line je formulovaná příliš hrubě a kolabuje (buď je vše relační, nebo nic).
4. **Kdyby III→II přechod závisel na kinematice (PJ stopě), ne na stavu** → opak F-015; "na co se ptáš" by nerozhodovalo, struktura by byla atribut. F-015 to *vyvrací* (typ žije ve stavu), ale 4D test (VYPOCET-16) to musí potvrdit i mimo 2D.

**Verdikt:** through-line JE jedna hypotéza, formalizovatelná v modulární teorii, s **konkrétním vyvracečem** (bod 2 = H4g-1). Není to metafyzika — je to tvrzení, že rohová non-Hadamardovost a selhání boost-flow jsou táž věc. To se dá spočítat.

---

## Hypotézy čtvrté generace

Šest zostřených hypotéz. Každá: tvrzení, opora (čísla), test, confidence. Čtvrtá generace je *užší a algebraičtější* než třetí — modulární jazyk pilíře 19 + uzavřené VYPOCET-11…14 zúžily prostor a daly přesné háčky.

### H4g-1 — Rohová non-Hadamardovost = místo, kde selhává boost-flow: koreluje s modulární teorií

**(jádro: roh diamantu jako modulární singularita; spojuje F-016 Hadamardovu diagnostiku s F-015 III₁→II a s through-line vrstvou B)**
**Confidence: medium-high** (dvě nezávislé datové opory už existují; chybí jejich *přímé* spojení).

- **Tvrdí:** non-Hadamardovská anomálie, kterou VYPOCET-13 lokalizoval do **rohů** kauzálního diamantu (4D inside −1,53 vs corner −2,79; 2D inside −0,160 vs corner −0,095 na analyticky známém u−v′=±2L), je **tatáž věc** jako místo, kde modulární tok σ_t SJ stavu přestává být geometrický boost. Konkrétně: na slab/Rindler klínu je modulární Hamiltonián K = boost generátor (Bisognano-Wichmann), tok je geometrický, SJ ≈ Unruh = Hadamard, algebra je III₁ regularizovatelná na II → area law. V rohu diamantu se dva null-okraje protínají, boost-flow nemá kam téct (degenerovaný Killing vektor), K přestane být lokální → SJ non-Hadamard → divergentní stopa (volume law) → "nezkrotitelná" III₁. **Roh = topologická obstrukce geometričnosti modulárního toku.**
- **Opora (čísla):** F-016 — Hadamardova anomálie *existuje a je lokalizovaná* (slab deep −3,81 ≈ surface −3,85, žádná anomálie; diamant roh strmější o ~1,3). F-015 — III₁→II přechod má číselný doklad (80× kolaps stopy, modulární spektrum flat-dense → integrabilní s IR hranou ε>1,6). F-011 — modular-hamiltonian je TOP HUB grafu (614/2437). Pilíř 19: K = strukturní most mezi vN, Tomita-Takesaki, JLMS, crossed-productem.
- **Test:** (a) **Spočítat modulární tok SJ stavu** na 4D slabu vs. diamantu (z korelátoru C=√(X·P), jak ve VYPOCET-12) a změřit jeho **geometričnost**: je σ_t lokální boost (Bisognano-Wichmann) na slabu a NElokální u rohu diamantu? Predikce: geometričnost selhává *přesně* tam, kde Hadamardova diagnostika ukazuje anomálii (roh). (b) **Korelovat** Hadamardův sklon |ReW| s lokalitou modulárního toku bod po bodu podél entangling plochy — predikce: monotónní vztah (čím non-Hadamardovější, tím méně geometrický K). (c) Pokud roh je non-Hadamardův, ALE modulární tok tam zůstane boost → **through-line vrstva B padá** (vyvraceč #2 z jednotící nitě).
- **Co by dalo:** spojilo by tři findings (F-015, F-016, F-011) do jednoho mechanismu a dalo through-line jeho **nejsilnější vyvraceč na test**. Povýšilo by entropy-cluster z "geometrie rozhoduje" na "modulární teorie *vysvětluje proč* geometrie rozhoduje".
- **Riziko (L-1, Sen-typ):** literatura (2008.07697/2412.07832) **explicitně zpochybňuje** přímou vazbu non-Hadamard ↔ volume. Musíme předem ověřit, že "selhání boost-flow" není jen jiný popis téhož kinematického rohu — pokud roh deformuje W i typ čistě diskrétností (bez modulárního obsahu), je to kinematika, ne modulární teorie, a hypotéza kolabuje na F-016.

### H4g-2 — Exponent B v zákonu W_sr ~ Ω(r)^B je určen dimenzí + spin-počítáním, ne metrikou

**(jádro: PROČ B=4,2 Kerr vs. 1,7 BTZ; zostření F-017/H3g-1/H3g-6)**
**Confidence: medium** (jev pevný, ale původ exponentu je zatím otevřená otázka — dobrá, protože ostrá).

- **Tvrdí:** mocninový exponent B v `W_sr ~ Ω(r)^B` (Kerr a=0,6: B=4,23; a=0,9: B=3,82; BTZ J=0,9: B=1,71) **není náhodné číslo fitu**, ale je určen kombinací (i) prostoročasové dimenze D (4 vs. 3), (ii) asymptotiky pádu Ω(r) (Kerr Ω~1/r³ vs. BTZ Ω~1/r²), a (iii) počtu superradiantních módů, které vstupují do SJ kladného podprostoru se zápornou KG-normou. Konkrétní hypotéza: **B ≈ (D−1) + korekce** — Kerr B≈3,8–4,2 ~ (D−1)=3 + měkká korekce; BTZ B≈1,7 ~ (D−1)=2 mínus korekce. Alternativně B je dán **rychlostí pádu Ω(r)**: hustota superradiantních módů v klínu ω(ω−kΩ)<0 škáluje jako mocnina Ω dané asymptotikou metriky.
- **Opora (čísla):** F-017 — B=4,23/3,82/1,71 přes tři konfigurace; ΔAIC 230–4200 decisivní pro Model S; A_W záporně-definitní 65/65; near-ergosféra |A_W|~0,49–0,60 vs. far-zone ~0,03–0,05 (faktor ~15–20). F-013 — superradiantní váha roste monotónně se spinem (a=0: 0,0000 exaktně; a=0,9: 0,0171). Geometrie-nezávislost: BTZ↔Kerr stejný kvalitativní vzorec [F-009].
- **Test:** (a) **Třetí dimenze/asymptotika:** spočítat W_sr ~ Ω^B na Kerr-AdS (4D, ale Ω~1/r jiná asymptotika) a/nebo 5D Myers-Perry. Predikce: pokud B závisí na D, B(5D) ≈ 4–5; pokud na asymptotice, B(Kerr-AdS) ≠ B(Kerr). To **disambiguuje** mezi "B z dimenze" a "B z pádu Ω". (b) **Spin-počítání:** rozložit W_sr do příspěvků jednotlivých (ω,k) módů a zjistit, zda B = mocnina v hustotě stavů superradiantního klínu. (c) Hustší vzdálený scan r=5–20M (doporučení z VYPOCET-14/15) pro disambiguaci Model E vs. S u a=0,6 (kde lineární korelace ještě favorizuje E: 0,971 vs. 0,900, protože 1/(r−r_erg) a Ω(r) jsou korelované).
- **Co by dalo:** povýšilo by F-017 z "Ω-zákon platí" na "Ω-zákon s **predikovatelným** exponentem" — falzifikovatelná predikce pro 4D Teukolsky (srovnání B se superradiantním zesilovacím koeficientem). To je rozdíl mezi fenomenologií a teorií.
- **Riziko:** fit narážel na horní mez A=100 (Kerr); absolutní B jsou orientační, robustní je ΔAIC a *relativní* B mezi konfiguracemi. Mohlo by se ukázat, že B je spojitá funkce spinu (klesá 4,23→3,82 s a=0,6→0,9), ne dimenzní konstanta — pak je hypotéza "B = f(D)" špatně formulovaná a správná je "B = f(spin, asymptotika)".

### H4g-3 — Fermionová indukce předpovídá kosmologickou konstantu: f₀ moment řídí Λ

**(jádro: co H3g-4/fermionová indukce předpovídá pro Λ; uzavírá riziko draftu-02 "indukovaná gravitace má v NCG subtilní status Λ")**
**Confidence: medium** (interpretace silná, ale Λ-predikce v NCG je notoricky subtilní — proto cenná, pokud vyjde).

- **Tvrdí:** je-li spektrální akce **fermionově-indukovaná** gravitace (H3g-4, potvrzeno F-014: graviton nezachrání −18/11, identita index-chráněná), pak kosmologická konstanta NENÍ volný parametr, ale je řízena **f₀ momentem** spektrální akce — tj. nultým Seeley-deWitt koeficientem a₀ Diracova operátoru. Konkrétně: spektrální akce Tr f(D/Λ) = f₄Λ⁴a₀ + f₂Λ²a₂ + f₀a₄ + … Členy a₀ (kosmologická konstanta) a a₂ (Einstein-Hilbert) jsou **fermionové vakuové momenty**, ne nezávislé konstanty. Hypotéza: poměr Λ_cc/M_Pl² je dán **týmž fermionovým obsahem** (45/48 Weylů), který fixuje −18/11 — tj. existuje *druhá* fermion-počítací identita pro Λ, analogická té pro C²/Euler.
- **Opora (čísla):** F-003/F-014 — fermionový sektor je jediný, co nese −18/11; faktor 11 sdílen ve spektrální Euler (11/60) i anomálii (a_Weyl=11/720) = otisk téhož Diracova a₄. Spektrální akce je funkcí výhradně D (VYPOCET-11): a₀, a₂, a₄ jsou VŠECHNY fermionové momenty. Sacharovova logika (VYPOCET-11 část iii): graviton neběží ve smyčce → všechny gravitační členy jsou vakuová polarizace Diracova moře.
- **Test:** (a) **Spočítat a₀, a₂ pro C⊕H⊕M₃(C)** stejnou exaktní sympy aritmetikou jako VYPOCET-02 a zjistit, zda Λ_cc/M_Pl² má **racionální fermion-počítací formu** (analogickou −18/11). (b) **Srovnat s VYPOCET-03** (Λ~1/√V prefaktory): je NCG-indukovaná Λ slučitelná s κ_Sorkin=0,21 nebo κ_EDT=1,5e-3, nebo je to třetí, nezávislá hodnota? To by spojilo dva dosud oddělené Λ-programy (F-005 a NCG). (c) **Sen-typ kontrola:** je Λ_cc v indukované gravitaci chráněná veličina (jako −18/11) nebo běží s RG? Pokud běží, predikce je jen na unifikační škále.
- **Co by dalo:** uzavřelo by poslední riziko draftu-02 ("interpretace musí přežít, že akce obsahuje i kosmologický člen") a dalo H3g-4 **fyzikální predikci** mimo C²/Euler. Pokud Λ vyjde racionálně-fermionová, je to druhá index-chráněná identita → silný argument pro fermionovou indukci jako *mechanismus*, ne analogii. Potenciální draft-04 (a₄ → Λ).
- **Riziko (známé):** Λ-člen v NCG je notoricky citlivý na cutoff funkci f a na škálu unifikace; "predikce Λ" může být scheme-závislá tam, kde −18/11 (poměr konformních anomálií) scheme-robustní byl. Musí se ukázat, že existuje *poměr* (jako C²/Euler), který je f-nezávislý — jinak je predikce iluzorní. Toto je tvrdý filtr: pokud žádný takový poměr není, hypotéza padá čistě.

### H4g-4 — III→II přechod přežívá ve 4D na slabu, ne na diamantu

**(jádro: 4D rozšíření F-015 podmíněné F-016 geometrií; běží jako VYPOCET-16)**
**Confidence: medium-high** (dvě 4D opory se sbíhají: slab dává area [F-016] + 2D dává III→II [F-015]; chybí jen jejich spojení ve 4D).

- **Tvrdí:** numerický III₁→II přechod, prokázaný ve 2D (F-015: 80× kolaps stopy, modulární spektrum flat-dense→integrabilní), **přežije ve 4D — ale jen na slab/Rindler geometrii, ne na diamantu**. Důvod (spojení F-015 + F-016 + H4g-1): typová signatura žije ve stavu/entropii, a entropie ve 4D je area-law jen na slabu (kde SJ ≈ Unruh = Hadamard = III₁ regularizovatelná na II). Na diamantu rohová non-Hadamardovost (F-016) drží algebru v "nezkrotitelné" III₁ i po truncaci (volume law). **Predikce: modulární spektrum SJ na 4D slabu bude flat-dense→integrabilní (jako 2D), na 4D diamantu zůstane flat-dense i po truncaci.**
- **Opora (čísla):** F-015 — 2D III₁→II doložen 2/3 proxy (modulární spektrum nejjednoznačnější: pile-up ~N^1.14 → 0; husté ~N → integrabilní). F-016 — 4D slab dává area law S~L^2.00, diamant volume; Hadamardova diagnostika lokalizuje anomálii do rohů. F-011 — modular-hamiltonian TOP HUB. Pilíř 19 otevřený problém #6: "odvodit truncaci a vztáhnout ji k regulované entropii typu II".
- **Test (= VYPOCET-16):** aplikovat VYPOCET-12 modulární-spektrum proxy (ε=ln[μ/(μ−1)], entropická stopa, centrální sekvence) na **4D slab** (iΔ link, validovaný objekt, half-space cut) vs. **4D diamant**. Predikce: slab → integrabilní spektrum s IR hranou (typ II), diamant → flat-dense i po truncaci (zaseknutá III₁). Pokud slab dá II a diamant zůstane III → potvrzuje H4g-1+H4g-4 najednou. Pokud i slab zůstane III → III→II je 2D-only a entropy-cluster je ve 4D mrtvý algebraicky (i když ne entropicky).
- **Co by dalo:** rozšířilo by trojcestnou identifikaci (SSEE truncace = crossed-product cutoff = LQG area gap) ze 2D do 4D — první **4D algebraický pilíř** entropy-clusteru. Spolu s H4g-1 by uzavřelo H04 jako "žije ve 4D, modulárně vysvětleno".
- **Riziko:** 4D modulární spektrum z link matice může být deformované hustotou (mean links ~N^0.65), jak ukázal VYPOCET-06/09; pak by ani slab nedal čistou II hranu kvůli objektu, ne kvůli fyzice. Záložní test: BD objekt (VYPOCET-09) na slabu — opravil tvar spektra, mohl by dát čistší modulární hranu.

### H4g-5 — Probe = QRF: druhá veličina mimo d_s a SSEE potvrdí, že neshoda sond je crossed-product

**(formalizace through-line vrstvy A; zostření H3g-5)**
**Confidence: medium** (most doložen pilířem 19, ale stále jen dva příklady — d_s a entropie; potřebuje třetí mimo entropy-cluster).

- **Tvrdí:** through-line vrstva A je testovatelná: dvě sondy *libovolné* veličiny na témž causetu, které dávají různé odpovědi, jsou spojeny **vnitřním automorfismem** crossed-product algebry (relativní veličina invariantní). Toto NENÍ jen reinterpretace — je to predikce, že neshoda sond má **algebraickou strukturu** (modulární tok), ne libovolnou.
- **Opora (čísla):** F-001/02 — CST d_s=2 (d'Alembertián) vs. >D (random-walk) ze stejné teorie. F-006/07 — entropy-cutoff p=1/2 vs. discreteness-knee p=1 z téhož spektra (dvě fyzicky odlišné škály). F-015 — typ žije ve stavu, ne kinematice (= "na co se ptáš" rozhoduje strukturu). Pilíř 19: QRF = crossed product → entropie závislá na pozorovateli, invariant = relativní entropie (2412.15502).
- **Test:** (a) najít **třetí** veličinu (mimo d_s a SSEE) s probe-závislostí — kandidát: geodetická vs. kauzální vzdálenost na causetu, nebo Hausdorffova vs. spektrální dimenze. Ukázat, že dvě hodnoty jsou spojeny crossed-productem (relativní hodnota invariantní). (b) **Formálně:** spočítat, zda γ-volba v d_s=D/γ odpovídá volbě modulárního toku σ_t (různé γ = různé σ_t). Pokud ano, **probe-osa JE doslova modulární-tok-osa** — through-line vrstva A i B splynou.
- **Co by dalo:** druhý/třetí příklad probe=QRF mimo d_s by povýšil through-line z "dva případy" na "vzor". Pokud γ-volba = σ_t volba, sjednotí d_s-program s modulárním programem do jedné osy.
- **Riziko (L-1):** Sen IR-univerzalita — některé veličiny (log-koeficienty) jsou IR-určené a *žádná* sonda jimi nehne. Hypotéza musí ostře oddělit UV-relační od IR-univerzálních veličin (vyvraceč #3 z jednotící nitě), jinak kolabuje na H2g-7.

### H4g-6 — Geometrie-nezávislost SJ podpisů přežije změnu asymptotiky a topologie

**(uzavření H3g-6; třetí geometrie jako rozhodující test univerzality)**
**Confidence: medium-high** (BTZ↔Kerr replikace pevná; chybí třetí, asymptoticky/topologicky odlišná geometrie).

- **Tvrdí:** čtyři SJ signatury (existence v ergoregionu; null-slope nula na ergosféře; opačná znaménka A_caus/A_W; Ω^B zákon) jsou určeny **jen přítomností strhávání** (Ω≠0), ne asymptotikou (plochá vs. AdS) ani topologií. BTZ (3D, Λ<0) a Kerr (4D, plochý) už to doložily; třetí, *kvalitativně jiná* geometrie (Kerr-AdS = 4D+Λ<0, nebo Kerr-Newman = nabitý, nebo extrémní a→1) musí dát tytéž signatury.
- **Opora (čísla):** F-009 — všechny 4 BTZ signatury replikují na Kerru; null-slope EXAKTNĚ na r_erg=2M. F-017 — BTZ J=0,9 reprodukuje Ω^B vzorec (pattern_matches_kerr=True), ΔAIC=231. F-013 — BTZ↔Kerr eigenvektor-rotace ~45° v obou (cos²=0,507 Kerr, 0,509 BTZ).
- **Test:** **třetí geometrie** — Kerr-AdS (odděluje asymptotiku: 4D ale Λ<0 jako BTZ) je nejostřejší, protože izoluje "dimenze vs. asymptotika" (spojuje s H4g-2). Predikce: tytéž 4 signatury, B exponent dle asymptotiky. **Levnější:** extrémní a→1, kde ergosféra a horizont splývají — chování signatur v limitě. Pokud signatura zmizí/změní znaménko se změnou Λ/náboje → univerzalita padá, jde o vlastnost třídy.
- **Co by dalo:** uzavřelo by draft-01 jako "univerzální podpis strhávání", ne "dva příklady". Spolu s H4g-2 (exponent B) by oddělilo, co je univerzální (znaménka, existence) od toho, co závisí na geometrii (B).
- **Riziko:** Kerr-AdS má jiné okrajové podmínky (reflective AdS hranice) → SJ konstrukce může vyžadovat jinou prescription; není zaručeno, že bounded-region SJ je dobře definovaný. Test musí předem ověřit well-definedness (jako φ-periodicita u draftu-01).

---

## Výpočetní fronta v3

Seřazeno podle (decisiveness × proveditelnost × novost). **Běží:** VYPOCET-16 (III→II na 4D slabu). Fronta určuje, co po něm.

| # | Výpočet | Hypotéza | Náročnost | Co rozhodne | Stav |
|---|---|---|---|---|---|
| — | **VYPOCET-16 — III→II na 4D slabu vs. diamantu** (modulární spektrum proxy) | H4g-4 | týden | Přežije III₁→II ve 4D na slab geometrii? První 4D algebraický pilíř entropy-clusteru | **běží** |
| 1 | **Modulární tok SJ: slab vs. diamantový roh** (geometričnost K) | H4g-1 | dny–týden | Selhává boost-flow PŘESNĚ v rohu (kde non-Hadamard)? Spojí F-015+F-016 do mechanismu; testuje through-line vrstvu B. **Nejvyšší výnos: dotýká se jednotící nitě.** | další |
| 2 | **a₀/a₂ moment C⊕H⊕M₃(C) → Λ** (exaktní sympy, jako VYPOCET-02) | H4g-3 | hodiny–dny | Má Λ_cc/M_Pl² racionální fermion-počítací formu? Druhá index-identita; uzavírá riziko draftu-02. **Nejlevnější, navazuje na hotový VYPOCET-02/11.** | další |
| 3 | **Třetí geometrie SJ: Kerr-AdS** (4D+Λ<0) | H4g-6, H4g-2 | týden | Izoluje dimenzi vs. asymptotiku; testuje univerzalitu signatur i původ exponentu B najednou | další |
| 4 | **W_sr ~ Ω^B na 5D / Kerr-AdS** — disambiguace exponentu B | H4g-2 | týden | B z dimenze (D−1) nebo z asymptotiky pádu Ω? Falzifikovatelná predikce pro Teukolsky | další |
| 5 | **Hustší vzdálený scan r=5–20M** (Model E vs. S u a=0,6) | H4g-2 | dny | Uzavře poslední dvojznačnost VYPOCET-14 (lineární korelace ještě favorizuje E u a=0,6) | další |
| 6 | **Třetí probe-veličina** (geodetická vs. kauzální vzdálenost) + crossed-product test | H4g-5 | dny–týden | Druhý/třetí příklad probe=QRF mimo d_s/entropie; vzor místo dvou případů | další |
| 7 | **γ-volba = σ_t test** (d_s=D/γ ↔ modulární tok) | H4g-5 | dny | Splynou through-line vrstvy A a B? Probe-osa = modulární-tok-osa | další |
| 8 | **Proxy 3 vN typ s 30–50 seedy** (centrální sekvence) | H4g-4 | dny | Dorozhodne třetí proxy III→II (při 8 seedech nerozhodnuto); levný follow-up VYPOCET-12 | další |

**Doporučené pořadí po VYPOCET-16:** #2 (hodiny, nejlevnější, otevírá draft-04 kandidáta Λ) a #1 (dotýká se jednotící nitě, nejvyšší koncepční výnos) paralelně; pak #3 (Kerr-AdS, dvojí výnos H4g-6+H4g-2); pak #4–5 podle výsledku VYPOCET-16.

---

## Publikační stav

Tři drafty, tři režimy zralosti. Společný blokátor všech: **§0 lidská re-derivace + ověření citací proti arXiv** (žádný výpočet zatím nezávisle neproběhl mimo AI pipeline — gate item ve všech třech).

### draft-02 — a₄ fermionová identita: **VĚDECKY UZAVŘEN** (v0.1)

- **Stav:** VYPOCET-11 uzavřel **oba** zbývající výpočetní blokátory (graviton sektor + index-teorém). Fyzika je hotová: graviton identitu nezachrání (test #1), identita je index-chráněná (test #7). Spektrální akce = fermionově-indukovaná gravitace, dvojí souhlasící zákaz (Sacharovův + anomální).
- **Co zbývá k lidské revizi:** výhradně **framing + lidské ověření**, žádná fyzika. (a) §0 etika + lidská re-derivace VYPOCET-02/11; (b) §1 doložit novelty-gap citacemi z 1001.2036 a 1106.3263 (ukázat, že identitu poměru nikdo nenapsal); (c) §2 lidské otevření PDF a potvrzení každé Duff/Vassilevich/CC hodnoty; (d) §3 RG-running a podíl vnitřních fluktuací na C².
- **Verdikt:** nejhotovější aktivum projektu. Po lidské revizi → krátká exaktní nota.

### draft-01 — SJ na rotujících ČD: **v0.2** (nejsilnější nepokryté území)

- **Stav:** VYPOCET-10/14 uzavřely nejslabší bod (mechanismus opačných znamének): toy-model reprodukuje A_caus i A_W (korelace 0,95–0,97), W_sr~Ω^B s ΔAIC 230–4200, A_W záporně-definitní 65/65, eigenvektor-rotace ~45°. §3.5b a §4.2 zpevněny.
- **Co zbývá k lidské revizi:** (a) §4 **φ-periodicita** (odložený tvrdý problém — konečné okno vs. válcová topologie; blocking, priorita 3); (b) §7 ověření citací proti arXiv (blocking, priorita 1); (c) §8 lidská re-derivace VYPOCET-05/08/10 (gate); (d) §5 srovnání se známými vakui; (e) kvantitativní link B ↔ |R_lm|² potřebuje 4D Teukolsky.
- **Verdikt:** robustní, ale dva blokátory (φ-periodicita, Teukolsky) jsou reálná fyzika, ne jen framing. Plnohodnotný paper až po nich; mezitím draft drží.

### draft-03 — d_s(z,D,probe) klasifikátor: **v0.1** (review-note)

- **Stav:** engine reprodukovatelný (12/12), probe jako třetí osa projektově-originální.
- **Co zbývá k lidské revizi:** (a) §1 obrana proti "Calcagniho program přebalený" (method-by-method kontrast + poctivé přiznání ingrediencí); (b) §2 "probe je triviální" protiargument přes doložený databázový rozpor (edge 501 vs. 1539); (c) §3 per-row D-konvence (mix D=spacetime=4 vs. D_space=3 v Hořava vzorci — reálná dvojznačnost) + illustrative-8 poctivost; (d) ověření 11 arXiv ID.
- **Verdikt:** nižší novost (vzorec known od 2009), hodnota v syntéze. Review-note po framing-práci.

### Doporučení pro draft-04 — dva kandidáti

1. **★ DOPORUČENO: vN-typ III₁→II evidence — numerická nota.**
   **Proč:** VYPOCET-12 dodal **první numerický doklad** III₁→II přechodu na causetu (2/3 proxy: 80× kolaps stopy + modulární spektrum flat-dense→integrabilní). Modular-hamiltonian je TOP HUB; pilíř 19 dal algebraický jazyk. Toto je projektově-nejnovější výsledek (žádná surveyovaná práce neměří vN-typ proxy na causetu). **Blokátor pro povýšení na draft-04:** doběhnout VYPOCET-16 (4D slab) — pokud III→II přežije ve 4D na slabu, nota se rozšíří z "2D" na "2D + 4D geometrie-podmíněné" a stane se silným letterem. Pokud ne, zůstává poctivá 2D nota. **Doporučení: čekat na VYPOCET-16, pak rozhodnout.**

2. **slab/corner geometrie entanglementu — review-note.**
   **Proč:** VYPOCET-13 ukázal čistý geometrický fakt: ve 4D rozhoduje **geometrie regionu, ne dimenze** (slab→area S~L^2.00, diamant→volume), a Hadamardova diagnostika lokalizuje non-Hadamardovost do **rohů**. To je projektově-originální (Surya et al. studují diamanty, ale neizolují rohovou geometrii jako mechanismus). **Riziko:** literatura nepotvrzuje non-Hadamard↔volume jako přímý mechanismus → nota musí být formulována jako "geometrie rozhoduje + Hadamardova diagnostika lokalizuje", ne jako "non-Hadamard *způsobuje* volume". S H4g-1 (modulární tok v rohu) by dostala mechanismus.

**Strategický závěr:** draft-02 (a₄) je připraven k lidské revizi *teď* (vědecky uzavřen). draft-04 = **vN-typ III→II nota**, ale až po VYPOCET-16 (rozhodne 2D-nota vs. 2D+4D letter). slab/corner geometrie je silný kandidát na draft-05 nebo se sloučí s vN-typ notou jako její geometrická polovina (slab=area=II, diamant=volume=III — jeden příběh). draft-01 uzavřít až po φ-periodicitě + Teukolsky; draft-03 po framing-práci.

---

*Anchory čtvrtého kola: `core-data/calculations/{a4-graviton-index, sj-vn-type, ssee-slab-4d,
sj-threshold-scan}/` (VYPOCET-11…14); `knowledge-base/vypocty/VYPOCET-11…14`;
`knowledge-base/hypotezy/H04-entropy-cluster-reframe.md` (rozhodnutí (c) potvrzeno, (a) vyvráceno);
`papers/draft-02-a4-fermionic-identity/` (vědecky uzavřen); `core-data/findings.json` (F-001…F-017);
`core-data/concept-graph.json` (modular-hamiltonian TOP HUB, 614 nodů/2437 hran). Běží: VYPOCET-16
(III→II na 4D slabu).*
