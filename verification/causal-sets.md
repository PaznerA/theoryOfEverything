# Ověřovací zpráva: Pilíř „causal-sets"

**Datum:** 2026-06-05
**Agent:** adversarial-verification (economy mode)
**Soubory:** `knowledge-base/approaches/05-causal-sets.md`, `core-data/fragments/causal-sets.json`

---

## Shrnutí

Celkem ověřeno **10 referencí** (8 primárních + 2 doplňkové). Nalezeny a opraveny **3 chyby**; zbývají **2 menší obavy** (viz níže).

---

## Ověřené reference

| # | arXiv / DOI | Výsledek |
|---|-------------|---------|
| Bombelli et al. 1987 | DOI 10.1103/PhysRevLett.59.521 | OK — zakládající PRL, autoři a rok správně |
| Surya 2019 | arXiv:1903.11544 | OK — Living Rev. Relativ. 22, 5 (2019), autorka správně |
| Rideout & Sorkin 1999 | arXiv:gr-qc/9904062 | OK — PRD 61, 024002 (2000), autoři a rok správně |
| Benincasa & Dowker 2010 | arXiv:1001.2725 | OK — PRL 104, 181301 (2010), autoři a rok správně |
| Dowker & Glaser 2013 | arXiv:1305.2588 | OK — CQG 30, 195016 (2013), autorky správně |
| Ahmed et al. 2004 | arXiv:astro-ph/0209274 | OK — PRD 69, 103523 (2004), autoři správně |
| Zwane, Afshordi & Sorkin 2018 | arXiv:1703.06265 | OK — CQG (2018), autoři správně |
| Loomis & Carlip 2017 | arXiv:1709.00064 | OK — CQG, DOI 10.1088/1361-6382/aa980b, autoři správně |
| Adamson & Wallden 2025 | arXiv:2505.22217 | **CHYBA** — opraveno níže |
| Ferguson, Nasiri & Wallden 2025 | arXiv:2506.19538 | **CHYBA** — opraveno níže |
| Saravani & Aslanbeigi | arXiv:1502.01655 | **CHYBA** — rok v MD byl 2014, správně 2015 |

---

## Opravené chyby

### 1. Špatný titul: Adamson & Wallden 2025
- **Původní:** „Benincasa-Dowker causal set actions by quantum counting"
- **Správný:** „Benincasa-Dowker-**Glaser** causal set actions by quantum counting"
- Publikováno: Phys. Rev. Research **8**, 023188 (2026)
- Opraveno v: `05-causal-sets.md` (text i seznam referencí), `causal-sets.json` (title, přidáno DOI)

### 2. Chybějící autoři: qmcmc-2025 (arXiv:2506.19538)
- **Původní autoři v JSON:** „(causal set collaboration)"
- **Správní autoři:** Stuart Ferguson, Arad Nasiri, Petros Wallden
- Opraveno v: `causal-sets.json` a `05-causal-sets.md`

### 3. Špatný rok: Saravani & Aslanbeigi
- arXiv:1502.01655 byl podán únor 2015, publikován PRD 92, 103504 (2015)
- **Původní rok v MD (ref. 19):** 2014
- **Správný rok:** 2015
- Opraveno v: `05-causal-sets.md` (seznam referencí)
- Rok v `causal-sets.json` (pole `saravani-2015-dm`) byl již správně 2015

---

## Ověření klíčových vzorců

| Vzorec | Výsledek |
|--------|---------|
| Axiomy causetu (4 podmínky) | OK — reflexivita, antisymetrie, tranzitivita, lokální konečnost |
| Poissonovo rozsetí $P_v(n) = (\rho v)^n e^{-\rho v}/n!$ | OK — standardní tvar |
| Diskrétní d'Alembertián 4D: koeficienty $(+1,-9,+16,-8)$ pro vrstvy $L_1..L_4$, prefaktor $4/(\sqrt{6}\,\ell^2)$ | OK — konzistentní s Benincasa & Dowker 2010 |
| BD akce: $N - N_1 + 9N_2 - 16N_3 + 8N_4$ | OK — znaménka a koeficienty konzistentní s d'Alembertiánem |
| Myrheim-Meyer dimenze: $f_0(d) = \Gamma(d+1)\Gamma(d/2)/[4\Gamma(3d/2)]$ | OK — standardní tvar z Meyer 1988 |
| SJ vakuum: $W_{SJ} = \sum_{\lambda_k>0}\lambda_k u_k u_k^*$ | OK — kladná část spektra Pauli-Jordanova operátoru |

---

## Zbývající obavy

1. **Rok Sorkinovy předpovědi $\Lambda$:** Tvrzení „předpověď z roku 1987" je v komunitě tradičně přijímáno, ale explicitní číslo $10^{-120}$ se poprvé objevuje v pozdějších Sorkinových přednáškách (1990s); formálně arXiv:0710.1675 (2007). Jde o slabé tvrzení konzistentní s konsensem (Surya 2019), nikoli prokazatelnou chybu — neoznačeno, ale hodné pozornosti.

2. **Citace Layden et al. (Nature 619, 282, 2023):** Citace pro qmcmc-2025 nebyla přímo ověřena (stránková čísla). Doporučuji ověřit při dalším průchodu.

---

## Celkový závěr

Oba soubory jsou po opravách faktograficky spolehlivé. JSON zůstává validní. Žádná reference nebyla smazána — všechny ověřené ID resolují a autoři odpovídají. Největší nalezená chyba byl neúplný titul klíčové práce z roku 2025 (chybějící „Glaser") a placeholder autoři u MCMC paperu.
