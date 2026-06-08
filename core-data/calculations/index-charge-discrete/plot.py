#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""VYPOCET-36 plot: the index-charge probe of H-E.

Left  : eta(D_K) (surrogate Dirac spectral asymmetry) vs N -- grows LINEARLY
        (slope ~1, a mode/volume count) and never sits on the Rohlin charge -2.
Right : eta(iDelta) (Pauli-Jordan) == 0 identically (structural +/- pairing),
        contrasted with the smooth even-integer target ind = -2.
Paths are __file__-relative (portability guard).
"""
import json
import os

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
RES = os.path.join(HERE, "results.json")
PNG = os.path.join(HERE, "index-charge-discrete.png")

d = json.load(open(RES))
N = np.array([p["N"] for p in d["per_N"]], float)
etaA = np.array([p["etaA"]["mean"] for p in d["per_N"]], float)
etaA_sd = np.array([p["etaA"]["std"] or 0.0 for p in d["per_N"]], float)
etaB = np.array([p["etaB"]["mean"] for p in d["per_N"]], float)
slopeA = float(np.polyfit(np.log(N), np.log(etaA), 1)[0])
target = d["meta"]["smooth_target_ind"]

fig, ax = plt.subplots(1, 2, figsize=(11, 4.4))

# --- left: etaA extensivity ---
ax[0].errorbar(N, etaA, yerr=etaA_sd, fmt="o-", color="#c0392b",
               capsize=3, label=r"$\eta(D_K)$ surrogate Dirac")
ax[0].axhline(target, color="#2c3e50", ls="--",
              label=fr"Rohlin charge  ind$=-\sigma/8={target}$ (even)")
ax[0].axhline(0, color="gray", lw=0.7)
ax[0].set_xlabel("N (sprinkled points)")
ax[0].set_ylabel(r"spectral asymmetry  $\eta = \sum_k \mathrm{sgn}\,\lambda_k$")
ax[0].set_title(fr"Probe A: $\eta(D_K)\propto N^{{{slopeA:.2f}}}$ "
                r"(volume count, NOT a charge)")
ax[0].legend(fontsize=8, loc="upper left")
ax[0].grid(alpha=0.25)

# --- right: etaB structural zero vs target ---
ax[1].plot(N, etaB, "s-", color="#27ae60", label=r"$\eta(i\Delta)$ Pauli-Jordan $\equiv 0$")
ax[1].axhline(target, color="#2c3e50", ls="--",
              label=fr"smooth ind $={target}$ (Rohlin)")
ax[1].axhline(0, color="gray", lw=0.7)
ax[1].set_ylim(-3.0, 1.0)
ax[1].set_xlabel("N (sprinkled points)")
ax[1].set_ylabel(r"$\eta(i\Delta)$")
ax[1].set_title(r"Probe B: $\eta(i\Delta)=0$ by $\pm$-pairing"
                "\n(no chiral grading $\\Rightarrow$ no Rohlin lock: THE GAP)")
ax[1].legend(fontsize=8, loc="lower left")
ax[1].grid(alpha=0.25)

fig.suptitle("VYPOCET-36  H-E: does a causal set carry the -18/11 "
             "index charge? (2D diamond, 8 seeds/N)", fontsize=11)
fig.tight_layout(rect=(0, 0, 1, 0.95))
fig.savefig(PNG, dpi=130)
print("wrote", PNG)
