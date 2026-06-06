"""
toe/spectral.py  --  Heat-kernel return probability, running spectral dimension,
and the d_s^UV classifier (Layer A, independent of causet/sj/entropy/vntype).

Distilled from:
  core-data/calculations/ds-classification/calc.py

No file I/O, no matplotlib side-effects, no global state.  All physics
parameters are explicit function arguments.

Formula: return-probability-uv-ir, spectral-dimension-def,
         spectral-dimension-flow, spectral-dimension-running
Evidence: VYPOCET-13 (core-data/calculations/ds-classification/calc.py)
"""

from __future__ import annotations

import numpy as np
import sympy as sp

from toe.fits import ExactResult

# ---------------------------------------------------------------------------
# Sentinel string used for the qualitative random-walk row
# ---------------------------------------------------------------------------
_RW_SENTINEL = ">D (increases)"


class _RWResult(ExactResult):
    """ExactResult subclass for the qualitative random-walk row.

    ``value`` is the string sentinel ``">D (increases)"``.
    ``as_float`` returns the illustrative ``D + 4`` value (e.g. 8.0 for D=4).
    """

    def __init__(self, D: int) -> None:
        super().__init__(value=_RW_SENTINEL, se_regression=0.0)
        self._D = D

    @property
    def as_float(self) -> float:  # type: ignore[override]
        """Return the illustrative D+4 value (e.g. 8.0 for D=4)."""
        return float(self._D + 4)


# ---------------------------------------------------------------------------
# A.  Exact symbolic master formula  d_s^UV = D / gamma
# ---------------------------------------------------------------------------

def ds_master_symbolic() -> sp.Expr:
    """Return the symbolic expression for the isotropic UV spectral dimension.

    Derives d_s^UV = D/gamma by computing the log-derivative of the radial
    heat trace integral for the inverse propagator F(k) ~ k^{2*gamma}, then
    simplifying symbolically.

    For a D-dimensional isotropic propagator F(k) ~ k^{2*gamma} the radial
    heat trace is::

        P(sigma) = INT_0^inf k^{D-1} exp(-sigma k^{2*gamma}) dk
                 ~ sigma^{-D/(2*gamma))

    so d_s = -2 d ln P / d ln sigma = D / gamma.

    Formula: return-probability-uv-ir, spectral-dimension-def
    Evidence: VYPOCET-13 (core-data/calculations/ds-classification/calc.py)
    Conventions: ds-classification.symbolic_master (Part A of calc.py).

    Returns:
        sympy.Expr that simplifies to D/gamma (two positive symbols).
    """
    sigma, k, D, gamma = sp.symbols("sigma k D gamma", positive=True)
    integrand = k ** (D - 1) * sp.exp(-sigma * k ** (2 * gamma))
    P = sp.integrate(integrand, (k, 0, sp.oo))
    P = sp.simplify(P)
    dlnP = sp.simplify(sigma * sp.diff(P, sigma) / P)
    ds = sp.simplify(-2 * dlnP)
    return sp.simplify(ds)


# ---------------------------------------------------------------------------
# B.  Numerical return-probability engine
# ---------------------------------------------------------------------------

def _logP_radial(sigma: float, F, D: int, *, npts: int = 20001) -> float:
    """Robust log of the radial heat trace integral (log-sum-exp).

    Computes::

        ln P(sigma) = ln INT_0^inf k^{D-1} exp(-sigma F(k)) dk

    in t = ln(k) coordinates with the log-sum-exp trick for numerical
    stability across the full sigma range (IR to UV).

    Formula: return-probability-uv-ir
    Evidence: VYPOCET-13 (core-data/calculations/ds-classification/calc.py)
    Conventions: ds-classification._logP_radial (Part B of calc.py).

    Args:
        sigma:  diffusion time (positive float).
        F:      callable k -> F(k), the inverse propagator.
        D:      topological (spacetime) dimension.
        npts:   number of quadrature points on the log-k grid (default 20001).

    Returns:
        ln P(sigma) as a float (may be -inf if sigma is pathological).
    """
    t = np.linspace(np.log(1e-12), np.log(1e12), npts)
    k = np.exp(t)
    Fk = F(k)
    # integrand in t-space: k^D * exp(-sigma F(k)) (Jacobian dk = k dt)
    g = D * t - sigma * Fk
    gmax = np.max(g)
    if not np.isfinite(gmax):
        return -np.inf
    w = np.exp(g - gmax)
    integral = np.trapezoid(w, t)
    return gmax + np.log(integral)


def return_probability(sigma: float, F, D: int) -> float:
    """Heat-kernel return probability P(sigma).

    P(sigma) = INT d^D k exp(-sigma F(k))

    The sphere surface factor cancels in the log-derivative so it is dropped
    here (only the radial piece matters for d_s).

    Formula: return-probability-uv-ir
    Evidence: VYPOCET-13 (core-data/calculations/ds-classification/calc.py)
    Conventions: ds-classification.P_isotropic; the sigma->inf (IR) limit
        gives d_s -> D for any F(k) ~ k^2; sigma->0 (UV) gives d_s -> D/gamma
        for F(k) ~ k^{2*gamma}.

    Args:
        sigma:  diffusion time (positive float).
        F:      callable k -> float array, the inverse propagator.
        D:      topological dimension (integer >= 1).

    Returns:
        P(sigma) as a positive float.
    """
    return float(np.exp(_logP_radial(sigma, F, D)))


def spectral_dimension(sigma: float, F, D: int, *, h: float = 1e-2) -> float:
    """Spectral dimension d_s(sigma) via central finite difference in ln sigma.

    d_s(sigma) = -2 * d ln P / d ln sigma
               ≈ -2 * [ln P(sigma*e^h) - ln P(sigma*e^{-h})] / (2h)

    Formula: spectral-dimension-def, spectral-dimension-running
    Evidence: VYPOCET-13 (core-data/calculations/ds-classification/calc.py)
    Conventions: ds-classification.ds_isotropic (Part B of calc.py).

    Args:
        sigma:  diffusion time.
        F:      callable inverse propagator k -> float array.
        D:      topological dimension.
        h:      step size in ln sigma for the central difference (default 1e-2).

    Returns:
        d_s(sigma) as a float.
    """
    lnsig = np.log(sigma)
    lnPp = _logP_radial(np.exp(lnsig + h), F, D)
    lnPm = _logP_radial(np.exp(lnsig - h), F, D)
    return float(-2.0 * (lnPp - lnPm) / (2.0 * h))


def spectral_dimension_flow(
    F,
    D: int,
    *,
    sigmas: np.ndarray | None = None,
) -> np.ndarray:
    """d_s(sigma) evaluated over a log-sigma grid (IR -> UV).

    Computes the full running of the spectral dimension from IR (large sigma)
    to UV (small sigma), as in ds-classification.flow_isotropic.

    Formula: spectral-dimension-flow, spectral-dimension-running
    Evidence: VYPOCET-13 (core-data/calculations/ds-classification/calc.py)
    Conventions: ds-classification.flow_isotropic; default grid
        np.logspace(6, -10, 90) matches the committed calc.py.

    Args:
        F:      callable inverse propagator k -> float array.
        D:      topological dimension.
        sigmas: 1-D array of sigma values (default: np.logspace(6, -10, 90),
                ordered IR -> UV).

    Returns:
        np.ndarray of d_s values, same length as sigmas.
    """
    if sigmas is None:
        sigmas = np.logspace(6, -10, 90)
    return np.array([spectral_dimension(s, F, D) for s in sigmas])


# ---------------------------------------------------------------------------
# B2.  Anisotropic (Horava-Lifshitz) kernel
# ---------------------------------------------------------------------------

def _logP_horava(sigma: float, D_space: int, z: int, m: float = 1.0) -> float:
    """Log return probability for the anisotropic Horava-Lifshitz dispersion.

    The inverse propagator factorises as::

        F(omega, k) = omega^2 + k^2 + k^{2z} / m^{2z-2}

    time part: INT_0^inf exp(-sigma*omega^2) d omega ~ sigma^{-1/2}
    space part: INT_0^inf k^{D_space-1} exp(-sigma F_space(k)) dk

    so d_s = 1 + D_space/z in the UV (k -> inf, k^{2z} dominates).

    Formula: spectral-dimension-def
    Evidence: VYPOCET-13 (core-data/calculations/ds-classification/calc.py)
    Conventions: ds-classification._logP_horava (Part B of calc.py);
        Horava arXiv:0902.3657 d_s = 1 + D_space/z.

    Args:
        sigma:   diffusion time.
        D_space: number of spatial dimensions (= D - 1 for spacetime D).
        z:       dynamical critical exponent.
        m:       crossover mass scale (units where m = 1 by default).

    Returns:
        ln P(sigma) as a float.
    """
    # time contribution: INT_0^inf exp(-sigma omega^2) d omega = sqrt(pi/sigma)/2
    ln_time = 0.5 * np.log(np.pi / sigma) - np.log(2.0)
    # space contribution via log-sum-exp
    t = np.linspace(np.log(1e-12), np.log(1e12), 20001)
    k = np.exp(t)
    F_space = k ** 2 + (k ** (2 * z)) / (m ** (2 * z - 2))
    g = D_space * t - sigma * F_space
    gmax = np.max(g)
    w = np.exp(g - gmax)
    ln_space = gmax + np.log(np.trapezoid(w, t))
    return ln_time + ln_space


def _ds_horava(sigma: float, D_space: int, z: int, h: float = 1e-2) -> float:
    """Spectral dimension for the Horava-Lifshitz dispersion."""
    lnsig = np.log(sigma)
    lnPp = _logP_horava(np.exp(lnsig + h), D_space, z)
    lnPm = _logP_horava(np.exp(lnsig - h), D_space, z)
    return float(-2.0 * (lnPp - lnPm) / (2.0 * h))


# ---------------------------------------------------------------------------
# C.  Concrete propagator factories
# ---------------------------------------------------------------------------

def _make_gr(D: int = 4, m: float = 1.0):
    """GR inverse propagator: F(k) = k^2 (gamma=1, d_s = D at all scales)."""
    return lambda k: np.asarray(k, dtype=float) ** 2


def _make_stelle(m: float = 1.0):
    """Stelle quadratic gravity: F(k) = k^2 (1 + k^2/m^2), UV ~ k^4, gamma=2."""
    return lambda k: (np.asarray(k, dtype=float) ** 2) * (1.0 + np.asarray(k, dtype=float) ** 2 / m ** 2)


def _make_as(D: int = 4, m: float = 1.0):
    """Asymptotic-Safety propagator with eta_* = 2-D (running anomalous dim).

    UV: F ~ k^{2-eta_*} = k^{2-(2-D)} = k^D, so gamma=D/2 and d_s = D/(D/2) = 2.
    IR: F ~ k^2 (d_s = D).
    """
    eta_star = 2 - D
    def F(k):
        kk = np.asarray(k, dtype=float)
        return kk ** 2 + (kk ** 2) ** (1.0 - eta_star / 2.0) / (m ** (-eta_star))
    return F


def _make_cst_dalembert(D: int = 4, m: float = 1.0):
    """Causal-set d'Alembertian effective propagator.

    UV: F ~ k^D -> gamma = D/2 -> d_s = D/(D/2) = 2 (universal; Belenchia+).
    IR: F ~ k^2 (d_s = D).
    """
    def F(k):
        kk = np.asarray(k, dtype=float)
        return kk ** 2 + (kk ** 2) ** (D / 2.0) / (m ** (D - 2))
    return F


def _make_cst_randomwalk(D: int = 4, m: float = 1.0):
    """Causal-set random-walk effective propagator (qualitative).

    Models the Eichhorn-Mizera 1311.2530 trend: UV d_s INCREASES above D.
    Uses an effective UV power < 1 (sub-diffusive -> super-dimensional).

    gamma_UV = D/(D+4)  =>  d_s_UV = D/gamma_UV = D + 4 > D.
    """
    gamma_uv = D / (D + 4.0)
    def F(k):
        kk = np.asarray(k, dtype=float)
        uv = (kk ** 2) ** gamma_uv * (m ** (2.0 - 2.0 * gamma_uv))
        ir = kk ** 2
        return np.minimum(ir, uv)
    return F


def _make_multifrac(D: int = 4, m: float = 1.0):
    """Multifractional effective propagator (Calcagni 1304.2709).

    UV: gamma = D/2 -> d_s = 2.  Identical functional form to CST d'Alembertian.
    """
    return _make_cst_dalembert(D, m)


# ---------------------------------------------------------------------------
# D.  The CLASSIFIER  d_s^UV(z, D)
# ---------------------------------------------------------------------------

def d_s_uv(
    z: int | float,
    D: int,
    *,
    probe: str = "heat_kernel",
    convention: str = "isotropic",
) -> ExactResult:
    """Return the EXACT rational UV spectral dimension d_s^UV for (z, D, probe).

    Master table:

    ============  ==================  =====================================
    convention    probe               d_s^UV
    ============  ==================  =====================================
    isotropic     heat_kernel         sympy.Rational(D, z)   (D/gamma, gamma=z)
    anisotropic   heat_kernel         1 + D_space/z  (Horava; D_space = D-1)
    isotropic     random_walk         sentinel ">D (increases)" (qualitative)
    ============  ==================  =====================================

    For the standard isotropic case the UV propagator F(k) ~ k^{2*gamma} with
    gamma = z gives d_s^UV = D/gamma = D/z exactly.

    Formula: return-probability-uv-ir, spectral-dimension-def,
             spectral-dimension-flow
    Evidence: VYPOCET-13 (core-data/calculations/ds-classification/calc.py)
    Conventions: ds-classification.ds_master / ds_horava_exact (Part E of
        calc.py); Horava arXiv:0902.3657 d_s = 1 + D/z with D_space = D-1 = 3
        for D=4 spacetime.  The D vs D_space convention (documented in
        papers/draft-03) means Horava rows use D_space = D - 1.

    Args:
        z:           UV propagator exponent (gamma = z for isotropic;
                     dynamical critical exponent for Horava).
        D:           topological (spacetime) dimension.
        probe:       ``"heat_kernel"`` (default) or ``"random_walk"``.
        convention:  ``"isotropic"`` (default) or ``"anisotropic"`` (Horava).

    Returns:
        ExactResult whose ``.value`` is a ``sympy.Rational`` (or the string
        sentinel ``">D (increases)"`` for random_walk), and ``.se_regression = 0``.
    """
    if probe == "random_walk":
        # Qualitative: d_s increases above D (Eichhorn-Mizera 1311.2530).
        # Returns _RWResult subclass whose .as_float gives the D+4 demo value.
        return _RWResult(D)

    if convention == "anisotropic":
        # Horava-Lifshitz: d_s = 1 + D_space / z, D_space = D - 1
        # (papers/draft-03 convention: Horava rows use D_space=3 for D=4)
        D_space = D - 1
        val = sp.Rational(1) + sp.Rational(D_space, int(z))
        return ExactResult(value=val, se_regression=0.0)

    # Default: isotropic master  d_s^UV = D / gamma  with gamma = z
    val = sp.Rational(int(D), int(z))
    return ExactResult(value=val, se_regression=0.0)
