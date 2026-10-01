---
scope_id: ntc2018-3.4.3
atti:
  - "D.M. 17/01/2018, § 3.4.3 COEFFICIENTE DI FORMA DELLE COPERTURE"
  - "Circolare 21/01/2019 n. 7 C.S.LL.PP., § C3.4.3 COEFFICIENTE DI FORMA DELLE COPERTURE"
file_markdown: cap03/3.4.3-neve-coefficiente-di-forma-delle-coperture.md
fonte_ntc: {pdf: verifica-conformita/fonte-ufficiale/GU-2018-42-SO8-DM-17-01-2018.pdf, pagine_fisiche: 62-63}
fonte_circolare: {pdf: verifica-conformita/fonte-ufficiale/GU-2019-35-SO5-Circolare-7-2019.pdf, pagine_fisiche: 76-80}
unita_registro: 1
formule_numerate: 6
formule_non_numerate: 10
tabelle: 2
figure: 8
pagine_fonte: 7
stato: CHIUSO
agente: CDX
macchina: W520
presa_in_carico: 2026-09-04T19:47:45+02:00
giro_g6: 1
max_giri: 3
rilievi_aperti: 0
rilievi_persistenti: 0
gate: {G0: OK, G1: OK, G2: OK, G3: OK, G4: OK, G5: OK, G6: OK, G7: OK}
snapshot_sha256: f310e117cbcf8fe1cb0329a1ae5ff8cb21b82c7aa1e018482e2c26d3a250d8c6
attesa_decisione: []
prossimo_passo: "nessuna attività sul file; attendere un nuovo via libera prima di aprire il solo scope 3.4.4 o altri scope"
routing_effettivo:
  p0d: {modello: "script locali; gpt-5.6-luna/medium", compito: "hash, estrazioni, inventari, diff, link, asset e render", esito: "preflight post-correzione R01 OK; zero candidati"}
  p0s: {modello: "non_usato", motivo: "scope coperto da script, Luna e ruoli critici", esito: "non_usato"}
  p1: {modello: "gpt-5.6-sol/high", motivo_escalation: "G0-G1, classificazione e due fasi correttive vincolate", esito: "G0-G3 e G5 OK post-correzione R01"}
  p2: {modello: "gpt-5.6-sol/xhigh", gate: "G4, G6 e G7", esito: "G4 OK post-correzione R01; G6 R01 OK; G7 R02 OK"}
esecutori:
  apertura: {coordinamento: "CDX/sessione principale", controlli_meccanici: "script locali"}
  preflight-p0d: {modello: "gpt-5.6-luna", ragionamento: "medium", esito: "sette pagine, sei formule numerate, due tabelle, otto figure; controlli meccanici eseguiti"}
  g0-g1: {modello: "gpt-5.6-sol", ragionamento: "high", esito: "OK limitatamente allo scope"}
  g2-g3-g5: {modello: "gpt-5.6-sol", ragionamento: "high", esito: "KO; prosa, rubriche, didascalie e asset classificati"}
  g4: {modello: "gpt-5.6-sol", ragionamento: "xhigh", esito: "KO; 6 formule, 10 relazioni non numerate, 20 celle e 8 figure controllate"}
  correzione-p1: {modello: "gpt-5.6-sol", ragionamento: "high", esito: "lista iniziale applicata; otto asset ripristinati e annotazioni AF create"}
  postcorrezione-p2: {modello: "gpt-5.6-sol", ragionamento: "xhigh", esito: "cinque residui individuati e confermati da adjudicazione separata"}
  correzione-r01-p1: {modello: "gpt-5.6-sol", ragionamento: "high", esito: "cinque correzioni congelate applicate; hash target f310e117...d8c6"}
  postcorrezione-r01-p0d: {modello: "gpt-5.6-luna", ragionamento: "medium", esito: "G2-G5 OK; controlli deterministici e render senza candidati"}
  postcorrezione-r01-p2: {modello: "gpt-5.6-sol", ragionamento: "xhigh", esito: "G2-G5 OK; zero ERR-MD, ERR-AUDIT e DUBBIO"}
  g6-r01-fonte-prima: {modello: "gpt-5.6-sol", ragionamento: "xhigh", esito: "primo congelamento respinto prima del confronto; sostitutivo fonte-prima-b valido"}
  g6-r01-blocco-a: {modello: "gpt-5.6-sol", ragionamento: "xhigh", esito: "pacchetto v2 OK; 15/15 input; zero ERR-MD, ERR-AUDIT e DUBBIO"}
  g6-r01-blocco-b: {modello: "gpt-5.6-sol", ragionamento: "xhigh", esito: "pacchetto v2 OK; 15/15 input; zero ERR-MD, ERR-AUDIT e DUBBIO"}
  g6-r01-duplicato-b: {modello: "gpt-5.6-sol", ragionamento: "xhigh", esito: "pacchetto v2 OK; concordanza completa; zero ERR-MD, ERR-AUDIT e DUBBIO"}
  g7-p0d: {modello: "gpt-5.6-luna", ragionamento: "medium", esito: "primo rapporto non valido per hash NTC storico errato; rapporto sostitutivo R01 OK, manifest 328/328"}
  g7-p2: {modello: "gpt-5.6-sol", ragionamento: "xhigh", esito: "primo G7 fermato sul solo ERR-AUDIT; G7 R02 OK dopo rettifica, zero residui"}
disegno_g6:
  congelato_il: 2026-09-04
  coordinatore: "CDX/sessione principale; non autore della trasposizione né delle correzioni"
  inventario_fonte_prima: "P2 fresco gpt-5.6-sol/xhigh; sole pagine fonte e testo estratto ausiliario"
  blocco_A: "NTC pagine fisiche 62-63 e Circolare pagine fisiche 76-77; P2 fresco gpt-5.6-sol/xhigh"
  blocco_B: "Circolare pagine fisiche 78-80; P2 fresco gpt-5.6-sol/xhigh"
  blocco_duplicato: "blocco B, scelto per densità di formule, glifi e figure; secondo P2 fresco gpt-5.6-sol/xhigh"
  nota_diversita: "nessuna seconda famiglia di fornitore esposta dal runtime; la duplicazione resta in contesto indipendente e l'assenza di altra famiglia non blocca il gate"
  metriche: "rilievi emessi, confermati in adjudicazione, intersezione sul duplicato e tasso DUBBIO"
---

## 2026-09-04 - G7 R02 chiuso OK e promozione VC-OK (CDX)

Il primo passaggio G7 è stato fermato per un solo `ERR-AUDIT`: il rapporto P0-D riportava un hash storico errato della fonte NTC. Il rapporto sostitutivo R01 ha ricalcolato correttamente fonti, target, manifest, G6 e render senza modificare lo snapshot. Un P2 fresco ha verificato la rettifica e chiuso G7 R02 `OK`, con manifest 328/328, zero `ERR-MD`, `ERR-AUDIT`, `DUBBIO` e `AF-COR`. Lo scope è promosso a `VC-OK al 2026-09-04` sullo snapshot `f310e117cbcf8fe1cb0329a1ae5ff8cb21b82c7aa1e018482e2c26d3a250d8c6`; il § 3.4.4 non è stato aperto.

## 2026-09-04 - G6 R01 chiuso OK e G7 aperto (CDX)

Il primo congelamento fonte-prima e la prima confezione dei blocchi sono stati respinti prima del confronto, rispettivamente per una didascalia inventariata senza il punto dopo `C` e per la collisione Windows fra `scope.md` e `SCOPE.md`; nessun giro è stato consumato da questi pacchetti privi di target valido. Il congelamento sostitutivo e i pacchetti v2 sono stati poi verificati da contesti freschi. Il blocco A ha coperto NTC 62-63 e Circolare 76-77; il blocco B ha coperto Circolare 78-80; un secondo P2 ha duplicato autonomamente il blocco B. Tutti i 45 input risultano integri. G6 R01 chiude `OK` con zero `ERR-MD`, `ERR-AUDIT`, `DUBBIO` e `AF-COR`; il duplicato ha emesso zero rilievi in entrambi i passaggi. È aperto G7 sullo snapshot `f310e117cbcf8fe1cb0329a1ae5ff8cb21b82c7aa1e018482e2c26d3a250d8c6`.

## 2026-09-04 - preflight post-correzione chiuso e G6 R01 aperto (CDX)

Il primo controllo post-correzione ha trovato cinque famiglie residue: due locuzioni, il verso stretto `b_2 < l_s`, l'identificativo `Figura C.3.4.5` e due `μ₁` invisibili nel render. La regola di non regressione è stata applicata ai due punti che ribaltavano letture precedenti, con raster a 600 dpi, `rawdict` e secondo P2 fresco; non sono rimasti dubbi. Un correttore P1 distinto ha applicato la seconda lista congelata e portato il target all'hash `f310e117cbcf8fe1cb0329a1ae5ff8cb21b82c7aa1e018482e2c26d3a250d8c6`. Il nuovo render ha nove pagine, mostra entrambe le occorrenze `μ₁` e contiene zero `U+FFFF`. Il P0-D e un P2 indipendente hanno poi chiuso G2-G5 `OK` con zero `ERR-MD`, `ERR-AUDIT` e `DUBBIO`. È aperto G6 R01 sul disegno congelato nel frontmatter.

## 2026-09-04 - G0-G5 pre-correzione e lista congelata (CDX)

G0-G1 sono `OK`. Il P0-D ha prodotto tutte le sette pagine a 600 dpi, target canonico, inventari, controlli e render diagnostico; gli otto asset vivi risultavano mancanti. Un P1 distinto ha chiuso G2, G3 e G5 `KO`; un P2 critico ha chiuso G4 `KO` dopo il controllo di sei formule numerate, dieci gruppi non numerati, venti celle logiche e otto figure. La discordanza sul numero dei riferimenti `C3`/`C.3` è stata riesaminata a 600 dpi e nel `rawdict`: le occorrenze da correggere sono quattro. Non restano `DUBBIO`, `ERR-AUDIT` o casi `AF-COR`. La lista autoritativa è congelata in `preflight/lista-correzioni-congelata.md`; G6 non è aperto.

## 2026-09-04 - apertura dello scope naturale (CDX)

Sandro ha autorizzato la VC del solo file 3.4.3. Il registro non contiene altri scope `IN-CORSO` e non esiste un'altra scheda naturale sul medesimo file. Le fonti ufficiali ricalcolano SHA-256 `dda1e397d56d71aa0f5bc457c3ba9b77064a468699dfc37bd056ac6c47105a46` e `f7c3b8d1f443aadb6b3e020b6b6c19813683492ecaadd2c15bf6bf1939aaed7c`. Snapshot iniziale del Markdown `1af91654cee3467e94c876f285e8aaf474102422ec64e2a44e4259e6ccacc014`. Il riscontro diretto dei confini ha corretto la mappatura della Circolare da pagina fisica 76 a 76-80: C3.4.3 termina prima di C3.4.5 a pagina fisica 81; la Circolare non contiene un autonomo C3.4.4. Dimensionamento preliminare: sette pagine fonte, sei formule numerate, due tabelle e otto figure; le formule non numerate e inline sostanziali saranno riconciliate dal preflight. I §§ 3.4.2 e 3.4.4-3.4.5 restano fuori perimetro.
