"""Estrae dalla fonte capoversi e tratti in enfasi del perimetro 8.5 (solo prosa, tabelle escluse)."""
import pymupdf as fitz, json, sys, re
CIRC="verifica-conformita/fonte-ufficiale/GU-2019-35-SO5-Circolare-7-2019.pdf"
NTC="verifica-conformita/fonte-ufficiale/GU-2018-42-SO8-DM-17-01-2018.pdf"
def stile(f):
    f=f.replace("PalatinoLinotype-","")
    if "BoldIta" in f or "BoldItalic" in f: return "bi"
    if "Bold" in f: return "b"
    if "Italic" in f: return "i"
    return ""
def pagine(pdf, pp, inizio, fine):
    d=fitz.open(pdf); out=[]
    for p in pp:
        pg=d[p-1]
        tabs=[t.bbox for t in pg.find_tables().tables] if not (pdf==CIRC and p==265) else []  # p. 265: falsa tabella sul capoverso «Prove esaustive»
        righe=[]
        for b in pg.get_text("dict")["blocks"]:
            for l in b.get("lines",[]):
                x0,y0,x1,y1=l["bbox"]
                if y0<70 or y0>740: continue
                if any(tb[1]-2<=y0<=tb[3]+2 and tb[0]-2<=x0<=tb[2]+2 for tb in tabs): continue
                spans=[(s["text"],stile(s["font"]),round(s["size"],1),s["font"]) for s in l["spans"] if s["text"]]
                t="".join(s[0] for s in spans)
                if not t.strip(): continue
                righe.append(dict(p=p,x0=x0,x1=x1,y0=y0,y1=y1,t=t,spans=spans))
        righe.sort(key=lambda r:(round(r["y0"]),r["x0"]))
        out+=righe
    # taglia al perimetro
    i=next(k for k,r in enumerate(out) if inizio(r)); j=next((k for k,r in enumerate(out) if k>i and fine(r)),len(out))
    return out[i:j]
def capoversi(righe):
    cap=[];prev=None
    for r in righe:
        nuovo = prev is None or (r["p"]==prev["p"] and r["y0"]-prev["y1"]>4.2) or (r["p"]!=prev["p"] and prev["x1"]<500) or r["x0"]>prev["x0"]+8 or r["x0"]<prev["x0"]-8
        if prev and abs(r["y0"]-prev["y0"])<2: nuovo=False  # stessa riga (rubrica numero+titolo)
        if nuovo: cap.append(dict(p=r["p"],y=round(r["y0"],1),x=round(r["x0"],1),righe=[r]))
        else: cap[-1]["righe"].append(r)
        prev=r
    for c in cap:
        c["testo"]=" ".join(x["t"].strip() for x in c["righe"])
        c["spans"]=[s for x in c["righe"] for s in x["spans"]]
    return cap
if __name__=="__main__":
    circ=pagine(CIRC,range(257,270),lambda r:r["t"].startswith("C8.5") and r["p"]==257,lambda r:r["t"].startswith("C8.6"))
    ntc=pagine(NTC,range(296,298),lambda r:r["t"].startswith("8.5."),lambda r:r["t"].startswith("8.6"))
    res={"circ":capoversi(circ),"ntc":capoversi(ntc)}
    for k in res:
        for c in res[k]: c.pop("righe")
    json.dump(res,open(sys.argv[1],"w"),ensure_ascii=False,indent=1)
    for k in res:
        print(k,len(res[k]))
        for c in res[k]: print(f"  {c['p']} {c['y']:6} x{c['x']:5} | {c['testo'][:90]}")
