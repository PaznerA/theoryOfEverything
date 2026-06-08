# VYPOCET-25: Škálovaná GitHub-Actions compute-kampaň — dS entropický strop ve 2D a 4D (H5g-1 / H5g-2 at scale)

**Datum:** 2026-06-08
**Status:** Dokončeno (syntéza; část compute-omezena, viz limity)
**Navazuje:** VYPOCET-23 / F-028 (2D dS strop → kvantitativní area-zákon, R=0.1321, c=7.57), VYPOCET-21 / F-025 (4D dS truncovaná area-law SSEE, H5g-1 PARTIAL), VYPOCET-19 / F-023 (2D dS II₁ vs II_∞)
**Hypotézy:** H5g-1 (4D truncovaná area-law SSEE odděluje typ sama), H5g-2 (dS strop = kvantitativní A/4-podobný zákon, je konstanta dimenzně-nezávislá?)
**Cluster:** entropy-cluster × von-Neumann II₁ × horizon-SJ × causal-set first-principles × dimension-dependence

**Datové artefakty (staged cloud, linux/x86_64 GH Actions):**
- `compute/results-archive/ds_entropy_cap_2d-rho30k.json` (2D R, ρ 240–1200 dosaženo, ρ 3000/30000 null/timeout)
- `compute/results-archive/ds_cap_4d-grid.json` (4D mřížka, ρ 60–960 × ℓ 0.8–1.5, 6 seedů, mnoho low-R² buněk)
- `compute/results-archive/ds_cap_4d-highN.json` (4D follow-up, ρ 960/1920, N až 6144 — rozhodující high-N)
- `compute/results-archive/ds4d_saturation-rho120.json` (4D F-025 saturace, ρ=120 hotovo, 600/2000 vynecháno)
- Figura: `core-data/calculations/ds-entropy-cap/plots/R_2d_vs_4d.png` (skript `plot_R_2d_vs_4d.py` tamtéž)

---

## Motivace a sázka

VYPOCET-23 (F-028) commitnul **2D** výsledek na úzkém rozsahu: poměr R = S_full_cap / A_mol je konstantní (R=0.1321, CV 1.3 %, c=1/R=7.57) přes ρ ∈ {240,600,1200} a ℓ ∈ {0.7,1.0,1.5}. To je povýšení kvalitativní saturace II₁ na kvantitativní area-zákon, ovšem **NE** doslovnou čtvrtinu. Otevřené otázky pro škálování:

1. **Drží 2D konstanta R na ŠIRŠÍM rozsahu?** (vyšší ρ, větší ℓ až 2.5)
2. **Je koeficient c dimenzně-nezávislý?** Tj. dá 4D ve stejné konvenci stejnou (nebo aspoň konstantní) R, nebo R **driftuje** s ρ? Pokud driftuje, je to konvence, aproximace, nebo genuinní fyzika? — toto je jádro této kampaně.
3. **Dosáhne 4D F-025 truncovaná SSEE plné saturace** při vyšší ρ, kterou VYPOCET-21 (PARTIAL) nedosáhl při N≤2500?

Kampaň běžela jako rounds na GH Actions (linux/x86_64), aby se škálovalo přes dense-eigh zeď, kterou macOS lokál nedosáhl. Antikruhovost (ε ~ ρ^(−1/d) FIXOVÁNO z F-006 **před** poměrem) zachována ze VYPOCET-23: 2D ε=ρ^(−1/2), 4D ε=ρ^(−1/4) (F-006 p=0.519±0.007, lift na d=4).

---

## Nález 1 — 2D R konstantní: POTVRZENO a ROZŠÍŘENO

`ds_entropy_cap_2d-rho30k.json`, validní (dense) buňky. R = S_full_cap / A_mol (Dou-Sorkin molekulová „plocha", gr-qc/0302009). Konvence F-028: 2D horizont = bod (kodim-2 v 2D = 0-dim), A_mol je počet ireducibilních linků křižujících fixní řez r*=0.8, ε-nezávislý.

| ρ | ℓ | S_full_cap | A_mol | **R** | c=1/R | S_full_cap_R² |
|---|---|---|---|---|---|---|
| 240 | 0.7 | 23.53 | 192.7 | **0.12210** | 8.19 | 0.63 |
| 240 | 1.0 | 45.50 | 360.6 | **0.12620** | 7.92 | 0.68 |
| 240 | 1.5 | 69.52 | 525.1 | **0.13240** | 7.55 | 0.96 |
| 240 | 2.5 | 89.10 | 665.9 | **0.13379** | 7.47 | 0.93 |
| 600 | 0.7 | 64.31 | 503.8 | **0.12765** | 7.83 | 0.78 |
| 600 | 1.0 | 122.30 | 931.6 | **0.13129** | 7.62 | 0.87 |
| 600 | 1.5 | 183.72 | 1367.9 | **0.13431** | 7.45 | 0.97 |
| 600 | 2.5 | 232.88 | 1750.2 | **0.13306** | 7.52 | 0.97 |
| 1200 | 0.7 | 132.22 | 1037.7 | **0.12742** | 7.85 | 0.71 |
| 1200 | 1.0 | 250.83 | 1925.1 | **0.13030** | 7.67 | 0.98 |

**Statistika přes 10 validních buněk:** R̄ = **0.12985 ± 0.00392 (CV 3.02 %)**, R ∈ [0.12210, 0.13431]; c = 1/R̄ = **7.70**. Drift d ln R / d ln ρ = **+0.0068 ± 0.0164** (slučitelné s 0).

**Vztah ke commitnutému F-028 (R=0.1321, CV 1.3 %, c=7.57):** souhlasí v rámci CV. Mírně nižší střední hodnota (0.1299 vs 0.1321) a vyšší CV (3.0 % vs 1.3 %) jsou důsledkem **rozšíření na ℓ=2.5 a na nejmenší ℓ=0.7** — ℓ=0.7 buňky systematicky leží na spodním okraji (R≈0.122–0.127, viz tabulka), což je nejmenší-záplata cutoff-efekt (méně bodů, S_full_cap_R² jen ~0.63–0.78). Při ℓ≥1.0 je R̄ = 0.1316 (CV 1.6 %), prakticky shodné s F-028. **Závěr: 2D konstanta R drží přes ROZŠÍŘENÝ rozsah ρ 240→1200 (5×) a ℓ 0.7→2.5 (3.6×); drift v ρ je nula.** To je publikovatelně silný výsledek (viz draft-04 sekce níže).

**Co NEDOběhlo (poctivě):** vysokohustotní cíle kampaně padly na timeout. Buňky ρ=1200 (ℓ=1.5, 2.5), ρ=3000 (ℓ=0.7, 1.0, 1.5) a celý plánovaný ρ=30000 blok jsou v JSON přítomny jako `path=sparse` s `S_full_cap = null`, `R = null`. Důvod: S_full je vnitřně **dense** (objemový zákon přes všech ~N modů; top-k sparse eigsh zachytí jen mody nad κ a NEreprezentuje S_full). Sparse cesta proto poskytla jen S_trunc_cap (O(1), konzistentní: ρ=3000/ℓ=1.5 → S_trunc=1.04), ale ne primární poměr R. `status: partial-time-budget`, runtime 17 321 s ≈ 4.8 h (timeout na max_hours=5.5 dosažen dříve, než doběhl dense S_full pro ρ≥1200/ℓ≥1.5). **R je tedy potvrzeno do ρ=1200, ne výš.**

---

## Nález 2 — 4D c NENÍ konstantní: v této konvenci dimenzně-závislý drift

`ds_cap_4d-grid.json` + `ds_cap_4d-highN.json`. **Klíčový kontrast vůči 2D.** Tabulka c^4D vs ρ při FIXNÍ velikosti záplaty ℓ=0.8 (nejčistší sloupec — drží ℓ, takže izoluje ρ-drift; high-N body z follow-up runu):

| ρ | S_full_cap | A_mol (raw) | ε=ρ^(−1/4) | **R^4D** | **c^4D=1/R** | S_full_cap_R² |
|---|---|---|---|---|---|---|
| 60 | 7.20 | 40.3 | 0.359 | 0.17879 | **5.59** | 0.54 (low) |
| 120 | 17.54 | 154.7 | 0.302 | 0.11337 | **8.82** | 0.61 |
| 240 | 36.57 | 560.9 | 0.254 | 0.06521 | **15.34** | 0.98 |
| 480 | 70.85 | 1883.7 | 0.214 | 0.03761 | **26.59** | 0.28 (low) |
| 960 | 140.60 | 5719.4 | 0.180 | 0.02458 | **40.68** | 0.25 (low) |
| 1920 | 292.08 | 19232.8 | 0.151 | 0.01519 | **65.85** | 0.77 |

**c^4D roste monotónně 5.6 → 66 (≈12×) přes ρ 60 → 1920 (32×).** R^4D = S_full_cap/A_mol **driftuje** s exponentem (fixní ℓ=0.8, n=6):

$$\frac{d\ln R^{4D}}{d\ln\rho} = -0.72 \pm 0.01.$$

(High-N summary blok hlásí −0.52 ± 0.30 z 3-bodového fitu, ale ten **míchá ℓ** — buňky (960,ℓ0.8), (960,ℓ1.0), (1920,ℓ0.8). Čistý fixní-ℓ=0.8 fit dá −0.72; pooled-přes-ℓ čisté buňky dají −0.77 ± 0.10. Oba jsou výrazně nenulové a vzdálené od nuly.)

**`R_full_4D_constant: false`, `c_is_dimension_dependent: true`** v obou JSON summary. To je tvrdý kontrast vůči 2D (Nález 1: drift +0.007, nula).

### Fit-kvalita — poctivé varování o low-R² buňkách

Mřížka `ds_cap_4d-grid.json` obsahuje **mnoho katastrofálně rozbitých S_full_cap fitů**. S_full_cap je saturující extrapolace přes 6 box-kroků; když per-box S_full data nejsou monotónní, fit vyplivne nesmyslnou hodnotu. Buňky vyřazené (R<0 nebo R>1 nebo S_full_cap_R²<0.40):

| ρ | ℓ | S_full_cap | R | flag |
|---|---|---|---|---|
| 60 | 1.0 | −2039.08 | −23.6 | rozbitý fit (R²=0.02) |
| 60 | 1.5 | +5090.38 | +25.7 | rozbitý fit (R²=0.11) |
| 120 | 1.0 | −16321.05 | −51.3 | rozbitý fit (R²=0.61, ale R<0) |
| 240 | 1.0 | +7113.58 | +6.44 | rozbitý fit (R²=0.25) |
| 480 | 0.8 | 70.85 | 0.0376 | R OK, ale R²=0.28 |
| 960 | 0.8/1.0 | 140.6/217.5 | 0.025/0.019 | R OK, ale R²=0.25 |

**Proč summary R_full_4D_mean = −3.52 (CV 524 %) v grid JSON je nesmysl:** zprůměroval přes rozbité buňky včetně −51 a +25. **NEpoužíváme ho.** Spolehlivý drift se čte jen z fyzikálně smysluplných buněk (R ∈ (0,1)), kterých je 6 (fixní-ℓ=0.8 sloupec + dvě 480 buňky + 1920). Tyto všechny dávají monotónní R↓ s ρ. Hodnota S_full_cap **sama** přitom škáluje čistě jako ρ^1.05 i v low-R² buňkách (low-R² je proto, že S_full skoro-plató, na které saturující fit špatně sedí — ne proto, že by hodnota byla šum; viz Nález 2c diskriminátor). Figura `R_2d_vs_4d.png` rozlišuje plné (R²≥0.70) vs prázdné (marginální 0.40–0.70) 4D markery.

### Interpretace driftu — TŘI konkurenční vysvětlení

Drift R^4D ~ ρ^(−0.72) je reálný. Co ho způsobuje? Tři hypotézy a diskriminátor mezi nimi:

**(a) DISKRÉTNĚ-PLOŠNÁ KONVENCE (převažující, ale s POCTIVOU korekcí oproti původní formulaci).**
Argument: 2D horizont = bod (kodim-2 v 2D = 0-dim), molekulový počet **A_mol ~ ρ^1** — sleduje refinement jako objem. 4D horizont = kodim-2 **plocha** (2-rozměrná), jejíž molekulový počet měl podle naivního počítání růst pomaleji. Původní hypotéza kampaně zněla: A_mol ~ ρ^(1/2), takže drift ρ^(−1/2) je ~přesně inverze tohoto růstu a S_full_cap by byl ρ-NEZÁVISLÝ.

> **Data tuto naivní formu VYVRACEJÍ — a je nutné to říct rovně.** Měřeno (fixní ℓ, ireducibilní linky piercing fixní kodim-2 plochu E={r*=R_CUT}):
> - **A_mol(raw) ~ ρ^(+1.77 ± 0.03)** (konzistentně přes ℓ=0.8/1.0/1.5: exponenty 1.768, 1.753, 1.755), **NE ρ^(1/2)**.
> - **S_full_cap ~ ρ^(+1.05 ± 0.03)** (objemový zákon, stejně jako 2D), **NEsaturuje** na ρ-nezávislou konstantu.
> - Drift R = S_full/A_mol = ρ^(1.05−1.77) = **ρ^(−0.72)**, přesně součet exponentů.
>
> Tedy: drift NENÍ ρ^(−1/2) a NENÍ to inverze růstu A_mol ~ ρ^(1/2). **Skutečná verze (a):** 4D kodim-2 piercing-link počet škáluje **rychleji** (ρ^1.77), než objemová S_full (ρ^1.05), takže poměr klesá. Co je ε-konvenční artefakt: A_mol je hlášen jako raw link count; spojitá „plocha" A_cont = A_mol·ε² = A_mol·ρ^(−1/2) ~ ρ^(1.27). I A_cont roste rychleji než S_full (ρ^1.05), takže drift Sf/A_cont ~ ρ^(−0.22). **Ani ε-renormalizovaná plocha drift neodstraní.** Závěr (a): jádro je, že v 4D molekulový počet kodim-2 plochy a obsah-entropie **NEškálují stejně** (na rozdíl od 2D, kde oba ~ρ^1), takže R není konstanta. Toto zůstává **vedoucí vysvětlení** — drift je deterministicky vysvětlen rozdílem dvou škálovacích exponentů — ale konkrétní číslo ρ^(−1/2) z prompt-hypotézy **data nepotvrzují**; je to ρ^(−0.72) (raw) resp. ρ^(−0.22) (ε-cont).

**(b) KONFORMNĚ-VÁHOVÝ CAVEAT (aproximace, ne fyzika).**
4D bezhmotný skalár NENÍ konformně invariantní (na rozdíl od 2D). Náš objekt = plochá kauzální struktura v (t,r*,x₁,x₂) + vlastní dS sech²-míra + Johnston link-Greenova fce (0909.0944) — je **řízená aproximace** VYPOCET-21, ne přesný dS Wightmanův stav. Drift by mohl být tato aproximace, ne fyzika. **Co by (b) odlišilo od (a):** kdyby drift mizel s lepším (zakřiveným) propagátorem při fixní geometrii. To naše data **netestují** (nemáme přesný 4D dS propagátor v repu). Caveat zůstává otevřený a musí být v jakémkoli draftu uveden.

**(c) GENUINNÍ DIMENZNÍ ZÁVISLOST koeficientu entropie-plocha.**
Možná je c skutečně dimenzně-závislé a 4D prostě nemá ρ-invariantní area-konstantu. To by znamenalo, že entropie-na-molekulu není v causal-setu dimenzní invariant.

**Diskriminátor mezi (a) a (c): saturuje S_full_cap SÁM (ne poměr) na ρ-nezávislou konstantu?**
- Pokud **ano** (S_full → konst), pak drift R je čistě růstem A_mol → konvence/diskrétnost (a).
- Pokud **ne** (S_full roste s ρ), pak S_full je objemová a poměr s libovolně-škálující „plochou" musí driftovat → buď (a) v korigované formě (dvě různá škálování), nebo (c).

> **Měření: S_full_cap NEsaturuje. Roste jako ρ^(+1.05)** (7.2 → 292 přes ρ 60→1920). To **VYVRACÍ původní formu (a)** (která tvrdila S_full ρ-nezávislé) a posouvá interpretaci k **hybridu (a)-jako-konvence + (c)**: S_full je objemová (ρ^1, jako 2D), ale 4D kodim-2 molekulová „plocha" škáluje ρ^1.77 (NE jako 2D ρ^1), takže poměr nutně driftuje. To NENÍ čistě „diskrétnost maskuje fyziku" (a v naivní formě); je to **reálný rozdíl škálovacích zákonů obsahu a kodim-2 plochy mezi 2D a 4D**. Zda je ten rozdíl konvenční (jiná definice 4D molekulové plochy by ho zrušila) nebo genuinní (c), zůstává **nerozhodnuto** — vyžaduje to nezávislou kalibraci 4D Dou-Sorkinova koeficientu, kterou repo nemá.

**Poctivý součet Nálezu 2:** c^4D roste 5.6→66; R^4D driftuje ρ^(−0.72); v této konvenci **NENÍ čistá 4D area-konstanta**. To přímo oslabuje jakýkoli „4D A/4" claim (viz draft sekce).

---

## Nález 3 — F-025 4D saturace: ρ=120 čistě, vyšší ρ compute-bound

`ds4d_saturation-rho120.json`. Diskriminátor H5g-1: truncovaná SSEE (n_max=2N^(3/4), F-019) na dS vs shodné ploché kontrole, řez roste k horizontu.

| veličina (ρ=120, ℓ=1.0, 4 seedy) | de Sitter | plochá kontrola |
|---|---|---|
| S_trunc průběh (R*_box 1.6→5.2) | 32.8 → 42.4 | 41.5 → 80.6 |
| cap (saturující fit) | 43.59 | 145.61 |
| full slope | +2.38 | +11.27 |
| late slope | **+2.36** | +8.15 |
| saturující fit R² | 0.88 | 0.99 |
| AIC vítěz | **saturující** | lineární |

**Výsledek:** `dS_truncS_saturates: true`, `flat_truncS_grows: true`, `H5g1_4D_clean_saturation: true`. AIC jednoznačně preferuje saturující model pro dS a lineární pro plochou; full-slope poměr flat/dS = 11.27/2.38 = **4.7×** (silnější separace než VYPOCET-21 poměr 2.96). To je **čistší separace, než dal VYPOCET-21** (PARTIAL).

**Poctivá kvalifikace:** „clean saturation" je verdikt AIC (saturující > lineární), ALE dS late-slope je stále **+2.36, ne literálně 0** — truncovaná dS SSEE pořád mírně stoupá, jen ~3.5× pomaleji než plochá. „Čistá" tedy znamená „AIC-rozlišená", ne „plató s nulovým sklonem". Konzistentní s VYPOCET-21 mechanismem (rostoucí řez při fixní ρ stále přidává dS body). max_N=2496, `dense_wall_lifted: false`.

**Limit (rovně, NE výsledek):** plánované potvrzení při ρ=600 a ρ=2000 **NEDOBĚHLO**. JSON má jen 1 buňku (ρ=120); `status: partial-time-budget`, runtime jen 181 s — run **spadl/skončil dříve, než spustil vyšší-ρ buňky** (per-cell checkpoint zapsal ρ=120 a max-hours/driver-bug ho ukončil před ρ=600). **Vyšší-ρ potvrzení saturace tedy NEEXISTUJE** v této kampani. H5g-1 zůstává na úrovni VYPOCET-21 (PARTIAL→jedna čistá ρ=120 buňka navíc), NE povýšeno na STRONG.

---

## Nález 4 — Cross-HW konzistence

Všechny čtyři artefakty běžely na **linux/x86_64 (Azure GH Actions runner, glibc2.39, Python 3.13.13, numpy 2.4.4, scipy 1.17.1, OMP_NUM_THREADS=4)**. Commitnuté F-028 hodnoty (VYPOCET-23) pochází z macOS. **Překryv:** 2D buňky ρ=240/600/1200 × ℓ=0.7/1.0/1.5 jsou v obou. Linux R̄(ℓ≥1.0)=0.1316 (CV 1.6 %) vs macOS commit 0.1321 (CV 1.3 %) — **shoda v rámci CV**. Žádný HW-závislý posun; ±-párovací invariant i∆ na linuxu < 1.3e-14 (dense float64) na každé buňce, totožně jako macOS. Cross-HW reprodukovatelnost 2D R je tedy potvrzena.

---

## Compute limitations (poctivá sekce — lekce pro drivery)

Tato kampaň měla rozhodnout 2D vysokou-ρ a 4D saturaci. **Vysokohustotní cíle systematicky nedoběhly** a stojí za to zaznamenat proč, protože to je opakující se vzorec:

- **2D (`ds_entropy_cap_2d-rho30k.json`):** runtime 17 321 s (4.81 h), `partial-time-budget`. ρ≥1200/ℓ≥1.5 a celé ρ=3000/30000 → `null` (S_full je dense-only, sparse eigsh nereprezentuje objemový zákon). R potvrzeno do ρ=1200.
- **4D grid (`ds_cap_4d-grid.json`):** runtime 3786 s, `complete`, ale ρ=960 (ℓ=0.8/1.0/1.5) `skipped` — N_max 3072–5749 > n_max_cap 3000 (4D dense-eigh zeď; **chybí 4D sparse primitiv**). Mnoho ℓ=1.0/1.5 buněk při nižší ρ má rozbité S_full_cap fity.
- **4D high-N (`ds_cap_4d-highN.json`):** runtime 19 873 s (5.52 h!), `partial-time-budget`. Doběhly jen 3 buňky ((960,0.8),(960,1.0),(1920,0.8)); plánované (1920,1.0) nedoběhlo. Tj. **6h cloud run vyprodukoval 3 buňky.**
- **4D saturace (`ds4d_saturation-rho120.json`):** runtime 181 s, `partial-time-budget`, jen 1 buňka. Driver zapsal ρ=120 checkpoint a skončil **před** ρ=600/2000.

**Vzorec a lekce:** per-cell checkpoint + **nevynucený** max-hours znamenal, že **dva ~6h cloud runy (highN 5.5 h, 2D 4.8 h) a dva ~5h lokální runy (mirror) vyprodukovaly ZERO vyšší-ρ saturačních buněk** nad ρ=120/1200. Když je per-cell náklad ~N³ (dense eigh) a nejdražší buňka je naplánovaná jako poslední, time-budget se vyčerpá na předposlední buňce a cílová buňka se nikdy nespustí. **Driver-lekce:**
1. **Řadit buňky od nejdražší** (nebo náklady-vyvážený scheduler), aby drahá cílová buňka startovala jako první, ne poslední.
2. **Vynucovat max-hours per-cell, ne jen globálně** — odhadnout N³ náklad předem a skipnout buňku, která se nevejde, místo abys ji začal a nechal zabít timeout (zanechá `null`/rozbitý fit).
3. **4D potřebuje sparse S_full primitiv** (iterativní generalizovaný eigensolver) — dense-eigh zeď na N~3000 je tvrdá hranice celé 4D R-analýzy. Bez něj je 4D R omezeno na N≲3000 (tj. ρ≤480 dense, ρ≤1920 jen pro ℓ=0.8).

---

## Co to znamená pro draft-04 dS sekci / případný draft-05

**2D (Nález 1) je publikovatelně silný.** R = S_full_cap/A_mol je konstantní (R̄=0.130, CV 3 %, drift v ρ = 0) přes rozšířený rozsah ρ 240–1200 a ℓ 0.7–2.5, cross-HW reprodukováno, antikruhovost dodržena. To je čistý kvantitativní area-zákon S_cap ∝ A_horizon s c=7.57 (NE 1/4, viz F-028). **Patří do draft-04 dS sekce jako commitnutý výsledek**, nyní s širším rozsahem než původní F-028.

**4D (Nález 2) NESMÍ nést A/4 claim, dokud se nevyřeší konvenční otázka.** Klíčové zjištění: v této konvenci **R^4D driftuje ρ^(−0.72)**, c roste 5.6→66, takže **NEEXISTUJE čistá 4D area-konstanta**. Diskriminátor (saturuje S_full sám?) ukázal, že S_full roste ρ^1.05 a 4D kodim-2 molekulová „plocha" roste ρ^1.77 — **škálují jinak**, na rozdíl od 2D, kde oba ~ρ^1. Vedoucí vysvětlení je hybrid (a)-jako-konvence: rozdíl škálovacích zákonů obsahu a kodim-2 plochy. **Důsledek pro draft:** jakýkoli „4D dS A/4" nebo „4D entropie-na-molekulu konstanta" claim je v této konvenci **neopodstatněný** a oslabený. Před draft-05 (samostatný dS draft) je nutné NEJDŘÍVE:
1. **Vyřešit konvenci** — definovat 4D molekulovou plochu tak, aby škálovala jako S_full (ρ^1), pokud taková definice existuje; jinak přijmout, že 4D area-konstanta neexistuje (silná verze (c)).
2. **Otestovat konformně-váhový caveat (b)** přesným dS propagátorem — drift může být aproximace.
3. **Dosáhnout vyšší ρ** přes 4D sparse S_full primitiv (Compute limitations bod 3).

Nejpravděpodobnější je **(a)-jako-konvence**: 4D nemá ρ-invariantní R v této piercing-link konvenci, což znamená **ŽÁDNOU čistou 4D area-konstantu**, a tedy oslabení (ne potvrzení) 4D A/4 claimu. **F-025 saturace (Nález 3)** zůstává PARTIAL (jedna čistá ρ=120 buňka navíc, vyšší-ρ compute-bound) — patří do draft-04 dS sekce vedle obsahového diskriminátoru, NE do samostatného draftu.

**Rozhodnutí H5g-6:** dS materiál → **draft-04 sekce**, ne draft-05. 2D area-zákon je commitnutelný; 4D vyžaduje vyřešení konvence jako budoucí práci. Konformně-váhový caveat (b) uvést poctivě v každém případě.

---

## Reference (jen přítomné v repu)

- `dou-sorkin-2003` (gr-qc/0302009) — horizontová entropie jako počet kauzálních linků (molekulová „plocha").
- `clpw-2022` (2206.10780) — dS statická záplata typ II₁.
- `2008.07697` — 4D area-law rank n_max=2N^(3/4).
- `0909.0944` — Johnston 4D link-Greenova fce.
- `1611.10281` — SSEE, dvojitá truncace.
- F-006 (`ssee-diamond/results.json`) — ε ~ ρ^(−1/d), p=0.519±0.007 (antikruhovost).
- F-023 (VYPOCET-19), F-025 (VYPOCET-21), F-028 (VYPOCET-23).
- **⚠️ neověřeno:** de-Sitter Gibbons-Hawking primární zdroj NENÍ v repu; A/4 na kosmologický horizont značeno ⚠️, postupováno přes bezrozměrný poměr R.

## Datové cesty

- 2D: `compute/results-archive/ds_entropy_cap_2d-rho30k.json`
- 4D grid: `compute/results-archive/ds_cap_4d-grid.json`
- 4D high-N: `compute/results-archive/ds_cap_4d-highN.json`
- 4D saturace: `compute/results-archive/ds4d_saturation-rho120.json`
- Figura + skript: `core-data/calculations/ds-entropy-cap/plots/R_2d_vs_4d.png`, `plot_R_2d_vs_4d.py`
