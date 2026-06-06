# Novelty Check: preprint-checks (L4-2, L4-5/L4-6, L5-3, L2-1)

Datum: 2026-06-06

## Celkový verdikt: partially-known

---

## (a) L4-2 — No-global-symmetries vs. Asymptotická bezpečnost

**Hypotéza:** No-global-symmetries je absolutní swampland kritérium; asymptotická bezpečnost (AS) ho porušuje, protože FRG fixed point může mít konzistentní global-charge operátor s nenulovým koeficientem.

**Co bylo nalezeno:**

- Basile, Knorr, Platania, Schiffer, *"Asymptotic safety, quantum gravity, and the swampland: a conceptual assessment"*, arXiv:2502.12290, SciPost Phys. 20, 027 (2026). Tato práce přímo adresuje konflikt. Autoři argumentují, že robustní odvození no-global-symmetries (přes topologické změny + BH termodynamiku + holografii) se v přísné polní teorii AS těžko implementuje — chybí topologická změna, takže logický řetězec se přeruší. Práce to formuluje jako otevřenou otázku s možnými skulinami (silná nelokálnost, efektivní AS, nekonečně mnoho polí), nikoli jako přímé tvrzení "AS porušuje swampland".
- Eichhorn et al., arXiv:2012.07868 (Constraints on discrete global symmetries in QG): kolektují evidence, že v AS kontextu diskrétní globální symetrie Z_n (n>4) nemohou být realizovány v near-perturbativním režimu — tzn. AS v tomto směru spíše *posiluje* no-global-symmetries, nikoli ho porušuje.
- Eichhorn, arXiv:1810.07615 (AS guide to QG and matter): gravitační fluktuace generují interakce pro matter fields; fixed-point values jsou nenulové a zachovávají globální symetrie minimálně vázaných teorií — ale existence fixed pointu respektujícího globální symetrii je nutná, nikoli postačující podmínka.
- arXiv:2407.09595 (non-local way around no-global-symmetries): jiný (ne-AS) přístup přes nelokální gravitační akce; destrkutivní interference BH konfigurací v path integrálu.

**Závěr pro L4-2:** Konflikt AS vs. no-global-symmetries je v literatuře identifikován a diskutován (2502.12290 ho explicitně mapuje). Přesné výpočtové tvrzení naší hypotézy — "FRG flow global-charge operátoru: koef. = 0 ve fixed pointu?" — zatím není v literatuře explicitně proveden jako numerický výsledek. **Status: partially-known.** Naše formulace přidává konkrétní výpočtový test (FRG koeficient) a ostrý verdikt (porušení vs. loophole); literaturní základ je však velmi blízko.

---

## (b) L4-5 / L4-6 — BMV/QGEM debate a 2025 rebuttal exchange

**Hypotéza (L4-5):** BMV/QGEM diskriminuje přístupy ke gravitaci (emergent vs. graviton-based), nejen Q vs. C.  
**Hypotéza (L4-6):** d_s→2 oslabuje gravitaci → napětí s WGC "gravity weakest" (δ(Q/M)).

**Ověření citovaných arXiv IDs:**

- **arXiv:2511.07348** existuje: Marletto, Oppenheim, Vedral, Wilson, *"Classical gravity cannot mediate entanglement"*. Hlavní argument: model Azize a Howlové v nerelativistickém limitu produkuje ultra-lokální interakci; totální unitár se faktorizuje; z produktového vstupu nevzniká entanglement. Verifikováno.
- **arXiv:2511.19242** existuje: Schneider, Huggett, Linnemann, *"Classical gravity cannot mediate entanglement on independent grounds"*. Newton-Cartanova analýza. Nezávislá podpora závěru 2511.07348. Verifikováno (není přímá odpověď na 2511.07348, ale paralelní podpora).
- **arXiv:2511.20717** existuje: Sienicki & Sienicki, *"Comment on Classical-Gravity–Quantum-Matter Claims About Gravity-Mediated Entanglement"*. Komentář k Aziz-Howl, reformulace přes channel teorii.
- **Aziz & Howl Nature 2025**: Nature, vol. 646 (2025) — verifikováno existuje, DOI: 10.1038/s41586-025-09595-7. Tvrdí, že klasické gravitační pole může přenášet kvantovou informaci a generovat entanglement přes lokální procesy v rámci QFT.

**Stav debaty:** Debata je aktivní a velmi živá (2025–2026). Framing naší hypotézy L4-5 ("BMV diskriminuje přístupy, ne jen Q vs C") je ale **odlišný** od aktuálního mainstreamu debaty, který se soustředí na Q vs. C (quantum vs. classical gravity). Tvrzení, že BMV experiment může rozlišit mezi různými kvantovými přístupy (AS graviton spektrální funkce vs. Verlinde mediátor), se v literaturně explicitně **neobjevuje** — to je plausibly novel.

**Pro L4-6 (d_s→WGC):** Hamada-Noumi-Shiu je citovaný základ pro WGC výpočty; přímé vložení 1/p^4 propagátoru a výpočet δ(Q/M) v AS kontextu nebylo v search nalezeno jako publikovaný výsledek.

---

## (c) L5-3 — SJ stav pro Kerr / Schwarzschild-de Sitter

**Hypotéza:** Sorkin-Johnston Pauli-Jordan stav poskytuje chybějící Hadamard stav pro Kerr nebo SdS spacetime.

**Co bylo nalezeno:**

- SJ stav byl konstruován pro: 2D kauzální diamant (arXiv:1906.07952, 2212.10592), de Sitter spacetime (arXiv:1306.3231, JHEP 2019), ultrastatic spacetimes.
- **Klíčový nález:** SJ stav obecně Hadamardův není. Na 1+1D kauzálním diamantu není Hadamardův na hranici (arXiv:2212.10592). Na de Sitterovém spacetime neodpovídá žádnému ze známých Mottola-Allen vakuí.
- **Pro Kerr ani SdS:** Žádná práce konstruující SJ stav explicitně na Kerrově nebo Schwarzschild-de Sitterově spacetime nebyla nalezena. Fewster-Verch a Kay-Wald no-go výsledky (citované v brainstormu) jsou relevantní pro stacionární non-statické spacetime, ale explicitní SJ↔Hadamard srovnání pro Kerr chybí.
- ArXiv:2412.07832 (2024) zmiňuje SJ stav v de Sitter kontextu s nejasnostmi ohledně Hadamardovy vlastnosti.

**Závěr pro L5-3:** Aplikace SJ stavu na rotující (Kerr) nebo multi-horizonový (SdS) spacetime je v literatuře **nezpracovaná**. Výsledky pro de Sitter a kauzální diamant existují, ale Kerr/SdS je nové území. **Status: plausibly-novel** pro Kerr/SdS specificky.

---

## (d) L2-1 — NCG = GFT = CDT (Liouville/Painlevé I universální třída)

**Hypotéza:** Dirac ensemble (NCG), GFT (group field theory) a CDT sdílejí totožnou Liouville/Painlevé I universální třídu v double scaling limitu — trojstranná ekvivalence.

**Co bylo nalezeno:**

- Hessam, Khalkhali, Pagliaroli, arXiv:2204.14206 (JPHYS A 2023): **NCG → Liouville** vazba je publikovaná. Double scaling limit Dirac ensembles dává kritické exponenty Liouville CFT + gravity, Painlevé I. Toto je přímý základ L2-1 (NCG strana).
- Khalkhali, Pagliaroli, arXiv:2312.10530 (JHEP 2024): 2-matrix ensemble, γ_str = 1/2 → universální třída kontinuálního náhodného stromu (CRT), **nikoli** Liouville. Jiná universální třída pro jiný model.
- Khalkhali, Pagliaroli, Verhoeven, arXiv:2405.05056 (2024): fuzzy geometries + fermiony, integer-valued β-ensembles; GFT ani CDT nejsou zmíněny.
- Khalkhali, Pagliaroli, arXiv:2512.08694 (2025): bootstrap přístup k NCG Dirac ensembles; GFT ani CDT nezmiňuje.
- **CDT ↔ Liouville/matrix models:** Jsou dobře dokumentovány (CDT jako scaling limit matrix modelů bez baby-universes), ale nezávisle od NCG/Dirac ensemble programu.
- **GFT ↔ Liouville:** Nepřímá vazba přes tensor modely; explicitní ekvivalence GFT = Dirac ensemble v Liouville třídě nebyla nalezena.

**Závěr pro L2-1:** NCG → Liouville (Khalkhali) je publikované. CDT → Liouville je publikované (odděleně). Ale **trojstranné tvrzení NCG = GFT = CDT v jedné universální třídě** nebylo v literatuře nalezeno. **Status: partially-known** (dvoustranné vazby publikovány, trojstranná syntéza je nová).

---

## Doporučení

1. **L4-2:** Aktualizovat popis tak, aby reflektoval, že Basile et al. 2502.12290 diskutují tento konflikt jako otevřenou otázku s loopholes — naše přidaná hodnota je konkrétní FRG výpočet (nulovost koeficientu). Citovat 2502.12290 explicitně.
2. **L4-5/L4-6:** Debata o BMV/Aziz-Howl je aktivní a arXiv IDs jsou verifikovány. Framing L4-5 (AS vs. Verlinde, nikoli Q vs. C) je skutečně nový — zachovat, ale upřesnit kontext. L4-6 zůstává nevyřešena v literatuře.
3. **L5-3:** Kerr/SdS SJ stav je nezpracované území — zachovat jako středně prioritní novum. Přidat odkaz na Fewster-Verch pro diskusi Hadamardových stavů.
4. **L2-1:** Označit NCG↔Liouville část jako published (citovat 2204.14206), zachovat trojstrannou NCG=GFT=CDT tezi jako novou hypotézu vyžadující explicitní propojení.
