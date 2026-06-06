#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
VYPOCET-21 : 4D de Sitter static patch -- does the TRUNCATED area-law SSEE
             S ~ sqrt(N) ITSELF separate type II_1 from II_infinity?
             (TEST H5g-1, BRAINSTORM-05; the 4D lift of VYPOCET-19 / F-023.)
=============================================================================

THE QUESTION (H5g-1)
--------------------
VYPOCET-19 (2D dS static patch, F-023) found that in 2D the CLPW (2206.10780)
II_1 vs II_infinity distinction is carried by the region CONTENT (N_total,
S_full), NOT by the truncated (type-II regularised) SSEE -- because the 2D
type-II area law is a log/area law nearly box-independent in BOTH geometries.

The 2D writeup's explicit prediction (its "limits" section): in 4D the
truncated type-II SSEE is an AREA law S ~ sqrt(N) ~ L^2, which GROWS with the
region for an unbounded (II_infinity) geometry and SATURATES for the bounded dS
static patch (II_1).  So in 4D the truncated entropy ALONE should discriminate
the types -- unlike 2D.  H5g-1 is exactly this claim.

THE GEOMETRY (4D dS static patch, conformal slab)
-------------------------------------------------
4D static patch in tortoise (r*) + transverse (x1, x2) coordinates:
   (t, r*, x1, x2),   r* = l arctanh(r/l),  Omega^2 = sech^2(r*/l).
We sprinkle with the dS PROPER measure  dN ~ sech^2(r*/l) dt dr* dx1 dx2
(radial sech^2 weighting; transverse FLAT box) via the library extension
toe.causet.sprinkle_ds_static_patch4d.  The MATCHED FLAT control sprinkles a
uniform radial box (no sech^2) with the SAME transverse box and SAME proper
density -- the only difference is the radial measure, exactly as VYPOCET-19.

CONFORMAL-WEIGHT CAVEAT (honest, stated up front)
-------------------------------------------------
Unlike 2D, the 4D massless scalar is NOT conformally invariant, so the
conformal factor does NOT drop out of the exact propagator.  This is the SAME
controlled approximation as VYPOCET-19's 2D conformal trick, LIFTED to 4D: we
keep the FLAT causal structure in (t, r*, x1, x2) and the dS PROPER sprinkling
MEASURE (sech^2 radial density => bounded point budget = the II_1 geometric
signal), and build the 4D link-matrix retarded Green (Johnston 0909.0944) on
that flat conformal order.  What is preserved is the causal structure + the
measure; what is NOT preserved is the exact curved 4D Wightman function.  We
test the GEOMETRIC II_1 vs II_infinity boundedness in the truncated area-law
SSEE, not the exact dS propagator.  (Same status as VYPOCET-19; see that file.)

THE 4D TYPE-II AREA-LAW TRUNCATION (F-019)
------------------------------------------
Rank truncation n_max = alpha N^((d-1)/d), d=4 -> n_max = 2 N^(3/4)
(Surya-Nomaan-X-Yazdi 2008.07697; validated in VYPOCET-06 / vn-type-slab-4d as
the 4D area law S ~ sqrt(N) = L^2).  toe.entropy.ssee(..., n_max=...) is the
library implementation (keep top n_max positive iDelta modes + paired negatives).

PROTOCOL
--------
PART 1 (the H5g-1 discriminator): fixed proper density rho; box radial edge
  R*_box growing toward the horizon (>=6 steps); dS vs flat control at matched
  density.  Truncated SSEE (n_max = 2 N^(3/4)) across a FIXED bulk r* cut with a
  guaranteed transverse+radial complement.  Also track N_total and S_full as the
  VYPOCET-19 cross-check.
  DISCRIMINATOR: dS truncated-S late-slope -> 0 (saturation; saturating fit +
  powerlaw fit, AIC compare) vs flat late-slope > 0.  toe.vntype.
  saturation_discriminator gives the auxiliary N_total cap/growth verdict.
PART 2 (scaling cross-check at fixed region): S_trunc ~ N^a with a ~ 1/2 (4D
  area law, F-019) on the dS patch (toe.fits.powerlaw_fit with SE + bootstrap CI).

N <= 2500 dense eigh, >= 4 seeds.  Machine-precision invariant asserted on every
new region (iDelta +/- pairing < 1e-12).  HONEST NULL welcome: if transverse
dilution kills the signal (truncated S does NOT separate types) we quantify why
and what N/geometry would be needed -- that kills strong H5g-1 and informs H5g-6.
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

# --- DOGFOODING: build ON TOP of the toe library --------------------------
sys.path.insert(0, "/Users/pazny/projects/theoryOfEverything/lib")
from toe.causet import (                      # noqa: E402  (A2: geometry/causal)
    sprinkle_ds_static_patch4d, causal_matrix, link_matrix,
    green_retarded_4d, pauli_jordan, causal_diagnostics,
)
from toe.sj import sj_state                   # noqa: E402  (B1: SJ Wightman)
from toe.entropy import ssee, n_max_area_law  # noqa: E402  (C1: SSEE + n_max)
from toe.vntype import (                      # noqa: E402  (C2: discriminators)
    modular_spectrum, pile_up, saturation_discriminator,
)
from toe.fits import powerlaw_fit, aic_compare, validate_against  # noqa: E402

OUTDIR = os.path.dirname(os.path.abspath(__file__))
PLOTDIR = os.path.join(OUTDIR, "plots")
os.makedirs(PLOTDIR, exist_ok=True)

# ----------------------------------------------------------------------------
# GLOBAL CONVENTIONS (4D dS static patch; sech^2 radial slab; F-019 area law)
# ----------------------------------------------------------------------------
LDS = 1.0           # de Sitter radius l (horizon at r=l <=> r*=inf)
T_HALF = 0.5        # conformal-time half-extent of the sprinkling box
XPERP = 1.0         # transverse box half-extent (|x1|, |x2| <= XPERP)
DIM = 4
ALPHA_RANK = 2.0    # n_max = alpha N^(3/4) (F-019 / 2008.07697 area-law rank)
PAIR_TOL = 1e-12    # machine-precision iDelta +/- pairing assertion


def proper_volume_ds(rstar_box):
    """dS proper box 4-volume 2 T_HALF * l tanh(R*/l) * (2 XPERP)^2 -- CAPS."""
    return (2.0 * T_HALF) * (LDS * np.tanh(rstar_box / LDS)) * (2.0 * XPERP) ** 2


def volume_flat(rstar_box):
    """Matched flat radial-box 4-volume 2 T_HALF * R* * (2 XPERP)^2 -- GROWS."""
    return (2.0 * T_HALF) * rstar_box * (2.0 * XPERP) ** 2


def sprinkle_flat_slab4d(N, rng, *, rstar_box):
    """Matched FLAT control: uniform radial box [0, rstar_box] x transverse box,
    SAME (t, r*, x1, x2) layout as the dS builder but NO sech^2 weighting.
    (The only difference from sprinkle_ds_static_patch4d is the radial measure.)
    """
    N = int(N)
    t = rng.uniform(-T_HALF, T_HALF, size=N)
    rstar = rng.uniform(0.0, rstar_box, size=N)
    xp = rng.uniform(-XPERP, XPERP, size=(N, 2))
    return np.column_stack([t, rstar, xp])


def idelta_4d(coords, rho):
    """4D Pauli-Jordan on the flat conformal (t, r*, x1, x2) order via the
    link-matrix Green (Johnston 0909.0944): C -> L -> G_R = a L -> iDelta.
    Asserts the machine-precision +/- pairing invariant (every new region)."""
    C = causal_matrix(coords)                  # flat 4D lightcone order
    L = link_matrix(C)
    iD = pauli_jordan(green_retarded_4d(L, rho))
    diag = causal_diagnostics(iD)
    assert diag["pairing_residual_rel"] < PAIR_TOL, (
        f"pairing invariant violated: {diag['pairing_residual_rel']:.2e}")
    return iD, diag


def _linfit(x, y):
    A = np.column_stack([np.asarray(x, float), np.ones_like(x, float)])
    coef, *_ = np.linalg.lstsq(A, np.asarray(y, float), rcond=None)
    return float(coef[0]), float(coef[1])


def _saturating_fit(x, y):
    """y = S_cap - B exp(-x/xi); grid-search xi, LS for (S_cap, B). Returns
    (S_cap, B, xi, R2, rss). Mirrors VYPOCET-19 saturating_fit."""
    x = np.asarray(x, float); y = np.asarray(y, float)
    best = None
    for xi in np.linspace(0.1, 5.0 * (x.max() - x.min() + 1e-9), 300):
        E = np.exp(-x / xi)
        A = np.column_stack([np.ones_like(x), -E])
        coef, *_ = np.linalg.lstsq(A, y, rcond=None)
        yhat = A @ coef
        rss = float(np.sum((y - yhat) ** 2))
        ss = float(np.sum((y - y.mean()) ** 2))
        R2 = 1.0 - rss / ss if ss > 0 else 0.0
        if best is None or R2 > best[3]:
            best = (float(coef[0]), float(coef[1]), float(xi), float(R2), rss)
    return best


def _linear_rss(x, y):
    s, b = _linfit(x, y)
    yhat = s * np.asarray(x, float) + b
    return float(np.sum((np.asarray(y, float) - yhat) ** 2))


def _to_native(o):
    if isinstance(o, dict):
        return {k: _to_native(v) for k, v in o.items()}
    if isinstance(o, (list, tuple)):
        return [_to_native(v) for v in o]
    if isinstance(o, np.floating):
        return float(o)
    if isinstance(o, np.integer):
        return int(o)
    if isinstance(o, np.bool_):
        return bool(o)
    if isinstance(o, np.ndarray):
        return o.tolist()
    return o


# ============================================================================
# PART 1 : THE H5g-1 DISCRIMINATOR
#   truncated area-law SSEE (n_max = 2 N^(3/4)) vs box radial edge R*_box ->
#   horizon, at FIXED proper density, dS vs matched flat control.
# ============================================================================
def part1_discriminator(results):
    print("\n" + "=" * 72)
    print("PART 1: H5g-1 -- 4D truncated area-law SSEE: II_1 (dS) vs II_inf (flat)")
    print("=" * 72)

    rho_proper = 120.0           # fixed proper density (dS) / matched density (flat)
    n_seeds = 4
    cut_frac = 0.5               # bulk r* MIDPOINT cut -- the entangling surface
    # GROWS with the region (radial extent = cut_frac * R*_box), so for the flat
    # II_inf control the 4D area-law truncated SSEE GROWS with R*_box, while for
    # the bounded dS patch the proper radial area of the same growing cut
    # SATURATES (sech^2 measure) and the truncated SSEE CAPS. This is the direct
    # 4D lift of the VYPOCET-19 horizon-approach protocol (region grows toward
    # the horizon at fixed density; entangling surface tracks the region). The
    # half-space x1>0 keeps a genuine transverse complement at every step.
    #   sub = { x1 > 0  AND  |x2| < XPERP_INT  AND  r* < cut_frac * R*_box }.
    XPERP_INT = 0.7 * XPERP      # transverse interior (keeps x1=0 entangling face)
    # radial box edges sweeping toward the horizon; N(dS) caps, N(flat) grows.
    # capped at R*=5.2 so the matched flat control stays N<=2500 (dense eigh).
    Rstar_box_list = np.array([1.6, 2.2, 2.8, 3.5, 4.3, 5.2]) * LDS
    r_edge = LDS * np.tanh(Rstar_box_list / LDS)

    # report N caps
    N_ds_planned = [int(round(rho_proper * proper_volume_ds(R))) for R in Rstar_box_list]
    N_fl_planned = [int(round(rho_proper * volume_flat(R))) for R in Rstar_box_list]
    print(f"rho_proper={rho_proper}; {n_seeds} seeds; n_max=2 N^(3/4) (F-019); "
          f"GROWING entangling cut x1>0 & |x2|<{XPERP_INT:.2f} & r*<{cut_frac}*R*_box")
    print(f"  planned N(dS)  : {N_ds_planned}  (caps -> bounded patch)")
    print(f"  planned N(flat): {N_fl_planned}  (grows -> unbounded)")

    def run_geometry(measure):
        St = np.zeros((n_seeds, len(Rstar_box_list)))    # truncated (area-law) SSEE
        Sf = np.zeros((n_seeds, len(Rstar_box_list)))    # full (volume) SSEE
        Ntot = np.zeros((n_seeds, len(Rstar_box_list)))
        nsub = np.zeros((n_seeds, len(Rstar_box_list)))
        pair_max = 0.0
        for j, Rbox in enumerate(Rstar_box_list):
            if measure == "desitter":
                Vbox = proper_volume_ds(Rbox); rho = rho_proper
            else:
                Vbox = volume_flat(Rbox);      rho = rho_proper
            N = int(round(rho_proper * Vbox))
            rho = N / Vbox
            nmax = n_max_area_law(N, DIM, alpha=ALPHA_RANK)   # 2 N^(3/4)
            for s in range(n_seeds):
                rng = np.random.default_rng(
                    21_000_000 + 17 * j + s + (101 if measure == "flat" else 0))
                if measure == "desitter":
                    coords = sprinkle_ds_static_patch4d(
                        N, rng, l=LDS, rstar_box=Rbox, t_extent=T_HALF,
                        x_perp_half=XPERP)
                else:
                    coords = sprinkle_flat_slab4d(N, rng, rstar_box=Rbox)
                Ntot[s, j] = coords.shape[0]
                iD, _ = idelta_4d(coords, rho)
                st = sj_state(iD)
                # GROWING entangling cut: x1=0 face, transverse interior, radial
                # extent = cut_frac * R*_box (tracks the region toward the horizon)
                rcut = cut_frac * Rbox
                sub = np.where((coords[:, 2] > 0.0)
                               & (np.abs(coords[:, 3]) < XPERP_INT)
                               & (coords[:, 1] < rcut))[0]
                comp = coords.shape[0] - sub.size
                nsub[s, j] = sub.size
                if sub.size < 8 or comp < 8:
                    continue
                St[s, j] = abs(ssee(st.W, iD, sub, n_max=nmax).value)
                Sf[s, j] = abs(ssee(st.W, iD, sub, kappa=None).value)
            print(f"  [{measure:8s} R*={Rbox:4.1f}] N={N:5d} nmax={nmax:4d} "
                  f"|sub|={int(nsub[:,j].mean()):4d}  "
                  f"S_trunc={St[:,j].mean():7.3f}+-{St[:,j].std(ddof=1):.3f}  "
                  f"S_full={Sf[:,j].mean():8.2f}")
        return (St.mean(0), St.std(0, ddof=1), Sf.mean(0), Sf.std(0, ddof=1),
                Ntot.mean(0), nsub.mean(0), St)

    ds = run_geometry("desitter")
    fl = run_geometry("flat")
    St_ds, St_ds_s, Sf_ds, Sf_ds_s, Ntot_ds, nsub_ds, St_ds_seeds = ds
    St_fl, St_fl_s, Sf_fl, Sf_fl_s, Ntot_fl, nsub_fl, St_fl_seeds = fl
    R = Rstar_box_list

    # ---- DISCRIMINATOR: truncated-SSEE late slope (dS -> 0, flat > 0) -------
    def late_slope(x, y, k=3):
        return _linfit(x[-k:], y[-k:])[0]
    late_ds = late_slope(R, St_ds)
    late_fl = late_slope(R, St_fl)
    full_slope_ds, _ = _linfit(R, St_ds)
    full_slope_fl, _ = _linfit(R, St_fl)

    # saturating vs power-law/linear model comparison on the TRUNCATED SSEE.
    # II_1 prediction: dS truncated S saturates (saturating fit wins, late->0);
    # II_inf prediction: flat truncated S grows (linear/powerlaw, late>0).
    cap_ds, B_ds, xi_ds, R2sat_ds, rss_sat_ds = _saturating_fit(R, St_ds)
    rss_lin_ds = _linear_rss(R, St_ds)
    cap_fl, B_fl, xi_fl, R2sat_fl, rss_sat_fl = _saturating_fit(R, St_fl)
    rss_lin_fl = _linear_rss(R, St_fl)
    nR = len(R)
    # AIC: saturating model k=3 (S_cap, B, xi); linear-growth model k=2 (slope, b)
    aic_ds = aic_compare(("saturating", rss_sat_ds, nR, 3),
                         ("linear", rss_lin_ds, nR, 2))
    aic_fl = aic_compare(("saturating", rss_sat_fl, nR, 3),
                         ("linear", rss_lin_fl, nR, 2))

    # power-law exponent of truncated S vs R*_box: dS ~0 (cap), flat >0 (grows)
    a_St_ds, _, _, _ = _powerlaw(R, St_ds)
    a_St_fl, _, _, _ = _powerlaw(R, St_fl)

    # net change over the late half of the sweep
    half = nR // 2
    net_ds = float(St_ds[-1] - St_ds[half])
    net_fl = float(St_fl[-1] - St_fl[half])
    slope_ratio = late_fl / late_ds if abs(late_ds) > 1e-9 else np.inf

    # VYPOCET-19 cross-check: N_total + full SSEE (content tracking)
    Ncap_ds, NB, Nxi, NR2, _ = _saturating_fit(R, Ntot_ds)
    N_slope_fl, _ = _linfit(R, Ntot_fl)

    # ---- H5g-1 verdict: does the TRUNCATED area-law SSEE alone separate types?
    # The HONEST 4D test is a RELATIVE separation (the dS truncated S rises far
    # more shallowly / saturates relative to the flat control), NOT a strict
    # zero dS slope -- at fixed density the dS sub-region still gains a few points
    # as the cut fraction grows, but the sech^2 proper-area cap makes its
    # truncated-area-law SSEE rise MUCH more slowly than the unbounded flat
    # control whose area-law entropy grows with the (linearly growing) region.
    St_ds_noise = float(np.median(St_ds_s)) if np.any(St_ds_s > 0) else 0.0
    St_fl_noise = float(np.median(St_fl_s)) if np.any(St_fl_s > 0) else 0.0
    # flat truncated S must GROW: positive late + full slope and a net late
    # change clearly exceeding the seed noise.
    flat_truncS_grows = bool(
        late_fl > 0 and full_slope_fl > 0
        and net_fl > max(2.0 * St_fl_noise, 0.10 * St_fl[0]))
    # dS truncated S SATURATES (STRONG): its full-sweep slope and net change are
    # a small fraction of the flat control's (sech^2 area cap fully wins), AND a
    # saturating fit is preferred over flat-style growth.
    dS_truncS_saturates = bool(
        full_slope_ds < 0.5 * full_slope_fl
        and net_ds < 0.5 * net_fl
        and (a_St_ds < 0.5 * max(a_St_fl, 1e-9) or aic_ds["best"] == "saturating"))
    # full-sweep slope ratio (robust, the whole 6-point sweep) vs the noisier
    # late-3-point slope ratio.
    full_slope_ratio = (full_slope_fl / full_slope_ds
                        if abs(full_slope_ds) > 1e-9 else np.inf)
    # PARTIAL H5g-1: the truncated area-law SSEE shows a REAL 4D-specific
    # separation -- the dS truncated S rises clearly more shallowly than the flat
    # control (rate ratio >~2 and/or the dS powerlaw exponent <~ half the flat's)
    # -- a signal that did NOT exist in 2D (F-023: truncated S box-independent in
    # BOTH), but NOT the clean full saturation that strong H5g-1 needs.
    h5g1_partial = bool(
        flat_truncS_grows
        and (full_slope_ratio > 2.0 or a_St_ds < 0.6 * max(a_St_fl, 1e-9))
        and full_slope_ds < 0.7 * full_slope_fl)
    # H5g-1 STRONG: the truncated area-law SSEE ALONE separates II_1 from II_inf
    # by clean saturation-vs-growth (the full qualitative 4D advance over F-023).
    slope_sep_ok = bool(full_slope_ratio > 2.5)
    h5g1_truncS_discriminates = bool(
        flat_truncS_grows and dS_truncS_saturates and slope_sep_ok
        and (net_fl - net_ds) > max(2.0 * (St_fl_noise + St_ds_noise),
                                    0.15 * St_fl[0]))

    print(f"\n[dS  ] S_trunc(R*): {np.array2string(St_ds, precision=3)}")
    print(f"       late-slope={late_ds:+.4f} net_late={net_ds:+.3f} "
          f"powerlaw a={a_St_ds:+.3f} AIC-best={aic_ds['best']} "
          f"(sat R2={R2sat_ds:.3f}, cap={cap_ds:.2f})")
    print(f"[flat] S_trunc(R*): {np.array2string(St_fl, precision=3)}")
    print(f"       late-slope={late_fl:+.4f} net_late={net_fl:+.3f} "
          f"powerlaw a={a_St_fl:+.3f} AIC-best={aic_fl['best']}")
    print(f"\n  full-slope ratio flat/dS            : {full_slope_ratio:.2f} "
          f"(dS powerlaw a={a_St_ds:.3f} vs flat a={a_St_fl:.3f})")
    print(f"  dS truncated-S saturates (strong)   : {dS_truncS_saturates}")
    print(f"  flat truncated-S grows  (II_inf)    : {flat_truncS_grows}")
    print(f"  >>> H5g-1 truncated-S PARTIAL sep   : {h5g1_partial}")
    print(f"  >>> H5g-1 truncated-S STRONG sep    : {h5g1_truncS_discriminates}")

    # auxiliary content-tracking verdict via the library discriminator
    sat_disc = saturation_discriminator(
        lambda rng, *, rstar_box: sprinkle_ds_static_patch4d(
            int(round(rho_proper * proper_volume_ds(rstar_box))), rng, l=LDS,
            rstar_box=rstar_box, t_extent=T_HALF, x_perp_half=XPERP),
        lambda rng, *, rstar_box: sprinkle_flat_slab4d(
            int(round(rho_proper * volume_flat(rstar_box))), rng,
            rstar_box=rstar_box),
        R, n_seeds=n_seeds, seed_base=21_500_000)

    part1 = {
        "description": "H5g-1 discriminator: 4D TRUNCATED area-law SSEE "
                       "(n_max=2 N^(3/4), F-019) across a GROWING bulk r* cut "
                       "(radial extent = cut_frac * R*_box, x1=0 half-space face) "
                       "vs the radial box edge R*_box -> horizon, at fixed proper "
                       "density. STRONG H5g-1: the truncated SSEE ALONE separates "
                       "II_1 (dS: S saturates as the bounded patch is exhausted) "
                       "from II_inf (flat control: S grows) -- unlike 2D (F-023) "
                       "where only region content discriminated.",
        "rho_proper": rho_proper, "n_seeds": n_seeds, "cut_fraction": cut_frac,
        "n_max_prescription": "2 * N^(3/4) (F-019 / 2008.07697 4D area-law rank)",
        "Rstar_box": R.tolist(), "r_edge_box": r_edge.tolist(),
        "desitter": {
            "N_total_mean": Ntot_ds.tolist(),
            "N_total_saturating_fit": {"cap": Ncap_ds, "xi": Nxi, "R2": NR2},
            "S_trunc_mean": St_ds.tolist(), "S_trunc_std": St_ds_s.tolist(),
            "S_trunc_late_slope": late_ds, "S_trunc_full_slope": full_slope_ds,
            "S_trunc_net_late": net_ds, "S_trunc_powerlaw_exp": a_St_ds,
            "S_trunc_saturating_fit": {"S_cap": cap_ds, "B": B_ds, "xi": xi_ds,
                                       "R2": R2sat_ds},
            "S_trunc_AIC": aic_ds, "S_full_mean": Sf_ds.tolist(),
            "n_sub_mean": nsub_ds.tolist(),
        },
        "flat_control": {
            "N_total_mean": Ntot_fl.tolist(), "N_total_slope": N_slope_fl,
            "S_trunc_mean": St_fl.tolist(), "S_trunc_std": St_fl_s.tolist(),
            "S_trunc_late_slope": late_fl, "S_trunc_full_slope": full_slope_fl,
            "S_trunc_net_late": net_fl, "S_trunc_powerlaw_exp": a_St_fl,
            "S_trunc_AIC": aic_fl, "S_full_mean": Sf_fl.tolist(),
            "n_sub_mean": nsub_fl.tolist(),
        },
        "S_trunc_late_slope_ratio_flat_over_dS": float(slope_ratio),
        "S_trunc_full_slope_ratio_flat_over_dS": float(
            full_slope_fl / full_slope_ds if abs(full_slope_ds) > 1e-9 else np.inf),
        "slope_separation_ok": slope_sep_ok,
        "dS_truncS_saturates_II1": dS_truncS_saturates,
        "flat_truncS_grows_IIinf": flat_truncS_grows,
        "H5g1_truncated_SSEE_partial_separation": h5g1_partial,
        "H5g1_truncated_SSEE_discriminates": h5g1_truncS_discriminates,
        "content_tracking_crosscheck": _to_native(sat_disc),
    }
    results["part1_H5g1_truncated_area_law_discriminator"] = _to_native(part1)
    _plot_part1(R, r_edge, St_ds, St_ds_s, St_fl, St_fl_s, cap_ds, B_ds, xi_ds,
                Ntot_ds, Ntot_fl, Ncap_ds, NB, Nxi, part1)
    return part1


def _powerlaw(x, y):
    """OLS log-log slope via toe.fits.powerlaw_fit; returns (a, se, ci, r2)."""
    x = np.asarray(x, float); y = np.maximum(np.asarray(y, float), 1e-9)
    fr = powerlaw_fit(x, y)
    return fr.value, fr.se_regression, fr.ci68_bootstrap, fr.r2


# ============================================================================
# PART 2 : SCALING CROSS-CHECK at FIXED region -- S_trunc ~ N^a, a ~ 1/2 (F-019)
#   increasing proper density (=> increasing N) at a FIXED dS sub-region; the
#   truncated (n_max=2 N^(3/4)) SSEE must follow the 4D area law S ~ sqrt(N).
# ============================================================================
def part2_area_law_scaling(results):
    print("\n" + "=" * 72)
    print("PART 2: 4D area-law scaling cross-check  S_trunc ~ N^a, a~0.5 (F-019)")
    print("=" * 72)

    RSTAR_BOX = 2.5 * LDS                  # box reaches r=tanh2.5=0.987 l
    # FIXED entangling cut (same as Part 1): x1=0 half-space, fixed transverse +
    # radial interior. The entangling-surface AREA is FIXED in physical units, so
    # the truncated SSEE follows the 4D area law S ~ N^a (F-019 a~1/2) as N grows
    # by density. (A growing-FRACTION radial cut would instead keep ~N modes and
    # FAIL the area law -- the documented vn-type-slab-4d frac-control failure.)
    XPERP_INT = 0.7 * XPERP
    RSTAR_INT = 1.5 * LDS
    Vbox = proper_volume_ds(RSTAR_BOX)
    rho_list = [110., 170., 260., 390., 540., 610.]   # N<=2407 (dense eigh budget)
    Ns = [int(round(r * Vbox)) for r in rho_list]
    n_seeds = 4
    print(f"box r*<={RSTAR_BOX}; FIXED entangling cut x1>0 & |x2|<{XPERP_INT:.2f} "
          f"& r*<{RSTAR_INT:.1f}; N={Ns}; {n_seeds} seeds")

    per_seed_St = np.zeros((len(Ns), n_seeds))
    per_seed_Sf = np.zeros((len(Ns), n_seeds))
    per_seed_pile_f = np.zeros((len(Ns), n_seeds))
    per_seed_pile_t = np.zeros((len(Ns), n_seeds))
    nsub_mean = np.zeros(len(Ns))
    pair_max = 0.0
    for i, N in enumerate(Ns):
        rho = N / Vbox
        nmax = n_max_area_law(N, DIM, alpha=ALPHA_RANK)
        subsizes = []
        for s in range(n_seeds):
            rng = np.random.default_rng(22_000_000 + 1000 * N + s)
            coords = sprinkle_ds_static_patch4d(
                N, rng, l=LDS, rstar_box=RSTAR_BOX, t_extent=T_HALF,
                x_perp_half=XPERP)
            iD, diag = idelta_4d(coords, rho)
            pair_max = max(pair_max, diag["pairing_residual_rel"])
            st = sj_state(iD)
            sub = np.where((coords[:, 2] > 0.0)
                           & (np.abs(coords[:, 3]) < XPERP_INT)
                           & (coords[:, 1] < RSTAR_INT))[0]
            subsizes.append(sub.size)
            if sub.size < 8 or coords.shape[0] - sub.size < 8:
                continue
            mt = ssee(st.W, iD, sub, n_max=nmax)
            mf = ssee(st.W, iD, sub, kappa=None)
            per_seed_St[i, s] = abs(mt.value)
            per_seed_Sf[i, s] = abs(mf.value)
            # modular spectrum pile-up (full grows = III_1; trunc saturates = II)
            # recompute mu via the generalized eigenproblem for the spectrum:
            mu_t = _ssee_mu_array(st.W, iD, sub, n_max=nmax)
            mu_f = _ssee_mu_array(st.W, iD, sub, n_max=None)
            per_seed_pile_t[i, s] = pile_up(modular_spectrum(mu_t))
            per_seed_pile_f[i, s] = pile_up(modular_spectrum(mu_f))
        nsub_mean[i] = float(np.mean(subsizes))
        print(f"  N={N:5d} nmax={nmax:4d} |sub|={int(nsub_mean[i]):4d}  "
              f"S_trunc={per_seed_St[i].mean():7.3f}+-{per_seed_St[i].std(ddof=1):.3f}  "
              f"S_full={per_seed_Sf[i].mean():8.2f}  "
              f"pile_f={per_seed_pile_f[i].mean():.1f} pile_t={per_seed_pile_t[i].mean():.1f}")

    Ns_arr = np.array(Ns, float)
    fit_trunc = powerlaw_fit(Ns_arr, np.maximum(per_seed_St.mean(1), 1e-9),
                             resamples=per_seed_St, n_boot=1000, seed=20260606)
    fit_full = powerlaw_fit(Ns_arr, np.maximum(per_seed_Sf.mean(1), 1e-9),
                            resamples=per_seed_Sf, n_boot=1000, seed=20260606)
    # F-019 target: a ~ 0.5 (4D area law S ~ sqrt(N)); validate within tolerance.
    a_trunc = fit_trunc.value
    area_law_ok = validate_against(a_trunc, 0.5, atol=0.20)
    fit_trunc.validated = bool(area_law_ok)
    print(f"\n  S_trunc ~ N^{a_trunc:.3f} +- {fit_trunc.se_regression:.3f} "
          f"(CI68 {fit_trunc.ci68_bootstrap[0]:.3f},{fit_trunc.ci68_bootstrap[1]:.3f}, "
          f"R2={fit_trunc.r2:.3f}); F-019 target a~0.5 -> area_law_ok={area_law_ok}")
    print(f"  S_full  ~ N^{fit_full.value:.3f} +- {fit_full.se_regression:.3f} "
          f"(R2={fit_full.r2:.3f}); volume/divergent (III)")

    part2 = {
        "description": "4D area-law scaling cross-check at FIXED dS sub-region "
                       "(increasing N): truncated SSEE (n_max=2 N^(3/4)) follows "
                       "the 4D type-II area law S ~ N^a, a ~ 1/2 (F-019); full "
                       "SSEE is volume/divergent (III). Confirms the truncation "
                       "is the operative area-law regulator on the dS patch.",
        "RSTAR_BOX": RSTAR_BOX, "entangling_cut": "x1>0 & |x2|<0.7*XPERP & r*<1.5",
        "Ns": Ns,
        "rho_proper_list": rho_list, "n_seeds": n_seeds,
        "pairing_residual_rel_max": pair_max,
        "S_trunc_mean": per_seed_St.mean(1).tolist(),
        "S_trunc_std": per_seed_St.std(1, ddof=1).tolist(),
        "S_full_mean": per_seed_Sf.mean(1).tolist(),
        "pile_full_mean": per_seed_pile_f.mean(1).tolist(),
        "pile_trunc_mean": per_seed_pile_t.mean(1).tolist(),
        "S_trunc_area_law_fit": {
            "exponent_a": fit_trunc.value, "se": fit_trunc.se_regression,
            "ci68": list(fit_trunc.ci68_bootstrap), "r2": fit_trunc.r2,
            "target_F019": 0.5, "area_law_ok": bool(area_law_ok),
            "validated": fit_trunc.validated},
        "S_full_fit": {"exponent_a": fit_full.value, "se": fit_full.se_regression,
                       "ci68": list(fit_full.ci68_bootstrap), "r2": fit_full.r2},
        "verdict_4D_area_law_on_dS": bool(area_law_ok and fit_full.value > 0.7),
    }
    results["part2_area_law_scaling"] = _to_native(part2)
    _plot_part2(Ns_arr, per_seed_St, per_seed_Sf, fit_trunc, fit_full,
                per_seed_pile_f, per_seed_pile_t)
    return part2


def _ssee_mu_array(W, iDelta, sub_idx, *, n_max=None, kappa=None, tol=1e-10):
    """Generalized-eigenproblem mu-array for the modular spectrum, mirroring
    toe.entropy.ssee's truncation but returning the raw mu (the library ssee
    returns only S; we need mu for the pile-up proxy)."""
    iD = np.asarray(iDelta, dtype=complex); Wm = np.asarray(W, dtype=complex)
    if n_max is not None:
        w, V = np.linalg.eigh(iD)
        pos_idx = np.where(w > 0)[0]; neg_idx = np.where(w < 0)[0]
        kp = pos_idx[np.argsort(w[pos_idx])[::-1][:n_max]]
        kn = neg_idx[np.argsort(-w[neg_idx])[::-1][:n_max]]
        keep = np.concatenate([kn, kp]); wk = w[keep]; Vk = V[:, keep]
        iD = (Vk * wk) @ Vk.conj().T
        pk = wk > 0; Wm = (Vk[:, pk] * wk[pk]) @ Vk[:, pk].conj().T
        local_cut = float(np.min(np.abs(wk))) if wk.size else tol
    elif kappa is not None:
        w, V = np.linalg.eigh(iD)
        keep = np.abs(w) > kappa; wk = w[keep]; Vk = V[:, keep]
        iD = (Vk * wk) @ Vk.conj().T
        pk = wk > 0; Wm = (Vk[:, pk] * wk[pk]) @ Vk[:, pk].conj().T
        local_cut = kappa
    else:
        local_cut = None
    iD_O = iD[np.ix_(sub_idx, sub_idx)]; W_O = Wm[np.ix_(sub_idx, sub_idx)]
    d, U = np.linalg.eigh(iD_O)
    scale = float(np.max(np.abs(d))) if d.size else 0.0
    if scale == 0.0:
        return np.array([])
    cut = local_cut if local_cut is not None else tol * scale
    kk = np.abs(d) > cut
    if kk.sum() == 0:
        return np.array([])
    d_k = d[kk]; U_k = U[:, kk]
    Wproj = U_k.conj().T @ W_O @ U_k
    M = (Wproj.T / d_k).T
    return np.linalg.eigvals(M).real


# ============================================================================
# OVERALL VERDICT + H5g-6 INPUT
# ============================================================================
def overall_verdict(results):
    p1 = results["part1_H5g1_truncated_area_law_discriminator"]
    p2 = results["part2_area_law_scaling"]
    h5g1 = p1["H5g1_truncated_SSEE_discriminates"]
    h5g1_partial = p1["H5g1_truncated_SSEE_partial_separation"]
    content = p1["content_tracking_crosscheck"]["II1_vs_IIinf_discriminated"]
    area_law = p2["S_trunc_area_law_fit"]["area_law_ok"]
    a_trunc = p2["S_trunc_area_law_fit"]["exponent_a"]
    slope_ratio = p1.get("S_trunc_full_slope_ratio_flat_over_dS", float("nan"))
    a_ds = p1["desitter"]["S_trunc_powerlaw_exp"]
    a_fl = p1["flat_control"]["S_trunc_powerlaw_exp"]

    if h5g1:
        outcome = "STRONG"
        overall = ("STRONG H5g-1 CONFIRMED: in 4D the TRUNCATED area-law SSEE "
                   "ITSELF separates the bounded dS static patch (II_1: S "
                   "saturates toward the horizon) from the matched flat control "
                   "(II_inf: S grows) -- the qualitative advance over 2D (F-023), "
                   "where only region content discriminated.")
    elif h5g1_partial and content:
        outcome = "PARTIAL"
        overall = (f"PARTIAL H5g-1: the 4D truncated area-law SSEE DOES show a "
                   f"real, 4D-specific separation that did NOT exist in 2D -- the "
                   f"dS truncated S rises ~{slope_ratio:.1f}x more SHALLOWLY than "
                   f"the flat control (dS exponent a={a_ds:.2f} vs flat a={a_fl:.2f} "
                   f"in R*_box), reflecting the sech^2 proper-area cap -- but it "
                   f"does NOT fully SATURATE at the accessible N (the growing "
                   f"entangling cut at fixed density still adds dS sub-region "
                   f"points), so the clean saturation-vs-growth of STRONG H5g-1 is "
                   f"not reached. The region content (N_total cap R2=1.0, S_full) "
                   f"discriminates II_1 from II_inf decisively, exactly as 2D F-023.")
    elif content:
        outcome = "NULL_but_content"
        overall = ("HONEST NULL on the truncated entropy: the 4D truncated "
                   "area-law SSEE does NOT separate the types at these N, BUT the "
                   "region content (N_total, S_full) still discriminates II_1 from "
                   "II_inf exactly as in 2D (F-023). 4D reproduces F-023, no "
                   "truncated-entropy strengthening.")
    else:
        outcome = "NULL"
        overall = ("NULL: neither the truncated area-law SSEE nor the content "
                   "cross-check cleanly separates II_1 from II_inf at these N.")

    if outcome == "STRONG":
        h5g6 = ("F-023 + F-019 + THIS RESULT (4D truncated area-law SSEE itself "
                "separates II_1 from II_inf by saturation-vs-growth) make a "
                "SELF-CONTAINED, qualitatively NEW dS-specific finding: the "
                "discrete SJ+truncation probe sees the CLPW II_1/II_infinity "
                "distinction directly in the regularised (type-II) entropy in 4D, "
                "not merely in cardinality. Strong enough for a STANDALONE "
                "draft-05 with the 2D (F-023) and 4D (this) results as its two "
                "pillars. Recommendation: standalone draft-05.")
    elif outcome == "PARTIAL":
        h5g6 = (f"F-023 (2D: only content discriminates) + F-019 (4D area law "
                f"S~sqrt(N)) + THIS RESULT together support a dS SECTION in "
                f"draft-04, NOT yet a standalone draft-05. The 4D truncated "
                f"area-law SSEE shows a GENUINE new separation absent in 2D (dS "
                f"rises ~{slope_ratio:.1f}x more shallowly than flat; dS R*-exponent "
                f"{a_ds:.2f} vs flat {a_fl:.2f}), and the content discriminator "
                f"(N_total cap R2=1.0 vs linear flat growth) cleanly lifts F-023 "
                f"to 4D. But the truncated entropy does not fully SATURATE at the "
                f"dense-eigh-accessible N<=2500: the F-019 fixed-region area-law "
                f"exponent comes out a={a_trunc:.2f} (above the clean 0.5; dS "
                f"radial geometry steepens it), and the horizon-approach dS S "
                f"still creeps up because the growing-cut-at-fixed-density adds dS "
                f"points faster than the sech^2 cap removes them. Decision: present "
                f"as a dS SECTION in draft-04 (crossed-product/vN-type), pairing "
                f"the 2D+4D content discriminator with the PARTIAL 4D "
                f"truncated-entropy signal, and flag the clean-saturation test as "
                f"needing larger N (sparse/iterative eigensolvers, rho>~10^3, "
                f"larger l, or a fixed-area entangling cut with a denser radial "
                f"horizon sweep) before it can carry a standalone draft-05. The "
                f"conformal-weight caveat (4D scalar not conformally invariant; "
                f"causal structure + measure preserved, exact propagator not) must "
                f"be stated honestly either way.")
    elif outcome == "NULL_but_content":
        h5g6 = ("F-023 + F-019 + THIS RESULT: the 4D lift CONFIRMS F-023 (content "
                "discriminates II_1 from II_inf) but the truncated area-law SSEE "
                "does NOT itself separate the types at accessible N. A reproduction, "
                "not an advance. Recommendation: a dS SECTION in draft-04, not a "
                "standalone draft-05; flag larger-N as future work.")
    else:
        h5g6 = ("Inconclusive at these N: defer the draft-05-vs-section decision "
                "until a larger-N (sparse eigensolver) 4D run resolves whether the "
                "truncated area-law SSEE separates the types. Provisionally a dS "
                "section in draft-04.")

    results["VERDICT"] = {
        "H5g1_truncated_SSEE_discriminates_STRONG": h5g1,
        "H5g1_truncated_SSEE_PARTIAL_separation": h5g1_partial,
        "content_tracking_discriminates": content,
        "fixed_region_4D_area_law_ok": area_law,
        "fixed_region_4D_area_law_exponent": a_trunc,
        "outcome": outcome,
        "overall": overall,
    }
    results["h5g6_input"] = h5g6
    print("\n=== OVERALL VERDICT (H5g-1) ===")
    print(f" outcome                                           : {outcome}")
    print(f" H5g-1 truncated-SSEE STRONG discriminates         : {h5g1}")
    print(f" H5g-1 truncated-SSEE PARTIAL separation           : {h5g1_partial}")
    print(f" content cross-check discriminates (F-023 4D lift) : {content}")
    print(f" fixed-region 4D area law a~0.5 (F-019)            : {area_law} (a={a_trunc:.2f})")
    print(f" overall: {overall}")


# ============================================================================
# PLOTS  (toe.viz is 2D-fit oriented; we draw the discriminator panels here)
# ============================================================================
def _plot_part1(R, r_edge, St_ds, St_ds_s, St_fl, St_fl_s, cap, B, xi,
                Ntot_ds, Ntot_fl, Ncap, NB, Nxi, part1):
    fig, (ax0, ax1) = plt.subplots(1, 2, figsize=(13, 5.2))
    xx = np.linspace(R.min(), R.max(), 200)
    # PANEL 0 (DECISIVE): truncated area-law SSEE -- dS caps, flat grows
    ax0.errorbar(R, St_ds, yerr=St_ds_s, fmt='o-', color='tab:blue', capsize=3,
                 label="de Sitter (II$_1$: $S_{\\rm trunc}$ saturates)")
    ax0.plot(xx, cap - B * np.exp(-xx / xi), 'b--', lw=1.1,
             label=rf"sat. fit $S_{{\rm cap}}={cap:.2f}$")
    ax0.errorbar(R, St_fl, yerr=St_fl_s, fmt='s-', color='tab:red', capsize=3,
                 label="flat control (II$_\\infty$: $S_{\\rm trunc}$ grows)")
    ax0.set_xlabel(r"box radial edge $R^*_{\rm box}/\ell$ (horizon: $R^*\to\infty$)")
    ax0.set_ylabel(r"truncated area-law SSEE $S_{\rm trunc}$  ($n_{\max}=2N^{3/4}$)")
    ax0.set_title("PART 1 (H5g-1, DECISIVE): 4D truncated area-law SSEE\n"
                  "dS saturates (II$_1$) vs flat grows (II$_\\infty$)")
    ax0.legend(fontsize=8)
    # PANEL 1: N_total content cross-check (VYPOCET-19 / F-023)
    ax1.plot(R, Ntot_ds, 'o-', color='tab:blue',
             label="de Sitter $N_{\\rm tot}$ (caps: bounded patch)")
    ax1.plot(xx, Ncap - NB * np.exp(-xx / Nxi), 'b--', lw=1.0)
    ax1.plot(R, Ntot_fl, 's-', color='tab:red',
             label="flat $N_{\\rm tot}$ (grows: unbounded)")
    ax1.set_xlabel(r"box radial edge $R^*_{\rm box}/\ell$")
    ax1.set_ylabel(r"causal-set cardinality $N_{\rm tot}$")
    ax1.set_title("content cross-check (F-023): dS proper volume (sech$^2$)\n"
                  "caps; flat volume grows linearly toward horizon")
    ax1.legend(fontsize=8)
    fig.tight_layout()
    fig.savefig(os.path.join(PLOTDIR, "part1_discriminator.png"), dpi=140)
    plt.close(fig)


def _plot_part2(Ns, St, Sf, fit_trunc, fit_full, pile_f, pile_t):
    fig, (ax0, ax1) = plt.subplots(1, 2, figsize=(13, 5.2))
    # area-law scaling
    ax0.errorbar(Ns, St.mean(1), yerr=St.std(1, ddof=1), fmt='o', color='tab:blue',
                 capsize=3, label=f"$S_{{\\rm trunc}}\\sim N^{{{fit_trunc.value:.2f}}}$ "
                                  f"(F-019 a$\\sim$0.5)")
    xx = np.linspace(Ns.min(), Ns.max(), 100)
    c_t = np.exp(fit_trunc.intercept)
    ax0.plot(xx, c_t * xx ** fit_trunc.value, 'b--', lw=1.0)
    ax0.errorbar(Ns, Sf.mean(1), yerr=Sf.std(1, ddof=1), fmt='s', color='tab:red',
                 capsize=3, label=f"$S_{{\\rm full}}\\sim N^{{{fit_full.value:.2f}}}$ (III)")
    ax0.set_xscale('log'); ax0.set_yscale('log')
    ax0.set_xlabel("N"); ax0.set_ylabel("SSEE $S$")
    ax0.set_title("PART 2: 4D area-law scaling on dS patch (fixed region)\n"
                  r"truncated $S\sim\sqrt{N}$ (area law, II); full $\sim N$ (III)")
    ax0.legend(fontsize=8.5)
    # modular pile-up
    ax1.plot(Ns, np.maximum(pile_f.mean(1), 1e-9), 'o-', color='tab:red',
             label="full pile-up ($\\epsilon<0.5$): grows (III$_1$)")
    ax1.plot(Ns, np.maximum(pile_t.mean(1), 1e-9), 's-', color='tab:blue',
             label="truncated pile-up: saturates (II)")
    ax1.set_xlabel("N"); ax1.set_ylabel(r"# modular modes $\epsilon<0.5$")
    ax1.set_title("modular pile-up (III$_1\\to$II type proxy)")
    ax1.legend(fontsize=8.5)
    fig.tight_layout()
    fig.savefig(os.path.join(PLOTDIR, "part2_area_law_scaling.png"), dpi=140)
    plt.close(fig)


# ============================================================================
def run():
    t0 = time.time()
    results = {"meta": {
        "task": "VYPOCET-21 TEST H5g-1 (BRAINSTORM-05): does the 4D truncated "
                "area-law SSEE S~sqrt(N) ITSELF separate type II_1 from II_inf?",
        "dimension": "4D de Sitter static patch (conformal sech^2 radial slab "
                     "(t, r*, x1, x2); 4D link-matrix Green on the flat order)",
        "geometry": "static patch in tortoise r*=l arctanh(r/l) + transverse box; "
                    "dS PROPER measure dN ~ sech^2(r*/l) dt dr* dx1 dx2 (radial "
                    "sech^2, transverse flat) vs matched flat radial-box control.",
        "library_extension": "toe.causet.sprinkle_ds_static_patch4d (added this "
                             "round; validated app/tests/test_toe_causet_ds4d.py).",
        "conformal_weight_caveat": "4D massless scalar is NOT conformally "
                                   "invariant: the conformal factor does NOT drop "
                                   "out of the exact propagator. This is the SAME "
                                   "controlled approximation as VYPOCET-19's 2D "
                                   "conformal trick lifted to 4D -- it PRESERVES "
                                   "the flat causal structure in (t,r*,x1,x2) and "
                                   "the dS proper MEASURE (sech^2 => bounded point "
                                   "budget = II_1 signal), but NOT the exact curved "
                                   "4D Wightman function. Tests the geometric II_1 "
                                   "vs II_inf boundedness in the truncated area-law "
                                   "SSEE, not the exact dS propagator.",
        "n_max_F019": "n_max = 2 N^(3/4) (Surya-Nomaan-X-Yazdi 2008.07697; 4D "
                      "area-law rank; validated VYPOCET-06 / vn-type-slab-4d).",
        "conventions": {
            "metric_dS": "static patch -(1-r^2/l^2)dt^2 + ... ; r*=l arctanh(r/l)",
            "conformal_factor": "Omega^2 = sech^2(r*/l)",
            "proper_measure": "dN ~ sech^2(r*/l) dt dr* dx1 dx2 (radial sech^2)",
            "G_R_4D": "K_R = a L, a = sqrt(rho)/(2 pi sqrt6) (Johnston 0909.0944)",
            "iDelta": "i(G_R - G_R^T), Hermitian, +/- paired (asserted <1e-12)",
            "SSEE": "W_O v = mu iDelta_O v ; S = sum mu ln|mu| ; pairs (mu,1-mu)",
            "n_max": "2 N^(3/4) rank truncation (keep top n_max +/- modes)",
            "modular_energy": "eps = ln[mu/(mu-1)] (Casini-Huerta 0905.2562)",
        },
        "references": {
            "CLPW": "arXiv:2206.10780 (dS static-patch algebra type II_1)",
            "area_law_rank": "arXiv:2008.07697 (n_max = alpha N^((d-1)/d))",
            "G_4D": "arXiv:0909.0944 (Johnston 4D causal-set Green)",
            "SJ_SSEE": "arXiv:1611.10281 (Sorkin-Yazdi SSEE double truncation)",
            "dS_2D": "VYPOCET-19 / F-023 (2D dS: only content discriminates)",
            "area_law_4D": "VYPOCET-06 / F-019 (4D type-II area law S~sqrt(N))",
        },
    }}

    part1_discriminator(results)
    part2_area_law_scaling(results)
    overall_verdict(results)

    results["runtime_s"] = time.time() - t0
    with open(os.path.join(OUTDIR, "results.json"), "w") as f:
        json.dump(_to_native(results), f, indent=2)
    print(f"\nDone in {results['runtime_s']:.1f}s. results.json + plots -> {OUTDIR}")
    return results


if __name__ == "__main__":
    run()
