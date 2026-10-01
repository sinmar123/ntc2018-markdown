---
scope_id: ntc2018-3.4.1
data: 2026-09-04
stato: VC-OK
markdown_sha256: aad946d48ddbf921a92851e8568a813e4df69a072ce05a9c360f6e2b95a46687
fonte_ntc_sha256: dda1e397d56d71aa0f5bc457c3ba9b77064a468699dfc37bd056ac6c47105a46
fonte_circolare_sha256: f7c3b8d1f443aadb6b3e020b6b6c19813683492ecaadd2c15bf6bf1939aaed7c
---

# Verbale di verifica di conformità - NTC 2018 § 3.4.1

Perimetro: `cap03/3.4.1-neve-carico-della-neve-sulle-coperture.md`, § 3.4.1 NTC a pagina fisica 61 e § C3.4.1 Circolare a pagina fisica 76. Lo scope comprende due rubriche, tre capoversi narrativi, una formula numerata `[3.4.1]`, un blocco `dove:` con quattro definizioni e sette rinvii a paragrafi. Non contiene tabelle, figure o asset; i §§ 3.4.2/C3.4.2 e gli apparati successivi sono esclusi.

Le due fonti ufficiali congelate sono state ricalcolate e coincidono con gli hash registrati. G0 ha confermato i confini naturali. G1 ha identificato entrambi gli atti, distinto la funzione applicativa della Circolare e verificato le fonti ufficiali correnti. Il D.M. 9 marzo 2023, n. 52, incide sull'articolo 2 del decreto e sui punti 11.4.2 e 11.5.2, non sui §§ 3.4.1/C3.4.1. Non sono state individuate modifiche successive incidenti sullo scope alla data del controllo; resta la normale riserva sulla disciplina transitoria applicabile alla singola opera.

G2-G5 hanno riconciliato integralmente inventario, prosa, formula, definizioni, rinvii, struttura, navigazione e resa. Sullo snapshot iniziale sono state individuate due famiglie `ERR-MD`: cassa non fedele della rubrica NTC e cassa non fedele con punto aggiunto dopo `C3.4.1` nella rubrica Circolare. Un correttore P1 distinto ha applicato esclusivamente le due correzioni congelate; la rigenerazione dell'indice interno ha riallineato soltanto la voce derivata della Circolare, lasciando invariata l'àncora. Il P0-D post-correzione ha confermato G3 `OK` e l'assenza di altre variazioni normative.

G4 è `OK`: la formula riproduce esattamente membro sinistro, uguaglianza, quattro fattori, tre operatori di moltiplicazione, indici, lettera greca, maiuscole/minuscole, ordine e tag. Le quattro definizioni mantengono l'associazione uno-a-uno con i simboli e la punteggiatura della fonte. Il render finale mostra correttamente il tag `[3.4.1]`. Tabelle, figure, didascalie e asset interni allo scope sono 0/0.

Le normalizzazioni applicabili sono quelle dell'elenco unico `verifica-conformita/normalizzazioni-dichiarate-NTC2018.md`. Nel presente scope sono state registrate soltanto cinque famiglie ammesse: spaziatura e riflusso, ricomposizione della sillabazione `co-`/`pertura`, quattro spazi omessi dopo `§`, blocco `dove:` reso come elenco e variante Unicode dell'apostrofo. Nessuna tocca cifre, coefficienti, pedici, operatori, tag o significato normativo. Non risultano `AF` né `AF-COR`.

Il G6 R01 cieco è stato eseguito da un P2 fresco `gpt-5.6-sol` xhigh. Prima di rendere disponibile il Markdown sono stati prodotti e congelati inventario, esito provvisorio e criterio fonte-prima, poi ricalcolati dal coordinatore. Il pacchetto di confronto ha conservato l'integrità di 10/10 input; il controllo ha coperto 14/14 unità e ha chiuso con zero `ERR-MD`, zero `ERR-AUDIT` e zero `DUBBIO`. Esito G6 `OK` al primo giro.

Il G7 ha impiegato prima un P0-D `gpt-5.6-luna` medium per il ricalcolo deterministico e poi un P2 fresco `gpt-5.6-sol` xhigh. Il manifest `verifica-conformita/manifest-sha256-ntc2018-3.4.1-2026-09-04.txt` contiene 38/38 record verificati, zero duplicati e zero mismatch; SHA-256 del manifest `bc9e316c0c7137b55648b22394ebd25a36ce9761b58808e063690d4790d7db33`. Il P2 ha ripetuto il confronto dei ritagli a 600 dpi col testo canonico, verificato il diff, ispezionato il render di una pagina e confermato separazione dei ruoli, catena G0-G6 e assenza di residui. Esito G7 `OK`; rapporto P2 SHA-256 `87a34ec9bd71193e8d4582a79ced07dc01f6d471757ac970c21161cfeb2db7ed`.

Controlli finali: indici interni, 311 file e 1.754 collegamenti, `OK`; linter del registro, zero errori e zero avvisi; sei collegamenti locali del target risolti; zero U+FFFD; UTF-8 con BOM e soli LF; render finale di una pagina controllato integralmente.

Tutti i gate G0-G7 sono `OK`. Promozione locale a `VC-OK al 2026-09-04` sul solo snapshot `aad946d48ddbf921a92851e8568a813e4df69a072ce05a9c360f6e2b95a46687`. Il master generale del corpus resta coerentemente `VC-DA-FARE`, perché la chiusura del singolo file naturale non conclude il corpus. I controlli indipendenti sono stati eseguiti da agenti AI; non è inclusa una revisione umana integrale.

Evidenze: `_tmp_render/cap03/vc-3.4.1-20260904/`.

Firma della redazione: CDX (Codex).
