## VC-OK del § 8.7.3 con C8.7.3

Verifica di conformità del solo file `cap08/8.7.3-progettazione-interventi-costruzioni-miste.md` (NTC p. 298, Circolare p. 289), conclusa con G7 `OK` e registrata `VC-OK` il 2026-10-23 secondo la procedura VC-NTC/10. [Verbale](verifica-conformita/verbale-VC-ntc2018-8.7.3-2026-10-22.md).

Ramo di lavoro `cdx/vc-8.7.3-261022`. **Nessuna pubblicazione su GitHub in questo passo** (né invio del ramo, né richiesta di unione): i salvataggi restano solo sul computer di Sandro.

## In parole semplici

1. Si è controllato che il testo Markdown del § 8.7.3 coincida con la Gazzetta (pagina NTC 298 e pagina Circolare 289), con immagini delle pagine aperte davvero dal verificatore.
2. Il controllo automatico del G6 (Claude Haiku, una sola sessione) è passato a zero rilievi.
3. Il controllo finale indipendente (G7) è passato al **tentativo 7**, con giudizio OK e nessun rilievo aperto.
4. La riga 8.7.3 del registro è stata segnata **VC-OK**. Non è stato toccato nessun altro paragrafo normativo.

## Nota su DeepSeek (prova)

Il G7 tentativo 7 è stato fatto in **prova** con OpenRouter e il modello `deepseek/deepseek-v4-pro` (firma `OR/DeepSeek/deepseek/deepseek-v4-pro`), su autorizzazione di Sandro del 2026-10-23 («allinea i documenti, poi G7 con DeepSeek»).

- **Non è un cambio stabile di procedura.** Per i prossimi G7 resta predefinito Codex Sol (`gpt-6.1-sol`), come finora.
- Consumi del tentativo 7: circa 560.208 token di lettura + 74.981 di risposta (di cui 70.393 di ragionamento), totale 635.189; costo circa 0,50 USD; 9 passaggi; durata dalle 14:03:50 alle 14:20:13 (ora di Roma).

I tentativi 1–6 con Sol erano andati KO per rilievi documentali (ERR-AUDIT), poi chiusi senza rifare il G6.

## Cosa cambia nei file

- **Testo 8.7.3**: invariato rispetto allo snapshot già giudicato (impronta `1a400982…d4f08`). Nessuna modifica al Markdown normativo in questa chiusura.
- **Registro**: riga 8.7.3 `VC-OK`, data 2026-10-23, procedura VC-NTC/10, agente GBOT. Lint del registro: 0 errori (restano 7 avvisi già presenti su altre righe).
- **Governo**: README, TODO, CHANGELOG, indice, revisione del capitolo 8 e scheda aggiornati da `vc-supporto.py registra`.
- **Dossier**: G7.json (OK), esecuzione e log ripulito del tentativo 7; manifest di 169 file (impronta `5f8f8a0e…0cf9e`); rettifica documentale AUDIT-12/13 (riserve di fase 2 dichiarate; normalizzazione 2 nel verbale). Il log del G7 in corso resta fuori dal manifest giudicato (`log-g7/indice-post-g7.json`).

## Chi ha fatto cosa

- **GBOT-verifica-ntc** (Grok Bot), C: allineamento documenti AUDIT-12/13, lotto di chiusura, G7 di prova via OpenRouter, registrazione VC-OK, questo testo.
- **Claude Code `claude-haiku-5-5`** (HAIKU/CC): G6 giro 2 in sessione unica (`session_id` `8df3e30c-…`), PNG aperti, `valida-g6` 0/0/0.
- **OpenRouter / DeepSeek `deepseek/deepseek-v4-pro`**: G7 tentativo 7 OK (prova).
- **Codex `gpt-6.1-sol`**: G7 tentativi 1–6 KO (rilievi documentali; Sol resta il predefinito).
- **Sandro**: decisione 2026-10-23 «Sì: allinea i documenti, poi G7 con DeepSeek». Nessuna revisione umana integrale del testo.

## Residui

- PDF e PNG di prova restano locali secondo `.gitignore`; il manifest ne conserva le impronte.
- DeepSeek in G7 è solo prova autorizzata; non sostituisce Sol nella procedura.
