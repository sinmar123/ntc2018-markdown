# Registro audit lotto C8-T05 — Tabella C8.7.6.3.II

## Perimetro e snapshot

- **Apparato**: Tabella C8.7.6.3.II "Possibili alternative per la limitazione del rischio di fuoriuscite di gas sotto azioni sismiche" — multipagina, pp. file PDF 298-300 (pp. stampate G.U. 294-296). Perimetro: didascalia, 7 intestazioni di colonna, 5 righe-criterio × 6 colonne-tipo = 30 celle dati (3 vuote nella fonte).
- **Fonte**: `raw/Circolare-7-2019-NTC.pdf` — SHA-256 `f7c3b8d1f443aadb6b3e020b6b6c19813683492ecaadd2c15bf6bf1939aaed7c` (riverificato). Ritagli in `_tmp_render/cap08/conformita-tabelle-formule-20260717-r04/fonte/` (crop-p298/299/300-tabII + pagine intere).
- **Markdown**: `cap08/8-esistenti.md`, righe 1457-1465.
  - snapshot pre-correzione: SHA-256 `d4d4ee4145232206613336529169a14c15590a7aced6e5a1c1674d5b0f6a099a` (= chiusura T04)
  - snapshot post-correzione E1: SHA-256 `da2bf432e7eeee3271712b468a082606b8ee21cffd05dfb84addc3f6f78f3833`

## Metodo

Protocollo `VC8-G4-TF` (skill `controllo-serrato-ntc2018`, riferimento `protocollo-conformita-tabelle-formule.md`): doppio passaggio indipendente su modelli diversi, alla cieca rispetto al Markdown e all'altro passaggio; riconciliazione e adjudicazione sul PDF da parte di CC; confronto meccanico A/B/MD; correzioni promosse solo dopo adjudicazione; recheck fresco a contesto pulito.

- **Passaggio A**: agente AI, modello di sessione **Opus 4.8** — `passaggio-a/trascrizione-tabII.md`.
- **Passaggio B**: agente AI, modello **Sonnet** — `passaggio-b/trascrizione-tabII.md`.
- **Confronto meccanico**: `diff/confronta_triplo.py` → `diff/confronto-triplo.csv` — 38 posizioni logiche (1 didascalia + 7 intestazioni + 30 celle).
- **Arbitro (CC, Opus 4.8)**: verifica visiva diretta sui ritagli fonte e zoom ad alta risoluzione della didascalia (`diff/zoom-didascalia-fine.png`).
- **Recheck fresco**: agente AI a contesto pulito, modello **Opus 4.8** — `recheck/recheck-tabII.md`.

## Esito confronto A vs B

Concordanza piena: **38/38 posizioni identiche** (didascalia, 7 intestazioni, 30 celle dati comprese le 3 vuote). Nessuna divergenza.

## Difformità Markdown rilevata e correzione promossa (ERR-MD)

| # | Posizione (md) | Fonte concordata | Markdown pre | Correzione |
|---|---|---|---|---|
| E1 | riga 1457, didascalia | nessun punto finale dopo "sotto azioni sismiche" (verificato a zoom alta risoluzione) | punto finale presente ("...sismiche.") | punto rimosso |

Confronto meccanico: **37/38 pre-correzione** (unica difformità la didascalia), **38/38 post-correzione**. Stessa fattispecie del punto spurio di didascalia già corretto in T03 (Tab. C8.5.VI) e in T04-E1 (Tab. C8.7.6.3.I).

## Anomalie della fonte mantenute fedelmente (AF)

1. Grafia "istallazione/istallate" (una s) nelle intestazioni col. 4-5, in R1/C1 e in R2/C6, incoerente con "installazione" (due s) nell'etichetta di riga e nelle celle R2/C2-C5 della stessa tabella.
2. Mancate elisioni: "la elevata concentrazione" (R1/C5), "da una unità centrale" (R1/C6).
3. Discordanza di genere/numero: "Nessuno, in quanto già previste..." (R2/C1).
4. Punteggiatura di cella incoerente: R2/C3 chiude con punto ("...dell'impianto."), la gemella R2/C4 senza ("...dell'apparecchio"); nessuna cella di R1 ha punto finale; in R3 solo C5 e C6 lo hanno. Mantenuta fedelmente cella per cella.
5. "d" eufonica ricorrente davanti a vocale diversa ("ad una soglia", "ad uno standard"): mantenuta.

## Normalizzazioni documentate (NORM)

1. Tabella multipagina (testata ripetuta a p. 299 e p. 300) → tabella Markdown unica: le testate ripetute e gli a-capo fisici di impaginazione non sono replicati; il testo di ogni cella spezzata tra le pagine è ricomposto continuo.
2. Apostrofi e virgolette tipografici della fonte → ASCII dritti nelle celle, coerente con la resa dei lotti T01-T04.
3. Didascalia fonte (etichetta + testo corsivo, senza punto) → didascalia tutta in grassetto senza punto (convenzione uniforme del file).

## Recheck fresco

Agente a contesto pulito (Opus 4.8) su fonte e Markdown corretto: verifica di E1 + giro di coerenza su 5 refusi mantenuti, punteggiatura asimmetrica R2/C3 vs R2/C4, 3 celle vuote, struttura 7×5. Esito in `recheck/recheck-tabII.md`.

**Esito: 5/5 CONFORME.** Nessuna difformità residua.

## Esito finale lotto

**Tabella C8.7.6.3.II CONFORME al 100% delle posizioni logiche** (38/38 al confronto meccanico post-correzione) sullo snapshot `da2bf432…`, nel perimetro dichiarato: didascalia, 7 intestazioni, 30 celle dati. Correzione E1 promossa dopo adjudicazione e ricontrollata da verificatore fresco (5/5). Cinque anomalie della fonte censite e mantenute fedelmente. Resta fuori perimetro la prosa del § C8.7.6.3 e del § C8.8 (lotto prosa/struttura).

Conformità documentale della Tabella C8.7.6.3.II rispetto al PDF identificato nel manifest, verificata sul 100 per cento delle posizioni logiche con due passaggi indipendenti. Doppio controllo indipendente eseguito da agenti AI; nessuna revisione umana integrale inclusa nel presente audit.

---
Compilato da CC (Claude Code, modello di sessione Opus 4.8) — 2026-07-17 19:31 +0200. Passaggio A: Opus 4.8. Passaggio B: Sonnet. Recheck: Opus 4.8.
