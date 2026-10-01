# Scope congelato — Lotto C8-T02 (Tabelle C.8.5.III e C8.5.IV)

- Data congelamento: 2026-07-17. Autore: Claude Code (CC), modello Fable 5.
- Protocollo: VC8-G4-TF (skill `controllo-serrato-ntc2018`, protocollo di conformità tabelle e formule).
- Cartella audit: `_tmp_render/cap08/conformita-tabelle-formule-20260717-r01/`.
- Lotto proposto dal §8 del registro di audit del pilota (C8-T01/F01, chiuso il 17/7).

## Fonti congelate (hash riscontrati il 2026-07-17)

- `raw/Circolare-7-2019-NTC.pdf` — SHA-256
  `f7c3b8d1f443aadb6b3e020b6b6c19813683492ecaadd2c15bf6bf1939aaed7c`
  (348 pagine; identico al manifest fonti del pilota 2026-07-16).
- `cap08/8-esistenti.md` — SHA-256
  `612a2c00fafcd8619786b54a0b2c21df62dd37cf5153771b7cb71c744185b395`
  (snapshot POST-promozione delle 14 correzioni del pilota; nuovo snapshot
  rispetto al manifest 2026-07-16, come previsto dal protocollo §3).

## Perimetro

1. **Tabella C.8.5.III** (grafia della fonte con punto dopo la C) — pagina PDF
   266, pagina stampata GU 262, dentro §C8.5.4.1: didascalia, intestazioni
   (Metodo di prova, Parametro, κ), 10 righe logiche con accorpamenti nella
   colonna Metodo, note (*) e (**) a corredo. Markdown: `cap08/8-esistenti.md`
   righe 506-523.
2. **Tabella C8.5.IV** — pagina PDF 267, pagina stampata GU 263, dentro
   §C8.5.4.2: didascalia, 6 colonne (Livello di conoscenza, Geometrie
   (carpenterie), Dettagli strutturali, Proprietà dei materiali, Metodi di
   analisi, FC (*)), 3 righe logiche LC1-LC3 con colonna Geometrie in cella
   unica accorpata, nota (*). Markdown: righe 531-539.

## Esclusioni dichiarate

- Prosa dei §§C8.5.4.1-C8.5.4.2 (formule e definizioni C8.5.4.1-3 già coperte
  dal lotto C8-F01; definizioni estese LC1-LC3 per c.a./acciaio fuori lotto).
- Nota 3 a piè di pagina 266 (già verificata nel pilota; qui solo contesto).
- Pagina PDF 268: contiene un solo richiamo testuale alla Tabella C8.5.IV,
  nessun apparato in scope.
- Anomalie strutturali note ADIACENTI allo scope, registrate come rilievi
  collaterali ma fuori perimetro tabellare: heading H2 spurio
  "## C8.5. Definizione del modello di riferimento per le analisi" (md riga
  529, probabile intestazione di pagina catturata) e seconda occorrenza
  dell'heading "#### C8.5.3.2." (md riga 543, testo del paragrafo spezzato,
  rilievo già censito nel registro di dettaglio su CIRC-C8.5.3.2).

## Metodo

Doppio passaggio indipendente A/B su soli render (pagine intere zoom 4,
ritagli zoom 6, super-zoom zoom 8), riconciliazione sul render della fonte,
confronto col Markdown vivo, correzioni con recheck. Verificatore A: subagente
Claude (Fable 5) a contesto pulito. Verificatore B: subagente Claude (Opus) a
contesto pulito — modelli diversi. Riconciliatore: Claude Code (CC, Fable 5).
