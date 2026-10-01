---
scope_id: ntc2018-3.2.1
data: 2026-08-28
stato: VC-OK
markdown_sha256: d63652647c796ab4b473827eb35d285529f7041fd3e04ff9e0caa480d6ee7d20
fonte_ntc_sha256: dda1e397d56d71aa0f5bc457c3ba9b77064a468699dfc37bd056ac6c47105a46
fonte_circolare_sha256: f7c3b8d1f443aadb6b3e020b6b6c19813683492ecaadd2c15bf6bf1939aaed7c
---

# Verbale di verifica di conformità - NTC 2018 § 3.2.1 e Circolare C3.2.1

## Perimetro

Il controllo riguarda esclusivamente `cap03/3.2.1-azione-sismica-stati-limite-e-relative-probabilita-di-superamento.md`, corrispondente al § 3.2.1 dell'allegato al D.M. 17 gennaio 2018 e al § C3.2.1 della Circolare 21 gennaio 2019 n. 7.

Le fonti occupano le pagine fisiche NTC 49-50 e Circolare 48-50. Inventario integrale finale: 2 rubriche, 27 capoversi source-first, 2 elenchi con 4 voci, 3 tabelle con 78 posizioni logiche e 11 accorpamenti, 4 formule numerate, 8 relazioni inline o non numerate, 2 note e una figura con un asset.

## Fonti e vigenza

- D.M. 17 gennaio 2018: `verifica-conformita/fonte-ufficiale/GU-2018-42-SO8-DM-17-01-2018.pdf`, SHA-256 `dda1e397d56d71aa0f5bc457c3ba9b77064a468699dfc37bd056ac6c47105a46`.
- Circolare 21 gennaio 2019 n. 7: `verifica-conformita/fonte-ufficiale/GU-2019-35-SO5-Circolare-7-2019.pdf`, SHA-256 `f7c3b8d1f443aadb6b3e020b6b6c19813683492ecaadd2c15bf6bf1939aaed7c`.

La ricognizione sulle fonti ufficiali al 2026-08-28 non ha individuato modifiche o sostituzioni del § 3.2.1 o del § C3.2.1. Il D.M. 9 marzo 2023 non incide sul perimetro.

## Gate

- G0 `OK`: identità, file e confini accertati direttamente sulle cinque pagine.
- G1 `OK`: fonti ufficiali identificate, hash ricalcolati e vigenza verificata.
- G2 `OK`: inventario source-first e confronto testuale integrale completati.
- G3 `OK`: glifi protetti, note, percentuali, apici, pedici, operatori e disuguaglianze verificati sui ritagli a 600 dpi.
- G4 `OK`: 3 tabelle, 4 formule numerate, relazioni matematiche e figura ricostruite e riconciliate in due passaggi indipendenti.
- G5 `OK`: render finale di 4 pagine, collegamenti, asset e apparati di navigazione verificati; 311 file e 1.754 collegamenti interni conformi.
- G6 `OK`: terzo giro cieco integralmente controllato e adjudicato; 0 `ERR-MD`, 0 `ERR-AUDIT` aperti e 0 `DUBBIO`.
- G7 `OK`: precontrollo P0-D Moon e controllo finale P2 Sol hanno confermato 16/16 hash e 16/16 dimensioni del manifest.

## Scarti e correzioni

Nel preflight sono stati corretti gli scostamenti testuali e strutturali accertati: congiunzioni, ordine di parole, omissione di `definendo`, cassa e punteggiatura delle rubriche, richiamo e testo della nota 2, denominazione `Figura`, struttura delle tabelle, catena completa della formula `[C.3.2.3]` e asset grafico mancante. Le testate non stampate o completate per inferenza sono state rimosse; le celle accorpate sono rese in forma logica interrogabile secondo la normalizzazione dichiarata.

Il G6 R01 ha rilevato e fatto correggere due ulteriori scostamenti: `ed un esiguo` nella voce SLC delle NTC e il separatore `–` dopo `(SLD)` nella prosa della Circolare. Il G6 R02 ha rilevato e fatto ripristinare le parentesi quadre attorno alla relazione del capoverso `È immediato constatare`.

Il G6 R03 aveva infine segnalato soltanto il separatore `-` della didascalia `Tab. 3.2.I`. Sandro ha stabilito il 28 agosto 2026 che `-`, `–` e `—` sono equivalenti nei separatori fra numero e testo delle didascalie. La normalizzazione dichiarata n. 10 è stata aggiornata e il rilievo è stato riclassificato `NORM`, senza modificare il Markdown e senza necessità di un quarto G6.

Nessuna cifra, coefficiente, esponente, apice, pedice, operatore, segno, verso di disuguaglianza o unità è stata modificata fuori dalla corrispondenza attestata dalla fonte.

## Anomalie della fonte

Sono conservate alla lettera tre famiglie di anomalie, per sei occorrenze complessive:

- tre sottotestate `$C_U =$` prive del valore nella Tabella C.3.2.II;
- una testata con `$T_r$` minuscolo nella stessa tabella;
- due legende raster `Cu=1,5` e `Cu=2,0` nella Figura C3.2.2.

Classificazione: 3 `AF` chiuse, 0 `AF-COR`. Nessun valore mancante è stato integrato per inferenza e l'asset conserva la grafia della fonte.

## G6, G7 e indipendenza

Sono stati svolti tre giri G6 integrali:

- R01 `KO`: 2 `ERR-MD`, poi corretti separatamente;
- R02 `KO`: 1 `ERR-MD`, poi corretto separatamente;
- R03 storico `KO`: 1 rilievo sul separatore della didascalia, successivamente riclassificato `NORM` per decisione di indirizzo di Sandro.

Il rapporto R03 resta immutato come evidenza storica. L'adjudicazione P2 chiude G6 `OK` sullo stesso snapshot, con zero rilievi aperti; non occorrono né una patch né G6 R04.

I giri G6 hanno usato contesti freschi P2 `gpt-5.6-sol/xhigh`, con inventario source-first e confronto integrale separati. Il G7 ha usato il profilo semplificato P0-D `gpt-5.6-luna/medium` per il precontrollo deterministico e un contesto fresco P2 `gpt-5.6-sol/xhigh` per il giudizio finale.

L'aggiornamento della normalizzazione n. 10 non invalida i quattro scope `VC-OK` precedenti: ciascun giudizio resta legato al proprio snapshot, al vecchio hash della normalizzazione e alla copia congelata nel relativo pacchetto; nessun testo normativo già rilasciato è cambiato.

I controlli sono stati eseguiti da agenti AI; non è inclusa una revisione umana integrale.

## Snapshot ed evidenze

Snapshot iniziale Markdown: `2926375cb07790a4faeb0cef7704fdec2f10c7477467ec629e24bd8d2a168e8f`.

Snapshot finale verificato: `d63652647c796ab4b473827eb35d285529f7041fd3e04ff9e0caa480d6ee7d20`.

Frammento normativo finale depurato dagli apparati: `64dc3f5af326f95612099b53703bea0dd47a10ccac9fb7ebf5104b910ccddb55`.

Render finale: `566508695dcb29d0f63e679e5c8622bfeb9eb588ff69bfd75713cadbec272a6d`.

Evidenze principali:

- `_tmp_render/cap03/vc-3.2.1-20260828/preflight/rapporto-consolidato-g0-g5.md`;
- i cinque ritagli di scope a 600 dpi in `_tmp_render/cap03/vc-3.2.1-20260828/g6-r01/preparazione/fonte/`;
- `_tmp_render/cap03/vc-3.2.1-20260828/preflight/render-scope.pdf`;
- `_tmp_render/cap03/vc-3.2.1-20260828/apparati/riconciliazione/registro-finale-precorrezione.md`;
- i rapporti consolidati in `_tmp_render/cap03/vc-3.2.1-20260828/g6-r01/`, `g6-r02/` e `g6-r03/`;
- `_tmp_render/cap03/vc-3.2.1-20260828/g6-r03/adjudicazione-post-g6.md`;
- i rapporti G7 in `_tmp_render/cap03/vc-3.2.1-20260828/g7/`;
- `cap03/annotazioni/3.2.1-anomalie-fonte.md`;
- `verifica-conformita/manifest-sha256-ntc2018-3.2.1-2026-08-28.txt`.

## Rilascio

Il precontrollo P0-D `gpt-5.6-luna/medium` e il controllo finale P2 `gpt-5.6-sol/xhigh` hanno ricalcolato e confermato le 16/16 voci del manifest. SHA-256 del manifest: `44610911c7f23af83773c112990b4406a2f5911239fea08e6e752bc2329b4b51`.

Tutti i gate G0-G7 sono `OK` e non restano rilievi aperti o persistenti. Lo scope è promosso localmente a `VC-OK al 2026-08-28`; il giudizio vale soltanto per lo snapshot e il perimetro dichiarati.

Firma della redazione: CDX (Codex).
