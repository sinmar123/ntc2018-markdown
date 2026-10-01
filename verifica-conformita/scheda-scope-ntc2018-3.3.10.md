---
scope_id: ntc2018-3.3.10
atti: ["D.M. 17/01/2018, § 3.3.10 Avvertenze progettuali", "Circolare 21/01/2019 n. 7, § C3.3.10 Avvertenze progettuali"]
file_markdown: cap03/3.3.10-vento-avvertenze-progettuali.md
fonte_ntc: {pdf: verifica-conformita/fonte-ufficiale/GU-2018-42-SO8-DM-17-01-2018.pdf, pagine_fisiche: 60}
fonte_circolare: {pdf: verifica-conformita/fonte-ufficiale/GU-2019-35-SO5-Circolare-7-2019.pdf, pagine_fisiche: 75}
unita_registro: 1
formule_numerate: 0
tabelle: 0
figure: 0
pagine_fonte: 2
stato: CHIUSO
agente: CDX
macchina: W520
presa_in_carico: 2026-09-03T18:10:28+02:00
giro_g6: 1
max_giri: 3
rilievi_aperti: 0
rilievi_persistenti: 0
gate: {G0: OK, G1: OK, G2: OK, G3: OK, G4: OK, G5: OK, G6: OK, G7: OK}
snapshot_sha256: 888c0d25d5eae5094ded93d635002b3a22964b1294a1a7b98f2ffb4441d98097
attesa_decisione: []
esecutori:
  preflight-p0d: {modello: "gpt-5.6-luna", ragionamento: "medium", esito: "2 titoli, 7 capoversi, zero apparati, 4 candidati"}
  g0-g1: {modello: "gpt-5.6-sol", ragionamento: "high", esito: "OK limitatamente allo scope"}
  g2-g5: {modello: "gpt-5.6-sol", ragionamento: "high", esito: "G2/G4/G5 OK; G3 KO con 4 ERR-MD"}
  correzione-p1: {modello: "gpt-5.6-sol", ragionamento: "high", esito: "4 ERR-MD corretti; AF-3.3-14 conservata"}
  post-correzione-p0d: {modello: "gpt-5.6-luna", ragionamento: "medium", esito: "hash, diff, conteggi, link, lint e indici OK"}
  post-correzione-p1: {modello: "gpt-5.6-sol", ragionamento: "high", esito: "G3/G5 OK; zero residui"}
  g6-r01: {modello: "gpt-5.6-sol", ragionamento: "xhigh", esito: "OK, copertura 9/9; 1 AF, 0 AF-COR; zero ERR-MD, ERR-AUDIT e DUBBIO"}
  g7: {p0-d: "gpt-5.6-luna/medium, manifest 39/39", p2: "gpt-5.6-sol/xhigh, OK"}
routing_effettivo:
  p0d: {modello: "gpt-5.6-luna e script locali", compito: "hash, conteggi, continuità, lint, indici e render", esito: "preflight finale OK"}
  p0s: {modello: "non_usato", motivo: "scope di due pagine con fascicolo semplice", esito: "non_usato"}
  p1: {modello: "gpt-5.6-sol", motivo_escalation: "G0-G1 e classificazione dei quattro residui isolati da P0-D", esito: "G0-G5 OK dopo correzione distinta e riconferma"}
  p2: {modello: "gpt-5.6-sol", gate: "G6/G7", esito: "G6 R01 e G7 OK"}
prossimo_passo: "nessuna attività sul file; attendere un nuovo via libera prima di aprire C3.3.11, il § 3.4 o altri scope"
---

## 2026-09-03 - apertura dello scope naturale (CDX)

Lucchetto acquisito sul solo file 3.3.10. Gli hash ricalcolati delle fonti ufficiali coincidono con quelli storici: NTC `dda1e397d56d71aa0f5bc457c3ba9b77064a468699dfc37bd056ac6c47105a46`; Circolare `f7c3b8d1f443aadb6b3e020b6b6c19813683492ecaadd2c15bf6bf1939aaed7c`. Nessun altro scope usa il file vivo. Snapshot iniziale `24443b293eeba541ae080baaa152713cf32c4ac8db70ce33fcffc507fec370b2`. I confini indicativi sono la pagina fisica NTC 60 e la pagina fisica Circolare 75; saranno accertati a vista prima di G0.

## 2026-09-03 - P0-D e G0-G1 completati (CDX)

Il P0-D `gpt-5.6-luna/medium` ha inventariato 2 titoli, 7 capoversi, zero formule, tabelle, figure e asset, ricollocando quattro candidati testuali. Il P1 `gpt-5.6-sol/high` ha chiuso G0 `OK` sui confini esatti dei due ritagli e G1 `OK` con ricognizione ufficiale ripetibile limitata allo scope: il D.M. 9 marzo 2023 non incide sul § 3.3.10. Evidenze in `_tmp_render/cap03/vc-3.3.10-20260903/preflight/`.

## 2026-09-03 - G2-G5 e rilievi pre-G6 (CDX)

Il P1 ha chiuso G2, G4 e G5 `OK`; G3 è `KO` sullo snapshot iniziale per quattro `ERR-MD` congelati: cassa del titolo NTC, `dei`/`di fenomeni`, `e il`/`ed il flutter`, cassa e punto del titolo Circolare. La sequenza della fonte `nei con fronti` è invece `AF`, da conservare alla lettera e documentare come `AF-3.3-14`. Nessun `AF-COR` e nessun `DUBBIO`. La correzione è affidata a un P1 distinto.

## 2026-09-03 - correzione e riconferma del preflight (CDX)

Un correttore P1 distinto ha applicato esclusivamente i quattro interventi congelati e ha registrato `AF-3.3-14`, conservando `nei con fronti`. Il P0-D ha verificato hash, diff, inventario, link, linter e indici; un P1 verificatore ha riconfermato G3 e G5 `OK`. Il target corrente ha SHA-256 `888c0d25d5eae5094ded93d635002b3a22964b1294a1a7b98f2ffb4441d98097`; zero `ERR-MD`, zero `ERR-AUDIT`, zero `DUBBIO`. Il render finale di una pagina è stato controllato integralmente. Il preflight G0-G5 è chiuso e il pacchetto pulito per G6 è pronto.

## 2026-09-03 - G6 R01 cieco completato (CDX)

Un P2 fresco `gpt-5.6-sol/xhigh` ha formato e congelato, prima di vedere il Markdown, inventario, esito provvisorio e criterio fonte-prima; il coordinatore ne ha ricalcolato gli hash prima di autorizzare il confronto. Il pacchetto input è risultato integro 11/11 e il confronto ha coperto 9/9 oggetti testuali. L'iniziale classificazione prudenziale della sola spaziatura `NTC 2008`/`NTC2008` come seconda AF è stata riesaminata da un P1 distinto e ricondotta alla normalizzazione dichiarata n. 1; il medesimo P2 l'ha confermato in addendum. Esito autoritativo G6 `OK`: 1 `AF` (`AF-3.3-14`), 0 `AF-COR`, zero `ERR-MD`, zero `ERR-AUDIT` e zero `DUBBIO`.

## 2026-09-03 - G7 e promozione VC-OK (CDX)

Il P0-D ha ricalcolato 39/39 record del manifest, fonti, snapshot, congelamento 3/3 e input G6 11/11. Un P2 fresco `gpt-5.6-sol/xhigh` ha ripetuto i controlli contenutistici e processuali, ispezionato ritagli e render e confermato G7 `OK` senza rilievi. Manifest SHA-256 `2884803bb46b52cdd662e1ad606e7d6695ecff446a7a7c52f272566853939b57`; snapshot promosso `888c0d25d5eae5094ded93d635002b3a22964b1294a1a7b98f2ffb4441d98097`. Stato locale `VC-OK al 2026-09-03`; l'intero corpus master resta invariato. Il metadato macchina è stato allineato a `W520`, coerentemente col percorso del workspace e col giornale generato dallo strumento condiviso.
