# NTC 2018 e Circolare 2019 in Markdown

Trascrizione in Markdown, paragrafo per paragrafo, di due atti:

| Atto | Gazzetta Ufficiale |
|---|---|
| D.M. 17 gennaio 2018, *Aggiornamento delle «Norme tecniche per le costruzioni»* (NTC 2018) | G.U. n. 42 del 20 febbraio 2018, Supplemento ordinario n. 8 |
| Circolare 21 gennaio 2019 n. 7 C.S.LL.PP., *Istruzioni per l'applicazione dell'«Aggiornamento delle Norme tecniche per le costruzioni»* | G.U. n. 35 dell'11 febbraio 2019, Supplemento ordinario n. 5 |

Ogni paragrafo delle NTC sta in un file, con il commento della Circolare che lo riguarda. Formule in LaTeX, tabelle in Markdown, figure ricavate dai PDF.

**Sito per la consultazione:** <https://sinmar123.github.io/ntc2018-markdown/>

## Fa fede soltanto la Gazzetta Ufficiale

Questo non è un testo ufficiale. Fa fede soltanto il testo pubblicato in Gazzetta Ufficiale.

La conversione è stata fatta con strumenti di intelligenza artificiale. La verifica sulla Gazzetta è in corso, paragrafo per paragrafo, e la maggior parte dei paragrafi non è ancora verificata. Un paragrafo non verificato può contenere errori di trascrizione: numeri, formule, celle di tabella, parole. Per un uso professionale si controlla sempre il passo sulla Gazzetta.

## Stato di verifica

Lo stato di ogni paragrafo è nel registro [`registro-verifica-conformita-ntc2018.csv`](../registro-verifica-conformita-ntc2018.csv), colonna `stato_vc`. Nel sito compare in un riquadro in testa a ogni pagina e nella tabella della pagina iniziale.

| Stato nel registro | Nel sito | Che cosa vuol dire |
|---|---|---|
| `VC-OK` | Verificato, con la data | Il testo è stato confrontato con la Gazzetta secondo la procedura di verifica del progetto ([`PROCEDURA-VC.md`](../PROCEDURA-VC.md)). Le evidenze sono in [`verifica-conformita/`](../verifica-conformita/). |
| `DA-RICONFERMARE` | Da riconfermare | Il paragrafo aveva superato la verifica su una versione precedente dei file. Dopo la riorganizzazione dei file la verifica va riconfermata. |
| `DA-RIFARE` | Da rifare | La verifica era stata aperta, ma è stata sospesa, è scaduta o si è chiusa con rilievi. Va rifatta. |
| `IN-CORSO` | In corso | La verifica è aperta e non è conclusa. |
| `MAI-FATTA` | Non ancora verificato | Il testo è stato convertito e non è ancora stato confrontato con la Gazzetta. |
| non presente | Stato non registrato | La pagina non è un paragrafo del registro: indici, raccolte di capitolo, annotazioni. |

Una pagina verificata può comunque contenere un errore sfuggito alla verifica. Se lo trovate, segnalatelo.

## Segnalare un errore

Aprite una segnalazione con il modello [Errore di trascrizione](https://github.com/sinmar123/ntc2018-markdown/issues/new?template=errore-di-trascrizione.yml). Servono quattro dati:

1. il paragrafo;
2. la pagina della Gazzetta;
3. il testo come appare nel repository;
4. il testo come appare in Gazzetta.

Ogni pagina del sito ha in testa il collegamento alla segnalazione. Le correzioni ai capitoli passano dalla procedura di verifica del progetto, quindi non si accettano modifiche dirette ai file dei capitoli con una pull request.

## Organizzazione del repository

- `cap01/` … `cap12/`: i file Markdown dei capitoli, con le figure in `img/` e le note in `annotazioni/`;
- `registro-verifica-conformita-ntc2018.csv`: il registro delle verifiche;
- `verifica-conformita/`: verbali, schede ed evidenze delle verifiche concluse;
- `strumenti/`: script di controllo e di costruzione del sito;
- [`README.md`](../README.md), `TODO.md`, `CHANGELOG.md`: registro interno di lavoro del progetto.

Il sito si costruisce con `python strumenti/costruisci-sito.py` e `mkdocs build --strict -f _sito/mkdocs.yml` (dipendenze in `strumenti/sito/requisiti.txt`). Lo script aggiunge lo stato di verifica solo nella copia in `_sito/`: i file dei capitoli non si modificano, perché le verifiche ne misurano l'impronta SHA-256.

## Licenza

Il testo delle norme è un atto ufficiale ed è escluso dal diritto d'autore (art. 5 L. 633/1941). La conversione è distribuita con licenza [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/deed.it); il codice in `strumenti/` con licenza MIT. Dettagli in [`LICENSE`](../LICENSE) e [`strumenti/LICENSE`](../strumenti/LICENSE).

Autore della conversione: Ing. Alessandro Sanvitale.
