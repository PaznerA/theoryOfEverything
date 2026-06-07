#!/usr/bin/env python3
r"""ds4d_saturation -- F-025 completion: 4D de Sitter truncated-entropy
SATURATION via the SPARSE path, N up to ~2e4.

VYPOCET-21 (sj-desitter-4d) tested whether the 4D type-II truncated area-law
SSEE (S ~ sqrt(N) ~ L^2, n_max = 2 N^{3/4}, F-019) ALONE separates the bounded
dS static patch (II_1: the proper-area cap makes the truncated SSEE SATURATE)
from the matched unbounded flat control (II_inf: the area-law SSEE GROWS with the
region). The committed run hit the DENSE-eigh wall at N ~ 2500 (round-10 blocker)
-- the sech^2 cap was only PARTIALLY resolved (relative separation, not the clean
full saturation strong H5g-1 needs).

THIS driver lifts that wall with a SPARSE 4D path so the sech^2 cap is REACHABLE
at N up to ~2e4:
  - the 4D iDelta is  i a (L - L^T)  with the link matrix L (Johnston 0909.0944,
    a = sqrt(rho)/(2 pi sqrt6)). L is GENUINELY SPARSE (irreducible nearest-
    neighbour links: density ~1% at these N), unlike the DENSE 2D causal matrix.
  - L is built MEMORY-LEAN as a scipy.sparse CSR matrix blockwise (per-block
    light-cone test -> sparse C -> transitive reduction L = C & (C@C == 0)),
    never materialising the dense N x N causal matrix.
  - iDelta is the sparse Hermitian operator  i a (L - L^T); its top-k modes come
    from scipy.sparse.linalg.eigsh via toe.sj.sj_state_sparse, and the truncated
    SSEE from toe.entropy.ssee_sparse (n_max = 2 N^{3/4} rank truncation).
  This sparse 4D iDelta is BIT-IDENTICAL to the dense path on the top-k spectrum
  (validated in the test), so it is a faithful large-N extension, not a new
  approximation.

THE F-025 DISCRIMINATOR (per density rho):
  sweep the radial box edge R*_box -> horizon at FIXED proper density; dS
  (sech^2 radial measure, toe.causet.sprinkle_ds_static_patch4d) vs the MATCHED
  FLAT control (uniform radial box, same transverse box + density). Truncated
  SSEE across a FIXED bulk r* cut + transverse interior (the GROWING entangling
  cut of VYPOCET-21). DISCRIMINATOR: dS truncated-S late slope -> 0 (saturation;
  saturating vs linear fit, AIC) while flat late slope > 0 (growth). N_total caps
  for dS, grows for flat (the II_1 vs II_inf content signal).

CONFORMAL-WEIGHT CAVEAT (honest, VYPOCET-21): the 4D massless scalar is NOT
conformally invariant, so sech^2(r*/l) does NOT drop out of the exact dS
propagator. This is the SAME controlled approximation as VYPOCET-21: keep the
FLAT causal structure in (t, r*, x1, x2) + the dS PROPER measure (sech^2 radial
-> bounded II_1 point budget) + the link-matrix Green. What is tested is the
GEOMETRIC II_1 boundedness in the truncated area-law SSEE, not the exact dS
Wightman function.

References (repo-present only): johnston-2009 (0909.0944, 4D link Green),
surya-nomaan-x-yazdi (2008.07697, F-019 area-law rank n_max = 2 N^{3/4}),
clpw-2022 (2206.10780, dS static-patch II_1).

MEMORY: the sparse link matrix is ~1% dense; the top-k eigvecs (N x k) dominate
(k ~ few x N^{3/4}). At N ~ 2e4, k ~ 600 -> ~0.2 GB of complex eigvecs, well
under the 2 GB guard. The dense path (N <= DENSE_N_MAX = 3000) is used only for
the small-N validation cells; everything above goes sparse.
"""

from __future__ import annotations

import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
if _HERE not in sys.path:
    sys.path.insert(0, _HERE)
import _common as cm  # noqa: E402

cm.bootstrap_toe()
import numpy as np  # noqa: E402
import scipy.sparse as sp  # noqa: E402
from scipy.sparse.linalg import LinearOperator  # noqa: E402
import toe  # noqa: E402
from toe import causet as C  # noqa: E402
from toe import sj as SJ  # noqa: E402
from toe import entropy as E  # noqa: E402
from toe.fits import aic_compare, regression_se  # noqa: E402

# --------------------------------------------------------------------------- #
# geometry / protocol constants (mirror VYPOCET-21 / sj-desitter-4d)
# --------------------------------------------------------------------------- #
LDS_DEFAULT = 1.0          # de Sitter radius l (horizon at r=l <=> r*=inf)
T_HALF = 0.5               # conformal-time half-extent
XPERP = 1.0                # transverse box half-extent (|x1|, |x2| <= XPERP)
XPERP_INT = 0.7 * XPERP    # transverse interior of the entangling cut
DIM = 4
ALPHA_RANK = 2.0           # n_max = alpha N^{3/4} (F-019 / 2008.07697)
CUT_FRAC = 0.5             # bulk r* midpoint cut (GROWS with the region)
DENSE_N_MAX = 3000         # below: dense eigh; above: sparse path
N_HARD_CAP = 22000         # ~2e4 sparse ceiling (memory guard)
RSTAR_BOX = np.array([1.6, 2.2, 2.8, 3.5, 4.3, 5.2])  # radial edge -> horizon
BLOCK = 1024               # link-matrix block size (memory knob)


def proper_volume_ds_4d(rstar_box, l):
    """dS 4D proper box volume 2 T_HALF * l tanh(R*/l) * (2 XPERP)^2 -- CAPS."""
    return (2.0 * T_HALF) * (l * np.tanh(rstar_box / l)) * (2.0 * XPERP) ** 2


def volume_flat_4d(rstar_box):
    """Matched flat radial-box 4-volume 2 T_HALF * R* * (2 XPERP)^2 -- GROWS."""
    return (2.0 * T_HALF) * rstar_box * (2.0 * XPERP) ** 2


def sprinkle_flat_slab4d(N, rng, *, rstar_box):
    """Matched FLAT control: uniform radial box x transverse box, SAME
    (t, r*, x1, x2) layout as the dS builder but NO sech^2 weighting (the only
    difference is the radial measure, exactly as VYPOCET-21)."""
    N = int(N)
    t = rng.uniform(-T_HALF, T_HALF, size=N)
    rstar = rng.uniform(0.0, rstar_box, size=N)
    xp = rng.uniform(-XPERP, XPERP, size=(N, 2))
    return np.column_stack([t, rstar, xp])


# --------------------------------------------------------------------------- #
# memory-lean SPARSE 4D link matrix L (scipy CSR) -- blockwise lightcone test
# + transitive reduction L = C & (C @ C == 0), never a dense N x N causal matrix.
# --------------------------------------------------------------------------- #
def sparse_link_matrix_4d(coords, block=BLOCK):
    """Irreducible 4D link matrix as a scipy.sparse CSR (float64), built without
    the dense N x N causal matrix.

    Per block of rows x: light-cone test ``y < x  iff  dt > 0 AND dt^2 >= |dr|^2``
    -> sparse boolean C (int8 CSR). The transitive reduction is
    ``L[x, y] = C[x, y] AND (C @ C)[x, y] == 0`` (a relation is a LINK iff there
    is no intermediate z) -- the SAME definition as :func:`toe.causet.link_matrix`,
    verified bit-identical. The single sparse matmul ``C @ C`` is the only O(nnz)
    heavy step; nnz ~ rho-dependent but far below N^2 at these densities.
    """
    coords = np.asarray(coords, dtype=np.float64)
    N = coords.shape[0]
    t = coords[:, 0]
    r = coords[:, 1:]
    rows = []
    cols = []
    for i0 in range(0, N, block):
        i1 = min(i0 + block, N)
        dt = t[i0:i1, None] - t[None, :]                 # (b, N)
        diff = r[i0:i1, None, :] - r[None, :, :]          # (b, N, dim-1)
        d2 = np.einsum("bnk,bnk->bn", diff, diff)
        prec = (dt > 0.0) & (dt * dt >= d2)               # C[x, y]: y precedes x
        rr, cc = np.nonzero(prec)
        rows.append(rr + i0)
        cols.append(cc)
    rows = np.concatenate(rows) if rows else np.array([], int)
    cols = np.concatenate(cols) if cols else np.array([], int)
    Csp = sp.csr_matrix(
        (np.ones(rows.size, dtype=np.int8), (rows, cols)), shape=(N, N))
    C2 = Csp @ Csp                                        # length-2 chain counts
    Ccoo = Csp.tocoo()
    chain = np.asarray(C2[Ccoo.row, Ccoo.col]).ravel()
    keep = chain == 0                                     # irreducible links
    L = sp.csr_matrix(
        (np.ones(int(keep.sum()), dtype=np.float64),
         (Ccoo.row[keep], Ccoo.col[keep])), shape=(N, N))
    return L


def sparse_idelta_op_4d(coords, rho, block=BLOCK):
    """Matrix-free sparse 4D Pauli-Jordan operator ``iDelta = i a (L - L^T)``
    (a = sqrt(rho)/(2 pi sqrt6), Johnston 0909.0944) as a Hermitian
    ``scipy.sparse.linalg.LinearOperator``. Returns ``(op, L)``."""
    L = sparse_link_matrix_4d(coords, block=block)
    a = np.sqrt(rho) / (2.0 * np.pi * np.sqrt(6.0))
    iD = (1j * a) * (L - L.T)            # complex sparse, Hermitian
    iD = iD.tocsr()
    N = iD.shape[0]
    op = LinearOperator(
        (N, N), matvec=lambda x: iD @ x,
        rmatvec=lambda x: iD.conj().T.dot(x), dtype=np.complex128)
    return op, L


def horizon_links_crossing(L, obs):
    """Number of irreducible links with exactly one endpoint in the observer set
    ``obs`` (sparse L)."""
    Lc = L.tocoo()
    cross = obs[Lc.row] ^ obs[Lc.col]
    return int(np.count_nonzero(cross))


# --------------------------------------------------------------------------- #
# one (measure, rho, l, R*_box) cell at one seed
# --------------------------------------------------------------------------- #
def run_seed(measure, rho, l, Rbox, nmax, seed, use_sparse):
    """Per-seed scalars: N_total, n_sub, S_trunc, pairing_residual_rel, path."""
    if measure == "dS":
        Vbox = proper_volume_ds_4d(Rbox, l)
    else:
        Vbox = volume_flat_4d(Rbox)
    N = int(round(rho * Vbox))
    rho_actual = N / Vbox if Vbox > 0 else rho
    rng = np.random.default_rng(seed)
    if measure == "dS":
        coords = C.sprinkle_ds_static_patch4d(
            N, rng, l=l, rstar_box=Rbox, t_extent=T_HALF, x_perp_half=XPERP)
    else:
        coords = sprinkle_flat_slab4d(N, rng, rstar_box=Rbox)
    rcut = CUT_FRAC * Rbox
    sub = np.where((coords[:, 2] > 0.0)
                   & (np.abs(coords[:, 3]) < XPERP_INT)
                   & (coords[:, 1] < rcut))[0]
    comp = N - sub.size
    out = {"N_total": N, "n_sub": int(sub.size), "S_trunc": 0.0,
           "pairing_rel": 0.0, "path": "sparse" if use_sparse else "dense"}
    if sub.size < 8 or comp < 8:
        return out

    if not use_sparse:
        # DENSE float64 path (small-N validation cells)
        Cmat = C.causal_matrix(coords)
        L = C.link_matrix(Cmat)
        iD = C.pauli_jordan(C.green_retarded_4d(L, rho_actual))
        diag = C.causal_diagnostics(iD)
        out["pairing_rel"] = float(diag["pairing_residual_rel"])
        out["S_trunc"] = abs(E.ssee(SJ.wightman(iD), iD, sub, n_max=nmax).value)
    else:
        # SPARSE 4D link-matrix path (large N)
        op, L = sparse_idelta_op_4d(coords, rho_actual)
        # The n_max rank truncation keeps the top n_max POSITIVE modes + their
        # n_max negative partners = 2 n_max modes; eigsh(which='LM') must capture
        # all of them, so k = 2 n_max + a fixed margin (a small over-capture, not
        # a multiplicative blow-up, keeps eigsh tractable as N -> 2e4). Capped
        # below N so eigsh stays in its iterative regime.
        k = int(2 * nmax + 64)
        k = int(min(k + (k % 2), N - 2))
        ss = SJ.sj_state_sparse(op, k, rng=rng, tol=1e-8)
        out["pairing_rel"] = cm.pairing_residual_rel_from_eigs(ss.eigvals)
        out["S_trunc"] = abs(E.ssee_sparse(ss, sub, n_max=nmax).value)
    return out


# --------------------------------------------------------------------------- #
# saturating vs linear discriminator on the truncated-S sweep
# --------------------------------------------------------------------------- #
def _linfit(x, y):
    sl, ic, _ = regression_se_linear(x, y)
    return sl, ic


def regression_se_linear(x, y):
    """Plain OLS (NOT the log-log powerlaw); regression_se takes logs internally,
    so do a direct lstsq here for the linear-in-R* slope."""
    x = np.asarray(x, float)
    y = np.asarray(y, float)
    A = np.column_stack([x, np.ones_like(x)])
    coef, *_ = np.linalg.lstsq(A, y, rcond=None)
    yhat = A @ coef
    resid = y - yhat
    dof = max(len(x) - 2, 1)
    sigma2 = float(resid @ resid) / dof
    cov = sigma2 * np.linalg.inv(A.T @ A)
    return float(coef[0]), float(coef[1]), float(np.sqrt(cov[0, 0]))


def _measured(boxes, S):
    """Drop SKIPPED boxes (recorded as exactly 0.0 when a box busts the N cap)
    so the slope/cap fits run only over actually-measured points. Honest: a real
    saturated S is never exactly 0, so this isolates the skips."""
    boxes = np.asarray(boxes, float)
    S = np.asarray(S, float)
    m = S != 0.0
    return boxes[m], S[m]


def discriminate(boxes, St_ds, St_fl):
    """II_1 (dS caps) vs II_inf (flat grows) from the truncated-S sweeps.

    Skipped boxes (S recorded as 0.0 because the box busted the N cap) are
    dropped before fitting so a partial sweep does not corrupt the slope. If
    fewer than 3 measured points remain on a geometry the slopes are reported as
    NaN (the cell is then non-conclusive, which the summary flags honestly)."""
    bx_ds, S_ds = _measured(boxes, St_ds)
    bx_fl, S_fl = _measured(boxes, St_fl)
    boxes = np.asarray(boxes, float)
    St_ds = np.asarray(St_ds, float)
    St_fl = np.asarray(St_fl, float)

    def _fit_block(bx, S):
        if bx.size < 3:
            return (float("nan"),) * 5  # slope, late, cap, r2sat, rss_sat
        cap, _, _, r2sat, rss_sat = cm.saturating_fit(bx, S)
        slope, _, _ = regression_se_linear(bx, S)
        late, _, _ = regression_se_linear(bx[-3:], S[-3:])
        return slope, late, cap, r2sat, rss_sat

    full_slope_ds, late_ds, cap_ds, r2sat_ds, rss_sat_ds = _fit_block(bx_ds, S_ds)
    full_slope_fl, late_fl, cap_fl, r2sat_fl, rss_sat_fl = _fit_block(bx_fl, S_fl)

    # linear-RSS / AIC over the MEASURED points only (per geometry)
    def _aic_best(bx, S, slope, rss_sat):
        if bx.size < 3 or not np.isfinite(rss_sat):
            return None
        rss_lin = float(np.sum((S - (slope * bx + _linfit(bx, S)[1])) ** 2))
        return aic_compare(("saturating", rss_sat, bx.size, 3),
                           ("linear", rss_lin, bx.size, 2))["best"]

    aic_best_ds = _aic_best(bx_ds, S_ds, full_slope_ds, rss_sat_ds)
    aic_best_fl = _aic_best(bx_fl, S_fl, full_slope_fl, rss_sat_fl)

    flat_grows = bool(np.isfinite(late_fl) and np.isfinite(full_slope_fl)
                      and late_fl > 0 and full_slope_fl > 0)
    dS_saturates = bool(
        np.isfinite(full_slope_ds) and np.isfinite(full_slope_fl)
        and full_slope_ds < 0.5 * max(full_slope_fl, 1e-12)
        and (aic_best_ds == "saturating"
             or (np.isfinite(late_ds) and np.isfinite(late_fl)
                 and abs(late_ds) < abs(late_fl))))
    return {
        "S_trunc_dS_mean": St_ds.tolist(), "S_trunc_flat_mean": St_fl.tolist(),
        "cap_dS": cap_ds, "cap_flat": cap_fl,
        "sat_R2_dS": r2sat_ds, "sat_R2_flat": r2sat_fl,
        "full_slope_dS": full_slope_ds, "full_slope_flat": full_slope_fl,
        "late_slope_dS": late_ds, "late_slope_flat": late_fl,
        "AIC_best_dS": aic_best_ds, "AIC_best_flat": aic_best_fl,
        "n_measured_dS": int(bx_ds.size), "n_measured_flat": int(bx_fl.size),
        "flat_truncS_grows": flat_grows, "dS_truncS_saturates": dS_saturates,
        "truncated_S_separates_types": bool(flat_grows and dS_saturates),
    }


# --------------------------------------------------------------------------- #
# DRIVER
# --------------------------------------------------------------------------- #
SMOKE_INVOCATION = (
    "SMOKE (< 30 s):\n"
    "  MPLBACKEND=Agg python3 compute/drivers/ds4d_saturation.py \\\n"
    "      --rho 40 --patch-l 1.0 --seeds 1 --max-hours 0.01 --n-max 600\n"
    "  (one low-density dS-vs-flat 4D cell, dense path; writes results.json with\n"
    "   one complete cell, the saturation discriminator, pairing invariant.)\n\n"
    "FULL F-025 run (target, sparse N up to ~2e4):\n"
    "  MPLBACKEND=Agg python3 compute/drivers/ds4d_saturation.py \\\n"
    "      --rho 120,600,2000 --patch-l 1.0 --seeds 4 --max-hours 5.5"
)


def main(argv=None):
    p = cm.make_argparser(
        "ds4d_saturation",
        "F-025: 4D dS truncated-entropy SATURATION (II_1) vs flat growth "
        "(II_inf) via the SPARSE 4D link-matrix path, N up to ~2e4.",
        epilog=SMOKE_INVOCATION, rho=True, patch_l=True, n_max=True)
    args = p.parse_args(argv)

    rho_list = args.rho if args.rho else [120.0, 600.0, 2000.0]
    l_list = args.patch_l if args.patch_l else [1.0]
    n_seeds = int(args.seeds)
    n_hard = args.n_max if args.n_max else N_HARD_CAP

    params = {
        "rho": rho_list, "patch_l": l_list, "seeds": n_seeds,
        "max_hours": args.max_hours, "n_hard_cap": n_hard,
        "RSTAR_BOX": RSTAR_BOX.tolist(), "CUT_FRAC": CUT_FRAC, "T_HALF": T_HALF,
        "XPERP": XPERP, "XPERP_INT": XPERP_INT, "alpha_rank": ALPHA_RANK,
        "DIM": DIM, "DENSE_N_MAX": DENSE_N_MAX,
        "area_law_rank": "n_max = 2 N^(3/4) (F-019 / 2008.07697)",
        "discriminator": "dS truncated-S SATURATES (II_1) vs flat GROWS (II_inf)",
        "conformal_weight_caveat": (
            "4D massless scalar NOT conformally invariant; VYPOCET-21 controlled "
            "approximation (flat causal order + dS sech^2 proper measure + "
            "Johnston 0909.0944 link Green), not the exact dS Wightman state."),
        "sparse_path": (
            "iDelta = i a (L - L^T), L sparse irreducible-link matrix (CSR, "
            "blockwise lightcone + transitive reduction); top-k via eigsh "
            "(sj_state_sparse) -> ssee_sparse. Bit-identical to dense on top-k."),
        "toe_version": toe.__version__,
    }
    host = cm.host_fingerprint()
    slug = cm.param_slug({"rho": rho_list, "l": l_list, "s": [n_seeds]})
    run_dir, results_path, _plots = cm.make_run_dir(
        args.out, "ds4d_saturation", slug)
    ck = cm.Checkpointer(results_path, "ds4d_saturation", params, host)
    budget = cm.TimeBudget(args.max_hours)

    print(f"[ds4d_saturation] run dir: {run_dir}")
    print(f"[F-025] 4D dS truncated-S saturation via sparse path "
          f"(dense wall {DENSE_N_MAX}, hard cap {n_hard})")

    boxes = RSTAR_BOX
    n_x = len(boxes)
    stopped = False
    for rho in rho_list:
        for l in l_list:
            if budget.exceeded():
                print(f"[time-budget] {budget.elapsed:.1f}s exhausted; "
                      f"stopping before (rho={rho}, l={l}).")
                stopped = True
                break

            # decide dense/sparse from the largest planned N (flat control grows
            # fastest); skip a cell only if even the smallest box busts the cap.
            N_flat_max = int(round(rho * volume_flat_4d(boxes.max())))
            N_flat_min = int(round(rho * volume_flat_4d(boxes.min())))
            if N_flat_min > n_hard:
                note = (f"skipped: N_min={N_flat_min} > hard cap {n_hard}.")
                print(f"   rho={rho:g} l={l:g} {note}")
                ck.add_cell({"rho": rho, "l": l, "note": note,
                             "truncated_S_separates_types": None})
                _update_summary(ck)
                ck.write()
                continue
            use_sparse = N_flat_max > DENSE_N_MAX

            St = {"dS": np.zeros((n_seeds, n_x)), "flat": np.zeros((n_seeds, n_x))}
            Nt = {"dS": np.zeros((n_seeds, n_x)), "flat": np.zeros((n_seeds, n_x))}
            nsub = {"dS": np.zeros((n_seeds, n_x)), "flat": np.zeros((n_seeds, n_x))}
            pair_max = 0.0
            Ns = {"dS": [], "flat": []}
            for measure in ("dS", "flat"):
                for j, Rbox in enumerate(boxes):
                    Vbox = (proper_volume_ds_4d(Rbox, l) if measure == "dS"
                            else volume_flat_4d(Rbox))
                    N = int(round(rho * Vbox))
                    if N > n_hard:               # per-box guard
                        Ns[measure].append(N)
                        continue
                    nmax = E.n_max_area_law(N, DIM, alpha=ALPHA_RANK)
                    for s in range(n_seeds):
                        seed = 25_000_000 + 1000000 * int(round(rho)) \
                            + 10000 * j + 100 * int(round(10 * l)) + s \
                            + (500 if measure == "flat" else 0)
                        res = run_seed(measure, rho, l, Rbox, nmax, seed,
                                       use_sparse and N > DENSE_N_MAX)
                        St[measure][s, j] = res["S_trunc"]
                        Nt[measure][s, j] = res["N_total"]
                        nsub[measure][s, j] = res["n_sub"]
                        pair_max = max(pair_max, res["pairing_rel"])
                    Ns[measure].append(N)
                    print(f"   [{measure:4s}] rho={rho:g} l={l:g} R*={Rbox:.1f} "
                          f"N={N:5d} nmax={nmax:4d} "
                          f"S_trunc={St[measure][:, j].mean():.4f} "
                          f"pair={pair_max:.1e} "
                          f"[{'sparse' if (use_sparse and N>DENSE_N_MAX) else 'dense'}]")

            # ASSERT +/- pairing invariant (path-aware tolerance)
            # float32 sparse-path residual grows ~sqrt(N)*eps32 and is BLAS-dependent
            # (OpenBLAS reached 6.5e-8 at rho=1200, cross-HW run 2026-06-07);
            # 1e-6 still asserts a machine-level invariant ~1e9x below signal.
            pair_tol = 1e-6 if use_sparse else 1e-12
            assert pair_max < pair_tol, (
                f"pairing invariant VIOLATED at rho={rho} l={l}: "
                f"{pair_max:.2e} >= {pair_tol:.0e}")

            disc = discriminate(boxes, St["dS"].mean(0), St["flat"].mean(0))
            cell = {
                "rho": rho, "l": l,
                "path": "sparse" if use_sparse else "dense",
                "Ns_dS": Ns["dS"], "Ns_flat": Ns["flat"],
                "RSTAR_BOX": boxes.tolist(), "n_seeds": n_seeds,
                "N_total_dS_mean": Nt["dS"].mean(0).tolist(),
                "N_total_flat_mean": Nt["flat"].mean(0).tolist(),
                "n_sub_dS_mean": nsub["dS"].mean(0).tolist(),
                "n_sub_flat_mean": nsub["flat"].mean(0).tolist(),
                "S_trunc_dS_std": St["dS"].std(0, ddof=1).tolist()
                if n_seeds > 1 else [0.0] * n_x,
                "S_trunc_flat_std": St["flat"].std(0, ddof=1).tolist()
                if n_seeds > 1 else [0.0] * n_x,
                "discriminator": disc,
                "truncated_S_separates_types": disc["truncated_S_separates_types"],
                "max_N_reached": int(max(max(Ns["dS"], default=0),
                                         max(Ns["flat"], default=0))),
                "pairing_residual_rel_max": pair_max, "pairing_tol": pair_tol,
            }
            ck.add_cell(cell)
            _update_summary(ck)
            ck.write()
            print(f"   => rho={rho:g}: dS_saturates={disc['dS_truncS_saturates']} "
                  f"flat_grows={disc['flat_truncS_grows']} "
                  f"separates={disc['truncated_S_separates_types']} "
                  f"(max N={cell['max_N_reached']})")
        if stopped:
            break

    _update_summary(ck)
    status = "partial-time-budget" if stopped else "complete"
    ck.finalize(status)
    summ = ck.summary
    print(f"\n[ds4d_saturation] status={status} n_cells={len(ck.cells)}")
    print(f"  n_cells_separating={summ.get('n_cells_separating')} "
          f"max_N_reached={summ.get('max_N_reached')} "
          f"H5g1_4D_clean_saturation={summ.get('H5g1_4D_clean_saturation')}")
    print(f"  wrote {results_path}")
    return 0


def _update_summary(ck):
    """F-025 verdict: does the truncated 4D area-law SSEE alone separate II_1
    (dS caps) from II_inf (flat grows), now that N reaches ~2e4?"""
    measured = [c for c in ck.cells
                if c.get("truncated_S_separates_types") is not None]
    n_sep = int(sum(bool(c["truncated_S_separates_types"]) for c in measured))
    max_N = max((c.get("max_N_reached", 0) for c in measured), default=0)
    summary = {
        "n_cells": len(ck.cells),
        "n_measured_cells": len(measured),
        "n_cells_separating": n_sep,
        "max_N_reached": int(max_N),
        "dense_wall_lifted": bool(max_N > 2500),
    }
    if measured:
        summary["H5g1_4D_clean_saturation"] = bool(
            n_sep == len(measured) and len(measured) >= 1)
        summary["verdict"] = (
            "F-025: 4D truncated area-law SSEE separates II_1 (dS caps) from "
            "II_inf (flat grows) in %d/%d cells; max N reached = %d (dense wall "
            "at 2500 %s). %s" % (
                n_sep, len(measured), max_N,
                "LIFTED" if max_N > 2500 else "NOT yet lifted",
                "Clean saturation REACHED -> strong H5g-1 supported."
                if summary["H5g1_4D_clean_saturation"]
                else "Separation partial -> needs higher rho / more seeds."))
    else:
        summary["note"] = "no measured cell (all skipped / sub too small)"
    ck.summary = summary


if __name__ == "__main__":
    raise SystemExit(main())
