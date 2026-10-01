# Istruzioni G7 R02

Riprendere il medesimo contesto V `20260909_165403_00ba4e`. Leggere esclusivamente `/blocco/g7`.

Il G7 R01 è conservato come esito negativo e non va modificato. Verificare il solo recupero documentale descritto in `rettifica-evidenze-g7-r01.json` e `chiusura-c-r02.md`, usando come manifest corrente `manifest-rilascio-r02.json`.

Accertare:

- presenza della copia congelata VC-NTC/3 e assenza della copia VC-NTC/2 dai record del manifest R02;
- correttezza del confine `C3.5`;
- correttezza delle normalizzazioni 2 e 1 indicate nella rettifica;
- integrità della catena R02 e permanenza degli invarianti di target, fonti, asset e G6;
- chiusura o persistenza dei tre rilievi G7 R01 e assenza di altri rilievi.

Scrivere `/blocco/giudizio-g7.json`. Se il giudizio è positivo, usare i campi prescritti dalla specifica: `firma`, `giudizio_g7: "OK"`, `scope: "3.4.5"`, `snapshot_sha256`, `manifest_sha256`, `gate` con G0-G7 tutti `OK`, `rilievi_aperti: []`; aggiungere una motivazione breve e l'isolamento. Se non è positivo, indicare rilievi puntuali. Non modificare altre evidenze e fermarsi dopo G7.
