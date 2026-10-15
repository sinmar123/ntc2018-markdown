# CLAUDE.md - Progetto NTC 2018

Ingresso per Claude Code. Importa le istruzioni locali comuni:

@AGENTS.md

Per conversione, correzione e verifica usare soltanto [PROCEDURA-VC.md](PROCEDURA-VC.md). Stato e lucchetti si leggono nei file indicati dal suo § 2, non nei prompt storici. Le precauzioni specifiche del corpus sono integrate nei §§ 4 e 6 della procedura, senza un protocollo aggiuntivo per Claude.

Avviare la sessione dalla radice del workspace per caricare le sue impostazioni, skill e strumenti comuni; mantenere il perimetro operativo di questo progetto.

## Sessione cloud (claude.ai/code), dal 2026-10-01

Dal 2026-10-01 questa cartella è il repository pubblico `sinmar123/ntc2018-markdown`. Dal 2026-10-13, per scelta di Sandro, **GitHub è la copia principale e il lavoro si fa dalle sessioni cloud**; il W520 non è più necessario. Una sessione cloud vede soltanto il repository: niente workspace, skill, giornale né server MCP del W520. Regole in più per lei:

- lavora su un ramo e chiude con una pull request; non scrive mai su `main`. Dal 2026-10-14, per decisione di Sandro, la sessione unisce da sé le proprie pull request con un merge commit, appena il job «costruisci» è verde sull'ultimo commit e non ci sono conflitti, e poi gli manda il riepilogo. Le scelte di metodo e le liste di correzioni della VC si chiedono comunque a Sandro prima;
- tocca solo i capitoli assegnati dal prompt, e mai le righe del registro in stato `IN-CORSO` di un altro agente: per subentrare serve un ordine esplicito di Sandro;
- per le VC vale [PROCEDURA-VC.md](PROCEDURA-VC.md) come per tutti; gli esecutori sono i profili della sessione cloud del suo § 5, dalla revisione 8. Nelle schede e nei comandi di `vc-supporto.py` l'agente è `CCC`, che nel registro diventa `CC cloud`; i modelli usati per ruolo vanno nella scheda;
- un paragrafo `VC-OK` si riapre solo per una correzione localizzata approvata da Sandro, con `prendi` e il campo `riapertura_vc_ok` (vedi `strumenti/vc-supporto.md`);
- la rete dell'ambiente «Default» ammette Gazzetta Ufficiale, Normattiva, `cdn.jsdelivr.net` e, dal 2026-10-14, il sito pubblicato `sinmar123.github.io`, oltre ai gestori di pacchetti. Dopo ogni pubblicazione la sessione controlla da sé le pagine cambiate. Se un sito necessario non risponde, il G1 si ferma e si dice, senza saltarlo;
- all'avvio della sessione `.claude/settings.json` installa da solo MkDocs e PyMuPDF (`strumenti/sito/requisiti.txt`, `strumenti/requisiti-vc.txt`), così girano costruzione del sito, lint e test di `vc-supporto.py`;
- i file dei capitoli non portano lo stato di verifica scritto dentro: lo aggiunge il sito al momento della costruzione, perché le VC misurano l'impronta dei file;
- la voce si scrive nel CHANGELOG con firma `CC cloud`, e il CHANGELOG fa anche da giornale: il giornale del workspace (`diario/nuova-voce.py`) e il registro generale fuori dal repository (`../_registro-verifica-conformita.csv`) non sono raggiungibili, quindi nelle registrazioni il master si dichiara non pertinente;
- le operazioni che la sessione non può fare da sé (impostazioni del repository, controlli del sito se `sinmar123.github.io` non risponde) si danno a Sandro come prompt pronto per Claude su Chrome. Le impostazioni di sicurezza dell'ambiente cloud, come la rete, Claude su Chrome non le cambia: Sandro le fa a mano, con Chrome che lo guida e poi controlla.

### Modelli per ruolo nelle VC (sessione su Opus)

La sessione si apre su Opus. Ruoli, modelli dei subagenti e limiti sono nel § 5 di [PROCEDURA-VC.md](PROCEDURA-VC.md), profili della sessione cloud, dalla revisione 8; il parametro `model` del tool Agent sceglie il modello del subagente. In breve: script per la meccanica, `haiku` o `sonnet` solo per lavori senza giudizio normativo e riconfrontati, Opus per C e per V, mai un modello leggero nel G6.

Rileggere il proprio lavoro con lo stesso modello non è un controllo. Il controllo vale quando un output rigenerato viene confrontato con la fonte da uno script, oppure quando c'è una seconda lettura indipendente. Il credito cloud è a tempo: i modelli minori dove la procedura li ammette servono a verificare più paragrafi con la stessa spesa, e nessun gate si alleggerisce per questo.
