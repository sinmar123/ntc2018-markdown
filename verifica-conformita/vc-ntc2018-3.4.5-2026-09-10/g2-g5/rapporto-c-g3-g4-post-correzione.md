# Rapporto C G3-G4 post-correzione, § 3.4.5

Data: 2026-09-09. Coordinatore: Hermes NTC-VC / HRM.

## E distinto

La conversazione figlia `deleg_b940d358`, subagent `sa-0-bad5cdb7`, ha operato esclusivamente come ruolo E sul file `cap03/3.4.5-neve-coefficiente-termico.md`. Ha applicato le quattro sostituzioni della lista chiusa e ha dichiarato zero differenze non autorizzate. Il coordinatore ha riletto direttamente il target e verificato i quattro punti.

Runtime effettivo di E: ereditato dal coordinatore, `gpt-5.6-sol`, provider `openai-codex`, ragionamento `high`, in conversazione separata. Non viene dichiarato `terra/medium`, perché l'entry point CLI registrato nel collaudo non è disponibile nel container corrente.

## Ricollazione

- Rubrica NTC: `3.4.5. COEFFICIENTE TERMICO`, conforme.
- Simbolo: `$\mathrm{C}_{\mathrm{t}}$ = 1.`, `C` e pedice `t` romani, conforme alla fonte.
- Rubrica Circolare: `C3.4.5 COEFFICIENTE TERMICO`, senza punto dopo il numero, conforme.
- Secondo capoverso Circolare: termina con `1 W/m²K°` senza punto, conforme.
- Lessico, capoversi, punteggiatura restante, `1,5 kN/m²`, `0°C` e `1,2`: invariati e conformi.

Il file depurato post-correzione coincide byte per byte con `source-attesa-normalizzata.md`. Snapshot target post-indici: SHA-256 `4527c114103e513df46c7deb497471aeb995f2bf2a4907e652678dc047e79f19`. Snapshot depurato: SHA-256 `4a19fc7bb9eaa8242be7904c8d6e8da44dfb50f3762c7b32da26401d2da61756`.

## Indici e controlli statici

Il generatore degli indici ha verificato 311 file e 1754 collegamenti interni; il manifest registra un solo file con SHA complessivo mutato, il target 3.4.5, e 311 corpi invariati rispetto all'intervento sugli apparati. Il linter del registro ha chiuso con 311 righe, 11 colonne, zero errori e zero avvisi. La vista XLSX è stata rigenerata e risulta conforme al CSV, con 311 righe, 11 colonne, 381 collegamenti e zero differenze non dichiarate.

## Gate

- G3 ripetuto: `OK`, zero rilievi aperti.
- G4 ripetuto: `OK`, zero rilievi aperti.
- G5: `BLOCCATO_HOST`; il tentativo canonico R02 si ferma con `FileNotFoundError: pandoc`.
- G6 e G7: non avviati.

Firma: Hermes NTC-VC / HRM.
