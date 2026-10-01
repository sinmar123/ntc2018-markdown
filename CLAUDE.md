# CLAUDE.md - Progetto NTC 2018

Ingresso per Claude Code. Importa le istruzioni locali comuni:

@AGENTS.md

Per conversione, correzione e verifica usare soltanto [PROCEDURA-VC.md](PROCEDURA-VC.md). Stato e lucchetti si leggono nei file indicati dal suo § 2, non nei prompt storici. Le precauzioni specifiche del corpus sono integrate nei §§ 4 e 6 della procedura, senza un protocollo aggiuntivo per Claude.

Avviare la sessione dalla radice del workspace per caricare le sue impostazioni, skill e strumenti comuni; mantenere il perimetro operativo di questo progetto.

## Sessione cloud (claude.ai/code), dal 2026-10-01

Dal 2026-10-01 questa cartella è anche il repository pubblico `sinmar123/ntc2018-markdown`. Una sessione cloud vede soltanto il repository: niente workspace, skill, giornale, server MCP né strumenti del W520. Regole in più per lei:

- lavora su un ramo e chiude con una pull request; non scrive mai su `main`;
- tocca solo i capitoli assegnati dal prompt, e mai le righe del registro in stato `IN-CORSO`, che sono di un agente locale;
- per le VC vale [PROCEDURA-VC.md](PROCEDURA-VC.md) come per tutti; gli esecutori sono gli «equivalenti documentati» che il suo § 5 chiede per gli altri runtime, nella tabella qui sotto. In `agente_vc` si scrive `CC cloud` col modello effettivo, e i modelli usati per ruolo vanno nella scheda;
- se la rete dell'ambiente non raggiunge Normattiva o la Gazzetta, il G1 si ferma e si dice, senza saltarlo;
- i file dei capitoli non portano lo stato di verifica scritto dentro: lo aggiunge il sito al momento della costruzione, perché le VC misurano l'impronta dei file;
- la voce si scrive nel CHANGELOG con firma `CC cloud`; la voce di giornale del workspace la fa il W520 quando riporta il lavoro in locale.

### Modelli per ruolo nelle VC (sessione su Opus)

La sessione si apre su Opus. I ruoli sono quelli del § 5 della procedura; cambia l'esecutore. Il parametro `model` del tool Agent sceglie il modello del subagente.

| Ruolo o lavoro | Esecutore | Limite |
|---|---|---|
| Meccanica: hash, pacchetti, conteggi, lint, manifest, registri | Script di `strumenti/` | Nessun giudizio normativo |
| Attività breve rigidamente definita e non coperta da script: estrarre pagine, contare, applicare sostituzioni già approvate | Subagente `haiku` | Solo se il risultato lo riconfronta uno script con la fonte o con la lista approvata; senza quel controllo, `sonnet` |
| E: preparazione del fascicolo e correzioni approvate che non si fanno con script | Subagente `sonnet` | Il diff si riconfronta per intero con la lista approvata. Una nuova trascrizione interpretativa di formule, numeri o tabelle la fa un subagente Opus diverso da C |
| C: confini, G0-G5, classificazione e adjudicazione | La sessione, Opus | Non scrive le correzioni che poi coordina nel G6 |
| V: inventario fonte-prima, G6 integrale, G7 | Subagente a contesto nuovo, modello della sessione (Opus) | Mai `haiku` o `sonnet`: il G6 non si degrada |
| Ambiguità persistente, possibile regressione | Ci si ferma e si chiede a Sandro | Il consulente Fable si usa solo se lo chiede lui |

Rileggere il proprio lavoro con lo stesso modello non è un controllo. Il controllo vale quando un output rigenerato viene confrontato con la fonte da uno script, oppure quando c'è una seconda lettura indipendente. Il credito cloud è a tempo: i modelli minori dove la tabella li ammette servono a verificare più paragrafi con la stessa spesa, e nessun gate si alleggerisce per questo.
