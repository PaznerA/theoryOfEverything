# TODO — what must be strengthened before draft-02 could become a real note

**Status: internal exploratory draft (v0.1, AI-assisted). NOT submission-ready. This list is the gate.**

The physics core here is a single exact rational identity ($-18/11$) plus a clean falsification of its naive bosonic extension. The arithmetic is convention-free and reproducible; the vulnerability is almost entirely in *framing* — whether an expert calls it trivial, and whether the conventions are airtight. This list targets exactly those.

---

## 0. Authorship / AI-assisted ethics note (must appear in any real version)

- This note and the underlying calculation (`calc.py`, exact sympy arithmetic) were produced by an **AI-assisted exploratory research pipeline**. No human has yet independently re-derived the heat-kernel coefficients, re-run the sympy, or re-checked the citations against the source PDFs.
- Any real submission requires: (a) a named human author who has verified the heat-kernel algebra (Vassilevich eq. 4.28 → $(a,c)$ per spin) and the spectral-action coefficients (CC9606 eq. 2.24) **by hand**, not just trusting the transcription; (b) an explicit AI-assistance statement per the target venue's policy and the project's publishing conventions; (c) public release of `calc.py` so the rational arithmetic is reproducible by anyone.
- Do not represent the eq.-2.24 transcription, the Duff Table 1 values, or the "verbatim from PDF" annotations as human-verified until a human has opened those PDFs and confirmed them. The provenance notes in VYPOCET-02 say "ověřeno verbatim z PDF" — that claim itself must be re-checked by a human before release.
- The identity is the kind of clean result that is easy to over-sell. Keep the claim narrow: *a ratio equality through one shared $a_4$*, content-independent on the fermionic sector. Nothing about model selection or unification should be stated as established.

---

## 1. The central referee attack: "this is trivial to anyone who knows heat kernels"

This is the single most likely rejection. A heat-kernel expert may say: *"Of course the spectral-action $C^2/$Euler ratio equals the single-Weyl-fermion $c/(-a)$ — both are literally the same $a_4$ coefficient of the same Dirac operator. You have rediscovered that $a_4$ is $a_4$."* The note lives or dies on the answer.

**The rebuttal must make three points, with evidence:**

1. **Triviality of the mechanism ≠ triviality of the statement.** The derivation (§2) is deliberately elementary *because* that is the proof it is a theorem. But the *explicit equality of these two specific published numbers* — CC's $-3f_0/10\pi^2 : 11f_0/60\pi^2$ and Duff's $1/40 : -11/720$ — collapsing to the same $-18/11$ has, per the novelty check, never been written down. Andrianov–Lizzi and Kurkov–Lizzi–Vassilevich connect spectral action and anomaly via RG flow and the bosonic action, but neither states this coefficient-ratio identity. **Document this gap explicitly**: quote the closest passages in 1001.2036 and 1106.3263 and show they stop short of the ratio equality. If a hostile referee finds it stated anywhere (Connes–Marcolli book; van Suijlekom's textbook; a Vassilevich review), the note must be downgraded or withdrawn.
2. **Why nobody stated it.** Hypothesis to defend in print: the two communities use different *normalizations* ($1/2880\pi^2$ heat-kernel vs $1/(4\pi)^2$ CFT) and different *bases* for the Euler term (Vassilevich's conformal combination vs Duff's $G$), so the equality is invisible *unless* one deliberately forms the convention-free ratio in CC's own basis. The contribution is precisely the observation that the ratio is the invariant object and that it lands on $-18/11$. State this as the reason for novelty, not as an excuse.
3. **The non-trivial half is the falsification.** Even granting the fermionic half is "obvious in hindsight," the clean bosonic break ($-1.636$ vs $-0.853$) and its reading (spectral $a_4$ gravity is fermion-induced; bosonic loops are not in the identity) is a positive, falsifiable statement that is *not* a tautology. Lead with this if the fermionic identity is judged too elementary to stand alone.

---

## 2. Convention dependence (the second-most-likely attack) — must be airtight

The whole result is a number; a referee will probe every convention that could move it.

- **Duff conventions.** Pin every value to Duff arXiv:2003.02688: the anomaly convention $g^{\mu\nu}\langle T_{\mu\nu}\rangle=\tfrac{1}{(4\pi)^2}(cF-aG)$ (eq. 14), the $720a$/$720c$ counting formulas (eq. 17), and the Table-1 entries (real scalar $1/360,1/120$; Weyl $11/720,1/40$; vector $31/180,1/10$). **A human must open the PDF and confirm these against the actual eq./table numbers** — the draft asserts them as verbatim. Note: Duff's $a,c$ vs the "$a,c$" of other groups (e.g. anomaly-coefficient sign and the $a$↔$c$ naming) differ across the literature; state which convention and check the sign of the Euler entry ($-a$ vs $+a$ in $\langle T\rangle$).
- **Vassilevich conventions.** Pin the $a_4$ master coefficient to hep-th/0306138 eq. 4.28 and the per-spin Table-1 coefficients ($a_H$: scalar 1, Dirac $-7/2$, vector+ghost $-13$; $b_H$: 1, $-11$, 62). Document that the $b_H$ column is a *conformal* Euler combination, not Duff's $G$ — this is why raw $a_H/b_H$ (scalar 1, Dirac $7/22$, vector $-13/62$) is **not** $c/(-a)$, and the match is made only in CC's $C^2$, $R^\ast R^\ast$ basis. A referee who computes $a_H/b_H$ and gets a different number must find this caveat already addressed in the text. (It is, in §5; make sure it is prominent, not buried.)
- **Chamseddine–Connes conventions.** Pin $\alpha_0=-3f_0/10\pi^2$, $\tau_0=11f_0/60\pi^2$ to hep-th/9606001 eq. 2.24 and the CCM hep-th/0610241 rewriting. Confirm the $R$-sign footnote (CC9606 takes $R<0$ on spheres) and verify it touches only signs, not the ratio.
- **The "$-a$" choice.** The headline ratio is $c/(-a)$, not $c/a$, because Euler enters $\langle T\rangle$ with $-a$. Make explicit that this sign choice is forced by the convention, not chosen to make the match work. Show that the *spectral* side independently has opposite relative sign between $C^2$ and $R^\ast R^\ast$ ($\alpha_0<0$, $\tau_0>0$), so $-18/11$ (negative) is genuinely the matched object.

---

## 3. Scheme / regularization dependence of $a_4$

- **Is $a_4$ scheme-independent here?** The integrated $a_4$ in $d=4$ is the conformal anomaly, which is famously *not* fully scheme-independent: the $a$-coefficient (Euler) is a genuine anomaly (scheme-independent, Cardy/$a$-theorem), but the $c$-coefficient and especially the $R^2$/$\Box R$ terms can carry scheme-dependent (local-counterterm) pieces. **Address head-on:** does the $C^2/$Euler ratio depend on the regularization scheme used to define $a_4$? Argue that $C^2$ and Euler are the scheme-*independent* combinations (the $\Box R$ ambiguity sits in a separate, total-derivative invariant), so the ratio is robust — or, if not fully, bound the scheme ambiguity and report it. This is a real physics point, not just bookkeeping.
- **RG running.** Free-field $(a,c)$ vs running $(a,c)$ in the interacting SM. The spectral action sits at the unification scale; the anomaly coefficients are scheme/scale-dependent away from free fields. State that the match is a free-field / fixed-scheme statement and that a running comparison needs a matched scheme (and that the $a$-theorem constrains the IR vs UV $a$ but not the ratio directly).
- **Inner-fluctuation share of $C^2$.** The full-SM gravitational $a_4$ gets bosonic contributions from inner fluctuations of $D$; their exact share of the $C^2$ coefficient beyond the Dirac multiplicity $N$ was not computed. So the "full-SM mismatch" ($-0.853$) is an **upper bound** on the discrepancy, not its exact value — keep it labelled as such, and ideally compute the exact inner-fluctuation contribution to close this.

---

## 4. Claims to soften or sharpen

- **"Theorem, not coincidence."** Justified by §2, but the word "theorem" invites scrutiny. Either keep it and make §2 fully rigorous (state the bundle, $E=-\tfrac14 R$ for the spinor, the trace over the spinor representation), or downgrade to "exact identity forced by a shared heat-kernel coefficient."
- **"Sakharov-induced gravity."** This framing is borrowed from Andrianov–Lizzi / Platania et al. and from CC's own motivation. Cite it as *their* reading extended, not as a new claim. Do not overstate that the spectral action "is" Sakharov gravity — it is a covariant completion in their sense.
- **"$\nu_R$ moves it closer."** True for the *full-SM* number only, and only marginally ($-0.853\to-0.866$). The draft already flags that this is *not* evidence about the (content-independent) identity. Keep that disclaimer prominent — it is the easiest place to be accused of over-claiming a "near-miss" as significant.
- **"Constraint on almost-commutative geometries."** Currently outlook, not result. Keep it clearly speculative until a second example (a non-SM spectral triple) is worked through and shown to either satisfy or violate the constraint.

---

## 5. Cross-checks required before release

- **Independent re-derivation** of $(a,c)$ for one Weyl fermion from the $a_4$ master (Vassilevich 4.28) directly, by hand, landing on $11/720,1/40$ — to confirm the per-spin table is being used correctly and the basis change to $C^2$/Euler is right.
- **Re-derive $-18/11$ three ways** and show they agree: (i) CC $\alpha_0/\tau_0$; (ii) single-Weyl $c/(-a)$; (iii) Dirac $2\times$Weyl $c/(-a)$. (Draft asserts all three; a human should reproduce them.)
- **Literature search for prior statement.** Re-run the novelty check specifically against: Connes–Marcolli *Noncommutative Geometry, Quantum Fields and Motives*; van Suijlekom *Noncommutative Geometry and Particle Physics*; any Vassilevich/Fursaev review giving $a_4$ in the $C^2$/Euler basis next to $(a,c)$. If the ratio is stated anywhere, this note becomes a clarification, not a discovery.
- **Verify every arXiv ID and bibliographic detail** (1001.2036, 1106.3263, 2003.02688, hep-th/0306138, hep-th/9606001, hep-th/0610241) against arXiv before any release. Do not cite anything not personally confirmed.

---

### Minimum bar to call this "real"

Section 0 (ethics + human re-derivation), §1 (the triviality rebuttal with the documented novelty gap), §2 (airtight conventions with PDF confirmation), and §3 (scheme-dependence of the $C^2$/Euler ratio addressed) are all blocking. The arithmetic is solid; the work that remains is making the *framing* referee-proof and confirming no one has stated the ratio before. Until then this remains an internal exploratory note.

---

## Update 2026-06-06 — VYPOCET-11 closes the two computational blockers (graviton sector + index theorem)

`core-data/calculations/a4-graviton-index/` + `knowledge-base/vypocty/VYPOCET-11-graviton-index.md`. Both BRAINSTORM-03 queue items (#1 graviton/Weyl sector, #7 index-theorem test) done in exact sympy, conventions re-verified against the source literature during the run. **Net effect: draft-02 is STRENGTHENED** on exactly the "why fermions?" and "is $-18/11$ protected?" axes a referee will attack.

- **Graviton does NOT rescue the full match (test #1, decisive for H3g-4).** The *physical* Einstein graviton is **non-conformal** — its trace anomaly is gauge/scheme dependent, defined only on-shell, carries an $R^2/\Box R$ piece, and therefore has **no convention-free $(a,c)$ and no well-defined $c/(-a)$** [Duff hep-th/9308075; gauge-dep. Anselmi hep-th/9503187, Martini–Nink–Percacci 2206.13287]. The *conformal* ("Weyl") graviton (4-derivative conformal gravity, a different field) does have clean $(a,c)=(87/20,199/30)$, giving $c/(-a)=-398/261\approx-1.525$ — still **not** $-18/11$. A collinearity test in the $(a,c)$ plane shows **only the Weyl fermion (and its multiples) lie on the $-18/11$ ray**; scalar, vector, and conformal graviton are all off it. To force $-18/11$ by adding gravitons one would need multiplicity $x=-143/32<0$ (unphysical). So **no induced/fundamental partition with the graviton on the fundamental side restores the identity** — it strictly delimits the Dirac sector. This is the test the draft flagged as the highest-yield blocker, and it lands on the H3g-4 side.
  - **Use in §3 / §4:** state explicitly that the graviton cannot enter the $C^2/$Euler ratio — *two independent prohibitions agree*: (a) Sakharov logic (the graviton kinetic term **is** the induced $a_4$; counting it as a fundamental loop double-counts), and (b) anomaly logic (a non-conformal field has no clean $(a,c)$ to contribute). This is a clean strengthening of the "Sakharov-induced gravity" reading in §3, not a new speculative claim.

- **The $-18/11$ has an index-theoretic shadow (test #7).** Deriving $a_4(D^2)$ from the Gilkey/Vassilevich master in the $\{C^2,E_4,R^2\}$ basis reproduces the Duff per-spin $(a,c)$ **exactly** (scalar $(1/360,1/120)$, Dirac $(11/360,1/20)$, Weyl $(11/720,1/40)$), with $R^2$ coefficient $=0$ (both conformal). The same spinor $a_4$ whose $E_4$ coefficient is the conformal $a$-anomaly ($a=11/720$, Gauss–Bonnet/Euler-characteristic response) carries, in its **Pontryagin** sector, the Atiyah–Singer index density $\hat A|_4=-p_1/24$; the normalization lock $\mathrm{ind}(D)=-\sigma/8$ with Rohlin ($\sigma$ divisible by 16) holds ($\sigma=16\to\mathrm{ind}=-2$). **This is the reusable answer to the §1 "trivial / why these fermions" attack**: $-18/11$ is content-independent *because* it sits inside an index-protected object — every Weyl fermion carries the same $(a,c)$ = the same unit of index density. Document which parts are textbook (master coefficient, $(a,c)$, $\hat A=-p_1/24$, Rohlin) vs the note's added value (the explicit $\{C^2,E_4,R^2\}$-basis identification of $-18/11$ as the spinor-$a_4$ ratio, and the lock tying the Euler/conformal and Pontryagin/index sectors of the *same* $a_4$).

- **Still NOT addressed by VYPOCET-11 (blocking items unchanged):** §0 human re-derivation/ethics, §1 documented-novelty-gap quotes from 1001.2036 & 1106.3263, §2 PDF confirmation of every Duff/Vassilevich/CC value by a human, §3 RG-running and the inner-fluctuation share of $C^2$. The computational physics is now closed on both queue items; the remaining gate is framing + human verification, as before.
