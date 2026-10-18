## VC-OK del § 8.7.2 con C8.7.2

Verifica di conformità del solo file `cap08/8.7.2-progettazione-interventi-costruzioni-in-calcestruzzo-armato-o-in-acciaio.md` (NTC p. 298, Circolare pp. 283-289), conclusa con G7 `OK` e registrata `VC-OK` il 2026-10-18 secondo la procedura VC-NTC/10. [Verbale](verifica-conformita/verbale-VC-ntc2018-8.7.2-2026-10-18.md).

Ramo `gbot/vc-8.7.2-261018`, basato su `cdx/vc-8.7.1-261017` (856c566, PR #19): da unire dopo la PR #19, oppure da ribasare su `main` quando la #19 sarà unita.

## Commit

1. `61aa496` Presa GBOT e lista v1 delle correzioni (non applicata).
2. `a3bc9a7` Lista v1 approvata e applicata, indici interni, G5.
3. `1e76550` G6 giro 1 KO: evidenze e giudizio di C.
4. `a68750e` Scheda aggiornata dopo il G6 giro 1.
5. `bfe3cfd` Decisione di Sandro sui rilievi G6, blocchi «dove:» come elenco, controllo delle modifiche OK, lotto di chiusura.
6. `d3a1326` G7 tentativo 1 KO per due ERR-AUDIT documentali.
7. `247ccca` Rettifiche documentali (prove di C nel manifest, `manifest_sha256` nel piano).
8. `d5817fe` VC-OK: G7 OK al tentativo 2, registro, file di governo e scheda.
9. Questo testo della PR, fuori dal manifest.

## Cosa cambia

- **Testo 8.7.2**: applicate con `applica-lista` le 70 voci della lista v1 approvata da Sandro il 2026-10-18 alle 16:15 (5 sostanziali: esponente 0.225 di [C8.7.2.1] senza segno meno, pedici b_o e h_o sotto [C8.7.2.2], V_W nelle formule [C8.7.2.8]-[C8.7.2.10]; 65 di forma). Dopo il G6, i tre blocchi «dove:» di [C8.7.2.1], [C8.7.2.8] e [C8.7.2.13] sono diventati elenchi puntati (voce 18 del catalogo, 21 righe, testo invariato). Indici interni rigenerati; nessun altro file normativo toccato.
- **Registro**: riga 8.7.2 `VC-OK`, procedura VC-NTC/10, agente Grok Bot (GBOT); totale 57 `VC-OK`, 0 `IN-CORSO`, 27 `DA-RICONFERMARE`, 9 `DA-RIFARE`, 286 `MAI-FATTA` (379 righe). Lint senza errori (7 avvisi già presenti).
- **Governo**: README, TODO, CHANGELOG, indice, revisione del capitolo 8 e scheda allineati da `vc-supporto.py registra`.

## Chi ha fatto cosa

- GBOT-verifica-ntc (Grok Bot), C: G0-G5, controllo sulla Gazzetta (livello vettoriale e ritagli fino a 800 dpi), lista per Sandro, applicazione con gli strumenti, pacchetti G6 e del controllo delle modifiche, giudizio dei rilievi, rettifiche, verbale e registrazione.
- Codex `gpt-5.6-terra` (high, read-only): confronto iniziale integrale, G6 giro 1 in due blocchi (66 ID, 6 rilievi: 1 corretto, 5 chiusi senza modifiche per decisione di Sandro), controllo delle modifiche (OK).
- Codex `gpt-6.1-sol` (high, read-only, contesto nuovo): G7. Tentativo 1 `KO` per due ERR-AUDIT documentali (PDF delle prove di C fuori dal manifest; impronta del manifest assente dal piano), rettificati su decisione di Sandro delle 18:55; tentativo 2 `OK`. Manifest di 104 file.
- Sandro: approvazione della lista e decisioni sui rilievi (16:15, 16:53, 18:55). Nessuna revisione umana integrale.

## Residui

- [C8.7.2.8] resta su due righe con il tag sotto: scarto di sola resa, deciso da Sandro (la formula su una riga non entra nella pagina).
- Isolamento: sandbox read-only senza `--always-approve`, cartelle temporanee esterne; i V hanno letto istruzioni del runtime (SKILL.md del plugin pdf, AGENTS.md del workspace), dichiarate nel verbale.
- PDF e PNG di prova restano locali secondo `.gitignore`; il manifest ne conserva le impronte.
