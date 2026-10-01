# Adjudicazione C del G6 R01 - VC NTC 2018 § 3.5

**Data:** 2026-09-11  
**Ruolo:** C, `gpt-5.6-sol`, provider `openai-codex`, ragionamento `high`  
**Rapporto V:** `C:/Users/sandro/AppData/Local/Temp/vc-35-cdx-20260911-r01/b01/rapporto-g6.json`, SHA-256 `f8c6db33679525b33534a8b167d8667d1fae7c13909ba4dff1e9c1686eb967d0`  
**Esito V:** `KO`, 74/74 ID coperti, sei `ERR-MD`, zero dubbi.

## Decisioni

1. **NTC-64-COND-3.5.2-02 - accolto come `ERR-MD`; fonte `A/AF`.** La p. fisica 64 stampa letteralmente `compresa fra tre mesi d un anno` e chiude la voce con `;`. Il target aggiunge `e` e usa `.`. L'anomalia ortografica e la punteggiatura della fonte vanno conservate; l'AF sarà documentata in `cap03/annotazioni/3.5.2-anomalie-fonte.md` e richiamata con link relativo dal punto interessato.
2. **NTC-64-FIG-3.5.1 - accolto come `ERR-MD`.** La figura è un raster distribuito in cinque bande JPEG native contigue, xref 1091-1095, bbox complessivo PDF `(226.977, 257.164)-(369.843, 437.110)`. L'asset corrente deriva dal crop a 600 dpi `[1720,2020,3240,3600]`, il cui fondo corrisponde a 432 pt e tronca il secondo elemento insulare sotto la Sicilia. Il crop `[1720,2020,3240,3680]` include l'intero bbox con margine inferiore di circa 4,5 pt e resta prima della didascalia: va rigenerato senza ridimensionamento.
3. **NTC-65-TAB-3.5.I-EST-CHIARA - accolto come `ERR-MD`.** La cella `Estate` è accorpata sulle tre righe; la normalizzazione 6 impone di ripeterla nella prima cella della riga `Superficie chiara`.
4. **NTC-65-TAB-3.5.I-EST-SCURA - accolto come `ERR-MD`.** Per la stessa normalizzazione, `Estate` va ripetuto nella prima cella della riga `Superficie scura`.
5. **NTC-65-TAB-3.5.I-INV - accolto come `ERR-MD`.** La cella `Inverno` copre le prime due colonne del corpo; la normalizzazione 6 impone `Inverno` in entrambe le celle logiche.
6. **CIRC-81-P-C3.5-01 - accolto come `ERR-MD`.** La p. fisica 81 stampa `strutture soggette ad azioni termiche speciali`; il target omette `termiche`.

## Prove critiche e precedente adjudicazione

Per il primo rilievo il ritaglio `fonte-extra01/ntc-p64-dettaglio-01-600dpi.png` mostra senza ambiguità `d un anno` e `anni;`; il livello caratteri conferma `U+0020 U+0064 U+0020 U+0075 U+006E U+0020` e `U+003B`. La Fig. 3.5.1 è localizzata a 600 dpi e il raster nativo xref 1095 conserva entrambi gli elementi insulari inferiori; i codepoint non sono applicabili.

La voce R7 di `cap03/cap03-azioni-sulle-costruzioni-revisione.md`, risalente al 2026-05-20, costituiva una precedente adjudicazione specifica secondo cui la fonte avrebbe confermato `ed un anno`. Per il suo ribaltamento è stato applicato il § 4: oltre al ritaglio a 600 dpi e ai caratteri vettoriali, un secondo lettore Astra xhigh nel contesto fonte-only `/root/c35_sol/lettore_fonte_35` ha letto soltanto il ritaglio e `dati-vettoriali.json`, con domanda aperta. Ha confermato ` d un `, senza `e` né apostrofo, e `;` dopo `anni`, senza dubbi; i caratteri pertinenti risultano non sintetici. Le prove concordano. Il riscontro Astra xhigh del coordinatore sulla fonte concorda inoltre con questa lettura. Non occorre un ulteriore verificatore.

## Esito

Tutti i sei rilievi sono fondati. La lista autoritativa unica è `lista-correzioni-g6-r01.json`: cinque sostituzioni testuali, un asset da rigenerare, un'annotazione AF da creare e una riga da aggiungere all'indice delle annotazioni. Nessuna correzione è applicata da C. Dopo E servono diff contro la lista, nuovo snapshot, render e preflight, quindi un nuovo G6 integrale secondo § 8. Il G6 R01 resta `KO`, giro 1/3.

**Firma:** Codex / CDX, ruolo C Sol high; supporto puntuale Astra xhigh come sopra dichiarato.

