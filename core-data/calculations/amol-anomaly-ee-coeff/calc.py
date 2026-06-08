# -*- coding: utf-8 -*-
"""amol-anomaly-ee-coeff (VYPOCET-35) -- H-B test: does the universal SSEE
coefficient c_EE match an anomaly rational built from the (a,c) central charges?

LOV-18-11-overlaps.md  H-B (flagship) + section 3.1 (exact test design).

PHYSICS BRIDGE (the (a,c) <-> EE link being probed):
  Trace-anomaly charges (a, c) govern UNIVERSAL entanglement-entropy terms:
    * Casini-Huerta-Myers (arXiv:1102.0440): the sphere EE universal coefficient
      of a CFT equals the a-charge (the F-quantity / sphere free energy).
    * Solodukhin (no repo bib entry -> marked unverified): the 4D logarithmic EE
      coefficient is a linear combination of (a, c) depending on the entangling
      surface geometry.
  Our discrete SSEE machinery (toe.entropy.ssee / ssee_scaling, and the F-029 dS
  static-patch area-law S_cap = A_horizon/(c_EE . G)) measures a DIMENSIONLESS
  universal coefficient c_EE.

  Anomaly side (EXACT, free, toe.ncg):
    * real scalar     -> (a, c) = (1/360, 1/120),  c/(-a) = -3   (DIRECT target:
                         our sprinkled field is a massless SCALAR)
    * one Weyl fermion -> (a, c) = (11/720, 1/40), c/(-a) = -18/11 (SECONDARY,
                         the index-protected NCG fermionic core)

THE QUESTION: does the measured c_EE (or 1/c_EE, or the full/trunc ratio) match
ANY pre-registered anomaly rational within CV (<5%)?
  * MATCH  -> extraordinary; the index core touches line B. Needs hardest scrutiny.
  * NO-MATCH (expected) -> c_EE is a GEOMETRIC kappa-cutoff coefficient, NOT an
    anomaly charge. A sharp, valuable negative that cleanly separates geometric
    from anomalous coefficients.

ANTI-CIRCULARITY (MANDATORY): the candidate rationals are PRE-REGISTERED and
written to results.json BEFORE any c_EE is measured. kappa = sqrt(N)/(4 pi) is
the Sorkin-Yazdi literature cutoff (1712.04227), not tuned. The F-029 dS c_EE was
measured in a PRIOR, independent run before this comparison existed.

Portability: all paths are __file__-relative. numpy/scipy/sympy only.
Atomic + progressive write: results.json is rewritten (tmp + os.replace) after
each stage so an interruption leaves a clean, valid partial output with `status`.
"""

from __future__ import annotations

import json
import os
import sys
import time
import tempfile

import numpy as np

# --- __file__-relative bootstrap (NO machine-absolute paths) ----------------
_HERE = os.path.dirname(os.path.abspath(__file__))
_REPO = os.path.normpath(os.path.join(_HERE, os.pardir, os.pardir, os.pardir))
_LIB = os.path.join(_REPO, "lib")
if _LIB not in sys.path:
    sys.path.insert(0, _LIB)

import sympy as sp  # noqa: E402

from toe.ncg import central_charges, a4_ratio, spectral_action_ratio  # noqa: E402
from toe.entropy import ssee_scaling, kappa_2d  # noqa: E402
from toe.causet import sprinkle_diamond2d  # noqa: E402

RESULTS_PATH = os.path.join(_HERE, "results.json")
PLOTS_DIR = os.path.join(_HERE, "plots")
PLOT_PATH = os.path.join(_HERE, "c_EE_vs_rationals.png")

# F-029 path: the ds-entropy-cap results.json (independent prior measurement).
DS_RESULTS = os.path.normpath(
    os.path.join(_HERE, os.pardir, "ds-entropy-cap", "results.json")
)

MATCH_TOL = 0.05  # 5% residual = "match" threshold (per LOV 3.1 / CV criterion)


# ---------------------------------------------------------------------------
# ATOMIC / PROGRESSIVE WRITE
# ---------------------------------------------------------------------------
def atomic_write(payload: dict) -> None:
    """Write payload to RESULTS_PATH atomically (tmp + os.replace)."""
    payload["_written_at"] = time.strftime("%Y-%m-%dT%H:%M:%S")
    fd, tmp = tempfile.mkstemp(dir=_HERE, suffix=".tmp")
    try:
        with os.fdopen(fd, "w") as f:
            json.dump(payload, f, indent=2, ensure_ascii=False, default=str)
        os.replace(tmp, RESULTS_PATH)
    finally:
        if os.path.exists(tmp):
            os.remove(tmp)


# ---------------------------------------------------------------------------
# STAGE 0 -- PRE-REGISTRATION (written BEFORE any measurement)
# ---------------------------------------------------------------------------
def build_preregistration() -> dict:
    """Compute the EXACT anomaly-side rationals and the pre-registered candidate
    list. This is computed from toe.ncg only -- NO entropy data is touched here.
    """
    a_s, c_s = central_charges(1, 0, 0)      # scalar (1/360, 1/120)
    a_w, c_w = central_charges(0, 1, 0)      # Weyl   (11/720, 1/40)
    ratio_scalar = sp.nsimplify(c_s / (-a_s))   # -3
    ratio_weyl = sp.nsimplify(c_w / (-a_w))     # -18/11
    sa_ratio = spectral_action_ratio().value    # -18/11
    a4r = a4_ratio(sector="fermion").value       # -18/11

    # Candidate rationals to compare the (positive) c_EE / 1/c_EE / ratio
    # against. Each carries an a-priori JUSTIFICATION. We register both the
    # SIGNED anomaly ratios and their absolute values, since c_EE is a positive
    # magnitude while c/(-a) is negative.
    candidates = [
        {
            "name": "3 (= |c/(-a)| scalar = 360*c_scalar = c_s/a_s)",
            "value": 3.0, "rational": "3",
            "justification": "DIRECT scalar anomaly magnitude |c/(-a)|=3; also "
                             "360*c_scalar=3 and c_scalar/a_scalar=3. Our field "
                             "is a massless scalar -> this is the PRIMARY target.",
            "tier": "primary-scalar",
        },
        {
            "name": "18/11 (= |c/(-a)| Weyl = NCG spectral-action ratio)",
            "value": float(sp.Rational(18, 11)), "rational": "18/11",
            "justification": "SECONDARY: index-protected NCG fermionic core "
                             "|alpha0/tau0|=|c_Weyl/(-a_Weyl)|=18/11 (F-003/F-014). "
                             "Match would mean the index core touches line B.",
            "tier": "secondary-fermion",
        },
        {
            "name": "8",
            "value": 8.0, "rational": "8",
            "justification": "Pre-registered round-number control (LOV 3.1 list). "
                             "No anomaly derivation -- a-priori null candidate near "
                             "the observed c_EE~7.6 to test for accidental match.",
            "tier": "control",
        },
        {
            "name": "12 (= a0/a2 per-mode ratio, lambda_induction_ledger)",
            "value": 12.0, "rational": "12",
            "justification": "Pre-registered (LOV 3.1). 12 = ratio_a0_over_a2 "
                             "per-mode (toe.ncg.lambda_induction_ledger) and the "
                             "11<->12 imprint (a_Weyl=11/720, c_Weyl=18/720).",
            "tier": "control",
        },
        {
            "name": "1/120 (= c_scalar)",
            "value": float(c_s), "rational": "1/120",
            "justification": "Raw scalar c-charge. Compared against c_EE, 1/c_EE.",
            "tier": "ac-built",
        },
        {
            "name": "1/360 (= a_scalar)",
            "value": float(a_s), "rational": "1/360",
            "justification": "Raw scalar a-charge (CHM: sphere-EE coefficient). "
                             "Compared against c_EE, 1/c_EE.",
            "tier": "ac-built",
        },
        {
            "name": "120 (= 1/c_scalar)",
            "value": 120.0, "rational": "120",
            "justification": "Inverse scalar c-charge; an (a,c)-built rational on "
                             "the same order channel as 1/c_EE.",
            "tier": "ac-built",
        },
        {
            "name": "360 (= 1/a_scalar)",
            "value": 360.0, "rational": "360",
            "justification": "Inverse scalar a-charge; (a,c)-built rational.",
            "tier": "ac-built",
        },
        {
            "name": "2*pi (= 6.283, A/4-adjacent geometric control)",
            "value": float(2 * np.pi), "rational": "2*pi",
            "justification": "GEOMETRIC (non-anomaly) control: if c_EE is a "
                             "kappa-cutoff geometric coefficient it should sit near "
                             "geometric constants, NOT anomaly rationals. Registered "
                             "to make the geometric/anomalous discrimination sharp.",
            "tier": "geometric-control",
        },
        {
            "name": "4 (= Bekenstein A/4 quarter)",
            "value": 4.0, "rational": "4",
            "justification": "GEOMETRIC control: the Bekenstein-Hawking 1/4 gives "
                             "c=4 if S=A/(4G). F-029 found c_EE~7.6 != 4 already.",
            "tier": "geometric-control",
        },
    ]
    return {
        "scalar_a": str(a_s), "scalar_c": str(c_s),
        "scalar_ratio_c_over_minus_a": str(ratio_scalar),           # -3
        "scalar_ratio_float": float(ratio_scalar),
        "weyl_a": str(a_w), "weyl_c": str(c_w),
        "weyl_ratio_c_over_minus_a": str(ratio_weyl),               # -18/11
        "weyl_ratio_float": float(ratio_weyl),
        "spectral_action_ratio": str(sa_ratio),                     # -18/11
        "a4_ratio_fermion": str(a4r),                               # -18/11
        "DIRECT_scalar_target": -3.0,
        "SECONDARY_fermion_target": float(ratio_weyl),
        "match_tolerance_frac": MATCH_TOL,
        "candidates": candidates,
        "anti_circularity": (
            "Candidates computed from toe.ncg ONLY (exact sympy). Written to "
            "results.json at stage 'preregistered' BEFORE any c_EE is read or "
            "measured. kappa=sqrt(N)/(4pi) is Sorkin-Yazdi 1712.04227 (not tuned)."
        ),
    }


# ---------------------------------------------------------------------------
# STAGE 1 -- c_EE channel A: reuse the F-029 dS static-patch value (PRIOR run)
# ---------------------------------------------------------------------------
def read_f029_cEE() -> dict:
    """Read the independently-measured c_EE from the F-029 ds-entropy-cap run.

    c_EE = 1 / R_full where R_full = S_full_cap / A_mol (PRIMARY A/4 channel).
    This was measured in a PRIOR run (VYPOCET-23/25) -> clean anti-circularity.
    """
    if not os.path.exists(DS_RESULTS):
        return {"available": False, "note": "ds-entropy-cap/results.json absent"}
    with open(DS_RESULTS) as f:
        d = json.load(f)
    disc = d.get("discriminator", {})
    prim = disc.get("PRIMARY_R_Sfull_over_Amol_density", {})
    R_list = prim.get("R", [])
    const = prim.get("constancy", {})
    R_mean = const.get("mean")
    R_cv = const.get("cv")
    if R_mean is None and R_list:
        R_mean = float(np.mean(R_list))
        R_cv = float(np.std(R_list) / np.mean(R_list))
    c_EE = (1.0 / R_mean) if R_mean else None
    # CV of c_EE = CV of R (first-order, 1/x).
    return {
        "available": True,
        "source": "ds-entropy-cap/results.json PRIMARY_R_Sfull_over_Amol_density",
        "R_full_mean": R_mean,
        "R_full_cv": R_cv,
        "R_full_per_rho": R_list,
        "c_EE": c_EE,
        "c_EE_cv": R_cv,
        "rho_grid": prim.get("rho", []),
        "note": "c_EE = 1/R_full; R_full = S_full_cap/A_mol (dS static patch, 2D). "
                "Independently measured in VYPOCET-23/25 (F-029), BEFORE this test.",
    }


# ---------------------------------------------------------------------------
# STAGE 2 -- c_EE channel B: fresh 2D causal-diamond SSEE area-law
# ---------------------------------------------------------------------------
def measure_diamond_cEE(time_budget_s: float, t0: float) -> dict:
    """Fresh 2D-diamond SSEE: dense N in [400,1800], 8 seeds, kappa-truncated.

    The 2D diamond SSEE obeys an area law S = c1 * ln(N) + c0 (the 2D "area" of a
    sub-interval is the log of the UV-cutoff ratio; Saravani-Sorkin-Yazdi
    1311.7146 / Sorkin-Yazdi 1611.10281). We extract:
      * the power-law exponent p (expected ~1/2 per F-006, a CONSISTENCY check),
      * a dimensionless area-law coefficient from a LOG fit S = c_log*ln(N)+b,
      * the full/trunc ratio (c_EE^full / c_EE^trunc) as an alternative channel.
    These are the candidate "universal coefficients" to test against the rationals.
    """
    Ns = [400, 600, 800, 1000, 1200, 1400, 1600, 1800]
    n_seeds = 8
    seed_base = 20260608

    # Cull any N that would blow the time budget: dense eigh is O(N^3); N<=1800
    # x 8 seeds x 8 N is comfortably within the ~20 min cap, but guard anyway.
    out = {"Ns": Ns, "n_seeds": n_seeds, "seed_base": seed_base,
           "frac": 0.5, "kappa_prescription": "sqrt(N)/(4 pi) (Sorkin-Yazdi)"}

    # --- kappa-truncated area law (universal, the physical channel) ---
    fit_trunc = ssee_scaling(
        sprinkle_diamond2d, Ns, frac=0.5,
        n_seeds=n_seeds, seed_base=seed_base, truncate="kappa",
    )
    out["powerlaw_exponent_trunc"] = float(fit_trunc.value)
    out["powerlaw_exponent_trunc_se"] = float(fit_trunc.se_regression)
    out["powerlaw_exponent_trunc_r2"] = float(fit_trunc.r2)
    out["powerlaw_exponent_trunc_ci68"] = list(fit_trunc.ci68_bootstrap)

    # Re-run the per-N/per-seed S to get the mean S(N) for the LOG-area fit and
    # to build c_EE candidates. ssee_scaling returns only the fit, so we redo the
    # cheap inner loop (it is the same deterministic seed scheme) to recover S(N).
    from toe.causet import green_retarded_2d, pauli_jordan
    from toe.sj import sj_state
    from toe.entropy import ssee, _causal_from_null, _subdiamond_idx

    S_trunc_mean = np.zeros(len(Ns))
    S_trunc_std = np.zeros(len(Ns))
    S_full_mean = np.zeros(len(Ns))
    S_full_std = np.zeros(len(Ns))
    per_seed_trunc = np.zeros((len(Ns), n_seeds))

    for i, N in enumerate(Ns):
        if time.time() - t0 > time_budget_s:
            out["TIME_BUDGET_HIT_at_N"] = N
            out["note_partial"] = "time budget reached; remaining N not measured"
            break
        kap = kappa_2d(N)
        st_trunc = np.zeros(n_seeds)
        st_full = np.zeros(n_seeds)
        for s in range(n_seeds):
            rng = np.random.default_rng(seed_base + 1000 * N + s)
            coords = sprinkle_diamond2d(N, rng)
            C = _causal_from_null(coords)
            iDelta = pauli_jordan(green_retarded_2d(C))
            state = sj_state(iDelta)
            sub_idx = _subdiamond_idx(coords, 0.5)
            m_trunc = ssee(state.W, iDelta, sub_idx, kappa=kap)
            m_full = ssee(state.W, iDelta, sub_idx, kappa=None)  # volume/untruncated
            st_trunc[s] = m_trunc.value
            st_full[s] = m_full.value
        S_trunc_mean[i] = st_trunc.mean()
        S_trunc_std[i] = st_trunc.std()
        S_full_mean[i] = st_full.mean()
        S_full_std[i] = st_full.std()
        per_seed_trunc[i] = st_trunc

    out["S_trunc_mean"] = S_trunc_mean.tolist()
    out["S_trunc_std"] = S_trunc_std.tolist()
    out["S_full_mean"] = S_full_mean.tolist()
    out["S_full_std"] = S_full_std.tolist()

    # --- LOG-area fit: S_trunc = c_log * ln(N) + b (2D area = ln of cutoff ratio) ---
    valid = S_trunc_mean > 0
    lnN = np.log(np.array(Ns, dtype=float)[valid])
    Sv = S_trunc_mean[valid]
    if valid.sum() >= 2:
        A = np.vstack([lnN, np.ones_like(lnN)]).T
        coef, res_, *_ = np.linalg.lstsq(A, Sv, rcond=None)
        c_log, b = float(coef[0]), float(coef[1])
        pred = A @ coef
        ss_res = float(np.sum((Sv - pred) ** 2))
        ss_tot = float(np.sum((Sv - Sv.mean()) ** 2))
        r2_log = 1.0 - ss_res / ss_tot if ss_tot > 0 else float("nan")
        # CV of c_log across seeds via per-seed log fits.
        c_log_seeds = []
        for s in range(n_seeds):
            ys = per_seed_trunc[valid, s]
            if np.all(ys > 0):
                cs = np.linalg.lstsq(A, ys, rcond=None)[0][0]
                c_log_seeds.append(float(cs))
        c_log_cv = (float(np.std(c_log_seeds) / np.abs(np.mean(c_log_seeds)))
                    if c_log_seeds and np.mean(c_log_seeds) != 0 else None)
    else:
        c_log, b, r2_log, c_log_cv = None, None, None, None

    out["c_log_2d_area"] = c_log
    out["c_log_intercept"] = b
    out["c_log_r2"] = r2_log
    out["c_log_cv_across_seeds"] = c_log_cv
    out["note_c_log"] = (
        "S_trunc = c_log*ln(N)+b. In 1+1 CFT the universal EE coeff is c/3 (Cardy); "
        "here c_log is the DISCRETE-SSEE analogue (not normalized to Cardy). The "
        "inverse 1/c_log is the candidate 'c_EE-like' coefficient on this channel."
    )
    out["inverse_c_log"] = (1.0 / c_log) if (c_log and abs(c_log) > 1e-12) else None

    # --- full/trunc ratio channel (LOV 3.1 explicitly lists this) ---
    with np.errstate(divide="ignore", invalid="ignore"):
        ratio_ft = np.where(S_trunc_mean > 0, S_full_mean / S_trunc_mean, np.nan)
    out["full_over_trunc_ratio_per_N"] = ratio_ft.tolist()
    finite_ratio = ratio_ft[np.isfinite(ratio_ft)]
    out["full_over_trunc_ratio_mean"] = (float(np.mean(finite_ratio))
                                         if finite_ratio.size else None)
    out["full_over_trunc_ratio_cv"] = (
        float(np.std(finite_ratio) / np.mean(finite_ratio))
        if finite_ratio.size and np.mean(finite_ratio) != 0 else None)
    out["note_full_trunc"] = (
        "full/trunc grows with N (full SSEE is volume-law, trunc is area-law) -> "
        "NOT a constant universal coefficient; reported for completeness per LOV 3.1."
    )
    return out


# ---------------------------------------------------------------------------
# STAGE 3 -- compare ALL c_EE channels against ALL pre-registered candidates
# ---------------------------------------------------------------------------
def compare_all(prereg: dict, cEE_channels: dict) -> dict:
    """For every measured c_EE channel value, compute the residual against EVERY
    pre-registered candidate. Report ALL comparisons (no p-hacking)."""
    comparisons = []
    for ch_name, ch_val, ch_cv in cEE_channels:
        if ch_val is None or not np.isfinite(ch_val):
            continue
        for cand in prereg["candidates"]:
            cv = cand["value"]
            if cv == 0:
                continue
            resid = abs(ch_val - cv) / abs(cv)
            comparisons.append({
                "channel": ch_name,
                "channel_value": float(ch_val),
                "channel_cv": ch_cv,
                "candidate": cand["name"],
                "candidate_value": float(cv),
                "candidate_tier": cand["tier"],
                "residual_frac": float(resid),
                "match_within_5pct": bool(resid < MATCH_TOL),
            })
    comparisons.sort(key=lambda x: x["residual_frac"])
    matches = [c for c in comparisons if c["match_within_5pct"]]
    return {
        "all_comparisons_sorted_by_residual": comparisons,
        "n_comparisons": len(comparisons),
        "matches_within_5pct": matches,
        "n_matches": len(matches),
        "best_match": comparisons[0] if comparisons else None,
    }


# ---------------------------------------------------------------------------
# PLOT
# ---------------------------------------------------------------------------
def make_plot(prereg: dict, cEE_channels: dict, comparison: dict) -> None:
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    os.makedirs(PLOTS_DIR, exist_ok=True)
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13, 5.5))

    # --- Panel 1: the c_EE~7.6 channel against candidates on a log axis ---
    cand_vals = [c["value"] for c in prereg["candidates"]]
    cand_names = [c["rational"] for c in prereg["candidates"]]
    tier_color = {"primary-scalar": "#d62728", "secondary-fermion": "#9467bd",
                  "control": "#7f7f7f", "ac-built": "#1f77b4",
                  "geometric-control": "#2ca02c"}
    colors = [tier_color.get(c["tier"], "#000") for c in prereg["candidates"]]
    ypos = np.arange(len(cand_vals))
    ax1.barh(ypos, cand_vals, color=colors, alpha=0.55)
    ax1.set_yticks(ypos)
    ax1.set_yticklabels(cand_names, fontsize=8)
    ax1.set_xscale("log")
    ax1.set_xlabel("value (log scale)")
    ax1.set_title("Pre-registered rationals (colored by tier)")
    # overlay the measured c_EE channels as vertical lines
    line_styles = ["-", "--", ":", "-."]
    for k, (ch_name, ch_val, ch_cv) in enumerate(cEE_channels):
        if ch_val is None or not np.isfinite(ch_val) or ch_val <= 0:
            continue
        ax1.axvline(ch_val, color="black", ls=line_styles[k % 4], lw=1.8,
                    label=f"{ch_name} = {ch_val:.3g}")
    ax1.legend(fontsize=7, loc="lower right")

    # --- Panel 2: residual matrix (channel x candidate), 5% line ---
    comps = comparison["all_comparisons_sorted_by_residual"]
    # focus on the primary c_EE channel (dS) for clarity
    prim_ch = "c_EE_dS_(1/R_full)"
    prim = [c for c in comps if c["channel"] == prim_ch]
    if not prim:
        prim = comps[:len(prereg["candidates"])]
    names = [c["candidate"].split(" ")[0] for c in prim]
    resids = [c["residual_frac"] * 100 for c in prim]
    cc = ["#d62728" if c["match_within_5pct"] else "#1f77b4" for c in prim]
    xp = np.arange(len(names))
    ax2.bar(xp, resids, color=cc, alpha=0.7)
    ax2.axhline(MATCH_TOL * 100, color="red", ls="--",
                label=f"{int(MATCH_TOL*100)}% match threshold")
    ax2.set_xticks(xp)
    ax2.set_xticklabels(names, rotation=55, ha="right", fontsize=7)
    ax2.set_ylabel("residual |c_EE - cand| / cand  [%]")
    ax2.set_title(f"Residuals: c_EE(dS)={cEE_channels[0][1]:.3f} vs candidates")
    ax2.set_yscale("log")
    ax2.legend(fontsize=8)

    fig.suptitle("H-B: universal SSEE coefficient c_EE vs anomaly rationals "
                 "(scalar c/(-a)=-3, Weyl=-18/11)", fontsize=11)
    fig.tight_layout(rect=(0, 0, 1, 0.96))
    fig.savefig(PLOT_PATH, dpi=130)
    plt.close(fig)


# ---------------------------------------------------------------------------
# MAIN
# ---------------------------------------------------------------------------
def main():
    t0 = time.time()
    TIME_BUDGET_S = 20 * 60  # 20 min cap (LOV budget)

    payload = {
        "schema_version": "1.0",
        "task": "VYPOCET-35 / amol-anomaly-ee-coeff -- H-B: does the universal "
                "SSEE coefficient c_EE match an anomaly rational from (a,c)?",
        "lov_ref": "LOV-18-11-overlaps.md H-B (flagship) + 3.1",
        "findings_ref": ["F-003", "F-014", "F-029"],
        "status": "preregistered",
        "toe_version": "0.3.0",
        "match_tolerance_frac": MATCH_TOL,
    }

    # --- STAGE 0: PRE-REGISTER (write BEFORE any measurement) ---
    payload["preregistration"] = build_preregistration()
    atomic_write(payload)  # <-- anti-circularity: candidates persisted first
    print("[stage 0] pre-registration written. DIRECT scalar target c/(-a) = -3; "
          "SECONDARY Weyl = -18/11.")

    # --- STAGE 1: c_EE channel A (F-029 dS, prior independent run) ---
    payload["status"] = "measuring_dS"
    f029 = read_f029_cEE()
    payload["cEE_channel_dS_F029"] = f029
    atomic_write(payload)
    c_dS = f029.get("c_EE")
    print(f"[stage 1] F-029 dS c_EE = {c_dS} (CV {f029.get('c_EE_cv')})")

    # --- STAGE 2: c_EE channel B (fresh 2D diamond) ---
    payload["status"] = "measuring_diamond"
    atomic_write(payload)
    diamond = measure_diamond_cEE(TIME_BUDGET_S, t0)
    payload["cEE_channel_diamond_2d"] = diamond
    atomic_write(payload)
    print(f"[stage 2] diamond: power-law p={diamond.get('powerlaw_exponent_trunc'):.4f}, "
          f"c_log={diamond.get('c_log_2d_area')}, 1/c_log={diamond.get('inverse_c_log')}")

    # --- STAGE 3: compare ALL channels vs ALL candidates ---
    payload["status"] = "comparing"
    atomic_write(payload)

    cEE_channels = [
        ("c_EE_dS_(1/R_full)", c_dS, f029.get("c_EE_cv")),
        ("R_full_dS", f029.get("R_full_mean"), f029.get("R_full_cv")),
        ("c_log_diamond_2d", diamond.get("c_log_2d_area"),
         diamond.get("c_log_cv_across_seeds")),
        ("inverse_c_log_diamond", diamond.get("inverse_c_log"),
         diamond.get("c_log_cv_across_seeds")),
        ("powerlaw_exponent_trunc", diamond.get("powerlaw_exponent_trunc"),
         None),
        ("full_over_trunc_ratio", diamond.get("full_over_trunc_ratio_mean"),
         diamond.get("full_over_trunc_ratio_cv")),
    ]
    comparison = compare_all(payload["preregistration"], cEE_channels)
    payload["comparison"] = comparison
    atomic_write(payload)

    # --- VERDICT ---
    n_match = comparison["n_matches"]
    best = comparison["best_match"]
    # Discriminate: does the PRIMARY dS c_EE match an ANOMALY-tier rational?
    anomaly_tiers = {"primary-scalar", "secondary-fermion", "ac-built"}
    ds_anomaly_matches = [
        m for m in comparison["matches_within_5pct"]
        if m["channel"] in ("c_EE_dS_(1/R_full)",) and m["candidate_tier"] in anomaly_tiers
    ]
    if ds_anomaly_matches:
        correspondence = "match"
        verdict_short = ("MATCH: the dS c_EE lands on an ANOMALY rational within 5% "
                         "-> the index core may touch line B. Requires hardest scrutiny.")
    elif n_match > 0 and best and best["candidate_tier"] in ("geometric-control",):
        correspondence = "no-match-geometric"
        verdict_short = ("NO ANOMALY MATCH: c_EE sits near a GEOMETRIC control, not "
                         "an anomaly rational -> c_EE is a geometric kappa-cutoff "
                         "coefficient, NOT an anomaly charge.")
    elif n_match > 0:
        correspondence = "partial"
        verdict_short = ("PARTIAL: some channel matches a control/round number but "
                         "the PRIMARY dS c_EE does NOT match an anomaly rational.")
    else:
        correspondence = "no-match-geometric"
        verdict_short = ("NO MATCH anywhere within 5% -> c_EE is not any pre-registered "
                         "anomaly rational; geometric coefficient.")

    payload["verdict"] = {
        "correspondence": correspondence,
        "summary": verdict_short,
        "dS_c_EE": c_dS,
        "dS_c_EE_cv": f029.get("c_EE_cv"),
        "best_match": best,
        "n_matches_within_5pct": n_match,
        "dS_anomaly_matches": ds_anomaly_matches,
        "DIRECT_scalar_target_c_over_minus_a": -3.0,
        "SECONDARY_fermion_target": float(sp.Rational(-18, 11)),
        "residual_dS_vs_scalar3": (abs(c_dS - 3.0) / 3.0) if c_dS else None,
        "residual_dS_vs_18_11": (abs(c_dS - 18 / 11) / (18 / 11)) if c_dS else None,
    }
    payload["status"] = "complete"
    payload["runtime_s"] = time.time() - t0
    atomic_write(payload)

    # --- PLOT ---
    try:
        make_plot(payload["preregistration"], cEE_channels, comparison)
        payload["plot"] = os.path.relpath(PLOT_PATH, _REPO)
        atomic_write(payload)
    except Exception as e:  # plotting must never corrupt the result
        payload["plot_error"] = str(e)
        atomic_write(payload)

    print(f"[done] correspondence = {correspondence}")
    print(f"       {verdict_short}")
    print(f"       best match: {best['candidate'] if best else None} "
          f"(resid {best['residual_frac']*100:.2f}%)" if best else "")
    print(f"       runtime {payload['runtime_s']:.1f}s")


if __name__ == "__main__":
    main()
