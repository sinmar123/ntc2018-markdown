---
scope_id: ntc2018-3.3.1
data: 2026-08-31
stato: VC-OK
markdown_sha256: f9116d86bd340884e93151d8e295b6e7b06daecc21771bd1e9ca3d13ed00a1ba
fonte_ntc_sha256: dda1e397d56d71aa0f5bc457c3ba9b77064a468699dfc37bd056ac6c47105a46
fonte_circolare_sha256: f7c3b8d1f443aadb6b3e020b6b6c19813683492ecaadd2c15bf6bf1939aaed7c
---

# Verbale di verifica di conformità - NTC 2018 § 3.3.1

## Perimetro

Il controllo riguarda esclusivamente `cap03/3.3.1-vento-velocita-base-di-riferimento.md`, corrispondente ai §§ 3.3.1 del D.M. 17 gennaio 2018 e C3.3.1 della Circolare 21 gennaio 2019 n. 7.

La Norma occupa la pagina fisica 56 e prosegue nella pagina 57 con la sola Fig. 3.3.1 e la relativa didascalia, prima dell'apertura del § 3.3.2. La Circolare occupa nella pagina fisica 54 il tratto compreso fra il titolo C3.3.1 e il titolo C3.3.2.

Inventario finale: 2 titoli, 5 capoversi di prosa, 3 blocchi formula, 2 tag, 4 definizioni, una tabella con 50 celle logiche, una figura e 2 didascalie.

## Riuso delle verifiche storiche

Il vecchio scope aggregato aveva già chiuso G0-G5 e completato un G6 integrale. La ricomposizione del 26 agosto ha superato 506/506 confronti canonici; il confronto mirato fra file naturale corrente e staging ha confermato che il contenuto normativo di 3.3.1 è rimasto identico e che le sole differenze introdotte riguardavano apparati di navigazione e collegamenti redazionali.

G0-G5, inventari e verifiche degli apparati sono stati quindi riusati, senza ripetere lavoro già valido. Sono stati rilanciati soltanto i controlli resi necessari dal nuovo file naturale: indici, render, disponibilità dell'asset, G6 e G7.

## Fonte e normalizzazioni

- D.M. 17 gennaio 2018: `verifica-conformita/fonte-ufficiale/GU-2018-42-SO8-DM-17-01-2018.pdf`, SHA-256 `dda1e397d56d71aa0f5bc457c3ba9b77064a468699dfc37bd056ac6c47105a46`.
- Circolare 21 gennaio 2019 n. 7: `verifica-conformita/fonte-ufficiale/GU-2019-35-SO5-Circolare-7-2019.pdf`, SHA-256 `f7c3b8d1f443aadb6b3e020b6b6c19813683492ecaadd2c15bf6bf1939aaed7c`.
- Elenco unico applicato: `verifica-conformita/normalizzazioni-dichiarate-NTC2018.md`, SHA-256 `d71319206ec54bcac3639dfd0b97c41754fa1062655b2d35c36ee5d6cb3036d6`.

Le normalizzazioni rilevate riguardano impaginazione, ricomposizione delle parole spezzate, liste di definizioni, resa LaTeX, tag, formula a più rami, ritaglio della figura e didascalie.

## Gate

- G0-G5 `OK` per riuso validato: identità, fonti, inventario, collazione e apparati sono coperti dalle evidenze storiche e dalla prova di continuità della ricomposizione; gli apparati nuovi sono stati verificati.
- G6 R01 `KO`: confronto integrale con un solo `ERR-MD`, la cassa della rubrica C3.3.1; zero `ERR-AUDIT` e zero `DUBBIO`.
- G6 R02 `OK`: nuovo confronto cieco integrale sullo snapshot corretto, con copertura 100% e zero residui.
- G7 P0-D `OK`: 27/27 percorsi, dimensioni e SHA-256 coincidenti, senza duplicati.
- G7 P2 `OK`: snapshot promuovibile e nessuna condizione bloccante.

## Correzioni e asset

Rispetto allo snapshot naturale iniziale sono cambiate due sole righe normative:

1. rubrica NTC 3.3.1 riportata alla cassa maiuscola della fonte;
2. rubrica C3.3.1 privata del punto assente nella fonte e riportata alla cassa maiuscola.

Le tre operazioni correttive sono state eseguite da un P1 distinto con prova inversa positiva; la seconda riga ha richiesto due passaggi perché il G6 R01 ha individuato la cassa non rilevata dal giro aggregato.

La Fig. 3.3.1, assente dalla cartella viva dopo la ricomposizione, è stata ripristinata byte-identica dalla copia già verificata del G4/G6 storico, SHA-256 `59efa69fa7c618cc42b35bde4cc9327a2656b720b97ee7380246da7027c13f4c`.

Resta una sola `AF-COR`, la nota `AF-COR-3.3-02` su `v_{b,0}`: la lettura corretta è attestata nella formula `[3.3.1]` della stessa pagina e la nota è presente sul posto. Nessun `AF` ulteriore.

## Snapshot ed evidenze

Snapshot iniziale: `78cc5089f03ee52dd20cc79251724029d527ff7330b855bbb796dd6c70cee672`.

Snapshot finale verificato: `f9116d86bd340884e93151d8e295b6e7b06daecc21771bd1e9ca3d13ed00a1ba`.

Manifest: `verifica-conformita/manifest-sha256-ntc2018-3.3.1-2026-08-31.txt`, 27 voci, SHA-256 `670566829255ef446bba3e8ddd3d76e510944d508197e5c16662de845c54e8ec`.

Evidenze principali:

- `_tmp_render/cap03/vc-3.3.1-20260831/continuita/`;
- `_tmp_render/cap03/vc-3.3.1-20260831/g6-r01/`;
- `_tmp_render/cap03/vc-3.3.1-20260831/g6-r02/`;
- `_tmp_render/cap03/vc-3.3.1-20260831/g7/`;
- `_tmp_render/cap03/vc-3.3.1-20260831/render-finale.pdf`.

## Rilascio

Residui finali: 0 `ERR-MD`, 0 `ERR-AUDIT`, 0 `DUBBIO`, 0 `AF` e 1 `AF-COR` conforme. Tutti i gate G0-G7 sono `OK`. Lo scope è promosso localmente a `VC-OK al 2026-08-31`; il giudizio vale soltanto per lo snapshot e il perimetro dichiarati.

I controlli sono stati eseguiti da agenti AI; non è inclusa una revisione umana integrale.

Firma della redazione: CDX (Codex).
