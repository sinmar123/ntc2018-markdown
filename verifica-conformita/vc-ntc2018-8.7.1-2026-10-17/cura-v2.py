"""GBOT-verifica-ntc (v2 2026-10-17, con le voci SC-xx e il dubbio D-01 dal confronto con structural-codes): elenco unico 8.7.1 da confronti A, B, C di Grok Build + aggiudicazione C (2026-10-17)."""
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

 # v2 (2026-10-17): lacune emerse dal confronto con structural-codes, verificate sulla Gazzetta
 'C-16': {'attuale': None, 'proposto': None,
          'nota': 'v2: elenco completo del «dove:» di [C8.7.1.16] come nella fonte (p. fisica 280): cinque voci l, t, σ0, f_td e τ0d, b; nessun «;» dopo l, t e σ0 (la fonte non li stampa); «.» dopo «altezza del pannello» come nella fonte. Sostituisce la v1, che separava solo l e t.'},
 'C-32': {'proposto': "**US** di testata.\n\nL'analisi di una **US**",
          'nota': 'v2: in grassetto anche la prima US di «nelle US di testata» (p. fisica 282, carattere Bold nel livello testo).'},
 'B-68': {'proposto': 'diversi contributi:\n\n1) un opportuno', 'nota': 'v2: marcatore stampato «1)» conservato (elenco ordinato con delimitatore «)», come nei file del corpus 6.2.4, 7.2.3, 7.3.3, 7.10.4, 10).'},
 'B-69': {'proposto': 'elementi;\n\n2) una dissipazione', 'nota': 'v2: marcatore stampato «2)» conservato.'},
 'B-70': {'proposto': 'modellato);\n\n3) una dissipazione', 'nota': 'v2: marcatore stampato «3)» conservato.'},
 'C-15': {'nota': 'Grassetto confermato. La nota di Grok Build secondo cui «Nel caso di muratura regolare» a p. 281 sarebbe in tondo è errata: è in grassetto, vedi G-01.'},
}
a0 = md.index('dove: $l$ è la lunghezza del pannello;'); a1 = md.index('$b$ è un coefficiente', a0) + len('$b$ è un coefficiente')
_c16 = md[a0:a1]
_c16p = (_c16.replace('dove: $l$ è la lunghezza del pannello; $t$ è lo spessore del pannello; $\\sigma_0$', 'dove:\n\n- $l$ è la lunghezza del pannello\n\n- $t$ è lo spessore del pannello\n\n- $\\sigma_0$')
             .replace('positiva se di compressione); $f_{td}$', 'positiva se di compressione)\n\n- $f_{td}$')
             .replace('altezza del pannello; $b$ è un coefficiente', 'altezza del pannello.\n\n- $b$ è un coefficiente'))
assert _c16p.count('\n\n- ') == 5, _c16p
patch['C-16']['attuale'] = _c16; patch['C-16']['proposto'] = _c16p
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
 # v2: voci da confronto con structural-codes (script locale, nessun LLM), verificate sulla Gazzetta
 dict(id='SC-01', riga_md=113, pagina_fisica='circ 272', attuale='disgregazione. Le ipotesi tradizionalmente', proposto='disgregazione.\n\nLe ipotesi tradizionalmente',
      fonte='«disgregazione.» chiude una riga corta (x 74-128, y 131); «Le ipotesi tradizionalmente…» apre un nuovo capoverso (y 144, interlinea 13 pt contro 10-11)', classe='ERR-MD', categoria='capoverso', effetto='forma', nota='v2, da structural-codes.'),
 dict(id='SC-02', riga_md=187, pagina_fisica='circ 274', attuale='dove: $g$ è l’accelerazione di gravità; $FC$ è il Fattore di Confidenza', proposto='dove:\n\n- $g$ è l’accelerazione di gravità;\n\n- $FC$ è il Fattore di Confidenza',
      fonte='«dove:» di [C8.7.1.4] composto a righe rientrate: simbolo a x 86, descrizione a x 111 (g, FC, δCx, e*)', classe='ERR-MD', categoria='elenco', effetto='forma', nota='v2, da structural-codes; voce 18 del catalogo, come A-11 e A-12.'),
 dict(id='SC-03', riga_md=187, pagina_fisica='circ 274', attuale='**LC1**; $\\delta_{Cx}$ è lo spostamento virtuale', proposto='**LC1**;\n\n- $\\delta_{Cx}$ è lo spostamento virtuale',
      fonte='voce δCx del «dove:» di [C8.7.1.4] (y 477)', classe='ERR-MD', categoria='elenco', effetto='forma', nota='v2, da structural-codes; si applica dopo B-75.'),
 dict(id='SC-04', riga_md=187, pagina_fisica='circ 274', attuale='configurazione indeformata iniziale; $e^*$ è la frazione', proposto='configurazione indeformata iniziale;\n\n- $e^*$ è la frazione',
      fonte='voce e* del «dove:» di [C8.7.1.4] (y 502)', classe='ERR-MD', categoria='elenco', effetto='forma', nota='v2, da structural-codes.'),
 dict(id='SC-05', riga_md=210, pagina_fisica='circ 275', attuale='dove: $g$ è l’accelerazione di gravità; $\\kappa$ è un coefficiente', proposto='dove:\n\n- $g$ è l’accelerazione di gravità;\n\n- $\\kappa$ è un coefficiente',
      fonte='«dove:» di [C8.7.1.7] composto a righe rientrate: simbolo a x 86, descrizione a x 111 (g, κ, L, λ, W, E)', classe='ERR-MD', categoria='elenco', effetto='forma', nota='v2, da structural-codes; voce 18 del catalogo, come A-11 e A-12.'),
 dict(id='SC-06', riga_md=210, pagina_fisica='circ 275', attuale='(trave appoggiata); $L$ è la lunghezza dell’elemento; $\\lambda$ è la snellezza', proposto='(trave appoggiata);\n\n- $L$ è la lunghezza dell’elemento;\n\n- $\\lambda$ è la snellezza',
      fonte='voci L e λ del «dove:» di [C8.7.1.7] (y 150, 162)', classe='ERR-MD', categoria='elenco', effetto='forma', nota='v2, da structural-codes.'),
 dict(id='SC-07', riga_md=210, pagina_fisica='circ 275', attuale='e lo spessore $t$); $W$ è il peso specifico della muratura; $E$ è il modulo', proposto='e lo spessore $t$);\n\n- $W$ è il peso specifico della muratura;\n\n- $E$ è il modulo',
      fonte='voci W ed E del «dove:» di [C8.7.1.7] (y 176, 189); la voce E termina con «condizioni fessurate.», poi B-30 apre il capoverso «Questo tratto lineare…»', classe='ERR-MD', categoria='elenco', effetto='forma', nota='v2, da structural-codes.'),
 dict(id='D-01', riga_md=368, pagina_fisica='circ 280', attuale='ed elastofragile a trazione', proposto='ed elastofragile a trazione',
      fonte='«elasto-» a fine riga (y 230), «fragile» a inizio della riga seguente; unica occorrenza della parola nella Circolare', classe='DUBBIO', categoria='prosa', effetto='forma',
      nota='v2, da structural-codes (loro «elasto-fragile»). Lettura A: trattino di sillabazione, «elastofragile» come nel file. Lettura B: composto con trattino, «elasto-fragile». La pagina non lo decide. Proposta: lasciare com’è salvo decisione di Sandro.'),
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
