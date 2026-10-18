# Consegna al verificatore: controllo delle modifiche, scope § 8.7.1 / C8.7.1

Sei il verificatore indipendente (V) del controllo delle modifiche previsto dal § 8 della procedura VC-NTC/9. Non hai scritto le correzioni e non coordini lo scope. Lavora soltanto sui file di questa cartella: non aprire altre cartelle, il workspace, il repository o internet. Non modificare né creare file: la tua risposta finale è il rapporto JSON descritto in fondo, e nient'altro.

La fonte è la pagina stampata della Circolare 21/01/2019 n. 7 (Gazzetta Ufficiale). Le immagini `fonte-circ-*.png` sono le pagine fisiche a 200 dpi; per la p. 281, che nella fonte è un'immagine raster, ci sono anche il raster nativo e un ritaglio a 600 dpi. `fonte-circ-278-righe-vettoriali.json` contiene le posizioni delle righe di testo della p. 278 lette dalla codifica del PDF. I criteri sono in `canone.md` (§§ 3-4 della procedura e catalogo delle normalizzazioni, voci 1-24) e nella voce 25 qui sotto.

**Voce 25 del catalogo, aggiunta il 2026-10-18 per decisione di Sandro.** Note a piè di pagina. Il richiamo di nota che la fonte stampa in apice nel testo corrente si scrive come nota a piè di pagina Markdown `[^n]`, con lo stesso numero della fonte; il testo della nota si scrive come definizione `[^n]: …` subito dopo il capoverso che contiene il richiamo, senza la parola «Nota» e senza altre parole, con le enfasi della fonte. Nel PDF prodotto dal renderer canonico il richiamo esce in apice con il numero della fonte e la nota a piè di pagina.

**Convenzione del corpus per le rubriche.** Le rubriche di sesto livello della Circolare che la fonte stampa in grassetto corsivo si scrivono `###### *testo*`. Il renderer canonico rende il livello 6 come testo corsivo non grassetto: per questo livello la forma da controllare è quella del Markdown.

## Che cosa è cambiato

Dopo il confronto integrale sono state applicate da script le quattro voci di `lista-correzioni.json`, tutte nel blocco b04. `b04-testo-prima.md` è il testo depurato del blocco b04 consegnato al confronto integrale, `b04-testo-dopo.md` quello attuale e `b04-diff.txt` il diff completo. Per i blocchi b01, b02 e b03 lo script che ha ricomposto i blocchi riporta un diff vuoto; `b01-testo-dopo.md` e `b03-testo-dopo.md` servono come contesto. Il renderer canonico ora compone le rubriche di livello 4 e 5 su riga propria: `resa-dopo.pdf` è la nuova resa completa del testo depurato e `resa-dopo-pNN.png` le pagine interessate.

Impronte SHA-256 del file Markdown dello scope: prima 09eab0335ca26594b29ea19f279acf1da8496550f70883b55fa6695a4b0ba6c8, dopo 5c466acd11ce6c074f28ba1b022d78fff5930d5829f378701493ac52b98ad57c.

## Che cosa controllare

1. **Diff.** `b04-diff.txt` deve contenere soltanto le quattro voci della lista, nel punto indicato, e nient'altro.
2. **Rilievi sul testo.** Per B04-C279-HD-01, B04-C281-HD-01, B04-C281-PR-07 e B04-C281-NT-01 (testo in `rilievi-g6.json`) controlla sulla fonte se il testo dopo è conforme, compresi rubriche, enfasi, richiamo e testo della nota con le sue enfasi.
3. **Rilievi sulla resa.** Per C-RUB-002, C-RUB-003, C-RUB-004, B03-E044, B04-C281-HD-02, B04-C282-HD-01 e B04-C283-HD-01 controlla nella nuova resa se rubrica e capoverso seguente sono su righe distinte, come nella fonte.
4. **Domande aperte sulla p. fisica 278.** Rispondi guardando soltanto la fonte (immagine e posizioni vettoriali), poi confronta la tua risposta con `b03-testo-dopo.md`:
   - Q1: il testo che comincia con «Nelle scelte di modellazione occorre considerare» apre un capoverso nuovo o continua il capoverso precedente?
   - Q2: il testo che comincia con «Nel caso di diaframmi di rigidezza finita» apre un capoverso nuovo o continua il capoverso precedente?
5. **Effetti.** Controlla nella resa le pagine con la nota 4 e con le rubriche corrette, e nel testo dopo il contesto delle modifiche: nessun effetto indesiderato.

Classifica ogni difformità come `ERR-MD`, `ERR-AUDIT` o `DUBBIO` secondo il canone. Se una lettura della fonte non è univoca, scrivi `DUBBIO`: non ricostruire ciò che la fonte non permette di leggere.

## Rapporto

Rispondi soltanto con un oggetto JSON valido, senza testo prima o dopo e senza blocchi di codice, con questi campi:

- `firma`: chi sei (modello e ruolo);
- `controllo`: "modifiche § 8, scope 8.7.1";
- `snapshot_prima_sha256`, `snapshot_dopo_sha256`: le impronte indicate sopra;
- `diff`: oggetto con `esito` ("OK" o "KO") e `note`;
- `rilievi`: elenco di oggetti `id`, `esito` ("CHIUSO" o "APERTO"), `prova` (pagina, file e che cosa hai visto, in breve);
- `domande_aperte`: elenco di oggetti `id` ("Q1", "Q2"), `lettura_fonte` ("NUOVO_CAPOVERSO", "STESSO_CAPOVERSO" o "DUBBIO"), `prova`, `markdown` ("CONFORME" o "DIFFORME");
- `resa`: oggetto con `pagine_osservate` ed `esito`;
- `nuovi_rilievi`: elenco, anche vuoto, di oggetti `id`, `classe`, `pagina`, `prova`;
- `esito`: "OK" soltanto se il diff è OK, tutti i rilievi sono CHIUSO, le domande hanno markdown CONFORME e non ci sono nuovi rilievi; altrimenti "KO";
- `letture`: elenco dei file che hai letto;
- `limiti`: limiti del controllo, in una o due frasi.
