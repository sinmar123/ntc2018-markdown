# Verbale VC del § 8.7.1 con C8.7.1

Data: 2026-10-18. Procedura VC-NTC/9, SHA-256 `14084c23fd8a0563515a906d0192b93dbd419ac0a8a2a6f8a3715938bedde82f`, copia congelata `vc-ntc2018-8.7.1-2026-10-17/procedura-congelata-r9.md`. Catalogo usato fino al G6 giro 1 `add1873d…e239e` (`catalogo-congelato.md`), con la voce 25 aggiunta il 2026-10-18 per decisione di Sandro `279267c2…72f48` (`catalogo-congelato-v25.md`).

**Esito proposto: VC-OK**, subordinato al giudizio G7 del verificatore, sul solo file [8.7.1-progettazione-interventi-costruzioni-in-muratura.md](../cap08/8.7.1-progettazione-interventi-costruzioni-in-muratura.md), snapshot SHA-256 `5c466acd11ce6c074f28ba1b022d78fff5930d5829f378701493ac52b98ad57c`. Fuori dal perimetro: 8.7, 8.7.2-8.7.5, C8.7.6, C8.8 e il file complessivo `cap08/8-esistenti.md`.

## Fonte, perimetro e vigenza

D.M. 17 gennaio 2018, § 8.7.1, pagine fisiche 297-298, da `8.7.1.` a prima di `8.7.2.`. Circolare 21 gennaio 2019 n. 7, § C8.7.1 con C8.7.1.1-C8.7.1.4, pagine fisiche 270-283, da `C8.7.1` a prima di `C8.7.2`; le pagine 270 e 283 sono condivise. PDF SHA-256 `dda1e397d56d71aa0f5bc457c3ba9b77064a468699dfc37bd056ac6c47105a46` (NTC) e `f7c3b8d1f443aadb6b3e020b6b6c19813683492ecaadd2c15bf6bf1939aaed7c` (Circolare). La p. 281 è solo raster, letta sul raster nativo 2221×3106, SHA-256 `d860503c…7d406`. Sedici pagine, una oltre la soglia consigliata di 15: segnalato a Sandro in G0, scope non diviso.

Vigenza: ricognizione piena del 2026-10-13, ricontrollo mirato del 2026-10-17 (`g1/ricontrollo-20261017.json`): schede GU dei tre atti invariate; il D.M. 9 marzo 2023 non tocca il capitolo 8.

## Ruoli effettivi

- C G0-G4: Grok Bot (GBOT-verifica-ntc); confronto iniziale integrale con Grok Build sul W520 (grok-4.6-build), tre sessioni separate; controllo aggiuntivo con il corpus structural-codes, script senza LLM.
- Applicazione della lista v3 (206 voci), G5 e G6 giro 1: Codex (CDX), subentrato il 2026-10-17; quattro V Codex a contesto nuovo, profilo richiesto gpt-5.6-sol xhigh, modello effettivo non esposto.
- Giudizio dei rilievi del G6, correzioni dopo il G6 (4 voci), renderer e catalogo: GBOT-verifica-ntc, 2026-10-18.
- Controllo delle modifiche: V Codex gpt-6.1-sol, high, read-only, lanciato da Sandro; prove comparative gpt-6-luna e gpt-5.6-terra. Deroga al profilo V del § 5 decisa da Sandro il 2026-10-18.
- G7: verificatore designato nel giudizio `G7.json`.

Natura: verifica svolta da agenti AI; nessuna revisione umana integrale. Sandro ha deciso la lista, i dubbi e i 14 rilievi, e ha eseguito il controllo delle modifiche lanciando Codex.

## Correzioni prima del G6

Lista v3 approvata da Sandro il 2026-10-17 (v2 alle 13:21, più SC-08): 206 voci, 21 sostanziali e 185 di forma; dubbi A-41, C-18, C-26 e D-01 decisi a testo invariato. Applicata da CDX con `applica-lista`; `verifica-lista` sulla base `92a449e` OK. Anomalie della fonte conservate: 22, elencate nella lista. Nessuna nota AF-COR.

## G5 e G6 integrale, giro 1

G5 OK (`g5/esito-resa.json`): 662 righe depurate, 16 pagine in quattro blocchi primari, resa del testo depurato di 18 pagine con 18 tag. G6 giro 1: 180/180 ID coperti; b02 OK, b01, b03 e b04 KO; 13 `ERR-MD`, 1 `ERR-AUDIT`, zero `DUBBIO` (`esito-g6.json`). Un primo tentativo di mappa era stato respinto prima della rivelazione, senza consumare il giro. Isolamento: cartelle temporanee esterne, restrizione istruttiva; due V hanno letto istruzioni generali del runtime.

## Esito dei 14 rilievi

Decisioni di Sandro del 2026-10-18 (`correzioni-g6/esito-rilievi-g6-r1.json`):

- 8, 9 (rubriche di sesto livello senza corsivo): corretti, voci G6R1-08 e G6R1-09.
- 13, 14 (nota 4): corretti come la fonte con la nota Markdown `[^4]`, voci G6R1-13 e G6R1-14; nuova voce 25 del catalogo.
- 1-3, 5, 10-12 (rubriche run-in nella resa): `-V block-headings` in `strumenti/render-capitolo.py`, Markdown invariato.
- 4 (C-PRO-016, ERR-AUDIT): rettifica documentale dell'inventario, nessun errore del testo; nessun ritorno a V (§ 8).
- 6, 7 (capoversi a p. 278): non fondati; interlinea ordinaria di circa 10,5 pt contro 13-14 pt fra capoversi.

## Controllo delle modifiche

Lista g6 di 4 voci applicata con `applica-lista`; `verifica-lista` della lista v3 più g6 (210 voci) sulla base `92a449e` OK. Snapshot prima `09eab033…a6c8`, dopo `5c466acd…ad57c`. `pacchetto-modifiche` sugli stessi blocchi del G6: solo b04 cambia. Resa del testo depurato con il renderer nuovo, 18 pagine, SHA-256 `78e6f1cb…1b0d`.

V gpt-6.1-sol: diff OK, 11 rilievi chiusi, Q1 e Q2 (rilievi 6 e 7, posti come domande aperte) stesso capoverso, Markdown conforme, nessun nuovo rilievo, esito OK. Prova comparativa gpt-6-luna: stesse chiusure e stesse letture, più un ERR-AUDIT sulla pagina della rubrica C8.7.1.3.1.2 nella resa, non fondato: la rubrica sta a p. 16 (`g6-modifiche/verifica-rilievo-luna.json`). Seconda prova comparativa gpt-5.6-terra, lanciata da Sandro, terminata alle 13:47: esito OK, stesse chiusure, Q1 e Q2 conformi, nessun nuovo rilievo (`g6-modifiche/esito-terra.json`). Per decisione di Sandro vale il giudizio di Sol. Un tentativo con Claude Code delle 11:35 è stato interrotto senza output. `giro_g6`: 1 su `max_giri` 3; il controllo delle modifiche non è un nuovo giro. G6: OK, zero `ERR-MD`, zero `ERR-AUDIT`, zero `DUBBIO`.

## Normalizzazioni, limiti e manifest

Normalizzazioni applicate secondo il catalogo, voci 1-25. Resa dei viewer: su GitHub la nota `[^4]` può comparire con numero 1, perché GitHub rinumera le note (voce 25); il PDF canonico stampa 4. Il file vivo non si rende direttamente per la profondità dell'indice interno: la resa canonica è quella del testo depurato.

Pagine della riga 8.7.1 nel CSV corrette il 2026-10-18 con il nuovo comando `vc-supporto.py pagine` (piano, `--applica`, lint OK), su decisione di Sandro delle 13:47: NTC da 297 a 297-298, Circolare da 270-272, 274-277, 279, 282-283 a 270-283. Valori riaccertati sui PDF ufficiali: rubrica `8.7.1.` a p. 297 e `8.7.2.` a p. 298; `C8.7.1` a p. 270 e `C8.7.2` a p. 283; p. 281 solo raster, interna all'intervallo (`vc-ntc2018-8.7.1-2026-10-17/registro-pagine/`). L'ERR-AUDIT del registro rilevato in G0, che aveva motivato il G7 tentativo 1 `KO` (`vc-ntc2018-8.7.1-2026-10-17/G7-tentativo-1-KO.json`, rilievo G7-REGISTRO-8.7.1), è chiuso. Consumi: Grok Build circa 15,33 USD per il confronto iniziale; Codex non esposti.

Il giudizio G7 è `vc-ntc2018-8.7.1-2026-10-17/G7.json`: sta fuori dal manifest perché ne riporta l'impronta; il tentativo 1 `KO` è conservato nel dossier, insieme al manifest di allora `manifest-rilascio-g7-tentativo-1.json`. [Manifest](vc-ntc2018-8.7.1-2026-10-17/manifest-rilascio.json). [Scheda](scheda-scope-ntc2018-8.7.1.md). Le pagine PNG e i PDF di prova restano locali secondo `.gitignore`; il manifest ne conserva le impronte.

VC-OK vale per questo snapshot e perimetro.

Prossima azione: Nessuna sul file: VC conclusa sullo snapshot registrato.
