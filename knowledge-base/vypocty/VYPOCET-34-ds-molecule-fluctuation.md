# VYPOCET-34: 4D dS horizontová entropie z FLUKTUACE molekul (order-by-disorder) — žije area-zákon ve varianci, kde mean selhal?

**Datum:** 2026-06-08
**Hypotéza:** H6g-6 (BRAINSTORM-06), přerámováno jako variance-osa nad F-031
**Status:** Dokončeno (`status: complete`, wall-clock ~515 s, 5 hustot × 200 seedů)
**Soubory:** `core-data/calculations/ds-molecule-fluctuation/calc.py`, `results.json`, `plots/var_molecule_vs_A.png`, `plots/fluctuation_vs_mean_arealaw.png`
**Knihovna:** nový primitiv `toe.causet.molecule_count_fluctuation` (+ test `app/tests/test_toe_molecule_count_fluctuation.py`, 5 testů); `toe` v0.3.1
**Cluster:** entropy-cluster × black-holes-information × horizon-molecule × order-by-disorder × dimension-dependence × variance-axis

---

## Cíl a sázka

F-031 / VYPOCET-27 zabil 4D **mean-count** area-zákon: korigovaná kodim-2 Dou-Sorkinova molekula škáluje jako vlastní plocha $\langle N_{mol}\rangle\sim\rho^{0.494}$, ALE obsahová entropie $S_{full}\sim\rho^{1.0}$, takže poměr $S_{full}/A$ driftuje — **žádný $\rho$-invariantní 4D area-zákon na ose střední hodnoty** (čistý negativ, dimenzně závislý: 2D funguje, 4D ne).

H6g-6 otvírá dveře, které F-031 nechal pootevřené: Sorkinova původní **order-by-disorder** horizontová entropie je tvrzení o **fluktuaci** počtu kauzálních linků křižujících horizont, NE o jeho střední hodnotě. Možná area-zákon žije ve **varianci** $\mathrm{Var}(N_{mol})$, kde mean selhal. To je entropický analog k F-035 / VYPOCET-31: tam Λ shot-noise **přežil** F-005 na ose variance / boost-kovariance (Fano $=1$, $\mathrm{Var}(N)\sim V$), kde mean-prefaktor byl vyvrácen. Otázka:

> Nese 4D dS horizontovou entropicko-plošnou relaci **fluktuace** (variance) kodim-2 molekulového počtu přes mnoho sprinklingů (order-by-disorder counting), místo jeho **střední hodnoty**?

**Predikce H6g-6:** $\mathrm{Var}(N_{mol}^{codim-2})\sim\rho^{0.5}$ (plocha) s $\rho$-invariantním poměrem $\mathrm{Var}/A_{proper}$ → order-by-disorder area-zákon existuje (pozitiv, zrcadlí F-035). Diskriminátor je, zda exponent variance $q$ vyjde $0.5$ (plocha) nebo zřetelně jinak.

---

## Metoda a setup

**Geometrie (identická s F-031 Stage B):** `toe.causet.sprinkle_ds_static_patch4d`, $l=1$, near-horizon box $R^*_{box}=4.3$ (plató box z VYPOCET-27), fixní řez $O=\{r^*\le R_{CUT}\}$, $R_{CUT}=1.0$, příčný box $|x_{1,2}|\le 1.0$, $T_{half}=0.5$. Kodim-2 entanglement 2-plocha $E_0=\{r^*=R_{CUT},\,t=0\}$ je **fixní** (geometrická plocha $A_{proper}=(2\cdot 1.0)^2=4$, $\rho$-nezávislá).

**Objekt:** `toe.causet.horizon_molecules_codim2` (VYPOCET-27 primitiv), $k_{tube}=1.5$ **zděděno beze změny** (žádné re-ladění — k_tube caveat z F-031 nesen poctivě). Přes každý seed jeden molekulový počet $N_{mol}$.

**Klíč: žádný eigh, žádný SSEE.** Měří se jen **kombinatorika** na kauzální matici (causal_matrix + redukce na linky uvnitř primitivu + počet molekul). Cena $O(N^2)$ na seed → stovky seedů levné. Tím je fluktuace **čistě geometrická** (počet near-null straddling linků na 2-ploše), bez SSEE-pozitivity otázek.

**Vzorek:** $\rho\in\{120,240,480,960,1920\}$, $N\in\{480,960,1919,3839,7677\}$, **200 seedů na hustotu** (variance-estimátor je šumný — BRAINSTORM-06 riziko; proto mnoho seedů A široký $\rho$-rozsah). Seed schéma: `default_rng(34_000_000 + 100000·int(rho) + s)`, nepřekrývající se streamy (disjunktní od VYPOCET-27 @ 27M a VYPOCET-31 @ 20.26M).

**Observable vs $\rho$:** mean $\langle N_{mol}\rangle$ (re-potvrzení F-031 plochy), $\mathrm{Var}(N_{mol})\sim\rho^{q}$ (THE order-by-disorder veličina), $\sqrt{\mathrm{Var}}\sim\rho^{q/2}$, Fano $=\mathrm{Var}/\langle N\rangle$ (Poisson → 1), a gaussovská order-by-disorder entropie $S_{fluc}=\tfrac12\ln(2\pi e\,\mathrm{Var})$ (= $\ln$ počtu rozlišitelných konfigurací).

**Anti-kruhovost:** $\varepsilon=\rho^{-1/4}$ (4D) ZAFIXOVÁNO z nezávislého F-006 zákona $\varepsilon\sim\rho^{-1/d}$ ($p_{rank}=0.519\pm0.007$), asertováno PŘED jakýmkoli poměrem — nikdy laděno, aby $\mathrm{Var}/A$ vyšlo konstantní.

**CI:** bootstrap přes seedy (2000 resamplů, resampling seedů uvnitř každé $\rho$, refit exponentu) — poctivé CI na exponentu variance, který je mnohem šumnější než mean.

---

## Výsledky

### Tabulka (5 hustot, 200 seedů každá)

| $\rho$ | $N$ | $\langle N_{mol}\rangle$ | $\mathrm{Var}(N_{mol})$ | $\sqrt{\mathrm{Var}}$ | Fano | $S_{fluc}$ | min | max |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 120 | 480 | 85.9 | 319.3 | 17.9 | 3.72 | 4.30 | 46 | 147 |
| 240 | 960 | 125.7 | 612.4 | 24.7 | 4.87 | 4.63 | 69 | 189 |
| 480 | 1919 | 180.9 | 842.4 | 29.0 | 4.66 | 4.79 | 104 | 274 |
| 960 | 3839 | 263.1 | 1407.9 | 37.5 | 5.35 | 5.04 | 179 | 388 |
| 1920 | 7677 | 386.4 | 2046.2 | 45.2 | 5.30 | 5.23 | 273 | 494 |

### Exponenty (log-log fit + bootstrap CI68/CI95)

| veličina | exponent | bootstrap CI68 | CI95 | cíl |
|---|---:|---|---|---|
| **mean** $\langle N_{mol}\rangle$ | $\rho^{0.540\pm0.003}$ | [0.535, 0.546] | — | $\rho^{0.5}$ (plocha) — **F-031 potvrzen** |
| **Var** $\mathrm{Var}(N_{mol})$ | $\rho^{0.656\pm0.040}$ | **[0.614, 0.701]** | **[0.575, 0.745]** | $\rho^{0.5}$ (plocha) nebo $\rho^{1.0}$ (objem)? |
| $\sqrt{\mathrm{Var}}$ | $\rho^{0.328}$ | [0.307, 0.350] | — | $\rho^{0.25}$ (= $q/2$ pro area) |
| Fano slope | $\rho^{0.115}$ | **[0.073, 0.160]** | — | $\rho^{0}$ (Poisson/area-clean) |
| $S_{fluc}$ | $\rho^{0.069\pm0.005}$ | — | — | (logaritmický nárůst, $\propto q\ln\rho$) |

**Rozhodující čísla:**

1. **$q_{var}=0.656$, CI95 $[0.575, 0.745]$ — VYLUČUJE plochu $\rho^{0.5}$** na 95% hladině (dolní hrana 0.575 > 0.5). Současně vylučuje objem $\rho^{1.0}$. Exponent variance leží **mezi** plochou (0.5) a objemem (1.0).
2. **mean $=0.540$** — přesně reprodukuje F-031 plochu $\rho^{0.494}$ (drobný rozdíl je near-horizon box vs plató cap; konzistentní v rámci k_tube tiltu +0.0–0.1).
3. **Fano roste**, slope $0.115$ s CI68 $[0.073, 0.160]$ **vylučuje 0** → počet je genuinně **super-Poissonovský** (Fano $\approx$ 3.7 → 5.3, ne 1). To je **klíčový kontrast s F-035** (tam Fano $=1$, čistý Poisson).
4. **$\mathrm{Var}/A_{proper}$ NENÍ $\rho$-invariantní**: CV $=0.66$ (mean/A CV $=0.57$). Ani jedna osa nedá plochou čáru poměru-k-ploše.

Figura `var_molecule_vs_A.png`: Var (oranžová) sleduje dráhu MEZI vodítky $\rho^{0.5}$ (zelená) a $\rho^{1.0}$ (červená), viditelně strmější než plocha. Figura `fluctuation_vs_mean_arealaw.png`: levý panel ukazuje, že ani $\mathrm{Var}/A$ ani $\langle N\rangle/A$ není plochá čára (žádný area-zákon na žádné ose); pravý panel Fano sedící na 4–5, vysoko nad Poissonovou linkou 1.

---

## Verdikt a limity

**Korespondence: `negative`.** Fluktuace molekulového počtu **NEDÁVÁ** čistý area-zákon: $\mathrm{Var}(N_{mol})\sim\rho^{0.66}$ (CI95 vylučuje plochu $\rho^{0.5}$ i objem $\rho^{1.0}$), $\mathrm{Var}/A_{proper}$ driftuje (CV 0.66). Mean už selhal (F-031), a teď **i fluktuace selhává** → 4D dS area-zákon je **NEPŘÍTOMNÝ na OBOU osách — mean i variance**. Druhý nezávislý negativ posilující F-031.

**Proč variance nedá plochu (mechanismus):** počet je **super-Poissonovský** s rostoucím Fano. Near-null straddling linky na kodim-2 ploše **clusterují** (kladná korelace přítomnosti molekul), takže variance je nadkriticky zvednutá nad mean-škálování plochy, aniž by dosáhla objemového zákona. Kontrast s F-035 je poučný: tam byl počet **přesně Poissonovský** (Fano $=1$, $\mathrm{Var}=\langle N\rangle$), takže variance kopírovala mean a nesla stejný (objemový, ale tam to byla zamýšlená veličina) signál; **tady** je počet ne-Poissonovský, takže variance nese **vlastní, odlišné** škálování ($q=0.66 \ne p=0.54$) — a to odlišné škálování bohužel není plocha.

### Vztah k F-035 (klíčové přerámování)

H6g-6 byl postaven jako entropický paralel k F-035 (variance přežije, kde mean selhal). **Paralela NEDRŽÍ**, a to je sám o sobě informativní:
- F-035: počet atomů v boxu je **Poisson** → Fano $=1$ je vlastnost procesu; variance je čistá a boost-kovariantní. Pozitiv tam stál na (ii) boost-invarianci a (iii) kontrastu s mřížkou, ne na triviálním Fano $=1$.
- F-034 (tento výpočet): počet molekul na 2-ploše je **super-Poisson** (Fano roste 3.7→5.3) → variance NENÍ čistá; nese exponent 0.66, který není ani plocha, ani objem. Order-by-disorder fluktuace tedy v této 4D konstrukci **nekóduje plochu**.

Rozdíl je fyzikální: Poissonův sprinkling počtu atomů je exaktně Lorentz-invariantní bodový proces (čistá variance), kdežto molekuly = **korelované** near-null kauzální páry na 2-ploše (clusterovaná variance). Order-by-disorder area-zákon by potřeboval, aby tyto korelace přesně vyšuměly na $\rho^{0.5}$ — nevyšuměly.

### Poctivé limity a caveaty

- **Konformně-váhový caveat (zděděno z VYPOCET-21/27).** 4D bezhmotný skalár NENÍ konformně invariantní; toto je řízená aproximace (plochá kauzální struktura v $(t,r^*,x_1,x_2)$ + dS proper sech² míra), NE přesný 4D dS Wightmanův stav. Zde ale **žádný eigh/SSEE** → fluktuace je čistě geometrická (počet near-null straddling linků), takže tento caveat se dotýká jen interpretace „dS horizont", ne samotného měření variance.
- **k_tube citlivost.** $k_{tube}=1.5$ zděděno beze změny z F-031. Mean exponent je na něm citlivý (0.4 při k=1.0 → 0.8 při k=2.0); variance exponent může být ještě citlivější. Netestováno přes k_tube v tomto běhu — verdikt platí pro $k_{tube}=1.5$ (principiální volba VYPOCET-27). To je hlavní reziduální nejistota; budoucí robustnostní test by měl k_tube sweepnout.
- **Rozsah $\rho$ a typ I_n.** $\rho\in[120,1920]$, 5 bodů, ale s 200 seedy a bootstrapem dává CI95 variance exponentu šířky $\sim0.17$, dost těsné na vyloučení plochy. Na konečném causal setu je každá algebra triviálně typ I_n; tady neřešíme von Neumann typ — měříme čistě počítací statistiku.
- **$S_{fluc}$ jako entropie.** Gaussovská $S_{fluc}=\tfrac12\ln(2\pi e\,\mathrm{Var})$ je jen logaritmus variance + konstanta; její $\rho$-exponent (0.069) je $\propto q/(\ln\rho\text{-baseline})$, tedy redundantní s $q_{var}$, ne nezávislý kanál. Uvedeno pro úplnost order-by-disorder rámce.
- **dS Gibbons-Hawking primár NENÍ v repu** → aplikace A/4 na kosmologický horizont značena ⚠️ neověřeno; postupováno přes bezrozměrné exponenty a poměry.

### Rozsah (scope)

4D, čistě kombinatorické (causal matrix + molekulový počet), bez eigh. Reprodukce bit-identická (dva po sobě jdoucí běhy daly shodná čísla do posledního místa). Testuje fluktuační spektrum molekulového počtu, ne hodnotu entropie.

---

## Návrh F-038 (do registru)

Viz `findingProposal` v orchestračním výstupu. Jádro: *„4D dS horizontový area-zákon je nepřítomný i na ose VARIANCE: order-by-disorder $\mathrm{Var}(N_{mol}^{codim-2})\sim\rho^{0.66}$ (CI95 [0.58,0.75] vylučuje plochu $\rho^{0.5}$ i objem $\rho^{1.0}$), $\mathrm{Var}/A$ driftuje (CV 0.66), počet je super-Poisson (Fano roste 3.7→5.3). Druhý nezávislý negativ k F-031 — 4D area-zákon chybí na MEAN i VARIANCE ose. Na rozdíl od F-035 (Poisson, Fano=1) jsou molekuly korelované, takže variance nekóduje plochu."*

---

## Dopad na hranu (edge impact)

Hrana `black-holes-information↔causal-sets` (barely): doplněna daty na ose FLUKTUACE. Sorkinova *„order-by-disorder counting of causal links across horizon… horizon-entropy FLUCTUATIONS"* je v této 4D ploché-kauzální + dS-sech² konstrukci **testována a vychází negativně** — fluktuace molekul nekóduje plochu (super-Poisson clustering, $q=0.66\ne0.5$). To uzavírá variance-osu jako záchranu 4D Dou-Sorkin linie, kterou F-031 nechal teoreticky otevřenou. Hrana `causal-sets↔cosmological-constant-fluctuation` (F-035): kontrast Poisson (čistá variance, area/objem-kóduje) vs molekuly (super-Poisson, nekóduje) je sám o sobě poznatek — **ne každá diskrétní počítací variance je čistá**; rozhoduje, zda je podkladový proces Poissonovský (atomy) nebo korelovaný (molekuly).

---

## Reference (pouze repo-přítomné; ŽÁDNÉ vymyšlené arXiv ID)

- `dou-sorkin-2003` (gr-qc/0302009) — horizontová entropie jako počet kauzálních linků (molekuly); order-by-disorder counting.
- `johnston-2009` (0909.0944) — 4D link-Greenova fce / link konvence.
- F-006 (`ssee-diamond/results.json`) — $\varepsilon\sim\rho^{-1/d}$, $p_{rank}=0.519\pm0.007$ (4D $\varepsilon=\rho^{-1/4}$).
- F-031 (VYPOCET-27, `ds-amol-convention`) — 4D mean-count area-zákon nepřítomný; primitiv `horizon_molecules_codim2`.
- F-035 (VYPOCET-31, `lambda-shot-noise`) — Poisson shot-noise variance přežívá F-005 (Fano=1); variance-osa precedent.
- **⚠️ neověřeno:** de-Sitter Gibbons-Hawking primární zdroj NENÍ v repu.

## Knihovní změny

- `lib/toe/causet.py:molecule_count_fluctuation(make_coords, n_seeds, *, r_index=1, r_cut, eps, k_tube=1.5, seed0=0, stride=1)` — nový composable primitiv (Formula/Evidence/Conventions docstring); across-sprinkling distribuce kodim-2 molekulového počtu (order-by-disorder), vrací `(counts, stats)` s mean/var/std/fano/s_fluc. Registrováno v `toe.__all__` + `__init__.py`; `toe` v0.3.0 → v0.3.1.
- Test `app/tests/test_toe_molecule_count_fluctuation.py` (5 testů: vnitřní konzistence statistik, determinismus ze seedu, shoda s přímým `horizon_molecules_codim2`, `n_seeds<2` raises, super-Poisson Fano>1.5 v 4D).

## Datové cesty

- `core-data/calculations/ds-molecule-fluctuation/{calc.py,results.json}`, `plots/{var_molecule_vs_A.png,fluctuation_vs_mean_arealaw.png}`
- Vstup F-006: `core-data/calculations/ssee-diamond/results.json` (čteno pro $\varepsilon$ anti-kruhovost).
