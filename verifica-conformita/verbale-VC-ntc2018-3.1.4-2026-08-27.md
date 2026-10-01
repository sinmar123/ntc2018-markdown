---
scope_id: ntc2018-3.1.4
data: 2026-08-27
stato: VC-OK
markdown_sha256: 776028cc5077b37cd3599398642a20774cc72e72161a64a1a0e643e60c3c6e3f
fonte_ntc_sha256: dda1e397d56d71aa0f5bc457c3ba9b77064a468699dfc37bd056ac6c47105a46
fonte_circolare_sha256: f7c3b8d1f443aadb6b3e020b6b6c19813683492ecaadd2c15bf6bf1939aaed7c
---

# Verbale di verifica di conformità - NTC 2018 § 3.1.4 e Circolare C3.1.4

## Perimetro

Il controllo riguarda esclusivamente `cap03/3.1.4-opere-civili-sovraccarichi.md`, corrispondente ai §§ 3.1.4-3.1.4.3 dell'allegato al D.M. 17 gennaio 2018 e ai §§ C3.1.4-C3.1.4.3 della Circolare 21 gennaio 2019 n. 7.

Le fonti occupano le pagine fisiche NTC 47-49, stampate 43-45, e la pagina fisica Circolare 46, stampata 42. Inventario complessivo: 8 titoli, 23 capoversi, 3 voci di elenco, una tabella su due pagine con 5 colonne, 30 fasce, 115 celle logiche, 14 accorpamenti, 7 gruppi e 21 voci d'uso, una didascalia, 2 note, 2 formule numerate e nessuna figura.

## Fonti e vigenza

- D.M. 17 gennaio 2018: `verifica-conformita/fonte-ufficiale/GU-2018-42-SO8-DM-17-01-2018.pdf`, SHA-256 `dda1e397d56d71aa0f5bc457c3ba9b77064a468699dfc37bd056ac6c47105a46`.
- Circolare 21 gennaio 2019 n. 7: `verifica-conformita/fonte-ufficiale/GU-2019-35-SO5-Circolare-7-2019.pdf`, SHA-256 `f7c3b8d1f443aadb6b3e020b6b6c19813683492ecaadd2c15bf6bf1939aaed7c`.

Entrambi i PDF locali sono stati confrontati nella medesima giornata con gli attuali download ufficiali della Gazzetta Ufficiale e risultano byte-identici. Il D.M. 9 marzo 2023 non modifica il perimetro 3.1.4/C3.1.4.

## Gate

- G0 `OK`: scope e confini accertati.
- G1 `OK`: fonti ufficiali identificate, hash ricalcolati e vigenza verificata.
- G2 `OK`: inventario source-first riconciliato al 100%.
- G3 `OK`: confronto testuale integrale superato dopo le correzioni dichiarate.
- G4 `OK`: Tab. 3.1.II e formule [3.1.1]-[3.1.2] verificate source-first, riconciliate e ricontrollate nei G6.
- G5 `OK`: render ufficiale e apparati di navigazione verificati; 311 file e 1754 collegamenti interni conformi.
- G6 `OK`: terzo giro cieco integrale; 0 `ERR-MD`, 0 `ERR-AUDIT` aperti, 0 `DUBBIO`.
- G7 `OK`: precontrollo P0-D Luna e controllo finale P2 Sol ripetuti sul fascicolo riallineato; tutte le 15 voci del manifest coincidono per SHA-256 e dimensione.

## Scarti e correzioni

Il P1 ha adjudicato 44 unità `ERR-MD`, 43 sostituzioni puntuali e una riscrittura strutturale della Tab. 3.1.II. Le correzioni puntuali comprendono cassa e punteggiatura delle rubriche, punteggiatura tabellare, cinque lettere `x`, due scarti lessicali, punto della formula [3.1.2] e 16 variabili con pedice portate in modalità matematica. Il riesame inverso ha annullato in memoria le sole correzioni autorizzate e ricostruito esattamente lo snapshot iniziale `1d10ba6ccaf7fc512ca5b2adc6cbd38ed088953262fbc45f64cfc77ccb3bd19d`.

Il G6 R01 ha inizialmente segnalato come accorpata la riga `Ambienti ad uso residenziale`; un ritaglio focalizzato a 600 dpi ha mostrato i tre separatori verticali e il rilievo è stato riclassificato `ERR-AUDIT`, annullando integralmente la correzione provvisoria. Il G6 R02 ha individuato la vera omissione strutturale: le sette celle `Cat.` accorpate verticalmente comprendono anche le righe-titolo. Sono state quindi aggiunte le sole categorie `A`, `B`, `C`, `D`, `E`, `F-G` e `H-I-K` nelle sette righe.

La resa finale della tabella comprende 51 espansioni logiche di celle accorpate, autorizzate dalla voce 6 dell'elenco unico: 21 ripetizioni verticali delle categorie, 18 ripetizioni dei sei titoli accorpati e 12 ripetizioni orizzontali. La riga `Ambienti ad uso residenziale` conserva invece vuote le tre celle numeriche separate della fonte.

Nessuna cifra, coefficiente, esponente, operatore, segno, verso di disuguaglianza o unità è stata modificata. Le ulteriori differenze sono soltanto normalizzazioni dichiarate: marcatori Markdown, a capo e sillabazioni ricomposte, apostrofi curvi resi diritti, spaziatura `n. 23`, resa LaTeX equivalente di pedici, esponenti e tag.

## Anomalie della fonte

Sono conservate alla lettera due anomalie grammaticali nello stesso capoverso NTC:

- `membrature verticali, tra i quali pilastri o setti`;
- `le componenti [...] possono essere ridotti`.

Classificazione: 2 `AF`, nessuna `AF-COR`. Non è stato aggiunto testo assente dalla fonte, salvo le espansioni semantiche dichiarate delle celle accorpate e gli apparati di navigazione esclusi dal confronto.

## G6, G7 e indipendenza

Sono stati necessari tre giri G6 integrali:

- R01 `KO`: un rilievo poi riclassificato `ERR-AUDIT` sul ritaglio focalizzato;
- R02 `KO`: una famiglia di 7 `ERR-MD` nelle categorie delle righe-titolo, corretta separatamente;
- R03 `OK`: 0 `ERR-MD`, 0 `ERR-AUDIT` aperti, un errore d'inventario chiuso nel giro e 0 `DUBBIO`.

Ogni giro è stato coordinato da un contesto fresco P2 `gpt-5.6-sol/xhigh`; inventario fonte-prima e confronto del blocco sono stati eseguiti da due ulteriori contesti freschi P2 `gpt-5.6-sol/xhigh`, con materiali minimi in staging esterno al workspace. Nessuno ha ricevuto rilievi attesi o storia delle correzioni e nessuno ha modificato il Markdown.

Un primo G7 ha confermato i 15 file, lo snapshot, il frammento depurato e la catena tecnica, ma ha pronunciato `KO` formale perché la scheda conteggiava impropriamente le due `AF` come rilievi persistenti e il rapporto R03 non distingueva l'errore d'inventario chiuso dagli `ERR-AUDIT` aperti. Il fascicolo è stato riallineato senza modificare il Markdown: 2 `AF`, 0 `AF-COR`, 0 `ERR-MD`, 0 `ERR-AUDIT` aperti, 0 `DUBBIO`, 0 rilievi aperti e 0 persistenti. Il manifest è stato rigenerato e il G7 è stato ripetuto integralmente con esito `OK`.

I controlli sono stati eseguiti da agenti AI; non è inclusa una revisione umana integrale.

## Snapshot ed evidenze

Snapshot iniziale Markdown: `1d10ba6ccaf7fc512ca5b2adc6cbd38ed088953262fbc45f64cfc77ccb3bd19d`.

Snapshot finale verificato: `776028cc5077b37cd3599398642a20774cc72e72161a64a1a0e643e60c3c6e3f`.

Frammento normativo depurato dagli apparati: `924d3b6b55ee31dddd37bf5aa73d9e49ffcdc7c29ce9ebd8db777d7858d6b871`.

Evidenze principali:

- `_tmp_render/cap03/vc-3.1.4-20260827/preflight/rapporto-p0d-luna.md`;
- `_tmp_render/cap03/vc-3.1.4-20260827/preflight/rapporto-preflight.md`;
- i quattro ritagli di scope a 600 dpi e il ritaglio focalizzato in `_tmp_render/cap03/vc-3.1.4-20260827/fonte/`;
- `_tmp_render/cap03/vc-3.1.4-20260827/preflight/md-confronto-corretto-render.pdf`;
- `_tmp_render/cap03/vc-3.1.4-20260827/apparati/tabella/riconciliazione/registro-finale.md`;
- i tre rapporti `_tmp_render/cap03/vc-3.1.4-20260827/g6-r01/`, `g6-r02/` e `g6-r03/`;
- `verifica-conformita/manifest-sha256-ntc2018-3.1.4-2026-08-27.txt`.

Il render ufficiale è stato rigenerato dopo l'ultima correzione; i controlli bloccanti confermano tag fra quadre e assenza di didascalie automatiche. La tabella è interrogabile e rende esplicita la struttura delle celle accorpate.

## Rilascio

Il precontrollo P0-D `gpt-5.6-luna/medium` e il controllo finale P2 `gpt-5.6-sol/xhigh` hanno ricalcolato e confermato 15/15 voci del manifest; SHA-256 del manifest `990eaef70d2946e806bc704e03ae1c5e1dfa06e3cff1156a0de4149113bc52d7`. Tutti i gate G0-G7 sono `OK` e non restano rilievi aperti o persistenti. Lo scope è promosso localmente a `VC-OK al 2026-08-27`; il giudizio vale soltanto per lo snapshot e il perimetro dichiarati.

Firma della redazione: CDX (Codex).
