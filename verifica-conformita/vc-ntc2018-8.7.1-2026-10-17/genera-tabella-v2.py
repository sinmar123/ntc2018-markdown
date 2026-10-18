"""Rigenera lista-correzioni-c.md (v2) da lista-correzioni.json e dubbi-e-scartati.json; anomalie e scartati dalla v1."""
import json, re
L = json.load(open('lista-correzioni.json', encoding='utf-8'))
DS = json.load(open('dubbi-e-scartati.json', encoding='utf-8'))
v1 = open('v1/lista-correzioni-c.md', encoding='utf-8').read()
riga = {}
for b in 'ABC':
    for r in json.load(open(f'confronto-{b}.json', encoding='utf-8-sig'))['rilievi']: riga[r['id']] = r['riga_md']
riga.update({'G-01':403,'G-02':412,'G-03':223,'G-04':230,'G-05':223,'G-06':230,'G-07':347,'G-08':362,'G-09':362,
             'SC-01':113,'SC-02':187,'SC-03':187,'SC-04':187,'SC-05':210,'SC-06':210,'SC-07':210})
NUOVE = {'SC-01','SC-02','SC-03','SC-04','SC-05','SC-06','SC-07'}; MOD = {'C-16','C-32','B-68','B-69','B-70'}
def c(s): return s.replace('|', '\\|').replace('\n', '⏎')
def tag(i): return ' (v2, nuova)' if i in NUOVE else (' (v2, modificata)' if i in MOD else '')
rows = ['| ID | Riga | Pagina | Categoria | Effetto | Attuale | Proposto | Nota |', '|---|---|---|---|---|---|---|---|']
for r in sorted(L, key=lambda r: (r['effetto'] != 'sostanziale', r['categoria'], riga.get(r['id'], 0))):
    lim = 400 if r['id'] == 'C-16' else 160
    rows.append(f"| {r['id']}{tag(r['id'])} | {riga.get(r['id'],'')} | {r['pagina'].replace('Circolare fisica ','C ')} | {r['categoria']} | {r['effetto']} | `{c(r['attuale'])[:lim]}` | `{c(r['proposto'])[:lim]}` | {c(r['nota'])[:300]} |")
dub = ['| ID | Riga | Pagina | Questione |', '|---|---|---|---|'] + [f"| {r['id']}{' (v2, nuovo)' if r['id']=='D-01' else ''} | {r['riga_md']} | {r['pagina_fisica']} | {c(r['nota'])} Fonte: {c(r.get('fonte',''))} |" for r in DS['dubbi']]
n = len(L); ns = sum(r['effetto'] == 'sostanziale' for r in L); nf = n - ns
anom = v1[v1.index('## Anomalie della fonte'):v1.index('## Respinte o assorbite')]
resp = v1[v1.index('## Respinte o assorbite'):]
txt = f"""# § 8.7.1 e C8.7.1: elenco unico delle non conformità (v2)

Firma: GBOT-verifica-ntc, 2026-10-17. Confronto iniziale di Grok Build in tre blocchi, aggiudicazione e controllo a campione di GBOT. Proposte **non applicate**: decisione di Sandro.

**Revisione v2 (2026-10-17, approvata da Sandro).** Le voci nuove SC-01…SC-07, il dubbio D-01 e le modifiche a C-16, C-32, B-68, B-69 e B-70 derivano dal confronto automatico con il corpus structural-codes (github.com/claudiopagani/structural-codes, commit 5698a0e; motore: script locale, nessun LLM), e ciascuna è stata verificata sulla Gazzetta (Circolare 7/2019, PDF congelato, livello testo e ritagli). Nessun testo di structural-codes è riportato qui. La v1 è conservata come `lista-correzioni-c-v1.md`.

File: `cap08/8.7.1-progettazione-interventi-costruzioni-in-muratura.md`, base git `92a449e`. Pagine fisiche: Norma 297-298; Circolare 270-283 (stampate 266-279; la 281 è solo raster).

Totale voci applicabili: {n} ({ns} sostanziali, {nf} di forma). Dubbi: {len(DS['dubbi'])}. Voci respinte o assorbite: {len(DS['scartati'])}. La lista eseguibile è [lista-correzioni.json](lista-correzioni.json), già ordinata per `applica-lista` (ogni `attuale` è unico al momento in cui si applica); il diff completo che ne risulta è [diff-proposto.patch](diff-proposto.patch).

Scelta per B-68…B-70: la fonte stampa «1)», «2)», «3)». La v1 li rendeva come elenco numerato «1.», cambiando il marcatore. La v2 li rende come elenco ordinato Markdown con delimitatore «)» (`1) testo`, voci separate da riga vuota), cioè il testo stampato resta identico carattere per carattere. È la forma già usata nel corpus per gli elenchi «1)» (6.2.4, 7.2.3, 7.3.3, 7.10.4, 10). Non si usa `- 1) …`, perché in CommonMark «1)» in testa alla voce aprirebbe un elenco annidato; non si usa l’escape `1\\)`, che aggiungerebbe un carattere estraneo alla fonte e non ha precedenti nel corpus. Limite noto: alcuni visualizzatori (ad esempio GitHub) disegnano la numerazione dell’elenco ordinato come «1.», ma il sorgente conserva «1)».

## Voci (sostanziali in testa)

""" + '\n'.join(rows) + """

## Dubbi da decidere

""" + '\n'.join(dub) + "\n\n" + anom + resp
open('lista-correzioni-c.md', 'w', encoding='utf-8').write(txt)
print(n, ns, nf, len(DS['dubbi']))
