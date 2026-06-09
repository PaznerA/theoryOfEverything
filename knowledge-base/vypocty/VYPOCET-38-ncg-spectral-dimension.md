# VYPOCET-38 — NCG ↔ spectral-dimension: sdílený heat kernel (`Tr e^{-σ D²}`)

> **Hypotéza:** H-C (`knowledge-base/LOV-18-11-overlaps.md` §2.3 / §3.2).
> **Hrana:** `noncommutative-geometry ↔ spectral-dimension` (ML link-prediction score **0.896**, `core-data/link-predictions.json`).
> **Kotva:** F-001 / F-002 (probe-závislost `d_s`), F-003 / F-014 (a₄ poměr = −18/11), F-012 (α-drift / non-konvergence varování).
> **Calc dir:** `core-data/calculations/ncg-spectral-dimension/` (`calc.py` + `results.json` + `heatkernel_ds_and_a4.png`).
> **Lib primitiva:** `toe.spectral.heat_kernel_from_spectrum` (+ `HeatKernelSpectrum`), test `app/tests/test_toe_spectral.py::TestHeatKernelFromSpectrum`.
> **Datum:** 2026-06-09.

---

## Shrnutí výpočtu

Z **jednoho** spektra operátoru `D²` na 2D Poissonem sprinklovaném causal diamondu se extrahují **obě** veličiny, které podle H-C žijí z téhož heat-kernelu `Tr e^{-σ D²} = Σᵢ e^{-σ λᵢ}`:

1. **Spektrální dimenze** `d_s(σ) = −2 d ln Z/d ln σ` — UV/IR škálovací exponent návratové pravděpodobnosti.
2. **Seeley–DeWittovy koeficienty** `a₀, a₂, a₄` z malo-`σ` rozvoje `Z(σ) ~ σ^{−D/2}(a₀ + a₂σ + a₄σ² + …)` — tytéž koeficienty, které čte NCG spektrální akce (`toe.ncg`).

**Hlavní čísla (N = 2200, 3 seedy, BD d'Alembertianova sonda):**

| veličina | naměřeno | analytický cíl | shoda |
|---|---|---|---|
| `d_s` plateau | **1.998 ± 0.044** | 2 (2D BD-sonda, F-001/F-002) | **ANO** (chyba 0.0024 < F-001 tol 0.06) |
| `a₀` (vedoucí objemový člen) | 0.394 | `Vol/(4π) = 0.318` (flat 2D Weyl) | řádově (finite-N drift) |
| `a₄/a₀` | **−1.40 ± 4.25** | −18/11 = −1.636 (kontinuum, Diracův obsah) | **NE** (rezidual 14 %, ale dominuje šum) |
| `d_s` (Pauli-Jordanova sonda) | 0.011 | — | omezené spektrum, žádné UV škálování |

**Korespondence: `partial`.** `d_s` je z **téhož** spektra robustně určen a sedí na analytickou 2D hodnotu; a₄ poměr `−18/11` se v plochém skalárním causetu **nereprodukuje** (a₄ je tam analyticky 0). Sdílený-heat-kernel most je tedy **datově prokázán na `d_s` kanálu** (barely → partially); kontinuální racionál −18/11 přes diskrétní koeficienty NE.

---

## Metoda a setup

### Geometrie a operátor

- **Geometrie:** `toe.causet.sprinkle_diamond2d(N, rng, t_half=1)` — (u,v)-čtverec, plocha 4, `ρ = N/4`.
- **Sonda A (čistá, Laplaceova):** sharp 2D Benincasa–Dowkerův d'Alembertián `B` (vrstvové koeficienty `(1, −2, 1)`, prefaktor `2/l² = 2ρ`, diagonála `−2ρ`). `B` je Lorentzovský (indefinitní) Box; jako pozitivní `D²` se bere **modul symetrizace** `D² = |sym(B)|` přes funkcionální kalkul. Spektrum je **neomezené nahoru** → existuje UV škálovací okno.
- **Sonda B (kontrast, F-001/F-002):** `D² = |iΔ|` přes `toe.spectraltriple.dirac_from_kernel(iΔ)`, kde `iΔ = i(G_R − G_Rᵀ)` z `G_R = ½C` (massless 2D skalár). Spektrum je **omezené nahoru** discreteness-škálou.

### Observable a extrakce (lib primitiva `heat_kernel_from_spectrum`)

`Z(σ) = Σᵢ e^{-σ λᵢ}` přes log-sum-exp (stabilní). Z toho:

- `d_s(σ) = −2 d ln Z/d ln σ` (central difference na log-σ mřížce, 160 bodů, σ ∈ [10², 10⁻⁵]).
- **Plateau:** nejširší okno na malo-σ straně (σ < 1, Z > 1.5), kde `|d_s − 2·round(med/2)| < 0.25`; `d_s` plateau = medián, šířka v dekádách.
- **Koeficienty:** kvadratický fit `Z(σ)·σ^{D/2} ≈ a₀ + a₂σ + a₄σ²` **striktně uvnitř** lokalizovaného `d_s` plateau (tam, kde vedoucí `σ^{−D/2}` škálování platí nejlépe).

### Konfigurace

- N ∈ {800, 1200, 1700, 2200} (dense `eigh`, N ≤ 2500), seedy {11, 23, 37}, D = 2.
- Wall cap ~25 min; reálný runtime **27 s**. numpy/scipy only.
- Atomický + progresivní zápis `results.json` (tmp + `os.replace`) po každé (probe, N) buňce, pevné schéma + pole `status`.

### Anti-cirkularita

- Cílové hodnoty **pre-registrované před měřením**: `d_s = 2` (F-001/F-002 BD-sonda), `a₄/a₀ = −18/11` (z `toe.ncg.spectral_action_ratio`, exact-rational, instant).
- BD vrstvové koeficienty `(1, −2, 1)` a prefaktor `2ρ` jsou z literatury (Sorkin / Benincasa–Dowker 1001.2725 — 2D analog 4D `(1, −9, 16, −8)`), neladěné.

---

## Výsledky

### `d_s` kanál (sdílené spektrum) — KONZISTENTNÍ a sedí

| N | `d_s` plateau (BD) | std | plateau šířka [dec] | shoda F-001 |
|---|---|---|---|---|
| 800 | 1.995 | 0.054 | 1.83 | ANO |
| 1200 | 1.988 | 0.033 | 1.91 | ANO |
| 1700 | 1.994 | 0.009 | 2.30 | ANO |
| 2200 | 1.998 | 0.044 | 2.25 | ANO |

`d_s → 2.00` na **každém** N, std klesá, plateau se **rozšiřuje** (1.83 → 2.30 dekád) — čistá konvergence. Pauli-Jordanova sonda dává `d_s ≈ 0.011` (omezené spektrum, `Z → N`, žádné UV škálování) — **F-001/F-002 probe-závislost zkonkretizována**: ne každé `D²` je platná UV heat-kernel sonda.

### `a₄` kanál — NEkonzistentní s −18/11 (čistý NEGATIV, plochý prostor)

`a₄/a₀` přes seedy a N:

| N | `a₄/a₀` (mean ± std) | per-seed hodnoty |
|---|---|---|
| 800 | −2.19 ± 2.39 | [−4.09, −2.97, +0.49] |
| 1200 | −10.30 ± 10.03 | [−21.59, −2.44, −6.88] |
| 1700 | −0.73 ± 1.80 | [−0.69, +1.06, −2.54] |
| 2200 | −1.40 ± 4.25 | [+0.79, −6.30, +1.30] |

Per-seed hodnoty **mění znaménko** a kolísají od −21.6 do +1.3; across-seed std je **větší než mean**; není žádná monotónní konvergence k −18/11. Hodnota −1.40 na největším N je **náhoda šumu**, ne signál. To je přesně očekávané: `a₂, a₄` jsou integrály křivosti → na **plochém** causetu jsou analyticky **0**, takže diskrétní `a₄/a₀` je finite-N artefakt driftující k ~0, konzistentní s F-012 (α-drift / non-konvergence při N ≤ 3000). Naproti tomu `a₀ ≈ 0.39–0.44` (vs flat-2D Weyl `Vol/(4π) = 0.318`) je řádově správný objemový člen.

### Sanity / lib validace

Syntetická Weylova spektra (deterministická, v testu): 2D konstantní hustota `A/(4π)` → `d_s = 2.015`, `a₀ = 0.3174` (cíl 0.3183, 0.3 %); 4D `N(E)~E²` → `d_s = 4.02`. Omezené spektrum → žádné `d_s = 2` plateau. Normalizační invariance (1/N se v log-derivaci kráti) ověřena.

---

## Verdikt a limity

**Korespondence = `partial`.** Diskriminátor H-C má dvě části a každá padla jinak:

- **`d_s` (POZITIV):** spektrální dimenze a heat-kernel koeficienty jsou prokazatelně extrahovány z **téhož** `Tr e^{-σ D²}` (sdílený heat kernel — to je doslova shared-math obsah hrany). `d_s` (BD-sonda) sedí na analytickou 2D hodnotu 2 do F-001 tolerance, robustně přes N. → Most `NCG ↔ spectral-dimension` je **datově podložen na `d_s` kanálu**, oprávněně **barely → partially** jako `shared-math`.
- **`a₄` poměr (NEGATIV):** kontinuální `−18/11` je Diracův-obsah/křivostní racionál bez protějšku v **plochém skalárním** diskrétním spektru (`a₄ = 0` tam analyticky). Diskrétní `a₄/a₀` nekonverguje a nereprodukuje −18/11 — **honest negative**, ne selhání metody.

**Limity (honesty filter):**
- **Probe-závislost (F-001/F-002):** „NCG `d_s`" není jednoznačné číslo; BD-sonda dává 2, Pauli-Jordanova sonda dává 0. Výsledek `d_s = 2` platí pro BD-d'Alembertianovu sondu.
- **2D, finite-N, massless skalár.** Není to 4D kontinuální tvrzení. `a₀` má finite-N drift; `a₄` je čistý šum (3 seedy).
- **Plochý prostor:** test záměrně NEměří −18/11 (to by vyžadovalo zakřivené pozadí + spinový/Diracův obsah, mimo plochý causet). Měří **konzistenci** (totéž spektrum dává `d_s` i `a_{2k}`) a reprodukci `d_s = 2`.
- Na konečném causetu je každá algebra triviálně typu I_n; měříme N-trendy, ne typy.

**Hrana zůstává `barely → partially` jako `shared-math`** se zdůvodněním „týž `Tr e^{-σ D²}`; `d_s = 2` datově ověřeno z téhož spektra; kvantitativní vztah −18/11 ↔ `d_s` zůstává otevřený (vyžadoval by zakřivené pozadí / Diracův obsah)."

---

## Návrh F-041 + lib_proposals

**F-041 (navrhováno):** Z jednoho `D²`-spektra (modul symetrizace 2D Benincasa–Dowkerova d'Alembertiánu) na 2D Poissonem sprinklovaném causal diamondu se z téhož `Tr e^{-σ D²}` extrahují **konzistentně** (i) spektrální dimenze `d_s(σ)` a (ii) Seeley–DeWittovy koeficienty `a₀, a₂, a₄`. `d_s` plateau konverguje na analytickou 2D BD-sondovou hodnotu **2** (1.998 ± 0.044 při N = 2200, chyba 0.0024 < F-001 tol 0.06; plateau se rozšiřuje 1.83 → 2.25 dekád), zatímco Pauli-Jordanova sonda dává `d_s ≈ 0` (omezené spektrum) — F-001/F-002 probe-závislost zkonkretizována. Diskrétní `a₄/a₀` **nereprodukuje** kontinuální NCG racionál −18/11 (naměřeno −1.40 ± 4.25, per-seed −21.6 … +1.3, bez konvergence): na plochém causetu je `a₄ = 0` analyticky, takže koeficient je finite-N šum, ne Diracův-obsah/křivostní racionál. **Status: confirmed (smíšený — pozitiv na `d_s`, honest negativ na `a₄`).** Most `NCG ↔ spectral-dimension` je datově podložen na `d_s` kanálu jako sdílený heat kernel (barely → partially); −18/11 přes diskrétní flat-spectrum koeficienty NE. Scope: 2D, finite-N (N ≤ 2200), massless skalár, BD-sonda.

**lib_proposals:**
- `toe.spectral.heat_kernel_from_spectrum(d2, D, …) -> HeatKernelSpectrum` — diskrétní heat-trace extraktor: z pole vlastních čísel `D²` vrací `Z(σ)`, běh `d_s(σ)`, robustní `d_s` plateau (+ SE + šířku) a malo-σ koeficienty `a₀, a₂, a₄` se reporting poměry `a₂/a₀, a₄/a₀`. Doplňuje stávající `return_probability` / `spectral_dimension` (které pracují nad **spojitým** propagátorem `F(k)`) o **diskrétní-spektrovou** cestu, kterou H-C potřebuje (totéž spektrum → `d_s` i `a_{2k}`). Test `TestHeatKernelFromSpectrum` (6 testů): 2D Weyl → `d_s = 2`, `a₀ = Vol/(4π)`; 4D Weyl → `d_s = 4`; omezené spektrum → žádné UV škálování; normalizační invariance; flat `a₄ ≠ −18/11`.

---

*Zdroje (repo-present): F-001/F-002/F-003/F-012/F-014; `LOV-18-11-overlaps.md`; `lib/toe/spectral.py`, `ncg.py`, `causet.py`, `spectraltriple.py`; `core-data/link-predictions.json`. Externí konvence (citovat v originále): Benincasa–Dowker arXiv:1001.2725 (BD d'Alembertián); Sorkin–Yazdi arXiv:1611.10281 (`G_R = ½C`); Chamseddine–Connes hep-th/9606001, Vassilevich hep-th/0306138 (heat-kernel `a₄`); Carlip arXiv:1705.05417, Eichhorn–Mizera arXiv:1311.2530, Belenchia et al. arXiv:1507.00330 (spektrální dimenze causal setů). Žádné arXiv ID nevymyšleno.*
