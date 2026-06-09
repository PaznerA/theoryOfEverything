**DRAFT v0.3 — generated 2026-06-06, revised 2026-06-08, internal research draft, NOT submitted, requires human review.** (v0.2: analytic mechanism of opposite-sign asymmetry, direct eigenvector-overlap measurement (~45° subspace rotation at <2% spectral change), and eigenvector-level superradiant-band signature — all from VYPOCET-10, integrated throughout Abstract, Results, Discussion. v0.3: §4.2 superradiant power-law program added — $W_{\rm sr}\sim\Omega(r)^{B}$ with a *continuously* spin-dependent exponent $B(a)$ (6.10→2.54, $dB/da=-2.20$), constant $B=D-1=3$ decisively rejected, BTZ below Kerr (VYPOCET-14/15/26 = F-017/F-018/F-030); Häfner–Klein attribution of arXiv:2602.09796 corrected; F-IDs attached to §3.5b/§3.6/§4.2. Abstract refinement 2026-06-08: the $B(a)$ superradiant-exponent trend (continuous, $B=D-1=3$ rejected, BTZ below Kerr) promoted into the Abstract as signature (vii), F-030.)

# Sorkin–Johnston vacua through the ergoregion: numerical construction in rotating BTZ and equatorial Kerr with an eigenvector signature of superradiance

## Abstract

For a rotating black hole there is no canonical quantum vacuum: the Kay–Wald theorem forbids any quasi-free state that is simultaneously Hadamard, isometry-invariant and globally defined, because superradiant modes obstruct a consistent positive/negative-frequency split with respect to the (non-timelike) Killing field inside the ergoregion. The Sorkin–Johnston (SJ) prescription evades this obstruction entirely: it builds a distinguished pure quasi-free state directly from the Pauli–Jordan operator $i\Delta$ restricted to a bounded region, requiring no timelike Killing vector. We perform what is, to our knowledge, the first numerical SJ construction in rotating spacetimes. Using the conformal triviality of the 2D massless scalar (the retarded propagator on a causal set is exactly $G_R=\tfrac12 C$, independent of the conformal factor), we sprinkle bounded $(t,\varphi)$ patches at fixed radius in rotating BTZ and in the equatorial section of asymptotically flat Kerr. We find: (i) the SJ state exists with a machine-precision $\pm$-paired $i\Delta$ spectrum at fixed-$r$ sections *inside* the ergoregion where $\partial_t$ is spacelike, while the matched static section there is not even Lorentzian; (ii) the interior null cone edge aligns with the $\varphi$-axis exactly on the static limit ($r=\sqrt M$ in BTZ, $r=2M$ in Kerr); (iii) frame dragging imprints a co-rotating causal-link asymmetry that saturates to $+1$ inside the ergoregion; (iv) the causal-count asymmetry and the SJ two-point asymmetry carry *opposite signs* — explained analytically: in the null coordinates aligned with the actual cone, $W_0 = -\tfrac{1}{4\pi}\ln|\Delta u\,\Delta v|$, so counter-rotating links (near the squeezed null edge) carry stronger correlations per link, while co-rotating links are more numerous, with the toy model reproducing both signs and magnitudes to within $\sim12\%$; (v) the $i\Delta$ spectrum is conformally invariant, so rotation lives in the eigenvectors, not the eigenvalues — confirmed directly: on a single shared sprinkling, the positive SJ subspaces of the rotating and static sections are rotated by a mean principal angle of $44.6^\circ$ ($\mathrm{mean}\;\cos^2=0.507$) while the eigenvalue spectra agree to $2.0\%$; (vi) the SJ positive eigenvectors carry weight in the superradiant frequency band $\omega(\omega-k\Omega)<0$ that grows monotonically with spin and sharply toward the ergosphere (0.000 at $r=4M$ to 0.0755 just outside $r_{\rm erg}$ at $r=2.05$), with the static control exactly zero; (vii) the onset of this superradiant weight follows a power law $W_{\rm sr}\sim\Omega(r)^{B}$ in the *local* ZAMO angular velocity rather than the ergosphere as a threshold ($\Delta\mathrm{AIC}\;230$–$4200$ favouring the $\Omega$-law), and the exponent is a *continuous, decreasing function of frame-dragging*: $B(a)$ falls from $6.1$ to $2.5$ across $a=0.3$–$0.99$ ($dB/da=-2.20$, $z=-33.6$), decisively rejecting the dimensional constant $B=D-1=3$ ($\chi^2/\mathrm{dof}\sim350$, the curve crossing $3$ only at a single spin $a\approx0.75$), with BTZ ($\Omega\sim r^{-2}$) lying systematically below the Kerr curve ($\Omega\sim r^{-3}$) — consistent with $B$ tracking the asymptotic fall-off of $\Omega$ rather than a privileged dimensional value (one 2D fixed-$r$ construct, not an independent dimension-versus-asymptotics separation) (F-030). All signatures replicate across both backgrounds, indicating geometry-independent properties of SJ states in rotating spacetimes. This is a 2D exploratory probe, not a 4D Kerr result, but it isolates concrete eigenvector-level targets for a full Teukolsky-mode construction.

---

## 1. Introduction

### 1.1 The missing vacuum for rotating black holes

Quantum field theory on a curved background requires a choice of state. On globally static spacetimes the timelike Killing field $\partial_t$ supplies a positive-frequency decomposition and hence a preferred Boulware vacuum; bifurcate Killing horizons additionally admit a Hartle–Hawking state. For a rotating black hole neither construction survives. Inside the ergoregion the Killing field $\partial_t$ becomes spacelike ($g_{tt}>0$), so it cannot define positive frequency, and the only globally timelike co-rotating combination $\partial_t+\Omega_H\,\partial_\varphi$ generically fails to be timelike everywhere outside the horizon. The technical manifestation is *superradiance*: in the band $0<\omega<m\Omega_H$ the "up" modes carry negative Klein–Gordon norm despite positive frequency, so no globally consistent positive/negative-frequency split respecting the $(\partial_t,\partial_\varphi)$ isometries exists.

This is not merely a calculational inconvenience. The Kay–Wald theorem (Kay & Wald, *Phys. Rep.* **207** (1991) 49) establishes a sharp no-go: on the maximally extended Kerr spacetime there is no quasi-free state that is (i) invariant under the $\partial_t$ and $\partial_\varphi$ isometries, (ii) Hadamard near the horizon, and (iii) globally defined. The candidate Boulware and Hartle–Hawking analogues simply do not exist (see also Balakumar, arXiv:2303.13488). The best that survives is the Unruh state, recently shown to exist and to be Hadamard for the bosonic Teukolsky field on subextreme Kerr (Häfner & Klein, arXiv:2602.09796), but the Unruh state is tied to the asymptotic in/out structure and is not a region-intrinsic object.

### 1.2 The Sorkin–Johnston prescription needs no timelike Killing vector — the point

The Sorkin–Johnston (SJ) construction (Afshordi, Aslanbeigi & Sorkin, arXiv:1205.1296; Sorkin & Yazdi, arXiv:1611.10281) builds a distinguished pure quasi-free state from spacetime data alone. Given a globally hyperbolic spacetime and a relatively compact subregion $M'$, one forms the Pauli–Jordan (commutator) operator
$$
\Delta(x,y) = G_R(x,y) - G_A(x,y),\qquad A \equiv i\Delta,
$$
which is a bounded self-adjoint operator on $L^2(M',\mathrm{dvol})$. Its spectral decomposition $A=\sum_k\lambda_k|\psi_k\rangle\langle\psi_k|$ defines the SJ Wightman function as the positive part,
$$
W_{\rm SJ}(x,y) = \sum_{\lambda_k>0}\lambda_k\,\psi_k(x)\,\psi_k^*(y).
$$
The output is a pure quasi-free state determined *uniquely* by the region and the field, with no input about symmetries.

The crucial observation for rotating spacetimes is that **the SJ construction never references a timelike Killing field**. The Kay–Wald hypothesis of isometry invariance is exactly what SJ drops: an SJ state on a rotating background is generically *not* invariant under $\partial_\varphi$ (or even $\partial_t$), so the Kay–Wald no-go does not apply to it. Likewise the Fewster–Verch dynamical-locality and Wick-square results (arXiv:1106.4785, arXiv:1307.5242) — which establish that generic SJ states fail to be Hadamard — are formulated for ultrastatic slabs with compact Cauchy surfaces, a class that excludes both Kerr and our bounded sections. SJ thus offers a candidate state precisely where the symmetric Hadamard family fails as a whole. This paper asks the most concrete version of the question: *can the SJ state be constructed, numerically and to machine precision, inside an ergoregion where $\partial_t$ is spacelike?*

### 1.3 Scope and strategy

We adopt the cheapest viable strategy (Strategy II of the project hypothesis H02): a 2D analogue where analytic control is maximal. The lever is a single exact fact: the 2D massless scalar wave operator is conformally invariant, so on a causal set the retarded propagator is exactly $G_R=\tfrac12 C$, independent of curvature and of the conformal factor. Every geometric effect — curvature, frame dragging, the ergoregion — then enters *only* through the tilt of the light cones in the chosen section. We probe two backgrounds with identical machinery: rotating BTZ (asymptotically AdS$_3$) and the equatorial section of asymptotically flat Kerr. The agreement between them is itself a result: it indicates the signatures are geometry-independent properties of SJ states in dragged spacetimes, not artifacts of a particular metric.

We emphasise the scope honestly. This is a 2D, massless-scalar, fixed-$r$ probe at modest $N$, not a 4D Kerr calculation. It is framed as "the SJ state exists and is computable where stationary constructions fail," and as a map of which observables carry the rotation signal, to guide a future full construction.

---

## 2. Method

### 2.1 The lever: conformal triviality of the 2D massless scalar

The entire construction rests on one exact statement. For a **massless** scalar in **any** 2D spacetime, the retarded Green function on a causal set is
$$
G_R = \tfrac12\,C, \qquad C_{xy}=\begin{cases}1 & y\prec x \ (y\ \text{in the causal past of }x)\\[2pt]0 & \text{otherwise.}\end{cases}
$$
The reasons, verified against the literature:
- Every 2D Lorentzian metric is locally conformally flat, $g_{ab}=\Omega^2\eta_{ab}$.
- The massless scalar wave operator is conformally invariant in $d=2$ (conformal coupling $\xi=0$ *is* minimal coupling in two dimensions).
- The retarded Green function therefore depends only on the causal/conformal structure, not on the conformal factor $\Omega$.

On a causal set this is the exact identity $G_R=\tfrac12 C$ (Sorkin–Yazdi, arXiv:1611.10281, eq. 9 and footnote 5: exact for all sprinkling densities). For a massive field $G_R=\tfrac12 C\,(I+(m^2/2\rho)C)^{-1}$, whose $m\to0$ limit is exactly $\tfrac12 C$ (Johnston et al., arXiv:1701.07212; arXiv:1712.04227). The use of $\tfrac12 C$ in curved 2D — justified precisely by conformal flatness — is carried out explicitly for AdS$_2$ in arXiv:2504.12919.

**Consequence.** For any fixed-$r$ 2D section of a rotating black hole we need *only* the causal order of the sprinkled points. Curvature, frame dragging and the ergoregion all enter exclusively through the tilt of the light cones (and through the proper-volume measure used for sprinkling).

### 2.2 Geometry I: rotating BTZ

The rotating BTZ black hole (Bañados–Teitelboim–Zanelli; metric and horizons cross-checked against arXiv:gr-qc/0003097 and arXiv:1707.08133), with AdS radius $\ell=1$:
$$
ds^2 = -N^2\,dt^2 + N^{-2}\,dr^2 + r^2\,(d\varphi + N^\varphi\,dt)^2,
$$
$$
N^2 = -M + r^2 + \frac{J^2}{4r^2},\qquad N^\varphi = -\frac{J}{2r^2}.
$$
The induced fixed-$r$ $(t,\varphi)$ metric has components $g_{tt}=M-r^2$, $g_{t\varphi}=-J/2$ (constant dragging), $g_{\varphi\varphi}=r^2$. Horizons are $r_\pm^2=\tfrac12(M\pm\sqrt{M^2-J^2})$; the ergosphere (static limit, $g_{tt}=0$) sits at $r_{\rm erg}=\sqrt M$. For $J\neq0$ one has $r_+<r_{\rm erg}$, so there is an ergoregion $r_+<r<r_{\rm erg}$ where $g_{tt}>0$ and $\partial_t$ is spacelike — no timelike Killing field.

**Choice of section (verified symbolically).** The fixed-$\varphi$ $(t,r)$ section becomes *Euclidean* inside the ergoregion (signature $(+,+)$ since both $g_{tt}>0$ and $g_{rr}>0$): $\varphi$ cannot be dropped there. The fixed-$r$ $(t,\varphi)$ section remains Lorentzian through the entire ergoregion,
$$
\det h = g_{tt}g_{\varphi\varphi}-g_{t\varphi}^2 = M r^2 - r^4 - J^2/4 = -N^2 r^2 < 0 \quad (r>r_+).
$$
Inside the ergoregion $\partial_t$ is spacelike but the dragged combination $(1,+s_{\rm drag})$ is timelike — the cones simply tilt. We therefore use the fixed-$r$ $(t,\varphi)$ section.

### 2.3 Geometry II: equatorial Kerr

For asymptotically flat Kerr (geometrised units $G=c=1$, mass $M$, spin $a$, $|a|\le M$; equatorial components cross-checked against the standard Kerr-metric literature, $\det h$ verified with sympy), with $\Sigma=r^2+a^2\cos^2\theta$, $\Delta=r^2-2Mr+a^2$, in the equatorial plane $\theta=\pi/2$ ($\Sigma=r^2$):
$$
g_{tt}=-\Big(1-\frac{2M}{r}\Big),\quad g_{t\varphi}=-\frac{2Ma}{r}\ (\text{$r$-dependent, unlike BTZ}),\quad g_{\varphi\varphi}=r^2+a^2+\frac{2Ma^2}{r}.
$$
The exact key identity is
$$
\det h = g_{tt}g_{\varphi\varphi}-g_{t\varphi}^2 = -(r^2-2Mr+a^2) = -\Delta,
$$
so the fixed-$r$ $(t,\varphi)$ section is Lorentzian wherever $\Delta>0$, i.e. outside the outer horizon $r_+=M+\sqrt{M^2-a^2}$. The equatorial static limit is $r_{\rm erg}=2M$ (independent of $a$), and the ergoregion is the shell $(r_+,2M)$.

**Honest geometric differences from BTZ.** (a) The Kerr equatorial ergoregion is a *thin shell*: for $M=1$ it is $(1.954,2.0)$ at $a=0.3$, $(1.800,2.0)$ at $a=0.6$, $(1.436,2.0)$ at $a=0.9$. Hence a given small radius (e.g. $r=1.5$) lies outside the horizon only for large spin. (b) $g_{t\varphi}$ is $r$-dependent in Kerr (constant $-J/2$ in BTZ), so the cone geometry varies even within one family of fixed-$r$ sections. Both points are reported transparently in the results.

### 2.4 Causal order, sprinkling, SJ pipeline

The induced 2-metric $h=\begin{psmallmatrix}g_{tt}&g_{t\varphi}\\ g_{t\varphi}&g_{\varphi\varphi}\end{psmallmatrix}$ is constant on a fixed-$r$ section (uniform cones). A displacement $D=x-y$ is future-directed causal iff
$$
h(D,D)\le 0 \quad\text{(causal)},\qquad h(T,D)<0\quad\text{(future)},\quad T=(1,\,s_{\rm drag}),\ \ s_{\rm drag}=-g_{t\varphi}/g_{\varphi\varphi},
$$
where $T$ is the locally non-rotating (zero-angular-momentum) reference direction, timelike since $h(T,T)=\det h/g_{\varphi\varphi}<0$. This defines a clean partial order on the patch.

We sprinkle $N$ points uniformly in $(t,\varphi)$ on a bounded coordinate patch $(t,\varphi)\in[0,T]\times[0,\Phi]$ — a finite $\varphi$-window (a causal rectangle on the cylinder, *not* the full $2\pi$ circle), giving a relatively compact globally hyperbolic patch that avoids the periodic identification $\varphi\sim\varphi+2\pi$. The proper volume $\sqrt{-\det h}\,dt\,d\varphi$ is constant, so uniform sprinkling has the correct measure. We use a fixed-$N$ (canonical) ensemble.

The SJ pipeline, with conventions inherited from the project's earlier 2D causal-diamond work and from Sorkin–Yazdi (arXiv:1611.10281):
1. $C_{xy}=1$ iff $y\prec x$ (tilted cones), zero diagonal.
2. $G_R=\tfrac12 C$; $\Delta=G_R-G_R^{\mathsf T}=\tfrac12(C-C^{\mathsf T})$; $i\Delta$ Hermitian.
3. SJ Wightman $W=$ positive part of $i\Delta=\sum_{\lambda_k>0}\lambda_k|v_k\rangle\langle v_k|$.

### 2.5 Observables: two sign-meaningful asymmetries

Both observables are built on the *same* causal data:
- **Causal directional asymmetry** $A_{\rm caus}=2f_{\rm co}-1$. Among all causally related pairs ($x$ to the future of $y$), record the azimuthal advance $d\varphi=\varphi_x-\varphi_y$; $f_{\rm co}$ is the fraction with $d\varphi>0$. In a static section the cone is symmetric under $\varphi\to-\varphi$, so $f_{\rm co}=0.5$, $A_{\rm caus}=0$. Frame dragging tilts the cone and favours $+\varphi$. Inside the ergoregion the cone is fully dragged: *every* causal link has $d\varphi>0$, so $A_{\rm caus}=+1$. This is the cleanest 2D causal-set imprint of the superradiant band.
- **SJ Wightman directional asymmetry** $A_W$. Over the same pairs, weight by the mean $\mathrm{Re}\,W(x,y)$ per link in the co- versus counter-rotating direction. This probes whether the *quantum correlations* of the SJ vacuum inherit the dragging. $A_W$ is undefined inside the ergoregion (no counter-rotating links, $n_{cc}=0$) — correctly reported, not an error.

---

## 3. Results

We fix $M=1$ throughout. BTZ fiducial: $J=0.6$ (rotating) versus $J=0$ (static control); $N=1600$, $T=\Phi=1.4$, 4 seeds. Kerr fiducial: $a=0.6$ (and $a=0.9$ aggressive); $N=1600$, $T=\Phi=1.4$, 3 seeds. The eigenvector-overlap and superradiant-wedge computations (§3.5b) use 5 seeds (shared sprinklings, seeds 101–505).

### 3.1 Existence inside the ergoregion; static control fails (headline)

**BTZ.** At $r=0.974$ *inside* the ergoregion ($r_+=0.949<r<r_{\rm erg}=1.0$, $g_{tt}=+0.0507>0$, so $\partial_t$ spacelike), the fixed-$r$ section is Lorentzian ($\det h=-0.0419$), both null slopes are positive $(+0.100,+0.532)$, and the SJ state is fully constructible: the $i\Delta$ spectrum has **796 positive / 796 negative** exact $\pm$ pairs with relative pairing residual $4.6\times10^{-16}$ and trace $2.3\times10^{-13}$ — machine precision. The matched static section ($J=0$) at the *same* $r$ is **not Lorentzian** (cone discriminant $-0.192<0$, $\det h=+0.048>0$, Euclidean): there is nothing for the SJ construction to act on.

**Kerr.** At $r=1.900$ inside the $a=0.6$ ergoregion ($g_{tt}=+0.053>0$) the section is Lorentzian ($\det h=-0.17$) and SJ gives **787+/787−** pairs, residual $4.7\times10^{-16}$. At $r=1.718$ inside the $a=0.9$ ergoregion ($g_{tt}=+0.164$), **790+/790−**, residual $5.3\times10^{-16}$. The matched static (Schwarzschild) section at the same $r$ has $\det h=+0.485>0$ (Euclidean, because that $r$ lies inside the Schwarzschild horizon $r_+=2M$): SJ is not constructible. In all ergoregion cases $f_{\rm co}=1.000$, $A_{\rm caus}=+1.000$, and the measured mean cone slope matches the frame-dragging slope (BTZ: $0.306$ vs $0.316$; Kerr $a=0.6$: $0.143$ vs $0.145$; $a=0.9$: $0.219$ vs $0.223$).

This is a direct numerical demonstration of the central thesis: the SJ state is well-defined to machine precision inside a rotating ergoregion where $\partial_t$ is spacelike, exactly where the static analogue degenerates and where no symmetric Hadamard vacuum exists. (We note that the exact $\pm$-pairing of the spectrum is an *algebraic* consequence of $i\Delta$ being $i$ times a real antisymmetric matrix — Hermitian with eigenvalues in $\pm$ pairs by construction — so the $\sim10^{-16}$ pairing residual tests the numerics, not the physics; the physical content is existence/non-degeneracy of the section inside the ergoregion, not the pairing itself.)

### 3.2 The interior null slope vanishes exactly at the static limit

A radial scan across the ergosphere (BTZ $J=0.6$; Kerr $a=0.6$ and $a=0.9$) shows the inner null cone edge $s_-=d\varphi/dt|_-$ passing through zero *exactly* at the static limit:
- BTZ: $s_-\approx-0.045$ just outside $r_{\rm erg}=1.0$; the cone edge aligns with the $\varphi$-axis at $r=\sqrt M=1.0$.
- Kerr: linear interpolation of $s_-$ gives the zero crossing at $r=2.0000$ for both $a=0.6$ and $a=0.9$, i.e. exactly $r_{\rm erg}=2M$, independent of spin.

Inside the ergoregion both null slopes are positive (fully dragged cone, $f_{\rm co}=1$); outside, the asymmetry decays smoothly as the dragging $\sim1/r^2$. This is a textbook cross-check: the inner light-ray turns around precisely at the static limit, where a co-rotating null ray can no longer make azimuthal headway against the rotation.

### 3.3 Co-rotating link fraction and the frame-dragging profile

The co-rotating link fraction $f_{\rm co}$ rises monotonically from the static value $0.5$ (far away) to $1.0$ inside the ergoregion. For BTZ ($J=0.6$): $f_{\rm co}=1.0$ at $r=0.958$ (inside), $0.923$ at $1.014$, $0.770$ at $1.070$, $0.605$ at $1.30$, $0.534$ at $1.80$. For Kerr the same monotone rise holds, saturating at $f_{\rm co}=1.0$ throughout the ergoregion and decaying outward. The dependence on spin is monotone: at the comparable radius $r=2.5$ in Kerr, $A_{\rm caus}=0.197,\,0.361,\,0.482$ for $a=0.3,\,0.6,\,0.9$ respectively, with the frame-dragging slope growing approximately linearly in $a$. This is the clean 2D causal-set signature of the superradiant band: inside the ergoregion no causal influence can be sent against the rotation.

### 3.4 The opposite-sign asymmetry phenomenon

The most striking and least anticipated finding is that the causal-count asymmetry and the SJ correlation asymmetry carry **opposite signs**. Outside the ergoregion, where both are defined:

| Background | $r$ | $A_{\rm caus}$ | $A_W$ |
|---|---|---|---|
| BTZ $J=0.6$ | 1.30 | $+0.227\pm0.007$ ($33.8\sigma$ from 0) | $-0.211$ |
| BTZ $J=0$ (control) | 1.30 | $+0.007\pm0.009$ ($0.7\sigma$, $\approx0$) | $-0.008$ ($\approx0$) |
| Kerr $a=0.6$ | 2.6 | $+0.317\pm0.002$ | $-0.296$ |
| Kerr $a=0.9$ | 2.6 | $+0.431\pm0.001$ | $-0.382$ |
| Kerr $a=0$ (control) | 2.6 | $+0.001\pm0.003$ | $+0.000$ |

The causal skeleton favours co-rotating links ($A_{\rm caus}>0$: more pairs co-rotate), yet the SJ two-point function is, per link, *stronger* in the counter-rotating direction ($A_W<0$). The static controls sit exactly on zero in both, confirming the effect is rotation. The phenomenon holds for every spin and every radius outside the ergoregion in both backgrounds. Its replication on a completely different (asymptotically flat) geometry promotes it from a possible BTZ artifact to a genuine property of the SJ vacuum in a dragged spacetime — one that a standard mode analysis tied to Killing symmetries would be ill-equipped to see, precisely because the SJ correlations live off the symmetry-adapted basis.

### 3.5 Conformal invariance of the spectrum: rotation lives in the eigenvectors

The $i\Delta$ eigenvalue spectra of the rotating and static sections at matched $r$ (outside the ergoregion) are nearly identical: relative difference $3.4\%$ in BTZ, with the same continuum plateau $k\lambda_k\approx 1/k$. A direct test on the *same* sprinkled points (removing sprinkling randomness) leaves only a $\sim1.8\%$ difference, attributable solely to the cone tilt changing *which* pairs are causally related (link fraction drifts $0.1795\to0.1818$); the $1/k$ shape is the same conformal class. We conclude that rotation does **not** reside in the bulk spectrum of $i\Delta$ — that is fixed by the conformal class — but in the **eigenvectors**, and hence in the two-point function $W$. This is exactly what the correlation-asymmetry observables detect and what the raw spectrum misses.

This conclusion is confirmed directly in §3.5b by a subspace-overlap measurement: on a single shared sprinkling, the positive SJ subspaces of the rotating ($a=0.9$) and static ($a=0$) sections have a mean principal angle of $44.6^\circ$ (mean $\cos^2=0.507$), while the spectra differ by only $2.0\%$ and the causal link fraction drifts by $0.6\%$. The static-versus-static sanity control gives $\cos^2=1.000000$ exactly. The eigenvectors swing by tens of degrees while the eigenvalues barely move.

### 3.5b Mechanism of the opposite-sign asymmetry, superradiant eigenvector signature, and direct subspace measurement

**Rotation lives in the eigenvectors — measured directly.** The subspace-overlap result is summarised in §3.5. For completeness: on a *single shared sprinkling*, the SJ positive subspace of the rotating section and of the matched static section are compared through principal angles (singular values of $V_{\rm rot}^\dagger V_{\rm stat}$). For Kerr $a=0.9$ versus $a=0$ at $r=2.6$ (5 seeds), the positive-eigenvalue spectra agree to $2.0\%$ and the causal link fraction drifts by only $0.6\%$, yet the two positive subspaces are rotated by a mean principal angle of $44.6^\circ$ (mean $\cos^2=0.507$). BTZ $J=0.6$ versus $J=0$ at $r=1.3$ gives the same $\cos^2=0.509$. A static-versus-static control on the same sprinkling returns $\cos^2=1.000000$ exactly, so the $\sim45^\circ$ rotation is not a method artifact. The eigenvalues barely move; the eigenvectors swing by tens of degrees. Rotation lives in $W$, not in the spectrum [F-013] (confirmed; 2D equatorial conformal sections, not full 4D fields).

**A superradiant signature in the frequency content of the SJ state.** Projecting the SJ positive eigenvectors onto approximate plane waves $e^{-i\omega t+ik\varphi}$ (Monte-Carlo $L^2$ overlap on the sprinkled points) yields the occupation map $P(\omega,k)=\sum_{\rm modes}\lambda\,|\langle\text{plane}|v\rangle|^2$ of the positive-SJ subspace. The static map is symmetric in $k$; the rotating map is visibly sheared, its occupation band and spectral gap tracking the drag line $\omega=k\Omega$ with $\Omega=-g_{t\varphi}/g_{\varphi\varphi}$ (the ZAMO angular velocity). Quantifying the weight in the discrete superradiant wedge $\omega(\omega-k\Omega)<0$ (co-rotating frequency $\omega-k\Omega$ opposite in sign to $\omega$), we find it grows monotonically with spin at $r=2.6$ ($0.0000,\,0.0012,\,0.0062,\,0.0171$ for $a=0,\,0.3,\,0.6,\,0.9$) and rises sharply toward the ergosphere at $a=0.9$ ($0.0000$ at $r=4.0$ to $0.0755$ just outside $r_{\rm erg}=2M$ at $r=2.05$). The static control is *exactly* zero — the wedge has measure zero when $\Omega=0$. The earlier remark that 2D has no superradiant analogue (the spectrum being conformally invariant) is thus refined: the superradiant imprint is present, but as an *eigenvector/frequency-content* signature, not a spectral one — exactly the structure we expect to find in 4D.

**Why the signs are opposite — the boosted-diamond toy model.** A fixed-$r$ section is a constant-$h$ ("sheared Minkowski") patch. In the null coordinates aligned with the actual cone, $u=\varphi-s_+t$ and $v=\varphi-s_-t$ (with $s_\pm$ the null slopes solving $g_{\varphi\varphi}s^2+2g_{t\varphi}s+g_{tt}=0$), the metric is purely off-diagonal ($h\propto du\,dv$, verified), so the massless Wightman function is $W_0=-\tfrac{1}{4\pi}\ln|\Delta u\,\Delta v|$ (up to a constant), depending only on the lightcone interval. The cone's timelike axis — the ridge of maximal interval — is the slope $s_{\rm drag}=\tfrac12(s_-+s_+)=-g_{t\varphi}/g_{\varphi\varphi}$, i.e. the frame-drag direction. Two effects then split:

- *Counting* (geometric). A causal link has slope $m\in(s_-,s_+)$; positive dragging opens the cone wider toward $+\varphi$ ($s_+>|s_-|$), so more links co-rotate and $A_{\rm caus}>0$. A continuum Monte-Carlo on a uniform patch (no SJ) gives $A_{\rm caus}^{\rm toy}=+0.217,\,+0.315,\,+0.426$ for BTZ ($J=0.6,r=1.3$), Kerr ($a=0.6,r=2.6$), Kerr ($a=0.9,r=2.6$) — matching the measured SJ values $+0.227,\,+0.317,\,+0.431$ to within $1\%$. The counting asymmetry is *purely* the cone aperture.
- *Correlation* (phase/interval). Along a link, $|\Delta u\,\Delta v|=(s_+-m)(m-s_-)\,dt^2$ is maximal at $m=s_{\rm drag}$ (longest interval, *weakest* $W_0$) and vanishes at the null edges (shortest interval, *strongest* $W_0$). Because dragging places $s_{\rm drag}>0$ on the co-rotating side, the counter-rotating band $(s_-,0)$ sits nearer a squeezed null edge, giving shorter intervals and hence *stronger* correlations per link: $A_W<0$. The bare log reproduces this sign in all three cases (the band-mean $\langle\ln|\Delta u\,\Delta v|\rangle$ is more negative on the counter side in every case).

The *magnitude* of $A_W$ is recovered once the finite-region offset of the SJ $W$ is included: regressing the measured per-link $\mathrm{Re}\,W$ against the continuum log gives correlation $0.95$–$0.97$; the numerator $m_{\rm co}-m_{\rm cc}$ is set by the log (sign), while the denominator $|m_{\rm co}|+|m_{\rm cc}|$ is set by the additive offset that the SJ construction fixes but the bare log does not. With the fitted offset, $A_W^{\rm toy}=-0.230,\,-0.334,\,-0.419$ against measured $-0.203,\,-0.298,\,-0.384$. The opposite sign is therefore not a normalization or binning convention (the v0.1 worry): it is the geometric consequence of frame dragging tilting the timelike axis onto the co-rotating side — counting favors the stretched null direction, correlation favors the squeezed one. (The toy null-diamond model reproduces both signs and magnitudes only to correlation $0.95$–$0.97$ — it explains the sign mechanism, it is not an exact derivation [F-013].)

### 3.6 BTZ $\leftrightarrow$ Kerr universality

All signatures of the BTZ probe (Sections 3.1–3.5b) replicate on equatorial Kerr: (i) machine-precision SJ existence inside the ergoregion with degeneracy of the static analogue; (ii) the interior null slope zeroing exactly at $r_{\rm erg}$ ($\sqrt M$ in BTZ, $2M$ in Kerr); (iii) the opposite-sign asymmetry for every $a$ and every $r$, with the same analytic mechanism (boosted-diamond toy model) reproduced in both geometries; (iv) monotone growth of asymmetry with spin; (v) the $\sim45^\circ$ eigenvector-subspace rotation at $<2\%$ spectral change replicated for BTZ ($\cos^2=0.509$) as well as Kerr ($\cos^2=0.507$). The signatures are insensitive to the asymptotics (AdS vs flat), to the curvature scale, and to whether $g_{t\varphi}$ is constant (BTZ) or $r$-dependent (Kerr). Within the conformal-lever framework this is expected — only the causal/conformal structure of the dragged section enters — and it is the central evidence that these are geometry-independent SJ properties of rotating spacetimes [F-009] (confirmed; 2D equatorial conformal sections of Kerr, not the full 4D field).

---

## 4. Discussion

### 4.1 Path to full 4D Kerr

The 2D probe identifies *where* the rotation signal lives: in the eigenvectors of $i\Delta$ / in $W$, not in the eigenvalue spectrum. This is now established by two independent measurements: (a) on a shared sprinkling, the positive SJ subspaces of rotating and static sections differ by $\sim45^\circ$ principal angle while spectra agree to $2\%$; (b) projecting eigenvectors onto plane waves reveals an occupation-map shear tracking the drag line $\omega=k\Omega$, and a superradiant-band weight $\omega(\omega-k\Omega)<0$ that grows with spin and toward the ergosphere. Together these sharpen the open question of hypothesis H02: do superradiant modes ($0<\omega<m\Omega_H$) contribute to SJ with positive or negative eigenvalues? In 2D the question has no direct spectral analogue (the spectrum is conformally invariant), which itself suggests that in 4D the superradiant imprint will again be an *eigenvector/two-point-function* signature rather than a coarse spectral one. A full construction (Strategy I/III of H02) requires either Poisson sprinkling into a bounded exterior region of Kerr with numerically integrated null geodesics for the causal order (Glaser, arXiv:0811.4235, extended to Kerr), since $G_R\neq\tfrac12 C$ in 4D, or an analytic SJ construction in the Teukolsky mode basis (Dafermos–Rodnianski boundedness, arXiv:2007.07211) with explicit checks of positivity for the superradiant band. The robustness of the opposite-sign phenomenon across two geometries, and its analytic derivation from the null-coordinate structure, are concrete predictions to test against either route.

### 4.2 Relation to superradiance

The co-rotating link fraction saturating to $f_{\rm co}=1$ inside the ergoregion is the causal-set face of superradiance: a classical influence cannot be sent against the rotation there, and the static limit $r_{\rm erg}$ is exactly where the inner null ray turns around. The opposite-sign result, now analytically explained (§3.5b), shows that while the *classical* causal skeleton is co-rotation-biased, the *quantum* SJ correlations weight the counter-rotating direction more strongly per link — a consequence of the massless Wightman function $W_0=-\tfrac{1}{4\pi}\ln|\Delta u\,\Delta v|$ and the squeezed-null-edge geometry. Beyond these classical and correlation signatures, the SJ positive eigenvectors carry a direct frequency-space imprint of the superradiant band: the weight in $\omega(\omega-k\Omega)<0$ grows monotonically from zero (at $a=0$ or $r\gg r_{\rm erg}$) to $0.0755$ just outside the ergosphere ($r=2.05$) at $a=0.9$, with the static control exactly zero by symmetry [F-013, F-017]. This 2D superradiant-band weight is not a reflection-coefficient ($|R_{lm}|^2>1$ requires the 4D Teukolsky route), but it is a concrete eigenvector-level prediction: in a full 4D construction, the superradiant imprint of the SJ state should appear in the frequency content of eigenvectors of $i\Delta$, not in its coarse spectrum.

**The superradiant-band weight scales as a power of the local frame-dragging rate, with a continuously spin-dependent exponent.** A radial scan of the superradiant weight $W_{\rm sr}$ against the local ZAMO angular velocity $\Omega(r)=-g_{t\varphi}/g_{\varphi\varphi}$ (near-zone radii with $W_{\rm sr}>0$, $N=1600$, 5 seeds, bootstrap CI across seeds) follows a power law $W_{\rm sr}\sim\Omega(r)^{B}$ rather than a function of the ergosphere as a discrete boundary: in log–log space an exponential model is decisively rejected against the power law (joint near+far fit $\Delta\mathrm{AIC}(E{-}S)=+3894$ [F-018, sj-far-zone]; per-geometry $\Delta\mathrm{AIC}$ in the range $230$–$4200$ [F-017, sj-threshold-scan: $+442$ at $a{=}0.6$, $+4216$ at $a{=}0.9$, $+232$ for BTZ]; correlation $\mathrm{corr}(\log W_{\rm sr},\log\Omega)=0.9992$ versus $0.942$ for $\log 1/(r-r_{\rm erg})$), and in the near zone $|A_W|\sim r^{-2.75\pm0.03}$ (predicted $-3$) and $|A_W|\sim\Omega^{0.98\pm0.01}$ (predicted $+1$) [F-018]. The fitted exponent $B$ is, however, **not** a privileged dimensional constant: removing the optimiser-bound artefact ($A\le100$) of the original fit, the reliable Kerr exponent $B(a)$ decreases *monotonically and continuously* with the frame-dragging spin — $6.10\,(a{=}0.3)$, $3.32\,(a{=}0.6)$, $2.67\,(a{=}0.9)$, $2.54\,(a{=}0.99)$, all with $R^2\ge0.988$ and $\mathrm{corr}_{\log\log}\ge0.995$, with slope $dB/da=-2.20\pm0.07$ ($z=-33.6$). A constant exponent equal to $D-1=3$ is *decisively rejected* ($\chi^2_{\rm const}=2473/7$ against a linear $\chi^2=111/6$; the curve $B(a)$ crosses $3$ only at the single spin $a\approx0.75$). The BTZ exponents sit *below* the Kerr curve at comparable rotation ($B=2.22$ at $J=0.6$, $2.12$ at $J=0.9$), consistent with the asymptotics (the absence of a Kerr-AdS reflecting boundary) moving the exponent without a privileged dimensional value — this is one fixed-$r$ 2D construct read across two backgrounds, not an independent variation of dimension against asymptotics [F-030]. The robust prediction for a 4D construction is therefore the *trend* — $dB/da<0$ together with the BTZ-below-Kerr ordering — not any single $B$. The earlier bounded values ($B=4.23$ at $a=0.6$, $3.82$ at $a=0.9$) were an artefact of the $A\le100$ optimiser bound and are superseded.

If this superradiant program survives to 4D, the SJ state would furnish a canonical, parameter-free input state for quantum superradiance calculations (mean emitted quanta, fluctuations, pair entropy) precisely where Boulware/Hartle–Hawking inputs are unavailable — and an independent comparison point for the Unruh state (arXiv:2602.09796) and for spectral spacetime-entropy definitions on Kerr.

### 4.3 Limitations

- **2D sections only.** This is a Strategy-II analogue (rotating BTZ; equatorial Kerr), not a 4D Kerr result. In 4D the conformal lever fails ($G_R\neq\tfrac12 C$), so null-geodesic integration or Teukolsky modes are required.
- **Fixed-$r$ uniform cones.** The induced 2-metric is constant, so a single section carries no radial gradient; $r$-dependence is mapped by scanning separate fixed-$r$ regions. A single 2D region covering $r$ through the ergoregion is impossible — the fixed-$\varphi$ $(t,r)$ section is Euclidean inside the ergoregion — so a faithful $r$-covering region would necessarily be 3D, beyond this probe.
- **Finite $\varphi$-window, not the full cylinder.** We use a causal rectangle to avoid the $\varphi\sim\varphi+2\pi$ identification. Since $\partial_\varphi$ is always spacelike ($g_{\varphi\varphi}>0$ outside $r_+$), no closed timelike curves arise from the $\varphi$-circle, but the periodic (wrap-around) case is a separate problem (see TODO).
- **Modest $N$ and few seeds.** $N=1600$, 4 seeds (BTZ) / 3 seeds (Kerr), fixed-$N$ canonical ensemble. Statistical errors on $A_{\rm caus}$ are $\sim10^{-3}$; existence and directional signs are robust, but no continuum ($N\to\infty$) extrapolation is performed here.
- **Kerr thin ergo-shell.** For small $a$ the shell $(r_+,2M)$ is narrow; $r=1.5$ is Lorentzian only for $a=0.9$. For $a=0.3,0.6$ the section at $r=1.5$ is inside the horizon and Euclidean — reported honestly, with a comparable $r=2.5$ scan added where all spins are Lorentzian.
- **SJ non-Hadamard caveat.** Generic SJ states are not Hadamard (Fewster–Verch, arXiv:1106.4785, arXiv:1307.5242). We measure existence and directional signatures, not UV structure, so this does not affect the claims here; a softened-SJ variant (Jubb–Surya, arXiv:2212.10592) restoring the Hadamard property at the cost of strict uniqueness is the natural extension for UV-sensitive observables.

---

## 5. References (arXiv IDs; to be verified against arXiv by a human before any release)

> ⚠️ Reference arXiv ID nebyla ověřena proti arxiv.org. Zejména nová 2025–2026 ID (např. 2602.09796, 2504.12919, 2303.13488) musí lidský revizor potvrdit (existence + autoři + obsah) před jakýmkoli vydáním — viz BRAINSTORM-05 §2 a REVIZE-PRO-CLOVEKA.md.

1. R. D. Sorkin and Y. K. Yazdi, *Entanglement Entropy in Causal Set Theory*, arXiv:1611.10281. [$G_R=\tfrac12 C$, $i\Delta$, SJ $W$ as positive part]
2. N. Afshordi, S. Aslanbeigi and R. D. Sorkin, *A distinguished vacuum state for a quantum field in a curved spacetime*, arXiv:1205.1296. [SJ continuum construction]
3. S. Johnston et al., *Scalar Field Green Functions on Causal Sets*, arXiv:1701.07212. [massive $G_R$, $m\to0$ limit]
4. *On the Entanglement Entropy of Quantum Fields in Causal Sets*, arXiv:1712.04227. [$G_R=\tfrac12 C$ conventions]
5. *Retarded Causal Set Propagator in 2D Anti-de-Sitter Spacetime*, arXiv:2504.12919. [conformal flatness $\Rightarrow$ $\tfrac12 C$ in curved 2D / AdS$_2$]
6. A. Mathur and S. Surya, *Sorkin–Johnston vacuum for a massive scalar field in the 2D causal diamond*, arXiv:1906.07952. [numerical SJ toolchain]
7. I. Jubb and S. Surya, *Softened SJ states / non-Hadamard SJ in 1+1D*, arXiv:2212.10592. [softened SJ, Hadamard recovery]
8. L. Glaser, R. Reid and S. Surya (sprinkling algorithm for Schwarzschild), arXiv:0811.4235. [causal-relation algorithm, extendable to Kerr]
9. B. S. Kay and R. M. Wald, *Theorems on the uniqueness and thermal properties of stationary, nonsingular, quasifree states on spacetimes with a bifurcate Killing horizon*, Phys. Rep. **207** (1991) 49. [no-go for symmetric Hadamard states on Kerr]
10. C. J. Fewster and R. Verch, *Dynamical locality and covariance*, arXiv:1106.4785. [no natural state; dynamical locality]
11. C. J. Fewster and R. Verch, *On a recent construction of vacuum-like quantum field states (Wick-square / Hadamard necessity)*, arXiv:1307.5242. [Hadamard necessity, ultrastatic slab]
12. V. Balakumar et al., *Superradiance and quantum states on Kerr*, arXiv:2303.13488. [superradiance obstruction to standard vacua]
13. D. Häfner and C. K. M. Klein, *The Unruh state for bosonic Teukolsky fields on subextreme Kerr spacetimes*, arXiv:2602.09796.
14. M. Dafermos and I. Rodnianski et al., *Boundedness of the Teukolsky equation on Kerr*, arXiv:2007.07211.
15. M. Bañados, C. Teitelboim and J. Zanelli; rotating BTZ metric, horizons and ergoregion ($r_+<r<\ell\sqrt M$), cross-checked against arXiv:gr-qc/0003097 and arXiv:1707.08133.

*Equatorial Kerr metric components ($g_{tt}=-(1-2M/r)$, $g_{t\varphi}=-2Ma/r$, $g_{\varphi\varphi}=r^2+a^2+2Ma^2/r$, $r_+=M+\sqrt{M^2-a^2}$, $r_{\rm erg}=2M$ on the equator) were cross-checked against the standard Kerr-metric literature; the identity $\det h=-\Delta$ was verified symbolically.*

---

*Internal source records:* `core-data/calculations/sj-rotating-btz/` (VYPOCET-05), `core-data/calculations/sj-kerr-equatorial/` (VYPOCET-08), and `core-data/calculations/sj-eigenvector-superradiance/` (VYPOCET-10, §3.5b mechanism + eigenvector/superradiance localization); hypothesis `knowledge-base/hypotezy/H02-sj-kerr.md`.
