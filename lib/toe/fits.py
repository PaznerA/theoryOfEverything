"""
toe/fits.py  --  Result dataclasses and fit primitives (Layer A, dependency root).

All modules in the toe library import their shared dataclasses and fit helpers
from here.  This module imports NOTHING from toe; it is the leaf of the import
graph.

Formula: spectral-dimension-fit
Evidence: VYPOCET-12 (core-data/calculations/sj-vn-type/calc_uncertainty.py)
"""

from __future__ import annotations

import math
from dataclasses import dataclass, field
from typing import Optional

import numpy as np


# ---------------------------------------------------------------------------
# 0.1  Result dataclasses
# ---------------------------------------------------------------------------

@dataclass
class FitResult:
    """A power-law / OLS fit outcome with honest uncertainty.

    Mirrors sj-vn-type/calc_uncertainty.py exactly.

    Formula: spectral-dimension-fit
    Evidence: VYPOCET-12 (core-data/calculations/sj-vn-type/calc_uncertainty.py)
    """
    value: float                            # central estimate (log-log slope)
    se_regression: float                    # residual-based OLS SE of the slope
    ci68_bootstrap: tuple[float, float]     # (lo, hi) = [16, 84] pct over resamples
    r2: float                               # coefficient of determination
    intercept: float = 0.0
    n_boot_used: int = 0
    boot_std: float = 0.0
    n_points: int = 0
    validated: Optional[bool] = None       # set by caller vs results.json target

    @property
    def ci_width(self) -> float:
        """Width of the 68 % bootstrap CI band."""
        return self.ci68_bootstrap[1] - self.ci68_bootstrap[0]


@dataclass
class Measurement:
    """Generic scalar observable with an uncertainty.

    Used by stochastic modules (causet/sj/entropy/vntype) that do not run a
    power-law fit themselves but must still return (value, uncertainty).
    """
    value: float
    se: float = 0.0                         # std-error (e.g. std / sqrt(n_seeds))
    ci68: Optional[tuple[float, float]] = None
    n: int = 0                              # sample size (e.g. n_seeds)
    validated: Optional[bool] = None


@dataclass
class ExactResult:
    """Exact-arithmetic outcome for sympy ncg/spectral-table functions.

    ``value`` is a sympy object (Rational | Expr); se is identically 0.
    """
    value: object                           # sympy.Rational | sympy.Expr
    se_regression: float = 0.0             # always 0.0 (exact computation)
    validated: Optional[bool] = None

    @property
    def as_float(self) -> float:
        """Convert sympy value to Python float."""
        import sympy as sp
        return float(sp.N(self.value))


# ---------------------------------------------------------------------------
# 0.3  Fit primitives
# ---------------------------------------------------------------------------

def regression_se(x: np.ndarray, y: np.ndarray) -> tuple[float, float, float]:
    """OLS slope, intercept, and residual-based SE for a log-log fit.

    Computes the honest single-fit standard error:
        SE = sqrt( SSR / (n-2) * (X^T X)^{-1}[0,0] )
    where X is the design matrix [log(x), 1].

    Formula: spectral-dimension-fit
    Evidence: VYPOCET-12 (core-data/calculations/sj-vn-type/calc_uncertainty.py)

    Args:
        x: 1-D array of x-values (positive; log is taken internally).
        y: 1-D array of y-values (positive; log is taken internally).

    Returns:
        (slope, intercept, se_slope) as plain floats.
    """
    lx = np.log(np.asarray(x, dtype=float))
    ly = np.log(np.asarray(y, dtype=float))
    n = len(lx)
    if n < 3:
        raise ValueError(f"Need at least 3 points for regression SE; got {n}.")
    X = np.column_stack([lx, np.ones(n)])
    # OLS via normal equations: beta = (X^T X)^{-1} X^T y
    XtX = X.T @ X
    Xty = X.T @ ly
    beta = np.linalg.solve(XtX, Xty)
    slope, intercept = float(beta[0]), float(beta[1])
    y_hat = X @ beta
    residuals = ly - y_hat
    ssr = float(residuals @ residuals)          # sum of squared residuals
    sigma2 = ssr / (n - 2)
    XtX_inv = np.linalg.inv(XtX)
    se_slope = float(math.sqrt(sigma2 * XtX_inv[0, 0]))
    return slope, intercept, se_slope


def bootstrap_slope_ci(
    per_sample: np.ndarray,
    x: np.ndarray,
    *,
    transform: str = "mean",
    n_boot: int = 1000,
    seed: int = 20260606,
) -> tuple[float, float, float]:
    """Bootstrap [16, 84] percentile CI for a power-law slope.

    Resamples *across seeds/samples* (WITH REPLACEMENT) following the
    calc_uncertainty.bootstrap_ci convention exactly: same floor (1e-9),
    same validity guard, same plain-OLS slope (lstsq, not residual SE).

    Formula: spectral-dimension-fit
    Evidence: VYPOCET-12 (core-data/calculations/sj-vn-type/calc_uncertainty.py)
    Conventions: calc_uncertainty.bootstrap_ci — floor=1e-9, transform in
        {"mean","cv"}, same-resampled-index-set applied across all N.

    Args:
        per_sample: shape ``(n_points, n_samples)`` — one column per seed/run.
        x:          1-D array of length ``n_points`` (the N-grid).
        transform:  ``"mean"`` -> fit mean over resampled columns;
                    ``"cv"`` -> fit coefficient of variation std/|mean|.
        n_boot:     number of bootstrap resamples (>= 1000 required).
        seed:       explicit RNG seed for reproducibility.

    Returns:
        (p16, p84, boot_std) — the [16, 84] percentile endpoints and std of
        the bootstrap slope distribution.
    """
    rng = np.random.default_rng(seed)
    per_sample = np.asarray(per_sample, dtype=float)
    x = np.asarray(x, dtype=float)
    n_points, n_samples = per_sample.shape
    floor = 1e-9  # matches calc_uncertainty.bootstrap_ci / calc.powerlaw_fit guard
    boots = []
    for _ in range(n_boot):
        idx = rng.integers(0, n_samples, size=n_samples)
        sub = per_sample[:, idx]
        if transform == "mean":
            yv = sub.mean(axis=1)
        elif transform == "cv":
            mean_v = sub.mean(axis=1)
            std_v = sub.std(axis=1, ddof=1)
            yv = std_v / np.maximum(np.abs(mean_v), 1e-12)
        else:
            raise ValueError(f"Unknown transform '{transform}'; use 'mean' or 'cv'.")
        yv = np.maximum(yv, floor)
        if not np.all(np.isfinite(yv)) or np.any(yv <= 0):
            continue
        # Plain OLS slope (matches calc_uncertainty.loglog_slope which uses lstsq)
        lx = np.log(x)
        ly = np.log(yv)
        A = np.vstack([lx, np.ones_like(lx)]).T
        coef, *_ = np.linalg.lstsq(A, ly, rcond=None)
        boots.append(float(coef[0]))
    boots_arr = np.array(boots)
    p16, p84 = float(np.percentile(boots_arr, 16.0)), float(np.percentile(boots_arr, 84.0))
    return p16, p84, float(boots_arr.std(ddof=1))


def powerlaw_fit(
    x: np.ndarray,
    y: np.ndarray,
    *,
    sig: Optional[np.ndarray] = None,
    n_boot: int = 1000,
    seed: int = 20260606,
    resamples: Optional[np.ndarray] = None,
) -> FitResult:
    """OLS power-law (log-log) fit with residual SE and optional bootstrap CI.

    Fits log(y) = slope * log(x) + intercept via OLS.  The SE is the honest
    residual-based single-fit SE.  If ``resamples`` (an ``(n_curves, n_points)``
    array of repeated measurements) is provided, runs the across-seed bootstrap
    CI (>= 1000 resamples, [16, 84] percentiles) following calc_uncertainty.py.
    Otherwise CI degenerates to ``(value, value)`` and ``n_boot_used = 0``.

    Formula: spectral-dimension-fit
    Evidence: VYPOCET-12 (core-data/calculations/sj-vn-type/calc_uncertainty.py)
    Conventions: calc_uncertainty.regression_se / bootstrap_ci from sj-vn-type.

    Args:
        x:         1-D x-values (positive).
        y:         1-D y-values (positive, e.g. mean S per N).
        sig:       unused weight placeholder (reserved for future weighted OLS).
        n_boot:    number of bootstrap resamples when ``resamples`` is given.
        seed:      explicit RNG seed.
        resamples: shape ``(n_curves, n_points)`` — per-seed y curves.  When
                   supplied the CI is meaningful; otherwise CI = (value, value).

    Returns:
        FitResult with value, se_regression, ci68_bootstrap, r2.
    """
    x = np.asarray(x, dtype=float)
    y = np.asarray(y, dtype=float)
    slope, intercept, se = regression_se(x, y)

    # R^2 in log-log space
    lx = np.log(x)
    ly = np.log(y)
    ly_hat = slope * lx + intercept
    ss_res = float(((ly - ly_hat) ** 2).sum())
    ss_tot = float(((ly - ly.mean()) ** 2).sum())
    r2 = 1.0 - ss_res / ss_tot if ss_tot > 0 else 1.0

    # Bootstrap CI (across seeds) if per-seed matrix is given
    if resamples is not None:
        per_sample = np.asarray(resamples, dtype=float)
        # resamples shape: (n_curves, n_points) -> need (n_points, n_curves)
        if per_sample.shape[0] == len(x):
            mat = per_sample
        else:
            mat = per_sample.T
        p16, p84, boot_std = bootstrap_slope_ci(mat, x, n_boot=n_boot, seed=seed)
        ci = (p16, p84)
        n_boot_used = n_boot
    else:
        ci = (slope, slope)
        boot_std = 0.0
        n_boot_used = 0

    return FitResult(
        value=slope,
        se_regression=se,
        ci68_bootstrap=ci,
        r2=r2,
        intercept=intercept,
        n_boot_used=n_boot_used,
        boot_std=boot_std,
        n_points=len(x),
    )


def aic(rss: float, n: int, k: int) -> float:
    """Gaussian-residual AIC: n * ln(rss/n) + 2k.

    Sign convention matches sj-threshold-scan delta_AIC_E_minus_S.

    Evidence: VYPOCET (sj-threshold-scan/calc.py)

    Args:
        rss: residual sum of squares from the fit.
        n:   number of data points.
        k:   number of free parameters.

    Returns:
        AIC value as a float.
    """
    return n * math.log(rss / n) + 2.0 * k


def aic_compare(*models) -> dict:
    """Compare models by AIC; return best model and delta-AIC for each.

    Evidence: VYPOCET (sj-threshold-scan/calc.py)

    Args:
        *models: each element is either ``(name, rss, n, k)`` (compute AIC
                 internally) or ``(name, aic_value)`` (pre-computed AIC).

    Returns:
        dict with keys ``"aic"`` (name->value), ``"best"`` (name with lowest
        AIC), ``"delta_aic"`` (name -> val - best_val).
    """
    aic_vals = {}
    for m in models:
        if len(m) == 4:
            name, rss, n, k = m
            aic_vals[name] = aic(rss, n, k)
        elif len(m) == 2:
            name, val = m
            aic_vals[name] = float(val)
        else:
            raise ValueError(f"Expected (name, rss, n, k) or (name, aic); got {m!r}")
    best = min(aic_vals, key=aic_vals.__getitem__)
    best_val = aic_vals[best]
    delta = {name: val - best_val for name, val in aic_vals.items()}
    return {"aic": aic_vals, "best": best, "delta_aic": delta}


def validate_against(
    value: float,
    target: float,
    *,
    rtol: float = 1e-9,
    atol: float = 0.0,
    exact: bool = False,
) -> bool:
    """Single chokepoint that checks a computed value against a target.

    Sets the ``validated`` flag on result dataclasses indirectly: callers
    pass the result's ``.value`` here and assign the return to ``.validated``.

    Evidence: VYPOCET-12 (sj-vn-type)

    Args:
        value:  computed value (float or sympy object when ``exact=True``).
        target: reference value from committed results.json.
        rtol:   relative tolerance for numeric comparison (default 1e-9).
        atol:   absolute tolerance for numeric comparison (default 0.0).
        exact:  when True uses sympy ``==`` (for ncg / spectral-table rationals).

    Returns:
        bool — True if the computed value matches the target.
    """
    if exact:
        import sympy as sp
        return bool(sp.Eq(sp.sympify(value), sp.sympify(target)))
    return math.isclose(float(value), float(target), rel_tol=rtol, abs_tol=atol)
