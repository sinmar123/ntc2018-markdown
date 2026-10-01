---
scope_id: ntc2018-3.1.4
atti:
  - "D.M. 17/01/2018, § 3.1.4 Sovraccarichi e §§ 3.1.4.1-3.1.4.3"
  - "Circolare 21/01/2019 n. 7, § C3.1.4 e §§ C3.1.4.1-C3.1.4.3"
file_markdown: cap03/3.1.4-opere-civili-sovraccarichi.md
fonte_ntc: {pdf: verifica-conformita/fonte-ufficiale/GU-2018-42-SO8-DM-17-01-2018.pdf, pagine_fisiche: 47-49}
fonte_circolare: {pdf: verifica-conformita/fonte-ufficiale/GU-2019-35-SO5-Circolare-7-2019.pdf, pagine_fisiche: 46}
unita_registro: 1
formule_numerate: 2
tabelle: 1
figure: 0
pagine_fonte: 4
stato: VC-OK
agente: CDX
macchina: W520
presa_in_carico: 2026-08-27T16:18:04+02:00
giro_g6: 3
max_giri: 3
rilievi_aperti: 0
rilievi_persistenti: 0
gate: {G0: OK, G1: OK, G2: OK, G3: OK, G4: OK, G5: OK, G6: OK, G7: OK}
snapshot_sha256: 776028cc5077b37cd3599398642a20774cc72e72161a64a1a0e643e60c3c6e3f
attesa_decisione: []
prossimo_passo: "nella nuova sessione aprire il 3.2.1 e proseguire uno scope alla volta fino al 3.2.4, già tutti autorizzati da Sandro; non aprire il 3.3"
routing_effettivo:
  p0d: {modello: "script locali + gpt-5.6-luna/medium", compito: "hash, confini, inventario, collazione, render e candidati", esito: "G0-G5 OK dopo adjudicazione dei residui"}
  p0s: {modello: "non previsto", motivo: "materiali predisponibili deterministicamente", esito: "non necessario salvo impedimenti"}
  p1: {modello: "gpt-5.6-sol/high", motivo_escalation: "soli residui testuali o strutturali prodotti da P0-D", esito: "44 ERR-MD adjudicati e corretti; zero residui"}
  p2: {modello: "gpt-5.6-sol/xhigh", gate: "riconciliazione Tab. 3.1.II e formule, G6 e G7", esito: "R01 riclassificato ERR-AUDIT; R02 KO corretto; R03 OK; primo G7 KO formale; secondo G7 OK sul manifest 15/15"}
esecutori:
  apertura: {coordinamento: "CDX/sessione principale", controlli_meccanici: "script locali"}
  preflight: {p0d: "gpt-5.6-luna/medium", g0_g1: "gpt-5.6-sol/high", p1_residui: "gpt-5.6-sol/high"}
  apparati: {passaggio_a: "gpt-5.6-luna/medium", passaggio_b: "gpt-5.6-sol/xhigh", riconciliazione: "gpt-5.6-sol/xhigh"}
---

## 2026-08-27 - apertura dello scope sul file naturale (CDX)

Scope limitato al solo file `cap03/3.1.4-opere-civili-sovraccarichi.md`, ai §§ 3.1.4 e 3.1.4.1-3.1.4.3 del D.M. 17/01/2018 e ai corrispondenti §§ C3.1.4-C3.1.4.3 della Circolare 7/2019. Fonti sulle pagine fisiche NTC 47-49 e Circolare 46.

Precondizioni superate: fonti ufficiali presenti, nessun'altra scheda sul medesimo file e nessun lucchetto concorrente. Snapshot Markdown iniziale SHA-256 `1d10ba6ccaf7fc512ca5b2adc6cbd38ed088953262fbc45f64cfc77ccb3bd19d`.

Dimensionamento preliminare: quattro pagine fonte, Tab. 3.1.II, due formule numerate [3.1.1]-[3.1.2], nessuna figura. Sandro ha autorizzato esplicitamente questo file insieme al precedente § 3.1.3, che è stato chiuso prima dell'apertura del presente scope.

Routing: script e Luna `medium` per il preflight deterministico; Sol `high` per i soli residui motivati; doppio passaggio source-first e riconciliazione Sol `xhigh` per tabella e formule; Sol `xhigh` in contesti freschi per G6 e G7.

## 2026-08-27 - chiusura G0-G5 e congelamento G6 R01 (CDX)

G0-G5 `OK` sul Markdown SHA-256 `3f04e1fdf2d5a434216790b4e2f0708f5f5979b1ffb63a4d84c3e72330a43e73`. Il confronto ha corretto 44 unità `ERR-MD`, 43 puntuali e una riscrittura strutturale della Tab. 3.1.II; il riesame inverso ha ricostruito esattamente lo snapshot iniziale. Tabella e formule sono state verificate source-first in due passaggi indipendenti e riconciliate da P2; residui aperti zero.

Il frammento normativo depurato dagli apparati ha SHA-256 `c654f1dc2f4187ac906e5d8ab0dc12b2caa90c1c2aa7ececdada7a214b848901`. Render ufficiale e verifica globale degli indici interni superati. Congelato il disegno del G6 R01: unico blocco di quattro pagine fonte, coordinatore fresco P2 e due verificatori freschi P2, senza rilievi attesi né audit precedenti.

## 2026-08-27 - G6 R01 KO e correzione separata (CDX)

Il G6 cieco R01 ha coperto integralmente 4 titoli, 14 capoversi, 3 voci di elenco, 21 righe tabellari, 51 celle numeriche, 2 formule e 2 note NTC, oltre a 4 titoli e 9 capoversi della Circolare. Esito: 1 `ERR-MD`, 1 `ERR-AUDIT`, 0 `DUBBIO`, 1 `AF`, 0 `AF-COR`.

L'`ERR-MD` riguardava la prima riga-titolo della Tab. 3.1.II: `Ambienti ad uso residenziale` copre nella fonte le quattro colonne logiche da `Ambienti` a `H_k`, ma era ripetuto soltanto nella prima. La lettura precedente è stata ribaltata con controllo diretto a 600 dpi; applicate tre ripetizioni semantiche ai sensi della voce 6. Nuovo Markdown SHA-256 `4046e6e67d13053afc6d2a1cf7b8a7c59b5e2fa1f3129fa77d928052168d2771`, frammento depurato `ddc73c14594881278c23c869ff8cd1b9b5e4181b6e84be0c025db8e74e9406f9`.

L'`ERR-AUDIT` era la lettura `×` al posto della lettera `x` in cinque occorrenze, già corrette nel Markdown. L'`AF` è l'accordo grammaticale `le componenti [...] possono essere ridotti`, conservato alla lettera. Un nuovo G6 integrale è obbligatorio; G7 resta vietato.

## 2026-08-27 - congelamento G6 R02 (CDX)

Congelato il secondo giro sul Markdown SHA-256 `4046e6e67d13053afc6d2a1cf7b8a7c59b5e2fa1f3129fa77d928052168d2771` e sul frammento normativo SHA-256 `ddc73c14594881278c23c869ff8cd1b9b5e4181b6e84be0c025db8e74e9406f9`. Disegno invariato: unico blocco di quattro pagine fonte, coordinatore fresco P2 e due verificatori freschi P2; nessun rilievo atteso, audit precedente o storia della correzione nel pacchetto.

## 2026-08-27 - G6 R02 KO e seconda correzione separata (CDX)

Il G6 R02 ha coperto nuovamente l'intero scope e ha rilevato una famiglia di 7 `ERR-MD`: le categorie accorpate verticalmente nella colonna `Cat.` non erano ripetute nelle sette righe-titolo. Applicate le sole sette ripetizioni `A`, `B`, `C`, `D`, `E`, `F-G`, `H-I-K`.

La riconciliazione sul ritaglio focalizzato `ntc-p47-tab-a-title-600dpi.png` ha inoltre riclassificato come `ERR-AUDIT` il rilievo R01: `Ambienti ad uso residenziale` resta nella sola colonna `Ambienti`, con le tre celle numeriche vuote. Nuovo Markdown SHA-256 `776028cc5077b37cd3599398642a20774cc72e72161a64a1a0e643e60c3c6e3f`; frammento depurato `924d3b6b55ee31dddd37bf5aa73d9e49ffcdc7c29ce9ebd8db777d7858d6b871`.

Riconosciute due `AF` grammaticali conservate nello stesso capoverso: `tra i quali` e `possono essere ridotti`. Zero dubbi. Il terzo G6 integrale è obbligatorio e coincide con `max_giri`; G7 resta vietato fino a un esito `OK`.

## 2026-08-27 - congelamento G6 R03 (CDX)

Congelato il terzo giro sul Markdown SHA-256 `776028cc5077b37cd3599398642a20774cc72e72161a64a1a0e643e60c3c6e3f` e sul frammento normativo SHA-256 `924d3b6b55ee31dddd37bf5aa73d9e49ffcdc7c29ce9ebd8db777d7858d6b871`. Disegno invariato, pacchetto cieco senza rilievi attesi né materiali R01-R02. Questo è il terzo e ultimo giro ammesso dalla scheda.

## 2026-08-27 - G6 R03 OK (CDX)

Il terzo giro cieco ha ricontrollato integralmente quattro pagine fonte, 8 titoli, 23 capoversi, 3 voci, la Tab. 3.1.II completa, 2 note e 2 formule. Esito: 0 `ERR-MD`, 0 `ERR-AUDIT` aperti, 1 `ERR-AUDIT` chiuso nel giro, 0 `DUBBIO`, 0 `AF-COR`. L'errore chiuso era il punto e virgola letto dall'inventario al posto dei due punti corretti in `massimi prevedibili: tali valori`.

Le due `AF` grammaticali già accertate nel R02 restano registrate e conservate alla lettera; non sono rilievi persistenti. G6 chiuso `OK` al terzo giro con `rilievi_aperti: 0` e `rilievi_persistenti: 0`; il passaggio a G7 è ora consentito.

## 2026-08-27 - primo G7 KO formale e riallineamento contabile (CDX)

Il primo controllo finale P2 ha confermato 15/15 voci del manifest, lo snapshot vivo, il frammento depurato, la catena R01-R03 e tutti i contenuti tecnici. Ha tuttavia bloccato formalmente la promozione perché la scheda conteggiava impropriamente le due `AF` come rilievi persistenti e il rapporto R03 esponeva l'errore d'inventario già risolto come `ERR-AUDIT: 1`, senza specificare che i rilievi aperti erano zero.

La contabilità è stata riallineata senza modificare il Markdown: 2 `AF` conservate, 0 `AF-COR`, 0 `ERR-MD`, 0 `ERR-AUDIT` aperti, 0 `DUBBIO`, `rilievi_aperti: 0`, `rilievi_persistenti: 0`. Poiché il rapporto R03 appartiene al manifest, il manifest deve essere rigenerato e il G7 ripetuto integralmente.

## 2026-08-27 - G7 ripetuto OK e chiusura VC-OK (CDX)

Il precontrollo P0-D `gpt-5.6-luna/medium` e un nuovo controllo finale indipendente P2 `gpt-5.6-sol/xhigh` hanno ricalcolato e confermato 15/15 voci del manifest rigenerato, SHA-256 `990eaef70d2946e806bc704e03ae1c5e1dfa06e3cff1156a0de4149113bc52d7`. Confermati lo snapshot vivo `776028cc5077b37cd3599398642a20774cc72e72161a64a1a0e643e60c3c6e3f`, il frammento depurato `924d3b6b55ee31dddd37bf5aa73d9e49ffcdc7c29ce9ebd8db777d7858d6b871`, 2 `AF`, 0 `AF-COR`, 0 `ERR-MD`, 0 `ERR-AUDIT` aperti, 0 `DUBBIO`, 0 rilievi aperti e 0 persistenti.

Tutti i gate G0-G7 sono `OK`. Lo scope è chiuso `VC-OK al 2026-08-27`, limitatamente allo snapshot e al perimetro dichiarati. Il § 3.1 non contiene altri file naturali: con il 3.1.4 è completo. Sandro ha successivamente autorizzato per la nuova sessione tutti i file 3.2.1-3.2.4, da lavorare uno per volta.
