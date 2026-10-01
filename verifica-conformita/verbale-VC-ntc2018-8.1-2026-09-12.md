# Verbale VC del § 8.1, Oggetto

Data di chiusura: 2026-09-12. Firma: GROK, coordinamento grok-4.6/xhigh. Giudizio G7: GROK-V3 / grok-4.6 xhigh, distinto dall'autore delle correzioni.

**Esito: VC-OK**, limitatamente al file [8.1-oggetto.md](../cap08/8.1-oggetto.md), snapshot SHA-256 `80a2c5a3af47c879dda192b43e7a729fd81a9c30fd5a53407cb2a4c08bdd832b`. G0-G7 OK, zero ERR-MD, ERR-AUDIT o DUBBIO residui. Nessuna revisione umana integrale. Il § 8.2 resta fuori perimetro.

## Fonte, perimetro e vigenza

D.M. 17 gennaio 2018, solo § 8.1, pagina fisica 294, dalla rubrica `8.1. OGGETTO` fino a prima di `8.2. CRITERI GENERALI`. Circolare 21 gennaio 2019 n. 7, titolo C8 a p. 253 e testo C8+C8.1 a p. 254, fino a prima di `C8.2`.

Fonti: [scheda GU 18A00716](https://www.gazzettaufficiale.it/eli/id/2018/02/20/18A00716/sg), [scheda GU 19A00855](https://www.gazzettaufficiale.it/eli/id/2019/02/11/19A00855/sg). PDF congelati SHA-256 `dda1e397d56d71aa0f5bc457c3ba9b77064a468699dfc37bd056ac6c47105a46` (NTC) e `f7c3b8d1f443aadb6b3e020b6b6c19813683492ecaadd2c15bf6bf1939aaed7c` (Circolare).

Vigenza: ricognizione 2026-09-09 riusata; ricontrollo mirato 2026-09-11, senza modifiche a 8.1/C8/C8.1. Il D.M. 9 marzo 2023 non tocca il Capitolo 8.

Procedura del confronto: VC-NTC/3, SHA-256 `4bd4440a6f9b204338e97ecf78c9bb74ab0d9e04f7478b9c97c436c62e817c7c`. Chiusura: VC-NTC/4, SHA-256 `9c43358436f1e4f3ba92b16b95872afccf45e6cdb277d365e4fe5ea16f546a96`. Catalogo SHA-256 `d71319206ec54bcac3639dfd0b97c41754fa1062655b2d35c36ee5d6cb3036d6`.

## Gate e copertura

| Gate | Esito | Evidenza |
|---|---|---|
| G0 | OK | Confini 8.1 / C8 / C8.1, 8.2 escluso |
| G1 | OK | Ricognizione 2026-09-09 e ricontrollo 2026-09-11 |
| G2 | OK | Rubriche e capoversi del perimetro presenti |
| G3 | OK | Prosa NTC coincidente; Circolare allineata dopo le correzioni |
| G4 | OK | Zero formule, tabelle, figure |
| G5 | OK | Render canonico di una pagina, corsivi visibili |
| G6 | OK | Integrale R02, 14/14; poi controllo localizzato dei due corsivi, VC-NTC/4 |
| G7 | OK | Manifest 14/14, giudizio V distinto |

Copertura integrale originaria: G6 R02, 14 elementi, pagine ntc:294 circ:253 circ:254. Giro G6: 2/3. Il controllo delle modifiche non è un nuovo giro.

## Correzioni

Prima del G6 R02: ordine e cassa delle rubriche C8/C8.1 e separazione dei capoversi. Dopo R02, elenco a Sandro: due corsivi mancanti in C8.1. Decisione di Sandro: correggere. Applicati `*Le costruzioni esistenti*`, i due virgolettati NTC in corsivo, `*struttura completamente realizzata*`. Diff soltanto su quelle otto asterischi. Conservati `D.M.14` senza spazio e l'assenza di punto dopo `esistenti` nella NTC. Nessuna AF-COR. Normalizzazioni 1 e 2.

Sandro ha deciso sui rilievi; non è una revisione umana integrale del documento.

## Indipendenza

C e correzioni: GROK grok-4.6/xhigh. V G6 R02: GROK-V2. Controllo modifiche e G7: GROK-V3, distinto dall'autore delle correzioni. Isolamento istruttivo, senza sandbox. Consumi: non disponibili.

## Evidenze

- [Manifest](vc-ntc2018-8.1-2026-09-12/manifest-rilascio.json), SHA-256 `1f88b13eefe384615093760d5d3ee2276469f636dd2b93b58885f001ce7574cb`
- [Rapporto G7](vc-ntc2018-8.1-2026-09-12/rapporto-g7.json), SHA-256 `3ef1c9066d06c722df51bd4fd94dabdbe32dfb2862489187849ffd775299c72a`
- [G6 R02](vc-ntc2018-8.1-2026-09-12/rapporto-g6-r02.json), [inventario](vc-ntc2018-8.1-2026-09-12/inventario-g6-r02.json)
- [Attestazione modifiche](vc-ntc2018-8.1-2026-09-12/attestazione-modifiche.json), [diff](vc-ntc2018-8.1-2026-09-12/diff-corsivi.md)
- [Render](vc-ntc2018-8.1-2026-09-12/target-scope.pdf)
- [Scheda](scheda-scope-ntc2018-8.1.md)

Il verbale e il G7 chiudono la catena esternamente al manifest. VC-OK vale per questo snapshot e perimetro, senza sostituire la fonte ufficiale.

Prossima azione: Nessuna sul file: VC conclusa sullo snapshot registrato.
