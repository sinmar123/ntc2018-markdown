# Adjudicazione C delle evidenze G6 R02 - § 3.5

**Data:** 2026-09-11  
**Oggetto:** delta documentale di `prove_raster` e metadati V  
**Rapporto V originario:** SHA-256 `63575bddbd7f861e0abbe935c2940cb36a16b2d0afad3e956a5264180268124d`  
**Rettifica append-only:** SHA-256 `987715c7da07c00775378db40d3e4fe1d33d7707c0b04a07f5b9edd26c097399`

## Decisione

La rettifica è accolta. Corregge esclusivamente la descrizione delle prove e dei metadati, senza modificare input, target, inventario, copertura o rapporto originario.

Per Fig. 3.5.1 le dimensioni 1520 × 1660 px appartengono all'asset target derivato dal render della pagina a 600 dpi e dal successivo crop senza ridimensionamento; non sono dimensioni native della fonte. La fonte contiene cinque JPEG originali consecutivi, xref 1091-1095, ciascuno di 697 × 176 px, che compongono una figura nativa di 697 × 880 px. Originali e localizzazione a 600 dpi confermano integralmente figura, campiture, confini, isole, etichette e completezza del margine inferiore. La diversa natura dell'asset target era già descritta nell'adjudicazione G6 R01 e non incide sulla conformità.

Per Fig. 3.5.2 l'asset target 588 × 380 px coincide byte per byte con il PNG incorporato originale xref 1105, SHA-256 `42d8357bab9e67729e98dfc4ca9de4e360a865b0f583d47a9d0d61e386c85b02`. La rettifica distingue correttamente i dpi di metadato dai dpi effettivi ricavati dalla bbox PDF.

La sessione effettiva è `01a0910c-8056-7bb0-ae6b-aecc452a0c0a`; il prefisso `id` nel rapporto originario è una qualificazione documentale inesatta. Il valore `2026-09-11T15:22:38.2230622Z` è una misura dell'orologio precedente alla lettura; il primo accesso effettivo al target è `2026-09-11T15:22:49.255Z`. Entrambi seguono il congelamento delle `2026-09-11T15:22:04.856533Z`, quindi isolamento e ordine temporale restano validi.

Il confronto integrale resta attestato su 36/36 unità, con zero rilievi. **G6 R02 è chiuso con esito OK sul medesimo snapshot G5, contatore 2/3.** Non occorre ripetere G6 per questa sola rettifica delle evidenze.

**Firma:** Codex / CDX, ruolo C Sol high.
