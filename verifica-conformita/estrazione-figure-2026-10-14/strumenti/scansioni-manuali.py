import json,sys
from PIL import Image
S=sys.argv[1]
BANDE={'Fig. C7.3.2a':(210,(300,1924,1085,2651)),'Fig. C7.3.2b':(210,(1085,1924,2219,2651)),'Fig. C7.6.3':(226,(37,723,2219,1580))}
E_=json.load(open(S+'/scansioni.json'))
for e in E_:
    if e['etichetta'] not in BANDE: continue
    n,b=BANDE[e['etichetta']]
    im=Image.open(f'{S}/nat/p{n:03d}.jpeg').convert('L')
    bb=im.crop(b).point(lambda p:255 if p<170 else 0).getbbox()
    box=(max(0,b[0]+bb[0]-12),max(0,b[1]+bb[1]-12),min(2219,b[0]+bb[2]+12),min(3106,b[1]+bb[3]+12))
    im.crop(box).save(f"{S}/out/png/{e['png']}",optimize=True)
    e['riquadro_px']=box; e['metodo']=f'scansione nativa 2219x3106, ritaglio px {box} (banda fissata a mano {b})'
    print(e['etichetta'],box)
json.dump(E_,open(S+'/scansioni.json','w'),ensure_ascii=False,indent=1)
