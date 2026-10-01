---
scope_id: ntc2018-3.1.2
data: 2026-08-27
stato: VC-OK
markdown_sha256: c89175b4fab3660a3e1853a32b53cc4851957bc27d5f041720ba68107b6e3e9b
fonte_sha256: dda1e397d56d71aa0f5bc457c3ba9b77064a468699dfc37bd056ac6c47105a46
---

# Verbale di verifica di conformità - NTC 2018 § 3.1.2

## Perimetro

Il controllo riguarda esclusivamente `cap03/3.1.2-opere-civili-pesi-propri-dei-materiali-strutturali.md`, corrispondente al § 3.1.2 `PESI PROPRI DEI MATERIALI STRUTTURALI` dell'allegato al D.M. 17 gennaio 2018. Fonte: Gazzetta Ufficiale, Serie generale n. 42 del 20 febbraio 2018, Supplemento ordinario n. 8, pagina fisica 46 e pagina stampata 42. La Circolare 21 gennaio 2019 n. 7 non contiene un § C3.1.2 corrispondente ed è fuori scope.

Confini: dalla rubrica `3.1.2. PESI PROPRI DEI MATERIALI STRUTTURALI` fino alla frase `trattando i valori nominali come valori caratteristici.`, prima del § 3.1.3. Inventario: 1 titolo, 2 capoversi, 3 frasi e la Tab. 3.1.I con 2 colonne logiche, 5 categorie, 24 righe-valore, 4 intervalli e 20 valori singoli; nessuna formula, figura, nota o asset.

## Fonte e vigenza

Fonte congelata: `verifica-conformita/fonte-ufficiale/GU-2018-42-SO8-DM-17-01-2018.pdf`, SHA-256 `dda1e397d56d71aa0f5bc457c3ba9b77064a468699dfc37bd056ac6c47105a46`.

L'identità dell'atto è stata riscontrata sulla Gazzetta Ufficiale, codice redazionale `18A00716`. Il D.M. 9 marzo 2023 modifica l'art. 2 del decreto e introduce sospensioni temporanee relative ai punti 11.4.2 e 11.5.2; non modifica il testo dell'allegato § 3.1.2.

## Gate

- G0 `OK`: scope e confini accertati.
- G1 `OK`: fonte ufficiale identificata, hash ricalcolato e ricognizione della modifica del 2023 eseguita.
- G2 `OK`: inventario source-first riconciliato al 100%.
- G3 `OK`: confronto testuale integrale; titolo e corpo coincidono dopo le sole normalizzazioni dichiarate.
- G4 `OK`: Tab. 3.1.I verificata source-first in due passaggi indipendenti e riconciliata da P2; 24/24 coppie materiale-valore conformi.
- G5 `OK`: file indicizzato, collegamenti e àncore interne risolti; verifica globale degli indici interni superata.
- G6 `OK`: primo giro cieco integrale, un blocco; 0 `ERR-MD`, 0 `ERR-AUDIT`, 0 `DUBBIO`.
- G7 `OK`: precontrollo P0-D e controllo finale P2 superati; tutte le 8 voci del manifest coincidono per SHA-256 e dimensione.

## Scarti e correzioni

Nel preflight sono stati rilevati otto `ERR-MD`, tutti corretti:

1. rubrica `Pesi propri dei materiali strutturali` portata alla cassa della fonte, `PESI PROPRI DEI MATERIALI STRUTTURALI`;
2. intestazione `Materiali` portata alla cassa della fonte, `MATERIALI`;
3. intestazione `Peso unità di volume [kN/m³]` portata alla cassa della fonte, `PESO UNITÀ DI VOLUME [kN/m³]`;
4. ripetizione della categoria `Calcestruzzi cementizi e malte` nelle due celle logiche coperte;
5. ripetizione della categoria `Metalli e leghe` nelle due celle logiche coperte;
6. ripetizione della categoria `Materiale lapideo` nelle due celle logiche coperte;
7. ripetizione della categoria `Legnami` nelle due celle logiche coperte;
8. ripetizione della categoria `Sostanze varie` nelle due celle logiche coperte.

Il riesame P1 ha annullato in memoria soltanto gli otto edit e ricostruito esattamente lo snapshot iniziale. Nessuna cifra, valore, intervallo, unità, simbolo, denominazione o frase è stata modificata.

Normalizzazioni di classe N applicate e già comprese nell'elenco unico `verifica-conformita/normalizzazioni-dichiarate-NTC2018.md`:

- spaziature, a capo e rientri della pagina;
- apostrofi e virgolette curve della fonte resi diritti nel Markdown;
- marcatori Markdown per titolo, grassetto, corsivo e struttura della tabella;
- unità disposta su una seconda riga nella fonte e sulla stessa riga dell'intestazione nel Markdown;
- etichette di categoria accorpate nella fonte ripetute nelle due celle logiche coperte, secondo la voce 6 dell'elenco unico.

Anomalie conservate `AF`: nessuna. Correzioni della fonte `AF-COR`: nessuna. Testo aggiunto alla fonte: nessuno nel pacchetto di confronto; gli apparati di navigazione sono rimossi meccanicamente.

## Controllo della Tab. 3.1.I

Due ricostruzioni source-first indipendenti, una con `gpt-5.6-luna/medium` e una con `gpt-5.6-sol/xhigh`, hanno concordato su intestazioni, unità, 5 categorie e tutte le 24 coppie materiale-valore. Il controllo P2 ha confermato 4 intervalli, 20 valori singoli, virgole decimali, segni `÷` e unità `[kN/m³]`, senza rilievi.

## G6 e indipendenza

Il G6 è stato coordinato da un subagente fresco P2 `gpt-5.6-sol/xhigh`. Inventario fonte-prima e confronto del blocco sono stati eseguiti da due ulteriori subagenti freschi P2 `gpt-5.6-sol/xhigh`, con materiali minimi in staging esterno al workspace. Nessuno ha ricevuto rilievi attesi o audit precedenti e nessuno ha modificato il Markdown.

I controlli sono stati eseguiti da agenti AI; non è inclusa una revisione umana integrale.

## Snapshot ed evidenze

Snapshot iniziale Markdown: `b6df571a6afcccf13b834c8ef6d2f2a21dd341844c36f888a4978ac94f43730c`.

Snapshot finale verificato: `c89175b4fab3660a3e1853a32b53cc4851957bc27d5f041720ba68107b6e3e9b`.

Evidenze:

- `_tmp_render/cap03/vc-3.1.2-20260827/preflight/rapporto-p0d-luna.md`;
- `_tmp_render/cap03/vc-3.1.2-20260827/preflight/rapporto-preflight.md`;
- `_tmp_render/cap03/vc-3.1.2-20260827/fonte/ntc-p46-scope-3.1.2-600dpi.png`;
- `_tmp_render/cap03/vc-3.1.2-20260827/preflight/md-confronto-corretto-render.pdf`;
- `_tmp_render/cap03/vc-3.1.2-20260827/tabella/riconciliazione/registro-finale.md`;
- `_tmp_render/cap03/vc-3.1.2-20260827/g6-r01/rapporto-consolidato.md`;
- `verifica-conformita/manifest-sha256-ntc2018-3.1.2-2026-08-27.txt`.

La resa dei viewer che non usano il template ufficiale del progetto resta una normalizzazione di visualizzazione dichiarata. Il render di controllo depurato dagli apparati di navigazione è leggibile su una pagina; non contiene tag di formula o didascalie automatiche.

## Rilascio

Tutti i gate G0-G7 sono `OK` e non restano rilievi aperti. Il precontrollo P0-D e il controllo finale P2 hanno ricalcolato e confermato le 8 voci del manifest; SHA-256 del manifest `9516e80300273862fa25cafd2b32cee7db640cbe5aa1a79624631f3d0a26e4ad`. Lo scope è promosso localmente a `VC-OK al 2026-08-27`. Il giudizio vale soltanto per lo snapshot e il perimetro dichiarati.

Firma della redazione: CDX (Codex).
