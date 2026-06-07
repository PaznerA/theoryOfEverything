# Nezávislá CAS validace (Wolfram Language) — „cross-HW pro symboliku"

Tato složka je **nezávislá křížová validační dráha** pro exaktní symbolické výsledky
projektu. Stejnou fyziku znovu odvozuje ve Wolfram Language **přímo z publikovaných
koeficientů** (Duff, Vassilevich, Chamseddine–Connes, Beccaria–Tseytlin, Hořava), nikoli
přepisem našich sympy výstupů.

## Proč to existuje

Hlavní výpočetní dráha projektu běží v Pythonu (`sympy`). Reprodukovatelnost na jiném
hardwaru (`reports/2026-06-07-cross-hw.md`) ukázala, že **numerické** výsledky jsou
platformově robustní. U **exaktních symbolických** identit (typicky $-18/11$) ale stejný
software běžící podvakrát není nezávislý důkaz — chyba v transkripci nebo v sympy by se
projevila v obou bězích stejně.

Druhý počítačový algebraický systém (CAS), který tytéž závěry odvodí z **literaturních
hodnot** (ne z našich mezivýsledků), je proto symbolickým ekvivalentem cross-HW
reprodukce:

- **shoda** obou drah = nezávislé potvrzení;
- **neshoda** = chyba v jedné ze dvou odvození (a víme, že je kde hledat).

Vstupní koeficienty jsou do `.wl` skriptů zadány ručně jako **literaturní hodnoty** s
komentářem u každého zdroje; nic se nečte z `core-data/`.

## Co každý skript ověřuje a proti jakým zdrojům

### `a4_identity.wl` — identita $-18/11$ (draft-02)

- per-field $(a,c)$ centrální náboje: skalár $(1/360,\,1/120)$, Weyl $(11/720,\,1/40)$,
  vektor $(31/180,\,1/10)$ — **Duff arXiv:2003.02688, Table 1**;
- `cOverMinusA` jednoho Weylova fermionu $= -18/11$ **přesně** (Rational aritmetika);
  Dirac $= 2\times$ Weyl má tentýž poměr;
- tří-cestná konzistence: spektrální akce $\alpha_0/\tau_0$ (**Chamseddine–Connes
  hep-th/9606001, eq. 2.24**) $=$ single-Weyl $c/(-a)$ $=$ Dirac $c/(-a)$; $f_0$ a $\pi$ se
  v poměru pokrátí (`FreeQ`);
- obsahová nezávislost: SM fermiony $45$ (bez $\nu_R$) i $48$ (s $\nu_R$) dávají $-18/11$;
  plný SM identitu láme ($-1698/1991$);
- konformní (Weylův) graviton $c/(-a) = -398/261$ a $\neq -18/11$ —
  **Beccaria–Tseytlin arXiv:1710.03779, eq. 31**; cross-lock přes CHS vzorec
  $a_s = \nu^2(14\nu+3)/720$ (vektor $s{=}1$, graviton $s{=}2$);
- $\mathrm{STr}(1) = n_B - n_F = -62$ (bez $\nu_R$) / $-68$ (s $\nu_R$) z SM multipletu.

### `ds_classifier.wl` — master hodnoty $d_s$ (draft-03)

- izotropní $d_s^{\rm UV} = D/\gamma$ a Hořava $d_s = 1 + D_{\rm space}/z$;
- konvence (draft-03 §5.1): $D$ = **prostoročasová** dimenze $= 4$; izotropní řádky
  používají $D{=}4$, Hořavovy řádky $D_{\rm space} = D-1 = 3$ (**Hořava arXiv:0902.3657**,
  $3{+}1$);
- exaktní racionální záznamy: GR $4$; Stelle $2$; asymptotická bezpečnost ($\eta_*{=}{-}2$)
  $2$; CST d'Alembertian $2$; multifrakcionální $2$; **Hořava $z{=}2 \to 5/2$**, **$z{=}3
  \to 2$**, IR $z{=}1 \to 4$; headline $D_{\rm space}{=}3, z{=}3 \to 2$.

### `lambda_ledger.wl` — Λ-indukční účetnictví (VYPOCET-17)

Formální symbolová aritmetika ($f_0,f_2,f_4,N,\hat k,\hat g,\Lambda$):

- $a_0$ i $a_2$ jsou **lineární v** $N = \mathrm{Tr}(1_F)$;
- poměr $a_0:a_2$ nese $(f_4/f_2)\,\Lambda^2$ — rozměrový a schématicky (cutoff-tvar)
  závislý: `! FreeQ` od $f_4, f_2, \Lambda$;
- intra-$a_4$ poměr ($-18/11$) je cutoff-řádově čistý: `FreeQ` od $f_0$ i $\Lambda$
  (to je ta index-chráněná identita);
- $\Lambda_{cc}/m_{Pl}^2 = \pi^2 f_4/(2 N f_2^2 \hat k^2)$ nese **explicitní** $1/N$ →
  žádná druhá identita pro kosmologickou konstantu;
- $\mathrm{STr}(1) = -62 / -68$, kvartická divergence se neruší.

Každý skript exportuje `*_result.json` (každý check jako `True/False` + exaktní racionály
jako řetězce).

## Instalace a spuštění

`wolframscript` (zdarma dostupný Wolfram Engine) na běžném CI stroji **není**
nainstalován — skripty se proto píší s maximální syntaktickou opatrností a validace se
spouští až po jednorázové instalaci:

```bash
# 1) instalace Wolfram Engine (macOS)
brew install --cask wolfram-engine

# 2) JEDNORÁZOVÁ interaktivní aktivace (vyžaduje bezplatné Wolfram ID).
#    Doporučeno spustit přímo v této session jako shell příkaz:
#        ! wolframscript -activate
#    (aktivace je interaktivní — zeptá se na Wolfram ID a heslo)

# 3) spuštění nezávislé CAS validace
python3 verification/cas/run_all.py
```

`run_all.py` se dá spustit z libovolného adresáře (cesty jsou `__file__`-relativní).
Návratové kódy:

| kód | význam |
|-----|--------|
| `0` | všechny skripty proběhly a každý `overall_pass` je `True` |
| `1` | `wolframscript` běžel, ale aspoň jeden check / skript selhal |
| `2` | `wolframscript` není nainstalován — nic se nevalidovalo (čistý skip) |

Souhrn se zapíše do `verification/cas/results.json` s celkovým `overall_pass`.

## Vazba na pytest

`app/tests/test_cas_validation.py`:

- **vždy běžící** guardy (bez Wolframu): existence `.wl` skriptů a runneru + kontrola, že
  neobsahují stroj-absolutní cesty;
- **Wolfram-podmíněné** testy (`@pytest.mark.skipif`, když chybí `wolframscript`):
  spustí `run_all.py`, ověří celkový pass a headline check $-18/11 = $ `True`.

Na stroji bez Wolframu testy korektně **skipnou** (guardy proběhnou):

```bash
# z kořene repozitáře:
MPLBACKEND=Agg python3 -m pytest app/tests/test_cas_validation.py -v
```

## Vazba na REVIZE-PRO-CLOVEKA

V `papers/REVIZE-PRO-CLOVEKA.md`, sekce draft-02, je přidán checkbox „nezávislá CAS
validace připravena — spustit po instalaci Wolfram Engine". Po aktivaci Wolframu a
úspěšném běhu `run_all.py` lze checkbox odškrtnout jako splněnou nezávislou re-derivaci
exaktní aritmetiky.
