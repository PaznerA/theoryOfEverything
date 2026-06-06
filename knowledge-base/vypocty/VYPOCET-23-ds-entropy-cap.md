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
| hustoty | ρ ∈ {240, 1000, 2000} dense (primární kanál); ρ = 3000 sparse (konzistenční blok) |
| SJ stav | dense: `causal_matrix → green_retarded_2d → pauli_jordan → sj.wightman`; sparse (N>4500): `idelta_operator_2d` (float32) + `sj_state_sparse` (eigsh, k = 5√N) |
| entropie | `entropy.ssee` (S_full bez truncace; S_trunc s κ = √N/4π); sparse: `ssee_sparse` |
| strop | saturující fit S_cap − B·exp(−R*/ξ) vs lineární; **AIC** (`fits.aic_compare`) |
| nejistoty | bootstrap přes seedy (1000 resamplů, CI68) přes `toe.fits` |
| invariant | ± párování `causal_diagnostics` asertováno na KAŽDÉ oblasti (< 1e-9) |

**Volba kanálu (klíčové fyzikální rozhodnutí).** S_full (obsah-sledující SSEE) i A_mol škálují ~ρ, takže jejich poměr **R_full = S_full_cap / A_mol** je ρ-invariantní „entropie na horizontovou molekulu" = diskrétní A/4 koeficient. Naopak **truncovaná** SSEE je O(1) a molekulový počet NEsleduje, proto je R_trunc/A_mol → 0; truncovaný kanál hlásíme proti spojité ploše A_cont (sekundárně). S_full je vnitřně **dense** (objemový zákon přes všech ~N modů), takže primární poměr měříme jen na dense hustotách.

**Seedy:** ≥4 při ρ ∈ {240,1000}, 2 při ρ=2000; l-scan 3 seedy; sparse blok 2 seedy.

---

## Výsledky

### F-023 reprodukováno

Obsah saturuje: N_total → 480 (ρ=240), shoda s F-023 (N_total_cap = 480.11). Strop S_full i N_total: AIC silně preferuje saturující fit nad lineárním. Plochá kontrola (VYPOCET-19) rostla — zde se soustředíme na dS stranu.

### Primární kanál: R_full = S_full_cap / A_mol

<!--FILL_TABLE-->

### Diskriminátor

<!--FILL_DISCRIMINATOR-->

---

## Verdikt

<!--FILL_VERDICT-->

---

## Honest nuly a limity

- **S_full je dense-only.** Top-k sparse zachycení nereprezentuje objemový zákon S_full; ρ=10000 (N=20000) je mimo rozpočet (eigsh ~160s/box). Primární poměr je tedy na rozsahu ρ ∈ {240,1000,2000} (8.3× hustoty) — ale to je rozhodné (drift by se na 8× projevil).
- **A_mol nelze oknovat.** Časové okno mění, které linky jsou ireducibilní (ověřeno: oknovaný odhad biasuje ρ-škálování). A_mol proto exaktně jen na dense hustotách.
- **Koeficient ≠ 1/4 a priori.** Geometrická O(1) normalizace 2D molekulového počtu vs. SSEE není fixována tak, aby dala přesně 4; testujeme **konstantnost** (kvalitativní→kvantitativní upgrade), ne doslovnou čtvrtinu.

---

## Konvence / citace

- A/4 zákon: `bekenstein-hawking-formula`. II₁ max-entropický strop: `clpw-2022` (2206.10780). Molekulová „plocha": `dou-sorkin-2003` (gr-qc/0302009).
- ε ~ ρ^(−1/2): F-006 (`ssee-diamond/results.json`, p_rank = 0.519 ± 0.007).
- ⚠️ neověřeno: de-Sitter Gibbons-Hawking primární zdroj není v repu.
