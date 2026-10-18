$$
\theta_y = \phi_y\frac{L_V}{3} + 0{,}0013\left(1+1{,}5\frac{h}{L_V}\right)
+ 0{,}13\phi_y\frac{d_bf_y}{\sqrt{f_c}}
\tag{C8.7.2.7a}
$$

per pareti

$$
\theta_y = \phi_y\frac{L_V}{3} + 0{,}002\left(1-0{,}125\frac{L_V}{h}\right)
+ 0{,}13\phi_y\frac{d_bf_y}{\sqrt{f_c}}
\tag{C8.7.2.7b}
$$

dove $\phi_y$ è la curvatura al raggiungimento della tensione di snervamento della sezione terminale, $h$ l’altezza della sezione, $d_b$ è il diametro (medio) delle barre longitudinali, ed $f_c$ e $f_y$ sono rispettivamente la resistenza a compressione del calcestruzzo e la tensione di snervamento dell’acciaio longitudinale in [MPa], ottenute come media delle prove eseguite in sito e da fonti aggiuntive di informazione, divise per il fattore di confidenza appropriato in relazione al Livello di Conoscenza raggiunto.

##### C8.7.2.3.5 Travi e pilastri: taglio

Per la valutazione delle resistenze ultime di elementi monodimensionali nei confronti di sollecitazioni taglianti dovute ai soli carichi gravitazionali, vale quanto indicato per le condizioni non sismiche al § 4.1.2.3.5 delle NTC, facendo in generale riferimento al § 4.1.2.3.5.2, considerando per le travi il contributo delle barre di armatura piegate ove presenti.

Per le azioni sismiche, occorre considerare la riduzione di resistenza a taglio in condizioni cicliche in funzione della domanda di duttilità sull’elemento, per il livello di azione considerato. La domanda massima a taglio nell’elemento può essere determinata, indipendentemente dal livello di azione considerato, a partire dai momenti resistenti nelle sezioni di estremità, valutati amplificando le resistenze medie dei materiali tramite il fattore di confidenza appropriato in relazione al Livello di Conoscenza raggiunto.

La resistenza a taglio $V_R$ in condizioni cicliche, quali quelle sismiche, può essere valutata sulla base dei tre contributi dovuti all’entità dello sforzo normale $N$, al calcestruzzo e all’acciaio, nonché dell’interazione con la rotazione flessionale dell’elemento in funzione della parte plastica della domanda di duttilità, $\mu_{\Delta,pl}$.

$$
\begin{aligned}
V_R = \frac{1}{\gamma_{el}}\Bigg[&\frac{h-x}{2L_V}\min\left(N;0.55A_cf_c\right) \\
&+ \left(1-0.05\min\left(0.5;\mu_{\Delta,pl}\right)\right)
\left[0.16\max\left(0.5;100\rho_{tot}\right)
\left(1-0.16\min\left(5;\frac{L_V}{h}\right)\right)\sqrt{f_c}A_c+V_W\right]\Bigg]
\end{aligned}
\tag{C8.7.2.8}
$$

(unità di misura MN, m) dove:

- $\gamma_{el}=1.15$ per gli elementi primari ed 1.0 per gli elementi secondari (come definiti al § 7.2.3 delle NTC);

- $h$ è l'altezza totale della sezione;

- $x$ è l'altezza della zona compressa della sezione (profondità dell'asse neutro);

- $N$ è lo sforzo normale di compressione (assunto pari a zero se di trazione);

- $L_V$ è la luce di taglio;

- $A_c$ è l'area della sezione pari a $(b\times d)$ per la sezione rettangolare e $\pi D_c^2/4$ per quella circolare (dove $D_c=D-2c-d_{bw}$, essendo $D$ il diametro della sezione, $c$ il copriferro, $d_{bw}$ il diametro delle staffe);

- $f_c$ è la resistenza a compressione del calcestruzzo ottenuta come media delle prove eseguite in sito, eventualmente corretta sulla base di fonti aggiuntive di informazione, divisa per il fattore di confidenza appropriato in relazione al Livello di Conoscenza raggiunto; per gli elementi sismici primari il valore di $f_c$ deve essere ulteriormente diviso per il relativo coefficiente parziale;

- $\rho_{tot}$ è la percentuale geometrica totale di armatura longitudinale;

- $V_w$ è il contributo dell'armatura trasversale per la resistenza a taglio definito come segue:

- sezioni rettangolari:

$$
V_W = \rho_{sx}b_wzf_y
\tag{C8.7.2.9}
$$

dove, oltre al significato dei simboli già noti, z è il braccio delle forze interne.

- per le sezioni circolari:

$$
V_W = \frac{\pi}{2}\frac{A_{sx}}{s}f_{yw}(D-2c)
\tag{C8.7.2.10}
$$

Il valore della resistenza a taglio fornito dalla (8.7.2.8) non può essere assunto maggiore del valore della resistenza a “taglio compressione”, valutata come per le condizioni non sismiche (Eq. [4.1.28] delle NTC), utilizzando $\theta=45^\circ$ ed assumendo $f_{cd}$ pari alla resistenza media del calcestruzzo divisa per il fattore di confidenza appropriato in relazione al Livello di Conoscenza raggiunto e per il coefficiente parziale del materiale.

Nella [8.7.2.8] $\mu_{\Delta,pl}$ rappresenta la parte plastica della domanda di duttilità ed è espressa dalla relazione: $\mu_{\Delta,pl}=\mu_\Delta-1$, dove $\mu_\Delta$ è la domanda di duttilità espressa come rapporto tra la rotazione massima $\theta_m$ per il livello di azione sismica considerato e la rotazione di prima plasticizzazione $\theta_y$. Ove necessario, la relazione tra duttilità di rotazione e duttilità di curvatura si ottiene dalla [8.7.2.7], con $\phi_m$ al posto di $\phi_u$, essendo $\phi_m$ la domanda di curvatura massima per il livello di azione considerato.

Nella [8.7.2.8], in assenza di specifiche valutazioni, l'altezza della zona compressa della sezione può essere calcolata in maniera semplificata attraverso la relazione: $x/h=0{,}25+0{,}85N/(A_c\cdot f_c)\le1$.

La resistenza a taglio in condizioni sismiche può essere valutata come indicato nel seguito.

Quando la domanda di duttilità $\mu_\Delta$ dell’elemento è inferiore a 2, la resistenza a taglio è data dalla maggiore tra la resistenza a taglio con armatura trasversale per le condizioni non sismiche (Eq. [4.1.29] delle NTC) e la resistenza a taglio ciclica fornita dalla [8.7.2.8]. Quando $\mu_\Delta>3$, la resistenza a taglio è quella relativa alle condizioni cicliche, valutata attraverso la [8.7.2.8]. Per le situazioni intermedie, si interpola linearmente tra la resistenza a taglio per $\mu_\Delta=2$ e quella ottenuta in base alla [8.7.2.8] per $\mu_\Delta=3$.

Per i carichi gravitazionali e, in generale, quando la domanda di duttilità $\mu_\Delta$ dell’elemento è inferiore a 1, la resistenza a taglio può essere valutata, alternativamente, come per gli elementi senza armature trasversali resistenti a taglio (§ 4.1.2.3.5.1 delle NTC).

In questo caso si deve verificare che, per l’azione considerata, la domanda a flessione o a pressoflessione non superi la corrispondente capacità al limite elastico (momento di prima plasticizzazione come definito al § 4.1.2.3.4.2 delle NTC) in entrambe le direzioni principali della sezione. Nel caso in cui si adottino metodi di analisi lineari, la domanda dovuta alle azioni sismiche deve essere valutata con riferimento al fattore di comportamento $q\le1{,}5$.

In condizioni sismiche, un approccio prudenziale suggerisce che la resistenza a taglio valutata con riferimento agli elementi senza armature trasversali venga considerata esclusivamente per le strutture in cui la domanda plastica sia in ogni caso contenuta, ad es. grazie all’uso di tecniche di protezione passiva quali i controventi (elastici o dissipativi) o l’isolamento sismico.

Nel caso di rinforzi di edifici esistenti, la messa in opera dei controventi dissipativi comporta problematiche e difficoltà differenti a seconda del tipo di struttura. Particolarmente negli edifici in cemento armato occorre curare la connessione con i telai, verificando correttamente le sollecitazioni trasmesse alle membrature esistenti e eventualmente predisponendo sistemi di ridistribuzione degli sforzi di taglio nei pilastri e di trazione nelle travi e negli orizzontamenti, utilizzando opportuni tiranti e piastre di ancoraggio.

***Nodi trave-pilastro***

La verifica di resistenza deve essere eseguita solo per i nodi non interamente confinati come definiti al § 7.4.4.3 delle NTC. Deve essere verificata sia la resistenza a trazione diagonale che quella a compressione diagonale. Per la verifica si possono adottare le seguenti espressioni:

- per la resistenza a trazione:

$$
\sigma_{jt} = \left\lvert\frac{N}{2A_j} - \sqrt{\left(\frac{N}{2A_j}\right)^2+\left(\frac{V_j}{A_j}\right)^2}\right\rvert
\le 0.3\sqrt{f_c}\,(f_c\,\text{in MPa})
\tag{C8.7.2.11}
$$

- per la resistenza a compressione:

$$
\sigma_{jc} = \frac{N}{2A_j} + \sqrt{\left(\frac{N}{2A_j}\right)^2+\left(\frac{V_j}{A_j}\right)^2}
\le 0.5f_c\,(f_c\,\text{in MPa})
\tag{C8.7.2.12}
$$

dove $N$ indica l’azione assiale presente nel pilastro superiore, $V_j$indica il taglio totale agente sul nodo, ottenuto come somma algebrica del taglio trasmesso dal pilastro superiore e degli sforzi orizzontali trasmessi dalle parti superiori delle travi, $A_j = b_j h_{jc}$ dove $b_j$ e $h_{jc}$ sono stati definiti al § 7.4.4.3.1 della norma. Le resistenze dei materiali sono ottenute come media delle prove eseguite in sito e da fonti aggiuntive di informazione, divise per il fattore di confidenza appropriato in relazione al Livello di Conoscenza raggiunto e per il coefficiente parziale del materiale.

#### C8.7.2.4 MODELLI DI CAPACITÀ PER LA VALUTAZIONE DI EDIFICI DI ACCIAIO

##### C8.7.2.4.1 Travi e pilastri: flessione con e senza sforzo normale

La capacità in termini di deformazione di travi e pilastri è definita con riferimento alla rotazione totale rispetto alla corda $\theta$ analogamente a quanto già descritto per le strutture di c.a. (v. § C8.7.2.3).

##### C8.7.2.4.2 Stato limite di prevenzione del collasso

Allo **SLC** la capacità in termini di rotazione rispetto alla corda può essere valutata utilizzando modelli numerici che tengano in debito conto le non linearità geometriche e meccaniche del materiale, ovvero sulla base delle indicazioni riportate in documenti di comprovata validità. È possibile riferirsi all’*Annex B (Steel and composite structures)* della Norma UNI EN 1998-3:2005. In particolare il punto B.5.2 –*member deformation capacities*, analizza il problema delle travi e colonne soggette a flessione, per le quali la capacità di deformazione inelastica è espressa in termini di rotazione plastica definita come multiplo della rotazione rispetto alla corda $\theta_y$ valutata al raggiungimento della tensione di snervamento. Il valore del moltiplicatore della rotazione $\theta_y$ dipende dallo stato limite considerato e dalla classe della sezione trasversale della trave o della colonna (classi 1 o 2, definite al § 4.2.3.1 delle NTC). Lo stesso Annesso riporta i moltiplicatori che consentono di determinare la capacità di elementi di controvento soggetti a compressione in termini di moltiplicatore dello sforzo normale corrispondente allo stato limite di instabilità, o di elementi di controvento tesi, in termini di moltiplicatore dello sforzo normale corrispondente al raggiungimento della tensione di snervamento del materiale.

##### C8.7.2.4.3 Stato limite di salvaguardia della vita

Allo stato limite di salvaguardia della vita, la capacità in termini di rotazione totale rispetto alla corda, $\theta_{SD}$, può essere assunta pari a 3/4 del valore $\theta_u$ valutato per lo **SLC**.

##### C8.7.2.4.4 Stato limite di danno

Allo stato limite di esercizio, la capacità in termini di rotazione rispetto alla corda, $\theta_y$, al raggiungimento della tensione di snervamento può essere valutata mediante la seguente espressione:

$$
\theta_y = \frac{M_{e.Rd}L_V}{2EI}
\tag{C8.7.2.13}
$$

dove:

- $M_{e,Rd}$ è il momento di prima plasticizzazione di calcolo;

- $L_V$ è la luce di taglio;

- $I$ è il momento di inerzia della sezione nella direzione considerata.

##### C8.7.2.4.5 Travi e pilastri: Taglio

La capacità in termini di resistenza a taglio $V_R$ si valuta come per il caso di nuove costruzioni per situazioni non sismiche.

##### C8.7.2.4.6 Collegamenti

Si applica quanto prescritto per gli edifici di nuova costruzione.
