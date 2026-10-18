Queste resistenze attritive si sviluppano anche nel caso in cui la lesione non sia “a pettine” (verticale) ma presenti un andamento inclinato. Tuttavia la [C8.7.1.2] può essere considerata valida solo nel caso di lesione verticale, perché nel caso di lesione inclinata le rotazioni e i distacchi tendono ad essere prevalenti sugli scorrimenti. Nel caso limite di lesione secondo la “scaletta” naturale (definita dal parametro $\phi$) in genere si ha solo distacco per rotazione e il contributo attritivo si annulla; la [C8.7.1.2] è stata formulata assumendo un coefficiente riduttivo pari a 0,8, per considerare che, anche nel caso di lesione verticale, non si ha uno scorrimento puro.

Si fa inoltre presente che la [C8.7.1.2] non considera il contributo di eventuali carichi applicati in sommità ai muri ortogonali a quello in esame, quali parapetti o solai e coperture, i quali incrementano lo stato di sollecitazione verticale sulle superfici di ammorsamento (ciò avviene in misura ridotta anche nel caso di lesione verticale “a pettine”, a seguito della diffusione delle tensioni nella muratura). L’entità di questa resistenza aggiuntiva può essere stimata e il suo punto di applicazione, in genere, può essere assunto a quota $1/2h$.

###### *C8.7.1.2.1.2 Analisi con approccio cinematico non lineare*

L’analisi con approccio cinematico non lineare (o cinematica non lineare) richiede la valutazione del moltiplicatore $\alpha$ non solo per la configurazione iniziale della catena cinematica ma anche per configurazioni variate, rappresentative dell’evoluzione del cinematismo e descritte dallo spostamento orizzontale $d_C$ di un punto $C$ di controllo del sistema, scelto a piacere. In generale il moltiplicatore $\alpha$ si riduce progressivamente, fino ad annullarsi in corrispondenza dello spostamento $d_{C0}$.

La curva $\alpha-d_C$, ottenuta attraverso l’analisi cinematica non lineare, rappresenta (a meno dell’accelerazione di gravità $g$) la curva forza reattiva-spostamento, o curva di spinta, del meccanismo locale. Per la sua determinazione è necessario considerare se, con l’evolversi del cinematismo, le forze interne ed esterne si modificano o si mantengono costanti.

###### *C8.7.1.2.1.3 Definizione dell'oscillatore non lineare equivalente*

Al fine di valutare la domanda sismica di spostamento, è necessario determinare la “curva di capacità” del meccanismo locale, ovvero ricondursi alla risposta (a meno dell’accelerazione di gravità $g$) di un oscillatore equivalente non lineare a un grado di libertà descritta in termini accelerazione-spostamento come $\alpha(d)$:

$$
a = \frac{\alpha(d_c)g}{e^*FC}
\tag{C8.7.1.3}
$$

$$
d = d_c\frac{\sum_{k=1}^{N}(P_k+Q_k)\delta_{PQx,K}^2}
{\delta_{Cx}\sum_{k=1}^{N}(P_k+Q_k)\delta_{PQx,K}}
\tag{C8.7.1.4}
$$

dove:

- $g$ è l’accelerazione di gravità;

- $FC$ è il Fattore di Confidenza, che in questo caso si applica direttamente alla capacità in termini di resistenza (nel caso in cui, per la valutazione del moltiplicatore $\alpha$, non si tenga conto della resistenza a compressione della muratura, il fattore di confidenza da utilizzare sarà comunque quello relativo al livello di conoscenza **LC1**;

- $\delta_{Cx}$ è lo spostamento virtuale orizzontale del punto di controllo valutato, così come gli spostamenti virtuali $\delta_{PQx,k}$, a partire dalla configurazione indeformata iniziale;

- $e^*$ è la frazione di massa partecipante che, in prima approssimazione, può essere valutata considerando gli spostamenti virtuali relativi al cinematismo (misurati a partire dalla configurazione indeformata iniziale) come rappresentativi del modo di vibrazione del meccanismo locale.

$$
e^* =
\frac{\left[\sum_{k=1}^{N}(P_k+Q_k)\delta_{PQx,k}\right]^2}
{\left[\sum_{k=1}^{N}(P_k+Q_k)\right]\left[\sum_{k=1}^{N}(P_k+Q_k)\delta_{PQx,k}^2\right]}
\tag{C8.7.1.5}
$$

La curva di capacità così ottenuta presuppone che il comportamento del meccanismo, prima della sua attivazione, sia infinitamente rigido; questa assunzione è ammissibile nel caso di meccanismi fuori dal piano di pareti murarie inizialmente vincolate con continuità alle pareti trasversali, in quanto le prime, precedentemente all’attivazione del meccanismo stesso, non sono caratterizzate da un comportamento dinamico autonomo.

Nel caso invece di elementi liberi di vibrare (quali parapetti, porzioni svettanti di facciate, pinnacoli o merlature, ecc.) è necessario considerare che la loro risposta, prima che si verifichino le condizioni di attivazione del cinematismo, è dinamica elastica, anche se spesso caratterizzata da un basso periodo di vibrazione; è quindi necessario introdurre un ramo elastico iniziale nella curva di capacità, legando l’accelerazione $a$ allo spostamento $d$ mediante il periodo $T_0$ attraverso la equazione [C8.7.1.6].

$$
a = \frac{4\pi^2}{T_0^2}d
\tag{C8.7.1.6}
$$

Il periodo $T_0$, a sua volta, può essere stimato, a partire dalla soluzione della trave con massa distribuita, con la formula:

$$
T_0 = k\lambda L\sqrt{\frac{W}{Eg}}
\tag{C8.7.1.7}
$$

dove:

- $g$ è l’accelerazione di gravità;

- $\kappa$ è un coefficiente che vale 6,2 per elementi svettanti (mensola) e 2,2 per meccanismi flessionali verticali (trave appoggiata);

- $\mathrm{L}$ è la lunghezza dell’elemento;

- $\lambda$ è la snellezza dell’elemento (rapporto tra la lunghezza $L$ e lo spessore $t$);

- $W$ è il peso specifico della muratura;

- $E$ è il modulo elastico della muratura (valori sono suggeriti nella Tabella C8.5.I); si suggerisce di introdurre un valore ridotto per considerare condizioni fessurate.

Questo tratto lineare definisce il primo ramo della curva di capacità fino all’intersezione $(a_y,d_y)$ con la curva di capacità del meccanismo locale in coordinate spettrali, come ottenuta dalla curva di spinta risultante dall’analisi cinematica non lineare mediante la trasformazione di variabili (C8.7.1.4) e (C8.7.1.5).

###### *C8.7.1.2.1.4 Azioni spettrali da applicare nella verifica dei meccanismi locali*

Per la verifica dei meccanismi locali occorre valutare correttamente gli effetti di interazione dinamica con la costruzione, in relazione alle sue caratteristiche dinamiche (frequenze proprie) e alla quota alla quale gli elementi soggetti a verifica sono collocati (forme modali). Per la determinazione degli spettri di risposta alle diverse quote della costruzione, si può fare riferimento al § C7.2.3 e, in particolare, alle equazioni [C.7.2.5÷10].

In particolare, per tener conto delle non linearità della struttura principale, che producono una riduzione dell’amplificazione delle accelerazioni relative ai meccanismi locali, occorre valutare lo smorzamento viscoso equivalente $\xi_k$ e l’incremento del periodo equivalente $T_k$, da introdurre nelle equazioni suddette.

È quindi opportuno valutare lo spettro alla quota $z$ con parametri compatibili con il livello di duttilità richiesto, alla struttura principale, dall’azione corrispondente alla formazione del meccanismo locale ricordando che, nella risposta globale allo stato limite ultimo, gli edifici in muratura presentano un incremento del periodo equivalente compreso tra il 50% ed il 100% e raggiungono valori di smorzamento viscoso equivalente variabili dal 10% fino al 20%.

Infine, si segnala che, nel caso di meccanismi locali che coinvolgano significative porzioni di muratura (ad esempio porzioni svettanti di facciate), la verifica per sottostrutture non è pienamente legittima, in quanto sarebbe necessario considerare l’interazione dinamica tra struttura principale e secondaria. Tale interazione comporta una riduzione della domanda in accelerazione sulla struttura secondaria, che può essere eventualmente stimata attraverso un opportuno coefficiente funzione del rapporto tra la massa di quest’ultima e quella della struttura principale; la formulazione proposta fornisce comunque una stima cautelativa della massima amplificazione spettrale.

###### *C8.7.1.2.1.5 Verifica dello Stato Limite di Danno del meccanismo locale*

Nel caso dei meccanismi locali l’attivazione del meccanismo comporta l’apertura di lesioni, una condizione che può essere ancora lontana dal vero e proprio ribaltamento; peraltro, la presenza di un quadro fessurativo non necessariamente indica l’attivazione di un meccanismo di dissesto. Tuttavia, nel caso di elementi murari non efficacemente connessi al resto della costruzione per l’assenza di catene, di ammorsamento con i muri ortogonali, di collegamenti con i diaframmi orizzontali, la vulnerabilità nei confronti di questo stato limite può risultare elevata, come è stato osservato frequentemente a seguito dei passati terremoti.

Nell’ipotesi che la porzione rappresentata dal sistema di corpi rigidi si comporti come infinitamente rigida fino all’attivazione del cinematismo, questo si attiva quando l’accelerazione massima alla quota $z$ ($a_{\mathrm{Z}}$) a cui si colloca il meccanismo locale in esame è uguale all’accelerazione $a_0$ corrispondente al moltiplicatore di attivazione $\alpha_0$:

$$
\mathrm{a}_{Z,SLD} = \frac{\alpha_0g}{e\ast FC}
\tag{C8.7.1.8}
$$

Nel caso invece di meccanismi locali relativi ad elementi liberi di vibrare (quali parapetti, porzioni svettanti di facciate, pinnacoli o merlature, ecc.) è necessario considerare la domanda in accelerazione (alla quota $z$) corrispondente al periodo caratteristico iniziale $T_0$ del meccanismo (per uno smorzamento $\xi=5\%$, a meno di più accurate valutazioni da adottare in funzione della geometria e delle condizioni di vincolo) e confrontarla con la capacità $a_y$ (che può in genere essere approssimata da $\alpha_0$):

$$
\mathrm{S}_{eZ,SLD}(T_0) = \frac{a_y}{FC} \cong \frac{\alpha_0g}{e\ast FC}
\tag{C8.7.1.9}
$$

Per la verifica è, in entrambi i casi, necessario valutare l’accelerazione al suolo $a_{g,SLD}$, rispettivamente attraverso la [C7.2.11] o la [C7.2.5], e confrontarla con l’accelerazione di riferimento al suolo $a_g$ valutata per la probabilità di superamento corrispondente allo stato limite di danno per la struttura oggetto di verifica.

###### *C8.7.1.2.1.6 Verifica degli Stati Limite Ultimi di Salvaguardia della Vita (SLV) e di prevenzione del Collasso (SLC)*

La verifica a stato limite ultimo può essere eseguita con riferimento ad uno dei due stati limite (**SLV** o **SLC**) individuati sulla curva di capacità attraverso opportune soglie dello spostamento spettrale $d$.

**SLV:** lo spostamento $d_{SLV}$ corrisponde al minore tra gli spostamenti così definiti:

- il 40% dello spostamento $d_0$ per cui si annulla l’accelerazione spettrale $a$ valutata su una curva di capacità in cui si considerino solamente le azioni di cui è verificata la presenza fino al collasso;

- lo spostamento corrispondente a situazioni nelle quali si verifichino rotture di elementi, quali catene o altri collegamenti, che, pur non comportando problemi di equilibrio, producano una riduzione della capacità, in termini di accelerazione, superiore al 50% del valore massimo; ovviamente non devono verificarsi le condizioni di seguito indicate per lo **SLC** (ad esempio sfilamento di travi, collasso di volte).

**SLC:** lo spostamento $d_{SLC}$ corrisponde al minore tra gli spostamenti così definiti:

- il 60% dello spostamento $d_0$ per cui si annulla l’accelerazione spettrale $a$ valutata su una curva di capacità in cui si considerino solamente le azioni di cui è verificata la presenza fino al collasso;

- lo spostamento corrispondente a situazioni localmente incompatibili con la stabilità degli elementi della costruzione (ad esempio sfilamento di travi, collasso di volte), nei casi in cui questo sia valutabile.

Per la verifica si utilizzano, in genere, metodi di analisi non lineare, statica o dinamica; la verifica allo **SLV** può essere eseguita anche adottando un metodo lineare, considerando solo il moltiplicatore di attivazione del meccanismo e utilizzando un fattore di comportamento $q$.

Le procedure descritte nel seguito sono state calibrate per meccanismi nei quali gli spostamenti dei punti di tutti i corpi rigidi coinvolti si mantengano paralleli ad uno stesso piano; condizioni di vincolo più complesse, che comportino ad esempio l’attivazione di cerniere torsionali, possono non esser adeguatamente rappresentante dalle equazioni che seguono.

###### *C8.7.1.2.1.7 Verifica semplificata dello SLV con fattore di comportamento q (analisi cinematica lineare)*

Questo metodo di verifica può essere utilizzato quando non viene calcolata la curva di capacità $a(d)$, ma solo il moltiplicatore $\alpha_0$ che attiva il meccanismo. Tale semplificazione può essere conveniente, in particolare, per meccanismi complessi, identificati tenendo conto anche del contributo dell’attrito e dell’interazione con altri elementi della costruzione, per i quali l’esecuzione di un’analisi cinematica non lineare risulterebbe problematica.

L’accelerazione al suolo $a_{g,SLV}$ può essere calcolata moltiplicando per un fattore di comportamento $q$ l’accelerazione valutata per lo SLD ($a_{g,SLD}$), attraverso le equazioni [C8.7.1.8] e [C7.2.8], nel caso di meccanismi locali rigidamente vincolati alla struttura principale, o le equazioni [C8.7.1.9] e [C7.2.5], nel caso di elementi liberi di vibrare.

In assenza di valutazioni più accurate, che tengano conto del tipo di meccanismo e dello spessore delle pareti, si può assumere $q=2$.

L’accelerazione al suolo $a_{g,SLV}$ deve essere confrontata con l’accelerazione di riferimento al suolo $a_g$ valutata per la probabilità di superamento dello SLV nella vita di riferimento, come definita al §3.2 delle NTC.

###### *C8.7.1.2.1.8 Verifica in spostamento allo SLV e allo SLC (analisi cinematica non lineare)*

La verifica in spostamento si esegue calcolando l’accelerazione al suolo che produce una domanda di spostamento sul meccanismo locale pari a quella prima definita come corrispondente al raggiungimento dello **SLV** o dello **SLC**. A tal fine è necessario valutare, a partire dalla curva di capacità a($d$), il periodo equivalente caratteristico dei due stati limite:

$$
T_{SLV} = 1{,}68\pi\sqrt{\frac{d_{SLV}}{a(d_{SLV})}}
\tag{C8.7.1.10}
$$

$$
T_{SLC} = 1{,}56\pi\sqrt{\frac{d_{SLC}}{a(d_{SLC})}}
\tag{C8.7.1.11}
$$

Tali periodi sono opportunamente ridotti rispetto a quelli corrispondenti allo spostamento ultimo assunto, tenendo conto della dispersione dei risultati in prossimità della soglia di instabilità dinamica.

La domanda di spostamento sul meccanismo locale allo **SLV** corrisponde al valore massimo dello spostamento spettrale valutato nell’intervallo di periodi [$T_0$, $T_{SLV}$]. Questo criterio deve essere seguito nel caso in cui siano stati selezionati accelerogrammi di sito o sia stata svolta un’analisi di risposta sismica locale (spettro di spostamento non strettamente crescente con il periodo $T$ anche per bassi periodi), in quanto i picchi dello spettro sono spesso associati a impulsi particolarmente pericolosi.

Nel caso in cui il meccanismo locale che si sta verificando sia collocato a livello del suolo e la verifica sia effettuata tramite gli spettri di norma, la domanda di spostamento è quella calcolata attraverso lo spettro di risposta elastico in spostamento $S_{De}(T)$ (§ 3.2.3.2.3 delle NTC) per i valori caratteristici del periodo corrispondenti ai due stati limite.

Per meccanismi ad una quota $z$ dell’edificio è necessario fare riferimento allo spettro in accelerazione alla quota z (v. formula [C7.2.5]), trasformato in spettro in spostamento sempre alla quota $z$ moltiplicandolo per $T^2/4\pi^2$. Per la verifica a stato limite ultimo dei meccanismi locali, considerato che i periodi di interesse dello spettro sono in genere lunghi, è sufficiente considerare il solo primo modo di vibrazione, o comunque il primo tra quelli caratterizzati da spostamenti significativi nella zona dove si sviluppa il meccanismo locale.

Considerato che la domanda di spostamento deve essere valutata, per quanto sopra detto, su uno spettro di spostamento non decrescente con il periodo $T$, è possibile riferirsi alle seguenti espressioni per lo SLV:

$$
d_{SLV} = S_{eZ}(T_{SLV},\xi,z)\frac{T_{SLV}^2}{4\pi^2}
\left(\ge S_{eZ}(T_1,\xi,z)\frac{b^2T_1^2}{4\pi^2}\quad \textit{per } T_{SLV}>bT_1\right)
\tag{C8.7.1.12}
$$

Dalla espressione [C8.7.1.12] è possibile calcolare l’accelerazione al suolo $a_{g,SLV}$ (nel caso in cui questa risulti minore di $a_{gSLD}$ calcolata al § C8.7.1.2.1.5, si assume quest’ultima anche per lo SLV). Per la verifica, $a_{gSLV}$ deve essere confrontata con l’accelerazione di riferimento al suolo $a_g$ valutata per la probabilità di superamento dello SLV nella vita di riferimento, come definita al § 3.2 delle NTC.

Un’espressione analoga alla [C8.7.1.12] consente di valutare la domanda di spostamento allo SLC e i corrispondenti valori di $a_{g,SLC}$.

Nel calcolo della domanda di spostamento allo stato limite ultimo è importante considerare l’effetto della dissipazione, sia nel calcolo dello spettro in quota (non linearità della struttura principale), sia nella valutazione della domanda di spostamento (non linearità del meccanismo locale). In assenza di valutazioni più accurate, lo smorzamento viscoso equivalente $\xi$ del meccanismo locale può essere assunto complessivamente pari all’8% per lo SLV e al 10% per lo SLC. È inoltre opportuno che lo smorzamento $\xi_1$ e il periodo $T_1$ dell’edificio siano valutati considerando il livello di non linearità raggiunto dalla struttura principale in corrispondenza dei valori $a_{g,SLV}$ e $a_{g,SLC}$.

###### *C8.7.1.2.1.9 Verifica con analisi dinamica non lineare dello SLV e SLC*

La verifica con analisi dinamica non lineare può essere effettuata facendo ricorso ad approcci computazionali avanzati, anche a più gradi di libertà, in grado di simulare il distacco, la formazione del meccanismo locale e la risposta dinamica della struttura muraria, quali ad esempio approcci agli elementi distinti o approcci a macroelementi.

La rappresentazione dell’azione sismica mediante accelerogrammi in linea di principio consente di tenere conto, in modo adeguato, di fattori importanti nella risposta dinamica dei meccanismi locali che si manifestano nelle strutture murarie, quali ad esempio la distanza epicentrale, la sequenza e la durata dei picchi del segnale accelerometrico, fattori questi che possono essere rappresentati solo parzialmente attraverso uno spettro di risposta. Per contro, però, tali fattori è possibile conoscerli con un accettabile grado di dettaglio esclusivamente dopo che si è manifestato l’evento. A tal fine, in fase di analisi, il numero di accelerogrammi rappresentativi da considerare è in genere maggiore che per la verifica con analisi dinamica non lineare delle risposta globale, per tener conto della sensibilità della risposta dei meccanismi locali alle caratteristiche del singolo accelerogramma. In particolare, si consiglia di ricercare combinazioni di accelerogrammi naturali compatibili con gli spettri in accelerazione delle NTC, utilizzando cataloghi di registrazioni digitali, affidabili nelle componenti a lungo periodo dello spettro di risposta.

Molti meccanismi locali possono essere descritti anche attraverso un sistema dinamico non lineare a un grado di libertà, la cui formulazione richiede la definizione di una relazione forza-spostamento appropriata e la stima della massa associata al meccanismo locale e dei fenomeni di dissipazione che si manifestano nella risposta dinamica.

La formulazione del modello può discendere dalla descrizione della catena cinematica di blocchi rigidi che rappresenta il meccanismo locale e quindi la relativa curva scheletro può coincidere con la curva di capacità definita ai § C8.7.1.2.1.2 e § C8.7.1.2.1.3. Il modello può anche essere arricchito per tenere conto della cedevolezza dei vincoli e dei contatti, della non perfetta monoliticità dei blocchi murari, della deformabilità iniziale e di quant’altro per una migliore rappresentazione dell’effettivo comportamento dinamico del meccanismo locale.

Per quanto attiene ai fenomeni di dissipazione, questi possono essere modellati considerando diversi contributi:

1) un opportuno coefficiente di restituzione atto a rappresentare la perdita dell’energia cinetica dovuta all’urto tra i blocchi, funzione del tipo di meccanismo e della snellezza degli elementi;

2) una dissipazione viscosa equivalente, rappresentativa della risposta elastica iniziale e che può includere anche l’effetto del coefficiente di restituzione (quando non esplicitamente modellato);

3) una dissipazione dovuta a locali plasticizzazioni e a meccanismi attritivi, direttamente modellata attraverso il comportamento isteretico.

La verifica con analisi dinamica non lineare consente anche di rappresentare la risposta di meccanismi non simmetrici, in particolare quelli influenzati da vincoli monolateri, come nel caso dell’oscillazione fuori dal piano di una parete che si può verificare solo verso l’esterno.

In assenza di valutazioni più accurate, gli stati limite ultimi SLV e SLC si intendono rispettati a condizione che la soglia di spostamento $d_0$ rappresentativa della crisi della struttura non venga superata per alcuna delle analisi dinamiche effettuate e che la media degli spostamenti massimi ottenuti, per i diversi segnali accelerometrici utilizzati, attraverso l’integrazione delle equazioni del moto non ecceda, per ciascuno dei due stati limite, la rispettiva soglia di spostamento $d_{SLV}$ o $d_{SLC}$ così come definita al § C8.7.1.2.1.6.

#### C8.7.1.3 MECCANISMI GLOBALI METODI DI ANALISI DELLA RISPOSTA SISMICA E CRITERI DI VERIFICA

##### C8.7.1.3.1 Edifici singoli

L’analisi globale della risposta sismica degli edifici con struttura muraria “singoli” (cioè non facenti parte di un aggregato) può essere effettuata sia mediante l’analisi dei singoli setti murari sottoposti alle azioni di loro competenza (nel proprio piano e fuori dal proprio piano) in base ad una suddivisione per aree di influenza (come già esposto), sia mediante un modello globale in grado di ripartire tra i vari setti le azioni sismiche agenti sull’intero fabbricato. La scelta deve essere effettuata in base alle effettive capacità degli elementi costruttivi presenti di garantire la ripartizione delle azioni orizzontali.

L’analisi e le verifiche devono essere condotte considerando le sollecitazioni e le capacità di tutti gli elementi costruttivi, quali le pareti, i diaframmi di piano, le connessioni tra essi e con gli eventuali presidi di rinforzo (quali ad esempio gli incatenamenti). Nelle scelte di modellazione occorre considerare le incertezze sulle caratteristiche meccaniche delle murature, degli elementi lignei, dei vincoli tra gli elementi strutturali e dei vincoli esterni (ad esempio con edifici in aderenza la cui modellazione esplicita sia omessa). Oltre a ciò, può essere opportuno condurre diverse analisi con modelli alternativi e/o formulare diverse ipotesi nel campo di variabilità dei parametri in gioco.

La verifica della risposta globale di costruzioni esistenti in muratura allo stato limite ultimo può essere eseguita con i metodi dell’analisi lineare o non lineare.

Nell’analisi lineare, per la verifica a **SLV** le sollecitazioni in ciascun elemento sono valutate con un’azione sismica ridotta dal fattore di comportamento $q$; tali sollecitazioni, eventualmente ridistribuite secondo quanto indicato al § 7.8.1.5.2 delle NTC, devono essere verificate con i criteri di resistenza indicati nel seguito.

Nell’analisi non lineare, il controllo della compatibilità tra sollecitazioni e resistenze a livello di singolo elemento è eseguito nel corso dell’analisi stessa e la verifica è effettuata a livello globale attraverso un confronto tra la domanda di spostamento e la corrispondente capacità. Eventuali meccanismi di rottura ritenuti significativi, ma non esplicitamente considerati nell’analisi (ad esempio quelli relativi ad alcuni elementi di connessione), devono essere verificati a posteriori.

Nel caso i diaframmi orizzontali siano di rigidezza trascurabile, ovvero non in grado di garantire una significativa ripartizione delle azioni sismiche tra le diverse pareti murarie, l’analisi globale della risposta sismica può essere effettuata analizzando i singoli setti murari, sottoposti alle azioni di loro competenza in base a una suddivisione per aree di influenza.

Nel caso invece di diaframmi dotati di rigidezza non trascurabile, l’analisi della risposta sismica globale può essere effettuata con uno dei metodi di cui al § 7.3, con le precisazioni e le restrizioni indicate al § 7.8.1.5, delle NTC. In particolare è possibile utilizzare l’analisi statica non lineare assegnando, come distribuzioni principale e secondaria, rispettivamente, la prima distribuzione, sia del Gruppo 1, sia del Gruppo 2, indipendentemente dalla percentuale di massa partecipante sul primo modo. Nel caso di diaframmi di rigidezza finita, non potendosi definire lo spostamento del centro di massa dell’ultimo livello (v. § 7.3.4.2 delle NTC), lo spostamento $d_C$ da assumersi per la curva di capacità può essere coerentemente assunto come lo spostamento medio tra quello delle diverse pareti, pesato con le corrispondenti masse sismiche.

Nella modellazione globale eventuali porzioni di muratura in grado di accoppiare la risposta degli elementi verticali possono essere considerate parte del sistema resistente, quando siano verificate entrambe le seguenti condizioni:

- la porzione considerata sia sorretta da un architrave, da un arco o da una piattabanda strutturalmente efficace, che ne garantisca il sostegno anche nel caso in cui la stessa sia fessurata e danneggiata dal sisma;

- essa sia efficacemente ammorsata alle pareti che la sostengono (ovvero sia possibile confidare in una resistenza orizzontale a trazione, anche se limitata) o si possa instaurare nella porzione un meccanismo resistente a puntone diagonale (ad esempio per la presenza di una catena o di un elemento accoppiato resistente a trazione).

Per le verifiche di sicurezza nei riguardi del comportamento sismico globale, è possibile applicare quanto prescritto dalle NTC per la progettazione delle nuove costruzioni in muratura, con le precisazioni nel seguito riportate.

Nel caso dell’analisi statica non lineare la capacità in spostamento relativa ai diversi stati limite è valutata, sulla curva taglio di base-spostamento, nei modi appresso indicati:

**SLC**: per la definizione della bilineare equivalente, identificata seguendo i criteri indicati al § C.7.3.4.2, lo spostamento ultimo a SLC è dato dal minore tra quelli forniti dalle seguenti due condizioni:

- quello corrispondente ad un taglio di base residuo pari all’80% del massimo;

- quello corrispondente al raggiungimento della soglia limite della deformazione angolare a SLC in tutti i maschi murari verticali di un qualunque livello in una qualunque parete ritenuta significativa ai fini della sicurezza (questo controllo può essere omesso nelle analisi quando i diaframmi siano infinitamente rigidi o quando sia eseguita l’analisi di una singola parete).

**SLV**: lo spostamento ultimo a SLV, sulla bilineare equivalente sopra definita, è pari a ¾ dello spostamento a SLC

**SLD:** lo spostamento corrispondente è il minore tra gli spostamenti ottenuti dalle seguenti due condizioni:

- quello corrispondente al limite elastico della bilineare equivalente, definita a partire dallo spostamento ultimo a SLC;

- quello corrispondente al raggiungimento della resistenza massima a taglio in tutti i maschi murari verticali in un qualunque livello di una qualunque parete ritenuta significativa ai fini dell’uso della costruzione (e comunque non prima dello spostamento per il quale si raggiunge un taglio di base pari a 3/4 del taglio di base massimo).

**SLO:** lo spostamento corrispondente è pari a 2/3 di quello allo SLD.

