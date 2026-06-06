# Dimenze jako otázka, kterou prostoročasu položíš

> ⚠️ **SPEKULATIVNÍ ESEJ — fantazie odbrzděná, fakta citována, extrapolace značeny.**
>
> Tento text záměrně přepíná mezi dvěma režimy. Oddíly **„Co víme"** jsou střízlivé,
> citované, opřené o naše vlastní výpočty (`knowledge-base/vypocty/`) a o publikovanou
> literaturu. Oddíly **„Co kdyby"** jsou odbržděné — extrapolace, metafory, odvážné
> domyšlení do důsledků. Každý takový skok **začíná u konkrétního výsledku** z báze a je
> značen `⟶ EXTRAPOLACE`. Závěrečný oddíl **„Co by muselo být pravda"** stahuje fantazii
> zpět na zem: vypisuje falzifikovatelné jádro celé vize. Co není značeno jako extrapolace,
> je míněno doslovně a má citaci.

---

## Prolog: špatně položená otázka

Po staletí jsme se prostoročasu ptali špatně. Ptali jsme se: *„Kolik máš dimenzí?"* — jako
bychom se ptali kamene, kolik váží. Čekali jsme číslo. Atribut. Vlastnost, kterou prostoročas
*má*, tak jako má kámen hmotnost, nezávisle na tom, kdo se ptá a čím měří.

Tahle esej tvrdí něco kacířského: že otázka *„kolik dimenzí má vesmír"* nemá odpověď ve formě
čísla. Že má odpověď ve formě **funkce** — funkce toho, *jak se ptáš*. A že tahle závislost na
způsobu dotazu není defekt našich měřicích nástrojů, který by se dal odladit, nýbrž je to
**ontologie**: prostoročas nemá dimenzi, dokud mu ji nezměříš, a měření je vždy dotaz, který
má svou gramatiku, svůj nástroj, svou sondu.

Tahle teze se v naší bázi nezrodila jako filozofická spekulace. Vypadla z numeriky. Konkrétně
ze čtyř výpočtů a jednoho vyřešeného rozporu. Začněme tím nejtvrdším.

---

## 1. Co víme: tatáž množina, dvě protichůdné dimenze

Spektrální dimenze $d_s$ je definovaná operačně. Pustíš difúzní proces (náhodnou procházku,
nebo tepelné jádro $e^{-\sigma F(k)}$) a sleduješ návratovou pravděpodobnost $P(\sigma)$ — jak
pravděpodobně se chodec po „čase" $\sigma$ vrátí domů. Spektrální dimenze je sklon

$$d_s(\sigma) = -2\,\frac{d\ln P}{d\ln\sigma}.$$

Na hladké 4-varietě dostaneš $d_s = 4$ na všech škálách. Pointa kvantové gravitace je, že v UV
to číslo *neutekne* na 4. V asymptotické bezpečnosti, CDT, Hořava–Lifshitz, multifrakcionálních
prostorech a (debatovaně) v kauzálních množinách padá $d_s$ k hodnotě kolem 2 (`SYNTEZA.md`,
oddíl „shody" #1; uzel `spectral-dimension` má degree 28). Tahle konvergence k dvojce se dlouho
prodávala jako *nejsilnější univerzální cross-approach observable* — společný otisk, který by
mohl znamenat, že všechny přístupy míří na totéž.

Náš `VYPOCET-01` (`vypocty/VYPOCET-01-ds-klasifikace.md`) tu konvergenci rozebral jediným
enginem. Symbolicky (sympy) i numericky (12 validačních kontrol, tolerance 0,06) ukázal, že
pro izotropní propagátor s UV mocninou $F \sim k^{2\gamma}$ platí uzavřený master-vzorec

$$\boxed{\,d_s^{\mathrm{UV}} = D/\gamma\,}.$$

GR ($\gamma{=}1$) dá 4. Stelle, asymptotická bezpečnost a causal-set d'Alembertián ($\gamma{=}2$,
propagátor $\sim k^4$) dají 2. Hořava $z{=}2$ dá $5/2$. **Dvojka tedy není univerzální konstanta;
je to shoda jediné podtřídy** — té s UV propagátorem $\sim k^4$. GR, Hořava $z{=}2$ a další
„dvojku" explicitně porušují. Zdánlivá univerzalita byla optický klam způsobený tím, že nejvíc
studované přístupy náhodou padly do téhož $\gamma{=}2$ kbelíku.

Ale to není ten nejtvrdší výsledek. Ten nejtvrdší je tohle: **causal sety dají na otázku po své
vlastní UV dimenzi dvě protichůdné odpovědi — podle toho, kterou sondou se zeptáš.**

- Pustíš-li na kauzální graf **d'Alembertián** (Benincasa–Dowker, nelokální spojitý operátor,
  arXiv:1507.00330), $d_s$ **klesá** k univerzální 2 ve všech dimenzích. Dimenzionální redukce.
- Pustíš-li **náhodnou procházku** po témže kauzálním grafu (Eichhorn–Mizera, arXiv:1311.2530),
  $d_s$ v UV **roste** nad $D$ (náš ilustrativní fit dal 8).

Stejná teorie. Stejná množina bodů. Stejné kauzální relace. **Opačný trend.** A není to chyba
měření — je to fyzika lorentzovské nelokality: hyperbola konstantního vlastního času protíná
v causetu nekonečně mnoho bodů (`approaches/05-causal-sets.md`, ř. 39), takže kauzální graf má
divokou konektivitu, kterou náhodný chodec „cítí" jako vysokou dimenzi, zatímco regularizovaný
d'Alembertián ji utlumí a „cítí" nízkou.

Tahle dvojznačnost dokonce vyřešila vnitřní rozpor v našich datech. Dvě hrany v
`connections.json` (edge 501 a edge 1539; viz `verification/ds-contradiction.md`) tvrdily
opačné věci — jedna „$d_s$ klesá", druhá „$d_s$ roste" — a roky se to bralo jako bug. Není to
bug. **Obě hrany měly pravdu.** Jen každá mlčky zobecnila ze své sondy. Klasifikátor spektrální
dimenze není dvojice $(z, D)$. Je to **trojice $(z, D, \text{sonda})$.**

Tady, přesně tady, se láme střízlivost do fantazie. Protože pokud je sonda rovnocenná osa
klasifikace vedle dimenze a exponentu — pokud odpověď „kolik dimenzí" *nelze* položit bez
specifikace nástroje — pak slovo „dimenze vesmíru" nemá referent. Má jen referent vzhledem
k dotazu.

---

## 2. Co kdyby: dimenze nebyla atribut, ale odpověď

⟶ **EXTRAPOLACE** (start: `VYPOCET-01` probe-dependence; `ds-contradiction.md`).

Dovolme si to domyslet úplně. Co kdyby `VYPOCET-01` nebyl technický detail o tom, jak se měří
difúze na grafech, ale **prototyp toho, jak je strukturovaná každá geometrická vlastnost
prostoročasu**?

Představme si prostoročas ne jako objekt s vlastnostmi, ale jako **respondenta**. Sedí naproti
tobě a ty mu kladeš otázky. Otázka má vždy dvě části: *co* se ptáš (dimenze? vzdálenost?
entropie? kauzální budoucnost?) a *čím* se ptáš (difúzní chodec? d'Alembertián? geodetika?
modulární tok? horizont nějakého pozorovatele?). A respondent odpoví — ale odpověď je společným
dílem otázky a respondenta, ne čtením předem napsaného atributu.

Tahle metafora má ostře jiné důsledky než obvyklý realismus. V obvyklém obrazu má prostoročas
dimenzi 4 (nebo $4{\to}2$ s nějakým crossover), tečka, a různé sondy ji jen *aproximují* s
různou chybou. V odbržděném obrazu **neexistuje žádné „skutečné" $d_s$ za zády sond**, ke
kterému by se sondy přibližovaly. Causet *nemá* UV dimenzi. Má rodinu odpovědí
$\{d_s^{\text{d'Alembert}} = 2,\; d_s^{\text{random walk}} > D,\; \dots\}$ a tahle rodina **je**
to, co o jeho dimenzionalitě existuje. Číslo „2" a číslo „8" nejsou dvě měření jedné věci. Jsou
to dvě věci.

Je to morální analog kontextualitě v kvantové mechanice. Tam nemá částice současně ostrou
polohu i hybnost; ptáš-li se na polohu, vyrobíš odpověď „poloha", a ta vylučuje koexistující
ostrou „hybnost". Co kdyby geometrie byla **kontextuální stejně radikálně**? Co kdyby
„spektrální dimenze d'Alembertiánem" a „spektrální dimenze náhodnou procházkou" byly
*komplementární observable* — dvě otázky, na něž nelze odpovědět současně jedním číslem, protože
nesdílejí společnou ontologickou bázi, na níž by ležely?

⟶ **EXTRAPOLACE** (start: master-vzorec $d_s = D/\gamma$).

A teď to nejdivočejší. Master-vzorec $d_s = D/\gamma$ říká, že UV dimenze je $D$ dělené mocninou
propagátoru. Ale propagátor *je* způsob, jak pole cítí prostor mezi dvěma body — je to sama
definice „sousedství". Co kdyby tedy $\gamma$ nebyl parametr teorie, ale **parametr otázky**?
Co kdyby každý fyzikální proces nesl svůj vlastní $\gamma$, a tedy svou vlastní efektivní
dimenzi — a „dimenze vesmíru" by byla jen tou dimenzí, kterou vidí proces, jímž zrovna měříme?
Foton vidí jednu dimenzi, neutrino jinou, gravitační vlna třetí, a všechny mají pravdu, protože
každý nese jiné $\gamma$. Prostoročas by pak byl **dimenzionálně polyfonní**: ne jedna melodie
(„je 4-rozměrný"), ale akord, jehož tóny jsou efektivní dimenze viděné různými poli.

---

## 3. Co víme: entropie, která neexistuje, dokud nezvolíš nůž

Druhý pilíř téhle eseje je entropie. A ten je možná ještě tvrdší než dimenze, protože tady
nejde o „kterou sondou", ale o ještě základnější věc: **kde useknout**.

Náš `VYPOCET-04` (`vypocty/VYPOCET-04-ssee-diamant.md`) spočítal Sorkin–Johnstonovu spacetime
entanglement entropy (SSEE) na poissonovsky rozsetém 2D kauzálním diamantu. Postup je
kanonický a citovaný řádek po řádku (Sorkin–Yazdi arXiv:1611.10281): retardovaný Green
$G_R = \tfrac12 C$, Pauli–Jordanův operátor $i\Delta$, Wightmanova funkce jako jeho kladná část,
restrikce na subdiamant, zobecněný problém vlastních čísel, $S = \sum_\mu \mu \ln|\mu|$.

A výsledek je dramatický. **Bez useknutí spektra je entropie 95,2 — roste s objemem (volume
law), diverguje, je to „type-III-like" divoká stopa bez konečné hodnoty.** Teprve dvojitou
truncací spektra na Sorkin–Yazdiho škále $\kappa = \sqrt{N}/4\pi$ (arXiv:1712.04227) spadne na
**1,58** — konečná, area/log-law, „type-II-like". Naměřili jsme, jak poloha toho řezu škáluje
s hustotou: entropický cutoff jde jako $N^{0,519\pm0,007}$, tedy $\varepsilon \sim \rho^{-1/2}$
(potvrzuje předpověď $\varepsilon \sim \rho^{-1/d}$ ve 2D; vylučuje alternativu $\rho^{-1/4}$ na
39 σ). Log-zákon má sklon $b = 0{,}49$ — správné znaménko i řád vůči spojité hodnotě $1/3$.

Čtěme to pomalu. **Entanglement entropie prostoročasové oblasti není definovaná veličina.** Než
zvolíš cutoff, je nekonečná (resp. roste s objemem bez meze). Po volbě cutoffu je konečná. A
hodnota — dokonce *zákon škálování* (area vs. volume) — závisí na tom, **kde řízneš**. Entropie
nečeká hotová uvnitř oblasti, aby ji pozorovatel přečetl. Entropie **vzniká aktem regularizace**.

Tohle není ojedinělost causetů. Je to tatáž struktura, kterou objevil program crossed-product
algeber v holografii (`foundations/16-conceptual-problems.md`, oddíl o crossed product;
`cross-cutting/13-entanglement-spacetime.md`, třetí vlna). Lokální algebra QFT v podoblasti je
typu III$_1$ — **nemá stopu, nemá dobře definovanou entropii**, entanglement přes hranici
diverguje. Teprve když přidáš **pozorovatele** — hodiny s omezeným spektrem, kvantový referenční
rámec — udělá se z type III crossed-productem type II, a *teprve type II má stopu a konečnou
entropii*, která se ukáže být přesně zobecněnou entropií $S_{\text{gen}} = A/4G_N + S_{\text{out}}$
(CLPW arXiv:2206.10780; Witten arXiv:2112.12828; Kudler-Flam–Leutheusser–Satishchandran
arXiv:2309.15897).

A pointa, na kterou jsme čekali: De Vuyst, Eccles, Höhn a Kirklin (arXiv:2412.15502) dokázali,
že **kvantový referenční rámec a crossed product jsou tatáž věc**. Přidat pozorovatele = vzít
crossed product = zkonstruovat entropii. Bez pozorovatele entropie *neexistuje*, ne ve smyslu
„je velká", ale ve smyslu „není to dobře položená otázka" (`16-conceptual-problems.md`:
„gravitační entropie je *observer-dependent*").

Naše dvě nezávislé linie — causet SSEE truncace (`VYPOCET-04`) a crossed-product type-II
konstrukce — říkají **mechanicky totéž**: divergentní (volume-law / type-III) stopa se stane
konečnou (area-law / type-II) teprve volbou — cutoffu, resp. pozorovatele. Novelty-check
(`verification/novelty/entropy-cluster.md`) přiznává, že trojcestná identifikace SSEE truncace
= LQG area gap = crossed-product cutoff *není v literatuře* — a `VYPOCET-04` ji poprvé
mechanicky podpořil: $\varepsilon \sim \rho^{-1/2}$ je kandidátní modulární cutoff.

---

## 4. Co kdyby: pozorovatel jako součást definice geometrie

⟶ **EXTRAPOLACE** (start: `VYPOCET-04` truncace + crossed-product = QRF, arXiv:2412.15502).

Spojme oba pilíře. `VYPOCET-01` říká: *dimenze* je odpověď na otázku, nese ji sonda. `VYPOCET-04`
plus crossed product říká: *entropie* je odpověď na otázku, nese ji volba cutoffu / pozorovatele.
Co kdyby to nebyly dvě izolovaná zjištění, ale **dvě instance jednoho zákona**?

Nazvěme ho — odbržděně — **principem relačnosti geometrie**:

> *Žádná geometrická veličina prostoročasu (dimenze, entropie, vzdálenost, objem, kauzální
> struktura) není atribut, který by oblast „měla". Každá je odpovědí na dvojici (otázka, sonda),
> a sonda je vždy nějaký kvantový referenční rámec — pozorovatel, pole, hodiny, řez. Geometrie
> není věc, je to relace mezi tím, co se ptá, a tím, nač se ptá.*

Tohle je radikalizace toho, co program „It from Qubit" už dělá napůl. Van Raamsdonk (2010)
ukázal, že rozpojíš-li entanglement, prostoročas se roztrhne (`13-entanglement-spacetime.md`):
geometrie *vyrůstá* z kvantových korelací, není fundamentální. Faulkner et al. (2014) odvodili
linearizované Einsteinovy rovnice z prvního zákona entanglementu — *gravitace plyne z
termodynamiky entanglementu, nepostuluje se*. Jacobson (1995) totéž z $\delta Q = T\,dS$ na
Rindlerově horizontu. Ale tyhle výsledky pořád nechávají geometrii být **něčím, co je tam** —
jen je to udělané z entanglementu místo z metriky.

⟶ Odbržděný krok dál: co kdyby geometrie nebyla *udělaná* z entanglementu, nýbrž **byla
formátem odpovědí** na otázky kladené entanglementem? Modulární Hamiltonián $H_A$ je pro kulovou
oblast generátorem boostu (Casini–Huerta–Myers 2011); modulární tok $\rho_A^{it}$ je
Tomita–Takesakiho čas (`13-entanglement-spacetime.md`, ř. 45) a half-sided modular inclusion je
*kandidát na emergenci času*. V tomhle světle:

- **Vzdálenost** = odpověď na otázku „jak silně jsou tyhle dvě oblasti entanglované" (mutuální
  informace $I(A{:}B)$; její vymizení = roztržení prostoročasu, Van Raamsdonk).
- **Čas** = odpověď na otázku „jaký je modulární tok algebry, kterou pozoruješ" (half-sided
  modular inclusion → translace; `emergence-of-time` je nejširší sdílený open-problem v
  `SYNTEZA.md`).
- **Entropie** = odpověď na otázku „kterého pozorovatele jsi přidal" (crossed product, type II).
- **Dimenze** = odpověď na otázku „kterou sondou difunduješ" (`VYPOCET-01`).
- **Objem** = u causetu doslova „kolik atomů jsi napočítal" (Order + Number = Geometry,
  `05-causal-sets.md`).

Vidíš ten vzorec? **Každá geometrická veličina se rozpustila ve dvojici (otázka, rámec).** A pak
přestává dávat smysl mluvit o „prostoročasu" jako o samostatném jsoucnu před otázkami. Zůstává
**síť možných dotazů a jejich odpovědí** — a tu síť nazýváme prostoročasem zkratkovitě, asi jako
nazýváme „osobností" konzistentní vzorec odpovědí člověka na situace, ač žádná „osobnost" jako
oddělená věc uvnitř lebky není.

⟶ **EXTRAPOLACE** (start: QRF = crossed product; observer-dependent $S_{\text{gen}}$).

Dotáhněme to do nejzazší polohy. Pokud je pozorovatel *součástí definice* entropie — ne někdo,
kdo ji zvenčí měří, ale komponenta, bez níž ta veličina není ani dobře položená — pak
**pozorovatel není v prostoročase. Pozorovatel je v geometrii samé.** Quantum reference frame
není zařízení uvnitř geometrické scény; je to *jedna z os, podél nichž se geometrie vůbec
definuje*. Změna QRF (De Vuyst et al.: „superpozice souřadnicových transformací") pak není pohyb
v daném prostoru, ale **přechod mezi dvěma geometriemi** — dvěma různými soubory odpovědí.

Vesmír bez pozorovatele by v téhle vizi neměl dimenzi 4, ani 2, ani žádnou. Neměl by entropii.
Neměl by ani jasný čas. Měl by **jen kauzální/algebraickou kostru schopnou odpovídat** — a
teprve dotaz nějakého rámce z ní vyřízne konkrétní geometrii. Wheelerovo „It from Bit" se zde
ostří na **„It from Question"**: jsoucno z otázky.

---

## 5. Co víme: tři varovné příběhy o nepřenosnosti

Než fantazie utече úplně, musíme citovat tři výsledky, které drží otěže. Všechny tři jsou
*negativní* — a právě proto cenné, protože ukazují, kde relačnost narazí na tvrdou strukturu.

**(a) Univerzalita má hranice — `VYPOCET-03`.** Hypotéza, že tři nezávislé odvození kosmologické
konstanty (Sorkin $\Lambda \sim 1/\sqrt V$, EDT, CosMIn) realizují *tutéž* fluktuační statistiku
$\delta\Lambda \sim 1/\sqrt N$, byla v silné formě **vyvrácena**
(`vypocty/VYPOCET-03-lambda-prefaktory.md`): prefaktory $\kappa$ se liší faktorem ~140
(Sorkin 0,2136 vs. EDT $1{,}53\times10^{-3}$), a žádnou volbou konvence to nesladíš — je to
intrinsický rozdíl. CosMIn navíc nemá fundamentální $\kappa$ vůbec; predikuje fixní číslo. Sdílí
se jen *dimenzionální* struktura $\Lambda \sim H^2$, ne numerika.

**(b) Spektrální shoda neznamená totožnost — `VYPOCET-02`.** Nekomutativní geometrie skoro
jednoznačně vybírá algebru Standardního modelu $\mathbb{C}\oplus\mathbb{H}\oplus M_3(\mathbb{C})$
(`approaches/07-noncommutative-geometry.md`). Náš `VYPOCET-02`
(`vypocty/VYPOCET-02-a4-matching.md`) testoval, zda Seeley–DeWittův koeficient $a_4$ spektrální
akce reprodukuje anomální poměr $c/(-a)$. Výsledek je chirurgicky rozdvojený: ve **fermionové
části PŘESNĚ POTVRZENO** (poměr $-18/11$ je exaktní pro 45 i 48 fermionů — Diracův $a_4$ je týž
v obou počítáních), ale v **plné SM verzi (s bosony) JEDNOZNAČNĚ VYVRÁCENO** ($-0{,}853$ vs. cíl
$-1{,}636$). Krásná dílčí shoda; falešná globální.

**(c) Sonda nemá nekonečnou svobodu.** I `VYPOCET-01` má hranice: IR limita je *vždy* 4 pro
všechny sondy. Random walk i d'Alembertián na causetu se v IR shodnou na $D{=}4$. Relačnost
neznamená libovůli — sondy se v makroskopickém režimu sjednotí.

Tyhle tři výsledky jsou kotvy. Říkají: relačnost geometrie není „všechno je relativní a nic
neplatí". Je to *strukturovaná* závislost na rámci — s pevnými body (IR dimenze 4), s exaktními
podshодami (Diracův sektor $a_4$), a s tvrdými mezemi nepřenosnosti (140× rozdíl
$\Lambda$-prefaktorů). Fantazie smí létat jen v prostoru, který tyhle kotvy vymezují.

---

## 6. Co kdyby: UV-kompletnost jako kompletnost slovníku otázek

⟶ **EXTRAPOLACE** (start: `VYPOCET-01` $d_s = D/\gamma$ závisí na sondě; `VYPOCET-03` nepřenosnost
prefaktorů; `13-entanglement-spacetime.md` emergence).

Tady přijde největší pojmový obrat, který tahle vize nabízí. Co *je* „UV-kompletní teorie"?

V dosavadním obrazu je UV-kompletnost vlastnost teorie: teorie je UV-kompletní, dává-li konečné
odpovědi na všech škálách až k nekonečné energii. Hledá se jedna pravá UV teorie — Reuterův
fixní bod, kontinuální limita CDT, spin-foam limita — a `SYNTEZA.md` (H2) doufá, že jsou *táž
věc*. `VYPOCET-01` ale tuhle naději oslabil: UV $d_s$ závisí na sondě, takže ani „UV dimenze"
není přístupově univerzální (`VYPOCET-01`, §5.3 přímo oslabuje cluster L2-5 o jednom Reuterově
fixním bodě).

⟶ Odbržděný návrh: **Co kdyby UV-kompletnost nebyla vlastnost teorie, ale úplnost jejího
slovníku otázek?** V relačním obrazu nemá smysl ptát se „je teorie konečná v UV". Smysl má jen
ptát se „je teorie konečná v UV *vzhledem k téhle sondě*". A protože sond je celá rodina (každé
pole, každý $\gamma$, každý QRF), pak:

> UV-kompletní teorie není ta, která dá jedno konečné číslo na vysoké škále. Je to ta, která má
> **konzistentní odpověď na každou legitimní otázku** — pro každou sondu, každý referenční rámec,
> každý $\gamma$ existuje konečná, vzájemně kompatibilní odpověď. UV-kompletnost = kompletnost
> slovníku, ne konečnost čísla.

To má krásný důsledek. „Trans-Planckovský problém" (`SYNTEZA.md`, sdílený open-problem napříč
quantum-cosmology, semiclassical, NCG, CST) — strach, že Hawkingovo spektrum nebo CMB závisí na
neznámé UV fyzice — se v tomhle obrazu **rozpouští do správně položené otázky**. Ne „jaká je
pravá UV fyzika za horizontem", ale „závisí *tahle konkrétní sonda* (Hawkingovy fotony,
Hadamardovo vakuum) na detailu cutoffu, nebo je vůči němu robustní?". A to je přesně otázka,
kterou by řešil výpočet SJ vakua na sprinklované černé díře (`SYNTEZA.md`, bílé místo #14). Sonda
sama říká, zda je trans-Planckovsky robustní — některé odpovědi jsou na cutoffu nezávislé (to je
ta robustnost), jiné ne, a relační teorie tyhle dvě třídy rozliší místo aby se bála „pravé UV".

⟶ **EXTRAPOLACE** (start: `VYPOCET-03` 140× rozdíl prefaktorů jako *intrinsický*).

A varování `VYPOCET-03` tu hraje krásnou dvojroli. Faktor 140 mezi Sorkinem a EDT je intrinsický
— *není* odladitelný konvencí. V relačním jazyce: Sorkinova sonda na $\Lambda$ a EDT sonda na
$\Lambda$ jsou **dvě různé otázky**, ne dvě měření jedné. Že dávají různá čísla, není rozpor —
je to očekávané. **Rozpor by byl, kdyby dávaly stejné číslo bez společné struktury.** Relačnost
převrací logiku falzifikace: shoda různých sond je ta podezřelá věc, kterou je třeba vysvětlit
(jako exaktní $-18/11$ v Diracově sektoru `VYPOCET-02`!), zatímco rozdíl je default.

---

## 7. Co kdyby: jak by vypadala teorie, kde je sonda v základech

⟶ **EXTRAPOLACE** (syntéza všech čtyř výpočtů + crossed-product/QRF programu).

Dovolme si načrtnout, jak by taková teorie *vypadala* — ne rovnicemi, na to je tahle esej příliš
divoká, ale architekturou.

**Fundamentální data nejsou geometrie, ale schopnost odpovídat.** Vezmi causet: lokálně konečný
poset, řád + počet (`05-causal-sets.md`). Sám o sobě nemá dimenzi, nemá entropii, nemá metriku
v obvyklém smyslu. Má jen kauzální kostru. To je „respondent" před otázkou. Kostra je
fundamentální; geometrie emergentní jako *vzorec jeho odpovědí*.

**Sonda je matematický objekt v základech, ne přídavek.** V dnešní formulaci je $d_s$ definovaná
*po* zadání teorie volbou difúze. V relační teorii by **prostor sond** byl součástí kinematiky —
stejně fundamentální jako prostor stavů. Formálně: ke každému stavu (causetu, algebře) by
patřila *kategorie sond* (operátorů, QRF, propagátorů), a observable by byl funktor z téhle
kategorie do čísel. „Dimenze" by nebyla číslo $d_s$, ale **funktor $\text{sonda} \mapsto d_s$**.
Náš master-vzorec $d_s = D/\gamma$ je první řádek tohoto funktoru: explicitní vzorec, jak sonda
($\gamma$) určuje odpověď.

**Pozorovatel je crossed-product, ne homunkulus.** Entropie by se nepočítala „pro daný stav",
ale „pro daný stav *po* zkřížení s pozorovatelem". Type III → type II přechod (CLPW, Witten) by
byl *povinný krok definice*, ne technikálie. Naše $\varepsilon \sim \rho^{-1/2}$ (`VYPOCET-04`)
je kandidátní hodnota toho cutoffu pro causet.

**Konzistence napříč sondami nahrazuje univerzalitu.** Místo požadavku „existuje jedna pravá
hodnota" by teorie požadovala **konzistenční podmínky** mezi odpověďmi na různé sondy: IR limity
se musí shodnout (a shodují — vždy 4, `VYPOCET-01`); kde se dvě sondy *překrývají* v doméně, musí
dát kompatibilní čísla; transformace mezi QRF musí respektovat princip ekvivalence
(Giacomini–Brukner, `16-conceptual-problems.md` bod 6). To je gauge teorie sond.

A teď ta nejhezčí spekulace, kterou tahle architektura umožňuje:

⟶ **EXTRAPOLACE** (start: `connections.json` rozpor 657 vs 1777 vyřešen sondou).

Co kdyby **mnohé „rozpory mezi přístupy" ke kvantové gravitaci byly rozpory sond, ne rozpory
fyziky** — přesně jako edge 501 vs. 1539? `SYNTEZA.md` listuje sedm tvrdých konfliktů: diskrétní
vs. spojité UV, volume-law vs. area-law entropie, AS vs. swampland, emergentní vs. kvantovaná
geometrie… Co když část z nich zmizí, jakmile přiznáme, že každý tábor mlčky fixoval jinou sondu?

- **Volume-law vs. area-law** (`causal-sets→holography`, conflict): `VYPOCET-04` ukázal, že
  *tatáž* SSEE je volume-law (95,2) *bez* cutoffu a area-law (1,58) *s* cutoffem. Rozpor je o
  tom, zda jsi přidal pozorovatele — ne o fyzice causetu. **Sonda smiřuje konflikt.**
- **Spektrální dimenze: klesá vs. roste** (causal sets): už smířeno `VYPOCET-01`. **Sonda.**
- **Emergentní vs. kvantovaná geometrie** (`emergent-gravity→LQG`, conflict): co kdyby
  „kvantovaná" byla odpověď LQG-sondy (punktury, spektra plochy) a „emergentní" odpověď
  termodynamické sondy ($\delta Q = T\,dS$) na *tutéž* kostru? Komplementární otázky, ne
  protichůdné pravdy. ⟶ čistá spekulace, ale strukturně přesně typu 501-vs-1539.

Pokud tohle platí byť jen pro polovinu konfliktů, je relačnost geometrie **nejproduktivnější
smiřovací princip** v celé bázi: nepřekonává konflikty argumentem, ale ukazuje, že se hádaly
různé otázky o stejném respondentovi.

---

## 8. Co víme: kde to skřípe (poctivá inventura)

Fantazie musí přiznat svá slabá místa, jinak je propaganda.

1. **`VYPOCET-01` random-walk hodnota je ilustrativní.** Číslo 8 ($=D+4$) splňuje jen „$d_s > D$";
   přesná asymptotika není v literatuře (Eichhorn–Mizera nezveřejnili konstantu). Závěr „roste"
   je robustní, *velikost* růstu ne (`VYPOCET-01`, limit #1).

2. **`VYPOCET-04` je 2D, bezhmotný skalár.** Hypotéza je primárně o 4D (LQG area gap). 2D je
   sanity-check mechanismu, ne důkaz. Identifikace $\varepsilon$ s area gapem
   $\Delta = 4\sqrt3\,\pi\gamma\,l_P^2$ zůstává nadcházejícím krokem (`VYPOCET-04`, limit; závěr).

3. **Crossed-product entropie je observer-dependent — ale není svévolná.** Různé QRF dávají různé
   algebry, ale Page-křivku, area law a $S_{\text{gen}}$ to reprodukuje *konzistentně*
   (Kudler-Flam et al.). Relačnost ≠ libovůle; viz §5.

4. **Sen IR-univerzalita** (`hypotezy/H01-gamma-cardy.md`): log-korekce entropie ČD jsou určeny
   *jen* nízkoenergetickými daty, jsou přístupově-nezávislé. To je vážná námitka proti tomu, aby
   sonda fixovala UV parametr — některé observable jsou prostě IR a *žádná* UV sonda je nehne.
   Relačnost musí rozlišit IR-univerzální veličiny (kde rámec nehraje roli) od UV-relačních.

5. **„Princip relačnosti geometrie" je v této obecnosti náš konstrukt, ne věta.** Doložené jsou
   *jednotlivé* instance (dimenze, entropie). Skok k „každá geometrická veličina je relační" je
   extrapolace — značená, ale extrapolace.

---

## 9. Co by muselo být pravda

Tady fantazie skládá zbraně a předkládá falzifikovatelné jádro. Aby vize „geometrie jako síť
odpovědí na otázky (sonda, QRF)" nebyla básnička, musí platit tohle — a každý bod lze v principu
vyvrátit:

**F1 — Probe-dependence je generická, ne ojedinělá.**
*Tvrzení:* Najdou se *další* geometrické observable (mimo $d_s$), které dají kvalitativně
protichůdné odpovědi pro různé sondy na *téže* mikrostruktuře — analog 501-vs-1539.
*Falzifikace:* Pokud systematický sken sond (různé propagátory, různé QRF) na sprinklovaném
causetu ukáže, že *všechny* rozumné sondy dají *tutéž* UV dimenzi a tutéž geometrii (až na
chybu), pak je `VYPOCET-01` izolovaná kuriozita lorentzovské nelokality, ne ontologie. Relačnost
padá.

**F2 — Entropie je nedefinovaná bez rámce, a cutoff škáluje univerzálně.**
*Tvrzení:* SSEE / type-III stopa je *vždy* divergentní (volume-law) bez volby, a konečnou
(area-law) ji dělá *jen* přidání pozorovatele/cutoffu; v 2D ten cutoff škáluje $\varepsilon \sim
\rho^{-1/2}$ (`VYPOCET-04`), ve 4D musí dát $\rho^{-3/4}$ (area-law ansatz $n_{\max}\sim
N^{3/4}$).
*Falzifikace:* (a) Pokud se najde regularizace dávající konečnou area-law entropii *bez* volby
pozorovatele/cutoffu — entropie je atribut, ne odpověď. (b) Pokud 4D výpočet dá exponent ≠ 3/4
mimo chybu, mechanismus „cutoff = $\rho^{-1/d}$" je špatně.

**F3 — Cutoff causetu = modulární cutoff = area gap (jedna škála, tři jména).**
*Tvrzení:* $\varepsilon$ z `VYPOCET-04`, modulární cutoff crossed-productu (type III→II) a LQG
area gap $\Delta = 4\sqrt3\,\pi\gamma\,l_P^2$ jsou *tatáž* škála; Barbero–Immirzi $\gamma$ je
renormalizační konstanta vázající causet/type-II stopu na Bekenstein–Hawking
(`entropy-cluster.md`).
*Falzifikace:* Spočítat typ von Neumannovy algebry implikovaný každým ze tří počítání. Pokud
*nejsou* všechny type II$_\infty$ se stejnou stopou (`SYNTEZA.md`, H4), nejsou ekvivalentní a
trojcestná identifikace padá. Konkrétní first step už zná `H04`-styl výpočet.

**F4 — Konzistence napříč sondami nahrazuje univerzalitu, ale IR je pevný bod.**
*Tvrzení:* Všechny legitimní sondy se v IR shodnou na $d_s = 4$ (`VYPOCET-01`); rozdíly žijí jen
v UV; a tam, kde se dvě sondy doménově překrývají, dají kompatibilní čísla.
*Falzifikace:* Pokud se najde sonda dávající IR $d_s \neq 4$ na manifold-like causetu, není to
relačnost — je to nekonzistence, a respondent (causet) prostě není dobrý model 4D prostoročasu.
Relačnost *vyžaduje* pevný IR bod; jeho ztráta ji boří.

**F5 — Část mezipřístupových konfliktů jsou konflikty sond, ne fyziky.**
*Tvrzení:* Alespoň jeden „conflict" z `SYNTEZA.md` (kandidát: volume-vs-area entropie) se rozpustí,
jakmile se oběma táborům přiřadí jejich mlčky fixovaná sonda — přesně jako edge 501 vs. 1539.
*Falzifikace:* Pokud po explicitním vyznačení sond konflikt *přetrvá* (tábory dají nekompatibilní
odpovědi na *tutéž* otázku se *stejnou* sondou), jde o pravý fyzikální rozpor a relačnost ho
nesmiřuje. (Pozn.: `VYPOCET-03` ukazuje, že některé neshody — $\Lambda$-prefaktory 140× — jsou
intrinsické; ty relačnost *nesmiřuje* a netvrdí to.)

**F6 — Rozliš UV-relační od IR-univerzálních veličin.**
*Tvrzení:* Existuje ostrá dělicí čára: veličiny určené *jen* IR daty (Senovy log-korekce entropie,
`H01`) jsou rámcově-invariantní — žádná sonda jimi nehne; veličiny s UV obsahem (UV $d_s$,
SSEE cutoff) jsou relační.
*Falzifikace:* Pokud se ukáže, že i Sen-typ IR-univerzální veličina *závisí* na sondě/QRF, pak
relačnost přetekla i tam, kde být nemá, a je to známka, že princip je formulovaný příliš hrubě
(nebo naopak že IR-univerzalita je iluze). Obojí je informativní porážka.

---

### Epilog: respondent, ne kámen

Začali jsme obviněním, že se prostoročasu ptáme špatně — jako kamene na váhu. Čtyři výpočty nám
ukázaly causet, který na otázku po vlastní dimenzi odpoví dvakrát a opačně (`VYPOCET-01`), a
oblast, jejíž entropie neexistuje, dokud nezvolíš nůž (`VYPOCET-04`); a crossed-product program
nám pošeptal, že i pozorovatel, který tu otázku klade, je součástí odpovědi, ne vně ní
(arXiv:2412.15502).

Odbržděný závěr téhle eseje je, že prostoročas **není kámen, je to respondent**. Nemá vlastnosti,
má odpovědi. „Dimenze vesmíru" je gramatický přelud — jako kdybys chtěl jedno číslo pro „barvu,
kterou věc má", a zapomněl, že barva je odpovědí na otázku položenou světlem určité vlnové délky.
Změň světlo, změníš barvu; změň sondu, změníš dimenzi; změň pozorovatele, změníš entropii. A
přesto to není chaos — IR je pevný bod, Diracův sektor je exaktní, prefaktory jsou intrinsické.
Strukturovaná relačnost, ne libovůle.

Možná že hledání „teorie všeho" je proto špatně pojmenované. Nehledáme teorii všeho. Hledáme
**úplný slovník otázek** — všechny legitimní sondy, všechny referenční rámce — a důkaz, že na
každou z nich má vesmír konzistentní odpověď. „Všechno" není seznam atributů. Je to úplnost
dialogu.

A poslední odbržděná věta, kterou si dovolím: jestli je tahle vize pravdivá, pak vesmír nikdy
nebyl „tam venku" jako hotová věc, na kterou se díváme. Vesmír je **rozhovor**, který vedeme tím,
že do něj strkáme sondy — a geometrie je tvar, který ten rozhovor pokaždé na okamžik nabere.
Otázka „kolik má vesmír dimenzí" je tedy konečně zodpovězena: *kolik chceš. Řekni, čím se ptáš.*

---

*Anchory: `vypocty/VYPOCET-01-ds-klasifikace.md`, `…-02-a4-matching.md`,
`…-03-lambda-prefaktory.md`, `…-04-ssee-diamant.md`; `verification/ds-contradiction.md`,
`verification/novelty/entropy-cluster.md`; `foundations/16-conceptual-problems.md`,
`cross-cutting/13-entanglement-spacetime.md`, `approaches/05-causal-sets.md`; `SYNTEZA.md`.
Klíčové externí citace: Eichhorn–Mizera 1311.2530, Belenchia et al. 1507.00330, Sorkin–Yazdi
1611.10281, Sorkin et al. 1712.04227, CLPW 2206.10780, Witten 2112.12828, Kudler-Flam et al.
2309.15897, De Vuyst et al. 2412.15502, Van Raamsdonk 1005.3035, Faulkner et al. 2014.*
