"""Confronta i capoversi della fonte con il target: segnala inizi di capoverso che nel target stanno a metà paragrafo."""
import json, sys, re, glob
fonte=json.load(open(sys.argv[1]))
files=sorted(glob.glob("cap08/8.5*.md"))
raw=""; spans=[]
for f in files:
    t=open(f,encoding="utf-8").read(); spans.append((len(raw),f)); raw+=t+"\n\n"
norm=[];pos=[]
for i,ch in enumerate(raw):
    if ch.isalnum(): norm.append(ch.lower()); pos.append(i)
norm="".join(norm)
def nz(s): return "".join(c.lower() for c in s if c.isalnum())
def fileof(i):
    f=[s for s in spans if s[0]<=i][-1]; return f[1], raw[f[0]:i].count("\n")+1
cur=0; out=[]
for atto in ("ntc","circ"):
    for c in fonte[atto]:
        key=nz(c["testo"])[:40]
        if len(key)<12: continue
        k=norm.find(key, cur)
        if k<0: k=norm.find(key)
        if k<0: out.append(("NONTROVATO",c["p"],c["testo"][:60])); continue
        cur=k
        i=pos[k]
        # contesto precedente nel raw, saltando marcatori
        j=i
        while j>0 and raw[j-1] in "*_#> -[(": j-=1
        prec=raw[max(0,j-2):j]
        ok = prec.endswith("\n") or j==0 or raw[j-1]=="|"
        if not ok:
            f,l=fileof(i); out.append(("FUSO",f,l,c["p"],c["y"],raw[max(0,i-40):i].replace("\n","⏎"),raw[i:i+40]))
for o in out: print(o)
print(len(out))
