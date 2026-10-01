---
scope_id: ntc2018-3.2.4
data: 2026-08-29
stato: VC-OK
markdown_sha256: 4105f2d3dd29c453c640b782433e03eb9685c808e5fdbd371b87d2b52357f877
fonte_ntc_sha256: dda1e397d56d71aa0f5bc457c3ba9b77064a468699dfc37bd056ac6c47105a46
fonte_circolare_sha256: null
---

# Verbale di verifica di conformità - NTC 2018 § 3.2.4

## Perimetro

Il controllo riguarda esclusivamente `cap03/3.2.4-azione-sismica-effetti-della-variabilita-spaziale-del-moto.md`, corrispondente al § 3.2.4 dell'allegato al D.M. 17 gennaio 2018.

La fonte occupa la pagina fisica NTC 55, dopo la chiusura del § 3.2.3 e prima dell'apertura del § 3.3. La Circolare 21 gennaio 2019 n. 7 passa dal § C3.2.3 al § C3.3 e non contiene un § C3.2.4 corrispondente.

Inventario finale: una pagina fonte, 3 rubriche, 14 capoversi, 4 gruppi di formule numerate, 5 espressioni o rami, 4 tag, nessuna tabella e nessuna figura.

## Fonte e normalizzazioni

- D.M. 17 gennaio 2018: `verifica-conformita/fonte-ufficiale/GU-2018-42-SO8-DM-17-01-2018.pdf`, SHA-256 `dda1e397d56d71aa0f5bc457c3ba9b77064a468699dfc37bd056ac6c47105a46`.
- Elenco unico applicato: `verifica-conformita/normalizzazioni-dichiarate-NTC2018.md`, SHA-256 `d71319206ec54bcac3639dfd0b97c41754fa1062655b2d35c36ee5d6cb3036d6`.

Le sole normalizzazioni rilevate riguardano a capo e parole spezzate, apostrofi e varianti Unicode, spaziatura e delimitatori LaTeX, virgole decimali, resa dei tag nel renderer canonico e scomposizione del gruppo a due rami `[3.2.16]`.

## Gate

- G0 `OK`: identità, file e confini accertati direttamente sulla pagina fonte.
- G1 `OK`: fonte ufficiale identificata e SHA-256 ricalcolato.
- G2 `OK`: inventario source-first e collazione integrale completati su 3 rubriche e 14 capoversi.
- G3 `OK`: cifre, esponenti, pedici, operatori, parentesi, tag e unità verificati sul raster a 600 dpi e sul livello caratteri del PDF.
- G4 `OK`: 4 gruppi formula, 5 espressioni o rami e 4 tag riconciliati; recheck P2 della `[3.2.14]` superato.
- G5 `OK`: render finale di 2 pagine non vuote, 311 file e 1.754 collegamenti interni verificati; linter con zero errori e zero avvisi.
- G6 `OK`: giro R01 integrale sull'unica pagina, con inventario fonte-prima Moon e verificatore P2 Sol indipendente.
- G7 `OK`: precontrollo P0-D Moon e giudizio finale P2 Sol hanno confermato manifest 22/22 e snapshot promuovibile.

## Scarti e correzioni

Sono stati corretti cinque `ERR-MD`:

1. rubrica `3.2.4` riportata nella cassa maiuscola della fonte;
2. rubrica `3.2.4.1` riportata nella cassa maiuscola della fonte;
3. rubrica `3.2.4.2` riportata nella cassa maiuscola della fonte;
4. `fra i punti` sostituito con la forma fonte `tra i punti`;
5. nella formula `[3.2.14]`, esponente interno `2` sostituito con l'esponente fonte `0,7`.

L'esponente è stato deciso sul raster a 600 dpi e sul livello caratteri del PDF, che codifica in apice la sequenza `0`, virgola, `7`. Un P2 source-first ha confermato lo scostamento iniziale e un secondo P2 ha ricontrollato la formula dopo la correzione, con esito `OK`. Non si tratta di una correzione della fonte e non è stata introdotta alcuna nota `AF-COR`.

Il confronto posizionale ha confermato cinque sole righe normative modificate. Le due ulteriori variazioni del file completo riguardano esclusivamente le etichette dell'indice interno riallineate meccanicamente alle rubriche; lo script canonico ha confermato i corpi normativi invariati durante la rigenerazione.

## G6 e G7

Il G6 R01 ha coperto integralmente l'unica pagina: 3/3 rubriche, 14/14 capoversi, 4/4 gruppi formula, 5/5 espressioni o rami e 4/4 tag. Esito: zero `ERR-MD`, zero `ERR-AUDIT`, zero `DUBBIO` e quattro sole famiglie `NORM` dichiarate. Non è stato necessario un secondo giro.

Il G7 P0-D `gpt-5.6-luna/medium` ha ricalcolato 22/22 hash e 22/22 dimensioni del manifest, senza duplicati o voci estranee. Il decisore finale P2 `gpt-5.6-sol/xhigh` ha pronunciato `G7 OK`.

I controlli sono stati eseguiti da agenti AI; non è inclusa una revisione umana integrale.

## Snapshot ed evidenze

Snapshot iniziale Markdown: `3a91e01cf59acb3d757cafd5c23c82d49dc8411f5378078d517fd29b6336e7b4`.

Snapshot finale verificato: `4105f2d3dd29c453c640b782433e03eb9685c808e5fdbd371b87d2b52357f877`.

Frammento normativo finale depurato: `2f616de6d85ace62f17b805274e670ea01030b86346515b26d45741e136a609f`.

Render finale: `3fbd333d9a67f319f249a81e1ca4ccb4d84444b451d95100381084a4de81f9ae`.

Evidenze principali:

- `_tmp_render/cap03/vc-3.2.4-20260829/preflight/fonte/ntc-p55-scope-3.2.4-600dpi.png`;
- `_tmp_render/cap03/vc-3.2.4-20260829/preflight/rapporto-consolidato-g0-g5.md`;
- `_tmp_render/cap03/vc-3.2.4-20260829/preflight/correzioni-p1-p2.md`;
- `_tmp_render/cap03/vc-3.2.4-20260829/apparati/`;
- `_tmp_render/cap03/vc-3.2.4-20260829/g6-r01/`;
- `_tmp_render/cap03/vc-3.2.4-20260829/g7/`;
- `verifica-conformita/manifest-sha256-ntc2018-3.2.4-2026-08-29.txt`.

## Rilascio

SHA-256 del manifest finale: `29a1d622cc776c03512fcb7be4d65156cb31fb3c919fb4b84214045797a4c66e`, 22 voci.

Residui finali: 0 `ERR-MD`, 0 `ERR-AUDIT`, 0 `DUBBIO`, 0 `AF` e 0 `AF-COR`. Tutti i gate G0-G7 sono `OK`. Lo scope è promosso localmente a `VC-OK al 2026-08-29`; il giudizio vale soltanto per lo snapshot e il perimetro dichiarati.

Firma della redazione: CDX (Codex).
