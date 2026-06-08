# VYPOCET-26: Mocninový exponent B(a) — je B spojitou funkcí strhávání, nebo dimenzionální konstanta D−1?

**Datum:** 2026-06-08
**Soubory:** `core-data/calculations/sj-kerr-b-scan/calc.py`, `results.json`, `plots/B_vs_spin.png`
**Status:** Dokončeno (plná mřížka 8 Kerr spinů + 2 BTZ; N=1600, 5 seedů; wall-clock 12,6 min)
**Hypotéza:** H5g-5 — je exponent B v `W_sr ~ Ω(r)^B` SPOJITOU funkcí strhávání/asymptotiky, nebo dimenzionální konstanta `D−1=3`?
**Návaznost:** Uzavírá fyzikální predikci §4.2 draftu-01; reuse pipeline z VYPOCET-14 (sj-threshold-scan) a VYPOCET-15 (sj-far-zone); navazuje na F-017, F-018, F-013.

---

## Cíl (proč to byl otevřený problém)

VYPOCET-14/15 rozhodly, že radiální profil superradiantní váhy sleduje **Model S** `W_sr = A·Ω(r)^B` (frekvenčně-stavový), nikoli Model E (geometrický Lorentzián na `r_erg`): společný near+far AIC dal ΔAIC = +3894 (a=0.6), +4216 (a=0.9), +231 (BTZ J=0.9). **Toto rozhodnutí je uzavřené a nezpochybňujeme ho.**

Co zůstalo otevřené: **samotná hodnota B**. Committed exponenty z VYPOCET-14 (B=4.23 pro a=0.6, B=3.82 pro a=0.9) pocházely z **omezeného** scipy fitu, který narazil na horní mez amplitudy `A=100` (viz caveat F-017). Absolutní B proto byly jen orientační. Otevřená fyzikální otázka pro §4.2:

- Pokud B je **dimenzionální konstanta** `D−1=3` (kde D je dimenze prostoročasu řezu), pak B musí být **konstantní v a** a stejné pro všechny geometrie.
- Pokud B se **plynule mění se spinem** (data už naznačovala 4.23→3.82 pro a=0.6→0.9), je B **spojitou funkcí strhávání rámce**.

Tento výpočet rozliší obě možnosti spolehlivým, **neomezeným** fitem B na husté spinové mřížce.

---

## Metoda

Pipeline identická s VYPOCET-14/15/10/08 (žádné nové pozadí):
- 2D bezhmotný skalár, `G_R=(1/2)C` (konformně invariantní, [1611.10281 eq.9]), `iΔ=i(1/2)(C−Cᵀ)`, SJ `W = Σ_{λ>0} λ vv†`.
- Kerr ekvatoriální `h=[[−(1−2M/r),−2Ma/r],[−2Ma/r,r²+a²+2Ma²/r]]`, `r_erg=2M`.
- BTZ `h=[[M−r²,−J/2],[−J/2,r²]]`, `r_erg=√M`.
- `Ω=−g_tφ/g_φφ` (ZAMO), superradiantní klín `ω(ω−kΩ)<0`, `W_sr` = váha v klínu.
- `N=1600`, 5 seedů `[101,202,303,404,505]`, `T=Φ=1.4`, `(ω,k)`-mřížka `NW=71, KMAX=35`.

### Neomezený log-log fit B (oprava artefaktu A=100)

Klíčová změna oproti VYPOCET-14: B se neextrahuje z omezeného nelineárního fitu, ale z **neomezené (váhované) log-log regrese**

$$\log W_{sr} = \log A + B\,\log\Omega,\qquad B = \text{sklon},\ A\ \text{volné}.$$

Váhy = propagovaná relativní chyba `sd(W)/W` (floor 1 %). Reportujeme:
- regresní směrodatnou chybu `B_se`,
- **bootstrap 95% CI** přes 5 seedů (2000 replik; resampling seedů s návratem, znovu-fit sklonu — zachycuje dominantní Monte-Carlo nejistotu sprinklingu),
- log-log korelaci a R² (analog `corr_loglog(S)=0.9992` z VYPOCET-15).

Do fitu vstupují jen near-zone body s `W_sr>0` strictly vně `r_erg` (a vně `r_+`). Použité poloměry: Kerr `r ∈ {2.02, 2.05, 2.10, 2.20, 2.40, 2.80}` (6 bodů; pro a=0.3 jen 5, protože při slabém spinu `W_sr=0` na r=2.80 — pod rozlišením mřížky); BTZ `r ∈ {1.02..1.80}` (7 bodů).

### Trend B(a)

Váhovaná lineární regrese `B(a)=B0 + slope·a` (váhy z bootstrap SE). Diskriminátor pro H5g-5: χ² dat vůči **konstantnímu modelu B=3** (`D−1`) versus χ² lineárního modelu, plus z-signifikance sklonu.

### Rozpočet a schéma

Plná 8-spinová mřížka by podle a-priori odhadu (~1,6 s/bod) trvala ~7,5 min ≪ 0,75·cap, takže běžela **plná mřížka** (žádné zúžení nebylo nutné). Skutečný wall-clock 12,6 min. `results.json` se zapisuje **atomicky** (`tmp` + `os.replace`) s polem `status` (`running`→per-spin flush→`complete`) a progresivně po každém spinu — přerušení na limitu by zanechalo validní částečný výstup.

---

## Výsledky

### Spolehlivý B(a) — Kerr (neomezený log-log fit)

| a | B ± SE | bootstrap 95% CI | R²(log-log) | corr | n | starý omezený B |
|---|--------|------------------|-------------|------|---|-----------------|
| 0.30 | **6.10 ± 0.11** | [5.83, 6.84] | 0.9878 | 0.9950 | 5 | — |
| 0.50 | **3.70 ± 0.06** | [3.62, 3.80] | 0.9981 | 0.9996 | 6 | — |
| 0.60 | **3.32 ± 0.05** | [3.23, 3.42] | 0.9985 | 0.9994 | 6 | **4.23** |
| 0.70 | **3.13 ± 0.05** | [3.06, 3.21] | 0.9988 | 0.9995 | 6 | — |
| 0.80 | **2.83 ± 0.04** | [2.79, 2.86] | 0.9994 | 0.9997 | 6 | — |
| 0.90 | **2.67 ± 0.04** | [2.63, 2.72] | 0.9994 | 0.9997 | 6 | **3.82** |
| 0.95 | **2.55 ± 0.04** | [2.51, 2.58] | 0.9993 | 0.9997 | 6 | — |
| 0.99 | **2.54 ± 0.04** | [2.51, 2.57] | 0.9994 | 0.9997 | 6 | — |

Všechny fity mají R² ≥ 0.988 a log-log korelaci ≥ 0.995 — **sklon (= B) je výborně určen** (konzistentní s `corr_loglog(S)=0.9992` z VYPOCET-15).

**Jak moc mez A=100 zkreslila starý B:** starý omezený B (a=0.6: 4.23; a=0.9: 3.82) leží **výrazně NAD** spolehlivým neomezeným B (3.32, resp. 2.67) — nadhodnocení o **+0.91** (a=0.6) a **+1.15** (a=0.9). Vynucení `A≤100` přitlačilo optimalizátor ke strmějšímu sklonu, aby se vešel do nižší amplitudy. Robustní informace VYPOCET-14 (ΔAIC, preference Model S) zůstává; absolutní B byl skutečně jen orientační, jak caveat F-017 přiznával.

### Trend B(a) — diskriminátor H5g-5

- **Sklon `dB/da = −2.20 ± 0.07`, z = −33.6** — extrémně signifikantní (≫ 3σ).
- B napříč Kerr mřížkou v rozsahu **[2.54, 6.10]**, váhovaný průměr 2.72.
- χ² vůči konstantnímu `B=3` (`D−1`) = **2473** (dof 7); χ² lineárního trendu = 111 (dof 6). Konstantní model `B=3` je **rozhodně zamítnut** (χ²/dof ≈ 350).
- Robustnost: po vyřazení vysoce pákového bodu a=0.3 (n=5, větší CI) zůstává sklon −2.13 ± 0.07 (z = −32), χ² vs B=3 = 2342. Závěr se nemění.
- B(a) protíná hodnotu 3 při **a ≈ 0.75** — `D−1=3` je tedy jen jeden bod na spojité křivce, nikoli privilegovaná hodnota.

**B NENÍ konstanta.** Je to monotónně klesající, spojitá funkce Kerr spinu. (Křivka navíc není přesně lineární — χ²_lin=111/6 je stále vysoké, takže `B(a)` je hladká nelineární funkce; ale kvalitativní závěr „spojitá, ne konstantní" je neotřesitelný.)

### BTZ asymptotický kontrast (Ω~r⁻² vs Kerr Ω~r⁻³)

| geometrie | B ± SE | 95% CI | R² | Kerr B na témže spinu |
|-----------|--------|--------|----|----------------------|
| BTZ J=0.6 | **2.22 ± 0.02** | [2.03, 2.31] | 0.938 | Kerr a=0.6: 3.32 |
| BTZ J=0.9 | **2.12 ± 0.03** | [1.94, 2.23] | 0.968 | Kerr a=0.9: 2.67 |

BTZ body leží **pod** Kerr křivkou při stejné hodnotě rotačního parametru: gap = **−1.10** (J=0.6) a **−0.55** (J=0.9). Spin sám (Kerr křivka B(a)) tedy BTZ hodnoty **nevysvětluje** — při daném J by Kerr predikoval B≈3.3 resp. 2.7, naměřeno je 2.2 resp. 2.1. Rozdíl je konzistentní se změlčejším asymptotickým poklesem BTZ (`Ω~r⁻²` proti Kerr `Ω~r⁻³`): mělčejší `Ω(r)` dává mělčejší závislost `W_sr(Ω)`, tj. nižší B. Pozorovaný gap se navíc s rostoucím J zužuje (od −1.10 k −0.55), tj. obě křivky konvergují směrem k silné rotaci.

**Důležitý caveat k interpretaci:** J (BTZ) a a (Kerr) nejsou totožné fyzikální veličiny a rozsahy `Ω` se mezi geometriemi liší (Kerr `Ω∈[0.04,0.16]`, BTZ `Ω∈[0.09,0.43]`). „Stejný spin" je tedy jen vizuální zarovnání na grafu, ne fyzikální ekvivalence. Robustní tvrzení je slabší a poctivější: **B se liší jak napříč Kerr spiny, tak mezi Kerr a BTZ při srovnatelném rotačním parametru — žádná jediná dimenzionální konstanta nesedí na všechna data.**

---

## Verdikt H5g-5

**B je SPOJITÁ funkce strhávání rámce, NIKOLI dimenzionální konstanta `D−1=3`.**

1. **Spojitost v spinu (jádro důkazu):** B(a) klesá monotónně a vysoce signifikantně (sklon −2.20, z=−33.6) z 6.10 (a=0.3) na 2.54 (a=0.99). Konstantní model B=3 je zamítnut s χ²/dof ≈ 350.
2. **`D−1=3` vyvráceno jako univerzální hodnota:** křivka B(a) prochází 3 jen při jediném spinu (a≈0.75); 3 není atraktor ani plateau.
3. **Asymptotika hraje roli:** BTZ (mělčí `Ω~r⁻²`) dává B≈2.1–2.2, systematicky pod Kerr křivkou při srovnatelném J — gap nelze vysvětlit samotným spinem. To je důkaz dimenze-vs-asymptotiky **bez** nutnosti řešit well-definedness Kerr-AdS.

**Stretch cíl (Kerr-AdS):** NEPROVEDENO. Reflektující AdS hranice mění kauzální strukturu fixed-r řezu (odražené nulové paprsky, periodicita) a well-definedness SJ stavu s touto hranicí není v repu prověřena; vynucovat ji by riskovalo nekontrolovaný artefakt. BTZ kontrast (3D, Λ<0) poskytuje asymptotický signál bezpečně, takže Kerr-AdS bod vynecháváme — viz instrukce „SKIP it and say so".

---

## Implikace pro draft-01 §4.2

§4.2 dosud predikovala „mocninový exponent B≈3.8–4.2 (Kerr) / 1.7 (BTZ) lze porovnat s 4D Teukolskyho zesilovacím koeficientem". Tento výpočet predikci **upřesňuje i koriguje**:

1. **Číselná korekce:** spolehlivý (neomezený) B je nižší než dříve uváděné omezené hodnoty — Kerr B klesá z 3.70 (a=0.5) na 2.54 (a=0.99); a=0.6→3.32, a=0.9→2.67 (NE 4.23/3.82). §4.2 by měla uvádět tyto neomezené hodnoty s CI, ne staré bounded.
2. **Kvalitativní zostření:** B není konstanta — je to klesající funkce spinu. Falsifikovatelná predikce pro 4D Teukolsky se mění z „porovnej jediné B" na „porovnej **trend** `dB/da<0` a polohu BTZ pod Kerr křivkou".
3. **Fyzikální obsah:** spojitá závislost B na strhávání + posun BTZ podporují interpretaci, že B kóduje **lokální geometrii klínu** (jak rychle `Ω(r)` roste vůči `r`), ne pouhý dimenzionální počet. To je v souladu s F-017/F-018 (řízení přes `Ω(r)`) a s toy modelem F-013 (sklon klínu = shear).

---

## Limity

- **2D bezhmotný skalár, fixed-r řez** (Strategie II z VYPOCET-08); 4D Teukolsky bude kvantitativně odlišný. Závěr „B spojité, ne konstantní" je vlastnost tohoto 2D SJ konstruktu.
- **B(a) není přesně lineární** (χ²_lin=111/6); reportovaný sklon je trendová statistika k odlišení od konstanty, ne tvrzení o přesné funkční formě.
- **a=0.3 jen 5 bodů** (W_sr=0 na r=2.80 pod rozlišením `(71×71)` mřížky při slabém spinu); má větší CI a páku. Závěr je robustní i bez něj.
- **J(BTZ) ≠ a(Kerr)** a `Ω`-rozsahy se liší — BTZ–Kerr srovnání je při srovnatelném rotačním parametru, ne při fyzikální ekvivalenci (viz caveat výše).
- **5 seedů, N=1600** — zděděné limity VYPOCET-14; konvergence v N neprovedena.
- **Kerr-AdS bod vynechán** (well-definedness AdS reflektující hranice neprověřena).

---

## Citace

- **1611.10281** — Sorkin, Yazdi (`G_R=½C`, SJ, `iΔ`, W = kladná část)
- **VYPOCET-14** (sj-threshold-scan) — Model S, omezený B, A=100 artefakt
- **VYPOCET-15** (sj-far-zone) — log-log diskriminant, `corr_loglog(S)=0.9992`
- **VYPOCET-10** (sj-eigenvector-superradiance) — toy model klínu/shearu (F-013)
- AIC/BIC — Akaike 1974, Schwarz 1978

---

## Vstup pro findings.json

Navrženo jako **F-030** (viz `findingProposal` v běhovém výstupu): H5g-5 uzavřeno — B je spojitá funkce strhávání (sklon −2.20, z=−33.6), `D−1=3` zamítnuto, BTZ pod Kerr křivkou. Status `confirmed` pro 2D SJ konstrukt, s caveatem o 2D/J≠a/nelinearitě.
