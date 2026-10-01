---
scope_id: ntc2018-3.2.4
atti:
  - "D.M. 17/01/2018, § 3.2.4 Effetti della variabilità spaziale del moto"
file_markdown: cap03/3.2.4-azione-sismica-effetti-della-variabilita-spaziale-del-moto.md
fonte_ntc: {pdf: verifica-conformita/fonte-ufficiale/GU-2018-42-SO8-DM-17-01-2018.pdf, pagine_fisiche: 55}
fonte_circolare: null
unita_registro: 1
formule_numerate: 4
tabelle: 0
figure: 0
pagine_fonte: 1
stato: VC-OK
agente: CDX
macchina: P53
presa_in_carico: 2026-08-29T14:51:45+02:00
giro_g6: 1
max_giri: 3
rilievi_aperti: 0
rilievi_persistenti: 0
gate: {G0: OK, G1: OK, G2: OK, G3: OK, G4: OK, G5: OK, G6: OK, G7: OK}
snapshot_sha256: 4105f2d3dd29c453c640b782433e03eb9685c808e5fdbd371b87d2b52357f877
attesa_decisione: []
prossimo_passo: "nella nuova sessione aprire il solo scope 3.3.1, già autorizzato, e proseguire in sequenza fino al 3.3.10; non aprire il § 3.4"
routing_effettivo:
  p0d: {modello: "script locali + gpt-5.6-luna/medium", compito: "confini, inventario, collazione, formule, render, link e candidati", esito: "P0-D OK"}
  p0s: {modello: "non_usato", motivo: "materiali predisposti deterministicamente", esito: "non necessario salvo impedimenti"}
  p1: {modello: "gpt-5.6-sol/high", motivo_escalation: "quattro candidati P0-D e controllo di non omissione", esito: "5 ERR-MD certi corretti, 0 dubbi"}
  p2: {modello: "gpt-5.6-sol/xhigh", gate: "formula critica [3.2.14], G6 e G7", esito: "G4, G6 R01 e G7 OK; snapshot promuovibile"}
esecutori:
  apertura: {coordinamento: "CDX/sessione principale", controlli_meccanici: "script locali"}
  preflight: {p0d: "gpt-5.6-luna/medium", p1_residui: "gpt-5.6-sol/high se necessari"}
  apparati: {passaggio_a: "gpt-5.6-luna/medium", passaggio_b: "gpt-5.6-sol/xhigh", riconciliazione: "gpt-5.6-sol/xhigh"}
---

## 2026-08-29 - autorizzato il seguito sul § 3.3 (CDX)

Sandro ha autorizzato per la nuova sessione la VC completa dei file naturali 3.3.1-3.3.10. Questa scheda resta chiusa e invariata nello stato `VC-OK`; nessun nuovo scope del § 3.3 è stato aperto durante la presente sessione. La ripresa deve iniziare dal solo 3.3.1 e procedere in sequenza. Il § 3.4 non è autorizzato.

## 2026-08-29 - G7 OK e promozione VC-OK (CDX)

Il precontrollo G7 P0-D Moon ha verificato 22/22 voci del manifest: 22/22 file presenti, 22/22 dimensioni e 22/22 SHA-256 coincidenti, senza duplicati o voci estranee. Il decisore finale P2 Sol ha pronunciato `G7 OK` sullo snapshot `4105f2d3dd29c453c640b782433e03eb9685c808e5fdbd371b87d2b52357f877`.

Bilancio finale: una pagina NTC, nessun § C3.2.4 corrispondente, 3 rubriche, 14 capoversi, 4 gruppi formula, 5 espressioni o rami, 4 tag, nessuna tabella e nessuna figura. Cinque `ERR-MD` corretti, 0 `ERR-MD` residui, 0 `ERR-AUDIT`, 0 `DUBBIO`, 0 `AF` e 0 `AF-COR`. Scope promosso a `VC-OK al 2026-08-29`. Verbale: `verifica-conformita/verbale-VC-ntc2018-3.2.4-2026-08-29.md`.

Con questa promozione i quattro file naturali 3.2.1-3.2.4 sono tutti `VC-OK`. Il § 3.3 resta fuori perimetro e non viene aperto.

## 2026-08-29 - G6 R01 integrale OK (CDX)

Il G6 R01 ha usato un inventario fonte-prima Moon separato dal pacchetto di confronto e un verificatore P2 Sol fresco sull'unica pagina dello scope. Gli ingressi congelati coincidono con il manifest: raster 600 dpi `4b38f196...`, frammento depurato `2f616de6...`; nessuna modifica durante il giro.

Copertura: 3/3 rubriche, 14/14 capoversi, 4/4 gruppi formula, 5/5 espressioni o rami e 4/4 tag. Esito: 0 `ERR-MD`, 0 `ERR-AUDIT`, 0 `DUBBIO` e quattro sole famiglie `NORM` dichiarate. G6 R01 `OK` sullo snapshot `4105f2d3dd29c453c640b782433e03eb9685c808e5fdbd371b87d2b52357f877`. Prossimo gate: G7.

## 2026-08-29 - G0-G5 chiusi e snapshot post-correzione (CDX)

Il preflight P0-D Moon ha individuato tre difformità di cassa nelle rubriche e un dubbio protetto sull'esponente della formula `[3.2.14]`. Il passaggio P1 Sol sull'intera pagina ha confermato i quattro candidati come `ERR-MD` e ha rilevato un quinto errore lessicale, `fra i punti` al posto di `tra i punti`. Il passaggio P2 source-first sulle formule ha confermato che la fonte stampa `(x/v_s)^{0,7}`, non `(x/v_s)^2`.

Applicate esclusivamente cinque correzioni su cinque righe. Dopo la rigenerazione canonica dell'indice interno, il frammento normativo depurato ha SHA-256 `2f616de6d85ace62f17b805274e670ea01030b86346515b26d45741e136a609f`; lo snapshot completo ha SHA-256 `4105f2d3dd29c453c640b782433e03eb9685c808e5fdbd371b87d2b52357f877`. Il recheck P2 mirato della `[3.2.14]` è `OK`, con zero `ERR-MD`, zero `ERR-AUDIT` e zero `DUBBIO`.

Render finale di due pagine non vuote, quattro gruppi formula per cinque espressioni e quattro tag, nessuna tabella o figura. Linter del registro: zero errori e zero avvisi; indici interni: 311 file e 1.754 collegamenti conformi. G0-G5 `OK`. Prossimo gate: G6 R01 integrale sull'unica pagina.

## 2026-08-29 - apertura dello scope sul file naturale (CDX)

Scope limitato al solo file `cap03/3.2.4-azione-sismica-effetti-della-variabilita-spaziale-del-moto.md` e al § 3.2.4 del D.M. 17/01/2018, pagina fisica 55 della fonte congelata. La pagina precedente appartiene al § 3.2.3 e la pagina successiva apre il § 3.3; la Circolare passa dal § C3.2.3 al § C3.3 e non contiene un § C3.2.4 corrispondente.

Precondizioni superate: fonte ufficiale presente, precedente scope 3.2.3 chiuso `VC-OK`, nessuna scheda esistente e nessun altro scope sul medesimo file. Snapshot Markdown iniziale SHA-256 `3a91e01cf59acb3d757cafd5c23c82d49dc8411f5378078d517fd29b6336e7b4`, 4.285 byte e 58 righe.

Dimensionamento preliminare: una pagina fonte, quattro gruppi di formule numerate, nessuna tabella e nessuna figura. Fonte di scope congelata a 600 dpi in `_tmp_render/cap03/vc-3.2.4-20260829/preflight/fonte/ntc-p55-scope-3.2.4-600dpi.png`. Routing semplificato richiesto da Sandro: script e Moon/Luna per il deterministico, Sol soltanto per residui motivati e gate critici. Nessuna modifica normativa eseguita in apertura.
