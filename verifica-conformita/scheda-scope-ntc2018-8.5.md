---
scope_id: ntc2018-8.5
stato: IN-CORSO
agente: CCC
macchina: claude.ai/code (sessione cloud)
presa_in_carico: 2026-10-14T14:00:15+00:00
procedura: VC-NTC/7
procedura_sha256: 01c7f0ed9908e4c7620189a0073b2892afe37aa499f99cf50329a84b43960e67
catalogo_sha256: dd5f1b9980e6fd37bd0444277d8b69d6ac0c000b91c1cf659a4f9a398b4a7c43
atti:
  - "D.M. 17/01/2018, § 8.5 DEFINIZIONE DEL MODELLO DI RIFERIMENTO PER LE ANALISI, fino a prima di 8.6"
  - "Circolare 21/01/2019 n. 7 C.S.LL.PP., § C8.5, fino a prima di C8.6"
file_markdown: [cap08/8.5-introduzione.md, cap08/8.5.1-modello-riferimento-analisi-analisi-storico-critica.md, cap08/8.5.2-modello-riferimento-analisi-rilievo.md, cap08/8.5.3-modello-riferimento-analisi-caratterizzazione-meccanica-dei-materiali.md, cap08/8.5.4-modello-riferimento-analisi-livelli-di-conoscenza-e-fattori-di-confidenza.md, cap08/8.5.5-modello-riferimento-analisi-azioni.md]
righe_registro: ["8.5", "8.5.1", "8.5.2", "8.5.3", "8.5.4", "8.5.5"]
snapshot_iniziale: verifica-conformita/vc-ntc2018-8.5-2026-10-14/snapshot-iniziale.json
snapshot_iniziale_sha256: 518675848c7fd227c06191a33a17f81ea070be081a899777a1707fc6a34c785d
snapshot_sha256: da-congelare
giro_g6: 0
max_giri: 3
rilievi_aperti: 0
gate: {G0: OK, G1: OK, G2: OK, G3: OK, G4: OK, G5: OK, G6: DA_FARE, G7: DA_FARE}
attesa_decisione: []
prossimo_passo: "G6 integrale in quattro blocchi, verificatori Opus a contesto nuovo"
routing_effettivo:
  C: {agente: "CC cloud (CCC)", modello: claude-opus-5-5}
  preparazione: "script di strumenti/"
  E: non_attivato
  V: "subagenti Opus a contesto nuovo, uno per blocco G6"
---

# Scheda scope § 8.5

## Presa in carico 2026-10-14, CC cloud (CCC)

Autorizzazione di Sandro del 2026-10-14: «vai con l'8.5», dopo la proposta di un solo scope con G6 in circa quattro blocchi. Perimetro: introduzione 8.5 e §§ 8.5.1-8.5.5, Norma e Circolare fino a prima di 8.6 e C8.6. Le righe 8.5.1-8.5.5 erano `DA-RICONFERMARE` (VC del capitolo 8 del 2026-07-29 sul vecchio file unico, non trasferita ai file attuali); la riga 8.5 era `MAI-FATTA`. Nessuna riga `VC-OK` coinvolta. Procedura VC-NTC/7.

## G0-G4 di C, 2026-10-14

G0: confini riscontrati sulla codifica dei PDF. NTC pp. fisiche 296-297 da «8.5.» fino a prima di «8.6.» (p. 296 contiene in testa la fine dell'8.4, esclusa); Circolare pp. 257-269 da «C8.5» fino a prima di «C8.6» (p. 257 contiene in testa C8.4.3, esclusa). Quindici pagine, al limite del § 2. Composto il testo unico con le sei parti della Norma prima e le sei della Circolare dopo, per tagliare i blocchi G6 a fine pagina: 364 righe depurate. Blocchi previsti: b01 NTC 296-297 e Circolare 257-259 (righe 1-116); b02 Circolare 260-262 (117-200); b03 263-265 (201-236); b04 266-269 (237-364).

G1: riuso della ricognizione del 2026-10-13 con il ricontrollo mirato del 2026-10-14 (`g1/riuso-g1.json`).

G2-G3: confronto parola per parola dell'intero testo con il testo del PDF; i residui sono sillabazioni, pedici, celle accorpate e simboli codificati male, tranne i punti della lista. Parte della Norma senza rilievi.

G4: sei tabelle confrontate cella per cella con le tabelle estratte dal PDF (numeri e parole): C8.5.II, C.8.5.III, C8.5.IV e C8.5.VI numericamente identiche; C8.5.I identica salvo «13 ÷ 16», cella accorpata ripetuta secondo la voce 6 del catalogo; C8.5.V identica salvo gli esponenti di m². Formule [C8.5.4.1]-[C8.5.4.3] riscontrate sulla pagina. Rilievi: testate di C8.5.V e C8.5.VI e corsivo dei titoli delle sei tabelle.

Lista per Sandro: `vc-ntc2018-8.5-2026-10-14/lista-correzioni-c.json`, L1-L14 e D1, con ritagli a 600 dpi in `c/`. Il rilievo L1 cambia un valore: nel C8.5.5.1 la fonte dà q = 1,75 αu/α1, il file 3,0.

## Decisione di Sandro, correzioni e G5, 2026-10-14

Decisione di Sandro sulla lista `lista-correzioni-c.json`: «ok tutto», cioè L1-L14 approvate e, per D1, sottolineatura non riprodotta. Correzioni applicate con script; controllo meccanico: annullando le 14 sostituzioni i tre file cambiati tornano identici a quelli di partenza, quindi nessuna modifica estranea (`diff-correzioni.diff`, `snapshot-prima-dopo.json`). File cambiati: 8.5.3 (due didascalie), 8.5.4 (quattro didascalie, testate di C8.5.V e C8.5.VI, frase ripetuta, «E’»), 8.5.5 (q = 1,75, «in cui», virgola, capoverso).

G5: testo unico ricomposto (370 righe depurate; confini dei blocchi invariati, b04 fino alla riga 370) e reso con `render-capitolo.py`: 20 pagine, nessun tag tondo, nessuna didascalia automatica; controllo visivo delle pagine con le tabelle e con C8.5.5.1. Lo snapshot corrente è quello consegnato al G6.

