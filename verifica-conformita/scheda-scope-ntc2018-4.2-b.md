---
scope_id: ntc2018-4.2-b
atti:
  - "D.M. 17/01/2018, §§ 4.2.4.1.3-4.2.4.1.7"
  - "Circolare 21/01/2019 n. 7 C.S.LL.PP., §§ C4.2.4-C4.2.4.1.3.4.9"
file_markdown: _tmp_render/cap04/ristrutturazione-4.2-20260825/archivio-file-sostituiti/4.2-acciaio-stabilita-verifiche.md
struttura_corrente: cap04/indice-4.2.md
validita_corrente: SCADUTA
fonte_ntc: {pdf: verifica-conformita/fonte-ufficiale/GU-2018-42-SO8-DM-17-01-2018.pdf, pagine_fisiche: 105-110}
fonte_circolare: {pdf: verifica-conformita/fonte-ufficiale/GU-2019-35-SO5-Circolare-7-2019.pdf, pagine_fisiche: 106-123}
unita_registro: 33
formule_numerate_preliminari: 93
stato: SOSPESO
agente: CDX
macchina: P53
presa_in_carico: 2026-08-25T15:08:28+02:00
giro_g6: 7
max_giri: 7
rilievi_aperti: 4
rilievi_persistenti: 0
gate: {G0: OK, G1: OK, G2: OK, G3: OK, G4: OK, G5: OK, G6: KO, G7: DA_FARE}
snapshot_sha256: 1b548e70e811ed9a508713db79688e67d468c86bf13765d7652413aa493b2b70
attesa_decisione: [apertura-nuovi-scope-su-file-naturali]
autorizzazioni:
  - "2026-08-25 - Sandro autorizza con 'ok.. vai' la ripresa del § 4.2-B in profilo economico, la correzione distinta dei 2 ERR-MD congelati dal sesto G6 e un settimo G6 integrale cieco; max_giri alzato da 6 a 7."
  - "2026-08-22 - Sandro autorizza max_giri: 6, la correzione distinta degli 11 ERR-MD, la risoluzione e verifica dell'ERR-AUDIT sul render/preflight e un sesto G6 integrale cieco (GBOT / cloud)."
  - "2026-08-06 - Sandro autorizza l'aumento di max_giri da 3 a 4, la correzione distinta dei nove ERR-MD congelati e il quarto G6 integrale cieco."
  - "2026-08-06 - Sandro autorizza l'aumento di max_giri da 4 a 5, la correzione distinta dei due ERR-MD congelati e il quinto G6 integrale cieco."
---

## 2026-08-25 - ricomposizione editoriale del § 4.2 (CDX)

Il vecchio scope resta `SOSPESO` con G6 r07 `KO`, senza autorizzazione né esecuzione di un ottavo giro. La ricomposizione editoriale del § 4.2 rende inoltre scaduto lo snapshot del file unico di audit: il file è archiviato e la futura verifica dovrà essere aperta sui file naturali indicati da `cap04/indice-4.2.md`.

## 2026-08-25 - CDX

Correzione distinta r07 completata sui 2 `ERR-MD` del sesto G6: la Tabella C4.2.II usa ora `A_v/J_v` e la [C4.2.78.b] conserva la radice quadrata nel numeratore e la radice quarta nella condizione. Revisione indipendente del diff e preflight superati; nuovo snapshot `1b548e70e811ed9a508713db79688e67d468c86bf13765d7652413aa493b2b70`.

Settimo G6 integrale cieco eseguito su 24 pagine, 881 posizioni di riga incluse, 21 asset, 93 formule numerate, 3 gruppi non numerati, 15 tabelle con 324 celle e 12 figure. Esito autoritativo: 3 `ERR-MD`, 1 `ERR-AUDIT`, 0 `DUBBIO`; `G6=KO`. Gli scostamenti del Markdown, tutti sulla pagina fisica 114 della Circolare, sono: denominatore `h_w^2` anziché `h_w` nella formula non numerata di `\sigma_E`; omissione del prodotto in `0{,}5\cdot h_w`; omissione di entrambi i prodotti in `15\cdot\varepsilon\cdot t`. L'errore di audit riguarda l'inventario fonte-prima congelato, che assegna [C4.2.50] e `\sigma_E` alla pagina stampata 109 anziché 110 e trascrive nello stesso punto `h_w^2` anziché `h_w`; dovrà essere sanato con errata-corrige, senza riscrittura silenziosa.

Verbale: `_tmp_render/cap04/vc-paragrafo-4-2b-20260806-r02/g6-r07/coordinamento/01-verbale-coordinamento-g6-r07.md`, SHA-256 `63303fd51205c092937a22ff471c842150f9584c8910dbe8d99db63cd194c889`. Manifest del dossier verificato 99/99, SHA-256 `4175b673680c75a50493292378d31bdf98aa34b94a58c9188cbf5e696a27da51`. Il Markdown non è stato ulteriormente modificato dopo il G6. Con `giro_g6: 7` uguale a `max_giri: 7`, lo scope è `SOSPESO`; G7 non è stato avviato e nessun registro è stato promosso. Serve l'autorizzazione esplicita di Sandro a `max_giri: 8` prima della correzione distinta dei tre rilievi, dell'errata-corrige di audit e dell'ottavo G6 integrale.

## 2026-08-25 - CDX

Scope ripreso su autorizzazione di Sandro con profilo economico. Ricalcolati gli hash: Markdown vivo `5057fa9980961215dc6fdebb5bff57c9d554016396940159383c8874f1df9f6f`, fonte NTC `dda1e397d56d71aa0f5bc457c3ba9b77064a468699dfc37bd056ac6c47105a46`, fonte Circolare `f7c3b8d1f443aadb6b3e020b6b6c19813683492ecaadd2c15bf6bf1939aaed7c`, tutti coincidenti con i valori congelati. Autorizzati la correzione distinta dei 2 `ERR-MD` r06 e il settimo G6 integrale; `giro_g6` resta 6 fino all'esecuzione del controllo. G7 resta vietato.

## 2026-08-24 - GBOT/verifica-ntc

Verbale di coordinamento g6-r06 consolidato (contesto coordinatore fresco): **2 ERR-MD** ([C4.2.78.b] numeratore; Tab. C4.2.II `A_v`/`J_v`), **0 ERR-AUDIT**, **0 DUBBIO**; `e_N`.prodotto chiuso come AF. G6 resta KO; standby su decisione Sandro. SHA verbale `b8811cf6a0bd89bbcb6322d8a206249e0c497cda9e03961d83b42b89fc25de8c`.

## 2026-08-24 - GBOT/verifica-ntc

Sesto G6 integrale cieco su snapshot `5057fa9980961215dc6fdebb5bff57c9d554016396940159383c8874f1df9f6f`: packaging con confini ridisegnati, sei blocchi P2 ciechi, coordinamento su dossier chiuso. Esito consolidato: **2 ERR-MD**, **0 ERR-AUDIT**, **0 DUBBIO**; **G6=KO**. L’ERR-MD decisivo su [C4.2.78.b] (numeratore: fonte √γ, MD ∜γ) ribalta r05 con ritaglio 600 dpi; resta aperto anche pedici Tab. C4.2.II (`e_N`.prodotto riclassificato AF nel verbale consolidato). ERR-AUDIT didascalie automatiche chiuso (Figure N:=0). Con `giro_g6: 6` = `max_giri: 6` lo scope è **SOSPESO**; G7 non avviato; vivo invariato. Verbale: `_tmp_render/cap04/vc-paragrafo-4-2b-20260806-r02/g6-r06/coordinamento/01-verbale-coordinamento-g6-r06.md`.

## 2026-08-24 - GBOT/verifica-ntc

Fase correttiva R06 completata: applicati 11/11 ERR-MD del verbale g6-r05 e risolto ERR-AUDIT (render senza `implicit_figures` + controllo didascalie automatiche; PDF preflight `Figure N:` = 0). Revisione indipendente del diff **PASS**. Nuovo snapshot `5057fa9980961215dc6fdebb5bff57c9d554016396940159383c8874f1df9f6f`. AF intatti. Scope `IN-CORSO`; `giro_g6` resta 5 fino al sesto G6; G7 vietato. Evidenze: `_tmp_render/cap04/vc-paragrafo-4-2b-20260806-r02/g6-r06/correzione-r06/`.

## 2026-08-24 - GBOT/verifica-ntc

Ripristinati i 12 PNG mancanti in `cap04/img` ritagliandoli dai PDF ufficiali sul computer cloud (`GU-2018-42-SO8-DM-17-01-2018.pdf`, `GU-2019-35-SO5-Circolare-7-2019.pdf`), densità allineata ai sibling (~zoom 8,333 sulla bbox del corpo grafico, didascalia esclusa). Conteggio asset: **21/21**. Markdown vivo non modificato (snapshot scheda resta `d339546a…`). SHA-256 dei 12 nuovi in CHANGELOG e in `_tmp/ntc-asset-restore/extract-meta.json`. Non avviati correzione ERR-MD né sesto G6: in attesa del via di capogrokbot. Sync workspace W520: CopyFromBox dei 12 PNG + scheda + CHANGELOG completato.

## 2026-08-24 - GBOT

Copia cloud: PDF ufficiali + report g6-r05 + 9/21 PNG in `cap04/img`. Mancano 12 asset anche sul W520 (recuperati solo 9 dai pacchetti g6). Scope resta in attesa del ripristino degli asset prima del sesto G6; la correzione distinta degli ERR-MD può partire sul markdown. Elenco mancanti in `normativa/COPIA-CLOUD.md`.

## 2026-08-22 - GBOT

Sandro ha autorizzato `max_giri: 6`, la correzione distinta degli 11 `ERR-MD` congelati dal quinto G6, la risoluzione e verifica dell'`ERR-AUDIT` sul render/preflight e un sesto G6 integrale cieco. Scope da riaprire `IN-CORSO` dopo copia PDF/asset sul computer cloud; `giro_g6` resta 5 fino al nuovo controllo; G7 vietato finché G6 non è `OK`. Correzione e sesto G6 in contesti distinti.

## 2026-08-06 - CDX

Quinto G6 integrale eseguito sullo snapshot `d339546a906bd29a3687154828974e7b72a4b215cd2b323bd7796622491e14c5`: inventario fonte-prima, sei blocchi P2 ciechi con confini ridisegnati e coordinatore P2 separato su dossier chiuso. Integrità verificata 94/94 nel packaging e 114/114 nel fascicolo di coordinamento; copertura completa di 24 pagine, 93 gruppi di formule numerate, 3 gruppi non numerati, 15 tabelle, 12 figure e 21 asset. Esito autoritativo: 11 `ERR-MD`, 1 `ERR-AUDIT`, 0 `DUBBIO`; `G6=KO`. Gli errori del Markdown riguardano un punto aggiunto dopo la definizione di `\Phi_{LT}`, l'intestazione accorpata della Tab. 4.2.XI ripetuta in entrambe le colonne, `LIMITI` reso al singolare, l'ordine immagine-didascalia di sette tabelle e la radice quadrata al posto della radice quarta nella [C4.2.78.b]. La lacuna di audit riguarda il render, che aggiunge 21 didascalie automatiche, duplica quelle esplicite e denomina come figure anche le tabelle raster. Confermati senza regressione come `AF` `b_{sl,l}` nella prosa, `aso I` nella Figura C4.2.17 e il doppio `++` della Tabella C4.2.X, tutti presenti nella fonte. Il vivo è rimasto invariato; con `giro_g6: 5` e `max_giri: 5` lo scope è `SOSPESO`, G7 non è stato avviato e nessun registro è stato promosso. Verbale autoritativo: `_tmp_render/cap04/vc-paragrafo-4-2b-20260806-r02/g6-r05/coordinamento/01-verbale-coordinamento-g6-r05.md`, SHA-256 `b5ae882c30d92ed3f123af52226d4caa6b7cd41ae7df33dab43f20e3cd851dd1`.

## 2026-08-06 - CDX

Fase correttiva R05 completata da un correttore P2 separato: applicati esattamente 2/2 rilievi congelati, senza modifiche estranee; revisione indipendente del diff `PASS`. Nuovo snapshot `d339546a906bd29a3687154828974e7b72a4b215cd2b323bd7796622491e14c5`; 93 tag distinti, 21/21 asset, BOM conservato, lint senza errori e render di 28 pagine senza pagine vuote. I sei pacchetti ciechi r05 hanno confini ridisegnati rispetto a r04, estratti coincidenti riga per riga e manifest del perimetro 94/94. `G6` resta `KO` fino all'esito del quinto controllo integrale. Evidenze: `_tmp_render/cap04/vc-paragrafo-4-2b-20260806-r02/g6-r05/correzione-r05/`, `preflight/` e `00-partizione-e-pacchetti.md`.

## 2026-08-06 - CDX

Sandro ha autorizzato l'aumento di `max_giri` da 4 a 5, la correzione distinta dei due `ERR-MD` congelati dal quarto G6 e un quinto G6 integrale cieco. Scope riaperto `IN-CORSO`; `giro_g6` resta 4 fino al nuovo controllo e G7 resta vietato finché G6 non risulta `OK`.

## 2026-08-06 - CDX

Quarto G6 integrale eseguito sullo snapshot `99af69e87987c10f50ab7eb10bb29428b61f84f35107ff011485697a8e1f80a2`: inventario fonte-prima in contesto fresco, sei blocchi P2 ciechi con confini ridisegnati e coordinatore P2 separato su fascicolo manifestato 116/116. Il primo rapporto C-D, materialmente completo ma contaminato dalla lettura di istruzioni esterne, è stato invalidato e ripetuto da un nuovo verificatore; il rapporto valido dichiara copertura integrale e nessun file esterno consultato. Il supplemento sulla riga 0778 ha sanato la sola lacuna probatoria con la pagina fisica 120 a 600 dpi, manifest 6/6 e adjudicatore P2 fresco. Esito consolidato: 2 `ERR-MD`, 0 `ERR-AUDIT`, 0 `DUBBIO`; riga 0545, `\simeq` al posto di `=` nella formula non numerata di `\sigma_E`; riga 0778, virgola omessa dopo `\sigma_{cr,p}`. Le proposte sulle parentesi alle righe 0536 e 0854 sono chiuse `NORM`, quest'ultima senza ribaltare l'adjudicazione precedente. `G6=KO`; con `giro_g6: 4` e `max_giri: 4` lo scope è `SOSPESO`. Il vivo è rimasto invariato, G7 non è stato avviato e nessun registro è stato promosso. Esito autoritativo: `_tmp_render/cap04/vc-paragrafo-4-2b-20260806-r02/g6-r04/coordinamento/02-esito-consolidato-g6-r04.md`.

## 2026-08-06 - CDX

Fase correttiva straordinaria R04 completata da un correttore P2 separato: applicati esattamente 9/9 rilievi congelati, senza modifiche estranee. La revisione indipendente del diff ha confermato 9 hunks limitati ai nove tag autorizzati. Nuovo snapshot `99af69e87987c10f50ab7eb10bb29428b61f84f35107ff011485697a8e1f80a2`; 93 tag distinti, 21/21 asset risolti, BOM conservato, lint senza errori e render di 28 pagine senza pagine vuote. I pacchetti ciechi del quarto G6 hanno confini ridisegnati e manifest validato 101/101. `G6` resta `KO` fino all'esito del quarto controllo integrale. Evidenze: `_tmp_render/cap04/vc-paragrafo-4-2b-20260806-r02/g6-r04/correzione-r04/`, `preflight/` e `00-partizione-e-pacchetti.md`.

## 2026-08-06 - CDX

Sandro ha autorizzato l'aumento di `max_giri` da 3 a 4 e, come richiesto nella sospensione, la correzione distinta dei nove `ERR-MD` congelati dal terzo G6 seguita da un quarto G6 integrale cieco. Scope riaperto `IN-CORSO`; `giro_g6` resta 3 fino al nuovo controllo e G7 resta vietato finché G6 non risulta `OK`.

## 2026-08-06 - CDX

Terzo G6 integrale, ultimo giro ordinario ammesso, eseguito sullo snapshot `917134d6f52f66c2f8d62f6acfcbdd78a57f429f390a9f94f2046a598ff8aa8c` con inventario fonte-prima, sei contesti P2 ciechi freschi e coordinamento P2 separato su fascicolo chiuso da manifest. Copertura riconciliata: 24/24 pagine, 93/93 formule numerate, 4 gruppi matematici esposti non numerati, 15/15 tabelle e 12/12 figure; 0 `ERR-AUDIT` e 0 `DUBBIO`. Restano 9 `ERR-MD` certi: cinque formule a più righe della Circolare rese con una graffa assente dalla fonte, due difformità di struttura o operatori nelle [C4.2.68] e [C4.2.70], e due nelle [C4.2.81.a] e [C4.2.85]. `G6=KO`; con `giro_g6: 3` e `max_giri: 3` lo scope è `SOSPESO`. Il file vivo non è stato modificato, G7 non è stato avviato e nessun registro è stato promosso. Verbale autoritativo: `_tmp_render/cap04/vc-paragrafo-4-2b-20260806-r02/g6-r03/coordinamento/01-verbale-coordinamento-g6-r03.md`.

## 2026-08-06 - CDX

Correzione R02 applicata dal correttore P2 separato sul verbale congelato del secondo G6: 18/18 `ERR-MD` corretti, 93 tag distinti, 21/21 asset risolti, BOM e lint superati. Nuovo snapshot `917134d6f52f66c2f8d62f6acfcbdd78a57f429f390a9f94f2046a598ff8aa8c`; `G6` resta `KO` fino al terzo controllo integrale, ultimo giro ordinario ammesso. Evidenze: `_tmp_render/cap04/vc-paragrafo-4-2b-20260806-r02/g6-r02/correzione-r02/`.

## 2026-08-06 - CDX

Secondo G6 integrale eseguito sullo snapshot `e41c7aa80dc8c4918aa01563cf85521110d450775424fb76db330fa9f09c056d` con sei contesti P2 ciechi freschi e coordinamento P2 separato sul dossier r2, comprensivo di nuove pagine 118-119 della Circolare a 600 dpi. Esito autoritativo: 18 `ERR-MD`, 0 `ERR-AUDIT`, 0 `DUBBIO`; `G6=KO`, `giro_g6=2`. I rilievi riguardano 14 scostamenti C-A, due intestazioni della Tabella C4.2.VII e due glifi C-C; tre rilievi C-D sono stati chiusi come una normalizzazione e due anomalie della fonte. Verbale: `_tmp_render/cap04/vc-paragrafo-4-2b-20260806-r02/g6-r02/coordinamento/01-verbale-coordinamento-g6-r02.md`.

## 2026-08-06 - CDX

Correzione R01 applicata da un P2 separato sul verbale congelato del primo G6. Una seconda adjudicazione P2 di non regressione ha accertato che `aso I` nella Figura C4.2.17 è già la lezione della fonte: il relativo ID è stato riclassificato `AF` e l'asset originale è stato ripristinato byte per byte. Esito correttivo: 59/59 `ERR-MD` applicati, 1/1 riclassificazione `AF`, 93 tag distinti, 21/21 asset risolti; nuovo snapshot `e41c7aa80dc8c4918aa01563cf85521110d450775424fb76db330fa9f09c056d`. `G6` resta `KO` fino a un nuovo controllo integrale. Evidenze: `_tmp_render/cap04/vc-paragrafo-4-2b-20260806-r02/g6-r01/correzione-r01/` e `_tmp_render/cap04/vc-paragrafo-4-2b-20260806-r02/g6-r01/coordinamento/02-adjudicazione-non-regressione-fig-c4.2.17.md`.

## 2026-08-06 - CDX

Primo G6 integrale eseguito sullo snapshot `025e96367368b4a5eed33a4ff5312b2f57629eba4d66a742136d75d13d105b3f`: inventario fonte-prima P2 e sei blocchi ciechi P2 (`gpt-5.6-sol`, xhigh), seguiti da coordinamento P2 separato sul dossier chiuso con 14 pagine ufficiali e 28 ritagli a 600 dpi. Esito autoritativo: 60 `ERR-MD`, 0 `ERR-AUDIT`, 0 `DUBBIO`; `G6=KO`, `giro_g6=1`. Il verbale congelato prescrive le correzioni puntuali e costituisce l'unico input di giudizio per la fase correttiva: `_tmp_render/cap04/vc-paragrafo-4-2b-20260806-r02/g6-r01/coordinamento/01-verbale-coordinamento-g6.md`.

## 2026-08-06 - CDX

G0-G5 rieseguiti sullo snapshot corrente `025e96367368b4a5eed33a4ff5312b2f57629eba4d66a742136d75d13d105b3f` con separazione fra controllo meccanico P0 (`gpt-5.6-terra`, medium) e giudizio interpretativo P1 (`gpt-5.6-sol`, high). Esito: `OK / OK / OK / OK / OK / OK`, nessun rilievo bloccante; ingresso al nuovo G6 autorizzato. Il vecchio G6 e il rapporto N-B restano invalidi e non contano come giro. Evidenze: `_tmp_render/cap04/vc-paragrafo-4-2b-20260806-r02/g0-g5-meccanico/` e `_tmp_render/cap04/vc-paragrafo-4-2b-20260806-r02/g0-g5-interpretativo/01-giudizio-g0-g5.md`.

## 2026-08-06 - CDX

Scope ripreso legittimamente dopo la presa in carico del 2026-08-04. Le due fonti ufficiali sono integre, ma le evidenze `g0-g5/` e il tentativo preliminare `g6-r01/` appartengono allo snapshot `ab92a1d27a992dea8763cd7ab8bf17190b830396ae4970a8e674174e3e679bfd`, precedente alla trasformazione delle rubriche già presenti in heading Markdown; il file vivo coincide invece con lo snapshot registrato `025e96367368b4a5eed33a4ff5312b2f57629eba4d66a742136d75d13d105b3f`. Il solo rapporto N-B già prodotto è inoltre invalidato da un confine che lasciava fuori cinque righe della Tab. 4.2.IX(b). G0-G5 devono quindi essere rieseguiti sullo snapshot corrente e il primo G6 deve ripartire da pacchetti nuovi; `giro_g6` resta 0. Evidenze storiche conservate senza sovrascrittura in `_tmp_render/cap04/vc-paragrafo-4-2b-20260804-r01/`.

## 2026-08-04 - CDX

G0-G5 superati sullo snapshot corrente: 33/33 unità mappate, 93 formule numerate, 15 tabelle o griglie, 12 figure e 21 asset collegati. Il render ha rilevato l'espulsione della formula [C4.2.28] oltre il margine: inserito un salto pagina tecnico, rigenerato il PDF e verificati 93/93 tag con parentesi quadre. Evidenze: `_tmp_render/cap04/vc-paragrafo-4-2b-20260804-r01/g0-g5/`.

## 2026-08-04 - CDX

Scope preso in carico nell'ambito della conversione coordinata del § 4.2/C4.2. Ricostruzione fonte-prima in corso; apparati sostituiti con ritagli ufficiali a 600 dpi e discrepanze sottoposte ad adjudicazione.

## 2026-08-04 - CDX

Scheda predisposta in coda. Confini e dimensionamento preliminare accertati durante l'apertura del § 4.2/C4.2. Evidenze: `_tmp_render/cap04/4.2-precondizioni-260804/`.
