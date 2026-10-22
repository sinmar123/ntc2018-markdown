# Verbale VC del § 8.7.3 con C8.7.3

Data: 2026-10-22. Procedura VC-NTC/10, SHA-256 `bc54cd41effc1e2aaf3f20f0dd75b99b4a3279df787a2eb35faaec7261b41b22`, copia congelata `vc-ntc2018-8.7.3-2026-10-22/procedura-congelata-r10.md`. Catalogo delle normalizzazioni, voci 1-25, SHA-256 `279267c27d0aa19045045f6110d8cece1f5ec99ebcaaceac3b7f267676372f48`, copia congelata `vc-ntc2018-8.7.3-2026-10-22/catalogo-congelato.md`.

**Esito proposto: VC-OK**, subordinato al giudizio G7 del verificatore, sul solo file [8.7.3-progettazione-interventi-costruzioni-miste.md](../cap08/8.7.3-progettazione-interventi-costruzioni-miste.md), snapshot SHA-256 `1a400982cb5e1e49d66f20b719bd7b8ee3449b6bb48f9b488f273f4d37cd4f08`. Fuori dal perimetro: 8.7, 8.7.1, 8.7.2, 8.7.4, 8.7.5, C8.7.4 e seguenti, il file complessivo `cap08/8-esistenti.md` e ogni altro file normativo.

## Fonte, perimetro e vigenza

D.M. 17 gennaio 2018, § 8.7.3, pagina fisica 298, da `8.7.3.` a prima di `8.7.4.` (p. 299); pagina condivisa con 8.7.1 e 8.7.2. Circolare 21 gennaio 2019 n. 7, § C8.7.3, pagina fisica 289, da `C8.7.3` a prima di `C8.7.4`; pagina condivisa con C8.7.2 e C8.7.4. Due pagine, sotto la soglia di 15. PDF SHA-256 `dda1e397d56d71aa0f5bc457c3ba9b77064a468699dfc37bd056ac6c47105a46` (NTC) e `f7c3b8d1f443aadb6b3e020b6b6c19813683492ecaadd2c15bf6bf1939aaed7c` (Circolare). Le colonne pagine della riga 8.7.3 nel CSV (NTC 298, Circolare 289) coincidono con il perimetro accertato in G0: il comando `pagine` non è servito.

Atti e URL ufficiali: D.M. 17/01/2018, S.O. n. 8 alla G.U. n. 42 del 20/02/2018, <https://www.gazzettaufficiale.it/eli/id/2018/02/20/18A00716/sg>; Circolare 21/01/2019 n. 7, S.O. n. 5 alla G.U. n. 35 dell'11/02/2019, <https://www.gazzettaufficiale.it/eli/id/2019/02/11/19A00855/sg>; D.M. 9/03/2023, <https://www.gazzettaufficiale.it/eli/id/2023/03/22/23A01847/sg>. Schede interrogate nel ricontrollo: <https://www.gazzettaufficiale.it/atto/serie_generale/caricaDettaglioAtto/originario?atto.dataPubblicazioneGazzetta=2018-02-20&atto.codiceRedazionale=18A00716>; <https://www.gazzettaufficiale.it/atto/serie_generale/caricaDettaglioAtto/originario?atto.dataPubblicazioneGazzetta=2019-02-11&atto.codiceRedazionale=19A00855>; <https://www.gazzettaufficiale.it/atto/serie_generale/caricaDettaglioAtto/originario?atto.dataPubblicazioneGazzetta=2023-03-22&atto.codiceRedazionale=23A01847>.

Vigenza: ricognizione piena del 2026-10-13, ricontrollo mirato del 2026-10-22 (`g1/ricontrollo-20261022.json`): schede GU di NTC, Circolare e D.M. 9 marzo 2023 identiche byte per byte a quelle del 2026-10-18, senza avvisi nuovi; il D.M. 9 marzo 2023 non tocca il capitolo 8.

## Ruoli effettivi

- C: Grok Bot (GBOT-verifica-ntc), presa del 2026-10-22 autorizzata da Sandro alle 07:13: G0-G5, controllo a campione sulla fonte (confronto parola per parola del livello di testo, ritagli a 400 e 600 dpi), lista per Sandro, applicazione con gli strumenti, pacchetti G6 e G7, giudizio dei rilievi per Sandro, worktree e commit. Su richiesta di Sandro delle 07:14 il lavoro lungo è stato affidato a Codex.
- Confronto iniziale integrale: Codex sul W520 (CDX), gpt-5.6-terra, high, read-only, un blocco in due passaggi (confronto-iniziale/codex-terra.json). Candidati di struttura con `strumenti/vc-struttura-fonte.py`. gpt-6.1-sol non attivato per dubbi: nessun dubbio.
- G6 integrale, giro 1: V Codex (CDX), contesto nuovo, indipendente da chi ha scritto e applicato la lista. Tentativo 1 annullato; tentativo 2 con gpt-5.6-terra, high, read-only, in entrambe le fasi (modello letto nel log).
- G7: Codex gpt-6.1-sol, high, read-only, contesto nuovo, giudizio in `G7.json`.

Natura: verifica svolta da agenti AI; nessuna revisione umana integrale. Sandro ha approvato la lista v1 e deciso sul G6 (annullamento del tentativo 1, chiusura del rilievo del tentativo 2). Isolamento reale: cartelle temporanee esterne al workspace e sandbox read-only di Codex, senza `--always-approve`; nessuna sandbox di lettura dimostrata; letture dichiarate da V solo nella cartella del blocco. In sandbox read-only V non può scrivere file: C ha trascritto byte per byte i messaggi finali JSON di V.

## Correzioni prima del G6

Lista v1 approvata per intero da Sandro il 2026-10-22 alle 07:35 («Sì, approvo le due correzioni e vai avanti»): 2 voci di forma, nessuna sostanziale, nessun dubbio. F-01: rubrica `### C8.7.3 COSTRUZIONI MISTE` senza punto e in maiuscolo (voce 23); F-02: due capoversi nella Circolare dopo «favorevole.», come nella fonte (voce 1). Entrambe trovate da CDX-terra e confermate da GBOT. Applicata con `applica-lista` (piano, `--applica`) alle 07:38; indici interni rigenerati (311 file, corpi invariati); `verifica-lista` sulla base `33f9a3d` OK; lint 0 errori; diff in `diff-proposto.patch` (`decisione-applicazione-20261022.json`). Target `e50344d7ef0b32ab7eb43669db16e4e7bcd98bb9db23387459aff01c05dea6dc` prima, `1a400982cb5e1e49d66f20b719bd7b8ee3449b6bb48f9b488f273f4d37cd4f08` dopo. Anomalie della fonte: nessuna. Nessuna nota AF-COR.

## G5 e G6 integrale, giro 1

G5 OK: testo composto con `componi-scope` e depurato di 17 righe, resa canonica `g5/resa-finale.pdf` di una pagina, osservata da C senza tagli né caratteri mancanti; un blocco (`config-g6.json`, `mappa-g5.json`): b01 NTC 298 e Circolare 289. G2-G4 chiusi sul confronto iniziale: nessun apparato nel perimetro (formule, tabelle, figure, note).

Tentativo 1 (07:40-07:44), **annullato** da Sandro alle 07:48 (`decisione-g6-20261022.json`): fase 1 con gpt-5.6-terra; fase 2 ripresa da C senza `-m`, quindi con il modello predefinito gpt-6-astra; esito KO per G6-AUDIT-01 (coordinate in pixel dell'inventario errate per la Circolare). Conservato in `g6-tentativo-1-annullato/`, `sequenza-g6-tentativo-1-annullato.json`, `esito-g6-tentativo-1-annullato.json`. Nessuna rettifica dell'inventario congelato.

Tentativo 2: nuovo `prepara` con la stessa configurazione; fase 1 dalle 07:49 alle 07:54, contesto nuovo; `valida-inventario`, `rivela` e `verifica-pacchetto` OK; fase 2 dalle 07:55 alle 07:57 nello stesso contesto (`codex exec resume` con `-m gpt-5.6-terra`); `valida-g6` schema OK, 6 ID coperti, 1 rilievo (`sequenza-g6.json`, `esito-g6.json`). NTC-873-CONDIZIONE (`ERR-MD` proposto da V): V legge «Per tale situazione» all'inizio del capoverso finale di 8.7.3. Decisione di Sandro del 2026-10-22 alle 08:07 (`decisione-g6-rilievo-20261022.json`): chiuso senza modifiche, non trova riscontro nella fonte; livello vettoriale e ritaglio a 600 dpi della p. 298 riportano «Per queste situazioni» (`prove-c/`). Target invariato; nessun controllo delle modifiche necessario.

`giro_g6`: 1 su `max_giri` 3; il recupero sullo stesso snapshot completa il giro corrente (§ 8). G6: OK, zero `ERR-MD`, zero `ERR-AUDIT`, zero `DUBBIO`.

## Normalizzazioni, limiti e manifest

Normalizzazioni applicate secondo il catalogo, voci 1-25; in questo scope voci 1, 21 e 23. Consumi (token dichiarati dalla CLI, letti dai log UTF-16; valori rettificati in `rettifica-g7-audit-01-20261022.json`): confronto iniziale gpt-5.6-terra 40.218; G6 tentativo 1 fase 1 43.968 (gpt-5.6-terra), fase 2 97.981 (gpt-6-astra); G6 tentativo 2 fase 1 54.208, fase 2 117.962 (gpt-5.6-terra); G7 tentativo 1 gpt-6.1-sol 67.227; G7 tentativo 2 nel giudizio. Nessun costo in valuta esposto.

Il G7 tentativo 1 (Codex gpt-6.1-sol, dalle 08:11 alle 08:14) è stato `KO` per due `ERR-AUDIT` documentali: G7-AUDIT-01, `sequenza-g6.json` riportava «non letto» per i modelli del G6 tentativo 2 perché lo script di C leggeva come UTF-8 i log UTF-16 di Codex; G7-AUDIT-02, il verbale non riportava gli URL degli atti e il ricontrollo G1 ne dava solo un modello. Su decisione di Sandro («Sì, correggi e rifai il G7 con Sol») C li ha rettificati senza toccare target, copertura o giudizi: `rettifica-g7-audit-01-20261022.json` (modelli e token dai log, file originali non riscritti), URL in questo verbale e campi aggiunti in `g1/ricontrollo-20261022.json`. Il tentativo 1 è conservato in `G7-tentativo-1-KO.json` (percorso locale redatto, `G7-tentativo-1-redazione.json`), con il manifest di allora `manifest-rilascio-g7-tentativo-1.json`.

Il giudizio G7 è `vc-ntc2018-8.7.3-2026-10-22/G7.json`: sta fuori dal manifest perché ne riporta l'impronta. [Manifest](vc-ntc2018-8.7.3-2026-10-22/manifest-rilascio.json). [Scheda](scheda-scope-ntc2018-8.7.3.md). Le pagine PNG e i PDF di prova restano locali secondo `.gitignore`; il manifest ne conserva le impronte.

VC-OK vale per questo snapshot e perimetro.

Prossima azione: Nessuna sul file: VC conclusa sullo snapshot registrato.
