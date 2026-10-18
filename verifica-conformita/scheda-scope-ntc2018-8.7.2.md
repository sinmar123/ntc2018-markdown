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
giro_g6: 0
max_giri: 3
rilievi_aperti: 0
gate: {G0: OK, G1: OK, G2: OK, G3: OK, G4: OK, G5: OK, G6: in_corso, G7: attesa}
attesa_decisione: []
prossimo_passo: "G6 integrale con V Codex gpt-5.6-terra in due blocchi; poi G7 con gpt-6.1-sol se il G6 è a zero rilievi."
lavorazione: verifica-conformita/vc-ntc2018-8.7.2-2026-10-18/
routing_effettivo:
  C: {agente: "Grok Bot (GBOT-verifica-ntc)", ruolo: "coordinamento, controllo sulla fonte, lista per Sandro, worktree e commit"}
  confronto_iniziale: {agente: "Codex sul W520", modello: "gpt-5.6-terra", sandbox: read-only, ruolo: "confronto integrale sulla fonte", blocchi: "A (md 1-123, NTC 298 e Circolare 283-285) 15:51-15:59; B (md 124-344, Circolare 285-289) 15:51-15:55", esito: "A 22 ERR-MD di forma e 1 DUBBIO; B 35 ERR-MD di forma; nessuna voce sostanziale"}
  primo_filtro: "corpus structural-codes, solo come filtro e mai come fonte"
  E: non_attivato
  V: "da attivare: gpt-5.6-terra ordinario, gpt-6.1-sol per dubbi e G7 (procedura rev. 10, § 5)"
consumi: {codex_terra_A: "149.256 token, 8 min", codex_terra_B: "164.504 token, 4,5 min", structural_codes: "script locale, nessun LLM", sol: "non usato"}
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
