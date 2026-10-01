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
agente: OC
macchina: OpenClaw
presa_in_carico: 2026-10-01T12:10:00+02:00
procedura: VC-NTC/6
procedura_sha256: 403157d71ba00bababeefad6b920915e631627bdf55e9ff1e9679cdbeea8383c
catalogo_sha256: d71319206ec54bcac3639dfd0b97c41754fa1062655b2d35c36ee5d6cb3036d6
snapshot_iniziale_sha256: vedi-corpo
snapshot_sha256: vedi-corpo
giro_g6: 1
max_giri: 3
rilievi_aperti: 7
gate: {G0: OK, G1: OK, G2: OK, G3: OK, G4: OK, G5: OK, G6: DA_FARE, G7: DA_FARE}
attesa_decisione: []
prossimo_passo: "Attendere Sandro sui 7 rilievi G6. Non correggere."
routing_effettivo:
  coordinatore: {modello: xai/grok-4.7, ragionamento: off, ruolo: C, contesti: 1, agente: "NormaNTC18 (OC)"}
  meccanica: "script locali"
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
