# Verifikační zpráva — Asymptotická bezpečnost (Asymptotic Safety)

**Datum:** 2026-06-05
**Ověřované soubory:**
- `knowledge-base/approaches/03-asymptotic-safety.md` (česká próza)
- `core-data/fragments/asymptotic-safety.json` (anglický JSON fragment)

## Co bylo zkontrolováno

### Validita JSON
JSON je syntakticky validní (parsuje se bez chyb). Po všech úpravách znovu ověřeno (`json.load` OK, 36 referencí, žádný „dangling" odkaz `source` ve vzorcích).

### Audit referencí (zkontrolováno 22+ z 36)
Přes WebFetch na arXiv byly ověřeny ID, název, autoři a rok u následujících klíčových prací (všechny **OK**, není-li uvedeno jinak):

- `hep-th/9605030` Reuter 1998 — OK (předloženo 1996, publ. 1998)
- `0912.0208` Shaposhnikov & Wetterich — OK
- `1301.4191` Falls et al. „A bootstrap strategy for AS" — OK
- `1410.4815` Falls et al. „Further evidence…" (do $R^{34}$) — OK
- `1607.04962` Falls et al. „On de Sitter solutions in AS f(R)" — OK
- `1311.2898` Donà, Eichhorn & Percacci — OK
- `hep-th/0508202` Lauscher & Reuter (fraktální prostoročas) — OK
- `0805.2909` Codello, Percacci & Rahmede — OK
- `1707.01107` Eichhorn & Held (top mass) — OK
- `1711.02949` Eichhorn, Held & Wetterich (jemná struktura) — OK
- `2107.03839` de Brito, Eichhorn & Lino dos Santos (weak-gravity) — OK
- `2310.20603` D'Angelo (lorentzovská AS) — OK
- `2412.13800` Pastor-Gutiérrez et al. — OK
- `2507.22169` Pawlowski, Reichert & Wessely — OK (existuje, předloženo 2025-07-29)
- `2509.26352` Schiffer 2025 — OK
- `2502.12290` Basile, Knorr, Platania & Schiffer 2025 — OK
- `1411.7712` Coumbe & Jurkiewicz — OK
- `2306.10408` Saueressig & Wang (foliated AS) — OK
- `1911.02967` Donoghue „A critique…" — OK
- `2302.04272` Platania „Black Holes in AS Gravity" — OK
- `hep-th/9907027` Souma 1999 — OK
- `hep-th/0312114` Litim 2004 — OK
- `hep-th/0108040` Lauscher & Reuter 2002 — OK
- `1710.05815` Wetterich (Exact evolution equation…) — OK (arXiv repost z 2017 původního rukopisu 1992, publ. Phys. Lett. B301, 90 (1993); název/autor/rok/DOI souhlasí)

### Audit vzorců (zkontrolováno 6)
- **Weinbergův $2+\varepsilon$ pevný bod $g^*=(3/38)\varepsilon$** — OK (Percacciho přehled: $\tilde G_*=\varepsilon/q$, $q=38/3$, tj. $=3\varepsilon/38$).
- **Anomální dimenze $\eta_N=2-d$, propagátor $1/p^4$, $d_{\rm eff}=2$** — OK (Lauscher & Reuter).
- **Spektrální dimenze $d_s:4\to2$** — OK.
- **EH-oseknutí: $\theta',\theta''$ a součin** — OK; Percacciho přehled uvádí $\tilde\Lambda=0{,}171$, $\tilde G=0{,}701$, vlastní čísla $-1{,}69\pm2{,}49i$ ⇒ $\theta'\approx1{,}69$, $\theta''\approx2{,}49$, součin $\approx0{,}12$. Konzistentní s prózou ($\theta'\approx1{,}5$–$2{,}5$, součin $0{,}12$–$0{,}14$).
- **Top kvark $M_t\approx171$ GeV a $m_t-m_b\approx170$ GeV** — OK (Eichhorn & Held 1707.01107).
- **Higgs $M_H\approx126$ GeV vs. naměřeno $125{,}25$ GeV** — OK.

## Co bylo špatně a co bylo opraveno

### 1. ZÁVAŽNÁ chybná atribuce reference (arXiv:1307.0765)
Práce `arXiv:1307.0765` „Critical exponents in quantum Einstein gravity" byla v próze i v JSON přiřazena autorům **Falls, Litim, Nikolakopoulos & Rahmede**. Ve skutečnosti je autorem **S. Nagy, B. Fazekas, L. Juhász, K. Sailer** (Phys. Rev. D88, 116010). Tato reference byla navíc použita jako hlavní zdroj nejsilnějších numerických tvrzení.
- **Oprava:** v JSON přejmenováno `falls-2013-critexp` → `nagy-critexp-2013` se správnými autory, názvem, DOI a poznámkou. V próze opraven bibliografický záznam #33 i text.

### 2. Neověřitelné numerické hodnoty $\lambda^*g^*\approx0{,}133$ (regulátor $0{,}136$) a $1/\nu=\theta'\approx1{,}472$
Tyto přesné hodnoty se NEPODAŘILO ověřit proti citovaným zdrojům. Skutečná vysokostupňová studie do $R^{34}$ (`1410.4815`) uvádí součin $g^*\lambda^*\approx0{,}121$ a vůdčí exponent $\theta'\approx2{,}5$ (nikoli $1{,}472$). Hodnota $1{,}472$ ani $0{,}133/0{,}136$ se v ověřených pracích Fallse a kol. nevyskytly.
- **Oprava:** v JSON vzorcích `fixed-point-condition` a `critical-exponents-def` (a v konceptu `critical-exponents`) nahrazeny přesné hodnoty rozmezím $0{,}12$–$0{,}14$ resp. $\theta'$ řádu $2{,}5$; zdroj přesměrován na `falls-2014-evidence`. Sporné hodnoty ponechány pouze jako explicitně označené **⚠️ neověřeno** s vysvětlením. V próze totéž (matematická sekce, milník 2013–2016, souhrnná tabulka).

### 3. Nekonzistentní cílové id v JSON connection
Connection `asymptotic-safety → "supergravity-uv"` měla popis o Stelleho kvadratické/vyšší-derivační gravitaci (ne o supergravitaci). Cílové id neodpovídalo obsahu ani prózové sekci „Kvadratická / vyšší-derivační gravitace".
- **Oprava:** cílové id změněno na `quadratic-gravity`.

### 4. Zbytkový redakční komentář v próze
Bibliografický záznam #16 obsahoval interní poznámku „Původně chybně uvedeno arXiv:1307.0765 / 1601.01800 — viz verifikační zpráva." — odstraněna (záznam je nyní správný).

## Konzistence próza ↔ JSON
- Hodnocení „explored" v JSON odpovídají prózovým hodnocením (CDT „partially", kvadratická gravitace „well", holografie „barely", swampland/struny „partially", LQG/GFT/emergentní „barely"). Slavná, dobře studovaná pojítka nejsou podhodnocena. **OK.**
- Numerické hodnoty (Higgs 126, top 171, $\eta_N=-2$, $d_s:4\to2$, obsah SM $N_S{=}4,N_V{=}12,N_F{=}45$) souhlasí mezi prózou a JSON.
- Bimetrické/fluktuační hodnoty $g^*\approx0{,}7$, $\lambda^*\approx0{,}2$ v próze jsou řádově konzistentní s jednometrickým EH pevným bodem ($\tilde G=0{,}701$, $\tilde\Lambda=0{,}171$).

## Co zůstává nejisté
- **Přesná univerzální hodnota součinu $g^*\lambda^*$ a vůdčího exponentu $\theta'$.** Literatura uvádí rozptyl podle schématu/oseknutí; přesná čísla $0{,}133$/$0{,}136$ a $1{,}472$ se nepodařilo doložit a jsou ponechána jako neověřená. Ověřená studie do $R^{34}$ dává $\approx0{,}121$ a $\theta'\approx2{,}5$.
- **Globální id v `relatedTo`/`connections`** (`quadratic-gravity`, `noncommutative-geometry`, `causal-sets`, `experimental-tests`, `black-holes-information` atd.) jsou plauzibilní, ale nebyla křížově ověřena proti centrálnímu rejstříku konceptů projektu — předpokládá se jejich existence.
- **Reference s ne-arXiv URL** (`weinberg-1979`, `thooft-veltman-1974`, `goroff-sagnotti-1986`, `stelle-1977`, `niedermaier-reuter-2006`, monografie Reuter-Saueressig) byly ověřeny metadaty/DOI, nikoli plnotextovým náhledem arXiv.
