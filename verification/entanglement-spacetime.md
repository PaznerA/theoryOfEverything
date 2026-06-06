# Verifikační zpráva — Entanglement & Emergence of Spacetime (It from Qubit)

**Datum:** 2026-06-05
**Ověřované soubory:**
- `knowledge-base/cross-cutting/13-entanglement-spacetime.md` (česká próza)
- `core-data/fragments/entanglement-spacetime.json` (anglický JSON fragment)

## Co bylo zkontrolováno

### 0. Validita JSON
JSON je syntakticky platný (před i po opravách). Struktura: 38 konceptů, 15 vzorců,
41 referencí, 16 spojení. Všechny `source` u vzorců odkazují na existující reference.

### 1. Audit referencí (ověřeno 22+ referencí přes arXiv/DOI)
Ověřeny ID, název, autoři a rok proti arXiv abstraktům. Plně potvrzené reference
(ID rezolvuje + název + autoři + rok sedí):

- ryu-takayanagi-2006 (hep-th/0603001) — OK
- van-raamsdonk-2010 (1005.3035) — OK
- faulkner-et-al-2014 (1312.7856) — OK (submit 2013, publ. 2014; rok 2014 je akceptovatelný)
- maldacena-susskind-2013 (1306.0533) — OK
- engelhardt-wall-2014 (1408.3203) — OK
- swingle-2012 (0905.1317) — OK (submit 2009, publ. PRD 2012; rok 2012 = rok publikace)
- maldacena-2001 (hep-th/0106112, „Eternal Black Holes in AdS", JHEP 0304 (2003) 021) — OK
- lewkowycz-maldacena-2013 (1304.4926) — OK
- faulkner-lewkowycz-maldacena-2013 (1307.2892) — OK
- pastawski-et-al-2015 (1503.06237) — OK
- bousso-fisher-leichenauer-wall-2015 (1506.02669, „A Quantum Focussing Conjecture") — OK
- brown-roberts-susskind-swingle-zhao-2016 (1509.07876) — OK
- jafferis-lewkowycz-maldacena-suh-2016 (1512.06431) — OK
- dong-harlow-wall-2016 (1601.05416) — OK
- freedman-headrick-2016 (1604.00354; submit 2016, publ. 2017) — OK
- gao-jafferis-wall-2017 (1608.05687) — OK
- almheiri-engelhardt-marolf-maxfield-2019 (1905.08762) — OK
- penington-2019 (1905.08255) — OK
- penington-shenker-stanford-yang-2019 (1911.11977) — OK
- almheiri-mahajan-maldacena-zhao-2019 (1908.10996) — OK
- maldacena-qi-2018 (1804.00491) — OK
- srednicki-1993 (hep-th/9303048) — OK
- casini-huerta-myers-2011 (1102.0440) — OK
- calabrese-cardy-2004 (hep-th/0405152) — OK
- dong-2013 (1310.5713) — OK
- bousso-et-al-qnec-proof-2015 (1509.02542) — OK
- han-hung-2017 (1610.02134) — OK
- liu-2025 (2510.07017, submit 8.10.2025) — OK (odpovídá tvrzení „publikováno 10/2025")
- emergent-holographic-spacetime-2025 (2506.06595, Takayanagi, PRL 134, 240001) — OK
- desitter-connectivity-2024 (2403.14889, Franken) — OK
- symmetric-orbifold-mirage-2025 (2502.01734, Belin/Bintanja/Castro/Knop) — OK
- jafferis-et-al-2022 (Nature 612, 51, DOI 10.1038/s41586-022-05424-3) — OK (bez arXiv ID,
  což je u Nature publikace v pořádku)

### 2. Audit vzorců (ověřeno 6+ klíčových vzorců proti autoritativním zdrojům)
- Entanglement entropie 2D CFT: `S = (c/3) ln(ℓ/ε)` — koeficient c/3 pro jeden interval — OK
- Casini–Huerta–Myers modulární Hamiltonián koule: `2π ∫ (R²−r²)/(2R) T_00` — OK
- Schwarzianova derivace: `f'''/f' − (3/2)(f''/f')²` — OK (přesně)
- QNEC: `⟨T_kk⟩ ≥ (1/2π√h) S''` — koeficient 1/(2π) — OK
- Brown–Henneaux: `c = 3L/2G_N` — OK
- Mez chaosu (MSS): `λ_L ≤ 2π/β = 2π k_B T/ℏ` — OK (zdroj „A bound on chaos", 1503.01409, 2015)
- Bekenstein–Hawking pro Schwarzschild: `S = 4πG M²/(ℏc)` — koeficient OK
- Standardní vzorce (RT `A/4G`, S_gen, ostrovní formule, první zákon, JLMS, bit threads,
  komplexita, TFD) odpovídají literatuře.

### 3. Audit konzistence
- Cíle `connections.to` odpovídají existujícím slug fragmentů; `holographic-principle`
  nemá vlastní fragment, ale je akceptovaným globálním id (používá ho 3+ jiných fragmentů).
- `relatedTo` id `emergent-gravity-jacobson` a `holographic-principle` nejsou definovány
  uvnitř fragmentu, jde však o věrohodné globální koncept-id (cross-fragment odkazy).
- Próza neodporuje JSON.
- Hodnocení „explored" jsou poctivá: AdS/CFT, holografický princip, černé díry/informace,
  strunová teorie jsou hodnoceny „well" (správně), žádná slavná, dobře prozkoumaná dualita
  není podhodnocena na „barely".

## Co bylo špatně a opraveno

1. **chandrasekaran-penington-witten-2022 — ŠPATNÉ arXiv ID.**
   Uvedeno `2206.10780`, ale to je JINÝ článek (Chandrasekaran–**Longo**–Penington–Witten,
   „An Algebra of Observables for de Sitter Space"). Správné ID pro „Large N algebras and
   generalized entropy" (Chandrasekaran, Penington, Witten) je **2209.10454** (DOI
   10.1007/JHEP04(2023)009, který byl v JSON správně). **Opraveno v JSON i v próze**
   (řádky textu i seznam referencí #21).

2. **covariant-entropy-cone-2026 — VYMYŠLENÝ název a autoři.**
   JSON uváděl název „Covariant Holographic Entropy Cone" a autory „(Hubeny et al. / 2026)".
   arXiv ID `2602.04888` je reálné a tvrzení (ekvivalence kovariantního/statického entropy
   cone přes „no-short-cut" teorém) skutečně podporuje, ale skutečný článek je
   **„Graph models for covariant holographic entropy I" od Bowena Zhaa** (jediný autor).
   Navíc je teorém *podmíněný* (vyžaduje existenci „exposed regions"). **Opraveno** v JSON
   (název, autor, significance) i v próze (řádek 182 a reference #40); doplněna podmínka.

3. **entropy-cone-markov-2025 — neúplní autoři.**
   JSON uváděl autory jako „(2025)". Skuteční autoři: **G. Grimaldi, M. Headrick,
   V. E. Hubeny** (2508.21823). **Doplněno** v JSON i v próze (reference #41). Zmírněno
   přehnané tvrzení „nezávislý důkaz, že HRT a RT cone splývají" na „nezávislá
   charakterizace" (článek dává novou charakterizaci, ne ostrý důkaz splynutí).

## Co zůstává nejisté

- **jafferis-et-al-2022 (Nature)**: ověřeno přes DOI/název z paměti a kontextu; přímý fetch
  Nature stránky selhal kvůli přesměrování na autentizaci. DOI 10.1038/s41586-022-05424-3
  a údaje (Nature 612, 51–55, 2022) jsou ale konzistentní s veřejně známým článkem.
- **sep-quantum-gravity-2024** (SEP, plato.stanford.edu): nebyl samostatně fetchnut; jde
  o stabilní encyklopedický zdroj, riziko chyby nízké.
- **emergent-gravity-jacobson** a **holographic-principle** jako `relatedTo`/`to` id: nemají
  vlastní fragment-soubor; předpokládá se, že jde o platné globální koncept-id. Nelze ověřit
  bez globálního rejstříku id (v repu nenalezen).
- Mez chaosu (MSS, 1503.01409) je v próze citována jen inline („MSS 2015"), nemá vlastní
  záznam v `references`. Není to chyba (atribuce je správná), jen poznámka pro úplnost.
- Drobné nesrovnalosti rok-submit vs. rok-publikace u několika referencí (Swingle, Freedman–
  Headrick, Penington, faulkner-et-al) jsou konzistentní s konvencí „rok = rok publikace"
  a nebyly považovány za chyby.
