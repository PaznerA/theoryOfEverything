# Výzkumní agenti (Research Agents)

Tato složka obsahuje **návrhové dokumenty** (design docs) tří specializovaných agentů, kteří asistují při vývoji výzkumné báze kvantové gravitace (Theory of Everything). Funkční definice (volatelné jako subagenti) žijí v [`.claude/agents/`](../../.claude/agents/) — viz § Použití níže.

## Přehled agentů — smyčka *návrh → výpočet → audit*

1. **[Exploratorní motor](exploratory-engine.md) — *Theorizing Mode*** → [`.claude/agents/exploratory-engine.md`](../../.claude/agents/exploratory-engine.md)
   - **Role:** navrhuje spekulativní, ale matematicky ukotvené hypotézy, extrapoluje nálezy k jejich limitům a loví „bílá místa" (connections rated `barely`/`partially` v `connections.json`); ke každé domněnce **navrhuje konkrétní toy-model** pro `lib/toe`.
   - **Použití:** kreativní brainstormy, seedování nové generace `BRAINSTORM-NN`, nové fyzikální modely (relační geometrie, Poissonův šum kosmologické konstanty, observer jako gravitující DoF přes crossed products).

2. **[Výpočetní fyzik](computational-physicist.md) — *Execution Mode*** → [`.claude/agents/computational-physicist.md`](../../.claude/agents/computational-physicist.md)
   - **Role:** převádí návrh testu na **reprodukovatelný výpočet**: `calc.py` + `results.json` (fixní schéma + atomický/progresivní zápis) + grafy, zápis `VYPOCET-NN`, návrh `F-NNN`, a — pokud se to skládá — novou funkci v `lib/toe`. Vynucuje naučené konvence: `__file__`-relativní cesty, rozpočty (dense N≤2500 / sparse N≤12000, vynucení mid-cell, skip-with-note), poctivé negativy.
   - **Použití:** spuštění navrženého experimentu; výstup se páruje s Adverzariálním verifikátorem.

3. **[Adverzariální verifikátor](adversarial-verifier.md) — *Strict Mode*** → [`.claude/agents/adversarial-verifier.md`](../../.claude/agents/adversarial-verifier.md)
   - **Role:** přísný oponent — hledá logické a metodologické mezery, ověřuje soulad závěrů s daty (`core-data/calculations/`, `findings.json`), kontroluje statistiky (SE/CI/AIC) proti raw výstupu a **referenční integritu (nikdy nevymýšlí arXiv ID/DOI, ověřuje lit. searchem)**.
   - **Použití:** audit hotových draftů, verifikace citací, prověřování vnitřní konzistence (konvence, vzorce, exaktní výsledky vs. fity).

## Použití ve workflow skriptech / přes Agent tool

Funkční subagenti se volají přes `agentType` (Workflow tool) nebo `subagent_type` (Agent tool) — Claude Code je resolvuje z registru `.claude/agents/`:

```javascript
// Workflow tool — audit posledního kola Adverzariálním verifikátorem
const audit = await agent(
  'Audituj integritu nálezů F-030..F-033 a writeupů VYPOCET-26..29 (statistiky vs raw, ověření referencí, overreach 2D->4D).',
  { label: 'verifier:round14-15', agentType: 'adversarial-verifier', schema: AUDIT_SCHEMA }
);
```

> **Pozn. ke konvenci:** dřívější verze README uváděla `systemPromptFile:` — to byla Gemini/Antigravity konvence. V Claude Code Workflow/Agent toolu se používá `agentType`/`subagent_type` odkazující na registrovaný subagent v `.claude/agents/`. Alternativně lze systémový prompt vložit inline do promptu (robustní, když registr ještě nenačetl nově přidaný soubor).

## Jazyková politika

- **Interní instrukce (prompty):** v angličtině (maximální přesnost LLM při sledování logiky).
- **Výstupy agentů:** **čeština** pro prózu, **angličtina** pro identifikátory/slugy/kód — striktně dle [CLAUDE.md](../../CLAUDE.md).
