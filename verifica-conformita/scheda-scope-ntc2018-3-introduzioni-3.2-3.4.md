---
scope_id: ntc2018-3-introduzioni-3.2-3.4
stato: CHIUSO
agente: CDX
presa_in_carico: 2026-09-12T16:32:38+02:00
procedura: VC-NTC/5
procedura_sha256: 658d98340bde641fc683e0e4f63bf1da12ebc8f854f44bcce4a0824a11a9b690
catalogo_sha256: d71319206ec54bcac3639dfd0b97c41754fa1062655b2d35c36ee5d6cb3036d6
file_markdown: [cap03/3.2-introduzione.md, cap03/3.3-introduzione.md, cap03/3.4-introduzione.md]
righe_registro: ["3.2", "3.3", "3.4"]
perimetro: sole introduzioni 3.2, 3.3 e 3.4; sottoparagrafi esclusi
snapshot_sha256: d42ee91c2f86d631a69827f5f2dd7fe5ef0523815d923742ae079e58bb242c66
snapshot_manifest: verifica-conformita/vc-ntc2018-introduzioni-3.2-3.4-2026-09-12/g5-r02/snapshot-finale.json
giro_g6: 1
max_giri: 3
rilievi_aperti: 0
gate: {G0: OK, G1: OK, G2: OK, G3: OK, G4: OK, G5: OK, G6: OK, G7: OK}
prossimo_passo: "Nessuna sul capitolo 3: tutti i file del registro sono VC-OK. Attendere un nuovo incarico prima di aprire altri scope."
routing_effettivo:
  C: {agente: /root/c_intro_32_34, modello: gpt-5.6-sol, ragionamento: high, contesti: 1}
  preparazione: script_locali
  E: non_attivato
  V:
    b01: {agente: /root/v_intro_32_b01, modello: gpt-5.6-sol, ragionamento: xhigh, contesti: 1, isolamento: istruttivo}
    b02: {agente: /root/v_intro_33_34_b02, modello: gpt-5.6-sol, ragionamento: xhigh, contesti: 1, isolamento: istruttivo}
consumi: {contatori: non_consolidati}
---

# Sole introduzioni 3.2, 3.3 e 3.4

## Chiusura 2026-09-12, CDX

CDX: introduzioni 3.2, 3.3 e 3.4 VC-OK, VC-NTC/5 - semplificata. Correzioni approvate e tre figure ripristinate; G0-G7 OK, G6 al primo giro 32/32, quattro falsi positivi esclusi e un pedice corretto con riscontro mirato, zero residui. Pagine della Circolare non rilevate automaticamente nel vecchio inventario: riferimenti verificati nel verbale. Registro solo CSV. Firma: Codex / CDX. Un solo giro G6, rapporti originari b01 KO/b02 OK preservati; quattro falsi positivi esclusi con prove fonte e una regressione di pedice corretta con controllo localizzato dello stesso V. Snapshot finale sopra indicato. [Verbale](./verbale-VC-ntc2018-introduzioni-3.2-3.4-2026-09-12.md), [attestazione mirata](./vc-ntc2018-introduzioni-3.2-3.4-2026-09-12/controllo-modifiche-r02/attestazione-v-modifiche.json), [manifest](./vc-ntc2018-introduzioni-3.2-3.4-2026-09-12/manifest-rilascio.json).

Prossima azione: Nessuna sul capitolo 3: tutti i file del registro sono VC-OK. Attendere un nuovo incarico prima di aprire altri scope.

## Correzioni approvate applicate e G0-G5 OK, 2026-09-12, CDX

Ordine di Sandro: «si applica tutto». Applicate 15 sostituzioni esatte e ripristinate tre figure dalla fonte; C ha verificato diff, asset, 71 righe di mappa/depurazione e quattro pagine della resa canonica: G0-G5 OK, zero residui. Due blocchi G6 da tre e quattro pagine fonte, minimo compatibile con la procedura. Inventari fonte-prima in corso; giro G6 ancora non consumato fino alla rivelazione dei target. Firma: CDX.

Prossima azione: Completare G6 e G7 e registrare VC-OK nel CSV.

## Confronto iniziale concluso il 2026-09-12, CDX

G0/G1 OK; G2-G4 conclusi con sette gruppi di NC: rubriche dei tre file e, nel 3.2, elenchi, particolarità della fonte, simboli inline, tre didascalie e tre figure mancanti. Confronto completo NTC pp. fisiche 49, 56, 61 e Circolare 46-47, 54, 76; p. 48 usata solo come confine esclusivo di C3.2.1. Ricognizione G1 del 2026-09-09 e ricontrollo GU del 2026-09-12 riusati sui medesimi atti, applicabilità confermata. [Rapporto con prove](../_tmp_render/cap03/vc-introduzioni-3.2-3.4-20260912-cdx/rapporto-c.md), [lista applicabile](../_tmp_render/cap03/vc-introduzioni-3.2-3.4-20260912-cdx/lista-correzioni.json).

Controllo meccanico: 15 sostituzioni univoche, tre sorgenti PNG presenti; target agli hash iniziali, nessuna correzione. Un contesto C Sol high, con interruzione di un comando superfluo rimasto bloccato; G6 mai avviato, nessun E o V. Consumi non consolidati. Firma: CDX.

Prossima azione: Attendere l’approvazione di Sandro sui sette gruppi di correzioni delle introduzioni 3.2, 3.3 e 3.4; poi applicare la lista e completare G5-G7.

## Presa del 2026-09-12, CDX

Ordine di Sandro: «vai con tutti», riferito alle tre introduzioni residue del capitolo 3. CDX: lotto autorizzato delle sole introduzioni 3.2, 3.3 e 3.4, VC-NTC/5 - semplificata. Sottoparagrafi già VC-OK esclusi; vecchia scheda aggregata 3.3 sospesa conservata come storia. Pagine della Circolare non rilevate automaticamente nel vecchio inventario. Registro solo CSV. Firma: CDX. [Lavorazione](../_tmp_render/cap03/vc-introduzioni-3.2-3.4-20260912-cdx/). Confronto iniziale in un unico contesto C; nessuna correzione prima della decisione sull'elenco. Le immagini collegate da 3.2 risultano mancanti e saranno confrontate con le figure ufficiali. Nessun nuovo scope sui sottoparagrafi né ripresa della vecchia scheda 3.3.

Prossima azione: Completare il confronto iniziale delle sole introduzioni 3.2, 3.3 e 3.4 e presentare a Sandro un unico elenco delle correzioni da approvare.
