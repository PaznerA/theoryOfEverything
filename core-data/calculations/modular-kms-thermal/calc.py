#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
H6g-1 : MODULAR KMS / THERMAL-TIME content of the SJ modular flow (2D Rindler slab)
====================================================================================
Does the SJ modular structure / modular Dirac D_K reproduce the THERMAL
(KMS / Unruh) content the continuum Bisognano-Wichmann (BW) theorem predicts --
rather than the spatial metric (the axis F-033 found FAILED)?

THE PROGRAM QUESTION (H6g-1, BRAINSTORM-06)
-------------------------------------------
F-033 (VYPOCET-29) found the surrogate modular Dirac D_K = sgn(K) sqrt(|K|)
reproduces the BW BOOST structure (linear diagonal K(x,x) vs distance-to-cut,
R^2 ~ 0.96, robust) but its Connes distance does NOT track causal distance
(metric axis FAILS). H6g-1 tests the OTHER axis -- the thermal one F-033 flagged
solid: on the 2D Rindler slab (cut O = {x > 0}) the modular flow sigma_t =
e^{iKt} is the boost, and the SJ state should be KMS (thermal) at the Unruh
temperature w.r.t. the boost generator.

OBSERVABLES (BRAINSTORM-06 Test A design), with a HONEST tautology/physics split
-------------------------------------------------------------------------------
The SJ state is, by Tomita-Takesaki/Casini-Huerta construction, a KMS (Gibbs)
state w.r.t. its OWN modular Hamiltonian K at beta = 1 in modular-energy units.
So two of the three observables are, at beta = 1, TAUTOLOGIES of the construction
-- they are CONSISTENCY checks, not geometric evidence. We compute them as such
and isolate the genuinely geometric (BW/Unruh) content:

(a) THERMAL OCCUPATION  n(eps) = 1/(e^{beta eps} - 1).  Per modular mode the SSEE
    generalised eigenvalue mu gives modular energy eps_k = ln[mu_k/(mu_k-1)] and
    occupation n_k = mu_k - 1, so n_k/(n_k+1) = e^{-eps_k} EXACTLY => beta_occ = 1
    to machine precision. TAUTOLOGY (consistency check). [The original kernel
    carrier sorts eps and nu INDEPENDENTLY -- they must be RE-PAIRED through the
    common mu, else the fit is spuriously anti-correlated.]

(b) KMS TWO-POINT.  The modular-evolved two-point G(t) = <A sigma_t(B)> with
    sigma_t = e^{iKt} obeys the KMS condition G(t) = G(-t - i*beta) iff the state
    is thermal at beta. We build the one-particle modular correlator in the
    generalised modular basis, G(t) = sum_k [(n_k+1) e^{-i eps_k t} + n_k
    e^{+i eps_k t}], and SCAN the imaginary-time period beta minimising the KMS
    residual ||G(t) - G(-t - i*beta)||. A clean single minimum at beta = 1 (to
    machine precision) is the analyticity/periodicity verification -- the modular
    flow IS a genuine single-beta KMS flow. (beta = 1 in eps-time; the Unruh 2*pi
    is the conversion to boost-rapidity time, see (a').)

(a') BW BOOST GEOMETRY -> Unruh (the only NON-tautological, geometric content).
    BW: the half-space modular Hamiltonian is K = 2*pi * K_boost,
    K_boost = integral x T_00 dx, so the modular energy density grows LINEARLY in
    the boost coordinate (distance to the cut). We measure the boost-diagonal
    slope d|K(x,x)|/d|x| and R^2 (the F-033 linear diagonal) and its
    rho-INVARIANCE. A rho-invariant, high-R^2 positive slope = the geometric boost
    generator is present. The ABSOLUTE Unruh 2*pi requires the geometric boost
    generator's rapidity normalisation, which the SURROGATE kernel (modular-energy
    units eps = ln[mu/(mu-1)] + site-basis lift) does NOT fix; we report the
    slope-to-2*pi ratio explicitly and do NOT claim 2*pi if it is not recovered.

(c) CONTROL.  A NON-Rindler cut (finite spatial INTERVAL 0<x<x0, BW does NOT
    apply -- the interval modular Hamiltonian peaks at BOTH ends, not linear in
    distance-to-one-end) and a SHUFFLED-K control (Haar-orthogonal conjugation:
    spectrum preserved, site geometry destroyed). On both, the boost-linearity
    must FAIL while the occupation tautology (beta=1) still holds -- proving the
    thermal-OCCUPATION fit is a spectral tautology and the geometric content lives
    in the boost diagonal (the eigenvectors).

DISCRIMINATOR (pre-registered)
------------------------------
KMS holds at a single beta (machine precision) AND the boost diagonal is linear,
rho-invariant, high-R^2 on the Rindler slab, FAILING on the interval + shuffle
controls => the modular flow DOES carry the thermal-time (Connes-Rovelli) +
boost (BW) structure => POSITIVE thermal-axis data edge causal-sets<->NCG,
complementing the F-033 metric no-match. If in addition the boost slope recovers
the absolute Unruh 2*pi, the positive is QUANTITATIVE; if only the qualitative
single-beta-KMS + rho-invariant boost geometry survives (2*pi not normalised by
the surrogate), the positive is PARTIAL (qualitative thermal content, no absolute
Unruh temperature). If KMS fails a single beta or the control also passes =>
honest negative.

CAVEAT (honest): beta_occ = 1 and beta_KMS = 1 in eps-time are TAUTOLOGIES of the
SJ/Casini-Huerta construction, NOT geometric evidence. Only the rho-invariant
boost-linear diagonal (failing on controls) carries BW geometry. The surrogate
does NOT fix the absolute 2*pi normalisation. D_K is a SURROGATE Dirac (inherits
F-033 caveat). beta = 2*pi is the continuum value; discrete corrections
O(1/sqrt N).

CONVENTIONS (verified literature / repo-present IDs only)
---------------------------------------------------------
SJ state + modular kernel: iDelta = i(G_R - G_R^T); 2D massless G_R = (1/2) C
  (Sorkin-Yazdi 1611.10281). W = positive spectral part of iDelta. One-particle
  modular Hamiltonian K(x,y) from W_O v = mu iDelta_O v, eps = ln[mu/(mu-1)]
  (Casini-Huerta 0905.2562). Untruncated (kappa=None) = the genuine SJ modular
  flow whose geometricity BW (1712.04227, context 2008.07697) predicts. Modular
  flow as thermal time: Connes-Rovelli gr-qc/9406019 ("Von Neumann Algebra
  Automorphisms and Time-Thermodynamics Relation"). Bisognano-Wichmann boost /
  Unruh temperature 1/2pi: references.bib Bisognano-Wichmann + Unruh entries.

All paths __file__-relative (portability guard). results.json: fixed schema with
'status' + atomic write (tmp + os.replace), progressive per-seed flush.
"""

import json
import os
import sys
import time

for _v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS",
           "VECLIB_MAXIMUM_THREADS", "NUMEXPR_NUM_THREADS"):
    os.environ.setdefault(_v, "4")

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# --- __file__-relative paths (portability) ---------------------------------
OUTDIR = os.path.dirname(os.path.abspath(__file__))
PLOTDIR = os.path.join(OUTDIR, "plots")
os.makedirs(PLOTDIR, exist_ok=True)
_REPO_ROOT = os.path.abspath(os.path.join(OUTDIR, os.pardir, os.pardir, os.pardir))
_LIB = os.path.join(_REPO_ROOT, "lib")
if _LIB not in sys.path:
    sys.path.insert(0, _LIB)

from toe.causet import sprinkle_slab2d, causal_matrix, green_retarded_2d, pauli_jordan
from toe.sj import sj_state
from toe.entropy import modular_kernel

# New lib primitives (added to lib/toe/spectraltriple.py); fall back to local copy
# if running against a pre-update lib build.
try:
    from toe.spectraltriple import kms_temperature, KMSFit
    _HAVE_LIB_KMS = True
except Exception:  # pragma: no cover
    _HAVE_LIB_KMS = False


# ===========================================================================
# CONFIG
# ===========================================================================
T_EXTENT = 0.30
X_EXTENT = 1.0
INTERVAL_X0 = 0.5 * X_EXTENT          # interval cut {0 < x < x0}: BW invalid
TWO_PI = 2.0 * np.pi
WALL_CAP_S = 25 * 60                   # 25 min total wall-clock cap


# ===========================================================================
# FIT HELPERS
# ===========================================================================

def r2(y, yhat):
    y = np.asarray(y, float)
    ss = np.sum((y - y.mean()) ** 2)
    return 1.0 - np.sum((y - yhat) ** 2) / ss if ss > 0 else 0.0


def linfit(x, y, mask=None):
    x = np.asarray(x, float); y = np.asarray(y, float)
    m = np.isfinite(x) & np.isfinite(y)
    if mask is not None:
        m &= mask
    if m.sum() < 2:
        return None, None, None
    A = np.vstack([x[m], np.ones(m.sum())]).T
    coef, *_ = np.linalg.lstsq(A, y[m], rcond=None)
    return float(coef[0]), float(coef[1]), float(r2(y[m], A @ coef))


def _m(lst):
    lst = [x for x in lst if x is not None and np.isfinite(x)]
    return float(np.mean(lst)) if lst else float("nan")


def _sd(lst):
    lst = [x for x in lst if x is not None and np.isfinite(x)]
    return float(np.std(lst, ddof=1)) if len(lst) > 1 else float("nan")


def _to_native(o):
    if isinstance(o, dict):
        return {k: _to_native(v) for k, v in o.items()}
    if isinstance(o, (list, tuple)):
        return [_to_native(v) for v in o]
    if isinstance(o, (np.floating,)):
        return float(o)
    if isinstance(o, (np.integer,)):
        return int(o)
    if isinstance(o, (np.bool_,)):
        return bool(o)
    if isinstance(o, np.ndarray):
        return o.tolist()
    return o


def write_results_atomic(results, path):
    tmp = path + ".tmp"
    with open(tmp, "w") as fh:
        json.dump(_to_native(results), fh, indent=2)
    os.replace(tmp, path)


# ===========================================================================
# PER-MODE PAIRING:  recover (eps_k, occ_k) from the common mu_k
# ===========================================================================

def paired_modes(mk, tol=1e-9):
    """(eps, occ) paired per modular mode through the common mu = nu + 1/2.

    The ModularKernel carrier sorts ``eps`` and ``nu`` INDEPENDENTLY ascending;
    since eps = ln[mu/(mu-1)] DECREASES with mu, pairing eps[k] with nu[k] is
    anti-correlated and wrong. Here we reconstruct mu = nu + 1/2 (>1), then
    eps_k = ln[mu_k/(mu_k-1)] and occ_k = mu_k - 1 are PAIRED by construction:
    n_k/(n_k+1) = e^{-eps_k} exactly (KMS at beta=1 in eps-units, Casini-Huerta).
    """
    mu = np.asarray(mk.nu, float) + 0.5
    mu = mu[mu > 1.0 + tol]
    eps = np.log(mu / (mu - 1.0))
    occ = mu - 1.0
    return eps, occ


# ===========================================================================
# (a) THERMAL OCCUPATION fit  n = 1/(e^{beta eps} - 1)   [tautology -> beta=1]
# ===========================================================================

def fit_bose_beta(eps, occ):
    """Single inverse-temperature beta of n = 1/(e^{beta eps} - 1) via the
    detailed-balance linearisation ln(1 + 1/n) = beta*eps (zero-intercept slope).
    Returns (beta0, r2, free_slope). For PAIRED SJ modes beta0 = 1 exactly."""
    eps = np.asarray(eps, float); occ = np.asarray(occ, float)
    m = np.isfinite(eps) & np.isfinite(occ) & (eps > 0) & (occ > 0)
    eps = eps[m]; occ = occ[m]
    if eps.size < 3:
        return float("nan"), float("nan"), float("nan")
    y = np.log1p(1.0 / occ)                         # = beta*eps for a Bose law
    denom = float(np.dot(eps, eps))
    beta0 = float(np.dot(eps, y) / denom) if denom > 0 else float("nan")
    r2_0 = float(r2(y, beta0 * eps))
    sl, _, _ = linfit(eps, y)
    return beta0, r2_0, (sl if sl is not None else float("nan"))


# ===========================================================================
# (b) KMS TWO-POINT  G(t) and imaginary-time period scan  [tautology -> beta=1]
# ===========================================================================

def kms_period_scan(eps, occ, *, n_t=9, t_span=2.0, betas=None):
    """Modular two-point G(t) in the generalised modular basis and the
    imaginary-time period beta minimising the KMS residual.

    One-particle modular correlator (real field):
        G(t) = sum_k [ (n_k + 1) e^{-i eps_k t} + n_k e^{+i eps_k t} ].
    KMS at beta: G(t) = G(-t - i*beta). The analytic continuation reweights the
    two branches by e^{-/+ beta eps_k}; the residual
        R(beta) = || G(t) - G_cont(-t - i*beta) || / || G(t) ||
    has a single sharp minimum at the KMS inverse-temperature. For the SJ modular
    flow this is beta = 1 in eps-time (machine precision). Returns
    (beta_kms, resid_at_beta1, resid_min, ts, G_re, G_im).
    """
    eps = np.asarray(eps, float); occ = np.asarray(occ, float)
    m = np.isfinite(eps) & np.isfinite(occ) & (eps > 0) & (occ >= 0)
    eps = eps[m]; occ = occ[m]
    if eps.size < 2:
        return float("nan"), float("nan"), float("nan"), [], [], []
    ts = np.linspace(-t_span, t_span, n_t)

    def G(t):
        return np.sum((occ + 1) * np.exp(-1j * eps * t)
                      + occ * np.exp(+1j * eps * t))

    def resid(beta):
        num = 0.0; den = 0.0
        for t in ts:
            lhs = G(t)
            # G(-t - i beta): e^{-i eps(-t-i beta)} = e^{+i eps t} e^{-eps beta};
            #                 e^{+i eps(-t-i beta)} = e^{-i eps t} e^{+eps beta}
            rhs = np.sum((occ + 1) * np.exp(+1j * eps * t) * np.exp(-eps * beta)
                         + occ * np.exp(-1j * eps * t) * np.exp(+eps * beta))
            num += abs(lhs - rhs) ** 2
            den += abs(lhs) ** 2
        return float(np.sqrt(num / den)) if den > 0 else float("inf")

    if betas is None:
        betas = np.linspace(0.2, 2.0, 181)          # fine grid around beta=1
    rr = np.array([resid(b) for b in betas])
    beta_kms = float(betas[int(np.argmin(rr))])
    resid_min = float(np.min(rr))
    resid_b1 = resid(1.0)
    G_curve = np.array([G(t) for t in ts])
    return (beta_kms, resid_b1, resid_min, ts.tolist(),
            np.real(G_curve).tolist(), np.imag(G_curve).tolist())


# ===========================================================================
# (a') BW BOOST DIAGONAL -> Unruh  [the geometric, NON-tautological observable]
# ===========================================================================

def boost_diagonal(K, x, *, surface=0.0, n_bins=15):
    """Boost-diagonal slope d|K(x,x)|/d(distance-to-cut), R^2, and the
    slope-to-2*pi ratio (energy-density-normalised).

    BW: K(x,x) ~ 2*pi * x * rho_E(x). A linear, high-R^2, positive slope =
    geometric boost generator present (the F-033 linear diagonal). The absolute
    2*pi requires the boost-generator rapidity normalisation, which the surrogate
    does NOT fix; we report:
      * boost_slope, boost_r2 (raw, dimensionful, rho-invariant constant);
      * unruh_ratio = boost_slope / e0 with e0 the through-origin energy density
        slope (diag ~ e0*x); BW would give unruh_ratio = 2*pi IF the surrogate
        were 2*pi-normalised -- reported explicitly, NOT claimed.
    """
    K = np.asarray(K)
    diag = np.abs(np.real(np.diag(K)))
    dist = np.abs(np.asarray(x, float) - surface)
    if dist.size < n_bins:
        return {"boost_slope": float("nan"), "boost_r2": float("nan"),
                "unruh_ratio": float("nan"),
                "boost_centers": [], "boost_prof": []}
    bins = np.linspace(dist.min(), np.percentile(dist, 98), n_bins + 1)
    centers = 0.5 * (bins[:-1] + bins[1:])
    idx = np.digitize(dist, bins)
    prof = np.full(n_bins, np.nan); cnt = np.zeros(n_bins, int)
    for b in range(1, n_bins + 1):
        msk = idx == b
        cnt[b - 1] = msk.sum()
        if msk.sum() > 0:
            prof[b - 1] = np.mean(diag[msk])
    bmask = cnt >= 8
    sl, _, rr = linfit(centers, prof, mask=bmask)
    g = bmask & np.isfinite(prof)
    e0 = (float(np.dot(centers[g], prof[g]) / np.dot(centers[g], centers[g]))
          if g.sum() >= 2 and np.dot(centers[g], centers[g]) > 0 else float("nan"))
    unruh_ratio = (float(sl / e0) if (sl is not None and np.isfinite(e0)
                   and e0 != 0) else float("nan"))
    return {"boost_slope": sl, "boost_r2": rr, "unruh_ratio": unruh_ratio,
            "boost_centers": centers.tolist(), "boost_prof": prof.tolist(),
            "boost_cnt": cnt.tolist()}


def shuffle_kernel(K, seed):
    """Haar-orthogonal conjugation K' = Q K Q^T: spectrum preserved, site
    geometry destroyed (the (c) shuffle control)."""
    K = np.real(np.asarray(K))
    n = K.shape[0]
    rng = np.random.default_rng(seed)
    Q, _ = np.linalg.qr(rng.standard_normal((n, n)))
    return Q @ K @ Q.T


# ===========================================================================
# ONE SEED
# ===========================================================================

def run_seed(N, seed):
    rng = np.random.default_rng(seed)
    coords = sprinkle_slab2d(N, rng, t_extent=T_EXTENT, x_extent=X_EXTENT)
    C = causal_matrix(coords)
    iDelta = pauli_jordan(green_retarded_2d(C))
    W = sj_state(iDelta).W
    out = {"N": int(N), "seed": int(seed)}

    # ---- RINDLER half-line cut O = {x > 0} (BW boost) ---------------------
    sub_R = np.where(coords[:, 1] > 0.0)[0]
    if sub_R.size < 8:
        return None
    mk_R = modular_kernel(W, iDelta, sub_R, kappa=None)
    if mk_R is None:
        return None
    eps_R, occ_R = paired_modes(mk_R)
    beta_occ, occ_r2, occ_free = fit_bose_beta(eps_R, occ_R)
    if _HAVE_LIB_KMS:
        kf = kms_temperature(eps_R, occ_R)
        beta_kms, kms_b1, kms_min = kf.beta, kf.resid_beta1, kf.resid_min
        ts, gre, gim = kf.ts, kf.g_re, kf.g_im
    else:
        beta_kms, kms_b1, kms_min, ts, gre, gim = kms_period_scan(eps_R, occ_R)
    bd_R = boost_diagonal(np.real(mk_R.K), coords[sub_R][:, 1])

    out["rindler"] = {
        "n_sub": int(sub_R.size), "n_modes": int(mk_R.n_modes), "S": float(mk_R.S),
        "beta_occ": beta_occ, "occ_r2": occ_r2, "occ_freeslope": occ_free,
        "beta_kms": beta_kms, "kms_resid_beta1": kms_b1, "kms_resid_min": kms_min,
        "boost_slope": bd_R["boost_slope"], "boost_r2": bd_R["boost_r2"],
        "unruh_ratio": bd_R["unruh_ratio"],
    }

    # ---- CONTROL 1: INTERVAL {0 < x < x0} (BW does NOT apply) --------------
    sub_I = np.where((coords[:, 1] > 0.0) & (coords[:, 1] < INTERVAL_X0))[0]
    interval = None
    if sub_I.size >= 8:
        mk_I = modular_kernel(W, iDelta, sub_I, kappa=None)
        if mk_I is not None:
            eps_I, occ_I = paired_modes(mk_I)
            b_occ_I, r2_occ_I, _ = fit_bose_beta(eps_I, occ_I)
            bd_I = boost_diagonal(np.real(mk_I.K), coords[sub_I][:, 1])
            interval = {
                "n_sub": int(sub_I.size), "n_modes": int(mk_I.n_modes),
                "beta_occ": b_occ_I, "occ_r2": r2_occ_I,
                "boost_slope": bd_I["boost_slope"], "boost_r2": bd_I["boost_r2"],
                "unruh_ratio": bd_I["unruh_ratio"],
            }
    out["interval_control"] = interval

    # ---- CONTROL 2: SHUFFLE (spectrum preserved, geometry destroyed) -------
    K_sh = shuffle_kernel(mk_R.K, seed + 7)
    bd_sh = boost_diagonal(K_sh, coords[sub_R][:, 1])
    # occupation on shuffled kernel: same spectrum => still thermal beta=1
    lam_sh = np.linalg.eigvalsh(K_sh)
    eps_sh = np.abs(lam_sh[np.abs(lam_sh) > 1e-9])
    occ_sh = 1.0 / np.clip(np.exp(eps_sh) - 1.0, 1e-12, None)
    b_occ_sh, r2_occ_sh, _ = fit_bose_beta(eps_sh, occ_sh)
    out["shuffle_control"] = {
        "beta_occ": b_occ_sh, "occ_r2": r2_occ_sh,
        "boost_slope": bd_sh["boost_slope"], "boost_r2": bd_sh["boost_r2"],
        "unruh_ratio": bd_sh["unruh_ratio"],
    }

    payload = {
        "eps_R": eps_R, "occ_R": occ_R, "bd_R": bd_R,
        "ts": ts, "G_re": gre, "G_im": gim, "beta_kms": beta_kms,
        "kms_resid_beta1": kms_b1,
    }
    return out, payload


# ===========================================================================
# PLOTS
# ===========================================================================

def plot_thermal_occupation(payload, agg, path):
    eps = np.asarray(payload["eps_R"]); occ = np.asarray(payload["occ_R"])
    fig, axs = plt.subplots(1, 2, figsize=(11.8, 4.5))
    ax = axs[0]
    m = (eps > 0) & (occ > 0)
    ax.semilogy(eps[m], occ[m], "o", ms=4, alpha=0.7, label="SJ occupation n=mu-1")
    eg = np.linspace(max(eps[m].min(), 1e-3), eps[m].max(), 200)
    ax.semilogy(eg, 1.0 / (np.exp(eg) - 1.0), "r-", lw=1.5,
                label=r"Bose $1/(e^{\epsilon}-1)$  ($\beta_\epsilon=1$)")
    ax.set_xlabel(r"modular energy $\epsilon=\ln[\mu/(\mu-1)]$")
    ax.set_ylabel("occupation n")
    bo = agg["rindler"]["beta_occ_mean"]
    ax.set_title(f"(a) Thermal occupation  ($\\beta_{{occ}}$={bo:.4f}, tautology)")
    ax.legend(fontsize=8); ax.grid(alpha=0.3, which="both")
    ax2 = axs[1]
    bc = np.asarray(payload["bd_R"]["boost_centers"])
    bp = np.asarray(payload["bd_R"]["boost_prof"])
    good = np.isfinite(bp)
    ax2.plot(bc[good], bp[good], "s", ms=5, label="|K(x,x)| boost diagonal")
    sl = agg["rindler"]["boost_slope_mean"]
    if np.isfinite(sl) and good.sum() >= 2:
        xx = np.linspace(bc[good].min(), bc[good].max(), 50)
        b0 = np.nanmean(bp[good]) - sl * np.nanmean(bc[good])
        ax2.plot(xx, sl * xx + b0, "r-", lw=1.3,
                 label=f"BW linear, slope={sl:.1f}, R²={agg['rindler']['boost_r2_mean']:.3f}")
    ax2.set_xlabel("distance to cut |x|")
    ax2.set_ylabel("modular energy density |K(x,x)|")
    ax2.set_title("(a') BW boost diagonal (rho-invariant geometry)")
    ax2.legend(fontsize=8); ax2.grid(alpha=0.3)
    fig.tight_layout()
    fig.savefig(path, dpi=115)
    plt.close(fig)


def plot_kms(payload, agg, path):
    fig, axs = plt.subplots(1, 2, figsize=(11.8, 4.5))
    ax = axs[0]
    ts = np.asarray(payload["ts"])
    ax.plot(ts, payload["G_re"], "-o", ms=3, label="Re G(t)")
    ax.plot(ts, payload["G_im"], "--s", ms=3, label="Im G(t)")
    ax.axvline(0, color="k", lw=0.6, alpha=0.4)
    ax.set_xlabel("modular time t")
    ax.set_ylabel(r"$G(t)=\langle A\,\sigma_t(B)\rangle$")
    ax.set_title("(b) Modular two-point G(t)")
    ax.legend(fontsize=8); ax.grid(alpha=0.3)
    ax2 = axs[1]
    eps = np.asarray(payload["eps_R"]); occ = np.asarray(payload["occ_R"])
    m = (eps > 0) & (occ > 0)
    ax2.semilogy(eps[m], occ[m] / (occ[m] + 1.0), "o", ms=4, alpha=0.6,
                 label=r"detailed balance $n/(n+1)$")
    eg = np.linspace(eps[m].min(), eps[m].max(), 100)
    bk = agg["rindler"]["beta_kms_mean"]
    ax2.semilogy(eg, np.exp(-bk * eg), "r-", lw=1.3,
                 label=fr"$e^{{-\beta_{{KMS}}\epsilon}}$, $\beta_{{KMS}}$={bk:.4f}")
    ax2.set_xlabel(r"modular energy $\epsilon$")
    ax2.set_ylabel(r"$n/(n+1)$")
    ax2.set_title(f"(b) KMS detailed balance  (resid$_{{\\beta=1}}$="
                  f"{agg['rindler']['kms_resid_beta1_mean']:.1e})")
    ax2.legend(fontsize=8); ax2.grid(alpha=0.3, which="both")
    fig.tight_layout()
    fig.savefig(path, dpi=115)
    plt.close(fig)


# ===========================================================================
# MAIN
# ===========================================================================

def main(argv=None):
    import argparse
    ap = argparse.ArgumentParser(
        description="H6g-1 modular KMS / thermal-time test (2D Rindler slab).",
        epilog="smoke: python3 calc.py --smoke  (N=400, 2 seeds, single rho)")
    ap.add_argument("--smoke", action="store_true",
                    help="tiny run for CI/dev (N=400, 2 seeds, single rho).")
    ap.add_argument("--Ns", type=int, nargs="+", default=None,
                    help="rho sweep as N values (default 300 600 1200).")
    ap.add_argument("--seeds", type=int, default=5)
    args = ap.parse_args(argv)

    t_start = time.time()
    if args.smoke:
        Ns = [400]; n_seeds = 2
    else:
        Ns = args.Ns if args.Ns else [300, 600, 1200]
        n_seeds = args.seeds
    Ns = [min(int(N), 1500) for N in Ns]      # dense eigh cap (H6g-1 N<=1500)

    per_seed = []
    payload_rep = None
    rep_n_sub = -1
    skipped = []
    for N in Ns:
        for s in range(n_seeds):
            if (time.time() - t_start) > WALL_CAP_S:
                skipped.append({"N": int(N), "seed": int(s), "reason": "wall cap"})
                continue
            res = run_seed(N, seed=1000 + 17 * s + N)
            if res is None:
                continue
            out, payload = res
            per_seed.append(out)
            if out["rindler"]["n_sub"] > rep_n_sub:
                rep_n_sub = out["rindler"]["n_sub"]
                payload_rep = payload
            _flush_partial(per_seed, Ns, n_seeds, t_start, "running")

    # ---- aggregate --------------------------------------------------------
    def agg_block(key, sub):
        vals = [d[sub].get(key) for d in per_seed if d.get(sub)]
        return _m(vals), _sd(vals)

    aggregate = {"rindler": {}, "interval_control": {}, "shuffle_control": {}}
    rind_keys = ["beta_occ", "occ_r2", "beta_kms", "kms_resid_beta1",
                 "kms_resid_min", "boost_slope", "boost_r2", "unruh_ratio",
                 "n_sub", "n_modes", "S"]
    for k in rind_keys:
        mu, sd = agg_block(k, "rindler")
        aggregate["rindler"][k + "_mean"] = mu
        aggregate["rindler"][k + "_sd"] = sd
    for blk in ("interval_control", "shuffle_control"):
        for k in ["beta_occ", "occ_r2", "boost_slope", "boost_r2", "unruh_ratio"]:
            mu, sd = agg_block(k, blk)
            aggregate[blk][k + "_mean"] = mu
            aggregate[blk][k + "_sd"] = sd

    # per-rho (rho-invariance of boost slope + beta_kms)
    per_rho = {}
    for N in sorted(set(Ns)):
        sub = [d for d in per_seed if d["N"] == N]
        if sub:
            per_rho[str(N)] = {
                "boost_slope_mean": _m([d["rindler"]["boost_slope"] for d in sub]),
                "boost_r2_mean": _m([d["rindler"]["boost_r2"] for d in sub]),
                "beta_kms_mean": _m([d["rindler"]["beta_kms"] for d in sub]),
                "beta_occ_mean": _m([d["rindler"]["beta_occ"] for d in sub]),
                "unruh_ratio_mean": _m([d["rindler"]["unruh_ratio"] for d in sub]),
                "n_seeds": len(sub),
            }

    # ===================================================================
    # VERDICT (pre-registered)
    # ===================================================================
    R = aggregate["rindler"]; I = aggregate["interval_control"]
    SH = aggregate["shuffle_control"]
    v = {}
    # (a) occupation tautology (consistency)
    v["occupation_thermal_beta1"] = bool(np.isfinite(R["beta_occ_mean"])
        and abs(R["beta_occ_mean"] - 1.0) < 1e-3 and R["occ_r2_mean"] > 0.999)
    # (b) KMS single beta at machine precision => genuine thermal flow
    v["kms_single_beta1"] = bool(np.isfinite(R["beta_kms_mean"])
        and abs(R["beta_kms_mean"] - 1.0) < 0.02 and R["kms_resid_beta1_mean"] < 1e-6)
    # (a') boost geometry present (F-033 linear diagonal), rho-invariant
    v["boost_geometry"] = bool(np.isfinite(R["boost_r2_mean"])
        and R["boost_r2_mean"] > 0.9 and (R["boost_slope_mean"] or 0) > 0)
    slopes = [per_rho[k]["boost_slope_mean"] for k in per_rho
              if np.isfinite(per_rho[k]["boost_slope_mean"])]
    cv = (float(np.std(slopes) / np.abs(np.mean(slopes)))
          if len(slopes) >= 2 and np.mean(slopes) != 0 else float("nan"))
    v["boost_slope_cv"] = cv
    v["boost_rho_invariant"] = bool(np.isfinite(cv) and cv < 0.10)
    # absolute Unruh 2*pi (only if the surrogate happens to be 2pi-normalised)
    v["unruh_2pi_recovered"] = bool(np.isfinite(R["unruh_ratio_mean"])
        and abs(R["unruh_ratio_mean"] - TWO_PI) / TWO_PI < 0.20)
    # (c) controls: boost geometry FAILS
    v["interval_boost_fails"] = bool(I.get("boost_r2_mean") is None
        or not np.isfinite(I.get("boost_r2_mean", float("nan")))
        or I["boost_r2_mean"] < 0.5)
    v["shuffle_boost_fails"] = bool(not np.isfinite(SH["boost_r2_mean"])
        or SH["boost_r2_mean"] < 0.5)
    v["shuffle_occupation_still_thermal"] = bool(np.isfinite(SH["beta_occ_mean"])
        and abs(SH["beta_occ_mean"] - 1.0) < 0.05)

    control_clean = v["interval_boost_fails"] and v["shuffle_boost_fails"]
    thermal_qualitative = (v["kms_single_beta1"] and v["boost_geometry"]
                           and v["boost_rho_invariant"] and control_clean)
    if thermal_qualitative and v["unruh_2pi_recovered"]:
        correspondence = "matches"          # quantitative Unruh 2*pi
    elif thermal_qualitative:
        correspondence = "partial"          # qualitative thermal/boost, no abs 2pi
    else:
        correspondence = "no-match"
    v["correspondence"] = correspondence
    v["thermal_qualitative_positive"] = bool(thermal_qualitative)
    v["control_clean"] = bool(control_clean)

    elapsed = time.time() - t_start
    results = {
        "schema": "modular-kms-thermal/v1",
        "status": "complete",
        "calc": "H6g-1 modular KMS / thermal-time content of SJ modular flow (2D Rindler slab)",
        "config": {
            "Ns": Ns, "n_seeds": n_seeds, "T_extent": T_EXTENT,
            "X_extent": X_EXTENT, "rindler_cut": "x>0 (half-line)",
            "interval_cut": f"0<x<{INTERVAL_X0} (BW does not apply)",
            "shuffle": "Haar-orthogonal conjugation of K (spectrum preserved)",
            "kappa": None, "two_pi": TWO_PI, "wall_cap_s": WALL_CAP_S,
            "lib_kms_primitive": bool(_HAVE_LIB_KMS),
        },
        "references_verified": [
            "gr-qc/9406019", "1712.04227", "1611.10281", "0905.2562",
            "2008.07697", "1305.2588",
        ],
        "per_seed": per_seed,
        "per_rho": per_rho,
        "aggregate": aggregate,
        "verdict": v,
        "skipped": skipped,
        "caveat": ("beta_occ=1 and beta_KMS=1 in eps-time are TAUTOLOGIES of the "
                   "SJ/Casini-Huerta construction (KMS at beta=1 by Tomita-"
                   "Takesaki), NOT geometric evidence. Only the rho-invariant "
                   "boost-linear diagonal (failing on interval+shuffle controls) "
                   "carries BW geometry. The SURROGATE kernel does NOT fix the "
                   "absolute Unruh 2*pi normalisation (unruh_ratio reported, not "
                   "claimed). D_K inherits the F-033 surrogate caveat; beta=2*pi "
                   "is the continuum value, discrete corrections O(1/sqrt N)."),
        "elapsed_s": float(elapsed),
    }
    write_results_atomic(results, os.path.join(OUTDIR, "results.json"))

    if payload_rep is not None:
        plot_thermal_occupation(payload_rep, aggregate,
                                os.path.join(PLOTDIR, "thermal_occupation_fit.png"))
        plot_kms(payload_rep, aggregate,
                 os.path.join(PLOTDIR, "kms_twopoint.png"))

    print(f"[done] correspondence={correspondence}  "
          f"beta_occ={R['beta_occ_mean']:.5f}  beta_kms={R['beta_kms_mean']:.5f}  "
          f"kms_resid_b1={R['kms_resid_beta1_mean']:.2e}  "
          f"boost_slope={R['boost_slope_mean']:.2f} (cv={cv:.3f}, R2={R['boost_r2_mean']:.3f})  "
          f"unruh_ratio={R['unruh_ratio_mean']:.3f} (2pi={TWO_PI:.3f})  "
          f"I_r2={I.get('boost_r2_mean', float('nan')):.3f} SH_r2={SH['boost_r2_mean']:.3f}  "
          f"elapsed={elapsed:.1f}s")
    return results


def _flush_partial(per_seed, Ns, n_seeds, t_start, status):
    partial = {
        "schema": "modular-kms-thermal/v1",
        "status": status,
        "calc": "H6g-1 modular KMS / thermal-time content of SJ modular flow (2D Rindler slab)",
        "config": {"Ns": Ns, "n_seeds": n_seeds},
        "per_seed": per_seed,
        "elapsed_s": float(time.time() - t_start),
    }
    write_results_atomic(partial, os.path.join(OUTDIR, "results.json"))


if __name__ == "__main__":
    main()
