---
scope_id: ntc2018-3.3.9
atti: ["D.M. 17/01/2018, § 3.3.9 Coefficiente dinamico", "Circolare 21/01/2019 n. 7, § C3.3.9 Coefficiente dinamico"]
file_markdown: cap03/3.3.9-vento-coefficiente-dinamico.md
fonte_ntc: {pdf: verifica-conformita/fonte-ufficiale/GU-2018-42-SO8-DM-17-01-2018.pdf, pagine_fisiche: 60}
fonte_circolare: {pdf: verifica-conformita/fonte-ufficiale/GU-2019-35-SO5-Circolare-7-2019.pdf, pagine_fisiche: 75}
unita_registro: 1
formule_numerate: 0
tabelle: 0
figure: 0
pagine_fonte: 2
stato: CHIUSO
agente: CDX
macchina: P53
presa_in_carico: 2026-09-03T15:29:54+02:00
giro_g6: 2
max_giri: 3
rilievi_aperti: 0
rilievi_persistenti: 0
gate: {G0: OK, G1: OK, G2: OK, G3: OK, G4: OK, G5: OK, G6: OK, G7: OK}
snapshot_sha256: 67fd21f95d852f39aee88ecd1766916fcc05866604925daed143626a85190f18
attesa_decisione: []
esecutori:
  preflight: {p0-d: "script locali/CDX", p1: "gpt-5.6-sol/high"}
  correzione-pre-g6: {p1: "gpt-5.6-sol/high"}
  g6-r01: {inventario: "gpt-5.6-sol/xhigh, fonte-prima", blocco-unico: "gpt-5.6-sol/xhigh, NTC p. 60 + Circolare p. 75"}
  g6-r02: {inventario-congelato: "gpt-5.6-sol/xhigh, fonte-prima", confronto-successivo: "gpt-5.6-sol/xhigh, NTC p. 60 + Circolare p. 75"}
  g7: {p0-d: "script locali/CDX", p2-r01: "gpt-5.6-sol/xhigh", p2-r02: "gpt-5.6-sol/xhigh, KO processuale", p2-r03: "gpt-5.6-sol/xhigh, OK"}
routing_effettivo:
  p0d: {modello: "script locali", compito: "hash, continuità canonica, conteggi, indici, lint e render", esito: "OK"}
  p0s: {modello: "non_usato", motivo: "fascicolo di due pagine interamente deterministico", esito: "non_usato"}
  p1: {modello: "gpt-5.6-sol", motivo_escalation: "classificazione dei due titoli difformi e correzione distinta", esito: "G0-G5 OK, due ERR-MD chiusi"}
  p2: {modello: "gpt-5.6-sol", gate: "G6/G7", esito: "G6 R02 OK; G7 R03 OK"}
prossimo_passo: "aprire il solo scope 3.3.10, già autorizzato; il § 3.4 resta fuori perimetro"
---

## 2026-09-03 - apertura dello scope naturale (CDX)

Lucchetto acquisito sul solo file 3.3.9. Gli hash ricalcolati delle fonti ufficiali coincidono con quelli storici: NTC `dda1e397d56d71aa0f5bc457c3ba9b77064a468699dfc37bd056ac6c47105a46`; Circolare `f7c3b8d1f443aadb6b3e020b6b6c19813683492ecaadd2c15bf6bf1939aaed7c`. Il vecchio scope aggregato 3.3 resta sospeso e scaduto; i suoi rilievi sono soltanto candidati storici da ricollocare. I confini del nuovo scope sono i due capoversi NTC di p. fisica 60 e il titolo con unico capoverso C3.3.9 di p. fisica 75.

## 2026-09-03 - G0-G5 prima della correzione (CDX)

Il P0-D ha dimostrato la continuità byte-identica della prosa con lo staging storico e isolato due soli residui. Il P1 `gpt-5.6-sol` high ha chiuso `OK` G0, G1, G2, G4 e G5; G3 è `KO` per la cassa dei due titoli e per il punto aggiunto dopo `C3.3.9`. I tre capoversi sono conformi, senza `AF`, `AF-COR` o `DUBBIO`. Evidenze: `_tmp_render/cap03/vc-3.3.9-20260903/preflight/`.

## 2026-09-03 - fase correttiva pre-G6 e preflight chiuso (CDX)

Un P1 distinto ha applicato soltanto i due `ERR-MD` congelati. Il diff inverso ricostruisce esattamente lo snapshot iniziale; dopo la rigenerazione meccanica dell'indice interno, G3 e G5 sono riconfermati `OK`. Il preflight attesta copertura 2/2 pagine, 2/2 titoli, 3/3 capoversi, zero formule, tabelle, figure, asset e candidati residui; lint, collegamenti e render di una pagina sono `OK`. Snapshot pronto per G6 `67fd21f95d852f39aee88ecd1766916fcc05866604925daed143626a85190f18`.

## 2026-09-03 - G6 R01 cieco concluso OK (CDX)

Un verificatore P2 `gpt-5.6-sol` xhigh in contesto fresco ha formato l'inventario fonte-prima e confrontato integralmente l'unico blocco di due pagine. Copertura: 2/2 titoli, 3/3 capoversi, zero apparati e asset. Esito: zero `ERR-MD`, zero `ERR-AUDIT`, zero `DUBBIO`; sola normalizzazione di a capo per `riferi-` / `mento`. Evidenza: `_tmp_render/cap03/vc-3.3.9-20260903/g6-r01/rapporto-g6-r01.md`. G7 avviato sullo snapshot invariato `67fd21f95d852f39aee88ecd1766916fcc05866604925daed143626a85190f18`.

## 2026-09-03 - G7 OK e chiusura VC-OK (CDX)

Il P0-D ha ricalcolato 24/24 record del manifest; il P2 fresco `gpt-5.6-sol` xhigh ha verificato la continuità della catena, la chiusura esatta dei due rilievi, la validità del G6 e lo snapshot invariato. G7 `OK`; verbale `verifica-conformita/verbale-VC-ntc2018-3.3.9-2026-09-03.md`. Lo scope passa a `CHIUSO` e il solo 3.3.10 resta autorizzato come prossimo file.

## 2026-09-03 - riapertura processuale dopo G7 R02 (CDX)

Un nuovo P2 fresco ha confermato contenuto normativo, snapshot e manifest 25/25, ma ha chiuso G7 R02 `KO` per tre difetti di prova: congelamento fonte-prima G6 non dimostrato, ricognizione G1 non abbastanza ripetibile sullo scope a due atti e documenti ancora riferiti al manifest precedente. La promozione è stata sospesa e lo scope riportato `IN-CORSO`; nessun rilievo riguarda il testo del § 3.3.9.

## 2026-09-03 - G1 e G6 R02 completati (CDX)

La ricognizione G1 R02 include ora entrambe le schede ufficiali, le stringhe di ricerca ripetibili e la scadenza al 22 marzo 2025 delle sospensioni del D.M. 9 marzo 2023. G6 R02 ha congelato prima del confronto inventario, esito provvisorio e criterio con hash verificati; soltanto dopo è stato reso disponibile l'estratto. Il confronto integrale ha chiuso `G6 OK`, con 2/2 titoli, 3/3 capoversi, zero apparati, zero `ERR-MD`, `ERR-AUDIT` e `DUBBIO`. Evidenze: `_tmp_render/cap03/vc-3.3.9-20260903/g6-r02/`. Il target resta invariato; occorre un nuovo G7 fresco sul manifest R03.

## 2026-09-03 - G7 R03 OK e chiusura definitiva VC-OK (CDX)

Il P0-D ha ricalcolato 44/44 record del manifest R03; il P2 fresco `gpt-5.6-sol` xhigh ha riconfermato integralmente G0-G6, chiuso i tre rilievi processuali R02 e autorizzato la promozione sullo snapshot invariato. G7 R03 `OK`; SHA-256 del manifest `702e57fcded60a9547b132652082a260d3667536b9c9532a86cfc4ce9e3b06ce`. Lo scope passa a `CHIUSO`; il solo 3.3.10 resta autorizzato come prossimo file.
