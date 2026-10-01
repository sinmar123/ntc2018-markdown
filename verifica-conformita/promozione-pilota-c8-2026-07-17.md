# Verbale di promozione e registrazione — Pilota C8 (lotti C8-T01 e C8-F01)

- Data: 2026-07-17. Autore: Claude Code (CC), modello Fable 5.
- Audit di riferimento: `audit-C8-T01-F01-20260716/registro.md` (VC8-G4-TF, eseguito il 2026-07-16 sui materiali congelati).
- Scope: `scope-pilota-c8-2026-07-16.md`. Manifest fonti: `manifest-fonti-2026-07-16.txt`.

## Catena di custodia verificata il 2026-07-17

Verifiche eseguite prima della registrazione degli esiti, dopo il ripristino
della cartella dall'incidente di sync del 16-17/7:

1. `raw/Circolare-7-2019-NTC.pdf` — SHA-256 riscontrato
   `f7c3b8d1f443aadb6b3e020b6b6c19813683492ecaadd2c15bf6bf1939aaed7c`:
   COINCIDE con il manifest fonti del congelamento.
2. `cap08/8-esistenti.md` (file vivo, dopo la promozione delle 14 correzioni
   ERR-MD avvenuta il 17/7 mattina) — SHA-256 riscontrato
   `612a2c00fafcd8619786b54a0b2c21df62dd37cf5153771b7cb71c744185b395`:
   COINCIDE bit per bit con la copia corretta prodotta e ricontrollata
   dall'audit (`diff/8-esistenti-POST-correzioni-proposto.md`, recheck 14/14
   di verificatore fresco). La riserva di promozione del §7 del registro di
   audit è quindi sciolta.

## Registrazione nel registro di dettaglio

`registro-dettaglio-verifica-ntc2018.csv`, aggiornato il 2026-07-17:

- **CIRC-C8.5.3.1** (perimetro TABELLE, gate G2|G4): verifica COMPLETA,
  esito **OK** — Tabelle C8.5.I-II, 100% delle celle logiche, 8 ERR-MD
  corrette e promosse.
- **CIRC-C8.5.4.1** (perimetro FORMULE, gate G2|G4): verifica COMPLETA,
  esito **OK** — formule [C8.5.4.1-3] conformi, 6 ERR-MD nelle definizioni
  corrette e promosse.
- Revisore A: Claude Code (CC), Fable 5. Revisore B: subagente Claude (Opus)
  a contesto pulito. Riconciliatore/convalidatore: Claude Code (CC), Fable 5.
  Nessuna revisione umana integrale inclusa.

Lint `strumenti/lint-registro-dettaglio.py` eseguito dopo l'aggiornamento:
**0 errori, 0 avvisi, 0 info** su 1.724 righe.

## Validità e limiti

- Gli esiti OK valgono per i perimetri dichiarati (TABELLE e FORMULE delle
  unità indicate) e per lo snapshot del manifest fonti 2026-07-16. Ogni
  modifica successiva a `cap08/8-esistenti.md` nelle porzioni in scope rende
  gli esiti da riverificare (hash di riferimento `612a2c00…`).
- Gli esiti alimentano i gate G2/G4 del registro master, che resta
  `VC-DA-FARE` a livello di corpus: il pilota copre 2 unità su 1.724.

## Evidenze finali

Copiate da `_tmp_render/cap08/conformita-tabelle-formule-20260716-r01/` in
`audit-C8-T01-F01-20260716/`: `registro.md`, `manifest.csv`,
`riconciliazione-A-B.md`, `scarti-md-vs-fonte.md`, `dettaglio-celle.csv`,
`dettaglio-formule.csv`. Render, ritagli e lavorazioni intermedie restano in
`_tmp_render/` (eliminabili secondo protocollo, esiti ormai verbalizzati).

## Prossimi lotti proposti (dal §8 del registro di audit)

- **C8-T02**: Tabelle C.8.5.III e C8.5.IV.
- **C8-F02**: successive ~10 formule esposte del Capitolo 8.
- Lotto dedicato di fedeltà prosa per le righe md 407-422 (simboli
  deteriorati già segnalati nello scope).
- Dopo C8: Capitolo 7 (mismatch noto formula 7.9.4).
