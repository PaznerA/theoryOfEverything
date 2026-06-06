# Verifikační zpráva — Kauzální dynamické triangulace (CDT)

**Datum verifikace:** 2026-06-05
**Verifikované soubory:**
- Česká próza: `knowledge-base/approaches/04-causal-dynamical-triangulations.md`
- Anglický JSON fragment: `core-data/fragments/causal-dynamical-triangulations.json`

**Verdikt:** JSON byl platný již na vstupu (žádná oprava syntaxe nebyla nutná) a po všech editacích zůstává platný (ověřeno `json.load`). Většina obsahu je přesná; nalezeno a opraveno bylo několik chyb v autorství referencí, jeden chybný název práce, jeden nadhodnocený význam a drobné textové artefakty.

---

## Co bylo zkontrolováno

### Audit referencí (ověřeno 24+ referencí proti arXiv / DOI / nezávislým zdrojům)
Ověřoval jsem rozlišení arXiv ID a shodu názvu + autorů + roku. Prioritně byly kontrolovány reference podpírající nejsilnější tvrzení a nejnovější (2024–2026) práce, u nichž je riziko fabulace nejvyšší.

Korektní reference (ID rozlišuje, název/autoři/rok sedí):
- `ambjorn-loll-1998` (hep-th/9805108) — OK
- `ajl-reconstructing-2005` (hep-th/0505154) — OK
- `ajl-spectral-dimension-2005` (hep-th/0505113) — OK
- `agjl-planckian-2008` (0712.2485) — OK (odeslán 2007, publikován 2008; rok v JSON odpovídá roku časopisu)
- `ajl-semiclassical-2011` (1102.3929) — OK
- `ajjl-phase-transitions-2012` (1205.1229) — OK
- `transfer-matrix-2012` (1205.3791) — OK
- `new-phase-2016` (1510.08672) — OK (odeslán 2015, JHEP 2016)
- `characteristics-cb-2017` (1610.05245) — OK
- `rg-flow-2014` (1405.4585) — OK
- `agjl-physrep-2012` (1203.3591) — OK
- `loll-review-2019` (1905.08669) — OK (CQG 37, 013002, 2020)
- `ambjorn-gateway-2024` (2401.09399) — OK
- `ambjorn-loll-new-2026` (2604.05641) — OK (existuje, duben 2026, příspěvek do Scholarpedie)
- `cdt-horava-2010` (1002.3298) — OK
- `2d-cdt-horava-2013` (Phys. Lett. B 722, 2013) — OK (doplněno chybějící arXiv ID 1302.6359)
- `klitgaard-loll-qrc-2018` (1802.10524) — OK
- `topology-first-order-2022` (2202.07392) — OK
- `scalar-fields-cdt-2021` (2105.10086) — OK
- `laiho-dark-energy-2024` (2408.08963) — OK
- `vdduin-effective-topology-2025` (2510.05695) — OK (DOI 10.1140/epjc/s10052-026-15322-x ověřen, EPJC 86, čl. 102, 2026)
- `vdduin-tda-2025` (2510.05693) — OK
- `clemente-delia-spectral-gauge-2023` (2307.04547) — OK
- `candido-yang-mills-cdt-2021` (2112.03157) — OK
- `lauscher-reuter-2005` (hep-th/0508202) — OK
- `horava-lifshitz-2009` (0901.3775) — OK
- `reuter-frg-1998` (hep-th/9605030) — OK (odeslán 1996, PRD 1998)
- `effective-action 2014` (1403.5940, próza ref. 21) — OK
- `Jordan & Loll 2013` (1307.5469) — OK
- `CDT and Cosmology 2017` (1703.08160) — ID OK, ale autorství bylo chybné (viz níže)

### Audit vzorců (5 klíčových vzorců ověřeno proti přehledu Ambjørn–Loll „Gateway" 2401.09399)
- Wickem rotovaná euklidovská 4D CDT Reggeho akce `-(κ0+6Δ)N0 + κ4(N41+N32) + Δ(2N41+N32)` — **správně** (standardní forma Physics Reports / AJL).
- Profil objemu de Sitter, `ω0^4 = 3/(8π^3)` — **přesná shoda** s eq. (18) přehledu.
- Fit běhu spektrální dimenze `D_S(σ) = 4.02 − 119/(54+σ)` — **přesná shoda**.
- `δ0 = 3/(8π^2)` — **přesná shoda**.
- Vztah Newtonovy konstanty `√V4/Γ = √V4/(24πG)` — **přesná shoda** s eq. (22).
- Doplňkově: UV hodnota `D_S → 1.80 ± 0.25` numericky konzistentní (`4.02 − 119/54 ≈ 1.82`); IR `4.02 ± 0.1`. OK.

### Audit konzistence
- Cíle v `connections`/`relatedTo` (asymptotic-safety, causal-sets, loop-quantum-gravity, group-field-theory, quantum-cosmology, semiclassical-gravity, string-theory, swampland, holography-adscft, emergent-gravity, entanglement-spacetime, black-holes-information, experimental-tests, noncommutative-geometry) odpovídají existujícím fragmentům nebo zavedeným tematickým id (`spectral-dimension`, `regge-calculus`, `euclidean-dynamical-triangulations`, `horava-lifshitz-gravity`) používaným i jinde v repozitáři — **plausibilní**.
- Hodnocení `explored` jsou poctivá: žádná slavná, dobře prozkoumaná dualita není podhodnocena. Ekvivalence CDT↔Hořava–Lifshitz je hodnocena „partially" (rigorózně dokázáno ve 2D, jen kvalitativně ve 4D) — což odpovídá realitě; `regge-calculus`, `quantum-cosmology`, `semiclassical-gravity`, `euclidean-dynamical-triangulations` mají „well", což sedí.
- Česká próza neodporuje JSONu v klíčových tvrzeních (fáze, dimenze, vzorce, výsledky).

---

## Co bylo špatně a opraveno

1. **`cdt-frg-2024` (2408.07808) — chybní autoři.** JSON i próza (ref. 23) uváděly „Jurkiewicz" a „Schiffer" jako autory; skuteční autoři jsou **J. Ambjørn, J. Gizbert-Studnicki, A. Górlich, D. Németh**. Jurkiewicz ani Schiffer nejsou autory, Németh chyběl. Opraveno v JSON i v próze.

2. **`toroidal-higher-order-2020` (2002.01051) — chybný druhý autor.** Uvedeno „Z. Drogosz"; skutečný druhý autor je **G. Czelusta**. Opraveno v JSON i v próze (ref. 18).

3. **`ml-lattice-gravity-2025` (2510.02159) — chybný název i autoři.** Uveden název „Machine learning in lattice quantum gravity" a autoři „J. Ambjorn et al." (próza dokonce mylně připisovala práci „Clemente & D'Elia"). Správně: **„Machine learning in phase transition analysis of lattice quantum gravity"**, autoři **J. Ambjørn, Z. Drogosz, J. Gizbert-Studnicki, A. Görlich, D. Németh, M. Reitz**. Opraveno v JSON i na třech místech prózy (sekce Současný stav, Klíčové výsledky, Reference 36).

4. **„CDT and Cosmology" 2017 (1703.08160) — chybní autoři v próze (ref. 29).** Uvedena skupina Ambjørn et al.; skuteční autoři jsou **L. Glaser a R. Loll**. Opraveno.

5. **`scalar-fields-cdt-2021` — chybná atribuce prvního autora v próze (ref. 22).** Uvedeno „Görlich, A. et al."; první autor je Ambjørn. Próza opravena na plný seznam autorů. (JSON měl autory správně.)

6. **`ambjorn-quest-2010` (1004.0352) — nadhodnocený význam.** JSON i próza tvrdily, že práce „diskutuje konečnost entropie černé díry". Abstrakt toto téma vůbec nezmiňuje (jde o obecný koncepční přehled). Tvrzení v JSON zmírněno a v próze označeno `⚠️ neověřeno`.

7. **Textové artefakty v próze.** Odstraněna dvě omylem vložená francouzská slova („connaissent", „connais") v odstavcích o UV pevném bodě (řádky o asymptotické bezpečnosti / otevřených problémech).

8. **`2d-cdt-horava-2013` — doplněno chybějící arXiv ID** (1302.6359); dříve byla uvedena jen DOI a odkaz na ScienceDirect.

---

## Co zůstává nejisté

- **Tvrzení o entropii černých děr (1004.0352):** nepodařilo se ověřit, zda plný text práce skutečně diskutuje konečnost Bekensteinovy–Hawkingovy entropie; ověřitelný byl jen abstrakt, který toto téma nezmiňuje. Označeno `⚠️ neověřeno`.
- **Vliv Barretta/Cranea/Baeze** (spinově-pěnová/simpliciální geometrie) na CDT — rozsah a přesnost této historické vazby nebyly samostatně ověřeny; tvrzení je obecné a plausibilní, ponecháno beze změny.
- **Mapování 3D CDT na hermitovský dvoumaticový model s ABAB-interakcí** (Ambjørn, Anagnostopoulos, Loll, Pushkina) — výsledek existuje, ale konkrétní reference není v seznamu literatury; přesné bibliografické údaje nebyly ověřeny.
- **Číselné hodnoty efektivních vazeb** (Γ = 23 ± 1, μ = 13.9 ± 0.7, λ_eff = 0.027 ± 0.003 při κ0 = 2.2, Δ = 0.6) jsou konzistentní se semiklasickou prací 1102.3929, ale přesné chybové úsečky nebyly ověřeny z originálu znak po znaku.
- **PDF originálů** (Gateway 2024, Spectral Dimension 2005) nebylo možné parsovat jako binární proud; klíčové vzorce byly ověřeny přes HTML verzi přehledu, kde se shodovaly přesně.
