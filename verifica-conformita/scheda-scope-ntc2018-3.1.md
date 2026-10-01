---
scope_id: ntc2018-3.1
stato: CHIUSO
agente: CDX
presa_in_carico: 2026-09-12T15:11:37.237503+02:00
procedura: VC-NTC/4
procedura_sha256: 9c43358436f1e4f3ba92b16b95872afccf45e6cdb277d365e4fe5ea16f546a96
catalogo_sha256: d71319206ec54bcac3639dfd0b97c41754fa1062655b2d35c36ee5d6cb3036d6
file_markdown: [cap03/3.1-introduzione.md]
righe_registro: ["3.1"]
fonte_ntc_pagine_fisiche: [46]
fonte_circolare_pagine_fisiche: [46]
perimetro: sola introduzione 3.1 e C3.1; file 3.1.1-3.1.4 esclusi
snapshot_sha256: eed07e9a0857055ac55c4e03cdd2413ec08575d2e3434cb847522a39651f80de
giro_g6: 1
max_giri: 3
rilievi_aperti: 0
gate: {G0: OK, G1: OK, G2: OK, G3: OK, G4: OK, G5: OK, G6: OK, G7: OK}
prossimo_passo: "Nessuna sulla sola introduzione 3.1: VC conclusa. Attendere un nuovo via libera prima di aprire altri scope."
routing_effettivo:
  C: {agente: /root/c_31_intro, modello: gpt-5.6-sol, ragionamento: high, contesti: 1}
  preparazione: script_locali
  E: non_attivato
  V: {agente: /root/v_31_intro, modello: gpt-5.6-sol, ragionamento: xhigh, contesti: 1, isolamento: istruttivo}
consumi: {contatori: non_consolidati}
---

# Scheda della sola introduzione 3.1

## Chiusura 2026-09-12, CDX

CDX: sola introduzione 3.1 registrata VC-OK con VC-NTC/4 - semplificata; due correzioni di presentazione approvate da Sandro, G0-G7 OK, G6 integrale al primo giro 2/2, zero residui. Colonne procedura_vc e agente_vc aggiunte; Codex (CDX) per 3.1, Grok (GROK) per 8.1 da scheda. XLSX escluso su richiesta. Firma: Codex / CDX. [Verbale](./verbale-VC-ntc2018-3.1-2026-09-12.md), [manifest](./vc-ntc2018-3.1-2026-09-12/manifest-rilascio.json). Un G6 integrale e G7 nello stesso contesto V; nessun ciclo successivo.

Prossima azione: Nessuna sulla sola introduzione 3.1: VC conclusa. Attendere un nuovo via libera prima di aprire altri scope.

## Correzioni approvate e G0-G5 conclusi, 2026-09-12, CDX

Sandro ha approvato le due correzioni e autorizzato la registrazione VC-OK dopo i controlli, chiedendo una colonna che identifichi la procedura semplificata. Script applicativo vincolato alla lista: due sostituzioni esatte, nessuna modifica estranea. C ha riconfrontato diff, rubriche sulla fonte e l'unica pagina canonica; G0-G5 OK, zero residui. Nuovo snapshot sopra indicato; inventario fonte-prima affidato a un solo V fresco, in attesa di congelamento e rivelazione. G6 non ancora consumato. Nessun E attivato e nessuna scrittura XLSX. Firma: Codex / CDX.

Prossima azione: Completare G6 e G7, poi registrare VC-OK con indicazione della procedura 4 semplificata.

## Confronto iniziale concluso, elenco da approvare, 2026-09-12, CDX

G0/G1/G4 OK; G2-G3 KO per due ERR-MD di sola presentazione. Il perimetro contiene soltanto due rubriche, NTC p. fisica 46 e Circolare p. fisica 46: nessun capoverso, formula, tabella o figura. [Rapporto C e tabella per Sandro](../_tmp_render/cap03/vc-3.1-introduzione-20260912-cdx/rapporto-c.md), [lista delle correzioni](../_tmp_render/cap03/vc-3.1-introduzione-20260912-cdx/lista-correzioni.json), prove a 600 dpi nella stessa cartella. Maiuscole dei due titoli e rimozione del punto dopo C3.1; testo normativo invariato. Nessuna correzione né G5/G6/G7 eseguiti prima della decisione di Sandro, secondo § 6 della procedura 4.

Ricognizione G1 riusata del 2026-09-09, ricontrollo GU del 2026-09-12, applicabilità confermata da C. La presa è stata completata dopo la correzione del vincolo globale dello strumento: ammessi scope autorizzati su target disgiunti, riga 8.1 preservata; test 29/29 e lint senza errori. Nessun tentativo XLSX. Firma: Codex / CDX.

Prossima azione: Attendere la decisione di Sandro sulle due correzioni delle rubriche della sola introduzione 3.1.

## Presa in carico del 2026-09-12, CDX

Ordine di Sandro: «andiamo con la introduzione 3.1 con la nuova procedura versione 4». Il verbale del 3.1.1 riguarda esclusivamente quel sottoparagrafo e non copre questa introduzione. Target iniziale e criteri congelati nella [lavorazione](../_tmp_render/cap03/vc-3.1-introduzione-20260912-cdx/). C Sol high svolge il confronto iniziale; nessun E o V attivato. La vista XLSX resta esclusa da scritture per istruzione dell'utente. Nessun altro scope è autorizzato. Firma: Codex / CDX.

Prossima azione: Completare il confronto iniziale della sola introduzione 3.1 e presentare a Sandro gli eventuali rilievi prima di correggere.
