# Index znalostní báze — Theory of Everything

> Anotovaný rejstřík všech souborů ve `knowledge-base/`, `core-data/` a `verification/`.
> Generováno: 2026-06-05; aktualizováno: 2026-06-09 (kolo 22: VYPOCET-37/38 přidány; F-040/F-041 přidány do findings.json (41 nálezů); NCG<->spectral-dimension UPGRADE barely->partially; NCG<->semiclassical-gravity anotováno F-040 ostřejším negativem; ncg-spectral-dimension přidáno do SLOW_CALCS; kolo 21 konsolidace: CAS revize vzorců — triáž 247, B1–B4 validace, 24 verified + 14 already_validated = 38 vzorců; `myrheim-meyer` RESOLVED (oprava /2, resolved_blocker); 7 WL skriptů aktivních; numerická reprodukční coverage druhého oblouku 10/11 PASS; oprava stale F-033 korelace 0.098→0.319).

---

## Klíčové dokumenty

> **VSTUPNÍ BOD PRO LIDSKÉHO AUTORA (drafty → revize → release):**
> [`../papers/REVIZE-PRO-CLOVEKA.md`](../papers/REVIZE-PRO-CLOVEKA.md) — přehledová tabulka stavu všech 4 draftů; doporučené pořadí revizí; ~80 checkboxů (matematika / citace / čísla / konvence); kritické high-risk položky; absolutní pravidla pro release; příkazy pro re-run všech calc.py. **Sem jít jako první před externím sdílením čehokoli z projektu.**

- [SYNTEZA.md](SYNTEZA.md) — Syntetická mapa všech 18 pilířů: kde každý stojí, co sdílí a kde jsou bílá místa; vstupní bod pro hledání skrytých vazeb.
- [BRAINSTORM-01.md](BRAINSTORM-01.md) — První systematický brainstorming nenalezených souvislostí: 5 analytických čoček nad `core-data/`, 10+ hypotéz s confidence skóre a prioritami pro Fázi 2.
- [BRAINSTORM-02.md](BRAINSTORM-02.md) — Druhé kolo brainstormingu (2026-06-06): verdikty čtyř dokončených výpočtů, 8 hypotéz druhé generace (H2g-1–H2g-8), výpočetní fronta 10 položek a strategický meta-závěr; kalibrace po falzifikaci silných verzí.
- [BRAINSTORM-03.md](BRAINSTORM-03.md) — Třetí kolo brainstormingu (2026-06-06, kolo 4): 3 hypotézy třetí generace — H3g-1 (opačná znaménka A_caus/A_W jako superradiantní podpis), H3g-4 (spektrální akce = fermionově-indukovaná gravitace), H3g-3 (SSEE truncace = crossed-product modulární cutoff); doporučení: draft-02 jako nejpevnější aktivum k releasování. H3g-1 uzavřena VYPOCET-15 (kolo 7); H3g-4 uzavřena VYPOCET-11 (kolo 5).
- [BRAINSTORM-04.md](BRAINSTORM-04.md) — Čtvrté kolo brainstormingu (2026-06-06, kolo 7): 3 hypotézy čtvrté generace — H4g-1 (rohová non-Hadamardovost = selhání boost-flow, medium-high), H4g-4 (III→II na slabu ne na diamantu, medium-high; POTVRZENA VYPOCET-16), H4g-3 (fermionová indukce predikuje Λ přes f₀/a₀, medium). Doporučená fronta: H4g-3 (nejlevnější, sympy, dny) + H4g-1 (nejvyšší konceptuální výnos). Viz PROGRESS.md § Další kroky.
- [BRAINSTORM-05.md](BRAINSTORM-05.md) — Páté kolo brainstormingu (2026-06-06, závěrečné): 6 hypotéz páté generace (H5g-1–H5g-6) navazujících na výsledky kol 7–9: dS II₁ diskriminátor (F-023), BD 4D modulární tok (F-024), causal-set typ-přechod, rohová non-Hadamardovost. Vstupní fronta pro velké review.
- [SYNTEZA-02.md](SYNTEZA-02.md) — Druhá syntéza (2026-06-06, kolo 7): přehled 7 kol a 19 nálezů; 5 uzavřených front (γ–Cardy, naivní Λ, plná SM, 4D volume-law jako dimenze-efekt, Model E pro superradianci); vlajková loď NCG a₄ = −18/11 (fermionicky-indukovaná gravitace, draft-02 uzavřen); causal-set triáda (III₁→II 2D/4D, slab area law, SSEE cutoff ρ^{−1/2}); through-line (vlastnosti prostoročasu jako odpovědi na otázky); výhled 10 kol.
- [BRAINSTORM-06.md](BRAINSTORM-06.md) — Šesté kolo brainstormingu (2026-06-08, kolo 16, šestá generace H6g): otevírací tah po uzavření celé fronty H5g; vede otvory, které negativy páté generace vytvořily (causal-sets↔NCG je tepelně-časová/KMS osa, ne metrická — F-033; konformně-váhový caveat 4D area-zákona — F-031; B(a) spojitá — F-030). Hypotézy H6g-1..H6g-6 (KMS/tepelná osa, Λ shot-noise, molekulová fluktuace, konformní 4D).
- [SYNTEZA-03.md](SYNTEZA-03.md) — Třetí syntéza (2026-06-08, po kolech 7–20, F-018..F-039): druhý oblouk zostřil 2D causal-set/von-Neumann jádro a −18/11 na publikovatelnou pevnost, ale **narazil na tvrdou zeď ve čtyřech ambiciózních směrech** — 4D area-zákon genuinně NEPŘÍTOMEN (pohřben 3× nezávisle: mean F-031, konformní F-037, variance F-038), −18/11 NEDOSÁHNE do entanglement linie (F-039) ani na absolutní Unruh teplotu (F-036 tautologie), B(a) spojitá ne D−1 (F-030). Dvě nové through-line osy: dimenze je reálný diskriminátor; variance vs. mean rozlišuje co přežije. Λ shot-noise ožil na ose variance (F-035). Výhled 7. gen: konsolidace/dokumentace (draft-06 „mapa negativů"), ne další 4D numerika.

---

## Denní zprávy a reviewové reporty (`reports/`)

- [../reports/2026-06-06-review.md](../reports/2026-06-06-review.md) — **Velké review část 1** (2026-06-06): verifikace 150 arXiv ID (7 chyb opraveno, tabulka problémových ID); audit 24 nálezů (cesty k evidenci + caveaty, žádný status nezměněn); opravy draftů (a_err rekonstrukce nejistot, CST konvence d_s=8 + D vs D_space); doplnění grafu (5 nových hran, 2 nové uzly, VNA pilíř na 11 hranách); nové statistiky registrů (625 uzlů, 2476 hran, 292 connections, 115 barely, 587 ref.); část 2 (reprodukce): **20/20 calc.py bitově identických** (§f — vč. 2 skrytých závislostí pořadí a opravy latentního print-bugu).
- [../reports/2026-06-06-day-report.md](../reports/2026-06-06-day-report.md) — Závěrečná denní zpráva (2026-06-06): přehled celého dne výzkumu (kola 3–9), souhrnné statistiky (20 výpočtů, 24 nálezů, 4 drafty), stav všech hypotéz, uzavřené fronty, doporučení a plán pro velké review.

---

## CAS validační dráha (`verification/cas/`)

- [../verification/cas/README.md](../verification/cas/README.md) — **Nezávislá CAS validace** (2026-06-07): 3 Wolfram Language skripty re-derivují publikované exaktní výsledky PŘÍMO z literárních koeficientů (Duff 2003.02688, Vassilevich hep-th/0306138, Chamseddine-Connes hep-th/9606001, Beccaria-Tseytlin 1710.03779, Hořava 0902.3657) — ne přepisem sympy výstupů. Shoda obou drah = nezávislý důkaz. Instalace: `brew install --cask wolfram-engine` + jednorázová aktivace; spuštění: `python3 verification/cas/run_all.py`. Testy gracefully skippují bez WL Engine.
- [../verification/cas/a4_identity.wl](../verification/cas/a4_identity.wl) — Ověřuje −18/11 (single Weyl), Dirac = 2×Weyl (stejný poměr), třícestnou konzistenci (spektrální α₀/τ₀ = single-Weyl = Dirac; f₀ i π se pokrátí přes `Together+FreeQ`), obsahovou nezávislost SM 45 i 48, plný SM láme identitu (−1698/1991), konformní graviton −398/261, STr(1) = −62/−68. Export `a4_identity_result.json`.
- [../verification/cas/ds_classifier.wl](../verification/cas/ds_classifier.wl) — Izotropní d_s = D/γ a Hořavova d_s = 1 + D_space/z; validuje ~9 exaktních racionálů vč. Hořava z=2→5/2, z=3→2, IR z=1→4. Export `ds_classifier_result.json`.
- [../verification/cas/lambda_ledger.wl](../verification/cas/lambda_ledger.wl) — Formální symbolová aritmetika (f₀,f₂,f₄,N,k̂,ĝ,Λ); ověřuje a₀ a a₂ lineární v N, poměr a₀:a₂ nese (f₄/f₂)Λ², intra-a₄ poměr −18/11 cutoff-čistý, Λcc/m_Pl² = π²f₄/(2Nf₂²k̂²) nese 1/N. Export `lambda_ledger_result.json`.
- [../verification/cas/run_all.py](../verification/cas/run_all.py) — Runner: volá `wolframscript -file` pro každý .wl, sbírá JSONy do `results.json` s overall pass/fail; při chybějícím wolframscript exit 2 + zpráva. **Kolo 20:** rozšířen o B1–B4 skripty (celkem 7 .wl skriptů v dráze). Testy: `app/tests/test_cas_validation.py` (3 vždy-běžící guardy + 2 Wolfram-podmíněné).
- [../verification/cas/heat-kernel-perturbative-gravity-counterterms.wl](../verification/cas/heat-kernel-perturbative-gravity-counterterms.wl) — **Dávka B1** (kolo 20): 8 vzorců heat-kernel / perturbativní gravitace: 'tHooft–Veltman (1/120, 7/20), Goroff–Sagnotti (209/2880), D=(d−2)L+2, 41/(10π), D_c(L)=4+6/L, g*=3/38ε, N=8 spin obsah, Stelle parciální zlomek. Všechny **verified**. Export `heat-kernel-perturbative-gravity-counterterms_result.json`.
- [../verification/cas/causal-set-combinatorial-operators.wl](../verification/cas/causal-set-combinatorial-operators.wl) — **Dávka B2** (kolo 20): 6 vzorců kauzálně-množinové kombinatoriky: BD akce, diskrétní d'Alembertián, KR počítání n²/4, Poissonův sprinkle, číslo–objem. **5 verified, 1 mismatch** (`myrheim-meyer`: BLOCKER — jmenovatel 4→2). Export `causal-set-combinatorial-operators_result.json`.
- [../verification/cas/b4-swampland-inflation-scaling.wl](../verification/cas/b4-swampland-inflation-scaling.wl) — **Dávka B4** (kolo 20): 7 vzorců swampland/inflace: slow-roll, WGC KK rate √(3/2), universální pattern 1/(d−2), species scale, w(1+∞) algebra, BCJ Jacobi. Všechny **verified**. Export `b4-swampland-inflation-scaling_result.json`.
- [../verification/cas/formula-coverage.json](../verification/cas/formula-coverage.json) — **Registr CAS pokrytí** (kolo 20, resolved kolo 21): stav `cas_verification` pro 38 vzorců (24 verified + 14 already_validated). `myrheim-meyer` RESOLVED (oprava jmenovatele 4→2 ve fragmentu + consolidate; `meta.resolved_blocker` zachycuje detail). Zbývající kategorie: definitional 158, numerical 36.

---

## Denní zprávy a reviewové reporty — kolo 20

- [../reports/2026-06-08-cas-formula-revision.md](../reports/2026-06-08-cas-formula-revision.md) — **CAS revize registru vzorců** (kolo 20, 2026-06-08): triáž 247 vzorců (34 CAS-checkable, 158 definitional, 36 numerical, 19 already-validated); validace B1–B4 (33 verified, 1 mismatch = BLOCKER `myrheim-meyer` jmenovatel 4→2); aktualizace run_all.py + formula-coverage.json.
- [../reports/2026-06-09-numerical-coverage.md](../reports/2026-06-09-numerical-coverage.md) — **Numerická reprodukční coverage druhého oblouku** (kolo 21, 2026-06-09): protějšek CAS revize — dvojí verifikační průchod. 8 calc adresářů kol 13–20 (F-029…F-039) dáno do `test_reproduction.py`: **10/11 PASS, 1 vyloučen** (ds-amol-convention — čte staged archiv mimo /tmp sandbox). Odhalené a opravené reprodukční defekty: `TIMING_FIELDS` (`elapsed_s`/`wall_clock_*`), `spectral-triple-modular` nedeterminismus (Connes wall-clock cap → committed korelace F-033 = 0.098 byl artefakt timing-truncace → reprodukovatelná 0.319, verdikt no-match nezměněn). Křížový odkaz na CAS revizi (Myrheim-Meyer = obdobný typ defektu).

---

## Predikce vazeb (`lib/kgraph/` + `core-data/link-predictions.json` + `reports/`)

- [../lib/kgraph/__init__.py](../lib/kgraph/__init__.py) — **`lib/kgraph/`** (2026-06-07): infra-knihovna pro strojové hledání nenalezených vazeb v grafu konceptů (numpy+scipy only, žádný networkx/torch). Moduly: `loader.py` (concept-graph.json → řídká sousednost vážená násobností, 1632 unikátních hran), `scores.py` (5 heuristik + spektrální embedding normalizovaného Laplaciánu, eigsh d=32, kosinus; ensemble = rank-průměr), `evaluate.py` (leave-k-out, AUC z Mann-Whitney U + precision@k), `predict.py` (cross-pillar flag, vysvětlení přes Adamic-Adar-vážené sousedy).
- [../core-data/link-predictions.json](../core-data/link-predictions.json) — **Top-50 kandidátních vazeb** (generated 2026-06-07, refreshed kolo 17 2026-06-08): leave-10%-out **AUC = 0,9034 ± 0,018** (8 seedů), P@50 ≈ 0,9975. Pozor: 17/50 jsou hub-artefakty (pilíř↔pilíř); 3 nejzajímavější koncept-koncept: generalized-entropy↔crossed-product-algebra (CLPW), spectral-triple↔SM-from-spectral-geometry (Connes NCG), noncommutative-geometry↔spectral-dimension (mezipřístupový). Kolo 17: topologie grafu nezměněna (0 nových/odebraných hran), AUC identické; posun registru: barely 114->113, partially 112->113 (upgrade idx 212 semiclassical-gravity<->causal-sets). **Kandidáti jsou NÁVRHY** — do fragmentů/connections.json až po redakčním rozhodnutí s arXiv/DOI oporou.
- [../reports/2026-06-07-link-prediction.md](../reports/2026-06-07-link-prediction.md) — Detailní report link prediction: metodologie, evaluace, kritické čtení top-50, vizualizace.

---

## Infrastruktura (`app/` + `lib/` + `web/` + `compute/` + GH Actions)

- [../compute/README.md](../compute/README.md) — **`compute/` — škálované výpočetní drivery** (2026-06-07): 3 drivery nad `lib/toe` v0.3.0 pro F-025/F-028 rozšíření a otevřenou otázku c^{4D} vs. c^{2D}; sdílená infrastruktura `_common.py` (atomický checkpointing, time-budget 5,5 h, host fingerprint); výsledky do `compute/results/` lokálně nebo artefakty GH Actions (90 dní). Testy: 4 smoke testy v `app/tests/test_compute_drivers.py`, každý < 30 s.
- [../.github/workflows/repro.yml](../.github/workflows/repro.yml) — **Cross-HW reprodukce** (2026-06-07): `workflow_dispatch` s volbou konkrétního výpočtu nebo `all`; matice 24 výpočetních adresářů, fail-fast=false, max-parallel=20, timeout 350 min. Každý job nahraje `results.json` jako artefakt a vypíše max. rel. odchylku do GITHUB_STEP_SUMMARY. Ošetřuje 4 adresáře bez pytest testů (exit 5 = skipped, ne fail).
- [../.github/workflows/compute.yml](../.github/workflows/compute.yml) — **Škálované výpočty** (2026-06-07): `workflow_dispatch` s výběrem driveru (`ds_entropy_cap_2d` / `ds4d_saturation` / `ds_cap_4d`), volnými args a `--max-hours`; timeout 355 min; artefakt `<driver>-run` s 90denní retencí; GITHUB_STEP_SUMMARY s fyzikálními výsledky ze `results.json`.

## Infrastruktura (`app/` + `lib/` + `web/`)

- [../app/README.md](../app/README.md) — Dockerizované prostředí (research/testing/prezentace): Jupyter Lab nad repem, pytest reprodukční sada (rychlá 6 výpočtů + plná 20 za `FULL_REPRO=1`), plný repro-runner, web služba buildující `web/dist/`. Verze knihoven pinované na stav bitové reprodukce 2026-06-06.
- [../lib/README.md](../lib/README.md) — **`lib/toe` v0.3.0** (kolo 12): kombinovatelná simulační knihovna distilovaná z 24 ověřených `calc.py`. 8 modulů ve vrstvách A/B/C (`fits`, `causet`, `spectral`, `ncg`, `viz` | `sj` | `entropy`, `vntype`), **64 veřejných funkcí** (+5 sparse z kola 12: sparse eigensolver mašinérie, float64+float32, dense vs. sparse cross-validace). Fyzikální vstupy → `(hodnota, SE/CI)` výstupy s `validated` flagem a `formula-id` docstringy. Testy: **304 passed / 14 skipped / 1 xfailed v 99.4 s** (16 nových sparse testů, ze 288 kolo 11).
- [../lib/examples/demo_pipeline.py](../lib/examples/demo_pipeline.py) — spustitelná end-to-end ukázka: 2D diamant N≤500, sprinkle → SJ stav → truncovaná SSEE → power-law fit → panel (`demo_output.png`); runtime <1 s.
- [../web/README.md](../web/README.md) — **`web/` — minimalistický statický site-builder** (krok 4 roadmapy + rozšíření 2026-06-07): `web/build.py` builduje **121 stránek** do `web/dist/` přímo ze zdrojů repozitáře (markdown + JSON registry jako zdroj pravdy, žádný duplicitní obsah). Spuštění: `python3 web/build.py` nebo `docker compose --profile web up web` (port 8080). Vč. interaktivního grafu konceptů: `web/dist/data/graph.html` (force-graph CDN, canvas; uzel ~ stupeň, barva ~ pilíř, hrana ~ explored; search/pilíř-filtr/rating-toggly/predikce-toggle; klik → boční panel). Ověřeno headless (0 chyb, file:// i http).

---

## Přístupy ke kvantové gravitaci (`approaches/`)

- [approaches/01-string-theory.md](approaches/01-string-theory.md) — Teorie strun a M-teorie: nejkomplexnější kandidát s mikroskopickou entropií ČD a AdS/CFT, ale bez ověřitelné předpovědi a s nevyřešeným landscape ~10⁵⁰⁰ vakuí.
- [approaches/02-loop-quantum-gravity.md](approaches/02-loop-quantum-gravity.md) — Smyčková kvantová gravitace: background-independentní kvantování geometrie s diskrétními spektry plochy a objemu, zatím bez dokončené dynamiky a semiklasické limity.
- [approaches/03-asymptotic-safety.md](approaches/03-asymptotic-safety.md) — Asymptotická bezpečnost: neporuchová renormalizovatelnost gravitace přes Reuterův UV pevný bod; retrodikuje Higgsovu hmotnost, otevřená otázka lorentzovský podpis a unitarita.
- [approaches/04-causal-dynamical-triangulations.md](approaches/04-causal-dynamical-triangulations.md) — Kauzální dynamické triangulace: mřížkový dráhový integrál přes simplexové geometrie dynamicky generuje 4D de Sitterův vesmír a běžící spektrální dimenzi 4→2.
- [approaches/05-causal-sets.md](approaches/05-causal-sets.md) — Teorie kauzálních množin: jediný přístup s úspěšnou předpovědí předem (Λ ∼ 10⁻¹²⁰ z roku 1987), kde „Order + Number = Geometry".
- [approaches/06-group-field-theory.md](approaches/06-group-field-theory.md) — Group field theory a tenzorové modely: druhá kvantizace LQG ve Fockově prostoru spinových sítí; melonická 1/N expanze propojuje GFT se SYK modelem a kondenzátovou kosmologií.
- [approaches/07-noncommutative-geometry.md](approaches/07-noncommutative-geometry.md) — Nekomutativní geometrie Connese: spektrální trojčlen odvozuje Standardní model + gravitaci z geometrického principu; zahrnuje κ-Minkowski, DSR a fuzzy prostory.
- [approaches/08-twistors-amplitudes.md](approaches/08-twistors-amplitudes.md) — Twistory a amplitudy: prostoročas jako odvozená struktura z twistorové geometrie, amplituhedronu a BCJ dvojité kopie; hustě propojen s holografií a Ashtekarovými proměnnými.
- [approaches/09-emergent-gravity.md](approaches/09-emergent-gravity.md) — Emergentní a entropická gravitace: Einsteinova rovnice jako termodynamická rovnice stavu (Jacobson 1995); Verlindeho entropická síla a jej napětí s daty galaktických kup.
- [approaches/10-supergravity-uv.md](approaches/10-supergravity-uv.md) — Supergravitace a UV chování: N=8 SUGRA s „vylepšenými kancelacemi" a otázkou konečnosti ve 4D; alternativy (Stelle, Hořava-Lifshitz) platí cenou duchů nebo LIV.

---

## Průřezová témata (`cross-cutting/`)

- [cross-cutting/11-holography-adscft.md](cross-cutting/11-holography-adscft.md) — Holografický princip a AdS/CFT: Maldacenova korespondence dnes zahrnuje Ryu-Takayanagi, ER=EPR a ostrovy; prostoročas emerguje z entanglementu hraniční CFT.
- [cross-cutting/12-black-holes-information.md](cross-cutting/12-black-holes-information.md) — Černé díry a informační paradox: průlom 2019–2020 (ostrovy, kvantové extrémní plochy, replikové červí díry) reprodukuje Pageovu křivku, ale mechanismus úniku informace zůstává záhadou.
- [cross-cutting/13-entanglement-spacetime.md](cross-cutting/13-entanglement-spacetime.md) — Entanglement a emergence prostoročasu (It from Qubit): Van Raamsdonk, Faulkner et al. a tensorové sítě ukazují, že geometrie roste z kvantového provázání — ale emergence *času* zůstává nevyřešena.
- [cross-cutting/14-swampland.md](cross-cutting/14-swampland.md) — Swampland: ostrá kritéria (WGC, Distance Conjecture, dS conjectures) vymezují, které EFT jsou UV-konzistentní; status de Sitterových vakuí KKLT je stále sporný, DESI 2024 oživil kvintesenci.

---

## Základy (`foundations/`)

- [foundations/15-semiclasical-gravity.md](foundations/15-semiclassical-gravity.md) — Semiklasická gravitace a QFT v zakřiveném prostoročase: Unruh, Hawking, stopová anomálie, Waldova entropie — nejrobustnější a experimentálně nejbližší rozhraní teorie a gravitace.
- [foundations/16-conceptual-problems.md](foundations/16-conceptual-problems.md) — Konceptuální problémy: problém času (H Ψ = 0), background independence, kosmologická konstanta, role pozorovatele — a nové výsledky 2023–2026 od algebraické holografie po debatu o kvantovosti gravitace.

---

## Fenomenologie (`phenomenology/`)

- [phenomenology/17-experimental-tests.md](phenomenology/17-experimental-tests.md) — Experimentální testy a fenomenologie: nejlepší meze LIV (Fermi/LHAASO), hmotnost gravitonu (GWTC-3), BMV entanglement experiment a střízlivé hodnocení — žádný pozitivní signál QG dosud neexistuje.
- [phenomenology/18-quantum-cosmology.md](phenomenology/18-quantum-cosmology.md) — Kvantová kosmologie: Wheeler-DeWitt, Hartle-Hawking vs. Vilenkin, LQC big bounce při ρ_c ≈ 0,41 ρ_Pl; DESI DR2 2024–2025 tvrdě svazuje modely temné energie.

---

## Datové registry (`core-data/`)

- [../core-data/_digest.md](../core-data/_digest.md) — Strojově generovaný souhrn celé báze (aktualizováno 2026-06-06, velké review část 1) — levný vstupní bod pro agenty.
- [../core-data/concept-graph.json](../core-data/concept-graph.json) — Graf konceptů (**626 uzlů, 2487 hran**, kolo 19: +6 hran spectral-action/NCG/trace-anomaly/EE/a-theorem): top huby holographic-principle, generalized-entropy, bekenstein-hawking-entropy, spectral-dimension, modular-hamiltonian, page-curve.
- [../core-data/connections.json](../core-data/connections.json) — Matice meziobjevových vazeb (**298 hran, 114 hodnoceno jako „barely explored"**) — základ pro hledání bílých míst. Kolo 19: +6 hran; link-prediction AUC 0.9057.
- [../core-data/references.json](../core-data/references.json) — Registr referencí: **587 unikátních** z 665 syrových; duplikáty odfiltrovány.
- [../core-data/references.bib](../core-data/references.bib) — BibTeX export téhož registru pro LaTeX/Pandoc workflow.
- [../core-data/formulas.json](../core-data/formulas.json) — Registr vzorců: **247 unikátních** z 249 syrových záznamů napříč 19 pilíři.
- [../core-data/open-problems.json](../core-data/open-problems.json) — Registr otevřených problémů: **153 problémů** (+9 fuzzy duplicit k posouzení).
- [../core-data/connections.json](../core-data/connections.json) — Viz výše.

### Kolo 22 (VYPOCET-37–38)

- [vypocty/VYPOCET-37-geometric-boost-dirac.md](vypocty/VYPOCET-37-geometric-boost-dirac.md) — Geometrický/gamma_5-gradovaný boostový Dirac (H6g-1, F-040): pojmenovaný chybějící prvek F-036 postaven na 2D Rindlerově slabu (3N × 5 seeds, N<=1500). Výsledky: {D,Gamma5}=0 strojově nulové, spektrum +-párové na 2.9e-15 (první sudý spektrální triple s chirálním gradováním na causetu). Geometrický Dirac VYŘEŠÍ log-kompresi F-036: exponent p_E=+1 (0.989, R2=1.000). ALE Route1 tautologická, Route2 diagonála nulová, Route3 driftuje (CV=0.205). Obstrukce přesunuta z eps-log-komprese na konečné-N diskretizaci prvořádového boostového generátoru. Wall 2 nepřechází. Status: confirmed-mixed-sharper-negative. Data: `core-data/calculations/geometric-boost-dirac/`. Knihovna: `lib/toe/spectraltriple.py` (geometric_boost_dirac). Test: `app/tests/test_toe_spectraltriple.py`. (F-040)
- [vypocty/VYPOCET-38-ncg-spectral-dimension.md](vypocty/VYPOCET-38-ncg-spectral-dimension.md) — NCG<->d_s heat-kernel (L3-1/L1-1, F-041): z téhož D^2-spektra (|sym(B)|, BD d'Alembertián, 2D causal diamond, N=2200, 3 seeds) se konzistentně extrahují d_s(sigma) i Seeley-DeWittovy koeficienty a0,a2,a4. d_s=1.998±0.044 (chyba 0.0024 < F-001 tol 0.06, plateau 1.83->2.25 dekád); Pauli-Jordanova sonda d_s=0.011 (F-001/F-002 probe-závislost zkonkretizována). Diskrétní a4/a0=-1.40±4.25 NEreprodukuje -18/11 (a4=0 analyticky na plochém causetu). Status: confirmed (smíšený). Hrana NCG<->spectral-dimension UPGRADOVÁNA barely->partially. Data: `core-data/calculations/ncg-spectral-dimension/`. Knihovna: `lib/toe/spectral.py`. Test: `app/tests/test_toe_spectral.py`. Runtime 27 s. (F-041)

### Kolo 19 (VYPOCET-35–36)

- [LOV-18-11-overlaps.md](LOV-18-11-overlaps.md) — **LOV na překryvy -18/11** (2026-06-08): brainstorm LOV dokument + výsledky kola 19. H-B (EE-koeficient vs anomálie): c_EE = 7.562 NEODPOVÍDÁ trace-anomálním racionálům — no-match-geometric, F-039 confirmed. H-E (index-náboj diskrétní): H-E vyvrácena — eta(iDelta)=0 strukturálně (chybí gamma5), eta(D_K)~N^1.02 extenzivní, VYPOCET-36 dokumentuje. +6 hran nakreslenýchrozhodnutím T3. Podmíněná NCG<->EE hrana nepřidána (H-B oslabuje). Data: `core-data/calculations/amol-anomaly-ee-coeff/` + `core-data/calculations/index-charge-discrete/`.
- [vypocty/VYPOCET-35-ee-coeff-vs-anomaly.md](vypocty/VYPOCET-35-ee-coeff-vs-anomaly.md) — H-B: c_EE vs trace-anomálnímu racionálu (F-039, confirmed/negativní): c_EE = 7.5623 (CV 1.26 %; z F-029 dS path), 60 srovnání (6 kanálů × 10 pre-registrovaných kandidátů), n_matches=0, no-match-geometric. Přímý skalár c/(-a)=-3: residual 152 %; -18/11: residual 362 %; kontrola 8: 5.47 % (NAD prahem); Bekenstein 4: 10.26 %. Anti-cirkularita strukturálně ověřena. Scope: 2D, finite-N, massless scalar. Runtime 233 s. Data: `core-data/calculations/amol-anomaly-ee-coeff/`. (F-039)
- [vypocty/VYPOCET-36-index-charge-discrete.md](vypocty/VYPOCET-36-index-charge-discrete.md) — H-E: index-náboj diskrétní (dokumentovaný negativní výsledek; F-040 NEPŘIDÁN): H-E vyvrácena v přímé formě. Probe A eta(D_K)~N^1.02 (slope 1.019, CV=0.42) — extenzivní. Probe B eta(iDelta)=0 na 48/48 bězích (±-párované spektrum, chybí gamma5 gradování). Probe C n_rel~N^2.00, n_link~N^1.20. Žádný proxy N-nezávislý sudě-celočíselný. Skutečný most vyžaduje euklidizaci + gamma5-gradování + saturující invariant (NCG↔NCG, ne causal-set↔Rohlin). Data: `core-data/calculations/index-charge-discrete/`.

### Kolo 18 (VYPOCET-32–34)

- [vypocty/VYPOCET-32-ncg-kms-unruh.md](vypocty/VYPOCET-32-ncg-kms-unruh.md) — NCG<->semiklasika KMS/Unruh netautologický test (H6g-1b, F-036): SJ modulární tok na 2D Rindlerově slabu + dS static patch (N∈{600,1000,1400}, 5 seedů, 15 Rindler + 15 dS). Zákonný exponent p_E=0,720+-0,040 (BW +1 nečteno, deficit 28 %); boost slope 29,20 (R2=0,969, CV 1,7 %); 2*pi best route 9,58 (off 52 %); dS: p_E=0,62, Gibbons-Hawkingova 2*pi=2,55. Kontroly selhávají (interval R2=0,038, shuffle R2=0,065). VERDIKT: informovany-negativ-tautologie — most struktury, NE teploty; hrana barely, edge NEPROPAGOVÁNA. Data: `core-data/calculations/ncg-kms-unruh/`. Knihovna: `lib/toe/spectraltriple.py`. (F-036)
- [vypocty/VYPOCET-33-ds-conformal-4d.md](vypocty/VYPOCET-33-ds-conformal-4d.md) — Konformně-vázaný 4D dS area-zákon (H6g-2, F-037): xi=1/6 vs xi=0 na 4D dS statické záplatě (rho∈{120,240,480}, 4 seedy, wall 1027 s). R' drift +0,386 identický pro oba; S_full conf/massless=1,0001; masivní SJ PSD (pairing 8,4e-15, Wightman 1e-15 — H6g-2 blokátor odstraněn). VERDIKT: supported (negativ) — 4D area-zákon absence je robustní fyzika; caveat (a) F-031 (xi-část) VYŘEŠEN. Data: `core-data/calculations/ds-conformal-4d/`. Knihovna: `lib/toe/causet.py` (primitiv bd_dalembertian_inverse_massive). (F-037)
- [vypocty/VYPOCET-34-ds-molecule-fluctuation.md](vypocty/VYPOCET-34-ds-molecule-fluctuation.md) — Molekulová fluktuace order-by-disorder 4D dS (H6g-6, F-038): Var(N_mol) vs. A_proper, 5 hustot × 200 seedů, N≤7677, čistě kombinatoricky. Var~rho^0,656, CI95 [0,575, 0,745] vylučuje plochu rho^0.5 i objem rho^1.0; super-Poisson (Fano 3,72->5,30); bit-identická reprodukce. VERDIKT: refuted-direction — druhý nezávislý negativ k F-031 (ani mean, ani variance 4D area-zákon). Data: `core-data/calculations/ds-molecule-fluctuation/`. Knihovna: `lib/toe/causet.py`. (F-038)

### Kolo 16 (VYPOCET-30–31)

- [vypocty/VYPOCET-30-modular-kms-thermal.md](vypocty/VYPOCET-30-modular-kms-thermal.md) — KMS/tepelná osa causal-sets<->NCG (H6g-1, F-034): SJ modulární tok na 2D Rindlerově slabu (N=300/600/1200, 15 seedů). beta_KMS=1.00000, KMS reziduum 1.9e-16 (strojová přesnost), occ R2=1.000 přes 8 řádů; rho-invariantní boostová diagonála R2=0.953 CV=2.7 %; non-Rindler kontroly selhávají (interval R2=0.053, shuffle R2=0.088); absolutní Unruhova 2pi NEobnovena (ratio=0.786). VERDIKT: partial — tepelná osa má kvalitativní datovou oporu, kvantitativní Unruh chybí. Data: `core-data/calculations/modular-kms-thermal/`. Knihovna: `lib/toe/spectraltriple.py`. (F-034)
- [vypocty/VYPOCET-31-lambda-shot-noise.md](vypocty/VYPOCET-31-lambda-shot-noise.md) — Poissonův shot-noise Lambda fluktuace + boost-invariance (H6g-4, F-035): 4D Minkowského box, 800–16000 seedů. Fanův faktor F=0.9986 +/-0.0112 při 16000 seedech (0.13 sigma od 1); delta_Lambda~V^{-0.484±0.006} (R2=0.999); boost-invariantní Var(N) max z=0.70; mřížkový kontrast 5.13x; bit-identická reprodukce. VERDIKT: supported — shot-noise přežívá F-005 na variance/boost-kovariantní ose, mean-prefaktor nevzkříšen. Data: `core-data/calculations/lambda-shot-noise/`. Knihovna: `lib/toe/causet.py`. (F-035)

### Kolo 15 (VYPOCET-29)

- [vypocty/VYPOCET-29-spectral-triple-modular.md](vypocty/VYPOCET-29-spectral-triple-modular.md) — Spektrální triple vs. SJ modulární Hamiltonián (H5g-4, F-033): surogátní D_K=sgn(K)sqrt(|K|), 2D slab T=0.30, N=1200, 5 seedů. Funkcionální kalkul exaktní (scale=1.0, R^2=1.0). BW boostová diagonála lineární (R^2=0.955, PASS). Off-diag spad log-log R^2=0.765 (pod prahem 0.8). Weylova dimenze 1.54 (pod [1.7,2.3]). **KLÍČOVÝ TEST — Connesova vzdálenost:** Pearson korelace s kauzální vzdáleností = 0.319, R^2=0.10 (16 párů, malý vzorek; kolo-21 reprodukční oprava committed 0.098 -> 0.319, verdikt no-match nezměněn) — plochost fyzikální (optimalizátor ověřen na 1D řetězci). VERDIKT: **no-match na metrické úrovni**, boostová osa solidní (Connes-Rovelli tepelný čas). Hrana causal-sets <-> NCG instancována jako informovaný negativ. Data: `core-data/calculations/spectral-triple-modular/`. Knihovna: `lib/toe/spectraltriple.py`, test `app/tests/test_toe_spectraltriple.py`. Runtime 327.6 s. (F-033)

### Kolo 14 (VYPOCET-26–28)

- [vypocty/VYPOCET-26-kerr-b-exponent.md](vypocty/VYPOCET-26-kerr-b-exponent.md) — H5g-5 uzavřena: B(a) v W_sr~Omega^B je SPOJITÁ funkce strhávání, ne dimenzní konstanta D-1=3. Neomezený log-log fit (oprava artefaktu meze A=100): Kerr B(a) 6.10(a=0.3)→2.54(a=0.99), trend dB/da=-2.20 (z=-33.6), chi2_const=2473/7. Konstantní model B=3 zamítnut; BTZ pod Kerr křivkou při srovnatelném rotačním parametru (gap -1.10/-0.55) — role asymptotiky potvrzena. Implikace pro draft-01 §4.2 uzavřena. N=1600, 5 seedů, 8 spinů, wall-clock 12.6 min. Data: `core-data/calculations/sj-kerr-b-scan/`. (F-030)
- [vypocty/VYPOCET-27-4d-amol-convention.md](vypocty/VYPOCET-27-4d-amol-convention.md) — 4D A_mol konvenční otázka VYPOCET-25 VYŘEŠENA (F-031). Diagnóza rho^1.77: horizon_link_count_4d počítá kodim-1 světočáru-tubus, NE kodim-2 entanglement 2-plochu; raw ~ rho^1.72 = (n_sub~rho^1.00) x (4D link-multiplicita~rho^0.655). Korigovaná kodim-2 molekula (toe.causet.horizon_molecules_codim2, k_tube=1.5): A_mol^codim-2 ~ rho^(0.494±0.006) = přesně rho^0.5. Avšak R'=S_full/A_codim2 driftuje rho^+0.55 — S_full škáluje objemově (~rho^0.997). 4D area-zákon genuinně nepřítomný v ploché-kauzální + dS-sech² konstrukci. Konformní caveat neotestován. Nový lib primitiv + test `test_toe_horizon_molecules_codim2.py`. Data: `core-data/calculations/ds-amol-convention/`. (F-031)
- [vypocty/VYPOCET-28-proxy3-seeds.md](vypocty/VYPOCET-28-proxy3-seeds.md) — proxy3 (CV self-averaging) 2D-diamant vN-type dorozhodnuta (F-032). Na VYPOCET-12 původním gridu [400..1800]: 8 seedů t=1.48 (NEsig, reprodukuje VYPOCET-12 null), 30 seedů t=2.15 (sig), 50 seedů slope=-0.224±0.069 (t=3.25, CI [-0.30,-0.15], factor_like=True). Na 5-bodovém gridu [300..1700]: 50 seedů t=4.38. 2D diamant upgradován ze 2/3 (F-015) na 3/3 při >=30 seedech. Klíčová výhrada: upgrade je genuinní seed-count efekt; nový grid nízko-seedový t=5.37 není srovnatelný s VYPOCET-12. Runtime ~17.8 min. Data: `core-data/calculations/vn-type-proxy3-seeds/`. (F-032)

### Kolo 13 (VYPOCET-25)

- [vypocty/VYPOCET-25-scaled-ds-entropy.md](vypocty/VYPOCET-25-scaled-ds-entropy.md) — Škálovaná kampaň dS entropie (F-029): vyhodnocení GH Actions artefaktů z kol 12–13. **2D (ds_entropy_cap_2d, rho 240–1200, ℓ 0.7–2.5, n=10 buněk):** R_full = 0.130 ± 0.0039 (CV 3.0 %), drift rho^{+0.007} ≈ nula, cross-HW reprodukce F-028 v rámci CV — 2D area-zákon publikovatelně silný. **4D (ds_cap_4d, rho 60–1920):** c^{4D} roste 5.6 → 65.8, R^{4D} ~ rho^{−0.72} — žádná čistá 4D area-konstanta (A_mol ~ rho^{1.77}, konvenční otázka otevřena). **F-025 saturace:** rho=120 čistá (AIC saturující vs. lineární), rho≥600 compute-bound. Driver budget/checkpoint fix: sub-cell BudgetExceeded + begin_cell/update_live/complete_cell (per seed/box); nový test `test_max_hours_enforced_mid_cell`. Data: `compute/results-archive/`. (F-029)

### Kolo 12 (VYPOCET-23–24)

- [vypocty/VYPOCET-23-ds-entropy-cap.md](vypocty/VYPOCET-23-ds-entropy-cap.md) — A/4 strop dS entropie vs. Gibbons-Hawking (H5g-2, F-028): 2D dS statická záplata, entanglementový řez r*=0.8, toe v0.3.0 sparse. Primární kanál R_full = S_full_cap/A_mol = 0.1321±1.3% KONSTANTNÍ přes 5× hustotu ρ∈{240,600,1200} a 2× velikost ℓ∈{0.7,1.0,1.5}: kvantitativní area-zákon S_cap=A/(c·G), c≈7.57. Truncovaná SSEE je O(1) a NEsleduje A_mol (kanál není A/4). Anti-kruhovost: ε~ρ^(−1/2) zafixováno z NEZÁVISLÉHO F-006 před měřením. **Verdikt: slabá H5g-2 POTVRZENA** (konstantní area-zákon); **silná H5g-2 VYVRÁCENA** (c≈7.57≠4). Data: `core-data/calculations/ds-entropy-cap/`. (F-028)
- [vypocty/VYPOCET-24-ds-tracial-probe.md](vypocty/VYPOCET-24-ds-tracial-probe.md) — Tracialní (max-entropický) podpis II₁ dS záplaty při ρ∈{10³,3×10³,10⁴}, retest VYPOCET-19 Část 3 (F-027): Část A (hustá, N≤3000, 3 seedy): dS IR-frakce sklon +0.495±0.112, plochá +1.493±0.483 — mezera ZÁPORNÁ (−0.998±0.495); Část B (řídká, truncovaný obsah ρ=10⁴): dS S_trunc saturuje (sklon +0.068), plochá roste (sklon +1.220, 18× strmější); sparse=dense validace S_trunc rel diff 4.1e-14. **Verdikt NULL UZAVŘEN**: tracialní akumulace neviditelná pro SJ+κ sondu v 2D (tracialní stav v mezeře mezi UV pile-up a IR gap); identifikace II₁ stojí na saturaci obsahu (F-023). Nosná oprava: sparse buildery berou (u,v)=(t−r*,t+r*), ne (t,r*). toe v0.3.0 koordinátová chyba: matvec rel err 0.63 s (t,r*), 3.9e-16 s (u,v). Runtime Part A 285 s + Part B 677 s. Data: `core-data/calculations/ds-tracial-probe/`. (F-027)

### Kolo 10 (VYPOCET-21–22)

- [vypocty/VYPOCET-21-desitter-4d-area-law.md](vypocty/VYPOCET-21-desitter-4d-area-law.md) — 4D dS statická záplata: truncovaná area-law SSEE (H5g-1, F-025): sech²-vážený 4D slab, iΔ, n_max=2N^{3/4}, N≤2496, 4 seeds. R*-exponenty dS a=0.27 vs plochá a=0.52 (reálný 4D signál); S_trunc~N^{0.717} (CI68 [0.697,0.739], R²=0.993); N_total strop 480 (R²=1.000) vs lineární růst ploché — F-023 II₁/II_∞ disk. do 4D. Plná saturace nedosažena při N≤2500. Verdikt PARCIÁLNÍ. `lib/toe` rozšířena: `sprinkle_ds_static_patch4d`, 6 nových testů, regrese čistá. Runtime 292 s. Data: `core-data/calculations/sj-desitter-4d/`. (F-025)
- [vypocty/VYPOCET-22-modularni-tok-codim2.md](vypocty/VYPOCET-22-modularni-tok-codim2.md) — Modulární tok: codim-2 klínová hrana jako 4D analog rohu? (H5g-3, F-026): BD d'Alembertián, N∈{800–2200}, 3 seeds. nl-vs-hrana sklon +0.115 (CI68 [0.106,0.124]) a wall-controlled +0.251 — oba KLADNÉ, stejné znaménko jako 4D null-tip, opačné než 2D roh. Edge/bulk f_nl=0.914. Diagonální boost-linearita R²=0.92 (BW slab strana přežívá). 1/4 signatur H5g-3. Verdikt H5g-3 VYVRÁCENA. 5 lib_proposals v results.json. Runtime 97 s. Data: `core-data/calculations/modular-flow-codim2/`. (F-026)

### Registr nálezů

- [../core-data/findings.json](../core-data/findings.json) — Registr **41 originálních nálezů** (kola 1–22, aktualizováno 2026-06-09): F-001–F-039 viz předchozí kola; **F-040 (VYPOCET-37, kolo 22)** geometrický/gamma_5-gradovaný boostový Dirac — confirmed-mixed-sharper-negative; sudý spektrální triple well-posed, log-komprese F-036 vyřešena, absolutní 2pi nedosažitelná (Route3 driftuje); **F-041 (VYPOCET-38, kolo 22)** NCG<->d_s heat-kernel — confirmed (smíšený); d_s=1.998±0.044 z téhož Tr e^{-sigma D^2} (MATCH F-001 tol), a4/a0 NEreprodukuje -18/11 (honest negativ). Každý nález rozlišuje reprodukci literatury od projektového přínosu.

### Fragmenty pilířů (`core-data/fragments/`)

Osmnáct strojově zpracovatelných JSON fragmentů (koncepty, vzorce, reference, problémy, souvislosti), jeden na pilíř — viz per-pillar počty v `PROGRESS.md § Statistiky`.

### Přezkum a sloučení (`core-data/_review/`)

- [../core-data/_review/concept-merge-candidates.json](../core-data/_review/concept-merge-candidates.json) — 80 kandidátních párů konceptů k posouzení soudcem (7 skupin sloučeno, 61 zamítnuto).
- [../core-data/_review/merge-decisions.json](../core-data/_review/merge-decisions.json) — Záznam přijatých a zamítnutých sloučení konceptů ze soudcovského průchodu.
- [../core-data/_review/problem-merge-candidates.json](../core-data/_review/problem-merge-candidates.json) — Kandidáti na sloučení duplicitních otevřených problémů (2 páry sloučeny).

---

## Výpočty (`knowledge-base/vypocty/` + `core-data/calculations/`)

Třicet osm výpočtů dokončeno (VYPOCET-01..38, 37 calc adresářů — 3 adresáře nesou 2 writeupy): čtyři v prvním deep-dive kole, tři v rozhodujícím kole, tři v kolech 3–4, dva v kole 5, dva v kole 6, dva v kole 7, dva v kole 8, dva v kole 9, dva v kole 10, dva v kolech 11–12, dva v kolech 12–13, tři v kole 14, jeden v kole 15, dva v kole 16, tři v kole 18 (VYPOCET-32/33/34), dva v kole 19 (VYPOCET-35/36). Každý má writeup v `knowledge-base/vypocty/` a strojová data (calc.py + results.json + plots) v odpovídajícím podadresáři `core-data/calculations/`.

### Kolo 1 (VYPOCET-01–04)

- [vypocty/VYPOCET-01-ds-klasifikace.md](vypocty/VYPOCET-01-ds-klasifikace.md) — Klasifikační tabulka d_s^UV(z, D, probe): symbolický master d_s=D/γ ověřen (sympy), 12/12 numerických kontrol; probe-dependence doložena (CST dává 2 i >D ze stejné teorie), čímž je vyřešen rozpor connections 657 vs. 1777.
- [vypocty/VYPOCET-02-a4-matching.md](vypocty/VYPOCET-02-a4-matching.md) — Anomaly-matching test NCG SM algebry C⊕H⊕M₃(C): fermionový sektor koef(C²)/koef(Euler)=−18/11 exaktní pro 45 i 48 fermionů; plná SM s bosony jednoznačně falzifikována (−0,853 vs. −1,636).
- [vypocty/VYPOCET-03-lambda-prefaktory.md](vypocty/VYPOCET-03-lambda-prefaktory.md) — Srovnání Λ prefaktorů (Sorkin, EDT, CosMIn): κ_Sorkin/κ_EDT = 139,6 ≈ 140×; silná sjednocující hypotéza vyvrácena, srovnání jako takové je první svého druhu v literatuře.
- [vypocty/VYPOCET-04-ssee-diamant.md](vypocty/VYPOCET-04-ssee-diamant.md) — SSEE na sprinklovaném 2D kauzálním diamantu: entropický cutoff škáluje jako rank~N^0,519 → ε~ρ^(−1/2), potvrzuje area-law ansatz a vylučuje ρ^(−1/4) na 39 σ; volume-law 95,2 → area/log-law 1,58 po truncaci.

### Rozhodující kolo (VYPOCET-05–07)

- [vypocty/VYPOCET-05-sj-rotujici-btz.md](vypocty/VYPOCET-05-sj-rotujici-btz.md) — SJ stav v rotujícím BTZ ergoregionu (M=1, J=0,6, N=1600): 796+/796− eigenvalue, reziduál 4,6×10⁻¹⁶ (strojová přesnost); statický řez na témže r není Lorentzův; kauzální asymetrie uvnitř ergoregionu +1,000 vs. 0,007 vně; nulový sklon mizí přesně na r_erg=1,0. Teze H2g-6 numericky potvrzena ve 2D sondě. Data: `core-data/calculations/sj-rotating-btz/`.
- [vypocty/VYPOCET-06-ssee-4d.md](vypocty/VYPOCET-06-ssee-4d.md) — 4D SSEE cutoff scaling test (predikce p=3/4): predikce NEPOTVRZENA; exponent závisí na cutoffu (0,65–0,98); slope-knee dává ~N¹; 4D nested diamant dává VOLUME law (R²=0,998) dle literatury. H2g-3 oslabena. Data: `core-data/calculations/ssee-4d/`. Runtime: 1517 s.
- [vypocty/VYPOCET-07-bmv-as-faze.md](vypocty/VYPOCET-07-bmv-as-faze.md) — BMV AS fázová korekce (Bonanno-Reuter): AS δφ/φ ≈ 6,2×10⁻²⁸ při d=100 µm (klasický RG, bez ħ); EFT ≈ 3,4×10⁻⁶² (kvantový, s ħ); poměr AS/EFT ≈ 1,82×10³⁴; obě 24 resp. 59 řádů pod dosažitelností. Oppenheimova varianta potvrzena jako jediný realisticky diskriminující experiment. H2g-8 posílena. Data: `core-data/calculations/bmv-as-phase/`.

### Kolo 3 (VYPOCET-08)

- [vypocty/VYPOCET-08-sj-kerr-ekvatorialni.md](vypocty/VYPOCET-08-sj-kerr-ekvatorialni.md) — Kerr ekvatoriální SJ stav: VŠECHNY čtyři BTZ signatury replikovány (strojová přesnost uvnitř ergoregionu, null-sklon nula přesně v r_erg=2M, A_caus>0 vs. A_W<0 na každém (a,r), A_caus monotónní se spinem 0.197/0.361/0.482 pro a=0.3/0.6/0.9). Geometrická nezávislost SJ vlastností v dragged spacetimes prokázána (F-009). Data: `core-data/calculations/sj-kerr-equatorial/`.

### Kolo 4 (VYPOCET-09–10)

- [vypocty/VYPOCET-09-ssee-bd-4d.md](vypocty/VYPOCET-09-ssee-bd-4d.md) — BD d'Alembertián spektrum (H04 interpretace b): BD dává čistý mocninový zákon λ_k~k^-α (R²≈0.99) vs. plochý link-matice spektrum — tvar spektra potvrzen. Ale α driftuje s N (+1.28 za N=500–3000, nekonvergoval), slope-knee p≈N¹, area/volume cutoff-závislé. Hlubší selhání než objekt-specifické (F-012). Runtime 394 s. Data: `core-data/calculations/ssee-bd-4d/`.
- [vypocty/VYPOCET-10-superradiance-eigenvektory.md](vypocty/VYPOCET-10-superradiance-eigenvektory.md) — SJ eigenvektorová rotace + superradiance + toy-model mechanismus: rotace ~44.6° kladného podprostoru při <2% spektrální změně; superradiantní váha v ω(ω−kΩ)<0 monotónní se spinem a k ergosféře; toy null-diamond model reprodukuje A_caus>0 (kauzální geometrie) a A_W<0 (Wightmanova funkce) s korelací 0.95–0.97 (F-013). Nejslabší body draftu-01 vyřešeny. Data: `core-data/calculations/sj-eigenvector-superradiance/`.

### Kolo 5 (VYPOCET-11–12)

- [vypocty/VYPOCET-11-graviton-index.md](vypocty/VYPOCET-11-graviton-index.md) — Graviton sektor + index-teorém (H3g-4, calc11): fyzikální Einstein graviton nekonformní → nemá čisté (a,c); konformní Weyl graviton dává c/(−a)=−398/261; žádný boson kolineární s Weylovým fermionem; x gravitonů pro vynucení −18/11 je −143/32<0 (nefyzikální). Spinorové a₄ koeficienty v bázi {C²,E₄,R²}: (−1/20, +11/360, 0), shoda s Duff Tab.1 exaktně. Rohlinův zámek: ind(D)=−2 (sudé celé). Spektrální akce = Sacharovova fermionově-indukovaná gravitace potvrzena. H3g-4 POSILENA. Draft-02 vědecky uzavřen. Vše sympy exaktní. Data: `core-data/calculations/a4-graviton-index/`. (F-014)
- [vypocty/VYPOCET-12-vn-typ-truncace.md](vypocty/VYPOCET-12-vn-typ-truncace.md) — Typ vN algebry + SSEE truncace v 2D (H3g-3, calc12): 2D, N=400–1800, 8 seeds. Proxy 1 (entropy-trace): S_full~N^1.04 (volume, III) → S_trunc 1.30–1.70 (area/log, II), 80x kolaps. Proxy 2 (modulární spektrum eps): untruncated Connes III₁ (flat/dense, frakce 0.087±0.006) → truncated typ II (8–20 módů, IR edge eps>1.6). Proxy 3 (CV centrální posloupnosti): samo-průměrující, nediskriminuje. Pauli-Jordan nukleární norma jen ~20% kontroly — typ v stavu/entropii, ne kinematice. Verdikt MIXED 2/3 = první přímý numerický důkaz crossed-product obrazu na kauzální množině (2D). Data: `core-data/calculations/sj-vn-type/`. (F-015)

### Kolo 6 (VYPOCET-13–14)

- [vypocty/VYPOCET-13-ssee-slab-4d.md](vypocty/VYPOCET-13-ssee-slab-4d.md) — 4D SSEE slab geometry (H04 interpretace c, calc13): half-space cut (iΔ, κ=0.05·λmax) dává AREA law S~L^2.00 (R²=0.982); interiérní edge-effect kontrola S~L^2.18 (R²=0.989) — čistší area. Kontrast s 4D diamantem (VYPOCET-06) VOLUME S~f^6.1: rohová geometrie (ne dimenze) rozhoduje. Hadamardova diagnostika lokalizuje non-Hadamard anomálii do rohů diamantu (inside vs corner: −1.53 vs −2.79 v 4D; −0.160 vs −0.095 v 2D); slab bez anomálie (deep≈surface: −3.81≈−3.85). Interpretace (c) POTVRZENA, (a) vyvrácena. Runtime 264 s, N≤2088. Data: `core-data/calculations/ssee-slab-4d/`. (F-016)
- [vypocty/VYPOCET-14-threshold-scan.md](vypocty/VYPOCET-14-threshold-scan.md) — Superradiantní nástup: ergosféra vs. Ω(r) (H3g-1, calc14): W_sr radial scan Kerr a=0.6 [0,0.145], a=0.9 [0,0.222]; BTZ J=0.9 analogicky. ΔAIC(E vs. S)=+441.6/+4216.3/+231.5 — rozhodující pro Model S (W_sr~Ω^B; B=4.23/3.82/1.71). A_W negativně-definitní ve všech 65 externích měřeních; amplituda sleduje |Ω| (near-erg ~0.5 vs far ~0.04, faktor 15–20). BTZ cross-check J=0.9 reprodukuje stejný vzorec. H3g-1 POTVRZENA. Zbývá: disambiguation a=0.6 hustším scanem r=5–20M (VYPOCET-15). N=1600, 5 seeds. Data: `core-data/calculations/sj-threshold-scan/`. (F-017)

### Kolo 9 (VYPOCET-19–20)

- [vypocty/VYPOCET-19-desitter-II1.md](vypocty/VYPOCET-19-desitter-II1.md) — SJ na dS statické záplatě × vN typ II₁ vs II_∞ (CLPW diskriminátor, F-023): konformní trik (sech² vlastní míra, ohraničená záplata = konečná stopa = II₁); N_total saturuje 442→480 (dS) vs. roste 768→3360 (plochá kontrola); S_full saturuje a překlápí (dS, R²=0.990) vs. roste (plochá, sklon +12.2); mezera late-half dS −13.1 vs plochá +21.7 = DISKRIMINOVÁNO. Tří-proxy baterie na dS záplatě: 2/3 proxy pass (stopa III→II, modulární pile-up N^{1.25}→0); Část 3 tracialní přístup poctivý null (threshold ρ~10³–10⁴). Poctivá 2D limita: rozdíl II₁/II_∞ žije v obsahu oblasti, ne truncované entropii. Runtime 431 s. Data: `core-data/calculations/sj-desitter-type/`. (F-023)
- [vypocty/VYPOCET-20-modularni-tok-bd-4d.md](vypocty/VYPOCET-20-modularni-tok-bd-4d.md) — BD d'Alembertián modulární tok v 4D: slab vs. diamantový roh (H4g-1, F-024); slab off-diag sklon −1.10 vs. diamant −0.52 (kontrast přítomen, správný směr, větší než 2D gap); rohová koncentrace f_nl nereplikuje čistě (f_nl 0.445, nl-vs-corner +0.71); 3/5 signatur podpořeno. Link-matice 4D null z VYPOCET-18 je z části objekt-závislý artefakt; slab boost-geometricity s BD robustní; H4g-1 4D parciální (2D výsledek zůstává primárním důkazem). Data: `core-data/calculations/modular-flow-bd-4d/`. (F-024)

### Kolo 8 (VYPOCET-17–18)

- [vypocty/VYPOCET-17-lambda-indukce.md](vypocty/VYPOCET-17-lambda-indukce.md) — Λ-indukce přes spektrální akci (H4g-3, F-020): exaktní sympy + literatura (CC hep-th/9606001 + Marcolli). a₀ (kosm.) a a₂ (EH) jsou cross-order (f₄Λ⁴ vs f₂Λ²) → jejich poměr dimenzionální a scheme-závislý; žádná druhá index-identita pro Λ_cc/M_Pl² neexistuje. STr 1 = −62 (bez ν_R) / −68 (s ν_R); ν_R nerovnováhu zhoršuje. Indukovaná γ₀ cutoff-kvartická (10¹²²). H4g-3 VYVRÁCENA. Draft-02 Λ-riziko uzavřeno. Data: `core-data/calculations/lambda-induced/`. (F-020)
- [vypocty/VYPOCET-18-modularni-tok-roh.md](vypocty/VYPOCET-18-modularni-tok-roh.md) — Modulární tok: slab vs. diamantový roh (H4g-1, F-021): 2D, N=400–1800, 5 seeds. Off-diag sklon modulárního kernelu: slab −0.47 (geometrický/boost-lokální) vs. diamant −0.094 (negeometrický), gap 0.37 stabilní. Diagonální modulární váha lineární v vzdálenosti od entangling surface (R²=0.977 = BW boost-váha). Per-site f_nl: bulk 0.673 → roh 0.828, sklon −0.383 (R²=0.989); roh/bulk=1.15. Poctivé nuly: cross-corner coupling ratio=1.00; integrovaná f_nl neodliší slab od diamantu. 4D (link matice, N≤2500): NEREPLIKUJE. H4g-1 PODPOŘENA v 2D (4/5), 4D nereplikuje. Runtime 248 s. Data: `core-data/calculations/modular-flow-corner/`. (F-021)

### Kolo 7 (VYPOCET-15–16)

- [vypocty/VYPOCET-15-far-zone.md](vypocty/VYPOCET-15-far-zone.md) — Far-zone disambiguace VYPOCET-14 pro Kerr a=0.6 (H3g-1, calc15): log-log diskriminant corr(log W_sr, log Ω)=0.9992 vs. corr(log W_sr, log 1/(r−r_erg))=0.942 — Model S; joint fit near+far (n=19, r=2.05–20M): ΔAIC(E−S)=+3894 (rozhodující). Near-zone A_W mocninový zákon: |A_W|~r^{−2.75±0.03} (předp. −3, R²=0.957), |A_W|~Ω^{0.98±0.01} (předp. +1, R²=0.932). Far-zone (13 radii, r=5–20M): W_sr=0 (pod mřížkovým rozlišením), A_W<0 všude. VYPOCET-14 ambiguita uzavřena; Ω(r) potvrzen pro Kerr a=0.6/0.9 + BTZ J=0.9. N=1600, 5 seeds. Data: `core-data/calculations/sj-far-zone/`. (F-018)
- [vypocty/VYPOCET-16-vn-typ-slab-4d.md](vypocty/VYPOCET-16-vn-typ-slab-4d.md) — vN-type proxy v 4D slab (H3g-3, H4g-4, calc16): 4D box-slab, iΔ, interior half-space cut, T=0.5, L=0.85, N=800–3500, 5 semen. Proxy 1 (entropická stopa): S_full~N^{1.34} (III divergentní) → S_trunc~N^{0.55}≈sqrt(N) (4D area law, II), kolaps 36x; fixní-frakce SELHÁVÁ. Proxy 2 (modulární spektrum): untruncated Connes III₁ (pile-up~N^{1.27}) → truncated typ II (pile-up=0, IR hrana eps~2.7, kompaktní nosič). Proxy 3 (p=3/4): N^{3/4} number-truncace → area law YES; fixní-frakce SELHÁVÁ; slab nemá vlastní ostré koleno (auto-koleno ~N^{1.06}) → N^{3/4} je crossed-product předpis, ne spektrální rys. Pauli-Jordan chyba 7.1e-14. Verdikt 3/3 proxy = H3g-3 podpořena v d=4. Runtime 158 s. Data: `core-data/calculations/vn-type-slab-4d/`. (F-019)

---

## Hypotézní dossiery (`knowledge-base/hypotezy/`)

Čtyři detailní dossiery pro hypotézy prošlé novelty-checkem (2026-06-06): shrnutí stavu, blocker-analýza a doporučené první testy.

- [hypotezy/H01-gamma-cardy.md](hypotezy/H01-gamma-cardy.md) — Cardy-LQG fixace γ≈0,274: jádro c=6k je known (Carlip 1410.5763); identifikován fatální blocker — Senova IR-univerzalita (1205.0971) brání UV-fixaci γ z CFT; UZAVŘENO (program dead).
- [hypotezy/H02-sj-kerr.md](hypotezy/H02-sj-kerr.md) — Sorkin-Johnston vakuum pro Kerr/SdS: genuinely open territory — žádná publikace SJ stav pro rotující ČD nezkonstruovala; Kay-Wald no-go neblokuje; BTZ analog (VYPOCET-05) + Kerr (VYPOCET-08) + mechanismus (VYPOCET-10) hotovy; draft-01 čeká na revizi.
- [hypotezy/H03-bmv-diskriminator.md](hypotezy/H03-bmv-diskriminator.md) — BMV/QGEM jako diskriminátor přístupů: binary „kvantovost gravitace" test vyřešen; jediný principiálně odlišitelný přístup je Oppenheimova postkvantová teorie (π-fázový posun); AS korekce ~10⁻⁶⁰ neměřitelná.
- [hypotezy/H04-entropy-cluster-reframe.md](hypotezy/H04-entropy-cluster-reframe.md) — H04 entropie-cluster (reframe): 4D link-matice spektrum ploché → BD d'Alembertián je správný objekt (interpretace b); VYPOCET-09 potvrdil tvar spektra (čistý power law), ale α driftuje s N a p=3/4 chybí; váha na interpretacích (a) a (c).

---

## Pilíř 19 (`core-data/fragments/`)

- [../core-data/fragments/von-neumann-algebras.json](../core-data/fragments/von-neumann-algebras.json) — Pilíř 19: von Neumannovy algebry v kvantové gravitaci (27 konceptů, 32 ověřených referencí, 2026-06-06); zahrnuje Tomita-Takesaki modular theory, typ I/II/III algebry, crossed-product construction, JLMS formula, modular-hamiltonian; po konsolidaci se modular-hamiltonian stal TOP HUBem celého grafu (614 uzlů, 2437 hran).

---

## Drafty článků (`papers/`)

> **VSTUPNÍ BOD PRO LIDSKÉHO AUTORA:** [`../papers/REVIZE-PRO-CLOVEKA.md`](../papers/REVIZE-PRO-CLOVEKA.md) — přehledová tabulka (vědecký stav + odhadovaný čas), doporučené pořadí revizí (draft-02 → draft-04 → draft-01 → draft-03), ~80 checkboxů, high-risk položky, absolutní pravidla pro release, příkazy calc.py. Sem jít jako první.

Čtyři drafty čekají na lidskou revizi (2026-06-06); draft-01 upgradován na v0.2 v kole 5; draft-04 napsán v kole 8.

- [../papers/draft-01-sj-rotating-spacetimes/draft.md](../papers/draft-01-sj-rotating-spacetimes/draft.md) — Draft-01 **v0.2** (kolo 5): SJ vakuum v rotujících prostoročasech; název aktualizován (eigenvector signature of superradiance); abstrakt rozšířen o mechanismus opačných znamének, překryv podprostorů 44.6°, superradiantní váha 0.0755; sekce 3.5b, 3.6, 4.1, 4.2 plně integrovány. Blokující pro release: N→∞ studie, analytické SJ pro strižený diamant, srovnání BTZ dvou-bod. funkce, verifikace citací, re-run pipeline (gate §8 TODO.md).
- [../papers/draft-01-sj-rotating-spacetimes/TODO.md](../papers/draft-01-sj-rotating-spacetimes/TODO.md) — TODO list pro draft-01 v0.2; položky 1.4, 3, 6 označeny DONE; nová gate §8 (lidská re-derivace).
- [../papers/draft-02-a4-fermionic-identity/draft.md](../papers/draft-02-a4-fermionic-identity/draft.md) — Draft-02: a₄ fermionová identita (krátká exaktní nota); exaktní identita C²/Euler=−18/11, heat-kernel descent §2, SM falzifikace −0.853 vs −1.636, pozice v trojúhelníku Andrianov-Lizzi/Kurkov-Lizzi-Vassilevich. VYPOCET-11 uzavřel vědecký obsah (graviton identitu nezachrání, Rohlinův zámek). Blokující pro release: lidská re-derivace a₄ koeficientů, citace-check PDF, scheme-dependence ošetření.
- [../papers/draft-02-a4-fermionic-identity/TODO.md](../papers/draft-02-a4-fermionic-identity/TODO.md) — TODO list pro draft-02.
- [../papers/draft-03-ds-classifier/draft.md](../papers/draft-03-ds-classifier/draft.md) — Draft-03 (kolo 6): UV spektrální dimenze jako klasifikátor trojice (z, D, sonda); master-tabulka reprodukuje 12 publikovaných čísel z jediného P(σ) enginu; sonda jako třetí klasifikační osa doložena vnitřním rozporem v databázi (CST d'Alembertián d_s→2 vs. náhodná procházka d_s>D). Sekce „Relation to prior work" vpředu; pozice vůči Hořavovi, Calcagnimu (1311.3340), Mielczarek–Trześniewski (1708.07445), Carlipovi, Eichhorn–Mizera, Belenchiovi. Blokující: obrana vůči „Calcagni přebalený" a „probe-trivialita" (viz TODO.md).
- [../papers/draft-03-ds-classifier/TODO.md](../papers/draft-03-ds-classifier/TODO.md) — TODO list pro draft-03; hlavní referee útok: simultánní engine + sonda jako osa + inverze čtení konvergence.
- [../papers/draft-04-type-transition-causal-sets/draft.md](../papers/draft-04-type-transition-causal-sets/draft.md) — Draft-04 **(kola 8+11, rozšíř. dS sekce)**: typ III₁→II přechod na kauzálních množinách přes Sorkin-Yazdi SSEE truncaci; tři finite-N proxy (entropická stopa, modulární spektrum, centrální-sekvence/rank); 2D diamant 2/3 proxy; 4D slab 3/3 proxy s N^{3/4} selektivitou; **§4.3 De Sitter static patch** (přidáno kolo 11): CLPW II₁ vs II_∞ diskriminátor — 2D F-023 'supported' (N_total saturuje R²=1.000), 4D F-025 'partial' (S_trunc~N^{0.717}, exponent 0.27 vs 0.52 ploché, plná saturace nedosažena); konformně-váhový caveat; původní geometrický caveat přečíslován §4.4. Blokující: 8+§7b lidských verifikačních bran (incl. dS re-run, 2 nové arXiv ID); odhad revize 16–26 h.
- [../papers/draft-04-type-transition-causal-sets/TODO.md](../papers/draft-04-type-transition-causal-sets/TODO.md) — TODO list pro draft-04; hlavní referee útaky (proxy ≠ typy, N^{3/4} jako prescription vs. spektrální feature, Gaussův stav); etická poznámka AI asistence; 8 lidských verifikačních bran.
- [../papers/draft-06-discrete-program-limits/draft.md](../papers/draft-06-discrete-program-limits/draft.md) — Draft-06 **v0.1 (2026-06-09): „mapa negativů"** — negative-results letter konsolidující tři ostré zdi druhého oblouku: (1) 4D entropicko-plošný zákon GENUINNĚ CHYBÍ (pohřben 3× — mean F-031, konformní F-037, variance F-038; 2D konstanta je dimenzní náhoda point-horizonu); (2) surogátní modulární Dirac nese boostovou strukturu, ne absolutní Unruh teplotu (off 52 %, F-036) ani Connesovu metriku (korelace 0,32, F-033) — log-komprese ε-spektra; (3) diskrétní SSEE koeficient c_EE≈7,56 je geometrický, ne anomální racionál (−18/11 off 362 %, F-039). Každá zeď pojmenovává chybějící ingredienci (zakřivený propagátor / geometrický-boost Dirac s γ₅ / anomálně-citlivý koeficient). DRAFT banner, jen existující findings, žádné nové arXiv ID. (Pozn.: slot draft-05 byl zvažovaný standalone dS-letter H5g-6, který se vlil do draft-04 §4.3.)
- [../papers/draft-06-discrete-program-limits/TODO.md](../papers/draft-06-discrete-program-limits/TODO.md) — TODO list pro draft-06; kritické: doplnit ověřená arXiv ID konvenčních referencí (CHM/Solodukhin/BW/Unruh), nepřeprodat negativy jako no-go, čísla vs findings; rozhodnout venue (standalone letter vs. appendix k draft-04).
- [../papers/REVIZE-PRO-CLOVEKA.md](../papers/REVIZE-PRO-CLOVEKA.md) — **LIDSKÝ VSTUPNÍ BOD** (kolo 9): přehledová tabulka stavu všech 4 draftů + odhadovaný čas revize; doporučené pořadí (draft-02 → draft-04 → draft-01 → draft-03); ~80 checkboxů pro (A) matematické re-derivace, (B) kontrolu citací proti PDF, (C) čísla vs results.json, (D) vědecké konvence; kritické high-risk položky (arXiv ID 2025–2026, placeholder a_err=0.776, ilustrativní hodnota 8 v CST); absolutní pravidla pro release (jmenovaný autor, AI-assistance statement, veřejný calc.py); přesné příkazy pro re-run všech 12 calc.py.

---

## Eseje (`knowledge-base/eseje/`)

Čtyři syntetické eseje (2026-06-06) rozvíjející nejhlubší motivy výzkumných kol.

- [eseje/ESEJ-01-dimenze-jako-otazka.md](eseje/ESEJ-01-dimenze-jako-otazka.md) — „Dimenze jako otázka": probe/observer-dependence jako generický klasifikační princip (H2g-1) — geometrická veličina je odpověď na (otázka, sonda), ne atribut oblasti; formalizace falzifikací F1/F5.
- [eseje/ESEJ-02-vesmir-ktery-se-pocita.md](eseje/ESEJ-02-vesmir-ktery-se-pocita.md) — „Vesmír, který se počítá": faktor 140 (Sorkin/EDT) jako možný směnný kurz mezi definicemi atomu prostoročasu (H2g-4); Everpresent Λ a swampland-kompatibilní de Sitter bez kvintesenčního pole (H2g-5).
- [eseje/ESEJ-03-gravitace-jako-stin.md](eseje/ESEJ-03-gravitace-jako-stin.md) — ESEJ-03 (kolo 6): syntetická esej k výsledkům kola 6.
- [eseje/ESEJ-04-vstup-pozorovatele.md](eseje/ESEJ-04-vstup-pozorovatele.md) — ESEJ-04 (kolo 9): syntetická esej k výsledkům kola 9 — dS II₁ diskriminátor a BD 4D modulární tok.

---

## Verifikační reporty (`verification/`)

Složka obsahuje 18 adversariálních verifikačních reportů, jeden pro každý pilíř, generovaných při zakládání báze (2026-06-05). Každý report dokumentuje zkontrolované citace, nalezené chyby a opravy. V průběhu economy runu téhož dne bylo 5 pilířů znovu re-verifikováno s hlubším přístupem na zdroje: **causal-sets** (3 opraveny, 2 zbývající obavy), **group-field-theory** (3 opraveny, 3 zbývající obavy), **twistors-amplitudes** (3 opraveny, 3 zbývající obavy), **emergent-gravity** (3 opraveny, 2 zbývající obavy) a **experimental-tests** (4 opraveny, 4 zbývající obavy). Podrobnosti viz `PROGRESS.md § Statistiky`. Jednotlivé soubory:

[verification/asymptotic-safety.md](../verification/asymptotic-safety.md) · [verification/black-holes-information.md](../verification/black-holes-information.md) · [verification/causal-dynamical-triangulations.md](../verification/causal-dynamical-triangulations.md) · [verification/causal-sets.md](../verification/causal-sets.md) · [verification/conceptual-problems.md](../verification/conceptual-problems.md) · [verification/emergent-gravity.md](../verification/emergent-gravity.md) · [verification/entanglement-spacetime.md](../verification/entanglement-spacetime.md) · [verification/experimental-tests.md](../verification/experimental-tests.md) · [verification/group-field-theory.md](../verification/group-field-theory.md) · [verification/holography-adscft.md](../verification/holography-adscft.md) · [verification/loop-quantum-gravity.md](../verification/loop-quantum-gravity.md) · [verification/noncommutative-geometry.md](../verification/noncommutative-geometry.md) · [verification/quantum-cosmology.md](../verification/quantum-cosmology.md) · [verification/semiclassical-gravity.md](../verification/semiclassical-gravity.md) · [verification/string-theory.md](../verification/string-theory.md) · [verification/supergravity-uv.md](../verification/supergravity-uv.md) · [verification/swampland.md](../verification/swampland.md) · [verification/twistors-amplitudes.md](../verification/twistors-amplitudes.md)
