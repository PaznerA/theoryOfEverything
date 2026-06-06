# Novelty check: entropy-cluster (L2-3 + L3-4 + L4-4)

**Datum:** 2026-06-06  
**Cluster:** entropy-cluster  
**Hypotézy:** L2-3 (CST SSEE = crossed-product type-II), L3-4 (LQG horizon entropy = crossed-product type-II), L4-4 (CST SSEE volume-vs-area = mirage teorém)

---

## Hypotéza (shrnutí)

SSEE truncace Pauli-Jordanova operátoru v causal sets, LQG area gap a crossed-product konstrukce dávající type-II von Neumannovy algebry jsou **tři aspekty téže regularizace** divergentní entanglement trace. Diskrétní škála (area gap Δ = 4√3 π γ l_P²) je totožná s modulárním/observer cutoffem crossed-productu; Barbero-Immirzi γ je renormalizační konstanta vázající LQG stopu na type-II stopu.

---

## Co bylo nalezeno (prior art)

### Dvoucestné spoje (existují)

1. **Chandrasekaran–Longo–Penington–Witten, arXiv:2206.10780 (2022)**  
   Algebra pozorovatele v de Sitter prostoru je type II₁; observer clock zajišťuje přechod type-III → type-II. Žádná zmínka o causal sets ani LQG area gap.

2. **Chandrasekaran–Penington–Witten, arXiv:2209.10454 (2022)**  
   Konstrukce type-II∞ algebry v AdS/CFT; entropie = generalizovaná entropie. Žádné LQG, žádné causal sets.

3. **Sorkin–Yazdi, arXiv:1611.10281 (2016)**  
   SSEE v causal set theory; area law jen po UV truncaci Pauli-Jordanova spektra. Žádné crossed products, žádné type-II algebry.

4. **Surya–Nomaan X et al., arXiv:2008.07697 (2020)**  
   SSEE pro causal set de Sitter horizons; area law pouze po truncaci spektra; "knee" v eigenvalue spektru identifikuje truncační práh. Žádné LQG, žádné crossed products.

5. **Perez, arXiv:1405.7287 (2014)**  
   Propojení statistické a entanglement entropie v LQG přes strukturu kvantové geometrie. Žádné crossed products ani type-II algebry.

6. **Subregion algebras in classical and quantum gravity, arXiv:2601.07915 (2026)**  
   Type-II∞ algebry pro subregiony v perturbativní kvantové gravitaci; area operátor jako Connes cocycle flow. Žádné LQG area gap, žádné causal sets.

7. **Barbero–Immirzi jako cutoff, arXiv:1507.00851 (2015)**  
   Immirzi jako kvantový cutoff v LQG holonomy prostoru. Žádné von Neumannovy algebry, žádné crossed products.

8. **Entanglement entropy in LQG through quantum error correction, arXiv:2510.26911 (2025)**  
   Entanglement entropy v LQG přes algebraický přístup (type-I algebry). Žádné crossed products, žádné causal sets.

### Výsledek hledání trojcestného spoje

Žádný nalezený paper explicitně neidentifikuje SSEE truncaci (causal sets) + LQG area gap + crossed-product type-II algebru jako **tutéž operaci**. Communita causal sets a communita von-Neumannových algeber v kontextu gravitace sdílejí klíčová slova ("modular", "Pauli-Jordan/KMS"), ale toto překrytí dosud nikde nevyústilo v explicitní ztotožnění truncace Pauli-Jordanova spektra s crossed-product cutoffem.

---

## Verdikt

**partially-known** — dvoucestné spoje jsou publikované (SSEE truncace je dobře zmapována; crossed-product → type-II je etablované od 2022; LQG area gap jako entanglement cutoff byl zmíněn); **specifická trojcestná syntéza + identifikace Immirziho γ jako renormalizační konstanty vázající LQG stopu na type-II stopu není v literatuře přítomna.**

---

## Co zbývá nového

- Explicitní identifikace truncačního ranku dávajícího S = A/4 v SSEE s modulárním cutoffem ε crossed-productu.
- Tvrzení, že area gap Δ = 4√3 π γ l_P² **je** observer/modulární cutoff přechodu type-III→type-II.
- Role Barbero-Immirziho γ jako renormalizační konstanty normalizující type-II stopu na Bekenstein-Hawking entropii.
- "Mirage teorém" interpretace: area-law okno v SSEE jako výběr geometrických stavů z generických kvantových stavů (L4-4).

---

## Doporučení

**pursue** — se střední prioritou. Trojcestná syntéza je genuinně nová. Riziko: tři subclaims se liší v tom, *co* hraje roli cutoffu (γ vs. Δ vs. ε), a normalizace Immirziho je v LQG nejednoznačná. Testovatelný první krok: numericky spočítat SSEE eigenvalues na sprinklovaném diamantu a ověřit, zda truncační rank koreluje s modulárním cutoffem ε ~ ρ^(-1/4) (kde ρ je sprinkling hustota).

> **✏️ Korekce (2026-06-06, VYPOCET-04):** Provedený výpočet na 2D sprinklovaném diamantu změřil škálování entropického cutoffu **rank ~ N^(0.519±0.007)**, tj. **ε ~ ρ^(−1/2)** — původní odhad ρ^(−1/4) je vyloučen na ~39σ. Obecná predikce pro dimenzi d: rank ~ N^((d−1)/d) (area law cutoffu); ve 3D tedy N^(2/3), ve 4D N^(3/4). Viz `core-data/calculations/ssee-diamond/` a `knowledge-base/vypocty/VYPOCET-04-ssee-diamant.md`.

---

## Citace (prohledané arXiv IDs)

- 1611.10281 (Sorkin–Yazdi SSEE)
- 2008.07697 (Surya et al., de Sitter SSEE)
- 2206.10780 (Chandrasekaran–Longo–Penington–Witten, dS algebra)
- 2209.10454 (Chandrasekaran–Penington–Witten, large N algebras)
- 2306.07323 (Crossed product algebras and generalized entropy)
- 1405.7287 (Perez, statistical and entanglement entropy LQG)
- 2601.07915 (Subregion algebras in QG)
- 1507.00851 (Immirzi as cutoff)
- 2510.26911 (LQG entanglement entropy via QEC)
- 2510.26922 (LQG entanglement entropy and area law)
