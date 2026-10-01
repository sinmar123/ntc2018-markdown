# Elenco delle non conformità, § 8.2

Firma: GROK, grok-4.6 xhigh, ruolo C. Data: 2026-09-12. Procedura VC-NTC/4. Target invariato. Nessuna correzione applicata.

## Perimetro (G0 OK)

Solo `cap08/8.2-criteri-generali.md`. NTC p. fisica 294, da `8.2. CRITERI GENERALI` fino a prima di `8.3`. Circolare pp. 254-255, da `C8.2 CRITERI GENERALI` fino a prima di `C8.3`, compresa la nota a piè ¹. 8.1 e 8.3 esclusi.

## G1 OK

Ricognizione 2026-09-09 riusata; ricontrollo mirato 2026-09-12 sugli stessi atti già aperti per 8.1 e 3.1. Nessuna modifica a 8.2/C8.2. PDF: NTC `dda1e397…`, Circolare `f7c3b8d1…`.

## G4 OK

Zero formule numerate, tabelle, figure.

## Residui da decidere (G2-G3 KO)

La prosa della NTC § 8.2 coincide con la fonte (spazi, a capo e trattini degli elenchi: catalogo N1/N2). I tre punti sotto riguardano solo la Circolare C8.2. Le parole ci sono tutte.

| ID | Dove | Cosa stampa la Gazzetta | Cosa c'è nel Markdown | Classe |
|---|---|---|---|---|
| R1 | circ:254, rubrica | `C8.2` e `CRITERI GENERALI` in maiuscolo, senza punto dopo C8.2 | `## C8.2. Criteri generali` | ERR-MD |
| R2 | circ:254-255, corpo | quattro capoversi prima della nota e dieci dopo, ciascuno a sé | due soli blocchi di testo | ERR-MD |
| R3 | circ:254, nota ¹ | richiamo in apice e nota a piè, due capoversi | richiamo `[1]` e `**Nota 1.**` nel flusso del testo | ERR-MD |

Conservare, se si corregge R2-R3: la virgola di `Attenzione deve essere, dedicata` e `D.M.` / `§8.4.1` come in fonte. Catalogo N1 copre gli a capo *dentro* un capoverso, non la fusione di capoversi.

G5 e G6 non avviati. Snapshot `3bf1ca93135c73fdb0519a4210ee3cada4f88a622c9507adb7955a802d4c4999`.

Prossima azione: Attendere la decisione di Sandro su R1, R2 e R3.
