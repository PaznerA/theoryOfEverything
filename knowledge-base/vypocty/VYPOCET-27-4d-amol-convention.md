# VYPOCET-27: 4D A_mol konvence — proč A_mol ~ ρ^1.77 a je 4D area-zákon zachranitelný?

**Datum:** 2026-06-08
**Status:** Dokončeno (rozhodnutí konvenční otázky otevřené VYPOCET-25)
**Navazuje:** VYPOCET-25 / F-029 (4D c driftuje 5.6→65.8, R^4D ~ ρ^−0.72, protože A_mol ~ ρ^1.77 zatímco S_full ~ ρ^1.05), VYPOCET-23 / F-028 (2D R konstantní: OBĚ S_full i A_mol ~ ρ^1.05)
**Otázka:** PROČ 4D horizontová „plocha" (molekulový počet) škáluje jako A_mol ~ ρ^1.77 (ne ρ^0.5), a je 4D entropicko-plošný zákon ZACHRANITELNÝ ve správné Dou-Sorkinově konvenci, nebo genuinně NEPŘÍTOMNÝ?
**Soubory:** `core-data/calculations/ds-amol-convention/calc.py`, `results.json`, `plots/A_mol_raw_vs_corrected_vs_rho.png`; `lib/toe/causet.py:horizon_molecules_codim2`; `app/tests/test_toe_horizon_molecules_codim2.py`
**Cluster:** entropy-cluster × von-Neumann II₁ × horizon-SJ × causal-set first-principles × dimension-dependence

---

## Cíl a sázka

VYPOCET-25 (F-029) nechal otevřenou **konvenční otázku**: 4D poměr R^4D = S_full_cap / A_mol driftuje jako ρ^−0.72, c roste 5.6→66, takže v té konvenci NEEXISTUJE čistá 4D area-konstanta. Kořen byl identifikován jako **rozdíl škálovacích zákonů**: A_mol (raw) ~ ρ^1.77, S_full ~ ρ^1.05. Tři otevřené úkoly:

1. **Diagnostikovat ρ^1.77** — proč raw počet linků křižujících řez škáluje tak rychle?
2. **Implementovat správnou kodim-2 Dou-Sorkinovu molekulu** — měřit horizontovou plochu na kodim-2 entanglement 2-ploše (fixní časořez), ne na kodim-1 světočáře.
3. **Rozhodnout:** zachrání korigovaná plocha 4D area-zákon (R' konstantní), nebo je area-zákon genuinně nepřítomný?

**Vedoucí podezřelý (z promptu, potvrzeno):** `compute/drivers/ds_cap_4d.py:horizon_link_count_4d()` počítá linky křižující řez `{r* = R_CUT}`. V souřadnicích (t, r*, x₁, x₂) je množina `{r* = R_CUT}` **kodim-1 SVĚTOČÁRA-TUBUS** (t, x₁, x₂ se VŠECHNY mění), NE kodim-2 entanglement PLOCHA (2-plocha na fixním čase). Počítání linků přes kodim-1 tubus přes celý časový rozsah škáluje jinak než molekuly na kodim-2 ploše.

---

## Nález 1 — Re-analýza exponentů ze staged dat: VYPOCET-25 POTVRZENO

Stage A, `compute/results-archive/ds_cap_4d-{grid,highN}.json`, dense buňky. Log-log fity A_mol(raw), S_full, n_sub, N_total vs ρ per ℓ (S_full bráno jako plató = průměr přes poslední 3 boxy, robustní vůči rozbitým saturujícím fitům dokumentovaným ve VYPOCET-25).

| ℓ | p_A (A_mol raw) | p_S (S_full) | p_n (n_sub) | p_N (N_total) | drift p_S − p_A |
|---|---|---|---|---|---|
| 0.8 | **1.768 ± 0.029** | **1.055 ± 0.028** | 1.000 | 1.000 | **−0.713** |
| 1.0 | 1.753 ± 0.027 | 1.029 ± 0.015 | 1.000 | 1.000 | −0.725 |
| 1.5 | 1.755 ± 0.013 | 1.012 ± 0.009 | 0.999 | 1.000 | −0.743 |

**Potvrzeno:** p_A ≈ **1.77**, p_S ≈ **1.05**, drift = p_S − p_A ≈ **−0.72** — přesně reprodukuje VYPOCET-25 / F-029. n_sub a N_total škálují čistě jako ρ^1 (objemové). Klíčový kontrast vůči 2D (F-028): tam OBĚ A_mol i S_full ~ ρ^1.05, takže poměr je ρ-invariantní; ve 4D škálují JINAK.

---

## Nález 2 — Diagnóza ρ^1.77: kodim-1 světočára-tubus × 4D link-multiplicita

Stage A2, přímé numerické měření na geometrii `sprinkle_ds_static_patch4d` (ρ ∈ {120,240,480,960}, 3 seedy). Dekompozice raw počtu:

> **raw_worldtube ~ ρ^1.717** (na nezávislém běhu; konzistentní s archivními 1.77)
> = (počet bodů v tubusu ~ n_sub ~ ρ^1.0) × (link-multiplicita na bod ~ ρ^0.66) × (povrchové obohacení)

Změřeno:
- **links_per_point (L/N) ~ ρ^0.655 ± 0.013** — počet ireducibilních linků na element ROSTE s hustotou. Toto je dobře známý 4D causal-set fakt: poměr link/relace NENÍ konstantní (na rozdíl od 2D, kde je O(1)). Hodnoty: L/N = 7.3 → 11.2 → 18.3 → 28.0 přes ρ 120→960.
- **straddling linky mají ρ-NEZÁVISLOU normálovou separaci:** `<|Δt|> ~ ρ^−0.037` (prakticky konstantní ≈ 0.65, blízko plnému t-rozsahu 1.0), `<|Δr*|> ≈ 0.40` konstantní. To je **kuřící zbraň**: straddling linky NEJSOU krátké ε-škálové páry — jsou to **dlouhé téměř-nulové (near-null) linky**, jejichž koncové body jsou daleko v (t, r*), ale lightcone je spojuje přes velkou příčnou (x₁, x₂) separaci.

**Závěr diagnózy:** raw počet = (3-objem světočáry-tubu vzorkovaný ~ ρ^1) × (4D link-multiplicita ~ ρ^0.7). Naivní odhad z promptu (kodim-1 plocha v ε-jednotkách ~ ρ^0.75) selhal o faktor ~ρ^1, protože **link-multiplicita na povrchový bod NENÍ O(1)** — ve 4D dlouhé near-null linky umožní jednomu povrchovému bodu linkovat na MNOHO bodů přes celý příčný rozsah. ρ^1.77 je tedy konzistentní s „linky přes kodim-1 světočáru-tubus", NE s kodim-2 plochou ρ^0.5. **Molekuly se v této ploché kauzální struktuře NElokalizují na žádnou 2-plochu.**

---

## Nález 3 — Korigovaná kodim-2 Dou-Sorkinova molekula: ρ^0.5 OBNOVENO

Nový knihovní primitiv `toe.causet.horizon_molecules_codim2` (Dou-Sorkin gr-qc/0302009). Molekula = straddling LINK (p, q) (právě jeden konec v O = {r* ≤ R_CUT}), jehož OBĚ koncové body leží v rámci vlastní vzdálenosti `k_tube·ε` od kodim-2 entanglement 2-plochy `E₀ = {r* = R_CUT, t = 0}` v normálové (t, r*) rovině, A jehož vlastní interval τ ≤ k_tube·ε (genuinní nejbližší kauzální pár, ne dlouhý near-null link). Příčné směry (x₁, x₂) zametají 2-plochu, takže počet vzorkuje 2-PLOCHU: pro fixní vlastní plochu `<n_molecule> ~ A/ε² ~ ρ^(D−2)/D = ρ^0.5`.

**Konvence kodim-2 oproti raw:** raw řez = celý kodim-1 tubus (t, x₁, x₂ se mění); E₀ = fixní-čas 2-plocha (jen x₁, x₂ se mění). Volba `k_tube = 1.5` (jedna nejbližší kauzální vrstva v normálové rovině) je principiální; `k_tube ≈ 1` je area-přesné ale šumové (málo molekul), `k_tube ≳ 2` přechází zpět ke kodim-1 tubu.

**Měřený exponent (Stage B, ρ ∈ {120, 240, 480}, ℓ=1.0, 4 seedy, dense N ≤ 1920):**

> **A_mol^codim-2 ~ ρ^(0.494 ± 0.006)** — prakticky PŘESNĚ vlastní-plošný cíl ρ^0.5.
>
> Pro srovnání na témže běhu: raw_worldtube ~ ρ^(1.702 ± 0.053), S_full ~ ρ^(0.997 ± 0.015).

Robustnost (prototyp, ℓ ∈ {0.8, 1.0}, k ∈ {1.0, 1.5, 2.0}): k=1.0 → p ≈ 0.40–0.45 (area, šum); **k=1.5 → p ≈ 0.52–0.62 (čistý počet I area)**; k=2.0 → p ≈ 0.76–0.80 (přechod k tubu). Reziduální tilt +0.0–0.1 nad 0.5 je tatáž 4D near-null link-multiplicita (poctivě hlášeno).

Figura `plots/A_mol_raw_vs_corrected_vs_rho.png` (log-log): raw (červená) sleduje ρ^1.77, korigovaná kodim-2 (zelená) sleduje ρ^0.5, S_full (modrá) sleduje ρ^1.05.

---

## Nález 4 — Test ρ-invariance R'/R'': ROZHODUJÍCÍ NEGATIV

| ρ | A_raw | A_codim2 | S_full plató | S_trunc plató | R' = S_full/A_cod2 | R'' = S_trunc/A_cod2 | R_raw = S_full/A_raw |
|---|---|---|---|---|---|---|---|
| 120 | 346 | 92.4 | 27.4 | 14.79 | 0.296 | 0.160 | 0.0792 |
| 240 | 1056 | 131.2 | 53.7 | 0.00 | 0.409 | 0.000 | 0.0508 |
| 480 | 3659 | 183.4 | 109.1 | 0.00 | 0.595 | 0.000 | 0.0298 |

- **R' = S_full_cap / A_mol^codim-2: CV = 0.35, drift d ln R'/d ln ρ = +0.50.** NENÍ konstantní. Drift je teď KLADNÝ (opak raw ρ^−0.72), přesně podle predikce: R' ~ ρ^(p_S − p_codim2) = ρ^(1.05 − 0.5) = **ρ^+0.55**.
- **R'' = S_trunc_cap / A_mol^codim-2: CV = 1.73.** NENÍ konstantní; navíc S_trunc kolabuje na 0 při ρ ≥ 240, ℓ=1.0 (n_max = 2N^0.75 truncace zahodí všechny mody — týž artefakt jako v archivu při ρ ≥ 240). S_trunc NENÍ správný plošný kanál.
- **R_raw = S_full_cap / A_mol^raw: CV = 0.46** (ρ^−0.72, jak ve VYPOCET-25).

**ŽÁDNÝ z poměrů (R', R'', R_raw) není ρ-invariantní.**

---

## Verdikt — výsledek (b): 4D area-zákon je v této konstrukci NEPŘÍTOMNÝ (poctivý negativ)

Z trojrozhodovacího diskriminátoru (deliverable 5) platí **(b)**, ne (a) ani (c):

**(a) Korigovaná molekula zachrání area-zákon → R' konstantní → ZAMÍTNUTO.** R' driftuje ρ^+0.55 (CV 0.35).
**(c) S_trunc je správný plošný kanál → R'' konstantní → ZAMÍTNUTO.** R'' CV 1.73; S_trunc kolabuje na 0.
**(b) Molekula škáluje ρ^0.5 ALE S_full roste ρ^1.05 → R' stále driftuje → POTVRZENO.**

> **Korigovaná kodim-2 molekula škáluje jako vlastní plocha (ρ^0.494 ± 0.006, přesně cíl), čímž je konvenční diagnóza VYŘEŠENA: ρ^1.77 byl artefakt počítání linků přes kodim-1 světočáru-tubus, NE selhání fyziky.** Ale i se SPRÁVNOU plochou **S_full sám škáluje objemově (ρ^0.997), NEsaturuje na ρ-nezávislou konstantu** — takže poměr S_full / A_plocha NUTNĚ driftuje. **V této konstrukci 4D strop NESLEDUJE vlastní horizontovou plochu**; čistý 4D area-zákon S ∝ A_proper v ní NEEXISTUJE.

To je **poctivý negativ, který POSILUJE VYPOCET-25 / F-029**, a vysvětluje jeho původ: drift R^4D NENÍ jen konvenční (kdyby byl, korigovaná plocha by ho zrušila — neudělala to). Jádro je, že **obsah-entropie S_full škáluje jako 4-objem (ρ^1), zatímco vlastní horizontová plocha škáluje jako 2-plocha (ρ^0.5)** — dvě různá škálování, jejichž poměr nemůže být konstantní. V 2D oba shodou okolností škálují ρ^1 (horizont je BOD, kodim-2 = 0-dim, jeho „plocha" = link-count ~ ρ^1, stejně jako objem), takže R^2D je konstantní (F-028). Ve 4D ta degenerace mizí.

### Rozhodnutí o 4D A/4 claimu

VYPOCET-25 4D A/4 claim „oslabil". **VYPOCET-27 ho ROZHODUJE: žádný 4D A/4 (ani „4D entropie-na-molekulu konstanta") claim NELZE udělat v této ploché-kauzální-struktuře + dS-sech²-míra konstrukci.** Není to ladění konvence — korigovaná Dou-Sorkinova plocha je správná a dává ρ^0.5, přesto poměr driftuje, protože S_full je objemová veličina. 4D area-zákon by vyžadoval, aby strop S_full SÁM saturoval na plošně-škálující veličinu — což se neděje (S_full ~ ρ^1).

---

## Poctivé limity a caveaty

- **Konformně-váhový caveat (b z VYPOCET-25) NEVYŘEŠEN.** 4D bezhmotný skalár NENÍ konformně invariantní; tohle je řízená aproximace VYPOCET-21 (plochá kauzální struktura v (t, r*, x₁, x₂) + dS proper sech² míra + Johnston 0909.0944 link-Green), NE přesný 4D dS Wightmanův stav. Drift S_full ~ ρ^1 vs plocha ρ^0.5 by mohl být částečně tato aproximace. Repo nemá přesný zakřivený 4D dS propagátor; netestujeme to. Tvrzení „4D area-zákon nepřítomný" platí **pro tuto konstrukci**, ne nutně pro přesný dS stav.
- **dS-specifický Gibbons-Hawking primár NENÍ v repu** → aplikace A/4 na kosmologický horizont značena ⚠️ neověřeno; postupováno přes bezrozměrné poměry.
- **k_tube citlivost.** Korigovaný exponent závisí na k_tube (0.4 při k=1.0 → 0.8 při k=2.0); k=1.5 dává čistý ρ^0.5 s rozumnými počty. Crossover sám je fyzikální (malá koule = kodim-2 area, velká = kodim-1 tubus). Reziduální tilt +0.0–0.1 nad 0.5 z 4D link-multiplicity.
- **S_trunc kolaps.** n_max = 2N^0.75 truncace dává S_trunc = 0 při ρ ≥ 240, ℓ=1.0 (týž archivní artefakt). R'' kanál je tím znehodnocen; nelze z něj udělat čistý area-test.
- **Rozsah ρ.** Stage B jen ρ ∈ {120, 240, 480} (dense N ≤ 1920, afternoon-budget; vyšší ρ by potřebovalo 4D sparse S_full primitiv, který repo nemá — viz VYPOCET-25 Compute limitations). Exponent 0.494 ± 0.006 je nicméně 3-bodový s těsným SE; prototyp potvrdil 0.46–0.62 i na ρ až 960 a přes ℓ.

---

## Reference (jen přítomné v repu)

- `dou-sorkin-2003` (gr-qc/0302009) — horizontová entropie jako počet kauzálních linků (molekulová „plocha"); kodim-2 lokalizace molekulového počtu.
- `johnston-2009` (0909.0944) — 4D link-Greenova fce.
- `clpw-2022` (2206.10780) — dS statická záplata typ II₁.
- F-006 (`ssee-diamond/results.json`) — ε ~ ρ^(−1/d), p=0.519±0.007 (antikruhovost; 4D ε = ρ^−1/4).
- F-028 (VYPOCET-23), F-029 (VYPOCET-25).
- **⚠️ neověřeno:** de-Sitter Gibbons-Hawking primární zdroj NENÍ v repu.

## Knihovní změny

- `lib/toe/causet.py:horizon_molecules_codim2(coords, C_or_L, *, r_index=1, r_cut, eps, k_tube=1.5, return_diagnostics=False)` — nový composable primitiv (Formula/Evidence/Conventions docstring); kodim-2 Dou-Sorkinova molekula. Test `app/tests/test_toe_horizon_molecules_codim2.py` (5 testů: základní hand-checkable případ, vyloučení dlouhého near-null straddle, C-vs-L ekvivalence, subset-of-raw audit, ρ^0.5-ne-ρ^1.77 škálování).

## Datové cesty

- `core-data/calculations/ds-amol-convention/{calc.py,results.json}`, `plots/A_mol_raw_vs_corrected_vs_rho.png`
- Vstupní archiv: `compute/results-archive/ds_cap_4d-{grid,highN}.json`
