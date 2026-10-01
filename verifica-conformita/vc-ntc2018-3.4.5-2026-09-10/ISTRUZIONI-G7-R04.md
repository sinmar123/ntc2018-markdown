# Istruzioni G7 R04

Riprendere lo stesso contesto V `20260909_165403_00ba4e` e leggere solo `/blocco/g7`.

Non esiste un nuovo manifest: usare `manifest-rilascio-r03.json`, rimasto immutato. Verificare il solo delta esterno `impronta-manifest-r03.json`, necessario a chiudere senza autoreferenza la catena del manifest R03.

Il giudizio R03 negativo è conservato in `g7-r03/giudizio-g7-ko.json`. Non rifare G6, inventario, render o confronto. Se il delta chiude l'ultimo rilievo e non ne emergono altri, scrivere il giudizio positivo canonico in `/blocco/giudizio-g7.json`.
