# Ověřovací zpráva — Swampland Program & the String Landscape

**Datum:** 2026-06-05
**Ověřované soubory:**
- `knowledge-base/cross-cutting/14-swampland.md` (česká próza)
- `core-data/fragments/swampland.json` (anglický JSON fragment)

## Co bylo zkontrolováno

### Reference (20 z 36 ověřeno přímo přes arXiv)
Ověřeny ID, název, autoři a rok u následujících prací; **všechny rozlišily a metadata odpovídala**:
hep-th/0509212 (Vafa), hep-th/0601001 (Arkani-Hamed–Motl–Nicolis–Vafa), hep-th/0605264 (Ooguri–Vafa), hep-th/0304042 (Polchinski), hep-th/0701050 (Denef–Douglas–Kachru), 1806.08362 (Obied a kol.), 1806.09718 (Agrawal a kol.), 1810.05506 (Ooguri–Palti–Shiu–Vafa), 1810.05337 a 1810.05338 (Harlow–Ooguri), 1810.03637 (Hamada–Noumi–Shiu), 1906.05225 (Lüst–Palti–Vafa), 1909.10355 (McNamara–Vafa), 1910.01135 (Lee–Lerche–Weigand), 1910.01648 (Festina Lente), 2009.03914 (Gao–Hebecker–Junghans), 2106.07650 (FL pheno), 2201.08380 (WGC review), 2205.12293 (Dark Dimension), 2311.01536 (Universal Pattern), 2311.09295 (Grimm–Monnee), 2403.18005 (Tale of Three Scales), 2312.00120 (Rudelius), 2503.19428 (S-dual Quintessence).

Zvláště ověřeny **rizikové prosincové práce z r. 2025** — obě existují a odpovídají:
- **2512.09052** — Montero, Vafa, Valenzuela, *Neutrinos, B-L Symmetry and the Dark Dimension* (9. 12. 2025). OK.
- **2512.22694** — A. Moradpouri, *The species scale and the refined TCC bound in time-dependent backgrounds of string theory* (27. 12. 2025). OK.
- **1912.00607** — Cai & Wang, *A refined trans-Planckian censorship conjecture* (2019). OK.

Žádná **vymyšlená (neexistující) arXiv ID** nebyla nalezena. Žádná reference nebyla smazána.

### Vzorce (ověřeno 6 klíčových proti autoritativním zdrojům)
- Univerzální vzorec `(∇m/m)·(∇Λ_sp/Λ_sp) = 1/(d-2)` — **správně** (2311.01536).
- Slabá gravitační hypotéza (elektrická i magnetická) — **správně**.
- Měřítko druhů `Λ_sp ~ M_Pl/√N` — **správně**.
- Festina Lente `m² ≥ √6 g q M_Pl H` — první forma **správně**.

## Co bylo špatně a opraveno

1. **Žurnálová reference WGC review (2201.08380).** Uvedeno chybně „Rev. Mod. Phys. 96 (2024) 035007“ (rok 2024, DOI .96./035007). Správně je **Rev. Mod. Phys. 95 (2023) 035003**, DOI `10.1103/RevModPhys.95.035003`, rok 2023. Opraveno v JSON (`year`, `doi`, `significance`) i na třech místech v próze (řádky cca 165, 339, 348).

2. **Exponent KK/winding věže (SDC).** Próza i JSON (`wgc-kk-rate`) uváděly `α = √2·√((d-1)/(d-2))`. Faktor **√2 je chybný**. Standardní exponent KK věže je `√((d+n-2)/(n(d-2)))`, pro jednu extra dimenzi (n=1) tedy `√((d-1)/(d-2))` (v d=4 = √(3/2)) — bez √2 (zdroj: Etheredge–Heidenreich–Kaya–Qiu–Rudelius, 2206.04063). Opraveno v próze i JSON; přidána i obecná n-závislá forma a dolní mez α ≥ 1/√(d-2).

3. **Festina Lente — druhá forma s V.** Próza i JSON uváděly „⟺ m⁴ ≥ 6(gq)²V". To je **chybné o faktor 3**: z V = 3 M_Pl² H² plyne `m⁴ ≥ 2(gq)²V`. Opraveno (původní `m⁴ ≥ 6(gq M_Pl H)²` je správně, převod na V dává koeficient 2).

4. **TCC asymptotický koeficient — chybné označení.** Koeficient `2/√((d-1)(d-2))` byl označen jako „asymptotický". Podle Bedroya–Vafa (1909.11063) je to mez **přes monotónní úsek**; skutečná **asymptotická** mez pro velké pole je `2/√(d-2)`. Opraveno označení a doplněna obě meze v próze (koncept i mat. rámec) i v JSON (`trans-planckian-censorship`, `tcc-bound`).

5. **Atribuce autora Festina Lente.** JSON uváděl „G. Venken" u 1910.01648 i 2106.07650. Správně je **V. Venken** (Victoria Venken; Gerben Venken je jiná osoba). Opraveno na „V. Venken".

6. **Vnitřní rozpor hodnocení (twistors-amplitudes).** Nadpis v próze říkal „sotva prozkoumáno", ale tělo i JSON říkají „částečně" (`partially`). Sjednoceno na **„částečně prozkoumáno"**.

7. **Přidána reference** `etheredge-sharpening-2022` (2206.04063), aby vzorec KK exponentu měl ověřitelný zdroj. JSON zůstává validní; všechny `source` u vzorců se rozlišují na existující reference.

## Co zůstává nejisté / drobné poznámky

- **Cosmetická ID neshoda (neopravené, nezavádějící v zobrazených polích):** `dvali-three-scales-2024` ve skutečnosti odkazuje na práci Bedroya–Vafa–Wu (autoři v poli `authors` jsou správně); `bena-kklt-control-2020` odkazuje na Gao–Hebecker–Junghans (Bena není autor; pole `authors` správné). Jde jen o vnitřní slug, nikoli o chybu v zobrazených metadatech — ponecháno.
- **Verze/datum 2512.09052:** WebFetch hlásil revizi „3. 3. 2026" shodně s prací o temné dimenzi — možná záměna modelu; název a autoři však sedí a práce existuje.
- **Statistické odhady krajiny** (~10^500, dolní mez ~10^272000 pro F-teorii) a Bousso–Polchinski discretuum nejsou samostatně číslovanými referencemi (poznámka v textu to přiznává); nebyly nezávisle ověřeny proti primárnímu zdroji.
- **Numerické fenomenologické hodnoty** scénáře temné dimenze (ℓ ≈ 7,42 μm, m ≈ 2,31 meV) a meze TCC (V^{1/4} ≲ 10⁹ GeV, ε < 10⁻³¹) nebyly přepočítány do detailu; řádově odpovídají literatuře.
