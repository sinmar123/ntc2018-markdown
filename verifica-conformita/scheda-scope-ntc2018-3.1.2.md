---
scope_id: ntc2018-3.1.2
atti:
  - "D.M. 17/01/2018, § 3.1.2 Pesi propri dei materiali strutturali"
file_markdown: cap03/3.1.2-opere-civili-pesi-propri-dei-materiali-strutturali.md
fonte_ntc: {pdf: verifica-conformita/fonte-ufficiale/GU-2018-42-SO8-DM-17-01-2018.pdf, pagine_fisiche: 46}
fonte_circolare: null
unita_registro: 1
formule_numerate: 0
tabelle: 1
figure: 0
pagine_fonte: 1
stato: CHIUSO
agente: CDX
macchina: W520
presa_in_carico: 2026-08-27T13:04:49+02:00
giro_g6: 1
max_giri: 3
rilievi_aperti: 0
rilievi_persistenti: 0
gate: {G0: OK, G1: OK, G2: OK, G3: OK, G4: OK, G5: OK, G6: OK, G7: OK}
snapshot_sha256: c89175b4fab3660a3e1853a32b53cc4851957bc27d5f041720ba68107b6e3e9b
attesa_decisione: []
prossimo_passo: "attendere il via libera di Sandro prima di aprire il file 3.1.3"
routing_effettivo:
  p0d: {modello: "script locali + gpt-5.6-luna/medium", compito: "hash, render, inventari, confronto letterale, struttura e lista residui", esito: "completato con cinque residui puntuali per P1"}
  p0s: {modello: "non_usato nella ripresa", motivo: "il preflight era interamente P0-D", esito: "precedente passaggio Terra conservato soltanto nella storia"}
  p1: {modello: "gpt-5.6-sol/high", motivo_escalation: "cinque residui puntuali prodotti da Luna", esito: "otto edit autorizzati e ricontrollati, G0-G5 OK"}
  p2: {modello: "gpt-5.6-sol/xhigh", gate: "G4, G6 e G7", esito: "G4 OK; G6 r01 OK; G7 OK, manifest 8/8"}
esecutori:
  apertura: {coordinamento: "CDX/sessione principale", controlli_meccanici: "script locali", preflight_p0s: "gpt-5.6-terra/medium"}
  ripresa-p0d: {modello: "gpt-5.6-luna/medium", ruolo: "inventario e confronto deterministico", esito: "copertura completa, cinque residui per P1"}
  g0-g5: {p1: "gpt-5.6-sol/high, soli residui", tabella_a: "gpt-5.6-luna/medium source-first", tabella_b: "gpt-5.6-sol/xhigh source-first", riconciliazione: "gpt-5.6-sol/xhigh", esito: "OK, zero residui"}
  g6-r01: {coordinatore: "gpt-5.6-sol/xhigh fresco", inventario_source_first: "gpt-5.6-sol/xhigh fresco", verifica_blocco: "gpt-5.6-sol/xhigh fresco", blocchi: 1, staging: "C:/Users/sandro/AppData/Local/Temp/ntc2018-vc-3.1.2-g6-r01-20260827-132620", esito: "OK, 0 ERR-MD, 0 ERR-AUDIT, 0 DUBBIO"}
  g7: {p0d: "script locali + gpt-5.6-luna/medium", rilascio: "gpt-5.6-sol/xhigh fresco", esito: "OK, manifest 8/8 confermato"}
---

## 2026-08-27 - G7 e rilascio (CDX)

Il precontrollo P0-D ha confermato 8/8 voci del manifest, percorsi unici, hash e dimensioni. Il controllo finale P2 fresco ha ricalcolato le medesime otto voci, verificato la catena G0-G6 e confermato lo snapshot Markdown `c89175b4fab3660a3e1853a32b53cc4851957bc27d5f041720ba68107b6e3e9b`.

G7 `OK`; rilievi residui: 0 `ERR-MD`, 0 `ERR-AUDIT`, 0 `DUBBIO`, 0 `AF`, 0 `AF-COR`. Scope chiuso e promosso localmente a `VC-OK al 2026-08-27`. Manifest: `verifica-conformita/manifest-sha256-ntc2018-3.1.2-2026-08-27.txt`; verbale: `verifica-conformita/verbale-VC-ntc2018-3.1.2-2026-08-27.md`. Nessun altro file naturale è stato aperto.

## 2026-08-27 - G6 r01 superato (CDX)

G6 eseguito su un unico blocco esterno al workspace, con coordinatore, inventario fonte-prima e verificatore di blocco distinti, tutti P2 `gpt-5.6-sol/xhigh` in contesti freschi. Copertura integrale: titolo, 2 capoversi, 3 frasi e Tab. 3.1.I con 5 categorie, 24 righe-valore, 4 intervalli e 20 valori singoli.

Esito: soltanto `NORM` dichiarate per resa tipografica e celle accorpate; 0 `AF`, 0 `AF-COR`, 0 `ERR-MD`, 0 `ERR-AUDIT`, 0 `DUBBIO`. G6 `OK` al primo giro. Evidenza: `_tmp_render/cap03/vc-3.1.2-20260827/g6-r01/rapporto-consolidato.md`.

## 2026-08-27 - disegno G6 r01 congelato prima dell'esecuzione (CDX)

Il solo scope di una pagina è stato congelato in un pacchetto esterno al workspace con sette file ammessi: due ritagli fonte a 200 e 600 dpi, testo ausiliario limitato al § 3.1.2, frammento Markdown depurato dagli apparati di navigazione, canone neutro, snapshot e istruzioni. Il testo ausiliario non contiene i §§ 3.1.1 o 3.1.3; immagini e Markdown coincidono per hash con le evidenze del preflight. Sono prenotati tre ruoli P2 freschi e separati: inventario source-first, verifica del blocco e coordinamento.

## 2026-08-27 - G0-G5 e preflight G6 chiusi (CDX)

G0-G5 tutti `OK`. Applicati e ricontrollati gli otto soli edit autorizzati: H1, due intestazioni e ripetizione delle cinque etichette accorpate. Il delta ricostruisce esattamente lo snapshot iniziale; nessuna cifra, unità, denominazione o altro testo è cambiato.

La Tab. 3.1.I è stata ricostruita source-first in due contesti indipendenti, Luna `medium` e Sol `xhigh`, con concordanza 24/24 valori. Controllo P2: G4 `OK`, zero rilievi. Snapshot congelato `c89175b4fab3660a3e1853a32b53cc4851957bc27d5f041720ba68107b6e3e9b`; evidenza principale `_tmp_render/cap03/vc-3.1.2-20260827/preflight/rapporto-preflight.md`.

## 2026-08-27 - preflight P0-D Luna completato (CDX)

`gpt-5.6-luna/medium` ha riconciliato integralmente una pagina, due capoversi, tre frasi e la Tab. 3.1.I: cinque categorie, 24 righe-valore, quattro intervalli e 20 valori singoli. Tutte le cifre, l'unità, i separatori e il simbolo `÷` coincidono; struttura e navigazione sono regolari.

Sono congelati cinque soli residui da passare a P1: cassa del titolo, cassa delle due intestazioni, virgolette e markup della didascalia, resa delle cinque righe-categoria accorpate. Evidenza: `_tmp_render/cap03/vc-3.1.2-20260827/preflight/rapporto-p0d-luna.md`. Nessun altro contenuto sarà riaffidato a Sol.

## 2026-08-27 - ripresa autorizzata con corsia Moon/Luna (CDX)

Sandro ha autorizzato la ripresa del solo § 3.1.2. Fonte e Markdown sono stati ricalcolati e coincidono con gli hash registrati; il lucchetto torna `IN-CORSO`. Il precedente passaggio Terra non viene usato come sostituto del nuovo P0-D: il preflight riparte con `gpt-5.6-luna/medium`, mentre Sol riceverà soltanto eventuali residui motivati.

## 2026-08-27 - sospensione e riallineamento del routing (CDX)

Sandro ha fermato lo scope prima della conclusione di G0-G5. Il passaggio P0-S con `gpt-5.6-terra/medium` era terminato; il successivo controllo P1 con `gpt-5.6-sol/high` è stato interrotto e non ha prodotto un esito utilizzabile. G6 e G7 non sono stati avviati; il Markdown vivo è rimasto allo snapshot iniziale.

La skill di orchestrazione è stata resa più stringente: per G2-G5 il passaggio Moon/Luna assorbe prima tutto il deterministico e Sol riceve soltanto i residui motivati. Alla ripresa, il preflight sarà quindi rieseguito con l'identificativo P0-D effettivamente esposto `gpt-5.6-luna`.

## 2026-08-27 - apertura dello scope sul file naturale (CDX)

Scope limitato al solo file `cap03/3.1.2-opere-civili-pesi-propri-dei-materiali-strutturali.md` e al § 3.1.2 del D.M. 17/01/2018, pagina fisica 46 della fonte congelata. La Circolare 7/2019 non contiene un § C3.1.2 corrispondente. Dimensionamento iniziale: una pagina fonte, una tabella, nessuna formula o figura.

Precondizioni di apertura superate: fonte ufficiale presente e ricalcolata con SHA-256 `dda1e397d56d71aa0f5bc457c3ba9b77064a468699dfc37bd056ac6c47105a46`; nessun'altra scheda sul medesimo file e nessun lucchetto concorrente. Snapshot Markdown iniziale SHA-256 `b6df571a6afcccf13b834c8ef6d2f2a21dd341844c36f888a4978ac94f43730c`.

Routing: script locali e Moon `medium` per estrazioni, conteggi e controlli deterministici; Sol `high` per confini, collazione e classificazioni; Sol `xhigh` in contesto fresco per G6 e G7. Nessuna modifica al Markdown eseguita in apertura.
