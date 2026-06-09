# Syntéza 03: Mapa po druhém výzkumném oblouku (kola 7–20, 2026-06-08)

> Sequel `SYNTEZA-02.md` (která mapovala kola 1–6, nálezy F-001..F-017). Tento dokument SYNTEZU-02 nemodifikuje. Vstupy: `core-data/findings.json` (**39 nálezů F-001..F-039**), `core-data/connections.json` (298 hran, 114 „barely"), nová CAS validační dráha (`verification/cas/`, 52/53 CAS-ověřitelných vzorců potvrzeno), tří-rolová agentní smyčka (`.claude/agents/`). Cíl: zaznamenat, co se stalo s pěti vlajkovými liniemi SYNTEZY-02 během druhého oblouku, a — poctivě — že **dominantní rys tohoto oblouku jsou ostře charakterizované NEGATIVY**: program systematicky pohřbil vlastní nejodvážnější nároky a nechal úzké, betonové jádro.

---

## 0. Jednou větou

Druhý oblouk **zesílil 2D causal-set/von-Neumann jádro a −18/11 identitu na publikovatelnou pevnost, ale narazil na tvrdou zeď ve všech čtyřech ambiciózních směrech** (4D entropicko-plošný zákon, most −18/11→entanglement, NCG↔semiklasika jako teplota, dimenzní konstanta B) — a každou zeď zmapoval přesně, nezamlčel. Through-line SYNTEZY-02 („vlastnosti = odpovědi na otázky") dostal dvě nové osy: **dimenze je reálný diskriminátor, ne detail**, a **variance vs. střední hodnota je rozlišovací osa**.

---

## 1. Co se stalo s pěti vlajkovými liniemi SYNTEZY-02

SYNTEZA-02 nechala pět vlajkových linií a doporučila „těžiště compute na 4D extenzi causal-set/von-Neumann fronty". Oblouk to přesně udělal — a výsledek je z velké části **negativní na ambiciózní straně, pozitivní na konsolidační**.

### 1.1 Linie A (SJ × horizonty / rotace) — UZAVŘENA s ostrou predikcí

SYNTEZA-02 nechala otevřenou Kerr `a=0.6` ambiguitu a marginální Model E/S spor. Oblouk ji **uzavřel** (F-018, VYPOCET-15: ΔAIC=+3894 pro Model S, far-zone scan r=5–20M). Pak povýšil draft-01 predikci z „Ω-zákon platí" na **kvantitativní tvrzení o exponentu**: F-030 ukázal, že $B$ v $W_{sr}\sim\Omega(r)^B$ je **SPOJITÁ klesající funkce strhávání rámce**, NE dimenzní konstanta $D{-}1{=}3$. Spolehlivý (unbounded log-log) $B(a)$ klesá $6.10\,(a{=}0.3)\to2.54\,(a{=}0.99)$, sklon $dB/da=-2.20\pm0.07$ ($z{=}-33.6$); konstantní model $B{=}3$ rozhodně zamítnut ($\chi^2/\mathrm{dof}\sim350$), křivka protíná 3 jen u jediného spinu $a\approx0.75$. BTZ ($\Omega\sim r^{-2}$) systematicky **pod** Kerr křivkou ($\Omega\sim r^{-3}$) → evidence role asymptotiky bez Kerr-AdS. **Negativ uvnitř:** původní naděje „$B=D{-}1$" je zabita. Ale linie A je tím nejhustší vlastní datový svazek projektu (F-009/013/017/018/030) — a teprve tímto obloukem se dostala do grafu (hrana `semiclassical-gravity↔causal-sets` povýšena barely→partially, kolo 17).

### 1.2 Linie B (III₁→II / typový přechod) — POSÍLENA na 3/3, ale 4D area-zákon POHŘBEN

SYNTEZA-02 měla F-015 jako „2/3 proxy, 2D". Oblouk:
- **F-019**: 4D slab dává **3/3 proxy** (N^{3/4} area-law rank jako operativní regulátor) — přechod lifted do 4D.
- **F-032**: 2D-diamant proxy3 (central-sequences/self-averaging), dosud nesignifikantní při 5–8 seedech, **se stává signifikantním při ≥30 seedech** (8 seedů $t{=}1.48$ → 50 seedů $t{=}3.25$, CI vylučuje 0) — 2D verdikt **upgrade 2/3 → 3/3**. Poctivé: je to genuinní seed-count efekt na původním gridu, ne grid-artefakt.
- **F-027**: tracialní II₁ probe zůstává **null** i při 6× hustotě — identifikace II₁ stojí na obsah-saturaci, ne na přímém tracialním podpisu (κ-truncace systematicky vyřezává low-eps módy).
- **F-023→F-028→F-029 (de Sitter konvergence A×B):** capstone kola 9 — diskrétní SJ sonda **vidí** CLPW distinkci II₁ vs. II_∞ na dS statické záplatě (obsah saturuje na dS, roste na ploché kontrole). 2D entropy-cap je **kvantitativní area-zákon**: $S_{cap}=A_{horizon}/(c\cdot G)$, $c\approx7.57$ KONSTANTNÍ přes 5× hustotu a 3.6× velikost záplaty (F-029: $R=0.130\pm0.0039$, CV 3 %), cross-HW reprodukováno — **publikovatelně silné**. Anti-kruhovost respektována (ε z nezávislého F-006 fixováno před měřením). **Silná forma $c{=}4$ vyvrácena** ($c\approx7.57\ne4$).

**Ale 4D entropicko-plošný zákon je GENUINNĚ NEPŘÍTOMEN — pohřben TŘEMI nezávislými způsoby:**
- **F-031 (mean):** 4D molekulová „plocha" $A_{mol}\sim\rho^{1.77}$ byl artefakt počítání linků přes **kodim-1 světočáru-tubus** (ne kodim-2 entanglement plochu); opravený codim-2 Dou-Sorkin primitiv (`toe.causet.horizon_molecules_codim2`) obnovuje vlastní-plošné $\rho^{0.49}$, ALE $S_{full}\sim\rho^{1.0}$ (objemově) → poměr nutně driftuje → ŽÁDNÝ rho-invariantní area-zákon. Ve 2D oba shodou $\sim\rho^1$ (horizont = bod), takže $R^{2D}$ konstantní; ve 4D degenerace mizí.
- **F-037 (konformní caveat vyřešen):** konformně-vázaný 4D skalár ($\xi{=}1/6$, $m^2_{eff}=\xi R=2/\ell^2$) dává $R'$ drift $\rho^{+0.39}$ **IDENTICKY** jako $\xi{=}0$ ($S_{full}$ se mění o $\le0.05\%$) → 4D nepřítomnost **NENÍ** konformně-vahový artefakt, je to robustní fyzika.
- **F-038 (variance):** order-by-disorder fluktuace molekulového počtu dává $\mathrm{Var}(N_{mol})\sim\rho^{0.656}$ (CI95 vylučuje plochu $\rho^{0.5}$ i objem $\rho^{1.0}$), super-Poissonovský Fano $3.7\to5.3$ (korelované near-null straddling linky) → area-zákon chybí i na varianci.

**Závěr linie B:** 2D je publikovatelně silné (3/3 proxy + kvantitativní area-zákon), **4D je dimenzně jiné — area-zákon $S\propto A_{proper}$ tam genuinně neexistuje** (mean / konformní / variance, vše vyloučeno). Dimenze není detail.

### 1.3 NCG index jádro (−18/11) — připojeno k anomálii, NEDOSÁHNE do ostatních linií

SYNTEZA-02 měla −18/11 jako „jedinou betonovou hranu, uzamčenou identitu, stojící stranou". Oblouk se ji pokusil **zapojit** — a poctivě zjistil hranice:
- **F-020:** Λ-sektor (a₀/a₂) NEMÁ sesterskou identitu k −18/11 (cross-order, scheme-závislé) → H4g-3 zabito. Index-ochrana je výlučná vlastnost a₄ poměru.
- **Most do linie B (F-039, hypotéza H-B):** trace-anomální náboje $(a,c)$ řídí univerzální EE členy (Casini-Huerta-Myers / Solodukhin); měříme univerzální koeficient $c_{EE}\approx7.56$. **Ostrý negativ:** $c_{EE}$ se neshoduje s žádným pre-registrovaným anomálním racionálem (skalární cíl $-3$ míjí o 152 %, $-18/11$ o 362 %) → $c_{EE}$ je **GEOMETRICKÝ** (κ-cutoffem řízený), ne anomální náboj. Index jádro se přes entanglement entropii linie B **NEDOTÝKÁ**.
- **Most na semiklasiku přes tepelný čas (F-033/F-034/F-036):** SJ modulární tok JE pravý jednoteplotní KMS tok ($\beta_{KMS}=1$) s ρ-invariantní boostovou geometrií (sklon $\sim29$, $R^2{=}0.95$, kontroly čistě selhávají) — ALE $\beta_{KMS}=1$ je **tautologie** Tomita-Takesaki, a absolutní Unruh $2\pi$ se z geometrie-fixované normalizace **neobnovuje** (ratio 0.79, off o 52 %); Connesova vzdálenost surogátního Diraca $D_K=\mathrm{sgn}(K)\sqrt{|K|}$ **nesleduje** kauzální vzdálenost (korelace 0.32, $R^2{=}0.10$, 16 párů). Most NCG↔SJ je most **STRUKTURY (boostová geometrie), NE TEPLOTY ani METRIKY**. Příčina diagnostikována: surogátní Dirac v jednotkách $\varepsilon=\ln[\mu/(\mu-1)]$ log-komprimuje a nenese chirální gradování $\gamma_5$.
- **Graf (kolo 17/19):** −18/11 = $c/(-a)$ je doslova chybějící most mezi NCG spektrální akcí a trace-anomaly clusterem (ten byl v grafu **ostrov**). Oblouk nakreslil **6 PROVEN/established hran** (2× `well`: `spectral-action↔trace-anomaly`, `a-theorem↔entanglement-entropy`). −18/11 **přestalo být izolovaný uzel** — ale zůstává „question-independent index core", protože kvantitativně nedosáhne do žádné jiné linie.

### 1.4 Λ linie — REVIVAL na ose variance

SYNTEZA-02 měla naivní $\Lambda\sim1/\sqrt V$ jako „silná forma zabita" (F-005, 140× prefaktor). Oblouk ji **oživil na ose, kterou F-005 netestoval** (F-035): Poissonův shot-noise počtu prostoročasových atomů přežívá ve VARIANCE formě — Fano $\mathrm{Var}(N)/\langle N\rangle = 0.9986$ (0.13σ od 1, přesný Poisson), $\delta\Lambda\sim\sqrt{\mathrm{Var}(N)}/V\sim V^{-0.48}$ (konzistentní s $V^{-1/2}\sim H^2$), a $\mathrm{Var}(N)$ je **boost-invariantní** (z=0.70) zatímco rigidní mřížka má boost-závislý počet (kontrast 5.13×). **Variancní/boost-kovariantní osa žije; sdílený mean-prefaktor (F-005) zůstává mrtvý.** Nutná, ne postačující podmínka pro everpresent-Λ.

### 1.5 Spektrální dimenze / probe (F-001/F-002) — NEDOTČENO, ale nově propojeno

Tato linie nedostala nový výpočet, ale link-prediction (kolo 17) odhalil vysoce-jistotný kandidát `noncommutative-geometry↔spectral-dimension` (score 0.896, týž $\mathrm{Tr}\,e^{-\sigma D^2}$) → hrana nakreslena (kolo 19). Spojuje a₄ koeficienty s $d_s$ flow přes sdílený heat-kernel — otevřená kvantitativní fronta.

---

## 2. Aktualizovaná mapa — nové data-hrany druhého oblouku

```mermaid
graph LR
  NCG[Nekomut. geometrie]
  EMG[Emergentní gravita]
  TA[trace-anomaly cluster]
  SD[spectral-dimension]
  ENT[Entanglement]
  CS[Kauzální množiny]
  VNA[von Neumann algebry]
  SCG[Semiklasická gravita]
  BH[ČD & informace]
  QC[Kvant. kosmologie]
  CC[Λ-fluktuace]

  %% ===== nové PROVEN hrany kolem -18/11 (kolo 17/19) =====
  NCG ==>|F-003/F-014 well: a4 = -18/11 = c/(-a)| TA
  TA  ==>|well: a = sférická EE CHM / Solodukhin| ENT
  NCG -.->|barely: týž Tr e^-sigmaD^2, ML 0.896| SD

  %% ===== datové verdikty druhého oblouku =====
  CS  ==o|F-029 2D: area-zákon c~7.57 KONSTANTNÍ| BH
  CS  ==x|F-031/F-037/F-038: 4D area-zákon GENUINNĚ ABSENT 3x| BH
  CS  ==>|F-032: proxy3 3/3, F-019 4D slab| VNA
  CS  ==o|F-030: B(a) SPOJITÁ, ne D-1| SCG
  NCG ==x|F-039: c_EE geometrický, NEdosáhne| ENT
  NCG ==o|F-034: KMS tok ano, ale most STRUKTURY ne teploty| SCG
  CS  ==>|F-035: Lambda shot-noise variance PŘEŽÍVÁ boost-inv| CC
  CS  ==x|F-005: Lambda mean-prefaktor mrtvý| QC
```

Legenda: `==>` posiluje/zakládá · `==o` přerámuje/podmíněně · `==x` zabíjí/vylučuje.

**Komentář.** Druhý oblouk **nepřidal žádnou novou betonovou pozitivní cross-pilíř hranu** srovnatelnou s −18/11 nebo CS↔VNA. Místo toho: (a) **zostřil** existující 2D hrany na publikovatelnou pevnost; (b) **vyloučil** čtyři ambiciózní 4D/most hrany s diagnózou PROČ; (c) **dokreslil** −18/11 do anomálního clusteru (proven, ale uzavřené). Mapa je teď hustší v dokázaných hranách a poctivější v negativech.

---

## 3. Through-line — dvě nové osy

SYNTEZA-02: „vlastnosti prostoročasu jsou **odpovědi na otázky** (probe, observer, geometrie regionu, regularita stavu), ne atributy." Druhý oblouk přidává:

**Osa I — dimenze je reálný diskriminátor, ne detail.** 2D area-zákon je konstantní (F-029), 4D genuinně chybí (F-031/037/038). Rohový mechanismus je 2D-only (F-024/F-026, codim-2 spoj 4D nerestoruje). Exponent $B$ je spojitá funkce, ne $D{-}1$ (F-030). Korespondence II₁/II_∞ se lifne do 4D (F-019/F-025), ale kvantitativní A/4 ne. **Co platí ve 2D nemusí platit ve 4D — a rozdíl je fyzika, ne artefakt** (konformní caveat explicitně vyloučen, F-037).

**Osa II — variance vs. střední hodnota je rozlišovací osa.** Λ shot-noise: mean mrtvý (F-005), variance žije a je boost-kovariantní (F-035). Entropie: mean nedá 4D area-zákon (F-031), ani variance ne (F-038, super-Poissonovské korelace). proxy3 self-averaging je variancní signatura faktoriality (F-032). **Otázka „je to v průměru, nebo ve fluktuaci?" odděluje, co přežije.**

**Metanález o metodě.** Druhý oblouk **vyzrál nástroj poctivosti**: tří-rolová agentní smyčka (exploratory návrh → computational-physicist výpočet → adversarial-verifier audit), kde verifier opakovaně přebil optimismus (chytil tautologii F-034/F-036, p-hacking riziko F-039, provenance mezeru kola 14, a CAS revize chytila reálný **Myrheim-Meyer factor-2 bug** v `formulas.json`). Co přežilo tímto filtrem, přežilo opakované pokusy o popravu — a stejně tak co padlo, padlo čistě, s diagnózou.

---

## 4. Zbývající bílá místa — přeřazeno po negativech

Po druhém oblouku se relativní cena front změnila. Co je teď nejvyšší ROI:

**Sestoupilo / uzavřeno (NElovit):**
- **4D entropicko-plošný zákon** přes mean/konformní/variance — VYČERPÁNO (F-031/037/038). Jediná zbylá cesta je *přesný zakřivený 4D dS propagátor* (mimo current machinery), ne další sonda na ploché-kauzální + dS-sech² konstrukci.
- **−18/11 → entanglement entropie** přes diskrétní $c_{EE}$ — ZAVŘENO (F-039, geometrický ne anomální).
- **NCG↔semiklasika jako absolutní Unruh teplota** přes surogátní Dirac — ZAVŘENO (F-036, tautologie/log-komprese).

**Drží / nově otevřeno (lovit):**
1. **NCG↔semiklasika přes NON-surogátní Dirac** — jediná zbylá cesta k netautologickému Unruh $2\pi$: Diracův operátor z geometrického Killingova boostu $\xi=x\partial_t+t\partial_x$ s chirálním gradováním $\gamma_5$, ne z $\varepsilon$-spektra. *Nová mašinérie, vysoké riziko, ale jediná čistá.*
2. **NCG↔spectral-dimension** (ML 0.896, F-001/F-002): kvantitativní vztah $a_4$ koeficientů a $d_s$ flow přes sdílený heat-kernel. *Odpoledne→sparse.*
3. **BD path integral → AS fixní bod** (SYNTEZA-02 žebříček #1, stále nedotčeno): F-012 α-drift varování trvá. *Sparse, vysoké riziko inconclusive.*
4. **Λ shot-noise → plný řetězec $\delta N\to\delta\Lambda$** (F-035 dal nutnou, ne postačující podmínku): Sorkinova $\Lambda\leftrightarrow V$ konjugace je sama hypotéza k testu.
5. **Twistor↔entanglement pozitivita** (SYNTEZA-02 #5, stále read+think, diverzifikace).

---

## 5. Strategický výhled — 7. generace

Druhý oblouk vyčerpal „compute na 4D causal-set frontě" doporučení SYNTEZY-02 (výsledek: 2D silné, 4D vyloučeno). Těžiště dalších kol se posouvá od **další numeriky** k **dokumentaci a publikaci toho, co přežilo**, plus selektivnímu řízenému risku:

**WRITE (zralé / dluh):**
- **Draft-02 (−18/11)** zůstává nejsilnější, uzavřený; navíc teď CAS-nezávisle validovaný (Wolfram).
- **Draft-01 (SJ rotace)** dostal F-030 spojitý $B(a)$ — predikce zostřena na „trend $dB/da<0$ + BTZ pozice".
- **Draft-04 (typový přechod)** má teď 2D 3/3 (F-032) a poctivý 4D area-zákon negativ (F-031/037/038).
- **Draft-06 kandidát: „mapa negativů"** — F-031/036/038/039 jako koherentní příběh o tom, kde diskrétní program naráží (dimenze, surogát, mean-vs-variance). Negativní letter má hodnotu.
- **Headline rozhodnutí u abstraktů** (draft-01/04, flaggedForHuman z kola 17) — čeká na lidskou redakci.

**COMPUTE (selektivně, řízený risk):**
- non-surogátní geometrický-boost Dirac (#1) — jediná čistá cesta k netautologickému NCG↔semiklasika mostu.
- NCG↔spectral-dimension (#2) — levné, vysoká novost.

**READ (diverzifikace):** twistor↔entanglement (#5), mimo causal-set/NCG linii.

**Doporučená sekvence:** těžiště na **konsolidaci a dokumentaci** (SYNTEZA-03 sama, draft-06 mapa negativů, headline rozhodnutí), ne na další 4D numeriku (vyčerpáno); selektivní compute jen na #1 (geometrický Dirac) a #2 (NCG↔$d_s$); zbytek read+think.

---

### 5řádkové shrnutí (CZ)

1. Druhý oblouk (kola 7–20, F-018..F-039) **zostřil 2D causal-set/von-Neumann jádro a −18/11 na publikovatelnou pevnost** (2D dS area-zákon $c\approx7.57$ konstantní, proxy3 3/3, $B(a)$ spojitá, CAS-validace 52/53), ale **narazil na tvrdou zeď ve všech čtyřech ambiciózních směrech**.
2. **4D entropicko-plošný zákon je genuinně NEPŘÍTOMEN** — pohřben třemi nezávislými způsoby (mean F-031, konformní F-037, variance F-038); dimenze je reálný diskriminátor, ne detail.
3. **−18/11 zůstává question-independent index core:** připojeno k anomálnímu clusteru v grafu (6 proven hran), ale kvantitativně NEDOSÁHNE do entanglement linie (F-039 geometrický $c_{EE}$) ani se nestane absolutní Unruh teplotou (F-036 tautologie); most NCG↔SJ je most struktury, ne teploty.
4. **Λ linie ožila na ose variance** (F-035 boost-invariantní Poissonův shot-noise), kde F-005 zabil jen mean — nová through-line osa „variance vs. mean".
5. **Výhled 7. generace:** těžiště na konsolidaci/dokumentaci (draft-06 „mapa negativů", headline rozhodnutí), ne na další 4D numeriku (vyčerpáno); selektivní compute jen na non-surogátní geometrický Dirac a NCG↔$d_s$.

---

*Anchory: `core-data/findings.json` (F-018..F-039); `knowledge-base/SYNTEZA-02.md` (předchozí oblouk); `BRAINSTORM-05.md`/`BRAINSTORM-06.md` (hypotézy H5g-*/H6g-*); `LOV-18-11-overlaps.md` (−18/11 hon); `verification/cas/` (CAS validace, Myrheim-Meyer fix); `VYPOCET-15..36`; `reports/2026-06-08-cas-formula-revision.md`. Klíčová literatura (vše repo-present): CLPW 2206.10780, Sorkin-Yazdi 1712.04227/1611.10281, Connes-Rovelli gr-qc/9406019, Casini-Huerta 0905.2562, Benincasa-Dowker 1001.2725, Chamseddine-Connes hep-th/9606001, Meyer 1988 (Myrheim-Meyer).*
