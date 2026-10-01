---
title: Normalizzazioni tipografiche dichiarate - corpus NTC 2018
aliases:
  - Normalizzazioni dichiarate NTC 2018
  - Classe N NTC 2018
tags:
  - formazione/normativa
  - ntc2018
  - verifica-conformita
---

# Normalizzazioni tipografiche dichiarate — corpus NTC 2018

Elenco unico delle differenze di **sola impaginazione** fra la Gazzetta Ufficiale e i file Markdown del corpus. Sono la «classe N» del ciclo di conversione e verifica, § 5: differenze prive di qualunque effetto normativo, ammesse ovunque, **dichiarate una volta sola qui** e mai annotate occorrenza per occorrenza.

Regola di lettura: se una differenza fra fonte e Markdown non rientra in questo elenco, **non è una normalizzazione**. O si conserva la forma della fonte, o si corregge con nota di trascrizione `AF-COR` alle condizioni del § 5. Non esistono terze vie.

Questo file va richiamato dal verbale di ogni scope al momento del G7, e riletto prima di aprirne uno nuovo.

## Ammesse fin dall'origine (ciclo, § 5, classe N)

1. Spaziature, a capo, rientri, spazi doppi della fonte.
2. Varianti Unicode dello stesso carattere; apostrofi e virgolette dritte o curve; `ϕ` e `φ`; hyphen-minus e `−` U+2212.
3. Spaziatura LaTeX, `\left`/`\right`, parentesi ridondanti che non cambiano la struttura, sostituzione di `[ ]` con `( )` come delimitatore esterno.
4. Virgola decimale italiana resa `0{,}85` in LaTeX. **Attenzione**: copre la *resa* di una virgola che la fonte stampa, non la *sostituzione* di un punto che la fonte stampa. Vedi `AF-3.3-03` e `AF-3.3-08`.
5. `\cdot` **aggiunto** dove la fonte moltiplica per giustapposizione. Mai tolto dove la fonte lo stampa: deciso da Sandro il 6/8/2026.
6. Espansione delle celle accorpate: nelle **testate** l'etichetta che copre più colonne si scrive una volta sola e le celle coperte restano vuote; nel **corpo** sia i valori sia le etichette di riga si ripetono in tutte le celle logiche coperte. Deciso da Sandro il 6/8/2026, schema Tab. C3.3.XI.
7. Resa in tabella di valori che la fonte espone come testo corrente, **a intestazioni vuote** e senza aggiungere parole.
8. Spazi interni ai tag di formula: `[C4.1.10 ]` reso `[C4.1.10]`.
9. Punteggiatura finale delle didascalie di tabella e figura, che la fonte chiude col punto fermo e il corpus omette. Deciso da Sandro il 6/8/2026.
10. Separatore fra numero e testo della didascalia: `-`, `–` e `—` sono equivalenti e non producono rilievi di conformità. Quando la fonte usa `:`, il corpus può conservarlo oppure renderlo con uno dei tre trattini. Deciso da Sandro il 28/8/2026; sostituisce la precedente prescrizione del solo `—`.
11. Riga di navigazione in testa a ogni file e apparato Obsidian (wikilink `[[…]]`, àncore `^nome`, marcatori di nota): non sono testo della fonte e vanno tolti meccanicamente dai pacchetti dei blocchi ciechi del G6.
12. Resa dei viewer che non usano il template di render, Obsidian compreso: i tag di formula vi appaiono fra tonde invece che fra quadre. Nel PDF prodotto da `strumenti/render-capitolo.py` le quadre sono corrette.

## Ammesse dal 6/8/2026, decise da Sandro

Emerse dal G2 e dal G4 del § 3.3. In nessuna cambia una parola, una cifra o un significato: cambia come la cosa appare sulla pagina. La strada alternativa, cioè riprodurre anche l'impaginazione della fonte, è stata scartata perché costringerebbe a riscrivere in HTML le tabelle senza testata e produrrebbe simboli che un tecnico leggerebbe come errori di battitura.

13. **Pedici e basi che la fonte compone a corpo pieno.** La fonte stampa `log10(A)` col `10` grande quanto le altre cifre e `Re` con la `e` grande; il corpus scrive `\log_{10}` e `R_e`. Casi noti: `[C3.3.3]`, testata della Tab. C3.3.XVIII.
14. **Tabelle senza riga di testata.** Diverse griglie della Circolare partono direttamente con i dati; la sintassi delle tabelle Markdown pretende una riga di titolo, e la prima riga di dati finisce in quella posizione. Nessuna parola aggiunta né persa. Casi noti: Tab. C3.3.IX, C3.3.XIII, C3.3.XV.
15. **Righe a piena larghezza interne alla griglia.** Quando la fonte chiude una tabella con una riga a piena larghezza senza contrassegno, il corpus la rende come capoverso subito dopo la tabella, nello stesso ordine di lettura. Caso noto: Tab. 3.3.III delle NTC.
16. **Formule a più rami.** La fonte le numera una volta sola, col tag centrato sul blocco; il corpus rende ogni ramo come formula esposta distinta e mette il tag su uno solo. Ne conseguono formule esposte non numerate che nella fonte non esistono come tali. Casi noti: `[3.3.1.b]`, `[3.3.7]`, `[C3.3.5]`, `[C3.3.6]`, `[C3.3.8]`.
17. **Formule con graffa rese come elenco.** Quando la fonte espone due o più valori alternativi con una graffa, il corpus li rende come voci di elenco puntato. Caso noto: `c_p` del § C3.3.8.7, p. fisica 74.
18. **Blocchi «dove:».** La fonte li compone come capoverso unico o come righe rientrate senza marcatore; il corpus li rende come elenco puntato, senza spezzare né riordinare il testo.

## Cronologia delle decisioni

| Data | Chi | Che cosa |
|---|---|---|
| 2026-08-28 | Sandro | voce 10: equivalenza fra trattino corto, medio e lungo nei separatori delle didascalie |
| 2026-07-31 | Sandro | approvato l'impianto delle tre classi del ciclo, § 5 |
| 2026-08-06 | Sandro | voci 5, 6 e 9: punti di moltiplicazione, accorpamenti, punteggiatura delle didascalie |
| 2026-08-06 | Sandro | voci 13-18, sui sei criteri di resa emersi da G2 e G4 del § 3.3 |
