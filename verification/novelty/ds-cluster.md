# Novelty check: ds-cluster (L3-1 + L2-5 + L5-5)

**Datum:** 2026-06-06
**Zpracoval:** Claude Sonnet 4.6 (subagent)

---

## Hypotéza

**L3-1 (jádro):** UV spektrální dimenze d_s NENÍ universálně rovna 2 — je predikovatelnou funkcí UV exponentu propagátoru z a topologické dimenze D, konkrétně d_s(z,D). Master-vzorec lze odvodit ze sdíleného formalismu P(s) = Tr e^{-sG^{-1}} pro libovolný přístup ke kvantové gravitaci.

**L2-5:** Spin-foam coarse-graining, CST Benincasa-Dowker d'alembertián a Reuterův AS fixed point sdílejí tentýž znaménko běhu d_s — konvergenční tvrzení, že jde o "jeden fixed point".

**L5-5:** Wetterich FRG aplikovaná na CST Benincasa-Dowker operátor (B_ε jako Γ_k^(2)) může vyřešit nelokalitu pomocí decoupligu ghost módů.

---

## Co bylo nalezeno

### Vysoké překrytí — L3-1 (master formula)

**1. Hořava, arXiv:0902.3657 (PRL 2009)**
Explicitně derivuje `d_s = 1 + D/z` pro Hořavovu gravitaci s dynamickým kritickým exponentem z v D+1 dimenzích. Toto JE master-vzorec — vztah d_s(z,D) pro anisotropní propagátor. Pro z=3, D=3 → d_s=2 (UV), pro z=1 → d_s=4 (IR). Srovnává s CDT.

**2. Sotiriou, Visser & Weinfurtner, arXiv:1105.6098 (PRD 2011)**
"From dispersion relations to spectral dimension — and back again": Explicitně ukazuje, jak přiřadit d_s libovolné disperzní relaci (=propagátorovému exponentu). Srovnává CDT a Hořavovu gravitaci. Toto je přímý předchůdce L3-1.

**3. Calcagni, Modesto & Nardelli, arXiv:1408.0199 (IJMPD 2016)**
"Quantum spectral dimension in quantum field theory": Zobecňuje výpočet d_s pro logaritmické disperzní relace a Stelle-teorie. d_s = 2 v UV pro Stelle, ale variabilní pro obecné z. Aplikuje Seeley-DeWitt a sedlového bodu techniku.

**4. Calcagni, Oriti & Thürigen, arXiv:1311.3340 (CQG 2014)**
"Spectral dimension of quantum geometries": Srovnává d_s přes LQG, spin-foam, GFT. Zjišťuje, že d_s NENÍ universální — závisí na kombinatorické struktuře (viz L3-1: probe-dependence jako prediktor). Neuvádí master-vzorec d_s(z,D) pro tyto přístupy.

**5. Calcagni & Nardelli, arXiv:1304.2709 (PRD 2013)**
"Spectral dimension and diffusion in multiscale spacetimes": d_s pro multifrakcionální prostory, srovnání tří tříd. Explicitní vzorec pro d_s(α,D) kde α je frakcionální exponent (= analogon z).

**6. Carlip, arXiv:1705.05417 (CQG 2017)**
Přehledový článek: "Dimension and Dimensional Reduction in Quantum Gravity". Uvádí, že d_s~2 v UV je "almost universal feature" pro UV-renormalizovatelné teorie — ale ne absolutně universální. Nezavádí master-vzorec d_s(z,D) explicitně, pouze diskutuje Hořavův výsledek.

### Střední překrytí — L2-5

**7. Calcagni et al., Towards the map of quantum gravity, arXiv:1708.07445 (2017)**
Srovnává d_s přes CDT, AS, LQG, Hořava, NCG, nelokalní gravitaci, Stelle. Zahrnuje výsledky pro spin-foam a CST. Nenašel jsem explicitní tvrzení o "jednom AS fixed pointu" unifikujícím spin-foam + CST BD + Reuter.

**8. Eichhorn & Mizera, arXiv:1311.2530 (CQG 2014)**
Probe-dependence v CST: d_s roste pro náhodnou procházku na diskrétním kauzálním grafu, ale klesá pro d'alembertianovou sondu. Přímo relevantní pro L2-5 (znaménko d_s v CST BD závisí na sondě — ne jednoznačné tvrzení o konvergenci k Reuterovu fixed pointu).

### Nízké překrytí — L5-5

**9. Žádný přímý nález** pro aplikaci Wetterich FRG na CST Benincasa-Dowker operátor jako Γ_k^(2) s β-funkcí nelokalního bumpu. Spin-foam coarse-graining (Steinhaus 2007.01315) pracuje s FRG-inspired metodami, ale ne přímo na BD operátoru.

---

## Verdikt

**L3-1: PARTIALLY-KNOWN**

Klíčový výsledek d_s(z,D) = 1 + D/z pro Hořavovu gravitaci je explicitně publikován od roku 2009 (Hořava, 0902.3657). Sotiriou-Visser-Weinfurtner (1105.6098) to zobecnil na libovolné disperzní relace. Calcagni et al. (1408.0199, 1304.2709) to dále rozvinul pro různé třídy propagátorů.

**Co ZŮSTÁVÁ nové v L3-1:**
- Jednotný formalizmus P(s) = Tr e^{-sG^{-1}} aplikovaný *systematicky* na všechny čtyři konkrétní přístupy (AS, CDT, LQG, CST) najednou, s explicitním tabulkovým srovnáním d_s^UV(z,D) pro každý.
- Tvrzení, že d_s není universálně 2 nejen jako technický fakt, ale jako *klasifikační otisk* — identifikátor, který odlišuje přístupy, nikoli pouze potvrzuje "konvergenci".
- Probe-dependence jako fundamentální součást klasifikace (viz ds-contradiction.md): tatáž teorie (CST) dává různá d_s pro různé sondy — toto **není** v literatuře systematicky formulováno jako klasifikační princip.

**L2-5: PARTIALLY-KNOWN**
Znaménko běhu d_s v CST závisí na sondě (Eichhorn & Mizera, Belenchia et al.). Tvrzení o "jednom Reuterově fixed pointu" pro spin-foam + CST BD + AS není v literatuře nalezeno. Ale konvergence d_s→2 v AS a CDT je dobře dokumentována; tvrzení L2-5 je příliš silné bez rozlišení probe-dependence.

**L5-5: PLAUSIBLY-NOVEL**
Aplikace Wetterich FRG specificky na CST BD operátor jako vertexní funkci Γ_k^(2) nebyla nalezena. Nízká priorita.

---

## Co zbývá nového (souhrnně)

Jádrem zbývající novosti je **systematická srovnávací tabulka d_s^UV(z,D)** přes všechny hlavní přístupy, využívající P(s) = Tr e^{-sG^{-1}} jako unifikující formalizmus, SPOLU s probe-dependence jako explicitní klasifikační dimenzí. Hořavův vzorec d_s=1+D/z je znám; jeho rozšíření na anisotropně modifikované propagátory LQG, CST BD a AS FRG propagátor v rámci jednotného heat-kernel formalismu, s explicitním tvrzením o ne-universalitě jako diskriminátoru mezi přístupy — to v literatuře systematicky chybí.

---

## Doporučení

**pursue** — ale s přerámováním: L3-1 by měla být prezentována nikoli jako "d_s není 2" (to je už v literatuře), ale jako "proof-of-concept systematické klasifikace: tabulka d_s^UV(z,D) pro AS / CDT / LQG / CST, včetně probe-dependence jako dalšího parametru klasifikace". Toto srovnání se systematickým formalismem P(s) = Tr e^{-sG^{-1}} přes všechny čtyři přístupy současně nebyla nalezena.

L2-5 vyžaduje opravu: místo "jeden Reuterův fixed point" upřesnit na "d_s v UV závisí na přístupu I SONDĚ — proto nelze tvrdit universální konvergenci". L5-5 je nízká priorita, ale novela je plausibilní.

---

## Klíčové citace

| arXiv | Rok | Autoři | Vztah k L3-1 |
|-------|-----|--------|--------------|
| 0902.3657 | 2009 | Hořava | Derivuje d_s=1+D/z — přímý předchůdce master-vzorce |
| 1105.6098 | 2011 | Sotiriou, Visser, Weinfurtner | d_s z libovolné disperzní relace — high overlap |
| 1408.0199 | 2016 | Calcagni, Modesto, Nardelli | d_s(z,D) pro log. disperze a Stelle — high overlap |
| 1311.3340 | 2014 | Calcagni, Oriti, Thürigen | d_s přes LQG/SF — probe-sensitive, ne master-vzorec |
| 1304.2709 | 2013 | Calcagni, Nardelli | d_s(α,D) pro multifrakcionální prostory — medium overlap |
| 1705.05417 | 2017 | Carlip | Přehled, "almost universal d_s~2" — kontextuální |
| 1311.2530 | 2014 | Eichhorn, Mizera | Probe-dependence v CST — relevantní pro L2-5 |
| 1708.07445 | 2017 | Calcagni et al. | Map of QG — srovnání d_s přes přístupy |
