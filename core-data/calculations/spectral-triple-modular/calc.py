#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
H5g-4 : SPECTRAL-TRIPLE / MODULAR-FLOW proof of concept (2D slab)
================================================================
Does a candidate spectral triple's Dirac operator reproduce the Sorkin-Johnston
(SJ) modular Hamiltonian / modular flow on a 2D slab?

THE PROGRAM QUESTION
--------------------
Causal sets (line A) and noncommutative geometry / spectral triples (line B)
are two of the program's pillars. They share an object in principle -- a Dirac
operator D that encodes both the dynamics and the metric -- but the link has
never been instantiated: the causal-sets-vs-NCG edge is rated `barely`. This
calculation tests one concrete bridge:

    take the SJ one-particle MODULAR Hamiltonian K(x,y) of a Rindler-like 2D
    slab cut (whose modular flow is the Bisognano-Wichmann BOOST), build a
    candidate Dirac operator D_K = sgn(K) sqrt(|K|), and ask whether the finite
    spectral triple (A = diagonal functions, H = C^n, D = D_K) reproduces the
    modular structure:
      (1) SPECTRUM: spec(D_K) = sgn(K) sqrt(|K|) by construction; we report the
          best-fit overall scale relating spec(K) and spec(D_K)^2 and the match
          metric (this is a consistency check of the functional calculus, not a
          free test).
      (2) LOCALITY of K on the slab: off-diagonal decay |K(x,y)| vs |x-y|
          (negative log-log slope = local boost) and diagonal boost weight
          |K(x,x)| vs distance-to-cut (Bisognano-Wichmann predicts LINEAR).
      (3) WEYL dimension: counting of |spec(D_K)| <= Lambda should grow with an
          effective dimension ~ 2 on the 2D slab.
      (4) CONNES distance d_D(x,y) = sup{|a(x)-a(y)| : ||[D,a]||_op <= 1} on a
          small point subset, CORRELATED against the causal/geodesic distance.

VERDICT LOGIC (pre-registered, from the feasibility recipe)
-----------------------------------------------------------
PASS (matches): diagonal boost LINEAR (R2 > 0.9), off-diagonal decay NEGATIVE
  log-log slope (R2 > 0.8), Weyl dimension in [1.7, 2.3], AND Connes distance
  POSITIVELY correlated with causal/geodesic distance.
PARTIAL: spectrum/locality recovered but Connes distance does not track the
  causal distance (or vice versa).
NO-MATCH: broken locality, non-linear boost, or uncorrelated Connes distance.
A negative is a clean result: the edge stays `barely`.

CAVEAT (honest, recipe-mandated): D_K is a SURROGATE Dirac (the square-root-
modulus of the modular kernel), NOT a from-first-principles causal-set Dirac of
a known KO-dimension / real-structure spectral triple. We test whether the
modular data ALONE carries metric (Connes) + locality content, not whether the
full axiomatic spectral triple exists.

----------------------------------------------------------------------------
CONVENTIONS (verified literature only -- IDs cited in results.json / writeup)
----------------------------------------------------------------------------
SJ state + modular kernel (dimension-independent):
  iDelta = i(G_R - G_R^T); 2D massless G_R = (1/2) C (Sorkin-Yazdi 1611.10281).
  W = positive spectral part of iDelta (SJ Wightman).
  One-particle modular Hamiltonian K(x,y) on region O from the SSEE generalized
  eigenproblem W_O v = mu iDelta_O v, eps = ln[mu/(mu-1)] (Casini-Huerta
  0905.2562), lifted to the site basis. UNTRUNCATED probe (kappa=None) = the
  genuine SJ modular flow whose geometricity Bisognano-Wichmann (1712.04227,
  context 2008.07697) predicts.
Candidate Dirac: D_K = sgn(K) sqrt(|K|) (symmetric functional calculus; D_K^2 =
  |K|, same eigenvectors as K).
Connes distance: d_D(x,y) = sup{|a(x)-a(y)| : ||[D,a]||_op <= 1} (Connes
  'Noncommutative Geometry', Academic Press 1994 -- the spectral-distance
  formula; commutative diagonal algebra, [D,a]_ij = D_ij (a_j - a_i), norm =
  largest singular value). Connes-Rovelli gr-qc/9406019 ("Von Neumann Algebra
  Automorphisms and Time-Thermodynamics Relation") motivates the modular-flow-
  as-thermal-time reading; it is NOT the distance-formula source.

All paths are derived __file__-relative (portability guard). results.json uses a
fixed schema with a 'status' field + atomic write (tmp + os.replace).
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
# lib/toe on sys.path (repo_root/lib), resolved __file__-relative
_REPO_ROOT = os.path.abspath(os.path.join(OUTDIR, os.pardir, os.pardir, os.pardir))
_LIB = os.path.join(_REPO_ROOT, "lib")
if _LIB not in sys.path:
    sys.path.insert(0, _LIB)

from toe.causet import sprinkle_slab2d, causal_matrix, green_retarded_2d, pauli_jordan
from toe.sj import sj_state
from toe.entropy import modular_kernel
from toe.spectraltriple import dirac_from_kernel, connes_distance, connes_commutator_norm


# ===========================================================================
# CONFIG
# ===========================================================================
T_EXTENT = 0.30      # slab temporal extent (T << L: Rindler-like half-space)
X_EXTENT = 1.0       # slab spatial half-extent (|x| < L)
WALL_CAP_S = 25 * 60  # 25 min total wall-clock cap


# ===========================================================================
# FIT HELPERS (verbatim convention from modular-flow-bd-4d/calc.py)
# ===========================================================================

def r2(y, yhat):
    y = np.asarray(y, float)
    ss = np.sum((y - y.mean()) ** 2)
    return 1.0 - np.sum((y - yhat) ** 2) / ss if ss > 0 else 0.0


def loglog_slope(x, y, mask=None):
    x = np.asarray(x, float); y = np.asarray(y, float)
    m = np.isfinite(x) & np.isfinite(y) & (x > 0) & (y > 0)
    if mask is not None:
        m &= mask
    if m.sum() < 3:
        return None, None, None
    lx = np.log(x[m]); ly = np.log(y[m])
    A = np.vstack([lx, np.ones_like(lx)]).T
    coef, *_ = np.linalg.lstsq(A, ly, rcond=None)
    return float(coef[0]), float(coef[1]), float(r2(ly, A @ coef))


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
    """Atomic JSON write: tmp file in same dir + os.replace (CLAUDE.md schema)."""
    tmp = path + ".tmp"
    with open(tmp, "w") as fh:
        json.dump(_to_native(results), fh, indent=2)
    os.replace(tmp, path)


# ===========================================================================
# LOCALITY DIAGNOSTICS  (verbatim from modular-flow-codim2/helpers.py logic)
# ===========================================================================

def offdiag_slope(Kabs, Dij, n_bins=16):
    """log-log slope of mean |K(x,y)| vs |x-y| (negative = local decay)."""
    n = Kabs.shape[0]
    off = ~np.eye(n, dtype=bool)
    dv = Dij[off].ravel(); kv = Kabs[off].ravel()
    keep = dv > 1e-9
    dv = dv[keep]; kv = kv[keep]
    if dv.size < 10:
        return None, None, None, None
    dmax = np.percentile(dv, 97)
    bins = np.linspace(0, dmax, n_bins + 1)
    centers = 0.5 * (bins[:-1] + bins[1:])
    idx = np.digitize(dv, bins)
    prof = np.full(n_bins, np.nan); cnt = np.zeros(n_bins, int)
    for b in range(1, n_bins + 1):
        msk = idx == b
        cnt[b - 1] = msk.sum()
        if msk.sum() > 0:
            prof[b - 1] = np.mean(kv[msk])
    sl, _, r2v = loglog_slope(centers, prof, mask=cnt >= 8)
    return sl, r2v, centers, prof


def diag_weight_vs_distance(diag, coords_sub, surface_value=0.0, n_bins=14):
    """Diagonal boost weight |K(x,x)| vs distance to cut x=surface_value
    (Bisognano-Wichmann predicts LINEAR ~ distance)."""
    xcoord = coords_sub[:, 1]
    dist = np.abs(xcoord - surface_value)
    order = np.argsort(dist)
    dist = dist[order]; w = np.abs(diag)[order]
    bins = np.linspace(dist.min(), np.percentile(dist, 98), n_bins + 1)
    centers = 0.5 * (bins[:-1] + bins[1:])
    idx = np.digitize(dist, bins)
    prof = np.full(n_bins, np.nan); cnt = np.zeros(n_bins, int)
    for b in range(1, n_bins + 1):
        msk = idx == b
        cnt[b - 1] = msk.sum()
        if msk.sum() > 0:
            prof[b - 1] = np.mean(w[msk])
    return centers, prof, cnt


def weyl_dimension(eigD, n_lam=18):
    """Effective Weyl dimension from the counting function N(Lambda) =
    #{|spec(D)| <= Lambda}: log-log slope of N vs Lambda.

    For a d-dimensional Dirac operator the eigenvalue density gives N(Lambda) ~
    Lambda^d (Weyl law), so the log-log slope of N vs Lambda estimates d. We fit
    on the bulk of the spectrum (avoiding the saturated top and the sparse
    bottom)."""
    s = np.sort(np.abs(np.asarray(eigD)))
    s = s[s > 1e-12]
    if s.size < 8:
        return None, None, None, None
    lam_grid = np.linspace(np.percentile(s, 10), np.percentile(s, 90), n_lam)
    N_of = np.array([np.sum(s <= L) for L in lam_grid], dtype=float)
    sl, _, r2v = loglog_slope(lam_grid, N_of, mask=N_of > 0)
    return sl, r2v, lam_grid, N_of


# ===========================================================================
# ONE SEED:  slab -> SJ -> K -> D_K -> diagnostics
# ===========================================================================

def run_seed(N, seed):
    """Build the 2D slab modular kernel K and Dirac D_K for one seed; return all
    diagnostics + the K, D_K, coords for the (optional) Connes pass."""
    rng = np.random.default_rng(seed)
    coords = sprinkle_slab2d(N, rng, t_extent=T_EXTENT, x_extent=X_EXTENT)
    C = causal_matrix(coords)               # 2D flat lightcone order
    iDelta = pauli_jordan(green_retarded_2d(C))
    st = sj_state(iDelta)
    W = st.W
    # HALF-LINE / RINDLER cut: O = {x > 0} (Bisognano-Wichmann boost modular flow)
    sub_idx = np.where(coords[:, 1] > 0.0)[0]
    if sub_idx.size < 8:
        return None
    mk = modular_kernel(W, iDelta, sub_idx, kappa=None)   # untruncated SJ flow
    if mk is None:
        return None
    K = mk.K
    coords_sub = coords[sub_idx]
    # --- candidate Dirac ---------------------------------------------------
    D_K = dirac_from_kernel(K)
    lamK = np.linalg.eigvalsh(0.5 * (K + K.conj().T))
    lamD = np.linalg.eigvalsh(D_K)

    # --- (1) spectrum consistency: D_K^2 == |K| up to scale ----------------
    # best-fit scale s minimizing || lamD^2 - s*|lamK| ||: closed-form ratio.
    abslamK = np.sort(np.abs(lamK))
    lamD2 = np.sort(lamD ** 2)
    m = min(abslamK.size, lamD2.size)
    aK = abslamK[-m:]; aD = lamD2[-m:]
    denom = float(np.dot(aK, aK))
    scale = float(np.dot(aD, aK) / denom) if denom > 0 else float("nan")
    resid = aD - scale * aK
    spec_match_r2 = float(r2(aD, scale * aK)) if aD.size else float("nan")
    spec_rel_resid = (float(np.linalg.norm(resid) / (np.linalg.norm(aD) + 1e-30))
                      if aD.size else float("nan"))

    # --- (2) locality of K on the slab ------------------------------------
    Kabs = np.abs(K)
    xs = coords_sub[:, 1:]                    # spatial coordinate(s)
    diff = xs[:, None, :] - xs[None, :, :]
    Dij = np.sqrt(np.einsum("ijk,ijk->ij", diff, diff))
    off_sl, off_r2, off_cen, off_prof = offdiag_slope(Kabs, Dij)

    diag = np.real(np.diag(K))
    dcen, dprof, dcnt = diag_weight_vs_distance(diag, coords_sub, surface_value=0.0)
    dmask = dcnt >= 8
    boost_slope, boost_int, boost_r2 = linfit(dcen, dprof, mask=dmask)

    # --- (3) Weyl dimension from spec(D_K) --------------------------------
    weyl_sl, weyl_r2, weyl_lam, weyl_N = weyl_dimension(lamD)

    out = {
        "N": int(N), "seed": int(seed), "n_sub": int(sub_idx.size),
        "n_modes": int(mk.n_modes), "S": float(mk.S),
        "spec_scale_D2_over_absK": scale,
        "spec_match_r2": spec_match_r2,
        "spec_rel_resid": spec_rel_resid,
        "offdiag_slope": off_sl, "offdiag_r2": off_r2,
        "boost_diag_slope": boost_slope, "boost_diag_r2": boost_r2,
        "weyl_dim": weyl_sl, "weyl_r2": weyl_r2,
    }
    payload = {
        "K": K, "D_K": D_K, "coords_sub": coords_sub, "sub_idx": sub_idx,
        "lamK": lamK, "lamD": lamD,
        "off_cen": off_cen, "off_prof": off_prof,
        "dcen": dcen, "dprof": dprof,
        "weyl_lam": weyl_lam, "weyl_N": weyl_N,
        "Dij": Dij,
    }
    return out, payload


# ===========================================================================
# CONNES DISTANCE PASS (small N subset, point pairs spanning the slab)
# ===========================================================================

def connes_pass(payload, n_pairs=16, seed=0, max_n=300, t_start=None,
                wall_cap=WALL_CAP_S):
    """Compute Connes distance d_D for ~n_pairs point pairs spanning the slab and
    correlate against the causal/geodesic (Euclidean spatial here, slab is flat)
    distance. Returns a dict; skips-with-note if N>max_n or wall budget is short.
    """
    D_K = payload["D_K"]
    coords_sub = payload["coords_sub"]
    Dij = payload["Dij"]
    n = D_K.shape[0]
    note = ""
    if n > max_n:
        # Restrict to a CONTIGUOUS spatial patch nearest the cut x=0 (the points
        # with the smallest x), NOT a random subsample: the modular Dirac is a
        # quasi-local operator, so its restriction to a contiguous region is
        # again a sensible (boundary-truncated) Dirac, whereas a random scatter
        # of points destroys the locality the Connes distance reads off.
        xv = coords_sub[:, 1]
        pick = np.sort(np.argsort(xv)[:max_n])
        D_K = D_K[np.ix_(pick, pick)]
        coords_sub = coords_sub[pick]
        Dij = Dij[np.ix_(pick, pick)]
        n = max_n
        note = (f"Connes on contiguous {max_n}-point near-cut patch "
                f"(full n={payload['D_K'].shape[0]})")

    rng = np.random.default_rng(seed + 11)
    # choose pairs spanning a range of causal/geodesic separations:
    # sort all candidate pairs by spatial distance and pick evenly across deciles
    iu = np.triu_indices(n, k=1)
    dpair = Dij[iu]
    order = np.argsort(dpair)
    sel = order[np.linspace(0, order.size - 1, n_pairs).astype(int)]
    pairs = list(zip(iu[0][sel], iu[1][sel]))

    causal_d = []
    connes_d = []
    used = 0
    for (i, j) in pairs:
        if t_start is not None and (time.time() - t_start) > wall_cap:
            note = (note + "; " if note else "") + \
                f"wall cap hit after {used}/{len(pairs)} pairs"
            break
        d_geo = float(Dij[i, j])
        d_con = connes_distance(D_K, i, j, seed=seed + used, n_random=18,
                                n_iter=40)
        if np.isfinite(d_con) and np.isfinite(d_geo) and d_geo > 0:
            causal_d.append(d_geo)
            connes_d.append(d_con)
            used += 1

    causal_d = np.array(causal_d); connes_d = np.array(connes_d)
    corr = float("nan"); slope = float("nan"); cr2 = float("nan")
    if causal_d.size >= 3:
        corr = float(np.corrcoef(causal_d, connes_d)[0, 1])
        slope, _, cr2 = linfit(causal_d, connes_d)
    return {
        "n_points_used": int(n),
        "n_pairs_used": int(causal_d.size),
        "causal_dist": causal_d.tolist(),
        "connes_dist": connes_d.tolist(),
        "pearson_corr": corr,
        "lin_slope": slope,
        "lin_r2": cr2,
        "note": note,
    }


# ===========================================================================
# PLOTS
# ===========================================================================

def plot_spectrum(payload_rep, results, path):
    lamK = payload_rep["lamK"]; lamD = payload_rep["lamD"]
    fig, axs = plt.subplots(1, 2, figsize=(11, 4.2))
    ax = axs[0]
    ax.plot(np.sort(lamK), marker=".", ls="none", label="spec(K) modular")
    ax.plot(np.sort(np.sign(lamD) * lamD ** 2), marker="x", ls="none",
            label="sgn(D_K)·D_K² (= spec K target)")
    ax.set_xlabel("mode index (sorted)"); ax.set_ylabel("eigenvalue")
    ax.set_title("Modular spectrum K vs reconstructed D_K²")
    ax.legend(fontsize=8); ax.grid(alpha=0.3)
    ax2 = axs[1]
    sK = np.sort(np.abs(lamK)); sD2 = np.sort(lamD ** 2)
    mlen = min(sK.size, sD2.size)
    ax2.plot(sK[-mlen:], sD2[-mlen:], ".", ms=4)
    lim = [0, max(sK.max(), sD2.max()) * 1.05]
    sc = results["aggregate"]["spec_scale_D2_over_absK_mean"]
    ax2.plot(lim, [sc * lim[0], sc * lim[1]], "r-", lw=1,
             label=f"scale={sc:.4f}, R²={results['aggregate']['spec_match_r2_mean']:.4f}")
    ax2.set_xlabel("|spec(K)|"); ax2.set_ylabel("spec(D_K)²")
    ax2.set_title("D_K² vs |K| (functional-calculus check)")
    ax2.legend(fontsize=8); ax2.grid(alpha=0.3)
    fig.tight_layout()
    fig.savefig(path, dpi=110)
    plt.close(fig)


def plot_connes(connes, path):
    fig, ax = plt.subplots(figsize=(6.0, 4.6))
    cd = np.array(connes["causal_dist"]); kd = np.array(connes["connes_dist"])
    if cd.size:
        ax.plot(cd, kd, "o", ms=6, alpha=0.8)
        if np.isfinite(connes["lin_slope"]):
            xx = np.linspace(cd.min(), cd.max(), 50)
            ax.plot(xx, connes["lin_slope"] * xx + (kd.mean() -
                    connes["lin_slope"] * cd.mean()), "r-", lw=1,
                    label=f"corr={connes['pearson_corr']:.3f}, "
                          f"R²={connes['lin_r2']:.3f}")
            ax.legend(fontsize=9)
    ax.set_xlabel("causal / geodesic distance |x-y|")
    ax.set_ylabel("Connes spectral distance d_D(x,y)")
    ax.set_title("Connes distance vs causal distance (2D slab)")
    ax.grid(alpha=0.3)
    fig.tight_layout()
    fig.savefig(path, dpi=110)
    plt.close(fig)


# ===========================================================================
# MAIN
# ===========================================================================

def main(argv=None):
    import argparse
    ap = argparse.ArgumentParser(
        description="H5g-4 spectral-triple / modular-flow PoC (2D slab).",
        epilog="smoke: python3 calc.py --smoke  (N=400, 2 seeds, tiny Connes)")
    ap.add_argument("--smoke", action="store_true",
                    help="tiny run for CI/dev (N=400, 2 seeds).")
    ap.add_argument("--Ns", type=int, nargs="+", default=None)
    ap.add_argument("--seeds", type=int, default=5)
    ap.add_argument("--connes-pairs", type=int, default=16)
    args = ap.parse_args(argv)

    t_start = time.time()
    status = "running"

    if args.smoke:
        Ns = [400]; n_seeds = 2; n_pairs = 8; connes_max_n = 200
    else:
        Ns = args.Ns if args.Ns else [1200]   # N<=1800 cap; 1200 = robust + fast
        n_seeds = args.seeds
        n_pairs = args.connes_pairs
        connes_max_n = 220   # recipe allows <=300; 220 keeps per-pair SVD cheap

    # cap N at 1800 (dense eigh budget)
    Ns = [min(int(N), 1800) for N in Ns]

    per_seed = []
    payloads = []
    for N in Ns:
        for s in range(n_seeds):
            res = run_seed(N, seed=1000 + 17 * s + N)
            if res is None:
                continue
            out, payload = res
            per_seed.append(out)
            payloads.append((out, payload))
            # progressive: write partial after each seed
            _flush_partial(per_seed, Ns, n_seeds, t_start, status="running")

    # ---- aggregate --------------------------------------------------------
    def agg(key):
        return _m([d[key] for d in per_seed])

    aggregate = {
        "spec_scale_D2_over_absK_mean": agg("spec_scale_D2_over_absK"),
        "spec_match_r2_mean": agg("spec_match_r2"),
        "spec_rel_resid_mean": agg("spec_rel_resid"),
        "offdiag_slope_mean": agg("offdiag_slope"),
        "offdiag_r2_mean": agg("offdiag_r2"),
        "boost_diag_slope_mean": agg("boost_diag_slope"),
        "boost_diag_r2_mean": agg("boost_diag_r2"),
        "weyl_dim_mean": agg("weyl_dim"),
        "weyl_r2_mean": agg("weyl_r2"),
        "n_sub_mean": agg("n_sub"),
    }

    # ---- Connes pass on the LARGEST-N representative seed ------------------
    # pick the seed with largest n_sub (most modes) as representative
    rep_idx = int(np.argmax([d["n_sub"] for d in per_seed])) if per_seed else 0
    rep_out, rep_payload = payloads[rep_idx]
    # t_start=None: never wall-clock-truncate the stored pair list — always
    # compute all n_pairs so the Connes output length is DETERMINISTIC (per-pair
    # cost is bounded by n_iter/n_random at N<=max_n). The earlier wall-clock cap
    # made the committed pair count timing-dependent (a reproduction non-determinism
    # caught by the kolo-21 numerical-coverage backfill).
    connes = connes_pass(rep_payload, n_pairs=n_pairs, seed=2024,
                         max_n=connes_max_n, t_start=None)

    # ===================================================================
    # VERDICT (pre-registered criteria)
    # ===================================================================
    v = {}
    v["spec_match"] = bool(np.isfinite(aggregate["spec_match_r2_mean"])
                           and aggregate["spec_match_r2_mean"] > 0.99)
    v["boost_linear"] = bool(np.isfinite(aggregate["boost_diag_r2_mean"])
                             and aggregate["boost_diag_r2_mean"] > 0.9
                             and (aggregate["boost_diag_slope_mean"] or 0) > 0)
    v["offdiag_local"] = bool(np.isfinite(aggregate["offdiag_r2_mean"])
                              and aggregate["offdiag_r2_mean"] > 0.8
                              and (aggregate["offdiag_slope_mean"] or 0) < 0)
    v["weyl_ok"] = bool(np.isfinite(aggregate["weyl_dim_mean"])
                        and 1.7 <= aggregate["weyl_dim_mean"] <= 2.3)
    v["connes_tracks_causal"] = bool(np.isfinite(connes["pearson_corr"])
                                     and connes["pearson_corr"] > 0.5
                                     and connes["n_pairs_used"] >= 3)

    spectral_geometry_ok = v["boost_linear"] and v["offdiag_local"] and v["weyl_ok"]
    if spectral_geometry_ok and v["connes_tracks_causal"]:
        correspondence = "matches"
    elif spectral_geometry_ok or v["connes_tracks_causal"]:
        correspondence = "partial"
    else:
        correspondence = "no-match"

    v["correspondence"] = correspondence
    v["spectral_geometry_ok"] = bool(spectral_geometry_ok)

    elapsed = time.time() - t_start
    status = "complete"
    results = {
        "schema": "spectral-triple-modular/v1",
        "status": status,
        "calc": "H5g-4 spectral-triple / modular-flow PoC (2D slab)",
        "config": {
            "Ns": Ns, "n_seeds": n_seeds, "T_extent": T_EXTENT,
            "X_extent": X_EXTENT, "cut": "x>0 (Rindler half-line)",
            "kappa": None, "connes_pairs": n_pairs, "connes_max_n": connes_max_n,
            "dirac_candidate": "D_K = sgn(K) sqrt(|K|) from untruncated SJ "
                               "modular kernel K(x,y)",
        },
        "references_verified": [
            "1611.10281", "1712.04227", "2008.07697", "0905.2562",
            "gr-qc/9406019", "1305.2588", "1001.2725",
        ],
        "per_seed": per_seed,
        "aggregate": aggregate,
        "connes": connes,
        "verdict": v,
        "caveat": ("D_K is a SURROGATE Dirac (square-root-modulus of the SJ "
                   "modular kernel), NOT an axiomatic causal-set spectral triple "
                   "of known KO-dimension/real structure. The test asks whether "
                   "the modular data alone carries metric+locality content."),
        "elapsed_s": float(elapsed),
    }

    out_path = os.path.join(OUTDIR, "results.json")
    write_results_atomic(results, out_path)

    # ---- plots ------------------------------------------------------------
    plot_spectrum(rep_payload, results, os.path.join(PLOTDIR, "spec_K_vs_D.png"))
    plot_connes(connes, os.path.join(PLOTDIR, "connes_vs_causal.png"))

    print(f"[done] correspondence={correspondence}  "
          f"boost_r2={aggregate['boost_diag_r2_mean']:.3f}  "
          f"offdiag_slope={aggregate['offdiag_slope_mean']:.3f}  "
          f"weyl={aggregate['weyl_dim_mean']:.3f}  "
          f"connes_corr={connes['pearson_corr']:.3f}  "
          f"elapsed={elapsed:.1f}s")
    return results


def _flush_partial(per_seed, Ns, n_seeds, t_start, status):
    """Progressive atomic write so a session-limit interrupt leaves a clean
    valid partial results.json."""
    partial = {
        "schema": "spectral-triple-modular/v1",
        "status": status,
        "calc": "H5g-4 spectral-triple / modular-flow PoC (2D slab)",
        "config": {"Ns": Ns, "n_seeds": n_seeds},
        "per_seed": per_seed,
        "elapsed_s": float(time.time() - t_start),
    }
    write_results_atomic(partial, os.path.join(OUTDIR, "results.json"))


if __name__ == "__main__":
    main()
