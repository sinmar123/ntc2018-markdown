---
scope_id: ntc2018-4.2-a
atti:
  - "D.M. 17/01/2018, §§ 4.2-4.2.4.1.2.9"
  - "Circolare 21/01/2019 n. 7 C.S.LL.PP., §§ C4.2-C4.2.3.7"
file_markdown: _tmp_render/cap04/ristrutturazione-4.2-20260825/archivio-file-sostituiti/4.2-acciaio.md
struttura_corrente: cap04/indice-4.2.md
validita_corrente: SCADUTA
fonte_ntc: {pdf: verifica-conformita/fonte-ufficiale/GU-2018-42-SO8-DM-17-01-2018.pdf, pagine_fisiche: 95-105}
fonte_circolare: {pdf: verifica-conformita/fonte-ufficiale/GU-2019-35-SO5-Circolare-7-2019.pdf, pagine_fisiche: 100-105}
unita_registro: 37
formule_numerate_preliminari: 61
stato: CHIUSO
agente: CDX
macchina: W520
presa_in_carico: 2026-08-05T19:54:45+02:00
chiusura: 2026-08-06
giro_g6: 5
max_giri: 5
rilievi_aperti: 0
rilievi_persistenti: 0
famiglie_correttive: 0
gate: {G0: OK, G1: OK, G2: OK, G3: OK, G4: OK, G5: OK, G6: OK, G7: OK}
snapshot_sha256: eccefb75094e290c75a9496d4d902bcff9bfecd7542affa566c23c69296e8994
attesa_decisione: []
prossimo_passo: "storico chiuso; per la struttura corrente aprire nuovi scope sui file naturali di livello 3"
autorizzazioni:
  - "2026-08-05 - Sandro autorizza il quarto G6 e l'aumento di max_giri da 3 a 4"
  - "2026-08-05 - Sandro autorizza la fase correttiva delle 11 occorrenze congelate, il quinto G6 e l'aumento di max_giri da 4 a 5"
esecutori:
  g6-3: {blocchi: "cinque rapporti firmati G6-N1/CDX; modello e versione non registrati", consolidamento: "CDX + subagente Codex gpt-5.6-sol/xhigh"}
  g6-4: {inventario: "g6_r04_inventario/gpt-5.6-sol/xhigh", blocchi: "B1 g6_r04_b1; B2 g6_r04_b2_recheck; B3 g6_r04_b3_recheck; B4 g6_r04_b4, tutti gpt-5.6-sol/xhigh", adjudicazione: "g6_r04_adjudicazione/gpt-5.6-sol/xhigh", consolidamento: "g6_r04_consolidamento/gpt-5.6-sol/xhigh", coordinamento: "CDX/P0 deterministico + P2"}
  g6-5: {correzione: "correzione_r05/gpt-5.6-sol/xhigh", revisione_diff: "revisione_diff_r05/gpt-5.6-sol/high", inventario: "g6_r05_inventario/gpt-5.6-sol/xhigh", blocchi: "B1 g6_r05_b1; B2 g6_r05_b2; B3 g6_r05_b3; B4 g6_r05_b4, tutti gpt-5.6-sol/xhigh", adjudicazione: "g6_r05_adjudicazione_phi0/gpt-5.6-sol/xhigh", consolidamento: "g6_r05_consolidamento_finale/gpt-5.6-sol/xhigh", verbale: "g7_r05_verbale/gpt-5.6-sol/xhigh", coordinamento: "CDX/P0 deterministico + P2"}
  g7-revisione-finale: {revisore: "g7_r05_revisione_finale/gpt-5.6-sol/xhigh", esito: "OK", evidenza: "_tmp_render/cap04/vc-paragrafo-4-2a-20260804-r01/g7/03-revisione-finale-p2.md"}
---

## 2026-08-26 - evidenza storica e master autonomo ripristinati (CDX)

È stata corretta una deriva dei registri successiva al rilascio e anteriore alla ricomposizione editoriale. Le 37 unità correnti restano `DA_FARE/NON_VALUTATO`, ma i campi storici rinviano nuovamente al quinto G6 e allo snapshot superato del 2026-08-06. Nel master generale è stato ripristinato il record autonomo `ntc2018--norme-costruzioni--cap04-2a` con stato corrente `VC-SCADUTA al 2026-08-25`. Nessun esito storico è stato trasferito ai file naturali correnti.

## 2026-08-25 - ricomposizione editoriale del § 4.2 (CDX)

Il giudizio `VC-OK al 2026-08-06` resta valido soltanto come esito storico dello snapshot indicato. La ricomposizione editoriale del § 4.2 in file naturali di livello 3 e il ripristino degli asset producono un nuovo insieme documentale: validità corrente `SCADUTA`. Il vecchio file è conservato nell'archivio pre-migrazione e verbale, manifest ed evidenze non sono stati alterati.

## 2026-08-06 - quinto G6 e G7 superati, scope chiuso VC-OK (CDX)

Il quinto G6 integrale ha confermato lo snapshot `eccefb75094e290c75a9496d4d902bcff9bfecd7542affa566c23c69296e8994` su 801/801 righe, 17/17 pagine e 10/10 asset. L'inventario fonte-prima e i quattro blocchi ciechi sono stati eseguiti da contesti P2 separati. Il dubbio descrittivo su `φ₀` nel rapporto B4 è stato risolto mediante ritaglio a 600 dpi, estratto congelato e codepoint: la riga Markdown è `OK` e l'errore materiale storico dell'audit è chiuso. Vettore residuo: `ERR-MD=0`, `ERR-AUDIT=0`, `DUBBIO=0`; G6 `OK`.

G7 ha validato 14/14 file del manifest finale. Sono state promosse esclusivamente le 37 unità di dettaglio e le 37 righe dell'indice appartenenti a 4.2-A; è stato creato e promosso il master autonomo `ntc2018--norme-costruzioni--cap04-2a` a `VC-OK al 2026-08-06`. Le unità `4` e `C4`, gli altri sottoscope 4.2, il Capitolo 4 e il master del corpus restano `VC-DA-FARE`. Verbale, scope formale e manifest sono in `verifica-conformita/`; evidenze finali in `_tmp_render/cap04/vc-paragrafo-4-2a-20260804-r01/g6-r05/` e `g7/`.

## 2026-08-05 - fase correttiva r05 conclusa e verificata (CDX)

Il correttore P2 distinto ha applicato esclusivamente le 11 occorrenze congelate dal quarto G6. Il revisore P1 indipendente ha ricostruito il risultato atteso e confermato tutte le correzioni senza modifiche estranee; le annotazioni `AF-4.2-a-01` - `AF-4.2-a-05` sono rimaste identiche e sono state aggiunte soltanto `AF-4.2-a-06` - `AF-4.2-a-10`. Il nuovo snapshot è `eccefb75094e290c75a9496d4d902bcff9bfecd7542affa566c23c69296e8994`.

I controlli post-correzione hanno confermato 801 righe, 61 formule numerate, 39 heading, 64 righe tabellari e 10 asset presenti. Il render produce 24 pagine senza pagine bianche né tag tondi; il lint del registro chiude con 0 errori e il solo avviso globale atteso su `NTC-4.2`. Sono state riallineate esclusivamente le coordinate delle righe `NTC-4.2.4` e `CIRC-C4.2`, conseguenza necessaria delle intestazioni corrette e della riga redazionale eliminata. Evidenze: `_tmp_render/cap04/vc-paragrafo-4-2a-20260804-r01/correzione/r05/`.

La correzione non assegna G6: il quinto G6 integrale è avviato su pacchetti ciechi con confini tutti diversi dal giro precedente.

## 2026-08-05 - autorizzata la correzione e il quinto G6 (CDX)

Sandro ha autorizzato esplicitamente la fase correttiva delle 11 occorrenze congelate dal quarto G6, il quinto G6 integrale e l'aumento di `max_giri` da 4 a 5. Lo scope torna `IN-CORSO`; il contatore passa a `giro_g6: 5` senza azzeramento. La correzione è affidata a un P2 distinto dal coordinatore e dai verificatori del giro r04. Dopo il nuovo snapshot saranno eseguiti diff vincolato ai rilievi, render e controlli automatici; il quinto G6 sarà nuovamente integrale, con contesti freschi e confini ridisegnati. G7 resta `DA_FARE` fino a un eventuale esito zero/zero/zero.

## 2026-08-05 - quarto G6 non superato, budget esaurito (CDX)

Il quarto G6 integrale ha controllato lo snapshot invariato `8404fcb9e41a73d8ab6af7cd0be02da5e3dc32a3888e2c7a2ad315a0b5927bdd` con inventario fonte-prima e quattro blocchi ciechi P2. Dopo la correzione del confine B2/B3 e la ripetizione dei due blocchi con contesti freschi, la copertura definitiva è 802/802 righe, 17/17 pagine e 10/10 asset. Le due famiglie `ERR-AUDIT` del terzo giro sono chiuse; `rilievi_persistenti=0`.

L'adjudicazione su ritagli a 600 dpi e codepoint ha congelato 11 occorrenze `ERR-MD`, raggruppabili operativamente in 7 famiglie correttive: tre `E’→È`, due difformità nella punteggiatura dei titoli, il pedice `pl.Rd` della [4.2.36], un riferimento redazionale aggiunto, un accento `é→è`, due segni `:` aggiunti e un testo alternativo redazionale. Esito consolidato: `ERR-MD=11`, `ERR-AUDIT=0`, `DUBBIO=0`, quindi G6 `KO`.

Il giro coincide con `max_giri: 4`. Lo scope è sospeso e G7 non è avviato; nessun registro è promosso e il file normativo non è stato modificato. Serve autorizzazione esplicita di Sandro ad alzare `max_giri` a 5 prima della fase correttiva distinta e di un quinto G6 integrale. Evidenze: `_tmp_render/cap04/vc-paragrafo-4-2a-20260804-r01/g6-r04/04-consolidamento-p2.md`, `05-manifest-sha256-g6-r04.txt` e `06-controlli-meccanici-finali.txt`.

Costo operativo previsto per la chiusura: una fase correttiva P2 su 11 siti congelati nel solo `cap04/4.2-acciaio.md`, con aggiornamento delle anomalie di fonte pertinenti e controlli post-correzione; poi un quinto G6 nuovamente integrale su 17 pagine, con inventario fonte-prima, quattro blocchi ciechi, eventuale adjudicazione e consolidamento. Non è sufficiente un controllo limitato alle sole righe corrette.

## 2026-08-05 - autorizzato e avviato il quarto G6 (CDX)

Sandro ha autorizzato esplicitamente il quarto G6 e l'aumento di `max_giri` da 3 a 4. Lo scope torna `IN-CORSO`; il contatore passa a `giro_g6: 4` senza azzeramento. Il nuovo giro sarà integrale sullo snapshot `8404fcb9e41a73d8ab6af7cd0be02da5e3dc32a3888e2c7a2ad315a0b5927bdd`, con inventario fonte-prima in contesto fresco, quattro blocchi da 4/4/4/5 pagine, confini ridisegnati, pacchetti completi e controllo automatico di copertura prima della consegna. G7 resta `DA_FARE` fino all'eventuale convergenza.

## 2026-08-05 - terzo G6 non superato, budget esaurito (CDX)

Il consolidamento coordinato ha rilevato due famiglie persistenti `ERR-AUDIT`: 19 righe normative non hanno un giudizio valido per lacune ai confini dei pacchetti e l'asset della Figura C4.2.2 non è stato confrontato insieme alla propria pagina fonte. Le partizioni r01, r02 e r03 non sono state ridisegnate. Lo snapshot e le fonti sono integri; non risultano `ERR-MD` dimostrati nelle porzioni effettivamente collazionate né `DUBBIO`, ma G6 è `KO`. Con `giro_g6: 3` e `max_giri: 3`, lo scope è sospeso in attesa dell'autorizzazione esplicita di Sandro a un quarto G6 integrale. G7 non è avviato e nessun registro è promosso. Evidenza: `_tmp_render/cap04/vc-paragrafo-4-2a-20260804-r01/g6-r03/00-consolidamento-coordinato.md`.

## 2026-08-04 - primo G6 non superato, fase correttiva avviata (CDX)

Il primo G6 integrale e cieco ha coperto 17/17 pagine con inventario fonte-prima congelato e cinque blocchi in contesti separati. Dopo adjudicazione sulla fonte ufficiale a 600 dpi risultano 17 famiglie `ERR-MD`, pari a 34 siti materiali, zero dubbi residui e due difetti di confezionamento dei pacchetti. Le correzioni sono limitate alle famiglie congelate e affidate a un agente distinto dal coordinatore. G7 non è avviato. Evidenze: `_tmp_render/cap04/vc-paragrafo-4-2a-20260804-r01/g6-r01/04-rapporto-finale-g6-r01.md` e `g6-r01/adjudicazione/00-adjudicazione-consolidata.md`.

## 2026-08-04 - fase correttiva r02 conclusa, secondo G6 da eseguire (CDX)

Applicate esclusivamente le 17 famiglie congelate, incluso il nuovo registro dell'anomalia conservata `AF-4.2-a-05`. Nuovo snapshot: `666f36bf78861f41acc09ea3733524b59431eb26da09a62a7789ddff45be1d4d`. Render riuscito e controllo automatico dei tag superato, 61/61 tag con parentesi quadre. La correzione non chiude G6: restano necessari un secondo G6 integrale e cieco, pacchetti con confini ridisegnati e successiva adjudicazione. Evidenze: `_tmp_render/cap04/vc-paragrafo-4-2a-20260804-r01/correzione/r02/`.

## 2026-08-04 - riallineamento mappature dopo la suddivisione dei file (CDX)

Le sottosezioni rese in precedenza come grassetto sono state convertite meccanicamente in heading Markdown, senza variazioni del testo normativo. Il lint del registro è ora a 0 errori; il solo avviso residuo riguarda la naturale ripetizione del titolo 4.2 nei quattro file. Poiché questa normalizzazione cambia lo snapshot in `1df10fb57a74f090c38cf2dfc85a254fe084a8e4164dee914be101aa74a6d94e`, G0-G6 sono riaperti e vanno rieseguiti sul nuovo hash.

## 2026-08-04 - G0-G5 rieseguiti sullo snapshot riallineato (CDX)

Mappature 37/37 complete nel sottoscope, lint del registro a 0 errori e 1 avviso atteso globale. Render r03 riuscito: 61 formule numerate, 39 heading, 64 righe tabellari e 10 asset d'immagine; nessun tag reso fra parentesi tonde. G0-G5 sono nuovamente `OK` sullo snapshot `1df10fb57a74f090c38cf2dfc85a254fe084a8e4164dee914be101aa74a6d94e`. Il secondo G6 integrale e cieco resta da svolgere. Evidenze: `_tmp_render/cap04/vc-paragrafo-4-2a-20260804-r01/g0-g5-r03/`.

## 2026-08-05 - terzo G6, rapporti di blocco ricevuti, consolidamento da riprendere (CDX)

Sul nuovo snapshot `8404fcb9e41a73d8ab6af7cd0be02da5e3dc32a3888e2c7a2ad315a0b5927bdd`, dopo la correzione distinta dei soli due punti in [4.2.7] e [4.2.40], i cinque blocchi ciechi N-A, N-B, N-C, C-A e C-B hanno restituito `OK`. I rapporti sono in `_tmp_render/cap04/vc-paragrafo-4-2a-20260804-r01/g6-r03/blocchi/`. Manca il consolidamento coordinato con controllo di copertura e l'eventuale adjudicazione finale: G6 resta `DA_FARE`, G7 non è avviato e nessun registro è promosso.

## 2026-08-04 - CDX

G0-G5 superati sullo snapshot corrente: 37/37 unità mappate, 61 formule numerate, 8 tabelle o griglie, 6 figure e 10 asset collegati. Render integrale di 25 pagine, 61/61 tag presenti con parentesi quadre. Evidenze: `_tmp_render/cap04/vc-paragrafo-4-2a-20260804-r01/g0-g5/` e `_tmp_render/cap04/4.2-precondizioni-260804/ricognizione-vigenza-2026-08-04.md`.

## 2026-08-04 - CDX

Scope preso in carico. Fonti ufficiali ricalcolate e integre: NTC `dda1e397d56d71aa0f5bc457c3ba9b77064a468699dfc37bd056ac6c47105a46`; Circolare `f7c3b8d1f443aadb6b3e020b6b6c19813683492ecaadd2c15bf6bf1939aaed7c`. Confini accertati visualmente sulle pagine fisiche condivise. Il file originario § 4.2/C4.2 è stato suddiviso in quattro file autonomi per rispettare i limiti di 40 pagine o 150 formule e mantenere stabili gli hash dei sottoscope chiusi. Evidenze: `_tmp_render/cap04/4.2-precondizioni-260804/`.
