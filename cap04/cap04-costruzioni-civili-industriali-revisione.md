---
title: Documento di revisione - NTC 2018 cap. 4 Costruzioni civili e industriali
stato: in corso
sorgente_verificata: cap04/
ultimo-aggiornamento: 2026-08-26
---
# Documento di revisione - NTC 2018 cap. 4 Costruzioni civili e industriali

> [!info] Scopo
> Questo file raccoglie i rilievi di revisione dell'intero capitolo `cap04/`, senza modificare direttamente i file sorgente. Serve come registro separato di controlli, anomalie, dubbi e verifiche chiuse o ancora da completare.

## Indice del capitolo

- [Inquadramento SGQ](#inquadramento-sgq)
- [Perimetro del controllo](#perimetro-del-controllo)
- [Esito sintetico complessivo](#esito-sintetico-complessivo)
- [Stato per sezione](#stato-per-sezione)
- [Rilievi di revisione](#rilievi-di-revisione)
  - [R1 - 4.1: formula 4.1.18 sdoppiata](#r1---41-numerazione-formula-4118-in-forma-sdoppiata)
  - [R2 - 4.1: formula 4.1.50 doppia](#r2---41-formula-4150-presente-due-volte)
  - [R3 - 4.1: controllo strutturale](#r3---41-controllo-strutturale-del-markdown)
  - [R4 - 4.2: completamento C4.2](#r4---42-completamento-del-blocco-c42-della-circolare)
  - [R5 - 4.2: numerazione formule C4.2](#r5---42-riallineamento-numerazione-formule-c42)
  - [R6 - 4.2: commenti autonomi assenti](#r6---42-assenza-di-commenti-autonomi-in-alcuni-paragrafi-della-circolare)
  - [R7 - 4.3-4.6: completezza e collegamenti](#r7---43-46-controllo-di-completezza-e-collegamenti)
  - [R8 - 4.2-4.4: controllo numerico tabelle](#r8---42-44-controllo-numerico-tabelle-ntc-e-circolare)
  - [R9 - 4.1: ciclo G6 concluso e VC-OK](#r9---41-ciclo-g6-concluso-e-vc-ok)
  - [R10 - 4.2-A: terzo G6 non superato](#r10---42-a-terzo-g6-non-superato-per-copertura-incompleta)
  - [R11 - 4.2-A: quarto G6 non superato](#r11---42-a-quarto-g6-non-superato-con-undici-err-md)
  - [R12 - 4.2-A: ciclo concluso e VC-OK](#r12---42-a-quinto-g6-e-g7-conclusi-con-vc-ok)
  - [R13 - 4.2-B: terzo G6 non superato](#r13---42-b-terzo-g6-non-superato-con-nove-err-md)
  - [R14 - 4.2-B: quarto G6 non superato](#r14---42-b-quarto-g6-non-superato-con-due-err-md)
  - [R15 - 4.2-B: quinto G6 non superato](#r15---42-b-quinto-g6-non-superato-con-undici-err-md-e-un-err-audit)
  - [R16 - 4.2-B: settimo G6 non superato](#r16---42-b-settimo-g6-non-superato-con-tre-err-md-e-un-err-audit)
  - [R17 - 4.2: ricomposizione e asset](#r17---42-ricomposizione-per-sottoparagrafi-e-ripristino-degli-asset)
  - [R18 - 4.2: nomi file con acciaio](#r18---42-nomi-dei-file-di-livello-3-esplicitati-con-acciaio)
  - [R19 - Perdita asset e scadenza § 4.1](#r19---capitolo-4-perdita-di-asset-e-scadenza-corrente-del-paragrafo-41)
  - [R20 - Ricomposizione per livello 3](#r20---capitolo-4-ricomposizione-uniforme-per-livello-3)
- [Criterio di classificazione](#criterio-di-classificazione)
- [Controlli futuri consigliati](#controlli-futuri-consigliati)
- [Cronologia](#cronologia)
  - [2026-08-26 - Audit asset e scadenza § 4.1](#2026-08-26---audit-degli-asset-e-scadenza-corrente-del-paragrafo-41)
  - [2026-08-26 - Ricomposizione cap. 4](#2026-08-26---ricomposizione-uniforme-del-capitolo-4-per-livello-3)
  - [2026-08-26 - Nomi file § 4.2](#2026-08-26---nomi-dei-file-di-livello-3-del-paragrafo-42-esplicitati)
  - [2026-08-25 - Settimo G6 § 4.2-B non superato](#2026-08-25---settimo-g6-del-paragrafo-42-b-non-superato)
  - [2026-08-06 - Quinto G6 § 4.2-B non superato](#2026-08-06---quinto-g6-del-paragrafo-42-b-non-superato)
  - [2026-08-06 - VC-OK § 4.2-A](#2026-08-06---quinto-g6-e-g7-del-paragrafo-42-a-superati)
  - [2026-08-06 - Quarto G6 § 4.2-B non superato](#2026-08-06---quarto-g6-del-paragrafo-42-b-non-superato)
  - [2026-08-06 - Terzo G6 § 4.2-B non superato](#2026-08-06---terzo-g6-del-paragrafo-42-b-non-superato)
  - [2026-08-05 - Quarto G6 § 4.2-A non superato](#2026-08-05---quarto-g6-del-paragrafo-42-a-non-superato)
  - [2026-08-05 - Terzo G6 § 4.2-A non superato](#2026-08-05---terzo-g6-del-paragrafo-42-a-non-superato)
  - [2026-08-04 - VC-OK § 4.1](#2026-08-04---settimo-g6-e-g7-del-paragrafo-41-superati)
  - [2026-08-03 - Sesto G6 § 4.1 non superato](#2026-08-03---sesto-g6-del-paragrafo-41-non-superato)
  - [2026-08-03 - Quarto G6 § 4.1 non superato](#2026-08-03---quarto-g6-del-paragrafo-41-non-superato)
  - [2026-07-30 - Correzione post-G6 § 4.1](#2026-07-30---correzione-distinta-post-g6-del-paragrafo-41)
  - [2026-07-30 - G6 § 4.1 non superato](#2026-07-30---audit-vc-8-del-paragrafo-41-non-superato-al-g6)
  - [2026-05-21 - Documento unico cap. 4](#2026-05-21---rinominato-come-documento-unico-di-revisione-del-capitolo-4)
  - [2026-05-20 - Controllo finale cap. 4](#2026-05-20---controllo-finale-del-capitolo-4)
  - [2026-04-11 - Apertura revisione 4.1](#2026-04-11---apertura-revisione-mirata-sul-paragrafo-41)

---

## Inquadramento SGQ

Per questa cartella il nome corretto non è "file del capitolo", ma **documento di revisione**.

La distinzione operativa è:
- **file sorgente**: contiene norma e circolare convertite in Markdown;
- **documento di revisione**: registra controlli, rilievi, anomalie e verifiche;
- **non conformità**: solo se c'è una difformità certa rispetto alla fonte o a una regola interna dichiarata.

Questo documento non sostituisce i file normativi del capitolo 4.

## R20 - Capitolo 4: ricomposizione uniforme per livello 3

- I file aggregati dei §§ 4.1, 4.3, 4.4 e 4.5 sono stati archiviati e sostituiti da indici, introduzioni e file naturali `x.y.z`, adottando il criterio già vigente nel § 4.2. Il § 4.6, privo di sottoparagrafi di livello 3, resta in un file unico.
- Confronto pre/post superato senza differenze di testo, formule o riferimenti grafici. Il registro e la navigazione sono stati rimappati sui file correnti.
- Le 136 unità del § 4.1 sono tornate a `DA_FARE/NON_VALUTATO`; l'esito G7 resta conservato soltanto come storico del file aggregato archiviato. Il master autonomo resta `VC-SCADUTA al 2026-08-26`.
- Evidenze e archivio recuperabile: `_tmp_render/ricomposizione-livello3-20260826/`.
- **Firma:** CDX (Codex).

## Perimetro del controllo

File sorgente del capitolo:
- `4.1-calcestruzzo.md`
- `indice-4.2.md` e i 13 file naturali di livello 3 da esso elencati
- `4.3-composte.md`
- `4.4-legno.md`
- `4.5-muratura.md`
- `4.6-altri-sistemi.md`
- `indice-cap04.md`
- immagini e tabelle grafiche in `img/`

Fonti di confronto:
- PDF NTC 2018, pagine 73-152
- Circolare 21/01/2019 n. 7 C.S.LL.PP., capitolo C4
- nuovo PDF `Circolare-7-2019-NTC.pdf`, verificato per la coda C4.2

## Esito sintetico complessivo

- Il capitolo 4 è completo come conversione di norma e circolare.
- I file di sezione sono navigabili e richiamati correttamente dall'indice del capitolo.
- I 63 richiami del § 4.2 risultano coerenti con i file presenti in `img/`; l'audit del 2026-08-26 ha invece accertato 42 richiami PNG non risolti negli altri file del capitolo: 14 nel § 4.1, 24 nel § 4.3 e 4 nel § 4.4.
- La doppia numerazione `4.1.50` è presente anche nel PDF NTC, quindi non è un errore del Markdown.
- La circolare C4.2 è stata completata il 2026-05-20.
- Il PDF della circolare passa direttamente da C4.2.4.1.4.6 a C4.2.9 e C4.2.12, quindi non contiene commenti autonomi per C4.2.5, C4.2.8, C4.2.10 o C4.2.11.
- Il controllo numerico delle tabelle del capitolo 4 è stato eseguito il 2026-05-30 su norma e Circolare C4.
- Nel controllo 2026-05-30 sono state corrette tabelle NTC in `4.2-acciaio.md`, `4.3-composte.md` e `4.4-legno.md`; le tabelle C4 della Circolare controllate non hanno richiesto correzioni.
- Il § 4.1 + § C4.1 conserva il giudizio storico `VC-OK al 2026-08-04` sullo snapshot SHA-256 `93360710906737ff6a9c3d5f91b54e353282e2c1ab08d57deab099f7465d8964`, ma è `VC-SCADUTA al 2026-08-26`: il Markdown normativo è invariato, mentre 13/17 asset del manifest sono mancanti e l'indice condiviso è cambiato.
- Il sottoscope storico 4.2-A era `VC-OK al 2026-08-06` sullo snapshot `eccefb75094e290c75a9496d4d902bcff9bfecd7542affa566c23c69296e8994`; dal 2026-08-25 è `VC-SCADUTA` per la ricomposizione editoriale del § 4.2 e il nuovo insieme di asset.
- Il sottoscope 4.2-B è `SOSPESO` dopo il settimo G6 sullo snapshot `1b548e70e811ed9a508713db79688e67d468c86bf13765d7652413aa493b2b70`: copertura completa di 24 pagine, 881 posizioni di riga incluse, 93 formule numerate, 3 gruppi non numerati, 15 tabelle con 324 celle, 12 figure e 21 asset, con 3 `ERR-MD`, 1 `ERR-AUDIT` e 0 `DUBBIO`; G7 non è stato avviato.

## Stato per sezione

| Sezione | File | Stato revisione |
|:---:|---|---|
| 4.1 | `4.1-calcestruzzo.md` | storico `VC-OK al 2026-08-04`, corrente `VC-SCADUTA al 2026-08-26`; 136/136 unità `COMPLETA/SCADUTO`; 13/17 asset certificati mancanti |
| 4.2 | `indice-4.2.md` e 13 file naturali | struttura e 63/63 asset completi; vecchio 4.2-A `VC-SCADUTA`; vecchi scope B-D sospesi e da non riprendere sui file archiviati |
| 4.3 | `4.3-composte.md` | testo controllato, norma e circolare presenti; tabelle NTC riallineate il 2026-05-30; 24 asset richiamati mancanti al 2026-08-26 |
| 4.4 | `4.4-legno.md` | testo controllato, norma e circolare presenti; tabelle NTC materiali riallineate il 2026-05-30; 4 asset richiamati mancanti al 2026-08-26 |
| 4.5 | `4.5-muratura.md` | controllato, norma e circolare presenti |
| 4.6 | `4.6-altri-sistemi.md` | controllato, norma e circolare presenti |

## Rilievi di revisione

### R1 - 4.1: numerazione formula 4.1.18 in forma sdoppiata

- **Stato:** osservazione storica, non trattata come errore.
- **Osservazione:** nel file non compare una formula taggata `4.1.18` in forma unica, ma compaiono `4.1.18a` e `4.1.18b`.
- **Valutazione:** la coppia appare coerente con il testo che introduce due relazioni distinte, una di resistenza e una di duttilità.

### R2 - 4.1: formula 4.1.50 presente due volte

- **Stato:** conforme alla fonte.
- **Osservazione:** nel file risultano due occorrenze del tag `4.1.50`.
- **Verifica:** il confronto con il PDF NTC 2018 conferma che la doppia numerazione `4.1.50` è presente anche nella fonte ufficiale, prima nel § 4.1.11.1 e poi nel § 4.1.12.1.
- **Valutazione:** non è un errore del Markdown.

### R3 - 4.1: controllo strutturale del markdown

- **Stato:** controllo positivo.
- **Controlli eseguiti:**
  - formule con delimitatori bilanciati;
  - immagini collegate a file esistenti;
  - riferimenti interni locali coerenti;
  - tabelle richiamate effettivamente presenti;
  - figure `4.1.1` - `4.1.4` presenti e correttamente collegate.

### R4 - 4.2: completamento del blocco C4.2 della circolare

- **Stato:** chiuso il 2026-05-20.
- **Osservazione:** la circolare C4.2 era rimasta incompleta nella conversione iniziale.
- **Esito:** completato il blocco da C4.2.4.1.4 Stato limite di fatica a C4.2.12 Profilati formati a freddo e lamiere grecate.
- **Aggiunte principali:** formule `[C4.2.93]` - `[C4.2.166]`, figure `C4.2.19` - `C4.2.36`, tabelle grafiche di fatica e tabelle `C4.2.XIX` - `C4.2.XX`.

### R5 - 4.2: riallineamento numerazione formule C4.2

- **Stato:** corretto il 2026-05-20.
- **Osservazione:** nel blocco C4.2.4.1.3.4 era stata rilevata una numerazione da riallineare.
- **Esito:** tolto il numero indebito alla formula di `sigma_E`, riportate le formule a `[C4.2.51]` - `[C4.2.92]` e separate le coppie `[C4.2.78.a]`/`[C4.2.78.b]` e `[C4.2.81.a]`/`[C4.2.81.b]`.

### R6 - 4.2: assenza di commenti autonomi in alcuni paragrafi della circolare

- **Stato:** chiarito, non anomalia.
- **Osservazione:** non risultano commenti autonomi per C4.2.5, C4.2.8, C4.2.10 e C4.2.11.
- **Verifica:** il PDF della circolare non contiene sezioni autonome per quei punti nel blocco considerato.
- **Valutazione:** il Markdown non deve inventare sezioni non presenti nella fonte.

### R7 - 4.3-4.6: controllo di completezza e collegamenti

- **Stato:** controllo positivo.
- **Osservazione:** i file `4.3-composte.md`, `4.4-legno.md`, `4.5-muratura.md` e `4.6-altri-sistemi.md` contengono norma e circolare corrispondente.
- **Esito:** nel controllo del 2026-05-20 non risultano immagini richiamate mancanti o wikilink rotti per il capitolo 4.

### R8 - 4.2-4.4: controllo numerico tabelle NTC e Circolare

- **Stato:** chiuso il 2026-05-30.
- **Perimetro:** controllo delle tabelle del capitolo 4, sia NTC sia Circolare C4, con confronto su PDF sorgenti in `raw/`.
- **Correzioni in `4.2-acciaio.md`:** riallineate le tabelle 4.2.I, 4.2.II, 4.2.VI, 4.2.VII, 4.2.IX(a-b), 4.2.XI, 4.2.XII, 4.2.XIII, 4.2.XIV, 4.2.XV, 4.2.XVI, 4.2.XVII e 4.2.XIX.
- **Correzioni in `4.3-composte.md`:** riallineate le tabelle 4.3.I e 4.3.II; sostituita la 4.3.III con immagine estratta dal PDF per conservare schemi e colonne originali.
- **Correzioni in `4.4-legno.md`:** riallineate le tabelle 4.4.I, 4.4.II e 4.4.III; mantenute le tabelle 4.4.IV e 4.4.V come immagini estratte dal PDF e aggiunta una trascrizione testuale controllata per renderle ricercabili e interrogabili dagli LLM.
- **Controlli positivi senza modifiche:** tabelle NTC 4.1, 4.5 e tabelle della Circolare C4 controllate; non sono emerse correzioni necessarie.
- **Materiale di verifica:** immagini di confronto PDF/Markdown in `_tmp_render/cap04/confronti/`.

### R9 - 4.1: ciclo G6 concluso e VC-OK

- **Stato:** chiuso il 2026-08-04 con `VC-OK` sul solo § 4.1 + § C4.1.
- **Perimetro:** solo § 4.1 NTC + § C4.1 Circolare, 136 unità e 37 pagine ufficiali.
- **Snapshot non superato dal primo G6:** SHA-256 `521a5e4f82bcb62be2fbb1d8f45751027b8670112020f18b363fe39cf20068a6`.
- **Secondo G6 r02:** realmente indipendente e cieco; 37 pagine, 81 formule numerate, 46 gruppi matematici non numerati, 11 tabelle e 17 figure. Esito `NON SUPERATO` per un solo `ERR-MD`; nessun `ERR-AUDIT` o `DUBBIO`.
- **Adjudicazione r02:** la fonte a 500 dpi riporta `[4.1.44]`; la precedente lettura `[4.1.44)` era errata.
- **Seconda correzione distinta:** il tag è ora reso con `\tag*{[4.1.44]}`; nessun'altra parte del testo, dell'indice o degli asset è stata modificata.
- **Nuovo snapshot r03:** SHA-256 `a05a99c00f13bc7e95b499f1136c927e0a0ffa19d9289e8b3ff77ee326f2acb4`; manifest SHA-256 `1026349fd1a7c45af39b57349ba482083db9e1eb91adfe23f749912898887048`.
- **Controlli post-correzione:** lint 0 errori e 0 avvisi; render integrale senza pagine vuote; tag verificato visivamente; G5 riconfermato.
- **Fase correttiva del 31/7:** chiusi gli undici rilievi del terzo giro; nuovo snapshot SHA-256 `a04eabdedcdb7f4d112d61f4b97291e3881f4a583784f1edf7f42f0bf4d0bc03`.
- **Quarto G6 del 3/8:** inventario source-first e dieci blocchi ciechi su 37/37 pagine; 81 formule numerate, 13 gruppi esposti non numerati, 11 tabelle o griglie, 274 celle logiche non vuote più una vuota strutturale, 17 figure.
- **Esito del quarto G6:** 43 famiglie `ERR-MD` per 61 siti materiali; zero `DUBBIO`, zero `ERR-AUDIT` e zero rilievi persistenti. Il file normativo non è stato modificato.
- **Quinto G6 del 3/8:** dopo la correzione delle 43 famiglie, esito non superato con 7 famiglie `ERR-MD` in 12 siti, zero `DUBBIO` e zero `ERR-AUDIT`.
- **Sesto G6 del 3/8:** dopo la correzione delle 7 famiglie, inventario fonte-prima di 37 pagine, 81 formule numerate, 20 gruppi non numerati, 11 tabelle o griglie con 315 celle logiche e 17 figure.
- **Esito del sesto G6:** una famiglia `ERR-MD` in un sito, zero `DUBBIO`, zero `ERR-AUDIT` e zero rilievi persistenti. Alla riga 993 manca la virgola dopo `A_c` prima di «essendo». Il file conserva SHA-256 `5b0d4356251f0d42b35b0b84e65c7dc11a18b21bf4a14dd5e23497551d253e9c`.
- **Settimo G6 del 4/8:** dopo l'autorizzazione di Sandro e la correzione distinta della sola R06-01, controllo integrale e cieco su 37/37 pagine con inventario fonte-prima e dieci blocchi separati; esito `ERR-MD=0`, `ERR-AUDIT=0`, `DUBBIO=0` sullo snapshot `93360710906737ff6a9c3d5f91b54e353282e2c1ab08d57deab099f7465d8964`.
- **G7:** manifest validato 21/21; 136/136 unità `COMPLETA/OK`; master autonomo `VC-OK al 2026-08-04`; master del corpus invariato `VC-DA-FARE`.
- **Evidenze:** giri storici sotto `_tmp_render/cap04/vc-paragrafo-4-1-20260730-*`; quarto, quinto e sesto G6 sotto `_tmp_render/cap04/vc-paragrafo-4-1-20260803-r01|r02|r03/g6/`; ciclo conclusivo sotto `_tmp_render/cap04/vc-paragrafo-4-1-20260804-r04/`; verbale e manifest finali in `verifica-conformita/`.

### R10 - 4.2-A: terzo G6 non superato per copertura incompleta

- **Stato:** sospeso il 2026-08-05, in attesa dell'autorizzazione di Sandro a un quarto G6 integrale.
- **Snapshot:** SHA-256 `8404fcb9e41a73d8ab6af7cd0be02da5e3dc32a3888e2c7a2ad315a0b5927bdd`; fonti ufficiali integre.
- **Esito:** cinque rapporti locali `OK`, ma consolidamento complessivo `KO` per due famiglie persistenti `ERR-AUDIT`.
- **Copertura mancante:** 19 righe normative ai confini N-A/N-B, N-B/N-C e N-C/C-A; asset della Figura C4.2.2 non confrontato insieme alla pagina fonte pertinente.
- **Procedura:** le partizioni r01-r03 non sono state ridisegnate. Con tre giri consumati su tre, G7 e ogni promozione restano vietati.
- **Evidenza:** `_tmp_render/cap04/vc-paragrafo-4-2a-20260804-r01/g6-r03/00-consolidamento-coordinato.md`.

### R11 - 4.2-A: quarto G6 non superato con undici ERR-MD

- **Stato:** sospeso il 2026-08-05, in attesa dell'autorizzazione di Sandro a un quinto G6 integrale.
- **Snapshot:** SHA-256 `8404fcb9e41a73d8ab6af7cd0be02da5e3dc32a3888e2c7a2ad315a0b5927bdd`; invariato durante il controllo.
- **Copertura:** inventario fonte-prima e quattro blocchi ciechi P2; 802/802 righe, 17/17 pagine e 10/10 asset. B2 e B3 sono stati ripetuti con verificatori freschi dopo la correzione del confine testuale.
- **Esito:** 11 occorrenze `ERR-MD`, zero `ERR-AUDIT`, zero `DUBBIO` e zero rilievi persistenti dal giro precedente.
- **Rilievi:** tre `E’→È`; punteggiatura difforme nei titoli `4.2.4.` e `C4.2`; `N_pl.Rd` reso `N_{pl,Rd}` nella [4.2.36]; riferimento redazionale assente dalla fonte; `é→è`; due segni `:` aggiunti; testo alternativo redazionale dell'asset della Tabella C4.2.I.
- **Procedura:** con `giro_g6: 4` e `max_giri: 4`, G7 e ogni promozione restano vietati. Il Markdown non è stato corretto; serve autorizzazione a `max_giri: 5` prima della fase correttiva distinta e del quinto G6.
- **Evidenze:** `_tmp_render/cap04/vc-paragrafo-4-2a-20260804-r01/g6-r04/04-consolidamento-p2.md`, `05-manifest-sha256-g6-r04.txt` e `06-controlli-meccanici-finali.txt`.

### R12 - 4.2-A: quinto G6 e G7 conclusi con VC-OK

- **Stato:** chiuso il 2026-08-06 con `VC-OK` sul solo sottoscope 4.2-A.
- **Perimetro:** NTC §§ 4.2-4.2.4.1.2.9 e Circolare §§ C4.2-C4.2.3.7, 37 unità e 17 pagine ufficiali.
- **Fase correttiva r05:** applicate esclusivamente le 11 occorrenze congelate dal quarto G6; diff indipendente P1 senza modifiche estranee. Nuovo snapshot `eccefb75094e290c75a9496d4d902bcff9bfecd7542affa566c23c69296e8994`.
- **Quinto G6:** inventario fonte-prima e quattro blocchi ciechi P2 con confini ridisegnati; copertura 801/801 righe, 17/17 pagine e 10/10 asset.
- **Adjudicazione:** il dubbio descrittivo su `φ₀` nel rapporto B4 è stato risolto su ritaglio a 600 dpi, estratto congelato e codepoint; la riga Markdown è conforme e l'errore materiale storico dell'audit è chiuso.
- **Esito G6:** `ERR-MD=0`, `ERR-AUDIT=0`, `DUBBIO=0` residui.
- **G7:** manifest validato 14/14; 37/37 unità e 37/37 righe dell'indice promosse; master autonomo `ntc2018--norme-costruzioni--cap04-2a` creato e promosso a `VC-OK al 2026-08-06`; master del corpus invariato `VC-DA-FARE`.
- **Evidenze:** `_tmp_render/cap04/vc-paragrafo-4-2a-20260804-r01/g6-r05/` e `g7/`; scope, verbale e manifest finali in `verifica-conformita/`.

### R13 - 4.2-B: terzo G6 non superato con nove ERR-MD

- **Stato:** sospeso il 2026-08-06, in attesa della decisione di Sandro sull'aumento di `max_giri` da 3 a 4.
- **Perimetro:** NTC §§ 4.2.4.1.3-4.2.4.1.7 e Circolare §§ C4.2.4-C4.2.4.1.3.4.9; 33 unità e 24 pagine ufficiali.
- **Snapshot:** SHA-256 `917134d6f52f66c2f8d62f6acfcbdd78a57f429f390a9f94f2046a598ff8aa8c`; invariato durante il terzo G6.
- **Copertura:** inventario fonte-prima, sei blocchi ciechi P2 e coordinamento P2 separato; 93 formule numerate, 4 gruppi matematici esposti non numerati, 15 tabelle e 12 figure, senza lacune di confine o apparato.
- **Esito:** 9 `ERR-MD`, 0 `ERR-AUDIT`, 0 `DUBBIO` e 0 rilievi persistenti dal giro precedente.
- **Rilievi:** formule [C4.2.51], [C4.2.52], [C4.2.54], [C4.2.57] e [C4.2.58] rese con una graffa assente dalla fonte e senza ripetizione del membro sinistro; difformità strutturali o di operatori nelle [C4.2.68], [C4.2.70], [C4.2.81.a] e [C4.2.85].
- **Procedura:** con `giro_g6: 3` e `max_giri: 3`, G7 e ogni promozione restano vietati. Il Markdown non è stato corretto; serve autorizzazione a `max_giri: 4` prima della correzione distinta e del quarto G6 integrale cieco.
- **Evidenza:** `_tmp_render/cap04/vc-paragrafo-4-2b-20260806-r02/g6-r03/coordinamento/01-verbale-coordinamento-g6-r03.md`.

### R14 - 4.2-B: quarto G6 non superato con due ERR-MD

- **Stato:** sospeso il 2026-08-06, in attesa della decisione di Sandro sull'aumento di `max_giri` da 4 a 5.
- **Snapshot:** SHA-256 `99af69e87987c10f50ab7eb10bb29428b61f84f35107ff011485697a8e1f80a2`; invariato durante il quarto G6.
- **Fase correttiva R04:** 9/9 interventi applicati da un correttore P2 separato; revisione indipendente del diff senza modifiche estranee.
- **Copertura:** inventario fonte-prima, sei blocchi ciechi P2 con confini ridisegnati e coordinamento P2 separato; 24 pagine, 93 formule numerate, 15 tabelle e 12 figure. Il rapporto C-D contaminato è stato invalidato e ripetuto integralmente.
- **Adjudicazione:** fascicolo 116/116; supplemento r0778 con pagina fisica 120 a 600 dpi e manifest 6/6. Le parentesi alle righe 0536 e 0854 sono `NORM`, senza ribaltare il precedente sulla [C4.2.86].
- **Esito:** 2 `ERR-MD`, 0 `ERR-AUDIT`, 0 `DUBBIO`: riga 0545, `\simeq` al posto di `=`; riga 0778, virgola omessa dopo `\sigma_{cr,p}`.
- **Procedura:** con `giro_g6: 4` e `max_giri: 4`, G7 e ogni promozione restano vietati. Serve autorizzazione a `max_giri: 5` prima della correzione distinta e del quinto G6 integrale cieco.
- **Evidenze:** `_tmp_render/cap04/vc-paragrafo-4-2b-20260806-r02/g6-r04/`; esito autoritativo `coordinamento/02-esito-consolidato-g6-r04.md`.

### R15 - 4.2-B: quinto G6 non superato con undici ERR-MD e un ERR-AUDIT

- **Stato:** sospeso il 2026-08-06, in attesa della decisione di Sandro sull'aumento di `max_giri` da 5 a 6.
- **Snapshot:** SHA-256 `d339546a906bd29a3687154828974e7b72a4b215cd2b323bd7796622491e14c5`; invariato durante il quinto G6.
- **Fase correttiva R05:** 2/2 interventi applicati da un correttore P2 separato; revisione indipendente del diff senza modifiche estranee.
- **Copertura:** inventario fonte-prima, sei blocchi ciechi P2 con confini ridisegnati e coordinamento P2 separato; packaging 94/94 e dossier 114/114, 24 pagine, 93 gruppi di formule numerate, 3 gruppi non numerati, 15 tabelle, 12 figure e 21 asset.
- **Adjudicazione:** 11 `ERR-MD`, relativi a un punto finale aggiunto, un'intestazione accorpata ripetuta, `LIMITI` reso al singolare, sette didascalie di tabella poste dopo l'immagine e una radice quadrata al posto della radice quarta; 1 `ERR-AUDIT` sul render, che duplica le didascalie e chiama figure anche le tabelle raster. Confermati `AF` i precedenti `b_{sl,l}` e `aso I`, oltre al doppio `++` della Tabella C4.2.X presente nella fonte.
- **Esito:** 11 `ERR-MD`, 1 `ERR-AUDIT`, 0 `DUBBIO`; `G6=KO`.
- **Procedura:** con `giro_g6: 5` e `max_giri: 5`, G7 e ogni promozione restano vietati. Serve autorizzazione a `max_giri: 6` prima della correzione distinta, della risoluzione dell'errore di audit e del sesto G6 integrale cieco.
- **Evidenza:** `_tmp_render/cap04/vc-paragrafo-4-2b-20260806-r02/g6-r05/coordinamento/01-verbale-coordinamento-g6-r05.md`, SHA-256 `b5ae882c30d92ed3f123af52226d4caa6b7cd41ae7df33dab43f20e3cd851dd1`.

### R16 - 4.2-B: settimo G6 non superato con tre ERR-MD e un ERR-AUDIT

- **Stato:** sospeso il 2026-08-25, in attesa della decisione di Sandro sull'aumento di `max_giri` da 7 a 8.
- **Snapshot:** SHA-256 `1b548e70e811ed9a508713db79688e67d468c86bf13765d7652413aa493b2b70`; invariato durante e dopo il settimo G6.
- **Fase correttiva r07:** applicati esclusivamente i 2 `ERR-MD` del sesto G6, `A_v/J_v` nella Tabella C4.2.II e radice quadrata nel numeratore della [C4.2.78.b]; revisione indipendente del diff e preflight superati.
- **Copertura:** inventario fonte-prima, sei blocchi ciechi e coordinamento separato; 24 pagine, 881 posizioni di riga incluse, 21 asset, 93 formule numerate, 3 gruppi non numerati, 15 tabelle con 324 celle e 12 figure. Manifest del dossier verificato 99/99.
- **Esito:** 3 `ERR-MD`, 1 `ERR-AUDIT`, 0 `DUBBIO`; `G6=KO`. Sulla pagina fisica 114 della Circolare il Markdown riporta `h_w^2` anziché `h_w` nella formula non numerata di `\sigma_E`, omette il prodotto in `0{,}5\cdot h_w` e i due prodotti in `15\cdot\varepsilon\cdot t`. L'inventario congelato assegna inoltre [C4.2.50] e `\sigma_E` alla pagina stampata 109 anziché 110 e trascrive `h_w^2` anziché `h_w`.
- **Procedura:** i due rilievi del sesto G6 restano chiusi. Con `giro_g6: 7` uguale a `max_giri: 7`, G7 e ogni promozione restano vietati. Serve autorizzazione a `max_giri: 8` prima della correzione distinta, dell'errata-corrige di audit e dell'ottavo G6 integrale cieco.
- **Evidenza:** `_tmp_render/cap04/vc-paragrafo-4-2b-20260806-r02/g6-r07/coordinamento/01-verbale-coordinamento-g6-r07.md`, SHA-256 `63303fd51205c092937a22ff471c842150f9584c8910dbe8d99db63cd194c889`.

### R17 - 4.2: ricomposizione per sottoparagrafi e ripristino degli asset

- **Stato:** correzione editoriale completata il 2026-08-25.
- I quattro file tecnici A-D sono stati sostituiti da 13 file corrispondenti alle sezioni naturali di livello 3 e da `indice-4.2.md`.
- Il confronto deterministico pre/post ha confermato la conservazione del testo per sezione, di 254 tag di formula e di 63 riferimenti grafici.
- Dei 63 PNG richiamati, 42 mancavano dal vivo: sono stati riestratti a 600 dpi, calibrati manualmente e controllati visivamente su sette tavole; nessun ritaglio contiene pagine intere o parti estranee.
- I vecchi file e lo snapshot di governo sono conservati in `_tmp_render/cap04/ristrutturazione-4.2-20260825/`. La ristrutturazione non promuove alcun esito VC e rende scaduto il precedente giudizio 4.2-A.
- **Firma:** CDX (Codex).

### R18 - 4.2: nomi dei file di livello 3 esplicitati con acciaio

- **Stato:** aggiornamento editoriale completato il 2026-08-26.
- I 12 file da `4.2.1` a `4.2.11` e `C4.2.12` adottano lo schema `4.2.x-acciaio-<argomento>.md`; `4.2-introduzione.md` e `indice-4.2.md` restano stabili.
- La rinomina ha aggiornato indici e 140 righe del registro senza modificare il contenuto: confronto byte per byte superato, 254 tag di formula e 63 riferimenti grafici conservati.
- **Firma:** CDX (Codex).

### R19 - Capitolo 4: perdita di asset e scadenza corrente del paragrafo 4.1

- **Stato:** rilievo strutturale aperto il 2026-08-26; non è una nuova collazione fonte-Markdown.
- L'inventario delle cartelle vive non ha trovato file vecchi o doppioni, ma ha rilevato 42 richiami PNG non risolti fuori dal § 4.2.
- Per il § 4.1 il manifest G7 elenca 17 asset unici. La ricerca nell'intero workspace ha recuperato quattro copie con lo stesso SHA-256, ripristinate senza modifiche; le copie omonime degli altri tredici hanno hash diverso e appartengono a snapshot anteriori.
- Il Markdown `4.1-calcestruzzo.md` resta byte-identico allo snapshot verificato. Il manifest corrente chiude con 7 percorsi `OK`, 13 `MANCANTE` e 1 `DIVERSO`, cioè `indice-cap04.md`.
- **Esito amministrativo:** giudizio storico invariato; validità corrente del § 4.1 portata a `VC-SCADUTA al 2026-08-26`, 136 unità `COMPLETA/SCADUTO`. Prima di una nuova promozione occorrono recupero o nuova estrazione verificata dei tredici asset, G4-G5 e nuovo G7.
- **Evidenze:** `_tmp_render/audit-struttura-capitoli-20260826/` e `_tmp_render/riallineamento-stati-vc-20260826/`.
- **Firma:** CDX (Codex).

## Criterio di classificazione

Per coerenza SGQ, in questo documento uso:
- **controllo positivo**: struttura coerente, navigazione corretta, apparati presenti;
- **osservazione**: punto da controllare o storicamente emerso, non confermato come errore;
- **anomalia probabile**: difformità plausibile, ma ancora da confermare sulla fonte;
- **errore confermato**: difformità certa rispetto a PDF o regola interna;
- **conforme alla fonte**: comportamento anomalo solo in apparenza, ma presente anche nel documento ufficiale.

## Controlli futuri consigliati

- Se si aggiorna uno dei file 4.1-4.6, registrare qui il controllo successivo.
- In caso di nuova estrazione immagini, verificare sempre richiami, didascalie e file in `img/`.
- Prima di dichiarare una nuova anomalia, confrontare sempre il PDF ufficiale.

## Cronologia

> [!info] Ordine cronologico inverso
> Le voci più recenti sono in cima.

### 2026-08-26 - Ricomposizione uniforme del capitolo 4 per livello 3

I §§ 4.1, 4.3, 4.4 e 4.5 sono stati ricomposti in indici e file naturali `x.y.z`; il § 4.2 era già conforme allo stesso criterio e il § 4.6 resta unitario. Confronto canonico, formule, immagini, registro e navigazione sono stati controllati senza regressioni. Lo storico VC del § 4.1 non è stato trasferito ai nuovi documenti. Evidenze in `_tmp_render/ricomposizione-livello3-20260826/`. **Firma:** CDX (Codex).

### 2026-08-26 - Audit degli asset e scadenza corrente del paragrafo 4.1

> [!warning] L'audit ha escluso vecchie versioni e doppioni nelle cartelle vive, ma ha accertato 42 richiami PNG mancanti nel capitolo 4. Il § 4.2 resta integro con 63/63 asset. Nel § 4.1 il Markdown conserva lo snapshot verificato, mentre tredici dei diciassette asset del manifest non sono più disponibili e l'indice condiviso è cambiato.
>
> Ripristinate soltanto quattro copie byte-identiche al manifest. Il § 4.1 è ora `VC-SCADUTA al 2026-08-26`; verbale ed esito storico del 2026-08-04 restano conservati.
>
> Evidenze in `_tmp_render/audit-struttura-capitoli-20260826/` e `_tmp_render/riallineamento-stati-vc-20260826/`.
>
> Firma: CDX (Codex).

### 2026-08-26 - Nomi dei file di livello 3 del paragrafo 4.2 esplicitati

> [!success] I 12 file di livello 3 del § 4.2 adottano ora nomi che contengono `acciaio`, secondo lo schema `4.2.x-acciaio-<argomento>.md`. Indici e registro sono stati riallineati; il confronto byte per byte conferma che il contenuto normativo non è cambiato.
>
> Evidenze in `_tmp_render/cap04/rinomina-acciaio-20260826/`.
>
> Firma: CDX (Codex).

### 2026-08-25 - Settimo G6 del paragrafo 4.2-B non superato

> [!failure] Dopo la correzione distinta dei due rilievi del sesto giro, il settimo G6 integrale cieco ha chiuso con 3 `ERR-MD`, 1 `ERR-AUDIT` e 0 `DUBBIO`. I due rilievi precedenti sono confermati chiusi. I nuovi scostamenti riguardano il denominatore di `\sigma_E` e tre operatori di prodotto omessi; l'inventario congelato richiede un'errata-corrige su pagina e trascrizione di [C4.2.50]/`\sigma_E`.
>
> Il file `4.2-acciaio-stabilita-verifiche.md` è rimasto invariato durante e dopo il controllo allo SHA-256 `1b548e70e811ed9a508713db79688e67d468c86bf13765d7652413aa493b2b70`. G7 non è stato avviato e nessun registro è stato promosso. Con `giro_g6: 7` e `max_giri: 7`, lo scope è sospeso in attesa dell'autorizzazione esplicita di Sandro alla correzione distinta, all'errata-corrige di audit e all'ottavo giro.
>
> Evidenze in `_tmp_render/cap04/vc-paragrafo-4-2b-20260806-r02/g6-r07/`; verbale autoritativo in `coordinamento/01-verbale-coordinamento-g6-r07.md`.
>
> Firma: CDX (Codex).

### 2026-08-06 - Quinto G6 del paragrafo 4.2-B non superato

> [!failure] Dopo la correzione distinta dei due rilievi precedenti, il quinto G6 integrale e cieco ha chiuso con 11 `ERR-MD`, 1 `ERR-AUDIT` e 0 `DUBBIO`. Oltre a quattro famiglie di scostamenti nel Markdown, il render aggiunge 21 didascalie automatiche, duplica quelle esplicite e denomina come figure anche le tabelle raster.
>
> Il file `4.2-acciaio-stabilita-verifiche.md` è rimasto invariato allo SHA-256 `d339546a906bd29a3687154828974e7b72a4b215cd2b323bd7796622491e14c5`. G7 non è stato avviato e nessun registro è stato promosso. Con `giro_g6: 5` e `max_giri: 5`, lo scope è sospeso in attesa dell'autorizzazione esplicita di Sandro alla correzione distinta, alla risoluzione dell'errore di audit e al sesto giro.
>
> Evidenze in `_tmp_render/cap04/vc-paragrafo-4-2b-20260806-r02/g6-r05/`; verbale autoritativo in `coordinamento/01-verbale-coordinamento-g6-r05.md`.
>
> Firma: CDX (Codex).

### 2026-08-06 - Quarto G6 del paragrafo 4.2-B non superato

> [!failure] Dopo la correzione distinta dei nove rilievi precedenti, il quarto G6 integrale e cieco ha chiuso con 2 `ERR-MD`, 0 `ERR-AUDIT` e 0 `DUBBIO`. I rilievi sono `\simeq` al posto di `=` nella formula non numerata di `\sigma_E` e la virgola omessa dopo `\sigma_{cr,p}`.
>
> Il file `4.2-acciaio-stabilita-verifiche.md` è rimasto invariato allo SHA-256 `99af69e87987c10f50ab7eb10bb29428b61f84f35107ff011485697a8e1f80a2`. G7 non è stato avviato e nessun registro è stato promosso. Con `giro_g6: 4` e `max_giri: 4`, lo scope è sospeso in attesa dell'autorizzazione esplicita di Sandro alla correzione distinta e al quinto giro.
>
> Evidenze in `_tmp_render/cap04/vc-paragrafo-4-2b-20260806-r02/g6-r04/`; esito consolidato in `coordinamento/02-esito-consolidato-g6-r04.md`.
>
> Firma: CDX (Codex).

### 2026-08-06 - Terzo G6 del paragrafo 4.2-B non superato

> [!failure] Il terzo G6 integrale e cieco ha raggiunto la copertura completa di 24 pagine, 93 formule numerate, 15 tabelle e 12 figure, congelando 9 `ERR-MD`; `ERR-AUDIT=0`, `DUBBIO=0` e rilievi persistenti 0.
>
> Il file `4.2-acciaio-stabilita-verifiche.md` è rimasto invariato allo SHA-256 `917134d6f52f66c2f8d62f6acfcbdd78a57f429f390a9f94f2046a598ff8aa8c`. G7 non è stato avviato e nessun registro è stato promosso. Con `giro_g6: 3` e `max_giri: 3`, lo scope è sospeso in attesa dell'autorizzazione esplicita di Sandro alla correzione distinta e al quarto giro.
>
> Evidenza in `_tmp_render/cap04/vc-paragrafo-4-2b-20260806-r02/g6-r03/coordinamento/01-verbale-coordinamento-g6-r03.md`.
>
> Firma: CDX (Codex).

### 2026-08-06 - Quinto G6 e G7 del paragrafo 4.2-A superati

> [!success] Il sottoscope 4.2-A è `VC-OK al 2026-08-06`.
>
> Dopo la correzione distinta delle 11 occorrenze congelate, il quinto G6 integrale e cieco ha chiuso con zero `ERR-MD`, zero `ERR-AUDIT` e zero `DUBBIO` residui. G7 ha validato 14/14 file, promosso 37/37 unità e lasciato `4`, `C4`, gli altri sottoscope 4.2, il Capitolo 4 e il corpus `VC-DA-FARE`. Snapshot finale: `eccefb75094e290c75a9496d4d902bcff9bfecd7542affa566c23c69296e8994`.
>
> Evidenze in `_tmp_render/cap04/vc-paragrafo-4-2a-20260804-r01/`; verbale in `verifica-conformita/verbale-VC-NTC2018-4.2-A-2026-08-06.md`.
>
> Firma: CDX (Codex).

### 2026-08-05 - Quarto G6 del paragrafo 4.2-A non superato

> [!failure] Il quarto G6 integrale e cieco ha raggiunto la copertura completa di 802/802 righe, 17/17 pagine e 10/10 asset, chiudendo le due famiglie `ERR-AUDIT` del giro precedente. L'adjudicazione su ritagli a 600 dpi e codepoint ha congelato 11 occorrenze `ERR-MD`; `ERR-AUDIT=0`, `DUBBIO=0` e rilievi persistenti 0.
>
> Il file `4.2-acciaio.md` è rimasto invariato allo SHA-256 `8404fcb9e41a73d8ab6af7cd0be02da5e3dc32a3888e2c7a2ad315a0b5927bdd`. G7 non è stato avviato e nessun registro è stato promosso. Con `giro_g6: 4` e `max_giri: 4`, lo scope è sospeso in attesa dell'autorizzazione esplicita di Sandro al quinto giro.
>
> Evidenze in `_tmp_render/cap04/vc-paragrafo-4-2a-20260804-r01/g6-r04/`.
>
> Firma: CDX (Codex).

### 2026-08-05 - Terzo G6 del paragrafo 4.2-A non superato

> [!failure] Il consolidamento dei cinque rapporti r03 ha accertato due famiglie persistenti `ERR-AUDIT`: 19 righe normative non giudicate e l'asset C4.2.2 privo di confronto con la propria pagina fonte. Le partizioni dei tre giri sono rimaste identiche.
>
> G6 è `KO`; con `giro_g6: 3` e `max_giri: 3` lo scope è sospeso in attesa dell'autorizzazione esplicita di Sandro a un quarto G6 integrale. G7 non è avviato, nessun registro è promosso e il file normativo non è stato modificato.
>
> Evidenza in `_tmp_render/cap04/vc-paragrafo-4-2a-20260804-r01/g6-r03/00-consolidamento-coordinato.md`.
>
> Firma: CDX (Codex).

### 2026-08-04 - Settimo G6 e G7 del paragrafo 4.1 superati

> [!success] Lo scope § 4.1 NTC + § C4.1 Circolare è `VC-OK al 2026-08-04`.
>
> Dopo la correzione distinta della sola virgola R06-01, il settimo G6 integrale e cieco ha chiuso con zero `ERR-MD`, zero `ERR-AUDIT` e zero `DUBBIO`. G7 ha validato 21/21 file, promosso 136/136 unità e lasciato il corpus `VC-DA-FARE`. Snapshot finale: `93360710906737ff6a9c3d5f91b54e353282e2c1ab08d57deab099f7465d8964`.
>
> Evidenze in `_tmp_render/cap04/vc-paragrafo-4-1-20260804-r04/`; verbale in `verifica-conformita/verbale-VC-NTC2018-4.1-2026-08-04.md`.
>
> Firma: CDX (Codex).

### 2026-08-03 - Sesto G6 del paragrafo 4.1 non superato

> [!failure] Il sesto G6 integrale e cieco ha congelato una sola famiglia `ERR-MD` in un sito materiale; nessun `DUBBIO` o `ERR-AUDIT` resta aperto.
>
> Il file `4.1-calcestruzzo.md` non è stato modificato durante G6 e conserva SHA-256 `5b0d4356251f0d42b35b0b84e65c7dc11a18b21bf4a14dd5e23497551d253e9c`. Il rilievo riguarda la virgola omessa alla riga 993 dopo `A_c`. G7 non è stato avviato e nessun registro è stato promosso. Il budget `max_giri: 6` è esaurito: lo scope è sospeso in attesa di un'eventuale autorizzazione al settimo giro.
>
> Evidenze in `_tmp_render/cap04/vc-paragrafo-4-1-20260803-r03/g6/`.
>
> Firma: CDX (Codex).

### 2026-08-03 - Quarto G6 del paragrafo 4.1 non superato

> [!failure] Il quarto G6 integrale e cieco ha congelato 43 famiglie `ERR-MD` in 61 siti materiali; nessun `DUBBIO` o `ERR-AUDIT` resta aperto.
>
> Il file `4.1-calcestruzzo.md` non è stato modificato e conserva SHA-256 `a04eabdedcdb7f4d112d61f4b97291e3881f4a583784f1edf7f42f0bf4d0bc03`. G7 non è stato avviato e nessun registro è stato promosso. Il budget `max_giri: 4` è esaurito: lo scope è sospeso in attesa di un'eventuale autorizzazione al quinto giro.
>
> Evidenze in `_tmp_render/cap04/vc-paragrafo-4-1-20260803-r01/g6/`.
>
> Firma: CDX (Codex).

### 2026-07-30 - Seconda correzione distinta post-G6 del paragrafo 4.1

> [!warning] Il G6 r02 realmente cieco ha congelato un solo `ERR-MD`: la fonte riporta `[4.1.44]`, non `[4.1.44)`.
>
> Corretto esclusivamente il delimitatore finale del tag. Nuovo snapshot r03 SHA-256 `a05a99c00f13bc7e95b499f1136c927e0a0ffa19d9289e8b3ff77ee326f2acb4`; lint 0 errori e 0 avvisi; G5 riconfermato. Serve un ulteriore G6 integrale, indipendente e cieco. Nessun `VC-OK`.
>
> Evidenze del G6 in `_tmp_render/cap04/vc-paragrafo-4-1-20260730-r02/g6/`; correzione e snapshot in `_tmp_render/cap04/vc-paragrafo-4-1-20260730-r03/`.
>
> Firma: CDX (Codex).

### 2026-07-30 - Correzione distinta post-G6 del paragrafo 4.1

> [!warning] Corretti in fase distinta i due `ERR-MD` del primo G6 e riallineate le quattro righe segnalate dal lint.
>
> Nuovo snapshot SHA-256 `fd67f65627f29b531aa3ced287d1c5490d7ee894f129f10d0b6b401bfca01705`; lint 0 errori e 0 avvisi; G5 riconfermato. Serve un nuovo G6 integrale, indipendente e cieco. Nessun `VC-OK`.
>
> Evidenze in `_tmp_render/cap04/vc-paragrafo-4-1-20260730-r02/`.
>
> Firma: CDX (Codex).

### 2026-07-30 - Audit VC-8 del paragrafo 4.1 non superato al G6

> [!failure] Completati G0-G5, ma il controllo indipendente G6 ha congelato due `ERR-MD` e un `ERR-AUDIT`.
>
> Non sono stati modificati il file normativo, gli asset o i registri VC; G7 non è stato avviato e il prompt resta in corso. Evidenze in `_tmp_render/cap04/vc-paragrafo-4-1-20260730-r01/g6/`.
>
> Firma: CDX (Codex).

### 2026-05-30 - Controllo numerico tabelle capitolo 4

> [!success] Controllate le tabelle del capitolo 4, norma e Circolare C4, contro i PDF sorgente.
>
> Corrette tabelle in `4.2-acciaio.md`, `4.3-composte.md` e `4.4-legno.md`. Le tabelle complesse 4.3.III, 4.4.IV e 4.4.V sono state riportate come immagini da PDF; per 4.4.IV e 4.4.V è stata aggiunta anche la trascrizione testuale controllata. Le immagini di confronto PDF/Markdown sono in `_tmp_render/cap04/confronti/`.

### 2026-05-21 - Rinominato come documento unico di revisione del capitolo 4

> [!info] Il vecchio file di revisione limitato al § 4.1 è stato trasformato in documento unico per tutto `cap04/`.
>
> Nuovo nome: `cap04-costruzioni-civili-industriali-revisione.md`.
>
> Aggiornati titolo, perimetro, stato per sezione, rilievi e riferimenti al file sorgente corretto `4.1-calcestruzzo.md`.

### 2026-05-20 - Controllo finale del capitolo 4

> [!success] Controllati i file `cap04/` contro il PDF NTC 2018 pagine 73-152 e contro la Circolare C4.
>
> Completata la circolare C4.2, riallineata la numerazione formule nel blocco C4.2.4.1.3.4, verificati immagini, indici e link interni. Il capitolo 4 risulta completo.

### 2026-04-11 - Apertura revisione mirata sul paragrafo 4.1

> [!note] Creato originariamente un file separato di revisione per il solo `4.1-calcestruzzo.md`.
>
> Verificati positivamente i collegamenti alle 4 immagini estratte.
>
> Registrati i primi rilievi: numerazione `4.1.18a`/`4.1.18b` da confermare e duplicazione della `4.1.50` da controllare.
