import csv,re,json,sys,os,collections
from PIL import Image
S=sys.argv[1]; voci=json.load(open(S+'/pagine.json'))
def righe(n):
    R=collections.OrderedDict()
    for r in csv.DictReader(open(f'{S}/nat/p{n:03d}.tsv'),delimiter='\t',quoting=csv.QUOTE_NONE):
        if r['level']!='5' or not r['text'].strip(): continue
        k=(r['block_num'],r['par_num'],r['line_num'])
        R.setdefault(k,[]).append((int(r['left']),int(r['top']),int(r['left'])+int(r['width']),int(r['top'])+int(r['height']),r['text'],float(r['conf'])))
    out=[]
    for k,w in R.items():
        out.append(dict(x0=min(a[0] for a in w),y0=min(a[1] for a in w),x1=max(a[2] for a in w),y1=max(a[3] for a in w),testo=' '.join(a[4] for a in w),parole=w))
    return out
def prosa(l):
    p=[a for a in l['parole'] if re.fullmatch(r"[A-Za-zÀ-ÿ’',.;:]{3,}",a[4]) and a[5]>50]
    return len(p)>=6 and (l['x1']-l['x0'])>900
res=[]
for v in voci:
    if not v.get('pagine_ocr') and 'C7' not in v['etichetta']: continue
    if v['pagine']: continue
    res.append(v)
json.dump([v['etichetta'] for v in res],sys.stdout); print()
PAG={'Fig. C7.10.3':239,'Fig. C7.2.2':199,'Fig. C7.2.5':207,'Fig. C7.10.2':237}
RXCAP={'Fig. C7.10.3':r'Figura\s*C\s*7\s*[.,]\s*10\s*[.,]\s*2\s*.{0,4}Rigidezza','Fig. C7.2.5':r'Figura\s*C\s*7\s*[.,]\s*2\s*[.,]?\s*5'}
os.makedirs(S+'/out/png',exist_ok=True); os.makedirs(S+'/out/scan',exist_ok=True)
esiti=[]
for v in res:
    lab=v['etichetta']; n=PAG.get(lab) or (v.get('pagine_ocr') or [None])[0]
    if lab.startswith('Tab'): esiti.append(dict(v,nota='tabella: a parte')); continue
    L=righe(n); num=lab.split('C7')[1]; let=num[-1] if num[-1] in 'ab' else ''; num=num.rstrip('ab').strip('.')
    rx=RXCAP.get(lab) or r'Figura\s*\.?\s*C\s*7\s*[.,]\s*'+r'\s*[.,]\s*'.join(num.split('.'))+(r'\s*'+let if let else r'(?![\d])')
    cap=None
    for l in L:
        m=re.match(r'\s*Figura',l['testo']) and re.search(rx,l['testo'])
        if m: cap=l; break
    if not cap: esiti.append(dict(v,pagina_scan=n,nota='didascalia non trovata')); continue
    # estensione orizzontale della singola didascalia, se due affiancate sulla stessa riga
    pr=[l for l in L if prosa(l)]
    gab=(max(0,min(l['x0'] for l in pr)-60),min(2219,max(l['x1'] for l in pr)+60)) if pr else (60,2160)
    xs=gab
    caps=[a for a in cap['parole'] if re.match(r'Figura',a[4])]
    if len(caps)>1:
        ord_=sorted(a[0] for a in caps); 
        idx=[i for i,a in enumerate(sorted(caps,key=lambda a:a[0])) if re.search(rx,' '.join(b[4] for b in cap['parole'] if b[0]>=a[0]-2))]
        i=idx[-1] if let=='b' or lab in ('Fig. C7.2.2',) else idx[0]
        meta=[(ord_[k]+ord_[k+1])//2 - 30 for k in range(len(ord_)-1)]
        xs=(gab[0] if i==0 else meta[i-1], gab[1] if i==len(ord_)-1 else meta[i])
    sx=min(l['x0'] for l in L)
    piene=[l for l in L if prosa(l) and (l['x1']-l['x0'])>1700]
    ids=set(id(l) for l in piene); Ls=sorted(L,key=lambda l:l['y0'])
    for i,l in enumerate(Ls):
        if id(l) in ids and i+1<len(Ls):
            nx=Ls[i+1]; h=l['y1']-l['y0']
            if abs(nx['x0']-sx)<40 and 0<=nx['y0']-l['y1']<1.2*h and (nx['y1']-nx['y0'])<1.6*h and not re.match(r'\s*Figura',nx['testo']): ids.add(id(nx))
    sopra=[l for l in L if id(l) in ids and l['y1']<=cap['y0']+5]
    vicine=[l['y0'] for l in L if re.match(r'\s*Figura',l['testo']) and abs(l['y0']-cap['y0'])<80]
    top=max([l['y1'] for l in sopra],default=0)+8; bot=min(vicine+[cap['y0']])-12
    if bot-top<60: esiti.append(dict(v,pagina_scan=n,nota=f'banda stretta top={top} bot={bot} cap={cap["testo"][:50]}')); continue
    im=Image.open(f'{S}/nat/p{n:03d}.jpeg').convert('L')
    band=im.crop((xs[0],top,xs[1],bot)).point(lambda p:255 if p<170 else 0)
    bb=band.getbbox()
    if not bb: esiti.append(dict(v,pagina_scan=n,nota='banda vuota')); continue
    box=(max(0,xs[0]+bb[0]-12),max(0,top+bb[1]-12),min(2219,xs[0]+bb[2]+12),min(3106,top+bb[3]+12))
    nome=os.path.basename(v['file'])
    im.crop(box).save(f'{S}/out/png/{nome}',optimize=True)
    esiti.append(dict(v,pagina_scan=n,riquadro_px=box,png=nome,metodo=f'scansione nativa 2219x3106, ritaglio px {box}',didascalia=cap['testo'][:90]))
json.dump(esiti,open(S+'/scansioni.json','w'),ensure_ascii=False,indent=1)
for e in esiti: print(e['etichetta'],e.get('pagina_scan'),e.get('riquadro_px'),e.get('nota',''))
