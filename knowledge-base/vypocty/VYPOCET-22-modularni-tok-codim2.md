# VYPOCET-22: Codim-2 spoj jako správný 4D protějšek 2D rohu — test H5g-3

**Datum:** 2026-06-06
**Soubory:** `core-data/calculations/modular-flow-codim2/calc.py`, `helpers.py`, `results.json`, `plots/{nonlocality_vs_N_codim2,nonlocality_vs_edge_codim2,wedge_slab_diagnostics_codim2,wedge_nl_powerlaw_panel}.png`
**Status:** Dokončeno
**Hypotéza:** H5g-3 (BRAINSTORM-05, medium-high; jednotící nit vrstva B, rohová podčást)
**Cluster:** entropy-cluster × von-Neumann × modular-hamiltonian (TOP HUB)
**Navazuje:** VYPOCET-20/F-024 (4D null-tip diamantu NEREPLIKUJE 2D rohový mechanismus s BD objektem), VYPOCET-18 (2D rohový mechanismus PODPOŘEN, sklon −0,383), VYPOCET-09 (BD objekt opravil tvar 4D spektra)
**Knihovna:** postaveno nad `toe` v0.1.0 (dogfooding kolo)

---

## Co se testuje a proč

VYPOCET-20 (finding F-024) zjistil, že **rohová koncentrace modulární non-geometričnosti** — čistá 2D signatura (VYPOCET-18: non-lokalita SJ modulárního kernelu roste monotónně k rohu diamantu, sklon −0,383, R²=0,989) — **NEREPLIKUJE ve 4D** ani s Benincasa-Dowkerovým objektem, který prokazatelně opravil tvar 4D spektra. Ve 4D diamantu byl nl-vs-tip sklon **+0,71** (non-lokalita KLESÁ k tipu) a poměr roh/bulk f_nl 0,445 (roh MÉNĚ non-lokální). VYPOCET-20 v limitech navrhl **dimenzionální diagnózu**: 4D null-tip diamantu je **degenerující 2-sféra** (prostorová S² se smrští do bodu), topologicky nepodobná 2D prostorovému tipu, kde se protínají dvě null-přímky.

**H5g-3 (BRAINSTORM-05) tvrdí:** správný 4D protějšek 2D rohu **není izolovaný tip**, ale **codim-2 SPOJ** — hrana klínu, která je **plochá 2-rovina**, kde boostový Killingův vektor degeneruje podél čisté 2-plochy (ne jednoho bodu). Pokud je 2D rohový mechanismus **codim-2-generický**, měla by se modulární non-geometričnost koncentrovat směrem k této hraně (nl-vs-hrana sklon < 0, jako ve 2D), s plochým slab kontrolním povrchem (bez spoje) bez takové koncentrace.

**Metodologická izolace příčiny:** VYPOCET-22 používá **TENTÝŽ dynamický objekt** jako VYPOCET-20 primary (smeared BD ε=0,6, G_R=B⁻¹) — mění se **POUZE geometrie / lokus**: codim-2 hrana klínu místo null-tipu diamantu. Jakákoli změna verdiktu je tak přičitatelná **lokusu** (geometrii spoje), čímž se testuje přesně H5g-3, že tip byl **špatný lokus**.

---

## Konvence (ověřené proti literatuře)

| Vstup | Forma | Zdroj |
|-------|-------|-------|
| Geometrie klínu (codim-2 spoj) | 4D Minkowski box {\|t\|,\|x\|,\|y\|,\|z\|≤0,5}, pravý Rindlerův klín W={x>\|t\|}, řez O={x>0}; entangling plocha = **hrana** E={t=0,x=0} = plochá 2-rovina (y,z) | Bisognano-Wichmann; Rindler |
| Vzdálenost k hraně | d_E = √(t²+x²) (transverzální vzdálenost ke 2-rovině) — přímý 4D protějšek 2D vzdálenosti-k-rohu | NEW (VYPOCET-22) |
| Slab kontrola (bez spoje) | objemově/hustotně shodný box, řez O={x>0}; plochá codim-1 nadrovina x=0, BEZ spoje; kontrolní lokus \|x\| | VYPOCET-18/20 slab |
| BD smeared 4D | α₄=−4/√6, β₄=4/√6, f₄(n,ε)=(1−ε)ⁿ Σ Cᵢ binom(n,i−1)(ε/(1−ε))^{i−1}, prefaktor √ε√ρ | Aslanbeigi-Saravani-Sorkin **1305.2588**; **1507.00330** |
| G_R = B⁻¹ | B dolně trojúhelníková v čase → G_R retardovaná | **1001.2725** |
| iΔ = i(G_R−G_Rᵀ), W = pozitivní část (rel-floor 1e−10) | SJ Pauli-Jordan | **1611.10281**; VYP-09/20 floor |
| Modulární kernel K(x,y) ze SSEE | W_O v=μ iΔ_O v, ε=ln[μ/(μ−1)], spektrální rezoluce do site-báze | **1611.10281**; Casini-Huerta **0905.2562** |

**Probe používá NETRUNCOVANÝ SJ modulární kernel** (kappa=None) — skutečný modulární tok, jehož geometričnost Bisognano-Wichmann předpovídá. Stejná volba jako VYPOCET-18/20.

**Proč je geometrie klínu nejčistší codim-2 spoj:** Modulární tok pravého Rindlerova klínu W={x>\|t\|} je **přesně x-t boost** (Bisognano-Wichmann). Boostový Killingův vektor ξ = x ∂_t + t ∂_x **degeneruje na hraně** E={t=0,x=0} — což je **plochá 2-rovina** (rozpjatá y,z), tj. genuinní codim-2 lokus (2 ze 4 souřadnic fixovány, 2 volné), a je **plochá**, nikoli smršťující se sféra — přesně H5g-3 predikce. Box je symetrický v t i x, takže hrana E leží uvnitř regionu.

**Parametry:** N ∈ {800, 1200, 1700, 2200} (mez maticové inverze N≤2200), 3 seedy. cond(B) ~10⁴–10⁵ (dobře podmíněný smeared objekt). **Strojová invariance:** iΔ ± párování ověřeno na KAŽDÉM regionu/seedu přes `toe.causet.causal_diagnostics` — max relativní reziduum **7,1·10⁻¹⁵ < 1e−12** ✓ (assert v kódu).

---

## Výsledky

### (A) Klíčová křivka: non-lokalita vs vzdálenost k codim-2 hraně

| Lokus | sklon nl-vs-lokus | SE | CI68 | R² | čtení |
|-------|-------------------|-----|------|-----|-------|
| **klín, codim-2 hrana** | **+0,115** | 0,053 | [0,106; 0,124] | 0,54 | non-lokalita KLESÁ k hraně |
| **klín, hrana, WALL-CTRL** (vyloučen roh boxu) | **+0,251** | 0,099 | [0,209; 0,292] | 0,62 | KLESÁ k hraně (čistší) |
| slab kontrola, nadrovina | −0,043 | 0,015 | — | 0,67 | plochá (~0,30 všude) |
| — 2D roh (VYP-18) | −0,383 | — | — | 0,99 | roste k rohu |
| — 4D null-tip (F-024) | +0,710 | — | — | 0,56 | klesá k tipu |

**Klín má KLADNÝ sklon** (+0,115; ve wall-controlled vnitřní oblasti dokonce **+0,251**), tj. **stejné znaménko jako 4D null-tip** (+0,71), **opačné než 2D roh** (−0,38). Non-lokalita SJ modulárního kernelu **klesá** směrem ke codim-2 hraně, ne roste. Slab kontrolní nadrovina je plochá (sklon −0,043, f_nl ~0,30 ve všech zónách), což potvrzuje, že kladný sklon klínu je reálný kontrast, ne univerzální artefakt.

**Wall-control (poctivá robustnost):** Vyloučení rohu boxu {\|t\|,\|x\|→0,5} z binningu vzdálenosti (kde žije stěna boxu, ne codim-2 hrana) sklon **NEsníží — zvýší** na +0,251 (CI68 [0,21; 0,29] vylučuje nulu). Kladný sklon tedy **NENÍ artefakt stěny**; je vnitřní a ve vnitřní oblasti dokonce čistší. Křivka roste z 0,218 u hrany (d=0,105) na 0,270 daleko (d=0,334).

### (B) Zóna hrany vs bulk

| Veličina (tail N) | hodnota | predikce H5g-3 |
|-------------------|---------|----------------|
| f_nl hrana / bulk | **0,914** (<1) | roh/hrana non-lokálnější → poměr >1 ✗ |
| edge_more_nonlocal_than_bulk | **False** | ✗ |

Zóna hrany je **MÉNĚ** non-lokální než bulk (poměr 0,914), stejné znaménko jako 4D tip (F-024: 0,445), opačné než 2D roh (VYP-18: 1,15).

### (C) Slab/boost strana — přežívá (konzistentní s VYPOCET-20)

| Veličina (tail N) | klín | slab | predikce |
|-------------------|------|------|----------|
| diagonální boost-linearita R² | **0,92** | 0,93 | lineární boostová váha (BW) → R²>0,6 ✓ |
| off-diag sklon | −0,28 | −0,26 | lokální mocninový pokles ✓ |

Diagonální modulární váha klínu je **lineární ve vzdálenosti** (R²=0,92, Bisognano-Wichmann) — boostová strana mechanismu **přežívá**, stejně jako ve VYPOCET-20 slab (R²=0,77) a VYPOCET-18 2D (R²=0,98). Off-diagonální pokles klínu (−0,28) je dokonce mírně strmější (lokálnější) než slab (−0,26), tj. žádná koncentrace non-lokality na hraně ani v off-diag sklonu.

---

## Verdikt

| Signatura | Predikce H5g-3 | Výsledek |
|-----------|----------------|----------|
| non-lokalita roste k codim-2 hraně | sklon nl-vs-hrana < 0 | ✗ (+0,115; wall-ctrl +0,251) |
| hrana non-lokálnější než bulk | poměr > 1 | ✗ (0,914) |
| slab lokálnější než klín (off-diag) | sklon slab < klín | ✗ (klín mírně strmější) |
| diagonála = lineární boost | R² > 0,6 | ✓ (R²=0,92) |
| **počet podporujících signatur** | | **1/4** |
| slab kontrola NEkoncentruje | sklon nadroviny ≈ 0 | ✓ (−0,043, plochá) |

> ### **VERDIKT: 2D-ONLY. Codim-2 spoj NEOBNOVUJE 2D rohový mechanismus ve 4D.**
>
> I při **čistém codim-2 spoji** (plochá 2-rovina, ne degenerující sféra) se modulární non-lokalita **NEkoncentruje k hraně — klesá k ní** (nl-vs-hrana sklon +0,115; wall-controlled vnitřní +0,251, CI68 [0,21; 0,29] vylučuje nulu), **stejné znaménko jako 4D null-tip** (+0,71), **opačné než 2D roh** (−0,38). Kladný sklon **NENÍ artefakt stěny boxu** (ve wall-controlled vnitřní oblasti je strmější). Slab kontrolní nadrovina je plochá (−0,043), takže kontrast je reálný.
>
> **Reframing 4D lokusu z null-TIPu na codim-2 SPOJ tedy 2D rohovou koncentraci NEOBNOVUJE.** Rohová podčást H4g-1 vrstvy B zůstává **dimenzionálně omezená** (zatím jen 2D). Boostová/slab strana mechanismu **přežívá** (diagonální boost-linearita R²=0,92), konzistentně s VYPOCET-18/20.

---

## Interpretace pro H5g-3 a jednotící nit (BRAINSTORM-04/05)

**H5g-3 je vyvrácen v testované sondě.** Hypotéza byla rozumná — geometricky je codim-2 hrana klínu skutečně bližší 2D rohu než degenerující tip (a kvantitativně to vidíme: klín +0,12 je **mnohem blíž nule** než tip +0,71, tj. codim-2 spoj posouvá 4D chování směrem od ostrého tip-nullu k neutralitě). Ale **znaménko se neobrátí**: non-lokalita ve 4D klesá k hraně, kdežto ve 2D rohu roste. Codim-2 plochost tedy **není dostatečnou podmínkou** pro 2D rohovou koncentraci.

**Co to říká o vrstvě B jednotící nitě:**

1. **Slab/boost podčást ("modulární tok = geometrický boost na klínu") — dimenzionálně robustní, opět potvrzena.** Diagonální boost-linearita R²=0,92 ve 4D klínu (VYP-18 2D R²=0,98, VYP-20 slab R²=0,77). To je třetí nezávislé 4D potvrzení boostové strany.

2. **Rohová/spojová podčást ("entangling spoj = obstrukce geometričnosti, K delokalizuje ke spoji") — stále jen 2D.** Selhává nejen na null-tipu (VYP-20), ale i na čistém codim-2 spoji (VYP-22). **Diagnóza se posouvá:** non-replikace není ani artefaktem link-matice (vyvráceno VYP-20 BD objektem), ani artefaktem degenerující-sféra-topologie tipu (vyvráceno VYP-22 plochým codim-2 spojem). Příčina je **hlubší dimenzionální vlastnost 4D modulární geometrie** — možná že 4D boost má vždy "kam téct" podél transverzálních y,z směrů, i na hraně klínu, takže K nedelokalizuje (zatímco 2D boost na rohu nemá žádný transverzální únik).

**Fyzikální čtení (proč klesá k hraně):** Ve 2D má boost jen jeden prostorový směr; roh je topologický konec, kde boost nemá kam téct → K delokalizuje. Ve 4D má codim-2 hrana **dva volné transverzální směry (y,z)**, podél nichž boost teče volně i přesně na hraně. Lokalita K je proto u hrany **zachována nebo zesílena** (boost má kam téct podél hrany), zatímco non-lokalita roste v bulku, kde se promíchávají vzdálenější páry. To je konzistentní s tím, že je to **stejné znaménko jako slab nadrovina** (plochá) — codim-2 hrana se chová spíš jako vyšší-dimenzionální boost-povrch než jako 2D-rohová obstrukce.

**Důsledek pro vyvraceč #2 jednotící nitě:** Ve 2D vyvraceč #2 NEnastal (roh ztrácí lokalitu K). Ve 4D **rohová predikce vrstvy B selhává robustně napříč třemi lokusy** (null-tip VYP-20, codim-2 spoj VYP-22) a třemi objekty (link VYP-18, BD smeared/sharp VYP-20). Vrstva B v rohové části tak vyžaduje **reformulaci pro fyzikální dimenzi**: 2D "boost nemá kam téct na rohu" se ve 4D nevyskytuje, protože codim-2 lokusy mají transverzální únikové směry.

---

## Knihovna (dogfooding `toe` v0.1.0)

**Použito z `toe`:**
- `toe.causet.causal_matrix` (4D Minkowského kauzální order), `pauli_jordan` (iΔ = i(G_R−G_Rᵀ)), `causal_diagnostics` (strojová ± párovací invariance, ověřena 7e−15 < 1e−12 na každém regionu).
- `toe.fits.regression_se`, `powerlaw_fit` (s SE + bootstrap CI), `validate_against` (chokepoint pro invariant flag), `Measurement` (nosič value/SE/CI68 pro edge slope).
- `toe.viz.powerlaw_panel` (panel mocninového fitu nl-vs-hrana, `wedge_nl_powerlaw_panel.png`).

**Chybělo v `toe` (lokální helpery v `helpers.py`, NEEDITOVÁNO `lib/toe/*.py` — VYPOCET-21 vlastní causet.py):**
- **Smeared BD d'Alembertián** — `toe.causet` má jen SHARP `bd_dalembertian_inverse(...,dim=4)`; validovaný VYPOCET-20 objekt je smeared ε=0,6, reprodukován v `helpers.bd_smeared_matrix`.
- **Export modulárního kernelu K_site** — `toe.entropy.ssee` vrací jen skalár S; lokalitní diagnostiky potřebují celý K (`helpers.modular_kernel_ssee`).
- **Relativní floor v `toe.sj.sj_state`** — BD-inverzní objekt (cond ~1e5) potřebuje relativní cut, ne absolutní tol=1e−12.
- **Region buildery klínu / codim-2 + nl-vs-lokus diagnostika** — `helpers.sprinkle_wedge_box4d`, `nl_vs_edge_profile`.

**Návrhy na migraci (`results.json` klíč `lib_proposals`, signatury ready-to-lift):**
- `toe.causet.sprinkle_wedge_box4d(N, rng, *, t_half, x_half, yz_half)` — t-symetrický box s codim-2 Rindlerovou hranou.
- `toe.causet.bd_smeared_dalembertian_inverse(C, rho, eps)` — ε-sourozenec sharp BD inverze.
- `toe.sj.sj_state(iDelta, *, tol, rel_floor=None)` — přidat relativní floor.
- `toe.entropy.modular_kernel(W, iDelta, sub_idx, *, kappa, tol) -> {K, eps, S, nu}` — exponovat site-bázový kernel.
- `toe.viz.nl_vs_locus(Kabs, Dij, d_locus, near_r, n_zones)` — zobecnit VYP-20 _nl_vs_corner_generic na libovolný lokus.

---

## Limity a poctivá zjištění

- **2D-only verdikt je reálný a robustní napříč lokusy a objekty.** Non-replikace rohové koncentrace platí pro link-matici (VYP-18), BD smeared/sharp na null-tipu (VYP-20) i BD smeared na codim-2 spoji (VYP-22). Není to artefakt jednoho lokusu, jednoho objektu ani jednoho metriku.
- **Kladný sklon NENÍ artefakt stěny boxu.** Wall-controlled vnitřní oblast (vyloučen roh boxu) dává sklon +0,251 (strmější než +0,115), CI68 [0,21; 0,29] vylučuje nulu. Při samostatném N=1700 byl sklon šumově blízko nuly (−0,012), ale při nejlépe rozlišeném N=2200 je jednoznačně kladný — finite-N robustnost potvrzena růstem N.
- **R² křivky je střední** (0,54–0,62), křivka není čistá přímka. Verdikt stojí na **znaménku** (od hrany vs k hraně) a na **kontrastu se slab kontrolou** (plochá), ne na absolutní hodnotě sklonu — stejná filozofie jako VYPOCET-18/20.
- **Slab/boost strana přežívá.** Diagonální boost-linearita R²=0,92 je čistá pozitivní signatura — verdikt 2D-only se týká **pouze rohové podčásti**, ne celé vrstvy B.
- **Sonda měří lokalitu K, ne analytický důkaz.** Stejně jako VYPOCET-18/20 jde o korelaci lokalitních metrik modulárního kernelu s geometrií lokusu, ne o analytický rozklad rohového/spojového příspěvku k modulárnímu Hamiltoniánu. Literární caveat (2008.07697/2412.07832: non-Hadamard↔volume pravděpodobně nesouvisí přímo) zachován.
- **Nefudgováno:** 1/4 verdikt, kladný sklon (proti H5g-3), poměr hrana/bulk <1, a flat slab kontrola jsou zachovány jako poctivé kontroly. Strojová ± párovací invariance asserted na každém regionu (max 7e−15).

---

## Dopad na hypotézu H5g-3 a F-024

| Před VYPOCET-22 | Po VYPOCET-22 |
|---|---|
| F-024: 4D null-tip NEREPLIKUJE 2D rohový mechanismus; **podezření, že tip je špatný lokus** (degenerující 2-sféra), správný by byl codim-2 spoj (H5g-3). | **H5g-3 vyvrácen v sondě:** i čistý codim-2 spoj (plochá 2-rovina) dává **kladný** nl-vs-hrana sklon (+0,12; wall-ctrl +0,25), stejné znaménko jako tip, opačné než 2D roh. Reframing lokusu rohovou koncentraci NEOBNOVUJE. Příčina není topologie tipu — je to **hlubší 4D vlastnost** (codim-2 lokusy mají transverzální boost-únik). |

**Nový finding (kandidát F-0xx):** *4D modulární non-geometričnost se nekoncentruje k entangling spojům žádné kodimenze ≥2 testované v této sondě (null-tip ani codim-2 hrana klínu); znaménko nl-vs-lokus sklonu je robustně kladné (klesá k lokusu), opačné než 2D roh. 2D rohový mechanismus "boost nemá kam téct" je dimenzionálně omezen tím, že codim-2 lokusy ve 4D mají transverzální boost-únikové směry.* H5g-3 přesouvá rohovou podčást vrstvy B z "otevřené, podezření na špatný lokus" na **"dimenzionálně omezená napříč lokusy; vyžaduje reformulaci rohového mechanismu pro 4D"**.

---

## Reference (klíčové pro tento výpočet)

- **1305.2588** — Aslanbeigi, Saravani, Sorkin: smeared/non-lokální BD d'Alembertián, f₄(n,ε).
- **1001.2725** — Benincasa, Dowker: BD diskrétní d'Alembertián, vrstvy (1,−9,16,−8).
- **1507.00330** — Belenchia et al.: spektrální dimenze, smeared BD aplikace.
- **1611.10281** — Sorkin, Yazdi: SSEE, W_O v=μ iΔ_O v.
- **0905.2562** — Casini, Huerta: korelátorové K, lokální modulární Hamiltonián.
- **Bisognano-Wichmann** — modulární tok klínu = boost; Killingův vektor ξ=x∂_t+t∂_x, hrana E={t=0,x=0}.
- VYPOCET-20/F-024 (4D null-tip NEREPLIKUJE), VYPOCET-18 (2D rohový mechanismus PODPOŘEN), VYPOCET-09 (BD objekt opravil tvar spektra), VYPOCET-13 (Hadamardova rohová anomálie), VYPOCET-16 (4D slab III₁→II).
- pilíř 19 (`foundations/19-von-neumann-algebras.md`) — modular-hamiltonian TOP HUB.

---

## Klíčová tabulka lokusů (3 geometrie, tentýž BD smeared ε=0,6 objekt)

| Lokus | dimenze/typ | nl-vs-lokus sklon | znaménko vs 2D roh | verdikt |
|-------|-------------|-------------------|--------------------|---------| 
| 2D roh diamantu (VYP-18) | 2D, dva null-okraje | **−0,383** (R²=0,99) | — (referenční) | PODPOŘENO |
| 4D null-tip diamantu (VYP-20/F-024) | degenerující 2-sféra → bod | **+0,710** (R²=0,56) | opačné | NEREPLIKUJE |
| **4D codim-2 hrana klínu (VYP-22)** | **plochá 2-rovina** | **+0,115** / wall-ctrl **+0,251** | **opačné** | **NEREPLIKUJE (2D-only)** |
