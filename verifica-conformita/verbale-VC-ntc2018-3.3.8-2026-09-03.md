---
scope_id: ntc2018-3.3.8
data: 2026-09-03
stato: VC-OK
markdown_sha256: 2997e1fd9e05b8f2045587c40d6d5cf0314c3f0a09d8811b59d7557ffd33125c
fonte_ntc_sha256: dda1e397d56d71aa0f5bc457c3ba9b77064a468699dfc37bd056ac6c47105a46
fonte_circolare_sha256: f7c3b8d1f443aadb6b3e020b6b6c19813683492ecaadd2c15bf6bf1939aaed7c
manifest_sha256: e5cc0a40531b9b34cbdb0c58b10e3ba4e5d01d8bd03526ac0d816cf80abaffcf
---

# Verbale di verifica di conformità - NTC 2018 § 3.3.8

## Perimetro e continuità

Perimetro: `cap03/3.3.8-vento-coefficienti-aerodinamici.md`, § 3.3.8 delle NTC, pagina fisica 60, e § C3.3.8 della Circolare, pagine fisiche 55-74. Dimensionamento effettivo: 21 pagine fonte, 6 formule numerate, 19 tabelle e 27 figure.

L'identità canonica con lo staging storico è stata dimostrata prima delle correzioni. Sono stati riusati G0-G5 e il G6 storico sui blocchi B02-B08; B08-05, relativo al § C3.3.11, è stato escluso. Sono stati applicati 19 rilievi pertinenti, per 31 occorrenze, e ripristinati 27 asset. Il G6 R02 ha ricontrollato a 600 dpi le quattro lacune storiche, le tre correzioni residue del checkpoint e gli asset ricostruiti; la copertura complessiva deriva dall'unione con i tratti validi del G6 storico e dal diff deterministico delle correzioni.

## G6 e G7

Il G6 R02 è stato eseguito da due verificatori AI freschi e indipendenti su blocchi disgiunti: Codex `gpt-5.6-sol` xhigh, blocco A, e Codex `gpt-5.6-sol` xhigh, blocco B. Il correttore separato è stato Codex `gpt-5.6-sol` high. Coordinamento, preflight deterministico e adjudicazione: Codex `gpt-5.6-sol`, sessione principale. Gli esecutori storici B02-B08 risultano dal consolidato R01: Codex `gpt-5.6-sol` xhigh, con il duplicato M01 affidato a Codex `gpt-5.6-terra` xhigh.

Esito del controllo incrementale G6 R02: 15 rilievi raggruppati `NORM`, 7 `AF`, 0 `AF-COR`, 0 `ERR-MD`, 0 `ERR-AUDIT`, 0 `DUBBIO`. Le quattro lacune di accoppiamento sono chiuse e le Figure C3.3.4, C3.3.14, C3.3.19, C3.3.20, C3.3.21 e C3.3.26 sono state confrontate integralmente nel contenuto interno. Il G7 P0-D e il controllo P2 fresco, eseguito da Codex `gpt-5.6-sol` xhigh, sono entrambi `OK`. Il P2 ha ricalcolato 117/117 record del manifest e controllato 30/30 pagine di resa. Non è stata eseguita una revisione umana integrale.

## Normalizzazioni di classe N applicate

- a capo, rientri, spaziatura e impaginazione senza modifica dell'ordine logico;
- varianti Unicode equivalenti, lineette delle didascalie e segno meno matematico;
- spaziatura LaTeX, delimitatori equivalenti e tag delle formule;
- punto di moltiplicazione esplicito dove la fonte usa la giustapposizione;
- espansione delle celle accorpate, con ripetizione di valori ed etichette in tutte le celle logiche coperte;
- disposizione sequenziale di gruppi tabellari affiancati, senza perdita o riordino dei valori;
- intestazione Markdown vuota per le griglie che nella fonte iniziano direttamente dai dati;
- resa su rami distinti delle formule a più casi, conservando il tag sul ramo stampato;
- trasformazione dei blocchi di definizione in elenchi, senza aggiunte o riordini;
- ricomposizione su una riga delle didascalie, uniformazione del separatore e omissione del punto finale;
- resa matematica della testata `Re` come `$R_e$`.

## Anomalie di classe A conservate

Sono conservate alla lettera, senza correzioni silenziose:

- il rinvio `C3.3.3.8.1`, la virgola in `si forniscono, tre` e la forma `Figura, C3.3.3`;
- le intestazioni `$C_U=2,0$` e `$C_U=1,5$` della Tabella C3.3.I e il doppio segno meno nella relativa formula;
- `Figure C3.3.4` al plurale e la locuzione `altezza minore o uguale della dimensione`;
- il punto decimale `±0.2` in sei celle della Tabella C3.3.IV;
- la testata `Θ – 0°` della Tabella C3.3.XI e la didascalia della Tabella C3.3.XII, che parla di suddivisione in zone mentre segue una griglia di coefficienti;
- `riportati i Figura C3.3.16`, la parentesi non chiusa nel rinvio alla Figura C3.3.19 e `Sono` maiuscolo dopo `$c_{pe,C}$`;
- il rinvio `Figura C.3.3.21` e la didascalia che parla di coefficienti di pressione pur rappresentando il coefficiente di forza `$c_F$`;
- la didascalia della Tabella C3.3.XVII riferita alle tettoie a semplice falda nel paragrafo sulle falde multiple;
- `il cui il rapporto`, la discordanza fra la descrizione verbale dell'altezza e la condizione `$b<h≤5b$`, e il successivo rapporto `h/d≤5` dove il diametro era stato indicato con `b`;
- le notazioni `c_{peo}`, `ψ_{λα}`, `α_p` e `c_{peA}`, nonché l'etichetta grafica della Figura C3.3.26 discordante dalla didascalia;
- la forma grammaticale `Indicate con:`.

Le anomalie a maggior rischio di essere scambiate per errori del corpus sono documentate permanentemente in `cap03/annotazioni/3.3-anomalie-fonte.md`, voci AF-3.3-01, AF-3.3-02, AF-3.3-03, AF-3.3-04, AF-3.3-06 e AF-3.3-09 fino ad AF-3.3-13. La Nota 4 di `cap03/annotazioni/3.3-note-redazionali.md` conserva inoltre il rilievo interpretativo sulle intestazioni `$C_U$` della Tabella C3.3.I.

Correzioni di classe C nello scope: nessuna. Le due correzioni AF-COR registrate nelle annotazioni del § 3.3 appartengono ai §§ 3.3.1 e 3.3.7 e non sono incluse nel presente giudizio.

## Resa e congelamento

Il render di controllo contiene 30 pagine e mostra i tag con le parentesi della fonte. Il template di verifica mappa esplicitamente i glifi Unicode non coperti dal font e, nella sola copia temporanea, inserisce la riga vuota necessaria al convertitore prima delle tabelle a pipe. I viewer che non usano il template possono rendere diversamente glifi e tabelle molto larghe: è una normalizzazione di visualizzazione, non una modifica del corpus.

Snapshot finale: `2997e1fd9e05b8f2045587c40d6d5cf0314c3f0a09d8811b59d7557ffd33125c`. Manifest: 117/117 record, SHA-256 `e5cc0a40531b9b34cbdb0c58b10e3ba4e5d01d8bd03526ac0d816cf80abaffcf`. Evidenze: `_tmp_render/cap03/vc-3.3.8-20260831/`.

Tutti i gate G0-G7 sono `OK`; lo scope è promosso a `VC-OK al 2026-09-03`. L'unica osservazione non bloccante riguarda la testata molto stretta della tabella resa a pagina 16, comunque completa e leggibile. Rapporto finale P2: `_tmp_render/cap03/vc-3.3.8-20260831/g7/rapporto-finale-p2-20260903.md`.

Firma della redazione: CDX (Codex).

