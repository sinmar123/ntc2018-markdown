# Scarti Markdown vs fonte concordata — e correzioni

- Base Markdown: snapshot pre-audit `markdown/8-esistenti-SNAPSHOT-pre-correzioni-20260716.md` (SHA-256 `9d2334c0…b2ef9c0`, identico al `cap08/8-esistenti.md` congelato). Numeri di riga riferiti allo snapshot.
- Fonte concordata: `diff/riconciliazione-A-B.md` (A+B adjudicati sui render).
- Le correzioni sono APPLICATE alla copia `diff/8-esistenti-POST-correzioni-proposto.md`; il file vivo `cap08/8-esistenti.md` è assente dal filesystem (v. registro §1.1) e va sostituito/riallineato al ripristino del progetto.

## 1. ERR-MD — difformità dal PDF, da correggere (14)

| # | Unità | Riga | Markdown (pre) | Fonte concordata | Correzione applicata alla copia |
|---|---|---|---|---|---|
| E1 | C8.5.3.1/T1 | 388 | legenda SENZA le due parentetiche dopo le definizioni di $\tau_0$ e $f_{v0}$ | dopo ciascuna delle due definizioni: "(con riferimento alla formula riportata, a proposito dei modelli di capacità, nel §C8.7.1.3)" | inserite entrambe le parentetiche |
| E2 | C8.5.3.1/T1 | 399 | `(es.: doppio UNI foratura ≤40%)` | `(es,: doppio UNI foratura ≤40%)` (refuso della fonte, da conservare) | `es.:` → `es,:` |
| E3 | C8.5.3.1/T1 | 401 | `i contatti ed aumentano` | `i contatti e aumentano` | `ed` → `e` |
| E4 | C8.5.3.1/T2 | 426 | intestazione senza le fasce di gruppo | fascia `Stato di fatto` su colonne 1-3 dati; fascia `Interventi di consolidamento` su colonne 4-7 dati (inclusa `Massimo coefficiente complessivo`) | percorsi di colonna espliciti `<Fascia> / <Etichetta>` (normalizzazione prevista dal protocollo §7 per intestazioni gerarchiche) |
| E5 | C8.5.3.1/T2 | 431 | `(tufo, calcarenite, ecc.)` | `(tufo, calcarenite, ecc.,)` (refuso fonte, da conservare; nel MD era conservato in C8.5.I ma non in C8.5.II) | `ecc.)` → `ecc.,)` |
| E6 | C8.5.3.1/T2 | 432 | `(tufo, calcarenite, ecc.)` | `(tufo, calcarenite, ecc.,)` | `ecc.)` → `ecc.,)` |
| E7 | C8.5.3.1/T2 | 435 | `(es.: doppio UNI foratura ≤40%)` | `(es,: doppio UNI foratura ≤40%)` | `es.:` → `es,:` |
| E8 | C8.5.3.1/T2 | 441 | `$f_m^{0{,}35}$` | esponente stampato `0.35` con PUNTO decimale (incoerenza tipografica della fonte, da conservare) | `$f_m^{0{,}35}$` → `$f_m^{0.35}$` |
| E9 | C8.5.4.1/F | 483 | `dei parametri μ’ e V’` | `dei parametri μ′ e σ′` (sigma primo; il `V` era residuo di text layer corrotto) | `V’` → `σ’` |
| E10 | C8.5.4.1/F | 502 | `dove { è la media` | `dove X̄ è la media` | `{` → `X̄` |
| E11 | C8.5.4.1/F | 502 | `prove dirette e è un coefficiente` | `prove dirette e κ è un coefficiente` | inserita `κ` |
| E12 | C8.5.4.1/F | 502 | `la varianza V’2 della distribuzione` | `la varianza σ′² della distribuzione` (2 in apice) | `V’2` → `σ’²` |
| E13 | C8.5.4.1/F | 502 | `il coefficiente rappresenta il peso` | `il coefficiente κ rappresenta il peso` | inserita `κ` |
| E14 | C8.5.4.1/F | 502 | `prove dirette { sia significativamente` | `prove dirette X̄ sia significativamente` | `{` → `X̄` |

Nota sulle E9-E14: nella copia corretta si conserva lo stile tipografico già in uso nel file (greche unicode in prosa, apostrofo tipografico `’` come segno di primo), limitando l'intervento alla sostanza semantica.

## 2. NORM — normalizzazioni Markdown documentate e accettate (nessuna correzione)

1. T1: intestazione a 2 righe della fonte compattata su 1 riga MD con `min-max` nel titolo di colonna (solo per f, τ0, E, G, come in fonte).
2. T1: doppio trattino sovrapposto nelle celle fv0 righe 1-4 (artificio tipografico) reso con `-` singolo.
3. T1: cella w fusa sulle righe 4-5 espansa ripetendo `13 ÷ 16 (**)` in entrambe le celle logiche (accorpamento registrato nel manifest); spazio MD prima di `(**)` dove la fonte stampa `16(**)` attaccato.
4. T1+T2: didascalia unica in corsivo della fonte resa come didascalia in grassetto + capoverso legenda (convenzione del corpus).
5. T2: etichette di colonna ruotate di 90° nella fonte: rotazione non riproducibile in Markdown (contenuto integrale conservato).
6. T2: `Intonacoarmato` stampato attaccato (anche nel text layer) reso `Intonaco armato (**)`; analoghi kerning di stampa `fpuò` (T1 nota **), `³Dalla`, `κper` (nota 3), `κsuggeriti` (didascalia C.8.5.III) resi con spazio.
7. T2 nota (***): virgolette tipografiche curve di "malta buona" rese con virgolette dritte.
8. F: nota 3 a piè di pagina resa come nota locale `**Nota 3.** …` con richiamo `[3]` (convenzione del corpus del 2026-06-18) in luogo dell'apice `³`.
9. F: LaTeX — `\frac{1}{2}` per la frazione impilata, `\left(\right)`, `\overline{X}`; grassetto delle formule [C8.5.4.1]-[C8.5.4.2] non riprodotto (peso font, non semantico); corsivi di prosa dei simboli latini (X, n) non marcati nel MD.

## 3. AF — anomalie della fonte conservate fedelmente (nessuna correzione; non "aggiustare" mai)

1. Legenda T1: definizioni di τ0 e fv0 IDENTICHE parola per parola (doppia parentetica §C8.7.1.3) — con E1 il MD le conserva entrambe.
2. `(es,: doppio UNI foratura ≤40%)` con virgola dopo `es` (T1 riga 8 e T2 riga 8) — conservato con E2/E7.
3. `ecc.,)` con virgola dopo il punto (T1 righe 4-5; T2 righe 4-5) — conservato (T1 già conforme; T2 con E5/E6).
4. Esponente `0.35` con punto decimale nella nota (***) di T2 — conservato con E8.
5. `C8..5.4.3` con due punti consecutivi ("Qualora…") — già conservato nel MD.
6. Numerazione incoerente della fonte: `Tabella C.8.5.I` / `tabella C.8.5.I` / `Tabella C.8.5.III` (punto dopo C) contro `C8.5.I`/`[C8.5.4.x]`/`§C8.7.1.3` (senza punto) — già conservata nel MD.
7. Fascia `Interventi di consolidamento` che copre anche la colonna `Massimo coefficiente complessivo` — riprodotta con E4.
8. Richiami di nota presenti nelle etichette di riga solo in T1 (righe 2, 5, 7) e non in T2 — già conforme.
9. Trattini singoli in T2 contro doppio trattino tipografico in T1/fv0 — resi entrambi `-` (v. NORM 2).

## 4. Elementi verificati CONFORMI senza intervento (campione principale)

- Tutte le 104 celle numeriche dati di T1+T2 (valori, separatori decimali a virgola, intervalli col trattino, `2` intero, `2,0` con decimale, `(***)`, `1,3 (****)`, trattini singoli).
- Le tre formule [C8.5.4.1]-[C8.5.4.3]: LaTeX MD conforme al concordato (tag inclusi), confronto visivo render MD vs ritaglio PDF superato.
- Frase LC3 (salvo E9), frase ponte, paragrafo definizioni (salvo E10-E14), nota 3, richiamo `[C8.5.4.3]` nella didascalia C.8.5.III.
- `13 ÷ 16 (**)` con `÷` (unico separatore `÷` della tabella), `≤40%`, `> 70 cm`, `a-priori`/`a-posteriori`, `sperimentali[3]` (convenzione), `C8..5.4.3`.

Firma: confronto concordato-vs-Markdown — Claude Code (CC), Fable 5, 2026-07-16.
