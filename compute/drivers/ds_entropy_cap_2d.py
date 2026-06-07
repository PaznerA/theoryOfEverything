#!/usr/bin/env python3
"""ds_entropy_cap_2d -- F-028 extension of VYPOCET-23 (H5g-2 / ds-entropy-cap).

Tighten the R_full = S_full_cap / A_mol constancy that VYPOCET-23 established
(R ~ 0.1321, CV 1.3%, implied area-law coefficient c = 1/R ~ 7.57) by pushing
to higher density (target rho up to 3e4), larger patch size l (up to 2.5) and
more seeds. If R_full stays constant over a 100x density range and a 3.5x patch
range, the discrete de Sitter cap obeys a QUANTITATIVE area law (the cap is
PROPORTIONAL to the Dou-Sorkin horizon-molecule count) and c is sharpened; if it
drifts, the cap is only a qualitative saturation. The DRIVER QUESTION downstream
(ds_cap_4d) is whether c ~ 7.57 is dimension-dependent.

PROTOCOL -- the VYPOCET-23 cap-ratio protocol VERBATIM
------------------------------------------------------
For each (rho, l):
  - sweep the box tortoise edge R*_box -> horizon (RSTAR_BOX) at FIXED proper
    density; build the 2D dS static-patch sprinkling
    (toe.causet.sprinkle_ds_static_patch2d, sech^2 proper measure -> the point
    budget CAPS = the II_1 geometric signal);
  - at a FIXED entangling cut r* = R_CUT measure (per seed):
      * S_full  = untruncated SSEE (content-tracking, volume law, the II_1 cap);
      * S_trunc = type-II truncated SSEE, |lambda| > kappa, kappa = sqrt(N)/(4 pi);
      * A_mol   = Dou-Sorkin horizon-molecule count = # irreducible causal LINKS
                  crossing the FIXED cut (the 2D codim-2 'area');
  - saturating-fit each channel vs R*_box -> the cap; bootstrap SE/CI68 over
    seeds (toe.fits-style bootstrap).
  - PRIMARY ratio R_full = S_full_cap / A_mol_cap (both ~ rho, so the ratio is
    the rho-invariant entropy-per-molecule = discrete area-law coefficient).

ANTI-CIRCULARITY (BRAINSTORM-05): the discreteness scale epsilon = rho^{-1/2} is
FIXED from the INDEPENDENT F-006 (ssee-diamond) result p_rank = 0.519 +/- 0.007
BEFORE any ratio is computed; it is NEVER tuned to make R = 1/4. Read at startup,
asserted (~1/2), used unchanged. (For R_full the eps^0 dimensionless 2D area
makes eps drop out, but we record it and use it for the secondary continuum
channel, exactly as VYPOCET-23.)

2D HORIZON-AREA CONVENTION (Dou-Sorkin gr-qc/0302009): in D dims the dS horizon
is codim-2 (area is (D-2)-dim). In D=2, D-2=0: the horizon is a POINT (the single
static-patch edge r*->inf); its discrete 'area' is the MOLECULE COUNT = number of
irreducible causal links crossing the horizon cut. In eps-units A/eps^{D-2} =
A/eps^0 = A is DIMENSIONLESS and eps-INDEPENDENT, so S_GH = A/4 is an O(1) number
in causal-set units.

MEMORY GUARD: the untruncated S_full needs the DENSE generalized eigenproblem
(all ~N modes) -- it is the volume-law content channel the top-k sparse capture
CANNOT represent. So the PRIMARY R_full ratio is measured only on cells whose
N stays under the dense wall (N <= DENSE_N_MAX = 3000). For higher densities the
dense path is unaffordable and the sparse path (toe v0.3.0) supplies only the
truncated + content-scaling consistency channel (S_full / A_mol -> NaN there).

References (repo-present only):
  dou-sorkin-2003 (gr-qc/0302009): horizon entropy as causal-link count.
  clpw-2022 (2206.10780): dS static-patch type II_1.
  bekenstein-hawking-formula (formulas.json): S = A/(4 ell_P^2) k.
  NB: the de-Sitter-specific Gibbons-Hawking primary is NOT in the repo -> the
  dS application of A/4 is marked '⚠️ neoveřeno' per policy; we report the
  dimensionless ratio R = S_cap / A_horizon (and its constancy), not a literal 4.
"""

from __future__ import annotations

import json
import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
if _HERE not in sys.path:
    sys.path.insert(0, _HERE)
import _common as cm  # noqa: E402

cm.bootstrap_toe()
import numpy as np  # noqa: E402
import toe  # noqa: E402
from toe import causet as C  # noqa: E402
from toe import sj as SJ  # noqa: E402
from toe import entropy as E  # noqa: E402

# --------------------------------------------------------------------------- #
# ANTI-CIRCULARITY: read epsilon ~ rho^{-1/2} from the INDEPENDENT F-006 result
# --------------------------------------------------------------------------- #
_F006_PATH = os.path.join(
    cm.repo_root(), "core-data", "calculations", "ssee-diamond", "results.json")
with open(_F006_PATH) as _f:
    _F006 = json.load(_f)
_KS = _F006["knee_scaling"]["entropy_cutoff_rank"]
P_RANK = float(_KS["p_rank_vs_N"])
P_RANK_ERR = float(_KS["p_err"])
EPS_EXPONENT = float(_KS["eps_exponent"])
assert abs(P_RANK - 0.5) < 0.05, (
    f"F-006 p_rank {P_RANK} not ~1/2; anti-circularity protocol broken")


def epsilon_of_rho(rho):
    """FIXED discreteness scale from F-006: eps = rho^{-1/2}. NOT tunable."""
    return float(rho) ** (-0.5)


# --------------------------------------------------------------------------- #
# geometry / protocol constants (mirror VYPOCET-19/23 part 1 VERBATIM)
# --------------------------------------------------------------------------- #
T_HALF = 1.0                       # conformal-time half-extent
R_CUT = 0.8                        # FIXED tortoise entangling cut (II_1 protocol)
RSTAR_BOX = np.array([1.6, 2.0, 2.6, 3.4, 4.4, 5.6, 7.0])  # box edge -> horizon
DENSE_N_MAX = 3000                 # dense eigh wall (memory guard, S_full needs it)


# --------------------------------------------------------------------------- #
# horizon molecule count (Dou-Sorkin gr-qc/0302009): irreducible causal LINKS
# crossing the FIXED entangling cut r* = R_CUT (the 2D codim-2 'area').
# --------------------------------------------------------------------------- #
def horizon_link_count(coords, Cmat, rcut):
    """Count irreducible causal links with exactly one endpoint each side of the
    FIXED cut r* = rcut (a 'horizon molecule'). The cut is the codim-2 horizon
    point (a worldline over the t-extent); its molecule count is the discrete 2D
    'area', scaling ~ rho along the timelike cut line."""
    L = C.link_matrix(Cmat)
    rstar = coords[:, 1]
    obs = rstar <= rcut
    a, b = np.nonzero(L)
    cross = (obs[a] ^ obs[b])      # exactly one endpoint each side of the cut
    return int(np.count_nonzero(cross))


# --------------------------------------------------------------------------- #
# one (rho, l, R*_box) cell at one seed -> the per-seed scalars
# --------------------------------------------------------------------------- #
def run_seed(rho, l, Rbox, kap, seed, use_sparse):
    """Return a dict of per-seed scalars at this box edge for one seed:
    N_total, n_sub, S_full, S_trunc, horizon_links, pairing_residual_rel."""
    Vbox = 2.0 * T_HALF * l * np.tanh(Rbox / l)        # proper volume (caps)
    N = int(round(rho * Vbox))
    rng = np.random.default_rng(seed)
    coords = C.sprinkle_ds_static_patch2d(
        N, rng, l=l, rstar_box=Rbox, t_extent=T_HALF)
    sub = np.where(coords[:, 1] <= R_CUT)[0]
    comp = N - sub.size
    out = {"N_total": N, "n_sub": int(sub.size), "S_full": 0.0,
           "S_trunc": 0.0, "horizon_links": 0.0, "pairing_rel": 0.0}
    if sub.size < 6 or comp < 6:
        return out

    if not use_sparse:
        # DENSE float64 path: S_full (volume law) + S_trunc + exact A_mol.
        Cmat = C.causal_matrix(coords)
        iD = C.pauli_jordan(C.green_retarded_2d(Cmat))
        diag = C.causal_diagnostics(iD)
        out["pairing_rel"] = float(diag["pairing_residual_rel"])
        W = SJ.wightman(iD)
        out["S_trunc"] = abs(E.ssee(W, iD, sub, kappa=kap).value)
        out["S_full"] = abs(E.ssee(W, iD, sub, kappa=None).value)
        out["horizon_links"] = float(horizon_link_count(coords, Cmat, R_CUT))
    else:
        # SPARSE matrix-free path (toe v0.3.0): truncated channel only.
        # LOAD-BEARING (VYPOCET-24): the sparse builders take EXPLICIT null
        # coords (u, v) = (t - r*, t + r*); raw (t, r*) gives a wrong matrix.
        uv = cm.null_coords_from_t_rstar(coords)
        op, perm = C.idelta_operator_2d(uv, dtype=np.float32)
        # k > 2 * #{|lambda| > kappa}: the entropy-cutoff rank grows ~ sqrt(N)
        # (F-006), so 5*sqrt(N) (+/- paired) captures all |lambda| > kappa modes.
        k = max(96, 5 * int(np.ceil(np.sqrt(N))))
        k = int(min(k + (k % 2), N - 2))
        ss = SJ.sj_state_sparse(op, k, rng=rng, tol=1e-7)
        out["pairing_rel"] = cm.pairing_residual_rel_from_eigs(ss.eigvals)
        coords_s = coords[perm]                  # operator's point order
        sub_s = np.where(coords_s[:, 1] <= R_CUT)[0]
        out["n_sub"] = int(sub_s.size)
        out["S_trunc"] = abs(E.ssee_sparse(ss, sub_s, kappa=kap).value)
        # S_full + A_mol are intrinsically dense / O(N^2) -> NaN on the sparse
        # path (the primary R_full ratio is measured on the dense densities).
        out["S_full"] = float("nan")
        out["horizon_links"] = float("nan")
    return out


# --------------------------------------------------------------------------- #
# bootstrap cap over seeds (toe.fits-style; VYPOCET-23 cap_with_se)
# --------------------------------------------------------------------------- #
def cap_with_se(per_seed_curves, x, seed=20260606):
    """Saturating-fit cap with bootstrap SE/CI68 across seeds. per_seed_curves:
    (n_seeds, n_x). Returns (cap, se, ci68, r2)."""
    per = np.asarray(per_seed_curves, float)
    mean = per.mean(0)
    cap0, _, _, r2, _ = cm.saturating_fit(x, mean)
    rng = np.random.default_rng(seed)
    n_seeds = per.shape[0]
    caps = []
    for _ in range(1000):
        idx = rng.integers(0, n_seeds, n_seeds)
        c, _, _, _, _ = cm.saturating_fit(x, per[idx].mean(0))
        caps.append(c)
    caps = np.asarray(caps)
    se = float(caps.std(ddof=1)) if np.isfinite(caps).sum() > 1 else 0.0
    fin = caps[np.isfinite(caps)]
    ci68 = ((float(np.percentile(fin, 16)), float(np.percentile(fin, 84)))
            if fin.size else (float("nan"), float("nan")))
    return cap0, se, ci68, r2


# --------------------------------------------------------------------------- #
# DRIVER
# --------------------------------------------------------------------------- #
SMOKE_INVOCATION = (
    "SMOKE (< 30 s):\n"
    "  MPLBACKEND=Agg python3 compute/drivers/ds_entropy_cap_2d.py \\\n"
    "      --rho 120 --patch-l 1.0 --seeds 1 --max-hours 0.01\n"
    "  (one low-density dense cell; writes results.json with one complete cell,\n"
    "   the pairing invariant, host fingerprint and the R_full ratio.)\n\n"
    "FULL F-028 run (target):\n"
    "  MPLBACKEND=Agg python3 compute/drivers/ds_entropy_cap_2d.py \\\n"
    "      --rho 240,600,1200,3000,30000 --patch-l 0.7,1.0,1.5,2.5 \\\n"
    "      --seeds 6 --max-hours 5.5"
)


def main(argv=None):
    p = cm.make_argparser(
        "ds_entropy_cap_2d",
        "F-028: tighten the 2D dS entropy-cap / A_mol ratio R_full constancy "
        "(VYPOCET-23 protocol; rho up to 3e4, l up to 2.5, more seeds).",
        epilog=SMOKE_INVOCATION, rho=True, patch_l=True)
    args = p.parse_args(argv)

    rho_list = args.rho if args.rho else [240.0, 600.0, 1200.0]
    l_list = args.patch_l if args.patch_l else [1.0]
    n_seeds = int(args.seeds)

    params = {
        "rho": rho_list, "patch_l": l_list, "seeds": n_seeds,
        "max_hours": args.max_hours, "RSTAR_BOX": RSTAR_BOX.tolist(),
        "R_CUT": R_CUT, "T_HALF": T_HALF, "DENSE_N_MAX": DENSE_N_MAX,
        "anti_circularity": {
            "epsilon_law": "epsilon = rho^(-1/2) FIXED from F-006 BEFORE the ratio",
            "F006_p_rank": P_RANK, "F006_p_err": P_RANK_ERR,
            "F006_eps_exponent": EPS_EXPONENT,
        },
        "horizon_area_2D_convention": (
            "Dou-Sorkin gr-qc/0302009: 2D codim-2 horizon = point; discrete area "
            "= irreducible causal-link molecule count crossing the FIXED cut. "
            "A/eps^0 dimensionless. dS A/4 application '⚠️ neoveřeno' (GH primary "
            "absent); we report the dimensionless ratio R = S_cap / A_mol."),
        "toe_version": toe.__version__,
    }
    host = cm.host_fingerprint()
    slug = cm.param_slug({"rho": rho_list, "l": l_list, "s": [n_seeds]})
    run_dir, results_path, _plots = cm.make_run_dir(
        args.out, "ds_entropy_cap_2d", slug)
    ck = cm.Checkpointer(results_path, "ds_entropy_cap_2d", params, host)
    budget = cm.TimeBudget(args.max_hours)

    print(f"[ds_entropy_cap_2d] run dir: {run_dir}")
    print(f"[anti-circularity] F-006 p_rank={P_RANK:.4f}+/-{P_RANK_ERR:.4f} "
          f"=> epsilon=rho^(-1/2) FIXED")

    boxes = RSTAR_BOX
    n_x = len(boxes)
    stopped = False
    for rho in rho_list:
        for l in l_list:
            if budget.exceeded():
                print(f"[time-budget] {budget.elapsed:.1f}s >= "
                      f"{budget.max_seconds:.1f}s; stopping before (rho={rho}, l={l}).")
                stopped = True
                break

            # decide dense vs sparse for THIS cell from its largest N
            Vmax = 2.0 * T_HALF * l * np.tanh(boxes.max() / l)
            N_max_cell = int(round(rho * Vmax))
            use_sparse = N_max_cell > DENSE_N_MAX

            Strunc = np.zeros((n_seeds, n_x))
            Sfull = np.zeros((n_seeds, n_x))
            Ntot = np.zeros((n_seeds, n_x))
            nsub = np.zeros((n_seeds, n_x))
            hlink = np.zeros((n_seeds, n_x))
            pair_per_box = []
            Ns = []
            for j, Rbox in enumerate(boxes):
                kap = None
                pair_box = 0.0
                for s in range(n_seeds):
                    seed = 28_000_000 + 1000 * int(round(rho)) + 100 * j \
                        + 10 * int(round(10 * l)) + s
                    Vbox = 2.0 * T_HALF * l * np.tanh(Rbox / l)
                    N = int(round(rho * Vbox))
                    kap = E.kappa_2d(N)
                    res = run_seed(rho, l, Rbox, kap, seed, use_sparse)
                    Ntot[s, j] = res["N_total"]
                    Strunc[s, j] = res["S_trunc"]
                    Sfull[s, j] = res["S_full"]
                    nsub[s, j] = res["n_sub"]
                    hlink[s, j] = res["horizon_links"]
                    pair_box = max(pair_box, res["pairing_rel"])
                Ns.append(N)
                pair_per_box.append(pair_box)
                print(f"   rho={rho:g} l={l:g} R*={Rbox:.1f} N={N:5d} "
                      f"kap={kap:.3f} S_trunc={Strunc[:, j].mean():.4f} "
                      f"S_full={Sfull[:, j].mean():.2f} "
                      f"hlinks={hlink[:, j].mean():.1f} pair={pair_box:.1e} "
                      f"[{'sparse' if use_sparse else 'dense'}]")

            # ASSERT +/- pairing invariant per region (path-aware tolerance)
            max_pair = max(pair_per_box) if pair_per_box else 0.0
            pair_tol = 5e-9 if use_sparse else 1e-12
            assert max_pair < pair_tol, (
                f"pairing invariant VIOLATED at rho={rho} l={l}: "
                f"{max_pair:.2e} >= {pair_tol:.0e}")

            # caps with bootstrap SE/CI68
            Sf_cap, Sf_se, Sf_ci, Sf_r2 = cap_with_se(Sfull, boxes)
            St_cap, St_se, St_ci, St_r2 = cap_with_se(Strunc, boxes)
            Nt_cap, Nt_se, Nt_ci, Nt_r2 = cap_with_se(Ntot, boxes)
            # horizon molecule plateau over the last 3 boxes
            hl_plateau = hlink[:, -3:]
            A_mol = float(np.nanmean(hl_plateau)) if np.isfinite(hl_plateau).any() \
                else float("nan")
            eps = epsilon_of_rho(rho)
            A_cont = A_mol * eps ** 2 if np.isfinite(A_mol) else float("nan")
            R_full = (Sf_cap / A_mol) if (np.isfinite(A_mol) and A_mol > 0) \
                else float("nan")
            R_trunc_cont = (St_cap / A_cont) if (np.isfinite(A_cont) and A_cont > 0) \
                else float("nan")
            implied_c = (1.0 / R_full) if (np.isfinite(R_full) and R_full) \
                else float("nan")

            cell = {
                "rho": rho, "l": l, "path": "sparse" if use_sparse else "dense",
                "Ns": Ns, "RSTAR_BOX": boxes.tolist(), "n_seeds": n_seeds,
                "N_total_mean": Ntot.mean(0).tolist(),
                "S_full_mean": Sfull.mean(0).tolist(),
                "S_trunc_mean": Strunc.mean(0).tolist(),
                "n_sub_mean": nsub.mean(0).tolist(),
                "horizon_links_mean": hlink.mean(0).tolist(),
                "N_total_cap": Nt_cap, "N_total_cap_se": Nt_se,
                "N_total_cap_ci68": list(Nt_ci), "N_total_cap_R2": Nt_r2,
                "S_full_cap": Sf_cap, "S_full_cap_se": Sf_se,
                "S_full_cap_ci68": list(Sf_ci), "S_full_cap_R2": Sf_r2,
                "S_trunc_cap": St_cap, "S_trunc_cap_se": St_se,
                "S_trunc_cap_ci68": list(St_ci), "S_trunc_cap_R2": St_r2,
                "horizon_links_cap_Amol": A_mol,
                "epsilon": eps, "A_cont_eps_units": A_cont,
                "R_Sfull_over_Amol": R_full,
                "R_Strunc_over_Acont": R_trunc_cont,
                "implied_coefficient_c": implied_c,
                "pairing_residual_rel_max": max_pair,
                "pairing_tol": pair_tol,
            }
            ck.add_cell(cell)
            _update_summary(ck)
            ck.write()
            print(f"   => R_full(S_full/A_mol)={R_full:.4f} "
                  f"implied_c={implied_c:.2f} (pair_max={max_pair:.1e})")
        if stopped:
            break

    _update_summary(ck)
    status = "partial-time-budget" if stopped else "complete"
    ck.finalize(status)
    summ = ck.summary
    print(f"\n[ds_entropy_cap_2d] status={status} n_cells={len(ck.cells)}")
    print(f"  R_full mean={summ.get('R_full_mean')!r} "
          f"CV={summ.get('R_full_cv')!r} implied_c={summ.get('implied_c_mean')!r}")
    print(f"  wrote {results_path}")
    return 0


def _update_summary(ck):
    """Recompute the cross-cell R_full constancy summary from the committed
    cells (the F-028 discriminator)."""
    R = np.array([c.get("R_Sfull_over_Amol") for c in ck.cells], float)
    R = R[np.isfinite(R)]
    rho_vals = np.array([c["rho"] for c in ck.cells if
                         np.isfinite(c.get("R_Sfull_over_Amol", np.nan))], float)
    summary = {
        "n_cells": len(ck.cells),
        "n_dense_cells": int(sum(c["path"] == "dense" for c in ck.cells)),
        "n_sparse_cells": int(sum(c["path"] == "sparse" for c in ck.cells)),
    }
    if R.size:
        summary["R_full_mean"] = float(R.mean())
        summary["R_full_std"] = float(R.std(ddof=1)) if R.size > 1 else 0.0
        summary["R_full_cv"] = (float(R.std(ddof=1) / abs(R.mean()))
                                if R.size > 1 and R.mean() else 0.0)
        summary["R_full_min"] = float(R.min())
        summary["R_full_max"] = float(R.max())
        summary["implied_c_mean"] = float(1.0 / R.mean()) if R.mean() else None
        summary["R_full_constant"] = bool(summary["R_full_cv"] < 0.05)
        # log-log drift d ln R / d ln rho over the dense cells
        if rho_vals.size >= 3 and np.all(rho_vals > 0) and np.all(R > 0):
            from toe.fits import regression_se
            sl, _ic, se = regression_se(rho_vals, R)
            summary["R_full_drift_vs_rho"] = float(sl)
            summary["R_full_drift_se"] = float(se)
    else:
        summary["R_full_mean"] = None
        summary["note"] = "no dense cell -> R_full undefined (sparse-only run)"
    ck.summary = summary


if __name__ == "__main__":
    raise SystemExit(main())
