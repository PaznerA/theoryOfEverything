# Progress tracker — Theory of Everything

> 🟢 **CROSS-HW REPRODUKCE POTVRZENA + ŠKÁLOVANÉ BĚHY BĚŽÍ (2026-06-07)** — všech 24 výpočtů přepočítáno na GH Actions (linux/x86_64/OpenBLAS): **0 verdict flipů, 0 strukturálních rozdílů**, většina výpočtů přesně identická, max core odchylka 7.05 % (detail [`reports/2026-06-07-cross-hw.md`](reports/2026-06-07-cross-hw.md); tolerance rekalibrována — noise floor + core/diagnostic split, commit `9d1c205`). Paralelně běží 3 škálované běhy `compute.yml`: `ds_cap_4d` (c^{4D} vs c^{2D}≈7.57, ρ→960), `ds4d_saturation` (F-025, ρ→2000), `ds_entropy_cap_2d` (F-028, ρ→30 000). **Po doběhnutí:** vyhodnotit artifacts → VYPOCET-25+. Follow-upy: H5g-4 (spektrální triple ↔ SJ K), H5g-5 (Kerr-AdS B).

> 🟢 **KOLO 12 DOKONČENO (2026-06-06)** — `lib/toe` povýšena na **v0.3.0**: sparse eigensolver mašinérie (float64 + float32, dense vs. sparse cross-validace, determinismus equal-seed bit-identikal); VYPOCET-23 A/4 strop dS + VYPOCET-24 tracialní sonda dS; 16 nových sparse testů. **Testy zelené: 304 passed, 14 skipped, 1 xfailed v 99.4 s** (ze 288 kolo 11, +16). **findings.json** rozšířen na **28 nálezů** (F-027 tracialní null uzavřen, F-028 kvantitativní A/4-like area-zákon dS). Web přebuildován po výsledcích (viz Task 4). Předchozí milník: kolo 11 — toe v0.2.0, 5 lib migrací, draft-04 §4.3.

> 🟢 **KOLO 11 DOKONČENO (2026-06-06)** — `lib/toe` povýšena na **v0.2.0**: všech 5 lib_proposals z VYPOCET-22 migrováno (sprinkle_wedge_box4d, bd_smeared_dalembertian_inverse, sj_state rel_floor, entropy.modular_kernel, viz.nl_vs_locus); **draft-04 rozšířen o §4.3 dS static patch** (H5g-6 rozhodnutí: ne samostatný draft-05); abstrakt, reference a REVIZE-PRO-CLOVEKA.md aktualizovány. **Testy zelené: 288 passed, 14 skipped, 1 xfailed** (14 nových validačních testů, bez regrese). Web přebuildován: **103 stránek**. Předchozí milník: kolo 10 — H5g-1 PARCIÁLNÍ, H5g-3 VYVRÁCENA, `lib/toe` v0.1.0.
>
> ✅ **VŠECHNY 4 KROKY ROADMAPY MAJÍ PRVNÍ VERZI HOTOVOU** — research ✅, velké review ✅, lib/toe v0.2.0 ✅, minimalistický web ✅.

## Roadmapa (zadání uživatele, 2026-06-06)

1. **Dokončit základní research** — kolo 9 (běží) → BRAINSTORM-05 → závěrečná zpráva.
2. **Velké review** (až doběhne kolo 9): kontrola správnosti všech dat, doplňování (teoretických) vazeb v grafu konceptů, celkový úklid repozitáře.
3. **Simulace a vizualizace** 🟢 *(zahájeno 2026-06-06; první verze hotová)*: založené na jednotlivých vzorcích z `core-data/formulas.json`, sjednocené do **co nejmenších kombinovatelných funkcí** (composable functions) podporujících/vyvracejících naše teze. → `lib/toe` v0.1.0 (8 modulů, 53 funkcí, testy zelené); viz [`lib/README.md`](lib/README.md).
4. **Minimalistický web** 🟢 *(dokončeno 2026-06-06; první verze hotová)*: prezentace papers, dat, tezí, nápadů a grafů; minimalistický framework, který **builduje web přímo z existující souborové struktury** repozitáře (markdown + JSON registry jako zdroj pravdy). → `web/build.py` (103 stránek v `web/dist/`); spuštění: `python3 web/build.py` nebo `docker compose --profile web up web`; viz [`web/README.md`](web/README.md).

## Aktuální stav

✅ **Fáze 2: Hledání souvislostí — ZÁKLADNÍ RESEARCH DOKONČEN** (kola 3–9, 2026-06-06): 4 drafty článků (draft-01 v0.2 SJ rotující prostoročasy, draft-02 a₄ fermionová identita, draft-03 d_s jako klasifikátor, draft-04 typ-přechod kauzální množiny). VYPOCET-19 diskriminoval II₁ vs II_∞ na dS statické záplatě: obsah-sledující veličiny saturují pro ohraničenou dS záplatu a rostou pro plochou kontrolu; 2/3 proxy baterie prošla. VYPOCET-20 částečně replikoval H4g-1 v 4D s BD d'Alembertiánem: slab/diamant off-diagonální sklon kontrastuje správně (−1.10 vs −0.52), rohová koncentrace nereplikuje (3/5 signatur). findings.json = 24 nálezů. BRAINSTORM-05 zapsán (6 hypotéz H5g-1–H5g-6). Závěrečná denní zpráva: `reports/2026-06-06-day-report.md`. **Další krok: velké review.** Vstupní bod pro lidskou revizi: **`papers/REVIZE-PRO-CLOVEKA.md`** — přehled stavu všech 4 draftů, doporučené pořadí revizí, kompletní checkboxy, příkazy pro spuštění calc.py.

## Fáze

| # | Fáze | Stav | Zahájeno | Dokončeno |
|---|---|---|---|---|
| 1 | Základní rešerše (18 pilířů QG) | ✅ dokončeno | 2026-06-05 | 2026-06-05 |
| 2 | Hledání nenalezených souvislostí (základní research) | ✅ dokončeno | 2026-06-05 | 2026-06-06 |

## Log

### 2026-06-07 (housekeeping — GH Actions výpočetní infrastruktura, compute/ drivery, web/Pages)

- **3 škálované výpočetní drivery** dokončeny v `compute/drivers/`: `ds_entropy_cap_2d.py` (F-028 rozšíření přes 100× hustotní rozsah), `ds4d_saturation.py` (F-025 dokončení přes řídkou 4D cestu N až ~2×10⁴), `ds_cap_4d.py` (otevřená otázka c^{4D} vs. c^{2D} ≈ 7,57). Sdílená infrastruktura v `_common.py` (argparse, atomický checkpointing, time-budget, host fingerprint, deterministické seedy). Testy: `app/tests/test_compute_drivers.py` — 4 smoke testy driverů, každý < 30 s (8,7 s / 13,0 s / 1,2 s). Plná suite: **308 passed, 14 skipped, 1 xfailed v 144 s (exit 0)**.
- **GitHub Actions workflowy**: `repro.yml` (cross-HW reprodukce — matice 24 výpočetních adresářů, max-parallel=20, timeout 350 min, artefakty `repro-<dir>`); `compute.yml` (manuální trigger škálovaných driverů — výběr ze 3 driverů, předání args + max_hours, artefakt `<driver>-run` 90 dní, GITHUB_STEP_SUMMARY s fyzikálními výsledky).
- **Repo veřejné + GitHub Pages running**: web buildovaný z `web/dist/` (103 stránek) publikován přes Pages workflow.
- **`compute/README.md`** napsán: účel, tabulka 3 driverů, checkpointing, kam padají výsledky, postup začlenění po stažení artefaktu.
- **`knowledge-base/00-INDEX.md`** aktualizován: nová sekce Infrastruktura → compute/ + GH workflows.

### 2026-06-06 (kolo 12 — VYPOCET-23: A/4 strop dS entropie + VYPOCET-24: tracialní sonda II₁, toe v0.3.0 sparse; úklid housekeeping)

- **toe v0.3.0 sparse mašinérie — validace:** Numerická validace overlap N∈{1000,2000}, float64 operator, dense vs. sparse: top-k eigenvalue rel diff ~3e-15 (N=1000 k=256) / ~3.7e-15 (N=2000 k=320), target <1e-8 PASS. Truncated SSEE S_trunc rel diff ~1.3e-14 / ~9.3e-15, target <1e-6 PASS. Hermiticity residual 3.5e-13; ±pairing_residual_rel <1e-10; matvec vs dense iD@x = 2.7e-15. Determinismus: equal-seed eigsh → bit-identikal spektra (np.array_equal True). SCALING SMOKE: N=8000 k=600 eigsh (float32, tol=1e-9) = 31.6 s (<120 s), build memory ~0.5 GB (<2 GB), top|lambda|=1715 ~ 0.21·N. `__version__` 0.2.0→0.3.0; 64 veřejných jmen (bylo 60). 16 nových sparse testů; full suite **304 passed / 14 skipped / 1 xfailed v 99.4 s**.

- **VYPOCET-23 — Strop dS entropie vs. Gibbons-Hawking A/4, test H5g-2 (F-028):** (viz podrobný zápis výše v log kola 12)

- **VYPOCET-24 — Tracialní (max-entropický) podpis II₁ dS záplaty při ρ∈{10³,3×10³,10⁴}, retest VYPOCET-19 Část 3 (F-027):** (viz podrobný zápis výše v log kola 12)

- **findings.json** rozšířen na **28 nálezů**: F-027 (VYPOCET-24 tracialní null uzavřen — tracialní IR-akumulace neviditelná pro diskrétní SJ+κ sondu v 2D; identifikace II₁ stojí na obsah-saturaci, ne přímém tracialním podpisu; coordinate bug oprava nosná); F-028 (VYPOCET-23 kvantitativní area-zákon dS — R_full=0.1321±1.3% konstantní přes 5× hustotu i 2× velikost záplaty; S_cap=A_horizon/(c·G), c≈7.57 ≠ 4; slabá H5g-2 POTVRZENA, silná VYVRÁCENA). **Poznámka k draft-04 §4.3:** výsledky VYPOCET-23/24 neobsahují nová tvrzení navazující na stávající text §4.3 (který shrnuje F-023/F-025); tracialní null F-027 uzavírá otevřenou sondovací otázku ze sekce Část 3 VYPOCET-19 — viz TODO.md §7b.

- **VYPOCET-23 — Strop dS entropie (F-023) vs. Gibbons-Hawking A/4, test H5g-2 (F-028):** 2D dS statická záplata (`toe.sprinkle_ds_static_patch2d`), fixní entanglement řez r*=0.8, hrana boxu → kosmologický horizont. **Antikruhovost:** ε ∼ ρ^(−1/2) zafixováno z NEZÁVISLÉHO F-006 (ssee-diamant p_rank=0.519±0.007) PŘED měřením. **2D plocha horizontu:** kodim-2 ⇒ ve 2D BOD; „plocha" = 0-rozměrný Dou-Sorkin počet kauzálních molekul (linků křižujících řez), bezrozměrný a ε-nezávislý (A/ε⁰=A). **Primární kanál R_full = S_full_cap / A_mol:** S_full_cap i A_mol škálují obě ∼ρ^1.05, takže poměr je ρ-invariantní. R_full **KONSTANTNÍ** napříč 5× hustotou ρ∈{240,600,1200} (0.1339,0.1321,0.1306; drift −0.015, CV 1.25 %) I 2× velikostí ℓ∈{0.7,1.0,1.5} (CV 1.6 %): **kombinovaně R = 0.1321 ± 1.3 %**. ⇒ S_cap = A_horizon/(c·G), **c ≈ 7.57**. Truncovaná SSEE je O(1) a NEsleduje A_mol (S_trunc∼ρ^0.09) — není to A/4 kanál. Sparse blok (ρ=3000, N≤6000): obsah saturuje na 6000, S_trunc≈1.14 O(1). **VERDIKT: slabá H5g-2 POTVRZENA** (existuje konstantní A/4-podobný area-zákon; kvalitativní→kvantitativní upgrade), **silná H5g-2 VYVRÁCENA** (c≈7.57 ≠ 4: geometrická O(1) normalizace molekulového počtu vs SSEE není fixována na 4 — Dou-Sorkin koeficient vyžaduje separátní kalibraci). Strojová přesnost ± párování: dense ∼1e-15, sparse ∼2e-9 (float32). Pozn.: `results.json` rekonstruováno z kompletního `run.log` (běh spadl na starém příliš těsném float32 assertu PO zalogování veškeré fyziky; assert nyní path-aware; double-log bug v drift_law opraven). (F-028)

- **VYPOCET-24 — Tracialní (max-entropický) podpis typu II₁ dS záplaty při ρ∈{10³,3×10³,10⁴}, retest poctivého nullu VYPOCET-19 Část 3 (H5g-2 příbuzné, F-027):** 2D dS statická záplata, box r*≤5, fixní bulk řez r*≤1, `toe` v0.3.0 řídká cesta. **Část A (hustá, GENUINE netruncovaná IR-frakce, N≤3000, 3 seedy):** dS f_IR sklon d/d ln N = **+0.495 ± 0.112** (CI68 [0.350, 0.660]), ale plochá kontrola **+1.493 ± 0.483** (CI68 [0.838, 2.205]) → mezera dS−plochá = **−0.998 ± 0.495** (ZÁPORNÁ); n_mod ∼ N^0.996 (dS) vs N^1.019 (plochá). **Část B (řídká, truncovaný typ-II obsah až ρ=10⁴, N≤2×10⁴):** sparse=dense validace S_trunc rel diff **4.1×10⁻¹⁴**; dS S_trunc 0.551→0.625 (sklon/lnρ **+0.068**, SATURUJE) vs plochá 0.517→0.626→0.734 (sklon **+1.220**, 18× strmější, ROSTE); dS ρ=10⁴ vynecháno (n_sub=15238>cap, lokální eigh = n_sub³ stěna, poctivý avatar II₁ ohraničenosti). Strojová přesnost iΔ ±-párování max 6.7×10⁻¹⁵; capture-complete dS i plochá. **Verdikt NULL PŘETRVÁVÁ**: tracialní IR-akumulace se neobjevuje ani při 6× hustotě VYPOCET-19 — identifikace II₁ stojí na saturaci OBSAHU (VYPOCET-19 Část 1 + zde Část B), ne na přímém tracialním podpisu. Vysvětlení: tracialní stav padá do mezery mezi netruncované (III₁ UV pile-up) a truncované (typ-II s IR-mezerou eps≳2.7) spektrum; κ=√N/(4π)-truncace systematicky vyřezává nízko-eps módy, takže tracialní akumulace je diskrétní SJ+κ sondě ve 2D v principu neviditelná. **Numerická oprava (nosná):** řídké stavitele `causal_blocks_2d`/`idelta_operator_2d` berou souřadnice jako EXPLICITNÍ nulové (u,v)=(t−r*,t+r*); předání (t,r*) napřímo dá chybnou kauzální matici (matvec rel chyba 0.63). (F-027)

### 2026-06-06 (kolo 11 — toe v0.2.0, 5 lib migrací z VYPOCET-22; draft-04 §4.3 dS)

- **`lib/toe` v0.2.0 — 5 migrací z VYPOCET-22 (lib_proposals):** Všechny návrhy implementovány s respektem k vrstvám A/B/C a konvencím ARCHITECTURE.md; 14 nových validačních testů (3 causet + 3 sj + 3 entropy + 5 viz); plná sada zelená 288 passed, 14 skipped, 1 xfailed (z 274 před kole 11). Refaktor `modular-flow-codim2/calc.py`: 4 fyzikální funkce importovány přímo z `toe`, přegenerovaný `results.json` BIT-FOR-BIT identický s commitnutým. `__init__.py` = 59 jmen, `__version__ = '0.2.0'`; CHANGELOG v `lib/README.md` (česky); ARCHITECTURE.md §5 (anglicky).
  - **M1 `toe.causet.sprinkle_wedge_box4d` (vrstva A):** t-symetrický 4D box s codim-2 hranou E={t=0,x=0}; test iΔ ± pairing_residual_rel < 1e-12.
  - **M2 `toe.causet.bd_smeared_dalembertian_inverse` (vrstva A):** rozmazaný BD G_R=B_eps^{-1}, eps-sourozenec ostré varianty; wedge_cond_B[0]=15577.092005018936 (N=800, 3 seedy, eps=0.6, rtol 1e-6, <5 s).
  - **M3 `toe.sj.sj_state(..., rel_floor=None)` (vrstva B):** relativní spektrální práh; výchozí None zachovává absolutní-tol chování BIT-IDENTICKY (doloženo array_equal testem).
  - **M4 `toe.entropy.modular_kernel` (vrstva C):** dataclass `ModularKernel` exposing K(x,y); mk.S konzistentní s ssee(...).value (trace-relace, rel diff ~3e-13). Adaptace: dataclass místo holého dictu.
  - **M5 `toe.viz.nl_vs_locus` (vrstva A, importuje jen toe.fits):** panel non-lokalita vs vzdálenost k locusu; vrací Figure + připíná raw data jako `fig._nl_vs_locus`. Adaptace: vrací Figure (viz-kontrakt).
- **draft-04 §4.3 De Sitter static patch** (H5g-6 rozhodnutí — NE samostatný draft-05): konzervativní sekce s výsledky F-023/F-025 (statusy verbatim z findings.json): (a) CLPW II₁ vs II_∞ motivace; (b) 2D F-023 'supported' — obsah saturuje (N_total cap=480.1, R²=1.000); (c) 4D F-025 'partial' — S_trunc~N^{0.717±0.029} (CI68 [0.697,0.739]), exponent 0.27 vs 0.52, plná saturace nedosažena; (d) konformně-váhový caveat; (e) outlook sparse solvers + H5g-2. Abstrakt rozšířen; reference doplněny o 1306.3231 a 1205.3855. Původní geometrický caveat přečíslován na §4.4. TODO.md a REVIZE-PRO-CLOVEKA.md aktualizovány (§7b s human-verification checkboxy; odhad revize draft-04 bumpnut na 16–26 h).

### 2026-06-06 (kolo 10 — VYPOCET-21/22, první `lib/toe`-powered výzkumné kolo)

- **VYPOCET-21 — 4D dS statická záplata: truncovaná area-law SSEE a II₁/II_∞ diskriminátor (H5g-1, F-025):** 4D sech²-vážený slab, iΔ link matrix, n_max=2N^{3/4}, N≤2496, 4 seeds, rho=120. **Část 1 (diskriminátor, N≤2496):** flat/dS full-slope ratio 2.96; R*-exponenty dS a=0.27 vs plochá a=0.52 — reálný 4D-specifický separační signál; N_total dS strop 480 (R²=1.000) vs plochá lineární růst (slope 480/unit r*) — F-023 II₁/II_∞ obsah-diskriminace lifted do 4D. **Část 2 (fixní oblast, N=434→2407):** S_trunc~N^{0.717±0.029} (CI68 [0.697,0.739], R²=0.993) — nad cílem 0.5, dS radiální geometrie strmí area law; S_full~N^{1.017} (volume/III); modulární pile-up full 6→32 vs trunc=0 (III→II potvrzeno). Strojová přesnost iDelta ±-párování <6.84e-15. Runtime 292 s. **Verdikt PARCIÁLNÍ**: signál je přítomen a je 4D-specifický (ne 2D artefakt), ale plná saturace truncované S při N≤2500 nedosažena — pro čistou saturaci nutné větší N (řídké eigensolvery, rho>~10³, větší ℓ). Konformní-váhový caveat (4D skalár není konformně invariantní) zapsán poctivě. `h5g6_input`: výsledek jde do draft-04 jako dS sekce, ne standalone draft-05. **Lib rozšíření**: přidán `toe.causet.sprinkle_ds_static_patch4d` (4D sech²-vážený dS slab, re-exportován v `toe/__init__.py`); 6 nových testů v `app/tests/test_toe_causet_ds4d.py`; regrese: všech 258 testů prošlo (1 xfail), bez regrese. (F-025)
- **VYPOCET-22 — Codim-2 spoj / wedge-joint: 4D analog rohu? (H5g-3, F-026):** 4D, BD d'Alembertián, N∈{800,1200,1700,2200}, 3 seeds. Codim-2 klínová hrana dává nl-vs-hrana sklon +0.115 (SE 0.053, CI68 [0.106,0.124], R²=0.54); wall-controlled inner slope +0.251 (CI68 [0.209,0.292]). Obě **kladné**, stejné znaménko jako 4D null-tip F-024 (+0.71), **opačné** než 2D roh VYP-18 (−0.383) — modulární non-lokalita ke spoji KLESÁ, ne roste. Slab kontrolní hyperplane sklon = −0.043 (plochý). Edge/bulk f_nl ratio = 0.914 (<1). Diagonální boost-linearita R²=0.92 (BW boost strana PŘEŽÍVÁ). 1/4 signatur H5g-3. Strojová přesnost: max iDelta ±-párování residual_rel = 7.09e-15. **Verdikt H5g-3 VYVRÁCENA**: codim-2 spoj 2D rohovou koncentraci NEobnovuje — příčina je reálná 4D vlastnost (codim-2 lokusy mají transverzální y,z směry, kam boost teče volně i na hraně). Rohová podčást vrstva B dimenzionálně omezena robustně napříč 3 lokusy a 3 objekty. Slab/boost podčást vrstva B přežívá (4D-robustní). 5 `lib_proposals` pro budoucí migraci do `lib/toe` zapsáno do `results.json`. (F-026)
- **findings.json** rozšířen na **26 nálezů**: F-025 (H5g-1 parciální, 4D dS area-law SSEE, reálný 4D signál, saturace nedosažena); F-026 (H5g-3 vyvrácena, codim-2 hrana nerestore 2D roh, rohová podčást čistě 2D).

### 2026-06-06 (krok 4 roadmapy — minimalistický web framework)

- **`web/build.py` — minimalistický statický site-builder.** Framework builduje web přímo z existující souborové struktury repozitáře bez externích závislostí: **zdroje pravdy** jsou `knowledge-base/` (markdown próza), `core-data/*.json` (registry), `papers/` (drafty) — žádný duplicitní obsah. **Výstup:** `web/dist/` — **103 statických stránek** (index, přístupy, průřezová témata, datové registry, drafty, výpočty, nálezy, brainstormingy + detail stránek). Testy: **274 passed, 14 skipped, 1 xfailed v 27.64 s** (plná app+tests sada); webový subset: 16 passed (12 původních + 4 nové regresní testy). Review odhalilo 4 problémy (3 blocker/major) — opraveny před mergem. **Spuštění:** `python3 web/build.py` (lokálně) nebo `docker compose --profile web up web` (přes Docker, port 8080). Image rebuild nutný po změně requirements: `docker compose build`.

### 2026-06-06 (krok 3 roadmapy — `lib/toe` v0.1.0, kombinovatelná simulační knihovna)

- **`lib/toe` v0.1.0 — první verze kombinovatelné simulační knihovny.** Distilace 20 ověřených `calc.py` skriptů do **8 modulů** v striktních importních vrstvách (modul smí importovat jen z nižší vrstvy):
  - **Vrstva A (nezávislá):** `fits` (nosné dataclassy `FitResult`/`Measurement`/`ExactResult` + fit-primitiva `powerlaw_fit`, `bootstrap_slope_ci`, `regression_se`, `aic`/`aic_compare`, `validate_against` — kořen grafu), `causet` (sprinkling oblasti, `causal_matrix`/`link_matrix`, `green_retarded_2d/4d`, `bd_dalembertian_inverse`, `pauli_jordan`, `causal_diagnostics`), `spectral` (`return_probability`, `spectral_dimension(_flow)`, `ds_master_symbolic`, klasifikátor `d_s_uv`), `ncg` (`a4_heat_kernel_bracket`, `central_charges`, `a4_ratio`, `spectral_action_ratio`, `sector_ledger`, `str_count`, `lambda_induction_ledger` — vše přesné sympy `Rational`), `viz` (Agg panely `powerlaw_panel`/`spectrum_plot`/`radial_scan_plot`, importuje JEN `toe.fits`).
  - **Vrstva B:** `sj` (Sorkin-Johnston stav `sj_state`/`wightman`/`SJState`, observably `asymmetry_causal/_wightman`, `superradiant_weight`, `positive_subspace_overlap`).
  - **Vrstva C:** `entropy` (SSEE přes zobecněný eigenproblém: `kappa_2d`, `n_max_area_law`, `rank_at_cutoff`, `ssee`, driver `ssee_scaling`), `vntype` (proxy von Neumannova typu: `modular_spectrum`, `pile_up`, `trace_scaling`, `type_proxies`, `saturation_discriminator`).
- **Princip:** fyzikální vstupy → `(hodnota, SE/CI)` výstupy přes nosné dataclassy (nikdy holý float/tuple); explicitní `rng`/`seed` u všeho stochastického; `validated` flag přes jediný chokepoint `validate_against` proti `results.json` cílům; `Formula:`/`Evidence:`/`Conventions:` docstring tagy ke křížovému propojení s pilíři. Čistá knihovna (žádné I/O, žádný globální RNG, matplotlib jen v `viz`).
- **`toe/__init__.py`:** čisté veřejné re-exporty (53 jmen v `__all__`), `__version__ = '0.1.0'`, dokumentační mapa modulů. `import toe; toe.powerlaw_fit(...)` funguje přímo.
- **Testy: 252 passed, 14 skipped, 1 xfailed (~26 s)** s `MPLBACKEND=Agg python3 -m pytest app/tests`. Předchozí sady drží: `test_environment` (4 pinované verze + headless), `test_reproduction` rychlá sada (6 sub-sekundových výpočtů). 14 skipů = `test_full_reproduction` za branou `FULL_REPRO=1` (~50 min); 1 xfail = `test_proxy3_factor_like_false` (zdokumentovaná volnost proxy3 při malém N — committed 8-seed výsledek má `factor_like=False`, robustní tvrzení je `n_passing >= 1`). **Žádný validační cíl nebyl oslaben.** Jediná oprava: `test_toe_viz::test_import_restriction` přepsán na izolovaný subproces (kontroluje SKUTEČNÝ invariant „viz.py importuje jen toe.fits" místo polluce `sys.modules` od sourozeneckých testů a od eager `__init__`).
- **Ukázka:** `lib/examples/demo_pipeline.py` — end-to-end 2D diamant N≤500: sprinkle → kauzální order → `green_retarded_2d` → `pauli_jordan` → `sj_state` → truncovaná `ssee` (κ=√N/4π) → `powerlaw_fit` → `powerlaw_panel`. Výsledek `a ≈ 0.286` (SE 0.029, R²=0.98) — malý exponent = saturující type-II trend, NE volume-law ~1; panel `lib/examples/demo_output.png`; runtime <1 s. Dokumentace `lib/README.md` (česky).

### 2026-06-06 (velké review část 1 — verifikace, audit, opravy)

- **Verifikace referencí (150 z 652 arXiv ID, 95,3 % správných):** Nalezeno a opraveno 7 chybných záznamů: 2403.08696 a 2408.00071 označeny `⚠️ neověřeno`; 2404.07834 opraveni autoři (Carrozza, ne Toriumi et al.); 1208.2422 → 1205.1296 (SJ paper Afshordi-Aslanbeigi-Sorkin, 8 výskytů); 1708.07445 přeznačeno z Calcagni na Mielczarek–Trześniewski (2018); gr-qc/0601127 opraven název (Mattingly). Celkem editováno 14 zdrojových souborů.
- **Audit findings.json (24 nálezů F-001–F-024):** Opraveny cesty k evidenci ve 24 polích (15 nálezů); přidány `caveats` u 14 nálezů. Žádný status nezměněn — projekt měl statusy správně. Klíčový nuance F-019: N^{3/4} je crossed-product předpis, ne spektrální rys; 3/3 u VYPOCET-16 jsou čestné (proxy jsou trace/modulární spektrum/rank, ne centrální sekvence, která je nesignifikantní u VYPOCET-12 a VYPOCET-19).
- **Opravy draftů:** (1) draft-04: placeholder `a_err=0.775853` nahrazen skutečnými regresními SE a 68% bootstrap CI (2000 resamplů); klíčové SE: S_full 1.04±0.013, S_trunc 0.17±0.012, CV proxy SE 0.08–0.11 (potvrzuje 2/3 verdikt). (2) draft-03: hodnota 8 (CST random walk) označena jako ilustrativní ve 3 místech; přidána konvenční poznámka D vs D_space před tabulku §5.1.
- **Doplnění grafu konceptů:** 5 nových hran (3× von-neumann-algebras → causal-sets/quantum-cosmology/holography-adscft [partially]; 1× causal-sets→noncommutative-geometry obohacena [barely, H5g-4]; 1× nová conjecture causal-sets→black-holes-information [barely, H5g-2]). 2 nové konceptuální uzly: `type-iii-factor`, `type-ii-factor`.
- **consolidate.py spuštěn:** Nové statistiky: concept-graph **625 uzlů / 2476 hran**; connections.json **292 hran / 115 barely**; references.json **587 unikátních**; open-problems.json **153** (+9 fuzzy); formulas.json **247 unikátních**. VNA pilíř nyní na 11 hranách (dříve 0 v registru).
- **Report:** [`reports/2026-06-06-review.md`](reports/2026-06-06-review.md).
- **Část 2 (reprodukce):** Spuštěna souběžně; probíhá → `workflows/review-prep/repro-results.json`.

### 2026-06-06 (BRAINSTORM-05 + závěrečná zpráva)

- **BRAINSTORM-05.md** zapsán do `knowledge-base/`: 6 hypotéz páté generace (H5g-1–H5g-6) navazujících na výsledky kol 7–9 (dS II₁ diskriminátor, BD 4D modulární tok, causal-set typ-přechod).
- **Závěrečná denní zpráva** zapsána do `reports/2026-06-06-day-report.md`: přehled celého dne (kola 3–9), statistiky, stav všech 4 draftů, 24 nálezů, doporučení pro velké review.
- **Základní research Fáze 2 UZAVŘEN.** Další krok: velké review.

### 2026-06-06 (kolo 9 — VYPOCET-19/20, ESEJ-04, REVIZE-PRO-CLOVEKA.md)

- **VYPOCET-20 — BD d'Alembertián modulární tok 4D (H4g-1, F-024):** Replika VYPOCET-18 slab vs. diamantový roh s BD objektem v 4D (N≤2500). Slab off-diag sklon −1.10 vs. diamant −0.52 — kontrast přítomen, správný směr, síla větší než v 2D ale rohová koncentrace f_nl nereplikuje čistě (rohová f_nl 0.445, nl-vs-corner sklon +0.71; 4D rohové statistiky tenké). **Verdikt: PARCIÁLNÍ 3/5 signatur — H4g-1 v 4D s BD objektem: slab boost-geometricity robustní, rohová koncentrace dimensionálně omezena; link-matice 4D null (VYPOCET-18) je z části objekt-závislý artefakt.** Off-diagonal slope kontrast je nový pozitivní signál pro H4g-1 v 4D. (F-024)
- **ESEJ-04:** Čtvrtá syntetická esej zapsána (kolo 9).
- **REVIZE-PRO-CLOVEKA.md** zapsána do `papers/`: vstupní bod pro lidského autora; obsahuje přehledovou tabulku (vědecký stav + odhadovaný čas revize pro každý draft), doporučené pořadí revizí (draft-02 → draft-04 → draft-01 → draft-03), ~80 checkboxů pro matematické re-derivace / citace / čísla / konvence, sekce kritických high-risk položek (arXiv ID z 2025–2026 k ověření, placeholder a_err=0.776, ilustrativní hodnota 8 v CST), absolutní pravidla pro release (jmenovaný autor, AI-assistance statement, veřejný calc.py), přesné příkazy pro re-run všech 12 calc.py.
- **findings.json** rozšířen na 24 nálezů: F-023 (dS II₁ diskriminátor — obsah-saturace, 2/3 proxy, poctivý null tracialní přístup, Část 2 dS záplata); F-024 (BD 4D modulární tok — parciální 3/5, slab robust, rohová cast dimenzionálně omezena).

### 2026-06-06 (kolo 9 — VYPOCET-19 SJ de Sitter II₁ test)

- **VYPOCET-19 — SJ na dS statické záplatě × von-Neumannův typ: test CLPW II₁ vs II_∞ (F-023):** Sjednocuje dvě vlajkové linie (SJ horizonty × typový přechod) na de Sitteru. Konformní trik: 2D bezhmotný skalár konformně invariantní → SJ plochá v želvích souřadnicích $r^*=\ell\,\mathrm{arctanh}(r/\ell)$, horizont vstupuje jen přes $\mathrm{sech}^2(r^*/\ell)$ vlastní míru sprinklingu (ohraničená záplata = konečná stopa = II₁). ±-párování $i\Delta$ = 2.3e-13 (strojová přesnost). **Část 1 (diskriminátor II₁ vs II_∞): DISKRIMINOVÁNO** — obsah-sledující veličiny při růstu oblasti k horizontu: $N_{\rm total}$ 442→480 SATURUJE (strop 480, R²=1.000) vs plochá 768→3360 ROSTE; $S_{\rm full}$ 40.9→0 saturuje-a-překlápí (sat. fit R²=0.990) vs plochá 87.6→159.6 roste (sklon +12.2); net-změna druhé poloviny dS −13.1 vs plochá +21.7, mezera 34.8. Poctivá 2D limita: truncovaná SSEE je log/area zákon téměř box-nezávislý v OBOU (rozdíl žije v obsahu, ne v truncované entropii; ve 4D by truncovaná $S\sim\sqrt N$ sama oddělila). **Část 2 (tří-proxy baterie na dS záplatě): 2/3** — P1 stopa $S_{\rm full}\sim N^{1.11}$ (objem/III) → $S_{\rm trunc}\sim N^{0.12}$ (saturuje/II); P2 modulární pile-up $\sim N^{1.25}$ (III₁ flat-dense) → přesně 0 (II, ostrá IR hrana ε≈5); P3 centrální sekvence nesignifikantní při 5 seedech (jako VYPOCET-12). **Část 3 (max-entropický tracialní přístup): POCTIVÝ NULL** — IR-frakce netruncovaného spektra klesá (dS −0.008, plochá −0.004), tracialní nárůst nezachycen při N≲2500; $\langle\varepsilon\rangle_{\rm trunc}$ null z konstrukce (truncace zabíjí tracialní módy); scaling pro rozlišení: ρ~10³–10⁴. První běh odhalil artefakt (sech²-koncentrace nested oblast pohltí množinu → triviální SSEE), opraveno na bulk-středový řez s garantovaným komplementem. **Verdikt: DISKRIMINOVÁNO — diskrétní SJ sonda VIDÍ CLPW rozdíl II₁ (ohraničená dS, konečná Tr 1) vs II_∞ (neohraničená plochá).** Runtime 431 s, 5–6 seedů, N≤1950. (F-023)

### 2026-06-06 (kolo 8 — VYPOCET-17/18, draft-04, housekeeping)

- **VYPOCET-17 — Λ-indukce přes spektrální akci (H4g-3, F-020):** Exaktní sympy + literatura (CC hep-th/9606001 + Marcolli). Tr f(D/Λ) ~ 2Λ⁴f₄·a₀ + 2Λ²f₂·a₂ + f₀·a₄. a₀ (kosmologický) a a₂ (Einstein-Hilbert) jsou oba lineárně v N = Tr(1_F), ale sedí na různých cutoff-řádech (f₄Λ⁴ vs f₂Λ²) → jakýkoli poměr nese (f₄/f₂)Λ² = dimenzionální a scheme-závislý; jedině −18/11 (poměr uvnitř a₄, stejný řád f₀Λ⁰) je index-chráněný. Λ_cc/m_Pl² = π²f₄/(2N f₂²k̂²) nese explicitní 1/N. Indukovaná γ₀ cutoff-kvartická (~10¹²² mismatch). STr 1 = n_B − n_F = −62 (bez ν_R) / −68 (s ν_R): ν_R rovnováhu počtů zhoršuje, nezlepšuje. Všech 8 interních VERDICT klíčů True. **H4g-3 je VYVRÁCENA jako pozitivní hypotéza. Draft-02 Λ-riziko uzavřeno.** (F-020)
- **VYPOCET-18 — modulární tok: slab vs. diamantový roh (H4g-1, F-021):** 2D, N=400–1800, 5 seeds. Self-test: corr(H_pi diagonála, analytická boost-váha)=0.992. Klíčový výsledek: off-diagonální sklon modulárního kernelu SJ stavu = −0.47 (slab, geometrický/boost-lokální) vs. −0.094 (diamant, negeometrický), gap 0.37 stabilní. Slab diagonální modulární váha lineární v vzdálenosti od entangling surface (R²=0.977, BW boost-váha). Per-site non-lokalita f_nl roste monotónně 0.673 (hluboký bulk) → 0.828 (roh), sklon vs. vzdálenost-k-rohu = −0.383 (R²=0.989); roh/bulk ratio = 1.15. Poctivé nuly: cross-corner u-v′=±2L coupling ratio=1.00; integrovaná f_nl neodliší slab(0.72) od diamantu(0.72) — diskriminace jen v off-diag sklonu. 4D (link matice, N≤2500): NEREPLIKUJE — slab/diamant ratio=0.996, rohová f_nl (0.11) < bulk (0.31) opačné znaménko, nl-vs-roh sklon=+0.75 (link-matice řídkost ~N^0.65 + tenká rohová statistika). **H4g-1 PODPOŘENA v 2D (4/5 signatur); 4D nereplikuje (poctivý null).** Runtime 248 s. (F-021)
- **draft-04-type-transition-causal-sets:** Draft a TODO zapsány do `papers/draft-04-type-transition-causal-sets/`. Testuje hypotézu Sorkin-Yazdi SSEE truncace = CLPW crossed-product typ III₁→II přechod. 2D diamant: 2/3 proxy (entropická stopa 80x, modulární pile-up N^1.14→0); 4D slab: 3/3 proxy (entropická stopa N^1.34→N^0.55, modulární spektrum flat-dense→integrovatelné, N^{3/4} selektivita). Geometrická výhrada (rohy diamantu ničí signaturu) a interpretace diskrétní škály jako modulárního cutoffu explicitely označeny jako konjektury. TODO.md: 8 lidských verifikačních bran, referee-útok příprava, etická poznámka, LQG-area-gap noha označena jako otevřená. (F-022)
- **findings.json** rozšířen na 22 nálezů: F-020 (H4g-3 vyvrácena, žádná druhá index-identita pro Λ, draft-02 uzavřen); F-021 (H4g-1 2D podpořena 4/5, modulární tok geometrický na slabu, negeometrický v rozích); F-022 (draft-04 zapsán, 2D 2/3 + 4D 3/3 proxy, N^{3/4} selektivita).

### 2026-06-06 (kolo 7 — VYPOCET-15/16, BRAINSTORM-04, SYNTEZA-02, housekeeping)

- **VYPOCET-15 — far-zone disambiguace Kerr a=0.6 (H3g-1, F-018):** Log-log diskriminant: corr(log W_sr, log Ω)=0.9992 vs. corr(log W_sr, log 1/(r−r_erg))=0.942 — favorizuje Model S. Joint fit (near+far, n=19, r=2.05–20M): ΔAIC(E−S)=+3894 (rozhodující). Near-zone A_W mocninový zákon (high-SNR n=11): |A_W|~r^{−2.75±0.03} (předp. −3, R²=0.957); |A_W|~Ω^{0.98±0.01} (předp. +1, R²=0.932). Far-zone (r=5–20M, 13 radii): W_sr=0 ve všech 13 poloměrech (pod (ω,k)-mřížkovým rozlišením); A_W<0 na všech 13. **Verdikt: VYPOCET-14 ambiguita pro a=0.6 uzavřena; Ω(r) jako spojitý řídící parametr superradiantního nástupu potvrzen konzistentně pro všechny tři geometrie (Kerr a=0.6, a=0.9, BTZ J=0.9).** Seeds: 5, N=1600. (F-018)
- **VYPOCET-16 — vN-type proxy v 4D slab (H3g-3, F-019):** 4D box-slab, iΔ link matrix, interior half-space cut, T=0.5, L=0.85, N=800–3500, 5 semen. Proxy 1 (entropická stopa): S_full~N^{1.34} (volume/super-volume, III divergentní, 27.5→209.1); S_number-trunc[n_max=2N^{3/4}]~N^{0.55}≈sqrt(N) (4D area law, typ II, 2.69→5.84), kolaps 36x; fixní-frakční kontrola S_frac~N^{0.83} area law NESPLNÍ. Proxy 2 (modulární spektrum eps=ln[mu/(mu-1)]): untruncated pile-up~N^{1.27} (III₁ flat-dense) → přesně 0 po truncaci (typ II, ostrá IR hrana eps~2.7, kompaktní nosič). Módový počet: full ~N^{1.11} → truncated ~N^{0.70} (~N^{3/4}). Proxy 3 (p=3/4 otázka): N^{3/4} number-truncace → area law YES; fixní-frakce SELHÁVÁ; slab spektrum nemá vlastní ostré koleno (auto-koleno ~N^{1.06}) → N^{3/4} je předpis (observer/crossed-product cutoff), ne spektrální rys. Pauli-Jordan +/- párování error = 7.1e-14 (strojová přesnost). **Verdikt: 3/3 proxy projdou — H3g-3 podpořena v d=4.** Runtime 158 s. (F-019)
- **BRAINSTORM-04.md** dokončen: 3 hypotézy čtvrté generace — H4g-1 (rohová non-Hadamardovost = místo kde selhává boost-flow, medium-high), H4g-4 (III→II přechod přežívá na 4D slabu ne na diamantu, medium-high; potvrzena VYPOCET-16), H4g-3 (fermionová indukce predikuje Λ přes f₀/a₀ moment, medium). Doporučená fronta: paralelně H4g-3 (exaktní sympy, dny) + H4g-1 (slab vs. diamantový roh modulární tok, vyšší konceptuální výnos). Soubor: `knowledge-base/BRAINSTORM-04.md`.
- **SYNTEZA-02.md** dokončena: přehled 7 kol, 19 nálezů, 5 uzavřených front (γ–Cardy, naivní Λ, plná SM, 4D volume-law jako dimenze-efekt, Model E pro superradianci); through-line (vlastnosti prostoročasu jako odpovědi na otázky); výhled 10 kol. Soubor: `knowledge-base/SYNTEZA-02.md`.
- **findings.json** rozšířen na 19 nálezů: F-018 (far-zone E-vs-S disambiguace, Ω(r) potvrzen pro všechny geometrie), F-019 (vN-type 4D slab 3/3 proxy, N^{3/4} operativní regulátor, H3g-3 d=4).

### 2026-06-06 (kolo 6 — VYPOCET-13/14, draft-03, ESEJ-03, housekeeping)

- **VYPOCET-13 — 4D SSEE slab geometry (H04 interpretace c, F-016):** Half-space cut (slab, iΔ link matrix, κ=0.05·λmax) dává AREA law: S~L^2.00 (R²=0.982), R²_area=0.984 > R²_vol=0.977. Interiérní edge-effect kontrola: S~L^2.18 (R²=0.989) — čistší area. Kontrast: 4D nested diamant (VYPOCET-06) = VOLUME S~f^6.1 (R²=0.998). **Verdikt: geometrie rohů (ne dimenze) určuje area vs. volume — interpretace (c) POTVRZENA, (a) vyvrácena.** Hadamardova diagnostika (log-log sklon |ReW|): 4D diamant inside=−1.53 vs corner=−2.79 (anomálie v rozích), 4D slab deep=−3.81 ≈ surface=−3.85 (žádná anomálie) — přesná signatura mechanismu (c). 2D diamant inside=−0.160 vs corner=−0.095 (anomálie na u−v′=±2L). Runtime 264 s. N≤2088 (slab, 3 seedy). Caveaty: literatura (2008.07697/2412.07832) nepotvrzuje non-Hadamard↔volume jako přímý mechanismus; absolutní Hadamardovy sklony finite-N deformované. Entropy-cluster program v 4D má živou cestu přes Rindler/slab klín (kde SJ ≈ Unruh = Hadamard).
- **VYPOCET-14 — superradiantní nástup: ergosféra vs. Ω(r) (H3g-1, F-017):** Radial scan W_sr: Kerr a=0.6 [0, 0.145], a=0.9 [0, 0.222] (12 radii each, monotone). Srovnání modelů (AIC): ΔAIC(E vs. S)=+441.6 (a=0.6), +4216.3 (a=0.9), +231.5 (BTZ J=0.9) — všechny tři rozhodující pro Model S (W_sr ~ Ω(r)^B). B=4.23 (a=0.6), 3.82 (a=0.9), 1.71 (BTZ). A_W znaménko: negativně-definitní ve všech 65 externích měřeních (5×8 Kerr + 5×5 BTZ); near-ergosphere |A_W|~0.49–0.60 vs far-zone ~0.03–0.05 (faktor ~15–20). BTZ cross-check J=0.9: stejná kvalitativní struktura (pattern_matches_kerr=True). **Verdikt: H3g-1 POTVRZENA.** Superradiantní váha řízena spojitým Ω(r), ne diskrétní ergosférou. Zbývající nejednoznačnost a=0.6 (lineární korelace mírně favorizuje Model E): Ω(r) a 1/(r−r_erg) korelovány → doporučen hustší scan r=5–20M (VYPOCET-15). N=1600, 5 seeds.
- **draft-03-ds-classifier:** Třetí draft přerámovává UV spektrální dimenzi jako klasifikátor (z, D, sonda); master-tabulka reprodukuje 12 publikovaných čísel z jediného P(σ) enginu; sonda jako třetí klasifikační osa doložena vnitřním rozporem v databázi (CST d'Alembertián vs. náhodná procházka). Sekce „Relation to prior work" vpředu; TODO.md připravuje obranu vůči hlavním referee útokům (Calcagni, probe-trivialita). Soubory: `papers/draft-03-ds-classifier/draft.md`, `TODO.md`.
- **ESEJ-03:** Třetí syntetická esej zapsána.
- **findings.json** rozšířen na 17 nálezů: F-016 (slab area law, rohová geometrie rozhoduje, H04-c potvrzena), F-017 (superradiantní nástup Ω(r) kontinuální, H3g-1 potvrzena).

### 2026-06-06 (kolo 5 — VYPOCET-11/12, draft-01 v0.2, housekeeping)

- **VYPOCET-11 — graviton sektor + index-teorém (H3g-4, calc11):** Fyzikální Einsteinův graviton je NEkonformní — nemá čisté (a,c), jeho anomálie jsou gauge/scheme-závislé a jen on-shell (Duff hep-th/9308075, hep-th/9503187). Konformní Weylův graviton dává c/(−a)=−398/261≈−1.525 (ne −18/11). Per-pole test: žádný boson není kolineární s Weylovým fermionem na rovině (a,c). Plné SM+konf.graviton: −6474/5123≈−1.264. Násobnost gravitonů nutná k vynucení −18/11: x=−143/32<0 (nefyzikální). **Závěr: identita −18/11 je striktní diskriminátor fermionového sektoru; nelze ji zachránit žádným gravitonem.** Index-teorémová část: spinorové koeficienty a₄ v bázi {C²,E₄,R²} jsou (−1/20, +11/360, 0) → (a,c)=(11/360, 1/20), shoda s Duff Tab.1 exaktně; Â-genus dává ind(D)=−σ/8, Rohlin σ=16→ind=−2 (sudé celé, zámek drží). −18/11=koef(C²)/koef(E₄) pro spinor = poměr Gaussovy-Bonnet/χ a Pontryaginovy/Â hustoty → H3g-4 posílena: spektrální akce je Sacharovova fermionově-indukovaná gravitace. Draft-02: dvě nezávislá blokování gravitonové záchrany jsou vnitřně konzistentní, release readiness potvrzena (čeká lidská re-derivace a citace-check).
- **VYPOCET-12 — typ vN algebry + SSEE truncace v 2D (H3g-3, calc12):** 2D, N=400–1800, 8 seeds, kappa=sqrt(N)/(4pi). Proxy 1 (entropy-trace): S_full~N^1.04 (volume, divergent III) → S_trunc saturuje 1.30–1.70 (area/log, finite II), 80x kolaps; Pauli-Jordan nukleární norma odstraní jen ~20% (typ žije v stavu/entropii, ne kinematice). Proxy 2 (modulární spektrum eps=ln[mu/(mu-1)]): untruncated ploché+husté (47–217 módů, pile-up eps<0.5 ~N^1.14, frakce N-stabilní 0.087±0.006) = Connes III₁; truncated integrovatelné (8–20 módů, pile-up=0, IR edge eps>1.6) = typ II. Proxy 3 (centrální posloupnosti): CV(S_trunc) 0.079→0.030 (samo-průměrující), nesignifikantní trend — nediskriminuje typ. **Verdikt: MIXED 2/3 — první přímý numerický důkaz crossed-product obrazu na kauzální množině; je to 2D výrok.** H3g-3: potřeba (a) 4D rozšíření, (b) 30+ seeds pro větší N, (c) analytické srovnání se crossed-product konstrukcí.
- **draft-01-sj-rotating-spacetimes v0.2:** Název aktualizován (přidán „eigenvector signature of superradiance"); abstrakt rozšířen o body (iv)–(vi) (mechanismus, překryv podprostorů 44.6°, superradiantní váha 0.0755); sekce 3.5 a 3.5b plně integrovány (ne přilepeny); sekce 3.6/4.1/4.2 aktualizovány; TODO.md: položky 1.4, 3, 6 označeny DONE; nová položka §8 (lidská re-derivace) jako gate; blokující zbývá: N→∞ studie, analytické SJ pro strižený diamant, srovnání s BTZ dvou-bodovou funkcí, verifikace citací, nezávislý re-run pipeline.
- **findings.json** rozšířen na 15 nálezů: F-014 (graviton+index, graviton identitu −18/11 nezachrání, Rohlinův zámek), F-015 (vN typ proxy, 2/3 III₁→II v 2D).

### 2026-06-06 (kolo 4 — BRAINSTORM-03, VYPOCET-09/10, draft-02, housekeeping)

- **BRAINSTORM-03.md** dokončen: 3 hypotézy třetí generace — H3g-1 (opačná znaménka A_caus/A_W jako superradiantní podpis, medium-high), H3g-4 (spektrální akce jako fermionově-indukovaná gravitace, high), H3g-3 (SSEE truncace = crossed-product modulární cutoff, medium). Doporučení: draft-02 jako nejpevnější aktivum, draft-01 uzavřít po VYPOCET-10.
- **VYPOCET-09 — BD d'Alembertián spektrum (H04 interpretace b):** BD G_R=B⁻¹ dává čistý mocninový zákon λ_k~k^-α (α≈3.0–3.4, R²≈0.99) tam, kde link matice dávala ploché spektrum — interpretace (b) potvrzena pro tvar. Ale α driftuje s N (+1.28 za N=500–3000, nekonvergoval), slope-knee p=0.977≈N¹ (identicky VYPOCET-06), area/volume cutoff-závislé. Hlubší selhání: váha k interpretacím (a) a (c). cond(B) 3.9e6→2.0e10. Runtime 394 s.
- **VYPOCET-10 — SJ eigenvektorová rotace + superradiance + mechanismus:** Kladné SJ podprostory rotujícího vs. statického řezu pootočeny o ~44.6° (cos²≈0.507) při <2% změně spektra — spin je eigenvektorový jev, ne spektrální. Váha v superradiantním klínu ω(ω−kΩ)<0 roste monotónně se spinem (a=0: 0.0000 exaktně → a=0.9: 0.0171) a k ergosféře (0.0000 při r=4.0 → 0.0755 při r=2.05). Toy model nulového diamantu reprodukuje obě znaménka A_caus>0/A_W<0 i velikosti (korelace 0.95–0.97): A_caus=kauzální geometrie clony, A_W=bezhmotná 2D Wightmanova funkce na stlačeném/roztaženém null-směru. Oba nejslabší body draftu-01 (TODO 1.4, 3, 6) vyřešeny.
- **draft-02-a4-fermionic-identity** zapsán: draft.md + TODO.md v `papers/draft-02-a4-fermionic-identity/`; věta o exaktní identitě C²/Euler = −18/11 + heat-kernel descent (§2) + SM falzifikace (−0.853 vs −1.636) + pozice v trojúhelníku Andrianov-Lizzi / Kurkov-Lizzi-Vassilevich. Slabiny: triviality-risk, konvence-závislost, schéma závislost a₄; doporučení: pursue s lidskou re-derivací.
- **findings.json** rozšířen na 13 nálezů (F-009 Kerr-BTZ geometrická nezávislost, F-010 γ–Cardy program closed, F-011 modular-hamiltonian top hub, F-012 BD d'Alembertián spektrum, F-013 SJ eigenvektorová rotace + mechanismus).

### 2026-06-06 (kolo 3 — VYPOCET-08/Kerr, H04-reframe, pilíř 19, draft-01)

- **VYPOCET-08 — Kerr ekvatoriální SJ (H2g-6):** VŠECHNY čtyři BTZ signatury replikovány na Kerru — SJ existuje strojovou přesností uvnitř ergoregionu (787±/790± páry, reziduál ~5e-16); null sklon se nuluje přesně v r_erg=2M pro a=0.6 i 0.9; opačná znaménka A_caus>0 vs. A_W<0 na každém (a,r) (a=0.6 r=2.6: +0.317/−0.296; a=0.9: +0.431/−0.382); A_caus roste monotónně se spinem (0.197/0.361/0.482 pro a=0.3/0.6/0.9). Závěr: SJ vlastnosti ergoregionu jsou geometricky nezávislé v prostředích se strhnutým rámem.
- **H04 — entropie-cluster reframe:** 4D link-matice spektrum ploché ⇒ interpretace (b) — BD d'Alembertián je správný kandidát (VYPOCET-09 navazuje).
- **Pilíř 19 — von Neumannovy algebry:** 27 nových konceptů, 32 ověřených referencí; po konsolidaci je modular-hamiltonian nový TOP HUB grafu (614 uzlů/2437 hran); fragment `von-neumann-algebras.json` uložen, consolidate.py spuštěn manuálně.
- **draft-01-sj-rotating-spacetimes** zapsán: `papers/draft-01-sj-rotating-spacetimes/draft.md` (v0.1) + `TODO.md`; nejslabší bod (opačná znaménka bez mechanismu) → řeší VYPOCET-10.
- **γ–Cardy program ukončen** (kolo 2 blocker Sen IR-universality plně potvrzen).

### 2026-06-06 (rozhodující kolo — H01 verdikt + VYPOCET-05/06/07 + findings.json)

- **γ–Cardy rozhodující čtení (H01 verdict: program-dead):** ENP 1006.0634 neobsahuje explicitní konstantní člen; Sen 1205.0971 potvrzuje, že log-koeficienty jsou IR-určeny (LQG −2 vs. Eukleidovská gravitace +1,71 — nesouhlasí); porovnávat konstantní člen s Carlipem/Cardy je fyzikálně nemotivované. H01 uzavřena. H2g-7 posílena jako definitivní negativní výsledek.
- **VYPOCET-05 — SJ stav v rotujícím BTZ ergoregionu (H2g-6, 2D analog):** 796+/796− eigenvalue, reziduál 4,6×10⁻¹⁶; statický řez na témže r není Lorentzův; kauzální asymetrie uvnitř ergoregionu = +1,000 vs. +0,007 vně; nulový sklon mizí přesně na r_erg=1,0; superradiantní signatura v eigenvektorech/W (ne v hrubém spektru). Teze H2g-6 (Strategie II) numericky potvrzena ve 2D sondě.
- **VYPOCET-06 — 4D SSEE cutoff scaling (H2g-3, p=3/4 predikce):** predikce NEPOTVRZENA; exponent závisí na cutoffu (0,65–0,98); slope-knee dává ~N¹; 4D nested diamant dává VOLUME law (R²=0,998). Jednoduchá 2D→4D extrapolace „změř p ze spektra" selhává. H2g-3 oslabena.
- **VYPOCET-07 — BMV AS fázová korekce (H2g-8):** AS korekce δφ/φ ≈ 6,2×10⁻²⁸ (klasický RG, bez ħ); EFT ≈ 3,4×10⁻⁶² (kvantový, s ħ); poměr AS/EFT ≈ 1,82×10³⁴; obě 24 resp. 59 řádů pod dosažitelností. Oppenheimova varianta (křížové korelace oscilátorů) potvrzena jako jediná realistická kontinuální diskriminace. H2g-8 posílena.
- **findings.json (8 nálezů):** pokrývají d_s probe-dependence (F-001/F-002), fermionový a_4 exaktní + SM falzifikace (F-003/F-004), 140× Λ prefaktor (F-005), ρ^(−1/2) potvrzení + ρ^(−1/4) vyloučení 39σ (F-006/F-007/F-008). Každý rozlišuje reprodukci literatury od projektového přínosu.
- **BRAINSTORM-02.md** doplněn o sekci "Výsledky rozhodujícího kola (2026-06-06)".
- **00-INDEX.md** aktualizován (VYPOCET-05/06/07, findings.json).

### 2026-06-06 (deep-dive kolo 1 — výpočty + dossiery + eseje + BRAINSTORM-02)

- **4 výpočty dokončeny:**
  - **VYPOCET-01 — d_s^UV klasifikační tabulka (L3-1):** Symbolický master d_s^UV = D/γ ověřen (sympy); 12/12 numerických kontrol PASS (tol 0,06); D=4 tabulka: GR→4, Hořava z=2→5/2, Hořava z=3→2, Stelle→2, AS (η_N=−2)→2, causal-set d'Alembertián→2 univerzálně, causal-set random walk→>D, multifraktální→2; všechny IR limity→4. **Verdikt: L3-1 v přerámované podobě PODPORENA** — probe-dependence jako třetí klasifikační osa doložena; řeší vnitřní rozpor connections 657 vs. 1777 (d'Alembertián→2 vs. random walk→>D ze stejné CST teorie).
  - **VYPOCET-02 — a_4 anomaly-matching test NCG SM algebry (L1-1):** Konvence: Duff arXiv:2003.02688, spektrální akce Chamseddine-Connes hep-th/9606001; koef(C²)/koef(Euler) = −18/11 spektrální akce = c/(−a) Weylova fermionu EXAKTNĚ pro 45 i 48 fermionů; faktor 11 sdílen (Euler 11/60, a_Weyl=11/720). Plná SM (N₀=4, N₁=12): −0,853 (bez ν_R) / −0,866 (s ν_R) vs. cíl −1,636. **Verdikt: L1-1 ve fermionové části PŘESNĚ POTVRZENA, v plné SM verzi JEDNOZNAČNĚ FALZIFIKOVÁNA** — obojí čistě; ν_R plnou shodu neuzavře, ale posouvá blíže (mismatch 0,784→0,771).
  - **VYPOCET-03 — Λ prefaktor srovnání:** Konvence: Λ l_P² = κ/√(V/l_P⁴), V=H₀⁻⁴; κ_Sorkin=0,2136, κ_EDT=1,53×10⁻³, κ_CosMIn(eff)=2,45; poměr κ_Sorkin/κ_EDT = 139,6 ≈ 140; Λ_obs l_P²=2,866×10⁻¹²². **Verdikt: silná sjednocující hypotéza VYVRÁCENA** (prefaktory se liší faktorem ~140, neslučitelné konvencí c_V; CosMIn nemá fundamentální κ); sdílí se pouze dimenzionální kostra Λ~H²; srovnání třech prefaktorů v literatuře neprovedeno — publikovatelný negativní výsledek.
  - **VYPOCET-04 — SSEE na sprinklovaném 2D kauzálním diamantu:** Entropický cutoff rank~N^0,519±0,007 → ε~ρ^(−1/2) (2,8 σ od přesně 1/2, ~39 σ od 1/4); intrinsická diskrétnost knee škáluje N^1,00; SSEE: volume-law 95,2 (bez truncace) → area/log-law 1,58 (dvojitě truncováno); 2D log-slope b=0,49 (kontinuum 1/3); N=400–1800, 5 semínek. **Verdikt: MECHANICKY PODPORUJE jádro** — truncace mění volume-law na area/log-law přes UV cutoff ε~ρ^(−1/2); ρ^(−1/4) vyloučeno 39 σ; identifikace s LQG area gapem ve 4D = nadcházející krok. Doporučena oprava entropy-cluster.md ř. 66 z ρ^(−1/4) na ρ^(−1/2).
- **3 dossiery (H01–H03):**
  - **H01 — Cardy-LQG (γ fixace):** jádro c=6k known (Carlip 1410.5763); identifikován blocker: Senova IR-univerzalita (1205.0971) strukturálně brání UV-fixaci γ z CFT; komplexní γ=±i (1212.4060) podkopává reálnou fixaci; priorita snížena.
  - **H02 — SJ vakuum pro Kerr/SdS:** genuinely open territory — žádná publikace SJ stav pro rotující ČD nezkonstruovala; Kay-Wald no-go neblokuje (SJ nevyžaduje Killing-symetrii); doporučen 2D analog (rotující BTZ / ekvatoriální Kerr).
  - **H03 — BMV/QGEM diskriminátor:** binary Q-vs-C test vyřešen (konsensus 2025); AS korekce ~10⁻⁶⁰ neměřitelná; jediný principiálně odlišitelný přístup = Oppenheimova postkvantová teorie (π-fázový posun); nový framing „diskriminátor přístupů" živý.
- **2 eseje:** ESEJ-01 (dimenze jako otázka, probe/observer H2g-1) + ESEJ-02 (vesmír který se počítá, faktor 140 H2g-4, Everpresent Λ H2g-5).
- **BRAINSTORM-02.md** dokončen: 8 hypotéz druhé generace (H2g-1–H2g-8), výpočetní fronta 10 položek, strategický meta-závěr — kalibrace od „velké sjednocení" k „přesným diskriminátorům a falzifikacím".
- Vytvořen `core-data/calculations/` (4 adresáře s calc.py + results.json + plots).
- Aktualizován `knowledge-base/00-INDEX.md` (přidány sekce Výpočty, Hypotézní dossiery, Eseje, BRAINSTORM-02).

### 2026-06-06 (novelty check + oprava d_s rozporu)

- Novelty check 6 klastrů (arXiv/web) + oprava d_s datového rozporu v CST:
  - **d_s klastr (L3-1+L2-5+L5-5):** partially-known → reframe. Hořavův vzorec d_s=1+D/z znám od 2009; novum = jednotný P(s) formalizmus + probe jako třetí parametr d_s(z,D,probe).
  - **d_s datová oprava:** rozpor connections 657 vs. 1777 vyřešen — probe-dependence v CST potvrzena (Eichhorn-Mizera 1311.2530: náhodná procházka → d_s roste; Belenchia et al. 1507.00330: d'Alembertiánová sonda → d_s klesá k 2). Fragmenty causal-sets.json + noncommutative-geometry.json opraveny, registry přebudovány.
  - **a_4 klastr (L1-1+L2-4+L5-4):** partially-known → **pursue**. Dvoustranné mosty pokryty (2010–2013), trojstranná identifikace a_4 + anomaly-matching test pro C⊕H⊕M₃(C) nepublikovány.
  - **Λ klastr (L1-2+L3-2+L2-2):** partially-known → reframe. Tři pilíře zcela nezávisle publikovány; mezipilířový prefaktorový test neproveden ani navržen.
  - **Entropie klastr (L2-3+L3-4+L4-4):** partially-known → **pursue**. Dvoucestné mosty etablovány (2016–2025), trojcestná syntéza SSEE-truncation = crossed-product modular cutoff = LQG area gap chybí; γ jako renormalizační konstanta nepublikováno.
  - **Cardy-LQG (L1-3):** partially-known → reframe. Jádro c=6k + Cardy explicitně publikováno (Carlip 1410.5763); zbývají 2 body: γ↔c=6Q₁Q₅ analogie a CFT log-fixing γ~0.274. Priorita snížena.
  - **Preprint checks (L4-2, L4-5/L4-6, L5-3, L2-1):** partially-known → reframe. Basile et al. 2502.12290 mapují AS/swampland tension; FRG koeficient (L4-2) nový; citace L4-5 ověřeny (Nature 2025 + 3 arXivy); SJ pro Kerr/SdS nepokryto; NCG↔Liouville publikováno, trojstranné tvrzení nepublikováno.
- Vytvořen `core-data/novelty-checks.json` (6 klastrů + dsContradiction entry, pretty-printed).
- Aktualizován `BRAINSTORM-01.md` — přidána sekce "Novelty check (2026-06-06)" s tabulkou a komentáři.
- Přepracována sekce "Prioritní hypotézy" v PROGRESS.md (Tier 1 pursue: a_4 + entropie; Tier 2 reframe: d_s + Λ + preprints; Tier 3: Cardy-LQG).

### 2026-06-05
- Založena struktura knowledge base (README, struktura složek, jazyková politika).
- Spuštěno první velké workflow `qg-knowledge-foundation`:
  - 18 paralelních výzkumných agentů (pilíře: teorie strun, LQG, asymptotická bezpečnost, CDT, kauzální množiny, GFT, nekomutativní geometrie, twistory/amplitudy, emergentní gravitace, supergravitace/UV, holografie/AdS-CFT, černé díry/informační paradox, entanglement↔prostoročas, swampland, semiklasická gravitace, konceptuální problémy, fenomenologie, kvantová kosmologie)
  - adversariální verifikace citací a vzorců
  - konsolidace do jednotných registrů (graf konceptů, reference, vzorce, problémy, souvislosti)
  - syntéza: mapa vztahů + bílá místa
- Economy run (housekeeping agent):
  - Re-verifikace 5 pilířů (causal-sets, group-field-theory, twistors-amplitudes, emergent-gravity, experimental-tests): celkem 39 referencí zkontrolováno, 16 chyb opraveno, 14 zbývajících obav zdokumentováno.
  - Deterministická konsolidace (Python): concept-graph 598 uzlů/2319 hran, references 563, formulas 235, open-problems 145, connections 280 (112 barely explored).
  - Soudcovský průchod deduplikace: sloučeno 7 skupin konceptů (9 ID), 2 duplicitní open-problems páry.
  - Syntéza SYNTEZA.md dokončena (průřez 18 pilíři + matice prozkoumanosti).
  - První brainstorming hypotéz nenalezených souvislostí: BRAINSTORM-01.md (5 analytických čoček, 10+ hypotéz, priority pro Fázi 2).
  - Vygenerován 00-INDEX.md (anotovaný rejstřík celé báze).

## Statistiky

Stav po velké review část 1 (2026-06-06). Celkem načteno 19 fragmentů (pilíř 19 přidán v kole 3).

### Per-pillar počty

| Pilíř | Koncepty | Vzorce | Reference | Problémy | Souvislosti |
|---|---|---|---|---|---|
| asymptotic-safety | 32 | 11 | 36 | 7 | 17 |
| black-holes-information | 25 | 16 | 43 | 10 | 17 |
| causal-dynamical-triangulations | 31 | 13 | 32 | 8 | 18 |
| causal-sets | 34 | 12 | 29 | 8 | 15 |
| conceptual-problems | 44 | 12 | 45 | 10 | 17 |
| emergent-gravity | 28 | 11 | 29 | 8 | 13 |
| entanglement-spacetime | 38 | 15 | 41 | 8 | 16 |
| experimental-tests | 31 | 13 | 39 | 8 | 18 |
| group-field-theory | 26 | 12 | 30 | 8 | 12 |
| holography-adscft | 40 | 13 | 35 | 8 | 18 |
| loop-quantum-gravity | 38 | 12 | 35 | 7 | 14 |
| noncommutative-geometry | 34 | 15 | 32 | 7 | 15 |
| quantum-cosmology | 30 | 12 | 35 | 9 | 14 |
| semiclassical-gravity | 36 | 14 | 40 | 8 | 14 |
| string-theory | 47 | 17 | 32 | 8 | 17 |
| supergravity-uv | 26 | 14 | 30 | 8 | 16 |
| swampland | 18 | 12 | 36 | 8 | 16 |
| twistors-amplitudes | 32 | 12 | 34 | 8 | 14 |

### Registry (celkem)

| Registr | Počet |
|---|---|
| references.json | 563 unikátních (z 633 syrových) |
| references.bib | export téhož |
| formulas.json | 235 unikátních (z 236 syrových) |
| open-problems.json | 145 (+9 fuzzy near-dup kandidátů) |
| concept-graph.json | 598 uzlů, 2319 hran |
| connections.json | 280 hran, 112 barely explored |
| _review/concept-merge-candidates.json | 80 párů k posouzení |

**Top hubs grafu (po velké review část 1):** holographic-principle, generalized-entropy, bekenstein-hawking-entropy, spectral-dimension, modular-hamiltonian, page-curve, adscft-correspondence, hawking-radiation. Graf: **625 uzlů, 2476 hran** (stav po konsolidaci 2026-06-06, velké review část 1). Connections: **292 hran, 115 barely explored**. References: **587 unikátních**. Open-problems: **153** (+9 fuzzy). Formulas: **247 unikátních**.

**Sloučení konceptů (soudcovský průchod):** sloučeno 7 skupin (9 ID přesměrováno na kanonická): ryu-takayanagi→ryu-takayanagi-formula, holographic-error-correction+quantum-error-correction→holographic-quantum-error-correction, tensor-network-holography+tensor-networks→tensor-network, bousso-bound→covariant-entropy-bound, gravitational-decoherence→gravitationally-induced-decoherence, ads-cft-correspondence→adscft-correspondence, swampland-distance-conjecture→distance-conjecture; v open-problems sloučeny 2 duplicitní páry.

### Re-verifikace 5 pilířů (2026-06-05, economy run)

| Pilíř | Zkontrolováno ref. | Nalezeno chyb | Opraveno | Zbývající obavy |
|---|---|---|---|---|
| causal-sets | 10 | 3 | 3 | 2 |
| group-field-theory | 10 | 3 | 3 | 3 |
| twistors-amplitudes | 8 | 3 | 3 | 3 |
| emergent-gravity | 8 | 3 | 3 | 2 |
| experimental-tests | 8 | 4 | 4 | 4 |

Podrobnosti zbývajících obav viz log níže.

## Další kroky

Odvozeno z BRAINSTORM-05 + výsledků kol 8–10. **Kolo 10 uzavřelo**: H5g-3 VYVRÁCENA (rohová podčást vrstva B čistě 2D, codim-2 spoj neobnovuje koncentraci); H5g-1 PARCIÁLNÍ (4D dS signál přítomen, plná saturace vyžaduje N>2500 + sparse solver). **Lib proposals z kola 10 (calc22 `results.json`)**: migrovat do `lib/toe` — `sprinkle_wedge_box4d`, `bd_smeared_dalembertian_inverse` (smeared ε=0.6), `sj_state` rel_floor, `entropy.modular_kernel`, `viz.nl_vs_locus`. **Hlavní vstupní bod pro lidského autora: `papers/REVIZE-PRO-CLOVEKA.md`** — zde začít před externím sdílením čehokoli z projektu.

### Důsledky kola 8 pro drafty a through-line

**Draft-02 finality (calc17):** H4g-3 je vyvrácena — žádná druhá index-identita pro Λ neexistuje. Tím je uzavřeno poslední otevřené riziko draftu-02: identita −18/11 nepotřebuje Λ-sekci, protože a₀ a a₂ jsou cross-order a jejich poměr je dimenzionální. Draft-02 je vědecky kompletní a čeká pouze na lidskou re-derivaci a₄ koeficientů a citace-check (žádný nový výpočet není potřeba).

**Through-line — vrstva B (calc18):** H4g-1 je v 2D mechanisticky podpořena. Modulární kernel SJ stavu je geometricky lokální (boost/Bisognano-Wichmann) na slabu a stává se non-lokálním monotónně směrem k rohům diamantu (off-diag sklon −0.47 vs −0.094, f_nl gradient R²=0.989) — přesně tam kde VYPOCET-13 lokalizoval Hadamardovu anomálii. F-016 a F-021 se propojují mechanismem (ne jen korelací). Ve 4D sonda nereplikuje s link-maticí; doporučená cesta: BD d'Alembertián nebo větší N.

### Uzavřené / odstraněné položky

- ~~**C_KM(γ) konstantní člen** z ENP 1006.0634~~ — UZAVŘENO: Sen blocker potvrzený, H01 mrtvá, γ-fixace z CFT fyzikálně nemotivovaná.
- ~~**4D SSEE sprinkling p=3/4 predikce (naivní)**~~ — UZAVŘENO: VYPOCET-06 predikci vyvrátil; exponent p=3/4 jako magnitudový cutoff není robustní (ale N^{3/4} number-truncace jako crossed-product předpis PROŠLA — VYPOCET-16).
- ~~**Cardy-LQG (L1-3) jako živá hypotéza**~~ — UZAVŘENO: program dead.
- ~~**VYPOCET-14 ambiguita a=0.6**~~ — UZAVŘENO (VYPOCET-15): corr(S)=0.9992, ΔAIC=+3894, Model S rozhodující.
- ~~**BRAINSTORM-04 jako doporučený první krok**~~ — DOKONČENO (kolo 7).
- ~~**H4g-3 — fermionová indukce predikuje Λ (druhá index-identita)**~~ — UZAVŘENO (VYPOCET-17): vyvrácena; žádná druhá index-identity pro Λ; draft-02 Λ-riziko uzavřeno.
- ~~**H4g-1 2D sonda (slab vs. diamantový roh, modulární tok)**~~ — DOKONČENO (VYPOCET-18): podpořena 4/5, through-line mechanismus aktivní v 2D.

### Drafty čekající na lidskou revizi

> Kompletní přehled se checkboxy a příkazy pro re-run: **`papers/REVIZE-PRO-CLOVEKA.md`** — vstupní bod pro lidského autora; doporučené pořadí draft-02 → draft-04 → draft-01 → draft-03.

- **draft-01-sj-rotating-spacetimes v0.2** (`papers/draft-01-sj-rotating-spacetimes/`) — silné výsledky (VYPOCET-14+15, ΔAIC>3894), nejvíce otevřených bloků (~15–25 hod). **Blokující pro release:** (1) N→∞ studie s 30+ seeds; (2) analytické SJ pro strižený diamant; (3) BTZ dvou-bodová funkce; (4) verifikace citací PDF; (5) nezávislá re-derivace / re-run (gate §8 TODO.md).
- **draft-02-a4-fermionic-identity** (`papers/draft-02-a4-fermionic-identity/`) — vědecky uzavřen (VYPOCET-11 + VYPOCET-17), nejmenší draft (~4–8 hod revize). **Blokující pro release:** lidská re-derivace a₄, citace-check PDF Duff/Andrianov-Lizzi/Kurkov-Lizzi-Vassilevich, scheme-dependence ošetření.
- **draft-03-ds-classifier** (`papers/draft-03-ds-classifier/`) — nejkřehčí novelty argument (Calcagni program); D-konvence ambiguita (~10–18 hod). **Blokující:** obrana vůči „Calcagni přebalený" a „probe-trivialita" (viz TODO.md).
- **draft-04-type-transition-causal-sets** (`papers/draft-04-type-transition-causal-sets/`) — konkrétní technický audit (~12–20 hod). **Blokující pro release:** 8 lidských verifikačních bran (viz TODO.md); oprava placeholder a_err=0.776 (kritická — přepsán do mnoha polí); BD 4D replika (VYPOCET-20 parciální — 3/5, rohová cast k ověření); LQG-area-gap noha trojúhelníku označena jako otevřená.

### DOPORUČENÁ FRONTA (BRAINSTORM-04, kolo 7)

**Dva paralelní výpočty (top priority):**

1. **H4g-3 — a₀/a₂ moment → Λ (fermionová indukce predikuje kosmologickou konstantu)** — nejlevnější (hodiny, exaktní sympy, navazuje na VYPOCET-02/11); otevírá draft-04 kandidáta a uzavírá draft-02 Λ-sekci. Hledá se druhá index-identita, racionální fermion-počítací forma pro Λ_cc/M_Pl².
2. **H4g-1 — modulární tok: slab vs. diamantový roh (rohová non-Hadamardovost = selhání boost-flow)** — nejvyšší konceptuální výnos; spojuje F-015/F-016/F-011 do jednoho mechanismu; testuje through-line (vrstva B); falzifikace: slab-modulární-tok geometrický boost musí selhat přesně v rozích.

**Tier 1 — BRAINSTORM-04 hypotézy:**

- **H4g-1** (rohová non-Hadamardovost = místo selhání boost-flow) — medium-high confidence; nejvyšší konceptuální výnos.
- **H4g-4** (III→II přechod přežívá na 4D slabu, ne na diamantu) — **POTVRZENA VYPOCET-16 (3/3 proxy)** — nyní: 4D diamant kontrolní výpočet + more seeds.
- **H4g-3** (Λ z fermionové indukce přes f₀/a₀ moment) — medium confidence; nejlevnější; dny; otevírá draft-04.

**Tier 2 — entropy-cluster program v 4D:**

- **VYPOCET-17 — 4D diamant vN-type kontrola** (navazuje na VYPOCET-16): ověřit predikci H4g-4: modulární spektrum na 4D diamantu zůstane III₁ i po N^{3/4} truncaci (rohová koncentrace jako blokátor přechodu).
- **VYPOCET-18 — slab area law větší N** (navazuje na VYPOCET-13): S~L^2.00 pro N=3000–5000, 10+ seeds; upřesnit Hadamardovy sklony.
- **4D Teukolský výpočet SJ** (H2g-6) — B exponent predikce; týdny.

**Tier 3 — přeneseno z BRAINSTORM-02/03:**

- **Oppenheim π-fázový posun** (H2g-8) — dny.
- **Ω_Λ sky-patch variance + stochastický w(z)** (H2g-5) — DESI DR2 / SKAO; dny.
- **Swerves ↔ l_cs most** — faktor 140 záchrana/pohřeb (H2g-4); dny.
- **FRG global-charge koeficient** AS fixed point (L4-2); týdny.

### Novelty check (arXiv/web) — DOKONČENO (2026-06-06)

- [x] **d_s klastr** — partially-known; reframe; probe-dependence potvrzena (VYPOCET-01).
- [x] **a_4 klastr** — partially-known; pursue; trojstranná identifikace nepublikována; VYPOCET-02 hotov.
- [x] **Λ klastr** — partially-known; reframe; prefaktorový test proveden (VYPOCET-03, 140×).
- [x] **Entropie klastr** — partially-known; pursue; VYPOCET-04 hotov (2D, ρ^(−1/2)); VYPOCET-06 vyvrátil 4D p=3/4.
- [x] **Cardy-LQG** — UZAVŘENO jako mrtvá (rozhodující kolo 2026-06-06).
- [x] **Preprint checks (L4-2, L4-5/L4-6, L5-3, L2-1)** — citace ověřeny; SJ pro Kerr/SdS otevřené (VYPOCET-05 = 2D BTZ dokončen).

### Stálé položky

- Doplnit chybějící témata (kandidáti: twistorová gravitace, post-Newtoniánská QFT, analogová gravitace jako samostatný pilíř).
- Průběžná aktualizace referencí při každém novém arXiv průchodu.
- Zavřít 9 fuzzy near-dup kandidátů v `open-problems.json` + zbývající concept-merge páry (61 zamítnuto, 80 původních).
- ~~Opravit entropy-cluster.md ř. 66: ρ^(−1/4) → ρ^(−1/2) (dle VYPOCET-04).~~ — Zaznamenáno; provést při příštím editačním průchodu.
- Zvážit Bianchi arXiv:1204.5122 (γ=i, γ-závislost mizí) jako okrajovou reziduální stopu po H01 closure.
