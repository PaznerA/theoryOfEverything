# TODO — what must be strengthened before draft-03 could become a real note

**Status: internal exploratory draft (v0.1, AI-assisted). NOT submission-ready. This list is the gate.**

The physics core is an assembled classification table for the UV spectral dimension plus a probe axis and a discriminator reading. Every individual number is from the literature; the engine reproduces them. The entire vulnerability is in *novelty framing* — whether a referee calls this "the Calcagni program repackaged" or "probe-dependence is obvious" — plus the usual convention/provenance airtightness. This list targets exactly those attacks.

---

## 0. Authorship / AI-assisted ethics note (must appear in any real version)

- The engine (`calc.py`), the master table, and the citation transcriptions were produced by an **AI-assisted exploratory pipeline**. No human has re-run the engine, re-derived the $D/\gamma$ and $1+D/z$ limits, or re-checked any convention against the source PDFs.
- Any real submission requires: (a) a named human author who has re-run the engine and confirmed the 12/12 validation checks and the symbolic master; (b) an explicit AI-assistance statement per the venue's policy and the project's publishing conventions; (c) public release of `calc.py` and `results.json` for reproducibility.
- The result is the kind that is easy to over-sell ("we unified the UV dimension of quantum gravity"). Keep the claim narrow: *one engine reproduces published numbers; the assembled table is a classifier; the probe is a third axis*. Nothing about a common fixed point, unification, or a new prediction is established — the table is reproduction, not discovery.

---

## 1. THE central referee attack: "this is Calcagni's program repackaged"

This is the single most likely rejection. The note lives or dies on the answer. Calcagni and collaborators (1311.3340, 1304.2709, 1408.0199, 1708.07445) already (i) compute $d_s$ across approaches, (ii) state it is not universal, (iii) know it is structure/probe-sensitive in causal sets. A hostile referee will say the note adds nothing.

**The defense must make three points, each with documented evidence, and must concede what is genuinely Calcagni's:**

1. **Simultaneous single-engine validation is the concrete deliverable.** Calcagni computes each entry with the method native to that approach (Seeley–DeWitt + saddle point for QFT/Stelle; combinatorial Laplacians for GFT/spin foam; fractional measures for multifractional). The "map of QG" (1708.07445) is a *collation across methods*, not one engine. Our deliverable is **one functional $P(\sigma)=\int d^Dk\,e^{-\sigma F(k)}$, one numerical implementation, one $d_s$ definition, reproducing all published UV/IR numbers at once (12/12)**. This is a falsifiable, reproducible artifact, not a survey. *Evidence to assemble:* quote the methods sections of 1311.3340 and 1708.07445 and show each uses approach-specific machinery; confirm no single $P(\sigma)$ engine reproduces all entries there.
   - **Caveat to be honest about:** our engine reproduces *asymptotics* via effective kernels (§6 limit 1), not first-principles simulations. A referee can fairly say "you reproduced the answers you put in." The rebuttal: the engine still enforces *internal consistency of one definition* across all rows, which is exactly what the scattered literature does not provide, and it exposes the $\gamma=2$ subclass structure that approach-specific methods hide. Do **not** overclaim the engine as derivation; claim it as unification of bookkeeping.

2. **Probe-as-axis is a stated organizing principle, not a noted side-effect.** Eichhorn–Mizera (1311.2530) and Belenchia et al. (1507.00330) document the two causal-set probes *separately*; Calcagni–Oriti–Thürigen (1311.3340) note structure-dependence. What is *not* in the literature as a stated principle is **"the classifier is $(z,D,\text{probe})$, on the same footing as $z$ and $D$,"** justified by the same-theory/opposite-trend contradiction. *Evidence to assemble:* find the closest sentence in 1311.3340 to "probe-dependence" and show it stops short of elevating the probe to a classification axis. If any paper *does* state $(z,D,\text{probe})$ as the classifier, downgrade claim 2 to "we make explicit what was implicit."

3. **The discriminator framing inverts the standard reading.** The literature presents $d_s\to 2$ as evidence *for* a common UV behaviour (Carlip's "almost universal"). We present it as a $\gamma=2$ subclass artifact and lead with the *violations* (GR $4$, Hořava $z=2$ at $5/2$, random walk $>D$). Carlip's "almost" is the closest prior statement, but it is framed as a caveat to universality, not as a classification principle. *This is the part most likely to survive the "repackaged" attack — lead with it if claims 1 and 2 are judged too close to Calcagni.*

**Bottom line for §1:** concede generously that the ingredients are Calcagni's; defend only the *assembly* (one engine), the *axis* (probe promoted), and the *inversion* (discriminator). If a referee finds all three already stated together anywhere — re-run novelty against Calcagni's books/reviews and the Mielczarek–Trześniewski / "map" follow-ups — the note becomes a clarification, not a contribution.

---

## 2. The second referee attack: "probe-dependence is obvious / trivial"

A referee may say: *"Of course the spectral dimension depends on which operator you diffuse with; that is definitional. A random walk and a d'Alembertian are different operators, so different $d_s$ is no surprise."*

**The counter is the published contradiction we found and fixed in our own database — this is the concrete, non-obvious evidence:**

- It was *not* obvious to the field as actually practiced. Our own knowledge graph (built from the literature) carried **two contradictory edges**: one said $d_s$ in causal sets *drops* (to $\sim 2$), the other said it *rises*. Both cited correct papers. Both were partially right. They were inconsistent *because the probe was not named*. The contradiction is documented in `verification/ds-contradiction.md` (edges: causal-sets$\to$spectral-dimension, and noncommutative-geometry$\to$causal-sets).
- The point: if probe-dependence were trivially obvious, this contradiction would never have entered a literature-derived database, and the two source papers (1311.2530 drop-opposite / 1507.00330 universal-drop) would routinely be cited together with the probe caveat. They are not. The "$d_s$ of causal sets" is quoted in surveys with a single sign of trend, which is exactly the error our contradiction encodes.
- **Defense framing:** "obvious in principle, routinely conflated in practice." The note's value is making the axis *explicit and load-bearing* so the conflation cannot recur. The same-theory/opposite-trend pair (CST d'Alembertian $\to 2$ vs CST random walk $>D$) is the minimal sharp example that forces the issue — it is not "two different theories," it is one theory, which is what makes it non-trivial.
- **Strengthen by:** (a) quoting at least one survey or talk that states "causal sets show dimensional reduction to 2" *without* the probe caveat (to prove the conflation is real, not strawman); (b) checking whether Eichhorn–Mizera themselves flag the tension with Belenchia et al. — if they do, cite it as confirmation; if they don't, that *is* the gap.

---

## 3. Convention and reproduction airtightness

Every "REPRODUCE" in the table is a claim against a published value; a referee will check each.

- **Hořava (0902.3657):** confirm $d_s=1+D/z$ and the specific $z=2\Rightarrow 5/2$, $z=3\Rightarrow 2$ for $D=4$ ($D_{\rm space}=3$). Note Hořava's headline case is $z=3,D=3$ (i.e. $3{+}1$ spacetime) $\Rightarrow d_s=2$; our $D=4$ convention must be stated unambiguously (is $D$ the spatial dimension or spacetime dimension in each row?). **This is a real ambiguity** — the table mixes $D$=spacetime (=4) with $D_{\rm space}$=3 in the Hořava formula. A human must verify the per-row $D$ convention is internally consistent and matches each source.
- **Asymptotic safety:** pin $\eta_*=2-d=-2$ (so propagator $\sim 1/p^4$, $d_s=d/2=2$) to Lauscher–Reuter hep-th/0508202 and Reuter–Saueressig 1110.5224. Confirm the sign and that $\eta_*=-2$ is the NGFP value used, not an ansatz.
- **Stelle (1408.0199):** confirm $d_s^{\rm UV}=2$ for any $D$ from the $k^4$ propagator. Confirm the IR returns $d_s=D=4$ from the inserted crossover (this is *our* crossover, not Stelle's — flag as model-inserted, §6 limit 2).
- **Causal-set d'Alembertian (1507.00330):** confirm "universal $d_s\to 2$ in all $D$" and the $(k^2)^{D/2}$ high-momentum behaviour. Confirm our $\gamma=D/2$ assignment reproduces this for $D=4$.
- **Causal-set random walk (1311.2530):** confirm $d_s$ *increases above* $D$. **Critical honesty item:** the numeric $8$ is *illustrative* ($=D+4$), not from the paper — Eichhorn–Mizera give no universal asymptotic constant. The table and §6 already flag this; make sure the "REPRODUCE (qualitative)" label is never read as a quantitative match. A referee who reads "$8$" as a claimed value will reject; the label and §6 must be unmissable.
- **Multifractional (1304.2709):** we use one class ($\gamma_{\rm UV}=D/2$). State that Calcagni gives several classes with different UV values; ours is a comparison value only.
- **Every arXiv ID** (0902.3657, 1105.6098, 1408.0199, 1311.3340, 1304.2709, 1708.07445, 1705.05417, 1311.2530, 1507.00330, hep-th/0508202, 1110.5224) must be confirmed against arXiv by a human before any release, with authors/year/journal checked.

---

## 4. Scheme / definition robustness of $d_s$ itself

- **Which $d_s$?** There are several inequivalent spectral dimensions in the literature (heat-kernel/return-probability, walk dimension, causal spectral dimension of Eichhorn–Mizera). Our engine uses the return-probability $d_s$ for the isotropic rows but the random-walk row refers to a *different* definition (causal spectral dimension). State explicitly that the probe axis partly *is* a change of $d_s$ definition, not only a change of operator — and argue that this is precisely the point (the "probe" subsumes operator + measurement protocol). A referee may say "you are comparing different quantities." The defense: yes, and that incommensurability is the content of the third axis. Make this explicit rather than letting it look like a category error.
- **Euclidean vs Lorentzian.** The engine is Euclidean; causal sets and the random walk are Lorentzian. §6 limit 1 flags this. Confirm that the effective-kernel reconstruction does not smuggle in a sign or analytic-continuation error that would change the *trend* (rise vs fall), since the trend is the whole claim for the CST rows.
- **Crossover model-dependence.** Re-state (already in §6) that only UV/IR *limits* are claimed; the transition shape is not physical. Ensure no figure caption or sentence implies the crossover region is a prediction.

---

## 5. Claims to soften or sharpen

- **"Classifier, not a constant."** Defensible and is the thesis. Keep it as a framing claim, not a theorem. Do not let it drift into "we predict $d_s$ for new theories" — the engine reproduces, it does not predict beyond $D/\gamma$ and $1+D/z$, both of which are known.
- **"$d_s\to 2$ is a subclass artifact."** Strong and correct *given the table*. Make sure the table's coverage is broad enough to support it — a referee may say the sample is cherry-picked to make $\gamma=2$ look special. Counter: GR and Hořava $z=2$ are not cherry-picked; they are the most standard cases and they violate $\to 2$.
- **"Same theory, opposite trend."** The crown jewel. Keep it airtight: it rests on (1311.2530, 1507.00330) being about the *same* causal-set framework. Confirm they are (both Benincasa–Dowker/sprinkling-based causal sets), so the "same theory" claim is literally true and not two different discrete models.
- **Relation to L2-5 (one-fixed-point claim).** This note *weakens* the project's L2-5 hypothesis (spin-foam + CST BD + Reuter AS = one fixed point): probe-dependence forbids asserting universal convergence. Record that this draft is a direct empirical input to revising `connections.json` for L2-5. Do not present the weakening as a result of *this* note's physics beyond the probe argument.

---

## 6. Cross-checks required before release

- **Re-run the engine** and independently confirm 12/12 validation checks and the symbolic $D/\gamma$.
- **Re-derive both limits by hand:** isotropic $d_s^{\rm UV}=D/\gamma$ from $\int d^Dk\,e^{-\sigma k^{2\gamma}}$, and anisotropic $d_s=1+D_{\rm space}/z$ from the factorized $P(\sigma)$.
- **Novelty re-run** specifically against: Calcagni's reviews/books and 1708.07445; Mielczarek–Trześniewski and other "spectral dimension across approaches" surveys; any paper stating $(z,D,\text{probe})$ or "probe as classification axis." If found, downgrade per §1/§2.
- **Confirm the two CST papers are the same underlying framework** (§5) so "same theory" holds.
- **Resolve the $D$-convention ambiguity** (§3, Hořava row) across the whole table.

---

### Minimum bar to call this "real"

Section 0 (ethics + human re-run), §1 (the "Calcagni repackaged" defense with documented method-by-method contrast and an honest concession of the ingredients), §2 (the "probe is obvious" counter via the documented database contradiction), and §3 (per-row REPRODUCE confirmation + the illustrative-$8$ and $D$-convention honesty items) are all blocking. The engine is reproducible and the limits are standard; the remaining work is making the *novelty framing* referee-proof and confirming the assembly/axis/inversion are genuinely unstated in the prior art. Until then this remains an internal exploratory note.
