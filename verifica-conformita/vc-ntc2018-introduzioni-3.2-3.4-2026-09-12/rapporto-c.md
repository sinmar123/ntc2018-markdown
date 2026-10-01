# Rapporto C, confronto iniziale G0-G4 delle introduzioni 3.2, 3.3 e 3.4

Data: 2026-09-12. Firma: Codex / CDX.

## Esito dei gate iniziali

**G0, OK.** I tre target coincidono byte per byte con gli snapshot iniziali. Confini confermati sulle pagine ufficiali: 3.2 NTC, p. fisica 49, dalla rubrica 3.2 al capoverso che termina con «successivi aggiornamenti», prima di 3.2.1; C3.2, pp. 46-47, dalla rubrica C3.2 alle tre figure C3.2.1 a, b, c e relative didascalie comprese, prima di C3.2.1, a p. 48. 3.3 NTC, p. 56, rubrica e due capoversi prima di 3.3.1; C3.3, p. 54, rubrica e capoverso prima di C3.3.1. 3.4 NTC, p. 61, sola rubrica prima di 3.4.1; C3.4, p. 76, sola rubrica prima di C3.4.1.

**G1, OK.** È riusata la ricognizione congelata del 2026-09-09 sui medesimi D.M. 17 gennaio 2018 e Circolare 21 gennaio 2019 n. 7, entro trenta giorni, con il ricontrollo mirato GU del 2026-09-12 già presente in g1. Il D.M. 9 marzo 2023 individuato dalla ricognizione interviene sui punti 11.4.2 e 11.5.2, estranei alle introduzioni 3.2-3.4. Il campo scope del JSON di ricontrollo nomina l’introduzione 3.1, ma le due interrogazioni e gli atti controllati sono a livello di atto e sono gli stessi dello scope presente; la sua applicabilità è quindi confermata. Non serve un’ulteriore ricerca generale.

**G2-G3, completati con rilievi.** Confrontato integralmente il testo delle sei porzioni, incluse rubriche, punteggiatura, rinvii e simboli inline. Sono ammesse e non rilevate come NC le spaziature, gli a capo, apostrofi/virgolette Unicode, le righe di navigazione e le righe editoriali identificative dell’atto. I marcatori visibili delle due liste di parametri non rientrano invece nelle normalizzazioni dichiarate: la voce 18 riguarda soltanto i blocchi «dove:».

**G4, completato con rilievi.** Inventario: tre figure e tre didascalie, tutte in C3.2; nessuna formula esposta, tabella o nota nello scope. Le tre figure sono composte da grafica e testo vettoriali del PDF. Nelle loro aree non esistono raster incorporati; i soli quattro raster della pagina sono marchi GU DeviceGray da 208 × 208 px fuori dallo scope. I ritagli a 600 dpi sono quindi render fedeli della sorgente vettoriale, non ricampionamenti dichiarati come dettaglio nativo. I tre asset collegati dal Markdown sono assenti.

## Elenco unico delle non conformità

| ID | File e posizione | Fonte e prova | Attuale | Proposta | Classe | Effetto | Decisione |
|---|---|---|---|---|---|---|---|
| NC-C-01 | Tre rubriche NTC, riga 3 dei tre file; tre rubriche Circolare, righe 23, 11, 11 | NTC 49, 56, 61; CIRC 46, 54, 76; ritagli rubriche in prove [prova 1](./prove/ntc-p49-rubrica-3.2-bbox-65-225-230-252-600dpi.png); [prova 2](./prove/ntc-p56-rubrica-3.3-bbox-65-88-245-115-600dpi.png); [prova 3](./prove/ntc-p61-rubrica-3.4-bbox-68-86-250-114-600dpi.png); [prova 4](./prove/circ-p46-rubrica-3.2-bbox-68-502-235-555-600dpi.png); [prova 5](./prove/circ-p54-rubrica-3.3-bbox-68-343-245-403-600dpi.png); [prova 6](./prove/circ-p76-rubrica-3.4-bbox-68-88-265-135-600dpi.png) | Maiuscole/minuscole difformi; nelle tre rubriche CIRC è aggiunto anche il punto dopo C3.x | Riprodurre le sei rubriche stampate, in maiuscolo e senza punto terminale nei numeri C3.x | ERR-MD | sola presentazione | da_approvare |
| NC-C-02 | 3.2, righe 13-15 e 42-44 | NTC 49 e CIRC 47; prove degli elenchi [prova 1](./prove/ntc-p49-elenco-parametri-bbox-68-340-528-425-600dpi.png); [prova 2](./prove/circ-p47-elenco-parametri-bbox-68-165-415-220-600dpi.png) | Sei righe rese come elenco puntato; nelle tre NTC è aggiunto anche il separatore «—» | Rendere sei capoversi senza marcatore; conservare «=» soltanto nelle tre righe CIRC | ERR-MD | sola presentazione | da_approvare |
| NC-C-03 | 3.2, riga 46 | CIRC 47, prova dallo-ingv-simboli [prova 1](./prove/circ-p47-dallo-ingv-simboli-bbox-68-216-528-275-600dpi.png) | «fornita dall’INGV», INGV non evidenziato | «fornita dallo INGV», con INGV in grassetto | ERR-MD; anomalia di fonte A da conservare | contenuto e presentazione | da_approvare |
| NC-C-04 | 3.2, riga 48 | CIRC 47, prova dallo-ingv-simboli; font e posizioni vettoriali riscontrati [prova 1](./prove/circ-p47-dallo-ingv-simboli-bbox-68-216-528-275-600dpi.png) | F_o e T_C^* | F_O e T*_{C}, come stampati nel solo capoverso | ERR-MD; anomalie di fonte A da conservare | contenuto | da_approvare |
| NC-C-05 | 3.2, righe 54, 58, 62 | CIRC 47; tre ritagli delle didascalie [prova 1](./prove/circ-p47-didascalia-C3.2.1a-bbox-122-435-475-452-600dpi.png); [prova 2](./prove/circ-p47-didascalia-C3.2.1b-bbox-122-550-475-567-600dpi.png); [prova 3](./prove/circ-p47-didascalia-C3.2.1c-bbox-120-667-478-688-600dpi.png) | «Fig.» e descrizione non corsiva; nella b, F_o | «Figura», descrizione corsiva; nella b, Fo a corpo pieno | ERR-MD | presentazione; contenuto per il simbolo della b | da_approvare |
| NC-C-06 | 3.2, collegamenti alle righe 52, 56, 60 | CIRC 47; tre ritagli vettoriali 600 dpi [prova 1](./prove/circ-p47-fig-C3.2.1a-vettoriale-bbox-165-337-425-437-600dpi.png); [prova 2](./prove/circ-p47-fig-C3.2.1b-vettoriale-bbox-165-450-425-552-600dpi.png); [prova 3](./prove/circ-p47-fig-C3.2.1c-vettoriale-bbox-165-565-425-668-600dpi.png) | I tre PNG collegati non esistono | Creare i tre PNG ai percorsi già collegati copiando i tre ritagli vettoriali indicati nella lista JSON | ERR-MD | contenuto/apparato assente | da_approvare |
| NC-C-07 | 3.2, riga 9 | NTC 49; dettaglio 600 dpi e testo vettoriale leggibile [prova 1](./prove/ntc-p49-simboli-inline-bbox-65-280-535-353-600dpi.png) | a_g e S_e(T) fuori dai delimitatori matematici, quindi con trattino basso letterale | $a_g$ e $S_e(T)$ | ERR-MD | sola presentazione | da_approvare |

I target e i registri sono rimasti invariati. G5, G6 e correzioni non sono stati avviati.

## Addendum dopo le correzioni approvate, G5

Data: 2026-09-12. Firma: Codex / CDX.

Sandro ha approvato l’intera lista. Il diff completo g5-r01/diff-correzioni.patch corrisponde esattamente alle 15 sostituzioni testuali approvate nei sette gruppi NC-C-01 - NC-C-07 e non contiene modifiche estranee. Le tre copie PNG corrispondono byte per byte alle sorgenti approvate: SHA-256 bc5015b5b0bb01a17c782508008020b0977534aa3f2443d96cceccb3acc48d89, 03117c3864652938271a0b58d8c60ec1a67781758cf8af4308bca562e0c88604, 1904ce4544355d7485f7c6deefa385759f7b66bcada41709efe493b2503ad182.

La depurazione contiene integralmente le tre introduzioni: 71 righe logiche, assegnate primariamente a b01 nelle righe 1-58 e a b02 nelle righe 59-71, senza lacune né sovrapposizioni; la riga 58 è il separatore vuoto fra i blocchi. Le sole esclusioni aggiuntive sono le due identificazioni editoriali della Circolare già giudicate fuori dal testo normativo.

La resa canonica è stata controllata integralmente: tre pagine per b01 e una per b02. Testo, rubriche, simboli inline, grassetti e corsivi sono leggibili; le tre figure e didascalie sono presenti, complete e senza tagli; non risultano caratteri mancanti, sovrapposizioni o tag resi impropriamente. Il salto sulla terza pagina di b01 lascia spazio bianco ma non perde contenuto.

Lo snapshot-finale.json elenca tre target e tre asset con dimensioni e hash tutti riscontrati sui file vivi; il suo SHA-256 è b28f0f73ae8a2a8695fabaafc8f15dd7bf5e1c8bf94c1aa4824f753fd2c06a06.

Esito: G0-G5 OK, zero rilievi residui. G6 non avviato. Nessuna modifica apportata da C ai target o ai registri in questo controllo.

Controllo meccanico CDX: 15 sostituzioni univoche sui tre Markdown iniziali e tre sorgenti PNG presenti; hash dei target invariati. NC-C-07 confermata sul ritaglio 600 dpi dei due simboli. Nessuna correzione applicata. [Lista applicabile](./lista-correzioni.json).
