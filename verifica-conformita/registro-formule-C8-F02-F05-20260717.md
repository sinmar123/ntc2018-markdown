# Registro audit formule C8 — lotti F02, F03, F04, F05 (2026-07-17)

## Perimetro

Formule esposte numerate della Circolare C8, 44 in totale:
- **F02** = C8.7.1.1 … C8.7.1.16 (16 formule) — meccanismi locali/cinematismi muratura, pp. file 271-283
- **F03** = C8.7.2.1 … C8.7.2.13 con coppia 7a/7b (14) — capacità c.a. edifici esistenti, pp. 283-289
- **F04** = C8.7.4.1 … C8.7.4.8 con coppia 7a/7b (9) — incamiciatura/confinamento, pp. 289-295
- **F05** = C8.8.5.1 … C8.8.5.5 (5) — ponti esistenti, analisi e verifiche, pp. 300-302

Fonte: `raw/Circolare-7-2019-NTC.pdf`, SHA-256 `f7c3b8d1f443aadb6b3e020b6b6c19813683492ecaadd2c15bf6bf1939aaed7c`.
Pagine renderizzate a zoom 3x in `_tmp_render/cap08/conformita-formule-20260717-r01/fonte/pagina-<n>.png`.
Markdown: `cap08/8-esistenti.md`.
- SHA pre-audit formule: `da2bf432…` (= chiusura T05)
- SHA post-correzione ERR-MD-01: `17de54431aa8c589f9b4c0667d0d84711d0345be8f81e711d8dda52af0bdbcb8`

## Metodo

Protocollo `VC8-G4-TF` (skill `controllo-serrato-ntc2018`). Doppio passaggio indipendente alla cieca sul solo PDF, su modelli diversi; ricostruzione LaTeX; confronto con il markdown vivo (blocchi estratti da `estrai_formule_md.py`); adjudicazione sul PDF da parte di CC; recheck fresco a contesto pulito. Caccia esplicita agli errori OCR ricorrenti (ν/v, ρ/p, τ/t, χ/x, φ/Φ, γ/y, l/1/I, O/0, meno/trattino, ≤/<).

- **Passaggio A**: Opus 4.8 (modello di sessione), un agente per lotto.
- **Passaggio B**: Sonnet, un agente per lotto.
- **Arbitro**: CC (Opus 4.8), verifica visiva diretta sui render di pagina (in particolare pagina-285 per l'errore di segno).
- **Recheck fresco**: Opus 4.8, contesto pulito, verifica di valore su C8.7.2.1 + 4 formule complesse (C8.7.2.8, C8.7.1.5, C8.7.4.6, C8.8.5.5) → esito in `recheck-formule-C8-20260717.md`.

Le trascrizioni LaTeX integrali dei passaggi A e B (con le note sulle anomalie di fonte) sono registrate nel transcript della sessione CC del 2026-07-17 (journal); questo verbale ne riporta metodo, esiti e ogni difformità adjudicata.

## Esito confronto A vs B

Concordanza piena A/B su struttura e simboli di tutte le 44 formule (frazioni, pedici/apici, lettere greche, sommatorie con estremi, operatori, disuguaglianze). Le uniche divergenze A/B sono di trascrizione tipografica minore (es. `(4)` vs apice unicode; punto vs virgola quando ambiguo), risolte sul PDF.

## Difformità di VALORE rilevata e corretta (ERR-MD)

| # | Formula | Fonte | Markdown pre | Correzione |
|---|---|---|---|---|
| ERR-MD-01 | C8.7.2.1 | esponente della parentesi quadra `[ … f_c]` **positivo 0,225** (verificato su pagina-285, nessun segno meno) | esponente **−0,225** (negativo) | rimosso il segno meno: `^{-0{,}225}` → `^{0{,}225}` |

È l'**unico errore di valore** in 44 formule. Un esponente di segno opposto alterava il valore della rotazione ultima θ_u (formula di capacità dei meccanismi duttili c.a.): errore sostanziale, intercettato dal doppio passaggio indipendente.

Recheck fresco sulla formula corretta e sulle 4 formule complesse: **5/5 CONFORME** al valore.

## Policy tipografica adottata (scelta di Sandro, 2026-07-17): "uniforme e leggibile"

Le seguenti differenze fonte↔markdown NON sono errori di valore e restano come normalizzazioni documentate (NORM):

1. **Separatore decimale**: la fonte C8 mescola punto e virgola in modo incoerente, a volte nella stessa formula (es. C8.7.2.1: numeri con virgola ma esponente "0.225" col punto; C8.7.1.10 "1,68" con virgola vs C8.7.1.2 "0.4" col punto). Il markdown uniforma alla **virgola italiana** (`0{,}xx`), convenzione esplicita del progetto NTC. Valore numerico invariato.
2. **Maiuscole/minuscole di pedici e simboli chiaramente equivalenti**, uniformate nel markdown dove la fonte è incoerente tra formula e definizione:
   - Φ/φ (coefficiente ammorsamento/ingranamento): fonte Φ maiuscola nella formula, φ minuscola nella definizione (C8.7.1.2, C8.7.1.15) → markdown `\phi`.
   - K/k (pedice δ_{PQx}): fonte K maiuscola in C8.7.1.4 vs k minuscola nella gemella C8.7.1.5 → markdown `k` coerente.
   - Z/z (pedice quota) e V/v (C8.7.1.14) → markdown minuscolo coerente.
   - S_h/s_h (C8.7.2.2), h_s scritto "hs" senza pedice (C8.7.4.7b), ρ_s f_y compattato "ρ_sfy" (C8.7.4.8), M_{e.Rd} con punto nel pedice (C8.7.2.13) → markdown reso in forma coerente e leggibile.
   - V_w/V_W (C8.7.2.8/9/10) → minuscolo coerente.
3. **Forma editoriale**: C8.8.5.1 la fonte ripete `S_{Di}(T)=` in ogni ramo delle graffe; il markdown fattorizza il primo membro fuori dalle `cases` (matematicamente identico). C8.7.1.9 usa `\simeq` dove la fonte ha `\cong` (entrambi "circa uguale", nessuna differenza di valore).

## Anomalie della fonte censite (AF, mantenute o interpretate secondo policy)

Refusi tipografici della Circolare C8 rilevati da A/B e documentati: incoerenza Φ/φ, K/k, S_h/s_h, "hs"/h_s, "ρ_sfy", "e.Rd" con punto, "inMPa" senza spazio, separatore decimale misto, parentesi orfana in nota di C8.8.5.5 ("tra 1 e 4)"). Sotto la policy "uniforme e leggibile" i simboli equivalenti sono resi in forma coerente; nessuno di questi refusi altera un valore.

## Esito finale lotti formule

**44/44 formule conformi nel VALORE** sullo snapshot `17de5443…`, perimetro F02-F05. Una sola correzione di valore (ERR-MD-01, segno esponente C8.7.2.1) promossa dopo adjudicazione sul PDF e ricontrollata da verificatore fresco. Differenze tipografiche residue trattate come normalizzazioni documentate secondo la policy "uniforme e leggibile" scelta da Sandro. Restano fuori perimetro il testo in prosa e i titoli del § C8.7-C8.8 (lotto prosa/struttura).

Conformità documentale del VALORE delle formule dei §§ C8.7.1, C8.7.2, C8.7.4 e C8.8.5 rispetto al PDF identificato nel manifest, verificata sul 100% delle 44 formule con due passaggi indipendenti su modelli diversi. Doppio controllo eseguito da agenti AI; nessuna revisione umana integrale inclusa.

---
Compilato da CC (Claude Code, Opus 4.8) — 2026-07-17. Passaggio A: Opus 4.8. Passaggio B: Sonnet. Recheck: Opus 4.8.
