---
scope_id: ntc2018-8.7.1
stato: CHIUSO
agente: GBOT
agente_istanza: GBOT-verifica-ntc
macchina: "W520; GBOT-verifica-ntc come C G0-G4; Grok Build per il confronto iniziale; CDX come C G5-G6 giro 1; GBOT-verifica-ntc come C per le correzioni dopo il G6 e il G7 dal 2026-10-18"
presa_in_carico: 2026-10-17
procedura: VC-NTC/9
procedura_sha256: 14084c23fd8a0563515a906d0192b93dbd419ac0a8a2a6f8a3715938bedde82f
catalogo_sha256: add1873d309b44930b8caccf8dd5ed3714926108a106230de35133a8a76e239e
catalogo_sha256_correzioni_g6: 279267c27d0aa19045045f6110d8cece1f5ec99ebcaaceac3b7f267676372f48
atti:
  - "D.M. 17/01/2018, § 8.7.1, dalla rubrica fino a prima di 8.7.2"
  - "Circolare 21/01/2019 n. 7, § C8.7.1 con C8.7.1.1-C8.7.1.4, dalla rubrica fino a prima di C8.7.2"
file_markdown: [cap08/8.7.1-progettazione-interventi-costruzioni-in-muratura.md]
righe_registro: ["8.7.1"]
base_git: 92a449e
snapshot_sha256: 5c466acd11ce6c074f28ba1b022d78fff5930d5829f378701493ac52b98ad57c
giro_g6: 1
max_giri: 3
rilievi_aperti: 0
gate: {G0: OK, G1: OK, G2: OK, G3: OK, G4: OK, G5: OK, G6: OK, G7: OK}
attesa_decisione: []
prossimo_passo: "Nessuna sul file: VC conclusa sullo snapshot registrato."
lavorazione: _tmp_render/cap08/vc-8.7.1-20261017-gbot/
routing_effettivo:
  C_G0_G4: {agente: "Grok Bot (GBOT-verifica-ntc)", ruolo: "coordinamento, controllo e lista per Sandro"}
  confronto_iniziale: {agente: "Grok Build sul W520, grok-4.6-build", ruolo: "G0-G4 integrale in tre sessioni separate"}
  controllo_aggiuntivo: {agente: "script locale con corpus structural-codes", ruolo: "controllo automatico, nessun LLM"}
  C_G5_G7: {agente: "Codex (CDX), modello effettivo non esposto dal runtime", ruolo: "coordinamento, G5 e predisposizione G7"}
  preparazione: "script di strumenti/; nessun modello leggero necessario"
  E: non_attivato
  C_correzioni_g6: {agente: "Grok Bot (GBOT-verifica-ntc)", ruolo: "giudizio dei 14 rilievi per Sandro, lista g6 di 4 voci applicata via script, renderer, catalogo voce 25, rettifica C-PRO-016, G7 predisposto"}
  V_modifiche: {agente: "Codex (CDX)", modello: "gpt-6.1-sol", ragionamento: high, sandbox: read-only, lanciato_da: Sandro, deroga: "profilo V della procedura rev. 9 § 5, decisione di Sandro del 2026-10-18"}
  prova_comparativa: {agente: Codex, modello: "gpt-6-luna", ragionamento: high, sandbox: read-only, esito: "un ERR-AUDIT non fondato"}
  prova_comparativa_terra: {agente: Codex, modello: "gpt-5.6-terra", sandbox: read-only, lanciato_da: Sandro, esito: "OK, zero nuovi rilievi"}
  V: {agenti: ["/root/v871_b01", "/root/v871_b02_v2", "/root/v871_b03_v2", "/root/v871_b04_v2"], profilo_richiesto: "gpt-5.6-sol, xhigh", modello_effettivo: "non esposto", isolamento: "contesti nuovi; cartelle temporanee esterne; restrizione istruttiva"}
consumi:
  Grok_Build: "A 5,82 M token e 3,73 USD; B 10,33 M e 6,45 USD; C 8,27 M e 5,15 USD; totale circa 24,4 M token e 15,33 USD, come esposto dai JSON CLI"
  CDX: non_disponibili
  V_modifiche_e_prova: "token e quota non esposti nei rapporti"
  GBOT: "non esposti"
---

# Scheda scope § 8.7.1

Sola riga 8.7.1, file `cap08/8.7.1-progettazione-interventi-costruzioni-in-muratura.md`, Norma e Circolare. Restano fuori 8.7, 8.7.2-8.7.5, C8.7.6, C8.8 e ogni altro file normativo.

## Storia e autorizzazioni

- Sandro ha autorizzato lo scope il 2026-10-17 con «Ok, facciamo 8.7.1».
- GBOT-verifica-ntc ha preso in carico lo scope il 2026-10-17 e ha coordinato G0-G4; il confronto iniziale integrale è stato svolto con Grok Build, con controllo automatico aggiuntivo tramite corpus structural-codes e riscontro sulla Gazzetta.
- Sandro ha approvato la lista v2 il 17/10/2026 alle 13:21, ora di Roma, ha deciso A-41, C-18, C-26 e D-01 a testo invariato e ha richiesto l'aggiunta SC-08, confluita nella lista v3.
- Questo prompt di Sandro autorizza il subentro di CDX per G5-G7, senza modifica del perimetro.

Lo scope reale copre 16 pagine: NTC 297-298 e Circolare 270-283. La soglia consigliata di 15 pagine è superata di una pagina; il dato è emerso in G0, è stato segnalato a Sandro nel rapporto C e lo scope già avviato prosegue intero, sotto il limite massimo di 40 pagine.

Firma del subentro: CDX, 2026-10-17.

## Avanzamento CDX

- Lista v3 applicata via script e `verifica-lista` conclusa con esito `OK`; target finale SHA-256 `09eab0335ca26594b29ea19f279acf1da8496550f70883b55fa6695a4b0ba6c8`.
- G5 `OK`: 662 righe depurate e 16 pagine assegnate una sola volta a quattro blocchi primari; link e indici verificati; resa canonica di 18 pagine osservata integralmente, con 18 tag numerati e nessun difetto visivo.
- Il primo commit previsto è bloccato dalla sandbox per diniego di scrittura su `.git/worktrees`; la lavorazione dei file prosegue come autorizzato da Sandro.
- G6, giro 1: quattro inventari fonte-prima validati, 180 ID complessivi; pacchetti rivelati e controllati integri. Il primo tentativo di mappa è stato respinto prima della rivelazione per un confine pagina-righe incoerente ed è conservato nel dossier. Due V hanno dovuto leggere le istruzioni generali della skill e la procedura per obbligo del runtime, senza consultare corpus, target, rapporti o risultati precedenti; il limite è registrato come restrizione istruttiva.
- G6 `KO`: 180/180 ID coperti, 13 `ERR-MD`, 1 `ERR-AUDIT`, zero `DUBBIO`. Esiti per blocco: b01 `KO` con 4 rilievi; b02 `OK`; b03 `KO` con 3 rilievi; b04 `KO` con 7 rilievi. Nessuna correzione applicata e nessuna seconda tornata avviata.
- G7 non eseguito: la procedura lo vieta finché G6 non è a zero `ERR-MD`, zero `ERR-AUDIT` e zero `DUBBIO`. La riga resta `IN-CORSO` in attesa della decisione di Sandro.

## Ripresa GBOT-verifica-ntc, 2026-10-18

Subentro di GBOT-verifica-ntc per chiudere lo scope, su decisione di Sandro del 2026-10-18 («Prima chiudiamo 8.7.1», «ok..vai» alle 11:18). Decisioni di Sandro sui 14 rilievi del G6 giro 1:

- 8 e 9: rubriche C8.7.1.3.1.1 e C8.7.1.3.1.2 in grassetto corsivo, scritte `###### *…*` come le altre rubriche di sesto livello;
- 13 e 14: nota 4 come la fonte, senza la parola «Nota», con la nota a piè di pagina Markdown `[^4]`; nuova voce 25 del catalogo;
- 1-3, 5, 10-12: solo resa; `-V block-headings` nel renderer comune, file Markdown invariati;
- 4: rettifica documentale dell'inventario di b01 (C-PRO-016);
- 6 e 7: non fondati, per le misure di interlinea della p. 278.

Lista `correzioni-g6/lista-correzioni-g6.json` di 4 voci applicata con `applica-lista`, indici rigenerati, `verifica-lista` della lista v3 più g6 (210 voci) sulla base `92a449e` OK. Nuovo snapshot `5c466acd…ad57c`. Controllo delle modifiche del § 8, non un nuovo giro: `giro_g6` resta 1 su `max_giri` 3. Lo ha eseguito Codex lanciato da Sandro, in deroga al profilo V: V gpt-6.1-sol, esito OK, 11 rilievi chiusi e Q1, Q2 conformi; prova comparativa gpt-6-luna, un ERR-AUDIT sulla pagina della resa giudicato non fondato (la rubrica sta a p. 16). Seconda prova comparativa gpt-5.6-terra, lanciata da Sandro, alle 13:47: OK, zero nuovi rilievi. Un primo tentativo con Claude Code alle 11:35 è stato interrotto senza output. Evidenze in `vc-ntc2018-8.7.1-2026-10-17/correzioni-g6/` e `g6-modifiche/`. G6: OK, zero rilievi aperti.

Firma: GBOT-verifica-ntc, 2026-10-18.

## G7 tentativo 1 e pagine del registro, 2026-10-18

G7 tentativo 1, Codex gpt-6.1-sol high read-only in contesto nuovo, dalle 13:25 alle 13:28: `KO` per il solo rilievo G7-REGISTRO-8.7.1, l'ERR-AUDIT delle pagine del registro rilevato in G0; gate G0-G6 confermati OK, manifest e snapshot riconciliati. Conservato in `vc-ntc2018-8.7.1-2026-10-17/G7-tentativo-1-KO.json`. Decisione di Sandro delle 13:47, strada (a): pagine corrette con il nuovo comando `vc-supporto.py pagine` (piano, `--applica`, lint OK), NTC da 297 a 297-298, Circolare da 270-272, 274-277, 279, 282-283 a 270-283. Valori riaccertati sui PDF ufficiali: rubrica `8.7.1.` a p. 297 e `8.7.2.` a p. 298; `C8.7.1` a p. 270 e `C8.7.2` a p. 283; p. 281 solo raster, interna all'intervallo (`registro-pagine/conferma-pagine.json`). Alle 13:50 Sandro ha deciso Codex gpt-5.6-terra per i controlli ordinari del verificatore e gpt-6.1-sol per punti dubbi e G7; Luna scartata. Prossimo passo: G7 tentativo 2 con le stesse modalità.

## Chiusura 2026-10-18

G7 tentativo 2, Codex gpt-6.1-sol high read-only in contesto nuovo, dalle 13:56 alle 13:58: `OK`, gate G0-G7 OK, zero rilievi aperti, manifest `b83b4ba1…ee4b` di 174 file, snapshot `5c466acd…ad57c` (`vc-ntc2018-8.7.1-2026-10-17/G7.json`). Riga 8.7.1 registrata `VC-OK` con `vc-supporto.py registra`. [Verbale](verbale-VC-ntc2018-8.7.1-2026-10-18.md). Firma: GBOT-verifica-ntc.
