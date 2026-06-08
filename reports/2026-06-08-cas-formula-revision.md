# Kolo 20 — CAS revize registru vzorců (2026-06-08)

## Shrnutí

Systémová triáž celého `core-data/formulas.json` (247 unikátních záznamů) z hlediska CAS ověřitelnosti, následovaná úplnou Wolfram Language validací 34 CAS-ověřitelných vzorců ve 4 dávkách (B1–B4). Výsledek: **33 ověřeno (verified), 1 neshoda (mismatch = BLOCKER), 0 nespuštěno (not-run)** z CAS-checkable množiny.

---

## 1. Triáž registru — přehled kategorií

| Kategorie | Počet | Popis |
|---|---|---|
| **CAS-checkable** (mimo already-validated) | **34** | Exaktní symbolické identity, které WL umí znovu odvodit z literárních koeficientů |
| **Definitional** | **158** | Definice a konvence bez ověřitelného tvrzení (S=A/4G, RT/HRT, komutátory, WdW, …) |
| **Numerical** | **36** | Empirické fity a měřené hodnoty (spectral-dimension-fit, γ₀≈0,274, ρ_c≈0,41ρ_Pl, …) |
| **Already validated** | **19** | Pokrýváno třemi stávajícími WL skripty (a4_identity, lambda_ledger, ds_classifier) |
| **Celkem** | **247** | |

Přístup byl záměrně konzervativní — naprostá většina vzorců registru **není** nezávisle CAS-ověřitelná, protože jde buď o definice/konvence, nebo o empirické fity.

### Already-validated (19 vzorců)

Skript `a4_identity.wl` pokrývá: `trace-anomaly-4d`, `heat-kernel-action`, `gravity-terms`, `spectral-action-formula`, `real-structure-signs`. Skript `lambda_ledger.wl` překrývá spektrální-akci. Skript `ds_classifier.wl` pokrývá: `spectral-dimension-def`, `spectral-dimension-running`, `spectral-dimension-flow`, `horava-action`, `stelle-action`, `return-probability-uv-ir`, `two-plus-epsilon-fp`, a oba kauzálně-množinové d'Alembertovské vzorce (`discrete-dalembertian-4d`, `benincasa-dowker-action-4d`) — pokud jde o výsledný d_s=2 (kombinatorické koeficienty vrstev ověřeny navíc v B2).

---

## 2. Výsledky validace — dávky B1–B4

### Dávka B1 — Heat-kernel / perturbativní gravitace, power counting

Skript: `verification/cas/heat-kernel-perturbative-gravity-counterterms.wl`

| ID vzorce | Verdikt | Poznámka |
|---|---|---|
| `onshell-oneloop-counterterm` | ✅ **verified** | 1/120 a 7/20 exaktní Rational; on-shell → 0 (čistá gravitace 1-smyčkově konečná) |
| `goroff-sagnotti-counterterm` | ✅ **verified** | 209/2880 exaktní, GCD=1, C³ přežívá Ricci-flat shell → neperturbativní nerenormalizovatelnost |
| `gravity-power-counting` | ✅ **verified** | D=(d−2)L+2, při d=4 dává 2L+2=2(1+L); L=1,2,3 → 4,6,8 |
| `quantum-potential` | ✅ **verified** | 41/(10π), přesně 1 mocnina ħ, přesně π⁻¹ |
| `n8-critical-dimension-formula` | ✅ **verified** | D_c(L)=4+6/L; 5-smyčkové D_c=24/5 < 26/5 |
| `two-plus-epsilon-fp` | ✅ **verified** | g*=3/38 ε exaktní Rational (Weinberg 1979) |
| `n8-spin-content` | ✅ **verified** | Binomial[8,4−2s] → {1,8,28,56,70}; součet 2⁸=256 |
| `stelle-propagator` | ✅ **verified** | Apart partial fraction = (1/M²)(1/q − 1/(q+M²)); negativní reziduum u masivního spinoru 2 = ghost |

### Dávka B2 — Kauzálně-množinová kombinatorika a estimátory dimenze

Skript: `verification/cas/causal-set-combinatorial-operators.wl`

| ID vzorce | Verdikt | Poznámka |
|---|---|---|
| `benincasa-dowker-action-4d` | ✅ **verified** | Váhy vrstev {1,−1,9,−16,8} z koeficientů Benincasa-Dowker 2010 (arXiv:1001.2725); prefaktor 4/√6 exaktní |
| `discrete-dalembertian-4d` | ✅ **verified** | Váhy vrstev (1,−9,16,−8) ověřeny; cross-lock s BD akcí potvrzen |
| `myrheim-meyer` | ❌ **mismatch** | **BLOCKER — viz § 3 níže** |
| `kr-count` | ✅ **verified** | Vedoucí exponent log₂(#posetů)=n²/4; rozdělení vrstev (n/4,n/2,n/4) sčítá na n (Loomis-Carlip arXiv:1709.00064) |
| `poisson-sprinkling` | ✅ **verified** | Normalizace ∑P=1, střední ∑n·P=μ=ρV, rozptyl=μ (Poissonův) |
| `number-volume` | ✅ **verified** | ⟨n⟩=ρV jako střední hodnota Poissonova sprinklingu; N=V/l_p⁴ |

### Dávka B3 — CFT centrální náboje a mikroskopická entropie ČD (exaktní)

Skript: `verification/cas/cft-central-charges-bh-entropy.wl`

| ID vzorce | Verdikt | Poznámka |
|---|---|---|
| `strominger-vafa-entropy` | ✅ **verified** | c=6Q₁Q₅ + Cardy → 2π√(Q₁Q₅n) exaktní; limita n→∞ → 1 |
| `cardy-formula` | ✅ **verified** | Dvousektorový Cardy; podmínka reality L₀≥c/24 ověřena přes Resolve[ForAll[…]] |
| `cardy-btz` | ✅ **verified** | BTZ Cardy = Strominger-Vafa (FullSimplify≡0); most SV↔BTZ↔Cardy ověřen |
| `brown-henneaux` | ✅ **verified** | c=3L/(2G₃); N=4 SYM a=c=(N²−1)/4; large-N vedoucí člen N²/4 |
| `mass-dimension` | ✅ **verified** | Δ(Δ−d)=m²L² → Δ₊=d/2+√(d²/4+m²L²); BF mez m²L²≥−d²/4 |
| `critical-dimension-anomaly` | ✅ **verified** | Bosonic D=26 (ghost −26); super D=10 (ghost −15=−26+11) exaktně |

### Dávka B4 — Swampland / inflace: exaktní škálovací relace a algebraické identity

Skript: `verification/cas/b4-swampland-inflation-scaling.wl`

| ID vzorce | Verdikt | Poznámka |
|---|---|---|
| `slow-roll-spectral-index` | ✅ **verified** | n_s−1=−6ε+2η a r=16ε exaktní; konzistenční r=−8n_t→0 (Planck 2018) |
| `wgc-kk-rate` | ✅ **verified** | γ(d=4,n=1)=√(3/2) exaktní; obecný vzorec ověřen (Etheredge et al. arXiv:2206.04063) |
| `universal-pattern-formula` | ✅ **verified** | Součin gradientů=1/(d−2); d=4→1/2, d=5→1/3 (Castellano-Ruiz-Valenzuela arXiv:2311.01536) |
| `species-scale` | ✅ **verified** | Λ_sp=M_Pl/√N; inverzní relace N=M_Pl²/Λ_sp² |
| `species-scale-formula` | ✅ **verified** | S_BH(Λ_sp⁻¹)~N ověřena ve 4D |
| `w-infinity-algebra` | ✅ **verified** | Strukturní konstanty w(1+∞) antisymetrické + Jacobiho identita na 8 trojicích i symbolicky |
| `bcj-jacobi` | ✅ **verified** | Color-Jacobi c_i+c_j+c_k=0 ↔ kinematic n_i+n_j+n_k=0 exaktní mapa |

---

## 3. ⚠️ BLOCKER — Neshoda: `myrheim-meyer`

> **Toto je chyba v registru — publikovaný vzorec NEODPOVÍDÁ aktuálnímu zápisu v `core-data/formulas.json`.**

**Aktuální latex v registru:**
$$f_0(d) = \frac{\Gamma(d+1)\,\Gamma(d/2)}{4\,\Gamma(3d/2)}$$

**Správný publikovaný vzorec (Meyer 1988, ověřen třemi nezávislými kotevními body):**
$$f_0(d) = \frac{\Gamma(d+1)\,\Gamma(d/2)}{2\,\Gamma(3d/2)}$$

**Dopad chyby:**

| d | Správná hodnota (/2) | Chybná hodnota (/4) |
|---|---|---|
| 2 | f₀(2) = 1/2 (Minkowského interval) | f₀(2) = 1/4 ❌ |
| 4 | f₀(4) = 1/10 | f₀(4) = 1/20 ❌ |
| d_MM (inverze, KR) | d ≈ 2,38 ✅ | d ≈ 1,44 ❌ (nesedí nic) |

**Oprava:** Ve fragmentu `core-data/fragments/causal-sets.json` v záznamu `myrheim-meyer` změnit jmenovatel `4` na `2` v poli `latex`, poté spustit `workflows/consolidate.py` pro přegenerování `formulas.json`.

Numerický důsledek d_MM≈2,38 je správně uveden v poli `meaning` jako numerická hodnota — ale vznikne jen při správném jmenovateli 2.

---

## 4. Co zbývá: definitional + numerical pokrytí

### Definitional (158 vzorců)

Definice a konvence nejsou CAS-ověřitelné ve smyslu re-derivace, ale mohou projít **rozměrovou/interní-konzistenční kontrolou**. Příklady:
- Bekenstein-Hawking S=A/(4G) a její varianty (RT, HRT, QES, island): dimenzionální analýza
- iΔ=i(G_R−G_A), modulární tok Δ^{it}: interní konzistence algebraických relací
- Wheeler-DeWitt, akce Polyakov/DBI/SUGRA, LQG Poissonovy závorky: symbolická konzistence

Tato dráha zatím nebyla spuštěna — je to přirozený další krok pro kolo 21+.

### Numerical (36 vzorců)

Empirické fity (spectral-dimension-fit 4,02−119/(54+σ), Γ=23±1, γ₀≈0,274, ρ_c≈0,41ρ_Pl, …) jsou ověřitelné pouze re-runem výpočtu, nikoli CAS. Jsou zahrnuty do sady `app/tests/test_reproduction.py`.

---

## 5. Aktualizovaná CAS infrastruktura

- **7 WL skriptů** aktivních v dráze: `a4_identity.wl`, `ds_classifier.wl`, `lambda_ledger.wl`, `heat-kernel-perturbative-gravity-counterterms.wl`, `causal-set-combinatorial-operators.wl`, `cft-central-charges-bh-entropy.wl`, `b4-swampland-inflation-scaling.wl`
- **`run_all.py` rozšířen** (kolo 20) o B1, B2, B4 skripty; graceful exit 2 při chybějícím `wolframscript`; `__file__`-relativní cesty
- **`formula-coverage.json`** nový registr pokrytí (oddělen od generovaného `formulas.json`)

Celkový přehled dráhy: `python3 verification/cas/run_all.py` (nebo pytest se skip-guardem).

---

## 6. Závěr

Z 247 vzorců v registru je 34 CAS-checkable (mimo 19 already-validated). Z těchto 34 bylo v kolech 20 ověřeno **33 jako verified** a **1 jako mismatch (BLOCKER)**. Mismatch je reálná chyba v registru — faktor-2 v jmenovateli Myrheim-Meyerovy odhadové funkce.

**Nejdůležitější akce po tomto reportu:** opravit `myrheim-meyer` v `core-data/fragments/causal-sets.json` (jmenovatel 4 → 2) a přegenerovat `formulas.json` přes `workflows/consolidate.py`.
