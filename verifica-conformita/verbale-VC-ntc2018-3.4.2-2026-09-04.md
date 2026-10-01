---
scope_id: ntc2018-3.4.2
data: 2026-09-04
stato: VC-OK
markdown_sha256: 8ba6dd0a425e4133e8e0ff05fb2114b6f60cb2801f2d0bd7a07332958b610e77
fonte_ntc_sha256: dda1e397d56d71aa0f5bc457c3ba9b77064a468699dfc37bd056ac6c47105a46
fonte_circolare_sha256: f7c3b8d1f443aadb6b3e020b6b6c19813683492ecaadd2c15bf6bf1939aaed7c
---

# Verbale di verifica di conformità - NTC 2018 § 3.4.2

Perimetro: `cap03/3.4.2-neve-valore-di-riferimento-del-carico-della-neve-al-suolo.md`, § 3.4.2 NTC alle pagine fisiche 61-62 e § C3.4.2 Circolare alla pagina fisica 76. Lo scope comprende cinque gruppi di formule numerate con nove rami complessivi, zero formule esposte autonome non numerate, zero tabelle e due figure con didascalia. I §§ 3.4.1/C3.4.1 e 3.4.3/C3.4.3 sono esclusi.

Le due fonti ufficiali congelate sono state ricalcolate e coincidono con gli hash registrati. G0 ha confermato identità, integrità e confini naturali. G1 ha verificato le fonti ufficiali correnti alla data del controllo. Il D.M. 9 marzo 2023, n. 52, incide sull'articolo 2 del decreto e sui punti 11.4.2 e 11.5.2, non sui §§ 3.4.2/C3.4.2. Non sono state individuate modifiche successive incidenti sullo scope; resta la normale riserva sulla disciplina transitoria applicabile alla singola opera.

G2-G5 hanno inizialmente individuato rubriche non letterali, un capoverso omesso, due asset mancanti e scostamenti puntuali nella prosa, nella formula della Circolare, nelle definizioni e nella didascalia. Un correttore P1 distinto ha applicato soltanto la lista congelata e ha ripristinato i due PNG come copie binarie degli estratti fonte. I controlli post-correzione hanno riconfermato completezza, fedeltà, formule, struttura, collegamenti, asset e render. Le formule NTC `[3.4.2]`-`[3.4.5]` e la formula Circolare `[C3.4.1]` conservano cifre, coefficienti, divisori, esponenti, pedici, operatori, condizioni, unità e tag della fonte.

Il G6 R01 ha coperto 53/53 elementi e 19/19 input, chiudendo `NON OK`. L'adjudicazione ha respinto come `ERR-AUDIT` del verificatore il candidato sulla locuzione `d un anno`, letterale nella fonte, e ha confermato il grassetto del rinvio `C3.4.1` e la gerarchia a doppio livello delle sette occorrenze di `q` nella Circolare. La non regressione è fondata su ritagli a 1200 dpi, codifica e origini vettoriali dei glifi, più conferme P2 in contesti separati. Un P1 distinto ha applicato le correzioni congelate in due passaggi; la catena degli snapshot è `53c48aa53c85f11c3517c10e2876b20675edb593527ef06357968826c560c1cc` -> `e3ea42dee106d07267474cc5287224198d3092896e62533ecfa3c8c066b5c1fb` -> `8ba6dd0a425e4133e8e0ff05fb2114b6f60cb2801f2d0bd7a07332958b610e77`.

Prima del G6 R02 il coordinatore ha scartato un primo congelamento fonte-prima che chiudeva indebitamente la parentesi nella definizione di `P_n` e non censiva in modo affidabile il numeratore finale. Il Markdown non era stato ancora reso disponibile, il pacchetto non è stato usato per il confronto e il giro non è stato consumato. Un P2 fresco ha prodotto un secondo congelamento source-first valido. Il confronto cieco R02 ha verificato 23/23 input e 46/46 elementi, chiudendo `OK` con zero `ERR-MD`, zero `ERR-AUDIT` e zero `DUBBIO`.

Le differenze residue ricadono esclusivamente nelle normalizzazioni dichiarate in `verifica-conformita/normalizzazioni-dichiarate-NTC2018.md`: spazi e a capo, varianti Unicode, spaziatura e raggruppamenti LaTeX, resa delle virgole effettivamente stampate, formule a più rami con tag singolo, elenchi e blocco `dove`, separatori delle didascalie, rimozione degli apparati di navigazione dai pacchetti e resa tipografica dei pedici. Le nove anomalie di fonte conservate sono documentate in `cap03/annotazioni/3.4.2-anomalie-fonte.md`: `d un anno`; `provincie`; alternanza di punti e virgole decimali; rinvio `C.3.4.1.` contro tag `[C3.4.1]`; parentesi non chiusa nella definizione di `P_n`; giustapposizione `C3.4.1n`; doppio livello dei pedici di `q`; concordanza `immutato sia i valori`; `In esse` dopo un richiamo singolare. Non risultano `AF-COR` né scostamenti silenziosi.

Il G7 ha impiegato prima un P0-D `gpt-5.6-luna` medium per il manifest deterministico e poi un P2 fresco `gpt-5.6-sol` xhigh. Il manifest `verifica-conformita/manifest-sha256-ntc2018-3.4.2-2026-09-04.txt` contiene 135/135 record verificati, zero duplicati e zero mismatch; SHA-256 del manifest `8111afc93a904007362a717d851c8819c8224d9d2f5c7cf95d44902987148b49`. Il P2 ha ricalcolato target, fonti, asset, congelamenti, manifest input e render, ha riconfermato la separazione dei ruoli e ha chiuso G7 `OK`; rapporto P2 SHA-256 `c31429873733bad9923d6e1cd632ca1213e67c240cd8448a6a88cc8919851247`.

Controlli finali: indici interni, 311 file e 1.754 collegamenti, `OK`; linter del registro, zero errori e zero avvisi; target UTF-8 con BOM e soli LF, zero `U+FFFD`; i due asset coincidono byte per byte con gli estratti fonte; render finale di quattro pagine controllato integralmente, con testo, formule, figure e didascalie leggibili e non tagliati. I cinque tag sono resi fra parentesi quadre e non risultano didascalie automatiche estranee.

Tutti i gate G0-G7 sono `OK`. Promozione locale a `VC-OK al 2026-09-04` sul solo snapshot `8ba6dd0a425e4133e8e0ff05fb2114b6f60cb2801f2d0bd7a07332958b610e77`. Il master generale del corpus resta `VC-DA-FARE`, perché la chiusura del singolo file naturale non conclude il corpus. I controlli indipendenti sono stati eseguiti da agenti AI; non è inclusa una revisione umana integrale.

Evidenze: `_tmp_render/cap03/vc-3.4.2-20260904/`.

Firma della redazione: CDX (Codex).
