# Revisione Capitolo 8 - Costruzioni esistenti

## 2026-10-14 - VC-OK del § 8.4 con C8.4

VC-OK del § 8.4 con C8.4, quattro file: G6 integrale giro 2 di V Opus a contesto nuovo, 72 elementi, 5 rilievi di forma decisi da Sandro e corretti (nota 2 senza punto finale, tre corsivi della fonte, grassetto non riprodotto); controllo delle modifiche e G7 di V OK; vigenza 2026-10-13, ricontrollo 2026-10-14; CC cloud, subentrato a NormaNTC18 (OC). [Verbale](../verifica-conformita/verbale-VC-ntc2018-8.4-2026-10-14.md).

Prossima azione: Nessuna sul file: VC conclusa sullo snapshot registrato.

## 2026-09-30 - VC-OK del solo § 8.3

Registrato `VC-OK` su `8.3-valutazione-sicurezza.md` su ordine di Sandro. Snapshot `4edeaeea47bddd2fd20f85f96df429f5236993b55b69033c8122a968de2a03e6`. Verbale `../verifica-conformita/verbale-VC-ntc2018-8.3-2026-09-30.md`. Firma: NormaNTC18 (OC).

## 2026-09-12 - VC-OK del solo § 8.2

Registrato `VC-OK` su `8.2-criteri-generali.md`. VC svolta insieme da Sandro e GROK. Snapshot `69158160ab7980444f6c3e9157b82020dfaa71eb158d3db651799a0dd314ffb5`. Verbale `../verifica-conformita/verbale-VC-ntc2018-8.2-2026-09-12.md`. Firma: GROK.

## 2026-09-12 - VC-OK del solo § 8.1

Registrato `VC-OK` su `8.1-oggetto.md`, 8.2 escluso. Snapshot `80a2c5a3af47c879dda192b43e7a729fd81a9c30fd5a53407cb2a4c08bdd832b`. Verbale `../verifica-conformita/verbale-VC-ntc2018-8.1-2026-09-12.md`. Firma: GROK.

[Torna all'indice del capitolo](./indice-cap08.md) | [Torna all'indice generale](../indice-ntc2018.md)

## 2026-08-26 - ricomposizione editoriale in file naturali

Il file unico `8-esistenti.md` è stato archiviato, con contenuto e SHA-256 invariati, e sostituito da 29 file normativi e 4 indici di sezione. Ogni sezione naturale `8.x.y` o `C8.x.y` appartiene ora a un solo file; norma e Circolare restano abbinate quando condividono il medesimo livello 3.

- Conservati 59/59 tag di formula e tutti i riferimenti grafici del file sorgente.
- Rimappate 113/113 unità del registro sui file correnti, ora `DA_FARE/NON_VALUTATO` come stato corrente e `DA_RICONFERMARE` come processo, con giudizio, snapshot e manifest precedenti conservati nei campi storici.
- Il precedente `VC-OK al 2026-07-29` è ora `VC-SCADUTA al 2026-08-26`, perché il giudizio riguardava il vecchio insieme documentale. Non è stata avviata né simulata una nuova VC.
- Indici e navigazione convertiti in collegamenti Markdown relativi portabili.
- Archivio, staging, snapshot e rapporti di controllo in `../_tmp_render/completamento-struttura-portabile-20260826/`.

**Firma:** CDX (Codex).

## 2026-08-26 - stato VC riconfermato prima della ricomposizione

Stato intermedio precedente alla ricomposizione editoriale descritta nella voce sopra. Era stata accertata una deriva amministrativa del registro di dettaglio e del master generale, non una modifica del corpus. I quattro percorsi del manifest finale erano stati ricalcolati e coincidevano per SHA-256 e dimensione con il congelamento del 2026-07-29, compresi `8-esistenti.md` e `indice-cap08.md`.

- Ripristinate 113/113 unità `COMPLETA/OK` nel registro di dettaglio.
- Ripristinato il master autonomo `ntc2018--norme-costruzioni--cap08` a `VC-OK al 2026-07-29`.
- Confermate 114 righe `VC-OK al 2026-07-29` nell'indice VC, compresa la riga generale `8 / C8`.
- Master del corpus invariato `VC-DA-FARE`.
- Lint globale: 0 errori, 0 avvisi e 0 informazioni.

**Firma:** CDX (Codex).

## 2026-07-29 - Rilascio formale VC-OK

Attribuito `VC-OK al 2026-07-29` al solo scope D.M. 17/01/2018 Capitolo 8 + Circolare 7/2019 Capitolo C8.

- Snapshot finale: SHA-256 `14457ad1b2f3a4931eb82dedfe64bda28367526761eb57e0392eb104b7fdf225`.
- Corrette tre difformità residue emerse dal nuovo G3: locuzione sulle plasticizzazioni a C8.4.2, punto elenco della resistenza a trazione prima di [C8.7.2.11], interpolazione «rispettivamente» a C8.8.5.
- G0-G7: tutti `OK`.
- Copertura: 58/58 pagine, 113/113 unità, 49 formule numerate, 2 relazioni non numerate, 425 occorrenze inline, 8 tabelle con 611 celle dati e 50 intestazioni.
- G3 finale: 195/195 scarti adjudicati, `ERR-MD=0`, `DUBBIO=0`.
- G4 finale: `ERR-MD=0`, `ERR-AUDIT=0`, `DUBBIO=0`.
- G6 indipendente cieco: `SUPERATO`, `ERR-MD=0`, `ERR-AUDIT=0`, `DUBBIO=0`; esito congelato SHA-256 `2f9403a74db0dba3847a443dd2f07b933da6943e3f70464f64b561ceaba006dd`.
- Manifest formale SHA-256 `6071ee53c6b274ec7e64a918254944b3ce179d0cb747b181b4d00620215e58c8`; verbale in `../verifica-conformita/verbale-VC-CAP08-2026-07-29.md`.
- Registro: 113/113 unità `COMPLETA/OK`; master autonomo `VC-OK al 2026-07-29`; master corpus invariato `VC-DA-FARE`; lint 0 errori e 0 avvisi.

Tutti i verificatori erano agenti AI. Non è stata eseguita una revisione umana integrale.

**Firma:** CDX (Codex), coordinatore del rilascio.

## 2026-07-29 - Correzione mirata post-G6 r02 superata

Corretto esclusivamente `ERR-MD-001` nel paragrafo C8.8.7 di
`8-esistenti.md`: la frase `superiore al 10%.` è stata ricomposta nel
primo punto elenco, in coerenza con la fonte ufficiale.

- Snapshot iniziale SHA-256:
  `255a090a8a8c4786b6fc1c4d092d34788756dd54d7a059681cc900c71a945f81`.
- Snapshot finale SHA-256:
  `97adcfa92cef5451cc12bc18ff210ec93601074fcd23f9a4a14877db470ab893`.
- Diff limitato alla sola ricomposizione autorizzata.
- Struttura Markdown e HTML: quattro elementi nello stesso elenco; nessun
  capoverso autonomo contenente la frase corretta.
- Render integrale rigenerato: 72 pagine, nessuna pagina vuota; controllo
  visivo mirato della pagina 71: PASS.
- Regressioni: 59/59 controlli PASS, con 20 heading NTC, 93 heading
  Circolare, 49 formule, 8 tabelle, 2 collegamenti e 0 pattern OCR
  vietati.
- Lint: 0 errori, 0 avvisi e 74 informazioni.
- Evidenze:
  `../_tmp_render/cap08/vc-cap08-20260729-correzione-g6-r02-r01/`.

Esito: **correzione post-G6 r02 PASS**. `ERR-MD-001` è chiuso sul nuovo
hash. La fase non è un nuovo G6 integrale, non modifica i registri e non
assegna `VC-OK`.

**Firma:** CDX (Codex), ruolo correzione post-G6 r02.

## 2026-07-29 - G6 indipendente r02 non superato

Eseguito il nuovo G6 source-first sullo snapshot SHA-256
`255a090a8a8c4786b6fc1c4d092d34788756dd54d7a059681cc900c71a945f81`,
senza modificare `8-esistenti.md`.

- Perimetro: 58/58 pagine ufficiali, 20 unità NTC, 93 unità Circolare, 49 formule numerate, 8 tabelle e 2 collegamenti.
- Due passaggi AI indipendenti A/B, riconciliati sul PDF; chiusi sei errori di audit mediante ritagli ingranditi, compresi il segno `-0,225`, `l_o`, la disuguaglianza `≤ 1` e il punto in `M_{e.Rd}`.
- Formule: 49/49 `OK`. Tabelle: 8/8 `OK` o `NORM`, con 581 posizioni logiche sorgente e 611 celle dati Markdown per la colonna `Categoria` resa esplicita nella C8.7.6.3.I.
- Render integrale: 72 pagine, nessuna pagina vuota; 2/2 collegamenti validi.
- Rilievo aperto `ERR-MD-001`: in C8.8.7 la frase `superiore al 10%.` appartiene al primo punto elenco della fonte, ma nel Markdown è resa come paragrafo autonomo dopo la chiusura del primo elenco.
- L'audit correttivo precedente aveva controllato la pagina e superato 53/53 test, ma non includeva un controllo sulla continuità HTML di questo punto.
- Evidenze: `../_tmp_render/cap08/vc-cap08-20260729-g6-r02/`; esito provvisorio immutabile SHA-256 `e2572a6c45798e98d8df342d9309d6acee66b89ddad45199cd1e3a77691aa7b2`.

Esito: **G6 NON SUPERATO**. Nessun `VC-OK`; stati di dettaglio e master
invariati. La correzione dell'unico errore dovrà avvenire in una fase
successiva distinta, con rigenerazione del render e ricontrollo del punto.

**Firma:** CDX (Codex), ruolo G6.

## 2026-07-29 - Correzioni post-G6 concluse

Conclusa la fase correttiva conseguente al G6 non superato del 2026-07-28.
Il file `8-esistenti.md` è passato dallo snapshot SHA-256
`a9b649bb8aa5a8cb45369f18e627a1663bf52379c0b1f98b072ac71af5f10f7a`
allo snapshot SHA-256
`255a090a8a8c4786b6fc1c4d092d34788756dd54d7a059681cc900c71a945f81`.

- Corrette le nove famiglie rilevate dal G6: indici di `zeta` e prodotto `a_g S`; segno della formula C8.7.2.1; tre occorrenze di `l_o`; indici e simbolo `theta` nel giunto; residuo OCR presso C8.7.2.13; tilde autonome; formule inline ed enumerazioni a)-d); confini LC1-LC3; sottotitoli e casi interni.
- Preservate le anomalie della fonte già censite, compresi `Tabella C.8.5.III`, `C8..5.4.3`, `0.35`, `M_{e.Rd}`, l'assenza di spazio fra `V_j` e `indica`, la ripetizione `in questa in questa categoria` e il richiamo `(4)` orfano.
- Evidenze: `../_tmp_render/cap08/vc-cap08-20260729-correzioni-r01/`, con snapshot, pagine fonte, 14 ritagli, diff, manifest, controlli e render integrale.
- Controlli automatici: 53/53 PASS. Render matematico: 68 pagine, nessuna pagina vuota; controllo visivo mirato PASS.
- Lint del registro di dettaglio: 0 errori, 0 avvisi, 74 informazioni relative a riferimenti di riga stantii.

La correzione non costituisce un G6 indipendente. Lo stato resta prudenziale:
111 unità `IN_CORSO/NON_VALUTATO`, 2 unità `COMPLETA/OK`, nessun `VC-OK`.
Il nuovo snapshot dovrà essere sottoposto a un G6 separato mediante
`../PROMPT-RIPRESA-CAPITOLO-8-G6-R02.md`.

**Firma:** CDX (Codex), ruolo correzione post-G6.

## 2026-07-28 - Controllo indipendente G6 non superato

Eseguito il controllo G6 source-first sullo snapshot SHA-256 `a9b649bb8aa5a8cb45369f18e627a1663bf52379c0b1f98b072ac71af5f10f7a`, senza applicare correzioni al file vivo.

- Perimetro: 58/58 pagine PDF, 20 unità NTC, 93 unità Circolare, 49 formule numerate, 8 tabelle e 2 collegamenti.
- Esito apparati: tabelle 8/8 conformi; struttura numerata completa; 1 formula numerata non conforme; notazioni inline, residui OCR e struttura semantica interna non conformi.
- Esito finale: **G6 NON SUPERATO**, 9 famiglie `ERR-MD`, 3 `ERR-AUDIT`, nessun dubbio.
- Rilievo sostanziale: `[C8.7.2.1]` nella fonte ha esponente `-0.225`; il precedente audit F02-F05 aveva adjudicato erroneamente il segno come positivo e aveva promosso la regressione.
- Altri rilievi aperti: indici `ζ_E`, `ζ_V,i` e altre notazioni non resi; `l_o` trascritto `l_0`; `θ` sostituita da `{`; residui `M e. Rd LV Ty`, `ÁÑR` e tilde; sottotitoli e casi interni fusi nella prosa.
- Evidenze: `../_tmp_render/cap08/vc-cap08-20260728-g6-r01/`; esito provvisorio immutabile SHA-256 `29b9a44231ab78d95305a0948d061454b9212bedf32d928e81dd3e856b5a95ed`.
- Stato delle unità invariato e prudenziale: 111 `IN_CORSO/NON_VALUTATO`, 2 `COMPLETA/OK` nei precedenti perimetri specialistici. Nessun `VC-OK`.

**Firma:** CDX (Codex), ruolo G6.

## 2026-07-28 - Audit integrale source-first r02

Ripreso dopo il crash l'audit VC-8 del Capitolo 8, conservando intatta la revisione r01 e producendo le nuove evidenze in `../_tmp_render/cap08/vc-cap08-20260728-r02/`.

- La sezione NTC del file vivo era una sintesi incompleta. È stata sostituita con la trascrizione integrale ricavata dalle pagine ufficiali 293-299: confronto normalizzato 5.319 token fonte contro 5.319 token Markdown, 0 scarti; la sezione viva coincide integralmente con la trascrizione ricostruita, al netto delle terminazioni di riga.
- La pagina file 281 della Circolare, pagina stampata 277, non possiede un text layer utile ed era stata saltata dalla conversione. Il controllo visivo del render ha consentito di reintegrare il seguito sulle resistenze residue, le formule [C8.7.1.17]-[C8.7.1.18], il § C8.7.1.3.1.2, l'inizio del § C8.7.1.3.2 e la nota 4.
- Risolti i rilievi strutturali RC1-RC2, l'heading spurio C8.5.3.2, la collocazione delle Tabelle C8.5.V-VI e numerosi simboli matematici alterati nell'OCR. Gli a-capo LC1-LC3 sono stati ricomposti e i rinvii interni riallineati agli heading effettivi.
- Controlli finali sul file vivo: 113 heading di paragrafo univoci, 49 tag formula univoci, 8 tabelle con colonne coerenti, 91 link a heading validi, 0 sintassi footnote standard, 0 caratteri di controllo e 0 glifi sospetti.
- Il confronto automatico della prosa della Circolare resta assistivo e non conclusivo a causa degli apparati, del LaTeX e della pagina senza text layer: i 132 gruppi di scarto sono stati riesaminati sul contesto e sui render nei punti sostanziali.
- Il registro di dettaglio è stato riallineato alle nuove righe: tutte le 113 unità del Capitolo 8 sono strutturalmente mappate; 111 restano `IN_CORSO/INTEGRALE`, mentre i due esiti specialistici già chiusi restano `COMPLETA/OK`. Il controllo indipendente G6 non è stato eseguito in questa sessione, quindi non viene dichiarato `VC-OK`.

**Firma:** CDX (Codex).

## 2026-07-17 (sera) - Lotto C8-T03: Tabelle C8.5.V e C8.5.VI conformi

Audit VC8-G4-TF (A/B Fable/Opus, concordanza 100%, recheck fresco 4/4) su Tabelle C8.5.V-VI e note esplicative. Corrette 4 famiglie: maiuscole "Livello di Indagini e Prove", punto finale spurio della didascalia VI, enfasi ***limitato/esteso/esaustivo***, blocco note rispezzato nei 6 capoversi della fonte. Snapshot `a3ee349b…` → `0f364296…`. Evidenze in `../verifica-conformita/audit-C8-T03-20260717/`. Rilievo collaterale: le Tabelle V-VI giacciono nel MD sotto l'heading duplicato C8.5.3.2 (md 543, generato dallo spezzamento del riferimento "(v. § C8.5.2.2 e C8.5.3.2)" del capoverso di p. 267-268): ricollocazione al lotto prosa. Lotto C8-T04 (Tab. C8.7.6.3.I) interrotto su richiesta a passaggi in corso, da rilanciare. Firma: CC, Fable 5.

## 2026-07-17 - Lotto C8-T02: Tabelle C.8.5.III e C8.5.IV conformi

Audit VC8-G4-TF a doppio passaggio indipendente (subagenti Fable 5 e Opus, riconciliazione CC) sul 100% delle 48 posizioni logiche, con recheck 5/5 di verificatore fresco. Evidenze in `../verifica-conformita/audit-C8-T02-20260717/`.

- Corrette 4 famiglie di difformità (E1-E4): nella nota (*) della Tab. C.8.5.III ripristinato il **refuso della fonte "τ"** ("purché si adotti un valore di τ almeno pari a 3") che la conversione aveva reso con κ — la fonte stampa nettamente tau, per quanto il contesto tratti il coefficiente κ: anomalia della fonte da conservare, qui registrata; rimossa una virgola aggiunta dopo "C.8.5.I)"; tolto il punto finale aggiunto alla didascalia della Tab. C8.5.IV (la fonte termina senza punto); ripristinate le enfasi semantiche della Tab. C8.5.IV (10 locuzioni in grassetto corsivo *indagini/prove limitate-estese-esaustive* e 3 etichette LC in grassetto).
- Snapshot: pre-audit `612a2c00…` → post-correzioni `a3ee349b…`; diff limitato alle sole righe 521, 531, 535-537 (porzioni del pilota C8-T01/F01 invariate).
- Rilievi collaterali FUORI perimetro, aperti per il lotto prosa: RC1 = capoverso del §C8.5.4.2 troncato "…ci si può riferire alla Tabella" (manca "C8.5.IV.", md 527); RC2 = heading H2 spurio "C8.5. Definizione del modello…" interposto a md 529. Censiti sulla riga CIRC-C8.5.4.2 del registro di dettaglio (trasposizione retrocessa a PARZIALE).

Firma: CC (Claude Code), Fable 5.

## 2026-07-14 - Preparazione del pilota di conformità C8

Adottato il nuovo protocollo di conformità documentale per tabelle e formule, registrato nella skill `controllo-serrato-ntc2018`.

### Stato

- La Circolare C8 è convertita, ma non è ancora dichiarata conforme secondo il nuovo criterio a doppio controllo indipendente.
- Gli audit del 2026-06 restano materiale sorgente utile, ma non provano da soli la corrispondenza di ogni cella e di ogni simbolo.
- Il controllo comprenderà le 8 tabelle Markdown, le 47 formule esposte taggate e gli apparati inline o non numerati censiti direttamente sul PDF.

### Primo lotto

- `C8-T01`: Tabelle C8.5.I e C8.5.II.
- `C8-F01`: formule C8.5.4.1-C8.5.4.3 e definizioni collegate di `X̄`, `κ` e `σ'²`.
- Creare l'audit datato in `_tmp_render/cap08/conformita-tabelle-formule-AAAAMMGG-r01/` all'avvio effettivo, con snapshot e hash delle fonti.

Nessuna modifica applicata a `cap08/8-esistenti.md` in questa fase.

**Firma:** CDX (Codex).

## 2026-06-18 - Note locali Circolare C8

Intervento eseguito da CDX sul file `cap08/8-esistenti.md`, limitato alla resa Markdown delle note fonte della Circolare C8.

### Esito

- Sostituita la sintassi footnote Markdown `[^1]`, `[^2]`, `[^3]` con richiami locali `[1]`, `[2]`, `[3]`.
- Le definizioni sono ora rese subito dopo il punto richiamato come `**Nota 1.**`, `**Nota 2.**`, `**Nota 3.**`.
- Motivazione: nei viewer Markdown le footnote standard vengono spesso raccolte in fondo al file, rendendo poco agevole la lettura del capitolo.
- Testo delle note invariato rispetto alla normalizzazione precedente; la nota 3 resta quella recuperata dal PDF sorgente.

### Controlli finali

- 0 sintassi footnote Markdown residua.
- 0 richiami nota incollati residui (`sismiche1`, `operativa2`, `sperimentali3`).
- 47 tag formula C8 invariati.
- 0 tabelle Markdown con numero colonne incoerente.

## 2026-06-16 - Reflow paragrafi Circolare C8

Intervento eseguito da CDX sul file `cap08/8-esistenti.md`, limitato alla sezione `# Circolare`, dopo segnalazione di a-capo anomali nella lettura Markdown.

### Esito

- Uniti i paragrafi della Circolare C8 che erano fisicamente spezzati a larghezza fissa dalla conversione PDF.
- Rimosse 54 righe vuote interne a frasi, riconosciute con criterio prudente: riga precedente terminante con parola e riga successiva iniziante con minuscola.
- Ridotte da 1729 a 0 le coppie di righe prose spezzate fuori dai blocchi formula.
- Normalizzati i richiami di nota `1`, `2`, `3`; stato finale aggiornato il 2026-06-18 con note locali, vedi sezione precedente.
- Recuperata dal PDF sorgente la nota 3, che nel Markdown precedente aveva il richiamo ma non il testo della nota.
- Titoli, tabelle Markdown e formule LaTeX non sono stati modificati.
- Restano 8 punti sospetti non uniti automaticamente perché richiedono controllo contenutistico sulla fonte PDF, non solo reflow.

### Controlli finali

- Testo normalizzato della Circolare invariato.
- 47 tag formula C8 invariati.
- 86 righe tabellari invariati.
- 98 titoli della Circolare invariati.
- 0 tabelle Markdown con numero colonne incoerente.

### Artefatti di controllo

`_tmp_render/cap08/reflow-c8-circolare-20260616/`

`_tmp_render/cap08/note-c8/nota-3-c8.5.4.png`

## 2026-06-11 - Conversione Markdown formule C8

Conversione eseguita da CDX sul file `cap08/8-esistenti.md`, sostituendo i richiami immagine delle formule della Circolare C8 con blocchi LaTeX Markdown.

### Esito

- Convertite 47 formule esposte C8 in LaTeX Markdown, mantenendo i tag originali.
- Rimossi dal testo i 47 richiami immagine formula precedenti.
- Controllato il caso `C8.7.2.7a` / `C8.7.2.7b`, perché i primi ritagli agganciavano un richiamo testuale e non la formula esposta: il blocco finale è stato letto dal ritaglio sorgente corretto.
- Corretto anche il testo/formula non numerato sotto `C8.8.5.1`: `q = mS_e(T)/F_y` e `m = \sum m_i\Phi_i`.

### Controlli finali

- 47 tag formula C8 in LaTeX.
- 0 richiami immagine formula residui.
- 8 tabelle Markdown nel file.
- 0 tabelle Markdown con numero colonne incoerente.
- 0 caratteri di controllo residui.

### Artefatti di controllo

`_tmp_render/cap08/controllo-formule-c8-md-wide/`

## 2026-06-11 - Conversione Markdown tabelle C8

Conversione eseguita da CDX sul file `cap08/8-esistenti.md`, sostituendo i richiami immagine delle tabelle della Circolare C8 con tabelle Markdown.

### Esito

- Convertite 8 tabelle ufficiali C8 in Markdown: C8.5.I, C8.5.II, C.8.5.III, C8.5.IV, C8.5.V, C8.5.VI, C8.7.6.3.I, C8.7.6.3.II.
- Rimossi dal testo i 10 richiami immagine tabellari precedenti.
- Accorpamenti PDF normalizzati: valori ripetuti nelle celle logiche coperte, non lasciati vuoti. Esempi controllati: `13 ÷ 16 (**)` in C8.5.I, geometrie ripetute su LC1-LC3 in C8.5.IV, categorie ripetute nella colonna `Categoria` in C8.7.6.3.I.
- Trascritte in testo anche le note interne alle tabelle che prima erano leggibili solo nei ritagli PDF.
- Stato successivo nello stesso giorno: le formule esposte sono state convertite in LaTeX Markdown, vedi sezione precedente.

### Controlli finali

- 8 tabelle Markdown nel file.
- 0 tabelle Markdown con numero colonne incoerente.
- 0 richiami immagine tabellari residui.
- 47 richiami immagine formula al termine della sola conversione tabellare, poi rimossi nella conversione formule del 2026-06-11.
- 0 caratteri di controllo residui.

### Artefatto di controllo

`_tmp_render/cap08/controllo-md-tabelle-c8/controllo-md-tabelle-c8.md`

## 2026-06-10 - Controllo accorpamenti tabelle C8

Controllo mirato eseguito da CDX sulle tabelle della Circolare C8 dopo segnalazione sulle celle accorpate nei PDF. Esito superato dalla conversione Markdown del 2026-06-11.

### Esito

- Stato del 2026-06-10, poi superato il 2026-06-11: nel file vivo `cap08/8-esistenti.md` le tabelle C8 non erano ancora rese come tabelle Markdown, ma come ritagli fonte PDF.
- Verificati esempi di accorpamento in C8.5.I, C8.5.II, C8.5.IV, C8.5.V, C8.5.VI, C8.7.6.3.I e C8.7.6.3.II.
- Regola confermata: se una cella PDF e' accorpata su piu' righe o colonne, in una futura tabella Markdown/CSV il valore deve essere ripetuto in tutte le celle logiche coperte. Una cella vuota e' ammessa solo quando nel PDF il valore e' davvero assente, non quando prosegue una cella accorpata.
- Nessuna modifica applicata a `cap08/8-esistenti.md` nella sessione del 2026-06-10, perche' in quel momento i ritagli PDF preservavano la struttura originale.

### Artefatto di controllo

`_tmp_render/cap08/controllo-accorpamenti-tabelle-c8/controllo-accorpamenti-tabelle-c8.md`

## 2026-06-09 - Riconversione Circolare C8

Riconversione eseguita da CDX sul file `cap08/8-esistenti.md`, sostituendo la sezione `# Circolare` generata in precedenza.

### Esito

- Fonte usata: `raw/Circolare-7-2019-NTC.pdf`, pp. PDF 253-303 circa.
- Testo C8 rigenerato dal PDF mantenuto, con titoli normalizzati in Markdown e rimozione dell'avviso di non affidabilità.
- Tabelle ufficiali C8 rese come ritagli fonte PDF in `cap08/img/`: 8 tabelle, 10 immagini collegate perché C8.7.6.3.I e C8.7.6.3.II sono multipagina.
- Formule esposte rese come ritagli fonte PDF in `cap08/img/`: 47 formule collegate nella riconversione del 2026-06-09, poi sostituite da formule LaTeX il 2026-06-11. Il tag `C8.7.1.17` risulta nel testo PDF come richiamo a un'equazione citata, non come formula esposta autonoma da ritagliare.
- Copia della versione precedente: `_tmp_render/cap08/riconversione-c8/8-esistenti-before-riconversione-20260609.md`.
- Script ripetibile: `_tmp_render/cap08/riconversione-c8.py`.

### Controlli finali

- 8 tabelle ufficiali collegate come ritagli fonte.
- 47 formule esposte collegate come ritagli fonte.
- 0 immagini mancanti nei richiami di `cap08/8-esistenti.md`.
- 0 tabelle Markdown con colonne incoerenti.
- 0 caratteri di controllo residui nel file riconvertito.

## 2026-06-09 - Controllo serrato fonte vs Markdown

Controllo eseguito con skill `controllo-serrato-ntc2018` su:

- Norma cap. 8, PDF `raw/NTC_18 con segnalibri (X.x.x.).pdf`, pp. PDF 293-300.
- Circolare C8, PDF `raw/Circolare-7-2019-NTC.pdf`, pp. PDF 253-302 circa.
- File Markdown `cap08/8-esistenti.md`.

### Esito

- Norma cap. 8: nessuna figura e nessuna tabella. Non sono emersi apparati da correggere, ma il controllo non certifica ancora la letteralità integrale del testo riga per riga.
- Circolare C8: controllo bocciato per fedeltà testuale. Il Markdown contiene molta parafrasi e non può essere trattato come trascrizione fonte-fedele.
- Stima automatica sulla Circolare: 11 blocchi lunghi riconosciuti su 410, 399 non riconosciuti nel testo PDF estratto.
- Tabelle censite: 8. C8.5.I e C8.5.II risultano sostanzialmente allineate; C8.5.III, C8.5.IV, C8.5.V, C8.5.VI, C8.7.6.3.I e C8.7.6.3.II sono da riconvertire.
- Formule: 48 tag formula nel Markdown e 48 tag nel PDF, ma diversi contenuti non corrispondono. Mancano i tag PDF C8.7.4.7a e C8.7.4.7b; il Markdown contiene invece C8.7.4.7.

### Errori principali

- C8.5.4.1-C8.5.4.3: nel PDF sono formule bayesiane su media e varianza a priori; nel Markdown sono formule diverse su `f_m`, `tau_0,m`, `E_m`.
- C8.5.III: tabella `kappa` errata e troppo ridotta.
- C8.5.IV-VI: tabelle semplificate, con perdita di colonne ufficiali, note e condizioni.
- C8.7.2.1-C8.7.2.13: formule in parte rinumerate o sostituite; per esempio C8.7.2.1 nel PDF è la rotazione ultima `theta_u`, nel Markdown è `M_y`.
- C8.7.4.6-C8.7.4.8: formule di confinamento e incamiciatura non fedeli; mancano C8.7.4.7a e C8.7.4.7b.
- C8.7.6.3.I-II: le tabelle ufficiali sugli elementi non strutturali e sul gas sono state sostituite da schemi sintetici non presenti nella fonte.
- C8.8.5.1-C8.8.5.5: formule sui ponti esistenti non fedeli alla fonte.

### Artefatti di audit

Cartella audit:

`_tmp_render/cap08/audit-cap08-fonte-vs-md/`

File principali:

- `cap08-controllo-serrato-registro.md`
- `cap08-tabelle-fonte-vs-md-registro.csv`
- `cap08-tabelle-fonte-vs-md-01.png`
- `cap08-tabelle-fonte-vs-md-02.png`
- `cap08-tabelle-fonte-vs-md-03.png`
- `cap08-tabelle-fonte-vs-md-04.png`

### Decisione operativa

La Circolare C8 va riconvertita dal PDF prima di essere usata come fonte Markdown affidabile. Fino alla riconversione, usare il PDF ufficiale mantenuto in `raw/` e questo registro per sapere quali parti sono state controllate.
