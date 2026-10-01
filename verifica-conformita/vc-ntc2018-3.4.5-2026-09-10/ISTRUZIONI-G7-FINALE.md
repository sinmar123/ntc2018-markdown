# Istruzioni G7 R05, manifest finale portabile

Riprendere lo stesso contesto V `20260909_165403_00ba4e` e leggere solo `/blocco/g7`.

Giudicare `manifest-rilascio-finale.json`, con impronta esterna in `impronta-manifest-finale.json`. Il manifest elenca 62 copie sotto `verifica-conformita/vc-ntc2018-3.4.5-2026-09-10/`; sono la ricollocazione portabile delle evidenze già verificate, inclusa la chiusura R04.

Verificare che la ricollocazione non introduca modifiche agli invarianti e che tutti i rilievi restino chiusi. Non rifare G6, inventario, render o confronto. Se positivo, scrivere il giudizio canonico in `/blocco/giudizio-g7.json` con `manifest_sha256` uguale all'impronta esterna del manifest finale.
