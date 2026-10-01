# Verbale VC-NTC/3, § 3.4.5 COEFFICIENTE TERMICO

Data di chiusura: 2026-09-10  
Firma interna: Hermes NTC-VC / HRM  
Ruolo di coordinamento: C

## 1. Scope e fonti

La verifica riguarda esclusivamente `cap03/3.4.5-neve-coefficiente-termico.md`, § 3.4.5 NTC e § C3.4.5 Circolare.

- NTC, pagina fisica 63, PDF SHA-256 `dda1e397d56d71aa0f5bc457c3ba9b77064a468699dfc37bd056ac6c47105a46`.
- Circolare n. 7/2019, pagina fisica 81, PDF SHA-256 `f7c3b8d1f443aadb6b3e020b6b6c19813683492ecaadd2c15bf6bf1939aaed7c`.
- Snapshot target giudicato: `3541307932ff82abd016c34b325b6bb11877315ae8cc1db320b57d925cb7ebd5`.

Confini: dalla rubrica `3.4.5. COEFFICIENTE TERMICO` alla chiusura `Cₜ = 1.` per la NTC; dalla rubrica `C3.4.5 COEFFICIENTE TERMICO` alla chiusura `neve al suolo.` per la Circolare. Tabelle, figure, note e asset propri: nessuno.

## 2. Vigenza

G1 è stato svolto il 2026-09-09. Le schede ufficiali della Gazzetta Ufficiale hanno confermato il D.M. 17 gennaio 2018 e la Circolare 21 gennaio 2019 n. 7. Il D.M. 9 marzo 2023 interviene sui punti 11.4.2 e 11.5.2 e non sul § 3.4.5. Le ricerche documentate non hanno individuato modifiche, rettifiche o errata-corrige pertinenti al perimetro. G1: `OK` alla data della ricognizione.

## 3. Normalizzazioni e anomalie

Normalizzazioni applicate nel confronto V: N1, N2, N3 e N11 del catalogo congelato. La rettifica append-only G7 ha precisato che apostrofi diritti/curvi ricadono in N2 e ritorni a capo o parole spezzate in N1. Non risultano anomalie della fonte né correzioni della fonte.

## 4. Correzioni del target

Il ruolo E separato ha applicato una lista chiusa:

- rubrica NTC portata alla cassa della fonte;
- `C` e pedice `t` resi romani;
- rubrica Circolare allineata per cassa e assenza del punto dopo il numero;
- rimosso il punto non presente dopo `1 W/m²K°`;
- ripristinata la separazione fra il primo e il secondo capoverso della Circolare.

Il runtime effettivo di E è stato `gpt-5.6-sol`, provider `openai-codex`, ragionamento `high`, in conversazioni separate. C non ha scritto direttamente le correzioni normative.

## 5. G0-G5 e resa

G0-G4 sono `OK` dopo ricollazione. Gli indici sono stati rigenerati e verificati su 311 file e 1754 collegamenti interni. Il linter del registro ha restituito 311 righe, 11 colonne, zero errori e zero avvisi; la vista XLSX è risultata conforme al CSV.

Il G5 R01 ha individuato la fusione di due capoversi. Dopo la correzione distinta, il G5 R02 ha verificato PDF e PNG sullo snapshot finale:

- PDF SHA-256 `9ea070d117aa890c7509f0bff88da150e4de7fec337ca154f9370215be972dbc`;
- PNG SHA-256 `28063269a8e3f5ad5173b2926f20308dc14794e315d4c798814788def6ce2b95`.

Rubriche, prosa, pedice, valori, unità, glifi e tre capoversi della Circolare sono leggibili e conformi. G5 R02: `OK`.

## 6. G6 indipendente

V ha operato nel container separato del canale di verifica, privo del montaggio del workspace. La fase fonte-prima R03 è iniziata nel contesto fresco `20260909_165403_00ba4e`, senza accesso al target; confronto e fasi successive hanno ripreso la stessa sessione per la continuità prescritta. C non ha svolto né simulato il ruolo V.

L'inventario comprende 11 elementi, 4 NTC e 7 Circolare, con 4 esclusioni e nessun dubbio. V ha confrontato 11/11 ID con fonti, `testo.md`, PDF e PNG. Il giro R02 aveva un `ERR-AUDIT` per resa target assente dal manifest. R03 ha chiuso quel rilievo e ha confermato zero `ERR-MD`, ma ha aperto un `ERR-AUDIT` sulla sola delimitazione descrittiva di `CIRC81-PRO-001`.

C ha adjudicato il difetto come errore della sola mappatura, con target e input invariati. La rettifica append-only ha sostituito, ai soli fini descrittivi, gli estremi `«Valori del coefficiente»` - `«edifici»` con `«L’adozione di valori»` - `«linea generale.»`. V ha verificato il delta e chiuso il rilievo. G6: `OK`, giro 2/3, zero residui. Inventario, congelamento, manifest e rapporto G6 originario sono rimasti immutati.

## 7. G7 separato

Il giudizio G7 è stato emesso da V nella sessione isolata continuativa del G6, distinta dal coordinatore. I passaggi R01-R03 hanno aperto soltanto rilievi documentali su copia procedurale, confine di scope scritto nel rapporto iniziale, numeri delle normalizzazioni e chiusura esterna dell'impronta. Le rettifiche sono append-only. R04 ha chiuso tutti i rilievi; R05 ha verificato la ricollocazione portabile delle stesse evidenze; R06 ha verificato l'aggiunta append-only del percorso vivo del target, richiesta dalla precondizione automatica di rilascio, con hash invariato.

Giudizio finale:

- G0-G7: tutti `OK`;
- rilievi aperti: nessuno;
- manifest finale R02: 67 file, integrità `OK`, SHA-256 `e338cac1d900f68473c48e30f7dfe11a6070cd4abf4649d8faf39415759a4586`;
- giudizio G7 SHA-256 `bafadafecdc3001439ba5d26523e72a0fd6aab1195e79d23159aa7d6cf1d937e`.

## 8. Metodo e runtime

- Procedura: VC-NTC/3, SHA-256 `4bd4440a6f9b204338e97ecf78c9bb74ab0d9e04f7478b9c97c436c62e817c7c`.
- Canone G6: 8705 byte, SHA-256 `546023234aec119b42de98bb7499187fdb8445f1ac83e5b32743e13174c1eb44`.
- C: `gpt-5.6-sol`, provider `openai-codex`, ragionamento `high`, 3 contesti, 3 tentativi, 1 compressione runtime registrata.
- E: `gpt-5.6-sol`, provider `openai-codex`, ragionamento `high`, conversazioni separate.
- V: `gpt-5.6-sol / openai-codex / Hermes Agent CLI`; il livello di ragionamento non è esposto negli esiti. Sessione R03-G7 `20260909_165403_00ba4e`.
- Token e costo: non disponibili, non stimati.

## 9. Limiti dichiarati

Nel G7 finale V non ha ricalcolato autonomamente le impronte: ha importato hash e integrità dall'output dello script conservato nell'evidenza esterna. Non ha rieseguito G6, inventario, render, confronto o ricognizione di vigenza durante la sola verifica della ricollocazione portabile. Tali attività erano già documentate e giudicate nei gate precedenti.

## 10. Esito

Lo snapshot `3541307932ff82abd016c34b325b6bb11877315ae8cc1db320b57d925cb7ebd5` ha superato G0-G7 secondo VC-NTC/3. Non risultano `ERR-MD`, `ERR-AUDIT` o `DUBBIO` aperti. Sono presenti manifest, giudizio G7 e dossier definitivo verificati.

Esito di rilascio predisposto: `VC-OK` sul solo § 3.4.5 e sullo snapshot sopra indicato.

Prossima azione: nessuna sul file; non aprire altri scope senza autorizzazione.
