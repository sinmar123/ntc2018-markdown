# Registro di audit — Lotto C8-T03 (Tabelle C8.5.V e C8.5.VI + note esplicative)

- Cartella: `_tmp_render/cap08/conformita-tabelle-formule-20260717-r02/`
- Protocollo: VC8-G4-TF. Fonte: `raw/Circolare-7-2019-NTC.pdf` — SHA-256 `f7c3b8d1…` (pagina PDF 268 = GU 264).
- Markdown pre-audit: `cap08/8-esistenti.md` SHA-256 `a3ee349b…` (post lotto T02); post-correzioni: SHA-256 `0f3642961dc8f086a89138f1bc713f2083ff7c0b88f51fcf7e1dbc81f4f20d85`.
- Data: 2026-07-17 (pomeriggio/sera). Riconciliatore: Claude Code (CC), Fable 5.

## Metodo ed esito

- Passaggi A (subagente Fable 5) e B (subagente Opus) a contesto pulito, soli render (pagina intera zoom 4, crop zoom 6, zoom 8-9), cartelle separate: **concordanza integrale al 100%**, nessuna divergenza da adjudicare (v. `diff/riconciliazione-A-B.md`). 13 celle logiche per tabella + blocco note verbatim identico.
- Confronto col MD (v. `diff/scarti-md-vs-fonte.md`): 4 famiglie ERR-MD corrette il 17/7 — E1 maiuscole "Livello di Indagini e Prove" (2 tabelle); E2 punto finale aggiunto alla didascalia della VI (fonte senza punto, AF); E3 enfasi grassetto-corsivo perse sulle 6 etichette ***limitato/esteso/esaustivo***; E4 blocco note ricompattato in 1 riga → rispezzato nei 6 capoversi della fonte (testo GIÀ fedele parola per parola, anomalie della fonte "Tabelle/tabelle", "esser variato", "utilizzata" incluse). 10 NORM documentate (riusate le categorie del corpus) e 5 AF conservate.
- Diff integrale contro lo snapshot `a3ee349b…`: toccate SOLO le righe 549, 551-553, 555, 557, 559-561, 563(→563-573). Porzioni dei lotti precedenti invariate. Struttura tabelle valida. Lint registro: 0 errori, 0 avvisi (71 info = drift di riga atteso, +10 righe dal blocco note).
- Recheck (§9.9): testuale contro la trascrizione A (coincide) + **verificatore fresco Opus a contesto pulito: 4/4 CONFERMATO** (maiuscole; didascalia VI senza punto; enfasi etichette; struttura del blocco note).

## Chiusura

- Perimetro verificato: 100% dello scope — 2 tabelle (26 celle logiche totali con intestazioni a 2 livelli e fasce fuse) + blocco note esplicative integrale (titolo, introduzione, note (a)-(d)).
- **Criterio di accettazione §12: SUPERATO** per il perimetro dichiarato. Doppio controllo indipendente eseguito da agenti AI; nessuna revisione umana integrale inclusa.
- Rilievo collaterale (fuori perimetro, già censito): nel MD le Tabelle C8.5.V-VI giacciono sotto la seconda occorrenza (spuria) dell'heading C8.5.3.2 (md 543), mentre nella fonte appartengono al §C8.5.4.2 — ricollocazione affidata al lotto prosa/struttura, che dovrà anche ricomporre il capoverso "A titolo esclusivamente orientativo… (v. § C8.5.2.2 e C8.5.3.2) e quindi…" spezzato dal convertitore (l'heading spurio a md 543 nasce dal riferimento "§ C8.5.3.2" dentro quel capoverso, pagine fonte 267-268).

Firma: audit eseguito e chiuso da Claude Code (CC), Fable 5, con subagenti Claude (Fable 5, Opus) nei ruoli A/B/recheck, 2026-07-17.
