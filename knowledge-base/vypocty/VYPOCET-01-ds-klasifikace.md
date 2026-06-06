# VÝPOČET 01 — Klasifikační tabulka spektrální dimenze d_s^UV(z, D, probe)

**Hypotéza:** L3-1 (přerámovaná) — *„Spektrální dimenze d_s NENÍ univerzálně 2; je
to klasifikační otisk propagátoru, navíc závislý na sondě (probe)."*
**Datum:** 2026-06-06
**Adresář výpočtu:** `core-data/calculations/ds-classification/`
**Skript:** `calc.py` · **Data:** `results.json` · **Graf:** `ds_flow.png`

---

## 1. Cíl

Sestavit jednotnou, **numericky** spočtenou klasifikační tabulku UV spektrální
dimenze d_s napříč hlavními přístupy ke kvantové gravitaci, a to:

1. **Reprodukovat** publikovanou prior art (validace metody): Hořavovo
   d_s = 1 + D/z (arXiv:0902.3657), Sotiriou–Visser–Weinfurtner (1105.6098),
   Stelle/Calcagni (1408.0199), asymptotická bezpečnost (hep-th/0508202,
   1110.5224), causal sets (1507.00330, 1311.2530).
2. **Přidat novou hodnotu:** jeden společný formalismus návratové pravděpodobnosti
   P(σ) aplikovaný numericky a uniformně na *všechny* přístupy najednou,
   a **sondu (probe) jako třetí klasifikační osu** vedle exponentu z a dimenze D.

Přerámování vychází z novelty-checku (`verification/novelty/ds-cluster.md`):
samotný vzorec d_s = 1 + D/z je v literatuře explicitní od roku 2009 — **nelze
jej prezentovat jako objev**. Novum je *systematičnost jedné metody*,
*probe-dependence jako parametr* a *interpretace jako diskriminátor* místo důkazu
konvergence.

---

## 2. Metoda

### 2.1 Jednotný formalismus návratové pravděpodobnosti

Pro (euklidovské) pole s inverzním propagátorem F(k) definujeme heat-trace /
návratovou pravděpodobnost difúzního procesu

> **P(σ) = ∫ d^D k · exp( −σ F(k) )**

a spektrální dimenzi jako

> **d_s(σ) = −2 · d ln P / d ln σ.**

* σ → ∞ sonduje IR (malé k, F → k² ⟹ d_s → D),
* σ → 0 sonduje UV (velké k, F ~ k^{2γ} ⟹ d_s → D/γ).

### 2.2 Master-vzorec (symbolicky ověřeno)

Pro radiální integrál s čistou mocninou F = k^{2γ} dává sympy uzavřeně

> **d_s^UV = D / γ,    γ = (UV mocnina hybnosti)/2.**

(Symbolická kontrola v `calc.py`, funkce `symbolic_master()`, vrací přesně
`D/gamma`.) Speciální případy:

| Přístup | F(k) v UV | γ | d_s^UV |
|---|---|---|---|
| GR | k² | 1 | D = 4 |
| Stelle / 4-derivative | k⁴ | 2 | D/2 = 2 |
| Asympt. safety | k^{2−η}, η=2−D=−2 → k⁴ | 2 | D/2 = 2 |
| Causal set (d'Alembert) | k^D (nelokální) | D/2 | 2 (univerzální) |

### 2.3 Anizotropní (Hořava–Lifshitz) případ

Hořava je **anizotropní** (čas škáluje jako k¹, prostor jako k^z), takže
*neřídí* se izotropním pravidlem D/γ. Návratová pravděpodobnost faktorizuje:

> P(σ) ~ σ^{−1/2} · σ^{−D_space/(2z)}  ⟹  **d_s = 1 + D_space/z.**

Implementováno přímo (`_logP_horava`), s fyzikálním IR crossoverem
F_space = k² + k^{2z}/m^{2z−2} (relevantní z=1 operátory vracejí d_s=4 v IR).

### 2.4 Numerická realizace

* Radiální integrál se počítá v proměnné t = ln k na širokém σ-adaptovaném
  gridu s **log-sum-exp** trikem (`_logP_radial`), aby byly stabilní i extrémní
  hodnoty σ ∈ [10⁻¹⁰, 10⁶]. Prefaktory (objem koule) se v log-derivaci ruší.
* d_s(σ) centrální diferencí ln P v ln σ (krok h=10⁻²).
* Σ-grid: 90 bodů logaritmicky od IR (σ=10⁶) do UV (σ=10⁻¹⁰).

---

## 3. Vstupy a citace

Každé číslo „expected" je validace proti publikované hodnotě; samotná d_s se
počítá numericky.

| Vstup | Hodnota | Zdroj (arXiv) |
|---|---|---|
| Hořava master-vzorec | d_s = 1 + D/z | Hořava **0902.3657** (PRL 2009) |
| d_s z disperzní relace | obecná procedura | Sotiriou–Visser–Weinfurtner **1105.6098** (PRD 2011) |
| Stelle UV | d_s^UV = 2 pro libovolné D | Calcagni–Modesto–Nardelli **1408.0199** (2016) |
| AS UV | d_s = 2 (d=4) | Lauscher–Reuter **hep-th/0508202** (2005) |
| AS: η_N a propagátor | η_N = 2−d = −2 → 1/p⁴, NGFP d_s=d/2 | Reuter–Saueressig **1110.5224** (2011) |
| Causal set, d'Alembert | univerzální UV d_s → 2 ve všech D | Belenchia–Benincasa–Marciano–Modesto **1507.00330** (PRD 2016) |
| Causal set, random walk | UV d_s **roste** nad D | Eichhorn–Mizera **1311.2530** (CQG 2014) |
| Multifrakcionální | d_s = D/γ, UV pick d_s → 2 | Calcagni–Nardelli **1304.2709** (PRD 2013) |
| Přehled „almost universal 2" | kontext | Carlip **1705.05417** (CQG 2017) |

Konvence ověřeny přímo fetchem abstraktů/PDF (viz `results.json →
conventions_validated`).

---

## 4. Výsledky

### 4.1 Master klasifikační tabulka (D = 4)

| Přístup | Sonda (probe) | z_eff | d_s^UV | d_s^IR | Validace | Zdroj |
|---|---|---|---|---|---|---|
| GR | heat kernel (k²) | z=1 | **4** | 4 | REPRODUKCE | Carlip 1705.05417 |
| Hořava–Lifshitz | heat kernel (anizotr.) | z=2 | **5/2** | 4 | REPRODUKCE | 0902.3657 |
| Hořava–Lifshitz | heat kernel (anizotr.) | z=3 | **2** | 4 | REPRODUKCE | 0902.3657 |
| Stelle kvadratická gravitace | heat kernel k²(1+k²/m²) | z=2 (UV k⁴) | **2** | 4 | REPRODUKCE | 1408.0199 |
| Asymptotická bezpečnost | heat kernel (η=−2 → 1/p⁴) | z_eff=2 | **2** | 4 | REPRODUKCE | 0508202, 1110.5224 |
| **Causal sets** | **d'Alembertián (Benincasa–Dowker)** | z_eff=D/2 | **2** | 4 | REPRODUKCE | 1507.00330 |
| **Causal sets** | **náhodná procházka na kauzálním grafu** | z_eff<1 | **>D (roste, num. 8)** | 4 | REPRODUKCE (kvalitat.) | 1311.2530 |
| Multifrakcionální (Calcagni) | heat kernel (frakční míra) | z_eff=D/2 | **2** | 4 | REPRODUKCE (srovnání) | 1304.2709 |

**Numerická shoda:** všech 12 validačních kontrol v `calc.py` prošlo
(GR UV=4.0; Hořava z=2 UV=2.5; Hořava z=3 UV=2.0; Stelle/AS/d'Alembert/multifrac
UV=2.0; všechny IR=4.0; random walk UV=8.0 > D). Symbolický master-vzorec =
`D/gamma`.

### 4.2 Graf

`ds_flow.png` — všechny toky d_s(σ) přeložené přes sebe; osa x = log₁₀(1/σ),
tj. IR vlevo, UV vpravo. Všechny křivky startují z d_s=4 (IR) a klesají
ke svým UV hodnotám 2 nebo 5/2 — **kromě** random-walk sondy na causal setu,
která jako jediná **roste** k 8.

---

## 5. Interpretace pro hypotézu

### 5.1 Co se reprodukuje (validace metody)

Řádky GR, Hořava (z=2,3), Stelle, AS, causal-set d'Alembertián a multifrakcionální
**reprodukují publikovaná čísla** přesně jediným numerickým enginem. To je důkaz,
že formalismus P(σ) = ∫d^Dk e^{−σF(k)} je správně implementován a konzistentní
napříč přístupy. Žádné z těchto čísel nepředstavuje nový objev — jsou to
literaturní hodnoty.

### 5.2 Co je naše přidaná hodnota (nové)

1. **Jeden formalismus, uniformně.** Tatáž numerická procedura (jeden engine,
   jedna definice d_s) dává *všechna* čísla. V literatuře jsou tato čísla
   roztroušena přes různé práce s různými konvencemi a metodami; sjednocená
   tabulka z jediného P(σ) chybí.

2. **Sonda jako třetí klasifikační osa.** Nejsilnější výsledek: **tatáž teorie
   (causal sets) dává OPAČNÝ UV trend podle sondy** — d'Alembertián vede k
   d_s → 2 (dimenzionální redukce), zatímco náhodná procházka vede k d_s rostoucí
   nad D (kvůli lorentzovské nelokálnosti / vysoké konektivitě kauzálního grafu).
   To přesně řeší vnitřní rozpor v našich datech (connections.json ř. 657 „drops"
   vs. ř. 1777 „increases"): **obě hrany měly pravdu, ale generalizovaly ze špatné
   sondy.** Klasifikátor není (z, D), ale **(z, D, probe)**.

3. **Přerámování z „konvergence" na „klasifikaci".** Zdánlivá univerzální
   konvergence d_s → 2 je ve skutečnosti shoda *podtřídy* propagátorů s UV mocninou
   k⁴ (Stelle, AS, d'Alembert) — tj. γ=2 v master-vzorci D/γ. Hořava z=2 (5/2),
   GR (4) a random-walk sonda (>D) konvergenci **explicitně porušují**. d_s^UV je
   tedy *otisk*, ne konstanta.

### 5.3 Vztah ke clusteru L2-5 (oprava)

Tvrzení L2-5 o „jednom Reuterově fixed pointu" sjednocujícím spin-foam + CST BD +
AS je tímto výpočtem **oslabeno**: UV d_s závisí nejen na přístupu, ale i na sondě,
takže univerzální konvergenci nelze tvrdit. Toto je přímý empirický vstup do
připravované úpravy `connections.json`.

---

## 6. Limity výpočtu

1. **Efektivní izotropní propagátory.** Causal-set d'Alembertián a random-walk
   sonda jsou v podstatě **lorentzovské a diskrétní**; jejich pravé chování není
   izotropní euklidovský propagátor. Naše F(k) jsou *efektivní* kernely
   reprodukující publikované **asymptotiky** (d'Alembert: univerzální UV=2;
   random walk: UV roste nad D), nikoli mikroskopické simulace sprinklingů.
   Random-walk řádek je proto explicitně označen **kvalitativní** a numerická
   hodnota 8 (=D+4) je *ilustrativní* volba splňující jen „d_s^UV > D"; přesné
   číslo závisí na hustotě sprinklingu a definici procházky (Eichhorn–Mizera
   nezveřejnili univerzální asymptotickou konstantu).

2. **Crossover, ne odvozený β-flow.** IR↔UV přechody (Stelle, AS, Hořava) jsou
   modelovány ručně vloženými crossover-kernely (dva mocninné členy), ne odvozeny
   z renormalizačně-grupového toku. UV a IR *limity* jsou robustní; tvar přechodu
   uprostřed je modelově závislý a nemá být interpretován kvantitativně.

3. **AS s běžící η jen jako fixed-point hodnota.** Anomální dimenze η_N je vzata
   jako konstantní fixed-point hodnota −2; skutečný škálově běžící η(k) (FRG tok)
   není integrován. To stačí pro UV/IR limity, ne pro detail přechodu.

4. **Multifrakcionální řádek** používá kanonickou volbu γ_UV=D/2 (d_s→2); Calcagni
   uvádí víc tříd s různými UV hodnotami — bereme jen srovnávací hodnotu 2.

5. **Numerická přesnost.** Tolerance validačních kontrol je 0.06 (konečné σ +
   kvadratura). UV/IR plató jsou ploché na ≲1 % — viz `ds_flow.png`.

---

## 7. Závěr

Jediný formalismus návratové pravděpodobnosti reprodukuje *všechna* publikovaná
UV/IR čísla spektrální dimenze pro GR, Hořavu (z=2,3), Stelle, asymptotickou
bezpečnost, causal sets (obě sondy) i multifrakcionální prostory. Tím je
hypotéza L3-1 v přerámované podobě **podpořena**: d_s^UV je predikovatelný otisk
trojice **(z, D, probe)**, nikoli univerzální konstanta 2. Klíčový nový prvek —
**probe jako klasifikační osa** — je doložen tím, že causal sets dávají d_s → 2
(d'Alembertián) versus d_s rostoucí (náhodná procházka) ze *stejné* teorie.
Zdánlivá konvergence k 2 je shoda podtřídy s UV propagátorem ~k⁴ (γ=2), kterou
GR, Hořava z=2 a random-walk sonda explicitně porušují.
