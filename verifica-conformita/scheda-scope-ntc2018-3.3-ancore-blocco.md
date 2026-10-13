---
scope_id: ntc2018-3.3-ancore-blocco
stato: IN-CORSO
agente: CCC
presa_in_carico: 2026-10-13T16:58:45+00:00
procedura: VC-NTC/7
procedura_sha256: 01c7f0ed9908e4c7620189a0073b2892afe37aa499f99cf50329a84b43960e67
catalogo_sha256: dd5f1b9980e6fd37bd0444277d8b69d6ac0c000b91c1cf659a4f9a398b4a7c43
file_markdown: [cap03/3.3.1-vento-velocita-base-di-riferimento.md, cap03/3.3.2-vento-velocita-di-riferimento.md, cap03/3.3.7-vento-coefficiente-di-esposizione.md, cap03/3.3.8-vento-coefficienti-aerodinamici.md]
righe_registro: ["3.3.1", "3.3.2", "3.3.7", "3.3.8"]
perimetro: "correzione localizzata (§ 8): tolti 9 identificativi di blocco `^…` in coda a righe di formula, didascalia e titolo di tabella; testo normativo escluso"
riapertura_vc_ok: {motivo: "identificativi di blocco dell'editor di note non più usato, apparato di navigazione della voce 11 del catalogo", autorizzazione: "Sandro, 2026-10-13, lista di 9 righe approvata («ok vai»)"}
snapshot_iniziale: verifica-conformita/vc-ntc2018-3.3-ancore-blocco-2026-10-13/snapshot-iniziale.json
snapshot_sha256: f4d7fcba65ad3f529049634e1b7427b966c9de6dd6b55565a46638a63b8c0d67
snapshot_manifest: verifica-conformita/vc-ntc2018-3.3-ancore-blocco-2026-10-13/snapshot-finale.json
giro_g6: 1
max_giri: 3
rilievi_aperti: 0
gate: {G0: OK, G1: OK, G2: OK, G3: OK, G4: OK, G5: OK, G6: IN_CORSO, G7: DA_FARE}
prossimo_passo: "Applicare la lista approvata, controllo delle modifiche di V e G7"
routing_effettivo:
  C: {agente: sessione cloud, modello: Opus, contesti: 1}
  preparazione: script_locali
  E: non_attivato
  V: {agente: subagente a contesto nuovo, modello: Opus, contesti: 1, isolamento: istruttivo, compito: controllo delle modifiche e G7}
consumi: {contatori: non_disponibili}
---

# Identificativi di blocco nei §§ 3.3.1, 3.3.2, 3.3.7 e 3.3.8

## Correzioni applicate e G0-G5, 2026-10-13, CC cloud

G0: quattro file, nove righe, solo apparato di navigazione. G1: ricognizione piena del 2026-10-13 sulla Gazzetta Ufficiale, perché quella del 2026-09-09 superava i trenta giorni; schede di decreto e Circolare invariate rispetto al 2026-09-12, unico atto modificativo il D.M. 9 marzo 2023, estraneo al § 3.3; Normattiva non restituisce la scheda del decreto. G2-G4: testo normativo invariato, il diff contiene esattamente le 9 righe approvate e nient'altro. G5: resa prima e dopo con `render-capitolo.py`; cambiano 5 pagine (3.3.1 pp. 1-2, 3.3.2 p. 1, 3.3.8 pp. 9-10), solo perché la vecchia regola di resa che toglieva il marcatore mangiava anche la riga vuota seguente; 3.3.7 identico. Il § 3.3.8 si rende qui solo con una resa ausiliaria (indice interno a cinque livelli). Snapshot finale `f4d7fcba65ad3f529049634e1b7427b966c9de6dd6b55565a46638a63b8c0d67`.

Prossima azione: Controllo delle modifiche di V e G7.

## Presa in carico 2026-10-13, CC cloud

Riapertura di quattro paragrafi `VC-OK` per una correzione localizzata del § 8 della procedura, approvata da Sandro il 2026-10-13. La lista toglie 9 identificativi di blocco `^…` dall'apparato di navigazione; nessun testo della fonte cambia. Le impronte dei quattro file coincidono con gli snapshot dei rispettivi verbali VC-OK. `giro_g6: 1` indica il G6 integrale originario di ciascun file, che resta valido: questo scope non ne esegue uno nuovo, solo il controllo delle modifiche.

Prossima azione: Applicare la lista approvata, controllo delle modifiche di V e G7.
