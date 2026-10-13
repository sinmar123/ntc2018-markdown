# Verbale VC: identificativi di blocco nei §§ 3.3.1, 3.3.2, 3.3.7 e 3.3.8

Data di chiusura: 2026-10-13. Firma: CC cloud (CCC). Procedura VC-NTC/7, SHA-256 `01c7f0ed9908e4c7620189a0073b2892afe37aa499f99cf50329a84b43960e67`; catalogo SHA-256 `dd5f1b9980e6fd37bd0444277d8b69d6ac0c000b91c1cf659a4f9a398b4a7c43`, copie congelate nel dossier.

**Esito: VC-OK** sui quattro file, con snapshot aggregato SHA-256 `f4d7fcba65ad3f529049634e1b7427b966c9de6dd6b55565a46638a63b8c0d67` ([snapshot finale](vc-ntc2018-3.3-ancore-blocco-2026-10-13/snapshot-finale.json)):

| File | SHA-256 dopo |
|---|---|
| `cap03/3.3.1-vento-velocita-base-di-riferimento.md` | `95707ad1af99746f202c222261849a132a8c20ef3ceb2afa16f442f0fe992eec` |
| `cap03/3.3.2-vento-velocita-di-riferimento.md` | `f23a6d08fbdd908918a60541830beb7ca7e9fff0e8a2161482af4431bc58e5e7` |
| `cap03/3.3.7-vento-coefficiente-di-esposizione.md` | `f9d02b31c5d17ead1d33f19db4c4235f01623a0f69f9bbf0e1dae3b644f28b4a` |
| `cap03/3.3.8-vento-coefficienti-aerodinamici.md` | `371cb9a92fe158af5179b9ca1718d0bffe9bba21ec719ce0aa561d96816a90c5` |

## Perimetro

Correzione localizzata del § 8 della procedura su quattro paragrafi già `VC-OK`, riaperti con `prendi` e `riapertura_vc_ok` su decisione di Sandro del 2026-10-13. Lista di 9 righe approvata da Sandro («ok vai»): tolti gli identificativi di blocco `^formula-3-3-1`, `^formula-3-3-2`, `^fig-3-3-2`, `^tab-c3-3-i`, `^tab-c3-3-ii`, `^tab-c3-3-iv`, `^tab-c3-3-vii`, `^tab-c3-3-xi`, `^tab-c3-3-xvii`, nati per l'editor di note non più usato. Sono apparato di navigazione (catalogo, voce 11), non testo della fonte. Nessun testo normativo cambia.

Elementi in fonte: formula [3.3.1] NTC p. fisica 56; formula [3.3.2] NTC p. 57; didascalia della Fig. 3.3.2 NTC p. 59 (la lista indicava p. 58, dove c'è solo il richiamo nel testo; rettificato da V); Tabelle C3.3.I e C3.3.II Circolare p. 56, C3.3.IV p. 58, C3.3.VII p. 61, C3.3.XI p. 63, C3.3.XVII p. 70. Fonti congelate: NTC `dda1e397d56d71aa0f5bc457c3ba9b77064a468699dfc37bd056ac6c47105a46`, Circolare `f7c3b8d1f443aadb6b3e020b6b6c19813683492ecaadd2c15bf6bf1939aaed7c`.

## Gate

- **G0:** quattro file, nove righe, sola navigazione. Snapshot iniziale `4f7af5dc8ac2b5da210a8ed8ab831e26bba887599fa6763b7bb153154caaafe1`, uguale agli snapshot dei verbali VC-OK del 2026-08-31 (3.3.1, 3.3.2, 3.3.7) e del 2026-09-03 (3.3.8).
- **G1:** ricognizione piena alla data **2026-10-13**, perché quella del 2026-09-09 superava i trenta giorni. Schede ufficiali del D.M. 17/01/2018 e della Circolare n. 7/2019 sulla Gazzetta Ufficiale identiche a quelle del 2026-09-12, senza rettifiche; unico atto modificativo il D.M. 9 marzo 2023, che riguarda l'art. 2 e i punti 11.4.2 e 11.5.2, non il § 3.3. Normattiva non restituisce la scheda del decreto ministeriale: la vigenza si basa sulla Gazzetta. [Ricognizione](vc-ntc2018-3.3-ancore-blocco-2026-10-13/g1/ricognizione-20261013.json).
- **G2-G4:** il testo normativo non cambia; il confronto meccanico del diff con la lista dà 9 righe conformi e zero estranee.
- **G5:** resa prima e dopo con `strumenti/render-capitolo.py` (pandoc 3.9, XeLaTeX TeX Live 2023). Cambiano 5 pagine: 3.3.1 pp. 1-2, 3.3.2 p. 1, 3.3.8 pp. 9-10. La vecchia regola di resa che toglieva il marcatore assorbiva anche la riga vuota seguente: ora l'elenco dopo la formula [3.3.1] è un elenco vero e il sottotitolo «Direzione del vento Θ = 0°» si separa dal titolo della Tabella C3.3.VII. Il contenuto stampato non cambia; il 3.3.7 è identico pagina per pagina. Il § 3.3.8 in questo ambiente si rende solo con una resa ausiliaria (indice interno a cinque livelli di elenco, oltre il limite LaTeX), prima e dopo. [Confronto](vc-ntc2018-3.3-ancore-blocco-2026-10-13/resa/confronto-resa.json).
- **G6:** resta valido il G6 integrale originario di ciascun file; questo scope ha il solo controllo delle modifiche di V, esito OK su R01-R09, zero residui. [Attestazione](vc-ntc2018-3.3-ancore-blocco-2026-10-13/attestazione-v-modifiche.json).
- **G7:** OK, emesso da V nello stesso contesto del controllo delle modifiche. [G7](vc-ntc2018-3.3-ancore-blocco-2026-10-13/G7.json), SHA-256 `debadae33eb3d61d516960ad3b9908a3ef749088e2a5f0c972118e139edeccbe`.

Manifest di rilascio: 39 file, SHA-256 `615db2bf3490bd24085219759708a821d367ffaf7c99e93c71e9f5c238a3458b` ([manifest](vc-ntc2018-3.3-ancore-blocco-2026-10-13/manifest-rilascio.json)).

## Esecutori e limiti

C: la sessione cloud CC cloud (Opus). V: subagente a contesto nuovo, Opus, isolamento istruttivo nello stesso ambiente. Nessun E: le sostituzioni le ha applicate uno script. Controlli eseguiti da agenti AI, senza revisione umana integrale; Sandro ha approvato la lista. Consumi: non disponibili. La resa dei viewer diversi dal renderer canonico è quella dichiarata nel catalogo.

VC-OK vale per questo snapshot e perimetro, senza sostituire la fonte ufficiale.

Prossima azione: Nessuna sul file: VC conclusa sullo snapshot registrato.
