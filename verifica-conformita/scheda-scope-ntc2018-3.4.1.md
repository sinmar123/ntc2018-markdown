---
scope_id: ntc2018-3.4.1
atti:
  - "D.M. 17/01/2018, § 3.4.1 CARICO DELLA NEVE SULLE COPERTURE"
  - "Circolare 21/01/2019 n. 7 C.S.LL.PP., § C3.4.1 CARICO DELLA NEVE SULLE COPERTURE"
file_markdown: cap03/3.4.1-neve-carico-della-neve-sulle-coperture.md
fonte_ntc: {pdf: verifica-conformita/fonte-ufficiale/GU-2018-42-SO8-DM-17-01-2018.pdf, pagine_fisiche: 61}
fonte_circolare: {pdf: verifica-conformita/fonte-ufficiale/GU-2019-35-SO5-Circolare-7-2019.pdf, pagine_fisiche: 76}
unita_registro: 1
formule_numerate: 1
tabelle: 0
figure: 0
pagine_fonte: 2
stato: CHIUSO
agente: CDX
macchina: W520
presa_in_carico: 2026-09-04T08:29:36+02:00
giro_g6: 1
max_giri: 3
rilievi_aperti: 0
rilievi_persistenti: 0
gate: {G0: OK, G1: OK, G2: OK, G3: OK, G4: OK, G5: OK, G6: OK, G7: OK}
snapshot_sha256: aad946d48ddbf921a92851e8568a813e4df69a072ce05a9c360f6e2b95a46687
attesa_decisione: []
prossimo_passo: "nessuna attività sul file; attendere un nuovo via libera prima di aprire il solo scope 3.4.2 o altri scope"
routing_effettivo:
  p0d: {modello: "script locali; gpt-5.6-luna/medium", compito: "hash, confini, estrazioni, inventario source-first, diff, link, render e post-correzione", esito: "G3 post-correzione e preflight OK"}
  p0s: {modello: "non_usato", motivo: "scope breve e determinabile", esito: "non_usato"}
  p1: {modello: "gpt-5.6-sol/high", motivo_escalation: "G0-G1, confini e classificazione/correzione dei residui", esito: "G0-G3 e G5 OK; due rubriche corrette"}
  p2: {modello: "gpt-5.6-sol/xhigh", gate: "G4, G6 e G7", esito: "G4, G6 R01 e G7 OK"}
esecutori:
  apertura: {coordinamento: "CDX/sessione principale", controlli_meccanici: "script locali"}
  preflight-p0d: {modello: "gpt-5.6-luna", ragionamento: "medium", esito: "inventario, candidati, diff, render e post-correzione OK"}
  g0-g1: {modello: "gpt-5.6-sol", ragionamento: "high", esito: "OK limitatamente allo scope"}
  g2-g5: {modello: "gpt-5.6-sol", ragionamento: "high", esito: "G2/G5 OK; G3 corretto e riconfermato"}
  g4: {modello: "gpt-5.6-sol", ragionamento: "xhigh", esito: "una formula e quattro definizioni conformi; zero altri apparati"}
  correzione-p1: {modello: "gpt-5.6-sol", ragionamento: "high", esito: "due famiglie ERR-MD corrette senza altre variazioni normative"}
  g6-r01: {modello: "gpt-5.6-sol", ragionamento: "xhigh", esito: "OK, copertura 14/14; 0 AF e AF-COR; zero ERR-MD, ERR-AUDIT e DUBBIO"}
  g7: {p0-d: "gpt-5.6-luna/medium, manifest 38/38", p2: "gpt-5.6-sol/xhigh, OK"}
---

## 2026-09-04 - G7 e promozione a VC-OK (CDX)

Il G6 R01 cieco ha coperto 14/14 unità con 10/10 input integri e zero `AF`, `AF-COR`, `ERR-MD`, `ERR-AUDIT` e `DUBBIO`. Il G7 P0-D/P2 fresco è `OK`: manifest 38/38, zero mismatch o duplicati, render finale di una pagina e sei collegamenti locali verificati. Hash finale del target `aad946d48ddbf921a92851e8568a813e4df69a072ce05a9c360f6e2b95a46687`; hash del manifest `bc9e316c0c7137b55648b22394ebd25a36ce9761b58808e063690d4790d7db33`. Lo scope è promosso a `VC-OK al 2026-09-04`; il § 3.4.2 non è aperto e richiede un nuovo via libera.

## 2026-09-04 - G0-G5 chiusi e G6 R01 aperto (CDX)

G0 e G1 sono `OK`: confini naturali accertati prima dei §§ 3.4.2/C3.4.2 e vigenza verificata sulle fonti ufficiali. G2 è `OK`. G3 ha rilevato due sole famiglie `ERR-MD`, cioè cassa non fedele delle rubriche e punto indebito dopo `C3.4.1`; il correttore P1 ha applicato esclusivamente le due correzioni congelate e il P0-D post-correzione ha ricontrollato `OK`. G4 è `OK`: una formula numerata `[3.4.1]`, quattro definizioni, zero tabelle, figure e asset. G5 è `OK`: 311 file e 1.754 collegamenti interni verificati, resa finale di una pagina leggibile. Hash finale del target: `aad946d48ddbf921a92851e8568a813e4df69a072ce05a9c360f6e2b95a46687`. È stato aperto G6 R01 con fonte-prima congelata e confronto cieco in corso.

## 2026-09-04 - apertura dello scope naturale (CDX)

Sandro ha autorizzato la ripresa della VC senza nominare lo scope. Il registro non contiene righe `IN-CORSO`; il § 3.3 è interamente `VC-OK` e i file di governo attendevano un nuovo via libera prima del § 3.4. È stato quindi aperto il solo primo candidato successivo, § 3.4.1. Le fonti ufficiali ricalcolano SHA-256 `dda1e397d56d71aa0f5bc457c3ba9b77064a468699dfc37bd056ac6c47105a46` e `f7c3b8d1f443aadb6b3e020b6b6c19813683492ecaadd2c15bf6bf1939aaed7c`, coincidenti con gli hash già registrati. Snapshot iniziale del Markdown `a26f43682b0d39a66f6112e898e44b69846c6cc27094c0e295d1443f5223e0de`. Perimetro indicativo da accertare a vista: pagine fisiche NTC 61 e Circolare 76, una formula numerata, nessuna tabella, figura o asset. I §§ 3.4.2-3.4.5 restano fuori perimetro.
