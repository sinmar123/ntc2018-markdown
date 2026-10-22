---
scope_id: ntc2018-8.7.3
stato: IN-CORSO
agente: GBOT
agente_istanza: GBOT-verifica-ntc
macchina: "W520; GBOT-verifica-ntc come C; Codex sul W520 (CDX) per confronto integrale, G5 e G6"
presa_in_carico: 2026-10-22
procedura: VC-NTC/10
procedura_sha256: bc54cd41effc1e2aaf3f20f0dd75b99b4a3279df787a2eb35faaec7261b41b22
catalogo_sha256: 279267c27d0aa19045045f6110d8cece1f5ec99ebcaaceac3b7f267676372f48
atti:
  - "D.M. 17/01/2018, § 8.7.3, dalla rubrica fino a prima di 8.7.4"
  - "Circolare 21/01/2019 n. 7, § C8.7.3, dalla rubrica fino a prima di C8.7.4"
file_markdown: [cap08/8.7.3-progettazione-interventi-costruzioni-miste.md]
righe_registro: ["8.7.3"]
base_git: 33f9a3d
snapshot_sha256: 1a400982cb5e1e49d66f20b719bd7b8ee3449b6bb48f9b488f273f4d37cd4f08
giro_g6: 1
max_giri: 3
rilievi_aperti: 0
gate: {G0: OK, G1: OK, G2: OK, G3: OK, G4: OK, G5: OK, G6: OK, G7: KO}
attesa_decisione: [G7-AUDIT-06, G7-AUDIT-07, G7-AUDIT-08]
prossimo_passo: "Decisione di Sandro sui rilievi G7-AUDIT-06, 07 e 08 del G7 tentativo 4."
lavorazione: verifica-conformita/vc-ntc2018-8.7.3-2026-10-22/
routing_effettivo:
  C: {agente: "Grok Bot (GBOT-verifica-ntc)", ruolo: "coordinamento, controllo a campione sulla fonte, lista per Sandro, worktree e commit"}
  confronto_iniziale: {agente: "Codex sul W520 (CDX)", modello: "gpt-5.6-terra", sandbox: read-only, ruolo: "confronto integrale sulla fonte e secondo passaggio mirato"}
  dubbi: {agente: "Codex sul W520 (CDX)", modello: "gpt-6.1-sol", sandbox: read-only, ruolo: "solo voci dubbie"}
  E: non_attivato
  V: {agente: "Codex sul W520 (CDX)", modello_g6: "gpt-5.6-terra (tentativo 2; tentativo 1 annullato: fase 2 gpt-6-astra)", modello_g7: "gpt-6.1-sol", sandbox: read-only}
consumi: {}
---

# Scheda scope § 8.7.3

Sola riga 8.7.3, file `cap08/8.7.3-progettazione-interventi-costruzioni-miste.md`, Norma e Circolare. Restano fuori 8.7, 8.7.1, 8.7.2, 8.7.4, 8.7.5, C8.7.4 e seguenti e ogni altro file normativo.

## Storia e autorizzazioni

- Sandro ha autorizzato lo scope il 2026-10-22 alle 07:13 con «Ok allora andiamo con il prossimo. Fallo fare a codex»: VC della riga successiva a 8.7.2, cioè 8.7.3 con C8.7.3, procedura rev. 10, lavoro a Codex sul W520. Alle 07:14 ha chiesto di ridurre al minimo il lavoro di C («cerca di non lavorare troppo, fai lavorare gli altri»).
- Ramo `cdx/vc-8.7.3-261022` creato da origin/main (33f9a3d), worktree `_tmp_render/wt-cdx-vc-8.7.3-261022`.

## G0

Norma pagina fisica 298, da `8.7.3.` a prima di `8.7.4.` (che apre p. 299); pagina condivisa con 8.7.1 e 8.7.2. Circolare pagina fisica 289, da `C8.7.3` a prima di `C8.7.4`; pagina condivisa con C8.7.2 e C8.7.4. Due pagine, sotto la soglia di 15. Le colonne del registro (NTC 298, Circolare 289) coincidono con la fonte: il comando `pagine` non serve. PDF ufficiali in `verifica-conformita/fonte-ufficiale/`, SHA-256 `dda1e397…5a46` (NTC) e `f7c3b8d1…ed7c` (Circolare), ricalcolati il 2026-10-22.

G1: ricognizione piena del 2026-10-13 riusabile (meno di trenta giorni); ricontrollo mirato da registrare prima della chiusura di G1.

Firma: GBOT-verifica-ntc, 2026-10-22.

## G1-G5, 2026-10-22

- **07:35:** Sandro approva la lista v1 («Sì, approvo le due correzioni e vai avanti»): F-01 e F-02, entrambe di forma (`decisione-applicazione-20261022.json`).
- **07:38:** G1 chiuso: ricontrollo mirato sulle schede GU di NTC, Circolare e D.M. 9/3/2023, identiche byte per byte a quelle del 2026-10-18; ricognizione piena del 2026-10-13 (`g1/ricontrollo-20261022.json`).
- **07:38:** lista applicata con `applica-lista` (piano, `--applica`); indici interni rigenerati, 311 corpi invariati; `verifica-lista` sulla base `33f9a3d` OK; lint 0 errori. Target `e50344d7…` → `1a400982…`; diff in `diff-proposto.patch`.
- **07:40:** G5. Testo composto con `componi-scope` e depurato (17 righe); resa canonica `g5/resa-finale.pdf` di una pagina, osservata da C senza tagli né caratteri mancanti. Un solo blocco G6 (`config-g6.json`, `mappa-g5.json`): NTC 298 e Circolare 289. G2-G4 chiusi sul confronto iniziale e sulla lista: nessun apparato nel perimetro.

## G6 giro 1, 2026-10-22

- Fase 1 (07:40-07:42) Codex gpt-5.6-terra, high, read-only, contesto nuovo: inventario di 9 elementi; `valida-inventario`, `rivela` e `verifica-pacchetto` OK.
- Fase 2 (07:42-07:44) nello stesso contesto con `codex exec resume`: **scostamento**, la ripresa senza `-m` ha usato il modello predefinito gpt-6-astra. `valida-g6`: schema OK, 9 ID coperti, 1 rilievo.
- Esito **KO**: 0 `ERR-MD`, 1 `ERR-AUDIT`, 0 `DUBBIO`. G6-AUDIT-01: coordinate in pixel dell'inventario errate per i tre elementi della Circolare; V attesta il confronto integrale e nessuna difformità del corpus. C lo giudica errore documentale fondato (`esito-g6.json`). G7 non avviato.

Firma: GBOT-verifica-ntc, 2026-10-22.

## G6 giro 1, tentativo 2, 2026-10-22

- **07:48:** Sandro decide «Rifai il G6 con Terra da capo, poi G7 con Sol». Tentativo 1 annullato (fase 2 con gpt-6-astra, G6-AUDIT-01), conservato in `g6-tentativo-1-annullato/` con `sequenza-g6-tentativo-1-annullato.json` ed `esito-g6-tentativo-1-annullato.json` (`decisione-g6-20261022.json`). `giro_g6` resta 1 (§ 8: recupero sullo stesso snapshot).
- Nuovo `prepara` con la stessa configurazione. Fase 1 (07:49-07:54) e fase 2 (07:55-07:57) con Codex gpt-5.6-terra, high, read-only, contesto nuovo e poi ripreso; modello letto nel log di entrambe le fasi. `valida-inventario`, `rivela`, `verifica-pacchetto` OK; `valida-g6`: schema OK, 6 ID coperti, 1 rilievo.
- Esito **KO**: 1 `ERR-MD`, 0 `ERR-AUDIT`, 0 `DUBBIO`. NTC-873-CONDIZIONE: V legge «Per tale situazione» all'inizio del capoverso conclusivo di 8.7.3. C lo giudica non fondato: la fonte stampa «Per queste situazioni» (livello vettoriale e ritaglio a 600 dpi in `prove-c/`). G7 non avviato; decisione a Sandro.

Firma: GBOT-verifica-ntc, 2026-10-22.

## Decisione sul rilievo e lotto di chiusura, 2026-10-22

- **08:07:** Sandro: «Sì, chiudi il rilievo e fai il G7 con Sol». NTC-873-CONDIZIONE chiuso senza modifiche: non trova riscontro nella fonte (p. 298, «Per queste situazioni», ritaglio a 600 dpi). G6 giro 1: zero `ERR-MD`, zero `ERR-AUDIT`, zero `DUBBIO` (`decisione-g6-rilievo-20261022.json`). Target invariato.
- Lotto di chiusura preparato per il G7: verbale, manifest, piano di registrazione e riepilogo meccanico.

Firma: GBOT-verifica-ntc, 2026-10-22, lotto G7.

## G7 tentativo 1, 2026-10-22

- 08:11-08:14 Codex gpt-6.1-sol (modello letto nel log), high, read-only, contesto nuovo: **KO** per due `ERR-AUDIT` documentali (`G7-tentativo-1-KO.json`, percorso locale redatto in `G7-tentativo-1-redazione.json`). Gate G0-G6 OK.
- G7-AUDIT-01: `sequenza-g6.json` riporta «non letto» per i modelli del tentativo 2, mentre verbale e scheda dicono gpt-5.6-terra letto nel log. Causa: log UTF-16 letti come UTF-8 dallo script di C; i log riletti riportano gpt-5.6-terra in entrambe le fasi.
- G7-AUDIT-02: verbale senza URL degli atti; `ricontrollo-g1-20261022.json` con un modello di URL.
- Nessun rilancio, nessuna registrazione: decisione di Sandro.

Firma: GBOT-verifica-ntc, 2026-10-22.

## Rettifiche e lotto G7 tentativo 2, 2026-10-22

- Sandro: «Sì, correggi e rifai il G7 con Sol». G7-AUDIT-01: `rettifica-g7-audit-01-20261022.json`, modelli e token del G6 riletti dai log UTF-16 (tentativo 2: gpt-5.6-terra, 54.208 e 117.962 token; tentativo 1: gpt-5.6-terra 43.968, gpt-6-astra 97.981); `sequenza-g6*.json` non riscritti. G7-AUDIT-02: URL degli atti nel verbale e in `g1/ricontrollo-20261022.json`. `giro_g6` resta 1.
- Manifest del tentativo 1 conservato come `manifest-rilascio-g7-tentativo-1.json`; manifest, verbale e piano di registrazione rigenerati.

Firma: GBOT-verifica-ntc, 2026-10-22, lotto G7 tentativo 2.

## G7 tentativo 2, KO

Il 2026-10-22, dalle 10:11 alle 10:14 (ora di Roma), CDX con Codex gpt-6.1-sol (ragionamento high, sandbox read-only, contesto nuovo, 79.544 token letti dal log in UTF-16) ha giudicato KO il G7 sul manifest 1ee7d16b4e984196af24fb9a0835e36b272be55473e2d64cc310a8845e67bd10. G7-AUDIT-01 e G7-AUDIT-02 risultano risolti. Resta un rilievo nuovo:

- G7-AUDIT-03 (ERR-AUDIT): la rettifica `rettifica-g7-audit-01-20261022.json` cita quattro log di Codex come fonte di modelli e token, ma i log non sono nel manifest. Il § 9 chiede che anche un'evidenza citata da un'altra evidenza del manifest sia inclusa.

Il giudizio è in `vc-ntc2018-8.7.3-2026-10-22/G7-tentativo-2-KO.json`, l'esecuzione in `G7-tentativo-2-esecuzione.json`. Nessun rilancio, nessuna registrazione: serve la decisione di Sandro.

Firma: GBOT-verifica-ntc, 2026-10-22, lotto G7 tentativo 2 KO.

## Rettifica G7-AUDIT-03 e lotto G7 tentativo 3, 2026-10-22

- Sandro: «Sì, aggiungi i log e rifai il G7 con Sol». I quattro log di Codex citati da `rettifica-g7-audit-01-20261022.json` sono nel dossier in `vc-ntc2018-8.7.3-2026-10-22/log-g6/`, copie UTF-8 con i percorsi locali sostituiti da segnaposto; `log-g6/indice.json` riporta le impronte degli originali e delle copie e le sostituzioni. Nella rettifica è stato aggiunto solo il campo `copie_dei_log`.
- Manifest del tentativo 2 conservato come `manifest-rilascio-g7-tentativo-2.json`; manifest, verbale e piano di registrazione rigenerati. `giro_g6` resta 1.

Firma: GBOT-verifica-ntc, 2026-10-22, lotto G7 tentativo 3.

## G7 tentativo 3, KO

Il 2026-10-22, dalle 10:53 alle 10:57 (ora di Roma), CDX con Codex gpt-6.1-sol (ragionamento high, sandbox read-only, contesto nuovo, 80.227 token letti dal log in UTF-16) ha giudicato KO il G7 sul manifest 7f1bc9eb9e4cc3bfaeb58437df98a039d02620c998903bc80fb7dc5cacbd5146. G7-AUDIT-01, G7-AUDIT-02 e G7-AUDIT-03 risultano risolti. Restano due rilievi nuovi:

- G7-AUDIT-04 (ERR-AUDIT): `G7-tentativo-2-esecuzione.json` cita il log del G7 tentativo 2 (sha256 7535ab28…c309), che non è nel manifest.
- G7-AUDIT-05 (ERR-AUDIT): le quattro copie in `log-g6/` conservano il percorso assoluto di sistema dell'eseguibile PowerShell (cartella Windows), una riga per copia.

Il giudizio è in `vc-ntc2018-8.7.3-2026-10-22/G7-tentativo-3-KO.json`, l'esecuzione in `G7-tentativo-3-esecuzione.json`. Nessun rilancio, nessuna registrazione: serve la decisione di Sandro.

Firma: GBOT-verifica-ntc, 2026-10-22, lotto G7 tentativo 3 KO.

## Rettifiche G7-AUDIT-04 e G7-AUDIT-05 e lotto G7 tentativo 4, 2026-10-22

- Sandro: «Sì, sistema tutto e rifai il G7 con Sol», poi «Togli il blocco AGENTS.md e i percorsi, poi G7 con Sol». Copie ripulite dei log dei G7 tentativi 1, 2 e 3 in `vc-ntc2018-8.7.3-2026-10-22/log-g7/`, con il contenuto dell'AGENTS.md del workspace omesso; copie in `log-g6/` rifatte senza alcun percorso assoluto e senza la documentazione dei plugin di Codex; indici con impronte, omissioni e sostituzioni; procedura in `ripulitura-log.py`.
- Controllo automatico `controllo-dossier.py` prima del manifest e sul manifest generato. Il log del G7 tentativo 4 resta fuori dal manifest che quel G7 verifica e sarà aggiunto dopo il giudizio.
- Manifest del tentativo 3 conservato come `manifest-rilascio-g7-tentativo-3.json`; manifest, verbale e piano di registrazione rigenerati. `giro_g6` resta 1.

Firma: GBOT-verifica-ntc, 2026-10-22, lotto G7 tentativo 4.

## G7 tentativo 4, KO

Il 2026-10-22, dalle 12:23 alle 12:29 (ora di Roma), CDX con Codex gpt-6.1-sol (ragionamento high, sandbox read-only, contesto nuovo, 130.412 token letti dal log in UTF-16) ha giudicato KO il G7 sul manifest 1b3684d6a6314861362e169e1930f5e2cf624ef1afd9d55fc64a1aa7c18a9048. Il verificatore non ha aperto file fuori dalla cartella, AGENTS.md compreso. G7-AUDIT-01..05 risultano risolti. Gate G6 e G7 giudicati KO per tre rilievi nuovi:

- G7-AUDIT-06 (ERR-AUDIT): nel G6 tentativo 2, fase 2, il verificatore ha letto la documentazione dei plugin di Codex, fuori dal blocco, mentre istruzioni e coordinatore lo vietavano; rapporto G6 e verbale attestano un confronto svolto solo sui materiali del blocco. Per il § 7 della procedura la lettura vietata invalida il blocco.
- G7-AUDIT-07 (ERR-AUDIT): i log del G6 tentativo 2 non dimostrano la lettura visiva integrale delle pagine (misure di pixel, estrazioni di testo e font, una «lettura visiva» stampata come stringa letterale dal comando).
- G7-AUDIT-08 (ERR-AUDIT): le autorizzazioni di Sandro ai rilanci dei G7 tentativi 2, 3 e 4 sono citate senza l'ora della decisione.

Il giudizio è in `vc-ntc2018-8.7.3-2026-10-22/G7-tentativo-4-KO.json`, l'esecuzione in `G7-tentativo-4-esecuzione.json`, la copia ripulita del log in `log-g7/g7-tentativo-4-log.txt` con `log-g7/indice-post-g7.json`. Nessun rilancio, nessuna registrazione: serve la decisione di Sandro. G7-AUDIT-06 e G7-AUDIT-07 toccano la validità del G6 e non sono correzioni documentali.

Firma: GBOT-verifica-ntc, 2026-10-22, lotto G7 tentativo 4 KO.
