# Verifikační zpráva — Černé díry a informační paradox

**Pilíř:** Black Hole Thermodynamics & the Information Paradox
**Soubory:**
- Česká próza: `knowledge-base/cross-cutting/12-black-holes-information.md`
- JSON fragment: `core-data/fragments/black-holes-information.json`
**Datum verifikace:** 2026-06-05
**Verifikoval:** adversariální ověřovací agent

---

## Shrnutí

Oba soubory jsou v dobrém stavu. JSON je **validní** (žádná oprava syntaxe nebyla potřeba). Ověřeno **22 referencí** (WebFetch arXiv/DOI) a **5+ klíčových vzorců** proti autoritativním zdrojům. **Nebyly nalezeny žádné vymyšlené arXiv ID, žádná chybná autorská atribuce ani vymyšlený rok.** Provedeny 2 drobné úpravy v próze (přidání citace, otagování neověřeného číselného odhadu). Žádné reference nebylo nutné smazat.

---

## STEP 1 — Validita JSON

JSON se načetl bez chyby (`json.load`). Struktura: 25 konceptů, 16 vzorců, 43 referencí, 10 otevřených problémů, 17 napojení. Žádná oprava nebyla nutná.

---

## STEP 2 — Audit referencí (ověřeno 22 z 43)

Všechny níže uvedené reference byly ověřeny přes WebFetch (arXiv abstrakt / DOI / vyhledávání). **Titul, autoři i rok souhlasí** u všech:

| Ref | ID | Výsledek |
|-----|-----|----------|
| Page 1993a | gr-qc/9305007 | OK — "Average Entropy of a Subsystem", D. N. Page, 1993 |
| Page 1993b | hep-th/9306083 | OK — "Information in Black Hole Radiation", D. N. Page, 1993 |
| Strominger–Vafa | hep-th/9601029 | OK — Strominger & Vafa, 1996 |
| Penington 2020 | 1905.08255 | OK — G. Penington (arXiv 2019, JHEP 2020) |
| AEMM | 1905.08762 | OK — Almheiri, Engelhardt, Marolf, Maxfield |
| AMMZ | 1908.10996 | OK — Almheiri, Mahajan, Maldacena, Zhao |
| PSSY | 1911.11977 | OK — Penington, Shenker, Stanford, Yang |
| AHMST (review) | 2006.06872 | OK — RevModPhys 93, 035002 (2021) souhlasí |
| AMPS firewall | 1207.3123 | OK — Almheiri, Marolf, Polchinski, Sully |
| Maldacena–Susskind | 1306.0533 | OK |
| Engelhardt–Wall | 1408.3203 | OK — QES, 2014/2015 |
| Maldacena 2003 | hep-th/0106112 | OK — věčné AdS ČD (arXiv titul "in AdS", JSON "in Anti-de-Sitter" — pouhé rozepsání zkratky, ne chyba) |
| MSS chaos bound | 1503.01409 | OK — "A bound on chaos" |
| Sen | 1108.3842 | OK — log. korekce (arXiv 2011, GRG 2013) |
| Geng–Karch | 2006.02438 | OK — "Massive Islands", 2020 |
| Geng–Karch et al. | 2107.03390 | OK — všech 7 autorů souhlasí |
| Raju | 2012.05770 | OK — "Lessons from the Information Paradox" |
| Chandrasekaran–Penington–Witten | 2209.10454 | OK — "Large N Algebras and Generalized Entropy" |
| Antonini et al. "Apologia" | 2506.04311 | **OK — reálná, JHEP 10 (2025) 034, DOI 10.1007/JHEP10(2025)034 ověřeno** |
| Hollands–Wald–Zhang | PRD 110, 024070 | OK — reálná, arXiv 2402.00818 (JSON arXiv ID neuvádí, metadata sedí) |
| Saad–Shenker–Stanford | 1903.11115 | OK |
| Marolf–Maxfield | 2002.08950 | OK |
| Wallace | 1710.03783 | OK (arXiv 2017, kniha *Beyond Spacetime* CUP 2020 — JSON rok 2020 odpovídá publikaci kapitoly) |
| Susskind "Trouble for Remnants" | hep-th/9501106 | OK |
| Bena–Martinec–Mathur–Warner | 2204.13113 | OK — všichni 4 autoři vč. Martince |

**Poznámka k rokům:** několik referencí (Penington, AEMM, AMMZ, PSSY, MSS, Sen) má arXiv submission rok o 1 nižší než rok v JSON — JSON důsledně používá rok **publikace v časopise**, což je legitimní a vnitřně konzistentní.

---

## STEP 3 — Audit vzorců (ověřeno 5+)

| Vzorec | Výsledek |
|--------|----------|
| Bekenstein–Hawking $S = A/4G\hbar$ | OK (standardní) |
| Hawkingova teplota $T_H = \hbar\kappa/2\pi k_B c = \hbar c^3/8\pi GMk_B$ | OK; $\kappa = c^4/4GM$ pro Schwarzschild OK |
| 1. zákon $dM = \frac{\kappa}{8\pi G}dA + \Omega dJ + \Phi dQ$ | OK (standardní) |
| Rychlost odpaření $dM/dt = -\hbar c^4/(15360\pi G^2 M^2)$ | **OK — koeficient 15360π ověřen** |
| Doba odpaření $t \sim 5120\pi G^2 M^3/\hbar c^4$ | **OK — koeficient 5120π ověřen** |
| Strominger–Vafa $S = 2\pi\sqrt{Q_1 Q_5 N}$ | OK — standardní tvar pro D1-D5-P |
| Bekensteinova mez $S \leq 2\pi k_B R E/\hbar c$ | **OK — koeficient 2π ověřen** |
| Chaos bound $\lambda_L \leq 2\pi k_B T/\hbar$ | **OK — ověřeno přímo v MSS 1503.01409** |
| Ostrovní formule / QES / S_gen | OK — odpovídají Engelhardt–Wall a island programu |
| Scrambling time $t_* \sim \frac{\beta}{2\pi}\ln S$ | OK (standardní) |

Žádný vzorec neměl chybný koeficient, znaménko ani konvenci. Próza i JSON uvádějí stejné tvary (vzájemně konzistentní).

**Drobnost (neopraveno, není chyba):** v JSON je `bekenstein-bound-formula` přiřazena zdroji `bousso-2002`. Bekensteinova mez pochází od Bekensteina (1981); v seznamu referencí ale chybí Bekenstein 1981. Atribuce na Boussův review je obhajitelná (review mez uvádí v kovariantní podobě) a `meaning` ji správně nazývá "Bekenstein bound". Próza atribuuje správně (Bekenstein vs. kovariantní Bousso).

---

## STEP 4 — Audit konzistence

- **Lokální concept ID:** 25 konceptů, žádné duplicitní/rozbité ID.
- **`relatedTo` na globální ID:** 31 odkazů mimo fragment (např. `holographic-principle`, `ryu-takayanagi`, `jt-gravity`, `hayden-preskill`, `pythons-lunch`) — všechny jsou věcně přijatelná globální ID konceptů, žádný nesmysl.
- **`connections`:** 15 ze 17 cílů odpovídá reálným sousedním pilířovým fragmentům. Zbývající dva (`holographic-complexity`, `quantum-error-correction`) jsou v próze explicitně označeny jako "(concept: …)" — záměrné odkazy na úrovni konceptu, ne rozbité pilíře. **Není to chyba.**
- **Honesta hodnocení "explored":**
  - `holography-adscft` = **well** — správně (ostrovy/Pageova křivka odvozeny uvnitř AdS/CFT).
  - `entanglement-spacetime` = **well**, `quantum-error-correction` = **well** — správně (ER=EPR/RT; ADH kód).
  - Hodnocení **barely** (LQG, asymptotic-safety, causal-sets, NC-geometry, swampland, experimental-tests) jsou poctivá — vazby na informační paradox jsou skutečně řídké.
  - **Žádná slavná/dobře prozkoumaná dualita není podhodnocena jako "barely".**
- **Próza vs. JSON:** žádný věcný rozpor. Časová osa, koncepty, vzorce i otevřené problémy se shodují.
- **SCGP sympozium "50 years of the black hole information paradox" (próza):** ověřeno jako reálné — organizátoři Afshordi, Martinec, Mathur, Stony Brook, listopad 2025. Próza správně.

---

## STEP 5 — Provedené opravy

1. **Próza, sekce "Současný stav" (stavová závislost):** nepodložený kvantitativní odhad "ostrov může vyčnívat $\sim \ell_P\sqrt{r_h}$ vně horizontu" otagován jako **⚠️ neověřeno** (bez dohledatelné citace); kvalitativní tvrzení (QES leží mírně vně horizontu) ponecháno, protože je etablované.
2. **Próza, sekce "Spekulativní okraj 2026":** doplněna **chybějící citace** pro tvrzení o G2-manifoldu / 7D Einstein–Cartan remnantu ~$9\times10^{-41}$ kg. Tvrzení bylo **ověřeno jako reálné** — Pinčák, Pigazzini, Pudlák & Bartoš, *Geometric origin of a stable black hole remnant from torsion in G2-manifold geometry*, Gen. Rel. Grav. (2026), DOI [10.1007/s10714-026-03528-z](https://doi.org/10.1007/s10714-026-03528-z). Hodnota hmotnosti remnantu i napojení na Higgsovo měřítko (~246 GeV) přesně souhlasí se zdrojem. Próza ji správně rámuje jako spekulativní/mimo hlavní proud.

**Žádná reference nebyla smazána** — všechny ověřené existují a sedí.

---

## STEP 6 — Co zůstává nejisté

- **Hollands–Wald–Zhang (PRD 110, 024070):** stránka APS vrátila HTTP 403 (blokace robotů), takže přímé ověření z APS neproběhlo; existence a metadata ale potvrzeny přes vyhledávání (arXiv 2402.00818). Doporučení: do JSON doplnit `arxiv: "2402.00818"`.
- **Neověřené (nesamplované) reference:** z 43 referencí jich bylo přímo ověřeno 22. Zbylých ~21 (Bekenstein 1973, Bardeen–Carter–Hawking, Hawking 1975/1976, Page 1976, Susskind–Thorlacius–Uglum, HPS soft hair, Brown et al. komplexita, Almheiri–Dong–Harlow, Papadodimas–Raju, Bousso 2002, Jacobson 1995, Wall 2012, Unruh 1981, Wald 2001, Mathur 2008/2009) jsou standardní, dobře známé práce s konzistentními ID/DOI; namátkové ověření problémy nenaznačuje, ale formálně ověřeny nebyly.
- **Kvantitativní odhad $\sim \ell_P\sqrt{r_h}$** — otagován jako neověřený; zdroj se nepodařilo jednoznačně dohledat.
- **`maldacena-2003` titul** — JSON uvádí "Eternal Black Holes in Anti-de-Sitter", arXiv "Eternal Black Holes in AdS". Pouhé rozepsání zkratky; neopraveno (není chyba).
