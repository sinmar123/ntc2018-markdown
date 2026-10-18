## Stato

Bozza: applicazione e G5 completati; G6 integrale concluso con rilievi aperti; G7 non eseguito.

## Cosa cambia

- applicate via `vc-supporto.py` le 206 correzioni approvate da Sandro per il solo § 8.7.1/C8.7.1, di cui 21 sostanziali e 185 di forma;
- rigenerati e verificati gli indici interni;
- aggiunti dossier, snapshot, prove G0-G5 e rapporti del giro G6 indipendente;
- nessuna modifica ad altri file normativi e nessuna modifica al master esterno.

## Perimetro e verifiche

Lo scope reale comprende NTC pp. PDF 297-298 e Circolare pp. PDF 270-283: 16 pagine, una oltre la soglia consigliata di 15 già segnalata durante G0. Il target finale ha SHA-256 `09eab0335ca26594b29ea19f279acf1da8496550f70883b55fa6695a4b0ba6c8`; `verifica-lista` sulla base `92a449e` ha dato `OK`.

G5 ha verificato 662 righe depurate, 25 link, 311 file e 1754 collegamenti interni. La resa canonica è di 18 pagine, con tutti i 18 tag di formula presenti e senza tagli, sovrapposizioni o glifi mancanti.

G6, giro 1, ha coperto integralmente 180/180 ID in quattro blocchi:

- b01: 55 ID, `KO`, 3 `ERR-MD` e 1 `ERR-AUDIT`;
- b02: 25 ID, `OK`, zero rilievi;
- b03: 53 ID, `KO`, 3 `ERR-MD`;
- b04: 47 ID, `KO`, 7 `ERR-MD`.

Totale: 13 `ERR-MD`, 1 `ERR-AUDIT`, zero `DUBBIO`. I rilievi sono riportati integralmente nei rapporti G6. Non sono stati corretti e non è stata avviata una seconda tornata. G7 è vietato dalla procedura finché G6 non è a zero rilievi; la riga resta `IN-CORSO` e richiede una decisione di Sandro.

## Limiti ed evidenze locali

L'isolamento dei V è stato istruttivo, in contesti nuovi e cartelle temporanee esterne; il runtime non documenta una sandbox di lettura effettiva né espone l'identificativo del modello, mentre il profilo richiesto era `gpt-5.6-sol` con ragionamento `xhigh`. Due V hanno dovuto leggere le sole istruzioni generali di skill e procedura per obbligo del runtime, senza accedere a target, rapporti o giudizi precedenti.

PNG, PDF, SVG, ritagli ad alta risoluzione, pacchetti originali con percorsi locali e altri binari di prova restano locali e sono rappresentati da impronte. Le copie pubblicate sono prive di percorsi personali; la redazione dei soli percorsi è documentata in `archiviazione-g6.json`.

Preparazione: Codex (CDX), 2026-10-17.
