# Prompt per la sessione cloud: il sito pubblico della conversione NTC 2018

Da incollare in una sessione cloud di Claude Code (claude.ai/code) sul repository `sinmar123/ntc2018-markdown`, dopo che il W520 lo ha creato (`PROMPT-IN-CORSO-ntc2018-repository-pubblico.md`). Preparato da CC il 2026-10-01.

---

Lavori sul repository della conversione in Markdown delle NTC 2018 (D.M. 17/01/2018, G.U. n. 42 del 20/02/2018, S.O. n. 8) e della Circolare 21/01/2019 n. 7 C.S.LL.PP. (G.U. n. 35 dell'11/02/2019, S.O. n. 5). Leggi prima `CLAUDE.md`, sezione «Sessione cloud», poi `README.md` § «Struttura» e l'intestazione di `registro-verifica-conformita-ntc2018.csv` (separatore `;`, BOM UTF-8; colonne usate qui: `paragrafo`, `titolo`, `n.`, `apri_md`, `stato_vc`, `data_ultima_vc`).

Il progetto diventa pubblico per scelta dell'autore, l'Ing. Alessandro Sanvitale: **si pubblica tutto, ciascun paragrafo con il suo stato di verifica in vista**. Al 2026-10-01 il registro ha 379 righe: 43 `VC-OK`, 289 `MAI-FATTA`, 34 `DA-RICONFERMARE`, 9 `DA-RIFARE`, 4 `IN-CORSO`. Ricontali dal file: valgono quelli.

## Che cosa costruire, su un ramo, con una pull request

1. **Sito su GitHub Pages** con MkDocs Material, costruito da una GitHub Action a ogni push su `main`:
   - uno script `strumenti/costruisci-sito.py` copia `cap*/` (con le cartelle `img/`) in `_sito/docs/` e lì, **solo nella copia**, aggiunge in testa a ogni pagina un riquadro con lo stato di verifica letto dal registro tramite `apri_md`: verificato (con la data), da riconfermare, da rifare, in corso, non ancora verificato. Le pagine che non compaiono nel registro portano «stato non registrato». **I file di `cap*/` non si modificano mai**: le verifiche misurano la loro impronta SHA-256;
   - la pagina iniziale si genera dal registro (capitoli, paragrafi in ordine di `n.`, stato di ciascuno, conteggi per stato), non da `indice-ntc2018.md`, che rimanda a cartelle escluse dal repository;
   - formule: `$...$` e `$$...$$` con `pymdownx.arithmatex` e MathJax; le macro di `_preambolo-tag.tex` vanno nella configurazione di MathJax;
   - lingua dell'interfaccia italiana, ricerca attiva.
2. **`.github/README.md`**, la pagina che GitHub mostra al posto del `README.md` di radice, che resta il registro interno di lavoro e non si tocca. Contenuto: che cos'è; gli atti con i loro estremi in Gazzetta e il collegamento al sito; **fa fede soltanto il testo pubblicato in Gazzetta Ufficiale**; la conversione è stata fatta con strumenti di intelligenza artificiale e la verifica è in corso, quindi un paragrafo non verificato può contenere errori di trascrizione; che cosa vuol dire ciascuno stato; come segnalare un errore; licenza. Niente toni promozionali.
3. **Licenze**: `LICENSE` con CC BY 4.0 per la conversione (testi, tabelle, figure ricavate), con la nota che il testo delle norme, come atto ufficiale, è escluso dal diritto d'autore (art. 5 L. 633/1941); `strumenti/LICENSE` con MIT per il codice.
4. **Modello di segnalazione** in `.github/ISSUE_TEMPLATE/errore-di-trascrizione.yml`: paragrafo, pagina della Gazzetta, testo come appare nel repository, testo come appare in Gazzetta.

## Regole di scrittura

Italiano corretto con gli accenti (è, à, perché), niente trattino lungo come inciso, frasi brevi e concrete, nessun aggettivo di lancio. Codice, identificatori e messaggi d'errore restano come sono.

## Controlli prima della pull request

Esegui e riporta gli esiti, con i numeri:

- `mkdocs build --strict` senza errori;
- pagine generate = file `.md` di `cap*/`;
- riquadri per stato = conteggi del registro;
- nessuna immagine rotta: ogni `![...](img/...)` trova il suo file;
- `git diff --stat main -- 'cap*/'` vuoto: i capitoli non sono stati toccati;
- tre pagine con formule aperte e controllate nell'HTML generato (che arithmatex le abbia avvolte).

I collegamenti rotti che stanno **dentro** i capitoli non si correggono qui: si elencano nella pull request, perché ogni modifica ai capitoli passa dalla procedura VC.

## Referto finale

Nella pull request e in una voce in cima a `CHANGELOG.md` firmata `CC cloud`: file creati, esiti dei controlli, che cosa non hai potuto verificare (per esempio la pubblicazione vera su Pages, che parte solo dopo l'unione in `main` e con Pages attivo nelle impostazioni del repository). Non unire tu la pull request.
