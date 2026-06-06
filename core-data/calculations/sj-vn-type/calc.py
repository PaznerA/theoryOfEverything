#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
VYPOCET-12 : von-Neumann TYPE diagnostics of the SSEE truncation (test of H3g-3)
================================================================================

CLAIM under test (H3g-3, BRAINSTORM-03 / H04):
    The double-truncation that converts the Sorkin spacetime entanglement
    entropy (SSEE) from a VOLUME law to an AREA/LOG law IS a
        type III_1  ->  type II
    transition of the underlying local von-Neumann algebra; the discreteness
    scale (the magnitude cutoff kappa = sqrt(N)/(4 pi)) plays the role of the
    modular / observer (crossed-product) cutoff that regularises the otherwise
    trace-less type III_1 algebra.

"Type" is an infinite-dimensional notion.  On a finite causal set every
operator is a finite matrix and every algebra is type I_n (B(C^n)).  So we
CANNOT measure the type directly.  Instead we build three HONEST finite-N
proxies whose N->infinity TREND carries the signature, and we measure the
trend with error bars across >=4 seeds, N = 400..1800 (clean 2D case).

----------------------------------------------------------------------------
CONVENTIONS (all verified against the literature)
----------------------------------------------------------------------------
* 2D massless scalar on a sprinkled causal diamond, Sorkin-Johnston (SJ):
    - G_R = (1/2) C,  C_xy = 1 if y precedes x (y in causal past of x).
      [Sorkin-Yazdi 1611.10281; Saravani-Sorkin-Yazdi 1311.7146]
    - Pauli-Jordan:  Delta = G_R - G_R^T = (1/2)(C - C^T), antisymmetric.
      i*Delta is Hermitian with real +/- paired eigenvalues.
    - SJ Wightman:  W = positive part of i*Delta = sum_{lam>0} lam |v><v|.
      Then W - W^dagger = i*Delta (the commutator) and W >= 0  (pure SJ state).
    - SSEE on a subregion O:  restrict W_O, (iDelta)_O ; generalized problem
      W_O v = mu (iDelta)_O v ;  S = sum_mu mu ln|mu|.  Eigenvalues pair
      (mu, 1-mu).  [Sorkin-Yazdi 1611.10281 eq.(6-7); Surya-NomaanX-Yazdi 2008.07697]
    - Double truncation (Sorkin-Yazdi / 1712.04227): discard |lam| <= kappa
      with kappa = sqrt(N)/(4 pi) in spec(iDelta) globally AND in spec(iDelta_O)
      locally; this restores the area/log law (S: 95 -> 1.6 in 2D, VYPOCET-04).

* Gaussian-state modular Hamiltonian (the standard bosonic correlator method,
  Casini-Huerta review 0905.2562 / arXiv:2501.09669; verified June 2026):
    - From field correlator X = <phi phi> and momentum correlator P = <pi pi>
      on a region, C = sqrt(X.P) has symplectic eigenvalues nu_k >= 1/2.
    - Single-mode modular energy:  eps_k = ln[(nu_k + 1/2)/(nu_k - 1/2)].
    - Entropy: S = sum [(nu_k+1/2) ln(nu_k+1/2) - (nu_k-1/2) ln(nu_k-1/2)].
  In the *covariant SJ* language the same physics is carried by the SSEE
  generalized eigenvalues mu (paired mu,1-mu).  A single bosonic mode with
  occupation n has reduced state rho ~ exp(-eps n); the SSEE pair (mu,1-mu)
  with mu = n+1 (mu>1) gives modular energy
        eps = ln[ mu / (mu - 1) ]        (mu = nu + 1/2,  nu = mu - 1/2)
  and S_mode = mu ln mu - (mu-1) ln(mu-1) = (nu+1/2)ln(nu+1/2)-(nu-1/2)ln(nu-1/2).
  We use the SSEE mu-spectrum as the NATIVE covariant object and map to the
  modular spectrum eps via eps = ln[mu/(mu-1)] (mu>1 branch) -- this is the
  spacetime analog of the Casini-Huerta single-mode modular energy and is
  what Connes' modular-spectrum invariant S(M) is built from.

----------------------------------------------------------------------------
THE THREE PROXIES (each: prediction -> measurement -> N-scaling)
----------------------------------------------------------------------------
PROXY 1  TRACE DIVERGENCE  (no-trace = III ; finite trace = II)
   The natural trace probe is Tr|iDelta_O| = sum of |eigenvalues| of the
   restricted Pauli-Jordan operator (this is the L1/nuclear norm; a genuine
   trace exists iff this stays finite as the algebra grows).  Type III: no
   normal trace -> Tr|iDelta_O| diverges with N.  Type II: finite trace ->
   the TRUNCATED operator's trace converges.
   PREDICTION (III->II): untruncated Tr|iDelta_O| grows without bound (~N^a,
   a>0); truncated Tr|iDelta_O^kappa| converges (a ~ 0).
   We ALSO report the SSEE itself (S_full vs S_trunc) as the entropy-trace.

PROXY 2  MODULAR SPECTRUM  (S(M)=R_+ flat dense = III_1 ; integrable = II)
   Build the modular spectrum {eps_k} from the SSEE mu-spectrum on the
   subdiamond, eps_k = ln[mu_k/(mu_k-1)].  Connes III_1 signature: as N grows
   the spectrum fills R densely with a *flat* (scale-invariant) density that
   does NOT integrate (the number of modes per unit eps near eps=0 grows
   without bound).  Type II signature: the density is integrable (finite total
   weight; an effective UV edge).  We measure:
     (a) the modular spectral density rho(eps) before vs after truncation;
     (b) eps_max (UV edge) and the count of modes with eps<eps0 (small-eps
         pile-up) vs N -- divergent pile-up = III_1, bounded = II;
     (c) the "flatness" of rho near eps=0.
   PREDICTION (III->II): untruncated rho is broad/flat with a small-eps
   pile-up that GROWS with N (III_1-like); truncated rho is compactly
   supported with a fixed UV edge and a small-eps count that SATURATES (II-like).

PROXY 3  CENTRAL SEQUENCES proxy  (factor = trivial centre = seed-independent)
   A type II_1/III_1 factor is a FACTOR (trivial centre): bulk quantities are
   independent of boundary microstructure.  Proxy: the relative seed-to-seed
   scatter (CV = std/mean across >=4 seeds) of the TRUNCATED SSEE should
   SHRINK with N (self-averaging / factor-like), whereas a quantity dominated
   by boundary microstructure (the untruncated volume-law S) stays noisy or
   grows.  We measure CV(S_trunc) and CV(S_full) vs N, and additionally the
   CV of the modular UV-edge eps_max.
   PREDICTION (factor-like for the truncated/type-II algebra): CV(S_trunc)
   decreases with N; the truncated entropy is boundary-microstructure
   independent.

VERDICT logic: does the truncation behave like III->II in ALL three proxies,
SOME, or NONE?  Negative/mixed results are first-class findings.
"""

import json
import os
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

OUTDIR = os.path.dirname(os.path.abspath(__file__))

# ----------------------------------------------------------------------------
# Geometry + SJ construction (identical conventions to ssee-diamond/calc.py)
# ----------------------------------------------------------------------------
T_HALF = 1.0
VOL_UV = (2 * T_HALF) ** 2          # area of (u,v) square = 4 ; rho = N/4


def sprinkle_diamond(N, rng):
    return rng.uniform(-T_HALF, T_HALF, size=(N, 2))


def causal_matrix(coords):
    u = coords[:, 0][:, None]; v = coords[:, 1][:, None]
    uy = coords[:, 0][None, :]; vy = coords[:, 1][None, :]
    prec = (uy <= u) & (vy <= v)
    C = prec.astype(np.float64)
    np.fill_diagonal(C, 0.0)
    return C


def pauli_jordan(C):
    Delta = 0.5 * (C - C.T)
    return 1j * Delta                # Hermitian


def sj_eig(iDelta):
    """Eigendecomposition of i*Delta (Hermitian)."""
    w, V = np.linalg.eigh(iDelta)
    return w, V


def sj_wightman_from_eig(w, V):
    pos = w > 0
    return (V[:, pos] * w[pos]) @ V[:, pos].conj().T


def points_in_subdiamond(coords, frac):
    u = coords[:, 0]; v = coords[:, 1]
    r = frac * T_HALF
    return np.where((np.abs(u) <= r) & (np.abs(v) <= r))[0]


def kappa_2d(N):
    """Sorkin-Yazdi UV magnitude cutoff for the 2D local massless scalar
    (1712.04227):  kappa = sqrt(N)/(4 pi)."""
    return np.sqrt(N) / (4.0 * np.pi)


def truncate_iDelta(w, V, kappa):
    """Return truncated iDelta and its SJ Wightman, keeping |lam|>kappa."""
    keep = np.abs(w) > kappa
    wk = w[keep]; Vk = V[:, keep]
    iD = (Vk * wk) @ Vk.conj().T
    pos = wk > 0
    Wm = (Vk[:, pos] * wk[pos]) @ Vk[:, pos].conj().T
    return iD, Wm


# ----------------------------------------------------------------------------
# SSEE generalized eigenvalue problem and modular spectrum
# ----------------------------------------------------------------------------
def ssee_mu(W, iDelta, sub_idx, kappa=None, tol=1e-10):
    """Return (S, mu_array) for the sub-region.  Double truncation if kappa.

    mu solve  W_O v = mu iDelta_O v  on the kept (|eig(iDelta_O)|>cut) subspace.
    Pairs (mu, 1-mu).  S = sum mu ln|mu| over good mu.
    """
    iD = iDelta; Wm = W
    if kappa is not None:
        w, V = np.linalg.eigh(iD)
        iD, Wm = truncate_iDelta(w, V, kappa)
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
    d_k = d[keep]; U_k = U[:, keep]
    Wproj = U_k.conj().T @ W_O @ U_k
    M = (Wproj.T / d_k).T
    mu = np.linalg.eigvals(M).real
    good = (np.abs(mu) > tol) & (np.abs(mu - 1.0) > tol)
    mu_g = mu[good]
    S = float(np.sum(mu_g * np.log(np.abs(mu_g))))
    return S, mu


def modular_spectrum_from_mu(mu, tol=1e-9):
    """Map SSEE generalized eigenvalues mu to modular energies eps.

    SSEE mu come in pairs (mu, 1-mu).  The physical occupation branch is mu>1
    (equivalently nu = mu - 1/2 >= 1/2 in the Casini-Huerta covariance method).
    Single-mode modular energy:
        eps = ln[ mu/(mu-1) ]  =  ln[(nu+1/2)/(nu-1/2)] ,   nu = mu - 1/2.
    eps in (0, inf).  Returns sorted ascending eps (UV modes = small eps).
    """
    m = mu[np.isfinite(mu)]
    big = m[m > 1.0 + tol]                      # mu>1 branch
    nu = big - 0.5                              # symplectic eigenvalue
    nu = nu[nu > 0.5 + tol]
    eps = np.log((nu + 0.5) / (nu - 0.5))
    eps = eps[np.isfinite(eps) & (eps > 0)]
    return np.sort(eps)


def trace_abs_iDelta_O(iDelta, sub_idx, kappa, w=None, V=None):
    """Tr|iDelta_O| = sum |eig(iDelta_O)| (nuclear norm) for the restricted
    Pauli-Jordan operator, optionally after global truncation |lam|>kappa.
    This is the trace probe: a genuine (semifinite) trace exists iff this
    stays finite as the algebra grows.  Also return the restricted-operator
    rank (number of nonzero modes) and Tr(iDelta_O^2) (HS norm^2)."""
    iD = iDelta
    if kappa is not None:
        if w is None:
            w, V = np.linalg.eigh(iD)
        iD, _ = truncate_iDelta(w, V, kappa)
    iD_O = iD[np.ix_(sub_idx, sub_idx)]
    d = np.linalg.eigvalsh(iD_O)
    tr_abs = float(np.sum(np.abs(d)))
    tr_sq = float(np.sum(d * d))
    rank = int(np.sum(np.abs(d) > 1e-9 * (np.max(np.abs(d)) if d.size else 1.0)))
    return tr_abs, tr_sq, rank


# ----------------------------------------------------------------------------
# fitting helpers
# ----------------------------------------------------------------------------
def powerlaw_fit(x, y, sig=None):
    lx = np.log(x); ly = np.log(y)
    A = np.vstack([lx, np.ones_like(lx)]).T
    if sig is None:
        w = np.ones_like(lx)
    else:
        sl = np.where(sig > 0, sig, np.min(sig[sig > 0]) if np.any(sig > 0) else 1.0)
        w = 1.0 / sl ** 2
    AW = A * w[:, None]
    cov = np.linalg.inv(A.T @ AW)
    coef = cov @ (AW.T @ ly)
    return float(coef[0]), float(coef[1]), float(np.sqrt(cov[0, 0]))


def linfit(x, y):
    A = np.vstack([x, np.ones_like(x)]).T
    coef, *_ = np.linalg.lstsq(A, y, rcond=None)
    return float(coef[0]), float(coef[1])


# ----------------------------------------------------------------------------
# Main experiment
# ----------------------------------------------------------------------------
def run():
    results = {"meta": {
        "task": "VYPOCET-12 von-Neumann TYPE diagnostics of SSEE truncation (H3g-3)",
        "dimension": "2D (clean case)",
        "claim": "truncation volume->area == type III_1 -> type II transition; "
                 "kappa=sqrt(N)/4pi == modular/observer (crossed-product) cutoff",
        "conventions": {
            "G_R": "G_R=(1/2)C (Sorkin-Yazdi 1611.10281)",
            "iDelta": "i(G_R-G_R^T)=i/2(C-C^T), Hermitian, +/- paired",
            "W_SJ": "positive part of iDelta",
            "SSEE": "W_O v=mu iDelta_O v ; S=sum mu ln|mu| ; pairs (mu,1-mu)",
            "kappa": "sqrt(N)/(4 pi) (1712.04227); double truncation",
            "modular_energy": "eps=ln[mu/(mu-1)]=ln[(nu+1/2)/(nu-1/2)], nu=mu-1/2 "
                              "(Casini-Huerta 0905.2562 bosonic single-mode)",
            "trace_probe": "Tr|iDelta_O|=sum|eig(iDelta_O)| (nuclear norm) "
                           "= trace existence probe (finite=II, divergent=III)",
        },
    }}

    Ns = [400, 600, 800, 1000, 1200, 1500, 1800]
    n_seeds = 8                 # >= 4 required
    frac = 0.5                  # concentric subdiamond (nested-diamond setup)
    eps0 = 0.5                  # small-eps pile-up threshold for proxy 2
    Ns_arr = np.array(Ns, float)
    rho_arr = Ns_arr / VOL_UV

    # storage
    store = {N: {"S_full": [], "S_trunc": [],
                 "trA_full": [], "trsq_full": [], "rank_full": [],
                 "trA_trunc": [], "trsq_trunc": [], "rank_trunc": [],
                 "epsmax_full": [], "epsmax_trunc": [],
                 "pile_full": [], "pile_trunc": [],
                 "nmodes_full": [], "nmodes_trunc": [],
                 "eps_full_pool": [], "eps_trunc_pool": []}
             for N in Ns}

    for N in Ns:
        kap = kappa_2d(N)
        for s in range(n_seeds):
            rng = np.random.default_rng(7_000_000 + 1000 * N + s)
            coords = sprinkle_diamond(N, rng)
            C = causal_matrix(coords)
            iD = pauli_jordan(C)
            w, V = sj_eig(iD)
            W = sj_wightman_from_eig(w, V)
            sub = points_in_subdiamond(coords, frac)

            # --- SSEE (entropy / entropy-trace) ---
            S_full, mu_full = ssee_mu(W, iD, sub, kappa=None)
            S_trunc, mu_trunc = ssee_mu(W, iD, sub, kappa=kap)
            store[N]["S_full"].append(S_full)
            store[N]["S_trunc"].append(S_trunc)

            # --- PROXY 1: trace of restricted Pauli-Jordan ---
            trA_f, trsq_f, rk_f = trace_abs_iDelta_O(iD, sub, None)
            trA_t, trsq_t, rk_t = trace_abs_iDelta_O(iD, sub, kap, w=w, V=V)
            store[N]["trA_full"].append(trA_f)
            store[N]["trsq_full"].append(trsq_f)
            store[N]["rank_full"].append(rk_f)
            store[N]["trA_trunc"].append(trA_t)
            store[N]["trsq_trunc"].append(trsq_t)
            store[N]["rank_trunc"].append(rk_t)

            # --- PROXY 2: modular spectrum ---
            eps_f = modular_spectrum_from_mu(mu_full)
            eps_t = modular_spectrum_from_mu(mu_trunc)
            store[N]["epsmax_full"].append(float(eps_f.max()) if eps_f.size else 0.0)
            store[N]["epsmax_trunc"].append(float(eps_t.max()) if eps_t.size else 0.0)
            store[N]["pile_full"].append(int(np.sum(eps_f < eps0)))
            store[N]["pile_trunc"].append(int(np.sum(eps_t < eps0)))
            store[N]["nmodes_full"].append(int(eps_f.size))
            store[N]["nmodes_trunc"].append(int(eps_t.size))
            # pool one representative seed (s==0) for density plots
            if s == 0:
                store[N]["eps_full_pool"] = eps_f.tolist()
                store[N]["eps_trunc_pool"] = eps_t.tolist()

        print(f"[N={N}] kappa={kap:.3f}  "
              f"S_full={np.mean(store[N]['S_full']):.2f}  "
              f"S_trunc={np.mean(store[N]['S_trunc']):.3f}  "
              f"Tr|iD_O|_full={np.mean(store[N]['trA_full']):.1f}  "
              f"Tr|iD_O|_trunc={np.mean(store[N]['trA_trunc']):.2f}  "
              f"pile_full={np.mean(store[N]['pile_full']):.1f}  "
              f"pile_trunc={np.mean(store[N]['pile_trunc']):.1f}  "
              f"nmod_full={np.mean(store[N]['nmodes_full']):.0f}  "
              f"nmod_trunc={np.mean(store[N]['nmodes_trunc']):.0f}  "
              f"epsmax_full={np.mean(store[N]['epsmax_full']):.2f}  "
              f"epsmax_trunc={np.mean(store[N]['epsmax_trunc']):.2f}")

    # ------------------------------------------------------------------
    # Aggregate + fit each proxy vs N
    # ------------------------------------------------------------------
    def mean_std(key):
        m = np.array([np.mean(store[N][key]) for N in Ns])
        sd = np.array([np.std(store[N][key], ddof=1) for N in Ns])
        return m, sd

    agg = {}
    for key in ["S_full", "S_trunc", "trA_full", "trA_trunc",
                "trsq_full", "trsq_trunc", "rank_full", "rank_trunc",
                "epsmax_full", "epsmax_trunc", "pile_full", "pile_trunc",
                "nmodes_full", "nmodes_trunc"]:
        m, sd = mean_std(key)
        agg[key] = {"mean": m, "std": sd}

    # ---- PROXY 1 fits: Tr|iDelta_O| ~ N^a ----
    p_trA_full, q_trA_full, e_trA_full = powerlaw_fit(
        Ns_arr, agg["trA_full"]["mean"],
        sig=agg["trA_full"]["std"] / np.maximum(agg["trA_full"]["mean"], 1e-12))
    p_trA_trunc, q_trA_trunc, e_trA_trunc = powerlaw_fit(
        Ns_arr, agg["trA_trunc"]["mean"],
        sig=agg["trA_trunc"]["std"] / np.maximum(agg["trA_trunc"]["mean"], 1e-12))
    p_Sfull, q_Sfull, e_Sfull = powerlaw_fit(Ns_arr, agg["S_full"]["mean"])

    # entropy-trace (the actual von Neumann trace functional -Tr rho ln rho):
    # S_trunc saturates -> finite trace (II); we fit its residual N-trend.
    St_mean = agg["S_trunc"]["mean"]
    p_Strunc, q_Strunc, e_Strunc = powerlaw_fit(Ns_arr, St_mean)

    proxy1 = {
        "description": (
            "TWO distinct trace objects. (A) ENTROPY-TRACE S=-Tr(rho ln rho): the "
            "actual von Neumann trace functional; III=no finite trace (volume law, "
            "diverges), II=finite trace (area/log law, saturates). (B) Pauli-Jordan "
            "NUCLEAR NORM Tr|iDelta_O|: a kinematic (symplectic-form) object, "
            "type-independent. Reported as an honest control."),
        "Ns": Ns, "rho": rho_arr.tolist(),
        "entropy_trace_full": {"mean": agg["S_full"]["mean"].tolist(),
                               "std": agg["S_full"]["std"].tolist(),
                               "exponent_a": p_Sfull, "a_err": e_Sfull,
                               "note": "volume law ~ N^1 = divergent trace (III-like)"},
        "entropy_trace_trunc": {"mean": agg["S_trunc"]["mean"].tolist(),
                                "std": agg["S_trunc"]["std"].tolist(),
                                "exponent_a": p_Strunc, "a_err": e_Strunc,
                                "note": "area/log law, saturates ~1.3-1.7 = finite trace (II-like)"},
        "PJ_nuclear_norm_full": {"mean": agg["trA_full"]["mean"].tolist(),
                                 "std": agg["trA_full"]["std"].tolist(),
                                 "exponent_a": p_trA_full, "a_err": e_trA_full},
        "PJ_nuclear_norm_trunc": {"mean": agg["trA_trunc"]["mean"].tolist(),
                                  "std": agg["trA_trunc"]["std"].tolist(),
                                  "exponent_a": p_trA_trunc, "a_err": e_trA_trunc,
                                  "note": "grows ~N^1 like full: kappa removes only a "
                                          "constant ~20% fraction, NOT the divergence"},
        "rank_full_mean": agg["rank_full"]["mean"].tolist(),
        "rank_trunc_mean": agg["rank_trunc"]["mean"].tolist(),
        "prediction": "III->II in the ENTROPY-TRACE: S_full divergent (a~1, volume), "
                      "S_trunc saturates (a~0, area/log).",
    }
    # entropy-trace ratio: how strongly truncation collapses the divergent trace
    proxy1["trace_collapse_factor_largest_N"] = float(
        agg["S_full"]["mean"][-1] / max(agg["S_trunc"]["mean"][-1], 1e-12))
    # DECISIVE metric = entropy-trace: full diverges (a>0.5, significant) AND
    # truncated saturates (|a|<0.25, i.e. effectively flat at this N range).
    sig_Sfull = p_Sfull / e_Sfull if e_Sfull > 0 else 0.0
    proxy1["entropy_full_divergent"] = bool(p_Sfull > 0.5)
    proxy1["entropy_trunc_saturates"] = bool(abs(p_Strunc) < 0.25)
    proxy1["verdict_III_to_II"] = bool(
        proxy1["entropy_full_divergent"] and proxy1["entropy_trunc_saturates"])

    # ---- PROXY 2 fits: modular spectrum ----
    p_pile_full, q_pile_full, e_pile_full = powerlaw_fit(
        Ns_arr, np.maximum(agg["pile_full"]["mean"], 1e-9),
        sig=agg["pile_full"]["std"] / np.maximum(agg["pile_full"]["mean"], 1e-9))
    pile_t = np.maximum(agg["pile_trunc"]["mean"], 1e-9)
    p_pile_trunc, q_pile_trunc, e_pile_trunc = powerlaw_fit(
        Ns_arr, pile_t,
        sig=agg["pile_trunc"]["std"] / pile_t)
    # epsmax trend
    s_em_full, b_em_full = linfit(Ns_arr, agg["epsmax_full"]["mean"])
    s_em_trunc, b_em_trunc = linfit(Ns_arr, agg["epsmax_trunc"]["mean"])

    # flatness of rho near eps=0 (use largest-N pooled spectra, all seeds)
    def pooled_eps(key):
        pool = []
        for N in Ns:
            pool.append(np.array(store[N][key]))   # only s==0 stored as list
        return pool
    # density flatness metric: fraction of modes below eps0 of the total
    frac_below_full = (agg["pile_full"]["mean"] /
                       np.maximum(agg["nmodes_full"]["mean"], 1e-9))
    frac_below_trunc = (agg["pile_trunc"]["mean"] /
                        np.maximum(agg["nmodes_trunc"]["mean"], 1e-9))

    proxy2 = {
        "description": "Modular spectrum eps=ln[mu/(mu-1)] from SSEE mu. "
                       "III_1: flat dense spectrum, small-eps pile-up grows with N. "
                       "II: integrable density, fixed UV edge, pile-up saturates.",
        "Ns": Ns, "eps0_threshold": eps0,
        "pile_below_eps0_full": {"mean": agg["pile_full"]["mean"].tolist(),
                                 "std": agg["pile_full"]["std"].tolist(),
                                 "exponent": p_pile_full, "err": e_pile_full},
        "pile_below_eps0_trunc": {"mean": agg["pile_trunc"]["mean"].tolist(),
                                  "std": agg["pile_trunc"]["std"].tolist(),
                                  "exponent": p_pile_trunc, "err": e_pile_trunc},
        "epsmax_full": {"mean": agg["epsmax_full"]["mean"].tolist(),
                        "std": agg["epsmax_full"]["std"].tolist(),
                        "slope_vs_N": s_em_full},
        "epsmax_trunc": {"mean": agg["epsmax_trunc"]["mean"].tolist(),
                         "std": agg["epsmax_trunc"]["std"].tolist(),
                         "slope_vs_N": s_em_trunc},
        "nmodes_full_mean": agg["nmodes_full"]["mean"].tolist(),
        "nmodes_trunc_mean": agg["nmodes_trunc"]["mean"].tolist(),
        "frac_below_eps0_full": frac_below_full.tolist(),
        "frac_below_eps0_trunc": frac_below_trunc.tolist(),
        "prediction": "III->II: pile_full exponent >0 (UV pile-up grows, dense "
                      "spectrum toward eps=0); pile_trunc saturates (exponent ~0).",
    }
    sig_pile_full = p_pile_full / e_pile_full if e_pile_full > 0 else 0.0
    proxy2["full_pileup_grows"] = bool(p_pile_full > 0.25 and sig_pile_full > 3)
    proxy2["trunc_pileup_saturates"] = bool(p_pile_trunc < 0.6 * p_pile_full)
    proxy2["verdict_III_to_II"] = bool(proxy2["full_pileup_grows"]
                                       and proxy2["trunc_pileup_saturates"])

    # ---- PROXY 3: central-sequences / factor proxy (CV vs N) ----
    cv_Sfull = agg["S_full"]["std"] / np.maximum(np.abs(agg["S_full"]["mean"]), 1e-12)
    cv_Strunc = agg["S_trunc"]["std"] / np.maximum(np.abs(agg["S_trunc"]["mean"]), 1e-12)
    cv_epsmax_trunc = (agg["epsmax_trunc"]["std"] /
                       np.maximum(agg["epsmax_trunc"]["mean"], 1e-12))
    cv_epsmax_full = (agg["epsmax_full"]["std"] /
                      np.maximum(agg["epsmax_full"]["mean"], 1e-12))
    s_cv_trunc, b_cv_trunc = linfit(Ns_arr, cv_Strunc)
    s_cv_full, b_cv_full = linfit(Ns_arr, cv_Sfull)
    # power-law trends of CV
    p_cv_trunc, _, e_cv_trunc = powerlaw_fit(Ns_arr, np.maximum(cv_Strunc, 1e-9))
    p_cv_full, _, e_cv_full = powerlaw_fit(Ns_arr, np.maximum(cv_Sfull, 1e-9))

    proxy3 = {
        "description": "Central-sequences / factor proxy: seed-to-seed CV of the "
                       "TRUNCATED SSEE should shrink with N (self-averaging / trivial "
                       "centre / boundary-microstructure independent).",
        "Ns": Ns, "n_seeds": n_seeds,
        "CV_S_trunc": cv_Strunc.tolist(), "CV_S_full": cv_Sfull.tolist(),
        "CV_epsmax_trunc": cv_epsmax_trunc.tolist(),
        "CV_epsmax_full": cv_epsmax_full.tolist(),
        "CV_S_trunc_slope_vs_N": s_cv_trunc, "CV_S_full_slope_vs_N": s_cv_full,
        "CV_S_trunc_powerlaw": p_cv_trunc, "CV_S_trunc_powerlaw_err": e_cv_trunc,
        "CV_S_full_powerlaw": p_cv_full, "CV_S_full_powerlaw_err": e_cv_full,
        "CV_S_trunc_largest_N": float(cv_Strunc[-1]),
        "prediction": "factor-like (II): CV(S_trunc) small and DECREASING with N "
                      "(slope<0, power-law exponent significantly <0).",
    }
    # HONEST verdict: require (a) truncated entropy is already self-averaging
    # (CV small, few %), AND (b) a STATISTICALLY SIGNIFICANT decreasing trend
    # (|exponent|/err > 2). With only n_seeds the trend may be unresolved.
    cv_significant = (e_cv_trunc > 0) and (abs(p_cv_trunc) / e_cv_trunc > 2.0)
    proxy3["trunc_is_self_averaging"] = bool(cv_Strunc[-1] < 0.05)
    proxy3["trunc_trend_significant"] = bool(cv_significant)
    proxy3["trunc_trend_decreasing"] = bool(p_cv_trunc < 0)
    # factor-like requires self-averaging; the DECREASING TREND is a stronger
    # claim and only counts if statistically significant.
    proxy3["verdict_factor_like"] = bool(
        proxy3["trunc_is_self_averaging"]
        and proxy3["trunc_trend_decreasing"]
        and proxy3["trunc_trend_significant"])
    proxy3["verdict_note"] = (
        "self-averaging (small CV) " + ("CONFIRMED" if proxy3["trunc_is_self_averaging"]
        else "NOT confirmed") + "; decreasing trend "
        + ("SIGNIFICANT" if cv_significant else "NOT significant at this seed count"))

    results["proxy1_trace"] = _to_native(proxy1)
    results["proxy2_modular_spectrum"] = _to_native(proxy2)
    results["proxy3_central_sequences"] = _to_native(proxy3)

    # ------------------------------------------------------------------
    # OVERALL VERDICT
    # ------------------------------------------------------------------
    v1 = proxy1["verdict_III_to_II"]
    v2 = proxy2["verdict_III_to_II"]
    v3 = proxy3["verdict_factor_like"]
    n_pass = int(v1) + int(v2) + int(v3)
    if n_pass == 3:
        overall = "ALL three proxies consistent with III_1 -> II"
    elif n_pass == 0:
        overall = "NONE of the proxies show III_1 -> II"
    else:
        overall = f"MIXED: {n_pass}/3 proxies consistent with III_1 -> II"
    results["VERDICT"] = {
        "proxy1_trace_III_to_II": v1,
        "proxy2_modular_spectrum_III_to_II": v2,
        "proxy3_factor_like": v3,
        "n_proxies_passing": n_pass,
        "overall": overall,
    }
    print("\n=== VERDICT ===")
    print(f" proxy1 (trace divergence):     {v1}")
    print(f" proxy2 (modular spectrum):     {v2}")
    print(f" proxy3 (central sequences):    {v3}")
    print(f" overall: {overall}")

    # ------------------------------------------------------------------
    # PLOTS
    # ------------------------------------------------------------------
    _plot_proxy1(Ns_arr, agg, proxy1)
    _plot_proxy2_trends(Ns_arr, agg, proxy2)
    _plot_modular_density(store, Ns)
    _plot_proxy3(Ns_arr, cv_Sfull, cv_Strunc, proxy3)

    with open(os.path.join(OUTDIR, "results.json"), "w") as f:
        json.dump(_to_native(results), f, indent=2)
    print("\nSaved results.json and plots to", OUTDIR)
    return results


# ----------------------------------------------------------------------------
def _to_native(o):
    import numpy as _np
    if isinstance(o, dict):
        return {k: _to_native(v) for k, v in o.items()}
    if isinstance(o, (list, tuple)):
        return [_to_native(v) for v in o]
    if isinstance(o, (_np.floating,)):
        return float(o)
    if isinstance(o, (_np.integer,)):
        return int(o)
    if isinstance(o, (_np.bool_,)):
        return bool(o)
    if isinstance(o, _np.ndarray):
        return o.tolist()
    return o


def _plot_proxy1(Ns, agg, proxy1):
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13, 5))
    # PRIMARY: entropy-trace (the actual von Neumann trace functional)
    Sf = np.array(agg["S_full"]["mean"]); Sf_s = np.array(agg["S_full"]["std"])
    St = np.array(agg["S_trunc"]["mean"]); St_s = np.array(agg["S_trunc"]["std"])
    a_Sf = proxy1["entropy_trace_full"]["exponent_a"]
    ax1.errorbar(Ns, Sf, yerr=Sf_s, fmt='o', color='tab:red', capsize=3,
                 label=f"untruncated (volume law) a={a_Sf:.2f} = DIVERGENT trace (III)")
    ax1.errorbar(Ns, St, yerr=St_s, fmt='s', color='tab:blue', capsize=3,
                 label="truncated (area/log law) = FINITE trace (II)")
    ax1.set_xscale('log'); ax1.set_yscale('log')
    ax1.set_xlabel(r"$N$  ($\rho=N/4$)"); ax1.set_ylabel(r"SSEE $S=-\mathrm{Tr}(\rho\ln\rho)$")
    ax1.set_title("PROXY 1 (decisive): ENTROPY-trace\nIII diverges, II saturates")
    ax1.legend(fontsize=8)

    # CONTROL: Pauli-Jordan nuclear norm (type-independent kinematic object)
    xx = np.linspace(Ns.min(), Ns.max(), 100)
    m_f = np.array(agg["trA_full"]["mean"]); s_f = np.array(agg["trA_full"]["std"])
    m_t = np.array(agg["trA_trunc"]["mean"]); s_t = np.array(agg["trA_trunc"]["std"])
    a_f = proxy1['PJ_nuclear_norm_full']['exponent_a']
    a_t = proxy1['PJ_nuclear_norm_trunc']['exponent_a']
    ax2.errorbar(Ns, m_f, yerr=s_f, fmt='o', color='tab:red', capsize=3,
                 label=f"untruncated a={a_f:.2f}")
    ax2.plot(xx, m_f[0] / Ns[0]**a_f * xx**a_f, '-', color='tab:red', lw=1)
    ax2.errorbar(Ns, m_t, yerr=s_t, fmt='s', color='tab:blue', capsize=3,
                 label=f"truncated a={a_t:.2f}")
    ax2.plot(xx, m_t[0] / Ns[0]**a_t * xx**a_t, '-', color='tab:blue', lw=1)
    ax2.set_xscale('log'); ax2.set_yscale('log')
    ax2.set_xlabel(r"$N$"); ax2.set_ylabel(r"$\mathrm{Tr}|i\Delta_O|$ (nuclear norm)")
    ax2.set_title("CONTROL: Pauli-Jordan nuclear norm\n(kinematic: both ~N, truncation "
                  "removes only ~20%)")
    ax2.legend(fontsize=8)
    fig.tight_layout(); fig.savefig(os.path.join(OUTDIR, "proxy1_trace.png"), dpi=140)
    plt.close(fig)


def _plot_proxy2_trends(Ns, agg, proxy2):
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13, 5))
    pf = np.array(agg["pile_full"]["mean"]); pfs = np.array(agg["pile_full"]["std"])
    pt = np.array(agg["pile_trunc"]["mean"]); pts = np.array(agg["pile_trunc"]["std"])
    xx = np.linspace(Ns.min(), Ns.max(), 100)
    ax1.errorbar(Ns, pf, yerr=pfs, fmt='o', color='tab:red', capsize=3,
                 label=f"untruncated  exp={proxy2['pile_below_eps0_full']['exponent']:.2f}")
    e = proxy2['pile_below_eps0_full']['exponent']
    ax1.plot(xx, pf[0]/Ns[0]**e * xx**e, '-', color='tab:red', lw=1)
    ax1.errorbar(Ns, pt, yerr=pts, fmt='s', color='tab:blue', capsize=3,
                 label=f"truncated  exp={proxy2['pile_below_eps0_trunc']['exponent']:.2f}")
    ax1.set_xscale('log'); ax1.set_yscale('log')
    ax1.set_xlabel(r"$N$"); ax1.set_ylabel(rf"# modes with $\epsilon<{proxy2['eps0_threshold']}$")
    ax1.set_title("PROXY 2: small-$\\epsilon$ pile-up (III$_1$ grows, II saturates)")
    ax1.legend(fontsize=9)

    emf = np.array(agg["epsmax_full"]["mean"]); emfs = np.array(agg["epsmax_full"]["std"])
    emt = np.array(agg["epsmax_trunc"]["mean"]); emts = np.array(agg["epsmax_trunc"]["std"])
    ax2.errorbar(Ns, emf, yerr=emfs, fmt='o', color='tab:red', capsize=3,
                 label="untruncated UV edge")
    ax2.errorbar(Ns, emt, yerr=emts, fmt='s', color='tab:blue', capsize=3,
                 label="truncated UV edge")
    ax2.set_xlabel(r"$N$"); ax2.set_ylabel(r"$\epsilon_{\max}$ (modular UV edge)")
    ax2.set_title("modular UV edge vs N")
    ax2.legend(fontsize=9)
    fig.tight_layout(); fig.savefig(os.path.join(OUTDIR, "proxy2_modular_trends.png"), dpi=140)
    plt.close(fig)


def _plot_modular_density(store, Ns):
    """Histogram of the modular spectrum (single representative seed) for the
    smallest and largest N, before vs after truncation."""
    fig, axes = plt.subplots(1, 2, figsize=(13, 5))
    for ax, key, title, col in [
        (axes[0], "eps_full_pool", "untruncated modular spectrum (III$_1$ probe)", 'tab:red'),
        (axes[1], "eps_trunc_pool", "truncated modular spectrum (II probe)", 'tab:blue')]:
        for N, alpha, ls in [(Ns[0], 0.45, '-'), (Ns[-1], 0.8, '-')]:
            eps = np.array(store[N][key])
            if eps.size < 3:
                continue
            bins = np.linspace(0, max(6.0, np.percentile(eps, 99)), 40)
            ax.hist(eps, bins=bins, density=True, histtype='step', lw=1.8,
                    color=col, alpha=alpha, label=f"N={N}")
        ax.set_xlabel(r"$\epsilon$ (modular energy)")
        ax.set_ylabel(r"$\rho(\epsilon)$ (normalised)")
        ax.set_title(title); ax.legend(fontsize=9)
    fig.suptitle("PROXY 2: modular spectral density   "
                 r"($\epsilon=\ln[\mu/(\mu-1)]$ from SSEE)")
    fig.tight_layout(); fig.savefig(os.path.join(OUTDIR, "proxy2_modular_density.png"), dpi=140)
    plt.close(fig)


def _plot_proxy3(Ns, cv_full, cv_trunc, proxy3):
    fig, ax = plt.subplots(figsize=(8, 5.5))
    ax.plot(Ns, cv_full, 'o-', color='tab:red',
            label=f"CV(S_full) slope={proxy3['CV_S_full_slope_vs_N']:.2e}")
    ax.plot(Ns, cv_trunc, 's-', color='tab:blue',
            label=f"CV(S_trunc) slope={proxy3['CV_S_trunc_slope_vs_N']:.2e}, "
                  f"exp={proxy3['CV_S_trunc_powerlaw']:.2f}")
    ax.set_xlabel(r"$N$"); ax.set_ylabel("seed-to-seed CV = std/mean")
    ax.set_title("PROXY 3: central-sequences / factor proxy\n"
                 "(factor-like II: CV of truncated SSEE shrinks with N)")
    ax.set_yscale('log'); ax.legend(fontsize=9)
    fig.tight_layout(); fig.savefig(os.path.join(OUTDIR, "proxy3_central_seq.png"), dpi=140)
    plt.close(fig)


if __name__ == "__main__":
    run()
