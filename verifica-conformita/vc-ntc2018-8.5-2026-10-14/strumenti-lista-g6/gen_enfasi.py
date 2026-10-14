"""Genera le voci di enfasi (grassetto, corsivo, grassetto corsivo) come coppie attuale/proposto univoche.
Ogni specifica: (file, ancora del capoverso, locuzione, occorrenza nel capoverso da 1, apertura, chiusura, pagina, nota)."""
import json, sys, glob
F={k:glob.glob(f"cap08/{k}-*.md")[0] for k in ("8.5.2","8.5.3","8.5.4")}
F["ntc8.5.3"]=F["8.5.3"]
BI=("***","***"); B=("**","**"); I=("*","*")
S=[
 ("8.5.3","Per conseguire un’adeguata conoscenza","in situ",1,("in *","*"),"NTC p. 297","«situ» in corsivo"),
 # C8.5.2.1, p. 258
 ("8.5.2","Nelle costruzioni di muratura, vista","Indagini limitate:",1,("***","*:**"),"Circolare p. 258","etichetta in grassetto corsivo, due punti in grassetto"),
 ("8.5.2","Nelle costruzioni di muratura, vista","Indagini estese:",1,BI,"Circolare p. 258","etichetta e due punti in grassetto corsivo"),
 ("8.5.2","Nelle costruzioni di muratura, vista","Indagini esaustive:",1,("***","*:**"),"Circolare p. 258",""),
 # C8.5.2.2, p. 259
 ("8.5.2","Nel caso in cui la geometria della struttura sia nota","Indagini limitate:",1,("***","*:**"),"Circolare p. 259",""),
 ("8.5.2","Nel caso in cui la geometria della struttura sia nota","Indagini estese",1,BI,"Circolare p. 259","due punti in tondo"),
 ("8.5.2","Nel caso in cui la geometria della struttura sia nota","Indagini esaustive:",1,("***","*:**"),"Circolare p. 259",""),
 ("8.5.2","rilievi dei particolari costruttivi (sfruttando","Costruzioni di calcestruzzo armato",1,BI,"Circolare p. 259","sottotitolo in grassetto corsivo"),
 ("8.5.2","Costruzioni di acciaio:","Costruzioni di acciaio:",1,BI,"Circolare p. 259","sottotitolo in grassetto corsivo"),
 # C8.5.3.1, pp. 261-263
 ("8.5.3","- **malta di buone","**malta di buone caratteristiche**:",1,("***malta di buone caratteristiche*:**",""),"Circolare p. 261","da grassetto a grassetto corsivo; due punti in grassetto"),
 ("8.5.3","- **presenza di ricorsi","**presenza di ricorsi (o listature)**:",1,("***presenza di ricorsi (o listature):***",""),"Circolare p. 261","grassetto corsivo, due punti compresi"),
 ("8.5.3","- **presenza sistematica","**presenza sistematica di elementi di collegamento trasversale tra i paramenti**:",1,("***presenza sistematica di elementi di collegamento trasversale tra i paramenti*:**",""),"Circolare p. 261",""),
 ("8.5.3","I muri realizzati con due paramenti","nucleo interno",1,I,"Circolare p. 262","solo la seconda occorrenza del capoverso, «nel caso in cui il nucleo interno sia ampio»"),
 ("8.5.3","**Consolidamento con iniezioni","**Consolidamento con iniezioni di miscele leganti**",1,("***Consolidamento con iniezioni di miscele leganti***",""),"Circolare p. 262","da grassetto a grassetto corsivo"),
 ("8.5.3","**Consolidamento con intonaco","**Consolidamento con intonaco armato**",1,("***Consolidamento con intonaco armato***",""),"Circolare p. 262",""),
 ("8.5.3","Consolidamento con diatoni","Consolidamento con diatoni artificiali o tirantini antiespulsivi",1,BI,"Circolare p. 263","rubrica in grassetto corsivo; il capoverso si divide a parte"),
 ("8.5.3","**Consolidamento con ristilatura","**Consolidamento con ristilatura armata e connessione dei paramenti**",1,("***Consolidamento con ristilatura armata e connessione dei paramenti***",""),"Circolare p. 263",""),
 ("8.5.3","**Prove limitate:** Si tratta","**Prove limitate:**",1,("***Prove limitate:***",""),"Circolare p. 263",""),
 ("8.5.3","**Prove estese:** Si tratta","**Prove estese:**",1,("***Prove estese:***",""),"Circolare p. 263",""),
 ("8.5.3","**Prove esaustive:** In aggiunta","**Prove esaustive:**",1,("***Prove esaustive:***",""),"Circolare p. 263",""),
 # C8.5.3.2, p. 264
 ("8.5.3","I valori delle caratteristiche meccaniche dei materiali prescindono","Calcestruzzo",1,BI,"Circolare p. 264","due punti in tondo"),
 ("8.5.3","I valori delle caratteristiche meccaniche dei materiali prescindono","Acciaio",1,BI,"Circolare p. 264","due punti in tondo"),
 ("8.5.3","I valori delle caratteristiche meccaniche dei materiali prescindono","Unioni di elementi d’acciaio:",1,("***","*:**"),"Circolare p. 264",""),
 ("8.5.3","I valori delle caratteristiche meccaniche dei materiali prescindono","Prove limitate:",1,("***","*:**"),"Circolare p. 264",""),
 ("8.5.3","I valori delle caratteristiche meccaniche dei materiali prescindono","Prove estese:",1,("***","*:**"),"Circolare p. 264",""),
 ("8.5.3","I valori delle caratteristiche meccaniche dei materiali prescindono","prove limitate",1,BI,"Circolare p. 264","«con le prove limitate risultino inferiori»"),
 ("8.5.3","I valori delle caratteristiche meccaniche dei materiali prescindono","Prove esaustive:",1,("***","*:**"),"Circolare p. 264",""),
 ("8.5.3","I valori delle caratteristiche meccaniche dei materiali prescindono","prove, limitate o estese",1,BI,"Circolare p. 264",""),
 # C8.5.3.3, p. 265
 ("8.5.3","L’esame degli elementi costruttivi","Prove limitate:",1,("***","***:"),"Circolare p. 265","D3: due punti e «s» di «si» in corsivo tondo non riprodotti"),
 ("8.5.3","L’esame degli elementi costruttivi","Prove estese:",1,BI,"Circolare p. 265","D3: la «s» di «si» in grassetto corsivo non riprodotta"),
 ("8.5.3","L’esame degli elementi costruttivi","Prove esaustive:",1,BI,"Circolare p. 265",""),
 # C8.5.4, p. 265
 ("8.5.4","I fattori di confidenza sono utilizzati","Fattori di Confidenza (FC)",1,("*Fattori di Confidenza* (**FC**)",""),"Circolare p. 265","sigla FC in grassetto"),
 ("8.5.4","I fattori di confidenza sono utilizzati","Livelli di Conoscenza (LC)",1,("***L****ivelli di* ***C****onoscenza* (**LC**)",""),"Circolare p. 265","iniziali L e C in grassetto corsivo, resto in corsivo, sigla in grassetto"),
 ("8.5.4","I fattori di confidenza sono utilizzati","LC1:",1,B,"Circolare p. 265",""),
 ("8.5.4","I fattori di confidenza sono utilizzati","indagini limitate",1,BI,"Circolare p. 265",""),
 ("8.5.4","I fattori di confidenza sono utilizzati","prove limitate",1,BI,"Circolare p. 265",""),
 ("8.5.4","I fattori di confidenza sono utilizzati","FC=1,35",1,B,"Circolare p. 265",""),
 ("8.5.4","I fattori di confidenza sono utilizzati","LC2",1,B,"Circolare p. 265","«non è LC2 solo a causa»"),
 ("8.5.4","I fattori di confidenza sono utilizzati","LC2:",1,B,"Circolare p. 265",""),
 ("8.5.4","I fattori di confidenza sono utilizzati","indagini estese",1,BI,"Circolare p. 265",""),
 ("8.5.4","I fattori di confidenza sono utilizzati","prove estese",1,BI,"Circolare p. 265",""),
 ("8.5.4","I fattori di confidenza sono utilizzati","FC=1,2",1,B,"Circolare p. 265",""),
 ("8.5.4","I fattori di confidenza sono utilizzati","LC3",1,B,"Circolare p. 265","«non è LC3 solo a causa»"),
 ("8.5.4","I fattori di confidenza sono utilizzati","LC3:",1,B,"Circolare p. 265",""),
 ("8.5.4","I fattori di confidenza sono utilizzati","indagini esaustive",1,BI,"Circolare p. 265",""),
 ("8.5.4","I fattori di confidenza sono utilizzati","prove esaustive",1,BI,"Circolare p. 265",""),
 ("8.5.4","I fattori di confidenza sono utilizzati","FC=1",3,B,"Circolare p. 265","«FC=1 (da applicarsi»"),
 ("8.5.4","I fattori di confidenza sono utilizzati","valore di FC",1,("valore di **FC**",""),"Circolare p. 265",""),
 ("8.5.4","I fattori di confidenza sono utilizzati","conoscenza LC3",1,("conoscenza **LC3**",""),"Circolare p. 265",""),
 # C8.5.4.2, pp. 267-268
 ("8.5.4","**LC1:** si intende raggiunto quando sia stata","indagini limitate",1,BI,"Circolare p. 267",""),
 ("8.5.4","**LC1:** si intende raggiunto quando sia stata","prove limitate",1,BI,"Circolare p. 267",""),
 ("8.5.4","**LC1:** si intende raggiunto quando sia stata","FC=1,35",1,B,"Circolare p. 267",""),
 ("8.5.4","**LC2:** si intende raggiunto quando sia stata","indagini limitate",1,BI,"Circolare p. 267",""),
 ("8.5.4","**LC2:** si intende raggiunto quando sia stata","indagine estesa",1,BI,"Circolare p. 267",""),
 ("8.5.4","**LC2:** si intende raggiunto quando sia stata","prove limitate",1,BI,"Circolare p. 267",""),
 ("8.5.4","**LC2:** si intende raggiunto quando sia stata","prove estese",1,BI,"Circolare p. 267",""),
 ("8.5.4","**LC2:** si intende raggiunto quando sia stata","prove estese",2,BI,"Circolare p. 267",""),
 ("8.5.4","**LC2:** si intende raggiunto quando sia stata","FC=1,2",1,B,"Circolare p. 267",""),
 ("8.5.4","**LC3:** si intende raggiunto quando sia stata","indagini limitate",1,BI,"Circolare p. 267",""),
 ("8.5.4","**LC3:** si intende raggiunto quando sia stata","indagine esaustiva",1,BI,"Circolare p. 267",""),
 ("8.5.4","**LC3:** si intende raggiunto quando sia stata","prove limitate",1,BI,"Circolare p. 267",""),
 ("8.5.4","**LC3:** si intende raggiunto quando sia stata","prove esaustive",1,BI,"Circolare p. 268",""),
 ("8.5.4","**LC3:** si intende raggiunto quando sia stata","prove esaustive",2,BI,"Circolare p. 268",""),
 ("8.5.4","**LC3:** si intende raggiunto quando sia stata","FC=1",1,B,"Circolare p. 268",""),
 ("8.5.4","**LC3:** si intende raggiunto quando sia stata","gli FC",1,("gli **FC**",""),"Circolare p. 268",""),
 ("8.5.4","**LC3:** si intende raggiunto quando sia stata","Gli FC",1,("Gli **FC**",""),"Circolare p. 268",""),
]
testi={f:open(f,encoding="utf-8").read() for f in set(F.values())}
voci=[]
for n,(k,anc,loc,occ,(a,c),pag,nota) in enumerate(S,1):
    f=F[k]; t=testi[f]
    assert t.count(anc)>=1,(k,anc)
    i=t.index(anc); fine=t.find("\n\n",i); fine=len(t) if fine<0 else fine
    i=t.rfind("\n",0,i)+1
    j=i
    try:
      for _ in range(occ):
        j=t.index(loc,j,fine)+ (0 if _==occ-1 else len(loc))
    except ValueError: print("NON TROVATO",n,k,anc,loc); continue
    if c=="" : nuovo=a
    elif a=="in *": nuovo="in *situ*"
    else: nuovo=a+loc+c if not loc.endswith(":") or c not in ("*:**","***:") else a+loc[:-1]+c
    # contesto univoco
    for w in range(8,80):
        att=t[j-w:j+len(loc)+w]
        if t.count(att)==1: break
    prop=t[j-w:j]+nuovo+t[j+len(loc):j+len(loc)+w]
    t=t[:j]+nuovo+t[j+len(loc):]; testi[f]=t
    voci.append({"id":f"E{n}","file":f,"pagina":pag,"attuale":att,"proposto":prop,"nota":nota})
json.dump(voci,open(sys.argv[1],"w"),ensure_ascii=False,indent=1)
for v in voci: print(v["id"],v["pagina"],repr(v["proposto"][:110]))
