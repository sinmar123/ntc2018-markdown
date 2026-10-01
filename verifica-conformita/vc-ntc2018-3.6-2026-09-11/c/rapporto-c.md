# Rapporto C - verifica normativa del § 3.6

Data: 2026-09-11  
Ruolo: C, confronto normativo indipendente G0 e G2-G4  
Firma: Codex / CDX

## Esito

Lo scope è nei limiti della procedura: 9 pagine fisiche dei PDF, 10 formule, 4 tabelle e 0 figure. Il confronto integrale ha prodotto 38 correzioni esatte: 27 rubriche e 11 punti di prosa o apparati. Non rimangono casi `DUBBIO`.

Giudizi:

- **G0: OK.** Perimetro, fonti congelate e separazione dei ruoli risultano determinati. Il controllo C non ha modificato i file normativi, i CSV o i file di governo.
- **G2: OK_CON_RILIEVI.** Coperti integralmente testo, rubriche, elenchi, note, didascalie e confini del § 3.6 NTC e C3.6. Sono state rilevate 38 difformità `ERR-MD`, elencate in `lista-correzioni.json`.
- **G3: OK_CON_RILIEVI.** Ogni residuo è stato classificato come normalizzazione dichiarata, anomalia della fonte da conservare o correzione esatta. Nessun residuo resta senza giudizio.
- **G4: OK_CON_RILIEVI.** Verificate tutte le 10 formule e tutte le celle delle 4 tabelle. I dati e gli operatori coincidono con la fonte, salvo il punto fermo terminale della formula [3.6.6] e l'espansione mancante della cella unita nella Tab. 3.6.III. Non vi sono figure.

Il giudizio C richiede l'applicazione delle 38 correzioni prima del controllo successivo. Questo rapporto non esprime un giudizio G1, G5 o G6.

## Fonti e impronte

- NTC 2018: `verifica-conformita/fonte-ufficiale/GU-2018-42-SO8-DM-17-01-2018.pdf`, SHA-256 `dda1e397d56d71aa0f5bc457c3ba9b77064a468699dfc37bd056ac6c47105a46`.
- Circolare 7/2019: `verifica-conformita/fonte-ufficiale/GU-2019-35-SO5-Circolare-7-2019.pdf`, SHA-256 `f7c3b8d1f443aadb6b3e020b6b6c19813683492ecaadd2c15bf6bf1939aaed7c`.

Nel rapporto, «pagina fisica» indica l'indice PDF 1-based. Le pagine fisiche NTC 66-71 corrispondono alle pagine stampate GU 62-67; le pagine fisiche Circolare 81-83 alle pagine stampate GU 77-79.

## Confini e mappa fonte-target

Il confine iniziale NTC è nella pagina fisica 66, dopo la conclusione del § 3.5.7. Il confine finale è nella pagina fisica 71, dopo il § 3.6.3.5 e prima del capitolo 4. Il confine iniziale della Circolare è nella pagina fisica 81, dopo C3.4.5 e C3.5. Il confine finale è nella pagina fisica 83, dopo C3.6.2.3 e prima di C4.

| Fonte | Contenuto | Target nel confronto |
|---|---|---|
| NTC, pagina fisica 66 | § 3.6; § 3.6.1 e § 3.6.1.1 fino alla formula [3.6.1] | `cap03/3.6-introduzione.md`; `cap03/3.6.1-azioni-eccezionali-incendio.md` |
| NTC, pagina fisica 67 | condizioni della [3.6.1], Tab. 3.5.IV, §§ 3.6.1.2-3.6.1.5 | `cap03/3.6.1-azioni-eccezionali-incendio.md` |
| NTC, pagina fisica 68 | §§ 3.6.1.5.1-3.6.1.5.4; formule [3.6.2]-[3.6.4] | `cap03/3.6.1-azioni-eccezionali-incendio.md` |
| NTC, pagina fisica 69 | § 3.6.2 completo; Tab. 3.6.I; formule [3.6.5a], [3.6.5b], [3.6.6] | `cap03/3.6.2-azioni-eccezionali-esplosioni.md` |
| NTC, pagina fisica 70 | § 3.6.3 fino a § 3.6.3.3.1; Tabelle 3.6.II e 3.6.III; formule [3.6.7]-[3.6.9] | `cap03/3.6.3-azioni-eccezionali-urti.md` |
| NTC, pagina fisica 71 | §§ 3.6.3.3.2-3.6.3.5 | `cap03/3.6.3-azioni-eccezionali-urti.md` |
| Circolare, pagina fisica 81 | C3.6; C3.6.1 e C3.6.1.1 | `cap03/3.6-introduzione.md`; `cap03/3.6.1-azioni-eccezionali-incendio.md` |
| Circolare, pagina fisica 82 | C3.6.1.2-C3.6.1.5.3 | `cap03/3.6.1-azioni-eccezionali-incendio.md` |
| Circolare, pagina fisica 83 | C3.6.1.5.3-C3.6.1.5.4; C3.6.2 e C3.6.2.3 | `cap03/3.6.1-azioni-eccezionali-incendio.md`; `cap03/3.6.2-azioni-eccezionali-esplosioni.md` |

La localizzazione iniziale «Circolare 81» non rappresenta l'intera estensione sostanziale: la copertura effettiva è 81-83. È sufficiente che scheda, note delle righe, rapporto e verbale conservino questa distinzione; il campo pagine del CSV non deve essere editato manualmente.

Il file storico monolitico `cap03/3.6-azioni-eccezionali.md` non appartiene al target. La riga corsiva `Circolare 21/01/2019 n. 7 C.S.LL.PP., §C3.6` è un apparato editoriale di identificazione dell'atto, non testo della Circolare: va esclusa meccanicamente dal pacchetto di confronto e dichiarata nella composizione. Non costituisce una correzione del target. La scelta è coerente con il trattamento già adottato per l'identica tipologia di riga nel § 3.5.

## Copertura G2

Sono stati confrontati senza campionamento:

- tutto il testo normativo NTC e della Circolare compreso nei confini;
- tutte le rubriche, compresi maiuscole, punteggiatura dopo l'identificatore e sottoparagrafi;
- tutti gli elenchi e le condizioni quantitative;
- tutte le didascalie e tutte le celle delle tabelle;
- tutti i rinvii interni e i numeri di paragrafo visibili nella fonte.

Le navigazioni Markdown, gli indici interni generati, le ancore HTML, le separazioni `Norma`/`Circolare` e il tag del visualizzatore delle formule sono apparati editoriali esclusi o normalizzati secondo catalogo. Sono state applicate, ove pertinenti, le normalizzazioni dichiarate N1-N6, N9-N12, N14 e N18. Non sono state ammesse riscritture sostanziali.

## Copertura G3 e rilievi

Le 38 correzioni sono congelate in `lista-correzioni.json`, con stringhe `prima` e `dopo` direttamente applicabili:

- 27 correzioni riportano le rubriche alla grafia della fonte, soprattutto maiuscolo integrale e assenza del punto dopo gli identificatori C3.6.x;
- 9 correzioni ripristinano parole, preposizioni o punteggiatura del testo ufficiale;
- 1 correzione ripristina il punto terminale della formula [3.6.6];
- 1 correzione espande la cella unita della Tab. 3.6.III secondo N6.

Cinque particolarità appartengono alla fonte e devono essere conservate o soltanto annotate:

1. **AF:** la tabella dei livelli di prestazione nel § 3.6.1 è numerata `Tab. 3.5.IV`. Il controllo precedente R5 era un'osservazione, non una base per rinumerare; la fonte conferma il numero.
2. **AF:** a pagina fisica NTC 69 la fonte reca `applicata da ogni direzione`. La forma è grammaticalmente anomala, ma va ripristinata al posto di `in ogni direzione`.
3. **AF:** la Circolare passa da C3.6.1.5.1 a C3.6.1.5.3, senza C3.6.1.5.2.
4. **AF:** C3.6.1.5.1 rinvia alle curve `citate nel paragrafo C3.6.1.1`, sebbene C3.6.1.1 contenga definizioni e non l'elenco delle curve. Il rinvio è fonte-fedele.
5. **AF:** a pagina fisica Circolare 83 la fonte reca `i requisiti ... sia previsto che siano mantenuti`; la discordanza grammaticale è fonte-fedele.

Non è necessario ribaltare il precedente controllo numerico delle Tabelle 3.5.IV, 3.6.I, 3.6.II e 3.6.III: valori e ordine erano stati giudicati correttamente. Va però aggiunta la correzione editoriale della cella unita della Tab. 3.6.III, che quel controllo non copriva.

## Copertura G4

Formule verificate integralmente:

- [3.6.1], incluse le tre condizioni successive `delta_q1 >= 1,00`, `delta_q2 >= 0,80` e `delta_n = prodotto da i=1 a 10 di delta_ni >= 0,20`;
- [3.6.2], [3.6.3], [3.6.4];
- [3.6.5a], [3.6.5b], [3.6.6];
- [3.6.7], [3.6.8], [3.6.9].

Numeri, indici, esponenti, operatori, parentesi e unità risultano corretti. L'aggiunta di `\cdot` dove la fonte usa la giustapposizione è consentita da N5. L'unica correzione di formula è il punto fermo che la fonte colloca alla fine della [3.6.6], prima del numero di formula. Le mappe caratteri del livello testuale PDF risultano in alcuni punti inaffidabili per simboli matematici; i glifi sono stati verificati sulle rese a 600 dpi e non rimane ambiguità da risolvere con codifica vettoriale ulteriore.

Tabelle verificate integralmente:

- Tab. 3.5.IV, 5 righe logiche;
- Tab. 3.6.I, 3 righe dati;
- Tab. 3.6.II, 3 righe dati;
- Tab. 3.6.III, 5 righe logiche.

Tutti i valori, le unità, le intestazioni, le didascalie e l'ordine delle righe coincidono. Nella Tab. 3.6.III la fonte unisce verticalmente `Aree di parcheggio e autorimesse` sulle ultime due righe: la rappresentazione Markdown deve ripetere l'etichetta nella seconda riga, secondo N6.

## Evidenze

Le nove pagine complete sono state rese a 200 dpi in `c/ntc-066.png`-`c/ntc-071.png` e `c/circ-081.png`-`c/circ-083.png`.

Gli apparati e la prosa sono stati verificati anche su ritagli a 600 dpi:

- `dettaglio-ntc066-formula-3.6.1.png`;
- `dettaglio-ntc067-condizioni-3.6.1.png`;
- `dettaglio-ntc067-tab-3.5.IV.png`;
- `dettaglio-ntc068-formule-3.6.2-4.png`;
- `dettaglio-ntc069-tab-3.6.I-formule-3.6.5-6.png`;
- `dettaglio-ntc070-tab-3.6.II-formula-3.6.7-tab-3.6.III.png`;
- `dettaglio-ntc070-formule-3.6.8-9.png`;
- `dettaglio-ntc071-condizioni-urti-ferroviari.png`;
- i nove ritagli `dettaglio-*-prosa-rubriche.png` relativi a tutte le pagine dello scope.

La scomposizione proposta b01 NTC 66-68, b02 NTC 69-71 e b03 Circolare 81-83 rispetta i confini di pagina e copre integralmente lo scope senza sovrapposizioni. La sua approvazione operativa e il G6 restano fuori dal ruolo C.

## Addendum C dopo esecuzione E e controllo G5

Data: 2026-09-11  
Firma: Codex / CDX, ruolo C

Questo addendum conserva il rapporto e la lista C originari e ne aggiorna il giudizio dopo l'esecuzione separata delle correzioni. In caso di contrasto sullo stato finale, prevalgono i giudizi di questo addendum.

### G1

**Giudizio G1: OK.** Il ricontrollo è documentato in `../g1/ricontrollo-g1.md` e `../g1/fonti-ricontrollo.json`. Le schede ufficiali Gazzetta Ufficiale acquisite il 2026-09-11 identificano correttamente il D.M. 17 gennaio 2018 e la Circolare 21 gennaio 2019 n. 7; le voci «Avviso di rettifica» ed «Errata corrige» compaiono soltanto come elementi `div class="ghost"`, senza collegamenti attivi. Il D.M. 9 marzo 2023 acquisito interviene sull'articolo 2 del decreto e sui punti 11.4.2 e 11.5.2, senza modificare il § 3.6 o C3.6. L'esito negativo resta circoscritto alla ricognizione riusata del 2026-09-09 e al ricontrollo mirato dichiarato, non è dedotto dal solo hash.

### Esecuzione delle correzioni e chiusura G2-G4

L'esecutore E ha applicato tutti e soli i 38 rilievi congelati in `lista-correzioni.json`. Il rapporto `../e-r01/rapporto-e.json` registra:

- 38 ID su 38 applicati;
- corrispondenza degli hash iniziali con lo snapshot C;
- unicità delle stringhe `prima`, assenza di sovrapposizioni e identità tra diff meccanico e lista;
- SHA-256 del diff completo `8fb0b27092d90f51792393aef864506bed60f5c292ebce9ad749758e8fd2bcc2`.

Il diff è stato controllato da C rispetto alla lista: comprende le 27 correzioni di rubriche e le 11 correzioni di prosa o apparati, senza modifiche normative estranee.

Le cinque anomalie della fonte sono state riversate senza correzioni `AF-COR` in `cap03/annotazioni/3.6-anomalie-fonte.md`. I cinque rinvii numerati e la riga dell'indice delle annotazioni sono stati applicati separatamente da E; `../e-af-r01/rapporto-e-af.json` attesta sei sostituzioni esatte, hash dell'annotazione coincidente e testo normativo depurato byte-identico prima e dopo.

Giudizi finali:

- **G2: OK.** Le 38 difformità sono state corrette e il confronto integrale non lascia residui sostanziali.
- **G3: OK.** Ogni scostamento è stato risolto; le cinque AF sono conservate, annotate e collegate. Nessun `DUBBIO` e nessuna `AF-COR`.
- **G4: OK.** Le 10 formule e le 4 tabelle risultano complete e fonte-fedeli dopo il ripristino del punto nella [3.6.6] e l'espansione della cella unita nella Tab. 3.6.III. Restano 0 figure.

La provenienza delle 26 prove C è in `provenienza-prove.json`: 9 pagine complete a 200 dpi e 17 ritagli a 600 dpi, con PDF, hash, pagina fisica, bbox, metodo e tipo di area. Tutti i ritagli sostanziali sono vettoriali; i soli raster rilevati sono quattro contrassegni GU per pagina nel piè di pagina, fuori dallo scope normativo.

### G5

È stata visionata integralmente la resa delle 11 pagine a 200 dpi in `../g5-r01/b01`, `../g5-r01/b02` e `../g5-r01/b03`. Non sono presenti sovrapposizioni, troncamenti, tag resi con parentesi tonde, didascalie automatiche estranee o difetti di leggibilità. Formule, elenchi e tabelle sono integri; la continuazione della Tab. 3.6.III ripete correttamente la testata e mantiene l'etichetta espansa della cella unita.

La mappa di `../g5-r01/mappa-composito.json` è approvata integralmente:

- composito di 387 righe;
- `b01`, righe 1-149;
- `b02`, righe 150-305;
- `b03`, righe 306-387;
- ordine: tutte le NTC, poi tutta la Circolare;
- esclusione meccanica della riga editoriale identificativa `Circolare 21/01/2019 n. 7 C.S.LL.PP., §C3.6`.

Il riscontro editoriale finale `../g5-r01/riscontro-editoriale-finale.json` attesta che i cinque rinvii numerati sono depurati e che il composito rimane byte-identico, SHA-256 `f14823cc7bee1bb8ceb61330dc4738c11223565ef1922cf4502624bda89fd6b7`. Non è stata necessaria una nuova resa.

**Giudizio G5: OK.** Lo snapshot finale comprende i quattro target normativi e l'annotazione AF, con integrità `OK`; il manifest `../g5-r01/snapshot-target-finale.json` ha SHA-256 `f78911a20fc0bbaa00d043bee52f009fa8e4ace185872c49042202fe11570dbc`. Il controllo globale successivo registra 311 file, 1754 collegamenti validi e lint del registro 0 errori/0 avvisi.

### Stato C conclusivo

**G0-G5: OK.** La verifica C del § 3.6 NTC 2018 e C3.6 Circolare è conclusa sullo snapshot finale sopra identificato. Il G6 non è stato eseguito da C e resta affidato ai verificatori ciechi freschi.

## Addendum C - adjudicazione del recupero di confezionamento G6 r01b

Data: 2026-09-11  
Firma: Codex / CDX, ruolo C

**Giudizio tecnico: recupero legittimo; `ERR-AUDIT` di confezionamento chiuso; indipendenza dei V conservata; `giro_g6 = 1`.**

Il primo `rivela` di b02 aveva costruito `input-confronto.json` mediante la scansione ricorsiva della cartella e aveva incluso anche le prove create da V sotto `prove-v`; `verify_package` ha respinto correttamente questi file estranei all'insieme canonico. L'errore riguardava soltanto il manifest e si è verificato prima di qualunque accesso V a un target valido. Il primo staging e le prove V sono stati conservati integralmente.

Il recupero documentato in `../recupero-confezionamento-g6-r01b.json` ha usato una nuova destinazione e un nuovo `prepara`, senza cambiare target o fonti. Ho verificato direttamente che `input-fonte.json` e `inventario.json` dei tre blocchi sono byte-identici fra staging originario e sostitutivo. Gli hash degli inventari restano:

- b01: `7be59cc6d135a3ed965919698a10e2f71f53573eb0ff6b4d463fc2b5e0cfd981`;
- b02: `645ae464eabf7a308cd9522cf66a8b68459f71993f4760c53314f2fab9499edb`;
- b03: `d5ce469bebbf3b56acd63fd3e7c3b468c56fc094ef604126d8e83441340ccfbf`.

La nuova esecuzione di `verify_package` dà integrità `OK` con 15 file per b01, 15 per b02 e 14 per b03. `../traccia-letture-v.json` registra per tutti i blocchi il primo accesso a `testo.md` dopo il rispettivo congelamento. Poiché gli inventari fonte-prima erano già validi, prodotti senza lettura del target e riferiti a input rimasti identici, la loro copia byte-identica non richiede una nuova inventariazione. È un recupero del solo confezionamento nello stesso giro, conforme ai §§ 7-8 della procedura.

Il rapporto G6 di b02 attesta copertura 44/44, esito `OK` e zero rilievi. La firma interna `Codex GPT-6` è inesatta: i metadati effettivi registrano modello `gpt-5.6-sol`, ragionamento `xhigh`, sessione `01a09163-dfe9-75e3-b9c8-9bbd2936cfac`. Questa è una rettifica documentale append-only di identità; il rapporto e l'inventario congelato originari restano invariati. La rettifica non incide su copertura, esito o indipendenza del blocco b02.

## Addendum C - adjudicazione dei rilievi G6 r01

Data: 2026-09-11  
Firma: Codex / CDX, ruolo C

Sono stati letti integralmente i tre rapporti `rapporto-g6.json` del confezionamento r01b e sono state osservate le prove V originali. Gli esiti sono b01 `KO` con tre rilievi, b02 `OK` su 44/44 elementi e b03 `KO` con due rilievi. **Giudizio C: tutti e cinque i rilievi sono accolti come `ERR-MD`; nessuno richiede una nuova `AF-COR`.** Le sostituzioni esatte e gli hash correnti sono congelati in `lista-correzioni-r02.json`.

1. **B01-66-P01, accolto.** La fonte NTC, pagina fisica 66, stampa `E’ opportuno` come due caratteri vettoriali, `E` U+0045 e apostrofo destro U+2019. Il target reca `È` U+00C8. N2 ammette varianti Unicode dello stesso carattere e apostrofi dritti o curvi, ma non la fusione di una lettera e di un apostrofo in una lettera accentata. Va quindi ripristinato letteralmente `E’ opportuno`.
2. **B01-66-C01 e B01-66-C02, accolti.** La fonte inizia le due alternative direttamente con `nominale:` e `naturale:` in corsivo, senza marcatori. Il target aggiunge due bullet U+2022 mediante i trattini Markdown. Nessuna normalizzazione del catalogo autorizza tali marcatori. Vanno eliminati e le due alternative vanno conservate come capoversi distinti.
3. **B03-C81-006-C3611-DEF01-02, accolto.** Nella prima voce definitoria di C3.6.1.1 la locuzione `capacità di compartimentazione` è in PalatinoLinotype-Roman nella fonte; il target la rende in LMRoman10-Italic. Il corsivo aggiunto va rimosso.
4. **B03-C81-008-ENF-LORDA, accolto.** La fonte rende `lorda` in romano con una sottolineatura vettoriale separata, bbox testo `[473.23, 672.94, 491.48, 680.77]` e tratto `[473.31, 679.41, 491.62, 679.82]`; il target usa LMRoman10-Bold senza sottolineatura. La sostituzione del sottolineato con il grassetto non è dichiarata nel catalogo.

Per la quarta correzione ho provato quattro codifiche con `strumenti/render-capitolo.py`, senza modificare il renderer. La prova è in `renderer-underline-test.md`, `renderer-underline-test.pdf`, `renderer-underline-test-288dpi.png` e `renderer-underline-test.json`. `_lorda_` produce LMRoman10-Italic; `<u>lorda</u>` produce romano senza linea; `[lorda]{.underline}` produce LMRoman10-Regular e una linea vettoriale separata; anche il comando TeX produce una linea. È pertanto prescritta la codifica Pandoc `[lorda]{.underline}`, che conserva testo romano e sottolineatura nel renderer canonico.

Questi cinque elementi non erano oggetto di una precedente adjudicazione specifica: sono rilievi tipografici sfuggiti al primo G2-G3, non ribaltamenti delle decisioni espresse sulle tabelle o sulle cinque anomalie di fonte. Anche applicando in via prudenziale la regola di ribaltamento a `E’`, il requisito del § 4 è soddisfatto: il V fresco e separato ha prodotto ritagli a 600 e 1200 dpi, codifica e posizioni vettoriali, concordanti con la fonte. Per i due rilievi della Circolare l'inventario fonte-prima registrava già il romano e la sottolineatura prima della rivelazione del target; le prove a 600 dpi e il riscontro vettoriale concordano. Non serve un ulteriore lettore cieco.

Le firme interne `GPT-6` di b01 e b02 sono inesatte e vanno rettificate soltanto in una registrazione documentale append-only basata sui metadati nativi delle sessioni; inventari e rapporti originari restano intatti. Per b02 i metadati sono quelli già registrati nell'addendum precedente. Questa inesattezza non incide sui contenuti del confronto o sull'indipendenza dei V.

Non emergono altri rilievi dai tre rapporti. Il giro G6 r01 si chiude `KO` per b01 e b03 e non può sostenere la chiusura del § 3.6. Dopo l'esecuzione separata delle cinque correzioni occorrono il controllo C del diff, un nuovo G5 e un nuovo G6 integrale con V freschi. La proposta di ridistribuzione in due blocchi, b01 NTC 66-69 fino al termine di 3.6.2.4 e b02 NTC 70-71 più Circolare 81-83, non spezza paragrafi o apparati; l'approvazione definitiva della mappa resta subordinata al composito e al render G5 r02. Lo stato riguarda soltanto le quattro righe del registro `3.6`, `3.6.1`, `3.6.2` e `3.6.3`; non promuove le introduzioni 3.1-3.4 né l'intero capitolo 3.

## Addendum C - chiusura G0-G5 r02

Data: 2026-09-11  
Firma: Codex / CDX, ruolo C

L'esecutore E ha applicato tutti e soli i cinque rilievi di `lista-correzioni-r02.json`. Ho confrontato il diff completo con la lista e con le copie pre-E: ogni stringa `prima` compariva una sola volta, la trasformazione simulata coincide byte per byte con i target correnti e non risultano modifiche estranee. Il diff `../e-r02/diff-unico-completo.diff` ha SHA-256 `9b1e8b30a825de9b1830e810c8fb7b732b1ceca78d18c773bd66a9fc72757e06`; gli hash dopo E coincidono con quelli attesi per tutti e quattro i target.

Giudizi r02:

- **G0: OK.** Perimetro e confini delle fonti restano invariati: NTC pagine fisiche 66-71 e Circolare pagine fisiche 81-83.
- **G1: OK, riusato.** Fonti e ricognizione non sono cambiate; non è stata ripetuta la verifica già documentata.
- **G2: OK.** I cinque residui emersi al G6 r01 sono stati corretti letteralmente. La resa mostra `E’ opportuno`, due capoversi distinti `nominale:` e `naturale:` senza bullet, e `capacità di compartimentazione` in romano nella voce C3.6.1.1.
- **G3: OK.** Tutti i cinque rilievi r02 sono chiusi come `ERR-MD`; restano le sole cinque anomalie di fonte già annotate. Nessuna nuova `AF-COR` e nessun dubbio aperto.
- **G4: OK.** Le correzioni r02 non modificano formule o tabelle. Restano verificate integralmente 10 formule, 4 tabelle e 0 figure.
- **G5: OK.** Sono state osservate integralmente le dieci PNG a 200 dpi e i due PDF canonici in `../g5-r02/b01` e `../g5-r02/b02`. Non risultano sovrapposizioni, troncamenti, contenuti fuori margine, formule o tabelle spezzate, tag con parentesi tonde, didascalie automatiche o problemi di leggibilità. La parola `lorda` è resa in LMRoman10-Regular con una linea vettoriale separata; il corsivo e il grassetto errati sono assenti.

La mappa `../g5-r02/mappa-composito.json` è approvata integralmente:

- composito di 388 righe, NTC completa seguita dalla Circolare completa;
- b01, righe 1-210: NTC pagine fisiche 66-69, fino al termine di 3.6.2.4;
- b02, righe 211-388: NTC pagine fisiche 70-71 e Circolare pagine fisiche 81-83;
- nessun paragrafo, formula, tabella o altro apparato è diviso fra i blocchi;
- resta esclusa soltanto la riga editoriale identificativa della Circolare già approvata.

Ho verificato che i due Markdown di blocco sono la partizione esatta del composito alle righe 210/211, che la loro concatenazione restituisce byte per byte `target-scope.md` e che il PDF complessivo contiene nell'ordine le stesse dieci pagine dei due PDF di blocco. Il manifest `../g5-r02/snapshot-target-finale.json` comprende i quattro target e l'annotazione, con integrità `OK` e SHA-256 `cd6a442021675c0bbaa29641f10551506f88cbbba0363759a981ef1f67ade672`.

**Stato C r02: G0-G5 OK sullo snapshot `cd6a4420…`.** Il G6 r01 resta storicamente `KO`; per la chiusura del § 3.6 occorre il nuovo G6 integrale sui due blocchi con V freschi. Il controllo degli indici registra 311 file e 1754 collegamenti validi. Il lint del registro sulle 379 righe dà 0 errori e 1 avviso relativo ai 35 residui storici già registrati da GROK: questo addendum non emette alcuna decisione VC su tali residui e non promuove il capitolo 3 nel suo complesso.
