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

from dataclasses import dataclass

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


# ---------------------------------------------------------------------------
# E.  DISCRETE heat kernel from a D^2 eigenvalue spectrum
#     (shared-heat-kernel object: d_s AND the a_2k coefficients from ONE spectrum)
# ---------------------------------------------------------------------------

@dataclass
class HeatKernelSpectrum:
    """Carrier for the discrete heat-trace analysis of a single ``D^2`` spectrum.

    Both the running spectral dimension ``d_s(sigma)`` and the small-sigma
    Seeley-DeWitt coefficients ``a_0, a_2, a_4`` are extracted from the SAME
    object ``Z(sigma) = Tr e^{-sigma D^2} = sum_i e^{-sigma lambda_i}`` -- this
    is the shared-heat-kernel content that links the NCG spectral action
    (which reads ``a_0, a_2, a_4``) to the spectral dimension (which reads the
    UV/IR scaling exponent of ``Z``).

    Fields:
        sigmas:      1-D log-sigma grid (IR -> UV, large -> small).
        Z:           ``Tr e^{-sigma D^2}`` on the grid (un-normalised).
        ds:          ``d_s(sigma) = -2 d ln Z / d ln sigma`` on the grid.
        ds_plateau:  robust plateau value of ``d_s`` (median over the widest
                     window where ``|d_s - 2 round(d_s_med/2)|`` is small);
                     compare to the analytic BD value (2D causet ~ 2).
        ds_plateau_se: across-grid std of ``d_s`` inside the plateau window.
        plateau_lo / plateau_hi: sigma bounds of the located plateau window.
        plateau_width_dec: width of the plateau in log10(sigma) decades.
        a0 / a2 / a4: Seeley-DeWitt coefficients from the small-sigma fit
                      ``Z(sigma) sigma^{D/2} ~ a0 + a2 sigma + a4 sigma^2``
                      (un-normalised; a0 is the volume term, a2/a4 the curvature
                      terms which vanish for FLAT space up to finite-N noise).
        a2_over_a0 / a4_over_a0: the reporting ratios (dimensionless).
        coeff_fit_r2: R^2 of the quadratic small-sigma fit.
        N:           spectrum size.
    """

    sigmas: np.ndarray
    Z: np.ndarray
    ds: np.ndarray
    ds_plateau: float
    ds_plateau_se: float
    plateau_lo: float
    plateau_hi: float
    plateau_width_dec: float
    a0: float
    a2: float
    a4: float
    a2_over_a0: float
    a4_over_a0: float
    coeff_fit_r2: float
    N: int


def heat_kernel_from_spectrum(
    d2,
    D,
    *,
    sigmas: np.ndarray | None = None,
    plateau_tol: float = 0.25,
    fit_window_dec: float = 1.0,
):
    """Discrete heat-trace analysis of a single ``D^2`` eigenvalue spectrum.

    Builds ``Z(sigma) = Tr e^{-sigma D^2} = sum_i e^{-sigma lambda_i}`` from the
    eigenvalues ``lambda_i`` of a positive operator ``D^2`` (e.g. ``|sym(BD)|``
    of the Benincasa-Dowker d'Alembertian, or ``|iDelta|`` of the Pauli-Jordan
    operator) and extracts BOTH of the shared-heat-kernel observables:

      (a) the running spectral dimension ``d_s(sigma) = -2 d ln Z / d ln sigma``
          and its robust intermediate PLATEAU value (the discrete UV avatar --
          for a finite spectrum bounded above by the discreteness, ``Z -> N`` and
          ``d_s -> 0`` as ``sigma -> 0``, so the physical scaling lives in the
          intermediate plateau, NOT the strict UV);
      (b) the small-sigma Seeley-DeWitt coefficients ``a_0, a_2, a_4`` from the
          asymptotic expansion ``Z(sigma) ~ sigma^{-D/2}(a_0 + a_2 sigma +
          a_4 sigma^2 + ...)``, fitted on the small-sigma side of the plateau.

    The point of returning both from ONE spectrum is the H-C discriminator
    (LOV-18-11-overlaps.md): ``d_s`` and the ``a_2k`` coefficients are
    CONSISTENT functions of the same ``D^2`` spectrum, exactly as the spectral
    dimension and the spectral action read the same ``Tr f(D^2)`` heat kernel.

    HONEST CAVEATS (F-001 / F-002 / F-012):
      * ``d_s`` is PROBE-DEPENDENT: the value depends on which operator built
        ``d2`` (BD d'Alembertian probe -> ~2 in any D; random-walk probe -> >D).
      * the coefficients ``a_2, a_4`` are CURVATURE integrals -- on a FLAT causet
        they vanish analytically, so their finite ``a4/a0`` here is a finite-N
        artefact, NOT the continuum NCG ``-18/11`` (which is a Dirac-content /
        curvature ratio with no flat-scalar-spectrum counterpart). The
        coefficient channel measures CONSISTENCY (a0 > 0 volume term, a2/a4 -> 0
        as N grows), not the continuum ratio.
      * the leading coefficient ``a_0`` may drift with N (cf. F-012 alpha-drift).

    Formula: return-probability-uv-ir, spectral-dimension-def,
             heat-kernel-action.
    Evidence: VYPOCET-38 (core-data/calculations/ncg-spectral-dimension/calc.py);
        the discrete d_s plateau ~2 (BD probe, 2D) matches F-001/F-002; the
        coefficient channel is the discrete avatar of the Gilkey/Vassilevich
        ``a_2k`` read by toe.ncg.
    Conventions: ``Z`` un-normalised (the 1/N normalisation cancels in the log
        derivative); plateau located as the widest small-sigma window where
        ``|d_s - target|`` is below ``plateau_tol`` with ``target = 2 round(med/2)``;
        coefficient fit on the ``fit_window_dec`` decades just BELOW the plateau
        centre (small-sigma side, where ``Z ~ sigma^{-D/2}`` holds best).

    Args:
        d2:             1-D array of NON-negative eigenvalues of ``D^2``.
        D:              topological (spacetime) dimension for the ``sigma^{D/2}``
                        prefactor (2 for a 2D causet, 4 for 4D).
        sigmas:         optional log-sigma grid (default: ``np.logspace(2, -5,
                        160)``, ordered IR -> UV).
        plateau_tol:    half-width tolerance for the plateau window in ``d_s``.
        fit_window_dec: number of log10(sigma) decades (below the plateau centre)
                        used for the coefficient fit.

    Returns:
        :class:`HeatKernelSpectrum`.
    """
    d2 = np.asarray(d2, dtype=float)
    d2 = d2[np.isfinite(d2)]
    d2 = np.clip(d2, 0.0, None)
    N = int(d2.size)
    D = float(D)
    if sigmas is None:
        sigmas = np.logspace(2.0, -5.0, 160)
    sigmas = np.asarray(sigmas, dtype=float)

    # Z(sigma) = sum_i exp(-sigma lambda_i), computed stably via log-sum-exp.
    lnZ = np.empty(sigmas.size)
    for k, s in enumerate(sigmas):
        g = -s * d2
        gmax = float(np.max(g))
        lnZ[k] = gmax + np.log(np.sum(np.exp(g - gmax)))
    Z = np.exp(lnZ)

    # d_s(sigma) = -2 d ln Z / d ln sigma  (central difference on the grid).
    lnsig = np.log(sigmas)
    ds = -2.0 * np.gradient(lnZ, lnsig)

    # ---- locate the intermediate plateau (small-sigma side) ----------------
    # restrict to sigma < 1 (UV-ward of the IR turnover) and sigma where Z >~ 1.
    win = (sigmas < 1.0) & (Z > 1.5)
    if np.count_nonzero(win) >= 3:
        med = float(np.median(ds[win]))
        target = 2.0 * round(med / 2.0) if med > 0 else 2.0
        if target <= 0:
            target = 2.0
        good = win & (np.abs(ds - target) < plateau_tol)
    else:
        good = np.zeros_like(win)
        target = 2.0
    if np.count_nonzero(good) >= 2:
        ds_plateau = float(np.median(ds[good]))
        ds_plateau_se = float(np.std(ds[good]))
        sg = sigmas[good]
        plateau_lo = float(np.min(sg))
        plateau_hi = float(np.max(sg))
        plateau_width_dec = float(np.log10(plateau_hi) - np.log10(plateau_lo))
        have_plateau = True
    else:
        ds_plateau = float(np.median(ds[win])) if np.count_nonzero(win) else float("nan")
        ds_plateau_se = float("nan")
        plateau_lo = plateau_hi = plateau_width_dec = float("nan")
        have_plateau = False

    # ---- small-sigma Seeley-DeWitt coefficient fit -------------------------
    # Z(sigma) sigma^{D/2} ~ a0 + a2 sigma + a4 sigma^2 fitted STRICTLY INSIDE the
    # located d_s plateau, where the leading sigma^{-D/2} scaling holds best. If
    # no plateau was found, fall back to a fixed window just below sigma = 1.
    if have_plateau:
        fit_mask = (sigmas >= plateau_lo) & (sigmas <= plateau_hi)
    else:
        s_hi = 0.1
        s_lo = s_hi * 10.0 ** (-float(fit_window_dec))
        fit_mask = (sigmas >= s_lo) & (sigmas <= s_hi)
    if np.count_nonzero(fit_mask) >= 4:
        sf = sigmas[fit_mask]
        yf = Z[fit_mask] * sf ** (D / 2.0)
        coef = np.polyfit(sf, yf, 2)   # [a4, a2, a0] (highest power first)
        a4, a2, a0 = float(coef[0]), float(coef[1]), float(coef[2])
        yhat = np.polyval(coef, sf)
        ss_res = float(np.sum((yf - yhat) ** 2))
        ss_tot = float(np.sum((yf - yf.mean()) ** 2))
        coeff_fit_r2 = 1.0 - ss_res / ss_tot if ss_tot > 0 else 1.0
    else:
        a0 = a2 = a4 = float("nan")
        coeff_fit_r2 = float("nan")
    a2_over_a0 = a2 / a0 if (a0 not in (0.0,) and np.isfinite(a0)) else float("nan")
    a4_over_a0 = a4 / a0 if (a0 not in (0.0,) and np.isfinite(a0)) else float("nan")

    return HeatKernelSpectrum(
        sigmas=sigmas, Z=Z, ds=ds,
        ds_plateau=ds_plateau, ds_plateau_se=ds_plateau_se,
        plateau_lo=plateau_lo, plateau_hi=plateau_hi,
        plateau_width_dec=plateau_width_dec,
        a0=a0, a2=a2, a4=a4,
        a2_over_a0=a2_over_a0, a4_over_a0=a4_over_a0,
        coeff_fit_r2=coeff_fit_r2, N=N,
    )
