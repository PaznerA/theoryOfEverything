# VYPOCET-29: Spektrální triple vs SJ modulární tok — Diracův operátor jako most causal-sets ↔ noncommutative-geometry (H5g-4)

**Datum:** 2026-06-08
**Soubory:** `core-data/calculations/spectral-triple-modular/calc.py`, `results.json`, `plots/{spec_K_vs_D,connes_vs_causal}.png`; knihovna `lib/toe/spectraltriple.py` (+ test `app/tests/test_toe_spectraltriple.py`)
**Status:** Dokončeno
**Hypotéza:** H5g-4 (BRAINSTORM-05; hrana `causal-sets → noncommutative-geometry`, rating `barely`, PRIORITY HUNTING TARGET)
**Cluster:** modular-hamiltonian × spectral-triple × Dirac-operator
**Navazuje:** VYPOCET-18/20/22 (modulární kernel K(x,y) a jeho lokalitní/boostové diagnostiky), VYPOCET-11/17 (NCG spektrální akce — exact-rational větev)

---

## Programová otázka

Causal sets (linka A) a noncommutative geometry / spektrální triply (linka B) sdílejí v principu **jeden objekt — Diracův operátor $D$**, který kóduje současně dynamiku i metriku. Hrana mezi nimi v concept-grafu je ohodnocena `barely` a explicitně pojmenovává H5g-4:

> *„NCG spektrální data (Diracův operátor $D$ / spektrální triple, Connesova vzdálenostní formule) rekonstruuje stejný geometrický obsah jako Sorkin-Johnstonův modulární Hamiltonián $K=-\log\Delta$ z Pauli-Jordanova operátoru $i\Delta$. Konkrétní datová hrana by srovnala Connesovu vzdálenost vůči modulární vzdálenosti na nasypaném slabu. Zcela neprozkoumáno jako explicitní korespondence."*

Tento výpočet **instancuje** přesně tuto datovou hranu: vezme SJ jednočásticový **modulární Hamiltonián $K(x,y)$** Rindlerovsky řezaného 2D slabu (jehož modulární tok je Bisognano-Wichmannův **boost**), postaví kandidátní Diracův operátor $D_K=\mathrm{sgn}(K)\sqrt{|K|}$ a ptá se, zda konečný spektrální triple $(\mathcal{A}=\text{diagonální funkce},\ \mathcal{H}=\mathbb{C}^n,\ D=D_K)$ reprodukuje modulární strukturu.

---

## Setup (ověřené konvence)

| Vstup | Forma | Zdroj |
|-------|-------|-------|
| Geometrie | 2D slab $\{0<t<0{,}3,\ |x|<1\}$, $T\ll L$ (Rindler-like), `sprinkle_slab2d` | **1611.10281** |
| Kauzální řád | plochý 2D světelný kužel, `causal_matrix` | **1611.10281** |
| Greenova fce | $G_R=\tfrac12 C$ (2D bezhmotný), `green_retarded_2d` | **1611.10281** |
| Pauli-Jordan | $i\Delta=i(G_R-G_R^{\mathsf T})$, `pauli_jordan` | **1611.10281** |
| SJ stav | $W=$ pozitivní spektrální část $i\Delta$, `sj_state` | **1611.10281** |
| Řez | $O=\{x>0\}$ (Rindler half-line; modulární tok = boost) | Bisognano-Wichmann **1712.04227** (kontext **2008.07697**) |
| Modulární kernel | $K(x,y)$ ze SSEE $W_O v=\mu\,i\Delta_O v$, $\varepsilon=\ln[\mu/(\mu-1)]$, $\kappa=$None (netruncovaný) | Casini-Huerta **0905.2562**; `entropy.modular_kernel` |
| **Kandidátní Dirac** | $D_K=\mathrm{sgn}(K)\sqrt{|K|}$ (symetrický funkcionální kalkul; $D_K^2=|K|$) | **0905.2562** + tento výpočet |
| Connesova vzdálenost | $d_D(x,y)=\sup\{|a(x)-a(y)|:\|[D,a]\|_{\mathrm{op}}\le1\}$, $[D,a]_{ij}=D_{ij}(a_j-a_i)$ | Connes *Noncommutative Geometry* (1994) |

**Poznámka k referenci gr-qc/9406019:** je to Connes-Rovelli *„Von Neumann Algebra Automorphisms and Time-Thermodynamics Relation"* (teze tepelného času, Tomita-Takesaki modulární automorfismus = čas) — motivuje čtení **modulárního toku jako času**, NENÍ to zdroj Connesovy vzdálenostní formule (ta je z knihy 1994). Ověřeno tento běh přes arXiv.

**Parametry:** $N=1200$ ($\le1800$ mez husté `eigh`), 5 seedů; Connesova podmnožina contiguous near-cut patch $\le220$ bodů, 14 párů (mez $\le300$ párů dle receptu).

**KAVEAT (poctivý, vynucený receptem):** $D_K$ je **surogát** Diraca (odmocnina-modulu modulárního kernelu), NIKOLI from-first-principles causal-set Dirac známé KO-dimenze / reálné struktury. Testujeme, zda **modulární data sama** nesou metrický (Connes) + lokalitní obsah, ne zda existuje plný axiomatický spektrální triple.

---

## Výsledky

### (1) Spektrum: funkcionální kalkul exaktní (konzistenční kontrola)

Z konstrukce $\mathrm{spec}(D_K)=\mathrm{sgn}(\lambda_K)\sqrt{|\lambda_K|}$ a $D_K^2=|K|$: best-fit škála $\mathrm{spec}(D_K)^2 / |K| = 1{,}0000$, match $R^2=1{,}0000$, rel. reziduum $\sim10^{-15}$ (raw `spec_rel_resid_mean`$=1{,}8\times10^{-15}$). To je triviální (z definice), slouží jako sanity check symetrického funkcionálního kalkulu, **ne** jako volný test.

### (2) Lokalita $K$ na slabu — boost ANO, off-diagonála hraničně lokální

| Veličina (5 seedů, N=1200) | Hodnota | Kritérium | Verdikt |
|----------------------------|---------|-----------|---------|
| Diagonální boostová váha $|K(x,x)|$ vs vzdálenost k řezu — linearita $R^2$ | **0,955** (0,947–0,968) | $>0{,}9$ a sklon $>0$ | **PASS** (boost lineární) |
| Off-diagonální spad $\log|K(x,y)|$ vs $\log|x-y|$ — sklon | **−0,50** (−0,57…−0,48) | $<0$ (lokální) | sklon negativní ✓ |
| Off-diagonální spad — $R^2$ | **0,765** (0,749–0,779) | $>0{,}8$ | **TĚSNĚ POD** prahem |
| Weylova dimenze (counting $N(\Lambda)\sim\Lambda^d$) | **1,54** (1,46–1,65) | $\in[1{,}7;2{,}3]$ | **POD pásmem** |

**Boostová Bisognano-Wichmannova váha je čistě lineární** (diagonála $K$ roste lineárně se vzdáleností od řezu, $R^2\approx0{,}96$) — to je nejsilnější pozitivní signál a potvrzuje, že SJ modulární kernel na Rindlerovsky řezaném slabu JE geometrický boost. Off-diagonální spad je **robustně negativní** (lokalita přítomna napříč všemi seedy), ale log-log $R^2\approx0{,}77$ leží **těsně pod** předregistrovaným prahem 0,8. Weylova dimenze $\approx1{,}5$ konzistentně **pod** cílem 2 — modulární Diracovo spektrální counting dává efektivní dimenzi bližší 1,5 než 2 (boostové/Rindlerovo spektrum není ploché Diracovo spektrum Minkowského).

### (3) Connesova vzdálenost vs kauzální vzdálenost — KLÍČOVÝ TEST

Connesova vzdálenost počítána na **contiguous near-cut patch 220 bodů** (z plného $n_{\text{sub}}=614$; mez rozpočtu), 14 párů přes rozsah separací. Optimalizace $d_D=\sup\{|a_i-a_j|:\|[D,a]\|_{\mathrm{op}}\le1\}$ jako scale-invariantní maximum (projektovaný ascent).

| Pár (kauzální vzdál.) | 0,00 | 0,03 | 0,06 | 0,10 | 0,14 | 0,19 | 0,27 | 0,36 |
|---|---|---|---|---|---|---|---|---|
| $d_D$ (Connes) | 2,19 | 2,37 | 2,09 | 1,83 | 2,70 | 2,45 | 2,14 | 2,69 |

**Pearsonova korelace $d_D$ vs kauzální vzdálenost = 0,098; lineární fit $R^2=0{,}0095$; sklon 0,27.** Connesovy vzdálenosti se shlukují kolem 2,0–2,5 **nezávisle** na kauzální/geodetické vzdálenosti (0,0 → 0,36). Distance je **plochá / saturovaná, NEsleduje** geodetickou vzdálenost.

**Optimalizátor ověřen nezávisle:** na kanonickém 1D Diracově řetězci $D=i(S-S^{\mathsf T})$ dává `connes_distance` sousedním bodům přesně 1 a monotónně roste se separací (test `test_toe_spectraltriple.py`). Plochost $d_D$ na modulárním Diracovi je tedy **fyzikální vlastnost objektu**, ne selhání solveru.

---

## Verdikt korespondence: **no-match** (s parciálním pozitivem na boostové straně)

Podle předregistrovaných kritérií:

| Subtest | Kritérium | Výsledek | Status |
|---------|-----------|----------|--------|
| Spektrální shoda $D_K^2=|K|$ | $R^2>0{,}99$ | 1,0000 | ✓ (triviální, z definice) |
| **Diagonální boost lineární** | $R^2>0{,}9$, sklon$>0$ | **0,955**, sklon 27 | **✓ PASS** |
| Off-diag spad lokální | $R^2>0{,}8$, sklon$<0$ | sklon −0,50 ✓, $R^2$ **0,765** | ✗ (sklon ano, $R^2$ těsně pod) |
| Weylova dimenze | $\in[1{,}7;2{,}3]$ | **1,54** | ✗ (pod pásmem) |
| **Connes sleduje kauzální vzdál.** | korelace$>0{,}5$ | **0,098** | **✗ FAIL** |

**Souhrn:** Spektrální triple z modulárního kernelu **reprodukuje boostovou strukturu** (lineární Bisognano-Wichmannova diagonální váha, $R^2\approx0{,}96$, robustní napříč 5 seedy) a **lokalitu** (negativní off-diagonální spad), ale **NEreprodukuje metrický obsah ve smyslu Connesovy vzdálenosti** — $d_D$ je plochá a nekorelovaná s geodetickou vzdáleností (korelace 0,10). Weylova dimenze $\approx1{,}5$ < 2.

To je **čistý parciální/negativní výsledek**: modulární data nesou *boostovou (časovou, modulárně-tokovou)* geometrii, ale modulární Diracova *prostorová* metrika (Connes) nereprodukuje kauzální vzdálenost. Korespondence „SJ modulární Hamiltonián ↔ NCG spektrální triple" v této surogátní instanci **NEplatí na úrovni metriky**.

### Proč to dává fyzikální smysl

$D_K=\mathrm{sgn}(K)\sqrt{|K|}$ má diagonálu rostoucí lineárně se vzdáleností od řezu (boostová váha $\beta(x)\sim x$). Connesova vzdálenost čte metriku z **off-diagonálního „gradientu"** $[D,a]_{ij}=D_{ij}(a_j-a_i)$. Modulární boostový generátor je dominován svou diagonální (lokálně-energetickou) složkou; jeho komutátorová struktura nedává distance-aditivní metriku — odtud saturace $d_D$. Modulární tok je generátor **boostu (času)**, ne Diracova **prostorová** metrika; korespondence selhává přesně tam, kde by musela ztotožnit dva různé geometrické obsahy.

---

## Co to znamená pro hranu causal-sets ↔ noncommutative-geometry a pro program

**Hrana `causal-sets → noncommutative-geometry` (`barely`, H5g-4 PRIORITY HUNTING TARGET)** byla touto prací **poprvé instancována** jako konkrétní datová hrana — přesně to, co popis hrany žádal („srovnat Connesovu vzdálenost vůči modulární vzdálenosti na nasypaném slabu"). Výsledek je **smíšený, převážně negativní na metrické úrovni**:

1. **Boostová / modulárně-toková strana funguje:** SJ modulární Hamiltonián JE geometrický boost na Rindlerovsky řezaném slabu (lineární diagonála, $R^2\approx0{,}96$) a kandidátní Dirac $D_K$ ho věrně nese. To podporuje *čtení modulárního toku jako (imaginárně-časového) generátoru* — což je přesně ta část korespondence, kterou motivuje Connes-Rovelli teze tepelného času (gr-qc/9406019).
2. **Metrická / Connesova strana NEfunguje:** Connesova vzdálenost surogátního modulárního Diraca nereprodukuje kauzální/geodetickou vzdálenost (korelace 0,10, $R^2=0{,}01$). NCG „rekonstrukce geometrie z Diraca" se v této instanci **NEztotožňuje** s SJ/SSEE rekonstrukcí.

**Doporučená změna hrany:** ponechat rating **`barely`**, ale **anotovat** ji o tento konkrétní tested negativ: „surogátní modulární Dirac $D_K=\mathrm{sgn}(K)\sqrt{|K|}$ reprodukuje boostovou strukturu, ale jeho Connesova vzdálenost NEsleduje kauzální vzdálenost (VYPOCET-29) — korespondence selhává na metrické úrovni; sjednocení linek A & B pod jedním Diracem touto cestou NEpotvrzeno." Hrana NEpřechází na `partially`, protože jediné instancování dalo na klíčové (metrické) ose negativní výsledek; je ale nyní *informovaný* negativ, ne *neprozkoumaný*.

**Pro program (sjednocuje to linky A & B pod Diracem?):** **NE, ne touto surogátní cestou.** Modulární Hamiltonián a NCG Diracův operátor nesou *různé* geometrické obsahy: $K$ je generátor boostu (modulární tok ≈ čas/Tomita-Takesaki), kdežto NCG Dirac kóduje *prostorovou* metriku přes Connesovu vzdálenost. Sjednocení by vyžadovalo Dirac postavený z kauzální struktury samé (ne z modulárního kernelu), jehož $D^2$ je d'Alembertián a jehož komutátorová metrika je geodetická — to zůstává otevřeným problémem. Pozitivem je, že boostová osa korespondence je solidní a knihovní primitivy (`dirac_from_kernel`, `connes_distance`) jsou nyní k dispozici pro budoucí non-surogátní testy.

---

## Knihovní příspěvek

Vznikl čistý composable primitiv `lib/toe/spectraltriple.py` (vrstva C3):

- `dirac_from_kernel(K)` → $D_K=\mathrm{sgn}(K)\sqrt{|K|}$ (symetrický funkcionální kalkul, $D_K^2=|K|$, Hermitovský);
- `connes_distance(D, i, j)` → $d_D=\sup\{|a_i-a_j|:\|[D,a]\|_{\mathrm{op}}\le1\}$ jako scale-invariantní Rayleighovo maximum (projektovaný ascent, deterministický seed);
- `connes_commutator_norm(D, a)` → $\sigma_{\max}([D,a])$.

Test `app/tests/test_toe_spectraltriple.py` validuje: (i) $D_K^2=|K|$ na strojovou přesnost; (ii) na kanonickém 1D Diracově řetězci $D=i(S-S^{\mathsf T})$ je Connesova vzdálenost sousedních bodů přesně 1 a monotónní v separaci (reprodukuje mřížkovou metriku). Tím je optimalizátor ověřen nezávisle — plochost $d_D$ na slabu je **fyzikální signál o modulárním Diracovi**, ne artefakt solveru.

---

## Limity

- $D_K$ je surogát, ne axiomatický spektrální triple (žádná reálná struktura / KO-dimenze / chiralita). Plný test by potřeboval konstrukci Diraca z kauzální struktury samé (otevřený problém).
- Off-diag $R^2$ a Weylova dimenze jsou hraniční / mírně pod prahem; nejsou vyladěny pro PASS (poctivost).
- Connesova podmnožina je contiguous near-cut patch $\le220$ bodů (mez rozpočtu); plný slab není testován Connesem.
- 2D slab, bezhmotný skalár; 4D BD-box je dle receptu vyloučen z této PoC.

---

## Reference (ověřené tento běh / přítomné v repu)

- **1611.10281** Sorkin-Yazdi — SJ stav, Pauli-Jordan, $G_R=\tfrac12 C$.
- **1712.04227** — Bisognano-Wichmann modulární tok = boost (kontext SSEE cutoff).
- **2008.07697** Surya et al. — SSEE truncace (kontext).
- **0905.2562** Casini-Huerta — *Entanglement entropy in free QFT*; jednomódové $\varepsilon=\ln[\mu/(\mu-1)]$.
- **gr-qc/9406019** Connes-Rovelli — *Von Neumann Algebra Automorphisms and Time-Thermodynamics Relation* (modulární tok = tepelný čas; motivace, NE distance-formule). Ověřeno tento běh.
- **1305.2588** Aslanbeigi-Saravani-Sorkin, **1001.2725** Benincasa-Dowker — BD objekty (kontext, ve 4D větvi).
- Connes, *Noncommutative Geometry* (Academic Press, 1994) — Connesova spektrální vzdálenostní formule (kniha, bez arXiv ID).
