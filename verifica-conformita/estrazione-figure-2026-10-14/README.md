# Estrazione delle 115 figure mancanti, 2026-10-14

Intervento tecnico di CC cloud, chiesto da Sandro il 2026-10-14. Non è una VC: le figure e i file che le richiamano restano nello stato del registro, e la verifica di ogni figura sulla fonte resta compito della VC del paragrafo.

## Fonti

| Atto | File | SHA-256 |
|---|---|---|
| NTC 2018, G.U. n. 42 del 20/02/2018, S.O. n. 8 | `../fonte-ufficiale/GU-2018-42-SO8-DM-17-01-2018.pdf` | `dda1e397d56d71aa0f5bc457c3ba9b77064a468699dfc37bd056ac6c47105a46` |
| Circolare 21/01/2019 n. 7, G.U. n. 35 dell'11/02/2019, S.O. n. 5 | `../fonte-ufficiale/GU-2019-35-SO5-Circolare-7-2019.pdf` | `f7c3b8d1f443aadb6b3e020b6b6c19813683492ecaadd2c15bf6bf1939aaed7c` |

## Metodo

Ogni figura è stata cercata dalla sua didascalia, ricavata dal testo alternativo del capitolo o, in mancanza, dal nome del file. La pagina è quella del PDF, non quella stampata della Gazzetta. Il ritaglio esclude la didascalia, che nei capitoli è già scritta come testo.

| Metodo | Figure | Come |
|---|---|---|
| Raster nativo | 44 | Immagine incorporata nel PDF, estratta senza ricampionare |
| Vettoriale | 23 | Area fra l'ultima riga di prosa e la didascalia, resa a 300 dpi |
| Scansione | 33 | Capitolo 7 della Circolare (pagine PDF 197-253): pagine solo immagine, scansioni JPEG 2219×3106 in scala di grigi. Ritaglio dei pixel nativi, senza ricampionare; posizione delle righe dall'OCR di tesseract 5.3.4 (`ita`) |
| Manuale | 15 | Riquadro o immagine fissati a mano dopo il controllo visivo (`strumenti/manuali.json`) |

Fra le 33 scansioni, cinque hanno la banda di ricerca fissata a mano: tre figure in `strumenti/scansioni-manuali.py` e le due parti della Tab. C7.3.I.

Tutti i ritagli sono stati controllati a vista su fogli con la pagina, il riquadro in rosso e il ritaglio affiancati. Per ogni figura `registro-figure.json` riporta file, etichetta, atto, pagina PDF, metodo, riquadro (in punti PDF o in pixel della scansione), dimensioni e SHA-256.

## Casi da sapere

- **Fig. C7.10.3**: la Circolare stampa due figure numerate C7.10.2 (pagine PDF 237 e 239). Il capitolo chiama la seconda C7.10.3 e lo dichiara già nella didascalia; il file viene dalla pagina 239.
- **Fig. 7.11.1**: il file si chiama `fig-7.11.1a-…` ma il capitolo lo richiama una volta sola per l'intera Fig. 7.11.1. Il ritaglio comprende le parti a) e b).
- **Fig. 7.5.1**: nella NTC occupa due pagine, b1)-b3) a pagina PDF 244 e c)-e) a pagina 245; la parte a) è solo testo. L'immagine unisce le due parti una sopra l'altra, rese a 300 dpi.
- **Figg. 5.1.3a e 5.1.3b**: nella NTC sono un'unica immagine incorporata. Divisa nella fascia bianca fra le due parti (colonna 1065 di 1685), senza ricampionare.
- **Figg. C7.2.1 e C7.2.2, C7.3.2a e C7.3.2b**: affiancate nella scansione, separate lungo la fascia bianca.
- **Fig. 5.1.2** e **Fig. C5.2.3**: ciascuna è fatta di due immagini incorporate, accostate senza ricampionare.
- **Fig. C4.1.6**: nella fonte la «P» di «Pilastro superiore» è coperta dal triangolo grigio. Il ritaglio la conserva così.
- **Tabelle 4.3.III, 4.4.IV, 4.4.V, C4.3.I, C7.3.I**: nei capitoli sono immagini. Il ritaglio segue la griglia della tabella; le note sotto la tabella restano fuori, perché i capitoli le riportano come testo. La Tab. C7.3.I è in due parti, una per pagina (PDF 213 e 214).

## Strumenti

Gli script in `strumenti/` sono quelli usati, conservati per riprodurre il lavoro dalla radice del repository; i percorsi di lavoro vanno passati come argomenti. Servono PyMuPDF, Pillow e tesseract con la lingua italiana.
