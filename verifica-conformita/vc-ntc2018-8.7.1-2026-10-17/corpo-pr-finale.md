## VC-OK del § 8.7.1 con C8.7.1

Verifica di conformità del solo file `cap08/8.7.1-progettazione-interventi-costruzioni-in-muratura.md` (NTC pp. 297-298, Circolare pp. 270-283), conclusa con G7 `OK` e registrata `VC-OK` il 2026-10-18. [Verbale](verifica-conformita/verbale-VC-ntc2018-8.7.1-2026-10-18.md).

## Commit

1. `5dfa139` Resa: rubriche di livello 4-5 su riga propria e note `[^n]` (voce 25 del catalogo).
2. `0fbf890` `vc-supporto.py`: comando `pagine` per le colonne pagine PDF del registro.
3. `18b135a` VC-OK § 8.7.1 con C8.7.1: testo, dossier, verbale, scheda e registro.
4. `614afe6` PROCEDURA-VC revisione 10.

## Cosa cambia

- **Testo 8.7.1**: applicate via script le 206 voci della lista v3 approvata da Sandro il 2026-10-17 (21 sostanziali, 185 di forma) e le 4 correzioni dopo il G6: due rubriche di sesto livello in corsivo (C8.7.1.3.1.1 e C8.7.1.3.1.2) e la nota 4 della Circolare come nota Markdown `[^4]`. Indici interni rigenerati; nessun altro file normativo toccato.
- **Resa**: `render-capitolo.py` usa `-V block-headings`, così le rubriche di livello 4 e 5 escono su riga propria come nella Gazzetta; il PDF stampa per le note lo stesso numero della fonte. Nuova voce 25 del catalogo: note a piè di pagina come `[^n]`, senza la parola «Nota».
- **Comando `pagine`**: corregge le sole colonne pagine di una riga `IN-CORSO`, con piano, `--applica`, lucchetto, ricevuta e lint. Primo uso sulla riga 8.7.1.
- **Registro**: riga 8.7.1 `VC-OK`; totale 56 `VC-OK`, 0 `IN-CORSO`. Lint senza errori.
- **Procedura, revisione 10**: V ordinario Codex `gpt-5.6-terra`, `gpt-6.1-sol` per punti dubbi e G7, Luna non per V; scelta dei modelli aperta alle prove di Sandro, registrate nel dossier; Antigravity non lanciato da agenti, usabile da Sandro sul W520; note `[^n]` al § 4. La VC del § 8.7.1 è stata svolta con la revisione 9.

## Chi ha fatto cosa

- GBOT-verifica-ntc (Grok Bot): G0-G4, liste di correzioni, giudizio dei 14 rilievi del G6 per Sandro, correzioni dopo il G6, renderer e resa.
- CDX (Codex): applicazione della lista v3, G5 e G6 integrale giro 1 (180/180 ID, 14 rilievi).
- Controllo delle modifiche e G7: Codex `gpt-6.1-sol`, in deroga al profilo V decisa da Sandro il 2026-10-18. Prove comparative di Sandro: `gpt-6-luna` (un rilievo non fondato) e `gpt-5.6-terra` (esito OK).
- G7 tentativo 1 `KO` per le sole pagine incomplete della riga nel registro; corrette con il comando `pagine`, G7 tentativo 2 `OK`. `giro_g6` 1 su 3. Manifest di 174 file.

## Residui

- GitHub rinumera le note: la nota `[^4]` può comparire come «1»; il PDF canonico stampa 4.
- Da riallineare alla voce 25, su autorizzazione: note di 8.2, 8.4, 8.5.4 e del file complessivo `8-esistenti.md` (nel TODO).
- Il file vivo 8.7.1 non si rende direttamente per la profondità dell'indice interno; la resa canonica è quella del testo depurato.
