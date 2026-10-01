---
scope_id: ntc2018-3.2.2
atti:
  - "D.M. 17/01/2018, § 3.2.2 Categorie di sottosuolo e condizioni topografiche"
  - "Circolare 21/01/2019 n. 7, § C3.2.2 Categorie di sottosuolo e condizioni topografiche"
file_markdown: cap03/3.2.2-azione-sismica-categorie-di-sottosuolo-e-condizioni-topografiche.md
fonte_ntc: {pdf: verifica-conformita/fonte-ufficiale/GU-2018-42-SO8-DM-17-01-2018.pdf, pagine_fisiche: 50-51}
fonte_circolare: {pdf: verifica-conformita/fonte-ufficiale/GU-2019-35-SO5-Circolare-7-2019.pdf, pagine_fisiche: 50-51}
unita_registro: 1
formule_numerate: 2
tabelle: 2
figure: 0
pagine_fonte: 4
stato: VC-OK
agente: CDX
macchina: P53
presa_in_carico: 2026-08-28T12:41:03+02:00
giro_g6: 3
max_giri: 3
rilievi_aperti: 0
rilievi_persistenti: 0
gate: {G0: OK, G1: OK, G2: OK, G3: OK, G4: OK, G5: OK, G6: OK, G7: OK}
snapshot_sha256: b0e539d976c230e709bc6af524360fc211ba1dcf41c43229cf476c4951c89556
attesa_decisione: []
prossimo_passo: "aprire il solo scope 3.2.3, già autorizzato"
routing_effettivo:
  p0d: {modello: "script locali + gpt-5.6-luna/medium", compito: "hash, confini, inventario, collazione, formule, tabelle, render, link e candidati", esito: "G0-G5 OK"}
  p0s: {modello: "non_usato", motivo: "materiali predisposti deterministicamente", esito: "non necessario salvo impedimenti"}
  p1: {modello: "gpt-5.6-sol/high", motivo_escalation: "residui protetti prodotti da P0-D", esito: "23 ERR-MD corretti; 4 AF conservate; zero residui"}
  p2: {modello: "gpt-5.6-sol/xhigh", gate: "apparati critici, G6 e G7", esito: "G7 OK, manifest 18/18 e scope promuovibile"}
esecutori:
  apertura: {coordinamento: "CDX/sessione principale", controlli_meccanici: "script locali"}
  preflight: {p0d: "gpt-5.6-luna/medium", g0_g1: "gpt-5.6-sol/high se necessario", p1_residui: "gpt-5.6-sol/high se necessari"}
  apparati: {passaggio_a: "gpt-5.6-luna/medium", passaggio_b: "gpt-5.6-sol/xhigh", riconciliazione: "gpt-5.6-sol/xhigh"}
---

## 2026-08-28 - apertura dello scope sul file naturale (CDX)

Scope limitato al solo file `cap03/3.2.2-azione-sismica-categorie-di-sottosuolo-e-condizioni-topografiche.md`, al § 3.2.2 del D.M. 17/01/2018 e al § C3.2.2 della Circolare 7/2019. Il controllo diretto delle rubriche ha accertato i confini sulle pagine fisiche NTC 50-51 e Circolare 50-51, con esclusione dei §§ 3.2.1, 3.2.3, C3.2.1 e C3.2.3.

Precondizioni superate: fonti ufficiali presenti, nessun'altra scheda sul medesimo file e precedente scope 3.2.1 chiuso `VC-OK`. Snapshot Markdown iniziale SHA-256 `fd41ee228aa961a024f634e2e1c858f3baa3d6dfdb1fca5d9575feb423c49517`.

Dimensionamento preliminare: quattro pagine fonte, due formule numerate, due tabelle e nessuna figura. Routing semplificato richiesto da Sandro: script e Moon/Luna per tutto il deterministico, Sol soltanto per residui motivati e gate critici. La normalizzazione n. 10 considera equivalenti `-`, `–` e `—` nei separatori delle didascalie.

## 2026-08-28 - G0-G5 chiusi (CDX)

Collazione integrale e apparati chiusi sullo snapshot `5c9f43af55becbefcedeb6b2495ca604f325f7f48c66107bc0d9991820dd5400`: 23 scostamenti corretti e ricontrollati, quattro anomalie della fonte conservate, zero `AF-COR`, zero `ERR-MD`, zero `ERR-AUDIT` e zero `DUBBIO`. Render finale di quattro pagine e 1.754 collegamenti interni verificati. Il renderer è stato corretto per non esporre le ancore davanti ai titoli, senza modificare alcun file normativo già rilasciato.

## 2026-08-28 - G6 R01 KO e correzione certa (CDX)

Il G6 R01 integrale a verificatore singolo, eseguito per deroga autorizzata da Sandro, ha rilevato un solo `ERR-MD`: `e in ipotesi residuali` in luogo della forma fonte `ed in ipotesi residuali`. Il rilievo certo è stato corretto senza altre modifiche. Snapshot successivo alla correzione: `3a026adb77c6ccd32c9cfa834f1143f1549b28ba8b4f2da7b724f9e0a1d56295`. Avviato G6 R02 integrale.

## 2026-08-28 - G6 R02 KO per errore dell'audit (CDX)

R02 ha letto come minuscola la `S` del membro sinistro `$V_{S,eq}$` della formula `[C.3.2.4]`. Il livello testuale nativo del PDF identifica invece il carattere `S` maiuscolo `U+0053`, coincidente con il Markdown e con la verifica focalizzata precedente. Il rilievo è stato riclassificato `ERR-AUDIT`; nessuna modifica è stata apportata allo snapshot. Avviato il terzo e ultimo G6 integrale.

## 2026-08-28 - G6 chiuso per deroga esplicita dopo R03 (CDX)

R03 ha rilevato la virgola omessa dopo `$V_{s,eq}$`; il rilievo certo è stato corretto. Raggiunto il massimo di tre giri, Sandro ha autorizzato il controllo mirato in luogo di un quarto G6 integrale. Il confronto fonte-PDF-Markdown del solo punto ha dato esito `OK`, con zero residui. G6 è pertanto chiuso per deroga dichiarata sullo snapshot `b0e539d976c230e709bc6af524360fc211ba1dcf41c43229cf476c4951c89556`.

## 2026-08-28 - G7 OK e promozione VC-OK (CDX)

Il precontrollo P0-D Moon e il giudizio finale P2 Sol hanno ricalcolato 18/18 hash e 18/18 dimensioni del manifest finale, senza file mancanti o voci estranee. Confermati zero `ERR-MD`, zero `ERR-AUDIT`, zero `DUBBIO`, cinque `AF`, zero `AF-COR` e nessun rilievo aperto o persistente. Lo scope è promosso a `VC-OK` sullo snapshot `b0e539d976c230e709bc6af524360fc211ba1dcf41c43229cf476c4951c89556`. Verbale: `verifica-conformita/verbale-VC-ntc2018-3.2.2-2026-08-28.md`.
