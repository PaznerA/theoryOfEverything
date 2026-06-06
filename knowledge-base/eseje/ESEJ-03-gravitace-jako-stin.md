# Gravitace jako stín fermionů

> ⚠️ SPEKULATIVNÍ ESEJ — fantazie odbrzděná, fakta citována, extrapolace značeny

---

Začněme u jednoho čísla, protože celá tahle esej visí na jediném čísle a já chci,
abyste ho měli před očima, než se rozletíme tam, kam se rozletět nemáme:

$$-\frac{18}{11}.$$

Není to konstanta jemné struktury. Není to hmotnostní poměr. Není to nic, co byste
našli v tabulkách na zadní straně učebnice. Je to poměr dvou koeficientů — koeficientu
u Weylova kvadrátu a koeficientu u Eulerovy hustoty — v rozvoji jistého funkcionálu,
který, jak uvidíme, popisuje gravitaci. A to číslo má jednu vlastnost, kvůli které
sedím v noci a dívám se na strop: **platí přesně pro fermiony a pro nic jiného.**

Tahle esej je o tom, co kdyby to nebyla náhoda. Co kdyby to číslo nebylo kuriozita,
ale doznání. Co kdyby gravitace nebyla síla.

Budu poctivý v jednom směru a nepoctivý v druhém. Poctivý budu k faktům: všechno, co
je v sekcích **„Co víme"**, je spočítané, citované a reprodukovatelné — vychází to
z výpočtů VYPOCET-02 a VYPOCET-11 a z draftu-02 tohoto projektu, opřených o Duffa,
Vassiliče, Gilkeyho, Chamseddina-Connese a Atiyaha-Singera. Nepoctivý — odbrzděný —
budu v sekcích **„Co kdyby"**, kde si dovolím extrapolovat za hranici toho, co kdokoli
dokázal, a kde každý takový skok zřetelně označím. Na konci, v sekci **„Co by muselo
být pravda"**, fantazii zase přibrzdím a vytáhnu z ní falzifikovatelné jádro — to, co
by musel svět splňovat, kdyby tahle bláznivá vidina měla mít kus pravdy.

Tak. Nadechněte se. Jdeme.

---

## Co víme: dvě cesty, jedno číslo

Existují dva výpočty, dvě naprosto nezávislé tradice fyziky, které se nikdy neměly
potkat, a přesto vrátí totéž racionální číslo.

**Cesta první — spektrální akce.** V nekomutativní geometrii Alaina Connese je veškerá
geometrie zakódovaná do spektrálního trojčlenu $(\mathcal{A}, \mathcal{H}, D)$ — algebry,
Hilbertova prostoru a Diracova operátoru $D$. Fyziku generuje jediný funkcionál,
spektrální akce $\mathrm{Tr}\, f(D/\Lambda)$, který závisí *pouze na spektru* Diracova
operátoru. Když ho rozvinete pomocí heat-kernelu, vypadne z něj — z ničeho, jen z $D$ —
kosmologická konstanta, Einsteinův-Hilbertův člen $R$, a kvadratické členy zakřivení.
A v tom $a_4$ členu (Chamseddine-Connes, hep-th/9606001, rov. 2.24; přepis CCM
hep-th/0610241) má koeficient u Weylova kvadrátu hodnotu

$$\alpha_0 = -\frac{3 f_0}{10\pi^2}, \qquad \tau_0 = \frac{11 f_0}{60\pi^2},$$

kde $f_0 = f(0)$ je hodnota cutoff-funkce v nule. A jejich poměr — nezávislý na $f_0$,
nezávislý na konvenci — je

$$\frac{\alpha_0}{\tau_0} = -\frac{18}{11}.$$

**Cesta druhá — konformní anomálie stopy.** Úplně jiný svět: kvantová teorie pole na
zakřiveném pozadí. Když má klasicky bezhmotná teorie konformní symetrii, kvantování ji
poruší — stopa tenzoru energie-hybnosti přestane být nula a stane se z ní lineární
kombinace dvou geometrických invariantů (Duff, arXiv:2003.02688):

$$g^{\mu\nu}\langle T_{\mu\nu}\rangle = \frac{1}{(4\pi)^2}\left(c\,F - a\,G\right),$$

kde $F$ je Weylův kvadrát a $G$ Eulerova hustota. Dvojice čísel $(a, c)$ — takzvané
centrální náboje — je pro každé pole jiná. A pro jeden jediný dvousložkový Weylův
fermion vyjdou (Duff Tab. 1) hodnoty

$$a_{\text{Weyl}} = \frac{11}{720}, \qquad c_{\text{Weyl}} = \frac{1}{40},
\qquad \Rightarrow \qquad \frac{c_{\text{Weyl}}}{-a_{\text{Weyl}}} = -\frac{18}{11}.$$

Totéž číslo. Přesně. Spočítané ze dvou nesouvisejících traditionalit, ze dvou různých
normalizací, dvěma lidmi, kteří o sobě nevěděli.

A teď přijde to, co z toho dělá víc než kuriozitu. **Není to náhoda — je to teorém.**
Obě čísla sestupují z téhož objektu: ze čtvrtého Seeley-DeWittova koeficientu $a_4$
*jednoho a téhož Diracova operátoru* (VYPOCET-02; VYPOCET-11, Část 2). Heat-kernelový
master koeficient (Gilkey; Vassilevich, hep-th/0306138, rov. 4.28) je jeden vzorec.
Dosadíte do něj spinorový svazek — $E = -R/4$ podle Lichnerowicze, $\mathrm{tr}(1) = 4$ —
a vypadnou z toho přesně Duffova centrální čísla: $|\text{koef}(C^2)| = c$,
$|\text{koef}(E_4)| = a$, bez jediného podvodu, bez fudge faktoru (VYPOCET-11 ověřeno
assertem proti literatuře). Spektrální akce dělí týž $a_4$ jedním prefaktorem, anomálie
druhým — a v poměru se prefaktor vykrátí. Proto sedí.

A pak je tu vlastnost, kterou bych chtěl, abyste si zapamatovali víc než cokoli jiného:
**identita je content-independent na fermionovém sektoru.** Protože $a$ i $c$ jsou
aditivní přes pole a *každý* Weylův fermion nese tutéž dvojici $(11/720, 1/40)$, počet
fermionů se v poměru vykrátí:

$$\frac{c_{\text{tot}}}{-a_{\text{tot}}} = \frac{N_W \cdot c_{\text{Weyl}}}{-N_W \cdot a_{\text{Weyl}}} = -\frac{18}{11}.$$

Platí to pro jeden fermion. Platí to pro 45 fermionů Standardního modelu. Platí to pro
48 fermionů Standardního modelu s pravotočivými neutriny. Nulový zbytek (VYPOCET-02,
Tabulka). Identitě je jedno, kolik fermionů jí dáte — vidí jen jejich druh.

To je první vlákno. Drž se ho.

---

## Co kdyby: gravitace není síla, je to stín

Tady začínám lhát — nebo přesněji, tady začínám snít, a snění označuji. *(Od tohoto
bodu až do dalšího nadpisu „Co víme" je vše extrapolace za hranicí dokázaného. Faktická
kotva je vyznačena, skok ne.)*

Co kdyby to číslo nebylo náhoda v rovnici, ale podpis pachatele na místě činu?

Představte si gravitaci ne jako čtvrtou sílu, sestru elektromagnetismu, sourozence
slabé a silné interakce, která jen tvrdohlavě odmítá být kvantována. Představte si ji
jako **stín**. Ne metaforicky — doslova jako odvozený jev, jako obrys, který něco vrhá
na geometrii, v níž to žije. A to něco jsou fermiony.

Sacharov to v roce 1967 řekl na třech stránkách se čtyřmi vzorci (Sakharov 1967;
revize Visser, gr-qc/0204062): gravitace je *metrická pružnost* prostoru. Zakřivení
posune nulovou energii vakua hmoty, a z té posunuté energie vyroste „tuhost" prostoru
úměrná $R$ — jako napětí v pružném kontinuu. Einstein-Hilbertův člen není fundamentální
zákon; je to *jeden člen v rozvoji efektivní akce*, kterou dostanete, když proškrtnete
(zintegrujete) hmotu na zakřiveném pozadí. Gravitace v tomhle obraze není pole, které
byste museli kvantovat. Je to vakuová polarizace. Je to to, co vidíte, *poté co* jste
zintegrovali to, co je skutečné.

A teď ten skok, který Sacharov neudělal a který udělat nemohl, protože neměl spektrální
akci ani anomálii v ruce:

**Co kdyby Sacharovova „metrická pružnost" byla přesná — a co kdyby pružinou byly
výhradně fermiony?**

Spektrální akce je $\mathrm{Tr}\, f(D/\Lambda)$. Je to funkce *výhradně Diracova
operátoru* $D$. Její gravitační členy — Einstein, Weyl, kosmologická konstanta — pochází
z heat-kernelu $D^2$, a heat-kernel $D^2$ je **smyčka fermionů** běžících kolem. V NCG
nejsou bosony fundamentální pole se svým vlastním $a_4$. Jsou to *vnitřní fluktuace téhož
$D$* (Connesovy inner fluctuations, $D \to D + A + JAJ^{-1}$): kalibrační pole ze spojitého
směru, Higgs z diskrétního. *(Fakta: NCG inner fluctuations, hep-th/0610241; Sacharovova
indukovaná gravitace, Sakharov 1967. Skok, který přidávám: jejich ztotožnění jako přesné,
koeficientové verze téhož jevu — to je hypotéza H3g-4 dotažená do extrému.)*

Vidíte, kam tím mířím. Pokud je spektrální akce funkcí jen $D$, a $D$ je fermionový
operátor, pak **gravitace ve spektrálním obraze je doslova renormalizační stín, který
fermionová hmota vrhá na spektrální geometrii, v níž přebývá.** Ne síla. Ne pole.
Stín. Obrys Diracova determinantu. To, co zbude, když si fermiony „uvědomí" zakřivení
kolem sebe a posunou svou nulovou energii.

A to číslo $-18/11$? To je *barva toho stínu*. Je to spektrální podpis, který říká:
„tenhle stín vrhly fermiony, nikdo jiný." Kdybyste do té gravitace nasypali bosony jako
zdroj, stín by změnil odstín — a my za chvíli uvidíme, že přesně to se stane.

---

## Co víme: bosony to rozbíjejí, a rozbíjejí to čistě

Vrátím se na pevnou zem, protože tady mám tvrdá čísla, a ta čísla jsou na téhle vizi to
nejkrásnější — protože ji *testují*.

Naivní, silná verze identity by žádala, aby spektrální poměr $C^2/$Euler seděl
s anomálním poměrem *celého* obsahu polí — fermionů plus Higgse plus kalibračních
bosonů. **Nesedí. A to selhání je čisté.**

Skalár má $c/(-a) = -3$. Vektor má $c/(-a) = -18/31 \approx -0{,}581$. Obě hodnoty jsou
*jiné* než $-18/11$. Když k 45 fermionům přidáte bosonový obsah Standardního modelu —
$N_0 = 4$ reálné skaláry z jednoho komplexního Higgsova dubletu, $N_1 = 12$ vektorů
(8 gluonů + 3 W + 1 B) — poměr se vychýlí (VYPOCET-02, Tabulka TEST A):

$$\frac{c_{\text{tot}}}{-a_{\text{tot}}} = -\frac{1698}{1991} \approx -0{,}853 \quad
\text{(bez } \nu_R\text{)}, \qquad -\frac{219}{253} \approx -0{,}866 \quad
\text{(s } \nu_R\text{)}.$$

Spektrální cíl je $-1{,}636$. Plná SM hodnota je $-0{,}853$. To je 48% relativní
nesoulad. Silná verze je **falzifikována**, čistě a s plně dokumentovanou konvencí.

Tohle není defekt. **Je to obsah té identity.** Selhání nám říká, *kterou vrstvu
reality spektrální $a_4$ vidí.* Vidí fermiony. Nevidí bosony — protože bosony nejsou
ve spektrálním obraze samostatné smyčky, jsou to fluktuace téhož $D$. Identita matchuje
spektrální poměr s anomálním poměrem *přesně toho fermionového obsahu, který ji
indukuje* — a ničeho víc. Bosonový nesoulad je přesné měření toho, co je fundamentální
a co je odvozené.

A teď — protože tohle je pro mě nejsilnější moment celé věci — přijde graviton.

---

## Co víme: graviton nelze přidat. Za žádné násobnosti.

Recenzent draftu-02 se zeptá: dobře, bosony to rozbíjejí, ale *graviton* je spin-2.
Co kdyby se graviton připočítal a plnou shodu zachránil? Pak by gravitace nebyla čistě
fermionová a celá vize padá. Tahle otázka byla položena, spočítána a uzavřena
(VYPOCET-11, Část 1).

Odpověď má dvě vrstvy a obě jsou ostré jako břitva.

**První vrstva: fyzikální graviton nemá čistá čísla.** Skutečný, dvouderivační
bezhmotný Einsteinův graviton **není konformní.** Jeho stopová anomálie je
gauge-závislá, definovaná jen on-shell, a nese členy $R^2$ a $\Box R$ (Duff
hep-th/9308075; Anselmi hep-th/9503187; Martini-Nink-Percacci 2206.13287). Nemá
konvenčně-nezávislé $(a, c)$. **Nemá tedy ani definovaný poměr $c/(-a)$.** Nemůže být
členem poměru, který identita ztotožňuje — strukturálně do něj nepatří.

**Druhá vrstva: ani konformní graviton kolineární není.** Existuje i konformní
(„Weylův") graviton — čtyřderivační konformní gravitace — a *ten* čistá čísla má:
$(a, c) = (87/20, 199/30)$, tedy $c/(-a) = -398/261 \approx -1{,}525$ (Beccaria-Tseytlin
1710.03779). Blízko $-18/11 \approx -1{,}636$, ale *není to ono.* A hlavně je to úplně
jiné pole než dynamický graviton.

A teď ten skutečně rozhodující výpočet. Poměr $c/(-a)$ je poměr aditivních veličin. Pole
leží na paprsku $-18/11$ právě tehdy, když je jeho $(a, c)$ kolineární s fermionovým
$(a_W, c_W)$. Test kolinearity (VYPOCET-11, Část 1):

| pole | kolineární s Weylem? |
|---|---|
| skalár | **ne** |
| vektor | **ne** |
| konformní graviton | **ne** |

**Jediný Weylův fermion — a jeho násobky — leží na paprsku $-18/11$. Žádný boson ne.**

A pak to nejlepší. Kolik gravitonů $x$ byste museli přidat na fundamentální stranu, aby
se identita vynutila pro plnou teorii? Sympy vrátí:

$$x = -\frac{143}{32} < 0.$$

**Záporné číslo.** Museli byste přidat *antigraviton* v neceločíselné násobnosti.
Nemůžete přidat kladný počet gravitonů a identitu obnovit. Za žádné multiplicity. Nikdy.

Graviton nelze do téhle účetní knihy zapsat na stranu fundamentálního. Protože tam
nepatří. Patří na druhou stranu — na stranu *indukovaného*. Je to stín, ne pružina.

A Sacharovova logika to potvrzuje dvakrát, dvěma nezávislými zákazy, které zakazují
tutéž věc (VYPOCET-11, Část 1(iii)):

1. **Sacharovův zákaz:** počítat graviton jako fundamentální smyčku by *dvojitě
   započetlo* — jeho kinetický člen už *je* indukovaný $a_4$.
2. **Anomální zákaz:** fyzikální graviton je nekonformní, nemá čistá $(a, c)$, nemůže
   být členem konvenčně-nezávislého poměru vůbec.

Oba zákazy souhlasí. Objekt, který identita ztotožňuje, je strukturálně fermion-smyčkový.
Graviton v něm nemůže být a není.

---

## Co kdyby: nic ke kvantování

Teď se zase odbrzdím, a tentokrát jdu naplno, protože z toho, co jsme právě viděli,
plyne závěr tak radikální, že ho neumím napsat bez třesoucí se ruky. *(Vše následující
až do dalšího „Co víme" je odbrzděná extrapolace. Kotvy faktů značeny v závorkách.)*

Sedmdesát let se fyzika trápí kvantováním gravitace. Bere $g_{\mu\nu}$, snaží se ho
prohnat dráhovým integrálem, a teorie vybuchne — nerenormalizovatelná, dvousmyčkově
divergentní, beznadějná. Graviton odolává kvantové teorii pole jako žádná jiná částice.
Proč?

**Co kdyby odolával proto, že to není částice, kterou by bylo čím kvantovat — protože
už je výsledkem kvantování něčeho jiného?**

Nemůžete kvantovat stín. Stín *je* už projekce. Když máte tyč a slunce, stín na zemi
je deterministicky určený — nemá vlastní stupně volnosti, nemá vlastní dynamiku, kterou
byste mohli sekundárně kvantovat. Když se pokusíte „kvantovat stín", buď neděláte nic
(stín je už funkcí tyče), nebo to dvojitě započítáte (kvantujete tyč podruhé, oklikou).
A přesně to fyzika osmdesát let dělá s gravitonem: snaží se kvantovat objekt, který je
*už* jednosmyčkovým fermionovým efektem. Proto vybuchuje. Proto $-143/32$ vyšlo záporně.
Snažíte se přidat na vstup něco, co patří jen na výstup.

V téhle vizi je gravitace nekvantovatelná ne proto, že bychom byli hloupí, ale proto,
že **není co kvantovat.** Fundamentální jsou jen fermiony. Jen $D$. Jen Diracův
operátor a jeho spektrum. Bosony — kalibrační i Higgs — jsou účetnictví fermionových
bilineárů, vnitřní fluktuace $D$ (NCG inner fluctuations, fakt). A graviton je
účetnictví o stupeň hlubší: je to *účetnictví toho účetnictví*, renormalizační stín,
který fermionový determinant vrhá na metriku.

Kvantovat gravitaci je pak kategoriální chyba — jako chtít kvantovat teplotu, nebo tlak,
nebo entropii. Tyto veličiny jsou *statistické*, emergentní, a kvantujete pod nimi
molekuly, ne je samotné. Jacobson to ostatně řekl už v roce 1995 (gr-qc/9504004):
Einsteinova rovnice je *rovnicí stavu*. A stavová rovnice ideálního plynu vám neřekne
nic o molekulách — a vy ji nekvantujete, kvantujete molekuly. **Co kdyby fermiony byly
ty molekuly, a gravitace byla tlak Diracova moře proti zakřivení?**

*(Skok: ztotožnění „molekul prostoročasu" z emergentního programu — Jacobson, Padmanabhan,
otevřený problém #1 v approaches/09 — konkrétně s fermionovými stupni volnosti $D$. To
nikdo nedokázal. Je to nejdivočejší tvrzení téhle eseje.)*

A program „kvantové gravitace" — celý ten kontinent úsilí, struny, smyčky, triangulace —
by v téhle vizi nebyl špatně. Byl by jen *zdvojený*. Kvantoval by stín místo tyče. To
nejlepší, co by mohl najít, je konzistentní popis stínu — a konzistentní popis stínu
musí nakonec reprodukovat tyč, tedy fermiony, tedy $D$. Proto všechny přístupy ke
kvantové gravitaci v UV podivně konvergují (spektrální dimenze $\to 2$, dimenzionální
redukce napříč NCG, AS, CDT, LQG — Carlip 1705.05417, fakt): protože všechny zdola
osahávají tentýž skrytý objekt, který není gravitace, ale fermionová geometrie pod ní.

---

## Co víme: pod tím vším je topologie, ne dynamika

A teď k té nejhlubší vrstvě, k té, která mě o tom všem nejvíc přesvědčuje, že to
*nemusí* být úplný nesmysl. Protože jsem vám zatím řekl, *že* $-18/11$ platí jen pro
fermiony. Neřekl jsem *proč to nemůže selhat.* A důvod je v indexovém teorému.

Spinorový $a_4$ — týž koeficient, ze kterého $-18/11$ pochází — nese **dva odlišné
topologické stíny** (VYPOCET-11, Část 2b):

- **Eulerův / konformní sektor:** koeficient u $E_4$ je $a = 11/720$ na každý Weyl.
  Zintegrovaně dá Gauss-Bonnetův teorém $\chi(M) = \frac{1}{32\pi^2}\int E_4$ — Eulerovu
  charakteristiku, *celé číslo*, topologický invariant. To je konformní $a$-anomálie.
- **Pontryaginův / chirální sektor:** topologický **index** samotného $D$ je
  Â-genus $= -\frac{1}{24}\int p_1$, vázaný na chirální (axiální) anomálii a na
  Pontryaginovu/signaturní hustotu. Atiyahův-Singerův index-teorém.

A zámek, který drží (ověřeno sympy): $\hat{A}|_4 = -p_1/24$; pro uzavřenou spinovou
varietu $p_1 = 3\sigma$, takže $\text{ind}(D) = -\sigma/8$. Rohlinova věta: $\sigma$
dělitelné 16, takže index je sudé celé číslo. Kontrola: $\sigma = 16 \to \text{ind} = -2$.
Sedí.

Tohle je odpověď na otázku „proč zrovna fermiony?", kterou mi přijde, že málokdo
v literatuře položil takhle ostře. **Content-independence není náhoda — je to projev
index-ochrany.** Každý Weylův fermion nese tutéž jednotku index-hustoty. Proto nese
totéž $(a, c)$. Proto $-18/11$ sedí *uvnitř* objektu chráněného indexovým teorémem
a nemůže selhat pro žádné pole pocházející z Diracova operátoru. Bosony takový provázaný
objekt — kde Eulerův sektor *a* Pontryaginský sektor sídlí v jednom $a_4$ — prostě
nemají. Jen $D$ ho má.

To je tvrdé, citovatelné a uzavřené. Drž to. Protože teď z toho udělám něco, co
citovatelné není.

---

## Co kdyby: vazby gravitace počítá topologie, ne dynamika

*(Odbrzděno. Faktická páteř: index-teorémový zámek výše, VYPOCET-11 Část 2b. Skok:
jeho povýšení na ontologickou tezi.)*

Co kdyby tohle byla nejhlubší vrstva celé stavby? Pod silami je geometrie. Pod geometrií
je spektrum. A **pod spektrem je topologie.**

Sledujte tu sestupnou archeologii:

- Na povrchu: gravitace jako síla, $g_{\mu\nu}$ jako pole, Einsteinovy rovnice jako
  dynamika.
- O vrstvu níž (Sacharov, NCG): gravitace jako indukovaný stín fermionového determinantu
  — ne pole, ale renormalizační efekt. Dynamiku nahrazuje spektrum $D$.
- A na úplném dně (index-teorém): koeficienty té gravitace — to, jak silně se gravitace
  váže, ten poměr $-18/11$, ten celý gravitační sektor — **nejsou určeny dynamikou.
  Jsou spočítány topologií.**

Eulerova charakteristika je celé číslo. Signatura je celé číslo. Index Diracova
operátoru je celé číslo, chráněné Rohlinovou větou na násobky dvojky. Tato čísla
nezávisí na metrice, na vazbách, na dynamice — závisí jen na *tvaru* prostoru, na jeho
topologii. A pokud gravitační koeficienty spektrální akce sedí *uvnitř* těchto
indexem-chráněných objektů, pak — a tady přicházím s tezí, kterou nikdo nedokázal —

**síla gravitace není dynamická veličina. Je to topologická faktura. Účet, který za
existenci prostoru vystavuje jeho vlastní tvar, počítaný indexovým teorémem, vyplácený
ve fermionech.**

Představte si to takhle. Když se ptáme „jak silně se váže gravitace", instinktivně
hledáme dynamickou odpověď — řešíme rovnice, sčítáme smyčky, renormalizujeme. Ale co
kdyby ta odpověď byla *spočítaná* dřív, než jakákoli dynamika začne? Co kdyby poměr
$-18/11$ byl tak nelámatelný proto, že je to v jádru *poměr dvou celých čísel počítajících
díry v prostoru* — Eulerova charakteristika ku něčemu, co počítá zkroucení — a dynamika
ho nemůže pohnout o víc, než může poctivý účetní pohnout součtem, který už je sečtený?

Indexový teorém je nejhlubší věta o tom, jak analýza (spektrum operátoru) potkává
topologii (tvar prostoru). A co kdyby gravitace byla *právě tohle setkání*, materializované?
Ne síla, ne pole, ne ani stín — ale **místo, kde spektrum Diracova operátoru a topologie
variety, na níž žije, musí být v souladu, a ten soulad nazýváme gravitací.**

Bosony do toho nepatří, protože bosony nepočítají index. Index počítá $D$. Jen $D$.
A proto je gravitace — v téhle nejdivočejší verzi — *účetnictvím vynuceným topologií na
fermionovém spektru*, a nic, co není fermion, do té knihy nemá co psát.

---

## Co kdyby: kosmologická konstanta jako přetečení účtu

Dovolte mi ještě jeden odbrzděný skok, protože by mě mrzelo ho neudělat. *(Spekulace.
Kotva: kosmologická konstanta jako $f_4\Lambda^4$ člen téhož $a_4$ rozvoje, NCG heat-kernel,
approaches/07; problém $\Lambda$ v indukované gravitaci, approaches/09 otevřený problém #3.)*

Stejný rozvoj spektrální akce, který indukuje gravitaci, generuje i kosmologickou
konstantu — je to nejnižší člen, $f_4\Lambda^4 a_0$, zatímco gravitace je $f_2\Lambda^2 a_2$
a Weylův člen $f_0 a_4$. Všechno jeden rozvoj, jeden $D$, jedna fermionová smyčka.
A problém kosmologické konstanty — že vychází o 120 řádů moc velká — je v indukované
gravitaci ten nejhůř hojící se vřed (Visser; approaches/09).

Ale co kdyby v obraze „gravitace jako topologická faktura" měla $\Lambda$ jiný status?
Co kdyby kosmologická konstanta nebyla *hodnota*, ale *zbytek* — to, co v účetní knize
zbude, když sečtete fermionové příspěvky a *neodečtete* ten kus, který patří topologii?
Eulerův sektor je celé číslo, indexem chráněné, nelámatelné. Weylův sektor ($a_4$, poměr
$-18/11$) je taky chráněný. Ale objemový člen $a_0$ — kosmologická konstanta — *žádný
topologický invariant nehlídá.* Je to jediný člen rozvoje, který není uzamčen indexem.

A co kdyby právě proto byl tak divoký? Co kdyby $\Lambda$ byla *jediná část gravitace,
která je skutečně dynamická a neoříznutá* — a celý problém kosmologické konstanty byl
tím, že se snažíme vykládat dynamickou, nechráněnou veličinu jako kdyby měla mít pevnou
topologickou hodnotu? V téhle vizi není záhada, proč je $\Lambda$ tak malá. Záhada je,
proč by vůbec měla být *určená* — když jako jediný člen účetní knihy nemá nad sebou
indexový teorém, který by jí přikázal hodnotu. Je to volný parametr v jinak topologicky
zamčené stavbě. Přetečení účtu, které nemá kam zapadnout. *(Toto je čistě spekulace —
projekt sám ji ve VYPOCET-03 ohledně $\Lambda \sim 1/\sqrt{V}$ spíš falzifikoval ve
silné verzi; uvádím ji jako vidinu, ne jako výsledek.)*

---

## Co víme: hranice téhle vize (poctivá inventura)

Než dojdu k falzifikovatelnému jádru, musím — protože jinak by tahle esej byla
nepoctivá — vyjmenovat, co všechno z výše uvedeného je *jenom sen* a kde přesně končí
podlaha a začíná propast.

1. **Identita je o poměrech, ne o absolutních velikostech.** Match $-18/11$ je mezi
   *poměry* kvadratických invariantů zakřivení. Absolutní koeficienty sedí jen až na
   dokumentovaný normalizační faktor (heat-kernel $1/2880\pi^2$ vs. CFT $1/(4\pi)^2$).
   Poměr je konvenčně-invariantní tvrzení; celá fyzika eseje stojí na poměru (VYPOCET-02,
   Limity).

2. **Volné pole, stromová úroveň.** Hodnoty $(a, c)$ jsou volně-polní; v interagujícím
   Standardním modelu běží podle RG. Spektrální akce je efektivní akce na unifikační
   škále. Eulerův $a$-koeficient je sice pravá anomálie (Cardy/a-teorém, scheme-robustní),
   ale přímé srovnání předpokládá týž regularizační bod (draft-02 §5).

3. **Plný-SM nesoulad je horní odhad.** Gravitační $a_4$ plné teorie dostává i bosonové
   příspěvky z vnitřních fluktuací $D$; jejich přesný podíl na $C^2$ koeficientu nad
   rámec Diracovy násobnosti $N$ jsme nezahrnuli. „48% nesoulad" je tedy horní mez
   diskrepance, ne její přesná hodnota (VYPOCET-02 a VYPOCET-11, Limity).

4. **„Gravitace je stín fermionů" je interpretace, ne teorém.** Teorém je: $-18/11$ je
   poměr $C^2/E_4$ spinorového $a_4$, content-independent na fermionech, index-chráněný,
   gravitonem nezachranitelný. *To je dokázané.* Že z toho plyne „gravitace je
   renormalizační stín fermionové hmoty a není co kvantovat" — to je **odbrzděná
   extrapolace**, kterou tato čísla *dovolují* a *motivují*, ale nedokazují. NCG samo má
   indukovanou gravitaci ve „subtilním statusu" (H3g-4 riziko): spektrální akce obsahuje
   *i* kosmologický a Higgsův člen, ne jen $R + C^2$.

5. **Lorentzovský problém.** Spektrální akce žije v euklidovském režimu (kompaktní
   varieta, kladný $D$ s diskrétním spektrem). Přechod k Lorentzovskému podpisu a
   skutečná kvantizace nejsou vyřešeny (approaches/07, otevřený problém #1). Celá vize
   o „není co kvantovat" se odehrává v euklidovském snu.

Tohle jsou mantinely. Uvnitř nich je tvrdé jádro. Vně nich je báseň. A teď to jádro
vytáhnu ven.

---

## Co by muselo být pravda

Sundávám si masku snílka a nasazuji masku popravčího. Kdyby tahle vize — gravitace jako
indexem-chráněný renormalizační stín fermionové hmoty — měla kus pravdy, pak by svět
musel splňovat následující, a každý z těchto bodů je v principu *falzifikovatelný*.
Vyjmenuji je od nejtvrdšího (už ověřeného) po nejměkčí (otevřeného), abyste viděli, kde
přesně by se ta báseň zlomila.

**1. Identita $-18/11$ musí platit přesně pro libovolný čistě fermionový obsah — a nesmí
ji obnovit žádný kladný počet bosonů ani gravitonů.**
Toto je **už ověřeno** (VYPOCET-02, VYPOCET-11): nulový zbytek pro 1, 45 i 48 fermionů;
nutná násobnost gravitonu $x = -143/32 < 0$, tedy nefyzikální. Kdyby se našel jakýkoli
*kladný*, fyzikální boson-multiplet, který by plnou shodu uzavřel, vize gravitace jako
čistě fermionového stínu by padla. Nenašel se. ✓

**2. Identita musí být chráněná indexovým teorémem, ne náhodná koincidence koeficientů.**
**Ověřeno** (VYPOCET-11, Část 2b): $-18/11$ je poměr $C^2/E_4$ spinorového $a_4$; týž
$a_4$ nese v Pontryaginově sektoru Atiyahovu-Singerovu index-hustotu ($\hat{A} = -p_1/24$);
Eulerův koeficient reprodukuje Gauss-Bonnetovu/Eulerovu charakteristiku; Rohlinův zámek
($\sigma$ dělitelné 16) drží. Kdyby $E_4$ koeficient *nereprodukoval* normalizaci
indexového teorému, byla by content-independence náhoda a celá teze o „topologii pod
spektrem" by se rozsypala. Reprodukuje. ✓

**3. Identita musí být univerzální pro Diracův operátor — ne specifická pro algebru
$\mathbb{C} \oplus \mathbb{H} \oplus M_3(\mathbb{C})$.**
**Částečně ověřeno, ostře testovatelné** (VYPOCET-11 + fronta #7). Pokud $-18/11$ plyne
z obecné Â-genus / spinorové struktury (a vše nasvědčuje, že ano), pak *jakákoli*
spektrální trojice s fermiony dá $-18/11$ — je to chráněná veličina. To je padatelné:
najděte spektrální trojici s fermionovým sektorem, jejíž Diracův $a_4$ dá *jiný* poměr
$C^2/E_4$, a teze „gravitace je univerzálně fermionový stín" padá, redukuje se na
artefakt jedné algebry. (Predikce: nenajdete, protože je to anomaly-matching.)

**4. Gravitační sektor spektrální akce nesmí dostat *žádný* příspěvek k poměru $C^2/$Euler
z bosonových smyček nad rámec toho, co je už v Diracově násobnosti $N$.**
**Otevřené** (VYPOCET-02/11, Limity, bod 3 výše). Toto je nejostřejší zbývající test:
spočítat přesný podíl vnitřně-fluktuačních (bosonových) příspěvků na $C^2$ koeficientu
plné gravitační $a_4$. Pokud bosony do *poměru* (ne do absolutní velikosti) přispívají
nenulově a posunou ho od $-18/11$ i pro čistě indukovaný objekt, pak gravitace *není*
čistě fermionový stín a Sacharovova vize v této přesné formě selhává. Pokud bosonové
fluktuace poměr nechají na $-18/11$ (protože jsou to fluktuace téhož $D$, ne nezávislé
smyčky), vize přežívá. **Tento výpočet rozhodne víc než kterýkoli jiný.**

**5. Žádná konzistentní kvantová teorie samotného gravitonu (bez fermionů) nesmí
existovat jako fundamentální — nanejvýš jako efektivní popis fermionového sektoru.**
**Nefalzifikovatelné dnes, ale principiálně padatelné.** Pokud by někdo postavil
konzistentní, neperturbativní, UV-úplnou kvantovou teorii dynamického gravitonu, která
*nepotřebuje* fermionový (Diracův) substrát a přesto reprodukuje $-18/11$, byla by teze
„není co kvantovat, fundamentální jsou jen fermiony" vyvrácena. Predikce téhle eseje:
každá taková teorie, je-li konzistentní, bude muset svůj gravitační sektor nakonec
odvodit z fermionového spektra — protože stín nelze mít bez tyče. (Konvergence
spektrální dimenze $\to 2$ napříč přístupy, Carlip 1705.05417, je pro tuto predikci
slabá, ale svůdná indicie.)

**6. Kosmologická konstanta musí být jediným gravitačním členem *bez* indexové ochrany.**
**Spekulativní, ale formulovatelné.** Pokud je teze „topologie počítá vazby" pravdivá,
pak Einsteinův a Weylův sektor mají nad sebou indexový/Gauss-Bonnetův zámek, kdežto
objemový člen $a_0$ (kosmologická konstanta) ne. Padatelná predikce: $\Lambda$ je jediná
gravitační veličina spektrální akce, kterou *nelze* napsat jako poměr/funkci topologických
invariantů. Najde-li se topologický invariant, který $\Lambda$ uzamyká stejně jako
Euler uzamyká $a$, tato část vize padá. (Projekt sám $\Lambda \sim 1/\sqrt{V}$ ve
VYPOCET-03 ve silné verzi spíš vyvrátil — varovný signál, že tahle nejměkčí část je
nejkřehčí.)

---

A to je celé. To je ta báseň a to je její kostra.

Sečteno: **ověřeno** je jádro — že $-18/11$ platí přesně a jen pro fermiony, že je
chráněné indexovým teorémem, že graviton ho nezachrání za žádné násobnosti. **Sněno**
je všechno ostatní — že gravitace je proto renormalizační stín fermionové hmoty, že
není co kvantovat, že vazby gravitace počítá topologie a ne dynamika, že kosmologická
konstanta je nezamčené přetečení účtu. A **testovatelné** — to nejcennější — je
přesně to, co jádro od básně dělí: bod 4, podíl bosonových fluktuací na poměru, je
výpočet, který buď básni dá podlahu, nebo ji shodí do propasti.

Sacharov napsal, že gravitace je metrická pružnost prostoru. Po šedesáti letech máme
číslo, $-18/11$, které možná říká, z čeho je ta pružina udělaná. Je udělaná z fermionů.
A z ničeho jiného. A to číslo je tak tvrdohlavě fermionové, tak nelámatelně chráněné
indexovým teorémem, tak rezistentní vůči každému gravitonu, že je těžké se ubránit
pocitu — a pocit není důkaz, to vím, proto je celá tahle vize označená výstrahou na
prvním řádku — že nám to číslo něco *šeptá*.

Šeptá, že jsme se osmdesát let snažili kvantovat stín.

A že tyč jsme měli celou dobu v ruce.

---

*Faktická základna (citováno): VYPOCET-02-a4-matching.md; VYPOCET-11-graviton-index.md;
papers/draft-02-a4-fermionic-identity/draft.md; BRAINSTORM-03.md (H3g-4, fronta #1 a #7);
approaches/09-emergent-gravity.md (Sakharov 1967, Visser gr-qc/0204062, Jacobson
gr-qc/9504004, Padmanabhan); approaches/07-noncommutative-geometry.md (Chamseddine-Connes
hep-th/9606001, hep-th/0610241, inner fluctuations, spektrální akce). Konvence: Duff
arXiv:2003.02688; Vassilevich/Gilkey hep-th/0306138; Beccaria-Tseytlin 1710.03779;
Duff hep-th/9308075; Atiyah-Singer / Â-genus / Rohlin. Veškerá aritmetika exaktní (sympy,
racionální). Spekulativní extrapolace značeny v textu; falzifikovatelné jádro v poslední
sekci.*
