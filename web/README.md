# `web/` — minimalistický generátor prezentačního webu

Tato složka je **krok 4 roadmapy**: čistě pythonový statický generátor, který
sestaví prezentační web **přímo ze stávající struktury repozitáře**. Markdown
soubory a JSON registry v `core-data/` jsou jediný zdroj pravdy — web je jejich
*pohled* (view), nikdy kopie, která by mohla začít žít vlastním životem.

> Žádný node, žádný JS build chain. Jen `python3` + `markdown` + `jinja2`.
> Matematika se renderuje v prohlížeči přes KaTeX (z CDN), kód je prosté `<pre>`.

## Struktura

```
web/
├── build.py              ← JEDINÝ vstupní bod (CLI; přijímá --out)
├── builder/              ← malé moduly
│   ├── sitemap.py        ← mapování souborů repa na routy (.html), sidebar zdroj
│   ├── mdrender.py       ← markdown → HTML (ochrana matematiky, přepis odkazů)
│   └── data.py           ← živé loadery core-data registrů + galerie výpočtů
├── templates/            ← jinja2 šablony (base + stránky)
├── static/style.css      ← jeden CSS soubor (light/dark přes prefers-color-scheme)
└── dist/                 ← VÝSTUP (maže se a přestavuje při každém běhu)
```

## Jak buildit

```bash
# z kořene repozitáře
python3 web/build.py
```

Výstup jde deterministicky do `web/dist/` (složka se před každým buildem smaže a
přestaví). Vlastní cílová složka:

```bash
python3 web/build.py --out /tmp/muj-web
python3 web/build.py -q        # tiše, bez statistik
```

Běh trvá několik sekund a vypíše počet sestavených stránek (aktuálně ~103:
98 z markdownu + 5 generovaných + zkopírované grafy do `dist/assets/`).

## Jak servírovat

Web používá **jen relativní odkazy**, takže funguje dvěma způsoby:

1. **Přímo z disku** — otevři `web/dist/index.html` v prohlížeči (`file://`).
2. **Přes HTTP server:**

   ```bash
   python3 -m http.server 8080 --directory web/dist
   # → http://localhost:8080
   ```

### V Dockeru

Služba `web` v `app/docker-compose.yml` build i servírování spojuje:

```bash
docker compose build web          # NUTNÝ rebuild image (markdown+jinja2)
docker compose --profile web up web
# → http://localhost:8080
```

Pozn.: volume služby `web` je nyní **zapisovatelný** (bez `:ro`), protože
`build.py` zapisuje do `web/dist/`. Po změně `requirements.txt` je potřeba image
přestavět, aby v něm byly `markdown` a `jinja2`.

## Jak přidat obsah

**Prostě přidej soubor do repozitáře.** Web je view nad strukturou — nic se
neopisuje ručně:

- **Nová stránka prózy** → vytvoř `*.md` v `knowledge-base/**`, `reports/`,
  `verification/` nebo `papers/**`. Při příštím buildu se z ní stane stránka na
  zrcadlové routě (`knowledge-base/foo/bar.md` → `knowledge-base/foo/bar.html`),
  objeví se v sidebaru i v drobečkové navigaci.
- **Nový výpočet** → přidej adresář do `core-data/calculations/<jmeno>/`
  s `results.json` a PNG grafy. Card se vygeneruje sám; pokud nějaký
  `knowledge-base/vypocty/VYPOCET-*.md` odkazuje na
  `core-data/calculations/<jmeno>`, propojí se „→ Výklad“ automaticky.
- **Nový záznam v registrech** → zapiš do `core-data/findings.json`,
  `connections.json`, `formulas.json` nebo `open-problems.json`. Tabulky i čísla
  na dashboardu (domovská stránka) se přepočítají **živě** z těchto JSONů.

### Co build dělá automaticky

- **Ochrana matematiky:** `$...$` a `$$...$$` se před markdownem schovají za
  placeholdery a po renderu vrátí v původním tvaru, takže je KaTeX dostane čisté.
- **Přepis interních odkazů:** odkazy mezi soubory repa (`../core-data/...`,
  `./VYPOCET-...md`) se přepíšou na odpovídající `.html` routy (best-effort);
  externí `http(s)` odkazy zůstávají; arXiv ID se autolinkují na `arxiv.org/abs/`.
- **Banner draftů:** **každá** stránka generovaná z `papers/**` nese výrazný
  červený banner „⚠️ INTERNÍ AI-ASISTOVANÝ DRAFT — …“. Web je lokální
  prezentace, **nikoli publikace.**

## Testy

```bash
cd /Users/pazny/projects/theoryOfEverything
MPLBACKEND=Agg python3 -m pytest app/tests/test_web_build.py -q
```

Testy buildí web do dočasné složky a ověřují: ≥ 80 stránek, existenci klíčových
stránek, banner na všech paper stránkách, rozlositelnost interních odkazů a
shodu počtu findings v HTML s `findings.json`. Běh < 30 s.
