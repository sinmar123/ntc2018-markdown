"""Voci R: rubriche della Circolare come nella fonte, senza punto dopo il numero e in maiuscolo (precedenti: § C3.1.4, § 8.4)."""
import json, sys, glob, re
FONTE={"C8.5":"DEFINIZIONE DEL MODELLO DI RIFERIMENTO PER LE ANALISI","C8.5.1":"ANALISI STORICO-CRITICA","C8.5.2":"RILIEVO",
"C8.5.2.1":"COSTRUZIONI DI MURATURA","C8.5.2.2":"COSTRUZIONI DI CALCESTRUZZO ARMATO O ACCIAIO","C8.5.2.3":"COSTRUZIONI DI LEGNO",
"C8.5.3":"CARATTERIZZAZIONE MECCANICA DEI MATERIALI","C8.5.3.1":"COSTRUZIONI DI MURATURA","C8.5.3.2":"COSTRUZIONI DI CALCESTRUZZO ARMATO O ACCIAIO","C8.5.3.3":"COSTRUZIONI DI LEGNO",
"C8.5.4":"LIVELLI DI CONOSCENZA E FATTORI DI CONFIDENZA","C8.5.4.1":"COSTRUZIONI DI MURATURA","C8.5.4.2":"COSTRUZIONI DI CALCESTRUZZO ARMATO O DI ACCIAIO","C8.5.4.3":"COSTRUZIONI DI LEGNO",
"C8.5.5":"AZIONI","C8.5.5.1":"COSTRUZIONI IN MURATURA","C8.5.5.2":"COSTRUZIONI DI CALCESTRUZZO ARMATO O ACCIAIO"}
PAG={"C8.5":257,"C8.5.1":258,"C8.5.2":258,"C8.5.2.1":258,"C8.5.2.2":258,"C8.5.2.3":260,"C8.5.3":260,"C8.5.3.1":260,"C8.5.3.2":264,"C8.5.3.3":264,"C8.5.4":265,"C8.5.4.1":266,"C8.5.4.2":267,"C8.5.4.3":268,"C8.5.5":269,"C8.5.5.1":269,"C8.5.5.2":269}
voci=[];n=0
for f in sorted(glob.glob("cap08/8.5*.md")):
    t=open(f,encoding="utf-8").read()
    for m in re.finditer(r"^(#+) (C8\.5(?:\.\d)*)\. (.+)$",t,re.M):
        num=m.group(2); assert m.group(3).upper()==FONTE[num],(num,m.group(3)); n+=1
        voci.append({"id":f"R{n}","file":f,"pagina":f"Circolare p. {PAG[num]}","attuale":m.group(0),"proposto":f"{m.group(1)} {num} {FONTE[num]}","nota":"rubrica come nella fonte"})
json.dump(voci,open(sys.argv[1],"w"),ensure_ascii=False,indent=1); print(len(voci))
