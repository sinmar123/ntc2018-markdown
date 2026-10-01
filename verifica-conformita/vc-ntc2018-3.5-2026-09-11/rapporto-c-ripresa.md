# Rapporto C di ripresa G0-G5 - VC NTC 2018 § 3.5

**Data:** 2026-09-11  
**Scope:** unico `ntc2018-3.5`, otto Markdown e due asset  
**Ruolo:** C, `gpt-5.6-sol`, provider `openai-codex`, ragionamento `high`  
**Metodo:** VC-NTC/3, SHA-256 `4bd4440a6f9b204338e97ecf78c9bb74ab0d9e04f7478b9c97c436c62e817c7c`; catalogo SHA-256 `d71319206ec54bcac3639dfd0b97c41754fa1062655b2d35c36ee5d6cb3036d6`. Il riferimento `VC-NTC/2` rimasto nel § 2 si legge secondo l'errata già conservata nel dossier del § 3.4.5; il canone non cambia.

## G0 - atti, perimetro e confini

Inclusi il D.M. 17 gennaio 2018, § 3.5, pagine fisiche 63-66, e la Circolare 21 gennaio 2019 n. 7 C.S.LL.PP., § C3.5, pagina fisica 81. Le copie ufficiali hanno rispettivamente SHA-256 `dda1e397d56d71aa0f5bc457c3ba9b77064a468699dfc37bd056ac6c47105a46` e `f7c3b8d1f443aadb6b3e020b6b6c19813683492ecaadd2c15bf6bf1939aaed7c`.

Il riscontro visivo conferma i confini: NTC dalla rubrica `3.5. AZIONI DELLA TEMPERATURA` nella p. 63 alla fine della Tab. 3.5.III nella p. 66, prima di 3.6; Circolare da `C3.5 AZIONI DELLA TEMPERATURA` alla fine del capoverso C3.5.2 nella p. 81, prima di C3.6. Sono esclusi § 3.4.5/C3.4.5, § 3.6/C3.6 e il duplicato storico non indicizzato `cap03/3.5-temperatura.md`. **G0: OK.**

## G1 - vigenza

Riusata la ricognizione del 2026-09-09 sugli stessi atti e versioni; ricontrollo mirato ufficiale eseguito il 2026-09-11 e conservato in `g1/ricontrollo-g1.md`, con URL, copie HTML e impronte in `g1/fonti-ricontrollo.json`. Non risultano aggiornamenti pertinenti a § 3.5/C3.5.

Il rapporto HRM G0-G4 indicava erroneamente che il D.M. 9 marzo 2023 intervenisse sul punto 7.4.3.1. È un `ERR-AUDIT` descrittivo dell'evidenza pregressa: l'art. 1 modifica l'art. 2 del decreto del 2018 e disciplina le sospensioni dei punti 11.4.2 e 11.5.2. La conclusione resta invariata, perché il § 3.5 non è interessato. **G1: OK alle date 2026-09-09 / 2026-09-11.**

## Composizione e mappa di copertura

Lo snapshot finale elenca gli otto file della scheda e i due asset. La verifica del manifest contro i file vivi dà `10/10 OK`. Il composito `g5-r02/target-scope.md`, 136 righe, contiene in ordine fonte tutte le 79 righe normative non vuote ricavate dai singoli Markdown, con corrispondenza sequenziale esatta; sono esclusi soltanto navigazione, indici interni, ancore e diciture redazionali di provenienza.

| Fonte primaria | Righe del composito | Contenuto |
|---|---:|---|
| NTC p. 63 | 1-8 | rubriche 3.5 e 3.5.1, due capoversi |
| NTC p. 64 | 9-61 | 3.5.2, Fig. 3.5.1, formule [3.5.1]-[3.5.8], 3.5.3 |
| NTC p. 65 | 62-112 | 3.5.4, Fig. 3.5.2, Tab. 3.5.I-II, 3.5.5-3.5.6 |
| NTC p. 66 | 113-129 | 3.5.7 e Tab. 3.5.III |
| Circolare p. 81 | 130-136 | C3.5 e C3.5.2 |

La mappa copre una volta sola le righe 1-136, senza lacune o sovrapposizioni primarie. Le due immagini richiamate puntano agli asset inclusi nello snapshot e copiati byte per byte nel dossier R02.

## G2-G4 - ricollazione e apparati

Il diff tra il backup `pre-e-r01` e gli otto file finali riscontra i 15 interventi approvati: otto rubriche NTC e due rubriche Circolare riallineate alla fonte; [3.5.6] con `0.3`; formula inline completa `\Delta T_u = T - T_0`; `tener conto`; ripristino dei due asset. L'unica variazione ulteriore è l'indice interno derivato di C3.5.2. R02 ha aggiunto il secondo asset col nome effettivamente richiamato, byte-identico all'immagine nativa `ntc-p65-xref1105.png`, SHA-256 `42d8357bab9e67729e98dfc4ca9de4e360a865b0f583d47a9d0d61e386c85b02`.

La ricollazione visiva delle cinque pagine fonte e del composito conferma la prosa e le rubriche. Gli apparati sono riconciliati integralmente: otto formule numerate, tre tabelle e due figure. In particolare, la fonte stampa il punto decimale in [3.5.6]; la formula inline e `tener conto` coincidono con p. 65; valori, segni, unità e accorpamenti delle tre tabelle sono completi; Fig. 3.5.1 è completa nel ritaglio della p. 64 e la sua area sorgente è composta da cinque bande JPEG incorporate e contigue, xref 1091-1095; Fig. 3.5.2 coincide con il raster nativo. Le differenze residue sono le sole normalizzazioni 6, 7 e 9 del catalogo. Nessuna classe A, AF-COR o lettura dubbia. **G2: OK. G3: OK. G4: OK.**

## G5 - preflight e resa

Il composito e il render R02 coincidono con le impronte registrate: Markdown `6962e1b4de3b9cc9a0148c388b40f28fb83d5e57c93e4f537b6f4547eabb7bba`, PDF `58e5e7283543d4aec4cc3c3b7b8844487a5bea8746607d797e7b1a62b4ef0b2c`; le cinque PNG e gli altri riscontri sono in `riscontro-input-ripresa.json`. La verifica visiva integrale delle cinque pagine conferma rubriche, prosa, formule, figure e tabelle leggibili e complete, tag fra quadre, nessun glifo mancante, contenuto fuori margine, taglio o sovrapposizione. La didascalia della Tab. 3.5.II chiude p. 4 e la tabella inizia a p. 5: il contenuto è completo e la separazione è una sola scelta di impaginazione, non un rilievo di conformità. Si riusano inoltre gli esiti già registrati: lint globale zero errori/avvisi e indici interni 311 file/1754 collegamenti verificati. Zero candidati non decisi. **G5: OK e riutilizzabile.**

## Anomalie e giudizio conclusivo

Resta la sola rettifica documentale G1 sopra indicata, chiusa in questo rapporto e senza effetto sul target. Gli esiti Hermes R01b e R01d confermano uscita tecnica 1 per assenza di eventi SSE, inventario assente e nessun testo target rivelato; non costituiscono G6 e non consumano il giro. Non emergono rilievi che impediscano di riusare G5 sullo snapshot SHA-256 aggregato `1728b7d061dd7b7ddcd3ea34ef395759084293efcbb592a5201b56bb5ac29a9c`. G6 resta non iniziato, `giro_g6: 0`.

**Firma:** Codex / CDX, ruolo C Sol high.
