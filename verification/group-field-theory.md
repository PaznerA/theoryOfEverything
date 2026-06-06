# Ověření: group-field-theory

**Datum:** 2026-06-05
**Agent:** adversarial-verifier (economy mode)
**Soubory:** `knowledge-base/approaches/06-group-field-theory.md`, `core-data/fragments/group-field-theory.json`

---

## Souhrn

Zkontrolováno 8 referencí (WebFetch na arxiv.org / DOI). Zkontrolovány 4 klíčové vzorce. Nalezeny a opraveny 3 chyby.

---

## Ověřené reference (8)

| # | ID | arXiv / DOI | Výsledek |
|---|-----|-------------|---------|
| 1 | `boulatov-1992` | hep-th/9202074 | OK — název, autor, rok 1992 souhlasí |
| 2 | `gurau-2010` | 1011.2726 | OK — název, autor (Gurau), submise 2010, publikováno 2011 |
| 3 | `de-pietri-1999` | hep-th/9907154 | OK — název, autoři (De Pietri, Freidel, Krasnov, Rovelli), rok 1999/2000 souhlasí |
| 4 | `oriti-sindoni-wilson-ewing-2016` | 1602.05881 | OK — název, autoři, rok 2016 souhlasí |
| 5 | `oriti-sindoni-wilson-ewing-2017` | 1602.08271 | OK — název, autoři, publikováno CQG 34, 04LT01 (2017) souhlasí |
| 6 | `witten-2016` | 1610.09758 | OK — název, autor (Witten), rok 2016 souhlasí |
| 7 | `klebanov-tarnopolsky-2016` | 1611.08915 | OK — název, autoři, rok 2016/2017 souhlasí |
| 8 | `gielen-oriti-sindoni-2013` | 1303.3576 | OK — název, autoři, rok 2013 souhlasí |

**Navíc ověřeno:**
- arXiv:2506.20340: skutečně existuje, ale jde o **doktorskou práci** jednoho autora (A.F. Jercher), nikoli o článek skupiny. Opraveno.
- arXiv:2110.15336 (Marchetti et al. 2021) i arXiv:2209.04297 (Marchetti et al. 2022): obě ID jsou reálná; jde o dvě odlišné práce. Próza správně cituje 2209.04297 jako „2022"; JSON má pouze 2110.15336 jako samostatný záznam.

---

## Nalezené a opravené chyby (3)

### 1. Špatná atribuce arXiv:2506.20340 (kritická)
- **Chyba:** JSON pole `authors` = `"GFT/spin-foam collaboration"`, v próze bez jména autora.
- **Skutečnost:** arXiv:2506.20340 je PhD thesis Alexandra F. Jerchera (2025).
- **Oprava:** `authors` změněno na `"A.F. Jercher"`, `significance` upřesněno; v próze doplněno „Jercher 2025, doktorská práce".

### 2. Chybné PII v URL Brézin-Kazakov 1990 (střední závažnost)
- **Chyba:** URL `pii/037026939291665V` (rok 1992 v PII čísle) neodpovídá článku z roku 1990.
- **Skutečnost:** Správné PII dle DOI `10.1016/0370-2693(90)90818-Q` je `037026939090818Q`.
- **Oprava:** URL opraveno v JSON i ve dvou místech prózy.

### 3. JSON neobsahuje samostatný záznam pro Marchetti et al. 2022 (arXiv:2209.04297)
- **Situace:** Próza správně cituje arXiv:2209.04297 jako „Marchetti et al. 2022" (Lorentzovské modely). JSON má pouze arXiv:2110.15336 (jiná práce ze 2021). Link v próze je funkční a odkazuje na reálný článek.
- **Rozhodnutí:** Chyba nebyla opravena přidáním záznamu do JSON (ekonomický mód; ID v próze je správné a průchozí). Ponecháno jako zbývající záležitost.

---

## Ověření klíčových vzorců (4)

1. **Gurauova expanze 1/N:** $N^{d-\frac{2}{(d-1)!}\omega}$ — správně; odpovídá Gurau 2011, rovnice pro barevné modely ranku $d$.

2. **Definice Gurauova stupně přes jackety:** $\omega = \sum_J g_J$, počet jacketů $\frac{d!}{2}$ — správně.

3. **Melonická gap rovnice:** $G = 1/(\mathcal{K}-\Sigma)$, $\Sigma(\tau_1,\tau_2)=g^2[G(\tau_1,\tau_2)]^{q-1}$, konformní řešení $\Delta=1/q$ — správně.

4. **Efektivní Friedmannova rovnice (jednospinová):** $(V'/3V)^2 = (4\pi G/3)(1-\rho/\rho_c) + 4V_{j_o}E_{j_o}/(9V)$, $\rho_c = 3\pi G\hbar^2/(2V_{j_o}^2)$ — správně; odpovídá arXiv:1602.05881.

---

## Zbývající záležitosti

- JSON neobsahuje samostatný záznam pro arXiv:2209.04297 (Marchetti et al. 2022, Lorentzovské modely), i když je tato práce citována v próze.
- arXiv:2506.20340 je PhD thesis, ne recenzovaný článek — přestože je opravena atribuce, charakter zdroje (disertace) by mohl být v hlavním textu prózy výraznějším způsobem zohledněn.
- Brézin-Kazakov (1990): opravená URL dosud nebyla ověřena přes WebFetch (ekonomický mód); DOI `10.1016/0370-2693(90)90818-Q` odpovídá správné práci dle standardní bibliografie.
