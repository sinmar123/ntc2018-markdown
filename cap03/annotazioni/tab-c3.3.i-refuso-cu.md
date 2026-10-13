---
title: Approfondimento - Tab. C3.3.I, possibile refuso C_U
stato: nota di approfondimento
data: 2026-05-31
tipo: probabile refuso non confermato
riferimento: C3.3.8.1.1 - Tabella C3.3.I
---
[Torna a 3.3 Vento](../3.3.8-vento-coefficienti-aerodinamici.md#c33811-pareti-verticali) - [Indice capitolo 3](../indice-cap03.md) - [Indice annotazioni](./README.md)

# Approfondimento - Tabella C3.3.I: possibile refuso nelle intestazioni `$C_{U}$`

## Origine

Questa nota recepisce il report di ricerca `Research Report tabella.md`, fornito da Sandro tramite Google Drive il 2026-05-31:

<https://drive.google.com/file/d/1mcIJM5Ip6JmIKvdTHEnQJroKg_HcLl6B/view?usp=drivesdk>

Il report riguarda la Tabella C3.3.I della Circolare 21 gennaio 2019, n. 7 C.S.LL.PP., nel paragrafo C3.3.8.1.1 "Pareti verticali".

## Sintesi

- La Tabella C3.3.I è intitolata "Edifici a pianta rettangolare: `$c_{pe}$` per facce sopravento, sottovento e laterali".
- Le intestazioni pubblicate nel PDF sono però:
  - `Faccia sopravento`;
  - `$C_{U}=2{,}0$`;
  - `$C_{U}=1{,}5$`.
- Questo è tecnicamente sospetto, perché `$C_{U}$` nelle NTC indica normalmente il coefficiente d'uso della costruzione, non un coefficiente aerodinamico del vento.
- Le formule presenti sotto le colonne 2 e 3 corrispondono invece, per andamento e segno, ai coefficienti globali `$c_{pe}$` delle facce laterali e della faccia sottovento.
- Alla data del report non risulta una errata corrige ufficiale del C.S.LL.PP. o della Gazzetta Ufficiale riferita alla Tabella C3.3.I.

Classificazione prudente: **probabile refuso non confermato ufficialmente**.

## Verifica sul PDF locale

Nel progetto è stato prodotto un render ad alta risoluzione della tabella dal PDF `raw/Circolare-7-2019-NTC.pdf`:

`_tmp_render/cap03/confronti/tab-C3.3.I-pdf-hires.png`

Il render conferma che l'anomalia non nasce dalla conversione Markdown: nel PDF della Circolare le intestazioni appaiono effettivamente come `$C_{U}=2{,}0$` e `$C_{U}=1{,}5$`.

## Perché `$C_{U}$` è sospetto

Nelle NTC 2018 `$C_{U}$` è il coefficiente d'uso impiegato per definire il periodo di riferimento dell'azione sismica:

$$V_R = V_N \cdot C_{U}$$

I valori `$C_{U}=1{,}5$` e `$C_{U}=2{,}0$` sono quelli tipici delle classi d'uso III e IV. Questo contesto non ha relazione diretta con i coefficienti aerodinamici `$c_{pe}$` del vento.

Nella Tabella C3.3.I, invece, le formule sono tutte formule di pressione/depressione sulle facce dell'edificio. I valori negativi delle colonne 2 e 3 sono incompatibili con un coefficiente d'uso.

## Mappatura tecnica probabile

| Colonna | Intestazione pubblicata | Interpretazione tecnica probabile | Formula riportata |
|---|---|---|---|
| 1 | Faccia sopravento | Faccia sopravento | per `h/d <= 1`: `$c_{pe} = 0,7 + 0,1 h/d$`; per `h/d > 1`: `$c_{pe} = 0,8$` |
| 2 | `$C_{U}=2{,}0$` | Facce laterali | per `h/d <= 0,5`: `$c_{pe} = -0,5 - 0,8 h/d$`; per `h/d > 0,5`: `$c_{pe} = -0,9$` |
| 3 | `$C_{U}=1{,}5$` | Faccia sottovento | per `h/d <= 1`: `$c_{pe} = -0,3 - 0,2 h/d$`; per `1 < h/d <= 5`: `$c_{pe} = -0,5 - 0,05(h/d - 1)$` |

La mappatura è coerente con la Fig. C3.3.2, con il titolo della tabella e con l'impostazione tecnica dei riferimenti citati dalla Circolare per gli edifici a pianta rettangolare.

> **Attenzione, aggiunto il 6/8/2026.** Le formule della colonna «Formula riportata» qui sopra sono la lettura **voluta**, non la trascrizione letterale. La Gazzetta stampa la formula della colonna 2 con **due segni meno consecutivi**, `c_pe = -0,5 - -0,8·h/d`, e dal 6/8/2026 `3.3-vento.md` la riproduce così, alla lettera. La ragione, la prova e la lettura corretta stanno in [AF-3.3-02](./3.3-anomalie-fonte.md#af-33-02-tab-c33i-doppio-segno-meno-nella-colonna-cu-20). Questa pagina e quella descrivono **due anomalie distinte della stessa tabella**: qui le intestazioni $C_U$, là il doppio meno.

## Fonti indicate nel report

| Fonte | Tipo | Indicazione utile |
|---|---|---|
| Gazzetta Ufficiale, atto 19A00855 | Fonte ufficiale | Pubblica la Circolare 21 gennaio 2019, n. 7. Non risulta una errata corrige specifica sulla Tabella C3.3.I. |
| PDF del capitolo C3 su Archliving | Copia non ufficiale fedele | Riproduce il capitolo C3 e mantiene la stessa anomalia testuale. |
| Commentario Albano, Legislazione Tecnica | Commento editoriale | Riproduce la tabella con le intestazioni `$C_{U}=2{,}0$` e `$C_{U}=1{,}5$`, confermando la propagazione dell'anomalia. |
| Manuale Jasp | Manuale software | Usa la Tabella C3.3.I come tabella di coefficienti `$c_{pe}$` per le facce, non come tabella di coefficienti d'uso. |
| EN 1991-1-4 | Riferimento tecnico | Distingue le zone/facce sopravento, sottovento e laterali per i coefficienti di pressione esterna. |
| CNR-DT 207/2008 | Riferimento tecnico nazionale | Usa la stessa impostazione generale per pareti laterali, faccia sopravento e facce sottovento/laterali. |

Link principali indicati nel report:

- Gazzetta Ufficiale, atto 19A00855: <https://www.gazzettaufficiale.it/eli/id/2019/02/11/19A00855/sg>
- Archliving, capitolo C3: <http://ntc.archliving.it/wp-content/uploads/2019/03/CAPITOLO-C3.pdf>
- Commentario Albano, estratto Legislazione Tecnica: <https://ltshop.legislazionetecnica.it/show_doc.asp?nomedoc=%2Fallegati_pdf%2FA-320-7-Commentario-NTC18-Circolare-Applicativa.pdf>

## Giudizio operativo

La lettura tecnicamente coerente è:

- colonna 1: faccia sopravento;
- colonna 2: facce laterali;
- colonna 3: faccia sottovento.

Tuttavia il testo ufficiale della tabella nel file `3.3-vento.md` resta mantenuto come pubblicato nel PDF, con le intestazioni `$C_{U}=2{,}0$` e `$C_{U}=1{,}5$`. L'interpretazione correttiva è riportata solo in nota, perché non esiste una rettifica ufficiale.

## Nota cautelativa consigliata

> **Nota di Sandro - possibile refuso di intestazione nella Tabella C3.3.I.** Nel testo pubblicato della Circolare 7/2019, le intestazioni della seconda e terza colonna della Tabella C3.3.I risultano `$C_{U}=2{,}0$` e `$C_{U}=1{,}5$`. Tali diciture sono incongruenti con il titolo della tabella, che riguarda i coefficienti `$c_{pe}$` per facce sopravento, sottovento e laterali, e con il significato ordinario di `$C_{U}$` nelle NTC, cioè coefficiente d'uso. Le formule riportate sotto le due colonne corrispondono invece ai coefficienti globali delle facce laterali e della faccia sottovento. In assenza di errata corrige ufficiale, il testo tabellare resta fedele alla fonte, ma la lettura tecnica più coerente è considerare le colonne come riferite a facce laterali e faccia sottovento.
