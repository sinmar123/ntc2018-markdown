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

## Catalogo delle normalizzazioni, estratto neutro

1. Spaziature, a capo, rientri, spazi doppi della fonte.

2. Varianti Unicode dello stesso carattere; apostrofi e virgolette dritte o curve; `ϕ` e `φ`; hyphen-minus e `−` U+2212.

3. Spaziatura LaTeX, `\left`/`\right`, parentesi ridondanti che non cambiano la struttura, sostituzione di `[ ]` con `( )` come delimitatore esterno.

4. Virgola decimale italiana resa `0{,}85` in LaTeX. **Attenzione**: copre la *resa* di una virgola che la fonte stampa, non la *sostituzione* di un punto che la fonte stampa.

5. `\cdot` **aggiunto** dove la fonte moltiplica per giustapposizione. Mai tolto dove la fonte lo stampa.

6. Espansione delle celle accorpate: nelle **testate** l'etichetta che copre più colonne si scrive una volta sola e le celle coperte restano vuote; nel **corpo** sia i valori sia le etichette di riga si ripetono in tutte le celle logiche coperte.

7. Resa in tabella di valori che la fonte espone come testo corrente, **a intestazioni vuote** e senza aggiungere parole.

8. Spazi interni ai tag di formula.

9. Punteggiatura finale delle didascalie di tabella e figura, che la fonte chiude col punto fermo e il corpus omette.

10. Separatore fra numero e testo della didascalia: `-`, `–` e `—` sono equivalenti e non producono rilievi di conformità. Quando la fonte usa `:`, il corpus può conservarlo oppure renderlo con uno dei tre trattini.

11. Riga di navigazione in testa a ogni file e apparato Obsidian (wikilink `[[…]]`, àncore `^nome`, marcatori di nota): non sono testo della fonte e vanno tolti meccanicamente dai pacchetti dei blocchi ciechi del G6.

12. Resa dei viewer che non usano il template di render, Obsidian compreso: i tag di formula vi appaiono fra tonde invece che fra quadre. Nel PDF prodotto da `strumenti/render-capitolo.py` le quadre sono corrette.

13. **Pedici e basi che la fonte compone a corpo pieno.** La fonte stampa `log10(A)` col `10` grande quanto le altre cifre e `Re` con la `e` grande; il corpus scrive `\log_{10}` e `R_e`.

14. **Tabelle senza riga di testata.** Diverse griglie della Circolare partono direttamente con i dati; la sintassi delle tabelle Markdown pretende una riga di titolo, e la prima riga di dati finisce in quella posizione. Nessuna parola aggiunta né persa.

15. **Righe a piena larghezza interne alla griglia.** Quando la fonte chiude una tabella con una riga a piena larghezza senza contrassegno, il corpus la rende come capoverso subito dopo la tabella, nello stesso ordine di lettura.

16. **Formule a più rami.** La fonte le numera una volta sola, col tag centrato sul blocco; il corpus rende ogni ramo come formula esposta distinta e mette il tag su uno solo. Ne conseguono formule esposte non numerate che nella fonte non esistono come tali.

17. **Formule con graffa rese come elenco.** Quando la fonte espone due o più valori alternativi con una graffa, il corpus li rende come voci di elenco puntato.

18. **Blocchi «dove:».** La fonte li compone come capoverso unico o come righe rientrate senza marcatore; il corpus li rende come elenco puntato, senza spezzare né riordinare il testo.
