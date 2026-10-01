---
scope_id: ntc2018-8.3
atti:
  - "D.M. 17/01/2018, § 8.3 VALUTAZIONE DELLA SICUREZZA"
  - "Circolare 21/01/2019 n. 7 C.S.LL.PP., § C8.3 VALUTAZIONE DELLA SICUREZZA"
file_markdown: cap08/8.3-valutazione-sicurezza.md
righe_registro: [8.3]
fonte_ntc: {pdf: verifica-conformita/fonte-ufficiale/GU-2018-42-SO8-DM-17-01-2018.pdf, pagine_fisiche: 294-295}
fonte_circolare: {pdf: verifica-conformita/fonte-ufficiale/GU-2019-35-SO5-Circolare-7-2019.pdf, pagine_fisiche: 255-256}
unita_registro: 1
file_scope: 1
pagine_fonte: 4
formule_numerate_preliminari: 0
tabelle_preliminari: 0
figure_preliminari: 0
stato: CHIUSO
agente: OC
macchina: OpenClaw
presa_in_carico: 2026-09-13T09:00:00+02:00
subentro: 2026-09-30T17:05:00+02:00
procedura: VC-NTC/6
procedura_sha256: 403157d71ba00bababeefad6b920915e631627bdf55e9ff1e9679cdbeea8383c
catalogo_sha256: d71319206ec54bcac3639dfd0b97c41754fa1062655b2d35c36ee5d6cb3036d6
snapshot_iniziale_sha256: aff44285ba6fbf1614fa8b3e0252cb7a4f63db8ea6399c2f398bda4e431129db
snapshot_sha256: 4edeaeea47bddd2fd20f85f96df429f5236993b55b69033c8122a968de2a03e6
giro_g6: 1
max_giri: 3
rilievi_aperti: 0
gate: {G0: OK, G1: OK, G2: OK, G3: OK, G4: OK, G5: OK, G6: OK, G7: OK}
attesa_decisione: []
prossimo_passo: "Nessuna sul file: VC conclusa sullo snapshot registrato."
routing_effettivo:
  coordinatore: {modello: xai/grok-4.7, ragionamento: off, ruolo: C, contesti: 1, agente: "NormaNTC18 (OC)"}
  meccanica: "script locali, applica-r1-r2.py"
  verificatore_previsto: {modello: xai/grok-4.7, ruolo: V, isolamento: istruttivo}
---

# Scheda scope § 8.3

## Chiusura registrata il 2026-09-30, NormaNTC18 (OC)

Riga `8.3` registrata `VC-OK` il 2026-09-30 su ordine di Sandro. Snapshot `4edeaeea47bddd2fd20f85f96df429f5236993b55b69033c8122a968de2a03e6`. Il rapporto G6 integrale in /tmp è perso. Il ritaglio è stato ricontrollato. [Verbale](verbale-VC-ntc2018-8.3-2026-09-30.md). Firma: NormaNTC18 (OC).

Prossima azione: Nessuna sul file: VC conclusa sullo snapshot registrato.


## Modifica CIR256-P-FON, 2026-09-30, NormaNTC18 (OC)

Sandro: «sistema tu». Script `applica-cir256-p-fon.py`: un solo spazio tolto in `cap08/8.3-valutazione-sicurezza.md`, da `terreno- fondazione` a `terreno-fondazione`. Snapshot prima `29b54df6d2237da6978fc3c4a847428c77e3376867854790b49c28aabd837f2a`, dopo `4edeaeea47bddd2fd20f85f96df429f5236993b55b69033c8122a968de2a03e6`. Resa `dopo-cir256-p-fon.pdf`, pagina 3, parola unita. Lo spazio di `l’ obbligatorietà` resta, come in fonte. Controllo: `_tmp_render/cap08/vc-8.3-20260930-oc/controllo-cir256-p-fon.md`.


## G5, 2026-09-30, NormaNTC18 (OC)

Resa canonica di tre pagine: `_tmp_render/cap08/vc-8.3-20260930-oc/g5-target.pdf`. Nessun tag con parentesi tonde (lo scope non ha formule numerate) e nessuna didascalia automatica. Vista delle tre pagine: rubrica C8.3 in maiuscolo e senza punto, capoversi staccati, ζ_E, ζ_{V,i} e a_g S leggibili, niente sovrapposizioni né caratteri mancanti. Il primo lancio dello script è uscito dopo il PDF perché il python di sistema non vede PyMuPDF e manca pdftotext; il controllo è stato rifatto con PyMuPDF. G5 OK.

Prossima azione: G6 integrale sul solo § 8.3: fonte-prima, poi confronto.

## Subentro e correzioni R1-R2, 2026-09-30, NormaNTC18 (OC)

Sandro, 2026-09-30, «vai»: subentro esplicito sul lucchetto GROK del 13/9. Decisione: applicare R1 e R2, poi un G6; non chiudere VC-OK senza il controllo indipendente.

Dal passaggio non ancora iniziato (correzioni e G6) si adotta VC-NTC/6. Canone G6 e catalogo invariati rispetto alla revisione 5. `giro_g6` resta 0 fino all'accesso di V al target. G1 riusato: ricognizione 2026-09-09 e ricontrollo 2026-09-13, ancora dentro i trenta giorni; oggi nessun nuovo ricontrollo sulla banca dati.

R1 e R2 applicati con `_tmp_render/cap08/vc-8.3-20260930-oc/applica-r1-r2.py`, sostituzioni esatte. Rubrica Circolare: `## C8.3 VALUTAZIONE DELLA SICUREZZA`, senza punto, come in 8.2. Sette stacchi di capoverso misurati sulla Gazzetta (interlinea circa 5,3 pt contro 2,7 pt dentro il capoverso): apertura, modalità, stato di progetto (con la frase sui § C.8.5-C.8.7), esclusione, parametri, C2.1, azioni non sismiche, azioni sismiche, fondazioni. Le due voci ζ erano già staccate. La prosa, a capo esclusi, è identica. Snapshot `29b54df6d2237da6978fc3c4a847428c77e3376867854790b49c28aabd837f2a`. NTC non toccata.

## Presa in carico 2026-09-13, GROK

Autorizzazione esplicita di Sandro: «andiamo con 8.3». Perimetro: solo `cap08/8.3-valutazione-sicurezza.md`, NTC § 8.3 pp. 294-295 fino a prima di 8.4, Circolare C8.3 pp. 255-256 fino a prima di C8.4. 8.2 resta VC-OK.

Procedura VC-NTC/4: elenco unico delle non conformità, nessuna correzione prima della decisione di Sandro.

Lavorazione: `_tmp_render/cap08/vc-8.3-20260913-grok/`.

## Confronto iniziale 2026-09-13, GROK

G0/G1/G4 OK. G2-G3 KO: due ERR-MD di presentazione in C8.3 (rubrica, capoversi fusi). NTC § 8.3 conforme. Target invariato. Elenco: `_tmp_render/cap08/vc-8.3-20260913-grok/rapporto-c.md`.

Prossima azione: Attendere la decisione di Sandro su R1 e R2 del § 8.3.
