---
scope_id: ntc2018-c3.3.11
data: 2026-09-03
stato: VC-OK
markdown_sha256: e33a5fd69766a6c821cb03b2d4efcb495b1a33c6611ace17a25f1c58f45e2d92
fonte_circolare_sha256: f7c3b8d1f443aadb6b3e020b6b6c19813683492ecaadd2c15bf6bf1939aaed7c
---

# Verbale di verifica di conformità - Circolare NTC 2018 § C3.3.11

Perimetro: `cap03/c3.3.11-vento-distacco-di-vortici.md`, § C3.3.11 della Circolare a p. fisica 75. Lo scope comprende una rubrica, sei capoversi narrativi o introduttivi, quattro formule numerate, sei relazioni o uguaglianze inline, due blocchi `dove` con sei definizioni e un elenco finale di tre voci. Non contiene testo NTC, tabelle, figure o asset del target. Il § C3.3.11 termina a `massima cautela.`; la pagina fisica 76 apre il § C3.4, rimasto fuori perimetro.

La fonte ufficiale congelata è stata ricalcolata e coincide con l'hash registrato. G0 ha accertato identità e confini dello scope. G1 ha identificato il fascicolo ufficiale G.U. `19A00855` e documentato la ricognizione di vigenza al 2026-09-03; il D.M. 9 marzo 2023 esaminato non interviene sul § C3.3.11.

G0-G5 hanno riconciliato integralmente confini, inventario, prosa, formule, simboli e navigazione. Sullo snapshot iniziale `aefaf0de041d4bda506851d6146a8c3e32acb305954a1c4841b828fa13486e36` sono stati individuati tre `ERR-MD`: cassa e punto della rubrica, mancato corsivo matematico dell'`i` in `i-esimo` e correzione silenziosa `cha`/`che`. Un correttore P1 distinto ha applicato esclusivamente le tre sostituzioni congelate. I controlli post-correzione P0-D e P1 hanno riconfermato G0-G5 `OK` sullo snapshot finale.

Le normalizzazioni applicabili sono quelle dell'elenco unico `verifica-conformita/normalizzazioni-dichiarate-NTC2018.md`. Nel presente scope ricorrono le voci 1, 2, 3, 12, 13 e 18: spaziature e a capo, varianti Unicode equivalenti, resa LaTeX senza mutamento strutturale, parentesi quadre dei tag garantite dal render ufficiale, pedici composti a corpo pieno nella fonte e blocchi `dove` resi come elenchi. In particolare, la forma fonte `fs` è resa `$f_s$` secondo NORM-13.

Le anomalie permanenti pertinenti sono conservate e documentate in `cap03/annotazioni/3.3-anomalie-fonte.md`: `AF-3.3-05` per `n_k`/`n_i` e per le due occorrenze di `v_{m,l}`, `AF-3.3-15` per `fs`/`n_s`, `AF-3.3-16` per `Si osservi cha`. Le soglie `Sc > 30`, `5 < Sc < 30` e `Sc < 5` sono condizioni letterali della fonte e non costituiscono una nuova AF. Non vi sono `AF-COR` nello scope.

Il preflight ha inoltre individuato e chiuso tre `ERR-AUDIT`: il primo inventario aveva reso il simbolo fonte `fs` come `f_s`, normalizzato `cha` in `che` e usato un primo ritaglio a 600 dpi troncato durante l'elenco finale. La collazione successiva ha ristabilito le forme corrette e il G6 ha ricevuto esclusivamente il ritaglio completo di 4250 x 5000 pixel, SHA-256 `0f585ac4bc08bd677a373883c4bbd2af23d91d12bced0fbb6d80dd38878c67f5`.

Il G6 R01 cieco è stato eseguito da un P2 fresco `gpt-5.6-sol` xhigh. Un primo avvio, il cui incarico esponeva accidentalmente conteggi di preflight, è stato interrotto prima che producesse file e non ha contribuito al giudizio. Il verificatore effettivo ha prodotto e congelato inventario, esito provvisorio e criterio fonte-prima prima di ricevere il Markdown; integrità confermata 3/3 per il congelamento e 11/11 per il pacchetto di confronto.

Il rapporto G6 originario ha coperto integralmente lo scope ma ha letto come cifra `1` la lettera `l` in `v_{m,l}` e ha pronunciato `KO`. Il target non è stato modificato. Tre ritagli diretti dal PDF a 1200 dpi, il codepoint `U+006C` della definizione e la pronuncia di un P2 fresco distinto hanno confermato la lettera `l`. Lo stesso verificatore G6 ha ritirato la richiesta di correzione con un addendum separato. È stato chiuso anche l'errore di segmentazione iniziale di sette anziché sei capoversi, senza omissioni testuali. Esito autoritativo G6 R01: zero `ERR-MD`, zero `ERR-AUDIT` residui e zero `DUBBIO`; nessun R02 necessario.

Il G7 ha impiegato prima un P0-D per il ricalcolo deterministico e poi un P2 fresco `gpt-5.6-sol` xhigh. Il manifest `verifica-conformita/manifest-sha256-ntc2018-c3.3.11-2026-09-03.txt` contiene 49/49 record verificati; SHA-256 del manifest `f4ee37a00afb9f5e1efec9e7e822946d16a3353ea2e196b5fc1036b6fb56e168`. Entrambi i passaggi hanno confermato snapshot, integrità 3/3 e 11/11, catena G0-G6, adjudicazione `l`/`1`, resa finale e assenza di residui. Esito G7 `OK`.

Controlli finali: indici interni, 311 file e 1.754 collegamenti, `OK`; linter del registro, zero errori e zero avvisi; quattro link locali risolti; zero U+FFFD; quattro tag unici e ordinati; render finale di due pagine ispezionato integralmente, senza perdita o troncamento.

Tutti i gate G0-G7 sono `OK`. Promozione locale a `VC-OK al 2026-09-03` sul solo snapshot `e33a5fd69766a6c821cb03b2d4efcb495b1a33c6611ace17a25f1c58f45e2d92`. I controlli sono stati eseguiti da agenti AI; non è inclusa una revisione umana integrale.

Evidenze: `_tmp_render/cap03/vc-c3.3.11-20260903/`.

Firma della redazione: CDX (Codex).

