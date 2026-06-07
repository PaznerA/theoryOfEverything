# compute/ — škálované výpočetní běhy

Tato složka obsahuje výpočetní drivery pro **škálované fyzikální výpočty**, které jsou o řády výš nad lokálními `calc.py` skripty ve `core-data/calculations/`. Drivery slouží dvěma účelům:

1. **Škálování** — rozšiřují parametrické rozsahy (hustota ρ, velikost záplaty ℓ, počet seedů) tam, kde lokální běhy narazily na stěnu paměti nebo výpočetního času.
2. **Cross-HW verifikace** — GitHub Actions spouštějí stejný kód na `linux/x86_64`, výsledky se porovnávají s lokálním `macOS/arm64` pomocí tolerance-based srovnání (ne bit-identita, ale shoda v rámci strojové přesnosti).

---

## Architektura

```
compute/
  drivers/
    _common.py          # sdílená infrastruktura (argparse, checkpointing, fingerprint)
    ds_entropy_cap_2d.py
    ds4d_saturation.py
    ds_cap_4d.py
  results/              # výstupní adresář (lokálně); .gitignore ignoruje velké soubory
```

Každý driver je tenký orchestrátor nad knihovnou `toe` v0.3.0; veškerá fyzika žije v `lib/toe`, drivery řeší jen parametrické smyčky, checkpointing a time-budget.

---

## Tři drivery

| Driver | Co počítá | Klíčové parametry | Vazba na nálezy / otázky |
|---|---|---|---|
| `ds_entropy_cap_2d.py` | Zpřesnění konstanty R_full = S_full_cap / A_mol pro 2D dS statickou záplatu přes 100× rozsah hustoty (ρ až 3×10⁴) a 3,5× rozsah záplaty (ℓ až 2,5) | `--rho`, `--patch-l`, `--seeds` (def. 4), `--max-hours` (def. 5,5) | F-028: kvantitativní area-zákon dS, c ≈ 7,57; H5g-2 (slabá verze POTVRZENA); vstup pro `ds_cap_4d` |
| `ds4d_saturation.py` | F-025 dokončení: 4D dS saturace truncované entropie přes ŘÍDKOU cestu (N až ~2×10⁴), srovnání dS vs. plochá kontrola (II₁ vs. II_∞ diskriminátor) | `--rho`, `--n-max` (strop n_max = 2N^{3/4}), `--seeds`, `--max-hours` | F-025: H5g-1 PARCIÁLNÍ (saturace nedosažena při N ≤ 2500); tento driver zvedá hustotní stěnu o řád |
| `ds_cap_4d.py` | **Otevřená otázka**: je koeficient c ≈ 7,57 dimenzně závislý? Měří R_full^{4D} = S_full_cap / A_mol^{4D} v rámci VYPOCET-23 cap-ratio protokolu zvednutého do 4D | `--rho`, `--patch-l`, `--seeds`, `--max-hours` | Navazuje na F-028 (2D) a F-025 (4D parciální); výsledek porovná c^{4D} s c^{2D} ≈ 7,57 |

### Smoke invokace (lokálně, z kořene repozitáře)

```bash
# ds_entropy_cap_2d — smoke (rho=240, l=1.0, 2 seedy, 0.05 h budget)
python3 compute/drivers/ds_entropy_cap_2d.py --rho 240 --patch-l 1.0 --seeds 2 --max-hours 0.05

# ds4d_saturation — smoke (rho=60, 2 seedy, 0.1 h budget)
python3 compute/drivers/ds4d_saturation.py --rho 60 --seeds 2 --max-hours 0.1

# ds_cap_4d — smoke (rho=30, l=0.8, 2 seedy, 0.05 h budget)
python3 compute/drivers/ds_cap_4d.py --rho 30 --patch-l 0.8 --seeds 2 --max-hours 0.05
```

Každý driver má `--help` s popisem parametrů a příklady smoke invokací v epilogu.

> **Pozor na defaulty.** Spuštění driveru BEZ argumentů NENÍ smoke — `--rho` bez hodnoty spadne na plný grid, `--seeds` má default 4 a `--max-hours` default 5,5 h, takže výchozí běh je TĚŽKÝ produkční běh. Smoke je vždy explicitní tiny invokace z `--help` epilogu (`SMOKE (< 30 s)`), nikdy ne holé `python3 driver.py`. Plný cílový běh i smoke se proto VŽDY spouští s explicitními argumenty; default se nepoužívá jako orientační.

---

## Checkpointing a time-budget chování

Drivery sdílejí infrastrukturu z `_common.py`:

- **Progresivní checkpointing**: `results.json` se přepisuje atomicky (temp soubor + `rename`) po každé dokončené buňce výpočtů (kombinaci parametrů a seedu). Přerušený běh → zachována veškerá hotová práce.
- **Time-budget** (`--max-hours`, výchozí 5,5 h): po vypršení budgetu driver dokončí aktuální buňku, zapíše `"status": "partial-time-budget"` a ukončí se s exit kódem 0. Plně dokončený běh zapíše `"status": "complete"`.
- **Host fingerprint**: každý `results.json` obsahuje blok `host` s `platform`, `machine`, `python`, `numpy`, `scipy`, `toe` — klíčové pro cross-HW srovnání.
- **Deterministické seedy**: výsledky jsou reprodukovatelné pro stejné parametry na stejném HW; cross-HW srovnání tolerance-based (rel. odchylka fyzikálních výsledků).
- **iDelta ±-párování**: každá buňka zaznamenává `pairing_residual_rel_max` — invariant ověřující správnost Pauli-Jordanova operátoru (ne fudgováno).

---

## Kam padají výsledky

### Lokálně

```
compute/results/<driver-name>--<param-slug>--<runstamp>/
    results.json     # kompletní výsledky + metadata
```

Výchozí výstupní adresář je `compute/results/`; lze přepsat přes `--out`.

### GitHub Actions (artefakty)

Workflow `compute.yml` (`.github/workflows/compute.yml`) spouští drivery manuálně přes `workflow_dispatch`. Po dokončení (nebo po time-budget exitu) nahraje `compute/results/**` jako artefakt `<driver>-run` s dobou uchovávání 90 dní. Stažení artefaktu:

```bash
gh run download <run-id> -n <driver>-run -D /tmp/gh-compute/
```

---

## Jak po stažení začlenit výsledky

1. **Porovnat s commitnutými výsledky**: klíčová čísla z lokálního `core-data/calculations/<dir>/results.json` (např. R_full, c, S_trunc exponent) srovnat s odpovídajícími buňkami v staženém `results.json`. Použít skript `workflows/review-prep/repro-runner.py` (funkce `compare()`), která vypočítá max. rel. odchylku.

2. **Validace tolerance**: cross-HW shoda se nepožaduje bit-identická, ale rel. odchylka fyzikálních veličin (R_full, entropické stropy, exponenty) by měla být pod ~1 % (float64 drivery) nebo ~1e-4 (float32 drivery). Větší odchylka = signál k prošetření (jiné numerické knihovny, precision, seedy).

3. **Nový zápis VYPOCET**: pokud driver rozšíří parametrický rozsah nad commitnuté výsledky a klíčová fyzika se potvrdí nebo zamítne hypotézu, zapsat nový `knowledge-base/vypocty/VYPOCET-XX.md` s:
   - odkazem na driver + parametry + run-id artefaktu,
   - poctivým CAVEAT blokem (co platí, co je aproximace),
   - verdiktem (POTVRZENA / VYVRÁCENA / PARCIÁLNÍ),
   - aktualizací `core-data/findings.json` (nový nebo aktualizovaný nález F-XXX).

4. **Aktualizovat PROGRESS.md**: přidat log entry + aktualizovat stav hypotéz H5g-1 (F-025) a H5g-2 (F-028) a otevřenou otázku c^{4D} vs. c^{2D}.

---

## Otevřené otázky (cíle driverů)

| ID | Otázka | Driver | Stav |
|---|---|---|---|
| F-025 / H5g-1 | Saturuje 4D dS truncovaná SSEE (II₁ vs II_∞)? | `ds4d_saturation` | PARCIÁLNÍ — N ≤ 2500 nestačí |
| F-028 / H5g-2 | Je R_full = S_full_cap / A_mol skutečně ρ-invariantní přes 100× hustotní rozsah? | `ds_entropy_cap_2d` | 2D POTVRZENA do ρ ≤ 1200; rozšíření čeká |
| otevřená | Je c ≈ 7,57 dimenzně závislý? c^{4D} vs. c^{2D} | `ds_cap_4d` | NOVÉ — žádná předchozí data |
