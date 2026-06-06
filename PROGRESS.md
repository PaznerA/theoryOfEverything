# Progress tracker — Theory of Everything

> ⏸️ **PAUZA (2026-06-06 ~11:00)** — na žádost uživatele (tokenový limit). Kolo 9 zastaveno v půlce: VYPOCET-19 (SJ de Sitter II₁ test) a VYPOCET-20 (BD 4D modulární tok) nedokončené (adresáře v `core-data/calculations/` založené, writeupy chybí), ESEJ-04 a `papers/REVIZE-PRO-CLOVEKA.md` nenapsané. **Obnovit:** spustit znovu workflow `workflows/qg-round-09.js`; poté plán BRAINSTORM-05 + závěrečná zpráva dne.

## Aktuální stav

🟢 **Fáze 2: Hledání souvislostí** — kola 3–8 dokončena (2026-06-06): 4 drafty článků (draft-01 v0.2 SJ rotující prostoročasy, draft-02 a₄ fermionová identita, draft-03 d_s jako klasifikátor, draft-04 typ-přechod kauzální množiny). VYPOCET-17 vyvrátil H4g-3: žádná druhá index-identita pro Λ neexistuje; −18/11 přežívá přítomnost kosmologického členu právě proto, že se na něj NErozšiřuje; draft-02 Λ-riziko uzavřeno. VYPOCET-18 podpořil H4g-1 v 2D (4/5 geometrických signatur; modulární tok geometrický na slabu, non-geometrický v rozích diamantu přesně tam kde F-016 lokalizoval Hadamardovu anomálii); 4D nereplikuje (link-matice řídkost). findings.json = 22 nálezů.

## Fáze

| # | Fáze | Stav | Zahájeno | Dokončeno |
|---|---|---|---|---|
| 1 | Základní rešerše (18 pilířů QG) | ✅ dokončeno | 2026-06-05 | 2026-06-05 |
| 2 | Hledání nenalezených souvislostí | 🟡 zahájena | 2026-06-05 | — |

## Log

### 2026-06-06 (kolo 8 — VYPOCET-17/18, draft-04, housekeeping)

- **VYPOCET-17 — Λ-indukce přes spektrální akci (H4g-3, F-020):** Exaktní sympy + literatura (CC hep-th/9606001 + Marcolli). Tr f(D/Λ) ~ 2Λ⁴f₄·a₀ + 2Λ²f₂·a₂ + f₀·a₄. a₀ (kosmologický) a a₂ (Einstein-Hilbert) jsou oba lineárně v N = Tr(1_F), ale sedí na různých cutoff-řádech (f₄Λ⁴ vs f₂Λ²) → jakýkoli poměr nese (f₄/f₂)Λ² = dimenzionální a scheme-závislý; jedině −18/11 (poměr uvnitř a₄, stejný řád f₀Λ⁰) je index-chráněný. Λ_cc/m_Pl² = π²f₄/(2N f₂²k̂²) nese explicitní 1/N. Indukovaná γ₀ cutoff-kvartická (~10¹²² mismatch). STr 1 = n_B − n_F = −62 (bez ν_R) / −68 (s ν_R): ν_R rovnováhu počtů zhoršuje, nezlepšuje. Všech 8 interních VERDICT klíčů True. **H4g-3 je VYVRÁCENA jako pozitivní hypotéza. Draft-02 Λ-riziko uzavřeno.** (F-020)
- **VYPOCET-18 — modulární tok: slab vs. diamantový roh (H4g-1, F-021):** 2D, N=400–1800, 5 seeds. Self-test: corr(H_pi diagonála, analytická boost-váha)=0.992. Klíčový výsledek: off-diagonální sklon modulárního kernelu SJ stavu = −0.47 (slab, geometrický/boost-lokální) vs. −0.094 (diamant, negeometrický), gap 0.37 stabilní. Slab diagonální modulární váha lineární v vzdálenosti od entangling surface (R²=0.977, BW boost-váha). Per-site non-lokalita f_nl roste monotónně 0.673 (hluboký bulk) → 0.828 (roh), sklon vs. vzdálenost-k-rohu = −0.383 (R²=0.989); roh/bulk ratio = 1.15. Poctivé nuly: cross-corner u-v′=±2L coupling ratio=1.00; integrovaná f_nl neodliší slab(0.72) od diamantu(0.72) — diskriminace jen v off-diag sklonu. 4D (link matice, N≤2500): NEREPLIKUJE — slab/diamant ratio=0.996, rohová f_nl (0.11) < bulk (0.31) opačné znaménko, nl-vs-roh sklon=+0.75 (link-matice řídkost ~N^0.65 + tenká rohová statistika). **H4g-1 PODPOŘENA v 2D (4/5 signatur); 4D nereplikuje (poctivý null).** Runtime 248 s. (F-021)
- **draft-04-type-transition-causal-sets:** Draft a TODO zapsány do `papers/draft-04-type-transition-causal-sets/`. Testuje hypotézu Sorkin-Yazdi SSEE truncace = CLPW crossed-product typ III₁→II přechod. 2D diamant: 2/3 proxy (entropická stopa 80x, modulární pile-up N^1.14→0); 4D slab: 3/3 proxy (entropická stopa N^1.34→N^0.55, modulární spektrum flat-dense→integrovatelné, N^{3/4} selektivita). Geometrická výhrada (rohy diamantu ničí signaturu) a interpretace diskrétní škály jako modulárního cutoffu explicitely označeny jako konjektury. TODO.md: 8 lidských verifikačních bran, referee-útok příprava, etická poznámka, LQG-area-gap noha označena jako otevřená. (F-022)
- **findings.json** rozšířen na 22 nálezů: F-020 (H4g-3 vyvrácena, žádná druhá index-identita pro Λ, draft-02 uzavřen); F-021 (H4g-1 2D podpořena 4/5, modulární tok geometrický na slabu, negeometrický v rozích); F-022 (draft-04 zapsán, 2D 2/3 + 4D 3/3 proxy, N^{3/4} selektivita).

### 2026-06-06 (kolo 7 — VYPOCET-15/16, BRAINSTORM-04, SYNTEZA-02, housekeeping)

- **VYPOCET-15 — far-zone disambiguace Kerr a=0.6 (H3g-1, F-018):** Log-log diskriminant: corr(log W_sr, log Ω)=0.9992 vs. corr(log W_sr, log 1/(r−r_erg))=0.942 — favorizuje Model S. Joint fit (near+far, n=19, r=2.05–20M): ΔAIC(E−S)=+3894 (rozhodující). Near-zone A_W mocninový zákon (high-SNR n=11): |A_W|~r^{−2.75±0.03} (předp. −3, R²=0.957); |A_W|~Ω^{0.98±0.01} (předp. +1, R²=0.932). Far-zone (r=5–20M, 13 radii): W_sr=0 ve všech 13 poloměrech (pod (ω,k)-mřížkovým rozlišením); A_W<0 na všech 13. **Verdikt: VYPOCET-14 ambiguita pro a=0.6 uzavřena; Ω(r) jako spojitý řídící parametr superradiantního nástupu potvrzen konzistentně pro všechny tři geometrie (Kerr a=0.6, a=0.9, BTZ J=0.9).** Seeds: 5, N=1600. (F-018)
- **VYPOCET-16 — vN-type proxy v 4D slab (H3g-3, F-019):** 4D box-slab, iΔ link matrix, interior half-space cut, T=0.5, L=0.85, N=800–3500, 5 semen. Proxy 1 (entropická stopa): S_full~N^{1.34} (volume/super-volume, III divergentní, 27.5→209.1); S_number-trunc[n_max=2N^{3/4}]~N^{0.55}≈sqrt(N) (4D area law, typ II, 2.69→5.84), kolaps 36x; fixní-frakční kontrola S_frac~N^{0.83} area law NESPLNÍ. Proxy 2 (modulární spektrum eps=ln[mu/(mu-1)]): untruncated pile-up~N^{1.27} (III₁ flat-dense) → přesně 0 po truncaci (typ II, ostrá IR hrana eps~2.7, kompaktní nosič). Módový počet: full ~N^{1.11} → truncated ~N^{0.70} (~N^{3/4}). Proxy 3 (p=3/4 otázka): N^{3/4} number-truncace → area law YES; fixní-frakce SELHÁVÁ; slab spektrum nemá vlastní ostré koleno (auto-koleno ~N^{1.06}) → N^{3/4} je předpis (observer/crossed-product cutoff), ne spektrální rys. Pauli-Jordan +/- párování error = 7.1e-14 (strojová přesnost). **Verdikt: 3/3 proxy projdou — H3g-3 podpořena v d=4.** Runtime 158 s. (F-019)
- **BRAINSTORM-04.md** dokončen: 3 hypotézy čtvrté generace — H4g-1 (rohová non-Hadamardovost = místo kde selhává boost-flow, medium-high), H4g-4 (III→II přechod přežívá na 4D slabu ne na diamantu, medium-high; potvrzena VYPOCET-16), H4g-3 (fermionová indukce predikuje Λ přes f₀/a₀ moment, medium). Doporučená fronta: paralelně H4g-3 (exaktní sympy, dny) + H4g-1 (slab vs. diamantový roh modulární tok, vyšší konceptuální výnos). Soubor: `knowledge-base/BRAINSTORM-04.md`.
- **SYNTEZA-02.md** dokončena: přehled 7 kol, 19 nálezů, 5 uzavřených front (γ–Cardy, naivní Λ, plná SM, 4D volume-law jako dimenze-efekt, Model E pro superradianci); through-line (vlastnosti prostoročasu jako odpovědi na otázky); výhled 10 kol. Soubor: `knowledge-base/SYNTEZA-02.md`.
- **findings.json** rozšířen na 19 nálezů: F-018 (far-zone E-vs-S disambiguace, Ω(r) potvrzen pro všechny geometrie), F-019 (vN-type 4D slab 3/3 proxy, N^{3/4} operativní regulátor, H3g-3 d=4).

### 2026-06-06 (kolo 6 — VYPOCET-13/14, draft-03, ESEJ-03, housekeeping)

- **VYPOCET-13 — 4D SSEE slab geometry (H04 interpretace c, F-016):** Half-space cut (slab, iΔ link matrix, κ=0.05·λmax) dává AREA law: S~L^2.00 (R²=0.982), R²_area=0.984 > R²_vol=0.977. Interiérní edge-effect kontrola: S~L^2.18 (R²=0.989) — čistší area. Kontrast: 4D nested diamant (VYPOCET-06) = VOLUME S~f^6.1 (R²=0.998). **Verdikt: geometrie rohů (ne dimenze) určuje area vs. volume — interpretace (c) POTVRZENA, (a) vyvrácena.** Hadamardova diagnostika (log-log sklon |ReW|): 4D diamant inside=−1.53 vs corner=−2.79 (anomálie v rozích), 4D slab deep=−3.81 ≈ surface=−3.85 (žádná anomálie) — přesná signatura mechanismu (c). 2D diamant inside=−0.160 vs corner=−0.095 (anomálie na u−v′=±2L). Runtime 264 s. N≤2088 (slab, 3 seedy). Caveaty: literatura (2008.07697/2412.07832) nepotvrzuje non-Hadamard↔volume jako přímý mechanismus; absolutní Hadamardovy sklony finite-N deformované. Entropy-cluster program v 4D má živou cestu přes Rindler/slab klín (kde SJ ≈ Unruh = Hadamard).
- **VYPOCET-14 — superradiantní nástup: ergosféra vs. Ω(r) (H3g-1, F-017):** Radial scan W_sr: Kerr a=0.6 [0, 0.145], a=0.9 [0, 0.222] (12 radii each, monotone). Srovnání modelů (AIC): ΔAIC(E vs. S)=+441.6 (a=0.6), +4216.3 (a=0.9), +231.5 (BTZ J=0.9) — všechny tři rozhodující pro Model S (W_sr ~ Ω(r)^B). B=4.23 (a=0.6), 3.82 (a=0.9), 1.71 (BTZ). A_W znaménko: negativně-definitní ve všech 65 externích měřeních (5×8 Kerr + 5×5 BTZ); near-ergosphere |A_W|~0.49–0.60 vs far-zone ~0.03–0.05 (faktor ~15–20). BTZ cross-check J=0.9: stejná kvalitativní struktura (pattern_matches_kerr=True). **Verdikt: H3g-1 POTVRZENA.** Superradiantní váha řízena spojitým Ω(r), ne diskrétní ergosférou. Zbývající nejednoznačnost a=0.6 (lineární korelace mírně favorizuje Model E): Ω(r) a 1/(r−r_erg) korelovány → doporučen hustší scan r=5–20M (VYPOCET-15). N=1600, 5 seeds.
- **draft-03-ds-classifier:** Třetí draft přerámovává UV spektrální dimenzi jako klasifikátor (z, D, sonda); master-tabulka reprodukuje 12 publikovaných čísel z jediného P(σ) enginu; sonda jako třetí klasifikační osa doložena vnitřním rozporem v databázi (CST d'Alembertián vs. náhodná procházka). Sekce „Relation to prior work" vpředu; TODO.md připravuje obranu vůči hlavním referee útokům (Calcagni, probe-trivialita). Soubory: `papers/draft-03-ds-classifier/draft.md`, `TODO.md`.
- **ESEJ-03:** Třetí syntetická esej zapsána.
- **findings.json** rozšířen na 17 nálezů: F-016 (slab area law, rohová geometrie rozhoduje, H04-c potvrzena), F-017 (superradiantní nástup Ω(r) kontinuální, H3g-1 potvrzena).

### 2026-06-06 (kolo 5 — VYPOCET-11/12, draft-01 v0.2, housekeeping)

- **VYPOCET-11 — graviton sektor + index-teorém (H3g-4, calc11):** Fyzikální Einsteinův graviton je NEkonformní — nemá čisté (a,c), jeho anomálie jsou gauge/scheme-závislé a jen on-shell (Duff hep-th/9308075, hep-th/9503187). Konformní Weylův graviton dává c/(−a)=−398/261≈−1.525 (ne −18/11). Per-pole test: žádný boson není kolineární s Weylovým fermionem na rovině (a,c). Plné SM+konf.graviton: −6474/5123≈−1.264. Násobnost gravitonů nutná k vynucení −18/11: x=−143/32<0 (nefyzikální). **Závěr: identita −18/11 je striktní diskriminátor fermionového sektoru; nelze ji zachránit žádným gravitonem.** Index-teorémová část: spinorové koeficienty a₄ v bázi {C²,E₄,R²} jsou (−1/20, +11/360, 0) → (a,c)=(11/360, 1/20), shoda s Duff Tab.1 exaktně; Â-genus dává ind(D)=−σ/8, Rohlin σ=16→ind=−2 (sudé celé, zámek drží). −18/11=koef(C²)/koef(E₄) pro spinor = poměr Gaussovy-Bonnet/χ a Pontryaginovy/Â hustoty → H3g-4 posílena: spektrální akce je Sacharovova fermionově-indukovaná gravitace. Draft-02: dvě nezávislá blokování gravitonové záchrany jsou vnitřně konzistentní, release readiness potvrzena (čeká lidská re-derivace a citace-check).
- **VYPOCET-12 — typ vN algebry + SSEE truncace v 2D (H3g-3, calc12):** 2D, N=400–1800, 8 seeds, kappa=sqrt(N)/(4pi). Proxy 1 (entropy-trace): S_full~N^1.04 (volume, divergent III) → S_trunc saturuje 1.30–1.70 (area/log, finite II), 80x kolaps; Pauli-Jordan nukleární norma odstraní jen ~20% (typ žije v stavu/entropii, ne kinematice). Proxy 2 (modulární spektrum eps=ln[mu/(mu-1)]): untruncated ploché+husté (47–217 módů, pile-up eps<0.5 ~N^1.14, frakce N-stabilní 0.087±0.006) = Connes III₁; truncated integrovatelné (8–20 módů, pile-up=0, IR edge eps>1.6) = typ II. Proxy 3 (centrální posloupnosti): CV(S_trunc) 0.079→0.030 (samo-průměrující), nesignifikantní trend — nediskriminuje typ. **Verdikt: MIXED 2/3 — první přímý numerický důkaz crossed-product obrazu na kauzální množině; je to 2D výrok.** H3g-3: potřeba (a) 4D rozšíření, (b) 30+ seeds pro větší N, (c) analytické srovnání se crossed-product konstrukcí.
- **draft-01-sj-rotating-spacetimes v0.2:** Název aktualizován (přidán „eigenvector signature of superradiance"); abstrakt rozšířen o body (iv)–(vi) (mechanismus, překryv podprostorů 44.6°, superradiantní váha 0.0755); sekce 3.5 a 3.5b plně integrovány (ne přilepeny); sekce 3.6/4.1/4.2 aktualizovány; TODO.md: položky 1.4, 3, 6 označeny DONE; nová položka §8 (lidská re-derivace) jako gate; blokující zbývá: N→∞ studie, analytické SJ pro strižený diamant, srovnání s BTZ dvou-bodovou funkcí, verifikace citací, nezávislý re-run pipeline.
- **findings.json** rozšířen na 15 nálezů: F-014 (graviton+index, graviton identitu −18/11 nezachrání, Rohlinův zámek), F-015 (vN typ proxy, 2/3 III₁→II v 2D).

### 2026-06-06 (kolo 4 — BRAINSTORM-03, VYPOCET-09/10, draft-02, housekeeping)

- **BRAINSTORM-03.md** dokončen: 3 hypotézy třetí generace — H3g-1 (opačná znaménka A_caus/A_W jako superradiantní podpis, medium-high), H3g-4 (spektrální akce jako fermionově-indukovaná gravitace, high), H3g-3 (SSEE truncace = crossed-product modulární cutoff, medium). Doporučení: draft-02 jako nejpevnější aktivum, draft-01 uzavřít po VYPOCET-10.
- **VYPOCET-09 — BD d'Alembertián spektrum (H04 interpretace b):** BD G_R=B⁻¹ dává čistý mocninový zákon λ_k~k^-α (α≈3.0–3.4, R²≈0.99) tam, kde link matice dávala ploché spektrum — interpretace (b) potvrzena pro tvar. Ale α driftuje s N (+1.28 za N=500–3000, nekonvergoval), slope-knee p=0.977≈N¹ (identicky VYPOCET-06), area/volume cutoff-závislé. Hlubší selhání: váha k interpretacím (a) a (c). cond(B) 3.9e6→2.0e10. Runtime 394 s.
- **VYPOCET-10 — SJ eigenvektorová rotace + superradiance + mechanismus:** Kladné SJ podprostory rotujícího vs. statického řezu pootočeny o ~44.6° (cos²≈0.507) při <2% změně spektra — spin je eigenvektorový jev, ne spektrální. Váha v superradiantním klínu ω(ω−kΩ)<0 roste monotónně se spinem (a=0: 0.0000 exaktně → a=0.9: 0.0171) a k ergosféře (0.0000 při r=4.0 → 0.0755 při r=2.05). Toy model nulového diamantu reprodukuje obě znaménka A_caus>0/A_W<0 i velikosti (korelace 0.95–0.97): A_caus=kauzální geometrie clony, A_W=bezhmotná 2D Wightmanova funkce na stlačeném/roztaženém null-směru. Oba nejslabší body draftu-01 (TODO 1.4, 3, 6) vyřešeny.
- **draft-02-a4-fermionic-identity** zapsán: draft.md + TODO.md v `papers/draft-02-a4-fermionic-identity/`; věta o exaktní identitě C²/Euler = −18/11 + heat-kernel descent (§2) + SM falzifikace (−0.853 vs −1.636) + pozice v trojúhelníku Andrianov-Lizzi / Kurkov-Lizzi-Vassilevich. Slabiny: triviality-risk, konvence-závislost, schéma závislost a₄; doporučení: pursue s lidskou re-derivací.
- **findings.json** rozšířen na 13 nálezů (F-009 Kerr-BTZ geometrická nezávislost, F-010 γ–Cardy program closed, F-011 modular-hamiltonian top hub, F-012 BD d'Alembertián spektrum, F-013 SJ eigenvektorová rotace + mechanismus).

### 2026-06-06 (kolo 3 — VYPOCET-08/Kerr, H04-reframe, pilíř 19, draft-01)

- **VYPOCET-08 — Kerr ekvatoriální SJ (H2g-6):** VŠECHNY čtyři BTZ signatury replikovány na Kerru — SJ existuje strojovou přesností uvnitř ergoregionu (787±/790± páry, reziduál ~5e-16); null sklon se nuluje přesně v r_erg=2M pro a=0.6 i 0.9; opačná znaménka A_caus>0 vs. A_W<0 na každém (a,r) (a=0.6 r=2.6: +0.317/−0.296; a=0.9: +0.431/−0.382); A_caus roste monotónně se spinem (0.197/0.361/0.482 pro a=0.3/0.6/0.9). Závěr: SJ vlastnosti ergoregionu jsou geometricky nezávislé v prostředích se strhnutým rámem.
- **H04 — entropie-cluster reframe:** 4D link-matice spektrum ploché ⇒ interpretace (b) — BD d'Alembertián je správný kandidát (VYPOCET-09 navazuje).
- **Pilíř 19 — von Neumannovy algebry:** 27 nových konceptů, 32 ověřených referencí; po konsolidaci je modular-hamiltonian nový TOP HUB grafu (614 uzlů/2437 hran); fragment `von-neumann-algebras.json` uložen, consolidate.py spuštěn manuálně.
- **draft-01-sj-rotating-spacetimes** zapsán: `papers/draft-01-sj-rotating-spacetimes/draft.md` (v0.1) + `TODO.md`; nejslabší bod (opačná znaménka bez mechanismu) → řeší VYPOCET-10.
- **γ–Cardy program ukončen** (kolo 2 blocker Sen IR-universality plně potvrzen).

### 2026-06-06 (rozhodující kolo — H01 verdikt + VYPOCET-05/06/07 + findings.json)

- **γ–Cardy rozhodující čtení (H01 verdict: program-dead):** ENP 1006.0634 neobsahuje explicitní konstantní člen; Sen 1205.0971 potvrzuje, že log-koeficienty jsou IR-určeny (LQG −2 vs. Eukleidovská gravitace +1,71 — nesouhlasí); porovnávat konstantní člen s Carlipem/Cardy je fyzikálně nemotivované. H01 uzavřena. H2g-7 posílena jako definitivní negativní výsledek.
- **VYPOCET-05 — SJ stav v rotujícím BTZ ergoregionu (H2g-6, 2D analog):** 796+/796− eigenvalue, reziduál 4,6×10⁻¹⁶; statický řez na témže r není Lorentzův; kauzální asymetrie uvnitř ergoregionu = +1,000 vs. +0,007 vně; nulový sklon mizí přesně na r_erg=1,0; superradiantní signatura v eigenvektorech/W (ne v hrubém spektru). Teze H2g-6 (Strategie II) numericky potvrzena ve 2D sondě.
- **VYPOCET-06 — 4D SSEE cutoff scaling (H2g-3, p=3/4 predikce):** predikce NEPOTVRZENA; exponent závisí na cutoffu (0,65–0,98); slope-knee dává ~N¹; 4D nested diamant dává VOLUME law (R²=0,998). Jednoduchá 2D→4D extrapolace „změř p ze spektra" selhává. H2g-3 oslabena.
- **VYPOCET-07 — BMV AS fázová korekce (H2g-8):** AS korekce δφ/φ ≈ 6,2×10⁻²⁸ (klasický RG, bez ħ); EFT ≈ 3,4×10⁻⁶² (kvantový, s ħ); poměr AS/EFT ≈ 1,82×10³⁴; obě 24 resp. 59 řádů pod dosažitelností. Oppenheimova varianta (křížové korelace oscilátorů) potvrzena jako jediná realistická kontinuální diskriminace. H2g-8 posílena.
- **findings.json (8 nálezů):** pokrývají d_s probe-dependence (F-001/F-002), fermionový a_4 exaktní + SM falzifikace (F-003/F-004), 140× Λ prefaktor (F-005), ρ^(−1/2) potvrzení + ρ^(−1/4) vyloučení 39σ (F-006/F-007/F-008). Každý rozlišuje reprodukci literatury od projektového přínosu.
- **BRAINSTORM-02.md** doplněn o sekci "Výsledky rozhodujícího kola (2026-06-06)".
- **00-INDEX.md** aktualizován (VYPOCET-05/06/07, findings.json).

### 2026-06-06 (deep-dive kolo 1 — výpočty + dossiery + eseje + BRAINSTORM-02)

- **4 výpočty dokončeny:**
  - **VYPOCET-01 — d_s^UV klasifikační tabulka (L3-1):** Symbolický master d_s^UV = D/γ ověřen (sympy); 12/12 numerických kontrol PASS (tol 0,06); D=4 tabulka: GR→4, Hořava z=2→5/2, Hořava z=3→2, Stelle→2, AS (η_N=−2)→2, causal-set d'Alembertián→2 univerzálně, causal-set random walk→>D, multifraktální→2; všechny IR limity→4. **Verdikt: L3-1 v přerámované podobě PODPORENA** — probe-dependence jako třetí klasifikační osa doložena; řeší vnitřní rozpor connections 657 vs. 1777 (d'Alembertián→2 vs. random walk→>D ze stejné CST teorie).
  - **VYPOCET-02 — a_4 anomaly-matching test NCG SM algebry (L1-1):** Konvence: Duff arXiv:2003.02688, spektrální akce Chamseddine-Connes hep-th/9606001; koef(C²)/koef(Euler) = −18/11 spektrální akce = c/(−a) Weylova fermionu EXAKTNĚ pro 45 i 48 fermionů; faktor 11 sdílen (Euler 11/60, a_Weyl=11/720). Plná SM (N₀=4, N₁=12): −0,853 (bez ν_R) / −0,866 (s ν_R) vs. cíl −1,636. **Verdikt: L1-1 ve fermionové části PŘESNĚ POTVRZENA, v plné SM verzi JEDNOZNAČNĚ FALZIFIKOVÁNA** — obojí čistě; ν_R plnou shodu neuzavře, ale posouvá blíže (mismatch 0,784→0,771).
  - **VYPOCET-03 — Λ prefaktor srovnání:** Konvence: Λ l_P² = κ/√(V/l_P⁴), V=H₀⁻⁴; κ_Sorkin=0,2136, κ_EDT=1,53×10⁻³, κ_CosMIn(eff)=2,45; poměr κ_Sorkin/κ_EDT = 139,6 ≈ 140; Λ_obs l_P²=2,866×10⁻¹²². **Verdikt: silná sjednocující hypotéza VYVRÁCENA** (prefaktory se liší faktorem ~140, neslučitelné konvencí c_V; CosMIn nemá fundamentální κ); sdílí se pouze dimenzionální kostra Λ~H²; srovnání třech prefaktorů v literatuře neprovedeno — publikovatelný negativní výsledek.
  - **VYPOCET-04 — SSEE na sprinklovaném 2D kauzálním diamantu:** Entropický cutoff rank~N^0,519±0,007 → ε~ρ^(−1/2) (2,8 σ od přesně 1/2, ~39 σ od 1/4); intrinsická diskrétnost knee škáluje N^1,00; SSEE: volume-law 95,2 (bez truncace) → area/log-law 1,58 (dvojitě truncováno); 2D log-slope b=0,49 (kontinuum 1/3); N=400–1800, 5 semínek. **Verdikt: MECHANICKY PODPORUJE jádro** — truncace mění volume-law na area/log-law přes UV cutoff ε~ρ^(−1/2); ρ^(−1/4) vyloučeno 39 σ; identifikace s LQG area gapem ve 4D = nadcházející krok. Doporučena oprava entropy-cluster.md ř. 66 z ρ^(−1/4) na ρ^(−1/2).
- **3 dossiery (H01–H03):**
  - **H01 — Cardy-LQG (γ fixace):** jádro c=6k known (Carlip 1410.5763); identifikován blocker: Senova IR-univerzalita (1205.0971) strukturálně brání UV-fixaci γ z CFT; komplexní γ=±i (1212.4060) podkopává reálnou fixaci; priorita snížena.
  - **H02 — SJ vakuum pro Kerr/SdS:** genuinely open territory — žádná publikace SJ stav pro rotující ČD nezkonstruovala; Kay-Wald no-go neblokuje (SJ nevyžaduje Killing-symetrii); doporučen 2D analog (rotující BTZ / ekvatoriální Kerr).
  - **H03 — BMV/QGEM diskriminátor:** binary Q-vs-C test vyřešen (konsensus 2025); AS korekce ~10⁻⁶⁰ neměřitelná; jediný principiálně odlišitelný přístup = Oppenheimova postkvantová teorie (π-fázový posun); nový framing „diskriminátor přístupů" živý.
- **2 eseje:** ESEJ-01 (dimenze jako otázka, probe/observer H2g-1) + ESEJ-02 (vesmír který se počítá, faktor 140 H2g-4, Everpresent Λ H2g-5).
- **BRAINSTORM-02.md** dokončen: 8 hypotéz druhé generace (H2g-1–H2g-8), výpočetní fronta 10 položek, strategický meta-závěr — kalibrace od „velké sjednocení" k „přesným diskriminátorům a falzifikacím".
- Vytvořen `core-data/calculations/` (4 adresáře s calc.py + results.json + plots).
- Aktualizován `knowledge-base/00-INDEX.md` (přidány sekce Výpočty, Hypotézní dossiery, Eseje, BRAINSTORM-02).

### 2026-06-06 (novelty check + oprava d_s rozporu)

- Novelty check 6 klastrů (arXiv/web) + oprava d_s datového rozporu v CST:
  - **d_s klastr (L3-1+L2-5+L5-5):** partially-known → reframe. Hořavův vzorec d_s=1+D/z znám od 2009; novum = jednotný P(s) formalizmus + probe jako třetí parametr d_s(z,D,probe).
  - **d_s datová oprava:** rozpor connections 657 vs. 1777 vyřešen — probe-dependence v CST potvrzena (Eichhorn-Mizera 1311.2530: náhodná procházka → d_s roste; Belenchia et al. 1507.00330: d'Alembertiánová sonda → d_s klesá k 2). Fragmenty causal-sets.json + noncommutative-geometry.json opraveny, registry přebudovány.
  - **a_4 klastr (L1-1+L2-4+L5-4):** partially-known → **pursue**. Dvoustranné mosty pokryty (2010–2013), trojstranná identifikace a_4 + anomaly-matching test pro C⊕H⊕M₃(C) nepublikovány.
  - **Λ klastr (L1-2+L3-2+L2-2):** partially-known → reframe. Tři pilíře zcela nezávisle publikovány; mezipilířový prefaktorový test neproveden ani navržen.
  - **Entropie klastr (L2-3+L3-4+L4-4):** partially-known → **pursue**. Dvoucestné mosty etablovány (2016–2025), trojcestná syntéza SSEE-truncation = crossed-product modular cutoff = LQG area gap chybí; γ jako renormalizační konstanta nepublikováno.
  - **Cardy-LQG (L1-3):** partially-known → reframe. Jádro c=6k + Cardy explicitně publikováno (Carlip 1410.5763); zbývají 2 body: γ↔c=6Q₁Q₅ analogie a CFT log-fixing γ~0.274. Priorita snížena.
  - **Preprint checks (L4-2, L4-5/L4-6, L5-3, L2-1):** partially-known → reframe. Basile et al. 2502.12290 mapují AS/swampland tension; FRG koeficient (L4-2) nový; citace L4-5 ověřeny (Nature 2025 + 3 arXivy); SJ pro Kerr/SdS nepokryto; NCG↔Liouville publikováno, trojstranné tvrzení nepublikováno.
- Vytvořen `core-data/novelty-checks.json` (6 klastrů + dsContradiction entry, pretty-printed).
- Aktualizován `BRAINSTORM-01.md` — přidána sekce "Novelty check (2026-06-06)" s tabulkou a komentáři.
- Přepracována sekce "Prioritní hypotézy" v PROGRESS.md (Tier 1 pursue: a_4 + entropie; Tier 2 reframe: d_s + Λ + preprints; Tier 3: Cardy-LQG).

### 2026-06-05
- Založena struktura knowledge base (README, struktura složek, jazyková politika).
- Spuštěno první velké workflow `qg-knowledge-foundation`:
  - 18 paralelních výzkumných agentů (pilíře: teorie strun, LQG, asymptotická bezpečnost, CDT, kauzální množiny, GFT, nekomutativní geometrie, twistory/amplitudy, emergentní gravitace, supergravitace/UV, holografie/AdS-CFT, černé díry/informační paradox, entanglement↔prostoročas, swampland, semiklasická gravitace, konceptuální problémy, fenomenologie, kvantová kosmologie)
  - adversariální verifikace citací a vzorců
  - konsolidace do jednotných registrů (graf konceptů, reference, vzorce, problémy, souvislosti)
  - syntéza: mapa vztahů + bílá místa
- Economy run (housekeeping agent):
  - Re-verifikace 5 pilířů (causal-sets, group-field-theory, twistors-amplitudes, emergent-gravity, experimental-tests): celkem 39 referencí zkontrolováno, 16 chyb opraveno, 14 zbývajících obav zdokumentováno.
  - Deterministická konsolidace (Python): concept-graph 598 uzlů/2319 hran, references 563, formulas 235, open-problems 145, connections 280 (112 barely explored).
  - Soudcovský průchod deduplikace: sloučeno 7 skupin konceptů (9 ID), 2 duplicitní open-problems páry.
  - Syntéza SYNTEZA.md dokončena (průřez 18 pilíři + matice prozkoumanosti).
  - První brainstorming hypotéz nenalezených souvislostí: BRAINSTORM-01.md (5 analytických čoček, 10+ hypotéz, priority pro Fázi 2).
  - Vygenerován 00-INDEX.md (anotovaný rejstřík celé báze).

## Statistiky

Stav po deterministické konsolidaci (2026-06-05). Celkem načteno 18 fragmentů.

### Per-pillar počty

| Pilíř | Koncepty | Vzorce | Reference | Problémy | Souvislosti |
|---|---|---|---|---|---|
| asymptotic-safety | 32 | 11 | 36 | 7 | 17 |
| black-holes-information | 25 | 16 | 43 | 10 | 17 |
| causal-dynamical-triangulations | 31 | 13 | 32 | 8 | 18 |
| causal-sets | 34 | 12 | 29 | 8 | 15 |
| conceptual-problems | 44 | 12 | 45 | 10 | 17 |
| emergent-gravity | 28 | 11 | 29 | 8 | 13 |
| entanglement-spacetime | 38 | 15 | 41 | 8 | 16 |
| experimental-tests | 31 | 13 | 39 | 8 | 18 |
| group-field-theory | 26 | 12 | 30 | 8 | 12 |
| holography-adscft | 40 | 13 | 35 | 8 | 18 |
| loop-quantum-gravity | 38 | 12 | 35 | 7 | 14 |
| noncommutative-geometry | 34 | 15 | 32 | 7 | 15 |
| quantum-cosmology | 30 | 12 | 35 | 9 | 14 |
| semiclassical-gravity | 36 | 14 | 40 | 8 | 14 |
| string-theory | 47 | 17 | 32 | 8 | 17 |
| supergravity-uv | 26 | 14 | 30 | 8 | 16 |
| swampland | 18 | 12 | 36 | 8 | 16 |
| twistors-amplitudes | 32 | 12 | 34 | 8 | 14 |

### Registry (celkem)

| Registr | Počet |
|---|---|
| references.json | 563 unikátních (z 633 syrových) |
| references.bib | export téhož |
| formulas.json | 235 unikátních (z 236 syrových) |
| open-problems.json | 145 (+9 fuzzy near-dup kandidátů) |
| concept-graph.json | 598 uzlů, 2319 hran |
| connections.json | 280 hran, 112 barely explored |
| _review/concept-merge-candidates.json | 80 párů k posouzení |

**Top hubs grafu (po pilíři 19):** modular-hamiltonian (nový TOP HUB po konsolidaci pilíře 19), holographic-principle, bekenstein-hawking-entropy, spectral-dimension, page-curve, generalized-entropy, adscft-correspondence, hawking-radiation, ryu-takayanagi. Graf: 614 uzlů, 2437 hran (stav po konsolidaci kolo 3).

**Sloučení konceptů (soudcovský průchod):** sloučeno 7 skupin (9 ID přesměrováno na kanonická): ryu-takayanagi→ryu-takayanagi-formula, holographic-error-correction+quantum-error-correction→holographic-quantum-error-correction, tensor-network-holography+tensor-networks→tensor-network, bousso-bound→covariant-entropy-bound, gravitational-decoherence→gravitationally-induced-decoherence, ads-cft-correspondence→adscft-correspondence, swampland-distance-conjecture→distance-conjecture; v open-problems sloučeny 2 duplicitní páry.

### Re-verifikace 5 pilířů (2026-06-05, economy run)

| Pilíř | Zkontrolováno ref. | Nalezeno chyb | Opraveno | Zbývající obavy |
|---|---|---|---|---|
| causal-sets | 10 | 3 | 3 | 2 |
| group-field-theory | 10 | 3 | 3 | 3 |
| twistors-amplitudes | 8 | 3 | 3 | 3 |
| emergent-gravity | 8 | 3 | 3 | 2 |
| experimental-tests | 8 | 4 | 4 | 4 |

Podrobnosti zbývajících obav viz log níže.

## Další kroky

Odvozeno z BRAINSTORM-04 (kolo 7) + výsledků kola 8. Kolo 8 uzavřelo dva hlavní risksecké body: H4g-3 vyvrácena (draft-02 finalizovatelný po lidské re-derivaci), H4g-1 podpořena v 2D (through-line mechanismus aktivní, 4D probe otevřena).

### Důsledky kola 8 pro drafty a through-line

**Draft-02 finality (calc17):** H4g-3 je vyvrácena — žádná druhá index-identita pro Λ neexistuje. Tím je uzavřeno poslední otevřené riziko draftu-02: identita −18/11 nepotřebuje Λ-sekci, protože a₀ a a₂ jsou cross-order a jejich poměr je dimenzionální. Draft-02 je vědecky kompletní a čeká pouze na lidskou re-derivaci a₄ koeficientů a citace-check (žádný nový výpočet není potřeba).

**Through-line — vrstva B (calc18):** H4g-1 je v 2D mechanisticky podpořena. Modulární kernel SJ stavu je geometricky lokální (boost/Bisognano-Wichmann) na slabu a stává se non-lokálním monotónně směrem k rohům diamantu (off-diag sklon −0.47 vs −0.094, f_nl gradient R²=0.989) — přesně tam kde VYPOCET-13 lokalizoval Hadamardovu anomálii. F-016 a F-021 se propojují mechanismem (ne jen korelací). Ve 4D sonda nereplikuje s link-maticí; doporučená cesta: BD d'Alembertián nebo větší N.

### Uzavřené / odstraněné položky

- ~~**C_KM(γ) konstantní člen** z ENP 1006.0634~~ — UZAVŘENO: Sen blocker potvrzený, H01 mrtvá, γ-fixace z CFT fyzikálně nemotivovaná.
- ~~**4D SSEE sprinkling p=3/4 predikce (naivní)**~~ — UZAVŘENO: VYPOCET-06 predikci vyvrátil; exponent p=3/4 jako magnitudový cutoff není robustní (ale N^{3/4} number-truncace jako crossed-product předpis PROŠLA — VYPOCET-16).
- ~~**Cardy-LQG (L1-3) jako živá hypotéza**~~ — UZAVŘENO: program dead.
- ~~**VYPOCET-14 ambiguita a=0.6**~~ — UZAVŘENO (VYPOCET-15): corr(S)=0.9992, ΔAIC=+3894, Model S rozhodující.
- ~~**BRAINSTORM-04 jako doporučený první krok**~~ — DOKONČENO (kolo 7).
- ~~**H4g-3 — fermionová indukce predikuje Λ (druhá index-identita)**~~ — UZAVŘENO (VYPOCET-17): vyvrácena; žádná druhá index-identity pro Λ; draft-02 Λ-riziko uzavřeno.
- ~~**H4g-1 2D sonda (slab vs. diamantový roh, modulární tok)**~~ — DOKONČENO (VYPOCET-18): podpořena 4/5, through-line mechanismus aktivní v 2D.

### Drafty čekající na lidskou revizi

- **draft-01-sj-rotating-spacetimes v0.2** (`papers/draft-01-sj-rotating-spacetimes/`) — všechny TODO body vyřešeny. **Blokující pro release:** (1) N→∞ studie s 30+ seeds; (2) analytické SJ pro strižený diamant; (3) BTZ dvou-bodová funkce; (4) verifikace citací PDF; (5) nezávislá re-derivace / re-run (gate §8 TODO.md).
- **draft-02-a4-fermionic-identity** (`papers/draft-02-a4-fermionic-identity/`) — vědecký obsah PLNĚ UZAVŘEN (VYPOCET-11 + VYPOCET-17: žádné Λ-riziko). **Blokující pro release:** lidská re-derivace a₄, citace-check Duff/Andrianov-Lizzi/Kurkov-Lizzi-Vassilevich, scheme-dependence ošetření.
- **draft-04-type-transition-causal-sets** (`papers/draft-04-type-transition-causal-sets/`) — vědecký obsah zapsán (kolo 8, VYPOCET-12 + VYPOCET-16). **Blokující pro release:** 8 lidských verifikačních bran (viz TODO.md); oprava placeholder a_err=0.776; BD d'Alembertián probe pro 4D repliku; LQG-area-gap noha trojúhelníku označena jako otevřená.

### DOPORUČENÁ FRONTA (BRAINSTORM-04, kolo 7)

**Dva paralelní výpočty (top priority):**

1. **H4g-3 — a₀/a₂ moment → Λ (fermionová indukce predikuje kosmologickou konstantu)** — nejlevnější (hodiny, exaktní sympy, navazuje na VYPOCET-02/11); otevírá draft-04 kandidáta a uzavírá draft-02 Λ-sekci. Hledá se druhá index-identita, racionální fermion-počítací forma pro Λ_cc/M_Pl².
2. **H4g-1 — modulární tok: slab vs. diamantový roh (rohová non-Hadamardovost = selhání boost-flow)** — nejvyšší konceptuální výnos; spojuje F-015/F-016/F-011 do jednoho mechanismu; testuje through-line (vrstva B); falzifikace: slab-modulární-tok geometrický boost musí selhat přesně v rozích.

**Tier 1 — BRAINSTORM-04 hypotézy:**

- **H4g-1** (rohová non-Hadamardovost = místo selhání boost-flow) — medium-high confidence; nejvyšší konceptuální výnos.
- **H4g-4** (III→II přechod přežívá na 4D slabu, ne na diamantu) — **POTVRZENA VYPOCET-16 (3/3 proxy)** — nyní: 4D diamant kontrolní výpočet + more seeds.
- **H4g-3** (Λ z fermionové indukce přes f₀/a₀ moment) — medium confidence; nejlevnější; dny; otevírá draft-04.

**Tier 2 — entropy-cluster program v 4D:**

- **VYPOCET-17 — 4D diamant vN-type kontrola** (navazuje na VYPOCET-16): ověřit predikci H4g-4: modulární spektrum na 4D diamantu zůstane III₁ i po N^{3/4} truncaci (rohová koncentrace jako blokátor přechodu).
- **VYPOCET-18 — slab area law větší N** (navazuje na VYPOCET-13): S~L^2.00 pro N=3000–5000, 10+ seeds; upřesnit Hadamardovy sklony.
- **4D Teukolský výpočet SJ** (H2g-6) — B exponent predikce; týdny.

**Tier 3 — přeneseno z BRAINSTORM-02/03:**

- **Oppenheim π-fázový posun** (H2g-8) — dny.
- **Ω_Λ sky-patch variance + stochastický w(z)** (H2g-5) — DESI DR2 / SKAO; dny.
- **Swerves ↔ l_cs most** — faktor 140 záchrana/pohřeb (H2g-4); dny.
- **FRG global-charge koeficient** AS fixed point (L4-2); týdny.

### Novelty check (arXiv/web) — DOKONČENO (2026-06-06)

- [x] **d_s klastr** — partially-known; reframe; probe-dependence potvrzena (VYPOCET-01).
- [x] **a_4 klastr** — partially-known; pursue; trojstranná identifikace nepublikována; VYPOCET-02 hotov.
- [x] **Λ klastr** — partially-known; reframe; prefaktorový test proveden (VYPOCET-03, 140×).
- [x] **Entropie klastr** — partially-known; pursue; VYPOCET-04 hotov (2D, ρ^(−1/2)); VYPOCET-06 vyvrátil 4D p=3/4.
- [x] **Cardy-LQG** — UZAVŘENO jako mrtvá (rozhodující kolo 2026-06-06).
- [x] **Preprint checks (L4-2, L4-5/L4-6, L5-3, L2-1)** — citace ověřeny; SJ pro Kerr/SdS otevřené (VYPOCET-05 = 2D BTZ dokončen).

### Stálé položky

- Doplnit chybějící témata (kandidáti: twistorová gravitace, post-Newtoniánská QFT, analogová gravitace jako samostatný pilíř).
- Průběžná aktualizace referencí při každém novém arXiv průchodu.
- Zavřít 9 fuzzy near-dup kandidátů v `open-problems.json` + zbývající concept-merge páry (61 zamítnuto, 80 původních).
- ~~Opravit entropy-cluster.md ř. 66: ρ^(−1/4) → ρ^(−1/2) (dle VYPOCET-04).~~ — Zaznamenáno; provést při příštím editačním průchodu.
- Zvážit Bianchi arXiv:1204.5122 (γ=i, γ-závislost mizí) jako okrajovou reziduální stopu po H01 closure.
