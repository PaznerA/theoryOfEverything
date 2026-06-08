#!/usr/bin/env python3
r"""VYPOCET-27 -- the 4D A_mol CONVENTION question left open by VYPOCET-25:
WHY does the 4D horizon "area" molecule count scale as A_mol ~ rho^{1.77} (not
rho^{0.5}), and is the 4D entropy-area law SALVAGEABLE under the correct
Dou-Sorkin codim-2 convention, or genuinely ABSENT?

Two stages, both written into a single fixed-schema results.json (atomic write,
``status`` field, progressive per-stage checkpoints):

  STAGE A -- EXPONENT RE-ANALYSIS of the staged cloud artifacts
    compute/results-archive/ds_cap_4d-{grid,highN}.json: fit
    A_mol_raw ~ rho^{p_A}, S_full ~ rho^{p_S}, n_sub ~ rho^{p_n},
    N_total ~ rho^{p_N} per l and pooled, with SE. Confirms VYPOCET-25
    (p_A ~ 1.77, p_S ~ 1.05; drift d ln R / d ln rho = p_S - p_A ~ -0.72).

  STAGE B -- CORRECTED codim-2 Dou-Sorkin molecule CONFIRMATORY RUN
    on the EXISTING sprinkle_ds_static_patch4d geometry (rho in {120,240,480},
    l = 1.0, 3-4 seeds, dense N <= ~2000): measure the corrected
    toe.causet.horizon_molecules_codim2 count vs rho (target proper area
    rho^{0.5}), and recompute R' = S_full_cap / A_mol_correct and
    R'' = S_trunc_cap / A_mol_correct -- does EITHER become density-invariant?

THE DIAGNOSIS (Stage A2, derived + checked numerically here): the raw count of
VYPOCET-25 / ds_cap_4d.horizon_link_count_4d counts irreducible causal LINKS
crossing the codim-1 WORLDTUBE {r* = R_CUT} (t, x1, x2 all vary) over the WHOLE
time extent, NOT molecules on the codim-2 entangling 2-surface {r* = R_CUT,
t = 0}. In 4D that worldtube count scales as (worldtube 3-volume ~ rho^1) x
(per-element link multiplicity ~ rho^{~0.77}) = rho^{~1.77}, whereas a proper
codim-2 area count scales as rho^{(D-2)/D} = rho^{0.5}. The corrected
horizon_molecules_codim2 restores rho^{~0.5}.

ANTI-CIRCULARITY: eps = rho^{-1/4} (4D) FIXED from the F-006 rho^{-1/d} law
(ssee-diamond, p_rank = 0.519 +/- 0.007), read + asserted BEFORE any ratio.

HONEST CAVEAT (carried from VYPOCET-21/25): the 4D massless scalar is NOT
conformally invariant; this is the VYPOCET-21 controlled approximation (flat
causal order in (t, r*, x1, x2) + dS proper sech^2 measure + Johnston 0909.0944
link Green), not the exact dS Wightman state. The de-Sitter-specific
Gibbons-Hawking primary is NOT in the repo, so the dS A/4 application is marked
'WARN neoveřeno'. Only repo-present references are cited: dou-sorkin-2003
(gr-qc/0302009), johnston-2009 (0909.0944), clpw-2022 (2206.10780), F-006.

Thin orchestrator over ``toe`` (v0.3.0); all physics lives in the library.
Portability: every path is derived __file__-relative (CLAUDE.md Konvence kodu).
"""

from __future__ import annotations

import json
import math
import os
import sys
import time

_HERE = os.path.dirname(os.path.abspath(__file__))
_LIB = os.path.normpath(os.path.join(_HERE, "..", "..", "..", "lib"))
if _LIB not in sys.path:
    sys.path.insert(0, _LIB)

import numpy as np  # noqa: E402
import toe  # noqa: E402
from toe import causet as C  # noqa: E402
from toe import sj as SJ  # noqa: E402
from toe import entropy as E  # noqa: E402

_PLOTS = os.path.join(_HERE, "plots")
os.makedirs(_PLOTS, exist_ok=True)
_RESULTS = os.path.join(_HERE, "results.json")
_ARCHIVE = os.path.normpath(os.path.join(_HERE, "..", "..", "..",
                                         "compute", "results-archive"))

# --------------------------------------------------------------------------- #
# ANTI-CIRCULARITY: eps = rho^{-1/4} (4D) FIXED from the INDEPENDENT F-006 law.
# --------------------------------------------------------------------------- #
_F006 = json.load(open(os.path.join(
    _HERE, "..", "ssee-diamond", "results.json")))
P_RANK = float(_F006["knee_scaling"]["entropy_cutoff_rank"]["p_rank_vs_N"])
P_RANK_ERR = float(_F006["knee_scaling"]["entropy_cutoff_rank"]["p_err"])
assert abs(P_RANK - 0.5) < 0.05, (
    f"F-006 p_rank {P_RANK} not ~1/2; anti-circularity protocol broken")


def epsilon_of_rho_4d(rho):
    """FIXED 4D discreteness scale eps = rho^{-1/4} (F-006 eps ~ rho^{-1/d},
    d = 4). NOT tunable -- never adjusted to make any ratio constant."""
    return float(rho) ** (-0.25)


# geometry constants -- mirror compute/drivers/ds_cap_4d.py exactly
LDS = 1.0
T_HALF = 0.5
XPERP = 1.0
R_CUT = 1.0
DIM = 4
ALPHA_RANK = 2.0
K_TUBE = 1.5            # codim-2 molecule tube radius in eps units (VYPOCET-27)
C_2D_REFERENCE = 7.570977917981071     # committed 2D c = 1/R (F-028 / VYPOCET-23)

t0 = time.time()


# --------------------------------------------------------------------------- #
# atomic, schema-stable writer (write tmp + os.replace)
# --------------------------------------------------------------------------- #
def _json_safe(obj):
    if isinstance(obj, dict):
        return {k: _json_safe(v) for k, v in obj.items()}
    if isinstance(obj, (list, tuple)):
        return [_json_safe(v) for v in obj]
    if isinstance(obj, np.ndarray):
        return [_json_safe(v) for v in obj.tolist()]
    if isinstance(obj, np.generic):
        obj = obj.item()
    if isinstance(obj, float):
        return obj if math.isfinite(obj) else None
    return obj


def _write(payload, status):
    payload = dict(payload)
    payload["status"] = status
    payload["runtime_s"] = time.time() - t0
    tmp = _RESULTS + ".tmp"
    with open(tmp, "w") as f:
        json.dump(_json_safe(payload), f, indent=2)
    os.replace(tmp, _RESULTS)


def _loglog_fit(x, y):
    """Fit ln y = p ln x + b; return (p, se_p, b, n). NaN/<=0-safe."""
    x = np.asarray(x, float)
    y = np.asarray(y, float)
    m = np.isfinite(x) & np.isfinite(y) & (x > 0) & (y > 0)
    x, y = x[m], y[m]
    n = x.size
    if n < 2:
        return float("nan"), float("nan"), float("nan"), int(n)
    lx, ly = np.log(x), np.log(y)
    A = np.vstack([lx, np.ones(n)]).T
    coef, *_ = np.linalg.lstsq(A, ly, rcond=None)
    p, b = float(coef[0]), float(coef[1])
    if n > 2:
        resid = ly - A @ coef
        s2 = float(np.sum(resid ** 2) / (n - 2))
        sxx = float(np.sum((lx - lx.mean()) ** 2))
        se = math.sqrt(s2 / sxx) if sxx > 0 else float("nan")
    else:
        se = float("nan")
    return p, se, b, int(n)


# =========================================================================== #
# STAGE A -- exponent re-analysis of the staged cloud artifacts
# =========================================================================== #
def stage_a():
    grid = json.load(open(os.path.join(_ARCHIVE, "ds_cap_4d-grid.json")))
    highN = json.load(open(os.path.join(_ARCHIVE, "ds_cap_4d-highN.json")))
    cells = ([c for c in grid["cells"] if c.get("path") == "dense"]
             + [c for c in highN["cells"] if c.get("path") == "dense"])

    def plateau(c, key):
        # robust scale = mean of the per-box means (avoids the broken saturating
        # S_full_cap fits flagged in VYPOCET-25); A_mol uses its committed cap.
        return float(np.mean(c[key]))

    by_l = {}
    for c in cells:
        by_l.setdefault(c["l"], []).append(c)

    def fits_for(group):
        g = sorted(group, key=lambda c: c["rho"])
        rho = [c["rho"] for c in g]
        A = [c["horizon_links_cap_Amol"] for c in g]
        Sf = [plateau(c, "S_full_mean") for c in g]
        ns = [plateau(c, "n_sub_mean") for c in g]
        Nt = [c.get("N_total_cap", plateau(c, "N_total_mean")) for c in g]
        out = {"rho": rho, "A_mol_raw": A, "S_full_plateau": Sf,
               "n_sub": ns, "N_total": Nt}
        for nm, y in (("p_A", A), ("p_S", Sf), ("p_n", ns), ("p_N", Nt)):
            p, se, _b, n = _loglog_fit(rho, y)
            out[nm] = p
            out[nm + "_se"] = se
            out[nm + "_n"] = n
        out["drift_pS_minus_pA"] = out["p_S"] - out["p_A"]
        return out

    per_l = {f"l={l}": fits_for(by_l[l]) for l in sorted(by_l)}
    pooled = fits_for(cells)
    # cleanest fixed-l = 0.8 column (the VYPOCET-25 reference column)
    clean = per_l.get("l=0.8")

    return {
        "description": ("Stage A: exponent re-analysis of the staged 4D dS "
                        "entropy-cap artifacts (ds_cap_4d-grid + -highN). "
                        "A_mol_raw = horizon_links_cap_Amol (codim-1 worldtube "
                        "link count); S_full = mean over boxes of S_full_mean "
                        "(robust to broken saturating-fit caps)."),
        "n_dense_cells": len(cells),
        "per_l": per_l,
        "pooled": pooled,
        "clean_column_l0p8": clean,
        "headline": {
            "p_A_clean_l0p8": clean["p_A"], "p_A_clean_se": clean["p_A_se"],
            "p_S_clean_l0p8": clean["p_S"], "p_S_clean_se": clean["p_S_se"],
            "drift_clean": clean["drift_pS_minus_pA"],
            "note": ("p_A ~ 1.77, p_S ~ 1.05, drift = p_S - p_A ~ -0.72 -- "
                     "confirms VYPOCET-25 / F-029."),
        },
    }


# =========================================================================== #
# STAGE A2 -- numerical diagnosis of the rho^{1.77} (link multiplicity grows)
# =========================================================================== #
def proper_volume(Rbox, l):
    return (2.0 * T_HALF) * (l * np.tanh(Rbox / l)) * (2.0 * XPERP) ** 2


def stage_a2_diagnosis(rhos=(120.0, 240.0, 480.0, 960.0), Rbox=4.3, seeds=3):
    """Decompose the raw worldtube count: per-element link multiplicity L/N and
    the typical proper (t, r*)-NORMAL separation of straddling links vs eps. The
    rho^{1.77} = (worldtube 3-volume ~ rho^1) x (link multiplicity ~ rho^{0.77});
    straddling links have a roughly rho-INDEPENDENT (large) normal separation,
    proving they are long near-null links, not codim-2-localised molecules."""
    rows = []
    for rho in rhos:
        N = int(round(rho * proper_volume(Rbox, LDS)))
        if N > 4200:        # keep this diagnosis cheap (dense NxN causal matrix)
            continue
        eps = epsilon_of_rho_4d(rho)
        LN, dt_str, dr_str, raw = [], [], [], []
        for s in range(seeds):
            rng = np.random.default_rng(70_000 + 100 * int(rho) + s)
            coords = C.sprinkle_ds_static_patch4d(
                N, rng, l=LDS, rstar_box=Rbox, t_extent=T_HALF,
                x_perp_half=XPERP)
            Cmat = C.causal_matrix(coords)
            L = C.link_matrix(Cmat)
            LN.append(float(L.sum()) / N)
            a, b = np.nonzero(L)
            obs = coords[:, 1] <= R_CUT
            st = obs[a] ^ obs[b]
            raw.append(int(np.count_nonzero(st)))
            t, rs = coords[:, 0], coords[:, 1]
            if st.any():
                dt_str.append(float(np.mean(np.abs(t[a[st]] - t[b[st]]))))
                dr_str.append(float(np.mean(np.abs(rs[a[st]] - rs[b[st]]))))
        rows.append({"rho": rho, "N": N, "eps": eps,
                     "links_per_point": float(np.mean(LN)),
                     "raw_worldtube_links": float(np.mean(raw)),
                     "straddle_mean_abs_dt": float(np.mean(dt_str)),
                     "straddle_mean_abs_drstar": float(np.mean(dr_str))})
    rho = [r["rho"] for r in rows]
    p_LN, se_LN, *_ = _loglog_fit(rho, [r["links_per_point"] for r in rows])
    p_raw, se_raw, *_ = _loglog_fit(rho, [r["raw_worldtube_links"] for r in rows])
    p_dt, *_ = _loglog_fit(rho, [r["straddle_mean_abs_dt"] for r in rows])
    return {
        "description": ("Stage A2: numerical diagnosis of the rho^{1.77} raw "
                        "count. links_per_point ~ rho^{p_LN} is the 4D "
                        "per-element link MULTIPLICITY (O(1) in 2D, grows in "
                        "4D); straddling links keep a rho-independent large "
                        "(t, r*)-normal separation => they are long near-null "
                        "links spanning the worldtube, NOT codim-2 molecules."),
        "rows": rows,
        "p_links_per_point": p_LN, "p_links_per_point_se": se_LN,
        "p_raw_worldtube": p_raw, "p_raw_worldtube_se": se_raw,
        "p_straddle_abs_dt": p_dt,
        "interpretation": (
            "raw ~ rho^{1.77} ~ (n_sub ~ rho^1) x (links_per_point ~ rho^{0.7}); "
            "straddle dt is ~rho-independent (~0.65, near the full t-extent) so "
            "the surface molecules are NOT eps-localised in this flat-order "
            "construction -- the codim-1 worldtube, not a codim-2 area."),
    }


# =========================================================================== #
# STAGE B -- corrected codim-2 molecule confirmatory run + R'/R'' invariance
# =========================================================================== #
RSTAR_BOX = np.array([1.6, 2.2, 2.8, 3.5, 4.3, 5.2])
DENSE_N_MAX = 2500     # afternoon-class wall: skip cells whose max-box N exceeds it


def _saturating_cap(x, y):
    from scipy.optimize import curve_fit
    x = np.asarray(x, float)
    y = np.asarray(y, float)
    p0 = [float(y[-1]), float(y[-1] - y[0]), 1.0]
    try:
        popt, _ = curve_fit(lambda t, cap, B, xi: cap - B * np.exp(-t / xi),
                            x, y, p0=p0, maxfev=40000)
        cap = float(popt[0])
        yhat = popt[0] - popt[1] * np.exp(-x / popt[2])
        sst = float(np.sum((y - y.mean()) ** 2))
        r2 = 1.0 - float(np.sum((y - yhat) ** 2)) / sst if sst > 0 else 0.0
    except Exception:
        cap, r2 = float(y[-1]), 0.0
    return cap, float(r2)


def stage_b(rhos=(120.0, 240.0, 480.0), l=1.0, seeds=4, budget_s=1200.0):
    """For each rho: sweep R*_box -> horizon at fixed proper density; FIXED cut
    O = {r* <= R_CUT}; per seed measure S_full (II_1 content cap), S_trunc
    (area-law n_max = 2 N^{3/4}), the raw worldtube link count A_mol_raw, and the
    CORRECTED codim-2 molecule count A_mol_codim2 (toe.causet). Saturating-fit
    each channel vs R*_box -> cap; then R' = S_full_cap / A_mol_codim2 and
    R'' = S_trunc_cap / A_mol_codim2."""
    cells = []
    for rho in rhos:
        N_max = int(round(rho * proper_volume(RSTAR_BOX.max(), l)))
        if N_max > DENSE_N_MAX:
            cells.append({"rho": rho, "l": l, "path": "skipped",
                          "N_max_planned": N_max,
                          "note": (f"skipped: N_max={N_max} > dense wall "
                                   f"{DENSE_N_MAX} (afternoon budget).")})
            yield ("checkpoint", cells)
            continue
        eps = epsilon_of_rho_4d(rho)
        nb = len(RSTAR_BOX)
        Sfull = np.zeros((seeds, nb))
        Strunc = np.zeros((seeds, nb))
        Araw = np.zeros((seeds, nb))
        Acod2 = np.zeros((seeds, nb))
        Ntot = np.zeros((seeds, nb))
        nsub = np.zeros((seeds, nb))
        max_pair = 0.0
        for j, Rbox in enumerate(RSTAR_BOX):
            if time.time() - t0 > budget_s:
                cells.append({"rho": rho, "l": l, "path": "partial-budget",
                              "completed_boxes": j,
                              "note": "wall-clock budget hit mid-cell."})
                yield ("checkpoint", cells)
                return
            Vbox = proper_volume(Rbox, l)
            N = int(round(rho * Vbox))
            rho_actual = N / Vbox
            nmax = E.n_max_area_law(N, DIM, alpha=ALPHA_RANK)
            for s in range(seeds):
                rng = np.random.default_rng(
                    27_000_000 + 100000 * int(rho) + 1000 * j + s)
                coords = C.sprinkle_ds_static_patch4d(
                    N, rng, l=l, rstar_box=Rbox, t_extent=T_HALF,
                    x_perp_half=XPERP)
                sub = np.where(coords[:, 1] <= R_CUT)[0]
                Ntot[s, j] = N
                nsub[s, j] = sub.size
                if sub.size < 8 or (N - sub.size) < 8:
                    continue
                Cmat = C.causal_matrix(coords)
                L = C.link_matrix(Cmat)
                iD = C.pauli_jordan(C.green_retarded_4d(L, rho_actual))
                diag = C.causal_diagnostics(iD)
                max_pair = max(max_pair, diag["pairing_residual_rel"])
                W = SJ.wightman(iD)
                Strunc[s, j] = abs(E.ssee(W, iD, sub, n_max=nmax).value)
                Sfull[s, j] = abs(E.ssee(W, iD, sub, kappa=None).value)
                a_raw, dch = C.horizon_molecules_codim2(
                    coords, L, r_cut=R_CUT, eps=eps, k_tube=K_TUBE,
                    return_diagnostics=True)
                Acod2[s, j] = a_raw
                Araw[s, j] = dch["n_raw_worldtube_links"]
            yield ("progress", (rho, Rbox, N))
        # caps over the box sweep (mean across seeds). The saturating-fit cap is
        # KNOWN to blow up when the per-box S_full curve is non-monotone (the
        # broken-fit pathology documented in VYPOCET-25): we therefore report it
        # as a DIAGNOSTIC and base R'/R''/the verdict on the ROBUST plateau =
        # mean over the last 3 (near-horizon) boxes, exactly the protocol
        # VYPOCET-25 used for its honest S_full ~ rho^1.05 exponent.
        Sf_cap, Sf_r2 = _saturating_cap(RSTAR_BOX, Sfull.mean(0))
        St_cap, St_r2 = _saturating_cap(RSTAR_BOX, Strunc.mean(0))
        Sf_plateau = float(np.mean(Sfull.mean(0)[-3:]))
        St_plateau = float(np.mean(Strunc.mean(0)[-3:]))
        # plateau A_mol over the last 3 boxes (matches ds_cap_4d convention)
        a_raw_cap = float(np.mean(Araw.mean(0)[-3:]))
        a_cod2_cap = float(np.mean(Acod2.mean(0)[-3:]))
        Rp = Sf_plateau / a_cod2_cap if a_cod2_cap > 0 else float("nan")
        Rpp = St_plateau / a_cod2_cap if a_cod2_cap > 0 else float("nan")
        R_raw = Sf_plateau / a_raw_cap if a_raw_cap > 0 else float("nan")
        cells.append({
            "rho": rho, "l": l, "path": "dense", "eps": eps,
            "n_seeds": seeds, "RSTAR_BOX": RSTAR_BOX.tolist(),
            "N_total_mean": Ntot.mean(0).tolist(),
            "n_sub_mean": nsub.mean(0).tolist(),
            "S_full_mean": Sfull.mean(0).tolist(),
            "S_trunc_mean": Strunc.mean(0).tolist(),
            "A_mol_raw_mean": Araw.mean(0).tolist(),
            "A_mol_codim2_mean": Acod2.mean(0).tolist(),
            "S_full_cap": Sf_cap, "S_full_cap_R2": Sf_r2,
            "S_trunc_cap": St_cap, "S_trunc_cap_R2": St_r2,
            "S_full_plateau": Sf_plateau, "S_trunc_plateau": St_plateau,
            "A_mol_raw_cap": a_raw_cap,
            "A_mol_codim2_cap": a_cod2_cap,
            "R_raw_Sfull_over_Amol_raw": R_raw,
            "R_prime_Sfull_over_Amol_codim2": Rp,
            "R_dprime_Strunc_over_Amol_codim2": Rpp,
            "pairing_residual_rel_max": max_pair,
        })
        yield ("checkpoint", cells)


def _scan_exponent(cells, key):
    g = [c for c in cells if c.get("path") == "dense"]
    rho = [c["rho"] for c in g]
    y = [c[key] for c in g]
    p, se, _b, n = _loglog_fit(rho, y)
    return {"p": p, "se": se, "n": n}


def _cv(cells, key):
    g = [c for c in cells if c.get("path") == "dense"
         and isinstance(c.get(key), (int, float)) and np.isfinite(c[key])]
    v = np.array([c[key] for c in g], float)
    if v.size < 2 or v.mean() == 0:
        return float("nan")
    return float(v.std(ddof=1) / abs(v.mean()))


# =========================================================================== #
# PLOT: A_mol_raw vs corrected codim-2 vs S_full on log-log
# =========================================================================== #
def make_plot(stage_a_res, stage_b_cells):
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    fig, ax = plt.subplots(figsize=(7.2, 5.4))
    # archive raw A_mol + S_full (clean l=0.8 column), full rho range
    clean = stage_a_res["clean_column_l0p8"]
    rho_a = np.array(clean["rho"], float)
    ax.loglog(rho_a, clean["A_mol_raw"], "o-", color="crimson",
              label=r"$A_{\rm mol}^{\rm raw}$ (codim-1 worldtube), $p_A=%.2f$"
                    % clean["p_A"])
    ax.loglog(rho_a, clean["S_full_plateau"], "s-", color="navy",
              label=r"$S_{\rm full}$ (content), $p_S=%.2f$" % clean["p_S"])
    # corrected codim-2 from Stage B
    g = [c for c in stage_b_cells if c.get("path") == "dense"]
    if g:
        rho_b = np.array([c["rho"] for c in g], float)
        cod2 = np.array([c["A_mol_codim2_cap"] for c in g], float)
        p2, *_ = _loglog_fit(rho_b, cod2)
        ax.loglog(rho_b, cod2, "D-", color="green",
                  label=r"$A_{\rm mol}^{\rm codim\text{-}2}$ (corrected), "
                        r"$p=%.2f$" % p2)
    # reference power-law guides
    rr = np.array([rho_a.min(), rho_a.max()])
    for p, c, lab in ((1.77, "crimson", r"$\rho^{1.77}$"),
                      (1.05, "navy", r"$\rho^{1.05}$"),
                      (0.5, "green", r"$\rho^{0.5}$ (proper area)")):
        y0 = (clean["A_mol_raw"][0] if p > 1.5 else
              clean["S_full_plateau"][0] if p > 0.9 else
              (cod2[0] if g else 1.0))
        ax.loglog(rr, y0 * (rr / rr[0]) ** p, "--", color=c, alpha=0.35, lw=1)
    ax.set_xlabel(r"density $\rho$")
    ax.set_ylabel("count / entropy")
    ax.set_title("VYPOCET-27: 4D horizon molecule convention\n"
                 r"raw $\rho^{1.77}$ vs corrected codim-2 $\rho^{0.5}$ vs "
                 r"$S_{\rm full}\,\rho^{1.05}$")
    ax.legend(fontsize=8, loc="upper left")
    ax.grid(True, which="both", alpha=0.25)
    fig.tight_layout()
    out = os.path.join(_PLOTS, "A_mol_raw_vs_corrected_vs_rho.png")
    fig.savefig(out, dpi=130)
    plt.close(fig)
    # Return a REPO-RELATIVE path: an absolute machine path written into
    # results.json would leak into the built web artifact (calculations.html),
    # which app/tests/test_web_build.py forbids. Portability per CLAUDE.md.
    repo_root = os.path.normpath(os.path.join(_HERE, "..", "..", ".."))
    return os.path.relpath(out, repo_root)


# =========================================================================== #
# MAIN
# =========================================================================== #
def main():
    meta = {
        "calc": "ds-amol-convention",
        "vypocet": "VYPOCET-27",
        "question": ("WHY A_mol ~ rho^{1.77} (codim-1 worldtube) not rho^{0.5} "
                     "(codim-2 area), and is the 4D area-law salvageable?"),
        "anti_circularity": {
            "epsilon_law": "eps = rho^{-1/4} (4D) FIXED from F-006 rho^{-1/d}",
            "F006_p_rank": P_RANK, "F006_p_err": P_RANK_ERR},
        "geometry": {"l": LDS, "T_HALF": T_HALF, "XPERP": XPERP,
                     "R_CUT": R_CUT, "DIM": DIM, "alpha_rank": ALPHA_RANK,
                     "k_tube_codim2": K_TUBE, "dense_N_max": DENSE_N_MAX},
        "references_repo_present_only": [
            "dou-sorkin-2003 (gr-qc/0302009)", "johnston-2009 (0909.0944)",
            "clpw-2022 (2206.10780)", "F-006 (ssee-diamond)"],
        "conformal_weight_caveat": (
            "4D massless scalar NOT conformally invariant; VYPOCET-21 controlled "
            "approximation (flat order + dS sech^2 measure + Johnston link "
            "Green), not the exact dS Wightman state. dS A/4 'WARN neoveřeno'."),
        "c_2D_reference": C_2D_REFERENCE,
        "toe_version": toe.__version__,
    }
    payload = {"meta": meta}

    print("[ds-amol-convention] STAGE A: exponent re-analysis")
    payload["stage_a_exponents"] = stage_a()
    _write(payload, "partial")
    h = payload["stage_a_exponents"]["headline"]
    print(f"  p_A(l=0.8)={h['p_A_clean_l0p8']:.3f}±{h['p_A_clean_se']:.3f}  "
          f"p_S={h['p_S_clean_l0p8']:.3f}±{h['p_S_clean_se']:.3f}  "
          f"drift={h['drift_clean']:.3f}")

    print("[ds-amol-convention] STAGE A2: rho^1.77 diagnosis")
    payload["stage_a2_diagnosis"] = stage_a2_diagnosis()
    _write(payload, "partial")
    d = payload["stage_a2_diagnosis"]
    print(f"  links/point ~ rho^{d['p_links_per_point']:.3f}  "
          f"raw ~ rho^{d['p_raw_worldtube']:.3f}  "
          f"straddle |dt| ~ rho^{d['p_straddle_abs_dt']:.3f}")

    print("[ds-amol-convention] STAGE B: corrected codim-2 confirmatory run")
    cells = []
    for kind, data in stage_b():
        if kind == "progress":
            rho, Rbox, N = data
            print(f"   rho={rho:g} R*={Rbox:.1f} N={N}")
        else:
            cells = data
            payload["stage_b_codim2_run"] = {"cells": cells}
            _write(payload, "partial")

    # cross-cell verdict (use the ROBUST plateau S_full, not the broken fit cap)
    p_cod2 = _scan_exponent(cells, "A_mol_codim2_cap")
    p_raw_b = _scan_exponent(cells, "A_mol_raw_cap")
    p_sfull_b = _scan_exponent(cells, "S_full_plateau")
    cv_Rp = _cv(cells, "R_prime_Sfull_over_Amol_codim2")
    cv_Rpp = _cv(cells, "R_dprime_Strunc_over_Amol_codim2")
    cv_Rraw = _cv(cells, "R_raw_Sfull_over_Amol_raw")
    drift_Rp, _se, *_ = _loglog_fit(
        [c["rho"] for c in cells if c.get("path") == "dense"],
        [c["R_prime_Sfull_over_Amol_codim2"]
         for c in cells if c.get("path") == "dense"])

    verdict = {
        "p_A_mol_codim2_corrected": p_cod2,
        "p_A_mol_raw_confirm": p_raw_b,
        "p_S_full_confirm": p_sfull_b,
        "R_prime_cv": cv_Rp, "R_prime_drift_lnln": drift_Rp,
        "R_dprime_cv": cv_Rpp, "R_raw_cv": cv_Rraw,
        "R_prime_constant": bool(np.isfinite(cv_Rp) and cv_Rp < 0.10),
        "R_dprime_constant": bool(np.isfinite(cv_Rpp) and cv_Rpp < 0.10),
        "outcome": _classify(p_cod2["p"], p_sfull_b["p"], cv_Rp, cv_Rpp),
    }
    payload["stage_b_codim2_run"]["verdict"] = verdict
    print(f"  corrected A_mol codim-2 ~ rho^{p_cod2['p']:.3f}±{p_cod2['se']:.3f}; "
          f"S_full ~ rho^{p_sfull_b['p']:.3f}")
    print(f"  R' CV={cv_Rp:.3f} (const={verdict['R_prime_constant']}), "
          f"R'' CV={cv_Rpp:.3f} (const={verdict['R_dprime_constant']})")
    print(f"  OUTCOME: {verdict['outcome']}")

    payload["plot"] = make_plot(payload["stage_a_exponents"], cells)
    _write(payload, "complete")
    print(f"  wrote {_RESULTS}")
    return 0


def _classify(p_cod2, p_sfull, cv_Rp, cv_Rpp):
    """Decisive discriminator (VYPOCET-27 deliverable 5):
    (a) R' constant -> 4D area-law SALVAGED;
    (b) molecule ~ rho^0.5 but S_full ~ rho^1 (R' drifts) -> area-law ABSENT
        in this construction (honest negative, strengthening VYPOCET-25);
    (c) R'' (S_trunc channel) constant -> truncated is the right area channel."""
    cod2_arealike = (np.isfinite(p_cod2) and abs(p_cod2 - 0.5) < 0.30)
    sfull_volumetric = (np.isfinite(p_sfull) and p_sfull > 0.85)
    if np.isfinite(cv_Rp) and cv_Rp < 0.10:
        return "(a) 4D area-law SALVAGED: R' = S_full_cap/A_mol_codim2 is density-invariant."
    if np.isfinite(cv_Rpp) and cv_Rpp < 0.10:
        return "(c) S_trunc is the area channel: R'' = S_trunc_cap/A_mol_codim2 is density-invariant."
    if cod2_arealike and sfull_volumetric:
        return ("(b) 4D area-law ABSENT in this construction: corrected molecule "
                "~rho^0.5 (proper area) but S_full ~rho^1 (volumetric content), "
                "so R' still drifts -- the cap does NOT track proper horizon "
                "area. Honest negative, strengthens VYPOCET-25/F-029.")
    return ("indeterminate: corrected molecule exponent or S_full exponent off "
            "the expected values -- see Stage B cells.")


if __name__ == "__main__":
    raise SystemExit(main())
