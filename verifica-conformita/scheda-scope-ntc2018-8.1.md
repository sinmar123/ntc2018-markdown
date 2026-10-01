---
scope_id: ntc2018-8.1
atti:
  - "D.M. 17/01/2018, § 8.1 OGGETTO"
  - "Circolare 21/01/2019 n. 7 C.S.LL.PP., § C8 e § C8.1 OGGETTO"
file_markdown: cap08/8.1-oggetto.md
righe_registro: [8.1]
fonte_ntc: {pdf: verifica-conformita/fonte-ufficiale/GU-2018-42-SO8-DM-17-01-2018.pdf, pagine_fisiche: 294}
fonte_circolare: {pdf: verifica-conformita/fonte-ufficiale/GU-2019-35-SO5-Circolare-7-2019.pdf, pagine_fisiche: 253-254}
unita_registro: 1
file_scope: 1
pagine_fonte: 3
formule_numerate_preliminari: 0
tabelle_preliminari: 0
figure_preliminari: 0
stato: CHIUSO
agente: GROK
macchina: W520
presa_in_carico: 2026-09-11T19:20:00+02:00
procedura: VC-NTC/3
procedura_sha256: 4bd4440a6f9b204338e97ecf78c9bb74ab0d9e04f7478b9c97c436c62e817c7c
catalogo_sha256: d71319206ec54bcac3639dfd0b97c41754fa1062655b2d35c36ee5d6cb3036d6
snapshot_iniziale_sha256: 130d0365b7fce252bfcb15f1841a3723f960f290fb53017c06435f28ae95ada1
snapshot_sha256: 80a2c5a3af47c879dda192b43e7a729fd81a9c30fd5a53407cb2a4c08bdd832b
giro_g6: 2
max_giri: 3
rilievi_aperti: 0
procedura_chiusura: VC-NTC/4
procedura_chiusura_sha256: 9c43358436f1e4f3ba92b16b95872afccf45e6cdb277d365e4fe5ea16f546a96
data_registrazione: 2026-09-12
gate: {G0: OK, G1: OK, G2: OK, G3: OK, G4: OK, G5: OK, G6: OK, G7: OK}
attesa_decisione: []
prossimo_passo: "Nessuna sul file: VC conclusa sullo snapshot registrato."
routing_effettivo:
  coordinatore: {modello: grok-4.6, ragionamento: xhigh, ruolo: C, contesti: 1, nota: "Equivalente Grok Build della sessione; Sol non disponibile su questo runtime."}
  meccanica: "script locali"
  verificatore_previsto: {modello: grok-4.6, ragionamento: xhigh, ruolo: V, isolamento: istruttivo, contesto: fresco}
  v_modifiche_g7: {modello: grok-4.6, ragionamento: xhigh, ruolo: V, isolamento: istruttivo, firma: GROK-V3}
---

# Scheda scope § 8.1

## Chiusura registrata il 2026-09-12, GROK

Riga `8.1` registrata `VC-OK` il 2026-09-12. G6 integrale R02 14/14 e controllo localizzato dei due corsivi C8.1 secondo VC-NTC/4. Snapshot `80a2c5a3af47c879dda192b43e7a729fd81a9c30fd5a53407cb2a4c08bdd832b`. 8.2 escluso. [Verbale](verbale-VC-ntc2018-8.1-2026-09-12.md). Firma: GROK.

Prossima azione: Nessuna sul file: VC conclusa sullo snapshot registrato.


## Presa in carico 2026-09-11, GROK

Autorizzazione esplicita di Sandro: VC del capitolo 8 inteso come primo paragrafo, fino al primo sottocapitolo escluso. Perimetro: solo `cap08/8.1-oggetto.md`, NTC § 8.1 fino a prima di 8.2, Circolare C8 introduttiva e C8.1 fino a prima di C8.2. Il § 8.2 non è aperto.

Il § 3.6 resta `IN-CORSO` di CDX su file diversi. `prendi` rifiuta un secondo IN-CORSO globale; la presa di questa riga è su file disgiunti, senza subentro sul 3.6. CSV aggiornato sulla sola riga `8.1`.

Lavorazione: `_tmp_render/cap08/vc-8.1-20260911-grok/`.

## Sospensione 2026-09-11, GROK

Sandro ha chiesto di fermarsi al § 8.1. G0-G5 `OK`. G6 R01 `KO`: tre `ERR-MD` (omissione di `CAPITOLO` nel titolo C8; fusione dei capoversi C8 e C8.1), poi corretti. G6 R02, già in corso, ha chiuso comunque `KO`: 14/14 ID, due `ERR-MD` di corsivo in C8.1 (`Le costruzioni esistenti` e i due virgolettati NTC; `struttura completamente realizzata`). Rapporto in `_tmp_render/cap08/vc-8.1-20260911-grok/g6-r02/`. Target non modificato dopo R02. G7 non avviato. Il § 8.2 resta fuori perimetro.

## Adjudicazione corsivi C8.1, 2026-09-12, GROK

C ha accolto i due `ERR-MD` del G6 R02. Applicati in `cap08/8.1-oggetto.md`: corsivo su *Le costruzioni esistenti* e sui due virgolettati NTC nel primo capoverso C8.1; corsivo su *struttura completamente realizzata* nel terzo. Snapshot `80a2c5a3af47c879dda192b43e7a729fd81a9c30fd5a53407cb2a4c08bdd832b`. Zero rilievi aperti. Serve G5 e G6 R03.

Prossima azione: G5 sul target corretto e G6 R03 integrale sul solo § 8.1; 8.2 escluso.
