# CLAUDE.md - Progetto NTC 2018

Ingresso per Claude Code. Importa le istruzioni locali comuni:

@AGENTS.md

Per conversione, correzione e verifica usare soltanto [PROCEDURA-VC.md](PROCEDURA-VC.md). Stato e lucchetti si leggono nei file indicati dal suo § 2, non nei prompt storici. Le precauzioni specifiche del corpus sono integrate nei §§ 4 e 6 della procedura, senza un protocollo aggiuntivo per Claude.

Avviare la sessione dalla radice del workspace per caricare le sue impostazioni, skill e strumenti comuni; mantenere il perimetro operativo di questo progetto.

## Sessione cloud (claude.ai/code), dal 2026-10-01

Dal 2026-10-01 questa cartella è anche il repository pubblico `sinmar123/ntc2018-markdown`. Una sessione cloud vede soltanto il repository: niente workspace, skill, giornale, server MCP né strumenti del W520. Regole in più per lei:

- lavora su un ramo e chiude con una pull request; non scrive mai su `main`;
- tocca solo i capitoli assegnati dal prompt, e mai le righe del registro in stato `IN-CORSO`, che sono di un agente locale;
- per le VC vale [PROCEDURA-VC.md](PROCEDURA-VC.md) come per tutti, con l'esecutore dichiarato secondo il § 5 per gli altri runtime: C è la sessione, V un subagente a contesto nuovo con il modello della sessione, mai uno minore; in `agente_vc` si scrive `CC cloud` col modello effettivo;
- se la rete dell'ambiente non raggiunge Normattiva o la Gazzetta, il G1 si ferma e si dice, senza saltarlo;
- i file dei capitoli non portano lo stato di verifica scritto dentro: lo aggiunge il sito al momento della costruzione, perché le VC misurano l'impronta dei file;
- la voce si scrive nel CHANGELOG con firma `CC cloud`; la voce di giornale del workspace la fa il W520 quando riporta il lavoro in locale.
