# Registro audit lotto C8-T04 — Tabella C8.7.6.3.I

## Perimetro e snapshot

- **Apparato**: Tabella C8.7.6.3.I "Raccomandazioni per la valutazione e l'adeguamento di componenti non strutturali esistenti e per l'ancoraggio di componenti non strutturali di nuova installazione al variare della zona sismica" — multipagina, pp. file PDF 297-298 (pp. stampate G.U. 293-294). Perimetro: didascalia, testata, 9 righe-categoria, 30 righe dati (12 colonne logiche fonte), note a piè di tabella 5-8, richiamo (4).
- **Fonte**: `raw/Circolare-7-2019-NTC.pdf` — SHA-256 `f7c3b8d1f443aadb6b3e020b6b6c19813683492ecaadd2c15bf6bf1939aaed7c` (riverificato al rilancio).
- **Markdown**: `cap08/8-esistenti.md`, righe 1414-1455.
  - snapshot pre-correzioni: SHA-256 `0f3642961dc8f086a89138f1bc713f2083ff7c0b88f51fcf7e1dbc81f4f20d85`
  - snapshot post-correzioni E1-E4: SHA-256 `d4d4ee4145232206613336529169a14c15590a7aced6e5a1c1674d5b0f6a099a`
- Primo avvio del lotto (17/7 mattina) interrotto su richiesta di Sandro senza alcun output A/B: rilancio da zero il 17/7 pomeriggio riusando i soli render fonte (PDF invariato). Storia snapshot in `ambiente.txt`.

## Metodo

Protocollo `VC8-G4-TF` (skill `controllo-serrato-ntc2018`, riferimento `protocollo-conformita-tabelle-formule.md`): doppio passaggio indipendente su modelli diversi, alla cieca rispetto al Markdown e all'altro passaggio; riconciliazione e adjudicazione sul PDF da parte di CC; confronto meccanico cella per cella; correzioni promosse solo dopo adjudicazione; recheck fresco a contesto pulito.

- **Passaggio A**: agente AI, modello di sessione (Opus 4.8), 17/07/2026 ore 17:01 — `passaggio-a/trascrizione-tabI.md` (18 osservazioni).
- **Passaggio B**: agente AI, modello Sonnet, 17/07/2026 ore 17:03 — `passaggio-b/trascrizione-tabI.md` (13 osservazioni).
- **Confronto meccanico**: `diff/confronta-triplo.py` → `diff/confronto-triplo.csv` — 390 celle logiche (30 righe × 13 campi, colonna Categoria inclusa).
- **Arbitro (CC, modello di sessione)**: verifica visiva diretta su `zoom-p297-tabI-testata.png`, `crop-p298-tabI-parte2.png`, `pagina-296-intera.png`; scansione automatica delle note a piè pagina dell'intero capitolo C8 (PyMuPDF, blocchi a corpo minore in fondo pagina, pp. 249-299).

## Esito confronto A vs B

Concordanza piena su: didascalia, 6 intestazioni (4 singole + 2 gruppi), 9 righe-categoria, 30 righe dati con tutti i valori (300 celle zone comprese), punto di rottura multipagina (riga "…isolatori per le / vibrazioni" con testata ripetuta a p. 298), note 5-8 parola per parola, refusi di stampa della fonte.

Unica differenza: resa del richiamo di nota della categoria "Componenti fissati al pavimento o sul tetto" — A `(4)` a corpo pieno, B `⁽⁴⁾` in apice unicode. Stessa lettura (apice con parentesi, attaccato a "tetto"): adjudicata come differenza di trascrizione, non di contenuto.

## Difformità Markdown rilevate e correzioni promosse (ERR-MD)

| # | Posizione (md pre) | Fonte concordata | Markdown pre | Correzione |
|---|---|---|---|---|
| E1 | riga 1414, didascalia | nessun punto finale dopo "zona sismica" | punto finale presente | punto rimosso (stessa fattispecie del punto spurio didascalia C8.5.VI, lotto T03) |
| E2 | riga 1416, 4ª intestazione | `Costo & interruzione per l'adeguamento` (e commerciale) | `Costo e interruzione per l'adeguamento` | ripristinata `&` |
| E3 | righe 1446-1447, categoria | `Sostanze Pericolose` (doppia maiuscola, incoerenza di stile della fonte mantenuta fedelmente) | `Sostanze pericolose` | ripristinata la doppia maiuscola (2 occorrenze) |
| E4 | riga 1416, gruppo Valutazione | `Valutazione / adeguamento` (barra spaziata) | `Valutazione/adeguamento` | ripristinati gli spazi (4 occorrenze di testata) |

Tutte e quattro verificate visivamente dall'arbitro sulle immagini fonte prima della promozione. Dopo le correzioni il confronto meccanico dà **390/390 celle conformi** e nessuna difformità extra-matrice residua.

## Anomalie della fonte mantenute fedelmente (AF)

1. "Generatore della elettrico d'emergenza" — sgrammaticato nella stampa (verosimile omissione di "corrente").
2. "Aree con stoccaggio o uso di materiale pericolosi di tipo chimico, nucleare o biologico" — disaccordo singolare/plurale.
3. Nota 8: "il rapporto di ribaltamento è pari h_c / x_min" — manca "a" dopo "pari".
4. **Richiamo "(4)" orfano**: la riga-categoria "Componenti fissati al pavimento o sul tetto (4)" richiama una nota 4 che NON è stampata in nessuna pagina del capitolo C8 (scansione integrale dei piè di pagina pp. 249-299: esistono le note 1 a p. 255, 2 a p. 256, 3 a p. 266, 5-8 a p. 297; la 4 manca; p. 296 è priva di note). Refuso editoriale della Circolare: il richiamo resta nel Markdown, la nota non può essere trascritta perché non esiste.
5. Incoerenze tipografiche della fonte già rese fedelmente: "tra 1 e 1.6." con punto finale contro le voci gemelle senza; ">1.6"/">200 mm"/">100 mm" senza spazio contro "< 1" con spazio; separatore decimale anglosassone "1.6"; virgola seriale in "riscaldamento, ventilazione, e condizionamento"; "…>200 mm e su attacchi…" contro "…>100 mm e attacchi…"; stile del richiamo (4) con parentesi contro 5-8 senza parentesi.

## Normalizzazioni documentate (NORM)

1. 9 righe-categoria della fonte (celle uniche a piena larghezza) → colonna `Categoria` ripetuta su ogni riga dati (convenzione del 2026-06-11).
2. Intestazioni di gruppo su 4 colonne senza sotto-testate → percorsi di colonna espliciti "… - zona N".
3. Richiami di nota in apice → "(n)" a corpo pieno preceduto da spazio: "Vulnerabilità (5)", "nelle zone" → "(6)", "zone⁷ᵉ⁸" → "(7)(8)", "tetto⁽⁴⁾" → "tetto (4)".
4. Apostrofi e virgolette tipografici della fonte (' " ") → ASCII dritti (' ") nelle celle di tabella, coerente con la resa de facto dei lotti T01-T03.
5. Pedici tipografici della nota 8 → LaTeX (`$h_c / x_{min}$`).
6. Didascalia fonte (etichetta in grassetto + testo corsivo, senza punto) → didascalia tutta in grassetto (convenzione uniforme del file).
7. Tabella multipagina → tabella Markdown unica: testata ripetuta di p. 298 e riga fisica di continuazione "vibrazioni" (11 celle vuote) non replicate; la riga spezzata è riunita ("…montati su isolatori per le vibrazioni").

## Recheck fresco

Agente a contesto pulito (modello di sessione, Opus 4.8) su fonte prima e Markdown poi, 4 punti E1-E4 + giro di coerenza: esito in `recheck/recheck-tabI.md`.

**Esito: 4/4 CONFORME (E1, E2, E3, E4).** Nessuna difformità sostanziale al giro di coerenza. Due osservazioni non bloccanti: (a) la resa di apici e linearizzazioni è sistematica e coerente (coincide con le NORM 3-5 già documentate sopra); (b) le note (5)-(8) non sono state riverificate dal recheck per contenere i token su indicazione di Sandro a metà lavoro — restano coperte dalla concordanza A/B parola per parola e dal riscontro dell'arbitro sul piè di pagina 297 durante la scansione delle note del capitolo.

## Esito finale lotto

**Tabella C8.7.6.3.I CONFORME al 100% delle celle logiche** (390/390 al confronto meccanico post-correzioni) sullo snapshot `d4d4ee41…`, nel perimetro dichiarato: didascalia, testata (6 intestazioni), 9 righe-categoria, 30 righe dati, note a piè di tabella 5-8, richiamo (4). Correzioni E1-E4 promosse dopo adjudicazione e ricontrollate da verificatore fresco (4/4). Cinque anomalie della fonte censite e mantenute fedelmente, compreso il richiamo di nota (4) orfano nella fonte stessa. Restano fuori perimetro: la prosa del § C8.7.6.3 (lotto prosa) e la Tabella C8.7.6.3.II (lotto C8-T05, render pronti in `…-r04/`).

Conformità documentale della Tabella C8.7.6.3.I rispetto al PDF identificato nel manifest, verificata sul 100 per cento delle celle logiche con due passaggi indipendenti. Doppio controllo indipendente eseguito da agenti AI; nessuna revisione umana integrale inclusa nel presente audit.

---
Compilato da CC (Claude Code, modello di sessione Opus 4.8) — 17/07/2026. Doppio controllo indipendente eseguito da agenti AI; nessuna revisione umana integrale inclusa nel presente audit.
