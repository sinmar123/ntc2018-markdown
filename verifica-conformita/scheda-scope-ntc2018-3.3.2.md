---
scope_id: ntc2018-3.3.2
atti:
  - "D.M. 17/01/2018, § 3.3.2 Velocità di riferimento"
  - "Circolare 21/01/2019 n. 7, § C3.3.2 Velocità di riferimento"
file_markdown: cap03/3.3.2-vento-velocita-di-riferimento.md
fonte_ntc: {pdf: verifica-conformita/fonte-ufficiale/GU-2018-42-SO8-DM-17-01-2018.pdf, pagine_fisiche: 57}
fonte_circolare: {pdf: verifica-conformita/fonte-ufficiale/GU-2019-35-SO5-Circolare-7-2019.pdf, pagine_fisiche: "54-55"}
unita_registro: 1
formule_numerate: 4
tabelle: 0
figure: 1
pagine_fonte: 3
stato: VC-OK
agente: CDX
macchina: P53
presa_in_carico: 2026-08-31T16:00:00+02:00
giro_g6: 2
max_giri: 3
rilievi_aperti: 0
rilievi_persistenti: 0
gate: {G0: OK, G1: OK, G2: OK, G3: OK, G4: OK, G5: OK, G6: OK, G7: OK}
snapshot_sha256: b9c678cce3396e90f10fec3f435b27b8d34dc7379253851dbe1e8f5fbfe1d80e
attesa_decisione: []
prossimo_passo: "aprire il solo scope 3.3.3, già autorizzato; non aprire 3.3.4 prima del suo G7"
routing_previsto:
  p0d: {modello: "script locali", compito: "continuità canonica, hash, render e manifest; G0-G5 riusati dalle evidenze storiche"}
  p1: {modello: "gpt-5.6-sol/high", compito: "applicazione dei soli rilievi congelati"}
  p2: {modello: "gpt-5.6-sol/xhigh", compito: "G6 e G7 sullo scope naturale"}
---

## 2026-08-31 - G7 OK e promozione VC-OK (CDX)

P0-D Luna ha validato 26/26 ingressi del manifest, hash e dimensioni, linter del registro e 311 file con 1.754 collegamenti interni. P2 Sol xhigh ha pronunciato `G7 OK` sullo snapshot `b9c678cce3396e90f10fec3f435b27b8d34dc7379253851dbe1e8f5fbfe1d80e`. Scope promosso a `VC-OK al 2026-08-31`; verbale `verifica-conformita/verbale-VC-ntc2018-3.3.2-2026-08-31.md`.

## 2026-08-31 - apertura dello scope naturale e riuso validato (CDX)

Il confronto canonico fra il file naturale corrente e lo staging della ricomposizione del 26 agosto conferma contenuto normativo identico. Le sole differenze sono i nuovi collegamenti Markdown di navigazione e della nota redazionale. Restano quindi valide e vengono riusate, senza ripeterle, le fasi storiche G0-G5, compresa la verifica della formula e della Fig. C3.3.1.

Dei 32 `ERR-MD` congelati dal G6 aggregato ricadono qui quattro correzioni testuali: cassa del titolo NTC, rimozione dei due punti dopo `dove`, rimozione del punto dopo il numero C3.3.2 con cassa della rubrica conforme alla fonte, e ripristino di `ed in documenti`. Lo scope naturale verrà ora sottoposto integralmente al solo G6 e, se conforme, al G7.

## 2026-08-31 - G6 R02 integrale OK (CDX)

Il primo giro naturale ha confermato zero errori Markdown ma ha respinto il pacchetto per due apparati redazionali non rimossi. Corretto il preparatore, il secondo pacchetto cieco ha coperto integralmente 2 titoli, 7 capoversi, 5 voci di elenco, 4 formule con 4 tag, 7 definizioni, una figura e una didascalia. Esito: zero `ERR-MD`, zero `ERR-AUDIT`, zero `DUBBIO`; G6 `OK` sullo snapshot `b9c678cce3396e90f10fec3f435b27b8d34dc7379253851dbe1e8f5fbfe1d80e`.
