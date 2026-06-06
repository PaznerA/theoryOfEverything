# `lib/` — kombinovatelná simulační knihovna `toe` (v0.3.0)

## Účel (krok 3 roadmapy)

Tato složka je **krok 3 roadmapy projektu**: destilace 20 ověřených `calc.py`
skriptů (`core-data/calculations/`) do jediné knihovny **kombinovatelných
funkcí**, jejichž skládáním lze podporovat nebo vyvracet teze o kvantové
gravitaci. Místo dvaceti monolitických skriptů máme nyní nejmenší znovupoužitelné
jednotky (sprinkling, kauzální struktura, Pauli-Jordanův operátor, SJ stav, SSEE,
spektrální dimenze, NCG spektrální akce), které jdou řetězit do nových
experimentů — to je primární lovná zóna pro hledání dosud nenalezených souvislostí
(`explored: barely`).

Knihovna `toe` je čistá: žádné I/O souborů, žádné globální RNG stavy, žádné
postranní efekty matplotlibu mimo `toe.viz` (který používá backend Agg). Importuje
se přes cestu (`lib/` na `sys.path` přes `app/tests/conftest.py`) — žádný
`setup.py` ani `pyproject.toml`.

## Princip

- **Vstupy = fyzikální veličiny.** Každá funkce bere fyzikální parametry
  (`N`, `dim`, `frac`, `kappa`, `rho`, frekvenční mřížky, metrika…), nikdy ad-hoc
  magické konstanty. Vše stochastické bere **explicitní `rng` / `seed`** jako
  povinný argument — plný determinismus z volajícího.
- **Výstupy = (hodnota, nejistota).** Funkce vrací malé nosné dataclassy z
  `toe.fits`, nikdy holý `float` nebo `tuple`:
  - `FitResult` — `value`, `se_regression` (reziduální OLS SE), `ci68_bootstrap`
    (percentily [16, 84] přes převzorkování seedů), `r2`;
  - `Measurement` — `value`, `se`, `ci68`, `n` (např. počet seedů);
  - `ExactResult` — přesná sympy `Rational`/`Expr`, `se_regression == 0`.
- **`validated` flag.** Každý nosič má volitelný `validated`. Jediný kontrolní bod
  `validate_against(value, target)` porovná spočtenou hodnotu proti zafixovanému
  cíli z `results.json` a nastaví `validated`. **Validační cíl se nikdy
  neoslabuje, aby prošel test.**
- **`formula-id` docstringy.** Každá veřejná funkce nese v docstringu tagy
  `Formula:` (ID vzorce z knowledge base), `Evidence:` (`VYPOCET-NN` + cesta ke
  zdrojovému `calc.py`) a `Conventions:` (load-bearing konvence + reference, např.
  Sorkin-Yazdi 1611.10281). Slouží ke křížovému propojení s pilíři a k ověřitelnosti.

## Mapa modulů (vrstvy A → B → C)

Importní vrstvy jsou striktní: modul smí importovat jen z **nižší** vrstvy;
`toe.fits` je list (neimportuje nic z `toe`).

| Vrstva | Modul | Obsah |
|---|---|---|
| **A1** | `toe.fits` | Nosné dataclassy (`FitResult`, `Measurement`, `ExactResult`) + fit-primitiva (`regression_se`, `bootstrap_slope_ci`, `powerlaw_fit`, `aic`, `aic_compare`, `validate_against`). Kořen závislostního grafu. |
| **A2** | `toe.causet` | Sprinkling oblasti (`sprinkle_diamond2d/_slab2d/_box4d/_slab4d/_wedge_box4d/_ds_static_patch2d`), kauzální/link struktura (`causal_matrix`, `link_matrix`), retardované Greenovy funkce (`green_retarded_2d/_4d`, `bd_dalembertian_inverse`, `bd_smeared_dalembertian_inverse`), Pauli-Jordanův operátor `pauli_jordan` + `causal_diagnostics`. **v0.3.0:** maticově-volná SPARSE cesta `causal_blocks_2d`, `idelta_operator_2d` (`LinearOperator` pro `iΔ` bez husté matice). |
| **A3** | `toe.spectral` | Heat-kernel return-probability (`return_probability`), běžící spektrální dimenze (`spectral_dimension`, `spectral_dimension_flow`), symbolický master (`ds_master_symbolic`) a klasifikátor `d_s_uv`. |
| **A4** | `toe.ncg` | Přesně-racionální NCG spektrální akce / heat-kernel `a4` čísla: `a4_heat_kernel_bracket`, `central_charges`, `a4_ratio`, `spectral_action_ratio`, `sector_ledger`, `str_count`, `lambda_induction_ledger`. |
| **A5** | `toe.viz` | Tenké matplotlib (Agg) prezentační panely: `powerlaw_panel`, `spectrum_plot`, `nl_vs_locus`, `radial_scan_plot`. Importuje **jen** `toe.fits`. |
| **B1** | `toe.sj` | Sorkin-Johnstonův stav (`sj_state`, `wightman`, `SJState`) a observably v rotujících prostoročasech: `asymmetry_causal`, `asymmetry_wightman`, `superradiant_weight`, `positive_subspace_overlap`. **v0.3.0:** iterativní top-k stav `sj_state_sparse` (+ nosič `SJStateSparse`) přes `scipy.sparse.linalg.eigsh`. |
| **C1** | `toe.entropy` | SSEE přes zobecněný eigenproblém: `kappa_2d`, `n_max_area_law`, `rank_at_cutoff`, `ssee`, scaling driver `ssee_scaling`, site-basis modulární jádro `modular_kernel` (+ nosič `ModularKernel`). **v0.3.0:** truncovaná SSEE z k-mode dat `ssee_sparse`. |
| **C2** | `toe.vntype` | Proxy von Neumannova typu pro III₁ → II přechod při truncaci: `modular_spectrum`, `pile_up`, `trace_scaling`, `type_proxies`, `saturation_discriminator`. |

Veřejné API je re-exportováno z `toe/__init__.py` (`__version__ = '0.3.0'`,
`__all__` se všemi 64 veřejnými jmény) — `import toe; toe.powerlaw_fit(...)`
funguje přímo.

## Jak spouštět testy

Testy žijí v `app/tests/` (`test_toe_<modul>.py` + předchozí `test_environment.py`
a `test_reproduction.py`). Vždy s headless backendem (`MPLBACKEND=Agg`).

**Na hostu:**

```bash
cd /Users/pazny/projects/theoryOfEverything
MPLBACKEND=Agg python3 -m pytest app/tests -v
```

Rychlá sada (smoke prostředí + 6 sub-sekundových reprodukcí + celá `toe`)
proběhne za ~25 s. Plná reprodukce všech 20 výpočtů (~50 min) se zapíná
`FULL_REPRO=1`.

**Přes Docker (reprodukovatelné, pinované verze):**

```bash
docker compose run --rm test                       # rychlá sada
docker compose run --rm -e FULL_REPRO=1 test       # + plná reprodukce
```

(Služba `test` je definovaná v `app/docker-compose.yml`, příkaz `pytest app/tests -v`.)

## Příklady kompozice

### 1. SSEE scaling: sprinkle → iDelta → SJ stav → SSEE → power-law fit

Kanonický řetězec napříč vrstvami A → B → C → A (kompletní spustitelná verze je
`lib/examples/demo_pipeline.py`):

```python
import numpy as np
from toe.causet import sprinkle_diamond2d, green_retarded_2d, pauli_jordan
from toe.sj import sj_state
from toe.entropy import kappa_2d, ssee
from toe.fits import powerlaw_fit

Ns, n_seeds, frac = [120, 200, 320, 500], 4, 0.5
per_seed_S = np.zeros((len(Ns), n_seeds))

for i, N in enumerate(Ns):
    kappa = kappa_2d(N)                              # C1: UV cutoff sqrt(N)/(4 pi)
    for s in range(n_seeds):
        rng = np.random.default_rng(7_000_000 + 1000 * N + s)
        coords = sprinkle_diamond2d(N, rng)          # A2: null souřadnice (u, v)
        # kauzální order v null konvenci: y < x  iff  u_y<=u_x & v_y<=v_x
        u, v = coords[:, 0][:, None], coords[:, 1][:, None]
        C = ((coords[:, 0][None, :] <= u) & (coords[:, 1][None, :] <= v)).astype(float)
        np.fill_diagonal(C, 0.0)
        iDelta = pauli_jordan(green_retarded_2d(C))  # A2: i (G_R - G_R^T)
        state = sj_state(iDelta)                      # B1: SJ Wightman W
        sub = np.where((np.abs(coords[:, 0]) <= frac) & (np.abs(coords[:, 1]) <= frac))[0]
        per_seed_S[i, s] = abs(ssee(state.W, iDelta, sub, kappa=kappa).value)  # C1

fit = powerlaw_fit(np.array(Ns, float), per_seed_S.mean(axis=1),
                   resamples=per_seed_S, n_boot=1000)   # A1
print(fit.value, fit.se_regression, fit.ci68_bootstrap)  # a ~ 0.29 (saturující, type-II)
```

Pohodlnější ekvivalent celého řetězce je driver `ssee_scaling`:

```python
from toe.causet import sprinkle_diamond2d
from toe.entropy import ssee_scaling

fit = ssee_scaling(sprinkle_diamond2d, [120, 200, 320, 500],
                   frac=0.5, n_seeds=4, seed_base=7_000_000, truncate="kappa")
```

### 2. NCG `a4` poměr c/(−a) = −18/11 (index-protected)

```python
from toe.ncg import a4_ratio, spectral_action_ratio

r = a4_ratio(sector="fermion")          # přesně -18/11 pro libovolný počet Weylů
print(r.value, r.validated)             # -18/11  True

# stejné heat-kernel číslo ze spektrální akce Chamseddine-Connes:
print(spectral_action_ratio().value)    # -18/11 (f0 se zkrátí)
```

### 3. Klasifikátor UV spektrální dimenze `d_s_uv`

```python
from toe.spectral import d_s_uv

print(d_s_uv(z=1, D=4).value)                          # 4   (GR: d_s = D)
print(d_s_uv(z=2, D=4).value)                          # 2   (Stelle / asympt. bezpečnost)
print(d_s_uv(z=3, D=4, convention="anisotropic").value)  # 2   (Hořava: 1 + D_space/z = 1+3/3)
```

Numerický flow (IR → UV) pro libovolný inverzní propagátor:

```python
import numpy as np
from toe.spectral import spectral_dimension_flow
ds = spectral_dimension_flow(lambda k: k**2 + k**4, D=4)  # Stelle: D → 2
```

## Spuštění ukázky

```bash
cd /Users/pazny/projects/theoryOfEverything
MPLBACKEND=Agg PYTHONPATH=lib python3 lib/examples/demo_pipeline.py
```

Vypíše scaling tabulku, fit (`a ≈ 0.29`, R² ≈ 0.98) a uloží log-log panel do
`lib/examples/demo_output.png`. Doba běhu < 1 s (cíl < 60 s).

## CHANGELOG

### v0.3.0 — SPARSE / ITERATIVNÍ cesta (velké N pro SJ + SSEE, N ~ 1e4)

Paměťově úsporná, **maticově-volná** cesta, aby SJ + SSEE pipeline dosáhly
`N ~ 1e4` (2D hustota sprinklingu `rho ~ 1e3–1e4`) **bez** materializace husté
float matice `iΔ` — potřebné pro **H5g-2** (A/4 cap) a **VYPOCET-19 Part-3**
traciální probe. Čtyři nová veřejná jména, vrstvená přesně jako jejich husté
protějšky:

- **`toe.causet.causal_blocks_2d(coords, *, dtype=np.float32, block=2048)`** —
  2D kauzální matice sestavená po blocích (řazení podle `u` + per-blok null-cone
  test), uložená jako jediné pole `dtype` (výchozí `float32`). Přechodný boolean
  buffer je `block x N`, ne `N x N`. Vrací `(C, perm)`; `C` je bit-identická s
  `causal_matrix` až na permutaci `perm`.
- **`toe.causet.idelta_operator_2d(coords, *, dtype=np.float32, block=2048)`** —
  maticově-volný hermitovský Pauli-Jordanův operátor jako
  `scipy.sparse.linalg.LinearOperator` (`(N, N)`, `complex128`). 2D Green
  `G_R = (1/2)C` je IMPLICITNÍ: `iΔ @ x = (i/2)(C @ x - C^T @ x)` jsou dvě
  bool-blok GEMV. Uloží se jen JEDNA float kopie `C` (+ souvislá transpozice).
  `dtype=float64` pro přesnou cestu (shoda 1e-14 vs husté), `float32` pro velké
  N (~1e-6, půlí paměť, ~2× BLAS).
- **`toe.sj.sj_state_sparse(idelta_op, k, *, rng, which='LM', tol=0, …)`** —
  top-k SJ spektrum přes `scipy.sparse.linalg.eigsh` (`which='LM'`). Spektrum
  `iΔ` je `+/-` párované, takže `'LM'` vrátí vyvážených top `~k/2` kladných +
  `~k/2` záporných — vše, co SSEE truncace (`|λ| > kappa`) potřebuje.
  **Determinismus**: startovní vektor eigsh `v0` se odvodí z **povinného** `rng`,
  takže restart se stejným seedem je bit-identický. Vrací nosič `SJStateSparse`
  (`W` se záměrně nematerializuje).
- **`toe.entropy.ssee_sparse(sj_sparse, sub_idx, *, kappa=None, n_max=None, …)`**
  — truncovaná SSEE rekonstruovaná z k-mode SJ dat (ponech `|λ| > kappa` resp.
  top `n_max`, postav truncované `(iΔ, W)` jen z těchto modů, pak stejný
  zobecněný eigenproblém `W_O v = mu iΔ_O v`, `S = sum_mu mu ln|mu|` jako husté
  `ssee`). Předpisy `n_max` (`n_max_area_law`) znovupoužity.

**Zvolená cesta — implicitní `eigsh` ZVÍTĚZIL, fallback na husté
`eigh(subset_by_index=...)` nebyl potřeba.** `eigsh(which='LM')` řeší extrémní
(magnitudou největší) konce spektra, což je přesně tam, kde žije SSEE obsah, a
vyhne se špatně podmíněnému INTERIOR-eigenvalue režimu, který by fallback
vynutil. Konverguje rychle a na strojovou přesnost.

**Validace (overlap velikosti, `app/tests/test_toe_sparse.py`, < 90 s):** při
`N ∈ {1000, 2000}` sparse cesta odpovídá husté — top-k vlastní čísla rel. rozdíl
`< 1e-8` (naměřeno `~3e-15`); truncovaná SSEE `< 1e-6` (naměřeno `~1e-14`); `+/-`
párovací + hermitovský invariant na náhodných vektorech; determinismus. Jeden
**scaling smoke**: `N=8000`, `k=600` eigsh (float32) doběhne ~32 s (< 120 s),
paměť ~0.5 GB (< 2 GB), top `|λ|` sleduje trend `max|λ| ~ 0.21 N`. Celá sada
zelená (`MPLBACKEND=Agg python3 -m pytest app/tests -q`).

### v0.2.0 — zvednutí 5 návrhů z VYPOCET-22 (codim-2 modulární tok)

Pět připravených návrhů (`lib_proposals` v
`core-data/calculations/modular-flow-codim2/results.json`) bylo přeneseno
z lokálního `helpers.py` do knihovny. Každý nese validační testy v `app/tests/`
(celá sada zelená: 288 prošlo, 14 přeskočeno, 1 xfailed).

- **`toe.causet.sprinkle_wedge_box4d`** (vrstva A) — t-symetrický 4D Minkowského
  box, jehož řez `O={x>0}` má entanglement plochu na **codim-2 hraně**
  `E={t=0,x=0}` (plochá 2-rovina = H5g-3 „joint“ Rindlerova klínu `W={x>|t|}`).
  Slab kontrola bez jointu používá stejný matchovaný box. Test: invariant
  párování `iΔ` `±` `pairing_residual_rel < 1e-12`.
- **`toe.causet.bd_smeared_dalembertian_inverse`** (vrstva A) — rozmazaný
  (non-lokální) Benincasa-Dowker d'Alembertián `G_R = B_eps^{-1}`, eps-sourozenec
  ostré `bd_dalembertian_inverse(…,dim=4)` (VYPOCET-20-validovaný objekt;
  `alpha4=-4/√6`, `beta4=4/√6`, `f4(n,eps)`; Aslanbeigi-Saravani-Sorkin
  1305.2588). Test reprodukuje zafixované `wedge_cond_B[0] = 15577.092005018936`
  (N=800, 3 seedy, eps=0.6) na `rtol 1e-6`, < 5 s.
- **`toe.sj.sj_state(…, rel_floor=None)`** (vrstva B) — **relativní** spektrální
  práh `rel_floor*λ_max` pro špatně podmíněné BD-inverze (`cond ~ 1e4–1e6`).
  **Výchozí `None` zachovává původní absolutní `tol` chování bit-identicky**
  (doloženo testem `array_equal` na 2D diamantu i celou stávající sadou).
- **`toe.entropy.modular_kernel`** (vrstva C) — expozice **site-basis**
  jednočásticového modulárního jádra `K(x,y)` (nosič `ModularKernel`) vedle
  skaláru `S` z `ssee`; potřebné pro lokalitní diagnostiku ve VYPOCET-18/20/22.
  Test: skalár `mk.S` je konzistentní s `ssee(...).value` na stejném řezu
  (trace-relace, `rtol 1e-7`).
- **`toe.viz.nl_vs_locus`** (vrstva A, importuje jen `toe.fits`) — panel
  „non-lokalita vs vzdálenost k locusu“; znaménko sklonu odečte koncentraci
  (záporný = ke 2D-rohu, kladný = od null-špičky).

**Refaktor `calc.py`:** `modular-flow-codim2/calc.py` nyní importuje zvednuté
funkce z `toe` místo `helpers.py`; přegenerovaný `results.json` je **bit-for-bit
identický** s commitnutým (kromě `runtime_s`). `helpers.py` si ponechává jen
lokalitní diagnostiky (`locality_profile`, `nonlocal_fraction`,
`offdiag_slope_subset`, `nl_vs_edge_profile`, `diag_weight_vs_distance`,
`box4d_volume`).

### v0.1.0 — destilace 20 ověřených `calc.py` skriptů (krok 3 roadmapy)

Iniciální knihovna: 8 modulů ve vrstvách A → B → C, 54 veřejných jmen.
