---
scope_id: ntc2018-3.4.2
atti:
  - "D.M. 17/01/2018, § 3.4.2 VALORE DI RIFERIMENTO DEL CARICO DELLA NEVE AL SUOLO"
  - "Circolare 21/01/2019 n. 7 C.S.LL.PP., § C3.4.2 VALORE DI RIFERIMENTO DEL CARICO DELLA NEVE AL SUOLO"
file_markdown: cap03/3.4.2-neve-valore-di-riferimento-del-carico-della-neve-al-suolo.md
fonte_ntc: {pdf: verifica-conformita/fonte-ufficiale/GU-2018-42-SO8-DM-17-01-2018.pdf, pagine_fisiche: 61-62}
fonte_circolare: {pdf: verifica-conformita/fonte-ufficiale/GU-2019-35-SO5-Circolare-7-2019.pdf, pagine_fisiche: 76}
unita_registro: 1
formule_numerate: 5
formule_non_numerate: 0
tabelle: 0
figure: 2
pagine_fonte: 3
stato: CHIUSO
agente: CDX
macchina: W520
presa_in_carico: 2026-09-04T17:28:52+02:00
giro_g6: 2
max_giri: 3
rilievi_aperti: 0
rilievi_persistenti: 0
gate: {G0: OK, G1: OK, G2: OK, G3: OK, G4: OK, G5: OK, G6: OK, G7: OK}
snapshot_sha256: 8ba6dd0a425e4133e8e0ff05fb2114b6f60cb2801f2d0bd7a07332958b610e77
attesa_decisione: []
prossimo_passo: "nessuna attività sul file; attendere un nuovo via libera prima di aprire il solo scope 3.4.3 o altri scope"
routing_effettivo:
  p0d: {modello: "script locali; gpt-5.6-luna/medium", compito: "hash, estrazioni, inventario, diff, link, asset, render e post-correzione", esito: "G2-G5 post-correzione e preflight OK"}
  p0s: {modello: "non_usato", motivo: "scope breve; deterministico coperto da script e Luna", esito: "non_usato"}
  p1: {modello: "gpt-5.6-sol/high", motivo_escalation: "G0-G1, confronto testuale, classificazione e correzione distinta", esito: "G0-G3 e G5 OK post-correzione"}
  p2: {modello: "gpt-5.6-sol/xhigh", gate: "G4, G6 e G7", esito: "G4 OK; G6 R01 NON OK e adjudicato; G6 R02 OK; G7 OK"}
esecutori:
  apertura: {coordinamento: "CDX/sessione principale", controlli_meccanici: "script locali"}
  preflight-p0d: {modello: "gpt-5.6-luna", ragionamento: "medium", esito: "inventario, diff, link, asset, render e post-correzione OK"}
  g0-g1: {modello: "gpt-5.6-sol", ragionamento: "high", esito: "OK limitatamente allo scope"}
  g2-g3-g5: {modello: "gpt-5.6-sol", ragionamento: "high", esito: "rilievi determinati, corretti in fase distinta e riconfermati OK"}
  g4: {modello: "gpt-5.6-sol", ragionamento: "xhigh", esito: "cinque gruppi numerati, nove rami, inline e due figure conformi post-correzione"}
  correzione-p1: {modello: "gpt-5.6-sol", ragionamento: "high", esito: "lista congelata applicata senza variazioni estranee"}
  g6-r01: {modello: "gpt-5.6-sol", ragionamento: "xhigh", esito: "NON OK; sei pedici annidati e un grassetto corretti, candidato `d un anno` respinto"}
  adjudicazione-r01: {modello: "gpt-5.6-sol", ragionamento: "xhigh", esito: "sette occorrenze annidate dopo riesame del numeratore finale, `C3.4.1` grassetto, `d un anno` letterale"}
  correzione-r01-p1: {modello: "gpt-5.6-sol", ragionamento: "high", esito: "otto correzioni congelate in due passaggi; hash target 8ba6dd0a...0e77"}
  g6-r02: {modello: "gpt-5.6-sol", ragionamento: "xhigh", esito: "OK, 46/46 elementi e 23/23 input; zero ERR-MD, ERR-AUDIT e DUBBIO"}
  g7-p0d: {modello: "gpt-5.6-luna", ragionamento: "medium", esito: "manifest 135/135, zero mancanti, duplicati o mismatch"}
  g7-p2: {modello: "gpt-5.6-sol", ragionamento: "xhigh", esito: "OK, zero ERR-MD, ERR-AUDIT, DUBBIO e AF-COR"}
---

## 2026-09-04 - G7 chiuso OK e scope promosso (CDX)

Il P0-D ha costruito e ricalcolato il manifest permanente di 135 file; un P2 fresco ha riconfermato 135/135 record, target e fonti, 23/23 input e 46/46 elementi del G6 R02, render finale e separazione dei ruoli. G7 è `OK` con zero `ERR-MD`, `ERR-AUDIT`, `DUBBIO` e `AF-COR`. Le nove anomalie di fonte sono conservate e documentate. È definitiva l'adjudicazione di tutte le sette occorrenze Circolare come `q_{s_n}`/`q_{s_k}`; la precedente lettura provvisoria del numeratore finale è superata dalle origini vettoriali e dal riesame indipendente. Il solo snapshot `8ba6dd0a425e4133e8e0ff05fb2114b6f60cb2801f2d0bd7a07332958b610e77` è promosso a `VC-OK al 2026-09-04`.

## 2026-09-04 - G6 R02 chiuso OK e G7 aperto (CDX)

Prima del confronto R02 il coordinatore ha scartato un primo congelamento fonte-prima che conteneva due errori d'inventario; il Markdown non era ancora stato reso disponibile e il giro non è stato consumato. Un P2 fresco ha prodotto un congelamento sostitutivo valido, poi il confronto cieco integrale ha verificato 23/23 input e 46/46 elementi. G6 R02 è `OK` con zero `ERR-MD`, `ERR-AUDIT` e `DUBBIO`. L'adjudicazione della gerarchia dei pedici è stata completata sulle sette occorrenze mediante ritagli a 1200 dpi, origini vettoriali e conferme indipendenti; la fase correttiva ha portato lo snapshot a `8ba6dd0a425e4133e8e0ff05fb2114b6f60cb2801f2d0bd7a07332958b610e77`. G7 è aperto.

## 2026-09-04 - G6 R01 non chiuso, adjudicazione e apertura R02 (CDX)

Il confronto cieco R01 ha coperto 53/53 elementi e 19/19 input, ma ha chiuso `NON OK` con tre candidati `ERR-MD`. L'adjudicazione su ritagli mirati a 1200 dpi ha respinto il candidato su `d un anno`, che la fonte stampa letteralmente, e ha confermato il grassetto del rinvio `C3.4.1`. Ha inoltre sostituito l'ipotesi uniforme sui pedici con la lettura puntuale, confermata da un P2 indipendente: sei occorrenze `q_{s_n}`/`q_{s_k}` con pedice annidato e un solo numeratore finale `q_{sn}` con suffissi allo stesso livello. Un P1 distinto ha applicato esclusivamente sei correzioni di gerarchia e il grassetto; hash target `e3ea42dee106d07267474cc5287224198d3092896e62533ecfa3c8c066b5c1fb`. La non regressione e le prove sono in `g6-r01/adjudicazione-r01.md`; è stato aperto G6 R02 con nuova fase fonte-prima e nuovo render canonico.

## 2026-09-04 - G0-G5 chiusi e G6 R01 aperto (CDX)

G0 e G1 sono `OK`: confini naturali accertati sulle pagine fisiche NTC 61-62 e Circolare 76, integrità e vigenza verificate sulle fonti ufficiali. G2-G5 hanno rilevato rubriche non letterali, un capoverso omesso, due asset mancanti e scostamenti puntuali in prosa, formula, definizioni e didascalia. La lista è stata congelata; un correttore P1 distinto ha applicato soltanto quelle correzioni e ha ripristinato i due PNG come copie binarie degli estratti fonte. Sei anomalie della Gazzetta sono conservate e documentate in `cap03/annotazioni/3.4.2-anomalie-fonte.md`. Il P0-D e il P2 post-correzione hanno riconfermato G2-G5 `OK`, hash finale del target `53c48aa53c85f11c3517c10e2876b20675edb593527ef06357968826c560c1cc`, render canonico di quattro pagine e zero residui. Gli `ERR-AUDIT` dell'apertura, cioè mappatura NTC incompleta, conteggio delle formule non numerate e riga CSV momentaneamente malformata, sono stati corretti; il linter passa con 311 righe, 11 colonne, zero errori e zero avvisi. È stato aperto G6 R01 con fonte-prima congelata e confronto cieco in corso.

## 2026-09-04 - apertura dello scope naturale (CDX)

Sandro ha autorizzato la VC del solo file 3.4.2. Il registro non contiene altri scope `IN-CORSO` e nessuna scheda naturale usa il medesimo file. Le fonti ufficiali ricalcolano SHA-256 `dda1e397d56d71aa0f5bc457c3ba9b77064a468699dfc37bd056ac6c47105a46` e `f7c3b8d1f443aadb6b3e020b6b6c19813683492ecaadd2c15bf6bf1939aaed7c`, coincidenti con gli hash registrati. Snapshot iniziale del Markdown `247db77ec069572c8e620ba6d4ecd80743e1e34f17fdad8a184490d8affbe113`. Il controllo visivo delle pagine condivise ha accertato che lo scope occupa le pagine fisiche NTC 61-62 e Circolare 76; la precedente mappatura locale della sola pagina NTC 61 era un `ERR-AUDIT`, corretto prima dei gate. Dimensionamento finale: tre pagine fonte, cinque gruppi di formule numerate con nove rami complessivi, nessuna formula esposta autonoma non numerata, nessuna tabella e due figure. I §§ 3.4.1 e 3.4.3-3.4.5 restano fuori perimetro.
