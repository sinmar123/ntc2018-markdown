# Riconciliazione dei passaggi A e B (fonte concordata)

- Data: 2026-07-16. Riconciliatore: Claude Code (CC), modello Fable 5.
- Input: `passaggio-a/A-trascrizione-fonte.md` (CC, Fable 5, estrazione PyMuPDF + lettura visiva) e `passaggio-b/B-trascrizione-fonte.md` (subagente Opus, sola lettura visiva dei 9 render fonte).
- Metodo: confronto cella per cella e simbolo per simbolo DOPO la chiusura di entrambi i passaggi; ogni divergenza risolta tornando al render della fonte (mai a maggioranza).

## 1. Esito complessivo

| Apparato | Celle/elementi confrontati | Divergenze A-B | Esito |
|---|---|---|---|
| Tab C8.5.I — didascalia+legenda | blocco unico (2 parentetiche incluse) | 0 | CONCORDANO |
| Tab C8.5.I — intestazione | 2 righe, 7 colonne logiche | 1 (D1) | risolta |
| Tab C8.5.I — corpo | 8 righe × 6 colonne dati = 48 celle + 8 etichette | 0 | CONCORDANO |
| Tab C8.5.I — note | (*) (**) (***) | 0 | CONCORDANO |
| Tab C8.5.II — didascalia | blocco unico | 0 | CONCORDANO |
| Tab C8.5.II — intestazione | 2 fasce + 7 etichette ruotate + Tipologia fusa | 0 | CONCORDANO (fascia "Interventi di consolidamento" estesa anche sull'ultima colonna: confermata da entrambi) |
| Tab C8.5.II — corpo | 8 righe × 7 colonne dati = 56 celle + 8 etichette | 0 | CONCORDANO |
| Tab C8.5.II — note | (*) (**) (***) (****) | 0 | CONCORDANO (esponente `0.35` col punto: entrambi) |
| Formule [C8.5.4.1], [C8.5.4.2], [C8.5.4.3] | LaTeX simbolo per simbolo + tag | 0 (equivalenza `\overline`/`\bar`, `\frac`/`\dfrac`, spaziature `\,`: normalizzazione LaTeX ammessa) | CONCORDANO |
| Frase LC3, frase ponte, paragrafo "dove…", "Nel determinare…", "Qualora…" | verbatim | 0 (inclusi σ′, X̄, κ ×3, σ′², `C8..5.4.3`) | CONCORDANO |
| Nota 3 a piè di pagina | verbatim | 1 (D2) | risolta |
| Didascalia Tab C.8.5.III (solo richiamo) | richiamo `[C8.5.4.3]` | 1 (D3, fuori dal nucleo del richiamo) | risolta |

## 2. Divergenze e adjudicazione sul render

### D1 — Tab C8.5.I, intestazione colonna 3: pedice `v0` o `V0`?
- A: `fv0` (minuscolo, senza annotazioni).
- B: legge `f_V0` ("la v sembra maiuscola") pur notando che legenda e testo usano `fv0` minuscolo.
- Adjudicazione: su `fonte/zoom-adjud-header-simboli-c85I.png` il glifo in pedice ha effettivamente forma da maiuscola, ma il text layer del PDF codifica `fv0` minuscolo anche nella cella di intestazione (`fonte/pagina-261-text.txt`, righe 12 e 20) e la legenda della stessa tabella definisce il simbolo come `fv0` minuscolo. L'apparenza è resa del grassetto corsivo a corpo pedice.
- CONCORDATO: `f_v0` minuscolo; annotata in registro l'apparenza tipografica. Markdown `$f_{v0}$`: conforme.

### D2 — Nota 3: attacco del richiamo `³` alla prima parola
- A: trascrive "3 Dalla formula emerge" (spazio di formattazione).
- B: "³Dalla" attaccato.
- Adjudicazione: su `fonte/nota3-footer-crop.png` l'apice 3 è ATTACCATO a "Dalla".
- CONCORDATO: `³Dalla` attaccato (vale B). Irrilevante per il Markdown: la nota è resa con la convenzione locale `**Nota 3.** …` (normalizzazione documentata).

### D3 — Didascalia Tab C.8.5.III: `κ suggeriti` o `κsuggeriti`
- A: "κ suggeriti" (con spazio, in citazione abbreviata).
- B: `κsuggeriti` attaccato.
- Adjudicazione: su `fonte/definizioni-qualora-crop.png` la kappa è ATTACCATA a "suggeriti" (stesso artefatto di crenatura di `κper` nella nota 3).
- CONCORDATO: `κsuggeriti` come stampato (vale B). L'elemento in scope (richiamo all'equazione `[C8.5.4.3]`, un solo punto dopo C8) è concordato da A e B senza divergenze.

## 3. Dichiarazione

Nessun'altra divergenza tra A e B su 104 celle dati, 16 etichette di riga, 2 apparati di intestazione, 7 note a piè di tabella/pagina, 3 formule e 5 blocchi di prosa in scope. La fonte concordata coincide con la trascrizione A integrata dalle adjudicazioni D1, D2, D3.

Firma: riconciliazione — Claude Code (CC), Fable 5, 2026-07-16.
