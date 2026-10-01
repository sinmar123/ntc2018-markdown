# Registro di audit — Pilota C8, lotti C8-T01 (Tabelle C8.5.I-II) e C8-F01 (Formule C8.5.4.1-3)

- Cartella: `_tmp_render/cap08/conformita-tabelle-formule-20260716-r01/`
- Protocollo: VC8-G4-TF (skill `controllo-serrato-ntc2018`, `references/protocollo-conformita-tabelle-formule.md`)
- Scope congelato: `verifica-conformita/scope-pilota-c8-2026-07-16.md`
- Manifest fonti: `verifica-conformita/manifest-fonti-2026-07-16.txt`
- Fonte: `raw/Circolare-7-2019-NTC.pdf` — SHA-256 `f7c3b8d1f443aadb6b3e020b6b6c19813683492ecaadd2c15bf6bf1939aaed7c` (348 pp.; pagine PDF 261, 262, 266 = GU 257, 258, 262)
- Markdown pre-audit: `cap08/8-esistenti.md` — SHA-256 `9d2334c028ef25c483246216033da432d8064127c4dc38f4ea30eea10b2ef9c0`
- Data: 2026-07-16. Compilatore del registro e riconciliatore: Claude Code (CC), modello Fable 5.

## 1. Stato trovato al ripristino della sessione (audit interrotto e ripreso)

L'audit era stato avviato da un agente CC (Fable 5) poi interrotto. Alla ripresa (sera del 2026-07-16) risultavano GIÀ prodotti:

- congelamento completo: scope, manifest fonti con hash, `ambiente.txt`, `manifest.csv` (7 unità, colonne esito vuote);
- `fonte/`: render pagine intere 261, 262, 263, 266, 267 (zoom 4 ≈288 dpi) + estrazioni text layer, ritagli apparati a ≈432 dpi (tab C8.5.I, tab C8.5.II, formule, definizioni, nota 3, contesto C.8.5.III) e super-zoom mirati;
- `passaggio-a/`: trascrizione A completa (`A-trascrizione-fonte.md`) con supporti `font-forensics.txt` e `parole-tabelle-posizioni.txt` — copre il 100% dello scope;
- `markdown/`: snapshot integrale pre-correzioni (SHA-256 riverificato alla ripresa: COINCIDE col manifest) ed estratto numerato dei blocchi in scope;
- `tavole/`: render delle formule Markdown (`render-md-formule-C8.5.4.png`);
- `passaggio-b/`: SOLO 15 ritagli `b-*.png` di un run B avviato e interrotto, SENZA trascrizione;
- `diff/`: vuota; `registro.md`: assente.

### 1.1 ANOMALIA GRAVE DI AMBIENTE (non risolubile in audit)

Alla ripresa, la cartella di progetto `normativa/ntc2018--norme-costruzioni/` risulta contenere SOLTANTO `verifica-conformita/` e `_tmp_render/`. Sono assenti dal filesystem (verificato con ricerca estesa su tutto `C:\Users\sandro`, incluso `ag_oc\workspace-old`):

- `raw/` (entrambi i PDF sorgente, inclusa la Circolare);
- `cap08/` (incluso il Markdown vivo `8-esistenti.md`);
- `registro-dettaglio-verifica-ntc2018.csv`;
- `strumenti/` (incluso `lint-registro-dettaglio.py`);
- `README.md`, `TODO.md`, `CHANGELOG.md`, `AGENTS.md` di cartella.

Conseguenze sul mandato:

- l'audit A/B e la riconciliazione sono stati completati sui materiali CONGELATI (render fonte prodotti dal PDF hashato prima della sparizione + snapshot Markdown con SHA-256 riverificato identico al manifest): la catena di custodia regge;
- le correzioni NON sono applicabili al file vivo (assente): sono consegnate come blocchi corretti pronti in `diff/` (vedi §6) da promuovere al ripristino del progetto;
- aggiornamento righe `CIRC-C8.5.3.1` e `CIRC-C8.5.4.1` del registro di dettaglio, lint e `TODO.md`: BLOCCATI (file assenti); gli esiti unità da riportare sono in §7.

## 2. Metodo alla ripresa

- Passaggio A: riusato integralmente (completo e conforme allo scope; nessuna rigenerazione di render: le pagine 261, 262, 266 erano già coperte).
- Passaggio B: rilanciato da zero come subagente a contesto pulito (modello Opus), input limitato ai SOLI 9 PNG render fonte (3 pagine intere + 6 ritagli apparato); vietati esplicitamente Markdown, passaggio A, text layer e web; output in `passaggio-b/B-trascrizione-fonte.md`.
- Quarantena: i 15 ritagli `b-*.png` del run B interrotto sono stati spostati in `passaggio-b/_prerun-quarantena/` PRIMA del lancio del nuovo B, perché i nomi file (es. riferimenti a punti specifici degli apparati) avrebbero indirizzato l'attenzione del nuovo verificatore, violando l'indipendenza. Nessun file cancellato.
- Riconciliazione: eseguita dal presente agente (CC, Fable 5) su A, B e render fonte; ogni divergenza risolta guardando il render (mai a maggioranza), quindi confronto del concordato con lo snapshot Markdown.
- Nota di indipendenza: A = CC/Fable 5 (sessione precedente, interrotta); B = subagente Opus a contesto pulito; riconciliatore = CC/Fable 5 (sessione nuova). Entrambi i passaggi sono svolti da agenti AI: nessuna revisione umana integrale inclusa nel presente audit.

## 3. Adjudicazioni puntuali del riconciliatore (verifiche dirette sui render, pre-B)

Verifiche svolte in proprio dal riconciliatore sui ritagli fonte, a corroborazione di A:

1. Tab C8.5.I, legenda: le DUE parentetiche identiche "(con riferimento alla formula riportata, a proposito dei modelli di capacità, nel §C8.7.1.3)" sono entrambe presenti (per τ0 e per fv0). Peculiarità della fonte, confermata.
2. Tab C8.5.I, celle fv0 righe 1-4: doppio trattino sovrapposto in verticale = artificio tipografico della fonte; valore logico unico "-". Confermato su `zoom-p261-fv0-trattini.png`.
3. Tab C8.5.I, intestazione fv0: a forte ingrandimento il pedice appare "V0" (sembra V maiuscola). DUBBIO aperto e CHIUSO così: il text layer della pagina codifica `fv0` minuscolo sia in legenda sia nella cella di intestazione (`fonte/pagina-261-text.txt` righe 12 e 20) e la legenda stampa chiaramente "fv0" minuscolo; l'apparenza da maiuscola è resa del grassetto corsivo a corpo pedice. Esito: intestazione = f_v0 minuscolo; A corretta; MD `$f_{v0}$` conforme. Evidenza: `fonte/zoom-adjud-header-simboli-c85I.png`, `fonte/zoom-adjud-legenda-fv0-b.png`.
4. Tab C8.5.I, colonna w righe 4-5: cella unica accorpata "13 ÷ 16(**)" (senza spazio prima del richiamo), confermata.
5. Tab C8.5.I riga 8 e Tab C8.5.II riga 8: "(es,: doppio UNI foratura ≤40%)" con VIRGOLA dopo "es" in entrambe le tabelle (refuso della fonte da conservare). Confermato su crop 432 dpi.
6. Tab C8.5.I righe 4-5 e Tab C8.5.II righe 4-5: "ecc.,)" con virgola dopo il punto in TUTTE e quattro le occorrenze (refuso della fonte da conservare).
7. Tab C8.5.I nota (*): "i contatti e aumentano" (con "e", non "ed"). Confermato.
8. Tab C8.5.II, fasce di intestazione: "Stato di fatto" copre le colonne dati 1-3; "Interventi di consolidamento" copre le colonne dati 4-7 COMPRESA "Massimo coefficiente complessivo" (nessun bordo verticale nella fascia sopra l'ultima colonna). Confermato su `zoom-p262-header-gruppi.png`.
9. Tab C8.5.II nota (***): esponente stampato "0.35" con PUNTO decimale, in corsivo apice (incoerenza tipografica della fonte, altrove virgola). Confermato su `zoom-p262-esponente-035.png`.
10. Tab C8.5.II intestazione: "Intonacoarmato" stampato attaccato anche nel text layer (`fonte/pagina-262-text.txt` riga 31): artefatto della fonte; lettura logica "Intonaco armato (**)".
11. Formule: [C8.5.4.1] μ′=½(X_min+X_max); [C8.5.4.2] σ′=½(X_max−X_min); [C8.5.4.3] μ″=(nX̄+κμ′)/(n+κ); tag tra parentesi quadre, un solo punto per livello. Confermate a vista sul crop 432 dpi; confronto visivo col render del Markdown (`tavole/render-md-formule-C8.5.4.png`): struttura, simboli, ordine dei pedici, primi e tag COINCIDONO per tutte e tre.
12. Prosa in scope (LC3, ponte, "dove...", "Nel determinare...", "Qualora...", nota 3): confermati sui render "μ′ e σ′" (sigma, non V), "X̄", "κ" tre occorrenze nel capoverso definizioni, "σ′2" (2 in apice), richiamo di nota "sperimentali3" in apice, refuso della fonte "C8..5.4.3" (due punti consecutivi), "tabella C.8.5.I" minuscola con punto anomalo, kerning di stampa "κper" nella nota 3 e "fpuò" nella nota (**) di C8.5.I.

## 4. Passaggio B (eseguito alla ripresa)

- Verificatore B: subagente Claude a contesto pulito, modello Opus, 2026-07-16 sera.
- Input: SOLO i 9 PNG render fonte (pagine intere 261, 262, 266 + 6 ritagli apparato in `fonte/`). Vietati e non aperti: `passaggio-a/`, `markdown/`, `diff/`, `tavole/`, i text layer `*-text.txt`, gli zoom di A, la quarantena.
- Output: `passaggio-b/B-trascrizione-fonte.md` (trascrizione integrale: 48+56 celle dati, 16 etichette, 2 intestazioni con architettura fasce, 7 note, 3 formule in LaTeX, prosa in scope verbatim, 17 osservazioni tipografiche) + 18 ritagli di lavoro `b-t1-*/b-t2-*/b-c-*.png`.
- Punti illeggibili dichiarati da B: nessuno. Violazioni dei divieti dichiarate: nessuna.

## 5. Riconciliazione A/B

Documento: `diff/riconciliazione-A-B.md`. Sintesi: piena concordanza su tutte le 104 celle dati, le etichette, le note, le 3 formule e la prosa in scope; 3 divergenze micro (D1 pedice intestazione fv0; D2 attacco `³Dalla`; D3 `κsuggeriti`), tutte risolte sul render della fonte (D1 anche col text layer). Fonte concordata = trascrizione A + adjudicazioni D1-D3.

## 6. Confronto col Markdown e correzioni

Documento: `diff/scarti-md-vs-fonte.md`. Esito:

- **14 difformità ERR-MD** (E1-E14): 3 su Tab C8.5.I (legenda privata delle due parentetiche §C8.7.1.3; `es.:` in luogo di `es,:`; `ed` in luogo di `e`), 5 su Tab C8.5.II (fasce di intestazione assenti; `ecc.)` ×2; `es.:`; esponente `0{,}35` in luogo di `0.35`), 6 sul blocco formule (V→σ′; `{`→X̄ ×2; κ omessa ×2; V'2→σ′²). Le formule [C8.5.4.1-3] in sé sono risultate CONFORMI.
- **Normalizzazioni NORM** documentate (9 categorie) e **anomalie della fonte AF** conservate (9 voci): elencate nel documento scarti.
- Correzioni: il file vivo `cap08/8-esistenti.md` è ASSENTE (v. §1.1), quindi le 14 correzioni sono state applicate alla copia integrale `diff/8-esistenti-POST-correzioni-proposto.md`, generata dallo snapshot congelato con sostituzioni verificate una a una (script `diff/_build-dettagli-e-copia.py`, ogni sostituzione con conteggio di occorrenze atteso = 1).
- **SHA-256 della copia corretta: `612a2c00fafcd8619786b54a0b2c21df62dd37cf5153771b7cb71c744185b395`** (il manifest pre-audit resta immutato; questo è l'hash del testo che il file vivo dovrà avere dopo la promozione). Un'occorrenza residua di `0{,}35` a riga 994 appartiene a una formula di altro paragrafo, FUORI dal perimetro congelato: non toccata.
- Ricontrollo delle correzioni (protocollo §9.9): recheck A = i frammenti corretti coincidono testualmente con la trascrizione A; recheck B = il transcript del subagente B non era più riattivabile, quindi è stato lanciato un VERIFICATORE FRESCO a contesto pulito (Opus, soli render, con facoltà di zoom): 14 conferme su 14 (evidenze `passaggio-b/b-rc-01..14*.png`, 18 ritagli). Registrato nel `manifest.csv` (colonne esito compilate per tutte le 7 unità di audit).

## 7. Esiti per le unità del registro di dettaglio (da riportare nel CSV al ripristino)

Il file `registro-dettaglio-verifica-ntc2018.csv` e lo strumento `strumenti/lint-registro-dettaglio.py` sono assenti dal filesystem: aggiornamento e lint NON eseguibili in questa sessione. Contenuto da riportare appena il progetto è ripristinato (data 2026-07-16, autore "Claude Code (CC)"):

- **CIRC-C8.5.3.1** (perimetro TABELLE, gate G2|G4): controllo VC8-G4-TF eseguito con doppio passaggio indipendente su Tabelle C8.5.I e C8.5.II (100% delle celle logiche); 8 difformità ERR-MD rilevate e corrette nella copia proposta; NON dichiarare conforme finché le correzioni non sono promosse sul file vivo e ricontrollate in loco.
- **CIRC-C8.5.4.1** (perimetro FORMULE, gate G2|G4): formule [C8.5.4.1], [C8.5.4.2], [C8.5.4.3] CONFORMI (doppio passaggio + confronto visivo render); 6 difformità ERR-MD nel corredo di definizioni (frase LC3 e paragrafo "dove…") corrette nella copia proposta; stessa riserva di promozione.
- `TODO.md` di cartella: assente, non aggiornabile; l'esito pilota è consegnato con questo registro.
- Il CSV master `normativa/_registro-verifica-conformita.csv` NON è stato toccato (fuori mandato).

## 8. Chiusura

- Perimetro verificato: 100% dello scope congelato (2 tabelle = 104 celle dati + 16 etichette di riga + 2 apparati di intestazione + 7 note; 3 formule esposte; 5 blocchi di prosa collegata; 1 nota a piè di pagina; richiami alla Tabella C.8.5.III limitati al richiamo).
- Criterio di accettazione (§12 del protocollo): **NON superato in questa sessione** — le correzioni ERR-MD non sono promosse sul Markdown vivo (file assente) e registro di dettaglio/TODO non sono aggiornabili. Stato dichiarato: **controllo in corso — correzioni pronte, promozione pendente**. Nessuna unità viene dichiarata "conforme" oltre a quelle con esito OK nel `manifest.csv` (le 3 formule e la nota 3, riferite allo snapshot congelato).
- Doppio controllo indipendente eseguito da agenti AI (A: CC/Fable 5; B: subagente Opus; recheck: verificatore fresco Opus); nessuna revisione umana integrale inclusa nel presente audit.
- Al ripristino del progetto: (1) verificare l'hash del PDF Circolare contro il manifest fonti; (2) se `cap08/8-esistenti.md` ricompare con SHA pre-audit `9d2334c0…`, sostituirlo con la copia corretta (o riapplicare E1-E14) e verificare lo SHA `612a2c00…`; se ricompare con hash diverso, aprire un NUOVO snapshot (protocollo §3); (3) aggiornare CSV di dettaglio + lint + TODO come da §7; (4) solo allora valutare la dichiarazione di conformità del lotto.
- Lotti successivi proposti (protocollo §13): C8-T02 = Tabelle C.8.5.III e C8.5.IV; C8-F02 = successive ~10 formule esposte C8; lotto dedicato di fedeltà prosa per le righe md 407-422 (simboli deteriorati già segnalati nello scope); dopo C8, Capitolo 7 (mismatch noto formula 7.9.4).

Firma: audit ripreso e chiuso da Claude Code (CC), modello Fable 5, 2026-07-16.
