# 3.5. AZIONI DELLA TEMPERATURA

# 3.5.1. GENERALITÀ

Variazioni giornaliere e stagionali della temperatura esterna, irraggiamento solare e convezione comportano variazioni della distribuzione di temperatura nei singoli elementi strutturali.

La severità delle azioni termiche è in generale influenzata da più fattori, quali le condizioni climatiche del sito, l'esposizione, la massa complessiva della struttura e la eventuale presenza di elementi non strutturali isolanti.

# 3.5.2. TEMPERATURA DELL’ARIA ESTERNA

La temperatura dell'aria esterna, $T_{est}$, può assumere il valore $T_{max}$ o $T_{min}$, definite rispettivamente come temperatura massima estiva e minima invernale dell'aria nel sito della costruzione, con riferimento ad un periodo di ritorno di 50 anni.

Per un'opera di nuova realizzazione in fase di costruzione o per le fasi transitorie relative ad interventi sulle costruzioni esistenti, il periodo di ritorno dell'azione potrà essere ridotto come di seguito specificato:

- per fasi di costruzione o fasi transitorie con durata prevista in sede di progetto non superiore a tre mesi, si assumerà $T_R$ ≥ 5 anni;
- per fasi di costruzione o fasi transitorie con durata prevista in sede di progetto compresa fra tre mesi ed un anno, si assumerà $T_R$ ≥ 10 anni.

In mancanza di adeguate indagini statistiche basate su dati specifici relativi al sito in esame, $T_{max}$ o $T_{min}$ dovranno essere calcolati in base alle espressioni riportate nel seguito, per le varie zone indicate nella Fig. 3.5.1. Tale zonazione non tiene conto di aspetti specifici e locali che, se necessario, dovranno essere definiti singolarmente.

![Fig. 3.5.1 - Zone della temperatura dell'aria esterna](img/fig-3.5.1-zone-temperatura-mappa.png)

**Fig. 3.5.1** - *Zone della temperatura dell'aria esterna*

Nelle espressioni seguenti, $T_{max}$ o $T_{min}$ sono espressi in °C; l'altitudine di riferimento $a_s$ (espressa in m) è la quota del suolo sul livello del mare nel sito dove è realizzata la costruzione.

**Zona I**

Valle d'Aosta, Piemonte, Lombardia, Trentino-Alto Adige, Veneto, Friuli-Venezia Giulia, Emilia Romagna:

$$T_{min} = -15 - 4 \cdot a_s / 1000 \tag{3.5.1}$$

$$T_{max} = 42 - 6 \cdot a_s / 1000 \tag{3.5.2}$$

**Zona II**

Liguria, Toscana, Umbria, Lazio, Sardegna, Campania, Basilicata:

$$T_{min} = -8 - 6 \cdot a_s / 1000 \tag{3.5.3}$$

$$T_{max} = 42 - 2 \cdot a_s / 1000 \tag{3.5.4}$$

**Zona III**

Marche, Abruzzo, Molise, Puglia:

$$T_{min} = -8 - 7 \cdot a_s / 1000 \tag{3.5.5}$$

$$T_{max} = 42 - 0.3 \cdot a_s / 1000 \tag{3.5.6}$$

**Zona IV**

Calabria, Sicilia:

$$T_{min} = -2 - 9 \cdot a_s / 1000 \tag{3.5.7}$$

$$T_{max} = 42 - 2 \cdot a_s / 1000 \tag{3.5.8}$$

# 3.5.3. TEMPERATURA DELL'ARIA INTERNA

In mancanza di più precise valutazioni, legate alla tipologia della costruzione ed alla sua destinazione d'uso, la temperatura dell'aria interna, $T_{int}$, può essere assunta pari a 20 °C.

# 3.5.4. DISTRIBUZIONE DELLA TEMPERATURA NEGLI ELEMENTI STRUTTURALI

Il campo di temperatura sulla sezione di un elemento strutturale monodimensionale con asse longitudinale x può essere in generale descritto mediante:

*a)* la componente uniforme $\Delta T_u = T - T_0$ pari alla differenza tra la temperatura media attuale T e quella iniziale alla data della costruzione $T_0$;

*b)* le componenti variabili con legge lineare secondo gli assi principali y e z della sezione, $\Delta T_{My}$ e $\Delta T_{Mz}$.

Nel caso di strutture soggette ad elevati gradienti termici si dovrà tener conto degli effetti indotti dall'andamento non lineare della temperatura all'interno delle sezioni.

La temperatura media attuale T può essere valutata come media tra la temperatura della superficie esterna $T_{sup,est}$ e quella della superficie interna dell'elemento considerato, $T_{sup,int}$.

Le temperature della superficie esterna, $T_{sup,est}$, e quella della superficie interna $T_{sup,int}$, dell'elemento considerato vengono valutate a partire dalla temperatura dell'aria esterna, $T_{est}$, e di quella interna, $T_{int}$, tenendo conto del trasferimento di calore per irraggiamento e per convezione all'interfaccia aria-costruzione e della eventuale presenza di materiale isolante (vedi Fig. 3.5.2).

In mancanza di determinazioni più precise, la temperatura iniziale può essere assunta $T_0$=15 °C.

Per la valutazione del contributo dell'irraggiamento solare si può fare riferimento alla Tab. 3.5.I.

![Fig. 3.5.2 - Andamento della temperatura all'interno di un elemento strutturale](img/fig-3.5.2-temperatura-elemento-schema.png)

**Fig. 3.5.2** - *Andamento della temperatura all'interno di un elemento strutturale*

**Tab. 3.5.I** - *Contributo dell'irraggiamento solare*

| Stagione | Natura della superficie | Incremento di Temperatura | |
|----------|------------------------|:--:|:--:|
| | | superfici esposte a Nord-Est | superfici esposte a Sud-Ovest od orizzontali |
| Estate | Superficie riflettente | 0 °C | 18 °C |
| | Superficie chiara | 2 °C | 30 °C |
| | Superficie scura | 4 °C | 42 °C |
| Inverno | | 0 °C | 0 °C |

# 3.5.5. AZIONI TERMICHE SUGLI EDIFICI

Nel caso in cui la temperatura non costituisca azione fondamentale per la sicurezza o per la efficienza funzionale della struttura è consentito tener conto, per gli edifici, della sola componente $\Delta T_u$, ricavandola direttamente dalla Tab. 3.5.II.

Nel caso in cui la temperatura costituisca, invece, azione fondamentale per la sicurezza o per la efficienza funzionale della struttura, l'andamento della temperatura T nelle sezioni degli elementi strutturali deve essere valutato più approfonditamente studiando il problema della trasmissione del calore.

**Tab. 3.5.II** - *Valori di $\Delta T_u$ per gli edifici*

| Tipo di struttura | $\Delta T_u$ |
|-------------------|:-----------:|
| Strutture in c.a. e c.a.p. esposte | ± 15 °C |
| Strutture in c.a. e c.a.p. protette | ± 10 °C |
| Strutture in acciaio esposte | ± 25 °C |
| Strutture in acciaio protette | ± 15 °C |

# 3.5.6. PARTICOLARI PRECAUZIONI NEL PROGETTO DI STRUTTURE SOGGETTE AD AZIONI TERMICHE SPECIALI

Strutture ed elementi strutturali in contatto con liquidi, aeriformi o solidi a temperature diverse, quali ciminiere, tubazioni, sili, serbatoi, torri di raffreddamento, ecc., devono essere progettati tenendo conto delle distribuzioni di temperatura corrispondenti alle specifiche condizioni di servizio.

# 3.5.7. EFFETTI DELLE AZIONI TERMICHE

Per la valutazione degli effetti delle azioni termiche, si può fare riferimento ai coefficienti di dilatazione termica a temperatura ambiente $\alpha_T$ riportati in Tab. 3.5.III.

**Tab. 3.5.III** - *Coefficienti di dilatazione termica a temperatura ambiente*

| Materiale | $\alpha_T$ [10⁻⁶/°C] |
|-----------|:--------------------:|
| Alluminio | 24 |
| Acciaio da carpenteria | 12 |
| Calcestruzzo strutturale | 10 |
| Strutture miste acciaio-calcestruzzo | 12 |
| Calcestruzzo alleggerito | 7 |
| Muratura | 6 ÷ 10 |
| Legno (parallelo alle fibre) | 5 |
| Legno (ortogonale alle fibre) | 30 ÷ 70 |

## C3.5 AZIONI DELLA TEMPERATURA

Larga parte di questo Capitolo resta invariato al passaggio dalle precedenti NTC alle attuali. In particolare non vengono modificati né il § 3.5.1 relativo alle generalità, né il § 3.5.3 in cui si definisce la temperatura dell'aria interna, né il § 3.5.4 relativo alla distribuzione della temperatura negli elementi strutturali, né il § 3.5.5 che definisce le azioni termiche sugli edifici, né il § 3.5.6 che fornisce indicazioni relativamente alle precauzioni da adottare per le strutture soggette ad azioni speciali, né infine il § 3.5.7 relativo alle valutazioni degli effetti delle azioni termiche sui materiali strutturali.

### C3.5.2 TEMPERATURA DELL’ARIA ESTERNA

Modifiche significative sono state apportate solo in questo paragrafo relativo alle temperature massime e minime da adottarsi per l'aria esterna; tali temperature, che nelle precedenti NTC venivano assunte uguali per l'intero territorio nazionale, nelle attuali vengono differenziate suddividendo il territorio nazionale in quattro zone ed in ciascuna di esse tenendo anche conto della quota del sito della costruzione sul livello del mare. In questo paragrafo vengono anche indicati i valori dei periodi di ritorno delle temperature dell'aria da assumere per fasi transitorie di durata compresa fra uno e tre mesi, ovvero fra tre mesi ed un anno.
