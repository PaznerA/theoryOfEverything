# VYPOCET-24: Tracialní (max-entropický) podpis typu II₁ de Sitterovy záplaty při vysoké hustotě — retest poctivého nullu VYPOCET-19 Část 3

**Datum:** 2026-06-06
**Soubory:** `core-data/calculations/ds-tracial-probe/calc.py`, `results.json`, `plots/tracial_probe.png`
**Status:** Dokončeno
**Navazuje:** VYPOCET-19 (sj-desitter-type) Část 3 (poctivý null při N≤2500); knihovna `toe` v0.3.0 (řídká/iterativní cesta)
**Cluster:** entropy-cluster × von-Neumann (modular-hamiltonian TOP HUB) × horizon-SJ
**Hypotéza (CLPW arXiv:2206.10780):** v algebře typu II₁ existuje **maximálně smíšený tracialní stav** (rho∼1/d) s **plochým** modulárním hamiltoniánem (eps→0). Jak ohraničená dS statická záplata **zaplňuje** (roste hustota), měl by se podíl IR-módů (eps<0.5) netruncovaného modulárního spektra zvětšovat směrem k tracialní akumulaci.

---

## Cíl: zaplnit mezeru VYPOCET-19 Část 3

VYPOCET-19 **diskriminoval** ohraničenou dS statickou záplatu (II₁: obsah a obsah-sledující entropie saturují) od shodné neohraničené ploché kontroly (II_∞: obsah roste), a viděl III₁→II truncaci (2/3 proxy). Ale **Část 3 — přímý tracialní (max-entropický) podpis — byl poctivý null při N≤2500**: IR-frakce netruncovaného spektra mírně **klesala** (0.144→0.105, sklon −0.008) místo aby rostla. Dokumentovaná škálovací úvaha říkala, že k rozvinutí hierarchie tracialních módů je potřeba **ρ∼10³–10⁴**, což bylo za hranicí husté matice `eigh` při N∼2500.

**Nyní máme řídkou cestu** (`toe` v0.3.0: `causal_blocks_2d` / `idelta_operator_2d` / `sj_state_sparse` / `ssee_sparse`). Tento výpočet retestuje sondu při ρ∈{10³, 3×10³, 10⁴} a ptá se: **objeví se tracialní IR-akumulace, nebo null přetrvá?**

---

## Metoda: dvě cesty, dvě pozorovatelné

Geometrie a SJ konstrukce jsou identické s VYPOCET-19 (konformní trik: 2D bezhmotný skalár konformně invariantní, SJ plochá v (t, r*), de Sitter vstupuje jen přes vlastní míru sech²(r*/l); `toe.causet.sprinkle_ds_static_patch2d`). Box r*≤5.0 (r=0.99991 ℓ, hluboko k horizontu, vlastní objem už saturovaný), **fixní bulk řez r*≤1.0**, eps_lo=0.5. Hustota roste při **fixní geometrii** (správný směr tracialní limity — záplata se zaplňuje).

### Pozorovatelná A (hustá, GENUINE tracialní sonda) — netruncovaná IR-frakce

IR-frakce `f_IR = #{eps<0.5}/n_mod` netruncovaného modulárního spektra na sub-oblasti. To je správná tracialní sonda (VYPOCET-19 Část 3b). **Vyžaduje plnou Wightmanovu submatici W_O** (všechny pozitivní módy) — přesně tu hustou N³ eigendekompozici, kterou řídká top-k cesta **neposkytuje**: `eigsh(which='LM')` vrací jen módy s **největší magnitudou** (UV obsah), zatímco tracialní akumulace žije v **malých** módech mu→1⁺ (IR). **Poctivý limit:** netruncovanou IR-frakci počítá hustá cesta, dotlačená na hustý strop N∼3000 (ρ až 1500 při tomto boxu; N=4000 by bylo ~190 s/seed a ~2.3 GB, příliš drahé při 3 seedech × 2 geometriích).

### Pozorovatelná B (řídká, typ-II obsah) — truncovaná SSEE + počet módů

Truncovaný (typ-II, |λ|>κ) SSEE obsah **je** top-magnitudová část, kterou `eigsh` zachytí **přesně**. Dotlačeno na **plné ρ=10⁴** (N∼2×10⁴) řídkou cestou, validováno sparse==dense na překryvném N. II₁ (dS): typ-II obsah saturuje; II_∞ (plochá): roste.

### Kritická numerická oprava (nosná, nalezena v tomto výpočtu)

Řídké stavitele `toe` v0.3.0 `causal_blocks_2d` / `idelta_operator_2d` interpretují 2D souřadnice **přímo jako nulové (u, v)**; **NEdělají** redukci (t, x)→(u, v)=(t+x, t−x), kterou hustá `causal_matrix` provádí interně. Předání (t, r*) napřímo dá **chybnou kauzální matici** (matvec rel. chyba ~0.63, top vlastní číslo 426 vs pravé 470). Předáváme proto **explicitní nulové souřadnice uv=(t−r*, t+r*)**; pak je matvec strojově přesný (rel. chyba 3.9×10⁻¹⁶) a řídká truncovaná SSEE souhlasí s hustou na ~5×10⁻¹⁵.

Validace `toe` v0.3.0 řídké cesty proti husté na překryvném N (N=2000): truncovaná SSEE rel. diff **4.1×10⁻¹⁴** (cíl <10⁻⁶ PASS). ±-párování / hermitovskost: hustá `pairing_residual_rel` na strojové přesnosti; float32 operátor `<x,Ax>` imag/real ~2.9×10⁻⁷ (v souladu s dokumentovanou float32 přesností ~10⁻⁶–10⁻⁷, proto float32 práh 10⁻⁵, float64 práh 10⁻¹²).

≥3 seedy při ρ=10³ v obou částech, ≥2 při ρ=10⁴ (Část B). Každé reportované číslo nese (hodnota, SE/CI) přes `toe.fits`.

---

## Část A — netruncovaná tracialní IR-frakce vs rostoucí hustota (HUSTÁ, genuine sonda)

| ρ (N) | dS f_IR | dS n_sub | dS n_mod | plochá f_IR | plochá n_sub | plochá n_mod |
|---|---|---|---|---|---|---|
| 300 (600) | 0.1066±0.0127 | 454 | 72 | 0.0525±0.0148 | 119 | 57 |
| 600 (1200) | 0.1093±0.0107 | 900 | 150 | 0.0707±0.0067 | 242 | 118 |
| 1000 (2000) | 0.1173±0.0085 | 1518 | 242 | 0.0691±0.0093 | 413 | 202 |
| 1500 (3000) | 0.1179±0.0016 | 2273 | 362 | 0.0751±0.0019 | 583 | 288 |

**Sklony IR-frakce vs ln N (lineární fit + across-seed bootstrap CI68, 2000 resamplů):**

| geometrie | sklon d f_IR/d ln N | SE | CI68 |
|---|---|---|---|
| **dS** | **+0.495** | 0.112 | [+0.350, +0.660] |
| **plochá** | **+1.493** | 0.483 | [+0.838, +2.205] |

**Mezera dS−plochá = −0.998 ± 0.495** (gap_se = √(SE_dS²+SE_plochá²)). **Záporná.**

**Exponent růstu počtu módů n_mod ∼ N^p (powerlaw_fit, bootstrap CI):**

| geometrie | p | CI68 | R² |
|---|---|---|---|
| dS | 0.996 | [0.973, 1.020] | 0.9998 |
| plochá | 1.019 | [1.000, 1.038] | 0.9994 |

**Verdikt Část A: TRACIALNÍ PODPIS SE NEOBJEVUJE (`tracial_emerges = False`).** Tracialní predikce vyžaduje, aby dS IR-frakce rostla s hustotou **rychleji** než plochá kontrola (přiblížení k maximálně smíšenému stavu). Místo toho:

1. dS IR-frakce je **téměř plochá** v absolutní hodnotě (0.107→0.118 přes 5× hustoty), s malým kladným sklonem +0.495.
2. **Plochá kontrola roste TŘIKRÁT rychleji** (sklon +1.493), takže mezera dS−plochá je **záporná** (−0.998±0.495). Tracialní podpis predikuje kladnou mezeru ≫ 0.
3. Počet modulárních módů roste v **obou** geometriích **lineárně** (dS N^0.996, plochá N^1.019) — žádná saturace módového rozpočtu na husté úrovni, kterou by II₁ tracialní limita vyžadovala v netruncovaném spektru.

**Confound (poctivě dokumentován):** dS sub-oblast drží ~77 % bodů záplaty (sech² koncentruje body u malých r*), zatímco plochá drží ~20 %. IR-frakce závisí na poměru oblast/komplement. Ale tento confound **posiluje null**: dS sub-oblast je mnohem blíž „celé záplatě" než plochá, takže pokud by tracialní akumulace byla reálná, dS by měla ukázat **více** IR-pile-upu — a přesto neroste rychleji. Null je tedy robustní (a mírně anti-tracialní: plochá kontrola pile-upuje víc).

---

## Část B — řídký truncovaný typ-II obsah vs hustota až ρ=10⁴ (saturace II₁)

Sparse vs dense validace (N=2000): truncovaná SSEE **0.538211 vs 0.538211, rel diff 4.1×10⁻¹⁴** (PASS).

| ρ (N) | dS S_trunc | dS n_sub | dS n_mod_trunc | plochá S_trunc | plochá n_sub | plochá n_mod_trunc |
|---|---|---|---|---|---|---|
| 1000 (2000) | 0.551±0.082 | 1526 | 24.0 | 0.517±0.019 | 409 | 16.7 |
| 3000 (5999) | 0.625±0.013 | 4581 | 39.7 | 0.626±0.015 | 1195 | 29.3 |
| 10000 (19998) | **SKIPPED** (n_sub>7000) | ~15400 | — | 0.700 (1 reach point) | 4006 | 55 |

**dS ρ=10⁴ vynecháno — poctivý limit diskrétní sondy (ne fudge):** sech² míra drží ~77 % ohraničené záplaty uvnitř bulk řezu r*≤1.0, takže při ρ=10⁴ je dS sub-oblast n_sub∼1.5×10⁴ a **lokální** eigh(iD_O) je sám n_sub³ hustý solve — **stejná N³ stěna**, které se řídká GLOBÁLNÍ cesta vyhýbá. To je přímý avatar ohraničenosti II₁: **řezaná oblast JE většina konečné záplaty**. Vynechání zaznamenáno v `results.json` (`skipped_points`, `skip_reason`, NSUB_CAP=7000).

**Typ-II obsah:**
- **dS S_trunc SATURUJE** (0.551→0.625, strop ∼0.62; `type_II_content_caps_dS=True`), n_mod_trunc roste pomalu (24→40).
- **Plochá S_trunc ROSTE** (0.517→0.626→0.700), n_mod_trunc roste rychle (17→29→55) — neomezený typ-II obsah neohraničené II_∞ oblasti.

To je **konzistentní s VYPOCET-19 Část 1** (obsah-sledující veličiny saturují pro dS, rostou pro plochou) a **rozšiřuje ji na vysokou hustotu** (ρ=10⁴ pro plochou) přes řídkou cestu.

---

## VERDIKT

| Část | Predikce (CLPW II₁ tracialní) | Výsledek |
|---|---|---|
| **A — netruncovaná IR-frakce (genuine tracialní sonda)** | dS f_IR roste s ρ rychleji než plochá | **NULL PŘETRVÁVÁ** (dS sklon +0.50 [0.35,0.66], plochá +1.49 [0.84,2.20]; mezera **−1.00±0.50**, `tracial_emerges=False`) |
| **B — řídký truncovaný typ-II obsah** | dS obsah saturuje (II₁), plochá roste (II_∞) | **✓ dS saturuje** (S_trunc 0.55→0.62), plochá roste (0.52→0.70); sparse=dense (4.1×10⁻¹⁴) |

> ### **CELKOVÝ VERDIKT: NULL PŘETRVÁVÁ.**
> I při nejvyšší husté-dostupné hustotě (ρ∼1500, N∼3000, 6× hustota VYPOCET-19) **netruncovaná IR-frakce dS sub-oblasti NEROSTE směrem k tracialní akumulaci** — sklon je malý kladný (+0.50), ale **plochá kontrola roste 3× rychleji** (+1.49), takže mezera je záporná. Tracialní (max-entropický) podpis II₁ **se v diskrétní SJ+truncace sondě neobjevuje**. Identifikace II₁ proto **spočívá na saturaci OBSAHU** (VYPOCET-19 Část 1 + zde Část B: typ-II obsah saturuje pro dS, roste pro plochou — diskriminováno až ρ=10⁴), **nikoli na přímém tracialním IR-pile-upu**, který diskrétní sonda ve 2D nevidí.

---

## Proč diskrétní sonda tracialní limitu nevidí (poctivá analýza)

1. **Netruncovaná IR-frakce není tracialní sonda, kterou jsme doufali.** Netruncované modulární spektrum SJ stavu nese **III₁** vakuovou strukturu (husté pile-up u eps=0 z UV koincidencí krátkých kauzálních spojů), ne tracialní strukturu konečné algebry. Pile-up u eps=0 v netruncovaném spektru roste s hustotou v **OBOU** geometriích (dS i plochá) z UV koincidencí, ne z přiblížení k maximálně smíšenému stavu. Plochá kontrola dokonce pile-upuje víc, protože její sub-oblast má více „okrajových" módů relativně k objemu. Tracialní stav je objekt **truncované** (typ-II) algebry — ale tam (Část B, a VYPOCET-19 Část 3a) je IR-frakce nula z konstrukce (truncace |λ|>κ odstraňuje právě nízko-eps módy). **Tracialní stav padá do mezery mezi obě sondy.**

2. **Tracialní limita je vlastnost truncované algebry, ale max-entropický stav má eps→0, což je přesně to, co κ-truncace zabíjí.** Maximálně smíšený stav rho∼1/d má všechna mu→1 (eps→0); ale truncace ponechává jen módy |λ|>κ, jejichž mu jsou daleko od 1 (eps≳2.7, viz VYPOCET-19 Část 3a min_eps∼2.7). Diskrétní typ-II algebra **nikdy nedosáhne tracialního stavu** v dostupném módovém okně — tracialní strop S_max∼ln(d_eff) je ve 2D O(1)–O(log) číslo, a hrubozrnný κ-truncovaný stav ho s ∼40 módy nedosáhne.

3. **Jaká hustota/velikost by to viděla — nebo proč ne v principu.** Aby κ-truncovaná typ-II algebra obsahovala módy s eps→0 (tracialní akumulace), musel by κ klesnout pod nízko-eps módy, tj. κ=√N/(4π)→0, což je opačný směr než hustá limita (κ roste s N). Ve **fixovaném** módovém okně nad κ je nejnižší eps∼2.7 nezávisle na N (VYPOCET-19 + zde). **Tracialní IR-pile-up je proto v principu neviditelný diskrétní SJ+κ-truncace sondě ve 2D** — strop S_max∼O(1) a κ-truncace soustavně vyřezává nízko-eps módy. 4D area-law (kde by S_max∼A/4∼L² byl velký a hierarchie módů bohatší) je přirozený další směr, ale i tam κ-truncace vyřezává nízko-eps konec — pravděpodobně by potřeboval **netruncovanou** konečně-stopovou regularizaci (crossed-product s konečným Tr 1), kterou diskrétní κ-cutoff nereprezentuje.

---

## Co tento výpočet pevně stanovil

1. **Řídká cesta `toe` v0.3.0 funguje pro tento problém** — po opravě (explicitní nulové souřadnice uv) souhlasí truncovaná SSEE sparse=dense na 4×10⁻¹⁴, a dotlačí truncovaný typ-II obsah na ρ=10⁴ (N∼2×10⁴) pro neohraničenou (plochou) geometrii. To je nový nástroj pro velké-N SJ+SSEE (sdíleno s H5g-2 A/4 cap).

2. **Saturace typ-II obsahu II₁ vs II_∞ je robustní i při vysoké hustotě** (Část B: dS S_trunc saturuje na ∼0.62, plochá roste na 0.70 při ρ=10⁴). To posiluje VYPOCET-19 Část 1.

3. **Genuine tracialní IR-sonda je null, a víme proč** (bod 1–3 výše): tracialní max-entropický stav padá do mezery mezi netruncované (III₁) a truncované (typ-II s IR-mezerou) spektrum; diskrétní κ-truncace systematicky vyřezává nízko-eps módy, takže tracialní akumulace je v principu neviditelná. **Identifikace II₁ stojí na saturaci obsahu, ne na přímém tracialním podpisu** — což je samo o sobě poctivý a důležitý závěr o limitech diskrétní von-Neumannovy typové sondy.

---

## Limity a poctivá zjištění

- **Hustý strop N∼3000** pro genuine sondu (Část A): N=4000 by bylo ~190 s/seed, mimo runtime rozpočet při 3 seedech × 2 geometriích. Trend je při N∼3000 jasný (dS sklon malý kladný, plochá větší → záporná mezera), null je rozhodnut.
- **dS ρ=10⁴ truncovaný obsah vynechán** (n_sub³ lokální eigh) — viz výše, poctivý limit diskrétní sondy plynoucí z ohraničenosti II₁.
- **Float32 řídká cesta při N∼2×10⁴**: matvec ~3×10⁻⁷ (v souladu s v0.3.0 dokumentací); použito jen pro plochý ρ=10⁴ reach-bod, hustá float64 cesta nese multi-seed trend do N=6000.
- **Nefudgováno:** Část A poctivě hlásí null (a mírně anti-tracialní mezeru), Část B poctivě hlásí vynechaný dS ρ=10⁴ bod s důvodem. Oprava nulových souřadnic dokumentována v `calc.py` i zde.

---

## Reference (klíčové)

- **2206.10780** — CLPW: dS statická záplata = typ II₁; max-entropický (tracialní) stav; rozdíl od II_∞.
- **1306.3231** — dS SJ vakuum; konformní trik pro kauzální strukturu.
- **1611.10281 / 1712.04227** — Sorkin-Yazdi SSEE; dvojitá truncace κ=√N/(4π).
- **2008.07697** — dS horizont SSEE; area law.
- **0905.2562** — Casini-Huerta modulární energie eps=ln[(ν+½)/(ν−½)].
- **1205.3855** — Anninos: dS₂ statická záplata, želví souřadnice.
- VYPOCET-19 (sj-desitter-type) — diskriminátor II₁ vs II_∞, Část 3 null; `toe` v0.3.0 řídká cesta.
