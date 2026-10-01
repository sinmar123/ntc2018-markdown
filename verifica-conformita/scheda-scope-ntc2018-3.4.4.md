---
scope_id: ntc2018-3.4.4
atti:
  - "D.M. 17/01/2018, § 3.4.4 COEFFICIENTE DI ESPOSIZIONE"
file_markdown: cap03/3.4.4-neve-coefficiente-di-esposizione.md
fonte_ntc: {pdf: verifica-conformita/fonte-ufficiale/GU-2018-42-SO8-DM-17-01-2018.pdf, pagine_fisiche: 63}
stato: CHIUSO
agente: CDX
macchina: W520
presa_in_carico: 2026-09-05T12:15:05.164853+02:00
procedura: VC-NTC/1
procedura_sha256: 3ed1723a25f875fad7632b5a7b7ce773d435dcb685fec938ea18df2524be93db
giro_g6: 1
max_giri: 3
gate: {G0: OK, G1: OK, G2: OK, G3: OK, G4: OK, G5: OK, G6: OK, G7: OK}
snapshot_sha256: 6e9a5f838301b7d04ed3dc6c39256fcaf6d78997f2f5567350d287bb6cafc448
attesa_decisione: []
consumi: vc-3.4.4-20260905/consumi.json
prossimo_passo: "Attendere un nuovo via libera prima di aprire il solo scope 3.4.5 o altri scope."
routing_effettivo:
  coordinatore: {modello: gpt-6-astra, ragionamento: max, contesti: 1, nota: "Profilo ereditato dalla sessione, riscontrato nei metadati runtime; non scelto come default della procedura."}
  meccanica: "script locali"
  verificatore: {modello: gpt-5.6-sol, ragionamento: xhigh, contesti: 2, nota: "Un contesto precedente respinto prima del target; un contesto fresco R01B valido per G6 e G7."}
  correttore: {modello: gpt-5.6-sol, ragionamento: high, contesti: 1, interventi: 2}
  coordinatore_ripresa: {modello: gpt-6-astra, ragionamento: xhigh, contesti: 1}
---

# Scheda scope § 3.4.4

## Presa in carico 2026-09-05, CDX

Autorizzazione esplicita di Sandro: «ok. vai con 3.4.4». Registro senza scope IN-CORSO prima della presa. Avviato solo il file naturale § 3.4.4; confini accertati sulla pagina condivisa NTC 63, dalla rubrica 3.4.4 fino al termine della Tab. 3.4.I, prima di 3.4.5. Snapshot iniziale, procedura e catalogo congelati in `_tmp_render/cap03/vc-3.4.4-20260905/`. Giro G6 non iniziato.

Prossima azione: completare G0-G5, poi G6 indipendente e G7.

## Ripresa 2026-09-05T17:05:03.195472+02:00, CDX

Richiesta di Sandro: «riprendiamo vc». Unico scope IN-CORSO nel CSV: 3.4.4. La sessione precedente 01a07101-e740-7b53-bdbb-781440b9bdae risulta terminata (task_complete del 2026-09-05T10:38:06.300Z); le altre sessioni recenti sono estranee al progetto e terminate. Ripresa della propria presa precedente, senza altro scope. Fonte NTC, target, procedura e catalogo ricalcolati: impronte identiche al congelamento. G0-G5 riutilizzati sul medesimo snapshot e sulla ricognizione della stessa data. Coordinatore della ripresa: gpt-6-astra/xhigh, metadati runtime, contesto 01a07217-7b68-7e41-b916-b776c06c2be0; non autore delle correzioni. Il tentativo tecnico precedente resta respinto e conservato; nuovo verificatore in contesto fresco, giro ancora 0/3.

Prossima azione: completare G6 indipendente e G7 sul solo § 3.4.4.

## G6 R01B avviato, 2026-09-05T17:13:03.557923+02:00, CDX

V gpt-5.6-sol/xhigh, /root/v_344_r01b, ha completato il censimento fonte-prima. Inventario e canone congelati dallo strumento prima della rivelazione; pacchetto ricontrollato 7/7 OK. V ha comunicato il primo accesso a testo.md il 2026-09-05T15:11:57Z: giro G6 1/3. Un unico blocco copre l'intero scope, una pagina fonte; nessun target modificato.

Prossima azione: completare il confronto G6 R01B e G7.

## Chiusura 2026-09-05T17:29:24.227273+02:00, CDX

G6 R01B e G7 OK: 19/19 elementi, 7/7 input G6, manifest 53/53; zero ERR-MD, ERR-AUDIT e DUBBIO, nessuna AF o AF-COR. Target invariato nella ripresa. Manifest SHA-256 `7e7b8870d2eba6818009154e3b412f33b5f10a6f18d5040f8eee7b4defd1de78`; snapshot `6e9a5f838301b7d04ed3dc6c39256fcaf6d78997f2f5567350d287bb6cafc448`. Verbale: [verbale-VC-ntc2018-3.4.4-2026-09-05.md](verbale-VC-ntc2018-3.4.4-2026-09-05.md). Il giudizio è AI, senza revisione umana integrale; isolamento istruttivo dichiarato. Contatore finale 1/3.

Prossima azione: Attendere un nuovo via libera prima di aprire il solo scope 3.4.5 o altri scope.

## Consumi e verifiche di chiusura, CDX

[Contatori per sessione](vc-3.4.4-20260905/consumi.json), registrati dopo la chiusura e il giornale: due contesti C, uno E e due V (uno respinto prima del target). Il perimetro iniziale C usa la baseline pre-autorizzazione; quello della ripresa è indicato con il timestamp dell’ultimo campione. Nessuna somma parent/figli, nessuna conversione in quota d’abbonamento e nessun risparmio percentuale dichiarato.

Verifiche finali: CSV 311 righe, zero errori e avvisi; XLSX 311 × 11, 380 collegamenti, zero differenze dalla fonte; manifest 53/53. Riallineata la cassa del titolo nel solo CSV alla rubrica già verificata del Markdown. Giornale registrato: 2026-09-05-ntc2018-norme-costruzioni-173104.md.

Prossima azione: Attendere un nuovo via libera prima di aprire il solo scope 3.4.5 o altri scope.
