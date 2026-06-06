# Verifikační zpráva — QFT v zakřiveném prostoročase a semiklasická gravitace

**Datum:** 2026-06-05
**Ověřované soubory:**
- `knowledge-base/foundations/15-semiclassical-gravity.md` (česká próza)
- `core-data/fragments/semiclassical-gravity.json` (anglický JSON fragment)

## Co bylo zkontrolováno

### Platnost JSON
JSON byl od začátku validní; po všech úpravách znovu ověřen (`json.load` proběhne bez chyby). Struktura: 36 konceptů, 14 vzorců, 40 referencí, 8 otevřených problémů, 14 propojení. Všechny `source` ids u vzorců odkazují na existující reference.

### Audit referencí (ověřeno >24 prací přes arXiv/DOI)
Ověřeno přes `WebFetch` na arXiv/DOI/Nature, vždy kontrola: rozliší se ID + souhlasí název, autoři a rok.

Potvrzeno bez problému (výběr nejsilnějších tvrzení):
- Wald 1993 (gr-qc/9307038), Fewster-Kontou 2022 (2108.12668), Bousso et al. 2016 (1506.02669), Ceyhan-Faulkner (1812.04683), Almheiri et al. (1911.12333), Penington et al. (1911.11977), Oppenheim (1811.03116), Trillo-Navascués (2411.02287), Kolb-Long (2312.09042), Meda-Pinamonti-Siemssen (2007.14665), Juárez-Aubry (2509.02051), Ferreiro-Navarro-Salas-Pla (2511.13518), Bose et al. (1707.06050), Marletto-Vedral (1707.06036), Hollands-Wald (1401.2026), Crispino-Higuchi-Matsas (0710.5373), BFV (math-ph/0112041), Moretti (gr-qc/0109048), Sahlmann-Verch (math-ph/0008029), Ford (2112.02444), Bertolini-Casarin (2406.12464), Agullo et al. (0906.5315), Gryb-Palacios-Thébault (1812.07078), Fadel et al. (2305.04780), Cheng et al. (2510.23050), Akhmedov et al. (2307.12831), Ho-Kawai-Shao (2411.01105), Lima-Lima (2511.13392), Aziz-Howl (Nature 2025, 10.1038/s41586-025-09595-7), Kudler-Flam et al. (PRD 111, 105001 / 2312.07646), Parker 1969 (Phys. Rev. 183, 1057).

### Audit vzorců (>5 ověřeno proti autoritativním zdrojům)
- Unruhova teplota `T_U = ħa/2πck_B` a `⟨N⟩=1/(e^{2πω/a}−1)` — správně.
- Hawkingova teplota `T_H = ħκ/2πck_B`, `κ_Schw = c⁴/4G_N M` — správně.
- Stopová anomálie `(4π)²⟨T⟩ = cC² − aE₄ + b□R`, `E₄ = R_{abcd}R^{abcd}−4R_{ab}R^{ab}+R²` — znaménková konvence `−aE₄` odpovídá standardu; správně.
- Waldova entropie `S_W = −2π∮(∂L/∂R_{abcd})ε_{ab}ε_{cd}` — odpovídá přesně originálu (Wald 1993).
- Bogoljubovovo číslo částic `⟨0_in|N̄_j|0_in⟩ = Σ|β_ji|²` a normalizace `Σ(αα*−ββ*)=δ` — standardní konvence (Birrell-Davies); správně.
- Diósi-Penroseův čas `τ ∼ ħ/E_G` s gravitační vlastní energií rozdílu — správně.

## Co bylo špatně a opraveno

1. **Chybné arXiv ID Kontou-Olum (vážné).** JSON i próza citovaly `arXiv:1507.06299` pro práci „Averaged null energy condition and quantum inequalities in curved spacetime" autorů Kontou & Olum. ID 1507.06299 je však **disertace samotné Kontou** (jediný autor). Skutečná společná práce Kontou-Olum dokazující ANEC je **arXiv:1507.00297**, „Proof of the averaged null energy condition in a classical curved spacetime using a null-projected quantum inequality" (Phys. Rev. D 92, 124009). Opraveno ID, název i DOI v JSON; opraven odkaz v próze (řádek u milníku QEI/ANEC).

2. **Chybné arXiv ID Fewster-Smith (vážné, jen v próze).** Próza odkazovala Fewster & Smith přes `arXiv:math-ph/0701012`, což je ovšem zcela nesouvisející práce o Fokker-Planckově rovnici (Shapovalov et al.). Správná práce je **gr-qc/0702056** („Absolute quantum energy inequalities in curved spacetime", 2007/2008). Opraveno.

3. **Špatný rok/údaj Parkerovy disertace.** Próza uváděla „(1965/1968)" pro harvardskou disertaci. Disertace byla obhájena na Harvardu v **1966** (školitel S. Coleman). Opraveno na „1966, školitel S. Coleman"; odkaz na článek přeznačen na „Parker 1969" (publikace Phys. Rev. 183, 1057, 1969).

4. **Název BFV.** JSON i próza měly „...paradigm for local quantum field theory"; správný název je „...paradigm for local quantum **physics**". Opraveno na obou místech.

5. **Doplnění autorů místo „(Various)".** Ověřené reálné autory doplněno do JSON: Trillo-Navascués (2411.02287), Aziz-Howl (Nature 2025), Bertolini-Casarin (2406.12464), Agullo-Navarro-Salas-Olmo-Parker (0906.5315), Gryb-Palacios-Thébault (1812.07078), Kudler-Flam-Leutheusser-Rahman-Satishchandran-Speranza (2312.07646; doplněno i arXiv).

## Audit konzistence
- Próza a JSON se navzájem neprotiřečí (vzorce, teploty, znaménka, definice konceptů shodné).
- `relatedTo` a `connections` odkazují na věrohodné globální ids (cross-pillar slugy jako `black-holes-information`, `holography-adscft`, `page-curve` atd.).
- Hodnocení `explored` je poctivé: dobře prostudovaná rozhraní (`black-holes-information`, `holography-adscft`, `emergent-gravity`, `page-curve`) jsou „well"; tenká rozhraní (`asymptotic-safety`, `loop-quantum-gravity`, `causal-sets`, `noncommutative-geometry`, `supergravity-uv`) jsou „barely". Žádná slavná, dobře prostudovaná dualita není podhodnocena.

## Co zůstává nejisté
- Reference `schrodinger-cat-decoherence-2023` (2305.04780) ponechána s autorem „(Various)"; jde o velkou experimentální kolaboraci a jednoznačný seznam autorů se nepodařilo spolehlivě potvrdit (WebFetch vrátil jen jedno jméno) — radši ponecháno neúplné než chybně přiřazené.
- ID reference `schwartz-conformal-correlators-2024` obsahuje zavádějící řetězec „schwartz", ačkoli autoři jsou Bertolini & Casarin (autory v poli opraveno; samotné `id` ponecháno kvůli možným externím odkazům).
- Plné texty za paywallem (Parker 1969, Nature 2025, některé APS DOI) ověřeny nepřímo přes ADS/INSPIRE/PubMed a vyhledávání, nikoli z primární stránky vydavatele.
- Historické datování Schrödingera/Fullinga/Daviese/Unruha v próze nebylo dohledáno do primárních pramenů; obecně konzistentní s literaturou, ale neověřeno do detailu.
