import json,sys,os
from PIL import Image,ImageDraw
S=sys.argv[1]; v=[x for x in json.load(open(sys.argv[2])) if x.get('png')]
per=4; os.makedirs(S+'/fogli',exist_ok=True)
for k in range(0,len(v),per):
    gruppo=v[k:k+per]; W=1000; H=420*len(gruppo)
    foglio=Image.new('RGB',(W,H),'white'); d=ImageDraw.Draw(foglio)
    for j,x in enumerate(gruppo):
        pg=Image.open(S+'/out/controllo/'+x['png']); pg.thumbnail((300,400)); foglio.paste(pg,(0,j*420+15))
        cr=Image.open(S+'/out/png/'+x['png']).convert('RGB'); cr.thumbnail((680,390)); foglio.paste(cr,(310,j*420+20))
        d.text((5,j*420+2),f"{k+j}: {x['etichetta']} p.{x['pagine'][0]} {x['metodo']} {x['png'][:60]}",fill=(200,0,0))
        d.line([(0,j*420+418),(W,j*420+418)],fill=(0,0,255))
    foglio.save(S+f'/fogli/f{k//per:02d}.png')
print(len(v))
