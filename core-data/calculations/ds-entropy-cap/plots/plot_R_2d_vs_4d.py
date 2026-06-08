#!/usr/bin/env python3
"""VYPOCET-25 summary figure: R = S_full_cap / A_mol vs rho, 2D vs 4D, log-log.

2D (committed F-028 convention, codim-2 horizon = point): R is FLAT ~0.13.
4D (codim-2 surface molecule count): R DRIFTS ~ rho^(-0.7).

Reads the staged cloud artifacts directly; standalone (matplotlib Agg).
Run:  python3 plot_R_2d_vs_4d.py
Out:  R_2d_vs_4d.png  (next to this script)
"""
import json
import os

import numpy as np
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

HERE = os.path.dirname(os.path.abspath(__file__))
ARCH = os.path.abspath(os.path.join(HERE, "..", "..", "..", "..",
                                    "compute", "results-archive"))


def load(name):
    with open(os.path.join(ARCH, name)) as f:
        return json.load(f)


d2 = load("ds_entropy_cap_2d-rho30k.json")
g4 = load("ds_cap_4d-grid.json")
h4 = load("ds_cap_4d-highN.json")

# --- 2D: valid (dense) cells only; R = S_full_cap / A_mol ---
two = [(c["rho"], c["R_Sfull_over_Amol"])
       for c in d2["cells"] if c.get("R_Sfull_over_Amol") is not None]
r2 = np.array([x[0] for x in two])
R2 = np.array([x[1] for x in two])
R2_mean = R2.mean()

# --- 4D: keep physically meaningful cap fits (R in (0,1), Sfull_R2 >= 0.40) ---
def four_cells(src):
    out = []
    for c in src["cells"]:
        if c.get("path") == "skipped":
            continue
        R = c.get("R_Sfull_over_Amol")
        if R is None or R <= 0 or R > 1 or c["S_full_cap_R2"] < 0.40:
            continue
        out.append((c["rho"], R, c["S_full_cap_R2"]))
    return out


four = four_cells(g4) + four_cells(h4)
r4 = np.array([x[0] for x in four])
R4 = np.array([x[1] for x in four])
# split high-confidence (R2>=0.7) vs marginal for marker styling
hi = np.array([x[2] >= 0.70 for x in four])

# 4D power-law guide rho^(-1/2)  (reference exponent in the convention)
xref = np.array([55.0, 2200.0])
# anchor the rho^-1/2 line at the rho=240 clean point
anchor = next(x for x in four if abs(x[0] - 240.0) < 1e-6)
yref_half = anchor[1] * (xref / anchor[0]) ** (-0.5)

fig, ax = plt.subplots(figsize=(7.0, 5.2))

# 2D flat line
ax.loglog(r2, R2, "o", color="#1f77b4", ms=7, label="2D  R = S_full/A_mol (F-028 conv.)")
ax.axhline(R2_mean, color="#1f77b4", ls="--", lw=1.2,
           label=f"2D mean R = {R2_mean:.4f}  (flat, CV 3%)")
ax.axhline(0.1321, color="#1f77b4", ls=":", lw=1.0, alpha=0.7,
           label="committed F-028 R = 0.1321")

# 4D drifting points
ax.loglog(r4[hi], R4[hi], "s", color="#d62728", ms=8,
          label="4D  R (S_full_cap_R2 ≥ 0.70)")
ax.loglog(r4[~hi], R4[~hi], "s", color="#d62728", ms=7, mfc="none",
          label="4D  R (marginal cap fit 0.40–0.70)")
ax.loglog(xref, yref_half, "-", color="#d62728", lw=1.3, alpha=0.8,
          label=r"$\rho^{-1/2}$ convention guide")

# annotate measured 4D drift
ax.text(0.40, 0.30, "4D fixed-l=0.8 drift:\n"
        r"$d\ln R/d\ln\rho = -0.72\pm0.01$"
        "\n(A_mol ~ rho^1.77, S_full ~ rho^1.05)",
        transform=ax.transAxes, fontsize=8.5, va="top",
        bbox=dict(boxstyle="round", fc="#fff3f3", ec="#d62728", alpha=0.9))
ax.text(0.40, 0.80, "2D: A_mol ~ rho^1, S_full ~ rho^1  =>  R flat",
        transform=ax.transAxes, fontsize=8.5, color="#1f77b4")

ax.set_xlabel(r"proper density  $\rho$")
ax.set_ylabel(r"$R \;=\; S_{\rm full,cap}\,/\,A_{\rm mol}$")
ax.set_title("dS entropy-cap ratio R: 2D constant vs 4D drifting (VYPOCET-25)")
ax.set_xlim(45, 2600)
ax.set_ylim(0.008, 0.30)
ax.grid(True, which="both", ls=":", alpha=0.35)
ax.legend(fontsize=7.6, loc="upper right", framealpha=0.92)

fig.tight_layout()
out = os.path.join(HERE, "R_2d_vs_4d.png")
fig.savefig(out, dpi=130)
plt.close(fig)
print("wrote", out)
print(f"2D: n={len(R2)} cells, mean R={R2_mean:.5f}, CV={100*R2.std(ddof=1)/R2_mean:.2f}%")
print(f"4D: n={len(R4)} clean cells, R range {R4.min():.4f}..{R4.max():.4f}")
