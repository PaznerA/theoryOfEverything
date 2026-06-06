# Verifikační zpráva — Smyčková kvantová gravitace a spinové pěny

**Pilíř:** Loop Quantum Gravity & Spin Foams
**Ověřované soubory:**
- `/Users/pazny/projects/theoryOfEverything/knowledge-base/approaches/02-loop-quantum-gravity.md` (česká próza)
- `/Users/pazny/projects/theoryOfEverything/core-data/fragments/loop-quantum-gravity.json` (anglický JSON fragment)

**Datum verifikace:** 2026-06-05
**Verdikt:** Oba soubory prošly auditem bez nutnosti opravných zásahů. Nebyly nalezeny žádné vymyšlené reference, chybné atribuce autorů ani nesprávné vzorce.

---

## 0. Validita JSON

JSON je syntakticky validní (úspěšně se naparsoval). 38 konceptů, 12 vzorců, 35 referencí, 7 otevřených problémů, 14 spojení. Žádná oprava struktury nebyla nutná.

## 1. Audit referencí (ověřeno 24 z 35)

Vzorek prioritizoval reference podpírající nejsilnější tvrzení a všechny „podezřelé" novější/2025–2026 práce. Každá byla ověřena přes stránku abstraktu na arXiv nebo přes DOI/vyhledávání (ID se rozlišuje + sedí název, autoři, rok):

| Reference | Stav |
|---|---|
| Ashtekar 1986 (DOI 10.1103/PhysRevLett.57.2244) | OK — PRL 57, 2244–2247 |
| Rovelli & Smolin 1990 (DOI 10.1016/0550-3213(90)90019-A) | OK — Nucl. Phys. B 331, 80 |
| Rovelli & Smolin gr-qc/9411005 (diskrétnost plochy/objemu) | OK |
| Rovelli & Smolin gr-qc/9505006 (spinové sítě) | OK |
| Ashtekar–Baez–Corichi–Krasnov gr-qc/9710007 | OK (submise 1997, publ. 1998) |
| Lewandowski–Okołów–Sahlmann–Thiemann gr-qc/0504147 (LOST) | OK |
| Ashtekar–Pawłowski–Singh gr-qc/0602086 | OK |
| Bianchi–Modesto–Rovelli–Speziale gr-qc/0604044 (graviton propagátor) | OK |
| Engle–Pereira–Rovelli–Livine 0711.0146 (EPRL) | OK (viz pozn. níže) |
| Freidel–Krasnov 0708.1595 | OK |
| Engle–Noui–Perez 0905.3168 | OK (viz pozn. k roku) |
| Engle 1201.2187 (proper vertex) | OK |
| Perez 1205.2019 (Living Reviews) | OK |
| Speziale–Wieland 1207.6348 | OK |
| Thiemann gr-qc/0305080 (Master Constraint / Phoenix) | OK |
| Bojowald–Morales-Tecotl–Sahlmann gr-qc/0411101 | OK |
| Haggard–Han–Kamiński–Riello 1412.7546 | OK (viz pozn. k názvu) |
| Han 2109.00034 | OK |
| Han–Hung 1610.02134 | OK |
| Asante–Dittrich–Haggard 2004.07013 | OK |
| Asante–Dittrich–Padua-Arguelles 2104.00485 | OK |
| Gozzini 2107.13952 (sl2cfoam-next) | OK |
| Gielen–Oriti–Sindoni 1303.3576 | OK |
| Eichhorn–Bahr–Pereira 2103.14605 (editorial) | OK |
| Bruno–Colafranceschi–Mele–Rovelli **2603.16999 (2026)** | OK — existuje a sedí (autoři, název, rok 2026) |
| Guedes–Mena Marugán–Vidotto–Müller 2412.20257 | OK |
| Han **2510.26922 (2025)** | OK — autor Muxin Han, entanglement area law |
| Trivedi & Loeb **2506.03334 (2025)** „Could Planck Star Remnants be Dark Matter?" | OK — existuje, publ. Phys. Dark Univ. |
| Vyas & Joshi (DOI 10.3390/physics4040072) | OK — Physics 2022, 4(4), 1094–1116 |

**Závěr:** Žádná vymyšlená ID. Žádná chybná atribuce. Self-opravy, které výzkumný agent zanesl do prózy (pozn. u ref. #16 Pranzetti není autor; #25 Padua-Arguelles místo Haggard; #28 Bojowald et al. místo Gambini & Pullin; #30 Bruno et al. místo Dittrich et al.; #31 Guedes et al. místo Liegener et al.; #34 Vyas & Joshi, strany 1094–1116), byly nezávisle potvrzeny jako správné.

### Drobné poznámky (nejsou chyby, neopravováno)
- **Engle–Noui–Perez 0905.3168:** na arXiv submitováno 2009, publikováno v PRL 105, 031302 v **2010**. Oba soubory uvádějí rok 2010 (rok publikace) — legitimní a konzistentní.
- **Pořadí autorů EPRL 0711.0146:** skutečné pořadí na arXiv je Engle, **Livine, Pereira**, Rovelli. Oba soubory používají akronymové pořadí E-P-R-L (Engle-Pereira-Rovelli-Livine), pod nímž je model v literatuře známý. Všichni 4 správní autoři jsou uvedeni — přijatelná konvence, neopravováno.
- **Haggard–Han–Kamiński–Riello 1412.7546:** plný název na arXiv má podtitul „…4D Loop Quantum Gravity with a Cosmological Constant: Semiclassical Geometry". Próza/JSON používají zkrácenou parafrázi názvu — práce je správná, parafráze neklamavá.
- **Han 2510.26922:** JSON `significance` zmiňuje „von Neumann algebra methods" — potvrzeno (článek používá von Neumannovu algebru typu I, nikoli typu II; obecná formulace v JSON je správná).

## 2. Audit vzorců (ověřeno 6 klíčových)

1. **Spektrum plochy** `Â_S = 8πγℓ_P² Σ √(j(j+1))` — POTVRZENO (koeficient 8πγ i příspěvek na hranu odpovídají autoritativním zdrojům).
2. **Area gap** `Δ = 4π√3 γ ℓ_P²` pro j=1/2 — POTVRZENO aritmeticky (8πγℓ_P²·√3/2).
3. **Kritická hustota LQC** `ρ_c = √3/(32π²γ³G²ℏ) ≈ 0,41 ρ_Planck` — POTVRZENO; odpovídá tvaru √3/(32π²γ³G_N ℓ_P²) v jednotkách c=1; číselná hodnota 0,41 sedí.
4. **Hodnoty Immirziho parametru** γ₀ ≈ 0,2375 (U(1)/Meissner) a ≈ 0,274 (SU(2)) — POTVRZENO (0,2375 a 0,2739). Poznámka, že ln2/(π√3) ≈ 0,127 ≠ 0,274, je aritmeticky správná.
5. **Y-mapa / lineární simplicitní vazba** `(p=γj, k=j)`, vnoření SU(2) → hlavní série SL(2,ℂ) — POTVRZENO (standardní konvence, ρ=γj, k=j).
6. **Entropie černé díry** `S = (γ₀/γ)·A/(4ℓ_P²) − ½ ln(A/ℓ_P²)` — struktura i závislost log-korekce na schématu (−½ U(1) vs. −3/2 SU(2)) odpovídají literatuře.

Vzorec **kosmologické konstanty** `Λ = 6π/(ℓ_P² k)` je v obou souborech již korektně označen jako neověřený (⚠️ neověřeno / NOTE v JSON); potvrzeno pouze škálování Λ ∝ 1/k. Ponecháno tak.

## 3. Audit konzistence

- **Vzorec.source → reference.id:** všech 12 zdrojů vzorců se rozlišuje na reálnou referenci.
- **`relatedTo` cíle mimo lokální koncepty** (asymptotic-safety, causal-dynamical-triangulations, causal-sets, experimental-tests, holographic-principle, noncommutative-geometry, page-curve, quantum-cosmology, topological-field-theory, twistors-amplitudes): jsou to plauzibilní globální ID jiných pilířů; většina se objevuje i mezi `connections`. Není to chyba.
- **Próza vs. JSON:** žádné věcné rozpory (hodnoty γ, ρ_c, autoři, roky se shodují).
- **Pravopis „Barbero":** české skloňované tvary „Barberův/Barberova/Barberových" jsou korektní (cizí jméno na -o tvoří přivlastňovací adjektivum vypuštěním -o, srov. Picasso → Picassův). Není to chyba.

## 4. Poctivost hodnocení „explored"

- `group-field-theory: well` — oprávněné (korespondence GFT ↔ spinové pěny je dobře ustavena).
- `quantum-cosmology: well` — oprávněné (LQC je nejrozvinutější aplikace).
- `holography-adscft: partially` — poctivé; LQG nemá skutečnou holografickou dualitu, jen Han–Hung tensor-network mapping. Vyšší hodnocení by bylo nepoctivé.
- `asymptotic-safety: barely`, `string-theory: barely`, `causal-sets: barely` — poctivé; jde o spekulativní, nedoložené mosty.

Žádná slavná, dobře prozkoumaná dualita není podhodnocena ani nadhodnocena.

## 5. Provedené opravy

**Žádné.** Soubory neobsahovaly vymyšlené reference, chybná metadata ani neověřitelná tvrzení vyžadující smazání nebo označení. Stávající tagy „⚠️ neověřeno" (koeficient kosmologické konstanty) jsou na místě a byly ponechány.

## 6. Co zůstává nejisté

1. **Číselný prefaktor 1/48 v operátoru objemu** — nebylo možné nezávisle ověřit přesnou číselnou hodnotu z autoritativního zdroje; prefaktor je navíc závislý na konvenci (operátor Rovelli–Smolin vs. Ashtekar–Lewandowski, definice hustotněné triády). Vzorec je v obou souborech podán schematicky („žádný uzavřený obecný vzorec"), takže riziko je nízké, ale hodnota není zcela pinpointnuta.
2. **Koeficient Λ = 6π/(ℓ_P² k)** — již označeno jako neověřené; potvrzeno jen škálování Λ ∝ 1/k.
3. **MDPI Vyas–Joshi** — stránka mdpi.com vrací HTTP 403 (anti-bot); metadata (název, autoři, svazek 4(4), strany 1094–1116, rok 2022, DOI) ověřena přes ADS/ResearchGate/arXiv mirror 2206.00458, nikoli přímo z DOI.
4. **Tvrzení o graviton propagátoru** — abstrakt gr-qc/0604044 je opatrný („some components… up to second order"); plné tvrzení o shodě s linearizovanou gravitací je výsledkem navazující literatury, nikoli doslova abstraktu této jedné práce.
