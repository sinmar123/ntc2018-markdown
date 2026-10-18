---
scope_id: ntc2018-8.7.2
stato: IN-CORSO
agente: GBOT
agente_istanza: GBOT-verifica-ntc
macchina: "W520; GBOT-verifica-ntc come C; Codex sul W520 per confronto integrale, G5 e G6"
presa_in_carico: 2026-10-18
procedura: VC-NTC/10
procedura_sha256: bc54cd41effc1e2aaf3f20f0dd75b99b4a3279df787a2eb35faaec7261b41b22
catalogo_sha256: 279267c27d0aa19045045f6110d8cece1f5ec99ebcaaceac3b7f267676372f48
atti:
  - "D.M. 17/01/2018, § 8.7.2, dalla rubrica fino a prima di 8.7.3"
  - "Circolare 21/01/2019 n. 7, § C8.7.2 con C8.7.2.1-C8.7.2.4, dalla rubrica fino a prima di C8.7.3"
file_markdown: [cap08/8.7.2-progettazione-interventi-costruzioni-in-calcestruzzo-armato-o-in-acciaio.md]
righe_registro: ["8.7.2"]
base_git: 856c566
snapshot_sha256: 6b338b8c2610ab51603db0dc9aa140ba6b0a15cbdfc68e0583c0f5626ae3b689
giro_g6: 1
max_giri: 3
rilievi_aperti: 0
gate: {G0: OK, G1: OK, G2: OK, G3: OK, G4: OK, G5: OK, G6: OK, G7: in_corso}
attesa_decisione: []
prossimo_passo: "G7 tentativo 2 con Codex gpt-6.1-sol (high, read-only, contesto nuovo); se OK registra, governo, diario e commit locali."
lavorazione: verifica-conformita/vc-ntc2018-8.7.2-2026-10-18/
routing_effettivo:
  C: {agente: "Grok Bot (GBOT-verifica-ntc)", ruolo: "coordinamento, controllo sulla fonte, lista per Sandro, worktree e commit"}
  confronto_iniziale: {agente: "Codex sul W520", modello: "gpt-5.6-terra", sandbox: read-only, ruolo: "confronto integrale sulla fonte", blocchi: "A (md 1-123, NTC 298 e Circolare 283-285) 15:51-15:59; B (md 124-344, Circolare 285-289) 15:51-15:55", esito: "A 22 ERR-MD di forma e 1 DUBBIO; B 35 ERR-MD di forma; nessuna voce sostanziale"}
  primo_filtro: "corpus structural-codes, solo come filtro e mai come fonte"
  E: non_attivato
  V: {agente: "Codex sul W520", modello: "gpt-5.6-terra", ragionamento: high, sandbox: read-only, ruolo: "G6 giro 1, blocchi b01 e b02, contesti nuovi", esito: "KO: b01 4 rilievi, b02 2 rilievi"}
  V_modifiche: {agente: "Codex sul W520", modello: "gpt-5.6-terra", ragionamento: high, sandbox: read-only, ruolo: "controllo delle modifiche § 8, contesto nuovo", esito: OK}
  G7: {agente: "Codex sul W520", modello: "gpt-6.1-sol", ragionamento: high, sandbox: read-only}
consumi: {codex_terra_A: "149.256 token, 8 min", codex_terra_B: "164.504 token, 4,5 min", structural_codes: "script locale, nessun LLM", codex_terra_g6_b01: "fase 1 276.110 input (239.488 in cache), 6.332 output; fase 2 1.387.422 input (1.298.176 in cache), 21.246 output; 3,5 + 8 min", codex_terra_g6_b02: "fase 1 258.065 input (223.488 in cache), 4.366 output; fase 2 615.542 input (534.016 in cache), 15.529 output; 2,5 + 6 min", codex_terra_modifiche: "369.881 input (312.576 in cache), 3.761 output; 2,7 min", sol: "solo G7"}
---

# Scheda scope § 8.7.2

Sola riga 8.7.2, file `cap08/8.7.2-progettazione-interventi-costruzioni-in-calcestruzzo-armato-o-in-acciaio.md`, Norma e Circolare. Restano fuori 8.7, 8.7.1, 8.7.3-8.7.5, C8.7.3 e seguenti e ogni altro file normativo.

## Storia e autorizzazioni

- Sandro ha autorizzato lo scope il 2026-10-18 alle 15:45 con «ok riparti»: VC di 8.7.2 con la parte di Circolare corrispondente, procedura rev. 10, costi bassi, lavoro lungo a Codex sul W520.
- Ramo `gbot/vc-8.7.2-261018` creato sopra `cdx/vc-8.7.1-261017` (856c566), perché la PR n. 19 non è ancora unita.

## G0-G1

G0: Norma pagina fisica 298 (stampata 294), da `8.7.2.` a prima di `8.7.3.`, pagina condivisa con 8.7.1 e 8.7.3. Circolare pagine fisiche 283-289 (stampate 279-285), da `C8.7.2` a prima di `C8.7.3`; 283 condivisa con C8.7.1, 289 con C8.7.3. Otto pagine, sotto la soglia di 15. Le colonne del registro coincidono già. PDF ufficiali SHA-256 `dda1e397…5a46` (NTC) e `f7c3b8d1…ed7c` (Circolare).

G1: ricognizione piena del 2026-10-13 riusata; ricontrollo mirato del 2026-10-18 sulle schede GU dei tre atti, senza avvisi nuovi (`vc-ntc2018-8.7.2-2026-10-18/g1/ricontrollo-20261018.json`).

Firma: GBOT-verifica-ntc, 2026-10-18.

## Lista delle correzioni (v1, 2026-10-18)

Confronto integrale di Codex `gpt-5.6-terra` (high, sola lettura) in due blocchi: 57 ERR-MD tutte di forma e 1 dubbio. Primo filtro con structural-codes (solo candidati). Controllo di C sulla Gazzetta, livello vettoriale e ritagli fino a 600 dpi, con tutte le 14 formule numerate: aggiunte 5 voci sostanziali che Codex non aveva visto (S-01 esponente di [C8.7.2.1] senza segno meno; S-02 pedice o sotto [C8.7.2.2]; S-03-S-05 V_W nelle formule [C8.7.2.8]-[C8.7.2.10]) e 10 di forma; corrette due proposte di Codex (A-16, B-33). Totale 70 voci, 5 sostanziali e 65 di forma; 4 dubbi con proposta di testo invariato; 6 anomalie della fonte conservate.

File: `vc-ntc2018-8.7.2-2026-10-18/lista-correzioni-c.md`, `lista-correzioni.json` (verificata con `applica-lista` senza `--applica`: 70 voci, nulla scritto), `diff-proposto.patch`, `confronto-sostanziali-8.7.2.pdf`, `confronto-iniziale/codex-terra-blocco-A.json` e `-B.json`. Target invariato (SHA-256 `5fe477b8…4d03`).

Firma: GBOT-verifica-ntc, 2026-10-18.

## Approvazione e applicazione (2026-10-18)

- **16:15 (ora di Roma):** Sandro approva l'intera lista v1, 70 voci (5 sostanziali S-01…S-05, 65 di forma); i dubbi D-01…D-04 restano a testo invariato.
- **16:17:** `applica-lista` piano e `--applica`: 70 voci, solo il target 8.7.2. Il risultato coincide con il target proposto prima dell'approvazione. `verifica-lista` rispetto a `61aa496`: OK. Indici interni rigenerati con `genera-indici-interni.py` (311 file, corpi invariati). Lint del registro: 0 errori. Evidenza: `vc-ntc2018-8.7.2-2026-10-18/decisione-applicazione-20261018.json`.
- **16:19:** G5. Testo composto con `componi-scope` e depurato (353 righe); resa canonica `g5/resa-finale.pdf` (8 pagine, 14 tag a quadre), osservata da C senza tagli o caratteri mancanti. Mappa e due blocchi G6 in `mappa-g5.json` e `config-g6.json`: b01 NTC 298 e Circolare 283-286, righe 1-205; b02 Circolare 287-289, righe 206-353.

Firma: GBOT-verifica-ntc, 2026-10-18.

## G6, giro 1 (2026-10-18)

- **16:21-16:25 (ora di Roma):** fase 1, inventario fonte-prima di V (Codex `gpt-5.6-terra`, high, read-only, contesto nuovo per blocco, senza `--always-approve`); `valida-inventario` e `rivela` OK su b01 e b02.
- **16:28-16:36:** fase 2, confronto nello stesso contesto. `valida-g6`: schema OK; b01 38 ID coperti, 4 rilievi; b02 28 ID coperti, 2 rilievi. Esito KO.
- Giudizio di C sulla fonte (livello vettoriale e ritagli a 600-800 dpi): COND-C285-DOVE-1 fondato (voce 18: i blocchi «dove:» vanno resi come elenco), esteso ai blocchi di [C8.7.2.8] e [C8.7.2.13]; l'errore viene dalla lista v1. FORM-287-03 riguarda solo la resa ed è da decidere. F-C285-87221, COND-C285-POST-ALFA e FORM-289-01 non sono fondati. C286-87234-FINO è una scelta di impacchettamento, non un errore del testo.
- Nessuna correzione applicata, G7 non avviato. Evidenze: `vc-ntc2018-8.7.2-2026-10-18/g6/`, `sequenza-g6.json`, `esito-g6.json`. Scarti dichiarati: C ha trascritto byte per byte i JSON di V (sandbox read-only); entrambi i V hanno letto lo SKILL.md del plugin pdf di Codex; V b02 ha fatto una chiamata Computer Use con risultato vuoto.

Firma: GBOT-verifica-ntc, 2026-10-18.

## Decisione sui rilievi e controllo delle modifiche (2026-10-18)

- **16:53 (ora di Roma):** Sandro decide sui sei rilievi (`vc-ntc2018-8.7.2-2026-10-18/decisione-g6-20261018.json`): COND-C285-DOVE-1 fondato, i tre blocchi «dove:» diventano elenco puntato (voce 18), senza toccare il testo; FORM-287-03 chiuso senza modifiche, [C8.7.2.8] resta com'è (solo resa, decisione di Sandro); F-C285-87221, COND-C285-POST-ALFA e FORM-289-01 chiusi senza modifiche (vettoriale e ritagli ad alta risoluzione); C286-87234-FINO chiuso come ERR-AUDIT documentale sul pacchetto.
- **16:55-16:56:** lista g6 di 3 voci (21 righe; nel PDF di confronto C ne aveva contate 22 per errore, perimetro e testo invariati) applicata con `applica-lista` piano e `--applica`; indici interni rigenerati (target invariato dagli indici); lint 0 errori; `verifica-lista` della lista v1 più g6, 73 voci, sulla base `61aa496`: OK. Target `6b338b8c…3b689`.
- **16:56:** `pacchetto-modifiche` sugli stessi blocchi del G6, con nuova resa di 9 pagine; confronto meccanico con la resa G5 e osservazione dell'intero documento da parte di C.
- **16:59-17:02:** controllo delle modifiche con V Codex `gpt-5.6-terra` (high, read-only, contesto nuovo): diff OK, tre blocchi chiusi, resa OK, nessun nuovo rilievo, esito OK (`g6-modifiche/esito-terra.json`). `giro_g6` resta 1; il § 8 non prevede un G6 di riscontro. G6: OK.

Firma: GBOT-verifica-ntc, 2026-10-18.

## G7 tentativo 1 (2026-10-18)

- **17:09-17:11 (ora di Roma):** G7 con Codex `gpt-6.1-sol` (high, read-only, contesto nuovo) sul lotto di chiusura (verbale, piano `chiusura.json`, manifest di 88 file `5fc2b42a…dd706`, riepilogo meccanico, attestazioni). Esito `KO`: gate G0-G6 confermati OK, G7 KO per due `ERR-AUDIT` documentali: G7-AUDIT-01, il PDF di confronto con le prove di C sui dubbi del G6, citato da `decisione-g6-20261018.json` ed `esito-g6.json`, non è nel manifest (§ 9); G7-AUDIT-02, `chiusura.json` non riporta l'impronta del manifest, come chiedeva la consegna di C. Giudizio in `vc-ntc2018-8.7.2-2026-10-18/G7-tentativo-1-KO.json` (percorso locale redatto, `G7-tentativo-1-redazione.json`). V ha letto l'AGENTS.md del workspace come istruzione preliminare del runtime.
- Nessuna rettifica applicata e nessun nuovo tentativo: si attende la decisione di Sandro.

Firma: GBOT-verifica-ntc, 2026-10-18.

## Rettifica dopo il G7 tentativo 1 (2026-10-18)

- **18:55 (ora di Roma):** Sandro approva le due rettifiche documentali proposte e il G7 tentativo 2 con Codex `gpt-6.1-sol`, high, read-only, contesto nuovo, conservando il tentativo 1.
- G7-AUDIT-01: PDF di confronto dei rilievi G6, ritagli e span vettoriali archiviati in `vc-ntc2018-8.7.2-2026-10-18/prove-c/` con `prove-c-sha256.json`; manifest e verbale rigenerati; manifest del tentativo 1 conservato come `manifest-rilascio-g7-tentativo-1.json`.
- G7-AUDIT-02: campo `manifest_sha256` aggiunto a `chiusura.json`.
- Target, copertura e giudizi invariati (§ 8, errore solo documentale).
- Lotto di chiusura rigenerato per il G7 tentativo 2.

Firma: GBOT-verifica-ntc, 2026-10-18.
