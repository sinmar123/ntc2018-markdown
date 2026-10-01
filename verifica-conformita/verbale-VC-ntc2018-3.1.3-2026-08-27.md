---
scope_id: ntc2018-3.1.3
data: 2026-08-27
stato: VC-OK
markdown_sha256: 40ff097b595fcf59bc6de8cbdd8b7bfa644636f19b4dcc48a7964a359e56a654
fonte_ntc_sha256: dda1e397d56d71aa0f5bc457c3ba9b77064a468699dfc37bd056ac6c47105a46
fonte_circolare_sha256: f7c3b8d1f443aadb6b3e020b6b6c19813683492ecaadd2c15bf6bf1939aaed7c
---

# Verbale di verifica di conformità - NTC 2018 § 3.1.3 e Circolare C3.1.3

## Perimetro

Il controllo riguarda esclusivamente `cap03/3.1.3-opere-civili-carichi-permanenti-non-strutturali.md`, corrispondente al § 3.1.3 `CARICHI PERMANENTI NON STRUTTURALI` dell'allegato al D.M. 17 gennaio 2018 e al § C3.1.3 omonimo della Circolare 21 gennaio 2019 n. 7.

Le fonti occupano le pagine fisiche NTC 46-47, stampate 42-43, e la pagina fisica Circolare 46, stampata 42. Inventario: 2 titoli, 7 capoversi narrativi, 11 frasi narrative e 5 enunciati matematici; nessuna formula numerata, tabella, figura o asset.

## Fonti e vigenza

- D.M. 17 gennaio 2018: `verifica-conformita/fonte-ufficiale/GU-2018-42-SO8-DM-17-01-2018.pdf`, SHA-256 `dda1e397d56d71aa0f5bc457c3ba9b77064a468699dfc37bd056ac6c47105a46`.
- Circolare 21 gennaio 2019 n. 7: `verifica-conformita/fonte-ufficiale/GU-2019-35-SO5-Circolare-7-2019.pdf`, SHA-256 `f7c3b8d1f443aadb6b3e020b6b6c19813683492ecaadd2c15bf6bf1939aaed7c`.

Entrambi i PDF locali sono stati confrontati con gli attuali download ufficiali della Gazzetta Ufficiale e risultano byte-identici. Il D.M. 9 marzo 2023 modifica l'art. 2 del decreto e introduce sospensioni temporanee relative ai punti 11.4.2 e 11.5.2; non modifica i §§ 3.1.3 o C3.1.3.

## Gate

- G0 `OK`: scope e confini accertati.
- G1 `OK`: fonti ufficiali identificate, hash ricalcolati e vigenza verificata.
- G2 `OK`: inventario source-first riconciliato al 100%.
- G3 `OK`: confronto testuale integrale superato dopo quattro correzioni logiche.
- G4 `OK`: cinque enunciati matematici verificati source-first in due passaggi indipendenti e riconciliati da P2.
- G5 `OK`: apparati di navigazione rigenerati meccanicamente; verifica globale di 311 file e 1754 collegamenti superata.
- G6 `OK`: primo giro cieco integrale, un blocco; 0 `ERR-MD`, 0 `ERR-AUDIT`, 0 `DUBBIO`.
- G7 `OK`: precontrollo P0-D Luna e controllo finale P2 Sol superati; tutte le 11 voci del manifest coincidono per SHA-256 e dimensione.

## Scarti e correzioni

Nel preflight sono stati rilevati quattro `ERR-MD`, corretti con tre sostituzioni fisiche:

1. rubrica NTC portata alla cassa della fonte, `CARICHI PERMANENTI NON STRUTTURALI`;
2. rubrica della Circolare portata alla medesima cassa;
3. eliminato il punto assente nella fonte dopo `C3.1.3`;
4. ripristinato il secondo `da` nella sequenza `o da normative o da documenti`.

Il riesame P1 ha annullato in memoria soltanto le tre sostituzioni e ricostruito esattamente lo snapshot iniziale `df65426720d7fa497f4296754e2c98a271947acdda0c3f465efcf52667fda8d3`. Le sole modifiche al testo normativo sono le quattro correzioni sopra elencate; il successivo riallineamento dell'etichetta dell'indice interno ha riguardato esclusivamente la navigazione. Nessun numero, valore, operatore o unità è stato modificato.

Normalizzazioni di classe N, tutte comprese nell'elenco unico `verifica-conformita/normalizzazioni-dichiarate-NTC2018.md`:

- spaziature, a capo, rientri e sillabazioni di fine riga;
- apostrofi curvi della fonte resi diritti nel Markdown;
- marcatori Markdown per titoli ed elenco;
- resa tipografica equivalente di pedici ed esponente;
- eliminazione dello spazio prima del punto e virgola del quarto enunciato e del punto finale del quinto.

Anomalie conservate `AF`: nessuna. Correzioni della fonte `AF-COR`: nessuna. Testo aggiunto alla fonte: nessuno nel pacchetto di confronto; gli apparati di navigazione sono rimossi meccanicamente.

## Controllo degli enunciati matematici

Due ricostruzioni source-first indipendenti, una con `gpt-5.6-luna/medium` e una con `gpt-5.6-sol/xhigh`, hanno controllato i cinque enunciati. Il passaggio A ha inizialmente letto come punto e virgola il terminatore finale; la riconciliazione P2 l'ha classificato `ERR-AUDIT` e chiuso a 600 dpi come punto, concorde col passaggio B e col Markdown.

Il controllo finale ha confermato tutti i pedici, esponenti, valori, virgole decimali, cinque segni `≤`, quattro segni `<`, cinque segni `=`, unità `kN/m` e `kN/m²`, quattro punti e virgola e il punto conclusivo. G4 `OK`, senza rilievi residui.

## G6 e indipendenza

Il G6 è stato coordinato da un subagente fresco P2 `gpt-5.6-sol/xhigh`. Inventario fonte-prima e confronto del blocco sono stati eseguiti da due ulteriori subagenti freschi P2 `gpt-5.6-sol/xhigh`, con materiali minimi in staging esterno al workspace. Nessuno ha ricevuto rilievi attesi o audit precedenti e nessuno ha modificato il Markdown.

I controlli sono stati eseguiti da agenti AI; non è inclusa una revisione umana integrale.

## Snapshot ed evidenze

Snapshot iniziale Markdown: `df65426720d7fa497f4296754e2c98a271947acdda0c3f465efcf52667fda8d3`.

Snapshot finale verificato: `40ff097b595fcf59bc6de8cbdd8b7bfa644636f19b4dcc48a7964a359e56a654`.

Evidenze principali:

- `_tmp_render/cap03/vc-3.1.3-20260827/preflight/rapporto-p0d-luna.md`;
- `_tmp_render/cap03/vc-3.1.3-20260827/preflight/rapporto-preflight.md`;
- i tre ritagli a 600 dpi in `_tmp_render/cap03/vc-3.1.3-20260827/fonte/`;
- `_tmp_render/cap03/vc-3.1.3-20260827/preflight/md-confronto-corretto-render.pdf`;
- `_tmp_render/cap03/vc-3.1.3-20260827/apparati/riconciliazione/registro-finale.md`;
- `_tmp_render/cap03/vc-3.1.3-20260827/g6-r01/rapporto-consolidato.md`;
- `verifica-conformita/manifest-sha256-ntc2018-3.1.3-2026-08-27.txt`.

Il frammento normativo depurato dagli apparati di navigazione ha SHA-256 `315b7b1eaea9a6a85ac2d100d77beca0acf1d083608042c5cc6b9e3e741dbf59`. Il render di controllo è leggibile su una pagina e la sua estrazione testuale conferma 6 occorrenze di `G₂`, 7 di `g₂`, 5 di `≤` e 5 di `kN/m²`.

## Rilascio

Il precontrollo P0-D Luna e il controllo finale P2 Sol hanno ricalcolato e confermato 11/11 voci del manifest; SHA-256 del manifest `745bc04fcc704855e01f76349bed02f33ce4a186274a65a9a283935fa5e2938d`. Tutti i gate G0-G7 sono `OK` e non restano rilievi aperti. Lo scope è promosso localmente a `VC-OK al 2026-08-27`; il giudizio vale soltanto per lo snapshot e il perimetro dichiarati.

Firma della redazione: CDX (Codex).
