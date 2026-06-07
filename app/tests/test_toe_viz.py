"""Tests for toe/viz.py  (module A5 — presentation layer).

Validation targets from ARCHITECTURE.md §A5:
  - Each function returns a matplotlib.figure.Figure with >= 1 Axes.
  - The CI band in powerlaw_panel spans fit.ci68_bootstrap.
  - save=tmp_path/... writes a non-empty PNG.
  - Uses a synthetic FitResult (no stochastic modules needed).
  - Total runtime < 5 s.

Run with (from the repo root):
    MPLBACKEND=Agg python3 -m pytest app/tests/test_toe_viz.py -v
"""

import os
import importlib

import numpy as np
import pytest
import matplotlib
import matplotlib.figure

# ---------------------------------------------------------------------------
# The conftest.py shim already prepended lib/ to sys.path, so imports work.
# ---------------------------------------------------------------------------
import toe.viz as viz
from toe.fits import FitResult


# ---------------------------------------------------------------------------
# Synthetic fixtures (no compute modules required — ARCHITECTURE §A5)
# ---------------------------------------------------------------------------

def _synthetic_fit(ci_lo=0.9, ci_hi=1.1) -> FitResult:
    """A deterministic FitResult built from a simple N^1 power-law mock."""
    return FitResult(
        value=1.0,
        se_regression=0.02,
        ci68_bootstrap=(ci_lo, ci_hi),
        r2=0.999,
        intercept=0.0,
        n_boot_used=1000,
        boot_std=0.05,
        n_points=7,
    )


def _synthetic_xy():
    """Simple N^1 curve: y = N, x = N."""
    x = np.array([100, 200, 400, 600, 800, 1000, 1200], dtype=float)
    y = x.copy()
    return x, y


# ---------------------------------------------------------------------------
# Helper: check a figure has at least one Axes
# ---------------------------------------------------------------------------

def _has_axes(fig) -> bool:
    return isinstance(fig, matplotlib.figure.Figure) and len(fig.get_axes()) >= 1


# ---------------------------------------------------------------------------
# 1. Agg backend is set at import time
# ---------------------------------------------------------------------------

def test_agg_backend_set():
    """matplotlib backend must be Agg after importing toe.viz (ARCHITECTURE §0.4)."""
    assert matplotlib.get_backend().lower() == "agg", (
        f"Expected Agg backend, got {matplotlib.get_backend()!r}"
    )


# ---------------------------------------------------------------------------
# 2. viz imports only toe.fits (no causet/sj/entropy imported transitively)
# ---------------------------------------------------------------------------

def test_import_restriction():
    """viz.py's OWN imports must pull in only toe.fits (not causet/sj/entropy/vntype).

    The invariant under test is viz.py's *direct* dependency graph (ARCHITECTURE
    §1 layer-A rule): viz imports only ``from toe.fits import FitResult``.  We
    must measure this in a fresh, isolated interpreter because (a) sibling test
    modules pollute the in-process ``sys.modules`` and (b) ``import toe.viz``
    runs the eager package ``toe/__init__.py``, which deliberately re-exports the
    whole public API and therefore loads every submodule.  So we load
    ``toe/fits.py`` and ``toe/viz.py`` straight from file, bypassing the package
    ``__init__``, and assert the compute modules were never imported.
    """
    import subprocess
    import sys as _sys

    lib_dir = os.path.join(
        os.path.dirname(os.path.abspath(__file__)), os.pardir, os.pardir, "lib"
    )
    viz_path = os.path.join(lib_dir, "toe", "viz.py")
    fits_path = os.path.join(lib_dir, "toe", "fits.py")

    # Load viz.py in isolation (as a stand-alone module named "toe", so its
    # `from toe.fits import FitResult` resolves to the file we register) and
    # check no compute submodule of toe ever entered sys.modules.
    snippet = (
        "import importlib.util, sys, types\n"
        "MPLBACKEND='Agg'\n"
        f"fits_path = {fits_path!r}\n"
        f"viz_path = {viz_path!r}\n"
        # register a minimal `toe` package namespace so `toe.fits` resolves
        "pkg = types.ModuleType('toe'); pkg.__path__ = []\n"
        "sys.modules['toe'] = pkg\n"
        "spec_f = importlib.util.spec_from_file_location('toe.fits', fits_path)\n"
        "fits = importlib.util.module_from_spec(spec_f)\n"
        "sys.modules['toe.fits'] = fits; spec_f.loader.exec_module(fits)\n"
        "spec_v = importlib.util.spec_from_file_location('toe.viz', viz_path)\n"
        "viz = importlib.util.module_from_spec(spec_v)\n"
        "sys.modules['toe.viz'] = viz; spec_v.loader.exec_module(viz)\n"
        "forbidden = {'toe.causet', 'toe.sj', 'toe.entropy', 'toe.vntype'}\n"
        "bad = forbidden & set(sys.modules.keys())\n"
        "assert not bad, 'viz.py directly imported forbidden modules: %s' % bad\n"
        "print('OK')\n"
    )
    env = dict(os.environ, MPLBACKEND="Agg")
    proc = subprocess.run(
        [_sys.executable, "-c", snippet],
        capture_output=True, text=True, env=env,
    )
    assert proc.returncode == 0, (
        "viz.py import-restriction invariant violated:\n"
        f"{proc.stdout}\n{proc.stderr}"
    )


# ---------------------------------------------------------------------------
# 3. powerlaw_panel — basic smoke
# ---------------------------------------------------------------------------

def test_powerlaw_panel_returns_figure():
    """powerlaw_panel returns a Figure with >= 1 Axes."""
    fit = _synthetic_fit()
    x, y = _synthetic_xy()
    fig = viz.powerlaw_panel(fit, x, y, label="test")
    assert _has_axes(fig), "powerlaw_panel did not return a Figure with Axes"
    plt = matplotlib.pyplot
    plt.close("all")


def test_powerlaw_panel_ci_band_present():
    """The CI band must be drawn when ci_lo < ci_hi."""
    fit = _synthetic_fit(ci_lo=0.85, ci_hi=1.15)
    x, y = _synthetic_xy()
    fig = viz.powerlaw_panel(fit, x, y)
    ax = fig.get_axes()[0]
    # The fill_between call creates a PolyCollection.
    from matplotlib.collections import PolyCollection
    polys = [c for c in ax.collections if isinstance(c, PolyCollection)]
    assert len(polys) >= 1, (
        "Expected at least one PolyCollection (CI band) in the Axes"
    )
    matplotlib.pyplot.close("all")


def test_powerlaw_panel_no_band_when_degenerate():
    """When ci_lo == ci_hi (no bootstrap), no CI band should be drawn."""
    fit = _synthetic_fit(ci_lo=1.0, ci_hi=1.0)
    x, y = _synthetic_xy()
    fig = viz.powerlaw_panel(fit, x, y)
    ax = fig.get_axes()[0]
    from matplotlib.collections import PolyCollection
    polys = [c for c in ax.collections if isinstance(c, PolyCollection)]
    assert len(polys) == 0, (
        "No CI band expected when ci_lo == ci_hi"
    )
    matplotlib.pyplot.close("all")


def test_powerlaw_panel_saves_png(tmp_path):
    """powerlaw_panel with save= writes a non-empty PNG file."""
    fit = _synthetic_fit()
    x, y = _synthetic_xy()
    out = str(tmp_path / "powerlaw_test.png")
    fig = viz.powerlaw_panel(fit, x, y, save=out)
    assert os.path.isfile(out), f"Expected PNG at {out}"
    assert os.path.getsize(out) > 0, "PNG file is empty"
    matplotlib.pyplot.close("all")


def test_powerlaw_panel_existing_ax():
    """powerlaw_panel uses the provided Axes and returns the parent Figure."""
    import matplotlib.pyplot as _plt
    fig_outer, ax_outer = _plt.subplots()
    fit = _synthetic_fit()
    x, y = _synthetic_xy()
    fig_returned = viz.powerlaw_panel(fit, x, y, ax=ax_outer)
    assert fig_returned is fig_outer, (
        "powerlaw_panel must return the Figure that owns the passed Axes"
    )
    _plt.close("all")


# ---------------------------------------------------------------------------
# 4. spectrum_plot — basic smoke
# ---------------------------------------------------------------------------

def _synthetic_eigvals(n: int = 50) -> np.ndarray:
    """Synthetic 1/k-distributed positive eigenvalues (deterministic)."""
    k = np.arange(1, n + 1, dtype=float)
    return 1.0 / k


def test_spectrum_plot_returns_figure():
    """spectrum_plot returns a Figure with >= 1 Axes."""
    eigvals = _synthetic_eigvals()
    fig = viz.spectrum_plot(eigvals)
    assert _has_axes(fig), "spectrum_plot did not return a Figure with Axes"
    matplotlib.pyplot.close("all")


def test_spectrum_plot_saves_png(tmp_path):
    """spectrum_plot with save= writes a non-empty PNG."""
    eigvals = _synthetic_eigvals()
    out = str(tmp_path / "spectrum_test.png")
    viz.spectrum_plot(eigvals, save=out)
    assert os.path.isfile(out), f"Expected PNG at {out}"
    assert os.path.getsize(out) > 0, "PNG file is empty"
    matplotlib.pyplot.close("all")


def test_spectrum_plot_filters_nonpositive():
    """spectrum_plot silently drops zero/negative eigenvalues."""
    mixed = np.array([-0.5, 0.0, 0.1, 0.05, 0.02, -0.01, 0.5])
    fig = viz.spectrum_plot(mixed)
    ax = fig.get_axes()[0]
    # There should be exactly 4 positive values plotted
    lines = [l for l in ax.get_lines() if l.get_label() != "continuum $c/k$"]
    if lines:
        xdata = lines[0].get_xdata()
        assert len(xdata) == 4, f"Expected 4 positive eigvals, plotted {len(xdata)}"
    matplotlib.pyplot.close("all")


def test_spectrum_plot_has_continuum_overlay():
    """spectrum_plot includes the 1/k continuum reference line."""
    eigvals = _synthetic_eigvals(20)
    fig = viz.spectrum_plot(eigvals)
    ax = fig.get_axes()[0]
    labels = [l.get_label() for l in ax.get_lines()]
    assert any("continuum" in lbl.lower() or "c/k" in lbl for lbl in labels), (
        f"Expected a continuum reference line, found labels: {labels}"
    )
    matplotlib.pyplot.close("all")


def test_spectrum_plot_semilogx_kind():
    """spectrum_plot with kind='semilogx' does not raise."""
    eigvals = _synthetic_eigvals(30)
    fig = viz.spectrum_plot(eigvals, kind="semilogx")
    assert _has_axes(fig)
    matplotlib.pyplot.close("all")


def test_spectrum_plot_existing_ax():
    """spectrum_plot uses the provided Axes and returns the parent Figure."""
    import matplotlib.pyplot as _plt
    fig_outer, ax_outer = _plt.subplots()
    eigvals = _synthetic_eigvals()
    fig_returned = viz.spectrum_plot(eigvals, ax=ax_outer)
    assert fig_returned is fig_outer
    _plt.close("all")


# ---------------------------------------------------------------------------
# 5. radial_scan_plot — basic smoke
# ---------------------------------------------------------------------------

def _synthetic_radial():
    """Synthetic radial-scan data."""
    r = np.linspace(0.5, 2.5, 20)
    obs = np.sin(r)  # simple oscillation, not physics
    return r, obs


def test_radial_scan_plot_returns_figure():
    """radial_scan_plot returns a Figure with >= 1 Axes."""
    r, obs = _synthetic_radial()
    fig = viz.radial_scan_plot(r, obs)
    assert _has_axes(fig), "radial_scan_plot did not return a Figure with Axes"
    matplotlib.pyplot.close("all")


def test_radial_scan_plot_saves_png(tmp_path):
    """radial_scan_plot with save= writes a non-empty PNG."""
    r, obs = _synthetic_radial()
    out = str(tmp_path / "radial_test.png")
    viz.radial_scan_plot(r, obs, save=out)
    assert os.path.isfile(out), f"Expected PNG at {out}"
    assert os.path.getsize(out) > 0, "PNG file is empty"
    matplotlib.pyplot.close("all")


def test_radial_scan_plot_ergoregion_band():
    """When ergo_band is given, a shaded span (PolyCollection/Polygon) appears."""
    r, obs = _synthetic_radial()
    fig = viz.radial_scan_plot(r, obs, ergo_band=(0.95, 1.20))
    ax = fig.get_axes()[0]
    from matplotlib.collections import PolyCollection
    from matplotlib.patches import Polygon
    spans = [c for c in ax.collections if isinstance(c, PolyCollection)]
    # axvspan creates a Polygon (patches) in some matplotlib versions
    patches = [p for p in ax.patches]
    has_shade = len(spans) > 0 or len(patches) > 0
    assert has_shade, (
        "Expected a shaded ergoregion band (PolyCollection or Patch) in the Axes"
    )
    matplotlib.pyplot.close("all")


def test_radial_scan_plot_no_ergo_band():
    """Without ergo_band, no extra PolyCollection should appear."""
    r, obs = _synthetic_radial()
    fig = viz.radial_scan_plot(r, obs)
    ax = fig.get_axes()[0]
    from matplotlib.collections import PolyCollection
    polys = [c for c in ax.collections if isinstance(c, PolyCollection)]
    assert len(polys) == 0, (
        "No ergo band expected when ergo_band is None"
    )
    matplotlib.pyplot.close("all")


def test_radial_scan_plot_existing_ax():
    """radial_scan_plot uses the provided Axes and returns the parent Figure."""
    import matplotlib.pyplot as _plt
    fig_outer, ax_outer = _plt.subplots()
    r, obs = _synthetic_radial()
    fig_returned = viz.radial_scan_plot(r, obs, ax=ax_outer)
    assert fig_returned is fig_outer
    _plt.close("all")


# ---------------------------------------------------------------------------
# 6. Robustness: NaN in observable does not crash radial_scan_plot
# ---------------------------------------------------------------------------

def test_radial_scan_nan_observable():
    """NaN values in observable must not raise (plotted as gaps)."""
    r = np.linspace(0.5, 2.0, 10)
    obs = np.sin(r)
    obs[3] = np.nan
    obs[7] = np.nan
    fig = viz.radial_scan_plot(r, obs)
    assert _has_axes(fig)
    matplotlib.pyplot.close("all")


# ---------------------------------------------------------------------------
# 7. End-to-end: all three helpers write non-empty PNGs in one tmp directory
# ---------------------------------------------------------------------------

def test_all_three_save_png(tmp_path):
    """All three viz functions write non-empty PNGs when save= is given."""
    fit = _synthetic_fit()
    x, y = _synthetic_xy()
    eigvals = _synthetic_eigvals()
    r, obs = _synthetic_radial()

    paths = {
        "powerlaw": str(tmp_path / "pl.png"),
        "spectrum": str(tmp_path / "sp.png"),
        "radial":   str(tmp_path / "rad.png"),
    }
    viz.powerlaw_panel(fit, x, y, save=paths["powerlaw"])
    viz.spectrum_plot(eigvals, save=paths["spectrum"])
    viz.radial_scan_plot(r, obs, ergo_band=(0.8, 1.2), save=paths["radial"])

    for name, path in paths.items():
        assert os.path.isfile(path), f"{name}: expected PNG at {path}"
        size = os.path.getsize(path)
        assert size > 100, f"{name}: PNG at {path} is too small ({size} bytes)"

    matplotlib.pyplot.close("all")


# ---------------------------------------------------------------------------
# 8. MIGRATION 5: nl_vs_locus -- non-locality vs distance-to-locus panel
# ---------------------------------------------------------------------------

def _synthetic_locus(n=120, seed=0, concentrate_at_locus=True):
    """Synthetic (Kabs, Dij, d_locus): a kernel whose non-local weight
    CONCENTRATES toward the locus (small d_locus) so the panel slope is < 0,
    matching the 2D-corner signature. Pure-numpy, no compute module imported."""
    rng = np.random.default_rng(seed)
    coords = rng.uniform(-0.5, 0.5, size=(n, 3))
    diff = coords[:, None, :] - coords[None, :, :]
    Dij = np.sqrt(np.einsum("ijk,ijk->ij", diff, diff))
    d_locus = np.sqrt(coords[:, 0] ** 2 + coords[:, 1] ** 2)
    # base local kernel ~ exp(-Dij); add a non-local tail whose amplitude grows
    # as the site approaches the locus (small d_locus) when concentrate_at_locus.
    Kabs = np.exp(-4.0 * Dij)
    amp = (0.6 - d_locus) if concentrate_at_locus else d_locus
    amp = np.clip(amp, 0.0, None)
    far = Dij > 0.4
    Kabs = Kabs + 0.3 * np.outer(amp, np.ones(n)) * far
    np.fill_diagonal(Kabs, 1.0)
    return Kabs, Dij, d_locus


def test_nl_vs_locus_returns_figure_with_axes():
    Kabs, Dij, d_locus = _synthetic_locus()
    fig = viz.nl_vs_locus(Kabs, Dij, d_locus, near_r=0.4, n_zones=6)
    assert isinstance(fig, matplotlib.figure.Figure)
    assert len(fig.axes) >= 1
    matplotlib.pyplot.close(fig)


def test_nl_vs_locus_curve_attached_and_binned():
    """The raw (cen, mean) curve is attached to the figure and has n_zones bins
    of equal-population quantile binning (the VYPOCET nl_vs_edge_profile return)."""
    Kabs, Dij, d_locus = _synthetic_locus()
    fig = viz.nl_vs_locus(Kabs, Dij, d_locus, near_r=0.4, n_zones=6)
    cen, mean = fig._nl_vs_locus
    assert cen.shape == (6,) and mean.shape == (6,)
    # bin centres are increasing in distance-to-locus
    assert np.all(np.diff(cen) > 0)
    # all means are finite fractions in [0, 1]
    assert np.all(np.isfinite(mean))
    assert np.all((mean >= 0.0) & (mean <= 1.0))
    matplotlib.pyplot.close(fig)


def test_nl_vs_locus_slope_sign_reads_concentration():
    """A kernel concentrating non-locality at the locus gives a NEGATIVE slope;
    one anti-concentrating gives a POSITIVE slope (the headline diagnostic)."""
    Kabs_c, Dij, d_locus = _synthetic_locus(concentrate_at_locus=True)
    fig_c = viz.nl_vs_locus(Kabs_c, Dij, d_locus, near_r=0.4)
    cen_c, mean_c = fig_c._nl_vs_locus
    slope_c = np.polyfit(cen_c, mean_c, 1)[0]
    assert slope_c < 0      # non-locality rises TOWARD the locus
    matplotlib.pyplot.close(fig_c)

    Kabs_a, Dij, d_locus = _synthetic_locus(concentrate_at_locus=False)
    fig_a = viz.nl_vs_locus(Kabs_a, Dij, d_locus, near_r=0.4)
    cen_a, mean_a = fig_a._nl_vs_locus
    slope_a = np.polyfit(cen_a, mean_a, 1)[0]
    assert slope_a > 0      # non-locality FALLS toward the locus
    matplotlib.pyplot.close(fig_a)


def test_nl_vs_locus_saves_png(tmp_path):
    Kabs, Dij, d_locus = _synthetic_locus()
    path = str(tmp_path / "nl_vs_locus.png")
    viz.nl_vs_locus(Kabs, Dij, d_locus, near_r=0.4, save=path, label="wedge")
    assert os.path.isfile(path)
    assert os.path.getsize(path) > 100
    matplotlib.pyplot.close("all")
