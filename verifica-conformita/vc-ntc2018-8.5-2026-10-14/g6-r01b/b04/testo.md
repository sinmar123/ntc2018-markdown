#### C8.5.4.1. Costruzioni di muratura

Nel caso in cui la muratura in esame possa essere ricondotta alle tipologie murarie presenti nelle Tabelle C8.5.I e C8.5.II, i valori medi dei parametri meccanici da utilizzare per le verifiche possono essere definiti, con riferimento alla tipologia muraria in considerazione per i diversi livelli di conoscenza, come segue:

**LC1:**

- Resistenze: i valori minimi degli intervalli riportati in Tabella C8.5.I.

- Moduli elastici: i valori medi degli intervalli riportati nella tabella suddetta.

**LC2:**

- Resistenze: i valori medi degli intervalli riportati in Tabella C8.5.I

- Moduli elastici: i valori medi degli intervalli riportati nella tabella suddetta.

**LC3:**

- I valori delle resistenze e dei moduli elastici riportati in Tabella C.8.5.I individuano una distribuzione a-priori che può essere aggiornata sulla base dei risultati delle misure eseguite in sito. Considerato il generico parametro X, una stima dei parametri μ’ e σ’ della distribuzione a-priori può essere dedotta dai valori minimo e massimo in tabella, con le formule seguenti:

$$
\mu' = \frac{1}{2}\left(X_{\min}+X_{\max}\right)
\tag{C8.5.4.1}
$$

$$
\sigma' = \frac{1}{2}\left(X_{\max}-X_{\min}\right)
\tag{C8.5.4.2}
$$

Eseguito un numero n di prove dirette, l’aggiornamento del valore medio può essere effettuato come segue:

$$
\mu'' = \frac{n\overline{X}+\kappa\mu'}{n+\kappa}
\tag{C8.5.4.3}
$$

dove X̄ è la media delle n prove dirette e κ è un coefficiente che tiene conto del rapporto tra la dispersione (varianza) della stima effettuata attraverso le prove (combinazione tra incertezza della misurazione sperimentale e dispersione dei parametri meccanici nell’ambito dell’edificio che si sta analizzando) e la varianza σ’² della distribuzione a-priori. Nel determinare la stima aggiornata del valore medio del parametro meccanico, il coefficiente κ rappresenta il peso relativo della distribuzione a-priori (associata ai parametri della tabella C.8.5.I) rispetto alle prove sperimentali[3]. Qualora la media delle n prove dirette X̄ sia significativamente diversa dal valore μ’ adottato per la distribuzione a-priori, e quindi la differenza tra μ’ e μ” risulti rilevante, l’accettabilità del risultato ottenuto applicando l’equazione C8..5.4.3 deve essere adeguatamente motivata.

**Nota 3.** Dalla formula emerge che, al crescere del numero di prove, il peso attribuito alla misura sperimentale aumenta, in quanto anche in presenza di una significativa dispersione del parametro nell’edificio la stima del suo valore medio risulta più attendibile. Nella scelta del coefficiente κ è opportuno considerare che l’incertezza legata al metodo di misura sperimentale non si riduce aumentando il numero di prove. Inoltre, l’attendibilità dei diversi metodi di prova cambia in relazione alle diverse tipologie murarie. In assenza di valutazioni specifiche da parte del progettista, la Tabella C.8.5.III suggerisce valori del coefficiente κ per i più diffusi metodi di indagine diretta in sito. Particolare cautela dovrà essere utilizzata nel caso di prove in laboratorio su campioni di muratura estratti in situ, a causa delle difficoltà nell’estrarre, movimentare e trasportare i provini senza arrecare loro danni.

**Tabella C.8.5.III** - *Valori del coefficiente $\kappa$ suggeriti per l'aggiornamento del valore medio dei parametri meccanici, secondo l'equazione [C8.5.4.3], con riferimento ai più diffusi metodi di indagine diretta sulle proprietà meccaniche della muratura.*

| Metodo di prova | Parametro | $\kappa$ |
|---|:---:|:---:|
| Prova di compressione diretta (su una porzione di parete muraria) | $E$ | 1,5 |
| Prova di compressione diretta (su una porzione di parete muraria) | $f$ | 1 |
| Martinetto piatto doppio | $E$ | 1,5 |
| Martinetto piatto doppio | $f$ (*) | 2 (*) |
| Prova di compressione e taglio (su un pannello isolato nella parete muraria) - prova tipo Sheppard | $G$ | 1,5 |
| Prova di compressione e taglio (su un pannello isolato nella parete muraria) - prova tipo Sheppard | $\tau_0 - f_{v0}$ | 1 |
| Prova di compressione diagonale | $G$ | 1,5 |
| Prova di compressione diagonale | $\tau_0$ | 1 |
| Prova di taglio diretto sul giunto | $f_{v0}$ | 2 |
| Prove in laboratorio sui costituenti (**) | $f_b$, $f_m$, $f_g$ | 2 |

(*) La prova con il martinetto piatto doppio consente di ottenere una misura del modulo elastico $E$ della muratura, molto più raramente di misurarne direttamente la resistenza a compressione. Il coefficiente in tabella è quello suggerito quando nella prova viene misurata direttamente la resistenza a compressione. Ricordando che esiste una correlazione empirica approssimata di proporzionalità tra modulo $E$ e la resistenza media a compressione della muratura (desumibile dagli intervalli di variazione dei due parametri nella tabella C.8.5.I) il modulo $E$ ottenuto dalla prova con martinetto piatto può fornire una stima indiretta di $f$ utilizzabile nell'equazione [C8.5.4.3] purché si adotti un valore di $\tau$ almeno pari a 3.

(**) Nel caso di muratura in blocchi di pietra squadrati o artificiali pieni o semipieni si ipotizza che, con prove a compressione diretta sugli elementi e sulla malta (i costituenti), si possa stimare la resistenza caratteristica a compressione della muratura $f_k$ tramite i metodi descritti al § 11.10.3.1.2 delle Norme. Nota: $f_k$, la resistenza a compressione media $f$ della muratura potrà essere quindi stimata come $f = 1{,}25 f_k$.

#### C8.5.4.2. Costruzioni di calcestruzzo armato o di acciaio

I fattori di confidenza, determinati in funzione del livello di conoscenza acquisito, vengono applicati ai valori medi delle resistenze dei materiali ottenuti dai campioni di prove distruttive e non distruttive, per fornire una stima dei valori medi delle resistenze dei materiali della struttura, entro l’intervallo di confidenza considerato (in genere si assume un intervallo di confidenza pari al 95%). Per determinare i fattori di confidenza per i diversi elementi strutturali o loro insiemi si deve tener conto che essi includono, oltre alle incertezze nella stima della resistenza dei materiali, anche le incertezze relative all’individuazione dei dettagli costruttivi. Il livello di conoscenza acquisito in base ai rilievi, alle indagini sui dettagli strutturali e alle prove sui materiali, determina i valori dei fattori di confidenza da applicare alle proprietà dei materiali, anche in maniera differenziata per elementi strutturali o gruppi di elementi, e suggerisce il metodo di analisi più appropriato. In assenza di valutazioni specifiche, ci si può riferire alla Tabella C8.5.IV.

**Tabella C8.5.IV** - *Livelli di conoscenza in funzione dell'informazione disponibile e conseguenti metodi di analisi ammessi e valori dei fattori di confidenza, per edifici in calcestruzzo armato o in acciaio*

| Livello di conoscenza | Geometrie (carpenterie) | Dettagli strutturali | Proprietà dei materiali | Metodi di analisi | FC (*) |
|---|---|---|---|---|:---:|
| **LC1** | Da disegni di carpenteria originali con rilievo visivo a campione; in alternativa rilievo completo ex-novo | Progetto simulato in accordo alle norme dell'epoca e ***indagini limitate*** in situ | Valori usuali per la pratica costruttiva dell'epoca e ***prove limitate*** in situ | Analisi lineare statica o dinamica | 1,35 |
| **LC2** | Da disegni di carpenteria originali con rilievo visivo a campione; in alternativa rilievo completo ex-novo | Elaborati progettuali incompleti con ***indagini limitate*** in situ; in alternativa ***indagini estese*** in situ | Dalle specifiche originali di progetto o dai certificati di prova originali, con ***prove limitate*** in situ; in alternativa da ***prove estese*** in situ | Tutti | 1,20 |
| **LC3** | Da disegni di carpenteria originali con rilievo visivo a campione; in alternativa rilievo completo ex-novo | Elaborati progettuali completi con ***indagini limitate*** in situ; in alternativa ***indagini esaustive*** in situ | Dai certificati di prova originali o dalle specifiche originali di progetto, con ***prove estese*** in situ; in alternativa da ***prove esaustive*** in situ | Tutti | 1,00 |

(*) A meno delle ulteriori precisazioni già fornite nel § C8.5.4.

La quantità e il tipo di informazioni richieste per conseguire uno dei tre livelli di conoscenza previsti, sono, a titolo esclusivamente orientativo, ulteriormente precisati nel seguito.

**LC1:** si intende raggiunto quando sia stata effettuata l’analisi storico-critica commisurata al livello considerato (con riferimento al § C8.5.1), la geometria della struttura sia nota in base ai disegni originali (effettuando un rilievo visivo a campione per verificare l’effettiva corrispondenza del costruito ai disegni) o a un rilievo, poiché non si dispone dei disegni costruttivi i dettagli costruttivi siano stati ricavati sulla base di un progetto simulato (con riferimento al § C8.5.2) e con indagini limitate in-situ sulle armature e sui collegamenti presenti negli elementi più importanti (i dati raccolti devono essere tali da consentire verifiche locali di resistenza), poiché non si dispone di informazioni sulle caratteristiche meccaniche dei materiali (provenienti dai disegni costruttivi o dai certificati di prova) si siano adottati i valori usuali della pratica costruttiva dell’epoca, convalidati da prove limitate in-situ sugli elementi più importanti (con riferimento al § C8.5.3); il corrispondente fattore di confidenza è FC=1,35. La valutazione della sicurezza è, in genere, eseguita mediante analisi lineare, statica o dinamica; le informazioni raccolte devono consentire la messa a punto di un modello strutturale idoneo.

**LC2:** si intende raggiunto quando sia stata effettuata l’analisi storico-critica commisurata al livello considerato (con riferimento al § C8.5.1), la geometria della struttura sia nota in base ai disegni originali (effettuando un rilievo visivo a campione per verificare l’effettiva corrispondenza del costruito ai disegni) o a un rilievo, i dettagli costruttivi siano noti, o parzialmente dai disegni costruttivi originali integrati da indagini limitate in situ sulle armature e sui collegamenti presenti negli elementi più importanti, o (con riferimento al § C8.5.2) a seguito di una indagine estesa in situ (i dati raccolti devono essere tali da consentire, nel caso si esegua un’analisi lineare, verifiche locali di resistenza, oppure la messa a punto di un modello strutturale non lineare), le caratteristiche meccaniche dei materiali siano note in base ai disegni costruttivi, integrati da prove limitate in situ (se i valori ottenuti dalle prove in situ sono minori dei corrispondenti valori indicati nei disegni di progetto, si eseguono prove estese in situ), o con prove estese in situ (con riferimento al § C8.5.3); il corrispondente fattore di confidenza è FC=1,2. La valutazione della sicurezza è eseguita mediante metodi di analisi lineare o non lineare, statici o dinamici; le informazioni raccolte sulle dimensioni degli elementi strutturali, insieme a quelle riguardanti i dettagli strutturali, devono consentire la messa a punto di un modello strutturale idoneo.

**LC3:** si intende raggiunto quando sia stata effettuata l’analisi storico-critica commisurata al livello considerato (con riferimento al § C8.5.1), la geometria della struttura sia nota in base ai disegni originali (effettuando un rilievo visivo a campione per verificare l’effettiva corrispondenza del costruito ai disegni) o a un rilievo, i dettagli costruttivi siano noti, o dai disegni costruttivi originali integrati da indagini limitate in situ sulle armature e sui collegamenti presenti negli elementi più importanti, o (con riferimento al § C8.5.2) a seguito di una indagine esaustiva in situ (i dati raccolti devono essere tali da consentire, nel caso si esegua un’analisi lineare, verifiche locali di resistenza, oppure la messa a punto di un modello strutturale non lineare), le caratteristiche meccaniche dei materiali siano note in base ai disegni costruttivi e ai certificati originali di prova, integrati da prove limitate in situ (se i valori ottenuti dalle prove in situ sono minori dei corrispondenti valori indicati nei certificati originali di prova, si eseguono prove esaustive in situ), o con prove esaustive in situ (con riferimento al § C8.5.3); il corrispondente fattore di confidenza è FC=1. La valutazione della sicurezza è eseguita mediante metodi di analisi lineare o non lineare, statici o dinamici; le informazioni raccolte sulle dimensioni degli elementi strutturali, insieme a quelle riguardanti i dettagli strutturali, devono consentire la messa a punto di un modello strutturale idoneo. Le resistenze dei materiali cui riferirsi nelle formule di capacità degli elementi sono ricavate dalle resistenze medie, ottenute dalle informazioni disponibili e dalle prove in situ aggiuntive, dividendole per gli FC indicati nella Tabella C8.5.IV. Gli FC possono essere valutati anche in modo differenziato per i diversi materiali, sulla base di considerazioni statistiche condotte su un insieme di dati significativo per gli elementi in esame e di metodi di comprovata validità. A titolo esclusivamente orientativo, nelle tabelle C8.5.V e C8.5.VI si lega il livello (limitato, esteso, esaustivo) delle indagini alla quantità di rilievi dei dettagli costruttivi e di prove per la valutazione delle caratteristiche meccaniche dei materiali. Rimane inteso che il piano delle indagini deve essere opportunamente calibrato in funzione dell’analisi preliminare (v. § C8.5.2.2 e C8.5.3.2) e quindi, in relazione al livello di conoscenza da raggiungere, orientato agli approfondimenti necessari nelle zone della costruzione ove risulti opportuno, sia in relazione all’impegno statico delle diverse membrature e al loro ruolo riguardo alla sicurezza della struttura, sia in relazione al grado di omogeneità dei risultati delle prove preliminari e al loro accordo con quanto previsto dai documenti originari.

**Tabella C8.5.V** - *Definizione orientativa dei livelli di rilievo e prova per edifici di c.a.*

| Livello di Indagini e Prove | Rilievo (dei dettagli costruttivi) (a) | Prove (sui materiali) (b)(c)(d) |
|---|---|---|
| | Per ogni elemento "primario" (trave, pilastro) | |
| ***limitato*** | La quantità e disposizione dell'armatura è verificata per almeno il 15% degli elementi | 1 provino di cls. per 300 m² di piano dell'edificio, 1 campione di armatura per piano dell'edificio |
| ***esteso*** | La quantità e disposizione dell'armatura è verificata per almeno il 35% degli elementi | 2 provini di cls. per 300 m² di piano dell'edificio, 2 campioni di armatura per piano dell'edificio |
| ***esaustivo*** | La quantità e disposizione dell'armatura è verificata per almeno il 50% degli elementi | 3 provini di cls. per 300 m² di piano dell'edificio, 3 campioni di armatura per piano dell'edificio |

**Tabella C8.5.VI** - *Definizione orientativa dei livelli di rilievo e prova per edifici di acciaio*

| Livello di Indagini e Prove | Rilievo (dei collegamenti) (a) | Prove (sui materiali) (b)(c)(d) |
|---|---|---|
| | Per ogni elemento "primario" (trave, pilastro...) | |
| ***limitato*** | Le caratteristiche dei collegamenti sono verificate per almeno il 15% degli elementi | 1 provino di acciaio per piano dell'edificio, 1 campione di bullone o chiodo per piano dell'edificio |
| ***esteso*** | Le caratteristiche dei collegamenti sono verificate per almeno il 35% degli elementi | 2 provini di acciaio per piano dell'edificio, 2 campioni di bullone o chiodo per piano dell'edificio |
| ***esaustivo*** | Le caratteristiche dei collegamenti sono verificate per almeno il 50% degli elementi | 3 provini di acciaio per piano dell'edificio, 3 campioni di bullone o chiodo per piano dell'edificio |

NOTE ESPLICATIVE ALLE TABELLE C8.5.V E C8.5.VI

Le percentuali di elementi da indagare ed il numero di provini da estrarre e sottoporre a prove di resistenza riportati nelle Tabelle C8.5.V e C8.5.VI hanno valore indicativo e vanno adattati ai singoli casi, tenendo conto dei seguenti aspetti:

(a) Nel controllo del raggiungimento delle percentuali di elementi indagati ai fini del rilievo dei dettagli costruttivi si tiene conto delle eventuali situazioni ripetitive, che consentano di estendere ad una più ampia percentuale i controlli effettuati su alcuni elementi strutturali facenti parte di una serie con evidenti caratteristiche di ripetibilità, per geometria e ruolo uguali nello schema strutturale.

(b) Le prove sugli acciai sono finalizzate all’identificazione della classe dell’acciaio utilizzata con riferimento alla normativa vigente all’epoca di costruzione. Ai fini del raggiungimento del numero di prove sull’acciaio necessario per acquisire il livello di conoscenza desiderato è opportuno tener conto dei diametri (nelle strutture in c.a.) o dei profili (nelle strutture in acciaio) di più diffuso impiego negli elementi principali, con esclusione delle staffe.

(c) Ai fini delle prove sui materiali è consentito sostituire alcune prove distruttive, non più del 50%, con almeno il triplo di prove non distruttive, singole o combinate, tarate su quelle distruttive.

(d) Il numero di provini riportato nelle tabelle C8.5.V e C8.5.VI può esser variato, in aumento o in diminuzione, in relazione alle caratteristiche di omogeneità del materiale. Nel caso del calcestruzzo in opera, tali caratteristiche sono spesso legate alle modalità costruttive tipiche dell’epoca di costruzione e del tipo di manufatto, di cui occorrerà tener conto nel pianificare l’indagine. Sarà opportuno, in tal senso, prevedere l’effettuazione di una seconda campagna di prove integrative, nel caso in cui i risultati della prima risultino fortemente disomogenei.

#### C8.5.4.3. Costruzioni di legno

Per le costruzioni di legno, fermo restando quanto indicato nel § 8.5 delle NTC, stante la possibile variabilità del materiale soprattutto nel costruito storico, è opportuno estendere, ove possibile ed in relazione ai livelli di conoscenza che si intende raggiungere, l’indagine ai singoli elementi, soprattutto per valutare il degrado biotico e abiotico. E’ inoltre opportuno verificare le condizioni delle estremità delle membrature (o di struttura lignea), in particolare quando a contatto con altro materiale.

### C8.5.5. Azioni

Le verifiche di sicurezza devono essere effettuate tenendo conto di tutte le azioni presenti, sia non sismiche, sia sismiche. Con riferimento a quanto espresso nel § 8.5 delle NTC si precisa che, nel caso di combinazioni di carico che includano l’azione sismica, ai fini della determinazione dell’entità massima delle azioni sopportabili dalla struttura si considerano i carichi permanenti effettivamente riscontrati e quelli variabili previsti dalle NTC. L'azione sismica è definita, per i diversi stati limite, al § 3.2 delle NTC, tenuto conto del periodo di riferimento definito al § 2.4 delle NTC (v. anche § C8.3). Per la combinazione dell’azione sismica con le altre azioni, valgono i criteri di cui al § 2.5.3 delle NTC. Le diverse componenti dell’azione sismica sono combinate con i criteri riportati al § 7.3.5 delle NTC.

#### C8.5.5.1. Costruzioni in muratura

Per la verifica di edifici con analisi lineare e impiego del fattore q, si possono utilizzare per quest'ultimo i seguenti valori:

- $q=2{,}0\alpha_u/\alpha_1$ per edifici regolari in elevazione, nel caso di muratura in pietra e/o mattoni pieni;
- $q=1{,}75\alpha_u/\alpha_1$ per edifici regolari in elevazione, nel caso di muratura in blocchi artificiali con percentuale di foratura >15% (elementi semipieni, forati...).

in cui $\alpha_u$ e $\alpha_1$ sono definiti al § 7.8.1.3 delle NTC. In assenza di più precise valutazioni, non può essere assunto un rapporto $\alpha_u/\alpha_1$ superiore a 1,5.

Nel caso di edificio non regolare in elevazione i valori di $q$ sono ridotti del 25%. La definizione di regolarità per un edificio esistente in muratura è quella indicata al § 7.2.1 delle NTC.

#### C8.5.5.2. Costruzioni di calcestruzzo armato o acciaio

Il fattore di comportamento q è scelto nel campo fra 1,5 e 3,0, sulla base della regolarità nonché dei tassi di lavoro dei materiali (quando soggetti alle azioni non sismiche). Valori di q superiori a quelli sopra indicati devono essere adeguatamente giustificati con riferimento alla duttilità disponibile a livello locale e globale.
