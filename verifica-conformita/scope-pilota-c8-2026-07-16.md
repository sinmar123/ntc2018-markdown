# Scope congelato — Pilota C8, lotti C8-T01 e C8-F01

- Data congelamento: 2026-07-16
- Autore: Claude Code (CC)
- Protocollo: VC8-G4-TF (skill `controllo-serrato-ntc2018`, riferimento `protocollo-conformita-tabelle-formule.md` §13)
- Fonte: `raw/Circolare-7-2019-NTC.pdf` — SHA-256 `f7c3b8d1f443aadb6b3e020b6b6c19813683492ecaadd2c15bf6bf1939aaed7c` (vedi `manifest-fonti-2026-07-16.txt`)
- Markdown di destinazione: `cap08/8-esistenti.md` — SHA-256 pre-audit `9d2334c028ef25c483246216033da432d8064127c4dc38f4ea30eea10b2ef9c0`
- Registro di dettaglio: `registro-dettaglio-verifica-ntc2018.csv` (separatore `;`, UTF-8 BOM)

## Lotto C8-T01 — Tabelle

Unità di registro: **CIRC-C8.5.3.1** (riga `id=CIRC-C8.5.3.1`, paragrafo C8.5.3.1 "Costruzioni di muratura", `perimetro_verifica_unita=TABELLE`, `gate_master=G2|G4`).

| Apparato | Pagina PDF | Pagina GU | Posizione Markdown (pre-audit) | Contenuto |
|---|---|---|---|---|
| Tabella C8.5.I | 261 | 257 | `cap08/8-esistenti.md` righe 386-405 | didascalia+legenda (f, τ0, fv0, E, G, w), intestazione a 2 righe (min-max), 8 righe di dati × 6 colonne, note (*) (**) (***) |
| Tabella C8.5.II | 262 | 258 | `cap08/8-esistenti.md` righe 424-443 | didascalia, intestazione a 2 livelli (gruppi "Stato di fatto" / "Interventi di consolidamento", colonne ruotate), 8 righe × 7 colonne, note (*) (**) (***) (****) |

Il perimetro comprende, per ciascuna tabella: didascalia e legenda, intestazioni (compresa la gerarchia dei gruppi), tutte le celle logiche (incluse celle accorpate ed espansioni), richiami e note a piè di tabella. NON comprende la prosa circostante del §C8.5.3.1.

## Lotto C8-F01 — Formule

Unità di registro: **CIRC-C8.5.4.1** (riga `id=CIRC-C8.5.4.1`, paragrafo C8.5.4.1 "Costruzioni di muratura", `perimetro_verifica_unita=FORMULE`, `gate_master=G2|G4`).

| Apparato | Pagina PDF | Pagina GU | Posizione Markdown (pre-audit) | Contenuto |
|---|---|---|---|---|
| Formula [C8.5.4.1] | 266 | 262 | `cap08/8-esistenti.md` righe 485-488 | μ′ = ½(X_min + X_max) |
| Formula [C8.5.4.2] | 266 | 262 | righe 490-493 | σ′ = ½(X_max − X_min) |
| Formula [C8.5.4.3] | 266 | 262 | righe 497-500 | μ″ = (nX̄ + κμ′)/(n + κ) |
| Frase introduttiva LC3 e frase ponte | 266 | 262 | righe 483, 495 | definizioni di X, μ′, σ′ e condizioni di applicazione |
| Paragrafo definizioni ("dove ...") | 266 | 262 | riga 502 | definizioni di X̄, κ, σ′² + frasi "Nel determinare..." e "Qualora..." |
| Nota 3 a piè di pagina | 266 | 262 | riga 504 | testo integrale della nota richiamata da "sperimentali³" |
| Richiamo alla Tabella C.8.5.III | 266 | 262 | righe 502-506 | SOLO il richiamo (in nota 3 e in didascalia) per quanto direttamente collegato all'apparato; il contenuto cella per cella della Tabella C.8.5.III è FUORI lotto (andrà nel lotto tabelle successivo) |

## Esclusioni esplicite

- Prosa dei §§ C8.5.3.1 e C8.5.4.1 fuori dagli apparati elencati (in particolare i capoversi con i simboli deteriorati "(f, W e fv0)" ecc., righe md 407-422: segnalati come candidato lotto futuro di fedeltà prosa).
- Tabella C.8.5.III, C8.5.IV, C8.5.V, C8.5.VI, C8.7.6.3.I, C8.7.6.3.II (lotti tabelle successivi).
- Le altre 44 formule esposte C8 (lotti formule successivi).

## Audit collegato

`_tmp_render/cap08/conformita-tabelle-formule-20260716-r01/` — doppio passaggio indipendente:
- A: Claude Code (CC), Fable 5 — estrazione testuale PyMuPDF + conferma visiva su render 432 dpi;
- B: subagente a contesto pulito, modello Opus — lettura visiva dei render, senza accesso al Markdown né al passaggio A.
