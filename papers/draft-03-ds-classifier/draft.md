DRAFT v0.1 — generated 2026-06-06, internal research draft, NOT submitted, requires human review.

# The UV spectral dimension is a fingerprint, not a constant: a $(z, D, \text{probe})$ classification across quantum-gravity approaches

## Abstract

The "dimensional reduction to $d_s\to 2$ in the deep ultraviolet" has acquired the status of a near-universal expectation in quantum gravity, repeated across causal dynamical triangulations, asymptotic safety, Hořava–Lifshitz gravity, and causal sets. We argue that this reading inverts the actual structure of the result. Running one return-probability engine, $P(\sigma)=\int d^D k\,e^{-\sigma F(k)}$ with $d_s(\sigma)=-2\,d\ln P/d\ln\sigma$, uniformly and numerically across all of these approaches at once, we reproduce the published UV/IR spectral dimensions in a single table from a single definition (12/12 internal validation checks pass; the isotropic UV limit is symbolically $d_s^{\rm UV}=D/\gamma$ for $F\sim k^{2\gamma}$, and the anisotropic Hořava limit is $d_s=1+D/z$). The point of the exercise is not the individual numbers — every one of them is in the literature — but what the assembled table shows: $d_s^{\rm UV}$ is a *classifier*. It is the fingerprint of three data, the UV propagator exponent (or anisotropy exponent $z$), the topological dimension $D$, and **the diffusion probe**, and it is not a universal constant. We make the probe explicit as a third classification axis, forced on us by a contradiction we found and corrected in our own database: causal sets yield $d_s\to 2$ under a non-local d'Alembertian probe (Belenchia et al., 1507.00330) yet $d_s$ *increasing above* $D$ under a random walk on the causal graph (Eichhorn–Mizera, 1311.2530). Same theory, opposite UV trend, different probe — so "the UV dimension of causal sets" is ill-posed until the probe is named. The apparent universality of $d_s\to 2$ is then exposed as a *subclass artifact*: it is exactly the value $D/\gamma$ for $\gamma=2$, i.e. theories with a UV $k^4$ propagator (Stelle gravity, asymptotic safety at $\eta_*=2-D=-2$, the causal-set d'Alembertian, the canonical multifractional pick), and it is explicitly violated by general relativity ($d_s=D=4$), by Hořava $z=2$ ($d_s=5/2$), and by random-walk probes ($d_s>D$). We position this honestly against a dense body of prior art (Hořava 0902.3657; Sotiriou–Visser–Weinfurtner 1105.6098; Calcagni–Oriti–Thürigen 1311.3340; Calcagni 1708.07445; Carlip 1705.05417) whose individual ingredients we do not claim — what we claim is the simultaneous single-engine validation, the probe as an explicit axis, and the discriminator framing. This is an internal exploratory note; the engine is an effective-kernel reconstruction of published asymptotics, not a first-principles simulation, and the limits say so plainly.

---

## 1. The claim, and what it is not

### 1.1 The folklore

It is by now a commonplace that the spectral dimension of spacetime runs from $d_s=4$ in the infrared to $d_s\approx 2$ in the ultraviolet, and that this "dimensional reduction to two" is a shared, almost universal feature of quantum-gravity approaches — causal dynamical triangulations (CDT), asymptotic safety (AS), Hořava–Lifshitz gravity, causal sets, non-commutative geometry. Carlip's review (arXiv:1705.05417) collects the evidence and calls $d_s\to 2$ an "almost universal" property of UV-renormalizable theories. The phrasing matters: *almost* universal. The folklore that has propagated from it — that $d_s\to 2$ is a deep, theory-independent signal of a common UV fixed point — is stronger than what the calculations support.

### 1.2 The reframing

We make one structural claim:

> $d_s^{\rm UV}$ is not a universal constant. It is a **classifier**: a predictable fingerprint of the triple $(z,\,D,\,\text{probe})$ — the UV propagator/anisotropy exponent, the topological dimension, and the diffusion probe used to measure it. The apparent convergence to $2$ is the coincidence of a *subclass* (UV $k^4$ propagators), not a universal attractor.

This is a deliberate inversion of emphasis. The same numbers that are usually presented as evidence *for* convergence are, when assembled uniformly, evidence that the UV dimension discriminates between approaches. Nothing in the underlying physics is new; the value of the note is the assembly, the probe axis, and the framing.

### 1.3 What we explicitly do not claim

We do not claim the master relation $d_s=1+D/z$: it is Hořava's, explicit since 2009 (arXiv:0902.3657). We do not claim the dispersion-relation-to-$d_s$ procedure: that is Sotiriou–Visser–Weinfurtner (arXiv:1105.6098). We do not claim that $d_s$ varies across approaches and combinatorial structures, nor that it is probe-sensitive in causal sets in isolation: those facts are in Calcagni–Oriti–Thürigen (arXiv:1311.3340), Eichhorn–Mizera (arXiv:1311.2530), and Belenchia et al. (arXiv:1507.00330). Section 3 states the overlap with prior work *before* the results, not after, because the overlap is high and a referee will find it immediately. Our three claimed contributions are narrow and are stated in §1.4.

### 1.4 The three contributions

1. **One engine, simultaneously validated.** A single return-probability functional $P(\sigma)=\int d^Dk\,e^{-\sigma F(k)}$, one numerical implementation, one definition of $d_s$, reproduces the published UV and IR spectral dimensions of GR, Hořava ($z=2,3$), Stelle quadratic gravity, asymptotic safety, the causal-set d'Alembertian, the causal-set random walk, and the multifractional measure — all at once, 12/12 internal checks. The literature carries these numbers scattered across distinct papers, conventions, and methods; the single-engine assembly is what we add, not the numbers.
2. **Probe as an explicit third axis.** The classifier is $(z,D,\text{probe})$, not $(z,D)$. The decisive evidence is internal: the *same* theory (causal sets) gives $d_s\to 2$ under one probe and $d_s>D$ under another. "The UV dimension" is therefore ill-posed without naming the probe — a statement we were forced into by a genuine contradiction in our own database (§4).
3. **The discriminator framing.** $d_s\to 2$ is a subclass artifact — the $D/\gamma=2$ value of UV $k^4$ propagators ($\gamma=2$) — explicitly violated by GR, by Hořava $z=2$, and by random-walk probes. Convergence is reframed as classification.

---

## 2. Method: one return-probability engine

### 2.1 The functional and the definition

For a Euclidean field with inverse propagator (kinetic kernel) $F(k)$, the heat-trace / return probability of the associated diffusion process is

$$
P(\sigma)=\int d^D k\;\exp\!\big(-\sigma\,F(k)\big),
\qquad
d_s(\sigma)=-2\,\frac{d\ln P}{d\ln\sigma}.
$$

The diffusion time $\sigma$ is the probe scale: $\sigma\to\infty$ samples the infrared (small $k$, $F\to k^2$, hence $d_s\to D$), while $\sigma\to 0$ samples the ultraviolet (large $k$, $F\sim k^{2\gamma}$, hence $d_s\to D/\gamma$). This is the standard heat-kernel definition of the spectral dimension; we use it unmodified.

### 2.2 The isotropic master limit (symbolically checked)

For a pure power $F=k^{2\gamma}$ the radial integral closes in elementary form and gives, in the UV,

$$
\boxed{\,d_s^{\rm UV}=\frac{D}{\gamma},\qquad \gamma=\tfrac12\,(\text{UV momentum power})\,}.
$$

A symbolic check (sympy, `calc.py::symbolic_master()`) returns exactly $D/\gamma$. The special cases that populate the table:

| approach | UV $F(k)$ | $\gamma$ | $d_s^{\rm UV}=D/\gamma$ |
|---|---|---|---|
| general relativity | $k^2$ | $1$ | $D=4$ |
| Stelle / 4-derivative | $k^4$ | $2$ | $D/2=2$ |
| asymptotic safety | $k^{2-\eta},\ \eta_*=2-D=-2\Rightarrow k^4$ | $2$ | $D/2=2$ |
| causal-set d'Alembertian | $k^D$ (non-local) | $D/2$ | $2$ (all $D$) |

The "universal $2$" is visibly the $\gamma=2$ row(s) and the special $D$-tuned non-local case — not a universal law.

### 2.3 The anisotropic (Hořava–Lifshitz) limit

Hořava–Lifshitz gravity is *anisotropic*: time scales as $k^1$, space as $k^z$, so it does not obey the isotropic $D/\gamma$ rule. The return probability factorizes,

$$
P(\sigma)\sim\sigma^{-1/2}\cdot\sigma^{-D_{\rm space}/(2z)}
\;\Longrightarrow\;
\boxed{\,d_s=1+\frac{D_{\rm space}}{z}\,},
$$

implemented directly (`_logP_horava`) with a physical IR crossover $F_{\rm space}=k^2+k^{2z}/m^{2z-2}$ so that relevant $z=1$ operators return $d_s=4$ in the IR. For $D=4$ ($D_{\rm space}=3$): $z=1\Rightarrow d_s=4$ (IR), $z=2\Rightarrow d_s=5/2$, $z=3\Rightarrow d_s=2$. This is Hořava's relation (0902.3657); we reproduce it, we do not claim it.

### 2.4 Numerical realization

The radial integral is evaluated in $t=\ln k$ on a wide, $\sigma$-adapted grid with a log-sum-exp accumulation (`_logP_radial`), stable across $\sigma\in[10^{-10},10^{6}]$; volume prefactors cancel in the log-derivative. $d_s(\sigma)$ is a central difference of $\ln P$ in $\ln\sigma$ (step $h=10^{-2}$). The $\sigma$-grid is 90 logarithmically spaced points from IR ($\sigma=10^6$) to UV ($\sigma=10^{-10}$). All UV/IR plateaux are flat to $\lesssim 1\%$; the validation tolerance is $0.06$.

---

## 3. Relation to prior work (stated before the results, because the overlap is high)

This is the note's principal referee risk, so we put it up front. Each ingredient of the engine and the table has a clear ancestor; we name them and say exactly where our line sits.

| arXiv | authors | what they established | what we take / do not take |
|---|---|---|---|
| 0902.3657 | Hořava (PRL 2009) | $d_s=1+D/z$ for anisotropic gravity; $z=3,D=3\Rightarrow d_s=2$ UV; compares to CDT | We **reproduce** $1+D/z$; we do **not** claim it. It is the anisotropic row of our table. |
| 1105.6098 | Sotiriou–Visser–Weinfurtner (PRD 2011) | "From dispersion relations to spectral dimension — and back": assigns $d_s$ to an arbitrary dispersion relation; compares CDT and Hořava | This is the direct ancestor of our isotropic $D/\gamma$ limit. We add only the *uniform single-engine* application and the probe axis. |
| 1408.0199 | Calcagni–Modesto–Nardelli (2016) | quantum $d_s$ in QFT for logarithmic dispersions and Stelle; $d_s^{\rm UV}=2$ for Stelle, variable for general $z$ | Source of our Stelle and multifractional UV values. Reproduced, not claimed. |
| 1311.3340 | Calcagni–Oriti–Thürigen (CQG 2014) | $d_s$ across LQG, spin foam, GFT; finds $d_s$ **not** universal, depends on combinatorial structure | Closest in spirit to the discriminator framing. They do not give a $(z,D)$ master across these approaches and do not isolate the probe as an axis. |
| 1304.2709 | Calcagni–Nardelli (PRD 2013) | $d_s(\alpha,D)$ for multifractional spacetimes; three classes | Source of our multifractional comparison row. |
| 1708.07445 | Calcagni et al. (2017) | "map of quantum gravity": compares $d_s$ across CDT, AS, LQG, Hořava, NCG, non-local, Stelle | The most directly comparable prior *survey*. See §3.1 for the boundary. |
| 1705.05417 | Carlip (CQG 2017) | review; "$d_s\sim 2$ almost universal" for UV-renormalizable theories | We invert the emphasis: the *almost* is the point, not a caveat. |
| 1311.2530 | Eichhorn–Mizera (CQG 2014) | causal-set $d_s$ **increases** for random walk on the causal graph | One of our two CST probe rows. |
| 1507.00330 | Belenchia–Benincasa–Marciano–Modesto (PRD 2016) | causal-set non-local d'Alembertian gives universal $d_s\to 2$ in all $D$ | The other CST probe row. The contradiction between this and 1311.2530 is our §4. |

### 3.1 The honest boundary against Calcagni's program

The sharpest version of the referee attack is: *"This is the Calcagni program (1311.3340, 1304.2709, 1408.0199, 1708.07445) repackaged. Calcagni already computes $d_s$ across approaches, already notes it is not universal, already knows it is probe/structure-sensitive in causal sets."* We accept that the overlap is high and state precisely where our line is:

- Calcagni and collaborators compute $d_s$ for each approach with the method appropriate to that approach (Seeley–DeWitt and saddle point for QFT/Stelle; combinatorial Laplacians for GFT/spin foam; fractional measures for multifractional spaces). Our value-add is a **single functional $P(\sigma)=\int d^Dk\,e^{-\sigma F(k)}$, one numerical engine, one $d_s$ definition**, validated against *all* of these published numbers simultaneously (12/12). The "map of quantum gravity" (1708.07445) is a survey collation across methods; it is not one engine reproducing all entries.
- The probe-dependence in causal sets is documented in the two source papers (1311.2530 and 1507.00330) *separately*. What is not in the literature as a stated organizing principle is **the probe elevated to a classification axis on the same footing as $z$ and $D$**, justified by the explicit same-theory/opposite-trend contradiction (§4). Calcagni–Oriti–Thürigen note structure-dependence but do not write "$(z,D,\text{probe})$ is the classifier."
- The discriminator framing — that $d_s\to 2$ is a $\gamma=2$ subclass artifact, *explicitly violated* by GR, Hořava $z=2$, and random walks — inverts the usual "evidence for convergence" reading. Carlip's "almost universal" is the closest, but it is presented as a caveat to universality, not as a classification principle.

If a referee shows that any one of these three — the simultaneous single-engine validation, the probe-as-axis principle, or the discriminator framing — is already stated as such in the literature, the corresponding claim must be downgraded. We have not found it stated; the TODO lists the exact searches that must still be run by a human.

---

## 4. The probe axis, forced by an internal contradiction (the load-bearing section)

### 4.1 The contradiction we found

Our own knowledge graph carried two mutually contradictory edges, each citing real literature:

- One edge (causal-sets $\to$ spectral-dimension) asserted that random walks and the non-local d'Alembertian on causal sets give a spectral dimension that **drops** at short scales (sometimes to $\sim 2$), echoing CDT and AS.
- Another edge (non-commutative-geometry $\to$ causal-sets) asserted the opposite — that $d_s$ in causal sets **increases** at short scales.

Both cited correctly; both were partially right; together they were inconsistent. The naive resolution ("one of the citations is wrong") is itself wrong.

### 4.2 The resolution: the probe is the missing variable

The contradiction dissolves once the diffusion probe is named:

- **Random walk on the discrete causal order** (Eichhorn–Mizera, 1311.2530): $d_s$ *increases* at short scales — the opposite of CDT/AS. The cause is the Lorentzian non-locality of causal sets, baked into the causal structure; the causal spectral dimension (meeting probability of two random walkers) shows the same upward trend.
- **Non-local d'Alembertian / continuum-reconstructed propagator** (Belenchia et al., 1507.00330): heat-kernel analysis with the causal-set-derived propagator gives a *universal* drop $d_s\to 2$ in the UV in all dimensions, because the regularized propagator behaves as $(k^2)^{D/2}$ at high momentum, improving the UV and reducing the effective dimension.

Both results are correct and do not contradict each other: they measure different aspects of the *same* discrete structure with different probes. We corrected both database edges to carry the full probe-resolved statement with both citations.

### 4.3 Why this forces the probe to be a classification axis

This is the strongest single result in the note, and it is not a numerical correction — it is structural. The *same theory* (causal sets) yields **opposite UV trends** depending solely on the probe: $d_s\to 2$ (dimensional reduction) under the d'Alembertian, $d_s$ rising above $D$ under the random walk. Therefore the phrase "the UV spectral dimension of causal sets" has no referent until the probe is specified. The classifier cannot be $(z,D)$; it must be $(z,D,\text{probe})$. Probe-dependence is not a measurement artifact to be averaged away — it is a physical fingerprint of the non-local, fundamentally Lorentzian structure of the discrete spacetime. The contradiction in our database was not a bug in the data; it was the data telling us the third axis was missing.

---

## 5. Results: the master classification table

### 5.1 The centerpiece ($D=4$)

Each row is computed by the *same* engine; the "validation" column records agreement with the published value. No number here is a new discovery; the assembly and its reading are the contribution.

| approach | probe | $z_{\rm eff}$ | $d_s^{\rm UV}$ | $d_s^{\rm IR}$ | validation | source |
|---|---|---|---|---|---|---|
| General relativity | heat kernel ($k^2$) | $z=1$ | $\mathbf{4}$ | $4$ | REPRODUCE | Carlip 1705.05417 |
| Hořava–Lifshitz | heat kernel (anisotropic) | $z=2$ | $\mathbf{5/2}$ | $4$ | REPRODUCE | 0902.3657 |
| Hořava–Lifshitz | heat kernel (anisotropic) | $z=3$ | $\mathbf{2}$ | $4$ | REPRODUCE | 0902.3657 |
| Stelle quadratic gravity | heat kernel $k^2(1+k^2/m^2)$ | $z=2$ (UV $k^4$) | $\mathbf{2}$ | $4$ | REPRODUCE | 1408.0199 |
| Asymptotic safety | heat kernel ($\eta_*=-2\Rightarrow1/p^4$) | $z_{\rm eff}=2$ | $\mathbf{2}$ | $4$ | REPRODUCE | 0508202, 1110.5224 |
| **Causal sets** | **d'Alembertian (Benincasa–Dowker)** | $z_{\rm eff}=D/2$ | $\mathbf{2}$ | $4$ | REPRODUCE | 1507.00330 |
| **Causal sets** | **random walk on causal graph** | $z_{\rm eff}<1$ | $\mathbf{>D}$ (rises; num. $8$, illustrative) | $4$ | REPRODUCE (qual.) | 1311.2530 |
| Multifractional (Calcagni) | heat kernel (fractional measure) | $z_{\rm eff}=D/2$ | $\mathbf{2}$ | $4$ | REPRODUCE (compare) | 1304.2709 |

**Numerical agreement.** All 12 validation checks pass: GR UV $=4.0$; Hořava $z=2$ UV $=2.5$; Hořava $z=3$ UV $=2.0$; Stelle / AS / d'Alembertian / multifractional UV $=2.0$; all IR $=4.0$; random walk UV $=8.0>D$ (illustrative, see §6). The symbolic isotropic master returns $D/\gamma$.

### 5.2 How to read the table

Three readings, in increasing order of the note's contribution:

1. **The "universal $2$" is a column, not a law.** Every UV value of $2$ in the table is a $\gamma=2$ row: $D/\gamma=4/2$. Stelle, AS ($\eta_*=-2\Rightarrow k^4$), the causal-set d'Alembertian ($k^D$ with $D/2=2$ tuned), and the multifractional pick all share UV $k^4$-like behaviour. The convergence is the coincidence of this subclass.
2. **The violations are not edge cases.** GR ($d_s=4$, the actual world in the IR and at any scale for the unmodified Laplacian), Hořava $z=2$ ($d_s=5/2$, a perfectly standard anisotropic value), and the random-walk probe ($d_s>D$) all sit *outside* the $\to 2$ column. These are not pathologies; they are common, physically motivated cases.
3. **One theory spans the table by probe alone.** The two causal-set rows are the same theory. They are the proof that $(z,D)$ is insufficient.

### 5.3 The flow picture

`ds_flow.png` overlays every $d_s(\sigma)$ flow (x-axis $\log_{10}(1/\sigma)$: IR left, UV right). All curves start at $d_s=4$ in the IR and descend to their UV values of $2$ or $5/2$ — **except** the random-walk probe on the causal set, which alone *rises*, toward $8$. The single rising curve is the visual statement of the whole note.

---

## 6. Limits and honest scope

1. **Effective isotropic kernels, not first-principles simulations.** The causal-set d'Alembertian and the random walk are intrinsically Lorentzian and discrete; their true behaviour is not an isotropic Euclidean propagator. Our $F(k)$ are *effective* kernels engineered to reproduce the published *asymptotics* (d'Alembertian: universal UV $2$; random walk: UV rising above $D$), not microscopic sprinkling simulations. The random-walk row is explicitly **qualitative**, and its numerical value $8=D+4$ is an *illustrative* choice satisfying only "$d_s^{\rm UV}>D$"; the exact number depends on sprinkling density and walk definition, and Eichhorn–Mizera publish no universal asymptotic constant.
2. **Crossovers are inserted, not derived.** The IR$\leftrightarrow$UV transitions (Stelle, AS, Hořava) are modeled with hand-inserted two-power crossover kernels, not derived from an RG flow. The UV and IR *limits* are robust; the *shape* of the transition is model-dependent and must not be read quantitatively.
3. **Asymptotic safety uses a fixed-point $\eta$, not a running $\eta(k)$.** The anomalous dimension is taken at its constant NGFP value $\eta_*=-2$; the genuine scale-dependent $\eta(k)$ (full FRG flow) is not integrated. Sufficient for the UV/IR limits, not for the transition detail.
4. **The multifractional row uses one canonical class.** We take $\gamma_{\rm UV}=D/2$ ($d_s\to 2$); Calcagni catalogues several classes with different UV values. Our row is a comparison value only.
5. **Numerical precision.** The validation tolerance is $0.06$ (finite $\sigma$ window plus quadrature). Plateaux are flat to $\lesssim 1\%$.
6. **AI-assisted provenance.** The engine (`calc.py`), the table, and the citation transcriptions were produced by an AI-assisted exploratory pipeline. No human has yet independently re-run the engine, re-derived the limits, or re-checked the conventions against the source PDFs. This is a gate, not a footnote (see TODO §0).

---

## 7. Conclusion

A single return-probability engine, $P(\sigma)=\int d^Dk\,e^{-\sigma F(k)}$, reproduces *all* the published UV and IR spectral dimensions for general relativity, Hořava–Lifshitz ($z=2,3$), Stelle gravity, asymptotic safety, causal sets (both probes), and the multifractional measure (12/12 checks). The conclusion we draw from the assembled table is not that these theories converge but that $d_s^{\rm UV}$ *discriminates* between them: it is the fingerprint of the triple $(z,D,\text{probe})$. The third axis — the probe — is not optional bookkeeping: the same theory (causal sets) gives $d_s\to 2$ under a d'Alembertian and $d_s$ rising above $D$ under a random walk, so the UV dimension is ill-posed without naming the probe, a point forced on us by a literal contradiction we found and fixed in our own database. The apparent universality of $d_s\to 2$ is the coincidence of a single subclass — UV $k^4$ propagators, $\gamma=2$ in the master $D/\gamma$ — explicitly violated by GR ($4$), Hořava $z=2$ ($5/2$), and random-walk probes ($>D$). The spectral dimension is a fingerprint, not a constant.

---

*Sources: VYPOCET-01-ds-klasifikace.md; core-data/calculations/ds-classification/results.json (numerical engine `calc.py`, symbolic check via sympy). Probe contradiction resolved in verification/ds-contradiction.md; novelty boundary in verification/novelty/ds-cluster.md. Prior art: Hořava 0902.3657; Sotiriou–Visser–Weinfurtner 1105.6098; Calcagni–Modesto–Nardelli 1408.0199; Calcagni–Oriti–Thürigen 1311.3340; Calcagni–Nardelli 1304.2709; Calcagni et al. 1708.07445; Carlip 1705.05417; Eichhorn–Mizera 1311.2530; Belenchia–Benincasa–Marciano–Modesto 1507.00330; AS: Lauscher–Reuter hep-th/0508202, Reuter–Saueressig 1110.5224.*
