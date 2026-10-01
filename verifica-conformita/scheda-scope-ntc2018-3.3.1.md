---
scope_id: ntc2018-3.3.1
atti:
  - "D.M. 17/01/2018, § 3.3.1 Velocità base di riferimento"
  - "Circolare 21/01/2019 n. 7, § C3.3.1 Velocità base di riferimento"
file_markdown: cap03/3.3.1-vento-velocita-base-di-riferimento.md
fonte_ntc: {pdf: verifica-conformita/fonte-ufficiale/GU-2018-42-SO8-DM-17-01-2018.pdf, pagine_fisiche: 56}
fonte_circolare: {pdf: verifica-conformita/fonte-ufficiale/GU-2019-35-SO5-Circolare-7-2019.pdf, pagine_fisiche: 54}
unita_registro: 1
formule_numerate: 2
tabelle: 1
figure: 1
pagine_fonte: 2
stato: VC-OK
agente: CDX
macchina: P53
presa_in_carico: 2026-08-31T15:07:35+02:00
giro_g6: 2
max_giri: 3
rilievi_aperti: 0
rilievi_persistenti: 0
gate: {G0: OK, G1: OK, G2: OK, G3: OK, G4: OK, G5: OK, G6: OK, G7: OK}
snapshot_sha256: f9116d86bd340884e93151d8e295b6e7b06daecc21771bd1e9ca3d13ed00a1ba
attesa_decisione: []
prossimo_passo: "aprire il solo scope 3.3.2, già autorizzato; non aprire 3.3.3 prima del suo G7"
routing_previsto:
  p0d: {modello: "script locali", compito: "continuità canonica della ricomposizione, hash, render e link; G0-G5 riusati dalle evidenze storiche"}
  p1: {modello: "gpt-5.6-sol/high", compito: "applicazione dei soli rilievi congelati e del residuo R01"}
  p2: {modello: "gpt-5.6-sol/xhigh", compito: "apparati critici, G6 e G7"}
---

## 2026-08-31 - G7 OK e promozione VC-OK (CDX)

Il precontrollo P0-D Luna ha verificato 27/27 percorsi, dimensioni e SHA-256 del manifest finale, senza duplicati; linter del registro con zero errori e zero avvisi, indici interni 311/311 e 1.754 collegamenti validi. Il decisore P2 Sol xhigh ha pronunciato `G7 OK` sullo snapshot `f9116d86bd340884e93151d8e295b6e7b06daecc21771bd1e9ca3d13ed00a1ba`.

Bilancio finale: 2 titoli, 5 capoversi, 3 blocchi formula, 2 tag, 4 definizioni, 50 celle logiche, una figura e 2 didascalie. Zero `ERR-MD`, zero `ERR-AUDIT`, zero `DUBBIO`, zero `AF` e un `AF-COR` conforme. Scope promosso a `VC-OK al 2026-08-31`. Verbale: `verifica-conformita/verbale-VC-ntc2018-3.3.1-2026-08-31.md`.

## 2026-08-31 - G6 R02 integrale OK (CDX)

Il secondo giro naturale, eseguito da un P2 Sol xhigh in contesto fresco su pacchetto rigenerato, ha coperto il 100% del file: 2/2 titoli, 5/5 capoversi, 3/3 blocchi formula, 2/2 tag, 4/4 definizioni, 50/50 celle logiche, 2/2 didascalie e 1/1 figura. Esito: zero `ERR-MD`, zero `ERR-AUDIT`, zero `DUBBIO`, un `AF-COR` conforme e sole normalizzazioni dichiarate. G6 `OK`; prossimo gate G7.

## 2026-08-31 - correzione del residuo R01 e apertura G6 R02 (CDX)

Il G6 R01 naturale ha ricontrollato l'intero piccolo scope e confermato integralmente prosa, formule, 50/50 celle della Tab. 3.3.I, figura e didascalia. Ha individuato un solo `ERR-MD` non emerso nel giro aggregato: anche la rubrica C3.3.1 è tutta maiuscola nella fonte. Il correttore P1 distinto ha modificato soltanto quella riga; la prova inversa ha ricostruito esattamente l'hash precedente.

Dopo la rigenerazione canonica dell'indice interno, il nuovo snapshot è `f9116d86bd340884e93151d8e295b6e7b06daecc21771bd1e9ca3d13ed00a1ba`. Aperto G6 R02 integrale in contesto P2 fresco, su pacchetto nuovo e senza trasmettere l'esito R01.

## 2026-08-31 - riuso validato delle fasi storiche e G6 R01 KO (CDX)

La ricomposizione del 26 agosto aveva superato 506/506 confronti canonici complessivi. Il confronto fra il file naturale corrente e il relativo staging ha confermato contenuto normativo identico; le sole differenze anteriori alle correzioni erano i nuovi apparati di navigazione e la forma del collegamento alla nota redazionale. Sono pertanto riusati G0-G5, gli inventari e il controllo storico di formule, tabella e figura, senza ripeterli.

Dei 32 `ERR-MD` del G6 aggregato ricadevano qui soltanto la cassa del titolo 3.3.1 e il punto aggiunto dopo il numero C3.3.1. Il correttore P1 distinto li ha applicati su due sole righe. La Fig. 3.3.1, mancante dalla cartella viva dopo la ricomposizione, è stata ripristinata byte-identica dalla copia già verificata del vecchio G4/G6, SHA-256 `59efa69fa7c618cc42b35bde4cc9327a2656b720b97ee7380246da7027c13f4c`.

Il G6 R01 naturale è stato chiuso `KO` con un solo residuo di cassa nella rubrica C3.3.1, zero `ERR-AUDIT` e zero `DUBBIO`. Nessun altro contenuto è risultato difforme.

## 2026-08-31 - apertura dello scope sul file naturale (CDX)

Scope limitato al solo file `cap03/3.3.1-vento-velocita-base-di-riferimento.md` e ai §§ 3.3.1 e C3.3.1 delle due fonti ufficiali congelate. Il vecchio scope aggregato `ntc2018-3.3` resta evidenza storica e non viene riaperto; i suoi rilievi sono soltanto candidati da verificare nuovamente.

Precondizioni superate: registro locale letto per primo, § 3.2 interamente `VC-OK`, autorizzazione di Sandro estesa ai dieci file naturali 3.3.1-3.3.10, nessun altro scope naturale del § 3.3 in corso. Snapshot Markdown iniziale SHA-256 `78cc5089f03ee52dd20cc79251724029d527ff7330b855bbb796dd6c70cee672`, 4.240 byte e 70 righe.

Dimensionamento preliminare: due pagine fonte condivise, due gruppi di formule numerate, una tabella e una figura nella Norma; testo in prosa nella Circolare. I confini verranno congelati visivamente nel preflight prima di chiudere G0. Routing semplificato: script e Luna per il deterministico, Sol soltanto per residui motivati e gate critici. Nessuna modifica normativa eseguita in apertura.
