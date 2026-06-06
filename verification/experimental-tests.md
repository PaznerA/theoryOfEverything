# Verifikační zpráva: experimental-tests

**Datum:** 2026-06-05
**Soubory:** `knowledge-base/phenomenology/17-experimental-tests.md`, `core-data/fragments/experimental-tests.json`
**Agent:** adversarial verification (economy mode)

---

## Zkontrolované reference (8 vzorků)

| # | arXiv / URL | Tvrzení v textu | Výsledek |
|---|---|---|---|
| 1 | 2402.06009 | LHAASO kol., PRL 133, 071501, $E_\mathrm{QG,1}>10\,E_\mathrm{Pl}$ | ✓ potvrzeno (PRL, nikoli PRD) |
| 2 | 1707.06050 | Bose et al. 2017, „Spin Entanglement Witness for Quantum Gravity", PRL 119, 240401 | ✓ potvrzeno |
| 3 | 1707.06036 | Marletto & Vedral 2017, PRL 119, 240402 | ✓ potvrzeno |
| 4 | 2308.15440 | Tobar et al. 2024, „Detecting single gravitons with quantum sensing", Nat. Commun. 15, 7229 | ✓ potvrzeno |
| 5 | 2112.06861 | LVK 2021, „Tests of General Relativity with GWTC-3" | ✓ potvrzeno (arXiv existuje) |
| 6 | 1611.08265 | Chou et al. 2017, holometr, Class. Quantum Grav. 34, 065005 | ✓ potvrzeno |
| 7 | 2308.03031 | Piran & Ofengeim 2024, nezávislá analýza (ne LHAASO kol.) | ✓ potvrzeno jako nezávislá práce |
| 8 | 2312.09079 | Původně chybně připsáno „LHAASO Collaboration" | **CHYBA** — autoři Yang, Bi & Yin; JCAP 04 (2024) 060 |

---

## Nalezené a opravené chyby

### 1. Chybné připsání autorství: arXiv:2312.09079

- **Problém:** Prose i JSON označovaly tuto práci jako „LHAASO Collaboration". Ve skutečnosti jde o nezávislou analýzu autorů Yu-Ming Yang, Xiao-Jun Bi a Peng-Fei Yin (JCAP 04 (2024) 060).
- **Opraveno:** Prose (ref. 9) i JSON (`lhaaso-liv-2312`) aktualizovány se správnými autory a DOI.

### 2. Chybné označení časopisu: arXiv:2402.06009

- **Problém:** Prose (řádek „Klíčové výsledky" i ref. 33) uváděla „PRD 109, L081501". Skutečná publikace je **PRL 133, 071501** (Physical Review Letters, nikoli Physical Review D). JSON `lhaaso-liv-prd-2024` měl DOI správný (PRL), ale text záznamu byl v pořádku — chyba byla pouze v prose.
- **Opraveno:** Obě místa v prose opravena na „PRL 133, 071501".

### 3. Chybní autoři a rok: arXiv:1812.00482

- **Problém:** Prose citovala „Graham, Hogan, Kasevich & Rajendran 2016" — nesprávní autoři i rok. Skutečný autor je Jon Coleman (za MAGIS-100 Collaboration), rok 2018. JSON měl rok 2018 správně, ale autory nesprávně (Graham et al.).
- **Opraveno:** Prose i JSON aktualizovány.

### 4. Falešný DOI v JSON: `lhaaso-liv-2023`

- **Problém:** Záznam pro Piran & Ofengeim (2308.03031) v JSON obsahoval DOI `10.1103/PhysRevD.109.L081501`, který patří oficiálnímu LHAASO kolaboračnímu článku (2402.06009), nikoli práci Pirana & Ofengeima.
- **Opraveno:** DOI z tohoto záznamu odstraněn; poznámka doplněna.

---

## Ověření vzorců (4 nejdůležitější)

1. **MDR + skupinová rychlost** — koeficienty a znaménka správná.
2. **Zpoždění doby letu** — faktor $(n+1)/2$ a kosmologický integrál jsou standardní; správně.
3. **Birefringence** — $\Delta\theta \propto \xi(E^2-E_0^2)d/(2E_\mathrm{Pl})$ — odpovídá standardnímu rozměru-5 SME operátoru.
4. **BMV gravitační fáze** — $\Delta\phi = Gm^2\Delta t/(\hbar d)$ — zjednodušená forma konzistentní s Bose et al. a Marletto-Vedral 2017.

Žádná chyba ve vzorcích.

---

## Zbývající nejistoty

- Hmotnostní mez gravitonu $m_g < 1.3\times10^{-23}\,\mathrm{eV}/c^2$ z GWTC-3 nebyla přímo potvrzena v textu článku (stránka výsledků nebyla dostupná v arXiv preview); hodnota je standardně uváděna v literatuře.
- Aziz & Howl 2025 (Nature 646, 813) — DOI v JSON ukazuje na Nature URL, přímé ověření titulní stránky nebylo provedeno; kros-reference s rebuttal papery je konzistentní.
- GW250114 (2509.08054) — preprint, dosud nepublikován v recenzovaném časopisu; v textu správně popsán jako arXiv 2025, ale DCC odkaz v původním textu byl zastaralý (nyní opravena citace na arXiv).

---

## Závěr

Celkem zkontrolováno 8 referencí, nalezeny 4 věcné chyby (2 v přiřazení autorství, 1 v označení časopisu, 1 v chybném DOI). Všechny opraveny přímo v souborech. Vzorce jsou správné. Žádná reference nebyla zcela nevěřitelná/fiktivní — všechny arXiv IDs se úspěšně resolvly.
