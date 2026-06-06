# `toe` — composable simulation library: ARCHITECTURE / BUILDER CONTRACT

> Roadmap step 3. This is the **binding contract** for the builder agents that
> implement each module. English code + identifiers (project policy); Czech
> README prose is produced separately and is out of scope here.
>
> The library is distilled from the **20 bit-reproducible** `calc.py` scripts
> (`reports/2026-06-06-review.md` §f: 20/20 bitwise-identical reproduction).
> The architectural principle is `reports/2026-06-06-review.md` §(g):
>
> - **input** = physics parameters (never ad-hoc numerical magic constants);
> - **output** = a `(value, uncertainty)` pair — regression SE *or* bootstrap CI;
> - **flag** = `validated: bool` = does this reproduce the committed
>   `core-data/calculations/*/results.json`.
>
> Every public function is the smallest composable unit that still maps cleanly
> `formula -> code`. The builder MUST NOT widen a function's responsibility.

---

## 0. Global conventions (apply to ALL modules)

### 0.1 Result dataclasses (the `(value, se/ci, validated)` convention)

Put these in `toe/fits.py` (module A1, the dependency root) and import them
everywhere. They are **plain `@dataclass` objects**, no behaviour beyond a
couple of cheap derived properties. `value` is always a Python `float` (or a
`sympy.Rational`/`sympy.Expr` for the exact ncg module — see 0.2).

```python
from dataclasses import dataclass, field
from typing import Optional

@dataclass
class FitResult:
    """A power-law / OLS fit outcome with honest uncertainty.
    Mirrors sj-vn-type/calc_uncertainty.py exactly."""
    value: float                       # central estimate (e.g. log-log slope)
    se_regression: float               # residual-based OLS SE of the slope
    ci68_bootstrap: tuple[float, float]  # (lo, hi) = [16,84] pct over resamples
    r2: float                          # coefficient of determination of the fit
    intercept: float = 0.0
    n_boot_used: int = 0
    boot_std: float = 0.0
    n_points: int = 0
    validated: Optional[bool] = None   # set by caller vs results.json target

    @property
    def ci_width(self) -> float:
        return self.ci68_bootstrap[1] - self.ci68_bootstrap[0]

@dataclass
class Measurement:
    """Generic scalar observable with an uncertainty, for the stochastic
    modules (causet/sj/entropy/vntype) that do not themselves run a powerlaw
    fit but still must return (value, uncertainty)."""
    value: float
    se: float = 0.0                    # std-error (e.g. std/sqrt(n_seeds))
    ci68: Optional[tuple[float, float]] = None
    n: int = 0                         # sample size (e.g. n_seeds)
    validated: Optional[bool] = None

@dataclass
class ExactResult:
    """Exact-arithmetic outcome for the sympy ncg/spectral-table functions.
    `value` is a sympy object (Rational/Expr); se is identically 0."""
    value: object                      # sympy.Rational | sympy.Expr
    se_regression: float = 0.0         # always 0.0 (exact)
    validated: Optional[bool] = None

    @property
    def as_float(self) -> float:
        import sympy as sp
        return float(sp.N(self.value))
```

Rules:
- A function returning a `(value, uncertainty)` pair MUST return one of these
  dataclasses, never a bare tuple or dict. Builders are forbidden from adding
  methods that do physics — derived properties must be pure formatting.
- `validated` is `None` until a comparison against a `results.json` target is
  performed (the tests do this; production callers may set it too).
- A `validate_against(result_value, target, ...)` free helper lives in
  `toe/fits.py` (see A1) so every module flips the flag the same way.

### 0.2 Docstring convention (MANDATORY for every public function)

Each public function's docstring MUST contain, in this order:

1. One-line summary of what it computes.
2. A `Formula:` line citing **formula id(s) from `core-data/formulas.json`**
   verbatim, e.g. `Formula: pauli-jordan, ssee-formula`.
3. An `Evidence:` line citing the originating **VYPOCET / calc directory**,
   e.g. `Evidence: VYPOCET-12 (core-data/calculations/sj-vn-type/calc.py)`.
4. A `Conventions:` line with the literature arXiv id pinned in the source
   `calc.py` (e.g. `Sorkin-Yazdi 1611.10281 eq.9: G_R = (1/2) C`).
5. `Args` / `Returns` (Returns must name the dataclass).

The exact formula ids each module is required to cite are listed per-module
below under **Docstring formula ids**. These ids are all verified present in
`core-data/formulas.json` (247 formulas). **Never invent a formula id**; if a
needed id is missing, the builder stops and flags it (project policy: no
unverifiable references).

### 0.3 Determinism / seeds

Every stochastic function takes an explicit RNG seed (or a
`numpy.random.Generator`) as a **required** argument — never an implicit global.
Convention inherited from the calc scripts: callers pass
`np.random.default_rng(seed)`. The sj-vn-type seed scheme
`7_000_000 + 1000*N + s` is reproduced by the entropy/vntype validation tests;
those tests pass the seeds explicitly.

### 0.4 No file I/O, no plotting side-effects in compute modules

Compute modules (A1–A4, B1, C1, C2) MUST be pure: no `json.dump`, no
`results.json` writing, no `matplotlib`. Only `toe/viz.py` (A5) imports
matplotlib, and it sets the **Agg** backend at import time (`matplotlib.use("Agg")`)
and returns `Figure` objects (optionally saving to a passed `save` path).
This fixes the §f hidden-path / hidden-run-order defects by construction: no
module reads another calc dir's `results.json`.

---

## 1. Dependency layers (NO CYCLES)

```
Layer A (independent):  fits, causet, spectral, ncg, viz
Layer B (needs A):      sj           ->  imports causet (+ fits)
Layer C (needs B):      entropy      ->  imports sj, causet (+ fits)
                        vntype       ->  imports sj, causet, fits
```

Import rules — enforced by `app/tests/test_toe_imports.py` (builder writes it):

- **A** modules may import only stdlib, numpy, scipy, sympy, matplotlib(viz only),
  and `toe.fits` (the dataclasses + fit helpers are the shared root; `fits` itself
  imports nothing from `toe`).
- **B** (`sj`) imports `toe.causet` and `toe.fits`. NOT `entropy`/`vntype`.
- **C** (`entropy`, `vntype`) import `toe.sj`, `toe.causet`, `toe.fits`. They MUST
  NOT import each other (siblings); shared helpers go down into `sj` or `causet`.
- `viz` (A5) imports `toe.fits` only (for the dataclass types it plots); it must
  not import causet/sj/entropy so it stays a thin presentation layer.
- No module imports `toe` (the package `__init__`) — always import the submodule
  directly, to keep the empty-`__init__` placeholder valid during the build.

---

## 2. Modules

For each module: file, public signatures + return types, docstring formula ids,
and **VALIDATION TARGETS** (concrete numbers read from the committed
`results.json` — exact for sympy, machine-precision for invariants, small-N
smoke with generous tolerance for stochastic, each test < 60 s).

---

### A1 — `toe/fits.py`   (layer A, dependency root)

Houses the Result dataclasses (§0.1) **and** the fit primitives. Follows
`core-data/calculations/sj-vn-type/calc_uncertainty.py` exactly (residual-based
OLS SE + ≥1000-resample across-seed bootstrap, [16,84] percentiles).

**Signatures**

```python
def powerlaw_fit(x, y, *, sig=None, n_boot=1000, seed=20260606,
                 resamples=None) -> FitResult
    # OLS slope of log(y) vs log(x). se_regression = residual-based
    # sqrt(SSR/(n-2) * (A^T A)^-1[0,0]) (calc_uncertainty.regression_se).
    # ci68_bootstrap: if `resamples` (an (n_curves, n_points) array of repeated
    # measurements, e.g. per-seed y-curves) is given, do the across-seed
    # bootstrap of the slope with >=1000 resamples drawn WITH REPLACEMENT and
    # take [16,84] percentiles (calc_uncertainty.bootstrap_ci). Otherwise the
    # CI degenerates to (value, value) and n_boot_used=0. r2 from the fit.

def regression_se(x, y) -> tuple[float, float, float]
    # (slope, intercept, se_slope) — the honest single-fit SE primitive.

def bootstrap_slope_ci(per_sample, x, *, transform="mean",
                       n_boot=1000, seed=20260606) -> tuple[float, float, float]
    # ([16] pct, [84] pct, boot_std). per_sample shape (n_points, n_samples);
    # transform in {"mean","cv"} exactly as calc_uncertainty.bootstrap_ci.

def aic(rss, n, k) -> float
    # AIC = n*ln(rss/n) + 2k  (Gaussian-residual form used by sj-threshold-scan).

def aic_compare(*models) -> dict
    # models: iterable of (name, rss, n, k) OR (name, aic_value). Returns
    # {"aic": {name: val}, "best": name, "delta_aic": {name: val-best_val}}.
    # Sign convention matches sj-threshold-scan delta_AIC_E_minus_S.

def validate_against(value, target, *, rtol=1e-9, atol=0.0,
                     exact=False) -> bool
    # The single chokepoint that sets `validated`. exact=True -> sympy ==
    # (for ncg / spectral-table). Numeric -> math.isclose with rtol/atol.
```

**Docstring formula ids**: `spectral-dimension-fit` (the measured-running-fit
prototype), and reference the AIC discriminator evidence inline (no formula id;
cite VYPOCET only). `powerlaw_fit` cites Evidence VYPOCET-12 +
`calc_uncertainty.py`.

**VALIDATION TARGETS** (`sj-vn-type/uncertainty.json` + `results.json`):
- `powerlaw_fit` on the committed `entropy_trace_full` mean-S-vs-N curve →
  `value = 1.0433381703439863` (results.json `exponent_a`); with the 8-seed
  resamples → `se_regression = 0.012687944964902706`,
  `ci68_bootstrap ≈ [1.0238418384973422, 1.0632126168887104]`.
  Tolerance: value exact to 1e-9 (deterministic OLS); SE to 1e-9; CI endpoints
  to **±0.01** (bootstrap RNG: seed 20260606, ≥1000 resamples — reproducible).
- `entropy_trace_trunc` → `value = 0.17243056092717168`, `se ≈ 0.011585364915`.
- `CV_S_trunc_powerlaw` → `value = -0.7135270246444776`, `se ≈ 0.08165431269`,
  `ci68 ≈ [-0.9103, -0.5107]` (±0.02).
- `aic_compare` on the committed sj-threshold-scan a=0.6 pair
  (`model_E.AIC=4757.534081426667`, `model_S.AIC=4315.942138405724`) →
  `delta_aic[model_E] = 441.5919430209433` (exact to 1e-9, deterministic);
  `best == "model_S"`. a=0.9 pair → `delta = 4216.307763406736`.
  (NB: review §g prose says ">3894 for a=0.6"; the **committed** results.json
  is 441.59 for a=0.6 / 4216.31 for a=0.9 — tests reproduce the committed JSON.)
- `validate_against(1.0433381703439863, 1.0433381703439863)` → `True`.

---

### A2 — `toe/causet.py`   (layer A)

Sprinkling region builders + causal/link structure + retarded Green +
Pauli-Jordan. Conventions are the union of `ssee-diamond` (2D), `ssee-4d` (4D
link-matrix Green), `sj-rotating-btz` / `sj-desitter-type` (tilted-cone + sech²).
**Seeds are explicit required args everywhere.**

**Signatures**

```python
# --- region builders: return (N,dim) float coords; rng REQUIRED ---
def sprinkle_diamond2d(N, rng, *, t_half=1.0) -> np.ndarray
def sprinkle_slab2d(N, rng, *, t_extent, x_extent) -> np.ndarray
def sprinkle_box4d(N, rng, *, half=1.0) -> np.ndarray
def sprinkle_slab4d(N, rng, *, t_extent, l_space) -> np.ndarray
def sprinkle_ds_static_patch2d(N, rng, *, l=1.0, rstar_box,
                               t_extent) -> np.ndarray
    # de Sitter static patch, PROPER measure dN ~ sech^2(r*/l) dt dr*
    # (sj-desitter-type: inverse-CDF sample r* ~ sech^2). Conformal factor
    # Omega^2 = sech^2(r*/l). Returns (t, r*) coords.

# --- causal structure ---
def causal_matrix(coords, *, metric=None, time_orientation=None) -> np.ndarray
    # C[x,y]=1 iff y precedes x (y in causal past of x), diag 0.
    # 2D-conformal default: prec = (u_y<=u_x)&(v_y<=v_x) on lightcone coords.
    # metric != None -> tilted-cone order h(D,D)<=0 & h(T,D)<0 (rotating BTZ/Kerr,
    # sj-rotating-btz.causal_matrix_section).
def link_matrix(C) -> np.ndarray
    # nearest-neighbour (irreducible) links: L = C with transitive relations
    # removed (ssee-4d.link_matrix), for the 4D BD Green.

# --- retarded Green + Pauli-Jordan ---
def green_retarded_2d(C) -> np.ndarray
    # G_R = (1/2) C  (2D massless, conformally invariant).
def green_retarded_4d(L, rho) -> np.ndarray
    # K_R = a L, a = sqrt(rho)/(2*pi*sqrt(6))  (Johnston 0909.0944 eq.17, m=0,
    # link convention). rho = N/volume.
def bd_dalembertian_inverse(C, rho, dim) -> np.ndarray
    # discrete Benincasa-Dowker d'Alembertian and its inverse giving G_R for the
    # massive/curved generalisation (ssee-bd-4d / modular-flow-bd-4d). For the
    # massless 2D limit this returns (1/2)C.
def pauli_jordan(G_R) -> np.ndarray
    # iDelta = i*(G_R - G_R^T). Hermitian, real +/- paired spectrum.
    # (For 2D pass green_retarded_2d(C); equals i*(1/2)(C - C^T).)
def causal_diagnostics(iDelta, *, tol=1e-9) -> dict
    # {n_positive, n_negative, n_zero, trace, pairing_residual_abs,
    #  pairing_residual_rel, max_abs_eig} (sj-rotating-btz.spectrum_health).
```

**Docstring formula ids**: `pauli-jordan` (for `pauli_jordan`, `green_retarded_*`,
`bd_dalembertian_inverse`), `swerves-diffusion` only if the BD swerve term is
exposed (else omit). Evidence: VYPOCET-04 (ssee-diamond), VYPOCET-06 (ssee-4d),
VYPOCET-08 (sj-rotating-btz), VYPOCET-19 (sj-desitter-type).

**VALIDATION TARGETS**:
- **Machine-precision invariant (iDelta ± pairing)**: build
  `sprinkle_diamond2d(N=300, rng=default_rng(0))` → `causal_matrix` →
  `green_retarded_2d` → `pauli_jordan`; `causal_diagnostics` must give
  `pairing_residual_rel < 1e-13` and `|trace| < 1e-12` (iDelta is Hermitian with
  exactly ± paired eigenvalues; antisymmetry of Δ is exact in float).
  Cross-check against committed `sj-rotating-btz/results.json`
  `ergoregion_pairing_residual_rel = 4.572344238792827e-16` (same construction
  family) — assert `< 1e-13`.
- **4D Green coefficient**: `green_retarded_4d(L, rho)` must equal
  `(sqrt(rho)/(2*pi*sqrt(6))) * L` elementwise to 1e-15 (the coefficient is the
  load-bearing convention from `ssee-4d/calc.py` line 184).
- **sech² measure smoke**: `sprinkle_ds_static_patch2d(N, ...)` r*-marginal
  histogram must be monotone-decreasing in |r*| (sech² weighting), and the
  achievable point budget caps — qualitative check; quantitative cap is tested
  in C2/entropy.
- **Diamond causal-link fraction smoke** (N=400, seed 0): link fraction of the
  2D diamond C is ≈ 0.25 ± 0.05 (uniform diamond has ~1/4 causally-related
  ordered pairs); generous tolerance, runs < 5 s.

---

### A3 — `toe/spectral.py`   (layer A)

Heat-kernel return probability, running spectral dimension, and the
`d_s_uv` classifier that reproduces the `ds-classification` master table.

**Signatures**

```python
def return_probability(sigma, F, D) -> float
    # P(sigma) = INT d^D k exp(-sigma F(k)); robust log-sum-exp radial integral
    # (ds-classification._logP_radial). F is callable k->F(k).
def spectral_dimension(sigma, F, D, *, h=1e-2) -> float
    # d_s(sigma) = -2 d ln P / d ln sigma (central diff in ln sigma).
def spectral_dimension_flow(F, D, *, sigmas=None) -> np.ndarray
    # vector d_s over a log sigma grid (IR->UV), default np.logspace(6,-10,90).
def d_s_uv(z, D, *, probe="heat_kernel", convention="isotropic") -> ExactResult
    # The CLASSIFIER. Returns the EXACT rational d_s^UV:
    #   isotropic master:  d_s = D / gamma,  gamma = z  (F ~ k^{2z} UV)
    #   horava (convention="anisotropic"): d_s = 1 + D_space/z, D_space = D-1
    #   probe="random_walk": ">D (increases)" sentinel (qualitative row)
    # value is sympy.Rational (or the string sentinel for random_walk).
def ds_master_symbolic() -> "sympy.Expr"
    # symbolic check: returns sympy expr that simplifies to D/gamma
    # (ds-classification.symbolic_master).
```

**Docstring formula ids**: `return-probability-uv-ir`, `spectral-dimension-def`,
`spectral-dimension-flow`, `spectral-dimension-running`. Evidence: VYPOCET-13
(ds-classification).

**VALIDATION TARGETS** (`ds-classification/results.json`, **EXACT** for the
classifier rationals; numeric ±0.06 for the flow, matching the source's own
`close()` tolerance):
- `ds_master_symbolic()` simplifies to `D/gamma` (symbolic equality).
- Classifier exact rationals (`d_s_uv(...).value == sympy.Rational(...)`):
  - GR `z=1, D=4` → `4`; IR also `4`.
  - Horava `z=2, D=4, convention="anisotropic"` → `5/2`; `z=3` → `2`; IR → `4`.
  - Stelle / AS / CST-d'Alembertian / multifractional UV → `2`.
  - CST random-walk → sentinel `">D (increases)"` and `.as_float` smoke `= 8.0`.
- Numeric flow smoke (±0.06): GR UV `≈ 4.0`; Horava z=3 UV `≈ 2.0`, IR `≈ 4.0`;
  Stelle UV `≈ 2.0`; CST random-walk UV `> 4.1`. Use a coarse sigma grid so the
  test runs < 60 s (the full 90-point flow over 8 propagators is the slow part —
  test only the 3–4 propagators above, or a reduced grid).

---

### A4 — `toe/ncg.py`   (layer A)   — EXACT sympy, the reference/unit-test bedrock

Exact-rational heat-kernel a4 coefficients, the index-protected `-18/11`, the
sector ledger, supertrace (STr) counting, and the Λ-induction ledger. Every
return is `ExactResult` (sympy), `se = 0`. This is the cleanest formula→code
mapping in the project (review §g item 1).

**Signatures**

```python
def a4_heat_kernel_bracket(field) -> dict
    # field in {"scalar","dirac","vector"}. Returns exact {"C2":Rational,
    # "E4":Rational, "R2":Rational} a4(D^2) bracket coefficients
    # (a4-graviton-index.a4_bracket; Vassilevich hep-th/0306138 eq.4.28).
def central_charges(n0, n_weyl, n1) -> tuple["Rational","Rational"]
    # exact (a, c) for a free-field content (a4-anomaly-matching.central_charges;
    # Duff 2003.02688 Table 1).
def a4_ratio(n_fermions=1, *, with_nu_R=False, sector="fermion") -> ExactResult
    # coeff(C^2)/coeff(Euler) = c/(-a). sector="fermion" -> EXACTLY -18/11 for
    # any fermion count (index-protected, nu_R-independent). sector="full_SM"
    # -> the content-dependent rational (-1698/1991 noNu / -219/253 withNu).
def spectral_action_ratio() -> ExactResult
    # alpha0/tau0 = (-3 f0/10 pi^2)/(11 f0/60 pi^2) = -18/11 (f0 cancels).
def sector_ledger(*, with_nu_R=False) -> dict
    # the SM (a,c) ledger per sector {fermions_only, full_SM} as exact rationals
    # (a4-anomaly-matching central_charges_totals).
def str_count(content) -> "Rational"
    # supertrace Tr(1_F) / graded counting over a finite-Dirac content
    # (a4-graviton-index STr / N=Tr(1_F)).
def lambda_induction_ledger() -> dict
    # exact a0:a2:a4 cosmological/Einstein-Hilbert ledger; reports
    # ratio_a0_over_a2_per_mode=12, ratio_a4_c_over_minus_a=-18/11, and the
    # N-independence-is-DEGENERATE verdict (lambda-induced Q3).
```

**Docstring formula ids**: `spectral-action-formula`, `heat-kernel-action`,
`gravity-terms`, `trace-anomaly-4d`, `lambda-prediction`. Evidence: VYPOCET-11
(a4-anomaly-matching, a4-graviton-index), VYPOCET-17 (lambda-induced).

**VALIDATION TARGETS** (**EXACT sympy equality**, `se == 0`):
- `a4_ratio(sector="fermion").value == sympy.Rational(-18, 11)` for
  `n_fermions ∈ {1, 45, 48}` and `with_nu_R ∈ {False, True}` (all give -18/11).
- `spectral_action_ratio().value == sympy.Rational(-18, 11)`.
- `central_charges(0, 1, 0) == (Rational(11,720), Rational(1,40))`  (one Weyl).
- `central_charges(4, 48, 12)` (full SM + νR) →
  `(Rational(253,90), Rational(73,30))` (a, c).
- `a4_ratio(sector="full_SM", with_nu_R=False).value == Rational(-1698,1991)`;
  `with_nu_R=True` → `Rational(-219,253)`.
- `a4_heat_kernel_bracket("scalar")` → `{"C2":1/120,"E4":-1/360,"R2":0}`;
  `"dirac"` → `{"C2":-1/20,"E4":11/360,"R2":0}`.
- `lambda_induction_ledger()["ratio_a0_over_a2_per_mode"] == 12` and
  `["ratio_a4_c_over_minus_a"] == Rational(-18,11)`.
- Each assertion exact; whole module test runs < 5 s.

---

### A5 — `toe/viz.py`   (layer A, presentation — Agg only)

Thin matplotlib helpers. `matplotlib.use("Agg")` at import. Every function
**returns a `Figure`** and optionally writes it when `save` is given. No physics,
no compute — consumes the dataclasses from A1.

**Signatures**

```python
def powerlaw_panel(fit: FitResult, x, y, *, save=None, label="",
                   ax=None) -> "matplotlib.figure.Figure"
    # log-log scatter + fitted line + shaded CI68 band from fit.ci68_bootstrap.
def spectrum_plot(eigvals, *, kind="loglog", save=None,
                  ax=None) -> "matplotlib.figure.Figure"
    # SJ / iDelta positive spectrum (rank vs |lambda|), continuum-1/k overlay.
def radial_scan_plot(r, observable, *, ergo_band=None, save=None,
                     ax=None) -> "matplotlib.figure.Figure"
    # observable vs radius with optional shaded ergoregion (sj-rotating-btz
    # PART C correlation_asymmetry plot).
```

**Docstring formula ids**: none required (presentation layer); cite the Evidence
calc whose figure each helper generalises (VYPOCET-08/12/13).

**VALIDATION TARGETS**: smoke only (no numerics) — each returns a `Figure` with
≥1 `Axes`, the CI band spans `fit.ci68_bootstrap`, and `save=tmp_path/...` writes
a non-empty PNG. Runs < 5 s. (Builder uses a synthetic `FitResult`, not a real
sprinkle, to keep viz tests independent of the stochastic modules.)

---

### B1 — `toe/sj.py`   (layer B → imports `causet`, `fits`)

SJ state from `iDelta`, Wightman, asymmetry observables, and the superradiant
eigenvector-overlap weight.

**Signatures**

```python
def sj_state(iDelta, *, tol=1e-12) -> "SJState"
    # SJState = small dataclass {eigvals, eigvecs, pos_spectrum, W}.
    # W = positive spectral part of iDelta = sum_{lam>0} lam |v><v|
    # (sj-vn-type.sj_wightman_from_eig). W - W^dagger = iDelta, W >= 0.
def wightman(iDelta) -> np.ndarray
    # convenience: just the SJ Wightman matrix W.
def asymmetry_causal(coords, C, *, axis=1) -> Measurement
    # A_caus = 2*f_co - 1, f_co = frac of causal links advancing in +phi
    # (sj-rotating-btz.two_point_profile causal_asymmetry). value in [-1,1].
def asymmetry_wightman(W, coords, C, *, axis=1) -> Measurement
    # A_W = (m_co - m_counter)/(|m_co|+|m_counter|) over causal links
    # (sj-rotating-btz wightman_asymmetry). value or NaN if fully dragged.
def superradiant_weight(coords, iDelta, *, omega, ws, ks, seed) -> Measurement
    # eigenvector-overlap construction: project SJ positive eigenvectors onto
    # plane waves e^{-i w t + i k phi}, weight of occupation map in the
    # superradiant wedge w(w - k*omega) < 0
    # (sj-eigenvector-superradiance.superradiance_weights). seed REQUIRED.
def positive_subspace_overlap(iDeltaA, iDeltaB) -> Measurement
    # mean cos^2 principal angle between two SJ positive subspaces
    # (sj-eigenvector-superradiance.subspace_overlap). sanity: self-overlap=1.
```

**Docstring formula ids**: `pauli-jordan`, `modular-flow-def` (for the SJ
modular structure), `modular-polar-decomposition` (Tomita-Takesaki, for the
W = positive-part construction). Evidence: VYPOCET-12 (sj-vn-type), VYPOCET-08
(sj-rotating-btz), VYPOCET-14/15 (sj-eigenvector-superradiance).

**VALIDATION TARGETS**:
- **Machine-precision invariant**: for `sj_state(iDelta)` built from a 2D
  diamond (N=300, seed 0), `W - W.conj().T` reproduces `iDelta` to 1e-12, and
  `W` is PSD (min eigenvalue `> -1e-10`).
- **Fully-dragged ergoregion smoke** (BTZ M=1, J=0.6, r=0.974, N≈800, seed 101,
  generous tolerance): `asymmetry_causal` → `value ≈ 1.0` (frac co-rot = 1.0,
  cf. committed `sj-rotating-btz/results.json`
  `causal_asymmetry_inside_ergo = 1.0`, `frac_corotating_links_inside_ergo = 1.0`).
  Assert `value > 0.95`.
- **Self-overlap sanity**: `positive_subspace_overlap(iD, iD).value ≈ 1.0`
  (committed `sanity_static_vs_static_mean_cos2 = 1.0000000000000002`); assert
  `> 0.999`.
- **Superradiant weight monotonicity smoke** (Kerr r=2.6, small N, 1–2 seeds):
  `superradiant_weight` increases with spin a (committed `vs_spin_r2.6`:
  `a=0.0 -> 0.0`, `a=0.3 -> 0.00121`, `a=0.6 -> 0.00622`). Assert
  `weight(a=0.6) > weight(a=0.0)` with the wedge weight at `a=0` ≈ 0 (±1e-3).
  Use the smallest N that keeps the trend; cap test < 60 s.

---

### C1 — `toe/entropy.py`   (layer C → imports `sj`, `causet`, `fits`)

SSEE via the generalized eigenproblem on a region/complement cut, with the
double truncation (`kappa = sqrt(N)/(4 pi)` in 2D) and the rank truncation
(`n_max = 2 * N^{3/4}` prescription in 4D), plus entropy-vs-region scaling.

**Signatures**

```python
def kappa_2d(N) -> float
    # Sorkin-Yazdi UV magnitude cutoff sqrt(N)/(4*pi) (1712.04227).
def n_max_area_law(N, dim, *, alpha=2.0) -> int
    # alpha * N^{(dim-1)/dim}; dim=4 -> 2*N^{3/4} prescription (review §19;
    # observer/crossed-product cutoff, ssee-4d). dim=2 -> N^{1/2}.
def ssee(W, iDelta, sub_idx, *, kappa=None, n_max=None, tol=1e-10) -> Measurement
    # generalized eigenproblem W_O v = mu iDelta_O v on the kept subspace;
    # S = sum_mu mu ln|mu|, pairs (mu, 1-mu). kappa -> double truncation
    # (sj-vn-type.ssee_mu); n_max -> rank truncation (ssee-4d.ssee_rank_truncated).
    # value = S; se from n_seeds if caller aggregates (else se=0).
def ssee_scaling(builder, Ns, *, frac=0.5, n_seeds, seed_base,
                 truncate="kappa") -> FitResult
    # build sprinkle->iDelta->W->ssee across Ns x seeds, fit S vs N power law.
    # builder: a causet region builder (e.g. sprinkle_diamond2d). Returns the
    # FitResult (value=exponent, se_regression, ci68_bootstrap, validated).
def rank_at_cutoff(pos_spectrum, kappa) -> int
    # number of positive modes with lambda > kappa (ssee-diamond.rank_at_cutoff).
```

**Docstring formula ids**: `ssee`, `ssee-formula`, `crossed-product-entropy`,
`crossed-product-def`, `type-ii-trace-entropy`. Evidence: VYPOCET-04
(ssee-diamond), VYPOCET-06 (ssee-4d), VYPOCET-12 (sj-vn-type).

**VALIDATION TARGETS**:
- **Single-demo reproduction** (`ssee-diamond/results.json` `.demo`, N=1200,
  the committed demo seed): `ssee(..., kappa=None)` → `S_full ≈ 95.19145102178456`
  and `ssee(..., kappa=kappa_2d(N))` → `S_trunc ≈ 1.5759042370547263`.
  These are deterministic for the committed seed → tolerance **±2%** on S_full,
  **±5%** on S_trunc (allow for any tie-breaking in degenerate-eigenvalue order).
  `kappa_2d(1200) == 2.7566444771089604` (exact, 1e-12).
- **III→II scaling smoke** (small Ns, e.g. `[400,600,800]`, 3 seeds, seed_base
  `7_000_000`): `ssee_scaling(sprinkle_diamond2d, Ns, truncate="none")`
  exponent ≈ 1 (volume law, value > 0.7); `truncate="kappa"` exponent ≈ 0
  (area/log law, |value| < 0.4). Committed full-run targets (7 Ns, 8 seeds):
  `S_full` exponent `1.0433`, `S_trunc` exponent `0.1724`. Small-N reproduces
  the SIGN/regime, not the exact exponent → assert regime, tolerance generous.
  Keep N ≤ 800 and ≤ 3 seeds so the test stays < 60 s.
- `n_max_area_law(N=2000, dim=4)` → `2*round(2000**0.75)` (integer, exact).

---

### C2 — `toe/vntype.py`   (layer C → imports `sj`, `causet`, `fits`)

Von Neumann type proxies: the entropy-trace scaling discriminator, the modular
spectrum `eps = ln(mu/(mu-1))`, the small-eps pile-up measure, and the
truncated-entropy saturation discriminator that separates II₁ (entropy caps,
bounded dS static patch) from II_∞ (entropy grows, flat control).

**Signatures**

```python
def modular_spectrum(mu, *, tol=1e-9) -> np.ndarray
    # eps = ln(mu/(mu-1)) on the mu>1 branch, sorted ascending
    # (sj-vn-type.modular_spectrum_from_mu; Casini-Huerta 0905.2562 single-mode).
def pile_up(eps, eps0=0.5) -> int
    # count of modular modes with eps < eps0 (small-eps pile-up; III_1 grows,
    # II saturates).
def trace_scaling(builder, Ns, *, frac, n_seeds, seed_base,
                  truncate) -> FitResult
    # entropy-trace exponent vs N (the proxy-1 trace divergence test).
def type_proxies(builder, Ns, *, frac, n_seeds, seed_base) -> dict
    # the full VYPOCET-12 three-proxy battery -> {proxy1: FitResult(s),
    # proxy2: {...}, proxy3: FitResult, verdict: {n_passing, overall}}.
def saturation_discriminator(builder_bounded, builder_flat, R_extents, *,
                             n_seeds, seed_base) -> dict
    # II_1 vs II_inf: fit truncated SSEE / region-content vs region tortoise
    # extent R*. Bounded dS -> saturating S_cap - B*exp(-R*/xi) (II_1, caps);
    # flat control -> growing (II_inf). Returns {desitter:{cap,xi,R2},
    # flat:{...}, II1_vs_IIinf_discriminated: bool}  (sj-desitter-type part1).
```

**Docstring formula ids**: `modular-spectrum`, `crossed-product-def`,
`type-ii-trace-entropy`, `ssee-formula`, `bekenstein-hawking-formula` (the
A/4G tracial-cap interpretation of II₁). Evidence: VYPOCET-12 (sj-vn-type),
VYPOCET-19 (sj-desitter-type).

**VALIDATION TARGETS**:
- **modular_spectrum smoke**: for an SSEE mu-array with a known pair, e.g.
  `mu = [2.0, -1.0]`, `modular_spectrum([2.0])` → `[ln(2/1)] = [0.6931...]`
  (exact, 1e-12). Monotonic; empty for all `mu <= 1`.
- **III→II trace exponents** (small-N smoke, `[400,600,800]`, 3 seeds, seed_base
  `7_000_000`, frac 0.5): `trace_scaling(..., truncate="none")` exponent > 0.7
  (volume, III-like); `truncate="kappa"` exponent < 0.4 (saturating, II-like).
  Committed full-run reference (`sj-vn-type/results.json`): S_full exponent
  `1.0433`, S_trunc exponent `0.1724`, overall verdict
  `"MIXED: 2/3 proxies consistent with III_1 -> II"`, `proxy3_factor_like=False`.
  Small-N asserts the regime (signs), not exact exponents.
- **type_proxies verdict smoke**: on the same small-N config the proxy1 and
  proxy2 verdicts come out `III_to_II == True` and proxy3 `factor_like == False`
  (committed `VERDICT.n_proxies_passing == 2`). Tolerance: assert proxy1 passes
  and proxy3 fails (the robust, reproducible part); proxy2 may be marked
  `xfail`/loose at small N.
- **Saturation discriminator** (`sj-desitter-type/results.json` part1): the
  bounded dS `N_total` saturating fit caps with `cap ≈ 480.11129`,
  `xi ≈ 0.50553`, `R2 ≈ 0.99994`; `dS_saturates_II1 == True` and
  `verdict_II1_vs_IIinf_discriminated == True`. Small-N smoke: assert the dS
  branch fit has `R2 > 0.9` and `II1_vs_IIinf_discriminated == True`; cap test
  < 60 s by using the committed (small) R*-extent grid and a few seeds. The
  truncated-SSEE proxy1 dS exponents (`S_full ≈ 1.1045`, `S_trunc ≈ 0.1163`)
  are the auxiliary targets.

---

## 3. Tests — naming, location, the conftest shim

- **Location**: `app/tests/`.
- **conftest** (already written): `app/tests/conftest.py` prepends
  `/Users/pazny/projects/theoryOfEverything/lib` to `sys.path` so `import toe`
  and `import toe.<module>` resolve to `lib/toe/`. No install step.
- **One test file per module**, named exactly:
  - `app/tests/test_toe_fits.py`
  - `app/tests/test_toe_causet.py`
  - `app/tests/test_toe_spectral.py`
  - `app/tests/test_toe_ncg.py`
  - `app/tests/test_toe_viz.py`
  - `app/tests/test_toe_sj.py`
  - `app/tests/test_toe_entropy.py`
  - `app/tests/test_toe_vntype.py`
  - plus `app/tests/test_toe_imports.py` (asserts the layer rules in §1: no
    cycles; B imports A; C imports B; viz imports only fits).
- **Time budget**: each module's test file MUST run in **< 60 s**. Stochastic
  modules (causet/sj/entropy/vntype) use the SMALL-N smoke targets above with
  generous tolerances; sympy modules (ncg, the spectral classifier) use exact
  equality; the machine-precision invariants (causet/sj pairing, Green
  coefficient) assert ≤ 1e-13 / 1e-15. Tests pass explicit seeds everywhere.
- **Validation flag**: each test reads the committed
  `core-data/calculations/<dir>/results.json` (or the quoted constants above),
  calls the function, and asserts via `toe.fits.validate_against(...)`, then
  checks the returned dataclass's `validated is True`. The exact target numbers
  are the ones quoted per-module (read from the committed JSON — not guessed).

---

## 4. Build order for the agents

1. `fits.py` (A1) — nothing depends on it being correct first, but everything
   imports its dataclasses. Validate against `sj-vn-type` SE/CI + AIC numbers.
2. `causet.py`, `spectral.py`, `ncg.py`, `viz.py` (A2–A5) — independent, parallel.
3. `sj.py` (B1) — after causet.
4. `entropy.py`, `vntype.py` (C1, C2) — after sj. Parallel (siblings, no
   cross-import).
5. Integrator fills `toe/__init__.py` re-exports last, once all 8 test files +
   `test_toe_imports.py` are green.

---

## 5. CHANGELOG

### v0.3.0 — SPARSE / ITERATIVE path (large-N SJ + SSEE, N ~ 1e4)

A memory-lean, matrix-FREE path so the SJ + SSEE pipelines reach `N ~ 1e4`
(2D sprinkling density `rho ~ 1e3-1e4`) without materialising a dense float
iDelta — needed by **H5g-2** (the A/4 cap) and the **VYPOCET-19 Part-3** tracial
probe. Three new public functions, layered exactly like their dense siblings:

- **A2 `causet.causal_blocks_2d(coords, *, dtype=np.float32, block=2048)`** —
  the 2D causal matrix assembled blockwise (sort-by-`u` + per-block null-cone
  test), stored as a single `dtype` array (default `float32`). The transient
  per-block boolean buffer is `block x N`, not `N x N`. Returns `(C, perm)` (the
  u-sort permutation); `C` is bit-identical to `causal_matrix` up to `perm`.
- **A2 `causet.idelta_operator_2d(coords, *, dtype=np.float32, block=2048)`** —
  the matrix-free Hermitian Pauli-Jordan operator as a
  `scipy.sparse.linalg.LinearOperator` (shape `(N, N)`, `complex128`). The 2D
  Green `G_R = (1/2)C` is IMPLICIT: `iDelta @ x = (i/2)(C @ x - C^T @ x)` is two
  bool-block GEMVs (real/imag split so the float32/float64 GEMM kernel is used).
  Only ONE float copy of `C` (+ its contiguous transpose) is stored. Returns
  `(op, perm)`. `dtype=float64` for the precision path (1e-14 vs dense),
  `float32` for the large-N smoke (~1e-6, halves memory, ~2x BLAS).
- **B1 `sj.sj_state_sparse(idelta_op, k, *, rng, which='LM', tol=0, maxiter=None,
  ncv=None)`** — top-k SJ spectral data via `scipy.sparse.linalg.eigsh`
  (`which='LM'`). The iDelta spectrum is `+/-` paired so `'LM'` returns a
  balanced top `~k/2` positive + `~k/2` negative set — all the SSEE truncation
  (`|lambda| > kappa`) needs. **Determinism**: the eigsh start vector `v0` is
  derived from the REQUIRED `rng` (`rng.standard_normal(N) + 1j ...`), so
  equal-seed restarts are bit-identical. Returns the `SJStateSparse` carrier
  (`eigvals`/`eigvecs`/`pos_spectrum` shaped like the dense `SJState` top slice;
  `W` is intentionally NOT materialised).
- **C1 `entropy.ssee_sparse(sj_sparse, sub_idx, *, kappa=None, n_max=None,
  tol=1e-10)`** — truncated SSEE reconstructed from the captured k-mode SJ data:
  keep the modes with `|lambda| > kappa` (or top `n_max`), build the truncated
  `(iDelta, W)` from those modes only (rank `<= k << N`), then the same restrict
  → local-cut → generalized-eigenproblem `W_O v = mu iDelta_O v` → `S = sum_mu mu
  ln|mu|` as the dense `ssee`. `n_max` prescriptions (`n_max_area_law`) reused.

**Path chosen — implicit `eigsh` WON, no dense-blocked fallback needed.** The
matrix-free `eigsh(which='LM')` resolves the extreme (largest-magnitude) ends of
the spectrum, which is precisely where the SSEE content lives (and avoids the
ill-conditioned INTERIOR-eigenvalue regime that would have forced a fall-back to
`scipy.linalg.eigh(subset_by_index=...)` on float32 blocks). It converges fast
and to machine precision: the dense-blocked partial-`eigh` fallback was prototyped
but not required.

**Validation (overlap sizes, `app/tests/test_toe_sparse.py`, < 90 s total):**
at `N in {1000, 2000}` the sparse path matches the dense path —
- top-k eigenvalues: rel diff `< 1e-8` (measured `~3e-15` with float64);
- truncated SSEE `S_trunc`: rel diff `< 1e-6` (measured `~1e-14`);
- `+/-` pairing + Hermiticity invariants on the operator applied to random
  vectors (`pairing_residual_rel < 1e-10`, `<x,Ax>` real, `<y,Ax>=conj<x,Ay>`);
- determinism (equal-seed eigsh → identical spectra);
- the captured top-k provably contains all `|lambda| > kappa` modes (k-sizing).

One **scaling smoke**: `N=8000` 2D diamond, `k=600` eigsh (float32 operator)
completes in ~32 s (< 120 s) and the top `|lambda|` follows the dense small-N
trend (`max|lambda| ~ 0.21 N`, loose). Build memory ~0.5 GB (< 2 GB). `eigsh`
seeded deterministically from the rng.

Package `__version__` → `0.3.0`; exports + `__all__` extended with the four new
names (`causal_blocks_2d`, `idelta_operator_2d`, `sj_state_sparse`/`SJStateSparse`,
`ssee_sparse`).

### v0.2.0 — VYPOCET-22 codim-2 migration (5 lifted proposals)

The five ready-to-lift proposals from `modular-flow-codim2/results.json`
(`lib_proposals`) were lifted out of that calc's `helpers.py` into the library,
respecting the layer rules:

- **A2 `causet.sprinkle_wedge_box4d(N, rng, *, t_half, x_half, yz_half)`** — the
  t-symmetric 4D Minkowski box whose `x>0` cut has its entangling surface on the
  codim-2 Rindler edge `E={t=0,x=0}` (the flat-2-plane H5g-3 joint). Tested via
  the iΔ ± pairing invariant (`pairing_residual_rel < 1e-12`).
- **A2 `causet.bd_smeared_dalembertian_inverse(C, rho, eps)`** — the SMEARED BD
  Green function `G_R = B_eps^{-1}`, the `eps`-sibling of the existing SHARP
  `bd_dalembertian_inverse(...,dim=4)` (Aslanbeigi-Saravani-Sorkin 1305.2588:
  `alpha4=-4/sqrt6`, `beta4=4/sqrt6`, `f4(n,eps)`). The smeared matrix builder is
  the private `_bd_smeared_matrix`. Test reproduces the committed
  `wedge_cond_B[0] = 15577.092005018936` (N=800, 3 seeds, eps=0.6).
- **B1 `sj.sj_state(iDelta, *, tol=1e-12, rel_floor=None)`** — added a RELATIVE
  positive-eigenvalue floor `rel_floor*max|lambda|` for ill-conditioned
  BD-inverse objects (`cond ~ 1e4-1e6`). **Default `rel_floor=None` keeps the
  absolute-`tol` path BIT-IDENTICAL** (proven by `array_equal` test + the full
  pre-existing suite staying green). `wightman` gained the same kwarg.
- **C1 `entropy.modular_kernel(W, iDelta, sub_idx, *, kappa=None, tol=1e-9)`** —
  exposes the site-basis one-particle kernel `K(x,y)` that `ssee` collapses to
  the scalar `S`. ADAPTATION vs the proposal's bare-dict return: it returns a
  small `ModularKernel` dataclass (`K, eps, S, nu, n, n_modes, validated`) per
  the §0.1 no-bare-dict rule, carrying the proposal's `{K, eps, S, nu}` fields.
  Test asserts the trace relation `mk.S == ssee(...).value` on the same cut.
- **A5 `viz.nl_vs_locus(Kabs, Dij, d_locus, near_r, *, n_zones=6, ...)`** —
  non-locality-vs-distance-to-locus panel. ADAPTATION vs the proposal's
  `(cen, mean)` tuple return: per the §A5 viz contract it RETURNS A `Figure`
  (imports only `toe.fits`), and additionally attaches the raw `(cen, mean)`
  curve as `fig._nl_vs_locus` for callers that want the VYPOCET binning array.

`modular-flow-codim2/calc.py` was refactored to import the four physics
functions (wedge builder, smeared inverse, rel-floored SJ state, modular kernel)
from `toe` instead of `helpers.py`; the regenerated `results.json` is bit-for-bit
identical to the committed one (only `runtime_s` differs). `helpers.py` keeps the
calc-local locality-profile diagnostics. Package `__version__` → `0.2.0`.
