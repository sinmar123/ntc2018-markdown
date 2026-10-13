# Changelog - NTC 2018

## 2026-10-01 - Sito pubblico su GitHub Pages, licenze e modello di segnalazione, CC cloud

- Su richiesta di Sandro (`ntc2018-261001-prompt-cloud-sito.md`), sul ramo `claude/lucid-ramanujan-so88m5` e con pull request. Nessun file di `cap*/`, del registro, della procedura o del `README.md` di radice è stato toccato.
- Nuovi: `strumenti/costruisci-sito.py` (copia `cap*/` in `_sito/docs/` e solo nella copia aggiunge il riquadro di stato letto dal registro tramite `apri_md`; genera la pagina iniziale dal registro e la navigazione in ordine di `n.`), `strumenti/controlla-sito.py` (controlli sull'HTML generato), `strumenti/sito/` (modello `mkdocs.yml`, configurazione MathJax con i tag fra parentesi quadre di `_preambolo-tag.tex`, foglio di stile, `requisiti.txt`), `.github/workflows/sito.yml` (costruzione a ogni push su `main` e a ogni pull request, pubblicazione su Pages solo da `main`), `.github/README.md`, `LICENSE` (CC BY 4.0 per la conversione, testo delle norme escluso per l'art. 5 L. 633/1941), `strumenti/LICENSE` (MIT), `.github/ISSUE_TEMPLATE/errore-di-trascrizione.yml`.
- Registro ricontato: 379 righe, 43 `VC-OK`, 289 `MAI-FATTA`, 34 `DA-RICONFERMARE`, 9 `DA-RIFARE`, 4 `IN-CORSO`, uguali al prompt.
- Controlli: `mkdocs build --strict` senza avvisi; 502 pagine HTML per 502 file `.md` di `cap*/`; riquadri 43/289/34/9/4 come il registro più 123 «stato non registrato»; nessuna `<img>` rotta nel sito; `git diff --stat main -- 'cap*/'` vuoto; MathJax provato in Chromium su §§ 2.5.3, 3.4.4, 4.2.4 e 7.3.1 (678 formule su 678 composte nel § 4.2.4, zero errori di MathJax, tag `[2.5.1]`).
- Trasformazioni della sola copia, oltre al riquadro: 495 rimandi a `../indice-ntc2018.md` puntano a una pagina generata; 12 collegamenti a `verifica-conformita/` e a cartelle `img/` portati su GitHub; 6 collegamenti a `_tmp_render/` e a cartelle `img/` inesistenti lasciati come testo; 230 riferimenti a 115 figure assenti dal repository (cap02 1, cap04 41, cap05 25, cap07 46, cap11 2) sostituiti da un avviso. Nessuna pagina `VC-OK` ha figure mancanti.
- Difetti nei capitoli, da correggere con la procedura VC: 314 `\tag{...}` scritti dopo i `$$` di chiusura in 46 file (33 `MAI-FATTA`, 13 non registrati; nessun `VC-OK`), che nel sito escono come formula in linea seguita da `$ \tag{...}` alla lettera; 4 rimandi a note scritti dopo i `$$` di chiusura, sulla stessa riga della formula, in `cap03/3.3-vento.md`, `3.3.1` e `3.3.2`; 7 ancore degli indici che non trovano il titolo (`cap05/indice-cap05.md` 4, `cap11/indice-cap11.md` 2, `cap03/annotazioni/tab-c3.3.i-refuso-cu.md` 1), declassate a INFO nella configurazione.
- Non verificato: la pubblicazione vera su Pages, che parte dopo l'unione in `main` e con Pages impostato su «GitHub Actions»; il caricamento di MathJax dal CDN, bloccato dalla rete di questa sessione (provato con la stessa versione presa da npm); il riconoscimento della licenza da parte di GitHub, perché `LICENSE` rimanda al testo legale CC BY 4.0 invece di riportarlo (il sito di Creative Commons non è raggiungibile da qui).
- Modelli: tutto il lavoro nella sessione (Opus); nessuna VC, nessun subagente.
- 2026-10-12: aggiunto `ntc2018-261012-prompt-chrome-github.md`, il prompt per Claude su Chrome che attiva Pages, crea l'etichetta delle segnalazioni, unisce la PR #1 dopo conferma di Sandro e controlla il sito; contiene anche lo stato per ripartire.

Prossima azione: Sandro rivede la pull request, attiva Pages con sorgente «GitHub Actions» e unisce; il W520 riporta in locale e scrive la voce di giornale. Poi: recuperare o estrarre le 115 figure mancanti e aprire uno scope VC per i `\tag` fuori dai `$$`.

## 2026-10-01 - Preparato il repository pubblico su GitHub, CC (P53)

- Sandro userà i 250 USD di credito delle sessioni cloud di Claude Code (scadenza 5/11/2026) anche per la conversione aperta a tutti. Sua scelta: si pubblica tutto, ciascun paragrafo con il suo stato di verifica in vista. La cartella diventa la copia di lavoro sul W520 del repository `sinmar123/ntc2018-markdown`, non ancora creato.
- Nuovi: `.gitignore` (fuori `raw/`, `_tmp_render/`, `old/`, `.agents/`, i prompt consumati o in corso, immagini e pdf delle evidenze tranne i due PDF della Gazzetta), sezione «Sessione cloud» in `CLAUDE.md`, `PROMPT-IN-CORSO-ntc2018-repository-pubblico.md` per il W520 e `ntc2018-261001-prompt-cloud-sito.md` per la prima sessione cloud.
- Controllo dei dati personali sui file pubblicabili: solo indirizzi di assistenza della Gazzetta e dell'IPZS, nessuna chiave, nessun numero di telefono.
- Nessun file dei capitoli, del registro o della procedura è stato toccato.
- Repository locale creato sul W520 da CC via ssh dal P53 (prompt preso in carico): commit `76e1aef`, 1.300 file (619 dei capitoli, 657 delle verifiche, gli altri di governo e strumenti), 76,7 MiB. Le sole immagini e i soli pdf sono le 117 figure dei capitoli e i due PDF della Gazzetta. Aggiunto `.gitattributes` con `* -text`: il W520 ha `core.autocrlf=true` di sistema, e senza quella riga git avrebbe cambiato i finali di riga, e con loro l'impronta dei file verificati; controllato con `git ls-files --eol` che i byte restano quelli del disco.
- Non ancora su GitHub: sul W520 la chiave di `gh` è scaduta, e da ssh git non raggiunge le credenziali.

Prossima azione: Sandro, dallo schermo del W520, rinnova `gh auth login` e lancia `gh repo create sinmar123/ntc2018-markdown --public --source . --push`; poi si chiude `PROMPT-IN-CORSO-ntc2018-repository-pubblico.md` dal § 4. Resta da chiarire se la VC con quattro righe `IN-CORSO` nel capitolo 8 è ferma.

## 2026-09-30 - VC-OK del solo § 8.3, NormaNTC18 (OC)

- VC-OK su `8.3-valutazione-sicurezza.md`, NTC pp. 294-295 e Circolare 255-256. R1 e R2 applicati. G6 con un ERR-MD (spazio in terreno-fondazione) corretto e ricontrollato sul ritaglio a 600 dpi. Il rapporto integrale era in /tmp ed è perso, non ricostruito. Il verificatore del ritaglio ha rifiutato il G7 sull'intero scope. Sandro ha ordinato la registrazione («Ok vai»). Snapshot `4edeaeea47bddd2fd20f85f96df429f5236993b55b69033c8122a968de2a03e6`. [Verbale](verifica-conformita/verbale-VC-ntc2018-8.3-2026-09-30.md). Firma: NormaNTC18 (OC).

Prossima azione: Nessuna sul file: VC conclusa sullo snapshot registrato.

## 2026-09-30 - Nuovo esecutore NormaNTC18 su OpenClaw, CC

- Creato su richiesta di Sandro l'agente OpenClaw `normantc18` (NormaNTC18, Grok 4.7), dedicato alle sole NTC e Circolare con `PROCEDURA-VC.md`; istruzioni in `ai/openclaw-sandroai/agenti/normantc18/`. Prende il posto di Hermes NTC-VC, che resta installato.
- Resa canonica nel container OpenClaw: pandoc 3.12 e TinyTeX. Prova su `cap03/3.2.3-azione-sismica-valutazione-dell-azione-sismica.md`, con PDF scritto in `/tmp` del container, fuori dal corpus, e controlli di tag e didascalie superati.
- Prova breve dell'agente: `vc-supporto.py avvio` senza scope, in sola lettura, riporta come unico scope in corso il § 8.3, lucchetto GROK dal 13/9, in attesa della decisione di Sandro su R1 e R2.
- Nessun file del corpus, registro o scheda toccato.
- **`PROCEDURA-VC.md` alla revisione 6**, su richiesta di Sandro: profili OpenClaw al § 5, con modelli leggeri per E e per le attività brevi: prima `openai/gpt-5.6-luna` in abbonamento, per scelta di Sandro, e `openrouter/deepseek/deepseek-v4.1-flash` se Luna non risponde o se la quota del piano si consuma troppo. Cinesi ammessi perché il testo normativo è pubblico. La tabella è stata corretta in giornata, prima che qualunque scope adottasse la revisione. Criteri, gate, catalogo e canone G6 invariati: il canone risulta identico byte per byte alla revisione 5, archiviata in `old/PROCEDURA-VC-r05-20260912.md` con lo SHA-256 `658d9834…` che le schede già registrano. `vc-supporto.py avvio` legge la revisione nuova senza errori. Firma: CC.

Prossima azione: primo scope di NormaNTC18, breve, scelto da Sandro; il § 8.3 resta a GROK finché Sandro non decide su R1 e R2 o non lo passa.

## 2026-09-13 - VC § 8.3, elenco di due ERR-MD per Sandro, GROK

- Presa del solo `8.3-valutazione-sicurezza.md`, NTC pp. 294-295 e Circolare 255-256, 8.2 e 8.4 esclusi. G0/G1/G4 OK; G2-G3 KO. NTC conforme. Circolare: due ERR-MD di presentazione (rubrica C8.3, capoversi fusi). Target invariato, G5/G6 non avviati. [Elenco](_tmp_render/cap08/vc-8.3-20260913-grok/rapporto-c.md), [scheda](verifica-conformita/scheda-scope-ntc2018-8.3.md). Firma: GROK.

Prossima azione: Attendere la decisione di Sandro su R1 e R2 del § 8.3.

## 2026-09-12 - Introduzioni 3.2, 3.3 e 3.4 VC-OK e capitolo 3 completato, CDX

CDX: introduzioni 3.2, 3.3 e 3.4 VC-OK, VC-NTC/5 - semplificata. Correzioni approvate e tre figure ripristinate; G0-G7 OK, G6 al primo giro 32/32, quattro falsi positivi esclusi e un pedice corretto con riscontro mirato, zero residui. Pagine della Circolare non rilevate automaticamente nel vecchio inventario: riferimenti verificati nel verbale. Registro solo CSV. Firma: Codex / CDX.

Confronto con NTC pp. fisiche 49, 56, 61 e Circolare 46-47, 54, 76: sette gruppi approvati, tre figure ripristinate; G6 originario 32/32, quattro falsi positivi esclusi mediante ritagli/font/codepoint/posizioni, una regressione di pedice nella didascalia b corretta e verificata dallo stesso V. Solo pagina 2 della resa modificata, nessun secondo G6 integrale. [Verbale](verifica-conformita/verbale-VC-ntc2018-introduzioni-3.2-3.4-2026-09-12.md), [manifest](verifica-conformita/vc-ntc2018-introduzioni-3.2-3.4-2026-09-12/manifest-rilascio.json), [annotazioni](cap03/annotazioni/3.2-introduzione-anomalie-fonte.md). Chiusura G7 nello stesso V b01, zero residui; consumi non consolidati. CSV e file di governo allineati tramite strumento comune; controllo finale nella ricevuta. Il capitolo 3 è completo per tutti i 40 file del registro; altri scope e corpus conservano i propri stati.

Prossima azione: Nessuna sul capitolo 3: tutti i file del registro sono VC-OK. Attendere un nuovo incarico prima di aprire altri scope.



## 2026-09-12 - VC-OK del solo § 8.2, GROK

- VC svolta insieme da Sandro e GROK. Solo `8.2-criteri-generali.md`, NTC p. 294 e Circolare 254-255. R1-R3 e nota 1 sistemati insieme; G6 indipendente escluso da Sandro. Snapshot `69158160ab7980444f6c3e9157b82020dfaa71eb158d3db651799a0dd314ffb5`. [Verbale](verifica-conformita/verbale-VC-ntc2018-8.2-2026-09-12.md). Firma: GROK.

Prossima azione: Nessuna sul file: VC conclusa sullo snapshot registrato.

## 2026-09-12 - Introduzioni 3.2, 3.3 e 3.4: confronto iniziale e lista da approvare, CDX

Sandro ha autorizzato insieme le tre introduzioni residue 3.2, 3.3 e 3.4. CSV: tre righe IN-CORSO nello scope `3-introduzioni-3.2-3.4`, procedura VC-NTC/5 semplificata. Target iniziali e fonti congelati; un solo C Sol high per il confronto iniziale. Confronto iniziale completato: G0-G1 OK, G2-G4 con sette gruppi di non conformità. Preparati 15 interventi testuali esatti e tre PNG da ripristinare dalla fonte vettoriale a 600 dpi; occorrenze e percorsi controllati. [Elenco unico per Sandro](_tmp_render/cap03/vc-introduzioni-3.2-3.4-20260912-cdx/rapporto-c.md), [lista applicabile](_tmp_render/cap03/vc-introduzioni-3.2-3.4-20260912-cdx/lista-correzioni.json). Target invariati, correzioni e G5-G7 non avviati. Firma: Codex / CDX. [Scheda](verifica-conformita/scheda-scope-ntc2018-3-introduzioni-3.2-3.4.md), [lavorazione](_tmp_render/cap03/vc-introduzioni-3.2-3.4-20260912-cdx/). Firma: Codex / CDX.

Il ritardo nella consegna era dovuto a un comando superfluo di rigenerazione delle prove rimasto bloccato, interrotto conservando le prove già valide. Nessun nuovo verificatore o giro G6; consumi non consolidati. Presa mediante strumento comune e controllo CSV riusciti; scheda aggregata storica 3.3 conservata. Fonti ufficiali congelate e preparate come pagine leggibili, testo ausiliario separato.

Prossima azione: Attendere l’approvazione di Sandro sui sette gruppi di correzioni delle introduzioni 3.2, 3.3 e 3.4; poi applicare la lista e completare G5-G7.


## 2026-09-12 - Correzioni R1-R3 del § 8.2, senza G6, GROK

- Sandro ha approvato le tre correzioni e ha escluso ulteriori ripassate. Applicati rubrica `C8.2 CRITERI GENERALI`, capoversi della Circolare e nota ¹. Snapshot `d3f24e03a1b4035da657dee0cab3e3f591af47f1cbfdab8a7833d490667b29e2`. G6 non eseguito. Firma: GROK.

Prossima azione: Registrare VC-OK del § 8.2 se Sandro lo richiede.

## 2026-09-12 - VC § 8.2, elenco di tre ERR-MD per Sandro, GROK

- Presa del solo `8.2-criteri-generali.md`, NTC p. 294 e Circolare 254-255, 8.1 e 8.3 esclusi. G0/G1/G4 OK; G2-G3 KO. NTC conforme. Circolare: tre ERR-MD di presentazione (rubrica C8.2, capoversi fusi, nota a piè). Target invariato, G5/G6 non avviati. [Elenco](_tmp_render/cap08/vc-8.2-20260912-grok/rapporto-c.md), [scheda](verifica-conformita/scheda-scope-ntc2018-8.2.md). Firma: GROK.

Prossima azione: Attendere la decisione di Sandro su R1, R2 e R3 del § 8.2.

## 2026-09-12 - Registro soltanto CSV e cancellazione XLSX, CDX

CDX: eliminata su ordine di Sandro la vista registro-verifica-conformita-ntc2018.xlsx. Rimossa la rigenerazione XLSX automatica da presa e chiusura VC; procedura revisione 5, con metodo semplificato della revisione 4 invariato. Aggiornati riferimenti operativi e indice; revisione 4 conservata byte per byte. CSV invariato. Firma: Codex / CDX.

Verifica mirata: XLSX assente, CSV invariato byte per byte; sintassi dello script valida e nessun richiamo al generatore XLSX nelle operazioni automatiche. Canone G6 invariato. [Revisione 4 archiviata](old/PROCEDURA-VC-r04-20260912.md). Nessun nuovo controllo normativo.

Prossima azione: Nessuna su questa modifica; alle prossime VC usare soltanto il registro CSV.

## 2026-09-12 - Colonne procedura e agente sulla riga § 8.1, GROK

- Allineata la sola riga `8.1`: `procedura_vc` = `VC-NTC/4 - semplificata`, `agente_vc` = `Grok (GROK)`. Le altre righe non toccate. XLSX non rigenerato.

Prossima azione: Nessuna sul file: VC conclusa sullo snapshot registrato.

## 2026-09-12 - Introduzione 3.1 VC-OK, procedura semplificata e agente nel registro, CDX

CDX: sola introduzione 3.1 registrata VC-OK con VC-NTC/4 - semplificata; due correzioni di presentazione approvate da Sandro, G0-G7 OK, G6 integrale al primo giro 2/2, zero residui. Colonne procedura_vc e agente_vc aggiunte; Codex (CDX) per 3.1, Grok (GROK) per 8.1 da scheda. XLSX escluso su richiesta. Firma: Codex / CDX.

Confrontate integralmente le due rubriche con le pagine fisiche 46 dei PDF ufficiali NTC e Circolare; C e V concordi, G6 2/2 e zero residui. [Verbale](verifica-conformita/verbale-VC-ntc2018-3.1-2026-09-12.md), [evidenze](verifica-conformita/vc-ntc2018-3.1-2026-09-12/). Aggiunte colonne con migrazione additiva nello strumento comune: nessuna attribuzione storica automatica; Grok riscontrato nella scheda 8.1. Aggiornati linter e generatore XLSX, 31 test superati, inclusi rifiuto delle attribuzioni discordanti e conservazione delle altre righe. Lint finale riportato nella ricevuta; XLSX non rigenerato.

Prossima azione: Nessuna sulla sola introduzione 3.1: VC conclusa. Attendere un nuovo via libera prima di aprire altri scope.

## 2026-09-12 - VC-OK del solo § 8.1, GROK

- Solo `cap08/8.1-oggetto.md`, NTC p. 294 e Circolare 253-254, 8.2 escluso. G0-G7 OK, VC-NTC/4: confronto integrale G6 R02 14/14 e controllo localizzato dei due corsivi C8.1. Snapshot `80a2c5a3af47c879dda192b43e7a729fd81a9c30fd5a53407cb2a4c08bdd832b`. [Verbale](verifica-conformita/verbale-VC-ntc2018-8.1-2026-09-12.md).
- Nessun nuovo G6 integrale dopo le correzioni. Consumi non disponibili. Firma: GROK.

Prossima azione: Nessuna sul file: VC conclusa sullo snapshot registrato.

## 2026-09-12 - Introduzione 3.1, primo confronto VC-NTC/4 e lista per Sandro, CDX

- Presa autorizzata della sola riga 3.1; sottoparagrafi 3.1.1-3.1.4 esclusi. Il vecchio verbale 3.1.1 non comprende l'introduzione. C Sol high ha confrontato integralmente le rubriche sulle pagine fisiche 46 di NTC e Circolare: due ERR-MD di sola presentazione, maiuscole dei titoli e punto aggiunto dopo C3.1. Nessuna prosa o apparato introduttivo presente nella fonte; G0/G1/G4 OK, G2-G3 KO.
- [Rapporto e tabella](./_tmp_render/cap03/vc-3.1-introduzione-20260912-cdx/rapporto-c.md), lista JSON e ritagli a 600 dpi conservati nella lavorazione; [scheda](verifica-conformita/scheda-scope-ntc2018-3.1.md) aggiornata. Target invariato, nessuna correzione e nessun G6 prima della decisione di Sandro. G1 riusato dal 2026-09-09 con ricontrollo mirato 2026-09-12; un solo contesto C, nessun E o V.
- Corretto il blocco globale di `prendi`, che impediva la presa per la presenza del § 8.1 in corso: ora verifica la disgiunzione dei target secondo la procedura. Test 29/29, incluso rifiuto del target condiviso prima di qualsiasi scrittura e conservazione della riga concorrente; lint senza errori. Primo tentativo rifiutato prima di scrivere, poi presa completata. XLSX non toccato su richiesta. Firma: Codex / CDX.

Prossima azione: Attendere la decisione di Sandro sulle due correzioni delle rubriche della sola introduzione 3.1.

## 2026-09-12 - § 3.6 registrato VC-OK su ordine di Sandro, CDX

- Quattro righe (`3.6`, `3.6.1`, `3.6.2`, `3.6.3`) registrate `VC-OK` il 2026-09-12, su giudizio G0-G7 positivo del 2026-09-11. G6 al giro 2/3, copertura 117/117, zero rilievi normativi e snapshot invariato. Rettifiche amministrative chiuse secondo VC-NTC/4; XLSX invariato su richiesta di Sandro. Firma: CDX.
- Riutilizzati G7 r02 e manifest congelato; rettificata nel verbale la dicitura sulle cinque correzioni r02 emerse dal G6 r01, dichiarati i consumi non consolidati. Nessun nuovo agente o giro di verifica.
- Registro e file di governo allineati tramite la funzione comune di registrazione; lint separato per omettere la rigenerazione XLSX esclusa da Sandro. Gli altri file conservano i propri stati. Firma: Codex / CDX.

Prossima azione: Nessuna sul § 3.6: VC conclusa. Attendere un nuovo via libera prima di aprire altri scope.



## 2026-09-12 - Procedura VC revisione 4, riduzione dei ricontrolli autorizzata da Sandro, CDX

- Aggiornata la sola procedura attiva dopo il consumo di circa il 20% della quota settimanale Pro riferito da Sandro: elenco unico delle non conformità, decisione o correzione manuale dell'utente, sostituzioni esatte tramite script. Primo confronto completo e G6 indipendente integrale conservati.
- Dopo il G6, una tornata correttiva approvata e un solo controllo delle modifiche e dei loro effetti. Parti invariate coperte dalle prove precedenti; rilievi residui restituiti a Sandro, senza nuovi giri automatici. Controllo esteso soltanto sul perimetro invalidato o interessato, dopo decisione esplicita. Il verbale distingue confronto integrale e ricontrollo localizzato.
- Ridotti i passaggi di coordinamento e chiusura: nessun agente per sostituzioni esatte, registri o consumi; nessuna nuova revisione normativa per refusi dei rapporti o contatori mancanti. La rendicontazione amministrativa non blocca la conformità documentata.
- Conservata byte per byte la [revisione 3](old/PROCEDURA-VC-r03-20260909.md); allineati README, TODO, indice e rinvio nella specifica degli strumenti. Canone dei §§ 3-4 e catalogo invariati. Nessun corpus, stato CSV, lucchetto o prova congelata modificato. Firma: Codex / CDX.

- Verifica: 28/28 test degli strumenti esistenti superati; archivio r03 identico all'impronta originaria, canone e catalogo invariati, quattro target § 3.6 coincidenti con il manifest congelato. Collegamenti controllati; quattro righe § 3.6 e riga § 8.1 ancora `IN-CORSO`.

Prossima azione: Applicare la revisione 4 alla prossima ripresa autorizzata, conservando le verifiche valide e presentando solo i residui.

## 2026-09-12 - Corsivi C8.1 del § 8.1 applicati, GROK

- Accolti i due `ERR-MD` del G6 R02: corsivo su *Le costruzioni esistenti* e sui due virgolettati NTC; corsivo su *struttura completamente realizzata*. Snapshot `80a2c5a3af47c879dda192b43e7a729fd81a9c30fd5a53407cb2a4c08bdd832b`.
- Il § 8.2 resta escluso. Serve G5 e G6 R03 sul target corretto.

Prossima azione: G5 sul target corretto e G6 R03 integrale sul solo § 8.1; 8.2 escluso.

## 2026-09-11 - Sessione § 3.6 registrata e fermata prima della chiusura VC, CDX

- Confrontati i quattro Markdown con nove pagine ufficiali, dieci formule numerate e quattro tabelle; applicate 43 correzioni in due tornate e conservate cinque anomalie della fonte, senza AF-COR. Resa canonica finale di dieci pagine.
- G0-G5 `OK`; secondo G6 integrale `OK`, 117/117 elementi e zero rilievi normativi. G7 positivo, con manifest verificato 349/349. Snapshot `cd6a442021675c0bbaa29641f10551506f88cbbba0363759a981ef1f67ade672`; [evidenze conservate](verifica-conformita/vc-ntc2018-3.6-2026-09-11/) e [scheda](verifica-conformita/scheda-scope-ntc2018-3.6.md). Verifiche svolte da agenti AI, senza revisione umana integrale; isolamento V istruttivo e tracciato.
- Il controllo C del piano finale ha lasciato due questioni documentali: consumi ancora da consolidare e motivazione G7 da precisare come cinque correzioni r02 emerse dal G6 r01. Il [verbale predisposto](verifica-conformita/verbale-VC-ntc2018-3.6-2026-09-11.md) richiede allineamento prima della registrazione.
- Stop esplicito di Sandro rispettato; nessuna registrazione finale applicata, quattro righe CSV ancora `IN-CORSO`. Registrata la sessione nei file di governo, conservando le voci concorrenti GROK. Il piano `chiusura-config.json` in lavorazione resta una traccia non applicata: alla ripresa occorre rigenerarlo sui file correnti. Firma: Codex / CDX.

Prossima azione: Alla ripresa autorizzata, completare le due rettifiche documentali del § 3.6 e rigenerare il piano di registrazione prima della chiusura VC.

## 2026-09-11 - VC del solo § 8.1 avviata e sospesa dopo G6 R02, GROK

- Perimetro autorizzato: primo paragrafo del capitolo 8, 8.2 escluso. Un file, NTC p. 294 e Circolare 253-254. Presa parallela al § 3.6 su file disgiunti; le quattro righe 3.6 non toccate.
- G0-G5 `OK`. G6 R01 `KO` su tre `ERR-MD` di Circolare: omissione di `CAPITOLO` nel titolo C8 e fusione dei capoversi C8 e C8.1. Correzioni applicate; snapshot `d0654c34b2c31614d2a6cb72398a82f627fffd27cecfd9a9fbec95d701c7fc75`.
- G6 R02 chiuso `KO` dopo la richiesta di fermarsi: 14/14 ID, due `ERR-MD` di corsivo in C8.1, target non ritoccato. G7 non avviato. [Scheda](verifica-conformita/scheda-scope-ntc2018-8.1.md), lavorazione `_tmp_render/cap08/vc-8.1-20260911-grok/`.

Prossima azione: Adjudicare i due corsivi C8.1 del G6 R02; 8.2 escluso.

## 2026-09-11 - Registro VC allineato a capitoli x e sezioni x.y, GROK

- Inserite 68 righe canoniche mancanti: capitoli 1 e 12, tredici sezioni autonome senza figli di livello 3, 53 introduzioni `x.y`. Il CSV passa da 311 a 379 righe, una per ciascun file normativo vivo indicizzato in `capXX/`.
- Ordine gerarchico da `1` a `12`. Contenuto delle tre righe `3.6.1`-`3.6.3` invariato salvo il progressivo `n.`. Aggiunte `3.5-introduzione` come `VC-OK` (stesso verbale dello scope aggregato) e `3.6-introduzione` come `IN-CORSO` sulla scheda CDX.
- Linter: nomi `x` / `x.y` / `x.y.z`, indice interno obbligatorio solo sui 311 `x.y.z`, annotazioni escluse. `genera-indici-interni.py` resta sui 311 file di livello 3. Test `test_vc_supporto.py` 28/28. Vista XLSX rigenerata dopo la chiusura del file: 379 righe, 11 colonne, 461 collegamenti, conforme al CSV.
- Backup del CSV precedente in `_tmp_render/audit-registro-gerarchia-20260911/`. Pagine delle nuove righe vuote, senza valori presunti. 35 residui pre-ricomposizione restano fuori dal registro.

Prossima azione: CDX include la riga `3.6` nella registrazione dello scope in corso.

## 2026-09-11 - Avvio VC dell'intero § 3.6, Codex / CDX

- Presa unica autorizzata da Sandro: introduzione e file naturali 3.6.1-3.6.3, NTC pp. fisiche 66-71 e Circolare 81-83. Nove pagine, dieci formule numerate, quattro tabelle, nessuna figura nel dimensionamento C. Nessun lucchetto concorrente; tre righe portate da `MAI-FATTA` a `IN-CORSO`, G6 0/3.
- Copie iniziali dei quattro target, impronte dei due PDF e procedura VC-NTC/3 e catalogo congelati in `_tmp_render/cap03/vc-3.6-20260911-cdx/`. Ricognizione G1 riusata dal 2026-09-09 con ricontrollo ufficiale mirato 2026-09-11; C Sol high avviato per giudizio e confronto integrale, distinto da eventuale E e dai futuri V.
- La presa ha scritto CSV e scheda e superato il lint; la rigenerazione della vista XLSX ha incontrato `PermissionError` sul file in uso. Ricevuta originaria conservata, nessun rilancio della presa. È stato chiesto di liberare il file mentre la verifica prosegue.

Prossima azione: Completare G1-G5 e avviare G6 integrale indipendente sul § 3.6.

## 2026-09-11 - VC-OK dell’intero § 3.5, Codex / CDX

- Confrontati integralmente gli otto Markdown e i due asset con NTC pp. fisiche 63-66 e Circolare p. 81. G6 al giro 2/3: 36/36 gruppi localizzabili, otto formule, tre tabelle, due figure; G0-G7 `OK`, zero rilievi residui. Manifest 133/133; [verbale](verifica-conformita/verbale-VC-ntc2018-3.5-2026-09-11.md).
- Corretti da E Terra medium i sei rilievi del primo G6: refuso e punteggiatura conservati secondo la fonte in 3.5.2, figura 3.5.1 completa, tre celle logiche della Tab. 3.5.I, parola `termiche` nel capoverso C3.5. Creata l’annotazione `AF-3.5.2-01` con àncora e rinvio portabili. La precedente adjudicazione R7 è stata ribaltata con ritaglio a 600 dpi, dati vettoriali e secondo lettore Astra xhigh fonte-only concorde.
- C Sol high ha confrontato l’applicazione esatta della lista e verificato visivamente tutte le cinque pagine del render canonico. V Sol xhigh fresco ha chiuso il nuovo G6 e G7; una rettifica documentale separata precisa raster nativi e metadati, mantenendo invariati target e input congelati. Natura AI e assenza di revisione umana integrale dichiarate nel verbale.
- Dossier definitivo `verifica-conformita/vc-ntc2018-3.5-2026-09-11/`; preservati tentativi Hermes, G6 precedente, diff e snapshot. G1 riusato dal 2026-09-09 con ricontrollo ufficiale mirato 2026-09-11. Profili effettivi, consumi disponibili e limiti del confronto col § 3.4.5 registrati nella scheda.
- Registrazioni tramite `vc-supporto.py registra`: sette righe promosse, 31 `VC-OK` su 311; master del corpus ancora `VC-DA-FARE`. Lint e XLSX verificati; indici interni 311 file e 1754 collegamenti validi. Nessuna modifica alla procedura viva o agli altri scope.
- Recupero della registrazione: le otto scritture della ricevuta erano tutte complete; il linter si era fermato perché il collegamento diretto all’annotazione nell’indice generale veniva interpretato come file normativo aggiuntivo. Il rinvio è stato portato all’indice editoriale delle annotazioni. Completati senza rilanciare `registra`: lint a zero errori e avvisi, XLSX conforme al CSV su 311 righe e 388 collegamenti. Conservata la ricevuta originaria con integrazione di recupero. Prompt di ripresa chiuso come `PROMPT-CONSUMATO-VC-3.5-G6-CODEX.md`.

Prossima azione: Attendere un nuovo via libera prima di aprire il § 3.6 o altri scope.

## 2026-09-11 - Subentro CDX sul § 3.5 e preparazione del G6 nativo

- Codex / CDX: su richiesta esplicita di Sandro preso in carico `PROMPT-IN-CORSO-VC-3.5-G6-CODEX.md` e assunto il lucchetto dell'unico scope aggregato. Conservati snapshot, sette righe IN-CORSO, cronologia HRM, `giro_g6: 0` e `max_giri: 3`.
- Adeguata la consegna al canale nativo Codex con restrizione istruttiva e letture controllate, secondo § 7; Sol high per C e Sol xhigh per V, E distinto se necessario. Non è un terzo rilancio del trasporto Hermes. Recuperati gli esiti originali SSE R01b/R01d, entrambi senza inventario e senza target rivelato; tre vecchi pacchetti preservati.
- Snapshot vivo 10/10 e impronte di due PDF fonte, composito e sei file della resa confermati. Nuova lavorazione in `_tmp_render/cap03/vc-3.5-20260911-cdx/`, pacchetto cieco in Temp esterna. Riaperta la ricognizione ufficiale per il ricontrollo mirato G1; giudizio C in corso.

Prossima azione: concludere il riscontro C di G0-G5 e il collaudo del canale nativo, quindi fonte-prima G6 con V Sol xhigh indipendente.


## 2026-09-11 - Ricognizione della procedura dopo le sessioni Hermes (CDX)

- Codex / CDX, su richiesta di Sandro prima della ripresa: confrontati procedura vigente, copia R01 del § 3.4.4, copia R03 ed errata del § 3.4.5, registrazioni Hermes, CSV, scheda del § 3.5 e prompt di subentro. Nessuna presa in carico del prompt o dello scope e nessuna nuova verifica MD-PDF eseguita.
- La procedura vigente è VC-NTC/3 del 2026-09-09, byte-identica alla R03 congelata del § 3.4.5: SHA-256 `4bd4440a6f9b204338e97ecf78c9bb74ab0d9e04f7478b9c97c436c62e817c7c`. Canone §§ 3-4 identico alla R01; catalogo corrente SHA-256 `d71319206ec54bcac3639dfd0b97c41754fa1062655b2d35c36ee5d6cb3036d6`, coincidente con la scheda del § 3.5. Tabella dei modelli invariata; le modifiche comuni riguardano soprattutto coordinamento, unità di scope a sezione, riuso G1 e registrazione tramite script. Renderer nel container e canale V sono adattamenti dell'esecuzione Hermes.
- Residui documentali riscontrati: § 2 della procedura viva cita ancora `VC-NTC/2`, già rettificato separatamente nelle evidenze del § 3.4.5; README/TODO riportano ancora nessun altro scope autorizzato e README descrive il renderer come esterno al container, superato dalle registrazioni del 2026-09-10; le prossime azioni delle sette righe CSV del § 3.5 sono ferme a G0-G5, mentre la scheda registra G5 OK e blocco tecnico G6. Il prompt Codex conserva percorsi Docker e impone V nel container Hermes, vincolo più stretto del § 7 comune: non è ancora una consegna per esecuzione interamente nativa Codex.
- Stato riscontrato: § 3.4.5 `VC-OK`; sette righe § 3.5 `IN-CORSO`, scheda HRM con `giro_g6: 0`, G6 `BLOCCATO-TECNICO` per due tentativi SSE falliti prima dell'inventario e G7 non iniziato. Nessuna modifica a procedura, prompt, corpus, registri, schede o prove congelate; registrata soltanto questa ricognizione nel CHANGELOG e nel giornale.

Prossima azione: prima della ripresa VC del § 3.5, allineare la consegna al runtime Codex e risolvere i residui documentali rilevati; questa ricognizione non avvia il subentro o il G6.

## 2026-09-11 - Prompt di subentro Codex per la VC del § 3.5 (HRM)

- Hermes NTC-VC / HRM: creato e riletto integralmente `PROMPT-RIPRESA-VC-3.5-G6-CODEX.md`, con subentro esplicito CDX sullo stesso scope aggregato, stato G0-G5, snapshot e confini verificati.
- Il prompt conserva `giro_g6: 0`, distingue i trasporti morti R01/R01c dai fallimenti SSE R01b/R01d e vieta un terzo tentativo identico prima del collaudo tecnico previsto dal § 8.
- Inclusi chiusura atomica delle sette righe, separazione di V, dossier G7 e confronto finale con il § 3.4.5. Nessun target o registro è stato modificato.

Prossima azione: Codex prende in carico `PROMPT-RIPRESA-VC-3.5-G6-CODEX.md` col gestore dei prompt e riprende dal blocco tecnico G6.

## 2026-09-11 - § 3.5 G6 sospeso per errore tecnico ripetuto (HRM)

- Hermes NTC-VC / HRM: R01d ha avviato il contesto V fresco `20260911_115402_4831e6`, ma è terminato prima dell'inventario con lo stesso errore SSE già restituito da R01b, dopo tre retry.
- Nessun target è stato rivelato, nessun giro G6 è consumato e `giro_g6` resta 0. R01 e R01c sono trasporti morti, non esecuzioni V.
- Il § 8 impone di sospendere dopo due tentativi tecnici effettivi consecutivi con la stessa anomalia. G6 è bloccato tecnicamente; G7 non è iniziato e le sette righe restano `IN-CORSO`.

Prossima azione: Sospendere nuove richieste V; Sandro decide come gestire il blocco tecnico SSE.

## 2026-09-11 - § 3.5, richiesta fonte-prima ridisposta dopo trasporto morto (HRM)

- Hermes NTC-VC / HRM: riclassificata la richiesta `vc-35-g6-r01-fonte-prima` come tentativo di trasporto morto prima dell’avvio di V: la macchina si è spenta dopo il marcatore `.preso`, senza inventario, esito o log.
- Nessun giro G6 è consumato; `giro_g6` resta 0. Il pacchetto fonte-prima e lo snapshot sono invariati.
- Depositata con nome nuovo `vc-35-g6-r01b-fonte-prima` sullo stesso blocco immutato.

Prossima azione: Attendere l'esito della richiesta V `vc-35-g6-r01b-fonte-prima`; non aprire G7.

## 2026-09-11 - § 3.5 G5 OK, G6 bloccato senza esito (HRM)

- Hermes NTC-VC / HRM: verificati sugli artefatti i 15 interventi E e le due figure; sessioni E separate `20260910_185522_efe78c` e `20260910_193518_2d97d6`, runtime `gpt-5.6-terra / openai-codex / medium`.
- G5 R02 `OK`: resa canonica di cinque pagine aperta integralmente, zero tagli, sovrapposizioni o capoversi fusi; snapshot aggregato `1728b7d061dd7b7ddcd3ea34ef395759084293efcbb592a5201b56bb5ac29a9c`.
- La richiesta V fonte-prima R01 è stata presa alle `2026-09-10T19:47:05+02:00`, ma dopo il riavvio del container non esistono esito o inventario. Non è stata ripetuta. G6 non giudicato, G7 non iniziato, sette righe ancora `IN-CORSO`.

Prossima azione: Attendere un esito esplicito del canale V sulla richiesta fonte-prima già presa; non ripetere la richiesta.

## 2026-09-10 - § 3.4.5, rettifica append-only n. 1 del verbale (HRM)

- Hermes NTC-VC / HRM: aggiunta una rettifica separata al verbale originario, rimasto immutato, con dichiarazione della natura AI delle attività C/E/V, assenza di revisione umana integrale e isolamento reale del verificatore.
- Registrata `AF-3.4.5-01`: la Circolare, pagina fisica 81, omette il punto fermo dopo `1 W/m²K°`; il target conserva la fonte ed è invariato. Aggiunti gli URL ufficiali degli atti.
- Il solo G7 R07 ha chiuso `OK`, zero rilievi, sul manifest delta SHA-256 `93e838f8f5ecd8c17e512c25282992289d0177792dc209b4710de0d0df471984`; giudizio SHA-256 `f09086de9625ede5807f4f8ea64a38bc70b6ef6101d3166e119482ce15cc3b47`. G6 non è stato rifatto e lo stato resta `VC-OK`.

Prossima azione: Nessuna sul file: VC conclusa sullo snapshot registrato.

## 2026-09-10 - § 3.4.5 VC-OK (HRM)

- Hermes NTC-VC / HRM: chiusa la VC-NTC/3 del solo § 3.4.5 sullo snapshot `3541307932ff82abd016c34b325b6bb11877315ae8cc1db320b57d925cb7ebd5`.
- G6 `OK` al giro 2/3 dopo rettifica append-only della sola delimitazione di `CIRC81-PRO-001`; G7 finale R06 `OK`, zero rilievi. Manifest di 67 file SHA-256 `e338cac1d900f68473c48e30f7dfe11a6070cd4abf4649d8faf39415759a4586`; giudizio G7 `bafadafecdc3001439ba5d26523e72a0fd6aab1195e79d23159aa7d6cf1d937e`.
- Verbale: `verifica-conformita/verbale-VC-ntc2018-3.4.5-2026-09-10.md`. Registro aggiornato esclusivamente con `vc-supporto.py registra`; nessun altro scope aperto.

Prossima azione: Nessuna sul file: VC conclusa sullo snapshot registrato.

## 2026-09-10 - § 3.4.5 G7 R04 OK (HRM)

- Hermes NTC-VC / HRM: V ha verificato l'evidenza esterna dell'impronta e ha emesso G7 `OK`; G0-G7 tutti `OK`, zero rilievi aperti.
- Manifest R03 SHA-256 `17a29d8ea850ef95cbf07a0e242c8e59392cf2e85eb138c9b1ecf7062e97145a`, 54 file e integrità `OK`; giudizio G7 SHA-256 `ef41f4c27a5134149f0aefcb3419924e76d9d2c091094de1f59485cf5bf81aea`.
- Target, fonti, asset e G6 sono rimasti invariati. Il registro resta `IN-CORSO` fino al rilascio atomico; nessun altro scope è autorizzato.

Prossima azione: eseguire il rilascio atomico VC-OK sullo snapshot registrato; nessun altro scope è autorizzato.

## 2026-09-10 - G7 R02 del § 3.4.5 KO-AUDIT (HRM)

- Hermes NTC-VC / HRM: il manifest R02, SHA-256 `db94e1930760c2de0c8bc077983a7366d67aafff689606ec65c56d81e5cfe4cd`, ha chiuso i tre rilievi R01. Giudizio R02 `KO`, SHA-256 `44dca2a727a36a4bf522a7224e3515667bdb57039bab5a477a423367ee62e916`.
- Restano due `ERR-AUDIT`: hash del manifest R01 trasposto come `04bd73…` anziché `04db73…`; richiamo interno `procedura: VC-NTC/2` rimasto nel § 2 della procedura identificata come R3.
- Adjudicazione C: rettifiche append-only e nuovo manifest, senza modifica di target, fonti, asset o G6. CSV non modificato a mano.

Prossima azione: rettificare append-only i due difetti, generare il manifest R03 e riaprire il solo G7.

---

## 2026-09-10 - G7 R01 del § 3.4.5 KO-AUDIT (HRM)

- Hermes NTC-VC / HRM: dossier G7 R01 generato e verificato, 42 file, manifest SHA-256 `04bd73b18947bd364331d32afa58f1008179acd181c906975106b6b643132f74`, non usato per chiusura; V ha ripreso la sessione isolata `20260909_165403_00ba4e` e ha emesso `KO`.
- Tre `ERR-AUDIT`: copia VC-NTC/2 inserita nel manifest al posto della VC-NTC/3; confine successivo indicato `C3.4.5.1` anziché `C3.5`; normalizzazioni del rapporto iniziale citate N01/N03/N10 anziché N2/N1. Target, fonti, asset e G6 invariati.
- Adjudicazione C: recupero documentale append-only secondo § 8, nuovo manifest e riapertura del solo G7; nessun nuovo G6. Rapporto G7 R01 conservato con SHA-256 `15054f77dbce3082431d96fa11fcdbb382a7d5804d7936708276204bd2867c20`. CSV non modificato a mano.

Prossima azione: rettificare append-only le tre incongruenze documentali del G7 R01, generare un nuovo manifest e riaprire il solo G7; G6 e target restano invariati.

---

## 2026-09-10 - G6 del § 3.4.5 OK dopo rettifica append-only (HRM)

- Hermes NTC-VC / HRM: ricostruito lo stato del solo § 3.4.5 con `vc-supporto.py avvio 3.4.5` dopo la ricreazione del container; procedura, catalogo, target e fonti ricalcolati con hash coincidenti.
- Rapporto G6 R03 validato: 11/11 ID, fonti, testo, PDF e PNG confrontati integralmente; zero `ERR-MD` e dubbi, un solo `ERR-AUDIT` descrittivo su `CIRC81-PRO-001`. Il rapporto originario resta immutato, SHA-256 `8c0282e4a2bd5383e714e3220a794fa08be17ca9afac4e2af8073664b89f911d`.
- Adjudicazione C secondo §§ 7-8: rettifica append-only della sola mappatura, senza terzo giro. Lo stesso V, sessione `20260909_165403_00ba4e`, ha verificato il delta e dichiarato rettifica `OK`, rilievo `CHIUSO` e G6 post-rettifica `OK`; zero residui, giro 2/3. CSV non modificato a mano. G7 non avviato.

Prossima azione: preparare nel blocco R03 le evidenze di chiusura del § 9 e richiedere al medesimo V il giudizio G7; non aprire altri scope.

---

## 2026-09-09 - Inventario G6 R03 congelato, testo e render rivelati (HRM)

- Hermes NTC-VC / HRM: acquisito l'inventario fonte-prima autonomo della sessione V fresca `20260909_165403_00ba4e`, 11 elementi su 2 pagine, 4 esclusioni, nessun dubbio, esito `LEGGIBILE`; nessun target era presente prima della rivelazione.
- Validazione schema `OK`; inventario, esito e canone congelati prima della creazione di `testo.md` e della copia degli asset target. Inventario SHA-256 `70fc44ed20f24ecf4b67b1ad242d457ca9e2299b9721852eccc7e4521a6865d2`.
- Manifest del confronto R03 con 11 file, SHA-256 `880b71f0ba7fd08fda1b99a2589065d08753fdc3472bdef73aa9a8ab0fae05a8`, integrità `OK`. PDF e PNG coincidono con le impronte del G5 R02. Il confronto non è avviato; recupero nel giro 1/3. CSV non modificato a mano.

Prossima azione: riprendere sull'host la sessione V `20260909_165403_00ba4e` per il confronto G6 R03 sul blocco `/opt/data/vc-ntc-3.4.5-g6-r03/b01`, compresa la cartella `resa-target`; produrre `rapporto-g6.json` e fermarsi, senza avviare G7.

---

## 2026-09-09 - G6 R02 del § 3.4.5 KO-AUDIT e blocco sostitutivo R03 (HRM)

- Hermes NTC-VC / HRM: acquisito e validato il rapporto originario G6 R02, SHA-256 `f88f6eca515d68422cbdbcece83e98ef8ffc3624721d77bfb3022f654231bb50`: copertura 11/11, normalizzazioni 1 e 2, confronto integrale, isolamento pulito, un solo `ERR-AUDIT` per assenza della resa target nel manifest. Nessuna difformità del corpus accertata; `giro_g6` 1/3.
- Adjudicazione C: niente integrazione post-confronto né rettifica del rapporto. R02 resta immutato; recupero con blocco sostitutivo e V fresco nello stesso giro, sul medesimo snapshot.
- Esteso `strumenti/vc-supporto.py` con `blocchi[].assets`: nome portabile, sorgente interna al progetto, SHA-256 obbligatorio, occultamento fino al congelamento e inclusione verificata nel manifest di confronto. Documentazione aggiornata; suite sintetica 26/26 `OK`.
- Predisposto `/opt/data/vc-ntc-3.4.5-g6-r03/b01`: sei soli input fonte, senza target. Il coordinamento esterno congela PDF e PNG del render G5 R02 da rivelare successivamente. Il CSV non è stato modificato a mano.

Prossima azione: avviare sull'host un nuovo V in contesto fresco per la sola fase fonte-prima del blocco sostitutivo `/opt/data/vc-ntc-3.4.5-g6-r03/b01`; fermarsi dopo `inventario.json`, senza rivelare il target.

---

## 2026-09-09 - § 3.4.5 adottata VC-NTC/3, inventario G6 congelato e target rivelato (HRM)

- Hermes NTC-VC / HRM: adottata prima del confronto G6 la revisione 3, SHA-256 `4bd4440a6f9b204338e97ecf78c9bb74ab0d9e04f7478b9c97c436c62e817c7c`. Il canone resta identico al pacchetto, 8705 byte e SHA-256 `546023234aec119b42de98bb7499187fdb8445f1ac83e5b32743e13174c1eb44`; nessun rifacimento del blocco.
- Inventario fonte-prima del V isolato, sessione `20260909_145740_bd7dee`, validato: 11 elementi, 2 pagine, 4 esclusioni, nessun dubbio, esito `LEGGIBILE`. Congelati inventario, esito e canone prima della creazione di `testo.md`; verifica del pacchetto `OK`, 9 file.
- V non ha ancora aperto il target, quindi il confronto non è iniziato e `giro_g6` resta 0. Il CSV non è stato modificato a mano.

Prossima azione: riprendere sull'host la sessione V `20260909_145740_bd7dee` per il confronto G6 sul blocco `/opt/data/vc-ntc-3.4.5-g6-r02/b01`; produrre `rapporto-g6.json` e fermarsi, senza avviare G7.

---

## 2026-09-09 - Procedura alla revisione 3, dalla misura del § 3.4.5 (CC)

Motivo. La revisione 2 doveva misurarsi sui consumi al primo scope autorizzato. Quella misura in token non esiste: il runtime di Hermes non espone i contatori, e la scheda del § 3.4.5 lo dichiara. Si è misurato il tempo: due capoversi di norma e uno di Circolare hanno occupato un pomeriggio, dalle 13:23 alle 16 senza arrivare al G6. Di quel tempo l'esecutore ha lavorato 73 minuti in tre tranche; il resto sono i due passaggi di consegna verso l'operatore per il render canonico, uno dei quali di 35 minuti. E dei 73 minuti la verifica delle due pagine è una frazione: il resto è attrito, cioè tre tentativi dell'estrattore G0, `copy2` che non passa sul filesystem condiviso, l'eseguibile `hermes` fuori dal PATH, il renderer senza `--help`, un punto e virgola scritto a mano nel CSV letto come dodicesima colonna, PIL assente, il pacchetto a 200 dpi rifatto a 600, più le ricerche su Gazzetta Ufficiale per accertare la vigenza di due atti che non cambiano.

Modifiche, tutte fuori dal canone congelato del G6.

- § 2, unità di scope: l'unità ordinaria diventa la **sezione** `x.y` e non più il singolo file naturale, restando dentro i limiti di dimensionamento già previsti. Il file singolo resta legittimo quando è l'ultimo della sezione o quando la sezione eccede i limiti. L'attrito di apertura, G1, confezionamento e chiusura non si riduce con la lunghezza del paragrafo.
- § 6, G1: la ricognizione congelata è riusabile fino a **trenta giorni** e non più solo in giornata, con un **ricontrollo mirato** sugli aggiornamenti di ciascun atto al posto della ricerca piena. Oltre i trenta giorni, o se il ricontrollo segnala un aggiornamento, si rifà tutto.
- § 9, verbale: quando il G1 è riusato, la vigenza si dichiara con **due date**, ricognizione e ricontrollo, mai con la data del verbale.
- § 9, registrazioni: il CSV **non si modifica a mano**, nemmeno per una riga. Il comando quota i campi, una patch no.

Verifica. Il canone del G6, cioè i §§ 3 e 4 fra i marcatori `CANONE-G6`, non è stato toccato, e neppure il catalogo delle normalizzazioni. `neutral_canone()` rigenerato dopo le modifiche dà 8705 byte e sha256 `546023234aec119b42de98bb7499187fdb8445f1ac83e5b32743e13174c1eb44`, identico al `canone.md` già confezionato nel blocco `/opt/data/vc-ntc-3.4.5-g6-r02/b01`: il pacchetto resta valido e non va rifatto. Nuovo hash della procedura: `4bd4440a6f9b204338e97ecf78c9bb74ab0d9e04f7478b9c97c436c62e817c7c`. Lo scope § 3.4.5 è in corso con G6 non iniziato e `giro_g6` a 0, quindi adotta la revisione 3 al prossimo gate non iniziato, come prevede il § 1.

Fuori procedura, sulla quarta voce di attrito: pandoc 3.11 e TeX Live 2026 sono stati installati nel volume dati del container di Hermes NTC-VC, non nell'immagine, così il renderer canonico gira dove lavora l'esecutore e il passaggio di consegna sparisce. Provato sul § 3.4.5: stesse font, stessa struttura, stesso testo del render dell'host, con soli ritorni a capo diversi perché le due installazioni TeX non sono la stessa versione. Ha effetto alla ricreazione del container, rinviata a scope chiuso.

Prossima azione: avviare sull'host il verificatore V isolato per la sola fase fonte-prima G6 del § 3.4.5, consegnandogli esclusivamente `/opt/data/vc-ntc-3.4.5-g6-r02/b01`.

---

## 2026-09-09 - G5 R02 del § 3.4.5 OK e blocco fonte-prima G6 predisposto (HRM)

- Hermes NTC-VC / HRM: target ricalcolato sullo snapshot `3541307932ff82abd016c34b325b6bb11877315ae8cc1db320b57d925cb7ebd5`; render host R02 riuscito senza warning, tag fra parentesi o didascalie automatiche.
- Riscontro visivo integrale positivo: rubriche, prosa, simbolo romano con `t` a pedice, valori, unità, punteggiatura e tre capoversi della Circolare conformi; nessun glifo mancante, taglio o sovrapposizione. G5 `OK`, zero rilievi aperti.
- Registrata la compressione runtime delle 14:54 come secondo contesto e secondo tentativo di C. Il primo pre-pacchetto G6 a 200 dpi resta non consegnato; il blocco destinato a V, con pagine a 600 dpi e senza target, è `/opt/data/vc-ntc-3.4.5-g6-r02/b01`. G6 non avviato.

Prossima azione: avviare sull'host il verificatore V isolato per la sola fase fonte-prima G6, consegnandogli esclusivamente `/opt/data/vc-ntc-3.4.5-g6-r02/b01`; fermarsi dopo `inventario.json`, senza rivelare il target.

---

## 2026-09-09 - G5 R01 del § 3.4.5 respinto, capoverso corretto e render R02 richiesto (HRM)

- Hermes NTC-VC / HRM: verificati direttamente hash, PDF e raster del render host R01. Cassa, simbolo con pedice, valori, unità, punteggiatura restante e leggibilità erano conformi; nessun warning, tag con parentesi tonde o didascalia automatica.
- Il controllo visivo ha aperto `ERR-MD-G5-01`: la fonte ha tre capoversi nella Circolare, mentre Markdown e render R01 fondevano i primi due. G5 R01 è `KO`; G6 non è stato avviato.
- E distinto ha inserito soltanto il capoverso fra `in linea generale.` e `Laddove adeguatamente motivato`, senza altre differenze. Ricollazione post-correzione e G3-G4 ripetuti `OK`, zero rilievi aperti. Nuovo snapshot `3541307932ff82abd016c34b325b6bb11877315ae8cc1db320b57d925cb7ebd5`.
- Indici verificati su 311 file e 1754 collegamenti; registro a zero errori e zero avvisi, XLSX conforme al CSV. Consegna R02 in `_tmp_render/cap03/vc-3.4.5-20260909/richiesta-operatore-g5-r02.md`.

Prossima azione: eseguire sull'host il render canonico G5 R02 del solo § 3.4.5 sullo snapshot `3541307932ff82abd016c34b325b6bb11877315ae8cc1db320b57d925cb7ebd5` e restituire PDF, PNG a 200 dpi ed esito; non avviare G6.

---

## 2026-09-09 - § 3.4.5 corretto e ricollazionato, fermo al render G5 sull'host (HRM)

- Hermes NTC-VC / HRM: completati G0-G2 sul solo § 3.4.5. Il confronto iniziale G3-G4 ha aperto quattro `ERR-MD`: cassa della rubrica NTC, stile romano di `C_t`, cassa e punto spurio della rubrica C3.4.5, punto spurio dopo `1 W/m²K°`.
- Il ruolo E separato ha applicato soltanto le quattro sostituzioni chiuse; C ha ricollazionato il target. G3-G4 ripetuti `OK`, zero rilievi aperti. Snapshot corrente `4527c114103e513df46c7deb497471aeb995f2bf2a4907e652678dc047e79f19`.
- Indici interni verificati su 311 file e 1754 collegamenti; il manifest dell'operazione registra un solo file complessivamente mutato e 311 corpi invariati. Registro: zero errori e zero avvisi; XLSX conforme al CSV. Corretto `strumenti/genera-indici-interni.py` per copiare nello snapshot i soli byte con `copyfile`, evitando l'errore `EPERM` di `copy2` sui metadati del filesystem condiviso.
- G5 non completato: il renderer canonico arriva all'invocazione di `pandoc`, assente nel container insieme a `xelatex` e `pdftoppm`. Consegna host in `_tmp_render/cap03/vc-3.4.5-20260909/richiesta-operatore-g5.md`. G6 e G7 non avviati; il registro resta `IN-CORSO`.

Prossima azione: eseguire sull'host il render canonico G5 del solo § 3.4.5 sullo snapshot `4527c114103e513df46c7deb497471aeb995f2bf2a4907e652678dc047e79f19` e restituire PDF, PNG a 200 dpi ed esito; non avviare G6.

---

## 2026-09-09 - Apertura VC del solo § 3.4.5 (HRM)

- Hermes NTC-VC / HRM: ricevuta l'autorizzazione di Sandro, preso in carico `PROMPT-IN-CORSO-VC-3.4.5.md` e aperta la scheda-lucchetto del solo file naturale `cap03/3.4.5-neve-coefficiente-termico.md`.
- Registro portato da `MAI-FATTA` a `IN-CORSO`. Confini preliminari accertati sulle pagine fisiche NTC 63 e Circolare 81; ricalcolate le impronte delle due fonti ufficiali, del target, della procedura VC-NTC/2 e del catalogo.
- Snapshot iniziale `b6b467482175546c91509ef8f76489039357e5a0c08de54d677991e81fdc154c`. Nessuna modifica al testo normativo; G0-G1 in corso, G2-G7 non ancora chiusi. Nessun altro scope autorizzato.

Prossima azione: completare G0-G5 sul solo § 3.4.5; se occorrono correzioni, applicarle tramite E distinto.

---

## 2026-09-07 - Hermes NTC-VC acceso e provato sulla meccanica, nessuna VC avviata (CC)

- Il coordinatore preparato da HRM è installato e collegato sul W520 come @hermesntcbot: cronaca, comandi e riscontri nel CHANGELOG di `ai/ai-ag-hermes/`. Qui restano aggiornati README e indice, e la procedura non cambia di una riga.
- Provato che `vc-supporto.py avvio` senza scope risponde `NON_UNIVOCA` con `in_corso` vuoto, senza scritture e senza prendere lucchetti. Nessun registro, contatore o stato del corpus è stato toccato.
- Il confezionamento fonte-prima gira ora anche dal container, dopo l'installazione di `PyMuPDF` e `openpyxl` nel volume dati dell'agente. Il render canonico del § 6 punto 7 no: pandoc, XeLaTeX e poppler restano fuori dall'immagine e quel passo si esegue sull'host.
- G6 provato su una norma sintetica inventata, fuori dal corpus e dai registri, con una discrepanza piantata di proposito: il verificatore isolato l'ha trovata insieme ad altre tre differenze e ha chiuso `KO` su 12 elementi coperti. Reggono separazione dei ruoli, cecità sul target, rivelazione differita e isolamento in lettura, che qui è una sandbox vera e non solo istruttiva. Non regge la continuità del contesto fra le due fasi chiesta dal § 7: `--resume` apre una sessione nuova, e il verificatore ricostruisce l'inventario dal file congelato.
- **Controllo cieco sul § 3.1.1, in sola lettura e senza effetti sul progetto.** Il paragrafo è `VC-OK` dal 27/8 e la fonte congelata e lo snapshot del Markdown hanno ancora gli hash del suo verbale, quindi il materiale è lo stesso. Un verificatore isolato, che non ha visto il verbale, ha censito sei elementi con quattro esclusioni coincidenti con i confini dichiarati allora e ha chiuso `esito: OK` con zero rilievi, citando le due normalizzazioni del catalogo: la stessa conclusione del G6 del 27/8, per una via diversa. Serviva a sapere se il meccanismo regge su materiale vero e non solo su una norma inventata. **Non è una VC e non produce alcun giudizio**: pacchetto, inventario e rapporto stanno fuori dal workspace, nella cartella dati dell'agente. Riscontrato dopo che registro, target e prompt sono rimasti quelli di prima.
- Nessuna prova sintetica diventa `VC-OK` di alcuna norma, e il § 3.4.5 resta da avviare.
- Test della scrittura: su richiesta di Sandro il bot ha aggiunto una voce di prova in cima a questo CHANGELOG, firmata HRM e con la riga `Prossima azione`, e la corrispondente voce di giornale con la sua sigla. Riscontrati i due file veri: la voce era in cima e non in fondo, la firma giusta, la voce di giornale esistente e non solo annunciata. La riga di prova è stata poi rimossa da CC, per non lasciare un finto precedente nel registro del progetto. Emersi due difetti dei container Hermes, non di questo progetto: le voci di giornale portano l'ora UTC, quindi due ore indietro rispetto a quelle di CC e OC, e il campo `macchina` registra l'id del container, che cambia a ogni ricreazione.
- Test dello scope implicito rifatto senza ordini dentro, «il 3.4.5 come sta messo?»: ha risposto con lo stato e basta, e i suoi dati sono stati riscontrati sul disco, cioè `MAI-FATTA`, NTC pagina 63 e Circolare pagina 81, nessuna scheda di scope, nessun lucchetto, prompt ancora attivo. Nel passaggio ha segnalato una riga arretrata di questo README, che al § 3.4 dava 3.4.4 e 3.4.5 come non aperti mentre il 3.4.4 è `VC-OK` dal 5/9 e la riga di testa lo diceva già: corretta, ora distingue il 3.4.4 concluso dal solo 3.4.5 da avviare.
- Alle 18:18 il bot, provando gli arresti, ha preso in carico `PROMPT-RIPRESA-VC-3.4.5.md` e lo ha rinominato `IN-CORSO`. Non è un errore suo: «riprendiamo la VC del 3.4.5» è l'innesco che `AGENTS.md` prescrive, e il § 3.4.5 risulta autorizzato e `MAI-FATTA` nel registro; si è fermato prima del G0 e ha riferito lo stato in modo esatto. Era il test a essere ambiguo. Riscontrato che nella cartella è cambiato quel solo file, senza toccare registro, lucchetti, schede o testo normativo; su decisione di Sandro il prompt è stato riportato ad attivo e l'intestazione di presa in carico rimossa, perché nessun lavoro era cominciato. Lo strumento dei prompt non ha un comando per annullare una presa in carico: si è fatto a mano e si è riscontrato con `stato`.

Prossima azione: nessuna su questo progetto. La ripresa VC resta quella di `PROMPT-RIPRESA-VC-3.4.5.md`, su richiesta di Sandro.

---

## 2026-09-07 - Preparato il coordinatore Hermes NTC-VC, nessuna VC avviata (HRM)

- Hermes / HRM: su richiesta di Sandro, predisposti nel progetto `ai/ai-ag-hermes/` profilo, SOUL, compose autonomo e prompt per l'attivazione locale del nuovo agente. README e indice NTC collegano la scheda; la sola procedura operativa rimane `PROCEDURA-VC.md`.
- Il profilo rinvia al routing e all'indipendenza della procedura, senza imporre max. Richiede il collaudo di input, contesto e continuità del verificatore: la conversazione fresca della delegazione Hermes può comunque ereditare istruzioni di progetto e non basta a dimostrare la cecità.
- Verifica dei nuovi artefatti: schema ufficiale Compose superato, tre blocchi bash sintatticamente validi, link locali risolti. Nessun avvio o collaudo operativo: daemon Docker non raggiungibile e plugin Compose assente nella sessione. Dettagli nel CHANGELOG Hermes. Nessun avvio sintetico VC eseguito.
- Non modificati procedura, testo normativo, fonti, schede, contatori o registri VC in questa preparazione. Il prompt VC del § 3.4.5 resta distinto e non preso in carico. La creazione del bot non autorizza una verifica di produzione.

Prossima azione: acquisire l'username del nuovo bot e attivare Hermes NTC-VC sul W520, con credenziali locali e collaudo della separazione C/E/V, senza avviare scope VC di produzione.

## 2026-09-06 - Chiusura sessione e prompt di ripresa del § 3.4.5

- CDX: salvato su richiesta di Sandro `PROMPT-RIPRESA-VC-3.4.5.md`, con comando iniziale di presa in carico, procedura vigente e misura dei consumi. Collegato in README e indice; nessuna VC avviata.
- CDX: registrata la chiusura richiesta da Sandro. Punto di ripresa: § 3.4.4 concluso, procedura VC-NTC/2 pronta, risparmio effettivo ancora da misurare sul § 3.4.5. Verificati contenuto del prompt e rinvii; conservati gli esiti delle verifiche tecniche già registrati nella voce precedente.

Prossima azione: eseguire il prompt del solo § 3.4.5 alla richiesta di ripresa di Sandro.

## 2026-09-05 - VC-NTC/2, riduzione del costo di coordinamento

- Su richiesta di Sandro dopo la misura del § 3.4.4, perfezionata la procedura unica senza modificarne il canone di fedeltà, la copertura integrale, l'indipendenza dei ruoli o i limiti dei giri. Revisione 1 e strumenti conservati in `old/procedura-vc-r01-20260905/`.
- `avvio` legge stato, lucchetto e soli estratti pertinenti; i tagli sono dichiarati. `prepara` consegna a V istruzioni neutre con campi esatti. `valida-inventario` intercetta gli errori di formato prima del congelamento; V può correggerli nello stesso contesto. `valida-g6` riconcilia gli ID senza obbligare a riscrivere l'inventario nel rapporto.
- Dimensionati i rapporti ordinari e introdotta una soglia di attenzione alle chiamate di coordinamento. Il controllo integrale di gruppi localizzabili resta obbligatorio; nessun limite redazionale tronca rilievi o prove. Un solo rapporto C e G7 nello stesso contesto di V, senza una nuova proposta narrativa di chiusura.
- `registra` prepara un piano senza scrivere; `--applica` allinea CSV, titolo, scheda e file di governo con sostituzioni esatte, poi esegue linter e rigenerazione/verifica XLSX. Rifiuta G7 non positivo, snapshot o evidenze cambiati, lucchetto di altro agente, variazioni dei contatori e testi attesi non univoci. Ricevuta e precondizioni evitano rilanci alla cieca dopo errori; il giornale resta al comando unico esistente.
- Per i nuovi manifest si selezionano soltanto le copie congelate di procedura/catalogo. L'opzione esplicita `--congelati` conserva verificabili i manifest storici senza modificarli: ammessa soltanto una copia già elencata con gli stessi byte e SHA-256, mai sostituzioni di target o fonte normativa. Sul § 3.4.4 verificati 53/53 file dello snapshot storico.
- Verifiche: 24 test sintetici superati. Canone §§ 3-4 identico alla revisione 1; catalogo, registro VC e manifest storico invariati. Nessuna VC aperta o promossa durante la manutenzione. Il risparmio in produzione non è ancora misurato.
- Firma: Codex (CDX).

Prossima azione: misurare VC-NTC/2 sul prossimo scope autorizzato; il § 3.4.5 resta da autorizzare.

## 2026-09-05 - Ripresa e VC-OK del solo § 3.4.4

- Ripresa l'unica presa CDX in corso, verificata la fine della precedente sessione e l'identità di fonte, target, procedura e catalogo. Riusati G0-G5 e la ricognizione ufficiale della stessa data.
- Confermate le correzioni pregresse su rubrica, notazioni e intestazioni: il target finale si ricostruisce esattamente dalle liste approvate, zero variazioni estranee. Nessuna modifica del testo in questa ripresa.
- G6 R01B fonte-prima e G7, gpt-5.6-sol/xhigh, OK: una pagina primaria, 11 righe depurate, 19/19 elementi, 12 celle logiche e 7/7 input G6; nessun ERR-MD, ERR-AUDIT, DUBBIO, AF o AF-COR. Il tentativo tecnico precedente resta conservato; unico giro effettivo 1/3.
- Manifest 53/53 e resa canonica di una pagina verificati. Snapshot `6e9a5f838301b7d04ed3dc6c39256fcaf6d78997f2f5567350d287bb6cafc448`; manifest SHA-256 `7e7b8870d2eba6818009154e3b412f33b5f10a6f18d5040f8eee7b4defd1de78`. Verbale `verifica-conformita/verbale-VC-ntc2018-3.4.4-2026-09-05.md`; evidenze definitive in `verifica-conformita/vc-3.4.4-20260905/`, prove precedenti conservate nel dossier `_tmp_render`.
- Registri locale e master, vista XLSX, scheda, README, TODO, revisione del capitolo e indice allineati; contatori disponibili registrati per sessione, senza sommare perimetri parent/figli incerti e senza dichiarare un risparmio percentuale. Verifica AI, senza attestazione umana integrale; isolamento istruttivo e letture controllate dichiarati.
- Verifiche finali: registro 311 righe, zero errori e avvisi; XLSX 311 × 11 e 380 collegamenti, zero differenze; manifest 53/53. Riallineata nel CSV la cassa del titolo già verificato nel Markdown.
- Firma: Codex (CDX).

Prossima azione: Attendere un nuovo via libera prima di aprire il solo scope 3.4.5 o altri scope.

## 2026-09-05 - Procedura unica VC-NTC/1 e riduzione del lavoro ripetuto

- Su richiesta di Sandro, introdotta `PROCEDURA-VC.md` come unica procedura per tutti gli agenti: assorbe ciclo, apparati, convenzioni e scelta dei modelli. Il catalogo delle normalizzazioni resta l'allegato prescrittivo invariato. Gli affinamenti successivi si versionano nello stesso file.
- Preparazione meccanica affidata agli script e attività vincolate a Terra; Sol per giudizio normativo e G6/G7, Astra soltanto sui punti difficili. Eliminati i doppioni obbligatori A/B più G6, le nuove letture integrali per rettifiche del solo rapporto e l'obbligo di famiglia diversa. Conservati copertura integrale, fonte-prima, indipendenza dei ruoli, prove sui glifi, non regressione, nuovo G6 dopo modifiche normative e limiti autorizzati dei giri.
- Recuperate nella procedura le precauzioni su raster nativi, frammenti di tabella, didascalie fuori pagina e limiti del testo estratto. Dichiarata la differenza fra isolamento reale e restrizione istruttiva. La manutenzione non apre scope e non azzera decisioni o contatori pendenti.
- Creati `strumenti/vc-supporto.py`, relativa specifica e `test_vc_supporto.py`: pacchetti a rivelazione differita, congelamento prima del target, verifica delle impronte attese e degli input, manifest espliciti riaperti, stato sintetico e lettura prudente dei contatori. Gli strumenti non emettono giudizi VC. Il comando consumi ha rifiutato correttamente un log storico del § 3.4.3 con contatore decrescente: nessun risparmio percentuale o costo dell'abbonamento è dichiarato.
- Allineati gli ingressi locali `AGENTS.md`, `CLAUDE.md`, skill di orchestrazione e rinvii, README, TODO e indice. Allineati i soli riferimenti NTC nelle skill condivise e native Codex, nel ciclo generale, nel protocollo master e nella memoria di progetto; le altre normative mantengono il proprio ciclo.
- Ritirati i due vecchi prompt operativi del § 4.2 come `old/ISTRUZIONI-SUPERATE-*.md`, senza eseguirli o dichiarare concluse le VC. Originali e versioni precedenti conservati in `old/procedura-vc-ante-20260905/`: 29 copie confrontate con le sorgenti tramite SHA-256 prima delle modifiche. Nessun audit storico eliminato.
- Verifica: 15 test sintetici superati; cinque ingressi skill validi; 21 link relativi verificati su 15 file senza errori; registro 311 righe senza errori o avvisi; indici 311 file e 1754 collegamenti validi. Revisione comportamentale indipendente Terra su sei scenari, recepiti i chiarimenti su G1, isolamento e non regressione. Hash del CSV e del catalogo identici all'inizio del lavoro; nessuna modifica a testo normativo, schede di scope o stati VC.
- Chiusura confermata da Sandro: completata la registrazione già presente nel giornale, senza duplicarla. La prova del metodo è rinviata a una nuova sessione; proposto il solo § 3.4.4, riscontrato `MAI-FATTA` nel CSV. Non creato un altro prompt-procedura e non avviata alcuna VC.
- Firma: CDX (Codex).

Prossima azione: aprire una nuova sessione e avviare la VC dello scope scelto con VC-NTC/1, misurando consumi ed esiti completi; proposto il § 3.4.4, non avviato qui.

## 2026-09-04 - VC-OK del file naturale § 3.4.3

- Verificato il solo scope 3.4.3 sulle pagine fisiche NTC 62-63 e Circolare 76-80: 14 rubriche, 6 formule numerate, 10 gruppi matematici sostanziali, 2 tabelle con 20 celle logiche e 8 figure.
- Due correttori P1 distinti hanno applicato soltanto le liste congelate: riallineati rubriche, prosa, formule, definizioni, tabelle, riferimenti e didascalie; ripristinati otto asset. Il preflight finale G2-G5 ha chiuso `OK` con zero residui e un render canonico di nove pagine.
- Conservate e documentate otto anomalie della fonte; nessuna `AF-COR`. Il primo inventario fonte-prima e la prima confezione dei pacchetti G6 sono stati respinti prima dell'esposizione al target e restano come traccia negativa.
- G6 R01 cieco `OK` al primo giro effettivo su due blocchi primari e un duplicato indipendente del blocco più denso. Il primo G7 è stato fermato per un hash NTC storico errato nel solo rapporto P0-D; la rettifica R01 e un P2 fresco hanno chiuso G7 R02 `OK` con zero `ERR-MD`, `ERR-AUDIT` e `DUBBIO`.
- Stato `VC-OK al 2026-09-04`; snapshot `f310e117cbcf8fe1cb0329a1ae5ff8cb21b82c7aa1e018482e2c26d3a250d8c6`, manifest 328/328, SHA-256 manifest `0082c99993186fa1644ca6b88e3b830b8b4d391b002a8a02d2321b327f5774bd`. Evidenze: `verifica-conformita/verbale-VC-ntc2018-3.4.3-2026-09-04.md` e `_tmp_render/cap03/vc-3.4.3-20260904/`.
- **Firma:** CDX (Codex).
- **Prossima azione:** attendere un nuovo via libera prima di aprire il solo scope 3.4.4 o altri scope.

## 2026-09-04 - VC-OK del file naturale § 3.4.2

- Verificato il solo scope 3.4.2 sulle pagine fisiche NTC 61-62 e Circolare 76: cinque gruppi di formule numerate con nove rami, zero formule autonome non numerate, zero tabelle e due figure.
- Corretti da P1 distinti gli scostamenti iniziali di rubriche, prosa, formula, definizioni, didascalia e asset; dopo G6 R01, sette gerarchie di pedice e il grassetto del rinvio `C3.4.1`. L'adjudicazione a 1200 dpi e sui glifi vettoriali ha conservato letteralmente `d un anno` e ha confermato tutte le sette rese `q_{s_n}`/`q_{s_k}` della Circolare.
- Il primo congelamento source-first R02 è stato scartato prima dell'esposizione al Markdown e conservato come traccia; il congelamento sostitutivo è stato accettato e il G6 R02 ha chiuso `OK` su 46/46 elementi e 23/23 input, con zero residui.
- Conservate e documentate nove anomalie della fonte; nessuna `AF-COR`. G7 P0-D Luna e P2 fresco Sol xhigh `OK`: manifest 135/135 e render finale di quattro pagine controllato integralmente.
- Stato `VC-OK al 2026-09-04`; snapshot `8ba6dd0a425e4133e8e0ff05fb2114b6f60cb2801f2d0bd7a07332958b610e77`, manifest SHA-256 `8111afc93a904007362a717d851c8819c8224d9d2f5c7cf95d44902987148b49`. Evidenze: `verifica-conformita/verbale-VC-ntc2018-3.4.2-2026-09-04.md` e `_tmp_render/cap03/vc-3.4.2-20260904/`.
- **Firma:** CDX (Codex).
- **Prossima azione:** attendere un nuovo via libera prima di aprire il solo scope 3.4.3 o altri scope.

## 2026-09-04 - VC-OK del file naturale § 3.4.1

- Aperto il solo scope 3.4.1 sulle pagine fisiche NTC 61 e Circolare 76: due rubriche, tre capoversi, una formula numerata, quattro definizioni e sette rinvii; zero tabelle, figure e asset.
- Corretti da un P1 distinto due `ERR-MD`: cassa della rubrica NTC e cassa più punto aggiunto nella rubrica Circolare. Il diff netto non contiene altre variazioni normative; l'indice interno ha riallineato soltanto la voce derivata della Circolare.
- G4 `OK` sulla formula `[3.4.1]` e sulle quattro definizioni. Le cinque famiglie di differenze residue sono tutte normalizzazioni dichiarate; nessuna `AF` o `AF-COR`.
- G6 R01 cieco `OK` con congelamento fonte-prima, integrità 10/10 e copertura 14/14. G7 P0-D Luna e P2 fresco Sol xhigh `OK`: manifest 38/38, zero `ERR-MD`, `ERR-AUDIT` e `DUBBIO`; render finale di una pagina controllato integralmente.
- Stato `VC-OK al 2026-09-04`; snapshot `aad946d48ddbf921a92851e8568a813e4df69a072ce05a9c360f6e2b95a46687`, manifest SHA-256 `bc9e316c0c7137b55648b22394ebd25a36ce9761b58808e063690d4790d7db33`. Evidenze: `verifica-conformita/verbale-VC-ntc2018-3.4.1-2026-09-04.md` e `_tmp_render/cap03/vc-3.4.1-20260904/`.
- **Firma:** CDX (Codex).
- **Prossima azione:** attendere un nuovo via libera prima di aprire il solo scope 3.4.2 o altri scope.

## 2026-09-03 - VC-OK del file autonomo § C3.3.11 e completamento del § 3.3

- Aperto il solo scope C3.3.11 sulla pagina fisica 75 della Circolare: una rubrica, sei capoversi, quattro formule numerate, due blocchi `dove` con sei definizioni e tre voci finali; nessun testo NTC, tabella, figura o asset del target.
- Corretti da un P1 distinto tre `ERR-MD`: cassa e punto della rubrica, corsivo matematico dell'`i` in `i-esimo`, ripristino di `Si osservi cha`. Il diff contro lo snapshot iniziale non contiene altre variazioni normative.
- Conservate e registrate `AF-3.3-05` per `n_k`/`n_i` e `v_{m,l}`, `AF-3.3-15` per `fs`/`n_s`, `AF-3.3-16` per `Si osservi cha`; nessuna `AF-COR`. Tre errori iniziali del preflight sono stati classificati e chiusi come `ERR-AUDIT`.
- G6 R01 `OK` dopo congelamento fonte-prima 3/3, input 11/11 e adjudicazione indipendente `l`/`1` su ritagli diretti a 1200 dpi e codepoint `U+006C`. Il target non è stato modificato dopo il preflight.
- G7 P0-D Luna e P2 fresco Sol xhigh `OK`: manifest 49/49, zero `ERR-MD`, `ERR-AUDIT` residui e `DUBBIO`; render finale di due pagine controllato integralmente.
- Stato `VC-OK al 2026-09-03`; snapshot `e33a5fd69766a6c821cb03b2d4efcb495b1a33c6611ace17a25f1c58f45e2d92`, manifest SHA-256 `f4ee37a00afb9f5e1efec9e7e822946d16a3353ea2e196b5fc1036b6fb56e168`. Tutti gli undici file naturali del § 3.3 sono `VC-OK`; evidenze: `verifica-conformita/verbale-VC-ntc2018-c3.3.11-2026-09-03.md` e `_tmp_render/cap03/vc-c3.3.11-20260903/`.
- **Firma:** CDX (Codex).
- **Prossima azione:** attendere un nuovo via libera prima di aprire il § 3.4 o altri scope.

## 2026-09-03 - VC-OK del file naturale § 3.3.10

- Aperto il solo scope 3.3.10 sulle pagine fisiche NTC 60 e Circolare 75. Il P0-D e il P1 hanno riconciliato 2/2 titoli e 7/7 capoversi; lo scope non contiene formule, tabelle, figure o asset.
- Corretti da un P1 distinto quattro `ERR-MD`: cassa del titolo NTC, `dei fenomeni` in `di fenomeni`, `e il flutter` in `ed il flutter`, cassa e punto del titolo Circolare. Il diff contro lo snapshot iniziale non contiene altre variazioni normative.
- Conservata la forma fonte `nei con fronti` e registrata come `AF-3.3-14`. La coppia `NTC 2008`/`NTC2008` è stata ricondotta alla normalizzazione dichiarata delle spaziature; nessuna `AF-COR`.
- G6 R01 `OK` dopo congelamento verificabile fonte-prima: integrità 3/3 e 11/11, copertura 9/9. G7 P0-D Luna e P2 fresco Sol xhigh `OK`: manifest 39/39, zero `ERR-MD`, `ERR-AUDIT` e `DUBBIO`; render finale di una pagina controllato integralmente.
- Stato `VC-OK al 2026-09-03`; snapshot `888c0d25d5eae5094ded93d635002b3a22964b1294a1a7b98f2ffb4441d98097`, manifest SHA-256 `2884803bb46b52cdd662e1ad606e7d6695ecff446a7a7c52f272566853939b57`.
- I dieci file 3.3.1-3.3.10 del piano autorizzato sono tutti `VC-OK`; `C3.3.11` resta `DA-RIFARE` e non è stato aperto. Evidenze: `verifica-conformita/verbale-VC-ntc2018-3.3.10-2026-09-03.md` e `_tmp_render/cap03/vc-3.3.10-20260903/`.
- **Firma:** CDX (Codex).
- **Prossima azione:** attendere un nuovo via libera prima di aprire `C3.3.11`, il § 3.4 o altri scope.

## 2026-09-03 - VC-OK del file naturale § 3.3.9

- Aperto il nuovo scope naturale sul solo file 3.3.9; lo scope aggregato storico è rimasto sospeso e scaduto.
- Il P0-D e il P1 hanno riconciliato 2/2 titoli e 3/3 capoversi. Corretti in fase distinta i due titoli: cassa NTC e Circolare, più il punto aggiunto dopo `C3.3.9`; nessun'altra modifica normativa.
- Il G7 R02 ha sospeso la prima chiusura per tre difetti processuali, non testuali. La ricognizione G1 R02 ha incluso entrambi gli atti e una traccia ripetibile; il G6 R02 ha congelato inventario, esito provvisorio e criterio prima di rendere disponibile l'estratto.
- G6 R02 e G7 R03 P0-D/P2 fresco `gpt-5.6-sol` xhigh `OK`: 2/2 titoli, 3/3 capoversi, zero formule, tabelle, figure, asset, `ERR-MD`, `ERR-AUDIT` e `DUBBIO`; render finale di una pagina.
- Stato `VC-OK al 2026-09-03`; snapshot `67fd21f95d852f39aee88ecd1766916fcc05866604925daed143626a85190f18`, manifest 44/44, SHA-256 manifest `702e57fcded60a9547b132652082a260d3667536b9c9532a86cfc4ce9e3b06ce`.
- Evidenze: `verifica-conformita/verbale-VC-ntc2018-3.3.9-2026-09-03.md` e `_tmp_render/cap03/vc-3.3.9-20260903/`.
- **Firma:** CDX (Codex).
- **Prossima azione:** aprire il solo scope 3.3.10, già autorizzato; il § 3.4 resta fuori perimetro.

## 2026-09-03 - VC-OK del file naturale § 3.3.8

- Ripresa la fase correttiva congelata: rimossi i punti non presenti nei titoli C3.3.8.1.2 e C3.3.8.4, ripristinata la cassa del secondo e ricollocato senza modifiche il gruppo [C3.3.6] prima della Figura C3.3.26 e della Tabella C3.3.XVIII.
- Rigenerati l'indice interno e il render di 30 pagine. `strumenti/render-capitolo.py` ora mappa esplicitamente i glifi Unicode necessari e riconosce nella sola copia temporanea le tabelle a pipe adiacenti alla didascalia; nessuna modifica al testo normativo deriva da queste normalizzazioni di visualizzazione.
- Il G6 R02, unito ai tratti validi storici B02-B08, ha chiuso le quattro lacune di accoppiamento a 600 dpi e verificato gli asset ricostruiti. Esito: 0 `ERR-MD`, 0 `ERR-AUDIT`, 0 `DUBBIO`.
- G7 P0-D e P2 fresco `gpt-5.6-sol` xhigh `OK`: manifest 117/117, 30/30 pagine di resa controllate, nessuna difformità bloccante. Unica osservazione non bloccante: testata stretta ma leggibile a pagina 16.
- Stato `VC-OK al 2026-09-03`; snapshot `2997e1fd9e05b8f2045587c40d6d5cf0314c3f0a09d8811b59d7557ffd33125c`, manifest SHA-256 `e5cc0a40531b9b34cbdb0c58b10e3ba4e5d01d8bd03526ac0d816cf80abaffcf`.
- Evidenze: `verifica-conformita/verbale-VC-ntc2018-3.3.8-2026-09-03.md` e `_tmp_render/cap03/vc-3.3.8-20260831/`.
- **Firma:** CDX (Codex).
- **Prossima azione:** aprire il solo scope 3.3.9, già autorizzato; 3.3.10 resta in coda e non va aperto prima del G7 di 3.3.9.

## 2026-08-31 - pausa del G6 incrementale sul file naturale § 3.3.8

- Dimostrata l'identità canonica col testo storico e riusati G0-G5 e i tratti validi del G6 B03-B08, senza ripetere 21 pagine e 27 figure.
- Applicati 19 rilievi storici pertinenti, per 31 occorrenze; ripristinati tutti i 27 asset e superato il render pulito di 30 pagine.
- I controlli P2 e P0 sono stati fermati alla pausa richiesta. Restano tre residui già isolati a p. 57 e p. 72; lo scope rimane `IN-CORSO` e il 3.3.9 non è stato aperto.
- **Prossima azione:** riprendere da `_tmp_render/cap03/vc-3.3.8-20260831/g6-r02/`, correggere i tre residui indicati nella scheda e riavviare soltanto i due controlli incrementali interrotti.
- **Firma:** CDX (Codex).

## 2026-08-31 - VC-OK del file naturale § 3.3.7

- Riusati G0-G5, 34 celle e due figure; corretti cinque rilievi storici e il solo residuo di punteggiatura di G6 R01.
- G6 R02 e G7 Luna/Sol `OK`, 34/34 celle, manifest 27/27; snapshot `595389d8410ec5bbe58707f7047fdd00036125c954379445de61426a6f4eb008`.
- **Prossima azione:** aprire il solo scope 3.3.8; non aprire 3.3.9 prima del suo G7.
- **Firma:** CDX (Codex).

## 2026-08-31 - VC-OK del file naturale § 3.3.6

- Continuità confermata, G0-G5 riusati e tre rilievi storici corretti.
- G6 R01 e G7 Luna/Sol `OK`, zero residui, manifest 17/17; snapshot `b9be00155c36c76bcee189112bf5ac44a3dafc84b9fd79d04695762c4fa847b6`.
- **Prossima azione:** aprire il solo scope 3.3.7; non aprire 3.3.8 prima del suo G7.
- **Firma:** CDX (Codex).

## 2026-08-31 - VC-OK del file naturale § 3.3.5

- Continuità confermata, G0-G5 riusati e tre rilievi storici corretti.
- G6 R01 e G7 Luna/Sol `OK`, zero residui, manifest 17/17; snapshot `1659758b05d21071666131a257744250a2787bbf18292979497220d058e3ca4e`.
- **Prossima azione:** aprire il solo scope 3.3.6; non aprire 3.3.7 prima del suo G7.
- **Firma:** CDX (Codex).

## 2026-08-31 - VC-OK del file naturale § 3.3.4

- Riusati G0-G5 e corretti tre rilievi storici; il G6 naturale ha aggiunto il solo residuo `$c_P$`/`$c_p$`, corretto puntualmente.
- G6 R02 e G7 Luna/Sol `OK`, zero residui, manifest 20/20; snapshot `e35de87780b07a1c2a366c14c6b160a32af5f27e57d321901d01b62db534e037`.
- Verbale `verifica-conformita/verbale-VC-ntc2018-3.3.4-2026-08-31.md`; evidenze `_tmp_render/cap03/vc-3.3.4-20260831/`.
- **Prossima azione:** aprire il solo scope 3.3.5; non aprire 3.3.6 prima del suo G7.
- **Firma:** CDX (Codex).

## 2026-08-31 - VC-OK del file naturale § 3.3.3

- Riusati G0-G5 dopo continuità canonica; corretti soltanto cassa/punteggiatura dei due titoli già rilevati nel G6 storico.
- G6 naturale integrale e G7 Luna/Sol `OK`, 2/2 titoli, 5/5 capoversi, zero residui; manifest 19/19.
- Stato `VC-OK al 2026-08-31`, snapshot `ea34a61cc5c8f301a8e7a996f0bc08359070df1e74c7562c1d40aa6224a81930`; verbale `verifica-conformita/verbale-VC-ntc2018-3.3.3-2026-08-31.md`.
- **Prossima azione:** aprire il solo scope 3.3.4, già autorizzato; non aprire 3.3.5 prima del suo G7.
- **Firma:** CDX (Codex).

## 2026-08-31 - VC-OK del file naturale § 3.3.2

- Riusati G0-G5 dopo continuità canonica e trasferiti soltanto quattro `ERR-MD` storici pertinenti; ripristinata byte-identica la Fig. C3.3.1.
- Il G6 R01 ha trovato zero errori normativi e un solo errore di preparazione del pacchetto. Corretto il preparatore, il G6 R02 integrale ha chiuso con zero `ERR-MD`, `ERR-AUDIT` e `DUBBIO`.
- Corretta anche la resa dei due `≥` nel PDF e l'esclusione degli apparati redazionali dai render, senza perdita di contenuto nel Markdown.
- G7 Luna e Sol `OK`, manifest 26/26. Stato `VC-OK al 2026-08-31`, snapshot `b9c678cce3396e90f10fec3f435b27b8d34dc7379253851dbe1e8f5fbfe1d80e`.
- Verbale: `verifica-conformita/verbale-VC-ntc2018-3.3.2-2026-08-31.md`; evidenze: `_tmp_render/cap03/vc-3.3.2-20260831/`.
- **Prossima azione:** aprire il solo scope 3.3.3, già autorizzato; non aprire 3.3.4 prima del suo G7.
- **Firma:** CDX (Codex).

## 2026-08-31 - VC-OK del file naturale § 3.3.1

- Riusati G0-G5 e gli apparati del vecchio scope aggregato dopo la verifica di continuità canonica della ricomposizione, evitando di ripetere i controlli già validi.
- Corretti i due titoli pertinenti ai rilievi storici e al residuo del nuovo G6; ripristinata byte-identica la Fig. 3.3.1 già verificata nel G4/G6 storico.
- G6 R01 `KO` con un solo residuo; G6 R02 integrale `OK` su 2 titoli, 5 capoversi, 3 blocchi formula, 2 tag, 50 celle logiche e una figura. Zero `ERR-MD`, `ERR-AUDIT` e `DUBBIO`; un `AF-COR` conforme.
- G7 P0-D Luna e P2 Sol `OK`, manifest 27/27. Stato locale `VC-OK al 2026-08-31`, snapshot `f9116d86bd340884e93151d8e295b6e7b06daecc21771bd1e9ca3d13ed00a1ba`.
- Verbale: `verifica-conformita/verbale-VC-ntc2018-3.3.1-2026-08-31.md`; evidenze: `_tmp_render/cap03/vc-3.3.1-20260831/`.
- **Prossima azione:** aprire il solo scope 3.3.2, già autorizzato; non aprire 3.3.3 prima del suo G7.
- **Firma:** CDX (Codex).

## 2026-08-31 - ripresa VC ancorata prima al registro operativo

- Corretta `.agents/skills/orchestra-vc-ntc2018/SKILL.md`: alla frase `riprendiamo VC`, la prima operazione di risoluzione dello scope è ora la lettura di `registro-verifica-conformita-ntc2018.csv`.
- Il registro determina stato corrente, eventuali righe `IN-CORSO`, ultimi `VC-OK`, candidato successivo, `prossima_azione` ed evidenza. TODO, CHANGELOG, registro di revisione e scheda servono poi a confermare autorizzazioni, rinvii e gate, senza poter sostituire lo stato del CSV.
- Vietata la scelta del prossimo scope per sola sequenza numerica quando più righe sono compatibili o le fonti di governo divergono; gli scope aggregati storici restano soltanto evidenze e non sostituiscono gli scope naturali correnti.
- Validazione della skill superata con `quick_validate.py`. Nessun file normativo e nessuno stato VC sono stati modificati.
- **Prossima azione:** alla prossima ripresa VC applicare il nuovo ordine e risolvere lo scope dal registro prima di avviare il routing semplificato.
- **Firma:** CDX (Codex).

## 2026-08-29 - chiusura sessione e autorizzazione della VC completa del § 3.3

- Confermata la chiusura del § 3.2, con i quattro file naturali 3.2.1-3.2.4 tutti `VC-OK`.
- Sandro ha autorizzato per la nuova sessione la VC completa dei dieci file naturali 3.3.1-3.3.10.
- Nessun nuovo scope naturale del § 3.3 è stato aperto in questa sessione. Il vecchio scope aggregato resta sospeso e scaduto e vale soltanto come evidenza storica.
- La ripresa deve aprire il solo 3.3.1 e procedere in sequenza fino al 3.3.10, con procedura semplificata Moon e confronto con Sandro sulle eventuali scelte di buon senso. Il § 3.4 resta fuori perimetro.
- **Firma:** CDX (Codex).

## 2026-08-29 - VC-OK del file naturale § 3.2.4 e chiusura del § 3.2

- Verificato il solo § 3.2.4 contro la pagina fisica NTC 55; la Circolare non contiene un C3.2.4 corrispondente.
- Corretti cinque `ERR-MD`: cassa delle tre rubriche, `fra i punti` riallineato a `tra i punti` e l'esponente della `[3.2.14]` corretto da `2` a `0,7` sulla prova concorde del raster a 600 dpi e del livello caratteri.
- G6 R01 integrale `OK` al primo giro, con copertura di 3 rubriche, 14 capoversi, 4 gruppi formula, 5 rami e 4 tag. G7 Moon e Sol `OK`, manifest 22/22, zero residui e zero anomalie della fonte.
- Stato locale `VC-OK al 2026-08-29`, snapshot `4105f2d3dd29c453c640b782433e03eb9685c808e5fdbd371b87d2b52357f877`. Verbale in `verifica-conformita/verbale-VC-ntc2018-3.2.4-2026-08-29.md`.
- I quattro file naturali 3.2.1-3.2.4 sono ora tutti `VC-OK`. Il § 3.3 non è stato aperto.
- **Firma:** CDX (Codex).

## 2026-08-29 - apertura VC del file naturale § 3.2.4

- Aperto il solo scope 3.2.4 dopo la chiusura `VC-OK` del 3.2.3. Confini accertati sulla pagina fisica NTC 55; la Circolare passa da C3.2.3 a C3.3 e non contiene un C3.2.4 corrispondente.
- Snapshot iniziale `3a91e01cf59acb3d757cafd5c23c82d49dc8411f5378078d517fd29b6336e7b4`, una pagina fonte, quattro gruppi di formule numerate, nessuna tabella e nessuna figura.
- Avviato il preflight P0-D con script e `gpt-5.6-luna/medium`; nessuna modifica normativa eseguita in apertura.
- **Firma:** CDX (Codex).

## 2026-08-29 - VC-OK del file naturale § 3.2.3 per deroga dichiarata

- Corretto il solo residuo del G6 R04 nella Tab. 3.2.VII, da `Categoria di sottosuolo` a `Categoria sottosuolo`; il confronto posizionale conferma una sola riga modificata e nessun'altra variazione del target.
- Per autorizzazione esplicita di Sandro, svolto un controllo indipendente mirato in luogo del quinto G6 integrale. Il controllo finale ha confermato 12/12 celle e 1/1 didascalia; G6 chiuso `OK` per deroga dichiarata, senza registrare un R05.
- Preflight P0-D Moon `OK` e G7 P2 Sol `OK`: manifest 47/47, 9/9 pagine fonte, 12 gruppi di formule, 4 tabelle, 2 figure, 4 `AF`, 0 `AF-COR` e zero rilievi aperti o persistenti.
- Stato locale `VC-OK al 2026-08-29`, snapshot `f2a3371c8beea285ed11b6a18e2a8169b4284740e6583742843345d5cc767086`. Verbale in `verifica-conformita/verbale-VC-ntc2018-3.2.3-2026-08-29.md`.
- **Prossima azione:** aprire il solo scope 3.2.4, già autorizzato; non aprire il § 3.3.
- **Firma:** CDX (Codex).

## 2026-08-28 - G6 R04 del § 3.2.3 chiuso KO con un residuo

- Preflight Moon `OK` sullo snapshot `e13bf499661ea40dbff3ad43623aca94846dfea92af9cb3ffc4cca10a5816ec0`: quattro sole righe corrette, 12 formule numerate, quattro tabelle, due figure e render canonico di nove pagine.
- G6 R04 eseguito con fonte-prima congelata, tre blocchi nuovi e disgiunti, 9/9 pagine e ricomposizione esatta 263/263 righe. Cinque rilievi chiusi come `ERR-AUDIT`, zero dubbi.
- Confermato un solo `ERR-MD`: la Tab. 3.2.VII aggiunge `di` nell'intestazione `Categoria di sottosuolo`, mentre la fonte stampa `Categoria sottosuolo`. Nessuna correzione applicata.
- Con `giro_g6: 4` uguale a `max_giri: 4`, l'esatta correzione e il quinto G6 integrale attendono l'autorizzazione esplicita di Sandro. Evidenze in `_tmp_render/cap03/vc-3.2.3-20260828/g6-r04/`.
- **Firma:** CDX (Codex).

## 2026-08-28 - correzioni autorizzate e apertura G6 R04 del § 3.2.3

- Sandro ha autorizzato l'aumento di `max_giri` da 3 a 4, le sole correzioni congelate dal coordinamento e un nuovo G6 integrale.
- Modificate esclusivamente quattro righe del target: ripristinata la sequenza `di risposta di progetto`, aggiunta la virgola dopo l'intervallo temporale e rese matematiche le otto variabili censite. Il confronto posizionale non rileva altre modifiche.
- Nuovo snapshot `e13bf499661ea40dbff3ad43623aca94846dfea92af9cb3ffc4cca10a5816ec0`, 32.905 byte. Evidenza correttiva in `_tmp_render/cap03/vc-3.2.3-20260828/g6-r04/correzioni-autorizzate.md`.
- **Firma:** CDX (Codex).

## 2026-08-28 - G6 formale giro 3 del file naturale § 3.2.3 chiuso KO

- Eseguito l'ultimo giro autorizzato con inventario fonte-prima congelato, tre blocchi disgiunti di tre pagine e coordinamento separato, tutti su `gpt-5.6-sol/xhigh`. Verificati 3/3 documenti fonte-prima, 17/17 ingressi e 9/9 pagine.
- Confermate tre famiglie `ERR-MD`: una frase omessa nel § 3.2.3.4, una virgola omessa nella Circolare e otto variabili matematiche rese come testo corrente. Chiusi come `ERR-AUDIT` i rilievi sui due tag e sull'accento di `é in genere`; zero dubbi.
- Rafforzato `strumenti/render-capitolo.py`: separazione corretta fra àncore e titoli, decodifica robusta dell'output dei comandi e resa esplicita dei caratteri greci `ξ` e `η`. Il render finale dello scope è stato prodotto in nove pagine senza regressioni visive.
- Nessuna correzione applicata. Lo scope resta `IN-CORSO`, G6 `KO`, G7 non avviato, sullo snapshot `636bc58f3d21d214a2b980fd73499409d5a4fbf089d06b016353e02461897192`.
- Con `giro_g6: 3` uguale a `max_giri: 3`, correzioni e quarto G6 integrale attendono l'autorizzazione esplicita di Sandro. Evidenze in `_tmp_render/cap03/vc-3.2.3-20260828/g6-formale/`.
- **Firma:** CDX (Codex).

## 2026-08-28 - apertura VC del file naturale § 3.2.3

- Aperto il solo scope 3.2.3 dopo la chiusura `VC-OK` del 3.2.2. Confini accertati sulle pagine fisiche NTC 51-55 e Circolare 51-54; riallineati nel registro i precedenti intervalli incompleti.
- Snapshot iniziale `a4ba890ee9712149e5c5b3e2b88769135cda83a5e21b95201d1cb1352ce33660`; inventario preliminare di quindici occorrenze di tag di formula, quattro tabelle, due figure e nove pagine fonte.
- Avviato il preflight P0-D con script e `gpt-5.6-luna/medium`. Nessuna modifica normativa ancora eseguita.
- **Firma:** CDX (Codex).

## 2026-08-28 - VC-OK del file naturale § 3.2.2

- Verificato il solo file `cap03/3.2.2-azione-sismica-categorie-di-sottosuolo-e-condizioni-topografiche.md` contro le pagine fisiche NTC 50-51 e Circolare 50-51. Snapshot rilasciato: `b0e539d976c230e709bc6af524360fc211ba1dcf41c43229cf476c4951c89556`.
- Corretti 23 `ERR-MD` nel preflight, uno nel G6 R01 e uno nel G6 R03. Il rilievo R02 sulla cassa di `$V_{S,eq}$` è stato riclassificato `ERR-AUDIT` sul livello caratteri del PDF.
- Dopo i tre giri G6, Sandro ha autorizzato un controllo mirato finale in luogo del quarto giro integrale. G6 chiuso per deroga dichiarata; G7 `OK`, manifest 18/18, cinque `AF`, zero `AF-COR` e zero rilievi aperti o persistenti.
- Corretto `strumenti/render-capitolo.py` per non mostrare le ancore HTML davanti ai titoli nel PDF e aggiunto `strumenti/prepara-scope-g6.py` per depurare meccanicamente gli scope G6; i file normativi già rilasciati non sono stati alterati dal renderer.
- Aggiornati scheda, verbale, manifest, registro CSV, README, TODO e registro di revisione del capitolo. Evidenze in `_tmp_render/cap03/vc-3.2.2-20260828/`.
- **Prossima azione:** aprire il solo scope 3.2.3, già autorizzato; non aprire il § 3.3.
- **Firma:** CDX (Codex).

## 2026-08-28 - apertura VC del file naturale § 3.2.2

- Aperto il solo scope 3.2.2 dopo la chiusura `VC-OK` del 3.2.1. Confini accertati sulle pagine fisiche NTC 50-51 e Circolare 50-51; corretti nel registro i precedenti intervalli incompleti di una sola pagina.
- Snapshot iniziale `fd41ee228aa961a024f634e2e1c858f3baa3d6dfdb1fca5d9575feb423c49517`; inventario preliminare di due formule, due tabelle, nessuna figura e quattro pagine fonte.
- Avviato il preflight P0-D con `gpt-5.6-luna/medium`, applicando la nuova equivalenza dei tre trattini nelle didascalie. Nessuna modifica normativa ancora eseguita.
- **Firma:** CDX (Codex).

## 2026-08-28 - VC-OK del file naturale § 3.2.1

- Verificato il solo file `cap03/3.2.1-azione-sismica-stati-limite-e-relative-probabilita-di-superamento.md` contro le pagine fisiche NTC 49-50 e Circolare 48-50. Snapshot rilasciato: `d63652647c796ab4b473827eb35d285529f7041fd3e04ff9e0caa480d6ee7d20`.
- I G6 R01 e R02 hanno prodotto tre correzioni complessive. L'unico rilievo R03 sul separatore della didascalia è stato riclassificato `NORM` dopo la decisione di Sandro che rende equivalenti `-`, `–` e `—`; nessuna modifica del target e nessun G6 R04.
- Conservate 3 famiglie di anomalie della fonte, 6 occorrenze, con 0 `AF-COR`. G0-G7 tutti `OK`; il precontrollo Moon e il controllo finale Sol hanno confermato 16/16 voci del manifest e zero rilievi aperti o persistenti.
- Aggiornati scheda, verbale, manifest, registro CSV, vista XLSX, README, TODO e registro di revisione del capitolo. Evidenze in `_tmp_render/cap03/vc-3.2.1-20260828/`.
- **Prossima azione:** aprire il solo scope 3.2.2, già autorizzato da Sandro; non aprire il § 3.3.
- **Firma:** CDX (Codex).

## 2026-08-28 - equivalenza dei trattini e chiusura G6 del § 3.2.1

- Sandro ha stabilito che `-`, `–` e `—` sono equivalenti nei separatori fra numero e testo delle didascalie; aggiornata la voce 10 dell'elenco unico delle normalizzazioni dichiarate.
- L'unico `ERR-MD` del G6 R03 è stato riclassificato `NORM` con conferma P2 `gpt-5.6-sol/xhigh`. Il rapporto storico resta immutato; l'adjudicazione è in `_tmp_render/cap03/vc-3.2.1-20260828/g6-r03/adjudicazione-post-g6.md`.
- Sullo stesso snapshot Markdown risultano zero `ERR-MD`, zero `ERR-AUDIT` aperti e zero `DUBBIO`; G6 è `OK`. Nessuna correzione al file normativo, nessun G6 R04 e nessun aumento di `max_giri`.
- **Prossima azione:** svolgere G7 e chiudere il § 3.2.1 prima di aprire il § 3.2.2.
- **Firma:** CDX (Codex).

## 2026-08-28 - § 3.2.1 fermato dopo il terzo G6 non superato

- Completati G0-G5 e tre giri G6 ciechi integrali sul file `cap03/3.2.1-azione-sismica-stati-limite-e-relative-probabilita-di-superamento.md`, contro le pagine fisiche NTC 49-50 e Circolare 48-50.
- R01 ha rilevato due `ERR-MD`, R02 un ulteriore `ERR-MD`; le tre correzioni sono state applicate separatamente e documentate. R03 ha chiuso `KO` con un solo nuovo `ERR-MD`, zero `ERR-AUDIT` aperti e zero `DUBBIO`: separatore della didascalia `Tab. 3.2.I` non conforme alla normalizzazione dichiarata n. 10.
- Conservate tre anomalie della fonte: tre sottotestate `C_U =` prive dei valori, `T_r` minuscolo nella testata e `Cu` nella legenda raster. Nessuna `AF-COR`.
- Esaurito il massimo di tre G6: il rilievo R03 non è stato corretto, lo scope resta `IN-CORSO`, G6 `KO`, G7 non avviato. Evidenze in `_tmp_render/cap03/vc-3.2.1-20260828/`.
- **Prossima azione:** attendere l'autorizzazione esplicita di Sandro ad alzare `max_giri` da 3 a 4; costo previsto 15-25 minuti per correzione, G6 R04 integrale e G7.
- **Firma:** CDX (Codex).

## 2026-08-28 - chiusura sessione e autorizzazione della prossima VC sul § 3.2

- Chiusa la sessione con il § 3.1 interamente `VC-OK`, il registro riallineato e la vista XLSX conforme al CSV. Nessun file del § 3.2 è stato aperto o modificato in questa sessione.
- Sandro ha autorizzato per la nuova sessione la VC di tutti i file naturali del § 3.2: 3.2.1, 3.2.2, 3.2.3 e 3.2.4. Gli scope saranno lavorati uno per volta e in sequenza, applicando il routing della skill locale con script e Moon/Luna per il deterministico e Sol per i gate critici.
- **Prossima azione:** nella nuova sessione aprire il solo scope 3.2.1 e, dopo la sua chiusura, proseguire in sequenza fino al 3.2.4 senza richiedere ulteriori autorizzazioni intermedie; non estendere il lavoro al § 3.3.
- **Firma:** CDX (Codex).

## 2026-08-28 - chiusura complessiva del § 3.1 e correzione del rinvio operativo

- Verificato su indice, cartella e registro che il § 3.1 contiene soltanto i file naturali 3.1.1-3.1.4, tutti già `VC-OK`; non esiste un file 3.1.5 e non resta alcuna VC da aprire nel § 3.1.
- Corretto il precedente rinvio inesatto al 3.1.5 nella scheda 3.1.4, nel TODO, nel registro di revisione del capitolo e nella voce di chiusura. Il prossimo file naturale in ordine è il 3.2.1, fuori dall'autorizzazione corrente e da aprire soltanto con un nuovo via libera di Sandro.
- Nessun file normativo, verbale, manifest o stato VC è stato modificato.
- **Firma:** CDX (Codex).

## 2026-08-28 - convenzione della prossima azione per le righe VC-OK

- Riallineata la colonna `prossima_azione` delle quattro righe `VC-OK` alla dicitura unica `Nessuna sul file: VC conclusa sullo snapshot registrato.`; rimossi i rinvii ormai storici ai file successivi.
- Registrata la convenzione nel README e nella skill locale di orchestrazione VC. Il prossimo scope resta nel TODO, nel registro di revisione del capitolo e nella scheda chiusa, non nella riga del file già verificato.
- Rafforzato `strumenti/lint-registro-verifica.py`: ogni futura riga `VC-OK` con una dicitura diversa viene ora segnalata come errore. Il CSV supera il linter; la vista XLSX è stata rigenerata e confrontata cella per cella con zero differenze non dichiarate.
- **Firma:** CDX (Codex).

## 2026-08-27 - VC-OK del file naturale § 3.1.4

- Verificato il solo `cap03/3.1.4-opere-civili-sovraccarichi.md` contro le pagine fisiche 47-49 del D.M. 17/01/2018 e la pagina fisica 46 della Circolare 7/2019.
- Il P1 ha corretto 44 unità `ERR-MD`; il G6 R02 ha poi rilevato e fatto correggere una famiglia di 7 categorie omesse nelle righe-titolo della Tab. 3.1.II. La resa finale comprende 51 espansioni semantiche di celle accorpate. Nessuna cifra, coefficiente, esponente, operatore, segno o unità è stata modificata.
- G6 R01 `KO` per un rilievo poi riclassificato `ERR-AUDIT`, R02 `KO` per le sette omissioni reali, R03 `OK` con zero `ERR-MD`, `ERR-AUDIT` aperti e `DUBBIO`. Il primo G7 ha imposto un riallineamento solo contabile; il secondo ha confermato 15/15 voci del manifest, SHA-256 `990eaef70d2946e806bc704e03ae1c5e1dfa06e3cff1156a0de4149113bc52d7`.
- Conservate alla lettera due `AF` grammaticali, nessuna `AF-COR`; zero rilievi aperti o persistenti. Snapshot rilasciato: `776028cc5077b37cd3599398642a20774cc72e72161a64a1a0e643e60c3c6e3f`.
- Aggiornati scheda, verbale, manifest, registro CSV, vista XLSX, README, TODO e registro di revisione del capitolo. Evidenze in `_tmp_render/cap03/vc-3.1.4-20260827/`.
- **Prossima azione:** il § 3.1 è completo; Sandro ha successivamente autorizzato per la nuova sessione tutti i file 3.2.1-3.2.4, da lavorare uno per volta.
- **Firma:** CDX (Codex).

## 2026-08-27 - VC-OK del file naturale § 3.1.3

- Verificato il solo `cap03/3.1.3-opere-civili-carichi-permanenti-non-strutturali.md` contro le pagine fisiche 46-47 del D.M. 17/01/2018 e la pagina fisica 46 della Circolare 7/2019.
- Applicate quattro correzioni logiche in tre sostituzioni: cassa delle due rubriche, eliminazione del punto assente dopo `C3.1.3` e reintegro del secondo `da` in `o da normative o da documenti`. Nessun numero, valore, operatore o unità modificato.
- Cinque enunciati matematici riconciliati source-first. G0-G7 tutti `OK`; G6 cieco superato al primo giro; precontrollo Luna e controllo finale Sol hanno confermato il manifest 11/11; zero `ERR-MD`, `ERR-AUDIT`, `DUBBIO`, `AF` e `AF-COR` residui. Snapshot rilasciato: `40ff097b595fcf59bc6de8cbdd8b7bfa644636f19b4dcc48a7964a359e56a654`.
- Aggiornati scheda, verbale, registro CSV, vista XLSX, README, TODO e registro di revisione del capitolo. Evidenze in `_tmp_render/cap03/vc-3.1.3-20260827/`.
- **Prossima azione:** aprire e verificare il file 3.1.4, già autorizzato da Sandro come scope distinto.
- **Firma:** CDX (Codex).

## 2026-08-27 - VC-OK del file naturale § 3.1.2

- Verificato il solo `cap03/3.1.2-opere-civili-pesi-propri-dei-materiali-strutturali.md` contro la pagina fisica 46 del D.M. 17/01/2018; la Circolare 7/2019 non contiene un § C3.1.2 corrispondente.
- Applicati otto soli edit: cassa della rubrica e delle due intestazioni, più ripetizione delle cinque categorie accorpate nelle due celle logiche secondo la normalizzazione dichiarata. Nessuna cifra, valore, intervallo, unità, simbolo, denominazione o frase è stata modificata.
- Tab. 3.1.I riconciliata 24/24 in due passaggi source-first indipendenti. G0-G7 tutti `OK`; G6 cieco superato al primo giro; controllo finale P2 e manifest superati 8/8; zero `ERR-MD`, `ERR-AUDIT`, `DUBBIO`, `AF` e `AF-COR` residui. Snapshot rilasciato: `c89175b4fab3660a3e1853a32b53cc4851957bc27d5f041720ba68107b6e3e9b`.
- Aggiornati scheda, verbale, registro CSV, vista XLSX, README, TODO e registro di revisione del capitolo. Evidenze in `_tmp_render/cap03/vc-3.1.2-20260827/`.
- **Prossima azione:** attendere il via libera esplicito di Sandro prima di aprire il file 3.1.3.
- **Firma:** CDX (Codex).

## 2026-08-27 - gate Moon/Luna e routing effettivo della VC Codex

- Rafforzata la skill `.agents/skills/orchestra-vc-ntc2018/` con una regola lampo per ogni file `x.y.z`: script, Moon/Luna P0-D, Terra P0-S soltanto se necessario, Sol P1 per i soli residui interpretativi e Sol P2 per G6/G7.
- Introdotto un gate bloccante: per G2-G5 Sol non può ripetere il fascicolo preparatorio senza che il passaggio P0 sia concluso e il motivo puntuale dell'escalation sia registrato.
- Registrato `gpt-5.6-luna` come alias operativo del profilo Moon quando è l'identificativo esposto dal runtime; l'assenza del nome `gpt-5.6-moon` non determina più il fallback automatico a Terra.
- Aggiunto alle schede il blocco `routing_effettivo`, distinto dal routing pianificato. Riallineata la scheda § 3.1.2 con gli esecutori reali: script, Terra P0-S completato, Sol P1 interrotto senza esito, P2 non avviato.
- Eseguita una prova comportamentale isolata con `gpt-5.6-luna/medium`: routing economico rispettato. Il test ha fatto emergere e chiudere tre ambiguità: per scope di 1-2 pagine il blocco G6 coincide con lo scope senza accorpare sezioni adiacenti; G4 con zero apparati si chiude su evidenza P0-D; P0-D prepara hash e manifest ma non può chiudere G7.
- Lo scope § 3.1.2 è stato portato a `SOSPESO` e la riga locale a `DA-RIFARE`; il Markdown è invariato allo snapshot iniziale. Stati del registro: 1 `VC-OK`, 37 `DA-RICONFERMARE`, 21 `DA-RIFARE`, 252 `MAI-FATTA`.
- **Prossima azione:** attendere un nuovo via libera di Sandro; alla ripresa del solo § 3.1.2 rieseguire il preflight P0-D con `gpt-5.6-luna`.
- **Firma:** CDX (Codex).

## 2026-08-27 - VC-OK del file naturale § 3.1.1

- Verificato il solo `cap03/3.1.1-opere-civili-generalita.md` contro la pagina fisica 46 del D.M. 17/01/2018; la Circolare 7/2019 non contiene un § C3.1.1 corrispondente.
- Corretto un unico `ERR-MD`, la cassa della rubrica da `Generalità` a `GENERALITÀ`; il confronto successivo conferma che il corpo normativo coincide integralmente dopo le sole normalizzazioni dichiarate.
- G0-G7 tutti `OK`. G6 cieco superato al primo giro; controllo finale P2 e manifest superati 7/7; zero `ERR-MD`, `ERR-AUDIT`, `DUBBIO`, `AF` e `AF-COR` residui. Snapshot rilasciato: `6b24bfaa2009cab169c81406b2cedce1f2581ed5d60dab5acee3afebdbf4c8a2`.
- Aggiornati scheda, verbale, registro CSV, vista XLSX, README, TODO e registro di revisione del capitolo. Evidenze in `_tmp_render/cap03/vc-3.1.1-20260827/`.
- **Prossima azione:** attendere il via libera di Sandro prima di aprire il file 3.1.2.
- **Firma:** CDX (Codex).

## 2026-08-27 - registro VC compatto e vecchi schemi archiviati

- Sostituito il registro operativo a 42 colonne e 1.724 unità con `registro-verifica-conformita-ntc2018.csv` compatto: 311 righe, una per file naturale `x.y.z`, e 11 colonne nell'ordine concordato. Conservati gli stati storici per aggregazione senza attribuire nuovi esiti VC: 37 `DA-RICONFERMARE`, 20 `DA-RIFARE`, 254 `MAI-FATTA`.
- Esposte per ciascun file le pagine fisiche NTC e Circolare già certe, compresse in intervalli; per 51 file la pagina Circolare non rilevata dal precedente inventario è rimasta vuota con nota esplicita. Date e verbali dei precedenti G7 sono collegati alle righe da riconfermare; le schede di scope sono collegate alle righe da rifare.
- Riscritto `strumenti/genera-vista-xlsx-registro.py` per il nuovo schema e rigenerata la vista XLSX: 311 righe, 11 colonne, 368 collegamenti relativi standard ai Markdown e alle evidenze, filtro, convalida dello stato, colori condizionali e riquadro congelato in `B2`. Verifica cella per cella: zero differenze non dichiarate e zero formule.
- Creato `strumenti/lint-registro-verifica.py`: controlla schema, progressivo, corrispondenza con i 311 file indicizzati, titoli H1, indici interni, pagine, stati, date, evidenze e assenza di URI Obsidian. Primo esito: `0 errori, 0 avvisi`.
- `strumenti/genera-indici-interni.py` ora prende dal registro compatto l'elenco canonico dei file attivi, evitando di includere automaticamente copie obsolete ripristinate dalla sincronizzazione. Verifica superata su 311 file e 1.754 collegamenti interni.
- Archiviati in `old/schema-registro-dettagliato-20260827/` il CSV a 42 colonne, la precedente vista XLSX, `indice-vc-ntc2018.csv`, il CSV a 38 colonne, generatore, linter e mappatore del vecchio indice VC. Archiviati in `old/schema-file-capitoli-pre-ricomposizione-20260827/` 14 file obsoleti dei §§ 4.2 e 11.3 ricomparsi durante la sincronizzazione. Raccolti in `old/sync-conflict-20260827/` 36 file di conflitto creati dalla sincronizzazione, conservandone i percorsi relativi. I prompt consumati ricomparsi sono stati nuovamente raccolti in `old/` dopo averne verificato l'identità.
- Aggiornati README, TODO, indice generale, AGENTS locale e `old/README.md`. Verifica visiva della nuova vista in `_tmp_render/semplificazione-registro-20260827/`; vecchio schema integralmente recuperabile in `old/`.
- **Prossima azione:** aprire una nuova sessione e riprendere la VC dello scope scelto, seguendo la relativa scheda in `verifica-conformita/`; nessuna VC è stata avviata in questa sessione.
- **Firma:** CDX (Codex).

## 2026-08-27 - indici interni estesi a tutti i file `x.y.z`

- Esteso il modello approvato sul § 4.1.1 a tutti i 311 file naturali `x.y.z` dei Capitoli 2-11, compresi i 13 file autonomi della sola Circolare.
- Generati 1.754 collegamenti Markdown interni con altrettante ancore HTML esplicite `toc-ntc2018-*`. Il blocco è delimitato da `INDICE-INTERNO:INIZIO/FINE`, così tutto l'apparato può essere escluso meccanicamente dai futuri pacchetti G6.
- Aggiunto `strumenti/genera-indici-interni.py`, che rigenera e verifica la forma canonica, impedisce modifiche se il censimento non coincide con 311 file e confronta il corpo privo degli apparati con una copia precedente.
- Controlli superati: 311/311 corpi normativi invariati byte per byte; 311 file e 1.754 destinazioni resi con `app-scrivania`, senza errori, ancore mancanti o duplicate; BOM UTF-8, terminatori LF e newline finale conservati in tutti i file.
- Il lint del registro chiude con `0 errori` e `0 avvisi`; segnala 1.206 sole informazioni per `linea_md` spostate. CSV e vista XLSX non sono stati modificati perché il runtime Codex non dispone dell'`@oai/artifact-tool` obbligatorio per la relativa skill.
- Copie recuperabili e manifest in `_tmp_render/indici-interni-x-y-z-20260827/`. Nessuna VC avviata e nessuno stato di verifica modificato.
- **Prossima azione:** riallineare i 1.206 valori informativi `linea_md` nel CSV con un runtime abilitato ai fogli di calcolo e rigenerare la vista XLSX; nessuna azione residua sugli indici interni.
- **Firma:** CDX (Codex).

## 2026-08-27 - vista Excel del registro VC, con il CSV che resta la fonte

- Creata `registro-verifica-conformita-ntc2018.xlsx`: un solo foglio `registro-vc`, 1.724 righe dati, 42 colonne, 1.643 collegamenti in `link_md`, riquadro congelato in `B2`, filtro automatico sull'intestazione, intestazione in grassetto e larghezze leggibili.
- Sciolto il blocco che aveva fermato Codex: la skill `Spreadsheets` del suo runtime impone `@oai/artifact-tool` e vieta `openpyxl`, vincolo che in Claude Code non esiste. Conversione eseguita con `openpyxl 3.1.5`.
- **Cambiata la decisione del prompt su indicazione di Sandro**: l'XLSX non diventa il registro unico. Il CSV resta la fonte operativa, cercabile con Grep, confrontabile riga per riga e senza conflitti di Obsidian Sync; l'XLSX è una vista derivata, da rigenerare e non da modificare a mano. Il CSV non è stato archiviato e generatore e lint non sono stati toccati, perché continuano a lavorare sulla fonte.
- Trovato e aggirato un ostacolo che il prompt non prevedeva: scritta `link_md` come formula `HYPERLINK`, **Excel rifiuta il file**. Excel ammette al massimo 255 caratteri per una stringa letterale dentro una formula e 53 dei 1.643 URL `obsidian://` arrivano a 346. Diagnosi per esclusione su cinque varianti dello stesso registro: dati, riquadro congelato e filtro aprono, le formule no. Nella vista la colonna è quindi un collegamento ipertestuale vero, che regge fino a circa 2.084 caratteri; il prompt lo consentiva, chiedendo di conservare «collegamenti o formule».
- Nuovo strumento `strumenti/genera-vista-xlsx-registro.py`: rigenera la vista dal CSV, poi la rilegge e la confronta cella per cella con la fonte, ricostruendo dall'XLSX la formula localizzata a partire da testo e URL del collegamento. Esce con codice diverso da zero alla prima differenza non dichiarata; `--verifica-soltanto` esegue il solo confronto.
- Due scostamenti dichiarati e obbligati. Sei colonne interamente numeriche sono scritte come numeri, per renderle ordinabili in Excel; `capitolo` resta testo perché usa lo zero iniziale. Due celle di `titolo` sono state ripulite dai caratteri di controllo che XML non ammette: riga CSV 394 `NTC-5.1.3.3` (`U+0014`) e riga CSV 493 `NTC-6.1` (`U+0003` due volte), residui dell'estrazione dai segnalibri del PDF; in entrambi i casi `heading_md` riporta il titolo giusto.
- Controlli finali: confronto cella per cella con zero differenze non dichiarate e ordine delle 1.724 unità conservato; apertura reale in Excel senza richiesta di ripristino, con 1.643 collegamenti nel foglio, `FreezePanes=True`, `SplitRow=1`, `SplitColumn=1`, zero iniziale di `capitolo` conservato e URL più lungo intatto; un collegamento lanciato davvero ha portato Obsidian sulla nota attesa. Excel normalizza in lettura `obsidian://open?vault=` in `obsidian://open/?vault=`, forma provata e funzionante.
- Nessuno stato VC modificato e nessuna verifica di conformità avviata. Verbale, script di conversione, controllo indipendente, script di apertura in Excel ed elenco dei caratteri rimossi in `_tmp_render/conversione-xlsx-20260827/`.
- **Firma:** CC (Claude Code).

## 2026-08-27 - prova di indice interno nel § 4.1.1

- Inserito nel solo file `cap04/4.1.1-calcestruzzo-valutazione-della-sicurezza-e-metodi-di-analisi.md` un indice interno gerarchico delle parti Norma e Circolare.
- Usati collegamenti Markdown nello stesso documento e identificatori HTML espliciti, indipendenti dagli slug automatici del viewer; il blocco è delimitato da commenti ed è quindi riconoscibile e reversibile.
- Verifica con il renderer corrente di `app-scrivania` e con Pandoc: 10 collegamenti interni, nessuna destinazione mancante e nessun identificatore duplicato. Nessuna estensione agli altri file e nessuna VC avviata.
- **Prossima azione:** attendere la valutazione di Sandro sulla prova prima di definire la convenzione generale ed estenderla al corpus.
- **Firma:** CDX (Codex).

## 2026-08-26 - diagnosticato il Not Found dei rinvii di testa

- Riprodotto il caso segnalato sul § 2.2.3 e verificato il corpus vivo: 459 Markdown, 2.402 link, zero destinazioni mancanti e zero file normativi privi della navigazione di testa.
- Accertato che i rinvii NTC sono normali link Markdown portabili, non wikilink Obsidian. `app-scrivania` lascia al browser i link relativi fra file e il server restituisce `Not Found`; gli ancoraggi interni come quelli di `bersdor-corrispondenza.md` funzionano perché restano nello stesso documento.
- Nessun file normativo modificato. Rapporto in `_tmp_render/diagnosi-link-indici-20260826/`; correzione dell'app demandata da Sandro a un agente esterno.
- **Firma:** CDX (Codex).

## 2026-08-26 - prompt consumati raccolti in old

- Spostati dalla radice a `old/` tutti i 7 file `PROMPT-CONSUMATO-*.md`; i prompt `RIPRESA` e `IN-CORSO` sono rimasti nella posizione operativa.
- Creato `old/README.md` come indice dell'archivio e aggiornati README, TODO, AGENTS locale e il rinvio della scheda § 4.1.
- Verificata l'identità dei sette file per nome e dimensione dopo lo spostamento; nessun contenuto storico è stato riscritto.
- **Firma:** CDX (Codex).

## 2026-08-26 - preparato il passaggio della conversione XLSX

- Creato `PROMPT-RIPRESA-RISOLUZIONE-BLOCCO-XLSX.md` nella radice del progetto, con presa in carico obbligatoria, diagnosi del blocco `@oai/artifact-tool`, vie ammesse per risolverlo e controlli richiesti per la futura conversione.
- Il prompt conserva come precondizioni i conteggi correnti del registro e vieta modifiche agli stati VC. Nessuna conversione e nessuna modifica al CSV sono state eseguite.
- **Firma:** CDX (Codex).

## 2026-08-26 - registro VC locale consolidato

- Rinominato `registro-dettaglio-verifica-ntc2018.csv` in `registro-verifica-conformita-ntc2018.csv`: il nome riflette l'uso come unica fonte operativa locale per stato corrente, storia del processo VC e prossima azione delle 1.724 unità.
- Dismesso dalla radice `indice-vc-ntc2018.csv`, vista derivata ormai ridondante; copia finale, snapshot pre-intervento e script storico di mappatura sono conservati in `_tmp_render/consolidamento-registro-vc-20260826/`.
- Aggiornati `indice-ntc2018.md`, README, TODO, AGENTS locale, percorsi nei record NTC 2018 del master e default di generatore e lint. Gli indici Markdown di navigazione restano distinti dal registro VC.
- Controlli finali: lint del registro senza errori, avvisi o info; 1.724 righe, 42 colonne e BOM UTF-8 preservato; nessun rinvio operativo residuo alla vista CSV dismessa.
- **Firma:** CDX (Codex).

## 2026-08-26 - il registro traccia anche il processo VC

- Esteso `registro-dettaglio-verifica-ntc2018.csv` da 38 a 42 colonne con `stato_processo_vc`, `scope_vc`, `ultimo_gate_vc` e `prossima_azione_vc`, collocando lo stato del processo subito dopo `esito_unita` per renderlo visibile in Excel.
- Classificate 286 unità `DA_RICONFERMARE`: Capitolo 8 113, § 4.1 136 e § 4.2-A 37. Per tutte è registrato `G7_OK_STORICO`; le quattro unità del Capitolo 8 che conservavano soltanto l'etichetta dei lotti specialistici ora espongono anche il successivo rilascio integrale G0-G7, senza perdere le evidenze precedenti.
- Classificate 150 unità `DA_RIAPRIRE`: § 3.3 45 con `G6_KO_R01_STORICO`, § 4.2-B 33 con `G6_KO_R07_STORICO`, § 4.2-C/D 72 con `SCOPE_APERTO_PRE_G0_STORICO`. Le altre 1.288 unità sono `NON_AVVIATO`.
- Conservati senza variazioni `stato_verifica_unita=DA_FARE` ed `esito_unita=NON_VALUTATO` su tutte le 1.724 righe: la nuova classificazione descrive il lavoro VC già svolto e la prossima azione, non attribuisce conformità corrente.
- Allineati l'indice VC e il master: Capitolo 8, § 4.1 e § 4.2-A risultano `VC-SCADUTA - DA RICONFERMARE`; gli scope sospesi risultano `VC-SCADUTA - DA RIAPRIRE`; il corpus resta `VC-DA-FARE`.
- Aggiornati generatore e lint per governare il nuovo schema. Controlli finali: 1.724 righe, 42 colonne, 1.643 formule `COLLEG.IPERTESTUALE`, BOM UTF-8 su tutti e tre i CSV, hash dei vivi coincidenti con le versioni candidate, lint `0 errori, 0 avvisi, 0 info`.
- Evidenze e snapshot pre-modifica in `_tmp_render/registro-processo-vc-20260826/`.
- **Firma:** CDX (Codex).

## 2026-08-26 - struttura di livello 3 completata e navigazione resa portabile

- Ricomposti i quattro file monolitici rimasti nei Capitoli 2, 8, 9 e 10 in 59 file di contenuto e 10 indici di sezione. Il corpus applica ora dall'inizio alla fine la regola «una sezione naturale `x.y.z`, un file Markdown»; i Capitoli 1 e 12 restano correttamente monolitici perché non hanno livelli `x.y.z`.
- Archiviati senza modifiche `2-sicurezza.md`, `8-esistenti.md`, `9-collaudo.md` e `10-redazione.md`. Lo staging ha superato 99/99 confronti canonici, ha conservato 59/59 tag di formula e l'intero insieme dei riferimenti grafici.
- Aggiornati l'indice generale e tutti i 12 indici di capitolo. Convertiti complessivamente 588 wikilink, 523 negli indici e 65 nei file normativi o nelle annotazioni; resi espliciti con `./` o `../` 685 rinvii di testa e altri 477 collegamenti degli indici.
- Stato finale: 379 file normativi, 53 indici di sezione, 12 indici di capitolo e 311 sezioni `x.y.z`. Controllati 2.403 collegamenti in 459 file Markdown, con zero collegamenti rotti, zero wikilink nei 66 indici e zero file normativi privi della navigazione di testa. Render rappresentativo dei Capitoli 2, 6, 8, 9 e 10 superato 5/5, senza pagine vuote, tag tondi o didascalie automatiche.
- Rimappate 173 righe del registro di dettaglio. Le 113 unità del Capitolo 8 sono `DA_FARE/NON_VALUTATO`, con evidenza storica preservata; il precedente `VC-OK al 2026-07-29` è `VC-SCADUTA al 2026-08-26`. Nessuna nuova VC è stata eseguita. Lint finale del registro: 1.724 righe, 0 errori, 0 avvisi e 0 info.
- Evidenze, copie recuperabili, staging e snapshot in `_tmp_render/completamento-struttura-portabile-20260826/`.
- **Firma:** CDX (Codex).

## 2026-08-26 - capitoli lunghi ricomposti in file naturali di livello 3

- Applicato ai capitoli 3, 4, 5, 6, 7 e 11 il criterio già adottato per il § 4.2: ogni sezione `x.y` è governata da `indice-x.y.md`, ha un file di introduzione e un file per ciascun sottoparagrafo naturale `x.y.z`, con il tema del paragrafo nel nome. Le sezioni della sola Circolare usano il prefisso `c`.
- Archiviati 33 file aggregati e installati 304 file di contenuto più 42 indici. Le sezioni brevi `7.0`, `7.1`, `11.1` e `11.6` sono state separate dai vecchi file combinati senza inventare un livello 3. Il § 4.2 e i capitoli brevi, incluso il Capitolo 8, sono rimasti invariati.
- Confronto deterministico superato: 506/506 confronti canonici, 501/501 tag di formula e 167/167 riferimenti grafici conservati; le 163 immagini già mancanti nel perimetro restano le stesse, senza nuove perdite. Controllati 1.348 collegamenti nello staging, nessuno rotto.
- Render smoke sul file più pesante di ciascuna delle 46 sezioni estratte: 33 file resi correttamente; 13 KO classificati come preesistenti, perché tutte le 83 righe con forma `$$…$$ \tag{…}` sono presenti identiche nei file aggregati archiviati. Zero errori di render nuovi dovuti alla divisione. La correzione di quella sintassi resta fuori dal perimetro di questa ricomposizione.
- Rimappate 1.409 righe del registro di dettaglio: 1.328 heading univoci e 81 unità prive di heading autonomo assegnate al file naturale pertinente. Restano 1.643 formule `COLLEG.IPERTESTUALE` attive; lint su 1.724 righe con `0 errori, 0 avvisi, 0 info`.
- Il vecchio scope § 4.1 non è stato trasferito alla nuova struttura: 136 unità correnti riportate a `DA_FARE/NON_VALUTATO`, con controllo, snapshot ed evidenza G7 conservati nei campi storici. In questo stato intermedio il Capitolo 8 conservava 113 unità `COMPLETA/OK` e il proprio `VC-OK`; la successiva ricomposizione descritta nella voce sopra ne ha reso scaduto il giudizio corrente.
- Navigazione aggiornata negli indici generale e di capitolo e nelle annotazioni, compresi i ritorni puntuali alle formule, figure e tabelle del § 3.3. Evidenze, staging, snapshot e archivio recuperabile in `_tmp_render/ricomposizione-livello3-20260826/`.
- **Firma:** CDX (Codex).

## 2026-08-26 - audit delle cartelle di capitolo e ripristino della coerenza VC

- Inventariati i 147 file vivi di `cap01`-`cap12`: nessun doppione byte-identico, nome da copia o backup, file normativo non indicizzato, unità senza registrazione o ID numerato duplicato fra documenti. Il vecchio `cap04/4.2-acciaio.md` non è presente; il § 4.2 corrente ha 13 file indicizzati e 63/63 asset risolti.
- Accertati 165 richiami PNG non risolti fuori dal § 4.2: 1 in `cap02`, 49 in `cap03`, 42 in `cap04`, 25 in `cap05`, 46 in `cap07` e 2 in `cap11`. Il problema è una perdita di asset, non la presenza di doppioni.
- Confrontato il manifest G7 del § 4.1 con il vivo e con tutte le copie omonime del workspace. Il Markdown `4.1-calcestruzzo.md` conserva esattamente lo SHA-256 verificato; ripristinati quattro asset byte-identici al manifest. Per gli altri tredici esistono soltanto versioni anteriori con hash diverso, lasciate negli audit storici.
- Riparata la deriva dei registri: 113 unità del Capitolo 8 riportate a `COMPLETA/OK`; 136 unità del § 4.1 a `COMPLETA/SCADUTO`; 37 unità del vecchio 4.2-A lasciate `DA_FARE/NON_VALUTATO` sulla struttura nuova ma nuovamente collegate all'evidenza storica.
- Aggiornate 136 righe dell'indice VC a `VC-SCADUTA al 2026-08-26` e ripristinati nel master generale i record autonomi Capitolo 8, § 4.1 e 4.2-A. In questo stato intermedio il solo Capitolo 8 restava `VC-OK` corrente; la successiva ricomposizione descritta nella voce sopra lo ha portato a `VC-SCADUTA`, mentre il corpus resta `VC-DA-FARE`.
- Controlli finali: manifest Capitolo 8 4/4; manifest § 4.1 con 7 percorsi `OK`, 13 `MANCANTE` e 1 `DIVERSO`; lint del registro su 1.724 righe con `0 errori, 0 avvisi, 0 info`. Evidenze e snapshot pre-modifica in `_tmp_render/audit-struttura-capitoli-20260826/` e `_tmp_render/riallineamento-stati-vc-20260826/`.
- **Firma:** CDX (Codex).

## 2026-08-26 - `link_md` resi cliccabili direttamente da Excel

- Sostituiti i 1.643 wikilink testuali della colonna `link_md` con formule italiane `COLLEG.IPERTESTUALE`, dirette a URI ufficiali `obsidian://open` codificati fino allo specifico heading.
- Verifica applicativa eseguita aprendo temporaneamente il CSV con Excel: `HasFormula=True`, testo visualizzato `Apri`, formula locale riconosciuta. Controllati inoltre 1.643/1.643 URI e destinazioni, senza errori.
- Il § 4.1 continua a usare un solo file fisico, `cap04/4.1-calcestruzzo.md`; nei collegamenti cambia soltanto l'heading dopo `#`.
- Lint globale confermato a `0 errori, 0 avvisi, 0 info`; stati di verifica ed esiti VC invariati. Snapshot ed evidenze in `_tmp_render/registro-link-excel-20260826/`.
- **Firma:** CDX (Codex).

## 2026-08-26 - registro riallineato ai Markdown e dotato di link ai paragrafi

- Riallineati meccanicamente 23 heading, compilate 4 mappature mancanti, corretti 8 conteggi di occorrenza e aggiornate 276 posizioni di riga nel registro di dettaglio. Nessun file normativo è stato modificato.
- Aggiunta la colonna `link_md` con 1.643 collegamenti Obsidian diretti ai paragrafi, successivamente resi formule Excel attive. Le 81 unità non mappate univocamente restano senza collegamento.
- Otto mappature certe sono passate da `DA_VERIFICARE` a `COMPLETA`; gli stati di verifica e gli esiti VC sono rimasti invariati. Riparate anche due righe CSV le cui note contenevano un punto e virgola non quotato.
- Aggiornati `strumenti/genera-registro-dettaglio-verifica.py` e `strumenti/lint-registro-dettaglio.py` per includere e verificare `link_md`.
- Lint globale finale: 1.724 righe, 38 colonne, `0 errori, 0 avvisi, 0 info`. Snapshot e manifest delle modifiche in `_tmp_render/registro-lint-20260826/`.
- **Firma:** CDX (Codex).

## 2026-08-26 - § 4.2, nomi dei file di livello 3 esplicitati con «acciaio»

- Rinominati i 12 file da `4.2.1` a `4.2.11` e `C4.2.12` secondo lo schema `4.2.x-acciaio-<argomento>.md`; mantenuti stabili `4.2-introduzione.md` e `indice-4.2.md`.
- Aggiornati entrambi gli indici del capitolo, il README e 140 righe del registro di dettaglio. Nessun vecchio riferimento resta nei file vivi controllati.
- Verifica pre/post superata: i dodici contenuti sono identici byte per byte; restano 254 tag di formula, 63 riferimenti grafici tutti risolti e zero collegamenti mancanti negli indici.
- Evidenze e snapshot precedente in `_tmp_render/cap04/rinomina-acciaio-20260826/`.
- Il lint globale conserva 23 errori e 8 avvisi preesistenti nei § 4.1 e 8; nessun errore riguarda il § 4.2 rinominato.
- **Firma:** CDX (Codex).

## 2026-08-25 - § 4.2 ricomposto per sottoparagrafi e asset ripristinati

- Sostituita la suddivisione tecnica in quattro file A-D con `cap04/indice-4.2.md` e 13 file corrispondenti alle sezioni naturali di livello 3; NTC e Circolare restano abbinate nello stesso file quando entrambe presenti.
- Confronto pre/post superato: testo conservato per sezione, 254 tag di formula e 63 riferimenti grafici invariati. Revisione strutturale indipendente `PASS` sullo staging.
- Accertato che 42 dei 63 PNG richiamati non erano presenti. Riestratti dai PDF ufficiali a 600 dpi, calibrati manualmente e verificati visivamente su sette tavole; ora 63/63 collegamenti grafici sono risolti.
- Archiviati senza cancellazione i quattro file sostituiti e congelato lo stato pre-migrazione in `_tmp_render/cap04/ristrutturazione-4.2-20260825/`.
- Rimappate le 142 unità del registro ai 13 file correnti. Il precedente giudizio 4.2-A è segnato `VC-SCADUTA`; gli scope storici A-D rinviano ai file archiviati e non sono trasferiti automaticamente alla nuova struttura.
- Aggiornata la vista `indice-vc-ntc2018.csv` dopo la chiusura di Excel: 37 righe storiche 4.2-A portate a `VC-SCADUTA al 2026-08-25`, altre 105 righe del § 4.2 lasciate `VC-DA-FARE`.
- Render finale superato per 13/13 file, 112 pagine complessive: 254/254 tag presenti con parentesi quadre e nessuna didascalia automatica. Il controllo generico ha inizialmente segnalato `(C4.2.22)`, poi confermato come rinvio testuale della fonte distinto dal tag `[C4.2.22]` correttamente reso.
- **Firma:** CDX (Codex).

## 2026-08-25 - § 4.2-B: settimo G6 integrale non superato

- Corretti in fase distinta i 2 `ERR-MD` del sesto G6: `A_v/J_v` nella Tabella C4.2.II e radice quadrata nel numeratore della [C4.2.78.b]. Revisione indipendente del diff e preflight superati; nuovo snapshot `1b548e70e811ed9a508713db79688e67d468c86bf13765d7652413aa493b2b70`.
- Applicato il profilo economico: Moon per il controllo deterministico, Terra per confezionamento e inventari tecnici, Sol per correzione, revisione normativa e G6.
- Settimo G6 integrale cieco completato con sei blocchi indipendenti e coordinatore separato. Copertura riconciliata: 24 pagine, 881 posizioni di riga incluse, 21 asset, 93 formule numerate, 3 gruppi non numerati, 15 tabelle con 324 celle e 12 figure. Manifest del dossier 99/99 verificato.
- Esito autoritativo: 3 `ERR-MD`, 1 `ERR-AUDIT`, 0 `DUBBIO`; `G6=KO`. I tre errori del Markdown sono `h_w^2` anziché `h_w` nella formula non numerata di `\sigma_E`, omissione del prodotto in `0{,}5\cdot h_w` e omissione dei due prodotti in `15\cdot\varepsilon\cdot t`. L'inventario congelato assegna inoltre [C4.2.50] e `\sigma_E` alla pagina stampata 109 anziché 110 e trascrive `h_w^2` anziché `h_w`.
- I due rilievi del sesto G6 restano chiusi e non regrediscono. Il Markdown non è stato modificato dopo il controllo. Con `giro_g6: 7` uguale a `max_giri: 7`, lo scope è `SOSPESO`; G7 non avviato e nessun registro promosso. Occorre un'autorizzazione esplicita a `max_giri: 8` per procedere.
- Verbale autoritativo: `_tmp_render/cap04/vc-paragrafo-4-2b-20260806-r02/g6-r07/coordinamento/01-verbale-coordinamento-g6-r07.md`, SHA-256 `63303fd51205c092937a22ff471c842150f9584c8910dbe8d99db63cd194c889`.
- **Firma:** CDX (Codex).

## 2026-08-25 - Profilo economico per la VC Codex

- Su autorizzazione di Sandro, aggiunto `.agents/skills/orchestra-vc-ntc2018/references/profilo-economico.md`: scope nuovi più piccoli, preflight bloccante prima del G6, contesti minimi e bonifica consolidata.
- Distinti i profili semplici: `gpt-5.6-moon` P0-D per il deterministico e `gpt-5.6-terra` P0-S per letture vincolate, mappe ed evidenze. Moon e Terra non possono classificare differenze normative, eseguire G6 o promuovere `VC-OK`.
- Aggiornate skill, matrice, README e TODO. Il ciclo condiviso resta invariato e prevalente: dopo una correzione post-G6 il controllo successivo resta integrale.
- Nessuno scope è stato ripreso e nessun file normativo o stato VC è stato modificato.
- **Firma:** CDX (Codex).

## 2026-08-25 - Orchestra Codex: P0 su gpt-5.6-moon

- Esecutore: **GBOT / verifica-ntc**, su conferma di Sandro che `gpt-5.6-moon` è visibile nel selettore Codex.
- Matrice `.agents/skills/orchestra-vc-ntc2018/references/matrice-profili.md`: P0 passa da Terra a Moon. Scala Moon → Terra (riserva meccanica) → Sol (`high` / `xhigh` / `max`).
- Skill orchestra: Moon per il meccanico; vietato ripiegare su Moon/Terra per G6, adjudicazione o `VC-OK`.
- **Firma:** GBOT (verifica-ntc).

## 2026-08-24 - § 4.2-B: sesto G6 cieco non superato (3 ERR-MD)

- Esecutore: **GBOT / verifica-ntc** (packaging P0, sei verificatori ciechi, coordinamento).
- Snapshot `5057fa99…` (post R06). Confini ridisegnati vs r05; asset 21/21; preflight senza didascalie `Figure N:`.
- Esito autoritativo consolidato: **2 ERR-MD** (verbale coordinatore; `e_N`.prodotto riclassificato AF), **0 ERR-AUDIT**, **0 DUBBIO**; **G6=KO**. Principale: [C4.2.78.b] numeratore (fonte √γ vs MD ∜γ) con prova 600 dpi che ribalta r05; più `e_N`.prodotto e pedici Tab. C4.2.II.
- `giro_g6: 6`, `max_giri: 6`, stato **SOSPESO**; G7 non avviato; vivo non modificato dal G6.
- Verbale: `_tmp_render/.../g6-r06/coordinamento/01-verbale-coordinamento-g6-r06.md`.
- **Firma:** GBOT (verifica-ntc).

## 2026-08-24 - § 4.2-B: correzione R06 (11 ERR-MD + ERR-AUDIT) e avvio sesto G6

- Esecutore: **GBOT / verifica-ntc** (correttore P2 e revisore P1 in contesti separati), su via di capogrokbot.
- Applicati esattamente 11/11 `ERR-MD` del verbale g6-r05 e risolto `COORD-ERR-AUDIT-01`: `strumenti/render-capitolo.py` disabilita `implicit_figures` e verifica assenza di didascalie `Figure N:`.
- Revisione indipendente del diff: **PASS** (`g6-r06/correzione-r06/02-revisione-diff-p1.md`).
- Nuovo snapshot vivo: `5057fa9980961215dc6fdebb5bff57c9d554016396940159383c8874f1df9f6f` (pre: `d339546a…`). AF non toccati.
- `G6` resta `KO` fino all'esito del sesto controllo integrale cieco; G7 non avviato.
- **Firma:** GBOT (verifica-ntc).

## 2026-08-24 - § 4.2-B: ripristino 12 PNG asset in `cap04/img` (GBOT/verifica-ntc)

- Esecutore: **GBOT / verifica-ntc**, su incarico di capogrokbot con autorizzazione di Sandro (max_giri 6 già in scheda; questo passo è solo ripristino asset).
- Ricostruiti dai PDF ufficiali cloud i 12 file mancanti; i 9 già presenti non sono stati sovrascritti. Esito meccanico: **21/21** riferimenti del vivo risolti.
- Densità ~8,333× sulla bbox del corpo grafico (allineata ai sibling GU); didascalie «Figura/Tabella …» escluse dal ritaglio, come nei sibling.
- Markdown `cap04/4.2-acciaio-stabilita-verifiche.md` invariato (SHA snapshot scheda `d339546a906bd29a3687154828974e7b72a4b215cd2b323bd7796622491e14c5`).
- SHA-256 nuovi:
  - `tab-4.2.X-coefficiente-kc.png` — `fc48202bfb1a8cd41b19570b4658e00e55e21b4d36afa27870248a6ee835098a`
  - `fig-c4.2.7-aste-composte-due-correnti.png` — `520dc5711db139a01252f781a9af0394af95a2c333a68e3f9bc991c557685a9e`
  - `fig-c4.2.8-lunghezza-inflessione-correnti-tralicciate.png` — `8aa7bdc1423140bb2139f643a91227f80cf041279cfc01253a1c25982ffe5c38`
  - `fig-c4.2.10-tipologie-elementi-ravvicinati.png` — `8076db319891cd4d3bc1104c8f31ca6d59cc1763f6f64bfa5fc0df02a31b1d8d`
  - `tab-c4.2.iv-coeff-interazione-torsione-vincolata.png` — `22071e007b734f9624d753d4d787af3157b6c16c2c6887729801789280d23698`
  - `tab-c4.2.v-coeff-interazione-torsione-libera.png` — `c69cf2548d4a4b68f2550661cfd0a4bdbdf21e3eb77f96e660a6ebe95fc531da`
  - `tab-c4.2.viii-pannelli-due-bordi.png` — `85ed0b4660f1a055786e0f7cbc1437787494a238c3b7954fad8cc36ed31a3c0d`
  - `tab-c4.2.ix-pannelli-un-bordo.png` — `6b5ba8bfed19a3b12db29cfe43cb391cba3a4820b28b445f14be6c96078ce87c`
  - `tab-c4.2.x-beta-larghezza-collaborante.png` — `d0846a9a5b119c908f5b1d9ab25c55174d72ea17c1b9f44b5dfdb3fc8a6fd6f7`
  - `fig-c4.2.15-lastra-irrigidita-compressa.png` — `41e2f73b9e87ff922c56d590d386b911bc8d1ad2fa93901ee06723c52d5d0d4d`
  - `tab-c4.2.xi-lastra-collaborante-irrigidita.png` — `38eb3f0d4e1176b64226c61835031ba4de78271668ef414f91b500a183720262`
  - `fig-c4.2.18-schema-calcolo-irrigiditori-trasversali.png` — `fe0bfcc89b6a6f3c74ec627d97e13f8da5a32969b0115b3d920913b4e1f560ea`
- Meta ritagli: `/workspace/_tmp/ntc-asset-restore/extract-meta.json`. Correzione ERR-MD e sesto G6 non avviati.
- **Firma:** GBOT (verifica-ntc).

## 2026-08-06 - § 3.3 vento: primo G6 non superato con 32 ERR-MD e 7 ERR-AUDIT

- Ricalcolati prima del giro gli SHA-256 delle due fonti congelate e del vivo: `dda1e397…`, `f7c3b8d1…`, `e3d8f75e…`, tutti coincidenti con i valori attesi. Il disegno G6 è stato congelato nella scheda prima dell'esecuzione: otto blocchi primari ciechi da 3-4 pagine e duplicazione cross-famiglia del B05, con esecutori, confini e metriche dichiarati.
- Costruito un inventario fonte-prima sulle 27 pagine rese: 45 titoli/unità, 20 formule numerate, 1 gruppo esposto non numerato, 22 tabelle, 822 celle comprese le testate, 31 figure e 4 apparati spezzati o multipagina. I due dubbi di solo conteggio dell'inventario non sono diventati rilievi di conformità.
- Eseguiti nove pacchetti ciechi privi di registri, verbali, rilievi attesi e apparato di navigazione. Tutti i riscontri sono stati adjudicati su ritaglio a 600 dpi o raster nativo. Esito consolidato: **32 `ERR-MD`**, **7 `ERR-AUDIT`**, **0 `DUBBIO`**; respinti due candidati primari e un candidato duplicato.
- I sette `ERR-AUDIT` derivano da quattro lacune di confine del confezionamento: righe 0376-0378, 0457-0497, 0684-0696 e 0800-0810. Pur essendo state aperte tutte le 27 pagine e tutti i 31 asset, la copertura fonte-abbinata è risultata 893/961 posizioni di riga, 19/22 tabelle, 29/31 figure e 21/21 formule o gruppi esposti.
- La duplicazione cross-famiglia non fornisce una stima quantitativa utile: l'unico candidato comune era un falso positivo correlato; dopo adjudicazione, insieme A di ampiezza 1, insieme B vuoto e intersezione nulla.
- Il vivo `cap03/3.3-vento.md` non è stato modificato e conserva lo SHA-256 `e3d8f75e0c0abc45a5fd5ae024a879478e3635c9a2949fcc28c330fc37abd8d5`. Scheda portata a `giro_g6: 1`, G6 `KO`, stato `SOSPESO`; G7 non è stato eseguito e non sono stati promossi registri o stati VC.
- Evidenze autoritative in `_tmp_render/cap03/vc-3.3-260806/g6-r01/`: `04-rilievi-congelati.md`, `05-esito-consolidato-g6-r01.md`, `06-manifest-finale.tsv`, pacchetti ciechi, esiti originali e adjudicazioni.
- Tutti i revisori attestati sono agenti AI; non è stata eseguita una revisione umana integrale dello scope.
- **Firma:** CDX (Codex).

## 2026-08-06 - § 3.3 vento: rilievi B1-B6 adjudicati e G4 completato sulle 31 figure

- **Adjudicati sulla fonte i sei rilievi B** con lo standard del § 7. B1: la prosa di p. 68 stampa «la relativa Figura C.3.3.21» col punto in più; B2: p. 64 stampa «riportati i Figura C3.3.16» senza la n — rinvii irregolari che il corpus correggeva in silenzio, ripristinati alla lettera. B3: il ramo b) della didascalia della Fig. C3.3.24 era abbreviato nel corpus, reintegrato per esteso. B4: la didascalia stampa «Figure C3.3.4» al plurale, ripristinato. B5: la testata della Tab. C3.3.XI stampa «Θ – 0°» a **tratto singolo** — probante il confronto con la gemella C3.3.XII, che a pari font e risoluzione stampa l'`=` nettamente a due tratti — e un segno non è correggibile nemmeno con nota; l'inciso «(α in °)» è invece conforme (la fonte non lo stampa). B6: nella Fig. C3.3.26 l'etichetta interna al disegno è `C_pm0` mentre la didascalia stampa `c_peo`, anomalia della fonte conservata.
- Sei correzioni in cinque punti con **prova inversa del diff**: riapplicando all'indietro le sostituzioni l'hash torna esattamente allo snapshot di partenza. Nuovo snapshot `e3d8f75e0c0abc45a5fd5ae024a879478e3635c9a2949fcc28c330fc37abd8d5`, 970 righe. Annotazioni `AF-3.3-09…13`; sanata la sezione di `AF-COR-3.3-02`, la cui nota esisteva nel file normativo senza sezione nelle annotazioni.
- **G4 completato sulle 31 figure**, ultimo perimetro scoperto: sei verificatori ciechi in contesti separati con pagine rese e raster nativi, didascalie trascritte a vista, adjudicazione sulla fonte prima di ogni correzione. Esito 31/31: 28 conformi, **3 asset incompleti corretti** — C3.3.4 senza le tre quote «b» inferiori, **C3.3.14 dimezzata** (il ritaglio ignorava lo schema Θ=90° in testa a p. 63, sopra la didascalia), C3.3.19 con l'etichetta «(c)» mozzata — 0 dubbi, 0 difformità di didascalia. Toccati solo asset PNG: il Markdown e il suo hash restano invariati. Versioni precedenti in `_tmp_render/cap03/vc-3.3-260806/g4-figure/`.
- I verificatori ciechi hanno confermato senza saperlo due correzioni del pomeriggio, trascrivendo dalla fonte «Figure C3.3.4» e la didascalia estesa della C3.3.24.
- Corretti altri due conteggi silenziosamente sbagliati di `inventario-g0.py`: la regex delle didascalie non riconosceva «Figure» al plurale e «metodo» veniva contato come `TODO` per mancanza di word boundary.
- **G4 `OK`.** Stato scope: G0, G1, G2, G4, G5 `OK`; G3 `PARZIALE` per il limite strutturale del livello testo della Circolare, coperto solo dal G6 visivo. Rilievi aperti: 0. **Prossimo passo: G6 in cieco**, che per il § 6.7 non può essere né coordinato né eseguito da CC (autore delle fasi correttive): va instradato su Codex, 7-8 blocchi da 3-4 pagine con blocco duplicato cross-famiglia, disegno da congelare nella scheda prima del giro.
- Nota per il verbale di G7: virgola di giuntura aggiunta dal corpus nella didascalia multi-riga della C3.3.3 (la fonte va a capo senza virgola), da dichiarare o togliere.
- Tutti i verificatori sono agenti AI; nessuna revisione umana integrale.
- **Firma:** CC (Claude Code).

## 2026-08-06 - § 4.2-B, quinto G6 non superato con undici ERR-MD e un ERR-AUDIT

- Sandro ha autorizzato l'aumento di `max_giri` da 4 a 5, la fase correttiva distinta dei due rilievi del quarto G6 e il quinto controllo integrale cieco.
- Il correttore P2 ha applicato 2/2 interventi; revisione indipendente del diff `PASS`, senza modifiche estranee. Nuovo snapshot `d339546a906bd29a3687154828974e7b72a4b215cd2b323bd7796622491e14c5`.
- Preflight: BOM conservato, 93 tag distinti, 21/21 asset, lint senza errori e render di 28 pagine senza pagine vuote. Pacchetti con confini ridisegnati e manifest 94/94.
- Quinto G6: inventario fonte-prima fresco, sei blocchi P2 ciechi e coordinatore P2 distinto su dossier 114/114. Copertura completa di 24 pagine, 93 gruppi di formule numerate, 3 gruppi non numerati, 15 tabelle, 12 figure e 21 asset.
- Esito autoritativo: 11 `ERR-MD`, 1 `ERR-AUDIT`, 0 `DUBBIO`. Gli errori del Markdown comprendono tre punti singoli, punto finale dopo `\Phi_{LT}`, `LIMITI` reso al singolare e ordine del radicale nella [C4.2.78.b], la ripetizione dell'intestazione accorpata nella Tab. 4.2.XI e sette didascalie di tabella poste dopo l'immagine anziché prima.
- L'errore di audit riguarda il render, che aggiunge 21 didascalie automatiche, duplica quelle esplicite e denomina come figure anche le tabelle raster. Le prove a 600 dpi confermano come `AF`, da lasciare intatti, `b_{sl,l}` nella prosa, `aso I` nella Figura C4.2.17 e il doppio `++` nella Tabella C4.2.X.
- Il vivo è rimasto invariato durante G6. Con `giro_g6: 5` e `max_giri: 5`, lo scope è `SOSPESO`; G7 non è stato avviato e nessun registro è stato promosso. Serve una decisione esplicita di Sandro prima della correzione, della risoluzione dell'errore di audit e di un eventuale sesto giro.
- Verbale autoritativo: `_tmp_render/cap04/vc-paragrafo-4-2b-20260806-r02/g6-r05/coordinamento/01-verbale-coordinamento-g6-r05.md`, SHA-256 `b5ae882c30d92ed3f123af52226d4caa6b7cd41ae7df33dab43f20e3cd851dd1`.
- Tutti i revisori attestati sono agenti AI; non è stata eseguita una revisione umana integrale dello scope.
- **Firma:** CDX (Codex).

## 2026-08-06 - elenco unico delle normalizzazioni dichiarate, e sei criteri di resa decisi

- Sandro ha deciso i sei criteri di resa emersi da G2 e G4 del § 3.3: restano come sono nei file e si dichiarano come differenze di sola impaginazione. Riguardano pedici che la fonte compone a corpo pieno (`log10`, `Re`), tabelle senza riga di testata, righe a piena larghezza interne alla griglia, formule a più rami numerate una volta sola, formule con graffa rese come elenco e blocchi «dove:» resi come elenco.
- Motivo registrato: la strada alternativa avrebbe imposto di riscrivere in HTML le tabelle senza testata, perché il Markdown non sa farne, e avrebbe prodotto `Re` e `log10` in una forma che un tecnico legge come errore di battitura. In nessuno dei sei cambia una parola, una cifra o un significato.
- Creato `verifica-conformita/normalizzazioni-dichiarate-NTC2018.md`: **elenco unico della classe N per tutto il corpus**, 18 voci, con la cronologia di chi ha deciso cosa e quando. Va richiamato dal verbale di ogni G7 e riletto prima di aprire uno scope. Se una differenza non è lì dentro, non è una normalizzazione.
- Aggiunto il rinvio in `AGENTS.md` del progetto, § Metodo.
- Nessun file normativo toccato. Rilievi aperti sul § 3.3 da 12 a 6.
- **Firma:** CC (Claude Code).

## 2026-08-06 - § 3.3 vento: G2 superato, G4 esteso a formule e tabelle, 40 occorrenze corrette

- **G2 `OK`**: inventario source-first costruito sulle pagine rese a 200 dpi da otto verificatori ciechi, uno per blocco di 2-4 pagine fisiche. 45 titoli, 20 formule numerate, 22 tabelle, 31 figure e 2 formule esposte senza tag, coincidenti uno a uno con l'inventario del Markdown. Il livello testo non era utilizzabile: sulla Circolare perde intere proposizioni.
- **G4 esteso** alle 20 formule e alle 19 tabelle della Circolare, 229 celle logiche confrontate; 9 tabelle non erano mai state riscontrate in questo ciclo.
- **Due difformità cambiavano un numero di progetto**, entrambe nella `[C3.3.5]`: `cos²` reso `cos` senza esponente e tre `≤` resi `<` agli estremi degli intervalli, nel § C3.3.8.3 sulle costruzioni a pianta circolare.
- Quattro famiglie di simbolo sostituito in silenzio verso la notazione degli Eurocodici: `c_peo` scritto `c_pe0`, accertato sui codepoint della prosa vettoriale; `ψ_λα` scritto `ψ_Mz`; `α_p` scritto `α_P`; `v_m,l` e `n_k` scritti `v_m,i` e `n_i`. Più `c_peA`, il punto dopo il tag `[C3.3.2]`, il separatore decimale a punto di `[3.3.3]` e `[C3.3.2]`, due didascalie e nove celle accorpate lasciate vuote.
- 40 occorrenze corrette, annotate come `AF-3.3-04…08` e `AF-COR-3.3-02`; diff confrontato con l'elenco dei rilievi, nessuna riga estranea.
- Corretti due controlli automatici che tacevano: la regex dei tag di `inventario-g0.py`, che ignorava la resa letterale `	ag*{[…].}`, e una soglia di posizione in `g4-localizza-formule.py` che faceva sparire il tag `[C3.3.7]`.
- Nuovo snapshot `d2e1eb41e27ea588f73f0cd799c714009a742a02f7ba9ecbb1ae322f9bc9181e`, 970 righe. G5 rieseguito con 0 errori e 0 avvisi.
- **Rilievi aperti: 12**, di cui 6 criteri di resa validi per tutto il corpus, in attesa di decisione. Le 31 figure non sono state confrontate con la fonte: G4 resta `PARZIALE`.
- Tutti i verificatori sono agenti AI; nessuna revisione umana integrale.
- **Firma:** CC (Claude Code).

## 2026-08-06 - § 4.2-B, quarto G6 non superato con due ERR-MD

- Sandro ha autorizzato l'aumento di `max_giri` da 3 a 4, la fase correttiva distinta dei nove rilievi del terzo G6 e il quarto controllo integrale cieco.
- Il correttore P2 ha applicato 9/9 interventi; revisione indipendente del diff `PASS`, con nove hunks limitati ai tag autorizzati. Nuovo snapshot `99af69e87987c10f50ab7eb10bb29428b61f84f35107ff011485697a8e1f80a2`.
- Preflight: 93 tag distinti, 21/21 asset, BOM conservato, lint senza errori, render di 28 pagine senza pagine vuote. Pacchetti r04 con confini ridisegnati e manifest 101/101.
- Quarto G6: inventario fonte-prima fresco, sei blocchi P2 ciechi e coordinatore P2 distinto su fascicolo 116/116. Il primo rapporto C-D è stato invalidato per contaminazione del contesto e ripetuto integralmente da un nuovo verificatore.
- L'adjudicazione ha chiuso `NORM` le parentesi alle righe 0536 e 0854. Il supplemento sulla riga 0778 ha aggiunto la pagina fisica 120 a 600 dpi, manifest 6/6, eliminando ogni `ERR-AUDIT` e `DUBBIO`.
- Esito autoritativo: 2 `ERR-MD`, 0 `ERR-AUDIT`, 0 `DUBBIO`. Rilievi: riga 0545, `\simeq` al posto di `=` nella formula non numerata di `\sigma_E`; riga 0778, virgola omessa dopo `\sigma_{cr,p}`.
- Il vivo è rimasto invariato durante G6. Con `giro_g6: 4` e `max_giri: 4`, lo scope è `SOSPESO`; G7 non avviato e nessun registro promosso. Serve una nuova decisione esplicita prima di correzione e quinto giro.
- Evidenze: `_tmp_render/cap04/vc-paragrafo-4-2b-20260806-r02/g6-r04/`; esito consolidato: `coordinamento/02-esito-consolidato-g6-r04.md`.
- Tutti i revisori attestati sono agenti AI; non è stata eseguita una revisione umana integrale dello scope.
- **Firma:** CDX (Codex).

## 2026-08-06 - § 4.2-B sospeso dopo il terzo G6, con nove ERR-MD congelati

- Ripresi e rieseguiti G0-G5 sullo snapshot valido, tutti `OK`; il precedente tentativo su uno snapshot superato e con confine N-B incompleto è stato conservato come storico ma escluso dal conteggio.
- Primo G6 integrale: 60 `ERR-MD`, ridotti a 59 dopo l'adjudicazione di non regressione sulla Figura C4.2.17, la cui lezione `aso I` è presente nella fonte. Correzione distinta completata e asset originale ripristinato byte per byte.
- Secondo G6 integrale: 18 `ERR-MD`, 0 `ERR-AUDIT`, 0 `DUBBIO`; correzione distinta completata. Snapshot risultante e tuttora vivo: `917134d6f52f66c2f8d62f6acfcbdd78a57f429f390a9f94f2046a598ff8aa8c`.
- Terzo G6, ultimo giro ordinario: inventario fonte-prima e sei blocchi P2 ciechi con coordinamento P2 separato; copertura completa di 24 pagine, 93 formule numerate, 4 gruppi matematici esposti non numerati, 15 tabelle e 12 figure.
- Esito consolidato: 9 `ERR-MD`, 0 `ERR-AUDIT`, 0 `DUBBIO`. Cinque rilievi eliminano graffe aggiunte e ripetono il membro sinistro come nella fonte; gli altri quattro riguardano [C4.2.68], [C4.2.70], [C4.2.81.a] e [C4.2.85].
- Il terzo G6 non ha modificato il Markdown vivo. Con `giro_g6: 3` e `max_giri: 3`, lo scope è `SOSPESO`; G7 non è stato avviato e nessun registro è stato promosso. Serve una decisione esplicita di Sandro prima di qualsiasi correzione o quarto giro.
- Verbale autoritativo: `_tmp_render/cap04/vc-paragrafo-4-2b-20260806-r02/g6-r03/coordinamento/01-verbale-coordinamento-g6-r03.md`; scheda: `verifica-conformita/scheda-scope-ntc2018-4.2-b.md`.
- Tutti i revisori attestati sono agenti AI; non è stata eseguita una revisione umana integrale dello scope.
- **Firma:** CDX (Codex).

## 2026-08-06 - § 3.3 vento, bonifica pre-G0 chiusa: 7 tabelle classificate, 20 correzioni, 3 anomalie della fonte annotate

- Classificate contro la fonte congelata le **7 tabelle che restavano** (C3.3.I, II, IV, V, VII, X, XIV), una per verificatore in contesto separato, poi adjudicate da chi coordina. **Nessuna delle 7 era conforme.**
- **Difetto più grave, corretto:** la Tab. C3.3.X riga 525 dava `c_pe,A = −0,8 − α/150` dove la Gazzetta stampa `− 0,8 **+** α/150`. Era l'unico scarto che cambiava un numero usato in progetto, con discontinuità di 0,4 al bordo dell'intervallo; il riscontro interno è la continuità con la riga sopra e con la Fig. C3.3.13.
- **Cinque versi di disuguaglianza corretti** in C3.3.V e C3.3.X (`<` dove la fonte stampa `≤`). Nel 2026 il registro di revisione li aveva archiviati come «differenze solo in alcuni estremi, ininfluenti»: il canone non lascia toccare quei glifi.
- Tolta da C3.3.VII la colonna «Caso» con le diciture *valori unici / principali / alternativi*, assenti dalla Circolare: applica alla VII la decisione già presa il 5/8 per la XI. Tolte da C3.3.IV le testate inventate `Tipologia` e `Parametro`. Reintegrati in C3.3.XIV la fascia `Direzione del vento Θ = 0° e Θ = 90°` e l'etichetta d'angolo `α₀ per Θ=0°, α₉₀ per Θ=90°`, che il file rendeva con un `α_S` inesistente nella fonte.
- Ripristinati **10 punti di moltiplicazione** che la fonte stampa e il file ometteva (C3.3.I, XV, XVI), per decisione di Sandro: la classe N resta a una via sola, il `·` si aggiunge dove la fonte giustappone e non si toglie mai dove la fonte lo stampa. Vale per tutto il corpus.
- **Tre anomalie della fonte conservate e annotate** in `cap03/annotazioni/3.3-anomalie-fonte.md`: `AF-3.3-01`, didascalia della Tab. C3.3.XVII riferita alle tettoie a semplice falda mentre la tabella è delle falde multiple; `AF-3.3-02`, la Tab. C3.3.I stampa `c_pe = -0,5 - -0,8·h/d` con **due meno consecutivi**, accertato sui codepoint e a 1200 dpi, e il file ora la riproduce alla lettera invece di correggerla in silenzio; `AF-3.3-03`, sei celle di C3.3.IV con `± 0.2` a punto decimale. Il README delle annotazioni avverte di leggerle prima di usare quelle tabelle in un calcolo.
- **Due errori di metodo del 5/8 scoperti e sanati.** `mappa-tabelle.json` sbagliava le voci I, II, III e IV e copriva solo metà della C3.3.XI, che è spezzata in **due raster affiancati**: il «110/110 coincidono» di quella sessione era stato ottenuto su un ritaglio privo della colonna J. Ricomposti i due raster e riverificata: l'esito regge. Mappa rifatta dalla fonte in `mappa-tabelle-260806.json`, con un campo che dichiara quali voci sono accertate.
- **Corretta l'affermazione, diffusa il 5/8 nel `CLAUDE.md` di progetto, che tutte le tabelle della Circolare siano raster:** le Tab. C3.3.I, II e III sono testo vettoriale in PalatinoLinotype, e lì i 600 dpi e la lettura dei codepoint del § 7.2 sono applicabili. È così che si è deciso `AF-3.3-02`.
- Decisioni di indirizzo prese da Sandro: punteggiatura finale delle didascalie **classe N dichiarata nel verbale**, nessun file toccato; testate a più livelli rese con lo **schema C3.3.XI** (fascia, lettere di zona, sottocampi), applicato a C3.3.II e C3.3.IV, così la parola «Zona» non si perde più.
- Chiarita e uniformata la convenzione degli accorpamenti, che il corpus applicava in modo incoerente: nelle testate l'etichetta che copre più colonne si scrive una volta e le celle coperte restano vuote; nel corpo valori ed etichette di riga si ripetono in tutte le celle logiche coperte. Uniformate C3.3.X, C3.3.XIV e C3.3.XV.
- Controlli finali su `cap03/3.3-vento.md`: 23 tabelle, **0 righe con numero di colonne incoerente**, nessun wikilink delle annotazioni con ancora inesistente, 966 righe.
- **Riancorati i riferimenti di pagina** del registro di revisione cap03, che rinviavano al PDF `_rid` cancellato con un offset stimato «≈ +4»: sostituito con l'ancoraggio accertato sui piedini della GU congelata, pagina fisica = pagina Gazzetta + 4, più rinvio alla mappa per tabella. Nello stesso registro rettificate con un blocco datato due affermazioni risultate false, il «`<`/`≤` ininfluenti» e l'«OK senza modifiche» della Tab. C3.3.X, con l'avvertenza che il controllo del 29/5/2026 è stato di lavorazione e non attestazione di conformità.
- **Snapshot congelato e G0 superato**: `cap03/3.3-vento.md` SHA-256 `97adc4ab0e8aeb55ce2d6502d209e3abed6f94cfade6f2b786601aceb9d5012f`, 966 righe, 74.893 byte; hash delle due fonti ricalcolati e coincidenti. Documento di scope: `verifica-conformita/scope-NTC2018-3.3-2026-08-06.md`. L'inventario è ricavato dal file e non dalle intenzioni, come impone il § 10 del ciclo dopo il caso del § 4.1: 47 heading meno i 2 separatori danno esattamente le 45 unità a registro; 20 formule taggate senza duplicati, 22 tabelle, 31 figure tutte presenti, 0 placeholder. Script riproducibile `inventario-g0.py`.
- **G1 `OK`** con limite dichiarato: la ricognizione di vigenza del 2026-08-04 è stata riusata e non rifatta, dichiarandolo, e verificata su questo perimetro; l'unico atto successivo censito, D.M. 9 marzo 2023 `23A01847`, tocca l'articolo 2 e i punti 11.4.2 e 11.5.2, tutti fuori dal § 3.3. Accertato che **Normattiva non indicizza i due atti**, perché hanno il testo tecnico in allegato e sono pubblicati in Supplemento Ordinario: la verifica si fa sulla Gazzetta Ufficiale e non è automatizzabile col connettore disponibile. Evidenza: `_tmp_render/cap03/vc-3.3-260806/g1-fonte-e-vigenza.md`.
- **G5 `OK`**: 31 immagini tutte presenti, 2 link relativi validi, 40 wikilink tutti risolti, 47 heading senza duplicati, 29 rinvii dell'indice di capitolo validi, riga di navigazione conforme; 0 errori e 0 avvisi. Script `g5-navigazione.py`.
- **G3 `PARZIALE`, con una scoperta che vale per tutto il corpus.** Parte NTC: confronto macchina completo e pulito, 1.805 parole allineate su 1.808 di prosa Markdown, **zero scarti lato Markdown**, cinque lato fonte tutti di apparato (Tab. 3.3.I, II, III e formule [3.3.7] e [3.3.1.b]), che vanno al G4. Parte Circolare: **il confronto macchina non è eseguibile per intero**, perché il livello testo è composto in un font a codifica rimappata e, quando una frase contiene un simbolo inline, si corrompe l'intera proposizione che lo contiene, non il solo simbolo. Verificato che stringhe stampate come `ossia con altezza minore`, `Si definisce grado di bloccaggio` e `tettoia libera` non compaiono in nessuna pagina del PDF; misura 7,7% di caratteri di controllo sulle pp. 54-75 contro lo 0,3% dell'NTC, e la percentuale sottostima il danno. Conseguenza registrata anche nel `CLAUDE.md`: chi dichiara conformità di una parte della Circolare sulla base di un confronto `pdftotext` misura una frazione del contenuto stampato, e la frazione persa è concentrata dove il testo tocca le grandezze; quella copertura si ottiene solo per via visiva, come fa il G6. Spiega anche perché sul § 4.1 il G6 trovò dieci difetti che tre controlli automatici non avevano visto. Evidenza: `g3-esito.md`.
- **G4 `PARZIALE`, parte NTC chiusa.** Confrontate le 3 tabelle del decreto, che la bonifica non aveva toccato perché riguardava le 19 della Circolare. Il test non è «il valore esiste nella pagina» ma «la sequenza dei valori compare nello stesso ordine e di seguito nella fonte», più riscontro visivo a 600 dpi. Tab. 3.3.I (36 valori) e Tab. 3.3.III (5 valori) **conformi**, con due sole differenze di classe N: la didascalia della 3.3.I senza spazio dopo il trattino e i quattro punti di sospensione della 3.3.III resi con tre. **Tab. 3.3.II difforme**: la fonte stampa `K_r` maiuscolo nell'intestazione mentre alla stessa p. fisica 58 la definizione sotto la [3.3.7] stampa `k_r` minuscolo, e il nostro file adottava la minuscola senza dichiararlo. Anche qui la posizione di partenza era sbagliata: la Tab. 3.3.III è a p. 59, non 58. Evidenza: `g4-esito-tabelle-ntc.md`.
- **Prima correzione di classe C del corpus, `AF-COR-3.3-01`.** Ricorrono tutte le condizioni del § 5 del ciclo: difetto tipografico, lettura corretta attestata dentro lo stesso atto e sulla stessa pagina, nessun glifo della lista vietata toccato perché cambia solo la cassa di una lettera, nessun valore alterato; è la famiglia che il ciclo indica come candidabile alla classe C nei propri esempi. Il file conserva `k_r` e porta accanto la nota di trascrizione prescritta: prima di oggi la stessa forma c'era ma **senza dichiararla**, cioè come correzione silenziosa.
- **Catena degli hash della giornata**: `97adc4ab0e8aeb55ce2d6502d209e3abed6f94cfade6f2b786601aceb9d5012f` congelato all'apertura del G0, 966 righe, poi `dae92970806bcdda5391b000162d8dc44badd20166d3f7ba6e335f20dfbe87f0` dopo la nota AF-COR, 968 righe. Controlli rifatti sul nuovo snapshot: 23 tabelle con 0 righe a colonne incoerenti, G5 con 0 errori e 0 avvisi, G3 invariato con la nota AF-COR esclusa dal confronto come prevede il § 5.
- Rilievi aperti: 0. Gate: `G0 OK, G1 OK, G3 PARZIALE, G4 PARZIALE, G5 OK`, gli altri `DA_FARE`. Nessuno stato `VC-OK` attribuito. **Il G6 non potrà essere né coordinato né eseguito da CC**, che ha scritto le correzioni di oggi: lo impone il § 6.7 del ciclo.
- Evidenze: `_tmp_render/cap03/bonifica-3.3-260805/02-rilievi-bonifica-260806.md`, ritagli e raster nativi in `adjudicazione/`, script `rileva-tabelle.py` e `adjudica-punti-critici.py`.
- Controlli eseguiti da agente AI, senza revisione umana integrale.
- **Firma:** CC (Claude Code).

## 2026-08-06 - § 4.2-A NTC + § C4.2-A Circolare chiuso VC-OK

- Sandro ha autorizzato la fase correttiva delle 11 occorrenze congelate, il quinto G6 integrale e l'aumento di `max_giri` da 4 a 5. Un correttore P2 distinto ha applicato soltanto gli 11 interventi ammessi; la revisione indipendente del diff li ha confermati senza modifiche estranee.
- Snapshot finale di `cap04/4.2-acciaio.md`: SHA-256 `eccefb75094e290c75a9496d4d902bcff9bfecd7542affa566c23c69296e8994`. Render di 24 pagine senza pagine bianche, 61/61 tag con parentesi quadre, 39 heading, 64 righe tabellari e 10 asset presenti.
- Quinto G6 integrale e cieco: inventario fonte-prima e quattro blocchi P2 in contesti separati, con copertura 801/801 righe, 17/17 pagine e 10/10 asset. Il solo quesito descrittivo su `φ₀` è stato adjudicato su ritaglio a 600 dpi ed esame dei codepoint; il Markdown è risultato corretto.
- Consolidamento finale P2: `ERR-MD=0`, `ERR-AUDIT=0`, `DUBBIO=0`; G6 `OK`. Manifest delle evidenze validato 117/117, SHA-256 `1e6493ca6839280f59f41ac35b293ac1e9710cb85bb6d6e9b084e16858231bd7`.
- G7 `OK`: manifest finale validato 14/14, SHA-256 `e54ec39734ac2f9ce737c2cab75a9dbeea562517e3041527c015aec832a1ca34`; 37/37 unità di dettaglio e 37/37 righe dell'indice promosse. Creato il master autonomo `ntc2018--norme-costruzioni--cap04-2a`, promosso a `VC-OK al 2026-08-06`.
- Le unità `4` e `C4`, gli altri sottoscope 4.2, il Capitolo 4 e il master dell'intero corpus non sono stati promossi e restano `VC-DA-FARE`. Lint finale: 0 errori, 1 avviso atteso globale su `NTC-4.2` e 357 informazioni.
- Scope formale: `verifica-conformita/scope-NTC2018-4.2-A-2026-08-06.md`; verbale: `verifica-conformita/verbale-VC-NTC2018-4.2-A-2026-08-06.md`; evidenze conclusive: `_tmp_render/cap04/vc-paragrafo-4-2a-20260804-r01/g6-r05/` e `g7/`.
- Una revisione finale P2 indipendente e in sola lettura ha ripetuto il validatore e confermato il rilascio senza rilievi; evidenza in `g7/03-revisione-finale-p2.md`.
- Tutti i revisori attestati sono agenti AI; non è stata eseguita una revisione umana integrale dello scope.
- **Firma:** CDX (Codex).

## 2026-08-05 - § 3.3 vento, scope aperto e bonifica pre-G0 avviata; le tabelle della Circolare sono immagini

- Aperto lo scope `ntc2018-3.3` come scope **unico**: 27 pagine fonte e 20 formule numerate stanno sotto entrambe le soglie del § 4.B.6. Scheda in `verifica-conformita/scheda-scope-ntc2018-3.3.md`, stato `SOSPESO` per riprendere a contesto pulito.
- Precondizioni assolte: hash delle due GU ricalcolati e coincidenti; **45 unità a registro tutte `COMPLETA`**, quindi il gate § 4.B.4 che sul § 4.2 aveva bloccato 72 mappature qui è già superato; confini accertati **a vista** e non dedotti, § 3.3 NTC alle pagine fisiche 56-60 senza pagine condivise, § C3.3 Circolare alle 54-75 con la sola p. 54 condivisa.
- Apparato delle formule conforme: 8 tag NTC e 12 Circolare, coincidenti uno a uno con la fonte.
- **Il problema delle tre impaginazioni non esisteva.** Confronto pagina per pagina: la Circolare in `raw/` è identica alla GU congelata su tutte e 348 le pagine, l'NTC su 371 su 372 tolte due filigrane (`Con Segnalibri…` e `scaricato da www.ingenio-web.it`). Il registro di dettaglio da 1724 righe **non va toccato**; resta da riancorare solo ciò che citava il PDF `_rid` cancellato.
- **Le tabelle della Circolare sono raster incorporati, non testo**: 145 nelle pagine dello scope, risoluzione nativa fra 173 e 354 dpi. I 600 dpi che il § 7 pretende non sono raggiungibili, oltre il nativo si interpola: la prova si ottiene estraendo il raster, non ri-renderizzando la pagina, e la lettura dei codepoint del § 7.2 lì non è applicabile. Le tabelle dell'NTC sono invece testo regolare.
- **Le parentesi quadre dei tag di formula non si estraggono come quadre**: nelle due GU lo stesso `[…]` esce come `> … @`, `" … #` o `[ … ]` secondo il font. Tre conteggi sono risultati sbagliati prima di accorgersene. Ogni controllo automatico sui tag deve cercare il contenuto e non i delimitatori.
- Bonifica: indice interno e note redazionali portati fuori dal file normativo (1050 → 962 righe), note in `cap03/annotazioni/3.3-note-redazionali.md`.
- **Corrette 12 occorrenze di `c_f` in `c_F`** nelle Tab. C3.3.XV, XVI e XVII e nel testo di raccordo: la fonte usa `c_F` per il coefficiente di forza, mentre `c_f` minuscolo è il coefficiente d'attrito, e il Markdown fondeva due grandezze distinte. Accertato con entrambi i metodi del § 7, concordi: a vista sul raster nativo e sulla codifica dei caratteri (`c` corpo 7,8 seguito da `F` corpo 4,8). Nella stessa scansione `q_p` è risultato minuscolo, e lì il Markdown era già giusto.
- Altre correzioni: reintegrato `(α in °)` nella didascalia della Tab. C3.3.VIII; `falda doppia` riportato a `doppia falda` nella C3.3.XVI; nella Tab. C3.3.XI tolta la colonna «Caso», le cui diciture *valori unici / principali / alternativi* non compaiono nella Circolare, sotto-righe rese ripetendo α per decisione di Sandro, e reintegrata la riga d'intestazione `Direzione del vento Θ = 0°`.
- Classificate 3 tabelle su 10 contro la fonte: C3.3.VIII 60/60 valori coincidenti, C3.3.XI 110/110, C3.3.XVI tutte. **Le correzioni pregresse del maggio-giugno risultano riallineamenti verso la fonte, non modifiche della fonte: nessuna nota `AF-COR` dovuta.**
- Rilievi aperti: **R4**, i punti di moltiplicazione che la fonte stampa e il Markdown omette, decisione di indirizzo in `attesa_decisione`; **R6**, classe A, la didascalia della Tab. C3.3.XVII dice «tettoie a semplice falda» mentre la tabella riguarda le falde multiple, e la Gazzetta stampa davvero così.
- G0 non aperto: la bonifica non è conclusa e congelare adesso costringerebbe a riaprire i gate, che è l'incidente occorso al § 4.2-a.
- Evidenze: `_tmp_render/cap03/bonifica-3.3-260805/`.
- **Firma:** CC (Claude Code).

## 2026-08-05 - § 4.2-A, quarto G6 non superato con 11 ERR-MD

- Eseguito il quarto G6 integrale sullo snapshot `8404fcb9e41a73d8ab6af7cd0be02da5e3dc32a3888e2c7a2ad315a0b5927bdd`, con inventario fonte-prima e quattro blocchi ciechi P2 da 4/4/4/5 pagine.
- Il primo confine testuale B2/B3 lasciava la riga 373 fuori dalla pagina pertinente: i rapporti preliminari sono stati conservati come invalidati, il confine è stato corretto a B2 144-372 e B3 373-598 e i due blocchi sono stati ripetuti da verificatori freschi. Copertura definitiva: 802/802 righe, 17/17 pagine, 10/10 asset.
- Adjudicati dieci quesiti su ritagli a 600 dpi e codepoint, per 11 occorrenze elementari. Confermati: tre `E’→È`, punto omesso in `4.2.4.`, punto aggiunto in `C4.2.`, `N_pl.Rd` reso `N_{pl,Rd}` nella [4.2.36], riferimento redazionale assente dalla fonte, `é→è`, due segni `:` aggiunti e testo alternativo redazionale dell'asset C4.2.I.
- Consolidamento P2: `ERR-MD=11`, `ERR-AUDIT=0`, `DUBBIO=0`; G6 `KO`. Le due famiglie `ERR-AUDIT` del terzo giro sono risolte e nessun rilievo del giro precedente persiste.
- Il Markdown normativo è rimasto invariato. Controlli meccanici superati; manifest validato 125/125. G7 non avviato e nessun registro promosso.
- Con `giro_g6: 4` e `max_giri: 4`, lo scope è sospeso in attesa dell'autorizzazione esplicita di Sandro ad alzare il limite a 5. Solo dopo sono ammesse la correzione distinta delle occorrenze congelate e l'esecuzione di un quinto G6 integrale.
- Evidenze: `_tmp_render/cap04/vc-paragrafo-4-2a-20260804-r01/g6-r04/`.
- **Firma:** CDX (Codex).

## 2026-08-05 - § 4.2-A, terzo G6 non superato per copertura incompleta

- Consolidati i cinque rapporti ciechi r03 sullo snapshot `8404fcb9e41a73d8ab6af7cd0be02da5e3dc32a3888e2c7a2ad315a0b5927bdd`; hash del Markdown e delle due fonti ufficiali ricalcolati e coerenti.
- Accertate due famiglie persistenti `ERR-AUDIT`: 19 righe normative non giudicate ai confini dei pacchetti e asset C4.2.2 non confrontato insieme alla pagina fonte pertinente.
- Le partizioni r01, r02 e r03 sono identiche e non rispettano il ridisegno obbligatorio dei confini. I cinque `OK` locali non consentono quindi di promuovere G6.
- G6 impostato a `KO`; scope sospeso con `giro_g6: 3` e `max_giri: 3`, in attesa dell'autorizzazione esplicita di Sandro a un quarto G6 integrale. G7 non avviato, nessun registro promosso e nessun file normativo modificato.
- Evidenza: `_tmp_render/cap04/vc-paragrafo-4-2a-20260804-r01/g6-r03/00-consolidamento-coordinato.md`.
- **Firma:** CDX (Codex).

## 2026-08-05 - Skill Codex `orchestra-vc-ntc2018`

- Creata in `.agents/skills/orchestra-vc-ntc2018/` la skill locale che seleziona modello, livello di ragionamento e modalità di delegazione in base alla fase VC e al rischio dell'attività.
- Definiti quattro profili: P0 Terra `medium` per operazioni deterministiche; P1 Sol `high` per collazione e interpretazione; P2 Sol `xhigh` per G6, apparati critici e rilascio; P3 Sol `max` per adjudicazioni eccezionali e non regressione.
- Inserite regole vincolanti per G6: contesti freschi, blocchi di 3-5 pagine, output separati, Markdown vivo in sola lettura, coordinatore distinto da traspositore e correttore, nessun uso di `Ultra`.
- Tre iterazioni di forward-test read-only hanno rilevato e corretto un'interpretazione troppo restrittiva del protocollo: un secondo verificatore nello stesso modello, ma in contesto separato, soddisfa l'indipendenza; un'altra famiglia o una revisione umana sono garanzie aggiuntive, non gate bloccanti.
- Validazione finale con `quick_validate.py`: `Skill is valid!`. Nessun file normativo, registro, scheda di scope o stato VC modificato.
- **Firma:** CDX (Codex).

## 2026-08-05 - § 4.2-A, terzo G6 in consolidamento

- Correzione distinta di due soli punti adjudicati a 600 dpi: aggiunto il punto terminale a [4.2.7], rimosso quello non stampato a [4.2.40]. Nuovo snapshot `8404fcb9e41a73d8ab6af7cd0be02da5e3dc32a3888e2c7a2ad315a0b5927bdd`; render superato, nessun tag con parentesi tonde.
- I cinque rapporti ciechi N-A, N-B, N-C, C-A e C-B del terzo G6 sono `OK`. Il consolidamento resta da eseguire; G6 non è ancora promosso e G7 non è avviato.
- Evidenze: `_tmp_render/cap04/vc-paragrafo-4-2a-20260804-r01/g6-r03/`.
- **Firma:** CDX (Codex).

## 2026-08-04 - § 4.2-A, G0-G5 rieseguiti sullo snapshot riallineato

- Mappature 37/37 complete; lint del registro a 0 errori e 1 avviso atteso globale.
- Render r03 riuscito sullo snapshot `1df10fb57a74f090c38cf2dfc85a254fe084a8e4164dee914be101aa74a6d94e`, con 61 formule numerate e nessun tag reso fra parentesi tonde.
- G0-G5 nuovamente `OK`; G6 resta da eseguire in forma integrale e cieca.
- Evidenze: `_tmp_render/cap04/vc-paragrafo-4-2a-20260804-r01/g0-g5-r03/`.
- **Firma:** CDX (Codex).

## 2026-08-04 - § 4.2, riallineamento mappature dopo la suddivisione

- Convertite meccanicamente in heading Markdown le sole rubriche del § 4.2 già presenti in grassetto nei quattro file di sottoscope, senza modificare il testo normativo.
- Lint del registro: 0 errori, 1 avviso atteso perché il titolo 4.2 ricorre, per ragioni di navigazione, in quattro file.
- Tutte le mappature § 4.2 risultano ora `COMPLETA`; i quattro snapshot e i gate G0-G6 sono stati riaperti, poiché la normalizzazione modifica gli hash di riferimento.
- **Firma:** CDX (Codex).

## 2026-08-04 - § 4.2-A, fase correttiva r02

- Applicate esclusivamente le 17 famiglie `ERR-MD` congelate dal primo G6, per 34 siti materiali, inclusa l'anomalia di fonte conservata `AF-4.2-a-05`.
- Nuovo snapshot di `cap04/4.2-acciaio.md`: `666f36bf78861f41acc09ea3733524b59431eb26da09a62a7789ddff45be1d4d`.
- Render r02 riuscito con `strumenti/render-capitolo.py`; controllo della resa superato, senza tag numerati fra parentesi tonde.
- Il lint del registro non supera il controllo: 72 errori e 73 avvisi di mapping dopo la suddivisione in quattro file del § 4.2. Non è stato eseguito G7 e nessun registro è stato promosso.
- Evidenze: `_tmp_render/cap04/vc-paragrafo-4-2a-20260804-r01/correzione/r02/`; stato operativo nella scheda `verifica-conformita/scheda-scope-ntc2018-4.2-a.md`.
- **Firma:** CDX (Codex).

## 2026-08-04 - § 4.1 NTC + § C4.1 Circolare chiuso VC-OK

- Sandro ha autorizzato il settimo giro. Un correttore distinto ha applicato esclusivamente R06-01, inserendo la virgola U+002C stampata dalla fonte dopo `A_c` alla riga 993; nuovo snapshot SHA-256 `93360710906737ff6a9c3d5f91b54e353282e2c1ab08d57deab099f7465d8964`.
- Controlli post-correzione: un solo byte aggiunto, 1957 righe invariate, lint 0 errori e 0 avvisi, render di 50 pagine senza pagine vuote e controllo dei tag superato.
- Eseguito il settimo G6 integrale e cieco con inventario source-first e dieci blocchi in contesti separati: 37/37 pagine, 81 occorrenze di formule numerate, 23 gruppi matematici non numerati secondo il criterio finale, 11 tabelle o griglie con 271 celle logiche e 17 figure.
- Adjudicazione su ritagli a 600 dpi, codepoint e render effettivo: zero `ERR-MD`, zero `ERR-AUDIT`, zero `DUBBIO`, zero rilievi persistenti e zero nuovi rilievi materiali. Il file normativo è rimasto invariato durante il G6.
- Manifest G6 validato 50/50, SHA-256 `1e36d3f86830cb0eb07fe6f8b0a36ddcc61cf5ea5bdb691cb591ae4d4a691597`.
- G7 superato: manifest dello scope validato 21/21, 136/136 unità promosse a `COMPLETA/OK`, 136/136 righe dell'indice promosse a `VC-OK al 2026-08-04`, master autonomo promosso e master del corpus confermato `VC-DA-FARE`.
- Lint conclusivo del registro: 1.724 righe, 0 errori, 0 avvisi e 195 informazioni su linee storicamente spostate.
- Verbale, scope e manifest finali in `verifica-conformita/`; evidenze con correzione, G6 e G7 in `_tmp_render/cap04/vc-paragrafo-4-1-20260804-r04/`.
- Non è stata eseguita una revisione umana integrale.
- Creato e poi preso in carico da CDX il prompt per lo scope § 4.2 NTC + § C4.2 Circolare; il file corrente è `PROMPT-IN-CORSO-CONVERSIONE-4-2.md`. Avviate le precondizioni, compresa la risoluzione delle 72 mappature `DA_VERIFICARE` e il dimensionamento in sotto-scope autonomi.
- **Firma:** CDX (Codex).

## 2026-08-03 - Fase correttiva e sesto G6 del § 4.1, non superato

- Applicate da un correttore distinto le 7 famiglie congelate dal quinto G6, pari a 12 siti materiali. Il nuovo snapshot è `5b0d4356251f0d42b35b0b84e65c7dc11a18b21bf4a14dd5e23497551d253e9c`; la Figura C4.1.7 è stata riestratta a 600 dpi con la cornice completa.
- Controlli post-correzione: lint 0 errori e 0 avvisi; render di 50 pagine senza pagine vuote; controllo dei tag superato; manifest correttivo validato 22/22. Evidenze in `_tmp_render/cap04/vc-paragrafo-4-1-20260803-r03/correzione/`.
- Eseguito sul nuovo hash il sesto G6 integrale e cieco. Inventario fonte-prima: 37 pagine, 81 occorrenze di formule numerate, 20 gruppi matematici non numerati, 11 tabelle o griglie con 315 celle logiche e 17 figure.
- I difetti iniziali di confine di sei pacchetti sono stati rilevati prima dell'esito, corretti e seguiti da riesecuzioni separate. I rapporti preliminari sono esclusi; il controllo definitivo chiude con zero `ERR-AUDIT`.
- Esito consolidato: **G6 NON SUPERATO**, una famiglia `ERR-MD` in un sito materiale, zero `DUBBIO`, zero `ERR-AUDIT` e zero rilievi persistenti. Alla riga 993 manca la virgola stampata dalla fonte dopo `A_c` prima di «essendo».
- Il rilievo è confermato da ritaglio a 600 dpi, codepoint U+002C e confronto indipendente. La regola di non regressione sulla [C4.1.4] ha invece confermato la forma corrente `0.015` con punto.
- Render corrente: 50 pagine, nessuna vuota, 81/81 tag con le parentesi della fonte, `[4.1.44)` conservato. Manifest del G6 validato 56/56.
- Nessuna correzione normativa è stata applicata durante il sesto G6; l'hash è rimasto invariato. G7 non avviato, registro di dettaglio e indice VC non promossi.
- Il sesto giro coincide con `max_giri: 6`: scope sospeso in attesa dell'autorizzazione di Sandro ad alzare il limite a 7. Solo dopo sono ammesse la correzione della sola R06-01 e l'esecuzione di un settimo G6 integrale.
- Evidenze in `_tmp_render/cap04/vc-paragrafo-4-1-20260803-r03/g6/`: rapporto `04-rapporto-finale-g6-r06.md`, manifest `05-manifest-sha256-g6-r06.txt`, rapporti di blocco ed evidenze di adjudicazione.
- **Firma:** CDX (Codex).

## 2026-08-03 - Fase correttiva e quinto G6 del § 4.1, non superato

- Applicate da un correttore distinto le 43 famiglie congelate dal quarto G6, pari a 61 siti materiali. Il nuovo snapshot è `a1df27fd79c2ef946256cae1e12fcf41d0d542d96e71676382aab8c5382b6700`; il confronto ha rilevato 60 righe modificate, tutte autorizzate e nessuna estranea.
- Controlli post-correzione: lint 0 errori e 0 avvisi; render di 49 pagine senza pagine vuote; controllo dei tag superato; 17 immagini collegate e nessun asset mancante. Evidenze correttive in `_tmp_render/cap04/vc-paragrafo-4-1-20260803-r02/correzione/`.
- Eseguito sul nuovo hash il quinto G6 integrale e cieco. Inventario fonte-prima: 37 pagine, 81 occorrenze di formule numerate, 21 gruppi matematici esposti non numerati, 11 tabelle o griglie con 304 celle logiche e 17 figure.
- I primi pacchetti dei blocchi non contenevano le pagine fonte. Il difetto è stato rilevato prima del congelamento, classificato come problema di confezionamento e sanato ripetendo integralmente i nove confronti su pacchetti completi; i rapporti preliminari sono esclusi dalla prova. Il controllo definitivo chiude con zero `ERR-AUDIT`.
- Esito consolidato: **G6 NON SUPERATO**, 7 famiglie `ERR-MD` per 12 siti materiali, zero `DUBBIO`, zero `ERR-AUDIT` e zero rilievi persistenti. Le famiglie riguardano un accento, un due punti, quattro pedici `clim`, un bordo di figura e cinque punti finali.
- Tutti i candidati sono stati decisi su ritagli a 600 dpi e, dove pertinente, sui codepoint della fonte, con seconda lettura indipendente. Le false positività strutturali e tipografiche sono state chiuse come normalizzazioni ammesse.
- Nessuna correzione normativa è stata applicata durante il quinto G6; l'hash è rimasto invariato. G7 non avviato, registro di dettaglio e indice VC non promossi.
- Il quinto giro coincide con `max_giri: 5`: scope sospeso in attesa dell'autorizzazione di Sandro ad alzare il limite a 6. Solo dopo sono ammesse la correzione delle 7 famiglie congelate e l'esecuzione di un sesto G6 integrale.
- Evidenze in `_tmp_render/cap04/vc-paragrafo-4-1-20260803-r02/g6/`: rapporto `04-rapporto-finale-g6-r05.md`, manifest `05-manifest-sha256-g6-r05.txt`, rapporti di blocco ed evidenze di adjudicazione.
- **Firma:** CDX (Codex).

## 2026-08-03 - Quarto G6 del § 4.1 non superato, budget esaurito

- Eseguito il quarto G6 integrale e cieco sullo snapshot `a04eabdedcdb7f4d112d61f4b97291e3881f4a583784f1edf7f42f0bf4d0bc03`, rimasto invariato per tutta la verifica. Perimetro: 37/37 pagine ufficiali del § 4.1 NTC e § C4.1 Circolare.
- Metodo: inventario source-first congelato prima della riconciliazione, dieci blocchi indipendenti con confini ridisegnati rispetto al giro precedente, adjudicazione diretta sulla Gazzetta mediante 45 prove a 600 dpi e controllo dei codepoint nel caso ambiguo.
- Inventario finale: 81 occorrenze di formule numerate, 13 gruppi matematici esposti non numerati, 11 tabelle o griglie con 274 celle logiche non vuote più una vuota strutturale, 17 figure.
- Esito: **G6 NON SUPERATO**, con 43 famiglie `ERR-MD` per 61 siti materiali, zero `DUBBIO`, zero `ERR-AUDIT` e zero rilievi persistenti dai giri precedenti. N1 e C3 sono risultati conformi dopo adjudicazione.
- Il rilievo matematico più rilevante è l'omissione del pedice in `ν_l` alla riga 1930. Gli altri scarti sono soprattutto di punteggiatura e maiuscole/minuscole; sono stati confermati anche `Ø` reso `Φ` e i decimali di fonte `0.015` e `0.4` trasformati silenziosamente in virgole. Non risultano variazioni di coefficienti, valori o versi di disuguaglianza.
- Nessuna correzione applicata al Markdown normativo. G7 non avviato; registro di dettaglio e indice VC non promossi. La riga autonoma del master resta `VC-IN-CORSO`, con G6 `KO` e 43 rilievi aperti.
- Il quarto giro coincide con `max_giri: 4`: scheda di scope sospesa in attesa dell'autorizzazione di Sandro ad alzare il limite a 5. Solo dopo sono ammesse la fase correttiva sulle famiglie congelate e un quinto G6 integrale sul nuovo hash.
- Evidenze in `_tmp_render/cap04/vc-paragrafo-4-1-20260803-r01/g6/`: rapporto finale `04-rapporto-finale-g6-r04.md`, manifest `05-manifest-sha256-g6-r04.txt`, rapporti dei dieci blocchi e prove di adjudicazione.
- **Firma:** CDX (Codex).

## 2026-07-31 (pomeriggio) - Fase correttiva del § 4.1: undici rilievi chiusi

- Sandro ha ratificato le due decisioni di indirizzo lasciate aperte dal G6: regime della classe C per i guasti tipografici della fonte e correzione della resa dei tag nel template invece che nelle formule. La fase correttiva è quindi partita su tutti i rilievi, non solo su quelli indipendenti dalla politica.
- Chiuso preventivamente il dubbio `G6-D1` su ritaglio a 600 dpi della pagina fisica 89 della Circolare: la dicitura «dove:» è presente nel riquadro di formule della Fig. C4.1.9. Diventa l'undicesimo rilievo e l'omissione è stata sanata.
- Classe C, con nota di trascrizione nel file e attestazione citata: `N_Eϕ` → `N_Ed` (attestato a p. fisica 82); `T_ed`/`V_ed` → `T_Ed`/`V_Ed` (attestati a p. fisica 85); `Δσμ` → `Δ_sm` (attestato a p. fisica 92 della Circolare, due righe sopra).
- Classe A, fonte ripristinata o conservata: tag `[4.1.44)` con la tonda di chiusura, che annulla la regressione del 30/7; duplicazione del tag `[4.1.50]`; **`Σ A₁`**, che la prima stesura della procedura dava per correggibile. La verifica dell'elenco dei simboli a p. fisica 85 ha mostrato che la Gazzetta definisce proprio `Σ A₁` con la cifra: manca l'attestazione interna di `A_l`, quindi il Markdown scrive ora `A_1` in tutte e tre le occorrenze, lasciando `a_l` dove la fonte usa la lettera.
- Difformità sotto qualunque politica, sanate: estremi aggiunti alla sommatoria della [4.1.12.f]; omissione di «per il rapporto»; omissione di «frattile 5%:» e «frattile 95%:»; intestazioni inventate nelle tabelle dei mandrini e di `α_c`, sostituite da intestazioni vuote con il testo della fonte ripristinato.
- Catena degli hash: da `a05a99c00f13bc7e95b499f1136c927e0a0ffa19d9289e8b3ff77ee326f2acb4` a `a04eabdedcdb7f4d112d61f4b97291e3881f4a583784f1edf7f42f0bf4d0bc03`. `indice-cap04.md` non toccato.
- Controlli: diff di 32 righe tutte riconducibili a un rilievo e nessuna estranea; 81 formule numerate con la sola duplicazione di fonte; unico tag a resa letterale `[4.1.44)`; 139 heading, 17 immagini, 14 tabelle invariati; tre note `AF-COR` con altrettante sezioni nelle annotazioni; lint 0 errori e 0 avvisi.
- Creata `cap04/annotazioni/` sul modello del capitolo 3, con `4.1-anomalie-tipografiche-fonte.md` che documenta in modo permanente le sei anomalie, tre corrette e tre conservate.
- Migrazione al nuovo meccanismo: `PROMPT-IN-CORSO-PARAGRAFO-4-1-VC-OK.md` chiuso **per migrazione e non per completamento**, con avvertenza in testa al file; stato trasferito in `verifica-conformita/scheda-scope-ntc2018-4.1.md`, prima scheda di scope del progetto.
- La fase non assegna `G6=OK` né `VC-OK`. Serve un G6 integrale sul nuovo hash: sarebbe il quarto e il budget è esaurito, quindi richiede l'autorizzazione di Sandro. Avendo CC eseguito la correzione, il prossimo G6 non può essere coordinato da CC.
- Attuata anche la seconda decisione: nuovo `strumenti/render-capitolo.py`, che rende un file del corpus con la macro `\tagform@` ridefinita e poi verifica da sé il risultato, uscendo in errore se trova anche un solo tag con le parentesi tonde. Prima non esisteva uno script di render condiviso e la macro non avrebbe avuto dove vivere. Provato sul § 4.1: 49 pagine, nessuna pagina vuota, 93 tag resi con le quadre come la Gazzetta e il tag anomalo `[4.1.44)` riprodotto alla lettera.
- Evidenze in `_tmp_render/cap04/vc-paragrafo-4-1-20260731-r01/`, con registro, diff, manifest e render post-correzioni.
- **Firma:** CC (Claude Code).

## 2026-07-31 - Procedura di conversione e verifica riscritta

- Creato `skills/conversione-normativa/references/ciclo-conversione-verifica.md`: procedura unica per tutte le normative, con innesco a frase, scheda di scope, precondizioni distinte fra apertura e ingresso a G0, tre classi di scostamento, metodo del G6 in cieco, standard di prova, loop correttivo e uscite dal ciclo. Sostituisce i prompt monouso da 16 KB, che duplicavano la procedura a ogni scope e la facevano derivare.
- `skills/conversione-normativa/SKILL.md`: rimando al ciclo in testa, sezione «Fedeltà alla fonte e refusi», regole nuove sui tag di formula, descrizione aggiornata con le frasi di innesco.
- `skills/controllo-serrato-ntc2018/SKILL.md`: rimando al ciclo, sostituito il divieto secco di correggere i refusi con la regola a tre classi.
- `skills/controllo-serrato-ntc2018/references/protocollo-conformita-tabelle-formule.md`: nuovo stato di registro `AF-COR`; standard di prova per l'adjudicazione e regola di non regressione in § 9; sanata la contraddizione del principio 2.6, che vietava ogni correzione mentre il § 10 la ammette entro la classe C. Riordinata la numerazione del § 9, che era rimasta spezzata.
- `AGENTS.md` del progetto: nuovo § «Ciclo di conversione e verifica» con le frasi di innesco, § «Metodo» riscritto sulle tre classi con clausola di primazia, aggiornata la frase su `verifica-conformita/` che dava la cartella come non ancora nata.
- Revisione critica indipendente affidata al consulente Fable 5: otto rilievi bloccanti, tutti recepiti. I più rilevanti: esclusione dura di cifre, coefficienti, esponenti, apici, operatori, segni, disuguaglianze e unità dalla classe C, senza la quale sarebbe stato lecito aggiungere un apice a `f_cd` e raddoppiare una resistenza; attestazione ristretta allo stesso documento e non allo scope, perché la Circolare non può correggere il decreto; consegna del canone delle classi ai verificatori ciechi, senza la quale il loop non converge mai perché le note legittime verrebbero risegnalate a ogni giro; regola di sblocco del tetto dei giri, altrimenti il § 4.1 sarebbe rimasto in stallo formale; migrazione dei prompt ancora `IN-CORSO` verso le schede di scope; correzione del caso `Σ A₁`, che nel primo testo era dato come correggibile mentre l'attestazione interna non esiste.
- Nessuna conversione avviata, nessun file normativo modificato, nessuno stato VC cambiato.
- **Firma:** CC (Claude Code), con revisione indipendente Fable 5.

## 2026-07-30 (sera) - Terzo G6 del § 4.1 non superato: 10 ERR-MD

- Eseguito il G6 integrale sullo snapshot r03 `a05a99c00f13bc7e95b499f1136c927e0a0ffa19d9289e8b3ff77ee326f2acb4`, richiesto dal protocollo dopo la correzione del mattino. Il file normativo non è stato modificato: hash a fine controllo identico a quello iniziale.
- Metodo: fase fonte-prima congelata alle 17:09 da CDX (137 titoli, 81 formule numerate, 31 gruppi non numerati, 11 tabelle per 271 celle, 17 figure); riconciliazione affidata a undici verificatori ciechi in contesti separati, uno per blocco di pagine fonte, senza conteggi attesi né notizia dei rilievi pregressi; adjudicazione finale di ogni rilievo sulla Gazzetta a 600 dpi e, nei casi di ambiguità grafica, sulla codifica dei caratteri del PDF.
- Esito: **G6 NON SUPERATO**, 10 `ERR-MD` e 1 `DUBBIO`, `ERR-AUDIT=0`. Nessun rilievo altera una prescrizione: sono tutti difetti di fedeltà documentale.
- **Regressione accertata**: la fonte stampa `[4.1.44)`, quadra in apertura e tonda in chiusura. Il G6 r02 aveva concluso il contrario e la correzione del mattino ha fatto divergere il file dove prima coincideva. Prova in `adjudica/01-ntc-p87-tag-4.1.44.png`.
- Refusi della fonte corretti in silenzio dal Markdown: `Σ A₁` con la cifra 1 reso `\sum A_l` nella [4.1.37], accertato anche sulla codifica (`0x31` contro `0x6c` di `T_Rld`); `T_ed`/`V_ed` minuscoli resi `T_Ed`/`V_Ed` nella [4.1.40]; `M_Ed = e · N_Eϕ` reso `N_Ed` a p. 82; `Δσμ= 0,75 (h – x)` con tag `[C4.1.10 ]` reso `\Delta_{sm}` nella Circolare a p. 92.
- Testo della fonte omesso: «per il rapporto» a p. 90 della Circolare; «frattile 5%:» e «frattile 95%:» davanti a [C4.1.14.a] e [C4.1.14.b] a p. 97.
- Struttura e testo aggiunti: la riga di testo dei mandrini a p. 99 della Circolare è resa come tabella con intestazioni «Diametro barre» e «Diametro mandrino»; la definizione a tratti di `α_c` a p. 84 delle NTC come tabella con intestazioni «Valore» e «Condizione». Nessuna delle quattro diciture è in fonte.
- Notazione aggiunta: nella [4.1.12.f] la fonte ha il solo `n` sotto il segno di sommatoria, il Markdown scrive `\sum_{i=1}^{n}`.
- Dubbio aperto: la presenza di «dove:» nel riquadro di formule della Fig. C4.1.9, p. 89 della Circolare, non decidibile sul livello testuale perché il riquadro è grafica con font a codifica propria.
- **Rilievo sistematico esteso a tutto il corpus**: `\tag{4.1.36}` rende `(4.1.36)` con parentesi tonde mentre la Gazzetta stampa `[4.1.36]`; sul render r03 riguarda 51 tag NTC e 19 della Circolare. Difformità presente solo nel documento reso, non nel sorgente Markdown.
- Riconciliazione strutturale conforme: 81/81 occorrenze di formule numerate (61 NTC + 20 Circolare) con la duplicazione di fonte del tag `[4.1.50]` conservata; 17/17 figure collegate e risolte.
- Stato invariato `VC-IN-CORSO`: G7 non avviato, nessun `VC-OK`, nessun registro promosso, prompt lasciato `IN-CORSO` come prescrive il protocollo quando il G6 non è superato.
- Evidenze: `_tmp_render/cap04/vc-paragrafo-4-1-20260730-r03/g6-rerun-01/`, con rapporto finale `04-rapporto-finale-g6.md`, manifest `05-manifest-sha256-g6.txt`, undici rapporti di blocco in `confronto/` e ritagli di prova in `adjudica/`.
- **Firma:** CC (Claude Code).

## 2026-07-30 - Seconda correzione distinta post-G6 del § 4.1

- Il G6 r02, eseguito in contesto fresco e realmente cieco, ha controllato 37/37 pagine, 81/81 formule numerate, 46/46 gruppi matematici non numerati, 11/11 tabelle e 17/17 figure. Esito `NON SUPERATO` per un solo `ERR-MD`; `ERR-AUDIT=0` e `DUBBIO=0`.
- Il controllo a 500 dpi ha accertato che la fonte ufficiale riporta `[4.1.44]`. La precedente adjudicazione `[4.1.44)` era errata; il Markdown è stato corretto esclusivamente da `\tag*{[4.1.44)}` a `\tag*{[4.1.44]}`.
- Fascicolo G6 r02 in `_tmp_render/cap04/vc-paragrafo-4-1-20260730-r02/g6/`; manifest validato 589/589, SHA-256 `3b9c26734cf9bc6c37d316f1124ad4da5e687a3cb3935ca9bc95c84229fe2de3`.
- Nuovo snapshot r03 SHA-256 `a05a99c00f13bc7e95b499f1136c927e0a0ffa19d9289e8b3ff77ee326f2acb4`; manifest di Markdown, indice e 17 asset SHA-256 `1026349fd1a7c45af39b57349ba482083db9e1eb91adfe23f749912898887048`.
- Controlli post-correzione: lint 0 errori e 0 avvisi; 139 heading, 81 formule numerate, 14 tabelle Markdown, 17 immagini e nessun collegamento mancante; render integrale di 45 pagine senza pagine vuote; tag `[4.1.44]` verificato visivamente; G5 riconfermato.
- Stato invariato `VC-IN-CORSO`: G7 non avviato, nessun `VC-OK`. Prossimo passo obbligatorio: nuovo G6 integrale, indipendente e cieco sullo snapshot r03.
- Evidenze correttive in `_tmp_render/cap04/vc-paragrafo-4-1-20260730-r03/`.
- **Firma:** CDX (Codex).

## 2026-07-30 - Correzione distinta post-G6 del § 4.1

- Corretti i due `ERR-MD` congelati dal G6 precedente: il tag anomalo della fonte è ora riprodotto letteralmente come `\tag*{[4.1.44)}` e nel primo capoverso C4.1 è stata ripristinata la virgola dopo `C28/35 e C32/40,`.
- Riallineate esclusivamente le quattro righe segnalate dal lint: titoli `heading_md` di `NTC-4.1.2.1.1` e `NTC-4.1.2.1.2`, heading e occorrenze di `CIRC-C4.1.12.1.3.2.1` e `.2`.
- Nuovo snapshot SHA-256 `fd67f65627f29b531aa3ced287d1c5490d7ee894f129f10d0b6b401bfca01705`; manifest dello snapshot, dell'indice di capitolo e dei 17 asset SHA-256 `4745c798a8b64f5bdd16ffb9be57878250309005b096beb436ff47048f769ea0`.
- Verifiche: tag `[4.1.44)` e virgola controllati sul render e sulle pagine fonte; 81 formule numerate; 139 heading senza duplicati; 17/17 asset; 14 tabelle; nessun link irrisolto; render integrale di 45 pagine senza pagine vuote.
- Registro di dettaglio preservato a 1.724 righe e 37 colonne, UTF-8 con BOM. Lint finale: 0 errori, 0 avvisi e 193 informazioni di solo spostamento righe.
- G5 riconfermato sul nuovo hash. La fase non costituisce G6: stato `VC-IN-CORSO`, nessun `VC-OK`, G7 non avviato. Prossimo passo: nuovo G6 integrale, indipendente e cieco.
- Evidenze in `_tmp_render/cap04/vc-paragrafo-4-1-20260730-r02/`.
- **Firma:** CDX (Codex).

## 2026-07-30 - G6 non superato sul § 4.1 NTC + § C4.1 Circolare

- Completati G0-G5 sul solo scope autonomo § 4.1 + § C4.1, costituito da 136 unità e 37 pagine ufficiali. Lo snapshot congelato e il file vivo coincidono allo SHA-256 `521a5e4f82bcb62be2fbb1d8f45751027b8670112020f18b363fe39cf20068a6`.
- Eseguito G6 con un nuovo subagente Codex: 37/37 pagine, 81/81 formule numerate, 32/32 gruppi matematici non numerati o inline, 11/11 tabelle con 271/271 celle logiche e 17/17 figure controllati.
- Esito G6: **NON SUPERATO**, con 2 `ERR-MD` e 1 `ERR-AUDIT` aperti. Il Markdown normalizza il tag anomalo di fonte `[4.1.44)` come `\tag{4.1.44}`; nel primo capoverso C4.1 omette la virgola dopo `C28/35 e C32/40,`; il requisito di cecità non è stato rispettato integralmente per un'esposizione accidentale a una nota della Fase 0.
- Il lint post-G6 ha rilevato 2 errori sui titoli registrati di `NTC-4.1.2.1.1` e `NTC-4.1.2.1.2` e 2 avvisi sui conteggi `occorrenze_md` di `CIRC-C4.1.12.1.3.2.1` e `.2`. Anche questi riallineamenti restano per la fase correttiva distinta.
- Nessuna correzione è stata applicata dopo G6. G7 non è stato avviato; dettaglio, master, indice VC, stato `4 / C4` e stato dell'intero corpus sono invariati. Il prompt resta `PROMPT-IN-CORSO-PARAGRAFO-4-1-VC-OK.md`.
- Evidenze in `_tmp_render/cap04/vc-paragrafo-4-1-20260730-r01/g6/`; manifest G6 validato 110/110, SHA-256 `346764f1048f33e33a06c354e7c53c716b61a3cd2f8521c3fe3059b4d3ceb70f`. Tutti i controlli sono stati svolti da agenti AI, senza revisione umana integrale.
- **Firma:** CDX (Codex).

## 2026-07-30 - Completamento delle pagine PDF nell'indice VC

- Compilate source-first le 220 pagine mancanti della Circolare nel registro di dettaglio: C3 35, C4 41, C6 3, C7 139 e C8 2. La copertura è ora 1.724/1.724 unità.
- Verifica svolta sui PDF ufficiali con OCR Windows e tavole visive. Evidenze e registri di mappatura sono conservati in `_tmp_render/cap03|cap04|cap06|cap07|cap08/mappatura-pagine-pdf-indice-vc-20260730-r01/`.
- Conservate senza modifiche tutte le 1.504 pagine preesistenti, gli stati del registro, gli stati VC e i file normativi.
- Rigenerato `indice-vc-ntc2018.csv` con 1.735 righe e quattro colonne, aggiungendo `pagina PDF`.
- Verifiche finali: 0 lacune, ordine monotono per sorgente, UTF-8 con BOM e numero di campi coerente; lint 0 errori, 0 avvisi e 74 informazioni. Gli hash sigillati del Capitolo 8 sono invariati.
- SHA-256 finali: `registro-dettaglio-verifica-ntc2018.csv` `902f6fb63ee6d2457233748f9e5043a3564cdfe97e8e3c5e6f762aad802c3d79`; `indice-vc-ntc2018.csv` `1d58b94f019a09a849fcff82c13b2e2855ed6981f82c852b291693a040f054b2`.
- Aggiunti `strumenti/mappa-pagine-pdf-indice-vc.py` e `strumenti/ocr-pagine-pdf-windows.ps1` per rendere ripetibile il controllo.
- **Firma:** CDX (Codex).

## 2026-07-30 - Prompt VC del Capitolo 4 ristretto al § 4.1

- Riesaminato integralmente il precedente `PROMPT-RIPRESA-CAPITOLO-4-VC-OK.md`, che copriva 458 unità e sei file.
- Per decisione di Sandro, sostituito con `PROMPT-RIPRESA-PARAGRAFO-4-1-VC-OK.md`, da eseguire dopo il completamento delle pagine PDF.
- Nuovo scope: 136 unità, 90 NTC e 46 Circolare, nel solo `cap04/4.1-calcestruzzo.md`, con 17 figure attualmente collegate.
- Il nuovo prompt recepisce la difformità accertata della formula [4.1.35], impone la risoluzione di 2 unità `DA_VERIFICARE` e mantiene fuori scope le due difformità note del § 4.3.
- Rimossi dal flusso operativo i riferimenti ormai superati al prompt in corso del Capitolo 8. Il master dell'intero Capitolo 4 non dovrà essere promosso.
- **Firma:** CDX (Codex).

## 2026-07-30 - Preparazione del completamento delle pagine PDF nell'indice VC

- Verificata la disponibilità del campo `pagina_pdf` nel registro di dettaglio: 1.504/1.724 unità compilate e 220 vuote.
- Le lacune riguardano esclusivamente la Circolare: C3 35, C4 41, C6 3, C7 139 e C8 2.
- Preparato `PROMPT-RIPRESA-INDICE-VC-PAGINE-PDF.md` per completare la mappatura source-first e aggiungere al CSV la quarta colonna `pagina PDF`, senza cambiare alcuno stato VC.
- Il prompt impone numerazione fisica 1-based, conferma sul PDF madre, lint finale, conservazione degli stati VC e verifica degli hash sigillati del Capitolo 8.
- `indice-vc-ntc2018.csv`, registro di dettaglio, registro master e file normativi non sono stati modificati in questa fase preparatoria.
- **Firma:** CDX (Codex).

## 2026-07-30 - Indice CSV degli stati VC

- Creato `indice-vc-ntc2018.csv`, vista di consultazione a tre colonne per capitoli e sottocapitoli NTC/Circolare.
- Inserite 1.735 righe senza chiavi duplicate o titoli vuoti: 114 `VC-OK al 2026-07-29` per il solo scope Capitolo 8 + C8 e 1.621 `VC-DA-FARE`.
- Collegato il nuovo CSV da `indice-ntc2018.md` e documentata in `README.md` la distinzione tra vista derivata, registro di dettaglio e master.
- Nessun file del Capitolo 8 compreso nel manifest formale è stato modificato.
- **Firma:** CDX (Codex).

## 2026-07-29 - Rilascio VC-OK autonomo del Capitolo 8

- Chiuso il protocollo VC-8 sul solo scope D.M. 17/01/2018 Capitolo 8 + Circolare 7/2019 Capitolo C8, senza promuovere l'intero corpus.
- Durante il nuovo G3 sono state individuate e corrette tre difformità residue: la locuzione di C8.4.2 sulle «eventuali plasticizzazioni», il punto elenco «per la resistenza a trazione» prima di [C8.7.2.11] e l'interpolazione «rispettivamente» assente a C8.8.5. Nuovo snapshot SHA-256 `14457ad1b2f3a4931eb82dedfe64bda28367526761eb57e0392eb104b7fdf225`.
- Ripetuti sul nuovo hash G3, G4 e G5. Esiti: 195/195 scarti testuali adjudicati; 49 formule numerate, 425 occorrenze inline, 8 tabelle con 661 celle comprese le intestazioni, 96 blocchi elenco; render integrale 72 pagine; zero `ERR-MD`, zero `ERR-AUDIT`, zero `DUBBIO`.
- Eseguito G6 indipendente in contesto fresco e cieco, con inventario fonte-prima congelato prima dell'apertura dello snapshot: 58/58 pagine, 8/8 tabelle, 49 formule numerate e 2 relazioni non numerate. Esito `SUPERATO`, SHA-256 `2f9403a74db0dba3847a443dd2f07b933da6943e3f70464f64b561ceaba006dd`.
- Creati `verifica-conformita/scope-CAP08-2026-07-29.md`, `manifest-sha256-CAP08-2026-07-29.txt` e `verbale-VC-CAP08-2026-07-29.md`. Manifest validato 4/4, SHA-256 `6071ee53c6b274ec7e64a918254944b3ce179d0cb747b181b4d00620215e58c8`.
- Promosse 113/113 unità del Capitolo 8 a `COMPLETA/OK`; master autonomo `ntc2018--norme-costruzioni--cap08` impostato a `VC-OK al 2026-07-29`; master del corpus conservato `VC-DA-FARE`.
- Lint finale: 0 errori, 0 avvisi e 74 informazioni su 1.724 righe. Tutti i verificatori erano agenti AI; nessuna revisione umana integrale.
- **Firma:** CDX (Codex).

## 2026-07-29 - Preparazione del rilascio VC-OK autonomo del Capitolo 8

- Creato `PROMPT-RIPRESA-CAPITOLO-8-VC-OK.md` per governare la chiusura formale del protocollo VC-8 sul solo scope Capitolo 8 NTC + C8 Circolare.
- Fissati come precondizioni il Markdown SHA-256 `97adcfa92cef5451cc12bc18ff210ec93601074fcd23f9a4a14877db470ab893` e gli hash già congelati dei due PDF ufficiali.
- Previsti scope master autonomo, chiusura conclusiva G0-G5, G6 integrale affidato a un verificatore diverso, manifest e verbale G7, promozione delle 113 unità soltanto dopo il superamento di tutti i gate.
- Esclusa espressamente la promozione dell'intero corpus NTC 2018 e qualunque attribuzione automatica di `VC-OK`.
- **Firma:** CDX (Codex).

## 2026-07-29 - Correzione mirata post-G6 r02 del Capitolo 8

- Corretto esclusivamente `ERR-MD-001` in `cap08/8-esistenti.md`: la frase `superiore al 10%.` è stata ricomposta nel primo punto elenco di C8.8.7.
- Snapshot SHA-256: `255a090a8a8c4786b6fc1c4d092d34788756dd54d7a059681cc900c71a945f81` → `97adcfa92cef5451cc12bc18ff210ec93601074fcd23f9a4a14877db470ab893`.
- Il diff è limitato alla ricomposizione autorizzata. Il nuovo HTML contiene quattro elementi nello stesso `<ul>`, senza un capoverso autonomo per la frase corretta.
- Rigenerato da zero il render integrale di 72 pagine. Controllo visivo della pagina 71: PASS; nessuna pagina vuota.
- Controlli di regressione: 59/59 PASS, con 20 heading NTC, 93 heading Circolare, 49 formule, 8 tabelle, 2 collegamenti e 0 pattern OCR vietati. Lint: 0 errori, 0 avvisi, 74 informazioni.
- Evidenze in `_tmp_render/cap08/vc-cap08-20260729-correzione-g6-r02-r01/`. `ERR-MD-001` è chiuso sul nuovo hash.
- La fase non costituisce un nuovo G6 integrale. Registri master e di dettaglio invariati; nessun `VC-OK`.
- **Firma:** CDX (Codex), ruolo correzione post-G6 r02.

## 2026-07-29 - Preparazione della correzione post-G6 r02 del Capitolo 8

- Creato il prompt correttivo post-G6 r02 con guardia generale contro il doppio avvio.
- Il prompt autorizza soltanto la ricomposizione del primo punto elenco di C8.8.7 che ha generato `ERR-MD-001`, seguita da nuovo render, controllo semantico HTML, verifica visiva e regressioni sull'intero capitolo.
- Fissato come precondizione lo snapshot `255a090a8a8c4786b6fc1c4d092d34788756dd54d7a059681cc900c71a945f81`; esclusa l'assegnazione automatica di `VC-OK` e la promozione dei registri.
- **Firma:** CDX (Codex).

## 2026-07-29 - G6 indipendente r02 del Capitolo 8

- Eseguito il controllo source-first integrale sullo snapshot `255a090a8a8c4786b6fc1c4d092d34788756dd54d7a059681cc900c71a945f81`, mantenendo `cap08/8-esistenti.md` in sola lettura.
- Due passaggi AI indipendenti hanno coperto 58/58 pagine e inventariato 20 unità NTC, 93 unità Circolare, 49 formule e 8 tabelle; il coordinamento ha risolto sul PDF sei errori di audit A/B.
- Verificati 49/49 apparati numerati, 581/581 posizioni logiche sorgente delle tabelle, 611 celle dati Markdown con normalizzazioni documentate, 2/2 collegamenti e 72/72 pagine render senza pagine vuote.
- Congelato l'esito provvisorio in `_tmp_render/cap08/vc-cap08-20260729-g6-r02/` con SHA-256 `e2572a6c45798e98d8df342d9309d6acee66b89ddad45199cd1e3a77691aa7b2`, prima di consultare l'audit correttivo precedente.
- Rilevato `ERR-MD-001`: la frase `superiore al 10%.` è separata nel Markdown dal primo punto elenco di C8.8.7; il render HTML chiude il primo `<li>` e il primo `<ul>` prima della frase.
- La riconciliazione successiva ha confermato tutte le nove famiglie di correzione precedenti e accertato che il nuovo rilievo non era coperto dai 53 controlli automatici dell'audit correttivo.
- Esito: **G6 NON SUPERATO**, nessun `VC-OK`; stati di dettaglio e master invariati. Il file normativo non è stato modificato.
- **Firma:** CDX (Codex), ruolo G6.

## 2026-07-29 - Correzioni post-G6 del Capitolo 8

- Applicate a `cap08/8-esistenti.md` le nove famiglie di correzione rilevate dal G6 del 2026-07-28, con confronto diretto sui PDF ufficiali e senza estendere l'intervento ad altri rilievi.
- Snapshot SHA-256: `a9b649bb8aa5a8cb45369f18e627a1663bf52379c0b1f98b072ac71af5f10f7a` → `255a090a8a8c4786b6fc1c4d092d34788756dd54d7a059681cc900c71a945f81`.
- Corrette notazioni matematiche, segno della formula C8.7.2.1, tre pedici `l_o`, indici del giunto, simbolo `theta`, residui OCR e tilde, enumerazioni a)-d), confini LC1-LC3, casi dei ponti e sottotitoli degli interventi.
- Preservate le anomalie della fonte già censite. Diff e catena di evidenza conservati in `_tmp_render/cap08/vc-cap08-20260729-correzioni-r01/`.
- Verifiche: 53/53 controlli automatici PASS; render matematico di 68 pagine senza pagine vuote; controllo visivo mirato PASS; lint del registro con 0 errori, 0 avvisi e 74 informazioni.
- La fase non costituisce un nuovo G6 e non assegna `VC-OK`. Stati invariati: 111 unità `IN_CORSO/NON_VALUTATO`, 2 unità `COMPLETA/OK`.
- Preparato `PROMPT-RIPRESA-CAPITOLO-8-G6-R02.md` per un controllo indipendente sul nuovo snapshot; neutralizzato a chiusura il prompt correttivo come `old/PROMPT-CONSUMATO-CAPITOLO-8-POST-G6.md`.
- **Firma:** CDX (Codex), ruolo correzione post-G6.

## 2026-07-29 - Neutralizzazione dei prompt di ripresa

- La guardia nata in questo progetto è stata promossa a regola generale del workspace, con strumento unico in `gestione-workspace/gestione-wks-260729-gestisci-prompt-ripresa.py`; rimossa la copia locale per evitare divergenze.
- I prompt passano da `PROMPT-RIPRESA-*` a `PROMPT-IN-CORSO-*` appena vengono presi in carico e a `PROMPT-CONSUMATO-*` alla chiusura positiva; non vengono cancellati e il doppio avvio viene bloccato.
- Inserita la guardia nel prompt attivo `PROMPT-RIPRESA-CAPITOLO-8-POST-G6.md`, senza avviare le correzioni del Capitolo 8.
- Il progetto rinvia ora alla regola unica in `../../AGENTS.md` § "Prompt di ripresa".
- **Firma:** CDX (Codex).

## 2026-07-28 - Controllo indipendente G6 del Capitolo 8

- Salvato nella radice del progetto `PROMPT-RIPRESA-CAPITOLO-8-POST-G6.md`, pronto per la sessione di correzione successiva. **Firma:** CDX.
- Creato l'audit `_tmp_render/cap08/vc-cap08-20260728-g6-r01/` sullo snapshot `a9b649bb8aa5a8cb45369f18e627a1663bf52379c0b1f98b072ac71af5f10f7a`; il file normativo vivo non è stato modificato.
- Controllate visivamente 58/58 pagine ufficiali, riconciliate 20 unità NTC e 93 unità Circolare, confrontate 49 formule numerate, 8 tabelle e 2 collegamenti.
- Esito: **G6 NON SUPERATO**. Restano 9 famiglie `ERR-MD`, 3 `ERR-AUDIT` e 0 `DUBBIO`; le tabelle risultano conformi 8/8.
- Confermata la regressione sostanziale di `[C8.7.2.1]`: la fonte reca l'esponente `-0.225`, mentre il Markdown reca `0,225`. Il registro F02-F05 e il relativo recheck del 2026-07-17 avevano letto il segno al contrario.
- Documentate le anomalie della fonte, comprese `0.35`, `C8..5.4.3`, l'alternanza `k`/`κ`, `M_{e.Rd}`, `AGGIUNTIVERELATIVE`, `C8.8.5.` autonomo e il richiamo `(4)` orfano.
- Congelato `esito-provvisorio.md` con SHA-256 `29b9a44231ab78d95305a0948d061454b9212bedf32d928e81dd3e856b5a95ed`; riconciliazione successiva e registro finale sono file distinti.
- Stato invariato: 111 unità del Capitolo 8 `IN_CORSO/NON_VALUTATO`, 2 precedenti lotti specialistici `COMPLETA/OK`; nessun `VC-OK`.
- **Firma:** CDX (Codex), ruolo G6.

## 2026-07-28 - Audit integrale source-first del Capitolo 8

- Ripreso nella revisione `_tmp_render/cap08/vc-cap08-20260728-r02/` l'audit interrotto dal crash; la r01 è stata conservata come evidenza storica.
- Sostituita nel file vivo la sezione NTC, risultata una vecchia sintesi incompleta, con la trascrizione integrale delle pagine ufficiali 293-299. Verifica finale: 5.319 token fonte e 5.319 token Markdown, 0 scarti; identità testuale con la trascrizione ricostruita, al netto delle terminazioni di riga.
- Recuperata dal render ufficiale la pagina file 281 della Circolare, pagina stampata 277, priva di text layer: reintegrati testo sulle resistenze residue, [C8.7.1.17]-[C8.7.1.18], C8.7.1.3.1.2, inizio di C8.7.1.3.2 e nota 4.
- Risolti i rilievi prosa/struttura aperti il 2026-07-17, ripristinati i simboli matematici corrotti e aggiornati gli indici. Controlli sul file vivo: 113 heading univoci, 49 formule taggate univoche, 8 tabelle strutturalmente coerenti, 91 link interni validi, nessun carattere di controllo o glifo sospetto.
- Riallineato `registro-dettaglio-verifica-ntc2018.csv`: tutte le 113 unità del Capitolo 8 sono strutturalmente `COMPLETA`; 111 verifiche restano `IN_CORSO/INTEGRALE` in attesa del controllo indipendente G6 e 2 conservano i precedenti esiti specialistici `COMPLETA/OK`. Lint: 0 errori, 0 avvisi su 1.724 righe.
- Nessun `VC-OK` assegnato; il master resta `VC-DA-FARE`.
- **Firma:** CDX (Codex).

## 2026-07-17 (sera) - Lotto C8-T05 (Tab. C8.7.6.3.II) + formule F02-F05 (44) + avvio prosa/struttura

Sessione CC su richiesta di Sandro ("chiudi tutto quello che puoi su C8"). Metodo VC8-G4-TF con **A = Opus 4.8 (sessione), B = Sonnet** (niente Fable), arbitrato e scrittura correzioni CC, recheck fresco Opus.

- **Lotto C8-T05 — Tabella C8.7.6.3.II** (multipagina pp. 298-300, render `…-r04/`): A/B concordi al 100% su 38 posizioni logiche (didascalia + 7 intestazioni + 30 celle). Unica ERR-MD: punto finale spurio della didascalia (E1), stessa fattispecie di T03/T04, rimosso. Confronto meccanico `confronta_triplo.py`: 37/38 pre → **38/38 post**. Recheck fresco **5/5 CONFORME**. 5 anomalie di fonte censite (istallazione, "la elevata"/"una unità", punteggiatura asimmetrica R2/C3-C4, celle vuote). Snapshot `d4d4ee41…` → `da2bf432…`. Evidenze in `verifica-conformita/audit-C8-T05-20260717/`.
- **Lotti formule F02-F05 — 44 formule** (C8.7.1.1-16, C8.7.2.1-13 con 7a/7b, C8.7.4.1-8 con 7a/7b, C8.8.5.1-5): pagine fonte rese a 3x in `_tmp_render/cap08/conformita-formule-20260717-r01/`; doppio passaggio A/B alla cieca su modelli diversi, confronto con i blocchi MD estratti da `estrai_formule_md.py`, arbitrato sul PDF. **1 solo errore di VALORE su 44**: in **C8.7.2.1** l'esponente della parentesi quadra era `-0,225` (negativo) contro la fonte `0,225` (positivo, verificato su pagina-285) → segno corretto. Recheck fresco di valore su C8.7.2.1 + 4 formule complesse: **5/5 CONFORME**. Snapshot `da2bf432…` → `17de5443…`. Verbale in `verifica-conformita/registro-formule-C8-F02-F05-20260717.md` + `recheck-formule-C8-20260717.md`.
- **Policy tipografica formule (scelta di Sandro): "uniforme e leggibile"**. La fonte C8 mescola punto e virgola decimale in modo incoerente (a volte nella stessa formula) e ha refusi di maiuscola (Φ/φ, K/k, S_h/s_h, "hs", "ρ_sfy", "e.Rd"): il markdown uniforma a virgola italiana e a simboli coerenti, tutto documentato come normalizzazione (NORM). Nessuna di queste differenze altera un valore.
- **Lotto prosa/struttura — AVVIATO, PARZIALE**. Corretti 2 rilievi strutturali di C8.8 verificati sulla fonte (pagina-302): il § **C8.8.3 troncato** ("…verifica del tipo indicato al §" → "…al § **C8.8.5.**") e l'**heading C8.8.5 duplicato/spurio** inserito prima di C8.8.4 (rimosso; ordine ripristinato C8.8.3 → C8.8.4 → C8.8.5). Snapshot `17de5443…` → `92ffc7fc4a72bc0b42f274fcdf51d24fdccd677c25d2b45bd270b21a9be7e0b5` (1591 righe). Fermato qui su richiesta di Sandro.
- **Rilievi prosa/struttura ANCORA APERTI** (per la prossima sessione): RC1 = capoverso troncato a md 527 ("…ci si può riferire alla Tabella" senza "C8.5.IV"); RC2 = heading H2 spurio "## C8.5. Definizione del modello…" a md 529; heading `#### C8.5.3.2` **duplicato/spurio a md 543** (nato dallo spezzamento del riferimento "(v. § C8.5.2.2 e C8.5.3.2)" a md 541); "muro" LC1-LC3 in unico capoverso a md 541; ricollocazione Tabelle C8.5.V-VI sotto il § corretto; reflow a-capo fisici nella prosa (es. md 407-422, 459-460).
- **Firma:** CC (Claude Code).

## 2026-07-17 - Lotto conformità C8-T04: Tabella C8.7.6.3.I (rilancio e chiusura)

- Rilanciato da zero il lotto C8-T04 (interrotto in giornata senza output) riusando i render fonte di `_tmp_render/cap08/conformita-tabelle-formule-20260717-r03/`: PDF invariato (SHA riverificato), snapshot markdown aggiornato al post-T03 `0f364296…` in `ambiente.txt`.
- Audit VC8-G4-TF con i modelli scelti secondo la scala di CLAUDE.md (niente Fable): **A = subagente Opus 4.8 (modello di sessione), B = subagente Sonnet**, alla cieca su sole immagini fonte; riconciliazione e arbitrato CC con verifica visiva diretta dei punti di correzione; confronto meccanico `diff/confronta-triplo.py` su 390 celle logiche (30 righe × 13 campi, matrice multipagina riunita).
- Esito: A e B concordi al 100% sul contenuto (unica differenza di resa, adjudicata: richiamo "(4)" trascritto `(4)` da A e `⁽⁴⁾` da B); 388/390 celle MD conformi pre-correzione; note 5-8 concordi parola per parola.
- Corrette e promosse 4 difformità ERR-MD su `cap08/8-esistenti.md` (righe 1414-1447): punto finale spurio della didascalia rimosso (stessa fattispecie del T03); ripristinata la e commerciale "Costo & interruzione" (il MD aveva "Costo e"); "Sostanze Pericolose" con la doppia maiuscola della fonte (2 occorrenze); "Valutazione / adeguamento" con barra spaziata come in fonte (4 intestazioni). Recheck fresco a contesto pulito: **4/4 CONFORME**. Snapshot: `0f364296…` → `d4d4ee4145232206613336529169a14c15590a7aced6e5a1c1674d5b0f6a099a`.
- **AF notevole**: il richiamo di nota "(4)" della riga-categoria "Componenti fissati al pavimento o sul tetto" è orfano nella fonte stessa: la nota 4 non fu mai stampata nel capitolo C8 (scansione automatica dei piè di pagina a corpo minore, pp. 249-299: esistono le note 1, 2, 3, 5, 6, 7, 8). Censito come anomalia della fonte, richiamo mantenuto fedelmente senza inventare la nota.
- Registro di dettaglio: CIRC-C8.7.6.3 → verifica `IN_CORSO`, perimetro `TABELLE`, gate `G2|G4`, nota estesa; lint 0 errori, 0 avvisi su 1.724 righe. Evidenze finali in `verifica-conformita/audit-C8-T04-20260717/` (registro, manifest, ambiente, trascrizioni A e B, confronto triplo CSV, recheck, estrazione MD).
- Prossimo: lotto C8-T05 (Tab. C8.7.6.3.II multipagina 298-300, render pronti in `…-r04/`), poi lotti formule F02-F05 (44 formule) e lotto prosa/struttura.
- **Firma:** CC (Claude Code).

## 2026-07-17 - Lotto conformità C8-T03: Tabelle C8.5.V e C8.5.VI (sera); C8-T04 interrotto

- Audit VC8-G4-TF sul lotto C8-T03 (cartella `_tmp_render/cap08/conformita-tabelle-formule-20260717-r02/`): doppio passaggio A/B su modelli diversi (Fable/Opus) con **concordanza integrale al 100%** — nessuna divergenza da adjudicare; 13 celle logiche per tabella (intestazioni a 2 livelli con celle fuse) + blocco note esplicative verbatim.
- Corrette e promosse 4 famiglie ERR-MD su `cap08/8-esistenti.md`: maiuscole "Livello di **I**ndagini e **P**rove" (2 tabelle); punto finale aggiunto alla didascalia della VI rimosso (la fonte termina senza punto); enfasi ***limitato/esteso/esaustivo*** ripristinate (6 etichette); blocco "NOTE ESPLICATIVE ALLE TABELLE C8.5.V E C8.5.VI" rispezzato nei 6 capoversi della fonte (titolo, introduzione, note (a)-(d)) — il testo era già fedele parola per parola.
- Recheck: confronto testuale con la trascrizione A + verificatore fresco Opus **4/4 CONFERMATO**. Criterio §12 SUPERATO per il perimetro. Snapshot: `a3ee349b…` → `0f364296…` (+10 righe; diff limitato alle righe attese; lint 0 errori 0 avvisi, 71 info di drift riga fisiologico).
- Registro di dettaglio: nota estesa su CIRC-C8.5.4.2 (Tab. V-VI conformi; unità ancora sospesa per i rilievi strutturali RC1-RC2 e per la ricollocazione delle tabelle, oggi sotto l'heading duplicato md 543). Evidenze in `verifica-conformita/audit-C8-T03-20260717/`.
- **Lotto C8-T04 (Tab. C8.7.6.3.I, multipagina 297-298) INTERROTTO su richiesta di Sandro** a passaggi A/B in corso, nessun output scritto: rilanciare da zero (render e crop pronti in `_tmp_render/cap08/conformita-tabelle-formule-20260717-r03/`). Pronto anche il lotto C8-T05 (Tab. C8.7.6.3.II, multipagina 298-300, render in `…-r04/`). Inventario formule residue: 44 in 4 gruppi (C8.7.1.1-16, C8.7.2.1-13 con 7a/7b, C8.7.4.1-8 con 7a/7b, C8.8.5.1-5).
- **Firma:** CC (Claude Code).

## 2026-07-17 - Lotto conformità C8-T02: Tabelle C.8.5.III e C8.5.IV

- Audit VC8-G4-TF completo sul lotto C8-T02 (cartella `_tmp_render/cap08/conformita-tabelle-formule-20260717-r01/`): scope congelato con hash, doppio passaggio indipendente su modelli diversi (A = subagente Fable 5, B = subagente Opus, soli render 288-432 dpi), riconciliazione sul render con un'unica divergenza sostanziale adjudicata ("Nota: f_k," contro "Noto f_k,": vince la lettura "Nota:", anomalia della fonte conservata).
- Corrette e promosse 4 famiglie di difformità su `cap08/8-esistenti.md` (righe 521, 531, 535-537): ripristinato il refuso di fonte "τ" nella nota (*) della Tab. C.8.5.III (il MD lo aveva "corretto" interpretativamente in κ, contro il principio di fedeltà); rimossa una virgola aggiunta; tolto il punto finale aggiunto alla didascalia della Tab. C8.5.IV; ripristinate 10 locuzioni in grassetto corsivo e 3 etichette LC in grassetto nella Tab. C8.5.IV.
- Recheck delle correzioni: confronto testuale con la trascrizione A (5/5) + verificatore fresco a contesto pulito su soli render (5/5 CONFERMATO). Criterio di accettazione §12 SUPERATO per il perimetro dichiarato.
- Snapshot: `612a2c00…` → `a3ee349b…`; diff integrale limitato alle 5 righe attese, porzioni del pilota invariate.
- Registro di dettaglio: nota estesa su CIRC-C8.5.4.1 (Tabella C.8.5.III conforme); CIRC-C8.5.4.2 a verifica IN_CORSO perimetro TABELLE con trasposizione retrocessa a PARZIALE per i rilievi prosa RC1 (capoverso troncato md 527) e RC2 (heading H2 spurio md 529). Lint: 0 errori, 0 avvisi.
- Evidenze finali in `verifica-conformita/audit-C8-T02-20260717/`; riga master aggiornata (prossimo passo: C8-F02, poi lotto prosa).
- **Firma:** CC (Claude Code).

## 2026-07-17 - Ripristino post-incidente sync e chiusura del pilota conformità C8

- Cartella ripristinata dopo l'incidente di sync del 16-17/7 (cancellazione partita dal P53 e propagata via Obsidian Sync): merge fra superstiti e copia pre-cancellazione, con verifica bit per bit dei 4 hash SHA-256 del manifest fonti (PDF norma e Circolare, cap08 pre-audit, registro dettaglio).
- Promosse sul file vivo `cap08/8-esistenti.md` le 14 correzioni ERR-MD del pilota C8 (audit A/B VC8-G4-TF del 16/7 sui materiali congelati); SHA-256 post-promozione `612a2c00…` conforme alla copia corretta ricontrollata 14/14 da verificatore fresco.
- Registrati gli esiti nel registro di dettaglio: CIRC-C8.5.3.1 (perimetro TABELLE) e CIRC-C8.5.4.1 (perimetro FORMULE) → verifica `COMPLETA`, esito `OK` sullo snapshot manifest-fonti-2026-07-16, con audit_id, evidenza, date e doppio revisore compilati. Lint `strumenti/lint-registro-dettaglio.py`: 0 errori, 0 avvisi su 1.724 righe.
- Evidenze finali dell'audit copiate da `_tmp_render/` in `verifica-conformita/audit-C8-T01-F01-20260716/` (registro, manifest esiti, riconciliazione A/B, scarti, dettagli celle e formule); nuovo verbale `verifica-conformita/promozione-pilota-c8-2026-07-17.md`.
- Riga master NTC aggiornata: gate `g4_apparati` → `PARZIALE`, prossimo passo = lotti C8-T02 (Tabelle C.8.5.III-IV) e C8-F02 (~10 formule esposte C8).
- **Firma:** CC (Claude Code).

## 2026-07-15 - Pulizia radice e lint del registro di dettaglio

- Corretto `AGENTS.md`: il riferimento per conversioni e riconversioni ora punta a `../../skills/conversione-normativa/SKILL.md`, sezione "Caso NTC 2018"; la skill `conversione-ntc2018` citata prima non esiste più.
- `AGENTS.md`: esplicitato che `_tmp_render/` contiene gli audit storici e non va mai svuotata in blocco; gli audit chiusi migreranno in `verifica-conformita/` col primo verbale formale.
- Radice ripulita: eliminati il prompt di ripresa `2026-05-29-RIPRESA-tabelle-altri-capitoli-DA-CANCELLARE-DOPO-AVVIO.md` (chiedeva esso stesso la cancellazione dopo l'avvio, avvenuto il 2026-05-29/30; metodo comunque superato dal protocollo 2026-07-14) e l'estratto temporaneo `_c42_p102_108.txt` (testo grezzo rigenerabile dal PDF); eliminata `strumenti/__pycache__/`.
- Spostati in `strumenti/` gli script storici `estrai-figure-c4.1.py`, `estrai-figure-c4.2.py`, `estrai-figure-c4.2-bis.py` (figure già estratte, conservati come documentazione del metodo).
- `README.md`: corretta l'indicazione dei PDF sorgenti (stanno in `raw/`) e allineato l'albero della struttura alla realtà (`raw/`, `strumenti/`, `_tmp_render/`, `annotazioni/`, `AGENTS.md`).
- Nuovo `strumenti/lint-registro-dettaglio.py`: controllo di sola lettura della coerenza del registro di dettaglio — vocabolari e combinazioni di stato, id, date, esistenza dei file, heading censiti ancora presenti, conteggio occorrenze, drift delle righe, collegamento alla riga master. Prima esecuzione sul registro corrente: 0 errori, 0 avvisi; controlli verificati anche al negativo con dati errati iniettati in memoria.
- Nella radice `normativa/`: eliminata la cartella vuota `diano_marina_varie` (residuo del vecchio naming; resta `diano-marina-varie`).
- **Firma:** CC (Claude Code).

## 2026-07-14 - Allineamento al registro generale VC-8

- `VC` esplicitato come Verifica di Conformità; confermato `normativa/_registro-verifica-conformita.csv` come unica fonte di verità degli stati generali `VC-*`.
- Rinominato il registro locale in `registro-dettaglio-verifica-ntc2018.csv`: resta una sintesi corrente per le 1.724 unità e non un secondo registro master.
- Aggiunti `registro_master_id`, `tipo_record`, `gate_master`, `ultimo_aggiornamento` e `aggiornato_da`; rinominati i campi locali in `stato_trasposizione_unita`, `stato_verifica_unita`, `esito_unita` e `perimetro_verifica_unita`.
- Stati iniziali riallineati a `DA_FARE` e `NON_VALUTATO`; nessuna riga ha ricevuto automaticamente `OK`.
- Il sottoprotocollo per tabelle e formule è identificato come `VC8-G4-TF`. Gli audit futuri avranno identificativi distinti per lotto e snapshot.
- Rinominato il generatore in `strumenti/genera-registro-dettaglio-verifica.py` e mantenute le protezioni contro la sovrascrittura accidentale.
- Aggiornata la riga master NTC: `VC-DA-FARE`, G0 `PARZIALE`, G1-G7 `DA_FARE`, collegamento al registro locale e prossimo passo C8-T01/C8-F01.
- Collegati dall'indice NTC il registro di dettaglio e il registro master della normativa.
- Nessun testo normativo, tabella o formula è stato modificato e nessun audit formale è stato avviato.
- **Firma:** CDX (Codex).

## 2026-07-14 - Registro CSV di conversione e conformità

- Creato `registro-conformita-ntc2018.csv`, con 32 campi e 1.724 righe source-first: 1.045 unità NTC, comprese Premessa e Capitolo 12, e 679 paragrafi della Circolare.
- Per le NTC l'inventario usa l'unione tra sommario ufficiale e titoli del corpo PDF, così conserva anche i 35 paragrafi presenti nel testo ma omessi dal sommario e l'anomalia di numerazione `7.9.5.3.2`.
- Mappati automaticamente i paragrafi ai file Markdown: 1.554 righe classificate `COMPLETA` come sola presenza strutturale e 170 casi `DA_VERIFICARE` per heading assente, duplicato o numerazione Markdown estranea all'inventario fonte.
- Segnalati nella riga `NTC-7.3.6` gli heading Markdown `7.3.6.4` e `7.3.6.5`, non censiti come paragrafi autonomi nella fonte.
- Tutti i controlli correnti sono inizializzati a `NON_AVVIATO` e tutti gli esiti a `NON_VALUTATA`; nessuna conformità è stata assegnata automaticamente.
- Predisposte le righe pilota `CIRC-C8.5.3.1` per le tabelle C8.5.I-C8.5.II e `CIRC-C8.5.4.1` per le formule C8.5.4.1-C8.5.4.3. I controlli storici sono registrati separatamente come parziali e riferiti a snapshot superati.
- Aggiunto `strumenti/genera-registro-conformita.py`, generatore ripetibile con simulazione predefinita, validazioni interne, CSV UTF-8 BOM separato da punto e virgola e protezione contro la sovrascrittura accidentale.
- Nessun testo normativo, tabella o formula è stato modificato e nessun audit di conformità è stato ancora avviato in questa fase.
- **Firma:** CDX (Codex).

## 2026-07-14 - Protocollo di conformità per tabelle e formule

- Aggiornata la skill `controllo-serrato-ntc2018` introducendo la distinzione tra conversione, controllo e conformità documentale.
- Allineate la skill condivisa in `workspace/skills/` e la copia caricata da Codex in `workspace/.agents/skills/`.
- Aggiunto il riferimento operativo `skills/controllo-serrato-ntc2018/references/protocollo-conformita-tabelle-formule.md`: inventario fonte-first, snapshot con hash, doppio passaggio indipendente A/B, matrici logiche delle tabelle, confronto strutturale e visivo delle formule, stati del registro e criterio di accettazione al 100 per cento.
- Registrato in `README.md` e `TODO.md` che nessun capitolo è ancora dichiarato conforme secondo il nuovo standard.
- Definito il pilota sulla Circolare C8. Primo lotto tabelle: C8.5.I-C8.5.II. Primo lotto formule: C8.5.4.1-C8.5.4.3 con definizioni dei simboli collegate.
- Nessun testo normativo, tabella o formula è stato modificato in questa fase metodologica.
- **Firma:** CDX (Codex).

## 2026-06-18 - Note locali Circolare C8

- `cap08/8-esistenti.md`: sostituita la sintassi footnote Markdown `[^1]`, `[^2]`, `[^3]` con note locali leggibili nel punto del testo: richiamo `[1]`, `[2]`, `[3]` e blocco immediatamente successivo `**Nota 1.**`, `**Nota 2.**`, `**Nota 3.**`.
- Motivazione: nei viewer Markdown le footnote standard vengono spesso raccolte in fondo al file, rendendo scomoda la lettura della Circolare C8.
- Controlli finali: 0 sintassi footnote residua, 0 richiami nota incollati residui, 47 tag formula C8 invariati, 0 tabelle Markdown con numero colonne incoerente.

## 2026-06-16 - Reflow Circolare C8

- `cap08/8-esistenti.md`: pulita la sezione `# Circolare` unendo le righe fisicamente spezzate dentro i paragrafi, così i viewer Markdown non mostrano a-capo anomali come `locali e al / loro conseguente...`.
- `cap08/8-esistenti.md`: normalizzati i richiami di nota della Circolare C8; recuperato dal PDF il testo della nota 3, assente nel Markdown precedente.
- Per il solo reflow dei paragrafi, il testo normalizzato della Circolare prima/dopo è invariato; la normalizzazione successiva delle note ha recuperato testo fonte mancante per la nota 3.
- Rimossi 54 vuoti interni a frasi; linee della sezione Circolare ridotte da 3134 a 1335; coppie di righe prose spezzate fuori dalle formule ridotte da 1729 a 0.
- Controlli finali: 47 tag formula C8 invariati, 86 righe tabellari invariati, 98 titoli Circolare invariati, 0 tabelle Markdown con numero colonne incoerente.
- Audit e copia pre-intervento in `_tmp_render/cap08/reflow-c8-circolare-20260616/`; ritaglio fonte per nota 3 in `_tmp_render/cap08/note-c8/`.

## 2026-06-11 - Conversione Markdown formule C8

- `cap08/8-esistenti.md`: convertite in LaTeX Markdown le 47 formule esposte della Circolare C8, sostituendo i richiami immagine fonte PDF.
- Mantenuti i tag originali delle formule: da `C8.5.4.1` a `C8.8.5.5`, inclusi `C8.7.2.7a`, `C8.7.2.7b`, `C8.7.4.7a` e `C8.7.4.7b`.
- Corretto anche il blocco formula non numerato sotto `C8.8.5.1`: `q = mS_e(T)/F_y` e `m = \sum m_i\Phi_i`.
- Controlli finali: 47 tag formula C8 in LaTeX, 0 richiami immagine formula residui, 8 tabelle Markdown con numero colonne coerente, 0 caratteri di controllo residui.
- `_tmp_render/cap08/controllo-formule-c8-md-wide/`: conservati ritagli larghi e tavole di controllo usati per la lettura delle formule.
- Aggiornati `README.md`, `TODO.md`, `cap08/indice-cap08.md` e `cap08/cap08-costruzioni-esistenti-revisione.md`.

## 2026-06-11 - Conversione Markdown tabelle C8

- `cap08/8-esistenti.md`: convertite in Markdown le 8 tabelle ufficiali della Circolare C8, sostituendo i 10 richiami immagine precedenti.
- Normalizzati gli accorpamenti del PDF: valori ripetuti nelle celle logiche coperte, categorie rese come colonna esplicita nella Tab. C8.7.6.3.I, colonne zone 1-4 rese esplicite.
- Trascritte anche le note interne alle tabelle C8.5.I, C8.5.II, C8.5.III, C8.5.IV e C8.7.6.3.I.
- Controlli finali della sola conversione tabellare: 8 tabelle Markdown con numero colonne coerente, 0 richiami immagine tabellari residui, 47 richiami formula immagine ancora presenti in quel momento, poi rimossi con la conversione formule del 2026-06-11, 0 caratteri di controllo residui.
- `_tmp_render/cap08/controllo-md-tabelle-c8/`: aggiunto rapporto di verifica finale della conversione tabellare.
- Aggiornati `TODO.md`, `cap08/indice-cap08.md` e `cap08/cap08-costruzioni-esistenti-revisione.md`.

## 2026-06-10 - Controllo accorpamenti tabelle C8

- `_tmp_render/cap08/controllo-accorpamenti-tabelle-c8/`: aggiunto rapporto mirato sugli accorpamenti nelle tabelle PDF della Circolare C8.
- `cap08/cap08-costruzioni-esistenti-revisione.md`: registrata la regola operativa per eventuali trascrizioni future: i valori delle celle PDF accorpate vanno ripetuti in tutte le celle logiche coperte; le celle vuote si usano solo quando il valore e' realmente assente nel PDF.
- `cap08/8-esistenti.md`: stato del 2026-06-10, poi superato il 2026-06-11: nessuna modifica applicata in quella sessione, quando le tabelle C8 erano ancora rese come ritagli fonte PDF e non come tabelle Markdown.

## 2026-06-09 - Riconversione Circolare C8

- `cap08/8-esistenti.md`: sostituita integralmente la sezione `# Circolare` del Capitolo 8 con una riconversione dal PDF mantenuto `raw/Circolare-7-2019-NTC.pdf`.
- `cap08/img/`: aggiunti ritagli fonte PDF per gli apparati critici della Circolare C8: 8 tabelle ufficiali collegate in 10 immagini e 47 formule esposte collegate come immagini, stato poi superato dalla conversione Markdown del 2026-06-11.
- `_tmp_render/cap08/riconversione-c8.py`: creato generatore ripetibile della riconversione; bozza e copia pre-riconversione salvate in `_tmp_render/cap08/riconversione-c8/`.
- `cap08/indice-cap08.md`: sostituito l'avviso di non affidabilità con nota di riconversione.
- `cap08/cap08-costruzioni-esistenti-revisione.md` e `TODO.md`: aggiornati esito, conteggi e stato del capitolo.
- Controlli finali: 0 immagini mancanti nei richiami di `cap08/8-esistenti.md`, 0 tabelle Markdown con colonne incoerenti, 0 caratteri di controllo residui.

## 2026-06-09 - Controllo serrato Capitolo 8

- `_tmp_render/cap08/audit-cap08-fonte-vs-md/`: prodotto audit fonte vs Markdown per il capitolo 8, norma e Circolare C8.
- `cap08/cap08-costruzioni-esistenti-revisione.md`: creato registro di revisione del capitolo con esito, tavole di audit, tabelle e formule critiche.
- `cap08/8-esistenti.md`: aggiunto avviso in testa alla sezione Circolare C8; la sezione non è fonte-affidabile fino a riconversione.
- `cap08/8-esistenti.md`: aggiornata la nota sulla Tab. C8.5.I rimuovendo il riferimento operativo al vecchio PDF compresso non più presente in `raw/`.
- Esito tabelle: 8 tabelle censite; C8.5.I e C8.5.II sostanzialmente allineate; C8.5.III, C8.5.IV, C8.5.V, C8.5.VI, C8.7.6.3.I e C8.7.6.3.II da riconvertire.
- Esito formule: mismatch sostanziali su C8.5.4.1-C8.5.4.3, C8.7.2.1-C8.7.2.13, C8.7.4.6-C8.7.4.8 e C8.8.5.1-C8.8.5.5; mancanti C8.7.4.7a e C8.7.4.7b.
- `TODO.md` e `cap08/indice-cap08.md`: aggiornato lo stato del cap. 8 indicando, nella fase di controllo, la necessità di riconversione della Circolare C8.

## 2026-06-09 - Verifica fonte vs Markdown tabelle Capitolo 3

- `_tmp_render/cap03/audit-tabelle-fonte-vs-md/`: prodotto un controllo affiancato PDF sorgente / tabella Markdown per tutte le 44 tabelle richiamate nei file normativi `cap03/*.md`.
- Rigenerate 22 tavole di audit `cap03-tabelle-fonte-vs-md-01.png` ... `cap03-tabelle-fonte-vs-md-22.png`, con registro CSV e Markdown.
- `cap03/3.3-vento.md`: normalizzata la Tabella C3.3.V a quattro colonne costanti, esplicitando le celle vuote dei valori positivi quando non applicabili.
- `cap03/3.3-vento.md`: corretta la struttura Markdown della Tabella C3.3.XVI, sostituendo il valore assoluto `|α|` con notazione LaTeX robusta per non spezzare la riga tabellare.
- `_tmp_render/cap03/audit-tabelle-fonte-vs-md/genera_audit_tabelle.py`: corrette le pagine sorgenti di confronto per tabelle spezzate o agganciate alla pagina vicina: Tab. 3.1.I, Tab. 3.1.II, Tab. 3.2.I-II, Tab. 3.2.V, C3.2.II, C3.3.III-IV e C3.3.XIX.
- Controllo automatico finale sulle 44 tabelle Markdown: 0 righe con numero di colonne incoerente.

## 2026-06-08 - Verifica fonte vs Markdown immagini Capitolo 3

- `_tmp_render/cap03/audit-fonte-vs-md/`: prodotto un controllo affiancato PDF sorgente / PNG Markdown per tutte le 49 immagini richiamate nei file `cap03/*.md`.
- `cap03/cap03-azioni-sulle-costruzioni-revisione.md`: registrato l'esito del controllo ulteriore: 31 agganci diretti a didascalia PDF, 9 verifiche con pagina manuale certa, 9 verifiche con pagina intera da richiamo testuale.
- Confermato che non risultano ulteriori immagini del capitolo 3 da sostituire dopo le correzioni su vento, neve e temperatura.
- Eseguiti controlli automatici finali sui riferimenti immagine: 49 richiami, 0 file mancanti, 0 PNG con dimensioni anomale.

## 2026-06-08 - Correzione immagini neve e temperatura Capitolo 3

- `cap03/3.3-vento.md`: aggiornato il richiamo della Fig. 3.3.3 verso un nuovo ritaglio pulito del solo grafico del coefficiente di esposizione, senza intestazione di pagina.
- `cap03/3.4-neve.md`: sostituiti i richiami delle Figure 3.4.1, 3.4.2, 3.4.3 e C3.4.1-C3.4.7 verso nuovi PNG estratti dai PDF sorgenti. I vecchi ritagli includevano testo tagliato, didascalie incorporate o zone sbagliate della pagina.
- `cap03/3.5-temperatura.md`: sostituiti i richiami delle Figure 3.5.1 e 3.5.2 verso nuovi ritagli puliti della mappa delle zone di temperatura e dello schema di distribuzione della temperatura.
- `cap03/img/`: creati 13 nuovi file con suffissi descrittivi `-grafico`, `-mappa` o `-schema`, per evitare cache di Obsidian sui vecchi file errati.
- `_tmp_render/cap03/audit-immagini/`: prodotte tavole di controllo visivo delle immagini richiamate dal capitolo 3.

## 2026-06-03 - Pulizia esempi Markdown

- `README.md` e `TODO.md`: riscritti alcuni esempi di figure e navigazione in forma non cliccabile, così i controlli automatici dei link non li scambiano per collegamenti reali mancanti.

## 2026-06-02 - Correzione Tabella C3.3.XI

- `cap03/3.3-vento.md`: riscritta la Tabella C3.3.XI delle coperture a doppia falda con vento ortogonale al colmo. La tabella precedente non rendeva correttamente celle accorpate e sotto-righe alternative del PDF.
- `cap03/3.3-vento.md`: normalizzate le colonne per zone F/G/H/I/J e per sottocampi `$c_{pe,10}$`/`$c_{pe,1}$`; i valori accorpati nel PDF sono ripetuti nelle due colonne Markdown quando valgono per entrambi.
- `cap03/3.3-vento.md`: corretti valori specifici della XI, inclusi il valore alternativo della zona J a `5°` (`+0,2`, non `−0,2`) e i segni delle zone F/G/H a `60°` e `75°` (`+0,7` e `+0,8`, non negativi).
- `cap03/3.3-vento.md`: aggiunta la Nota 8 per documentare la normalizzazione della Tabella C3.3.XI.
- `_tmp_render/cap03/confronti/tab-C3.3.XI-pdf.png`: creato ritaglio ad alta risoluzione della tabella PDF per controllo visivo.

## 2026-06-02 - Correzione Tabella C3.3.VII

- `cap03/3.3-vento.md`: riscritta la Tabella C3.3.VII delle coperture a semplice falda con vento ortogonale al colmo. La tabella precedente era sbilanciata: la zona H non aveva sottocolonne esplicite e alcune celle erano fuse, ad esempio valori come `−0,6 −1,2` nella stessa cella.
- `cap03/3.3-vento.md`: divisa la trascrizione in due sottotabelle, `Θ = 0°` e `Θ = 180°`, con colonne esplicite per zone F/G/H e per `$c_{pe,10}$`/`$c_{pe,1}$`.
- `cap03/3.3-vento.md`: aggiunta la Nota 7 per chiarire che i valori accorpati nel PDF sono ripetuti nei due sottocampi quando valgono per entrambi.
- `_tmp_render/cap03/confronti/tab-C3.3.VII-pdf.png`: creato ritaglio ad alta risoluzione della tabella PDF per controllo visivo.

## 2026-06-02 - Correzione Figure C3.3.9-C3.3.28

- `cap03/3.3-vento.md`: aggiornati tutti i collegamenti delle figure residue della Circolare vento, da C3.3.9 a C3.3.28, verso nuovi ritagli puliti dal PDF `raw/Circolare-7-2019-NTC.pdf`.
- `cap03/img/`: creati 20 nuovi PNG puliti, mantenendo solo grafici e schemi della figura ed eliminando intestazioni di pagina, didascalie incorporate, testo normativo circostante e tabelle adiacenti.
- `cap03/img/fig-C3.3.25-tettoie-multiple-schema.png`: corretta una mappatura errata; il vecchio file richiamato nel capitolo mostrava un ritaglio della Fig. C3.3.24 invece della figura sulle tettoie a falda multipla.
- `cap03/img/fig-C3.3.26-cilindro-cpe-schema-grafico.png`: corretta una mappatura errata; il vecchio file richiamato nel capitolo mostrava formule/testo della Circolare invece del grafico del coefficiente di pressione esterna del cilindro.
- `_tmp_render/cap03/confronti/fig-c3.3.9-28-anteprima.png`: creata anteprima complessiva per controllo visivo dei nuovi ritagli.

## 2026-06-02 - Correzione Figure C3.3.7-C3.3.8

- `cap03/3.3-vento.md`: aggiornati i collegamenti delle Figure C3.3.7 e C3.3.8 verso nuovi ritagli puliti dal PDF della Circolare.
- `cap03/img/fig-C3.3.7-falda-singola-schema-pulito.png`: creato ritaglio solo schema, rimuovendo Tabella C3.3.IV, testo del paragrafo e didascalia incorporata.
- `cap03/img/fig-C3.3.8-falda-singola-cpe-perp-grafico.png`: creato ritaglio solo grafico, rimuovendo la Figura C3.3.7 e la didascalia incorporata.

## 2026-06-02 - Correzione Tabella C3.3.IV

- `cap03/3.3-vento.md`: corretta la Tabella C3.3.IV delle coperture piane. La tabella precedente aveva righe sbilanciate e celle vuote dovute agli accorpamenti grafici del PDF. La trascrizione è stata normalizzata con colonne esplicite per `F/G/H/I` e per `$c_{pe,10}$`/`$c_{pe,1}$`.
- `cap03/3.3-vento.md`: aggiunta la Nota 6 per chiarire che i valori accorpati nel PDF, in particolare nella zona I e nella zona H per raccordi curvi e piani, sono ripetuti in entrambe le colonne Markdown per evitare ambiguità.

## 2026-06-02 - Ritagli solo schema Figure C3.3.1-C3.3.6

- `cap03/3.3-vento.md`: aggiornati i collegamenti delle Figure C3.3.1, C3.3.2, C3.3.4, C3.3.5 e C3.3.6 verso immagini senza didascalia incorporata; la didascalia resta come testo Markdown sotto ogni figura.
- `cap03/img/fig-C3.3.1-coefficiente-alfa-r-schema.png` e `cap03/img/fig-C3.3.2-pareti-verticali-schema.png`: creati ritagli puliti dal PDF della Circolare, eliminando rispettivamente intestazione/didascalia e testo descrittivo già riportato nel Markdown.
- `cap03/img/fig-C3.3.4-quote-riferimento-schema.png`, `cap03/img/fig-C3.3.5-coperture-piane-schema.png` e `cap03/img/fig-C3.3.6-zone-coperture-piane-schema.png`: creati/aggiornati ritagli puliti dal PDF della Circolare, mantenendo solo gli schemi e le etichette grafiche necessarie.

## 2026-06-01 - Annotazioni separate dal testo normativo

- `cap03/annotazioni/`: creata la cartella per separare note tecniche, dubbi e possibili refusi dal testo normativo principale.
- `cap03/annotazioni/tab-c3.3.i-refuso-cu.md`: spostato qui l'approfondimento sul possibile refuso `$C_{U}$` della Tab. C3.3.I, mantenendo il testo normativo in `cap03/3.3-vento.md` più pulito.
- `cap03/annotazioni/README.md`: aggiunto indice delle annotazioni del capitolo 3 e convenzione minima per future note collaborative.
- `cap03/3.3-vento.md` e `cap03/indice-cap03.md`: aggiornati i rimandi verso la nuova cartella `annotazioni/`.
- `cap03/3.3-vento.md`: spostate le note dentro la sezione finale "Note redazionali"; nel testo normativo restano solo note numerate con wikilink Obsidian accanto ai punti interessati, con link di ritorno al punto annotato.
- `cap03/3.3-vento.md`: convertite nello stesso sistema anche le note precedenti sulle formule `[3.3.1]`, `[3.3.2]` e sulla Fig. 3.3.2; la Nota di Sandro sulla Tab. C3.3.I resta attribuita nel richiamo redazionale.
- `cap03/3.3-vento.md`: aggiunta la voce "Note redazionali" nel sommario iniziale del file.
- `cap03/3.3-vento.md`: aggiunto identificatore Obsidian al sommario (`^sommario-3-3`) e link "Torna al sommario" sotto le principali destinazioni dell'indice interno, come prova di navigazione su Obsidian W520/mobile.
- `cap03/annotazioni/fig-3.3.2-categorie-esposizione-lettura-llm.md`: spostata in annotazione separata la lettura tabellare dello schema della Fig. 3.3.2, così il capitolo principale resta più fedele al testo normativo.
- `cap03/indice-cap03.md`: aggiunto il rimando all'approfondimento sulla Fig. 3.3.2 sotto il §3.3.7.
- `cap03/3.4-neve.md`: rese heading reali le sottosezioni C3.4.3.3.1-C3.4.3.3.6 della Circolare neve; la Fig. C3.4.4 sulle coperture cilindriche era già presente, ma ora è raggiungibile dal sommario interno.
- `cap03/indice-cap03.md`: aggiunti link diretti alle figure C3.4.4-C3.4.7 della Circolare neve.
- `cap03/img/fig-C3.3.4-quote-riferimento-ritaglio.png`: riestratta dal PDF della Circolare la Fig. C3.3.4 sulle quote di riferimento negli edifici bassi e alti, usando un nuovo nome file per forzare il refresh su Obsidian mobile. Il vecchio file esisteva, ma il ritaglio precedente includeva tabella e testo della pagina invece della figura.
- `cap03/img/fig-C3.3.5-coperture-piane-ritaglio.png`: riestratta dal PDF della Circolare la Fig. C3.3.5 sullo schema di riferimento per coperture piane, usando un nuovo nome file per forzare il refresh su Obsidian mobile. Il vecchio file mostrava testo precedente invece della figura.
- `cap03/img/fig-C3.3.6-zone-coperture-piane-ritaglio.png`: riestratta dal PDF della Circolare la Fig. C3.3.6 sulla suddivisione delle coperture piane e sulle altezze di riferimento. Il vecchio file includeva anche Fig. C3.3.5, Tab. C3.3.III e testo precedente.
- `README.md`: aggiunta la convenzione generale per tenere annotazioni e testo normativo separati, in vista di un possibile uso open source collaborativo.

## 2026-05-31 - Nota di Sandro su Tab. C3.3.I

- `cap03/3.3-vento.md`: mantenuta la Tab. C3.3.I con le intestazioni del PDF della Circolare (`$C_{U}=2{,}0$` e `$C_{U}=1{,}5$`) e aggiunto un richiamo redazionale che segnala il dubbio sull'assenza di intestazioni esplicite per faccia sottovento e facce laterali. Valori, formule e testo tabellare invariati rispetto alla fonte.
- `cap03/annotazioni/tab-c3.3.i-refuso-cu.md`: aggiunto approfondimento dedicato dal report di ricerca fornito da Sandro su Google Drive. Il documento classifica il caso come probabile refuso non confermato ufficialmente, riassume le fonti cercate e propone la lettura tecnica prudente delle colonne come facce laterali e faccia sottovento.
- `cap03/indice-cap03.md`: aggiunto il link all'approfondimento sotto la voce C3.3.8.1.
- `cap03/3.3-vento.md`, `cap03/annotazioni/tab-c3.3.i-refuso-cu.md`, `cap03/indice-cap03.md`: normalizzata la resa Markdown della notazione come `$C_{U}$`, evitando LaTeX dentro il testo del link per non mostrare `$...$` letterali nei viewer mobili.
- `cap03/3.3-vento.md`: corretta la Tab. C3.3.II. Nel PDF le celle delle zone C ed E sono accorpate sui sottocampi `$c_{pe,10}$` e `$c_{pe,1}$`; nel Markdown precedente il valore era riportato solo nella prima delle due colonne, lasciando vuota la seconda. I valori sono ora ripetuti in entrambe le colonne, con richiamo redazionale, e le intestazioni sono state normalizzate come `A cpe,10`, `A cpe,1`, ecc. per evitare celle vuote ambigue.

## 2026-05-31 - Ritaglio Fig. C3.3.2

- `cap03/img/fig-C3.3.2-pareti-verticali-hires.png`: aggiornato il link in `cap03/3.3-vento.md` verso un nuovo render ad altissima risoluzione dal PDF della Circolare (`4368x1584 px`), così il capitolo Markdown non resta agganciato a immagini precedenti in cache. Il ritaglio rimuove i paragrafi e le intestazioni catturati sopra la figura; anche i vecchi nomi `fig-C3.3.2-pareti-verticali.png` e `fig-C3.3.2-pareti-verticali-ritaglio.png` sono stati allineati allo stesso render. L'originale completo è conservato in `_tmp_render/cap03/figure-originali/fig-C3.3.2-pareti-verticali-original.png`.
- `cap03/img/fig-C3.3.3-zone-pareti-verticali-hires.png`: riestratta la Fig. C3.3.3 direttamente dal PDF della Circolare ad alta risoluzione, rimuovendo la coda della Tab. C3.3.I e la riga di testo catturate sopra la figura. Il link in `cap03/3.3-vento.md` punta al nuovo nome file per evitare cache del visualizzatore; anche il vecchio nome `fig-C3.3.3-zone-pareti-verticali.png` è stato allineato allo stesso render. L'originale precedente è conservato in `_tmp_render/cap03/figure-originali/fig-C3.3.3-zone-pareti-verticali-original.png`.
- `cap03/img/fig-C3.3.3-zone-pareti-verticali-schema-hires.png`: aggiornato il ritaglio della Fig. C3.3.3 per rimuovere anche la didascalia interna e lasciare solo gli schemi con le etichette (a) e (b). Il testo descrittivo resta nella didascalia Markdown sotto l'immagine; anche i vecchi nomi della figura sono stati allineati allo stesso render.

## 2026-05-31 - Ritaglio Fig. 3.3.1

- `cap03/img/fig-3.3.1-mappa-zone-vento-ritaglio.png`: ritagliata la Fig. 3.3.1 ripartendo dall'immagine originale, per lasciare solo la mappa dell'Italia completa, inclusa la Sicilia, rimuovendo intestazione e bordo superiore del PDF. Il link in `cap03/3.3-vento.md` punta al nuovo nome file per evitare cache del visualizzatore mobile.
- `cap03/img/fig-3.3.2-categorie-esposizione-ritaglio.png` e `cap03/img/fig-3.3.2-categorie-esposizione.png`: ritagliata la Fig. 3.3.2 per lasciare solo gli schemi delle categorie di esposizione, rimuovendo la Tab. 3.3.III e il testo già trascritti in Markdown. Anche il vecchio nome file è stato sovrascritto con il ritaglio per evitare vecchi riferimenti o cache del visualizzatore mobile.
- `cap03/3.3-vento.md`: aggiunta sotto la Fig. 3.3.2 una nota di lettura per LLM con trascrizione tabellare degli schemi di categoria di esposizione per zone 1-5, 6, 7-8 e 9.
- `cap03/3.3-vento.md`: aggiunta una nota di lettura sotto la formula `[3.3.2]` per chiarire che `$v_b$` si legge "v con pedice b" e non `$v_0$`.

## 2026-05-30 - Correzione didascalie Fig. C3.2.1

- `cap03/3.2-azione-sismica.md`: corretta la notazione da `$T^*_C$` a `$T_C^*$` nel testo della Circolare C3.2 e riscritte le didascalie delle Figure C3.2.1 a-c senza corsivo globale `*...*`, così l'asterisco della formula `$T_C^*$` non viene più interpretato come markup Markdown.
- `cap03/3.3-vento.md`: corretto nel §3.3.1 NTC il testo "a 10 m di altezza al suolo" in "a 10 m di altezza sul suolo", come da PDF della norma.
- `cap03/3.3-vento.md`: aggiunta una nota di lettura sotto la formula `[3.3.1]` per chiarire che `$v_{b,0}$` si legge "v con pedice b,0" e non `$v_o$`.
- `cap03/3.3-vento.md`: corretta la definizione sotto la formula `[C3.3.1]` della Circolare, da `$v_R$` a `$v_b$`, coerentemente con la formula `$v_b(T_R) = \alpha_R \cdot v_b$` e con il PDF.

## 2026-05-30 — Tab. 3.2.I: rappresentazione Markdown più adatta agli LLM

- `cap03/3.2-azione-sismica.md`: trasformata la Tab. 3.2.I da layout con celle vuote, usato per imitare l'accorpamento grafico del PDF, a tabella normalizzata con colonne `Gruppo`, `Stato limite`, `$P_{V_R}$`. I valori restano invariati e già verificati: SLO 81%, SLD 63%, SLV 10%, SLC 5%.
- Rigenerato il confronto Markdown in `_tmp_render/cap03/confronti/tab-3.2.I-md.png`; il confronto PDF resta in `_tmp_render/cap03/confronti/tab-3.2.I-pdf.png`.

## 2026-05-30 — Controllo numerico delle tabelle del Capitolo 4

Verifica delle tabelle del cap. 4, norma e Circolare C4, contro i PDF sorgenti in `raw/`. Controllo mirato ai valori tabellari, distinto dalla revisione di completezza del 20/5.

**Correzioni principali**:
- `cap04/4.2-acciaio.md`: riallineate le tabelle 4.2.I, 4.2.II, 4.2.VI, 4.2.VII, 4.2.IX(a-b), 4.2.XI, 4.2.XII, 4.2.XIII, 4.2.XIV, 4.2.XV, 4.2.XVI, 4.2.XVII e 4.2.XIX.
- `cap04/4.3-composte.md`: riallineate 4.3.I e 4.3.II; sostituita 4.3.III con immagine estratta dal PDF per conservare schemi e fattori originali.
- `cap04/4.4-legno.md`: riallineate 4.4.I, 4.4.II e 4.4.III; mantenute 4.4.IV e 4.4.V come immagini da PDF e aggiunta una trascrizione testuale controllata sotto ciascuna tabella, così i valori restano interrogabili anche dagli LLM che leggono solo Markdown. La trascrizione precedente introduceva colonne/semplificazioni non presenti nella fonte.

**Esito Circolare C4**: tabelle controllate senza correzioni necessarie. `4.1-calcestruzzo.md` e `4.5-muratura.md` risultano coerenti per le tabelle controllate; `4.6-altri-sistemi.md` non contiene tabelle.

Immagini di verifica PDF/Markdown prodotte in `_tmp_render/cap04/confronti/`. Dettaglio nel registro `cap04/cap04-costruzioni-civili-industriali-revisione.md`, rilievo R8.

## 2026-05-29 — Pulizia fonti: una sola edizione della Circolare

Le due copie della Circolare 7/2019 in `raw/` sono lo stesso documento. Eliminata la versione compressa `Circ_MIT_21_01_2019_7_rid.pdf` (11 MB, 337 pp., tabelle-immagine a bassa risoluzione ~520×315 px) e mantenuta `Circolare-7-2019-NTC.pdf` (48 MB, 348 pp., stesse tabelle a ~1000-1300 px, molto più leggibili). Testo equivalente (≈1,01 M caratteri in entrambe).

**Riferimenti residui al vecchio nome/offset** (non modificati per non introdurre numeri di pagina errati; da aggiornare quando si lavora su quei file): `cap08/8-esistenti.md`, gli script `estrai-figure-c4.1.py` / `estrai-figure-c4.2.py` / `estrai-figure-c4.2-bis.py` (storici, figure già estratte), la skill dismessa `skills/conversione-ntc2018/SKILL.md`. Sul file mantenuto gli offset della Circolare sono ≈ +4 rispetto al rid.

## 2026-05-29 — Controllo numerico delle tabelle del Capitolo 3 (Azioni sulle costruzioni)

Verifica cella per cella di tutte le tabelle del cap. 3 (norma e Circolare) contro i PDF in `raw/` (testo OCR + render ad alto zoom 4-17×; cross-check sulla 2ª edizione della Circolare per i simboli). È il controllo dei *valori* dentro le tabelle, distinto dalla revisione strutturale/filologica del 20/5.

**Esito**: §3.1 e §3.2 già verificati in precedenza (OK); §3.3-3.6 verificati in questa sessione. Sulle 22 tabelle del vento (3 norma + 19 Circolare): 17 OK, 5 corrette. Neve/temperatura/eccezionali: OK, con un'integrazione minore.

**Correzioni in `cap03/3.3-vento.md`** (Circolare vento):
- **Tab. C3.3.I**: intestazione colonne 2-3 da "$c_{L1}$" a "$C_{U}=2{,}0$ / $C_{U}=1{,}5$" (dicitura fedele alla GU, identica nelle due edizioni; i valori erano già corretti).
- **Tab. C3.3.VII**: aggiunta la sotto-riga di valori alternati "0 | 0 | 0" ad α=5° (Θ=0°, zone F/G/H), prima omessa.
- **Tab. C3.3.VIII**: riscritta — mancava la zona **F_b** (sono 5 zone: F_a, F_b, G, H, I); corretto H $c_{pe,1}$=−1,3 (era −1,5) per α=30°-75° e ripristinata la zona I.
- **Tab. C3.3.XIV**: riscritta — il md fondeva "L,M,N" in una colonna e perdeva segni/valori; ripristinate le 9 zone F-N con $c_{pe,10}$/$c_{pe,1}$ e le sotto-righe alternate di F/G/H.
- **Tab. C3.3.XVI**: corretto il segno dei "Valori positivi": $c_f$=+0,2+0,7|α|/30 (era −0,2−0,7|α|/30).

**Correzioni in `cap03/3.4-neve.md`**: aggiunta "Olbia-Tempio" all'elenco province della Zona III (presente nella GU, era omessa).

**Rilievo indice C3.2 chiuso come infondato**: le tabelle C.3.2.I e C.3.2.II esistono nel PDF (titolate "C.3.2", col punto dopo la C, sfuggite ai grep su "C3.2") e sono già presenti e corrette in `3.2-azione-sismica.md`; l'indice che le cita è corretto, nessuna modifica.

**Verificate OK senza modifiche**: norma 3.3.I-III, 3.4.I-II, 3.5.I-IV, 3.6.I-III + formule q_sk e T_min/T_max per zona; Circolare C3.3.III, V, VI, IX, X, XII, XIII, XV, XVII-XIX, C3.4.I, C.3.2.I-II. Note successive: la Tab. C3.3.II, la Tab. C3.3.IV, la Tab. C3.3.VII e la Tab. C3.3.XI sono state normalizzate per rendere esplicite in Markdown le celle accorpate e le sotto-righe.

Dettaglio nel registro `cap03/cap03-azioni-sulle-costruzioni-revisione.md`, § "Controllo numerico delle tabelle". File di lavoro (render/script) in `_tmp_render/cap03/`.

## 2026-05-29 — Murature: riscrittura Tab. C8.5.I e C8.5.II

- **Riscrittura Tab. C8.5.I e C8.5.II (caratteristiche meccaniche murature esistenti) in `cap08/8-esistenti.md`**: le due tabelle convertite erano gravemente errate. Riscritte integralmente dal PDF della Circolare (`raw/Circ_MIT_21_01_2019_7_rid.pdf`, pp. 257-258), con verifica incrociata sulla seconda edizione (`raw/Circolare-7-2019-NTC.pdf`, p. 261). Errori corretti:
  - **Unità di misura sbagliate**: `f` e `τ₀` erano indicati in N/cm² invece di N/mm² (fattore 100).
  - **Colonna `f_v0` assente**: aggiunta la colonna della resistenza a taglio per murature regolari (criterio di scorrimento), distinta da `τ₀` (murature irregolari).
  - **Tab. C8.5.I**: due tipologie inesistenti ("conci di pietra tenera con malta di buona qualità", "blocchi laterizi semipieni pareti da 30 cm") sostituite con le tipologie reali ("conci sbozzati a spessore disomogeneo", distinzione "irregolare" / "conci regolari" di pietra tenera); corretti `f`, `E`, `G`, `w` di varie righe; ripristinate le note ufficiali (*), (**), (***) e il peso variabile 13÷16 per la pietra tenera.
  - **Tab. C8.5.II**: aggiunta la colonna "Massimo coefficiente complessivo" (mancante); corrette etichette di colonna, tipologie e valori dei coefficienti; aggiunte note ufficiali (*)-(****), inclusa la definizione di "malta buona" per i mattoni e il coefficiente $f_m^{0{,}35}$.
  - Segnalata anomalia: la cella `f` dei conci sbozzati riporta "2,0" (valore singolo) in entrambe le edizioni PDF, contro l'intervallo 2,0-3,0 comunemente riportato; lasciata nota di conversione, da verificare sulla GU.
  - Immagini di lavoro in `_tmp_render/murature/`.
- **Allineati gli strumenti di calcolo che riportavano la stessa tabella errata** (la propagazione era il rischio operativo: questi file servono per verifiche firmate):
  - `skills/verifica-muratura-esistente/calcola_resistenza_muratura.py`: corretti tutti i valori della Tab. C8.5.I (erano quelli vecchi/errati, in parte ripresi dalla Circolare 2009); rimossa la tipologia inesistente `tufo-malta-buona` (sostituita da `tufo-regolare` = conci regolari di pietra tenera) e `laterizi-semipieni`; corretta l'etichetta di `mattoni-cem` (sono semipieni); separata la resistenza a taglio `tau0` (murature irregolari) da `fv0` (regolari). Test: il caso exmulino (tufo LC1) ridà f_d = 0,52 N/mm² e tasso 0,84.
  - `metodo-resistenze-muratura-esistente.md` (scheda di metodo, fonte unica della skill): allineate la Tab. C8.5.I (aggiunta colonna f_v0) e l'estratto della Tab. C8.5.II; aggiornato l'esempio exmulino (riga base tufo 140-220).
  - Chi avesse comandi/relazioni salvati con le chiavi `tufo-malta-buona` o `laterizi-semipieni` dello script deve aggiornarli.

## 2026-05-27

- **Segnalazione discrepanza testo C8.4.1 vs PDF originale**: nel file `cap08/8-esistenti.md` la trascrizione della Circolare C8.4.1 (righe 326-337) è una parafrasi e non corrisponde al testo letterale del PDF `raw/Circolare-7-2019-NTC.pdf` (pag. 252).
  - Il file md elenca 6 bullet di esempi tra cui "la modifica di una porzione limitata della struttura (ad esempio, la sostituzione di un solaio, la rimozione di una tramezzatura pesante)".
  - Il PDF originale articola in 3 sotto-categorie e cita come esempio della terza "l'apertura di un vano in una parete, accompagnata da opportuni rinforzi". La sotto-categoria 2 ("realizzazione di nuovi collegamenti [...] tra componenti prefabbricati") non è resa fedelmente nel md.
  - Quando si cita la C8.4.1 in atti ufficiali, prendere il testo dal PDF in `raw/`. Da rivedere la conversione md di `cap08/8-esistenti.md` per allineare il testo della Circolare alla fonte primaria.
  - Contesto: scoperto durante l'analisi della richiesta di perfezionamento del Genio Civile sul progetto `volterra12` (vedi `progetti_lavoro/volterra12/volterra12-260527-analisi-classificazione.md`).

## 2026-05-25

- Riordino strutturale: spostati i 3 PDF sorgente (`NTC_18 con segnalibri...`, `Circolare-7-2019-NTC`, `Circ_MIT_21_01_2019_7_rid`) dalla radice della cartella alla sottocartella `raw/`, per coerenza con la nuova convenzione `<norma>/raw/` adottata nel riordino di `normativa/`.

## 2026-05-21

- Rinominato e riorganizzato il documento di revisione del capitolo 4:
  - rimosso il vecchio file `cap04/4.1-costruzioni-calcestruzzo-revisione.md`, troppo simile al nome del file sorgente e quindi ingannevole;
  - creato `cap04/cap04-costruzioni-civili-industriali-revisione.md` come documento unico di revisione per tutto il capitolo 4;
  - incorporati i rilievi storici sul § 4.1 e aggiunte sezioni di stato per 4.1-4.6;
  - aggiornati `cap04/indice-cap04.md` e `README.md` con il nuovo riferimento.

## 2026-05-20

- **Completamento §C4.2 - Circolare Costruzioni di acciaio**: chiuso il blocco mancante in `cap04/4.2-acciaio.md`, dal §C4.2.4.1.4 Stato limite di fatica al §C4.2.12 Profilati formati a freddo e lamiere grecate.
  - Aggiunte formule `[C4.2.93]`-`[C4.2.166]`, comprese curve S-N, fatica dei connettori a piolo, profili formati a freddo, verifiche di resistenza/stabilità e unioni per piccoli spessori.
  - Aggiunte/rigenerate dal nuovo PDF le immagini `Fig. C4.2.19`-`Fig. C4.2.36`, le tabelle grafiche di fatica `Tab. C4.2.XII.a`-`Tab. C4.2.XVII` e le tabelle `C4.2.XIX`-`C4.2.XX`.
  - Aggiornati `indice-ntc2018.md`, `cap04/indice-cap04.md`, `TODO.md`, `README.md` e l'indice interno di `4.2-acciaio.md`.
  - Esito: Capitolo 4 **ok come capitolo completo**; la Circolare C4.2 è completa. Il PDF passa direttamente da C4.2.4.1.4.6 a C4.2.9 e C4.2.12, quindi non contiene commenti autonomi per C4.2.5, C4.2.8, C4.2.10 o C4.2.11.

- **Controllo Capitolo 4 - Costruzioni civili e industriali**: verificati i file `cap04/` contro il PDF NTC 2018 pagine 73-152 e contro la Circolare C4.
  - Norma: controllo formule, figure, tabelle e link sui file 4.1-4.6; nessuna immagine richiamata mancante e nessun wikilink rotto. La doppia formula `4.1.50` è confermata nel PDF NTC, quindi non è un errore del Markdown; aggiornata la nota nel file di revisione del §4.1.
  - Circolare: C4.1 e C4.3-C4.6 risultano presenti; C4.2 resta incompleta perché manca ancora il blocco da C4.2.4.1.4 Fatica a C4.2.12.
  - Corretto `cap04/4.2-acciaio.md`: riallineata al PDF la numerazione delle formule del blocco C4.2.4.1.3.4, togliendo il numero indebito alla formula di `sigma_E`, riportando le formule a `[C4.2.51]`-`[C4.2.92]` e separando `[C4.2.78.a]`/`[C4.2.78.b]` e `[C4.2.81.a]`/`[C4.2.81.b]`.
  - Verificato il nuovo PDF `Circolare-7-2019-NTC.pdf`: per la coda C4.2 il testo coincide con `Circ_MIT_21_01_2019_7_rid.pdf` con offset di 4 pagine; le differenze estratte sono solo spaziature/artefatti nelle tabelle grafiche.
  - Esito: Capitolo 4 **non ancora ok come capitolo completo**, perché la Circolare C4.2 è ancora da completare.

- **Controllo Capitolo 3 - Azioni sulle costruzioni**: verificati i file `cap03/` contro il PDF NTC 2018 pagine 45-72 e contro la Circolare C3.
  - Norma: confronto con pagine PDF 45-72; corrette due frasi nelle sezioni 3.4 e 3.5, entrambe riportate a `compresa fra tre mesi ed un anno`.
  - Circolare: confronto con pagine PDF 41-79; aggiunta in C3.2 la Fig. C3.2.2 mancante, con frase introduttiva e immagine estratta dal nuovo PDF.
  - Verificato che il nuovo PDF `Circolare-7-2019-NTC.pdf` coincide con il PDF ridotto per C3; cambia solo l'offset delle pagine.
  - Verificati formule, tabelle, figure, immagini mancanti, link interni e indici; aggiornati `cap03/indice-cap03.md`, `TODO.md`, `indice-ntc2018.md` e il file di revisione `cap03/cap03-azioni-sulle-costruzioni-revisione.md`.

- **Controllo Capitolo 2 - Sicurezza e prestazioni attese**: verificato `cap02/2-sicurezza.md` contro il PDF NTC e contro la Circolare C2.
  - Norma: confronto con pagine PDF 37-44; corrette differenze puntuali di trascrizione e allineati pedici/simboli in §2.5.
  - Circolare: confronto con pagine PDF 35-40; corrette differenze puntuali di trascrizione in C2.4-C2.6.
  - Sistemata la Tab. 2.6.I in Markdown: l'intestazione aveva una colonna in meno rispetto alle righe, pur con valori corretti.
  - Verificati formule, tabelle, figura C2.1, link interni e corrispondenza del nuovo PDF `Circolare-7-2019-NTC.pdf` per C2.

- **Controllo Capitolo 1 - Oggetto**: verificato `cap01/1-oggetto.md` contro il PDF NTC e contro la Circolare C1.
  - Norma: confronto completo con pagine PDF 35-36, nessuna differenza residua.
  - Circolare: confronto completo con pagine PDF 28-34, corrette piccole differenze di trascrizione rispetto al testo della Gazzetta Ufficiale.
  - Verificato che il nuovo PDF `Circolare-7-2019-NTC.pdf` contiene per C1 lo stesso testo del PDF ridotto; cambia solo l'offset delle pagine file e la qualità grafica del documento.

- **§C4.3 — Circolare Costruzioni composte di acciaio-calcestruzzo** (pp. 143-150): conversione COMPLETA.
  - `cap04/4.3-composte.md` — sostituito il segnaposto della circolare con C4.3 premessa, C4.3.1 Valutazione della sicurezza, C4.3.2 Analisi strutturale, C4.3.4 Travi con soletta collaborante, C4.3.4.3 Sistemi di connessione, C4.3.4.3.6 Instabilità flesso-torsionale, C4.3.6 Solette composte con lamiera grecata.
  - Aggiunte formule [C4.3.1]-[C4.3.13], Tab. C4.3.II in markdown e 10 immagini: Tab. C4.3.I + Fig. C4.3.1-C4.3.9.
  - Riallineati anche i link alle figure della norma §4.3, che puntavano a nomi file non più presenti in `cap04/img/`.
  - Aggiornati `cap04/indice-cap04.md`, `TODO.md` e `README.md`.
  - Stato intermedio dopo C4.3: C4.1 e C4.3 fatti; C4.2 ancora in corso; C4.4-C4.6 non ancora lavorati in quella fase.
- **§C4.4 - Circolare Costruzioni di legno** (pp. 151-159): conversione COMPLETA.
  - `cap04/4.4-legno.md` - sostituito il segnaposto della circolare con C4.4 premessa, valutazione della sicurezza, analisi, azioni, classi di durata e servizio, resistenza di progetto, SLE, SLU, collegamenti, elementi, sistemi strutturali, robustezza, durabilità, fuoco, esecuzione e controlli.
  - Aggiunte formule [C4.4.1]-[C4.4.3] e Fig. C4.4.1.
- **§C4.5 - Circolare Costruzioni di muratura** (p. 161): conversione COMPLETA.
  - `cap04/4.5-muratura.md` - aggiunte le indicazioni su verifiche agli SLU, verifiche semplificate, muratura armata e muratura confinata.
- **§C4.6 - Circolare Altri sistemi costruttivi** (p. 162): conversione COMPLETA.
  - `cap04/4.6-altri-sistemi.md` - aggiunte le indicazioni sui sistemi costruttivi non disciplinati dalle NTC, dichiarazione di idoneità e ruolo del Servizio Tecnico Centrale; aggiunto anche l'indice interno ora che il file contiene una sezione di circolare.
- Stato C4 aggiornato: C4.1 e C4.3-C4.6 fatti; resta da chiudere solo C4.2.
- Controllo collegamenti capitolo 4: corretti i richiami a immagini già presenti in `cap04/4.2-acciaio.md`, estratta la Tab. 4.2.XVIII mancante e riallineato il link alla Fig. 4.4.1 in `cap04/4.4-legno.md`.
- Controllo immagini esteso a NTC 2018: estratte le figure mancanti C3.2.1a-c, C3.2.3, C3.2.4 e C3.4.1-C3.4.7; in `cap07/7.11-geotecnica.md` eliminato il secondo richiamo immagine rotto perché la Fig. 7.11.1 esistente contiene già entrambe le parti a) e b).
- Chiuso il falso segnaposto C12: la circolare non contiene un commento specifico al Capitolo 12, quindi `cap12/12-riferimenti.md` ora riporta una nota esplicita e `cap12/indice-cap12.md` la richiama.
- Chiusura sessione: salvato riepilogo locale in `sessioni/260520-cdx-ntc2018-c4-circolare-e-controlli.md`; aggiornata pagina Notion `frm-ntc2018`; creata riga task Notion `260520-CDX-ntc2018-c4-circolare-e-controlli`.

## 2026-05-01

- Aggiunto indice cliccabile interno in cima a tutti i file foglia (34 file) — sezione `## Indice del capitolo` con wikilink agli heading h2/h3 (pattern allineato a `dpr380--edilizia/titolo-IV/capo-II-sanzioni.md`). File trattati: cap01/1-oggetto, cap02/2-sicurezza, cap03/{3.1-3.6, cap03-azioni-sulle-costruzioni-revisione}, cap04/{4.1, 4.1-revisione, 4.2-4.5}, cap05/{5.1, 5.2}, cap06/{6.1-6.2, 6.3, 6.4, 6.5-6.6, 6.7-6.12}, cap07/{7.0-7.2, 7.3, 7.4, 7.5, 7.6-7.7, 7.8, 7.9-7.10, 7.11}, cap08/8-esistenti, cap09/9-collaudo, cap10/10-redazione, cap11/{11.1-11.2, 11.3.1-11.3.2, 11.3.3-11.3.4, 11.4-11.6, 11.7, 11.8, 11.9, 11.10}. Saltati: `cap04/4.6-altri-sistemi.md` e `cap12/12-riferimenti.md` (file con sole h1, nessuna sezione h2/h3 da indicizzare).

## 2026-04-19 (sessione notturna 2)

- **§C4.2 — Circolare, terzo blocco stabilità pannelli** (pp. 108-119, 11 pp.): conversione C4.2.4.1.3.4 Stabilità dei pannelli (tutte e 9 le sotto-sezioni)
  - `cap04/4.2-acciaio.md` — aggiunte:
    - chiusura §C4.2.4.1.3.3 con Metodo generale: [C4.2.40] $\bar{\lambda}_{op}$, [C4.2.41] $\chi_{op}$, [C4.2.42] verifica $\chi_{op}\alpha_{ult,k}/\gamma_{M1} \ge 1$
    - C4.2.4.1.3.4.1 Pannelli a taglio: [C4.2.43]-[C4.2.57] (V_b,Rd, V_bw,Rd, V_bf,Rd, M_f,Rd, $\bar{\lambda}_w$, $\sigma_E$, $k_\tau$ con/senza irrigiditori longitudinali, I_st, forza assiale irrigiditori) con Tab. C4.2.VII ($\chi_w$) e Fig. C4.2.12
    - C4.2.4.1.3.4.2 Pannelli compressi: $\rho$ casi due/un lato [C4.2.58]-[C4.2.59], $\bar{\lambda}_p$ [C4.2.60], verifiche [C4.2.61]-[C4.2.62] con Tab. C4.2.VIII-IX
    - C4.2.4.1.3.4.3 Larghezza collaborante: $b_{eff}$ [C4.2.63], $\alpha_0$ [C4.2.64], distribuzione tensioni [C4.2.65] con Fig. C4.2.13-C4.2.14, $A_{c,eff}$ [C4.2.66], Tab. C4.2.X ($\beta$)
    - C4.2.4.1.3.4.4 Pannelli con irrigiditori: $A_{c,eff,loc}$ [C4.2.67], $A_{c,eff}$ totale [C4.2.68], $\rho_c$ [C4.2.69], $\xi$ [C4.2.70], Fig. C4.2.15-C4.2.16, Tab. C4.2.XI
    - C4.2.4.1.3.4.5 Instabilità di colonna: $\sigma_{cr,c}$ [C4.2.71]-[C4.2.72], $\sigma_{cr,sl}$ [C4.2.73], $\bar{\lambda}_c$ [C4.2.74]-[C4.2.75], $\alpha_e$ [C4.2.76], i [C4.2.77]
    - C4.2.4.1.3.4.6 Instabilità di piastra: $\sigma_{cr,p}$ [C4.2.78], $k_{\sigma,p}$ casi [C4.2.79], $\gamma$ [C4.2.80], $\delta$ [C4.2.81]; uno/due irrigiditori con Fig. C4.2.17, $\sigma_{cr,sl}$ [C4.2.82], $a_c$ [C4.2.83], $\sigma_{cr,p}$ min [C4.2.84]
    - C4.2.4.1.3.4.7 Requisiti irrigiditori trasversali: $w_0$ [C4.2.85] con Fig. C4.2.18
    - C4.2.4.1.3.4.8 Verifiche semplificate: I_st [C4.2.86], $\sigma_m$ [C4.2.87], u [C4.2.88], N_Ed [C4.2.89], $\Delta N_{st}$ [C4.2.90], q [C4.2.91], I_T/I_p [C4.2.92], $\sigma_{cr}$ torsionale [C4.2.93]
    - C4.2.4.1.3.4.9 Requisiti irrigiditori longitudinali
  - 7 figure estratte: Fig. C4.2.14-C4.2.20 (script `estrai-figure-c4.2-bis.py`)
  - 5 tabelle estratte come immagini: C4.2.VII, C4.2.VIII, C4.2.IX, C4.2.X, C4.2.XI (Tab. C4.2.VII resa anche in markdown)
  - **Nota numerazione**: nella circolare originale [C4.2.57] è duplicato (p.110 e p.111); il markdown applica shift di +1 da [C4.2.58] in poi per evitare ambiguità
  - Restano da convertire pp. 119-142 (23 pp.): C4.2.4.1.4 Fatica (pp. 119-130), C4.2.5 SLE, C4.2.8 Unioni, C4.2.10 Durabilità, C4.2.11 Fuoco, C4.2.12 classe 4

## 2026-04-19 (sessione notturna)

- **§C4.2 — Circolare Costruzioni di acciaio, secondo blocco** (pp. 102-108, 7 pp.): conversione C4.2.4 Verifiche (primo sotto-blocco aste composte + stabilità laterale + pressoflessione)
  - `cap04/4.2-acciaio.md` — aggiunte le sezioni:
    - C4.2.4.1.3.1 Aste compresse (composte, parete piena, tralicciate, calastrellate): imperfezione e0 [C4.2.21] con Fig. C4.2.7, forza normale correnti [C4.2.22]-[C4.2.23] con Ncr euleriano, taglio [C4.2.24], verifica aste tralicciate [C4.2.25]-[C4.2.26] con Fig. C4.2.8 e Tab. C4.2.II (rigidezza taglio SV per 4 schemi tralicciati/calastrellati), verifiche calastrellate [C4.2.27]-[C4.2.28] con Fig. C4.2.9, elementi ravvicinati [C4.2.29] con Fig. C4.2.10 e Tab. C4.2.III (imbottiture)
    - C4.2.4.1.3.2 Travi inflesse: momento critico Mcr [C4.2.30] per profili I/H con coefficiente ψ [C4.2.31]
    - C4.2.4.1.3.3 Membrature inflesse e compresse — Metodo A [C4.2.32]-[C4.2.36] con Fig. C4.2.11 (trave con MA, MB); Metodo B [C4.2.37]-[C4.2.38] con coefficienti kyy, kyz, kzy, kzz da Tab. C4.2.IV (sez. chiuse/aperte vincolate) e Tab. C4.2.V (sez. aperte non vincolate), correzione classe 4 [C4.2.39], coefficienti αmy, αmz, αmLT da Tab. C4.2.VI
  - 7 figure estratte: Fig. C4.2.7-C4.2.13 (script `estrai-figure-c4.2.py`)
  - 4 tabelle estratte come immagini: Tab. C4.2.II (in realtà renderizzata in markdown), Tab. C4.2.IV, Tab. C4.2.V, Tab. C4.2.VI
  - Restano da convertire pp. 109-142 (≈34 pp.): C4.2.4.1.3.4 Stabilità pannelli (Fig. C4.2.12 già estratta), C4.2.5 SLE, C4.2.8 Unioni, C4.2.10 Durabilità, C4.2.11 Fuoco, C4.2.12 Sezioni classe 4

## 2026-04-19 (sessione serale)

- **§C4.2 — Circolare Costruzioni di acciaio, primo blocco** (pp. 96-101, 6 pp.): conversione del primo blocco di C4.2
  - `cap04/4.2-acciaio.md` — sezione Circolare aggiunta: C4.2 premessa (acciai inossidabili, UNI EN 1993, UNI EN 1090-2:2011 e Specifica di esecuzione), C4.2.1 Materiali (acciai S235-S460 + inox), C4.2.2 Valutazione sicurezza (instabilità/fatica/basse temperature), C4.2.3 Analisi strutturale con tutte le sotto-sezioni:
    - C4.2.3.1 classificazione sezioni classi 1-4 ([C4.2.1] trattamento classe 4 come classe 3)
    - C4.2.3.3 metodi analisi globale (E/EP/P + ridistribuzione), Mpl,Rd [C4.2.2], lunghezza stabile a* [C4.2.3], gerarchia resistenze zone tese [C4.2.4]
    - C4.2.3.4 effetti deformazioni, moltiplicatore critico αcr ≥ 10 (elastica) o 15 (plastica), formula semplificata [C4.2.5] (Fig. C4.2.1), snellezza travi [C4.2.6]
    - C4.2.3.5 imperfezioni globali φ = φ0·αh·αm [C4.2.7]-[C4.2.8] con Fig. C4.2.2, effetti orizzontamenti Fig. C4.2.3, trascurabilità [C4.2.9], imperfezioni locali e0/L, forze concentrate/distribuite equivalenti [C4.2.11]-[C4.2.12] Fig. C4.2.4, controventi e0 [C4.2.13]-[C4.2.14] con Tab. C4.2.I (curve a0-d), carichi distribuiti [C4.2.15], N_Ed da elemento inflesso [C4.2.16] Fig. C4.2.5, forze giunzioni [C4.2.17] Fig. C4.2.6
    - C4.2.3.6 analisi stabilità strutture intelaiate, coefficiente amplificazione β [C4.2.18] per αcr ≥ 3,0
    - C4.2.3.7 lunghezza stabile Ls zona cerniera plastica [C4.2.19]-[C4.2.20] con ψ = M_Ed,min/M_pl,Rd
  - 6 figure estratte: Fig. C4.2.1-C4.2.6
  - 1 tabella: C4.2.I (valori massimi imperfezioni locali e0/L per curve instabilità a0, a, b, c, d)
  - Restano da convertire pp. 102-142 (≈41 pp.): C4.2.4 Verifiche (membrature, stabilità aste composte, pannelli), C4.2.5 SLE, C4.2.8 Unioni, C4.2.9 Progettazione/esecuzione, C4.2.10 Durabilità, C4.2.11 Fuoco, C4.2.12 Sezioni classe 4
- **Stato circolare aggiornato**: 10 capitoli + §C4.1 + §C4.2 primo blocco. C4 ancora in corso.

## 2026-04-19 (sessione pomeridiana)

- **§C4.1 — Circolare Costruzioni di calcestruzzo** (pp. 80-95, 16 pp.): conversione COMPLETA
  - `cap04/4.1-calcestruzzo.md` — sezione Circolare aggiunta: C4.1 premessa (γc=1,5, αcc=0,85, legami parabola-rettangolo/elasto-plastico/stress block, γs=1,15), C4.1.1.1 analisi elastica lineare con ridistribuzione momenti travi continue e telai (δ≥0,70, ΔM≤30%, [C4.1.1]), C4.1.2.1 cls confinato parabola-rettangolo + legame Annex E UNI EN 1998-2 con softening, C4.1.2.2 SLE deformazione [C4.1.2]-[C4.1.4] con Tab. C4.1.I (K e l/h limite), fessurazione wk [C4.1.5]-[C4.1.10] con Tab. C4.1.II-III, limitazione tensioni (n=15), C4.1.2.3 SLU NRd pilastri [C4.1.11], duttilità curvatura, torsione ν=0,5, zone diffusive, C4.1.6 dettagli costruttivi (copriferro Tab. C4.1.IV), C4.1.9 solai misti c.a./laterizio (regole generali, limiti dimensionali, caratteristiche fisico-meccaniche), C4.1.12 calcestruzzo aggregati leggeri LC (Tab. C4.1.V-VI, [C4.1.12]-[C4.1.19], Fig. C4.1.13)
  - 13 figure estratte: Fig. C4.1.1-C4.1.13 (Fig. C4.1.10 combinata da pp. 87-88)
  - 6 tabelle: C4.1.I (K e l/h), C4.1.II (diametri fessurazione), C4.1.III (spaziature fessurazione), C4.1.IV (copriferri), C4.1.V (classi LC), C4.1.VI (classi massa LC)
  - Aggiornati `indice-cap04.md` con sommario Circolare §C4.1 e `TODO.md`
- **Stato circolare aggiornato**: 10 capitoli + §C4.1 completato. Restano C4.2-C4.6 per completare C4.

## 2026-04-19

- **Capitolo C7 — Circolare Progettazione per azioni sismiche** (pp. 193-248, 56 pp.): conversione COMPLETA su tutti gli 8 file della cartella `cap07/`
  - `cap07/7.0-7.2-generalita-criteri.md` — C7.0 introduzione, C7.1 requisiti SL, C7.2.1 regolarità (Fig. C7.2.1, C7.2.2), C7.2.2 dissipativo/non dissipativo + CD"A"/CD"B" + γRd, C7.2.3 elementi secondari/non strutturali con spettri di piano (formule [C7.2.1]-[C7.2.11], Tab. C7.2.I-II, Fig. C7.2.3, C7.2.4), C7.2.6 modellazione + αf (Fig. C7.2.5)
  - `cap07/7.3-metodi-analisi.md` — C7.3.1 q' [C7.3.1], C7.3.3 lineare (CQC/SRSS, [C7.3.2]), C7.3.4 non lineare statica/dinamica (Metodo A/B per pushover, [C7.3.3]-[C7.3.10], Fig. C7.3.1-C7.3.5), C7.3.5 componenti, C7.3.6 requisiti SL (Tab. C7.3.I)
  - `cap07/7.4-calcestruzzo.md` — C7.4 introduzione, C7.4.2 conglomerato, C7.4.3 tipologie + deformabilità torsionale ([C7.4.1]-[C7.4.2]), C7.4.4 dimensionamento (travi Fig. C7.4.1, pilastri [C7.4.3] + Fig. C7.4.2, nodi Fig. C7.4.3, diaframmi, pareti con ridistribuzione 30%), C7.4.5 prefabbricate (Fig. C7.4.4-C7.4.6), C7.4.6 dettagli (pilastri θ ≤ 0,3, nodi)
  - `cap07/7.5-acciaio.md` — C7.5.2 tipologie (Fig. C7.5.1), C7.5.3 generali (bulloni/saldature), C7.5.4 telaio + pannelli ([C7.5.1]-[C7.5.2], Fig. C7.5.2), C7.5.5 controventi concentrici ([C7.5.3], Fig. C7.5.3), C7.5.6 eccentrici (link Fig. C7.5.4)
  - `cap07/7.6-7.7-composte-legno.md` — **C7.6** composte (collegamenti zone dissipative con meccanismi 1-2-3 trasferimento soletta-colonna [C7.6.1]-[C7.6.11], Fig. C7.6.1-C7.6.5; pannelli composti [C7.6.12]-[C7.6.14], Fig. C7.6.6; controventi concentrici/eccentrici composti) + **C7.7** legno (aspetti concettuali, materiali, tipologie, analisi strutturale, disposizioni costruttive)
  - `cap07/7.8-muratura.md` — C7.8.1 regole generali (premessa, materiali con foratura 45/55%, analisi statica non lineare, verifiche SLD/SLV/SLO/SLC, q* ≤ 4/3, costruzioni semplici), C7.8.2 ordinaria (capacità spostamento SLC 1,0%, taglio), C7.8.3 armata (1,6%), C7.8.4 confinata (UNI EN 1996, 1,2%/0,5%), C7.8.5 miste, C7.8.6 dettagli
  - `cap07/7.9-7.10-ponti-isolamento.md` — **C7.9** progettazione in capacità pile da ponte (Fig. C7.9.1) + **C7.10** isolamento e dissipazione (C7.10.1 scopo + Fig. C7.10.1, C7.10.2 dissipazione + Fig. C7.10.2, C7.10.2 requisiti generali sovra/sotto-struttura non dissipativa CDB, C7.10.3 dispositivi, C7.10.4 indicazioni progettuali con Fig. C7.10.3 + [C7.10.1]-[C7.10.2], C7.10.5 modellazione e analisi statica/dinamica/non lineare con [C7.10.3]-[C7.10.8], C7.10.6 verifiche SLE/SLV q=1,5/SLC, C7.10.8 collaudo)
  - `cap07/7.11-geotecnica.md` — C7.11.1 requisiti SL, C7.11.2 caratterizzazione, C7.11.3 risposta sismica e stabilità (RSL con indagini in sito, analisi numeriche monodim/bi-tridim, scelta accelerogrammi, liquefazione, pendii con metodi pseudostatici/spostamenti/dinamici), C7.11.4 fronti di scavo, C7.11.5 fondazioni (superficiali con γR=2,3 o 1,8, pali, miste), C7.11.6 sostegno (muri con βm, paratie con accelerazione critica)
  - 24 figure estratte e referenziate, 1 tabella estratta come immagine (Tab. C7.3.I)
  - Aggiornati `indice-cap07.md` con sommario Circolare completo e `TODO.md`
- **Stato circolare aggiornato**: 10 capitoli su 11 completati (C1, C2, C3, C5, C6, **C7**, C8, C9, C10, C11). Resta solo **C4** (83 pp., 1 capitolo).

## 2026-04-14

- **Capitolo C8 — Circolare Costruzioni esistenti** (pp. 249-299, 51 pp.): conversione COMPLETA
  - `cap08/8-esistenti.md` — C8.1-C8.8 completo (~1170 righe di circolare)
  - C8.1 oggetto (D.P.C.M. 9/2/2011 beni culturali)
  - C8.2 criteri generali (criticità locali, categorie intervento, collaudo)
  - C8.3 valutazione sicurezza (ζE, ζVi, fondazioni)
  - C8.4 classificazione interventi (C8.4.1 riparazione locale, C8.4.2 miglioramento ζE≥0,6, C8.4.3 adeguamento ζE≥1,0/0,8)
  - C8.5 modello di riferimento: analisi storico-critica, rilievo (muratura/c.a./acciaio/legno, 3 livelli), materiali con Tab. C8.5.I (8 tipologie muratura) e Tab. C8.5.II (coefficienti correttivi consolidamento), LC1-LC3 con FC 1,35/1,2/1,0, formule bayesiane [C8.5.4.1]-[C8.5.4.3], Tab. C8.5.III (κ), Tab. C8.5.IV-VI (rilievo e prove c.a./acciaio)
  - C8.6 materiali (compatibilità, ritiro, incompatibilità chimica)
  - C8.7 progettazione interventi: muratura (meccanismi locali corpo rigido [C8.7.1.1]-[C8.7.1.2], cinematico lineare/non lineare [C8.7.1.3]-[C8.7.1.5], oscillatore equivalente [C8.7.1.6]-[C8.7.1.7], verifiche SLD [C8.7.1.8]-[C8.7.1.9], SLV/SLC [C8.7.1.10]-[C8.7.1.12], pareti murarie [C8.7.1.13]-[C8.7.1.18], edifici in aggregato, semplici), c.a./acciaio (modelli capacità [C8.7.2.1]-[C8.7.2.13], flessione, taglio, nodi), miste, interventi consolidamento muratura (6 categorie) e c.a. (incamiciatura [C8.7.4.1]-[C8.7.4.8], compositi), elementi non strutturali (Tab. C8.7.6.3.I-II rischio gas)
  - C8.8 ponti esistenti (C8.8.1-C8.8.7, metodi analisi [C8.8.5.1]-[C8.8.5.5], fondazioni, classificazione interventi)
  - Aggiornati `indice-cap08.md`, `TODO.md`

## 2026-04-13

- **Capitolo C3 — Circolare Azioni sulle costruzioni** (pp. 41-79): conversione COMPLETA, tutti i 6 file
  - `cap03/3.1-opere-civili.md` — C3.1 opere civili (carichi permanenti non strutturali, sovraccarichi, verticali distribuiti/concentrati, orizzontali lineari)
  - `cap03/3.2-azione-sismica.md` — C3.2 azione sismica (stati limite SLO/SLD/SLV/SLC, Tab. C3.2.I-II, [C3.2.1]-[C3.2.5], Fig. C3.2.1a-c/C3.2.3/C3.2.4 da estrarre, categorie sottosuolo Vs,eq [C.3.2.4], spettro elastico, storie temporali)
  - `cap03/3.3-vento.md` — **C3.3 vento COMPLETATO**: C3.3.1-C3.3.11, coefficienti aerodinamici (C3.3.8.1-C3.3.8.8: edifici rettangolari con pareti/coperture piane/falda singola-doppia/padiglione/falde multiple/volta cilindrica, tettoie singola-doppia-multiple, pianta circolare/cupole sferiche, pressioni interne, travi, torri, attrito), distacco vortici (Strouhal, Scruton), [C3.3.1]-[C3.3.12], Tab. C3.3.I-XIX, 28 figure estratte (Fig. C3.3.1-C3.3.28)
  - `cap03/3.4-neve.md` — C3.4 neve (carico coperture, qsk per zona/altitudine [C.3.4.1], coefficienti forma μ₁/μ₂ Tab. C3.4.I, coperture a più falde/cilindriche/adiacenti Fig. C3.4.2-C3.4.7 da estrarre, effetti locali, sporgenze, neve aggettante [C.3.4.2]-[C.3.4.7], coefficiente termico)
  - `cap03/3.5-temperatura.md` — C3.5 temperatura (solo C3.5.2 temperatura aria esterna: 4 zone, quota, periodi ritorno)
  - `cap03/3.6-azioni-eccezionali.md` — C3.6 azioni eccezionali (C3.6.1 incendio: definizioni, richieste prestazione D.M. 9/3/2007 e D.M. 3/8/2015, classi resistenza al fuoco, criteri progettazione, procedura analisi C3.6.1.5.1-C3.6.1.5.4; C3.6.2 esplosioni)

- **Capitolo C11 — Circolare Materiali e prodotti per uso strutturale** (pp. 310-337): convertita sezione circolare completa su tutti gli 8 file
  - `cap11/11.1-11.2-generalita-calcestruzzo.md` — intro C11, C11.1 generalità (definizioni CPR: fabbricante, norma armonizzata, marcatura CE, ETA, FPC, organismi notificati, NANDO, accettazione in cantiere DL), C11.2 calcestruzzo (C11.2.1-C11.2.8, C11.2.12: specifiche, controlli qualità, valutazione preliminare, prelievo campioni, accettazione tipo A/B, prescrizioni comuni, resistenza in opera con Tab. C11.2.6.I fattore di disturbo, prove complementari, cls industrializzato, FRC)
  - `cap11/11.3.1-11.3.2-acciaio-ca.md` — C11.3.1 prescrizioni comuni (controlli, qualificazione, mantenimento, forniture, CdT), C11.3.2 acciaio c.a. (B450C/B450A, proprietà meccaniche, dimensionali, reti/tralicci UNI EN ISO 17660, zincati, controlli CdT, prove aderenza beam-test, accettazione cantiere)
  - `cap11/11.3.3-11.3.4-acciaio-cap-carpenteria.md` — C11.3.3 acciaio c.a.p. (prove qualificazione, zincati), C11.3.4 carpenteria metallica (generalità, saldatura, bulloni/chiodi, centri trasformazione/produzione con Tab. C11.3.4.11.2.I, accettazione cantiere)
  - `cap11/11.4-11.6-ancoranti-precompressione-appoggi.md` — C11.4 ancoranti (ETAG 001/032), C11.5 precompressione (ETAG 013), C11.6 appoggi strutturali (UNI EN 1337)
  - `cap11/11.7-legno.md` — C11.7 legno (generalità, massiccio rettangolare/irregolare, giunti a dita, lamellare, pannelli, collegamenti sismici, fabbricanti/centri lavorazione, attestati, formazione direttori tecnici, accettazione cantiere)
  - `cap11/11.8-prefabbricati.md` — C11.8 prefabbricati (generalità casi A/B/C, produzione occasionale, a piè d'opera, controllo produzione, qualificazione serie dichiarata/controllata, documenti accompagnamento, dispositivi meccanici collegamento)
  - `cap11/11.9-dispositivi-antisismici.md` — C11.9 dispositivi antisismici (tipologie: vincolo temporaneo/fusibile/provvisorio, lineari, non lineari, viscosi, isolatori elastomerici/scorrimento, procedura accettazione, formule smorzamento/rigidezza, isolatori elastomerici con formule verifica)
  - `cap11/11.10-muratura.md` — C11.10 muratura portante (elementi: prove accettazione, resistenza caratteristica fbk con formula, malte: prove accettazione, parametri meccanici: compressione e taglio sperimentale)
  - Aggiornato `TODO.md` con stato C11 fatto

- **Circolare — avvio conversione**:
  - Mappate le pagine PDF della circolare (337 pp., capitoli C1-C11, C12 non presente)
  - **Capitolo C1 — Introduzione** (pp. 28-34): convertita sezione circolare completa
    - `cap01/1-oggetto.md` — aggiunta sezione Circolare con C1.1 (logica della norma) e C1.2 (organizzazione della norma e della circolare)
    - Aggiornato `indice-cap01.md` con sommario sezioni circolare
    - Aggiornato `TODO.md` con mappa pagine circolare
  - **Capitolo C2 — Sicurezza e prestazioni attese** (pp. 35-40): convertita sezione circolare completa
    - `cap02/2-sicurezza.md` — aggiunta sezione Circolare con C2.1-C2.6 (principi fondamentali, robustezza, vita nominale, classi d'uso, periodo di riferimento, azioni, stati limite)
    - Estratta Fig. C2.1 (affidabilità strutturale e vita nominale)
    - Aggiornato `indice-cap02.md` con sommario sezioni circolare
  - **Capitolo C9 — Collaudo statico** (pp. 300-304): convertita sezione circolare completa
    - `cap09/9-collaudo.md` — C9.1 prescrizioni generali (adempimenti tecnici a-i, certificato), C9.2 prove di carico, C9.2.1-C9.2.4 (prefabbricate, ponti stradali, ferroviari, isolamento)
  - **Capitolo C10 — Redazione progetti** (pp. 305-309): convertita sezione circolare completa
    - `cap10/10-redazione.md` — C10.1 caratteristiche generali (relazione calcolo, materiali, elaborati grafici, particolari costruttivi, piano manutenzione, relazioni specialistiche), C10.2 codici di calcolo (C10.2.1 relazione, C10.2.2 valutazione indipendente)
  - **Capitolo C5 — Ponti** (pp. 163-172): convertita sezione circolare completa
    - `cap05/5.1-ponti-stradali.md` — C5.1 ponti stradali: compatibilità idraulica, corsie convenzionali, schemi di carico, carichi su rilevati (Fig. C5.1.1), parapetti, fatica [C5.1.1]-[C5.1.2], deformazione [C5.1.3]-[C5.1.8], sismica, ponti pedonali [C5.1.9] (Fig. C5.1.2)
    - `cap05/5.2-ponti-ferroviari.md` — C5.2 ponti ferroviari: temperatura, interazione treno-binario-struttura (Fig. C5.2.1-C5.2.3), sismica, verifiche SLU/fatica
    - Estratte 5 figure: C5.1.1, C5.1.2, C5.2.1, C5.2.2, C5.2.3
  - **Capitolo C6 — Progettazione geotecnica** (pp. 173-192): convertita sezione circolare completa su tutti i 5 file
    - `cap06/6.1-6.2-disposizioni-articolazione.md` — C6.2 articolazione del progetto (C6.2.1-C6.2.5: modellazione geologica e geotecnica, indagini in sito Tab. C6.2.I, laboratorio, parametri caratteristici, relazione geotecnica, fasi costruttive, verifiche SLU/SLE con EQU/STR/GEO/UPL/HYD, Approcci 1 e 2)
    - `cap06/6.3-pendii.md` — C6.3 stabilità pendii naturali (C6.3.1-C6.3.6: prescrizioni, modellazione geologica e geotecnica, verifiche di sicurezza, interventi di stabilizzazione, controlli e monitoraggio)
    - `cap06/6.4-fondazioni.md` — C6.4 opere di fondazione (C6.4.1-C6.4.3: criteri generali, superficiali SLU/SLE, pali SLU + prove di carico)
    - `cap06/6.5-6.6-sostegno-tiranti.md` — C6.5 opere di sostegno (muri SLU Approccio 2, paratie SLU Approccio 1, SLE); C6.6 tiranti (criteri, verifiche sfilamento/rottura, aspetti costruttivi)
    - `cap06/6.7-6.12-altre-opere.md` — C6.7 sotterraneo, C6.8 materiali sciolti e fronti di scavo, C6.11 discariche, C6.12 fattibilità grandi aree

- **Revisione indici e qualità testo**:
  - Corretti 7 link rotti in `indice-ntc2018.md` (percorsi cap02 e cap08 nella ricerca rapida)
  - Uniformate heading cap07: aggiunto punto dopo il numero in `7.4-calcestruzzo.md` (30+ heading) e `7.5-acciaio.md` (15+ heading), ora coerenti con tutti gli altri capitoli
  - Corretti tutti i wikilink in `indice-cap07.md` (punti aggiunti agli anchor di tutte le sezioni)
  - Ristrutturato `indice-cap11.md`: aggiunta tabella sezioni, corretti 18+ anchor troncati (11.3, 11.8, 11.9, 11.10)
  - Corretti 134 apostrofi usati come accenti in `11.3.1-11.3.2-acciaio-ca.md` (91) e `11.3.3-11.3.4-acciaio-cap-carpenteria.md` (42+1): qualità, conformità, può, è, ecc.

- **Capitolo 11 — Materiali e prodotti per uso strutturale**: conversione completa della norma in 8 file (62 pp.)
  - `cap11/11.1-11.2-generalita-calcestruzzo.md` — generalità (casi A/B/C, DL, STC), calcestruzzo (specifiche, controlli tipo A/B Tab. 11.2.I, resistenza in opera, cls industrializzato, componenti Tab. 11.2.II-IV, caratteristiche [11.2.1]-[11.2.10] Tab. 11.2.Va-VII, durabilità, FRC)
  - `cap11/11.3.1-11.3.2-acciaio-ca.md` — prescrizioni comuni acciaio (qualificazione, CdT, forniture), acciaio per c.a. (B450C/B450A Tab. 11.3.Ia-Ic, reti/tralicci [11.3.1], saldabilità [11.3.2] Tab. 11.3.II, tolleranze Tab. 11.3.III, controlli [11.3.3]-[11.3.6] Tab. 11.3.IV-VI)
  - `cap11/11.3.3-11.3.4-acciaio-cap-carpenteria.md` — controlli reti/tralicci (§11.3.2.11-12 Tab. 11.3.VII), acciaio per c.a.p. (Tab. 11.3.VIII-XI), acciaio per carpenteria metallica (laminati, saldatura Tab. 11.3.XII, bulloni Tab. 11.3.XIII-XIV, connettori, acciai sismici, controlli)
  - `cap11/11.4-11.6-ancoranti-precompressione-appoggi.md` — ancoranti (ETAG 001), giunti di dilatazione (ETAG 032), precompressione post-tesi (ETAG 013), tiranti geotecnici, appoggi strutturali (UNI EN 1337)
  - `cap11/11.7-legno.md` — proprietà materiali Tab. 11.7.I, [11.7.1]-[11.7.2], massiccio, giunti a dita, lamellare, pannelli, adesivi, collegamenti, durabilità, centri di lavorazione, accettazione cantiere
  - `cap11/11.8-prefabbricati.md` — generalità, stabilimenti, controllo produzione, qualificazione, documenti, dispositivi collegamento
  - `cap11/11.9-dispositivi-antisismici.md` — tipologie, qualificazione, accettazione, lineari [11.9.1]-[11.9.4] Tab. 11.9.I, non lineari [11.9.5]-[11.9.6] Tab. 11.9.II, viscosi [11.9.7]-[11.9.8] Tab. 11.9.III, elastomerici Tab. 11.9.IV, scorrimento [11.9.9], fusibili, vincolo provvisorio
  - `cap11/11.10-muratura.md` — elementi Tab. 11.10.I, [11.10.1]-[11.10.3], malte Tab. 11.10.II-V, parametri meccanici [11.10.4]-[11.10.9] Tab. 11.10.VI-VIII
  - `cap11/indice-cap11.md` con sommario wikilink Obsidian e ricerca rapida per argomento
  - Figure estratte: Fig. 11.9.1, Fig. 11.9.2
- **Capitolo 7 — Figure**: estratte 13 figure dal PDF con PyMuPDF a 3x zoom (~216 DPI)
  - Fig. 7.4.1-7.4.6 (calcestruzzo sismico: travi, pilastri, pareti, momenti, taglio, bordi)
  - Fig. 7.5.1 (tipologie strutturali acciaio)
  - Fig. 7.6.1-7.6.2 (composte: rapporti dimensionali, definizione elementi)
  - Fig. 7.9.1 (ponte obliquo)
  - Fig. 7.11.1a (fusi granulometrici liquefazione), 7.11.2-7.11.3 (coefficienti α e β paratie)
- **NORMA COMPLETA**: tutti i 12 capitoli della norma sono ora convertiti in Markdown, con tutte le figure estratte

## 2026-04-12

- **Capitolo 7 — Progettazione per azioni sismiche**: conversione completa della norma in 8 file (82 pp.)
  - `cap07/7.0-7.2-generalita-criteri.md` — generalità, requisiti SL, regolarità, CD"A"/CD"B", Tab. 7.2.I (γRd), fondazioni, modellazione, [7.2.1]
  - `cap07/7.3-metodi-analisi.md` — fattore q, Tab. 7.3.I-III, CQC, pushover, drift, [7.3.1]-[7.3.15]
  - `cap07/7.4-calcestruzzo.md` — travi, pilastri, nodi, pareti, prefabbricati, dettagli costruttivi CD"A"/"B", [7.4.1]-[7.4.33], 6 figure
  - `cap07/7.5-acciaio.md` — telai, controventi concentrici/eccentrici, γov, Tab. 7.5.I, [7.5.1]-[7.5.26], Fig. 7.5.1
  - `cap07/7.6-7.7-composte-legno.md` — composte acciaio-cls (Tab. 7.6.I-IV, [7.6.1]-[7.6.8]), legno (duttilità, zone dissipative)
  - `cap07/7.8-muratura.md` — ordinaria/armata/confinata, Tab. 7.8.I-II, [7.8.0]-[7.8.10], regole di dettaglio
  - `cap07/7.9-7.10-ponti-isolamento.md` — ponti (q₀, pile, impalcato, [7.9.1]-[7.9.23]), isolamento sismico ([7.10.1]-[7.10.5])
  - `cap07/7.11-geotecnica.md` — liquefazione (Fig. 7.11.1), pendii (Tab. 7.11.I), fondazioni (Tab. 7.11.II), sostegno (Tab. 7.11.III), paratie (Fig. 7.11.2-3), [7.11.1]-[7.11.12]
  - `cap07/indice-cap07.md` con sommario wikilink Obsidian
  - Figure da estrarre dal PDF
- **Capitolo 12 — Riferimenti tecnici**: conversione completa della norma (1 p.)
  - `cap12/12-riferimenti.md` — Eurocodici, norme UNI EN, C.N.R., documenti di comprovata validità
- **Capitolo 10 — Redazione dei progetti strutturali**: conversione completa della norma (4 pp.)
  - `cap10/10-redazione.md` — elaborati di progetto, relazione di calcolo, codici di calcolo automatico, valutazione indipendente
- **Capitolo 9 — Collaudo statico**: conversione completa della norma (4 pp.)
  - `cap09/9-collaudo.md` — prescrizioni generali, prove di carico, strutture prefabbricate, ponti stradali/ferroviari
- **Capitolo 8 — Costruzioni esistenti**: conversione completa della norma (8 pp.)
  - `cap08/8-esistenti.md` — valutazione della sicurezza (ζE, ζVi), classificazione interventi (riparazione locale, miglioramento ζE≥0,6, adeguamento ζE≥1,0), modello di riferimento (analisi storico-critica, rilievo, LC1-LC3, fattori di confidenza), materiali, interventi sismici (muratura, c.a./acciaio, miste)
- **Capitolo 6 — Progettazione geotecnica**: conversione completa della norma in 5 file
  - `cap06/6.1-6.2-disposizioni-articolazione.md` — disposizioni generali, articolazione del progetto, verifiche SLU/SLE (Approcci 1 e 2), formule [6.2.1]-[6.2.7], Tab. 6.2.I-III (coefficienti parziali azioni, parametri geotecnici, sollevamento)
  - `cap06/6.3-pendii.md` — stabilità dei pendii naturali, verifiche di sicurezza, interventi di stabilizzazione
  - `cap06/6.4-fondazioni.md` — fondazioni superficiali (Tab. 6.4.I), fondazioni su pali (Tab. 6.4.II-VI, formule [6.4.1]-[6.4.5], fattori ξ), fondazioni miste, prove di carico
  - `cap06/6.5-6.6-sostegno-tiranti.md` — muri di sostegno (Tab. 6.5.I), paratie, tiranti di ancoraggio (Tab. 6.6.I-III, formule [6.6.1]-[6.6.2])
  - `cap06/6.7-6.12-altre-opere.md` — opere in sotterraneo, materiali sciolti e fronti di scavo (Tab. 6.8.I), miglioramento e rinforzo terreni, consolidamento opere esistenti, discariche e depositi inerti, fattibilità opere su grandi aree
  - `cap06/indice-cap06.md` con sommario wikilink Obsidian
  - Nessuna figura in questo capitolo
- **Capitolo 5 — Ponti**: conversione completa della norma in 2 file
  - `cap05/5.1-ponti-stradali.md` — prescrizioni generali (altezza libera, compatibilità idraulica), azioni (Schemi di Carico 1-6, frenamento, centrifuga, vento, urto), combinazioni di carico (Tab. 5.1.IV-VI), verifiche (SLU, SLE, fatica modelli 1-4), strutture portanti, vincoli, opere accessorie, formule [5.1.1]-[5.1.4], Tab. 5.1.I-X, 6 figure
  - `cap05/5.2-ponti-ferroviari.md` — modelli di carico LM 71 (α=1,1), SW/0, SW/2, treno scarico, effetti dinamici (Φ₂, Φ₃, Tab. 5.2.II LΦ), azioni orizzontali (centrifuga, serpeggio, frenatura/avviamento), effetti aerodinamici, interazione treno-binario-struttura, azioni eccezionali (deragliamento, rottura catenaria), verifiche SLU/SLE, formule [5.2.1]-[5.2.11], Tab. 5.2.I-VIII, 14 figure
  - `cap05/indice-cap05.md` con sommario wikilink Obsidian
  - Aggiornato indice generale con sezione Ponti nella ricerca rapida
- **Capitolo 4.6 — Altri sistemi costruttivi**: conversione completa della norma
  - `cap04/4.6-altri-sistemi.md` — dichiarazione idoneità, art. 52 D.P.R. 380/01
- **Capitolo 4.5 — Costruzioni di muratura**: conversione completa della norma
  - `cap04/4.5-muratura.md` — definizioni, materiali (Tab. 4.5.Ia-Ib classificazione laterizio/cls), murature (singolo/doppio paramento, pietra squadrata/listata), caratteristiche meccaniche (fk, fvk0, E, G), organizzazione strutturale (comportamento scatolare, cordoli, spessori minimi), snellezza λ [4.5.1], verifiche (fd [4.5.2]-[4.5.3], Tab. 4.5.II γM, Φ Tab. 4.5.III, eccentricità [4.5.4]-[4.5.11], Tab. 4.5.IV ρ, semplificate [4.5.12]), muratura armata, confinata
  - Aggiornato `cap04/indice-cap04.md` con sommario §4.5 e §4.6
  - Capitolo 4 completato (tutte le sezioni 4.1-4.6 convertite)
- **Capitolo 4.4 — Costruzioni di legno**: conversione completa della norma
  - `cap04/4.4-legno.md` — classi durata carico, classi servizio, resistenza di progetto (kmod, γM), verifiche SLU (trazione, compressione, flessione, taglio, torsione, stabilità), SLE (deformazioni kdef), collegamenti, sistemi strutturali, formule [4.4.1]-[4.4.16], Tab. 4.4.I-V
  - Estratta 1 figura: Fig. 4.4.1
- **Capitolo 4.3 — Costruzioni composte acciaio-calcestruzzo**: conversione completa della norma
  - `cap04/4.3-composte.md` — travi composte (flessione, taglio, connettori piolo), colonne composte (4 tipologie, stabilità, confinamento, interazione N-M), solette con lamiera grecata, formule [4.3.1]-[4.3.38], Tab. 4.3.I-III
  - Estratte 13 figure: Fig. 4.3.1-4.3.12
  - Aggiornato `cap04/indice-cap04.md` con sommario §4.3
- **Capitolo 4.2 — Costruzioni di acciaio**: conversione completa della norma
  - `cap04/4.2-acciaio.md` — materiali (Tab. 4.2.I-II), classificazione sezioni (classi 1-4), verifiche SLU (trazione, compressione, flessione, taglio, torsione, interazione, stabilità), fatica, fragilità, verifiche SLE (deformabilità, vibrazioni), unioni (bulloni, perni, saldature), formule [4.2.0]-[4.2.85], Tab. 4.2.I-XIX
  - Estratte 11 figure/tabelle grafiche: Tab. 4.2.III-V, VIII, X, Fig. 4.2.3-7
  - Aggiornato `cap04/index.md` con ricerca rapida per acciaio
- **Capitolo 3 — Azioni sulle costruzioni**: conversione completa della norma in 6 file
  - `cap03/3.1-opere-civili.md` — pesi propri (Tab. 3.1.I), sovraccarichi (Tab. 3.1.II), formule [3.1.1]-[3.1.2]
  - `cap03/3.2-azione-sismica.md` — stati limite, sottosuolo, spettri, formule [3.2.0]-[3.2.16], Tab. 3.2.I-VII
  - `cap03/3.3-vento.md` — velocità, pressione, esposizione, formule [3.3.1]-[3.3.7], Tab. 3.3.I-III
  - `cap03/3.4-neve.md` — carico neve, zone I-III, formule [3.4.1]-[3.4.5], Tab. 3.4.I-II
  - `cap03/3.5-temperatura.md` — zone, Tmin/Tmax, formule [3.5.1]-[3.5.8], Tab. 3.5.I-III
  - `cap03/3.6-azioni-eccezionali.md` — incendio, esplosioni, urti, formule [3.6.1]-[3.6.9], Tab. 3.5.IV, 3.6.I-III
  - `cap03/index.md` — indice sezioni e ricerca rapida per argomento
  - Estratte 8 figure: Fig. 3.3.1-3.3.3, Fig. 3.4.1-3.4.3, Fig. 3.5.1-3.5.2
- Impostata la skill generale `conversione-normativa` per governare anche NTC 2018 (la vecchia skill dedicata `conversione-ntc2018` è stata poi dismessa)
- Creati README.md e CHANGELOG.md
- Creato `index.md` generale con indice capitoli e ricerca rapida per argomento
- Creato `cap04/index.md` con indice sezioni e ricerca rapida
- Definita struttura: norma + circolare nello stesso file, soglia 15 pagine per file/cartella
- Aggiunta navigazione (link indice) e placeholder circolare nel file 4.1
- Creata pagina progetto su Notion (frm-ntc2018)

## 2026-04-11

- Capitolo 1 (Oggetto): convertito in `cap01-oggetto.md` — solo norma
- Capitolo 2 (Sicurezza e prestazioni attese): convertito in `cap02-sicurezza.md` — solo norma, include tutte le tabelle (2.4.I, 2.4.II, 2.5.I, 2.6.I) e formule di combinazione
- Capitolo 4.1 (Costruzioni di calcestruzzo): convertito in `cap04/4.1-calcestruzzo.md` — solo norma, ~1300 righe, 50 formule numerate [4.1.1]-[4.1.50], tutte le tabelle (4.1.I-IV)
- Estratte 4 figure dal PDF per il §4.1:
  - Fig. 4.1.1 — Modelli σ-ε calcestruzzo
  - Fig. 4.1.2 — Modelli σ-ε calcestruzzo confinato
  - Fig. 4.1.3 — Modelli σ-ε acciaio
  - Fig. 4.1.4 — Sezione pressoinflessa
- Mappati tutti i capitoli con pagine PDF di inizio/fine
