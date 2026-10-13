# Prompt per Claude su Chrome: attivare Pages, unire la PR #1 e controllare il sito

Da incollare in Claude su Chrome, con il browser collegato a GitHub come `sinmar123`. Preparato da CC cloud il 2026-10-12, sessione https://claude.ai/code/session_01RcP7chNA8MJouvbwqgsWNP.

## Dove eravamo

- La pull request [sinmar123/ntc2018-markdown#1](https://github.com/sinmar123/ntc2018-markdown/pull/1) (sito MkDocs, `.github/README.md`, licenze, modello di segnalazione) è aperta, con il controllo `costruisci` verde e senza conflitti. Ramo: `claude/lucid-ramanujan-so88m5`.
- Per pubblicare servono tre cose da fare su GitHub: Pages con sorgente «GitHub Actions», l'etichetta `errore-di-trascrizione`, l'unione della PR. Il prompt qui sotto le fa con Claude su Chrome e chiede conferma prima di unire.
- Se il workflow «Sito» su `main` fallisce, si riporta l'errore alla sessione cloud: la correzione si fa su un ramo nuovo, non a mano su GitHub.
- Restano aperti, per la procedura VC: 115 figure assenti dal repository; 314 `\tag{...}` dopo i `$$` di chiusura in 46 file; 7 ancore degli indici; 4 rimandi a note scritti dopo le formule nel § 3.3; un `\newpage` nel § 4.2.4. Dettagli nella voce del CHANGELOG del 2026-10-01 e nella PR.

---

```
Lavori su GitHub, nel repository sinmar123/ntc2018-markdown, con il mio account già collegato. Rispondi in italiano. Non modificare file del repository e non toccare nient'altro oltre ai passi qui sotto. Se una pagina non corrisponde a quanto descritto, o serve una scelta non prevista, fermati e chiedimi.

1. Attiva GitHub Pages
   - Apri https://github.com/sinmar123/ntc2018-markdown/settings/pages
   - In «Build and deployment», alla voce «Source», scegli «GitHub Actions». Non scegliere «Deploy from a branch» e non creare nessun workflow proposto da GitHub: il workflow c'è già (.github/workflows/sito.yml).

2. Crea l'etichetta per le segnalazioni
   - Apri https://github.com/sinmar123/ntc2018-markdown/labels
   - Se non esiste già, crea l'etichetta con nome esattamente «errore-di-trascrizione», descrizione «Testo diverso da quello pubblicato in Gazzetta Ufficiale», colore a scelta.

3. Controlla la pull request #1 prima dell'unione
   - Apri https://github.com/sinmar123/ntc2018-markdown/pull/1
   - Verifica e riferiscimi: stato «Open»; nessun conflitto con main; controllo «costruisci» verde; nella scheda «Files changed» nessun file sta in una cartella cap01 … cap12.
   - Se uno di questi punti non torna, fermati e dimmelo.

4. Unione: chiedimi conferma
   - Se tutto torna, scrivimi «Pronta per l'unione, confermi?» e aspetta la mia risposta.
   - Solo dopo il mio sì, premi «Merge pull request» (merge commit normale, non squash né rebase), poi «Confirm merge». Non cancellare il ramo.

5. Controlla la pubblicazione
   - Apri https://github.com/sinmar123/ntc2018-markdown/actions e segui l'esecuzione del workflow «Sito» partita dall'unione su main. Attendi che finisca (qualche minuto).
   - Riferiscimi l'esito dei job «costruisci» e «pubblica». Se uno fallisce, apri il job, copia le ultime righe di errore e riportamele senza tentare correzioni.
   - Se passano, apri https://sinmar123.github.io/ntc2018-markdown/ e controlla:
     a) la pagina iniziale mostra la tabella degli stati con 43 Verificato, 34 Da riconfermare, 9 Da rifare, 4 In corso, 289 Non ancora verificato;
     b) aprendo il paragrafo 2.5.3 si vedono in testa il riquadro «Non ancora verificato» e le formule composte, con i numeri a destra fra parentesi quadre, per esempio [2.5.1];
     c) aprendo il paragrafo 3.4.4 c'è il riquadro verde «Verificato il 5 settembre 2026»;
     d) la casella «Cerca» trova la parola «neve».

6. Facoltativo, solo se il sito funziona
   - Nella pagina principale del repository, ingranaggio accanto ad «About»: alla voce «Website» inserisci https://sinmar123.github.io/ntc2018-markdown/ e salva.

Alla fine dammi un riepilogo in punti: che cosa hai fatto, l'esito di ogni controllo e ciò che non hai potuto fare.
```
