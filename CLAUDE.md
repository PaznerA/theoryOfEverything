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

## Workflow

- Velké rešerše a analýzy se orchestrují přes Workflow tool; skripty se archivují do `workflows/`.
- Po každé dokončené fázi aktualizovat PROGRESS.md (stav, statistiky, další kroky).
- Nové poznatky se zapisují do knowledge base, ne jen do konverzace.
