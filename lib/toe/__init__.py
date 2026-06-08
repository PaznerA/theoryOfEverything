# -*- coding: utf-8 -*-
"""toe -- composable simulation library distilled from the 20 verified calc.py
scripts of the Theory of Everything knowledge base (roadmap step 3).

Each public function takes physics parameters as inputs and returns a small
result carrier (``FitResult`` / ``Measurement`` / ``ExactResult``) that pairs a
value with an honest uncertainty (SE / bootstrap CI / exact-zero) plus an
optional ``validated`` flag.  Functions carry ``Formula:`` / ``Evidence:`` /
``Conventions:`` docstring tags pointing back to the committed calc scripts.

Module map (import layers A -> B -> C; a module may import only from lower
layers; ``fits`` is the leaf):

    Layer A (independent)
      toe.fits      Result dataclasses + fit primitives (dependency root).
      toe.causet    Sprinkling regions, causal/link structure, retarded Green
                    functions, the Pauli-Jordan operator iDelta + diagnostics.
      toe.spectral  Heat-kernel return probability, running spectral dimension,
                    the d_s^UV classifier.
      toe.ncg       Exact-rational NCG spectral-action / heat-kernel a4 numbers
                    (central charges, c/(-a) ratio, lambda-induction ledger).
      toe.viz       Thin matplotlib (Agg) presentation panels.  Imports ONLY
                    toe.fits from the package.

    Layer B (depends on A)
      toe.sj        The Sorkin-Johnston state and rotating-spacetime SJ
                    observables (asymmetries, superradiant weight, overlaps).

    Layer C (depends on A + B)
      toe.entropy   SSEE via the generalized eigenproblem; scaling driver.
      toe.vntype    von Neumann type proxies for the SSEE truncation transition.
      toe.spectraltriple  Finite spectral-triple Dirac D_K = sgn(K) sqrt(|K|)
                    from a one-particle modular kernel, and the Connes spectral
                    distance d_D(x,y) = sup{|a(x)-a(y)| : ||[D,a]|| <= 1}.

Import convention: the package lives under ``lib/`` and is imported by path
(``sys.path`` shim in app/tests/conftest.py); there is no setup.py / pyproject.
"""

from __future__ import annotations

__version__ = "0.3.0"

# ---------------------------------------------------------------------------
# Layer A1 -- fits (result carriers + fit primitives, the dependency root)
# ---------------------------------------------------------------------------
from toe.fits import (
    FitResult,
    Measurement,
    ExactResult,
    regression_se,
    bootstrap_slope_ci,
    powerlaw_fit,
    aic,
    aic_compare,
    validate_against,
)

# ---------------------------------------------------------------------------
# Layer A2 -- causet (geometry / causal structure / Pauli-Jordan)
# ---------------------------------------------------------------------------
from toe.causet import (
    sprinkle_diamond2d,
    sprinkle_slab2d,
    sprinkle_box4d,
    sprinkle_slab4d,
    sprinkle_wedge_box4d,
    sprinkle_ds_static_patch2d,
    sprinkle_ds_static_patch4d,
    poisson_count_box4d,
    lattice_count_box4d,
    boost_coords,
    fano_factor,
    causal_matrix,
    link_matrix,
    green_retarded_2d,
    green_retarded_4d,
    bd_dalembertian_inverse,
    bd_smeared_dalembertian_inverse,
    pauli_jordan,
    causal_diagnostics,
    causal_blocks_2d,
    idelta_operator_2d,
)

# ---------------------------------------------------------------------------
# Layer A3 -- spectral (heat-kernel d_s flow + classifier)
# ---------------------------------------------------------------------------
from toe.spectral import (
    ds_master_symbolic,
    return_probability,
    spectral_dimension,
    spectral_dimension_flow,
    d_s_uv,
)

# ---------------------------------------------------------------------------
# Layer A4 -- ncg (exact-rational spectral-action numbers)
# ---------------------------------------------------------------------------
from toe.ncg import (
    a4_heat_kernel_bracket,
    central_charges,
    a4_ratio,
    spectral_action_ratio,
    sector_ledger,
    str_count,
    lambda_induction_ledger,
)

# ---------------------------------------------------------------------------
# Layer A5 -- viz (presentation panels; imports only toe.fits)
# ---------------------------------------------------------------------------
from toe.viz import (
    powerlaw_panel,
    spectrum_plot,
    nl_vs_locus,
    radial_scan_plot,
)

# ---------------------------------------------------------------------------
# Layer B1 -- sj (Sorkin-Johnston state + rotating observables)
# ---------------------------------------------------------------------------
from toe.sj import (
    SJState,
    sj_state,
    wightman,
    asymmetry_causal,
    asymmetry_wightman,
    superradiant_weight,
    positive_subspace_overlap,
    SJStateSparse,
    sj_state_sparse,
)

# ---------------------------------------------------------------------------
# Layer C1 -- entropy (SSEE generalized eigenproblem + scaling)
# ---------------------------------------------------------------------------
from toe.entropy import (
    kappa_2d,
    n_max_area_law,
    rank_at_cutoff,
    ssee,
    ssee_scaling,
    ModularKernel,
    modular_kernel,
    ssee_sparse,
)

# ---------------------------------------------------------------------------
# Layer C2 -- vntype (von Neumann type proxies)
# ---------------------------------------------------------------------------
from toe.vntype import (
    modular_spectrum,
    pile_up,
    trace_scaling,
    type_proxies,
    saturation_discriminator,
)

# ---------------------------------------------------------------------------
# Layer C3 -- spectraltriple (finite spectral-triple Dirac + Connes distance)
# ---------------------------------------------------------------------------
from toe.spectraltriple import (
    dirac_from_kernel,
    connes_commutator_norm,
    connes_distance,
    ConnesDistance,
)

__all__ = [
    "__version__",
    # fits (A1)
    "FitResult",
    "Measurement",
    "ExactResult",
    "regression_se",
    "bootstrap_slope_ci",
    "powerlaw_fit",
    "aic",
    "aic_compare",
    "validate_against",
    # causet (A2)
    "sprinkle_diamond2d",
    "sprinkle_slab2d",
    "sprinkle_box4d",
    "sprinkle_slab4d",
    "sprinkle_wedge_box4d",
    "sprinkle_ds_static_patch2d",
    "sprinkle_ds_static_patch4d",
    "poisson_count_box4d",
    "lattice_count_box4d",
    "boost_coords",
    "fano_factor",
    "causal_matrix",
    "link_matrix",
    "green_retarded_2d",
    "green_retarded_4d",
    "bd_dalembertian_inverse",
    "bd_smeared_dalembertian_inverse",
    "pauli_jordan",
    "causal_diagnostics",
    "causal_blocks_2d",
    "idelta_operator_2d",
    # spectral (A3)
    "ds_master_symbolic",
    "return_probability",
    "spectral_dimension",
    "spectral_dimension_flow",
    "d_s_uv",
    # ncg (A4)
    "a4_heat_kernel_bracket",
    "central_charges",
    "a4_ratio",
    "spectral_action_ratio",
    "sector_ledger",
    "str_count",
    "lambda_induction_ledger",
    # viz (A5)
    "powerlaw_panel",
    "spectrum_plot",
    "nl_vs_locus",
    "radial_scan_plot",
    # sj (B1)
    "SJState",
    "sj_state",
    "wightman",
    "asymmetry_causal",
    "asymmetry_wightman",
    "superradiant_weight",
    "positive_subspace_overlap",
    "SJStateSparse",
    "sj_state_sparse",
    # entropy (C1)
    "kappa_2d",
    "n_max_area_law",
    "rank_at_cutoff",
    "ssee",
    "ssee_scaling",
    "ModularKernel",
    "modular_kernel",
    "ssee_sparse",
    # vntype (C2)
    "modular_spectrum",
    "pile_up",
    "trace_scaling",
    "type_proxies",
    "saturation_discriminator",
    # spectraltriple (C3)
    "dirac_from_kernel",
    "connes_commutator_norm",
    "connes_distance",
    "ConnesDistance",
]
