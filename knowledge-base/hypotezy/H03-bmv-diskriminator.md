# H03 — BMV/GIE jako diskriminátor MEZI přístupy ke kvantové gravitaci

> **Status hypotézy:** Plausibilně nová ve framing dimenzii (viz `verification/novelty/preprint-checks.md` §b).
> **Vytvořeno:** 2026-06-06 · **Economy mode** (live web search + databáze projektu)
> **Rodičovské soubory:** `phenomenology/17-experimental-tests.md`, `approaches/03-asymptotic-safety.md`, `approaches/09-emergent-gravity.md`, `foundations/16-conceptual-problems.md`

---

## TL;DR

Standardní framing BMV/QGEM experimentů testuje **binaritu**: kvantová vs. klasická gravitace. Tato hypotéza navrhuje rozšíření na **diskriminaci mezi kvantovými přístupy** — perturbativní gravitonový EFT, asymptotická bezpečnost (AS), emergentní/entropická gravitace, stochastická/klasická gravitace (Oppenheim), GUP/minimální délka. Každý přístup předpovídá jiný tvar entanglementní fáze, dekoherenčního tempa nebo statistiky korelací. Verdikt této analýzy: binární test (quantum vs. classical) je v dosahu plánovaných experimentů; diskriminace mezi kvantovými přístupy je pravděpodobně mimo dosah stávajících plánů o 3–15 řádů, pokud neexistují nové teoretické derivace nízkoenergetických imprint.

---

## 1. Mapa aktuální debaty (2025 a novější)

### 1.1 Jádro sporu — Aziz–Howl vs. Marletto–Oppenheim–Vedral (2025)

Debata probíhá ve čtyřech hlavních dokumentech vydaných v rozmezí šesti měsíců:

**Aziz & Howl — Nature 2025 (arXiv: 2510.19714)**
*"Classical theories of gravity produce entanglement"*
Tvrzení: Při plném použití rámce kvantové teorie pole, kde kvantová hmota je vázána na klasické gravitační pole, mohou vyšší řády procesů generovat entanglaci mezi dvěma prostorově oddělenými hmotami prostřednictvím fyzikálně lokálních procesů. Důsledkem by bylo, že pozorování GIE *neimplikuje* kvantovost gravitace. Jde o přímý útok na logický základ celého QGEM programu.

**Marletto, Oppenheim, Vedral, Wilson — arXiv: 2511.07348**
*"Classical gravity cannot mediate entanglement"*
Odpověď: V nerelativistické limitě, které Aziz–Howl skutečně používají, se interakční hamiltonián redukuje na součet lokálních termů $H_{int} \approx V_1 + V_2$ — každý působí jen na jednu hmotu nezávisle. Klíčový vazební člen $\Phi/c^2(\nabla\hat\phi)^2$ je v nerelativistické limitě příliš malý a je zahazován. Bez tohoto členu unitární operátor faktorizuje a žádná entanglace z produktového vstupu nevzniká. Konzistentní analýza nemůže v nerelativistickém limitu uplatnit ultra-lokalitu pro výpočet fází a zároveň znovu zavést vazbu přes propagátor (kde se $k^2$ v jmenovateli vrátí).

**Schneider, Huggett, Linnemann — arXiv: 2511.19242**
*"A demonstration that classical gravity does not produce entanglement"*
Nezávislý argument pomocí Newton-Cartanovy formulace: pokud gravitace působí klasicky jako mediátor a je pozorována entanglace, pak musí být za entanglaci odpovědný jiný mechanismus. Navazuje na dřívější práci (arXiv: 2205.09013) a poskytuje geometricky transparentní důkaz.

**Sienicki & Sienicki — arXiv: 2511.20717**
*"Comment on Classical-Gravity–Quantum-Matter Claims About Gravity-Mediated Entanglement"*
Kanalový pohled: reformulace výsledku 2511.07348 jako **model-nezávislý argument** z teorie kvantových kanálů. Dále upřesňují rozdíl mezi *aktivací již existujícího entanglementu v hmotě* (která může proběhnout klasicky) a *skutečnou mediací entanglementu klasickým polem* (která nemůže). Klíčový závěr: standardní BMV inference — „pozorování GIE silně nasvědčuje nekvantickým gravitačním stupňům volnosti" — zůstává v platnosti.

**Gundhi, Infantino, Bassi — arXiv: 2604.19696 (2026)**
Nejnovější vstup: entanglement v Aziz–Howl modelu vzniká zahazováním přechodových amplitud; při jejich zahrnutí zůstává počáteční produktový stav produktovým po celou dobu vývoje.

### 1.2 Paralelní vývoj: co jde nad entanglament

**arXiv: 2506.04300 — "Beyond Entanglement: Diagnosing quantum mediator dynamics in gravitationally mediated experiments"**
Autoři zavádějí **dynamickou fidelity susceptibilitu** $\chi_F$ jako sondovací nástroj tří-oscilátorového systému (dva terminální + mediátor). Klíčový objev: kvantový mediátor ve **heavy-mediator regime (HMR)** — kde efektivní hmota mediátoru diverguje a kinetický člen z hamiltoniánu mizí — se chová dynamicky jako „zmrzlý" a entanglament terminálních oscilátorů může být nulový nebo lokalizovaný, i když mediátor je stále kvantový. To znamená, že **absence entanglementu != klasickost mediátoru**. $\chi_F$ rozlišuje HMR od LMR (light-mediator regime) i tam, kde entanglamentní míry selhávají. Relevance pro BMV: plánovaný experiment pracuje s ne-dynamickým Newtonským potenciálem — což je přesně HMR aproximace. Je otázka, zda by alternativní pozorovatelné (korelace hybností, $\chi_F$) mohly poskytnout jemnější diagnostiku.

---

## 2. Tabulka predikcí pro BMV setup

Referenční parametry: hmotnost $m = 10^{-14}$ kg, vzdálenost center $d_\mathrm{min} = 35$ µm, velikost superpozice $\Delta x \sim 1$–10 µm, čas $\tau = 1$ s.

Gravitační fáze v standardním (EFT) přístupu:
$$\phi \approx \frac{Gm^2\,\tau}{\hbar\,r}, \quad r \approx d_\mathrm{min}$$

Pro výše uvedené parametry: $\phi \sim Gm^2\tau/(\hbar \cdot 35\,\mu\text{m}) \approx 10^{-3}$–$10^{-2}$ rad (závisí na geometrii), tedy řádově jednotky mrad — na hranici detekovatelnosti entanglamentním svědkem.

| Přístup | Mechanismus entanglamentu | Kvalitativní predikce fáze / viditelnosti | Škála odchylky od EFT | Komentář |
|---|---|---|---|---|
| **Perturbativní graviton EFT** (standardní) | Výměna virtuálních gravitonů (spin-2), Newtonský limit plné kvantové gravitace; zahrnuje jednosmyčkové kvantové korekce | $\phi_\mathrm{EFT} = Gm^2\tau/(\hbar r)$ plus jednosmyčkové kvantové korekce $\delta\phi \sim (G\hbar/r^3)(m/r)$ řádu $\sim 10^{-4}$ relativní korekce; viditelnost plná při splnění dekoherenčních požadavků | Referenční hodnota; jednosmyčkové korekce $\sim G\hbar/(r^3\tau^{-1})\ll 1$ — zcela neměřitelné v plánovaných parametrech | Newtonský potenciál je constraint (ne dynamický stupeň volnosti) — role gravitonu v GIE je konceptuálně sporná, výsledek entanglamentu je ale jednoznačný |
| **Asymptotická bezpečnost (AS)** s běžícím $G(k)$ a anomálním rozměrem $\eta$ | Totéž jako EFT, ale Newtonova konstanta teče: $G(k) \to g^*/k^2$ pro $k\gg k_\mathrm{Pl}$; gravitonový propagátor se mění jako $\sim p^{-2(1-\eta/2)}$ | Modifikace potenciálu na škálách $r\lesssim\ell_\mathrm{Pl} \sim 10^{-35}$ m — tj. o 30 řádů menší než plánovaná separace; na škálách BMV teorie předpovídá *přesně* Newtonský potenciál | Odchylka $\sim (k\,\ell_\mathrm{Pl})^{2+\eta}$ nastupuje až u $r\sim\ell_\mathrm{Pl}$; v BMV setup neměřitelná ($\delta\phi/\phi\sim(\ell_\mathrm{Pl}/d)^2\sim10^{-60}$) | V rámci AS platí nízkoenergetická decoupling — žádný fenomén nižší energie není signifikantně modifikován. Detekce GIE by *potvrdila* kvantovost gravitace konzistentní s AS, ale nerozlišila by AS od EFT |
| **Emergentní/entropická gravitace (Verlinde)** | Gravitace jako emergentní entropická síla — není fundamentální mediátor; zákon síly $F = -T\,\nabla S$ z holografické entropie na informačních obrazovkách | Nejasné, zda entropická síla může generovat entanglement — konzistentní kvantový mechanický popis Verlindeho teorie na mikroskopické úrovni neexistuje; v koherentní superpozici by entropická síla závisela na průměrné poloze, ne na větvi vlnové funkce | Pokud Verlindeho model funguje jako klasický mediátor (průměrná poloha), předpovídá *nulový* entanglement nebo podstatně nižší korelace; pokud je formulace kvantová, splyne s EFT | Fundamentální problém: Verlindeho teorie nemá dokončenou mikroskopickou kvantovou formulaci. GIE bez Newtonského EFT mechanismu by bylo *falzifikací* emergentní gravitace — nebo by vynutilo kvantifikaci entropického mechanismu |
| **Stochastická/klasická gravitace (Oppenheim — postquantum theory)** | Gravitační pole zůstává klasické ($g_{\mu\nu}$ = c-číslo), kvantová hmota se s ním interaguje přes klasicko-kvantovou dynamiku; teorie je konzistentní, ale vyžaduje *ireducibilní fluktuace* metriky | **Predikce:** žádný gravitačně zprostředkovaný entanglement, ale charakteristická **zkřížená dekoherence** a **korelace pohybů** dvou oscilátorů přes stochastické fluktuace pole; identifikovatelný $\pi$-fázový posun v křížové korelaci vzdáleného od rezonance | Dekoherenční signatura nastupuje na škálách, kde je $\varepsilon\neq 0$ (parametr stochasticity); při $\omega = 2\pi \cdot 100$ Hz, $\gamma = 2\pi \cdot 10^{-3}$ Hz jsou křížové korelace měřitelné bez makroskopické superpozice | Oppenheimova teorie předpovídá *jiný typ experimentu* — ne entanglement, ale korelace pohybu. Pozorování GIE by Oppenheimovu teorii vyloučilo; nepozorování GIE je konzistentní s jeho teorií ale nedokazuje ji (nutno měřit křížové korelace) |
| **GUP / minimální délka** | Deformace komutačních relací $[\hat x, \hat p] = i\hbar(1+\beta\hat p^2)$ implikující minimální délku $\Delta x_\mathrm{min}\sim\sqrt\beta\,\ell_\mathrm{Pl}$; modifikuje gravitační potenciál na $r\sim\ell_\mathrm{Pl}$ a mění statistiku superpozicí | Modifikace fáze: $\delta\phi_\mathrm{GUP}/\phi \sim \beta(m/m_\mathrm{Pl})^2\cdot(\ell_\mathrm{Pl}/\Delta x)^2$; pro $\Delta x\sim 1$ µm a $m\sim10^{-14}$ kg to dává $\delta\phi/\phi\sim\beta\cdot10^{-52}$ | Jedině pokud by $\beta\gg1$ (extrémně liberální meze), mohla by být modifikace měřitelná; standardní meze $\beta\lesssim10^{34}$ (z AURIGA/LIGO dat) stále nestačí — odchylka $\sim10^{-18}$ nebo méně | GUP modifikuje i dekoherenční tempo superpozic; sekundární efekt na schopnost udržet koherentní stav po $\tau=1$ s by byl $\sim\beta\cdot(m\omega\Delta x/\hbar)^2$ — rovněž neměřitelný v plánovaném rozsahu |

---

## 3. Experimentální parametry a jejich rozlišovací schopnost

### 3.1 Parametry plánovaných experimentů (QGEM 2025)

Klíčové parametry ze skenování parametrického prostoru s elektromagnetickým stíněním (arXiv: 2502.12474):

| Parametr | Rozsah / Optimum |
|---|---|
| Hmotnost $m$ | $10^{-15}$–$10^{-14}$ kg (NV centrum v diamantu) |
| Minimální separace $d_\mathrm{min}$ | 35 µm (s EM stíněním, původně 200 µm) |
| Velikost superpozice $\Delta x$ | 1–70 µm (závisí na $m$ a dekoherenci) |
| Dekoherenční tempo $\gamma$ | $10^{-4}$–$10^{-1}$ Hz (cíl: $\lesssim 10^{-3}$ Hz) |
| Čas interakce $\tau$ | 1 s |
| Gravitační fáze $\phi$ | $\sim 10^{-3}$–$10^{-2}$ rad (řád jednotky mrad) |
| Optimální setup | 2-qubitový paralelní setup, 3-qubitový pro vyšší $\gamma$ |

Entanglamentní svědek $\langle W\rangle < 0$ (nebo ekvivalentní spinová korelace) je detekován, pokud $\phi\gtrsim\phi_\mathrm{crit}(\gamma,\tau)$ — s dekoherenčním tempem $\gamma\lesssim10^{-3}$ Hz to je splnitelné pro $m=10^{-14}$ kg a $\Delta x\gtrsim 1$ µm.

### 3.2 Co by rozlišilo různé přístupy

**Test 1: Pozorování GIE (entanglament YES/NO)**

- Výsledek: entanglament **detekován**
  - Konzistentní s: EFT, AS, GUP (marginálně)
  - Vyloučen: Oppenheimova postkvantová teorie (jako výhradní mechanismus), Verlinde (v interpretaci klasického mediátoru)
  - Nezodpovězeno: který *kvantový* přístup platí

- Výsledek: entanglament **nedetekován**
  - Konzistentní s: Oppenheim (nutno ověřit křížové korelace), Verlinde, nebo technické selhání superpozice
  - Nezodpovězeno: neimplikuje přímo žádný specifický přístup

**Test 2: Tvar závislosti $\phi(m, r, \tau)$**

Pokud by bylo možné systematicky měnit $m$, $r$, $\tau$ přes několik řádů:

- EFT: $\phi \propto m^2/r$ bez modifikace (do $r\gg\ell_\mathrm{Pl}$)
- AS: totéž v plánovaném rozsahu, ale pro hypotetické $r\lesssim$ nm by se $G(r)$ změnilo
- GUP: $\phi_\mathrm{eff} = \phi_\mathrm{Newton}\cdot[1 + \beta\,f(m,\Delta x)]$ — hypotetically detekovat při $\beta\gg1$ a $\Delta x\to\ell_\mathrm{Pl}$
- Oppenheim: $\phi=0$ (entanglement), ale $C_{12}(\omega)\neq 0$ (křížové korelace)

**Test 3: Dekoherence-entanglement trade-off (Oppenheimův signál)**

Oppenheimova teorie predikuje **korelaci pohybů** dvou gravitačně interagujících oscilátorů přes stochastická pole — bez potřeby makroskopické superpozice. Pro $\omega = 2\pi\cdot 100$ Hz, $\gamma = 2\pi\cdot 10^{-3}$ Hz by charakteristický $\pi$-fázový posun v křížové korelační funkci $C_{12}(\Delta t)$ byl identifikovatelný. Tento test je na technicky jiné úrovni obtížnosti než QGEM — nevyžaduje superpozici, jen přesná mechanická měření.

### 3.3 Srovnání s plánovanými experimenty

| Otázka | Plánované QGEM ($m\sim10^{-14}$ kg, $d\sim35$ µm) | Realistické hodnocení |
|---|---|---|
| Quantum vs. klasická gravitace (binarita) | **V dosahu** — detekce GIE certifikuje kvantovost | Technicky extrémně náročné, ale principiálně dosažitelné do 2030+ |
| EFT vs. AS (kvantové korekce k potenciálu) | **Mimo dosah** — efekt $\sim10^{-60}$ relativní | Vyžadovalo by experimenty u $r\sim$nm, mimo technologický horizont |
| EFT vs. Verlinde (emergentní mediátor) | **Částečně v dosahu** — absence GIE by byl negativní test | Pozitivní detekce GIE by vyžadovala kvantifikaci Verlindeho mechanismu nebo jeho falsifikaci |
| EFT vs. Oppenheim (cross-korelace) | **Možné v alternativním experimentu** — bez superpozic | Paralelní typ experimentu (osmilátory, křížové korelace), technicky odlišný od QGEM |
| GUP/minimální délka korekce | **Mimo dosah** — efekt $\sim\beta\cdot10^{-52}$ | Vyžadovalo by $\beta\gg10^{18}$ nebo experiment u nanometrových oddělení |

---

## 4. Verdikt: je diskriminace realistická?

### Stručný závěr

**Binární test (quantum vs. classical) je v dosahu — diskriminace MEZI kvantovými přístupy není.**

Detailní posouzení podle přístupu:

**AS vs. EFT:** Oba přístupy předpovídají *identickou* Newtonskou entanglamentní fázi na škálách $r\gg\ell_\mathrm{Pl}$. AS je UV úplný a jeho nízkoenergetická decoupling zajišťuje, že žádná modifikace EFT predikce není viditelná nad $\sim\ell_\mathrm{Pl}^2/r^2\sim10^{-60}$ úrovní relativní korekce. **Diskriminace nemožná v plánovaných experimentech.**

**Verlinde vs. EFT:** Verlindeho entropická gravitace nemá mikroskopicky konzistentní kvantový popis koherentních superpozic. Pokud GIE bude detekováno, Verlindeho model v klasické interpretaci bude *vyloučen* jako výhradní mechanismus gravitace. To je jeden z nejzajímavějších potenciálních výsledků QGEM. Pokud ale Verlinde přijme, že jeho teorie přechází v EFT při kvantové kohercenci, test se stane neprůkazný.

**Oppenheim vs. EFT:** Toto je *skutečně diskriminovatelný* kontrast — ale ne přímým QGEM. Oppenheimova teorie předpovídá:
1. Nulový gravitačně zprostředkovaný entanglement (měřitelný v QGEM)
2. Charakteristický vzor křížových korelací pohybů (měřitelný v alternativním mechanickém experimentu)
Tyto dvě predikce mohou být testovány, i když s různými typy experimentů. Sada (1) + (2) by poskytnula silnou diskriminaci.

**GUP vs. EFT:** Modifikace jsou pod jakýmkoliv technologicky dosažitelným prahem, pokud neexistují specifické modely s $\beta\gg1$. Marginálně otevřená otázka: jsou-li fenomenologické meze na $\beta$ z AURIGA/LIGO dat ~$10^{34}$, stále zbývá prostor pro $\delta\phi/\phi\sim10^{-18}$, což je pod BMV citlivostí.

**Novost framingu (evaluace):** Standardní literatura diskutuje BMV jako test quantum vs. classical. Rámování jako diskriminátor *mezi* kvantovými přístupy se v hlavní literatuře explicitně nevyskytuje (potvrzeno analýzou `verification/novelty/preprint-checks.md`). Nejblíže jsou práce analyzující implikace GIE pro různé semi-klasické přístupy (Oppenheim, Diósi-Penrose), ale systematické srovnání AS, EFT, Verlinde, Oppenheim, GUP v jednom rámci nebylo nalezeno v literatuře do 2026-06.

### Doporučené další kroky pro projekt

1. **Derivovat AS korekci k entanglamentní fázi** — formálně: modifikovaný Newtonský potenciál z AS (Bonanno–Reuter 2000) aplikovat na BMV fázový výpočet, kvantifikovat $\delta\phi/\phi$.
2. **Verlinde formalizace** — pokusit se o konzistentní kvantový popis GIE v entropickém rámci; kde se teorie rozchází?
3. **Oppenheim-QGEM interface** — navrhnout hybridní experiment: BMV + oscilátorové křížové korelace ve stejném aparátu.
4. **GUP BMV výpočet** — explicitní výpočet modifikace entanglamentní fáze s GUP deformovanými komutátory; hledat parametrický prostor, kde efekt není triviálně nulový.

---

## Reference

- Aziz & Howl (2025) — *Classical theories of gravity produce entanglement*, Nature; arXiv: 2510.19714
- Marletto, Oppenheim, Vedral, Wilson (2025) — *Classical gravity cannot mediate entanglement*, arXiv: 2511.07348
- Schneider, Huggett, Linnemann (2025) — *A demonstration that classical gravity does not produce entanglement*, arXiv: 2511.19242
- Sienicki & Sienicki (2025) — *Comment on Classical-Gravity–Quantum-Matter Claims*, arXiv: 2511.20717
- Gundhi, Infantino, Bassi (2026) — arXiv: 2604.19696 (korekce k Aziz-Howl)
- (Bez jmen) — *Beyond Entanglement: Diagnosing quantum mediator dynamics*, arXiv: 2506.04300; Phys. Rev. D (2025)
- Bose et al. (2017) — BMV návrh, arXiv: 1707.06050; Marletto & Vedral (2017), arXiv: 1707.06036
- *Parameter scanning in QGEM experiment with electromagnetic screening*, arXiv: 2502.12474 (2025)
- Oppenheim (2023) — *A Postquantum Theory of Classical Gravity?*, Phys. Rev. X 13, 041040
- Oppenheim et al. — *Distinguishable consequence of classical gravity on quantum matter*, arXiv: 2309.09105; Phys. Rev. Lett. 134, 061501 (2025)
- Reuter & Saueressig — *Asymptotic Safety*, Living Review + monografie (2019)
- Verlinde (2011) — *Gravity as an Entropic Phenomenon*, arXiv: 1011.4106
- Niedermaier & Reuter (2006) — Living Reviews in Relativity, AS přehled

---

*Soubor vytvořen research-dossier agentem (economy mode) ze živých zdrojů 2026-06-06.*
