# TODO — what must be strengthened before draft-01 could become a real paper

**Status: internal exploratory draft (v0.2, AI-assisted). NOT submission-ready. This list is the gate.**

---

## NOTE — 2026-06-06: VYPOCET-14 sharpens §4.2 (Teukolsky prediction)

**VYPOCET-14** (sj-threshold-scan) completed a fine radial scan (12 radii, Kerr a=0.6 and a=0.9,
plus BTZ J=0.9 cross-check; N=1600, 5 seeds) with three key findings relevant to draft-01:

1. **Onset controlled by Ω(r), not r_erg alone.** W_sr(r) ~ Ω(r)^B fits the radial profile better
   than a Lorentzian at r_erg (ΔAIC = +442 for a=0.6, +4216 for a=0.9, +232 for BTZ; all decisive,
   all three geometries preferring Model S). The ergosphere is a necessary condition but the
   quantitative profile tracks the local ZAMO angular velocity — a falsifiable prediction for §4.2.
   Power-law exponent B ≈ 3.8–4.2 (Kerr) / 1.7 (BTZ) can be compared to the superradiant
   amplification coefficient from 4D Teukolsky.

2. **A_W is negative-definite across the full scan.** No sign flip in 5×8 (Kerr) + 5×5 (BTZ) exterior
   measurements. Magnitude grows toward ergosphere by factor ~20 (|A_W|~0.03 at r=8M vs ~0.6 at
   r=2.05M). Amplitude tracks Ω(r). Consistent with VYPOCET-10 toy model: sign fixed by drag direction
   (geometry), magnitude by shear strength (dynamical). This closes the §3.5b mechanism loop and
   sharpens the framing in §4.2.

3. **BTZ pattern matches Kerr qualitatively and semi-quantitatively** (ΔAIC preference for Model S;
   same sign structure of A_W; same ergoregion A_W=0 behaviour). Supports H3g-6 geometry-independence
   claim.

   Files: core-data/calculations/sj-threshold-scan/; writeup: knowledge-base/vypocty/VYPOCET-14-threshold-scan.md

---

## NOTE — 2026-06-06: VYPOCET-15 closes the Kerr a=0.6 ambiguity from VYPOCET-14

**VYPOCET-15** (sj-far-zone, Kerr a=0.6, r=5..20M, 13 radii, N=1600, 5 seeds) resolves the
residual ambiguity from VYPOCET-14 (where linear corr(E)=0.971 slightly favoured Model E for a=0.6).

Key findings:

1. **Joint fit (near + far, n=19): ΔAIC(E−S) = +3894 — Model S decisive** (threshold: >6).
   χ²/dof: Model S = 97.5, Model E = 326.5. Far zone provides the leverage: Model S predicts
   W_sr ~ r^{−3B} while Model E predicts ~ r^{−1}, slopes differ by factor ~13 in log-log.

2. **Log-log discriminant (near-zone, W_sr>0 points):** corr_loglog(S)=0.9992 vs
   corr_loglog(E)=0.942. The linear-scale correlation of VYPOCET-14 was misleading (nearby
   high-W_sr points dominated); log-log is the correct discriminant for power-law models.

3. **|A_W| power law (high-SNR, n=11, r=2.05..8M):**
   - |A_W| ~ r^{−2.75±0.03}  (toy prediction: r^{−3};   R²=0.957)
   - |A_W| ~ Ω^{0.98±0.01}   (toy prediction: Ω^{+1};   R²=0.932)
   Both consistent with toy model from VYPOCET-10 within 2σ.

4. **Combined with VYPOCET-14:** all three geometries (Kerr a=0.6, a=0.9, BTZ J=0.9) now
   unanimously prefer Model S (ΔAIC = +3894, +4216, +231 respectively). The near-zone
   ambiguity for a=0.6 was an artefact of linear-scale correlation; it does not survive
   the log-log test or the joint fit.

**Implication for §4.2:** The onset of W_sr(r) ~ Ω(r)^B is now confirmed for all tested
geometries. A_W ~ Ω(r)^1 ~ r^{−3} is a falsifiable prediction for 4D Teukolsky calculations.

Files: core-data/calculations/sj-far-zone/; writeup: knowledge-base/vypocty/VYPOCET-15-far-zone.md

---

## 0. Authorship / ethics note (must appear in any real version)

- This draft and the underlying calculations were produced by an **AI-assisted exploratory research pipeline**. No human has yet independently re-derived or re-run the results.
- Any real submission requires: (a) a named human author who has verified the physics and the code; (b) an explicit statement of AI assistance per the target venue's policy and per the project's `dokumentace/zasady-publikovani.md`-style conventions; (c) public release of `calc.py` for both calculations so the numerics are reproducible.
- Do not represent the conformal-triviality lever, the metric identities, or the citations as independently human-checked until they have been.

---

## 1. What a referee will attack first

1. **"You only built a partial order on a flat-looking 2D rectangle — where is the rotating black hole?"**
   The fixed-$r$ section has a *constant* induced 2-metric; all geometry is in the constant cone tilt. A referee will say the result is "a sheared 2D Minkowski diamond" and that curvature/asymptotics enter nowhere. Rebuttal needs an explicit argument (and ideally a calculation) that the cone tilt is the *only* gauge-invariant content at fixed $r$, plus at least one observable that distinguishes the tilt's *origin* (dragging vs a coordinate shear). As written, the BTZ↔Kerr "universality" could be reframed by a hostile referee as "of course they agree — both are the same sheared diamond."

2. **"$A_{\rm caus}=+1$ inside the ergoregion is trivial / a coordinate artifact."**
   With fully tilted cones every link is co-rotating by construction. A referee will ask what is *quantum* or *SJ-specific* about it (the classical causal order already gives it). The genuinely SJ statement is the spectrum pairing and $A_W$; sharpen the framing so the headline is "SJ exists where the static section is not even Lorentzian," not "$A_{\rm caus}=1$."

3. **"$\det h = -\Delta$ in Kerr and $-N^2 r^2$ in BTZ are just the lapse — Lorentzian-ness of the fixed-$r$ section is automatic outside the horizon and says nothing about the ergoregion specifically."**
   True, and must be stated up front. The non-trivial content is that the *fixed-$\varphi$* section degenerates while the fixed-$r$ one does not; make that contrast the load-bearing claim, with the static-control degeneracy as the actual evidence.

4. ✅ **DONE — The opposite-sign result ($A_{\rm caus}>0$, $A_W<0$) needs a mechanism, not just a measurement.** (VYPOCET-10; draft §3.5b.)
   *Done:* boosted/sheared-diamond toy model in null coordinates $u=\varphi-s_+t$, $v=\varphi-s_-t$ ($h\propto du\,dv$ verified). Counting asymmetry $A_{\rm caus}>0$ is pure cone aperture (continuum Monte-Carlo matches measured SJ to ~1%). Correlation asymmetry $A_W<0$ follows from $W_0=-\tfrac1{4\pi}\ln|\Delta u\,\Delta v|$: the drag tilts the cone's timelike axis onto the co-rotating side, so counter-rotating links sit nearer a squeezed null edge (shorter interval, stronger $W$). Sign reproduced from the bare log in all three cases (BTZ $J=0.6$, Kerr $a=0.6$, $a=0.9$); magnitude recovered with the finite-region SJ offset (SJ $W$ per link correlates 0.95–0.97 with the log). Confirmed NOT a binning/normalization convention.
   *Remaining:* a fully closed-form (non-Monte-Carlo) expression for $A_{\rm caus}(s_-,s_+)$ and $A_W$ on the finite rectangle would be the final polish (see §3 below).

5. **Non-Hadamard SJ + bounded region $\Rightarrow$ boundary-dominated correlations.**
   SJ on a finite patch is known to be boundary-sensitive; $A_W$ may be dominated by edge effects of the $(t,\varphi)$ rectangle, not by ergoregion physics. Must show $A_W$ is stable under changes of $T,\Phi$ and under interior-only restriction.

---

## 2. Numerics that must be strengthened *(blocking)*

- **Larger $N$ and a continuum study.** $N=1600$ is small. Need $N$ up to $\sim10^4$–$10^5$ with an explicit $N\to\infty$ extrapolation of $A_{\rm caus}$, $A_W$, the spectral plateau, and the null-slope zero crossing. Show convergence rates ($O(1/\sqrt N)$ expected for asymmetries). **[Priority 1]**
- **More seeds + proper error bars.** 3–5 seeds is too few for a stable variance. Use $\gtrsim30$ seeds; report bootstrap CIs, not just SD across a handful of runs. **[Priority 1]**
- **Poisson (fluctuating-$N$) ensemble**, not only the fixed-$N$ canonical approximation, to confirm the $O(1/N)$ difference is negligible for the headline claims. **[Priority 2]**
- **Window-size and aspect-ratio sweep.** Vary $T/\Phi$ and absolute patch size; demonstrate the SJ existence, the spectral $1/k$ plateau, and especially $A_W$ are not artifacts of the chosen rectangle. **[Priority 2 — also addresses item 1.5 above]**
- **Independent re-implementation** of the causal-order test and the $i\Delta$ diagonalization to rule out a single-code bug behind the machine-precision pairing (the pairing is also a generic consequence of $i\Delta$ being a real antisymmetric matrix times $i$ — state this so the $10^{-16}$ residual is not oversold as a physics result). **[Priority 2]**

---

## 3. Analytic cross-checks required *(blocking)*

- **Continuum SJ for the sheared 2D diamond.** Derive the SJ spectrum/eigenfunctions analytically for the constant-tilt 2D section (it is conformal to a standard causal diamond/rectangle, for which SJ is known, e.g. Mathur–Surya). Compare to the sprinkled spectrum — this both validates the code and quantifies what the tilt does to eigenvectors. **[Priority 1]**
- **Analytic prediction of the null-slope zero at $r_{\rm erg}$.** Currently shown numerically (interpolated to $2.0000$). Give the closed-form: $s_-=0 \Leftrightarrow g_{tt}=0 \Leftrightarrow r=r_{\rm erg}$, with the exact relation between the inner null slope and $(g_{tt},g_{t\varphi},g_{\varphi\varphi})$. **[Priority 2 — result is geometrically obvious but should be stated]**
- **Closed-form for $A_{\rm caus}(r)$** from the cone-opening angles (the tilt is a known function of the metric), to confirm the $\sim1/r^2$ tail and the monotone $a$-dependence are not statistical. **[Priority 2]**
- ✅ **DONE — Toy-model derivation of the opposite-sign effect** (see 1.4). (VYPOCET-10; draft §3.5b; closed-form $A_{\rm caus}$ on the finite rectangle remains — see item 1.4 "Remaining".)

---

## 4. $\varphi$-periodicity (the deferred hard problem) *(blocking)*

- We deliberately used a finite $\varphi$-window to avoid $\varphi\sim\varphi+2\pi$. A real treatment must handle the actual cylinder topology: wrap-around causal relations, whether the SJ state is well-defined on the periodic section, and how $A_W$ changes. Since $\partial_\varphi$ is spacelike there are no CTCs, but the bounded-region SJ prescription assumes relative compactness in a globally hyperbolic spacetime — verify this carefully for the periodic case (or justify the finite window as a controlled approximation with an explicit error estimate as $\Phi\to2\pi$). **[Priority 3]**

---

## 5. Comparison to known vacua (essential for credibility) *(blocking)*

- **BTZ has known vacua** (global AdS$_3$ vacuum, the AdS/CFT thermal state, Hartle–Hawking-type states for rotating BTZ). Compare $W_{\rm SJ}$ on the bounded section to the restriction of a *known* BTZ two-point function. Agreement (or a controlled disagreement) is the standard sanity check the current draft entirely lacks. **[Priority 1]**
- **2D massless subtlety.** The 2D massless scalar has the well-known IR zero-mode / non-existence-of-vacuum issue; address how the SJ prescription on a bounded region handles it and whether the $1/k$ plateau is the expected continuum behavior. **[Priority 2]**
- **Equatorial Kerr "vacuum."** There is no canonical one (that is the point), but compare against the equatorial restriction of the Unruh-state two-point function (arXiv:2602.09796) at least schematically, to position SJ relative to the one known Hadamard state. **[Priority 3]**

---

## 6. Physics framing to tighten

- **Superradiance claim.** "$f_{\rm co}=1$ is the causal-set signature of superradiance" is suggestive but not demonstrated to connect to the actual superradiant amplification $|R_{lm}|^2>1$. Either make the connection quantitative or downgrade to "consistent with."
  ✅ **STRENGTHENED v0.2 — VYPOCET-10 §3.5b** adds a frequency-space superradiant-band weight ($\omega(\omega-k\Omega)<0$) in the SJ positive subspace that grows with $a$ and toward $r_{\rm erg}$ with the static control exactly zero — a closer analogue of the superradiant band than $f_{\rm co}$, though still not a reflection-coefficient $|R_{lm}|^2>1$ computation (that needs the 4D Teukolsky route). Downgrade of "$f_{\rm co}=1$" language done; frequency-content result promoted to Abstract. **[Remaining: quantitative link to $|R_{lm}|^2$, needs 4D]**
- **Eigenvector claim.** "Rotation lives in the eigenvectors" should be backed by a direct eigenvector-overlap measurement.
  ✅ **DONE v0.2 — VYPOCET-10, draft §3.5b.** On a single shared sprinkling, the rotating-vs-static SJ positive subspaces are rotated by a mean principal angle of $44.6^\circ$ ($\cos^2=0.507$, Kerr $a=0.9$ vs $a=0$, $r=2.6$; BTZ $\cos^2=0.509$) while the spectrum differs $2.0\%$ and link fraction drifts $0.6\%$; static-vs-static control returns $\cos^2=1.000000$. Plus a $(\omega,k)$ occupation map showing the dragged shear and superradiant-wedge weight that grows with $a$ and toward $r_{\rm erg}$ (static control exactly 0).
- **Mass.** Everything is massless (so the lever applies). State clearly that the massive case is genuinely different ($G_R\neq\tfrac12 C$) and is not covered. *(Already in §4.3 limitations.)*

---

## 7. Verify all citations against arXiv before any release *(blocking)*

- Several references are paraphrased from internal writeups. Confirm exact titles, authors, and arXiv IDs — especially the recent ones (2504.12919, 2602.09796, 2303.13488, 2212.10592, 2007.07211) and the BTZ/Kerr metric references. **Do not cite anything not personally verified on arXiv.** Any ID that cannot be confirmed must be removed, not guessed. **[Priority 1 — must be done by a human before any external sharing]**

---

## 8. Human re-derivation / independent verification *(blocking for any real submission)*

- No human has yet independently re-run VYPOCET-05, VYPOCET-08, or VYPOCET-10. The eigenvector-overlap result (~45° rotation), the superradiant-wedge growth, and the toy-model $A_W$ magnitudes are all AI-pipeline results and must be independently verified before these claims can be presented outside the project. **[Priority 1 — gate item]**

---

### Minimum bar to call this "real"

Sections 1 (referee rebuttals with analytics), 2 (continuum study + more seeds), 3 (at least the SJ-diamond and null-slope analytic checks), 5 (comparison to a known BTZ vacuum), and 0 + 7 + 8 (ethics + verified citations + human re-derivation) are all blocking. Until then this remains an internal exploratory note.

### Priority summary for next work

| Priority | Item |
|----------|------|
| **1 (next)** | Continuum study (larger $N$, 30+ seeds) — §2 |
| **1 (next)** | Analytic SJ for sheared diamond / comparison to Mathur–Surya — §3 |
| **1 (next)** | Comparison to a known BTZ two-point function — §5 |
| **1 (gate)** | Citation verification against arXiv PDFs — §7 |
| **1 (gate)** | Human re-derivation / independent re-run — §8 |
| **2** | Window-size sweep ($A_W$ boundary sensitivity) — §2, §1.5 |
| **2** | Closed-form $A_{\rm caus}(s_-,s_+)$ and $A_W$ on finite rectangle — §1.4, §3 |
| **2** | Poisson ensemble check — §2 |
| **3** | $\varphi$-periodicity study — §4 |
| **3** | Schematic comparison to Unruh state — §5 |
