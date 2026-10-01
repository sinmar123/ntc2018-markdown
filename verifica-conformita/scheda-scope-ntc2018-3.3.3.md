---
scope_id: ntc2018-3.3.3
atti:
  - "D.M. 17/01/2018, § 3.3.3 Azioni statiche equivalenti"
  - "Circolare 21/01/2019 n. 7, § C3.3.3 Azioni statiche equivalenti"
file_markdown: cap03/3.3.3-vento-azioni-statiche-equivalenti.md
fonte_ntc: {pdf: verifica-conformita/fonte-ufficiale/GU-2018-42-SO8-DM-17-01-2018.pdf, pagine_fisiche: 57}
fonte_circolare: {pdf: verifica-conformita/fonte-ufficiale/GU-2019-35-SO5-Circolare-7-2019.pdf, pagine_fisiche: 55}
unita_registro: 1
formule_numerate: 0
tabelle: 0
figure: 0
pagine_fonte: 2
stato: VC-OK
agente: CDX
macchina: P53
presa_in_carico: 2026-08-31T17:00:00+02:00
giro_g6: 1
max_giri: 3
rilievi_aperti: 0
rilievi_persistenti: 0
gate: {G0: OK, G1: OK, G2: OK, G3: OK, G4: OK, G5: OK, G6: OK, G7: OK}
snapshot_sha256: ea34a61cc5c8f301a8e7a996f0bc08359070df1e74c7562c1d40aa6224a81930
attesa_decisione: []
prossimo_passo: "aprire il solo scope 3.3.4, già autorizzato; non aprire 3.3.5 prima del suo G7"
routing_previsto:
  p0d: {modello: "script locali", compito: "continuità, hash, render e manifest; G0-G5 riusati"}
  p1: {modello: "gpt-5.6-sol/high", compito: "applicazione dei soli rilievi congelati"}
  p2: {modello: "gpt-5.6-sol/xhigh", compito: "G6 e G7 sullo scope naturale"}
---

## 2026-08-31 - G7 OK e promozione VC-OK (CDX)

P0-D Luna ha validato 19/19 ingressi, linter e indici; P2 Sol xhigh ha pronunciato `G7 OK` sullo snapshot `ea34a61cc5c8f301a8e7a996f0bc08359070df1e74c7562c1d40aa6224a81930`. Verbale `verifica-conformita/verbale-VC-ntc2018-3.3.3-2026-08-31.md`.

## 2026-08-31 - apertura e riuso validato (CDX)

Il confronto canonico col relativo staging della ricomposizione del 26 agosto conferma contenuto normativo identico; sono scomparsi soltanto i vecchi wikilink di navigazione, come previsto. Sono riusati G0-G5 storici. Dei rilievi congelati ricadono qui soltanto la cassa del titolo NTC e il punto/cassa del titolo C3.3.3.

## 2026-08-31 - G6 R01 integrale OK (CDX)

Il verificatore P2 in contesto fresco ha confrontato 2/2 pagine, 2/2 titoli e 5/5 capoversi. Esito `G6 OK`: zero `ERR-MD`, zero `ERR-AUDIT`, zero `DUBBIO`.
