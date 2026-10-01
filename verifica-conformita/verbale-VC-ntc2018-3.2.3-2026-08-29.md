---
scope_id: ntc2018-3.2.3
data: 2026-08-29
stato: VC-OK
markdown_sha256: f2a3371c8beea285ed11b6a18e2a8169b4284740e6583742843345d5cc767086
fonte_ntc_sha256: dda1e397d56d71aa0f5bc457c3ba9b77064a468699dfc37bd056ac6c47105a46
fonte_circolare_sha256: f7c3b8d1f443aadb6b3e020b6b6c19813683492ecaadd2c15bf6bf1939aaed7c
---

# Verbale di verifica di conformità - NTC 2018 § 3.2.3 e Circolare C3.2.3

## Perimetro

Il controllo riguarda esclusivamente `cap03/3.2.3-azione-sismica-valutazione-dell-azione-sismica.md`, corrispondente al § 3.2.3 dell'allegato al D.M. 17 gennaio 2018 e al § C3.2.3 della Circolare 21 gennaio 2019 n. 7.

Le fonti occupano le pagine fisiche NTC 51-55 e Circolare 51-54. Inventario finale: 9 pagine fonte, 12 gruppi di formule numerate o taggate, 4 tabelle con 55 celle logiche e 2 figure.

## Fonti e normalizzazioni

- D.M. 17 gennaio 2018: `verifica-conformita/fonte-ufficiale/GU-2018-42-SO8-DM-17-01-2018.pdf`, SHA-256 `dda1e397d56d71aa0f5bc457c3ba9b77064a468699dfc37bd056ac6c47105a46`.
- Circolare 21 gennaio 2019 n. 7: `verifica-conformita/fonte-ufficiale/GU-2019-35-SO5-Circolare-7-2019.pdf`, SHA-256 `f7c3b8d1f443aadb6b3e020b6b6c19813683492ecaadd2c15bf6bf1939aaed7c`.
- Elenco unico applicato: `verifica-conformita/normalizzazioni-dichiarate-NTC2018.md`, SHA-256 `d71319206ec54bcac3639dfd0b97c41754fa1062655b2d35c36ee5d6cb3036d6`.

La resa dei tag con parentesi quadre nel PDF canonico è stata verificata. I trattini corto, medio e lungo nei separatori delle didascalie sono stati considerati equivalenti secondo la normalizzazione dichiarata n. 10.

## Gate

- G0 `OK`: identità, file e confini accertati direttamente sulle nove pagine.
- G1 `OK`: fonti ufficiali identificate e hash ricalcolati.
- G2 `OK`: inventario source-first e collazione integrale completati.
- G3 `OK`: glifi protetti, cifre, apici, pedici, operatori, disuguaglianze, unità e tag verificati sui ritagli a 600 dpi.
- G4 `OK`: 12 gruppi di formule numerate o taggate, 4 tabelle con 55 celle logiche, 2 asset e 2 didascalie riconciliati.
- G5 `OK`: render finale di 9 pagine, apparati di navigazione e 1.754 collegamenti interni verificati.
- G6 `OK` per deroga esplicita: quattro giri integrali documentati, correzione finale certa e controllo indipendente mirato autorizzato da Sandro in luogo del quinto giro.
- G7 `OK`: precontrollo P0-D Moon e controllo finale P2 Sol hanno confermato il dossier e il manifest 47/47.

## G6 e deroga finale

I giri G6 R01-R03 hanno prodotto correzioni e adjudicazioni registrate. Il G6 R04, svolto con fonte-prima congelata, tre blocchi disgiunti, copertura 9/9 e coordinamento indipendente, ha chiuso cinque rilievi come `ERR-AUDIT` e ha lasciato un solo `ERR-MD`: `Categoria di sottosuolo` al posto della forma fonte `Categoria sottosuolo` nella Tab. 3.2.VII.

Raggiunto il massimo di quattro giri, Sandro ha autorizzato il 2026-08-29 una scelta di buon senso: correggere soltanto la parola aggiunta, svolgere un controllo indipendente mirato, ripetere il preflight P0-D Moon e passare al G7 P2 Sol, senza un quinto G6 integrale. Il confronto posizionale fra gli snapshot rileva una sola riga modificata, la riga 173, e nessuna variazione nelle altre 305 righe.

Il primo controllo mirato ha confermato tutte le 12 celle ma ha contestato la didascalia del solo estratto di audit. I due rilievi sono stati chiusi come `ERR-AUDIT`: il trattino è coperto dalla normalizzazione n. 10 e il punto finale era stato aggiunto soltanto nell'estratto, non nel target normativo. L'estratto riallineato è stato affidato a un secondo verificatore indipendente, che ha confermato 12/12 celle e 1/1 didascalia, con zero `ERR-MD`, zero `ERR-AUDIT` e zero `DUBBIO`.

La verifica focalizzata non viene presentata come quinto G6. Il G6 R04 resta storicamente `KO` sullo snapshot precedente; G6 è chiuso `OK` per deroga dichiarata sullo snapshot finale.

## Anomalie della fonte

Sono conservate alla lettera quattro anomalie:

- `F_o` nel denominatore interno del primo ramo della formula `[3.2.8]`;
- accento acuto in `é in genere` nel § C3.2.3.6;
- pedice minuscolo `T_e` nel denominatore della formula `[3.2.11]`;
- rinvio della Circolare alla Tabella 3.2.II per le condizioni topografiche.

Classificazione: 4 `AF`, 0 `AF-COR`. Cifre, casse e simboli protetti sono stati conservati senza correzioni per inferenza.

## G7 e indipendenza

Il precontrollo G7 P0-D `gpt-5.6-luna/medium` ha ricalcolato 47/47 hash e 47/47 dimensioni del manifest, con 47/47 file presenti, zero duplicati e zero voci estranee. Il decisore finale P2 `gpt-5.6-sol/xhigh` ha pronunciato `G7 OK`, con zero rilievi aperti o persistenti.

I controlli sono stati eseguiti da agenti AI; non è inclusa una revisione umana integrale.

## Snapshot ed evidenze

Snapshot iniziale Markdown: `a4ba890ee9712149e5c5b3e2b88769135cda83a5e21b95201d1cb1352ce33660`.

Snapshot finale verificato: `f2a3371c8beea285ed11b6a18e2a8169b4284740e6583742843345d5cc767086`.

Frammento normativo finale depurato dagli apparati: `ad97ea6914146922fd6aac9e5992c7af3bdd93c370e6c218eb0115b2eb42b1e0`.

Render finale: `cde3871c076f335874ac632665df92abd44fab41a6093083cd329b4153e48ad8`.

Evidenze principali:

- `_tmp_render/cap03/vc-3.2.3-20260828/preflight/rapporto-consolidato-g0-g5.md`;
- i nove ritagli di scope a 600 dpi in `_tmp_render/cap03/vc-3.2.3-20260828/g6-preparazione/fonte/`;
- i rapporti G6 e le adjudicazioni in `_tmp_render/cap03/vc-3.2.3-20260828/g6-r01/`, `g6-r02/`, `g6-r03/` e `g6-r04/`;
- la correzione, i controlli mirati, il frammento e il render finali in `_tmp_render/cap03/vc-3.2.3-20260828/deroga-finale-20260829/`;
- i rapporti G7 in `_tmp_render/cap03/vc-3.2.3-20260828/g7-finale-20260829/`;
- `cap03/annotazioni/3.2.3-anomalie-fonte.md`;
- `verifica-conformita/manifest-sha256-ntc2018-3.2.3-2026-08-29.txt`.

## Rilascio

SHA-256 del manifest finale: `42658bc6d013a01146ce8f08398e97fa31c367801c3cb7645fed9aa102a0f05a`, 47 voci.

Tutti i gate G0-G7 sono `OK` secondo il percorso e la deroga dichiarati. Non restano rilievi aperti o persistenti. Lo scope è promosso localmente a `VC-OK al 2026-08-29`; il giudizio vale soltanto per lo snapshot e il perimetro dichiarati.

Firma della redazione: CDX (Codex).
