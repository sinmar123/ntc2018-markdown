"""Genera le voci di divisione dei capoversi: per ogni inizio di capoverso della fonte che nel target segue testo sulla stessa riga."""
import json, sys, glob
fonte=json.load(open(sys.argv[1]))
# falsi positivi verificati a mano: righe di continuazione rientrate delle note, voci già separate, Nota 3, LC3 (continuazione)
ESCLUSI={(261,411.2),(261,419.4),(261,430.2),(261,438.3),(261,457.3),(261,465.6),(262,463.4),(262,471.6),(262,482.4),(262,493.1),(262,501.3),(262,512.2),
 (266,209.2),(266,552.9),(266,663.2),(267,383.3),(268,547.0),(268,574.3),(268,601.5),(268,620.4)}
files=sorted(glob.glob("cap08/8.5*.md"))
voci=[]
for f in files:
    raw=open(f,encoding="utf-8").read()
    norm=[];pos=[]
    for i,ch in enumerate(raw):
        if ch.isalnum(): norm.append(ch.lower()); pos.append(i)
    norm="".join(norm)
    for atto in ("ntc","circ"):
        for c in fonte[atto]:
            if (c["p"],c["y"]) in ESCLUSI: continue
            key="".join(ch.lower() for ch in c["testo"] if ch.isalnum())[:40]
            if len(key)<12: continue
            k=-1
            while True:
                k=norm.find(key,k+1)
                if k<0: break
                i=pos[k]; j=i
                while j>0 and raw[j-1] in "*_": j-=1
                ls=raw.rfind("\n",0,j)+1
                riga=raw[ls:raw.find("\n",j) if raw.find("\n",j)>0 else len(raw)]
                if riga.startswith(("#","<","  ","- [","[Torna")): continue
                prima=raw[ls:j]
                if prima.startswith("- "): prima=prima[2:]
                if not prima.strip(" *"): continue
                if raw[j-1]!=" ": continue
                for w in range(30,200,5):
                    att=raw[j-w:j+25]
                    if raw.count(att)==1: break
                prop=raw[j-w:j-1]+"\n\n"+raw[j:j+25]
                voci.append({"file":f,"pagina":f"{'Circolare' if atto=='circ' else 'NTC'} p. {c['p']}","y_pt":c["y"],"attuale":att,"proposto":prop})
json.dump(voci,open(sys.argv[2],"w"),ensure_ascii=False,indent=1)
print(len(voci))
for v in voci: print(v["file"][6:30],v["pagina"],v["y_pt"],repr(v["attuale"][20:45]))
