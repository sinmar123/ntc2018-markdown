import pymupdf,json,sys,os,io
from PIL import Image, ImageChops
F='verifica-conformita/fonte-ufficiale/'
docs={'NTC':pymupdf.open(F+'GU-2018-42-SO8-DM-17-01-2018.pdf'),'Circolare':pymupdf.open(F+'GU-2019-35-SO5-Circolare-7-2019.pdf')}
voci=json.load(open(sys.argv[1])); MAN=json.load(open('/tmp/claude-0/-home-user-ntc2018-markdown/c560b245-980e-5a6b-a155-56bea6ec132c/scratchpad/fig/manuali.json')); out=sys.argv[2]; os.makedirs(out+'/png',exist_ok=True); os.makedirs(out+'/controllo',exist_ok=True)
def salva(img,path):
    if img.mode!='L':
        rgb=img.convert('RGB'); r,g,b=rgb.split()
        if ImageChops.difference(r,g).getbbox() is None and ImageChops.difference(g,b).getbbox() is None: img=rgb.convert('L')
        else: img=rgb
    img.save(path,optimize=True)
for v in voci:
    if not v.get('riquadro'): continue
    doc=docs[v['atto']]; p=doc[v['pagine'][0]-1]; R=pymupdf.Rect(v['riquadro'])
    nome=os.path.basename(v['file']); dest=out+'/png/'+nome
    if nome in MAN:
        m=MAN[nome]; pezzi=[]; metodi=[]
        for pt in m['parti']:
            pp=doc[pt['pagina']-1]
            if 'xref' in pt:
                x=doc.extract_image(pt['xref']); im=Image.open(io.BytesIO(x['image']))
                if 'taglio_x' in pt:
                    g=im.convert('L'); w,h=g.size; px=g.load()
                    col=[sum(px[i,j] for j in range(h)) for i in range(w)]
                    zona=range(int(w*0.4),int(w*0.7)); bianca=[i for i in zona if col[i]>=max(col[k] for k in zona)-h]
                    cx=(min(bianca)+max(bianca))//2
                    if len(pt['taglio_x'])>2: cx=pt['taglio_x'][2]
                    im=im.crop((0,0,cx,h)) if pt['taglio_x'][1] is None else im.crop((cx,0,w,h))
                    metodi.append(f"raster nativo {x['width']}x{x['height']} tagliato in x={cx}")
                else: metodi.append(f"raster nativo {im.width}x{im.height}")
            else:
                pix=pp.get_pixmap(dpi=300,clip=pymupdf.Rect(pt['riquadro'])); im=Image.open(io.BytesIO(pix.tobytes('png'))); metodi.append(f"p.{pt['pagina']} {pt['riquadro']} reso a 300 dpi")
            pezzi.append(im.convert('RGB') if len(m['parti'])>1 else im)
        if len(pezzi)>1:
            if m['unisci']=='verticale':
                W=max(p.width for p in pezzi); img=Image.new('RGB',(W,sum(p.height for p in pezzi)),'white'); y=0
                for p_ in pezzi: img.paste(p_,((W-p_.width)//2,y)); y+=p_.height
            else:
                H=max(p.height for p in pezzi); img=Image.new('RGB',(sum(p.width for p in pezzi),H),'white'); x_=0
                for p_ in pezzi: img.paste(p_,(x_,0)); x_+=p_.width
        else: img=pezzi[0]
        v['metodo']='manuale: '+'; '.join(metodi); v['riquadro']=m['parti'][0].get('riquadro',v['riquadro'])
        salva(img,dest); v['png']=nome; v['dimensioni']=list(img.size)
        pg=p.get_pixmap(dpi=60); imc=Image.open(io.BytesIO(pg.tobytes('png'))).convert('RGB'); imc.save(out+'/controllo/'+nome)
        continue
    ras=v.get('raster') or []
    soloraster = len(ras)==1 and v.get('disegni',0)<=1 and v.get('testi',0)==0 and abs(pymupdf.Rect(ras[0][0]).width-R.width)<12 and abs(pymupdf.Rect(ras[0][0]).height-R.height)<12
    if soloraster:
        x=doc.extract_image(ras[0][3]); img=Image.open(io.BytesIO(x['image'])); v['metodo']=f"raster nativo {img.width}x{img.height}"
    else:
        pix=p.get_pixmap(dpi=300,clip=R); img=Image.open(io.BytesIO(pix.tobytes('png'))); v['metodo']='vettoriale reso a 300 dpi'
    salva(img,dest); v['png']=nome; v['dimensioni']=list(img.size)
    pg=p.get_pixmap(dpi=60); im=Image.open(io.BytesIO(pg.tobytes('png'))).convert('RGB')
    from PIL import ImageDraw
    d=ImageDraw.Draw(im); k=60/72; d.rectangle([R.x0*k,R.y0*k,R.x1*k,R.y1*k],outline=(255,0,0),width=2)
    im.save(out+'/controllo/'+nome)
json.dump(voci,open(sys.argv[1],'w'),ensure_ascii=False,indent=1)
