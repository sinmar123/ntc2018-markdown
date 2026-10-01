# Scope formale NTC 2018 § 3.3 + Circolare § C3.3

Data di congelamento: 2026-08-06

## Identità dello scope

- ID master autonomo: `ntc2018--norme-costruzioni--cap03-3-3`.
- ID operativo: `ntc2018-3.3`.
- Tipo record: `DOCUMENTO`.
- Protocollo: `VC-8`, con sottoprotocollo specialistico `VC8-G4-TF` per tabelle e formule.
- Oggetto: D.M. 17 gennaio 2018, § 3.3 «Azioni del vento», e Circolare 21 gennaio 2019 n. 7 C.S.LL.PP., § C3.3.

## Perimetro normativo

- D.M. 17 gennaio 2018: pagine fisiche PDF **56-60** della copia ufficiale congelata, 5 pagine. Confini accertati a vista sulla fonte e non dedotti da un registro: non ci sono pagine condivise con i paragrafi contigui. Rettifica del 6/8 pomeriggio: sulla p. 56 il § 3.3 comincia **in testa alla pagina**, non a metà, come si era scritto all'apertura del G0.
- Circolare 21 gennaio 2019 n. 7 C.S.LL.PP.: pagine fisiche PDF **54-75** della copia ufficiale congelata, 22 pagine. La sola p. 54 è condivisa con la coda del § C3.2, che resta esclusa.
- Totale: **27 pagine fisiche**. Paginazione accertata sui piedini: pagina fisica = pagina Gazzetta + 4.
- Inventario delle unità: **45 unità** nel registro di dettaglio, 11 NTC e 34 Circolare, tutte `COMPLETA`, nessuna `DA_VERIFICARE`.
- Sono compresi testo, titoli, commi, elenchi, note normative, formule esposte numerate e non numerate, matematica inline, definizioni, simboli, unità, tabelle, figure, richiami e struttura.

## Inventario ricavato dal file, non dalle intenzioni

Verificato meccanicamente sullo snapshot congelato, come impone il § 10 del ciclo dopo il caso del § 4.1, dove lo scope dichiarava fuori perimetro due capoversi che il Markdown invece conteneva.

| Elemento | Quantità | Dettaglio |
|---|---|---|
| Heading | 47 | 11 NTC (§ 3.3 e §§ 3.3.1-3.3.10), 34 Circolare (§ C3.3 e discendenti fino a C3.3.11), più i due separatori `# Norma` e `# Circolare` |
| Formule con tag | 20 | 8 NTC: `[3.3.1]`, `[3.3.1.b]`, `[3.3.2]`-`[3.3.7]`; 12 Circolare: `[C3.3.1]`-`[C3.3.12]`. Nessun tag duplicato |
| Tabelle | 22 | 3 NTC: Tab. 3.3.I, 3.3.II, 3.3.III; 19 Circolare: Tab. C3.3.I-C3.3.XIX |
| Figure | 31 | 3 NTC e 28 Circolare, tutte presenti su disco, nessun richiamo ripetuto |
| Apparato di navigazione | 40 wikilink, 9 ancore `^` | Resta nel file ed è escluso meccanicamente dai pacchetti dei blocchi ciechi del G6, § 5 del ciclo |
| Placeholder | 0 | Nessun `[Da completare]` né residuo di lavorazione |

I 47 heading meno i 2 separatori danno le 45 unità del registro: **la corrispondenza fra scope dichiarato e file reale è verificata**, non asserita.

## File e fonti congelati

- `verifica-conformita/fonte-ufficiale/GU-2018-42-SO8-DM-17-01-2018.pdf`, SHA-256 `dda1e397d56d71aa0f5bc457c3ba9b77064a468699dfc37bd056ac6c47105a46`;
- `verifica-conformita/fonte-ufficiale/GU-2019-35-SO5-Circolare-7-2019.pdf`, SHA-256 `f7c3b8d1f443aadb6b3e020b6b6c19813683492ecaadd2c15bf6bf1939aaed7c`;
- `cap03/3.3-vento.md`, SHA-256 `e3d8f75e0c0abc45a5fd5ae024a879478e3635c9a2949fcc28c330fc37abd8d5`, 970 righe;
- `cap03/indice-cap03.md`;
- 31 asset immagine collegati dal file normativo.

Entrambi gli hash delle fonti sono stati **ricalcolati** il 2026-08-06 e coincidono con quelli congelati il 2026-08-05.

Il presente documento, il verbale, la scheda di scope, le annotazioni di `cap03/annotazioni/` e i registri appartengono al governo della verifica e non sono file immutabili dello scope.

## Esclusioni

- D.M. 17 gennaio 2018: contenuto precedente al § 3.3 e successivo al § 3.3.10.
- Circolare 21 gennaio 2019 n. 7 C.S.LL.PP.: contenuto precedente a C3.3, compresa la coda del § C3.2 sulla p. fisica 54, e contenuto successivo a C3.3.11.
- Gli altri paragrafi del Capitolo 3, cioè 3.1, 3.2, 3.4, 3.5 e 3.6, e le corrispondenti sezioni della Circolare, che restano nei rispettivi file.
- Le unità superiori `3` e `C3`, l'intero Capitolo 3 e l'intero corpus NTC 2018.
- Giudizi sulla correttezza tecnica delle prescrizioni normative. In particolare, le tre anomalie della fonte registrate in `cap03/annotazioni/3.3-anomalie-fonte.md` sono conservate come stampate: il corpus attesta che il Markdown coincide con la Gazzetta, non che la Gazzetta sia corretta.
- Garanzie sulla vigenza successive alla data della presente ricognizione.

## Vincolo amministrativo

Le 45 unità di dettaglio conservano il collegamento al registro vigente. Un eventuale giudizio autonomo sarà attribuito soltanto al master `ntc2018--norme-costruzioni--cap03-3-3` e non promuoverà le unità `3` e `C3`, il Capitolo 3 o la riga master del corpus.

## Stato del congelamento

Catena degli hash di `cap03/3.3-vento.md` in questa giornata:

- `97adc4ab0e8aeb55ce2d6502d209e3abed6f94cfade6f2b786601aceb9d5012f` — congelato all'apertura del G0, 966 righe;
- `dae92970806bcdda5391b000162d8dc44badd20166d3f7ba6e335f20dfbe87f0` — 968 righe, dopo l'inserimento della nota di trascrizione `AF-COR-3.3-01` prodotta dal G4 sulle tabelle NTC;
- `d2e1eb41e27ea588f73f0cd799c714009a742a02f7ba9ecbb1ae322f9bc9181e` — 970 righe, 76.574 byte, dopo la fase correttiva del pomeriggio del 6/8/2026: 40 occorrenze in dieci famiglie di difformità accertate da G2 e G4, più la nota `AF-COR-3.3-02`;
- `e3d8f75e0c0abc45a5fd5ae024a879478e3635c9a2949fcc28c330fc37abd8d5` — **corrente**, 970 righe, 76.703 byte, dopo l'adjudicazione dei rilievi B1-B6 nella ripresa serale del 6/8/2026: sei correzioni con prova inversa del diff, annotazioni `AF-3.3-09…13`. Nella stessa ripresa il G4 è stato completato sulle 31 figure, con tre asset PNG corretti (C3.3.4, C3.3.14, C3.3.19) senza toccare il Markdown.

| Gate | Stato | Nota |
|---|---|---|
| G0 Identità e scope | **OK** | Questo documento. Inventario ricavato dal file e coincidente con le 45 unità a registro |
| G1 Fonte ufficiale e vigenza | **OK**, con limite dichiarato | `g1-fonte-e-vigenza.md`. Hash ricalcolati; ricognizione del 2026-08-04 riusata e verificata su questo perimetro: l'unico atto successivo, D.M. 9 marzo 2023, tocca l'art. 2 e i punti 11.4.2 e 11.5.2, tutti fuori scope. Normattiva non indicizza questi due atti: la verifica si fa sulla Gazzetta Ufficiale |
| G2 Completezza strutturale | **OK**, con limite dichiarato | `g2-esito.md`. Inventario source-first sulle **pagine rese**, otto verificatori ciechi sul Markdown, uno per blocco di 2-4 pagine. 45 titoli, 20 formule numerate, 22 tabelle, 31 figure e 2 formule esposte senza tag: coincidono uno a uno con l'inventario del Markdown. Il G2 non copre la coincidenza del **testo** di ciascuna unità, che è del G3 e, sulla Circolare, del G6 |
| G3 Conformità testuale integrale | **PARZIALE** | `g3-esito.md`. Parte NTC: confronto macchina completo e pulito, 0 scarti di prosa in entrambe le direzioni, i 5 scarti lato fonte sono apparato e vanno a G4. Parte Circolare: **non eseguibile per intero a macchina**, perché il livello testo perde intere proposizioni ovunque la frase contenga un simbolo. Quella copertura va acquisita dal G6 per via visiva |
| G4 Apparati non testuali | **OK** | `g4-esito-tabelle-ntc.md`, `g4-esito.md`, `g4-figure/00-esito-figure.md`. Le **3 tabelle del decreto** confrontate a macchina e riscontrate a 600 dpi (Tab. 3.3.II chiusa in classe C, `AF-COR-3.3-01`); le **20 formule** e le **19 tabelle della Circolare** confrontate il pomeriggio del 6/8 con dieci famiglie di difformità corrette, fra cui un `cos²` reso `cos` e tre `≤` resi `<` nella [C3.3.5]; le **31 figure** confrontate la sera del 6/8 da sei verificatori ciechi: 28 conformi, 3 asset incompleti corretti dai raster nativi (C3.3.4, C3.3.14 dimezzata, C3.3.19), 0 dubbi, 0 difformità di didascalia |
| G5 Struttura e navigazione | **OK** | `g5-navigazione.py`: 31 immagini tutte presenti, 2 link relativi validi, 40 wikilink tutti risolti, 47 heading senza duplicati, 29 rinvii dell'indice di capitolo tutti risolti, riga di navigazione conforme. 0 errori, 0 avvisi |
| G6 Seconda verifica indipendente | `DA_FARE` | Da eseguire in cieco, 7-8 blocchi da 3-4 pagine, con un blocco duplicato cross-famiglia per la misura del § 12 |
| G7 Congelamento e impronte | `DA_FARE` | |

Rilievi aperti al 6/8/2026, ripresa serale: **0**. I sei criteri di resa (A1-A6)
sono stati decisi da Sandro e sono le voci 13-18 delle normalizzazioni dichiarate;
le sei segnalazioni dei verificatori (B1-B6) sono state adjudicate sulla fonte,
con esito in `_tmp_render/cap03/vc-3.3-260806/adjudicazione/b/00-esito-b1-b6.md`.
Prossimo gate: G6, da instradare su un agente diverso da CC (§ 6.7 del ciclo).

Nessuno stato `VC-OK` è attribuito. Il master del corpus resta `VC-DA-FARE`.

Firma del redattore: Claude Code / CC
Modello: `claude-opus-5[1m]`
Livello di ragionamento: `max`
Data: 2026-08-06

Controlli eseguiti da agente AI, senza revisione umana integrale.
