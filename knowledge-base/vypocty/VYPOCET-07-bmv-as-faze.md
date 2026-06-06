# VYPOCET-07 — AS korekce k BMV entanglamentní fázi

> **Stav:** Dokončeno  
> **Datum:** 2026-06-06  
> **Adresář výpočtu:** `core-data/calculations/bmv-as-phase/`  
> **Rodičovská hypotéza:** `knowledge-base/hypotezy/H03-bmv-diskriminator.md`  
> **Cíl skriptu:** kvantifikovat relativní opravu entanglamentní fáze z asymptotické bezpečnosti (AS) a perturbativní EFT pro realistické i agresivní parametry QGEM experimentů

---

## 1. Cíl

Hypotéza H03 navrhuje použít BMV/QGEM experiment nejen jako binární test (kvantová vs. klasická gravitace), ale jako diskriminátor mezi různými přístupy ke kvantové gravitaci. Tento výpočet kvantifikuje, jak velkou relativní opravu δφ/φ k vedoucímu členu entanglamentní fáze

$$\phi_0 = \frac{G_0\,m^2\,t}{\hbar\,d}$$

předpovídají:
1. **Perturbativní EFT** jednosmyčková kvantová korekce (Donoghue 1994; Bjerrum-Bohr, Donoghue, Holstein 2003)
2. **Asymptotická bezpečnost (AS)** — RG-vylepšený Newtonův potenciál (Bonanno & Reuter 2000)
3. **GUP** — deformace komutátorů minimální délkou

Výsledky jsou konfrontovány s dosažitelností v plánovaných experimentech (QGEM 2025) a agresivními budoucími parametry.

---

## 2. Metoda

### 2.1 Bonanno–Reuter RG-vylepšený potenciál

Z neperturbativní renormalizační skupiny pro Einsteinovu gravitaci plyne běžící Newtonova konstanta (nerelativistická limita, cutoff $k = \xi/r$):

$$G_\mathrm{AS}(r) = \frac{G_0\,r^2}{r^2 + \tilde\omega\,G_0/c^3}$$

kde koeficient $\tilde\omega = 118/(15\pi) \approx 2.507$ je fixován porovnáním s jednosmyčkovou EFT. Zdroj: [BR00], potvrzeno v arXiv:2510.06689.

Délková škála AS korekce: $\sqrt{\tilde\omega\,G_0/c^3} \approx 2.49 \times 10^{-18}$ m (sub-Planckovo měřítko).

Modifikovaný dvoutělový potenciál:

$$V_\mathrm{AS}(r) = -\frac{G_\mathrm{AS}(r)\,m^2}{r}$$

Relativní korekce fáze (exaktní):

$$\frac{\delta\phi_\mathrm{AS}}{\phi} = \frac{G_\mathrm{AS}(r)}{G_0} - 1 = -\frac{\tilde\omega\,G_0}{c^3\,r^2 + \tilde\omega\,G_0}$$

Pro $r \gg \sqrt{\tilde\omega\,G_0/c^3}$ (vždy splněno pro $r \gtrsim$ nm):

$$\frac{\delta\phi_\mathrm{AS}}{\phi} \approx -\frac{\tilde\omega\,G_0}{c^3\,r^2}$$

**Klíčová poznámka:** Tato korekce **neobsahuje $\hbar$** — jde o klasický RG efekt, nikoli kvantovou smyčku. Má jiný dimensionální původ než EFT korekce.

### 2.2 EFT jednosmyčková kvantová korekce

Donoghue (1994) a Bjerrum-Bohr, Donoghue, Holstein (2003) odvodili vedoucí neanalytickou kvantovou korekci k Newtonovu potenciálu:

$$V_\mathrm{EFT}(r) = -\frac{G_0 m_1 m_2}{r}\left[1 + \frac{3G_0(m_1+m_2)}{r c^2} + \frac{41}{10\pi}\frac{G_0\hbar}{r^2 c^3}\right]$$

kde druhý člen je klasická PN korekce a třetí je kvantová. Pro rovné hmotnosti $m_1 = m_2 = m$:

$$\frac{\delta\phi_\mathrm{EFT}}{\phi} = \frac{41}{10\pi}\frac{G_0\hbar}{r^2 c^3}$$

Koeficient $41/(10\pi) \approx 1.306$. Tato korekce **obsahuje $\hbar$** — je to skutečný jednosmyčkový kvantový efekt.

### 2.3 GUP korekce

Z deformovaných komutačních relací $[\hat x, \hat p] = i\hbar(1 + \beta \hat p^2)$:

$$\frac{\delta\phi_\mathrm{GUP}}{\phi} \approx \beta\left(\frac{\ell_\mathrm{Pl}}{d}\right)^2\left(\frac{m}{m_\mathrm{Pl}}\right)^2$$

### 2.4 Parametrické sady

| Sada | $m$ [kg] | $d$ [µm] | $t$ [s] | Motivace |
|------|----------|----------|---------|----------|
| QGEM-1s | $10^{-14}$ | 100–450 | 1 | Plánovaný experiment |
| QGEM-10s | $10^{-14}$ | 100–450 | 10 | Prodloužená koherence |
| Agresivní | $10^{-12}$ | 10–100 | 10 | Hypotetická budoucnost |

---

## 3. Vstupy a konstanty

| Konstanta | Hodnota | Zdroj |
|-----------|---------|-------|
| $G_0$ | $6.674 \times 10^{-11}$ m³ kg⁻¹ s⁻² | CODATA |
| $\hbar$ | $1.0546 \times 10^{-34}$ J s | CODATA |
| $c$ | $2.998 \times 10^{8}$ m s⁻¹ | CODATA |
| $m_\mathrm{Pl}$ | $2.176 \times 10^{-8}$ kg | odvozeno |
| $\ell_\mathrm{Pl}$ | $1.616 \times 10^{-35}$ m | odvozeno |
| $\tilde\omega$ | $118/(15\pi) \approx 2.507$ | [BR00], arXiv:2510.06689 |
| $41/(10\pi)$ | $\approx 1.306$ | [BDH03] Phys. Rev. D 67, 084033 |

---

## 4. Výsledky

### 4.1 Vedoucí fáze φ₀

| Parametry | $d$ [µm] | $\phi_0$ [rad] |
|-----------|----------|---------------|
| $m=10^{-14}$ kg, $t=1$ s | 100 | $6.3 \times 10^{-1}$ |
| $m=10^{-14}$ kg, $t=1$ s | 250 | $2.5 \times 10^{-1}$ |
| $m=10^{-14}$ kg, $t=1$ s | 35 | $\sim 1.8 \times 10^{0}$ |
| $m=10^{-12}$ kg, $t=10$ s | 10 | $6.3 \times 10^{5}$ |

Fáze na hranici detekce ($\phi_0 \sim 10^{-3}$ rad) nastává pro $m=10^{-14}$ kg, $d \sim 35$ µm, $t=1$ s.

### 4.2 Relativní korekce δφ/φ

| Model | $d=100$ µm | $d=250$ µm | $d=10$ µm (agr.) |
|-------|------------|------------|-----------------|
| **AS** (bez $\hbar$) | $6.2 \times 10^{-28}$ | $9.9 \times 10^{-29}$ | $6.2 \times 10^{-26}$ |
| **EFT** (s $\hbar$) | $3.4 \times 10^{-62}$ | $5.5 \times 10^{-63}$ | $3.4 \times 10^{-60}$ |
| **GUP** ($\beta=1$) | $5.5 \times 10^{-75}$ | $8.8 \times 10^{-76}$ | $5.5 \times 10^{-69}$ |

### 4.3 Klíčové dimensionální zjištění

AS a EFT korekce mají **různou dimensionální strukturu**:

$$\frac{\delta\phi_\mathrm{AS}}{\phi} = -\frac{\tilde\omega\,G_0}{c^3\,r^2} \qquad \text{(bez } \hbar \text{, klasický RG)}$$

$$\frac{\delta\phi_\mathrm{EFT}}{\phi} = +\frac{41}{10\pi}\frac{G_0\,\hbar}{c^3\,r^2} \qquad \text{(s } \hbar \text{, kvantová smyčka)}$$

Poměr AS/EFT:

$$\frac{|\delta\phi_\mathrm{AS}/\phi|}{|\delta\phi_\mathrm{EFT}/\phi|} = \frac{\tilde\omega}{(41/10\pi)\cdot\hbar} \approx 1.82 \times 10^{34}$$

AS korekce je $1.8 \times 10^{34}$× **větší** než EFT (protože neobsahuje $\hbar \sim 10^{-34}$ J s v jmenovateli). Přesto je AS korekce stále přibližně 25 řádů pod experimentálním dosahem.

### 4.4 Vzdálenost od experimentálního dosahu

| Model | Vzdálenost od dosahu ($10^{-3}$ rel.) při $d=100$ µm |
|-------|------------------------------------------------------|
| AS (bez $\hbar$) | **~25 řádů** |
| EFT (s $\hbar$) | **~59 řádů** |
| GUP ($\beta=1$) | **~72 řádů** |
| GUP ($\beta=10^{34}$, max. AURIGA/LIGO mez) | **~38 řádů** |

---

## 5. Tabulka diskriminátorů

### 5.1 Binární diskriminátory

| Test | Typ | Predikce: detekce GIE | Vyloučen při: | Dostupnost |
|------|-----|----------------------|---------------|------------|
| **B1** Kvantová vs. klasická gravitace | YES/NO entanglement | $\phi_0 \gtrsim 10^{-3}$ rad | Oppenheim (jako výhradní), Verlinde (klasický) | **V dosahu 2030–2035** |
| **B2** Oppenheim post-kv. teorie | Křížové korelace pohybů + nulový entanglement | Alternativní experiment (oscilátor) | — | **Principiálně dostupné** |
| **B3** Verlinde emergentní gravitace | Absence kvantového GIE | — pozitivní GIE detekce | Verlinde (klasický mediátor) | **Částečně v dosahu** |

### 5.2 Kontinuální diskriminátory (tvar fáze)

| Test | Model | $\delta\phi/\phi$ | Potřebná přesnost | Dostupnost |
|------|-------|-------------------|-------------------|------------|
| **C1** EFT jednosmyčka | EFT vs. žádná korekce | $3.4 \times 10^{-62}$ | $3.4 \times 10^{-62}$ | **Nedosažitelné (59 řádů)** |
| **C2** AS běžící G | AS vs. EFT | $6.2 \times 10^{-28}$ | $6.2 \times 10^{-28}$ | **Nedosažitelné (25 řádů)** |
| **C3** GUP ($\beta=1$) | GUP vs. EFT | $5.5 \times 10^{-75}$ | — | **Nedosažitelné (72 řádů)** |

---

## 6. Interpretace

### 6.1 Fyzikální charakter korekcí

Výsledky odhalují důležitý konceptuální rozdíl:

- **EFT korekce** je skutečný jednosmyčkový kvantový efekt — výsledek virtuálních gravitonů. Škáluje jako $\hbar \cdot G_0 / (d^2 c^3) = \ell_\mathrm{Pl}^2 / d^2$, kde $\ell_\mathrm{Pl}$ je Planckova délka. Je to nerozlučitelně spojena s kvantovou povahou gravitace.

- **AS korekce** je klasický neperturbativní RG efekt — vyjadřuje, jak Newtonova konstanta "teče" s energetickou škálou i v semi-klasickém přiblížení. Nemá $\hbar$, škáluje jako $G_0 / (d^2 c^3) \cdot \tilde\omega$. Tato korekce by existovala i v klasické RG teorii.

Paradoxně: AS je typicky prezentována jako "kvantová gravitace" (UV pevný bod), ale její nízkoenergetická korekce k Newtonovu potenciálu je $\hbar$-nezávislá a tedy svou škálou bližší klasické než perturbativně-kvantové korekci.

### 6.2 Rozsah nedosažitelnosti

Pro srovnání: vzdálenost EFT korekce ($10^{-62}$) od experimentálního dosahu ($10^{-3}$) je 59 řádů. Aby bylo dosažitelné v BMV experimentu, bylo by nutno:
- Zkrátit vzdálenost na $d \sim \ell_\mathrm{Pl}$ (nemožné),
- nebo zvýšit sensitivitu entanglamentního svědku o 59 řádů.

Pro AS korekci je to "pouze" 25 řádů — stále daleko za hranicí technologické fantazie tohoto století.

### 6.3 Asymptotická bezpečnost a BMV: co by měření řeklo

Pokud by byl entanglement detekován:
- **Konzistentní s AS**: AS předpovídá Newtonský potenciál v nízkoenerg. limitě — detekce GIE AS nevylučuje ani nepotvrzuje.
- **Konzistentní s EFT**: totéž.
- **Diskriminace AS vs. EFT**: vyžadovala by měření na škálách $r \lesssim 10^{-18}$ m — mimo technologický horizont.

### 6.4 Oppenheimova teorie jako výjimka

Jedinou realisticky dostupnou diskriminací v rámci kontinuálního testu je **Oppenheimova post-kvantová teorie** — ale nikoli přímou měřením δφ/φ. Oppenheim předpovídá:
1. Nulový GIE (binární test — v dosahu QGEM)
2. Charakteristický vzor křížových korelací pohybů dvou oscilátorů ($\pi$-fázový posun při $\omega \sim 100$ Hz) — dostupné v alternativním mechanickém experimentu bez makroskopické superpozice.

Tato dvojice testů (1) + (2) by poskytla silnou diskriminaci EFT vs. Oppenheim.

---

## 7. Limity výpočtu

1. **Identifikace cutoffu**: AS potenciál závisí na volbě $k = \xi/r$; koeficient $\tilde\omega = 118/(15\pi)$ odpovídá standardní volbě [BR00], ale jiné volby $\xi$ by daly jiné hodnoty $\tilde\omega$. Tato nejednoznačnost je inherentní pro RG-vylepšené přístupy.

2. **Dvoutělový problém**: Výpočet používá jednoduchou aproximaci $V(r) = -G(r) m^2 / r$ pro identické hmotnosti. Přesnější výpočet by vyžadoval kvantově-mechanický výpočet rozptylové amplitudy v modifikovaném potenciálu.

3. **GUP odhad**: GUP korekce je řádový odhad, nikoli přesný výpočet pro konkrétní model deformace. Různé GUP modely dávají různé koeficienty.

4. **BMV fáze jako aproximace**: $\phi = G m^2 t / (\hbar d)$ je vedoucí člen pro identické hmotnosti v rovnoběžné konfiguraci. Geometrické faktory (vzájemné orientace, průměrování přes trajektorie superpozice) mění numerický prefaktor.

5. **Experimentální práh**: Hodnota $10^{-3}$ rad jako experimentální dosah je optimistická — reálný threshold závisí na dekoherenčním tempu $\gamma$, počtu opakování a konkrétní geometrii [arXiv:2502.12474].

---

## 8. Závěr

**Binární diskriminátor (kvantová vs. klasická gravitace) je v dosahu experimentů do ~2035.** Detekce GIE by potvrdila kvantovost gravitačního mediátoru a vyloučila Verlindeho emergentní gravitaci v klasické interpretaci.

**Kontinuální diskriminátory (tvar fáze) jsou mimo dosah tohoto století:**
- EFT jednosmyčková korekce: $\delta\phi/\phi \sim 10^{-62}$ při $d = 100$ µm — 59 řádů pod dosažitelností
- AS běžící G korekce: $\delta\phi/\phi \sim 10^{-28}$ při $d = 100$ µm — 25 řádů pod dosažitelností (větší než EFT o $10^{34}$ kvůli absenci $\hbar$, přesto nedosažitelné)
- GUP ($\beta=1$): $\delta\phi/\phi \sim 10^{-75}$ — 72 řádů pod dosažitelností

**Nové fyzikální zjištění z výpočtu:** AS a EFT korekce mají různou dimensionální strukturu — AS neobsahuje $\hbar$ (je to klasický neperturbativní RG efekt), EFT $\hbar$ obsahuje (jednosmyčkový kvantový efekt). Poměr AS/EFT ≈ $1.82 \times 10^{34}$ = $1/\hbar$ v přirozených jednotkách. Přestože je AS korekce o 34 řádů větší než EFT, ani AS diskriminaci neumožňuje.

Hypotéza H03 je potvrzen a zpřesněna: framing "diskriminace mezi kvantovými přístupy" zůstává konceptuálně hodnotný pro budoucí teoretické práce, ale experimentálně relevantní je pouze binární otázka a Oppenheimův alternativní experiment.

---

## Reference

- **[BR00]** Bonanno & Reuter, *Renormalization group improved black hole space-times*, Phys. Rev. D **62**, 043008 (2000); arXiv:hep-th/0002196
- **[Don94]** Donoghue, *Leading quantum correction to the Newtonian potential*, Phys. Rev. Lett. **72**, 2996 (1994); arXiv:gr-qc/9310024
- **[BDH03]** Bjerrum-Bohr, Donoghue & Holstein, *Quantum gravitational corrections to the nonrelativistic scattering potential*, Phys. Rev. D **67**, 084033 (2003); arXiv:hep-th/0211072
- **[QGEM25]** Parameter scanning in QGEM experiment with electromagnetic screening, arXiv:2502.12474 (2025)
- arXiv:2510.06689 — potvrzení $\tilde\omega = 118/(15\pi)$ v Bonanno-Reuter metrice
- arXiv:2212.07913 — výpočet Newtonovy kosmologie s kvantovými korekcemi ($\zeta = -41\pi/10$)
- Bose et al. (2017), arXiv:1707.06050; Marletto & Vedral (2017), arXiv:1707.06036 — BMV návrh
- Oppenheim (2023), Phys. Rev. X **13**, 041040 — post-kvantová teorie klasické gravitace

---

*Výpočet dokončen 2026-06-06. Soubory: `calc.py`, `results.json`, `bmv_as_eft_corrections.png`, `bmv_corrections_wide_loglog.png`, `bmv_phase_vs_d.png`.*
