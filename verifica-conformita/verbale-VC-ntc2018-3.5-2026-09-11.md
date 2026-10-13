# Verbale VC del § 3.5, Azioni della temperatura

**Data di chiusura:** 2026-09-11  
**Firma:** Codex / CDX  
**Giudizio copiato dal G7 critico:** **VC-OK**

Il giudizio vale esclusivamente per lo scope `ntc2018-3.5` e per lo [snapshot finale](vc-ntc2018-3.5-2026-09-11/g5-cdx-r02/snapshot-target-finale.json) SHA-256 `bce58988f35b359df4ea503c1ce0785f4c11c97d395d57dc8d6ff13a913a9344`. Lo scope comprende otto file Markdown e due asset; tutti i gate G0-G7 sono `OK` e non restano `ERR-MD`, `ERR-AUDIT`, dubbi o adjudicazioni aperte.

## Fonte, perimetro e vigenza

Il perimetro comprende il D.M. 17 gennaio 2018, allegato tecnico, § 3.5, pagine fisiche 63-66, dalla rubrica `3.5. AZIONI DELLA TEMPERATURA` alla fine della Tab. 3.5.III, prima del § 3.6; comprende inoltre la Circolare 21 gennaio 2019 n. 7 C.S.LL.PP., § C3.5, pagina fisica 81, dalla relativa rubrica alla fine del capoverso C3.5.2, prima di C3.6. Sono esclusi § 3.4.5/C3.4.5, § 3.6/C3.6 e il duplicato storico non indicizzato `cap03/3.5-temperatura.md`.

Fonti ufficiali: [scheda GU delle NTC, codice 18A00716](https://www.gazzettaufficiale.it/eli/id/2018/02/20/18A00716/sg) e [scheda GU della Circolare, codice 19A00855](https://www.gazzettaufficiale.it/eli/id/2019/02/11/19A00855/sg). Le copie PDF congelate hanno SHA-256 `dda1e397d56d71aa0f5bc457c3ba9b77064a468699dfc37bd056ac6c47105a46` per le NTC e `f7c3b8d1f443aadb6b3e020b6b6c19813683492ecaadd2c15bf6bf1939aaed7c` per la Circolare.

La vigenza è dichiarata alle due date prescritte: ricognizione riusata del **2026-09-09** e [ricontrollo ufficiale mirato](vc-ntc2018-3.5-2026-09-11/g1/ricontrollo-g1.md) del **2026-09-11**. Sono state riaperte le due schede GU e verificato l'[articolo 1 del D.M. 9 marzo 2023](https://www.gazzettaufficiale.it/atto/serie_generale/caricaArticolo?art.versione=1&art.idGruppo=0&art.flagTipoArticolo=0&art.codiceRedazionale=23A01847&art.idArticolo=1&art.idSottoArticolo=1&art.idSottoArticolo1=10&art.dataPubblicazioneGazzetta=2023-03-22&art.progressivo=0), che riguarda l'articolo 2 del decreto del 2018 e le sospensioni dei punti 11.4.2 e 11.5.2, senza modificare § 3.5 o C3.5. Il precedente riferimento descrittivo al punto 7.4.3.1 è stato chiuso come `ERR-AUDIT`, senza effetti sul target. Una modifica successiva delle fonti richiederà una nuova valutazione.

## Metodo e canone

È stata applicata la [procedura R3 congelata](vc-ntc2018-3.5-2026-09-11/metodo/PROCEDURA-VC-r03-congelata.md), SHA-256 `4bd4440a6f9b204338e97ecf78c9bb74ab0d9e04f7478b9c97c436c62e817c7c`, con l'[errata conservata](vc-ntc2018-3.5-2026-09-11/metodo/errata-PROCEDURA-VC-r03.json) per il refuso `VC-NTC/2` nel § 2. Il [canone G6](vc-ntc2018-3.5-2026-09-11/g6-cdx-r02/b01/canone.md) ha SHA-256 `546023234aec119b42de98bb7499187fdb8445f1ac83e5b32743e13174c1eb44`; il [catalogo congelato delle normalizzazioni](vc-ntc2018-3.5-2026-09-11/metodo/normalizzazioni-congelate.md) ha SHA-256 `d71319206ec54bcac3639dfd0b97c41754fa1062655b2d35c36ee5d6cb3036d6`.

## Gate e copertura

| Gate | Esito | Evidenza essenziale |
|---|---|---|
| G0 | OK | Atti, otto Markdown, due asset, pagine e confini riconciliati |
| G1 | OK | Ricognizione del 2026-09-09 e ricontrollo ufficiale del 2026-09-11 |
| G2 | OK | Composito integrale di 136 righe, 79 non vuote, senza lacune o sovrapposizioni |
| G3 | OK | Prosa, rubriche, condizioni e rinvii confrontati integralmente |
| G4 | OK | Otto formule, tre tabelle e due figure verificati contro fonte e prove di dettaglio |
| G5 | OK | Snapshot 10/10, PDF canonico di cinque pagine e cinque raster controllati integralmente |
| G6 | OK | Secondo giro fonte-prima: 36/36 gruppi, copertura 100%, zero rilievi |
| G7 | OK | Manifest 133/133 integro, snapshot e copie G6 coincidenti, zero rilievi aperti |

Il secondo G6 ha censito e coperto una sola volta 36 gruppi: tutte le rubriche e la prosa, le otto formule numerate, le tre tabelle complete e le due figure con didascalie e asset. Lo scope costituiva un solo blocco di cinque pagine; una divisione 3+2 avrebbe violato il minimo di tre pagine per blocco. Il G6 positivo è il giro effettivo **2/3**.

Normalizzazioni applicate: 1, spaziature e a capo; 2, varianti Unicode; 3, spaziatura e delimitatori LaTeX equivalenti; 6, espansione delle celle accorpate; 9, punteggiatura finale delle didascalie; 10, separatore fra numero e testo delle didascalie. Navigazione, indici e richiamo editoriale all'annotazione sono stati esclusi meccanicamente dal pacchetto fonte-prima.

## Correzioni e anomalie

Prima del primo G6, le correzioni G0-G5 già approvate e riscontrate comprendevano quindici interventi: otto rubriche NTC e due rubriche della Circolare riallineate alla fonte, il punto decimale in [3.5.6], la formula inline completa `\Delta T_u = T - T_0`, `tener conto` e il ripristino dei due asset. Diff, baseline e controllo sono conservati nel [dossier E](vc-ntc2018-3.5-2026-09-11/e/) e nel [rapporto C di ripresa](vc-ntc2018-3.5-2026-09-11/rapporto-c-ripresa.md).

Il primo G6 ha aperto sei rilievi, tutti adjudicati e chiusi mediante lista congelata, E distinto e nuovo controllo C:

| Rilievo | Correzione e riscontro |
|---|---|
| Durata transitoria del § 3.5.2 | Conservati `d un anno` e il punto e virgola finale, letti sulla fonte a 600 dpi e sul livello caratteri, con conferma fonte-only indipendente |
| Fig. 3.5.1 | Esteso il crop alla figura completa; verificati i cinque JPEG nativi, la localizzazione a 600 dpi e i due piccoli elementi insulari distinti sotto la Sicilia |
| Tab. 3.5.I, superficie chiara | Ripetuta `Estate` nella cella logica secondo N6 |
| Tab. 3.5.I, superficie scura | Ripetuta `Estate` nella cella logica secondo N6 |
| Tab. 3.5.I, riga invernale | Ripetuto `Inverno` nella seconda cella logica secondo N6 |
| C3.5 | Ripristinato `azioni termiche speciali` e riconfrontato il capoverso |

La fonte contiene una sola anomalia dichiarata nello scope, `AF-3.5.2-01`, per `d un anno` e la punteggiatura finale; è conservata alla lettera e documentata con àncora portabile. Non risultano altre anomalie A e il conteggio `AF-COR` è **0**.

La [rettifica append-only delle evidenze R02](vc-ntc2018-3.5-2026-09-11/g6-cdx-r02/b01/rettifica-g6-001.json) distingue le dimensioni dell'asset target della Fig. 3.5.1 dai cinque JPEG nativi della fonte, conferma la coincidenza byte per byte della Fig. 3.5.2 col PNG nativo e precisa sessione e tempi di accesso. C l'ha accolta nell'[adjudicazione separata](vc-ntc2018-3.5-2026-09-11/adjudicazione-g6-r02-evidenze.md); input, target, copertura e giudizio G6 non sono cambiati.

## Ruoli, indipendenza e resa

La catena è stata eseguita da agenti AI: C critico `gpt-5.6-sol/high`; E vincolato `gpt-5.6-terra/medium`; V fonte-prima e G7 `gpt-5.6-sol/xhigh`, sessione `01a0910c-8056-7bb0-ae6b-aecc452a0c0a`; coordinamento tecnico root `gpt-6-astra/xhigh`; secondo lettore fonte-only `gpt-6-astra/xhigh`, sessione `01a090fe-45f9-7b22-8b5e-a599762466ba`. Sandro ha autorizzato lo scope, ma non ha svolto né attestato una revisione umana integrale dello snapshot.

L'isolamento di V e del secondo lettore è stato istruttivo, con pacchetti distinti e letture controllate dalle tracce, non imposto da una sandbox del filesystem. Il target è stato rivelato a V solo dopo il congelamento dell'inventario; G7 è stato svolto dallo stesso V dopo la conclusione della fase cieca, come ammesso dalla procedura. I tentativi Hermes privi di inventario e testo sono conservati come esiti tecnici e non costituiscono giri G6.

Il render canonico è stato prodotto nel container previsto, con Pandoc 3.11 e TeX Live 2026. Il PDF e le cinque pagine raster sono completi e leggibili. Vale il limite N12 del catalogo: nei viewer che non usano il template di render, i tag di formula possono apparire fra parentesi tonde; nel PDF canonico sono correttamente fra parentesi quadre.

## Evidenze e catena delle impronte

- [Manifest di rilascio](vc-ntc2018-3.5-2026-09-11/manifest-rilascio.json): 133 file, SHA-256 `2cee48a46d7bc510cc21a140b1b4159e5f508a8b950c04e9fb0ec67d6b201f66`.
- [Snapshot finale](vc-ntc2018-3.5-2026-09-11/g5-cdx-r02/snapshot-target-finale.json): SHA-256 `bce58988f35b359df4ea503c1ce0785f4c11c97d395d57dc8d6ff13a913a9344`.
- [Rapporto G6 R01](vc-ntc2018-3.5-2026-09-11/g6-cdx-r01/b01/rapporto-g6.json): SHA-256 `f8c6db33679525b33534a8b167d8667d1fae7c13909ba4dff1e9c1686eb967d0`.
- [Rapporto G6 R02](vc-ntc2018-3.5-2026-09-11/g6-cdx-r02/b01/rapporto-g6.json): SHA-256 `63575bddbd7f861e0abbe935c2940cb36a16b2d0afad3e956a5264180268124d`.
- [Rettifica G6 R02](vc-ntc2018-3.5-2026-09-11/g6-cdx-r02/b01/rettifica-g6-001.json): SHA-256 `987715c7da07c00775378db40d3e4fe1d33d7707c0b04a07f5b9edd26c097399`.
- [Rapporto G7](vc-ntc2018-3.5-2026-09-11/rapporto-g7.json): SHA-256 `cfb158ae4f5c26a35c8ec31df3447c140b80cc5eefb1689b798503bfc2fccd17`.
- [PDF canonico finale](vc-ntc2018-3.5-2026-09-11/g5-cdx-r02/target-scope.pdf): SHA-256 `ed8cd4258d01464bca80d358f3533822177c3225f99c50ef391c99a796983f76`.

Il manifest comprende gli input e le evidenze effettivamente usati fino al G6; il rapporto G7 e questo verbale chiudono esternamente la catena, senza autoreferenze. Misure di esecuzione e consumi rinviano alla scheda finale `scheda-scope-ntc2018-3.5.md`, da completare fino ai controlli di chiusura: i contatori dei contesti parent e figli restano separati e non vengono sommati. Non è dichiarato alcun risparmio non misurato.

Alla firma di questo verbale le registrazioni derivate sono ancora da applicare. Il verbale copia il giudizio G7 già emesso e non attesta che il CSV, la vista XLSX o gli altri file di governo siano già aggiornati. `VC-OK` vale per lo snapshot e la vigenza dichiarati e non sostituisce la fonte ufficiale.

Prossima azione: applicare le registrazioni di chiusura previste dal § 9 della procedura sul giudizio G7 già emesso.
