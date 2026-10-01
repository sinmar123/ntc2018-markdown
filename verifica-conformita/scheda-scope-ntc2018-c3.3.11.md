---
scope_id: ntc2018-c3.3.11
atti:
  - "Circolare 21/01/2019 n. 7 C.S.LL.PP., § C3.3.11 Distacco di vortici"
file_markdown: cap03/c3.3.11-vento-distacco-di-vortici.md
fonte_ntc: null
fonte_circolare: {pdf: verifica-conformita/fonte-ufficiale/GU-2019-35-SO5-Circolare-7-2019.pdf, pagine_fisiche: 75}
unita_registro: 1
formule_numerate: 4
tabelle: 0
figure: 0
pagine_fonte: 1
stato: CHIUSO
agente: CDX
macchina: W520
presa_in_carico: 2026-09-03T22:12:48+02:00
giro_g6: 1
max_giri: 3
rilievi_aperti: 0
rilievi_persistenti: 0
gate: {G0: OK, G1: OK, G2: OK, G3: OK, G4: OK, G5: OK, G6: OK, G7: OK}
snapshot_sha256: e33a5fd69766a6c821cb03b2d4efcb495b1a33c6611ace17a25f1c58f45e2d92
attesa_decisione: []
prossimo_passo: "nessuna attività sul file; attendere un nuovo via libera prima di aprire il § 3.4 o altri scope"
routing_effettivo:
  p0d: {modello: "gpt-5.6-luna e script locali", compito: "hash, estrazioni, inventari, diff, link e render", esito: "preflight meccanico OK; tre ERR-AUDIT iniziali corretti"}
  p0s: {modello: "non_usato", motivo: "scope di una pagina con materiali determinabili", esito: "non_usato"}
  p1: {modello: "gpt-5.6-sol", motivo_escalation: "G0-G1, classificazione e riconferma distinta", esito: "G0-G5 OK dopo tre correzioni"}
  p2: {modello: "gpt-5.6-sol", gate: "apparati, G6 e G7", esito: "G6 R01 e G7 OK; zero residui"}
esecutori:
  apertura: {coordinamento: "CDX/sessione principale", controlli_meccanici: "script locali"}
  preflight: {p0d: "gpt-5.6-luna/medium", p1_residui: "gpt-5.6-sol/high"}
  apparati: {passaggio_a: "gpt-5.6-luna/medium", passaggio_b: "gpt-5.6-sol/xhigh", riconciliazione: "gpt-5.6-sol/xhigh"}
  g6-1: {inventario_e_blocco: "gpt-5.6-sol/xhigh fresco", adjudicazione: "gpt-5.6-sol/xhigh fresco", coordinamento: "CDX/sessione principale"}
  g7: {p0d: "gpt-5.6-luna/medium, manifest 49/49", p2: "gpt-5.6-sol/xhigh fresco, OK"}
---

## 2026-09-03 - apertura dello scope naturale (CDX)

Sandro ha autorizzato la VC del solo file autonomo C3.3.11. Il registro non contiene altri scope `IN-CORSO` e nessuna scheda naturale usa il medesimo file. La fonte ufficiale della Circolare ricalcola SHA-256 `f7c3b8d1f443aadb6b3e020b6b6c19813683492ecaadd2c15bf6bf1939aaed7c`; snapshot iniziale del Markdown `aefaf0de041d4bda506851d6146a8c3e32acb305954a1c4841b828fa13486e36`. Perimetro indicativo: pagina fisica 75 della Circolare, da accertare a vista; una pagina, quattro formule numerate, nessuna tabella, figura o asset. Il § 3.4 resta fuori perimetro.

## 2026-09-03 - inventari indipendenti del preflight (CDX)

Il P0-D Luna ha inventariato la pagina fonte prima del confronto col Markdown; il rapporto è stato congelato con SHA-256 `161dd4bbdf34e93094a60bd2f2e06f71f3fd8610cad5cf7f285970ea6c44377a`. Il successivo confronto meccanico ha rilevato che l'inventario aveva normalizzato per errore la sequenza fonte `Si osservi cha` in `Si osservi che`: il candidato è trattato come `ERR-AUDIT` del preflight e non come prova sul testo normativo. Un P2 indipendente ha quindi trascritto dalla sola fonte i quattro apparati matematici e le notazioni inline; inventario congelato con SHA-256 `a1a7622e249cd03b249965dddcbd96aadddfa0b7452a56b763ad3d74e280edd5`, prima di autorizzare il confronto col Markdown. I gate restano aperti fino ai giudizi P1/P2 e alla validazione post-correzione.

## 2026-09-03 - correzione e chiusura G0-G5 (CDX)

Il P1 ha isolato tre `ERR-MD`: rubrica, corsivo matematico dell'`i` in `i-esimo` e correzione silenziosa `cha`/`che`. Un correttore P1 ha applicato esclusivamente questi tre interventi e registrato `AF-3.3-15` e `AF-3.3-16`; `n_k` e `v_{m,l}` restano già documentati in `AF-3.3-05`. Il controllo post-correzione ha inoltre scoperto che il primo ritaglio a 600 dpi era troncato durante l'elenco: il raster è stato rigenerato integralmente e l'`ERR-AUDIT` è chiuso. P0-D e P1 fresco hanno riconfermato G0-G5 `OK`, zero residui, sullo snapshot `e33a5fd69766a6c821cb03b2d4efcb495b1a33c6611ace17a25f1c58f45e2d92`. Render finale di due pagine ispezionato; il pacchetto pulito per G6 è pronto.

## 2026-09-03 - G6 R01 cieco e adjudicazione `l`/`1` (CDX)

Il P2 fresco ha congelato i tre elaborati fonte-prima prima di ricevere il Markdown; integrità 3/3 e pacchetto input 11/11. La collazione integrale ha inizialmente pronunciato `KO` leggendo `v_{m,1}`. Il target non è stato toccato: tre ritagli diretti a 1200 dpi, il codepoint `U+006C` nella definizione e un P2 indipendente hanno confermato `v_{m,l}`. Lo stesso verificatore G6 ha rettificato il rilievo con addendum firmato. Esito autoritativo G6 R01 `OK`: zero `ERR-MD`, `ERR-AUDIT` residui e `DUBBIO`; nessun G6 R02 necessario.

## 2026-09-03 - G7 e chiusura VC (CDX)

Il P0-D ha ricalcolato manifest 49/49, congelamento 3/3 e input G6 11/11. Un P2 fresco ha riesaminato integralmente fonte, catena G0-G6, diff, adjudicazione `l`/`1` e render finale di due pagine. Esito G7 `OK`, zero `ERR-MD`, `ERR-AUDIT` residui e `DUBBIO`. Il file è promosso a `VC-OK al 2026-09-03` sul solo snapshot `e33a5fd69766a6c821cb03b2d4efcb495b1a33c6611ace17a25f1c58f45e2d92`; manifest SHA-256 `f4ee37a00afb9f5e1efec9e7e822946d16a3353ea2e196b5fc1036b6fb56e168`. Il § 3.3 è completo; il § 3.4 non è stato aperto.
