---
scope_id: ntc2018-3.1.3
atti:
  - "D.M. 17/01/2018, § 3.1.3 Carichi permanenti non strutturali"
  - "Circolare 21/01/2019 n. 7, § C3.1.3 Carichi permanenti non strutturali"
file_markdown: cap03/3.1.3-opere-civili-carichi-permanenti-non-strutturali.md
fonte_ntc: {pdf: verifica-conformita/fonte-ufficiale/GU-2018-42-SO8-DM-17-01-2018.pdf, pagine_fisiche: 46-47}
fonte_circolare: {pdf: verifica-conformita/fonte-ufficiale/GU-2019-35-SO5-Circolare-7-2019.pdf, pagine_fisiche: 46}
unita_registro: 1
formule_numerate: 0
apparati_matematici_inline: 5
tabelle: 0
figure: 0
pagine_fonte: 3
stato: CHIUSO
agente: CDX
macchina: W520
presa_in_carico: 2026-08-27T13:50:00+02:00
giro_g6: 1
max_giri: 3
rilievi_aperti: 0
rilievi_persistenti: 0
gate: {G0: OK, G1: OK, G2: OK, G3: OK, G4: OK, G5: OK, G6: OK, G7: OK}
snapshot_sha256: 40ff097b595fcf59bc6de8cbdd8b7bfa644636f19b4dcc48a7964a359e56a654
attesa_decisione: []
prossimo_passo: "aprire il file 3.1.4 già autorizzato da Sandro"
routing_effettivo:
  p0d: {modello: "script locali + gpt-5.6-luna/medium", compito: "hash, pagine, inventario, confronto deterministico, render e candidati", esito: "copertura 100%, quattro candidati complessivi passati a P1"}
  p0s: {modello: "non_usato", motivo: "scope breve e interamente predisponibile con script e Luna", esito: "non necessario"}
  p1: {modello: "gpt-5.6-sol/high", motivo_escalation: "G0-G1, due rubriche, punteggiatura di C3.1.3 e parola omessa", esito: "G0-G1 OK; quattro ERR-MD corretti e ricontrollati; G3-G4 OK"}
  p2: {modello: "gpt-5.6-sol/xhigh", gate: "G4, G6 e G7", esito: "G4 OK; G6 r01 OK; G7 OK, manifest 11/11"}
esecutori:
  apertura: {coordinamento: "CDX/sessione principale", controlli_meccanici: "script locali"}
  g0-g5: {p0d: "gpt-5.6-luna/medium", confini_vigenza: "gpt-5.6-sol/high", residui: "gpt-5.6-sol/high", apparati_a: "gpt-5.6-luna/medium source-first", apparati_b: "gpt-5.6-sol/xhigh source-first", riconciliazione: "gpt-5.6-sol/xhigh", esito: "G0-G5 OK, zero residui"}
  g6-r01: {coordinatore: "gpt-5.6-sol/xhigh fresco", inventario_source_first: "gpt-5.6-sol/xhigh fresco", verifica_blocco: "gpt-5.6-sol/xhigh fresco", blocchi: 1, staging: "C:/Users/sandro/AppData/Local/Temp/ntc2018-vc-3.1.3-g6-r01-20260827-155657", esito: "OK, 0 ERR-MD, 0 ERR-AUDIT, 0 DUBBIO"}
  g7: {p0d: "script locali + gpt-5.6-luna/medium", rilascio: "gpt-5.6-sol/xhigh fresco", esito: "OK, manifest 11/11 confermato"}
---

## 2026-08-27 - G7 e rilascio (CDX)

Il precontrollo P0-D Luna ha confermato 11/11 voci del manifest, percorsi unici, hash e dimensioni. Il controllo finale P2 Sol fresco ha ricalcolato le medesime undici voci, verificato la catena G0-G6 e confermato lo snapshot Markdown `40ff097b595fcf59bc6de8cbdd8b7bfa644636f19b4dcc48a7964a359e56a654`.

G7 `OK`; rilievi residui: 0 `ERR-MD`, 0 `ERR-AUDIT`, 0 `DUBBIO`, 0 `AF`, 0 `AF-COR`. Scope chiuso e promosso localmente a `VC-OK al 2026-08-27`. Manifest: `verifica-conformita/manifest-sha256-ntc2018-3.1.3-2026-08-27.txt`; verbale: `verifica-conformita/verbale-VC-ntc2018-3.1.3-2026-08-27.md`.

## 2026-08-27 - G6 r01 superato (CDX)

G6 eseguito su un unico blocco esterno al workspace, con coordinatore, inventario fonte-prima e verificatore di blocco distinti, tutti P2 `gpt-5.6-sol/xhigh` in contesti freschi. Copertura integrale: 2 titoli, 7 capoversi, 11 frasi narrative e 5 enunciati matematici.

Esito: soltanto `NORM` dichiarate per resa tipografica; 0 `AF`, 0 `AF-COR`, 0 `ERR-MD`, 0 `ERR-AUDIT`, 0 `DUBBIO`. G6 `OK` al primo giro. Evidenza: `_tmp_render/cap03/vc-3.1.3-20260827/g6-r01/rapporto-consolidato.md`.

## 2026-08-27 - disegno G6 r01 congelato prima dell'esecuzione (CDX)

Pacchetto esterno al workspace con undici file ammessi: sei ritagli fonte a 200 e 600 dpi, testo ausiliario limitato allo scope, frammento Markdown depurato, canone neutro, snapshot e istruzioni. I sei ritagli coincidono per hash con le evidenze del preflight; il testo ausiliario non contiene i §§ 3.1.2 o 3.1.4. Sono prenotati tre ruoli P2 freschi e separati: inventario source-first, verifica del blocco e coordinamento.

## 2026-08-27 - G0-G5 e preflight G6 chiusi (CDX)

G0-G5 tutti `OK`. Il ricontrollo P1 ha confermato i quattro soli edit autorizzati e ricostruito lo snapshot iniziale; la rigenerazione meccanica dell'indice interno ha allineato la sola etichetta di navigazione. Il corpo normativo depurato coincide con il frammento congelato.

I cinque enunciati matematici sono stati ricostruiti source-first in due contesti indipendenti. La divergenza del passaggio A sul quinto terminatore è stata chiusa a 600 dpi come `ERR-AUDIT`: la fonte ha quattro punti e virgola e un punto finale, coincidenti col Markdown. Snapshot finale `40ff097b595fcf59bc6de8cbdd8b7bfa644636f19b4dcc48a7964a359e56a654`; evidenza principale `_tmp_render/cap03/vc-3.1.3-20260827/preflight/rapporto-preflight.md`.

## 2026-08-27 - preflight P0-D, G0-G1 e adjudicazione residui (CDX)

Luna `medium` ha coperto il 100% delle tre pagine fonte e confermato i cinque enunciati matematici. Sol `high` ha chiuso G0 e G1 sulle fonti ufficiali correnti, poi ha adjudicato i quattro soli residui: cassa delle due rubriche, punto non presente dopo `C3.1.3` e omissione del secondo `da` nella sequenza `o da normative o da documenti`.

G4 `OK`: 5/5 enunciati conformi per pedici, cifre, operatori, unità e terminatori. Applicate le quattro correzioni logiche in tre sostituzioni fisiche; nessun numero, segno o unità toccato. G3 resta `KO` fino al ricontrollo separato.

## 2026-08-27 - apertura dello scope sul file naturale (CDX)

Scope limitato al solo file `cap03/3.1.3-opere-civili-carichi-permanenti-non-strutturali.md`, al § 3.1.3 del D.M. 17/01/2018 e al § C3.1.3 della Circolare 7/2019. I confini visivi occupano la parte finale della pagina fisica NTC 46, la parte iniziale della pagina 47 e la parte iniziale della pagina Circolare 46.

Precondizioni superate: fonti ufficiali presenti e ricalcolate, nessun'altra scheda sul medesimo file e nessun lucchetto concorrente. Snapshot Markdown iniziale SHA-256 `df65426720d7fa497f4296754e2c98a271947acdda0c3f465efcf52667fda8d3`. Il precedente campo pagina NTC del registro riportava soltanto `46`; il confine accertato include anche la pagina fisica 47 e viene riallineato nella riga locale.

Dimensionamento: tre pagine fonte parziali, nessuna formula numerata, tabella o figura; cinque condizioni matematiche in elenco, con disuguaglianze, pedici e unità da controllare integralmente. Sandro ha autorizzato esplicitamente anche il successivo § 3.1.4, che resterà però chiuso fino al G7 del presente scope.

Routing: script e Luna `medium` per il preflight deterministico; Sol `high` per G0-G1 e soli residui motivati; Sol `xhigh` per G6 e G7.
