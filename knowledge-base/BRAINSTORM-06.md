# Brainstorming 06 — šestá generace, otevírací tah po VYPOCET-25…29 (2026-06-08)

> **Status oproti BRAINSTORM-05:** páté kolo bylo *capstone* (obě vlajkové linie se potkaly na de
> Sitteru, F-023) a fronta H5g se nyní celá uzavřela: **H5g-1 SUPPORTED** (čistá 4D dS saturace při
> ρ=120, vyšší ρ compute-bound), **H5g-2 PARCIÁLNĚ→UZAVŘENO** (2D area-zákon konstanta *c*≈7.6 robustní
> přes 5× ρ a 3.6× ℓ, ale **silná 1/4 forma vyvrácena** a **4D area-zákon GENUINNĚ NEPŘÍTOMNÝ**, F-031),
> **H5g-3 VYVRÁCENA** (codim-2 hrana = 4D null-tip znaménko, ne 2D roh), **H5g-4 NO-MATCH NA METRICKÉ
> ÚROVNI** (D_K reprodukuje BW boost R²=0.96, ale Connesova vzdálenost nesleduje kauzální vzdálenost
> R²=0.01, F-033), **H5g-5 UZAVŘENA** (B(a) spojitá funkce, B=3 zamítnut na χ²/dof~350, F-030),
> **H5g-6 STRATEGICKÁ** (draft-05 rozhodnut H5g-1). Pět generací filtru: program je teď definovaný
> spíš svými **negativy** než nadějemi. Šestá generace **vede otvory, které ty negativy vytvořily** —
> ne jejich opakováním. Tři nejostřejší otvory: (i) F-033 ukázal, že **správná osa** korespondence
> causal-sets↔NCG je tepelně-časová/KMS, ne metrická; (ii) F-031 nechal **konformně-váhový caveat
> NEVYŘEŠENÝ** — je 4D nepřítomnost area-zákona artefakt non-konformního skaláru? (iii) F-030 dal
> spojitou B(a) křivku, která **volá po analytické předpovědi** z hustoty superradiantních módů.

---

## 1. Teoretická syntéza — co negativy páté generace skutečně otevřely

Pět generací zúžilo program na **dvě betonové linie + jedno index-chráněné jádro**, ale teprve páté
kolo proměnilo tři „nadějné mosty" v **informované negativy**. Informovaný negativ je cennější než
neprozkoumaná zóna: říká nejen *„tudy ne"*, ale i *„tudy ano"* na sousední ose. Poctivá inventura,
co každý z F-029…F-033 zavřel a co tím **odemkl**:

### Otvor 1 (nejostřejší) — F-033: korespondence causal-sets↔NCG žije na TEPELNÉ ose, ne metrické

F-033 je nejinformativnější negativ celé generace. Surogátní modulární Dirac $D_K=\mathrm{sgn}(K)\sqrt{|K|}$
ze SJ modulárního kernelu na 2D slabu (Rindlerova geometrie) **reprodukoval Bisognano-Wichmannovu
boostovou strukturu** (lineární diagonála $R^2=0.955$, robustní přes 5 seedů), ale jeho **Connesova
vzdálenost NEsledovala kauzální/geodetickou vzdálenost** (Pearson 0.10, $R^2=0.0095$; $d_D$ shlukuje
kolem 2.0–2.5 nezávisle na separaci). Optimalizátor ověřen na kanonickém 1D Diracově řetězci
(sousední $d_D=1.0$ přesně) — plochost je **fyzikální vlastnost modulárního Diraca**, ne selhání
solveru.

Co to znamená geometricky: modulární tok JE generátor **boostu** (Bisognano-Wichmann), tedy
**tepelného času** (Connes-Rovelli, gr-qc/9406019; Tomita-Takesaki KMS). Connesova vzdálenost naopak
měří **prostorovou metriku**. F-033 ukázal, že se to ztotožnit nedá — modulární data nesou tepelný
obsah, ne metrický. **To je ale přesně diagnóza, KAM mířit dál.** Místo abychom nutili modulární
Dirac dělat metriku (selže), testujme, zda dělá **termodynamiku**: KMS podmínku, Unruhovu teplotu,
Connes-Rovelliho tepelný čas. Hrana `von-neumann-algebras↔semiclassical-gravity` (partially) i
`von-neumann-algebras↔noncommutative-geometry` (partially) explicitně říkají: *"Bisognano-Wichmann
modular flow reproduces the Unruh effect and the thermal time"* a *"the Connes cocycle and the
time-thermodynamics (thermal time) relation"*. **Tohle ještě nikdy nebylo na causetu numericky
otestováno** — F-033 testoval METRIKU a selhal; TEPELNÁ osa je panenská a F-033 ji předpověděl jako
solidní. → **H6g-1.**

### Otvor 2 — F-031: 4D area-zákon je nepřítomný, ale konformní caveat zůstává NEVYŘEŠEN

F-031 byl poctivý negativ: ve ploché-kauzální + dS-sech² konstrukci 4D area-zákon $S\sim A_{proper}$
**genuinně neexistuje**, protože $S_{full}\sim\rho^{0.997}$ (objemově) zatímco korigovaná kodim-2
plocha $A_{mol}^{codim-2}\sim\rho^{0.494}$ — žádný poměr není ρ-invariantní. Diagnóza byla čistá
(kodim-1 světočáru-tubus vs. kodim-2 entanglement 2-plocha) a nový primitiv
`horizon_molecules_codim2` obnovil $\rho^{0.5}$.

**Ale caveat (a) zůstává výslovně otevřený:** *„4D bezhmotný skalár NENÍ konformně invariantní, repo
nemá přesný zakřivený 4D dS propagátor, takže drift $S_{full}\sim\rho^1$ vs plocha $\sim\rho^{0.5}$
může být ČÁSTEČNĚ tato aproximace; verdikt platí pro TUTO konstrukci, ne nutně pro přesný dS stav."*
Tady je otvor: VYPOCET-19 trik fungoval ve 2D **právě proto, že 2D bezhmotný skalár JE konformně
invariantní** — konformní faktor vypadl z propagátoru a horizont vstoupil jen přes míru sprinklingu.
Ve 4D faktor nevypadne. Je tedy 4D nepřítomnost area-zákona **fyzika** (4D dS opravdu nemá diskrétní
area-zákon v této SJ konstrukci), nebo **artefakt** toho, že počítáme Green funkci na ploché kauzální
struktuře místo na zakřiveném dS propagátoru? Rozhodnout to lze **konformní vazbou**: 4D skalár s
$\xi R\phi^2$ členem ($\xi=1/6$) JE konformně invariantní, a na dS pozadí $R=12/\ell^2$ konst. dává
efektivní hmotu $m_{eff}^2=\xi R$, kterou lze v link-matici Green funkci implementovat jako masivní
propagátor. Pokud konformně-vázaný 4D skalár area-zákon **obnoví**, byla nepřítomnost artefakt;
pokud ne, je 4D nepřítomnost robustní fyzika. → **H6g-2.**

### Otvor 3 — F-030: spojitá B(a) křivka volá po analytické predikci z hustoty módů

F-030 uzavřel H5g-5 daty: $B(a)$ je spojitá klesající funkce (6.10→2.54 přes $a=0.3$→0.99,
$dB/da=-2.20$, $z=-33.6$), $B=3$ rozhodně zamítnut, BTZ ($\Omega\sim r^{-2}$) systematicky pod Kerr
($\Omega\sim r^{-3}$). To je teď **fenomenologie bez teorie**. Otvor: $B$ je definováno jako exponent
v $W_{sr}\sim\Omega(r)^B$, kde $W_{sr}$ je váha SJ pozitivního podprostoru v superradiantním klínu
$\omega(\omega-k\Omega)<0$. Hustota módů v tom klínu je **počitatelná** — je to objem oblasti
$\{(\omega,k):\omega(\omega-k\Omega)<0\}$ vážený occupation mapou $P(\omega,k)$. Pro malé $\Omega$ je
klín tenký a jeho míra škáluje mocninně s $\Omega$; exponent té mocniny je predikce pro $B$. To dává
**analytickou předpověď $B(\Omega)$ z geometrie klínu × spektrální hustoty**, srovnatelnou se 4D
Teukolského zesilovacím koeficientem $|R_{lm}|^2$ (kde superradiance $\propto(\omega-m\Omega_H)$).
Pokud predikovaný exponent reprodukuje měřený trend $dB/da<0$ a BTZ-Kerr gap z asymptotiky, povýší to
draft-01 z „Ω-zákon s naměřeným B" na „Ω-zákon s **odvozeným** B". → **H6g-3.**

### Otvor 4 — standing directive: Λ jako Poissonův shot-noise, přerámovaný PROTI F-005

Trvalá direktiva: $\delta\Lambda\sim 1/\sqrt{V}\sim H^2$ z počítání atomů prostoročasu
($N\sim V/\ell_P^4$, $\delta N\sim\sqrt{N}$). **Napětí s F-005 je reálné a musí se respektovat:**
F-005 vyvrátil **silnou** formu — že tři mechanismy ($\kappa_{Sorkin}$, $\kappa_{EDT}$, CosMIn) sdílejí
JEDEN prefaktor (mismatch 139.6×). Ale F-005 testoval **střední hodnotu** $\langle\Lambda\rangle\ell_P^2
=\kappa/\sqrt{V}$ a její prefaktor. Shot-noise hypotéza je o **fluktuačním spektru** (varianci), ne o
střední hodnotě. Sorkinova everpresent-Λ je explicitně $\Lambda\sim\pm 1/\sqrt{V}$ — to ZNAMÉNKO ±
je signatura fluktuace, ne mean. Přerámování: netestovat prefaktor (to F-005 zabil), ale **distribuci**
— je $\delta N/N$ na causetovém sprinklingu skutečně $\sim 1/\sqrt{N}$ (Poisson) a je tato fluktuace
**Lorentz-invariantní** (nezávislá na boostu sprinklovacího rámce)? To je čistě geometrický test
sprinklingu, který F-005 NEzkoušel (F-005 srovnával prefaktory ze tří hotových čísel; tady měříme
distribuci přímo). Diskriminátor: $\mathrm{Var}(N)/\langle N\rangle\to 1$ (Poisson) a invariance pod
boostem $\Lambda=\mathrm{diag}(e^\eta,e^{-\eta})$. Pokud variance škáluje jinak než Poisson, padá i
slabá forma; pokud Poisson + boost-invariance drží, je to **falzifikovatelná predikce fluktuačního
spektra** nezávislá na prefaktoru. → **H6g-4.**

### Zbývající bílá místa pro doplňkové hypotézy

`causal-sets↔asymptotic-safety` (barely, SYNTEZA-02 lovecký #1) zůstává **nedotčená VYPOCETem** —
máme spektrální engine (F-001) + BD spektrum (F-012), ale α-drift varuje. `black-holes-information
↔causal-sets` (barely/partially) je teď **2D vyřešená** (F-028 area-zákon), ale 4D Dou-Sorkin
molekula nikdy nebyla spojena s **horizontovou-entropie FLUKTUACÍ** (Sorkinova order-by-disorder
varianta). → **H6g-5, H6g-6, H6g-7** jako doplňkové.

**Organizační princip šesté generace** (through-line pokračuje): páté kolo ukázalo, že
„vlastnosti = odpovědi na otázky" má **ostrou hranici** — F-033 ji vytáhl explicitně: SJ modulární
data odpovídají na otázku *„jaký je tepelný čas?"* (boost, KMS), NE na otázku *„jaká je vzdálenost?"*
(metrika). Šestá generace tu hranici **respektuje a využívá**: testuje každou hypotézu na té ose, na
které data žijí, ne na té, kde už víme, že selhávají.

---

## 2. Nové hypotézy a extrapolace (PROPOSALS — vstupují do findings až po compute + editorial)

Sedm hypotéz šesté generace. **Všechny jsou návrhy, ne nálezy** — do `findings.json` /
`connections.json` vstoupí teprve po výpočtu a editorial rozhodnutí (stejná disciplína jako pět
předchozích generací). Každá: tvrzení (falzifikovatelné), opora (F-ID), konkrétní test pro `lib/toe`
(geometrie / ρ / N / seedy / observable / diskriminátor / tier proveditelnosti), priorita, riziko.

Tier proveditelnosti: **[odpoledne]** = varianta hotového kódu, dense eigh $N\le 2500$;
**[sparse]** = `sj_state_sparse`+`idelta_operator_2d`, $N\le 12000$; **[read-first]** = vyžaduje
rešerši/novou mašinérii před compute.

---

### H6g-1 — Modulární Dirac reprodukuje KMS / tepelný čas, ne metriku (správná osa causal-sets↔NCG)

> **STATUS (kolo 16, VYPOCET-30, F-034): PARTIAL — tepelná/KMS osa má kvalitativní datovou oporu. beta_KMS=1 strojová přesnost (1.9e-16), rho-invariantní boost diagonála R2=0.953 CV=2.7 %, non-Rindler kontroly selhávají (R2=0.05/0.09). Absolutní Unruhova 2pi NEobnovena (ratio=0.786). Verdikt: partial (kvalitativní pozitiv na tepelné ose, kvantitativní Unruh chybí).**

> **STATUS (kolo 18, VYPOCET-32, F-036): INFORMOVANY-NEGATIV-TAUTOLOGIE — netautologický flagship test (H6g-1b) selhal kvantitativně na obou nezávislých invariantech: zákonný exponent p_E=0,720 (BW +1 nečteno, deficit 28 %), koeficient 9,58 (off 52 % od 2*pi). Rho-invariantní boostová diagonála strukturálně solidní (sklon 29,2, R2=0,969, CV 1,7 %). Most NCG<->semiklasika je most struktury, NE teploty. Hrana zůstává barely. Edge do connections.json NEPROPAGOVÁNA (audit). Příští krok: non-surogátní Dirac z geometrického Killingova boostu.**

**(jádro: F-033 otvor — D_K dělá boost/KMS, ne vzdálenost; testuj termodynamiku, ne geometrii)**
**Priorita: high (nejvyšší ROI generace — instancuje barely hranu na ose, kde F-033 předpověděl PASS).**

- **Tvrdí:** týž surogátní modulární Dirac $D_K$, jehož Connesova vzdálenost selhala na metrice
  (F-033), **reprodukuje tepelně-časový obsah** korespondence causal-sets↔NCG. Konkrétně: modulární
  tok $\sigma_t=e^{iKt}\cdot e^{-iKt}$ generovaný kernelem $K$ (a stejně i $D_K^2=|K|$) splňuje
  **KMS podmínku** s tepelnou periodou $\beta=2\pi$ (Bisognano-Wichmann: boost má Unruhovu teplotu
  $T=1/2\pi$ v jednotkách boostového rapidity) a **modulární dvoubodová funkce**
  $G_\beta(x,y;t)=\langle\phi(x,t)\phi(y,0)\rangle$ na slabu je periodická v imaginárním čase s
  periodou $2\pi$. Predikce: spektrum $K$ je **rovnoměrně rozprostřené** (boostové vlastní hodnoty
  $\sim$ rapidity, lineární v poloze podél boostu — přesně to F-033 viděl jako lineární diagonálu
  $R^2=0.96$), a **Unruhova teplota odečtená z modulárního spektra** ($T_{mod}$ z KMS sklonu
  $\ln[\mu/(\mu-1)]$ vs. boostový parametr) konverguje k $1/2\pi$ nezávisle na ρ a N. To je osa, na
  které F-033 dal PASS (diagonála lineární), zde zostřená na **kvantitativní termodynamiku**.
- **Opora (F-ID):** F-033 (D_K reprodukuje BW boost lineární diagonála $R^2=0.955$ robustní; verdikt
  *„modulární tok je generátor boostu / tepelného času Connes-Rovelli, NIKOLI Diracova prostorová
  metrika — boostová/tepelně-časová osa korespondence je SOLIDNÍ"*). F-011 (modular-hamiltonian TOP
  HUB). Hrana `von-neumann-algebras↔semiclassical-gravity` (partially): *„Bisognano-Wichmann modular
  flow reproduces the Unruh effect and the thermal time"*. Hrana `von-neumann-algebras↔
  noncommutative-geometry` (partially): *„Connes cocycle and the time-thermodynamics (thermal time)
  relation are foundational results of NCG imported into quantum gravity"*. Hrana `causal-sets↔NCG`
  (barely, INSTANCOVANÁ F-033 jako informovaný negativ na metrice — tepelná osa nedotčená).
- **Test:** **Geometrie** — 2D slab $T=0.30<L=1.0$, řez $O=\{x>0\}$ (Rindler, modulární tok = BW
  boost) — IDENTICKÝ setup jako F-033/VYPOCET-29, takže `core-data/calculations/spectral-triple-modular/`
  je hotová kostra. **Objekt:** netruncovaný modulární kernel $K$ z `entropy.modular_kernel(W, iDelta,
  sub_idx, kappa=None)`; tepelný čas přes $\sigma_t$. **Observable:** (a) **KMS test** — spočti
  modulární dvoubodovou funkci $G(x,y;t)$ podél boostové orbity a ověř periodicitu v imaginárním
  čase ($G_\beta(t+i\beta)=G_\beta(t)$) s $\beta=2\pi$; (b) **Unruhova teplota** — z modulárních
  energií $\epsilon=\ln[\mu/(\mu-1)]$ (Casini-Huerta) jako funkce boostové souřadnice $\eta=\mathrm{arctanh}$,
  odečti $T_{mod}=d\eta/d\epsilon$ a srovnej s $1/2\pi\approx 0.159$; (c) **spektrální planost** $K$
  — vlastní hodnoty rovnoměrně husté (boostový spektrum), kontrast s metrickým Diracem (kde by byly
  shlukované). **Diskriminátor:** $T_{mod}\to 1/2\pi$ (do 10–20 %) nezávisle na ρ, N **A** KMS
  periodicita drží → **modulární Dirac JE NCG-jazyk Unruhova/tepelného času** (datová hrana causal-sets
  ↔NCG na tepelné ose, POZITIVNÍ); $T_{mod}$ driftuje s ρ nebo KMS selže → modulární data nenesou ani
  tepelný obsah a F-033 negativ se rozšiřuje. **N:** $N=1200$, 5–10 seedů, dense eigh — **[odpoledne]**,
  varianta hotového VYPOCET-29 kódu (kernel už máme, přidává se KMS/teplota analýza).
- **Co by dalo:** **první POZITIVNÍ datová hrana causal-sets↔NCG** v grafu (F-033 dal negativ na
  metrice; tohle by dalo pozitiv na termodynamice). Sjednotilo by linii B (von Neumann) s NCG přes
  Connes-Rovelliho tepelný čas — through-line vrstva B by dostala NCG/Unruh formulaci. Doplnilo by
  hranu `von-neumann-algebras↔semiclassical-gravity` z partially na well daty.
- **Riziko:** modulární „tepelný čas" na konečném causetu je trend, ne přesná KMS (konečné N porušuje
  spojitý modulární tok). $T_{mod}=1/2\pi$ je analytická BW hodnota pro spojitý Rindler — diskrétní
  korekce mohou posunout o $O(1/\sqrt{N})$. Záloha: měř *trend* $T_{mod}(\rho)$ a extrapoluj
  $\rho\to\infty$, ne absolutní hodnotu při jednom ρ. Pokud i tepelná osa driftuje, je to čistý
  negativ (modulární surogát nenese vůbec geometrický obsah), stále publikovatelné jako uzavření
  hrany.

---

### H6g-2 — Konformně-vázaný 4D skalár obnoví dS area-zákon (rozhodne caveat F-031)

> **STATUS (kolo 18, VYPOCET-33, F-037): UZAVRENA NEGATIVEM — konformní vazba xi=1/6 NEOBNOVI 4D dS area-zákon. R' drift +0,386 identický pro xi=1/6 i xi=0 (CV 0,275 vs 0,276), S_full conf/massless=1,0001. Caveat (a) F-031 (xi-část) VYRESEN: 4D absence area-zákona je robustní fyzika, ne konformně-vážový artefakt. H6g-2 blokátor (masivní SJ well-definedness) odstraněn (pairing 8,4e-15, Wightman PSD 1e-15). F-031 stojí silněji. Korespondence: negative.**

**(jádro: F-031 nevyřešený konformní caveat — je 4D nepřítomnost area-zákona artefakt non-konformního skaláru?)**
**Priorita: high (rozhoduje, zda F-031 negativ je fyzika nebo aproximace — přímý draft-04/05 dopad).**

- **Tvrdí:** 4D nepřítomnost area-zákona (F-031: $S_{full}\sim\rho^{0.997}$ objemově, $A_{codim-2}
  \sim\rho^{0.494}$, žádný ρ-invariantní poměr) je **artefakt non-konformního skaláru**, ne robustní
  fyzika. Příčina: VYPOCET-19 trik fungoval ve 2D **právě proto**, že 2D bezhmotný skalár je konformně
  invariantní — konformní faktor $\Omega^2=\mathrm{sech}^2(r^*/\ell)$ vypadl z propagátoru a dS vstoupil
  jen přes míru sprinklingu (čistý area-zákon). Ve 4D bezhmotný skalár konformně invariantní NENÍ,
  takže faktor zůstává v propagátoru a kazí škálování $S_{full}$. **Konformní vazba** $\xi R\phi^2$ s
  $\xi=1/6$ činí 4D skalár konformně invariantním; na dS $R=12/\ell^2$ je konstantní, takže
  $m_{eff}^2=\xi R=2/\ell^2$ je konstantní efektivní hmota, implementovatelná v link-matici Green
  funkci jako masivní 4D propagátor (Klein-Gordon s $m^2=2/\ell^2$). Predikce: konformně-vázaný 4D
  skalár dá $S_{full}\sim\rho^{0.5}$ (area-zákon) na dS-sech² geometrii, ρ-invariantní poměr
  $S_{full}/A_{codim-2}\to$ konst., zatímco bezhmotný (testovaný F-031) ne.
- **Opora (F-ID):** F-031 (caveat (a) VÝSLOVNĚ: *„4D bezhmotný skalár NENÍ konformně invariantní…
  verdikt platí pro TUTO konstrukci, ne nutně pro přesný dS stav"*; korigovaná $A_{codim-2}\sim
  \rho^{0.494}$ = vlastní-plošný cíl). F-023 (2D konformní trik FUNGOVAL — 2D skalár je konformně
  invariantní). F-019 (4D slab area-zákon $S\sim N^{0.55}\approx\sqrt N$ s $n_{max}=2N^{3/4}$ —
  bezhmotný, plochá geometrie, area-zákon DRŽÍ; rozdíl od dS musí být v zakřivení/míře).
  F-016 (4D slab = čistý Hadamard, area-zákon $S\sim L^{2.00}$). Hrana `causal-sets↔holography-adscft`
  (conflict): *„Dou-Sorkin horizon-molecule counting reproduces S=A/4"* — area-zákon JE očekáván,
  takže jeho nepřítomnost ve F-031 je překvapení k vysvětlení.
- **Test:** **Geometrie** — 4D dS statická záplata, `causet.sprinkle_ds_static_patch4d(N, rng, l,
  rstar_box, t_extent, x_perp_half)` (hotový primitiv) + plochá kontrola. **Objekt:** masivní 4D
  link-matice Green funkce s $m_{eff}^2=\xi R=2/\ell^2$ — `causet.green_retarded_4d` rozšířený o
  hmotný člen (Klein-Gordon retardovaný propagátor; nový lib parametr `mass` nebo nový primitiv
  `green_retarded_4d_massive`), pak `pauli_jordan`+`sj`. **Observable:** $S_{full}$ (truncovaná SSEE
  s $n_{max}=2N^{3/4}$, F-019 regulátor) a $A_{codim-2}$ (`horizon_molecules_codim2`, k_tube=1.5) jako
  funkce ρ; poměr $R'=S_{full}/A_{codim-2}$. **Srovnání:** konformně-vázaný ($\xi=1/6$) vs. bezhmotný
  ($\xi=0$, F-031 baseline) na shodné dS geometrii. **Diskriminátor:** konformně-vázaný $R'$
  ρ-invariantní (CV<0.1, $d\ln R'/d\ln\rho\approx 0$) → 4D nepřítomnost byla artefakt, area-zákon se
  OBNOVÍ konformní vazbou; konformně-vázaný $R'$ stále driftuje ($\rho^{+0.5}$ jako F-031) → 4D
  nepřítomnost je **robustní fyzika** nezávislá na konformní vazbě, F-031 stojí silněji.
  **N:** Stage B rozsah F-031, $\rho\in\{120,240,480\}$, dense $N\le 1920$, 5 seedů — **[odpoledne]**
  na nižší ρ, **[sparse]** pro $\rho>480$. Hlavní práce = masivní Green funkce (jinak hotová
  mašinérie).
- **Co by dalo:** kdyby konformní vazba area-zákon obnovila, byl by to **diskrétní first-principles
  4D dS area-zákon** (silnější než F-028 2D) a otevřel by H5g-2 znovu na 4D s vyřešeným caveatem —
  vlajkový výsledek. Kdyby ne, **uzamkne F-031** jako robustní fyziku (4D dS opravdu nemá diskrétní
  area-zákon v SJ konstrukci, nezávisle na konformní vazbě) — silný, čistý negativ pro draft-04.
  Tak jako tak rozhodne otevřený caveat, který blokuje 4D závěr.
- **Riziko:** masivní propagátor mění SJ konstrukci — $iΔ$ pro masivní pole má jiné spektrum a SJ
  pozitivita se musí ověřit (well-definedness). Efektivní hmota $m_{eff}^2=2/\ell^2$ je
  $O(1)$ v dS jednotkách, ne malá — propagátor může být dominantně masivní (krátký dosah), což deformuje
  entanglement strukturu jinak než zakřivení. Druhotně: i konformně-vázaný skalár na ploché kauzální
  struktuře není přesný dS propagátor (caveat se jen ZMENŠÍ, nezmizí). Záloha: pokud masivní SJ není
  well-defined, je to read-first (potřebuje analytickou kontrolu masivního dS SJ stavu).

---

### H6g-3 — Analytická predikce B(Ω) z míry superradiantního klínu × spektrální hustoty

**(jádro: F-030 spojitá B(a) křivka volá po teorii — odvoď exponent z geometrie klínu, ne fituj)**
**Priorita: medium-high (povýší draft-01 z fenomenologie na odvozenou predikci; částečně analytická).**

- **Tvrdí:** spojitý exponent $B$ v $W_{sr}\sim\Omega(r)^B$ (F-030: 6.10→2.54, $dB/da=-2.20$) je
  **odvoditelný analyticky** z geometrie superradiantního klínu $\{(\omega,k):\omega(\omega-k\Omega)<0\}$
  vážené spektrální occupation mapou $P(\omega,k)$ SJ pozitivního podprostoru. Pro malé $\Omega$ je
  klín tenký výseč v $(\omega,k)$ rovině, jehož míra (vážená $P$) škáluje jako $\Omega^B$ s exponentem
  **daným okrajovým chováním $P(\omega,k)$ u $\omega\to 0$** (IR hrana spektra). Konkrétně: pokud
  $P(\omega,k)\sim\omega^{p}|k|^{q}$ u počátku, integrace přes klín dává $W_{sr}\sim\Omega^{B}$ s
  $B=B(p,q)$ analyticky. Predikce: (i) $B$ klesá s rostoucím $\Omega$ (klín se otevírá → menší
  relativní citlivost), reprodukuje $dB/da<0$; (ii) BTZ ($\Omega\sim r^{-2}$, mělčí asymptotika) má
  jiný efektivní $(p,q)$ než Kerr ($\Omega\sim r^{-3}$) → systematicky nižší $B$ (F-030 BTZ-Kerr gap
  −1.1/−0.55 vysvětlen asymptotikou IR hrany). To je **diskrétní analog 4D Teukolského** zesilovacího
  koeficientu, kde superradiance $\propto(\omega-m\Omega_H)$ a amplifikace $|R_{lm}|^2$ závisí na
  hraničních podmínkách v asymptotice.
- **Opora (F-ID):** F-030 (B(a) spojitá, $dB/da=-2.20$ $z=-33.6$, B=3 zamítnut χ²/dof~350, BTZ pod
  Kerr; *„B je dán hustotou superradiantních módů v klínu $\omega(\omega-k\Omega)<0$, která škáluje s
  asymptotikou metriky"* — F-030 to NAVRHL jako mechanismus, nikdy neodvodil). F-018 ($\Omega(r)$ zákon
  robustní log-log; $A_W$ near-zone $\sim r^{-2.75}\approx r^{-3}$ tracking $|\Omega|$). F-013
  (frame-dragging v eigenvektorech, ne spektru; $A_{caus}/A_W$ odvozeno z 1. principů — precedent pro
  analytické odvození SJ veličiny). `superradiant_weight` v `lib/toe/sj.py` má hotovou occupation
  mapu $P(\omega,k)$ — surovinu pro analytickou hustotu.
- **Test:** **Analytická část** — odvoď $B(p,q)$ integrací $\int_{wedge}P(\omega,k)\,d\omega\,dk$ s
  parametrizovaným $P\sim\omega^p|k|^q$ u IR hrany (symbolicky přes sympy, jako `ncg.py` exaktní
  aritmetika). **Numerická validace** — z hotových `sj-kerr-b-scan` dat (F-030) extrahuj **změřenou**
  occupation mapu $P(\omega,k)$ (`superradiant_weight` vrací mapu), fituj IR exponenty $(p,q)$ u
  $\omega\to 0$, dosaď do analytického $B(p,q)$, srovnej s naměřeným $B(a)$. **Geometrie:** Kerr
  ekvatoriální $a=0.3…0.99$ (hotová data) + BTZ $J=0.6,0.9$. **Observable:** predikované $B_{pred}(a)$
  z $(p,q)$ vs. naměřené $B(a)$ z F-030. **Diskriminátor:** $B_{pred}(a)$ reprodukuje trend
  $dB/da<0$ A BTZ-Kerr gap (do CI F-030) → **B je odvozen, ne fitován** (draft-01 predikce); $B_{pred}$
  nesouhlasí → mechanismus „hustota klínu" je nesprávný a B zůstává fenomenologický fit.
  **N:** žádný nový sprinkling — re-analýza hotových `sj-kerr-b-scan/results.json` + symbolická
  derivace. **[odpoledne]** (read-analyze hotová data) až **[read-first]** (pokud IR hrana není čistá).
- **Co by dalo:** povýšilo by draft-01 §4.2 z „naměřené $B(a)$ s CI" na „**odvozené** $B(a)$ z hustoty
  módů, validované daty" — rozdíl mezi fenomenologií a teorií. Spojilo by SJ superradianci s analytickou
  superradiantní amplitudou (Teukolsky-like), most `semiclassical-gravity↔causal-sets` posílen
  teoretickým obsahem.
- **Riziko:** occupation mapa $P(\omega,k)$ u IR hrany může být zašuměná (konečné N, MC overlap) —
  fit $(p,q)$ nepřesný. Klín není přesný výseč (occupation mapa má strukturu mimo jednoduchou mocninu).
  $B$ nemusí být čistá funkce $(p,q)$ (vyšší momenty $P$ přispívají). Pokud analytika nereprodukuje
  ani trend, je to negativní výsledek o mechanismu (ale B(a) data F-030 stojí nezávisle). Nejnižší
  výpočetní riziko (žádný nový běh), ale střední riziko, že analytika nevyjde čistě.

---

### H6g-4 — Λ shot-noise jako Lorentz-invariantní fluktuační spektrum sprinklingu (přerámováno PROTI F-005)

> **STATUS (kolo 16, VYPOCET-31, F-035): SURVIVES — Poissonův shot-noise přežívá F-005 na variance/boost-kovariantní ose. Fanův faktor F=0.9986 +/-0.0112 při 16000 seedech (0.13 sigma od 1), delta_Lambda~V^{-0.484±0.006} (R2=0.999), boost-invariantní Var(N) max z=0.70, mřížkový kontrast 5.13x. Mean-prefaktor (F-005) nevzkříšen. Verdikt: korespondence survives (supported).**

**(jádro: standing directive — δΛ~1/√V jako VARIANCE, ne mean; F-005 zabil prefaktor, ne distribuci)**
**Priorita: medium (vysoká novost, čistě geometrický test; opatrné přerámování po F-005 negativu).**

- **Tvrdí:** kosmologická konstanta jako Poissonův shot-noise počítání atomů prostoročasu je
  **fluktuační spektrum** (variance), ne střední hodnota — a v této formě **přežívá F-005**. F-005
  vyvrátil SILNOU formu (jeden sdílený prefaktor $\kappa$ mezi Sorkin/EDT/CosMIn, mismatch 139.6×),
  testoval $\langle\Lambda\rangle\ell_P^2=\kappa/\sqrt V$. Shot-noise je o **distribuci**: počet atomů
  $N$ v minulém 4-objemu $V$ je Poissonovský ($\langle N\rangle=\rho V$, $\mathrm{Var}(N)=\langle N\rangle$),
  takže $\delta N/\langle N\rangle=1/\sqrt{\langle N\rangle}\sim 1/\sqrt{V}$, a Sorkinova
  $\Lambda\sim\pm 1/\sqrt V$ je přesně tato **fluktuace se znaménkem ±** (mean i znaménko fluktuace),
  ne deterministický mean. Falzifikovatelná predikce: (i) na causetovém Poisson-sprinklingu je
  $\mathrm{Var}(N)/\langle N\rangle\to 1$ (přesný Poisson) přes rozsah objemů; (ii) tato fluktuace je
  **Lorentz-invariantní** — pod boostem sprinklovacího rámce $\Lambda(\eta)=\mathrm{diag}(e^\eta,e^{-\eta},
  1,1)$ zůstává $\mathrm{Var}(N)/\langle N\rangle=1$ a nezávisí na rapiditě $\eta$ (na rozdíl od
  mřížkové diskretizace, kde by boost porušil počet). To je signatura, kterou F-005 NEtestoval (F-005
  srovnával tři hotová čísla prefaktorů; tady měříme distribuci a její boost-kovarianci přímo).
- **Opora (F-ID):** F-005 (ZABÍJÍ silnou formu: $\kappa_{Sorkin}/\kappa_{EDT}=139.6$, mean-prefaktor
  mismatch — **ale netestoval varianci/distribuci ani boost-invarianci**). Hrana `causal-sets↔
  cosmological-constant-fluctuation` (partially): *„Sorkin's everpresent-Lambda… $\Lambda\sim 1/\sqrt V
  \sim 10^{-120}$, made in 1987… the only prediction-in-advance from any QG approach"*. Hrana
  `causal-sets↔experimental-tests` (partially): *„CST's exact Lorentz invariance (Poisson sprinkling)"*
  — Lorentz-invariance sprinklingu je dokumentovaná, ale fluktuace $N$ pod boostem nikdy přímo neměřena.
  `causet.sprinkle_*` + `causal_matrix` dávají přesný Poisson sprinkling — surovinu.
- **Test:** **Geometrie** — 4D kauzální diamant/box (`sprinkle_box4d`) jako proxy minulého světelného
  kužele; spočti $N$ v podobjemech, opakuj přes mnoho seedů. **Boost test:** aplikuj Lorentzův boost
  $\Lambda(\eta)$ na souřadnice PŘED sprinklingem vs. PO sprinklingu a srovnej $\mathrm{Var}(N)$.
  **Observable:** (a) $\mathrm{Var}(N)/\langle N\rangle$ jako funkce $\langle N\rangle$ (rozsah objemů)
  — Poisson predikuje konstantu 1; (b) tatáž veličina pod boostem $\eta\in[0,2]$ — predikce: nezávislá
  na $\eta$; (c) **diskriminátor proti mřížce:** mřížková kontrola (pravidelná 4D mřížka místo Poissonu)
  — $\mathrm{Var}(N)$ pod boostem POROŠÍ (Lorentzova kontrakce mění počet), zatímco Poisson ne.
  **Diskriminátor:** Poisson $\mathrm{Var}(N)/\langle N\rangle=1\pm\epsilon$ boost-invariantní →
  shot-noise je Lorentz-invariantní fluktuační spektrum (slabá forma Λ-fluktuace přežívá F-005);
  $\mathrm{Var}/\langle N\rangle\ne 1$ nebo boost-závislé → i slabá forma padá. **N:** žádný eigh
  problém — jen počítání bodů, $N$ do $10^5$–$10^6$, stovky seedů. **[odpoledne]** (čistě geometrické,
  nejlevnější výpočetně z celé generace; není to maticový problém).
- **Co by dalo:** **rehabilitovalo by Λ-fluktuační linii** v přerámované (variance, ne prefaktor)
  formě, kterou F-005 nezabil — slabá forma jako Lorentz-invariantní fluktuační spektrum je
  falzifikovatelná a páková (hrana `causal-sets↔cosmological-constant-fluctuation`, Sorkinova vlajková
  predikce). Most k `swampland` (dynamická dark energy / TCC rezonance) a `quantum-cosmology`.
- **Riziko:** $\mathrm{Var}(N)/\langle N\rangle=1$ je **triviální vlastnost Poissonova procesu** —
  test může být tautologický (sprinkling JE Poisson z definice). Netriviální obsah je až (ii)
  boost-invariance a (iii) kontrast s mřížkou; pokud se test zredukuje na „Poisson je Poisson",
  novost mizí. Hlubší riziko: $\delta\Lambda\sim 1/\sqrt V$ vyžaduje, aby fluktuace $\delta N$
  generovala $\delta\Lambda$ přes konkrétní mechanismus (Sorkinova konjugace $\Lambda$↔$V$), který je
  sám hypotéza — tento test ověří jen Poissonovskou statistiku $N$, ne celý řetězec $N\to\Lambda$.
  **Musí být explicitní:** testuje fluktuaci POČTU atomů a její boost-kovarianci, ne plnou
  everpresent-Λ dynamiku. To je nutná, ne postačující podmínka.

---

### H6g-5 — BD path integral realizuje AS-like fixní bod (nedotčená barely, SYNTEZA-02 lovecký #1)

**(jádro: causal-sets↔asymptotic-safety, nedotčená VYPOCETem; máme spektrální engine + BD spektrum)**
**Priorita: medium (vysoká novost, ale α-drift F-012 varuje; compute-target).**

- **Tvrdí:** Benincasa-Dowker (BD) d'Alembertián na causetu definuje **efektivní RG tok** se
  spektrální dimenzí $d_s(\sigma)$ jako funkcí škály $\sigma$, jejíž UV chování realizuje
  **asymptoticky-bezpečný-podobný fixní bod** se srovnatelnými kritickými exponenty jako CDT/FRG.
  Otázka už nezní „je $d_s\to 2$?" (víme z F-001/F-002, že d'Alembertián probe ano), ale **„má BD
  $d_s(\sigma)$ flow tvar $\eta_N$ škálování AS fixního bodu, nebo jen monotónní redukci?"**.
  Falzifikovatelná forma: $d_s(\sigma)$ z BD spektra fitnutá na AS-FRG predikci $d_s=4/(1+...)$ má
  konzistentní kritický exponent $\theta$ vs. CDT $d_s$-flow.
- **Opora (F-ID):** F-001/F-002 (validovaný spektrální engine; $d_s$ probe-dependentní, d'Alembertián
  dává $d_s\to 2$). F-012 (BD d'Alembertián opravuje tvar 4D spektra na power-law; **ALE α-drift
  $+1.28$ nekonvergován při $N\le 3000$, cond(B) roste do $2\times 10^{10}$**). Hrana `causal-sets↔
  asymptotic-safety` (barely): *„Whether the BD action / causal-set path integral realizes an
  asymptotically-safe-like RG fixed point is essentially unexplored"*. SYNTEZA-02 lovecký žebříček #1.
- **Test:** **Geometrie** — 4D box sprinkling (`sprinkle_box4d`), BD d'Alembertián
  (`bd_smeared_dalembertian_inverse`, $\epsilon$ smearing). **Objekt:** spektrum BD operátoru → return
  probability $P(\sigma)$ → $d_s(\sigma)=-2\,d\ln P/d\ln\sigma$ (`spectral.spectral_dimension_flow`).
  **Observable:** $d_s(\sigma)$ flow přes škály, fit na AS-like formu, kritický exponent. **Diskriminátor:**
  $d_s(\sigma)$ flow má fixní-bod strukturu konvergentní v N → AS-like; flow driftuje s N (α-drift
  nezkonvergován) → fixní bod není dosažitelný při těchto N, negativní/inconclusive. **N:** $N\le
  12000$ **[sparse]** (eigsh na BD spektru), ale F-012 varuje, že konvergence nemusí nastat —
  $\epsilon$ smearing nutný pro podmíněnost.
- **Co by dalo:** první **datová hrana causal-sets↔asymptotic-safety** (dosud čistě barely shared-math).
  I negativní výsledek (fixní bod nekonverguje při $N\le 12000$) je publikovatelný diskriminátor
  (CDT-FRG vs. BD-causet rozdíl).
- **Riziko (vysoké, dokumentované):** F-012 už ukázal α-drift +1.28 nekonvergován a cond(B)$\to 2e10$
  — fixní bod **nemusí být dosažitelný** při $N\le 12000$. Toto je nejrizikovější compute generace:
  velká šance na inconclusive (ne čistý negativ, ne pozitiv). Zařadit až po levnějších [odpoledne]
  testech.

---

### H6g-6 — 4D Dou-Sorkin horizontová entropie z FLUKTUACE molekul (order-by-disorder), ne z mean count

> **STATUS (kolo 18, VYPOCET-34, F-038): UZAVRENA NEGATIVEM (refuted-direction) — Var(N_mol)~rho^0,656, bootstrap CI95 [0,575, 0,745] vylučuje plochu rho^0.5 i objem rho^1.0; super-Poisson (Fano 3,72->5,30, CI68 vylučuje 0). Paralela k F-035 (Poisson atomy) NEDRZI — molekuly jsou korelované (near-null clustering). Druhý nezávislý negativ k F-031: ani mean, ani variance 4D area-zákon nedají. Korespondence: negative.**

**(jádro: black-holes-information↔causal-sets, 2D vyřešena F-028, 4D mean-count zabit F-031 → zkus FLUKTUACI)**
**Priorita: medium (otvor po F-031 negativu: mean-count selhal, ale Sorkin order-by-disorder je o VARIANCI).**

- **Tvrdí:** ve 4D, kde **střední** Dou-Sorkin molekulový počet nedává area-zákon konstantu (F-031:
  $S_{full}\sim\rho^{1}$ vs $A_{codim-2}\sim\rho^{0.5}$, žádný poměr ρ-invariantní), může **fluktuace**
  (variance) molekulového počtu přes horizont sledovat plochu. Sorkinova „order-by-disorder" /
  horizon-entropy-fluctuation varianta tvrdí $\mathrm{Var}(N_{mol})\sim A$ (ne $\langle N_{mol}\rangle
  \sim A$). Predikce: $\mathrm{Var}(N_{mol}^{codim-2})/\langle N_{mol}\rangle$ nebo přímo
  $\mathrm{Var}(N_{mol})$ škáluje jako $\rho^{0.5}$ (plocha), i když mean selhal — protože fluktuace
  počtu blízko-null linků na 2-ploše je řízena plochou, ne objemem. To je **paralela k H6g-4** (tam Λ
  z variance $N$, tady $S$ z variance $N_{mol}$).
- **Opora (F-ID):** F-031 (4D mean-count $A_{codim-2}\sim\rho^{0.494}$ = vlastní-plošný cíl, ALE poměr
  $S/A$ driftuje — mean-cesta vyčerpána; nový primitiv `horizon_molecules_codim2` JE k dispozici).
  F-028/F-029 (2D area-zákon konstanta robustní — 2D mean funguje, 4D ne). Hrana `black-holes-information
  ↔causal-sets` (barely): *„Sorkin spacetime entropy, order-by-disorder counting of causal links across
  horizon… horizon-entropy FLUCTUATIONS"* — výslovně FLUKTUACE, ne mean. Hrana `emergent-gravity↔
  causal-sets` (barely): *„counting causal links (Dou-Sorkin) gives S proportional to A"*.
- **Test:** **Geometrie** — 4D dS statická záplata (`sprinkle_ds_static_patch4d`) + plochá kontrola.
  **Objekt:** `horizon_molecules_codim2` (return_diagnostics=True) přes mnoho seedů → distribuce
  $N_{mol}$. **Observable:** $\mathrm{Var}(N_{mol}^{codim-2})$ a $\mathrm{Var}/\langle N_{mol}\rangle$
  jako funkce ρ. **Diskriminátor:** $\mathrm{Var}(N_{mol})\sim\rho^{0.5}$ (plocha) ρ-invariantní poměr
  k $A_{proper}$ → **horizontová entropie z fluktuace** (4D order-by-disorder area-zákon, kde mean
  selhal); $\mathrm{Var}$ škáluje jinak (např. $\rho^1$ jako mean) → ani fluktuace nedá 4D area-zákon,
  F-031 negativ se rozšiřuje na varianci. **N:** $N\le 1920$ dense (jen počítání molekul, žádný eigh),
  stovky seedů pro varianci — **[odpoledne]** (levné, čistě kombinatorické, varianta hotového
  VYPOCET-27 kódu).
- **Co by dalo:** kdyby fluktuace dala area-zákon tam, kde mean selhal, **zachránilo by to 4D
  Dou-Sorkin linii** v order-by-disorder formě (Sorkinova původní teze) a doplnilo hranu
  `black-holes-information↔causal-sets` daty. Kdyby ne, je to druhý nezávislý negativ k F-031
  (ani mean, ani variance 4D area-zákon nedají).
- **Riziko:** variance molekulového počtu má vyšší statistický šum než mean → potřebuje hodně seedů.
  `horizon_molecules_codim2` závisí na k_tube (F-031 caveat (b): exponent 0.4–0.8 přes k=1.0–2.0) —
  fluktuace může být ještě citlivější na k_tube. Pokud variance jen kopíruje mean škálování, nepřináší
  nic nového.

---

### H6g-7 — Draft-06 kandidát: informované negativy páté generace tvoří „mapu selhání" jako samostatný výstup

**(meta-hypotéza o publikační strategii: F-031+F-033 negativy jako pozitivní vědecký výstup)**
**Priorita: medium (strategická; rozhoduje, jak rámovat páté kolo navenek).**

- **Tvrdí:** tři informované negativy páté generace — F-031 (4D dS area-zákon genuinně nepřítomný),
  F-033 (causal-sets↔NCG selhává na metrice, drží na boostu/KMS), H5g-3 vyvrácení (codim-2 ≠ 2D roh) —
  tvoří **koherentní „mapu selhání"**, která je samostatný publikovatelný výstup, ne jen vedlejší
  produkt. Společná nit: **každý negativ lokalizuje, na KTERÉ OSE diskrétní konstrukce funguje a na
  které ne** — area-zákon žije ve 2D ne 4D (dimenze-závislé), korespondence žije na tepelné ose ne
  metrické (osově-závislé), rohový mechanismus žije ve 2D ne 4D (dimenze-závislé). To je
  through-line „vlastnosti = odpovědi na otázky" v **negativní formě**: říká, KTERÉ otázky diskrétní
  SJ/NCG aparát NEumí zodpovědět. Letter „kde diskrétní gravitační aparát selhává a proč" je cennější
  než tři roztroušené null-výsledky.
- **Opora (F-ID):** F-031 (4D area-zákon nepřítomný), F-033 (NCG metrika selhává, boost drží),
  F-026/H5g-3 (codim-2 ≠ roh). F-030 (B(a) spojitá — pozitivní, ale uzavírá „B=D-1" naději).
  SYNTEZA-02 through-line („vlastnosti = odpovědi na otázky"). Precedent: draft-02 (a₄=−18/11) je
  z velké části o tom, co graviton NEzachrání — negativ jako vlajková loď.
- **Test (rozhodovací, ne výpočetní):** rozhodnou **H6g-1** (drží tepelná osa?) a **H6g-2** (je 4D
  nepřítomnost area-zákona robustní?). Pokud H6g-1 dá POZITIV na tepelné ose (Unruh teplota) a H6g-2
  POTVRDÍ 4D nepřítomnost jako fyziku (ne artefakt), je „mapa selhání" kompletní a koherentní →
  draft-06 letter. Pokud H6g-2 area-zákon OBNOVÍ (konformní vazba), mapa selhání má díru a F-031 se
  překlápí na pozitiv → jiný příběh.
- **Co by dalo:** ujasnilo by publikační rámec pátého kola. Negativní výsledky jsou v QG vzácně
  publikované poctivě — „mapa, kde diskrétní aparát selhává" je metodologicky cenná a odlišuje program
  od hype.
- **Riziko:** „mapa selhání" může vypadat jako sbírka neúspěchů, ne pozitivní výsledek — rámování je
  klíčové a referee může číst jako „nic nefunguje". Závisí na tom, zda H6g-1/H6g-2 dají čisté
  rozhodnutí (negativ MUSÍ být informovaný, ne inconclusive). Strategická, ne výpočetní — neřeší se
  compute, ale editorial.

---

## 3. Návrh simulačního testu / výpočtu — konkrétní specifikace pro `lib/toe`

Souhrn nejostřejších tří testů (H6g-1, H6g-2, H6g-4) v plné lib-specifikaci. Cesty `__file__`-relativní
(per CLAUDE.md Konvence kódu); výsledky atomickým/progresivním zápisem (per Hygiena agentů — schéma);
ε z F-006 zafixováno PŘED měřením (anti-kruhovost).

### Test A (H6g-1) — Unruhova teplota z modulárního kernelu [odpoledne]

```
Geometrie:  causet.sprinkle_slab2d(N=1200, rng, t_extent=0.30, x_extent=1.0)
            řez O = {x > 0}  (Rindler, modulární tok = BW boost)
Objekt:     C = causet.causal_matrix(coords)
            G_R = causet.green_retarded_2d(C);  iDelta = causet.pauli_jordan(G_R)
            W = sj.wightman(iDelta);  sub_idx = np.where(coords[:,1] > 0)[0]
            mk = entropy.modular_kernel(W, iDelta, sub_idx, kappa=None)   # netruncovaný = pravý SJ tok
Observable: (a) modulární energie eps_i = ln[mu_i/(mu_i-1)]  (mk vrací mu)
            (b) boostová souřadnice eta_i = arctanh(x_i / t_i)  resp. rapidity podél orbity
            (c) T_mod = 1 / (2pi * sklon(eps vs eta))    # Unruh: beta_mod = 2pi
            (d) KMS: G_beta(x,y;t) periodicita v imag. čase, perioda 2pi
Diskrim.:   T_mod -> 1/2pi ≈ 0.159 (do 10-20 %) NEZÁVISLE na rho a N  AND  KMS drží
            -> POZITIVNÍ datová hrana causal-sets<->NCG na tepelné ose (F-033 předpověděl)
            T_mod driftuje s rho  -> modulární data nenesou ani tepelný obsah (negativ se rozšiřuje)
N, seedy:   N=1200, 5-10 seedů, dense eigh; sweep rho ∈ {300,600,1200} pro rho-invarianci T_mod
Tier:       [odpoledne] — varianta hotového core-data/calculations/spectral-triple-modular/
```

### Test B (H6g-2) — konformně-vázaný 4D dS area-zákon [odpoledne→sparse]

```
Geometrie:  causet.sprinkle_ds_static_patch4d(N, rng, l=1.0, rstar_box, t_extent, x_perp_half)
            + plochá kontrola (uniform měřítko, shodná hustota)
Objekt:     L = causet.link_matrix(causet.causal_matrix(coords))
            G_R = green_retarded_4d_massive(L, rho, m2 = xi*R = 2/l^2)   # NOVÝ: hmotný KG propagátor
                  baseline: green_retarded_4d (m=0, xi=0) = F-031 kontrola
            iDelta = pauli_jordan(G_R);  S_full = entropy.ssee(..., n_max=2*N**0.75)  # F-019 regulátor
            A_codim2 = causet.horizon_molecules_codim2(coords, L, r_index=1,
                          r_cut, eps=rho**(-1/4), k_tube=1.5)             # F-031 primitiv, eps z F-006
Observable: R' = S_full / A_codim2  jako funkce rho, pro xi=1/6 vs xi=0
Diskrim.:   konformní (xi=1/6) R' rho-invariantní (CV<0.1, d ln R'/d ln rho ≈ 0)
            -> 4D nepřítomnost BYLA artefakt, area-zákon OBNOVEN  (F-031 caveat (a) rozhodnut)
            konformní R' stále driftuje rho^+0.5  -> 4D nepřítomnost ROBUSTNÍ fyzika (F-031 stojí silněji)
N, seedy:   rho ∈ {120,240,480}, dense N≤1920, 5 seedů (F-031 Stage B rozsah)
            rho>480 -> [sparse] sj_state_sparse + idelta_operator (4D varianta nutná)
Tier:       [odpoledne] na nízké rho. Hlavní práce = green_retarded_4d_massive (masivní KG retard. propag.)
Riziko:     masivní SJ pozitivita NEzaručena -> ověřit well-definedness sj_state na masivním iDelta
```

### Test C (H6g-4) — Lorentz-invariantní shot-noise sprinklingu [odpoledne, nejlevnější]

```
Geometrie:  causet.sprinkle_box4d(N, rng, half=1.0)   # 4D box = proxy minulého kužele
            podobjemy V_k ⊂ box, počítej N_k = #{body ∈ V_k}
Objekt:     ŽÁDNÝ eigh — jen počítání bodů.  Boost: coords' = Lambda(eta) @ coords, eta ∈ [0,2]
            kontrola: pravidelná 4D mřížka místo Poisson sprinklingu
Observable: (a) Var(N_k)/<N_k> jako funkce <N_k> (rozsah objemů)         # Poisson -> konst. 1
            (b) Var(N)/<N> pod boostem eta                               # predikce: nezávislé na eta
            (c) mřížková kontrola: Var(N) pod boostem                    # predikce: POROŠÍ (kontrakce)
Diskrim.:   Poisson Var/<N> = 1 ± eps boost-invariantní AND mřížka boost-závislá
            -> shot-noise je Lorentz-invariantní fluktuační spektrum (slabá forma přežívá F-005)
            Var/<N> ≠ 1 nebo boost-závislé -> i slabá forma padá
N, seedy:   N do 1e5-1e6, stovky seedů (jen counting, žádný maticový problém)
Tier:       [odpoledne] — výpočetně nejlevnější celé generace (není to eigh)
Caveat:     testuje fluktuaci POČTU atomů + boost-kovarianci, NE plný řetězec N -> Lambda (nutná, ne postačující)
```

Testy D (H6g-3 re-analýza `sj-kerr-b-scan`, žádný nový běh) a E (H6g-6 variance molekul, varianta
VYPOCET-27) jsou levné follow-upy; H6g-5 (BD→AS) je [sparse] s vysokým rizikem inconclusive (α-drift).

---

## 4. Hlavní teoretická rizika a limity

Poctivá inventura rizik šesté generace — co může každou hypotézu rozbít a kde je hranice
interpretace.

1. **Konečné N měří TRENDY, ne asymptotické invarianty (systematické napříč všemi H6g).** Stejně jako
   draft-04: typ algebry, II₁/II_∞, Unruhova teplota $1/2\pi$, AS fixní bod — všechno jsou
   $N\to\infty$ / $\rho\to\infty$ tvrzení; na konečném causetu měříme TRENDY (saturace vs. růst,
   konvergence vs. drift). H6g-1 $T_{mod}=1/2\pi$ je spojitá BW hodnota — diskrétní korekce $O(1/\sqrt N)$.
   Každá H6g musí být explicitní: měříme trend a extrapolujeme, ne hodnotu při jednom $N$.

2. **Surogát ≠ from-first-principles (H6g-1 zdědí F-033 caveat).** $D_K=\mathrm{sgn}(K)\sqrt{|K|}$ je
   SUROGÁT modulárního Diraca, ne axiomatický spektrální triple známé KO-dimenze. H6g-1 testuje, zda
   modulární DATA nesou tepelný obsah, ne existenci plného triplu. Pozitiv na tepelné ose neznamená
   plnou NCG rekonstrukci — znamená, že modulární surogát kóduje Unruh/KMS (slabší, ale čisté tvrzení).

3. **Konformní caveat se ZMENŠÍ, nezmizí (H6g-2 limit).** I konformně-vázaný 4D skalár na PLOCHÉ
   kauzální struktuře (link-matice Green) NENÍ přesný zakřivený dS propagátor. H6g-2 odstraní
   $\xi=0$→$\xi=1/6$ část caveatu (a), ale zbytek (plochá kauzalita vs. zakřivený propagátor) zůstává.
   Verdikt H6g-2 bude „area-zákon obnoven konformní vazbou NA TÉTO ploché-kauzální konstrukci", ne
   „na přesném dS stavu". Plné rozhodnutí vyžaduje zakřivený 4D dS propagátor, který repo NEMÁ.

4. **Masivní SJ well-definedness (H6g-2 blokátor).** $m_{eff}^2=2/\ell^2$ je $O(1)$, ne malá hmota —
   masivní $iΔ$ má jiné spektrum a SJ pozitivita NENÍ zaručena (jako φ-periodicita u draftu-01).
   Pokud masivní SJ stav není dobře definovaný, H6g-2 padá na read-first (analytická kontrola
   masivního dS SJ).

5. **Triviálnost Poissonu (H6g-4 limit).** $\mathrm{Var}(N)/\langle N\rangle=1$ JE z definice
   Poissonova procesu — netriviální obsah je až boost-invariance a kontrast s mřížkou. Test ověří
   POČET atomů a jeho boost-kovarianci, NE plný řetězec $\delta N\to\delta\Lambda$ (Sorkinova konjugace
   $\Lambda$↔$V$, sama hypotéza). Nutná, ne postačující podmínka pro everpresent-Λ. Riziko
   „Poisson je Poisson" tautologie.

6. **α-drift / konvergence (H6g-5 dominantní riziko).** F-012 už dokumentoval BD α-drift $+1.28$
   nekonvergován při $N\le 3000$, cond(B)$\to 2e10$. AS fixní bod **nemusí být dosažitelný** při
   $N\le 12000$ — vysoká šance na inconclusive (ne čistý negativ). Nejrizikovější compute generace.

7. **k_tube citlivost (H6g-2, H6g-6 zděděno z F-031).** `horizon_molecules_codim2` exponent závisí na
   k_tube (0.4 při k=1.0 až 0.8 při k=2.0; k=1.5 dává čistý $\rho^{0.5}$). Variance (H6g-6) může být
   ještě citlivější. Verdikty musí reportovat k_tube-závislost.

8. **Anti-kruhovost (všechny H6g s kalibrací).** ε ~ $\rho^{-1/d}$ MUSÍ být zafixováno z NEZÁVISLÉHO
   F-006 PŘED měřením poměru, nikdy tuninguto k cíli (stejný filtr jako −18/11 scheme-robustnost a
   H5g-2 disciplína). Platí zvlášť pro H6g-2 ($R'$ poměr) a H6g-6 ($\mathrm{Var}/A$).

9. **Žádné vymyšlené arXiv ID (CLAUDE.md striktní).** Tento dokument cituje POUZE repo-přítomné
   reference (gr-qc/9406019 Connes-Rovelli, 1611.10281 SSEE, 2206.10780 CLPW, gr-qc/0302009 Dou-Sorkin,
   1001.2725 BD, 0905.2562 Casini-Huerta, 1712.04227 BW-boost — všechny v F-033 refs / draft anchorech).
   Žádné nové ID. Hypotézy jsou PROPOSALS — do findings/connections vstoupí až po compute + editorial.

---

## Doporučená fronta

Seřazeno podle (decisiveness × proveditelnost × novost). Tier: **[odpoledne]** (dense eigh $N\le 2500$
nebo čisté counting), **[sparse]** (eigsh $N\le 12000$), **[read-first]**.

| # | Test | Hypotéza | Tier | Co rozhodne | Decis. | Proveditelnost | Novost |
|---|------|----------|------|-------------|:------:|:--------------:|:------:|
| 1 | **Unruhova teplota / KMS z modulárního kernelu** (2D slab Rindler, T_mod→1/2π?, varianta VYPOCET-29) | H6g-1 | **[odpoledne]** | Drží TEPELNÁ osa causal-sets↔NCG, kde F-033 dal PASS na diagonále? → POZITIVNÍ datová hrana | ★★★ | ★★★ | ★★★ |
| 2 | **Konformně-vázaný 4D dS area-zákon** (ξ=1/6 masivní KG vs ξ=0, R' ρ-invariance) | H6g-2 | **[odpoledne]**→[sparse] | Je 4D nepřítomnost area-zákona (F-031) artefakt non-konf. skaláru, nebo fyzika? Rozhodne otevřený caveat | ★★★ | ★★☆ | ★★★ |
| 3 | **Lorentz-invariantní shot-noise sprinklingu** (Var(N)/⟨N⟩ pod boostem, mřížka kontrola) | H6g-4 | **[odpoledne]** | Přežívá slabá Λ-fluktuace F-005 jako boost-invariantní variance (ne prefaktor)? Nejlevnější | ★★☆ | ★★★ | ★★★ |
| 4 | **Analytická B(Ω) z míry klínu × hustoty** (re-analýza sj-kerr-b-scan + symbolika) | H6g-3 | **[odpoledne]**/[read-first] | Je B(a) odvoditelné, ne fitované? → draft-01 fenomenologie→teorie. Žádný nový běh | ★★☆ | ★★★ | ★★☆ |
| 5 | **4D molekulová FLUKTUACE = area-zákon** (Var(N_mol) kde mean selhal, varianta VYPOCET-27) | H6g-6 | **[odpoledne]** | Dá order-by-disorder area-zákon tam, kde mean-count (F-031) selhal? | ★★☆ | ★★★ | ★★☆ |
| 6 | **BD path integral → AS fixní bod** (d_s(σ) flow, kritický exponent) | H6g-5 | **[sparse]** | Realizuje BD causet AS-like fixní bod? VYSOKÉ riziko inconclusive (α-drift F-012) | ★★☆ | ★☆☆ | ★★★ |
| 7 | **Draft-06 „mapa selhání"** (F-031+F-033+H5g-3 koherentní negativ) | H6g-7 | **[read-first]** | Rozhodují H6g-1/H6g-2; editorial, ne compute | ★★☆ | ★★☆ | ★★☆ |

**Doporučené pořadí:** **#1 a #3 paralelně** (obě [odpoledne], obě nejlevnější, obě instancují
nedotčenou/přerámovanou hranu) — nejvyšší ROI tohoto kola. #1 je vlajkový (F-033 explicitně předpověděl
PASS na tepelné ose — vysoká šance pozitivu, první POZITIVNÍ causal-sets↔NCG hrana). #3 je nejlevnější
a rehabilituje Λ-linii v F-005-přežívající formě. Pak **#2** (rozhodne otevřený konformní caveat F-031 —
vyžaduje masivní Green funkci, ale jinak hotová mašinérie; vlajkový dopad na draft-04/05). #4 a #5 jsou
levné follow-upy (re-analýza hotových dat / varianta VYPOCET-27). **#6 (BD→AS) zařadit poslední** —
nejvyšší riziko inconclusive (α-drift dokumentován F-012). #7 je editorial, rozhodne se výsledkem
#1+#2.

**Jedno odpoledne:** #1, #3, #4, #5. **Nová mašinérie:** #2 (masivní KG propagátor + sparse 4D),
#6 (sparse BD spektrum). **Read-first:** #7 (editorial), #4 (pokud IR hrana není čistá).

---

*Anchory šesté generace: `core-data/findings.json` (F-001…F-033, F-029…F-033 nejčerstvější);
`knowledge-base/vypocty/VYPOCET-27-4d-amol-convention.md` (4D area-zákon nepřítomný, konformní caveat
otevřen), `VYPOCET-29-spectral-triple-modular.md` (NCG metrika selhává, boost/KMS drží),
`VYPOCET-26-kerr-b-exponent.md` (B(a) spojitá), `VYPOCET-28-proxy3-seeds.md` (proxy3 ≥30 seedů),
`VYPOCET-25-scaled-ds-entropy.md` (2D area-zákon robustní, 4D drift); `knowledge-base/SYNTEZA-02.md`
(through-line, lovecký žebříček #1 causal-sets↔AS); `knowledge-base/BRAINSTORM-05.md` (capstone, fronta);
`core-data/connections.json` (292 hran; barely: causal-sets↔NCG INSTANCOVÁNA F-033 informovaný negativ,
causal-sets↔AS nedotčená, black-holes↔causal-sets, cosmological-constant-fluctuation);
`lib/toe/` (entropy.modular_kernel, spectraltriple.dirac_from_kernel/connes_distance,
causet.sprinkle_ds_static_patch4d/horizon_molecules_codim2, sj.superradiant_weight,
sj.sj_state_sparse + causet.idelta_operator_2d sparse path). Klíčová literatura (vše repo-přítomné,
ŽÁDNÉ nové ID): gr-qc/9406019 (Connes-Rovelli tepelný čas), 1611.10281 (SSEE), 2206.10780 (CLPW dS II₁),
gr-qc/0302009 (Dou-Sorkin horizon molecules), 1001.2725 (Benincasa-Dowker), 0905.2562 (Casini-Huerta
modulární energie), 1712.04227 (Bisognano-Wichmann boost). Hypotézy H6g-1…H6g-7 jsou PROPOSALS —
vstupují do findings/connections teprve po compute + editorial rozhodnutí.*
