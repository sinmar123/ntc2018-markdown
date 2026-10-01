---
scope_id: ntc2018-3.3
atti:
  - "D.M. 17/01/2018, § 3.3 Azioni del vento"
  - "Circolare 21/01/2019 n. 7 C.S.LL.PP., § C3.3"
file_markdown: _tmp_render/ricomposizione-livello3-20260826/archivio-file-sostituiti/cap03/3.3-vento.md
struttura_corrente: cap03/indice-3.3.md
fonte_ntc: {pdf: verifica-conformita/fonte-ufficiale/GU-2018-42-SO8-DM-17-01-2018.pdf, pagine_fisiche: 56-60}
fonte_circolare: {pdf: verifica-conformita/fonte-ufficiale/GU-2019-35-SO5-Circolare-7-2019.pdf, pagine_fisiche: 54-75}
unita_registro: 45
formule_numerate: 20
tabelle: 22
figure: 31
pagine_fonte: 27
stato: SOSPESO
validita_corrente: SCADUTA
agente: CDX
macchina: P53
presa_in_carico: 2026-08-06T18:38:20+02:00
giro_g6: 1
max_giri: 3
rilievi_aperti: 32
rilievi_persistenti: 0
gate: {G0: OK, G1: OK, G2: OK, G3: PARZIALE, G4: OK, G5: OK, G6: KO, G7: DA_FARE}
snapshot_sha256: e3d8f75e0c0abc45a5fd5ae024a879478e3635c9a2949fcc28c330fc37abd8d5
snapshot_precedente: d2e1eb41e27ea588f73f0cd799c714009a742a02f7ba9ecbb1ae322f9bc9181e  # prima dell'adjudicazione B1-B6
attesa_decisione: []
prossimo_passo: "autorizzato il 2026-08-29: nella nuova sessione aprire il solo scope naturale 3.3.1 e proseguire in sequenza fino al 3.3.10; il G6 r01 resta evidenza storica e non è riprendibile sulla struttura nuova"
esecutori:
  g2: {inventario-source-first: "8 blocchi, CC/opus-5"}
  g4: {formule: "4 blocchi, CC/opus-5", tabelle: "4 blocchi, CC/opus-5", adjudicazione: "CC/opus-5"}
  adjudicazione-b: {esecutore: "CC/fable-5, ripresa serale 6/8"}
  g4-figure: {verificatori: "6 blocchi, subagenti CC/fable-5", adjudicazione: "CC/fable-5"}
  g6-1:
    coordinamento: "CDX/gpt-5.6-sol/xhigh, compatibile con § 6.7"
    inventario: "subagente fresco P2/gpt-5.6-sol/xhigh, fonte-prima"
    blocchi: "B01 NTC 56-58; B02 NTC 59-60 + CIRC 54; B03 CIRC 55-57; B04 CIRC 58-60; B05 CIRC 61-63; B06 CIRC 64-67; B07 CIRC 68-71; B08 CIRC 72-75; tutti primari P2/gpt-5.6-sol/xhigh"
    duplicato: "B05 CIRC 61-63: secondo contesto fresco gpt-5.6-terra/xhigh, cross-family supplementale per la sola misura; copertura e giudizio autoritativi restano al verificatore P2 Sol e all'adjudicatore"
    metriche: "per esecutore: rilievi emessi, confermati, falsi positivi, DUBBIO; sul duplicato: |A|, |B|, |A∩B| sui confermati e stima cattura-ricattura se definita; globali: pagine, righe Markdown, asset e apparati coperti, ERR-MD, ERR-AUDIT, DUBBIO"
    esito: "G6 KO: 32 ERR-MD confermati, 7 ERR-AUDIT da quattro difetti radice dei confini, 0 DUBBIO residui; 2 falsi positivi primari e 1 supplementale correlato"
    evidenze: "_tmp_render/cap03/vc-3.3-260806/g6-r01/05-esito-consolidato-g6-r01.md"
---

## 2026-08-29 - autorizzata la ripresa sui file naturali (CDX)

Sandro ha autorizzato la VC completa dei dieci file naturali 3.3.1-3.3.10 per la nuova sessione. Il presente scope aggregato resta `SOSPESO` e con validità `SCADUTA`: non viene riattivato. I 32 `ERR-MD` del primo G6 restano candidati storici da ricollocare e verificare contro la fonte nei nuovi scope. La ripresa apre il solo 3.3.1 e procede in sequenza; il § 3.4 resta fuori perimetro.

## 2026-08-26 - scope storico scaduto per ricomposizione editoriale (CDX)

Il file aggregato `cap03/3.3-vento.md` è stato archiviato con hash nella ricomposizione generale dei capitoli lunghi. La struttura corrente è governata da `cap03/indice-3.3.md` e comprende introduzione, dieci file naturali NTC/Circolare e un file della sola Circolare. Lo scope resta `SOSPESO` come stato storico del G6 r01, ma la sua validità corrente è `SCADUTA`: i 32 `ERR-MD`, i 7 `ERR-AUDIT` e le altre evidenze non sono trasferiti automaticamente ai nuovi documenti.

Per riprendere la VC occorre aprire nuovi scope sui singoli file naturali, mantenendo il vecchio audit soltanto come antecedente documentale.

## 2026-08-06 - G6 r01 eseguito, G6 KO e scope sospeso (CDX)

Primo giro integrale eseguito sullo snapshot
`e3d8f75e0c0abc45a5fd5ae024a879478e3635c9a2949fcc28c330fc37abd8d5`:
inventario fonte-prima congelato prima della riconciliazione, otto blocchi ciechi
P2 Sol e duplicato B05 su Terra, con CC escluso da ogni ruolo. Le 27 pagine e i
31 asset sono stati aperti, ma quattro confini Markdown-pagina hanno impedito la
copertura bidirezionale integrale: righe 0376-0378, 0457-0497, 0684-0696 e
0800-0810.

Esito dopo adjudicazioni a 600 dpi o su raster nativo: 32 `ERR-MD` confermati,
7 `ERR-AUDIT`, 0 `DUBBIO` residui, 2 falsi positivi primari. Il candidato comune
alle due famiglie sulla testata della Tabella C3.3.XI è stato refutato: la fonte
stampa davvero `Θ – 0°`; la stima cattura-ricattura sui confermati non è quindi
definita. Rilievi congelati in
`_tmp_render/cap03/vc-3.3-260806/g6-r01/04-rilievi-congelati.md`; esito
autoritativo in `05-esito-consolidato-g6-r01.md`, SHA-256
`ba2f84176a77dd1cdc0519b1faeabc5b33a333297b7423ebeca5cc6e0bfa09c4`.

Il Markdown vivo è rimasto invariato. `G6=KO`, `giro_g6=1`; stato `SOSPESO` in
attesa di autorizzazione alla fase correttiva distinta e al ridisegno dei
pacchetti. G7 non è stato avviato e nessun registro è stato promosso.

## 2026-08-06 - lucchetto CDX e disegno G6 r01 congelato prima del giro (CDX)

Precondizioni di apertura ricontrollate sul P53: SHA-256 NTC
`dda1e397d56d71aa0f5bc457c3ba9b77064a468699dfc37bd056ac6c47105a46`,
Circolare
`f7c3b8d1f443aadb6b3e020b6b6c19813683492ecaadd2c15bf6bf1939aaed7c`
e Markdown
`e3d8f75e0c0abc45a5fd5ae024a879478e3635c9a2949fcc28c330fc37abd8d5`:
tutti coincidenti con i valori congelati. Nessun altro scope usa
`cap03/3.3-vento.md`.

Disegno r01 congelato prima dell'inventario e dei confronti, ai sensi dei §§ 6 e
12 del ciclo:

1. B01: NTC pp. fisiche 56-58, 3 pagine;
2. B02: NTC pp. 59-60 più Circolare p. 54, 3 pagine, limitando p. 54 al solo
   § C3.3;
3. B03: Circolare pp. 55-57, 3 pagine;
4. B04: Circolare pp. 58-60, 3 pagine;
5. B05: Circolare pp. 61-63, 3 pagine, duplicato cross-family per la misura;
6. B06: Circolare pp. 64-67, 4 pagine;
7. B07: Circolare pp. 68-71, 4 pagine;
8. B08: Circolare pp. 72-75, 4 pagine.

Ogni pagina appartiene a un solo blocco primario. I confini di pagina non si
spostano durante il giro. Gli intervalli Markdown, anche non contigui per B02,
saranno derivati meccanicamente e congelati nel manifest di confezionamento prima
di avviare i verificatori. I pacchetti conterranno soltanto pagine rese a 200 dpi
o più, testo estratto dichiarato ausiliario, estratti Markdown privati di
navigazione e asset collegati; non conterranno conteggi attesi, registri, verbali,
rilievi storici, README, TODO, CHANGELOG o annotazioni pregresse. Tutti riceveranno
il canone neutro delle tre classi e delle 18 normalizzazioni dichiarate, senza
esempi tratti dallo scope.

Esecutori congelati: inventario fonte-prima in contesto fresco P2
`gpt-5.6-sol/xhigh`; otto blocchi primari in otto contesti freschi P2
`gpt-5.6-sol/xhigh`; B05 duplicato in un contesto fresco
`gpt-5.6-terra/xhigh` per la sola misura cross-family, senza sostituire la lettura
P2; coordinamento e adjudicazione CDX P2, compatibile col § 6.7. CC è escluso da
ogni ruolo nel G6.

Metriche congelate: per ogni esecutore rilievi emessi, confermati, falsi positivi
e tasso di `DUBBIO`; sul duplicato `|A|`, `|B|`, `|A∩B|` calcolati sui rilievi
confermati e stima cattura-ricattura solo se matematicamente definita; sul giro
copertura di pagine, righe Markdown, asset e apparati, più totali `ERR-MD`,
`ERR-AUDIT` e `DUBBIO`. Il Markdown vivo resta in sola lettura. Nessun G7 e
nessuna promozione sono autorizzati.

## 2026-08-05 - apertura, precondizioni assolte e bonifica pre-G0 avviata (CC)

Scope aperto a valle della decisione di lavorarlo **intero**, senza spezzarlo: 27 pagine fonte e 20 formule numerate stanno sotto entrambe le soglie del § 4.B.6. La densita' e' pero' in tabelle e figure, quindi al G6 la partizione andra' fatta a **7-8 blocchi da 3-4 pagine** invece dei 5 usati sul § 4.2-a, con un blocco duplicato cross-famiglia per la misura prevista dal § 12.

**Precondizioni § 4.A assolte.** Hash delle due fonti ricalcolati e coincidenti con i registrati: NTC `dda1e397…`, Circolare `f7c3b8d1…`. Lucchetto libero, nessun altro scope su `cap03/3.3-vento.md`.

**Precondizione § 4.B.4 gia' soddisfatta**: 45 unita' a registro (11 NTC, 34 Circolare), tutte `COMPLETA`, nessuna `DA_VERIFICARE`. E' la differenza principale rispetto al § 4.2, che ne aveva 72 aperte.

**Confini § 4.B.5 accertati a vista**, non dedotti: § 3.3 NTC alle pagine fisiche 56-60, senza pagine condivise; § C3.3 Circolare alle 54-75, con la sola p. 54 condivisa con la coda di C3.2. Ritagli in `_tmp_render/cap03/bonifica-3.3-260805/confini/`.

**Apparato delle formule conforme**: 8 tag NTC e 12 Circolare, coincidenti uno a uno con la fonte in numero e forma.

Bonifica pre-G0 avviata e **non conclusa**: vedi la voce seguente. Il G0 non si apre finche' non e' chiusa, perche' ogni modifica successiva al congelamento riaprirebbe i gate, che e' l'incidente occorso al § 4.2-a.

Evidenze: `_tmp_render/cap03/bonifica-3.3-260805/00-confini-e-dimensionamento.md`.

## 2026-08-05 - bonifica pre-G0, stato al momento della sospensione (CC)

**Fatto.**

1. Indice interno e note redazionali portati fuori dal file normativo, per il § 5 «Il file normativo contiene solo la fonte»: il file passa da 1050 a 962 righe. Le 8 note stanno in `cap03/annotazioni/3.3-note-redazionali.md`, l'indice e' stato tolto perche' `indice-cap03.md` ne conteneva gia' uno piu' ricco, integrato con le 10 voci mancanti.
2. Correzioni applicate, tutte accertate sulla fonte congelata:
   - **12 occorrenze di `c_f` portate a `c_F`** (Tab. C3.3.XV, XVI, XVII e testo di raccordo). La fonte usa `c_F` per il coefficiente di forza; `c_f` minuscolo e' il coefficiente d'attrito, e il Markdown fondeva due grandezze. Restano minuscole le sole 4 occorrenze dell'attrito, corrette.
   - didascalia Tab. C3.3.VIII: reintegrato `(α in °)` che la fonte stampa;
   - didascalia Tab. C3.3.XVI: `falda doppia` riportato a `doppia falda`;
   - Tab. C3.3.XI: tolta la colonna «Caso» con diciture assenti dalla fonte, sotto-righe rese ripetendo α, reintegrata la riga d'intestazione `Direzione del vento Θ = 0°`.
3. Classificate 3 tabelle su 10 contro la fonte: C3.3.VIII 60/60 valori coincidenti, C3.3.XI 110/110, C3.3.XVI tutte. **Le correzioni pregresse del maggio-giugno risultano riallineamenti verso la fonte, non modifiche della fonte: nessuna nota `AF-COR` dovuta.**

**Da fare alla ripresa.**

1. Classificare le 7 tabelle restanti: C3.3.I (p. 56), II (p. 57, **solo 173 dpi nativi**), IV (p. 59), V (p. 59), VII (p. 61), X (p. 62), XIV (p. 65). Per V e X il registro di revisione dichiarava «differenze solo in alcuni estremi `<`/`≤`, ininfluenti»: **da riesaminare**, perche' i versi di disuguaglianza sono fra i glifi che il canone non lascia toccare.
2. Riancorare alla GU congelata i riferimenti di pagina del registro di revisione cap03 e dell'annotazione `tab-c3.3.i-refuso-cu.md`, che citano il PDF `_rid` cancellato. **Non serve toccare il registro di dettaglio da 1724 righe**: verificato che i PDF di `raw/` hanno la stessa paginazione delle GU congelate.
3. Annotare `AF-3.3-01` (rilievo R6) in `cap03/annotazioni/`.
4. Congelare lo snapshot e aprire G0.

**Rilievi aperti: 2.**

- **R4**, decisione di indirizzo in `attesa_decisione`: la fonte stampa i punti di moltiplicazione (`0,7·|α|/30`) che il Markdown omette. La classe N ammette di aggiungere `\cdot` dove la fonte giustappone, non di toglierlo dove la fonte lo stampa. Riguarda tutto il corpus.
- **R6**, classe A: la didascalia della Tab. C3.3.XVII dice «tettoie a semplice falda» mentre la tabella riguarda le falde multiple. Accertato che **la Gazzetta stampa cosi'**: il Markdown e' fedele, l'anomalia e' della fonte. Refuso di contenuto, non correggibile nemmeno con nota, da scalare a Sandro.

**Scoperte di metodo, valide oltre questo scope.**

- Le tabelle della Circolare **sono immagini raster incorporate**, non testo: 145 nelle pagine dello scope, risoluzione nativa fra 173 e 354 dpi. I 600 dpi che il § 7 pretende **non sono raggiungibili**: oltre il nativo si interpola. La prova si ottiene estraendo il raster incorporato, non ri-renderizzando la pagina, e la lettura dei codepoint del § 7.2 li' non e' applicabile. Le tabelle dell'NTC sono invece testo regolare.
- **Le parentesi quadre dei tag di formula non si estraggono come quadre**: nelle due GU lo stesso `[…]` esce come `> … @`, `" … #` o `[ … ]` secondo il font. Ogni controllo automatico sui tag deve cercare il contenuto e non i delimitatori, e i verificatori ciechi vanno avvertiti che su questo apparato il testo estratto mente.

Mappa didascalia-raster delle 19 tabelle in `_tmp_render/cap03/bonifica-3.3-260805/mappa-tabelle.json`; raster nativi in `tabelle/native/`; rilievi in `01-rilievi-bonifica.md`; copia del file prima della bonifica in `3.3-vento.PRIMA.md`.

Stato `SOSPESO` e non `IN-CORSO`: la sospensione e' deliberata, per riprendere a contesto pulito. Chi riprende puo' prendere il lucchetto senza chiedere.

Controlli eseguiti da agente AI, senza revisione umana integrale.

## 2026-08-06 - ripresa: classificate le 7 tabelle restanti, 14 correzioni, mappa dei ritagli rifatta (CC)

Lucchetto preso a norma del § 2: la scheda era `SOSPESO` con sospensione deliberata.

**Decisioni prese da Sandro all'apertura della sessione.** R4, punti di
moltiplicazione: si **ripristina il `·`** dove la fonte lo stampa; la classe N
resta a una via sola, si aggiunge dove la fonte giustappone e non si toglie mai
dove la fonte lo stampa. Vale per tutto il corpus. R6, didascalia incongrua della
Tab. C3.3.XVII: **classe A**, si conserva e si annota, nessuna nota nel file
normativo. Entrambi tolti da `attesa_decisione`.

**Le 7 tabelle restanti sono state classificate**, una per verificatore in
contesto separato, poi adjudicate da chi coordina sulla fonte congelata. Esito:
**nessuna delle 7 era conforme**. Dettaglio in
`_tmp_render/cap03/bonifica-3.3-260805/02-rilievi-bonifica-260806.md`.

**Due errori di metodo scoperti, che invalidano prove del 5/8.**

1. `mappa-tabelle.json` e' sbagliata su **I, II, III, IV** e incompleta su **XI**.
   Tre verificatori l'hanno scoperto indipendentemente: i ritagli consegnati non
   contenevano le tabelle dichiarate. La C3.3.XI e' spezzata in **due raster
   affiancati** e la mappa ne copriva uno solo, tagliando via la colonna J: il
   «110/110 coincidono» del 5/8 era stato ottenuto su un ritaglio mutilo. Oggi
   riverificato ricomponendo i due raster, e l'esito regge. Mappa rifatta dalla
   fonte in `mappa-tabelle-260806.json`, con un campo che dice quali voci sono
   accertate e quali no.
2. La «scoperta di metodo» del 5/8 secondo cui **tutte** le tabelle della Circolare
   sono raster **e' vera solo in parte**: C3.3.I, II e III sono testo vettoriale, e
   li' i 600 dpi e la lettura dei codepoint del § 7.2 sono applicabili. Corretto il
   `CLAUDE.md` di progetto, che diffondeva la versione sbagliata.

**14 correzioni applicate**, tutte adjudicate sulla fonte da chi coordina e tutte
difformi sotto qualunque politica, quindi lecite anche in attesa delle decisioni di
indirizzo (§ 8). La piu' grave e' **C1**: la Tab. C3.3.X riga 525 dava
`c_pe,A = −0,8 − α/150` dove la Gazzetta stampa `− 0,8 **+** α/150`. Era l'unico
difetto che cambia un numero usato in progetto, con discontinuita' di 0,4 al bordo
dell'intervallo. Seguono 4 versi di disuguaglianza in C3.3.V e uno in C3.3.X, che
nel 2026 il registro di revisione aveva archiviato come «differenze solo in alcuni
estremi, ininfluenti»: non lo erano, e il canone non lascia toccare quei glifi.

Controlli dopo le correzioni: 23 tabelle, **0 righe con numero di colonne
incoerente**; nessun residuo delle diciture inventate.

**Quattro rilievi nuovi, tutti chiusi in giornata.**

- **R7**, deciso da Sandro: la Gazzetta stampa `c_pe = -0,5 - -0,8·h/d` nella
  Tab. C3.3.I, con **due meno consecutivi**, accertato sia sui codepoint (tre
  U+002D distinti, a x 231,2 / 243,9 / 247,9) sia a 1200 dpi. E' un refuso di
  contenuto: alla lettera dà un valore discontinuo di 0,8 al bordo dell'intervallo.
  Il canone vieta di correggere un segno anche con nota (§ 5, classe C, condizione
  4), e il file conteneva la forma corretta senza dichiararlo, cioè una correzione
  silenziosa. **Scelta: conservare alla lettera**, classe A, con annotazione
  `AF-3.3-02`. Applicato.
- **R8**, deciso da Sandro: la fonte chiude le didascalie di tabella con il punto
  fermo, il nostro corpus lo omette su tutte e 19. **Scelta: classe N dichiarata
  nel verbale**, nessun file toccato, qui né negli altri capitoli. Da riportare nel
  verbale di G7 insieme alle altre normalizzazioni sistematiche.
- **R9**, deciso da Sandro: le testate a più livelli venivano appiattite e la parola
  «Zona» spariva. **Scelta: schema C3.3.XI ovunque**, cioè riga della fascia, riga
  delle lettere di zona, riga dei sottocampi. Applicato a C3.3.II (2 righe di
  testata) e C3.3.IV (3 righe). Nessuna parola della fonte più omessa.
- **R10**, adjudicato da chi coordina: in 6 celle della zona I di C3.3.IV, blocco
  «Con parapetti», la fonte stampa `± 0.2` con spazio e **punto** decimale, mentre
  tutte le altre celle stampano `±0,2`. Confermato dal confronto affiancato delle
  celle sul raster nativo a 348 dpi: punto sulla linea di base senza discendente,
  contro la virgola con discendente delle altre. Classe A, conservato, annotato
  come `AF-3.3-03`.

**Convenzione degli accorpamenti, chiarita e uniformata.** Il corpus era incoerente.
Regola messa in atto, ricavata dallo schema C3.3.XI scelto da Sandro: nelle
**testate** l'etichetta che copre più colonne si scrive una volta sola e le celle
coperte restano vuote; nel **corpo**, sia i valori sia le etichette di riga si
ripetono in tutte le celle logiche coperte. Uniformate su questa base C3.3.X (2
etichette su 5 righe), C3.3.XIV (10 righe, 19 colonne) e C3.3.XV.

**Annotazioni create**: `cap03/annotazioni/3.3-anomalie-fonte.md` con AF-3.3-01,
AF-3.3-02 e AF-3.3-03, indicizzate nel README delle annotazioni con l'avvertenza di
leggerle prima di usare quelle tabelle in un calcolo. Aggiunta l'ancora
`^tab-c3-3-xvii`, che mancava. Allineato `tab-c3.3.i-refuso-cu.md`, che riportava la
formula col meno singolo e ora rinvia ad AF-3.3-02.

Controlli finali: 23 tabelle, **0 righe con numero di colonne incoerente**; nessun
wikilink delle annotazioni con ancora inesistente; 966 righe.

Controlli eseguiti da agente AI, senza revisione umana integrale.

## 2026-08-06 - riancoraggio delle pagine, snapshot congelato, G0 superato (CC)

**Riancoraggio, ultimo punto della lista del 5/8.** Il registro di revisione
`cap03/cap03-azioni-sulle-costruzioni-revisione.md` rinviava a un PDF `_rid`
cancellato, con un offset stimato «≈ +4». Sostituito con l'ancoraggio accertato
sulla fonte congelata: **pagina fisica = pagina Gazzetta + 4**, § C3.3 alle pagine
fisiche 54-75, e rinvio alla mappa `mappa-tabelle-260806.json` per la posizione
tabella per tabella con la natura dell'apparato. Il registro di dettaglio da 1724
righe non e' stato toccato, come gia' accertato il 5/8.

**Corrette due affermazioni sbagliate dello stesso registro**, con un blocco datato
che non riscrive la storia ma la rettifica: la riga «in V e X differenze solo in
alcuni estremi `<`/`≤`, ininfluenti» era falsa due volte, perche' quelle differenze
erano difformita' nostre e perche' i versi di disuguaglianza non sono normalizzabili
per canone; e la Tab. C3.3.X non era «OK senza modifiche», visto che conteneva il
segno invertito. Aggiunta l'avvertenza che il controllo del 29/5/2026 va letto come
stato di lavorazione e non come attestazione di conformita'.

**Snapshot congelato**: `cap03/3.3-vento.md` SHA-256
`97adc4ab0e8aeb55ce2d6502d209e3abed6f94cfade6f2b786601aceb9d5012f`, 966 righe,
74.893 byte. Hash delle due fonti **ricalcolati** e coincidenti con i congelati:
NTC `dda1e397…`, Circolare `f7c3b8d1…`.

**G0 superato.** Documento di scope in
`verifica-conformita/scope-NTC2018-3.3-2026-08-06.md`. L'inventario e' stato
**ricavato dal file e non dalle intenzioni**, come impone il § 10 del ciclo dopo il
caso del § 4.1: 47 heading meno i 2 separatori `# Norma` e `# Circolare` danno
esattamente le **45 unita'** del registro, 11 NTC e 34 Circolare. Contati anche 20
formule taggate senza duplicati (8 NTC, 12 Circolare), 22 tabelle (3 NTC, 19
Circolare), 31 figure tutte presenti su disco e nessun richiamo ripetuto, 0
placeholder. Script riproducibile: `inventario-g0.py`.

**G1 lasciato deliberatamente `DA_FARE`.** Le fonti sono congelate e gli hash
ricalcolati, ma la ricognizione degli aggiornamenti normativi successivi alla data
odierna non e' stata eseguita in questa sessione: dichiararlo superato sarebbe
un'attestazione non provata.

Controlli eseguiti da agente AI, senza revisione umana integrale.

## 2026-08-06 - G1 e G5 superati, G3 parziale per un difetto della fonte (CC)

**G1 `OK` con limite dichiarato.** Evidenza in `_tmp_render/cap03/vc-3.3-260806/g1-fonte-e-vigenza.md`.
Hash delle due fonti ricalcolati. La ricognizione di vigenza del 2026-08-04 e' stata
**riusata e non rifatta**, dichiarandolo, e verificata su questo perimetro: l'unico
atto successivo censito, D.M. 9 marzo 2023 `23A01847`, tocca l'articolo 2 del decreto
e i punti 11.4.2 e 11.5.2, tutti fuori dal § 3.3. Accertato inoltre che **Normattiva
non indicizza** ne' il D.M. 17/01/2018 ne' la Circolare 7/2019, perche' sono atti con
testo tecnico in allegato pubblicati in Supplemento Ordinario: la verifica di vigenza
di questo corpus si fa sul sito della Gazzetta Ufficiale e non e' automatizzabile.

**G5 `OK`.** Script `g5-navigazione.py`: 31 immagini tutte presenti su disco, 2 link
relativi validi, 40 wikilink tutti risolti a file, heading o ancore reali, 47 heading
senza duplicati, 29 rinvii dell'indice di capitolo tutti risolti, riga di navigazione
conforme. Zero errori e zero avvisi.

**G3 `PARZIALE`, e la ragione e' una scoperta che vale per tutto il corpus.**
Evidenza in `g3-esito.md`, strumento `g3-confronto-testuale.py`.

- **Parte NTC: confronto macchina completo e pulito.** 2.292 parole di fonte contro
  1.808 di prosa Markdown, 1.805 allineate; **zero scarti lato Markdown** e cinque
  lato fonte, tutti apparato — i valori delle Tab. 3.3.I, II e III e le formule
  [3.3.7] e [3.3.1.b] — presenti nel file come tabelle e LaTeX e quindi di
  competenza del G4. Il livello testo dell'NTC e' sano: 0,3% di caratteri corrotti.
- **Parte Circolare: il confronto macchina non e' eseguibile per intero.** Il livello
  testo e' composto in un font a codifica rimappata, e quando una frase contiene un
  simbolo inline **si corrompe l'intera proposizione che lo contiene**, non il solo
  simbolo. A p. fisica 57 la Gazzetta stampa «Per gli edifici bassi, ossia con
  altezza minore o uguale della dimensione in pianta ortogonale al flusso del vento
  (h ≤ b), l'altezza di riferimento…» e l'estrazione restituisce `$ ++ + x", l'altezza
  di riferimento…`: la proposizione iniziale non c'e'. Verificato che stringhe come
  `ossia con altezza minore`, `Si definisce grado di bloccaggio` e `tettoia libera`
  **non compaiono in nessuna pagina** del PDF pur essendo stampate. Misura: 7,7% di
  caratteri di controllo sulle pp. 54-75, contro lo 0,3% dell'NTC, e la percentuale
  sottostima il danno perche' ogni grumo sta al posto di testo leggibile assente.

Conseguenza, registrata anche nel `CLAUDE.md` di progetto: **un confronto testuale
automatico sulla Circolare misura una frazione del contenuto stampato, e la frazione
che perde e' concentrata dove il testo tocca le grandezze**, cioe' dove un errore
peserebbe di piu'. Quella copertura si acquisisce solo per via visiva, a blocchi,
come fa il G6. E' anche la spiegazione del perche' sul § 4.1 il G6 trovo' dieci
difetti che tre controlli automatici precedenti non avevano visto.

Controlli eseguiti da agente AI, senza revisione umana integrale.

## 2026-08-06 - G4 parte NTC: le 3 tabelle del decreto, e la prima classe C del corpus (CC)

Chiusa la lacuna trovata in mattinata: la bonifica pre-G0 aveva classificato le 19
tabelle della **Circolare** e non le 3 del **decreto**. Qui il confronto e' possibile
a macchina, perche' il livello testo del D.M. ha lo 0,3% di caratteri corrotti contro
il 7,7% della Circolare. Evidenza in `g4-esito-tabelle-ntc.md`, strumento
`g4-tabelle-ntc.py`.

Il test non e' «il valore esiste da qualche parte nella pagina», che non prova nulla,
ma «la sequenza dei valori del Markdown compare **nello stesso ordine e di seguito**
nella fonte»: un valore giusto nella cella sbagliata fallisce. Al meccanico si somma
il riscontro visivo a 600 dpi, perche' il primo prova solo che due estrazioni
concordano.

- **Tab. 3.3.I**, p. fisica 56, 36 valori: **conforme**, comprese le descrizioni
  regione per regione e le parentesi delle eccezioni. Unica differenza, classe N: la
  fonte stampa la didascalia senza spazio dopo il trattino.
- **Tab. 3.3.II**, p. fisica 58, 15 valori: valori conformi, ma **l'intestazione
  della fonte stampa `K_r` con la maiuscola** e il nostro file scriveva `k_r` senza
  dichiararlo. Vedi sotto.
- **Tab. 3.3.III**, p. fisica **59** e non 58: **conforme**. Unica differenza, classe
  N: dove la fonte stampa quattro punti di sospensione il Markdown ne stampa tre.

Nota di metodo: anche qui la posizione di partenza era sbagliata, la Tab. 3.3.III e'
a p. 59. Stesso genere di errore della mappa delle tabelle della Circolare: una
posizione presa da un elenco invece che dalla fonte.

**Prima correzione di classe C del corpus: `AF-COR-3.3-01`.** La fonte e' incoerente
con se' stessa nello spazio di mezza pagina: alla stessa p. 58, la definizione che
segue la [3.3.7] stampa `k_r` minuscolo, l'intestazione della tabella `K_r`
maiuscolo. Accertato con entrambi i metodi del § 7, che concordano: a 600 dpi il
glifo ha la forma e l'altezza di una maiuscola, e l'estrazione restituisce `Kr`
nell'intestazione e `kr` nella definizione. Ricorrono tutte le condizioni del § 5:
difetto tipografico, lettura corretta attestata **dentro lo stesso atto e sulla
stessa pagina**, nessun glifo della lista vietata toccato perche' cambia solo la
cassa di una lettera, nessun valore alterato. E' la famiglia che il ciclo indica come
candidabile alla classe C nei propri esempi (`T_ed` per `T_Ed`). Il file conserva
`k_r` e porta accanto la nota prescritta: prima di oggi la stessa forma c'era ma
**senza dichiararla**, cioe' come correzione silenziosa.

**Nuovo snapshot**: `dae92970806bcdda5391b000162d8dc44badd20166d3f7ba6e335f20dfbe87f0`,
968 righe. Catena: `97adc4ab…` al G0, poi questo. Controlli rifatti sul nuovo
snapshot: 23 tabelle con 0 righe a colonne incoerenti, G5 rieseguito con 0 errori e
0 avvisi, G3 invariato con la nota `AF-COR` esclusa dal confronto come prevede il § 5.

**G4 resta `PARZIALE`**: coperta la parte NTC, restano le 19 tabelle della Circolare
da riprendere come evidenza di gate e non come lavorazione, piu' 20 formule e 31
figure mai inventariate contro la fonte in questo ciclo.

**Prossima azione**, invariata: G2 e il resto del G4, sapendo che sulla Circolare
l'inventario source-first va fatto sulle pagine rese e non sul livello testo. Poi il
G6 in cieco, che **non puo' essere ne' coordinato ne' eseguito da chi ha scritto
queste correzioni** (§ 6.7): va a un altro agente, a contesto pulito, partizionato in
7-8 blocchi da 3-4 pagine con un blocco duplicato cross-famiglia. Il disegno del G6
va congelato nella scheda **prima** del primo giro.

Controlli eseguiti da agente AI, senza revisione umana integrale.

## 2026-08-06 - chiusura di sessione, stato SOSPESO (CC)

Stato portato a `SOSPESO` **deliberatamente**, non per abbandono: la sessione si
chiude a lavoro coerente, con snapshot congelato, controlli rifatti e zero rilievi
aperti. Chi riprende puo' prendere il lucchetto senza chiedere, anche in giornata.

Senza questa riga, il § 2 avrebbe fermato la ripresa: una scheda `IN-CORSO` a nome
del proprio agente con presa in carico odierna non e' automaticamente una ripresa
dopo un crash, puo' essere un'altra sessione ancora aperta, e la regola impone di
chiedere prima di procedere.

Frasi di innesco per la ripresa: `riprendiamo VC 3.3`, che e' quella esatta ora che
la trasposizione e' chiusa, oppure `riprendiamo conversione 3.3`.

**Avvertenza per chi riprende.** Per G2 e per il resto del G4 va bene qualunque
agente. Per il **G6 no**: chi ha eseguito la fase correttiva del 6/8/2026 e' CC, e il
§ 6.7 gli vieta sia di coordinare sia di verificare. Instradare il G6 su Codex, che
oltre a rispettare la regola fornisce anche la famiglia diversa richiesta dal § 12
per il blocco duplicato.

Snapshot alla chiusura: `dae92970806bcdda5391b000162d8dc44badd20166d3f7ba6e335f20dfbe87f0`.

## 2026-08-06 (pomeriggio) - G2 superato, G4 esteso a formule e tabelle, 40 occorrenze corrette (CC)

Lucchetto preso alle 15:03 su sospensione deliberata, come previsto dalla voce
precedente. Hash delle due fonti ricalcolati e coincidenti.

**G2 `OK`.** L'inventario source-first e' stato costruito sulle **pagine rese**, non
sul livello testo, perche' il G3 aveva accertato che sulla Circolare l'estrazione
perde intere proposizioni. Otto verificatori in contesti separati, uno per blocco di
2-4 pagine fisiche, ciascuno con il divieto di aprire il Markdown, i registri e i
verbali; la riconciliazione l'ha fatta chi coordina, dopo. Esito: 45 titoli, 20
formule numerate, 22 tabelle e 31 figure, **coincidenti uno a uno** con l'inventario
del Markdown, piu' due formule esposte senza tag presenti in entrambi. Evidenza in
`g2-esito.md`, inventari in `g2/inventari/`.

Rettifica al documento di scope: la p. fisica 56 delle NTC **non e' condivisa** col
paragrafo precedente, il § 3.3 vi comincia in testa.

**G4 esteso.** Coperte le 20 formule e le 19 tabelle della Circolare, di cui 9 mai
riscontrate in questo ciclo. Le posizioni dei ritagli sono state ricavate dalla fonte
e non da mappe pregresse; a ogni verificatore e' stata data anche la pagina intera con
l'obbligo di controllare per primo che il ritaglio contenesse la tabella dichiarata.

**Dieci famiglie di difformita' accertate e corrette, 40 occorrenze.** Le due piu'
gravi cambiano un numero di progetto, entrambe nella `[C3.3.5]` del § C3.3.8.3:
il **`cos²` reso `cos`**, senza esponente, e **tre `<` dove la fonte stampa `≤`**.
Seguono quattro famiglie di simbolo sostituito, tutte accertate coi metodi del § 7:
`c_peo` con la lettera o, accertato sui **codepoint** `0x70 0x65 0x6f` della prosa
vettoriale di p. 71; `ψ_λα` reso `ψ_Mz`; `α_p` reso `α_P`; `v_m,l` e `n_k` resi
`v_m,i` e `n_i` nel § C3.3.11. Piu' `c_peA`, il punto fermo stampato dopo il tag
`[C3.3.2]`, il separatore decimale a punto di `[3.3.3]` e `[C3.3.2]`, la virgola della
didascalia della Fig. C3.3.1, la didascalia della Tab. C3.3.XII con due parole omesse,
nove celle accorpate lasciate vuote in C3.3.VI e C3.3.XII, e la parola «il» soppressa
a p. 70.

Tutte queste erano **correzioni silenziose verso la notazione corrente o verso
l'Eurocodice**: il canone le vieta perche' la forma «giusta» si ricava da conoscenza
esterna all'atto. Annotate come AF-3.3-04…08 e AF-COR-3.3-02.

**Diff confrontato con l'elenco dei rilievi**: 27 intervalli modificati, tutti
corrispondenti a un rilievo, nessuna riga estranea. Due righe di **testata** della
Tab. C3.3.XII erano state toccate per errore dallo script di ripristino degli
accorpamenti e sono state riportate alla forma originale: nelle testate la cella
coperta resta vuota, la ripetizione vale solo nel corpo.

**Nuovo snapshot**: `d2e1eb41e27ea588f73f0cd799c714009a742a02f7ba9ecbb1ae322f9bc9181e`,
970 righe, 76.574 byte. Catena: `97adc4ab…` (G0) → `dae92970…` → questo.
Controlli rifatti: G5 con 0 errori e 0 avvisi, 23 tabelle con 0 righe a colonne
incoerenti, inventario 45/20/22/31 invariato.

**Corretto anche `inventario-g0.py`**, che con la resa letterale `	ag*{[C3.3.2].}`
contava 19 formule invece di 20 **senza dare errore**. Stessa famiglia della soglia
del 55% che in `g4-localizza-formule.py` faceva sparire il tag `[C3.3.7]`, stampato al
53% della gabbia: un controllo automatico che manca il bersaglio tace, non protesta.

**Rilievi aperti: 12**, in `rilievi-aperti-260806.md`. Sei sono criteri di resa che
valgono per tutto il corpus e che il § 8 impone di far decidere a Sandro; sei sono
segnalazioni dei verificatori non ancora adjudicate sulla fonte da chi coordina.

**Le 31 figure non sono state confrontate con la fonte**: il G4 resta `PARZIALE`.

Il G6 non e' avviabile prima di aver chiuso quei dodici punti, e comunque non puo'
essere ne' coordinato ne' eseguito da CC (§ 6.7): va instradato su Codex.

Controlli eseguiti da agente AI, senza revisione umana integrale.

## 2026-08-06 (sera) - decisione di Sandro sui sei criteri di resa (CC)

Sandro ha scelto la **strada A**: i sei punti emersi da G2 e G4 restano come sono nei
file e si dichiarano come differenze di sola impaginazione. Sono le voci 13-18 di
`verifica-conformita/normalizzazioni-dichiarate-NTC2018.md`, che da oggi e' l'elenco
unico della classe N per tutto il corpus e va richiamato dal verbale di ogni G7.

Motivo della scelta, registrato perche' non vada perso: la strada alternativa avrebbe
costretto a riscrivere in HTML le tabelle che nella fonte non hanno riga di testata,
perche' il Markdown non sa farne senza, e avrebbe prodotto `Re` e `log10` in una forma
che un tecnico legge come errore di battitura. In nessuno dei sei punti cambia una
parola, una cifra o un significato.

`attesa_decisione` torna vuoto. Rilievi aperti da 12 a **6**: restano i soli B1-B6,
segnalazioni dei verificatori che chi coordina non ha ancora adjudicato sulla fonte.

Nessun file normativo toccato da questa decisione.

## 2026-08-06 (sera) - adjudicazione B1-B6: tutti decisi, sei correzioni, cinque annotazioni nuove (CC)

Lucchetto ripreso alle 16:56 su sospensione deliberata; hash delle fonti e dello
snapshot ricalcolati e coincidenti prima di toccare qualunque file.

**I sei punti B sono stati adjudicati sulla fonte con lo standard del § 7**: ritagli
a 600 dpi e codepoint per il testo vettoriale, raster nativi per gli apparati raster,
con un riscontro comparativo probante per il glifo della Tab. C3.3.XI (la gemella
C3.3.XII stampa l'`=` a due tratti alla stessa risoluzione; la XI stampa un tratto
solo). Esiti: **B1, B2, B3, B4, B5-segno confermati; B5-inciso refutato (corpus
conforme); B6 confermato come anomalia della fonte.** Rapporto completo con le prove:
`_tmp_render/cap03/vc-3.3-260806/adjudicazione/b/00-esito-b1-b6.md`.

**Sei correzioni applicate in cinque punti**: ripristinati alla lettera della fonte
il rinvio «Figura C.3.3.21» (p. 68), «riportati i Figura C3.3.16» (p. 64), la
didascalia «Figure C3.3.4» al plurale (didascalia e alt, p. 57) e la testata
«Direzione del vento Θ – 0°» della Tab. C3.3.XI (p. 63); reintegrato il testo esteso
del ramo b) della didascalia della Fig. C3.3.24 (p. 70), che il corpus abbreviava.
**Prova inversa eseguita**: riapplicando all'indietro le sei sostituzioni l'hash
torna esattamente allo snapshot di partenza, quindi il diff contiene solo i rilievi.

**Annotazioni**: nuove `AF-3.3-09…13`; sanata la sezione mancante di `AF-COR-3.3-02`,
la cui nota esisteva nel file normativo senza sezione nelle annotazioni (errore di
conversione per il § 5, trovato in questo giro). README delle annotazioni aggiornato.

**Nuovo snapshot**: `e3d8f75e0c0abc45a5fd5ae024a879478e3635c9a2949fcc28c330fc37abd8d5`,
970 righe, 76.703 byte. Catena: `97adc4ab…` → `dae92970…` → `d2e1eb41…` → questo.
Controlli rifatti: G5 con 0 errori e 0 avvisi; inventario invariato 45/20/22/31 con
28 didascalie e 0 placeholder; 23 tabelle con 0 righe a colonne incoerenti.

**Due falsi conteggi dello script `inventario-g0.py` corretti**: la regex delle
didascalie non riconosceva «Figure» al plurale (AF-3.3-11) e il conteggio placeholder
contava «metodo» come `TODO` per mancanza di word boundary.

Rilievi aperti: **0**. Resta il perimetro scoperto delle **31 figure** (G4
`PARZIALE`), affrontato nella fase successiva di questa stessa sessione.

Controlli eseguiti da agente AI, senza revisione umana integrale.

## 2026-08-06 (sera) - G4 completato: 31 figure confrontate con la fonte, tre asset corretti (CC)

**Era l'ultimo perimetro scoperto del G4.** Sei verificatori in contesti separati,
uno per blocco di 5-6 figure, ciascuno con i soli PNG del proprio pacchetto
(ritaglio corpus, pagine rese a 200 dpi, raster nativi alla risoluzione nativa) e il
canone neutro; didascalie trascritte a vista dalla pagina, mai dal testo estratto.
Le difformità adjudicate da chi coordina sulla fonte prima di ogni correzione.

**Esito: 31/31 figure, 28 conformi, 3 difformità di asset, 0 dubbi, 0 difformità di
didascalia.** Le tre difformità, tutte ritagli incompleti, sono state corrette in
giornata: C3.3.4 senza le tre quote «b» inferiori (sostituita col raster nativo
completo, 173 dpi nativi); **C3.3.14 dimezzata** — il ritaglio copriva solo lo
schema Θ=0° di p. 62 mentre la figura stampata comprende anche lo schema Θ=90° in
testa a p. 63, sopra la didascalia (ricomposta dai due raster nativi; adjudicata
sulla pagina resa); C3.3.19 con l'etichetta «(c)» mozzata (rigenerata sulle bbox
misurate). Versioni precedenti conservate in `g4-figure/fig-*-PRIMA-*.png`.

Le correzioni toccano **solo asset PNG**: lo snapshot `e3d8f75e…` del Markdown
resta invariato. G5 rieseguito sul corredo aggiornato: 0 errori, 0 avvisi.

Conferme incrociate: i verificatori ciechi hanno trascritto dalla fonte «Figure
C3.3.4» al plurale e la didascalia estesa della C3.3.24, confermando senza saperlo
le correzioni B3 e B4 del pomeriggio.

Nota di resa per il verbale di G7: nella didascalia della C3.3.3 il corpus aggiunge
una **virgola di giuntura** fra i rami a) e b) dove la fonte va a capo senza virgola
(in C3.3.2, C3.3.6 e C3.3.19 la virgola è invece stampata). Nessuna parola cambia;
da dichiarare insieme alla resa dell'etichetta in testa, o da togliere se si
preferisce la fedeltà stretta. Rapporto completo: `g4-figure/00-esito-figure.md`.

**Il G4 passa a `OK`**: tutti gli apparati non testuali dello scope hanno evidenza
di gate (3 tabelle NTC, 19 tabelle Circolare, 20 formule, 31 figure).

**Stato dello scope a fine giornata**: G0-G5 tutti `OK` tranne G3 `PARZIALE` per il
limite strutturale del livello testo della Circolare, che solo il G6 visivo può
coprire. Rilievi aperti: 0. **Prossimo passo: il G6 in cieco**, 7-8 blocchi da 3-4
pagine con un blocco duplicato cross-famiglia, disegno da congelare nella scheda
prima del primo giro. Il G6 **non può essere né coordinato né eseguito da CC**
(§ 6.7: CC ha firmato le fasi correttive del 6/8): va instradato su Codex.

Controlli eseguiti da agente AI, senza revisione umana integrale.
