# Rozlišení rozporu: spektrální dimenze v teorii kauzálních množin

**Datum:** 2026-06-06  
**Dotčené hrany:** edge 501 (causal-sets → spectral-dimension), edge 1539 (noncommutative-geometry → causal-sets)

## Co bylo tvrzeno

- **Edge 501 (causal-sets.json):** Tvrdil, že náhodné procházky na kauzálních množinách a nelokalní d'Alembertián dávají spektrální dimenzi, která *klesá* na krátkých škálách (někdy na ~2), čímž ozvěňuje CDT a asymptoticky bezpečnou gravitaci.
- **Edge 1539 (noncommutative-geometry.json):** Tvrdil, že spektrální dimenze se chová opačně — v NCG *klesá*, zatímco v kauzálních množinách *roste*.

Tyto dvě tvrzení si navzájem odporovaly, přičemž obě obsahovaly částečnou pravdu.

## Co říká literatura

Rozpor je způsoben **závislostí na sondě (probe-dependence)**:

1. **Náhodná procházka na diskrétním kauzálním uspořádání** (Eichhorn & Mizera, arXiv:1311.2530, CQG 31:125007, 2014): Spektrální dimenze se na krátkých škálách *zvyšuje* — opak CDT/asymptotické bezpečnosti. Příčinou je nelokalita kauzálních množin hluboce zakotvená v lorentzovské struktuře; kauzální spektrální dimenze (pravděpodobnost setkání dvou náhodných chodců) vykazuje stejný trend.

2. **Nelokalní d'Alembertián / kontinuální propagátory** (Belenchia, Benincasa, Marciano & Modesto, arXiv:1507.00330, PRD 2016): Tepelně-jádrová analýza s propagátorem odvozeným z kauzálních množin dává *universální pokles* d_s → 2 v UV ve všech dimenzích. Mechanismus: regularizovaný propagátor se chová jako (k²)^(d/2) ve vysokých hybnostech, čímž zlepšuje UV chování a způsobuje redukci dimenze.

Oba výsledky jsou správné a navzájem se nevylučují — měří jiné aspekty diskrétní struktury.

## Co bylo opraveno

- V `causal-sets.json` (connections, causal-sets → spectral-dimension): zjednodušené tvrzení o poklesu nahrazeno plnou probe-závislou charakterizací s oběma citacemi.
- V `noncommutative-geometry.json` (connections, noncommutative-geometry → causal-sets): tvrzení „roste v CST, klesá v NCG" upřesněno — vztahuje se pouze na náhodnou procházku v CST vs. tepelné jádro v NCG; d'Alembertianová sonda v CST se shoduje s NCG na redukci k ~2.

## Vztah k hypotéze L3-1

Hypotéza L3-1 předpokládá, že efektivní dimenze prostočasu závisí na volbě sondy (probe-dependence jako predikce, nikoli anomálie). Tento výsledek tuto hypotézu přímo potvrzuje: tatáž teorie (kauzální množiny) dává kvalitativně opačné chování spektrální dimenze v závislosti na tom, zda se použije diskrétní náhodná procházka na kauzálním grafu, nebo kontinuální nelokalní d'Alembertián. Probe-dependence není numerická korekce, ale zásadní fyzikální příznak nelokalní, fundamentálně lorentzovské struktury diskrétního prostočasu.
