"""GBOT-verifica-ntc: elenco unico 8.7.1 da confronti A, B, C di Grok Build + aggiudicazione C (2026-10-17)."""
import json, sys
FILE = 'cap08/8.7.1-progettazione-interventi-costruzioni-in-muratura.md'
md = open(sys.argv[1], encoding='utf-8').read()
rows = []
for b in 'ABC':
    d = json.load(open(f'confronto-{b}.json', encoding='utf-8-sig'))
    rows += d['rilievi']
def fix(s): return s.replace('\\n\\n', '\n\n')
respinti = {
 'C-24': 'Respinto: il richiamo di nota [4] è la convenzione del corpus, usata nei file VC-OK 8.5.4 e 8.4 (voce 11 del catalogo, marcatori di nota).',
 'C-25': 'Respinto: la resa **Nota 4.** è la convenzione del corpus, usata nei file VC-OK 8.5.4 e 8.4; il testo della nota coincide.',
}
dubbi_c = {
 'C-18': 'Riclassificato DUBBIO da GBOT: la fonte stampa in grassetto l’intera espressione «fbt = 0,1fb»; la voce 20 toglie il grassetto ai simboli, resta da decidere se togliere anche quello del numero (lettura A: $f_{bt}=0{,}1f_b$ invariato; lettura B: solo 0,1 in grassetto).',
}
patch = {
 # apostrofo curvo da conservare, come nel file
 'B-03': {'proposto': 'legando l’accelerazione $a$ allo spostamento $d$ mediante il periodo $T_0$'},
 # B-11/B-12 assorbono B-64/B-66 (stessa riga)
 'B-11': {'attuale': 'il 40% dello spostamento d0 per cui si annulla l’accelerazione spettrale valutata su una curva di capacità in cui si\nconsiderino',
          'proposto': 'il 40% dello spostamento $d_0$ per cui si annulla l’accelerazione spettrale $a$ valutata su una curva di capacità in cui si considerino'},
 'B-12': {'attuale': 'il 60% dello spostamento d0 per cui si annulla l’accelerazione spettrale valutata su una curva di capacità in cui si\nconsiderino',
          'proposto': 'il 60% dello spostamento $d_0$ per cui si annulla l’accelerazione spettrale $a$ valutata su una curva di capacità in cui si considerino'},
 # B-75 assorbe B-76
 'B-75': {'attuale': 'livello di conoscenza LC1);', 'proposto': 'livello di conoscenza **LC1**;',
          'nota': 'LC1 in grassetto e, come nella fonte, nessuna parentesi chiusa prima del punto e virgola (assorbe B-76).'},
 'A-33': {'attuale': '). In particolare, la verifica', 'proposto': ').\n\nIn particolare, la verifica'},
 'C-50': {'proposto': 'quanto segue:\n\n- a. i solai', 'nota': 'Lettera a. conservata nel testo della voce, come in A-10 (voce 21: cambia solo la resa del marcatore).'},
 'C-51': {'proposto': 'loro piano;\n\n- b. tutte'},
 'C-52': {'proposto': 'flessionale;\n\n- c. tutti'},
 'C-53': {'proposto': 'lignea);\n\n- d. tutti'},
 'C-54': {'proposto': 'ecc.);\n\n- e. le pareti'},
 'C-55': {'proposto': 'collegate;\n\n- f. le murature'},
 'C-57': {'attuale': 'comignoli,\n\ncornicioni ecc.);', 'proposto': 'comignoli, cornicioni ecc.);'},
 'C-15': {'nota': 'Grassetto confermato. La nota di Grok Build secondo cui «Nel caso di muratura regolare» a p. 281 sarebbe in tondo è errata: è in grassetto, vedi G-01.'},
}
assorbiti = {'B-64': 'B-11', 'B-66': 'B-12', 'B-76': 'B-75'}
nuovi = [
 dict(id='G-01', riga_md=403, pagina_fisica='circ 281 (raster)', attuale='Nel caso di muratura regolare, la', proposto='**Nel caso di muratura regolare**, la',
      fonte='«Nel caso di muratura regolare» in grassetto', classe='ERR-MD', categoria='enfasi', effetto='forma', nota='Aggiunto da GBOT sul raster nativo 2221×3106.'),
 dict(id='G-02', riga_md=412, pagina_fisica='circ 281 (raster)', attuale='e $\\mu$ coefficiente d’attrito)', proposto='e $\\mu$, coefficiente d’attrito)',
      fonte='«f_v0,e μ, coefficiente d’attrito)», virgola dopo μ', classe='ERR-MD', categoria='prosa', effetto='forma', nota='Aggiunto da GBOT; virgola omessa.'),
 dict(id='G-03', riga_md=223, pagina_fisica='circ 275', attuale='{e^*FC}\n\\tag{C8.7.1.8}', proposto='{e\\ast FC}\n\\tag{C8.7.1.8}',
      fonte='[C8.7.1.8] stampa e∗FC con asterisco centrato sulla linea, non in apice come in [C8.7.1.3]', classe='ERR-MD', categoria='formula', effetto='forma', nota='Aggiunto da GBOT, ritaglio 1200 dpi. Anomalia della fonte da conservare.'),
 dict(id='G-04', riga_md=230, pagina_fisica='circ 275', attuale='{e^*FC}\n\\tag{C8.7.1.9}', proposto='{e\\ast FC}\n\\tag{C8.7.1.9}',
      fonte='[C8.7.1.9] stampa e∗FC con asterisco centrato', classe='ERR-MD', categoria='formula', effetto='forma', nota='Aggiunto da GBOT, ritaglio 1200 dpi.'),
 dict(id='G-05', riga_md=223, pagina_fisica='circ 275', attuale='a_{Z,SLD} = \\frac{\\alpha_0g}', proposto='\\mathrm{a}_{Z,SLD} = \\frac{\\alpha_0g}',
      fonte='[C8.7.1.8]: la a è in tondo', classe='ERR-MD', categoria='formula', effetto='forma', nota='Aggiunto da GBOT; si applica dopo B-06. Anche S di [C8.7.1.9] è in tondo (G-06).'),
 dict(id='G-06', riga_md=230, pagina_fisica='circ 275', attuale='S_{eZ,SLD}(T_0) =', proposto='\\mathrm{S}_{eZ,SLD}(T_0) =',
      fonte='[C8.7.1.9]: la S è in tondo', classe='ERR-MD', categoria='formula', effetto='forma', nota='Aggiunto da GBOT; si applica dopo B-08.'),
 dict(id='G-07', riga_md=347, pagina_fisica='circ 279', attuale='f_{v,lim} = \\frac{0.065f_b}{0.7}', proposto='f_{V,lim} = \\frac{0.065f_b}{0.7}',
      fonte='[C8.7.1.14] stampa f_{V,lim} con V maiuscola; la prosa stampa f_{v,lim}', classe='ERR-MD', categoria='formula', effetto='sostanziale', nota='Aggiunto da GBOT, ritaglio 1200 dpi; si applica dopo C-01. Anomalia della fonte da conservare.'),
 dict(id='G-08', riga_md=362, pagina_fisica='circ 280', attuale='\\frac{\\mu\\sigma_y}{\\phi}\\right)', proposto='\\frac{\\mu\\sigma_y}{\\Phi}\\right)',
      fonte='[C8.7.1.15] stampa Φ maiuscolo al denominatore', classe='ERR-MD', categoria='formula', effetto='sostanziale', nota='Aggiunto da GBOT, ritaglio 1200 dpi. Come A-01, la prosa usa φ minuscolo: anomalia della fonte da conservare.'),
 dict(id='G-09', riga_md=362, pagina_fisica='circ 280', attuale='f_{ftd} = \\min\\left(', proposto='f_{ftd} = min\\left(',
      fonte='[C8.7.1.15] stampa min in corsivo', classe='ERR-MD', categoria='formula', effetto='forma', nota='Aggiunto da GBOT; min corsivo come stampato.'),
]
lista, scartati = [], []
for r in rows:
    r = dict(r); rid = r['id']
    if rid in assorbiti: scartati.append({'id': rid, 'motivo': f'assorbito in {assorbiti[rid]}'}); continue
    if rid in respinti: scartati.append({'id': rid, 'motivo': respinti[rid]}); continue
    r.update(patch.get(rid, {}))
    if rid in dubbi_c: r['classe'] = 'DUBBIO'; r['nota'] = dubbi_c[rid]
    r['attuale'] = fix(r['attuale']); r['proposto'] = fix(r['proposto'])
    lista.append(r)
lista += nuovi
# ordine di applicazione: tentativi ripetuti finché ogni attuale è unico al momento
todo = [r for r in lista if r['classe'] == 'ERR-MD']
text, ordine, guard = md, [], 0
while todo and guard < 10:
    guard += 1; resto = []
    for r in todo:
        if text.count(r['attuale']) == 1:
            text = text.replace(r['attuale'], r['proposto']); ordine.append(r['id'])
        else: resto.append(r)
    todo = resto
print('non applicabili:', [(r['id'], text.count(r['attuale'])) for r in todo])
pos = {k: i for i, k in enumerate(ordine)}
out = []
for r in sorted([r for r in lista if r['classe'] == 'ERR-MD'], key=lambda r: pos.get(r['id'], 999)):
    out.append({'id': r['id'], 'file': FILE, 'attuale': r['attuale'], 'proposto': r['proposto'],
                'pagina': 'Circolare fisica ' + str(r['pagina_fisica']).replace('circ ', '') if str(r['pagina_fisica']).startswith('circ') else str(r['pagina_fisica']),
                'classe': r['classe'], 'effetto': r['effetto'], 'categoria': r['categoria'],
                'decisione': 'da decidere (Sandro)', 'nota': r.get('nota', '') + (' Fonte: ' + r['fonte'] if r.get('fonte') else '')})
json.dump(out, open('lista-correzioni.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
json.dump({'dubbi': [r for r in lista if r['classe'] == 'DUBBIO'], 'scartati': scartati}, open('dubbi-e-scartati.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
open('target-dopo-lista.md', 'w', encoding='utf-8').write(text)
from collections import Counter
print(len(out), Counter((r['effetto'], r['categoria']) for r in out))
print('dubbi', [r['id'] for r in lista if r['classe'] == 'DUBBIO'], 'scartati', scartati)
