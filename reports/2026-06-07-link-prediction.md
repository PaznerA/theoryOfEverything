# Predikce chybějících hran v konceptuálním grafu (link prediction)

**Datum:** 2026-06-07
**Vstup:** `core-data/concept-graph.json` (626 uzlů, 1632 neorientovaných hran po sloučení paralelních záznamů)
**Nástroj:** `lib/kgraph/` (samostatná infrastruktura, oddělená od fyzikální knihovny `toe`)
**Generátor:** `workflows/qg-link-prediction.py` → `core-data/link-predictions.json`

Cílem je strojová varianta hlavní mise projektu: hledání dosud nenalezených
souvislostí mezi přístupy. Úloha "link prediction" predikuje, které dvojice
konceptů, jež dnes nejsou spojené hranou, by spojené *měly* být — to jsou
kandidáti na nové vztahy.

---

## 1 Metodika

### Graf

Záznamy hran v `concept-graph.json` jsou formálně orientované (`from`/`to`), ale
sémanticky symetrické (`related-concept`, `shared-structure`, `duality`, …),
proto je sloučíme do **neorientovaného** grafu. Paralelní záznamy mezi toutéž
dvojicí (v datech až násobnost 3) se sčítají do celočíselné **váhy** hrany
(násobnost = mírný signál síly vazby). Smyčky a hrany na neexistující uzly se
zahazují. Výsledek: řídká symetrická matice sousednosti (`scipy.sparse`),
nulová diagonála.

### Skórovací funkce

Všech pět klasických heuristik je implementováno přímo nad maticí sousednosti
(žádný `networkx`, žádný `torch` — jen `numpy` + `scipy`). Pro dvojici uzlů
*u*, *v* se sousedskými množinami *N(u)*, *N(v)* a stupni *k(·)*:

| heuristika | vzorec | intuice |
|---|---|---|
| společní sousedé | $\lvert N(u)\cap N(v)\rvert$ | kolik konceptů odkazuje na oba |
| Jaccard | $\lvert N(u)\cap N(v)\rvert / \lvert N(u)\cup N(v)\rvert$ | překryv normovaný na velikost |
| Adamic–Adar | $\sum_{w\in N(u)\cap N(v)} 1/\log k(w)$ | vzácní (specifičtí) sousedé váží víc |
| resource allocation | $\sum_{w\in N(u)\cap N(v)} 1/k(w)$ | totéž, ostřejší penalizace hubů |
| preferential attachment | $k(u)\cdot k(v)$ | čistě stupňový baseline |

Navíc **spektrální embedding**: vlastní vektory normalizovaného Laplaciánu
$L = I - D^{-1/2} A D^{-1/2}$ pro 32 nejmenších netriviálních vlastních čísel
(`scipy.sparse.linalg.eigsh`, shift-invert kolem 0). Každý uzel dostane
32-rozměrný vektor; skóre dvojice = kosinová podobnost vektorů. To zachytí
*globální* strukturu, kterou lokální heuristiky nevidí (dva uzly bez společného
souseda mohou být spektrálně blízké).

**Ensemble = rank-average:** každé skóre se převede na pořadí v $[0,1]$ a pořadí
se zprůměrují. Rank-averaging je bezrozměrný, takže se snese sčítání počtů
(celá čísla) s kosiny.

### Hodnocení (poctivá kontrola)

Leave-10%-out: náhodně skryjeme 10 % existujících hran, postavíme trénovací graf
*bez nich*, oskórujeme skryté hrany (pozitiva) proti stejnému počtu náhodně
vzorkovaných ne-hran (negativa), a měříme:

- **AUC** — pravděpodobnost, že náhodné pozitivum předběhne náhodné negativum
  (0,5 = náhoda), počítáno exaktně z rank-sum statistiky (Mann–Whitney *U*);
- **precision@50** — podíl skutečných skrytých hran v top-50 oskórovaných
  kandidátech.

Vše je nasázené (seed) a opakovatelné; reportujeme průměr přes 8 seedů.

---

## 2 Výsledek hodnocení — AUC

```
AUC (8 seedů):   průměr 0.9034   ±0.0176   (min 0.876, max 0.931)
precision@50:    průměr 0.9975
```

**AUC ≈ 0,90 je výrazně nad náhodou (0,5).** Skórovač tedy umí ze schovaných
hran skutečně vytáhnout pozitiva nad náhodné ne-hrany — což je netriviální
generalizace (skóruje se jen na trénovacím grafu *bez* skrytých hran), ne
memorování. Precision@50 ≈ 1,0
znamená, že prakticky všech 50 nejlépe oskórovaných kandidátů byly v testu
skutečně skryté hrany.

Příspěvek jednotlivých složek (průměrná AUC):

| složka | AUC |
|---|---|
| spektrální embedding (kosinus) | **0.930** |
| resource allocation | 0.859 |
| Adamic–Adar | 0.859 |
| Jaccard | 0.856 |
| společní sousedé | 0.855 |
| preferential attachment | 0.617 |

Nejsilnější je **spektrální embedding** — globální struktura nese víc signálu
než lokální překryv sousedů. Naopak **preferential attachment** je jen slabě nad
náhodou (0,62); ponecháváme ho v ensemblu jako poctivý baseline, ale je to ta
složka, která zvýhodňuje hub-uzly (viz kritika níže) a samotná by predikovala
hlavně "spoj dva nejnapojenější uzly".

> Upřímná poznámka: AUC ≈ 0,90 je dobré, ale graf je sám produktem dřívějšího
> AI/redakčního budování. Predikujeme tedy *konzistenci s dosavadní topologií*,
> ne fyzikální pravdu. Vysoké AUC říká "model dobře doplňuje vzor, který už v
> grafu je", nikoli "tyto vazby ve fyzice existují".

---

## 3 Top kandidáti — kritické čtení

Celkem 50 kandidátů je v `core-data/link-predictions.json`. Rozpadají se na dvě
velmi odlišné kategorie:

### 3a Hub artefakty (NEzajímavé) — pillar↔pillar dvojice

**17 z top-50** jsou dvojice dvou *pilířových* uzlů (těch 19 zastřešujících
přístupů). Ty mají z definice obrovský stupeň a sdílejí desítky sousedů, takže
je každá heuristika tlačí nahoru. Příklady, které okupují prvních 9 míst:

| # | dvojice (pilíř ↔ pilíř) | skóre | proč je to artefakt |
|---|---|---|---|
| 1 | Conceptual Problems ↔ Emergent/Entropic Gravity | 0.980 | 15 společných sousedů, ale jde o dva sběrné hub-pilíře |
| 3 | Experimental Tests ↔ Von Neumann Algebras | 0.963 | spojuje fenomenologii s abstraktní algebrou jen přes hubovost |
| 5 | CDT ↔ Conceptual Problems | 0.955 | "conceptual-problems" je soused skoro všeho |

**Tyto kandidáty je nutné z brainstormu odfiltrovat** (v JSON je odhalí
`typeFrom == "pillar" && typeTo == "pillar"`). Že je `crossPillar` flag u nich
zapnutý je *zavádějící* — nejde o nový můstek mezi přístupy, jen o dva velké
rozcestníky. Pole `pillarPairCount` v JSON jejich počet vyčísluje.

### 3b Fyzikálně zajímaví kandidáti (koncept↔koncept)

Po odfiltrování hubů zůstává jádro v top-50 silně koncentrované do **von
Neumannových algeber / modulární teorie / crossed-product konstrukcí** — což je
skutečná současná hranice výzkumu (CLPW pozorovatelské algebry, typ II vs III).
Patnáct nejzajímavějších:

| pořadí | kandidát | skóre | komentář |
|---|---|---|---|
| 10 | **Generalized entropy ↔ Crossed product algebra** | 0.943 | Velmi přirozený: generalizovaná entropie v CLPW programu *je* stopa na crossed-product algebře typu II. Pravděpodobně chybějící hrana, hodná zápisu. |
| 14 | **Crossed product algebra ↔ de Sitter static-patch observer algebra** | 0.927 | de Sitter algebra pozorovatele (CLPW) je přímo crossed product. Kosinus 1,00 — silný kandidát. |
| 16 | **Modular Hamiltonian ↔ Type III₁ of local QFT algebras** | 0.925 | Reeh–Schlieder + Bisognano–Wichmann pojí modulární Hamiltonián s typem III₁. Učebnicová, ale v grafu chybějící vazba. |
| 17 | **Problem of time ↔ Relational / dressed observables** | 0.924 | Klasické řešení problému času přes relační/dressed pozorovatelné (Page–Wootters). Logická, spíš "doplnění" než objev. |
| 19 | Modular flow ↔ Bisognano–Wichmann theorem | 0.916 | BW *je* geometrický modulární tok pro Rindlerův klín — opět triviální v rámci jednoho pilíře. |
| 20 | Connes classification of type III ↔ Crossed product algebra | 0.915 | Connesova klasifikace stojí na crossed-product konstrukci. Standardní. |
| 23 | **Generalized entropy ↔ Modular Hamiltonian** | 0.910 | Přes JLMS relaci — netriviální a fyzikálně bohatý můstek. |
| 24 | Renormalized Stress-Energy Tensor ↔ Algebraic/Locally Covariant QFT | 0.909 | Waldovy axiomy + Hadamardův stav; přirozené v semiklasické gravitaci. |
| 28 | **Spectral triple ↔ Standard Model from spectral geometry** | 0.901 | Jediný silný kandidát mimo modulární klastr: NCG spektrální trojice ↔ odvození SM ze spektrální geometrie. Connesův program. |
| 31 | Tomita–Takesaki ↔ Emergent geometry from modular data | 0.899 | "Thermal time" / emergentní geometrie z modulárních dat — zajímavé, leč spekulativnější. |
| 35 | Swampland Program ↔ Swampland Distance Conjecture | 0.897 | Triviální (pilíř a jeho vlastní conjecture). |
| 38 | D-brane ↔ M-theory | 0.896 | Triviálně související uvnitř strun (přes S-dualitu, BFSS). Artefakt. |
| 39 | **Noncommutative Geometry ↔ Spectral Dimension** | 0.896 | Minimální délka + spektrální dimenze napříč NCG/CDT/causal sets — mezipřístupově zajímavé. |
| 42 | Diósi–Penrose ↔ Post-quantum classical gravity | 0.895 | Modely kolapsu vs. Oppenheimerova post-kvantová gravitace — fenomenologicky zajímavý můstek. |
| 33–34 | EPRL-FK spin foam ↔ Effective / coarse-grained spin foams | 0.898 | Triviální uvnitř LQG; doplnění, ne objev. |

**Tři nejzajímavější** (kritérium: koncept-koncept, nenulový mezipřístupový
obsah, ne učebnicová tautologie):

1. **Generalized entropy ↔ Crossed product algebra** (#10, 0.943) — jádro CLPW
   programu, přirozeně chybějící hrana mezi entanglementem a vN algebrami.
2. **Spectral triple ↔ Standard Model from spectral geometry** (#28, 0.901) —
   jediný silný kandidát mimo modulární klastr, srdce Connesova NCG odvození SM.
3. **Noncommutative Geometry ↔ Spectral Dimension** (#39, 0.896) — skutečně
   mezipřístupový (NCG ↔ CDT/causal-sets přes minimální délku a běh spektrální
   dimenze), tj. typ vazby, kterou projekt loví.

### Obecná kritika

- Skórovač má **silný bias k hub-uzlům** a k **hustému okolí jednoho pilíře**
  (von Neumann/modulární klastr je v grafu nejhustěji propojený, tak ho model
  preferuje). To není chyba — odráží topologii — ale znamená to, že
  "objevnost" kandidáta je nepřímo úměrná jeho skóre: nejvyšší skóre = nejvíc
  očekávané, nejméně objevné vazby.
- **Žádný z top-50 není v `connections.json`** (ověřeno) — nejde o
  re-derivaci už zapsaných vztahů, ale ani o garanci novosti: většina je
  "v učebnici zřejmá, jen v grafu nezakreslená".
- Skutečně objevné můstky (vzdálené pilíře s málo společnými sousedy) budou
  skórovat *nízko*, ne vysoko — pro ně je lepší prohledávat střední pásmo
  žebříčku a `explored: barely` zónu, ne špičku.

---

## 4 Jak s tím naloží příští brainstorm — provenance policy

**Kandidáti jsou NÁVRHY, ne fakta.** Pravidlo:

1. **Nikdy nezapisovat kandidáta přímo** do fragmentů knowledge base ani do
   `connections.json` jen proto, že ho model vyhodil. To by zanesla strojový
   artefakt jako doložené tvrzení.
2. Do fragmentu/registru se vazba propíše **až po redakčním/výzkumném
   rozhodnutí**: člověk (nebo cílený rešeršní běh) ověří, že vazba má oporu v
   literatuře (arXiv ID / DOI dle datové konvence), a teprve pak ji zapíše s
   řádnou provenancí a ratingem `explored`.
3. **Hub-pilířové dvojice (3a) se ignorují** — filtr
   `typeFrom==pillar && typeTo==pillar`.
4. Pro příští brainstorm jsou nejcennější vstupy:
   - **#10, #28, #39** jako horké tipy k ověření;
   - a paradoxně **střední a spodní pásmo** žebříčku + zóna `explored: barely`,
     kde žije skutečná "objevnost" (vzdálené pilíře). Špička žebříčku slouží
     spíš jako sanity-check, že graf je vnitřně konzistentní.

Výstup je strojově dostupný v `core-data/link-predictions.json` (pole
`candidatePolicy` nese tuto politiku i v datech) a vizuálně na webu
(`/data/graph.html`, predikované hrany odlišnou barvou, přepínatelné).
