# Istruzioni G7 R06, manifest finale R02

Riprendere lo stesso contesto V `20260909_165403_00ba4e` e leggere solo `/blocco/g7`.

Giudicare `manifest-rilascio-finale-r02.json`, con impronta esterna in `impronta-manifest-finale-r02.json`. Il delta append-only aggiunge il percorso `cap03/3.4.5-neve-coefficiente-termico.md`, copia del target vivo con lo stesso SHA-256 già giudicato, e conserva manifest e giudizio R05 sotto il dossier portabile.

Verificare il solo delta e che tutti i rilievi restino chiusi. Non rifare G6, inventario, render o confronto. Se positivo, scrivere `/blocco/giudizio-g7.json` con `manifest_sha256` uguale all'impronta del manifest finale R02.
