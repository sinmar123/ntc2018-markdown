# Consegna al verificatore: G7 tentativo 2, scope § 8.7.3 / C8.7.3

Sei il verificatore critico indipendente del G7 previsto dal § 9 della procedura VC-NTC/10 (firma: CDX, Codex gpt-6.1-sol). Non hai scritto la lista, le correzioni, il verbale o il piano di registrazione e non coordini lo scope. Lavora soltanto sui file di questa cartella: non aprire altre cartelle, il workspace, il repository o internet, e non usare strumenti di controllo del computer o del browser. Non modificare né creare file: la tua risposta finale è il giudizio JSON descritto in fondo, e nient'altro.

Il G7 è una riconciliazione documentale sull'intero scope, in un solo passaggio: non rileggere la fonte normativa e non ripetere il confronto del G6. Controlla che verbale, piano di registrazione e riepiloghi meccanici concordino con le attestazioni conservate, che la catena degli hash sia chiusa e che non resti alcun rilievo aperto.

## Tentativo 1 e rettifiche

Il G7 tentativo 1 (`G7-tentativo-1-KO.json`) è stato `KO` per due `ERR-AUDIT` documentali: G7-AUDIT-01, `sequenza-g6.json` riportava «non letto» per i modelli del G6 tentativo 2 mentre verbale e scheda dicevano gpt-5.6-terra letto nel log (causa: log UTF-16 letti come UTF-8 dallo script di C); G7-AUDIT-02, il verbale non riportava gli URL degli atti e il ricontrollo G1 ne dava solo un modello. Sandro ha approvato le rettifiche: `rettifica-g7-audit-01-20261022.json` (modelli e token riletti dai log, con le impronte dei log; i file `sequenza-g6*.json` non sono riscritti), URL nel verbale e campi `url_consultati` e `url_eli` aggiunti a `ricontrollo-g1-20261022.json`; manifest e verbale rigenerati, manifest del tentativo 1 conservato come `manifest-rilascio-g7-tentativo-1.json`. Controlla che le due rettifiche chiudano i rilievi e che non abbiano cambiato target, copertura o giudizi.

## Regole del ciclo VC che valgono qui

- La procedura è `procedura-congelata-r10.md` (VC-NTC/10): G7 solo con G6 a zero `ERR-MD`, zero `ERR-AUDIT`, zero `DUBBIO`; il verificatore è distinto da chi ha scritto e applicato le correzioni (C = GBOT-verifica-ntc).
- Le normalizzazioni ammesse sono solo quelle di `catalogo-congelato.md`; nessuno scostamento silenzioso dalla fonte, nessun dato inventato.
- `max_giri` non si alza; `giro_g6` resta 1 per il recupero sullo stesso snapshot (§ 8); un errore solo documentale si rettifica senza nuovo G6 (§ 8).
- `VC-OK` solo per la riga 8.7.3 e solo con tutti i gate `OK` e nessun rilievo aperto; nessuna promozione di altre righe.
- Nessun dato personale e nessun percorso assoluto della macchina nei file del dossier.

## File

- `procedura-congelata-r10.md`: la procedura (§§ 7, 8 e 9 per questo controllo); `catalogo-congelato.md`: il catalogo delle normalizzazioni.
- `verbale.md`: verbale proposto (`verifica-conformita/verbale-VC-ntc2018-8.7.3-2026-10-22.md`).
- `scheda.md`: scheda dello scope prima della chiusura.
- `chiusura.json`: piano di registrazione per `vc-supporto.py registra`. Il campo `g7_sha256` vale `DA_COMPILARE_DOPO_IL_G7`: dopo il tuo giudizio C vi scrive soltanto l'impronta di `G7.json`, senza altre modifiche.
- `manifest-rilascio.json` e `riepilogo-meccanico.json`: manifest dei file usati e riepilogo prodotto dagli script (impronte, `verifica-manifest`, `verifica-lista`, `valida-g6`, lint del registro, riga CSV attuale, impronte dei file di questa cartella).
- Rettifica: `G7-tentativo-1-KO.json`, `rettifica-g7-audit-01-20261022.json`, `manifest-rilascio-g7-tentativo-1.json`.
- Attestazioni: `ricontrollo-g1-20261022.json` (vigenza), `decisione-applicazione-20261022.json` (lista v1 approvata e applicata), `mappa-g5.json` (G5), `decisione-g6-20261022.json` (annullamento del tentativo 1 del G6), `sequenza-g6-tentativo-1-annullato.json` ed `esito-g6-tentativo-1-annullato.json` (tentativo annullato), `sequenza-g6.json`, `esito-g6.json`, `inventario-g6-b01.json`, `rapporto-g6-b01.json` (G6 integrale giro 1, tentativo 2), `decisione-g6-rilievo-20261022.json` (decisione di Sandro sull'unico rilievo), `prova-NTC-873-CONDIZIONE.json` e `ntc298-per-queste-600dpi.png` (prova di C su quel rilievo).

## Che cosa controllare

1. Copertura: il G6 integrale del tentativo 2 copre tutto il testo dello scope (un blocco, 6 ID) e `valida-g6` è OK.
2. Tentativo 1: l'annullamento è deciso da Sandro, motivato (modello della fase 2 diverso da quello previsto, rilievo documentale sull'inventario) e registrato; il tentativo resta conservato e non è usato come copertura; `giro_g6` resta 1 come previsto dal § 8 per il recupero sullo stesso snapshot.
3. Rilievi: l'unico rilievo del tentativo 2 è chiuso senza modifiche per decisione di Sandro, con prova registrata. Nessun rilievo aperto.
4. Snapshot: l'impronta del target nel manifest, nel verbale, nella scheda, nella decisione di applicazione e nel riepilogo è la stessa.
5. Catena degli hash: impronte di manifest e verbale nel riepilogo, nel piano di registrazione (`manifest_sha256`, `verbale_sha256`); tutte le evidenze citate sono nel manifest; `verifica-manifest` OK; il G7 resta fuori dal manifest.
6. Verbale e scheda: riportano ruoli effettivi e modelli effettivi, natura AI senza revisione umana integrale, isolamento, scarti dichiarati, vigenza con due date, revisione di procedura e catalogo, normalizzazioni, anomalie, decisioni di Sandro con data e ora, `giro_g6` 1 su 3.
7. Piano di registrazione: aggiorna tutti e soli i file di governo previsti, con testo coerente con il verbale; la riga CSV attuale è `IN-CORSO`; procedura VC-NTC/10.

Se qualcosa non concorda, è un rilievo: classificalo `ERR-AUDIT` (documentale) o `DUBBIO`.

## Giudizio

Rispondi soltanto con un oggetto JSON valido, senza testo prima o dopo e senza blocchi di codice, con questi campi:

- `firma`: chi sei (modello e ruolo);
- `data`: "2026-10-22";
- `giudizio_g7`: "OK" o "KO";
- `scope`: "8.7.3";
- `snapshot_sha256`: l'impronta del target giudicato;
- `manifest_sha256`: l'impronta di `manifest-rilascio.json`;
- `gate`: oggetto con `G0`-`G7`, ciascuno "OK" o "KO";
- `rilievi_aperti`: elenco, vuoto se OK, di oggetti `id`, `classe`, `prova`;
- `motivazione`: in poche frasi;
- `letture`: elenco dei file letti;
- `limiti`: limiti del controllo, in una o due frasi.
