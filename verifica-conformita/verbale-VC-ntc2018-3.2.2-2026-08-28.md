---
scope_id: ntc2018-3.2.2
data: 2026-08-28
stato: VC-OK
markdown_sha256: b0e539d976c230e709bc6af524360fc211ba1dcf41c43229cf476c4951c89556
fonte_ntc_sha256: dda1e397d56d71aa0f5bc457c3ba9b77064a468699dfc37bd056ac6c47105a46
fonte_circolare_sha256: f7c3b8d1f443aadb6b3e020b6b6c19813683492ecaadd2c15bf6bf1939aaed7c
---

# Verbale di verifica di conformità - NTC 2018 § 3.2.2 e Circolare C3.2.2

## Perimetro

Il controllo riguarda esclusivamente `cap03/3.2.2-azione-sismica-categorie-di-sottosuolo-e-condizioni-topografiche.md`, corrispondente al § 3.2.2 dell'allegato al D.M. 17 gennaio 2018 e al § C3.2.2 della Circolare 21 gennaio 2019 n. 7.

Le fonti occupano le pagine fisiche NTC 50-51 e Circolare 50-51. Inventario finale: 4 rubriche, 21 capoversi, 6 voci di elenco, 2 tabelle con 22 celle logiche e 9 righe dati, 2 formule numerate, 25 relazioni inline o non numerate, nessuna nota e nessuna figura.

## Fonti e vigenza

- D.M. 17 gennaio 2018: `verifica-conformita/fonte-ufficiale/GU-2018-42-SO8-DM-17-01-2018.pdf`, SHA-256 `dda1e397d56d71aa0f5bc457c3ba9b77064a468699dfc37bd056ac6c47105a46`.
- Circolare 21 gennaio 2019 n. 7: `verifica-conformita/fonte-ufficiale/GU-2019-35-SO5-Circolare-7-2019.pdf`, SHA-256 `f7c3b8d1f443aadb6b3e020b6b6c19813683492ecaadd2c15bf6bf1939aaed7c`.

La ricognizione sulle fonti ufficiali al 2026-08-28 non ha individuato modifiche o sostituzioni del § 3.2.2 o del § C3.2.2. Il D.M. 9 marzo 2023 non incide sul perimetro.

## Gate

- G0 `OK`: identità, file e confini accertati direttamente sulle quattro pagine.
- G1 `OK`: fonti ufficiali identificate, hash ricalcolati e vigenza verificata.
- G2 `OK`: inventario dalla fonte e confronto testuale integrale completati.
- G3 `OK`: glifi protetti, cifre, apici, pedici, operatori, disuguaglianze, unità e tag verificati sui ritagli a 600 dpi.
- G4 `OK`: 2 formule numerate, 4 sommatorie, 2 tabelle, 22 celle logiche, 9 righe dati e 2 didascalie ricostruite e riconciliate.
- G5 `OK`: render finale di 4 pagine e apparati di navigazione verificati; 311 file e 1.754 collegamenti interni conformi.
- G6 `OK` per deroga esplicita: tre giri integrali, correzione finale certa e controllo mirato fonte-PDF-Markdown autorizzato da Sandro in luogo del quarto giro.
- G7 `OK`: precontrollo P0-D Moon e controllo finale P2 Sol hanno confermato 18/18 hash e 18/18 dimensioni del manifest.

## Scarti e correzioni

Nel preflight sono state corrette 23 occorrenze `ERR-MD`: cassa e punteggiatura delle rubriche, differenze lessicali e congiunzioni, testo aggiunto assente dalla fonte, intervallo della categoria D, forma della formula `[C.3.2.4]`, quattro variabili di tabella, separatori aggiunti nel blocco delle definizioni e cinque segmenti corsivi. Nessuna cifra, coefficiente, esponente, apice, pedice, operatore, segno, verso di disuguaglianza o unità è stata modificata fuori dalla corrispondenza attestata dalla fonte.

Il G6 R01 ha rilevato e fatto correggere `e in ipotesi residuali` in `ed in ipotesi residuali`. Il G6 R02 ha contestato la cassa del pedice nel membro sinistro `$V_{S,eq}$`; il livello caratteri del PDF ha confermato `S` maiuscola `U+0053`, coincidente con il Markdown, e il rilievo è stato riclassificato `ERR-AUDIT` senza modifiche. Il G6 R03 ha rilevato e fatto ripristinare la virgola dopo `$V_{s,eq}$`.

Raggiunto il massimo di tre giri G6, Sandro ha autorizzato la scelta di buon senso di non svolgere un quarto controllo integrale. È stato eseguito il confronto mirato del punto corretto sul raster a 600 dpi, sul testo del PDF e sul Markdown finale, con esito `OK` e zero residui.

## Anomalie della fonte

Sono conservate alla lettera cinque anomalie:

- estremo inferiore `j=2` nella prima sommatoria della formula `[C.3.2.4]`;
- intestazione `Caratteristiche della superficie topografica` nella Tab. 3.2.II dedicata alle categorie di sottosuolo;
- rinvio della Circolare alla Tabella 3.2.IV, mentre le categorie topografiche sono nella Tab. 3.2.III delle NTC;
- alternanza fra `$V_{S,eq}$` e `$V_{s,j}$` nella formula `[C.3.2.4]`;
- prosa `maggiore di 30 m` seguita dalla condizione inclusiva `(H ≥ 30 m)`.

Classificazione: 5 `AF`, 0 `AF-COR`. Cifre, casse e simboli protetti sono stati conservati senza correzioni per inferenza.

## G6, G7 e indipendenza

Sono stati svolti tre giri G6 integrali a verificatore singolo, secondo la deroga procedurale autorizzata da Sandro:

- R01 `KO`: 1 `ERR-MD`, poi corretto separatamente;
- R02 storico `KO`: 1 rilievo successivamente riclassificato `ERR-AUDIT`;
- R03 `KO`: 1 `ERR-MD`, poi corretto separatamente.

La successiva verifica focalizzata non viene presentata come quarto G6 integrale. G6 è chiuso `OK` per deroga dichiarata sullo snapshot finale, con zero rilievi aperti. Il G7 ha usato il profilo semplificato P0-D `gpt-5.6-luna/medium` per il precontrollo deterministico e un contesto P2 `gpt-5.6-sol/xhigh` per il giudizio conclusivo.

I controlli sono stati eseguiti da agenti AI; non è inclusa una revisione umana integrale.

## Snapshot ed evidenze

Snapshot iniziale Markdown: `fd41ee228aa961a024f634e2e1c858f3baa3d6dfdb1fca5d9575feb423c49517`.

Snapshot finale verificato: `b0e539d976c230e709bc6af524360fc211ba1dcf41c43229cf476c4951c89556`.

Frammento normativo finale depurato dagli apparati: `e35b9128d6b100f5f5b34d9f5e26d8637d843d52739b38d9ff85e2a3506dcfaa`.

Render finale: `4b621cd670e3bf5de35908b6933e4a1411ff830bfde155c66ba158a0cec50ab8`.

Evidenze principali:

- `_tmp_render/cap03/vc-3.2.2-20260828/preflight/rapporto-consolidato-g0-g5.md`;
- i quattro ritagli di scope a 600 dpi in `_tmp_render/cap03/vc-3.2.2-20260828/g6-r03/preparazione/fonte/`;
- `_tmp_render/cap03/vc-3.2.2-20260828/preflight/render-scope-finale.pdf`;
- `_tmp_render/cap03/vc-3.2.2-20260828/apparati/riconciliazione/registro-finale.md`;
- i rapporti consolidati in `_tmp_render/cap03/vc-3.2.2-20260828/g6-r01/`, `g6-r02/` e `g6-r03/`;
- `_tmp_render/cap03/vc-3.2.2-20260828/g6-r02/adjudicazione-post-g6.md`;
- `_tmp_render/cap03/vc-3.2.2-20260828/g6-r03/correzione-e-chiusura-deroga.md`;
- `_tmp_render/cap03/vc-3.2.2-20260828/preflight/rapporto-controllo-mirato-finale.md`;
- i rapporti G7 in `_tmp_render/cap03/vc-3.2.2-20260828/g7/`;
- `cap03/annotazioni/3.2.2-anomalie-fonte.md`;
- `verifica-conformita/manifest-sha256-ntc2018-3.2.2-2026-08-28.txt`.

## Rilascio

Il precontrollo P0-D `gpt-5.6-luna/medium` e il controllo finale P2 `gpt-5.6-sol/xhigh` hanno ricalcolato e confermato le 18/18 voci del manifest. SHA-256 del manifest: `27c39a259d0875134e75df5d062640792b2f26138a15ca50c86821649172f64c`.

Tutti i gate G0-G7 sono `OK` secondo il percorso e la deroga dichiarati. Non restano rilievi aperti o persistenti. Lo scope è promosso localmente a `VC-OK al 2026-08-28`; il giudizio vale soltanto per lo snapshot e il perimetro dichiarati.

Firma della redazione: CDX (Codex).
