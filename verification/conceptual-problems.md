# Ověřovací zpráva — Konceptuální problémy kvantové gravitace

**Pilíř:** Conceptual Problems of Quantum Gravity
**Ověřované soubory:**
- `knowledge-base/foundations/16-conceptual-problems.md` (česká próza)
- `core-data/fragments/conceptual-problems.json` (anglický JSON fragment)
**Datum ověření:** 2026-06-05
**Režim:** adverzariální verifikace (předpoklad existence chyb)

---

## Co bylo zkontrolováno

### 1. Validita JSON
JSON je syntakticky validní (`json.load` projde) před i po všech úpravách.

### 2. Audit referencí (ověřeno 20+ z 45)
Pro každou klíčovou referenci byla načtena stránka arXiv abstraktu (případně DOI/ADS/PMC) a ověřeny **ID, název, autoři a rok**. Ověřené reference (vše souhlasí, pokud není uvedeno jinak):

| ID | arXiv/DOI | Výsledek |
|---|---|---|
| hoehn-smith-lock-2021 | 1912.00033 | OK (Hoehn, Smith, Lock; 2019/PRD 2021) |
| clpw-2022 | 2206.10780 | OK (Chandrasekaran, Longo, Penington, Witten) |
| diffusion-bounds-2024 | 2403.08912 | OK (Janse et al.) |
| stochastic-modes-2026 | 2605.05375 | OK (Oppenheim, Sajjad; reálně 6. 5. 2026) |
| jusufi-collapse-2025 | 2512.15393 | OK (Jusufi, Singleton, Lobo; PLB 877) |
| aziz-howl-2025 | 2510.19714 | **CHYBA v iniciále autora** (viz níže) — jinak Nature 646, 813 (2025) potvrzeno |
| marletto-cannot-2025 | 2511.07348 | **CHYBA v iniciále 4. autora** (viz níže) |
| calcinari-gielen-2024 | 2407.03432 | OK (Quantum 9, 1610, 2025) |
| singularity-constraints-2025 | 2510.25927 | OK (Shahbazi-Moghaddam) |
| weinberg-nogo-qg-2017 | 1706.05804 | OK (Ichiro Oda) |
| donadi-2021 | 2111.13490 | OK (Donadi et al.; Nat. Phys. 17, 74) |
| oppenheim-pqcg-2018 | 1811.03116 | OK (Oppenheim; PRX 13, 041040) |
| kaimakkamis-2024 | 2412.18532 | OK (Kaimakkamis, Partouche, Sil, Toumbas) |
| nonlocal-cc-2025 | 2502.07321 | OK (Capozziello, Mazumdar, Meluccio) |
| bose-2017 | 1707.06050 | OK (Bose, Mazumdar, Morley et al.) |
| belenchia-2018 | 1807.07015 | OK (Belenchia, Wald, Giacomini, Castro-Ruiz, Brukner, Aspelmeyer) |
| observer-entropy-2024 | 2309.15897 | OK (Kudler-Flam, Leutheusser, Satishchandran) |
| qrf-crossed-2024 | 2412.15502 | OK (De Vuyst, Eccles, Hoehn, Kirklin) |
| giacomini-2019 | 1712.07207 | OK (Giacomini, Castro-Ruiz, Brukner; Nat. Commun. 10, 494) |
| large-spin-sg-2023 | 2312.05170 | OK (Braccini, Schut, Serafini, Mazumdar, Bose) |
| tabletop-interpretation-2022 | 2204.08064 | OK (Emily Adlam) |
| (próza) asymptotic-safety | 2507.14296 | OK (Renata Ferrero, „Asymptotic Safety and Canonical Quantum Gravity") |
| (próza) nanodiamanty | 2508.14272 | OK (Skakunenko et al., Paul trap / matter-wave interferometrie) |
| page-wootters-1983 | DOI 10.1103/PhysRevD.27.2885 | DOI za paywallem (403), ale kanonická citace „Evolution without evolution", Phys. Rev. D 27, 2885 (1983) je zavedená a potvrzená vyhledáváním |

Žádné **vymyšlené (neexistující) arXiv ID** nebylo nalezeno. Všechna testovaná ID se rozliší na reálné práce s odpovídajícím názvem a (po opravě iniciál) autory.

### 3. Audit vzorců (ověřeno 5+)
- **Wheelerova–DeWittova rovnice** — koeficienty `-16πGℏ²` a `√h/(16πG)((3)R−2Λ)` odpovídají standardní formě (Wikipedia / DeWitt). **OK.**
- **Schrödinger–Newtonova rovnice** — koeficient `Gm²` u nelineárního self-gravitačního členu odpovídá literatuře. **OK.**
- **Penroseův čas objektivní redukce** `τ≈ℏ/E_G` a struktura `E_G` (gravitační self-energie *rozdílu* rozložení) — **OK**; číselné odhady (elektron ≫ stáří vesmíru, zrnko ~Planckovy hmotnosti ~1 s) souhlasí.
- **Semiklasická Einsteinova rovnice** `G_μν+Λg_μν = 8πG⟨T_μν⟩` — **OK.**
- **Decoherence–diffusion trade-off** — **CHYBA** (viz níže), opraveno.

### 4. Audit konzistence
- Všechny `relatedTo` cíle ukazují na existující koncept-id v rámci fragmentu **kromě** `page-curve` a `firewall-paradox` (v konceptu `locality-vs-unitarity`). `page-curve` je platný globální pilíř (figuruje v `connections`); `firewall-paradox` je věrohodné globální id. **Ponecháno** (přípustné křížové odkazy).
- Všechny `formula.source` ukazují na existující `reference.id`.
- Hodnocení `explored`: žádná slavná, dobře prozkoumaná vazba není podhodnocena. „well" u black-holes / page-curve / semiclassical / LQG / quantum-cosmology je poctivé; „barely" u asymptotic-safety, causal-sets, twistors, noncommutative-geometry, swampland a nového Jusufi-mostu na strunovou teorii odpovídá skutečně tenkým/čerstvým propojením.
- Próza ⇔ JSON: po opravách nejsou rozpory.

---

## Co bylo špatně a co bylo opraveno

### CHYBA 1 — Špatná iniciála autora (Aziz)
- **Bylo:** „A. Aziz" (JSON ref `aziz-howl-2025`; próza ref č. 37).
- **Správně:** **J. Aziz** (Joseph Aziz). Ověřeno přes arXiv 2510.19714, Semantic Scholar i ADS.
- **Opraveno** v JSON i v próze. Při té příležitosti doplněna stránka „Nature 646, **813**".

### CHYBA 2 — Špatná iniciála autora (Wilson)
- **Bylo:** „M. Wilson" (JSON ref `marletto-cannot-2025`; próza ref č. 38).
- **Správně:** **E. Wilson** (Elizabeth Wilson). Ověřeno přes arXiv 2511.07348 (pole „From: Elizabeth Wilson").
- **Opraveno** v JSON i v próze. (Výskyty pouze s příjmením „Marletto–Oppenheim–Vedral–Wilson" jsou v pořádku.)

### CHYBA 3 — Nesprávný tvar nerovnosti decoherence–diffusion trade-off
- **Bylo:** `2 D_2 D_0 ⪰ 𝟙` (a údajný skalární ekvivalent `D_2^{ij} D_{0,ij} ≥ 1/4`).
- **Problém:** pravá strana byla nahrazena jednotkovou maticí / číselnou konstantou a **úplně vypadl člen vazby (back-reaction) D_1**. Tím vzorec ztrácel fyzikální obsah (mez na difuzi je dána *silou vazby*, ne univerzální konstantou).
- **Správně (Oppenheim et al. 2023, rov. 23):** `2 D_2 ⪰ D_1^{br} D_0^{-1} (D_1^{br})^†` — difuze metriky je zdola omezena koeficientem zpětné reakce `D_1` děleným dekoherencí `D_0`. Ověřeno přes primární zdroj (Nat. Commun. verze, PMC10696068, rov. 23 a obs. verze rov. 26).
- **Opraveno** ve všech čtyřech místech: JSON `formulas` (latex+meaning), JSON koncept `decoherence-diffusion-tradeoff`, JSON ref `significance`, a v próze (vzorcový blok, milník „Post-kvantová klasická gravitace", reference č. 30). Domnělý ekvivalent `≥ 1/4` byl jako fabrikace odstraněn.

---

## Co zůstává nejisté

1. **Page–Wootters DOI (10.1103/PhysRevD.27.2885)** se nepodařilo přímo načíst (HTTP 403 / paywall APS). Metadata ale odpovídají zavedené kanonické citaci; považováno za věrohodné, nikoli ověřené z primárního zdroje.

2. **DeWittova supermetrika v próze** je psána s `h^{-1/2}` u `G_abcd` (dolní indexy), zatímco standardní *kovariantní* supermetrika nese `h^{+1/2}` (forma s `h^{-1/2}` je kontravariantní/inverzní). Jde o smíšení konvence kovariantní vs. kontravariantní; nosná fyzika (lorentzovská signatura, jeden záporný „škálový" směr) je správná, proto ponecháno bez zásahu, ale stojí za pozdější sjednocení.

3. **Reference `page-curve` / `firewall-paradox`** v `relatedTo` nejsou definovány v tomto fragmentu; předpokládá se, že jde o platná globální id jiných pilířů. Nebylo ověřeno proti globálnímu rejstříku konceptů (mimo rozsah těchto dvou souborů).

4. **Rebuttalová krajina kolem Aziz–Howl** je v souborech popsána korektně, ale neúplně: existují i další kritiky (arXiv:2511.00852, 2511.20717) a navazující práce (arXiv:2604.19696). Není to chyba, jen neúplnost; ponecháno.

5. **DOI/žurnálové údaje** u některých prací (Phys. Lett. B u Capozziello, čísla stránek) nebyly ověřovány do úrovně čísla stránky — ověřovaly se primárně ID, název, autoři, rok.
