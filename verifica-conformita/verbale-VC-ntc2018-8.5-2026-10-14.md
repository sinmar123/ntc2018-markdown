# Verbale VC: § 8.5 Definizione del modello di riferimento per le analisi, NTC e Circolare

Data di chiusura: 2026-10-14. Firma: CC cloud (CCC). Procedura VC-NTC/7, SHA-256 `01c7f0ed9908e4c7620189a0073b2892afe37aa499f99cf50329a84b43960e67`; catalogo SHA-256 `dd5f1b9980e6fd37bd0444277d8b69d6ac0c000b91c1cf659a4f9a398b4a7c43`, copie congelate nel dossier.

**Esito proposto: VC-OK** sui sei file, con snapshot aggregato SHA-256 `192309df7472efee19155003f2f11f539e1485a1b4517409ddb1c0b2ff260534` ([snapshot finale](vc-ntc2018-8.5-2026-10-14/snapshot-finale.json)), subordinato al giudizio G7 di V:

| File | SHA-256 |
|---|---|
| `cap08/8.5-introduzione.md` | `3b6931a00951f21b8322577d5a718a991f33b16f7b6ae456c1a17e46fb1f3ac1` |
| `cap08/8.5.1-modello-riferimento-analisi-analisi-storico-critica.md` | `a5e7dec4a8a8a4a9804fc58394c0db9287be7c6183d872adce9ad9b988b4dd75` |
| `cap08/8.5.2-modello-riferimento-analisi-rilievo.md` | `b38b46841388d1040f5d2c7e454b7fba2435a7a10860695150e9fdfb746f8cc2` |
| `cap08/8.5.3-modello-riferimento-analisi-caratterizzazione-meccanica-dei-materiali.md` | `dc9af032a6a935ce362b40e62bd57d6d7350ff24a338ffebf66e896049651009` |
| `cap08/8.5.4-modello-riferimento-analisi-livelli-di-conoscenza-e-fattori-di-confidenza.md` | `b2bdcedd7f36b38d456e9687825b7bde5d8ffa6616995971a3550d909544b4ba` |
| `cap08/8.5.5-modello-riferimento-analisi-azioni.md` | `17649ccb3a933834e0d7d2c9d2792360de645cffdd077ef2102015124c80b42a` |

## Perimetro e atti

- D.M. 17/01/2018, G.U. n. 42 del 20/02/2018, S.O. n. 8, § 8.5 fino a prima di 8.6: pagine fisiche 296-297 della copia congelata, SHA-256 `dda1e397d56d71aa0f5bc457c3ba9b77064a468699dfc37bd056ac6c47105a46`. Scheda ufficiale: https://www.gazzettaufficiale.it/eli/id/2018/02/20/18A00716/sg
- Circolare 21/01/2019 n. 7 C.S.LL.PP., G.U. n. 35 dell'11/02/2019, S.O. n. 5, § C8.5 fino a prima di C8.6, con la nota 3: pagine fisiche 257-269, SHA-256 `f7c3b8d1f443aadb6b3e020b6b6c19813683492ecaadd2c15bf6bf1939aaed7c`. Scheda ufficiale: https://www.gazzettaufficiale.it/eli/id/2019/02/11/19A00855/sg

Righe del registro: 8.5, 8.5.1, 8.5.2, 8.5.3, 8.5.4, 8.5.5. Nel perimetro: tre formule numerate ([C8.5.4.1]-[C8.5.4.3]), sei tabelle (C8.5.I, C8.5.II, C.8.5.III, C8.5.IV, C8.5.V, C8.5.VI), nessuna figura.

## Vigenza

Ricognizione piena del **2026-10-13** ([ricognizione](vc-ntc2018-3.3-ancore-blocco-2026-10-13/g1/ricognizione-20261013.json)) e ricontrollo mirato del **2026-10-14** ([ricontrollo](vc-ntc2018-8.4-2026-10-14/g1/ricontrollo-20261014.json)), riusati entro i trenta giorni ([riuso](vc-ntc2018-8.5-2026-10-14/g1/riuso-g1.json)): schede ufficiali identiche; il D.M. 9 marzo 2023 non tocca il § 8.5 né C8.5.

## Storia dello scope e gate

- **Presa in carico** 2026-10-14 su autorizzazione di Sandro («vai con l'8.5»). Righe 8.5.1-8.5.5 `DA-RICONFERMARE`, riga 8.5 `MAI-FATTA`.
- **G0:** sei file; confini riscontrati sulla codifica dei PDF. Testo unico composto con le sei parti della Norma prima e le sei della Circolare dopo, per tagliare i blocchi del G6 a fine pagina.
- **G1:** come sopra, due date.
- **G2-G4 di C:** confronto parola per parola con il testo del PDF e tabelle cella per cella. Lista L1-L14 e D1 ([lista](vc-ntc2018-8.5-2026-10-14/lista-correzioni-c.json), ritagli in `c/`). L1 cambia un valore: nel C8.5.5.1 la fonte dà q = 1,75 αu/α1, il file 3,0. Decisione di Sandro: «ok tutto». Correzioni con script ([diff](vc-ntc2018-8.5-2026-10-14/diff-correzioni.diff)).
- **G5:** resa canonica con `strumenti/render-capitolo.py` prima del G6 (20 pagine) e dopo le correzioni del G6 (21 pagine): nessun tag tondo, nessuna didascalia automatica, nessun glifo mancante. Dopo le correzioni ci sono due rese degli stessi sei file, che differiscono solo per l'ordine di composizione: `modifiche/resa-dopo.pdf` (SHA-256 `c5c8ca4b…`, Norma prima e Circolare dopo, come il testo del G6) è la resa finale controllata dai V; `modifiche-r01-pacchetto-errato/resa-dopo.pdf` (SHA-256 `bee19c2f…`, file per file) è quella citata da `modifiche/controllo-script.json`, conservata.
- **G6 giro 1, integrale, quattro blocchi:** V Opus a contesto nuovo, uno per blocco (b01 NTC 296-297 e Circolare 257-259; b02 260-262; b03 263-265; b04 266-269). Inventari fonte-prima di 67, 65, 68 e 60 elementi, validati e congelati prima della rivelazione; b02 ha chiesto ritagli a 600 dpi e codepoint per pedici ed esponenti ([prove](vc-ntc2018-8.5-2026-10-14/prove-v-b02/)). La prima rivelazione è fallita per file di lavoro di V dentro le cartelle dei blocchi; nuova destinazione con fonti e inventari identici byte per byte, prima di ogni accesso al target ([recupero](vc-ntc2018-8.5-2026-10-14/recupero-confezionamento-g6-r01b.json)). Confronti integrali, tutti gli id coperti, esito `KO` in ogni blocco: 5, 10, 6 e 6 rilievi ([rapporti](vc-ntc2018-8.5-2026-10-14/g6-r01b/)). Valori, formule e celle conformi.
- **Riscontro di C** su codifica dei PDF e ritagli fino a 1200 dpi ([ritagli](vc-ntc2018-8.5-2026-10-14/c-g6/)). Respinti: «V maiuscola» nella testata della Tab. C8.5.I (codepoint U+0076, v a corpo pieno come nella didascalia, catalogo n. 13; V b02 accetta) e titolo «Circolare» della resa (apparato del corpus). Aggiunto da C: «Rilievo(dei» senza spazio nella Tab. C8.5.V.
- **Decisioni di Sandro** (2026-10-14): ripristinare capoversi ed enfasi della fonte; rubriche della Circolare come nella fonte; greche come simboli; un solo trattino nella colonna fv0. Lista unica approvata («Sì, applica tutto»), poi O22-O23 dopo il controllo della resa ([lista](vc-ntc2018-8.5-2026-10-14/lista-correzioni-g6.json)).
- **Correzioni:** 192 voci generate da script sulla codifica del PDF ([script](vc-ntc2018-8.5-2026-10-14/strumenti-lista-g6/)) e applicate da script; indici interni rigenerati con `strumenti/genera-indici-interni.py`. La lista riapplicata ai file di partenza ridà il corpus, esclusi gli indici interni ([controllo](vc-ntc2018-8.5-2026-10-14/modifiche/controllo-script.json)).
- **Controllo delle modifiche (§ 8):** stessi quattro V, ciascuno sul proprio blocco. Il primo pacchetto era confezionato male da C, file per file invece che Norma prima e Circolare dopo: l'hanno segnalato tutti e quattro i V, b01, b02 e b03 come ERR-AUDIT residuo e b04 come osservazione non bloccante ([primo tentativo](vc-ntc2018-8.5-2026-10-14/modifiche-r01-pacchetto-errato/)). Rifatto con la composizione del G6: esito OK nei quattro blocchi, nessun rilievo residuo ([attestazioni](vc-ntc2018-8.5-2026-10-14/modifiche/)). Osservazione non bloccante di V b02: nella resa PDF, sulle pagine di continuazione della Tab. C8.5.II si ripete solo la prima riga di testata, perché la seconda riga è di corpo secondo il catalogo n. 6.
- **G7:** primo tentativo `KO` documentale ([G7 r01](vc-ntc2018-8.5-2026-10-14/G7-r01-KO.json)): segnalazioni del primo pacchetto attribuite a due V anziché a quattro; resa citata dal controllo di script assente dal manifest. Rimediati; giudizio finale nel file `G7.json` del dossier.

Copertura: il G6 integrale copre tutto il testo dello snapshot consegnato al G6, comprese le correzioni L1-L14; le righe cambiate dopo il G6 sono coperte dal controllo delle modifiche.

## Normalizzazioni, anomalie e correzioni

- Normalizzazioni del catalogo dichiarate dai V: 1, 2, 3, 4, 5, 6, 10, 11, 13.
- Anomalie della fonte conservate (A), fra le altre: «C8..5.4.3», «τ almeno pari a 3», «(LC)crescenti», «§ C8.5.2,prove», «Intonacoarmato», «Rilievo(dei», «illustrate» senza punto, `f_m^{0.35}` con il punto decimale, «E’ inoltre», frase ripetuta alle pp. 265 e 267.
- Particolarità tipografiche della fonte non riprodotte, per decisione di Sandro: sottolineature (p. 269, D1; cinque tratti alle pp. 258-259, D4); doppio trattino per cella nella colonna fv0 della Tab. C8.5.I (D2); stile dei due punti e della «s» dopo due etichette di p. 265 (D3); simboli f, fm, fv0, τ0, E, G stampati in grassetto nella Circolare (D6). I marcatori di elenco della fonte sono resi come elenchi Markdown (D5).
- Correzioni di ERR-MD di questo scope (nessuna AF-COR): L1-L14 prima del G6, fra cui il valore di q; dopo il G6, 66 enfasi (E), 21+2 voci puntuali (O: pedici ed esponenti di fm, N/mm² e γG, didascalia della Tab. C8.5.I, testata della Tab. C8.5.II su due livelli, punto e spazio aggiunti, lineetta, richiami in apice, greche e X media come simboli, due capoversi), 17 rubriche (R), 86 capoversi (C).

## Manifest e catena degli hash

Manifest di rilascio nel dossier (`manifest-rilascio.json`), con fonti, target, procedura e catalogo congelati, G1, inventari, congelamenti, rapporti e configurazione del G6, prove e ritagli, liste, script, attestazioni dei due pacchetti di modifiche, resa finale e snapshot finale. Le immagini delle fonti e delle rese consegnate ai V nei pacchetti del G6 non sono copiate: le loro impronte sono negli `input-fonte.json` e `input-confronto.json` dei blocchi e si rigenerano con `vc-supporto.py prepara` da `config-g6-r01.json`. Manifest superato, conservato: `manifest-rilascio-r01.json` (125 file, senza la prima resa dopo le correzioni). G7 e registrazioni chiudono la catena dall'esterno.

## Esecutori e limiti

C: la sessione cloud CC cloud (modello Opus), che non ha scritto le correzioni in modo interpretativo: le voci sono state generate da script sulla codifica del PDF, approvate da Sandro e applicate da script. V: quattro subagenti Opus a contesto nuovo, isolamento istruttivo nello stesso ambiente, ciascuno limitato alla cartella del proprio blocco e alle prove consegnate. Nessun E. Controlli eseguiti da agenti AI, senza revisione umana integrale; Sandro ha deciso sui rilievi. Consumi: non disponibili. La resa dei viewer diversi dal renderer canonico è quella dichiarata nel catalogo.

Questione fuori scope: il renderer canonico non ha i glifi greci, e le lettere greche scritte come testo semplice spariscono dal PDF di controllo. Nel § 8.5 è risolta con le voci O11-O18, O21-O23; altri 42 file del corpus hanno greche in testo semplice, da trattare a parte.

VC-OK vale per questo snapshot e perimetro, senza sostituire la fonte ufficiale.

Prossima azione: Nessuna sul file: VC conclusa sullo snapshot registrato.
