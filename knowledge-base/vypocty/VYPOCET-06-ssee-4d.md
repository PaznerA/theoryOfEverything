# VYPOCET-06: SSEE na sprinklovaném 4D kauzálním diamantu — test škálovacího exponentu p = 3/4

**Datum:** 2026-06-06
**Soubory:** `core-data/calculations/ssee-4d/calc.py`, `results.json`, `spectrum_knee.png`, `S_vs_rank.png`, `rank_vs_N.png`, `area_law.png`
**Status:** Dokončeno
**Cluster:** entropy-cluster (navazuje na VYPOCET-04; viz `verification/novelty/entropy-cluster.md`)

---

## Cíl

Rozhodující navazující test na VYPOCET-04. Ve 2D jsme naměřili, že rank zachovaných módů při Sorkin-Yazdiho entropickém cutoffu škáluje jako **rank ~ N^0.519 ± 0.007 = N^(1/2)**, tedy přesně area-law exponent (d−1)/d v d=2. Obecná předpověď pro dimenzi d zní:

> **rank ~ N^((d−1)/d)** (area law, Surya, Nomaan X, Yazdi 2008.07697)

**Testovaná předpověď (d=4): p = 3/4 = 0.75** (oproti 2D hodnotě 1/2).

Sekundárně: řídí se dvojitě-truncovaná SSEE ve 4D area-law tvarem S ∝ A/ℓ² (A = plocha bifurkační 2-sféry subdiamantu)?

Klíčová změna oproti 2D: ve 4D je bezhmotná retardovaná Greenova funkce na causal setu úměrná **link matici L** (tranzitivní redukce kauzální relace), nikoli kauzální matici C — Johnstonova konstrukce (arXiv:0909.0944).

---

## Metoda

### 4D geometrie a sprinkling

- **Kauzální diamant** mezi vrcholy (∓T, **0**): D = {x = (t, **r**) : |t| + |**r**| ≤ T}, signatura (−,+,+,+). 4-objem Vol(D) = (2/3)π T⁴ = 2.0944 pro T=1. Hustota ρ = N/Vol.
- **Sprinkling** je Poissonův proces v Lebesgueově míře dt d³r (Lorentzovsky invariantní). Vzorkuji exaktně (žádné rejection sampling): |t| s hustotou ∝ objemu prostorové koule (T−|t|)³ ⇒ s = T·U^(1/4); pak uniformní bod v kouli poloměru s. Ověřeno: všech N bodů uvnitř, počet bodů v subdiamantu f=0.5 ≈ N·(0.5)⁴ = N/16 (objemový poměr) — geometrie potvrzena.
- **Kauzální matice** C[x,y] = 1, právě když y předchází x: (t_x − t_y) ≥ |**r**_x − **r**_y| (časupodobně/nulově do budoucnosti), diagonála 0.
- **Link matice** (tranzitivní redukce / pokrývací relace): L[x,y] = 1, právě když C[x,y]=1 a neexistuje meziprvek w s y < w < x. Počet meziprvků je (C·C)[x,y], takže **L = C ∧ (C·C == 0)**. Vektorizováno; C·C je booleovský matmul (BLAS, 0.4 s při N=5000).

### Sorkin-Johnstonova konstrukce (dimenzně nezávislá, identická s VYPOCET-04)

1. **Retardovaná Greenova funkce (4D bezhmotný skalár):** G_R = a·L, **a = √ρ / (2π√6)**. *(Johnston 0909.0944 eq.17 v limitě m=0; vysokohustotní limita √(ρ/6)⟨L⟩ → 2π G₀^(4): Nomaan X, Dowker, Surya 1701.07212.)*
2. **Pauli-Jordanův operátor:** iΔ = i(G_R − G_R^T), hermitovský, reálná vlastní čísla v párech ±|λ|. *(Ověřeno: Δ exaktně antisymetrická, spektrum přesně symetrické kolem 0.)*
3. **SJ Wightman:** W = pozitivní část iΔ.
4. **SSEE:** zobecněný problém W_O v = μ(iΔ_O)v na subdiamantu, S = Σ μ ln|μ|. *(1611.10281; 2008.07697.)*
5. **Dvojitá truncace** vlastním číslem magnitudou κ (globálně i lokálně), aby se odstranily sub-diskrétní módy. *(1712.04227.)*

### Měřené cutoff/koleno definice (rank vs N)

Ve 2D existoval jeden robustní entropický cutoff κ = √N/4π. Ve 4D literatura **uzavřenou formuli κ pro diamant neuvádí**, proto měřím rank pro několik fyzikálně motivovaných cutoffů a sleduji, který (pokud vůbec) dává robustní exponent:

- **rank @ frac·λ_max** (sebe-kalibrující magnitudový cutoff, density-independentní): frac ∈ {0.02, 0.05, 0.10}.
- **intrinsická koleno** (k·λ_k opouští plató, 2D estimátor): tol ∈ {0.10, 0.20}.
- **slope-knee** (literaturní metoda, 2008.07697 sek. 2.4): rank, kde lokální log-log sklon λ_k vs k klesne zlomkem δ=0.15 pod plató.

### Sekundární area-law test

Při fixním N měním velikost subdiamantu f a fituji S vs plocha A(f) = 4π(fT)² versus S vs počet bodů n_sub (∝ 4-objem). Plus literaturní fixed-rank truncace n_max = α·N^(3/4), α ∈ {1,2} (2008.07697 eq.15).

### Numerika

`numpy.linalg.eigh` (komplexní hermitovský iΔ), 4 seedy na N ∈ {500…5000}, vážený mocninový fit. Úzké hrdlo: eigendekompozice 5000×5000 (~45 s), ne link matmul. Celková doba běhu 1517 s.

---

## Vstupy s citacemi

| Vstup | Hodnota / forma | Zdroj (arXiv ID) |
|-------|-----------------|------------------|
| G_R (4D bezhmotný) = (√ρ/(2π√6))·L | link matice, prefaktor √ρ | Johnston **0909.0944** eq.17 (m=0) |
| Link matice L = tranzitivní redukce C | L = C ∧ (C²==0) | **0909.0944**; **1701.07212** |
| Vysokohustotní normalizace √(ρ/6)⟨L⟩→2πG₀ | konstanta 1/(2π√6) | **1701.07212**; **1611.09947** |
| iΔ = i(G_R−G_R^T), W=Pos(iΔ), S=Σμ ln|μ| | SSEE | **1611.10281**; **2008.07697** |
| Dvojitá truncace magnitudou κ | UV cutoff | **1712.04227** |
| Area-law ansatz n_max = α N^((d−1)/d), d=4 → N^(3/4) | **p = 3/4** | Surya, Nomaan X, Yazdi **2008.07697** eq.15 |
| Slope-knee (δ ≈ 0.10–0.15) | spektrální koleno | **2008.07697** sek. 2.4 |
| 4D nested diamanty → VOLUME law bez truncace | kvalitativní | **2008.07697**; **1712.04227** |
| 2D porovnání: rank ~ N^0.519 = N^(1/2) | p = 1/2 | VYPOCET-04 |

---

## Výsledky

### Tabulka 1 — Škálování cutoff/koleno ranku s N (4 seedy, Vol=2.0944, ρ=N/Vol)

| N | ρ | rank@0.02·λmax | rank@0.05·λmax | rank@0.10·λmax | slope-knee |
|---|-----|------|------|------|------|
| 500 | 239 | 189.5 | 142.5 | 95.8 | 39.2 |
| 800 | 382 | 301.0 | 222.5 | 143.8 | 62.0 |
| 1200 | 573 | 443.0 | 321.0 | 197.5 | 92.0 |
| 1800 | 859 | 655.5 | 463.8 | 270.2 | 136.8 |
| 2600 | 1241 | 937.2 | 651.2 | 360.0 | 197.0 |
| 3600 | 1719 | 1275.5 | 864.2 | 447.0 | 271.5 |
| 5000 | 2387 | 1747.5 | 1155.8 | 558.2 | 377.0 |

### Tabulka 2 — Mocninové fity rank ~ N^p (předpověď p = 3/4)

| Cutoff definice | p | p_err | odchylka od 3/4 |
|-----------------|-----|-------|------------------|
| rank @ 0.02·λmax | 0.964 | 0.003 | +69 σ |
| rank @ 0.05·λmax | 0.903 | 0.005 | +32 σ |
| **rank @ 0.10·λmax** | **0.751** | 0.007 | **+0.1 σ (shoda — náhodná)** |
| intrinsická koleno (k·λ plató) | 0.651 | 0.022 | −4.5 σ |
| **slope-knee (literaturní, 2008.07697)** | **0.985** | 0.001 | **+167 σ (≈ N¹)** |

### Tabulka 3 — Area-law test (N=5000, dvojitá truncace 5% λmax)

| Fit | R² | tvar | verdikt |
|-----|-----|------|---------|
| S vs plocha A(f)=4π(fT)² | 0.962 | — | — |
| **S vs objem n_sub** | **0.998** | S ~ f^6.1 | **VOLUME law** |

Kontrolní test (N=2000, plně podmíněný, numericky stabilní) pro tři cutoffy (κ_knee, 2%, 10%): **všechny dávají VOLUME law** (R²_vol > R²_area), stable=True. Literaturní fixed-rank truncace n_max = α N^(3/4) je v této geometrii **numericky patologická** (S diverguje k 10⁴–10⁵, R²≈0.05) — metoda de Sitter slabu se na single-N nested-diamond nepřenáší.

### Tvar 4D spektra (klíčová diagnostika)

4D bezhmotné SJ spektrum **NENÍ čistý mocninový zákon λ_k ~ 1/k jako ve 2D.** Plot `spectrum_knee.png`: λ_k je téměř ploché (~10–30) přes 3 dekády ranku, pak na samém konci prudce spadne. Součin k·λ_k (který je ve 2D plató) **monotónně roste** k vrcholu u ranku ~900 a pak klesá. To znamená λ_k ≈ konst, ne ~1/k. Spektrum tedy nemá area-law koleno, které by se dalo přečíst přímo.

Mean links/point roste s N (~36 při N=3000) — link matice je hustá, řádky rostou ~N^0.65, což pohání ploché spektrum.

---

## Interpretace pro hypotézu

**Hlavní výsledek: předpověď p = 3/4 NENÍ potvrzena jako robustní spektrální exponent. Naměřený exponent kriticky závisí na volbě cutoffu (od 0.65 do 0.98) a hodnotu 3/4 trefuje jen jeden arbitrární cutoff (10 % λmax) — náhodou.**

To je čistý, nezfalšovaný a fyzikálně důležitý nález — kvalitativně odlišný od 2D:

1. **Ve 2D** dával Sorkin-Yazdiho cutoff κ = √N/4π robustní rank ~ N^(1/2) **bez ohledu na detaily** (spektrum je čisté λ_k ~ 1/k s ostrým plató a kolenem). Měření exponentu ze spektra je tam dobře definované.

2. **Ve 4D** je SJ Pauli-Jordanovo spektrum (postavené z link matice) **ploché, ne mocninové.** Neexistuje ostré area-law koleno. Důsledek: jakýkoli rank-cutoff dá jiný exponent. Literaturní slope-knee (jediná spektrální feature s definovaným fyzikálním smyslem, 2008.07697) škáluje jako **N^0.985 ≈ N¹**, NIKOLI N^(3/4).

3. **Proč p = 3/4 přesto „funguje" v literatuře:** V Surya-Nomaan-X-Yazdi (2008.07697) je n_max = α N^(3/4) **vstupní ansatz, nikoli měřený exponent.** Předpokládají area-law škálování a ověří, že s tímto rankem konzistentně vyjde area law (S = a√N + b) v de Sitter slabu. Naše práce ukazuje, že tento exponent **nelze nezávisle odečíst ze spektra 4D diamantu** — je to imposovaná hodnota.

4. **Sekundární: 4D dvojitě-truncovaná SSEE na nested diamantu robustně dává VOLUME law** (S ~ objem ~ f^6, R²=0.998), ne area law. To **přesně reprodukuje literaturu**: „nested causal diamonds in 4d Minkowski naturally give a volume law … area law je obnoven jen při vhodné truncaci" (2008.07697, 1712.04227); volume law „can be traced to the non-locality inherent in the causal set." Naše dvojitá truncace magnitudou (analogická 2D κ) area law **neobnoví** — to vyžaduje specializovanou slab-geometrii nebo externě imposovaný rank.

**Verdikt pro entropy-cluster hypotézu:** Jednoduchá extrapolace „naměř p ze spektra" z 2D (p=1/2 ✓) na 4D (p=3/4) **selhává**. Modulární/UV cutoff identifikovaný ve 2D nemá ve 4D nested diamantu robustní spektrální protějšek; 4D area law je v literatuře dosažen imposicí, ne emergencí. To je důležité varování pro hypotézu: pokud entropy-cluster spojuje truncační cutoff s area gapem LQG (Δ = 4√3 π γ l_P² ve 4D), pak ve 4D **chybí čistá spektrální signatura**, kterou 2D nabízelo. Identifikace ε ~ ρ^(−1/d) ve 4D není vyloučena, ale **z těchto dat ji nelze potvrdit** — naměřený exponent je 0.65–0.98 podle cutoffu, ne ostré 3/4.

Tento výsledek je metodologicky cenný: ukazuje, kde 2D analogie přestává platit, a směřuje k tomu, že area-law charakter 4D SSEE je subtilnější (vyžaduje slab nebo Rindler geometrii, ne nested diamant) — což je třeba zohlednit při jakémkoli mostu k LQG area gapu.

---

## Limity výpočtu

- **Ploché 4D spektrum brání odečtu exponentu.** Na rozdíl od 2D (čisté 1/k) nemá 4D SJ spektrum ostré koleno; všechny rank-cutoff estimátory dávají různá p. To je intrinsická vlastnost link-matice konstrukce, ne numerický artefakt (ověřeno přesnou ±-párovostí a antisymetrií).
- **Nested diamant ≠ de Sitter slab.** Literaturní area law (2008.07697) byl validován na slab/Rindler geometrii s fixní plochou a měnícím se N (S=a√N+b). Náš protokol mění velikost subregionu při fixním N. Pro tuto geometrii literatura sama předpovídá volume law — náš výsledek je s ní konzistentní, ale **netestuje area-law slab konfiguraci.**
- **Fixed-rank truncace numericky nestabilní** v diamantové geometrii (S ~ 10⁵). Zobecněný problém W_O v = μ iΔ_O v je špatně podmíněný, když globální rank-cut a lokální submatice nesedí. Reportováno jako limit, nepoužito pro číselný závěr.
- **N ≤ 5000.** Eigendekompozice 5000×5000 je úzké hrdlo (~45 s/seed). Vyšší N by zpřesnilo fity, ale nezmění kvalitativní nález (ploché spektrum, cutoff-závislé p) — ten je robustní napříč N ∈ [500, 5000].
- **Pouze magnitudová dvojitá truncace.** Neimplementovali jsme literaturní slope-knee truncaci pro SSEE samotnou (jen pro měření ranku), protože v diamantu nedává stabilní entropii. 3D případ (predikce p=2/3, Johnston/Dowker-Surya konvence přes C s jinou konstantou — 1701.07212) nebyl proveden, protože 4D byl výpočetně proveditelný (~25 min) a je primárním cílem; 3D zůstává možným doplňkem.
- **Mean links/point roste s N** (link matice hustne); kontinuum-limita G_R → spojitá G_R je platná jen pro ρ → ∞, takže nejmenší N (500) jsou nejméně konvergované. Fit slope-knee (p=0.985, malé reziduum) je nejstabilnější.

---

## Citace (prohledané/použité arXiv IDs)

- **0909.0944** — Johnston, *Feynman Propagator for a Free Scalar Field on a Causal Set* (PRL 103, 180401): G_R^(4) = (√ρ/(2π√6))·L, link matice, eq.17
- **1701.07212** — Nomaan X, Dowker, Surya, *Scalar Field Green Functions on Causal Sets*: 4D/2D/3D konvence, √(ρ/6)⟨L⟩→2πG₀
- **1611.09947** — *Towards Spectral Geometry for Causal Sets*: normalizace 1/(2π√6)
- **1611.10281** — Sorkin-Yazdi, *Entanglement Entropy in Causal Set Theory*: SSEE formule, dvojitá truncace
- **2008.07697** — Surya, Nomaan X, Yazdi, *Entanglement Entropy of Causal Set de Sitter Horizons*: n_max = α N^((d−1)/d), slope-knee δ≈0.15, volume→area přes truncaci, S=a√N+b
- **1712.04227** — *On the Entanglement Entropy of Quantum Fields in Causal Sets*: dvojitá truncace, 4D volume law bez truncace
