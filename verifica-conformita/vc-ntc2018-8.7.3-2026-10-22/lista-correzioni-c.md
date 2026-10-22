# § 8.7.3 e C8.7.3: lista delle correzioni proposte (v1)

Firma: GBOT-verifica-ntc, 22/10/2026. Procedura VC-NTC/10.

**Stato.** In attesa della decisione di Sandro. Nessuna correzione applicata.

File: `cap08/8.7.3-progettazione-interventi-costruzioni-miste.md`, base git `33f9a3d` (ramo `cdx/vc-8.7.3-261022`). Pagine fisiche: Norma 298; Circolare 289. PDF ufficiali in `verifica-conformita/fonte-ufficiale/`, SHA-256 `dda1e397…5a46` (NTC) e `f7c3b8d1…ed7c` (Circolare).

Motori: confronto integrale di Codex `gpt-5.6-terra` (CDX-terra, reasoning high, sola lettura), in due passaggi, il secondo mirato a formule, simboli, esponenti, pedici, numeri, enfasi e capoversi (`confronto-iniziale/codex-terra.json`, 40.218 token). Candidati di struttura con `strumenti/vc-struttura-fonte.py` (`confronto-iniziale/candidati-struttura-*.json`). Controllo di GBOT: confronto parola per parola fra il livello di testo della Gazzetta e il Markdown, Norma e Circolare, e lettura dei ritagli a 400 dpi. Codex `gpt-6.1-sol` non attivato: nessun dubbio.

Totale voci: 2, entrambe di forma, entrambe nella Circolare. Voci sostanziali: 0. Dubbi: 0. Anomalie della fonte conservate: nessuna. Nel perimetro non ci sono formule, simboli, tabelle, figure né note. Il testo della Norma (rubrica, capoverso introduttivo, tre voci di elenco con i trattini resi come elenco puntato, capoverso finale) coincide con la Gazzetta.

Dopo l’applicazione l’indice interno va rigenerato con `genera-indici-interni.py` (cambia la rubrica C8.7.3).

## Voci di forma

| ID | Riga | Pagina | Categoria | Attuale | Proposto | Trovata da | Nota |
|---|---|---|---|---|---|---|---|
| F-01 | 32 | C 289 | rubrica | `### C8.7.3. Costruzioni miste` | `### C8.7.3 COSTRUZIONI MISTE` | CDX-terra; confermata GBOT | Numero senza punto finale; titolo in maiuscoletto, reso in maiuscolo (catalogo, voce 23). |
| F-02 | 34 | C 289 | capoverso | `sia favorevole. L’analisi statica non lineare` | `sia favorevole.⏎⏎L’analisi statica non lineare` | CDX-terra; confermata GBOT e dallo script | La fonte apre un nuovo capoverso (y 549,3 pt); la voce 1 non copre l’unione dei capoversi. |

Proposta GBOT: approvare F-01 e F-02.
