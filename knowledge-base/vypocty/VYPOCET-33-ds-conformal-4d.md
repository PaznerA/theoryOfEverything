# VYPOCET-33: Konformně-vázaný 4D dS skalár — rozhoduje nevyřešený konformní caveat F-031 (H6g-2)

**Datum:** 2026-06-08
**Soubory:** `core-data/calculations/ds-conformal-4d/calc.py`, `results.json`, `plots/R_conformal_vs_nonconformal.png`; knihovna `lib/toe/causet.py` (nový primitiv `bd_dalembertian_inverse_massive` + test `app/tests/test_toe_causet.py`: `test_bd_massive_m0_recovers_massless`, `test_bd_massive_conformal_sj_well_defined`)
**Status:** Dokončeno (rozhoduje jediný nevyřešený caveat F-031)
**Hypotéza:** H6g-2 (BRAINSTORM-06; hrana `causal-sets ↔ holography-adscft`, rating `barely`)
**Navazuje:** VYPOCET-27 / F-031 (4D dS area-zákon GENUINNĚ NEPŘÍTOMNÝ v ploché-kauzální + dS-sech²-míra konstrukci: korigovaná kodim-2 molekula $A_{mol}\sim\rho^{0.494}$ ale $S_{full}\sim\rho^{0.997}$ objemově, žádný ρ-invariantní poměr). F-031 nechal otevřený **jediný caveat (a)**: 4D bezhmotný skalár NENÍ konformně invariantní, takže drift mohl být artefakt non-konformní aproximace.
**Cluster:** entropy-cluster × horizon-SJ × causal-set first-principles × conformal-coupling × dimension-dependence

---

## Programová otázka

F-031 (VYPOCET-27) uzavřel 4D dS area-zákon jako **poctivý negativ** — ale s jednou výslovnou výhradou (caveat (a), doslova): *„4D bezhmotný skalár NENÍ konformně invariantní … verdikt platí pro TUTO konstrukci, ne nutně pro přesný dS stav."* H6g-2 tuto výhradu **rozhoduje**.

Logika podezření: 2D konformní trik VYPOCET-19/23 (F-028, čistý 2D area-zákon) fungoval **právě proto**, že 2D bezhmotný skalár JE konformně invariantní — dS konformní faktor $\Omega^2=\mathrm{sech}^2(r^*/\ell)$ vypadl z propagátoru a dS vstoupil jen přes míru sprinklingu. Ve 4D bezhmotný skalár konformně invariantní NENÍ, takže faktor zůstává v propagátoru a **mohl** kazit škálování $S_{full}$. **Konformní vazba** $\xi R\phi^2$ s $\xi=1/6$ činí 4D skalár konformně invariantním; na dS $R=12/\ell^2$ je konstantní, takže efektivní hmota je konstanta $m_{eff}^2=\xi R=2/\ell^2$ — masivní 4D Klein-Gordonovo pole.

**Predikce, kdyby caveat byl příčinou:** konformně-vázaný skalár dá $S_{full}\sim\rho^{0.5}$ (area-zákon), ρ-invariantní poměr $R'=S_{full}/A_{codim-2}\to$ konst. **Diskriminátor (BRAINSTORM-06 Test B):**

- konformní ($\xi=1/6$) $R'$ ρ-invariantní (CV < 0,1, $d\ln R'/d\ln\rho\approx 0$) → 4D nepřítomnost **byla artefakt**, area-zákon OBNOVEN (`recovered`);
- konformní $R'$ stále driftuje $\rho^{+0.5}$ jako F-031 → 4D nepřítomnost je **robustní fyzika**, F-031 stojí silněji (`negative`).

---

## Metoda a setup

**Geometrie:** SHODNÁ s VYPOCET-27 — `toe.causet.sprinkle_ds_static_patch4d` (plochá kauzální struktura v $(t,r^*,x_1,x_2)$ + dS proper sech² míra), $\ell=1{,}0$, $T_{half}=0{,}5$, $x_\perp=1{,}0$, fixní řez $O=\{r^*\le R_{CUT}=1{,}0\}$, sweep $R^*_{box}\in\{1{,}6;2{,}2;2{,}8;3{,}5;4{,}3;5{,}2\}$.

**Objekt (nový primitiv):** masivní retardovaná Greenova funkce z masivní ostré Benincasa-Dowkerovy d'Alembertiánu. BD operátor $B$ (vrstvové koeficienty $(1,-9,16,-8)$, prefaktor $4\sqrt\rho/\sqrt6$) je diskrétní realizace $\Box$; Klein-Gordonovo retardované jádro řeší $(\Box-m^2)G_R=\delta$, tedy

$$G_R = (B - m^2 I)^{-1}, \qquad m^2 = \xi R = \tfrac{1}{6}\cdot\tfrac{12}{\ell^2} = \tfrac{2}{\ell^2}.$$

`bd_dalembertian_inverse_massive(C, rho, m2)`; baseline $\xi=0$ ($m^2=0$) reprodukuje bit-za-bit massless `bd_dalembertian_inverse(...,dim=4)`. Body se před invertováním časově uspořádají (`argsort(coords[:,0])`) pro striktní retardovanost (protokol ssee-bd-4d).

**Observable na SHODNÉM sprinklingu (per seed):** $\xi=0$ i $\xi=1/6$ z TÉŽE sprinkle → $i\Delta=\mathrm{pauli\_jordan}(G_R)$, SJ stav, $S_{full}$ (netruncovaná SSEE = II₁ obsah) a $S_{trunc}$ (F-019 regulátor $n_{max}=2N^{3/4}$). Molekula $A_{mol}^{codim-2}$ (`horizon_molecules_codim2`, $k_{tube}=1{,}5$) a raw worldtube count jsou sprinkle-only (ξ-nezávislé). Plató = průměr přes poslední 3 near-horizon boxy (robustní VYPOCET-25/27 protokol).

**Anti-kruhovost:** $\varepsilon=\rho^{-1/4}$ (4D) FIXNĚ z nezávislého F-006 ($p_{rank}=0{,}519\pm0{,}007$), asertováno PŘED jakýmkoli poměrem. $k_{tube}=1{,}5$ převzato z VYPOCET-27 (čistý $\rho^{0.5}$), nikdy laděno k cíli.

**N, seedy, rozpočet:** $\rho\in\{120,240,480\}$, dense $N\le1920$, 4 seedy. Wall-clock 1098 s (~18 min, v rozpočtu). $\rho>480$ přeskočeno-s-poznámkou (repo nemá generický 4D sparse $S_{full}$ primitiv — týž limit jako F-031).

---

## Nález 1 — Masivní SJ stav je dobře definovaný (H6g-2 blokátor ODSTRANĚN)

Hlavní riziko H6g-2 (BRAINSTORM-06 §4 riziko 4): $m_{eff}^2=2/\ell^2$ je $O(1)$, ne malá hmota — masivní $i\Delta$ má jiné spektrum a SJ pozitivita NENÍ a priori zaručena. **Změřeno:** ±-párovost $i\Delta$ přežívá na strojovou přesnost (`max_pairing_residual_rel = 8{,}4\times10^{-15}$ přes všechny ρ/boxy/seedy), SJ Wightmanova matice je PSD na strojovou přesnost (`max_sj_wightman_min_eig_rel = -1{,}0\times10^{-15}$). **Masivní/konformní SJ stav je dobře definovaný**; H6g-2 nepadá na read-first.

---

## Nález 2 — Konformní vazba NEMĚNÍ $S_{full}$ (rozhodující negativ)

| $\rho$ | $A_{mol}^{codim-2}$ | $S_{full}$ ($\xi=0$) | $S_{full}$ ($\xi=1/6$) | $S_{full}^{conf}/S_{full}^{m0}$ | $R'$ massless | $R'$ conformal |
|---|---|---|---|---|---|---|
| 120 | 73,8 | 30,32 | 30,33 | 1,00035 | 0,4111 | 0,4112 |
| 240 | 125,4 | 63,22 | 63,25 | 1,00048 | 0,5041 | 0,5043 |
| 480 | 168,1 | 118,06 | 118,00 | 0,99947 | 0,7024 | 0,7020 |

> **Konformní vazba mění $S_{full}$ o ≤ 0,05 % na všech hustotách** (průměrný poměr $S_{full}^{conf}/S_{full}^{m0}=1{,}00010$). Křivky konformní a bezhmotné se v log-log překrývají bod na bod.

**Fitované exponenty (3-bod, SE):**

| veličina | $\xi=0$ (massless) | $\xi=1/6$ (conformal) |
|---|---|---|
| $S_{full}\sim\rho^{p_S}$ | $0{,}981\pm0{,}046$ | $0{,}980\pm0{,}046$ |
| $A_{mol}^{codim-2}\sim\rho^{p_A}$ | $0{,}594\pm0{,}099$ (sprinkle-only) | táž |
| $R'=S_{full}/A_{codim-2}\sim\rho^{p_{R'}}$ | $+0{,}386\pm0{,}053$ | $+0{,}386\pm0{,}053$ |
| CV($R'$) | 0,276 | 0,275 |

- **$R'$ driftuje IDENTICKY** pro obě vazby: $\rho^{+0.386}$ (CV ≈ 0,28). `R_prime_conformal_invariant = False`.
- $S_{full}$ zůstává **objemové** ($\rho^{0.98}$) pro obě vazby; $A_{codim-2}$ sleduje vlastní plochu ($\rho^{0.59}$, konzistentní s VYPOCET-27 $\rho^{0.494}$ při daném $k_{tube}$ a 3-bod SE).

Figura `plots/R_conformal_vs_nonconformal.png`: vlevo $R'$ konformní (crimson) překrytý $R'$ bezhmotný (navy), oba sledují $\rho^{+0.4}$; vpravo $S_{full}$ obou vazeb na $\rho^{1}$ vodítku, $A_{codim-2}$ na $\rho^{0.5}$.

---

## Verdikt — korespondence NEGATIVE: 4D nepřítomnost je robustní fyzika

Z diskriminátoru H6g-2 platí **negativní** větev:

> **Konformní vazba $\xi=1/6$ ($m_{eff}^2=2/\ell^2$) NEOBNOVÍ 4D dS area-zákon.** $R'$ driftuje $\rho^{+0.39}$ identicky pro $\xi=1/6$ i $\xi=0$ (CV ≈ 0,28 v obou), $S_{full}$ zůstává objemové ($\rho^{0.98}$) pro obě vazby. F-031 4D nepřítomnost area-zákona NENÍ konformně-váhový artefakt — je to **robustní fyzika nezávislá na konformní vazbě**. F-031 stojí silněji.

**Fyzikální výklad PROČ.** Drift $R'$ pramení z toho, že $S_{full}$ škáluje **objemově** ($\rho^1$), zatímco vlastní plocha $\rho^{0.5}$. Objemovost $S_{full}$ pochází z **ploché kauzální struktury** (Johnston/BD link-matice samplující 4-objem), NE z hmotného/konformního členu propagátoru. Konformní mass $m^2=2$ je navíc **malá perturbace** vůči škále operátoru (prefaktor $4\sqrt\rho/\sqrt6\sim 20\text{–}40$ pro $\rho=120\text{–}480$), takže $G_R=(B-2I)^{-1}\approx B^{-1}$ — odtud ≤ 0,05 % změna $S_{full}$. Konformní faktor $\mathrm{sech}^2$ vstupuje do TÉTO konstrukce jen přes míru sprinklingu (jako ve 2D), ne do propagátoru; přidání $\xi R$ tedy nemá co „vyspravit", protože škálovací problém nesedí v propagátoru, ale v dimenzionalitě objem-vs-plocha samplingu. Ve 2D je horizont BOD (kodim-2 = 0-dim), takže $A_{mol}\sim\rho^1$ shodně s objemem a $R^{2D}$ je konstantní (F-028); ve 4D ta degenerace mizí a žádná vazba ji neobnoví.

---

## Stav konformního caveatu (částečně vyřešen)

- **VYŘEŠENA část (a) caveatu F-031:** přechod $\xi=0\to\xi=1/6$ (non-konformní → konformně invariantní 4D skalár) je nyní otestován a **NEMĚNÍ verdikt**. Drift S_full vs plocha NENÍ tím, že 4D bezhmotný skalár není konformně invariantní. Tuto výhradu lze z F-031 odstranit.
- **ZŮSTÁVÁ reziduum (BRAINSTORM-06 §4 riziko 3):** i konformně-vázaný 4D skalár na PLOCHÉ kauzální struktuře (BD link/operátor Green) NENÍ přesný **zakřivený** 4D dS propagátor. H6g-2 odstranil ξ-část caveatu, ne zbytek (plochá kauzalita vs zakřivený propagátor). Plné rozhodnutí by vyžadovalo zakřivený 4D dS Wightmanův stav, který repo NEMÁ. Verdikt zní: „4D area-zákon nepřítomný i pod konformní vazbou NA TÉTO ploché-kauzální konstrukci".

---

## Poctivé limity a caveaty

- **Rozsah ρ.** Jen $\rho\in\{120,240,480\}$ (dense $N\le1920$, afternoon-budget; vyšší ρ by potřebovalo 4D sparse $S_{full}$ primitiv, který repo nemá — viz F-031). Exponenty jsou 3-bodové; klíčový závěr (konformní ≡ massless) je ale exaktní per-cell (poměr 1,0001 nezávisí na fitu).
- **$R'$ exponent +0,39 vs F-031 +0,50.** Mírně nižší než F-031 link-Green $\rho^{+0.5}$, protože (i) zde je $S_{full}$ z BD-inverze (ne link-Green) a (ii) 3-bod $A_{codim-2}$ exponent 0,59 (vs 0,494 ve VYPOCET-27 s více body) je tažený nahoru 4D near-null link-multiplicitou. Kvalitativní závěr (kladný drift, $S_{full}$ objemové) je identický; konformní vs massless srovnání je interní a imunní vůči těmto kalibracím.
- **BD vs link-Green baseline.** BD-massless $S_{full}$ je objemové ($p_S=0{,}98$), shodně s F-031 link-Green ($p_S\approx1{,}04$) — BD baseline reprodukuje kvalitativní F-031 nález, takže konformní kontrast stojí na téže noze.
- **$k_{tube}$ citlivost** (zděděno z F-031): $A_{codim-2}$ exponent závisí na $k_{tube}$; $k=1{,}5$ fixní z VYPOCET-27. Ovlivňuje absolutní hodnotu $R'$, ne konformní/massless rovnost.
- **dS Gibbons-Hawking primár NENÍ v repu** → A/4 aplikace značena ⚠️ neověřeno; postupováno přes bezrozměrné poměry.

---

## Reference (jen přítomné v repu)

- `dou-sorkin-2003` (gr-qc/0302009) — horizontová entropie jako počet kauzálních linků (kodim-2 molekula).
- `johnston-2009` (0909.0944) — 4D link-Greenova fce (massless baseline kontext).
- `benincasa-dowker-2010` (1001.2725) — diskrétní d'Alembertián $B$ (vrstvy $(1,-9,16,-8)$), jádro masivní KG inverze $G_R=(B-m^2I)^{-1}$.
- `clpw-2022` (2206.10780) — dS statická záplata typ II₁.
- F-006 (`ssee-diamond/results.json`) — $\varepsilon\sim\rho^{-1/d}$, $p=0{,}519\pm0{,}007$ (4D $\varepsilon=\rho^{-1/4}$).
- F-031 (VYPOCET-27), F-028 (VYPOCET-23).
- **⚠️ neověřeno:** de-Sitter Gibbons-Hawking primární zdroj NENÍ v repu.

## Knihovní změny

- `lib/toe/causet.py:bd_dalembertian_inverse_massive(C, rho, m2)` — nový composable primitiv (Formula/Evidence/Conventions docstring): retardovaná Greenova fce masivního/konformně-vázaného 4D skaláru $G_R=(B-m^2I)^{-1}$; $m^2=0$ reprodukuje massless bit-za-bit; $m^2=\xi R=2/\ell^2$ = konformní skalár. Exportováno v `toe.__init__`.
- Testy `app/tests/test_toe_causet.py`: `test_bd_massive_m0_recovers_massless` (bit-za-bit massless recovery), `test_bd_massive_conformal_sj_well_defined` (konformní mass mění $G_R$, $i\Delta$ ±-párovost na $10^{-12}$, SJ Wightman PSD — H6g-2 well-definedness).
- Registrace v `app/tests/test_reproduction.py` (SLOW_CALCS + deps na `ssee-diamond` pro F-006 anti-kruhovost).

## Datové cesty

- `core-data/calculations/ds-conformal-4d/{calc.py,results.json}`, `plots/R_conformal_vs_nonconformal.png`
