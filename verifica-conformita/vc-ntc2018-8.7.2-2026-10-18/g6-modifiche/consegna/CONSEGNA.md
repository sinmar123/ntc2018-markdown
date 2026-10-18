# Consegna al verificatore: controllo delle modifiche, scope § 8.7.2 / C8.7.2

Sei il verificatore indipendente (V) del controllo delle modifiche previsto dal § 8 della procedura VC-NTC/10. Non hai scritto le correzioni né la lista e non coordini lo scope. Lavora soltanto sui file di questa cartella: non aprire altre cartelle, il workspace, il repository o internet, e non usare strumenti di controllo del computer o del browser. Non modificare né creare file: la tua risposta finale è il rapporto JSON descritto in fondo, e nient'altro.

La fonte è la pagina stampata della Circolare 21/01/2019 n. 7 (Gazzetta Ufficiale). `fonte-circ-285.png`, `fonte-circ-287.png` e `fonte-circ-289.png` sono le pagine fisiche a 200 dpi; `fonte-circ-*-dove-600dpi.png` sono ritagli nativi a 600 dpi dei tre blocchi «dove:» interessati. I criteri sono in `canone.md` (§§ 3-4 della procedura e catalogo delle normalizzazioni). La voce 18 del catalogo regola i blocchi «dove:».

## Che cosa è cambiato

Il confronto integrale (G6, giro 1) ha prodotto i sei rilievi di `rilievi-g6.json`. Sandro ha deciso il 2026-10-18 alle 16:53 (ora di Roma), come riportato nello stesso file: un solo rilievo corretto, COND-C285-DOVE-1. Le definizioni dei blocchi «dove:», prima capoversi senza marcatore, sono ora voci di elenco puntato `- `; la stessa correzione è stata estesa ai blocchi «dove:» di [C8.7.2.8] e [C8.7.2.13]. Gli altri cinque rilievi sono chiusi senza modifiche e non vanno ricontrollati.

Le tre voci applicate da script sono in `lista-correzioni.json`. Per ciascun blocco del confronto integrale, `bNN-testo-prima.md` è il testo depurato consegnato al G6, `bNN-testo-dopo.md` quello attuale e `bNN-diff.txt` il diff completo. `resa-dopo.pdf` è la nuova resa canonica completa; `resa-dopo-pNN.png` sono le pagine con i blocchi corretti (4-5, 7, 9). La nuova resa contiene in testa anche l'indice interno del file e le righe di navigazione, che il G6 non consegnava: non sono testo normativo e non fanno parte del controllo.

Impronte SHA-256 del file Markdown dello scope: prima 242f7892a7d3c7432d4dd90a847d2a92a9073e2640618056c4b63417a6a52527, dopo 6b338b8c2610ab51603db0dc9aa140ba6b0a15cbdfc68e0583c0f5626ae3b689.

## Che cosa controllare

1. **Diff.** `b01-diff.txt` e `b02-diff.txt` devono contenere soltanto l'aggiunta del marcatore `- ` all'inizio delle righe di definizione dei tre blocchi: 9 righe dopo [C8.7.2.1] (da γ_el = 1.5 ad α), 9 righe dopo [C8.7.2.8] (da γ_el = 1.15 a V_w), 3 righe dopo [C8.7.2.13] (da M_e,Rd a I). Nessun'altra variazione, nessuna parola cambiata, nessun riordino.
2. **Rilievo COND-C285-DOVE-1 e blocchi estesi.** Sulla fonte, controlla per i tre blocchi che le righe diventate voci di elenco siano esattamente le definizioni composte come righe rientrate, nello stesso ordine e con lo stesso testo, e che il testo dopo sia conforme alla voce 18. Le sottovoci «sezioni rettangolari:» e «per le sezioni circolari:» erano già voci di elenco e non sono cambiate.
3. **Effetti.** Nella resa (pagine indicate) e nel contesto del testo dopo: formule [C8.7.2.1], [C8.7.2.2], [C8.7.2.8], [C8.7.2.9], [C8.7.2.13] e testo vicino invariati, elenco composto correttamente, nessun effetto indesiderato.

Classifica ogni difformità come `ERR-MD`, `ERR-AUDIT` o `DUBBIO` secondo il canone. Se una lettura della fonte non è univoca, scrivi `DUBBIO`: non ricostruire ciò che la fonte non permette di leggere.

## Rapporto

Rispondi soltanto con un oggetto JSON valido, senza testo prima o dopo e senza blocchi di codice, con questi campi:

- `firma`: chi sei (modello e ruolo);
- `controllo`: "modifiche § 8, scope 8.7.2";
- `snapshot_prima_sha256`, `snapshot_dopo_sha256`: le impronte indicate sopra;
- `diff`: oggetto con `esito` ("OK" o "KO") e `note`;
- `rilievi`: elenco di oggetti `id`, `esito` ("CHIUSO" o "APERTO"), `prova` (pagina, file e che cosa hai visto, in breve), con una voce per COND-C285-DOVE-1 e una per ciascuno dei due blocchi estesi (id "EST-C287-DOVE" e "EST-C289-DOVE");
- `resa`: oggetto con `pagine_osservate` ed `esito`;
- `nuovi_rilievi`: elenco, anche vuoto, di oggetti `id`, `classe`, `pagina`, `prova`;
- `esito`: "OK" soltanto se il diff è OK, tutti i rilievi sono CHIUSO e non ci sono nuovi rilievi; altrimenti "KO";
- `letture`: elenco dei file che hai letto;
- `limiti`: limiti del controllo, in una o due frasi.
