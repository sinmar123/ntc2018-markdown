---
scope_id: ntc2018-8.6
stato: CHIUSO
agente: CDX
presa_in_carico: 2026-10-16T12:21:07+02:00
procedura: VC-NTC/9
procedura_sha256: 0935df033bd12222a7bbe672d063d57c893e17205c187f689043f0a946b42a34
procedura_copia: vc-ntc2018-8.6-2026-10-16/procedura-congelata-lettura-web.md
catalogo_sha256: add1873d309b44930b8caccf8dd5ed3714926108a106230de35133a8a76e239e
file_markdown: [cap08/8.6-materiali.md]
righe_registro: ["8.6"]
snapshot_sha256: e15023936101ca022e043099b63d5e3f358a80a31bfd0a098a6855fe11eb3fba
giro_g6: 1
max_giri: 3
rilievi_aperti: 0
gate: {G0: OK, G1: OK, G2: OK, G3: OK, G4: OK, G5: OK, G6: OK, G7: OK}
attesa_decisione: []
routing_effettivo:
  C: "Codex (CDX), GPT-6; identificativo specifico del modello non esposto"
  preparazione: "Script locali; nessun modello leggero necessario"
  E: non_attivato
  V: "Profilo richiesto gpt-5.6-sol xhigh; /root/v86, fork_turns none; G6 e G7 conclusi, modello effettivo non esposto"
consumi:
  contesti_V: 1
  giri_G6: 1
  preparazioni_G6: 2
  nota_preparazioni: "Una respinta per percorsi prima di creare il pacchetto; una valida"
  input: non_disponibile
  input_cache: non_disponibile
  output: non_disponibile
  limite: "Il runtime non espone contatori separati affidabili per questo scope; nessuna stima in token o percentuale di quota"

---

# Scheda scope § 8.6

## 2026-10-16 - Integrazione della VC 8.7 e autorizzazione all’unione della PR #17, CDX

Su autorizzazione di Sandro integrato main 27943b3, che comprende la PR #16 sulla sola introduzione 8.7. Risolti i cinque conflitti nei file di governo conservando entrambe le VC. Nel CSV sono stati trasferiti integralmente i record già registrati: 8.6 dal ramo CDX, 8.7 da main, senza una nuova registrazione o modifica dei campi. Target 8.6 identico allo snapshot verificato; target ed evidenze 8.7 identici a main. Confermate le dieci correzioni approvate e l’integrità delle 73 evidenze locali del manifest di pubblicazione. Linter: 379 righe, 13 colonne, 55 VC-OK, zero errori e sette avvisi, compreso quello ereditato dalla riga 8.7. Unione della PR #17 autorizzata da Sandro; esito remoto consultabile nella PR. Firma: CDX. [PR #17](https://github.com/sinmar123/ntc2018-markdown/pull/17).

Prossima azione: Nessuna sul § 8.6: VC conclusa sullo snapshot registrato.

## 2026-10-16 - Pubblicazione della VC del § 8.6, PR #17, CDX

Pubblicata la VC del solo § 8.6/C8.6 nella PR #17. Acquisita la procedura originale r9, sincronizzato main e risolti i tre conflitti dei file di governo con approvazione di Sandro. Target invariato, dieci correzioni conformi alla lista; G7 integrativo OK, 73/73 evidenze locali integre. Linter CSV: zero errori, sei avvisi fuori dal perimetro. I 14 binari di prova restano locali secondo .gitignore. Firma: CDX. [PR #17](https://github.com/sinmar123/ntc2018-markdown/pull/17), [addendum](vc-ntc2018-8.6-2026-10-16/addendum-pubblicazione.md).

Prossima azione: Revisione e unione della PR #17; nessuna nuova correzione del § 8.6 richiesta.

## 2026-10-16 - Chiusura documentale locale, CDX

Giudizio G7 positivo recepito nel CSV mediante vc-supporto.py registra. VC locale del solo § 8.6/C8.6, 2026-10-16, CDX. Dieci correzioni approvate da Sandro, applicate via script e riscontrate sulla fonte; G6 integrale indipendente, 23 ID, zero rilievi; G7 documentale OK. [Verbale](verbale-VC-ntc2018-8.6-2026-10-16.md). Pubblicazione remota pendente per indisponibilità Git HTTPS; acquisizione originale r9 e sincronizzazione da completare. Firma: CDX.

Prossima azione: Nessuna sul file: VC conclusa sullo snapshot registrato. Prima della pubblicazione acquisire la procedura originale r9, sincronizzare Git e aprire la pull request.

## 2026-10-16 - G6 integrale concluso, CDX

V ha confrontato integralmente i 23 ID del proprio inventario contro le pagine fonte, Markdown e PDF finale: esito OK, zero rilievi. Rapporto originale conservato in `vc-ntc2018-8.6-2026-10-16/g6/b01/rapporto-g6.json`; validazione dello schema OK. Un solo contesto V e un solo giro integrale, nessuna correzione successiva al G6. Letture dichiarate limitate al blocco; isolamento istruttivo. Profilo richiesto `gpt-5.6-sol`, `xhigh`; il runtime V non espone un identificativo effettivo verificabile, come precisato nel rapporto. La firma generica GPT-5 dell’inventario non attesta la variante effettiva.

Prossima azione: G7 documentale nello stesso contesto V; poi registrazione locale se positivo. Pubblicazione remota subordinata ai riscontri indicati nel dossier.

## 2026-10-16 - Correzioni approvate e applicate, CDX

Sandro ha approvato la lista L01-L10 con «ok vai». Applicata con lo strumento comune; `verifica-lista` sulla base Git iniziale ha dato OK, un solo file e nessuna modifica estranea. Punti corretti riscontrati sui ritagli ufficiali a 600 dpi. Decisione e impronte in [decisione-applicazione](vc-ntc2018-8.6-2026-10-16/decisione-applicazione-20261016.json). Nessun E interpretativo necessario. Indici interni verificati e collegamenti del target validi.

G5 OK: PDF canonico finale prodotto e osservato integralmente; configurazione e dati MiKTeX temporanei nel workspace. I timeout del processo di controllo e il completamento successivo dei figli sono documentati in g5/esito-resa.json. Nessuna modifica all’installazione condivisa. Un primo config G6 respinto prima della creazione della destinazione; percorsi corretti, nessun giro consumato. V avviato sulla sola fonte in un contesto nuovo, con restrizione istruttiva alle cartelle consegnate; nessuna sandbox di lettura dichiarata.

Prossima azione: Completare G5 e avviare il solo blocco G6; sincronizzazione remota e PR restano da completare.

## 2026-10-16 - Presa locale e confronto completo, CDX

Autorizzazione di Sandro: «fai 8.6». Solo `cap08/8.6-materiali.md`, da 8.6 a prima di 8.7 nelle NTC (p. fisica 297) e da C8.6 a prima di C8.7 nella Circolare (p. fisica 269). Un solo blocco G6 previsto. Esclusi tutti gli altri paragrafi delle pagine condivise.

Ramo `cdx/vc-8.6-261016`, worktree separata. Presa nel CSV di questo ramo soltanto: nessun lucchetto pubblicato su GitHub, perché il collegamento Git HTTPS non è disponibile. Base locale `2f9fb3a`. Testo remoto consultato tramite lettore web; identità byte per byte con main non attestata. Prima del rilascio sincronizzare e ricontrollare il perimetro se sono intervenute modifiche.

Adottata VC-NTC/9 letta integralmente da GitHub; copia testuale e limite di acquisizione in [provenienza](vc-ntc2018-8.6-2026-10-16/provenienza-procedura.json). Catalogo congelato identico alla copia locale.

Confronto completo di C: Norma conforme; Circolare, una rubrica, otto confini di capoverso e la grafia E’/È. Nove capoversi fonte contro uno nel target. Lo script ha trovato sette degli otto confini: quello prima di E’ è stato recuperato dal controllo visivo. Nessuna formula, tabella o figura nello scope; richiami 8.5.3, 8.6, C.8.5.I e Capitolo 12 riscontrati. Prove a 600 dpi e codifica PDF nel dossier. Target invariato. Lista unica [L01-L10](vc-ntc2018-8.6-2026-10-16/lista-correzioni-c.md).

G1: riuso della ricognizione del 2026-10-13 e ricontrollo web del 2026-10-16; applicabilità e limiti nel dossier G1. G5-G7 non avviati. G3 resta KO fino alla decisione e all'applicazione delle correzioni approvate.

Prossima azione: Decisione di Sandro sulla lista L01-L10; poi correzioni approvate e un blocco G6. Prima del rilascio sincronizzare Git e aprire la pull request.
