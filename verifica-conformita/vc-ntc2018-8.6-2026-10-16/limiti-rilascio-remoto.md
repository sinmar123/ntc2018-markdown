# Limiti della pubblicazione remota

Firma: Codex (CDX), 2026-10-16.

La verifica riguarda esclusivamente lo snapshot locale di `cap08/8.6-materiali.md`, identificato nel rapporto C. Il confronto della fonte ufficiale e il canone dei §§ 3-4 non dipendono dall’allineamento Git: il canone locale r8 coincide con r9 dopo normalizzazione degli spazi; il catalogo è congelato e lo scope letterale r9 è stato applicato.

La lettura web di VC-NTC/9 ? stata conservata come testo effettivamente consultato, con hash proprio. Non è attestata l’identità dei byte con il file remoto. È conservata anche la copia r8 originale effettivamente letta dal generatore del pacchetto. Il giudizio G7 deve valutare esplicitamente la sufficienza di queste evidenze per lo snapshot locale, senza trasformare l’hash della lettura in hash del file GitHub.

Prima della pubblicazione sul repository remoto restano obbligatori: acquisire l’originale r9, sincronizzare il ramo con main, verificare che il target e i criteri congelati non siano cambiati e gestire eventuali modifiche concorrenti. Git HTTPS non è disponibile in questa sessione; nessuna PR o presa pubblicata è dichiarata. La VC locale non certifica contenuti eventualmente modificati su main e non autorizza una pubblicazione senza questi riscontri.

Prossima azione: Completare il giudizio documentale locale; acquisire e sincronizzare prima della PR.
