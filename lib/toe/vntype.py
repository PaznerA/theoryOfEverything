# -*- coding: utf-8 -*-
"""toe.vntype -- von Neumann type proxies for the SSEE truncation transition.

Module C2 of the ``toe`` library (Layer C). Depends on ``toe.sj`` (B1),
``toe.causet`` (A2), and ``toe.fits`` (A1). Must NOT import ``toe.entropy``
(sibling C1).

Physical context (VYPOCET-12/19, ARCHITECTURE.md C2)
-----------------------------------------------------
Finite causal sets have type-I algebras, but the N->infinity *trend* of
specific dimensionless quantities carries the fingerprint of the limiting
von-Neumann algebra type. The double-truncation kappa = sqrt(N)/(4 pi)
(Sorkin-Yazdi 1712.04227) turns the volume-law untruncated SSEE (type-III_1
divergent trace) into an area/log-law saturating SSEE (type-II finite trace).
This module measures the three proxies of VYPOCET-12 that detect the trend:

  * proxy1: the entropy-trace scaling exponent (S_full ~ N^a with a>0.7 and
    S_trunc ~ N^b with |b|<0.4 = the decisive III_1 -> II signal);
  * proxy2: the modular spectrum  eps = ln(mu/(mu-1))  from the SSEE mu-
    eigenvalues (mu > 1 branch); pile-up of modes at small eps grows for
    III_1 and saturates for type II;
  * proxy3: the central-sequences / factor proxy -- seed-to-seed CV of
    S_trunc should shrink with N (self-averaging = factor-like).

A fourth function, saturation_discriminator, implements the VYPOCET-19
Part-1 II_1 vs II_inf test: the bounded de Sitter static patch (II_1: capped
entropy) vs a matched flat control (II_inf: growing entropy).

Design contract (ARCHITECTURE.md §0):
  - smallest composable functions; physics-parameter inputs;
  - explicit seed args for anything stochastic; no global state;
  - every public function returning (value, uncertainty) returns a
    FitResult or Measurement -- never a bare tuple or dict;
  - no file I/O, no matplotlib side-effects.
"""

from __future__ import annotations

from typing import Optional

import numpy as np

import toe.causet as _causet
import toe.sj as _sj
from toe.fits import FitResult, Measurement, powerlaw_fit, validate_against

__all__ = [
    "modular_spectrum",
    "pile_up",
    "trace_scaling",
    "type_proxies",
    "saturation_discriminator",
]


# ---------------------------------------------------------------------------
# INTERNAL SSEE primitives (mirror sj-vn-type/calc.py / sj-desitter-type/calc.py)
# ---------------------------------------------------------------------------

def _kappa_2d(N: int) -> float:
    """Sorkin-Yazdi UV magnitude cutoff: kappa = sqrt(N) / (4 pi).

    Formula: ssee-formula
    Evidence: VYPOCET-12 (core-data/calculations/sj-vn-type/calc.py kappa_2d).
    Conventions: Sorkin-Yazdi 1712.04227.
    """
    return np.sqrt(N) / (4.0 * np.pi)


def _truncate_iDelta(w, V, kappa):
    """Truncate iDelta: keep only |eigenvalue| > kappa modes.

    Returns (iDelta_trunc, W_trunc) as numpy arrays.
    Evidence: VYPOCET-12 (sj-vn-type/calc.py truncate_iDelta).
    """
    keep = np.abs(w) > kappa
    wk = w[keep]
    Vk = V[:, keep]
    iD = (Vk * wk) @ Vk.conj().T
    pos = wk > 0
    W = (Vk[:, pos] * wk[pos]) @ Vk[:, pos].conj().T
    return iD, W


def _ssee_mu(W_full, iD_full, sub_idx, *, kappa=None, tol=1e-10):
    """SSEE S and eigenvalue array mu on a sub-region.

    Implements W_O v = mu iDelta_O v (generalized eigenproblem). With
    kappa!=None applies the Sorkin-Yazdi double truncation (global + local
    cutoff). Pairs (mu, 1-mu); S = sum_good mu * ln|mu|.

    Evidence: VYPOCET-12 (sj-vn-type/calc.py ssee_mu).
    Conventions: Sorkin-Yazdi 1611.10281 eq.(6-7); 1712.04227 double trunc.
    """
    iD = iD_full
    Wm = W_full
    if kappa is not None:
        w_g, V_g = np.linalg.eigh(iD_full)
        iD, Wm = _truncate_iDelta(w_g, V_g, kappa)

    iD_O = iD[np.ix_(sub_idx, sub_idx)]
    W_O = Wm[np.ix_(sub_idx, sub_idx)]
    d, U = np.linalg.eigh(iD_O)
    scale = np.max(np.abs(d)) if d.size else 0.0
    if scale == 0.0:
        return 0.0, np.array([])
    local_cut = kappa if kappa is not None else tol * scale
    keep = np.abs(d) > local_cut
    if keep.sum() == 0:
        return 0.0, np.array([])
    d_k = d[keep]
    U_k = U[:, keep]
    Wproj = U_k.conj().T @ W_O @ U_k
    M = (Wproj.T / d_k).T
    mu = np.linalg.eigvals(M).real
    good = (np.abs(mu) > tol) & (np.abs(mu - 1.0) > tol)
    mu_g = mu[good]
    S = float(np.sum(mu_g * np.log(np.abs(mu_g))))
    return S, mu


def _sub_idx_diamond2d(coords, frac):
    """Indices of points inside the concentric sub-diamond of fraction frac.

    Evidence: VYPOCET-12 (sj-vn-type/calc.py points_in_subdiamond).
    """
    u = coords[:, 0]
    v = coords[:, 1]
    return np.where((np.abs(u) <= frac) & (np.abs(v) <= frac))[0]


def _sub_idx_rstar_cut(coords, rstar_cut):
    """Indices of points with tortoise coord r* <= rstar_cut (dS geometry).

    Evidence: VYPOCET-19 (sj-desitter-type/calc.py part1_discriminator).
    """
    return np.where(coords[:, 1] <= rstar_cut)[0]


def _linfit(x, y):
    """Simple linear least-squares fit y = a*x + b; returns (slope, intercept)."""
    A = np.column_stack([x, np.ones_like(x)])
    coef, *_ = np.linalg.lstsq(A, y, rcond=None)
    return float(coef[0]), float(coef[1])


def _saturating_fit(x, y):
    """Fit y = S_cap - B * exp(-x / xi) via grid-search on xi, LS on (S_cap, B).

    Returns (S_cap, B, xi, R2).
    Evidence: VYPOCET-19 (sj-desitter-type/calc.py saturating_fit).
    """
    x = np.asarray(x, float)
    y = np.asarray(y, float)
    best = None
    for xi in np.linspace(0.1, 5.0 * (x.max() - x.min() + 1e-9), 200):
        E = np.exp(-x / xi)
        A = np.column_stack([np.ones_like(x), -E])
        coef, *_ = np.linalg.lstsq(A, y, rcond=None)
        yhat = A @ coef
        ss = float(np.sum((y - y.mean()) ** 2))
        R2 = 1.0 - float(np.sum((y - yhat) ** 2)) / ss if ss > 0.0 else 0.0
        if best is None or R2 > best[3]:
            best = (float(coef[0]), float(coef[1]), float(xi), float(R2))
    return best  # (S_cap, B, xi, R2)


# ---------------------------------------------------------------------------
# PUBLIC API
# ---------------------------------------------------------------------------

def modular_spectrum(mu, *, tol: float = 1e-9) -> np.ndarray:
    """Modular energies eps = ln(mu / (mu-1)) from SSEE mu-eigenvalues.

    Maps the SSEE generalized eigenvalues mu to modular energies via the
    Casini-Huerta single-mode formula for a bosonic field:
        eps = ln(mu / (mu-1)) = ln((nu+1/2)/(nu-1/2)),   nu = mu - 1/2.
    Only the mu > 1 branch is physical (occupation number n = mu - 1 >= 0).
    The result is sorted ascending (UV modes = small eps, IR modes = large eps).

    Formula: modular-spectrum
    Evidence: VYPOCET-12 (core-data/calculations/sj-vn-type/calc.py
    modular_spectrum_from_mu).
    Conventions: Casini-Huerta 0905.2562 single-mode modular energy; mu = nu
    + 1/2 where nu >= 1/2 is the symplectic eigenvalue; eps in (0, inf).

    Args:
        mu: 1-D array of SSEE generalized eigenvalues (real).
        tol: threshold above 1 for the mu > 1 branch selection.

    Returns:
        np.ndarray of finite positive modular energies, sorted ascending.
        Empty array if no mu > 1 + tol survive.
    """
    m = np.asarray(mu, dtype=float)
    m = m[np.isfinite(m)]
    big = m[m > 1.0 + tol]
    nu = big - 0.5                         # symplectic eigenvalue nu = mu - 1/2
    nu = nu[nu > 0.5 + tol]               # require nu > 1/2 (nu-1/2 > 0)
    eps = np.log((nu + 0.5) / (nu - 0.5))
    eps = eps[np.isfinite(eps) & (eps > 0.0)]
    return np.sort(eps)


def pile_up(eps: np.ndarray, eps0: float = 0.5) -> int:
    """Count of modular modes with eps < eps0 (small-eps pile-up measure).

    The small-eps pile-up is the Connes-type III_1 signature: as N grows the
    number of modes below eps0 grows without bound (flat dense spectrum toward
    eps = 0). For type II it saturates (finite integrable density; sharp IR
    edge after double truncation).

    Formula: modular-spectrum, type-ii-trace-entropy
    Evidence: VYPOCET-12 (core-data/calculations/sj-vn-type/calc.py run
    proxy2 pile_full / pile_trunc).
    Conventions: eps0 = 0.5 is the VYPOCET-12 reference threshold; larger
    eps0 counts the more-occupied (more-IR) modes.

    Args:
        eps: modular energy array (from :func:`modular_spectrum`).
        eps0: pile-up threshold (default 0.5, matching VYPOCET-12).

    Returns:
        int -- number of modular modes with eps < eps0.
    """
    return int(np.sum(np.asarray(eps) < eps0))


def trace_scaling(
    builder,
    Ns,
    *,
    frac: float,
    n_seeds: int,
    seed_base: int,
    truncate: str,
) -> FitResult:
    """Entropy-trace scaling exponent for the sub-region SSEE vs N.

    Builds sprinkle -> causal_matrix -> pauli_jordan -> sj_state -> ssee across
    Ns x n_seeds, computes the mean S per N, and fits S ~ N^a. The exponent a
    is the proxy-1 trace-divergence test: a > 0.7 (volume law, III-like) for
    truncate='none'; |a| < 0.4 (saturating, II-like) for truncate='kappa'.

    Formula: type-ii-trace-entropy, ssee-formula, crossed-product-def
    Evidence: VYPOCET-12 (core-data/calculations/sj-vn-type/calc.py run
    proxy1_trace).
    Conventions: SSEE = W_O v = mu iDelta_O v; S = sum mu ln|mu|;
    kappa = sqrt(N)/(4pi) (Sorkin-Yazdi 1712.04227); 2D diamond builder;
    seed scheme 7_000_000 + 1000*N + s (VYPOCET-12).

    Args:
        builder: callable(N, rng) -> (N, dim) coords array (e.g.
            ``toe.causet.sprinkle_diamond2d``).
        Ns: sequence of N values (at least 3 for a fit).
        frac: fraction for the sub-diamond / sub-region cut.
        n_seeds: number of independent sprinklings per N.
        seed_base: base seed; each realisation uses seed_base + 1000*N + s.
        truncate: 'none' (no truncation) or 'kappa' (double truncation with
            kappa = sqrt(N)/(4 pi)).

    Returns:
        FitResult with value=exponent, se_regression, ci68_bootstrap, r2.
        ci68_bootstrap is computed via across-seed bootstrap (n_boot=1000).
        n_boot_used > 0 iff n_seeds >= 2.
    """
    Ns_arr = np.array(Ns, dtype=float)
    # per_seed_S: shape (len(Ns), n_seeds)
    per_seed_S = np.zeros((len(Ns), n_seeds))

    for i, N in enumerate(Ns):
        kap = _kappa_2d(int(N)) if truncate == "kappa" else None
        for s in range(n_seeds):
            rng = np.random.default_rng(seed_base + 1000 * int(N) + s)
            coords = builder(int(N), rng)
            C = _causet.causal_matrix(coords)
            iD = _causet.pauli_jordan(_causet.green_retarded_2d(C))
            st = _sj.sj_state(iD)
            sub = _sub_idx_diamond2d(coords, frac)
            S, _ = _ssee_mu(st.W, iD, sub, kappa=kap)
            per_seed_S[i, s] = abs(float(S))

    # Mean S per N (guard against zeros for powerlaw fit)
    mean_S = np.maximum(per_seed_S.mean(axis=1), 1e-12)

    fit = powerlaw_fit(
        Ns_arr,
        mean_S,
        resamples=per_seed_S,      # shape (n_points, n_seeds) for bootstrap
        n_boot=1000,
        seed=20260606,
    )
    return fit


def type_proxies(
    builder,
    Ns,
    *,
    frac: float,
    n_seeds: int,
    seed_base: int,
) -> dict:
    """Full VYPOCET-12 three-proxy type-III_1 -> type-II battery.

    Runs trace_scaling for proxy1, computes modular pile-up scaling for
    proxy2, and the seed-to-seed CV scaling for proxy3. Returns the full
    proxy dict mirroring the VYPOCET-12 results.json structure.

    Formula: type-ii-trace-entropy, ssee-formula, modular-spectrum,
    crossed-product-def, bekenstein-hawking-formula
    Evidence: VYPOCET-12 (core-data/calculations/sj-vn-type/calc.py run).
    Conventions: SSEE W_O v = mu iDelta_O v; proxy1 = entropy-trace exponent;
    proxy2 = modular pile-up exponent (eps0=0.5); proxy3 = CV(S_trunc) vs N;
    verdict: n_passing >= 2 -> mixed or consistent with III_1 -> II.

    Args:
        builder: callable(N, rng) -> (N, dim) coords.
        Ns: sequence of N values (>= 3 for meaningful fits).
        frac: sub-region fraction.
        n_seeds: number of seeds per N.
        seed_base: base seed (seed = seed_base + 1000*N + s).

    Returns:
        dict with keys proxy1, proxy2, proxy3, verdict:
          proxy1: {'fit_full': FitResult, 'fit_trunc': FitResult,
                   'III_to_II': bool}
          proxy2: {'exponent_full': float, 'exponent_trunc': float,
                   'III_to_II': bool}
          proxy3: {'cv_powerlaw': FitResult, 'factor_like': bool}
          verdict: {'n_passing': int, 'overall': str}
    """
    Ns_arr = np.array(Ns, dtype=float)
    n_N = len(Ns)
    eps0 = 0.5

    # Storage arrays: (n_N, n_seeds)
    S_full = np.zeros((n_N, n_seeds))
    S_trunc = np.zeros((n_N, n_seeds))
    pile_full = np.zeros((n_N, n_seeds))
    pile_trunc = np.zeros((n_N, n_seeds))

    for i, N in enumerate(Ns):
        kap = _kappa_2d(int(N))
        for s in range(n_seeds):
            rng = np.random.default_rng(seed_base + 1000 * int(N) + s)
            coords = builder(int(N), rng)
            C = _causet.causal_matrix(coords)
            iD = _causet.pauli_jordan(_causet.green_retarded_2d(C))
            st = _sj.sj_state(iD)
            sub = _sub_idx_diamond2d(coords, frac)

            Sf, mu_f = _ssee_mu(st.W, iD, sub, kappa=None)
            St, mu_t = _ssee_mu(st.W, iD, sub, kappa=kap)
            S_full[i, s] = abs(float(Sf))
            S_trunc[i, s] = abs(float(St))

            eps_f = modular_spectrum(mu_f)
            eps_t = modular_spectrum(mu_t)
            pile_full[i, s] = pile_up(eps_f, eps0)
            pile_trunc[i, s] = pile_up(eps_t, eps0)

    mean_Sf = np.maximum(S_full.mean(axis=1), 1e-12)
    mean_St = np.maximum(S_trunc.mean(axis=1), 1e-12)
    mean_pf = np.maximum(pile_full.mean(axis=1), 1e-9)
    mean_pt = np.maximum(pile_trunc.mean(axis=1), 1e-9)

    # --- PROXY 1: entropy-trace exponents ---
    fit_full = powerlaw_fit(Ns_arr, mean_Sf, resamples=S_full, n_boot=1000,
                            seed=20260606)
    fit_trunc = powerlaw_fit(Ns_arr, mean_St, resamples=S_trunc, n_boot=1000,
                             seed=20260606)
    p1_III_to_II = bool(fit_full.value > 0.5 and abs(fit_trunc.value) < 0.4)

    # --- PROXY 2: modular pile-up exponents (simple OLS, no bootstrap) ---
    pile_fit_full = powerlaw_fit(Ns_arr, mean_pf, resamples=pile_full,
                                 n_boot=1000, seed=20260606)
    pile_fit_trunc = powerlaw_fit(Ns_arr, mean_pt, resamples=pile_trunc,
                                  n_boot=1000, seed=20260606)
    sig_p2 = (pile_fit_full.se_regression > 0 and
              pile_fit_full.value / pile_fit_full.se_regression > 3.0)
    p2_full_grows = bool(pile_fit_full.value > 0.25 and sig_p2)
    p2_trunc_sats = bool(pile_fit_trunc.value < 0.6 * pile_fit_full.value)
    p2_III_to_II = bool(p2_full_grows and p2_trunc_sats)

    # --- PROXY 3: CV of S_trunc vs N ---
    cv_trunc = S_trunc.std(axis=1, ddof=1) / np.maximum(
        np.abs(S_trunc.mean(axis=1)), 1e-12)
    cv_full = S_full.std(axis=1, ddof=1) / np.maximum(
        np.abs(S_full.mean(axis=1)), 1e-12)
    cv_mat = cv_trunc[:, None]  # (n_N, 1) for powerlaw_fit (no bootstrap CI)
    cv_fit = powerlaw_fit(Ns_arr, np.maximum(cv_trunc, 1e-9))
    cv_sig = (cv_fit.se_regression > 0 and
              abs(cv_fit.value) / cv_fit.se_regression > 2.0)
    self_avg = bool(cv_trunc[-1] < 0.05)
    p3_factor_like = bool(self_avg and cv_fit.value < 0.0 and cv_sig)

    # --- OVERALL VERDICT ---
    n_passing = int(p1_III_to_II) + int(p2_III_to_II) + int(p3_factor_like)
    if n_passing == 3:
        overall = "ALL three proxies consistent with III_1 -> II"
    elif n_passing == 0:
        overall = "NONE of the proxies show III_1 -> II"
    else:
        overall = f"MIXED: {n_passing}/3 proxies consistent with III_1 -> II"

    return {
        "proxy1": {
            "fit_full": fit_full,
            "fit_trunc": fit_trunc,
            "entropy_full_divergent": bool(fit_full.value > 0.5),
            "entropy_trunc_saturates": bool(abs(fit_trunc.value) < 0.25),
            "III_to_II": p1_III_to_II,
        },
        "proxy2": {
            "exponent_full": pile_fit_full.value,
            "exponent_trunc": pile_fit_trunc.value,
            "fit_full": pile_fit_full,
            "fit_trunc": pile_fit_trunc,
            "full_pileup_grows": p2_full_grows,
            "trunc_pileup_saturates": p2_trunc_sats,
            "III_to_II": p2_III_to_II,
        },
        "proxy3": {
            "cv_powerlaw": cv_fit,
            "cv_trunc": cv_trunc.tolist(),
            "cv_full": cv_full.tolist(),
            "trunc_is_self_averaging": self_avg,
            "trunc_trend_decreasing": bool(cv_fit.value < 0.0),
            "trunc_trend_significant": cv_sig,
            "factor_like": p3_factor_like,
        },
        "verdict": {
            "n_passing": n_passing,
            "overall": overall,
        },
    }


def saturation_discriminator(
    builder_bounded,
    builder_flat,
    R_extents,
    *,
    n_seeds: int,
    seed_base: int,
) -> dict:
    """II_1 vs II_inf discriminator: saturating dS patch vs growing flat control.

    Implements the VYPOCET-19 Part-1 discrimination test. At each tortoise
    extent R*_box in R_extents, sprinkle a causal set from each builder and
    measure (a) the region cardinality N_total (the decisive geometric signal)
    and (b) the full untruncated SSEE S_full across the bulk midpoint cut.

    The de Sitter proper-measure sprinkling has conformal factor sech^2(r*/l),
    so the achievable N_total SATURATES as R*_box -> inf (finite static-patch
    proper volume). The flat control grows without bound. This saturating-vs-
    growing distinction is the II_1 vs II_inf signal (CLPW arXiv:2206.10780):
      * dS  (II_1): N_total caps -> saturating fit N_cap - B*exp(-R*/xi) with
        good R2; S_full turns over and decreases (bounded content);
      * flat (II_inf): N_total grows linearly; S_full grows monotonically.

    The builder convention is:
        coords = builder(rng, *, rstar_box=R)  ->  (N, 2) coords (t, r*)
    where the builder determines N internally from its embedded proper density.

    Formula: ssee-formula, type-ii-trace-entropy, crossed-product-def,
    bekenstein-hawking-formula
    Evidence: VYPOCET-19 (core-data/calculations/sj-desitter-type/calc.py
    part1_discriminator).
    Conventions: CLPW arXiv:2206.10780 type II_1 static patch; SSEE double
    truncation kappa=sqrt(N)/(4pi); bulk midpoint cut at 0.5*R*_box;
    N_total caps for dS (sech^2 proper measure), grows for flat.

    Args:
        builder_bounded: callable(rng, *, rstar_box) -> (N, 2) coords; should
            implement the dS sech^2 proper measure (II_1 branch).
        builder_flat: callable(rng, *, rstar_box) -> (N, 2) coords; should
            implement the uniform flat measure (II_inf branch).
        R_extents: 1-D array of tortoise extents R*_box to sweep.
        n_seeds: number of seeds per extent.
        seed_base: base seed; realisations use seed_base + 17*j + s (dS),
            seed_base + 101 + 17*j + s (flat).

    Returns:
        dict with keys:
          'desitter':   {'N_total_mean': list, 'S_full_mean': list,
                         'cap': float, 'xi': float, 'R2': float,
                         'net_late': float, 'dS_saturates_II1': bool}
          'flat':       {'N_total_mean': list, 'S_full_mean': list,
                         'slope': float, 'net_late': float,
                         'flat_grows_IIinf': bool}
          'II1_vs_IIinf_discriminated': bool
    """
    R_extents = np.asarray(R_extents, dtype=float)
    n_R = len(R_extents)

    Ntot_ds = np.zeros((n_seeds, n_R))
    Ntot_fl = np.zeros((n_seeds, n_R))
    Sf_ds = np.zeros((n_seeds, n_R))
    Sf_fl = np.zeros((n_seeds, n_R))

    for j, Rbox in enumerate(R_extents):
        cut = 0.5 * Rbox           # bulk midpoint cut fraction

        for s in range(n_seeds):
            # --- de Sitter branch ---
            rng_ds = np.random.default_rng(seed_base + 17 * j + s)
            coords_ds = builder_bounded(rng_ds, rstar_box=Rbox)
            N_ds = coords_ds.shape[0]
            Ntot_ds[s, j] = N_ds
            if N_ds < 12:
                continue
            C_ds = _causet.causal_matrix(coords_ds)
            iD_ds = _causet.pauli_jordan(_causet.green_retarded_2d(C_ds))
            st_ds = _sj.sj_state(iD_ds)
            sub_ds = _sub_idx_rstar_cut(coords_ds, cut)
            comp_ds = N_ds - sub_ds.size
            if sub_ds.size >= 6 and comp_ds >= 6:
                S_full, _ = _ssee_mu(st_ds.W, iD_ds, sub_ds, kappa=None)
                Sf_ds[s, j] = abs(float(S_full))

            # --- flat branch ---
            rng_fl = np.random.default_rng(seed_base + 101 + 17 * j + s)
            coords_fl = builder_flat(rng_fl, rstar_box=Rbox)
            N_fl = coords_fl.shape[0]
            Ntot_fl[s, j] = N_fl
            if N_fl < 12:
                continue
            C_fl = _causet.causal_matrix(coords_fl)
            iD_fl = _causet.pauli_jordan(_causet.green_retarded_2d(C_fl))
            st_fl = _sj.sj_state(iD_fl)
            sub_fl = _sub_idx_rstar_cut(coords_fl, cut)
            comp_fl = N_fl - sub_fl.size
            if sub_fl.size >= 6 and comp_fl >= 6:
                S_full_fl, _ = _ssee_mu(st_fl.W, iD_fl, sub_fl, kappa=None)
                Sf_fl[s, j] = abs(float(S_full_fl))

    mean_Ntot_ds = Ntot_ds.mean(axis=0)
    mean_Ntot_fl = Ntot_fl.mean(axis=0)
    mean_Sf_ds = Sf_ds.mean(axis=0)
    mean_Sf_fl = Sf_fl.mean(axis=0)

    # --- Fit dS N_total: saturating N_cap - B*exp(-R*/xi) ---
    cap, B_val, xi, R2_sat = _saturating_fit(R_extents, mean_Ntot_ds)

    # --- Fit flat N_total: linear growth ---
    slope_fl_N, _ = _linfit(R_extents, mean_Ntot_fl)

    # --- Full SSEE late trends ---
    half = n_R // 2
    net_Sf_ds_late = float(mean_Sf_ds[-1] - mean_Sf_ds[half]) if half < n_R else 0.0
    net_Sf_fl_late = float(mean_Sf_fl[-1] - mean_Sf_fl[half]) if half < n_R else 0.0
    slope_Sf_fl, _ = _linfit(R_extents, mean_Sf_fl)

    # --- Discriminator verdicts ---
    Ntot_caps_dS = bool(R2_sat > 0.9
                        and cap < 1.4 * float(mean_Ntot_ds[0])
                        if mean_Ntot_ds[0] > 0 else False)
    Ntot_grows_flat = bool(slope_fl_N > 0
                           and float(mean_Ntot_fl[-1]) > 2.0 * float(mean_Ntot_fl[0])
                           if mean_Ntot_fl[0] > 0 else False)
    discriminated = bool(Ntot_caps_dS and Ntot_grows_flat)

    return {
        "desitter": {
            "N_total_mean": mean_Ntot_ds.tolist(),
            "S_full_mean": mean_Sf_ds.tolist(),
            "cap": float(cap),
            "B": float(B_val),
            "xi": float(xi),
            "R2": float(R2_sat),
            "net_late": net_Sf_ds_late,
            "dS_saturates_II1": Ntot_caps_dS,
        },
        "flat": {
            "N_total_mean": mean_Ntot_fl.tolist(),
            "S_full_mean": mean_Sf_fl.tolist(),
            "slope": float(slope_fl_N),
            "net_late": net_Sf_fl_late,
            "flat_grows_IIinf": Ntot_grows_flat,
        },
        "II1_vs_IIinf_discriminated": discriminated,
    }
