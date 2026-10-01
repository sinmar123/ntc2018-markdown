# Rettifica append-only del manifest finale

Firma: Hermes NTC-VC / HRM. Data: 2026-09-10.

Il dry-run di `vc-supporto.py registra` ha rifiutato il manifest R01 perché elencava la copia congelata del target ma non il percorso vivo `cap03/3.4.5-neve-coefficiente-termico.md` richiesto dalla precondizione di rilascio. Il target vivo ha lo stesso SHA-256 giudicato, `3541307932ff82abd016c34b325b6bb11877315ae8cc1db320b57d925cb7ebd5`.

La rettifica aggiunge quel percorso e conserva manifest e giudizio R05. Non modifica target, fonti, asset, G6 o evidenze già manifestate.
