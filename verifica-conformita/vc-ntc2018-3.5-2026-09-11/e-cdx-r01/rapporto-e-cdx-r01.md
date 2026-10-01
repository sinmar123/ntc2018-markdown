# Rapporto E, applicazione lista G6 r01, § 3.5

**Firma:** Codex / CDX Terra medium, 2026-09-11.

Lista congelata verificata: `lista-correzioni-g6-r01.json`, SHA-256 `6ca6843e575cfb9e8c14f8b7ded72b686280fb254f1e59ac7b17d27bfec82963`.
Addendum append-only verificato: `addendum-lista-correzioni-g6-r01-001.json`, SHA-256 `0b2e128cb0cf3d1ee16d0f689acd91b5c3acffd676ce39a96f9b79cd900e0bb9`.

## Operazioni applicate

1. Sostituzione testuale in § 3.5.2.
2. Ritaglio Pillow dell’asset da raster 600 dpi, box 0-based `(1720, 2020, 3240, 3680)`, nessun ridimensionamento.
3. Inserimento `Estate` nella prima riga pertinente della tabella 3.5.I.
4. Inserimento `Estate` nella seconda riga pertinente della tabella 3.5.I.
5. Duplicazione prescritta di `Inverno` nella riga invernale della tabella 3.5.I.
6. Sostituzione testuale nel commento C3.5.
7. Creazione dell’annotazione AF-3.5.2-01 col contenuto esatto della lista.
8. Inserimento della riga AF-3.5.2-01 nell’indice delle annotazioni.
Addendum: inserita la sola àncora HTML esplicita nell’annotazione appena creata.

## Snapshot post-E

| Path | SHA-256 | Byte |
|---|---|---:|
| `cap03/3.5-introduzione.md` | `b963768d94fbd72d33baae26efb18a71dcfb5998cff2d2dd7f189e503521249c` | 950 |
| `cap03/3.5.2-temperatura-temperatura-dell-aria-esterna.md` | `5242a12816ea4c2bfdc0fa71dc8af8e934481d5fad592a832ef21fec36e5bf31` | 3543 |
| `cap03/3.5.4-temperatura-distribuzione-della-temperatura-negli-elementi-strutturali.md` | `5f2d207a728b6c8a68d3e33ad767290b1bfd94a2b464250a0ce691e76a4fd7c7` | 2494 |
| `cap03/annotazioni/README.md` | `8ee1f5ee97db57d3f82173b8c0082e72bf39e1fba566cc0a01d3a6c88514d5e3` | 6043 |
| `cap03/img/fig-3.5.1-zone-temperatura-mappa.png` | `fec8da7e6de1b4009d6d7a79ce88e7d0c136bd252e5242f5f5a8ab25536f7ff1` | 716633 |
| `cap03/annotazioni/3.5.2-anomalie-fonte.md` | `554711b40704d622d75ac73fe1cfb0ea769f8e291a2ec2bafc5a736a6a69d4a4` | 1366 |

## Figura 3.5.1

- Dimensioni: 1520 × 1660 px, RGB.
- SHA-256 post-E: `fec8da7e6de1b4009d6d7a79ce88e7d0c136bd252e5242f5f5a8ab25536f7ff1`.
- Byte post-E: 716633.
- Verifica meccanica: output identico pixel per pixel al crop richiesto del raster di input, box e dimensioni conformi; nessun resize.

## Diff completo del testo, prima/dopo

### `cap03/3.5-introduzione.md`
```diff
--- prima/cap03/3.5-introduzione.md
+++ dopo/cap03/3.5-introduzione.md
@@ -11,4 +11,4 @@
 ## C3.5 AZIONI DELLA TEMPERATURA
 *Circolare 21/01/2019 n. 7 C.S.LL.PP., §C3.5*
 
-Larga parte di questo Capitolo resta invariato al passaggio dalle precedenti NTC alle attuali. In particolare non vengono modificati né il § 3.5.1 relativo alle generalità, né il § 3.5.3 in cui si definisce la temperatura dell'aria interna, né il § 3.5.4 relativo alla distribuzione della temperatura negli elementi strutturali, né il § 3.5.5 che definisce le azioni termiche sugli edifici, né il § 3.5.6 che fornisce indicazioni relativamente alle precauzioni da adottare per le strutture soggette ad azioni speciali, né infine il § 3.5.7 relativo alle valutazioni degli effetti delle azioni termiche sui materiali strutturali.
+Larga parte di questo Capitolo resta invariato al passaggio dalle precedenti NTC alle attuali. In particolare non vengono modificati né il § 3.5.1 relativo alle generalità, né il § 3.5.3 in cui si definisce la temperatura dell'aria interna, né il § 3.5.4 relativo alla distribuzione della temperatura negli elementi strutturali, né il § 3.5.5 che definisce le azioni termiche sugli edifici, né il § 3.5.6 che fornisce indicazioni relativamente alle precauzioni da adottare per le strutture soggette ad azioni termiche speciali, né infine il § 3.5.7 relativo alle valutazioni degli effetti delle azioni termiche sui materiali strutturali.
```

### `cap03/3.5.2-temperatura-temperatura-dell-aria-esterna.md`
```diff
--- prima/cap03/3.5.2-temperatura-temperatura-dell-aria-esterna.md
+++ dopo/cap03/3.5.2-temperatura-temperatura-dell-aria-esterna.md
@@ -18,7 +18,7 @@
 Per un'opera di nuova realizzazione in fase di costruzione o per le fasi transitorie relative ad interventi sulle costruzioni esistenti, il periodo di ritorno dell'azione potrà essere ridotto come di seguito specificato:
 
 - per fasi di costruzione o fasi transitorie con durata prevista in sede di progetto non superiore a tre mesi, si assumerà $T_R$ ≥ 5 anni;
-- per fasi di costruzione o fasi transitorie con durata prevista in sede di progetto compresa fra tre mesi ed un anno, si assumerà $T_R$ ≥ 10 anni.
+- per fasi di costruzione o fasi transitorie con durata prevista in sede di progetto compresa fra tre mesi d un anno, si assumerà $T_R$ ≥ 10 anni; [1](./annotazioni/3.5.2-anomalie-fonte.md#af-3-5-2-01-d-un-anno-e-punto-e-virgola-finale)
 
 In mancanza di adeguate indagini statistiche basate su dati specifici relativi al sito in esame, $T_{max}$ o $T_{min}$ dovranno essere calcolati in base alle espressioni riportate nel seguito, per le varie zone indicate nella Fig. 3.5.1. Tale zonazione non tiene conto di aspetti specifici e locali che, se necessario, dovranno essere definiti singolarmente.
 
```

### `cap03/3.5.4-temperatura-distribuzione-della-temperatura-negli-elementi-strutturali.md`
```diff
--- prima/cap03/3.5.4-temperatura-distribuzione-della-temperatura-negli-elementi-strutturali.md
+++ dopo/cap03/3.5.4-temperatura-distribuzione-della-temperatura-negli-elementi-strutturali.md
@@ -37,6 +37,6 @@
 |----------|------------------------|:--:|:--:|
 | | | superfici esposte a Nord-Est | superfici esposte a Sud-Ovest od orizzontali |
 | Estate | Superficie riflettente | 0 °C | 18 °C |
-| | Superficie chiara | 2 °C | 30 °C |
-| | Superficie scura | 4 °C | 42 °C |
-| Inverno | | 0 °C | 0 °C |
+| Estate | Superficie chiara | 2 °C | 30 °C |
+| Estate | Superficie scura | 4 °C | 42 °C |
+| Inverno | Inverno | 0 °C | 0 °C |
```

### `cap03/annotazioni/README.md`
```diff
--- prima/cap03/annotazioni/README.md
+++ dopo/cap03/annotazioni/README.md
@@ -36,6 +36,7 @@
 
 | Riferimento | Annotazione | Stato |
 |---|---|---|
+| § 3.5.2 (AF-3.5.2-01) | [Anomalia della fonte conservata](3.5.2-anomalie-fonte.md) | **Da leggere prima di correggere per inferenza la seconda durata transitoria del § 3.5.2**: la fonte stampa `d un anno` e chiude la voce con punto e virgola; il Markdown conserva entrambi. |
 | § 3.4.3 (AF-3.4.3-01/08) | [Anomalie della fonte conservate](3.4.3-anomalie-fonte.md) | **Da leggere prima di correggere formule, riferimenti o concordanze per inferenza**: la fonte lascia senza condizione il secondo ramo della `[C3.4.4]`, alterna `C3.4.x` e `C.3.4.x`, stampa `k ≤ dγ` e `sin` corsivo, e conserva quattro anomalie grammaticali. Il Markdown riproduce tutte e otto le anomalie; nessuna `AF-COR`. |
 | § 3.4.2 (AF-3.4.2-01/09) | [Anomalie della fonte conservate](3.4.2-anomalie-fonte.md) | **Da leggere prima di correggere per inferenza testo, decimali, tag, parentesi, spaziatura, concordanze o pedici del § 3.4.2/C3.4.2**: la fonte stampa `d un anno`, `provincie`, alterna punti e virgola decimali, usa il tag `[C3.4.1]` contro il rinvio `C.3.4.1.`, lascia aperta una parentesi nella definizione di `$P_n$`, giustappone `C3.4.1n`, usa nella Circolare pedici di `$q$` a doppio livello, scrive `immutato sia i valori` e `In esse` dopo il richiamo singolare. Il Markdown conserva tutte e nove le anomalie. |
 | § 3.2.1 (AF-3.2.1-01/03) | [Anomalie della fonte conservate](3.2.1-anomalie-fonte.md) | **Da leggere prima di completare le testate della Tabella C.3.2.II per inferenza**: la fonte lascia vuoti i tre valori dopo `$C_U =$`, stampa `$T_r$` minuscolo nella testata destra e usa `Cu` nella legenda raster; il Markdown conserva le tre anomalie. |
```

### `cap03/annotazioni/3.5.2-anomalie-fonte.md`, nuovo file
```diff
--- prima/cap03/annotazioni/3.5.2-anomalie-fonte.md
+++ dopo/cap03/annotazioni/3.5.2-anomalie-fonte.md
@@ -0,0 +1,29 @@
+---
+title: Anomalie della fonte conservate - § 3.5.2 NTC 2018
+aliases:
+  - Anomalie fonte 3.5.2
+  - AF-3.5.2
+tags:
+  - formazione/normativa
+  - ntc2018
+  - annotazioni
+---
+
+[Torna alle annotazioni del capitolo 3](README.md) | [Torna al § 3.5.2](../3.5.2-temperatura-temperatura-dell-aria-esterna.md#toc-ntc2018-3-5-2-norma)
+
+# Anomalie della fonte conservate - § 3.5.2
+
+L'anomalia qui documentata è riprodotta nel Markdown senza correzioni e appartiene alla classe `AF`. Non sono presenti correzioni `AF-COR` nello scope.
+
+Fonte congelata: `verifica-conformita/fonte-ufficiale/GU-2018-42-SO8-DM-17-01-2018.pdf`, SHA-256 `dda1e397d56d71aa0f5bc457c3ba9b77064a468699dfc37bd056ac6c47105a46`. La pagina citata è fisica.
+
+<a id="af-3-5-2-01-d-un-anno-e-punto-e-virgola-finale"></a>
+## AF-3.5.2-01 - «d un anno» e punto e virgola finale
+
+- Riferimento: NTC 2018, § 3.5.2, pagina fisica 64.
+- Fonte: `compresa fra tre mesi d un anno, si assumerà $T_R$ ≥ 10 anni;`.
+- Tipo: omissione ortografica e punteggiatura anomala della fonte.
+- Prova: lettura diretta del ritaglio a 600 dpi e conferma sul livello caratteri del PDF; un secondo lettore fonte-only in contesto separato ha confermato `d un`, senza `e` né apostrofo, e il punto e virgola finale, senza dubbi.
+- Esito: forma e punteggiatura anomale conservate alla lettera.
+
+**Firma:** Codex / CDX, 2026-09-11.
```

## Verifica di conformità alla lista e all’addendum

- Baseline dei cinque target iniziali: hash e byte tutti corrispondenti prima dell’applicazione.
- Ogni occorrenza `prima` delle sei sostituzioni esistenti era presente una volta prima dell’applicazione.
- Ogni risultato `dopo` è identico al contenuto atteso ricostruito dalla lista, applicata in ordine.
- L’annotazione non esisteva prima dell’operazione 7; il file post-E coincide con il contenuto esatto dell’operazione 7 più la sola àncora dell’addendum.
- Il rinvio `[1]` in § 3.5.2 compare una volta e corrisponde all’ID HTML inserito una volta.
- Asset: hash iniziale corrispondente alla lista, crop post-E verificato pixel per pixel contro il raster e il box prescritti.

Controllo visivo: eseguito con `view_image` sull’asset risultante. Si vede l’intera carta, con Sardegna e Sicilia come due distinti elementi insulari sotto la penisola; non compaiono didascalia né contenuto esterno alla figura.
