---
scope_id: ntc2018-4.1
atti:
  - "D.M. 17/01/2018, § 4.1 Costruzioni di calcestruzzo"
  - "Circolare 21/01/2019 n. 7 C.S.LL.PP., § C4.1"
file_markdown: _tmp_render/ricomposizione-livello3-20260826/archivio-file-sostituiti/cap04/4.1-calcestruzzo.md
struttura_corrente: cap04/indice-4.1.md
fonte_ntc:
  pdf: verifica-conformita/fonte-ufficiale/GU-2018-42-SO8-DM-17-01-2018.pdf
  sha256: dda1e397d56d71aa0f5bc457c3ba9b77064a468699dfc37bd056ac6c47105a46
  pagine_fisiche: 74-95
fonte_circolare:
  pdf: verifica-conformita/fonte-ufficiale/GU-2019-35-SO5-Circolare-7-2019.pdf
  sha256: f7c3b8d1f443aadb6b3e020b6b6c19813683492ecaadd2c15bf6bf1939aaed7c
  pagine_fisiche: 85-99
unita_registro: 136
stato: CHIUSO
validita_corrente: SCADUTA
agente: CDX
macchina: W520
presa_in_carico: 2026-08-04T13:07:20+02:00
chiusura: 2026-08-04
giro_g6: 7
max_giri: 7
autorizzazione_max_giri: "alzato da 3 a 4 da Sandro il 2026-07-31; alzato da 4 a 5 da Sandro il 2026-08-03; alzato da 5 a 6 da Sandro il 2026-08-03, per consentire la correzione dei rilievi congelati e il sesto G6 integrale; alzato da 6 a 7 da Sandro il 2026-08-04 con il comando 'ok.. vai', in risposta alla richiesta esplicita di autorizzazione al settimo giro"
rilievi_aperti: 0
rilievi_persistenti: 0
gate: {G0: OK, G1: OK, G2: OK, G3: OK, G4: OK, G5: OK, G6: OK, G7: OK}
snapshot_sha256: 93360710906737ff6a9c3d5f91b54e353282e2c1ab08d57deab099f7465d8964
attesa_decisione: []
prossimo_passo: "recuperare o rigenerare e verificare i 13 asset mancanti, poi aprire nuovi scope sui file naturali correnti del § 4.1 e chiudere nuovi G7"
---

# Scheda di scope — § 4.1 NTC 2018 + § C4.1 Circolare

Prima scheda creata secondo `../../skills/conversione-normativa/references/ciclo-conversione-verifica.md`. Sostituisce `../old/PROMPT-CONSUMATO-PARAGRAFO-4-1-VC-OK.md`, chiuso per migrazione e non per completamento.

## Situazione

Il giudizio `VC-OK al 2026-08-04` resta valido come esito storico dello snapshot indicato, ma dal 2026-08-26 la validità corrente è `SCADUTA`. Il vecchio `cap04/4.1-calcestruzzo.md`, che conserva esattamente lo SHA-256 verificato, è ora archiviato nel percorso indicato nel frontmatter. La struttura corrente è governata da `cap04/indice-4.1.md` e comprende introduzione e tredici file naturali di livello 3. Il giudizio non è stato trasferito ai nuovi documenti. Restano inoltre mancanti 13 dei 17 asset del manifest finale; quattro asset erano stati ripristinati da copie byte-identiche al manifest, mentre le versioni anteriori degli altri tredici non sono state usate come sostituti.

Sandro ha autorizzato il 4/8/2026 l'innalzamento di `max_giri` da 6 a 7. Un correttore distinto ha applicato esclusivamente la famiglia R06-01 e prodotto lo snapshot SHA-256 `93360710906737ff6a9c3d5f91b54e353282e2c1ab08d57deab099f7465d8964`.

Il settimo G6 integrale e cieco è stato superato con zero `ERR-MD`, zero `ERR-AUDIT`, zero `DUBBIO` e copertura 37/37 pagine. G7 è stato superato con manifest 21/21; le 136 unità dello scope sono state promosse a `COMPLETA/OK` e il master autonomo a `VC-OK al 2026-08-04`, senza promuovere `4`, `C4` o il corpus. Verbale e manifest finali sono in `verifica-conformita/`; evidenze del ciclo conclusivo in `_tmp_render/cap04/vc-paragrafo-4-1-20260804-r04/`.

## Istruzioni eseguite per il quarto G6

Scritte da CC il 31/7/2026 al momento della consegna. Non sostituiscono la procedura: il metodo sta in `../../../skills/conversione-normativa/references/ciclo-conversione-verifica.md` § 6 e § 7, che va letto integralmente. Qui stanno solo i fatti propri di questo scope.

**Chi.** Coordinamento a CDX. CC ha eseguito la fase correttiva e per il § 6.7 della procedura non può coordinare questo giro né giudicare i blocchi.

**Su cosa.** Snapshot `a04eabdedcdb7f4d112d61f4b97291e3881f4a583784f1edf7f42f0bf4d0bc03`, da riverificare prima di iniziare. Perimetro: D.M. pagine fisiche 74-95, Circolare pagine fisiche 85-99. Nella pagina 95 del decreto il § 4.2 è fuori scope; nella pagina 85 della Circolare i due capoversi generali del Capitolo C4 **sono** nel file e vanno considerati dentro il perimetro, perché la dichiarazione di scope va allineata a ciò che il file contiene davvero.

**Materiale già pronto, da non rifare.** Pagine fonte a 200 dpi in `_tmp_render/cap04/vc-paragrafo-4-1-20260730-r03/g6/fonte/ntc-pagine-200dpi/` e `circolare-pagine-200dpi/`; testo estratto di ausilio in `_tmp_render/cap04/vc-paragrafo-4-1-20260730-r03/g6-rerun-01/fonte/`. I ritagli a 600 dpi delle adjudicazioni già fatte sono in `.../g6-rerun-01/adjudica/` e servono a chi coordina, **non** ai verificatori ciechi.

**Cosa consegnare a ciascun verificatore di blocco.** Le immagini delle sue pagine, il testo estratto dichiarato non autorevole, l'intervallo di righe Markdown, le immagini collegate, e il § 5 della procedura come canone neutro delle tre classi. Senza il canone i verificatori segnaleranno come errori le tre note `AF-COR`, le tabelle a intestazioni vuote e il tag `\tag*{[4.1.44)}`, che sono tutte scelte legittime.

**Cosa non consegnare mai.** Conteggi attesi, rilievi dei giri precedenti, registro delle correzioni, annotazioni del capitolo, verbali, README, TODO, CHANGELOG, questa scheda.

**Partizione dei blocchi.** Va ridisegnata: la precedente aveva i confini alle pagine NTC 74-78, 79-81, 82-84, 85-88, 89-92, 93-95 e Circolare 85-87, 88-90, 91-93, 94-96, 97-99. Spostarli, così un punto cieco di bordo non ricade due volte nello stesso posto.

**Attenzione ai punti già toccati.** Undici righe sono state modificate il 31/7. Se un verificatore le segnala, prima di trattarle come rilievi vanno confrontate con `_tmp_render/cap04/vc-paragrafo-4-1-20260731-r01/correzione/registro-correzioni.md`: se la segnalazione ribalta un'adjudicazione già registrata, si applica la regola di non regressione del § 7, che richiede ritaglio a 600 dpi, lettura dei codepoint e conferma di un secondo verificatore prima di toccare il file.

**Render.** Usare `strumenti/render-capitolo.py`, che porta la macro dei tag e verifica da sé il risultato. Un render fatto a mano con pandoc reintroduce la difformità delle parentesi.

**Se il G6 passa.** Si procede a G7 e alla promozione dei registri, sulle sole 136 righe con prefisso `4.1` e `C4.1`, lasciando `4 / C4` a `VC-DA-FARE`. Se non passa, il budget è di nuovo esaurito: fermarsi e chiedere a Sandro.

## Diario

### 2026-08-26 - file aggregato archiviato e stato corrente riportato a DA_FARE (CDX)

Il § 4.1 è stato ricomposto in file naturali di livello 3. Il file verificato dal G7 resta conservato, byte-identico, in `_tmp_render/ricomposizione-livello3-20260826/archivio-file-sostituiti/cap04/4.1-calcestruzzo.md`; il nuovo insieme documentale non coincide con il vecchio manifest.

Le 136 unità correnti sono state pertanto riportate a `DA_FARE/NON_VALUTATO`, lasciando invariati `controllo_storico`, `snapshot_storico` ed `evidenza_storica`. Per un nuovo `VC-OK` occorrono il recupero degli asset mancanti e nuovi scope sui file naturali.

### 2026-08-26 - validità corrente scaduta per perdita di asset e variazione dell'indice (CDX)

L'audit delle cartelle vive ha accertato che il Markdown normativo è ancora byte-identico allo snapshot G7, ma tredici dei diciassette PNG certificati non sono più disponibili in tutto il workspace. Sono state ripristinate soltanto quattro copie con SHA-256 identico al manifest. Il file `cap04/indice-cap04.md`, incluso nel perimetro congelato, è inoltre cambiato dopo la ricomposizione editoriale del § 4.2.

Le 136 unità del registro sono state riallineate a `COMPLETA/SCADUTO`; le 136 righe dell'indice sono `VC-SCADUTA al 2026-08-26` e il master autonomo è stato ripristinato con lo stesso stato. Il verbale, il manifest e l'esito storico G0-G7 non sono stati alterati. Per una nuova promozione occorre recuperare o rigenerare dalla fonte e verificare i tredici asset, rieseguire G4-G5 e chiudere un nuovo G7.

### 2026-08-04 - settimo G6 e G7 superati, scope chiuso VC-OK (CDX)

Il settimo G6 integrale e cieco ha coperto 37/37 pagine mediante inventario fonte-prima e dieci blocchi in contesti separati. Inventario finale: 81 occorrenze di formule numerate, 23 gruppi matematici non numerati secondo il criterio dichiarato, 11 tabelle o griglie con 271 celle logiche e 17 figure. Dopo adjudicazione a 600 dpi, controllo dei codepoint e verifica del render risultano `ERR-MD=0`, `ERR-AUDIT=0`, `DUBBIO=0`. Il file normativo è rimasto invariato durante G6.

G7 ha validato il manifest definitivo su 21/21 file. Promosse 136/136 unità del registro e 136/136 righe dell'indice; la riga master autonoma è `VC-OK al 2026-08-04`, mentre il corpus resta `VC-DA-FARE`. Lint conclusivo: 0 errori, 0 avvisi e 195 informazioni. Non è stata eseguita una revisione umana integrale.

### 2026-08-04 - fase correttiva chiusa, settimo G6 avviato (CDX)

Il correttore distinto ha applicato esclusivamente R06-01 alla riga 993: inserita la sola virgola U+002C stampata dalla fonte dopo il primo `A_c`. Il diff aggiunge un byte, conserva 1957 righe e ricostruisce esattamente lo snapshot precedente rimuovendo il solo carattere inserito. Nuovo snapshot SHA-256 `93360710906737ff6a9c3d5f91b54e353282e2c1ab08d57deab099f7465d8964`.

Controlli post-correzione: lint con 0 errori e 0 avvisi; render rigenerato con il template dei tag; snapshot vivo e copia congelata hanno hash coincidenti. Avviato il settimo G6 integrale: `giro_g6` portato a 7. La fase fonte-prima è affidata a un agente fresco senza accesso al Markdown; la riconciliazione usa dieci blocchi da 3-5 pagine con confini spostati rispetto al sesto giro.

### 2026-08-04 - autorizzato il settimo giro, ripresa della fase correttiva (CDX)

Sandro ha autorizzato l'innalzamento di `max_giri` da 6 a 7 con il comando «ok.. vai», in risposta alla richiesta esplicita di autorizzazione al settimo giro. Le precondizioni di apertura sono state riverificate: hash delle due fonti ufficiali e dello snapshot Markdown coincidenti con quelli registrati, lucchetto ripreso legittimamente da CDX dal giorno precedente e nessun altro scope sul file `cap04/4.1-calcestruzzo.md`.

La fase correttiva è limitata alla sola famiglia R06-01, cioè il ripristino della virgola stampata dalla fonte dopo `A_c` alla riga 993. La correzione è affidata a un agente distinto; CDX conserva il coordinamento del prossimo G6 e non modifica direttamente il file normativo.

### 2026-08-03 - sesto G6 non superato, budget esaurito (CDX)

Completato il sesto G6 integrale e cieco sullo snapshot `5b0d4356251f0d42b35b0b84e65c7dc11a18b21bf4a14dd5e23497551d253e9c`, rimasto invariato durante il controllo. Inventario fonte-prima: 37 pagine, 81 occorrenze di formule numerate, 20 gruppi matematici non numerati, 11 tabelle o griglie con 315 celle logiche e 17 figure. La differenza dai conteggi del quinto giro è stata riconciliata per identità e criterio, senza oggetti mancanti.

Esito consolidato: una famiglia `ERR-MD` in un sito, zero `DUBBIO`, zero `ERR-AUDIT` e zero rilievi persistenti. Il rilievo R06-01 è la virgola omessa alla riga 993 dopo `A_c`; è confermato da ritaglio a 600 dpi, codepoint U+002C e confronto indipendente. La regola di non regressione sulla formula [C4.1.4] ha invece confermato `0.015` con punto. Render: 50 pagine, nessuna vuota, 81/81 tag corretti. Manifest G6 validato 56/56.

G7 non avviato e registri non promossi. Poiché `giro_g6: 6` coincide con `max_giri: 6`, lo scope è sospeso in attesa dell'eventuale autorizzazione di Sandro a un settimo giro. Evidenze: `_tmp_render/cap04/vc-paragrafo-4-1-20260803-r03/g6/04-rapporto-finale-g6-r06.md`, `05-manifest-sha256-g6-r06.txt` e `adjudicazione/00-adjudicazione-consolidata.md`.

### 2026-08-03 — fase correttiva chiusa, sesto G6 avviato (CDX)

Il correttore distinto ha applicato esclusivamente le 7 famiglie congelate, pari a 12 siti materiali. Il diff contiene 11 righe sostituite tutte autorizzate; la Figura C4.1.7 è stata riestratta dalla fonte a 600 dpi con cornice completa. Nuovo snapshot SHA-256 `5b0d4356251f0d42b35b0b84e65c7dc11a18b21bf4a14dd5e23497551d253e9c`; nuovo hash dell'asset `afa03b3760796055cecf16a315016fe087a719229797b0425ceefc6df1e3b730`.

Riallineati i soli tre `heading_md` tecnici interessati dai punti terminali ripristinati. Lint: 0 errori e 0 avvisi. Render: 50 pagine, nessuna vuota, controllo dei tag superato. Manifest correttivo validato 22/22. Evidenze in `_tmp_render/cap04/vc-paragrafo-4-1-20260803-r03/correzione/`.

Avviato il sesto G6 integrale: `giro_g6` portato a 6. La fase fonte-prima è affidata a un agente fresco senza accesso al Markdown; la riconciliazione usa dieci blocchi da 3-4 pagine con confini spostati rispetto al quinto giro e pacchetti che includono scansioni, testo assistivo, estratto Markdown, canone neutro e asset collegati.

### 2026-08-03 — autorizzato il sesto giro, ripresa della fase correttiva (CDX)

Sandro ha autorizzato l'innalzamento di `max_giri` da 5 a 6. Lo scope torna `IN-CORSO`; si procede con la fase correttiva limitata alle 7 famiglie `ERR-MD` congelate dal quinto G6, pari a 12 siti materiali, poi con i controlli post-correzione e un sesto G6 integrale sul nuovo hash. Il contatore `giro_g6` resta a 5 fino all'avvio effettivo del nuovo controllo.

La correzione è affidata a un agente distinto. CDX mantiene il ruolo di coordinatore del prossimo G6 e non applica direttamente le correzioni al file normativo.

### 2026-08-03 — quinto G6 non superato, budget esaurito (CDX)

Completato il quinto G6 integrale e cieco sullo snapshot `a1df27fd79c2ef946256cae1e12fcf41d0d542d96e71676382aab8c5382b6700`, rimasto invariato durante la verifica. Inventario fonte-prima: 37 pagine, 81 occorrenze di formule numerate, 21 gruppi matematici esposti non numerati, 11 tabelle o griglie con 304 celle logiche e 17 figure.

Esito consolidato dopo adjudicazione a 600 dpi e controllo dei codepoint: 7 famiglie `ERR-MD` per 12 siti materiali, zero `DUBBIO`, zero `ERR-AUDIT` e zero rilievi persistenti. L'iniziale difetto di confezionamento dei blocchi, privi delle pagine fonte, è stato rilevato prima del congelamento, sanato con la ripetizione integrale dei nove confronti su pacchetti completi e chiuso senza lacune residue. Nessuna correzione normativa è stata applicata durante il G6.

G7 non avviato e registri non promossi. Poiché `giro_g6: 5` coincide con `max_giri: 5`, lo scope è sospeso in attesa dell'autorizzazione di Sandro a un eventuale sesto giro. Evidenze: `_tmp_render/cap04/vc-paragrafo-4-1-20260803-r02/g6/04-rapporto-finale-g6-r05.md`, `05-manifest-sha256-g6-r05.txt` e `adjudicazione/00-adjudicazione-consolidata.md`.

### 2026-08-03 — fase correttiva chiusa, quinto G6 avviato (CDX)

Il correttore distinto `collation_c2` ha applicato le 43 famiglie congelate, pari a 61 siti materiali, senza rilievi non applicabili. Il confronto meccanico con lo snapshot precedente mostra 60 righe modificate, tutte autorizzate e nessuna estranea; la differenza fra righe e siti dipende da due correzioni sulla stessa riga.

Nuovo snapshot SHA-256 `a1df27fd79c2ef946256cae1e12fcf41d0d542d96e71676382aab8c5382b6700`. Allineato il solo `heading_md` tecnico della riga `NTC-4.1.2.1.2`; registrate permanentemente le nuove anomalie `AF-4.1-04` e `AF-4.1-05`; stati ed esiti del registro invariati. Lint: 0 errori e 0 avvisi. Render: 49 pagine, nessuna vuota, controllo dei tag superato. Evidenze e manifest in `_tmp_render/cap04/vc-paragrafo-4-1-20260803-r02/correzione/`.

Avviato il quinto G6 integrale: `giro_g6` portato a 5. La nuova fase fonte-prima è affidata a un agente fresco senza accesso al Markdown né agli esiti pregressi; la partizione dei blocchi verrà nuovamente ridisegnata.

### 2026-08-03 — autorizzato il quinto giro, ripresa della fase correttiva (CDX)

Sandro ha autorizzato l'innalzamento di `max_giri` da 4 a 5. Lo scope torna `IN-CORSO`; si procede con la fase correttiva limitata alle 43 famiglie `ERR-MD` congelate dal quarto G6, poi con i controlli post-correzione e un quinto G6 integrale sul nuovo hash. Il contatore `giro_g6` resta a 4 fino all'avvio effettivo del nuovo controllo.

Per rispettare la separazione dei ruoli del § 6.7, la correzione viene affidata a un agente distinto; CDX conserva il ruolo di coordinatore del prossimo G6 e non modifica il file normativo.

### 2026-08-03 — quarto G6 non superato, budget esaurito (CDX)

Completati inventario fonte-prima e dieci blocchi ciechi su 37/37 pagine. Dopo adjudicazione a 600 dpi e, per un dubbio, sui codepoint della fonte, risultano 43 famiglie `ERR-MD` per 61 siti materiali; zero `DUBBIO` e zero `ERR-AUDIT` aperti. Formule numerate 81/81, tabelle fonte 11/11, celle logiche 274 più una vuota strutturale, figure 17/17. Il file normativo non è stato modificato e conserva SHA-256 `a04eabdedcdb7f4d112d61f4b97291e3881f4a583784f1edf7f42f0bf4d0bc03`.

G7 non avviato e nessun registro promosso. Il quarto giro coincide con `max_giri: 4`: scope sospeso in attesa dell'autorizzazione di Sandro per un quinto G6, da precedere con una fase correttiva limitata ai rilievi congelati. Evidenze: `_tmp_render/cap04/vc-paragrafo-4-1-20260803-r01/g6/04-rapporto-finale-g6-r04.md` e `05-manifest-sha256-g6-r04.txt`.

### 2026-08-03 — quarto G6 preso in carico (CDX)

Precondizioni di apertura verificate sul W520: lucchetto libero, nessun altro scope sul file `cap04/4.1-calcestruzzo.md`, prompt storico già consumato, hash delle due fonti ufficiali e dello snapshot Markdown coincidenti con quelli registrati. Avviato il quarto G6 integrale e cieco autorizzato da Sandro il 31/7/2026.

### 2026-07-31 — autorizzato il quarto giro, scope consegnato a CDX (CC)

Sandro ha autorizzato l'innalzamento di `max_giri` da 3 a 4, per consentire il G6 successivo alla fase correttiva, e ha scelto di aprire il lavoro su Codex.

Scheda riportata a `LIBERO` perché CDX possa prenderla in carico senza urtare il lucchetto. Il contatore `giro_g6` resta a 3 e va portato a 4 da chi esegue il controllo. Istruzioni di consegna nella sezione qui sopra.

### 2026-07-31 — fase correttiva, undici rilievi chiusi (CC)

Eseguita dopo la ratifica di Sandro sulle due decisioni di indirizzo: regime della classe C e politica di resa dei tag.

Snapshot iniziale `a05a99c00f13bc7e95b499f1136c927e0a0ffa19d9289e8b3ff77ee326f2acb4`, finale `a04eabdedcdb7f4d112d61f4b97291e3881f4a583784f1edf7f42f0bf4d0bc03`. Evidenze in `_tmp_render/cap04/vc-paragrafo-4-1-20260731-r01/`.

Chiuso anche il dubbio rimasto dal G6: la dicitura «dove:» è effettivamente presente nel riquadro di formule della Fig. C4.1.9, quindi è diventata l'undicesimo rilievo e la sua omissione è stata sanata.

| rilievo | classe | intervento |
|---|---|---|
| G6-01 tag `[4.1.44)` | A | ripristinata la parentesi tonda della fonte, resa letterale con `\tag*` |
| G6-02 `Σ A₁` | A | ripristinata la cifra della fonte in tutte e tre le occorrenze; annotazione dedicata |
| G6-03 `T_ed`/`V_ed` | C | conservata la forma corretta, aggiunta la nota `AF-COR-4.1-02` |
| G6-04 `N_Eϕ` | C | conservata la forma corretta, aggiunta la nota `AF-COR-4.1-01` |
| G6-05 sommatoria [4.1.12.f] | — | rimossi gli estremi non presenti in fonte |
| G6-06 `Δσμ` | C | conservata la forma corretta, aggiunta la nota `AF-COR-4.1-03` |
| G6-07 «per il rapporto» | — | testo della fonte ripristinato |
| G6-08 «frattile 5%» e «frattile 95%» | — | diciture della fonte ripristinate |
| G6-09 tabella mandrini | — | rimosse le intestazioni inventate, ripristinato «per» |
| G6-10 tabella `α_c` | — | rimosse le intestazioni inventate |
| G6-D1 «dove:» Fig. C4.1.9 | — | dicitura della fonte ripristinata |

Controlli superati: diff di 32 righe corrispondenti una a una ai rilievi e a nulla d'altro; 81 formule numerate con la sola duplicazione di fonte del tag `[4.1.50]`; unico tag a resa letterale `[4.1.44)`; 139 heading, 17 immagini, 14 tabelle; tre note `AF-COR` presenti e corrispondenti alle tre annotazioni; lint del registro 0 errori e 0 avvisi.

Attuata anche la seconda decisione ratificata: creato `strumenti/render-capitolo.py`, che porta la macro di resa dei tag e verifica da sé il risultato. Render post-correzioni di 49 pagine, nessuna pagina vuota, 93 tag resi con le quadre della Gazzetta e il tag anomalo `[4.1.44)` riprodotto alla lettera.

Non eseguiti in questa fase, perché non di competenza della fase correttiva: nuovo G6, G7, promozione dei registri.

### 2026-07-30 — terzo G6, non superato (CC)

Undici verificatori ciechi per blocchi di pagine fonte, adjudicazione a 600 dpi e sulla codifica dei caratteri. Esito: 10 `ERR-MD` e 1 `DUBBIO`, `ERR-AUDIT=0`. Rapporto in `_tmp_render/cap04/vc-paragrafo-4-1-20260730-r03/g6-rerun-01/04-rapporto-finale-g6.md`.

### 2026-07-30 — secondo G6 e correzione, entrambi con esito viziato (CDX)

Il G6 r02 lesse `[4.1.44]` a 500 dpi e la correzione conseguente fece divergere il file dalla fonte. È il caso da cui nasce la regola di non regressione.

### 2026-07-30 — primo G6 e G0-G5 (CDX)

Evidenze in `_tmp_render/cap04/vc-paragrafo-4-1-20260730-r01/` e `r02/`.
