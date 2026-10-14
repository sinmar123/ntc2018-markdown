"""Voci puntuali (O) come coppie attuale/proposto, verificate univoche sul testo corrente."""
import json, sys, glob
def F(k): return glob.glob(f"cap08/{k}-*.md")[0]
f3,f4,f5=F("8.5.3"),F("8.5.4"),F("8.5.5")
O=[
 ("O1",f3,"compressione fm stimabile tra 0,7 e 1,5 N/mm2)","compressione $f_m$ stimabile tra 0,7 e 1,5 N/mm²)","Circolare p. 260","pedice ed esponente della fonte"),
 ("O2",f3,"compressione fm stimabile inferiore a 0,7 N/mm2)","compressione $f_m$ stimabile inferiore a 0,7 N/mm²)","Circolare p. 260","pedice ed esponente della fonte"),
 ("O3",f3,"diverse tipologie di muratura.*\n\nI valori si riferiscono a: $f$ = resistenza media a compressione, $\\tau_0$ = resistenza media a taglio in assenza di tensioni normali (con riferimento alla formula riportata, a proposito dei modelli di capacità, nel §C8.7.1.3), $f_{v0}$ = resistenza media a taglio in assenza di tensioni normali (con riferimento alla formula riportata, a proposito dei modelli di capacità, nel §C8.7.1.3), $E$ = valore medio del modulo di elasticità normale, $G$ = valore medio del modulo di elasticità tangenziale, $w$ = peso specifico medio.",
  "diverse tipologie di muratura. I valori si riferiscono a:* $f$ *= resistenza media a compressione,* $\\tau_0$ *= resistenza media a taglio in assenza di tensioni normali (con riferimento alla formula riportata, a proposito dei modelli di capacità, nel §C8.7.1.3),* $f_{v0}$ *= resistenza media a taglio in assenza di tensioni normali (con riferimento alla formula riportata, a proposito dei modelli di capacità, nel §C8.7.1.3),* $E$ *= valore medio del modulo di elasticità normale,* $G$ *= valore medio del modulo di elasticità tangenziale,* $w$ *= peso specifico medio.*",
  "Circolare p. 261","definizioni dei simboli dentro la didascalia in corsivo, come nella fonte"),
 ("O4",f3,"| Tipologia di muratura | Stato di fatto / Malta buona | Stato di fatto / Ricorsi o listature | Stato di fatto / Connessione trasversale | Interventi di consolidamento / Iniezione di miscele leganti (*) | Interventi di consolidamento / Intonaco armato (**) | Interventi di consolidamento / Ristilatura armata con connessione dei paramenti (**) | Interventi di consolidamento / Massimo coefficiente complessivo |\n|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|\n",
  "| Tipologia di muratura | Stato di fatto | | | Interventi di consolidamento | | | |\n|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|\n| | Malta buona | Ricorsi o listature | Connessione trasversale | Iniezione di miscele leganti (*) | Intonacoarmato (**) | Ristilatura armata con connessione dei paramenti (**) | Massimo coefficiente complessivo |\n",
  "Circolare p. 262","testata su due livelli secondo il catalogo n. 6, come le Tabelle C8.5.V e C8.5.VI; «Intonacoarmato» come stampa la fonte (A)"),
 ("O5",f3,"secondo le modalità di seguito illustrate.","secondo le modalità di seguito illustrate","Circolare p. 262","la fonte non ha il punto finale (A)"),
 ("O6",f4,"l’analisi storico- critica","l’analisi storico-critica","Circolare p. 265","spazio aggiunto"),
 ("O7",f4,"| Prova di compressione e taglio (su un pannello isolato nella parete muraria) - prova tipo Sheppard | $G$","| Prova di compressione e taglio (su un pannello isolato nella parete muraria) – prova tipo Sheppard | $G$","Circolare p. 266","lineetta della fonte"),
 ("O8",f4,"| Prova di compressione e taglio (su un pannello isolato nella parete muraria) - prova tipo Sheppard | $\\tau_0","| Prova di compressione e taglio (su un pannello isolato nella parete muraria) – prova tipo Sheppard | $\\tau_0","Circolare p. 266","lineetta della fonte"),
 ("O9",f4,"| Livello di Indagini e Prove | Rilievo (dei dettagli costruttivi) (a) | Prove (sui materiali) (b)(c)(d) |","| Livello di Indagini e Prove | Rilievo(dei dettagli costruttivi)$^{\\text{(a)}}$ | Prove (sui materiali)$^{\\text{(b)(c)(d)}}$ |","Circolare p. 268","richiami in apice; «Rilievo(dei» senza spazio come la fonte (A)"),
 ("O10",f4,"| Livello di Indagini e Prove | Rilievo (dei collegamenti) (a) | Prove (sui materiali) (b)(c)(d) |","| Livello di Indagini e Prove | Rilievo (dei collegamenti)$^{\\text{(a)}}$ | Prove (sui materiali)$^{\\text{(b)(c)(d)}}$ |","Circolare p. 268","richiami in apice"),
 ("O11",f4,"dei parametri μ’ e σ’ della","dei parametri $\\mu'$ e $\\sigma'$ della","Circolare p. 266","greche come simboli (decisione di Sandro)"),
 ("O12",f4,"prove dirette e κ è un coef","prove dirette e $\\kappa$ è un coef","Circolare p. 266",""),
 ("O13",f4,"e la varianza σ’² della","e la varianza $\\sigma'^2$ della","Circolare p. 266",""),
 ("O14",f4,"il coefficiente κ rappresenta","il coefficiente $\\kappa$ rappresenta","Circolare p. 266",""),
 ("O15",f4,"dal valore μ’ adottato","dal valore $\\mu'$ adottato","Circolare p. 266",""),
 ("O16",f4,"differenza tra μ’ e μ”","differenza tra $\\mu'$ e $\\mu''$","Circolare p. 266","apice doppio come nella formula [C8.5.4.3]"),
 ("O17",f4,"coefficiente κ è opportuno","coefficiente $\\kappa$ è opportuno","Circolare p. 266","nota 3"),
 ("O18",f4,"coefficiente κ per i più","coefficiente $\\kappa$ per i più","Circolare p. 266","nota 3"),
 ("O19",f4,"**LC2:**\n\n- Resistenze","**LC2**:\n\n- Resistenze","Circolare p. 266","i due punti sono in tondo nella fonte"),
 ("O20",f4,"sperimentali[3]. Qualora","sperimentali[3].\n\nQualora","Circolare p. 266","capoverso della fonte"),
 ("O21",f5,"assegnando a γG valori","assegnando a $\\gamma_G$ valori","NTC p. 297","pedice della fonte; la γ in testo semplice spariva anche nella resa"),
]
voci=[]
for i,f,a,p,pag,nota in O:
    t=open(f,encoding="utf-8").read()
    n=t.count(a)
    if n!=1: print("NON UNIVOCO",i,n); continue
    voci.append({"id":i,"file":f,"pagina":pag,"attuale":a,"proposto":p,"nota":nota})
json.dump(voci,open(sys.argv[1],"w"),ensure_ascii=False,indent=1); print(len(voci))
