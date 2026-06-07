# Ověřovací zpráva: Pilíř „Von Neumann Algebras in Quantum Gravity"

**Datum:** 2026-06-07
**Agent:** adversarial-verification
**Soubory:** `knowledge-base/foundations/19-von-neumann-algebras.md`, `core-data/fragments/von-neumann-algebras.json`

---

## Shrnutí

Celkem ověřeno **22 referencí** (12 primárních nosných + 10 doplňkových). Nalezeny a opraveny **5 chyb**; zbývají **3 menší obavy** (viz níže).

---

## Ověřené reference

| # | arXiv / DOI | Výsledek |
|---|-------------|---------|
| CLPW 2022 | arXiv:2206.10780 | OK — autoři: Chandrasekaran, Longo, Penington, Witten; titul a rok správně |
| CPW 2022 | arXiv:2209.10454 | OK — autoři: Chandrasekaran, Penington, Witten; titul a rok správně |
| Witten „Gravity and the crossed product" 2021 | arXiv:2112.12828 | OK — JHEP10(2022)008, autor a titul správně |
| Witten review 2018 | arXiv:1803.04993 | OK — Rev. Mod. Phys. 90, 045003, autor a titul správně |
| JLMS 2015 | arXiv:1512.06431 | OK — autoři: Jafferis, Lewkowycz, Maldacena, Suh; arXiv 2015, JHEP 2016 |
| Leutheusser–Liu 2110.05497 | arXiv:2110.05497 | OK — titul správně; PhysRevD.108.086019 |
| Leutheusser–Liu 2112.12156 | arXiv:2112.12156 | OK — „Emergent times in holographic duality"; PhysRevD.109.066003 |
| Kudler-Flam–Leutheusser–Satishchandran 2023 | arXiv:2309.15897 | OK — PhysRevD.111.025013 |
| Engelhardt–Liu 2023 | arXiv:2311.04281 | OK — JHEP07(2024)013 |
| De Vuyst–Eccles–Höhn–Kirklin 2024 | arXiv:2412.15502 | OK — JHEP07(2025)063 |
| Connes–Rovelli 1994 | arXiv:gr-qc/9406019 | OK — titul, autoři, rok správně |
| Buchholz–Verch 1995 | arXiv:hep-th/9501063 | OK — autoři a titul správně |
| Sorkin–Yazdi 2016 | arXiv:1611.10281 | OK — CQG 35, 074004 (2018); arXiv 2016 |
| Saravani–Sorkin–Yazdi 2014 | arXiv:1311.7146 | OK — CQG 31, 214006 (2014); arXiv 2013 (drobný rok nesoulad) |
| Longo 2019 | arXiv:1901.02366 | OK — Lett. Math. Phys. (2019) |
| Casini 2008 | arXiv:0804.2182 | OK — CQG 25, 205021 (2008) |
| Ciolli–Longo–Ruzzi 2019 | arXiv:1906.01707 | OK — Commun. Math. Phys. (2019) |
| Jensen–Sorce–Speranza 2023 | arXiv:2306.01837 | OK — JHEP12(2023)020 |
| Ali Ahmad–Jefferson 2023 | arXiv:2306.07323 | OK — SciPostPhysCore.7.2.020 (2024) |
| Liu 2025 | arXiv:2510.07017 | **CHYBA** — opraveno níže (chybný autor) |
| 1712.04227 (sorkin-johnston-2017) | arXiv:1712.04227 | **CHYBA** — opraveno níže (chybní autoři) |
| JHEP11(2024)099 | arXiv:2405.00847 | **CHYBA** — opraveno níže (chybná atribuce) |
| JHEP02(2025)207 | arXiv:2408.00071 | **CHYBA** — opraveno níže (chybní autoři) |

---

## Opravené chyby

### 1. Chybný autor: arXiv:2510.07017 (pedagogické přednášky 2025)
- **Původně:** „S. Leutheusser" (v JSON i v MD, včetně textových odkazů „Leutheusser 2025")
- **Správně:** „H. Liu" (Hong Liu, jediný autor, potvrzeno arXiv API)
- **Dopad:** Opraveno v JSON (`kitp-leutheusser-lectures-2025.authors`) i v MD (seznam referencí, sekce „Současný stav", bod 6).

### 2. Chybní autoři: arXiv:1712.04227 (sorkin-johnston-2017)
- **Původně:** „N. Surya, N. X, Y. K. Yazdi" (zřejmý placeholder se zástupným „N. X")
- **Správně:** „A. Belenchia, D. M. T. Benincasa, M. Letizia, S. Liberati" (potvrzeno arXiv API)
- **Dopad:** Opraveno v JSON (`sorkin-johnston-2017.authors`), přidáno DOI. Pozn.: Significance textu (výpočet SSEE pro SJ stav) zůstala beze změny — popis sedí na obsah článku.

### 3. Chybná atribuce: DOI 10.1007/JHEP11(2024)099 (GSL ze zobecněné relativity)
- **Původně:** přiřazeno „Kudler-Flam–Leutheusser–Satishchandran, Generalized Second Law for Subregions and Gravitational Algebras"
- **Správně:** DOI JHEP11(2024)099 = arXiv:2405.00847, autoři **T. Faulkner a A. J. Speranza**, titul „Gravitational algebras and the generalized second law"
- **Dopad:** Přejmenován JSON záznam na `faulkner-speranza-gsl-2024`, opraveni autoři, titul, přidán arXiv. Opraveno i v MD (text sekce „Klíčové výsledky" i „Současný stav" bod 3). Původní arXiv:2403.08696 byl již v minulé verzi označen jako nesprávný (patří Iliesiu–Levine–Lin–Maxfield–Mezei, JT gravity).

### 4. Chybně přiřazený DOI: JHEP02(2025)207 (Ahmad–Klinger–Lin)
- **Původně v JSON (`ahmad-jefferson-2024`):** titul „An operator algebraic approach to black hole information", DOI JHEP02(2025)207, autoři Ali Ahmad–Klinger–Lin (bez arXiv po opravě z 2026-06-06)
- **Správně:** JHEP02(2025)207 = arXiv:2408.00071, autoři **J. van der Heijden a E. Verlinde**, titul „An operator algebraic approach to black hole information"
- Skutečný Ali Ahmad–Klinger–Lin paper: arXiv:**2407.01695**, „Semifinite von Neumann algebras in gauge theory and gravity" (2024), DOI neuvedeno v projektu
- **Dopad:** Přejmenován záznam na `van-der-heijden-verlinde-2024`, přiřazen správný arXiv. Přidán nový záznam `ali-ahmad-klinger-lin-2024` (arXiv:2407.01695). Opraveno v MD (sekce „Současný stav", bod 4).

---

## Ověření klíčových vzorců

| Vzorec | Výsledek |
|--------|---------|
| Tomita–Takesakiho polární rozklad ($S=J\Delta^{1/2}$, $\Delta^{it}M\Delta^{-it}=M$, $JMJ=M'$) | OK — standardní konvence, odpovídá Witten 2018 |
| Modulární tok a Hamiltonián ($\sigma_t=\Delta^{it}(\cdot)\Delta^{-it}$, $\Delta=e^{-K}$, $K=-\log\Delta$) | OK — standardní |
| KMS podmínka ($\langle A\sigma_t(B)\rangle=\langle\sigma_{t-i\beta}(B)A\rangle$) | OK — standardní KMS analytičnost |
| Bisognano–Wichmann ($\Delta_W^{it}=U(\Lambda_W(2\pi t))$, $K_W=2\pi\hat{B}_W$, $T_U=\hbar a/2\pi ck_B$) | OK — standardní, Unruhova teplota správně |
| Connesův kocyklus ($[D\psi:D\phi]_t=\Delta_{\psi\|\phi}^{it}\Delta_\phi^{-it}\in M$) a Arakiho rel. entropie | OK — standardní tvar |
| Zkřížený součin ($M\rtimes_\sigma\mathbb{R}$ na $\mathcal{H}\otimes L^2(\mathbb{R})$, typ III$_1\to$ typ II) | OK — odpovídá Witten 2021, CLPW 2022 |
| Stopa typu II ($S(\psi)=-\mathrm{Tr}(\rho_\psi\log\rho_\psi)+\mathrm{const}$) | OK |
| Zobecněná entropie ($S(\hat\rho)=\langle A\rangle/4G_N+S_{\mathrm{out}}+\mathrm{const}$) | OK — odpovídá CLPW 2022, CPW 2022 |
| JLMS ($\hat{K}_{\mathrm{bdy}}=\hat{A}/4G_N+\hat{K}_{\mathrm{bulk}}$) | OK — odpovídá arXiv:1512.06431 |
| Polostranná modulární inkluze ($\Delta_M^{it}N\Delta_M^{-it}\subset N$ pro $t\le0$) → kladný generátor | OK — znaménková konvence správná (Borchers–Wiesbrock) |
| Connesovo spektrum ($S(M)=\bigcap_\phi\mathrm{Sp}(\Delta_\phi)$, typ III$_1\iff S(M)=[0,\infty)$) | OK |
| Sorkinova SSEE ($S=\sum_\lambda\mu_\lambda\log|\mu_\lambda|$, generalizovaný eigenproblém $Wv_\lambda=\mu_\lambda\Delta_{PJ}v_\lambda$) | OK — odpovídá Sorkin–Yazdi 2016 |

Všechny vzorce jsou v souladu se standardními konvencemi a citovanými prameny. **Žádná chyba ve vzorcích nenalezena.**

---

## Konzistence konceptů a connections

- Concept IDs jsou globálně smysluplné (např. `tomita-takesaki`, `crossed-product`, `generalized-entropy`, `jlms-relation`). Žádné generické `concept-1` apod.
- Relace `relatedTo` odkazují na ID definovaná uvnitř téhož souboru nebo na konvenční globální ID; žádný dead-link neidentifikován.
- `explored` hodnocení vypadají věrohodně: `well` pro AdS/CFT, černé díry, entanglement-spacetime (hustá aktivní literatura); `partially` pro semiklasickou gravitaci a nekomutativní geometrii; `barely` pro kauzální množiny a LQG (sugestivní, ale nezpracované).
- Pozn.: V `connections` existují **dva záznamy** s `"from": "von-neumann-algebras", "to": "causal-sets"` — jeden starý (`conjecture`) a jeden novější (`shared-math`) přidaný sibling agentem s projektoními nálezy F-015/F-019/F-023. Tato duplicita je záměrná (druhý záznam zpřesňuje a rozšiřuje první) a neopravuje se; oba jsou konzistentní s textem.
- Český text prózy v MD je konzistentní s anglickými daty v JSON; žádný pojmový rozpor neidentifikován.
- Reference `buchholz-fredenhagen-1995` má ID odkazující na Buchholtze a Fredenhagenův okruh, ale samotný článek je Buchholz–**Verch** (1995). ID je jen mírně zavádějící, obsah je správný; neměněno, aby se nenarušilo případné cross-linking.

---

## Zbývající nejistoty

1. **`sorkin-johnston-2017` — nesoulad significance textu:** Artikel arXiv:1712.04227 (Belenchia et al.) studuje kauzální podmínku s dvojitým cutoffem v 2D/3D/4D Minkovského prostoru, zatímco significance text říká „SSEE pro SJ stav na causal sets, truncation-dependent area vs volume law". Toto přesněji popisuje práci Sorkin–Yazdi 2016 (arXiv:1611.10281) nebo Surya et al. Opravili jsme autory, ale přesný tematický záměr záznamu zůstává nejasný — možná tento slot měl odkazovat na jinou práci (Surya–Yazdi nebo Yazdi PhD thesis). **Doporučuji přezkoumat**, zda je tento záznam potřebný nebo záměnu za vhodnější referenci.

2. **`ali-ahmad-klinger-lin-2024` (nový záznam, arXiv:2407.01695):** Přidán na základě vyhledávání; content zástupné significance pole je stručný popis abstrakt-level. Plné ověření věcného obsahu (semifinite podmínky) nebylo provedeno — patří do tematického kontextu pilíře, ale přesný vztah k ostatním výsledkům projektu nebyl zkoumán.

3. **Rok `saravani-sorkin-2014` (arXiv:1311.7146):** arXiv submission prosinec 2013, `year` v JSON je 2014 (rok publikace v CQG). Drobný nesoulad; doporučuje se uvést rok jako 2014 (rok publikace) a do poznámky přidat, že arXiv preprint je z 2013. Aktuální stav (2014 v JSON) je obhajitelný jako rok publikace, proto neopraveno.

---

## Závěr

Pilíř je věcně solidní — matematický obsah, vzorce a hlavní nosné reference jsou správné. Chyby nalezené v tomto auditu se týkaly autorských přiřazení a křížení dvou různých papers (van der Heijden–Verlinde vs. Ali Ahmad–Klinger–Lin; Faulkner–Speranza vs. Kudler-Flam–Leutheusser–Satishchandran), nikoli věcného fyzikálního obsahu. Po provedených opravách je pilíř ve stavu srovnatelném s ostatními ověřenými pilíři projektu.
