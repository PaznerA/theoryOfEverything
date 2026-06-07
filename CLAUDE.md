# Konvence projektu Theory of Everything

Tato složka je knowledge base + progress tracker + backoffice pro výzkum kvantové gravitace. Cíl: nashromáždit strukturovaná kontextová data, aby AI mohla hledat dosud nenalezené souvislosti mezi přístupy.

## Jazyková politika (striktní)

- **Próza** (`knowledge-base/`, `verification/`, PROGRESS.md): čeština; anglický originál termínu v závorce při prvním výskytu; přímé citace v původní angličtině.
- **Core data** (`core-data/*.json`, `.bib`): angličtina.
- **Identifikátory, slugy, názvy souborů**: angličtina, kebab-case.

## Datové konvence

- Reference vždy s arXiv ID nebo DOI; **nikdy nevymýšlet arXiv ID** — neověřitelné reference se mažou nebo značí `⚠️ neověřeno`.
- Vzorce v LaTeX (`$$...$$` v markdownu, `latex` pole v JSON).
- ID konceptů jsou globálně smysluplná (`holographic-principle`, ne `concept-1`) — slouží ke křížovému propojení mezi pilíři.
- Každá souvislost mezi přístupy nese `explored: well | partially | barely`. Rating `barely` = primární lovná zóna pro hledání nových spojů.

## Konvence kódu (přenositelnost)

- **Žádné machine-absolutní cesty v kódu** (`/Users/...`, `/home/<user>/...`) v žádném `*.py` pod `core-data/calculations/`, `compute/`, `lib/`, `web/`, `app/tests/` — ani v komentářích/docstringech. Cesty se odvozují `__file__`-relativně (vzor: `os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir, ...))`). Natvrdo zadaná cesta hosta dvakrát rozbila CI (OUTDIR batch + lib-imports batch). Hlídá `app/tests/test_portability_guards.py`.

## Workflow

- Velké rešerše a analýzy se orchestrují přes Workflow tool; skripty se archivují do `workflows/`.
- Po každé dokončené fázi aktualizovat PROGRESS.md (stav, statistiky, další kroky).
- Nové poznatky se zapisují do knowledge base, ne jen do konverzace.
- **Hygiena agentů (přenositelnost):** každému agentovi, který píše/upravuje kód, se předává instrukce odvozovat cesty `__file__`-relativně (nikdy machine-absolutní cesta hosta — viz Konvence kódu).
- **Hygiena agentů (schéma výsledků):** agent, který zapisuje výsledky (results.json apod.), musí zapisovat podle pevného schématu s progresivním/atomickým zápisem, aby přerušení na session-limitu skončilo čistým, validním částečným výstupem (vzor: `compute/drivers/_common.py` — atomický rename + pole `status`).

## Provozní konvence (naučené)

Lekce z incidentů; každá je vynucena testem nebo zapsána v dokumentaci.

- **Přenositelnost cest:** žádné machine-absolutní cesty v portovatelném kódu; `__file__`-relativní bootstrap (viz § Konvence kódu). Hlídá `app/tests/test_portability_guards.py`. Dvakrát rozbilo CI.
- **Driver defaults = plný běh, NE smoke:** holé `python3 driver.py` spadne na plný grid (`--rho` bez hodnoty), `--seeds 4`, `--max-hours 5.5` — tj. těžký produkční běh. Smoke je VŽDY explicitní tiny invokace z `--help` epilogu; default se nepoužívá jako orientační. Varování v `compute/README.md`.
- **Pořadí reprodukce + PYTHONPATH:** některé výpočty čtou výstup jiných (deps dict v `app/tests/test_reproduction.py`); `lib/toe` výpočty potřebují `PYTHONPATH=lib`. Pořadí běhu i PYTHONPATH jsou zakotvené v `test_reproduction.py` a `REVIZE-PRO-CLOVEKA.md §4.3`.
- **Tolerance filozofie (cross-HW):** numerické srovnání má noise floor `1e-10`, core pole `<10 %`, diagnostická pole `<500 %`; patologicky nestabilní sekce vyloučené přes `DIAGNOSTIC_PAT`. Plošná jednotná tolerance falešně „selhává" — viz `test_reproduction.py`.
- **Schéma povinné pro workflow agenty:** agent zapisující výsledky používá pevné schéma + atomický/progresivní zápis (atomický rename + pole `status`), aby přerušení na session-limitu skončilo čistým validním částečným výstupem (vzor `compute/drivers/_common.py`).
