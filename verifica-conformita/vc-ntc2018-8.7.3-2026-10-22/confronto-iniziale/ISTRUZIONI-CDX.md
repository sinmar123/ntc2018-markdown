# Compito CDX: confronto integrale § 8.7.3 NTC 2018 e § C8.7.3 Circolare 7/2019

Sei il confrontatore (CDX, Codex gpt-5.6-terra) di una verifica di conformità. Lavori in sola lettura nella cartella corrente. Non modificare nulla, non leggere file fuori da questa cartella, non usare rete. La fonte è la pagina ufficiale: i PDF a pagina singola e le immagini qui presenti. Il testo estratto (`testo-*.txt`) è solo un ausilio. Non inventare: ogni rilievo deve essere visibile sulla pagina ufficiale.

## File
- `target-8.7.3.md`: il Markdown da verificare (righe numerate a partire da 1, file intero). Esclusi dal confronto: righe di navigazione, blocco INDICE-INTERNO, ancore `<a id=...>`, rubriche di servizio `## Norma`/`## Circolare` e il separatore `---`.
- `fonte-ntc-298.pdf` (+ `fonte-ntc-298.png` 200 dpi, `fonte-ntc-298-400dpi.png`): D.M. 17/01/2018, pagina fisica 298. Perimetro: dalla rubrica `8.7.3.` fino a prima di `8.7.4.` (la pagina contiene anche 8.7.1/8.7.2: fuori perimetro).
- `fonte-circ-289.pdf` (+ png 200 e 400 dpi): Circolare 21/01/2019 n. 7, pagina fisica 289. Perimetro: dalla rubrica `C8.7.3` fino a prima di `C8.7.4`.
- `catalogo.md`: catalogo delle normalizzazioni ammesse (voci 1-25). Una differenza che rientra nel catalogo NON è un rilievo.
- `convenzioni.md`: convenzioni del corpus e classificazione (ERR-MD, AF, AF-COR, DUBBIO).

Puoi usare python con PyMuPDF (fitz) per leggere il livello vettoriale dei PDF (testo, font, corsivi/grassetti con flags, posizioni delle righe, rientri), purché senza scrivere file.

## Che cosa confrontare, parola per parola
Rubriche (numero, punto finale, maiuscole/maiuscoletto secondo voce 23), ogni capoverso (unione o divisione dei capoversi come nella fonte), voci di elenco e loro marcatori e punteggiatura finale, ogni parola, punteggiatura, maiuscole, corsivi e grassetti, virgolette e apostrofi solo se fuori catalogo, simboli, pedici, apici ed esponenti, formule, tabelle, figure, note a piè di pagina (in corpus `[^n]`), rinvii (§, tabelle, formule). Fai DUE passaggi: il primo lineare, il secondo mirato solo a formule, simboli, esponenti, pedici, numeri e decimali (virgola o punto come stampato, voce 4), enfasi, a capo di capoverso e parole saltate o aggiunte.

## Uscita
Il tuo messaggio finale deve essere SOLO un oggetto JSON valido, senza testo attorno, con questa forma:
{"blocco":"unico","pagine":{"ntc":[298],"circ":[289]},"righe_md":"<intervallo confrontato>","conteggi":{"rubriche":n,"capoversi":n,"voci_elenco":n,"formule_display":n,"formule_inline":n,"tabelle":n,"figure":n,"note":n},
 "rilievi":[{"id":"T-01","riga_md":n,"pagina_fisica":"ntc 298|circ 289","riga_pagina":"<numero di riga di stampa contando dall'alto della pagina, o descrizione>","attuale":"<testo esatto del Markdown, che compaia una sola volta nel file>","fonte":"<come stampa la fonte>","proposto":"<testo sostitutivo>","classe":"ERR-MD|AF|DUBBIO","categoria":"rubrica|capoverso|elenco|parola|punteggiatura|enfasi|simbolo|formula|nota|altro","effetto":"forma|sostanziale","nota":"<motivo, con voce del catalogo se pertinente>"}],
 "passaggio_2":"<che cosa hai controllato nel secondo passaggio e con quale esito>",
 "controllati_senza_rilievi":["<elenco breve dei punti controllati e conformi>"]}
Effetto `sostanziale` = cambia o può cambiare il contenuto normativo (parole, numeri, simboli, rinvii, negazioni); `forma` = sola presentazione. Per i DUBBIO indica le letture possibili, senza scegliere. Se non trovi rilievi, `rilievi` è vuoto: non inventarne.
