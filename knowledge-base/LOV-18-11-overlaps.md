# LOV: −18/11 — lov na nenakreslené překryvy kolem indexově chráněného NCG fermionového jádra

> **Status:** brainstorm / exploratory (Exploratory Engine, Theorizing Mode). Vše níže jsou **návrhy hypotéz a testů**, ne findings. Nic se nezapisuje do `findings.json` ani `connections.json` bez výpočtu a editorského rozhodnutí. Navrhované hrany grafu jsou v § *Návrh hran* — **nepřidávat automaticky**.
>
> **Kotva:** F-003, F-014, F-020; `papers/draft-02-a4-fermionic-identity/draft.md`; `lib/toe/ncg.py` (exact-rational a₄ stroj: `central_charges`, `a4_ratio`, `spectral_action_ratio`, `sector_ledger`, `str_count`, `lambda_induction_ledger`).
> **Datum:** 2026-06-08.

---

## 1. Teoretická syntéza — co je −18/11 a proč stojí stranou

### 1.1 Přesné tvrzení

V $a_4$ (Seeley–DeWitt, $\Lambda^0$) členu Chamseddine–Connes spektrální akce je poměr koeficientu u $C^2$ (Weyl-kvadrát) ku koeficientu u Eulerovy (Gauss–Bonnet) hustoty přesně
$$
\frac{\alpha_0}{\tau_0}=\frac{-3f_0/10\pi^2}{\,11f_0/60\pi^2\,}=-\frac{18}{11}=-1.6363\ldots,
$$
a totéž číslo je konformně-anomální poměr $c/(-a)$ pro **jediný Weylův fermion**:
$$
\frac{c_{\rm Weyl}}{-a_{\rm Weyl}}=\frac{1/40}{-11/720}=-\frac{18}{11}.
$$
Klíčová vlastnost je **content-independence**: protože každý Weylův fermion nese stejnou dvojici $(a,c)=(11/720,\,1/40)$, $N_W$ se v poměru zkrátí. Identita tedy platí *přesně* pro 1 fermion, pro 45 (SM bez $\nu_R$) i pro 48 (s $\nu_R$), s nulovým reziduem (F-003).

### 1.2 Proč je to věta, ne náhoda

Obě strany jsou **týž** $a_4(D^2)$ koeficient jednoho Diracova operátoru, čtený ve dvou normalizacích (draft-02 §2): v $d=4$ je integrovaný $a_4$ *právě* konformní anomálie ($a_4=\frac{1}{16\pi^2}\int\sqrt g(cW^2-aE_4)$), a současně je to $\Lambda^0$ člen $\mathrm{Tr}\,f(D/\Lambda)$. Poměr dvou členů *uvnitř* $a_4$ je invariantní vůči libovolné společné renormalizaci ($f_0$, $N$, $1/2880\pi^2$ vs $1/(4\pi)^2$ se zkrátí). Otisk společného původu: prvočíslo „11" se objevuje v $\tau_0=11f_0/60\pi^2$ i v $a_{\rm Weyl}=11/720$ (poměr $=12$).

### 1.3 Indexová ochrana (proč je to „topologický náboj")

F-014 ukazuje, že −18/11 je **striktní fermionový diskriminátor**, který nelze zachránit žádným bosonem:
- konformní (Weylův) graviton dává $-398/261\neq-18/11$;
- žádný jednotlivý boson neleží na fermionovém paprsku −18/11 v rovině $(a,c)$;
- multiplicita gravitonů nutná k vynucení full-SM na −18/11 je $x=-143/32<0$ (nefyzikální).

Eulerův sektor spinorového $a_4$ je konformní $a$-anomálie ($\chi$/Gauss–Bonnet); Pontryaginův sektor je Atiyah–Singer Â-index-hustota: $\hat A|_4=-p_1/24$, $\mathrm{ind}(D)=-\sigma/8$, Rohlinova věta $\sigma=16\Rightarrow\mathrm{ind}=-2$ (sudé celé číslo). −18/11 je tedy **scheme-independent, indexem chráněný** racionál — to je důvod, proč ho lze brát jako diskrétní „náboj", který by ostatní pilíře měly reprodukovat, ne ladit.

### 1.4 Proč stojí stranou — důkaz z grafu

Ověřeno v `core-data/concept-graph.json` + `connections.json`:

- **Trace-anomaly ostrov.** Uzel `trace-anomaly` má 8 hran, **všechny** typu `related-concept`/`explored:None`, a vede jen k semiclassical-gravity sousedům + `a-theorem`/`central-charge`/`conformal-anomaly`/`worldsheet-cft`/`critical-dimension`/`cardy-formula`. `a-theorem` má jedinou hranu (na `trace-anomaly`). Tento klastr **nemá ani jednu hranu** do NCG spektrálně-akčního klastru.
- **Spektrálně-akční klastr.** `spectral-action` vede na `dirac-operator`, `spectral-triple`, `heat-kernel-expansion`, `almost-commutative-geometry`, `inner-fluctuations` — ale **nikam do anomálního klastru**. `heat-kernel-expansion` vede na `spectral-action`, `cosmological-constant-problem` a **`spectral-dimension`** — ale ne na `trace-anomaly`.
- **Chybějící mosty** (ověřeno, že v `connections.json` neexistují): `spectral-action↔trace-anomaly`, `spectral-action↔central-charge`, `noncommutative-geometry↔trace-anomaly`, `noncommutative-geometry↔spectral-dimension`, `trace-anomaly↔entanglement-entropy`, `noncommutative-geometry↔entanglement-entropy`, `a-theorem↔spectral-dimension`. Existuje pouze `noncommutative-geometry↔entanglement-spacetime` jako `barely`.
- **NCG hub.** 42 hran, z toho 21 `barely`, 9 `partially`, 3 `well`. Drtivá většina cross-pillar je `barely` — primární lovná zóna.

**Závěr:** $a_4$ heat-kernel koeficient JE konformní/trace anomálie. Takže −18/11 = $c/(-a)$ je doslova **chybějící shared-math most** mezi NCG spektrálně-akčním klastrem a trace-anomaly klastrem — nejvýraznější nenakreslený překryv v grafu. Stojí stranou, protože dvě obří literatury (NCG / anomálie) sdílejí jeden koeficient, ale projektový graf je dosud nepropojil.

---

## 2. Nové hypotézy a extrapolace (řazeno podle síly evidence × dosahu)

### H-A — **Trace-anomaly ↔ spectral-action: chybějící most (kotevní)**

**Fyzikální tvrzení.** Trace-anomaly klastr a NCG spektrálně-akční klastr nejsou dvě nezávislé fyziky, ale dva pohledy na **týž** $a_4(D^2)$. −18/11 je doslovný číselný spoj. Hrana `spectral-action↔trace-anomaly` (resp. `↔central-charge`) má patřit do grafu s `explored: well` (je to *věta*, F-003/F-014), ne `barely`.

**Sdílená matematika.** $a_4=\frac{1}{16\pi^2}\int\sqrt g(cW^2-aE_4)$ = $\Lambda^0$ člen $\mathrm{Tr}\,f(D/\Lambda)$. Identický Gilkey/Vassilevich heat-kernel koeficient (draft-02 §2, kroky 1–5).

**Evidence.** F-003 (exact, zero mismatch, sympy), F-014 (index-protekce, Duff Table 1 cross-check). Graf: most prokazatelně chybí (§1.4).

**Riskovost.** **Nízká** — to není spekulace, je to dokázaná identita, kterou graf jen nezaznamenal. Hodnota není v objevu, ale v *uzavření* zjevně chybějícího mostu a v tom, že odemyká H-B–H-E.

---

### H-B — **−18/11 ↔ univerzální koeficient entanglement entropie (most do LINIE B)** ★ vlajková

**Fyzikální tvrzení.** Trace-anomální náboje $(a,c)$ řídí **univerzální** členy entanglement entropie: ve 4D je univerzální log-koeficient $\sim c$ (resp. kombinace $a,c$ podle geometrie entangling plochy; Solodukhin), a sférická/Rényi EE $\sim a$ (Casini–Huerta–Myers: $a = $ koeficient sférické EE). Naše SSEE / type-transition mašinérie (draft-04, `lib/toe.entropy`, `lib/toe.vntype`, F-015/019/023/029) **měří koeficienty entropie**. Tvrdím: dimensionless koeficient, který extrahujeme z diskrétní SSEE area-law, je *tentýž druh objektu* jako $a_4$ $a$-koeficient — a je svázán s −18/11. Pokud naše čistě-fermionové (resp. konformně-skalární) pole reprodukuje racionál odvozený z $(a,c)$, poprvé se indexem-chráněné NCG jádro dotkne von-Neumann/type-transition vlajkové linie.

**Sdílená matematika.** $a$-věta: $a$ je monotónně klesající náboj počítající efektivní stupně volnosti; sférická EE konformního pole $= a$ (CHM). Naše F-029 už extrahuje dimensionless $c_{\rm EE}$ z de-Sitter static-patch area-law: $S_{\rm cap}=A_{\rm horizon}/(c_{\rm EE}\cdot G)$, $c^{2D}_{\rm EE}\approx 7.70$ (CV 3 %, F-029). To JE univerzální koeficient. Otázka: je $c^{2D}_{\rm EE}$ (resp. jeho 4D protějšek) racionálně příbuzný $a$-/$c$-náboji konformně-skalárního pole, které sprinkujeme — a tím nepřímo struktuře, z níž žije −18/11?

**Evidence.** F-023, F-029 (de Sitter II₁ saturace + extrahovaný $c_{\rm EE}$), F-015/019 (III₁→II přechod, entropie area-law $S\sim\sqrt N$). `lib/toe.entropy.ssee`, `ssee_scaling`. Anomální strana: `lib/toe.ncg.central_charges`, `a4_ratio`. Graf: `noncommutative-geometry↔entanglement-entropy` a `trace-anomaly↔entanglement-entropy` **chybí**.

**Riskovost.** **Střední → vysoká, ale levně testovatelná.** Past: naše pole je masless skalár (conformal trick), ne Weylův fermion — takže přímý cíl je *skalární* $(a,c)=(1/360,1/120)$, $c/(-a)=-3$, a teprve sekundárně −18/11 po záměně obsahu na fermion. Hodnota: i *negativní* výsledek (diskrétní $c_{\rm EE}$ NEodpovídá $a_4$ $a$) je ostrý — řekne, že SSEE-koeficient je geometrický (κ-cutoff řízený), ne anomální. Toto je most do linie B a **doporučený první test** (§3.1).

---

### H-C — **noncommutative-geometry ↔ spectral-dimension (ML-předpovězená hrana, score 0.896)**

**Fyzikální tvrzení.** $a$-koeficient počítá efektivní stupně volnosti (a-věta: monotónně klesá pod RG tokem); spektrální dimenze $d_s({\rm probe})$ (draft-03, F-001/F-002, `lib/toe.spectral`) počítá efektivní dimenzi pod difuzí/RG. Tvrdím existenci vztahu mezi indexem-chráněným anomálním poměrem a UV/IR $d_s$ téhož obsahu polí: spektrální dimenze a spektrální akce sdílejí **týž Diracův operátor a týž heat-kernel** ($P(\sigma)=\mathrm{Tr}\,e^{-\sigma D^2}$ vs $\mathrm{Tr}\,f(D/\Lambda)$ — oba jsou funkcionály $D^2$-spektra).

**Sdílená matematika.** Heat-kernel $\mathrm{Tr}\,e^{-\sigma D^2}\sim\sum_k a_{2k}\sigma^{(k-D/2)}$: spektrální dimenze čte UV/IR škálovací exponent návratové pravděpodobnosti, spektrální akce čte tytéž koeficienty $a_0,a_2,a_4$. Uzel `heat-kernel-expansion` **už** vede na `spectral-dimension` (ověřeno v grafu) — most NCG↔spectral-dimension je tedy „o jeden uzel daleko" a ML link-prediction ho navrhuje (score 0.896, `noncommutative-geometry↔spectral-dimension`, 7 shared neighbors).

**Evidence.** `core-data/link-predictions.json` (top NCG-dotykový kandidát, 0.896). F-001/F-002. `heat-kernel-expansion→spectral-dimension` hrana existuje; `noncommutative-geometry↔spectral-dimension` **chybí**.

**Riskovost.** **Střední.** Past: $d_s$ je probe-závislá (F-001/F-002), takže „NCG $d_s$" není jednoznačné číslo. Ale shared-math (týž heat-kernel) je solidní; hrana patří do grafu minimálně jako `shared-math/barely` s heat-kernel zdůvodněním.

---

### H-D — **−18/11 jako UV-fixed-point invariant asymptotic safety (odvážné)**

**Fyzikální tvrzení.** Indexem chráněný poměr by mohl být invariant Reuterova UV fixed-pointu. AS graviton má anomální dimenzi $\eta_N$ na fixed-pointu; Weyl²/Euler poměr efektivní akce na fixed-pointu by mohl být zafixován na racionální hodnotu, kterou index chrání. Pokud je −18/11 (nebo blízký racionál) UV invariant fermionového obsahu v AS, propojí to indexové jádro s `asymptotic-safety` (dnes NCG↔AS = `barely`).

**Sdílená matematika.** Na FP jsou dimensionless couplings konstantní; poměr dvou kvadraticko-křivostních couplingů ($g_{C^2}/g_{\rm GB}$) je čisté číslo. $a$-věta (Komargodski–Schwimmer) svazuje UV a IR $a$; index chrání UV stranu fermionového sektoru.

**Evidence.** Graf hit-list měl asymptotic-safety graviton-anomalous-dimension uzly. NCG↔AS hrana je `barely`. F-014 (index-protekce).

**Riskovost.** **Vysoká.** Past: FP-poměr v AS je schéma/truncation-závislý (na rozdíl od $a_4$, kde se schéma zkrátí); rovnost s −18/11 by mohla být numerologie. Test by vyžadoval FRG truncation, mimo `lib/toe`. Označuji jako spekulaci, ne k okamžitému testu.

---

### H-E — **Index-protekce ↔ topologie napříč pilíři: −18/11 jako diskrétní náboj (nejodvážnější)**

**Fyzikální tvrzení.** Atiyah–Singer Â / η-invariant / spectral flow chrání −18/11. Tytéž topologické invarianty se objevují v causal-set topology change, LQG spin-network moves a CDT. Tvrdím: $\mathrm{ind}(D)=-\sigma/8$ a Rohlinův zámek ($\sigma=16\Rightarrow\mathrm{ind}=-2$) jsou *diskrétní topologické náboje*, které by diskrétní pilíře měly reprodukovat — např. signature/index molekuly causal setu nebo spin-network spektrální flow by měly nést sudý-celočíselný index konzistentní s Rohlinem.

**Sdílená matematika.** Â-genus, $p_1$/24, Rohlin $\sigma\equiv0\ (\mathrm{mod}\ 16)$ pro spin 4-manifoldy. `lib/toe.causet.horizon_molecules_codim2` počítá codim-2 molekuly (Euler/topologický proxy).

**Evidence.** F-014 (Rohlin zámek explicitní). NCG↔causal-sets = `barely`, NCG↔CDT = `barely`, NCG↔LQG = `partially`.

**Riskovost.** **Velmi vysoká.** Past: $\sigma=16$ je vlastnost hladké spin 4-variety; causal set je Lorentzovský a nemá přímou signature-formu. Spojení je analogické, ne nutně shared-math. Spekulace — uvádím pro úplnost lovné zóny, ne k testu.

---

### H-F — **Čísla 11 a 18 samotná: racionál vs kontinuum (kuriozita s testovatelným jádrem)**

**Fyzikální tvrzení.** 11 pochází z $a_{\rm Weyl}=11/720$ (Eulerův/Â sektor), 18 z $c_{\rm Weyl}=1/40$ přes $18/720$. Index-protekce dělá z −18/11 **diskrétní racionální** invariant — kontrast s irracionálními/kontinuálními veličinami jinde (spektrální dimenze 2.5, exponenty $p=0.519$, atd.). Tvrdím slabou hypotézu: indexem-chráněné veličiny projektu jsou racionály, neindexové jsou kontinuální driftující exponenty. To je *klasifikační* tvrzení napříč findings.

**Evidence.** F-003 (přesný racionál) vs F-012 (driftující $\alpha$), F-006 ($p=0.519$). `str_count` (STr 1 = −62/−68 — také celá čísla).

**Riskovost.** **Vysoká / spíš meta-pozorování.** Past: čistá numerologie, pokud se nepodepře mechanismem. Hodnota jen jako organizační princip („racionál = indexová stopa").

---

## 3. Návrh simulačního testu (TOP 2)

### 3.1 ★ LEVNÝ ODPOLEDNÍ TEST — H-B: reprodukuje diskrétní SSEE univerzální koeficient $a_4$ $a$-koeficient?

**Cíl/diskriminátor.** Otestovat, zda dimensionless univerzální koeficient $c_{\rm EE}$ z naší diskrétní SSEE area-law je racionálně příbuzný anomálnímu $(a,c)$ pole, které sprinkujeme (massless conformal scalar) — a tím připravit půdu pro fermionovou variantu cílící na −18/11.

**Přesný setup (vše v `lib/toe`, dense path, $N\le2500$):**
1. **Geometrie:** 2D Poisson-sprinkled causal diamond — `toe.causet.sprinkle_diamond2d(N, rng)`.
2. **Pole/stav:** massless skalár → `green_retarded_2d(C)` → `pauli_jordan(...)` → `toe.sj.sj_state(iDelta)`.
3. **Observable:** `toe.entropy.ssee_scaling(sprinkle_diamond2d, Ns, frac=0.5, n_seeds=8, seed_base=..., truncate="kappa")` s $\kappa=\sqrt N/(4\pi)$ (entropy cutoff). Vrací area-law exponent (očekáváme $p\approx1/2$, F-006) a `S_mean(N)`.
4. **Extrakce koeficientu:** z `S_trunc` area-law nafitovat dimensionless koeficient $\tilde c$ v $S=A/(\tilde c\cdot G_{\rm eff})$ — analogicky F-029 ($c^{2D}_{\rm EE}\approx7.70$). Použít **už hotovou** de Sitter cestu (F-029, `ds_cap_2d`) jako čistší zdroj $c_{\rm EE}$ (saturuje, type II₁).
5. **Anomální strana (exact, zdarma):** `toe.ncg.central_charges(n0=1, n_weyl=0, n1=0)` → skalární $(a,c)=(1/360,1/120)$, $c/(-a)=-3$; `central_charges(0,1,0)` → Weyl $(11/720,1/40)$, ratio `a4_ratio(sector="fermion")` $=-18/11`. 
6. **Diskriminátor:** je $c_{\rm EE}$ (resp. $1/c_{\rm EE}$, resp. poměr $c_{\rm EE}^{\rm full}/c_{\rm EE}^{\rm trunc}$) ve shodě (do CV) s racionálem postaveným z $\{1/120,1/360\}$ (např. $c_{\rm EE}\approx 7.70$ vs $360/45.6$? vs $8=$?) **na úrovni $<5\%$**? Pre-registrovat cílové racionály PŘED měřením (anti-circularity, direktiva #5): kandidáti $\{3,\ 18/11,\ 8,\ 12,\ 360/c_{\rm scalar}\}$. **Match → most H-B reálný; no-match → SSEE-koeficient je geometrický, ne anomální** (oba výsledky publikovatelné).

**Feasibility tier: CHEAP.** Dense $N\in[400,1800]$, 8 seedů, 2D — minuty až desítky minut (srov. VYPOCET-04 runtime). `central_charges` je exact-rational, instant. Lze spustit příští kolo.

**Anti-circularity:** $\kappa=\sqrt N/(4\pi)$ je z literatury (Sorkin-Yazdi 1712.04227), ne laděno; cílové racionály pre-registrované; $c_{\rm scalar}$ z F-029 je nezávisle naměřený PŘED srovnáním.

---

### 3.2 STŘEDNÍ TEST — H-C: heat-kernel most NCG ↔ spectral-dimension

**Cíl/diskriminátor.** Ukázat, že spektrální dimenze a $a_4$ koeficienty žijí z téhož $D^2$-spektra: spočítat $d_s(\sigma)$ a heat-kernel koeficienty $a_0,a_2,a_4$ z JEDNOHO Diracova operátoru a ověřit, že UV $d_s$ a $a_4$-poměr jsou konzistentní funkce téhož spektra.

**Setup:**
1. **Spektrum:** `toe.spectraltriple.dirac_from_kernel(K)` na sprinkled causal setu (2D/4D) → Diracovo $D$.
2. **Spektrální dimenze:** `toe.spectral.spectral_dimension(sigma, F, D)` / `d_s_uv(...)` z návratové pravděpodobnosti $\mathrm{Tr}\,e^{-\sigma D^2}$.
3. **Heat-kernel koeficienty:** z téhož $\mathrm{Tr}\,e^{-\sigma D^2}$ malého-$\sigma$ rozvoje extrahovat $a_0,a_2,a_4$ a porovnat $a_4$-poměr s `toe.ncg.spectral_action_ratio()` ($=-18/11$) v kontinuální limitě.
4. **Diskriminátor:** souhlasí UV exponent $d_s$ a $a_4$-poměr z téhož spektra s analytickými hodnotami (GR $d_s=4$; $a_4$-poměr −18/11 pro Diracův obsah) do tolerance F-001 (0.06)?

**Feasibility tier: MEDIUM.** Sparse `eigsh` path $N\le12000$; vyžaduje čistou extrakci heat-kernel koeficientů z diskrétního spektra (finite-N drift, srov. F-012 $\alpha$-drift varování). 1 den.

---

## 4. Hlavní teoretická rizika a limity (honesty filter)

| Překryv | Reálná shared-math? | Kde hrozí numerologie | Honesty verdikt |
|---|---|---|---|
| **H-A** trace-anomaly↔spectral-action | **ANO, dokázaná věta** (týž $a_4$) | Žádná — to je F-003/F-014. | Most patří do grafu jako `well`; nejde o spekulaci. |
| **H-B** −18/11↔EE-koef. | Částečně: $a$-věta + CHM svazují $a$ s sférickou EE; F-029 už extrahuje $c_{\rm EE}$. | Naše pole je **skalár**, ne fermion → přímý cíl je $-3$, ne −18/11; $c_{\rm EE}$ může být řízen κ-cutoffem (geometrie), ne anomálií. | Levný test rozhodne; negativní výsledek je stejně cenný (oddělí geometrický vs anomální koeficient). Nepřeprodávat jako „naměřili jsme −18/11". |
| **H-C** NCG↔spectral-dimension | ANO: týž heat-kernel/$D^2$. | $d_s$ je probe-závislá (F-001/F-002) → „NCG $d_s$" není jednoznačné; finite-N drift koeficientů (F-012). | Hrana `shared-math/barely` je oprávněná hned; kvantitativní vztah −18/11↔$d_s$ je otevřený. |
| **H-D** −18/11↔AS fixed-point | Slabá: FP-poměr je schéma-závislý, na rozdíl od $a_4$. | Vysoká: rovnost s −18/11 by byla pravděpodobně koincidence truncation. | Spekulace; netestovat bez FRG. Označit ⚠️. |
| **H-E** index↔diskrétní topologie | Analogická, ne nutně shared-math. | Velmi vysoká: $\sigma=16$ je hladká-spin vlastnost; causal set ji přímo nemá. | Spekulace pro úplnost; ne k testu. |
| **H-F** 11/18 racionál vs kontinuum | Meta-pozorování, ne fyzika. | Čistá numerologie bez mechanismu. | Jen organizační princip („racionál = indexová stopa"). |

**Společné riziko (cross-HW, finite-N):** všechny SSEE veličiny mají noise floor ~$10^{-10}$ a finite-N drift (CLAUDE.md tolerance filozofie); koeficienty porovnávat přes CV napříč seedy/HW, ne bodově. Cílové racionály VŽDY pre-registrovat (direktiva #5, anti-circularity).

---

## Návrh hran do connections.json (NEPŘIDÁVAT automaticky — jen návrhy)

> Vše čeká na editorské rozhodnutí + (kde uvedeno) výpočet. Formát odpovídá `connections.json` (`from`/`to`/`type`/`explored`/`description`).

1. **`spectral-action` ↔ `trace-anomaly`** — `type: shared-math`, `explored: well`.
   *Evidence:* F-003, F-014; draft-02 §2. $a_4(D^2)$ je společný rodič; $C^2$/Euler poměr = $c/(-a)$ = **−18/11** přesně. **Nejsilnější návrh** (dokázaná identita, most prokazatelně chybí).
2. **`spectral-action` ↔ `central-charge`** — `type: shared-math`, `explored: well`. Stejná evidence; $(a,c)$ jsou definovány jako $a_4$ koeficienty $E_4$/$W^2$.
3. **`noncommutative-geometry` ↔ `trace-anomaly`** — `type: shared-math`, `explored: partially`. Pilířová hrana zastřešující #1/#2.
4. **`noncommutative-geometry` ↔ `spectral-dimension`** — `type: shared-math`, `explored: barely`.
   *Evidence:* link-predictions.json score **0.896** (top NCG kandidát); `heat-kernel-expansion→spectral-dimension` už existuje → most je „o uzel daleko". Týž $\mathrm{Tr}\,e^{-\sigma D^2}$.
5. **`noncommutative-geometry` ↔ `entanglement-entropy`** — `type: conjecture`, `explored: barely`.
   *Evidence:* H-B; $(a,c)$ řídí univerzální EE členy (Solodukhin, CHM); F-029 extrahuje $c_{\rm EE}$. **Podmíněno testem §3.1.**
6. **`trace-anomaly` ↔ `entanglement-entropy`** — `type: shared-math`, `explored: partially`. $a$ = sférická EE (CHM), $c$ = log-koeficient (Solodukhin). Most do linie B.
7. **`a-theorem` ↔ `spectral-dimension`** — `type: conjecture`, `explored: barely`. Oba počítají efektivní d.o.f./dimenzi pod RG; podmíněno H-C.
8. **`a-theorem` ↔ `entanglement-entropy`** — `type: shared-math`, `explored: well`. CHM: $a$-věta dokázána přes EE monotonii (známá literatura; uzavírá ostrov `a-theorem`, který má dnes 1 hranu).

---

*Zdroje (repo-present): findings.json F-003/F-014/F-020/F-015/F-019/F-023/F-029; papers/draft-02-a4-fermionic-identity/draft.md; lib/toe/ncg.py, entropy.py, vntype.py, spectral.py, spectraltriple.py; core-data/concept-graph.json, connections.json, link-predictions.json. Externí konvence (citovat v originále): Duff arXiv:2003.02688; Chamseddine–Connes hep-th/9606001; Vassilevich hep-th/0306138; Solodukhin (EE log-koef.); Casini–Huerta–Myers (sférická EE = a); Komargodski–Schwimmer (a-věta). Žádné arXiv ID nevymyšleno; nepotvrzené reference neuvedeny.*

---

## Výsledky kola 19 (2026-06-08)

### H-B — EE-koeficient vs trace-anomálie (VYPOCET-35, F-039)

**Verdikt: no-match-geometric (ostrý NEGATIV)**

Univerzální diskrétní SSEE koeficient `c_EE = 7.562 +/- 1.3% (CV)` z F-029 de Sitter static-patch area-law neodpovídá **žádnému** pre-registrovanému trace-anomálnímu racionálu ze 6 kanálů × 10 kandidátů (60 srovnání, `matches_within_5pct=[]`). Klíčová čísla:

- Přímý skalární cíl `|c/(-a)| = 3`: residual **152 %**.
- Sekundární indexem chráněné NCG/Weyl-fermionové jádro `|-18/11| = 1.636`: residual **362 %**.
- Nejbližší kandidát: geometrická/kontrolní konstanta 8 (residual 5.47 %, stále **NAD** prahem 5 %).
- Čerstvý 2D diamant: c_log = 0.227, 1/c_log = 4.41 — taktéž žádná shoda s anomálními racionály.

**Závěr:** c_EE je GEOMETRICKÝ (kappa-cutoff řízený) koeficient, NIKOLI konformně-anomální náboj. Indexem chráněné NCG jádro -18/11 se přes tento kanál entanglement-entropy NEDOTÝKÁ vlajkové linie B. Anti-cirkularita ověřena strukturálně. Scope: 2D, finite-N, massless scalar; ne 4D kontinuální tvrzení. **F-039 zapsáno, status: confirmed (negativní/diskriminační).**

### H-E — index-náboj diskrétní (VYPOCET-36, F-040 NEPŘIDÁN)

**Verdikt: refuted (čistý negativní výsledek, VYPOCET-36 dokumentuje)**

H-E v přímé formě VYVRÁCENA — a je to cenný, ostrý výsledek:

- **Probe B** `eta(iDelta) = 0.000` na 48/48 bězích (CV = 0): strukturálně nula kvůli ±-párovanému Pauli-Jordanovu spektru. NENÍ to Rohlinův `ind=0`, je to ABSENCE chirálního gradování γ5.
- **Probe A** `eta(D_K)~N^1.02` (slope 1.019, eta/N~0.21, CV=0.42): extenzivní objemový mode-count, pravý opak N-nezávislého topologického náboje.
- **Probe C**: n_rel~N^2.00, n_link~N^1.20, n_mol~N^0.32 — všechny extenzivní.

Indexová ochrana -18/11 (Atiyah-Singer Â, Rohlin σ=16 => ind=-2) je vlastnost HLADKÉHO gradovaného Riemannského spinového sektoru, ne Lorentzovského causal setu. Skutečný most by vyžadoval: euklidizaci, chirální gradování (γ5, even spectral triple), saturující/kvantovaný invariant (Regge/CDT Euler χ nebo APS spektrální flow). Most existuje jen na úrovni NCG↔NCG gradovaných spektrálních triplů, NE causal-set↔Rohlin. **F-040 NEPŘIDÁN** (čistě negativní/analogický výsledek, ne nový finding).

### Hrany nakresleně v kole 19 (+6)

Pipeline dodržen: fragmenty → consolidate → link-prediction.

| Hrana | Typ | Explored | Zdůvodnění |
|---|---|---|---|
| spectral-action ↔ trace-anomaly | shared-math | well | F-003/F-014, hep-th/9606001, hep-th/0306138 — dokázaná identita |
| spectral-action ↔ central-charge | shared-math | well | táž evidence; (a,c) = a4 koeficienty E4/W² |
| noncommutative-geometry ↔ trace-anomaly | shared-math | partially | pilíř-level umbrella nad #1/#2 |
| noncommutative-geometry ↔ spectral-dimension | shared-math | barely | link-pred score 0.896, týž Tr(e^{-σD²}) heat-kernel |
| trace-anomaly ↔ entanglement-entropy | shared-math | partially | CHM + Solodukhin kontinuální CFT; H-B negativní pro diskrétní c_EE |
| a-theorem ↔ entanglement-entropy | shared-math | well | CHM a-věta přes EE monotonii; uzavírá a-theorem ostrov |

**Podmíněná hrana NCG↔entanglement-entropy (LOV návrh #5) NEPŘIDÁNA** — H-B test (VYPOCET-35) ji měl potvrdit, ale výsledek byl no-match-geometric → hrana zůstává podržena a je tímto testem OSLABENA, ne potvrzena.

Link prediction po kole 19: edges 1638 (+6), AUC mean 0.9057 (bylo 0.9034), std 0.0108 (utaženo), P@50 0.9975 (beze změny). Všech 6 nových hran vypadlo z kandidátní listiny. Nový top kandidát: conceptual-problems↔emergent-gravity (score 0.978).
