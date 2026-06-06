# H01 — Immirziho parametr z Cardyho logaritmické korekce

**Datum:** 2026-06-06  
**Stav:** Pracovní dossier (ekonomický mód — cílené čtení)  
**Navazuje na:** verification/novelty/cardy-lqg.md  
**Verdikt novosti:** jádro known (Carlip 1410.5763 + Ghosh-Pranzetti 1405.7056); nepokryté residuum viz §2

---

## §1 — Přehled publikovaných log-korekcí entropie ČD napříč přístupy

### 1.1 LQG — U(1) formalismus (Rovelli, Krasnov, Barbero-Immirzi)

Standardní LQG počítání s U(1) gauge symetrií horizontu (izolovaný horizont jako hranice U(1) Chern-Simons teorie) dává:

```
S = (γ₀/γ) · A/(4l_P²)  −  (1/2) ln(A/l_P²)  +  O(1)
```

kde γ₀ ≈ 0.274 je hodnota fixovaná podmínkou S = A/4. Koeficient log korekce je **−1/2**. Tato hodnota pochází z počítání stran spin-sítí s j_min = 1/2; převládající příspěvky jsou od punctures s j = 1/2.

- Zdroj: Meissner (2004), Ghosh a spol.; shrnutí v arXiv:1201.6102.

### 1.2 LQG — SU(2) formalismus (Kaul-Majumdar, Engle-Noui-Perez)

Kaul a Majumdar (2000, Phys. Rev. Lett. 84, 5255) jako první upozornili, že správná gauge symetrie izolovaného horizontu je SU(2), nikoli U(1). Přepočítání dimenzí SU(2) CS Hilbertova prostoru dává:

```
S = A/(4l_P²)  −  (3/2) ln(A/l_P²)  +  O(1)
```

Koeficient log korekce je **−3/2**. Výsledek je pro γ = γ₀(SU(2)) a přesnost je asymptotická v limitě k → ∞ (kde k = A/(4πγl_P²) je CS level). Pro konečné k přísné škálování S ∝ A bez log korekce (viz §1.7).

- Zdroje: Kaul-Majumdar (2000); Engle-Noui-Perez arXiv:0905.3168, 1006.0634; Majumdar přednáška Edinburgh (2011).

### 1.3 String theory / Cardy — BTZ a D1-D5 systém

V 2+1 dimenzionální gravitaci (BTZ ČD) Strominger (1997) ukázal, že Brown-Henneaux centrální náboj c = 3l/(2G) a Cardyho formule

```
S_Cardy = 2π√(cL₀/6)
```

reprodukují Bekenstein-Hawkingovu entropii. Logaritmická korekce z rozšíření Cardyho formule (Carlip gr-qc/0005017):

```
S = S_BH  −  (3/2) ln S_BH  +  ln c  +  const
```

Koeficient **−3/2** pochází z hustoty stavů CFT: ρ(E) ~ E^{−3/4} exp(2π√(cE/6)), logaritmický člen je −(3/4)·2 = −3/2 z prefaktoru. Pro D1-D5 systém c = 6Q₁Q₅ (celkový centrální náboj N₁N₅ kopií c=6 volné SCFT na T⁴), Cardyho formule reprodukuje Strominger-Vafa entropii přesně.

- Zdroje: Carlip gr-qc/0005017; Strominger-Vafa (1996); Brown-Henneaux (1986); arXiv:hep-th/9812013.

### 1.4 Sen — Eukleidovská gravitace, IR-universalita (klíčová křížová reference)

**Sen, arXiv:1205.0971** (JHEP 2013) je metodologicky klíčový papír pro celou debatu. Sen počítá log korekce k entropii ne-extremálních ČD metodou Eukleidovské gravitace (one-loop efektivní akce). Hlavní tvrzení:

> *Logaritmické korekce k entropii ČD jsou určeny výhradně z IR (nízkoenergetických) dat — spektra bezhmotných polí a jejich interakcí. Nejsou závislé na UV detailech teorie.*

Pro Schwarzschildovo ČD v 4D Sen dostává koeficient **−2** (přesněji −2 ln M nebo ekvivalentně určitý koeficient ln A po přepočtu proměnných), zatímco LQG předpovídá −1/2 (U(1)) nebo −3/2 (SU(2)). Tato neshoda je explicitně uvedena v abstraktu 1205.0971:

> *"For Schwarzschild black holes in four space-time dimensions the macroscopic result seems to disagree with the existing result in loop quantum gravity."*

**Klíčový důsledek universality:** Pokud jsou log korekce čistě IR, pak musí souhlasit ve VŠECH UV-úplných teoriích gravitace — LQG, string theory, AS — pokud ty popisují stejnou IR fyziku. Neshoda LQG s Senovou předpovědí je tedy buď (a) chyba v LQG počítání, nebo (b) LQG a standardní QFT gravitace mají odlišné IR limity.

- Zdroje: Sen 1205.0971; PhysicsForum diskuse o dopadu na LQG (2013); arXiv:1108.3842 (extremální případ, N=2 SUSY, perfektní shoda string/semi-klasika).

### 1.5 Asymptotická bezpečnost (AS)

V AS (Bonanno-Reuter) renormalizační skupina mění G(r) podél horizontu. Log korekce entropie jsou přítomny ve tvaru S = A/4 + C ln(A), kde znaménko C závisí na tom, zda dominují gravitační nebo hmotové fluktuace. AS log korekce jsou proto **modelově závislé** v rámci AS (závislost na trajektorii RG toku) a nesdílí universalitu Senova IR výsledku.

- Zdroje: arXiv:2204.11616; diskuse v arXiv:2004.06810 (kritické ohlédnutí za AS).

### 1.6 Semiclasika — Wald entropie a Euclidean path integral

Při zahrnutí vyšších derivativových oprav (R² atd.) Waldova entropie dává opravy, ale ty jsou polynom v zakřivení, nikoliv log A. Čistě semiclasické log korekce pocházejí z 1-loop determinantů (Senův výpočet); ty jsou IR-universální jak popsáno v §1.4.

### 1.7 Speciální případ: absence log korekce v LQG pro konečné k

Ghosh a spol. (arXiv:1206.3411) ukázali, že pro konečné CS level k (fixované, nikoliv rostoucí s A) entropie SU(2) LQG je přísně S = A/(4l_P²) bez log korekce. Implication: log korekce v LQG jsou artefaktem limity k → ∞ a pro fyzikální fixaci γ = γ₀ záleží na přesném provedení limity.

### 1.8 Přehledná tabulka koeficientů

| Přístup | Koeficient log A | Podmínka |
|---------|-----------------|----------|
| LQG U(1), Meissner 2004 | **−1/2** | k → ∞, γ = γ₀ ≈ 0.274 |
| LQG SU(2), Kaul-Majumdar 2000 | **−3/2** | k → ∞, SU(2) CS counting |
| LQG SU(2), konečné k | **0** (žádná) | k = A/(4πγl_P²), fixní γ |
| LQG, γ = i (komplexní, Frodden et al.) | nespecifikována* | γ → ±i, BH→ exp(A/4) |
| Cardy/BTZ/CFT (Brown-Henneaux) | **−3/2** | c ≫ 1 limit Cardy |
| Cardy/string D1-D5 | **−3/2** | c = 6Q₁Q₅ |
| Sen (Eukleidovská gravitace, 4D Schwarz.) | **≠ −1/2, ≠ −3/2** (~−2) | IR, bezhmotná pole, 1-loop |
| AS (Bonanno-Reuter) | **±C** (závisí) | model-specific |
| Semiclasika 1-loop (obecná) | **−(N_s−N_f+N_v−...)/12** | závisí na spektru |

*Pro γ = i logaritmická korekce nebyla explicitně spočtena v nalezené literatuře.

---

## §2 — Přesná formulace zbývajícího tvrzení a co přesně spočítat

### 2.1 Nepokrytý prvek (residuum)

Z novelty checku zbývají **dvě konkrétní tvrzení** bez explicitního publikovaného výpočtu:

**Tvrzení A (analogie):** Immirziho parametr γ je LQG analogií c = 6Q₁Q₅ ze stringové teorie — tj. γ hraje roli *normalizátoru centrálního náboje* v efektivní CFT horizontu, analogicky jako Q₁Q₅ v D1-D5 systému.

**Tvrzení B (predikce):** Shoda LQG log korekce (−1/2 z U(1) nebo −3/2 z SU(2)) s universálním Cardyho log členem (−3/2 ln c) *jednoznačně fixuje reálné γ* bez nutnosti pheno-fenomenologické kalibrace na BH entropii (tj. bez explicitní podmínky S_LQG = S_BH).

### 2.2 Přesná matematická formulace Tvrzení B

Mějme SU(2) CS popis LQG horizontu s levelem k = A_H/(4πγl_P²). Carlip (1410.5763) ukázal c_eff = 6k. Cardyho formule pak dává:

```
S_Cardy = 2π√(c_eff · L₀/6)  s log korekcí  −(3/2) ln c_eff
```

Přitom c_eff = 6k = 6A_H/(4πγl_P²) = (3/2πγ) · (A_H/l_P²).

Log korekce z Cardy:

```
δS_Cardy = −(3/2) ln c_eff = −(3/2) ln[(3/2πγ) · A_H/l_P²]
          = −(3/2) ln(A_H/l_P²)  −  (3/2) ln(3/2πγ)
```

LQG SU(2) výpočet dává (Kaul-Majumdar):

```
δS_LQG = −(3/2) ln(A_H/l_P²)  +  C_KM(γ)
```

kde C_KM(γ) je O(1) konstanta závislá na γ z detailů CS počítání.

**Podmínka shody** (log člen i konstanta):

```
−(3/2) ln(3/2πγ) = C_KM(γ)
```

Tato rovnice by fixovala γ bez potřeby porovnání hlavního členu A/4.

**Kroky výpočtu:**

1. Z Engle-Noui-Perez (1006.0634) extrakt přesné hodnoty C_KM(γ) — tj. konstantního členu v log-expansi pro velká k.
2. Vyjádřit C_KM jako funkci γ (závisí přes k = A/(4πγl_P²) na způsobu normalizace).
3. Porovnat s −(3/2) ln(3/2πγ) z Carlipova c_eff.
4. Vyřešit rovnici pro γ; zkontrolovat, zda řešení odpovídá γ₀ ≈ 0.274.

### 2.3 Tvrzení A — co spočítat

D1-D5 systém: c = 6·N₁·N₅. Carlip LQG: c_eff = 6k = 6·A_H/(4πγl_P²). Identifikace:

```
N₁ · N₅  ↔  A_H/(4πγl_P²) = k
```

Pro fyzikální ČD s A_H = 16πM²G², dostaneme k = 4MG/γl_P². Stringová analogie tedy říká: „počet D-brane stavů" N₁N₅ odpovídá CS level k, s γ jako volný parametr analogický stringovému výběru charge product Q₁Q₅. Toto tvrzení je **kvalitativní** a nevede k unikátní předpovědi bez dalšího vstupu — k výpočtu nestačí.

---

## §3 — Rizika: Senova universalita může tvrzení zabít

### 3.1 Hlavní riziko: IR-universalita log korekcí

**Senovo hlavní tvrzení** (1205.0971) je, že logaritmické korekce k entropii ČD jsou *universální ve smyslu IR* — jsou určeny jednoloop efektivní akcí nízkoenergetických bezhmotných polí (graviton, foton, dilaton, ...) a *nejsou citlivé na UV fyziku* (na typ a parametry UV teorie).

**Přímý dopad na Tvrzení B:**

Pokud log korekce jsou čistě IR, pak:
- Nemohou záviset na γ (UV parametr LQG).
- Nemohou tedy γ fixovat.
- Koeficient log korekce je *deterministicky* dán počtem a spinem bezhmotných polí; pro čistou 4D Einsteinovu gravitaci (graviton j=2 a možná gravitino) Sen dostává specifické číslo, které se liší od −3/2.

**Toto je klíčová námitka:** Pokud γ je UV parametr (jako délkové kvantum), log korekce, které jsou IR-universální, ho jednoduše fixovat nemohou. Shoda numerická by mohla existovat, ale byla by náhodná, nikoli principiální.

### 3.2 Protiargument LQG komunity (Ghosh-Perez)

Ghosh a Perez tvrdí, že *origin* log korekce v LQG je odlišný od Senovy: v LQG jde o entanglement entropy a počítání CS mikrostavu, zatímco Sen počítá 1-loop gravitační determinanty. Tyto jsou různé fyzikální mechanismy a není důvod, aby dávaly identické číslo.

Tím Ghosh-Perez *odmítají*, že neshoda LQG vs. Sen je problém — ale zároveň tím **podrývají** Tvrzení B, protože pokud mechanismy jsou různé, pak shoda log-koeficientů není principiálně odůvodněna.

### 3.3 Problém komplexního γ

Frodden-Geiller-Noui-Perez (1212.4060) a Ghosh-Pranzetti (1405.7056) ukazují, že správná LQG reprodukce BH entropie *bez finetuning γ* vyžaduje γ = ±i (komplexní Ashtekarovy proměnné). Pro imaginární γ:

- CS level k = A/(4πγl_P²) je *imaginární* — CS teorie s imaginárním levelem je netriviální (WZW korelace, analytické pokračování).
- Carlipův c_eff = 6k je pak také imaginární nebo komplexní.
- Log korekce −(3/2) ln c_eff pro komplexní c nemá přímočarý reálný smysl.

Pokud se přijme γ = i jako "správná" hodnota LQG, Tvrzení B (fixace *reálného* γ) se stane bezpředmětným. 

### 3.4 Problém with U(1) vs. SU(2) — diskontinuita

U(1) LQG dává −1/2, SU(2) LQG dává −3/2, Sen dává ≈ −2. Cardyho formula dává −3/2. Takže:

- −3/2 (SU(2) LQG) = −3/2 (Cardy) — numerická shoda! Ale je to pouze shoda hlavního log-členu; O(1) konstanty se mohou lišit.
- Nicméně tato shoda (SU(2) LQG = Cardy) je *již* v literatuře implicitně přítomna (Carlip 1410.5763 ukazuje přímo Cardy z c_eff = 6k → −3/2 log-korekce).
- Tedy Tvrzení B musí jít za pouhé porovnání −3/2 = −3/2 a pracovat s konstantním členem (§2.2 krok 1-4).

### 3.5 Riziko tautologie

Carlip (1410.5763) již použil c_eff = 6k a Cardy formuli pro LQG entropii — čímž implicitně zabudoval shodu −3/2 log korekce. Pokud Tvrzení B pouze reprodukuje Carlipův výpočet z jiného úhlu, je tautologické. Non-trivialita Tvrzení B závisí na tom, zda fixace konstantního členu C_KM(γ) je skutečně nová podmínka — to vyžaduje explicitní výpočet (§2.2).

---

## §4 — Verdikt: stojí výpočet za to?

### 4.1 Stručný verdikt

**Podmíněně ano, ale s úzkým oknem.**

Výpočet stojí za to *pouze pokud* je cílem fixace konstantního členu O(1) v log-expansi entropie SU(2) LQG přes Carlipův c_eff. Toto je konkrétní, počitatelné, a není explicitně v literatuře.

**Výpočet nestojí za to**, pokud:
- Tvrzení je formulováno pouze jako koeficient −3/2 = −3/2 (to je triviálně Carlip+Kaul-Majumdar).
- Tvrzení je formulováno jako "γ lze fixovat z log-korekcí" bez ošetření Senovy IR-universality.
- Tvrzení je formulováno jako qualitativní analogie γ ↔ c = 6Q₁Q₅ bez kvantitativní predikce.

### 4.2 Skóre rizik

| Riziko | Závažnost | Ošetření |
|--------|-----------|----------|
| Senova IR-universalita zakazuje fixaci γ | **VYSOKÁ** | Nutno argumentovat, že γ vstupuje do IR přes horizonton kvantizaci |
| Carlip 1410.5763 je tautologický prior | **STŘEDNÍ** | Přejít na konstantní člen C_KM, ne jen koeficient |
| γ = i je správnější než reálné γ | **STŘEDNÍ** | Zaměřit se explicitně na reálný případ a jeho limity |
| Ghosh-Perez: různé mechanismy = různé log | **VYSOKÁ** | Toto je vážná námitka; musí být adresována |
| Výsledné γ nemusí odpovídat γ₀ ≈ 0.274 | **STŘEDNÍ** | Je to testovatelný výstup výpočtu |

### 4.3 Doporučený postup

**Minimální hodnotný výpočet (2–3 strany):**

1. Z Engle-Noui-Perez (1006.0634) extrahovat *přesný* konstantní člen log-expansi SU(2) CS entropie jako funkci γ.
2. Z Carlipova c_eff = 6k odvodit, jaký konstantní člen predikuje Cardyho formule.
3. Porovnat — pokud se rovnají pro γ = γ₀ ≈ 0.274, je to netriviální shoda (potenciálně publikovatelný krátký poznámkový papír).
4. Pokud nesouhlasí: clarify že −3/2 shoda je pouze koeficientová, ne úplná.

**Kritický test před začátkem:** Zkontrolovat, zda Carlip 1410.5763 sekce 5–6 již explicitně neprovádí tento porovnání včetně konstantního členu. Pokud ano: výpočet je known a publikace nemá smysl.

**Senova námitka:** Musí se argumentovat, proč log korekce z LQG mikrostavu-počítání jsou principiálně odlišné od Senových IR-korekci, nebo proč přesto musí souhlasit (možný argument: holografická dualita na horizontu). Bez tohoto argumentu je výpočet "zajímavý výsledek bez fyzikálního principu."

---

## §5 — Klíčové reference

| Papír | arXiv | Rok | Relevance |
|-------|-------|-----|-----------|
| Kaul-Majumdar, log correction SU(2) | Phys.Rev.Lett.84:5255 | 2000 | −3/2, origin |
| Carlip, log corrections from Cardy | gr-qc/0005017 | 2000 | −3/2 z Cardy, C string analogy |
| Carlip, BH entropy from CFT | hep-th/9812013 | 1998 | c = 3l/2G |
| Meissner, U(1) LQG log correction | gr-qc/0407052 | 2004 | −1/2 U(1) |
| Engle-Noui-Perez, SU(2) CS | 0905.3168 | 2009 | c_eff, SU(2) counting |
| Engle-Noui-Perez, Type I SU(2) | 1006.0634 | 2010 | přesné konstanty |
| Frodden-Geiller-Noui-Perez, complex γ | 1212.4060 | 2013 | γ = i, bez log detail |
| Ghosh-Pranzetti, CFT/gravity | 1405.7056 | 2014 | WZW na horizontu |
| Carlip, c=6k v LQG | 1410.5763 | 2014 | KLÍČOVÝ: c_eff = 6k |
| **Sen, non-extremal log corr.** | **1205.0971** | **2013** | **IR-universalita, LQG neshoda** |
| Sen, extremal N=2 log corr. | 1108.3842 | 2011 | IR-okno, dokonalá shoda string |
| Ghosh a spol., absence log corr. | 1206.3411 | 2012 | konečné k → 0 log |
| Pranzetti-Sahlmann | 1412.7435 | 2015 | 3D gravity na horizontu |

---

## Rozhodující čtení (2026-06-06)

*Přímé čtení tří klíčových prací. Cíl: rozhodnout, zda program srovnání konstantního členu (Tvrzení B z §2.2) je (a) již publikován, (b) provitelný a nový, nebo (c) strukturálně zabitý.*

---

### Q1: Je srovnání konstantního členu log-expanze již publikováno?

#### ENP: Engle-Noui-Perez, arXiv:1006.0634

Přímé čtení papíru (30 stran, plný PDF) prokázalo:

**Exaktní tvar entropie v ENP (1006.0634):**

> *"It turns out to be S_BH = β₀ · a_H / (4β l_p²), where β₀ = 0.274067... However, the subleading corrections turn out to have the form ΔS = −(3/2) log a_H (instead of the ΔS = −(1/2) log a_H that follows the classic treatment)"*

ENP tedy uvádí pouze koeficient logaritmického členu **−3/2**. **Konstantní člen O(1) ENP explicitně neuvádí.** Odkaz [31] (Engle-Noui-Perez-Pranzetti, "The SU(2) Black Hole entropy revisited", JHEP 2011, arXiv:1006.0634 companion paper) je označen jako zdroj přesného počítání; ENP (1006.0634) sám obsahuje pouze výsledek asymptotiky bez explicitní hodnoty konstantního členu.

**Závěr pro Q1a:** ENP **neprovádí** srovnání konstantního členu s Carlipovou/Cardyho predikcí. Konstantní člen O(1) není v papíru ani odvozen, ani porovnán.

#### Carlip, arXiv:1410.5763

Přímé čtení sekce 5 (kanonická Cardyho formule) a sekce 6 (mikrokanonická Cardyho formule):

**Sekce 5:** Carlip dosazuje c_eff = 6k a geometrickou teplotu T ≈ 1/2π, čímž dostane S = A_Δ/(8G) — *polovinu* Bekenstein-Hawkingovy entropie. Neprovádí rozvoj na log korekce s konstantním členem. Žádné porovnání s LQG konstantním členem.

**Sekce 6 (mikrokanonická):** Carlip dosadí konfirmní váhy ∆_j = −j(j−1)/(k−2) do mikrokanonické Cardyho formule (2.3) a dostane:

> S ≈ 2π Σ_punctures √(−j(j−1))

Toto odpovídá standardnímu LQG výrazu pro plochu horizontu, nikoliv log opravě. Sekce 6 **neobsahuje** rozvinutý log člen ani konstantní člen — výsledek je přímo hlavní člen entropie.

**Klíčový závěr Carlipa (sekce 7):** Carlip explicitně komentuje Immirziho parametr:

> *"Indeed, the strange standard value of the Barbero-Immirzi parameter can be traced to the properties of this combinatorial problem... [Cardy formula approach] leading to a simple dependence on the Barbero-Immirzi parameter."*

Carlip **neprovádí** srovnání O(1) konstantního členu Cardy vs. LQG a **nefixuje** γ z tohoto srovnání. Implicitně naznačuje, že γ-závislost vstupuje přes Cardyho formuli, ale nevyřeší rovnici (viz §2.2 tohoto dossier).

**Závěr pro Q1:** Srovnání konstantního členu O(1) v log-expansi SU(2) LQG entropie s Carlipovou/Cardyho predikcí **nebylo publikováno** ani v ENP 1006.0634, ani v Carlip 1410.5763. Tvrzení B z §2.2 je v tomto smyslu **nové** — výpočet nebyl proveden.

*Avšak tato novost nemá velkou hodnotu, protože Q2 (Sen) výpočet strukturálně podkopává — viz níže.*

---

### Q2: Zabíjí Senova IR-universalita program fixace γ z CFT log korekcí?

#### Sen, arXiv:1205.0971 — přesný text argumentu

**Hlavní tvrzení o IR-universalitě** (sekce 1 a sekce 2.5 Sena):

> *"[L]ogarithmic corrections arise only from loops of massless fields and from the range of loop momentum integration where the loop momenta remain much smaller than the Planck scale. Thus this can be evaluated purely from the knowledge of the low energy data — the spectrum of massless fields and their coupling to the black hole background."*

A dále, o robustnosti výsledku (sekce 2.5):

> *"[A]s long as the massless fields are kept massless and minimally coupled to gravity even after renormalization effects are taken into account, the one loop logarithmic correction to the partition function is not altered by higher loop corrections."*

Tj.: log korekce jsou **jednosmyčkové IR efekty** a jsou **odolné vůči UV fyzice** — jak vyšší smyčky, tak masivní pole, tak vyšší derivativové opravy neovlivňují logaritmický člen.

**Srovnání Sen vs. LQG (sekce 4 Sena, přesný text):**

> *"S^(lqg)_singlet = S_BH − 2 ln a ... This is different from [Euclidean gravity result S_BH + (212/45 − 3) ln a], showing that the loop quantum gravity result for logarithmic correction to the entropy does not agree with the prediction of the Euclidean gravity analysis."*

Sen tedy explicitně tvrdí: **LQG výsledek −3/2 log (resp. −2 log po korekci na ensemble) nesouhlasí s jeho IR-universálním výsledkem 212/45 − 3 ≈ 1.71 pro čistou 4D gravitaci.**

**Strukturální implikace pro fixaci γ:**

Pokud jsou log korekce čistě IR, pak:

1. Koeficient log členu je deterministicky určen spektrem bezhmotných polí (graviton, příp. gravitino). Pro čistou 4D Einsteinovu gravitaci je výsledek Sena fixní číslo — **nepřizpůsobitelné** volbou γ.

2. Pokud LQG dává odlišný koeficient (−3/2 nebo −2), jde buď o chybu LQG počítání (jiný ensemble, jiná normalizace), nebo LQG nesdílí ten samý IR limit.

3. **Konstantní člen O(1)** je rovněž určen IR daty: je to funkce c_eff, L₀, a teplotní normalizace v Cardyho formuli — ale pokud koeficient log členu nesouhlasí, srovnání konstantního členu je bezpředmětné.

**Klíčová destruktivní implikace pro Tvrzení B:**

Program §2.2 hledá γ z podmínky: −(3/2) ln(3/2πγ) = C_KM(γ). Tato podmínka předpokládá, že Cardyho konstantní člen a LQG konstantní člen musí souhlasit. **Proč by musely?** Sen ukazuje, že log korekce v Cardyho formuli (IR, z c_eff = 6k) a log korekce v LQG mikrostavovém počítání (kombinatorický problém, UV) jsou různé výpočty různé fyziky. Shoda koeficientů −3/2 je:

- buď náhodná numerická koincidence,
- nebo odráží stejné IR struktury (holografická dualita na horizontu), ale pak musí koeficient souhlasit také se Senem — a ten se liší.

**Ghosh-Perez protiargument vs. Senova pozice — rozhodnutí:**

Ghosh-Perez tvrdí, že LQG log korekce mají odlišný fyzikální původ než Sen. Pokud je to pravda, pak:
- Log korekce v LQG nejsou "stejná fyzika" jako Senovy IR korekce.
- Ale pak nejsou ani "stejná fyzika" jako Carlipova Cardyho korekce (která je rovněž IR/CFT).
- Konsistentní pozice Ghosh-Perez by tedy znamenala: LQG log korekce **nepředstavují** IR-universální fyziku a jejich shoda s Cardy −3/2 je **náhoda** nebo **artefakt** specifického počítání.

V obou případech — Senova pozice nebo Ghosh-Perez pozice — **fixace γ z porovnání konstantních členů nemá fyzikální opodstatnění.**

---

### Verdikt: Program je mrtvý

**Tvrzení B je strukturálně neudržitelné** z následujících důvodů:

1. **Sen (1205.0971) explicitně vyvrátil shodu LQG log korekcí s IR-universálním výsledkem.** LQG předpovídá −2 ln a (po korekci ensemble), Eukleidovská gravitace předpovídá +(212/45 − 3) ln a ≈ +1.71 ln a. Tyto hodnoty se **neshodují v koeficientu**. Pokud koeficienty nesouhlasí, porovnání konstantních členů je nerelevantní — hledáme shodu uvnitř modelu, který sám se sebou nekonverguje.

2. **Carlip 1410.5763 neprovádí srovnání konstantního členu** a netvrdí, že by jím šlo fixovat γ. Carlipova práce pracuje primárně s γ = i (komplexní Ashtekarovy proměnné) a explicitně říká, že γ je v standardním přístupu "fixed by an obscure combinatorial problem" — ne z Cardyho formule.

3. **ENP 1006.0634 neuvádí konstantní člen O(1)** v asymptotice, takže vstupní data pro výpočet §2.2 nejsou v ENP dostupná bez dalšího samostatného výpočtu. Tento výpočet by neměl komu co srovnat, protože na Carlipově straně žádný konstantní člen v log-expansi není odvozen.

4. **Strukturální problém**: Program §2.2 implicitně předpokládá, že LQG mikrokanonický výpočet a Carlipův CFT/Cardy výpočet popisují tutéž fyziku natolik úzce, že konstantní členy musí souhlasit. Senova analýza ukazuje, že tato předpoklad není oprávněný — LQG a semiclasická gravitace mají různé log korekce již na úrovni koeficientů.

**Tvrzení A** (analogie γ ↔ c = 6Q₁Q₅) je čistě kvalitativní a nenese testovatelnou predikci. Není ani nové (Carlip tuto analogii implicitně zmiňuje).

**Čistý výsledek:** Hypotéza H01 ve formulaci Tvrzení B **je mrtvá**. Výpočet konstantního členu by mohl být technicky proveden, ale:
- Nemá co srovnávat (Carlip ani ENP ho na druhé straně nepočítají),
- Fyzikální odůvodnění podmínky shody chybí (Sen ukazuje, že LQG a CFT log korekce jsou různé fyziky),
- I kdyby shoda pro γ = γ₀ nastala, bylo by to numerická koincidence bez principiálního základu.

**Zabití hypotézy je správný výsledek.** Čas věnovaný jejímu vyvrácení byl lépe strávený než čas strávený neúspěšným výpočtem.

### Doporučení pro další kroky

Jediná reziduální hodnota programu: zkontrolovat, zda **Bianchi (arXiv:1204.5122)** nebo **Frodden-Geiller-Noui-Perez (1301.6210)** neprovádí srovnání constantních členů pro γ = i případ — tam je γ-závislost eliminována a srovnání může být principiální. Ale i to je marginální — Sen's argument stále platí pro nekomplexní gravitaci.

**Stav H01: UZAVŘENO — program mrtev.**
