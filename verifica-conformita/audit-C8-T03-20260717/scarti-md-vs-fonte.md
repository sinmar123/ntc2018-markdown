# Scarti Markdown vs fonte concordata — Lotto C8-T03 (Tabelle C8.5.V-VI + note)

- Data: 2026-07-17. Compilatore: Claude Code (CC), Fable 5.
- Markdown: `cap08/8-esistenti.md`, snapshot pre-correzioni SHA-256 `a3ee349b…`, righe 547-563.
- Fonte concordata: riconciliazione A/B (concordanza 100%).

## 1. ERR-MD — difformità da correggere

- **E1-T03** (md 549 e 557): intestazione `Livello di indagini e prove` in minuscolo dove la fonte stampa `Livello di Indagini e Prove` (I e P maiuscole, concordi A/B/zoom). Correzione: ripristino maiuscole in entrambe le tabelle.
- **E2-T03** (md 555): punto fermo aggiunto alla didascalia della Tab. C8.5.VI (`…per edifici di acciaio.`) dove la fonte termina senza punto (AF-2). Stesso vizio già corretto su C8.5.IV (E3 del lotto T02). Correzione: rimozione.
- **E3-T03** (md 551-553 e 559-561): etichette di livello `limitato`, `esteso`, `esaustivo` prive dell'enfasi grassetto-corsivo della fonte (enfasi semantica: i tre livelli richiamati dal testo del paragrafo). Correzione: `***limitato***` ecc., 6 celle.
- **E4-T03** (md 563): blocco note esplicative compattato in un'unica riga (titolo + capoverso introduttivo + note (a)-(d) fusi). Il TESTO è integrale e fedele parola per parola (verificato contro la fonte concordata), ma la struttura in 6 blocchi della fonte è persa. Correzione: rispezzatura in 6 capoversi (titolo / introduzione / (a) / (b) / (c) / (d)), contenuto invariato.

## 2. NORM — normalizzazioni accettate (nessuna correzione)

1. Didascalie in grassetto complessivo + trattino `-` = NORM 4 e NORM trattini del corpus.
2. `Rilievo(dei` attaccato (solo Tab. V) reso `Rilievo (dei` = NORM 6 (kerning di stampa).
3. Richiami di nota da APICE (fonte: ^(a)^, ^(b)(c)(d)^) a IN LINEA nel MD (`(a)`, `(b)(c)(d)`) = nuova NORM di notazione richiami nelle intestazioni (i marcatori delle note nel blocco sono in linea anche nella fonte).
4. Spazio prima degli apici ^(b)(c)(d)^ presente solo nella VI (micro-incoerenza della fonte): assorbito dalla NORM 3.
5. Fascia di intestazione fusa "Per ogni elemento "primario" (trave, pilastro[…])" resa come percorso esplicito ` - per ogni elemento "primario" (…)` appeso a ENTRAMBE le colonne coperte = metodo dei percorsi di colonna del pilota (C8.5.II), copertura completa. Conforme.
6. Virgolette tipografiche curve di "primario" rese dritte = NORM 7 del pilota.
7. `m²` con carattere superscript Unicode contro apice tipografico = equivalente, conforme.
8. Ellissi di "pilastro…" resa `...` (tre punti) = indeterminazione D3 della fonte, accettata.
9. A capo fisici interni alle celle non riprodotti = impaginazione non semantica.
10. Intestazioni MD non in grassetto esplicito = il renderer Markdown le rende in grassetto di default, conforme alla resa tonda-su-grigio della fonte (peso font di intestazione, non semantico).

## 3. AF — anomalie della fonte conservate fedelmente

1. `Rilievo(dei` senza spazio nella sola Tab. V (kerning, assorbito da NORM 2).
2. Didascalia della Tab. C8.5.VI senza punto finale contro la V che chiude con "c.a." — conservata con E2-T03.
3. Incoerenze del blocco note: "Tabelle C8.5.V e C8.5.VI" (maiuscolo, intro) contro "tabelle C8.5.V e C8.5.VI" (minuscolo, nota d); "può esser variato" tronco; "classe dell'acciaio utilizzata" — già fedeli nel MD, conservate.
4. "(trave, pilastro)" nella V contro "(trave, pilastro…)" nella VI — già fedele nel MD.
5. "1 campione di bullone o chiodo" / "2-3 campioni di bullone o chiodo" (singolare mantenuto) — già fedele.

## 4. Elementi verificati CONFORMI senza intervento

Didascalia V (testo, punto di "c.a."), tutte le 18 celle di corpo delle due tabelle parola per parola (verbi concordati, percentuali, "cls."/"acciaio", "300 m²", "bullone o chiodo", apostrofi tipografici), percorsi di colonna con richiami (a) e (b)(c)(d) su entrambe le colonne, testo integrale delle note (a)-(d) e dell'introduzione (anomalie della fonte incluse).
