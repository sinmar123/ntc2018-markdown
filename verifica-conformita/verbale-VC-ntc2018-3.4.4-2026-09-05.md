# Verbale VC del § 3.4.4, Coefficiente di esposizione

Data di chiusura: 2026-09-05. Firma: Codex (CDX), coordinamento della ripresa gpt-6-astra/xhigh. Giudizio critico G7: gpt-5.6-sol/xhigh, /root/v_344_r01b.

**Esito: VC-OK**, limitatamente al file [3.4.4-neve-coefficiente-di-esposizione.md](../cap03/3.4.4-neve-coefficiente-di-esposizione.md), snapshot SHA-256 `6e9a5f838301b7d04ed3dc6c39256fcaf6d78997f2f5567350d287bb6cafc448`. Tutti G0-G7 OK, nessun ERR-MD, ERR-AUDIT o DUBBIO residuo. Nessuna revisione umana integrale documentata.

## Fonte, perimetro e vigenza

D.M. 17 gennaio 2018, allegato tecnico, solo § 3.4.4: pagina fisica 63, pagina stampata 59, dalla rubrica al termine della Tab. 3.4.I, prima di 3.4.5. Escluse le sezioni precedenti e successive sulla pagina condivisa. La Circolare non contiene un autonomo C3.4.4; pagine fisiche 80-81 consultate soltanto per accertare il confine G0, senza attribuire loro copertura normativa G6.

Fonti ufficiali: [scheda GU 18A00716](https://www.gazzettaufficiale.it/eli/id/2018/02/20/18A00716/sg), [PDF del supplemento](https://www.gazzettaufficiale.it/do/gazzetta/downloadPdf?dataPubblicazioneGazzetta=20180220&edizione=0&estensione=pdf&numeroGazzetta=42&numeroSupplemento=8&progressivo=0&tipoSerie=SG&tipoSupplemento=SO). PDF congelato SHA-256 `dda1e397d56d71aa0f5bc457c3ba9b77064a468699dfc37bd056ac6c47105a46`; acquisizione del 2026-09-05 e confronto binario positivo registrati nel fascicolo G1.

Vigenza ricognita al 2026-09-05, riutilizzata nella ripresa della stessa data e sul medesimo scope: esaminate le fonti ufficiali e il [D.M. 9 marzo 2023](https://www.gazzettaufficiale.it/eli/id/2023/03/22/23A01847/sg), senza modifiche al contenuto del § 3.4.4 rilevate nelle ricerche documentate. La ricognizione e gli HTML acquisiti sono compresi nel manifest; il solo hash non è stato usato come prova di vigenza.

Procedura VC-NTC/1, SHA-256 `3ed1723a25f875fad7632b5a7b7ce773d435dcb685fec938ea18df2524be93db`. Catalogo delle normalizzazioni congelato, SHA-256 `d71319206ec54bcac3639dfd0b97c41754fa1062655b2d35c36ee5d6cb3036d6`. Nessuna modifica del metodo nel corso dello scope.

## Gate e copertura

| Gate | Esito | Evidenza essenziale |
|---|---|---|
| G0 | OK | Atto, file e confini della pagina condivisa riconciliati |
| G1 | OK | Acquisizioni e ricognizione ufficiale del 2026-09-05 |
| G2 | OK | Una pagina primaria, tutte le 11 righe depurate, nessuna lacuna o sovrapposizione |
| G3 | OK | Confronto integrale della prosa e ricostruzione esatta del diff approvato |
| G4 | OK | Ritaglio 600 dpi, font/codepoint/coordinate vettoriali, apparati integralmente verificati |
| G5 | OK | Quattro link locali, indici canonici, render completo di una pagina verificato a vista |
| G6 | OK | Inventario fonte-prima congelato, 19/19 elementi, 7/7 input integri, zero residui |
| G7 | OK | Manifest riaperto, 53/53 file integri, giudizio critico indipendente e resa finale |

Copertura: una rubrica, un capoverso di tre proposizioni, un rinvio, una didascalia, una tabella con tre intestazioni e nove celle di corpo; quattro notazioni C con pedice E e relazione inline C con pedice E = 1. Nessuna formula esposta, figura, nota o asset del target. Il conteggio di 19 elementi G6 include i livelli di inventario e non si somma ai conteggi per componenti.

## Correzioni e classificazioni

Prima di G6, E distinto ha applicato le sole liste congelate: R01, cassa della rubrica; R02a, due notazioni nella prosa in tondo; R02b, notazione della testata in grassetto; R03, grassetto delle altre due intestazioni. Il confronto del target finale ricostruito dallo snapshot iniziale mediante tali sostituzioni è identico, senza modifiche estranee. Prosa, valori e associazioni delle celle restano quelli della fonte. Nella ripresa il testo non è stato modificato.

Normalizzazioni applicate: voci 1 (spaziature, a capo, sillabazione), 2 (apostrofi) e 10 (separatore di didascalia). Navigazione e indice sono esclusi meccanicamente dal confronto. Nessuna anomalia A/AF e nessuna correzione C/AF-COR. Nessun rilievo da adjudicare dopo G6. La resa degli altri viewer resta quella dichiarata nel catalogo.

## Indipendenza e tentativi

C iniziale gpt-6-astra/max, profilo ereditato; C della ripresa gpt-6-astra/xhigh. E gpt-5.6-sol/high, un contesto e due interventi vincolati. V G6/G7 gpt-5.6-sol/xhigh, contesto fresco /root/v_344_r01b, distinto da C ed E. Attività meccaniche con script locali. Verifica AI, senza attestazione di revisione umana integrale.

Il tentativo tecnico precedente fu respinto prima del congelamento e della rivelazione del target ed è conservato nel dossier storico. Il nuovo V ha rifatto l'inventario fonte-prima in contesto separato. G6 R01B: unico giro effettivo, **1/3**, interamente positivo; lo scope occupa una sola pagina e richiede un unico blocco.

Isolamento mediante cartelle temporanee distinte e restrizione istruttiva, senza sandbox filesystem. Inventario/canone congelati prima del primo accesso al target. Il controllo delle 13 custom_tool_call filesystem del verificatore ha riscontrato letture nei soli input ammessi; i messaggi interagente cifrati restano fuori da tale controllo. Sequenza e precisazione documentale sono conservate senza riscrivere i rapporti originari.

## Evidenze e catena delle impronte

- [Manifest di rilascio](vc-3.4.4-20260905/manifest-rilascio.json): 53 file selezionati e riaperti, SHA-256 `7e7b8870d2eba6818009154e3b412f33b5f10a6f18d5040f8eee7b4defd1de78`.
- [Rapporto G7](vc-3.4.4-20260905/rapporto-g7.json): SHA-256 `0d025a29899c8bfe4a4158720416149cf28ab869983906ee29a278f18c823389`.
- [Rapporto G6 originale](vc-3.4.4-20260905/g6-r01b/b01/rapporto-g6.json), [inventario congelato](vc-3.4.4-20260905/g6-r01b/b01/inventario.json) e [sequenza G6](vc-3.4.4-20260905/sequenza-g6-r01b.json).
- [Rapporto C G0-G5 e ripresa](../_tmp_render/cap03/vc-3.4.4-20260905/rapporto-c-g0-g5.md), [proposta C di chiusura](vc-3.4.4-20260905/rapporto-c-chiusura.md), [render finale](../_tmp_render/cap03/vc-3.4.4-20260905/render-finale.pdf).
- [Scheda e consumi](scheda-scope-ntc2018-3.4.4.md): sessioni e tentativi effettivi, contatori disponibili separati per perimetro. Non è attestato un risparmio percentuale o un costo della quota d'abbonamento.

Il manifest comprende gli input e le evidenze effettivamente usate fino a G6 e nella preparazione di G7; il rapporto G7 e questo verbale ne costituiscono la chiusura esterna, senza hash autoreferenziali. Le registrazioni derivate non modificano lo snapshot verificato. VC-OK vale per tale snapshot e per la data di vigenza dichiarata, senza sostituire la fonte ufficiale.

Prossima azione: Attendere un nuovo via libera prima di aprire il solo scope 3.4.5 o altri scope.
