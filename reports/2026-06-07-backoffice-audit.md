# Backoffice audit — připravenost na další den výzkumu

> Datum: 2026-06-07. Rozsah: 4 paralelní auditní oblasti (deliverables
> `qg-knowledge-foundation` + archiv workflow skriptů; datová pipeline
> fragmenty → `consolidate.py` → registry; infrastruktura testy/`lib/toe`/compute
> drivery/CI/docker/web; přenositelnost a trvalé zakotvení provozních lekcí).
> Auditní agenti: 4. Opravy aplikované rovnou: 5 (viz § Zakódovaná poučení).

## (a) Executive summary — je backoffice připravená na další den?

**Verdikt: ANO, backoffice je připravená na další výzkumný den.** Žádný
blocker, žádná ztráta dat, žádný regres testů. Pipeline je konzistentní
(registry bajtově identické s regenerací přes `consolidate.py` — žádný drift),
všech 308+ testů zelených, všechny deliverables `qg-knowledge-foundation`
přítomné a validní, žádná závislost dalšího dne nežije pouze v `/tmp`.

**Top rizika (žádné není blokující, dvě jsou „major" v redakčním smyslu):**

1. **Coverage frontier ([major]):** Nejnovější nálezy **F-024 až F-028**
   (kola 9–12) nemají reprezentaci ve fragmentech ani v `connections.json`. Graf
   konceptů se přegeneruje z fragmentů, takže registr tyto výsledky nevidí.
   Konkrétně spojení `causal-sets → black-holes-information` je v grafu stále
   formulováno jako otevřený „PRIORITY HUNTING TARGET (H5g-2)" a předpovídá
   faktor `1/4`, ačkoli **F-028 už tuto otázku zodpověděl** (naměřeno
   `c ≈ 7.57 ≠ 4`: slabá H5g-2 potvrzena, silná vyvrácena). **Riziko:** příští
   den může „lovit" v zóně `barely`, která je už vyřešená. Vyžaduje redakční
   rozhodnutí o znění a `explored`-ratingu, proto neopraveno automaticky.
2. **Rozbité odkazy v `00-INDEX.md` ([major]):** 19 z 24 odkazů na VYPOCET
   writeupy míří na neexistující názvy souborů (např. INDEX uvádí
   `VYPOCET-02-a4-anomaly-matching.md`, soubor je `VYPOCET-02-a4-matching.md`).
   Funkční jsou jen odkazy na VYPOCET-01, -11, -21, -22, -23, -24. Navíc INDEX
   odkazuje na neexistující datové cesty `core-data/calculations/VYPOCET-NN/`
   (skutečné adresáře jsou pojmenované sémanticky). Kosmetické pro výzkum, ale
   ruší navigaci pro člověka.
3. **UX past „default = plný běh" ([major], opraveno dokumentačně):** Spuštění
   compute driveru bez argumentů NENÍ smoke, ale několikahodinový produkční běh
   (plný grid, `--seeds 4`, `--max-hours 5.5`). Riziko nechtěného dlouhého běhu.
   **Opraveno:** varování přidáno do `compute/README.md` a zakódováno do
   CLAUDE.md jako trvalá konvence.

Nejvyšší okamžitá hodnota pro příští den: **propsat F-026/F-027/F-028 do
fragmentů a přegenerovat registry**, aby lovná zóna grafu odpovídala realitě, a
**opravit odkazy v `00-INDEX.md`**. Obojí je redakční, ne urgentní.

## (b) Tabulka nálezů podle oblasti a závažnosti

| Oblast | Závažnost | Nález | Stav |
|---|---|---|---|
| Datová pipeline | major | F-024..F-028 (kola 9–12) bez reprezentace ve fragmentech/`connections.json`; `causal-sets→black-holes-information` stále „barely / H5g-2 target", ač F-028 odpověděl (c≈7.57≠1/4) | **Doporučení** (redakční — propsat + `consolidate.py`) |
| Datová pipeline | major | 19/24 odkazů na VYPOCET writeupy v `00-INDEX.md` rozbitých; navíc neexistující `core-data/calculations/VYPOCET-NN/` | **Doporučení** (oprava cílů na skutečné názvy souborů) |
| Infrastruktura | major | `repro.yml:109-115` obsoletní special-case: exit-5 ↦ „skipped"; komentář tvrdí, že 4 adresáře nejsou v SLOW_CALCS — už jsou. Mrtvý kód maskuje budoucí regresi (test by tiše „skipped" místo fail) | **Doporučení** (zrušit větev nebo exit 5 překlasifikovat na FAIL) |
| Infrastruktura | major | UX past: holé `python3 driver.py` = plný ~5,5 h běh, ne smoke; epilogy ukazují jen smoke příklady, varování chybělo | **Opraveno dokumentačně** (`compute/README.md`, CLAUDE.md) |
| Přenositelnost | major | Lekce (a) absolutní cesty neměla dopředné pravidlo v trvalém dokumentu | **Opraveno** (CLAUDE.md § Konvence kódu) |
| Přenositelnost | major | Lekce (b) „driver defaults = smoke" nikde nezapsaná (a reálně opačná — default = plný běh) | **Opraveno** (compute/README.md + CLAUDE.md) |
| Přenositelnost | major | Lekce (e) hygiena workflow-agentů (cesty `__file__`-relativně; schéma s čistým failem na limitu) nezapsaná | **Opraveno** (CLAUDE.md § Workflow + § Provozní konvence) |
| Přenositelnost | minor | 5 výskytů machine-absolutní cesty v komentářích/docstringech guarded `*.py` | **Opraveno** (5 souborů přepsáno na repo-relativní znění) |
| Přenositelnost | minor | `workflows/consolidate.py:15` hardkóduje `ROOT` (mimo scope guard testu) | **Doporučení** (sjednotit na `__file__`-relativní jako sourozenec `repro-runner.py`) |
| qg-knowledge-foundation | minor | `verification/von-neumann-algebras.md` chybí — pilíř 19 přidán v kole 3 mimo původní scope, adversariální verify neproběhl | **Doporučení** (jednorázový verify agent logikou `verifyPrompt`) |
| qg-knowledge-foundation | minor | 7 pilíř-md souborů těsně pod 350-řádkovým minimem šablony (hustší formátování, všechny sekce přítomné) | **Doporučení** (info; rozšířit při příštím průchodu) |
| Datová pipeline | minor | `00-INDEX.md:110,122` zastaralé počty: „18 fragmentů" (reálně 19), „22 výpočtů" (reálně 24) — PROGRESS.md má správně | **Doporučení** (textová oprava, formálně mimo zadání) |
| qg-knowledge-foundation | info | Absolutní cesty `/Users/pazny/...` unikly do 3 verify zpráv, `novelty-checks.json`, 1 VYPOCET writeupu (kosmetické) | **Doporučení** (přechod na relativní cesty v nových skriptech) |
| qg-knowledge-foundation | info | Verify zprávy `semiclassical-gravity.md` a `swampland.md` nejmenší ze setu (48 řádků), ale věcně splňují `verifyPrompt` | **Žádná akce** |
| ds_cap_4d | info | dense-bound kanál přeskakuje buňky nad `--n-max` místo fallbacku — poctivě dokumentováno v docstringu + implementaci (`path='skipped'`) | **Žádná akce** |

Aplikováno rovnou: **5 oprav** (CLAUDE.md ×2 sekce, compute/README.md ×1, 5
guarded `*.py` komentářů, nový guard test). Doporučení k redakčnímu schválení:
**8** (2× major datová pipeline, 1× major CI, zbytek minor/info).

## (c) Stav deliverables qg-knowledge-foundation (odpověď na původní otázku)

**Co NEchybělo (vše ověřeno):**

- Všech **18 pilíř-md** souborů přítomno (approaches 01–10, cross-cutting 11–14,
  foundations 15–16, phenomenology 17–18), každý se všemi **9 povinnými
  sekcemi** (Přehled, Klíčové koncepty, Matematický rámec, Klíčové výsledky,
  Současný stav, Otevřené problémy, Vztahy, Mapa konceptů, Reference).
- Všech **18 fragmentů** `core-data/fragments/*.json` přítomno a validní JSON
  (+ 19. `von-neumann-algebras.json` z kola 3, mimo původní scope). Všechny
  splňují minima: ≥15 konceptů, ≥10 vzorců, ≥25 referencí, ≥6 problémů,
  ≥8 propojení.
- Všechny **4 hlavní registry** validní: `concept-graph.json` (625 uzlů /
  2476 hran), `references.json` (587), `formulas.json` (247),
  `open-problems.json` (153); `connections.json` (292 hran, 115 barely).
- `references.bib`, `SYNTEZA.md`, `00-INDEX.md` přítomny.
- Všech **18 verifikačních zpráv** pro původní pilíře přítomno (5 pilířů
  FAILED_FIRST_RUN re-verifikováno).
- Všechny **workflow skripty archivovány** — 21 z 21 v `workflows/`, žádný
  nechybí.

**Co skutečně chybělo / je gap:**

- **`verification/von-neumann-algebras.md` chybí [minor].** Pilíř 19 prošel
  výzkumem a konsolidací (`qg-round-03-paper.js`), ale workflow neobsahoval krok
  `verifyPrompt` pro VNA — adversariální verifikace citací a vzorců pro tento
  jediný pilíř neproběhla. Pilíř 19 přitom **nebyl součástí scope**
  `qg-knowledge-foundation`, takže formálně to není mezera v původním zadání;
  je to nedodělek z následného kola 3. Doporučení: spustit jednorázový verify
  agent stejnou logikou jako `verifyPrompt(PILLARS[18])`.
- **7 pilíř-md těsně pod 350-řádkovým minimem šablony [minor]:**
  `02-loop-quantum-gravity.md` (298), `09-emergent-gravity.md` (293),
  `01-string-theory.md` (331), `06-group-field-theory.md` (349),
  `11-holography-adscft.md` (325), `12-black-holes-information.md` (348),
  `13-entanglement-spacetime.md` (327). Žádná sekce nechybí — jde o hustší
  formátování (34–68 kB), ne o vynechaný obsah.

**Shrnutí:** původní scope `qg-knowledge-foundation` je **kompletní**. Jediný
reálný deliverable-gap je chybějící VNA verify zpráva (následný pilíř 19), což
je minor a snadno doplnitelné.

## (d) Zakódovaná poučení vs. zbývající

**Zakódováno trvale v tomto auditu (guard testy + dokumentace):**

- **Lekce (a) absolutní cesty → CLAUDE.md § Konvence kódu (přenositelnost).**
  Zákaz machine-absolutních cest v `*.py` pod `core-data/calculations/`,
  `compute/`, `lib/`, `web/`, `app/tests/`; vzor `__file__`-relativního
  odvození. Vynucuje `app/tests/test_portability_guards.py` (3 passed, < 5 s).
- **Lekce (b) driver defaults → `compute/README.md` blockquote + CLAUDE.md.**
  Explicitní varování, že holé `python3 driver.py` je TĚŽKÝ produkční běh, ne
  smoke; smoke je vždy explicitní tiny invokace z `--help` epilogu.
- **Lekce (e) hygiena workflow-agentů → CLAUDE.md § Workflow + § Provozní
  konvence.** Agenti píšící kód dostávají `__file__`-relativní instrukce; agenti
  zapisující výsledky používají pevné schéma s atomickým/progresivním zápisem
  (vzor `_common.py` — atomický rename + pole `status`).
- **5 mechanických oprav komentářů/docstringů** v 5 guarded `*.py` souborech +
  nový guard test (3 testy) — guarded scope je nyní CLEAN.
- **Lekce (c) run-order + PYTHONPATH** a **(d) tolerance filozofie** byly
  **už dříve trvale zakotvené** v `test_reproduction.py` (deps dict,
  `PYTHONPATH=lib`; noise floor 1e-10, core <10 %, diagnostics <500 %,
  `DIAGNOSTIC_PAT`) a v `REVIZE-PRO-CLOVEKA.md §4.3` — ověřeno, žádná akce.

**Zbývá (doporučení, neopraveno automaticky):**

- Propsat F-026/F-027/F-028 do fragmentů + přegenerovat registry (redakční).
- Opravit 19 rozbitých odkazů + neexistující datové cesty v `00-INDEX.md`.
- Aktualizovat počty v `00-INDEX.md` (18→19 fragmentů, 22→24 výpočtů).
- Uklidit `repro.yml:109-115` (mrtvá exit-5 větev / překlasifikovat na FAIL).
- Sjednotit `workflows/consolidate.py:15` na `__file__`-relativní `ROOT`.
- Doplnit `verification/von-neumann-algebras.md` jednorázovým verify agentem.

## (e) Doporučený checklist pro start dalšího výzkumného dne

1. **Sanity:** `MPLBACKEND=Agg python3 -m pytest app/tests -q` — očekávej
   ~311 passed / 18 skipped / 1 xfailed (zelené). Skip = SLOW_CALCS pod
   `FULL_REPRO`, záměrné.
2. **Staleness:** pokud byly editovány fragmenty, spusť `consolidate.py` a ověř,
   že registry odpovídají (žádný ruční edit registrů — generují se).
3. **Coverage frontier (priorita):** než „lovit" v zóně `barely`, propsat
   výsledky F-024..F-028 do fragmentů (`causal-sets`, `von-neumann-algebras`,
   `semiclassical-gravity`); zvlášť `causal-sets → black-holes-information`
   přeformulovat z „conjecture/barely/H5g-2 target" na výsledek (c≈7.57≠1/4),
   poté přegenerovat registry.
4. **Navigace:** opravit rozbité odkazy a počty v `00-INDEX.md` (po manuálním
   ověření mapování VYPOCET ↔ writeup ↔ calc-dir).
5. **Compute drivery:** NIKDY nespouštět driver bez argumentů (= plný ~5,5 h
   běh). Smoke = explicitní tiny invokace z `--help` epilogu; škálované běhy přes
   `compute.yml` (manuální trigger) nebo s explicitními `--rho/--seeds/--max-hours`.
6. **Po doběhnutí škálovaných běhů** (`ds_cap_4d`, `ds4d_saturation`,
   `ds_entropy_cap_2d`): stáhnout artefakty → vyhodnotit → VYPOCET-25+ →
   findings.json → fragmenty → registry → web.
7. **Web:** po jakékoli změně md/JSON spustit `python3 web/build.py`
   (~106 stránek, exit 0).
8. **Přenositelnost:** žádné machine-absolutní cesty v novém kódu; cesty
   `__file__`-relativně; guard test musí zůstat zelený.

## Co bylo ověřeno čistě (výběr)

- **Staleness CHECK:** regenerace všech 19 fragmentů + `consolidate.py` do
  izolovaného adresáře → všech 7 artefaktů (5 JSON registrů + `.bib` +
  `_digest.md`) i 2 `_review` soubory **bajtově identické** s commitnutými.
  Žádný drift, registry přegenerovány po editacích fragmentů.
- **Evidence:** všech 28 nálezů F-001..F-028 má všechny evidence-cesty na disku
  (0 chybějících). Mapování výpočet ↔ writeup je dokonalé **1:1** (24 calc
  adresářů ↔ 24 writeupů, žádné sirotky).
- **Fragmenty ↔ pilíř-md:** dokonalá **1:1** korespondence (19/19).
- **Tests:** 308 passed / 18 skipped / 1 xfailed; `lib/toe` v0.3.0 konzistentní
  napříč `__init__.py`/ARCHITECTURE.md/README; layer import-restriction PASS;
  CONTRACT compliance ověřen reálným smoke během (`status='complete'`, atomický
  `os.replace`). Docker `compose config -q` PASS. Web build: 106 stránek, 79
  plot assetů, exit 0.
- **`/tmp` inventura:** žádná závislost dalšího dne nežije pouze v `/tmp`; vše
  potřebné committnuto v `workflows/review-prep/`.
</content>
</invoke>
