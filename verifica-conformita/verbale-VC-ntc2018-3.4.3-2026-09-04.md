---
scope_id: ntc2018-3.4.3
data: 2026-09-04
stato: VC-OK
markdown_sha256: f310e117cbcf8fe1cb0329a1ae5ff8cb21b82c7aa1e018482e2c26d3a250d8c6
fonte_ntc_sha256: dda1e397d56d71aa0f5bc457c3ba9b77064a468699dfc37bd056ac6c47105a46
fonte_circolare_sha256: f7c3b8d1f443aadb6b3e020b6b6c19813683492ecaadd2c15bf6bf1939aaed7c
---

# Verbale di verifica di conformità - NTC 2018 § 3.4.3

Perimetro: `cap03/3.4.3-neve-coefficiente-di-forma-delle-coperture.md`, § 3.4.3 NTC alle pagine fisiche 62-63 e § C3.4.3 Circolare alle pagine fisiche 76-80. Lo scope comprende 14 rubriche, 6 formule numerate, 10 gruppi matematici non numerati o inline sostanziali, 2 tabelle con 20 celle logiche e 8 figure con i relativi asset. I §§ 3.4.2/C3.4.2 e 3.4.4-3.4.5 sono esclusi; la Circolare non contiene un autonomo C3.4.4 e il § C3.4.3 termina prima di C3.4.5 a pagina fisica 81.

Le due fonti ufficiali congelate sono state ricalcolate il 4 settembre 2026 e risultano identiche byte per byte ai PDF ufficiali correntemente distribuiti dalla Gazzetta Ufficiale. G0 ha confermato identità, integrità e confini naturali. G1 ha verificato le fonti ufficiali correnti alla medesima data. Il D.M. 9 marzo 2023, n. 52, incide sull'articolo 2 del decreto e sui punti 11.4.2 e 11.5.2, non sui §§ 3.4.3/C3.4.3. Non sono state individuate rettifiche o modifiche successive incidenti sullo scope; resta la normale riserva sulla disciplina transitoria applicabile alla singola opera.

G2-G5 hanno inizialmente individuato rubriche e prosa non letterali, un capoverso omesso, riferimenti e didascalie difformi, scostamenti nelle formule e nelle definizioni, la resa di una cella di tabella e tutti gli otto asset vivi mancanti. Un correttore P1 distinto ha applicato soltanto la lista congelata, ha creato e collegato le annotazioni permanenti e ha ripristinato gli otto asset da copie vettoriali o ritagli a 600 dpi delle fonti. Il primo controllo post-correzione ha isolato cinque famiglie residue: le locuzioni `in cui` e `dove:`, il segno stretto in `$b_2$ < $l_s$`, la grafia `Figura C.3.4.5` e due simboli `μ₁` non visibili nel render. Dopo adjudicazione separata, un P1 distinto ha applicato la seconda lista congelata. P0-D e P2 post-correzione hanno quindi chiuso G2-G5 `OK` con zero `ERR-MD`, `ERR-AUDIT` e `DUBBIO`.

Le sei formule `[C3.4.2]`-`[C3.4.7]`, i dieci gruppi matematici sostanziali e le venti celle conservano cifre, coefficienti, esponenti, pedici, operatori, condizioni, unità e tag della fonte. Il render canonico finale contiene nove pagine, mostra entrambe le occorrenze `μ₁`, non contiene `U+FFFF`, rende i sei tag fra parentesi quadre e non introduce didascalie automatiche. Gli otto asset sono presenti, leggibili, completi e separati dalle didascalie.

Il G6 R01 ha usato un inventario fonte-prima e due blocchi primari disgiunti: blocco A sulle pagine NTC 62-63 e Circolare 76-77, blocco B sulle pagine Circolare 78-80. Il blocco B, scelto per densità di formule, glifi e figure, è stato duplicato in un secondo contesto indipendente. Un primo congelamento fonte-prima, che aveva inventariato la didascalia come `Figura C3.4.5` anziché `Figura C.3.4.5`, è stato respinto prima dell'esposizione al Markdown. Anche la prima confezione dei pacchetti è stata respinta prima del confronto per la collisione, sul filesystem Windows, fra `scope.md` e `SCOPE.md`; il target non era presente nei pacchetti difettosi. Le evidenze negative sono conservate, ma non hanno consumato un giro. I pacchetti v2 validi hanno verificato 15/15 input ciascuno, copertura primaria 7/7 pagine e concordanza completa del duplicato. G6 R01 ha chiuso `OK` al primo giro effettivo con zero `ERR-MD`, `ERR-AUDIT`, `DUBBIO` e `AF-COR`.

Le differenze residue ricadono esclusivamente nelle normalizzazioni dichiarate in `verifica-conformita/normalizzazioni-dichiarate-NTC2018.md`: spazi e a capo, varianti Unicode e composizione matematica equivalente, spaziatura e raggruppamenti LaTeX, resa delle virgole effettivamente stampate, strutture di elenco e blocchi di definizione, separatori delle didascalie, ripetizione delle celle logicamente accorpate e rimozione degli apparati di navigazione dai pacchetti G6. Nei viewer che non usano il template canonico possono variare soltanto la composizione grafica delle formule e l'allineamento dei tag, senza variazione del contenuto: questa è una normalizzazione di visualizzazione.

Le otto anomalie della fonte conservate sono documentate in `cap03/annotazioni/3.4.3-anomalie-fonte.md`: secondo ramo della `[C3.4.4]` privo di condizione e valore `L_c = 50 m` non coperto; alternanza `C3.4.x`/`C.3.4.x`; relazione `k ≤ dγ`; `sin` corsivo; locuzione `ed Caso (ii)`; concordanza `La presenza ... causano`; concordanza `l'azione ... sommato`; definizione finale di `α` senza verbo. Non risultano `AF-COR` né scostamenti silenziosi.

Il G7 ha impiegato un P0-D `gpt-5.6-luna` medium per i controlli deterministici e un P2 fresco `gpt-5.6-sol` xhigh per la ripetizione critica finale. Il primo G7 è stato fermato perché il rapporto P0-D riportava un hash NTC storico errato, pur lasciando invariati target ed evidenze. Il rapporto sostitutivo `rapporto-p0d-g7-r01.md` ha rettificato l'unico `ERR-AUDIT`; il P2 fresco ha ricalcolato le impronte, riconfermato la continuità delle evidenze e chiuso G7 R02 `OK`. Il manifest `verifica-conformita/manifest-sha256-ntc2018-3.4.3-2026-09-04.txt` contiene 328/328 record verificati, 328 percorsi univoci, zero duplicati, file mancanti o mismatch; SHA-256 del manifest `0082c99993186fa1644ca6b88e3b830b8b4d391b002a8a02d2321b327f5774bd`. Il rapporto P2 finale ha SHA-256 `959f511d1c859306fed8da651f76d659caf079bed5eb50db78f08db1b939bdf8`.

Controlli finali: indici interni, 311 file e 1.754 collegamenti, `OK`; linter del registro, 311 righe e 11 colonne, zero errori e zero avvisi; target UTF-8 con BOM e soli LF, zero caratteri di sostituzione; 15 ancore interne e nessun link relativo rotto; render finale di nove pagine controllato integralmente, senza tagli, sovrapposizioni o segnaposto.

Tutti i gate G0-G7 sono `OK`. Promozione locale a `VC-OK al 2026-09-04` sul solo snapshot `f310e117cbcf8fe1cb0329a1ae5ff8cb21b82c7aa1e018482e2c26d3a250d8c6`. Il master generale del corpus resta `VC-DA-FARE`, perché la chiusura del singolo file naturale non conclude il corpus. I controlli indipendenti sono stati eseguiti da agenti AI; non è inclusa una revisione umana integrale.

Evidenze: `_tmp_render/cap03/vc-3.4.3-20260904/`.

Firma della redazione: CDX (Codex).
