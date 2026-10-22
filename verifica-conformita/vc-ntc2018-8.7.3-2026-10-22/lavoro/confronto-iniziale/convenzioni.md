### Convenzioni del corpus

- Capitoli in `capXX/` con `indice-capXX.md`, mai `index.md`; ogni sezione con figli ha `indice-x.y.md`, introduzione `x.y-introduzione.md` e file naturali `x.y.z-<tema>-<argomento>.md`. Sezioni senza livello 3 autonome; Capitoli 1 e 12 monolitici. Le sezioni presenti soltanto nella Circolare hanno prefisso `c` nel nome. Norma e Circolare si abbinano nel file naturale quando condividono il livello 3.
- Ogni file naturale ha indice interno gerarchico dei due atti: link Markdown nello stesso documento e ancore HTML `toc-ntc2018-*`, fra marcatori `INDICE-INTERNO:INIZIO/FINE`. Generazione e controllo con `strumenti/genera-indici-interni.py`; rimozione meccanica dai pacchetti G6. Non mantenere a mano l'indice derivato.
- Link Markdown relativi e portabili, con ancore esplicite quando occorrono; niente wikilink `[[…]]`. Ogni file rinvia all'indice di sezione, del capitolo e generale. Gli indici hanno sommario e link ai paragrafi; il link al titolo principale non dipende da un'àncora implicita.
- Simboli, grandezze e lettere greche nella prosa si scrivono in LaTeX inline (`$\mu'$`, `$f_m$`, `$\gamma_G$`, `$\overline{X}$`), mai come caratteri Unicode semplici: il renderer canonico non ha i glifi greci e li perde. Pedici ed esponenti come nella fonte, anche nelle unità (`N/mm²`). I richiami di nota che la fonte stampa in apice, per esempio nelle testate di tabella, si scrivono `$^{\text{(a)}}$`. Una testata su due livelli segue la voce 6 del catalogo: prima riga con le etichette di gruppo, una sola volta, e riga successiva del corpo con la prima cella vuota e le etichette di colonna.
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

## 3. Fedeltà e classificazione

La pagina ufficiale è la fonte. OCR e testo estratto sono ausili, non prove finali. Il controllo riguarda il testo stampato, anche quando appare tecnicamente strano; l'equivalenza algebrica non dimostra fedeltà editoriale.

- **N / NORM:** soltanto le trasformazioni elencate nel catalogo delle normalizzazioni consegnato. Nessuna estensione per analogia. Una differenza non prevista si conserva o viene esaminata secondo A/C.
- **A / AF:** anomalia della fonte conservata letteralmente. Tag anomali, numerazioni ripetute, rinvii irregolari, refusi di contenuto e letture alternative entrambe sensate restano conservati. I tag anomali si rendono con `\tag*{...}`; soltanto gli spazi interni sono normalizzabili. Una questione che richiede conoscenza esterna all'atto resta un rilievo da sottoporre a Sandro.
- **C / AF-COR:** refuso esclusivamente tipografico o di codifica, correggibile soltanto se la lettura corretta è attestata nello stesso atto, con pagina fisica puntuale. Una precedente trascrizione corretta non è un'attestazione; decreto e Circolare non si correggono reciprocamente. La correzione non cambia valore né grandezza e non tocca cifre, coefficienti, esponenti, apici/primi, operatori, segni, disuguaglianze o unità. Richiede la prova del § 4 e una nota visibile subito dopo l'apparato: `*Nota di trascrizione AF-COR-<id>: la fonte, p. fisica <pagina>, stampa <lettura>; refuso tipografico per <lettura attestata>, attestata a p. fisica <pagina>.*` Le note pregresse con diversa punteggiatura restano valide. Nota sul posto, annotazione permanente e verbale devono concordare. Senza tutte le condizioni, conservare e aprire il rilievo.
- **ERR-MD:** omissione, aggiunta o difformità della trascrizione rispetto alla fonte e alle trasformazioni ammesse.
- **ERR-AUDIT:** errore del pacchetto, della mappatura o delle evidenze; non è automaticamente un errore del corpus.
- **DUBBIO:** lettura non risolta. Non equivale a `OK`.

Non aggiungere parole, intestazioni di tabella, estremi di sommatoria o notazioni assenti dalla fonte. Le spiegazioni editoriali stanno nelle annotazioni, separate dal testo normativo. Apparati di navigazione e indici interni si escludono meccanicamente dal confronto; le note AF-COR restano visibili e se ne controlla la legittimità. Una nota o normalizzazione legittima non è un errore.

