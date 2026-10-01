# VC § 3.4.4, verifica del coordinatore C

Firma: CDX, gpt-6-astra/max, profilo ereditato dalla sessione e riscontrato nei metadati runtime. Data: 2026-09-05. Ambito autorizzato: solo file naturale § 3.4.4. Il coordinatore non scrive correzioni del target.

## G0 e G1

G0 OK: D.M. 17 gennaio 2018, allegato tecnico § 3.4.4, pagina fisica 63, stampata 59. Il perimetro inizia dalla rubrica 3.4.4 e termina con l'ultima riga della Tab. 3.4.I, prima di 3.4.5. Escluse tutte le parti precedenti e successive della pagina condivisa. Il ritaglio diretto a 600 dpi occupa il rettangolo PDF [72, 438, 555, 577] punti. L'area è interamente vettoriale: nessuna immagine incorporata interseca il perimetro; il relativo censimento e i dati grezzi dei caratteri sono conservati.

La Circolare è stata consultata soltanto per riscontrare il confine: la pagina fisica 80 conclude C3.4.3 e la 81 apre C3.4.5; non c'è un autonomo C3.4.4 da abbinare. Le immagini delle due pagine restano prova del confine, senza attribuire loro copertura normativa G6 o includere la Circolare negli atti oggetto di G1.

G1 OK al 2026-09-05. Fonte ufficiale: [scheda GU 18A00716](https://www.gazzettaufficiale.it/eli/id/2018/02/20/18A00716/sg), [PDF del supplemento](https://www.gazzettaufficiale.it/do/gazzetta/downloadPdf?dataPubblicazioneGazzetta=20180220&edizione=0&estensione=pdf&numeroGazzetta=42&numeroSupplemento=8&progressivo=0&tipoSerie=SG&tipoSupplemento=SO). Acquisizione odierna in memoria e confronto binario positivo con il PDF congelato. SHA-256 e date effettive sono in `avvio.json` e `g1/acquisizioni.json`.

La nuova ricognizione corrente è documentata da `g1/ricognizione.json` e dagli HTML ufficiali congelati. Letto integralmente l'articolo modificativo del [D.M. 9 marzo 2023](https://www.gazzettaufficiale.it/eli/id/2023/03/22/23A01847/sg): modifica disposizioni transitorie dell'art. 2 e punti del capitolo 11, senza incidere sul § 3.4.4. Nelle ricerche ufficiali indicate non sono emerse rettifiche o modifiche del contenuto dello scope. Non è riutilizzata come G1 una ricognizione di data diversa.

## G2-G4, primo confronto integrale

Letti a vista l'intero perimetro a 600 dpi e il Markdown completo: una rubrica; un capoverso di tre proposizioni; una didascalia; una tabella con tre intestazioni e nove celle di corpo. Quattro notazioni C con pedice E: due nel capoverso, una nella didascalia e una in testata. Inclusa la relazione inline C con pedice E = 1 e la condizione che la precede. Un rinvio alla Tab. 3.4.I. Nessuna formula esposta numerata o autonoma non numerata, nessuna figura, nota o asset richiamato dal target. La tabella non presenta celle vuote o accorpate, unità, note o continuazioni su altre pagine.

G2 OK: intero contenuto normativo del file riconciliato con la fonte, esclusi meccanicamente solo navigazione, indice interno, ancora e contenitore Norma. La mappa definitiva delle righe depurate sarà prodotta sullo snapshot corretto.

G3/G4 iniziali: due famiglie ERR-MD, congelate in `correzioni-congelate-r00.json`: cassa della rubrica, più veste grafica di tre notazioni C con pedice E, per quattro occorrenze materiali complessive. La prosa, tutte le celle e i valori 0,9 / 1,0 / 1,1 concordano; ordine, associazione alle classi e relazione inline sono fedeli. Il corsivo della notazione in didascalia è attestato e resta invariato.

Le decisioni sono fondate sul ritaglio a 600 dpi e sui dati vettoriali: rubrica BritannicBold; due notazioni nel capoverso PalatinoLinotype tondo; testata PalatinoLinotype,Bold; didascalia PalatinoLinotype,Italic. In tutti i casi E è un pedice maiuscolo distinto dalla base C. Nessuna anomalia A e nessuna correzione C/AF-COR: si corregge il Markdown per seguire la fonte. Nessuna adjudicazione pregressa viene ribaltata.

`trascrizione-fonte-c.md` conserva una sola trascrizione strutturale dalla fonte, inclusi apparati, per il confronto meccanico successivo. Provenienza: pagina fisica 63 e ritaglio a 600 dpi letti da C; non è un input del verificatore V.

Normalizzazioni applicabili: catalogo 1 (spaziature, a capo e ricomposizione di parola a fine riga), 2 (apostrofi dritti/curvi), 10 (separatore di didascalia); apparati di navigazione esclusi secondo 11 e procedura § 3. Nessuna estensione della classe N.

## Correzione, preflight e resa

La fase correttiva E R00 ha applicato esclusivamente la prima lista. Il diff indipendente C coincide esattamente con le sostituzioni congelate; la rilettura integrale di prosa, formule inline e tutte le celle è positiva. La prima resa canonica, una pagina, ha fatto emergere il mancato grassetto delle prime due intestazioni: nel renderer la sola posizione di testata Markdown non basta. R03 congelato separatamente prima di ogni G6 e affidato allo stesso E distinto. Il preflight R00 è conservato in `preflight-r00/`. La trascrizione strutturale C esplicita ora il grassetto delle due testate già visibile nella fonte. Nessuna modifica ai criteri e nessun giro G6 iniziato.

G3/G4 finali OK. Seconda restituzione E e diff indipendente C: soltanto R01, R02a, R02b e R03, zero cambiamenti estranei. Rilettura integrale sul testo finale e sulla trascrizione fonte: concordanza completa dopo le sole normalizzazioni dichiarate. Tre famiglie di rilievi, sei occorrenze materiali complessive (rubrica, tre notazioni e due intestazioni), tutte chiuse prima del G6. Nessun ERR-MD, ERR-AUDIT o DUBBIO residuo.

G5 OK. `preflight-finale.py` ha riconciliato le 11 righe depurate con la sola pagina primaria ntc:63 senza lacune né sovrapposizioni, verificato i quattro link del file e il diff completo. Lo strumento degli indici ha verificato 311 file e 1754 collegamenti interni; l'indice derivato del file non richiedeva variazioni. Il renderer canonico ha prodotto una pagina senza tag anomali o didascalie automatiche. C ha ispezionato integralmente `render-finale-p01.png`: prosa, didascalia, tre testate, nove celle, quattro pedici E e relazione inline sono leggibili, senza caratteri mancanti, tagli o sovrapposizioni. Confermati tondo, corsivo e grassetto. Differenze di larghezza, rientro e allineamento delle celle appartengono alla resa, senza alterarne l'associazione logica.

Snapshot finale importato dall'output dello script: `6e9a5f838301b7d04ed3dc6c39256fcaf6d78997f2f5567350d287bb6cafc448`. Tutti G0-G5 OK prima dell'avvio G6. Un solo blocco coprirà tutto lo scope: non si aggiungono pagine estranee per raggiungere tre pagine.

La preparazione locale ha avuto due interruzioni tecniche distinte, prima della creazione di pacchetti G6: stampa Python su console cp1252 e serializzazione di byte delle immagini nel rawdict. Risolte con modalità UTF-8 e flag di estrazione dei soli caratteri; immagini censite separatamente. Scheda e CSV riletti prima di proseguire. Nessun rilievo sul contenuto deriva da questi errori e nessun tentativo G6 viene occultato o azzerato.
