---
scope_id: ntc2018-8.4
atti:
  - "D.M. 17/01/2018, § 8.4 CLASSIFICAZIONE DEGLI INTERVENTI, fino a prima di 8.5"
  - "Circolare 21/01/2019 n. 7 C.S.LL.PP., § C8.4 CLASSIFICAZIONE DEGLI INTERVENTI, fino a prima di C8.5"
file_markdown: cap08/8.4-introduzione.md
righe_registro: [8.4, 8.4.1, 8.4.2, 8.4.3]
fonte_ntc: {pdf: verifica-conformita/fonte-ufficiale/GU-2018-42-SO8-DM-17-01-2018.pdf, pagine_fisiche: 295-296}
fonte_circolare: {pdf: verifica-conformita/fonte-ufficiale/GU-2019-35-SO5-Circolare-7-2019.pdf, pagine_fisiche: 256-257}
unita_registro: 4
file_scope: 4
pagine_fonte: 4
formule_numerate_preliminari: 0
tabelle_preliminari: 0
figure_preliminari: 0
stato: IN-CORSO
agente: CCC
macchina: claude.ai/code (sessione cloud)
agente_precedente: OC
subentro: 2026-10-14
presa_in_carico: 2026-10-01T12:10:00+02:00
procedura: VC-NTC/7
procedura_sha256: 01c7f0ed9908e4c7620189a0073b2892afe37aa499f99cf50329a84b43960e67
catalogo_sha256: dd5f1b9980e6fd37bd0444277d8b69d6ac0c000b91c1cf659a4f9a398b4a7c43
snapshot_iniziale_sha256: vedi-corpo
snapshot_sha256: 70dbe9d6fcc8a18704c4dc50c5d4f87a149a735d872c3fde55b29740363813ec
giro_g6: 2
max_giri: 3
rilievi_aperti: 0
gate: {G0: OK, G1: OK, G2: OK, G3: OK, G4: OK, G5: OK, G6: OK, G7: DA_FARE}
attesa_decisione: []
prossimo_passo: "G7 di V sul lotto di chiusura (verbale, scheda, manifest), poi registra."
routing_effettivo:
  coordinatore_fino_al_2026-10-13: {modello: xai/grok-4.7, ragionamento: off, ruolo: C, contesti: 1, agente: "NormaNTC18 (OC)"}
  coordinatore: {modello: claude-opus-5-5, ruolo: C, agente: "CC cloud (CCC)"}
  verificatore: {modello: "subagente Opus a contesto nuovo", ruolo: V}
  meccanica: "script di strumenti/"
---

# Scheda scope § 8.4

## Presa in carico 2026-10-01, NormaNTC18 (OC)

Autorizzazione di Sandro: «facciamo 8.4». Perimetro: introduzione e §§ 8.4.1, 8.4.2, 8.4.3, con la Circolare fino a prima di C8.5. NTC pp. 295-296, Circolare 256-257. 8.3 resta VC-OK. 8.5 escluso.

Procedura VC-NTC/6. G1 riusato: ricognizione 2026-09-09 e ricontrollo 2026-09-13, ancora dentro i trenta giorni. Nessun ricontrollo nuovo sulla banca dati oggi.

## Decisione 2026-10-01, «applica secondo buon senso»

Applicate con script, prosa invariata a parte rubrica, richiamo e grassetto:

- R1. Rubriche C8.4, C8.4.1, C8.4.2, C8.4.3 in maiuscolo, senza punto. Come i §§ 8.2 e 8.3.
- R2. Capoversi della Circolare staccati come in Gazzetta: sei, sei e cinque. Gli a capo interni restano uniti.
- R3. Nota 2 con linee e etichetta **Nota 2.** Il richiamo, dopo «fai come gazzetta», è `operativa².`: il 2 sta prima del punto, come sulla pagina.
- R4. Le tre etichette della NTC in grassetto corsivo, due punti compresi.
- R5. Nella Norma, `0,6 ,` con lo spazio prima della virgola. Nella Circolare lo `0,6` resta attaccato, perché lì la Gazzetta non ha lo spazio.
- R6. Nella Norma, spazio prima del punto: `0{,}80` .
- R7. Nella Circolare, `di  classe` e `previste  per`.

G4: zero formule numerate, zero tabelle, zero figure. Il segno davanti a 1,0 e a 0,80 è ≥, ritaglio a 600 dpi.

Diff: `_tmp_render/cap08/vc-8.4-20261001-oc/diff-buon-senso.txt`.

Snapshot iniziale, prima delle correzioni:

- `8.4-introduzione.md` `2127bbe59a918898e92516641e6e8c31b3b668a4ba076972995127952042842e`
- `8.4.1-....md` `78fc80f76f91eec972cf3eff4d9f4cc01b6a853f54f6de01240684b1074f598c`
- `8.4.2-....md` `ec0e0f722aa3f3f253b0f7dd379ad4c700fcce2e0449a66a63f7631485083fea`
- `8.4.3-....md` `6c66b5b619cd074446472a6a949ccecfcadf4436da7597deab8c0587dae1c582`

Snapshot dopo le correzioni:

- `8.4-introduzione.md` `1d1c7f3e07d6ec3aa1018ecc5d6b525f2bc053e3400123cf8ee48a96df074660`
- `8.4.1-....md` `473952bb57870840e0823fe5cd2f707790d409147c4f715f1d47a1aeb4ef5bf2`
- `8.4.2-....md` `c95ac40657e5bb11c96f35ee4e72ff4d5b20f8a2baf3fbf1b463c3b2dcd88497`
- `8.4.3-....md` `bae49def63ec3e0eb48f9f41a67f4735a777b797fca48c0f61c1fdfd4a933100`

Prossima azione: G5, resa canonica dei quattro file e controllo visivo. Poi G6.

G5, 2026-10-01: resa dei quattro file riuscita. Tag e didascalie automatiche assenti. Pagine guardate. Lo spazio prima del punto di 0,80 è uno spazio unificatore, così il punto non cade da solo a capo. G6 preparato, un solo blocco, 117 righe depurate, pagine NTC 295-296 e Circolare 256-257.

G6 giro 1, 2026-10-01: schema OK, 65 id, esito del verificatore KO, 7 rilievi. Rapporto `g6-r01/b01/rapporto-g6.json`. Fermati in attesa di Sandro.

## Subentro 2026-10-14, CC cloud (CCC)

Ordine esplicito di Sandro del 2026-10-14: subentra CC cloud a NormaNTC18 (OC), che non lavora più sullo scope. Le righe 8.4, 8.4.1, 8.4.2 e 8.4.3 restano `IN-CORSO`.

Stato ereditato: G0-G5 `OK`; correzioni R1-R7 applicate. Le impronte dei quattro file correnti coincidono con lo snapshot «dopo le correzioni» qui sopra. Il G6 giro 1 del 2026-10-01 si era chiuso `KO` con 7 rilievi, ma il rapporto (`g6-r01/b01/rapporto-g6.json`) e il diff stavano in `_tmp_render/` sulla macchina OpenClaw e non sono nel repository: i 7 rilievi non sono ricostruibili. Decisione di Sandro del 2026-10-14: rifare il G6 integrale come giro 2 (`giro_g6` non si azzera), con un verificatore Opus a contesto nuovo; i rilievi trovati vanno a Sandro in un unico elenco prima di qualunque correzione. `rilievi_aperti` passa a 0 perché i 7 non sono più identificabili; il giro 2 li riesamina comunque per intero.

Procedura: lo scope adotta la revisione 7 (VC-NTC/7) dal G6 giro 2, primo passaggio non iniziato, come prevede il § 1. Le modifiche della revisione 7 riguardano solo diciture; criteri, canone G6 e gate invariati.

G1: ricognizione piena del 2026-10-13 (scope 3.3-ancore-blocco, copre NTC e Circolare) con ricontrollo mirato del 2026-10-14: schede ufficiali identiche, nessun aggiornamento. Evidenza `vc-ntc2018-8.4-2026-10-14/g1/ricontrollo-20261014.json`.

G5, 2026-10-14: i quattro file uniti in `g6-r02/target-scope.md` (depurato: 111 righe) e resi con `render-capitolo.py`: cinque pagine, nessun tag tondo, nessuna didascalia automatica, controllo visivo senza difetti.

G6 giro 2, 2026-10-14: un blocco, pagine NTC 295-296 e Circolare 256-257, righe 1-111. V subagente Claude Opus a contesto nuovo: inventario fonte-prima di 72 elementi, validato e congelato prima della rivelazione; confronto integrale con tutti i 72 id coperti. Esito `KO`, 5 rilievi. Testo e numeri conformi; i rilievi riguardano un punto aggiunto alla fine della nota 2 della Circolare, tre corsivi della fonte omessi (C8.4 «riparazione o intervento locale», «miglioramento», «adeguamento»; C8.4.3 lettere b, c, d, e; 8.4.3 «a)») e il grassetto di alcuni pedici e segni nella Circolare. C ha riscontrato ogni rilievo sulla codifica del PDF e su ritagli a 600 dpi (`c/`): confermati; nel 8.4.3 il punto dopo «a)» è in tondo, a differenza della lettura di V. Isolamento: V dichiara di aver salvato per errore i propri ritagli nella cartella madre del pacchetto, senza aprirne altri file. Rapporto `g6-r02/b01/rapporto-g6.json`, `valida-g6` OK. Lista per Sandro: `lista-correzioni.json` (L1-L4 e la questione D1). Fermati prima di correggere.

## Decisione di Sandro e correzioni, 2026-10-14

Decisione di Sandro sulla lista `lista-correzioni.json`: «ok vai», cioè L1-L4 approvate e, per D1, grassetto non riprodotto. Correzioni applicate con script il 2026-10-14:

- L1 (C03, Circolare p. 256): tolto il punto finale della nota 2, come stampa la Gazzetta; anomalia della fonte conservata.
- L2 (C02, Circolare p. 256): corsivo su *riparazione o intervento locale*, *miglioramento*, *adeguamento*.
- L3 (C24, Circolare p. 257): corsivo sulle sole lettere *b*), *c*), *d*) od *e*).
- L4 (N33, NTC p. 296): corsivo su *a)*, punto in tondo.
- D1 (Circolare pp. 256-257): il grassetto di alcuni pedici E di ζE, di un punto e di una virgola non si riproduce; anomalia tipografica della fonte registrata nel verbale.

Diff `diff-correzioni.diff`: 4 righe, tutte conformi alla lista, nessuna estranea. Impronte prima e dopo in `snapshot-prima-dopo.json`. Resa dopo con `render-capitolo.py`: cinque pagine, tag e didascalie a posto (`modifiche/resa-dopo/`).

Controllo delle modifiche (§ 8) dello stesso V: esito OK sui 5 rilievi, diff limitato alle righe 21, 23, 99 e 111 del testo depurato, resa corretta; V conferma che il punto dopo «a)» è in tondo. `modifiche/attestazione-v-modifiche.json`.

Snapshot finale dei 4 file: `snapshot-finale.json`, SHA-256 `70dbe9d6fcc8a18704c4dc50c5d4f87a149a735d872c3fde55b29740363813ec`.

G7 primo tentativo, 2026-10-14: `KO` documentale (`G7-r01-KO.json`): manifest senza la resa finale, scheda non aggiornata, verbale assente; testo conforme. Rimedi: resa finale nel dossier e nel manifest, rigenerato con 52 file (`manifest-rilascio.json`; il precedente da 40 file resta come `manifest-rilascio-r01.json`), questa sezione della scheda e il verbale. Lotto ripresentato a V per la sola riconciliazione.

G7 secondo tentativo, 2026-10-14: `OK` sul manifest da 52 file (`G7-r02.json`), con un'osservazione sulla dicitura «Correzioni (C)» del verbale. Il piano di `registra` ha poi richiesto lo snapshot finale dentro il manifest: manifest rigenerato con 54 file (il precedente resta `manifest-rilascio-r02.json`) e verbale aggiornato di conseguenza, con la dicitura corretta in «Correzioni di ERR-MD (nessuna AF-COR)». Lotto ripresentato a V per la riconciliazione finale.

