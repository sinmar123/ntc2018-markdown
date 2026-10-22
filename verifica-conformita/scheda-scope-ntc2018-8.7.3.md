---
scope_id: ntc2018-8.7.3
stato: IN-CORSO
agente: GBOT
agente_istanza: GBOT-verifica-ntc
macchina: "W520; GBOT-verifica-ntc come C; Codex sul W520 (CDX) per confronto integrale, G5 e G6"
presa_in_carico: 2026-10-22
procedura: VC-NTC/10
procedura_sha256: bc54cd41effc1e2aaf3f20f0dd75b99b4a3279df787a2eb35faaec7261b41b22
catalogo_sha256: 279267c27d0aa19045045f6110d8cece1f5ec99ebcaaceac3b7f267676372f48
atti:
  - "D.M. 17/01/2018, § 8.7.3, dalla rubrica fino a prima di 8.7.4"
  - "Circolare 21/01/2019 n. 7, § C8.7.3, dalla rubrica fino a prima di C8.7.4"
file_markdown: [cap08/8.7.3-progettazione-interventi-costruzioni-miste.md]
righe_registro: ["8.7.3"]
base_git: 33f9a3d
giro_g6: 0
max_giri: 3
rilievi_aperti: 0
gate: {G0: OK, G1: in_corso, G2: in_corso, G3: in_corso, G4: in_corso, G5: attesa, G6: attesa, G7: attesa}
attesa_decisione: [lista delle correzioni]
prossimo_passo: "Confronto integrale con Codex gpt-5.6-terra, secondo passaggio mirato di Terra, dubbi a gpt-6.1-sol, controllo a campione di C sulla fonte, lista per Sandro."
lavorazione: verifica-conformita/vc-ntc2018-8.7.3-2026-10-22/
routing_effettivo:
  C: {agente: "Grok Bot (GBOT-verifica-ntc)", ruolo: "coordinamento, controllo a campione sulla fonte, lista per Sandro, worktree e commit"}
  confronto_iniziale: {agente: "Codex sul W520 (CDX)", modello: "gpt-5.6-terra", sandbox: read-only, ruolo: "confronto integrale sulla fonte e secondo passaggio mirato"}
  dubbi: {agente: "Codex sul W520 (CDX)", modello: "gpt-6.1-sol", sandbox: read-only, ruolo: "solo voci dubbie"}
  E: non_attivato
  V: "da attivare: gpt-5.6-terra ordinario, gpt-6.1-sol per dubbi e G7 (procedura rev. 10, § 5)"
consumi: {}
---

# Scheda scope § 8.7.3

Sola riga 8.7.3, file `cap08/8.7.3-progettazione-interventi-costruzioni-miste.md`, Norma e Circolare. Restano fuori 8.7, 8.7.1, 8.7.2, 8.7.4, 8.7.5, C8.7.4 e seguenti e ogni altro file normativo.

## Storia e autorizzazioni

- Sandro ha autorizzato lo scope il 2026-10-22 alle 07:13 con «Ok allora andiamo con il prossimo. Fallo fare a codex»: VC della riga successiva a 8.7.2, cioè 8.7.3 con C8.7.3, procedura rev. 10, lavoro a Codex sul W520. Alle 07:14 ha chiesto di ridurre al minimo il lavoro di C («cerca di non lavorare troppo, fai lavorare gli altri»).
- Ramo `cdx/vc-8.7.3-261022` creato da origin/main (33f9a3d), worktree `_tmp_render/wt-cdx-vc-8.7.3-261022`.

## G0

Norma pagina fisica 298, da `8.7.3.` a prima di `8.7.4.` (che apre p. 299); pagina condivisa con 8.7.1 e 8.7.2. Circolare pagina fisica 289, da `C8.7.3` a prima di `C8.7.4`; pagina condivisa con C8.7.2 e C8.7.4. Due pagine, sotto la soglia di 15. Le colonne del registro (NTC 298, Circolare 289) coincidono con la fonte: il comando `pagine` non serve. PDF ufficiali in `verifica-conformita/fonte-ufficiale/`, SHA-256 `dda1e397…5a46` (NTC) e `f7c3b8d1…ed7c` (Circolare), ricalcolati il 2026-10-22.

G1: ricognizione piena del 2026-10-13 riusabile (meno di trenta giorni); ricontrollo mirato da registrare prima della chiusura di G1.

Firma: GBOT-verifica-ntc, 2026-10-22.
