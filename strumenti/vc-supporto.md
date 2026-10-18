# Strumenti comuni VC NTC

Specifica tecnica di `vc-supporto.py`, redatta da CDX il 2026-09-05. Il metodo e le decisioni restano esclusivamente in [PROCEDURA-VC.md](../PROCEDURA-VC.md). Gli esiti `integrita: OK` degli script non assegnano `VC-OK`.

## Ambiente e comandi

Compatibilità con VC-NTC/4, 2026-09-12, CDX: `valida-g6` continua a validare il rapporto integrale originale; gli addendum sul controllo delle modifiche sono evidenze richiamate dal giudizio G7 e da `registra`, senza presentarli allo strumento come nuovi confronti integrali. Criteri e sequenza restano nei §§ 8-9 della [procedura unica](../PROCEDURA-VC.md).

Python 3.9 o successivo; PyMuPDF (`fitz`) per preparare i raster e per i test. Gli altri comandi usano la libreria standard. Non installare un altro motore OCR o un altro renderer per eseguire questi strumenti.

```text
python strumenti/vc-supporto.py --help
python strumenti/vc-supporto.py avvio
python strumenti/vc-supporto.py avvio 3.4.4
python strumenti/test_vc_supporto.py
```

`stato` restituisce la sola riga CSV richiesta, senza scrivere o prendere il lucchetto. Uno stato `MAI-FATTA` e la cella `Avviare la VC.` non costituiscono autorizzazione.

`avvio` aggiunge frontmatter e ultima nota della scheda, hash di procedura/target e un solo tratto pertinente di README, TODO e CHANGELOG. Senza scope seleziona esclusivamente l'unico `IN-CORSO`; zero o più candidati restituiscono `NON_UNIVOCA`, senza aprire il successivo. Gli estratti tagliati portano `troncato: true`; integrare solo quanto serve a decidere la ripresa. Non è un nuovo archivio o una prova di lettura integrale.

Per una sezione `x.y` composta da più righe (introduzione, eventuali autonomi e file naturali `x.y.z`), la presa unica usa un JSON con `scope`, `righe`, `agente`, `scheda`, `scheda_contenuto`, `nota` e `prossima_azione`. Dal 2026-09-11 il CSV ha anche i capitoli `x` e le sezioni `x.y`; l'elenco `righe` deve comprenderli quando fanno parte dello scope.

```text
python strumenti/vc-supporto.py prendi PRESA_JSON
python strumenti/vc-supporto.py prendi PRESA_JSON --applica
```

Il piano non scrive. L'applicazione rifiuta righe duplicate, target mancanti, un target condiviso con uno scope `IN-CORSO` o un lucchetto preesistente. Sono ammesse prese autorizzate su file disgiunti, preservando le altre righe. Crea una sola scheda di sezione, porta insieme le righe a `IN-CORSO`, conserva una ricevuta e verifica il registro CSV. Il CSV non si modifica a mano.

Una riga `VC-OK` si prende soltanto per una correzione localizzata del § 8 della procedura, con il campo `riapertura_vc_ok`: oggetto con `motivo` e `autorizzazione` non vuoti, cioè che cosa si corregge e la decisione di Sandro con la data. Senza quel campo le righe `VC-OK` restano rifiutate. Piano e ricevuta riportano le righe riaperte. Aggiunto il 2026-10-13, CC cloud, insieme alla sigla `CCC` (`CC cloud`) fra gli agenti ammessi.

Se E modifica rubriche di righe già `IN-CORSO`, i titoli del CSV si allineano senza patch manuali:

```text
python strumenti/vc-supporto.py sincronizza-titoli CONFIG_JSON
python strumenti/vc-supporto.py sincronizza-titoli CONFIG_JSON --applica
```

Il JSON contiene `scope`, `righe` e `agente`. Il comando controlla il medesimo lucchetto, aggiorna esclusivamente il campo `titolo`, conserva una ricevuta ed esegue il lint.

Se le pagine PDF di una riga `IN-CORSO` risultano errate o incomplete rispetto alla fonte, si correggono con lo strumento:

```text
python strumenti/vc-supporto.py pagine CONFIG_JSON
python strumenti/vc-supporto.py pagine CONFIG_JSON --applica
```

Il JSON contiene `scope`, `agente`, `riga`, una o entrambe le colonne `pagine_pdf_ntc` e `pagine_pdf_circolare`, `motivo`, `autorizzazione` ed `evidenza` (file del repository con l'accertamento sulla fonte). Il comando controlla lo stesso lucchetto, valida i valori con il lint, aggiorna esclusivamente quelle colonne della sola riga indicata, conserva una ricevuta ed esegue il lint. Aggiunto il 2026-10-18, GBOT-verifica-ntc, su decisione di Sandro.

## Composizione del testo dello scope

Dalla revisione 8 della procedura, 2026-10-15, CC cloud. Uno scope con più file si confronta su un testo unico: tutte le parti Norma nell'ordine dei file, poi tutte le parti Circolare, divise alla rubrica `## Circolare`.

```text
python strumenti/vc-supporto.py componi-scope LISTA_FILE_JSON USCITA_MD
```

`LISTA_FILE_JSON` è un array di percorsi relativi alla radice, nell'ordine dei file naturali (lo stesso di `lista-snapshot.json`). Il comando non sovrascrive l'uscita. Il testo così composto è il `target` della configurazione di `prepara`; la stessa lista si ripassa a `pacchetto-modifiche`.

## Confezionamento con rivelazione differita

Il coordinatore prepara una configurazione JSON nella lavorazione dello scope. I percorsi di `target` e `pdf` sono relativi a quel JSON, oppure assoluti. Il target è il file normativo completo del perimetro; il programma usa il depuratore comune `prepara-scope-g6.py` per ricavare le righe del confronto.

| Campo | Contenuto |
|---|---|
| `scope` | Identificativo dello scope autorizzato |
| `target` | Percorso del Markdown sullo snapshot pronto |
| `dpi` | Risoluzione delle pagine intere, predefinita 200; intervallo tecnico 200-1200 |
| `fonti` | Elenco di oggetti con `id`, `pdf`, `sha256`, `pagine` |
| `fonti[].id` | Identificativo breve minuscolo, per esempio `ntc` o `circ` |
| `fonti[].sha256` | Hash atteso della fonte congelata, da confrontare con il ricalcolo, non da inventare |
| `fonti[].pagine` | Numeri fisici 1-based inclusi nello scope, senza duplicati |
| `blocchi` | Elenco ordinato di blocchi primari con `id`, `pagine`, `righe`, `limiti` |
| `blocchi[].pagine` | Chiavi `id-fonte:pagina`, per esempio `ntc:61` |
| `blocchi[].righe` | Intervalli inclusivi 1-based del Markdown **depurato**, compresi gli a capo; ogni intervallo è `[inizio, fine]` |
| `blocchi[].limiti` | Confini neutri ricavati dalla fonte, senza rilievi o conteggi attesi |
| `blocchi[].assets` | Facoltativo: evidenze target da rivelare solo dopo il congelamento, ciascuna con `name` portabile nel blocco, `source` interno al progetto e `sha256` obbligatorio; serve anche per PDF/PNG del render canonico non richiamati dal Markdown |

Ogni pagina deve appartenere a un solo blocco primario; la concatenazione delle righe dei blocchi deve coprire una sola volta e nello stesso ordine l'intero testo depurato. Il programma verifica queste proprietà, ma la correttezza sostanziale della mappa pagina-righe resta a C. Gli asset espliciti non compaiono nel blocco fonte-prima: percorso e hash restano in `coordinamento.json` e i file sono copiati e aggiunti a `input-confronto.json` soltanto da `rivela`, dopo il congelamento. Per misurazioni facoltative con un blocco duplicato, copiare un pacchetto fonte in uno staging separato per il nuovo V; non inserire il duplicato nella copertura primaria.

```text
python strumenti/vc-supporto.py prepara CONFIG_JSON DESTINAZIONE_NUOVA
```

Gli argomenti maiuscoli nei comandi rappresentano i percorsi scelti dal coordinatore. La destinazione non deve esistere. Per il G6 usare una directory temporanea esterna al workspace; l'archiviazione successiva si fa nel dossier dello scope. Il programma crea:

```text
DESTINAZIONE_NUOVA/
  coordinamento.json          dati del coordinatore, mai consegnati a V
  b01/
    PERIMETRO.md
    canone.md
    ISTRUZIONI-V.md             consegna neutra e campi esatti degli output
    fonte-ntc-61.png           una pagina per ciascuna chiave assegnata
    input-fonte.json          hash degli input fonte
```

Il canone deriva dai §§ 3-4 della procedura e dalle voci prescrittive del catalogo, private degli esempi storici. Il generatore si ferma se cambia la struttura del catalogo: il suo adattamento va collaudato, non aggirato. La copia non sostituisce il catalogo originale. Le pagine sono renderizzate direttamente dai PDF di impronta verificata; eventuali ritagli ad alta risoluzione per le decisioni si producono e si conservano secondo la procedura.

Consegnare a V solo la cartella `b01`. `coordinamento.json` contiene percorsi, mappature e impronte del target e resta al coordinatore. `prepara` crea anche `DESTINAZIONE_NUOVA-lavoro/b01/`, la cartella di lavoro di V da indicargli insieme al blocco: ritagli, appunti, script e versioni precedenti dell'inventario vanno lì, mai nel blocco. Il tool non crea una sandbox: i permessi e i confini reali degli strumenti vanno dichiarati secondo la procedura.

V scrive nella propria cartella `inventario.json`, con questi campi:

- `firma`: identificativo effettivo del verificatore;
- `esito_provvisorio`: `LEGGIBILE` o `DUBBIO`, riferito alla fonte;
- `elementi`: elenco non vuoto; ogni elemento ha `id` univoco, `pagina` nel formato assegnato e `riferimento` che localizza titolo, capoverso, formula, tabella/celle, figura, nota o definizione. Può aggiungere `tipo` e note utili;
- `esclusioni`: elenco, anche vuoto, con `pagina` e `riferimento` motivato per le parti esterne allo scope;
- eventuali dubbi sono descritti senza anticipare il contenuto del Markdown.

Lo schema controlla la presenza di tutte le pagine, non la completezza dell'inventario a livello di contenuto: questa è parte della verifica indipendente. C controlla la forma dell'output senza suggerire a V conteggi o letture attese.

```text
python strumenti/vc-supporto.py rivela DESTINAZIONE_NUOVA b01
python strumenti/vc-supporto.py verifica-pacchetto DESTINAZIONE_NUOVA b01
```

`rivela` rifiuta per primo un blocco che contenga file diversi dagli input fonte e da `inventario.json`, prima di qualsiasi scrittura: il messaggio elenca i file da spostare nella cartella di lavoro. Poi ricontrolla fonti, inventario, target e asset; scrive e riapre `congelamento.json` con hash dell'inventario, esito provvisorio e hash del canone/criterio **prima** di creare `testo.md` e gli asset. Infine genera e verifica `input-confronto.json`. Il registro del comando è parte della prova di sequenza; gli hash da soli non attestano l'istante della lettura del modello.

Non rinominare `testo.md` in `scope.md` né creare coppie di nomi distinte solo per maiuscole. I percorsi degli asset restano quelli del Markdown e devono essere relativi, portabili e contenuti nella cartella del target; i casi non supportati causano un errore esplicito. Il generatore non riscrive testo o formule. Il controllo del pacchetto confronta anche l'estratto atteso e l'insieme degli input: un manifest internamente coerente con un file sbagliato non basta.

Nessun file congelato viene sovrascritto. Se un comando si interrompe dopo aver creato parte della destinazione, conservarla come tentativo fallito e preparare una destinazione nuova; non riparare a mano il pacchetto già consegnato. Le rettifiche descrittive successive all'inventario sono documenti di errata separati, non modifiche di `inventario.json`.

Prima di `rivela` eseguire `valida-inventario CARTELLA_BLOCCO`. Legge soltanto gli input fonte e l'inventario del blocco, senza coordinamento o target vivo. Se fallisce per campi mancanti, corregge V nello stesso contesto prima del congelamento, mantenendo separatamente la traccia precedente; il comando non crea una destinazione parziale e non richiede un nuovo pacchetto. I pacchetti della revisione 1 mantengono lo schema storico, senza essere riscritti.

Dopo il confronto, `valida-g6 CARTELLA_BLOCCO RAPPORTO_JSON` controlla il formato compatto: `firma`, `esito` (`OK`/`KO`), `coperti` (ID univoci dell'inventario), `rilievi` (array). `OK` richiede zero rilievi e copertura di tutti gli ID; giudizio sostanziale, normalizzazioni, letture e isolamento restano responsabilità di V secondo la consegna. Lo schema non impone un oggetto ripetitivo per ogni ID già presente nell'inventario.

Per le prove fonte aggiuntive richieste da V, creare una cartella separata **fuori da `b01`** e dagli altri blocchi, con soli file fonte, provenienza (PDF e hash, pagina/area, dpi o risoluzione nativa) e manifest esplicito generato col comando sotto. Consegnare a V solo quei file e registrare la sequenza nel rapporto. Non aggiungerli ai manifest già congelati e non consegnare la cartella del coordinatore. Includere queste integrazioni nel manifest finale se effettivamente usate. Lo strumento verifica l'integrità dei file; l'assenza di indicazioni suggestive e la correttezza del ritaglio restano controlli del coordinatore.

## Controllo delle modifiche e liste di correzioni

```text
python strumenti/vc-supporto.py applica-lista LISTA_JSON
python strumenti/vc-supporto.py applica-lista LISTA_JSON --applica
python strumenti/vc-supporto.py verifica-lista LISTA_JSON BASE
python strumenti/vc-supporto.py pacchetto-modifiche CARTELLA_G6 LISTA_FILE_JSON NUOVA [--resa]
```

La lista è un array di voci, oppure un oggetto con `gruppi[].voci[]`. Ogni voce ha `id` univoco, `file` relativo alla radice, `attuale` e `proposto`; pagina, classe e nota sono campi descrittivi. Le voci si applicano nell'ordine, ciascuna sul risultato delle precedenti, e `attuale` deve comparire una sola volta nel file in quel momento: altrimenti il comando si ferma senza scrivere. Senza `--applica` restituisce solo il piano.

`verifica-lista` riapplica la lista ai file della revisione git `BASE` (per esempio il commit consegnato al G6) e confronta il risultato con i file vivi, escludendo i blocchi `INDICE-INTERNO` rigenerati da `genera-indici-interni.py`. Esito `OK` o errore con i file diversi; elenca anche i file della lista cambiati dalla base.

`pacchetto-modifiche` legge `coordinamento.json` e i `testo.md` dei blocchi del G6 già rivelati, controlla che ricompongano il testo depurato congelato, compone il testo dopo le correzioni con `componi-scope`, lo depura e lo divide negli stessi blocchi. I confini si riportano sulle righe con testo e, dentro una zona cambiata, sulle lettere, che le correzioni di forma conservano. Per ogni blocco scrive `testo-dopo.md` e `diff-testo.txt` (diff unificato rispetto a `testo.md`); in radice `target-scope-dopo.md`, `testo-dopo.md` e `riepilogo.json`. Con `--resa` produce `resa-dopo.pdf` con `render-capitolo.py`, attraverso un file temporaneo accanto al primo file della lista, poi cancellato. Le rese PDF non sono riproducibili byte per byte: ogni resa citata da un'evidenza va nel manifest.

## Candidati di struttura dal PDF

```text
python strumenti/vc-struttura-fonte.py --pdf FONTE.pdf --pagine 257-269 --inizio REGEX --fine REGEX \
    --target "cap08/8.5*.md" [--senza-tabelle 265] --uscita candidati.json
```

Legge dalla codifica del PDF le righe del perimetro, tabelle escluse, ricostruisce i capoversi (interlinea, rientro, righe corte) e i tratti in grassetto, corsivo e grassetto corsivo. Restituisce gli inizi di capoverso che nel target stanno a metà paragrafo e i tratti in enfasi senza marcatori nel target. Sono candidati per C: righe rientrate di elenco, simboli in grassetto e testo diviso dalla codifica danno falsi positivi. `--senza-tabelle` disattiva il riconoscimento delle tabelle sulle pagine dove scambia un capoverso per una griglia. Sul § 8.5 prima delle correzioni ha dato 87 candidati di capoverso per 86 voci approvate; dopo, uno solo, falso.

## Manifest di rilascio

La lista JSON è un array di percorsi relativi alla radice dichiarata, selezionati secondo il § 9 della procedura. Non passare una cartella da includere ricorsivamente. Copiare prima nel dossier definitivo le evidenze accettate prodotte nello staging esterno e le versioni di procedura/catalogo effettivamente usate; non perdere i rapporti originari o gli scarti da conservare.

```text
python strumenti/vc-supporto.py manifest RADICE LISTA_JSON MANIFEST_NUOVO_JSON
python strumenti/vc-supporto.py verifica-manifest RADICE MANIFEST_NUOVO_JSON
```

Il manifest JSON contiene versione e record `path`, `bytes`, `sha256`; viene riletto e confrontato con i file prima del riepilogo. Rifiuta file mancanti, percorsi esterni, duplicati anche senza distinzione di maiuscole, inclusione di sé stesso e sovrascrittura di manifest esistenti. Il formato vale per le nuove verifiche; i precedenti manifest TXT restano immutati con i relativi verbali.

Importare il riepilogo nel verbale e aggiungere il giudizio G7 del verificatore. Non ricopiare manualmente hash storici o assegnare `VC-OK` sulla sola esecuzione dello script.

Nei nuovi manifest selezionare le copie congelate di procedura e catalogo. Per un manifest storico che contiene anche i percorsi vivi, `verifica-manifest RADICE MANIFEST --congelati` può risolvere soltanto `PROCEDURA-VC.md` e `verifica-conformita/normalizzazioni-dichiarate-NTC2018.md` mediante una copia con nome contenente `congelat`, già elencata nello stesso manifest e con identici byte e SHA-256. L'output elenca ogni sostituzione; nessun manifest viene modificato e nessuna fonte normativa, asset o target può essere sostituito. Senza l'opzione il controllo resta strettamente sui percorsi originari.

## Registrazioni dopo G7

```text
python strumenti/vc-supporto.py registra CHIUSURA_JSON
python strumenti/vc-supporto.py registra CHIUSURA_JSON --applica
```

Il primo comando restituisce il piano senza scrivere; il secondo applica solo sostituzioni esatte e copia nei registri il giudizio già emesso da V. C controlla il piano e l'effettiva indipendenza, che non è dimostrata dallo schema JSON. Non riscrivere uno script per ogni scope.

Il rapporto G7 usato dai nuovi scope ha i campi: `firma`, `giudizio_g7: "OK"`, `scope` (stringa), `snapshot_sha256`, `manifest_sha256`, `gate` (mappa `G0`-`G7` a stringhe `OK`), `rilievi_aperti: []`. Il giudizio, le motivazioni necessarie e i limiti sono redatti dal V critico, mai generati da uno script. I rapporti storici di altro formato restano immutati e non si adattano automaticamente per promuovere uno stato.

Campi di CHIUSURA_JSON, tutti forniti una sola volta da C:

| Campo | Contenuto |
|---|---|
| `scope`, `agente`, `data` | Scope autorizzato, titolare del lucchetto, data ISO |
| `righe` | Per uno scope aggregato, elenco completo delle righe naturali da chiudere insieme; si omette nel caso singolo |
| `g7`, `g7_sha256` | Percorso relativo e impronta del rapporto giudicato |
| `manifest` | Manifest relativo, la cui impronta deve coincidere con G7 |
| `snapshot_manifest`, `snapshot_sha256` | Per uno scope aggregato, manifest dei target e asset vivi e sua impronta, coincidente con `snapshot_sha256` di G7 |
| `verbale`, `verbale_sha256` | Verbale completo già preparato, da lasciare invariato |
| `nota`, `prossima_azione` | Testi completi riutilizzati nelle registrazioni |
| `procedura_vc` | Etichetta coerente con la revisione della scheda; per VC-NTC/4 e VC-NTC/5 il valore ordinario aggiunge ` - semplificata` alla revisione della scheda |
| `agenti_vc_da_schede` | Facoltativo: mappa ID riga/sigla per attribuzioni pregresse esplicite, riscontrate nelle rispettive schede; non cambia stato o procedura |
| `modifiche` | Un oggetto `path`, `prima`, `dopo` per ciascun file di governo |
| `master` | Se pertinente: `id`, mappa `attesi` e mappa `valori` con gli stessi campi; soltanto righe del progetto |
| `master_non_pertinente` | In alternativa al precedente, motivazione esplicita |

In `dopo` si possono usare `{{scope}}`, `{{data}}`, `{{nota}}`, `{{prossima_azione}}`, `{{verbale}}`: il testo finale non deve avere segnaposto residui. Le modifiche coprono README, TODO, CHANGELOG, indice generale, scheda dello scope e file di revisione del capitolo. Il titolo del CSV si ricava dal Markdown con la stessa funzione del linter.

Prima di scrivere si verificano G7, tutti i gate, assenza di rilievi, impronte di manifest/target/verbale, stato `IN-CORSO`, titolare e snapshot della scheda e tutte le occorrenze dei testi attesi. Non sono consentite modifiche agli input del manifest, al target, al rapporto G7 o al verbale. Ogni file si ricontrolla immediatamente prima della sostituzione; non esiste una transazione filesystem fra più file. La ricevuta `CHIUSURA.eseguito.json` conserva fase e impronte prima/dopo anche se un controllo fallisce: ispezionare lo stato parziale, non rilanciare alla cieca. Su successo si esegue il linter del CSV. Il giornale resta al comando esistente `diario/nuova-voce.py`, una sola volta, con gli stessi `nota` e `prossima_azione`.

## Consumi

Dal 2026-09-12 il registro prevede anche `procedura_vc` e `agente_vc`. `registra` aggiunge le colonne mancanti, attribuisce l'agente titolare allo scope chiuso e lascia vuote le attribuzioni storiche non riscontrate. `agente_vc` indica l'assistente responsabile, distinto dal modello dei ruoli. Il linter accetta anche i precedenti schemi a undici e dodici colonne. Dal 2026-09-12 la revisione 5 usa esclusivamente CSV; il generatore XLSX è fuori dal flusso operativo. Firma: CDX.

```text
python strumenti/vc-supporto.py consumi CARTELLA_LOG --contiene _343
```

Il comando legge metadati e contatori dei file JSONL direttamente contenuti nella cartella, selezionando le sessioni figlie il cui nome di ruolo contiene il filtro. Non stampa conversazioni, segreti, chiavi o contenuti degli input. Esclude i coordinatori per evitare di mescolare uno storico che può comprendere più scope. Usa l'ultimo totale valido di ogni sessione; cache e ragionamento sono sottoinsiemi, non voci da sommare nuovamente.

Si ferma se un contatore decresce, se una sessione è duplicata o cambia modello: in questi casi non produce un totale apparentemente affidabile. I numeri non sono la fatturazione né la quota Codex. Per altri runtime riportare la loro metrica esposta, oppure `non disponibile`, senza stimarla dai caratteri o dai prezzi API.

## Verifica dello strumento

I test creano PDF e dati sintetici in una directory temporanea isolata e la rimuovono alla fine. Coprono rivelazione differita, congelamento, hash, collisioni Windows, lacune/sovrapposizioni, target errato anche con manifest ricalcolato, asset, integrità degli input e contatori cumulativi. Nessun test modifica un file normativo o esegue una VC su contenuti reali.
