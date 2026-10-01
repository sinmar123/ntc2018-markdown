# Verifica append-only della rettifica G6 R03

Questa consegna interviene dopo il rapporto G6 R03 e non sostituisce la consegna originaria.

Leggere soltanto i file della cartella `/blocco`. Non aprire percorsi esterni. Riprendere il medesimo contesto V del G6 R03.

1. Non modificare né sovrascrivere `inventario.json`, `congelamento.json`, `input-confronto.json` o `rapporto-g6.json`.
2. Leggere `rettifica-inventario-001.json` e verificarne il solo delta per `CIRC81-PRO-001` contro `fonte-circ-81.png`, `testo.md`, `resa-target/render-3.4.5.pdf` e `resa-target/render-3.4.5-200dpi.png`.
3. Accertare se gli estremi rettificati delimitano il primo capoverso effettivamente confrontato nel G6 R03 e se fonti, target, asset e manifest verificati sono rimasti invariati.
4. Scrivere esclusivamente il nuovo file `esito-rettifica-g6-001.json`, senza riscrivere il rapporto originario, con i campi:
   - `firma`;
   - `esito`: `OK` oppure `KO`;
   - `rettifica`: `rettifica-inventario-001.json`;
   - `id`: `CIRC81-PRO-001`;
   - `verifica`: motivazione puntuale;
   - `letture`: soli percorsi effettivamente letti;
   - `isolamento`;
   - `rilievo_originario`: `CHIUSO` oppure `APERTO`;
   - `esito_g6_post_rettifica`: `OK` soltanto se la rettifica è corretta, il rilievo è chiuso e non emergono altri rilievi, altrimenti `KO`.
5. Fermarsi dopo questo file. Non avviare G7.

La verifica è limitata al delta documentale. Non costituisce un nuovo giro G6 integrale e non autorizza correzioni del corpus.
