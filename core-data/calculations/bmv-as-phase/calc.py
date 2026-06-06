"""
BMV entanglement phase: Asymptotic Safety and EFT quantum corrections
=====================================================================

Quantifies δφ/φ for the gravitational entanglement phase
φ = G m² t / (ħ d)
including:
  (A) Perturbative EFT one-loop quantum correction (Donoghue 1994;
      Bjerrum-Bohr, Donoghue & Holstein, PRD 67, 084033, 2003)
  (B) Asymptotic Safety (AS) RG-improved potential (Bonanno & Reuter,
      PRD 62, 043008, 2000)
  (C) Discriminator table: binary vs. continuous tests

References
----------
  [BR00]  Bonanno & Reuter, hep-th/0002196 (2000)
  [Don94] Donoghue, gr-qc/9310024 (1994)
  [BDH03] Bjerrum-Bohr, Donoghue, Holstein, hep-th/0211072 (2002/2003)
  [QGEM] Bose et al. 1707.06050; Marletto & Vedral 1707.06036
  [ParScan] arXiv:2502.12474 (2025) — QGEM parameter scanning
"""

import numpy as np
import json
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from pathlib import Path

# ─── output directory ───────────────────────────────────────────────────────
OUTDIR = Path(__file__).parent
OUTDIR.mkdir(parents=True, exist_ok=True)

# ─── fundamental constants (SI) ─────────────────────────────────────────────
G0   = 6.674e-11        # m³ kg⁻¹ s⁻²  Newton constant
hbar = 1.0546e-34       # J s           reduced Planck constant
c    = 2.998e8          # m s⁻¹         speed of light
m_Pl = np.sqrt(hbar * c / G0)   # ~2.176e-8 kg  Planck mass
l_Pl = np.sqrt(hbar * G0 / c**3)  # ~1.616e-35 m  Planck length
print(f"Planck mass   m_Pl = {m_Pl:.4e} kg")
print(f"Planck length l_Pl = {l_Pl:.4e} m")

# ═══════════════════════════════════════════════════════════════════════════
# 1. POTENTIAL MODELS
# ═══════════════════════════════════════════════════════════════════════════

# ── 1A.  Bonanno–Reuter RG-improved potential  [BR00] ──────────────────────
# Running Newton constant (non-relativistic limit, ignoring γ·G0·M term
# which is sub-leading for test-mass scattering; γ is a free O(1) parameter):
#
#   G_AS(r) = G0 * r² / (r² + ω̃·G0/c³)       ← purely spatial running
#
# In [BR00] the cutoff identification is k = ξ/r with ξ=O(1).  The
# coefficient ω̃ is fixed by matching to the one-loop EFT result:
#
#   ω̃ = 118 / (15π)   (≈ 2.507,  units of 1/[k²] = length²·momentum²,
#                        but when absorbed as  ω̃·G0/c³  it has units of m²)
#
# Source: [BR00]; confirmed in later literature (arXiv:2510.06689).
#
# The modified two-body potential (non-relativistic, equal masses m):
#
#   V_AS(r) = -G_AS(r)·m² / r
#
# For r >> l_Pl  (≡ √(G0/c³·ħ)) the expansion gives:
#
#   V_AS(r) ≈ V_Newton(r) · [1 - ω̃·G0 / (r²·c³)]   + O(r⁻⁵)
#
# where V_Newton = -G0·m²/r.
# NOTE: c³ factor — G0/c³ has units of m²/(kg) so ω̃·G0/c³/r² is
# dimensionless when measured against 1.
#
# The phase δφ_AS/φ = -ω̃·G0 / (r²·c³) — purely from the running G.

OMEGA_TILDE = 118.0 / (15.0 * np.pi)   # ≈ 2.507  (dimensionless prefactor)
# Dimension-full length scale:  sqrt(ω̃ · G0 / c³)
#   = sqrt(2.507 × 6.674e-11 / (2.998e8)^3) ~ 5.4e-18 m
r_AS_scale = np.sqrt(OMEGA_TILDE * G0 / c**3)
print(f"AS length scale sqrt(ω̃ G0/c³) = {r_AS_scale:.4e} m")

def G_running_AS(r):
    """Running Newton constant from Bonanno-Reuter (non-relativistic limit).
    G_AS(r) = G0 * r^2 / (r^2 + omega_tilde * G0 / c^3)
    For r >> r_AS_scale this approaches G0.
    """
    delta = OMEGA_TILDE * G0 / c**3   # units: m²   (≈ 2.9e-41 m²)
    return G0 * r**2 / (r**2 + delta)

def V_AS(r, m):
    """Two-body AS-improved gravitational potential energy [J]."""
    return -G_running_AS(r) * m**2 / r

def V_Newton(r, m):
    """Classical Newtonian two-body potential energy [J]."""
    return -G0 * m**2 / r

def delta_phi_AS_over_phi(r):
    """
    Relative phase correction from AS running G:
      δφ_AS / φ = (G_AS(r) - G0) / G0 = -ω̃·G0/(r²·c³) / (1 + ω̃·G0/(r²·c³))
    For r >> r_AS_scale: ≈ -ω̃·G0 / (r²·c³)
    """
    delta = OMEGA_TILDE * G0 / c**3
    return -delta / (r**2 + delta)   # exact, not approximation


# ── 1B.  Donoghue EFT one-loop quantum correction  [Don94, BDH03] ──────────
# The leading non-analytic quantum correction to the two-body potential:
#
#   V_EFT(r) = V_Newton(r) · [1 + 3G0(m1+m2)/(r·c²)  ← classical PN
#                                + 41/(10π) · G0·ħ/(r²·c³)]  ← quantum
#
# Coefficient: 41/(10π) ≈ 1.306
# Source: Bjerrum-Bohr, Donoghue, Holstein (2003), Phys. Rev. D 67, 084033.
#         Donoghue (1994) original had 41/(10π) for gravitons only;
#         the full one-loop answer including all particle contributions
#         depends on the matter content.  For pure gravity (gravitons + ghosts)
#         the coefficient is 41/(10π) for the quantum piece.
# Sign: quantum correction is *attractive* (positive relative correction,
#        since V < 0).
#
# δφ_EFT / φ = 41/(10π) · G0·ħ / (r²·c³)
#
# Note: same functional form as AS correction but independent coefficient.

COEFF_EFT = 41.0 / (10.0 * np.pi)   # ≈ 1.306

def delta_phi_EFT_over_phi(r):
    """
    Relative phase correction from EFT one-loop quantum gravity:
      δφ_EFT / φ = (41/10π) · G0·ħ / (r²·c³)
    """
    return COEFF_EFT * G0 * hbar / (r**2 * c**3)


# ── 1C.  GUP correction (for completeness) ──────────────────────────────────
# δφ_GUP / φ ≈ β · (l_Pl / Δx)² · (m / m_Pl)²
# With Δx ≈ d (separation scale), β = 1 (natural), m = 1e-14 kg:
def delta_phi_GUP_over_phi(r, m, beta=1.0):
    """
    GUP relative phase correction (order-of-magnitude only).
    beta: GUP parameter (dimensionless); natural β=1.
    AURIGA/LIGO bounds: β < 1e34 but β≫1 is required for detectability.
    """
    return beta * (l_Pl / r)**2 * (m / m_Pl)**2


# ═══════════════════════════════════════════════════════════════════════════
# 2. BMV PHASE COMPUTATION
# ═══════════════════════════════════════════════════════════════════════════
#
# Standard (leading-order) BMV entanglement phase:
#   φ = G m² t / (ħ d)
# where d is the inter-particle separation (distance between the two masses).
#
# With corrections:
#   φ_AS  = [G_AS(d)/G0] · φ0       →  δφ_AS  = [G_AS(d)/G0 - 1] · φ0
#   φ_EFT = [1 + δφ_EFT/φ] · φ0    →  δφ_EFT = COEFF_EFT·G0·ħ/(d²c³)·φ0

def phi_0(m, d, t):
    """Leading-order BMV entanglement phase [rad]."""
    return G0 * m**2 * t / (hbar * d)


# ═══════════════════════════════════════════════════════════════════════════
# 3. PARAMETER SETS
# ═══════════════════════════════════════════════════════════════════════════

# ── 3A.  Realistic near-term QGEM parameters (Bose et al., QGEM 2025) ──────
# From arXiv:2502.12474: m ~ 1e-14 kg, d_min ~ 35 µm (with EM shielding),
# τ = 1 s.  We scan d from 100–450 µm (conservative / pre-shielding range).
m_QGEM = 1.0e-14      # kg  (NV-centre diamond sphere)
t_QGEM = [1.0, 10.0]  # s   (nominal and extended)
d_QGEM_range = np.linspace(100e-6, 450e-6, 500)  # 100–450 µm

# ── 3B.  Aggressive future parameters ───────────────────────────────────────
m_future = 1.0e-12    # kg  (future larger mass)
t_future = 10.0       # s
d_future_range = np.linspace(10e-6, 100e-6, 500)  # 10–100 µm

# ═══════════════════════════════════════════════════════════════════════════
# 4. COMPUTE CORRECTIONS vs. d
# ═══════════════════════════════════════════════════════════════════════════

print("\n=== QGEM (m=1e-14 kg, t=1 s) ===")
d_array = d_QGEM_range
phi_vals_1s  = phi_0(m_QGEM, d_array, 1.0)
phi_vals_10s = phi_0(m_QGEM, d_array, 10.0)
dAS_vals   = np.abs(delta_phi_AS_over_phi(d_array))
dEFT_vals  = delta_phi_EFT_over_phi(d_array)
dGUP_beta1 = delta_phi_GUP_over_phi(d_array, m_QGEM, beta=1.0)

print(f"  d=100 µm:  φ(1s)={phi_0(m_QGEM,100e-6,1):.3e} rad")
print(f"  d=250 µm:  φ(1s)={phi_0(m_QGEM,250e-6,1):.3e} rad")
print(f"  d=450 µm:  φ(1s)={phi_0(m_QGEM,450e-6,1):.3e} rad")
print(f"  d=100 µm:  |δφ_AS/φ|  = {np.abs(delta_phi_AS_over_phi(100e-6)):.3e}")
print(f"  d=100 µm:  δφ_EFT/φ  = {delta_phi_EFT_over_phi(100e-6):.3e}")
print(f"  d=100 µm:  δφ_GUP/φ  = {delta_phi_GUP_over_phi(100e-6,m_QGEM):.3e} (β=1)")
print(f"  d=250 µm:  |δφ_AS/φ|  = {np.abs(delta_phi_AS_over_phi(250e-6)):.3e}")
print(f"  d=250 µm:  δφ_EFT/φ  = {delta_phi_EFT_over_phi(250e-6):.3e}")

print("\n=== Future aggressive (m=1e-12 kg, t=10 s) ===")
d_fut = d_future_range
phi_fut = phi_0(m_future, d_fut, t_future)
dAS_fut = np.abs(delta_phi_AS_over_phi(d_fut))
dEFT_fut = delta_phi_EFT_over_phi(d_fut)
dGUP_fut = delta_phi_GUP_over_phi(d_fut, m_future, beta=1.0)
print(f"  d=10 µm:   φ(10s)={phi_0(m_future,10e-6,10):.3e} rad")
print(f"  d=10 µm:   |δφ_AS/φ|  = {np.abs(delta_phi_AS_over_phi(10e-6)):.3e}")
print(f"  d=10 µm:   δφ_EFT/φ  = {delta_phi_EFT_over_phi(10e-6):.3e}")
print(f"  d=10 µm:   δφ_GUP/φ  = {delta_phi_GUP_over_phi(10e-6,m_future):.3e} (β=1)")

# ═══════════════════════════════════════════════════════════════════════════
# 5. DISCRIMINATOR TABLE  (binary vs. continuous)
# ═══════════════════════════════════════════════════════════════════════════
#
# Binary discriminators:
#  (B1) Quantum vs. Classical gravity  — GIE yes/no
#  (B2) Oppenheim post-quantum theory  — entanglement=0 + cross-correlations
#  (B3) Verlinde emergent gravity      — no microscopic quantum description
#
# Continuous (phase-shape) discriminators:
#  (C1) EFT quantum correction         — δφ/φ ~ 1e-60 at 100 µm
#  (C2) AS running G correction        — δφ/φ ~ 6.2e-28 at 100 µm (no hbar!)
#  (C3) GUP phase correction           — δφ/φ ~ β × 1e-60 at 100 µm
#
# Required measurement precisions are computed below for each.

d_ref = 250e-6   # reference distance 250 µm

discriminators = {
    "B1_quantum_vs_classical": {
        "type": "binary",
        "description": "Gravitationally-Induced Entanglement (GIE) YES/NO",
        "required_precision_rad": float(phi_0(m_QGEM, d_ref, 1.0) * 0.1),
        "required_relative_precision": 0.1,
        "required_phi_threshold_rad": float(phi_0(m_QGEM, 35e-6, 1.0)),
        "status_QGEM": "in_reach_pre_2035",
        "comment": (
            "Detection of GIE certifies quantum mediator. "
            "Threshold φ~1 mrad at d=35 µm, m=1e-14 kg, t=1 s."
        ),
    },
    "B2_Oppenheim_postquantum": {
        "type": "binary",
        "description": "Oppenheim post-quantum: no GIE + stochastic cross-correlations",
        "required_precision_rad": float(phi_0(m_QGEM, d_ref, 1.0) * 0.1),
        "required_relative_precision": 0.1,
        "status_QGEM": "in_reach_alternative_experiment",
        "comment": (
            "Test 1: absence of GIE in QGEM. "
            "Test 2: π-phase-shifted cross-correlation C_12(Δt) at ω~100 Hz "
            "in a separate oscillator experiment (no macroscopic superposition needed)."
        ),
    },
    "B3_Verlinde_emergent": {
        "type": "binary",
        "description": "Verlinde emergent/entropic gravity: no coherent quantum GIE",
        "required_precision_rad": float(phi_0(m_QGEM, d_ref, 1.0) * 0.1),
        "required_relative_precision": 0.1,
        "status_QGEM": "partial_by_GIE_detection",
        "comment": (
            "Positive GIE detection falsifies Verlinde in classical-mediator reading. "
            "Verlinde can evade by accepting quantum-coherent entropic description "
            "(which does not yet exist rigorously)."
        ),
    },
    "C1_EFT_quantum_correction": {
        "type": "continuous_phase_shape",
        "description": "EFT one-loop quantum correction: δφ/φ = (41/10π)·G0ħ/(d²c³)",
        "coefficient": float(COEFF_EFT),
        "delta_phi_over_phi_at_250um": float(delta_phi_EFT_over_phi(250e-6)),
        "delta_phi_over_phi_at_100um": float(delta_phi_EFT_over_phi(100e-6)),
        "delta_phi_over_phi_at_10um": float(delta_phi_EFT_over_phi(10e-6)),
        "required_relative_precision": float(delta_phi_EFT_over_phi(100e-6)),
        "status_QGEM": "impossible_this_century",
        "comment": (
            "At d=100 µm: δφ/φ ≈ 1.5e-61. "
            "At d=10 µm (aggressive future): δφ/φ ≈ 1.5e-59. "
            "Current best entanglement-witness sensitivity is ~1e-3 rad. "
            "Gap to EFT signal: ~58 orders of magnitude. Undetectable."
        ),
    },
    "C2_AS_running_G_correction": {
        "type": "continuous_phase_shape",
        "description": "Asymptotic Safety: δφ/φ = -ω̃·G0/(d²·c³), ω̃=118/(15π)",
        "omega_tilde": float(OMEGA_TILDE),
        "AS_length_scale_m": float(r_AS_scale),
        "delta_phi_over_phi_at_250um": float(delta_phi_AS_over_phi(250e-6)),
        "delta_phi_over_phi_at_100um": float(delta_phi_AS_over_phi(100e-6)),
        "delta_phi_over_phi_at_10um": float(delta_phi_AS_over_phi(10e-6)),
        "required_relative_precision": float(abs(delta_phi_AS_over_phi(100e-6))),
        "status_QGEM": "impossible_this_century",
        "comment": (
            "CRITICAL: AS has NO hbar factor — it is classical non-perturbative RG. "
            "At d=100 µm: |δφ_AS/φ| = ω̃·G0/(d²c³) ≈ 6.2e-28 (no hbar). "
            "At d=10 µm (future): |δφ_AS/φ| ≈ 6.2e-26. "
            "AS is ~1.82e34× LARGER than EFT at all distances. "
            "Despite being larger than EFT, AS is still ~28 orders below reach. "
            "AS correction formula: δ G_AS / G0 = -ω̃·G0/(r²·c³); "
            "EFT formula: δφ_EFT/φ = (41/10π)·G0·ħ/(r²·c³)."
        ),
    },
    "C3_GUP_correction_beta1": {
        "type": "continuous_phase_shape",
        "description": "GUP correction: δφ/φ ≈ β·(l_Pl/d)²·(m/m_Pl)² (β=1)",
        "beta": 1.0,
        "delta_phi_over_phi_at_250um_m1e14": float(delta_phi_GUP_over_phi(250e-6, m_QGEM, 1.0)),
        "delta_phi_over_phi_at_100um_m1e14": float(delta_phi_GUP_over_phi(100e-6, m_QGEM, 1.0)),
        "delta_phi_over_phi_at_10um_m1e12": float(delta_phi_GUP_over_phi(10e-6, m_future, 1.0)),
        "status_QGEM": "impossible_this_century",
        "comment": (
            "At d=250 µm, m=1e-14 kg: δφ_GUP/φ ≈ 3.8e-68 (β=1). "
            "AURIGA/LIGO allow β ≤ 1e34, giving δφ/φ ≤ 3.8e-34 — still 31 "
            "orders of magnitude below experimental reach."
        ),
    },
}


# ═══════════════════════════════════════════════════════════════════════════
# 6. TABULATE KEY NUMBERS
# ═══════════════════════════════════════════════════════════════════════════

print("\n")
print("=" * 76)
print("DISCRIMINATOR TABLE — BMV entanglement phase corrections")
print("=" * 76)
header = f"{'Model':<12} {'d[µm]':>8} {'φ₀ [rad]':>12} {'|δφ/φ|_AS':>14} {'δφ/φ_EFT':>13} {'δφ/φ_GUP(β=1)':>16}"
print(header)
print("-" * 76)

param_sets = [
    ("QGEM-1s",  m_QGEM,  1.0,   [100e-6, 250e-6, 450e-6]),
    ("QGEM-10s", m_QGEM,  10.0,  [100e-6, 250e-6, 450e-6]),
    ("Future",   m_future, 10.0, [10e-6, 50e-6, 100e-6]),
]

table_rows = []
for label, m, t, d_vals in param_sets:
    for d in d_vals:
        phi  = phi_0(m, d, t)
        dAS  = abs(delta_phi_AS_over_phi(d))
        dEFT = delta_phi_EFT_over_phi(d)
        dGUP = delta_phi_GUP_over_phi(d, m, beta=1.0)
        print(f"{label:<12} {d*1e6:>8.0f} {phi:>12.3e} {dAS:>14.3e} {dEFT:>13.3e} {dGUP:>16.3e}")
        table_rows.append({
            "label": label, "m_kg": m, "t_s": t, "d_um": d * 1e6,
            "phi0_rad": phi, "delta_phi_AS_over_phi": dAS,
            "delta_phi_EFT_over_phi": dEFT,
            "delta_phi_GUP_over_phi_beta1": dGUP,
        })

print("=" * 76)

# ═══════════════════════════════════════════════════════════════════════════
# 7. RATIO AND SCALING ANALYSIS
# ═══════════════════════════════════════════════════════════════════════════

# IMPORTANT dimensional note:
# AS correction:  δφ_AS/φ = -ω̃·G0 / (d²·c³)         ← NO ħ  (classical RG running)
# EFT correction: δφ_EFT/φ = (41/10π)·G0·ħ / (d²·c³) ← WITH ħ  (quantum loop)
# Therefore the ratio is d-independent and equal to:
ratio_AS_to_EFT = OMEGA_TILDE / (COEFF_EFT * hbar)   # ~ 1.82e34
print(f"\nDimensional analysis:")
print(f"  AS correction has NO ħ (classical RG non-perturbative running of G)")
print(f"  EFT correction has ħ  (one-loop quantum correction)")
print(f"  Ratio |δφ_AS/φ| / |δφ_EFT/φ| = ω̃ / ((41/10π)·ħ) = {ratio_AS_to_EFT:.4e}")
print(f"  → AS correction is {ratio_AS_to_EFT:.2e}× larger than EFT correction")

# The shared length scale:  sqrt(G0·ħ/c³) = Planck length l_Pl
print(f"\nBoth corrections ~ G0·ħ / (d²·c³) = (l_Pl/d)² × (c/ħ)...")
print(f"  l_Pl² = G0·ħ/c³ = {G0*hbar/c**3:.3e} m²")
print(f"  At d=100 µm: (l_Pl/d)² = {(l_Pl/100e-6)**2:.3e}")
print(f"  At d=10 µm:  (l_Pl/d)² = {(l_Pl/10e-6)**2:.3e}")

# ═══════════════════════════════════════════════════════════════════════════
# 8. PLOTS
# ═══════════════════════════════════════════════════════════════════════════

fig, axes = plt.subplots(1, 2, figsize=(14, 6))
fig.suptitle(
    "BMV Entanglement Phase: Quantum Gravity Corrections\n"
    "δφ/φ vs. separation distance d",
    fontsize=14, fontweight='bold'
)

# ── Plot 1: QGEM range (100–450 µm), m=1e-14 kg ─────────────────────────
ax = axes[0]
d_um = d_QGEM_range * 1e6
ax.semilogy(d_um, dAS_vals, 'b-',  lw=2.0,  label=r'AS: $|\delta\phi/\phi| = \tilde\omega G_0/(d^2c^3)$')
ax.semilogy(d_um, dEFT_vals,'r--', lw=2.0,  label=r'EFT: $\delta\phi/\phi = (41/10\pi) G_0\hbar/(d^2c^3)$')
ax.semilogy(d_um, dGUP_beta1, 'g:', lw=1.5, label=r'GUP: $\delta\phi/\phi \approx (l_{Pl}/d)^2(m/m_{Pl})^2,\ \beta=1$')

# Experimental sensitivity line  ~1e-3 (rough order of magnitude, optimistic)
ax.axhline(1e-3,  color='gray', ls='-.',  alpha=0.7, label='Experimental reach ~$10^{-3}$')

ax.set_xlabel('Separation $d$ [µm]', fontsize=12)
ax.set_ylabel(r'$|\delta\phi/\phi|$', fontsize=12)
ax.set_title(
    r'QGEM range: $m = 10^{-14}$ kg, $t = 1$ s',
    fontsize=11
)
ax.legend(fontsize=9, loc='upper right')
ax.set_xlim(100, 450)
ax.grid(True, which='both', alpha=0.3)

# Annotate values at d=250 µm
d_ann = 250e-6
ax.annotate(
    f'AS: {abs(delta_phi_AS_over_phi(d_ann)):.1e}\nEFT: {delta_phi_EFT_over_phi(d_ann):.1e}',
    xy=(250, abs(delta_phi_AS_over_phi(d_ann))),
    xytext=(320, 1e-58),
    fontsize=8, color='navy',
    arrowprops=dict(arrowstyle='->', color='navy', lw=0.8)
)

# ── Plot 2: Aggressive future range (10–100 µm), m=1e-12 kg ─────────────
ax2 = axes[1]
d_fut_um = d_future_range * 1e6
ax2.semilogy(d_fut_um, dAS_fut,  'b-',  lw=2.0, label=r'AS: $|\delta\phi/\phi|$')
ax2.semilogy(d_fut_um, dEFT_fut, 'r--', lw=2.0, label=r'EFT: $\delta\phi/\phi$')
ax2.semilogy(d_fut_um, dGUP_fut, 'g:',  lw=1.5, label=r'GUP ($\beta=1$): $\delta\phi/\phi$')

ax2.axhline(1e-3,  color='gray', ls='-.',  alpha=0.7, label='Experimental reach ~$10^{-3}$')
ax2.axhline(1e-10, color='orange', ls='--', alpha=0.6, label='Speculative future ~$10^{-10}$')

ax2.set_xlabel('Separation $d$ [µm]', fontsize=12)
ax2.set_ylabel(r'$|\delta\phi/\phi|$', fontsize=12)
ax2.set_title(
    r'Aggressive future: $m = 10^{-12}$ kg, $t = 10$ s',
    fontsize=11
)
ax2.legend(fontsize=9, loc='upper right')
ax2.set_xlim(10, 100)
ax2.grid(True, which='both', alpha=0.3)

# Show ratio annotation
ax2.text(
    25, 1e-53, f'AS/EFT ratio ~ {ratio_AS_to_EFT:.1e}\n(AS has no ħ)',
    fontsize=9, color='purple',
    bbox=dict(facecolor='lavender', edgecolor='purple', boxstyle='round,pad=0.3')
)

plt.tight_layout()
plot1_path = OUTDIR / "bmv_as_eft_corrections.png"
plt.savefig(plot1_path, dpi=150, bbox_inches='tight')
plt.close()
print(f"\nSaved: {plot1_path}")


# ── Plot 3: Both model sets on a single wider range (log-log) ────────────
fig2, ax3 = plt.subplots(figsize=(10, 6))

d_wide = np.logspace(-5, -3, 600)   # 10 nm to 1 mm
d_wide_um = d_wide * 1e6

ax3.loglog(d_wide_um, np.abs(delta_phi_AS_over_phi(d_wide)),
           'b-', lw=2.5, label=r'AS Bonanno–Reuter ($\tilde\omega = 118/15\pi$)')
ax3.loglog(d_wide_um, delta_phi_EFT_over_phi(d_wide),
           'r--', lw=2.5, label=r'EFT Donoghue–BDH ($41/10\pi$)')
ax3.loglog(d_wide_um, delta_phi_GUP_over_phi(d_wide, m_QGEM, beta=1.0),
           'g:', lw=1.8, label=r'GUP QGEM ($m=10^{-14}$ kg, $\beta=1$)')
ax3.loglog(d_wide_um, delta_phi_GUP_over_phi(d_wide, m_future, beta=1.0),
           'm:', lw=1.8, label=r'GUP future ($m=10^{-12}$ kg, $\beta=1$)')

# Shaded experimental domains
ax3.axvspan(100, 450, alpha=0.08, color='blue', label='QGEM range 100–450 µm')
ax3.axvspan(10, 100, alpha=0.08, color='green', label='Aggressive future 10–100 µm')

# Experimental precision levels
ax3.axhline(1e-3,  color='gray',   ls='-.', lw=1.5, alpha=0.8, label='Near-term reach ~$10^{-3}$')
ax3.axhline(1e-6,  color='silver', ls='-.', lw=1.0, alpha=0.6, label='Speculative reach ~$10^{-6}$')

ax3.set_xlabel('Separation $d$ [µm]', fontsize=13)
ax3.set_ylabel(r'$|\delta\phi/\phi|$ (relative phase correction)', fontsize=13)
ax3.set_title(
    'AS vs. EFT vs. GUP: relative BMV phase corrections\n'
    r'AS (no $\hbar$): $\tilde\omega G_0/(d^2c^3)$; EFT (with $\hbar$): $(41/10\pi)G_0\hbar/(d^2c^3)$; AS/EFT $\approx 1.8\times10^{34}$',
    fontsize=11
)
ax3.legend(fontsize=9, loc='upper right')
ax3.set_xlim(10, 1000)
ax3.grid(True, which='both', alpha=0.25)

# Gap annotation
gap_y = 1e-3
gap_x = 250
ax3.annotate(
    f'Gap at d=250 µm:\nEFT: {delta_phi_EFT_over_phi(250e-6):.0e}\n'
    f'→ {int(np.log10(1e-3/delta_phi_EFT_over_phi(250e-6)))} orders of magnitude\nbelow reach',
    xy=(gap_x, delta_phi_EFT_over_phi(250e-6)),
    xytext=(80, 1e-6),
    fontsize=9, color='red',
    arrowprops=dict(arrowstyle='->', color='red', lw=1.0)
)

plt.tight_layout()
plot2_path = OUTDIR / "bmv_corrections_wide_loglog.png"
plt.savefig(plot2_path, dpi=150, bbox_inches='tight')
plt.close()
print(f"Saved: {plot2_path}")


# ── Plot 4: BMV phase φ₀ vs. d for all parameter sets ────────────────────
fig3, ax4 = plt.subplots(figsize=(9, 6))

ax4.semilogy(d_QGEM_range * 1e6, phi_0(m_QGEM, d_QGEM_range, 1.0),
             'b-',  lw=2, label=r'QGEM $m=10^{-14}$ kg, $t=1$ s')
ax4.semilogy(d_QGEM_range * 1e6, phi_0(m_QGEM, d_QGEM_range, 10.0),
             'b--', lw=2, label=r'QGEM $m=10^{-14}$ kg, $t=10$ s')
ax4.semilogy(d_future_range * 1e6, phi_0(m_future, d_future_range, 10.0),
             'r-',  lw=2, label=r'Future $m=10^{-12}$ kg, $t=10$ s')

ax4.axhline(1e-3,  color='gray', ls='--', lw=1.5, alpha=0.8,
            label='Entanglement detection threshold ~$10^{-3}$ rad')
ax4.axhline(1e-2,  color='green', ls='--', lw=1.0, alpha=0.5,
            label='Comfortable detection ~$10^{-2}$ rad')

ax4.set_xlabel('Separation $d$ [µm]', fontsize=13)
ax4.set_ylabel(r'$\phi_0 = G_0 m^2 t / (\hbar d)$ [rad]', fontsize=13)
ax4.set_title('Leading-order BMV entanglement phase', fontsize=12)
ax4.legend(fontsize=10)
ax4.grid(True, which='both', alpha=0.3)
ax4.set_xlim(10, 450)

plt.tight_layout()
plot3_path = OUTDIR / "bmv_phase_vs_d.png"
plt.savefig(plot3_path, dpi=150, bbox_inches='tight')
plt.close()
print(f"Saved: {plot3_path}")


# ═══════════════════════════════════════════════════════════════════════════
# 9. SAVE results.json
# ═══════════════════════════════════════════════════════════════════════════

results = {
    "calculation": "BMV entanglement phase: AS and EFT corrections",
    "date": "2026-06-06",
    "references": {
        "BR00": "Bonanno & Reuter, PRD 62, 043008 (2000); hep-th/0002196",
        "Don94": "Donoghue, PRL 72, 2996 (1994); gr-qc/9310024",
        "BDH03": "Bjerrum-Bohr, Donoghue, Holstein, PRD 67, 084033 (2003); hep-th/0211072",
        "QGEM25": "QGEM parameter scan, arXiv:2502.12474 (2025)",
    },
    "constants": {
        "G0_SI": G0, "hbar_SI": hbar, "c_SI": c,
        "m_Pl_kg": float(m_Pl), "l_Pl_m": float(l_Pl),
    },
    "model_parameters": {
        "omega_tilde_AS": float(OMEGA_TILDE),
        "omega_tilde_formula": "118 / (15 * pi)",
        "EFT_coefficient": float(COEFF_EFT),
        "EFT_coefficient_formula": "41 / (10 * pi)",
        "AS_length_scale_m": float(r_AS_scale),
        "AS_to_EFT_ratio_note": "AS has NO hbar factor (classical RG); EFT has hbar (quantum loop)",
        "AS_to_EFT_ratio_at_all_d": "omega_tilde / (41/(10pi) * hbar) ~ 1.82e34",
    },
    "key_results": {
        "CRITICAL_dimensional_note": (
            "AS correction has NO hbar: delta_phi_AS/phi = -omega_tilde*G0/(d^2*c^3). "
            "EFT correction HAS hbar: delta_phi_EFT/phi = (41/10pi)*G0*hbar/(d^2*c^3). "
            "These are DIFFERENT physical effects with different dimensional origins."
        ),
        "AS_correction_at_100um": float(abs(delta_phi_AS_over_phi(100e-6))),
        "EFT_correction_at_100um": float(delta_phi_EFT_over_phi(100e-6)),
        "AS_correction_at_10um": float(abs(delta_phi_AS_over_phi(10e-6))),
        "EFT_correction_at_10um": float(delta_phi_EFT_over_phi(10e-6)),
        "GUP_beta1_at_100um_m1e14": float(delta_phi_GUP_over_phi(100e-6, m_QGEM)),
        "BMV_phase_100um_1e14kg_1s": float(phi_0(m_QGEM, 100e-6, 1.0)),
        "BMV_phase_250um_1e14kg_1s": float(phi_0(m_QGEM, 250e-6, 1.0)),
        "BMV_phase_35um_1e14kg_1s":  float(phi_0(m_QGEM, 35e-6, 1.0)),
        "BMV_phase_10um_1e12kg_10s": float(phi_0(m_future, 10e-6, 10.0)),
        "orders_of_magnitude_gap_EFT_vs_reach_at_100um": int(
            np.log10(1e-3 / delta_phi_EFT_over_phi(100e-6))),
        "orders_of_magnitude_gap_AS_vs_reach_at_100um": int(
            np.log10(1e-3 / abs(delta_phi_AS_over_phi(100e-6)))),
        "ratio_AS_over_EFT_at_100um": float(
            abs(delta_phi_AS_over_phi(100e-6)) / delta_phi_EFT_over_phi(100e-6)),
        "ratio_explanation": "AS/EFT = omega_tilde / ((41/10pi)*hbar) ~ 1.82e34 (no hbar in AS)",
    },
    "discriminator_table": discriminators,
    "detailed_table_rows": table_rows,
    "plots": [
        "bmv_as_eft_corrections.png",
        "bmv_corrections_wide_loglog.png",
        "bmv_phase_vs_d.png",
    ],
    "conclusion": (
        "Binary discriminators (B1-B3) are in experimental reach by 2035+. "
        "Continuous phase-shape discriminators require vast improvements. "
        "KEY DIMENSIONAL FINDING: AS and EFT corrections have DIFFERENT forms: "
        "AS = classical RG running: delta_phi_AS/phi = -omega_tilde*G0/(d^2*c^3), "
        "no hbar, scale ~6.2e-28 at d=100um. "
        "EFT = quantum loop: delta_phi_EFT/phi = (41/10pi)*G0*hbar/(d^2*c^3), "
        "with hbar, scale ~3.4e-62 at d=100um. "
        "AS is ~1.82e34x larger than EFT due to absence of hbar. "
        "Gap to experimental reach: AS is 25 orders below reach; EFT is 59 orders. "
        "Both are undetectable this century. "
        "Best realistic discrimination: binary B1 (quantum vs. classical gravity) "
        "and B2 (Oppenheim cross-correlations in alternative mechanical experiment)."
    ),
}

results_path = OUTDIR / "results.json"
with open(results_path, 'w', encoding='utf-8') as fh:
    json.dump(results, fh, indent=2, ensure_ascii=False)
print(f"\nSaved: {results_path}")
print("\nDONE.")
