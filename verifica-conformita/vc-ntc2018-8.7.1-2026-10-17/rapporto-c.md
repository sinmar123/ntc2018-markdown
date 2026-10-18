# Rapporto C, § 8.7.1 (Norma e Circolare), confronto iniziale

Firma: GBOT-verifica-ntc (C), 2026-10-17. Esecutore del confronto: Grok Build sul W520 (modello `grok-4.6-build`), tre sessioni a contesto separato. Procedura VC-NTC/9, hash `14084c23fd8a0563515a906d0192b93dbd419ac0a8a2a6f8a3715938bedde82f`. Catalogo `add1873d309b44930b8caccf8dd5ed3714926108a106230de35133a8a76e239e`. Base git `92a449e`. Target SHA-256 `643c7e83faec95dcde4cf74be90976190b0c122d46b50d88c12df50f03ae2a45`.

G0. Riga `8.7.1`, file `cap08/8.7.1-progettazione-interventi-costruzioni-in-muratura.md`. Norma: pagine fisiche 297-298, da `8.7.1.` a prima di `8.7.2.` (il registro indica solo 297: ERR-AUDIT del registro, da correggere alla registrazione). Circolare: pagine fisiche 270-283 (stampate 266-279), da `C8.7.1` a prima di `C8.7.2`; pagine 270 e 283 condivise con testo escluso. Il registro elenca 270-272, 274-277, 279, 282-283: mancano 273, 278, 280, 281, che contengono testo dello scope. Fuori: 8.7, 8.7.2-8.7.5, C8.7.6, C8.8. Lo scope occupa 16 pagine, sopra la soglia di 15 del § 2 oltre la quale si propone un sotto-scope: segnalato a Sandro, non diviso.

G1. Ricognizione piena del 2026-10-13 riusata (dentro i trenta giorni). Ricontrollo mirato del 2026-10-17: le tre schede GU (D.M. 17/01/2018, Circolare 7/2019, D.M. 9/3/2023) sono identiche byte per byte al ricontrollo del 2026-10-16 (`g1/`). Impronte dei PDF congelati invariate.

G2-G4. Tre blocchi: A righe 1-164 (Norma e Circolare 270-274), B righe 165-323 (274-279), C righe 324-472 (279-283). Norma: conforme parola per parola, rubrica compresa. Circolare: 18 formule numerate, nessuna tabella, nessuna figura, una nota. La pagina 281 non ha strato di testo: letta sul raster nativo 2221×3106, impronta `d860503c1a902573839c9451c86db2d4b884fc058ea1cc75e547b5807397d406`. Esito del confronto iniziale (v1): 198 voci applicabili, 21 sostanziali, 3 dubbi, 22 anomalie della fonte, 5 voci respinte o assorbite. Esito corrente (v3): 206 voci applicabili, 21 sostanziali e 185 di forma, 4 dubbi, 22 anomalie della fonte, 5 voci respinte o assorbite. Elenco in [lista-correzioni-c.md](lista-correzioni-c.md).

Controllo a campione di C. Tutte le 18 formule viste a 600-1200 dpi; ricontrollati sulla pagina i punti sostanziali B-01, B-07, B-11, B-12, B-15, B-18, B-75 e i pedici di A-41: confermati. Aggiunte G-01...G-09 (sfuggite ai blocchi): grassetto «Nel caso di muratura regolare» (la nota di C-15 che lo dava in tondo è errata), virgola dopo μ a p. 281, e∗ centrato in [C8.7.1.8]-[C8.7.1.9], a e S in tondo, V maiuscola in [C8.7.1.14], Φ e min corsivo in [C8.7.1.15]. Respinte C-24 e C-25: «[4]» e «**Nota 4.**» sono la convenzione dei file VC-OK 8.5.4 e 8.4. Assorbite B-64, B-66, B-76. Uniformate le lettere degli elenchi (C-50...C-55 le conservano come A-10). C-18 riclassificata DUBBIO. Il confronto di parole fra target e target dopo la lista mostra solo le modifiche attese.

Revisione v2 (2026-10-17). Confronto automatico con il corpus structural-codes (commit 5698a0e; script locale, nessun LLM; costo nullo), con ogni esito verificato sulla Gazzetta. Aggiunte SC-01…SC-07 (capoverso a p. 272; elenchi «dove:» di [C8.7.1.4] e [C8.7.1.7]); modificate C-16 (elenco completo del «dove:» di [C8.7.1.16], senza i «;» non stampati e con «.» dopo «altezza del pannello»), C-32 (prima US di «nelle US di testata» in grassetto), B-68…B-70 (marcatori «1)», «2)», «3)» conservati); nuovo dubbio D-01 («elasto-/fragile» a fine riga, p. 280). Esiti della prova in /workspace/vc871-sc/ sul box.

Revisione v3 (2026-10-17). Aggiunta SC-08 su richiesta di Sandro: L in tondo ($\mathrm{L}$) nel «dove:» di [C8.7.1.7], dove la fonte la stampa in PalatinoLinotype-Roman; nella formula [C8.7.1.7] e nella voce λ la L è in corsivo e resta invariata.

Approvazione. Sandro ha approvato la lista v2 il 17/10/2026 alle 13:21 (ora di Roma), con i dubbi A-41, C-18, C-26 e D-01 a testo invariato, e ha chiesto SC-08 (v3). Ricontrollo: tutte le 206 voci si applicano in un solo punto sul file a 92a449e.

Stato: G0-G4 svolti; lista v3 approvata, da applicare con `cura.py`; nessuna correzione ancora applicata al corpus; G5-G7 non avviati.

Consumi Grok Build (dal JSON della CLI): A 5,82 M token, 3,73 USD; B 10,33 M, 6,45 USD; C 8,27 M, 5,15 USD; totale circa 24,4 M token (in gran parte cache), 15,33 USD.

## Integrazione CDX: applicazione approvata e G5

Firma: CDX, 2026-10-17. Subentro autorizzato da Sandro per G5-G7.

La lista v3 approvata, SHA-256 `989e47a02697e92a222f40785eb885aab597620e7922b3fa578e92e9f87f8fa8`, è stata applicata con `vc-supporto.py applica-lista`: piano di 206 voci su un solo file e applicazione `OK`. Lo SHA-256 prima della rigenerazione degli indici è `d238498989cf417dd1176f8bc6b0f52c5e2622529f0103dbe15441991a89836c`; `verifica-lista` sulla base `92a449e` ha restituito `OK`, uguaglianza a indici esclusi e nessun file estraneo. Gli indici sono stati rigenerati e verificati; il target finale ha SHA-256 `09eab0335ca26594b29ea19f279acf1da8496550f70883b55fa6695a4b0ba6c8`.

G5. Lo scope composto conserva l'ordine Norma poi Circolare; il testo depurato ha 662 righe. La mappa assegna una sola volta tutte le righe e le 16 pagine reali a quattro blocchi primari, senza lacune o sovrapposizioni e senza spezzare formule, definizioni o elenchi. Il superamento di una pagina della soglia consigliata di 15 era emerso in G0 ed era stato segnalato a Sandro; lo scope già avviato resta intero. I 25 link del file non hanno destinazioni o ancore mancanti; la verifica globale degli indici ha superato 311 file e 1754 collegamenti interni.

Il render canonico del testo normativo depurato è di 18 pagine, SHA-256 `a4749131516e679e75b008fbebe1c96539060fb7f0952ba81211985c14d49622`. Tutte le pagine sono state osservate: zero tagli, sovrapposizioni e caratteri mancanti; presenti e leggibili i 18 tag `[C8.7.1.1]`-`[C8.7.1.18]`, nessun tag tondo e nessuna didascalia automatica. Il tentativo diretto sul file vivo è stato respinto dalla profondità dell'indice interno; l'indice è stato verificato separatamente e il render depurato rimuove solo apparati di navigazione. G0-G5: `OK`; rilievi aperti: zero.

## Integrazione CDX: esito G6

Firma: CDX, 2026-10-17.

Il giro G6 integrale ha coperto 180/180 ID su tutte le 16 pagine e le 662 righe depurate. I quattro inventari fonte-prima sono stati validati prima della rivelazione; dopo il congelamento, `rivela`, `verifica-pacchetto` e `valida-g6` hanno dato esito meccanico positivo per ogni blocco. Il primo tentativo di mappa è stato respinto prima della rivelazione perché pagina PDF e righe non coincidevano; nessun V aveva ancora visto il target e `giro_g6` era rimasto 0. La seconda preparazione costituisce il giro 1.

Esiti: b01 `KO`, 55 ID e 4 rilievi; b02 `OK`, 25 ID e nessun rilievo; b03 `KO`, 53 ID e 3 rilievi; b04 `KO`, 47 ID e 7 rilievi. Totale: 13 `ERR-MD`, 1 `ERR-AUDIT`, zero `DUBBIO`. I rilievi riguardano la resa run-in di rubriche, due rubriche prive del grassetto-corsivo della fonte, quattro unioni o mappature di capoversi e la resa del richiamo e della struttura della nota 4. Le prove fonte aggiuntive ad alta risoluzione hanno invece confermato i glifi delle formule controllate e non hanno prodotto rilievi ulteriori.

L'osservazione G5 aveva escluso tagli, sovrapposizioni e glifi mancanti; il confronto indipendente G6 ha rilevato differenze strutturali e tipografiche rispetto alla fonte, che sono un controllo distinto e restano aperte. Nessuna correzione è stata applicata, nessuna seconda tornata è stata avviata e `giro_g6` resta 1. G6: `KO`. G7 non eseguito perché la procedura lo ammette soltanto a zero `ERR-MD`, zero `ERR-AUDIT` e zero `DUBBIO`. La riga 8.7.1 resta `IN-CORSO` in attesa della decisione di Sandro.

## Integrazione GBOT-verifica-ntc: rilievi G6, correzioni e controllo delle modifiche

Firma: GBOT-verifica-ntc (C), 2026-10-18.

Giudizio di C sui 14 rilievi, controllati sulla Gazzetta e presentati a Sandro in un PDF con ritagli: 2 fondati sul testo (8, 9: corsivo mancante nelle rubriche di sesto livello, errore della lista C-19); 7 solo di resa (1-3, 5, 10-12: rubriche di livello 4-5 run-in nel renderer); 1 documentale (4); 2 non fondati (6, 7); 2 da decidere sulla convenzione della nota (13, 14). Decisioni di Sandro del 2026-10-18: vedi la scheda e `correzioni-g6/esito-rilievi-g6-r1.json`.

Correzioni: 4 voci in `correzioni-g6/lista-correzioni-g6.json`, applicate con `applica-lista`; indici rigenerati; `verifica-lista` della lista v3 più g6 sulla base `92a449e` OK (`correzioni-g6/verifica-lista.json`). Snapshot finale `5c466acd11ce6c074f28ba1b022d78fff5930d5829f378701493ac52b98ad57c`. Renderer comune con `-V block-headings` e contatore delle note allineato a `[^n]`; resa del testo depurato di 18 pagine, `correzioni-g6/esito-resa.json`. Catalogo: voce 25, copia congelata `catalogo-congelato-v25.md`.

Controllo delle modifiche del § 8 sul pacchetto di `pacchetto-modifiche` (solo b04 cambia nel testo): V Codex gpt-6.1-sol, esito OK; prova comparativa gpt-6-luna con un ERR-AUDIT non fondato; seconda prova comparativa gpt-5.6-terra, lanciata da Sandro, esito OK senza nuovi rilievi (`g6-modifiche/esito-terra.json`). Dettagli in `g6-modifiche/registro-g6-modifiche.json`. G6: OK, zero `ERR-MD`, zero `ERR-AUDIT`, zero `DUBBIO`.

Registro: il G7 tentativo 1 (Codex gpt-6.1-sol, 2026-10-18 alle 13:28) è stato `KO` per il solo rilievo G7-REGISTRO-8.7.1, l'ERR-AUDIT delle pagine rilevato in G0 e lasciato nel TODO (`G7-tentativo-1-KO.json`). Pagine della riga 8.7.1 nel CSV corrette il 2026-10-18 con il nuovo comando `vc-supporto.py pagine` (piano, `--applica`, lint OK), su decisione di Sandro delle 13:47: NTC da 297 a 297-298, Circolare da 270-272, 274-277, 279, 282-283 a 270-283. Valori riaccertati sui PDF ufficiali: rubrica `8.7.1.` a p. 297 e `8.7.2.` a p. 298; `C8.7.1` a p. 270 e `C8.7.2` a p. 283; p. 281 solo raster, interna all'intervallo (`registro-pagine/`). Rilievo chiuso; segue un G7 nuovo, tentativo 2.
