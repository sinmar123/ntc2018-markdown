# Rapporto C finale G0-G5 - VC NTC 2018 § 3.5

**Data:** 2026-09-11  
**Scope:** unico `ntc2018-3.5`, otto Markdown e due asset  
**Ruolo:** C, `gpt-5.6-sol`, provider `openai-codex`, ragionamento `high`  
**Metodo:** VC-NTC/3, SHA-256 `4bd4440a6f9b204338e97ecf78c9bb74ab0d9e04f7478b9c97c436c62e817c7c`; catalogo SHA-256 `d71319206ec54bcac3639dfd0b97c41754fa1062655b2d35c36ee5d6cb3036d6`.

## Evidenze richiamate

Il presente rapporto chiude il controllo C post-E e sostituisce, per lo snapshot corrente, il giudizio G0-G5 del precedente `../rapporto-c-ripresa.md`, che resta congelato e invariato. Per G1 rinvia a `../g1/ricontrollo-g1.md`; per i sei rilievi del primo G6, alla decisione motivata `../adjudicazione-g6-r01.md`, alla lista congelata `../lista-correzioni-g6-r01.json` e all'addendum `../addendum-lista-correzioni-g6-r01-001.json`. L'applicazione E è documentata in `../e-cdx-r01/rapporto-e-cdx-r01.md`.

La prova firmata del secondo lettore fonte-only è `../prova-secondo-lettore-fonte-only.md`; la traccia filtrata è `../traccia-secondo-lettore.json`. Il JSONL integrale resta prova scratch in `../secondo-lettore-fonte-only-sessione-01a090fe-45f9-7b22-8b5e-a599762466ba.jsonl`, SHA-256 `0c7a1945da3d64fb7f97844500c08b0db6af0907d3dcbdc7496e8610aa973581`, e non è un allegato del dossier definitivo.

## G0-G1 - atti, scope e vigenza

Fonti, perimetro e confini non sono cambiati: NTC § 3.5, pagine fisiche 63-66, e Circolare § C3.5, pagina fisica 81. Il ricontrollo ufficiale G1 del 2026-09-11 non ha rilevato modifiche pertinenti. Resta chiuso come `ERR-AUDIT` il precedente riferimento descrittivo inesatto al D.M. 9 marzo 2023, senza effetto sul target. **G0: OK. G1: OK.**

## Controllo post-E e G2-G4

La lista e l'addendum risultano invariati, rispettivamente SHA-256 `6ca6843e575cfb9e8c14f8b7ded72b686280fb254f1e59ac7b17d27bfec82963` e `0b2e128cb0cf3d1ee16d0f689acd91b5c3acffd676ce39a96f9b79cd900e0bb9`. La ricostruzione indipendente dalla baseline `../pre-e-cdx-r01/` ha verificato una occorrenza per ciascuna stringa `prima`; tutti i file testuali risultanti coincidono esattamente con l'applicazione ordinata delle sostituzioni prescritte. Il nuovo file AF coincide con il contenuto della lista più la sola àncora dell'addendum, presente una volta e raggiunta dal rinvio portabile. Non risultano variazioni testuali ulteriori.

I sei rilievi del primo G6 sono chiusi: conservati alla lettera `d un anno` e il punto e virgola finale con annotazione `AF-3.5.2-01`; completate secondo N6 le celle `Estate`, `Estate` e `Inverno`; ripristinato `azioni termiche speciali`; rigenerata Fig. 3.5.1 col crop prescritto, senza ricampionamento. L'asset misura 1520 × 1660 px e ha SHA-256 `fec8da7e6de1b4009d6d7a79ce88e7d0c136bd252e5242f5f5a8ab25536f7ff1`. Il controllo visivo distingue correttamente, sotto la Sicilia, i due piccoli elementi insulari separati; Sardegna e Sicilia non sono stati usati come surrogato di tale verifica. Fig. 3.5.2 resta invariata, SHA-256 `42d8357bab9e67729e98dfc4ca9de4e360a865b0f583d47a9d0d61e386c85b02`. **G2: OK. G3: OK. G4: OK.**

## Composizione e mappa di copertura

`composizione.json` registra otto fonti Markdown, 136 righe complessive e 79 righe non vuote. Il composito ha SHA-256 `cfe9119fad6da4d7e1f778b8b69ee04f8d67ae5c62626d7e876c1fcf7c1a31b1`; contiene integralmente e nell'ordine previsto le porzioni normative, dopo la sola depurazione meccanica degli apparati editoriali prevista dal metodo.

| Fonte primaria | Righe del composito | Contenuto |
|---|---:|---|
| NTC p. 63 | 1-8 | 3.5 e 3.5.1 |
| NTC p. 64 | 9-61 | 3.5.2, Fig. 3.5.1, formule [3.5.1]-[3.5.8], 3.5.3 |
| NTC p. 65 | 62-112 | 3.5.4, Fig. 3.5.2, Tab. 3.5.I-II, 3.5.5-3.5.6 |
| NTC p. 66 | 113-129 | 3.5.7 e Tab. 3.5.III |
| Circolare p. 81 | 130-136 | C3.5 e C3.5.2 |

La mappa copre le righe 1-136 una volta sola, senza lacune né sovrapposizioni. I due asset copiati nel dossier sono byte-identici ai target vivi.

## G5 - snapshot, preflight e resa

Il manifest `snapshot-target-finale.json` ha SHA-256 `bce58988f35b359df4ea503c1ce0785f4c11c97d395d57dc8d6ff13a913a9344`; `vc-supporto verifica-manifest` restituisce `10/10`, integrità `OK`. Il render canonico ha prodotto un PDF di cinque pagine, SHA-256 `ed8cd4258d01464bca80d358f3533822177c3225f99c50ef391c99a796983f76`. Le cinque PNG a 200 dpi coincidono con le impronte registrate in `raster-render.json`.

Sono state esaminate integralmente tutte le cinque pagine e, separatamente, entrambe le immagini. Rubriche, testo, formule, tag, figure e tabelle risultano leggibili e completi, senza glifi mancanti, tagli, sovrapposizioni o contenuto fuori margine. La seconda formula a fondo pagina 2 conserva circa 25 pt di margine inferiore nel PDF e non è tagliata. La Tab. 3.5.I mostra tutte le quattro righe con le celle ripetute prescritte; il testo C3.5 contiene `azioni termiche speciali`. Restano confermati lint globale con zero errori e zero avvisi e indici interni con 311 file e 1754 collegamenti validi. **G5: OK.**

## Giudizio e confini per il secondo G6

Non emergono anomalie residue, candidati non decisi o rilievi G0-G5 sullo snapshot corrente. L'anomalia `AF-3.5.2-01` è dichiarata e conservata, quindi non costituisce residuo. Il nuovo G6 integrale resta obbligatorio e non è svolto in questo rapporto.

Per il secondo G6 lo scope forma un unico blocco di cinque pagine. I confini non sono spostabili: la sola divisione possibile in sequenza produrrebbe blocchi di tre e due pagine, e il secondo violerebbe il minimo di tre pagine per blocco.

**Firma:** Codex / CDX, ruolo C Sol high.
