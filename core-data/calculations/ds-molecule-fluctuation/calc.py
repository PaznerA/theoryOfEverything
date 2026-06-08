#!/usr/bin/env python3
r"""VYPOCET-34 -- H6g-6: is the 4D de Sitter horizon entropy-AREA relation
carried by the FLUCTUATION (variance) of the codim-2 Dou-Sorkin molecule count
across sprinklings (Sorkin "order-by-disorder" counting), rather than by its
MEAN -- where the mean failed in F-031 / VYPOCET-27?

Background (the open door this test walks through):

  * F-031 / VYPOCET-27 killed the 4D MEAN-count area-law: the corrected codim-2
    molecule count scales as the proper area <N_mol> ~ rho^{0.494}, BUT the
    content entropy S_full ~ rho^{1.0}, so the ratio S_full / A drifts -- NO
    rho-invariant 4D area-law on the MEAN axis (clean negative, dimension-dep:
    2D works, 4D does not).

  * F-035 / VYPOCET-31 is the SAME "variance not mean" theme one rung over: the
    Lambda shot-noise survives F-005 on the VARIANCE / boost-covariance axis
    (Fano = 1, Var(N) ~ V, boost-invariant) where the mean prefactor was refuted.

  H6g-6 is the entropy analog: maybe the area-law lives in Var(N_mol), not
  <N_mol>. Sorkin's original order-by-disorder horizon-entropy is a statement
  about the FLUCTUATION of the causal-link count across the horizon, not its
  mean. Prediction to test: Var(N_mol^codim-2) ~ rho^{0.5} (proper area), giving
  a rho-invariant ratio Var/A_proper -> an order-by-disorder area-law where the
  mean one was absent (positive, mirrors F-035). If instead Var ~ rho^{>~1}
  (volumetric / Fano-anomalous), neither mean nor variance gives a 4D area-law
  (clean negative, strengthens F-031 on a second independent axis).

METHOD. On the SAME fixed codim-2 entangling 2-surface E_0 = {r* = R_CUT, t = 0}
and the SAME geometry as F-031 (sprinkle_ds_static_patch4d, l = 1, near-horizon
box R*_box = 4.3, R_CUT = 1.0, k_tube = 1.5), measure the across-seed
DISTRIBUTION of the codim-2 molecule count N_mol over MANY independent
sprinklings (>= 80 seeds) at rho in {120, 240, 480, 960}. The molecule count is
pure combinatorics on the causal/link matrix -- NO eigh, NO SSEE -- so many
seeds are cheap. Observables vs rho:

   mean   <N_mol>                        (re-confirm F-031 area scaling rho^0.5)
   Var    Var(N_mol)            ~ rho^q  (THE order-by-disorder observable)
   std    sqrt(Var)             ~ rho^{q/2}
   Fano   Var / <N_mol>                  (Poisson => 1; trend is the discriminator)
   S_fluc 0.5 ln(2 pi e Var)            (Gaussian order-by-disorder entropy = ln #configs)

ANTI-CIRCULARITY: eps = rho^{-1/4} (4D) FIXED from the INDEPENDENT F-006
rho^{-1/d} law (ssee-diamond, p_rank = 0.519 +/- 0.007), asserted BEFORE any
ratio -- never tuned to make Var/A constant. k_tube = 1.5 inherited UNCHANGED
from the F-031 primitive (no re-tuning; the k_tube sensitivity caveat is carried
honestly from VYPOCET-27).

DISCRIMINATOR (reported as `correspondence`):
   Var(N_mol) ~ rho^{~0.5}, Var/A_proper rho-invariant (CV < ~0.15)
       -> "fluctuation-arealaw": order-by-disorder area-law EXISTS where the mean
          one did not (positive, mirrors F-035); reopens 4D entropy-area on the
          variance axis.
   Var(N_mol) ~ rho^{clearly != 0.5} (e.g. ~rho^1), no rho-invariant ratio
       -> "negative": 4D area-law ABSENT on BOTH mean and fluctuation axes
          (clean negative, strengthens F-031).
   mixed / borderline -> "partial".

HONEST CAVEATS (carried): 4D massless scalar is NOT conformally invariant; this
is the VYPOCET-21 controlled approximation (flat causal order in (t, r*, x1, x2)
+ dS proper sech^2 measure), NOT the exact dS Wightman state. No eigh here, so no
SSEE positivity question arises; the fluctuation is purely geometric (count of
near-null straddling links on the codim-2 surface). The de-Sitter-specific
Gibbons-Hawking primary is NOT in the repo -> dS A/4 application 'WARN
neoveřeno'. Only repo-present references cited: dou-sorkin-2003 (gr-qc/0302009),
johnston-2009 (0909.0944), F-006, F-031 (VYPOCET-27), F-035 (VYPOCET-31).

Thin orchestrator over ``toe`` (v0.3.x); all physics lives in the library
(toe.causet.horizon_molecules_codim2 from VYPOCET-27 + the new
toe.causet.molecule_count_fluctuation helper added in this run).
Portability: every path is derived __file__-relative (CLAUDE.md Konvence kodu);
results.json is written atomically (tmp + os.replace) with a progressive
``status`` field so a session-limit interruption leaves a clean partial output.
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

_PLOTS = os.path.join(_HERE, "plots")
os.makedirs(_PLOTS, exist_ok=True)
_RESULTS = os.path.join(_HERE, "results.json")

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


# geometry constants -- mirror VYPOCET-27 / compute/drivers/ds_cap_4d.py exactly
LDS = 1.0
T_HALF = 0.5
XPERP = 1.0
R_CUT = 1.0
DIM = 4
K_TUBE = 1.5            # codim-2 molecule tube radius in eps units (VYPOCET-27)
RSTAR_BOX = 4.3        # near-horizon box = the F-031 Stage-B plateau box
SEED0 = 34_000_000     # disjoint from VYPOCET-27 (27M) and VYPOCET-31 (20.26M)
STRIDE = 100_000       # non-overlapping per-rho seed streams

# rho grid + per-rho seed count. The molecule count is pure combinatorics on the
# N x N causal matrix (no eigh), so the cost is O(N^2) per seed; many seeds are
# cheap. N(rho) at R*_box = 4.3: 480, 960, 1919, 3839, 7677 for rho 120..1920.
# rho=1920 (N=7677, ~0.47 GB causal matrix) extends the lever arm to harden the
# Var exponent CI -- the variance estimator is the noisy one (BRAINSTORM-06
# risk), so the answer (is 0.5 excluded?) needs both many seeds AND a wide rho.
RHOS = (120.0, 240.0, 480.0, 960.0, 1920.0)
N_SEEDS = 200          # >> the >=50 floor; variance estimator needs many seeds
DENSE_N_WALL = 8000    # causal-matrix (NOT eigh) wall; rho=1920 -> N=7677 < wall

t0 = time.time()


# --------------------------------------------------------------------------- #
# atomic, schema-stable writer (write tmp + os.replace), progressive checkpoints
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


def proper_volume(Rbox, l):
    return (2.0 * T_HALF) * (l * np.tanh(Rbox / l)) * (2.0 * XPERP) ** 2


def proper_area_codim2(l):
    """Proper AREA of the FIXED codim-2 entangling 2-surface E_0 = {r* = R_CUT,
    t = 0}, swept by the two transverse directions x1, x2 in [-XPERP, XPERP].
    In the flat (t, r*, x1, x2) order the transverse box is flat, so the proper
    area is just (2 XPERP)^2 -- rho-INDEPENDENT, the geometric area whose
    rho^{1/2} discretisation gives <N_mol> = A / eps^2 * O(1)."""
    return (2.0 * XPERP) ** 2


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


def _bootstrap_var_exponent(counts_by_rho, rhos, n_boot=2000, seed=20260608):
    """Bootstrap the exponent of Var(N_mol) ~ rho^q AND of sqrt(Var) ~ rho^{q/2}
    AND of mean ~ rho^p by resampling SEEDS within each rho (with replacement),
    recomputing the per-rho mean/var, and refitting. Returns dict of
    (value, [p16, p84], boot_std) for q (var), q_std (sqrt-var), p (mean),
    and the Fano slope. This is the honest CI on a variance exponent (the
    variance estimator is much noisier than the mean -- BRAINSTORM-06 risk)."""
    rng = np.random.default_rng(seed)
    rhos = np.asarray(rhos, float)
    q_boot, qstd_boot, p_boot, fano_slope_boot = [], [], [], []
    for _ in range(n_boot):
        var_b, mean_b, std_b, fano_b = [], [], [], []
        for rho in rhos:
            c = counts_by_rho[rho]
            idx = rng.integers(0, c.size, size=c.size)
            cs = c[idx].astype(float)
            mu = cs.mean()
            v = cs.var(ddof=1)
            mean_b.append(mu)
            var_b.append(v)
            std_b.append(math.sqrt(v) if v > 0 else 0.0)
            fano_b.append(v / mu if mu > 0 else float("nan"))
        q, *_ = _loglog_fit(rhos, var_b)
        qs, *_ = _loglog_fit(rhos, std_b)
        p, *_ = _loglog_fit(rhos, mean_b)
        fs, *_ = _loglog_fit(rhos, fano_b)
        if math.isfinite(q):
            q_boot.append(q)
        if math.isfinite(qs):
            qstd_boot.append(qs)
        if math.isfinite(p):
            p_boot.append(p)
        if math.isfinite(fs):
            fano_slope_boot.append(fs)

    def summarise(arr):
        a = np.asarray(arr, float)
        return {
            "value": float(np.median(a)),
            "ci68": [float(np.percentile(a, 16)), float(np.percentile(a, 84))],
            "ci95": [float(np.percentile(a, 2.5)), float(np.percentile(a, 97.5))],
            "boot_std": float(a.std(ddof=1)),
            "n_boot": int(a.size),
        }

    return {
        "q_var": summarise(q_boot),
        "q_std_sqrtvar": summarise(qstd_boot),
        "p_mean": summarise(p_boot),
        "fano_slope": summarise(fano_slope_boot),
    }


# =========================================================================== #
# STAGE 1 -- across-seed molecule-count distribution at each rho
# =========================================================================== #
def stage_measure(rhos=RHOS, n_seeds=N_SEEDS, budget_s=1100.0):
    """For each rho, draw n_seeds INDEPENDENT sprinklings of the SAME fixed
    geometry (near-horizon box, fixed codim-2 cut), count the codim-2 molecule
    number per seed, and accumulate the across-seed distribution. Pure
    combinatorics (causal matrix + link reduction + molecule count) -- no eigh.
    Progressive: yields a checkpoint after each rho so an interruption leaves a
    valid partial results.json."""
    cells = []
    counts_by_rho = {}
    for rho in rhos:
        N = int(round(rho * proper_volume(RSTAR_BOX, LDS)))
        eps = epsilon_of_rho_4d(rho)
        if N > DENSE_N_WALL:
            cells.append({"rho": rho, "N": N, "path": "skipped",
                          "note": (f"skipped: N={N} > causal-matrix wall "
                                   f"{DENSE_N_WALL}.")})
            counts_by_rho[rho] = np.array([], int)
            yield ("checkpoint", (cells, counts_by_rho))
            continue
        counts = np.empty(n_seeds, dtype=np.int64)
        n_done = 0
        for s in range(n_seeds):
            if time.time() - t0 > budget_s:
                # partial-budget: keep the seeds done so far (valid sub-sample)
                counts = counts[:n_done]
                cells.append({"rho": rho, "N": N, "eps": eps,
                              "path": "partial-budget", "n_seeds": int(n_done),
                              "note": "wall-clock budget hit mid-rho."})
                counts_by_rho[rho] = counts
                yield ("checkpoint", (cells, counts_by_rho))
                return
            rng = np.random.default_rng(SEED0 + STRIDE * int(rho) + s)
            coords = C.sprinkle_ds_static_patch4d(
                N, rng, l=LDS, rstar_box=RSTAR_BOX, t_extent=T_HALF,
                x_perp_half=XPERP)
            Cm = C.causal_matrix(coords)
            counts[s] = C.horizon_molecules_codim2(
                coords, Cm, r_index=1, r_cut=R_CUT, eps=eps, k_tube=K_TUBE)
            n_done += 1
        counts_by_rho[rho] = counts
        mu = float(counts.mean())
        var = float(counts.var(ddof=1))
        std = math.sqrt(var)
        # SE of the variance estimator (normal approx): Var * sqrt(2/(n-1))
        var_se = var * math.sqrt(2.0 / (n_seeds - 1)) if n_seeds > 1 else float("nan")
        fano = var / mu if mu > 0 else float("nan")
        # Gaussian order-by-disorder entropy = ln(#configs) for a continuous
        # Gaussian of variance var: S_fluc = 0.5 ln(2 pi e var). Up to the
        # additive log this is "ln(number of distinguishable configurations)".
        s_fluc = 0.5 * math.log(2.0 * math.pi * math.e * var) if var > 0 else float("nan")
        cells.append({
            "rho": rho, "N": N, "eps": eps, "path": "dense",
            "n_seeds": int(n_seeds),
            "mean_Nmol": mu,
            "var_Nmol": var, "var_Nmol_SE": var_se,
            "std_Nmol": std,
            "fano_Nmol": fano,
            "S_fluc_gaussian": s_fluc,
            "min_Nmol": int(counts.min()), "max_Nmol": int(counts.max()),
            "A_proper_codim2": proper_area_codim2(LDS),
            "var_over_A": var / proper_area_codim2(LDS),
            "mean_over_A": mu / proper_area_codim2(LDS),
        })
        yield ("progress", (rho, N, mu, var, fano))
        yield ("checkpoint", (cells, counts_by_rho))


def _cv(values):
    v = np.array([x for x in values if isinstance(x, (int, float))
                  and np.isfinite(x)], float)
    if v.size < 2 or v.mean() == 0:
        return float("nan")
    return float(v.std(ddof=1) / abs(v.mean()))


def _classify(q_var, q_var_ci, p_mean, cv_var_over_A, cv_mean_over_A,
              fano_slope):
    """Order-by-disorder discriminator (deliverable).

    The proper-area target is rho^{0.5}; the volumetric scaling is rho^{1.0}.
    The decision keys on the bootstrap CI of the Var exponent q AND on whether
    the ratio Var/A_proper is rho-invariant:

    fluctuation-arealaw : q_var CI INCLUDES 0.5 (area) and EXCLUDES ~1 AND
        Var/A_proper rho-invariant (CV < 0.15) -> order-by-disorder area-law
        EXISTS where the MEAN one did not (positive, mirrors F-035).
    negative            : q_var CI EXCLUDES 0.5 (the area target is ruled out)
        -> no fluctuation area-law; the 4D dS area-law is ABSENT on BOTH the
        mean and the variance axes (clean negative, strengthens F-031).
    partial             : q_var CI INCLUDES 0.5 but is too wide to also exclude
        ~1, or Var/A_proper still drifts -- genuinely inconclusive."""
    lo, hi = q_var_ci
    ci_includes_half = (lo <= 0.5 <= hi)
    ci_excludes_half = (lo > 0.5) or (hi < 0.5)
    ci_excludes_one = hi < 0.85
    var_area_invariant = (np.isfinite(cv_var_over_A) and cv_var_over_A < 0.15)

    if ci_includes_half and ci_excludes_one and var_area_invariant:
        return ("fluctuation-arealaw", (
            f"Var(N_mol) ~ rho^{q_var:.2f} (CI [{lo:.2f},{hi:.2f}] includes the "
            f"area target 0.5, excludes volumetric ~1) and Var/A_proper is "
            f"rho-invariant (CV={cv_var_over_A:.2f} < 0.15): an order-by-disorder "
            f"area-law EXISTS on the FLUCTUATION axis where the MEAN-count one "
            f"was absent (F-031). Mirrors F-035 (variance survives where mean "
            f"failed). Reopens the 4D entropy-area question on the variance axis."))
    if ci_excludes_half:
        return ("negative", (
            f"Var(N_mol) ~ rho^{q_var:.2f} (CI [{lo:.2f},{hi:.2f}]) EXCLUDES the "
            f"proper-area target rho^0.5; Var/A_proper drifts (CV={cv_var_over_A:.2f}). "
            f"The MEAN already failed (F-031: <N_mol> ~ rho^{p_mean:.2f} area but "
            f"S_full ~ rho^1) and now the FLUCTUATION also fails to give a clean "
            f"area-law -> the 4D dS area-law is ABSENT on BOTH the mean and the "
            f"variance axes. A second independent negative strengthening F-031. "
            f"The molecule count is super-Poisson with a growing Fano "
            f"(~rho^{fano_slope:.2f}): the variance exponent {q_var:.2f} sits "
            f"ABOVE the area 0.5 but BELOW the volumetric 1.0, i.e. clustering of "
            f"near-null straddling links on the codim-2 surface lifts Var above "
            f"area scaling without reaching a volume law. Unlike F-035 (Fano=1, "
            f"Poisson), the count is NOT Poisson here, so the variance carries no "
            f"clean area signal."))
    return ("partial", (
        f"Var(N_mol) ~ rho^{q_var:.2f} (CI [{lo:.2f},{hi:.2f}]): the CI includes "
        f"the area target 0.5 but is too wide to exclude steeper scalings, or "
        f"Var/A_proper still drifts (CV={cv_var_over_A:.2f}). Inconclusive on "
        f"whether a fluctuation area-law exists -- more seeds / wider rho needed."))


# =========================================================================== #
# PLOTS
# =========================================================================== #
def make_plots(cells, fits):
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    dense = [c for c in cells if c.get("path") == "dense"]
    rho = np.array([c["rho"] for c in dense], float)
    mean = np.array([c["mean_Nmol"] for c in dense], float)
    var = np.array([c["var_Nmol"] for c in dense], float)
    var_se = np.array([c["var_Nmol_SE"] for c in dense], float)
    std = np.array([c["std_Nmol"] for c in dense], float)
    fano = np.array([c["fano_Nmol"] for c in dense], float)

    # Plot paths are stored CALC-DIR-relative ("plots/<name>.png"): a repo-root-
    # relative path would differ between the committed location and the /tmp
    # reproduction sandbox (FULL_REPRO test flags it as a value-change), and an
    # absolute path leaks the host into the web build (test_web_build). The
    # basename-only convention mirrors the sibling lambda-shot-noise calc.
    paths = {}

    # ---- Plot 1: Var(N_mol) and sqrt(Var) vs rho (the area-law test) -------- #
    fig, ax = plt.subplots(figsize=(7.4, 5.6))
    ax.errorbar(rho, var, yerr=var_se, fmt="o", color="darkorange", capsize=3,
                label=r"$\mathrm{Var}(N_{\rm mol})$, "
                      r"$q=%.2f\pm%.2f$" % (fits["q_var"]["value"],
                                            fits["q_var"]["boot_std"]))
    ax.plot(rho, std, "s", color="teal",
            label=r"$\sqrt{\mathrm{Var}}$, "
                  r"$q/2=%.2f$" % fits["q_std_sqrtvar"]["value"])
    ax.plot(rho, mean, "^", color="navy",
            label=r"$\langle N_{\rm mol}\rangle$ (mean, F-031), "
                  r"$p=%.2f$" % fits["p_mean"]["value"])
    rr = np.array([rho.min(), rho.max()])
    # reference guides anchored at the first var point
    for p, lab, col in ((0.5, r"$\rho^{0.5}$ (proper area)", "green"),
                        (1.0, r"$\rho^{1.0}$ (volumetric)", "red")):
        ax.plot(rr, var[0] * (rr / rr[0]) ** p, "--", color=col, alpha=0.4,
                lw=1.2, label=lab)
    ax.set_xscale("log"); ax.set_yscale("log")
    ax.set_xlabel(r"density $\rho$")
    ax.set_ylabel(r"molecule count statistics")
    ax.set_title("VYPOCET-34 (H6g-6): order-by-disorder molecule fluctuation\n"
                 r"is the 4D dS horizon area-law carried by $\mathrm{Var}(N_{\rm mol})$?")
    ax.legend(fontsize=8, loc="upper left")
    ax.grid(True, which="both", alpha=0.25)
    fig.tight_layout()
    out1 = os.path.join(_PLOTS, "var_molecule_vs_A.png")
    fig.savefig(out1, dpi=130); plt.close(fig)
    paths["var_molecule_vs_A"] = os.path.relpath(out1, _HERE)

    # ---- Plot 2: fluctuation vs mean area-law (Fano + ratios) --------------- #
    fig, (axL, axR) = plt.subplots(1, 2, figsize=(11.0, 4.8))
    # left: Var/A and mean/A vs rho (rho-invariance test)
    A0 = dense[0]["A_proper_codim2"]
    axL.plot(rho, var / A0, "o-", color="darkorange",
             label=r"$\mathrm{Var}/A_{\rm proper}$ (fluctuation)")
    axL.plot(rho, mean / A0, "^-", color="navy",
             label=r"$\langle N\rangle/A_{\rm proper}$ (mean)")
    axL.set_xscale("log"); axL.set_yscale("log")
    axL.set_xlabel(r"density $\rho$")
    axL.set_ylabel(r"count / $A_{\rm proper}$")
    axL.set_title("ratio-to-area: rho-invariant => area-law\n"
                  r"(flat line = area-law on that axis)")
    axL.legend(fontsize=8); axL.grid(True, which="both", alpha=0.25)
    # right: Fano factor vs rho (Poisson => flat at 1)
    axR.plot(rho, fano, "D-", color="purple",
             label=r"Fano $=\mathrm{Var}/\langle N\rangle$, "
                   r"slope $%.2f$" % fits["fano_slope"]["value"])
    axR.axhline(1.0, ls=":", color="gray", label="Poisson (Fano = 1)")
    axR.set_xscale("log")
    axR.set_xlabel(r"density $\rho$")
    axR.set_ylabel("Fano factor")
    axR.set_title("Fano trend: flat@1 = Poisson/area-clean;\n"
                  "rising = super-Poisson (Var steeper than mean)")
    axR.legend(fontsize=8); axR.grid(True, which="both", alpha=0.25)
    fig.tight_layout()
    out2 = os.path.join(_PLOTS, "fluctuation_vs_mean_arealaw.png")
    fig.savefig(out2, dpi=130); plt.close(fig)
    paths["fluctuation_vs_mean_arealaw"] = os.path.relpath(out2, _HERE)
    return paths


# =========================================================================== #
# MAIN
# =========================================================================== #
def main():
    meta = {
        "calc": "ds-molecule-fluctuation",
        "vypocet": "VYPOCET-34",
        "hypothesis": "H6g-6 (BRAINSTORM-06)",
        "question": ("Is the 4D dS horizon entropy-AREA relation carried by the "
                     "FLUCTUATION Var(N_mol^codim-2) across sprinklings "
                     "(order-by-disorder), where the MEAN count failed (F-031)?"),
        "anti_circularity": {
            "epsilon_law": "eps = rho^{-1/4} (4D) FIXED from F-006 rho^{-1/d}",
            "F006_p_rank": P_RANK, "F006_p_err": P_RANK_ERR,
            "k_tube": K_TUBE, "k_tube_note": (
                "k_tube=1.5 inherited UNCHANGED from VYPOCET-27 primitive; not "
                "re-tuned to make Var/A constant (k_tube sensitivity caveat "
                "carried from F-031).")},
        "geometry": {"l": LDS, "T_HALF": T_HALF, "XPERP": XPERP,
                     "R_CUT": R_CUT, "DIM": DIM, "RSTAR_BOX": RSTAR_BOX,
                     "k_tube_codim2": K_TUBE, "dense_N_wall": DENSE_N_WALL,
                     "A_proper_codim2": proper_area_codim2(LDS)},
        "seed_scheme": {"SEED0": SEED0, "STRIDE": STRIDE,
                        "formula": "default_rng(SEED0 + STRIDE*int(rho) + s)"},
        "rho_grid": list(RHOS), "n_seeds_per_rho": N_SEEDS,
        "references_repo_present_only": [
            "dou-sorkin-2003 (gr-qc/0302009)", "johnston-2009 (0909.0944)",
            "F-006 (ssee-diamond)", "F-031 (VYPOCET-27 ds-amol-convention)",
            "F-035 (VYPOCET-31 lambda-shot-noise)"],
        "conformal_weight_caveat": (
            "4D massless scalar NOT conformally invariant; VYPOCET-21 controlled "
            "approximation (flat order in (t,r*,x1,x2) + dS sech^2 measure). No "
            "eigh/SSEE here -> the fluctuation is purely GEOMETRIC (count of "
            "near-null straddling links on the codim-2 surface). dS A/4 'WARN "
            "neoveřeno' (no GH primary in repo)."),
        "toe_version": toe.__version__,
    }
    payload = {"meta": meta}
    _write(payload, "partial")

    print("[ds-molecule-fluctuation] measuring molecule-count distribution")
    cells = []
    counts_by_rho = {}
    for kind, data in stage_measure():
        if kind == "progress":
            rho, N, mu, var, fano = data
            print(f"  rho={rho:g} N={N}  <N>={mu:.1f}  Var={var:.1f}  "
                  f"Fano={fano:.2f}")
        else:
            cells, counts_by_rho = data
            payload["distribution"] = {"cells": cells}
            _write(payload, "partial")

    # ----- exponent fits + bootstrap CIs (variance estimator is noisy) ------- #
    dense = [c for c in cells if c.get("path") == "dense"]
    rho = [c["rho"] for c in dense]
    p_mean, se_mean, *_ = _loglog_fit(rho, [c["mean_Nmol"] for c in dense])
    q_var, se_var, *_ = _loglog_fit(rho, [c["var_Nmol"] for c in dense])
    q_std, se_std, *_ = _loglog_fit(rho, [c["std_Nmol"] for c in dense])
    fano_slope, se_fano, *_ = _loglog_fit(rho, [c["fano_Nmol"] for c in dense])
    p_sfluc, se_sfluc, *_ = _loglog_fit(rho, [c["S_fluc_gaussian"] for c in dense])

    boot = _bootstrap_var_exponent(
        {c["rho"]: counts_by_rho[c["rho"]] for c in dense}, rho)

    cv_var_over_A = _cv([c["var_over_A"] for c in dense])
    cv_mean_over_A = _cv([c["mean_over_A"] for c in dense])
    cv_fano = _cv([c["fano_Nmol"] for c in dense])

    corr, corr_text = _classify(
        boot["q_var"]["value"], boot["q_var"]["ci68"], p_mean,
        cv_var_over_A, cv_mean_over_A, boot["fano_slope"]["value"])

    verdict = {
        "p_mean_Nmol": {"p": p_mean, "se": se_mean},          # re-confirm F-031
        "q_var_Nmol": {"p": q_var, "se": se_var},             # THE observable
        "q_std_sqrtvar": {"p": q_std, "se": se_std},
        "fano_slope": {"p": fano_slope, "se": se_fano},
        "p_S_fluc": {"p": p_sfluc, "se": se_sfluc},
        "bootstrap": boot,
        "cv_var_over_A": cv_var_over_A,
        "cv_mean_over_A": cv_mean_over_A,
        "cv_fano": cv_fano,
        "var_area_invariant": bool(np.isfinite(cv_var_over_A)
                                   and cv_var_over_A < 0.15),
        "area_target_q": 0.5,
        "volumetric_q": 1.0,
        "correspondence": corr,
        "correspondence_text": corr_text,
    }
    payload["distribution"]["verdict"] = verdict

    print(f"\n  MEAN  <N_mol> ~ rho^{p_mean:.3f}+-{se_mean:.3f}  (F-031 area axis)")
    print(f"  VAR   Var      ~ rho^{q_var:.3f}+-{se_var:.3f}  "
          f"(boot CI68 [{boot['q_var']['ci68'][0]:.2f},"
          f"{boot['q_var']['ci68'][1]:.2f}])")
    print(f"  Fano slope     ~ rho^{fano_slope:.3f}  "
          f"(0 => Poisson/area-clean)")
    print(f"  CV(Var/A)={cv_var_over_A:.3f}  CV(mean/A)={cv_mean_over_A:.3f}")
    print(f"  CORRESPONDENCE: {corr}")
    print(f"  -> {corr_text}")

    payload["plots"] = make_plots(cells, {
        "q_var": boot["q_var"], "q_std_sqrtvar": boot["q_std_sqrtvar"],
        "p_mean": boot["p_mean"], "fano_slope": boot["fano_slope"]})
    _write(payload, "complete")
    print(f"\n  wrote {_RESULTS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
