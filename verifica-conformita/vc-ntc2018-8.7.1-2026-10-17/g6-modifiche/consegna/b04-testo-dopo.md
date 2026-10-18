La domanda di spostamento, da confrontarsi con le suddette capacità di spostamento ai diversi stati limite, può essere valutata sul sistema bilineare equivalente attraverso le espressioni indicate nel § C.7.3.4.2, valide sia per la risposta in campo non lineare (SLV, con $q^*\le 3$, e SLC, con $q^*\le 4$) che in campo lineare equivalente (SLO e SLD).

Nel caso di analisi dinamica non lineare, le domande di spostamento, per ciascuna direzione e verso, sono rappresentate dalla media dei valori massimi ottenuti applicando un numero significativo di storie temporali, compatibili con le condizioni di pericolosità del sito. Ciascuna domanda di spostamento deve essere confrontata con la corrispondente capacità ottenuta da un’analisi statica non lineare. Quest’ultima può essere definita attraverso un confronto tra le curve forza-spostamento cicliche, ottenute dalle analisi dinamiche, e quelle monotone, ottenute dalle analisi statiche con le due distribuzioni di forze come sopra indicato; in assenza di tale valutazione è possibile considerare la capacità di spostamento minore tra quelle fornite dalle due distribuzioni.

###### *C8.7.1.3.1.1 Pareti murarie*

Nel caso di analisi elastica con il fattore $q$ (analisi lineare statica ed analisi dinamica modale con fattore di comportamento), i valori di calcolo delle resistenze sono ottenuti dividendo i valori medi per i rispettivi fattori di confidenza e per il coefficiente parziale di sicurezza dei materiali (in accordo a quanto indicato al § C8.5); nel caso di analisi non lineare, i valori di calcolo delle resistenze sono ottenuti dividendo i valori medi per i rispettivi fattori di confidenza.

I modelli di capacità degli elementi in muratura sono differenziati in funzione della loro geometria, condizioni al contorno, ruolo strutturale e tipologia muraria. In alcune situazioni è possibile fare riferimento ad elementi maschio (ad asse verticale) ed elementi fascia (ad asse orizzontale), per i quali sono meglio note e più facilmente definibili le capacità in resistenza e in deformazione. Per questi elementi, nel caso di analisi non lineare, è possibile utilizzare un modello bilineare taglio-spostamento, in cui la resistenza è calcolata come la minore tra quelle relative ai diversi possibili meccanismi di rottura e la capacità di spostamento è valutata di conseguenza, attraverso una deformazione angolare limite di elemento.

**Nei maschi murari** i principali meccanismi di rottura nel piano sono:

- pressoflessione;

- taglio-scorrimento;

- taglio con fessurazione diagonale.

Per la verifica a pressoflessione si rimanda al § 7.8.2.2.1 delle NTC, precisando che lo spostamento ultimo è valutato in base alla rotazione della corda nelle due sezioni di estremità $i$ e $j$ del maschio data dalle formule [C8.7.1.13].

$$
\begin{aligned}
\theta_i &= \left\lvert \varphi_i - \frac{u_i-u_0}{h_i}\right\rvert \\
\theta_j &= \left\lvert \varphi_j - \frac{u_0-u_j}{h_j}\right\rvert
\end{aligned}
\tag{C8.7.1.13}
$$

dove (assumendo nel piano della parete una terna destrorsa): $\varphi_i$ e $\varphi_j$ sono le rotazioni, $u_j$ e $u_i$ sono gli spostamenti orizzontali, $u_0$ è lo spostamento orizzontale del punto di flesso, $h_i$ e $h_j$ sono le luci di taglio (essendo $h=h_i+h_j$ l’altezza dell’elemento). Lo spostamento ultimo a SLC è definito in corrispondenza di una rotazione della corda pari a 0,01.

Il criterio di resistenza per la verifica a taglio scorrimento, da valutare nelle sezioni soggette a momento massimo (solitamente le due sezioni di estremità del pannello), è quello indicato al § 7.8.2.2.2 delle NTC, utilizzando i valori di $f_{v0}$ indicati in tabella 8.5.1, con la precisazione che la limitazione $f_{v,lim}$ relativa alla rottura dei blocchi è fornita dalla seguente relazione, ricavata per blocchi di forma standard:

$$
f_{V,lim} = \frac{0.065f_b}{0.7}
\tag{C8.7.1.14}
$$

dove $f_b$ è la resistenza a compressione del blocco, normalizzata. Lo spostamento ultimo a SLC è definito in corrispondenza di una rotazione della corda, calcolata come sopra per la sezione di estremità di verifica, pari a 0.005.

Per le verifiche a taglio con fessurazione diagonale si rinvia ai due meccanismi di rottura definiti nel seguito.

**Nelle fasce di piano** i possibili meccanismi di rottura nel piano sono:

- pressoflessione;

- taglio con fessurazione diagonale.

**Per le valutazioni relative alla pressoflessione** nelle fasce, un aspetto critico della modellazione è la valutazione dell’azione assiale, influenzata dall’interazione con i diaframmi orizzontali (in taluni modelli assunti rigidi) e dall’interazione cinematica tra rotazione e deformazione assiale nelle fasce stesse (trascurata nei modelli a trave). Nel caso in cui siano presenti elementi orizzontali dotati di resistenza a trazione (catene, cordoli), accoppiati alla fascia, si può fare utile riferimento al § 7.8.2.2.4 delle NTC.

Diversamente dal caso dei maschi, il dominio di resistenza a pressoflessione per le fasce può essere determinato tenendo conto della resistenza a trazione ($f_{ftd}$) che si genera nelle sezioni di estremità per effetto dell’ingranamento con le porzioni di muratura adiacenti. I meccanismi di rottura possono coinvolgere la resistenza per trazione dei blocchi $f_{btd}$ o avvenire per scorrimento lungo i giunti orizzontali; la resistenza a trazione orizzontale è quindi data dall’espressione:

$$
f_{ftd} = min\left(\frac{f_{btd}}{2};\,f_{v0d}+\frac{\mu\sigma_y}{\Phi}\right)
\tag{C8.7.1.15}
$$

dove $\sigma_y$ è la tensione normale media agente sui giunti orizzontali nella sezione d’estremità; $f_{v0d}$ è la resistenza a taglio della muratura in assenza di tensioni normali (che cautelativamente in questo contesto può essere trascurata); $\mu$ è il coefficiente d’attrito locale del giunto; $\phi$ è il coefficiente di ingranamento murario, già definito nella equazione [C8.7.1.2].

In assenza di valutazioni più accurate, $\sigma_y$ può essere stimata pari a metà della tensione normale media $\sigma_0$ agente nei maschi adiacenti. Stimata la resistenza a trazione della fascia $f_{ft}$, il dominio di resistenza a pressoflessione $M-N$ può essere calcolato ipotizzando la conservazione della sezione piana e un legame tensione-deformazione elastoplastico a compressione ed elastofragile a trazione, nel caso di rottura dei blocchi, elastoplastico, eventualmente a duttilità controllata, nel caso di rottura per scorrimento dei giunti. Per la resistenza a compressione occorre valutare quella in direzione orizzontale $f_h$, usualmente inferiore a quella in direzione verticale. Considerato che per le fasce il modello globale non è usualmente in grado di valutare in modo affidabile l’azione assiale orizzontale, la resistenza per pressoflessione può essere calcolata in via cautelativa assumendo $N=0$.

Lo spostamento ultimo a SLC è valutato calcolando la deformazione angolare nelle due sezioni di estremità del pannello secondo la [C8.7.1.13], eventualmente assumendo che il punto di flesso sia a metà dell’elemento; la soglia limite è pari a 0,02, in presenza di elemento orizzontale resistente a trazione accoppiato alla fascia, 0,015 negli altri casi.

**Per le valutazioni relative al taglio,** sia nei maschi, sia nelle fasce, si distinguono due famiglie di murature:

- le murature a tessitura irregolare, con rottura per trazione diagonale governata dal parametro $\tau_0$;

- le murature a tessitura regolare, per le quali la fessurazione può essere “a scaletta”, ossia con andamento diagonale
attraverso i giunti di malta (governata dal parametro di resistenza $f_{v0}$, associato idealmente alla crisi dei giunti), oppure diagonale attraverso gli inerti della muratura (governata dal parametro di resistenza $f_{v,lim}$).

La Tabella C8.5.I, fornendo valori di riferimento per $\tau_0$ e $f_{v0}$, suggerisce quale criterio adottare in funzione della tipologia muraria; per la tipologia “muratura in mattoni pieni e malta di calce” è possibile utilizzare, sulla base delle caratteristiche specifiche rilevate dal progettista, alternativamente uno dei due metodi.

**Nel caso di muratura irregolare**, la resistenza a taglio di calcolo per azioni nel piano del pannello può essere valutata con la relazione seguente:

$$
V_t = l \cdot t\,\frac{1.5\tau_{0d}}{b}\sqrt{1+\frac{\sigma_0}{1.5\tau_{0d}}}
= l \cdot t\,\frac{f_{td}}{b}\sqrt{1+\frac{\sigma_0}{f_{td}}}
\tag{C8.7.1.16}
$$

dove:

- $l$ è la lunghezza del pannello

- $t$ è lo spessore del pannello

- $\sigma_0$ è la tensione normale media, riferita all’area totale della sezione ($=P/lt$, con $P$ forza assiale agente, positiva se di compressione)

- $f_{td}$ e $\tau_{0d}$ sono, rispettivamente, i valori di calcolo della resistenza a trazione per fessurazione diagonale e della corrispondente resistenza a taglio di riferimento della muratura ($f_t=1{,}5\tau_0$); nel caso in cui tale parametro sia desunto da prove di compressione diagonale, la resistenza a trazione per fessurazione diagonale $f_t$ si assume pari al carico diagonale di rottura diviso per due volte la sezione media del pannello sperimentato valutata come $t(l+h)/2$, con $t$, $l$ e $h$ rispettivamente spessore, base e altezza del pannello.

- $b$ è un coefficiente correttivo legato alla distribuzione degli sforzi sulla sezione, dipendente dalla snellezza della parete. Si può assumere $b=h/l$, comunque non superiore a 1,5 e non inferiore a 1, dove $h$ è l'altezza del pannello.

Nel caso dei maschi la soglia limite della deformazione angolare a SLC è pari a 0,005 e, in assenza di più precise formulazioni, la deformazione angolare rappresentativa di un pannello soggetto a taglio per fessurazione diagonale può essere valutata a partire dai valori della rotazione della corda nei due estremi $i$ e $j$ (v. formula [C8.7.1.13]).

Nel caso delle fasce di piano, la resistenza a taglio può essere valutata con la formula [C8.7.1.16], nella quale la tensione media di compressione $\sigma_0$, che può essere usualmente trascurata, è la maggiore tra quella orizzontale, se nota in maniera affidabile dal modello di calcolo, e quella verticale, valutabile a partire dai carichi eventualmente trasmessi dai solai e dalla diffusione delle tensioni verticali nei maschi murari adiacenti.

Raggiunto, allo **SLC**, il valore limite della deformazione angolare sopra indicato per i maschi, la presenza di un architrave efficace consente di mantenere una resistenza a taglio residua anche per valori di deformazione angolare superiori a 0,015.

Qualora nel modello si considerassero anche le resistenze residue, in assenza di formulazioni più accurate, si possono adottare valori della resistenza residua, come frazione di quella massima fornita dalla [C8.7.1.16], pari a:

- architrave in calcestruzzo armato o in profilato d’acciaio, purché appoggiato per una significativa estensione nella muratura: 60%;

- architrave in legno, di buone caratteristiche e ben ammorsato: 40%;

- arco in muratura: 10%.

Il contributo della resistenza residua può eventualmente essere messo in conto attraverso un legame costitutivo multilineare, che simula la riduzione di resistenza in corrispondenza di una deformazione angolare pari a 0,005, o ancora con un modello bilineare ma assegnando alla fascia direttamente una resistenza pari a quella residua e assumendo un valore di deformazione angolare ultimo pari a 0,015.

**Nel caso di muratura regolare**, la resistenza a taglio può essere ottenuta dalla relazione semplificata, indicata per la muratura irregolare che risulterà generalmente più cautelativa, oppure dalla relazione più completa riportata nel seguito:

$$
V_t = \frac{lt}{b}\left(\tilde f_{v0d}+\tilde\mu\sigma_0\right)
= \frac{lt}{b}\left(\frac{f_{v0d}}{1+\mu\phi}+\frac{\mu}{1+\mu\phi}\sigma_0\right)
\le V_{t,lim}
\tag{C8.7.1.17}
$$

dove: $\tilde f_{v0d}$ è la resistenza equivalente a taglio della muratura e $\tilde\mu$ è un coefficiente di attrito equivalente, funzione dei parametri di resistenza locale del giunto (coesione, assunta convenzionalmente pari alla resistenza a taglio della muratura in assenza di tensioni normali $f_{v0}$, e $\mu$, coefficiente d’attrito) e della tessitura attraverso il coefficiente di ingranamento murario $\phi$, definito come rapporto tra l’altezza del blocco e la lunghezza di sovrapposizione minima dei blocchi di due corsi successivi (tale parametro rappresenta la tangente dell’angolo medio di inclinazione della fessura diagonale “a scaletta” e può essere stimato sulla base del rilievo della tessitura del paramento murario).

In assenza di valutazioni più accurate, il coefficiente di attrito locale $\mu$ può essere assunto pari a 0,577 (corrispondente ad un angolo di attrito di 30°); ciò porta a valori del coefficiente di attrito equivalente $\tilde\mu$ variabili da circa 0,4 (per murature con buona tessitura) a 0,2 (per murature con blocchi scarsamente ammorsati). Si noti, a titolo di esempio, che questo criterio di resistenza è in grado di distinguere la diversa vulnerabilità, a parità di malta e di mattoni, di un paramento costruito con mattoni disposti “per lungo” o “di lista”, in quanto presenta normalmente una diversa inclinazione della fessura a scaletta.

$V_{t,lim}$ è un valore limite che può essere stimato, in via approssimata, in funzione della rottura a trazione dei blocchi $f_{btd}$, e tenendo conto della geometria del pannello, attraverso l’espressione, ricavata per blocchi di forma standard:

$$
V_{t,lim} = \frac{lt}{b}\frac{f_{btd}}{2.3}\sqrt{1+\frac{\sigma_0}{f_{btd}}}
\tag{C8.7.1.18}
$$

dove $f_{btd}$ può essere ricavata da dati di letteratura o attraverso prove di caratterizzazione diretta in laboratorio su campioni prelevati in sito, eventualmente stimandola a partire dalla resistenza a compressione del blocco $f_b$, come $f_{bt}=0{,}1f_b$.

Lo spostamento ultimo a SLC è definito valutando la deformazione angolare rappresentativa come nel caso della rottura a taglio per trazione diagonale e assumendo per le tipologie murarie riportate in Tabella C8.5.I una soglia limite pari a 0,005. Nel caso invece di murature di tipologia moderna, ovvero costituite da blocchi forati, la soglia limite è pari a 0,004.

Nel caso delle fasce di piano valgono le precisazioni riportate per la rottura a taglio per trazione diagonale, relativamente alla valutazione della tensione media di compressione $\sigma_0$ e al calcolo della resistenza residua.

###### *C8.7.1.3.1.2 Solai e coperture*

I solai possono essere considerati infinitamente rigidi e resistenti nel loro piano nei casi in cui esistano effettivi elementi strutturali atti a impedirne le deformazioni, così come indicato al § 7.2.6 delle NTC, salvo valutazioni più accurate della reale situazione svolte dal progettista. Le indicazioni del § 7.2.6 costituiscono un utile riferimento comparativo ad altre tipologie al fine di decidere se attribuire al diaframma la condizione di infinita rigidezza nel proprio piano.

Le volte, proprio a causa delle incertezze sulla loro capacità di trasferire le sollecitazioni sismiche alle pareti, non possono essere considerate capaci di svolgere la funzione di diaframma di piano, salvo venga dimostrata e quantificata la loro capacità in tal senso.

##### C8.7.1.3.2 Edifici in aggregato

Un aggregato edilizio di edifici[^4] è il risultato di una genesi articolata e sovente non unitaria, dovuta a molteplici fattori (sequenza costruttiva, uso di materiali diversi, mutate esigenze, etc.). Nell’analisi di un aggregato edilizio occorre individuare, in via preliminare, le Unità Strutturali (**US**) che compongono l’aggregato, evidenziando le azioni che su ciascuna di esse possono derivare dalle Unità Strutturali contigue. Ove necessario, tale analisi preliminare può estendersi all’intero aggregato, al fine di individuare le relazioni tra ciascuna **US** e il resto dell’aggregato, con particolare attenzione al contesto ed ai meccanismi di giustapposizione e di sovrapposizione.

[^4]: Nell’analisi degli aggregati, al concetto di edificio si preferisce sostituire il concetto di Unità Strutturale (US), chiaramente definito e individuato negli ultimi capoversi del § 8.7.1 delle NTC.

La porzione di aggregato che costituisce l’**US** comprende cellule tra loro legate in elevazione ed in pianta da un comune processo costruttivo, e considera tutti gli elementi interessati dalla trasmissione a terra dei carichi verticali.

In particolare, il processo di indagine sugli aggregati edilizi si dovrebbe sviluppare, ove significativo in relazione alle verifiche da effettuare e/o agli interventi previsti, attraverso l’individuazione di diversi strati d’informazione:

- i rapporti tra i processi di aggregazione ed organizzazione dei tessuti edilizi;

- i principali eventi che hanno influito sugli aspetti morfologici del costruito storico (fonti storiche);

- la disposizione e la gerarchia dei cortili ed il posizionamento delle scale;

- l’allineamento delle pareti (con particolare riferimento alle facciate, al disassamento dei fronti ed ai flessi planimetrici);

- i rapporti spaziali elementari delle singole cellule murarie, nonché i rapporti di regolarità, ripetizione, modularità, ai
diversi piani, al fine di distinguere le cellule originare da quelle realizzate successivamente;

- la forma e la posizione delle aperture nelle pareti: loro assialità, simmetria e ripetizione al fine di individuare il percorso di
trasmissione degli sforzi e la sua evoluzione nel tempo;

- i disassamenti e le rastremazioni delle pareti, i muri poggianti “in falso” sui solai sottostanti, le differenze di quota tra
solai contigui.

L’**US** è caratterizzata da comportamento strutturale unitario nei confronti dei carichi orizzontali e verticali per cui, nell’individuarla, si terrà conto della tipologia costruttiva e del permanere di elementi caratterizzanti, anche al fine di definire interventi coerenti con la configurazione strutturale.

L’**US** deve comunque garantire con continuità il trasferimento dei carichi in fondazione e, generalmente, è delimitata o da spazi aperti, o da giunti strutturali, o da edifici contigui costruiti, ad esempio, con tipologie costruttive e strutturali diverse, o con materiali diversi, oppure in epoche diverse.

Tra le interazioni strutturali con gli edifici adiacenti occorre considerare: le azioni (sia verticali che orizzontali) provenienti da solai o da pareti di **US** adiacenti; le spinte di archi e volte appartenenti ad **US** contigue; le spinte provenienti da archi di contrasto o da tiranti ancorati su altri edifici; i martellamenti tra **US** adiacenti.

Ove necessario, occorre anche considerare gli effetti di: spinte causate da orizzontamenti sfalsati di quota sulle pareti in comune con le **US** adiacenti; effetti locali causati da disallineamenti dei prospetti, differenze di altezza o di rigidezza tra **US** adiacenti; azioni di ribaltamento e di traslazione nelle **US** di testata.

L'analisi di una **US** secondo i metodi utilizzati per edifici isolati, se effettuata modellando in maniera approssimata (o addirittura trascurando) l'interazione con i corpi di fabbrica adiacenti, assume un significato largamente convenzionale, per cui la determinazione della capacità sismica globale dell'**US** può essere eseguita attraverso metodologie semplificate.

Qualora i solai dell'edificio siano di rigidezza trascurabile si può procedere all'analisi delle singole pareti dell’**US**, ciascuna analizzata come struttura indipendente, soggetta ai carichi verticali di competenza ed all'azione del sisma nella direzione parallela alla parete; nel caso in cui la parete oggetto di verifica abbia continuità con quella di una **US** adiacente (ad esempio nel caso delle facciate di aggregati in linea) è necessario stimare se l’azione sismica da prendere in considerazione non debba essere incrementata rispetto a quella derivante dalle sole masse dell’**US** in esame (fatto che, ad esempio, si verifica nelle **US** di angolo o di testata). L'analisi e le verifiche di ogni singola parete seguono i criteri esposti nei punti precedenti.

Nel caso di solai infinitamente rigidi o di rigidezza significativa, la verifica agli stati limite ultimi e/o di esercizio di una **US** in aggregato può essere svolta, anche per edifici con più di due piani, mediante l'analisi statica non lineare analizzando e verificando separatamente ciascun interpiano dell'edificio e trascurando la variazione della forza assiale nei maschi murari dovuta all'effetto dell'azione sismica. Con l'esclusione di unità strutturali d'angolo o di testata, così come di parti di edificio non vincolate o non aderenti su più lati alle **US** contigue (es. piani superiori di un edificio di maggiore altezza rispetto alle **US** adiacenti), l'analisi può anche essere svolta trascurando gli effetti torsionali, ipotizzando che i solai, infinitamente rigidi, possano unicamente traslare nella direzione considerata dell'azione sismica.

##### C8.7.1.3.3 Edifici semplici

Sulle costruzioni esistenti è possibile eseguire interventi che consentano di assimilare la costruzione ad un edificio semplice. In tali casi l’intervento è volto a soddisfare le regole di cui al § 7.8.1.9 delle NTC; facendo riferimento al posto della resistenza caratteristica a compressione $f_k$, al valore medio $f_m$, diviso per il fattore di confidenza. Oltre alle condizioni sopra indicate è necessario che, dopo l’eventuale intervento, risulti verificato anche quanto segue:

- a. i solai siano in grado di svolgere la funzione di diaframma di piano, siano ben collegati alle pareti e siano in grado di evitare il ribaltamento delle pareti fuori dal loro piano;

- b. tutte le aperture abbiano architravi dotati di adeguata resistenza flessionale;

- c. tutti gli elementi spingenti, comprese le coperture a falda, eventualmente presenti siano dotati di accorgimenti atti ad eliminare o equilibrare le spinte orizzontali e a inibire lo scivolamento dei vari elementi (es. presenza di connessioni quali chiodi, viti o staffe tra tutti gli elementi delle coperture a falda con struttura lignea);

- d. tutti gli elementi ad elevata vulnerabilità, anche non strutturali, siano stati eliminati o resi sicuri (ad esempio comignoli, cornicioni ecc.);

- e. le pareti ortogonali siano tra loro ben collegate;

- f. le murature non siano a sacco o a doppio paramento o, in generale, di cattiva qualità e scarsa resistenza (es. muratura in “forati”, muratura con pietre tondeggianti di fiume o pareti di spessore chiaramente insufficiente).

Se l’intervento rispetta tutto quanto sopra descritto, lo stesso potrà essere considerato come un intervento di adeguamento e sarà possibile omettere le analisi ante e post intervento.

#### C8.7.1.4 ELEMENTI STRUTTURALI IN LEGNO

I collegamenti tra differenti elementi lignei devono essere ripristinati nella loro funzionalità statica, mantenendo valori di rigidezza simili a quelli posseduti dalla struttura originaria, a meno di evidenti riconosciute carenze strutturali/costruttive.

Il ripristino della continuità strutturale tra parti diverse di uno stesso elemento può essere realizzato mediante collegamenti tradizionali a secco utilizzando, quando possibile, elementi lignei o, in alternativa, metallici o altri riconosciuti idonei. Adesivi strutturali, in alternativa a collegamenti meccanici, possono essere usati con cautela e comunque non per trasmettere tensioni di trazione ortogonali al piano di incollaggio.

Nell’intervenire su elementi lignei è opportuno garantire la possibilità di variazione dimensionale dell'elemento a seguito di variazioni di umidità, per evitare stati di coazione. Sono da evitarsi interventi che producano manomissioni delle fessure longitudinali da ritiro (cretti) o che impediscano, in qualsiasi modo, dilatazioni e ritiri trasversali del legno.

Nella definizione dello schema strutturale occorre tenere conto, in generale, anche degli altri elementi che possono interferire, a livello di comportamento globale, con la struttura lignea in esame, considerando, ove necessario, anche dei possibili effetti sul comportamento dell’intero edificio. A tale riguardo si deve anche osservare che, generalmente, la struttura lignea costituisce parte essenziale nel comportamento statico di insieme dell'edificio. Conseguentemente, modificazioni staticamente importanti della struttura lignea necessitano di valutazioni complessive atte a valutare l'interazione tra elementi lignei e non lignei nonché l'effettivo contributo delle stesse membrature lignee al comportamento strutturale globale.
