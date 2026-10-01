---
scope_id: ntc2018-3.2.3
atti:
  - "D.M. 17/01/2018, § 3.2.3 Valutazione dell'azione sismica"
  - "Circolare 21/01/2019 n. 7, § C3.2.3 Valutazione dell'azione sismica"
file_markdown: cap03/3.2.3-azione-sismica-valutazione-dell-azione-sismica.md
fonte_ntc: {pdf: verifica-conformita/fonte-ufficiale/GU-2018-42-SO8-DM-17-01-2018.pdf, pagine_fisiche: 51-55}
fonte_circolare: {pdf: verifica-conformita/fonte-ufficiale/GU-2019-35-SO5-Circolare-7-2019.pdf, pagine_fisiche: 51-54}
unita_registro: 1
formule_numerate: 12
tabelle: 4
figure: 2
pagine_fonte: 9
stato: VC-OK
agente: CDX
macchina: P53
presa_in_carico: 2026-08-28T16:05:43+02:00
giro_g6: 4
max_giri: 4
rilievi_aperti: 0
rilievi_persistenti: 0
gate: {G0: OK, G1: OK, G2: OK, G3: OK, G4: OK, G5: OK, G6: OK, G7: OK}
snapshot_sha256: f2a3371c8beea285ed11b6a18e2a8169b4284740e6583742843345d5cc767086
attesa_decisione: []
prossimo_passo: "aprire il solo scope 3.2.4, già autorizzato"
routing_effettivo:
  p0d: {modello: "script locali + gpt-5.6-luna/medium", compito: "hash, confini, inventario, collazione, formule, tabelle, figure, render, link e candidati", esito: "completato con due ERR-AUDIT poi chiusi"}
  p0s: {modello: "non_usato", motivo: "da valutare dopo il passaggio deterministico", esito: "non avviato"}
  p1: {modello: "gpt-5.6-sol/high", motivo_escalation: "residui testuali e glifi protetti emersi dopo P0-D", esito: "completato, 0 residui"}
  p2: {modello: "gpt-5.6-sol/xhigh", gate: "apparati critici, controllo mirato e G7", esito: "G7 OK; manifest 47/47 e snapshot promuovibile"}
esecutori:
  apertura: {coordinamento: "CDX/sessione principale", controlli_meccanici: "script locali"}
  preflight: {p0d: "gpt-5.6-luna/medium", g0_g1: "CDX su fonti congelate", p1_residui: "gpt-5.6-sol/high se necessari"}
  apparati: {passaggio_a: "gpt-5.6-luna/medium", passaggio_b: "gpt-5.6-sol/xhigh", riconciliazione: "gpt-5.6-sol/xhigh"}
  g6_formale:
    fonte_prima: {agente: "vc_323_g6_source_first", modello: "gpt-5.6-sol/xhigh", perimetro: "nove pagine fonte senza accesso al Markdown"}
    blocco_a: {agente: "vc_323_g6_formal_a", modello: "gpt-5.6-sol/xhigh", pagine: "NTC fisiche 51-53"}
    blocco_b: {agente: "vc_323_g6_formal_b", modello: "gpt-5.6-sol/xhigh", pagine: "NTC fisiche 54-55 e Circolare fisica 51"}
    blocco_c: {agente: "vc_323_g6_formal_c", modello: "gpt-5.6-sol/xhigh", pagine: "Circolare fisiche 52-54"}
    coordinamento: {agente: "vc_323_g6_formal_coord", modello: "gpt-5.6-sol/xhigh"}
  g6_r04:
    preflight: {agente: "vc_323_r04_p0d", modello: "gpt-5.6-luna/medium", esito: "P0-D OK"}
    fonte_prima: {agente: "vc_323_r04_source_first", modello: "gpt-5.6-sol/xhigh", perimetro: "nove pagine fonte senza accesso al Markdown"}
    blocco_a: {agente: "vc_323_r04_a", modello: "gpt-5.6-sol/xhigh", pagine: "NTC 51-52 e Circolare 54"}
    blocco_b: {agente: "vc_323_r04_b", modello: "gpt-5.6-sol/xhigh", pagine: "NTC 53-54 e Circolare 51"}
    blocco_c: {agente: "vc_323_r04_c", modello: "gpt-5.6-sol/xhigh", pagine: "NTC 55 e Circolare 52-53"}
    coordinamento: {agente: "vc_323_r04_coord", modello: "gpt-5.6-sol/xhigh"}
  deroga_finale:
    controllo_tabella: {agente: "vc_323_deroga_tab_vii_r02", modello: "gpt-5.6-sol/xhigh", esito: "OK, 12/12 celle e 1/1 didascalia"}
    preflight: {agente: "vc_323_deroga_p0d", modello: "gpt-5.6-luna/medium", esito: "P0-D OK"}
    g7_p0d: {agente: "vc_323_g7_p0d_finale", modello: "gpt-5.6-luna/medium", esito: "47/47 manifest"}
    g7_p2: {agente: "vc_323_g7_p2_finale", modello: "gpt-5.6-sol/xhigh", esito: "G7 OK"}
---

## 2026-08-29 - G7 OK e promozione VC-OK per deroga dichiarata (CDX)

Sandro ha autorizzato la correzione del solo residuo certo del G6 R04 e, in luogo di un quinto G6 integrale, un controllo indipendente mirato, un nuovo preflight P0-D Moon e il G7 P2 Sol. La riga 173 è stata modificata da `Categoria di sottosuolo` a `Categoria sottosuolo`; il confronto posizionale rileva questa sola differenza e nessuna variazione nel numero delle righe.

Il primo controllo mirato ha confermato 12/12 celle ma ha rilevato due difformità nel solo estratto di audit, poi riclassificate `ERR-AUDIT`: il trattino è normalizzazione dichiarata e il punto finale non era presente nel target. Un secondo verificatore indipendente, su estratto riallineato e normalizzazioni dichiarate, ha confermato 12/12 celle e 1/1 didascalia, con zero rilievi. Il controllo mirato non costituisce un quinto G6 integrale; G6 è chiuso `OK` per deroga esplicita sullo snapshot finale.

Il precontrollo G7 P0-D Moon ha confermato 47/47 hash e 47/47 dimensioni del manifest, senza duplicati o voci estranee. Il giudizio P2 Sol ha pronunciato `G7 OK`: 9/9 pagine fonte, 12 gruppi di formule numerate, 4 tabelle, 2 figure, 4 `AF`, 0 `AF-COR`, 0 `ERR-MD`, 0 `ERR-AUDIT` aperti e 0 `DUBBIO`. Lo scope è promosso a `VC-OK al 2026-08-29` sullo snapshot `f2a3371c8beea285ed11b6a18e2a8169b4284740e6583742843345d5cc767086`. Verbale: `verifica-conformita/verbale-VC-ntc2018-3.2.3-2026-08-29.md`.

## 2026-08-28 - G6 R04 chiuso KO (CDX)

Il G6 R04 ha coperto 9/9 pagine con fonte-prima congelata e partizione ridisegnata, ricomposta 263/263 righe. Il coordinamento ha chiuso cinque `ERR-AUDIT`: accento di `é in genere`, blocco `nelle quali:`, sistemi di formula e resa dei tag. Zero dubbi.

Resta un solo `ERR-MD`: la prima intestazione della Tab. 3.2.VII reca `Categoria di sottosuolo`, mentre la fonte stampa `Categoria sottosuolo`. Nessuna correzione applicata. Pronuncia `G6 R04 KO`; poiché `giro_g6: 4` coincide con `max_giri: 4`, l'esatta correzione e un quinto G6 integrale richiedono nuova autorizzazione esplicita di Sandro. Evidenza autoritativa in `_tmp_render/cap03/vc-3.2.3-20260828/g6-r04/g6-formale/rapporto-coordinamento.md`.

## 2026-08-28 - correzioni autorizzate e apertura G6 R04 (CDX)

Sandro ha autorizzato l'aumento di `max_giri` da 3 a 4, l'applicazione delle sole tre famiglie congelate e un nuovo G6 integrale. Sono state modificate esclusivamente quattro righe del target: ripristino di `di risposta di progetto`, aggiunta della virgola dopo l'intervallo temporale e resa matematica delle otto variabili censite. Il confronto posizionale non mostra altre modifiche.

Nuovo snapshot: `e13bf499661ea40dbff3ad43623aca94846dfea92af9cb3ffc4cca10a5816ec0`, 32.905 byte. G6 R04 aperto con confini da ridisegnare e verificatori nuovi.

## 2026-08-28 - G6 formale giro 3 chiuso KO (CDX)

Il controllo conclusivo ha rispettato la procedura completa: inventario fonte-prima congelato, tre blocchi disgiunti di tre pagine con verificatori nuovi `gpt-5.6-sol/xhigh` e coordinamento indipendente. Gli ingressi sono rimasti integri, la copertura è 9/9 pagine e il blocco A è risultato conforme.

Il coordinamento ha chiuso come `ERR-AUDIT` i due falsi rilievi sui tag e quello sull'accento di `é in genere`. Restano tre famiglie `ERR-MD`: omissione di `di risposta di progetto` nel § 3.2.3.4, virgola omessa dopo l'intervallo temporale nella Circolare e otto variabili matematiche rese come testo corrente. Zero dubbi. Pronuncia `G6 KO`; con `giro_g6: 3` uguale a `max_giri: 3`, le correzioni e un quarto G6 integrale richiedono autorizzazione esplicita di Sandro. Lista autoritativa e prove in `_tmp_render/cap03/vc-3.2.3-20260828/g6-formale/rapporto-coordinamento.md`.

## 2026-08-28 - apertura del G6 formale conclusivo (CDX)

In seguito al precontrollo G7, il precedente materiale G6 resta storico ma non viene usato come base sufficiente per il rilascio. È stato aperto il giro 3 con inventario fonte-prima indipendente e congelato, tre blocchi disgiunti di tre pagine affidati a verificatori nuovi `gpt-5.6-sol/xhigh` e coordinamento finale separato. Il conteggio delle formule numerate è stato allineato ai 12 gruppi effettivi dello snapshot finale.

## 2026-08-28 - G6 chiuso sullo snapshot finale (CDX)

Il G6 R03 ha completato una nuova lettura integrale delle nove pagine e non ha prodotto nuovi `ERR-MD`. I suoi due rilievi sono stati riclassificati `ERR-AUDIT`: `\tag{...}` è la sintassi sorgente resa con parentesi quadre dal renderer canonico, mentre `T_e` nella `[3.2.11]` è confermato dalla fonte e registrato come `AF-3.2.3-03`.

Bilancio G6 complessivo: R01 e R02 hanno individuato due errori concordanti, poi corretti; R03 sul nuovo snapshot ha 0 errori reali dopo adjudicazione. G6 `OK`, 0 rilievi aperti e 0 dubbi. Prossimo gate: G7.

## 2026-08-28 - correzioni del G6 R01/R02 e apertura R03 (CDX)

I due confronti ciechi indipendenti R01 e R02 hanno concordato su due `ERR-MD`: virgola omessa dopo il primo `$T_{is}$` nella prosa NTC e pedici minuscoli in `\rho_{x,y}` al posto di `\rho_{X,Y}` nella formula `[C3.2.5]`. Entrambi sono stati corretti. Il rilievo R02 su `é in genere` è stato riclassificato `ERR-AUDIT` perché il livello caratteri del PDF conferma `é` U+00E9.

Nuovo snapshot target: `636bc58f3d21d214a2b980fd73499409d5a4fbf089d06b016353e02461897192`. Nuovo frammento depurato: `587605026f864d3c1efad435231ab736243bd3e953b73c6ec7c004c510a93f4a`. È stato aperto il G6 R03 integrale con un verificatore nuovo Moon/Luna.

## 2026-08-28 - G0-G5 chiusi e G6 avviato (CDX)

Il target è stato portato allo snapshot SHA-256 `dcdfcd8e259c5197c8997fe43e79be6eb055708588d99fb2181281b8b9f414e5`. Il controllo critico ha riconciliato 20/20 blocchi formula, 55/55 celle logiche, 2/2 asset e 2/2 didascalie; quattro anomalie della fonte sono conservate in `cap03/annotazioni/3.2.3-anomalie-fonte.md`, con 0 `AF-COR` e 0 `DUBBIO`. Il render finale di nove pagine e i 1.754 collegamenti interni sono conformi.

Il G6 è stato aperto con due pacchetti ciechi indipendenti sul frammento depurato SHA-256 `51aa71298d70851d5e7656fb4f78064ba4f70f58b6af43648c1a5910c9328b83`, nove ritagli fonte a 600 dpi e due asset.

## 2026-08-28 - apertura dello scope sul file naturale (CDX)

Scope limitato al solo file `cap03/3.2.3-azione-sismica-valutazione-dell-azione-sismica.md`, al § 3.2.3 del D.M. 17/01/2018 e al § C3.2.3 della Circolare 7/2019. Il controllo diretto delle rubriche ha accertato i confini sulle pagine fisiche NTC 51-55 e Circolare 51-54, con esclusione dei §§ 3.2.2, 3.2.4, C3.2.2 e C3.3.

Precondizioni superate: fonti ufficiali presenti, nessun'altra scheda sul medesimo file e precedente scope 3.2.2 chiuso `VC-OK`. Snapshot Markdown iniziale SHA-256 `a4ba890ee9712149e5c5b3e2b88769135cda83a5e21b95201d1cb1352ce33660`.

Dimensionamento preliminare: nove pagine fonte, quindici occorrenze di tag di formula nel Markdown, quattro tabelle e due figure. Routing semplificato richiesto da Sandro: script e Moon/Luna per tutto il deterministico, Sol soltanto per residui motivati e gate critici.
