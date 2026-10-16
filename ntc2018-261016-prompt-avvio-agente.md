# Prompt di avvio per un agente nuovo

Prompt per far partire da zero un agente sulla conversione e verifica NTC 2018, scritto da CC cloud il 2026-10-16 su richiesta di Sandro. Vale per una sessione cloud di Claude Code aperta sul repository `sinmar123/ntc2018-markdown`, con l'ambiente «Default», e per gli altri agenti che possono clonarlo e aprire pull request (Codex, OpenClaw). Il paragrafo da verificare non sta nel prompt: lo chiede l'agente, come seconda domanda.

Le regole non sono ricopiate qui: stanno in AGENTS.md, CLAUDE.md e PROCEDURA-VC.md, e il prompt resta valido anche quando la procedura cambia.

## Prompt da incollare

```text
Lavori sul progetto NTC 2018: il D.M. 17/01/2018 e la Circolare 7/2019 convertiti in
Markdown, con una verifica di conformità (VC) sulla Gazzetta Ufficiale per ogni paragrafo.
Il repository è https://github.com/sinmar123/ntc2018-markdown ed è la copia principale.

Prima di fare qualsiasi cosa:
1. Leggi AGENTS.md (e CLAUDE.md se sei Claude Code), poi per intero PROCEDURA-VC.md:
   è l'unica procedura valida. Il catalogo delle normalizzazioni è il suo allegato.
2. Esegui `python strumenti/vc-supporto.py avvio` e dimmi in poche righe chi sei
   (agente e modello) e lo stato attuale: eventuali VC in corso e, dal registro
   registro-verifica-conformita-ntc2018.csv, i prossimi paragrafi ancora da verificare.
3. Chiedimi su quale paragrafo lavorare e aspetta la risposta. Lo scope si legge alla
   lettera: «8.6» è solo la riga 8.6, i sottocapitoli solo se li nomino.
4. Avuto lo scope, esegui `python strumenti/vc-supporto.py avvio <scope>`, dimmi cosa
   farai e in quanti blocchi di G6, e procedi.

Regole che non si saltano:
- Lavora su un ramo e chiudi con una pull request; mai scrivere su main.
- Non toccare righe del registro IN-CORSO di altri agenti e non modificare il CSV a mano.
- Prima di correggere qualsiasi file mi porti la lista delle non conformità e ti fermi.
- Scrivi in italiano.
```

## Varianti

- Per far partire l'agente subito su un paragrafo, sostituire i punti 2-4 con: «Esegui `python strumenti/vc-supporto.py avvio 8.6` e procedi con la VC del § 8.6, solo la riga 8.6», cambiando il numero.
- Per una sezione intera: «8.7 con i sottocapitoli» oppure «tutto l'8.7».
