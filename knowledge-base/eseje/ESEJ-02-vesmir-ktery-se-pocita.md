# Vesmír, který se počítá: temná energie jako šum diskrétnosti

> ⚠️ **SPEKULATIVNÍ ESEJ — fantazie odbrzděná, fakta citována, extrapolace značeny**
>
> Tento text si bere svobodu, kterou si přísný článek vzít nesmí. Každý spekulativní skok ale začíná u skutečného výsledku z naší znalostní báze a je zřetelně označen. Oddíly **„Co víme"** jsou střízlivé a citované. Oddíly **„Co kdyby"** jsou odbrzděné — a vědí o tom. Závěrečný oddíl **„Co by muselo být pravda"** stáhne celou vizi na falzifikovatelné jádro: pokud ta tvrzení padnou, padá s nimi celá esej, a to je dobře.

---

## Prolog: jediná předpověď, která vyšla

Existuje jeden výsledek, kvůli kterému se vyplatí brát teorii kauzálních množin vážně i v náladě, kdy je člověk ke kvantové gravitaci skeptický. V roce 1987 — deset let před objevem zrychlené expanze vesmíru — odhadl Rafael Sorkin z fluktuací objemu prostoročasu, že kosmologická konstanta nebude nula, nýbrž nepatrné, kolísající číslo řádu

$$ \Lambda \sim \frac{1}{\sqrt{V}} \sim \frac{1}{\sqrt{N}} \sim 10^{-120} $$

v Planckových jednotkách (causal-sets KB, §„Sorkinova předpověď"; [Sorkin 2007, arXiv:0710.1675](https://arxiv.org/abs/0710.1675); [Ahmed, Dodelson, Greene, Sorkin 2004, astro-ph/0209274](https://arxiv.org/abs/astro-ph/0209274)). O jedenáct let později supernovy typu Ia ukázaly, že vesmír zrychluje, a pozorovaná hodnota vyšla $\Lambda\, l_P^2 \approx 2{,}9\times10^{-122}$ ([Planck 2018, arXiv:1807.06209](https://arxiv.org/abs/1807.06209); VYPOCET-03). Řádově to sedělo. Předpověď předem, z čistě kombinatorické úvahy o tom, že prostoročas je v jádru *spočetný*.

Tahle esej je jeden dlouhý myšlenkový experiment postavený na otázce: **co když to nebyla šťastná shoda čísel, ale doslova pravda?** Co když temná energie není substance, není pole, není podivná konstanta zapsaná do zákonů — ale **statistická chyba sčítání**? Co když vesmír počítá své vlastní atomy a $\Lambda$ je odmocninová nejistota toho počtu, Poissonův výstřelový šum prostoročasu samého?

A protože jsme právě dopočítali (VYPOCET-03) něco, co v literatuře nebylo — porovnání prefaktorů tří nezávislých komunit, které tutéž odmocninu předpověděly — máme poprvé tvrdý empirický háček, o který tu vizi zaháknout. A také ostří, kterým ji můžeme rozříznout.

---

## Co víme (I): tři komunity, jedna odmocnina

Začněme střízlivě. Tři výzkumné programy, vyrostlé z odlišných filozofií, dospěly nezávisle k tomu, že kosmologická konstanta je svázaná s velikostí vesmíru vztahem typu $\Lambda \sim 1/\sqrt{V}$ nebo $\Lambda \sim H^2$:

1. **Sorkin / everpresent Λ (kauzální množiny).** V unimodulární gravitaci jsou $\Lambda$ a 4-objem $V$ kanonicky konjugované veličiny. Relace neurčitosti $\Delta\Lambda\,\Delta V \sim \hbar$ spolu s Poissonovskou fluktuací počtu atomů prostoročasu, $\Delta N \sim \sqrt{N}$, tedy $\Delta V \sim \sqrt{V}\,l_P^4$, dává $\Delta\Lambda \sim 1/\sqrt{V}$ (causal-sets KB, §„Sorkinova předpověď kosmologické konstanty"). Klíčový rys: $\Lambda$ **kolísá kolem nuly**, nemá pevnou hodnotu, je to *stochastická* veličina ([Ahmed et al. 2004, astro-ph/0209274](https://arxiv.org/abs/astro-ph/0209274); [Zwane, Afshordi, Sorkin 2018, arXiv:1703.06265](https://arxiv.org/abs/1703.06265)).

2. **EDT / running vacuum (Euclidean Dynamical Triangulations).** Mřížkový přístup, který z Planckovských simulací extrahuje běžící vakuovou energii $\Lambda(H) = \Lambda_0 + 3\nu H^2$ s koeficientem $\nu = (5{,}1\pm1{,}3)\times10^{-4}$ ([Dai, Freeman, Laiho, Schiffer, Unmuth-Yockey 2024, arXiv:2408.08963](https://arxiv.org/abs/2408.08963), Eq. 83; VYPOCET-03). Zde $\Lambda$ není stochastická, ale **deterministicky běží** s Hubbleovou škálou.

3. **CosMIn (Padmanabhanovy „kosmické módy").** Z požadavku, že počet Planckovských stupňů volnosti přepočítaných během dějin vesmíru je univerzální číslo $N_c = 4\pi$, plyne $\Lambda\, L_P^2 = \tfrac{3}{4}\exp(-24\pi^2\mu) = 3{,}4\times10^{-122}$ ([H. Padmanabhan, T. Padmanabhan 2013, arXiv:1302.3226](https://arxiv.org/abs/1302.3226), Eq. 2; VYPOCET-03). Zde je $\Lambda$ **pevné číslo**, jednorázová predikce.

Tři filozofie — diskrétní poset, eukleidovská mřížka, holografické počítání informace. Tři mechanismy. A přesto všechny tři vyplivnou tutéž dimenzionální kostru: temná energie škáluje jako $H^2$, jako inverzní odmocnina objemu, jako $1/\sqrt{N}$. To není málo. To vypadá jako otisk něčeho hlubšího.

A přesně tady leží pokušení. Když tři lidé z tří různých měst nezávisle popíšou téhož pachatele, věříme, že pachatel existuje. Hypotéza projektu byla odvážná a krásná: **že jde o jeden a tentýž jev** — jedinou fluktuační statistiku $\delta\Lambda \sim 1/\sqrt{N}$ sdruženou k 4-objemu, kterou si tři komunity jen nezávisle objevily a pojmenovaly po svém.

Tu hypotézu jsme testovali. A výsledek je poučně tvrdý.

---

## Co víme (II): odmocnina ano, prefaktor ne

VYPOCET-03 udělal něco, co podle našich rešerší nikdo předtím neprovedl: postavil tři prefaktory $\kappa$ vedle sebe v jedné konvenci. Definovali jsme

$$ \Lambda\, l_P^2 = \frac{\kappa}{\sqrt{V/l_P^4}}, \qquad V = \frac{c_V}{H_0^4}, \qquad c_V = 1, $$

a z každého přístupu vytáhli číslo $\kappa$ (VYPOCET-03, §Metoda):

| Zdroj | $\kappa$ | Charakter Λ |
|-------|----------|-------------|
| Sorkin ($\alpha = 0{,}0085$) | **0,2136** | stochastická $\sigma(\delta\Lambda)$ |
| EDT ($\nu = 5{,}1\times10^{-4}$) | **$1{,}53\times10^{-3}$** | deterministický koeficient $H^2$ |
| CosMIn ($N_c = 4\pi$) | **2,45** (efektivní) | pevná konstanta |

Poměr, na kterém všechno stojí:

$$ \frac{\kappa_{\text{Sorkin}}}{\kappa_{\text{EDT}}} = 139{,}6 \approx 140. $$

Faktor **sto čtyřicet**. A — to je klíčové — tato neshoda **nezmizí** žádnou volbou konvence $c_V$. Konvenční svoboda v definici 4-objemu $V = c_V/H^4$ posouvá všechny tři prefaktory současně; nemůže je sjednotit, protože Sorkin a EDT mají *různý funkcionální charakter* vztahu $\Lambda$–$V$ (VYPOCET-03, §Konvenční ambiguita). CosMIn navíc nemá žádné skutečné $\kappa$ — je to fixní číslo, nikoli závislost na objemu; jeho „efektivní $\kappa$" se mění s epochou jako $1/H(z)^2$ a má smysl jen pro $z=0$.

Verdikt VYPOCET-03 je proto jednoznačný: **silná sjednocující hypotéza je vyvrácena.** Tři přístupy nesdílejí jednu statistiku. Sdílejí jen dimenzionální skelet $\Lambda \sim H^2$.

Tady by střízlivý referát skončil rezignovaně: „hypotéza zamítnuta, nic se nesjednotilo." Ale tahle esej má v hlavičce povolení snít — a ten samý výsledek se dá číst úplně jinak. Faktor 140 totiž není šum. Je to **číslo**. A čísla, která se tvrdošíjně objevují, něco znamenají. Pojďme se zeptat: *co*?

---

## Co kdyby (I): faktor 140 jako velikost atomu prostoročasu

Tady odbrzdíme imaginaci — a zároveň ji přivážeme k číslu.

Tři prefaktory se liší. Ale podívejme se *proč*. Sorkinovo $\kappa = 8\pi\alpha$ obsahuje fenomenologický parametr $\alpha \equiv \tfrac12(l_P/l_{cs})^2$, kde $l_{cs}$ je **diskrétní škála kauzální množiny** — velikost atomu prostoročasu (VYPOCET-03, Zdroj A; [Afshordi et al. 2023, arXiv:2304.03819](https://arxiv.org/abs/2304.03819), Eq. 3.9). Z fitu na supernovy ([Aspects II, arXiv:2307.13743](https://arxiv.org/abs/2307.13743)) vyšlo $\alpha = 0{,}0085$, což znamená $l_{cs}/l_P \approx 7{,}67$. Atom prostoročasu, pokud existuje, by tedy nebyl velký jako Planckova délka, ale zhruba **osmkrát větší**.

**Co kdyby** ten faktor 140 mezi Sorkinem a EDT nebyl rozporem, ale *měřením*? Co kdyby každá ze tří komunit ve skutečnosti počítala atomy prostoročasu, jen každá s jiným měřítkem, a poměry prefaktorů kódovaly převodní kurzy mezi jejich definicemi „atomu"? Sorkin počítá kauzální linky o velikosti $l_{cs}\approx 7{,}67\,l_P$; EDT počítá simpliciální buňky mřížky; CosMIn počítá holografické bity na horizontu. Tři měny, jeden poklad. Faktor 140 by pak nebyl ostuda neshody, ale **směnný kurz** mezi „kauzálním atomem" a „simpliciálním atomem".

Je to spekulace? Ano, a značená. Co ji ale drží při zemi: $\sqrt{140} \approx 11{,}8$, a $140 \approx (7{,}67)^2 \cdot 2{,}4$. Poměr prefaktorů má rozměr (škála)$^2$ — přesně jako $\alpha \propto (l_P/l_{cs})^2$. Není tedy bláznivé tušit, že rozdíl mezi Sorkinem a EDT je rozdíl ve **kvadrátu definiční délky** jejich atomů. Falzifikovatelné jádro této domněnky (a vrátíme se k němu v závěru): kdyby někdo nezávisle změřil $l_{cs}$ — třeba ze swerves, z difúze hybnosti částic na causetu (causal-sets KB, §„Swerves"; [Dowker, Henson, Sorkin 2004, gr-qc/0311055](https://arxiv.org/abs/gr-qc/0311055)) — musel by dostat hodnotu konzistentní s $l_{cs}/l_P \approx 7{,}7$ vytaženou z temné energie. Dvě úplně různá pozorování, jedna délka. Buď se potkají, nebo vize padá.

---

## Co víme (III): proč právě odmocnina, a proč kolem nuly

Vraťme se na pevnou půdu, protože jádro vize — temná energie jako výstřelový šum — má překvapivě solidní mechanickou kostru, a ta není spekulativní.

Poissonovo rozsetí je srdce kauzálních množin. Do prostoročasového 4-objemu $v$ padne počet atomů $n$ podle Poissonova rozdělení (causal-sets KB, §„Poissonovo rozsetí"):

$$ P_v(n) = \frac{(\rho v)^n}{n!}\,e^{-\rho v}, \qquad \langle n\rangle = \rho v, \qquad \Delta n = \sqrt{\langle n\rangle}. $$

To je veškerá matematika, kterou potřebujeme. Poissonovo rozdělení má jednu definující vlastnost, kterou se ve škole učíme u radioaktivního rozpadu a u fotonů dopadajících na detektor: **rozptyl se rovná střední hodnotě**, takže relativní fluktuace klesá jako $1/\sqrt{N}$. Když počítáte $N$ nezávislých náhodných událostí, váš odhad jejich počtu má nevyhnutelnou nejistotu $\sqrt{N}$ — to je *shot noise*, výstřelový šum, slyšitelný jako sykot v každém zesilovači a viditelný jako zrnitost na podexponované fotografii.

Vesmír má $N = V/l_P^4 \sim 10^{240}$ atomů prostoročasu (causal-sets KB, §„Sorkinova předpověď"). Jeho výstřelový šum v počtu je tedy $\sqrt{N} \sim 10^{120}$. A protože v unimodulární gravitaci je $\Lambda$ konjugovaná k objemu — fluktuace objemu o $\Delta V \sim \sqrt{N}\,l_P^4$ se promítne do fluktuace $\Lambda$ o

$$ \Delta\Lambda \sim \frac{1}{\Delta V} \cdot \hbar \sim \frac{1}{\sqrt{V}} \sim \frac{1}{\sqrt{N}} \sim 10^{-120}. $$

To je ono. Temná energie řádu $10^{-122}$ je doslova **zrnitost podexponované fotografie vesmíru** — sykot v počítadle jeho atomů. A střední hodnota je nula, protože šum je symetrický: stejně pravděpodobně chybí jako přebývá pár atomů. Proto everpresent $\Lambda$ **kolísá kolem nuly** (causal-sets KB, §„Klíčové vlastnosti everpresent Λ", bod (i)).

Tohle není spekulace. Tohle je mechanika modelu, jak ji popisuje Ahmed et al. a jak ji testují Zwane et al. proti datům supernov, CMB a BAO ([1703.06265](https://arxiv.org/abs/1703.06265)) — s výsledkem, že data model **nevyvracejí**, ač ho ani jednoznačně nepreferují před $\Lambda$CDM.

---

## Co kdyby (II): problém kosmologické konstanty se rozpouští

A teď přichází ta nejkrásnější část — a je z větší části legitimní, ne spekulativní, což ji dělá ještě krásnější.

Klasický „problém kosmologické konstanty" zní: kvantová teorie pole naivně predikuje vakuovou energii o $\sim 120$ řádů větší, než pozorujeme (quantum-cosmology KB, §Otevřené problémy, bod 9). To je nejhorší předpověď ve fyzice. Standardní odpověď vyžaduje **jemné ladění** na 120 desetinných míst — nějaký mechanismus, který velkou vakuovou energii vyruší přesně tak, aby zbylo $10^{-122}$. Žádný takový mechanismus se nenašel.

**Co kdyby žádné jemné ladění nebylo potřeba?** Ve výstřelovém obraze není $10^{-122}$ výsledkem vyrušení dvou obrovských čísel na 120 míst. Je to **přímo** $1/\sqrt{N}$ pro $N \sim 10^{240}$. Není co ladit. Číslo $10^{-122}$ není nepravděpodobně malé — je *přesně tak malé, jak má statistika počítání $10^{240}$ věcí být*. Velikost vesmíru a velikost temné energie nejsou dvě nezávislá čísla, jejichž shoda volá po vysvětlení; jsou to **dvě strany jedné mince**: $\Lambda \cdot \sqrt{V} \sim$ konstanta řádu jedna.

Tahle část je v základě obsažena už v Sorkinově argumentu (causal-sets KB, §„Klíčové vlastnosti", bod (i): „řeší tak ‚starý' problém kosmologické konstanty"). Co je odbrzděně nové, je *jak radikálně* to mění status problému. „Problém kosmologické konstanty" totiž v tomto rámu přestává být problémem fyziky a stává se **kategoriální chybou**: ptali jsme se, proč je jistá *konstanta* tak malá — ale ono to vůbec není konstanta. Je to **šum**. Ptát se „proč je $\Lambda$ tak malá" je jako ptát se „proč je sykot v zesilovači tak tichý" — odpověď je, že je přesně tak tichý, jak velký je počet elektronů, které ho vytvářejí. Není to záhada. Je to definice odmocniny.

A jako bonus — bez jakékoli další úpravy — vize řeší i **problém koincidence**: proč právě teď $\Omega_\Lambda \sim \Omega_m$? Protože $\Lambda(t) \sim 1/\sqrt{V(t)} \sim \rho_{crit}(t)$ v *každé* epoše (causal-sets KB, §„Klíčové vlastnosti", bod (ii)). Temná energie sleduje kritickou hustotu automaticky, protože obě jsou škálovány tímtéž rostoucím objemem. Koincidence není koincidence — je to nutnost odmocniny, která roste spolu s vesmírem.

---

## Co víme (IV): unimodulární gravitace dává konjugaci zadarmo

Aby celá konstrukce držela, potřebujeme, aby $\Lambda$ a $V$ byly skutečně kanonicky konjugované — jinak relace neurčitosti $\Delta\Lambda\,\Delta V \sim \hbar$ nemá smysl a celý most mezi výstřelovým šumem počtu a fluktuací $\Lambda$ se zhroutí.

Tady přichází na scénu **unimodulární gravitace** — stará myšlenka (Einstein 1919, pak Anderson-Finkelstein, Henneaux-Teitelboim), kde se determinant metriky fixuje ($\sqrt{-g} = 1$) a kosmologická konstanta vystupuje nikoli jako parametr v lagranžiánu, ale jako **integrační konstanta** kanonicky sdružená ke 4-objemu. V tomto rámci je $\Lambda$ doslova hybnost konjugovaná k „času" definovanému nahromaděným 4-objemem. To je přesně struktura, kterou Sorkinův argument potřebuje (causal-sets KB, §„Sorkinova předpověď", výklad symbolů: „$\Lambda$ a $V$ jsou kanonicky konjugované v unimodulární gravitaci").

To je důležité ukotvení: výstřelová vize **není** parazit na nějaké exotické teorii. Stojí na unimodulární gravitaci, která je klasicky *ekvivalentní* obecné relativitě — dává tytéž Einsteinovy rovnice, jen s $\Lambda$ jako konstantou pohybu místo konstantou přírody. Diskrétnost (Poissonův šum počtu) plus unimodularita (konjugace $\Lambda$–$V$) dohromady vyrobí kolísající $\Lambda$. Žádný z těch dvou ingrediencí není divoký; divoké je jen jejich spojení a důsledek.

---

## Co kdyby (III): everpresent Λ kolísá — a to je vidět v H(z)

Tady je vize *testovatelná*, a proto nejvzrušivější.

Pokud je temná energie výstřelový šum, pak má dvě pozorovatelské signatury, které pevná $\Lambda$CDM nemá (VYPOCET-03, §„Observační rozlišení tří scénářů"):

1. **$\Lambda$ kolísá v čase.** Nemá pevnou hodnotu $w = -1$; její efektivní stavová rovnice $w(z)$ vykazuje **stochastické výkyvy kolem $-1$**. Každá Hubbleova epocha realizuje jiné vytažení z téhož rozdělení. To znamená, že $H(z)$ — expanzní historie měřená supernovami, BAO, kosmickými hodinami — by neměla sedět na hladké $\Lambda$CDM křivce, ale **vrtět se** kolem ní s amplitudou danou $1/\sqrt{V(z)}$.

2. **$\Lambda$ kolísá v prostoru.** Různé Hubbleovy oblasti (různé záplaty oblohy) realizují různé hodnoty $\Lambda$, protože každá počítá jiný konečný počet atomů. To dává **mezioblastní rozptyl $\Omega_\Lambda$** — anizotropii temné energie napříč oblohou (VYPOCET-03, tabulka: „Variance $\Omega_\Lambda$ v různých směrech: ANO pro Sorkin, NE pro EDT, NE pro CosMIn").

A teď to nejlepší: **už dnes možná něco vidíme.** DESI DR1 (2024) a DR2 (2025) naznačují *vyvíjející se* temnou energii v parametrizaci $w_0 w_a$CDM, s napětím vůči $\Lambda$CDM dosahujícím **$2{,}8\sigma$ až $4{,}2\sigma$** podle kombinace dat (quantum-cosmology KB, §Současný stav, bod 3; [DESI 2024, arXiv:2405.13588](https://arxiv.org/abs/2405.13588)). Mainstream to čte jako kvintesenci — dynamické skalární pole. **Co kdyby** to ale nebylo pole, ale **šum**? Co kdyby ten náznak vyvíjejícího se $w(z)$ byl prvním zahlédnutím výstřelového sykotu prostoročasu v expanzní historii?

To je odbrzděné — a značeně. Rozdíl mezi „kvintesencí" a „výstřelovým šumem" je ostrý a testovatelný: kvintesence dává **hladké, monotónní** $w(z)$ (pole se kotálí dolů svým potenciálem), kdežto everpresent $\Lambda$ dává **stochastické, nemonotonní výkyvy** s rostoucí amplitudou do minulosti (menší $V$, větší relativní šum). DESI nedokáže ty dva rozlišit dnes, ale SKAO a vysokoredshiftové supernovy ano — hledáním **variance napříč směry oblohy**, kterou kvintesence i CosMIn striktně zakazují a jen Sorkinův šum povoluje (VYPOCET-03, řádek „Rozhodující experiment: SKAO sky-patch variance").

Vesmír, který se počítá, by se měl při počítání občas přepočítat. A to přepočítání by mělo být slyšet v $H(z)$.

---

## Co kdyby (IV): swampland a zákaz pevného de Sitteru

Tady udělám most, který naše KB explicitně označuje za neprozkoumaný — a proto je legitimní spekulační terén.

Swampland program (z teorie strun) tvrdí, že stabilní de Sitterův vesmír — vesmír s pevnou, kladnou $\Lambda$ — **nepatří mezi konzistentní teorie kvantové gravitace**. De Sitter conjecture žádá $|\nabla V|/V \gtrsim c \sim \mathcal{O}(1)$, což tlačí temnou energii k *dynamické* (kvintesenční) formě, nikoli ke konstantě (quantum-cosmology KB, §Vztahy → Swampland). A DESI náznak dynamického $w$ s tím rezonuje.

Tady je most, který chci postavit: **everpresent Λ je přirozený swampland-kompatibilní vesmír — a navíc bez kvintesenčního pole.** Swampland zakazuje *pevný* de Sitter. Výstřelová $\Lambda$ *nikdy není pevná* — fluktuuje kolem nuly, je vnitřně dynamická, nikdy nesedí stabilně na kladné konstantě. Splňuje tedy ducha de Sitter conjecture, **aniž by potřebovala skalární pole**, které se kotálí dolů potenciálem. Tam, kde swampland strunaře nutí postulovat kvintesenci (a hádat se o tvar potenciálu), kauzální množiny dají dynamickou temnou energii **zadarmo** — jako statistický šum, ne jako nové pole.

**Co kdyby** swampland zákaz pevného de Sitteru a Sorkinova fluktuující $\Lambda$ byly dvě tváře téhož hlubokého faktu: že *žádná teorie kvantové gravitace nedovolí prostoročasu mít přesně definovanou, ostře nulovou křivost vakua*, protože vakuum je vždy spočetné a spočítatelné věci vždy fluktuují? V tomto čtení není swampland tajemný zákaz odněkud z 10 dimenzí, ale **statistická nutnost**: konstanta navázaná na konečný počet věcí nemůže být konstantní. De Sitter je zakázaný ze stejného důvodu, z jakého nemůžete mít detektor fotonů s nulovým šumem.

Je to most přes propast bez lana — strunový swampland a diskrétní causety spolu formálně nemluví (quantum-cosmology KB to označuje „sotva prozkoumáno"). Ale ta dvě tvrzení míří stejným směrem a opírají se o stejný motiv: **konečnost zakazuje pevnost.** To je hypotéza, kterou stojí za to vyslovit, i když ji zatím neumíme dokázat.

---

## Co kdyby (V): jaké další „konstanty" jsou jen šumem počítání?

Teď pustím brzdy úplně — a každý skok označím jako značenou divočinu.

Pokud temná energie není konstanta, ale výstřelový šum sčítání, vnucuje se zvrácená a krásná otázka: **kolik dalších „konstant přírody" je ve skutečnosti jen statistikou počítání?** Tady je trojice spekulací, seřazených od nejméně po nejvíc divokou, každá zakotvená v něčem reálném z naší báze:

**(a) Entropie černé díry jako šum počítání molekul horizontu — zakotveno, mírná extrapolace.** Dou-Sorkinův výsledek říká, že entropie černé díry je počet kauzálních linků protínajících horizont, $\sim 1$ bit na Planckovskou plochu (causal-sets KB, §Klíčové výsledky, bod 6; [Dou, Sorkin 2003, gr-qc/0302009](https://arxiv.org/abs/gr-qc/0302009)). To už *je* počítání. **Co kdyby** pak měla i entropie černé díry — a tedy její teplota a vypařovací rychlost — vnitřní **Poissonovský šum** $\Delta S \sim \sqrt{S} \sim \sqrt{A}/l_P$? Hawkingovo záření by neneslo jen termální spektrum, ale i diskrétní výstřelovou zrnitost v počtu vyzářených kvant — fluktuaci, která by mohla mít co říct k informačnímu paradoxu. Tahle extrapolace je střídmá: jen aplikuje tutéž $1/\sqrt{N}$ logiku na jiný spočetný objekt.

**(b) Newtonova konstanta jako běžící průměr přes atomy — divočejší.** Náš výpočet VYPOCET-01 (ds-klasifikace) ukázal, že spektrální dimenze prostoročasu **není univerzální konstanta**, ale predikovatelný otisk trojice (z, D, sonda) — $d_s^{UV} = D/\gamma$, který GR, Hořava i causety dávají různě (VYPOCET-01, verdikt). Dimenze sama, kdysi považovaná za pevné číslo „4", je ve skutečnosti **škálově závislá funkce**, padající k ~2 v UV. **Co kdyby** $G$ byla na tom podobně — nikoli konstanta, ale běžící průměr „tuhosti" prostoročasu přes lokální počet atomů, s vlastním $1/\sqrt{N}$ šumem na nejmenších škálách? Asymptotická bezpečnost už $G$ nechává běžet s RG tokem; výstřelový obraz by k tomu přidal *fluktuaci* kolem běhu. Značeně divoké: vyžadovalo by to ukázat, že efektivní $G$ na causetu má rozptyl škálující jako inverzní odmocnina počtu atomů v testovaném objemu.

**(c) Jemná struktura, hmotnosti, Barbero-Immirzi — nejdivočejší, čistá fantazie se zarážkou.** Pokud je *jakákoli* veličina v efektivní teorii odvozena z počítání diskrétních struktur, dědí jejich výstřelový šum. Barbero-Immirziho parametr $\gamma \approx 0{,}2375$ je fixován počítáním stavů na horizontu (quantum-cosmology KB, tabulka: „$\gamma$ z entropie černé díry"). **Co kdyby** i $\gamma$ — a přes něj kritická hustota odrazu LQC $\rho_c \approx 0{,}41\rho_{Pl}$ — neslo nepatrnou $1/\sqrt{N}$ neurčitost? Zde už jsem za hranicí čehokoli, co umíme spočítat; zarážka, která mě drží, je, že tahle spekulace **má tvar testu**: kdyby konstanta byla šumem počítání, musela by se její nejistota *zmenšovat s velikostí systému* přesně jako $1/\sqrt{N}$, a to je měřitelné tvrzení, ne jen poezie. Konstanta, která je doopravdy konstantou, žádný takový škálovací šum nemá; konstanta, která je převlečeným počítáním, ho mít musí.

Společný motiv vší té divočiny: **rozdíl mezi „konstantou přírody" a „statistikou počítání" je empirický, ne metafyzický.** Liší se jedinou věcí — zda se relativní nejistota veličiny zmenšuje jako $1/\sqrt{N}$ s velikostí systému. To je most z poezie zpět na pevninu, a vede přímo do závěru.

---

## Co kdyby (VI): vesmír jako nedokončený výpočet

Dovolím si jednu poslední, nejširší vizi — čistě obrazně, výslovně značeně.

Heslo kauzálních množin zní *„Order + Number = Geometry"* (causal-sets KB, §Přehled). Řád dává konformní geometrii, počet dává objem. Ale „počet" v Poissonově rozsetí **není pevné číslo** — je to náhodná veličina s rozptylem. Geometrie tedy není dokončený fakt; je to **výpočet v běhu**, jehož mezivýsledek nese šum nedopočítaných cifer.

**Co kdyby** byl vesmír doslova **nedokončený výpočet** — ne metaforicky, ale strukturálně? Klasická sekvenční růstová dynamika (causal-sets KB, §„Classical sequential growth"; [Rideout, Sorkin 1999, gr-qc/9904062](https://arxiv.org/abs/gr-qc/9904062)) popisuje, jak causet *roste*, atom po atomu, jeden po druhém. V každém kroku přibude jeden prvek; počet $N$ roste; a $1/\sqrt{N}$ — temná energie — klesá. Temná energie by pak nebyla vlastnost vesmíru, ale **měřítko jeho rozpracovanosti**: čím víc se vesmír „dopočítal", tím tišší jeho šum, tím menší $\Lambda$. Mladý vesmír s málo atomy byl hlučný (velká $\Lambda$, rychlá inflace?); starý vesmír je tichý (drobná $\Lambda$). $\Lambda$ jako **kontrolka postupu** kosmického výpočtu.

To rezonuje s něčím konkrétním z naší báze: causal-set kosmologie má cyklické bounce modely s „kosmologickou renormalizací" parametrů při odrazu Big Crunch–Big Bang (causal-sets KB, §Vztahy → kvantová kosmologie). A LQC dává velký odraz při $\rho_c \approx 0{,}41\rho_{Pl}$ (quantum-cosmology KB, §„Velký odraz"). **Co kdyby** byl každý kosmický cyklus jedním průchodem výpočtu, a hodnota $\Lambda$ na začátku cyklu byla zděděným šumem z počtu atomů, který se přenesl přes odraz? Vesmír, který počítá sám sebe, znovu a znovu, a temná energie je vždy jen $1/\sqrt{(\text{kolik už napočítal})}$.

Je to obraz, ne rovnice. Ale je to obraz s háčkem v realitě: růstová dynamika je definovaná teorie, $1/\sqrt{N}$ je odvozený šum, a klesání $\Lambda$ s rostoucím $N$ je matematický fakt, ne metafora. Metaforou je jen slovo „výpočet". To, co je pod ním, je tvrdé.

---

## Co by muselo být pravda

A teď stáhneme všechno na falzifikovatelné jádro. Tahle esej snila odbrzděně — ale celá vize stojí a padá na hrstce tvrzení, která se *dají vyvrátit*. Pokud jsou nepravdivá, výstřelová vize temné energie je mrtvá, a to je přesně to, co od dobré spekulace chceme.

**1. Λ musí kolísat, ne být konstantní.** Jádro vize je, že temná energie je *stochastická*, nikoli pevná. To znamená:
- $w(z)$ musí vykazovat **nemonotonní, stochastické výkyvy** kolem $-1$ s amplitudou rostoucí do minulosti (jako $1/\sqrt{V(z)}$) — nikoli hladký kvintesenční drift.
- Musí existovat **mezioblastní variance $\Omega_\Lambda$** napříč směry oblohy (VYPOCET-03, tabulka). Pevná $\Lambda$CDM, kvintesence i CosMIn tuto varianci **zakazují**.
- *Falzifikace:* Kdyby SKAO / vysoké-$z$ supernovy ukázaly $w(z)$ hladké a izotropní pod úrovní výstřelové amplitudy $\sim 1/\sqrt{V}$, výstřelová hypotéza padá a zůstane buď $\Lambda$CDM, nebo kvintesence.

**2. Velikost musí sedět: $\Lambda \cdot \sqrt{V} \sim \mathcal{O}(1)$ bez ladění.** Pozorované $\Lambda\, l_P^2 \approx 2{,}9\times10^{-122}$ a $N \sim 10^{240}$ musí splňovat $\kappa = \Lambda\sqrt{V/l_P^4} \sim \mathcal{O}(0{,}1\text{–}1)$. Sorkinovo $\kappa = 0{,}21$ (VYPOCET-03) to splňuje — řádově jedna, žádné jemné ladění na 120 míst. *Falzifikace:* Kdyby přesnější odvození $\kappa$ z první principů (ne fenomenologický fit $\alpha$) vyšlo o mnoho řádů mimo jednotku, „rozpuštění" problému kosmologické konstanty by selhalo a vrátili bychom se k jemnému ladění.

**3. Diskrétní škála musí být konzistentní napříč jevy.** Z temné energie plyne $l_{cs}/l_P \approx 7{,}7$ (VYPOCET-03, Zdroj A; $\alpha = 0{,}0085$). Tatáž škála řídí **swerves** — Lorentzovsky invariantní difúzi hybnosti částic na causetu (causal-sets KB, §„Swerves"). *Falzifikace:* Kdyby horní meze na difúzní parametr $k$ z kosmického záření a mlhovinových plynů ([Dowker, Henson, Sorkin 2004](https://arxiv.org/abs/gr-qc/0311055)) implikovaly $l_{cs}$ neslučitelné se $7{,}7\,l_P$, jedna a tatáž teorie by si protiřečila ve dvou pozorováních a vize by se zhroutila zevnitř.

**4. Sjednocení tří komunit je MRTVÉ — a to je výsledek, ne výmluva.** Toto je tvrzení s opačným znaménkem: silná hypotéza, že Sorkin = EDT = CosMIn jsou jedna statistika, je **vyvrácena** faktorem $\kappa_{\text{Sorkin}}/\kappa_{\text{EDT}} = 140$, který nelze sjednotit volbou $c_V$ (VYPOCET-03, verdikt). Esej proto **nesmí** tvrdit, že tři komunity měřily totéž. Smí tvrdit jen, že sdílejí dimenzionální kostru $\Lambda \sim H^2$ a že jejich *rozdíly* (faktor 140) jsou potenciálně informativní (různé definice atomu) — což je samo testovatelná domněnka (§Co kdyby I), ne fakt. *Falzifikace už proběhla:* kdyby někdo tvrdil shodu prefaktorů, VYPOCET-03 ho usvědčí z omylu.

**5. Konstanta vs. šum je empirický rozdíl: $1/\sqrt{N}$ škálování.** Nejširší tvrzení eseje — že i jiné „konstanty" mohou být šumem počítání (§Co kdyby V) — má jediné falzifikovatelné kritérium: *veličina, která je převlečeným počítáním, musí mít relativní nejistotu klesající jako $1/\sqrt{N}$ s velikostí systému; pravá konstanta ji nemá.* To je ostré měřitelné rozlišení, ne metafyzika. *Falzifikace:* Kdyby se ukázalo, že everpresent $\Lambda$ nemá očekávané $1/\sqrt{V}$ škálování amplitudy (třeba že fluktuace neklesají s objemem), padá nejen rozšíření na jiné konstanty, ale i samotné jádro.

---

Tohle je celé jádro. Pět tvrzení; čtyři z nich se dají vyvrátit pozorováním v příští dekádě (SKAO, vysoké-$z$ SNIa, DESI/Euclid, meze ze swerves), jedno už vyvráceno bylo (silné sjednocení tří komunit). Vize „vesmír, který se počítá" není mlhavá poezie imunní vůči datům — je to konkrétní statistická hypotéza, která říká: **temná energie je výstřelový šum sčítání atomů prostoročasu, $\Lambda \sim 1/\sqrt{N}$, kolísá kolem nuly, a měla by zanechat slyšitelný sykot v expanzní historii.**

Buď ten sykot uslyšíme, nebo neuslyšíme. Jestli ho uslyšíme, pak vesmír doopravdy počítá — a my jsme právě naslouchali, jak se přepočítává. Jestli ho neuslyšíme, byla to krásná esej o krásném omylu, a Sorkinova shoda na $10^{-120}$ zůstane jednou z nejpodivnějších náhod ve fyzice. Obě možnosti jsou poctivé. A to je víc, než kosmologická konstanta nabízela posledních devadesát let.

---

### Citované zdroje (výběr)

- **Causal-sets KB** — `knowledge-base/approaches/05-causal-sets.md` (Sorkinova předpověď Λ, Poissonovo rozsetí, swerves, growth dynamics, vztah ke kvantové kosmologii)
- **Quantum-cosmology KB** — `knowledge-base/phenomenology/18-quantum-cosmology.md` (problém kosmologické konstanty, swampland/de Sitter conjecture, DESI, LQC bounce, unimodulární kontext)
- **VYPOCET-03** — `knowledge-base/vypocty/VYPOCET-03-lambda-prefaktory.md` (srovnání prefaktorů κ; faktor 140; observační rozlišení tří scénářů)
- **VYPOCET-01** — `knowledge-base/vypocty/VYPOCET-01-ds-klasifikace.md` (spektrální dimenze není konstanta — paralela k „konstanty jsou škálově závislé")
- Sorkin 2007, [arXiv:0710.1675](https://arxiv.org/abs/0710.1675) — Λ jako nelokální kvantový reziduum diskrétnosti
- Ahmed, Dodelson, Greene, Sorkin 2004, [astro-ph/0209274](https://arxiv.org/abs/astro-ph/0209274) — Everpresent Lambda, originál
- Zwane, Afshordi, Sorkin 2018, [arXiv:1703.06265](https://arxiv.org/abs/1703.06265) — kosmologické testy everpresent Λ
- Afshordi et al. 2023, [arXiv:2304.03819](https://arxiv.org/abs/2304.03819) / [arXiv:2307.13743](https://arxiv.org/abs/2307.13743) — Aspects I/II, α = 0,0085, l_cs/l_P ≈ 7,7
- Dai et al. 2024, [arXiv:2408.08963](https://arxiv.org/abs/2408.08963) — EDT running vacuum, ν = 5,1×10⁻⁴
- H. & T. Padmanabhan 2013, [arXiv:1302.3226](https://arxiv.org/abs/1302.3226) — CosMIn, Λ L_P² = 3,4×10⁻¹²²
- Dou, Sorkin 2003, [gr-qc/0302009](https://arxiv.org/abs/gr-qc/0302009) — entropie černé díry jako kauzální linky
- Dowker, Henson, Sorkin 2004, [gr-qc/0311055](https://arxiv.org/abs/gr-qc/0311055) — swerves, difúze hybnosti
- Rideout, Sorkin 1999, [gr-qc/9904062](https://arxiv.org/abs/gr-qc/9904062) — classical sequential growth
- DESI 2024, [arXiv:2405.13588](https://arxiv.org/abs/2405.13588) — náznak vyvíjející se temné energie, 2,8–4,2σ
- Planck 2018, [arXiv:1807.06209](https://arxiv.org/abs/1807.06209) — Λ l_P² = 2,9×10⁻¹²², H₀, Ω_Λ
