# Scarti Markdown vs fonte concordata — Lotto C8-T02 (Tabelle C.8.5.III e C8.5.IV)

- Data: 2026-07-17. Compilatore: Claude Code (CC), Fable 5 (riconciliatore).
- Fonte concordata: `passaggio-a/A-trascrizione-fonte.md` + adjudicazioni in `riconciliazione-A-B.md`.
- Markdown: `cap08/8-esistenti.md`, snapshot SHA-256 `612a2c00…`, righe 506-523 (Tab. C.8.5.III) e 531-539 (Tab. C8.5.IV).
- Categorie NORM/AF riusate dal lotto C8-T01/F01 (`verifica-conformita/audit-C8-T01-F01-20260716/scarti-md-vs-fonte.md`) per coerenza di classificazione.

## 1. ERR-MD — difformità da correggere

- **E1** (md 521, nota (*) Tab. III): il MD scrive `un valore di $\kappa$ almeno pari a 3` dove la fonte stampa nitidamente **τ** (tau minuscolo), lettura concorde di A e B e confermata dal riconciliatore su crop 432 dpi. Il MD ha "corretto" interpretativamente il presunto refuso della fonte, violando il principio di fedeltà (cfr. precedente E8 del pilota: esponente `0.35`). Correzione: ripristinare `$\tau$`; anomalia della fonte registrata in AF-3.
- **E2** (md 521, nota (*) Tab. III): virgola aggiunta dal MD dopo la parentesi — `nella tabella C.8.5.I), il modulo` contro fonte `nella tabella C.8.5.I) il modulo`. Correzione: rimuovere la virgola.
- **E3** (md 531, didascalia Tab. IV): punto fermo finale aggiunto dal MD (`…in acciaio.`) dove la didascalia della fonte termina senza punto dopo "acciaio" (anomalia della fonte, AF-4). Correzione: rimuovere il punto.
- **E4** (md 535-537, Tab. IV): perse le enfasi della fonte con valore semantico: 10 locuzioni in grassetto corsivo (`indagini limitate` ×3, `indagini estese`, `indagini esaustive`, `prove limitate` ×2, `prove estese` ×2, `prove esaustive`) e 3 etichette `LC1`/`LC2`/`LC3` in grassetto. La convenzione della fonte è sistematica (identica nel corpo testo della stessa pagina) e distingue i gradi normativi di indagine e prova. Correzione: ripristinare `***…***` sulle 10 locuzioni e `**…**` sulle 3 etichette. (Precedente pilota assimilabile: fasce di intestazione assenti = E-MD; il caso NORM-9 del pilota — grassetto uniforme delle formule esposte — non è assimilabile perché lì il peso font è indistinto, qui l'enfasi è selettiva.)

## 2. NORM — normalizzazioni accettate (nessuna correzione)

1. Didascalie in grassetto MD contro grassetto+corsivo della fonte = NORM 4 del pilota (convenzione del corpus).
2. `κsuggeriti` attaccato (kerning di stampa) reso `$\kappa$ suggeriti` = NORM 6 del pilota (già codificato per questo esatto caso).
3. Trattini: en dash `–` della fonte (didascalie `III –Valori`, `IV – Livelli`; cella `muraria) – prova tipo Sheppard`) resi con `-` = NORM 2/9 del pilota.
4. Doppio spazio (o spazio largo di giustificazione) dopo `resistenza a compressione.` nella nota (*) reso con spazio singolo = normalizzazione di spaziatura (G3 ammette normalizzazione spazi).
5. Celle accorpate espanse: colonna Metodo (4 celle fuse 2×) ripetuta per riga; colonna Geometrie (cella unica su LC1-LC3) ripetuta nelle 3 righe = NORM prevista dal protocollo §7, accorpamenti registrati nel manifest.
6. Virgola decimale in LaTeX `1{,}25` = normalizzazione ammessa dal protocollo §8.
7. Simboli in math mode (`$E$`, `$f$`, `$\tau_0$`, `$f_{v0}$`, `$f_b$, $f_m$, $f_g$`, `$\kappa$`) contro tondo della fonte = convenzione del corpus (cfr. pilota).
8. Allineamento MD delle colonne testuali della Tab. IV a sinistra contro centratura della fonte = impaginazione non semantica.
9. Nota 3 a piè di pagina già resa come nota locale (NORM 8 del pilota, fuori perimetro qui).

## 3. AF — anomalie della fonte conservate fedelmente

1. Numerazione incoerente `C.8.5.III` (punto dopo la C) contro `C8.5.IV`, `[C8.5.4.3]`, `§ C8.5.4` = AF-6 del pilota, già conservata nel MD.
2. `Nota: f_k, la resistenza…` nella nota (**): costruzione sintatticamente anomala della fonte (ci si aspetterebbe "Noto f_k,"), stampata però "Nota:" — adjudicata sul render (D-r1). Il MD la conserva già fedelmente.
3. **τ** in chiusura della nota (*) (`purché si adotti un valore di τ almeno pari a 3.`) in un contesto che tratta il coefficiente **κ** dell'equazione [C8.5.4.3]: probabile refuso della fonte, da conservare (ripristinato con E1). Segnalato anche nel registro di revisione del capitolo.
4. Didascalia della Tab. C8.5.IV senza punto fermo finale (contro la Tab. C.8.5.III che lo ha) — conservata con E3.
5. Attacco `–Valori` (en dash senza spazio a destra) nella didascalia III contro `– Livelli` spaziato nella IV — assorbito dalla NORM 3 sui trattini.

## 4. Elementi verificati CONFORMI senza intervento

- Tab. C.8.5.III: didascalia (testo), intestazioni, tutte le 30 posizioni logiche (metodi, parametri con pedici τ₀, f_v0, f_b, f_m, f_g; valori κ 1,5/1/2 con richiami (*) su riga 4), nota (**) integrale (inclusa `Nota: f_k,` e `f = 1{,}25 f_k`), nota (*) salvo E1-E2.
- Tab. C8.5.IV: didascalia (testo, salvo E3), 6 intestazioni con richiamo `FC (*)`, tutte le 18 posizioni logiche (testi delle celle parola per parola, `Tutti`, `Analisi lineare statica o dinamica`, FC 1,35/1,20/1,00), nota (*) integrale.

## 5. Rilievi collaterali FUORI perimetro (non corretti in questo lotto)

- **RC1** (md 527): il capoverso del §C8.5.4.2 termina troncato `…ci si può riferire alla Tabella` — manca `C8.5.IV.` (visibile sul render di pagina 267). Prosa fuori perimetro tabellare; da correggere nel lotto prosa.
- **RC2** (md 529): heading H2 spurio `## C8.5. Definizione del modello di riferimento per le analisi` interposto tra il capoverso e la didascalia della Tab. IV: duplicato del titolo di sezione fuori posto, estraneo alla fonte in questa posizione. Da risolvere con il rilievo strutturale già censito su CIRC-C8.5.3.2 (heading duplicato md 455/543 e prosa spezzata, incluso il "muro" md 541).
- Questi rilievi alimentano G2/G5 del capitolo e il registro di dettaglio (righe CIRC-C8.5.4.2 e CIRC-C8.5.3.2), senza bloccare l'esito delle due tabelle, i cui apparati sono integri e verificabili.
