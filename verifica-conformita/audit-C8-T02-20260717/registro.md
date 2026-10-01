# Registro di audit — Lotto C8-T02 (Tabelle C.8.5.III e C8.5.IV)

- Cartella: `_tmp_render/cap08/conformita-tabelle-formule-20260717-r01/`
- Protocollo: VC8-G4-TF (skill `controllo-serrato-ntc2018`, `references/protocollo-conformita-tabelle-formule.md`)
- Scope congelato: `verifica-conformita/scope-lotto-c8-t02-2026-07-17.md`
- Fonte: `raw/Circolare-7-2019-NTC.pdf` — SHA-256 `f7c3b8d1f443aadb6b3e020b6b6c19813683492ecaadd2c15bf6bf1939aaed7c` (348 pp.; pagine PDF 266-267 = GU 262-263)
- Markdown pre-audit: `cap08/8-esistenti.md` — SHA-256 `612a2c00fafcd8619786b54a0b2c21df62dd37cf5153771b7cb71c744185b395` (snapshot post-promozione del pilota C8-T01/F01)
- Markdown post-correzioni: SHA-256 `a3ee349b09b0c8f01fe0cb791869440394f092c8e52f434e09647629d30527ac`
- Data: 2026-07-17. Compilatore del registro e riconciliatore: Claude Code (CC), modello Fable 5.

## 1. Metodo

- Congelamento: hash di PDF e MD riscontrati prima dell'audit (`ambiente.txt`); render pagine intere 266-268 a zoom 4 (~288 dpi), ritagli apparato a zoom 6 (~432 dpi), super-zoom a zoom 8-10; text layer estratto come solo ausilio.
- Passaggio A: subagente Claude (Fable 5) a contesto pulito; input limitato ai 7 PNG fonte; output `passaggio-a/A-trascrizione-fonte.md` (matrici complete, 3 micro-dubbi dichiarati).
- Passaggio B: subagente Claude (Opus, modello diverso da A) a contesto pulito, in parallelo e all'oscuro di A; stessi 7 PNG; output `passaggio-b/B-trascrizione-fonte.md` (matrici complete, 2 dubbi dichiarati).
- Riconciliazione: eseguita dal presente agente su A, B e render; divergenze risolte sul render (mai a maggioranza); documento `diff/riconciliazione-A-B.md`.
- Nota di indipendenza: entrambi i passaggi e il riconciliatore sono agenti AI; nessuna revisione umana integrale inclusa nel presente audit.

## 2. Riconciliazione A/B

Concordanza piena su didascalie, architetture, tutte le 30 posizioni logiche della Tab. C.8.5.III e le 18 della Tab. C8.5.IV, note a corredo. Unica divergenza sostanziale: nota (**) della III, "Nota: f_k," (A) contro "Noto f_k," (B, con dubbio dichiarato) — adjudicata sul render `fonte/zoom-adjud-nota2ast-noto-vs-nota.png` a favore di A ("Nota:"), text layer concorde; costruzione anomala della fonte classificata AF. Altre due divergenze puramente terminologiche/indeterminabili (trattini), senza impatto. Fonte concordata = trascrizione A + adjudicazioni.

## 3. Confronto col Markdown e correzioni

Documento: `diff/scarti-md-vs-fonte.md`. Esito:

- **4 famiglie di difformità ERR-MD (E1-E4)**: E1 = nel MD `$\kappa$` dove la fonte stampa `τ` in chiusura della nota (*) della III ("correzione" interpretativa del convertitore, contraria al principio di fedeltà); E2 = virgola aggiunta dopo "C.8.5.I)" nella stessa nota; E3 = punto fermo aggiunto alla didascalia della IV (la fonte termina senza punto); E4 = perdita delle enfasi semantiche nella IV (10 locuzioni in grassetto corsivo "indagini/prove limitate-estese-esaustive" + 3 etichette LC1-LC3 in grassetto).
- **9 normalizzazioni NORM** documentate (riusate le categorie del pilota: didascalie in grassetto, kerning "κsuggeriti", trattini, espansione accorpamenti, math mode, `1{,}25`, allineamenti, spaziatura).
- **5 anomalie della fonte AF** conservate (numerazione "C.8.5.III" puntata vs "C8.5.IV"; "Nota: f_k,"; il refuso `τ` in contesto κ — ripristinato con E1 e segnalato nel registro di revisione; didascalia IV senza punto; attacco "–Valori").
- Correzioni E1-E4 applicate direttamente sul file vivo il 2026-07-17 (righe 521, 531, 535-537). Diff integrale contro lo snapshot pre-audit: **toccate solo le 5 righe attese**; le porzioni certificate dal pilota (Tabelle C8.5.I-II, formule C8.5.4.1-3 e definizioni) risultano invariate nel passaggio allo snapshot `a3ee349b…`.
- Controlli automatici: struttura tabelle valida (12 righe × 4 pipe; 5 righe × 7 pipe); math inline standard compilante.

## 4. Ricontrollo delle correzioni (protocollo §9.9)

- Recheck A (testuale): i 5 frammenti corretti coincidono con la trascrizione A della fonte concordata (5/5).
- Recheck B: i transcript di A e B non erano riattivabili (limite già incontrato nel pilota) → lanciato VERIFICATORE FRESCO a contesto pulito (Opus, soli render): **5/5 CONFERMATO** (1a virgola assente; 1b glifo τ, identico ai τ₀ della colonna Parametro; 2 didascalia senza punto; 3a etichette LC in grassetto; 3b/3c distribuzione esatta delle 10 locuzioni in grassetto corsivo, contorno in tondo).

## 5. Rilievi collaterali FUORI perimetro (aperti, non bloccanti)

- RC1 (md 527): capoverso del §C8.5.4.2 troncato "…ci si può riferire alla Tabella" (manca "C8.5.IV."). Da lotto prosa.
- RC2 (md 529): heading H2 spurio "## C8.5. Definizione del modello di riferimento per le analisi" fuori posto. Da risolvere col rilievo strutturale su CIRC-C8.5.3.2 (heading duplicato md 455/543, prosa spezzata, "muro" md 541).

## 6. Esiti per il registro di dettaglio

- **CIRC-C8.5.4.1** (contiene la Tab. C.8.5.III): l'esito OK del pilota sul perimetro FORMULE resta valido (porzione invariata); la Tabella C.8.5.III del paragrafo è ora anch'essa verificata CONFORME (nota della riga aggiornata; il vocabolario del campo perimetro non ammette valori multipli).
- **CIRC-C8.5.4.2** (contiene la Tab. C8.5.IV): Tabella C8.5.IV CONFORME post-correzioni; esito dell'unità SOSPESO (verifica IN_CORSO) perché la trasposizione del paragrafo resta DA_VERIFICARE per i rilievi strutturali (heading duplicato, RC1-RC2).

## 7. Chiusura

- Perimetro verificato: 100% dello scope congelato — 2 tabelle = 48 posizioni logiche (30 + 18), 9 intestazioni di colonna, 5 accorpamenti, 3 note a corredo, 2 didascalie.
- Correzioni: 4 famiglie ERR-MD applicate e ricontrollate (recheck testuale 5/5 + verificatore fresco 5/5).
- **Criterio di accettazione §12: SUPERATO** per il perimetro dichiarato. Conformità documentale delle Tabelle C.8.5.III e C8.5.IV della Circolare C8 rispetto al PDF identificato nel manifest, verificata sul 100% degli apparati con due passaggi indipendenti. Restano esclusi dal perimetro il testo in prosa (rilievi RC1-RC2 aperti fuori scope) e gli altri apparati del capitolo. Doppio controllo indipendente eseguito da agenti AI; nessuna revisione umana integrale inclusa nel presente audit.
- Lotti successivi proposti: C8-F02 (~10 formule esposte C8), lotto fedeltà prosa (righe md 407-422 + RC1-RC2 + struttura C8.5.3.2/C8.5.4.2), poi Tabelle C8.5.V-VI e C8.7.6.3.I-II, quindi Capitolo 7 (mismatch noto formula 7.9.4).

Firma: audit eseguito e chiuso da Claude Code (CC), modello Fable 5, con subagenti Claude (Fable 5, Opus) nei ruoli A/B/recheck, 2026-07-17.
