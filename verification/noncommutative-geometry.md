# Ověřovací zpráva — Nekomutativní geometrie (Noncommutative Geometry)

**Datum ověření:** 2026-06-05
**Ověřované soubory:**
- Česká próza: `/Users/pazny/projects/theoryOfEverything/knowledge-base/approaches/07-noncommutative-geometry.md`
- Anglický JSON fragment: `/Users/pazny/projects/theoryOfEverything/core-data/fragments/noncommutative-geometry.json`

---

## Co bylo zkontrolováno

### 1. Validita JSON
JSON byl od počátku syntakticky validní. Po provedených úpravách (odstranění tří spojení) byl znovu ověřen Pythonem — **zůstává validní**.

### 2. Audit referencí (zkontrolováno 25+ referencí, tedy prakticky všechny)
U každé reference jsem přes WebFetch ověřil, že arXiv ID / DOI **rezolvuje** a že **název, autoři i rok odpovídají**. Ověřené a v pořádku:

| Reference | arXiv/DOI | Stav |
|---|---|---|
| Snyder 1947 | 10.1103/PhysRev.71.38 | OK |
| DFR 1995 | hep-th/0303037 (repost CMP 172, 1995) | OK — rok 1995 je správně (publikace), arXiv repost je z 2003 |
| Connes 1995 *NCG and reality* | 10.1063/1.531241 (JMP 36, 6194) | OK |
| Chamseddine–Connes 1996 *Spectral Action* | hep-th/9606001 | OK |
| Kempf–Mangano–Mann 1995 | hep-th/9412167 | OK |
| Seiberg–Witten 1999 | hep-th/9908142 | OK |
| Amelino-Camelia (DSR review) | 1003.3942, rok 2010 | OK (viz poznámka níže k id) |
| Chamseddine–Connes–Marcolli 2007 | hep-th/0610241 | OK |
| Connes 2008 *spectral characterization* | 0810.2088 | OK |
| Aastrup–Grimstrup–Nest 2009 | 0802.1783 | OK |
| Chamseddine–Connes 2012 *Resilience* | 1208.1030 | OK |
| Chamseddine–Connes–van Suijlekom 2013 | 1304.7583 | OK |
| Chamseddine–Connes–Mukhanov 2014 *Quanta* | 1409.2471 | OK |
| Chamseddine–Connes–Mukhanov 2014b *Basics* | 1411.0977 | OK |
| Chamseddine–Connes–van Suijlekom 2015 | 1507.08161 | OK |
| Barrett–Glaser 2016 | 1510.01377 | OK |
| D'Andrea–Kurkov–Lizzi 2016 | 1605.03231 | OK |
| Lizzi 2018 | 1805.00411 | OK |
| Marcolli–Pierpaoli–Teh 2010 | 1012.0780 | OK (3 autoři vč. Teh — v próze i JSON správně) |
| Hessam–Khalkhali–Pagliaroli 2022 | 2204.14206 | OK |
| Khalkhali–Pagliaroli 2023 | 2312.10530 | OK |
| van Suijlekom 2024 (2. vyd.) | 10.1007/978-3-031-59120-4 | OK |
| Chamseddine 2025 *Hearing the Shape* | 2511.05909 | OK |
| Dąbrowski et al. 2025 *Spectral torsion* | 2511.08159 | OK (autoři: Dąbrowski, Mukhopadhyay, Požar) |
| D'Arcangelo–Gnutzmann 2026 | 2601.14141 | OK |
| Khalkhali–Pagliaroli 2025 *Bootstrapping* | 2512.08694 | OK |
| Gamble–Khalkhali–Pagliaroli 2026 *Schwinger-Dyson* | 2606.01343 | OK |
| Carlip 2017 | 1705.05417 | OK |
| Steinacker 2010 | 1003.4134 | OK |
| Kudler-Flam–Leutheusser–Satishchandran 2023 | 2309.15897 | OK |
| Valero–Gisbert–Ilisie 2025 *GUP bounds* | 2505.06598 | OK |
| Wei 2025 (GRB polarimetrie, jen v próze) | 2503.18277 | OK |

**Pozoruhodné:** I velmi nedávné reference (prosinec 2025, leden/květen 2026) rezolvují a souhlasí — žádné vymyšlené ID, žádná chybná atribuce autorů ani roku u referencí v seznamu.

### 3. Audit formulí (zkontrolováno 9 klíčových)
- **Tabulka znamének KO-dimenze** (ε, ε′, ε″ pro n mod 8) — odpovídá kanonické tabulce Connes 1995 / Chamseddine–Connes–Marcolli 2007. **Správně.**
- **Princip spektrální akce** `S = Tr f(D/Λ) + ⟨ψ,Dψ⟩` — správně.
- **Heat-kernel rozvoj** `f_4 Λ^4 a_0 + f_2 Λ^2 a_2 + f_0 a_4` a momenty `f_k = ∫_0^∞ f(u) u^{k-1} du` (k>0), `f_0 = f(0)` — odpovídá standardní konvenci. **Správně.**
- **GUP** `[x,p]=iℏ(1+βp²) ⟹ Δx_min = ℏ√β` (Kempf–Mangano–Mann) — ověřeno proti literatuře. **Správně.**
- **Moyalův hvězdičkový součin** vč. rozvoje 1. řádu `fg + (i/2)θ^{μν}∂_μf ∂_νg` — správně.
- **Fuzzy sféra** `[x_i,x_j] = (ir/√(j(j+1))) ε_ijk x_k`, `x_i = (r/√(j(j+1)))J_i` — správně.
- **Vnitřní fluktuace** `D_A = D + A + ε′ JAJ⁻¹` — správně.
- **Connesova vzdálenostní formule** + vztah ke geodetické / Wassersteinově vzdálenosti řádu 1 — ověřeno; správně (s drobnou subtilitou u diskrétních prostorů, viz níže).
- **DFR relace neurčitosti** — odpovídají standardním DFR vztahům. **Správně.**

### 4. Audit konzistence
- **Cílové slug-y spojení** porovnány proti reálným fragmentům v `core-data/fragments/`. 15 z 18 cílů byly platné pilíře; **3 cíle byly chybné** (mířily na interní koncepty místo na jiné pilíře) — opraveno.
- **`source` formulí a `relatedTo` konceptů** — všechny `source` formulí míří na existující id referencí. `relatedTo` cíle mimo lokální koncepty jsou hodnověrné globální/křížové id (string-theory, asymptotic-safety, grand-unification, liouville-quantum-gravity, cosmological-constant-problem atd.) — akceptováno.
- **Hodnocení „explored"** — próza a JSON jsou **plně konzistentní** u všech 15 spojení. Žádná slavná, dobře prozkoumaná dualita není podhodnocena. Hodnocení „well" (struny ↔ Moyal/Seiberg–Witten, experimentální testy/DSR fenomenologie) jsou poctivá; nově vznikající mosty (von Neumann/holografie, entanglement) jsou poctivě „partially"/„barely".
- **Próza vs. JSON** — věcně bez rozporů (algebra SM `C ⊕ H ⊕ M_3(C)`, KO-dim 6, celkový časoprostor 10 ≡ 2 mod 8, oprava predikce Higgse σ-polem na 125 GeV — vše konzistentní mezi oběma soubory).

---

## Co bylo špatně a opraveno

1. **Chybná atribuce reference u černých děr (próza).**
   Citace `arXiv:1304.6581` měla podpírat tvrzení o „kvantizaci plochy horizontu v násobcích minimální plochy" a „regulárním jádru nekomutativních černých děr". Ve skutečnosti je `1304.6581` článek Sho Tanaky *„Where Does Black Hole Entropy Lie?…"* — týká se sice NCG a area-entropy zákona, ale **nepodpírá konkrétní citovaná tvrzení**. Citace odstraněna a dotčené tvrzení označeno `⚠️ neověřeno`.

2. **Tři chybná spojení v JSON (`connections`).**
   Spojení s cíli `doubly-special-relativity`, `minimal-length` a `relative-locality` mířila na **interní koncepty tohoto fragmentu**, nikoli na jiné pilíře (mezi fragmenty v `core-data/fragments/` neexistují). Pilíř má být spojen s jinými pilíři; tyto vztahy jsou už zachyceny v poli `relatedTo` příslušných konceptů. **Tři spojení odstraněna** (18 → 15). JSON zůstává validní.

---

## Co zůstává nejisté

1. **Reference id `amelino-camelia-2002`** má slug naznačující rok 2002, ale pole `year` je 2010 a obsah je DSR přehled z r. 2010 (arXiv 1003.3942). Formule `kappa-minkowski-commutator` na tuto id míří. Reference rezolvuje správně a pole `year` je v pořádku; slug je pouze zavádějící (kosmetické, neopraveno, aby se nerozbily interní ukazatele `source`).

2. **Subtilita Connesova vzdálenost vs. Wasserstein.** Tvrzení „pro smíšené stavy = Wassersteinova vzdálenost řádu 1" je v souladu s běžným fyzikálním podáním, ale v literatuře existuje upřesnění, že na *diskrétních* prostorech se spektrální vzdálenost mezi obecnými stavy obecně nerovná Wassersteinově vzdálenosti s nákladem rovným spektrální vzdálenosti mezi čistými stavy. Pro spojité variety tvrzení platí. Ponecháno beze změny jako přijatelné zjednodušení.

3. **Atribuce zdroje formule fuzzy sféry** (`steinacker-2010`). Relace fuzzy sféry pocházejí historicky od Madoreho (1992); Steinackerova přehledová práce 2010 je obsahuje, takže jako zdroj je akceptovatelná, ale není to původní reference.

4. **Tvrzení o nekomutativních černých dírách** (regulární jádro, kvantizace plochy) zůstává po odstranění chybné citace **bez podpůrné reference** a je označeno `⚠️ neověřeno`. Tvrzení je v literatuře pravdivé (Nicolini a spol.), ale konkrétní citace nebyla doplněna.

5. **Reference-only ověření.** Tituly/autoři/roky byly ověřeny proti arXiv/DOI metadatům; **obsahová** správnost toho, že daný článek skutečně dokazuje konkrétní tvrzení v textu, byla ověřena jen u nejsilnějších tvrzení (spektrální akce, KO-dim, GUP, Connesova vzdálenost, struny↔NCG). U ostatních se spoléhá na shodu tématu.
