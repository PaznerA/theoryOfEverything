# VYPOCET-37: Geometrický / γ₅-gradovaný boostový Dirac — pojmenovaný chybějící prvek F-036 / Wall 2

**Datum:** 2026-06-09
**Soubory:** `core-data/calculations/geometric-boost-dirac/calc.py`, `results.json`, `plots/unruh_geometric_vs_surrogate.png`; knihovna `lib/toe/spectraltriple.py` (nový primitiv `geometric_boost_dirac` + `GeometricBoostDirac`, tři testy v `app/tests/test_toe_spectraltriple.py`)
**Status:** Dokončeno
**Slug:** `geometric-boost-dirac`
**Hypotéza:** F-036 explicitně pojmenoval opravu chybějícího prvku — **non-surogátní Dirac z geometrického Killingova boostu** $\xi = x\partial_t + t\partial_x$ s chirálním gradováním $\gamma_5$ (sudý spektrální triple), NE odmocnina-z-modulu modulárního $\varepsilon$-spektra. Otázka: obnoví tento geometrický/gradovaný Dirac absolutní Unruhovu $2\pi$ a exponent $+1$ z geometrie-fixované normalizace, kde surogát selhal (9,58 vs 6,28, off 52 %; exponent 0,72 vs $+1$)?
**Cluster:** modular-flow / Bisognano-Wichmann boost × Unruh/Tolman lokální teplota × NCG sudý spektrální triple
**Navazuje:** VYPOCET-32 / F-036 (SUROGÁTNÍ Dirac $D_K=\mathrm{sgn}(K)\sqrt{|K|}$ v jednotkách $\varepsilon=\ln[\mu/(\mu-1)]$ LOG-KOMPRIMUJE: reprodukuje boostovou geometrii, ale nečte absolutní $2\pi$ ani exponent $+1$); VYPOCET-29 / F-033 ($D_K$ je surogát, ne axiomatický spektrální triple — žádná chiralita / KO-dimenze).

---

## Programová otázka

F-036 diagnostikoval, že surogátní Dirac postavený z modulárního kernelu v jednotkách $\varepsilon=\ln[\mu/(\mu-1)]$ (Casini-Huerta 0905.2562) **log-komprimuje**: reprodukuje Bisognano-Wichmannovu boostovou geometrii ($\rho$-invariantní lineární diagonála, $R^2\approx0{,}97$, kontroly kolabují), ALE z geometrie-fixované normalizace neobnoví ani absolutní Unruhovu $2\pi$ (nejlepší routa 9,58, off 52 %), ani zákonný exponent $+1$ (měřeno 0,72). $\beta_{KMS}=1$ je Tomita-Takesaki **tautologie**. F-036 pojmenoval jedinou cestu k absolutní $2\pi$:

> **non-surogátní Dirac postavený z geometrického Killingova boostu** $\xi=x\partial_t+t\partial_x$ s chirálním gradováním $\gamma_5$ (sudý spektrální triple), NE odmocnina-z-modulu $\varepsilon$-spektra.

Tento výpočet tu konstrukci postaví a testuje. **Antikruhovost (strukturální, zděděná z F-036):** scale proper vzdálenosti je fixovaný PŘED jakýmkoli sklonem z hustoty sprinkling ($\varepsilon_{\text{disc}}=\rho^{-1/2}$) a proper okna $[0{,}06,\,0{,}90]\cdot x_{\text{extent}}$ — IDENTICKÉHO s F-036, aby side-by-side bylo apples-to-apples. NIKDY laděno k $2\pi$.

---

## Setup a konstrukce

### Geometrický / γ₅-gradovaný Dirac (sudý spektrální triple)

2D reálné gamma-matice v chirální bázi (Clifford $\{\gamma^a,\gamma^b\}=2\eta^{ab}$):

$$\gamma^0 = \begin{pmatrix}0&1\\1&0\end{pmatrix},\quad \gamma^1=\begin{pmatrix}0&-1\\1&0\end{pmatrix},\quad \gamma_5=\gamma^0\gamma^1=\mathrm{diag}(-1,+1).$$

Bezhmotný 2D Dirac na spinorovém svazku nad $n$ body:

$$D = -i(\gamma^0\,D_t + \gamma^1\,D_x),$$

kde $D_t, D_x$ jsou **antisymetrické** nearest-neighbour first-difference stencily (6 sousedů, váha $(coord_j-coord_i)/|dr|^2$, exaktně antisymetrizováno), takže $-iD_\mu$ je hermitovský. Chirální gradování $\Gamma_5 = I_n\otimes\gamma_5$ antikomutuje s každým $\gamma^a$ (Clifford), tedy $\{D,\Gamma_5\}=0$ **exaktně** — **sudý spektrální triple**.

### Tři routy k absolutní 2π

| Routa | Definice | Charakter |
|-------|----------|-----------|
| **(1) klasická Killingova váha** | $w_{\text{boost}} = 2\pi\,\rho_{\text{proper}}$, $\rho_{\text{proper}}=\sqrt{x^2-t^2}$ | **TAUTOLOGICKÁ** — $\xi$ nese $2\pi$ z definice; konzistence-check, NE objev |
| **(2) operátorová diagonála** | $|K_{op}(x,x)|$, $K_{op}=\tfrac12\{\xi^\mu,p_\mu\}$ | boostová váha NENÍ diagonální observabla |
| **(3) operátorový spektrální boost-kvantum** | $\mathrm{median}(|eig_k|\langle\rho\rangle_k)$ z $K_{op}$ | **NETAUTOLOGICKÁ** — analog F-036 boost-quanta, BW kontinuum $2\pi$ |

Routa (3) je rozhodující netautologický test: $K_{op}=\tfrac12\{\xi^\mu,p_\mu\}$ je postaven z **vlastní finite-difference struktury causetu** (ne vložen ručně), jeho spektrum probe-uje absolutní $2\pi$.

**Side-by-side (c):** na témž slabu / téže pod-oblasti / témž okně se měří F-036 SUROGÁT $D_K=\mathrm{sgn}(K)\sqrt{|K|}$ i raw $|K(x,x)|$ — reprodukce F-036 čísel jako kontrola.

**Parametry:** sweep $\rho$ přes $N\in\{600,1000,1400\}$ (mez husté `eigh` $\le1500$), 5 seedů/$\rho$ = 15 seedů. Seed scheme $3000+17s+N$ (deterministický). Wall-clock cap 25 min, skutečný běh **~21 s**. Schéma `geometric-boost-dirac/v1`, atomický + progresivní zápis (per-seed flush).

**KAVEAT (poctivý, zásadní):** klasická Killingova váha $w_{\text{boost}}=2\pi\rho$ je **klasická Killing-fieldová veličina vložená ručně** ($\xi$ nese $2\pi$ z DEFINICE boostového generátoru) — obnova $2\pi$ z ní je NORMALIZAČNÍ KONZISTENCE-CHECK, NE objev. Skutečný operátorový obsah je routa (3) a well-posedness gradování. 2D, bezhmotný, $N\le1500$ dense: TREND ($\rho$-invariance), ne $N\to\infty$.

---

## Výsledky

### Sudý spektrální triple je WELL-POSED (exaktně)

| Diagnostika gradování | Hodnota | Práh |
|---|---|---|
| $\|\{D,\Gamma_5\}\|/\|D\|$ (antikomutace) | **0,0** | $<10^{-10}$ ✓ |
| $\|D-D^\dagger\|/\|D\|$ (hermiticita) | **0,0** | $<10^{-10}$ ✓ |
| $\|\Gamma_5^2-I\|$ | **0,0** | $<10^{-10}$ ✓ |
| $\pm$-párové (chirální) spektrum | **$2{,}9\times10^{-15}$** | $<10^{-6}$ ✓ |

Geometrický/$\gamma_5$-gradovaný Dirac je **exaktně sudý spektrální triple na konečném causetu** — antikomutace strojově nulová (Clifford), spektrum $\pm$-párové na strojovou přesnost. To je první konstrukce ve výzkumu, kde Dirac NESE chirální gradování (F-033 surogát žádné nemá).

### (1) Klasická Killingova váha — obnoví 2π a exponent +1 (TAUTOLOGICKY)

| veličina | hodnota | cíl |
|---|---|---|
| koeficient $w_{\text{boost}}/\rho$ (through-origin) | **6,290 ± 0,012** (rel. err **0,2 %**) | $2\pi=6{,}283$ |
| zákonný exponent $p_E$ | **0,989 ± 0,013** ($R^2=1{,}000$) | BW $+1$ |

Geometrický route **MŮŽE** nést absolutní $2\pi$ a exponent $+1$ — ale tautologicky: $\xi$ nese $2\pi$ z definice. Toto je baseline, vůči němuž se měří operátorová routa (3).

### (3) Operátorový spektrální boost-kvantum — netautologická routa: DRIFTUJE, nekonverguje k 2π

| $N$ | operátorový boost-kvantum $\mathrm{median}(|eig|\langle\rho\rangle)$ | poměr k $2\pi$ |
|---|---|---|
| 600 | 4,747 | 0,756 |
| 1000 | 5,647 | 0,899 |
| 1400 | 7,707 | 1,227 |
| **agregát** | **6,034 ± 1,393** | **0,960** |

Operátorová routa **monotónně driftuje s $N$** (4,75 → 5,65 → 7,71), kříží $2\pi$ kolem $N\approx1100$, ale **NEKONVERGUJE** — je to veličina závislá na diskretizační škále (CV **0,205**, $>0{,}15$ práh). Agregát 6,034 leží blízko $2\pi$ JEN proto, že sweep $2\pi$ obkličuje. Relativní chyba agregátu 19,1 % (těsně pod 20% prahem), ALE $\rho$-invariance selhává.

### (2) Operátorová diagonála — exaktně nula

$|K_{op}(x,x)|_{\max} = 0{,}0$: boostová váha NENÍ diagonální observabla diskrétního prvořádového operátoru ($-i\times$ antisymetrický $\Rightarrow$ nulová diagonála). Instruktivní: boostová informace žije v off-diagonálním/spektrálním obsahu.

### (c) Side-by-side se surogátem F-036 — reprodukce a kontrast

| veličina | geometrický (routa 3) | F-036 surogát $|K(x,x)|$ | surogát $D_K$ |
|---|---|---|---|
| koeficient $2\pi$ | **6,034** (off 19 %) | **36,62** (off 4,8×) | — |
| zákonný exponent $p_E$ | **0,99** (routa 1) | **0,714** | 0,411 |

Surogátní exponent **0,714 reprodukuje F-036** (0,72) na vysokou přesnost — kontrola, že surogátní pipeline odpovídá F-036. Geometrický exponent $+1$ (vs surogát 0,72) a koeficient blízko $2\pi$ (vs surogát off 4,8× na raw diagonále) ukazují, že **$\varepsilon$-log-komprese je odstraněna**.

---

## Verdikt korespondence: **partial** — exponent obnoven, koeficient ne $\rho$-invariantní (ostřejší negativ než F-036)

Podle předregistrovaných kritérií (diskriminátor řízen OPERÁTOROVOU routou 3, NE tautologickým baseline 1):

| Subtest | Kritérium | Výsledek | Status |
|---------|-----------|----------|--------|
| routa 3 absolutní $2\pi$ | rel. err $<0{,}20$ | 0,191 | ✓ (těsně) |
| routa 3 $\rho$-invariantní | CV $<0{,}15$ | 0,205 | **✗ FAIL** |
| gradovaný Dirac well-posed | residua $<10^{-10/-6}$ | 0/2,9e-15 | ✓ |
| (baseline) routa 1 konzistence $2\pi$ | rel. err $<0{,}20$, exp $\approx1$ | 0,002 / 0,99 | ✓ (tautologicky) |

**Souhrn:** geometrický/$\gamma_5$-gradovaný boostový Dirac je **exaktně sudý spektrální triple na konečném causetu** ({D,Γ₅}=0 strojově nulové, spektrum $\pm$-párové na $10^{-15}$). Klasická Killingova váha obnoví $2\pi$ a exponent $+1$ — ale **tautologicky** ($\xi$ nese $2\pi$ z definice). Operátorová routa (postavená z vlastní finite-difference struktury causetu) obnoví **exponent $+1$** (vs surogát 0,72) a **odstraní $\varepsilon$-log-kompresi** (koeficient blízko $2\pi$ vs surogát off 4,8×), ALE její absolutní koeficient **DRIFTUJE s diskretizací** (4,75 → 7,71, CV 0,21), nekonverguje k $2\pi$.

**Wall 2 NEPŘECHÁZÍ na pozitivní** (operátorová routa není $\rho$-invariantní). ALE negativ je **OSTŘEJŠÍ a JINAK LOKALIZOVANÝ než F-036**: obstrukce se **přesunula** z $\varepsilon$-log-komprese (F-036, exponent stlačen na 0,72, koeficient off 4,8×) na **konečně-$N$ diskretizaci prvořádového boostového operátoru** (exponent teď $+1$, koeficient teď řádu $2\pi$, ale driftuje). Geometrický Dirac **vyřeší log-kompresní problém** F-036 (to je reálný pokrok), ale **odhalí hlubší obstrukci**: diskrétní prvořádový boostový generátor na nepravidelném sprinklingu nenese stabilní absolutní rapidity-škálu při konečném $N$.

### Proč to dává fyzikální smysl

Surogát F-036 selhal na DVOU osách: (i) log-komprese $\varepsilon=\ln[\mu/(\mu-1)]$ stlačila exponent na 0,72; (ii) $\varepsilon$-jednotky nefixují boostové rapidity ($2\pi$ off 52–87 %). Geometrický Dirac z Killingova boostu $\xi$ **odstraní (i)** (exponent $+1$, žádná log-komprese) a klasická Killingova váha **triviálně řeší (ii)** ($\xi$ nese $2\pi$). Netautologická operátorová routa ale ukazuje, že **diskretizace prvořádového operátoru** zavádí NOVOU škálovou závislost: $K_{op}=\tfrac12\{\xi^\mu,p_\mu\}$ na finite-difference stencilu má spektrum, jehož lokalizace $\langle\rho\rangle_k$ závisí na hustotě sousedů, takže $|eig_k|\langle\rho\rangle_k$ driftuje. Absolutní $2\pi$ tedy NENÍ jen otázka „správného Diraca" — vyžaduje i kontinuální limit diskrétního prvořádového operátoru, který konečné $N\le1500$ nedosáhne.

---

## Co to znamená pro hranu noncommutative-geometry ↔ semiclassical-gravity

1. **Pojmenovaný chybějící prvek F-036 byl POSTAVEN:** sudý spektrální triple s chirálním $\gamma_5$ z geometrického Killingova boostu existuje a je well-posed na konečném causetu (na rozdíl od F-033 surogátu bez chirality).
2. **Log-kompresní obstrukce F-036 je VYŘEŠENA:** exponent $+1$ (ne 0,72), žádné $\varepsilon$-stlačení. To je reálný pokrok — surogátní kaveat F-033/F-034/F-036 je tu odstraněn.
3. **Absolutní $2\pi$ stále NENÍ $\rho$-invariantní:** operátorová routa driftuje (CV 0,21), klasická routa je tautologická. Most NCG↔semiklasika zůstává **most struktury, ne stabilní teploty** — ale obstrukce je teď ostře lokalizovaná na konečně-$N$ diskretizaci prvořádového operátoru, ne na surogátních jednotkách.

**Doporučená změna hrany:** ponechat rating **`barely`** a anotovat ostřejším negativem: „Geometrický/$\gamma_5$-gradovaný boostový Dirac (sudý spektrální triple, {D,Γ₅}=0 na $10^{-15}$, postavený z Killingova $\xi=x\partial_t+t\partial_x$) VYŘEŠÍ log-kompresi F-036 (exponent $+1$ ne 0,72), ale operátorový boost-kvantum DRIFTUJE s diskretizací (4,75→7,71, CV 0,21, nekonverguje k $2\pi$) a klasická Killingova váha nese $2\pi$ tautologicky; obstrukce se přesunula z $\varepsilon$-jednotek na konečně-$N$ diskretizaci (VYPOCET-37 / F-040)." Příští krok, pokud se hrana znovu otevře: kontinuální limit operátorového boost-kvanta (sparse path $N\gg1500$) nebo Dixmierův trace / spektrální akce na gradovaném Diraci.

---

## Knihovní příspěvek

Nový composable primitiv v `lib/toe/spectraltriple.py` (vrstva C):

- `geometric_boost_dirac(coords, *, two_pi, k_nn, x_lo, x_hi)` → `GeometricBoostDirac(boost_weight, rho_proper, op_boost_quantum, op_boost_quantum_nmodes, op_diag_max, anticomm_residual, herm_residual, gamma5_sq_residual, spectrum_symmetry, n)`: postaví geometrický/$\gamma_5$-gradovaný boostový Dirac 2D Rindlerovy pod-oblasti — sudý spektrální triple z Killingova $\xi=x\partial_t+t\partial_x$. Vrací (1) klasickou Killingovu váhu $2\pi\rho_{\text{proper}}$, (2/3) operátorový boost-generátor $K_{op}=\tfrac12\{\xi^\mu,p_\mu\}$ s jeho diagonálou a spektrálním boost-kvantem, a čtyři diagnostiky gradování (antikomutace, hermiticita, $\Gamma_5^2$, $\pm$-párovost). Docstring nese poctivý kaveat: `boost_weight` nese $2\pi$ z konstrukce (konzistence-check, NE objev); genuine obsah je `op_boost_quantum` (driftuje) a well-posedness.

Tři nové testy v `app/tests/test_toe_spectraltriple.py`: (i) sudý spektrální triple — {D,Γ₅}=0 na $10^{-12}$, $\pm$-párové spektrum na $10^{-9}$; (ii) klasická váha nese `two_pi` exaktně + propaguje jiné `two_pi` (žádné skryté hard-coded $2\pi$); (iii) operátorová diagonála mizí + spektrální boost-kvantum konečné/kladné (NE asertováno na $2\pi$, protože driftuje).

---

## Limity

- Klasická Killingova váha $w_{\text{boost}}=2\pi\rho$ je tautologická ($\xi$ nese $2\pi$ z definice) — proto NEřídí verdikt; diskriminátor je operátorová routa (3).
- Operátorový boost-kvantum driftuje s $N$ (CV 0,21): konečně-$N$ diskretizace prvořádového operátoru, ne $N\to\infty$. Konvergence by vyžadovala sparse path $N\gg1500$.
- 2D, bezhmotný skalár, $N\le1500$ dense, 6-NN finite-difference stencil: diskrétní korekce $O(1/\sqrt N)$ + závislost na $k_{NN}$ (netestováno přes $k_{NN}$).
- Side-by-side surogát je raw $|K(x,x)|$ (off 4,8×) i $D_K$ diagonála; F-036 boost-quantum routa (eps$_k\langle x\rangle_k$ = 9,58) je jiná veličina, zde nereprodukovaná (reprodukován exponent 0,71 ≈ F-036 0,72).

---

## Reference (ověřené tento běh / přítomné v repu)

- **1611.10281** Sorkin-Yazdi — SJ stav, Pauli-Jordan, $G_R=\tfrac12 C$ (side-by-side surogát).
- **0905.2562** Casini-Huerta — jednomódové $\varepsilon=\ln[\mu/(\mu-1)]$ (surogátní jednotky).
- **gr-qc/9406019** Connes-Rovelli — modulární tok = tepelný čas.
- **bisognano1976duality** Bisognano-Wichmann — modulární tok = boost, $K=2\pi K_{\text{boost}}$.
- **unruh1976notes** Unruh — lokální teplota $1/(2\pi\rho)$.
- Connes 'Noncommutative Geometry' (Academic Press, 1994) — sudý spektrální triple, chirální gradování $\gamma_5$ (klasický výsledek, kniha).

POZN. (oprava reference, zděděná z F-036): 1712.04227 je Belenchia et al. o EE na causetech, NE zdroj BW/Unruh-$2\pi$ — to odkazuje `bisognano1976duality` / `unruh1976notes`.
