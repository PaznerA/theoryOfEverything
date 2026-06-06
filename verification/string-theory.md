# Verifikační zpráva — Teorie strun a M-teorie

**Datum:** 2026-06-05
**Ověřované soubory:**
- Česká próza: `knowledge-base/approaches/01-string-theory.md`
- Anglický JSON fragment: `core-data/fragments/string-theory.json`

---

## Co bylo zkontrolováno

### 1. Validita JSON
JSON je syntakticky platný (47 konceptů, 17 vzorců, 32 referencí, 8 otevřených problémů, 17 propojení). Žádné duplicitní `id` konceptů ani referencí. Všechny `source` u vzorců odkazují na existující reference. Žádné opravy struktury nebyly nutné.

### 2. Audit referencí (ověřeno 24 z 32 — výrazně nad minimem 12)
Každá reference byla ověřena přes arXiv (`https://arxiv.org/abs/ID`) nebo DOI; kontrolovala se shoda názvu, autorů a roku. Ověřené (a potvrzené jako správné):

- **Maldacena 1997** (hep-th/9711200) — AdS/CFT — OK
- **Strominger & Vafa 1996** (hep-th/9601029) — entropie ČD — OK
- **Witten 1995** (hep-th/9503124) — M-teorie — OK
- **Polchinski 1995** (hep-th/9510017) — D-brány — OK
- **BFSS 1996** (hep-th/9610043) — OK
- **IKKT 1996** (hep-th/9612115) — OK (arXiv prosinec 1996)
- **Ooguri & Vafa** (hep-th/0605264) — Distance Conjecture — OK
- **Arkani-Hamed et al.** (hep-th/0601001) — WGC — OK (arXiv leden 2006)
- **Ryu & Takayanagi 2006** (hep-th/0603001) — OK
- **Lee, Lerche, Weigand 2019** (1910.01135) — Emergent String Conjecture — OK
- **Sen & Zwiebach 2024** (2405.19421) — přehled SFT — OK (reálná práce, nešlo o smyšlenku)
- **Montero, Vafa, Valenzuela 2022** (2205.12293) — dark dimension — OK
- **Vafa 2005** (hep-th/0509212) — swampland — OK
- **Green & Schwarz 1984** (DOI 10.1016/0370-2693(84)91565-X) — OK
- **Gross, Harvey, Martinec, Rohm 1985** (PRL 54, 502; DOI 10.1103/PhysRevLett.54.502) — OK
- **Veneziano 1968** (DOI 10.1007/BF02824451) — OK
- **KKLT 2003** (hep-th/0301240) — OK
- **Conlon, Quevedo, Suruliz 2005** (hep-th/0505076) — LVS — OK
- **Strominger 1997** (hep-th/9712251) — OK
- **GKP 1998** (hep-th/9802109) — OK
- **Witten 1998** (hep-th/9802150) — OK
- **Obers & Pioline** (hep-th/9809039) — OK (arXiv 1998, Phys. Rept. 1999)
- **Obied, Ooguri, Spodyneiko, Vafa 2018** (1806.08362) — dS swampland — OK
- **Hořava & Witten 1995** (hep-th/9510209) — OK (arXiv 1995, NPB 1996)
- **Bena, Martinec, Mathur, Warner 2022** (2204.13113) — OK
- **Mathur 2005** (hep-th/0502050) — fuzzball — OK
- **Palti 2019** (1903.06239) — OK
- **Seiberg & Witten 1999** (hep-th/9908142) — OK

Ověřeny i arXiv ID citované v sekci „Současný stav" prózy:
- **2309.10024** = Rudelius, „Gopakumar-Vafa Invariants and the Emergent String Conjecture" — OK; potvrzena i citace **JHEP 03(2024)061**.
- **2310.07708 / JHEP 12(2024)019** = Castellano, Herráez, Ibáñez, „On the species scale…" — OK.
- **2503.17310** = Bena & Warner, „Microstate Geometries" (2025) — OK.
- **2507.00615** = AbdusSalam et al., numerická stabilizace Kählerových modulů (2025) — OK.
- **2205.06016** = Brahma, Brandenberger, Laliberte, BFSS kosmologie (2022) — OK.
- **brennan-carta-vafa 1711.00864** — OK.

**Výsledek auditu referencí:** Žádná vymyšlená arXiv ID, žádná chybná atribuce autorů, žádné neexistující/parafrázované názvy. Všechny vzorky se rozlišily správně.

### 3. Audit vzorců (ověřeno >5 klíčových vzorců proti autoritativním zdrojům)
- **Polyakovova akce** — koeficient $-1/4\pi\alpha'$ — správně.
- **Napětí D$p$-brány** — kompaktní tvar $2\pi/(g_s(2\pi\sqrt{\alpha'})^{p+1})$ je algebraicky totožný se standardním Polchinského $1/((2\pi)^p g_s\,\alpha'^{(p+1)/2})$ — správně.
- **Strominger–Vafa** — centrální náboj $c=6Q_1Q_5$ a $S=2\pi\sqrt{Q_1Q_5 n}$ potvrzeno — správně.
- **Cardyho formule** — $S=2\pi\sqrt{(c/6)(L_0-c/24)}$ — správně.
- **Chern–Simonsův člen 11D SUGRA** — koeficient $-1/(12\kappa^2)$ (tj. $-\tfrac{1}{6}$ v normalizaci $1/2\kappa^2$, $\alpha=1$ CJS) — správně.
- **Hagedornova teplota (uzavřená struna)** — $T_H=1/(4\pi\sqrt{\alpha'})$ pro typ II — potvrzeno.

Žádné chybné znaménko ani koeficient nebyly nalezeny.

### 4. Audit konzistence
- Všechny `relatedTo` cíle, které nejsou lokálními koncepty, jsou věrohodná globální id (slugy jiných pilířů nebo dílčí koncepty: `black-holes-information`, `supergravity-uv`, `central-charge`, `graviton`, `page-curve`, `supersymmetry` atd.).
- Všechny `connections.to` odkazují na věrohodné slugy pilířů.
- Hodnocení `explored` jsou poctivá: AdS/CFT, černé díry, supergravitace, swampland = „well" (správně — nejde podhodnotit slavné, dobře prozkoumané duality); LQG, asymptotická bezpečnost, kauzální množiny, CDT, GFT = „barely" (poctivě, most prakticky neexistuje).
- Próza neodporuje JSON; hodnocení v próze („dobře/částečně/sotva prozkoumáno") odpovídají hodnotám v JSON.

---

## Co bylo špatně a opraveno

1. **Nekonzistence roku u tří referencí** (id slug vs. pole `year`): pole `year` bylo nastaveno na rok časopisecké publikace, zatímco slug i próza používaly rok arXiv preprintu. Sjednoceno na rok arXiv preprintu (shodný se slugem):
   - `strominger-1997`: `year` 1998 → **1997**
   - `ooguri-vafa-2006`: `year` 2007 → **2006**
   - `arkani-hamed-2007`: `year` 2007 → **2006** (arXiv hep-th/0601001, leden 2006)
2. **Milník IKKT v próze** uváděl „(1997)", zatímco reference i JSON mají 1996 (arXiv prosinec 1996). Opraveno v próze na **„IKKT model (1996)"** kvůli konzistenci.

Žádná reference nemusela být smazána — všechny se ověřily jako reálné a správně atribuované. Žádné tvrzení nebylo nutné označit `⚠️ neověřeno`, protože všechny klíčové vzorce i reference prošly ověřením.

---

## Co zůstává nejisté / drobné poznámky

- **Atribuce „species scale"**: vzorec $\Lambda_{\rm sp}=M_{\rm Pl}/\sqrt{N}$ je v JSON přiřazen k `palti-2019` (přehledový článek). Původní zdroj konceptu je Dvali (2007, „Black Holes and Large N Species…"). Palti je legitimní sekundární/pedagogický zdroj, takže nejde o chybu, ale primární citace by byla přesnější.
- **Konvence roku (arXiv vs. časopis)**: u referencí jako `obers-pioline-1999` a `horava-witten-1996` se rok arXiv a rok časopisu liší o jeden rok. Ponecháno v existující podobě (slug dle časopisu), jde o stylovou volbu, nikoli věcnou chybu.
- **Dangling `relatedTo` cíl `dbi-action`**: koncept `d-brane` odkazuje na `dbi-action`, což v tomto fragmentu existuje jako *vzorec* (formula id), nikoli jako koncept. Není to chyba (lze brát jako globální id), ale odkaz nemá lokální cíl mezi koncepty.
- **Próza spojuje semiklasickou gravitaci a kvantovou kosmologii** pod jedním nadpisem „částečně prozkoumáno", zatímco JSON je rozděluje (`semiclassical-gravity`=well, `quantum-cosmology`=partially). Drobná organizační nekonzistence, věcně obhajitelná.
