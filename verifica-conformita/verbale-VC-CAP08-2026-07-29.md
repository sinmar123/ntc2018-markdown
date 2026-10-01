# Verbale di conformità VC-CAP08

Data: 2026-07-29

## Decisione

Si attribuisce:

> `VC-OK al 2026-07-29`

esclusivamente allo scope costituito dal Capitolo 8 del D.M. 17 gennaio 2018 e dal Capitolo C8 della Circolare 21 gennaio 2019 n. 7 C.S.LL.PP., rispetto alle fonti, alla ricognizione di vigenza e agli hash identificati nel presente verbale.

Il giudizio non si estende agli altri capitoli né all'intero corpus NTC 2018.

## Atti e scope

- D.M. 17 gennaio 2018, «Aggiornamento delle Norme tecniche per le costruzioni», Capitolo 8, pagine PDF 293-299.
- Circolare 21 gennaio 2019 n. 7 C.S.LL.PP., «Istruzioni per l'applicazione dell'Aggiornamento delle Norme tecniche per le costruzioni», Capitolo C8, pagine PDF 253-303.
- Pagine controllate: 58.
- Unità censite e chiuse: 20 NTC e 93 Circolare, 113 complessive.
- Sono compresi prosa, titoli, note, elenchi, formule numerate e non numerate, matematica inline, simboli, unità, tabelle, richiami, struttura e navigazione.
- File normativo: `cap08/8-esistenti.md`.
- File di navigazione: `cap08/indice-cap08.md`.
- Asset immagine collegati: nessuno.
- Scope formale: `verifica-conformita/scope-CAP08-2026-07-29.md`.

## Fonti ufficiali, acquisizione e vigenza

Ricognizione e acquisizione: 2026-07-29.

- Scheda ufficiale del D.M. 17 gennaio 2018: `https://www.gazzettaufficiale.it/atto/serie_generale/caricaDettaglioAtto/originario?atto.codiceRedazionale=18A00716&atto.dataPubblicazioneGazzetta=2018-02-20`
- PDF ufficiale del D.M.: `https://www.gazzettaufficiale.it/eli/gu/2018/02/20/42/so/8/sg/pdf/`
- Scheda ufficiale della Circolare 21 gennaio 2019 n. 7: `https://www.gazzettaufficiale.it/atto/serie_generale/caricaArticoloDefault/originario?atto.codiceRedazionale=19A00855&atto.dataPubblicazioneGazzetta=2019-02-11&atto.tipoProvvedimento=CIRCOLARE`
- PDF ufficiale della Circolare: `https://www.gazzettaufficiale.it/eli/gu/2019/02/11/35/so/5/sg/pdf`
- D.M. 9 marzo 2023, atto successivo controllato: `https://www.gazzettaufficiale.it/eli/id/2023/03/22/23A01847/sg`

Il D.M. 9 marzo 2023 modifica l'articolo 2 del D.M. 17 gennaio 2018 e riguarda temporaneamente i punti 11.4.2 e 11.5.2. Non incide sul Capitolo 8 né sul Capitolo C8. Nelle fonti ufficiali consultate non sono emerse modifiche successive che incidano sullo scope.

Lo scope è dichiarato vigente al 2026-07-29, nei limiti della ricognizione documentata. Non si fornisce garanzia per variazioni successive.

## Hash congelati

- PDF D.M. 17 gennaio 2018, 9.888.288 byte: SHA-256 `dda1e397d56d71aa0f5bc457c3ba9b77064a468699dfc37bd056ac6c47105a46`.
- PDF Circolare 21 gennaio 2019 n. 7, 50.658.045 byte: SHA-256 `f7c3b8d1f443aadb6b3e020b6b6c19813683492ecaadd2c15bf6bf1939aaed7c`.
- `cap08/8-esistenti.md`, 293.759 byte: SHA-256 `14457ad1b2f3a4931eb82dedfe64bda28367526761eb57e0392eb104b7fdf225`.
- `cap08/indice-cap08.md`, 5.403 byte: SHA-256 `5e550dd8f57f88255ab3235a58b9f0be4308d794e6e771b9007b2d4dfccae0b0`.
- Manifest dello scope: `verifica-conformita/manifest-sha256-CAP08-2026-07-29.txt`, SHA-256 `6071ee53c6b274ec7e64a918254944b3ce179d0cb747b181b4d00620215e58c8`.

Il manifest contiene quattro file, è stato validato rileggendo ogni file e confrontando hash e dimensione: 4/4 conformi.

## Esito dei gate

- G0, identità e scope: `OK`. Inventario source-first riconciliato con 113/113 righe `capitolo=08`.
- G1, fonte ufficiale e vigenza: `OK`. I due PDF acquisiti dagli URL ufficiali coincidono byte per byte con le copie congelate.
- G2, completezza: `OK`. Copertura visuale 58/58 pagine e presenza di tutte le unità e degli apparati censiti.
- G3, testo: `OK`. Sono stati adjudicati sul PDF visuale 186 scarti della Circolare e 9 NTC, 195/195 chiusi, con `ERR-MD=0` e `DUBBIO=0`.
- G4, apparati: `OK`. Controllate 49 formule numerate, 425 occorrenze matematiche inline, 8 tabelle con 611 celle dati e 50 intestazioni, 96 blocchi elenco; `ERR-MD=0`, `ERR-AUDIT=0`, `DUBBIO=0`.
- G5, struttura e navigazione: `OK`. Verificati heading, gerarchia, indice, link, assenza di asset mancanti e render integrale di 72 pagine senza pagine vuote o rotture semantiche.
- G6, seconda verifica indipendente: `OK`. Inventario congelato prima dell'apertura dello snapshot, 58/58 pagine, 8/8 tabelle, 49 formule numerate e 2 relazioni non numerate; `ERR-MD=0`, `ERR-AUDIT=0`, `DUBBIO=0`. Esito congelato SHA-256 `2f9403a74db0dba3847a443dd2f07b933da6943e3f70464f64b561ceaba006dd`; manifest G6 SHA-256 `92f6d05357a69fae393397b0abb8aeade333e44fddef6719bb949d775ba805cd`.
- G7, congelamento e manifest: `OK`. Hash dello scope invariati dopo G6, manifest validato 4/4 e presente questo verbale firmato.

Esito logico: `G0 AND G1 AND G2 AND G3 AND G4 AND G5 AND G6 AND G7 = OK`.

## Normalizzazioni e anomalie della fonte

È documentata una normalizzazione lecita: le due relazioni non numerate `q=mS_e(T)/F_y` e `m=Σm_iΦ_i`, graficamente isolate nella fonte a pagina PDF 301, sono rese inline nella frase introdotta da «dove:». Contenuto, simboli e funzione logica sono integri.

Sono state conservate senza correzioni interpretative alcune peculiarità o anomalie redazionali della fonte, fra cui:

- la didascalia `Tabella C.8.5.III`;
- il richiamo `C8..5.4.3`;
- la ripetizione «in questa in questa categoria»;
- il richiamo `(4)` nelle categorie della tabella C8.7.6.3.I, privo della corrispondente nota stampata nel capitolo;
- particolarità tipografiche come `0.35`, `M_{e.Rd}` e l'assenza di spazio nella sequenza `$V_j$indica`;
- l'esponente `-0,225` della formula [C8.7.2.1], verificato direttamente sulla fonte.

Questi elementi non costituiscono rilievi aperti contro il Markdown, perché riproducono la fonte ufficiale.

## Rilievi

Zero rilievi aperti nello scope:

- `ERR-MD`: 0;
- `ERR-AUDIT`: 0;
- `DUBBIO`: 0.

## Strumenti ed evidenze

Sono stati usati rendering raster delle pagine ufficiali, estrazione del text layer come solo ausilio, confronti tokenizzati e mappati, Pandoc, MathJax, Chrome/Edge headless, XeLaTeX, PyMuPDF e controlli Python su hash, struttura, tabelle, formule, link e manifest.

Evidenze primarie:

- `_tmp_render/cap08/vc-cap08-20260729-rilascio-vc-ok-r01/`;
- `_tmp_render/cap08/vc-cap08-20260729-g6-rilascio-finale-r01/`;
- `verifica-conformita/manifest-sha256-CAP08-2026-07-29.txt`.

## Revisori e natura del controllo

- Verificatore primario e coordinatore: Codex / CDX, agente AI.
- Passaggio G3: subagente Codex in contesto dedicato, agente AI.
- Passaggio G4: subagente Codex indipendente dal G3, agente AI.
- Verificatore G6: nuovo subagente Codex in contesto fresco e cieco, agente AI.
- Convalidatore dei manifest, degli hash e dei registri: Codex / CDX, agente AI.

Non è stata eseguita una revisione umana integrale dell'intero scope. Il presente giudizio documenta una verifica svolta da agenti AI con passaggi indipendenti e controlli riproducibili; non sostituisce la responsabilità professionale nell'uso della norma.

Firma del verificatore primario e coordinatore: Codex / CDX  
Firma del verificatore G6: Codex / CDX, agente AI in contesto fresco  
Firma del convalidatore: Codex / CDX
