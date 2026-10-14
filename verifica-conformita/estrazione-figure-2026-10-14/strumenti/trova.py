import pymupdf,re,json,sys,glob,os
F='verifica-conformita/fonte-ufficiale/'
docs={'NTC':pymupdf.open(F+'GU-2018-42-SO8-DM-17-01-2018.pdf'),'Circolare':pymupdf.open(F+'GU-2019-35-SO5-Circolare-7-2019.pdf')}
r=json.load(open('_sito/rapporto-costruzione.json'))['figure_mancanti']
alt={}
for m in r:
    t=open(m['pagina'],encoding='utf-8-sig').read()
    a=re.search(r'!\[([^\]]*)\]\('+re.escape(m['figura'])+r'\)',t)
    alt.setdefault(m['file'],a.group(1) if a else '')
out=[]
for f,a in sorted(alt.items()):
    n=os.path.basename(f); nn=re.match(r'(fig|tab)-([cC]?)([\d.]*\d)([a-z]?)-',n)
    a2=a if re.match(r'\s*(Fig\w*\.?|Tab\w*\.?)\s*C?\.?\s*\d',a) else f"{'Fig.' if nn.group(1)=='fig' else 'Tab.'} {nn.group(2).upper()}{nn.group(3)}{nn.group(4)}"
    m=re.match(r'\s*(Fig\w*\.?|Tab\w*\.?)\s*(C?)\.?\s*([\d.]*\d(?:\.[IVX]+)?)\s*(?:[.(]?([a-z])\)?(?![a-z]))?',a2)
    tipo='Fig' if m.group(1).startswith('F') else 'Tab'; c=m.group(2); num=m.group(3); let=m.group(4) or ''
    atto='Circolare' if c else 'NTC'; doc=docs[atto]
    par=r'Fig\w*\.?|Figura' if tipo=='Fig' else r'Tab\w*\.?|Tabella'
    lab=(r'C\.?' if c else '')+re.escape(num)+(r'\s*[.(]?'+let+r'\)?' if let else '')
    rx=re.compile(r'^\s*(?:%s)\s*%s(?![\dIVX]|\.\d)\s*\.?\s*([–\-—]|[A-Z])'%(par,lab))
    pag=[]
    for i,p in enumerate(doc):
        if any(rx.search(b[4]) for b in p.get_text('blocks')): pag.append(i+1)
    out.append(dict(file=f,alt=a,etichetta=f'{tipo}. {c}{num}{let}',atto=atto,regex=rx.pattern,pagine=pag))
json.dump(out,open(sys.argv[1],'w'),ensure_ascii=False,indent=1)
for o in out:
    if len(o['pagine'])!=1 and not o['etichetta'].startswith(('Fig. C7','Tab. C7')): print(o['etichetta'],o['atto'],o['pagine'],o['alt'][:50])
print(len(out),'univoche',sum(len(o['pagine'])==1 for o in out))
