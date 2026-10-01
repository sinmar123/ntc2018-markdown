# Istruzioni G7 R03

Riprendere lo stesso contesto V `20260909_165403_00ba4e` e leggere solo `/blocco/g7`.

Usare `manifest-rilascio-r03.json`. Verificare il solo delta append-only:

- il valore corretto dell'impronta del manifest R01 è `04db73b18947bd364331d32afa58f1008179acd181c906975106b6b643132f74`;
- `errata-PROCEDURA-VC-r03.json` chiarisce il richiamo interno `/2` rimasto nella procedura congelata R3, senza modificarne criteri o revisione.
- Target, fonti, asset e G6 devono risultare invariati.

I giudizi G7 R01 e R02 restano storici e non vanno modificati. Scrivere soltanto `/blocco/giudizio-g7.json`. Se positivo, usare lo schema prescritto con `giudizio_g7: "OK"`, manifest R03, G0-G7 tutti `OK` e `rilievi_aperti: []`. Altrimenti indicare rilievi puntuali. Fermarsi dopo G7.
