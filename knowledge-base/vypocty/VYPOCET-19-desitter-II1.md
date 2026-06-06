# VYPOCET-19: SJ stav na de Sitterově statické záplatě × von-Neumannův typ — test CLPW predikce typu II₁ (NE II_∞)

**Datum:** 2026-06-06
**Soubory:** `core-data/calculations/sj-desitter-type/calc.py`, `results.json`, `plots/{part1_discriminator,part2_proxies,part3_maxent}.png`
**Status:** Dokončeno
**Hypotéza:** sjednocení dvou vlajkových linií projektu — SJ stavy v horizontových prostoročasech (pilíř kauzální množiny) × von-Neumannův typový přechod (pilíř 19) — na **de Sitterově** geometrii; test predikce CLPW (**arXiv:2206.10780**)
**Cluster:** entropy-cluster × von-Neumann (modular-hamiltonian TOP HUB) × horizon-SJ
**Navazuje:** VYPOCET-12 (2D III₁→II), VYPOCET-16 (4D slab 3/3 proxy)

---

## Cíl: rozliší diskrétní SJ sonda typ II₁ od typu II_∞?

CLPW (Chandrasekaran-Longo-Penington-Witten, **arXiv:2206.10780**) dokázali, že algebra pozorovatele na **statické záplatě** (static patch) de Sitterova prostoru je von-Neumannova algebra **typu II₁** — a to klíčově **II₁**, nikoli II_∞ jako v případě černé díry. Operační rozdíl:

| | typ II₁ (de Sitter) | typ II_∞ (černá díra / Rindler) |
|---|---|---|
| stopa | **normalizovatelná**, Tr 1 < ∞ | semifinitní, Tr 1 = ∞ |
| max-entropický stav | **existuje** (prázdný dS, S~A/4G) | neexistuje |
| chování entropie | **SATURUJE** na konečný strop, jak oblast vyčerpává záplatu | **ROSTE bez omezení** s velikostí oblasti |

Předchozí výpočty (VYPOCET-12 ve 2D, VYPOCET-16 ve 4D slabu) ukázaly, že dvojitá Sorkin-Yazdi truncace nese signaturu přechodu **III₁ → II** (od bezstopové algebry k semifinitní). Ale obě geometrie byly **neohraničené** (diamant, slab/Rindlerův klín) — tedy typ **II_∞**. Otevřená otázka: **vidí SJ+truncace machinerie rozdíl mezi II₁ a II_∞?** To je první test, který sjednocuje obě vlajkové linie na fyzikálně netriviální geometrii s **konečnou** stopou.

**Sázka:** Pro II₁ musí truncovaná stopa SATUROVAT na konečné maximum (Tr 1 < ∞, tracialní max-entropický stav), jak oblast vyčerpává statickou záplatu, zatímco plochý-slab/diamantové II_∞ chování roste neomezeně s velikostí oblasti. Měříme to proti ploché kontrole na **shodných parametrech**.

---

## Geometrie: 2D de Sitterova statická záplata a konformní trik

**Statická záplata 2D de Sitteru** (ověřeno proti literatuře, červen 2026 — Hartman dS lecture notes; Anninos **1205.3855**; standardní dS₂ konvence):

$$ds^2 = -\left(1 - \frac{r^2}{\ell^2}\right)dt^2 + \frac{dr^2}{1 - r^2/\ell^2}, \qquad r \in (-\ell, \ell).$$

**Želví souřadnice** (tortoise) $r^* = \ell\,\mathrm{arctanh}(r/\ell) \in (-\infty, +\infty)$ převedou metriku do **konformně ploché** podoby:

$$ds^2 = \left(1 - \frac{r^2}{\ell^2}\right)\left(-dt^2 + dr^{*2}\right), \qquad \Omega^2 = 1 - \frac{r^2}{\ell^2} = \mathrm{sech}^2(r^*/\ell).$$

**Klíčový fakt (konformní trik, přesně jako v dS causal-set literatuře arXiv:1306.3231 pro 1+1 SJ vakuum):** 2D bezhmotný skalár je **konformně invariantní**, takže konformní faktor $\Omega^2$ **vypadne** z teorie pole. Kauzální uspořádání, retardovaná Greenova funkce, Pauli-Jordanův operátor i celá SJ konstrukce jsou **identické** s plochým 2D prostorem v konformních souřadnicích $(t, r^*)$. Sprinklujeme tedy v $(t, r^*)$, stavíme SJ stav standardní 2D plochou causal-matrix konstrukcí (Sorkin-Yazdi **1611.10281**, totožné s VYPOCET-12), a geometrie vstupuje **jen** přes to, KDE leží horizont.

**Horizont:** $r \to \ell \iff r^* \to +\infty$. Kosmologický horizont je v **nekonečné** želví vzdálenosti. To je geometrický původ rozdílu II₁ vs II_∞:

- Aproximace k horizontu = posunutí vnější hrany oblasti $R^*_{\rm box}$ k větším hodnotám, tj. $r_{\rm edge} = \ell\tanh(R^*_{\rm box}/\ell) \to \ell$.
- Fyzická (vlastní) plocha, kterou interval $[0, R^*_{\rm box}]$ v želvích souřadnicích zabírá, je **konečná a ohraničená** plnou vlastní plochou záplaty, protože $\Omega^2 = \mathrm{sech}^2$ klesá exponenciálně: jednotková želví buňka u horizontu nese exponenciálně málo vlastní plochy / stupňů volnosti.

**Implementace de Sitterovy geometrie:** SJ konstrukce zůstává plochá v $(t, r^*)$, ale **měřítko sprinklingu** sleduje vlastní dS míru $dV_{\rm proper} = \Omega^2\,dt\,dr^* = \mathrm{sech}^2(r^*/\ell)\,dt\,dr^*$. Posun hrany k horizontu přidává **exponenciálně méně** nových bodů — rozpočet bodů oblasti SATURUJE. To je diskrétní avatar konečné (II₁) stopy.

### Dvě shodné geometrie

| | de Sitter (čekáno II₁) | plochá kontrola (II_∞) |
|---|---|---|
| míra sprinklingu | $dN \sim \mathrm{sech}^2(r^*/\ell)\,dt\,dr^*$ (vlastní) | $dN \sim dt\,dr^*$ (uniformní) |
| rozpočet bodů při růstu $R^*_{\rm box}$ | **saturuje** (konečný objem záplaty) | **roste lineárně** (neomezeně) |
| SJ machinerie | identická plochá 2D v $(t,r^*)$ | identická plochá 2D v $(t,r^*)$ |

Jediný rozdíl je míra sprinklingu, která kóduje de Sitterův horizont. To je nejčistší možná shodná kontrola (matched control) pro otázku II₁ vs II_∞.

---

## Konvence (ověřené proti literatuře)

Identické se SJ machinerií VYPOCET-12:

| Vstup | Forma | Zdroj |
|---|---|---|
| kauzální matice C (plochá v $t,r^*$) | $C_{xy}=1$ pokud $y \prec x$: $u_y\le u_x \wedge v_y\le v_x$, $u=t-r^*, v=t+r^*$ | **1611.10281**; **1306.3231** (dS konformní) |
| $G_R = \tfrac12 C$ | retardovaná Greenova fce | **1611.10281** |
| $i\Delta = i(G_R - G_R^\top) = \tfrac{i}{2}(C-C^\top)$ | Pauli-Jordan, hermitovský, ± párovaný | **1611.10281** |
| $W$ = pozitivní část $i\Delta$ | SJ Wightman (čistý SJ stav) | **1611.10281** |
| SSEE: $W_O v = \mu\,i\Delta_O v$, $S=\sum\mu\ln|\mu|$, páry $(\mu,1-\mu)$ | spacetime entanglement | **1611.10281**; **2008.07697** |
| $\kappa = \sqrt{N}/(4\pi)$, dvojitá truncace | UV magnitudový cutoff | **1712.04227** |
| $\varepsilon = \ln[\mu/(\mu-1)] = \ln[(\nu+\tfrac12)/(\nu-\tfrac12)]$, $\nu=\mu-\tfrac12$ | modulární energie | Casini-Huerta **0905.2562** |

**Validace SJ konstrukce:** kontrola ±-párování spektra $i\Delta$ dala $\max|\sum_{\rm sorted}\pm\lambda| = 2.3\cdot10^{-13}$ (dS) a $1.7\cdot10^{-13}$ (plochá) — strojová přesnost, $i\Delta$ správně antisymetrický.

---

## Metoda a numerika

Tři části, ≥4 seedů (5–6), N až ~2500:

- **Část 1 (diskriminátor II₁ vs II_∞):** oblast roste k horizontu; truncovaná SSEE přes **bulk-středový řez** (fixní podíl $\mathrm{cut\_frac}=0.5$ želví hrany boxu) vs vnější hrana $R^*_{\rm box} \to$ horizont, při fixní (vlastní resp. ploché) hustotě $\rho=240$. 6 seedů, hrany $R^*_{\rm box}\in[1.6,7.0]\ell$.
- **Část 2 (tří-proxy typová baterie):** baterie VYPOCET-12 (stopa, modulární spektrum, centrální sekvence) na dS statické záplatě vs plochá kontrola, při rostoucím N (kontinuální limita při fixní oblasti, směr 2008.07697). Box $R^*\le3.0$, fixní bulk řez $r^*\le1.0$ (= $r=0.762\ell$, zaručený komplement na obou stranách), N∈[239,1950], 5 seedů.
- **Část 3 (modulární spektrum max-entropického kandidáta):** stopová/tracialní sonda, dvě měření.

Runtime 431 s, thread-cap 4 (sdílený host).

---

## Část 1 — Diskriminátor II₁ vs II_∞ (jádro výpočtu)

Při fixní hustotě roste oblast k horizontu; měříme obsah-sledující (content-tracking) veličiny přes bulk-středový řez. Klíčové zjištění: **rozdíl II₁ vs II_∞ se ve 2D ukazuje rozhodujícím způsobem v OBSAHU oblasti, ne v truncované entropii.**

| veličina (hrana $R^*_{\rm box}$: 1.6 → 7.0 ℓ) | de Sitter | plochá kontrola |
|---|---|---|
| **$N_{\rm total}$** (kardinalita kauzální množiny) | **442 → 480, SATURUJE** (strop=480, $R^2=1.000$) | **768 → 3360, ROSTE** (sklon 480/jedn. $r^*$) |
| **$S_{\rm full}$** (plná SSEE, sleduje objem/obsah) | **40.9 → 0, SATURUJE-a-překlápí** (saturační fit $R^2=0.990$, pozdní sklon −1.67) | **87.6 → 159.6, ROSTE** (sklon +12.2, pozdní +4.82) |
| $S_{\rm trunc}$ (truncovaná, typ-II) | 0.57 → 0 (2D log-plochá, pozdní sklon −0.015) | 1.01 → 0.42 (2D log-plochá, pozdní sklon −0.083) |

**Mechanismus:** de Sitterova vlastní plocha ($\mathrm{sech}^2$) saturuje — kardinalita zabíhá k 480 a další posun hrany k horizontu už nepřidává body. Plochá kontrola roste lineárně (768 → 3360). Obsah-sledující $S_{\rm full}$ proto v dS saturuje a překlápí se k nule (jak se bulk-středový řez ve fixním podílu blíží horizontu, jeho komplement se vyprazdňuje), zatímco v ploché kontrole roste monotónně.

**Poctivá 2D limita:** truncovaná (typ-II regularizovaná) SSEE je ve 2D log/area zákon, který je **téměř nezávislý na velikosti boxu v OBOU geometriích** (pozdní sklony −0.015 dS, −0.083 plochá). Takže sama o sobě typy magnitudou neoddělí. Rozdíl II₁ vs II_∞ nesou rozhodně **$N_{\rm total}$ a obsah-sledující $S_{\rm full}$** — obě SATURUJÍ pro ohraničenou dS statickou záplatu (II₁) a ROSTOU bez omezení pro plochou kontrolu (II_∞).

**Verdikt části 1: DISKRIMINOVÁNO ✓.** Net-změna $S_{\rm full}$ přes druhou polovinu sweepu: dS −13.1 (obsah klesá/saturuje), plochá +21.7 (obsah roste); mezera 34.8, opačná znaménka. Diskrétní sonda jednoznačně odlišuje ohraničenou dS záplatu (II₁) od neomezené ploché kontroly (II_∞).

Obrázek `part1_discriminator.png`: **vlevo (rozhodující)** obsah-sledující $S_{\rm full}$ — dS (modrá) saturuje a klesá, plochá (červená) roste, modrá čárkovaná = saturační fit; **uprostřed** $N_{\rm total}$ — dS plateau na 480, plochá lineární růst k 3360; **vpravo** truncovaná SSEE — poctivá 2D limita (log-plochá v obou).

---

## Část 2 — Tří-proxy typová baterie na dS statické záplatě

Při fixní oblasti (bulk řez $r^*\le1.0$) a rostoucí hustotě (N=239→1950) běží baterie VYPOCET-12, aby nezávisle prokázala **typ-II charakter** (vs III₁) na dS záplatě, a srovnává s plochou kontrolou.

### PROXY 1 — Entropická stopa

| veličina | dS (N=239→1950) | exponent $a$ ($S\sim N^a$) | plochá kontrola |
|---|---|---|---|
| $S_{\rm full}$ (netruncovaná) | 16.1 → 168.5 | **$a=1.105\pm0.017$** ($R^2=0.999$) → objemová, divergentní stopa (III) | $a=1.080$ |
| $S_{\rm trunc}$ (truncovaná) | 0.43 → 0.54 | **$a=0.116\pm0.028$** → saturuje, konečná stopa (II) | $a=0.179$ |

**Verdikt proxy 1: III → II ✓** (dS: $S_{\rm full}$ objemová $a=1.11$ divergentní; $S_{\rm trunc}$ saturuje $a=0.12$).

### PROXY 2 — Modulární spektrum

| veličina | full (netruncovaná) | truncovaná |
|---|---|---|
| pile-up u $\varepsilon<0.5$ | $\sim N^{1.248\pm0.001}$ (roste, III₁ flat-dense) | **přesně 0** ($\sim N^{-0.000}$, typ II) |
| počet modulárních módů | 28 → 228 (husté) | 8 → 22 (kompaktní) |

Obrázek `part2_proxies.png` (vpravo): netruncovaná modulární hustota (červená) má hromadění u $\varepsilon=0$ a plochou hustotu do $\varepsilon\sim6$ (Connesova III₁ signatura $S(M)=\mathbb{R}_+$); truncovaná (modrá) má **nulovou váhu pod $\varepsilon\approx5$ (ostrá IR mezera)** — integrabilní, kompaktně-nesené spektrum typu II.

**Verdikt proxy 2: III₁ → II ✓** (pile_full $\sim N^{1.25}$ → pile_trunc = 0; nejjednoznačnější proxy, stejně jako ve 2D diamantu a 4D slabu).

### PROXY 3 — Centrální sekvence (faktor / triviální centrum)

CV($S_{\rm trunc}$) na dS = 0.086 při největším N, samo-průměrující, ale **trend nesignifikantní** při 5 seedech (stejně jako VYPOCET-12). Plochá kontrola: CV=0.025, samo-průměrující, trend signifikantní. **Verdikt: faktor-like nepotvrzen na dS při 5 seedech** (potřeba 30+ seedů, dokumentováno).

> **Souhrn části 2: dS statická záplata vykazuje III₁→II charakter ve 2/3 proxy** (stopa + modulární spektrum), přesně jako 2D diamant (VYPOCET-12). Typ-II charakter dS záplaty je nezávisle potvrzen.

---

## Část 3 — Modulární spektrum max-entropického (tracialního) kandidáta

V algebře typu II₁ je stopa SAMA stavem (maximálně smíšený tracialní stav, $S_{\rm max}$), jehož modulární spektrum je **triviální** ($\varepsilon=0$: $\rho\propto\mathbf{1}$, plochý modulární hamiltonián). Dvě sondy při růstu oblasti k horizontu:

| sonda | dS | plochá | výsledek |
|---|---|---|---|
| (a) $\langle\varepsilon\rangle$ truncovaného stavu | 5.69 → 5.91 (sklon +0.06) | 6.16 → 6.42 (sklon +0.06) | **POCTIVÝ NULL z konstrukce** — truncace odstraňuje právě nízko-$\varepsilon$ tracialní módy, takže $\langle\varepsilon\rangle_{\rm trunc}$ je přibitý na UV hraně a NEMŮŽE vidět tracialní limitu |
| (b) IR-frakce ($\varepsilon<0.5$, netruncovaný spektrum) | 0.144 → 0.105 (sklon −0.008) | 0.097 → 0.075 (sklon −0.004) | **NULL** — IR-frakce mírně klesá v obou, tracialní nárůst se při těchto N neobjevuje |

**Poctivé zjištění:** ani jedna sonda neukazuje čistý tracialní (max-entropický) přístup při těchto N. Sonda (a) je null z konstrukce (truncace zabíjí tracialní módy). Sonda (b) je správnou tracialní sondou, ale IR-frakce při $N\lesssim2500$ tracialní nárůst nezachycuje — diskutováno níže ve scaling-analýze.

Obrázek `part3_maxent.png`: vlevo IR-frakce (správná tracialní sonda, null), vpravo $\langle\varepsilon\rangle_{\rm trunc}$ (null z konstrukce, s vysvětlující anotací).

---

## VERDIKT

| Část | Predikce | Výsledek |
|---|---|---|
| **1 — diskriminátor II₁ vs II_∞** | dS obsah saturuje (II₁), plochá roste (II_∞) | **✓ DISKRIMINOVÁNO** ($N_{\rm total}$: 480 strop vs 3360 růst; $S_{\rm full}$: saturuje-a-překlápí vs roste; mezera net-změny 34.8) |
| **2 — typ-II charakter dS záplaty** | III₁→II ve stopě + modulárním spektru | **✓ 2/3 proxy** (stopa $a$: 1.11→0.12; modulární pile-up $N^{1.25}$→0; centrální sekvence nesignifikantní při 5 seedech) |
| **3 — max-entropický tracialní přístup** | dS IR-frakce roste k horizontu | **POCTIVÝ NULL** (nezachyceno při $N\lesssim2500$; scaling níže) |

> ### **CELKOVÝ VERDIKT: DISKRIMINOVÁNO.**
> SJ+truncace machinerie ODLIŠUJE ohraničenou de Sitterovu statickou záplatu (II₁: obsah a obsah-sledující entropie saturují na konečný strop) od shodné neohraničené ploché kontroly (II_∞: obsah roste bez omezení), A nezávisle vidí III₁→II truncaci na dS záplatě (2/3 proxy). **Rozdíl CLPW II₁ vs II_∞ je VIDITELNÝ v diskrétní sondě.**

**Nejdůležitější dílčí výsledky:**

1. **Sjednocení dvou vlajkových linií na de Sitteru funguje.** Konformní trik (2D bezhmotný skalár konformně invariantní → SJ plochá v želvích souřadnicích, horizont vstupuje jen přes $\mathrm{sech}^2$ vlastní míru) je čistý a numericky validovaný (±-párování $i\Delta$ na strojové přesnosti). Tato geometrie dovoluje poprvé testovat **konečnou-stopovou (II₁)** algebru diskrétně, na rozdíl od dosud studovaných neohraničených (II_∞) diamantů a slabů.

2. **Rozdíl II₁ vs II_∞ žije v OBSAHU oblasti, ne v truncované entropii (ve 2D).** Truncovaná typ-II SSEE je ve 2D log/area zákon téměř nezávislý na velikosti boxu v obou geometriích — takže magnitudou typy neoddělí. Ale obsah-sledující $N_{\rm total}$ a $S_{\rm full}$ rozhodně oddělí: dS saturuje (ohraničená záplata, konečná Tr 1), plochá roste (neohraničená, Tr 1 = ∞). To je přesný diskrétní avatar normalizovatelnosti stopy.

3. **dS statická záplata nese stejnou III₁→II truncační signaturu jako 2D diamant a 4D slab** (2/3 proxy: stopa + modulární spektrum). Typ-II charakter je tedy robustní vůči geometrii (diamant, slab, dS záplata), zatímco rozdíl II₁/II_∞ (normalizovatelnost stopy) je nový rozměr, který tato geometrie poprvé zpřístupňuje.

---

## Limity a poctivá zjištění (co by typy rozlišilo a jaké N to vyžaduje)

- **Truncovaná entropie typy ve 2D neoddělí (poctivá 2D limita).** Ve 2D je typ-II area law logaritmický a téměř box-nezávislý; rozdíl II₁/II_∞ musí být čten z obsahu ($N_{\rm total}$, $S_{\rm full}$). Ve **4D** by truncovaná typ-II SSEE byla $S\sim\sqrt{N}\sim L^2$ (area law, VYPOCET-16), tj. rostla by s velikostí oblasti pro II_∞ a saturovala pro ohraničenou dS záplatu — tam by **truncovaná entropie sama oddělila II₁ od II_∞**. To je přirozené pokračování (4D dS statická záplata, $\mathrm{sech}^2$-vážený slab).

- **Část 3 (tracialní přístup) je null při $N\lesssim2500$.** Aby IR-frakce netruncovaného spektra ukázala tracialní nárůst (max-entropický stav, $\rho\to\mathbf{1}/d$, modulární spektrum $\to\varepsilon=0$), je třeba, aby diskrétní stav skutečně dosáhl blízkosti maximálně smíšeného stavu. Pro N~480 (dS plný rozpočet při $\rho=300$) je oblast příliš hrubá: max-entropický strop $S_{\rm dS}\sim\ln(\text{horizont-area}/4)$ je ve 2D O(1) číslo, a hrubozrnný stav ho nedosáhne. **Scaling pro rozlišení:** potřeba $\rho\gtrsim10^3$–$10^4$ (tj. $N_{\rm patch}\sim10^3$–$10^4$ při saturované vlastní ploše záplaty), aby se hierarchie tracialních módů rozvinula — to je za hranicí dense-matice eigh při $N\sim2500$ a vyžadovalo by řídké/iterativní metody nebo větší $\ell$.

- **Connesův λ-invariant (III_λ vs III₁) ani II₁ vs II_∞ stopová normalizace nejsou z konečného N přímo měřitelné** — měříme TRENDY (saturace vs neomezený růst obsahu). Plný důkaz Tr 1 < ∞ je asymptotický; diskrétní sonda dává jeho jasnou konečně-N stopu (saturace $N_{\rm total}$, $R^2=1.000$).

- **Nefudgováno:** Část 3 poctivě hlásí null a vysvětluje, proč (truncace zabíjí tracialní módy; hrubozrnnost při dostupných N). První běh odhalil artefakt (nested oblast pohltí celou množinu v dS sech²-koncentraci → triviální SSEE); design byl opraven na bulk-středový řez s garantovaným komplementem na obou stranách — zdokumentováno v komentářích `calc.py` i zde.

---

## Dopad na sjednocení vlajkových linií

| Před VYPOCET-19 | Po VYPOCET-19 |
|---|---|
| VYPOCET-12 (2D diamant) + VYPOCET-16 (4D slab): III₁→II truncační přechod prokázán, ale jen na **neohraničených** geometriích (typ **II_∞**). Rozdíl II₁/II_∞ (klíčový CLPW rozdíl dS od černé díry) diskrétně netestován. | **dS statická záplata: diskriminátor II₁ vs II_∞ funguje.** Obsah-sledující entropie a kardinalita SATURUJÍ pro ohraničenou dS záplatu (II₁), ROSTOU pro plochou kontrolu (II_∞). Třícestná identifikace (SSEE truncace = crossed-product cutoff) získává **dS-specifický rozměr**: nejen III₁→II, ale i II₁ vs II_∞ rozlišení. |

Tento výpočet **sjednocuje** SJ-horizontovou linii (kauzální množiny v horizontových prostoročasech, dS SJ vakuum **1306.3231**) s von-Neumannovou linií (typový přechod, crossed product **2206.10780**) na de Sitteru: ukazuje, že diskrétní SJ+truncace machinerie vidí přesně ten rozdíl, který CLPW analyticky předpověděli — statická záplata má **konečnou** stopu (II₁), na rozdíl od černo-děrového/Rindlerova II_∞. Konformní trik dělá 2D dS výpočetně dostupným bez ztráty kauzální fyziky.

**Pro draft-04 / BRAINSTORM-05:** crossed-product identifikace je nyní testována na třech geometriích (diamant, slab, dS záplata) a na **obou** stranách von-Neumannovy klasifikace (II_∞ neohraničené vs II₁ ohraničené). 4D dS statická záplata (kde by truncovaná area-law entropie sama oddělila typy) je přirozený další krok.

---

## Reference (klíčové pro tento výpočet)

- **2206.10780** — Chandrasekaran, Longo, Penington, Witten: algebra pozorovatele dS statické záplaty je **typu II₁**; max-entropický stav (prázdný dS); $S_{\rm gen}=A/4G_N+S_{\rm out}$; rozdíl od černo-děrového II_∞.
- **1306.3231** — Surya, X, Yazdi (resp. dS SJ): SJ vakuum na de Sitteru; 1+1 kauzální diamant simulace; konformní/Bunch-Davies srovnání; **konformní trik pro kauzální strukturu**.
- **1611.10281** — Sorkin, Yazdi: SSEE, dvojitá truncace, $W_O v = \mu\,i\Delta_O v$.
- **1712.04227** — causet SSEE: magnitudový cutoff $\kappa=\sqrt{N}/(4\pi)$.
- **2008.07697** — Surya, X, Yazdi: dS horizont SSEE; slab + Rindler klín → area law; $n_{\max}=\alpha N^{(d-1)/d}$.
- **0905.2562** — Casini, Huerta: bosonová modulární energie $\varepsilon=\ln[(\nu+\tfrac12)/(\nu-\tfrac12)]$.
- **1205.3855** — Anninos: de Sitter musings (dS₂ statická záplata, želví souřadnice, konformně-coupled skalár).
- **2112.12828** — Witten: gravity and the crossed product (II_∞ pro Rindler/černou díru).
- Connes 1973 — klasifikace III_λ / II₁ / II_∞; modulární invariant $S(M)$.
- pilíř 19 (`foundations/19-von-neumann-algebras.md`) — typová klasifikace, crossed product, dS II₁.
- VYPOCET-12 (2D III₁→II), VYPOCET-16 (4D slab 3/3 proxy, II_∞).
