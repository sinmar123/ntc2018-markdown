# Verbale VC: § 8.4 Classificazione degli interventi, NTC e Circolare

Data di chiusura: 2026-10-14. Firma: CC cloud (CCC), subentrato a NormaNTC18 (OC) su ordine di Sandro del 2026-10-14. Procedura VC-NTC/7, SHA-256 `01c7f0ed9908e4c7620189a0073b2892afe37aa499f99cf50329a84b43960e67`; catalogo SHA-256 `dd5f1b9980e6fd37bd0444277d8b69d6ac0c000b91c1cf659a4f9a398b4a7c43`, copie congelate nel dossier. Lo scope era stato aperto con la revisione 6 e adotta la 7 dal G6 giro 2, primo passaggio non iniziato al subentro.

**Esito proposto: VC-OK** sui quattro file, con snapshot aggregato SHA-256 `70dbe9d6fcc8a18704c4dc50c5d4f87a149a735d872c3fde55b29740363813ec` ([snapshot finale](vc-ntc2018-8.4-2026-10-14/snapshot-finale.json)), subordinato al giudizio G7 di V:

| File | SHA-256 |
|---|---|
| `cap08/8.4-introduzione.md` | `b53479c7bcd437d162bdbb4d8a5e8046a13d50c2309e04709db4396188df774c` |
| `cap08/8.4.1-classificazione-interventi-riparazione-o-intervento-locale.md` | `473952bb57870840e0823fe5cd2f707790d409147c4f715f1d47a1aeb4ef5bf2` |
| `cap08/8.4.2-classificazione-interventi-intervento-di-miglioramento.md` | `c95ac40657e5bb11c96f35ee4e72ff4d5b20f8a2baf3fbf1b463c3b2dcd88497` |
| `cap08/8.4.3-classificazione-interventi-intervento-di-adeguamento.md` | `94a0fdd4299d60e0993ad0e2a549e69ef610522485232cff50bb2a246184346e` |

## Perimetro e atti

- D.M. 17/01/2018, G.U. n. 42 del 20/02/2018, S.O. n. 8, § 8.4 fino a prima di 8.5: pagine fisiche 295-296 della copia congelata, SHA-256 `dda1e397d56d71aa0f5bc457c3ba9b77064a468699dfc37bd056ac6c47105a46`. Scheda ufficiale: https://www.gazzettaufficiale.it/eli/id/2018/02/20/18A00716/sg
- Circolare 21/01/2019 n. 7 C.S.LL.PP., G.U. n. 35 dell'11/02/2019, S.O. n. 5, § C8.4 fino a prima di C8.5, con la nota 2: pagine fisiche 256-257, SHA-256 `f7c3b8d1f443aadb6b3e020b6b6c19813683492ecaadd2c15bf6bf1939aaed7c`. Scheda ufficiale: https://www.gazzettaufficiale.it/eli/id/2019/02/11/19A00855/sg

Righe del registro: 8.4, 8.4.1, 8.4.2, 8.4.3. Nessuna formula esposta, tabella o figura nel perimetro.

## Vigenza

Ricognizione piena del **2026-10-13** ([ricognizione](vc-ntc2018-3.3-ancore-blocco-2026-10-13/g1/ricognizione-20261013.json)) e ricontrollo mirato del **2026-10-14** ([ricontrollo](vc-ntc2018-8.4-2026-10-14/g1/ricontrollo-20261014.json)): schede ufficiali dei tre atti identiche byte per byte; unico atto modificativo noto il D.M. 9 marzo 2023 (art. 2, punti 11.4.2 e 11.5.2), estraneo al § 8.4 e a C8.4. Normattiva non restituisce la scheda del decreto: la vigenza si basa sulla Gazzetta Ufficiale.

## Storia dello scope e gate

- **2026-10-01, NormaNTC18 (OC), VC-NTC/6:** presa in carico; G0-G4 `OK`; correzioni R1-R7 approvate da Sandro «secondo buon senso» (rubriche della Circolare, capoversi, nota 2, grassetti corsivi delle etichette, spazi della fonte), applicate con script. Snapshot iniziale e dopo R1-R7 nella scheda. G5 `OK`. G6 giro 1 `KO` con 7 rilievi: il rapporto stava fuori dal repository e non è recuperabile.
- **2026-10-14, subentro di CC cloud:** i quattro file coincidono con lo snapshot dopo R1-R7. Decisione di Sandro: rifare il G6 integrale come giro 2.
- **G0:** quattro file, perimetro e confini riscontrati sulla codifica dei PDF (rubriche 8.4 e 8.5, C8.4 e C8.5).
- **G1:** come sopra, due date.
- **G2-G4:** confronto del G6 integrale; nessuna formula esposta, tabella o figura; condizioni numeriche (minore dell'unità, 0,6, 0,1, = 1,0, 10 %, 50 %, ≥ 1,0, ≥ 0,80, 0,8) verificate come elementi distinti.
- **G5:** resa canonica con `strumenti/render-capitolo.py` (pandoc 3.9, XeLaTeX) prima e dopo le correzioni: cinque pagine, nessun tag tondo, nessuna didascalia automatica, controllo visivo.
- **G6 giro 2 (integrale):** V a contesto nuovo; inventario fonte-prima di 72 elementi, validato e congelato prima della rivelazione del testo; confronto integrale con tutti i 72 id coperti. Esito `KO`, 5 rilievi, tutti di forma: punto aggiunto alla fine della nota 2 della Circolare; corsivi della fonte omessi in C8.4, C8.4.3 e 8.4.3; grassetto di alcuni segni nella Circolare. [Rapporto](vc-ntc2018-8.4-2026-10-14/g6-r02/b01/rapporto-g6.json).
- **Riscontro di C:** codifica dei PDF e ritagli a 600 dpi ([ritagli](vc-ntc2018-8.4-2026-10-14/c/)) confermano i rilievi; nel § 8.4.3 il punto dopo «a)» è in tondo, diversamente dalla prima lettura di V.
- **Decisione di Sandro** (2026-10-14, «ok vai») e correzioni L1-L4 applicate con script; diff di 4 righe, nessuna estranea ([lista](vc-ntc2018-8.4-2026-10-14/lista-correzioni.json), [diff](vc-ntc2018-8.4-2026-10-14/diff-correzioni.diff)).
- **Controllo delle modifiche (§ 8):** stesso V, esito OK sui 5 rilievi; conferma il punto in tondo dopo «a)». [Attestazione](vc-ntc2018-8.4-2026-10-14/modifiche/attestazione-v-modifiche.json).
- **G7:** primo tentativo `KO` documentale ([G7 r01](vc-ntc2018-8.4-2026-10-14/G7-r01-KO.json)): resa finale fuori dal manifest, scheda non aggiornata, verbale mancante. Rimediati con questo lotto; il giudizio finale è nel file `G7.json` del dossier.

Copertura: il G6 integrale del giro 2 copre tutto il testo dello snapshot precedente alle correzioni L1-L4, comprese le correzioni R1-R7 del 2026-10-01; le quattro righe cambiate dopo il G6 sono coperte dal controllo delle modifiche.

## Normalizzazioni, anomalie e correzioni

- Normalizzazioni del catalogo applicate: voci 1, 2, 3, 4 e 11.
- Anomalie della fonte conservate (A): «0,6 ,» e «≥ 0,80 .» con lo spazio prima del segno nella NTC; «§8.3» e «§8.4.3» senza spazio; «D.M. 14. gennaio 2008»; doppi spazi «di  classe» e «previste  per» nella Circolare; nota 2 senza punto finale.
- Anomalia tipografica della fonte non riprodotta, per decisione di Sandro (D1): nella Circolare, pp. 256-257, alcuni pedici E di ζE, un punto e una virgola sono stampati in grassetto. Non cambia né la grandezza né il segno.
- Correzioni (C) di questo scope: L1 nota 2 senza punto finale; L2 corsivo delle tre categorie in C8.4; L3 corsivo delle lettere b, c, d, e in C8.4.3; L4 corsivo di «a)» nel § 8.4.3.

## Manifest e catena degli hash

Manifest di rilascio: 52 file, SHA-256 `df2412c17c0168ee5fc3d3aca0f8f6e0873a0baff8774b364a7dae0e0db6c4a9` ([manifest](vc-ntc2018-8.4-2026-10-14/manifest-rilascio.json)), con fonti, target, procedura e catalogo congelati, G1, pacchetto e rapporto G6, ritagli, lista, diff, attestazione e resa finale. Il manifest precedente da 40 file, senza resa finale, resta come `manifest-rilascio-r01.json`. G7 e registrazioni chiudono la catena dall'esterno.

## Esecutori e limiti

C: la sessione cloud CC cloud (modello Opus), che non ha scritto le correzioni in modo interpretativo: le ha applicate uno script dalla lista approvata. V: subagente Opus a contesto nuovo, isolamento istruttivo nello stesso ambiente; V dichiara di aver salvato per errore alcuni ritagli di lavoro nella cartella madre del pacchetto, senza aprirne altri file. Nessun E. Controlli eseguiti da agenti AI, senza revisione umana integrale; Sandro ha deciso sui rilievi. Il coordinamento fino al 2026-10-13 è di NormaNTC18 (OC, xai/grok-4.7). Consumi: non disponibili. La resa dei viewer diversi dal renderer canonico è quella dichiarata nel catalogo.

VC-OK vale per questo snapshot e perimetro, senza sostituire la fonte ufficiale.

Prossima azione: Nessuna sul file: VC conclusa sullo snapshot registrato.
