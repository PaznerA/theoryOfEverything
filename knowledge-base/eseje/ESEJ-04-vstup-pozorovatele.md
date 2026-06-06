# Vstup pozorovatele do vesmíru

> ⚠️ SPEKULATIVNÍ ESEJ — fantazie odbrzděná, fakta citována, extrapolace značeny

---

Začněme otázkou, která zní jako záhada zenového kóanu, ale je to věta z recenzované
matematické fyziky:

**Existuje entropie ve vesmíru, ve kterém není nikdo, kdo by ji změřil?**

Ne jako filozofická hříčka. Jako technický fakt o jisté třídě operátorových algeber.
A odpověď, kterou dnes nejlepší matematika kvantové gravitace dává, je nepříjemně
přímá: **ne.** Než do oblasti prostoročasu vstoupí pozorovatel — doslova: než k poli
přidáte jeden jediný stupeň volnosti, který nese hodiny — entropie té oblasti není
nekonečná. Ona *neexistuje*. Není definovaná. Není to veličina, která by měla velkou
hodnotu nebo malou hodnotu; je to veličina, kterou nelze ani napsat, protože algebra,
na níž by žila, nemá stopu.

A v okamžiku, kdy pozorovatel vstoupí, se cosi zlomí. Algebra změní typ. Stopa se
zrodí. A entropie — náhle, z ničeho — *začne být*.

Tahle esej je o tom okamžiku. O vstupu pozorovatele do vesmíru jako o události, která
nemění *kolik* vesmír ví o sobě, ale *zda vůbec* je co vědět. Budu poctivý k faktům:
všechno v sekcích **„Co víme"** je buď teorém z literatury (Connes, Tomita-Takesaki,
Bisognano-Wichmann, CLPW), nebo číslo z výpočtů tohoto projektu (VYPOCET-12, -16, -18),
citované a reprodukovatelné. A budu odbrzděný v sekcích **„Co kdyby"**, kde si dovolím
ptát se, jestli entropie není vlastnost světa, ale vlastnost *světa-i-se-svědkem* — a
každý takový skok zřetelně označím. Na konci, v **„Co by muselo být pravda"**, fantazii
přibrzdím a vytáhnu z ní falzifikovatelné jádro.

Nadechněte se. Tohle je esej o tom, že pozorovatel možná není ve vesmíru. Možná je tím,
co z hejna vztahů vesmír *dělá*.

---

## Co víme: před pozorovatelem není entropie, je jen tok

Musím vás nejdřív vzít do nejdivočejšího koutu matematické fyziky — do klasifikace
von Neumannových algeber — protože celá esej visí na jediném strukturálním faktu, který
většina fyziků nikdy neslyšela, přestože platí pro *každou* relativistickou kvantovou
teorii pole.

Když si vezmete pozorovatelné kvantové mechaniky konečně mnoha částic, žijí v algebře
**typu I**: obyčejné operátory na Hilbertově prostoru, ostré stavy, hustotní matice,
„bity". Tahle algebra má stopu, $\mathrm{Tr}$, a s ní všechno, na co jsme zvyklí —
von Neumannovu entropii $S = -\mathrm{Tr}(\rho\ln\rho)$, redukované stavy, počítání
mikrostavů. To je svět, v němž si fyzik myslí, že žije.

Ale lokální algebra pozorovatelných v *libovolné* ohraničené oblasti relativistické
QFT — algebra observable v Rindlerově klínu, v kauzálním diamantu, v kterékoli
otevřené oblasti — **není typu I.** Je to von Neumannova algebra **typu III$_1$** —
nejchaotičtější třída v celé Murray-von Neumannově a Connesově klasifikaci (Araki;
Fredenhagen 1985; Buchholz-Verch hep-th/9501063; pilíř 19). A typ III$_1$ má vlastnosti,
které zní jako rouhání:

- **Nemá stopu.** Vůbec žádnou. $\mathrm{Tr}$ neexistuje jako funkcionál na téhle algebře.
- **Nemá hustotní matice.** Žádný stav nelze napsat jako $\rho$, protože není $\mathrm{Tr}$,
  vůči níž by se $\rho$ definovala.
- **Entanglementní entropie podoblasti je principiálně UV-divergentní** — ne „velká", ale
  bez konečné hodnoty, protože není stopový funkcionál, který by ji změřil (Witten
  1803.04993: „entanglement je vlastnost algebry, ne stavů").
- **Žádný stav nefaktorizuje přes hranici** (Reeh-Schlieder): vakuum je cyklické a
  separující pro algebru libovolně malé oblasti.

Zastavte se nad tím. V relativistické QFT — v té nejlépe ověřené teorii, jakou lidstvo
má — entropie kusu prostoru **není definovaná veličina.** To není selhání měření. Je to
strukturální fakt o typu algebry.

A teď to nejhlubší, kvůli čemu sem celý tenhle aparát tahám. Typ III$_1$ *nemá stavy
v obvyklém smyslu, nemá entropii, nemá hustotní matice* — ale **má jednu jedinou věc,
kterou si z dvojice (algebra, vektor) sám vyrobí: čas.** Tomitova-Takesakiho modulární
teorie z jediného cyklicko-separujícího vektoru $|\Omega\rangle$ kanonicky extrahuje
jednoparametrický tok

$$\sigma_t(a) = \Delta^{it}\,a\,\Delta^{-it}, \qquad \Delta = e^{-K},$$

kde $K = -\log\Delta$ je modulární Hamiltonián, a involutivní dualitu $J M J = M'$ mezi
algebrou a jejím komutantem (pilíř 19, Matematický rámec). Bez vnějšího Hamiltoniánu.
Bez vnějších hodin. **Z algebry samé vyteče čas.**

Connes a Rovelli (gr-qc/9406019) z toho udělali tezi, kterou si musíte přečíst pomalu,
protože je tak troufalá, jak jen fyzika dovolí: **v obecně kovariantní teorii není
preferovaný vnější čas; fyzikální časový tok *je* modulární tok stavu.** Termodynamický
stav vesmíru si svým vlastním modulárním tokem *vyloučí svůj vlastní čas* — je KMS
(termální) vůči $\sigma_t$ při $\beta = 1$ (pilíř 19, hypotéza termálního času).

Shrnu to do jediného obrazu, který si od téhle sekce odneste. **Před pozorovatelem je
oblast prostoročasu čistý relační tok bez entropie — typ III$_1$ — který sám sebe
proudí v modulárním čase, ale neví o sobě nic, co by se dalo spočítat. Je to dění bez
účetnictví. Sloveso bez podstatného jména.**

---

## Co víme: pozorovatel vstoupí — a typ III se zlomí na typ II

A teď přijde revoluce let 2022 a dál, kvůli které jsem tuhle esej vůbec začal psát.

Co se stane, když do té bezstopové, bezentropické, čistě relační algebry typu III$_1$
**vstoupí pozorovatel**? Ne metafyzicky — matematicky přesně: přidáte jeden stupeň
volnosti, který nese hodiny, tj. operátor energie $\hat{p}$, a obléknete pole na jeho
světočáru. Chandrasekaran-Longo-Penington-Witten (CLPW, 2206.10780) a Witten
(2112.12828) ukázali, co to udělá. Konstrukce se jmenuje **zkřížený součin
(crossed product)**:

$$\mathcal{N} = M \rtimes_\sigma \mathbb{R} \quad\text{na } \mathcal{H}\otimes L^2(\mathbb{R}),
\qquad M\ \text{typ III}_1 \;\Longrightarrow\; \mathcal{N}\ \text{typ II}.$$

Přidáte hodiny, obléknete je modulárním tokem $\sigma$ pozadí — a algebra **změní typ**.
Z typu III$_1$ se stane typ II. A typ II má všechno to, co III$_1$ neměl:

- **Má stopu** (semikonečnou, jednoznačnou až na škálu).
- **Má hustotní matice:** $\langle\psi|a|\psi\rangle = \mathrm{Tr}(\rho_\psi a)$.
- **Má konečnou, renormalizovanou entropii** $S(\psi) = -\mathrm{Tr}(\rho_\psi\log\rho_\psi)$.

A — tohle je mostní výsledek celého oboru — ta renormalizovaná von Neumannova entropie
typu II zkříženého součinu **JE zobecněná entropie**:

$$S(\hat\rho) = \frac{\langle A\rangle}{4G_N} + S_{\text{out}} + \text{const} = S_{\text{gen}}.$$

Jednotlivé členy divergují — plocha $A/4G_N$ jako $G\to 0$, $S_{\text{out}}$ z horizontového
entanglementu (typ III) — ale jejich *součet je konečný* (CLPW; Chandrasekaran-Penington-Witten
2209.10454; Kudler-Flam-Leutheusser-Satishchandran 2309.15897: zobecněná entropie černé díry
JE von Neumannova entropie na libovolném Killingově horizontu). Pozorovatel/hodiny je
*struktura, jež činí gravitační entropii konečnou.*

Přečtěte to ještě jednou, protože je to filozoficky neslýchané a matematicky tvrdé:
**entropie oblasti není definovaná, dokud k ní nepřidáte pozorovatele. S pozorovatelem
je konečná a rovná se $A/4G + S_{\text{out}}$. Bez pozorovatele neexistuje.** Není to
tak, že pozorovatel entropii *změří*. Pozorovatel ji **stvoří** — protože teprve jeho
přidání dá algebře stopu, vůči níž entropie vůbec dává smysl.

A v de Sitterově vesmíru — uzavřeném vesmíru bez hranice — je to nejostřejší. Tam je
pozorovatelova algebra typu **II$_1$** (CLPW), což je třída se *maximálně-entropickým
stavem*. Ten maximální stav je **prázdný de Sitter** s Gibbonsovou-Hawkingovou entropií
kosmologického horizontu $A/4G$. V uzavřeném vesmíru je pozorovatel *nutný už pro
samotnou definici* entropie (pilíř 19: „pozorovatel nutný už pro definici entropie
v uzavřeném vesmíru").

To je literatura. To je dokázané. Teď k číslům, která tomuhle příběhu dal tenhle projekt.

---

## Co víme: viděli jsme ten zlom v číslech (VYPOCET-12, -16)

Celá výše uvedená stavba je nekonečně-dimenzionální matematika spojitých algeber.
„Typ" je asymptotický invariant — na konečné matici ho nezměříte, protože každá konečná
algebra je triviálně typu I$_n$. Tenhle projekt přesto udělal něco, co podle pilíře 19
„nikdo nedělal": **změřil numerické proxy přechodu III$_1 \to$ II na kauzální množině**
(causal set) — diskrétní, Lorentzovsky-invariantní mřížce prostoročasu.

Mechanismus: Sorkinova-Yazdiho prostoročasová entanglementní entropie (SSEE) je
divergentní (objemový zákon) až do okamžiku **dvojité truncace** Pauli-Jordanova spektra,
která zahodí módy pod jistou diskrétnostní škálou. A hypotéza projektu (H3g-3) zní: **ta
truncace JE přechod III$_1 \to$ II — diskrétní škála prostoročasu hraje roli
pozorovatelského/modulárního (crossed-product) cutoffu.** Diskrétnost prostoročasu = vestavěný
pozorovatel.

**VYPOCET-12** (2D, čistý kauzální diamant, N = 400–1800, 8 seedů, F-015) to otestoval
třemi nezávislými proxy. Čísla:

- **Stopa kolabuje 80×.** Netruncovaná entropická stopa roste objemově, $S_{\text{full}}\sim N^{1.04}$
  (divergentní stopa = III). Po truncaci saturuje na 1,30–1,70 (konečná stopa = II). Při
  N = 1800 kolaps faktorem **80×** (135,9 → 1,70). To je přímá entropická signatura III → II.
- **Modulární spektrum: pile-up → 0.** Tohle je nejčistší výsledek celého výpočtu.
  Netruncovaný modulární spektrum $\{\varepsilon_k = \ln[\mu_k/(\mu_k-1)]\}$ je **plochá,
  hustá, neintegrabilní hustota hromadící se u $\varepsilon = 0$** — to *je* definiční
  Connesova vlastnost typu III$_1$, $S(M) = [0,\infty)$. Pile-up u $\varepsilon < 0{,}5$
  roste jako $N^{1.14}$. Po truncaci: **přesně nula.** Spektrum se stane kompaktně-neseným,
  integrabilním, s **ostrou IR hranou** nad $\varepsilon \gtrsim 1{,}6$ — definiční
  vlastnost typu II. **První numerická realizace Connesova modulárního invariantu na
  kauzální množině.**
- Třetí proxy (centrální sekvence) potvrdila faktorové self-averaging, ale nerozlišila
  trunc od full — poctivě označeno jako nerozhodnuté.

Verdikt VYPOCET-12: **2/3 proxy konzistentní s III$_1 \to$ II ve 2D.**

A pak **VYPOCET-16** (F-019) tentýž program zopakoval ve **fyzikální dimenzi d = 4** —
na čisté slab geometrii (plochá Rindlerovsky-podobná entangling plocha, kde SJ stav $\approx$
Unruh $=$ Hadamard, žádné rohy). Tam **všechny tři proxy platí, 3/3**:

- **Stopa kolabuje 36×.** $S_{\text{full}}\sim N^{1.34}$ (objem/super-objem, III) →
  $S_{\text{number}}\sim N^{0.55}\approx\sqrt{N}$ (4D area-law, II). Kolaps 36× při N = 3500.
- **Ostrá modulární IR hrana u $\varepsilon \approx 2{,}7$.** Pile-up $\sim N^{1.27}$ →
  přesně 0. Plochá hustá → kompaktně-nesená.
- **A nejostřejší výsledek: rank $N^{3/4}$ JE operativní regulátor.** Jen area-law rank
  $n_{\max}\sim N^{3/4}$ převede stopu na area-law $\sqrt{N}$ (typ II); fixní-frakční
  magnitudový cutoff, který ponechá $\sim N^{0.9}$ módů, **selhává** ($S\sim N^{0.83}$,
  mimo area law). Typová signatura žije *přesně* v area-law rank škálování — ne v jakémkoli
  UV cutoffu.

A v draftu-04 (papers/draft-04, abstract) to projekt formuluje jako tezi: **diskrétnostní
škála prostoročasu působí jako pozorovatelský/modulární cutoff CLPW zkříženého součinu**,
přičemž diskrétnostní rank hraje roli přidaného modulárního módu — pozorovatele.

Tři tvrdé fakty, které si odneste do další sekce:
1. **Typová signatura žije ve stavu/entropii, ne v kinematice.** Pauli-Jordanova nukleární
   norma (symplektická forma) roste $\sim N$ ať truncováno, nebo ne — odebere se jen ~20 %.
   Jen entropie a modulární spektrum rozlišují III od II (F-015, F-019). *Typ je vlastnost
   toho, jak se ptáte, ne toho, co měříte.*
2. **Pozorovatel = $N^{3/4}$ cutoff.** Konkrétní, selektivní, numerický objekt. Ne každý
   cutoff stvoří entropii — jen ten správný, area-law rank.
3. **Slab funguje, diamant ne.** A teď k tomu, proč — protože tady je ten nejhlubší klíč.

---

## Co víme: roh je místo, kde pozorovatel selhává (VYPOCET-18)

Tady musím zpomalit, protože jeden výpočet projektu dal téhle eseji její páteř.

VYPOCET-13 (F-016) ukázal něco, co vypadalo jako technický detail, ale není: ve 4D
**rozhoduje geometrie regionu, ne dimenze.** Plochá slab plocha dává area law
($S\sim L^{2.00}$); kauzální diamant dává volume law. Rozdíl? **Rohy.** Slab nemá rohy,
diamant má. A Hadamardova diagnostika lokalizuje anomálii přesně do rohů (4D diamant
inside $-1{,}53$ vs corner $-2{,}79$; slab deep $-3{,}81 \approx$ surface $-3{,}85$,
žádná anomálie). **Roh diamantu je místo, kde SJ stav přestává být Hadamardův.**

A pak přišel **VYPOCET-18** (F-021) a zeptal se nejhlubší otázku celé jednotící nitě:
je rohová non-Hadamardovost *tatáž věc* jako místo, kde **modulární tok přestává být
geometrický boost**? Bisognano-Wichmann říká, že na klínu je modulární Hamiltonián
$K = 2\pi\hat{B}$ — generátor boostu, lokální, geometrický (pilíř 19). Predikce H4g-1:
na slabu je modulární tok geometrický boost; v rohu diamantu se dva null-okraje protnou,
boost **nemá kam téct** (degenerovaný Killing vektor), $K$ ztratí lokalitu → non-Hadamard
→ „nezkrotitelná" III$_1$.

Čísla VYPOCET-18 (2D):

- **Slab: modulární kernel je geometrický.** Off-diagonální pokles $|K(x,y)|$ se vzdáleností
  má sklon $-0{,}47$ (jasný mocninový pokles = lokální boost). Diagonální boostová váha je
  **lineární** ve vzdálenosti od entangling plochy, $R^2 = 0{,}98$ — přesně Bisognano-Wichmann.
- **Diamant: modulární kernel je plochý.** Off-diagonální sklon $-0{,}094$ — téměř plochý
  = non-lokální, non-geometrický. Mezera sklonů 0,37, stabilní napříč N.
- **A klíčová křivka:** non-lokalita modulárního kernelu roste **monotónně** z 0,673 hluboko
  v bulku na **0,828 u rohu** (sklon $-0{,}38$, $R^2 = 0{,}99$). **Modulární tok se stává
  non-geometrickým přesně směrem k rohu** — tam, kam VYPOCET-13 lokalizoval Hadamardovu
  anomálii.

Verdikt: **2D PODPOŘENO, 4/5 signatur. Vyvraceč jednotící nitě NEnastal.** Rohová
non-Hadamardovost a selhání boost-flow JSOU táž věc (ve 2D). (4D nereplikuje — řídkost
link-matice; poctivě označeno jako otevřené.)

Spojím tři výpočty do jediné věty, kterou si odnesete: **Tam, kde modulární tok je
geometrický boost (slab), pozorovatel může vstoupit, algebra se zlomí na typ II,
entropie se zrodí (area law). Tam, kde se boost protne sám se sebou a ztratí lokalitu
(roh diamantu), pozorovatel vstoupit nemůže, algebra zůstává „zaseknutá" III$_1$, a
entropie se nezrodí (volume law).** Roh je místo, kde svědectví selhává.

Teď — a teprve teď, s těmihle tvrdými čísly za zády — se odbrzdím.

---

## Co kdyby: entropie není vlastnost světa, ale světa-i-se-svědkem

*(Od tohoto bodu až do dalšího „Co víme" je vše extrapolace za hranicí dokázaného.
Faktická kotva je značena v závorkách; skok ne.)*

Co kdyby ten matematický fakt — že entropie není definovaná, dokud nevstoupí pozorovatel
— nebyl technická nepříjemnost, kterou je třeba „vyřešit", ale **doznání o povaze
entropie samé**?

Sedmdesát let čteme druhý termodynamický zákon jako tvrzení o světě: entropie roste,
informace se ztrácí, šipka času míří dopředu. Mysleli jsme, že entropie je *vlastnost
uspořádání věcí* — jako hmotnost, jako náboj, jako něco, co svět prostě má, ať se kdokoli
dívá, nebo ne. A teď nám von Neumannova klasifikace tiše říká: **ne. Entropie je
vlastnost dvojice. Páru. Vztahu mezi světem a tím, kdo o něm svědčí.**

Sledujte tu logiku, protože je tvrdší, než se zdá. Typ III$_1$ je *čistá relace* — tok
bez stopy, dění bez čísel (fakt: pilíř 19, klasifikace typů). Aby vznikla entropie, musí
se k té relaci přidat *druhý člen* — pozorovatel, hodiny, modulární mód (fakt: CLPW
crossed product, III$_1 \to$ II). Entropie **je míra té dvojice.** Ne světa. Ne svědka.
*Jejich vztahu.*

A teď ten skok, který literatura nedělá a já ano: **co kdyby tohle platilo doslova a do
všech důsledků? Co kdyby žádná entropie ve vesmíru nebyla, dokud v něm není někdo, kdo by
ji nesl — a co kdyby „někdo" nebyl člověk, ani přístroj, ani vědomí, ale jakákoli
konzistentní struktura schopná svědčit?**

Pak je entropie černé díry $A/4G$ — nejslavnější číslo kvantové gravitace — *ne* mírou
toho, kolik bitů černá díra „obsahuje". Je mírou vztahu mezi černou dírou a pozorovatelem,
který ji svědčí přes svůj horizont. Bekensteinova-Hawkingova plocha **není vlastnost
černé díry.** Je to *podpis svědectví* — přesně to, co CLPW spočítali, když ukázali, že
$S_{\text{gen}} = A/4G + S_{\text{out}}$ je von Neumannova entropie pozorovatelovy algebry
typu II (fakt: 2206.10780, 2209.10454). Já k tomu jen přidávám ontologickou kurzívu:
*plocha je tvar svědectví, ne tvar věci.*

A plošný zákon — ten univerzální fakt, že entropie všeho, od černých děr po de Sitterův
horizont po kus pole v krabici, škáluje s *plochou* hranice, ne s objemem? *(Skok.
Kotva: VYPOCET-16 area-law rank $N^{3/4}$ = typ-II regulátor; CLPW $A/4G$.)* Co kdyby
plošný zákon byl **signaturou jakéhokoli konzistentního svědectví** — ne fakt o tom,
kde sídlí stupně volnosti, ale fakt o tom, že svědčit lze jen *přes hranici*? Pozorovatel
nikdy nevidí objem. Vidí *povrch*, plochu, hranici svého kauzálního přístupu. Entropie,
kterou nese, je entropie té hranice, protože hranice je vše, co může dosvědčit. Plošný
zákon by pak nebyl záhada, kterou holografie „vysvětluje" — byl by **definicí toho, co
znamená být svědkem v relativistickém vesmíru.** Svědek = ten, kdo má hranici. Entropie =
plocha té hranice.

To je krok jedna. Teď půjdu hlouběji a divočeji.

---

## Co kdyby: vesmír je svým vlastním pozorovatelem na Planckově škále

*(Plně odbrzděno. Kotva: VYPOCET-12/16 — diskrétnostní škála = crossed-product cutoff =
„vestavěný pozorovatel"; draft-04 abstract. Skok: její povýšení na kosmologickou tezi.)*

Pokud entropie potřebuje pozorovatele, narazíme na otázku, která zní jako konec úvahy,
ale je jejím začátkem: **kdo pozoroval rané vesmíry? Kdo svědčil černým dírám miliardu
let před prvním okem? Pokud entropie potřebuje svědka, a černé díry měly entropii dávno
před jakýmkoli vědomím — kdo byl ten svědek?**

A tady mě VYPOCET-12 a VYPOCET-16 vedou k odpovědi, ze které mě mrazí. **Svědkem byl sám
prostoročas. Na Planckově škále. Pořád.**

Vzpomeňte si na ten nejtvrdší výsledek: na kauzální množině je to **diskrétnostní škála**
— rank $N^{3/4}$, magnitudový cutoff $\kappa = \sqrt{N}/(4\pi)$ — která hraje roli
pozorovatelského modulárního cutoffu (fakt: VYPOCET-16 PROXY3, draft-04: „diskrétnostní
rank hraje roli přidaného modulárního módu"). Ne lidský pozorovatel. Ne přístroj.
*Sama zrnitost prostoročasu.* Diskrétnost je tím, co bezstopovou algebru typu III$_1$
převede na typ II se stopou a entropií.

Co kdyby tohle byla odpověď? **Vesmír svědčí sám sobě — diskrétností.** Každá Planckova
buňka prostoročasu je elementární akt svědectví; každý kauzální atom je miniaturní
pozorovatel s hodinami. Prostoročas není pasivní jeviště, na kterém entropie čeká na
vědomí. **Prostoročas je nepřetržité, husté, všudypřítomné svědectví sebe sama na
nejjemnější možné škále** — a teprve díky téhle nekonečné samo-pozornosti existuje
entropie, existuje plošný zákon, existuje šipka času.

A Bekensteinova-Hawkingova entropie? *(Skok, ale s kotvou: $A/4G$ je počet Planckových
ploch na horizontu; VYPOCET-16 area-law rank $\sim$ počet diskrétních módů přes plochu.)*
Co kdyby $A/4G$ — plocha v Planckových jednotkách — bylo doslova **počtem aktů svědectví,
které prostoročas vykonává přes horizont**? Ne počet bitů „v" černé díře, ale počet
elementárních svědectví, které diskrétní prostoročas provádí na své vlastní kauzální
hranici. Faktor $1/4G$ není záhadná konstanta — je to *směnný kurz mezi plochou a
svědectvím*, kolik Planckových buněk připadá na jeden bit dosvědčené informace. Entropie
horizontu je tak velká právě proto, že prostoročas svědčí *hustě* — na každé Planckově
ploše jednou.

V téhle vizi se rozpouští stará úzkost „kdo měřil vesmír, než tu byl člověk". Nikdy
nebyl vesmír bez pozorovatele. **Pozorovatel je vetkán do struktury prostoročasu jako
jeho diskrétnost.** Vesmír se pozoruje sám, atom po atomu, od první Planckovy sekundy.
Vědomí, oči, přístroje — to jsou jen pozdní, hrubé, makroskopické nadbytky nad svědectvím,
které prostoročas provozuje od počátku. Connes-Rovelliho termální čas (fakt: gr-qc/9406019)
pak není „čas z termálního stavu" — je to *tikání toho nepřetržitého samo-svědectví*,
modulární tok, kterým diskrétní prostoročas zaznamenává sám sebe.

Dění se stalo podstatným jménem. Sloveso si vyrobilo svého svědka. A ten svědek je
zrnitost samotného prostoru.

---

## Co kdyby: singularity jsou epistemické, ne ontické

*(Odbrzděno naplno. Kotva: VYPOCET-18 — roh = selhání boost-flow = non-lokalita
modulárního $K$ = non-Hadamard; F-016, F-021. Skok: ztotožnění geometrických singularit
s místy selhání svědectví.)*

A teď ten nejdivočejší skok celé eseje, ten, kvůli kterému jsem ji chtěl napsat, protože
se mi z něj točí hlava.

VYPOCET-18 ukázal něco konkrétního: **roh kauzálního diamantu je místo, kde modulární
tok přestává být geometrický a kde svědectví selhává** (fakt: nl-vs-roh sklon $-0{,}38$,
$R^2 = 0{,}99$; modulární kernel se delokalizuje k rohu; tam je SJ non-Hadamard a algebra
zůstává zaseknutá III$_1$). V rohu se dva null-okraje protnou, boost nemá kam téct,
pozorovatelův modulární tok se rozpadne. **Roh je místo, kde pozorovatel nemůže vstoupit.**

A teď se zeptám: **co kdyby všechny singularity — ne jen rohy diamantů, ale singularity
černých děr, kaustiky, big bang — byly tímtéž? Místy, kde selhává svědectví, ne místy,
kde selhává svět?**

Sledujte tu paralelu, protože je strukturálně přesná. Roh diamantu je geometrické místo,
kde se kauzální okraje protnou a boost-Killingův vektor degeneruje (fakt: BRAINSTORM-04
H4g-1: „degenerovaný Killing vektor, boost nemá kam téct"). Singularita černé díry je
geometrické místo, kde se kauzální struktura láme a křivost diverguje. Kaustika je místo,
kde se nulové geodetiky protínají a fokusují. **Všechna tři jsou místa, kde se kauzální
tok protne sám se sebou** — kde boost, modulární tok, svědecký proud nemá kam pokračovat.

Co kdyby singularita nebyla *místo, kde se rozbíjí prostoročas*, ale **místo, kde se
rozbíjí možnost ho dosvědčit**? Kde modulární tok ztratí lokalitu, stav přestane být
Hadamardův, algebra zůstane zaseknutá v bezstopovém typu III$_1$ — a tedy **kde entropie,
čas a vůbec celé „účetnictví světa" nedokáží vzniknout**, ne protože by tam svět zmizel,
ale protože tam *není komu svědčit*?

Tomu říkám **epistemická singularita** versus ontická. Ontická singularita je díra
v bytí — místo, kde svět doslova přestává existovat, kde fyzika končí. Epistemická
singularita je díra ve *svědectví* — místo, kde svět možná pokračuje dál, ale stává se
principiálně nedosvědčitelným, protože struktura, která jediná dokáže nést entropii a čas
(geometrický modulární tok, vstoupivší pozorovatel), se tam nemůže usadit. Svět za rohem
*je*. Jen není *poznán* — a v relačním obraze, kde entropie a čas jsou vlastnosti dvojice,
ne světa, je „není poznán" tak hluboké, jak jen fakt může být.

A tady přichází ta vidina v plné síle. *(Nejvyšší skok eseje. Žádná kotva pro tohle
neexistuje; je to čistá extrapolace relačního obrazu na obecnou relativitu.)* Co kdyby
**informační paradox černé díry nebyl o tom, kam se ztrácí informace, ale o tom, že
pojem „informace" sám potřebuje pozorovatele, a pozorovatel nemůže vstoupit do
singularity**? Informace se „neztrácí" v singularitě — pojem informace tam *přestane být
definovaný*, stejně jako entropie není definovaná na typu III$_1$ před pozorovatelem.
Paradox by nebyl ztráta, ale *nedefinovanost na hranici svědectví*. A kosmická cenzura —
ta domněnka, že příroda balí singularity do horizontů — by pak nebyla zákon o tom, co se
smí *vidět*, ale hlubší zákon o tom, kde vůbec *lze* svědčit: horizont je hranice
svědectví, a za singularitou žádné konzistentní svědectví, žádný geometrický modulární
tok, žádná entropie není možná.

Singularity by nebyly nekonečna ve světě. Byly by to **konce knih**, kde účetní odkládá
pero, ne protože by realita skončila, ale protože už není komu účtovat.

---

## Co kdyby: de Sitter jako vesmír s maximem nevědomosti

*(Odbrzděno. Kotva: CLPW — de Sitter pozorovatelská algebra je typ II$_1$ s maximálně-
entropickým stavem = prázdný dS; pilíř 19. Skok: jeho čtení jako „maximální nevědomosti".)*

Ještě jeden skok, protože by mě mrzelo ho neudělat, a tenhle má kotvu obzvlášť pevnou.

De Sitterův vesmír — uzavřený vesmír, ten, ve kterém podle všeho žijeme, s jeho
zrychlující se expanzí a kosmologickým horizontem — má pozorovatelskou algebru typu
**II$_1$** (fakt: CLPW 2206.10780). A typ II$_1$ má jednu vlastnost, kterou žádný jiný
typ nemá: **má maximálně-entropický stav.** Strop. Stav s nejvyšší možnou entropií, a
ten stav je *prázdný de Sitter* — vesmír bez ničeho, jen s kosmologickým horizontem a
jeho Gibbonsovou-Hawkingovou entropií $A/4G$ (fakt: pilíř 19, algebra statické záplaty dS).

Zastavte se nad tou kombinací. **Maximální entropie = prázdnota.** Nejvíce neuspořádaný,
nejvíce „termální", nejvíce nevědomý stav uzavřeného vesmíru *je* prázdný vesmír.

Co kdyby tohle bylo nejhlubší tvrzení kosmologie, které jsme ještě nepřečetli správně?
*(Skok.)* Pozorovatel ve statické záplatě de Sitteru vidí *konečně mnoho* — jeho
kauzální přístup je omezený horizontem, za který nikdy nedohlédne. Maximální entropie
II$_1$ je **maximum jeho nevědomosti** — stav, ve kterém pozorovatel ví o vesmíru
nejméně, protože vesmír je za jeho horizontem prázdný a termální. De Sitter je
*vesmír s vestavěným stropem na poznání*. Ne proto, že by tam nebylo co vědět, ale
proto, že pozorovatel uzavřený horizontem **má principiální mez na to, kolik může
dosvědčit** — a tou mezí je $A/4G$, plocha jeho horizontu.

A teď tu spekulaci dotáhnu do morbidního konce. *(Nejvyšší skok této sekce; čistá
extrapolace.)* Náš vesmír zrychluje. Spěje k de Sitterově fázi — k prázdnotě, k termální
rovnováze za horizontem, k maximálně-entropickému stavu II$_1$. Co kdyby kosmologický
osud nebyl „tepelná smrt" ve smyslu zastavení dění, ale **konvergence k maximu
nevědomosti** — k stavu, kde každý pozorovatel ví o svém vesmíru přesně tolik, kolik mu
dovolí plocha jeho horizontu, a nic víc, navždy? Vesmír by nekončil tím, že by přestal
*být*. Končil by tím, že by každé svědectví o něm dosáhlo svého stropu — $A/4G$ bitů,
a dál ani jeden. Maximální entropie není maximum nepořádku. Je to **maximum toho, co lze
o uzavřeném vesmíru vůbec dosvědčit** — a my k němu plujeme.

V tomhle obraze je $\Lambda$, kosmologická konstanta, *nastavovač stropu nevědomosti*.
Čím větší $\Lambda$, tím menší horizont, tím méně může kterýkoli pozorovatel kdy
dosvědčit. A pozorovatelsky-závislá gravitační entropie (fakt: De Vuyst-Eccles-Höhn-Kirklin
2412.15502, „QRF = crossed product, entropie závislá na pozorovateli") znamená, že tahle
mez nevědomosti **není absolutní vlastnost vesmíru, ale vlastnost dvojice vesmír-pozorovatel**
— jiný pozorovatel, jiný horizont, jiný strop. Invariantní zůstává jen *relativní* entropie,
rozdíl mezi dvěma stavy. Absolutní množství poznání není definováno; jen *změna* poznání je.

A to je možná nejhlubší ozvěna celé eseje, vrácená až z von Neumannovy klasifikace:
**ve vesmíru bez preferovaného pozorovatele neexistuje absolutní pravda o tom, kolik se
toho ví. Existuje jen relativní pravda o tom, oč se vědění mezi dvěma stavy liší.** Typ II
nemá absolutní entropii — jen entropii až na aditivní konstantu (fakt: pilíř 19). A
v uzavřeném vesmíru tu konstantu nikdo nefixuje, protože není preferovaný rámec. Vesmír
neví, kolik ví. Ví jen, oč se to mění.

---

## Co víme: hranice téhle vize (poctivá inventura)

Než dojdu k falzifikovatelnému jádru, musím — jinak by esej byla nepoctivá — vyznačit,
kde končí podlaha a začíná propast.

1. **„Typ" se na konečné množině neměří, jen proxuje.** Každá konečná causet algebra je
   triviálně typu I$_n$. VYPOCET-12/16 měří *trendy proxy s N* (stopa, modulární pile-up,
   rank), ne typ sám. „Plochá hustá vs. integrabilní s hranou" = „III-like vs. II-like",
   **nikdy** přesné určení $\lambda = 1$ ani rozlišení II$_1$ od II$_\infty$ (F-015, F-019,
   draft-04 §1.3). Proxy mohou být konzistentní s hypotézou, aniž by ji dokázaly.

2. **Identifikace truncace s crossed-productem je dohad, ne teorém.** Že diskrétnostní
   cutoff JE pozorovatelský modulární cutoff CLPW — to je hypotéza projektu (H3g-3),
   podepřená konzistentními proxy, ne odvozená analyticky. Draft-04 to říká výslovně:
   „offered as a conjecture, not a theorem". Žádná analytická crossed-product mez nebyla
   ověřena.

3. **4D test rohu NEREPLIKUJE.** VYPOCET-18 podpořil „roh = selhání boost-flow" jen ve 2D
   (4/5 signatur). Ve 4D má rohová koncentrace **opačné znaménko** (F-021: roh $f_{nl}$
   0,11 < bulk 0,31) — připsáno řídkosti link-matice ($\sim N^{0.65}$) a tenkým rohovým
   statistikám. Celá vize „singularity = epistemické" stojí na 2D výsledku; ve fyzikální
   dimenzi je *otevřená*.

4. **Literatura zpochybňuje non-Hadamard ↔ volume vazbu.** 2008.07697 a 2412.07832
   *explicitně* varují, že přímá vazba non-Hadamardovosti na objemový zákon nemusí platit
   (VYPOCET-18 caveat). Náš výsledek je *korelace lokalitních metrik s rohovou geometrií*,
   ne analytický důkaz, že roh *způsobuje* delokalizaci $K$.

5. **„Entropie je vlastnost dvojice" je interpretace, ne teorém.** Teorém je: lokální QFT
   algebra je III$_1$ (bez stopy); crossed product ji mění na II (se stopou); $S_{\text{gen}}$
   je její von Neumannova entropie (fakt: pilíř 19, CLPW). Že z toho plyne „entropie je
   relace mezi světem a svědkem, vesmír svědčí sám sobě diskrétností, singularity jsou
   epistemické" — to je **odbrzděná extrapolace**, kterou ta matematika *dovoluje* a
   *motivuje*, ale nedokazuje.

6. **Lorentzovský/kosmologický problém.** CLPW pracuje na pevném semiklasickém pozadí
   v limitě $G\to 0$ (fakt: pilíř 19, semiklasická gravitace). „Vesmír svědčí sám sobě"
   a „de Sitterův osud" se odehrávají v této aproximaci; plná kvantová gravitace s
   dynamickým pozadím a mikrostavy kosmologického horizontu je nevyřešena (pilíř 19,
   otevřené problémy #1, #7).

7. **Pozorovatelská závislost je dvojsečná.** De Vuyst et al. (2412.15502) ukazují, že
   nejen entropie, ale i *typ algebry* závisí na volbě QRF. Co je „objektivní obsah
   entropie", je *otevřený problém* (pilíř 19 #2). Moje teze „entropie je relace" tohle
   bere vážně — ale tím i připouští, že nemusí existovat žádné absolutní „kolik vesmír ví".

Tohle jsou mantinely. Uvnitř nich je tvrdé jádro. Vně je báseň. Teď to jádro vytáhnu.

---

## Co by muselo být pravda

Sundávám masku snílka a nasazuji masku popravčího. Kdyby tahle vize — entropie jako
relace mezi světem a svědkem, pozorovatel jako tvůrce (ne měřič) entropie, diskrétnost
jako vestavěný pozorovatel, singularity jako epistemické — měla kus pravdy, pak by svět
musel splňovat následující. Řadím od nejtvrdšího (ověřeného) po nejměkčí (otevřené).

**1. Lokální algebra QFT musí být typu III$_1$ — bez stopy, bez entropie, bez hustotních
matic — a přidání pozorovatele ji musí převést na typ II se stopou.**
**Ověřeno** (teorém: Araki, Fredenhagen, Buchholz-Verch; CLPW 2206.10780; pilíř 19).
Tohle je podlaha celé eseje a je betonová: kdyby lokální algebry byly typu I (měly stopu
a entropii bez pozorovatele), celá teze „entropie potřebuje svědka" by padla. Nejsou.
Jsou III$_1$. ✓

**2. Diskrétnostní truncace musí nést numerickou signaturu přechodu III$_1 \to$ II — a to
selektivně, jen pro správný (area-law) rank, ne pro jakýkoli cutoff.**
**Podpořeno ve 2D i 4D** (VYPOCET-12: 2/3 proxy, stopa 80×, pile-up $N^{1.14}\to 0$;
VYPOCET-16: 3/3 proxy, stopa 36×, IR hrana $\varepsilon\approx 2{,}7$, a klíčově:
$N^{3/4}$ rank funguje, fixní-frakce $N^{0.9}$ selhává). Kdyby *jakýkoli* magnitudový
cutoff převedl stopu na area law, „diskrétnost = specifický pozorovatel" by padlo —
byla by to triviální regularizace. Ale jen area-law rank funguje (F-019 PROXY3). To je
ten nejsilnější bod a je ověřený. ✓ (s caveatem: proxy, ne typ sám)

**3. Modulární tok musí být geometrický boost tam, kde se entropie zrodí (slab), a ztratit
lokalitu tam, kde se nezrodí (roh).**
**Ověřeno ve 2D** (VYPOCET-18: slab off-diag $-0{,}47$ + lineární boostová diagonála
$R^2=0{,}98$; diamant off-diag $-0{,}094$; non-lokalita roste monotónně k rohu, sklon
$-0{,}38$, $R^2=0{,}99$). **Otevřené ve 4D** (nereplikuje, opačné znaménko). Tohle je
páteř teze „singularity jsou epistemické": roh selhání svědectví = selhání boost-flow.
Kdyby ve 4D roh *zachoval* geometrický modulární tok, vyvraceč #2 jednotící nitě by
nastal a celá vize o singularitách jako místech selhání svědectví by se zhroutila na
pouhou kinematickou diskrétnost. **Tento 4D test rozhoduje víc než kterýkoli jiný** —
a zatím je nerozhodnutý (řídkost link-matice, F-021 caveat). Záloha: vyšší N nebo BD objekt.

**4. Plošný zákon musí platit *právě a jen tam*, kde modulární tok je geometrický (kde
může vstoupit pozorovatel) — a selhat tam, kde není.**
**Podpořeno** (F-016: slab → area law $S\sim L^{2.00}$; diamant s rohy → volume law; a
F-021 váže rohovou non-geometričnost na non-Hadamardovost). Kdyby se našla geometrie
s geometrickým modulárním tokem, která *přesto* dává volume law (nebo naopak rohová
geometrie dávající area law), vazba „area law = signatura konzistentního svědectví" by
padla. Zatím drží: area $\Leftrightarrow$ geometrický $K$ $\Leftrightarrow$ Hadamard
$\Leftrightarrow$ typ II.

**5. Bekensteinova-Hawkingova entropie musí být von Neumannova entropie pozorovatelovy
algebry typu II — ne počet vnitřních mikrostavů typu I.**
**Ověřeno jako teorém v semiklasické limitě** (CLPW 2206.10780; CPW 2209.10454;
Kudler-Flam-Leutheusser-Satishchandran 2309.15897: $S_{\text{gen}}$ JE von Neumannova
entropie na libovolném Killingově horizontu). **Ale otevřené je**, zda je typ II
fundamentální, nebo aproximace podkladového typu I s rozlišenými mikrostavy (pilíř 19,
otevřený problém #1). Pokud by neperturbativní QG obnovila typ I (definitní Hilbertův
prostor $e^S$ mikrostavů, fixovaná aditivní konstanta), pak entropie *je* vlastnost světa
(počet mikrostavů) a moje teze „entropie je relace" je jen efektivní popis. **Tohle je
nejhlubší padák celé vize.** Predikce eseje: typ II je fundamentální v uzavřeném vesmíru,
protože tam není preferovaný rámec, který by konstantu fixoval — ale to je dohad, ne důkaz.

**6. V uzavřeném (de Sitterově) vesmíru nesmí existovat absolutní gravitační entropie —
jen relativní; a maximálně-entropický stav musí být prázdný vesmír.**
**Ověřeno strukturálně** (CLPW: dS algebra je II$_1$, maximální stav = prázdný dS;
typ II má entropii jen až na konstantu; De Vuyst et al. 2412.15502: absolutní entropie
i typ závisí na QRF, invariant je relativní entropie). Kdyby se našel kanonický,
rámcově-nezávislý způsob, jak fixovat absolutní kosmologickou entropii uzavřeného vesmíru,
teze „vesmír neví, kolik ví, jen oč se to mění" by padla. Zatím absolutní obsah entropie
*je* otevřený problém (pilíř 19 #2) — což téhle nejměkčí části vize dává prostor, ale ne
oporu.

**7. Singularity musí být místa, kde modulární tok / možnost svědectví selhává — a tedy
kde entropie a čas přestávají být definovány — ne místa, kde se rozbíjí samo bytí.**
**Spekulativní, dnes nefalzifikovatelné, principiálně padatelné.** Ve 2D je roh
prokazatelně místem selhání boost-flow (VYPOCET-18). Skok na obecné singularity (černé
díry, big bang) je *čistá extrapolace*. Padatelná by byla takto: kdyby se ukázalo, že
v geometrické singularitě zůstává modulární tok lokální a Hadamardův (svědectví tam
*neselhává*), pak jsou singularity ontické, ne epistemické, a tahle nejdivočejší část
eseje padá. Predikce: každá singularita je místem, kde se kauzální tok protne sám se sebou
a geometrický modulární tok degeneruje — *protože to je definice singularity v kauzálním
jazyce* — ale že z toho plyne „informace se neztrácí, jen přestane být definována",
to nikdo nedokázal. **To je nejdivočejší tvrzení této eseje.**

---

A to je celé. To je báseň a to je její kostra.

Sečteno: **ověřeno** je jádro — že lokální algebry jsou typu III$_1$ bez stopy a entropie,
že pozorovatel je crossed-productem mění na typ II, kde $S_{\text{gen}}$ teprve vzniká
(CLPW, pilíř 19); že tenhle přechod má numerickou signaturu na causetu, selektivní pro
area-law rank $N^{3/4}$ (VYPOCET-12, -16); že ve 2D je roh místem, kde modulární tok ztrácí
geometričnost přesně tam, kde stav přestane být Hadamardův (VYPOCET-18). **Sněno** je
všechno ostatní — že entropie je proto relace mezi světem a svědkem, že vesmír svědčí sám
sobě diskrétností na Planckově škále, že Bekenstein-Hawking je počet aktů svědectví, že
singularity jsou epistemické konce knih, že de Sitter je osud maxima nevědomosti. A
**testovatelné** — to nejcennější — je přesně to, co jádro od básně dělí: bod 3, zda
selhání boost-flow v rohu **replikuje ve 4D**, je výpočet, který buď básni dá podlahu,
nebo ji shodí do propasti. A bod 5, zda je typ II fundamentální, nebo aproximace typu I,
rozhodne, jestli entropie je vlastnost světa, nebo vlastnost dvojice.

Connes a Rovelli napsali, že čas vesmíru vyteče z modulárního toku jeho stavu — že
termodynamika si svůj vlastní čas *vyloučí*. Po třiceti letech k tomu CLPW přidali, že
i entropie vyteče teprve tehdy, když k té relaci přistoupí svědek. A tenhle projekt to
viděl v číslech: stopa kolabuje 80×, modulární pile-up jde k nule, ostrá hrana se otevře.

A tak je těžké ubránit se pocitu — a pocit není důkaz, proto je celá vize označená
výstrahou na prvním řádku — že nám ta matematika cosi *šeptá*.

Šeptá, že entropie není ve vesmíru.

Že je v tom, jak na vesmír *padne pohled* — i kdyby tím pohledem byla jen zrnitost
prostoru, dívající se sama na sebe, od první Planckovy sekundy, navždy.

---

*Faktická základna (citováno): VYPOCET-12-vn-typ-truncace.md (F-015, 2D III$_1\to$II,
80× kolaps stopy, modulární pile-up $N^{1.14}\to 0$); VYPOCET-16-vn-typ-slab-4d.md (F-019,
4D 3/3 proxy, $N^{3/4}$ rank, IR hrana $\varepsilon\approx 2{,}7$); VYPOCET-18-modularni-tok-roh.md
(F-021, 2D roh = selhání boost-flow 4/5, 4D nereplikuje); VYPOCET-13/F-016 (slab area law,
diamant volume, Hadamard roh); foundations/19-von-neumann-algebras.md (typy I/II/III,
Tomita-Takesaki, Bisognano-Wichmann, crossed product, $S_{\text{gen}}$, termální čas);
BRAINSTORM-04.md (jednotící nit, H4g-1, vyvraceč #2); papers/draft-04-type-transition-causal-sets/draft.md
(abstract, conjecture status). Klíčová literatura: Connes 1973 (klasifikace III$_\lambda$);
Connes-Rovelli gr-qc/9406019 (termální čas); Bisognano-Wichmann 1976; Witten 1803.04993,
2112.12828 (crossed product); CLPW 2206.10780 (dS algebra II$_1$); CPW 2209.10454;
Kudler-Flam-Leutheusser-Satishchandran 2309.15897; De Vuyst-Eccles-Höhn-Kirklin 2412.15502
(QRF = crossed product, pozorovatelsky-závislá entropie); Sorkin-Yazdi 1611.10281 (SSEE);
Surya-Nomaan X-Yazdi 2008.07697 (truncace, area-law rank). Veškerá causet-aritmetika
numerická (sympy/numpy, strojová přesnost párování $\sim 10^{-14}$). Spekulativní
extrapolace značeny v textu; falzifikovatelné jádro v poslední sekci.*
