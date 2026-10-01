# Rapporto C G2-G4, stato iniziale del § 3.4.5

Data: 2026-09-09. Coordinatore: Hermes NTC-VC / HRM. Confronto svolto sulle pagine fisiche NTC 63 e Circolare 81, con raster a 200 e 600 dpi, estrazioni di testo e `rawdict`, e target iniziale depurato congelato.

## Inventario fonte-prima del coordinatore

- Rubriche: 2, `3.4.5. COEFFICIENTE TERMICO` e `C3.4.5 COEFFICIENTE TERMICO`.
- Corpo NTC: 1 capoverso, 3 periodi.
- Corpo Circolare: 3 capoversi, 3 periodi complessivi.
- Tabelle, figure, formule numerate, note e rimandi: nessuno.
- Elementi inline sostanziali: `C` con pedice `t` e valore `1`; `1,5 kN/m²`; `1 W/m²K°`; `0°C`; `1,2`.
- Asset locali necessari: nessuno.
- Confine iniziale: rubrica `3.4.5.` della NTC.
- Confine finale: periodo `neve al suolo.` della Circolare; fuori scope iniziano `3.5.` nella NTC e `C3.4.5.1` nella Circolare.

## Trascrizione di controllo

### NTC

`3.4.5. COEFFICIENTE TERMICO`

`Il coefficiente termico tiene conto della riduzione del carico della neve, a causa dello scioglimento della stessa, causata dalla perdita di calore della costruzione. Tale coefficiente dipende dalle proprietà di isolamento termico del materiale utilizzato in copertura. In assenza di uno specifico e documentato studio, deve essere posto C_t = 1.`

Il `t` è un pedice reale: nel `rawdict` ha corpo 5,066 pt rispetto ai 7,599 pt del testo e posizione verticale ribassata. Il glifo `C` e il pedice sono nello stesso carattere romano Palatino del corpo, non in corsivo matematico.

### Circolare

`C3.4.5 COEFFICIENTE TERMICO`

`L’adozione di valori inferiori all’unità del coefficiente termico è da sconsigliarsi in linea generale.`

`Laddove adeguatamente motivato può applicarsi solamente per coperture ricadenti in località nelle quali il carico della neve al suolo è superiore a 1,5 kN/m², e caratterizzate da trasmittanza superiore a 1 W/m²K°`

`Per edifici nei quali la temperatura interna è mantenuta intenzionalmente sotto 0°C (edifici frigoriferi, impianti per il pattinaggio su ghiaccio ecc.) si raccomanda di assumere il valore del coefficiente termico pari a 1,2, indipendentemente dal valore del carico neve al suolo.`

Il secondo capoverso termina con `K°` senza punto fermo. L’estrazione strutturata conferma i due `2` in apice e non registra alcun segno dopo `K°`.

## Esito del confronto iniziale

1. `ERR-MD-01`: la rubrica NTC è in cassa mista nel target, ma tutta maiuscola nella fonte.
2. `ERR-MD-02`: `$C_t$` rende `C` e `t` in corsivo matematico; la fonte li mostra romani con `t` a pedice. Forma approvata: `$\mathrm{C}_{\mathrm{t}}$`.
3. `ERR-MD-03`: la rubrica della Circolare ha nel target un punto non presente dopo `C3.4.5` ed è in cassa mista anziché maiuscola.
4. `ERR-MD-04`: il target aggiunge un punto fermo dopo `1 W/m²K°`; la fonte non lo presenta.

Non risultano altre differenze nel lessico, nei cinque valori inline, nelle unità, nei tre capoversi della Circolare o nella punteggiatura restante. Le elisioni dritte del target sono ammesse da N01; i ritorni di riga e le parole spezzate a fine riga sono trattati secondo N03 e N10.

## Lista chiusa delle sostituzioni affidate a E

Nel solo file `cap03/3.4.5-neve-coefficiente-termico.md`:

1. `# 3.4.5. Coefficiente termico` → `# 3.4.5. COEFFICIENTE TERMICO`.
2. `deve essere posto $C_t$ = 1.` → `deve essere posto $\mathrm{C}_{\mathrm{t}}$ = 1.`.
3. `### C3.4.5. Coefficiente termico` → `### C3.4.5 COEFFICIENTE TERMICO`.
4. `superiore a 1 W/m²K°.` → `superiore a 1 W/m²K°`.

E non è autorizzato a modificare altri file, a riscrivere frasi, a cambiare valori o a introdurre normalizzazioni ulteriori.

## Stato dei gate

- G2: `OK`, inventario completato.
- G3: `OK_CON_RILIEVI`, quattro differenze chiuse e classificabili.
- G4: `OK_CON_RILIEVI`, cassa, pedice e punto finale verificati anche sul raster 600 dpi e sui dati strutturati.
- Correzione: necessaria prima della ripetizione G3-G4 e del G5.

Firma: Hermes NTC-VC / HRM.
