#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""
VYPOCET-36  --  INDEX CHARGE IN THE DISCRETE PILLARS  (probe of H-E)
====================================================================
Bold hypothesis H-E (knowledge-base/LOV-18-11-overlaps.md):

    The ratio c/(-a) = -18/11 is index-PROTECTED on the smooth/NCG side:
    the Euler sector of the spinor a4 is the conformal a-anomaly, the
    Pontryagin sector is the Atiyah-Singer A-hat index density
    (A-hat|_4 = -p1/24, ind(D) = -sigma/8), and Rohlin's theorem
    (sigma = 16 mod 16 for a smooth closed spin 4-manifold) forces an
    EVEN-INTEGER topological charge ind(D) = -2 (F-014).

    H-E asks: do the SAME topological invariants surface in the DISCRETE
    pillars?  Can a causal set's surrogate Dirac reproduce an even-integer
    index / signature consistent with the Rohlin lock -- i.e. is -18/11 a
    discrete "topological charge" the other pillars must CARRY, not tune?

WHAT IS ACTUALLY CHECKABLE (and what is NOT).
The full smooth index ind(D) = int_M A-hat needs a closed Riemannian spin
4-manifold; a causal set is Lorentzian, has no smooth spin structure, no
de-Rham cohomology and (for the SJ surrogate Dirac) no chirality grading
gamma^5, so the chiral index dim ker D+ - dim ker D- is NOT EVEN DEFINED.
The one index ingredient that IS computable from a finite Hermitian
spectrum is the Atiyah-Patodi-Singer BOUNDARY term: the eta-invariant
(spectral asymmetry) eta(D) = sum_k sign(lambda_k).  APS:
    ind(D, M-with-boundary) = int_M A-hat - (eta(D_boundary) + h)/2.
So the cleanest honest discrete shadow of "an even-integer index" is the
spectral asymmetry / eta of the surrogate Dirac.  We run THREE proxies and
report honestly whether ANY lands on an even integer or a Rohlin-consistent
quantised value, or whether it is structurally trivial / drifts.

PROBE A -- eta-invariant (spectral asymmetry) of the surrogate Dirac D_K.
    D_K = sgn(K) sqrt(|K|) (toe.spectraltriple.dirac_from_kernel) is the
    symmetric-functional-calculus image of the SJ/modular kernel K of a
    sub-diamond, so it PRESERVES the sign pattern of K: eta(D_K) = n+(K)-n-(K)
    of the modular spectrum.  Target of H-E: an EVEN integer (Rohlin), stable
    across N and seeds.  Reality check: does it quantise, or drift?

PROBE B -- spectral asymmetry of the Pauli-Jordan operator iDelta itself.
    STRUCTURAL CONTROL.  By antisymmetry of Delta the spectrum of iDelta is
    EXACTLY +/- paired (toe.sj.sj_state docstring; W - W^dag = iDelta), so
    eta(iDelta) == 0 IDENTICALLY -- a property of every Lorentzian causal set,
    independent of any topology.  This pins down the gap: the discrete pillar
    has a built-in CP/charge symmetry that ZEROES the asymmetry by
    construction, the opposite of the smooth chiral asymmetry that Rohlin
    quantises to an even integer.  A zero here is NOT "Rohlin ind=0"; it is
    "no chiral grading exists".

PROBE C -- causet topological/signature proxy from molecule + chain counts.
    A Lorentzian causet DOES have a combinatorial avatar of the Euler-ish
    count (codim-2 Dou-Sorkin "molecules", toe.causet.horizon_molecules_codim2)
    and the alternating order-interval / link parities.  We test whether ANY
    of {molecule count parity, link-minus-relation alternating sum,
    Euler-like chain count} quantises to a STABLE even integer across N/seeds
    (a genuine topological charge) or grows extensively (~ rho^p) like a
    volume/area count (NOT a topological invariant).

DISCRIMINATOR (pre-registered, anti-circular -- directive #5):
    smooth target  : ind(D) = -2   (EVEN integer, Rohlin sigma=16)
    H-E PASS would need a discrete proxy that (i) is an integer, (ii) is EVEN,
    (iii) is STABLE (CV small) across N in [400,1500] and >=6 seeds, and (iv)
    is NOT just an extensive volume count (does not scale ~ rho^p, p>0).
    Any proxy failing (iii) or (iv) is a volume/area observable, not a charge.

Budget: dense N <= 1500, ~20 min, numpy/scipy only, every seed explicit.
Schema: fixed dict + atomic temp+rename write (CLAUDE.md hygiene); progressive
write after each N so a session-limit interrupt leaves a valid partial file.
Paths: __file__-relative bootstrap (portability guard).

Sources (repo-present only; NO invented arXiv IDs):
  Atiyah-Singer / A-hat genus, Rohlin sigma=16 -> ind=-2  : F-014, VYPOCET-11.
  Atiyah-Patodi-Singer eta-invariant boundary term        : standard APS
      (named in prose; no arXiv id asserted here).
  Surrogate Dirac D_K = sgn(K) sqrt|K|                     : toe.spectraltriple.
  SJ state / Pauli-Jordan +/- pairing                      : toe.sj, Sorkin-Yazdi
      1611.10281 (cited in lib docstrings).
  Dou-Sorkin horizon molecules                             : gr-qc/0302009
      (cited in lib docstring of horizon_molecules_codim2).
"""

from __future__ import annotations

import json
import os
import time

import numpy as np

# --- __file__-relative bootstrap (portability guard: no host-absolute path) ---
HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HERE, os.pardir, os.pardir, os.pardir))
LIB = os.path.join(REPO, "lib")
import sys
if LIB not in sys.path:
    sys.path.insert(0, LIB)

from toe.causet import (  # noqa: E402
    sprinkle_diamond2d,
    causal_matrix,
    link_matrix,
    green_retarded_2d,
    pauli_jordan,
    horizon_molecules_codim2,
)
from toe.sj import sj_state  # noqa: E402
from toe.entropy import modular_kernel  # noqa: E402
from toe.spectraltriple import dirac_from_kernel  # noqa: E402

OUT = os.path.join(HERE, "results.json")

# Pre-registered smooth target (F-014), fixed BEFORE any measurement.
SMOOTH_TARGET_IND = -2          # ind(D) = -sigma/8, Rohlin sigma=16
SMOOTH_TARGET_PARITY = "even"

NS = [400, 600, 800, 1000, 1250, 1500]
N_SEEDS = 8
SEED_BASE = 20260608
SUB_FRAC = 0.5                  # concentric half-diamond sub-region
ETA_TOL = 1e-9                  # |lambda| below this counts as a zero mode (iDelta)
ETA_TOL_DIRAC = 1e-6            # relative floor for D_K (drops lifted-kernel nulls)


def _spectral_asymmetry(spectrum, tol):
    """eta = sum_k sign(lambda_k) over |lambda| > tol; plus the counts."""
    s = np.asarray(spectrum, dtype=float)
    pos = int(np.count_nonzero(s > tol))
    neg = int(np.count_nonzero(s < -tol))
    zero = int(s.size - pos - neg)
    return pos - neg, pos, neg, zero


def _sub_diamond_idx(coords, frac):
    """Indices of points in the concentric sub-diamond {|u|,|v| <= frac}."""
    u, v = coords[:, 0], coords[:, 1]
    half = frac * float(np.max(np.abs(coords)))
    return np.nonzero((np.abs(u) <= half) & (np.abs(v) <= half))[0]


def _one_seed(N, seed):
    """All three probes on one sprinkled 2D diamond. Returns a flat dict."""
    rng = np.random.default_rng(seed)
    coords = sprinkle_diamond2d(N, rng)
    C = causal_matrix(coords)
    L = link_matrix(C)

    # ---- field / SJ state (massless 2D scalar) ----
    G_R = green_retarded_2d(C)
    iDelta = pauli_jordan(G_R)
    st = sj_state(iDelta, tol=1e-10)

    # PROBE B: spectral asymmetry of iDelta (structural control, must be ~0)
    etaB, posB, negB, zeroB = _spectral_asymmetry(st.eigvals, ETA_TOL)

    # PROBE A: eta of the surrogate Dirac on the sub-diamond modular kernel
    sub = _sub_diamond_idx(coords, SUB_FRAC)
    etaA = float("nan")
    posA = negA = zeroA = -1
    n_modes = 0
    if sub.size >= 4:
        mk = modular_kernel(st.W, iDelta, sub, kappa=None, tol=1e-9)
        if mk is not None:
            D_K = dirac_from_kernel(mk.K)
            dvals = np.linalg.eigvalsh(0.5 * (D_K + D_K.conj().T))
            # scale tol to the operator (modular energies span orders of mag)
            sc = float(np.max(np.abs(dvals))) if dvals.size else 1.0
            etaA_i, posA, negA, zeroA = _spectral_asymmetry(
                dvals, ETA_TOL_DIRAC * sc)
            etaA = float(etaA_i)
            n_modes = int(mk.n_modes)

    # PROBE C: causet topological / signature proxies
    n_rel = int(C.sum())                 # ordered relations (4-volume^2 proxy)
    n_link = int(L.sum())                # links (nearest causal pairs)
    # codim-2 Dou-Sorkin molecule count on the t=0, u=v cut of the diamond:
    # use the radial coord r = (u - v)/2 (= x) at level 0; eps = rho^{-1/2} in 2D
    vol = (2.0 * 1.0) ** 2 / 2.0         # diamond (u,v)-square area / 2
    rho = N / vol
    eps2d = rho ** (-0.5)
    coords_tx = np.column_stack([
        0.5 * (coords[:, 0] + coords[:, 1]),   # t = (u+v)/2
        0.5 * (coords[:, 0] - coords[:, 1]),   # x = (u-v)/2
    ])
    try:
        n_mol = int(horizon_molecules_codim2(
            coords_tx, C, r_index=1, r_cut=0.0, eps=eps2d, k_tube=1.5))
    except Exception:
        n_mol = -1
    # alternating "Euler-like" parity proxy: links - relations of length-2
    # (transitive pairs) mod parity -- a crude signature surrogate
    C2 = C @ C
    n_chain2 = int((C2 > 0).sum())       # pairs joined by a length-2 chain
    euler_like = n_link - n_chain2       # alternating inclusion-exclusion proxy

    return {
        "N": int(N), "seed": int(seed),
        "etaA_surrogate_dirac": etaA, "posA": posA, "negA": negA,
        "zeroA": zeroA, "n_modes": n_modes,
        "etaB_pauli_jordan": int(etaB), "posB": posB, "negB": negB,
        "zeroB": zeroB,
        "n_rel": n_rel, "n_link": n_link, "n_mol": n_mol,
        "n_chain2": n_chain2, "euler_like": euler_like,
        "n_sub": int(sub.size),
    }


def _agg(rows, key):
    v = np.array([r[key] for r in rows if np.isfinite(r[key])], dtype=float)
    if v.size == 0:
        return {"mean": None, "std": None, "cv": None, "n": 0,
                "all_int": None, "all_even": None}
    mean = float(np.mean(v))
    std = float(np.std(v, ddof=1)) if v.size > 1 else 0.0
    cv = float(std / abs(mean)) if mean != 0 else (0.0 if std == 0 else float("inf"))
    is_int = bool(np.all(np.abs(v - np.round(v)) < 1e-9))
    is_even = bool(is_int and np.all(np.round(v).astype(int) % 2 == 0))
    return {"mean": mean, "std": std, "cv": cv, "n": int(v.size),
            "all_int": is_int, "all_even": is_even}


def _write(payload):
    tmp = OUT + ".tmp"
    with open(tmp, "w") as f:
        json.dump(payload, f, indent=1)
    os.replace(tmp, OUT)


def main():
    t0 = time.time()
    payload = {
        "meta": {
            "calc": "VYPOCET-36 index-charge-discrete",
            "hypothesis": "H-E",
            "status": "running",
            "smooth_target_ind": SMOOTH_TARGET_IND,
            "smooth_target_parity": SMOOTH_TARGET_PARITY,
            "Ns": NS, "n_seeds": N_SEEDS, "seed_base": SEED_BASE,
            "sub_frac": SUB_FRAC, "eta_tol": ETA_TOL,
            "eta_tol_dirac": ETA_TOL_DIRAC,
            "geometry": "2D Poisson causal diamond, massless scalar SJ",
            "note": (
                "eta(D) = spectral asymmetry = APS boundary index term. "
                "Probe B (Pauli-Jordan) is a structural control: iDelta has "
                "an EXACTLY +/- paired spectrum, so eta=0 identically -- the "
                "Lorentzian causal set lacks the chiral grading Rohlin "
                "quantises."),
        },
        "per_N": [],
        "rows": [],
        "VERDICT": {},
    }
    _write(payload)

    all_rows = []
    for N in NS:
        seeds = [SEED_BASE + N * 1000 + s for s in range(N_SEEDS)]
        rows = []
        for s in seeds:
            rows.append(_one_seed(N, s))
        all_rows.extend(rows)
        payload["per_N"].append({
            "N": int(N),
            "etaA": _agg(rows, "etaA_surrogate_dirac"),
            "etaB": _agg(rows, "etaB_pauli_jordan"),
            "n_mol": _agg(rows, "n_mol"),
            "n_link": _agg(rows, "n_link"),
            "n_rel": _agg(rows, "n_rel"),
            "euler_like": _agg(rows, "euler_like"),
        })
        payload["rows"] = all_rows
        payload["meta"]["elapsed_s"] = round(time.time() - t0, 1)
        _write(payload)
        print(f"[N={N}] etaA={payload['per_N'][-1]['etaA']['mean']} "
              f"etaB={payload['per_N'][-1]['etaB']['mean']} "
              f"n_mol={payload['per_N'][-1]['n_mol']['mean']} "
              f"n_link={payload['per_N'][-1]['n_link']['mean']} "
              f"({payload['meta']['elapsed_s']}s)")

    # ---- verdict (anti-circular: target was pre-registered) ----
    # extensivity test: log-log slope of each proxy vs N
    Nvals = np.array(NS, dtype=float)

    def slope(key):
        y = np.array([p[key]["mean"] for p in payload["per_N"]
                      if p[key]["mean"] not in (None, 0)], dtype=float)
        x = Nvals[:len(y)]
        m = y > 0
        if m.sum() < 3:
            return None
        return float(np.polyfit(np.log(x[m]), np.log(y[m]), 1)[0])

    # is etaA a stable even integer (H-E PASS) ?
    etaA_means = [p["etaA"]["mean"] for p in payload["per_N"]
                  if p["etaA"]["mean"] is not None]
    etaA_global = _agg(all_rows, "etaA_surrogate_dirac")
    etaB_global = _agg(all_rows, "etaB_pauli_jordan")

    pass_etaA = bool(
        etaA_global["n"] > 0 and etaA_global["all_int"]
        and etaA_global["all_even"] and etaA_global["cv"] is not None
        and etaA_global["cv"] < 0.10)

    payload["VERDICT"] = {
        "smooth_target": {"ind": SMOOTH_TARGET_IND, "parity": "even"},
        "probeA_eta_surrogate_dirac": {
            "global": etaA_global,
            "is_even_integer_stable": pass_etaA,
            "interpretation": (
                "PASS only if eta(D_K) is an even integer stable across N/seeds "
                "(CV<10%). Otherwise it is not a Rohlin-locked charge."),
        },
        "probeB_eta_pauli_jordan": {
            "global": etaB_global,
            "structurally_zero": bool(
                etaB_global["mean"] is not None
                and abs(etaB_global["mean"]) < 0.5),
            "interpretation": (
                "eta(iDelta)=0 IDENTICALLY by +/- pairing of Delta. This is NOT "
                "Rohlin ind=0; it is the ABSENCE of a chiral grading. THE GAP."),
        },
        "probeC_extensivity": {
            "slope_etaA_vs_N": slope("etaA"),
            "slope_n_link_vs_N": slope("n_link"),
            "slope_n_rel_vs_N": slope("n_rel"),
            "slope_n_mol_vs_N": slope("n_mol"),
            "interpretation": (
                "Nonzero positive slope => the count is an EXTENSIVE volume/area "
                "observable, NOT a topological charge (a charge is N-independent). "
                "etaA slope ~1 means eta(D_K) ~ N (a mode count), the OPPOSITE of "
                "the N-independent Rohlin charge ind=-2."),
        },
        "H_E_verdict": (
            "PASS" if pass_etaA else "REFUTED_AS_DIRECT_INDEX_no_even_integer_charge"),
    }
    payload["meta"]["status"] = "done"
    payload["meta"]["elapsed_s"] = round(time.time() - t0, 1)
    _write(payload)
    print("VERDICT:", payload["VERDICT"]["H_E_verdict"],
          "| etaA global:", etaA_global,
          "| etaB global:", etaB_global)


if __name__ == "__main__":
    main()
