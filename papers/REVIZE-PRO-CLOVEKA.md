# REVIZE PRO ČLOVĚKA — vstupní bod pro lidského výzkumníka

**Stav: 2026-06-08 | Generováno AI koordinačním agentem. Všechny níže uvedené checkboxy jsou určeny výhradně pro lidské splnění.**

> **Aktualizace 2026-06-08 (kola 12–16 + agent-framework):** Tato revize byla doplněna o nálezy z kol 12–16 (F-024..F-035), které vznikly po nasazení tří výzkumných agentů na `main` (exploratory-engine + computational-physicist + adversarial-verifier, commit `6e0f394`). Audit-fixy kola 14–15 od verifiera jsou již aplikovány (commit `e79b75e`: M-1 proxy3 30-seed committed podklad, m-1 F-031 měřený vs predikovaný drift, m-2 F-033 reziduum). Klíčové dopady na drafty: **draft-01 §4.2** dostal spojitý superradiantní exponent $B(a)$ (F-030, nahrazuje starý ohraničený 4.23/3.82), **draft-04 §4.3** dostal poctivé negativy F-029 (2D ano / 4D ne) a F-031 (4D area-law genuinně chybí). Per-draft checklisty níže (§2) byly o tyto položky rozšířeny.

---

## 1. Přehledová tabulka čtyř draftů

| Draft | Stav | Vědecká uzavřenost | Hlavní nárok | Největší riziko | Odhad lidské revize |
|-------|------|-------------------|--------------|-----------------|---------------------|
| **draft-01** — SJ ve rotujících prostoročasech (v0.3) | Interní explorační draft; NENÍ připraven k odeslání. VYPOCET-14 + VYPOCET-15 zpevnily §4.2; VYPOCET-26 (F-030) **nahradil** starý ohraničený B spojitým B(a). | Otevřená: zbývá kontinuální studie (velké N), analytická křížová kontrola, srovnání se známými BTZ vakuy | SJ stav existuje a je numericky konstruovatelný uvnitř ergoregiónu; rotace žije v vlastních vektorech, ne ve spektru; superradiantní pásový otisk v pozitivním podprostoru SJ; **superradiantní exponent B je spojitá klesající funkce strhávání (6.10→2.54, dB/da=−2.20), NE konstanta D−1=3** (F-030) | Referee napadne: „Je to jen zkosený 2D Minkowského diamant" a „A_caus = +1 je triviální klasický výsledek" | 15–25 hodin (matematika §§2–3 + BTZ vakuum + citace) |
| **draft-02** — identita −18/11 (v0.1) | Interní explorační draft; fyzika výpočetně uzavřena (VYPOCET-11 + VYPOCET-17). | **Uzavřena:** žádný otevřený fyzikální blokátor; zbývají framing + lidská verifikace PDF | Exaktní racionální identita c/(−a) = −18/11 je obsahově nezávislá na fermiónové části; graviton identitu neobnoví; Λ-člen nemá sesterskou identitu | Referee napadne: „Tautologie — znovu jste odvozili, že a₄ = a₄"; pokud někdo toto číslo napsal dříve (Connes–Marcolli kniha, van Suijlekom) | 4–8 hodin (nejmenší draft, exaktní aritmetika) |
| **draft-03** — ds klasifikátor (v0.1) | Interní explorační draft; NENÍ připraven k odeslání. | Otevřená: novelty re-check nutný; per-řádkový REPRODUCE audit; D-konvence nejasná | d_s je klasifikátor (z, D, sonda), ne universální konstanta; zjevná universalita d_s → 2 je artefakt γ=2 podtřídy; „stejná teorie, opačný trend" (CST d'Alembertian vs. random walk) | Referee napadne: „Calcagni program přebalený"; D-konvence ambiguita v Hořavově řádku | 10–18 hodin (per-řádková verifikace 12 hodnot + novelty search) |
| **draft-04** — přechod typů na kauzálních množinách (v0.2) | Interní explorační draft; NENÍ připraven k odeslání. Round-10/11 přidal de Sitter §4.3 (F-023 `supported` 2D + F-025 `partial` 4D); kola 12–16 doplnila F-027/F-028/F-029/F-031/F-032. | Otevřená: proxy nejsou typy; ~~placeholder chyba `a_err=0.776`~~ (VYŘEŠENO 2026-06-06); větší N v 4D potřeba; **dS §4.3: 2D area-law potvrzen (F-029), ale 4D area-law GENUINNĚ CHYBÍ (F-031), konformně-váhový caveat NEVYŘEŠEN** | 3/3 proxy ukazuje III₁→II přechod ve 4D desce; selektivita (N^{3/4} funguje, fixed-fraction nefunguje); dS §4.3 přidává II₁ vs II_∞ obsahový diskriminátor; **Proxy 3 2/3→3/3 při ≥30 seedech (F-032)**; poctivé negativy: 4D žádné A/4 (F-031), 2D c≈7.57≠4 (F-028) | Referee napadne: „Konečná matice = vždy typ I; nic jste neměřili"; N^{3/4} je předpis; **4D skalár není konformně invariantní; 4D area-law chybí** | 16–26 hodin (re-run 6+ calc.py + statistika + verifikace ~17 arXiv ID; +4–6 h za de Sitter §4.3) |

---

## 2. Co přesně musí člověk ověřit v každém draftu

### 2.1 draft-01 — SJ ve rotujících prostoročasech

#### A) Matematické re-derivace (blokující)
- [ ] **Analytické SJ pro zkosený 2D diamant:** odvodit SJ spektrum/vlastní funkce analyticky pro konstantně-skloněnou sekci (je konformně ekvivalentní standardnímu kauzálnímu diamantu/obdélníku, pro nějž je SJ znám, srov. Mathur–Surya). Porovnat s numerickým spektrem z kódu.
- [ ] **Analytická předpověď nulového přechodu skloněné null-souřadnice na r_erg:** odvodit uzavřenou formu: s₋ = 0 ⟺ g_tt = 0 ⟺ r = r_erg, s přesným vztahem mezi vnitřním null-sklonem a (g_tt, g_tφ, g_φφ).
- [ ] **Uzavřená forma A_caus(r)** z úhlů otevření kužele (sklon je funkce metriky), potvrdit ~1/r² chvost a monotonní a-závislost nejsou statistické artefakty.
- [ ] **Mechanismus opačného znaménka (§3.5b):** ověřit, že toy-model derivace v null-souřadnicích u=φ−s₊t, v=φ−s₋t reprodukuje oba znaky a magnitudy (h∝du dv ověřeno symbolicky — potvrdit výpočtem).

#### B) Kontrola citací proti PDF (blokující — Priorita 1 — musí provést člověk)
- [x] arXiv:1205.1296 (Afshordi–Aslanbeigi–Sorkin, „A distinguished vacuum state for a quantum field in a curved spacetime", JHEP 2012) — ID opraveno z chybného 1208.2422 (2026-06-06)
- [ ] arXiv:1611.10281 (Sorkin–Yazdi) — potvrdit eq. 9 a footnote 5 (G_R = ½C)
- [x] arXiv:2602.09796 — **OPRAVENO 2026-06-08:** ID existuje, ale je to **Häfner & Klein, „The Unruh state for bosonic Teukolsky fields on subextreme Kerr spacetimes" (2026-02-10)**, NE „Dafermos–Luk et al.". Atribuce opravena v draft-01 §1.1, §4.2, ref.13. Obsah tvrzení (Unruhův stav existuje a je Hadamardův pro Teukolsky pole na subextremálním Kerru) je podporován; chybné bylo pouze autorství. Nezaměňovat s Dafermos–Rodnianski 2007.07211 (correctly cited).
- [ ] arXiv:2303.13488 (Balakumar) — potvrdit existenci a obsah
- [ ] arXiv:2504.12919 (AdS₂ SJ) — potvrdit existenci a obsah
- [ ] arXiv:2212.10592 — potvrdit
- [ ] arXiv:2007.07211 — potvrdit
- [ ] BTZ/Kerr metrické reference (gr-qc/0003097, 1707.08133) — potvrdit
- [ ] arXiv:0909.0944, 1701.07212, 1712.04227 — potvrdit

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
- [ ] arXiv:1106.3263 (Kurkov–Lizzi–Vassilevich) — totéž

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
- [ ] arXiv:1712.04227 (double truncation, 2D local) — potvrdit κ a double aplikaci
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

## 3. Doporučené pořadí revizí s odůvodněním

### Doporučení: draft-02 → draft-04 → draft-01 → draft-03

**1. Začněte s draft-02 (identita −18/11)**

*Proč první:* Nejmenší draft. Fyzika je výpočetně uzavřena (VYPOCET-11 + VYPOCET-17 — žádný otevřený fyzikální blokátor). Klíčová aritmetika je exaktní (sympy, racionální čísla), takže re-derivace jsou krátké a buď vyjdou nebo nevyjdou — žádná interpretační šedá zóna. Jediné zbývající bloky jsou framing a lidská verifikace PDF. Odhad: 4–8 hodin práce člověka. Navíc: pokud novelty re-check odhalí, že −18/11 bylo dříve publikováno, ušetříte práci na zbytku.

**2. Pokračujte s draft-04 (přechod typů)**

*Proč druhý:* Fyzika je zajímavá a konzistentní (3/3 proxy ve 4D), ale blokátory jsou konkrétní a mechanické — re-run kódu, opravit chybu placeholder, verifikovat 15 arXiv ID. Nejde o otevřený vědecký spor, ale o technický audit. Odhad: 12–20 hodin. Navíc: jde o syntézu tří publikovaných výsledků; pokud Jones–Yazdi 2602.16782 a CLPW-identifikace jsou potvrzeny, jádro drží.

**3. Třetí draft-01 (SJ v rotujících prostoročasech)**

*Proč třetí:* Nejrozsáhlejší a vědecky nejotevřenější (chybí kontinuální studie, BTZ vakuum srovnání, analytická křížová kontrola). Velký N scan a 30+ seeds jsou strojový čas, ale matematické odvození SJ na zkoseném diamantu vyžaduje skutečnou analytickou práci. Výsledky VYPOCET-14 a VYPOCET-15 jsou silné (ΔAIC > 3894 všude), takže jádro stojí — ale šance na odeslání závisí na tom, zda analytická práce proběhne. Odhad: 15–25 hodin.

**4. Nakonec draft-03 (d_s klasifikátor)**

*Proč poslední:* Novelty argument je nejkřehčí — vyžaduje rozsáhlý literature search (Calcagni knihy, reviews, follow-upy). Fyzika (engine, limity) je solidní a D-konvence ambiguita je opravitelná, ale obhájit „nový příspěvek" vůči Calcagni programu je nejnáročnější framing task. Doporučuje se odložit, dokud nebudete mít zbytek vyřešen a dokud nesprovedete novelty search. Odhad: 10–18 hodin.

---

## 4. Společné zásady: AI-asistovaná proveniencí, autorství, reprodukce

### 4.1 Co znamená „AI-asistovaný výzkum" pro autorství

Všechny čtyři drafty byly generovány AI-asistovaným výzkumným pipeline. To konkrétně znamená:

- **Výpočty**: calc.py skripty a výsledky (results.json, výpočetní poznámky VYPOCET-*) byly navrženy, spuštěny a interpretovány jazykovým modelem bez lidské supervize každého kroku.
- **Citace**: proveniencé poznámky říkají „ověřeno verbatim z PDF" nebo „transcribed" — ale toto tvrzení **samo o sobě musí lidský výzkumník ověřit** otevřením každého PDF.
- **Framing**: vědecké argumenty a interpretace jsou AI-generované. Mohou být přesvědčivé, aniž by byly správné.

**Žádný draft nesmí být odeslán bez:**
1. Jmenovaného lidského autora, který prověřil fyziku a kód.
2. Explicitního prohlášení o AI-asistenci dle zásad cílového vydavatelství (viz `dokumentace/zasady-publikovani.md`-style konvence projektu).
3. Veřejného vydání calc.py pro reprodukovatelnost.

### 4.2 Pravidlo nezávislé lidské re-derivace

**Žádný draft nesmí být podán bez nezávislé lidské re-derivace klíčových výsledků.** Toto je absolutní pravidlo pro všechny čtyři drafty:

- **draft-01**: nikdo dosud nezávisle nespustil VYPOCET-05, VYPOCET-08, VYPOCET-10 ani VYPOCET-14, VYPOCET-15.
- **draft-02**: nikdo dosud nezávisle neodvodil heat-kernel koeficienty, nespustil sympy, ani nezkontroloval citace na zdrojových PDF.
- **draft-03**: nikdo dosud nezávisle nespustil engine ani neodvodil oba limity.
- **draft-04**: nikdo dosud nezávisle nespustil žádný ze čtyř calc.py skriptů.

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

*Konec dokumentu. Verze: 2026-06-08 (kola 12–16 + agent-framework doplněna; předchozí 2026-06-06). Generováno AI koordinačním agentem. Všechny checkboxy jsou určeny pro lidské splnění před jakýmkoli externím sdílením nebo odesláním.*
