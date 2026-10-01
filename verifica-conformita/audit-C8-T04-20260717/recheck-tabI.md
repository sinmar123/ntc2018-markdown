# Recheck fresco — Tabella C8.7.6.3.I (pp. 297-298)

Verifica a contesto pulito, ordine rispettato: prima le immagini fonte, poi il markdown.
Immagini lette: `fonte/crop-p297-tabI-parte1.png`, `fonte/zoom-p297-tabI-testata.png`, `fonte/crop-p298-tabI-parte2.png`. Le pagine intere NON sono state aperte (risparmio token su indicazione di Sandro): bastavano i crop per i 4 punti.

## FASE 1 — Cosa stampa la fonte

1. **Fine didascalia**: "...di nuova installazione al variare della zona sismica" — **senza punto finale** (verificato sia nel crop parte 1 sia nello zoom testata).
2. **Quarta intestazione (costo)**: "Costo **&** interruzione per l'adeguamento" — la congiunzione è la **e commerciale "&"**, non la lettera "e".
3. **Intestazione gruppo valutazione**: "Valutazione **/** adeguamento se esistenti nelle zone 6" — la barra è **staccata, con spazio** ("Valutazione /" a fine riga, "adeguamento" a capo).
4. **Riga-categoria sostanze (p. 298)**: "**S**ostanze **P**ericolose" — **entrambe le iniziali maiuscole** (S e P).

## FASE 2 — Confronto col markdown (`markdown/estrazione-md-tabI.md`)

1. **CONFORME** — riga 9: `...di nuova installazione al variare della zona sismica**` — la didascalia termina senza punto, come la fonte.
2. **CONFORME** — riga 11: `Costo & interruzione per l'adeguamento` — usa "&" come la fonte.
3. **CONFORME** — riga 11: `Valutazione / adeguamento se esistenti - zona N (6)` — barra staccata con spazi attorno, come la fonte.
4. **CONFORME** — righe 41-42: `| Sostanze Pericolose |` — S e P maiuscole, come la fonte.

## FASE 3 — Giro di coerenza sull'intero estratto

**Difformità sostanziali: nessuna.**

Controlli fatti: didascalia integrale; tutte le intestazioni; le 9 righe-categoria (Gas per uso medico, Impianto elettrico d'emergenza, Ascensori, Apparecchiature per la comunicazione, Apparecchiature e rifornimenti medici, Componenti fissati al pavimento o sul tetto (4), Sistemi di distribuzione, Componenti architettonici, Sostanze Pericolose); valori a campione su ~15 righe (Serbatoi di ossigeno 1-2-3/1-2-3-4; Generatore 1-2-3/1-2-3-4; Guide ascensore 1-2/1-2-3-4; Caldaie 1-2/1-2-3; ribaltamento <1 1-2/1-2; Pedane vuote/1-2; Tubature >200 1-2/1-2-3; Condotto vuote/1; Soffitto vuote/1; Lampadari 1/1-2; le due righe Sostanze Pericolose 1-2-3-4/1-2-3-4): tutti coincidenti. Riprodotto fedelmente anche il refuso d'origine della fonte "Generatore della elettrico d'emergenza" (riga 16), correttamente non "corretto".

Struttura markdown: tabella regolare, 13 colonne coerenti su header, separatore e tutte le righe dati; nessuna riga sbilanciata.

Osservazioni non bloccanti (scelte di resa, non difformità):
- linearizzazione dichiarata: le righe-categoria a tutta larghezza diventano la colonna "Categoria" e i due gruppi di colonne zone vengono esplosi in 4 colonne ciascuno; resa sistematica e coerente. Gli apici della fonte (5, 6, 7e8, 4) sono resi come note (5) (6) (7)(8) (4); virgolette e apostrofi tipografici resi dritti. Tutto uniforme nell'estratto.
- le note a piè di tabella (5)-(8) presenti nel markdown (righe 44-50) non compaiono nei crop letti: non verificate in questo recheck (avrebbero richiesto le pagine intere, non aperte per contenere i token).

---
Recheck fresco — agente AI, modello di sessione (Opus 4.8) — 2026-07-17 17:22
