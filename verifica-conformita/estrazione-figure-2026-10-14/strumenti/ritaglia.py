"""Propone il riquadro di ogni figura: fra l'ultimo blocco di prosa sopra la didascalia e la didascalia.
Per le tabelle: dalla didascalia in giù fino alla prosa successiva."""
import pymupdf,re,json,sys
F='verifica-conformita/fonte-ufficiale/'
docs={'NTC':pymupdf.open(F+'GU-2018-42-SO8-DM-17-01-2018.pdf'),'Circolare':pymupdf.open(F+'GU-2019-35-SO5-Circolare-7-2019.pdf')}
voci=json.load(open(sys.argv[1]))
def prosa(b):
    t=b[4].strip()
    parole=[w for w in re.findall(r"[A-Za-zÀ-ÿ’']+",t) if len(w)>=3]
    return len(parole)>=6 or re.match(r'^(C?\d+\.\d+(\.\d+)+\s+[A-Z])',t)
def didascalia(p,v):
    rx=re.compile(v['regex'])
    for b in p.get_text('blocks'):
        if rx.search(b[4]): return b
for v in voci:
    if len(v['pagine'])!=1: continue
    p=docs[v['atto']][v['pagine'][0]-1]
    cap=didascalia(p,v)
    if not cap: v['riquadro']=None; continue
    blocchi=[b for b in p.get_text('blocks') if 80<b[1]<745 and b is not cap and b[4].strip()]
    oggetti=[tuple(d['rect']) for d in p.get_drawings() if 80<d['rect'][1]<745]+[tuple(i['bbox']) for i in p.get_image_info() if i['bbox'][1]<745]
    cy=lambda o:(o[1]+o[3])/2
    if v['etichetta'].startswith('Fig'):
        y0=max([b[3] for b in blocchi if prosa(b) and cy(b)<cap[1]],default=80); y1=cap[1]
    else:
        y0=cap[3]; y1=min([b[1] for b in blocchi if prosa(b) and cy(b)>cap[3] and not re.match(r'^\s*Tab',b[4])],default=745)
    if v['etichetta'].startswith('Fig'):
        tagli=[b[1] for b in blocchi if re.match(r'^\s*Fig',b[4]) and y0<cy(b)<y1]
        if tagli: y1=min(tagli)
    dentro=[o for o in oggetti if y0<=cy(o)<=y1]+[b[:4] for b in blocchi if not prosa(b) and y0<=cy(b)<=y1]
    # gruppi separati da più di SOGLIA punti in verticale: si tiene quello attaccato alla didascalia
    SOGLIA=v.get('soglia',14)
    if dentro:
        dentro.sort(key=lambda o:o[1]); gruppi=[[dentro[0]]]; fondo=dentro[0][3]
        for o in dentro[1:]:
            if o[1]-fondo>SOGLIA: gruppi.append([o])
            else: gruppi[-1].append(o)
            fondo=max(fondo,o[3])
        dentro=gruppi[-1] if v['etichetta'].startswith('Fig') else gruppi[0]
        if len(gruppi)>1: v['gruppi_scartati']=len(gruppi)-1
    v['disegni']=sum(1 for o in oggetti if y0<=cy(o)<=y1)
    if not dentro: v['riquadro']=[83,y0,513,y1]; v['vuoto']=True; continue
    x0=min(o[0] for o in dentro);x1=max(o[2] for o in dentro);a=min(o[1] for o in dentro);b=max(o[3] for o in dentro)
    a=max(a,y0); b=min(b,y1-1)
    v['riquadro']=[round(x0-3,1),round(a-3,1),round(x1+3,1),round(min(b+3,y1-0.5),1)]
    v['raster']=[(tuple(round(c) for c in i['bbox']),i['width'],i['height'],i['xref']) for i in p.get_image_info(xrefs=True) if y0<=(i['bbox'][1]+i['bbox'][3])/2<=y1]
    v['testi']=sum(1 for b in blocchi if not prosa(b) and y0<=cy(b)<=y1)
json.dump(voci,open(sys.argv[2],'w'),ensure_ascii=False,indent=1)
print(sum(1 for v in voci if v.get('riquadro')),'riquadri;',[v['etichetta'] for v in voci if len(v['pagine'])==1 and not v.get('riquadro')])
