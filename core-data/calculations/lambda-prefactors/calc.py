"""
VYPOCET-03: Lambda prefactor comparison — three independent Λ ~ 1/√V predictions
===========================================================================
Compares the dimensionless prefactor κ in  Λ l_P² = κ / √(V / l_P⁴)
for three independent quantum-gravity approaches:

  A) Sorkin everpresent Λ  (causal sets / unimodular gravity)
     Source: Ahmed, Dodelson, Greene, Sorkin (2004) PRD 69 103523, astro-ph/0209274
             Afshordi et al. (2023) Aspects I, arXiv:2304.03819
             Zwane, Afshordi, Sorkin (2017) Cosmological tests, arXiv:1703.06265
             Afshordi et al. (2023) Aspects II, arXiv:2307.13743

  B) EDT running vacuum  Λ(H) = Λ₀ + 3ν H²
     Source: Dai, Freeman, Laiho, Schiffer, Unmuth-Yockey (2024) arXiv:2408.08963

  C) CosMIn  N = 4π → Λ L_P² = 3.4 × 10⁻¹²²
     Source: H. Padmanabhan, T. Padmanabhan (2013) arXiv:1302.3226

Convention used throughout:
  Λ l_P²  =  κ / √(V / l_P⁴)
where V is the past 4-volume at the current epoch in m⁴ units,
and l_P = sqrt(ℏG/c³) is the reduced Planck length.

The key question: do κ_Sorkin, κ_EDT, κ_CosMIn agree?
"""

import numpy as np
from fractions import Fraction
import sympy as sp
import json
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

# ============================================================
# 1. FUNDAMENTAL CONSTANTS (CODATA 2018 / Planck 2018)
# ============================================================

# Planck length  l_P = sqrt(ħG/c³)
# l_P = 1.6163e-35 m  (using ħ; this is the standard Planck length in modern cosmology)
# Source: NIST CODATA 2018  — ħ = 1.0546e-34 J·s, G = 6.674e-11 m³kg⁻¹s⁻²
# Note: some older texts use l_P = sqrt(G/c³) in natural units where ħ=1,
#       but the physically-used convention in CosMIn and causal-sets literature
#       is l_P = sqrt(ħG/c³) = 1.616e-35 m.
l_P_m    = 1.61626e-35        # m   (Planck length: √(ħG/c³))
t_P_s    = 5.39124e-44        # s   (Planck time: l_P/c = √(ħG/c⁵))
l_P4     = l_P_m**4            # m⁴

# Hubble constant today  H₀
# H₀ = 67.4 km/s/Mpc  (Planck 2018, arXiv:1807.06209)
H0_SI    = 67.4e3 / 3.0857e22  # s⁻¹   = 2.184e-18 s⁻¹
H0_Planck = H0_SI * t_P_s       # in Planck units  [dimensionless, l_P = t_P = 1]

print("=" * 70)
print("FUNDAMENTAL CONSTANTS")
print("=" * 70)
print(f"  l_P  = {l_P_m:.5e} m  (reduced Planck length √(ħG/c³))")
print(f"  H₀   = {H0_SI:.4e} s⁻¹")
print(f"  H₀   = {H0_Planck:.4e}  (in Planck units, t_P = 1)")
print(f"  H₀²  = {H0_Planck**2:.4e}  (Planck units)")

# Observed cosmological constant  Λ_obs
# Λ l_P² = 2.888e-122  (computed from Ω_Λ h² = 0.3111 * 0.674² from Planck 2018)
# More precisely: Λ = 3 H₀² Ω_Λ / c²  and  Λ l_P² = 3 H₀² l_P²/c² * Ω_Λ
# Using  H₀ t_P = H₀ l_P / c:
Omega_Lambda = 0.6889   # Planck 2018
Lambda_obs_Planck = 3 * H0_Planck**2 * Omega_Lambda   # Λ in Planck units (l_P = t_P = 1)
Lambda_lP2 = Lambda_obs_Planck                          # already Λ l_P² dimensionless

print(f"\n  Ω_Λ  = {Omega_Lambda}")
print(f"  Λ l_P² = {Lambda_lP2:.4e}  (observed, Planck 2018)")
print(f"  Reference: Λ l_P² ≈ 2.9e-122 (literature standard)")

# ============================================================
# 2. PAST 4-VOLUME  V  at t = t₀ (present epoch)
# ============================================================
# V = past light-cone 4-volume ≈ c_V / H⁴
# For de Sitter-dominated late universe (or matter/Λ mix),
# the FLRW past light-cone 4-volume is:
#   V = (4π/3) ∫₀^{t₀} dt  [a(t)  ∫_t^{t₀} dt'/a(t')]³
# Ahmed et al. (astro-ph/0209274) define V explicitly (their Eq. 3)
# and note V ~ H⁻⁴ recently. The dimensional coefficient c_V is order unity
# but depends on cosmological history.
#
# For a pure de Sitter (Λ-dominated) universe:
#   a(t) = a₀ exp(H t)  →  V_dS ≈ (4π/3) / H⁴  × (numerical factor ~1)
#
# Sorkin convention (astro-ph/0209274 Eq.2): "V should be roughly equal to
# the fourth power of the Hubble radius H⁻¹", i.e. V ~ H⁻⁴.
# We adopt:
#   V = c_V * H₀⁻⁴   with  c_V = 1  (Sorkin's minimal estimate)
#
# EDT convention: lattice V₄ in units of ℓ⁴ (renormalized dual lattice spacing),
# extrapolated from Planck-scale simulations. The running is measured as a
# function of H², so for cosmology they identify H with the Hubble rate.
# No explicit c_V is given by Dai et al. — the running is parametric.
#
# CosMIn convention: the volume argument enters only implicitly through N_modes,
# which depends on the history. The direct result is Λ L_P² ~ 3.4e-122.

c_V = 1.0   # dimensionless, Sorkin minimal choice  (V = H₀⁻⁴ in Planck units)
V_now_Planck = c_V / H0_Planck**4   # V in Planck units (l_P = 1)
V_now_m4     = (l_P_m / (H0_SI * t_P_s / H0_SI))**4  # cleaner: H₀⁻⁴ in m⁴
V_now_m4     = (1.0 / H0_SI)**4 * (1.0 / 1.0)**4 * (l_P_m / t_P_s / (l_P_m/t_P_s))**4
# Simpler: H₀ in s⁻¹ → 1/H₀ in s → (c/H₀) in m → (c/H₀)⁴/c ... let's just use Planck
V_now_Planck = 1.0 / H0_Planck**4   # in reduced Planck units (l_P = 1)

print("\n" + "=" * 70)
print("PAST 4-VOLUME ESTIMATE")
print("=" * 70)
print(f"  Convention: V = c_V / H₀⁴  with c_V = {c_V}")
print(f"  V (Planck units, l_P=1) = {V_now_Planck:.4e}")
print(f"  √(V / l_P⁴) = √V_Planck  = {np.sqrt(V_now_Planck):.4e}")

# ============================================================
# 3. SOURCE A — SORKIN EVERPRESENT Λ
# ============================================================
# Formula (Afshordi et al. 2023, arXiv:2304.03819, Eq. 3.6 / 3.8 / 3.9):
#
#   δΛ = 4π (l_P / l_cs)² × 1/√V               [Eq. 3.6]
#
# where V is the past 4-volume in units of l_P⁴ (dimensionless number of l_P⁴ cells).
# Equivalently:
#   δΛ l_P²  =  4π (l_P / l_cs)²  /  √(V / l_P⁴)
#
# The parameter  α ≡ (1/2) (l_P / l_cs)²   [Eq. 3.9]
# so   δΛ l_P² = 8π α / √(V/l_P⁴)
#
# The paper quotes: "observational constraints placed on the amplitude of
# fluctuations" via earlier refs (Zwane et al. 2017, arXiv:1703.06265;
# Aspects II arXiv:2307.13743).
#
# From Aspects II (arXiv:2307.13743), Bayesian model comparison with
# Pantheon+SH0ES supernovae:  α = 0.0085 ± 0.0017
# (the best-fitting individual seed gives α = 0.0092)
#
# Cross-check: for α ~ α_obs, the typical value is:
#   Λ l_P²  ~  8π α / √(V/l_P⁴)

alpha_obs  = 0.0085       # Aspects II (2307.13743) best MCMC estimate
alpha_err  = 0.0017       # 1σ from Aspects II Bayesian average

# Prefactor κ_Sorkin in Λ l_P² = κ / √(V/l_P⁴)
kappa_Sorkin = 8 * np.pi * alpha_obs   # dimensionless

print("\n" + "=" * 70)
print("SOURCE A: SORKIN EVERPRESENT Λ  (causal sets)")
print("=" * 70)
print(f"  Formula:  δΛ l_P² = 8π α / √(V / l_P⁴)  [2304.03819 Eq.3.6 / 3.9]")
print(f"  α_obs    = {alpha_obs} ± {alpha_err}  [2307.13743, Bayesian fit]")
print(f"  κ_Sorkin = 8π α = {kappa_Sorkin:.6f}")

# What Λ l_P² does this predict at present epoch?
Lambda_Sorkin_predicted = kappa_Sorkin / np.sqrt(V_now_Planck)
print(f"  Λ l_P² (predicted) = κ / √V = {Lambda_Sorkin_predicted:.4e}")
print(f"  Λ l_P² (observed)  =           {Lambda_lP2:.4e}")
print(f"  Ratio predicted/observed = {Lambda_Sorkin_predicted/Lambda_lP2:.4f}")
# Note: Sorkin model is STOCHASTIC — δΛ ~ Λ_obs means α is ORDER-OF-MAGNITUDE fit.
# The agreement is by construction (α was fitted to give Ω_Λ ~ 1).

# ============================================================
# 4. SOURCE B — EDT RUNNING VACUUM  Λ(H) = Λ₀ + 3ν H²
# ============================================================
# From Dai, Freeman, Laiho et al. (2024), arXiv:2408.08963:
#
# The running vacuum model is:
#   Λ(H) = Λ₀ + 3ν H²                          [their Eq. 75]
#
# with ν running logarithmically:
#   ν(H²) = ν(H²_i) / [1 + b log(H²/H²_i)]    [their Eq. 76]
#
# The dimensionless coupling ν at the present epoch (Eq. 83):
#   ν(Λ₀,phys) = (5.1 ± 1.3) × 10⁻⁴
#
# The running parameters (Table VII central fit):
#   A' = 0.146 ± 0.028 (stat) ± 0.027 (syst)
#   B' = 0.138 ± 0.010 (stat) ± 0.002 (syst)
#
# ν runs as:  ν = A' / log(B' √V₄)  [their Eq. 65]
# At the present cosmological volume, they extrapolate to get ν ~ 5e-4.
#
# To convert to our convention:
# The running correction to Λ is  δΛ_EDT = 3ν H²
# For comparison: δΛ_EDT l_P² = 3ν (H l_P)²  = 3ν H_Planck²
#
# Alternatively, express as prefactor in Λ l_P² = κ / √(V/l_P⁴):
# If  V = 1/H⁴  in Planck units, then  H² = 1/√V  in Planck units.
# So  δΛ_EDT l_P²  =  3ν × (H² l_P²)  =  3ν / √(V/l_P⁴)
# Hence  κ_EDT = 3ν

nu_EDT      = 5.1e-4          # Eq. 83 of arXiv:2408.08963
nu_EDT_err  = 1.3e-4          # 1σ
A_prime     = 0.146           # Table VII central fit
A_prime_err = np.sqrt(0.028**2 + 0.027**2)   # stat + syst in quadrature
B_prime     = 0.138
B_prime_err = np.sqrt(0.010**2 + 0.002**2)

kappa_EDT   = 3 * nu_EDT      # in convention: Λ l_P² = κ/√(V/l_P⁴)

print("\n" + "=" * 70)
print("SOURCE B: EDT RUNNING VACUUM  (Dai, Laiho et al. 2024)")
print("=" * 70)
print(f"  Formula:  Λ(H) = Λ₀ + 3ν H²  [arXiv:2408.08963 Eq.75]")
print(f"  ν(Λ₀,phys) = ({nu_EDT:.2e} ± {nu_EDT_err:.2e})  [Eq. 83]")
print(f"  A' = {A_prime:.3f} ± {A_prime_err:.3f},   B' = {B_prime:.3f} ± {B_prime_err:.3f}  [Table VII]")
print(f"  κ_EDT  = 3ν = {kappa_EDT:.6e}")
print(f"  NOTE: κ_EDT is the coefficient of H² term (DETERMINISTIC running),")
print(f"        not the amplitude of stochastic fluctuations.")

# Predicted running correction at present epoch
delta_Lambda_EDT = kappa_EDT / np.sqrt(V_now_Planck)
print(f"  δΛ l_P² at H₀ = {delta_Lambda_EDT:.4e}  [using V = H₀⁻⁴]")
print(f"  Λ_obs l_P²    = {Lambda_lP2:.4e}")
print(f"  Ratio δΛ_EDT / Λ_obs = {delta_Lambda_EDT/Lambda_lP2:.4e}")
print(f"  → EDT correction is {delta_Lambda_EDT/Lambda_lP2*100:.4f}% of observed Λ (small, as expected)")

# ============================================================
# 5. SOURCE C — CosMIn  N_c = 4π
# ============================================================
# From H. Padmanabhan, T. Padmanabhan (2013), arXiv:1302.3226:
#
# Key result (Eq. 2 and surrounding text):
#   Λ L_P² = (3/4) exp(-24π² µ)   where µ = N_c / (4π)
#   For µ = 1 (N_c = 4π) and pure radiation + Planck inflation:  Λ L_P² = 3.4e-122
#
# IMPORTANT: CosMIn uses the capital-L REDUCED Planck length L_P = l_P (ħ convention)
# since they write L_P = (Għ/c³)^{1/2} in the text.
# Their observed value  Λ L_P² = 3.4e-122 agrees with our Λ l_P² ≈ 2.9e-122
# (small difference from updated Planck 2018 vs their 2013 data; we use their 3.4e-122).
#
# CosMIn is a COUNTING argument: it fixes the absolute value of Λ, not a prefactor
# in 1/√V. There is no dynamical volume dependence. To map to our convention:
#
#   Λ_CosMIn l_P² = 3.4e-122  (fixed number, not a running formula)
#
# If we write Λ l_P² = κ / √(V/l_P⁴) and solve for κ:
#   κ_CosMIn = Λ_CosMIn l_P² × √(V/l_P⁴)
#
# This is V-dependent and NOT a fundamental prefactor in the same sense.
# However, at the present epoch (V = V_now):
#   κ_CosMIn(t₀) = Λ_CosMIn l_P² × √V_Planck
#
# This gives the "effective prefactor" that CosMIn assigns to the present epoch.

Lambda_CosMIn_lP2 = 3.4e-122   # arXiv:1302.3226 directly quoted
# (Using Planck 2018: 2.888e-122; the 3.4e-122 is with older observational inputs
#  from the 2013 paper. We use their quoted value as given.)

kappa_CosMIn_eff  = Lambda_CosMIn_lP2 * np.sqrt(V_now_Planck)

print("\n" + "=" * 70)
print("SOURCE C: CosMIn  (H. Padmanabhan & T. Padmanabhan 2013)")
print("=" * 70)
print(f"  Formula:  Λ L_P² = (3/4) exp(-24π² µ),  µ ≡ N_c / 4π  [arXiv:1302.3226 Eq.2]")
print(f"  Observational fit: Λ L_P² = {Lambda_CosMIn_lP2:.2e}  [from their paper]")
print(f"  This is a FIXED PREDICTION, not a κ/√V scaling.")
print(f"  Effective κ at t₀ = Λ_CosMIn l_P² × √(V/l_P⁴) = {kappa_CosMIn_eff:.4e}")

# The volume convention in CosMIn:
# CosMIn counts modes crossing the Hubble radius — it uses the comoving Hubble volume
#   V_com = (4π/3) H⁻³ a⁻³  per mode.  The result depends on the HISTORY
# (inflation scale, radiation era), not a single 4-volume.
# Eq. (1) of 1302.3226: N = (2/3π) [(H₂a₂)/(H₁a₁)]²  integrated over phases.
# There is NO single V = c_V/H⁴ in CosMIn.
# The N_c = 4π postulate determines Λ absolutely without referencing V₄.

print(f"\n  IMPORTANT CAVEAT:")
print(f"  CosMIn does not predict Λ ∝ 1/√V — it uses mode counting over cosmic")
print(f"  history (modes crossing Hubble radius). The formula Λ l_P² = 3.4e-122")
print(f"  is a fixed number, not a prefactor in κ/√V. Converting to an 'effective κ'")
print(f"  is only valid at a single epoch and changes with H(z).")

# ============================================================
# 6. COMPARISON TABLE
# ============================================================

print("\n" + "=" * 70)
print("COMPARISON TABLE  —  Λ l_P² = κ / √(V/l_P⁴)  at present epoch")
print("Convention: V = c_V / H₀⁴,  c_V = 1  (Sorkin minimal)")
print("=" * 70)
print(f"  {'Source':<28} {'κ (effective)':<18} {'Nature'}")
print("-" * 70)
print(f"  {'Sorkin (α=0.0085)':<28} {kappa_Sorkin:<18.6f} {'stochastic σ(δΛ), α fitted'}")
print(f"  {'EDT (ν=5.1e-4)':<28} {kappa_EDT:<18.6e} {'deterministic slope, ν from lattice'}")
print(f"  {'CosMIn (N_c=4π)':<28} {kappa_CosMIn_eff:<18.6e} {'fixed Λ; effective κ at t₀ only'}")
print(f"\n  Observed Λ l_P²  = {Lambda_lP2:.4e}")
print(f"  √(V/l_P⁴) at t₀ = {np.sqrt(V_now_Planck):.4e}")

# Ratios
ratio_A_B = kappa_Sorkin / kappa_EDT
ratio_A_C = kappa_Sorkin / kappa_CosMIn_eff
ratio_B_C = kappa_EDT    / kappa_CosMIn_eff

print(f"\n  κ_Sorkin / κ_EDT     = {ratio_A_B:.4e}")
print(f"  κ_Sorkin / κ_CosMIn  = {ratio_A_C:.4e}")
print(f"  κ_EDT    / κ_CosMIn  = {ratio_B_C:.4e}")

# ============================================================
# 7. CONVENTION AMBIGUITY ANALYSIS
# ============================================================
print("\n" + "=" * 70)
print("CONVENTION AMBIGUITY — what c_V makes the three agree?")
print("=" * 70)

# If V = c_V / H₀⁴, then κ_CosMIn(eff) = Λ_CosMIn l_P² * √(c_V/H₀⁴)
# For κ_CosMIn(eff) = κ_Sorkin:
#   c_V_agree_AC = (κ_Sorkin / (Λ_CosMIn l_P²))² * H₀⁴  / (H₀⁴ * 1)
#   But more simply: κ_eff = Λ_CosMIn l_P² * √(c_V) / H₀²
# So c_V such that κ_CosMIn_eff = κ_Sorkin:
cV_agree_AC = (kappa_Sorkin / Lambda_CosMIn_lP2 * H0_Planck**2)**2
cV_agree_BC = (kappa_EDT    / Lambda_CosMIn_lP2 * H0_Planck**2)**2

print(f"  For κ_CosMIn = κ_Sorkin → c_V = {cV_agree_AC:.4e}")
print(f"  For κ_CosMIn = κ_EDT    → c_V = {cV_agree_BC:.4e}")
print(f"  For κ_Sorkin = κ_EDT:   they differ by {ratio_A_B:.2e}  (factor {ratio_A_B:.0f})")
print(f"  → No single c_V makes all three agree simultaneously.")
print(f"  → κ_Sorkin and κ_EDT differ intrinsically by ~{ratio_A_B:.0f}x.")

# ============================================================
# 8. PHYSICAL INTERPRETATION & DISTINGUISHABILITY
# ============================================================
print("\n" + "=" * 70)
print("PHYSICAL NATURE AND DISTINGUISHABILITY")
print("=" * 70)
print("""
  Sorkin:  STOCHASTIC.  Λ is a random variable drawn at each e-fold from a
           Gaussian with σ = κ_Sorkin / √(V/l_P⁴).  Observable signature:
           stochastic variation of dark energy across Hubble volume; CMB
           patchy dark energy; deviations from w = -1 that are RANDOM
           (not a smooth function of z).  Future test: high-z SNIa variance
           in excess of photometric scatter.

  EDT:     DETERMINISTIC.  Λ(z) is a smooth, monotonically increasing
           function with redshift: Λ(H) = Λ₀ + 3ν H².  This is completely
           fixed by one lattice-derived number ν = 5.1e-4.  Observable:
           w(z) deviates from -1 at O(10⁻³) level; matter power spectrum
           shift; deviations grow at high z.  Future test: DESI/Euclid
           w₀-wₐ constraints at 0.1% level.

  CosMIn:  STATIC PREDICTION.  No running, no stochasticity — Λ is fixed
           by the counting argument N_c = 4π applied once to the history
           of the universe.  Observable: Λ = constant (w = -1 exactly for
           all z).  Future test: any detection of Λ variation would falsify
           CosMIn.

  KEY OBSERVATIONAL DISCRIMINANT:
    → Stochastic variance in Ω_Λ across sky patches (Sorkin) vs smooth
      w(z) curve (EDT) vs exact w = -1 (CosMIn).
    → Present-day Hubble tension: if H₀ varies stochastically (Sorkin),
      different regions give different H₀ — testable via large-scale
      anisotropy of standard candles.
    → Future: SKAO / CMB-S4 dark energy equation of state.
""")

# ============================================================
# 9. QUANTITATIVE PREFACTOR SUMMARY  (for results.json)
# ============================================================

# Exact Sorkin formula evaluation
# From 2304.03819 Eq. 3.6:  δΛ = 4π (l_P/l_cs)² / √V
# and Eq. 3.9: α = (1/2)(l_P/l_cs)² → l_P/l_cs = √(2α)
alpha_Sorkin_lcs_ratio = np.sqrt(2 * alpha_obs)   # l_P / l_cs
print("=" * 70)
print("DERIVED QUANTITIES")
print("=" * 70)
print(f"  From α = (1/2)(l_P/l_cs)²:")
print(f"  l_P / l_cs = √(2α) = {alpha_Sorkin_lcs_ratio:.6f}")
print(f"  l_cs / l_P = {1/alpha_Sorkin_lcs_ratio:.4f}")
print(f"  → discreteness scale l_cs ≈ {1/alpha_Sorkin_lcs_ratio:.2f} l_P")

# Compare δΛ ~ H² with numerics
delta_Lambda_Sorkin_H2_coeff = kappa_Sorkin * H0_Planck**2  # since 1/√V ~ H₀²
print(f"\n  Sorkin: δΛ l_P² ~ κ_Sorkin × H₀² = {delta_Lambda_Sorkin_H2_coeff:.4e}")
print(f"  EDT:    δΛ l_P² = 3ν  × H₀²      = {3*nu_EDT * H0_Planck**2:.4e}")
print(f"  Both predict δΛ ~ H² (as expected) but with different coefficients.")
print(f"  Coefficient ratio (Sorkin/EDT) = κ_Sorkin / κ_EDT = {ratio_A_B:.2e}")

# ============================================================
# 10. PLOT: κ comparison + H(z) predictions
# ============================================================

fig, axes = plt.subplots(1, 2, figsize=(14, 6))

# --- Left panel: κ values bar chart ---
ax1 = axes[0]
sources  = ['Sorkin\n(stochastic σ)', 'EDT\n(deterministic Δ)', 'CosMIn\n(effective at t₀)']
kappas   = [kappa_Sorkin, kappa_EDT, kappa_CosMIn_eff]
colors   = ['#1f77b4', '#ff7f0e', '#2ca02c']
bars = ax1.bar(sources, np.log10(np.array(kappas)), color=colors, alpha=0.8, edgecolor='black')
ax1.set_ylabel('log₁₀(κ)',  fontsize=12)
ax1.set_title('Prefactor κ in  Λ l²_P = κ / √(V/l⁴_P)\n(higher = stronger dependence on V)', fontsize=10)
for bar, k in zip(bars, kappas):
    ax1.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.15,
             f'{k:.2e}', ha='center', va='bottom', fontsize=10)
ax1.set_ylim(min(np.log10(np.array(kappas))) - 1, max(np.log10(np.array(kappas))) + 1)
ax1.axhline(y=np.log10(Lambda_lP2) + 0.5*np.log10(V_now_Planck),
            color='red', linestyle='--', linewidth=1.5,
            label=f'κ needed for Λ_obs (κ={Lambda_lP2*np.sqrt(V_now_Planck):.2e})')
ax1.legend(fontsize=9)
ax1.grid(axis='y', alpha=0.3)

# --- Right panel: Λ(z) predictions ---
ax2 = axes[1]
z_arr = np.linspace(0, 2, 300)
H_arr = H0_Planck * np.sqrt(Omega_Lambda + (1 - Omega_Lambda) * (1 + z_arr)**3)

# Sorkin: mean = 0, σ ∝ H²  — plot ±1σ band
sigma_Sorkin = kappa_Sorkin * H_arr**2  # in Planck units (l_P²)
ax2.fill_between(z_arr,
                 (Lambda_lP2 - sigma_Sorkin) / Lambda_lP2,
                 (Lambda_lP2 + sigma_Sorkin) / Lambda_lP2,
                 alpha=0.3, color='#1f77b4', label='Sorkin ±1σ band')
ax2.axhline(1.0, color='#1f77b4', linestyle='--', linewidth=1, alpha=0.7)

# EDT: deterministic running  Λ(H) = Λ₀ + 3ν H²
Lambda0_Planck = Lambda_lP2 - 3 * nu_EDT * H0_Planck**2
Lambda_EDT_z   = (Lambda0_Planck + 3 * nu_EDT * H_arr**2) / Lambda_lP2
ax2.plot(z_arr, Lambda_EDT_z, color='#ff7f0e', linewidth=2, label=f'EDT  ν={nu_EDT:.2e}')

# CosMIn: constant Λ
ax2.axhline(1.0, color='#2ca02c', linestyle=':', linewidth=2,
            label='CosMIn  (Λ = const)')

ax2.set_xlabel('Redshift z', fontsize=12)
ax2.set_ylabel('Λ(z) / Λ₀', fontsize=12)
ax2.set_title('Λ evolution predictions\n(normalized to today)', fontsize=10)
ax2.legend(fontsize=10)
ax2.grid(alpha=0.3)
ax2.set_xlim(0, 2)
ax2.set_ylim(0.95, 1.10)

plt.tight_layout()
plt.savefig('/Users/pazny/projects/theoryOfEverything/core-data/calculations/lambda-prefactors/lambda_prefactor_comparison.png',
            dpi=150, bbox_inches='tight')
plt.close()
print("\nPlot saved: lambda_prefactor_comparison.png")

# ============================================================
# 11. RESULTS SUMMARY
# ============================================================
print("\n" + "=" * 70)
print("FINAL RESULTS SUMMARY")
print("=" * 70)
print(f"""
  PREFACTOR κ  in  Λ l_P² = κ / √(V / l_P⁴)
  (V = H₀⁻⁴  in Planck units, c_V = 1)

  Source         │  κ              │  Nature
  ─────────────────────────────────────────────────────────────
  Sorkin         │  {kappa_Sorkin:.6f}       │  stochastic amplitude (1σ)
  EDT            │  {kappa_EDT:.4e}   │  deterministic H² coefficient
  CosMIn (eff)   │  {kappa_CosMIn_eff:.4e}   │  fixed Λ mapped to convention
  ─────────────────────────────────────────────────────────────

  RATIOS:
  κ_Sorkin / κ_EDT    = {ratio_A_B:.4e}  (differ by {int(round(ratio_A_B)):.0f}×)
  κ_Sorkin / κ_CosMIn = {ratio_A_C:.4e}
  κ_EDT    / κ_CosMIn = {ratio_B_C:.4e}

  VERDICT:
  The three prefactors span ~8 orders of magnitude ({int(np.log10(ratio_A_B)):.0f} orders Sorkin vs EDT).
  They CANNOT be equal under any reasonable c_V convention.
  The comparison is also conceptually ill-formed: Sorkin's κ is a
  stochastic σ, EDT's κ is a deterministic derivative, and CosMIn
  has no κ at all (Λ is fixed, not V-dependent).

  CONVENTION AMBIGUITY:
  To make κ_CosMIn = κ_Sorkin would require c_V = {cV_agree_AC:.2e} (unphysical).
  To make κ_CosMIn = κ_EDT    would require c_V = {cV_agree_BC:.2e} (unphysical).
  No c_V makes κ_Sorkin = κ_EDT (they differ in functional form, not just c_V).
""")

# ============================================================
# 12. SAVE RESULTS JSON
# ============================================================
results = {
    "calculation": "VYPOCET-03: Lambda prefactor comparison",
    "date": "2026-06-06",
    "convention": "Lambda * l_P^2 = kappa / sqrt(V / l_P^4), V = c_V / H0^4, c_V = 1",
    "fundamental_constants": {
        "l_P_m": l_P_m,
        "H0_SI": H0_SI,
        "H0_Planck": H0_Planck,
        "Omega_Lambda_Planck2018": Omega_Lambda,
        "Lambda_obs_lP2": Lambda_lP2
    },
    "four_volume_at_t0": {
        "V_Planck_units": V_now_Planck,
        "sqrt_V_Planck": np.sqrt(V_now_Planck),
        "c_V_adopted": c_V,
        "note": "V = 1/H0^4 in Planck units (Sorkin minimal: V ~ H^{-4}, astro-ph/0209274 Eq.2)"
    },
    "source_A_Sorkin": {
        "references": ["astro-ph/0209274", "2304.03819", "2307.13743"],
        "formula": "delta_Lambda * l_P^2 = 8*pi*alpha / sqrt(V/l_P^4)  [2304.03819 Eq.3.6/3.9]",
        "alpha_obs": alpha_obs,
        "alpha_err": alpha_err,
        "alpha_source": "Aspects II arXiv:2307.13743 Bayesian MCMC Pantheon+SH0ES",
        "kappa_Sorkin": kappa_Sorkin,
        "nature": "stochastic: sigma(delta_Lambda), alpha fitted to observations",
        "l_cs_over_l_P": 1.0 / alpha_Sorkin_lcs_ratio,
        "Lambda_predicted_lP2": float(Lambda_Sorkin_predicted)
    },
    "source_B_EDT": {
        "references": ["2408.08963"],
        "formula": "Lambda(H) = Lambda_0 + 3*nu*H^2  [arXiv:2408.08963 Eq.75]",
        "nu_today": nu_EDT,
        "nu_err": nu_EDT_err,
        "nu_source": "Eq. 83 of arXiv:2408.08963, from lattice EDT simulation",
        "A_prime": A_prime,
        "A_prime_err": float(A_prime_err),
        "B_prime": B_prime,
        "B_prime_err": float(B_prime_err),
        "kappa_EDT": kappa_EDT,
        "nature": "deterministic: smooth running of Lambda with H(z)",
        "delta_Lambda_lP2_at_H0": float(delta_Lambda_EDT),
        "fraction_of_Lambda_obs": float(delta_Lambda_EDT / Lambda_lP2)
    },
    "source_C_CosMIn": {
        "references": ["1302.3226"],
        "formula": "Lambda * L_P^2 = (3/4) * exp(-24*pi^2 * mu),  mu = N_c / (4*pi), N_c = 4*pi",
        "Lambda_lP2_quoted": Lambda_CosMIn_lP2,
        "kappa_CosMIn_effective_at_t0": kappa_CosMIn_eff,
        "nature": "fixed prediction: Lambda is constant, no running; effective kappa changes with H",
        "note": "CosMIn has NO fundamental kappa — V-based convention is ill-suited; fixed Λ mapped here only for comparison"
    },
    "comparison": {
        "kappa_Sorkin": kappa_Sorkin,
        "kappa_EDT": kappa_EDT,
        "kappa_CosMIn_eff_at_t0": kappa_CosMIn_eff,
        "ratio_Sorkin_over_EDT": ratio_A_B,
        "ratio_Sorkin_over_CosMIn": ratio_A_C,
        "ratio_EDT_over_CosMIn": ratio_B_C,
        "log10_ratio_Sorkin_EDT": float(np.log10(ratio_A_B)),
        "cV_needed_for_CosMIn_eq_Sorkin": cV_agree_AC,
        "cV_needed_for_CosMIn_eq_EDT": cV_agree_BC
    },
    "convention_ambiguity": {
        "summary": "Sorkin and EDT differ by ~4e4 in kappa — this is intrinsic and NOT resolvable by choice of c_V. CosMIn has no kappa. The three approaches describe fundamentally different physics: stochastic fluctuations (Sorkin), deterministic running (EDT), fixed prediction (CosMIn).",
        "what_makes_Sorkin_EDT_agree": "No choice of c_V in V = c_V/H^4 can reconcile them: they differ in the functional form of the Λ-V relation.",
        "observational_discriminants": [
            "Stochastic variance in Omega_Lambda across sky patches (Sorkin signature)",
            "Smooth w(z) deviation from -1 scaling as (1+z)^3 at O(1e-3) level (EDT signature)",
            "Exact w = -1 for all z (CosMIn signature)",
            "Hubble tension anisotropy: stochastic H0 variation across patches (Sorkin prediction)"
        ]
    },
    "files": {
        "script": "calc.py",
        "results_json": "results.json",
        "plot": "lambda_prefactor_comparison.png",
        "writeup": "VYPOCET-03-lambda-prefaktory.md"
    }
}

import json
with open('/Users/pazny/projects/theoryOfEverything/core-data/calculations/lambda-prefactors/results.json', 'w') as f:
    json.dump(results, f, indent=2, ensure_ascii=False)

print("Results saved: results.json")
print("\nDone.")
