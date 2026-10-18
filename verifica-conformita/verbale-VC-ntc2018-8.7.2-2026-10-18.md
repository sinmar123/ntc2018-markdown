# Verbale VC del § 8.7.2 con C8.7.2

Data: 2026-10-18. Procedura VC-NTC/10, SHA-256 `bc54cd41effc1e2aaf3f20f0dd75b99b4a3279df787a2eb35faaec7261b41b22`, copia congelata `vc-ntc2018-8.7.2-2026-10-18/procedura-congelata-r10.md`. Catalogo delle normalizzazioni, voci 1-25, SHA-256 `279267c27d0aa19045045f6110d8cece1f5ec99ebcaaceac3b7f267676372f48`, copia congelata `vc-ntc2018-8.7.2-2026-10-18/catalogo-congelato.md`.

**Esito proposto: VC-OK**, subordinato al giudizio G7 del verificatore, sul solo file [8.7.2-progettazione-interventi-costruzioni-in-calcestruzzo-armato-o-in-acciaio.md](../cap08/8.7.2-progettazione-interventi-costruzioni-in-calcestruzzo-armato-o-in-acciaio.md), snapshot SHA-256 `6b338b8c2610ab51603db0dc9aa140ba6b0a15cbdfc68e0583c0f5626ae3b689`. Fuori dal perimetro: 8.7, 8.7.1, 8.7.3-8.7.5, C8.7.3 e seguenti, il file complessivo `cap08/8-esistenti.md` e ogni altro file normativo.

## Fonte, perimetro e vigenza

D.M. 17 gennaio 2018, § 8.7.2, pagina fisica 298 (stampata 294), da `8.7.2.` a prima di `8.7.3.`; pagina condivisa con 8.7.1 e 8.7.3. Circolare 21 gennaio 2019 n. 7, § C8.7.2 con C8.7.2.1-C8.7.2.4, pagine fisiche 283-289 (stampate 279-285), da `C8.7.2` a prima di `C8.7.3`; 283 condivisa con C8.7.1, 289 con C8.7.3. Otto pagine, sotto la soglia di 15. PDF SHA-256 `dda1e397d56d71aa0f5bc457c3ba9b77064a468699dfc37bd056ac6c47105a46` (NTC) e `f7c3b8d1f443aadb6b3e020b6b6c19813683492ecaadd2c15bf6bf1939aaed7c` (Circolare). Le colonne pagine della riga 8.7.2 nel CSV (NTC 298, Circolare 283-289) coincidono con il perimetro accertato in G0.

Vigenza: ricognizione piena del 2026-10-13, ricontrollo mirato del 2026-10-18 (`g1/ricontrollo-20261018.json`): schede GU dei tre atti senza avvisi nuovi; il D.M. 9 marzo 2023 non tocca il capitolo 8.

## Ruoli effettivi

- C: Grok Bot (GBOT-verifica-ntc), presa del 2026-10-18 autorizzata da Sandro alle 15:45: G0-G4, controllo sulla fonte (livello vettoriale e ritagli fino a 800 dpi), lista per Sandro, applicazione con gli strumenti, G5, pacchetti G6 e del controllo delle modifiche, giudizio dei rilievi per Sandro, worktree e commit.
- Confronto iniziale integrale: Codex sul W520, gpt-5.6-terra, high, read-only, due blocchi (A e B). Primo filtro con il corpus structural-codes, script senza LLM, mai usato come fonte.
- G6 integrale, giro 1: due V Codex gpt-5.6-terra, high, read-only, contesto nuovo per blocco, indipendenti da chi ha scritto la lista.
- Controllo delle modifiche (§ 8): V Codex gpt-5.6-terra, high, read-only, contesto nuovo; continuità con il G6 dichiarata tramite i rapporti conservati.
- G7: Codex gpt-6.1-sol, high, read-only, contesto nuovo, giudizio in `G7.json`.

Natura: verifica svolta da agenti AI; nessuna revisione umana integrale. Sandro ha approvato la lista v1, deciso i dubbi e i sei rilievi del G6. Isolamento reale: cartelle temporanee esterne al workspace e sandbox read-only di Codex, senza `--always-approve`; nessuna sandbox di lettura dimostrata. Nel G6 entrambi i V hanno letto lo SKILL.md del plugin pdf di Codex (caricamento del runtime, nessun dato del corpus) e il V di b02 ha fatto una chiamata Computer Use con risultato vuoto. In sandbox read-only V non può scrivere file: C ha trascritto byte per byte i messaggi finali JSON di V.

## Correzioni prima del G6

Lista v1 approvata per intero da Sandro il 2026-10-18 alle 16:15: 70 voci, 5 sostanziali (S-01 esponente di [C8.7.2.1] senza segno meno; S-02 pedice o sotto [C8.7.2.2]; S-03-S-05 V_W nelle formule [C8.7.2.8]-[C8.7.2.10]) e 65 di forma; dubbi D-01-D-04 decisi a testo invariato. Applicata con `applica-lista` (piano, `--applica`) alle 16:17; il risultato coincide con il target proposto prima dell'approvazione; `verifica-lista` sulla base `61aa496` OK; indici interni rigenerati, corpi invariati (`decisione-applicazione-20261018.json`). Anomalie della fonte conservate: AF-01-AF-06, elencate in `lista-correzioni-c.md` (rinvii senza C, e.Rd/e,Rd, V_W/Vw, b_o/b_0, punto decimale, quadre e tonde). Nessuna nota AF-COR.

## G5 e G6 integrale, giro 1

G5 OK: testo depurato di 353 righe, resa canonica `g5/resa-finale.pdf` di 8 pagine con 14 tag a quadre; due blocchi (`config-g6.json`): b01 NTC 298 e Circolare 283-286, righe 1-205; b02 Circolare 287-289, righe 206-353. G6 giro 1 dalle 16:21 alle 16:36: inventario fonte-prima, `valida-inventario` e `rivela` OK, confronto nello stesso contesto; `valida-g6` schema OK, b01 38 ID coperti e 4 rilievi, b02 28 ID coperti e 2 rilievi; esito KO, 2 `ERR-MD`, 1 `ERR-AUDIT`, 3 `DUBBIO` (`sequenza-g6.json`, `esito-g6.json`).

## Esito dei sei rilievi

Decisione di Sandro del 2026-10-18 alle 16:53 (`decisione-g6-20261018.json`), sul confronto preparato da C:

- COND-C285-DOVE-1 (`ERR-MD`): fondato, voce 18 del catalogo. I blocchi «dove:» dopo [C8.7.2.1], [C8.7.2.8] e [C8.7.2.13] sono resi come elenco puntato, solo con il marcatore, testo invariato; l'estensione agli ultimi due blocchi è di C. L'errore veniva dalla lista v1.
- FORM-287-03 (`ERR-MD`): chiuso senza modifiche per decisione di Sandro. [C8.7.2.8] resta in due righe con il tag sotto: contenuto identico alla fonte, scarto di sola resa, non regolato dal catalogo.
- F-C285-87221 (`DUBBIO`): non fondato; esponente 0.225 positivo nel livello vettoriale e a 600 dpi.
- COND-C285-POST-ALFA (`DUBBIO`): non fondato; lettera o nel vettoriale (PalatinoLinotype-Italic) e a 600 dpi.
- FORM-289-01 (`DUBBIO`): non fondato; e.Rd con il punto nel vettoriale e a 800 dpi.
- C286-87234-FINO (`ERR-AUDIT`): documentale sul pacchetto; la resa data come asset a ogni blocco copre l'intero scope, come in 8.7.1; testo e perimetro del blocco corretti.

## Controllo delle modifiche

Lista g6 di 3 voci (21 righe) applicata con `applica-lista` alle 16:55; indici interni rigenerati, target invariato dagli indici; lint 0 errori; `verifica-lista` della lista v1 più g6 (73 voci) sulla base `61aa496` OK (`correzioni-g6/verifica-lista.json`). Snapshot prima `242f7892…52527`, dopo `6b338b8c…3b689`. `pacchetto-modifiche` sugli stessi blocchi del G6, con nuova resa di 9 pagine SHA-256 `0964c756…63003`; confronto meccanico e osservazione dell'intero documento da parte di C (`correzioni-g6/esito-resa.json`). Nel PDF di confronto C aveva contato 22 righe: sono 21 (9 + 9 + 3), con perimetro e testo invariati.

V gpt-5.6-terra dalle 16:59 alle 17:02: diff OK (solo i 21 marcatori), COND-C285-DOVE-1, EST-C287-DOVE ed EST-C289-DOVE chiusi sui ritagli a 600 dpi, resa delle pp. 4, 5, 7 e 9 OK, nessun nuovo rilievo, esito OK (`g6-modifiche/esito-terra.json`, `g6-modifiche/registro-g6-modifiche.json`). `giro_g6`: 1 su `max_giri` 3; il controllo delle modifiche non è un nuovo giro e il § 8 non prevede un G6 di riscontro. G6: OK, zero `ERR-MD`, zero `ERR-AUDIT`, zero `DUBBIO`.

## Normalizzazioni, limiti e manifest

Normalizzazioni applicate secondo il catalogo, voci 1-25; in questo scope in particolare voci 1, 3, 4, 5, 16, 18, 19, 20, 21 e 23. La resa canonica del controllo delle modifiche include in testa l'indice interno e le righe di navigazione, che la resa G5 non conteneva: non sono testo normativo. Consumi: Codex gpt-5.6-terra, confronto iniziale 149.256 e 164.504 token; G6 b01 276.110 + 1.387.422 token di input (in gran parte in cache), 27.578 di output; G6 b02 258.065 + 615.542 di input, 19.895 di output; controllo delle modifiche 369.881 di input, 3.761 di output. G7 nel giudizio. Nessun costo in valuta esposto.

Il giudizio G7 è `vc-ntc2018-8.7.2-2026-10-18/G7.json`: sta fuori dal manifest perché ne riporta l'impronta. [Manifest](vc-ntc2018-8.7.2-2026-10-18/manifest-rilascio.json). [Scheda](scheda-scope-ntc2018-8.7.2.md). Le pagine PNG e i PDF di prova restano locali secondo `.gitignore`; il manifest ne conserva le impronte.

VC-OK vale per questo snapshot e perimetro.

Prossima azione: Nessuna sul file: VC conclusa sullo snapshot registrato.
