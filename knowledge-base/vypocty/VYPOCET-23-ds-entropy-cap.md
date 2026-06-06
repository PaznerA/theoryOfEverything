# VYPOCET-23: Strop de-Sitterovy entropie vs. Gibbons-Hawking A/4 — test H5g-2

**Datum:** 2026-06-06
**Soubory:** `core-data/calculations/ds-entropy-cap/calc.py`, `results.json`, `plots/{saturation,discriminator,scaling}.png`
**Status:** Dokončeno
**Hypotéza (BRAINSTORM-05, H5g-2, priorita high):** Mapuje se konečný **strop**, na který saturuje entropie ohraničené de-Sitterovy statické záplaty (nález F-023, VYPOCET-19), **KVANTITATIVNĚ** na Gibbons-Hawking / Bekenstein-Hawking **A/4** — tedy diskrétní de-Sitterova entropie z prvních principů?
**Cluster:** entropy-cluster × von-Neumann II₁ × horizon-SJ × causal-set first-principles
**Navazuje:** VYPOCET-19 (F-023: dS strop, II₁), F-006 (VYPOCET-04 ssee-diamant: kalibrace ε ~ ρ^(−1/2))

---

## Cíl a sázka

VYPOCET-19 (F-023) ukázal, že obsah ohraničené dS statické záplaty **saturuje** na konečný strop (N_total → 480 při ρ_proper = 240), a že SJ+truncace machinerie odliší typ **II₁** (saturuje) od II_∞ (roste). To je **kvalitativní** signatura. H5g-2 ptá ostřeji: je strop **kvantitativně** A/4-zákon? Tj. je entropický strop _úměrný_ diskrétní „ploše" horizontu, s **konstantním** poměrem nezávislým na hustotě ρ a velikosti záplaty ℓ?

**Diskriminátor:** poměr R = S_cap / (plocha horizontu v ε-jednotkách).
- R **konstantní** napříč (ρ, ℓ) ⇒ kvantitativní A/4-podobný zákon (S ∝ A); je konstanta ~1/4?
- R **driftuje** ⇒ strop je jen kvalitativní; silnou H5g-2 zabíjíme, dokumentujeme drift.

---

## Antikruhovost (povinný protokol BRAINSTORM-05)

Měřítko diskrétnosti **ε ~ ρ^(−1/2) FIXUJEME z NEZÁVISLÉHO výsledku F-006** (`ssee-diamond/results.json`) PŘED měřením jakéhokoli poměru — ε se **nikdy neladí**, aby vyšel poměr 1/4.

F-006 (entropy-cutoff rank): `p_rank_vs_N = 0.5189 ± 0.0067`, tedy rank kept-modů ~ N^0.519 ≈ N^(1/2), což přesně odpovídá ε ~ ρ^(−1/2). Používáme **ideální exponent 1/2** (měření F-006 ho potvrzuje v rámci ~3σ); v kódu:

```
ε(ρ) = ρ^(−1/2)   # FIXED, not tunable
```

---

## 2D formulace „plochy horizontu" (pečlivě)

V D rozměrech je dS horizont **kodimenze 2** (plocha je (D−2)-rozměrná). Ve **D = 2** je D−2 = 0:

- **Horizont je BOD** (jediná hrana statické záplaty r* → ∞); jeho „plocha" je **0-rozměrná**.
- Spojitá plocha v ε-jednotkách: A / ε^(D−2) = A / ε^0 = A — **bezrozměrná a na ε NEZÁVISLÁ**. Proto S_GH = A/4 je v causal-set jednotkách **číslo O(1)**.
- Diskrétní avatar 0-rozměrné plochy = **počet kauzálních linků („horizontových molekul")** křižujících řez, à la **Dou-Sorkin (gr-qc/0302009, „Black Hole Entropy as Causal Links")**.

**Operační realizace.** Entanglement řez fixujeme na r* = R_CUT = 0.8 (kodim-2 plocha = bod na časořezu, tj. časupodobná světočára přes t-rozsah). Hrana boxu R*_box → kosmologický horizont (r* → ∞) při fixní ρ. Měříme:
- **A_mol** = počet ireducibilních linků (b ≺ a, žádný mezilehlý bod) s právě jedním koncem na každé straně řezu r* = R_CUT.

**Klíčové škálování (změřeno, exaktně z plné link-matice):** A_mol ∝ ρ (= ε^(−2)). Řez je 1-rozměrná světočára nesoucí ~ρ·t_extent linků. Spojitá plocha A_cont = A_mol·ε² = A_mol/ρ → O(1) konstanta (F-006 ε² převádí ρ-škálující počet molekul na O(1) spojitou plochu).

---

## Reference (jen přítomné v repu)

| ref | arXiv/DOI | role |
|---|---|---|
| `clpw-2022` | 2206.10780 | dS statická záplata typ II₁; max-entropický prázdný-dS stav, S ~ generalized entropy |
| `dou-sorkin-2003` | gr-qc/0302009 | entropie horizontu jako počet kauzálních linků (2D horizontová „plocha") |
| `bekenstein-hawking-formula` | formulas.json | S = A/(4 ℓ_P²) k (samotný A/4 zákon) |

**⚠️ neověřeno (per jazyková politika):** de-Sitter-specifický Gibbons-Hawking primární zdroj (typu gr-qc/0205058) **NENÍ v repu**. Aplikaci A/4 na _kosmologický_ horizont tedy značíme `⚠️ neověřeno` a postupujeme přes **bezrozměrný poměr** — samotný A/4 vzorec a II₁ max-entropický strop (CLPW) přítomné jsou.

---

## Metodika

| krok | implementace (thin nad `toe` v0.3.0) |
|---|---|
| geometrie | `causet.sprinkle_ds_static_patch2d` (sech² vlastní míra; protokol VYPOCET-19 Part 1) |
| hustoty | ρ ∈ {240, 600, 1200} dense (primární kanál; 5× rozsah); ρ = 3000 sparse (konzistenční blok) |
| SJ stav | dense: `causal_matrix → green_retarded_2d → pauli_jordan → sj.wightman`; sparse (N>4500): `idelta_operator_2d` (float32) + `sj_state_sparse` (eigsh, k = 5√N) |
| entropie | `entropy.ssee` (S_full bez truncace; S_trunc s κ = √N/4π); sparse: `ssee_sparse` |
| strop | saturující fit S_cap − B·exp(−R*/ξ) vs lineární; **AIC** (`fits.aic_compare`) |
| nejistoty | bootstrap přes seedy (1000 resamplů, CI68) přes `toe.fits` |
| invariant | ± párování `causal_diagnostics` asertováno na KAŽDÉ oblasti (< 1e-9) |

**Volba kanálu (klíčové fyzikální rozhodnutí).** S_full (obsah-sledující SSEE) i A_mol škálují ~ρ, takže jejich poměr **R_full = S_full_cap / A_mol** je ρ-invariantní „entropie na horizontovou molekulu" = diskrétní A/4 koeficient. Naopak **truncovaná** SSEE je O(1) a molekulový počet NEsleduje, proto je R_trunc/A_mol → 0; truncovaný kanál hlásíme proti spojité ploše A_cont (sekundárně). S_full je vnitřně **dense** (objemový zákon přes všech ~N modů), takže primární poměr měříme jen na dense hustotách.

**Seedy:** 4 při ρ ∈ {240, 600}, 3 při ρ=1200; l-scan 3 seedy; sparse blok 2 seedy. ± párovací invariant ověřen na každé oblasti: dense ~1e-15 (float64), sparse ~2e-9 (float32 eigsh, v rámci tolerance daného path).

---

## Výsledky

### F-023 reprodukováno

Obsah saturuje: N_total → 480 (ρ=240, fixní cut), shoda s F-023 (N_total_cap = 480.11). Při fixním entanglement řezu r* = 0.8 a hraně boxu → horizont saturuje jak obsah pod-oblasti, tak S_full a S_trunc na konečný strop. AIC preferuje saturující fit nad lineárním. Vysokohustotní sparse blok (ρ=3000, N≤6000): N_total saturuje na 6000, S_trunc ≈ 1.14 (O(1)) — konzistentní.

### Primární kanál: R_full = S_full_cap / A_mol (A/4 kandidát)

**Škálování s hustotou** (l = 1):

| ρ | N_max | S_full_cap | A_mol | ε = ρ^(−1/2) | **R_full** | R_trunc_cont |
|---|---|---|---|---|---|---|
| 240 | 480 | 46.19 | 344.8 | 0.0645 | **0.1339** | 0.4463 |
| 600 | 1200 | 121.82 | 921.8 | 0.0408 | **0.1321** | 0.4449 |
| 1200 | 2400 | 249.46 | 1909.8 | 0.0289 | **0.1306** | 0.4666 |

**Škálování s velikostí záplaty** (ρ = 600):

| ℓ | S_full_cap | A_mol | **R_full** |
|---|---|---|---|
| 0.7 | 62.84 | 484.8 | **0.1296** |
| 1.0 | 122.89 | 927.2 | **0.1325** |
| 1.5 | 182.60 | 1364.7 | **0.1338** |

Nezávislá single-box (R*=7) sonda dala R_full = {0.137, 0.132, 0.129} při ρ = {240, 1000, 3000} — konstantnost potvrzena i za dense žebříček.

### Diskriminátor

| veličina | drift exponent (d ln/d ln ρ) | interpretace |
|---|---|---|
| A_mol vs ρ | **+1.06** | molekulový počet ∝ ρ (Dou-Sorkin; ε^(−2)) |
| S_full_cap vs ρ | **+1.05** | obsah-entropie ∝ ρ |
| S_trunc_cap vs ρ | +0.09 | truncovaná = 2D area/log, O(1) — NEsleduje A_mol |
| **R_full vs ρ** | **−0.015** | **R = S_full/A_mol prakticky NEZÁVISLÉ na ρ** |

**Konstantnost R_full:** CV(ρ) = 1.25 %, CV(ℓ) = 1.6 %. Kombinovaná střední hodnota přes (ρ, ℓ): **R_full = 0.1321 ± (CV 1.3 %)**, drift exponent vs ρ = −0.015 (slučitelný s 0).

S_full_cap i A_mol škálují obě ∝ ρ^1.05 → jejich poměr je ρ-invariantní = diskrétní „entropie na horizontovou molekulu".

---

## Verdikt

**PARTIAL/AFFIRMATIVE — kvalitativní strop F-023 je povýšen na KVANTITATIVNÍ area-zákon, ale konstanta NENÍ 1/4.**

Poměr R_full = S_full_cap / A_mol je **KONSTANTNÍ** napříč 5× rozsahem hustoty ρ ∈ {240, 600, 1200} I 2× rozsahem velikosti záplaty ℓ ∈ {0.7, 1.0, 1.5}, s kombinovanou střední hodnotou **R = 0.1321 ± 1.3 %** a driftovým exponentem −0.015 (slučitelným s nulou). To znamená:

$$S_{\rm cap} = \frac{A_{\rm horizon}}{c\,G}, \qquad c = \frac{1}{R_{\rm full}} \approx 7.57.$$

Entropický strop ohraničené dS statické záplaty je tedy **ÚMĚRNÝ** diskrétní Dou-Sorkinově horizontové „ploše" (počtu kauzálních molekul) — povýšení **kvalitativní saturace (II₁) → kvantitativní area-zákon**. Hypotéza H5g-2 ve **slabé** formě (existuje konstantní A/4-podobný zákon) je **POTVRZENA**.

V **silné** formě (konstanta = 1/4) je **VYVRÁCENA**: R = 0.132 ≈ 0.53 × (1/4), tedy c ≈ 7.57 ≠ 4. To je očekávané a poctivé: geometrická O(1) normalizace 2D molekulového počtu vs. SSEE není v causal-set jednotkách fixována tak, aby dala přesně 4 (samotný Dou-Sorkin koeficient vyžaduje separátní kalibraci). **Doslovná čtvrtina není získána; úměrnost ano.**

**Antikruhovost dodržena:** ε ~ ρ^(−1/2) zafixováno z F-006 před měřením; konstantnost R_full je nezávislá na volbě ε (2D plocha je ε-nezávislá), takže výsledek není kalibrací zařízen.

---

## Honest nuly a limity

- **S_full je dense-only.** Top-k sparse zachycení (eigsh, k~5√N) reprezentuje jen mody nad κ — nereprezentuje objemový zákon S_full (potřebuje všech ~N modů). Generalizovaný eigenproblém S_full škáluje ~N_sub³, takže rozpočet omezuje N≤~2500 → primární poměr na ρ ∈ {240, 600, 1200} (5× hustoty). To je rozhodné (drift by se na 5× projevil; R drift = −0.015). ρ=10000 (N=20000) je mimo rozpočet (eigsh ~160 s/box).
- **A_mol nelze oknovat.** Časové okno mění, které linky jsou ireducibilní (ověřeno: oknovaný odhad biasuje ρ-škálování, est/ρ = 0.88 vs 0.24). A_mol proto exaktně jen z plné link-matice na dense hustotách.
- **Koeficient ≠ 1/4 (poctivé vyvrácení silné formy).** R = 0.132, c = 7.57. Geometrická O(1) normalizace 2D molekulového počtu vs. SSEE není fixována tak, aby dala přesně 4. Potvrzujeme **konstantnost** (kvalitativní→kvantitativní upgrade), NE doslovnou čtvrtinu.
- **Float32 sparse párovací tolerance.** Sparse eigsh páruje ± na ~2e-9 (float32 přesnost), ne 1e-15 jako dense float64 — `calc.py` assert je nyní path-aware (dense < 1e-12, sparse < 5e-9). (První běh na starém příliš těsném assertu (1e-9) spadl v sparse bloku PO zalogování veškeré fyziky; `results.json` rekonstruováno z kompletního `run.log` přes `reconstruct.py`, hodnoty caps jsou bootstrap caps běhu, per-box hodnoty seed-průměry.)
- **Sdílené CPU.** Běh sdílel stroj s paralelní úlohou (ds-tracial-probe); proto delší runtime, ale výsledky nedotčené.

---

## Konvence / citace

- A/4 zákon: `bekenstein-hawking-formula`. II₁ max-entropický strop: `clpw-2022` (2206.10780). Molekulová „plocha": `dou-sorkin-2003` (gr-qc/0302009).
- ε ~ ρ^(−1/2): F-006 (`ssee-diamond/results.json`, p_rank = 0.519 ± 0.007).
- ⚠️ neověřeno: de-Sitter Gibbons-Hawking primární zdroj není v repu.
