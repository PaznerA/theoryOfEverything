# Velká konsolidace po druhém oblouku (2026-06-09, kolo 21)

> Konsolidační report uzavírající druhý výzkumný oblouk (kola 13–20, nálezy F-029…F-039). Vstupem byly tři nezávislé auditní fasety — A (registry/integrita), B (drafty), C (graf/dokumentace/verifikace). Tento dokument shrnuje konsolidovaný stav projektu, integritní verdikt po fasetách, automaticky aplikované opravy a punch-list zbylých položek pro lidského revizora.

## 1. Stav projektu

Projekt je po druhém oblouku ve fázi **konsolidace/dokumentace**, ne další těžké 4D numeriky. Konkrétní stav:

- **39 nálezů** (`findings.json`, F-001…F-039, kontinuální, 0 duplicit, 39 distinct). Všech 104 evidence-cest existuje na disku. Status↔`results.json` verdikty konzistentní napříč druhým obloukem.
- **5 draftů + 1 negative-results letter.** draft-01 (SJ rotující prostoročasy, v0.3), draft-02 (−18/11 fermionová identita, v0.2), draft-03 (d_s klasifikátor, v0.2), draft-04 (typ-přechod kauzální množiny + dS §4.3, v0.2), draft-06 (limity diskrétního programu / „mapa negativů", v0.1). Všechny nesou DRAFT banner „internal research draft, NOT submitted, requires human review". Drafty jsou navzájem konzistentní; žádný neupgraduje status nad `findings.json`.
- **Dvojí verifikace.** (a) **CAS dráha** (`verification/cas/`): 175/175 symbolických checků přes 7 Wolfram Language skriptů; formula-coverage 24 verified + 14 already_validated = 38 vzorců; **Myrheim-Meyer RESOLVED** (jmenovatel 4→2 ve fragmentu + consolidate, `resolved_blocker`). (b) **Numerická reprodukce** (`test_reproduction.py`): druhý oblouk 10/11 PASS, `ds-amol-convention` vědomě vyloučen (čte staged archiv mimo /tmp sandbox) + dokumentován. Žádný second-arc calc nepokryt OBĚMA dráhami.
- **Agent framework.** Tři výzkumní agenti na `main` (exploratory-engine + computational-physicist + adversarial-verifier); každý výpočet prošel adversariálním auditem. Agenti zapisují podle pevného schématu (atomický/progresivní zápis, pole `status`) a odvozují cesty `__file__`-relativně (portability guardy zelené).
- **Graf konceptů.** `connections.json` 298 hran (**114 barely / 115 partially / 69 well**); `concept-graph.json` 626 uzlů / 2487 hran (index v souladu). Hrany generovány z fragmentů přes `workflows/consolidate.py` (žádné ruční editace generovaných registrů).
- **SYNTEZA chain.** SYNTEZA-01/02/03 zapsány; SYNTEZA-03 (po kolech 7–20) konsoliduje druhý oblouk: tři „zdi" (4D area-zákon genuinně nepřítomný — F-031/F-037/F-038; surogátní Dirac = struktura ne teplota/metrika — F-033/F-036; diskrétní koeficient geometrický ne anomální — F-039) + draft-06 „mapa negativů".
- **Testy:** 356 passed, 29 skipped, 1 xfailed (plná `app/tests` quick suite po konsolidaci, bez regrese).

## 2. Integritní verdikt po fasetách

| Faseta | Rozsah | Verdikt | Jádro |
|--------|--------|---------|-------|
| **A — registry/integrita** | staleness regen, findings, mapping calc↔writeup, lib primitiva | **CLEAN** | Izolovaný regen v /tmp byl 7/7 byte-identický s committed; 39 findings kontinuálních, 104/104 evidence existuje; 35 calc dirs ↔ 36 writeupů (3 dirs nesou 2 writeupy) bez sirotků; 5/5 lib primitiv + 15 testů PASS. Drobnosti: 1× API-nekonzistence (kms/unruh re-export), 1× stale docstring. |
| **B — drafty** | 5 draftů + REVIZE, banner, F-ID konzistence | **issues-found** | Drafty navzájem konzistentní; bannery CLEAN. Jádro: REVIZE zaostává za draft-06 a druhým obloukem (F-036/037/038 chyběly, F-034 nikde); drobné ref-integrity stopy v BRAINSTORM-05/draft-01. |
| **C — graf/dokumentace/verifikace** | connections/graph, link-check, CAS+numerika, PROGRESS/INDEX | **DRIFT** | Stale F-033 korelace 0.098/0.0095 přežívala v 8 lokacích (ground truth + statement už opraveny na 0.319); F-033 si vnitřně protiřečil; PROGRESS/INDEX bannery popisovaly neaktuální stav (Myrheim-Meyer „BLOCKER", počty výpočtů/vzorců); 3 rozbité interní odkazy. |

## 3. Automaticky aplikované opravy (12 souborů)

Všechny `autoApplicable=true` položky aplikovány; graf/hrany výhradně přes pipeline fragment → `consolidate.py` (žádná ruční editace generovaných registrů).

### Stale F-033 korelace 0.098 → 0.319 (faseta C, Major/Minor)
1. **`core-data/fragments/causal-sets.json`** (zdroj hrany idx 61): „Pearson 0.10, R^2=0.0095" → „Pearson 0.319, R^2=0.10, 16 párů, malý vzorek; kolo-21 reprodukční oprava — committed 0.098/0.0095 byl artefakt timing-truncace, verdikt no-match nezměněn".
2. **`consolidate.py` spuštěn** → přegenerovány `connections.json` (idx 61) + `concept-graph.json` (uzel hrany). Diff je **přesně 1 řádek v každém** registru, žádný jiný drift; ostatních 5 artefaktů (references/formulas/open-problems/.bib/_digest) byte-identických.
3. **`core-data/findings.json` F-033** — sjednocena pole `implications` + `noveltyStatus` na 0.319/R²=0.10/16 párů (statement byl už opraven); vnitřní rozpor odstraněn.
4. **Prose**: `00-INDEX.md` ř.142, `VYPOCET-29` ř.106, `BRAINSTORM-05` ř.220, `BRAINSTORM-06` ř.9+31, `SYNTEZA-03` ř.41 (0.32 zaokrouhleně v bridge-větě).

### INDEX drift (faseta C, Minor)
5. **3 rozbité interní odkazy** v `00-INDEX.md`: `H04-ssee-entropy-cluster.md` → `H04-entropy-cluster-reframe.md`; `ESEJ-03.md` → `ESEJ-03-gravitace-jako-stin.md`; `ESEJ-04.md` → `ESEJ-04-vstup-pozorovatele.md`.
6. **Stale počty**: „Třicet jedna výpočtů" → „Třicet šest" (VYPOCET-01..36 / 35 calc dirs); banner+coverage „37 vzorců / 1 mismatch BLOCKER myrheim-meyer" → „38 vzorců (24 verified + 14 already_validated) / Myrheim-Meyer RESOLVED"; hlavička aktualizována na kolo 21.
7. **2 chybějící index položky**: `BRAINSTORM-06.md` (sekce Klíčové dokumenty) + `reports/2026-06-09-numerical-coverage.md` (reviewové reporty, s křížovým odkazem na CAS revizi).

### Registry/API (faseta A, Minor)
8. **`lib/toe/__init__.py`** — doplněn re-export `kms_temperature, KMSFit, unruh_proper_law, UnruhLawFit` do import bloku i `__all__`; všechna 4 primitiva `spectraltriple` jsou nyní top-level importovatelná konzistentně. Ověřeno (`import toe`; 4× True/True), testy 13 PASS.

### Drafty / REVIZE (faseta B, Major/Minor)
9. **`REVIZE-PRO-CLOVEKA.md`** — rozšířen aktualizační banner o pokrytí F-024..**F-039**: F-036 (`informovany-negativ-tautologie`), F-037 (`supported`), F-038 (`refuted-direction`), F-039 (`confirmed`/no-match-geometric) s verbatim statusy a odkazy na VYPOCET-32..35 / SYNTEZA-03; explicitní poznámka, že **F-034 je předchůdce konsolidovaný do F-036** (vědomé superseder, ne opomenutí); zmínka opravy F-033 0.098→0.319.
10. **`BRAINSTORM-05.md`** — ref-integrity: ř.371 „Dafermos–Luk" → „Häfner & Klein, Unruh na subextremálním Kerru" (oprava z 2026-06-08, ID **zůstává neověřené**); ř.370 doplněna atribuce „Fröb" u 2501.09669 (stále **potvrdit existenci**).
11. **`papers/draft-01-.../draft.md` §5 References** — doplněna stejná hlavičková poznámka jako draft-04/06 („arXiv IDs; to be verified against arXiv by a human before any release") + ⚠️ caveat na nová 2025–2026 ID. **Žádné ID nevymyšleno; žádné označeno jako ověřené.**

Testy po všech opravách: **356 passed, 29 skipped, 1 xfailed** (bez regrese).

## 4. Punch-list pro lidského revizora (zbylé NE-auto položky)

Tyto vyžadují lidský úsudek / strukturální přepis a NEBYLY aplikovány automaticky:

1. **[B, Major — strukturální] REVIZE je stále čtyř-draftový dokument.** Nadpis §1 „Přehledová tabulka čtyř draftů"; §2 má jen §2.1–§2.4 (chybí §2.5 draft-06 s lidským checklistem); §3 pořadí jmenuje 4 drafty; §4.1/§4.2/§4.3 explicitně „čtyři drafty" a reprodukční příkazy nepokrývají žádný výpočet draftu-06. *Auto-banner už pokrytí F-036..F-039 + draft-06 propsal, ale plný přepis „čtyři → pět" + nové §2.5 + §4.3 příkazy (modular-dirac / spectral-triple / ds-amol / amol-variance / conformal-coupling) zůstávají na člověku.*
2. **[A, Minor — stale docstring] `lib/toe/spectraltriple.py` úvodní docstring** říká „The two units are:" a jmenuje jen `dirac_from_kernel` + `connes_distance`; modul má od druhého oblouku 4 funkce. Doplnit přehled o `kms_temperature` (KMS inverzní teplota modulárního toku) a `unruh_proper_law` (Unruhův teplotní zákon diagonály vs. proper distance). *Samotné funkce jsou plně zdokumentované; mezera je jen v přehledu na začátku modulu.*
3. **[C, Major — judgment] Nový top-banner PROGRESS.md kola 21.** Aplikováno (viz §5 níže), ale formulace konsolidovaného stavu / roadmapy je redakční rozhodnutí — člověk nechť potvrdí znění.
4. **[C, Minor — judgment] Duplicitní/zbytkové barely páry v `connections.json`.** von-neumann↔causal-sets má barely i partially; causal-sets↔black-holes-information má barely + 2× partially; causal-sets↔NCG 2× barely. Možná legitimní směrované hrany, možná artefakt — ověřit, zda deduplikovat (nafukuje rating-count 114 barely) nebo ponechat. Není blocker.
5. **[B, Minor — redakční] draft-04/draft-06 venue rozhodnutí** (standalone letter vs. appendix) a konvenční ref ID (CHM/Solodukhin/BW/Unruh/Gibbons-Hawking) — flagged v draftech, k ověření člověkem.

**Absolutní pravidla pro release (z REVIZE) nadále platí:** jmenovaný lidský autor, AI-assistance statement, veřejný calc.py, re-run pipeline, ověření všech arXiv ID proti arxiv.org. Nikdy nevymýšlet arXiv ID.

## 5. Závěr

Druhý oblouk je konsolidovaný: 39 nálezů s dvojí verifikací (CAS + numerika), 5 draftů + negativ-letter, graf 298 hran, SYNTEZA-03 jako uzavírací syntéza. **Integritní souhrn: A CLEAN, B issues-found (REVIZE strukturálně zaostává — auto-banner zacelil propagaci, plný přepis na člověku), C DRIFT zaceleny** (stale F-033, INDEX/PROGRESS bannery, rozbité odkazy). Repo je čistý, registry v souladu s fragmenty (regen ověřen), testy zelené.

**Roadmapa:** konsolidace HOTOVA → **compute režim** (těžké škálované běhy na GH Actions, případné rozhodnutí 4D conformal propagator) → **velké review** lidským revizorem podle REVIZE-PRO-CLOVEKA.md (po doplnění §2.5/§4.3 draft-06).
