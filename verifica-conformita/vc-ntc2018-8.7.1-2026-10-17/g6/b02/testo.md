Per le verifiche che seguono, l’insieme di tali vincoli deve essere tale da costituire una catena cinematica a un grado di libertà, il cui atto di moto può essere descritto da un parametro di spostamento (o rotazione) virtuale infinitesimo. La rappresentazione della struttura come catena cinematica di corpi rigidi è attendibile solo se la parete non è vulnerabile nei riguardi di fenomeni di disgregazione.

Le ipotesi tradizionalmente adottate per modellare questo tipo di meccanismi locali sono le seguenti:

- resistenza della muratura a trazione, nulla;

- scorrimento tra i blocchi, assente;

- resistenza a compressione della muratura, infinita.

Tuttavia, per una simulazione più realistica (anche se in forma approssimata) del comportamento, è possibile considerare:

- a) gli scorrimenti tra i blocchi, considerando la presenza dell’attrito;

- b) le connessioni, anche di resistenza limitata, tra le pareti murarie;

- c) la presenza di catene metalliche e di collegamenti alle strutture orizzontali;

- d) la limitata resistenza a compressione della muratura, considerando le cerniere adeguatamente arretrate rispetto allo spigolo della sezione;

- e) la presenza di pareti a paramenti scollegati.

In generale occorre considerare i meccanismi locali significativi, verificando ciascuno di essi con analisi che vanno dalla statica, lineare o non lineare, alla dinamica non lineare.

Nel caso di analisi statica, l’azione sismica è espressa da forze orizzontali di massa la cui intensità è rappresentata dal moltiplicatore $\alpha$, pari al rapporto tra le forze orizzontali e i corrispondenti pesi delle masse presenti. La verifica può essere eseguita in termini di accelerazione (***approccio cinematico lineare***) o di spostamento (***approccio cinematico non lineare***).

In particolare, la verifica attraverso i metodi dell’analisi limite con approccio cinematico si articola nei seguenti passi:

- individuazione del meccanismo di dissesto;

- valutazione del moltiplicatore orizzontale dei carichi $\alpha_0$ che comporta l’attivazione del meccanismo;

- determinazione della curva $\alpha-d_C$ (essendo $d_C$ lo spostamento di un punto di controllo della catena cinematica, usualmente
scelto in prossimità del baricentro delle masse) fino all’annullamento della forza sismica orizzontale;

- trasformazione della curva così ottenuta nella curva di capacità che esprime l’accelerazione spettrale $a$ in funzione dello spostamento spettrale $d$ di un oscillatore non lineare equivalente a un grado di libertà;

- esecuzione delle verifiche di sicurezza, attraverso il controllo della compatibilità degli spostamenti e/o delle resistenze
richiesti alla struttura.

L’***approccio cinematico lineare*** si basa sulla valutazione dell’azione orizzontale che è in grado di attivare il cinematismo; la verifica consiste nel confronto tra l’accelerazione necessaria per attivare il cinematismo e la massima accelerazione al suolo corrispondente allo stato limite di interesse, opportunamente ridotta, nel caso di verifica allo SLV, attraverso il fattore di comportamento $q$.

L’***approccio cinematico non lineare*** richiede la determinazione dell’azione orizzontale che la struttura è progressivamente in grado di sopportare all’evolversi del meccanismo. La curva che ne rappresenta l’andamento esprime il valore del moltiplicatore $\alpha$ in funzione dello spostamento $d_C$ di un punto di riferimento del sistema, e deve essere tracciata fino all’annullamento di ogni capacità di sopportare azioni orizzontali ($\alpha=0$).

Essa può essere trasformata, come di seguito descritto (v. § C8.7.1.2.4), nella curva di capacità di un sistema equivalente a un grado di libertà, sulla quale può essere individuata la capacità di spostamento ultimo del meccanismo; la verifica consiste nel confronto tra lo spostamento richiesto dall’azione sismica e quello corrispondente al raggiungimento dello stato limite ultimo.

Nel caso di analisi dinamica non lineare, l’azione sismica è descritta in forma di accelerogrammi, opportunamente selezionati in base alle caratteristiche sismologiche del sito in esame e allo stato limite considerato, come indicato nelle NTC e meglio precisato nel seguito della presente Circolare; tali accelerogrammi debbono essere in numero sufficiente ad individuare una risposta media significativa, stante la sensibilità alle caratteristiche del singolo accelerogramma mostrata dalla risposta dinamica di meccanismi di parete soggetti ad azioni fuori dal loro piano medio.

###### *C8.7.1.2.1.1 Analisi con approccio cinematico lineare*

L'analisi con approccio cinematico lineare (o cinematica lineare) richiede il calcolo del solo moltiplicatore di attivazione del meccanismo $\alpha_0$ e può essere utilizzata per eseguire sia la verifica allo Stato Limite di Danno (attivazione del meccanismo locale) sia quella allo SLV, in quest’ultimo caso attraverso il metodo semplificato del fattore di comportamento $q$,.

A titolo indicativo, è necessario individuare preliminarmente l’entità ed il punto di applicazione dei pesi propri e di quelli portati da ciascun blocco o elemento della catena cinematica, l’entità delle forze esterne applicate e attritive, nonché di quelle interne agenti negli elementi elastici. L’azione sismica può essere rappresentata da un sistema di forze orizzontali, proporzionali ai pesi attraverso un coefficiente $\alpha$. Nel calcolo dell’azione sismica è opportuno che siano considerate anche le forze orizzontali indotte dalle eventuali masse che non gravano direttamente sui blocchi, ma la cui azione sismica inerziale andrebbe ad agire sui blocchi del meccanismo (ad esempio, un solaio o una copertura gravano sull’elemento della catena cinematica solo parzialmente ma, se non trattenuti all’altra estremità, possono esercitare un’azione sismica orizzontale proporzionale all’intera massa).

Applicando il teorema dei lavori virtuali è possibile calcolare il moltiplicatore $\alpha_0$ che attiva il cinematismo, attraverso la seguente espressione:

$$
\alpha_0 =
\frac{\sum_{k=1}^{N}P_k\delta_{Py,k}-\sum_{k=1}^{m}F_k\delta_{F,k}+L_i}
{\sum_{k=1}^{N}(P_k+Q_k)\delta_{PQx,k}}
\tag{C8.7.1.1}
$$

dove:

- $N$ è il numero dei blocchi di cui è costituita la catena cinematica;

- $m$ è il numero di forze esterne, assunte indipendenti dall’azione sismica, applicate ai diversi blocchi;

- $P_k$ è la risultante delle forze peso applicate al $k$-esimo blocco (peso proprio del blocco, applicato nel suo baricentro, sommato agli altri pesi portati);

- $Q_k$ è la risultante delle forze peso non gravanti sul $k$-esimo blocco ma la cui massa genera su di esso una forza sismica orizzontale, in quanto non efficacemente trasmessa ad altre parti dell'edificio;

- $F_k$ è la generica forza esterna applicata ad uno dei blocchi; tali forze possono favorire l’attivazione del meccanismo (ad es. spinte di volte) o ostacolarlo (ad es. archi di contrasto, ovvero forze attritive che si sviluppano in presenza di parti della costruzione non coinvolte nel meccanismo);

- $\delta_{Py,k}$ è lo spostamento virtuale verticale del baricentro delle forze peso proprie e portate $P_k$, agenti sul $k$-esimo blocco, assunto positivo se verso l’alto;

- $\delta_{F,k}$ è lo spostamento virtuale del punto d’applicazione della forza esterna $F_k$, proiettato nella direzione della stessa (di segno positivo o negativo a seconda che questa favorisca o contrasti il meccanismo);

- $\delta_{PQx,k}$ è lo spostamento virtuale orizzontale del baricentro delle forze orizzontali $\alpha(P_k+Q_k)$ agenti sul $k$-esimo blocco, assumendo come verso positivo quello dell’azione sismica che attiva il meccanismo;

- $L_i$ è il lavoro totale di eventuali forze interne (allungamento di una catena; scorrimento con attrito in presenza di ammorsamento tra i blocchi del meccanismo, dovuto a moti relativi traslazionali o torsionali; deformazione nel piano di solai o coperture collegate ma non rigide).

Il moltiplicatore $\alpha_0$ che si ottiene dall’equazione [C8.7.1.1] rappresenta una stima per eccesso dell’effettivo moltiplicatore statico di collasso (corrispondente all’attivazione del meccanismo in ambito dinamico).

Quest’ultimo può essere stimato come il più basso dei moltiplicatori $\alpha_0$ ottenuti per i meccanismi selezionati come possibili tra quelli ricorrenti per configurazioni analoghe, in quanto caratterizzati da condizioni statiche e cinematiche realistiche; in tal senso, la forma geometrica delle porzioni di muratura coinvolte nella catena cinematica (e la posizione delle cerniere) dovrebbe derivare, nell’ambito di ciascuna classe di meccanismo, da un processo di minimizzazione, facendo riferimento anche a modelli attritivi a blocchi rigidi (identificazione del meccanismo corretto).

Un caso particolarmente significativo è quello di una parete che, pur essendo collegata alle pareti di spina ortogonali attraverso un ammorsamento murario parzialmente efficace, ribalta fuori dal proprio piano medio (ribaltamento semplice). A meno che non sia già in atto un distacco evidente dalle pareti ortogonali o che queste non siano totalmente prive di ammorsamento, tale meccanismo può considerare il contributo stabilizzante esercitato dalle pareti ortogonali attraverso resistenze attritive. La risultante della forza attritiva che può svilupparsi lungo l’altezza $h$ dell’ammorsamento con una parete ortogonale (lesione verticale a pettine, ipotizzando caratteristiche di ammorsamento pressoché uniformi) può essere ricavata in modo approssimato dalla seguente espressione:

$$
F = 0.4\,n(n+1)\Phi\mu l^2t_sW
\tag{C8.7.1.2}
$$

dove:

- $n$ è il numero dei filari interessati dalla lesione verticale ($n=h/h_b$, dove $h_b$ è l’altezza media degli elementi costituenti la muratura);

- $l$ è la lunghezza del singolo giunto attritivo, sovrapposizione tra i blocchi di due corsi successivi;

- $\phi$ è il coefficiente di ammorsamento, così definito $\phi=h_b/l$; tale parametro è analogamente definito per il criterio di resistenza a taglio per fessurazione diagonale, con rottura “a scaletta” nei giunti di malta, nell’equazione [C8.7.1.17];

- $\mu$ è il coefficiente d’attrito; un valore di riferimento è 0,577, identico a quello indicato per l’equazione [C8.7.1.17];

- $t_s$ è lo spessore della parete trasversale (opportunamente ridotto nel caso di muratura a tre paramenti);

- $w$ è il peso specifico della muratura (valori sono suggeriti nella Tabella C8.5.I).

Il punto di applicazione di questa resistenza può essere assunto a quota $1/3h$; si ricorda che l’altezza $h$ (ovvero la estensione della cerniera) dovrebbe essere identificata attraverso un processo di minimizzazione del moltiplicatore $\alpha_0$.

