---
scope_id: ntc2018-3.5
atti:
  - "D.M. 17/01/2018, § 3.5 AZIONI DELLA TEMPERATURA"
  - "Circolare 21/01/2019 n. 7 C.S.LL.PP., § C3.5 AZIONI DELLA TEMPERATURA"
file_markdown:
  - cap03/3.5-introduzione.md
  - cap03/3.5.1-temperatura-generalita.md
  - cap03/3.5.2-temperatura-temperatura-dell-aria-esterna.md
  - cap03/3.5.3-temperatura-temperatura-dell-aria-interna.md
  - cap03/3.5.4-temperatura-distribuzione-della-temperatura-negli-elementi-strutturali.md
  - cap03/3.5.5-temperatura-azioni-termiche-sugli-edifici.md
  - cap03/3.5.6-temperatura-particolari-precauzioni-nel-progetto-di-strutture-soggette-ad-azioni.md
  - cap03/3.5.7-temperatura-effetti-delle-azioni-termiche.md
righe_registro: [3.5.1, 3.5.2, 3.5.3, 3.5.4, 3.5.5, 3.5.6, 3.5.7]
fonte_ntc: {pdf: verifica-conformita/fonte-ufficiale/GU-2018-42-SO8-DM-17-01-2018.pdf, pagine_fisiche: 63-66}
fonte_circolare: {pdf: verifica-conformita/fonte-ufficiale/GU-2019-35-SO5-Circolare-7-2019.pdf, pagine_fisiche: 81}
unita_registro: 7
file_scope: 8
pagine_fonte: 5
formule_numerate_attese_preliminari: 8
tabelle_attese_preliminari: 3
figure_attese_preliminari: 2
stato: CHIUSO
agente: CDX
macchina: "W520 / Codex app, Windows"
presa_in_carico: 2026-09-11T16:32:59+02:00
prima_misura_temporale: 2026-09-10T14:56:38+02:00
procedura: VC-NTC/3
procedura_sha256: 4bd4440a6f9b204338e97ecf78c9bb74ab0d9e04f7478b9c97c436c62e817c7c
catalogo_sha256: d71319206ec54bcac3639dfd0b97c41754fa1062655b2d35c36ee5d6cb3036d6
snapshot_iniziale_manifest: _tmp_render/cap03/vc-3.5-20260910/apertura-r01/snapshot-iniziale-esistente.json
snapshot_iniziale_sha256: 2577aa2a2057adcc6eb4a155899093c2e95b054837827871940ec5c1dd1b3838
snapshot_sha256: bce58988f35b359df4ea503c1ce0785f4c11c97d395d57dc8d6ff13a913a9344
snapshot_finale_manifest: verifica-conformita/vc-ntc2018-3.5-2026-09-11/g5-cdx-r02/snapshot-target-finale.json
asset_inizialmente_mancanti:
  - cap03/img/fig-3.5.1-zone-temperatura-mappa.png
  - cap03/img/fig-3.5.2-temperatura-elemento-schema.png
giro_g6: 2
max_giri: 3
rilievi_aperti: 0
rilievi_persistenti: 0
gate: {G0: OK, G1: OK, G2: OK, G3: OK, G4: OK, G5: OK, G6: OK, G7: OK}
attesa_decisione: []
prossimo_passo: "Attendere un nuovo via libera prima di aprire il § 3.6 o altri scope."
routing_effettivo:
  verificatore_ripresa_r02: {modello: gpt-5.6-sol, ragionamento: xhigh, agente_nativo: /root/v35_b01_r02, ruolo: V, contesti: 1, tentativi: 1, isolamento: istruttivo_con_letture_controllate, fase: confronto}
  editor_ripresa: {modello: gpt-5.6-terra, ragionamento: medium, agente_nativo: /root/e35_terra_r01, ruolo: E, contesti: 1, tentativi: 1}
  secondo_lettore_r7: {modello: gpt-6-astra, ragionamento: xhigh, agente_nativo: /root/c35_sol/lettore_fonte_35, ruolo: lettore_fonte_only_regressione, contesti: 1, sessione: 01a090fe-45f9-7b22-8b5e-a599762466ba}
  verificatore_ripresa_r01: {modello: gpt-5.6-sol, ragionamento: xhigh, agente_nativo: /root/v35_b01_r01, ruolo: V, contesti: 1, tentativi: 1, isolamento: istruttivo_con_letture_controllate, fase: confronto}
  coordinatore_ripresa: {modello: gpt-5.6-sol, ragionamento: high, contesti: 1, agente_nativo: /root/c35_sol, ruolo: C}
  coordinamento_principale_ripresa: {modello: gpt-6-astra, ragionamento: xhigh, sessione: 01a090ca-db85-7ed3-b78f-b12a84fba0ed, ruolo: coordinamento_tecnico, riscontro: metadati_JSONL_runtime, motivo_profilo: sessione_principale_preesistente_per_revisione_metodo_e_subentro_tecnico}
  coordinatore: {modello: gpt-5.6-sol, provider: openai-codex, ragionamento: high, contesti: 1, tentativi: 1, ruolo: C}
  editor: {sessioni: [20260910_185522_efe78c, 20260910_193518_2d97d6], modello: gpt-5.6-terra, provider: openai-codex, ragionamento: medium, contesti: 2, tentativi: 2, ruolo: E}
  meccanica: "script locali"
  verificatore_previsto_hermes_storico: {modello: gpt-5.6-sol, provider: openai-codex, ragionamento: xhigh, ruolo: V, isolamento: "container separato senza montaggio /workspace, avvio tramite canale richieste"}
consumi:
  coordinatore: {contesti: 1, tentativi: 1, contatori_token: non_esposti_dal_runtime_della_chat}
  editor: {contesti: 2, tentativi: 2, chiamate_modello: 24, chiamate_strumenti: 68, input_token: 184999, output_token: 14066, reasoning_token: 5615, cache_read_token: 1786752, costo_usd: 0.0, costo_stato: included}
---

# Scheda scope § 3.5

## Consumi e misura conclusiva, 2026-09-11, CDX

[Dati per sessione](vc-ntc2018-3.5-2026-09-11/consumi-ripresa-cdx.json), rilevati alle `2026-09-11T15:56:01.175963+00:00`. Durata trascorsa della ripresa CDX: 83.04 minuti, dalle `2026-09-11T16:32:59+02:00`, incluse le attese degli esecutori; non è una misura di ore professionali. La precedente attività Hermes e le interruzioni restano distinte.

| Ruolo | Modello / ragionamento | Input | In cache | Output | Di cui ragionamento |
|---|---|---:|---:|---:|---:|
| Coordinamento tecnico principale | `gpt-6-astra` / `xhigh` | 28.825.891 | 28.105.984 | 94.942 | 38.511 |
| C e verbale/piano | `gpt-5.6-sol` / `high` | 16.582.442 | 16.229.760 | 69.164 | 21.785 |
| Secondo lettore fonte-only | `gpt-6-astra` / `xhigh` | 137.071 | 111.872 | 953 | 164 |
| E | `gpt-5.6-terra` / `medium` | 760.972 | 687.872 | 10.589 | 1.753 |
| V G6 R01 | `gpt-5.6-sol` / `xhigh` | 3.849.698 | 3.646.976 | 30.306 | 13.165 |
| V G6 R02 e G7 | `gpt-5.6-sol` / `xhigh` | 6.621.236 | 6.312.704 | 46.629 | 20.783 |

Ogni riga identifica un contesto; per V sono presenti due contesti indipendenti. Si usa l’ultimo contatore cumulativo, per il coordinatore principale il delta rispetto al contatore anteriore al subentro. Non si sommano parent e figli perché il runtime non ne attesta l’aggregazione. Cache e ragionamento sono sottoinsiemi, non consumi da aggiungere. La misura include le registrazioni e i controlli finali fino all’ultimo contatore emesso; non include i token della presente rilevazione e della risposta conclusiva.

Il confronto quantitativo completo col § 3.4.5 non è disponibile: mancano i suoi contatori e quelli di parte della precedente attività Hermes del § 3.5; i perimetri sono inoltre diversi. Entrambi hanno richiesto due giri effettivi su tre autorizzati. In questa ripresa il canale nativo ha funzionato e il renderer canonico locale era disponibile. Nessuna percentuale di risparmio o di quota dell’abbonamento viene stimata. I consumi Hermes già presenti sotto restano nella metrica originale, che separa cache e input.

Firma: Codex / CDX.

Prossima azione: Attendere un nuovo via libera prima di aprire il § 3.6 o altri scope.

## Rilascio 2026-09-11, Codex / CDX

G7 positivo nel rapporto `vc-ntc2018-3.5-2026-09-11/rapporto-g7.json`, SHA-256 `cfb158ae4f5c26a35c8ec31df3447c140b80cc5eefb1689b798503bfc2fccd17`. Snapshot aggregato `bce58988f35b359df4ea503c1ce0785f4c11c97d395d57dc8d6ff13a913a9344`; manifest 133/133, SHA-256 `2cee48a46d7bc510cc21a140b1b4159e5f508a8b950c04e9fb0ec67d6b201f66`. [Verbale completo](verbale-VC-ntc2018-3.5-2026-09-11.md). Sette righe `VC-OK`, introduzione inclusa nella stessa verifica; nessun rilievo aperto o persistente. Il G6 resta al giro 2/3. Firma: CDX.

Prossima azione: Attendere un nuovo via libera prima di aprire il § 3.6 o altri scope.

## Secondo G6 concluso, 2026-09-11, CDX

V Sol xhigh, sessione `01a0910c-8056-7bb0-ae6b-aecc452a0c0a`, ha censito in fonte-prima 36 gruppi localizzabili, con copertura integrale degli stessi contenuti del primo giro. Congelamento alle `2026-09-11T15:22:04.856533+00:00`; misura d'orologio preaccesso alle `15:22:38.2230622Z`, chiamata che apre effettivamente il target alle `15:22:49.255Z`. Entrambe successive al congelamento. Il contatore è 2/3.

G6 `OK`, 36/36 ID, zero rilievi. La rettifica append-only `g6-cdx-r02/b01/rettifica-g6-001.json` distingue i cinque JPEG nativi della mappa dal ritaglio target, conferma l'identità del secondo asset con il PNG incorporato e precisa i soli metadati di sessione e tempo. V ha confrontato tutti i raster originali e le localizzazioni a 600 dpi; C ha accolto la rettifica, senza nuova correzione o nuovo giro G6. Normalizzazioni applicate: 1, 2, 3, 6, 9, 10; una `AF` conservata, nessuna `AF-COR`.

Le 23 chiamate registrate fino alla chiusura G6 e alla rettifica leggono soltanto il blocco e l'integrazione fonte autorizzata. Dossier `vc-ntc2018-3.5-2026-09-11/`; manifest finale verificato 133/133, SHA-256 `2cee48a46d7bc510cc21a140b1b4159e5f508a8b950c04e9fb0ec67d6b201f66`. G7 affidato allo stesso V soltanto dopo il completamento del G6.

Firma: Codex / CDX.

Prossima azione: completare G7 e le registrazioni dello scope già autorizzato, senza aprire altri scope.

## G6 R01, correzioni e nuovo G5, 2026-09-11, CDX

Il canale nativo è stato collaudato sulla continuità del contesto. V `/root/v35_b01_r01`, Sol xhigh, ha completato l'inventario fonte-prima di 74 elementi; congelamento alle `2026-09-11T14:48:49.341436+00:00`, primo accesso dichiarato al target alle `2026-09-11T14:49:26.9105963Z`. Il G6 R01 è `KO`, con sei `ERR-MD` e nessun dubbio. Letture registrate limitate al blocco e alle due integrazioni fonte autorizzate; isolamento istruttivo, senza sandbox di lettura. Questo primo confronto valido ha portato il contatore a 1/3.

C Sol high ha accolto tutti i rilievi. Per ribaltare la precedente adjudicazione R7 è stata acquisita la seconda lettura Astra xhigh fonte-only, concorde con ritaglio a 600 dpi e dati vettoriali su `d un anno` e punto e virgola finale. Lista congelata e addendum dell'àncora sono in `vc-ntc2018-3.5-2026-09-11/adjudicazione-r01/`.

E `/root/e35_terra_r01`, Terra medium, ha applicato cinque sostituzioni testuali e il ritaglio completo della mappa, aggiungendo l'annotazione `AF-3.5.2-01` con rinvio portabile. C ha confrontato tutti i byte con le operazioni approvate, verificato i due piccoli elementi insulari sotto la Sicilia e aperto tutte le cinque pagine del nuovo PDF. G0-G5 nuovamente `OK`, zero rilievi ancora aperti; il G6 precedente resta storico `KO` e deve essere ripetuto integralmente.

Nuovo snapshot: otto Markdown e due asset, manifest `bce58988f35b359df4ea503c1ce0785f4c11c97d395d57dc8d6ff13a913a9344`. PDF canonico prodotto nello stesso container, con Pandoc 3.11 e TeX Live 2026; SHA-256 `ed8cd4258d01464bca80d358f3533822177c3225f99c50ef391c99a796983f76`. Lint: zero errori e avvisi; indici: 311 file e 1754 collegamenti verificati. Il nuovo G6 mantiene l'unico blocco di cinque pagine: una divisione 3+2 violerebbe il minimo di tre pagine per blocco della procedura.

Firma: Codex / CDX.

Prossima azione: eseguire il secondo G6 integrale fonte-prima, con V Sol xhigh fresco.

## Subentro CDX autorizzato, 2026-09-11

Sandro ha autorizzato in questa chat la ripresa del § 3.5 con Codex, dopo la ricognizione del metodo e la conferma dei profili Terra/Sol. Preso in carico `PROMPT-IN-CORSO-VC-3.5-G6-CODEX.md`. Coordinamento della ripresa nella chat GPT-6; giudizi ordinari affidati a Sol high, V previsto Sol xhigh in contesto nativo fresco. E resta distinto per eventuali correzioni. Si conserva la cronologia HRM, inclusi tentativi falliti e consumi, senza azzerare `giro_g6: 0` o `max_giri: 3`.

Il nuovo tentativo usa il canale nativo Codex, da collaudare prima della fonte-prima; non rilancia il trasporto Hermes che ha fallito due volte. Isolamento istruttivo dichiarato e letture controllate secondo § 7, senza attestare una sandbox di lettura. Il riferimento alla revisione 2 nel § 2 della R3 si legge come revisione 3, secondo l'errata già presente nel dossier del § 3.4.5; nessuna modifica ai criteri o alla procedura congelata.

Firma: Codex / CDX.

Prossima azione: riscontrare G0-G5 e collaudare il canale nativo Codex prima di avviare un V Sol xhigh fonte-prima sul medesimo scope aggregato.

## Presa in carico 2026-09-10, HRM

Sandro ha autorizzato in chat la VC-NTC/3 dell'intera sezione 3.5 in un solo scope, comprendente il file introduttivo e i sette file naturali 3.5.1-3.5.7. Il dimensionamento effettivo è di cinque pagine fonte, NTC 63-66 e Circolare 81, otto formule numerate, tre tabelle e due figure: nessuna soglia del § 2 è superata. Runtime C effettivo: `gpt-5.6-sol`, provider `openai-codex`, ragionamento `high`. Nessun altro paragrafo è autorizzato.

La pagina NTC 63 è condivisa con il § 3.4.5 già `VC-OK`: il perimetro inizia dalla rubrica `3.5. AZIONI DELLA TEMPERATURA`. La pagina Circolare 81 è condivisa con C3.4.5 già `VC-OK`: il perimetro inizia dalla rubrica `C3.5. AZIONI DELLA TEMPERATURA`. Le parti precedenti sono escluse e non si toccano. `cap03/3.5-temperatura.md` è un duplicato storico non indicizzato e non registrato, escluso dal target vivo.

Lo snapshot iniziale fotografa gli otto Markdown esistenti. I due asset richiamati, Fig. 3.5.1 e Fig. 3.5.2, risultano mancanti: sono due difetti iniziali recuperabili dalle pagine ufficiali e impediscono di chiudere G4-G5 finché non vengono ripristinati e verificati.

## Correzioni E e verifica C, 2026-09-10, HRM

E ha operato in sessione separata `20260910_185522_efe78c`, runtime effettivo `gpt-5.6-terra`, provider `openai-codex`, ragionamento `medium`. Il diff C contro il baseline congelato conferma tutti i 15 interventi approvati. L'unica variazione aggiuntiva è l'allineamento meccanico dell'indice interno di C3.5.2; il confronto fra il backup pre-indici e il corpus dimostra che gli altri 310 file sono identici byte per byte. Entrambe le figure sono state aperte e risultano complete, non vuote e non tagliate.

Prossima azione: Eseguire G5 canonico e controllo visivo integrale del solo scope 3.5.

## G5 R02, 2026-09-10, HRM

La verifica preliminare ha rilevato che il primo mandato E aveva congelato un nome non coincidente con il collegamento vivo della Fig. 3.5.2. E R02, sessione `20260910_193518_2d97d6`, ha creato la copia byte-identica col nome effettivamente richiamato. Il render canonico R02 ha prodotto cinque pagine, aperte integralmente: figure e tabelle complete, nessun taglio, sovrapposizione o capoverso fuso. Snapshot finale aggregato SHA-256 `1728b7d061dd7b7ddcd3ea34ef395759084293efcbb592a5201b56bb5ac29a9c`.

Prossima azione: Preparare e avviare G6 fonte-prima del solo scope 3.5.

## Tentativo di trasporto fonte-prima morto, 2026-09-11, HRM

Hermes NTC-VC / HRM aveva confezionato un solo blocco fonte-prima di cinque pagine e depositato la richiesta `vc-35-g6-r01-fonte-prima`. La macchina si è spenta dopo il marcatore `.preso` e prima dell'avvio di V. Non esistono inventario, esito o log. È un tentativo di trasporto morto, non un G6: `giro_g6` resta 0. Pacchetto e snapshot sono invariati. La richiesta è stata ridisposta col nome nuovo `vc-35-g6-r01b-fonte-prima`.

Prossima azione: Attendere l'esito della richiesta V `vc-35-g6-r01b-fonte-prima`; non aprire G7.

## Tentativo tecnico fonte-prima R01b fallito, 2026-09-11, HRM

La richiesta `vc-35-g6-r01b-fonte-prima` ha avviato il contesto V fresco `20260911_060128_6c36b1`, ma si è chiusa con uscita 1 prima dell'inventario: `Codex stream produced no SSE events for 12s after first byte`, dopo tre retry. Nessun target è stato rivelato e `giro_g6` resta 0 ai sensi del § 7. Il tentativo è conservato nei consumi. È stato preparato il blocco sostitutivo byte-identico `/opt/data/vc-ntc-3.5-g6-r01c/b01` e depositata la richiesta `vc-35-g6-r01c-fonte-prima` per un nuovo contesto fresco.

Prossima azione: Attendere l'esito della richiesta V `vc-35-g6-r01c-fonte-prima`; non aprire G7.

## Arresto della sessione, 2026-09-11, HRM

Su richiesta di Sandro, Hermes NTC-VC / HRM interrompe qui le attività. La richiesta `vc-35-g6-r01c-fonte-prima` risulta presa dal sorvegliante; il relativo file `.esito.json` non è ancora presente. G6 resta non iniziato, `giro_g6` resta 0 e G7 non è stato aperto. La sessione successiva ricostruirà lo stato dai file e leggerà l'esito V dal canale delle richieste.

Prossima azione: Leggere `/opt/data/richieste-v/vc-35-g6-r01c-fonte-prima.esito.json`; se presente, riprendere dalla fase fonte-prima senza aprire G7 anticipatamente.

## Ripresa e nuovo trasporto R01d, 2026-09-11, HRM

Hermes NTC-VC / HRM ha ricostruito lo stato dai file. La richiesta R01c, presa alle `08:06:08+02:00`, non ha prodotto esito o inventario ed è anteriore all'avvio del container corrente alle `12:53:16+02:00`: è classificata come trasporto morto, senza esecuzione V e senza consumo del giro. È stato creato il blocco sostitutivo `/opt/data/vc-ntc-3.5-g6-r01d/b01`, con input fonte byte-identici, target assente e nessun collegamento simbolico. È stata depositata la richiesta `vc-35-g6-r01d-fonte-prima`.

Prossima azione: Attendere l'esito della richiesta V `vc-35-g6-r01d-fonte-prima`; non aprire G7.

## Blocco tecnico G6 dopo R01d, 2026-09-11, HRM

La richiesta R01d ha avviato il contesto V fresco `20260911_115402_4831e6`, ma è terminata con uscita 1 prima dell'inventario: `Codex stream produced no SSE events for 12s after first byte`, dopo tre retry. È la stessa anomalia del precedente tentativo V effettivo R01b. R01c era soltanto un trasporto morto e non interrompe la consecutività delle due esecuzioni tecniche. Nessun target è stato rivelato, nessun inventario è stato prodotto e `giro_g6` resta 0. Ai sensi del § 8, non si deposita un terzo tentativo identico. G7 resta non iniziato.

Prossima azione: Sospendere nuove richieste V; Sandro decide come gestire il blocco tecnico SSE.
