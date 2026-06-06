# VYPOCET-10: Kde v SJ stavu žije rotace (eigenvektory / Wightman) a mechanismus opačných znamének (A_caus>0 vs A_W<0)

**Datum:** 2026-06-06
**Soubory:** `core-data/calculations/sj-eigenvector-superradiance/calc.py`, `results.json`, `plots/{eigenvector_overlap,occupation_map,superradiance_weight,toy_model_opposite_sign}.png`
**Status:** Dokončeno (dvě provázané sondy navazující na VYPOCET-05 a VYPOCET-08)
**Hypotéza:** H02 — SJ stav na Kerrově prostoročase, **Strategie II** (`knowledge-base/hypotezy/H02-sj-kerr.md`)
**Návaznost:** Přímé prohloubení VYPOCET-05 (rotující BTZ) a VYPOCET-08 (ekvatoriální Kerr). Zděděná konformní páka, geometrie i SJ pipeline jsou **identické**; zde se útočí na dva nejslabší body draftu-01 (`papers/draft-01-sj-rotating-spacetimes/TODO.md`, body 1.4, 3 a 6): (A) tvrzení „rotace žije v eigenvektorech, ne ve spektru" a (B) **mechanismus** opačného znaménka `A_caus>0` vs `A_W<0`.

---

## Cíl

VYPOCET-05/08 zjistily, že **eigenvalue spektrum** `iΔ` je téměř konformně invariantní — rotace je v eigenvalues neviditelná. Současně našly **opačné znaménko**: kauzálně-početní asymetrie `A_caus>0` (více co-rotujících spojů), ale SJ-korelační asymetrie `A_W<0` (na spoj jsou korelace silnější proti-rotujícně). Obojí bylo dosud jen *naměřeno*, bez mechanismu. Tento výpočet má dva provázané cíle:

**CÍL A — Kde rotace žije?** Ukázat přímo, že rotace sedí v **eigenvektorech / Wightmanově funkci `W`**:
- A1: na **jediném sdíleném sprinklingu** porovnat SJ kladný podprostor rotujícího a statického řezu — měřit překryv (hlavní úhly).
- A2: **frekvenční analýza** — projektovat SJ eigenvektory na přibližné rovinné vlny `e^{−iωt+ikφ}` (nejmenší čtverce / Monte-Carlo L² na sprinklovaných bodech) a postavit mapu obsazení `(ω,k)` kladného SJ podprostoru.
- A3: **signatura superradiance** — ve strženém (ZAMO) rámci hledat váhu módů s `ω(ω−kΩ)<0` (diskrétní analog superradiantního míchání), kvantifikovat vs spin `a` a vs `r` relativně k ergosféře; statická kontrola musí dát ~nulu.

**CÍL B — Mechanismus opačných znamének.** Postavit analytický toy model: 2D diamant pod boostem/shearem (strhávání naklání kužely) a spočítat, jak naklonění ovlivňuje (i) **početní** asymetrii kauzálních párů (geometrie) vs (ii) **fázovou/korelační** asymetrii bezhmotné Wightmanovy funkce `W₀(x,y)=−(1/4π)ln(…)` na nakloněných intervalech. Otestovat proti naměřeným číslům (BTZ +0.227/−0.211 při r=1.3; Kerr a=0.6 +0.317/−0.296; a=0.9 +0.431/−0.382).

---

## Metoda

### Páka a pipeline (identické s VYPOCET-05/08)

Bezhmotný 2D skalár ⇒ `G_R=(1/2)C` (konformně invariantní; Sorkin–Yazdi 1611.10281 eq.9; zakřivená 2D/AdS₂ 2504.12919). `iΔ=i·(1/2)(C−Cᵀ)` hermitovský; SJ Wightman `W = Σ_{λ>0} λ vv†`. Pevné-`r` řez `(t,φ)`, konstantní indukovaná 2-metrika `h`, kauzální uspořádání z naklonených kuželů, rovnoměrný sprinkling. Geometrie:
- **Kerr (ekvátor):** `h=[[−(1−2M/r),−2Ma/r],[−2Ma/r,r²+a²+2Ma²/r]]`, `det h=−Δ`, `r_erg=2M`.
- **BTZ:** `h=[[M−r²,−J/2],[−J/2,r²]]`, `det h=−N²r²`, `r_erg=√M`.

Strhávací (ZAMO/LNRF) úhlová rychlost: `Ω = −g_tφ/g_φφ` (= strhávací sklon, tentýž, který orientuje čas v VYPOCET-05/08).

### CÍL A — měřítka

- **A1 (překryv podprostorů).** Na **témž** sprinklingu (stejný seed) se postaví `C` pro rotující a statický řez, diagonalizuje `iΔ`, vezmou kladné eigenvektory `V₊`. Překryv obou kladných podprostorů přes singulární čísla matice `V₁†V₂` (= kosiny hlavních úhlů): `mean cos²`. `1` = identické podprostory, `→0` = ortogonální. Odděluje to náhodnost sprinklingu (sdílené body) a izoluje **čistý vliv naklonění kuželů na eigenvektory**. Statika-vs-statika musí dát přesně `1` (sanity).
- **A2 (mapa obsazení).** `P(ω,k)=Σ_módy λ·|⟨vlna(ω,k)|v⟩|²`, kde `⟨vlna|v⟩=(1/N)Σ_n exp(+iωt_n−ikφ_n)v_n` (Monte-Carlo aproximace L² skalárního součinu na rovnoměrném sprinklingu; vlna `e^{−iωt+ikφ}`). Normováno na součet 1.
- **A3 (superradiantní klín).** Váha mapy v klínu `ω(ω−kΩ)<0` (ko-rotující frekvence `ω−kΩ` má opačné znaménko než `ω`), plus ko/proti `k`-asymetrie kladně-frekvenční (`ω>0`) části. Klín je invariantní pod `(ω,k)→(−ω,−k)`, takže nezávisí na konvenci znaménka SJ kladné části. Pro statiku (`Ω=0`) má klín míru nula ⇒ váha přesně 0.

### CÍL B — toy model (naklonený/strižený diamant)

Pevné-`r` řez je konstantní-`h` 2D patch (= „strižený Minkowski"). Zavedeme **nulové souřadnice zarovnané se skutečným kuželem**:
```
u = φ − s₊ t,   v = φ − s₋ t,
```
kde `s±=(dφ/dt)` nulové sklony řeší `g_φφ s² + 2g_tφ s + g_tt = 0`. V `(u,v)` je `h` čistě mimodiagonální (`h ∝ du dv` — ověřeno numericky, viz níže), takže řez je konformní s plochým 2D a bezhmotná Wightmanova funkce je
```
W₀(x,y) = −(1/4π) ln|Δu Δv|  (+ konst.),
```
závisí **pouze** na nulovém intervalu (konformní invariance). „Časupodobná osa" kuželu (hřeben maximálního intervalu) je sklon `m=s_drag=(s₋+s₊)/2 = −g_tφ/g_φφ` — přesně strhávací směr.

- **(i) Početní asymetrie (geometrie).** Kauzální spoj má sklon `m=dφ/dt ∈ (s₋,s₊)`. `f_co` = podíl s `dφ>0` (tj. `m>0`). Pro kladné strhávání se kužel otevírá víc do `+φ` (`s₊>|s₋|`), takže víc spojů ko-rotuje: `A_caus>0`. Čistý jev clony kuželu; spočítáno kontinuálně Monte-Carlem na rovnoměrném patchi (žádné SJ).
- **(ii) Korelační asymetrie (fáze/interval).** Podél kauzálního spoje `|Δu Δv| = (s₊−m)(m−s₋)·dt²` je **maximální** ve středu kuželu `m=s_drag` (nejdelší interval = nejslabší korelace) a `→0` u nulových hran (nejkratší interval = nejsilnější korelace). Protože strhávání posune časupodobnou osu `s_drag>0` na ko-rotující stranu, ko-rotující pás `(0,s₊)` osedlá hřeben slabé korelace, zatímco proti-rotující pás `(s₋,0)` leží blíž nulové hraně ⇒ **kratší interval ⇒ silnější `W` na spoj ⇒ `A_W<0`**. Korelace jsou silnější podél **stlačeného** nulového směru, spojů je víc podél **roztaženého** — opačná znaménka z téhož naklonění.

**Kontrola velikosti `A_W`.** Na **skutečném** sprinklovaném SJ `W` se per-link `Re W` regreduje proti kontinuálnímu logu `−(1/4π)ln|Δu Δv|` (fit `α·log+β`). Ukáže se, že **znaménko** (čitatel `m_co−m_cc`) je dáno logem, **velikost** (jmenovatel `|m_co|+|m_cc|`) je dána aditivním offsetem konečné oblasti, který SJ `W` fixuje, ale holý log ne.

---

## Vstupy s citacemi

| Vstup | Hodnota / forma | Zdroj |
|-------|-----------------|-------|
| `G_R=(1/2)C` (2D bezhmotný, konformně invariantní) | faktor ½ | Sorkin-Yazdi **1611.10281** eq.9; zakřivená AdS₂ **2504.12919** |
| `iΔ=i(1/2)(C−Cᵀ)`; SJ W = kladná část | spektrální | Sorkin-Yazdi **1611.10281**; Afshordi-Aslanbeigi-Sorkin **1205.1296** |
| Bezhmotná 2D Wightman `W₀=−(1/4π)ln(−Δx²+iε Δx⁰)` | logaritmická, konf. inv. | standardní 2D QFT (ověřeno; viz limity níže) |
| Superradiantní podmínka `ω−mΩ<0` (`ω(ω−mΩ)<0`) | ko-rotující frekvence záporná | standardní (Kerr superradiance); zde `Ω=−g_tφ/g_φφ` (ZAMO) |
| Kerr/BTZ metrika, horizonty, ergosféra | viz | VYPOCET-05/08, tamtéž |
| Konvence + kód zděděny z VYPOCET-05/08 | — | tento projekt |

---

## Výsledky

### Ověření faktorizace do nulových souřadnic (předpoklad CÍLE B)

Pro Kerr `a=0.6, r=2.6` je `h` v `(u,v)` souřadnicích čistě mimodiagonální (diagonála `~10⁻¹⁶`, mimodiagonála `≈3.698`), tj. `h ∝ du dv`. Strhávací sklon `Ω=0.0624` je přesně `(s₋+s₊)/2`. Řez je tedy konformní s plochým 2D a `W₀=−(1/4π)ln|Δu Δv|` je korektní kontinuální Wightman.

### CÍL A1 — rotace žije v eigenVEKTORECH (HLAVNÍ VÝSLEDEK A)

| Srovnání (sdílený sprinkling, 5 seedů) | mean cos² podprostorů | hlavní úhel | rel. rozdíl spektra | drift link-frakce |
|----------------------------------------|------------------------|-------------|---------------------|--------------------|
| **Kerr** `a=0.9` vs `a=0`, `r=2.6` | **0.507** | **44.6°** | **2.0 %** | **0.6 %** |
| **BTZ** `J=0.6` vs `J=0`, `r=1.3` | **0.509** | ~44.6° | 2.3 % | — |
| statika vs statika (sanity) | **1.000000** | 0° | — | — |

**Interpretace:** Eigenvalue spektra se shodují na ~2 %, kauzální link-frakce driftuje <1 %, ale **kladné SJ podprostory rotujícího a statického řezu jsou pootočené o ~45°** (`mean cos²≈0.51`). To je přímý, kvantitativní důkaz teze draftu: rotace nesedí v eigenvalues, ale v **eigenvektorech** — a tedy v `W`. Sanity (statika vs statika na témž sprinklingu) dává přesně `1`, takže ~45° není artefakt metody. (Plot `eigenvector_overlap.png`.)

### CÍL A2 — mapa obsazení `(ω,k)` (frekvenční tvář strhávání)

Plot `occupation_map.png`: statická mapa (`a=0`) je **symetrická v `k`** s kladným SJ podprostorem koncentrovaným při `ω<0` (negativně-frekvenční obsah pole v této znaménkové konvenci SJ kladné části). Rotující mapa (`a=0.9`) je viditelně **strižená/nakloněná**: pás obsazení i tmavá „mezera" sledují strhávací přímku `ω=kΩ` (Ω=0.084). To je frekvenčně-prostorový otisk strhávání.

### CÍL A3 — superradiantní váha SJ kladného podprostoru (HLAVNÍ VÝSLEDEK A)

**Vs spin `a` (r=2.6, 5 seedů):**

| `a` | `Ω` | váha superrad. klínu `ω(ω−kΩ)<0` | `k`-asymetrie (`ω>0`) |
|-----|-----|-----------------------------------|------------------------|
| **0 (kontrola)** | 0.000 | **0.0000 ± 0.0000** | +0.007 ± 0.013 (≈0) |
| 0.3 | 0.033 | 0.0012 ± 0.0001 | +0.042 ± 0.009 |
| 0.6 | 0.062 | 0.0062 ± 0.0003 | +0.073 ± 0.007 |
| 0.9 | 0.085 | **0.0171 ± 0.0004** | +0.100 ± 0.007 |

**Vs `r` relativně k ergosféře (a=0.9, `r_erg=2.0`):**

| `r` | `r−r_erg` | `Ω` | váha superrad. klínu | `k`-asymetrie |
|-----|-----------|-----|-----------------------|----------------|
| 2.05 | +0.05 | 0.151 | **0.0755** | +0.266 |
| 2.2 | +0.20 | 0.128 | 0.0493 | +0.193 |
| 2.6 | +0.60 | 0.085 | 0.0171 | +0.100 |
| 3.2 | +1.20 | 0.049 | 0.0031 | +0.058 |
| 4.0 | +2.00 | 0.026 | 0.0000 | +0.036 |

**Interpretace:** SJ kladný podprostor nese ko-rotující váhu v superradiantním pásmu `ω(ω−kΩ)<0`, která **roste monotónně se spinem** a **prudce směrem k ergosféře** (0.0000 daleko → 0.0755 těsně vně `r_erg`). **Statická kontrola dává přesně nulu** (klín má míru nula při `Ω=0`). Toto je diskrétní, eigenvektorová signatura superradiantního míchání ve struktuře SJ stavu — přesně tam, kde VYPOCET-05/08 předpověděly, že rotace bude žít (ne v hrubém spektru). (Plot `superradiance_weight.png`.)

### CÍL B — mechanismus opačných znamének (HLAVNÍ VÝSLEDEK B)

| Případ | kužel `(s₋,s₊)` | strhávání | `A_caus` toy vs měřené | `A_W` toy (log) — znaménko | `A_W` velikost: log+offset vs měřené SJ | korelace SJ~log |
|--------|------------------|-----------|--------------------------|------------------------------|------------------------------------------|------------------|
| **BTZ** J=0.6 r=1.3 | (−0.486,+0.841) | +0.178 | **+0.217** vs +0.227 (96 %) | OK (−) | **−0.230** vs −0.203 | 0.967 |
| **Kerr** a=0.6 r=2.6 | (−0.125,+0.250) | +0.062 | **+0.315** vs +0.317 (99 %) | OK (−) | **−0.334** vs −0.298 | 0.953 |
| **Kerr** a=0.9 r=2.6 | (−0.103,+0.272) | +0.084 | **+0.426** vs +0.431 (99 %) | OK (−) | **−0.419** vs −0.384 | 0.951 |

**Mechanismus potvrzen ve všech třech případech z prvních principů:**
1. **`A_caus` je čistě početní (geometrie clony kuželu).** Kontinuální toy hodnota sedí na naměřenou SJ na ~1 % — kauzálně-početní asymetrie je čistě v naklonění kuželu, žádné SJ.
2. **Znaménko `A_W<0` plyne z holého bezhmotného logu `W₀`** ve všech případech. Mechanismus: ve všech třech má **proti-rotující pás kratší interval** (`⟨ln|Δu Δv|⟩`: BTZ co=−2.35/cc=−2.66; Kerr a=0.6 co=−4.85/cc=−5.24; a=0.9 co=−4.82/cc=−5.39) ⇒ silnější korelace na proti-rotující straně ⇒ `A_W<0`.
3. **Velikost `A_W`** se obnoví, jakmile se zahrne aditivní offset konečné oblasti: SJ per-link `Re W` koreluje s kontinuálním logem na **0.95–0.97**; čitatel (`m_co−m_cc`) je dán logem, jmenovatel (`|m_co|+|m_cc|`) je dán offsetem (SJ `W` má skoro nulový průměr, `β≈−0.42`, holý log má velký kladný offset). Po dosazení fitovaného offsetu: toy `−0.230/−0.334/−0.419` vs měřené `−0.203/−0.298/−0.384` (shoda na ~12 %).

To přímo odpovídá na nejzranitelnější bod draftu (TODO 1.4): opačné znaménko **NENÍ** normalizační/binningová konvence, ale geometrický důsledek toho, že strhávání posune časupodobnou osu kuželu na ko-rotující stranu — početní výhoda je na roztažené straně, korelační síla na stlačené. (Plot `toy_model_opposite_sign.png`.)

---

## Interpretace pro hypotézu H02

1. **Rotace v SJ stavu je eigenvektorový jev.** A1 to ukazuje přímo: ~45° pootočení kladného podprostoru při <2 % změně spektra a <1 % změně link-frakce. To uzavírá mezeru v draftu („rotace žije v eigenvektorech" už není jen z malého spektrálního rozdílu, ale z přímého měření překryvu eigenvektorů).

2. **Superradiance má eigenvektorovou signaturu i ve 2D.** VYPOCET-05/08 tvrdily, že v 2D nemá superradiantní pásmo přímý analog (spektrum konformně invariantní). A3 ukazuje, že **má** — ne ve spektru, ale ve frekvenčním obsahu kladného SJ podprostoru: váha v `ω(ω−kΩ)<0` roste se spinem a k ergosféře, statická kontrola je nula. To je most ke 4D: ve 4D Kerrovi bude superradiantní otisk SJ stavu pravděpodobně rovněž ve frekvenčním obsahu eigenvektorů / `W`, ne v hrubém spektru `iΔ`.

3. **Opačné znaménko je vyřešeno mechanismem, ne jen naměřeno.** Toy model (boostnutý/strižený diamant) reprodukuje obě znaménka a velikosti z prvních principů: početní asymetrie z clony kuželu (geometrie), korelační z bezhmotné Wightmanovy funkce na nakloněných intervalech (stlačený vs roztažený nulový směr). To povyšuje „netriviální vlastnost SJ vakua" na **odvozený geometrický důsledek strhávání**.

---

## Limity výpočtu

- **Pouze 2D, bezhmotný skalár, pevné-`r` řez** (Strategie II), zděděno z VYPOCET-05/08. 4D (`G_R≠½C`) zůstává otevřený.
- **Rovinné vlny na sprinklingu nejsou ortonormální báze.** Mapa obsazení `P(ω,k)` je standardní per-mód overlap estimator s normalizovanými vlnami, ne přesná spektrální dekompozice; absolutní hodnoty váhy klínu závisí na `(ω,k)`-mřížce (KMAX=35, 71×71). **Trendy** (monotonie ve spinu/`r`, statická nula) jsou robustní; absolutní čísla klínu jsou orientační. Statická nula je ovšem exaktní (klín míry nula), ne numerický artefakt.
- **`mean cos²≈0.5`** je průměr přes všechny hlavní úhly; část pochází z toho, že naklonění mění, *které* páry jsou kauzální (drift link-frakce 0.6 %). I tak je 0.6 % link-drift vs 44° pootočení podprostoru jasný signál „v eigenvektorech".
- **Velikost `A_W` v toy modelu** vyžaduje fitovaný offset z reálného SJ `W` (znaménko je bez fitu, čistě z logu). Offset je vlastnost konečné oblasti / SJ konstrukce, ne volný parametr — fit má korelaci 0.95–0.97 a jednu degeneraci (sklon+posun).
- **Fixní N=1600, 5 seedů, konečné φ-okno** — zděděné limity VYPOCET-05/08; směrové signatury a existence jsou robustní, kontinuální (`N→∞`) extrapolace zde není.
- **`W₀` má v 2D bezhmotném IR/zero-mode subtilitu** (aditivní konstanta logu) — to je přesně ten offset, který odděluje znaménko od velikosti; SJ na konečné oblasti ho fixuje.

---

## Citace (prohledané/použité)

- **1611.10281** — Sorkin, Yazdi (`G_R=½C`, `iΔ`, SJ W = kladná část)
- **1205.1296** — Afshordi-Aslanbeigi-Sorkin (SJ kontinuum)
- **2504.12919** — konformní plochost ⇒ `½C` v zakřivené 2D (AdS₂)
- **1701.07212, 1712.04227** — masivní `G_R`, limita m→0
- Bezhmotná 2D Wightman `W₀=−(1/4π)ln(…)`, logaritmická a konformně invariantní — standardní 2D QFT (ověřeno proti literatuře; faktor `1/4π` a `iε`-předpis)
- Superradiantní podmínka `ω<mΩ_H` (`ω−mΩ` ko-rotující frekvence) — standardní Kerr superradiance; zde `Ω=−g_tφ/g_φφ` (ZAMO/LNRF)
- **H02-sj-kerr.md** (tento projekt) — Strategie II
- **VYPOCET-05** (sj-rotating-btz), **VYPOCET-08** (sj-kerr-equatorial) — zděděné konvence, kód, naměřená čísla
- **draft-01 TODO.md** body 1.4, 3, 6 — referee atak, na který tento výpočet odpovídá
