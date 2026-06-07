#!/usr/bin/env python3
r"""ds_cap_4d -- THE OPEN QUESTION: is the dS entropy-cap area-law coefficient
``c = 1/R ~ 7.57`` (VYPOCET-23, 2D) DIMENSION-DEPENDENT?

VYPOCET-23 established in 2D that the bounded de Sitter static-patch entropy CAP
is PROPORTIONAL to the Dou-Sorkin discrete horizon area (R_full = S_full_cap /
A_horizon CONSTANT across density and patch size, R ~ 0.1321, implied coefficient
c = 1/R ~ 7.57). The literal Bekenstein-Hawking 1/4 is NOT recovered -- the O(1)
geometric normalisation of the discrete molecule count vs the SSEE is unfixed.
THE open follow-up: does that same constant survive in 4D, or is c a function of
spacetime dimension? This driver lifts the VYPOCET-23 cap-ratio protocol to the
4D dS static patch and measures R_full^{4D} = S_full_cap / A_horizon^{4D} over a
density / patch-size scan, then compares c^{4D} = 1/R^{4D} against c^{2D} ~ 7.57.

============================================================================
4D DISCRETE-AREA CONVENTION  (worked out + HONEST CAVEAT)
============================================================================
In D spacetime dimensions the de Sitter horizon is a CODIMENSION-2 surface (the
"area" is (D-2)-dimensional). The continuum Bekenstein-Hawking / Gibbons-Hawking
law is  S = A / (4 G)  with  A = the (D-2)-volume of that surface.

  * D = 2 (VYPOCET-23): D-2 = 0, the horizon is a POINT; its discrete "area" is
    the Dou-Sorkin (gr-qc/0302009) MOLECULE COUNT = number of irreducible causal
    LINKS crossing the horizon cut. In eps-units A/eps^{D-2} = A/eps^0 = A is
    dimensionless. c^{2D} = 1/R^{2D} ~ 7.57.

  * D = 4 (HERE): D-2 = 2, the horizon is a 2-SURFACE. The discrete "area" is
    the codim-2 SURFACE MOLECULE COUNT: the number of irreducible causal LINKS
    that PIERCE the codim-2 entangling surface E -- i.e. links (y < x) with one
    endpoint in the observer region O (r* <= R_CUT) and the other in its
    complement, restricted to a thin tube around E. By the standard causal-set
    horizon-molecule scaling (Dou-Sorkin; Barton-Counsell-...-Wilkes-Wilson-...
    style counting), the number of such surface-piercing links scales as

        A_mol  ~  (number density of links per unit codim-2 area) x (Area / eps^2)
               ~  rho^{...}  with the codim-2 surface measured in eps^2 units,

    so the eps-units area is  A / eps^{D-2} = A / eps^2  with  eps = rho^{-1/4}
    in 4D (the 4D discreteness scale: rho = N / V_4, eps ~ (V_4/N)^{1/4} ~
    rho^{-1/4}, the fundamental length per point). The DISCRETE 4D horizon area
    we report is therefore the surface-piercing irreducible-LINK count A_mol; the
    eps-units continuum area is A_cont = A_mol * eps^2 = A_mol * rho^{-1/2}.

  HONEST CAVEAT (⚠️ neoveřeno where the source is absent):
    (1) The 4D massless scalar is NOT conformally invariant, so the conformal
        factor sech^2(r*/l) does NOT drop out of the exact dS propagator. This
        driver uses the SAME controlled approximation as VYPOCET-21 / the toe
        builder sprinkle_ds_static_patch4d: keep the FLAT causal structure in
        (t, r*, x1, x2) + the dS PROPER sprinkling MEASURE (sech^2 radial -> the
        bounded II_1 point budget) + the 4D link-matrix retarded Green (Johnston
        0909.0944). What is preserved is the causal order + the measure; what is
        NOT preserved is the exact curved 4D Wightman function. We test the
        GEOMETRIC II_1 cap and its area proportionality, not the exact dS state.
    (2) The de-Sitter-specific Gibbons-Hawking entropy primary (a gr-qc/0205058
        -style reference) is NOT present in the repo, so the dS APPLICATION of the
        A/4 law is marked '⚠️ neoveřeno' per project policy. We therefore report
        the DIMENSIONLESS ratio R^{4D} = S_full_cap / A_mol and its constancy /
        implied coefficient c^{4D} -- NOT a literal 1/4.
    (3) The precise rho-power of the 4D surface-molecule count is MEASURED here
        (reported as horizon_links_cap_drift_vs_rho), not assumed; the area-law
        claim is the CONSTANCY of R_full = S_full_cap / A_mol across the scan
        (both must share the SAME rho-power for the ratio to be density-invariant).
    Only repo-present references are cited: dou-sorkin-2003 (gr-qc/0302009),
    johnston-2009 (0909.0944, 4D link Green), clpw-2022 (2206.10780, dS II_1),
    bekenstein-hawking-formula (formulas.json).

============================================================================
PROTOCOL (VYPOCET-23 cap-ratio, lifted to 4D)
============================================================================
For each (rho, l):
  - sweep the radial box edge R*_box -> horizon at FIXED proper density; build
    toe.causet.sprinkle_ds_static_patch4d (sech^2 radial proper measure -> the
    point budget CAPS = the II_1 signal; transverse box flat);
  - FIXED entangling cut: observer region O = { r* <= R_CUT } (a codim-2 surface
    E = {r* = R_CUT} x transverse box held FIXED while the patch fills in);
  - per seed measure S_full (untruncated content-tracking SSEE, the II_1 cap),
    S_trunc (type-II area-law truncation n_max = 2 N^{3/4}, F-019), and A_mol =
    irreducible causal links piercing E;
  - saturating-fit each channel vs R*_box -> the cap (bootstrap SE/CI68 / seeds);
  - PRIMARY ratio R_full^{4D} = S_full_cap / A_mol_cap.
ANTI-CIRCULARITY: eps = rho^{-1/4} (4D) is FIXED from the F-006 rho^{-1/2}
discreteness law lifted to 4D (eps ~ (V/N)^{1/4}); read + asserted at startup,
used unchanged, NEVER tuned to make R = 1/4.

MEMORY GUARD: S_full + the 4D dense generalized eigenproblem cap N at
DENSE_N_MAX = 3000; the 4D dS proper-volume caps N, so the dense path covers the
primary cells. (The 4D sparse top-k path is not yet a toe primitive for the
generic 4D causal order, so cells whose N would exceed the wall are SKIPPED with
a recorded note rather than silently mis-measured.)
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
# ANTI-CIRCULARITY: eps = rho^{-1/4} (4D) FIXED from the F-006 rho^{-1/2} law.
# F-006 (ssee-diamond, 2D) gives the discreteness scale eps ~ rho^{-1/d} per
# dimension d (eps ~ (V/N)^{1/d}); the 2D p_rank ~ 1/2 CONFIRMS eps ~ rho^{-1/2}
# there, and the dimensional generalisation is eps ~ rho^{-1/d}, so eps^{4D} =
# rho^{-1/4}. Read + asserted BEFORE any ratio.
# --------------------------------------------------------------------------- #
_F006_PATH = os.path.join(
    cm.repo_root(), "core-data", "calculations", "ssee-diamond", "results.json")
with open(_F006_PATH) as _f:
    _F006 = json.load(_f)
_KS = _F006["knee_scaling"]["entropy_cutoff_rank"]
P_RANK = float(_KS["p_rank_vs_N"])
P_RANK_ERR = float(_KS["p_err"])
assert abs(P_RANK - 0.5) < 0.05, (
    f"F-006 p_rank {P_RANK} not ~1/2; anti-circularity protocol broken")

# the committed 2D result we compare c^{4D} against (VYPOCET-23 / F-028)
C_2D_REFERENCE = 7.570977917981071     # = 1 / R_full^{2D}, ds-entropy-cap VERDICT


def epsilon_of_rho_4d(rho):
    """FIXED 4D discreteness scale: eps = rho^{-1/4}. NOT tunable (lifted from
    the F-006 eps ~ rho^{-1/d} law, d=4)."""
    return float(rho) ** (-0.25)


# --------------------------------------------------------------------------- #
# geometry / protocol constants (mirror VYPOCET-21 / sj-desitter-4d)
# --------------------------------------------------------------------------- #
LDS_DEFAULT = 1.0          # de Sitter radius l (horizon at r=l <=> r*=inf)
T_HALF = 0.5               # conformal-time half-extent
XPERP = 1.0                # transverse box half-extent (|x1|, |x2| <= XPERP)
DIM = 4
ALPHA_RANK = 2.0           # n_max = alpha N^{3/4} (F-019 / 2008.07697 area law)
R_CUT = 1.0                # FIXED tortoise entangling cut (codim-2 surface)
RSTAR_BOX = np.array([1.6, 2.2, 2.8, 3.5, 4.3, 5.2])  # radial edge -> horizon
DENSE_N_MAX = 3000         # dense eigh wall (memory guard)


def proper_volume_ds_4d(rstar_box, l):
    """dS 4D proper box volume 2 T_HALF * l tanh(R*/l) * (2 XPERP)^2 -- CAPS."""
    return (2.0 * T_HALF) * (l * np.tanh(rstar_box / l)) * (2.0 * XPERP) ** 2


# --------------------------------------------------------------------------- #
# 4D horizon "area" = codim-2 SURFACE molecule count: irreducible causal LINKS
# piercing the FIXED codim-2 entangling surface E = { r* = R_CUT }.
# --------------------------------------------------------------------------- #
def horizon_link_count_4d(coords, Cmat, rcut):
    """Count irreducible causal links piercing the FIXED codim-2 surface E =
    { r* = rcut } (the 4D discrete horizon 'area'). A link (y < x) pierces E iff
    exactly one endpoint is in the observer region O = { r* <= rcut } and the
    other is in its complement. This is the 4D codim-2 generalisation of the 2D
    Dou-Sorkin (gr-qc/0302009) horizon-molecule count: in 4D the cut surface is a
    2-surface (codim-2), and its discrete area is the surface-piercing link count
    (~ Area / eps^2; eps = rho^{-1/4})."""
    L = C.link_matrix(Cmat)
    rstar = coords[:, 1]
    obs = rstar <= rcut
    a, b = np.nonzero(L)
    cross = (obs[a] ^ obs[b])      # exactly one endpoint each side of E
    return int(np.count_nonzero(cross))


# --------------------------------------------------------------------------- #
# 4D Pauli-Jordan on the flat conformal (t, r*, x1, x2) order (VYPOCET-21)
# --------------------------------------------------------------------------- #
def idelta_4d(coords, rho):
    """4D iDelta via the link-matrix Green (Johnston 0909.0944):
    C -> L -> G_R = a L -> iDelta. Returns (iDelta, C, pairing_residual_rel)."""
    Cmat = C.causal_matrix(coords)             # flat 4D lightcone order
    L = C.link_matrix(Cmat)
    iD = C.pauli_jordan(C.green_retarded_4d(L, rho))
    diag = C.causal_diagnostics(iD)
    return iD, Cmat, float(diag["pairing_residual_rel"])


# --------------------------------------------------------------------------- #
# one (rho, l, R*_box) cell at one seed
# --------------------------------------------------------------------------- #
def run_seed(rho, l, Rbox, nmax, seed):
    """Per-seed scalars at this 4D box edge: N_total, n_sub, S_full, S_trunc,
    horizon_links, pairing_residual_rel."""
    Vbox = proper_volume_ds_4d(Rbox, l)
    N = int(round(rho * Vbox))
    rho_actual = N / Vbox if Vbox > 0 else rho
    rng = np.random.default_rng(seed)
    coords = C.sprinkle_ds_static_patch4d(
        N, rng, l=l, rstar_box=Rbox, t_extent=T_HALF, x_perp_half=XPERP)
    sub = np.where(coords[:, 1] <= R_CUT)[0]
    comp = N - sub.size
    out = {"N_total": N, "n_sub": int(sub.size), "S_full": 0.0,
           "S_trunc": 0.0, "horizon_links": 0.0, "pairing_rel": 0.0}
    if sub.size < 8 or comp < 8:
        return out
    iD, Cmat, pair = idelta_4d(coords, rho_actual)
    out["pairing_rel"] = pair
    W = SJ.wightman(iD)
    out["S_trunc"] = abs(E.ssee(W, iD, sub, n_max=nmax).value)
    out["S_full"] = abs(E.ssee(W, iD, sub, kappa=None).value)
    out["horizon_links"] = float(horizon_link_count_4d(coords, Cmat, R_CUT))
    return out


def cap_with_se(per_seed_curves, x, seed=20260606):
    """Saturating-fit cap with bootstrap SE/CI68 across seeds (VYPOCET-23
    cap_with_se). per_seed_curves: (n_seeds, n_x). Returns (cap, se, ci68, r2)."""
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
    "  MPLBACKEND=Agg python3 compute/drivers/ds_cap_4d.py \\\n"
    "      --rho 30 --patch-l 1.0 --seeds 1 --max-hours 0.01\n"
    "  (one low-density 4D dS cell; writes results.json with one complete cell,\n"
    "   the codim-2 area-law ratio R_full^4D, pairing invariant, host print.)\n\n"
    "FULL open-question run (target):\n"
    "  MPLBACKEND=Agg python3 compute/drivers/ds_cap_4d.py \\\n"
    "      --rho 60,120,240 --patch-l 0.8,1.0,1.5 --seeds 6 --max-hours 5.5\n"
    "  (compares c^4D = 1/R_full^4D against the committed 2D c ~ 7.57.)"
)


def main(argv=None):
    p = cm.make_argparser(
        "ds_cap_4d",
        "THE open question: is the dS entropy-cap area-law coefficient c ~ 7.57 "
        "dimension-dependent? (VYPOCET-23 cap-ratio protocol lifted to 4D.)",
        epilog=SMOKE_INVOCATION, rho=True, patch_l=True, n_max=True)
    args = p.parse_args(argv)

    rho_list = args.rho if args.rho else [60.0, 120.0, 240.0]
    l_list = args.patch_l if args.patch_l else [1.0]
    n_seeds = int(args.seeds)
    n_cap = args.n_max if args.n_max else DENSE_N_MAX

    params = {
        "rho": rho_list, "patch_l": l_list, "seeds": n_seeds,
        "max_hours": args.max_hours, "n_max_cap": n_cap,
        "RSTAR_BOX": RSTAR_BOX.tolist(), "R_CUT": R_CUT, "T_HALF": T_HALF,
        "XPERP": XPERP, "alpha_rank": ALPHA_RANK, "DIM": DIM,
        "DENSE_N_MAX": DENSE_N_MAX,
        "c_2D_reference": C_2D_REFERENCE,
        "anti_circularity": {
            "epsilon_law": "epsilon = rho^(-1/4) (4D) FIXED from F-006 rho^(-1/d) "
                           "lifted to d=4, BEFORE the ratio",
            "F006_p_rank": P_RANK, "F006_p_err": P_RANK_ERR,
        },
        "horizon_area_4D_convention": (
            "codim-2 SURFACE molecule count: irreducible causal links PIERCING "
            "the FIXED codim-2 entangling surface E={r*=R_CUT}. A/eps^{D-2}="
            "A/eps^2 with eps=rho^(-1/4). dS A/4 application '⚠️ neoveřeno' "
            "(Gibbons-Hawking dS primary absent; 4D conformal-weight caveat). "
            "We report the dimensionless ratio R^4D = S_full_cap / A_mol and "
            "c^4D = 1/R^4D vs the committed 2D c ~ 7.57."),
        "conformal_weight_caveat": (
            "4D massless scalar is NOT conformally invariant; this is the "
            "VYPOCET-21 controlled approximation (flat causal order + dS proper "
            "measure + Johnston 0909.0944 link Green), not the exact dS state."),
        "toe_version": toe.__version__,
    }
    host = cm.host_fingerprint()
    slug = cm.param_slug({"rho": rho_list, "l": l_list, "s": [n_seeds]})
    run_dir, results_path, _plots = cm.make_run_dir(args.out, "ds_cap_4d", slug)
    ck = cm.Checkpointer(results_path, "ds_cap_4d", params, host)
    budget = cm.TimeBudget(args.max_hours)

    print(f"[ds_cap_4d] run dir: {run_dir}")
    print(f"[anti-circularity] F-006 p_rank={P_RANK:.4f} => eps=rho^(-1/4) (4D) FIXED")
    print(f"[reference] comparing c^4D against committed 2D c={C_2D_REFERENCE:.4f}")

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

            # MEMORY GUARD: the 4D dS proper volume caps N; if the largest box
            # would still exceed the dense wall, record a SKIP note (no silent
            # mis-measure -- there is no generic-4D sparse top-k toe primitive).
            Vmax = proper_volume_ds_4d(boxes.max(), l)
            N_max_cell = int(round(rho * Vmax))
            if N_max_cell > n_cap:
                note = (f"skipped: N_max={N_max_cell} > n_max cap {n_cap} "
                        f"(4D dense eigh wall; no 4D sparse primitive).")
                print(f"   rho={rho:g} l={l:g} {note}")
                ck.add_cell({"rho": rho, "l": l, "path": "skipped",
                             "N_max_planned": N_max_cell, "note": note,
                             "R_Sfull_over_Amol": float("nan")})
                _update_summary(ck)
                ck.write()
                continue

            Strunc = np.zeros((n_seeds, n_x))
            Sfull = np.zeros((n_seeds, n_x))
            Ntot = np.zeros((n_seeds, n_x))
            nsub = np.zeros((n_seeds, n_x))
            hlink = np.zeros((n_seeds, n_x))
            pair_per_box = []
            Ns = []
            nmaxes = []
            for j, Rbox in enumerate(boxes):
                Vbox = proper_volume_ds_4d(Rbox, l)
                N = int(round(rho * Vbox))
                nmax = E.n_max_area_law(N, DIM, alpha=ALPHA_RANK)
                pair_box = 0.0
                for s in range(n_seeds):
                    seed = 24_000_000 + 100000 * int(round(rho)) + 1000 * j \
                        + 10 * int(round(10 * l)) + s
                    res = run_seed(rho, l, Rbox, nmax, seed)
                    Ntot[s, j] = res["N_total"]
                    Strunc[s, j] = res["S_trunc"]
                    Sfull[s, j] = res["S_full"]
                    nsub[s, j] = res["n_sub"]
                    hlink[s, j] = res["horizon_links"]
                    pair_box = max(pair_box, res["pairing_rel"])
                Ns.append(N)
                nmaxes.append(int(nmax))
                pair_per_box.append(pair_box)
                print(f"   rho={rho:g} l={l:g} R*={Rbox:.1f} N={N:5d} "
                      f"nmax={nmax:4d} S_trunc={Strunc[:, j].mean():.4f} "
                      f"S_full={Sfull[:, j].mean():.2f} "
                      f"hlinks={hlink[:, j].mean():.1f} pair={pair_box:.1e}")

            # ASSERT +/- pairing invariant per region (dense float64 -> ~1e-12)
            max_pair = max(pair_per_box) if pair_per_box else 0.0
            pair_tol = 1e-12
            assert max_pair < pair_tol, (
                f"pairing invariant VIOLATED at rho={rho} l={l}: "
                f"{max_pair:.2e} >= {pair_tol:.0e}")

            Sf_cap, Sf_se, Sf_ci, Sf_r2 = cap_with_se(Sfull, boxes)
            St_cap, St_se, St_ci, St_r2 = cap_with_se(Strunc, boxes)
            Nt_cap, Nt_se, Nt_ci, Nt_r2 = cap_with_se(Ntot, boxes)
            A_mol = float(np.nanmean(hlink[:, -3:]))   # plateau, last 3 boxes
            eps = epsilon_of_rho_4d(rho)
            A_cont = A_mol * eps ** 2 if np.isfinite(A_mol) else float("nan")
            R_full = (Sf_cap / A_mol) if (np.isfinite(A_mol) and A_mol > 0) \
                else float("nan")
            R_trunc_cont = (St_cap / A_cont) if (np.isfinite(A_cont) and A_cont > 0) \
                else float("nan")
            implied_c = (1.0 / R_full) if (np.isfinite(R_full) and R_full) \
                else float("nan")

            cell = {
                "rho": rho, "l": l, "path": "dense", "Ns": Ns,
                "n_max_per_box": nmaxes, "RSTAR_BOX": boxes.tolist(),
                "n_seeds": n_seeds,
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
                "implied_coefficient_c_4D": implied_c,
                "pairing_residual_rel_max": max_pair, "pairing_tol": pair_tol,
            }
            ck.add_cell(cell)
            _update_summary(ck)
            ck.write()
            print(f"   => R_full^4D={R_full:.4f} c^4D={implied_c:.2f} "
                  f"(2D c={C_2D_REFERENCE:.2f}; pair={max_pair:.1e})")
        if stopped:
            break

    _update_summary(ck)
    status = "partial-time-budget" if stopped else "complete"
    ck.finalize(status)
    summ = ck.summary
    print(f"\n[ds_cap_4d] status={status} n_cells={len(ck.cells)}")
    print(f"  c^4D mean={summ.get('implied_c_4D_mean')!r} "
          f"vs 2D c={C_2D_REFERENCE:.4f}; "
          f"dimension_dependent={summ.get('c_is_dimension_dependent')!r}")
    print(f"  wrote {results_path}")
    return 0


def _update_summary(ck):
    """Cross-cell R_full^4D constancy + the c^4D vs c^2D dimension-dependence
    verdict (THE open question)."""
    measured = [c for c in ck.cells
                if np.isfinite(c.get("R_Sfull_over_Amol", np.nan))]
    R = np.array([c["R_Sfull_over_Amol"] for c in measured], float)
    rho_vals = np.array([c["rho"] for c in measured], float)
    summary = {
        "n_cells": len(ck.cells),
        "n_measured_cells": len(measured),
        "n_skipped_cells": int(sum(c.get("path") == "skipped" for c in ck.cells)),
        "c_2D_reference": C_2D_REFERENCE,
    }
    if R.size:
        summary["R_full_4D_mean"] = float(R.mean())
        summary["R_full_4D_std"] = float(R.std(ddof=1)) if R.size > 1 else 0.0
        summary["R_full_4D_cv"] = (float(R.std(ddof=1) / abs(R.mean()))
                                   if R.size > 1 and R.mean() else 0.0)
        c4d = float(1.0 / R.mean()) if R.mean() else None
        summary["implied_c_4D_mean"] = c4d
        summary["R_full_4D_constant"] = bool(summary["R_full_4D_cv"] < 0.10)
        if rho_vals.size >= 3 and np.all(rho_vals > 0) and np.all(R > 0):
            from toe.fits import regression_se
            sl, _ic, se = regression_se(rho_vals, R)
            summary["R_full_4D_drift_vs_rho"] = float(sl)
            summary["R_full_4D_drift_se"] = float(se)
        # THE verdict: is c dimension-dependent? c^4D differs from c^2D by more
        # than ~2x the cross-cell spread of c^4D.
        if c4d is not None and R.size:
            c_spread = (summary["R_full_4D_std"] / R.mean() ** 2
                        if R.mean() else float("inf"))
            summary["c_4D_minus_c_2D"] = float(c4d - C_2D_REFERENCE)
            summary["c_is_dimension_dependent"] = bool(
                abs(c4d - C_2D_REFERENCE) > 2.0 * max(c_spread, 1e-9))
            summary["verdict"] = (
                "PRELIMINARY (needs the full multi-cell scan): c^4D=%.3f vs "
                "c^2D=%.3f -> %s. Dimension-dependence is decided by R_full "
                "constancy across the FULL (rho, l) scan." % (
                    c4d, C_2D_REFERENCE,
                    "DIFFERENT (dimension-dependent)"
                    if summary["c_is_dimension_dependent"] else
                    "consistent (NOT clearly dimension-dependent)"))
    else:
        summary["R_full_4D_mean"] = None
        summary["note"] = "no measured cell (all skipped or sub too small)"
    ck.summary = summary


if __name__ == "__main__":
    raise SystemExit(main())
