**DRAFT v0.2 — generated 2026-06-06, revised 2026-06-08, internal research draft, NOT submitted, requires human review.** (v0.2: §4 graviton non-rescue + index protection added [F-014]; §5 cosmological-constant no-sister-identity negative added [F-020].)

# The −18/11 fermionic identity: an exact Weyl-to-Euler coefficient ratio common to the spectral action, induced gravity, and the conformal trace anomaly

## Abstract

We report an exact rational identity. In the $a_4$ Seeley–DeWitt term of the Chamseddine–Connes spectral action the ratio of the Weyl-squared coefficient to the Euler (Gauss–Bonnet) coefficient is
$$
\frac{\alpha_0}{\tau_0}=\frac{-3f_0/10\pi^2}{\,11f_0/60\pi^2\,}=-\frac{18}{11}.
$$
The same number is the conformal-anomaly ratio $c/(-a)$ of a single Weyl fermion, $\tfrac{1/40}{-(11/720)}=-\tfrac{18}{11}$. Because every two-component Weyl fermion carries identical $(a,c)$, the identity is **content-independent on the purely fermionic sector**: it holds *exactly* for one Weyl fermion, for the 45 Weyl fermions of the Standard Model, and for the 48 of the Standard Model with three right-handed neutrinos, with zero residual. This is a theorem, not a numerical coincidence: both sides descend from the same $a_4$ heat-kernel coefficient of the Dirac operator. We give the one-page derivation. We then show the identity is sharply broken by bosons: the naive "full Standard Model" ratio $c/(-a)$ is $-1698/1991\approx-0.853$ (without $\nu_R$) versus the spectral target $-18/11\approx-1.636$ — a 48% relative mismatch. The lesson is structural: the $a_4$ gravity of the spectral action is *fermion-induced* gravity in the sense of Sakharov, and bosonic loops are simply not part of the $a_4$ identity. Adding three $\nu_R$ moves the full-SM ratio marginally closer ($-219/253\approx-0.866$) but, by content-independence, does not touch the fermionic identity itself. We position this note as completing the triangle whose two-way edges were established by Andrianov–Lizzi (arXiv:1001.2036) and Kurkov–Lizzi–Vassilevich (arXiv:1106.3263): the third edge, the explicit equality of the spectral-action $C^2/$Euler ratio with the single-fermion $c/(-a)$ anomaly ratio through one shared $a_4$, has to our knowledge not been stated before. We close with the implication: anomaly-matching of $(a,c)$ becomes a convention-free constraint on the gravitational sector of almost-commutative geometries.

---

## 1. Statement and context

### 1.1 The number

Two computations, performed independently in the standard literature, return the same rational number.

**(i) Spectral action.** The bosonic spectral action $S=\mathrm{Tr}\,f(D/\Lambda)$ of Chamseddine–Connes, expanded in the heat kernel, has an $a_4$ (curvature-squared, $\Lambda^0$) term whose gravitational part is, in their normalization (hep-th/9606001, eq. 2.24; transcribed in CCM hep-th/0610241),
$$
\alpha_0=-\frac{3f_0}{10\pi^2}\ \ (\text{coefficient of }C_{\mu\nu\rho\sigma}C^{\mu\nu\rho\sigma}),
\qquad
\tau_0=\frac{11f_0}{60\pi^2}\ \ (\text{coefficient of }R^\ast R^\ast),
$$
with $f_0=f(0)$ the value of the cutoff function at the origin. The ratio is convention- and $f_0$-free:
$$
\boxed{\ \frac{\alpha_0}{\tau_0}=-\frac{18}{11}=-1.6363\ldots\ }
$$

**(ii) Trace anomaly.** In the standard convention $g^{\mu\nu}\langle T_{\mu\nu}\rangle=\tfrac{1}{(4\pi)^2}\,(c\,F-a\,G)$, $F=C^2$, $G=$ Euler density (Duff, arXiv:2003.02688, eq. 14–17, Table 1), a single two-component Weyl fermion has
$$
a_{\rm Weyl}=\frac{11}{720},\qquad c_{\rm Weyl}=\frac{1}{40},
\qquad\Rightarrow\qquad
\frac{c_{\rm Weyl}}{-a_{\rm Weyl}}=\frac{1/40}{-11/720}=-\frac{18}{11}.
$$
(The Euler density enters $\langle T\rangle$ with the sign $-a$; the relevant ratio of the two curvature-squared invariants is therefore $c/(-a)$.) A Dirac control, $2\times$ Weyl, gives $c=1/20$, $a=11/360$, ratio $-18/11$ — identical.

The two ratios are equal, exactly.

### 1.2 Why this is the natural comparison

The absolute $C^2$ coefficient of the spectral action carries a factor $f_0$ (a moment of the unspecified cutoff function) and the overall fermionic multiplicity $N=\mathrm{Tr}(\mathbf 1_F)$, neither of which has a counterpart in the $1/(4\pi)^2$ normalization of the anomaly. The *ratio* of the two curvature-squared invariants, however, is a pure number on both sides — independent of $f_0$, of $N$, and of the overall heat-kernel normalization $1/2880\pi^2$. It is the natural convention-free observable, and it is what we match.

### 1.3 Content independence (the sharp form)

Both $a$ and $c$ are additive over fields, and every Weyl fermion contributes the *same* pair $(11/720,\,1/40)$. Hence for any purely fermionic content of $N_W$ Weyl fermions,
$$
\frac{c_{\rm tot}}{-a_{\rm tot}}=\frac{N_W\,c_{\rm Weyl}}{-N_W\,a_{\rm Weyl}}=\frac{c_{\rm Weyl}}{-a_{\rm Weyl}}=-\frac{18}{11},
$$
with the $N_W$ cancelling identically. The match is therefore exact for

| fermionic content | $a_{\rm tot}$ | $c_{\rm tot}$ | $c/(-a)$ | mismatch vs $-18/11$ |
|---|---|---|---|---|
| single Weyl fermion | $11/720$ | $1/40$ | $-18/11$ | **0 (exact)** |
| SM fermions, no $\nu_R$ ($N_W=45$) | $11/16$ | $9/8$ | $-18/11$ | **0 (exact)** |
| SM fermions, with $\nu_R$ ($N_W=48$) | $11/15$ | $6/5$ | $-18/11$ | **0 (exact)** |

This is the headline: **the identity does not select a fermion count.** Whether the almost-commutative geometry carries 45 or 48 Weyl fermions, its Dirac sector reproduces the spectral-action $C^2/$Euler ratio exactly. The right-handed neutrinos that Connes' axioms favour (16 spinors per generation $=4^2$) are, for this identity, free: they change neither side.

---

## 2. Why it is a theorem, not a coincidence (the one-page derivation)

Both numbers are the same $a_4$ heat-kernel coefficient of one Dirac operator, read in two normalizations. We make the descent explicit.

**Step 1 — one master coefficient.** For a Laplace-type operator $D^2=-(\nabla^2+E)$ acting on a vector bundle with curvature $\Omega_{ij}$, the fourth Seeley–DeWitt coefficient is (Gilkey; Vassilevich, hep-th/0306138, eq. 4.28)
$$
a_4=\frac{1}{(4\pi)^{n/2}}\frac{1}{360}\int\sqrt g\,\mathrm{tr}_V\!\Big[60E_{;kk}+60RE+180E^2+12R_{;kk}+5R^2-2R_{ij}R_{ij}+2R_{ijkl}R_{ijkl}+30\,\Omega_{ij}\Omega_{ij}\Big].
$$
This single formula is the common ancestor. Everything below is a choice of bundle and endomorphism $E$.

**Step 2 — the curvature-squared content fixes a basis.** The three independent quadratic curvature invariants can be traded for $C^2$ (Weyl-squared), $G$ (Euler density), and $R^2$. The pure-gravity part of $a_4$ (the $\Omega$-independent, $E$-independent terms $5R^2-2R_{ij}R_{ij}+2R_{ijkl}R_{ijkl}$, plus the contributions through $E\propto -\tfrac14 R$ for a fermion) is what carries the $C^2$ and $G$ coefficients. For a given field this part is fixed once and for all by the spin, because $E$ and $\Omega$ are fixed by the spin connection.

**Step 3 — the same $a_4$ is the trace anomaly.** In $d=4$ the integrated $a_4$ coefficient *is* the conformal anomaly: the textbook relation (Duff 1977; Deser–Schwimmer; reviewed in Vassilevich hep-th/0306138) is
$$
a_4=\frac{1}{16\pi^2}\int\sqrt g\,\big(c\,W^2-a\,E_4\big),
$$
i.e. the central charges $(a,c)$ are *defined* as the $a_4$ coefficients of $E_4$ and $W^2$. For a Weyl fermion this reads off $(a,c)=(11/720,\,1/40)$ in Duff's normalization.

**Step 4 — the same $a_4$ is the spectral action's $\Lambda^0$ term.** The Chamseddine–Connes spectral action is the heat-kernel expansion of $\mathrm{Tr}\,f(D/\Lambda)$; its $\Lambda^0$ piece *is* the same $a_4(D^2)$. Their eq. 2.24 is precisely this coefficient evaluated for the (almost-commutative) Dirac operator and written in the $C^2$, $R^\ast R^\ast$ basis, giving $(\alpha_0,\tau_0)=(-3f_0/10\pi^2,\,11f_0/60\pi^2)$.

**Step 5 — the ratio is normalization-invariant.** Steps 3 and 4 take the *same* object $a_4(D^2)$ and divide it by two different overall constants ($1/16\pi^2$ with a CFT measure on one side; $1/2880\pi^2$ times $f_0\,N$ on the other). Any such overall rescaling cancels in the ratio of two terms *within* $a_4$. Therefore
$$
\Big[\tfrac{\text{coeff}(C^2)}{\text{coeff(Euler)}}\Big]_{\rm spectral}
=\Big[\tfrac{\text{coeff}(C^2)}{\text{coeff(Euler)}}\Big]_{a_4(D^2)}
=\Big[\tfrac{c}{-a}\Big]_{\rm anomaly},
$$
each equality being "the same $a_4$, different prefactor." The shared value is $-18/11$. **QED.** The equality is forced by the single heat-kernel coefficient; it cannot fail for any field whose $a_4$ is computed from a Dirac-type operator, which is why it is content-independent on the fermionic sector.

*Bonus trace of the common origin.* The Euler numerical factor of the spectral action is $11/60$; the Weyl-fermion central charge $a$ is $11/720$. The same prime "$11$" appears in both (ratio $(11/60)/(11/720)=12$), a fingerprint of the identical Dirac $a_4$ term rather than two unrelated computations.

---

## 3. The falsification: bosons break it (and what that teaches)

The naive strong reading of the identity would demand that the spectral $C^2/$Euler ratio match the anomaly ratio of the *full* field content — fermions plus the Higgs scalars and the gauge bosons. It does not, and the failure is clean and informative.

Scalars and vectors carry different $(a,c)$ ratios: a real scalar has $c/(-a)=\tfrac{1/120}{-1/360}=-3$, a vector has $\tfrac{1/10}{-(31/180)}=-18/31$. Adding the SM bosonic content ($N_0=4$ real scalars from one complex Higgs doublet; $N_1=12$ vectors $=8+3+1$) to the 45 fermions gives

| content | $a_{\rm tot}$ | $c_{\rm tot}$ | $c/(-a)$ | rel. mismatch vs $-18/11$ |
|---|---|---|---|---|
| spectral target | — | — | $-18/11\approx-1.636$ | — |
| full SM, no $\nu_R$ | $1991/720$ | $283/120$ | $-1698/1991\approx-0.853$ | $-0.479$ |
| full SM, with $\nu_R$ | $253/90$ | $73/30$ | $-219/253\approx-0.866$ | $-0.471$ |

The full-SM ratio is $-0.853$, off the spectral $-1.636$ by 48%. The strong version is **falsified, cleanly and with fully documented conventions.**

**The lesson — Sakharov-style fermion-induced gravity.** The mismatch is not a defect; it is the content of the identity. The $C^2$ term of the spectral action descends from $\mathrm{Tr}\,f(D/\Lambda)$, i.e. from the Dirac operator, whose internal multiplicity is the dimension of the *fermionic* Hilbert space. Structurally the spectral-action gravity is induced by the fermions running in the loop — Sakharov's induced gravity, completed covariantly by the spectral formalism (a reading already present, on the two-way edges, in Andrianov–Lizzi and Kurkov–Lizzi–Vassilevich). Bosonic loops contribute to the *physical* full effective action and to the *physical* running of $(a,c)$, but they are **not** part of the $a_4$ object whose ratio the identity equates. The identity therefore matches the spectral $C^2/$Euler ratio to the anomaly ratio of *exactly the fermionic content that induces it* — and to nothing more. The bosonic mismatch is the precise statement of which sector the spectral $a_4$ "sees."

**The $\nu_R$ observation.** Adding three right-handed neutrinos shifts the full-SM ratio from $-0.853$ to $-0.866$, i.e. marginally *toward* the fermion-dominated $-18/11$ — consistent with the fact that $\nu_R$ tips the fermion/boson balance toward the fermionic value, and consistent with Connes' axioms wanting $\nu_R$. But this is a property of the *full* mixture only. On the fermionic identity proper, $\nu_R$ is invisible: §1.3 already gives $-18/11$ exactly with or without it. We flag this asymmetry to avoid over-claiming: the $\nu_R$ "improvement" is real for the full-SM number but is *not* evidence about the identity, which is content-independent by construction.

---

## 4. Implications and outlook

1. **A convention-free constraint on almost-commutative geometries.** The result reframes a piece of the spectral-action output as an anomaly-matching condition. Any finite spectral triple $(\mathcal A,\mathcal H,D)$ whose gravitational $a_4$ is to be read as the $\Lambda^0$ term *must* have its $C^2/$Euler ratio equal to the $c/(-a)$ of the fermion representation on $\mathcal H$. For a purely fermionic Dirac sector this is automatic ($-18/11$); it becomes a genuine constraint the moment one tries to attribute the gravitational sector to a *mixed* (fermion+boson) content, as the §3 mismatch shows one cannot.

2. **The graviton does not rescue a bosonic reading — and the discriminator is index-protected.** A natural objection is that the gravitational sector should itself carry $(a,c)$ and so might restore a bosonic match. It does not. The physical Einstein graviton is *not* conformal: it has no well-defined pure $(a,c)$ pair (the central charges are gauge/scheme-dependent and defined only on-shell; Duff, hep-th/9308075, hep-th/9503187), so it cannot be placed on the $(a,c)$ plane at all. The *conformal* (four-derivative Weyl) graviton, which does have a pure pair, gives $c/(-a)=-398/261\approx-1.525\neq-18/11$, and no single bosonic field is collinear with the Weyl-fermion ray $-18/11$; the full SM plus a conformal graviton gives $-6474/5123\approx-1.264$, still not $-18/11$. The multiplicity $x$ of conformal gravitons that would be required to force the full-SM ratio onto $-18/11$ is negative ($x=-143/32<0$), i.e. unphysical. The $-18/11$ identity is therefore a *strict fermionic discriminator*, protected from a bosonic "rescue" by index theory: the relevant Rohlin-type constraint (signature $\sigma=16\Rightarrow$ index $-2$) locks the fermionic sector that the identity selects [F-014]. This converts the §3 bosonic mismatch from a numerical accident into an index-theoretic statement of *which* sector the spectral $a_4$ sees.

3. **Completing the triangle.** Andrianov–Lizzi (arXiv:1001.2036, "Bosonic Spectral Action Induced from Anomaly Cancellation," JHEP 05 (2010) 057) established spectral-action $\leftrightarrow$ anomaly as one edge; Kurkov–Lizzi–Vassilevich (arXiv:1106.3263, "Spectral action, Weyl anomaly and the Higgs–dilaton potential," JHEP 10 (2011) 001) established spectral-action $\leftrightarrow$ Weyl-anomaly via heat kernel + RG flow as another. The present note supplies the explicit third edge: a single rational number, $-18/11$, equal on both sides through one shared $a_4(D^2)$, valid for any fermionic content. The three edges close a triangle (spectral action — induced/Sakharov gravity — trace anomaly) around one coefficient.

4. **Outlook.** (a) Promote the constraint to a model-selection tool: scan candidate almost-commutative geometries and reject those whose Dirac-sector $c/(-a)$ deviates from the spectral $C^2/$Euler ratio under a chosen completion prescription. (b) Track the constraint under RG flow — $(a,c)$ run in the interacting theory while the spectral action lives at the unification scale; a matched-scheme comparison is required (see TODO). (c) Determine whether the inner-fluctuation (bosonic) contributions to the *full* gravitational $a_4$ enter the $C^2$ coefficient beyond the pure Dirac multiplicity $N$, which would sharpen "full-SM mismatch" from an upper bound to an exact number.

---

## 5. Honest scope and limits

- **Ratios, not absolute magnitudes.** The match is between *ratios* of curvature-squared invariants. Absolute $C^2$ coefficients agree only up to the documented normalization factor (heat-kernel $1/2880\pi^2$ vs CFT $1/(4\pi)^2$; a single real scalar gives $c=1/120$, not $1/180$ — the standard 120-vs-180 factor, logged as TEST_B in the results). The ratio is the convention-free statement.
- **Heat-kernel vs CFT basis for the Euler term.** Vassilevich's tabulated $b$-coefficient uses a conformal Euler combination, not exactly Duff's $G$; raw $a_H/b_H$ therefore differs from $c/(-a)$. The comparison is made in Chamseddine–Connes' own $C^2$, $R^\ast R^\ast$ basis (their eq. 2.24), which coincides with Duff's; there the $-18/11$ holds.
- **Free-field, tree-level.** $(a,c)$ are free-field values; in the interacting SM they run. The spectral action is an effective action at the unification scale; a direct comparison assumes a common regularization/scale point.
- **Inner-fluctuation gravitational pieces.** The full-SM gravitational $a_4$ also receives bosonic contributions from inner fluctuations of $D$; we did not include their exact share of the $C^2$ coefficient beyond the Dirac multiplicity $N$, so the "full-SM" mismatch is an upper bound on the discrepancy, not its exact value.
- **Sign convention of $R$.** CC9606 takes $R$ negative for spheres; this affects signs only, not the ratios on which the identity rests.
- **No sister identity for the cosmological constant.** The same fermion-induction logic does *not* predict a second scheme-robust identity for $\Lambda$: the spectral-action $\Lambda$-term ($a_0$, cutoff-quartic $f_4\Lambda^4$) and the Einstein–Hilbert term ($a_2$, cutoff-quadratic $f_2\Lambda^2$) sit on *different* cutoff orders, so any ratio between them is dimensionful and scheme-dependent (it carries an explicit $(f_4/f_2)\Lambda^2$ factor), and $\Lambda_{\rm cc}/M_{\rm Pl}^2$ carries an explicit $1/N$, hence is content-*dependent* — unlike $-18/11$. (The relevant supertrace constraint also fails on the NCG-SM content: $\mathrm{STr}\,\mathbf 1 = n_B-n_F = -62$, worsening to $-68$ with $\nu_R$.) Reporting this negative bounds the claim: the $-18/11$ identity is the curvature-squared-ratio statement, with no cosmological-constant analogue [F-020].

---

*Sources: VYPOCET-02-a4-matching.md; core-data/calculations/a4-anomaly-matching/results.json (exact rational arithmetic, sympy). Conventions: Duff arXiv:2003.02688 (anomaly, $(a,c)$ table); Vassilevich hep-th/0306138 (heat-kernel $a_4$ master); Chamseddine–Connes hep-th/9606001 eq. 2.24, CCM hep-th/0610241 (spectral action). Prior two-way edges: Andrianov–Lizzi arXiv:1001.2036; Kurkov–Lizzi–Vassilevich arXiv:1106.3263.*
