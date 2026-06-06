# Verifikační zpráva — Supergravitace a UV chování perturbativní gravity

**Pilíř:** `supergravity-uv`
**Ověřované soubory:**
- `/Users/pazny/projects/theoryOfEverything/knowledge-base/approaches/10-supergravity-uv.md` (česká próza)
- `/Users/pazny/projects/theoryOfEverything/core-data/fragments/supergravity-uv.json` (anglický JSON fragment)

**Datum kontroly:** 2026-06-05
**Režim:** adversariální verifikace (předpoklad, že chyby existují)

---

## 1. Platnost JSON

JSON byl při prvním načtení **validní**, nebylo třeba jej opravovat. Po všech editacích zůstává validní (ověřeno `json.load`).

---

## 2. Audit referencí

Ověřeno **20+ referencí** (přes WebFetch arXiv abstraktů / DOI), s prioritou na ty, které podpírají nejsilnější tvrzení. Pro každou byly kontrolovány: existence ID, titul, autoři a rok.

### Ověřeno jako správné (titul + autoři + rok souhlasí)

- `tHooft-Veltman-1974` (Ann. Inst. H. Poincaré) — OK
- `Donoghue-1994` (gr-qc/9405057) — OK
- `Bjerrum-Bohr-Donoghue-Holstein-2003` (hep-th/0211072) — OK (paper podán 2002, publikován 2003; rok 2003 je v pořádku)
- `Bern-Dixon-Roiban-2006` (hep-th/0611086) — OK (podán 2006, publikován 2007; rok 2006 v referenci, 2007 v próze — obojí obhajitelné)
- `Bern-et-al-2007-3loop` (hep-th/0702112) — OK
- `Bern-Carrasco-Johansson-2008-BCJ` (0805.3993) — OK
- `Bern-et-al-2008-3loop-manifest` (0808.4112) — OK
- `Bern-Carrasco-Johansson-2010` (1004.0476) — OK
- `Beisert-et-al-2010-E7` (1009.1643) — OK
- `Bern-Davies-Dennen-Huang-2012` (1202.3423) — OK
- `Bern-Davies-Dennen-2014-N5` (1409.3089) — OK
- `Salvio-Strumia-2014` (1403.4226) — OK
- `Kallosh-2014-update` (1412.7117) — OK; tvrzení v próze („žádné divergentní 1PI struktury za 6 smyčkami", konflikt s dřívější předpovědí divergence na 7 smyčkách) **přesně** odpovídá zdroji
- `Barvinsky-et-al-2016-Horava` (1512.02250) — OK
- `Gies-Knorr-Lippoldt-Saueressig-2016` (1601.01800) — OK
- `Bern-et-al-2018-5loop` (1804.09311) — OK (titul i 8 autorů souhlasí; D_c=24/5, protičlen D^8R^4, žádná zesílená kancelace na 5 smyčkách — vše souhlasí)
- `Horava-2009` (0901.3775) — OK
- `Biswas-Gerwick-Koivisto-Mazumdar-2012` (1110.5249) — OK
- `Maldacena-2011-conformal` (1105.5632) — OK
- `Donoghue-2022-review` (2211.09902) — OK
- `Bern-et-al-2023-review` (2304.07392) — OK
- `Quanta-2025-ghost` — OK (titul, autor Charlie Wood, datum 17. 11. 2025, všech 6 jmen badatelů ověřeno)

---

## 3. Nalezené a opravené problémy

### PROBLÉM 1 — Špatný titul reference Green-Ooguri-Schwarz (oba soubory) — OPRAVENO

Reference `Green-Ooguri-Schwarz-2007` (arXiv:0704.0777) byla uvedena s titulem
*„Nondecoupling of maximal supergravity from the superstring"*.
Skutečný titul je **„Decoupling Supergravity from the Superstring"**.

ID se rozlišuje správně, autoři (Green, Ooguri, Schwarz) i rok 2007 souhlasí, a **směr tvrzení je správný** — práce skutečně argumentuje, že perturbativní maximální supergravitaci NELZE oddělit od strun pro d>3, a konjekturuje, že je ve swamplandu. Chybný byl pouze titul.

**Oprava:** titul opraven v JSON (`title`) i v próze (seznam referencí, položka 11). Do prózy doplněna poznámka o swamplandové konjektuře. Tvrzení v těle textu (řádky 163, 234, 249, 273) jsou věcně správná a zůstala.

### PROBLÉM 2 — Chybějící autoři reference Bern-Davies-Dennen 2013 (oba soubory) — OPRAVENO

Reference `Bern-Davies-Dennen-2013-N4` (arXiv:1309.2498) uváděla pouze 3 autory
(„Z. Bern, S. Davies, T. Dennen").
Skutečný autorský seznam má **5 autorů**: Z. Bern, S. Davies, T. Dennen, **Alexander V. Smirnov, Vladimir A. Smirnov**.

**Oprava:** doplněni oba Smirnovové v JSON (pole `authors`) i v próze (seznam referencí položka 17 a historická časová osa, řádek 164). Věcné tvrzení (N=4 diverguje na 4 smyčkách kvůli U(1) anomálii duality) je správné.

### PROBLÉM 3 — Chybějící arXiv ID u Anselmi 2024 (JSON) — OPRAVENO

Reference `Anselmi-2024-fakeons` odkazovala pouze na `renormalization.com/24a2/`. Práce má ověřitelné arXiv ID **2410.21599** (titul i autor souhlasí).

**Oprava:** doplněno pole `arxiv: "2410.21599"` a `url` přesměrováno na arXiv abstrakt.

---

## 4. Audit vzorců

Ověřeno proti autoritativním zdrojům **více než 5 klíčových vzorců**:

1. **Goroffův-Sagnottiho koeficient 209/2880** u C^3 protičlenu — **POTVRZENO** (web. zdroje k dvousmyčkové renormalizaci gravity).
2. **Donoghueho kvantová korekce potenciálu, koeficient 41/(10π)** u G·ℏ/r²c³ — **POTVRZENO** (je to publikovaný univerzální koeficient; klasický PN člen 3G(m₁+m₂)/rc² je rovněž standardní).
3. **Kritická dimenze D_c = 4 + 6/L** — **POTVRZENO**: L=3 → 6, L=4 → 11/2; na 5 smyčkách by formule dala 26/5, ale naměřeno 24/5 (nižší). Soubory tento jemný bod (žádná zesílená kancelace na 5 smyčkách) popisují správně a v souladu s Bern et al. 2018.
4. **Spinový obsah N=8: (1, 8, 28, 56, 70)** přes binom. koef. \binom{8}{4-2s}; 256 stavů; 70 skalárů parametrizuje E7(7)/SU(8) (dim 133−63=70) — **POTVRZENO**.
5. **arXiv 2603.07150** (citovaná v próze, taxonomie duchů, položka 4 — PT-symetrie / invertovaný harmonický oscilátor) — **POTVRZENO jako reálná práce** (Kumar & Marto, 25. 3. 2026). NENÍ vymyšlená.
6. **Stelleho propagátor / rozklad na póly 1/(p²(p²+M²))** — algebraicky správný; znaménko ducha konzistentní.

### Drobná poznámka ke vzorci `onshell-oneloop-counterterm` (1/120 R² + 7/20 R_μν²)

**Relativní** koeficienty 1/120 a 7/20 jsou standardní, literaturou potvrzené hodnoty 't Hooftova-Veltmanova jednosmyčkového výsledku a nesou fyziku (mizení on-shell přes R_μν=0). Celkový předfaktor je v JSON psán jako 1/(ε)·1/(4π)², zatímco kanonická forma bývá 1/(8π²(d−4)); to se liší o faktor 2 a znaménko (konvenční volba ε=4−d vs. d−4). Jde o **konvenční normalizaci**, nikoli o věcnou chybu v poměru koeficientů. Ponecháno beze změny; poznamenáno níže jako drobná nejistota.

---

## 5. Audit konzistence

- **relatedTo (koncepty):** Pět cílů neukazuje na lokální koncept fragmentu: `power-counting`, `string-theory`, `holographic-principle`, `cosmological-constant-problem`. Jsou to **věrohodná globální (mezipilířová) id** odkazující na jiné pilíře/koncepty — v pořádku.
- **Zdroje vzorců:** všech 14 polí `source` odpovídá existujícímu `id` reference — v pořádku.
- **Próza vs. JSON:** žádný věcný rozpor nenalezen (po opravě titulu a autorů). Číselné hodnoty (209/2880, 41/10π, D_c hodnoty, spinový obsah) jsou v obou souborech shodné.
- **Hodnocení „explored":** poctivé. Dva nejlépe prozkoumané mosty (`string-theory`, `twistors-amplitudes`) jsou hodnoceny „well" — což je správné, protože vztah N=8 SUGRA ke strunám (string limit, double copy, KLT) a k amplitudovým metodám je skutečně intenzivně studovaný. **Žádná slavná dualita není podhodnocena na „barely".** Mosty „barely" (spectral-dimension, swampland, CDT, LQG, NCG, emergent, black holes) jsou věrohodně okrajové.
- **Hodnota agravity inflace n_s≈0.967, r≈0.13** (řádek 258) — ověřena jako **původní predikce Salvia-Strumii** (r≈0.13 je horní mez rozsahu 0.003 < r < 0.13). Próza ji uvádí věrně jako predikci dané práce.

---

## 6. Co zůstává nejisté

1. **Strukturální nesoulad dvou `connections`:** cíle `cosmological-constant-problem` a `spectral-dimension` neodpovídají žádnému existujícímu slugu pilíře (fragmentu) v projektu. `spectral-dimension` je navíc lokální koncept fragmentu, nikoli samostatný přístup. Obsah těchto vazeb je fyzikálně smysluplný, proto **nebyly smazány**; ale jejich cílová id by měla být přemapována na reálné pilíře (např. unimodulární → kosmologická konstanta jako součást jiného pilíře) nebo přeznačena jako pojmové, nikoli mezipilířové vazby. **Doporučuji revizi datového modelu, nikoli smazání obsahu.**
2. **Konvenční předfaktor vzorce `onshell-oneloop-counterterm`** (faktor 2 a znaménko vůči kanonické 1/(8π²(d−4))). Relativní koeficienty (fyzika) jsou správné; absolutní normalizace by si zasloužila sjednocení konvence. Nepovažováno za chybu, jen za konvenční nejednoznačnost.
3. **Přesné koeficienty 1/120 a 7/20** se nepodařilo extrahovat přímo z původního 't Hooftova-Veltmanova PDF (PDF byla nečitelná / TLS chyby); spoléhá se na shodu se standardní literaturou a potvrzení on-shell konečnosti čisté gravity z více zdrojů. Vysoká, nikoli však absolutní jistota.

---

## 7. Shrnutí

- **Ověřeno referencí:** 22
- **Nalezené problémy:** 3 (špatný titul GOS, chybějící 2 autoři BDD-2013, chybějící arXiv ID Anselmi)
- **Opraveno:** 3
- **Zbývající nejistoty:** 2 strukturální nesoulady `connections` + konvenční předfaktor jednosmyčkového vzorce

Žádná reference se neukázala jako vymyšlená; všechna arXiv ID se rozlišují. Hlavní fyzikální tvrzení (nerenormalizovatelnost přes Goroff-Sagnotti, EFT predikce 41/10π, otevřená 7-smyčková otázka N=8, zesílené kancelace, problém duchů) jsou věcně správná a dobře podložená.
