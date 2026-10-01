---
title: Procedura unica di conversione e verifica NTC 2018
procedura_id: VC-NTC
revisione: 3
data: 2026-09-09
approvazione: Sandro, perfezionamento autorizzato dopo la misura del § 3.4.5 il 2026-09-09
redazione: CC
---

# Procedura unica VC NTC 2018

## 1. Autorità, revisione e campo di applicazione

Questo è l'unico percorso operativo per convertire, correggere, verificare e rilasciare NTC 2018 e Circolare 7/2019, per tutti gli agenti. Sostituisce, su questo corpus, il ciclo generale, il precedente sottoprotocollo tabelle/formule e le matrici di orchestrazione ed economia. Non si sommano i loro passaggi a quelli qui definiti. Il significato di `VC-OK` resta quello documentale del VC-8, con G0-G7 superati e zero rilievi aperti.

Il [catalogo delle normalizzazioni](verifica-conformita/normalizzazioni-dichiarate-NTC2018.md) è l'unico allegato prescrittivo: contiene le trasformazioni di classe N, non un secondo workflow. Le istruzioni di workspace restano applicabili per sicurezza, autorizzazioni e registrazioni. Skill, memoria e file di governo rinviano qui senza ricopiare le regole.

Ogni affinamento operativo si applica a questo file, incrementando `revisione` e registrando motivo e verifica nel CHANGELOG. Non creare una procedura economica, sperimentale o specifica per modello concorrente. Una modifica dei criteri di fedeltà, della copertura integrale, dell'indipendenza o delle autorizzazioni richiede una decisione esplicita di Sandro; un miglioramento tecnico che li preserva può essere applicato e verificato nell'incarico autorizzato.

La revisione e l'hash della procedura e del catalogo usati si congelano nelle evidenze di ciascuno scope. Per scope precedenti, alla ripresa autorizzata si registra l'adozione della revisione corrente al prossimo gate non iniziato, mantenendo snapshot, rilievi, adjudicazioni, contatore G6, limite autorizzato e decisioni pendenti. Un G6 già iniziato non cambia regole a metà: si termina secondo il disegno congelato, oppure si interrompe e se ne registra il consumo prima del successivo. Nessun esito storico viene reinterpretato o promosso per effetto di questo aggiornamento.

Nell'unificazione autorizzata sono stati ritirati i due vecchi prompt operativi del § 4.2, conservati in `old/ISTRUZIONI-SUPERATE-*.md` con gli originali nell'archivio del metodo. È una disattivazione amministrativa, non un'esecuzione o una chiusura positiva degli scope. Le loro richieste e i contatori datati non sostituiscono lo stato corrente di CSV e schede.

## 2. Avvio, stato e contesto minimo

Inneschi: `iniziamo conversione <scope>`, `riprendiamo conversione <scope>`, `riprendiamo VC <scope>`. L'autorizzazione riguarda soltanto lo scope chiesto; non apre automaticamente il successivo.

1. Eseguire `python strumenti/vc-supporto.py avvio [scope]`: restituisce riga CSV, lucchetto, ultima nota e soli estratti pertinenti di README/TODO/CHANGELOG, senza scritture. CSV resta l'unica fonte dello stato; lo script non autorizza né prende in carico. Per scope storici/aggregati senza riga autonoma leggere le righe coinvolte e quella master, oltre alla scheda; non dedurre lo stato da vecchi prompt.
2. Integrare soltanto le parti necessarie della scheda, gli estratti segnalati come troncati e la voce pertinente della revisione del capitolo. Aprire l'indice solo per localizzare contenuti. Non stampare gli interi storici o i manifest. La procedura si legge integralmente una volta per contesto; se è già disponibile si controlla l'hash e si rileggono soltanto le parti cambiate. I ruoli delegati ricevono la consegna pertinente, non il bootstrap e la conversazione del coordinatore; restano applicabili le istruzioni di sicurezza del runtime.
3. Se manca lo scope nella richiesta, riprendere l'unico `IN-CORSO` soltanto se l'autorizzazione e il lucchetto lo consentono. Senza univocità chiedere una sola precisazione. La sequenza numerica non autorizza un nuovo scope.
4. La scheda è il lucchetto: `IN-CORSO` di un altro agente richiede subentro esplicito; stesso agente e presa odierna richiedono verificare che non sia un'altra sessione attiva. La ripresa di una propria presa precedente si annota. Due scope non possono modificare lo stesso file.
5. Ricalcolare le impronte delle fonti congelate in `verifica-conformita/fonte-ufficiale/` e del target. Accertare i confini sulle pagine, comprese quelle condivise. Risolvere le mappature incerte prima di chiudere G2.

Unità ordinaria: la **sezione** `x.y`, cioè i file naturali `x.y.z` ancora da verificare presi in una sola volta, con Norma e Circolare dove presenti. Il singolo file naturale resta un'unità legittima quando è l'unico rimasto della sua sezione, quando gli altri sono già chiusi o in carico ad altri, o quando la sezione da sola supera i limiti qui sotto. La ragione è di costo, misurata sul § 3.4.5 il 2026-09-09: l'attrito di apertura, G1, confezionamento e chiusura non si riduce con la lunghezza del paragrafo, quindi su due capoversi pesa più della verifica. Dimensionare per pagine effettivamente coinvolte, formule, celle e figure. Oltre 15 pagine, 40 formule numerate o 10 apparati complessi proporre sotto-scope prima della presa; i limiti massimi restano 40 pagine o 150 formule. Uno scope già avviato non si spezza senza decisione esplicita.

La scheda conserva i campi già in uso, aggiungendo `procedura: VC-NTC/2`, `procedura_sha256`, `routing_effettivo` e, quando disponibili, `consumi`. Le schede chiuse mantengono la revisione effettivamente usata. `giro_g6` non si azzera; `max_giri` è 3 salvo limite diverso già autorizzato. CSV = stato corrente; scheda = lucchetto e diario tecnico; verbale/manifest = evidenza dello snapshot. Il master `../_registro-verifica-conformita.csv` conserva gli stati generali e degli scope autonomi. La vista XLSX è derivata e non si modifica a mano.

### Convenzioni del corpus

- Capitoli in `capXX/` con `indice-capXX.md`, mai `index.md`; ogni sezione con figli ha `indice-x.y.md`, introduzione `x.y-introduzione.md` e file naturali `x.y.z-<tema>-<argomento>.md`. Sezioni senza livello 3 autonome; Capitoli 1 e 12 monolitici. Le sezioni presenti soltanto nella Circolare hanno prefisso `c` nel nome. Norma e Circolare si abbinano nel file naturale quando condividono il livello 3.
- Ogni file naturale ha indice interno gerarchico dei due atti: link Markdown nello stesso documento e ancore HTML `toc-ntc2018-*`, fra marcatori `INDICE-INTERNO:INIZIO/FINE`. Generazione e controllo con `strumenti/genera-indici-interni.py`; rimozione meccanica dai pacchetti G6. Non mantenere a mano l'indice derivato.
- Link Markdown relativi e portabili, con ancore esplicite quando occorrono; niente wikilink Obsidian. Ogni file rinvia all'indice di sezione, del capitolo e generale. Gli indici hanno sommario, link ai paragrafi e frontmatter `aliases`; il link al titolo principale non dipende da un'àncora implicita.
- Formule LaTeX inline/display con il tag originale, tabelle Markdown e figure PNG in `img/`, con risoluzione adeguata alla fonte e senza ricampionamenti spacciati per nuovo dettaglio. Le prove sui glifi seguono il § 4. Annotazioni separate in `capXX/annotazioni/`, con rinvii portabili al testo pertinente.

<!-- CANONE-G6:INIZIO -->
## 3. Fedeltà e classificazione

La pagina ufficiale è la fonte. OCR e testo estratto sono ausili, non prove finali. Il controllo riguarda il testo stampato, anche quando appare tecnicamente strano; l'equivalenza algebrica non dimostra fedeltà editoriale.

- **N / NORM:** soltanto le trasformazioni elencate nel catalogo delle normalizzazioni consegnato. Nessuna estensione per analogia. Una differenza non prevista si conserva o viene esaminata secondo A/C.
- **A / AF:** anomalia della fonte conservata letteralmente. Tag anomali, numerazioni ripetute, rinvii irregolari, refusi di contenuto e letture alternative entrambe sensate restano conservati. I tag anomali si rendono con `\tag*{...}`; soltanto gli spazi interni sono normalizzabili. Una questione che richiede conoscenza esterna all'atto resta un rilievo da sottoporre a Sandro.
- **C / AF-COR:** refuso esclusivamente tipografico o di codifica, correggibile soltanto se la lettura corretta è attestata nello stesso atto, con pagina fisica puntuale. Una precedente trascrizione corretta non è un'attestazione; decreto e Circolare non si correggono reciprocamente. La correzione non cambia valore né grandezza e non tocca cifre, coefficienti, esponenti, apici/primi, operatori, segni, disuguaglianze o unità. Richiede la prova del § 4 e una nota visibile subito dopo l'apparato: `*Nota di trascrizione AF-COR-<id>: la fonte, p. fisica <pagina>, stampa <lettura>; refuso tipografico per <lettura attestata>, attestata a p. fisica <pagina>.*` Le note pregresse con diversa punteggiatura restano valide. Nota sul posto, annotazione permanente e verbale devono concordare. Senza tutte le condizioni, conservare e aprire il rilievo.
- **ERR-MD:** omissione, aggiunta o difformità della trascrizione rispetto alla fonte e alle trasformazioni ammesse.
- **ERR-AUDIT:** errore del pacchetto, della mappatura o delle evidenze; non è automaticamente un errore del corpus.
- **DUBBIO:** lettura non risolta. Non equivale a `OK`.

Non aggiungere parole, intestazioni di tabella, estremi di sommatoria o notazioni assenti dalla fonte. Le spiegazioni editoriali stanno nelle annotazioni, separate dal testo normativo. Apparati di navigazione e indici interni si escludono meccanicamente dal confronto; le note AF-COR restano visibili e se ne controlla la legittimità. Una nota o normalizzazione legittima non è un errore.

## 4. Apparati, prove e non regressione

Verificare il 100% di prosa, rubriche, note, rinvii, formule numerate e non numerate, inline sostanziali, definizioni/condizioni, celle logiche, figure e didascalie. Il conteggio aiuta a dimostrare copertura, ma da solo non dimostra conformità.

Per le tabelle controllare ordine, intestazioni gerarchiche, etichette, ogni valore, segno, decimale, unità, nota e accorpamento. Distinguere vuoto, trattino e non applicabile. Applicare alle celle accorpate esclusivamente la convenzione del catalogo; non inventare una colonna `Categoria`. Proteggere le barre matematiche nella sintassi Markdown e controllare le tabelle multipagina.

Per le formule controllare entrambi i membri, struttura di frazioni/radici, parentesi, indici e gerarchie di pedice, apici/primi, accenti, greche, operatori, segni, limiti, casi, numeri, unità, tag, definizioni e condizioni. Servono sia il confronto strutturale sia la verifica visiva della resa effettiva. Le immagini devono corrispondere alla figura fonte completa e leggibile, con ritaglio pulito e didascalia verificata.

Prima di scegliere la prova, accertare se l'area è testo vettoriale, raster incorporato o una combinazione dei due. Ogni decisione su un glifo, apice, pedice, parentesi, cifra o accento richiede un ritaglio dalla pagina fisica a **600 dpi o più**. In caso di ambiguità leggere anche font, corpo, codepoint e posizione vettoriale del PDF. Se codifica e immagine discordano, prevale la pagina stampata e si registra la discordanza. Conservare pagina, dpi, percorso, metodo ed esito della prova.

Per un elemento esclusivamente raster, la prova di dettaglio è l'immagine incorporata alla risoluzione nativa, estratta senza ricampionamento: il ritaglio di pagina a 600 dpi serve anche a localizzarla, ma interpolare non crea informazione. Registrare dimensioni e risoluzione native, impronta del raster e non applicabilità dei codepoint. Estrarre tutti gli eventuali frammenti, conservandone disposizione e copertura; verificare anche la didascalia se su una pagina diversa. Nelle aree miste controllare separatamente le componenti raster e vettoriali. Non chiedere una risoluzione nativa o una codifica inesistenti, né scambiare un raster parziale per l'intero apparato.

Per ribaltare un'adjudicazione precedente servono insieme: ritaglio ad almeno 600 dpi, codifica/posizione vettoriale e un secondo verificatore in contesto separato. Il secondo riceve solo la fonte e una domanda aperta su ciò che stampa, senza letture concorrenti né risposta attesa. Può usare lo stesso modello; un altro modello o fornitore è facoltativo. Se le prove concordano, si procede senza una conferma ulteriore; se resta discordanza, non modificare e chiedere a Sandro.

Se il glifo contestato esiste soltanto nel raster, alla codifica/posizione vettoriale si sostituiscono l'originale nativo identificato e la non applicabilità documentata dei codepoint; il secondo verificatore e la concordanza delle prove restano obbligatori. Se il dettaglio nativo non consente una lettura univoca, resta `DUBBIO` e si chiede a Sandro, senza ricostruire ciò che la fonte non permette di leggere.
<!-- CANONE-G6:FINE -->

## 5. Esecutori: pochi ruoli, nessuna scala obbligatoria di chiamate

I gate sono criteri, non otto incarichi. Configurazione ordinaria: C, un V per blocco G6 e script; E distinto si attiva soltanto per correzioni o lavoro preparatorio che richieda un modello. Riutilizzare lo stesso esecutore per attività compatibili; un'operazione locale breve non giustifica uno spawn. Le operazioni ripetitive passano dai comandi comuni: non ricreare script di registrazione per ogni scope né usare un agente per leggere il riepilogo di un altro script.

| Ruolo o lavoro | Profilo Codex ordinario | Limite |
|---|---|---|
| Meccanica: hash, pacchetti, conteggi, lint, manifest, registri | Script locale | Nessun giudizio normativo |
| E: preparare mappe, ordinare differenze, proporre trascrizioni, applicare sostituzioni esatte approvate | `gpt-5.6-terra`, `medium` | Non chiude da solo G3/G4/G6/G7, né decide N/A/C |
| Attività breve rigidamente definita, non coperta da script, se serve davvero delegarla | `gpt-5.6-luna`, `medium` | Alternativa a E per quel compito, non passaggio aggiuntivo |
| C: confini, giudizio G0-G5, classificazione e adjudicazione ordinaria | `gpt-5.6-sol`, `high` | Non scrive le correzioni del target che coordinerà nel G6 |
| V: inventario fonte-prima, G6 integrale e giudizio G7 | `gpt-5.6-sol`, `xhigh` | Contesto fresco, nessuna correzione del target |
| Ambiguità persistente, possibile regressione, revisione del metodo | `gpt-6-astra`, `high`; `xhigh` solo se motivato | Solo il punto difficile e le prove necessarie |

C usa Sol `xhigh` anche in G4/adjudicazione per glifi ambigui e apparati critici. Una sostituzione su formule o numeri può essere applicata da Terra solo se testo prima/dopo e localizzazione sono già approvati da Sol e il diff è riconfrontato; se richiede una nuova trascrizione interpretativa la esegue Sol, distinto da C. Il primo passaggio normativo e quello indipendente restano entrambi capaci di controllare gli apparati.

Questi sono profili operativi, **non** l'obbligo di usare il massimo modello oggi disponibile. L'arrivo di Astra non promuove automaticamente tutti i ruoli ad Astra. Non usare `max` o `ultra` di default. Non promettere un cambio di modello della sessione principale: se serve un esecutore diverso si delega il compito delimitato, usando solo identificativi e livelli esposti dal runtime e registrando quelli effettivi. Se l'esecutore corrente è compatibile con il ruolo, può completarlo senza un nuovo contesto inutile, salvo l'indipendenza di V.

Per altri runtime scegliere equivalenti documentati per preparazione, giudizio normativo e verifica critica, dichiarando il modello effettivo; non imporre la classe massima a tutte le attività. In assenza di un modello economico, uno script o il coordinatore può coprire la preparazione, dichiarando il mancato risparmio. In assenza del profilo critico, non degradare G6 a Terra/Luna: cercare un esecutore di capacità comparabile; se non disponibile fermare quel gate. Diversità di modello/fornitore e duplicazione di un blocco sono facoltative, da motivare come misurazione; non costituiscono gate.

## 6. Preparazione e G0-G5

1. **G0:** identificare atti, versioni, file, confini, inclusioni ed esclusioni. Nessuna porzione del target può restare fuori dalla dichiarazione.
2. **G1:** documentare URL ufficiali, acquisizione, impronte e ricognizione delle modifiche successive per ciascun atto presente nello scope, alla data dichiarata. Se sono presenti Norma e Circolare, vanno coperti entrambi; per uno scope di sola Circolare non si aggiunge il decreto. È riutilizzabile una ricognizione congelata che copra gli stessi atti/versioni e tutte le modifiche pertinenti, purché non più vecchia di **trenta giorni**: registrare il rinvio, verificare l'applicabilità allo scope ed eseguire un **ricontrollo mirato** sulla banca dati ufficiale, cioè la sola interrogazione degli aggiornamenti di ciascun atto, senza rifare la ricerca piena. Il ricontrollo si registra con la sua data ed è esso stesso evidenza. Oltre i trenta giorni, o se il ricontrollo segnala un aggiornamento, la ricognizione si rifà per intero. Un hash invariato da solo non prova la vigenza.
3. E/script prepara un solo fascicolo: pagine fonte, testo ausiliario, Markdown depurato, mappa pagina-righe, inventari e candidati. Per le pagine intere bastano immagini leggibili ad almeno 200 dpi; usare alta risoluzione sui ritagli necessari, senza inviare più volte l'intera pagina.
4. **G2-G3:** C riconcilia la copertura integrale e giudica i residui del confronto testuale completo. E può ordinare i candidati; né il diff né un estrattore con codifica difettosa provano da soli l'assenza di errori. Le porzioni illeggibili per la macchina si controllano visivamente, segnandone la copertura.
5. **G4:** C esegue la prima verifica completa degli apparati secondo § 4. Il successivo G6 ne costituisce la seconda lettura indipendente. Non si aggiungono una coppia A/B autonoma, una doppia trascrizione integrale e un ulteriore G6 per soddisfare lo stesso requisito. Se un confronto strutturale richiede una trascrizione fonte, conservarla una volta e ricavarne il diff; V non riceve questa trascrizione né l'esito G4. Se non ci sono apparati, chiudere G4 sul conteggio riconciliato, senza agente dedicato.
6. Congelare tutti i rilievi ammessi in una sola lista con identificativo, posizione, prova, classe e modifica esatta. E corregge soltanto quella lista; C confronta il diff. Non mescolare migliorie editoriali. Controllare di nuovo le parti corrette e gli effetti sul documento completo prima di congelare lo snapshot.
7. **G5/preflight:** mappa completa delle pagine e di tutte le righe del Markdown depurato; nessuna lacuna o sovrapposizione primaria; apparati e asset riconciliati; zero candidati non decisi. Eseguire i controlli di link/indici e il render canonico con `strumenti/render-capitolo.py`. Verificare visivamente la resa completa e i tag; controllare asset, caratteri mancanti, tabelle, tagli e sovrapposizioni. Un render riuscito non equivale a verifica visiva.

I controlli meccanici si eseguono con script e se ne legge il riepilogo, non l'intero manifest. Accorpare operazioni indipendenti; interrompere un lotto solo quando il risultato determina il passo successivo. Non ripetere hash, render o lint sullo stesso insieme immutato, salvo il controllo richiesto alla rivelazione, archiviazione o chiusura. Prima del G6 tutti G0-G5 sono `OK`, senza rilievi aperti. Un solo rapporto C conserva giudizi, mappa e preflight: niente rapporto separato di proposta di chiusura che li riscriva.

L'estrazione può perdere intere proposizioni attorno ai simboli inline, non soltanto il simbolo: l'assenza di differenze nel testo estratto non esclude omissioni nella prosa. Anche i delimitatori dei tag possono essere decodificati male; la localizzazione automatica cerca il contenuto del tag e il riscontro visivo decide la forma stampata. Questi limiti non riducono la copertura integrale del G6.

## 7. G6 integrale e indipendente

C non può essere autore della trasposizione/correzione dello snapshot. V è distinto da C ed E e non conosce giudizi precedenti. Se un ruolo è incompatibile, sostituire soltanto quel ruolo. Non affidare a C l'inventario cieco né la verifica dei blocchi.

Partizionare in blocchi di 3-5 pagine fonte, rispettando continuità di formule, tabelle e definizioni. Se lo scope intero occupa 1-2 pagine, un solo blocco copre tutto. Non includere sezioni estranee per raggiungere tre pagine. Assegnare tutte le righe depurate a un blocco e tutte le pagine a un blocco primario. La duplicazione facoltativa non aumenta la copertura primaria.

Ogni V usa un contesto fresco (`fork_turns="none"`, dove disponibile), in due fasi nello stesso contesto:

1. **Fonte-prima:** riceve il solo blocco prodotto da `prepara`, con `ISTRUZIONI-V.md`, canone, pagine/ritagli e confini neutri. Censisce dalla fonte con ID stabili, pagina e localizzazione, leggibilità, esclusioni e dubbi. Sono ammessi gruppi localizzabili di capoversi o rettangoli di celle, con estremi e componenti dichiarati; formule e condizioni devono restare rintracciabili. Non trascrivere tutta la prosa o tutte le celle per descrivere la copertura. Il controllo resta sul 100% degli elementi del gruppo.
2. **Congelamento:** `valida-inventario` controlla il formato senza leggere il target. V corregge nello stesso contesto eventuali campi errati prima del congelamento; si conserva la traccia del tentativo, senza ricreare le fonti o rifare la lettura. `rivela` ripete il controllo e congela inventario, esito e canone prima del Markdown. Dopo il congelamento nessun input si sovrascrive: eventuali rettifiche sono aggiunte separate. Non riutilizzare il contesto se sono venute meno cecità o copertura.
3. **Confronto:** solo dopo il congelamento V riceve `testo.md` e gli asset. Confronta tutto e scrive un solo rapporto: ID coperti, normalizzazioni, rilievi puntuali, letture, isolamento ed esito. Con zero rilievi bastano ID e attestazione integrale, senza una motivazione OK per ogni cella o una copia dell'inventario. `valida-g6` riconcilia gli ID; la correttezza del giudizio rimane di V.

Mai consegnare a V README, TODO, CHANGELOG, scheda, verbali, inventari preparatori, conteggi attesi, correzioni note o risultati di altri blocchi. Il canone contiene i criteri e le normalizzazioni in forma neutra, senza esempi o rilievi del corpus. Il rapporto può essere strutturato e breve, ma deve rendere ricostruibile la copertura.

V può richiedere una prova fonte aggiuntiva indicando pagina, area e domanda aperta. C/script fornisce soltanto ritaglio, raster nativo o dati vettoriali pertinenti, con provenienza e hash, senza suggerire la lettura. Si conserva l'integrazione separatamente dagli input già congelati, registrando quando è stata consegnata; non si altera retroattivamente l'inventario fonte-prima. Una prova aggiuntiva tratta dalla medesima fonte non compromette da sola la cecità.

Il verificatore riceve la sola cartella del blocco, preferibilmente in una directory temporanea esterna al workspace, con strumenti limitati agli input ammessi quando il runtime lo permette. `cwd`, `-C`, `read-only` e `fork_turns="none"` **non dimostrano da soli** il divieto di leggere altre cartelle. Registrare isolamento effettivo o sola restrizione istruttiva; non simulare una sandbox. Una lettura di materiale vietato invalida il blocco, da rifare in un nuovo contesto.

La sola indisponibilità di una sandbox di lettura non richiede una conferma: si procede con restrizione istruttiva dichiarata e controllo delle letture registrate. Se non è possibile nemmeno mantenere separati input, contesto e ruoli, G6 non può essere dichiarato indipendente e si cerca un esecutore compatibile.

`giro_g6` aumenta quando il primo V accede a un target valido per il confronto. Tentativi di preparazione respinti prima restano comunque tracciati e conteggiati nei consumi. C adjudica le segnalazioni sulla fonte, senza alterare i rapporti originari. G6 chiude soltanto con copertura integrale e zero `ERR-MD`, `ERR-AUDIT` e `DUBBIO` residui.

## 8. Correzioni, ripetizioni e arresto

| Evento | Azione obbligatoria |
|---|---|
| Correzione post-G6 del testo normativo o di un asset verificato | Lista congelata, E distinto, diff contro lista, nuovo snapshot/render/preflight; poi nuovo G6 integrale |
| Errore nel solo rapporto, hash ricopiato male o manifest, con target/input effettivamente verificati invariati | Rettifica append-only e verifica dell'evidenza interessata; riaprire G7 se necessario, senza rifare automaticamente G6 |
| Pacchetto privo di target, fonte errata, copertura mancante o cecità compromessa | Non attribuire copertura al blocco; correggere il confezionamento e rifare integralmente i blocchi invalidi in contesti freschi. Se cambia il target, vale la prima riga |
| Stessa anomalia tecnica di preparazione per due tentativi consecutivi | Sospendere gli spawn e correggere/collaudare lo strumento; nessun terzo tentativo identico |
| Rilievo che ribalta una decisione precedente | Applicare § 4 prima di correggere |

Al nuovo giro integrale spostare i confini dove materialmente possibile; per scope indivisibili di 1-2 pagine dichiarare che coincidono. Non è obbligatorio cambiare famiglia. Dopo una correzione post-G6 non sostituire il controllo integrale con un controllo a campione o dei soli punti corretti, salvo deroga espressa di Sandro riferita allo scope.

Il recupero dei soli blocchi invalidi, sul medesimo snapshot e senza modificare i blocchi validi, completa il giro corrente: non azzera il contatore e non costituisce un nuovo giro integrale. Registrare separatamente i tentativi falliti e quelli sostitutivi, così il risparmio non nasconde lavoro già consumato.

Fermare il ciclo e chiedere una decisione con i soli rilievi residui quando: si raggiunge `max_giri` senza convergere; i rilievi già aperti e persistenti non diminuiscono dopo una fase correttiva; restano adjudicazioni discordi; serve conoscenza esterna all'atto o una scelta generale di politica. I nuovi rilievi non contano come mancata decrescita dei persistenti. Il limite di giri aumenta soltanto con autorizzazione esplicita e non si azzera migrando procedura o modello. Nel frattempo si possono correggere gli errori certi già adjudicati che non dipendono dalla decisione pendente.

## 9. G7 e chiusura

Gli script calcolano e riaprono un manifest degli input/output **effettivamente usati**: fonti, target, asset, annotazioni pertinenti, procedura/catalogo congelati, pacchetti validi, inventari/rapporti G6, adjudicazioni, diff e render finale. Gli scarti precedenti restano conservati nello storico; non vanno aggiunti automaticamente tutti al manifest di rilascio. Gli hash del rapporto si importano dall'output dello script, non si ricostruiscono a memoria.

V può chiudere G7 nello stesso contesto della propria verifica, ricevendo allora le evidenze di chiusura: la cecità è richiesta fino al termine del G6, non dopo. Non occorre un nuovo P2 che rilegga tutto il fascicolo. Per più blocchi, designare uno dei V alla decisione G7. C può predisporre verbale e registrazioni; il giudizio resta a un esecutore critico non autore delle correzioni. Dopo una rettifica puramente documentale lo stesso esecutore G7 può controllare il delta e l'integrità, senza un nuovo inventario.

Il verbale riporta: scope e snapshot, atti/URL/vigenza, revisione di procedura e catalogo, gate G0-G7, copertura, normalizzazioni applicate, anomalie A, tutte le C con riscontro, rilievi chiusi, catena degli hash, manifest e identità effettive dei ruoli. Quando il G1 riusa una ricognizione congelata, la vigenza si dichiara con **due date**, quella della ricognizione e quella del ricontrollo mirato, e non con la data del verbale: chi legge deve sapere fino a quando è stato guardato, non quando è stato scritto. Dichiarare natura AI/umana, presenza o assenza di revisione umana integrale e isolamento reale. La resa dei viewer diversi dal renderer canonico è quella dichiarata nel catalogo.

Per i nuovi rilasci il manifest punta alle copie congelate di procedura e catalogo, senza aggiungerne anche le versioni vive. Un manifest storico che contiene entrambe può essere controllato con `verifica-manifest --congelati`: il riepilogo dichiara la copia sostitutiva già presente nel manifest e impone identità di hash e byte. L'opzione non vale per target, fonti normative o asset e non cambia il manifest originale. G7 e verbale chiudono esternamente la catena degli hash, evitando autoreferenze.

Rilasciare solo se tutti i gate sono `OK` e non restano rilievi. Aggiornare CSV locale e, quando pertinente, master; per le righe `VC-OK` usare `Nessuna sul file: VC conclusa sullo snapshot registrato.`. Rigenerare la vista XLSX con `strumenti/genera-vista-xlsx-registro.py` e passare `strumenti/lint-registro-verifica.py`. Aggiornare scheda a `CHIUSO`, README, TODO, CHANGELOG, revisione del capitolo e indice se cambia l'inventario file; registrare il giornale con firma e la stessa prossima azione. Il prossimo scope resta una proposta, non un'autorizzazione.

Usare `registra CONFIG` per controllare il piano di allineamento; dopo il riscontro di C, `registra CONFIG --applica` copia il giudizio già emesso, riallinea anche il titolo dal Markdown e verifica registro/XLSX. **Il CSV non si modifica a mano**, nemmeno per una riga: il comando quota i campi, una patch no, e il 2026-09-09 un punto e virgola scritto a mano nella prossima azione del § 3.4.5 è diventato una dodicesima colonna, costando un giro di controlli per rimetterla a posto. Il JSON contiene testi completi e sostituzioni esatte, non nuovi script; formato nella specifica tecnica. Nessuna nuova autorizzazione di Sandro è necessaria per applicare le registrazioni dello scope già autorizzato. Il giornale usa il comando dedicato, una sola volta. Fallimenti o modifiche concorrenti si recuperano dalla ricevuta, senza ripetere alla cieca.

`VC-OK` vale per quello snapshot/perimetro e non sostituisce la fonte ufficiale. Una modifica dei file verificati o della fonte richiede rivalutare lo stato e la verifica; una fonte normativa aggiornata rende superata la vigenza dichiarata. La manutenzione della procedura non modifica retroattivamente il corpus o le prove congelate delle verifiche precedenti.

## 10. Strumenti, consumi e affinamento

`python strumenti/vc-supporto.py --help` è l'ingresso per stato sintetico, pacchetti a rivelazione differita, manifest verificati e riepilogo dei consumi. La specifica tecnica dei comandi è in [strumenti/vc-supporto.md](strumenti/vc-supporto.md); non introduce gate o criteri ulteriori. Gli script non emettono `VC-OK` e non sostituiscono il controllo visivo.

Dimensionare il testo delle evidenze, non la profondità della verifica. Per uno scope di 1-2 pagine senza rilievi aperti: un rapporto C entro 400 parole, prosa dell'inventario e del G6 entro 300 parole ciascuno, motivazione G7 entro 200 parole. ID, mappe, dati calcolati e rilievi con prove restano fuori da questi limiti. Se occorre più spazio si registra il motivo nel rapporto, senza troncare controlli, dubbi o prove e senza chiedere una deroga. I budget sono limiti redazionali, non nuovi gate. G7 richiama le evidenze senza ricopiarle; il verbale è la sola sintesi finale per il lettore.

Alle transizioni G5/G6/G7 controllare il costo delle interazioni: se il coordinamento di uno scope di 1-2 pagine supera 12 chiamate senza nuovi rilievi, accorpare il lavoro meccanico residuo prima di continuare. La soglia serve a correggere il modo di eseguire, non autorizza un controllo incompleto né nuovi contesti automatici. Non interrompere una lettura indipendente soltanto per risparmiare token. Nei contesti grandi, ridurre input e output specifici della consegna; non promettere di rimuovere istruzioni iniettate dal runtime che l'agente non controlla.

Registrare nella scheda, per ruolo/fase: modello effettivo, ragionamento, numero di contesti/tentativi e, se esposti, input, input in cache, output (ragionamento come sottoinsieme, senza sommarlo due volte). Per i log cumulativi si usa l'ultimo contatore valido di ogni sessione, non la somma degli aggiornamenti. Non sommare parent/figli se il runtime non chiarisce l'aggregazione; dichiarare separatamente il perimetro misurato. Non convertire token o prezzi API in percentuali di quota dell'abbonamento.

La prima applicazione registra una base di confronto per il costo **dello scope completato**, comprese preparazione, correzioni e chiusura. Non promettere risparmi percentuali prima della misura. Un ulteriore abbassamento del profilo critico si valuta su copie con errori noti e casi senza errori, in cieco rispetto alle soluzioni, confrontando omissioni, falsi positivi, dubbi, giri e consumo completo; non si prova degradando silenziosamente il G6 di produzione.

Versioni precedenti: [prima dell'unificazione](old/procedura-vc-ante-20260905/) e [VC-NTC/1 con strumenti](old/procedura-vc-r01-20260905/). Non sono istruzioni attive.

La revisione 2 derivava dalla misura del § 3.4.4 e la sua efficacia doveva misurarsi al primo scope autorizzato, cioè il § 3.4.5 del 2026-09-09. **Quella misura in token non c'è**: il runtime che ha eseguito lo scope non espone i contatori, e la scheda lo dichiara. Quello che si è potuto misurare è il tempo e il suo impiego: due paragrafi di poche righe hanno occupato un pomeriggio, di cui circa metà in attesa fra il coordinatore e l'operatore per il render canonico, e la parte restante in attrito degli strumenti più che in verifica. La revisione 3 nasce da lì e agisce su tre voci di quell'attrito, cioè unità di scope, riuso del G1 e divieto di toccare il CSV a mano; la quarta, il renderer mancante nel container dell'esecutore, si è risolta fuori dalla procedura installandolo. Nessuna promessa percentuale: la prossima sezione autorizzata dirà se è servito.

La revisione 3 non tocca il canone congelato del G6, cioè i §§ 3 e 4 fra i marcatori `CANONE-G6`: i pacchetti già confezionati sotto la revisione 2 restano validi e non vanno rifatti.
