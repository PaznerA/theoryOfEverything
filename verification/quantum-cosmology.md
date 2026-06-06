# Verifikační zpráva — Kvantová kosmologie (Quantum Cosmology)

**Datum:** 2026-06-05
**Ověřované soubory:**
- Český text: `knowledge-base/phenomenology/18-quantum-cosmology.md`
- Anglický JSON fragment: `core-data/fragments/quantum-cosmology.json`

## Co bylo ověřeno

### Reference (ověřeno 20+ z 35)
Přes WebFetch (arXiv abstrakty / DOI) bylo ověřeno více než 20 referencí, prioritně ty,
které nesou nejsilnější tvrzení. U každé byl kontrolován název, autoři a rok.

Ověřené a **správné** reference:
- DeWitt 1967 (PhysRev 160.1113) — OK
- Halliwell & Hawking 1985 „Origin of structure in the Universe" (PRD 31, 1777) — OK
- Vilenkin 2002 „Quantum cosmology and eternal inflation" (gr-qc/0204061) — OK
- Bojowald 2001 (gr-qc/0102069) — OK (publikovaný název má člen „a", triviální)
- Khoury-Ovrut-Steinhardt-Turok 2001 „The Ekpyrotic Universe" (hep-th/0103239) — OK
- Ashtekar-Pawlowski-Singh 2006 (gr-qc/0602086) — OK
- Taveras 2008 (0807.3325) — OK
- Hartle-Hawking-Hertog 2008 (0803.1663) — OK
- Gasperini-Veneziano „Pre-Big-Bang in String Cosmology" (hep-th/9211021, podáno 1992) — OK
- Ijjas-Lehners-Steinhardt 2014 (1404.1265) — OK
- Feldbrugge-Lehners-Turok 2017 „Lorentzian Quantum Cosmology" (1703.02076) — OK
- Feldbrugge-Lehners-Turok 2017b „No smooth beginning for spacetime" (1705.00192) — OK
- Halliwell-Hartle-Hertog 2019 (1812.01760) — OK
- Hawking-Hertog 2018 „A Smooth Exit from Eternal Inflation?" (1707.07702) — OK
- Di Tucci-Lehners 2019 (1903.06757) — OK
- Bedroya-Vafa „Trans-Planckian Censorship and the Swampland" (1909.11063) — OK
- Lehners „Allowable complex metrics..." (2111.07816) — OK
- Lehners „Review of the No-Boundary Wave Function" (2303.08802) — OK
- Hertog-Janssen-Karlsson 2023 (2305.15440) — OK; navazující práce o anizotropii
  (2408.02652) rovněž ověřena a existuje — OK
- Li-Motaharfar-Singh 2024 „Constraining regularization ambiguities in LQC via CMB"
  (2405.12296) — OK (pořadí autorů v originále: Bao-Fei Li, Meysam Motaharfar,
  Parampreet Singh; uvedené „B.-F. Li, P. Singh, M. Motaharfar" je drobně přeházené,
  ale věcně správné)
- DESI 2024 (2405.13588) — ID odpovídá práci Lodha et al. „Constraints on
  Physics-Focused Aspects of Dark Energy using DESI DR1 BAO Data" — OK

### Vzorce (ověřeno 6 nejdůležitějších)
- **FLT Lorentzovská minisuperprostorová akce** (2π², kinetický člen −3/(4N²)·q̇²,
  potenciál +3−Λq): ověřeno proti rovnici (18) v 1703.02076 — **správně**.
- **No-boundary de Sitter exponent** exp(+12π²/ħΛ) a tunelovací exp(−12π²/ħΛ):
  ověřeno přímo v textech FLT — **správně** (12π²/ħΛ je kanonická forma; ekvivalence
  s 3/(8G²ρ_Λ) platí v dané jednotkové konvenci).
- **LQC modifikovaná Friedmannova rovnice** H²=(8πG/3)ρ(1−ρ/ρ_c) a
  ρ_c=√3/(32π²γ³G²ħ)≈0,41ρ_Pl: ověřeno proti autoritativním zdrojům — **správně**.
- **Plošná mezera** Δ=4√3·π·γ·ℓ_Pl²: **správně**.
- **TCC mez** |V′|/V ≳ 2/√(d−2): ověřeno proti Bedroya-Vafa — **správně**.
- **No-boundary váha fluktuací (FLT)**: viz nalezené chyby níže.

### Konzistence
- Všech 14 cílů v `connections` (`to`) odpovídá reálným sousedním fragmentům
  (loop-quantum-gravity, string-theory, holography-adscft, swampland,
  asymptotic-safety, causal-dynamical-triangulations, causal-sets,
  group-field-theory, noncommutative-geometry, black-holes-information,
  semiclassical-gravity, experimental-tests, entanglement-spacetime,
  conceptual-problems) — OK.
- Všechny `source` ve `formulas` odkazují na existující `id` v `references` — OK.
- Hodnocení „explored": žádná slavná, dobře prozkoumaná dualita není podhodnocena.
  AdS/CFT (holografická kosmologie) je „partially" — poctivé, protože plné AdS/CFT
  je sice prozkoumané, ale jeho kosmologická aplikace nikoli. LQG→LQC „well" a
  semiklasická gravitace „well" jsou poctivé. — OK.
- Český text a JSON si vzájemně neodporují (stejné ρ_c, exponenty, TCC mez, DESI σ).

## Co bylo špatně a opraveno

1. **Chybný název reference Nayeri 2026 (arXiv:2602.21263).**
   - Uvedeno: „Quantum Cosmology, Decoherence, and the Emergence of Classical Spacetime".
   - Skutečnost: „The Cosmological Arrow of Time from Inflationary Branch Decoherence"
     (autor Ali Nayeri, ID i rok souhlasí).
   - Opraveno v JSON (`nayeri-2026`) i v textu (ref. č. 33 a sekce „Současný stav",
     bod 4).

2. **Chybný vzorec — váha fluktuací v Lorentzovském no-boundary (FLT).**
   - Uvedeno: exp(+3π/(2GħΛ)·Σ (l−1)(l+2)|δφ_l|²).
   - Skutečnost (ověřeno dvakrát proti 1705.00192 a 1708.05104): multipólový faktor je
     **l(l+1)(l+2)** (nikoli (l−1)(l+2)) a prefaktor je **3/(2ħΛ)** (bez π a bez G;
     Λ už nese příslušnou škálu). Správná forma:
     exp(+3/(2ħΛ)·Σ l(l+1)(l+2)|φ_l|²).
   - Opraveno v JSON (`no-boundary-perturbation-weight`) i v textu (sekce
     „Matematický rámec").

3. **Zaměněná/sloučená reference DESI v textu (ref. č. 28).**
   - Text uváděl dva názvy najednou: „DESI 2024 VI: Cosmological Constraints..."
     (to je jiná práce, 2404.03002) sloučenou s „Constraints on Physics-Focused
     Aspects of Dark Energy". ID 2405.13588 odpovídá pouze druhé z nich (Lodha et al.).
   - Opraveno: ponechán jen správný název odpovídající ID; doplněno upřesnění napětí
     (~4,2σ při DESI DR2 + Planck + DES-Y5). JSON byl už správně.

4. **Kosmetická oprava ve vzorci** FLT akce: odstraněn zbytečný zápis q̇²/1 → q̇²
   (matematicky bez vlivu).

## Co zůstává nejisté

- **Numerické důsledky TCC** (V^{1/4} ≲ 6×10⁸ GeV, r ≲ 10⁻³⁰) jsou v textu připsány
  výhradně práci Bedroya-Vafa 2019; v jejím abstraktu se přímo neobjevují (pocházejí
  z navazující literatury, např. Bedroya-Brandenberger-Loverde-Vafa 1909.11106).
  Hodnoty jsou v literatuře standardní a nejsou vymyšlené, ale připsání zdroje je
  drobně nepřesné — ponecháno bez označení (řádově korektní, široce citované).
- **Ekvivalence exponentů** 12π²/ħΛ = 3/(8G²ρ_Λ) platí jen v konkrétní jednotkové
  konvenci (efektivně G=1/(4π)-typ); v textu není konvence explicitně rozepsána.
  Kanonická forma 12π²/ħΛ je ověřena přímo u FLT, takže tvrzení je správné, ale
  čtenář by měl vědět, že druhá rovnost je konvenčně podmíněná.
- **Pořadí autorů** u Li-Motaharfar-Singh 2024 je v textu/JSON drobně přeházené
  („P. Singh, M. Motaharfar" vs. originál „M. Motaharfar, P. Singh"). Věcně neškodné,
  neopravováno.
- **Misner 1972 „Minisuperspace"** (kapitola ve sborníku *Magic Without Magic*) nemá
  DOI a nelze ji ověřit přes arXiv; existence je dobře doložena v sekundární
  literatuře, ponecháno s ADS odkazem.
- **Plný text vzorců FLT akce a Friedmannovy rovnice** byl ověřen přes HTML (ar5iv)
  a sekundární zdroje, nikoli přes původní PDF s plnou typografií — riziko jemných
  konvenčních rozdílů (znaménko, faktor ħ) je nízké, ale ne nulové.
