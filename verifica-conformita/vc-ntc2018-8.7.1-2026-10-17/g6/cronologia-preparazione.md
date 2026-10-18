# Cronologia della preparazione G6

Firma: CDX  
Scope: 8.7.1  
Data: 2026-10-17

## Primo tentativo, respinto prima della rivelazione

La configurazione `config-g6.json`, sha256 `24559dcc1f249ebe96bbf9447dd094f49bdd287810267b2506979df9159269a8`, è stata preparata in una destinazione temporanea esterna al workspace. Tre V indipendenti hanno lavorato soltanto sulle fonti. Nessuno ha cercato o letto il target.

- b01: inventario fonte-prima valido, 55 elementi, 7 esclusioni, zero dubbi, sha256 `50bde0633444ca55754cb8a6b03e9a0195e24080fb9a6cf383826d9fe6488986`.
- b02: inventario fonte-prima, 29 elementi e 6 esclusioni, sha256 `58fa7338ec17f13c0ca8d20d7af31ac7802af2eedbfbdd2ce3cad9a5eef8e384`.
- b03: inventario fonte-prima, 60 elementi e 5 esclusioni, sha256 `13fa4277c955952563abd8fa3ba9ae1a258a4a2799b4807d19297ac95c67ff99`. Il V ha rilevato che il limite iniziale dichiarato, «Si fa inoltre presente», non era presente nelle pagine consegnate e che la prima pagina iniziava con la continuazione «dove:».
- b04 non era ancora stato avviato.

Il controllo ha dimostrato che la pagina fisica 274 era stata assegnata a b02 mentre le righe corrispondenti erano state assegnate a b03. Il tentativo è quindi classificato come errore tecnico di mappatura del pacchetto, non come rilievo sul target. Non si è proceduto a `rivela`; `giro_g6` è rimasto 0.

## Seconda preparazione

La configurazione corretta è `config-g6-v2.json`, sha256 `c1f1a20833d5b62592146c96cfc8bee3e1fdf120a1b5ed30b20f3f1264d5e238`. La mappa G5 aggiornata ha sha256 `47f4a1fe4b9d89934fb3dced934170a1e3f5a38414d234d73415fae82a4798eb`.

- b01: NTC 297-298 e Circolare 270-271, righe 1-109. Gli input sono byte-identici al primo tentativo; l'inventario validato è riusato senza nuova lettura.
- b02: Circolare 272-273, righe 110-219.
- b03: Circolare 274-278, righe 220-455.
- b04: Circolare 279-283, righe 456-662.

Ogni pagina e ogni riga depurata è assegnata una volta sola. b02 comprende due pagine, sotto la fascia consigliata di 3-5, perché i confini alternativi avrebbero separato una formula dalle sue definizioni oppure una sequenza normativa continua. I tre blocchi modificati sono affidati a V in nuovi contesti fonte-prima.
