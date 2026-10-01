---
scope_id: ntc2018-3.2.1
atti:
  - "D.M. 17/01/2018, § 3.2.1 Stati limite e relative probabilità di superamento"
  - "Circolare 21/01/2019 n. 7, § C3.2.1 Stati limite e relative probabilità di superamento"
file_markdown: cap03/3.2.1-azione-sismica-stati-limite-e-relative-probabilita-di-superamento.md
fonte_ntc: {pdf: verifica-conformita/fonte-ufficiale/GU-2018-42-SO8-DM-17-01-2018.pdf, pagine_fisiche: 49-50}
fonte_circolare: {pdf: verifica-conformita/fonte-ufficiale/GU-2019-35-SO5-Circolare-7-2019.pdf, pagine_fisiche: 48-50}
unita_registro: 1
formule_numerate: 4
tabelle: 3
figure: 1
pagine_fonte: 5
stato: VC-OK
agente: CDX
macchina: P53
presa_in_carico: 2026-08-28T09:47:29+02:00
giro_g6: 3
max_giri: 3
rilievi_aperti: 0
rilievi_persistenti: 0
gate: {G0: OK, G1: OK, G2: OK, G3: OK, G4: OK, G5: OK, G6: OK, G7: OK}
snapshot_sha256: d63652647c796ab4b473827eb35d285529f7041fd3e04ff9e0caa480d6ee7d20
attesa_decisione: []
prossimo_passo: "aprire il solo scope 3.2.2 e proseguire poi in sequenza fino al 3.2.4, già autorizzati da Sandro; non aprire il 3.3"
routing_effettivo:
  p0d: {modello: "script locali + gpt-5.6-luna/medium", compito: "hash, confini, inventario, collazione, render, link e candidati", esito: "OK"}
  p0s: {modello: "non_usato", motivo: "materiali predisposti deterministicamente", esito: "non necessario"}
  p1: {modello: "gpt-5.6-sol/high", motivo_escalation: "soli residui interpretativi prodotti da P0-D e verifica della patch", esito: "OK"}
  p2: {modello: "gpt-5.6-sol/xhigh", gate: "apparati, G6, adjudicazione e G7", esito: "G7 OK; manifest 16/16; promozione VC-OK confermata"}
esecutori:
  apertura: {coordinamento: "CDX/sessione principale", controlli_meccanici: "script locali"}
  preflight: {p0d: "gpt-5.6-luna/medium", g0_g1: "gpt-5.6-sol/high", p1_residui: "gpt-5.6-sol/high se necessari"}
  apparati: {passaggio_a: "gpt-5.6-luna/medium", passaggio_b: "gpt-5.6-sol/xhigh", riconciliazione: "gpt-5.6-sol/xhigh"}
---

## 2026-08-28 - G7 OK e chiusura VC (CDX)

Il precontrollo deterministico P0-D `gpt-5.6-luna/medium` e il controllo finale P2 `gpt-5.6-sol/xhigh` hanno ricalcolato e confermato 16/16 hash e 16/16 dimensioni del manifest. G0-G7 sono tutti `OK`, con zero rilievi aperti e persistenti.

Lo scope è promosso a `VC-OK al 2026-08-28` sullo snapshot Markdown `d63652647c796ab4b473827eb35d285529f7041fd3e04ff9e0caa480d6ee7d20`. Il verbale è `verbale-VC-ntc2018-3.2.1-2026-08-28.md`; le evidenze G7 sono in `_tmp_render/cap03/vc-3.2.1-20260828/g7/`.

Il controllo P2 ha inoltre confermato che la nuova equivalenza dei trattini nelle didascalie non invalida i quattro scope `VC-OK` precedenti, perché ciascuno conserva snapshot, hash e copia congelata delle normalizzazioni applicate. Prossimo scope autorizzato: 3.2.2.

## 2026-08-28 - decisione di Sandro e chiusura G6 per adjudicazione (CDX)

Sandro ha deciso che `-`, `–` e `—` sono equivalenti nei separatori delle didascalie. La voce 10 dell'elenco unico delle normalizzazioni è stata aggiornata; l'unico rilievo R03 è stato riclassificato da `ERR-MD` a `NORM` con conferma P2 `gpt-5.6-sol/xhigh`.

Il rapporto storico R03 resta immutato. Sul medesimo snapshot Markdown risultano zero `ERR-MD`, zero `ERR-AUDIT` aperti e zero `DUBBIO`; G6 è `OK`. Non è stata applicata alcuna correzione al Markdown, `max_giri` resta 3 e non occorre G6 R04. Prossimo gate: G7.

## 2026-08-28 - G6 R03 KO, budget di giri esaurito (CDX)

Il terzo giro cieco ha chiuso `KO` con un solo `ERR-MD`, zero `ERR-AUDIT` aperti e zero `DUBBIO`. Il rilievo riguarda esclusivamente il separatore della didascalia `Tab. 3.2.I`: il Markdown usa `-` U+002D, mentre la normalizzazione dichiarata n. 10 prescrive `—` U+2014 per i separatori delle didascalie del corpus.

Il rilievo è certo ma non è stato corretto, perché il ciclo § 8 impone l'arresto dopo il terzo G6 non superato. Lo scope resta `IN-CORSO`, G6 `KO`, G7 non avviato. Serve autorizzazione esplicita di Sandro per portare `max_giri` da 3 a 4; il contatore non verrà azzerato. Costo previsto per la chiusura: una correzione tipografica puntuale, rigenerazione di frammento e render, un G6 R04 integrale di cinque pagine e il G7 finale, stimati in circa 15-25 minuti.

## 2026-08-28 - congelamento G6 R03 (CDX)

Congelato il terzo giro sul Markdown SHA-256 `d63652647c796ab4b473827eb35d285529f7041fd3e04ff9e0caa480d6ee7d20`, frammento depurato `64dc3f5af326f95612099b53703bea0dd47a10ccac9fb7ebf5104b910ccddb55` e render ufficiale `566508695dcb29d0f63e679e5c8622bfeb9eb588ff69bfd75713cadbec272a6d`. Snapshot del pacchetto SHA-256 `63e684818057970c0596aae32a7c82718fed4d82d2db50e6cb63d570fb5a251c`.

Pacchetto cieco nuovo, senza rapporti o rilievi R01-R02. Disegno invariato: unico blocco integrale di cinque pagine, coordinatore P2 fresco e due verificatori P2 freschi. Il G6 R03 non riceve l'elenco delle correzioni.

## 2026-08-28 - G6 R02 KO e correzione separata (CDX)

Il secondo giro cieco ha controllato integralmente cinque pagine, 31 blocchi testuali, 4 voci di elenco, 3 tabelle con 78 posizioni logiche e 11 accorpamenti, 4 formule numerate, una relazione matematica aggiuntiva, relazioni inline, 2 note e una figura. Esito `KO`: un `ERR-MD`, zero `ERR-AUDIT` aperti e zero `DUBBIO`.

Corrette separatamente le sole parentesi quadre omesse attorno alla relazione inline del capoverso `È immediato constatare`, presenti nella Circolare a pagina fisica 48. Nessun valore, simbolo interno o apparato è stato modificato. Il giro ha inoltre censito tre gruppi `AF` chiusi, compresa la grafia `Cu` nella legenda raster della figura, registrata nell'annotazione `AF-3.2.1-03`.

## 2026-08-28 - congelamento G6 R02 (CDX)

Congelato il secondo giro sul Markdown SHA-256 `5802bb17b1e23980e0ef15021eae3a2c021b6be5d929f5c71e68a869d7f9478f`, frammento depurato `023bba2b973ad8de1701295598eecd15e5c534345bafda0786dbba41b1c1dd60` e render ufficiale `5e59ce9b3a67cecefde0dbc5f117a2e622230be3839138e4c6fab7c48334a96b`. Pacchetto cieco nuovo, senza rapporto o rilievi R01, snapshot SHA-256 `e173136b23334cc1b26a73407e9b242ba571bb469d2e5c980f2eccb99da6bc8a`.

Disegno invariato: unico blocco integrale di cinque pagine, coordinatore P2 fresco e due verificatori P2 freschi. Il G6 R02 non riceve l'elenco delle due correzioni.

## 2026-08-28 - G6 R01 KO e correzione separata (CDX)

Il primo giro cieco ha controllato integralmente 27 capoversi, 4 voci di elenco, 78 posizioni di griglia, 4 formule numerate, 7 relazioni inline, 2 note e 1 figura. Esito `KO`: due `ERR-MD`, zero `ERR-AUDIT` aperti e zero `DUBBIO`. Le due `AF` della Tabella C.3.2.II sono state confermate e non sono rilievi aperti.

Corretti separatamente i soli due residui: `ed un esiguo` nelle NTC e il trattino `–` dopo `(SLD)` nella Circolare. Nessun apparato o valore è stato modificato. Il frammento e il render devono essere rigenerati e lo scope sottoposto a G6 R02 integrale su nuovo snapshot.

## 2026-08-28 - congelamento G6 R01 (CDX)

Congelato il primo giro G6 sul Markdown vivo SHA-256 `958688213292cc054fd4727c5220c61da9e9bc5fda98f78bbf978642f9f1cb0d` e sul frammento depurato SHA-256 `85b552e04bb13cb29c874daad012a0b2ec8eb1051d0ebc1dca47de875598139f`. Pacchetto esterno al workspace composto da 16 file: dieci ritagli delle cinque pagine fonte a 200/600 dpi, frammento Markdown, asset, normalizzazioni, canone neutro, istruzioni e snapshot. Nessun rilievo atteso, audit precedente o cronologia delle correzioni è incluso.

Disegno del controllo: unico blocco di cinque pagine, coordinatore fresco P2 e due verificatori freschi P2, uno source-first e uno di confronto integrale. Snapshot del pacchetto SHA-256 `a7be06a709f62d751515059dae9bdc03989e7f82d98d21790d2b7a45d34b2911`.

## 2026-08-28 - chiusura del preflight G0-G5 (CDX)

G0-G5 chiusi `OK` sullo snapshot Markdown `958688213292cc054fd4727c5220c61da9e9bc5fda98f78bbf978642f9f1cb0d`. Copertura integrale delle cinque pagine fonte; inventario finale di tre tabelle e 78 celle logiche, quattro formule numerate, tre gruppi matematici inline e una figura.

Il preflight Moon ha isolato i candidati deterministici; Sol `high` ha ricevuto soltanto i residui testuali e la verifica della patch; Sol `xhigh` è stato usato per il passaggio B e la riconciliazione degli apparati. Corretti gli scostamenti del Markdown e registrate due anomalie della fonte, `AF-3.2.1-01/02`, senza `AF-COR`.

Indici interni, registro CSV, vista XLSX, collegamenti, asset e render ufficiale sono conformi. Il frammento depurato ha SHA-256 `85b552e04bb13cb29c874daad012a0b2ec8eb1051d0ebc1dca47de875598139f`; il render a quattro pagine ha SHA-256 `4d0e53acb3f664812e1412e189c17116af5ae38ffaa329d7ad8963e2c0599f6f`. Residui: zero `ERR-MD`, zero `ERR-AUDIT`, zero `DUBBIO`.

## 2026-08-28 - apertura dello scope sul file naturale (CDX)

Scope limitato al solo file `cap03/3.2.1-azione-sismica-stati-limite-e-relative-probabilita-di-superamento.md`, al § 3.2.1 del D.M. 17/01/2018 e al § C3.2.1 della Circolare 7/2019. Il controllo diretto delle rubriche sulle fonti ha accertato i confini: pagine fisiche NTC 49-50 e Circolare 48-50, con esclusione meccanica del testo adiacente dei §§ 3.2, 3.2.2, C3.2 e C3.2.2.

Precondizioni superate: fonti ufficiali presenti e ricalcolate agli SHA-256 `dda1e397d56d71aa0f5bc457c3ba9b77064a468699dfc37bd056ac6c47105a46` e `f7c3b8d1f443aadb6b3e020b6b6c19813683492ecaadd2c15bf6bf1939aaed7c`, coincidenti con i manifest registrati; nessun'altra scheda sul medesimo file e nessun lucchetto concorrente. Snapshot Markdown iniziale SHA-256 `2926375cb07790a4faeb0cef7704fdec2f10c7477467ec629e24bd8d2a168e8f`.

Dimensionamento preliminare: cinque pagine fonte parzialmente condivise, quattro formule numerate, tre tabelle, una figura e un asset. Lo scope resta entro le soglie economiche e formerà un unico blocco G6 di cinque pagine, dopo il preflight completo.

Routing semplificato richiesto da Sandro: script e profilo logico Moon, esposto dal runtime come `gpt-5.6-luna/medium`, per tutto il deterministico; Sol `high` riceverà soltanto candidati puntuali non risolvibili in P0-D; Sol `xhigh` resta riservato a G6, apparati critici e G7.
