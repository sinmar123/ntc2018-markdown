# Confronto G0-G4, blocco A

Righe 1-164 del file `cap08/8.7.1-progettazione-interventi-costruzioni-in-muratura.md`. Pagine NTC 297-298, dalla rubrica 8.7.1 fino a prima di 8.7.2, e Circolare 270-274 fino a prima di C8.7.1.2.1.2. Fuori dal confronto: indice interno, ancore, link di ritorno, rubriche di struttura «Norma» e «Circolare», linea di separazione.

La Norma coincide con la pagina: rubrica `8.7.1. COSTRUZIONI IN MURATURA` e nove capoversi. Nella Circolare coincidono la prosa parola per parola, i due elenchi a trattino (voce 21 del catalogo), la formula [C8.7.1.1] e il W della [C8.7.1.2]. I corsivi dei simboli sono in LaTeX. Spazi, apostrofi e sillabazioni di fine riga rientrano nelle voci 1 e 2.

Copertura sulla fonte: 6 rubriche, 51 capoversi, 28 voci di elenco con marcatore, 15 righe dei due blocchi «dove», 2 formule numerate, 49 espressioni inline, nessuna tabella, figura o nota. Candidati scartati: 25, tra frammenti di formula, a capo interni alle voci e corsivi di simbolo già resi in matematica.

## Sostanziale

| ID | Pagina | Fonte | Markdown |
|---|---|---|---|
| A-01 | circ 273, formula [C8.7.1.2] | Φ maiuscolo | φ minuscolo |

La definizione sotto la formula stampa φ minuscolo. L’incongruenza è della fonte e non si pareggia.

## Forma

| Gruppo | ID | Che cosa |
|---|---|---|
| Rubriche | A-04–A-08 | Maiuscolo o maiuscoletto (voce 23) e niente punto dopo il numero. C8.7.1.2.1.1 è anche in grassetto corsivo. |
| Capoversi | A-13–A-40 | 28 fusioni. Il dettaglio, con il frammento unico e il `\n\n`, è nel JSON. |
| Elenchi | A-10, A-11, A-12 | Voci a)–e) e i due «dove» (voci 21 e 18). Recuperano anche lo stacco prima di «In generale» e prima di «Il punto di applicazione». |
| Enfasi | A-09, e dentro A-34 e A-35 | «approccio cinematico lineare» e «approccio cinematico non lineare» in grassetto corsivo. |
| Formula | A-02 | [C8.7.1.2] stampa `0.4` con il punto. La voce 4 non copre la virgola. Il numero non cambia. |
| Prosa | A-03 | Il periodo di C8.7.1.2.1.1 chiude con «q,» e un punto. Il Markdown ha solo il punto. |

## Anomalie della fonte

Non si propongono correzioni.

| Pagina | Anomalia | Nel Markdown |
|---|---|---|
| circ 271 | Nell’elenco dei dissesti, «presenza di fenomeni di degrado nei materiali» chiude col punto fermo; le altre voci col punto e virgola. | conservata |
| circ 272 | Rinvio «v. § C8.7.1.2.4», con un livello in meno rispetto alle rubriche C8.7.1.2.1.n stampate sulle stesse pagine. | conservata |
| circ 272 | Chiusura «q, .», senza testo di nota in calce. | non conservata (A-03) |
| circ 273 | [C8.7.1.2] con punto decimale `0.4`. | non conservata (A-02) |
| circ 273 | [C8.7.1.2] con Φ; la definizione con φ. | non conservata (A-01) |
| circ 273 | [C8.7.1.2] con W; la definizione con w. | conservata |

## Dubbio

A-41, circ 273, pedice di t nello spessore della parete trasversale. Lettura del livello testo: S maiuscolo (Palatino corsivo, corpo 4.8). Lettura della pagina a 200 dpi, anche ingrandita: s minuscolo, come il Markdown e come il t_s della formula. Nessuna delle due è scelta.
