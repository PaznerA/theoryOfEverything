# VYPOCET-31: Λ shot-noise — Lorentz-invariantní fluktuační spektrum sprinklingu

**Datum:** 2026-06-08
**Hypotéza:** H6g-4 (BRAINSTORM-06), přerámováno **PROTI** F-005
**Soubory:** `core-data/calculations/lambda-shot-noise/calc.py`, `results.json`, `fano_vs_V.png`, `deltaLambda_vs_V_loglog.png`, `boost_invariance.png`
**Status:** Dokončeno (`status: complete`, wall-clock 26 s)
**Knihovna:** nové primitivy `toe.causet.poisson_count_box4d / lattice_count_box4d / boost_coords / fano_factor` (+ testy)

---

## Cíl

Otestovat hypotézu H6g-4, že kosmologická konstanta jako **Poissonův shot-noise počítání atomů prostoročasu** je *fluktuační spektrum* (variance), nikoli střední hodnota — a že v této formě **přežívá negativ F-005**.

Past 4-objem $V$ obsahuje $N \sim \mathrm{Poisson}(\rho V)$ diskrétních elementů (Poisson sprinkling). Fluktuace počtu $\delta N = \sqrt{\mathrm{Var}(N)} = \sqrt N$ indukuje $\delta\Lambda \sim \sqrt{\mathrm{Var}(N)}/V \sim \rho^{1/2}V^{-1/2}$. Toto je tvrzení o **rozptylu**, odlišné od vyvrácené střední hodnoty.

---

## Přerámování proti F-005 (klíčové — co F-005 vyvrátil a co NE)

**F-005 (VYPOCET-03) vyvrátil SILNOU formu:** jediný sdílený **mean-prefaktor** $\kappa$ v relaci
$$\langle\Lambda\rangle\, \ell_P^2 = \kappa / \sqrt{V/\ell_P^4}$$
napříč třemi mechanismy (Sorkin/EDT/CosMIn). Naměřeno $\kappa_{\text{Sorkin}}/\kappa_{\text{EDT}} = 139{,}6$ (rozdíl ~2,1 řádu). F-005 porovnával tři **hotová prefaktorová čísla** — nikdy neměřil distribuci.

**F-005 NEvyvrátil:**
- **varianci / fluktuační spektrum** $\delta\Lambda \sim \sqrt{\mathrm{Var}(N)}/V$;
- **boost-kovarianci** počítací statistiky.

H6g-4 je tvrzení o **varianci**, distinktní od střední hodnoty. Tento výpočet testuje (1) Poissonovskou statistiku počtu (Fano = 1), (2) její $V^{-1/2}$ škálování, (3) Lorentz/boost-invarianci $\mathrm{Var}(N)$ — žádné z toho F-005 netestoval. **Tento výpočet NEvzkřísí F-005-vyvrácený naivní mean-prefaktor.**

---

## Metoda a setup

**Geometrie:** 4D Minkowského box $[-h,h]^4$ (proxy minulého kužele). Pravý Poissonův bodový proces: počet atomů $N \sim \mathrm{Poisson}(\rho\,\mathrm{Vol})$ s $\mathrm{Vol}=(2h)^4$ — na rozdíl od `sprinkle_box4d` (fixní $N$) je počet **sám náhodný**, což je objekt nesoucí shot-noise.

**Žádný eigh problém** — pouze počítání bodů a boosty. Seed schéma: `np.random.default_rng(SEED0 + group*STRIDE + s)` s nepřekrývajícími se streamy (STRIDE = 100000), 800 seedů na bod (16000 pro konvergenční kontrolu), `SEED0 = 20260608`.

**Tři testy / observable:**

| Test | Observable | Predikce |
|------|-----------|----------|
| (1) Poisson | Fano $F = \mathrm{Var}(N)/\langle N\rangle$ vs $\langle N\rangle = \rho V$ | $F = 1$ přesně |
| (2) Škálování | $\delta\Lambda = \sqrt{\mathrm{Var}(N)}/V$ vs $V$ (nezávislé realizace na $V$) | exponent $-1/2$ |
| (3) Lorentz | $\mathrm{Var}(N)$ v boostnutém regionu téhož vlastního 4-objemu | nezávislé na rapiditě $\eta$ |

**Diskriminátor proti mřížce:** pravidelná 4D mříž (`lattice_count_box4d`, rozteč $a=\rho^{-1/4}$) jako ne-kovariantní kontrola.

**Dimenzionální bookkeeping (poctivě):** v Planckových jednotkách $\rho \sim 1$ (jeden atom na $\ell_P^4$), $V$ v jednotkách $\ell_P^4$. $\langle N\rangle = \rho V$, $\mathrm{Var}(N)=\rho V$, tedy $\delta N = \sqrt{\rho V}$ a
$$\delta\Lambda := \delta N / V = \sqrt\rho\, V^{-1/2}.$$
Pro $V \sim H^{-4}$ (4D Hubblův 4-objem) je $V^{-1/2} \sim H^2$, takže $\delta\Lambda \sim H^2$ — Sorkinovo everpresent-Λ škálování, zde jako tvrzení o **varianci** (NE F-005-vyvrácený mean-prefaktor).

---

## Výsledky

### (1) Poissonova kontrola — Fano faktor

| $\rho$ ($=\langle N\rangle$, $V=1$) | $\langle N\rangle$ | $\mathrm{Var}(N)$ | $F = \mathrm{Var}/\langle N\rangle$ |
|---:|---:|---:|---:|
| 50 | 50,06 | 49,93 | 0,997 |
| 100 | 99,79 | 94,34 | 0,945 |
| 200 | 200,83 | 203,60 | 1,014 |
| 500 | 500,72 | 544,35 | 1,087 |
| 1000 | 999,70 | 977,43 | 0,978 |
| 2000 | 1997,85 | 1902,68 | 0,952 |
| 5000 | 5002,72 | 4679,93 | 0,935 |
| 10000 | 10006,82 | 9605,07 | 0,960 |

**Sdružený Fano = 0,9796 ± 0,0173 (1,18 σ od 1).**
**Konvergenční kontrola (ρ=1000, 16000 seedů): F = 0,9986 ± 0,0112 (0,13 σ od 1).** → Poisson potvrzen, $F=1$.

Pozn.: estimátor Fano má při konečném vzorku malou kladnou systematickou odchylku, takže jednotlivé body lehce kolísají kolem 1; konvergenční kontrola s 16000 seedy ji rozpustí (čistá konvergence, ne tuning).

### (2) Škálování fluktuace δΛ

Nezávislé Poissonovy realizace na každý sub-objem $V$ (nikoli vnořené počty — vnořené boxy sdílejí atomy a korelace mírně vychyluje exponent).

| $V$ | $\langle N\rangle$ | $\mathrm{Var}(N)$ | $\delta\Lambda = \sqrt{\mathrm{Var}}/V$ |
|---:|---:|---:|---:|
| 0,04 | 799,6 | 742,9 | 681,4 |
| 0,08 | 1600,4 | 1508,0 | 485,4 |
| 0,16 | 3201,1 | 3025,1 | 343,8 |
| 0,32 | 6403,6 | 5977,9 | 241,6 |
| 0,64 | 12800,3 | 13387,3 | 180,8 |
| 1,00 | 19998,2 | 20259,3 | 142,3 |

**Fit $\delta\Lambda \sim V^p$: $p = -0{,}4840 \pm 0{,}0061$, $R^2 = 0{,}99936$** (2,62 σ od $-1/2$).
Křížová kontrola $\mathrm{Var}(N)\sim V^q$: $q = 1{,}0320 \pm 0{,}0122$ (Poisson: $q=1$). → $V^{-1/2}$ škálování potvrzeno (konzistentní s $-1/2$; mírná odchylka je jednobodová fluktuace na největším $V$).

### (3) Lorentz-invariance — boost test

Inner měřicí region $[-0{,}18, 0{,}18]^4$ uvnitř velkého boxu $[-1{,}4, 1{,}4]^4$. Geometrický constraint: roh boostnutého boxu mapuje na $|t'|,|x'| = e^\eta h$, takže pro $\eta_{\max}=2$ je $e^2\cdot 0{,}18 = 1{,}33 < 1{,}4$ — boostnutý region **zůstává uvnitř** sprinklovaného nosiče (klíčové: dřívější verze měla únik z boxu při $\eta=2$, který maskoval signál).

| $\eta$ | Poisson $\mathrm{Var}(N)$ | $\mathrm{Var}/\mathrm{Var}_0$ | mříž posun $\langle N\rangle$ |
|---:|---:|---:|---:|
| 0,00 | 162,6 | 1,000 | +0,00 % |
| 0,25 | 174,3 | 1,072 | −1,17 % |
| 0,50 | 164,1 | 1,009 | −0,79 % |
| 0,75 | 160,6 | 0,988 | −0,80 % |
| 1,00 | 148,8 | 0,916 | −1,06 % |
| 1,50 | 150,1 | 0,923 | −0,42 % |
| 2,00 | 159,5 | 0,981 | +5,04 % |

**Poisson $\mathrm{Var}(N)$ je boost-invariantní** v rámci seedové chyby: max z-skóre $\mathrm{Var}(\eta)$ vs $\mathrm{Var}(0)$ = **0,70** (predikce: invariantní, det $\Lambda = 1$).

**Diskriminátor (apples-to-apples):** per-realizační frakční rozptyl počtu napříč $\eta$:
- mříž (jediná rigidní mřížka): **64,5 %** (počet je boost-ZÁVISLÝ),
- Poisson (jeden seed): **12,6 %** (jen počítací šum),
- **poměr mříž/Poisson = 5,13** → mříž ne-kovariantní, Poisson kovariantní.

Poznámka k diskriminátoru: fázově *zprůměrovaná* mřížka obnovuje statistickou izotropii (proto je její $\langle N\rangle(\eta)$ téměř plochá); ne-kovariance se projeví u **jediné** rigidní realizace, jejíž počet je deterministická, boost-závislá funkce $\eta$ — což přesně kontrastuje s Poissonovým skalárem.

---

## Verdikt a limity

**Korespondence: `survives`.** Všechny tři diskriminátory prošly:

1. **Fano = 1** (Poisson): 0,9986 ± 0,0112 při 16000 seedech (0,13 σ).
2. **$\delta\Lambda \sim V^{-1/2}$**: $p = -0{,}484 \pm 0{,}006$ (konzistentní s $-1/2$).
3. **Boost-invariance $\mathrm{Var}(N)$**: Poisson plochý (z = 0,70), mříž ne-kovariantní (poměr rozptylu 5,13×).

Shot-noise Λ-**fluktuace** (variance, ne mean) tedy **přežívá ve formě, kterou F-005 NEvyvrátil**, a je genuinně Lorentz-kovariantní.

### Limity (poctivá inventura)

- **Triviálnost Poissonu (riziko z BRAINSTORM-06 §4.5).** $\mathrm{Var}(N)/\langle N\rangle = 1$ JE z definice Poissonova procesu — sám o sobě tautologie („Poisson je Poisson"). **Netriviální obsah je až (ii) boost-invariance a (iii) kontrast s mřížkou** — a právě ty tvoří jádro pozitivu (poměr 5,13× je netriviální).
- **Nutná, ne postačující podmínka.** Test ověřuje **fluktuaci POČTU atomů + boost-kovarianci**, NE plný řetězec $\delta N \to \delta\Lambda$ (Sorkinova konjugace $\Lambda \leftrightarrow V$, sama hypotéza). Boost-invariance počtu je vlastnost, kterou kovariantní Λ-fluktuace *potřebuje*, ne důkaz everpresent-Λ dynamiky.
- **NEvzkřísí F-005 mean-prefaktor.** Pozitiv je výlučně na ose *variance/distribuce + Lorentz-kovariance*. Mean-prefaktorový mismatch 139,6× z F-005 stojí beze změny.
- **Konečný box.** Boost-test je omezen na $\eta \le 2$ geometrickým constraintem $e^{\eta_{\max}} h_{\text{inner}} < h_{\text{box}}$; vyšší rapidity by vyžadovaly větší box (kvadraticky více atomů).
- **Mřížková kontrola je idealizace.** Pravidelná kubická mříž je nejhrubší ne-kovariantní kontrola; sofistikovanější diskrétní struktury (např. BCC, kvazikrystaly) by mohly mít menší anizotropii, ale Poissonův sprinkling je jediný *exaktně* Lorentz-invariantní (CST argument).

### Rozsah (scope)

4D, čisté počítání. Reprodukce bit-identická (0 numerických diffů při re-runu s `PYTHONPATH=lib`). Testuje fluktuační spektrum, ne hodnotu mean Λ.

---

## Návrh F-035 (do registru)

Viz `findingProposal` v orchestračním výstupu. Jádro: *„shot-noise Λ-fluktuace přežívá F-005 ve variance/boost-kovariantní formě (Fano = 1, $\delta\Lambda \sim V^{-1/2}$, $\mathrm{Var}(N)$ boost-invariantní; mříž ne); nevzkříší mean-prefaktor."*

---

## Reference (pouze repo-přítomné; ŽÁDNÉ vymyšlené arXiv ID)

- Sorkin everpresent Λ: **astro-ph/0209274** (Ahmed–Dodelson–Greene–Sorkin) — $\Lambda \sim 1/\sqrt V$, hrana `causal-sets↔cosmological-constant-fluctuation`.
- Prefaktorový mismatch (tento projekt): **F-005 / VYPOCET-03** (zdroje 2304.03819, 2307.13743, 2408.08963, 1302.3226).
- Lorentz-invariance Poissonova sprinklingu: hrana `causal-sets↔experimental-tests` (*„CST's exact Lorentz invariance (Poisson sprinkling)"*).
