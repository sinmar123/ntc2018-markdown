---
scope_id: ntc2018-3.3.8
atti: ["D.M. 17/01/2018, § 3.3.8 Coefficienti aerodinamici", "Circolare 21/01/2019 n. 7, § C3.3.8 Coefficienti aerodinamici"]
file_markdown: cap03/3.3.8-vento-coefficienti-aerodinamici.md
fonte_ntc: {pdf: verifica-conformita/fonte-ufficiale/GU-2018-42-SO8-DM-17-01-2018.pdf, pagine_fisiche: 60}
fonte_circolare: {pdf: verifica-conformita/fonte-ufficiale/GU-2019-35-SO5-Circolare-7-2019.pdf, pagine_fisiche: "55-74"}
unita_registro: 1
formule_numerate: 6
tabelle: 19
figure: 27
pagine_fonte: 21
stato: CHIUSO
agente: CDX
macchina: P53
presa_in_carico: 2026-08-31T19:20:00+02:00
giro_g6: 2
max_giri: 3
rilievi_aperti: 0
rilievi_persistenti: 0
gate: {G0: OK, G1: OK, G2: OK, G3: OK, G4: OK, G5: OK, G6: OK, G7: OK}
snapshot_sha256: 2997e1fd9e05b8f2045587c40d6d5cf0314c3f0a09d8811b59d7557ffd33125c
attesa_decisione: []
esecutori:
  g6-r02: {correzione: "gpt-5.6-sol/high", preflight: "script locali/CDX", blocco-a: "gpt-5.6-sol/xhigh", blocco-b: "gpt-5.6-sol/xhigh"}
  g7: {p0-d: "script locali/CDX", p2-fresco: "gpt-5.6-sol/xhigh"}
prossimo_passo: "aprire il solo scope 3.3.9, già autorizzato; 3.3.10 resta in coda e non va aperto prima del G7 di 3.3.9"
---

## 2026-09-03 - G7 OK e chiusura VC-OK (CDX)

P0-D e P2 fresco `gpt-5.6-sol` xhigh `OK`. Il revisore finale ha ricalcolato 117/117 record del manifest e verificato le 30 pagine del render, senza difformità bloccanti. Unica osservazione non bloccante: testata molto stretta della tabella a pagina 16, completa e leggibile. Verbale `verifica-conformita/verbale-VC-ntc2018-3.3.8-2026-09-03.md`; snapshot `2997e1fd9e05b8f2045587c40d6d5cf0314c3f0a09d8811b59d7557ffd33125c`.

## 2026-09-03 - G6 R02 incrementale concluso OK (CDX)

Applicate soltanto le tre correzioni residue congelate e verificato il diff contro il checkpoint. Rigenerati indice, scope depurato e render finale di 30 pagine; il renderer mappa esplicitamente i simboli Unicode non coperti dal font e riconosce le tabelle a pipe anche quando seguono subito la didascalia, senza modificare il testo normativo. Preflight P0-D superato: 6 formule numerate, 19 tabelle, 27 figure, 0 asset mancanti, registro e indici validi.

Due verificatori P2 in contesti freschi hanno controllato otto pagine fonte a 600 dpi in due blocchi disgiunti. Chiuse le quattro lacune di accoppiamento e verificate integralmente le figure ricostruite C3.3.4, C3.3.14 e C3.3.19. Entrambi i blocchi `OK`: 0 `ERR-MD`, 0 `ERR-AUDIT`, 0 `DUBBIO`; evidenza `_tmp_render/cap03/vc-3.3.8-20260831/g6-r02/rapporto-g6-r02-consolidato-20260903.md`. G7 avviato sullo snapshot `2997e1fd9e05b8f2045587c40d6d5cf0314c3f0a09d8811b59d7557ffd33125c`.

## 2026-08-31 - pausa richiesta da Sandro (CDX)

Applicati 19 rilievi storici pertinenti, per 31 occorrenze; B08-05 appartiene al § C3.3.11 e resta fuori scope. Ripristinati tutti i 27 asset: 24 byte-identici dai pacchetti storici, C3.3.4 byte-identica al manifest e C3.3.14/C3.3.19 ricostruite dalla stessa fonte documentata dal G4. Il render pulito di 30 pagine è riuscito, con tag e didascalie automatiche conformi.

I controlli incrementali P2 e P0 sono stati interrotti su richiesta prima del rapporto. Restano tre residui già isolati sui due PNG di lacuna aperti dal coordinatore: punto aggiunto nel titolo C3.3.8.1.2; ordine della formula [C3.3.6] da riportare prima di Figura C3.3.26 e Tabella C3.3.XVIII; titolo C3.3.8.4 da rendere senza punto e in maiuscolo. Evidenze e istruzioni sono in `_tmp_render/cap03/vc-3.3.8-20260831/g6-r02/`. Non aprire 3.3.9.

## 2026-08-31 - apertura incrementale (CDX)

Continuità canonica col relativo staging confermata: hash depurato identico `919edc71efab58faf...`; le differenze del file vivo sono soltanto apparati di navigazione. Si riusano G0-G5 e le evidenze G6 storiche B03-B08 già valide. Il nuovo giro non ripete le 21 pagine e le 27 figure: applica i 20 rilievi congelati ricadenti nel file, verifica le posizioni modificate e chiude le quattro lacune di accoppiamento alle pagine 57, 61, 68 e 72.
