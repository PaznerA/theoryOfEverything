# Verifikační zpráva: emergent-gravity

**Datum:** 2026-06-05
**Soubory:** `knowledge-base/approaches/09-emergent-gravity.md`, `core-data/fragments/emergent-gravity.json`
**Agent:** adversariální verifikátor (economy mode)

---

## Postup

Zkontrolováno 8 referencí (WebFetch arxiv.org/DOI), 4 klíčové vzorce, platnost JSON.

---

## Výsledky ověření referencí

| # | ID | arXiv/DOI | Stav |
|---|----|-----------|------|
| 1 | jacobson-1995 | gr-qc/9504004 | ✓ ID, název, autor, rok odpovídá |
| 2 | verlinde-2010 | 1001.0785 | ✓ ID, název, autor odpovídá; rok publikace v JSON je 2011 (správně — arXiv 2010, JHEP 2011) |
| 3 | verlinde-2016 | 1611.02269 | ✓ ID, název, autor, rok (SciPost 2017) odpovídá |
| 4 | jacobson-2015 | 1505.04753 | ✓ ID, název, autor; rok PRL publikace 2016 správně |
| 5 | steinhauer-2016 | 1510.00621 | ✓ ID, název (Nat. Phys. 12, 959, 2016) odpovídá |
| 6 | munoz-de-nova-2019 | 1809.00913 | **OPRAVENO** — skutečný název: „…at the Hawking temperature…", nikoli „…and its temperature…" |
| 7 | padmanabhan-cosmin-2013 | 1302.3226 | ✓ ID, autoři (H. Padmanabhan & T. Padmanabhan), rok odpovídá |
| 8 | bianconi-2025 | 2408.14391 | ✓ ID, název, autor, PRD 111, 066001 (2025) odpovídá |

### Zjištěná a opravená chyba autorů

- **Schmöle et al. (TU Wien)** — vynalezené autorství. Skutečný seznam autorů článku PRR 3, 033065 (arXiv:2012.10626): A. J. Schimmoller, G. McCaul, H. Abele, D. I. Bondar. Opraveno v `.md` i `.json`.

### Volovik 2024

- Citace v `.md` (ref. 27) nese poznámku „přesný arXiv ID neověřen." Titul a obsah lze ověřit přes ResearchGate (publication 380515346), ale přesné arXiv číslo se nepodařilo jednoznačně potvrdit. Stav: ⚠️ neověřeno — arXiv ID chybí.

---

## Ověření vzorců

| Vzorec | Výsledek |
|--------|----------|
| Jacobsonova Clausiova relace: η = k_B c^3/(4Gℏ) | ✓ Standardní Bekenstein–Hawkingova hustota entropie |
| Verlindeho M_D: koeficient a_0/6 | ✓ Potvrzeno z Hodson–Zhao (1612.06282), Eq. 6 odpovídá |
| Padmanabhanovo N_bulk = 2|ρ+3p|V/(k_B T) | ✓ Komarova energie → správný koeficient 2 |
| G = 1/(4ℏη) identifikace | ✓ Logicky konzistentní s η |

---

## Provedené opravy

1. **`.md` řádek 134:** `Schmöle et al. 2021` → `Schimmoller et al. 2021`; odkaz opraven na `arxiv.org/abs/2012.10626`.
2. **`.md` ref. 22:** název Muñoz de Nova opraven na „…at the Hawking temperature…".
3. **`.md` ref. 29:** autoři opraveni na `A. J. Schimmoller, G. McCaul, H. Abele, D. I. Bondar`; odkaz přesměrován na arXiv.
4. **`.json` `munoz-de-nova-2019`.title:** opraven název.
5. **`.json` `schmole-2021`.authors a .title:** opraveny na skutečné hodnoty.

---

## Zbývající obavy

- Volovik 2024 (ref. 27 v `.md`): arXiv ID dosud neověřeno; poznámka v textu zachována.
- Padmanabhanův CosMIn vzorec Lambda*L_P^2 ≈ 3.4e-122 je prezentován jako kvantitativní výstup, ale postulát N = 4π není odvozen — text to přiznává, není třeba opravovat.
- JSON neobsahuje referenci na Volovik 2024 (nenalezeno v `references`), takže chybějící arXiv ID nenarušuje strukturu JSON.
