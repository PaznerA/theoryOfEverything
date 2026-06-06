# Verifikační zpráva — Twistorová teorie a program amplitud

**Pilíř:** `twistors-amplitudes`
**Datum verifikace:** 2026-06-05 (aktuální verze souborů)
**Agent:** adversarial verification, economy mode
**Ověřované soubory:**
- `knowledge-base/approaches/08-twistors-amplitudes.md` (česká próza)
- `core-data/fragments/twistors-amplitudes.json` (anglický JSON fragment)

---

## Metodika

Staženo 8 referencí přes WebFetch z arxiv.org (prioritizovány reference podpírající nejsilnější tvrzení). Zkontrolovány 4 klíčové vzorce. JSON byl platný bez oprav.

---

## Ověřené reference (bez problémů)

| ID / arXiv | Název | Autoři | Rok | Výsledek |
|---|---|---|---|---|
| hep-th/0312171 | Perturbative Gauge Theory As A String Theory In Twistor Space | E. Witten | 2003 | OK |
| hep-th/0501052 | Direct Proof of Tree-Level Recursion Relation in Yang-Mills Theory | Britto, Cachazo, Feng, Witten | 2005 | OK |
| 0805.3993 | New Relations for Gauge-Theory Amplitudes | Bern, Carrasco, Johansson | 2008 | OK |
| 1312.2007 | The Amplituhedron | Arkani-Hamed, Trnka | 2013 | OK |
| 2105.14346 | w(1+infinity) and the Celestial Sphere | A. Strominger | 2021 | OK |
| hep-th/0611086 | Is N=8 Supergravity Ultraviolet Finite? | Bern, Dixon, Roiban | 2006 | OK |

---

## Nalezené a opravené problémy

### 1. Chybné autorství — ref 32 MD (arXiv:2104.07031)

**Problém:** Markdown (ref 32, řádek 378) přisuzoval práci „Twistor action for general relativity" autorovi **Mason, L.**, ačkoli skutečným a jediným autorem je **Atul Sharma**.

**Dopad:** JSON (`twistor-action-gr-2021`) byl správný (autoři: „A. Sharma"). Chyba byla pouze v próze.

**Oprava:** Ref 32 opraven na „Sharma, A. (2021)." a titul sjednocen se správným názvem „Twistor action for general relativity".

---

### 2. Chybné autorství — ref 33 MD (arXiv:2312.13267)

**Problém:** Markdown (ref 33, řádek 380) přisuzoval práci „On the anomaly interpretation of amplitudes in self-dual Yang-Mills and gravity" autorům **Costello, Paquette, Sharma**, ačkoli skutečnými autory jsou **George Doran, Ricardo Monteiro, Sam Wikeley**.

**Dopad:** JSON (`integrability-anomaly-2023`) byl správný. Chyba byla pouze v próze.

**Oprava:** Ref 33 opraven na „Doran, G., Monteiro, R. & Wikeley, S."

---

### 3. Matoucí citace — N=5 vs. N=8 (arXiv:1409.3089)

**Problém:** V těle textu (řádek 159) byl arXiv:1409.3089 citován ve větě o **N=8 SUGRA UV konečnosti do 4 smyček**. Tato práce (Bern, Davies, Dennen 2014) se však týká **N=5 supergravitace**, nikoli N=8. V číslovaném seznamu referencí (ref 26) byl titul uveden správně jako „N=5 Supergravity".

**Oprava:** Tělo textu bylo přepsáno tak, aby primárním zdrojem pro N=8 byl Bern–Dixon–Roiban 2006, a N=5 výsledek je explicitně označen jako „N=5".

---

## Ověřené vzorce (bez oprav)

| Vzorec | Výsledek |
|---|---|
| Penroseova transformace: $H^1(\mathbb{PT}, \mathcal{O}(-2h-2))$; pro $h=0$: $\mathcal{O}(-2)$, pro $h=2$: $\mathcal{O}(-6)$ | Správně |
| Parke–Taylor: $\langle ij\rangle^4/(\langle12\rangle\langle23\rangle\cdots\langle n1\rangle)$ | Správně |
| $w_{1+\infty}$ komutátor: $[w^p_m, w^q_n]=[m(q-1)-n(p-1)]w^{p+q-2}_{m+n}$ | Správně |
| ASD podmínka: $C_{abcd} = -\tfrac{1}{2}\epsilon_{ab}{}^{pq}C_{cdpq}$ | Správně |

---

## Zbývající nejistoty

- **arXiv:1409.3089** cituje explicitně „N=5", ale v literatuře existují analogické 4-smyčkové výsledky pro N=8 SUGRA (zejm. arXiv:0905.2326). V dokumentu není přímá citace N=8 čtyřsmyčkového výpočtu — jde o mezeru, nikoli chybu.
- **arXiv:2507.00772** (celestiální chirální algebry, sekce o současném stavu) nebyl ověřen (URL neexistovala k datu verifikace, může jít o preprint z budoucnosti). Označeno inline v próze pro transparentnost.
- **JSON byl platný** bez nutnosti oprav; veškeré opravy se týkaly pouze prózového souboru MD.
