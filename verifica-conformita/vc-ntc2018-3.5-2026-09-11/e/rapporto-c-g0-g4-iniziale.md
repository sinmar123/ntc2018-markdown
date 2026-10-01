# Rapporto C G0-G4 - VC NTC 2018 § 3.5

**Agente:** Hermes NTC-VC, ruolo C (HRM)  
**Runtime:** `gpt-5.6-sol`, provider `openai-codex`, ragionamento `high`  
**Scope:** unico `ntc2018-3.5`, comprendente `3.5-introduzione.md` e i sette file naturali 3.5.1-3.5.7  
**Esclusioni:** § 3.4.5/C3.4.5 già `VC-OK`; § 3.6/C3.6; duplicato storico non indicizzato `cap03/3.5-temperatura.md`.

## G0 - Identità delle fonti

G0 è riusato ai sensi del § 3 di VC-NTC/3 dal dossier del § 3.4.5, chiuso oggi sugli stessi due PDF e già accettato da G7 R06:

- DM 17 gennaio 2018, PDF locale SHA-256 `dda1e397d56d71aa0f5bc457c3ba9b77064a468699dfc37bd056ac6c47105a46`;
- Circolare 21 gennaio 2019 n. 7 C.S.LL.PP., PDF locale SHA-256 `f7c3b8d1f443aadb6b3e020b6b6c19813683492ecaadd2c15bf6bf1939aaed7c`;
- evidenza riusata: `verifica-conformita/vc-ntc2018-3.4.5-2026-09-10/g0-g1/rapporto-c-g0-g1.md`.

La lettura visiva del presente scope usa NTC pp. fisiche 63-66 e Circolare p. fisica 81, rasterizzate a 200 e 600 dpi in `_tmp_render/cap03/vc-3.5-20260910/apertura-r02/`.

**Esito G0:** `OK` per riuso valido.

## G1 - Vigenza e applicabilità

Le pagine ufficiali confermano il DM 17 gennaio 2018 e la Circolare 21 gennaio 2019 n. 7 C.S.LL.PP.[1][2]

Il DM 9 marzo 2023 è stato ricontrollato nel testo completo e nell'articolo unico: l'intervento riguarda il punto 7.4.3.1 e non modifica il § 3.5 né C3.5.[3][4]

**Esito G1:** `OK`; nessuna modifica applicabile allo scope.

## G2-G4 - Confronto coordinatore

Copertura: cinque pagine fisiche, otto formule numerate [3.5.1]-[3.5.8], tre tabelle, due figure, sette paragrafi NTC e due rubriche/capoversi di Circolare. I confini condivisi sono esclusi prima di `3.5` sulla NTC p. 63 e prima di `C3.5` sulla Circolare p. 81; lo scope termina prima di `3.6` e `C3.6`.

Differenze da correggere, cinque gruppi e 15 interventi elementari:

1. **Rubriche NTC, 8 interventi:** `3.5` e `3.5.1`-`3.5.7` devono riprodurre il maiuscolo della fonte.
2. **Rubriche Circolare, 2 interventi:** `C3.5` e `C3.5.2` devono essere maiuscole e senza punto dopo il numero, come la fonte.
3. **Asset, 2 interventi:** mancano `cap03/img/fig-3.5.1-zone-temperatura-mappa.png` e `cap03/img/fig-3.5.2-componenti-temperatura.png`. La prima è vettoriale nella NTC p. 64 e va rasterizzata dalla fonte; la seconda è disponibile come immagine incorporata `ntc-p65-xref1105.png`.
4. **Formula [3.5.6], 1 intervento:** la fonte stampa `0.3`; il target ha `0{,}3`. La normalizzazione n. 4 non è applicabile perché la fonte non usa la virgola.
5. **Testo e formula inline 3.5.4, 2 interventi:** la fonte ha `tener conto`, non `tenere conto`; l'espressione deve essere una formula inline completa, equivalente a `$\Delta T_u = T - T_0$`, e non una formula spezzata fra math e testo.

Le tre tabelle sono complete; ripetizioni delle celle raggruppate, spaziature, trattini e omissione del punto nelle didascalie rientrano nelle normalizzazioni n. 6, 7 e 9. Non sono state rilevate anomalie della fonte di classe A nello scope.

**Esito G2-G4:** `KO` correggibile; passaggio a E necessario.  
**Firma:** Hermes NTC-VC / HRM, 2026-09-10.

## Sources

[1] https://www.gazzettaufficiale.it/eli/id/2018/02/20/18A00716/sg — Gazzetta Ufficiale - DM 17 gennaio 2018
[2] https://www.gazzettaufficiale.it/eli/id/2019/02/11/19A00855/sg — Gazzetta Ufficiale - Circolare 21 gennaio 2019 n. 7 C.S.LL.PP.
[3] https://www.gazzettaufficiale.it/atto/vediMenuHTML?atto.dataPubblicazioneGazzetta=2023-03-22&atto.codiceRedazionale=23A01847&tipoSerie=serie_generale&tipoVigenza=originario — Gazzetta Ufficiale - DM 9 marzo 2023, testo completo
[4] https://www.gazzettaufficiale.it/atto/serie_generale/caricaArticolo?art.versione=1&art.idGruppo=0&art.flagTipoArticolo=0&art.codiceRedazionale=23A01847&art.idArticolo=1&art.idSottoArticolo=1&art.idSottoArticolo1=10&art.dataPubblicazioneGazzetta=2023-03-22&art.progressivo=0 — Gazzetta Ufficiale - DM 9 marzo 2023, articolo unico
