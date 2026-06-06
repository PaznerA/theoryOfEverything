# Ověřovací zpráva — Holografický princip a AdS/CFT

**Datum ověření:** 2026-06-05
**Ověřované soubory:**
- Česká próza: `knowledge-base/cross-cutting/11-holography-adscft.md`
- Anglický JSON fragment: `core-data/fragments/holography-adscft.json`

> **Stav po re-verifikaci (2026-06-05):** Tento fragment prošel druhým,
> nezávislým adversariálním ověřením. Všechny dříve provedené opravy (viz níže)
> byly potvrzeny jako správné a jsou ve zdrojových souborech přítomny. Při tomto
> druhém průchodu nebyla nalezena žádná nová chyba; zdrojové soubory nebyly dále
> upravovány.

## Co bylo zkontrolováno

### Validita JSON
JSON fragment byl při vstupu validní a po všech úpravách zůstává validní (ověřeno `json.load`).

### Audit referencí (cíleno na nejsilnější tvrzení)
Ověřeno přes arXiv / DOI více než 25 referencí (ID se musí rozlišit a současně musí sedět název, autoři i rok):

Plně potvrzené (ID, název, autoři i rok sedí):
- Maldacena 1997 (hep-th/9711200), GKP 1998 (hep-th/9802109), Witten 1998 (hep-th/9802150)
- Strominger–Vafa 1996 (hep-th/9601029), KSS 2004 (hep-th/0405231), Bousso 1999 (hep-th/9905177)
- Ryu–Takayanagi 2006 (hep-th/0603001), HRT 2007 (0705.0016), HKLL (hep-th/0506118)
- Penington 2019 (1905.08255), Almheiri–Engelhardt–Marolf–Maxfield 2019 (1905.08762)
- PSSY replikové červí díry (1911.11977), Almheiri et al. replica (1911.12333)
- Pestun 2007 (0712.2824), Beisert et al. 2010 (1012.3982), Maldacena–Susskind 2013 (1306.0533)
- Almheiri–Dong–Harlow (1411.7041), HaPPY (1503.06237), McGough–Mezei–Verlinde (1611.03470)
- Obied et al. 2018 (1806.08362), Laddha–Raju et al. 2020 (2002.02448)
- Donnay 2023 (2310.12922), Strominger dS/CFT 2001 (hep-th/0106113)
- Strominger Cardy/BTZ 1997 (hep-th/9712251), Hartnoll–Lucas–Sachdev (1612.07324), Hubeny 2015 (1501.00007)
- Bekenstein 1981 (DOI 10.1103/PhysRevD.23.287) — DOI se rozlišuje
- Brown–Henneaux 1986 (DOI 10.1007/BF01211590) — potvrzeno, Commun. Math. Phys. 104, 207 (1986)
- Huang 2024 (2412.05446) — ID i název sedí
- Oba prosincové 2025 články (2512.14389, 2512.10367) — ID se rozlišují, názvy sedí, autoři dohledáni
- Prozaicky citovaná ID stavu 2024–2026 (2506.19720, 2505.08116, 2412.00852, 2512.18912, 2508.08373, 2405.00845) — všechna se rozlišují, názvy sedí

### Audit vzorců
Zkontrolováno vůči autoritativním zdrojům více než 6 klíčových vzorců:
- Bekensteinova mez `S ≤ 2πkRE/(ħc)` — správně
- Bekenstein–Hawking `S = A/4` (Planckovy jednotky) — správně
- KSS `η/s ≥ ħ/(4πk_B) ≈ 0,08 ħ/k_B` — správně (1/4π ≈ 0,0796)
- Slovník AdS5 `L⁴/α'² = 4π g_s N = g_YM² N = λ`, `g_s = g_YM²/(4π)` — správně (konzistentní s R²/α' = √λ)
- Vztah hmotnost–rozměr `Δ(Δ−d) = m²L²`, BF mez `m²L² ≥ −d²/4` — správně
- Brown–Henneaux `c = 3L/2G₃`, Cardy, Ryu–Takayanagi `S = Area/4G` — správně
- N=4 SYM anomálie `a = c = (N²−1)/4` — správně

### Audit konzistence
- Hodnocení „explored": žádná slavná, dobře prozkoumaná dualita není podhodnocena. Klíčové vazby (teorie strun, černé díry/informace, provázání-prostoročas, supergravitace, semiklasická gravitace, emergentní gravitace, Page curve) jsou „well"; „barely" je vyhrazeno pro skutečně tenké mosty (asymptotická bezpečnost, LQG, kauzální množiny, GFT, CDT, nekomutativní geometrie). Hodnocení je poctivé.
- Česká próza a JSON jsou navzájem konzistentní (stejné koncepty, vzorce, reference).
- Identifikátory v `relatedTo`/`connections` odkazují na věrohodná globální/lokální id.

## Co bylo špatně a co bylo opraveno

1. **Chybné arXiv ID u celestiální holografie (Pasterski–Pate–Raclariu).**
   Reference `pasterski-2021` i próza (ref. 26 a inline citace v sekci „Současný stav") uváděly arXiv **2108.04801**. To je ale jiný článek („Lectures on Celestial Amplitudes", jediný autor S. Pasterski). Správný Snowmass white paper „Celestial Holography" od Pasterski, Pate a Raclariu má arXiv **2111.11392**.
   → Opraveno v JSON i ve dvou výskytech v próze.
   → Re-verifikace potvrdila: 2108.04801 = „Lectures on Celestial Amplitudes"
     (jediný autor S. Pasterski) a 2111.11392 = Snowmass white paper „Celestial
     Holography" (Pasterski, Pate, Raclariu). Oprava je správná a je v souborech.

2. **Nesprávné autorství „H. Huang et al." (Huang 2024, 2412.05446).**
   Jde o jednoautorský článek (Han Huang), nikoli „et al.".
   → Opraveno v JSON i v próze (ref. 29) na „H. Huang".

3. **Zástupné autorství „(2025)" u dvou prosincových referencí.**
   Doplněni skuteční autoři: `holography-swampland-2025` = S. Upadhyay, A. Reshetnyak, P. Moshin, R. Castro; `bridging-dscft-celestial-2025` = H. Furugori, N. Ogawa, S. Sugishita, T. Waki.
   → Doplněno v JSON.

Žádná reference nebyla smazána — všechny ostatní vzorkované reference se ověřily jako pravé.

## Co zůstává nejisté

- Dva prosincové 2025 články (2512.14389, 2512.10367) i nejnovější prozaicky citovaná preprintová ID (2024–2026) se rozlišují a názvy sedí, ale jde o velmi čerstvé, dosud nerecenzované preprinty; jejich vědecké závěry nebyly nezávisle ověřeny.
- Reference `huang-2024` (2412.05446) je jednoautorský preprint bez uvedeného časopiseckého vydání — jako „přehled" je věrohodný, ale není to zavedený kanonický review (na rozdíl od MAGOO).
- Drobná strukturální nekonzistence: `connections` mezi pilíři obsahuje cíl `page-curve`, který je zároveň lokálním konceptem v tomto fragmentu (ne samostatný pilíř). Nešlo o faktickou chybu, ponecháno beze změny.
- Roky u některých referencí jsou uváděny dle roku publikace v časopise, nikoli dle data vložení na arXiv (např. ADH „2015" vs. arXiv 11/2014; Hubeny „2015" vs. arXiv 12/2014). Toto je standardní citační konvence, ponecháno.
