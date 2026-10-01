---
title: Annotazioni capitolo 3 - NTC 2018
aliases:
  - Annotazioni cap. 3 NTC 2018
tags:
  - formazione/normativa
  - ntc2018
  - annotazioni
---

[Torna all'indice del capitolo 3](../indice-cap03.md)

# Annotazioni capitolo 3

Questa cartella raccoglie note tecniche, dubbi, verifiche e possibili refusi relativi al capitolo 3.

I file normativi del capitolo restano il più possibile fedeli al testo ufficiale. Le annotazioni sono separate e collegate dai punti interessati, così il testo della norma resta pulito e le osservazioni possono essere discusse, aggiornate o corrette senza alterare la trascrizione principale.

Nei file normativi il richiamo è una nota numerata con collegamento Markdown relativo, per esempio `[1](./3.3-note-redazionali.md#nota-1)`, posta accanto alla tabella, formula o figura interessata. Anche i collegamenti di ritorno usano percorsi relativi e ancore Markdown, così restano attivi fuori da Obsidian.

**Il testo della nota sta in questa cartella, non in fondo al file normativo.** Dal 5/8/2026 il file normativo contiene soltanto ciò che sta nella fonte: la sezione «Note redazionali» che stava in coda a `3.3-vento.md` è stata spostata in `3.3-note-redazionali.md`. La ragione è nel ciclo di conversione e verifica, § 5, «Il file normativo contiene solo la fonte»: un blocco di Markdown che non corrisponde ad alcuna pagina della fonte non ha destinatario nel confronto cieco del G6, quindi o non lo controlla nessuno o viene segnalato come testo aggiunto a ogni giro.

Restano invece nel file normativo i richiami numerati e gli eventuali identificatori di navigazione, che non sono testo della fonte: sono riconoscibili meccanicamente e vanno tolti dal Markdown quando si confezionano i pacchetti dei blocchi ciechi, così il verificatore confronta con la fonte solo il testo.

## Convenzione

Ogni annotazione dovrebbe indicare:

- riferimento normativo interessato;
- tipo di nota: refuso, dubbio, conversione, confronto fonte, interpretazione;
- stato: da verificare, probabile, confermato, rettificato ufficialmente;
- autore o origine della segnalazione, quando utile;
- fonti consultate.

## Elenco

| Riferimento | Annotazione | Stato |
|---|---|---|
| § 3.5.2 (AF-3.5.2-01) | [Anomalia della fonte conservata](3.5.2-anomalie-fonte.md) | **Da leggere prima di correggere per inferenza la seconda durata transitoria del § 3.5.2**: la fonte stampa `d un anno` e chiude la voce con punto e virgola; il Markdown conserva entrambi. |
| § 3.4.3 (AF-3.4.3-01/08) | [Anomalie della fonte conservate](3.4.3-anomalie-fonte.md) | **Da leggere prima di correggere formule, riferimenti o concordanze per inferenza**: la fonte lascia senza condizione il secondo ramo della `[C3.4.4]`, alterna `C3.4.x` e `C.3.4.x`, stampa `k ≤ dγ` e `sin` corsivo, e conserva quattro anomalie grammaticali. Il Markdown riproduce tutte e otto le anomalie; nessuna `AF-COR`. |
| § 3.4.2 (AF-3.4.2-01/09) | [Anomalie della fonte conservate](3.4.2-anomalie-fonte.md) | **Da leggere prima di correggere per inferenza testo, decimali, tag, parentesi, spaziatura, concordanze o pedici del § 3.4.2/C3.4.2**: la fonte stampa `d un anno`, `provincie`, alterna punti e virgola decimali, usa il tag `[C3.4.1]` contro il rinvio `C.3.4.1.`, lascia aperta una parentesi nella definizione di `$P_n$`, giustappone `C3.4.1n`, usa nella Circolare pedici di `$q$` a doppio livello, scrive `immutato sia i valori` e `In esse` dopo il richiamo singolare. Il Markdown conserva tutte e nove le anomalie. |
| § 3.2.1 (AF-3.2.1-01/03) | [Anomalie della fonte conservate](3.2.1-anomalie-fonte.md) | **Da leggere prima di completare le testate della Tabella C.3.2.II per inferenza**: la fonte lascia vuoti i tre valori dopo `$C_U =$`, stampa `$T_r$` minuscolo nella testata destra e usa `Cu` nella legenda raster; il Markdown conserva le tre anomalie. |
| § 3.2.2 (AF-3.2.2-01/05) | [Anomalie della fonte conservate](3.2.2-anomalie-fonte.md) | **Da leggere prima di correggere formule, testate, rinvii o disuguaglianze per inferenza**: la fonte usa `j=2` nella prima sommatoria `[C.3.2.4]`, alterna `V_{S,eq}` e `V_{s,j}`, intesta la Tab. 3.2.II con caratteristiche topografiche, rinvia alla Tabella 3.2.IV per le categorie T1-T4 e affianca «maggiore di 30 m» a `(H ≥ 30 m)`. Il Markdown conserva tutte e cinque le anomalie. |
| § 3.2.3 (AF-3.2.3-01/04) | [Anomalie della fonte conservate](3.2.3-anomalie-fonte.md) | **Da leggere prima di correggere formule, accenti o rinvii per inferenza**: la fonte stampa `F_o` nel denominatore interno della `[3.2.8]`, `T_e` nel denominatore della `[3.2.11]`, `é in genere` nella Circolare e rinvia alla Tabella 3.2.II per le condizioni topografiche. Il Markdown conserva le quattro anomalie. |
| § 3.3 (AF-3.3-01…16, AF-COR-3.3-01/02) | [Anomalie della fonte conservate e corrette](3.3-anomalie-fonte.md) | **Da leggere prima di correggere per inferenza il § C3.3.10, oppure di usare in un calcolo le Tab. C3.3.I, C3.3.IV, C3.3.XI e C3.3.XVII, il § C3.3.8.3 sulle pareti circolari e la [C3.3.11] sul distacco di vortici**: in quei punti la Gazzetta è anomala e noi la riproduciamo fedelmente. In particolare `AF-3.3-05` spiega perché la [C3.3.11] porta il pedice `v_m,l` e non `v_m,i`, `AF-3.3-06` perché il § C3.3.8.3 scrive `c_peo` e `ψ_λα` invece della notazione degli Eurocodici, `AF-3.3-15` conserva `fs`/`n_s` e `AF-3.3-16` conserva «Si osservi cha». Contiene anche le due correzioni di classe C del corpus, `AF-COR-3.3-01` sulla Tab. 3.3.II e `AF-COR-3.3-02` sulla definizione di `v_b,0` |
| § 3.3 (Note 1-8) | [Note redazionali del § 3.3](3.3-note-redazionali.md) | Spostate dal file normativo il 5/8/2026; le Note 5-8 sono classe N da riversare nel verbale |
| Fig. 3.3.2 | [Lettura tabellare delle categorie di esposizione](fig-3.3.2-categorie-esposizione-lettura-llm.md) | Da verificare sullo schema grafico originale |
| Tab. C3.3.I | [Possibile refuso `$C_{U}$` nelle intestazioni](tab-c3.3.i-refuso-cu.md) | Probabile refuso non confermato ufficialmente |
