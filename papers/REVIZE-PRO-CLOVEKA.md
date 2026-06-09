# REVIZE PRO ČLOVĚKA — vstupní bod pro lidského výzkumníka

**Stav: 2026-06-09 | Generováno AI koordinačním agentem. Všechny níže uvedené checkboxy jsou určeny výhradně pro lidské splnění.**

> **Toto je JEDINÝ kompletní lidský handoff dokument.** Pokrývá všech **5 draftů** (draft-01/02/03/04/06), všech **41 nálezů** (F-001..F-041), **agentní framework** (tří-rolová smyčka), **dvojí verifikaci** (CAS + numerická reprodukce) a odkazuje na vědecký review companion `reports/2026-06-09-velke-review.md` (referee verdikt per draft + prioritizovaný punch-list) a na integritní konsolidaci `reports/2026-06-09-consolidation.md`. Pořadí čtení: nejdřív tento dokument (§1 přehled → §2 per-draft checklist → §3 pořadí → §4 reprodukce/autorství), pak review report pro referee-grade verdikt a odhady času.

> **Aktualizace 2026-06-08 (kola 12–16 + agent-framework):** Tato revize byla doplněna o nálezy z kol 12–16 (F-024..F-035), které vznikly po nasazení tří výzkumných agentů na `main` (exploratory-engine + computational-physicist + adversarial-verifier, commit `6e0f394`). Audit-fixy kola 14–15 od verifiera jsou již aplikovány (commit `e79b75e`: M-1 proxy3 30-seed committed podklad, m-1 F-031 měřený vs predikovaný drift, m-2 F-033 reziduum). Klíčové dopady na drafty: **draft-01 §4.2** dostal spojitý superradiantní exponent $B(a)$ (F-030, nahrazuje starý ohraničený 4.23/3.82), **draft-04 §4.3** dostal poctivé negativy F-029 (2D ano / 4D ne) a F-031 (4D area-law genuinně chybí). Per-draft checklisty níže (§2) byly o tyto položky rozšířeny.
>
> **Aktualizace 2026-06-09 (kola 18–21, druhý/třetí oblouk + konsolidace):** Pokrytí rozšířeno z F-024..F-035 na **F-024..F-039**. Draft-06 (negative-results letter, řádek tabulky §1) stojí na čtyřech nálezech druhého/třetího oblouku, které musí lidský revizor ověřit proti `findings.json` (verbatim statusy): **F-036** (KMS/Unruh netautologický test, status `informovany-negativ-tautologie` — most struktury/boostové geometrie, NE teploty; absolutní Unruh $2\pi$ neobnovena, VYPOCET-32); **F-037** (konformní 4D dS area-zákon, status `supported` — $\xi=1/6$ neobnoví area-zákon, R' drift $\rho^{+0.386}$ identický pro $\xi=1/6$ i $\xi=0$; posiluje F-031, VYPOCET-33); **F-038** (molekulová fluktuace, status `refuted-direction` — Var$(N_{mol})\sim\rho^{0.656}$, CI95 vylučuje plochu i objem; druhý nezávislý negativ k F-031, VYPOCET-34); **F-039** (EE-koeficient vs trace-anomálie, status `confirmed`/no-match-geometric — $c_{EE}=7.562$ CV 1.26 %, $-18/11$ míjí o 362 %, VYPOCET-35 / SYNTEZA-03 zeď 3). Poznámka: **F-034** (`partial`, KMS/thermal-time na Rindlerově slabu, VYPOCET-30) je předchůdce **konsolidovaný do F-036** — v draftu-06 (Wall 2) je tato fyzika reprezentována přes F-036, takže absence F-034 v draftu je vědomé superseder, ne opomenutí. Kolo 21 navíc opravilo stale F-033 korelaci 0.098→0.319 (timing-truncace artefakt; verdikt no-match nezměněn) napříč registry + knowledge-base.
>
> **Aktualizace 2026-06-09 (kolo 22 + velké review):** Pokrytí rozšířeno na **F-001..F-041**. Dva nové nálezy kola 22 (compute-doporučení SYNTEZY-03 #1/#2): **F-040** (geometrický γ5-gradovaný boost Dirac, status `confirmed-mixed-sharper-negative` — pojmenovaný chybějící prvek F-036 byl postaven a well-posed na konečném causetu, VYŘEŠIL log-kompresní obstrukci, exponent +1 ne 0.72, koeficient O(2π); ALE absolutní Unruh 2π se neobnovuje ρ-invariantně, operátorová routa driftuje s N, CV 0.205 → obstrukce PŘESUNUTA na konečné-N diskretizaci; VYPOCET-36, geometric-boost-dirac); **F-041** (NCG↔spectral-dimension, status `confirmed` — z téhož Tr e^{−σD²} heat-trace plyne d_s=2 i Seeley-DeWittovy a_k, ale diskrétní a_4/a_0 NEreprodukuje −18/11 na plochém causetu; Wall-3 separace potvrzena z NCG strany; ncg-spectral-dimension). Draft-06 Wall 2/§7 + SYNTEZA-03 top-banner dostaly forward-note kola 22 (mezitím aplikováno). **Velké review** (`reports/2026-06-09-velke-review.md`) provedlo referee-grade audit všech 5 draftů + sady nálezů + dvojí verifikace; aplikovalo bezpečné auto-fixy (F-009 statement number-mismatch, kappa-atribuce 1712.04227→1611.10281 ve F-039/F-028/F-006, F-040 `route3_2pi_recovered` flag true→false, draft-01 §3.1/§4.2 clarity, draft-06 Wall 1/Wall 2 forward-notes); zbytek je v lidském punch-listu §2 níže + v review reportu s odhady času. **Nově nalezeno: 7 chybných autorských atribucí přežívajících v draftech** (ID existují, témata sedí, jména autorů jsou špatně — viz per-draft checklisty B níže a §6 review reportu); lidská verifikace arXiv ID proti arxiv.org je nejvyšší priorita.

---

## 1. Přehledová tabulka pěti draftů

| Draft | Stav | Vědecká uzavřenost | Hlavní nárok | Největší riziko | Odhad lidské revize |
|-------|------|-------------------|--------------|-----------------|---------------------|
| **draft-01** — SJ ve rotujících prostoročasech (v0.3) | Interní explorační draft; NENÍ připraven k odeslání. VYPOCET-14 + VYPOCET-15 zpevnily §4.2; VYPOCET-26 (F-030) **nahradil** starý ohraničený B spojitým B(a). | Otevřená: zbývá kontinuální studie (velké N), analytická křížová kontrola, srovnání se známými BTZ vakuy | SJ stav existuje a je numericky konstruovatelný uvnitř ergoregiónu; rotace žije v vlastních vektorech, ne ve spektru; superradiantní pásový otisk v pozitivním podprostoru SJ; **superradiantní exponent B je spojitá klesající funkce strhávání (6.10→2.54, dB/da=−2.20), NE konstanta D−1=3** (F-030) | Referee napadne: „Je to jen zkosený 2D Minkowského diamant" a „A_caus = +1 je triviální klasický výsledek" | 15–25 hodin (matematika §§2–3 + BTZ vakuum + citace) |
| **draft-02** — identita −18/11 (v0.1) | Interní explorační draft; fyzika výpočetně uzavřena (VYPOCET-11 + VYPOCET-17). | **Uzavřena:** žádný otevřený fyzikální blokátor; zbývají framing + lidská verifikace PDF | Exaktní racionální identita c/(−a) = −18/11 je obsahově nezávislá na fermiónové části; graviton identitu neobnoví; Λ-člen nemá sesterskou identitu | Referee napadne: „Tautologie — znovu jste odvozili, že a₄ = a₄"; pokud někdo toto číslo napsal dříve (Connes–Marcolli kniha, van Suijlekom) | 4–8 hodin (nejmenší draft, exaktní aritmetika) |
| **draft-03** — ds klasifikátor (v0.1) | Interní explorační draft; NENÍ připraven k odeslání. | Otevřená: novelty re-check nutný; per-řádkový REPRODUCE audit; D-konvence nejasná | d_s je klasifikátor (z, D, sonda), ne universální konstanta; zjevná universalita d_s → 2 je artefakt γ=2 podtřídy; „stejná teorie, opačný trend" (CST d'Alembertian vs. random walk) | Referee napadne: „Calcagni program přebalený"; D-konvence ambiguita v Hořavově řádku | 10–18 hodin (per-řádková verifikace 12 hodnot + novelty search) |
| **draft-04** — přechod typů na kauzálních množinách (v0.2) | Interní explorační draft; NENÍ připraven k odeslání. Round-10/11 přidal de Sitter §4.3 (F-023 `supported` 2D + F-025 `partial` 4D); kola 12–16 doplnila F-027/F-028/F-029/F-031/F-032. | Otevřená: proxy nejsou typy; ~~placeholder chyba `a_err=0.776`~~ (VYŘEŠENO 2026-06-06); větší N v 4D potřeba; **dS §4.3: 2D area-law potvrzen (F-029), ale 4D area-law GENUINNĚ CHYBÍ (F-031), konformně-váhový caveat NEVYŘEŠEN** | 3/3 proxy ukazuje III₁→II přechod ve 4D desce; selektivita (N^{3/4} funguje, fixed-fraction nefunguje); dS §4.3 přidává II₁ vs II_∞ obsahový diskriminátor; **Proxy 3 2/3→3/3 při ≥30 seedech (F-032)**; poctivé negativy: 4D žádné A/4 (F-031), 2D c≈7.57≠4 (F-028) | Referee napadne: „Konečná matice = vždy typ I; nic jste neměřili"; N^{3/4} je předpis; **4D skalár není konformně invariantní; 4D area-law chybí** | 16–26 hodin (re-run 6+ calc.py + statistika + verifikace ~17 arXiv ID; +4–6 h za de Sitter §4.3) |
| **draft-06** — limity diskrétního programu / „mapa negativů" (v0.1) | Interní explorační draft (2026-06-09); negative-results letter konsolidující F-031/037/038 (zeď 1), F-033/036 (zeď 2), F-039 (zeď 3) + SYNTEZA-03. Jen existující findings, žádné nové claimy. | Otevřená: **doplnit ověřená arXiv ID konvenčních ref** (CHM/Solodukhin/BW/Unruh — citovány bez ID, flagged v §References); rozhodnout venue (standalone letter vs. appendix k draft-04); nepřeprodat negativy jako no-go | Tři ostré, mechanismem-podložené negativy: 4D area-zákon genuinně chybí (dimenzní náhoda 2D), surogátní Dirac = struktura ne teplota/metrika, diskrétní koeficient je geometrický ne anomální; každý pojmenovává chybějící ingredienci | Referee napadne: „negativy konkrétní konstrukce, ne no-go"; nutná konzistence s draft-04 §4.3 (tatáž 4D-area-law absence) | 8–14 hodin (verifikace ~10 ref ID + čísla vs findings + venue rozhodnutí; nejmenší nová položka, syntéza hotových výsledků) |

---

## 2. Co přesně musí člověk ověřit v každém draftu

### 2.1 draft-01 — SJ ve rotujících prostoročasech

#### A) Matematické re-derivace (blokující)
- [ ] **Analytické SJ pro zkosený 2D diamant:** odvodit SJ spektrum/vlastní funkce analyticky pro konstantně-skloněnou sekci (je konformně ekvivalentní standardnímu kauzálnímu diamantu/obdélníku, pro nějž je SJ znám, srov. Mathur–Surya). Porovnat s numerickým spektrem z kódu.
- [ ] **Analytická předpověď nulového přechodu skloněné null-souřadnice na r_erg:** odvodit uzavřenou formu: s₋ = 0 ⟺ g_tt = 0 ⟺ r = r_erg, s přesným vztahem mezi vnitřním null-sklonem a (g_tt, g_tφ, g_φφ).
- [ ] **Uzavřená forma A_caus(r)** z úhlů otevření kužele (sklon je funkce metriky), potvrdit ~1/r² chvost a monotonní a-závislost nejsou statistické artefakty.
- [ ] **Mechanismus opačného znaménka (§3.5b):** ověřit, že toy-model derivace v null-souřadnicích u=φ−s₊t, v=φ−s₋t reprodukuje oba znaky a magnitudy (h∝du dv ověřeno symbolicky — potvrdit výpočtem).
- [ ] **⚠️ BLOCKER (velké review 2026-06-09) — nejsilnější referee útok (sheared diamond):** doplnit explicitní argument/výpočet, že při fixed-r je jediný gauge-invariant **cone-tilt**, + alespoň jednu **observable odlišující dragging od coordinate shear**. Bez toho hostilní referee přerámuje BTZ↔Kerr univerzalitu jako tautologii („oba jsou stejný zkosený 2D Minkowského diamant, kde je černá díra?"). Nejlepší existující obrana §3.5/§3.5b (rotace žije v eigenvektorech 44.6°, ne ve spektru) je solidní, ale draft ji NEpostaví explicitně proti tomuto útoku. Vlastní výpočet + srovnání s Mathur-Surya SJ a se ZNÁMÝM BTZ vakuem je HUMAN+compute. (Viz TODO §1.1.)

#### B) Kontrola citací proti PDF (blokující — Priorita 1 — musí provést člověk)
- [x] arXiv:1205.1296 (Afshordi–Aslanbeigi–Sorkin, „A distinguished vacuum state for a quantum field in a curved spacetime", JHEP 2012) — ID opraveno z chybného 1208.2422 (2026-06-06)
- [ ] arXiv:1611.10281 (Sorkin–Yazdi) — potvrdit eq. 9 a footnote 5 (G_R = ½C)
- [x] arXiv:2602.09796 — **OPRAVENO 2026-06-08:** ID existuje, ale je to **Häfner & Klein, „The Unruh state for bosonic Teukolsky fields on subextreme Kerr spacetimes" (2026-02-10)**, NE „Dafermos–Luk et al.". Atribuce opravena v draft-01 §1.1, §4.2, ref.13. Obsah tvrzení (Unruhův stav existuje a je Hadamardův pro Teukolsky pole na subextremálním Kerru) je podporován; chybné bylo pouze autorství. Nezaměňovat s Dafermos–Rodnianski 2007.07211 (correctly cited).
- [ ] **arXiv:2303.13488 (Balakumar) — ⚠️ OPRAVA (velké review 2026-06-09):** titul v draftu „...on Kerr" je zkomolen; skutečný titul „Superradiance and quantum states on black hole space-times", autoři **Balakumar, Bernar, Winstanley**. Vedoucí autor sedí; opravit titul + doplnit spoluautory.
- [ ] **arXiv:2504.12919 (AdS₂ SJ) — ⚠️ OPRAVA:** draft cituje bez autorů; skutečný titul „Numerical Evaluation of the Causal Set Propagator in 2D Anti-de Sitter Spacetime", autoři **Kastrati & Hinrichsen**. ID a téma správné; doplnit autory + přesný titul.
- [ ] **arXiv:2212.10592 — ⚠️ OPRAVA:** draft připisuje „Jubb-Surya, Softened SJ"; skutečnost = **Zhu & Yazdi**, „On the (Non)Hadamard Property of the SJ State in a 1+1D Causal Diamond" (CQG 2024). Téma (softened SJ / Hadamard recovery v 1+1D diamantu) sedí, AUTORSTVÍ špatně. Ověřit, zda Jubb-Surya nemají SAMOSTATNÝ softened-SJ paper (jiné ID); jinak přeřadit všechna „softened SJ" tvrzení na Zhu-Yazdi.
- [ ] **arXiv:2007.07211 — ⚠️ OPRAVA:** draft připisuje „Dafermos-Rodnianski, Boundedness of the Teukolsky equation on Kerr"; skutečnost = **Shlapentokh-Rothman & Teixeira da Costa**, „Boundedness and decay for the Teukolsky equation on Kerr in the full subextremal range |a|<M". ID ukazuje na reálný Teukolsky-boundedness-on-Kerr paper jiných autorů. Pokud byl míněn klasický Dafermos-Holzegel-Rodnianski výsledek, dohledat správné ID.
- [ ] BTZ/Kerr metrické reference (gr-qc/0003097, 1707.08133) — potvrdit
- [ ] arXiv:0909.0944, 1701.07212, 1712.04227 — potvrdit (pozn.: 1712.04227 = Belenchia-Benincasa-Letizia-Liberati, „On the Entanglement Entropy of Quantum Fields in Causal Sets" — ověřit, že draft-01 ho cituje jen pro G_R=½C konvence, ne pro autorství výsledku)

#### C) Číselné výsledky vs. results.json (blokující)
- [ ] Zkontrolovat, že headline čísla v draftu (A_caus ≈ +1 uvnitř ergoregiónu; středová osa 44.6° rotace vlastního vektoru; cos² = 0.507; spektrální shoda 2.0%; superradiantní pásová váha 0.000 → 0.0755) odpovídají výsledkům uloženým v `core-data/calculations/sj-rotating-btz/`, `sj-kerr-equatorial/`, `sj-eigenvector-superradiance/`
- [ ] Potvrdit VYPOCET-14: ΔAIC = +442 (a=0.6), +4216 (a=0.9), +232 (BTZ) — zkontrolovat v `core-data/calculations/sj-threshold-scan/` (decisive ve prospěch Model S = W_sr ~ Ω(r)^B; F-017)
- [ ] Potvrdit VYPOCET-15: ΔAIC(E−S) = +3894 pro joint fit; |A_W| ~ r^{−2.75±0.03} — zkontrolovat v `core-data/calculations/sj-far-zone/` (F-018)
- [ ] **NOVÉ (F-030, VYPOCET-26 — §4.2 draft přepsán 2026-06-08):** Potvrdit, že po odstranění artefaktu meze A=100 z VYPOCET-14 je spolehlivý Kerr exponent **B(a) SPOJITÁ klesající funkce**, NE konstanta D−1=3. Ověřit v `core-data/calculations/sj-kerr-b-scan/`: B = 6.10(a=0.3), 3.32(a=0.6), 2.67(a=0.9), 2.54(a=0.99), všechny R²≥0.988; slope **dB/da = −2.20±0.07 (z=−33.6)**; konstantní B=3 **rozhodně zamítnut** (χ²_const = 2473/7 vs χ²_lin = 111/6; křivka protíná 3 jen při a≈0.75). BTZ **pod** Kerr křivkou (B=2.22 při J=0.6, 2.12 při J=0.9) → role asymptotiky bez Kerr-AdS. Starý ohraničený B (4.23/3.82) byl artefakt meze A≤100 a je v draftu nahrazen. Framing draftu: „trend dB/da<0 + BTZ pozice", NE jediné B. Caveat zachovat: 2D bezhmotný fixed-r řez (ne 4D Teukolsky).
- [ ] Ověřit, že párovací residuum i∆ je skutečně machine-precision (~10⁻¹⁶)

#### D) Vědecké konvence
- [ ] Potvrdit, že §4.3 explicitně uvádí omezení na masový případ (masivní pole není pokryto)
- [ ] Zkontrolovat, že jazyk „f_co = 1 je podpis superradiance" byl degradován na „konzistentní s" (v0.2)
- [ ] Potvrdit, že prohlášení o autorství/AI-asistenci je přítomno (§0)

---

### 2.2 draft-02 — identita −18/11 (vědecky uzavřená)

#### A) Matematické re-derivace (blokující — ale krátké)
- [ ] **Odvodit (a, c) pro jeden Weylův fermion z a₄ masteru (Vassilevich eq. 4.28) ručně:** přistát na 11/720, 1/40; ověřit, že báze-změna na C²/Euler je správná
- [ ] **Re-derivovat −18/11 třemi způsoby a ověřit shodu:** (i) CC α₀/τ₀; (ii) single-Weyl c/(−a); (iii) Dirac 2×Weyl c/(−a)
- [ ] **Ověřit VYPOCET-11 výsledek (graviton):** fyzický Einstein graviton je non-konformní → žádné dobře-definované (a,c) → neobnoví identitu; konformní graviton (4-derivátová konformní gravitace) dává c/(−a) = −398/261 ≈ −1.525 ≠ −18/11 — potvrdit tato čísla ručně nebo přes sympy
- [ ] **Ověřit VYPOCET-17 výsledek (Λ-člen):** a₀:a₂ poměr nese (f₄/f₂)Λ² — rozměrový a cutoff-tvarový závislý → žádná sesterská identita pro Λ; čísla pro n_B = 28, n_F = 90/96 zkontrolovat
- [ ] **Nezávislá CAS validace připravena — spustit po instalaci Wolfram Engine:** druhá, na sympy nezávislá dráha ve Wolfram Language (`verification/cas/`) znovu odvozuje −18/11, konformní-graviton −398/261, STr(1) = −62/−68 a Λ-ledger strukturu přímo z publikovaných koeficientů. Spustit `brew install --cask wolfram-engine`, jednorázově interaktivně `! wolframscript -activate` (vyžaduje Wolfram ID), pak `python3 verification/cas/run_all.py`; očekává se `overall_pass = True`. Viz `verification/cas/README.md`. (Symbolický ekvivalent cross-HW reprodukce.)

#### B) Kontrola citací proti PDF (blokující — musí provést člověk)
- [ ] arXiv:2003.02688 (Duff) — otevřít PDF, potvrdit eq. 14 (konvence g^μν⟨T_μν⟩), eq. 17, Table 1: reálný skalár (1/360, 1/120), Weyl (11/720, 1/40), vektor (31/180, 1/10)
- [ ] hep-th/0306138 (Vassilevich) — otevřít PDF, potvrdit eq. 4.28 (a₄ master), a_H tabulku
- [ ] hep-th/9606001 (Chamseddine–Connes 9606) — otevřít PDF, potvrdit eq. 2.24: α₀ = −3f₀/10π², τ₀ = 11f₀/60π²
- [ ] hep-th/0610241 (CCM) — potvrdit přepis α₀, τ₀
- [ ] arXiv:1001.2036 (Andrianov–Lizzi) — citovat nejbližší pasáže a ukázat, že se zastaví před poměrovou rovností
- [ ] **arXiv:1106.3263 — ⚠️ OPRAVA (velké review 2026-06-09):** draft cituje 3–4× jako „Kurkov–Lizzi–Vassilevich"; skuteční autoři = **Andrianov–Kurkov–Lizzi** (Vassilevich NENÍ autor; Andrianov chybí). ID i titul „Spectral action, Weyl anomaly and the Higgs-Dilaton potential" SPRÁVNÉ. Přepsat všechny výskyty (abstract ř.11, §3 ř.110, §4 bod 3 ř.122, Sources ř.139) + zkontrolovat propagaci do VYPOCET-02 a references.bib/json. **Pro draft, jehož novost stojí na „completing the triangle" přesně z těchto prací, je atribuce load-bearing.**
- [ ] **arXiv:hep-th/9503187 — ⚠️ OPRAVA + obsahová tenze:** draft §4 implicitně přiřazuje Duffovi, TODO ř.77 Anselmimu; skutečnost = **Cho & Kantowski**, „Gauge Independent Trace Anomaly for Gravitons" (1995). Navíc titul „gauge INDEPENDENT" je v TENZI s tvrzením draftu, že gravitonové (a,c) jsou gauge/scheme-dependentní. Ověřit, kterou práci draft skutečně chce (kandidáti **Anselmi hep-th/9709047**, **Duff hep-th/9308075**); opravit atribuci i ID, nebo doplnit přesný výklad Cho-Kantowski.

#### C) Novelty re-check (blokující)
- [ ] **Prohledat Connes–Marcolli knihu** (*Noncommutative Geometry, Quantum Fields and Motives*) na explicitní zmínku o −18/11 nebo c/(−a) v CC normalizaci
- [ ] **Prohledat van Suijlekom** (*Noncommutative Geometry and Particle Physics*) totéž
- [ ] **Prohledat jakýkoli Vassilevich/Fursaev review** dávající a₄ v C²/Euler bázi vedle (a,c)
- [ ] Pokud je nalezeno: downgrade na „zpřesnění", ne „objev"

#### D) Schémová nezávislost — fyzikální bod
- [ ] Explicitně adresovat, zda C²/Euler poměr závisí na regularizačním schématu; argumentovat (nebo ohraničit), že C² a Euler jsou schémově nezávislé kombinace (□R ambiguita sedí ve zvláštní totálně-derivátové invariantě) — toto je reálný fyzikální bod, ne jen účetnictví

---

### 2.3 draft-03 — d_s klasifikátor

#### A) Matematické re-derivace (blokující)
- [ ] **Re-run engine:** spustit `calc.py` v `core-data/calculations/ds-classification/` a nezávisle potvrdit 12/12 validačních kontrol a symbolický výsledek D/γ
- [ ] **Re-derivovat oba limity ručně:**
  - izotropní d_s^UV = D/γ z ∫d^D k e^{−σk^{2γ}}
  - anizotropní d_s = 1 + D_space/z z faktorizovaného P(σ)
- [ ] **Ověřit D-konvenci:** v Hořavově řádku je D spacetime dimenze nebo prostorová dimenze? Potvrdit per-řádkovou konzistenci v celé tabulce

#### B) Kontrola citací proti PDF (blokující)
- [ ] arXiv:0902.3657 (Hořava) — potvrdit d_s = 1 + D/z a specifické hodnoty z=2 → 5/2, z=3 → 2 pro D=4
- [ ] arXiv:1507.00330 (Belenchia et al.) — potvrdit „universální d_s → 2 ve všech D" a (k²)^{D/2} high-momentum chování
- [ ] arXiv:1311.2530 (Eichhorn–Mizera) — potvrdit, že d_s *roste nad* D; potvrdit, že numerická hodnota 8 je ILUSTRATIVNÍ, ne z papíru
- [ ] arXiv:1311.3340 (Calcagni–Oriti–Thürigen) — potvrdit per-method výpočty; najít nejbližší větu k „probe-dependence" a ukázat, že zastaví před elevací probe na klasifikační osu
- [ ] arXiv:1304.2709 (Calcagni) — potvrdit, která třída multifraktálních teorií je použita
- [ ] arXiv:1708.07445 (Mielczarek–Trześniewski „mapa QG") — potvrdit, že srovnává přístupy bez unifikovaného enginu
- [ ] arXiv:hep-th/0508202 (Lauscher–Reuter), arXiv:1110.5224 (Reuter–Saueressig) — potvrdit η_* = 2 − d = −2 pro NGFP
- [ ] arXiv:1408.0199 (Stelle) — potvrdit d_s^UV = 2 pro libovolné D z k⁴ propagátoru
- [ ] arXiv:1105.6098 (Sotiriou–Visser–Weinfurtner) — potvrdit
- [ ] arXiv:1705.05417 (Carlip) — potvrdit „almost universal"

#### C) Novelty re-check (blokující)
- [ ] Prohledat Calcagni review/knihy a follow-upy 1708.07445 (Mielczarek–Trześniewski) na explicitní zmínku (z, D, probe) jako trojice klasifikátoru
- [ ] Prohledat Mielczarek–Trześniewski na „probe jako klasifikační osa"
- [ ] Potvrdit, že 1311.2530 a 1507.00330 jsou skutečně stejný podkladový CST framework (Benincasa–Dowker/sprinkling-based)

#### D) Čísla vs. results.json
- [ ] Potvrdit, že hodnota 8 (CST random walk) je v tabulce označena jako REPRODUCE (qualitative), nikoliv kvantitativní
- [ ] Zkontrolovat všechna čísla v tabulce against `core-data/calculations/ds-classification/results.json`

---

### 2.4 draft-04 — přechod typů na kauzálních množinách

#### A) Matematické re-derivace a re-run (blokující)
- [ ] **Re-run všechny čtyři calc.py** a reprodukovat headline čísla:
  - 2D diamant: trace 80× collapse; S ~ N^{1.04} → N^{0.17}
  - 2D diamant: pile-up N^{1.14} → přesně 0
  - 4D deska: trace 36× collapse; S ~ N^{1.34} → N^{0.55}
  - 4D deska: pile-up N^{1.27} → 0, IR edge ε ≈ 2.7
  - fixed-fraction control: S ~ N^{0.83} (nenastane area law)
- [x] **Opravit placeholder chybu `a_err = 0.775853...`:** ~~nahradit každou nejistotu exponentu (i) regresní standardní chybou a (ii) across-seed bootstrap CI~~ **VYŘEŠENO 2026-06-06:** `core-data/calculations/sj-vn-type/calc_uncertainty.py` (stejné seedy/parametry jako `calc.py`, centrální hodnoty reprodukovány do všech číslic) dopočítal pro 5 zasažených exponentů regresní SE + 68% across-seed bootstrap CI (2000 resamplů); zapsáno do `results.json` (`*_se_regression`/`*_ci68_bootstrap`) a draft-04. Klíčové: S_full a=1.04 ±0.013, S_trunc a=0.17 ±0.012, pile-up_trunc identicky 0 (SE 0), CV oba SE 0.08–0.11 (CI široké → proxy 3 zůstává nediskriminující). 2D verdikt 2/3 beze změny. (4D + companion calc: fit-error audit zatím otevřený.)
- [ ] **Ověřit ε = ln[μ/(μ−1)] derivaci:** potvrdit jednomódovou bosónovou derivaci z 0905.2562 a mapování (μ, 1−μ) páru na ν = μ − ½ s μ > 1 větví
- [ ] **Potvrdit G_R konvence:** 2D G_R = ½C (1611.10281 eq. 9); 4D G_R = (√ρ/2π√6)L, link matice (0909.0944 eq. 17, m=0) — potvrdit link-matrix vs. causal-matrix rozlišení správně aplikováno v 4D
- [ ] **Ověřit double truncation κ = √N/(4π) (2D local)** z 1712.04227 — potvrdit 4π a *double* aplikaci; potvrdit, že single global rank truncation dává negativní S
- [ ] **Ověřit area-law rank n_max = αN^{(d−1)/d}, α=2, d=4 → N^{3/4}** z 2008.07697 — potvrdit α a exponent; potvrdit, že kontinuální směr (zvyšovat ρ při fixním regionu, NE zvětšovat box při fixním ρ) odpovídá de Sitter-horizon proceduře v 2008.07697
- [ ] **Ověřit ±-párovací residuum:** 4D 7.1×10⁻¹⁴ / 2D ~10⁻¹⁶ — re-run a potvrdit

#### B) Kontrola citací proti PDF (blokující — 15 arXiv ID)
- [ ] arXiv:1611.10281 (Sorkin–Yazdi) — potvrdit eqs. 6–7, 9
- [ ] **arXiv:1712.04227 — ⚠️ OPRAVA (velké review 2026-06-09):** draft připisuje „Saravani, Aslanbeigi, Sorkin" / „Sorkin–Yazdi (Saravani–Aslanbeigi)"; skutečnost = **Belenchia, Benincasa, Letizia, Liberati**, „On the Entanglement Entropy of Quantum Fields in Causal Sets". Pokud je míněn κ=√N/(4π) double truncation výsledek, citovat **1311.7146 (Saravani–Sorkin–Yazdi)**. Odstranit „Aslanbeigi". Sjednotit ř. 18/90/250. (Stejná chyba ve draft-06 — opravit oba.)
- [ ] **arXiv:2212.10592 — ⚠️ OPRAVA:** draft připisuje „Yazdi–Mathur–Surya"; skutečnost = **Zhu, Yazdi**, „On the (Non)Hadamard Property of the SJ State in a 1+1D Causal Diamond". Mathur/Surya pravděpodobně kontaminace z 1906.07952. Potvrdit lokalizaci u−v'=±2L (paper je o non-Hadamard na hranici diamantu — sedí).
- [ ] arXiv:2008.07697 (Surya–Nomaan X–Yazdi, area-law rank) — potvrdit N^{3/4}, α=2, a směr kontinuálního limitu
- [ ] arXiv:0909.0944 (Johnston) — potvrdit eq. 17, m=0, link matice
- [ ] arXiv:1701.07212 — potvrdit konvence
- [ ] arXiv:0905.2562 (Casini–Huerta) — potvrdit bosónovou modulární derivaci
- [ ] arXiv:2206.10780 (CLPW) — potvrdit typ III₁→II via observer
- [ ] arXiv:2209.10454 (CPW) — potvrdit II_∞
- [ ] arXiv:2112.12828 (Witten) — potvrdit
- [ ] arXiv:2501.09669 — **KRITICKÉ: nový (2025), potvrdit existenci a obsah**
- [ ] arXiv:2602.16782 (Jones–Yazdi) — **KRITICKÉ: nový (2026), potvrdit existenci a podporu ε = ln[μ/(μ−1)] identifikace** (draft tvrdí verbatim z provenience poznámky, neověřeno)
- [ ] arXiv:1906.07952, 2412.07832 — potvrdit
- [ ] arXiv:2601.07915, 2306.07323 — potvrdit pro novelty overlap s type-II-on-causal-set framingem
- [ ] Connes 1973 — potvrdit klasifikaci typů von Neumannových algeber

#### C) Statistika (blokující)
- [ ] 2D Proxy 3 je nediskrimiující (N^{−0.71±0.78} konzistentní s nulou): verdikt 2D je **2/3**, nikoli 3/3 — potvrdit, že summary toto nezmaten
- [ ] 4D použilo 5 seeds, 2D 8 seeds: reportovat pro IR-edge ε ≈ 2.7 a pile-up exponent N^{1.27} across-seed spread
- [ ] **⚠️ §4.4 number-mismatch (velké review 2026-06-09, Major):** §4.4 uvádí „4D slab → AREA law: S∼L^{2.00}, S∼A^{1.00}". To jsou CÍLOVÉ referenční exponenty (`area_law_slope:2.0`), NE naměřené. `ssee-slab-4d/results.json` dává `fit_S_vs_L.slope=1.590` a `fit_S_vs_area_pow.p=0.795`. Přepsat na: „S∼L^{1.59} (R²=0.982), klasifikováno jako AREA dle R²_area>R²_vol (0.984 vs 0.977, **těsná marže**), proti referenčnímu area-law sklonu 2.0". **Opravit i F-016 statement v findings.json** (mění finding — proto NEbylo aplikováno auto). Neuvádět cílový exponent jako naměřený.
- [ ] **IR edge ε≈2.7 / 39σ exclusion neauditovatelné z results.json:** hodnota „sharp IR modular edge ε≈2.7" (4D slab) a „excluding ρ^{−1/4} at ~39σ" nejsou v results.json přímo uloženy (jen `eps0_threshold=0.5`, `p_minus_half_sigma=2.82`). Hrubé odhady jsou konzistentní; při příštím re-run uložit `IR_edge_eps_number` a `sigma_vs_quarter`, nebo v textu označit jako odvozené ze spektra.

#### D) De Sitter sekce §4.3 (round-10/11 provenance — F-023 `supported` 2D, F-025 `partial` 4D)

Tato sekce byla přidána v rohu 10/11 (rozhodnutí H5g-6: **sekce v draft-04, NE samostatný draft-05**, dokud není demonstrována plná 4D saturace při větším N). Statusy musí zůstat **verbatim** dle `findings.json` (F-023 `supported`, F-025 `partial`) — **nikdy neupgradovat**. Plný checklist je v `papers/draft-04-type-transition-causal-sets/TODO.md §7b`; blokující položky:

- [ ] **Re-derivovat saturační fity z `results.json`** (`sj-desitter-type` 2D: N_total cap=480.11 R²≈1.0000, S_full sat-fit R²=0.990 late-slope −1.67, plochá kontrola roste; baterie 2/3 — Proxy 1 a=1.105→0.116, Proxy 2 pile-up 1.248→0, Proxy 3 nesignifikantní při 5 seedech; Part-3 tracialní **honest null**)
- [ ] **Re-derivovat 4D fity z `results.json`** (`sj-desitter-4d`: R*-exponent dS 0.27 vs plochá 0.52, poměr sklonů 2.96; fixní-region S_trunc~N^{0.717±0.029} CI68 [0.697,0.739] R²=0.993 — **nad cílem 0.5**, dS radiální geometrie strmí; kontrolní reprodukce a=0.58 vs commit 0.547; N_total cap=480 R²=1.000; pile-up full 6→32 vs trunc=0). Potvrdit, že plná saturace **NENÍ** dosažena při N≤2500 (F-025 `partial`)
- [ ] **Ověřit konformně-váhový caveat:** draft musí poctivě uvádět, že 4D bezhmotný skalár **není konformně invariantní** (zachována kauzální struktura + míra sech², ne přesný propagátor); 2D konformní trik (1306.3231) je exaktní, 4D lift je řízená aproximace
- [ ] **Zkontrolovat shodu statusů F-023/F-025 s `findings.json`** (F-023 = `supported`, F-025 = `partial`); §4.3 a abstrakt **netvrdí** II₁ jako naměřené, **netvrdí** čistou 4D saturaci, **netvrdí** A/4 strop
- [ ] **Re-run obou dS `calc.py`** (`sj-desitter-type/calc.py`, `sj-desitter-4d/calc.py`) — reprodukovat headline čísla + ±-párování (2D 2.3×10⁻¹³, 4D <6.84×10⁻¹⁵)
- [ ] **Ověřit 2 nové arXiv ID:** 1306.3231 (dS SJ vakuum / konformní trik) a 1205.3855 (Anninos, dS₂ statická záplata, želví + sech² konvence) — existence, autoři/rok, obsah
- [ ] ~~**H5g-2 (A/4 strop) je citován jako OTEVŘENÝ, ne testovaný**~~ **AKTUALIZOVÁNO 2026-06-08 (F-028/F-031):** H5g-2 je nyní *částečně* testován. §4.3 outlook v draftu byl přepsán: ve **2D** je slabá H5g-2 (existuje konstantní A/4-*podobný* zákon) **podpořena** (R=0.132±1.3 %, S_cap~A_horizon, ε~ρ^{−1/2} fixováno nezávisle z F-006 = anti-cirkularita), ale silná H5g-2 (konstanta = 1/4) **zabita** (c=1/R≈7.57≠4). Ve **4D žádný A/4 nárok** (F-031: korigovaná kodim-2 molekula ~ρ^0.5 vs obsahová entropie ~ρ^1.0 → poměr driftuje). Ověřit, že draft toto rozlišuje a netvrdí literální 1/4 ani ve 2D, ani A/4 ve 4D.

#### E) Kola 12–16 (přidáno 2026-06-08) — nálezy F-027..F-032 v §4.3/§4.1/§4.4

Tyto nálezy vznikly po round-10/11 a byly do draftu propsány 2026-06-08. Statusy ověřit **verbatim** proti `findings.json`; **nikdy neupgradovat**.

- [ ] **F-029 (`partial`, VYPOCET-25) — §4.3:** Potvrdit v `core-data/calculations/ds-entropy-cap/` (2D, scaled): R_full = S_full_cap/A_mol = **0.130±0.0039 (CV 3.0 %)**, drift d ln R/d ln ρ = +0.007 (≈0), reprodukuje F-028 committed 0.1321 cross-HW, rozšířeno přes 5× hustotu + 3.6× velikost záplaty → 2D kvantitativní area-law potvrzen a rozšířen. **4D je kvalitativně jiné** (c^{4D} roste 5.6→65.8 s ρ) → žádná čistá 4D area-law konstanta.
- [ ] **F-031 (`supported`, VYPOCET-27) — §4.3 (BLOCKER opraven):** Potvrdit v `core-data/calculations/ds-amol-convention/`, že 4D „plocha" A_mol~ρ^1.77 byla **kodim-1 artefakt** (světočára-tubus {r*=R_cut} v (t,r*,x1,x2), NE kodim-2 2-plocha {r*=R_cut, t=0}). Korektní kodim-2: p_S=1.055±0.028, p_A=1.768±0.029, **měřený** drift p_S−p_A=−0.71 (predikce −0.55). Verdikt: ve ploché-kauzální + dS-sech² konstrukci 4D area-law S~A_proper **genuinně NEEXISTUJE**. Caveat (a) konformně-váhový NEVYŘEŠEN: drift S_full~ρ^1 vs plocha~ρ^0.5 může být částečně tato aproximace → verdikt platí pro tuto konstrukci, ne nutně přesný dS stav.
- [ ] **F-028 (`supported`, VYPOCET-23) — §4.3 outlook:** Potvrdit v `core-data/calculations/ds-entropy-cap/` slabá H5g-2 **supported** (R=0.1321±1.3 %, S_cap~A_horizon, ε z F-006), silná H5g-2 **killed** (c≈7.57≠4). Draft už nahradil staré „untested, and not claimed".
- [ ] **F-027 (`supported`, VYPOCET-24) — §4.3 tracialní null:** Potvrdit v `core-data/calculations/ds-tracial-probe/`, že tracialní II₁ probe je **null UZAVŘEN** i při 6× hustotě (ρ∈{1000,3000}): gap dS−flat = −0.998±0.495 (negativní). II₁ identifikace bounded dS stojí na **content-saturaci**, ne na tracialním signálu (κ-truncace odstraňuje low-ε módy).
- [ ] **F-032 (`supported`, VYPOCET-28) — §4.1/§7 Proxy 3:** Potvrdit v `core-data/calculations/vn-type-proxy3-seeds/`, že Proxy 3 verdikt **2/3 → 3/3** při ≥30 seedech na **původním** VYPOCET-12 gridu: 8 seedů slope −0.280±0.190 (t=1.48, null), 30 seedů −0.198±0.092 (t=2.15, sig), 50 seedů −0.224±0.069 (t=3.25, sig, CI68 [−0.30,−0.15] vylučuje 0). **NOSNÁ VÝHRADA:** upgrade je seed-count efekt (genuine), NE gridový artefakt; nový 5-bodový grid nafukuje low-seed t-stat (8 seedů t=5.37) a nesmí se číst jako 8-seedové srovnání VYP-12. (Committed podklad: commit `e79b75e`, M-1.)
- [ ] **F-019/F-016 (`supported`/`confirmed`) — §4.2/§4.4:** F-IDy doplněny v próze (N^{3/4} selektivita §4.2; slab S~L^2.00 vs diamant S~f^6.1, Hadamard anomálie na rozích §4.4). Statusy ověřit.
- [ ] **F-024/F-026 (`partial`/`refuted`) — §4.4 scope caveat:** Ověřit, že draft netvrdí čistý 4D corner mechanismus: 4D modular-flow PARTIAL 3/5 (slab off-diag −1.10 vs diamant −0.52) [F-024]; kodim-2 wedge REFUTED (nl-vs-edge slope +0.115, opačně k 2D corner) [F-026]. 2D corner non-Hadamard koncentrace se do 4D **NEpřenáší cleanly**.

---

### 2.5 draft-06 — limity diskrétního programu / „mapa negativů" (negative-results letter)

Draft-06 je negativní letter konsolidující tři „zdi" druhého/třetího oblouku. NEnese žádné nové claimy — jen existující findingy. Po velkém review (2026-06-09) má Wall 2/§7 + abstrakt + Wall 1 už doplněné forward-notes a clarity (AUTO). Zbylé lidské brány (plný checklist v `papers/draft-06-discrete-program-limits/TODO.md`):

#### A) Číselné výsledky vs. findings.json + results.json (blokující)
- [ ] **Wall 1 (F-031/F-037/F-038) — 4D area-zákon GENUINNĚ CHYBÍ:** ověřit, že draft uvádí (a) opravený codim-2 molekulový počet ρ^{0.49} vs S_full ρ^{0.997} → poměr driftuje ρ^{+0.50} (F-031, `ds-amol-convention`); (b) konformní caveat VYŘEŠEN — ξ=1/6 dává identický drift jako ξ=0, d ln R'/d ln ρ=+0.386±0.053 (F-037, `ds-conformal-4d`); (c) variance Var(N_mol)~ρ^{0.656}, CI95 [0.575,0.745] vylučuje plochu i objem, super-Poisson Fano 3.7→5.3 (F-038, `ds-molecule-fluctuation`).
- [ ] **Wall 2 (F-033/F-036/F-040) — surogátní Dirac = struktura, ne teplota/metrika:** ověřit boostová diagonála R²≈0.97 ρ-invariantní (F-036, `ncg-kms-unruh`); Connesova vzdálenost nesleduje kauzální (korelace 0.32, R²=0.10, 16 párů; F-033, `spectral-triple-modular`); absolutní Unruh 2π neobnoven (off 52 %). **Forward-note kola 22 (F-040, `geometric-boost-dirac`) je v draftu doplněn** — ověřit, že čte správně: geometrický γ5-gradovaný boost Dirac VYŘEŠIL log-kompresi (exponent +1, koeficient O(2π)), ale absolutní 2π drift s N (CV 0.205) → obstrukce přesunuta na konečné-N.
- [ ] **Wall 3 (F-039) — koeficient geometrický, ne anomální:** ověřit c_EE=7.562±1.3 % nesedí na žádný anomální racionál (skalár −3 míjí 152 %, −18/11 míjí 362 %), nejbližší geometrické kontroly 8 (5.5 %) a 4 (10 %; F-039, `amol-anomaly-ee-coeff`). **Pozn.: kappa-atribuce κ=√N/(4π) v F-039 byla velkým review opravena 1712.04227→1611.10281** (Sorkin-Yazdi) — ověřit, že draft cituje κ-zdroj správně.

#### B) Kontrola citací proti PDF (blokující)
- [ ] **arXiv:1712.04227 — ⚠️ OPRAVA (velké review 2026-06-09, Major):** draft cituje „Sorkin–Yazdi ... double truncation, 1712.04227"; skutečnost = **Belenchia–Benincasa–Letizia–Liberati**, „On the Entanglement Entropy of Quantum Fields in Causal Sets". Přesměrovat „double truncation"/„κ=√N/(4π)" na **1611.10281** (a/nebo 2008.07697). F-036 už interně tuto záměnu vlajkuje; AUTO-fix opravil findings.json kappa-atribuci, ale **draft text zůstává na člověku**. (Stejná chyba ve draft-04 — opravit oba.)
- [ ] **Konvenční ref bez ID** (CHM/Solodukhin/BW/Unruh/Gibbons-Hawking, §References) — doplnit OVĚŘENÁ arXiv ID; flagged v draftu jako „to be cited with verified IDs by a human". Gibbons-Hawking dS primár je ⚠️ neoveřeno (není v repu) — dS aplikace reportována jako bezrozměrný poměr, ne literální 1/4.

#### C) Konzistence a venue (blokující/redakční)
- [ ] **Konzistence s draft-04 §4.3** (tatáž 4D area-law absence): ověřit, že Wall 1 rozlišuje dS-cap area-zákon (CHYBÍ, F-031) od truncated-SSEE **slab** area-zákona neseného type-II rankem ~√N (PŘÍTOMEN, F-019) — **rozlišení už AUTO-doplněno**, ověřit, že čtenář nečte „4D entropy-area law genuinely absent" jako popření i slab area-zákona.
- [ ] **Nepřeprodat negativy jako no-go:** ověřit §6 „these are negatives of a specific finite-N construction, not no-go theorems".
- [ ] **Venue rozhodnutí:** standalone letter vs. appendix k draft-04 (redakční, na člověku).

---

## 3. Doporučené pořadí revizí s odůvodněním

### Doporučení: draft-02 → draft-06 → draft-04 → draft-01 → draft-03

(Pořadí dle ROI/uzavřenosti; identické s velkým review reportem `reports/2026-06-09-velke-review.md §1`. **Nejlevnější univerzální brána napříč všemi: lidská verifikace arXiv ID proti arxiv.org** — velké review našlo 7 chybných autorských atribucí, viz §6 review reportu.)

**1. Začněte s draft-02 (identita −18/11)**

*Proč první:* Nejmenší draft. Fyzika je výpočetně uzavřena (VYPOCET-11 + VYPOCET-17 — žádný otevřený fyzikální blokátor). Klíčová aritmetika je exaktní (sympy, racionální čísla, navíc CAS-nezávisle re-odvozená) — re-derivace jsou krátké a buď vyjdou nebo nevyjdou. Zbývající bloky: framing („theorem"→„exact identity"), 2 ref-atribuce (1106.3263, hep-th/9503187), novelty-gap (Connes-Marcolli / van Suijlekom). Odhad: 4–8 hodin. Navíc: pokud novelty re-check odhalí, že −18/11 bylo dříve publikováno, ušetříte práci na zbytku.

**2. Pokračujte s draft-06 (mapa negativů)**

*Proč druhý:* Syntéza HOTOVÝCH výsledků (žádné nové claimy, jen existující findingy F-031/033/036/037/038/039 + kolo-22 F-040/F-041). Po velkém review má forward-notes a clarity už doplněné (AUTO). Zbývá: 1 ref-atribuce (1712.04227, sdílená s draft-04), verifikace ~10 konvenčních ref ID, venue rozhodnutí. Nejmenší nová položka. Odhad: 8–14 hodin. Navíc: konzistence s draft-04 §4.3 (tatáž 4D area-law absence) je už ověřena.

**3. Třetí draft-04 (přechod typů)**

*Proč třetí:* Fyzika je zajímavá a konzistentní (3/3 proxy ve 4D + dS §4.3), ale blokátory jsou konkrétní a mechanické — re-run 4+ calc.py, verifikovat ~17 arXiv ID (2 už nalezeny chybné: 1712.04227, 2212.10592), opravit §4.4 number-mismatch (S∼L^{1.59} ne 2.00) + párový F-016. Technický audit, ne otevřený vědecký spor. 7/8 lidských bran TODO §8 nesplněno. Odhad: 16–26 hodin.

**4. Čtvrtý draft-01 (SJ v rotujících prostoročasech)**

*Proč čtvrtý:* Nejrozsáhlejší a vědecky nejotevřenější (chybí kontinuální studie, BTZ vakuum srovnání, analytická křížová kontrola; sheared-diamond útok není plně pre-emptován). Velký N scan a 30+ seeds jsou strojový čas, ale analytické odvození SJ na zkoseném diamantu + observable odlišující dragging od shear vyžaduje skutečnou práci. Výsledky VYPOCET-14/15 jsou silné (ΔAIC > 3894 všude), jádro stojí. 3 ref-atribuce nalezeny chybné (2212.10592, 2007.07211, 2303.13488). Odhad: 15–25 hodin.

**5. Nakonec draft-03 (d_s klasifikátor)**

*Proč poslední:* Novelty argument je nejkřehčí — vyžaduje rozsáhlý literature search (Calcagni knihy, reviews, follow-upy k 1708.07445). Fyzika (engine, limity) je solidní, ilustrativní d_s=8 poctivě označen, D-konvence opravitelná (human PDF 0902.3657), ale obhájit „probe jako klasifikační osa" vůči Calcagni programu je nejnáročnější framing task. Odložit, dokud nebude zbytek vyřešen a neprovedena novelty rešerše. Odhad: 10–18 hodin.

---

## 4. Společné zásady: AI-asistovaná proveniencí, autorství, reprodukce

### 4.1 Co znamená „AI-asistovaný výzkum" pro autorství

Všech pět draftů bylo generováno AI-asistovaným výzkumným pipeline. To konkrétně znamená:

- **Výpočty**: calc.py skripty a výsledky (results.json, výpočetní poznámky VYPOCET-*) byly navrženy, spuštěny a interpretovány jazykovým modelem bez lidské supervize každého kroku.
- **Citace**: proveniencé poznámky říkají „ověřeno verbatim z PDF" nebo „transcribed" — ale toto tvrzení **samo o sobě musí lidský výzkumník ověřit** otevřením každého PDF.
- **Framing**: vědecké argumenty a interpretace jsou AI-generované. Mohou být přesvědčivé, aniž by byly správné.

**Žádný draft nesmí být odeslán bez:**
1. Jmenovaného lidského autora, který prověřil fyziku a kód.
2. Explicitního prohlášení o AI-asistenci dle zásad cílového vydavatelství (viz `dokumentace/zasady-publikovani.md`-style konvence projektu).
3. Veřejného vydání calc.py pro reprodukovatelnost.

### 4.2 Pravidlo nezávislé lidské re-derivace

**Žádný draft nesmí být podán bez nezávislé lidské re-derivace klíčových výsledků.** Toto je absolutní pravidlo pro všech pět draftů:

- **draft-01**: nikdo dosud nezávisle nespustil VYPOCET-05, VYPOCET-08, VYPOCET-10 ani VYPOCET-14, VYPOCET-15.
- **draft-02**: nikdo dosud nezávisle neodvodil heat-kernel koeficienty, nespustil sympy, ani nezkontroloval citace na zdrojových PDF.
- **draft-03**: nikdo dosud nezávisle nespustil engine ani neodvodil oba limity.
- **draft-04**: nikdo dosud nezávisle nespustil žádný ze čtyř calc.py skriptů.
- **draft-06**: nikdo dosud nezávisle nespustil žádný z osmi calc.py skriptů (F-031/033/036/037/038/039 + kolo-22 F-040/F-041); jde o syntézu existujících findingů, takže re-derivace = re-run těchto výpočtů (viz §4.3).

### 4.3 Jak spustit reprodukce (přesné příkazy)

Všechny calc.py skripty jsou runnable. Standardní postup:

```bash
# draft-01 — SJ v rotujících prostoročasech
python /Users/pazny/projects/theoryOfEverything/core-data/calculations/sj-rotating-btz/calc.py
python /Users/pazny/projects/theoryOfEverything/core-data/calculations/sj-kerr-equatorial/calc.py
python /Users/pazny/projects/theoryOfEverything/core-data/calculations/sj-eigenvector-superradiance/calc.py
python /Users/pazny/projects/theoryOfEverything/core-data/calculations/sj-threshold-scan/calc.py
python /Users/pazny/projects/theoryOfEverything/core-data/calculations/sj-far-zone/calc.py

# draft-02 — identita −18/11
python /Users/pazny/projects/theoryOfEverything/core-data/calculations/a4-anomaly-matching/calc.py
python /Users/pazny/projects/theoryOfEverything/core-data/calculations/a4-graviton-index/calc.py
python /Users/pazny/projects/theoryOfEverything/core-data/calculations/lambda-induced/calc.py

# draft-03 — d_s klasifikátor
python /Users/pazny/projects/theoryOfEverything/core-data/calculations/ds-classification/calc.py

# draft-04 — přechod typů
python /Users/pazny/projects/theoryOfEverything/core-data/calculations/ssee-diamond/calc.py
python /Users/pazny/projects/theoryOfEverything/core-data/calculations/vn-type-slab-4d/calc.py
python /Users/pazny/projects/theoryOfEverything/core-data/calculations/ssee-slab-4d/calc.py
python /Users/pazny/projects/theoryOfEverything/core-data/calculations/sj-vn-type/calc.py

# draft-06 — mapa negativů (VŠECH 8 skriptů importuje `toe` → nutné PYTHONPATH=lib)
# spouštět z kořene repa s: PYTHONPATH=lib python <cesta>/calc.py
PYTHONPATH=lib python /Users/pazny/projects/theoryOfEverything/core-data/calculations/ds-amol-convention/calc.py        # Wall 1 mean (F-031)
PYTHONPATH=lib python /Users/pazny/projects/theoryOfEverything/core-data/calculations/ds-conformal-4d/calc.py          # Wall 1 konformní caveat (F-037)
PYTHONPATH=lib python /Users/pazny/projects/theoryOfEverything/core-data/calculations/ds-molecule-fluctuation/calc.py  # Wall 1 variance (F-038)
PYTHONPATH=lib python /Users/pazny/projects/theoryOfEverything/core-data/calculations/spectral-triple-modular/calc.py  # Wall 2 metric (F-033)
PYTHONPATH=lib python /Users/pazny/projects/theoryOfEverything/core-data/calculations/ncg-kms-unruh/calc.py            # Wall 2 temperature (F-036)
PYTHONPATH=lib python /Users/pazny/projects/theoryOfEverything/core-data/calculations/geometric-boost-dirac/calc.py    # Wall 2 kolo-22 (F-040)
PYTHONPATH=lib python /Users/pazny/projects/theoryOfEverything/core-data/calculations/amol-anomaly-ee-coeff/calc.py    # Wall 3 (F-039)
PYTHONPATH=lib python /Users/pazny/projects/theoryOfEverything/core-data/calculations/ncg-spectral-dimension/calc.py   # kolo-22 NCG↔d_s (F-041)
```

**Po každém spuštění:** porovnat výstup s headline čísly uvedenými v sekci 2 výše (checkboxy C). Každá neshoda je blokátor.

**Závislosti:** skripty pravděpodobně vyžadují numpy, scipy, sympy. Zkontrolovat requirements nebo import záhlaví každého calc.py.

**⚠️ Pořadí spouštění (zjištěno deterministickou reprodukcí 2026-06-06):** dva skripty čtou
výsledky sousedních adresářů — `sj-far-zone/calc.py` potřebuje hotový
`sj-threshold-scan/results.json` a `modular-flow-bd-4d/calc.py` potřebuje
`modular-flow-corner/results.json`. Spouštět tedy v pořadí uvedeném výše (threshold-scan
před far-zone) a nikdy nereprodukovat tyto adresáře izolovaně. Dále: po `sj-vn-type/calc.py`
spustit i `sj-vn-type/calc_uncertainty.py` (regeneruje pole `*_se_regression`/`*_ci68_bootstrap`).

**✅ Stav 2026-06-06:** kompletní deterministická reprodukce všech 20 výpočtů proběhla
(`workflows/review-prep/repro-runner.py`): **20/20 bitově identických** (jediné rozdíly
wall-clock pole). Viz `reports/2026-06-06-review.md` §(f). Lidská nezávislá reprodukce
tím NENÍ nahrazena — běžela na stejném stroji a prostředí.

**Aktualizace (2026-06-06 večer):** 5 skriptů mělo natvrdo absolutní cesty hosta (opraveno
na `__file__`-relativní; detail v review §f) — příkazy výše teď fungují z libovolného
umístění. Nejjednodušší cesta k reprodukci je nyní dockerizované prostředí:
`cd app && docker compose run --rm test` (rychlá sada) nebo
`docker compose run --rm -e FULL_REPRO=1 test` (všech 20, ~50 min) — pinované verze
knihoven odpovídají ověřenému prostředí (viz `app/README.md`).

**✅ Cross-HW reprodukce (2026-06-07):** všech 24 výpočtů nezávisle přepočítáno na
GitHub Actions (ubuntu/x86_64/OpenBLAS vs ověřený macOS/arm64/Accelerate): **0 verdict
flipů, 0 strukturálních rozdílů**; většina výpočtů přesně identická, max. core odchylka
7.05 % (jeden per-size element). Detail: `reports/2026-06-07-cross-hw.md`. Platformové
artefakty lze vyloučit jako zdroj výsledků; lidská re-derivace tím NENÍ nahrazena.
Manuální spuštění: workflow „Cross-HW reproduction" na GitHubu (volba `target`).

**✅ Stav 2026-06-09 (druhý/třetí oblouk + kolo 22):** numerická reprodukce druhého oblouku
je v `app/tests/test_reproduction.py` (`SLOW_CALCS`): **10/11 PASS deterministicky**;
`ds-amol-convention` vědomě vyloučen (čte staged archiv mimo /tmp sandbox) + dokumentován.
Kola 22 (`geometric-boost-dirac`/F-040, `ncg-spectral-dimension`/F-041) POKRYTA. Pokrytí
viz `reports/2026-06-09-numerical-coverage.md`. **⚠️ PYTHONPATH:** všech 8 draft-06 calců
+ draft-03 `ds-classification` importuje `toe` → nutné `PYTHONPATH=lib` (zakotveno v
`test_reproduction.py`; viz CLAUDE.md § Provozní konvence). Toleranční filozofie cross-HW:
noise floor 1e-10, core pole <10 %, diagnostická pole <500 %, patologicky nestabilní sekce
vyloučené přes `DIAGNOSTIC_PAT` — plošná jednotná tolerance falešně „selhává".

### 4.4 Agentní framework a dvojí verifikace (kontext pro revizora)

**Tří-rolová agentní smyčka.** Výpočty druhého/třetího oblouku vznikly přes tři výzkumné
agenty na `main` (`.claude/agents/`): **exploratory-engine** (návrh hypotéz/výpočtů),
**computational-physicist** (implementace calc.py + run), **adversarial-verifier** (audit).
Verifier opakovaně přebil optimismus: chytil tautologii F-034/F-036 (β_KMS=1 je
Tomita-Takesaki tautologie, ne měření), p-hacking riziko F-039, provenance mezeru kola 14,
a CAS revize chytila reálný **Myrheim-Meyer factor-2 bug** ve `formulas.json`. Co přežilo
tímto filtrem, přežilo opakované pokusy o popravu; co padlo, padlo s diagnózou. Agenti
zapisují podle pevného schématu (atomický/progresivní zápis, pole `status`) a odvozují cesty
`__file__`-relativně (portability guardy zelené — `app/tests/test_portability_guards.py`).

**Dvojí verifikace (CAS + numerika).** Každý vlajkový výsledek má až dvě nezávislé dráhy:
1. **CAS dráha** (`verification/cas/`, Wolfram Language): **175/175 symbolických checků** přes
   7 skriptů; formula-coverage 38 vzorců (24 verified + 14 already_validated); **Myrheim-Meyer
   RESOLVED**. Nezávisle na sympy re-odvozuje −18/11, konformní-graviton −398/261, Λ-ledger.
   Spuštění: `python3 verification/cas/run_all.py` (po `brew install --cask wolfram-engine`
   + `wolframscript -activate`); očekává se `overall_pass = True`. Viz `verification/cas/README.md`.
2. **Numerická reprodukce** (`app/tests/test_reproduction.py` + cross-HW GitHub Actions; viz
   §4.3). Deterministická bit-identita na řízeném prostředí + cross-platform robustnost.

**Důležité:** žádná z drah NEnahrazuje lidskou nezávislou re-derivaci (§4.2) — obě běžely na
prostředí projektu. CAS pokrývá symbolické identity, numerika stochastické výpočty; překryv
je strukturální, ne plný (žádný second-arc calc není pokryt OBĚMA současně).

---

## 5. Co v draftech není — a proč je to dobře

### 5.1 Zabité programy a proč nejsou v draftech

**γ–Cardy sjednocení (H4g-2)**

Hypotéza: fermionová indukce (−18/11 identita) + Cardy-like entropic formula pro kauzální množiny = sjednocující vztah pro γ-konstantu v LQG. Program byl prozkoumán a zabit čistou negativní odpovědí: Cardyho formula se vztahuje k 2D CFT, kde centrální náboj c vstupuje přes Virasoro algebru — to nemá přímý analog v 4D LQG-γ nebo v NCG spektrálním akci kontextu. Přenos by vyžadoval ztotožnit dva různé „c" — to je kategoriální chyba, ne výzkumná otázka. **Proč je dobře, že to v draftech není:** přítomnost neobhajitelného bridge argumentu by podryla důvěryhodnost celého projektu.

**Λ-sjednocení (H4g-3) — výsledek VYPOCET-17**

Hypotéza: stejná fermionová indukční logika, která fixuje −18/11, predikuje druhou obsahově-nezávislou identitu pro kosmologickou konstantu. VYPOCET-17 tuto hypotézu čistě zabil: a₀ a a₂ sedí na různých cutoff-řádech (Λ⁴f₄ resp. Λ²f₂), jejich poměr nese (f₄/f₂)Λ² — rozměrový a cutoff-tvarový závislý. Fyzická Λ_cc/m_Pl² nese explicitní 1/N → obsahově závislá. Navíc: STr 1 = n_B − n_F = −62 → −68 s ν_R (boson/fermion imbalance se zhoršuje), žádná ze tří supertraces STr 1 = STr M² = STr M⁴ = 0 není splněna NCG SM obsahem. **Proč je dobře, že to v draftech není:** poctivé přiznání limitu (−18/11 nemá kosmologickou sestru) posiluje důvěryhodnost toho, co v draftech zůstalo. Tvrzení zůstalo úzké a obhajitelné.

**H4g-3 konektor: LQG γ-gap = CLPW cutoff**

Třetí noga trojúhelníkové identifikace v draft-04 (SSEE truncation = crossed-product cutoff = LQG area gap Δ = 4√3 π γ ℓ_P²) zůstává **explicitně neotestovaná a označená jako konjektura**. To, že tato noga není prezentována jako výsledek, je záměrné a správné: žádný numerický důkaz pro toto propojení neexistuje. **Proč je dobře, že tam není:** prezentovat neotestovanou spekulaci jako výsledek by byl etický problém a vědecká chyba. Konjektura je explicitně označena v §5 a TODO draft-04 — to je správný způsob, jak s ní pracovat.

### 5.2 Co z toho plyne pro budoucí práci

Zabité programy nejsou ztracená práce — jsou to ohraničení, která říkají, kde jádro drží a kde ne. Výsledek VYPOCET-17 je sám o sobě pozitivní výsledek (záporná odpověď je výsledek), který posiluje main claim draft-02. Podobně neotestovaná LQG noga v draft-04 je čestně označená budoucí výzva, ne skrytý problém.

---

*Konec dokumentu. Verze: 2026-06-09 (kolo 22 + velké review: 5 draftů, F-001..F-041, agentní framework §4.4, dvojí verifikace §4.4, draft-06 §2.5 + §4.3 příkazy, 7 ref-atribucí k opravě; předchozí 2026-06-08 kola 12–16, 2026-06-06). Vědecký companion: `reports/2026-06-09-velke-review.md` (referee verdikt + odhady času). Integritní companion: `reports/2026-06-09-consolidation.md`. Generováno AI koordinačním agentem. Všechny checkboxy jsou určeny pro lidské splnění před jakýmkoli externím sdílením nebo odesláním.*
