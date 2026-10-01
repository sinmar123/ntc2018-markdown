# Riconciliazione A/B — Lotto C8-T02 (Tabelle C.8.5.III e C8.5.IV)

- Data: 2026-07-17. Riconciliatore: Claude Code (CC), modello Fable 5.
- Input: `passaggio-a/A-trascrizione-fonte.md` (subagente Claude Fable 5, contesto pulito), `passaggio-b/B-trascrizione-fonte.md` (subagente Claude Opus, contesto pulito), render in `fonte/`.
- Metodo: confronto integrale delle due trascrizioni; ogni divergenza risolta guardando il render della fonte (mai a maggioranza); text layer usato solo come corroborazione.

## Esito del confronto

**Concordanza piena** tra A e B su:

- didascalie di entrambe le tabelle (inclusi: "C.8.5.III" con punto dopo la C vs "C8.5.IV" senza; attacco "–Valori" senza spazio dopo il trattino nella III vs "– Livelli" spaziato nella IV; attacco "κsuggeriti"; corsivo dei testi; punto finale presente nella III e assente nella IV);
- architettura: III = 3 colonne × 10 sottorighe logiche, 4 celle fuse verticali 2× + 2 singole nella colonna Metodo, comparto note interno alla cornice; IV = 6 colonne × 3 righe logiche, colonna "Geometrie (carpenterie)" in cella unica fusa su LC1-LC3, nota fuori cornice;
- **tutte le 30 posizioni logiche della III** (valori κ: 1,5/1/1,5/2 (*)/1,5/1/1,5/1/2/2; parametri E, f, f (*), G, τ₀ - f_v0, τ₀, f_v0, f_b, f_m, f_g con pedici concordi);
- **tutte le 18 posizioni logiche della IV** (celle testuali parola per parola, enfasi grassetto-corsivo sulle locuzioni "indagini/prove limitate-estese-esaustive", FC = 1,35/1,20/1,00);
- note (*) e (**) della III e nota (*) della IV, parola per parola (incluso il possibile doppio spazio dopo "compressione." nella nota (*), segnalato da entrambi come probabile artefatto di giustificazione, e "τ almeno pari a 3" in chiusura della nota (*), anomalia della fonte trascritta fedelmente da entrambi).

## Divergenze e adjudicazioni

- **D-r1 — Nota (**) della III, parola dopo "delle Norme."**: A trascrive "Nota: f_k,"; B trascrive "Noto f_k," dichiarando il DUBBIO con lettura alternativa "Nota: f_k,". Adjudicata sul render `fonte/zoom-adjud-nota2ast-noto-vs-nota.png` (zoom 10×): il glifo finale è una "a" e seguono due punti nitidi → **"Nota: f_k,"**. Corroborazione text layer (`fonte/pagina-266-text.txt` riga 90): concorde. Esito: **lettura A**; la costruzione sintatticamente anomala ("Nota: f_k, la resistenza…" dove ci si aspetterebbe "Noto f_k,") è un'anomalia della fonte da conservare fedelmente (AF).
- **D-r2 — nomenclatura dei trattini in B**: B chiama "trattino breve" sia il glifo di "τ₀ - f_v0" sia (in legenda) l'en dash U+2013. I glifi trascritti da B coincidono però con quelli di A (hyphen-minus spaziato in "τ₀ - f_v0"; en dash in "muraria) – prova tipo Sheppard" e nelle didascalie). Divergenza puramente terminologica, nessun impatto sul contenuto. Fonte concordata secondo la descrizione di A (§1.5 punto 8).
- **D-r3 — peso del trattino nelle didascalie** (dubbi D1/D3 di A): non determinabile al render se il trattino sia in grassetto; semanticamente irrilevante e non rappresentabile in Markdown in modo distinto. Registrato come micro-indeterminazione senza effetto sull'esito.

## Fonte concordata

La **trascrizione A** (`passaggio-a/A-trascrizione-fonte.md`) integrale, con le adjudicazioni D-r1-D-r3 sopra, costituisce la rappresentazione sorgente concordata per il confronto col Markdown.

Firma: riconciliazione eseguita da Claude Code (CC), Fable 5, 2026-07-17.
