"""toe/viz.py — Thin matplotlib presentation helpers (layer A, Agg backend).

Sets the Agg backend at import time so that no display is needed.  Every
function returns a ``matplotlib.figure.Figure`` object and optionally writes
a PNG when a ``save`` path is given.  No physics is computed here; this
module consumes the dataclasses from ``toe.fits``.

Import policy (ARCHITECTURE.md §1):
    viz imports ONLY stdlib + numpy + matplotlib + toe.fits.
    It MUST NOT import toe.causet, toe.sj, toe.entropy, or any compute module.

Evidence references (no formula ids required for the presentation layer):
    VYPOCET-08 (core-data/calculations/sj-rotating-btz/calc.py)  — radial_scan_plot
    VYPOCET-12 (core-data/calculations/sj-vn-type/calc.py)        — powerlaw_panel
    VYPOCET-13 (core-data/calculations/ds-classification/calc.py) — spectrum_plot
"""

# ---------------------------------------------------------------------------
# Backend — MUST be set before any other matplotlib import (ARCHITECTURE §0.4)
# ---------------------------------------------------------------------------
import matplotlib
matplotlib.use("Agg")

import os
from typing import Optional

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.figure

# Only toe.fits may be imported from toe (ARCHITECTURE §1 layer-A rule).
from toe.fits import FitResult


# ---------------------------------------------------------------------------
# Public API
# ---------------------------------------------------------------------------

def powerlaw_panel(
    fit: FitResult,
    x,
    y,
    *,
    save: Optional[str] = None,
    label: str = "",
    ax=None,
) -> matplotlib.figure.Figure:
    """Log-log scatter of (x, y) with fitted power-law line and CI68 band.

    Generalises the proxy1_trace log-log error-bar + fit-line panel from
    VYPOCET-12 (sj-vn-type/calc.py ``_plot_proxy1``).

    Formula: (presentation layer — no formula id required)
    Evidence: VYPOCET-12 (core-data/calculations/sj-vn-type/calc.py)
    Conventions: The fitted line uses ``fit.value`` (slope) and
        ``fit.intercept``; the shaded band spans ``fit.ci68_bootstrap``
        evaluated across the x range.  Both axes are log-scaled.

    Args:
        fit:   FitResult from ``toe.fits.powerlaw_fit`` (carries slope,
               intercept, ci68_bootstrap).
        x:     1-D array of x values (positive, e.g. sprinkle sizes N).
        y:     1-D array of y values (positive, e.g. mean entropy S).
        save:  if not None, save the figure to this path as a PNG.
        label: optional legend label prefix for the scatter points.
        ax:    if provided, draw into this existing Axes; otherwise create
               a new Figure with one Axes.

    Returns:
        matplotlib.figure.Figure containing the panel.
    """
    x = np.asarray(x, dtype=float)
    y = np.asarray(y, dtype=float)

    if ax is None:
        fig, ax = plt.subplots(figsize=(7, 5))
    else:
        fig = ax.get_figure()

    # --- scatter ---
    scatter_label = f"{label} data" if label else "data"
    ax.plot(x, y, "o", ms=5, color="tab:blue", label=scatter_label, zorder=3)

    # --- fitted line y = exp(intercept) * x^slope ---
    x_line = np.logspace(np.log10(x.min()), np.log10(x.max()), 200)
    y_line = np.exp(fit.intercept) * x_line ** fit.value
    fit_label = f"fit  slope={fit.value:.3f}"
    ax.plot(x_line, y_line, "-", color="tab:red", lw=2, label=fit_label, zorder=4)

    # --- CI68 band (shaded region between lower and upper power-law lines) ---
    ci_lo, ci_hi = fit.ci68_bootstrap
    # Only draw the band when it is non-degenerate (bootstrap was run)
    if ci_hi > ci_lo:
        y_lo = np.exp(fit.intercept) * x_line ** ci_lo
        y_hi = np.exp(fit.intercept) * x_line ** ci_hi
        ax.fill_between(
            x_line, y_lo, y_hi,
            color="tab:red", alpha=0.18,
            label=f"68 % CI  [{ci_lo:.3f}, {ci_hi:.3f}]",
            zorder=2,
        )

    ax.set_xscale("log")
    ax.set_yscale("log")
    ax.set_xlabel("$x$")
    ax.set_ylabel("$y$")
    title = f"Power-law fit  (slope = {fit.value:.3f} ± {fit.se_regression:.3f})"
    if label:
        title = f"{label}  —  " + title
    ax.set_title(title, fontsize=10)
    ax.legend(fontsize=8)
    fig.tight_layout()

    if save is not None:
        fig.savefig(save, dpi=140)

    return fig


def spectrum_plot(
    eigvals,
    *,
    kind: str = "loglog",
    save: Optional[str] = None,
    ax=None,
) -> matplotlib.figure.Figure:
    """Plot the positive SJ / iDelta spectrum (rank vs absolute eigenvalue).

    Generalises the ``spectra_J0_vs_J.png`` plot from VYPOCET-08
    (sj-rotating-btz/calc.py) and the spectral-dimension flow plot from
    VYPOCET-13.  Overlays a 1/k continuum reference curve.

    Formula: (presentation layer — no formula id required)
    Evidence: VYPOCET-08 (core-data/calculations/sj-rotating-btz/calc.py),
              VYPOCET-13 (core-data/calculations/ds-classification/calc.py)
    Conventions: ``eigvals`` are the *positive* eigenvalues of iDelta, sorted
        descending.  The rank k runs from 1 to len(eigvals).  The continuum
        reference is c / k where c = eigvals[0] (normalised to the first mode).

    Args:
        eigvals: 1-D array of positive eigenvalues (will be sorted descending
                 internally if not already sorted).
        kind:    "loglog" (default) or "semilogx" — axis scaling.
        save:    if not None, save the figure to this path as a PNG.
        ax:      if provided, draw into this existing Axes.

    Returns:
        matplotlib.figure.Figure containing the spectrum panel.
    """
    eigvals = np.asarray(eigvals, dtype=float)
    # Keep only positive and sort descending
    pos = eigvals[eigvals > 0]
    pos = np.sort(pos)[::-1]
    k = np.arange(1, len(pos) + 1, dtype=float)

    if ax is None:
        fig, ax = plt.subplots(figsize=(7, 5))
    else:
        fig = ax.get_figure()

    # --- spectrum ---
    if kind == "loglog":
        ax.loglog(k, pos, ".", ms=3, color="tab:blue", label=r"$\lambda_k$ (positive)")
    else:
        ax.semilogx(k, pos, ".", ms=3, color="tab:blue", label=r"$\lambda_k$ (positive)")

    # --- 1/k continuum overlay ---
    if len(pos) > 0:
        c = pos[0]
        k_ref = np.logspace(0, np.log10(k[-1]), 300)
        y_ref = c / k_ref
        ax.plot(k_ref, y_ref, "--", color="gray", lw=1.2, alpha=0.7,
                label=r"continuum $c/k$")

    ax.set_xlabel("rank $k$ (descending)")
    ax.set_ylabel(r"$|\lambda_k|$ of $i\Delta$ (positive spectrum)")
    ax.set_title("SJ / $i\\Delta$ positive spectrum")
    ax.legend(fontsize=8)
    fig.tight_layout()

    if save is not None:
        fig.savefig(save, dpi=140)

    return fig


def nl_vs_locus(
    Kabs,
    Dij,
    d_locus,
    near_r,
    *,
    n_zones: int = 6,
    save: Optional[str] = None,
    label: str = "",
    ax=None,
) -> matplotlib.figure.Figure:
    """Non-locality vs distance-to-LOCUS panel: per-site non-local fraction of
    ``|K|^2`` binned by the distance ``d_locus`` to an entangling locus.

    For each site the non-local fraction is the share of its off-diagonal
    ``|K|^2`` row-weight at distances ``Dij > near_r``; these per-site fractions
    are then averaged in ``n_zones`` equal-population quantile bins of
    ``d_locus``. The slope of the binned curve is the headline diagnostic
    (VYPOCET-18/20/22): a NEGATIVE slope = non-locality CONCENTRATES toward the
    locus (the 2D-corner signature), a POSITIVE slope = it falls toward the
    locus (the 4D null-tip behaviour). The ``d_locus`` argument is the
    GENERALISED locus distance -- the diamond/wedge tip, the codim-2 edge, or the
    flat hyperplane -- so the same panel serves all three controls.

    This is the presentation generalisation of the VYPOCET-20
    ``_nl_vs_corner_generic`` binning; it consumes the already-computed kernel
    magnitude ``Kabs`` and pairwise distances ``Dij`` (no physics is recomputed
    here, the binning is a display aggregation) and overlays an OLS trend line so
    the sign of the slope is read straight off the panel.

    Formula: (presentation layer -- no formula id required)
    Evidence: VYPOCET-22 (core-data/calculations/modular-flow-codim2/helpers.py
    nl_vs_edge_profile), VYPOCET-18/20 (modular-flow-bd-4d nl_vs_corner).
    Conventions: row-normalised non-local fraction
    ``rowfar / rowtot`` with ``rowfar = sum_{Dij > near_r} |K|^2``; equal-
    population quantile bins in ``d_locus``; the binning matches the VYPOCET-20
    diagnostic exactly (so the returned bin centres/means coincide with the
    committed ``nl_vs_*_dist`` / ``nl_vs_*_mean`` arrays).

    Args:
        Kabs: (n, n) absolute modular-kernel magnitude ``|K(x, y)|``.
        Dij: (n, n) pairwise spatial distance matrix on the sub-region sites.
        d_locus: (n,) per-site distance to the entangling locus (tip / edge /
            hyperplane).
        near_r: locality radius; pairs with ``Dij > near_r`` count as non-local.
        n_zones: number of equal-population distance bins (default 6).
        save: if not None, save the figure to this path as a PNG.
        label: optional legend label prefix for the curve.
        ax: if provided, draw into this existing Axes.

    Returns:
        matplotlib.figure.Figure with the binned non-locality-vs-locus curve and
        its OLS trend line. The bin centres and means are also stored on the
        Figure as ``fig._nl_vs_locus = (cen, mean)`` for callers that want the
        raw curve (the VYPOCET ``(cen, mean)`` return of ``nl_vs_edge_profile``).
    """
    Kabs = np.asarray(Kabs, dtype=float)
    Dij = np.asarray(Dij, dtype=float)
    d_locus = np.asarray(d_locus, dtype=float)

    # --- per-site non-local fraction (row-normalised |K|^2 beyond near_r) -----
    K2 = Kabs ** 2
    np.fill_diagonal(K2, 0.0)
    rowtot = K2.sum(axis=1)
    farmask = Dij > near_r
    np.fill_diagonal(farmask, False)
    rowfar = (K2 * farmask).sum(axis=1)
    with np.errstate(divide="ignore", invalid="ignore"):
        nl = np.where(rowtot > 0, rowfar / rowtot, np.nan)

    good = np.isfinite(nl)
    dc = d_locus[good]
    nlv = nl[good]

    cen_list, mean_list = [], []
    if dc.size >= n_zones:
        qs = np.linspace(0, 1, n_zones + 1)
        edges = np.quantile(dc, qs)
        edges[0] -= 1e-9
        edges[-1] += 1e-9
        for b in range(n_zones):
            m = (dc >= edges[b]) & (dc < edges[b + 1])
            if m.sum() == 0:
                continue
            cen_list.append(float(np.mean(dc[m])))
            mean_list.append(float(np.mean(nlv[m])))
    cen = np.asarray(cen_list, dtype=float)
    mean = np.asarray(mean_list, dtype=float)

    if ax is None:
        fig, ax = plt.subplots(figsize=(7, 5))
    else:
        fig = ax.get_figure()

    curve_label = f"{label} nl vs locus" if label else "nl vs locus"
    ax.plot(cen, mean, "o-", ms=5, color="tab:red", label=curve_label, zorder=3)

    # --- OLS trend line so the sign of the slope is read off the panel --------
    if cen.size >= 2:
        A = np.vstack([cen, np.ones_like(cen)]).T
        coef, *_ = np.linalg.lstsq(A, mean, rcond=None)
        slope = float(coef[0])
        x_line = np.linspace(cen.min(), cen.max(), 100)
        ax.plot(x_line, coef[0] * x_line + coef[1], "--", color="tab:gray",
                lw=1.5, label=f"slope = {slope:+.3f}", zorder=2)

    ax.set_xlabel("distance to locus")
    ax.set_ylabel("per-site non-local fraction")
    ax.set_title("Non-locality vs distance-to-locus", fontsize=10)
    ax.legend(fontsize=8)
    fig.tight_layout()

    # expose the raw (cen, mean) curve (the VYPOCET nl_vs_edge_profile return)
    fig._nl_vs_locus = (cen, mean)

    if save is not None:
        fig.savefig(save, dpi=140)

    return fig


def radial_scan_plot(
    r,
    observable,
    *,
    ergo_band: Optional[tuple] = None,
    save: Optional[str] = None,
    ax=None,
) -> matplotlib.figure.Figure:
    """Observable vs radius with optional shaded ergoregion band.

    Generalises the ``correlation_asymmetry.png`` PART C radial-scan panel
    from VYPOCET-08 (sj-rotating-btz/calc.py ``_plot_proxy1``).

    Formula: (presentation layer — no formula id required)
    Evidence: VYPOCET-08 (core-data/calculations/sj-rotating-btz/calc.py)
    Conventions: ``observable`` is plotted against ``r``.  If ``ergo_band``
        is given as ``(r_inner, r_outer)``, a shaded gold band marks the
        ergoregion between those radii.

    Args:
        r:          1-D array of radial positions.
        observable: 1-D array of observable values (same length as r).
                    NaN entries are plotted as gaps (np.where / masking).
        ergo_band:  optional (r_inner, r_outer) pair for the ergoregion shade.
        save:       if not None, save the figure to this path as a PNG.
        ax:         if provided, draw into this existing Axes.

    Returns:
        matplotlib.figure.Figure containing the radial-scan panel.
    """
    r = np.asarray(r, dtype=float)
    observable = np.asarray(observable, dtype=float)

    if ax is None:
        fig, ax = plt.subplots(figsize=(7, 5))
    else:
        fig = ax.get_figure()

    # --- optional ergoregion band ---
    if ergo_band is not None:
        r_in, r_out = ergo_band
        ax.axvspan(r_in, r_out, color="gold", alpha=0.30, label="ergoregion")

    # --- observable ---
    ax.plot(r, observable, "o-", ms=4, color="tab:blue", label="observable")
    ax.axhline(0.0, color="gray", lw=0.8, ls="--")

    ax.set_xlabel("$r$")
    ax.set_ylabel("observable")
    ax.set_title("Radial scan of SJ observable")
    ax.legend(fontsize=8)
    fig.tight_layout()

    if save is not None:
        fig.savefig(save, dpi=140)

    return fig
