# Velké review druhého oblouku — vědecký verdikt po draftech (2026-06-09)

> Referee-grade review companion ke konsolidaci integrity (`reports/2026-06-09-consolidation.md`). Zatímco konsolidace řešila **integritu registrů** (stale data, rozbité odkazy, regen pipeline), tento dokument nese **vědecký verdikt**: je každý draft referee-ready? jaké jsou blokátory? je sada nálezů a dvojí verifikace kompletní? Vstupem byly čtyři nezávislé referee-grade fasety (A: draft-01+03, B: draft-02+06, C: draft-04, D: findings+verifikace). Tento report shrnuje verdikt, automaticky aplikované opravy a **prioritizovaný lidský punch-list** s odhady času. Lidský vstupní bod pro vlastní revizi zůstává `papers/REVIZE-PRO-CLOVEKA.md`.

---

## 1. Verdikt po draftech (referee-ready? blokátory?)

Žádný z pěti draftů NENÍ referee-ready k odeslání — a každý to **sám deklaruje** (DRAFT banner „internal research draft, NOT submitted, requires human review" + TODO brány). To je správný stav: jde o interní explorační/reprodukční/negativní noty, ne hotové papery. Klíčový pozitivní nález napříč všemi fasetami: **žádný draft nepovyšuje status nad `findings.json`, žádné arXiv ID není vymyšlené, scope-caveaty (2D / finite-N / ne-4D) jsou drženy poctivě a opakovaně.** Blokátory jsou tedy téměř výhradně (a) lidská verifikace referencí proti PDF, (b) lidská nezávislá re-derivace/re-run, a (c) novelty-framing — NE chybné vědecké závěry na číslech.

| Draft | Referee-ready? | Třída blokátorů | Nejsilnější referee útok | Odhad lidské revize |
|-------|----------------|-----------------|--------------------------|---------------------|
| **draft-01** (SJ rotující prostoročasy, v0.3) | NE — vnitřně poctivý, kvantitativně bezchybný explorační note; všechna čísla sedí na `results.json` (0 number-mismatch) | Major: chybí kontinuální N→∞ + 30+ seedů; chybí srovnání se ZNÁMÝM BTZ vakuem; chybí analytické SJ pro sheared diamond; 3 chyby v autorství referencí (human); lidská re-derivace neproběhla | „Je to jen zkosený 2D Minkowského diamant, kde je černá díra?" — identifikován v TODO §1.1, ale v draftu NENÍ plně pre-emptován (nejlepší obrana §3.5/§3.5b: rotace žije v eigenvektorech, ne ve spektru) | 15–25 h |
| **draft-02** (−18/11 fermionová identita, v0.2) | NE — aritmetika NEPRŮSTŘELNÁ (nezávisle reprodukováno exact sympy + CAS); blokuje jen framing + 2 ref-chyby + lidská PDF verifikace | Major: chybná atribuce 1106.3263 a hep-th/9503187 (human); novelty-gap nedoložen přímými citáty z 1001.2036/1106.3263 + Connes-Marcolli / van Suijlekom knihy | „Tautologie — znovu jste odvodili, že a₄ = a₄"; headline slovo „theorem/QED" je nejvyšší referee-riziko (TODO §1 ho drží jako blokátor) | 4–8 h |
| **draft-03** (d_s klasifikátor, v0.2) | NE — mimořádně poctivý reproduction/classification note; nejblíže readiness; tabulka d_s sedí na `results.json` i literaturu (ověřeno proti arXiv) | Major: celá hodnota stojí na NOVELTY framing vůči Calcagniho programu — draft to sám přiznává; obrana (single-engine, probe-as-axis, discriminator-inversion) je legitimní, ale framing-claim, ne teorém; D-konvence Hořava (human PDF) | „Calcagni program přebalený" (1311.3340 + 1708.07445); novelty nárok není doložen pozitivní rešerší, jen tvrzen | 10–18 h |
| **draft-04** (typový přechod kauzální množiny + dS §4.3, v0.2) | NE — epistemická poctivost velmi vysoká; ÚSTŘEDNÍ obsah věrný datům; žádný Blocker ve smyslu chybného závěru | Major: 2 chybné autorské atribuce (1712.04227, 2212.10592, human); 2 number-mismatch v §4.4 (S∼L^2.00/A^1.00 jsou CÍLOVÉ, ne naměřené 1.59/0.795 — viz §4 níže); 7/8 lidských bran TODO §8 nesplněno | „Konečná matice = vždy typ I; nic jste neměřili" — preemptivně ošetřeno (N→∞ trendy, ne naměřený typ); „N^{3/4} je předpis" — poctivě přiznáno | 16–26 h |
| **draft-06** (mapa negativů / limity diskrétního programu, v0.1) | NE — referee-ready jako negativní letter PO opravě atribuce 1712.04227 + doplnění kolo-22 forward-note (oboje níže AUTO); čísla sedí, konzistentní s draft-04 §4.3 | Major: chybná atribuce 1712.04227 (human); Wall 2 byl zastaralý vůči kolo-22 F-040 (AUTO-doplněno) | „Negativy konkrétní konstrukce, ne no-go" — §6 explicitně „not no-go theorems" | 8–14 h |

**Pořadí doporučené revize (dle ROI/uzavřenosti):** draft-02 → draft-06 → draft-04 → draft-01 → draft-03. (draft-02 nejmenší a exaktní; draft-06 syntéza hotových výsledků; draft-04 mechanický audit; draft-01 vědecky nejotevřenější; draft-03 nejkřehčí novelty.)

---

## 2. Verdikt sady nálezů (F-001..F-041)

**Sada 41 nálezů je z velké části vědecky čistá a referee-ready pro handoff.** Statusy věrně odrážejí sílu evidence:

- `confirmed` je rezervováno pro exaktní racionální identity (F-003, F-014, F-020) a robustní negativy/falzifikace (F-004, F-005, F-010, F-031-cluster).
- finite-N / multi-proxy výsledky nesou poctivě `supported` nebo `partial` (F-006, F-015, F-019, F-021, F-024, F-025, F-029).
- Druhý-obloukový negativní klastr (F-031/036/037/038/040 + F-033) je vzájemně konzistentní i konzistentní s pozitivy (F-028/029/030/032/035/041): **metrická osa korespondence padá, tepelně/boostová-strukturní osa stojí, absolutní 2π se neobnovuje** — všechny findingy to říkají souhlasně, bez vzájemného sporu.
- Overreach je systematicky hlídán: každý 2D/finite-N výsledek nese explicitní scope-caveat; žádný finding nevydává 2D nebo konečné-N za 4D kontinuum nebo type-theoretic důkaz.

**Žádné vědecké blokátory.** Editorské položky k vyčištění (3 zbylo AUTO-opraveno, viz §3; zbytek na člověku v §4): nestandardní status-řetězce u 4 findingů (kanonický enum), reference-slip kappa→1712.04227, zavádějící `route3_2pi_recovered:true` flag.

---

## 3. Verdikt kompletnosti verifikace (CAS + numerika)

**Dvojí verifikace je kompletní a poctivě dokumentovaná.**

- **CAS dráha** (`verification/cas/`): 175/175 symbolických checků přes 7 Wolfram Language skriptů (faseta D: 33/34 verified + 1 resolved-blocker na úrovni vzorců). **Myrheim-Meyer factor-2 bug RESOLVED** (jmenovatel 4→2 ve fragmentu + consolidate, `resolved_blocker`). −18/11, konformní-graviton −398/261, Λ-ledger struktura nezávisle re-odvozeny mimo sympy.
- **Numerická reprodukce** (`app/tests/test_reproduction.py`): druhý oblouk 10/11 PASS deterministicky v `SLOW_CALCS`; `ds-amol-convention` vědomě vyloučen (čte staged archiv mimo /tmp sandbox) + dokumentován. Kola 22 (F-040, F-041) POKRYTA. Cross-HW (GitHub Actions ubuntu/x86_64/OpenBLAS vs macOS/arm64/Accelerate): 0 verdict flipů, max core odchylka 7.05 %.

**Mezera (nízká priorita):** žádný second-arc calc není pokryt OBĚMA dráhami (CAS i numerika) zároveň — CAS pokrývá symbolické identity, numerika stochastické výpočty; překryv je strukturální, ne plný. Lidská nezávislá re-derivace NENÍ nahrazena ani jednou dráhou (oboje běželo na řízeném prostředí projektu).

---

## 4. Automaticky aplikované opravy (tento review)

Aplikovány POUZE bezpečné, finding-podložené, mechanické opravy (number-mismatch vs findings, chybějící forward-notes, clarity bez změny nároku). Interpretační / úsudkové / vědecké přepisy a referenční atribuce NEbyly aplikovány (HUMAN, viz §5). Žádné arXiv ID nevymyšleno.

### findings.json
1. **F-009 statement (number-mismatch):** `787+/790+ pairs` → `787+/787- pairs for a=0.6, 790+/790- pairs for a=0.9`. Statement chybně slučoval počty z a=0.6 (787±) a a=0.9 (790±) do zavádějícího „787+/790+". Draft-01 §3.1 byl SPRÁVNĚ — chyba byla jen v zápisu findingu. (Draft NEMĚNĚN.)
2. **F-039 statement + F-039 caveat + F-006 caveat (ref-integrity):** atribuce kappa=√N/(4π) opravena z `Sorkin-Yazdi 1712.04227` na `Sorkin-Yazdi 1611.10281`. ID 1712.04227 je Belenchia et al. (EE na causetech); zdroj κ-cutoffu je Sorkin-Yazdi 1611.10281 — ID už v repu (references.json, evidence F-006). Jméno autora i ID nyní souhlasí.

### core-data/calculations/geometric-boost-dirac/results.json (F-040)
3. **`route3_2pi_recovered` flag (number-mismatch):** `true` → `false` + přidáno pole `route3_2pi_recovered_note` dokumentující, že aggregate-mean je v rámci 19 % od 2π, ALE routa je NEkonvergentní (CV=0.205 > 0.15 práh, `route3_rho_invariant=false`, drift 4.747→5.647→7.707 s N). Flag protiřečil headline „sharper-negative" verdiktu; próza findingu byla vědecky správná, problém byl jen v JSON flagu. `wall2_positive=false` beze změny.

### papers/draft-06-discrete-program-limits/draft.md
4. **Wall 2 forward-note (logical-gap — Wall 2 zastaralý vůči kolo-22):** doplněna citačně-vázaná poznámka (F-040, status `confirmed-mixed-sharper-negative`), že pojmenovaný chybějící prvek (geometrický γ5-gradovaný boost Dirac) byl MEZITÍM postaven a VYŘEŠIL log-kompresi (exponent +1, koeficient O(2π)), ale absolutní 2π se neobnovuje — obstrukce se PŘESUNULA na konečné-N diskretizaci (operátorová routa driftuje, CV 0.21). Paralelní F-041 (NCG↔d_s: d_s=2, ale a_4≠−18/11 na plochém causetu) zmíněna. Stejná poznámka přidána do §7 (Summary).
5. **Wall 1 slab-vs-cap rozlišení (ref-integrity / skim-misread):** přidána věta odlišující dS-cap area-zákon (CHYBÍ ve 4D, F-031) od truncated-SSEE slab area-zákona neseného type-II rankem ~√N (PŘÍTOMEN, F-019) — stejné rozlišení, jaké dělá draft-04 v abstraktu, aby drafty nečetly proti sobě.
6. **Abstrakt c≈7.57 1.3 %/3.0 % (number-mismatch):** rozlišeno, že CV 1.3 % je z committed F-028 běhu, zatímco CV 3.0 % je při rozšíření přes 5× hustotu + 3.6× velikost záplaty (F-029).

### papers/draft-01-sj-rotating-spacetimes/draft.md
7. **§3.1 ±-párování (overclaim):** doplněna věta, že ±-párování spektra je ALGEBRAICKÝ důsledek toho, že iΔ = i × (reálná antisymetrická matice), takže reziduum ~10⁻¹⁶ testuje numeriku, ne fyziku.
8. **Abstrakt (vii) + §4.2 (overreach 2D→dimenze):** „evidence that B tracks asymptotic fall-off, not the spacetime dimension" → „consistent with B tracking asymptotic fall-off rather than a privileged dimensional value (one 2D fixed-r construct, not an independent dimension-versus-asymptotics separation)".
9. **§4.2 ΔAIC atribuce (ref-integrity):** upřesněno, že joint ΔAIC=+3894 je F-018 (sj-far-zone), per-geometry rozsah 230–4200 je F-017 (sj-threshold-scan: +442/+4216/+232), B(a) trend je F-030.

### knowledge-base/SYNTEZA-03.md
10. **Forward-note kolo 22 (F-040/F-041):** top-banner doplněn o poznámku, že compute-doporučení #1 (non-surogátní geometrický boost Dirac) bylo PROVEDENO — F-040 vyřešil log-kompresi, ale absolutní 2π drift; F-041 d_s=2 ale a_4≠−18/11. §5 #1 přesunout z „lovit" na „proveden, ostřejší negativ", #2 z „sparse" na „částečně proveden". Verdikty linií 1.2/1.3 se nemění (zostřují se).

**Po opravách:** `app/tests/test_web_build.py` 21/21 PASS (findings.json se rebuiluje na web a počet 41 i obsah sedí); JSON validita findings.json i F-040 results.json ověřena; žádný test neasertoval starou hodnotu `route3_2pi_recovered`.

---

## 5. Prioritizovaný lidský punch-list (per draft, s odhady)

Položky níže NEBYLY aplikovány automaticky — vyžadují lidskou verifikaci proti PDF, nezávislou re-derivaci/re-run, nebo novelty rešerši/úsudek. Plné checklisty per-draft jsou v `papers/REVIZE-PRO-CLOVEKA.md §2`.

### draft-01 (SJ rotující prostoročasy) — 15–25 h

**Blocker (vědecká obrana — referee-ready gate):**
- [ ] **Sheared-diamond útok (TODO §1.1):** doplnit explicitní argument/výpočet, že při fixed-r je jediný gauge-invariant cone-tilt, + alespoň jednu observable odlišující dragging od coordinate shear. Bez toho hostilní referee přerámuje BTZ↔Kerr univerzalitu jako tautologii. Vlastní výpočet + srovnání s Mathur-Surya SJ a se ZNÁMÝM BTZ vakuem je HUMAN+compute. *(Část rámce lze AI, vlastní výpočet ne.)*

**Major:**
- [ ] **Ref-integrita #7 (2212.10592):** opravit autory z „Jubb-Surya, Softened SJ" na **Zhu & Yazdi**, „On the (Non)Hadamard Property of the SJ State in a 1+1D Causal Diamond" (CQG 2024). Ověřit, zda Jubb-Surya nemají SAMOSTATNÝ softened-SJ paper (jiné ID); pokud ne, přeřadit veškerá „softened SJ" tvrzení na Zhu-Yazdi.
- [ ] **Ref-integrita #14 (2007.07211):** opravit autory z „Dafermos-Rodnianski" na **Shlapentokh-Rothman & Teixeira da Costa**, „Boundedness and decay for the Teukolsky equation on Kerr in the full subextremal range |a|<M". Pokud byl míněn klasický Dafermos-Holzegel-Rodnianski výsledek, dohledat správné ID.
- [ ] Kontinuální N→∞ studie + 30+ seedů (strojový čas, ale chybí).
- [ ] Nezávislá lidská re-derivace VYPOCET-05/08/10/14/15.

**Minor:**
- [ ] **Ref #12 (2303.13488):** opravit titul „...on Kerr" → „...on black hole space-times"; doplnit spoluautory **Bernar, Winstanley** (vedoucí Balakumar sedí).
- [ ] **Ref #5 (2504.12919):** doplnit autory **Kastrati & Hinrichsen** a přesný titul „Numerical Evaluation of the Causal Set Propagator in 2D Anti-de Sitter Spacetime" (ID a téma správné).

### draft-02 (−18/11 fermionová identita) — 4–8 h

**Blocker (framing — referee-ready gate):**
- [ ] **„theorem/QED" downgrade:** zvážit downgrade „theorem" → „exact identity forced by one shared a₄". Před povýšením z „internal" splnit novelty-gap (níže). *(Aritmetika je nezávisle reprodukovaná — toto je nedokončená obrana, ne chyba.)*

**Major:**
- [ ] **Ref-integrita 1106.3263:** přepsat VŠECHNY výskyty (abstract, §3, §4, Sources) `Kurkov-Lizzi-Vassilevich` → **Andrianov-Kurkov-Lizzi** (Vassilevich NENÍ autor; Andrianov chybí; ID i titul „Spectral action, Weyl anomaly and the Higgs-Dilaton potential" správné). Zkontrolovat propagaci do VYPOCET-02 a references.
- [ ] **Ref-integrita hep-th/9503187:** ID = **Cho & Kantowski**, „Gauge Independent Trace Anomaly for Gravitons" — NENÍ Duff ani Anselmi (jak tvrdí draft §4 resp. TODO). Ověřit, kterou práci draft skutečně chce pro gauge/scheme-dependenci gravitonového (a,c) (kandidáti Anselmi hep-th/9709047, Duff hep-th/9308075); titul „gauge INDEPENDENT" je v tenzi s tvrzením „gauge-dependent".
- [ ] **Novelty-gap (doložit):** doslovné citáty z 1001.2036 a 1106.3263, že ratio-rovnost −18/11 tam NENÍ napsaná; prohledat **Connes-Marcolli** „NCG, Quantum Fields and Motives" a **van Suijlekom** „NCG and Particle Physics".

**Minor:**
- [ ] **TODO ref 2206.13287:** opravit atribuci „Martini-Nink-Percacci" → **Bastianelli, Bonezzi, Melis**, „Gauge-invariant coefficients in perturbative quantum gravity" (jen v TODO, neblokuje draft).

### draft-03 (d_s klasifikátor) — 10–18 h

**Major:**
- [ ] **Novelty rešerše vs Calcagni (probe-as-third-axis):** provést a ZDOKUMENTOVAT cílenou rešerši (Calcagniho reviews/knihy 1311.3340 etc., follow-upy k 1708.07445 Mielczarek-Trześniewski, cokoli uvádějícího probe jako klasifikační osu). Pokud se najde, downgradovat nárok „probe povýšen na osu" na „we make explicit what was implicit". Bez rešerše zůstává nárok novelty nepodložený (NE nepravdivý). *(Ověřeno proti arXiv: 1311.3340 najde, že d_s NENÍ univerzální; 1708.07445 je survey/mapa — ale ani jeden neuvádí (z,D,probe) jako princip; draft to ale jen tvrdí „We have not found it stated".)*

**Minor (logical-gap, human PDF):**
- [ ] **D-konvence Hořava (TODO §3):** potvrdit proti PDF 0902.3657, že čitatel d_s=1+D/z je **D_space=3**, ne D_spacetime=4, a že z=2→5/2 je v paperu explicitně. (Konvence v draftu je konzistentní s tím, co results.json počítá; ověření Hořava formule + flow 4(IR)→2(UV) pro z=3 PASS proti arXiv abstraktu.)
- [ ] Per-řádkový REPRODUCE audit 12 hodnot + re-run enginu. *(Ilustrativní d_s=8 je správně 4× označen „not from literature"; ověření proti 1311.2530 POTVRZUJE, že Eichhorn-Mizera žádnou univerzální UV konstantu neudávají — caveat oprávněný.)*

### draft-04 (typový přechod kauzální množiny) — 16–26 h

**Major:**
- [ ] **§4.4 number-mismatch (S∼L^2.00/A^1.00):** přepsat na NAMĚŘENÉ hodnoty: „S∼L^{1.59} (R²=0.982), klasifikováno jako AREA dle R²_area>R²_vol (0.984 vs 0.977, TĚSNÁ marže), proti referenčnímu area-law sklonu 2.0". Hodnoty 2.00/1.00 jsou CÍLOVÉ referenční exponenty (`area_law_slope:2.0`), NE naměřené (`fit_S_vs_L.slope=1.590`, `fit_S_vs_area_pow.p=0.795`). **Opravit i F-016 statement v findings.json** (human-required, mění finding). *(NEaplikováno auto: fix reframuje headline klasifikaci na těsnou marži — vědecká re-prezentace + párová editace findingu.)*
- [ ] **Ref-integrita 1712.04227:** opravit „Saravani, Aslanbeigi, Sorkin" / „Sorkin-Yazdi (Saravani-Aslanbeigi)" → **Belenchia, Benincasa, Letizia, Liberati**, „On the Entanglement Entropy of Quantum Fields in Causal Sets". Pokud je míněn κ=√N/(4π) double truncation, citovat **1311.7146 (Saravani-Sorkin-Yazdi)**. Odstranit „Aslanbeigi". Sjednotit ř. 18/90/250.
- [ ] **Ref-integrita 2212.10592:** opravit autory „Yazdi-Mathur-Surya" → **Zhu, Yazdi** (Mathur/Surya pravděpodobně kontaminace z 1906.07952). Potvrdit lokalizaci u−v'=±2L.
- [ ] **Lidské brány TODO §8 (7/8 nesplněno):** re-run 4 calc.py, N-push N>6000 ve 4D, 3. rank scheme, α-nezávislost. *(Tento audit uzavírá část brány §8.3 arXiv verifikace — 2 chybné atribuce nalezeny.)*

**Minor:**
- [ ] **2412.07832:** doplnit autora **Jones**; ověřit, že paper obsahuje výhradu EE↔non-Hadamard „likely NOT directly connected" (load-bearing pro „correlational, not causal" framing).
- [ ] IR edge ε≈2.7 / 39σ exclusion neauditovatelné z results.json — uložit `IR_edge_eps_number` a `sigma_vs_quarter` při příštím re-run.
- [ ] Sjednotit zaokrouhlení 0.55 vs 0.547 mezi §4.2 a §4.3; doplnit journal ref Connes 1973.

### draft-06 (mapa negativů) — 8–14 h

**Major:**
- [ ] **Ref-integrita 1712.04227:** opravit „Sorkin-Yazdi ... double truncation, 1712.04227" → **Belenchia-Benincasa-Letizia-Liberati**; přesměrovat „double truncation"/„κ=√N/(4π)" na **1611.10281** (a/nebo Surya-Nomaan-Yazdi 2008.07697). Zkontrolovat i draft-04 (sdílí konvenční odstavec). *(F-036 už interně tuto záměnu vlajkuje; AUTO-fix v findings.json kappa-atribuci opravil, ale draft text zůstává na člověku.)*

**Minor:**
- [ ] Venue rozhodnutí (standalone letter vs. appendix k draft-04); konvenční ref ID (CHM/Solodukhin/BW/Unruh/Gibbons-Hawking) ověřit proti arXiv. *(Wall 2 forward-note kolo-22 a Wall 1 slab-vs-cap rozlišení už AUTO-doplněno — viz §4.)*

### Napříč drafty / sada nálezů (editorské, human-decision)

**Minor:**
- [ ] **Status-enum normalizace:** F-036/F-038/F-040 (+ F-033/F-034/F-041) používají nestandardní status-řetězce (`informovany-negativ-tautologie`, `refuted-direction`, `confirmed-mixed-sharper-negative`). Normalizovat na kanonický enum (confirmed/supported/partial/refuted/negative) + samostatné textové pole pro nuanci. *(Lidské rozhodnutí o cílovém enumu; popisně bohaté statusy jsou poctivé, ale rozbíjejí strojové filtrování.)*
- [ ] **F-002 status asymetrie:** zvážit downgrade `confirmed` → `supported` kvůli souladu s F-001 (F-002 je syntéza/reframing dvou publikovaných probe-výsledků, ne nový kvantitativní nález).
- [ ] **VYPOCET-34 ř.85:** opravit cross-ref F-034 → F-038 (záměna ID v próze, finding to sám vlajkuje).
- [ ] **F-029 forward-pointer:** volitelně přidat odkaz na F-031 (konvenční zdroj ρ^1.77 diagnostikován v F-031).

---

## 6. Jediná nejdůležitější věc, kterou má člověk udělat první

**Spustit lidskou verifikaci VŠECH arXiv ID proti arxiv.org — je to absolutní gate pro JAKÉKOLI sdílení a tento audit už našel 7 chybných autorských atribucí přežívajících napříč drafty** (draft-01: 2212.10592, 2007.07211, 2303.13488, 2504.12919; draft-02: 1106.3263, hep-th/9503187; draft-04 + draft-06: 1712.04227, 2212.10592). Žádné ID není vymyšlené a obsah/témata sedí — chybná jsou jména autorů. Tato třída chyby je systémová (kontaminace mezi příbuznými papery) a NELZE ji opravit strojově bez rizika; vyžaduje otevřít každé PDF. Dokud neproběhne, nelze citovat nic — a je to nejlevnější brána, která odblokuje draft-02 (4–8 h, nejblíže readiness) a zároveň pokryje gate §8.3 draftu-04.

---

*Anchory: `reports/2026-06-09-consolidation.md` (integrita), `papers/REVIZE-PRO-CLOVEKA.md` (lidský vstupní bod, per-draft checklisty), `core-data/findings.json` (F-001..F-041), `verification/cas/` + `app/tests/test_reproduction.py` (dvojí verifikace). Review fasety A/B/C/D archivovány v orchestraci. Generováno AI review-lead agentem 2026-06-09; všechny položky punch-listu jsou pro lidské splnění.*
