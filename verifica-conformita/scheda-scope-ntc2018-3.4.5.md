---
scope_id: ntc2018-3.4.5
atti:
  - "D.M. 17/01/2018, § 3.4.5 COEFFICIENTE TERMICO"
  - "Circolare 21/01/2019 n. 7 C.S.LL.PP., § C3.4.5 COEFFICIENTE TERMICO"
file_markdown: cap03/3.4.5-neve-coefficiente-termico.md
fonte_ntc: {pdf: verifica-conformita/fonte-ufficiale/GU-2018-42-SO8-DM-17-01-2018.pdf, pagine_fisiche: 63}
fonte_circolare: {pdf: verifica-conformita/fonte-ufficiale/GU-2019-35-SO5-Circolare-7-2019.pdf, pagine_fisiche: 81}
unita_registro: 1
pagine_fonte: 2
stato: CHIUSO
agente: HRM
macchina: "W520 / container hermes-ntc-vc, hostname ec834751365a"
presa_in_carico: 2026-09-09T13:23:26+02:00
procedura: VC-NTC/3
procedura_sha256: 4bd4440a6f9b204338e97ecf78c9bb74ab0d9e04f7478b9c97c436c62e817c7c
catalogo_sha256: d71319206ec54bcac3639dfd0b97c41754fa1062655b2d35c36ee5d6cb3036d6
snapshot_iniziale_sha256: b6b467482175546c91509ef8f76489039357e5a0c08de54d677991e81fdc154c
snapshot_sha256: 3541307932ff82abd016c34b325b6bb11877315ae8cc1db320b57d925cb7ebd5
giro_g6: 2
max_giri: 3
rilievi_aperti: 0
rilievi_persistenti: 0
gate: {G0: OK, G1: OK, G2: OK, G3: OK, G4: OK, G5: OK, G6: OK, G7: OK}
attesa_decisione: []
prossimo_passo: "Nessuna sul file: VC conclusa sullo snapshot registrato."
routing_effettivo:
  coordinatore: {modello: gpt-5.6-sol, provider: openai-codex, ragionamento: high, contesti: 3, tentativi: 3, compressioni_runtime: 1, ultima_compressione: "2026-09-09T14:54:00+02:00", ultimo_ripristino: "2026-09-10, container ricreato e stato ricostruito dai file", ruolo: "C"}
  meccanica: "script locali"
  correttore: {modello: gpt-5.6-sol, provider: openai-codex, ragionamento: high, contesti: 1_separato, ruolo: "E", stato: "completato; runtime ereditato dal coordinatore, non terra/medium"}
  correttore_g5: {modello: gpt-5.6-sol, provider: openai-codex, ragionamento: high, contesti: 1_separato, ruolo: "E", stato: "completato; runtime ereditato dal coordinatore, non terra/medium"}
  verificatore_r02: {modello: gpt-5.6-sol, provider: openai-codex, ragionamento: xhigh, sessione: 20260909_145740_bd7dee, contesti: 1, tentativi: 1, stato: G6_KO_ERR_AUDIT_resa_target_assente}
  verificatore_r03: {modello: gpt-5.6-sol, provider: openai-codex, ragionamento: xhigh, sessione: 20260909_165403_00ba4e, contesti: 1, tentativi: 3, stato: G6_OK_dopo_rettifica_append_only_verificata}
  verificatore_g7_rettifica_verbale: {modello: gpt-5.6-sol, provider: openai-codex, ragionamento: xhigh, sessione: 20260909_165403_00ba4e, stato: G7_R07_OK_append_only}
consumi:
  coordinatore: {sessione: ricreata_2026-09-10, contesti: 3, tentativi: 3, compressioni_runtime: 1, evento_compressione: "2026-09-09T14:54:00+02:00", contatori: non_esposti_dal_runtime_della_chat}
  correttore: {delegazione: deleg_b940d358, subagent: sa-0-bad5cdb7, contatori: non_esposti_nel_riepilogo_figlio}
  correttore_g5: {delegazione: deleg_b25407dc, subagent: sa-0-a109bfc5, contatori: non_esposti_nel_riepilogo_figlio}
  meccanica: {render_g5: "2 tentativi: R01 KO visivo, R02 OK", prepara_g6: "3 tentativi: R01 a 200 dpi non consegnato; R02 usato ma KO per resa target assente; R03 sostitutivo con asset target differiti"}
  verificatore_r02: {sessione: 20260909_145740_bd7dee, fase_fonte_prima: completata, fase_confronto: KO_ERR_AUDIT, contesti: 1, tentativi: 1, copertura: 11_su_11, contatori: da_acquisire_dal_runtime_host}
  verificatore_r03: {sessione: 20260909_165403_00ba4e, fase_fonte_prima: completata, fase_confronto: KO_ERR_AUDIT_descrittivo, fase_rettifica: OK, esito_g6_post_rettifica: OK, contesti: 1, tentativi: 3, elementi: 11, contatori_token: non_esposti_dal_canale_V}
---

# Scheda scope § 3.4.5

## Presa in carico 2026-09-09, HRM

Sandro ha autorizzato in chat la VC del solo § 3.4.5, Coefficiente termico, considerando inviato il testo `ai/ai-ag-hermes/ai-ag-hermes-260907-consegna-vc-3.4.5.md`. Il prompt operativo è stato preso in carico con sigla HRM e rinominato `PROMPT-IN-CORSO-VC-3.4.5.md` prima di modificare altri file. Nessun altro scope è autorizzato.

Il registro riportava `MAI-FATTA`, senza altri scope `IN-CORSO` e senza scheda o lucchetto preesistente. Sono stati ricalcolati gli hash delle due fonti ufficiali congelate, del target, della procedura e del catalogo. Confini preliminari accertati direttamente sui raster delle pagine fisiche: NTC pagina 63, dalla rubrica `3.4.5. COEFFICIENTE TERMICO` fino a prima di `3.5. AZIONI DELLA TEMPERATURA`; Circolare pagina 81, dalla rubrica `C3.4.5 COEFFICIENTE TERMICO` fino a prima di `C3.5 AZIONI DELLA TEMPERATURA`. Le porzioni precedenti e successive sulle pagine condivise sono escluse.

Fonti: NTC SHA-256 `dda1e397d56d71aa0f5bc457c3ba9b77064a468699dfc37bd056ac6c47105a46`; Circolare SHA-256 `f7c3b8d1f443aadb6b3e020b6b6c19813683492ecaadd2c15bf6bf1939aaed7c`. Target iniziale SHA-256 `b6b467482175546c91509ef8f76489039357e5a0c08de54d677991e81fdc154c`. Evidenze iniziali in `_tmp_render/cap03/vc-3.4.5-20260909/`; i tentativi `apertura` e `apertura-r02`, fermati rispettivamente dalla serializzazione di dati binari e dalla copia dei metadati temporali, restano conservati. `apertura-r03` è il fascicolo iniziale valido con pagine a 200 e 600 dpi, estrazioni e copie congelate.

## G0-G4 iniziali, 2026-09-09, HRM

G0 e G1 sono `OK`; la ricognizione di vigenza è documentata nel fascicolo `apertura-r03` con atti completi ufficiali e ricerche salvate. L'inventario G2 comprende due rubriche, un capoverso NTC, tre capoversi della Circolare e cinque elementi inline sostanziali; non vi sono asset, tabelle, figure, formule numerate, note o rimandi.

Il confronto G3-G4 ha aperto quattro `ERR-MD`: cassa della rubrica NTC, stile romano del simbolo con pedice `C_t`, cassa e punto spurio nella rubrica della Circolare, punto spurio dopo `1 W/m²K°`. La lista chiusa è in `_tmp_render/cap03/vc-3.4.5-20260909/apertura-r03/rapporto-c-g2-g4-iniziale.md`. E è una conversazione figlia separata, ma eredita il runtime effettivo `gpt-5.6-sol/high`; l'entry point CLI `terra/medium` registrato nel collaudo non è presente nel container, quindi non viene dichiarato.

## Correzione e ricollazione, 2026-09-09, HRM

E distinto ha applicato le quattro sostituzioni chiuse nel solo target e ha dichiarato zero differenze non autorizzate; C ha riletto il file. Dopo la rigenerazione meccanica dell'indice interno, il target depurato coincide byte per byte con la trascrizione normalizzata. G3 e G4 ripetuti: `OK`, zero rilievi aperti. Snapshot corrente SHA-256 `4527c114103e513df46c7deb497471aeb995f2bf2a4907e652678dc047e79f19`.

Il generatore degli indici ha chiuso su 311 file e 1754 collegamenti, con un solo SHA complessivo mutato e 311 corpi invariati rispetto all'operazione sugli apparati. Il linter del registro è a zero errori e zero avvisi; la vista XLSX è conforme al CSV. Per consentire lo snapshot sul filesystem condiviso, `strumenti/genera-indici-interni.py` usa ora `copyfile` al posto di `copy2`: il manifest certifica i byte e non richiede metadati temporali.

## Blocco G5, 2026-09-09, HRM

Il tentativo canonico `g5-r02` si arresta realmente all'invocazione di `pandoc`, assente nel container; sono assenti anche `xelatex` e `pdftoppm`. Il render non è stato sostituito con un metodo diverso. La consegna per l'host è `_tmp_render/cap03/vc-3.4.5-20260909/richiesta-operatore-g5.md`. G6 e G7 non sono avviati.

Prossima azione: eseguire sull'host il render canonico G5 del solo § 3.4.5 sullo snapshot `4527c114103e513df46c7deb497471aeb995f2bf2a4907e652678dc047e79f19` e restituire PDF, PNG a 200 dpi ed esito; non avviare G6.

## G5 R01 e correzione del capoverso, 2026-09-09, HRM

Il render host R01 è stato prodotto sullo snapshot previsto e senza warning. Il controllo visivo integrale ha confermato cassa, simbolo con pedice, valori, unità, punteggiatura, leggibilità e assenza di artefatti, ma ha aperto `ERR-MD-G5-01`: la fonte presenta tre capoversi nella Circolare, mentre il target e il render ne fondevano i primi due. G5 R01 è `KO`; G6 non è stato avviato.

E distinto ha inserito esclusivamente un capoverso fra `in linea generale.` e `Laddove adeguatamente motivato`, dichiarando zero differenze non autorizzate; C ha riletto il target. La ricollazione completa del Markdown depurato coincide byte per byte con la trascrizione normalizzata. G3-G4 ripetuti: `OK`, zero rilievi aperti. Nuovo snapshot SHA-256 `3541307932ff82abd016c34b325b6bb11877315ae8cc1db320b57d925cb7ebd5`.

La consegna R02 è `_tmp_render/cap03/vc-3.4.5-20260909/richiesta-operatore-g5-r02.md`.

Prossima azione: eseguire sull'host il render canonico G5 R02 del solo § 3.4.5 sullo snapshot `3541307932ff82abd016c34b325b6bb11877315ae8cc1db320b57d925cb7ebd5` e restituire PDF, PNG a 200 dpi ed esito; non avviare G6.

## G5 R02 e predisposizione del blocco G6, 2026-09-09, HRM

Il render host R02 è stato prodotto sullo snapshot `3541307932ff82abd016c34b325b6bb11877315ae8cc1db320b57d925cb7ebd5`, coincidente col target ricalcolato. L'operatore ha attestato renderer riuscito, nessun warning o errore, nessun tag reso fra parentesi tonde e nessuna didascalia automatica. C ha controllato integralmente il PNG e un ritaglio ravvicinato contro i raster fonte a 600 dpi: rubriche, prosa, simbolo con pedice, valori, unità, punteggiatura e tre capoversi della Circolare sono conformi; nessun glifo mancante, taglio o sovrapposizione. PDF SHA-256 `9ea070d117aa890c7509f0bff88da150e4de7fec337ca154f9370215be972dbc`; PNG SHA-256 `28063269a8e3f5ad5173b2926f20308dc14794e315d4c798814788def6ce2b95`. G5 R02: `OK`; zero rilievi aperti.

Alle 14:54 C ha subito una compressione automatica del contesto del runtime. Ai fini del § 10 sono registrati per C due contesti e due tentativi nella stessa sessione, con una compressione; i contatori token della chat non sono esposti. Modello effettivo invariato: `gpt-5.6-sol`, provider `openai-codex`, ragionamento `high`.

Il primo pre-pacchetto G6, integro ma a 200 dpi, è conservato in `/opt/data/vc-ntc-3.4.5-g6-r01` come tentativo preparatorio non consegnato. Il blocco destinato a V è stato rigenerato a 600 dpi in `/opt/data/vc-ntc-3.4.5-g6-r02/b01`; contiene soltanto istruzioni neutre, perimetro, canone, manifest fonte e le due pagine fonte da 4959 × 7017 pixel. `testo.md` non esiste ancora. `coordinamento.json` resta nella cartella superiore e non va montato né consegnato a V. G6 non è avviato e `giro_g6` resta 0.

Prossima azione: avviare sull'host il verificatore V isolato per la sola fase fonte-prima G6, consegnandogli esclusivamente `/opt/data/vc-ntc-3.4.5-g6-r02/b01`; fermarsi dopo `inventario.json`, senza rivelare il target.

## Adozione VC-NTC/3 e inventario fonte-prima G6, 2026-09-09, HRM

Prima del congelamento e dell'accesso di V al target, lo scope adotta la procedura vigente VC-NTC/3, SHA-256 `4bd4440a6f9b204338e97ecf78c9bb74ab0d9e04f7478b9c97c436c62e817c7c`, secondo il § 1. Restano invariati snapshot, rilievi, adjudicazioni, `giro_g6: 0`, `max_giri: 3` e decisioni pendenti. Il canone G6 non è cambiato: la copia nel blocco misura 8705 byte e ha SHA-256 `546023234aec119b42de98bb7499187fdb8445f1ac83e5b32743e13174c1eb44`, identico al canone rigenerato; il § 10 della revisione 3 dichiara validi i pacchetti già confezionati sotto la revisione 2 quando il canone è invariato.

Il V isolato, sessione `20260909_145740_bd7dee`, ha completato la sola fase fonte-prima nello stesso blocco: 11 elementi, 4 su `ntc:63` e 7 su `circ:81`, quattro esclusioni, nessun dubbio, esito provvisorio `LEGGIBILE`. Nel blocco è comparso soltanto `inventario.json`; V ha dichiarato nessun accesso al target. Il runtime host conserva l'identificativo della sessione per la ripresa della fase di confronto nello stesso contesto. Inventario non ancora congelato al momento di questa registrazione.

Prossima azione: validare `inventario.json`, quindi eseguire `rivela` per congelare inventario, esito e canone prima di creare `testo.md`; fermarsi senza avviare il confronto.

## Congelamento e rivelazione G6, 2026-09-09, HRM

`valida-inventario` ha restituito schema `OK`, 11 elementi e 2 pagine, senza emettere giudizi VC. `rivela` ha quindi congelato prima della rivelazione: inventario SHA-256 `f78112c1c0a124599be7c0ba17c3467324c2bcd0da8bb0ca67bc537d6e96d64f`, esito provvisorio `LEGGIBILE`, canone SHA-256 `546023234aec119b42de98bb7499187fdb8445f1ac83e5b32743e13174c1eb44` e manifest fonte SHA-256 `a151d996e38cbad05c2920f7a228b68a3e21b7b7813238e4ee34e071b6230a33`. `congelamento.json` precede `testo.md` ed è stato riaperto dallo script.

Il testo depurato è stato poi creato con SHA-256 `5f654893f4e6b0ff78686d012b2e4b750c01271f3b012cac433ec388ebfce2be`; `input-confronto.json` ha SHA-256 `d9deccb812bc62532901bd11647496060f989cdfb131c16334c7620672cc0820`. `verifica-pacchetto` ha restituito integrità `OK`, 9 file verificati e nessun giudizio VC. V non ha ancora ripreso la sessione né aperto il target: `giro_g6` resta 0 fino al primo accesso di V a `testo.md`. Il CSV non è stato modificato a mano, in applicazione della VC-NTC/3.

Prossima azione: riprendere sull'host la sessione V `20260909_145740_bd7dee` per il confronto G6 sul blocco `/opt/data/vc-ntc-3.4.5-g6-r02/b01`; produrre `rapporto-g6.json` e fermarsi, senza avviare G7.

## G6 R02 KO e blocco sostitutivo R03, 2026-09-09, HRM

V ha ripreso la sessione isolata `20260909_145740_bd7dee`, ha avuto accesso al target e ha confrontato integralmente 11/11 elementi, dichiarando normalizzazioni 1 e 2 e letture limitate a `/blocco`. `giro_g6` sale a 1/3. Il rapporto originario, SHA-256 `f88f6eca515d68422cbdbcece83e98ef8ffc3624721d77bfb3022f654231bb50`, chiude R02 `KO` con un solo `ERR-AUDIT`, `V-NTC63-345-FORM1`: confronto strutturale concorde, nessuna difformità del corpus accertata, ma assenza nel manifest di una resa target osservabile per la verifica visiva della formula inline.

Adjudicazione C: il rilievo è confermato come errore del pacchetto, non del corpus. Non si integra R02 dopo il confronto, perché `input-confronto.json` ha congelato un insieme privo di una prova target obbligatoria e la procedura disciplina le integrazioni successive per le sole prove fonte. Il rapporto non contiene un errore documentale rettificabile. R02 resta immutato e il blocco viene sostituito nello stesso giro, sul medesimo snapshot, da un nuovo contesto V fonte-prima.

La versione effettiva di `prepara` non accettava asset espliciti dal JSON. È stato aggiunto il supporto meccanico a `blocchi[].assets`, con nome portabile, sorgente interna al progetto e SHA-256 obbligatorio; gli asset restano fuori dalla fase fonte-prima e sono copiati soltanto da `rivela`, dopo il congelamento. Suite sintetica: 26 test su 26 `OK`, compresi occultamento fino al congelamento, verifica hash e manifest del confronto.

Il blocco sostitutivo `/opt/data/vc-ntc-3.4.5-g6-r03/b01` contiene ora soltanto i sei input fonte ammessi. Nel coordinamento esterno sono registrati il PDF G5 R02, SHA-256 `9ea070d117aa890c7509f0bff88da150e4de7fec337ca154f9370215be972dbc`, e il PNG a 200 dpi, SHA-256 `28063269a8e3f5ad5173b2926f20308dc14794e315d4c798814788def6ce2b95`, da rivelare dopo il nuovo inventario. Snapshot invariato `3541307932ff82abd016c34b325b6bb11877315ae8cc1db320b57d925cb7ebd5`. Un solo `ERR-AUDIT` aperto; G7 non avviato. Il CSV non è stato modificato a mano.

Prossima azione: avviare sull'host un nuovo V in contesto fresco per la sola fase fonte-prima del blocco sostitutivo `/opt/data/vc-ntc-3.4.5-g6-r03/b01`; fermarsi dopo `inventario.json`, senza rivelare il target.

## Congelamento e rivelazione G6 R03, 2026-09-09, HRM

Il V fresco, sessione `20260909_165403_00ba4e`, ha prodotto un inventario fonte-prima autonomo con 11 elementi, 4 su `ntc:63` e 7 su `circ:81`, quattro esclusioni, nessun dubbio ed esito `LEGGIBILE`; ha dichiarato nessun accesso al target. Prima della rivelazione il blocco conteneva soltanto i sei input fonte e `inventario.json`.

`valida-inventario` e `rivela` sono stati eseguiti consecutivamente. Validazione: schema `OK`, 11 elementi, 2 pagine, nessun giudizio VC. Congelamento: inventario SHA-256 `70fc44ed20f24ecf4b67b1ad242d457ca9e2299b9721852eccc7e4521a6865d2`, esito `LEGGIBILE`, canone SHA-256 `546023234aec119b42de98bb7499187fdb8445f1ac83e5b32743e13174c1eb44`, manifest fonte SHA-256 `a151d996e38cbad05c2920f7a228b68a3e21b7b7813238e4ee34e071b6230a33`.

Dopo il congelamento sono stati rivelati `testo.md`, il PDF e il PNG del render G5 R02. `input-confronto.json` ha SHA-256 `880b71f0ba7fd08fda1b99a2589065d08753fdc3472bdef73aa9a8ab0fae05a8` e comprende 11 file; `verifica-pacchetto` ha restituito integrità `OK`. Gli asset coincidono con le impronte G5: PDF `9ea070d117aa890c7509f0bff88da150e4de7fec337ca154f9370215be972dbc`, PNG `28063269a8e3f5ad5173b2926f20308dc14794e315d4c798814788def6ce2b95`. V non ha ancora ripreso la sessione né aperto gli input rivelati. R03 è il recupero sostitutivo del giro 1/3; l'`ERR-AUDIT` R02 resta aperto fino all'esito del confronto R03. Il CSV non è stato modificato a mano.

Prossima azione: riprendere sull'host la sessione V `20260909_165403_00ba4e` per il confronto G6 R03 sul blocco `/opt/data/vc-ntc-3.4.5-g6-r03/b01`, compresa la cartella `resa-target`; produrre `rapporto-g6.json` e fermarsi, senza avviare G7.

## G6 R03 e rettifica append-only, 2026-09-10, HRM

Il rapporto originario R03, SHA-256 `8c0282e4a2bd5383e714e3220a794fa08be17ca9afac4e2af8073664b89f911d`, ha coperto integralmente 11/11 ID contro le due pagine fonte, `testo.md`, PDF e PNG, senza `ERR-MD` né dubbi. V ha aperto un solo `ERR-AUDIT`: gli estremi descrittivi congelati di `CIRC81-PRO-001` non delimitavano il primo capoverso effettivamente verificato. Testo normativo e resa erano conformi. `giro_g6` è 2/3.

Adjudicazione C: errore nella sola mappatura descrittiva, senza copertura mancante e con target, fonti, asset e manifest effettivamente verificati invariati. Applicati i §§ 7 e 8 con `rettifica-inventario-001.json` separata, SHA-256 `cf0677a67f19d96a70c15742363b59ca4a234f03ff125aed79bb9955163900a8`; nessun congelato e nessun rapporto originario sono stati sovrascritti.

Lo stesso V, nella sessione `20260909_165403_00ba4e`, ha verificato il solo delta. `esito-rettifica-g6-001.json`, SHA-256 `4e65f462a8554bd55bd392131a31292d2b100bb905b1ad62bd9cad90660b9dc5`, dichiara rettifica `OK`, rilievo originario `CHIUSO`, G6 post-rettifica `OK` e nessun nuovo rilievo. La ripresa è documentata dal canale isolato; letture limitate a `/blocco`, senza workspace o coordinamento. G6: `OK`, rilievi residui zero. G7 non ancora avviato.

Il 2026-09-10 il container C è stato ricreato. Il nuovo contesto, hostname `ec834751365a`, ha ricostruito lo stato con `vc-supporto.py avvio 3.4.5` e dai file autoritativi; procedura, catalogo, target e fonti sono stati ricalcolati con hash coincidenti. Il contesto C sale a 3; i contatori token non sono esposti.

Prossima azione: preparare nel blocco R03 le evidenze di chiusura del § 9 e richiedere al medesimo V il giudizio G7; non aprire altri scope.

## G7 R01 KO-AUDIT, 2026-09-10, HRM

V ha ripreso la sessione `20260909_165403_00ba4e` tramite il canale isolato e ha scritto `giudizio-g7.json`, SHA-256 `15054f77dbce3082431d96fa11fcdbb382a7d5804d7936708276204bd2867c20`. Il giudizio è `KO` per tre soli `ERR-AUDIT`: nel manifest è entrata la copia VC-NTC/2, SHA-256 `1781211f…`, invece della VC-NTC/3 dichiarata e adottata; il rapporto G2-G4 iniziale indica per errore `C3.4.5.1` anziché `C3.5` come inizio dell'area successiva; lo stesso rapporto associa apostrofi e a capo a N01/N03/N10 anziché, rispettivamente, N2 e N1.

Adjudicazione C: target, fonti, asset e G6 non cambiano. I tre rilievi ricadono nel recupero documentale append-only del § 8; occorrono rettifica separata, nuovo manifest verificato e riapertura del solo G7. G6 resta `OK`, giro 2/3. G7 R01 resta conservato come esito negativo.

Prossima azione: rettificare append-only le tre incongruenze documentali del G7 R01, generare un nuovo manifest e riaprire il solo G7; G6 e target restano invariati.

## G7 R02 KO-AUDIT, 2026-09-10, HRM

Il manifest R02, SHA-256 `db94e1930760c2de0c8bc077983a7366d67aafff689606ec65c56d81e5cfe4cd`, ha chiuso i tre rilievi R01. V ha però aperto due nuovi `ERR-AUDIT`: la rettifica C ha trasposto l'hash R01 come `04bd73…` invece dell'effettivo `04db73…`; la procedura congelata si identifica correttamente come revisione 3 ma conserva al § 2 il richiamo letterale storico `procedura: VC-NTC/2`. Giudizio R02 SHA-256 `44dca2a727a36a4bf522a7224e3515667bdb57039bab5a477a423367ee62e916`.

Adjudicazione C: entrambi sono difetti documentali append-only. Il secondo è un richiamo interno obsoleto, non una modifica dei criteri o della revisione adottata, attestata dal frontmatter e dall'hash R3. Target, fonti, asset e G6 restano invariati.

Prossima azione: rettificare append-only l'hash del manifest R01 e il richiamo interno VC-NTC/2 rimasto nella procedura R3 congelata; generare il manifest R03 e riaprire il solo G7.

## G7 R03 KO-AUDIT, 2026-09-10, HRM

Il manifest R03, 54 file e integrità `OK`, ha SHA-256 `17a29d8ea850ef95cbf07a0e242c8e59392cf2e85eb138c9b1ecf7062e97145a`.

V ha chiuso i due rilievi R02 e ha lasciato un solo `ERR-AUDIT`: l'impronta del manifest R03 non era presente nelle evidenze osservabili. Giudizio R03 SHA-256 `d54f6f4de997403aaeea1e3c5b85e18439177415db16e3c2f9197cbc79b628da`. Il § 9 chiude manifest, G7 e verbale esternamente per evitare autoreferenze: si fornisce quindi il valore calcolato come aggiunta esterna, senza rigenerare il manifest. Target, fonti e G6 restano invariati.

Prossima azione: fornire a V l'impronta esterna del manifest R03 e riaprire il solo G7 sul delta; non rigenerare manifest, G6 o target.

## G7 R04 OK, 2026-09-10, HRM

V ha verificato il delta esterno `impronta-manifest-r03.json` e ha emesso `G7: OK`: G0-G7 tutti `OK`, nessun rilievo aperto. Manifest R03 SHA-256 `17a29d8ea850ef95cbf07a0e242c8e59392cf2e85eb138c9b1ecf7062e97145a`; giudizio G7 SHA-256 `ef41f4c27a5134149f0aefcb3419924e76d9d2c091094de1f59485cf5bf81aea`. Sessione V `20260909_165403_00ba4e`, conservata fra G6 e G7; verifica R04 limitata al delta esterno, senza rifare G6, inventario, render o confronto. Firma: Hermes NTC-VC / HRM.

Prossima azione: eseguire il rilascio atomico VC-OK sullo snapshot registrato; nessun altro scope è autorizzato.

## Rilascio VC-OK, 2026-09-10, HRM

VC-NTC/3 conclusa sullo snapshot `3541307932ff82abd016c34b325b6bb11877315ae8cc1db320b57d925cb7ebd5`. Manifest finale R02 di 67 file SHA-256 `e338cac1d900f68473c48e30f7dfe11a6070cd4abf4649d8faf39415759a4586`; giudizio G7 finale R06 `OK`, SHA-256 `bafadafecdc3001439ba5d26523e72a0fd6aab1195e79d23159aa7d6cf1d937e`; verbale `verifica-conformita/verbale-VC-ntc2018-3.4.5-2026-09-10.md`. Zero rilievi aperti. Firma: Hermes NTC-VC / HRM.

Prossima azione: Nessuna sul file: VC conclusa sullo snapshot registrato.

## Rettifica append-only n. 1 del verbale e G7 R07, 2026-09-10, HRM

Tre rilievi documentali successivi al rilascio sono stati trattati ai sensi del § 8 senza modificare verbale originario, target, fonti, G6 o manifest base. La rettifica separata dichiara la natura AI di C, E e V, l'assenza di revisione umana integrale e l'isolamento del verificatore; integra gli URL ufficiali degli atti e registra `AF-3.4.5-01`, assenza del punto fermo dopo `1 W/m²K°` nella Circolare, pagina fisica 81, conservata nel target.

Il solo G7 R07 ha restituito `OK`, G0-G7 tutti `OK` e zero rilievi. Manifest della rettifica, 10 file, SHA-256 `93e838f8f5ecd8c17e512c25282992289d0177792dc209b4710de0d0df471984`; giudizio SHA-256 `f09086de9625ede5807f4f8ea64a38bc70b6ef6101d3166e119482ce15cc3b47`. Stato `VC-OK` e snapshot invariati. Firma: Hermes NTC-VC / HRM.

Prossima azione: Nessuna sul file: VC conclusa sullo snapshot registrato.
