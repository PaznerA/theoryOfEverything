# TODO — what must be strengthened before draft-04 could become a real note

**Status: internal exploratory draft (v0.1, AI-assisted). NOT submission-ready. This list is the gate.**

The physics core is: three finite-$N$ proxies for a type III$_1\to$II transition driven by Sorkin–Yazdi truncation, fired 2/3 in a clean 2D diamond and 3/3 in a clean 4D slab, plus a geometry caveat (diamond corners spoil it) and a conjectural identification of the discreteness scale with the CLPW crossed-product modular cutoff. The whole vulnerability is in **(a) "proxies are not types"**, **(b) "$N^{3/4}$ is a prescription you imposed"**, and **(c) the Gaussian-state limitation** — plus the usual novelty-framing and convention airtightness. This list targets exactly those attacks.

---

## 0. Authorship / AI-assisted ethics note (must appear in any real version)

- The calculations (`calc.py` in each of the four `core-data/calculations/*` dirs), the proxy definitions, the $N$-scaling fits, and the citation transcriptions were produced by an **AI-assisted exploratory pipeline**. **No human has** re-run the code, re-derived the $\varepsilon=\ln[\mu/(\mu-1)]$ modular-energy formula, re-checked the $G_R$ conventions against the source PDFs, or confirmed the $\pm$-pairing / area-law-rank claims independently.
- Any real submission requires: (a) a named human author who has re-run all four scans and reproduced the headline numbers (2D $80\times$ / $N^{1.04}\to N^{0.17}$; 4D $36\times$ / $N^{1.34}\to N^{0.55}$; pile-up $\to0$; fixed-fraction $N^{0.83}$ failure); (b) an explicit AI-assistance statement per venue policy and project publishing conventions; (c) public release of `calc.py` and `results.json` for all four calculations.
- This is the kind of result that is **trivial to over-sell** ("we found the type-III$\to$II transition of quantum gravity on a causal set"). Keep the claim narrow: *finite-$N$ proxies, consistent trends, two of three legs of the triangle, no analytic derivation, Gaussian state only.* Nothing about a proven type, a derived crossed product, or the LQG area gap is established.

---

## 1. THE central referee attack: "finite-$N$ proxies are not von Neumann types"

This is the single most likely rejection, and it is **correct in principle**: on a finite causal set every algebra is type I$_n$; type is an asymptotic invariant that no finite matrix carries. A hostile referee will say "you measured three finite-dimensional numbers and called their trends a type transition."

**The defense must concede the principle and then make the trend argument precise — head-on:**

1. **Concede fully.** State in the response (and §1.2/§6 already do) that we do **not** measure a type and cannot at finite $N$. The claim is strictly about *$N$-scaling trends of surrogates predicted to differ between III$_1$-like and II-like situations.*
2. **The $N$-scaling-trends argument is the substance.** A single number proves nothing; the content is that **three independent proxies, each with a sharp pre-registered prediction, move in the predicted direction together, and the modular-spectrum proxy does so with a definite sign of exponent** ($N^{1.14}$/$N^{1.27}$ pile-up $\to$ exactly 0). The Connes signature III$_1\iff S(\mathcal M)=[0,\infty)$ is *defined* by the flat-dense-down-to-$\varepsilon=0$ density; our finite-$N$ surrogate measures precisely the growth of that $\varepsilon\to0$ pile-up with $N$ and its annihilation by truncation. This is the closest finite-$N$ shadow of the actual invariant that exists.
3. **The honest limit on the trend.** A pile-up exponent measured over $N\in[400,1800]$ (2D) / $[800,3500]$ (4D) is an extrapolation. *To strengthen:* (a) push $N$ higher (4D to $N\gtrsim 6000$, eigh is the bottleneck) and confirm the pile-up exponent and the IR-edge location $\varepsilon\approx2.7$ are $N$-stable; (b) bootstrap the exponents' confidence intervals over seeds rather than quoting the single-fit $a\_err$ (the 2D trace $a\_err=0.78$ is the *seed-spread placeholder*, NOT a clean fit error — fix this: report the fit's own standard error and an across-seed CI separately).
4. **Do not let the modular-spectrum proxy carry the type claim alone.** It is the strongest, but it is one definition. State that the *conjunction* with the trace proxy (independent: trace functional vs. spectral density) is what raises confidence; a referee who kills one proxy must still face the other.

**Bottom line for §1:** concede the proxies are not types; defend the *joint, signed, $N$-scaled trend* of independent surrogates, and the fact that the modular-spectrum surrogate is a direct finite-$N$ image of the defining Connes invariant. If a referee finds a finite-$N$ artifact that fakes a $\varepsilon\to0$ pile-up collapse (e.g. pure rank reduction), address it: show the fixed-fraction control *also* reduces rank but does **not** collapse the pile-up cleanly to the area law — the effect is truncation-scheme-selective, not a generic rank artifact.

---

## 2. The second referee attack: "$N^{3/4}$ is a prescription, not a spectral feature — you imposed the answer"

Proxy 3c states honestly that the slab spectrum has **no intrinsic knee** at $N^{3/4}$ (auto-knee finds rank $\sim N^{1.06}$). A referee will say: "you keep the top $2N^{3/4}$ modes by hand, get $S\sim\sqrt N$ by construction, and call it type II. Circular."

**The counter is the selectivity result (3a $\wedge$ 3b) — this is the paper's strongest single argument and must be foregrounded:**

- **The answer is NOT imposed generically.** Two magnitude cutoffs were run on the *same* region. The area-law rank $n_{\max}\sim N^{3/4}$ gives $S\sim N^{0.55}\approx\sqrt N$ (area law). The fixed-fraction cutoff $\kappa=0.05\lambda_{\max}$, which keeps $\sim N^{0.90}$ modes, gives $S\sim N^{0.83}$ — **not** the area law. If "keeping fewer modes by hand" were the whole story, *both* would regularize. Only the specific $N^{(d-1)/d}$ rank does. **The type signature is selective in the truncation prescription.**
- **3c is a feature, not a bug.** In the crossed-product construction the modular/observer cutoff is an **external** structure adjoined to a traceless III$_1$ algebra — it is *not* supposed to be an intrinsic spectral feature of the region. That the slab has no self-generated knee means the clean III$_1$ kinematics is present and type II appears only on *adjoining* the $N^{3/4}$ cutoff. This is the correct crossed-product behavior, and the response should say so explicitly, with the CLPW analogy spelled out.
- **To strengthen:** (a) run a *third* truncation scheme — e.g. $n_{\max}\sim N^{0.6}$ and $n_{\max}\sim N^{0.85}$ — and show $S$-exponent is monotone in the rank exponent and crosses the area-law target $0.5$ specifically near the $3/4$ prescription, not at the fixed-fraction $\sim0.9$; that turns "the $3/4$ works" into "$3/4$ is *selected* by the area-law requirement." (b) Verify the $\alpha=2$ prefactor does not drive the $0.55$ vs. $0.50$ gap (vary $\alpha\in[1,4]$; the *exponent* should be $\alpha$-independent).
- **Honest concession to make:** $a=0.55$ is not exactly $0.50$. State the gap, attribute it to finite-$N$ + prefactor, and show via (a)/(b) that the exponent converges toward $0.5$ as $N$ grows / is $\alpha$-independent. Do not quote $0.55\approx0.5$ without this.

---

## 3. The third referee attack: "the Gaussian-state limitation makes the modular identification cheap"

The modular spectrum $\varepsilon=\ln[\mu/(\mu-1)]$ uses the quasifree/Gaussian structure of the SJ state. A referee will say: "for a Gaussian state the modular Hamiltonian is *always* a quadratic form with this spectrum; you have shown nothing about the algebra type, only re-expressed the symplectic eigenvalues."

**The defense:**

- **The Gaussian structure is the correct and only available object here.** The SJ state *is* quasifree (it is the positive part of $i\Delta$); the free-field crossed-product results of CLPW/CPW are *also* established at the Gaussian/free level. So the comparison is like-for-like: we test the free-SJ state against the free-field type prediction. Jones–Yazdi (2602.16782) independently connect SSEE to exactly this covariance-matrix modular formalism — cite as direct support, and **a human must read 2602.16782 and confirm it supports (not undermines) the $\varepsilon=\ln[\mu/(\mu-1)]$ identification** (this draft asserts it from the provenance note, unverified).
- **What the Gaussian limit does NOT let us claim:** anything about non-Gaussian sectors, interacting fields, or the full algebra beyond the free part. State this in §6 (done) and do not let the interpretation drift to "the local algebra is type III$_1$" — it is "the free SJ state's modular density is III$_1$-like".
- **The non-triviality is in the truncation, not the parametrization.** Re-expressing $\mu$ as $\varepsilon$ is trivial; what is *not* trivial is that the *density* of $\varepsilon$ is flat-dense-to-zero before truncation and integrable-with-edge after. A referee conflating the two should be pointed at the density plots: the parametrization is fixed, the density's qualitative change is the result.

---

## 4. Novelty framing (three-way synthesis vs. partially-known prior art)

The novelty check (`verification/novelty/entropy-cluster.md`) returns **partially-known**: pairwise edges published, three-way identification not. Position this *before* the results (§3 does). Referee risk: "this is just CLPW applied to a known causal-set truncation."

- **Concede the pairwise edges generously.** CLPW 2206.10780 (III$_1\to$II via observer); CPW 2209.10454 (II$_\infty$); Sorkin–Yazdi 1611.10281 (SSEE truncation); Surya et al. 2008.07697 (area-law rank, slab/Rindler). Each is named in §3 with "no causal sets / no crossed products / no LQG" tags.
- **Defend only:** (i) the three-way synthesis *as a stated hypothesis*, and (ii) its *first numerical proxy test on a causal set*. Do not claim the crossed product, the SSEE formula, or the rank law.
- **The weakest novelty point is that we test only 2 of 3 legs.** A referee can say "you call it a triangle and test one edge." The response: we are explicit (§1.3, §5, §6) that the LQG leg is untested and the third edge is the most speculative. Downgrade any language that implies the triangle is established.
- **To verify:** re-run novelty against (a) Jones–Yazdi 2602.16782 and any 2025–2026 follow-ups — if *they* already state SSEE-truncation $=$ crossed-product cutoff, this note becomes a confirmation, not a contribution; (b) the "subregion algebras in QG" line (2601.07915) and crossed-product-and-generalized-entropy (2306.07323) for overlap with the type-II-on-causal-set framing.

---

## 5. Convention and reproduction airtightness

Every numerical claim is checkable; a referee will check.

- **$G_R$ conventions:** 2D $G_R=\tfrac12 C$ (1611.10281 eq. 9); 4D $G_R=(\sqrt\rho/2\pi\sqrt6)L$, *link* matrix (0909.0944 eq. 17, $m=0$; 1701.07212). A human must confirm the link-matrix vs. causal-matrix distinction is applied correctly in 4D and that BD-vs-link does not change the *scaling* (companion VYPOCET-09 claims it does not — re-verify).
- **Double truncation $\kappa=\sqrt N/(4\pi)$ (2D local)** from 1712.04227 — confirm the $4\pi$ and the *double* (global + restricted) application; the single global rank truncation gives negative $S$ (stated) — confirm the sign.
- **Area-law rank $n_{\max}=\alpha N^{(d-1)/d}$, $\alpha=2$, $d=4\to N^{3/4}$** from 2008.07697 — confirm $\alpha$ and the exponent; confirm the continuum direction (raise $\rho$ at fixed region, NOT enlarge box at fixed $\rho$) matches the de Sitter-horizon procedure in 2008.07697. **This direction choice is load-bearing** (it is what makes $N^{3/4}$ meaningful); a human must confirm 2008.07697 actually does it this way.
- **Modular formula $\varepsilon=\ln[(\nu+\tfrac12)/(\nu-\tfrac12)]$, $\nu=\mu-\tfrac12$** from 0905.2562 — confirm the single-mode bosonic derivation and that the $(\mu,1-\mu)$ pair maps to $\nu=\mu-\tfrac12$ with $\mu>1$ branch.
- **$\pm$-pairing residual $7.1\times10^{-14}$ (4D) / $10^{-16}$ (2D)** — re-run and confirm $i\Delta$ is exactly antisymmetric (validity of the whole construction).
- **Every arXiv ID** (1611.10281, 1712.04227, 2008.07697, 0909.0944, 1701.07212, 0905.2562, 2501.09669, 2602.16782, 2206.10780, 2209.10454, 2112.12828, 2212.10592, 1906.07952, 2412.07832, Connes 1973) must be confirmed against arXiv by a human — authors/year/journal — before any release. **2501.09669 and 2602.16782 are recent (2025–2026) and must be checked to exist and to say what is claimed.**

---

## 6. Statistics / fit robustness

- **[RESOLVED 2026-06-06] The 2D `a_err = 0.775853...` seed-spread placeholder is purged.** It was `sqrt((A^T A)^{-1}[0,0])` under assumed unit variance — a function of the $\log N$ abscissa only, hence identical across all five `sig=None`/degenerate fits, and meaningless as an uncertainty. `core-data/calculations/sj-vn-type/calc_uncertainty.py` (minimal re-run, IDENTICAL seeds `7e6+1000N+s`, Ns, 8 seeds, frac=0.5, eps0=0.5; central values reproduced to all digits) now computes for each affected exponent (i) the residual-based OLS regression SE of the log-log slope and (ii) a 68% across-seed bootstrap CI (2000 resamples). Results written to `results.json` as `*_se_regression` / `*_ci68_bootstrap` (legacy `a_err`/`err` kept but annotated as superseded) and `uncertainty.json`. New values: $S_{\rm full}$ $a=1.043$ SE $0.013$ CI $[1.024,1.063]$; $S_{\rm trunc}$ $a=0.172$ SE $0.012$ CI $[0.155,0.190]$; pile-up$_{\rm trunc}$ identically 0 (SE $0$, no power law to fit); $\mathrm{CV}(S_{\rm trunc})$ $a=-0.714$ SE $0.082$ CI $[-0.91,-0.51]$; $\mathrm{CV}(S_{\rm full})$ $a=-0.754$ SE $0.114$ CI $[-0.92,-0.40]$. The proxy-3 CIs are wide (non-discriminating verdict unchanged). draft.md §2D Proxy 1/3 tables updated (and a `-0.50`$\to$`-0.75` display typo for $\mathrm{CV}(S_{\rm full})$ fixed).
- **Proxy 3 (2D) is honestly non-discriminating** ($N^{-0.71\pm0.78}$ consistent with zero). Keep it labeled as such; do not let a summary read "3/3 in 2D". The 2D verdict is **2/3**, the 4D verdict is **3/3** — these must never be conflated.
- **More seeds for 2D proxy 3:** $\sim30$–$50$ seeds (cheap) to decide whether truncated SSEE is *more* self-averaging than full; only then could 2D become 3/3.
- **4D used 5 seeds, 2D used 8.** State both; confirm $\ge4$ (project minimum) is met (it is). For the IR-edge location $\varepsilon\approx2.7$ and pile-up exponent $N^{1.27}$, report across-seed spread.
- **$R^2$ values** (0.97–0.98 for the 4D trace fits) are good but not decisive given 6 $N$-points; report residuals and check for curvature (the 2D intrinsic-knee showed tolerance-dependent curvature in the companion — confirm the trace/pile-up fits are clean).

---

## 7. Claims to soften or sharpen

- **Soften:** "the discreteness scale acts as the observer/modular cutoff" $\to$ "is *consistent with* / a *candidate for*". Already conjecture-labeled in §5; keep it there, never in the abstract as fact.
- **Soften:** "first numerical realization of Connes' modular invariant on a causal set" $\to$ "first numerical *surrogate* for the modular-density signature of $S(\mathcal M)$". The actual invariant is not computed at finite $N$.
- **Sharpen:** the selectivity result (area-law rank works, fixed-fraction fails) — this is the strongest argument and should be unmissable in both abstract and §4.2; ensure it is not buried under the modular-spectrum result.
- **Sharpen:** the geometry caveat. State clearly that the clean type-II signature is **not** generic to 4D — it is specific to the flat, Hadamard, Rindler-like region — so the result is "4D *with the right geometry*", not "4D".
- **Do not claim** II$_1$ vs. II$_\infty$, III$_\lambda$ resolution, the LQG leg, or any interacting/non-Gaussian statement.

---

## 7b. De Sitter section (§4.3) — round-10/11 provenance, separate verification checklist

The §4.3 de Sitter extension was added in round 10/11 (decision H5g-6: a section in *this* draft, **not** a standalone draft-05, until full 4D saturation is demonstrated at larger $N$). Its statuses are quoted verbatim from `findings.json` — F-023 `supported` (2D), F-025 `partial` (4D) — and **must not be upgraded** in any revision. Re-verify all of the following independently:

- [ ] **Re-derive the saturating fits from `results.json`.** From `core-data/calculations/sj-desitter-type/results.json`: 2D content-saturation — $N_{\rm total}$ cap $=480.11$, $R^2=0.99994$ ($\approx1.0000$); $S_{\rm full}$ saturating-fit $R^2=0.990$, late slope $-1.67$; flat control $N_{\rm total}$ $768\to3360$ (slope $480$), $S_{\rm full}$ grows (slope $+12.2$, late $+4.82$); late-half net change dS $-13.1$ vs. flat $+21.7$ (gap $34.8$). Fixed-region battery: Proxy 1 $S_{\rm full}\,a=1.105\pm0.017$ ($R^2=0.999$) $\to S_{\rm trunc}\,a=0.116\pm0.028$; Proxy 2 pile-up $a=1.248\to$ exactly 0; Proxy 3 (CV) **non-significant at 5 seeds** (verdict 2/3, matching VYPOCET-12). Part-3 tracial probe **honest null** (IR-fraction slope dS $-0.008$, flat $-0.004$; documented resolution scaling $\rho\sim10^{3}$–$10^{4}$).
- [ ] **Re-derive the 4D fits from `core-data/calculations/sj-desitter-4d/results.json`.** Truncated $R^*_{\rm box}$-exponent dS $a=0.27$ vs. flat $a=0.52$ (full-slope ratio $2.96\approx3\times$ shallower); fixed-region truncated area-law $S_{\rm trunc}\sim N^{0.717\pm0.029}$, CI68 $[0.697,0.739]$, $R^2=0.993$ — **above** the §4.2 slab target $0.5$ (dS radial geometry steepening, **not** a pipeline error); matched-control reproduction $a=0.58$ vs. committed $0.547$ (validates SSEE composition); $S_{\rm full}\sim N^{1.017}$ (volume/III); $N_{\rm total}$ cap $480$, $R^2=1.000$ (content discriminator lifts to 4D); pile-up full $6\to32$ vs. trunc $=0$. Confirm full saturation is **NOT** reached at $N\le2500$ (dense-`eigh` bound) — F-025 status is `partial`, not `supported`.
- [ ] **Verify the conformal-weight caveat wording.** Confirm the draft states plainly that the **4D massless scalar is not conformally invariant** (unlike the 2D massless scalar), so the construction preserves the flat causal structure in $(t,r^*,x_1,x_2)$ and the dS proper **measure** ($\mathrm{sech}^2$, bounded point budget $=$ II$_1$ signal) but **not** the exact curved 4D Wightman function / propagator. The 2D conformal trick (1306.3231) is exact; the 4D lift is a controlled approximation. The §4.3 caveat paragraph must not be softened away.
- [ ] **Check F-023/F-025 statuses match `findings.json`.** F-023 must read `supported` (2D content discriminator; 2/3 proxy battery; honest 2D truncated-entropy null; Part-3 tracial honest null). F-025 must read `partial` (real 4D-specific separation signal, but no full saturation at $N\le2500$; exponent $0.717$ above target). Confirm §4.3 and the abstract do **not** state II$_1$ as measured, do **not** claim clean 4D saturation, and do **not** claim the $A/4$ cap (H5g-2 cited as open only).
- [ ] **Re-run the two dS `calc.py`** and reproduce the headline dS numbers: `core-data/calculations/sj-desitter-type/calc.py` (2D, $\pm$-pairing $2.3\times10^{-13}$) and `core-data/calculations/sj-desitter-4d/calc.py` (4D, $\pm$-pairing $<6.84\times10^{-15}$).
- [ ] **Verify the two new arXiv IDs cited by §4.3:** 1306.3231 (de Sitter SJ vacuum / conformal trick) and 1205.3855 (Anninos, dS$_2$ static patch, tortoise + $\mathrm{sech}^2$ conventions) — confirm existence, authors/year, and that they say what is claimed. (2206.10780 CLPW II$_1$ and 2008.07697 area-law rank are already in the §5/§8 arXiv list.)
- [ ] **H5g-2 ($A/4$ cap) is cited as OPEN, not tested.** Confirm the §4.3 outlook flags the dS-entropy-cap-vs-horizon-area question as future work and does not present any quantitative $A/4$ match.

## 8. Human verification gates (must all pass before this leaves the building)

1. [ ] A named human re-runs all four `calc.py` and reproduces: 2D trace $80\times$ / $N^{1.04}\to N^{0.17}$; 2D pile-up $N^{1.14}\to0$; 4D trace $36\times$ / $N^{1.34}\to N^{0.55}$; 4D pile-up $N^{1.27}\to0$, IR edge $\varepsilon\approx2.7$; fixed-fraction $N^{0.83}$ failure.
2. [x] All uncertainties re-derived (regression SE + bootstrap CI); the placeholder `a_err=0.776` purged. **(2026-06-06: `calc_uncertainty.py` adds `*_se_regression`+`*_ci68_bootstrap` to `results.json`; draft updated. Note: this covers the 2D `sj-vn-type` calc; the analogous fit-error audit for the 4D and the two companion calcs is still pending.)**
3. [ ] All 15 arXiv IDs verified against arXiv (authors/year/journal); 2501.09669 and 2602.16782 confirmed to exist and support the modular formula and SSEE-modular link.
4. [ ] Novelty re-checked against 2602.16782, 2601.07915, 2306.07323 to confirm the three-way synthesis is still unpublished.
5. [ ] The selectivity control extended (third rank scheme $N^{0.6}$/$N^{0.85}$; $\alpha$-independence of the exponent).
6. [ ] $N$ pushed higher in 4D ($\gtrsim6000$) to confirm pile-up exponent and IR-edge stability.
7. [ ] AI-assistance statement added; `calc.py`/`results.json` release prepared.
8. [ ] Every "type" claim downgraded to a proxy/surrogate claim per §7; the LQG-leg "untested" statement present in abstract, §1.3, §5, §6.

> **Until all eight gates pass, this is an internal note and nothing in it should be cited, quoted, or treated as a result.**
