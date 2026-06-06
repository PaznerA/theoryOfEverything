# Theory of Everything — výzkumná knowledge base

Tato složka je **knowledge base, progress tracker a backoffice** pro výzkum kvantové gravitace a teorie všeho. Primárním cílem je nashromáždit maximum strukturovaných kontextových dat (citace, reference, vzorce, grafy konceptů, otevřené problémy), aby AI mohla systematicky hledat **dosud nenalezené souvislosti** mezi přístupy ke kvantové gravitaci.

## Jazyková politika

| Typ obsahu | Jazyk |
|---|---|
| Próza, výklad, syntézy (`knowledge-base/`) | **Čeština** (anglické originály termínů v závorce při prvním výskytu; přímé citace v původní angličtině) |
| Core data — JSON registry, vzorce, reference, graf konceptů (`core-data/`) | **Angličtina** |
| Identifikátory, slugy, názvy souborů | **Angličtina** (kebab-case) |

## Struktura

```
theoryOfEverything/
├── README.md                  ← tento soubor
├── PROGRESS.md                ← progress tracker výzkumu
├── CLAUDE.md                  ← konvence pro AI sessions
├── knowledge-base/            ← česká próza, hustá na fakta
│   ├── 00-INDEX.md            ← anotovaný index všeho
│   ├── SYNTEZA.md             ← mapa souvislostí + bílá místa (loviště pro AI)
│   ├── approaches/            ← hlavní přístupy ke kvantové gravitaci (10 pilířů)
│   ├── cross-cutting/         ← průřezová témata (holografie, černé díry, entanglement, swampland)
│   ├── foundations/           ← QFT v zakřiveném prostoročase, konceptuální problémy
│   └── phenomenology/         ← experimentální testy, kvantová kosmologie
├── core-data/                 ← strojově čitelná data (EN)
│   ├── fragments/             ← surové JSON fragmenty z jednotlivých pilířů
│   ├── concept-graph.json     ← sjednocený graf konceptů (uzly + hrany)
│   ├── references.json + .bib ← deduplikovaná bibliografie s arXiv/DOI odkazy
│   ├── formulas.json          ← registr vzorců (LaTeX + význam + zdroj)
│   ├── open-problems.json     ← otevřené problémy, tagované podle pilířů
│   └── connections.json       ← matice mezipřístupových vztahů s ratingem prozkoumanosti
├── verification/              ← verifikační reporty (kontrola citací a vzorců)
└── workflows/                 ← skripty a logy výzkumných workflow
```

## Klíčový princip: rating prozkoumanosti

Každá zaznamenaná souvislost mezi přístupy nese pole `explored: well | partially | barely`.
Souvislosti s ratingem **`barely`** jsou primární lovná zóna — tam AI hledá nové spoje.

## Fáze výzkumu

1. **Základní rešerše** — 18 pilířů kvantové gravitace, hloubková literatura → knowledge base + core data
2. **Hledání souvislostí** — AI analýza grafu konceptů, generování a prověřování hypotéz
3. *(další fáze podle výsledků — viz PROGRESS.md)*
