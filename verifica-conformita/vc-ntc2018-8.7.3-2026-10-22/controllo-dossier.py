"""Controllo automatico del dossier VC 8.7.3 prima del G7 (GBOT-verifica-ntc, 2026-10-22).

Uso, dalla radice del repository:
  python -X utf8 <dossier>/controllo-dossier.py --modo pre   # sull'insieme che andra' nel manifest (lista-manifest.json, impronte vive)
  python -X utf8 <dossier>/controllo-dossier.py --modo post  # sul manifest-rilascio.json generato

Controlli, su tutti i file del dossier e sui file di scope (target, verbale, scheda):
 (a) ogni impronta sha256 e ogni file citato da un'evidenza del manifest e' risolto: nel manifest con l'impronta
     corretta; oppure versione precedente di un file del manifest conservata nella storia git del ramo; oppure
     originale di una copia ripulita dichiarata in un indice log-*/indice.json del manifest; oppure valore derivato
     dichiarato in quell'indice; oppure in una delle categorie escluse per costruzione elencate qui sotto.
     Il log del G7 in corso non esiste ancora quando il manifest e' generato: e' escluso per costruzione.
 (b) nessun percorso assoluto (unita' disco, UNC, cartelle Unix di utente o di sistema, variabili d'ambiente),
     nessun nome utente o dato personale noto, nessun blocco riconoscibile di file del workspace esterni al progetto
     (impronte di finestre di 8 parole in impronte-blocchi-esterni.json).
 (c) gli URL degli atti sono nel verbale e nel ricontrollo G1.
Il risultato non riporta il testo trovato, solo file, riga e tipo, per non ricopiare cio' che si cerca.
"""
import json, os, re, sys, hashlib, subprocess, argparse
R = 'verifica-conformita/vc-ntc2018-8.7.3-2026-10-22'
T = 'cap08/8.7.3-progettazione-interventi-costruzioni-miste.md'
V = 'verifica-conformita/verbale-VC-ntc2018-8.7.3-2026-10-22.md'
SC = 'verifica-conformita/scheda-scope-ntc2018-8.7.3.md'
BASE = '33f9a3d'
ESCLUSI = {  # esclusi dal manifest per costruzione (procedura § 9 e ciclo di chiusura)
    'G7.json': 'giudizio del G7 in corso, fuori dal manifest che giudica',
    'G7-redazione.json': 'redazione del giudizio del G7 in corso',
    'chiusura.json': 'piano di registrazione: legato al manifest per impronta, compilato dopo il G7',
    'chiusura.eseguito.json': 'esito della registrazione, successivo al G7',
    'manifest-rilascio.json': 'il manifest stesso',
    'lista-manifest.json': 'elenco di lavoro da cui il manifest e\' generato',
    'corpo-pr.md': 'testo della richiesta di unione, successivo al G7',
    'controllo-dossier-esito-post-manifest.json': 'esito di questo controllo sul manifest gia\' generato',
    'indice-post-g7.json': 'indice della copia del log del G7 in corso, aggiunta dopo il giudizio',
}
FUORI_MANIFEST = {SC: 'scheda dello scope: e\' aggiornata dalla registrazione dopo il G7, quindi resta fuori dal manifest'}
GOVERNO = {'README.md', 'registro-verifica-conformita-ntc2018.csv', 'TODO.md', 'CHANGELOG.md', 'indice-ntc2018.md', 'cap08-costruzioni-esistenti-revisione.md',
           'registro-verifica.csv', 'PROCEDURA-VC.md', 'CATALOGO-NORMALIZZAZIONI.md', 'vc-supporto.py',
           'lint-registro-verifica.py', 'genera-indici-interni.py', 'prepara-scope-g6.py', 'vc-struttura-fonte.py', 'nuova-voce.py'}
# nomi con cui i file del dossier sono consegnati nelle cartelle di lavoro del G7 (copia piatta)
ALIAS = {'verbale.md': V, 'scheda.md': SC, 'ricontrollo-g1-20261022.json': R + '/g1/ricontrollo-20261022.json',
         'rapporto-g6-b01.json': R + '/g6/b01/rapporto-g6.json', 'inventario-g6-b01.json': R + '/g6/b01/inventario.json',
         'prova-NTC-873-CONDIZIONE.json': R + '/prove-c/prova-NTC-873-CONDIZIONE.json',
         'ntc298-per-queste-600dpi.png': R + '/prove-c/ntc298-per-queste-600dpi.png'}
CARTELLA_G7 = {'CONSEGNA-G7.md': 'consegna al verificatore nella cartella di lavoro del G7, fuori dal repository',
               'riepilogo-meccanico.json': 'riepilogo prodotto dagli script nella cartella di lavoro del G7, fuori dal repository',
               'ISTRUZIONI-CDX.md': None}
URL_ATTI = ['https://www.gazzettaufficiale.it/eli/id/2018/02/20/18A00716/sg',
            'https://www.gazzettaufficiale.it/eli/id/2019/02/11/19A00855/sg',
            'https://www.gazzettaufficiale.it/eli/id/2023/03/22/23A01847/sg']
# (b) schemi costruiti in modo da non riconoscere se stessi in questo file
UNITA = re.compile(r'(?<![A-Za-z0-9])[A-Za-z]' + ':' + r'[\\/]')
UNC = re.compile(r'(?:^|(?<=[\s\'"(=,]))' + r'\\\\' + r'[A-Za-z0-9][A-Za-z0-9._$-]+\\[A-Za-z0-9$]')
UNIX = re.compile(r'(?<![\w.:/<>-])/(?:ho' + r'me|Us' + r'ers|ro' + r'ot|tm' + r'p|va' + r'r|mn' + r't|op' + r't|et' + r'c|privat' + r'e)/')
AMB = re.compile(r'(?i)%(?:te' + r'mp|tm' + r'p|userprofile|appdata|localappdata|homepath|username)%|\$env:(?:te' + r'mp|tm' + r'p|userprofile|appdata|localappdata|username)')
UTENTE = re.compile(r'(?<![A-Za-z])sa' + r'ndro(?![A-Za-z])')
PERSONA = re.compile(r'(?i)sanvi' + r'tale|ales' + r'san' + r'dro')
HEX = re.compile(r'(?<![0-9A-Fa-f])[0-9a-fA-F]{64}(?![0-9A-Fa-f])')
CORTO = re.compile(r'(?<![0-9A-Fa-f])([0-9a-f]{6,16})(?:…|\.\.\.)([0-9a-f]{4,8})(?![0-9A-Fa-f])')
SEGNAPOSTO_EST = re.compile(r'<(?:codex-home|workspace|home|npm|sistema|powershell|unita)>[^\s\'"`]*')
SEGNAPOSTO_TEMP = re.compile(r'<temp>(?:[\\/]+[^\\/\s\'"`]+)*?[\\/]+(?=[^\\/\s\'"`]+\.\w+)')
PERCORSO = re.compile(r'(?<![\w.<>/-])((?:[\w.-]+/)*[\w][\w.-]*\.(?:json|md|pdf|png|html|txt|patch|py|tex|csv))(?![\w])')

def sha(b): return hashlib.sha256(b).hexdigest()
def leggi(p):
    b = open(p, 'rb').read()
    if b'\x00' in b: return b, None
    try: return b, b.decode('utf-8')
    except UnicodeDecodeError: return b, None

def storia_git(paths):
    """impronte sha256 di tutte le versioni dei file dati nei commit da BASE a HEAD"""
    com = sorted(set(subprocess.run(['git', 'rev-list', BASE + '..HEAD'], capture_output=True, text=True).stdout.split() + [BASE]))
    blobs = {}
    for c in com:
        out = subprocess.run(['git', 'ls-tree', '-r', c, '--'] + sorted(paths), capture_output=True, text=True, encoding='utf-8').stdout
        for riga in out.splitlines():
            meta, p = riga.split('\t', 1)
            blobs.setdefault(meta.split()[2], set()).add(p)
    ris = {}
    if blobs:
        ids = list(blobs)
        r = subprocess.run(['git', 'cat-file', '--batch'], input=('\n'.join(ids) + '\n').encode(), capture_output=True).stdout
        i = 0
        for bid in ids:
            nl = r.index(b'\n', i); n = int(r[i:nl].split()[2]); dati = r[nl + 1:nl + 1 + n]; i = nl + 1 + n + 1
            for p in blobs[bid]: ris.setdefault(sha(dati), set()).add(p)
    return ris

def intermedio():
    """stato del target dopo la lista e prima degli indici interni: il target vivo con le righe dell'indice interno
    riportate a quelle della base, come risultano dalle coppie -/+ di voci d'indice in diff-proposto.patch"""
    t = open(T, 'rb').read().decode('utf-8'); righe = open(R + '/diff-proposto.patch', encoding='utf-8').read().split('\n')
    for i in range(len(righe) - 1):
        a, b = righe[i], righe[i + 1]
        if a.startswith('-  - [') and b.startswith('+  - ['):
            t = t.replace(b[1:], a[1:])
    return sha(t.encode('utf-8'))

def main():
    ap = argparse.ArgumentParser(); ap.add_argument('--modo', choices=['pre', 'post'], required=True); a = ap.parse_args()
    problemi = []; note = {}
    nome_esito = 'controllo-dossier-esito-' + a.modo + '-manifest.json'
    def prob(tipo, file, riga=None, dett=None): problemi.append({k: v for k, v in (('tipo', tipo), ('file', file), ('riga', riga), ('dettaglio', dett)) if v is not None})
    # insieme del manifest
    if a.modo == 'pre':
        lista = json.load(open(R + '/lista-manifest.json', encoding='utf-8'))
        man = {p: (sha(open(p, 'rb').read()) if os.path.exists(p) else None) for p in lista}
        for p, h in man.items():
            if h is None and os.path.basename(p) != 'controllo-dossier-esito-pre-manifest.json': prob('lista: file mancante', p)
    else:
        m = json.load(open(R + '/manifest-rilascio.json', encoding='utf-8'))
        man = {r['path']: r['sha256'] for r in m['files']}
        for p, h in man.items():
            if not os.path.exists(p) or sha(open(p, 'rb').read()) != h: prob('manifest: impronta diversa dal file vivo', p)
    per_sha = {}
    for p, h in man.items():
        if h: per_sha.setdefault(h, set()).add(p)
    # file in esame: tutto il dossier + scope
    esame = sorted(set([T, V, SC] + [os.path.join(d, f).replace('\\', '/') for d, _, fs in os.walk(R) for f in fs]))
    for p in esame:
        b = os.path.basename(p)
        if p not in man and b not in ESCLUSI and p not in FUORI_MANIFEST:
            prob('file del dossier fuori dal manifest', p)
    # indici delle copie dei log
    originali, derivati, rinvio_storia, rinvio_log = {}, set(), [], []
    esterni_omessi, nomi_lavoro = set(), set()
    for p in man:
        if re.search(r'/(?:log-g[67]|lavoro)/indice\.json$', p):
            ind = json.load(open(p, encoding='utf-8'))
            for x in ind.get('log', []) + ind.get('file', []):
                esito = x.get('esito', 'copia')
                if esito == 'copia':
                    cp = R + '/' + x['copia']
                    if man.get(cp) != x['sha256_copia_ripulita']: prob('indice: copia non nel manifest o impronta diversa', p, dett=x['copia'])
                elif esito == 'uguale_al_file_del_dossier':
                    if man.get(x['riferimento']) != x['sha256_originale']: prob('indice: file dichiarato uguale ma impronta diversa', p, dett=x['riferimento'])
                elif esito == 'uguale_a_versione_storica':
                    rinvio_storia.append((p, x['sha256_originale'], x['riferimento']))
                elif esito == 'indicizzato_in_log':
                    rinvio_log.append((p, x['sha256_originale'], x['riferimento']))
                else: prob('indice: esito sconosciuto', p, dett=esito)
                originali[x['sha256_originale']] = p
                for k, v in x.items():
                    if k.startswith('sha256_') and k not in ('sha256_originale', 'sha256_copia_ripulita'): derivati.add(v)
                for o in x.get('omissioni', []):
                    derivati.add(o['sha256_blocco']); esterni_omessi.update(o.get('file_letti', []))
                if 'file' in x and 'cartella' in x: nomi_lavoro.add(os.path.basename(x['file']))
                for v in x.get('copie_precedenti', {}).values(): derivati.add(v)
    storia = storia_git(set(man) | {T, V, SC, R + '/chiusura.json'})
    derivati.add(intermedio())
    tracciati = set(subprocess.run(['git', 'ls-files', 'cap08'], capture_output=True, text=True, encoding='utf-8').stdout.split())
    for p, hh, rif in rinvio_log:
        ind = json.load(open(R + '/' + rif, encoding='utf-8'))
        if not any(x['sha256_originale'] == hh for x in ind['log']): prob('indice: log dichiarato indicizzato ma assente dall\'indice', p, dett=rif)
    for p, hh, rif in rinvio_storia:
        if rif not in storia.get(hh, set()): prob('indice: versione storica dichiarata non trovata nella storia git', p, dett=rif)
    for p in man:  # file di redazione: impronte dell'originale non pubblicato e della copia pubblicata
        if re.search(r'/G7-tentativo-\d+-redazione\.json$', p):
            x = json.load(open(p, encoding='utf-8')); derivati.add(x['sha256_originale'])
    vocab = set()
    for q in (R + '/procedura-congelata-r10.md', R + '/catalogo-congelato.md'):
        vocab |= set(PERCORSO.findall(open(q, encoding='utf-8').read()))
    # impronte di blocchi esterni
    imp = json.load(open(R + '/impronte-blocchi-esterni.json', encoding='utf-8'))
    finestre = set(imp['impronte']); nparole = imp['parole_per_finestra']
    conteggi = {'file_esaminati': 0, 'file_binari': 0, 'impronte_citate': 0, 'percorsi_citati': 0}
    for p in esame:
        if not os.path.exists(p) or os.path.basename(p) == nome_esito: continue  # esito di questa esecuzione, riscritto alla fine
        b, t = leggi(p); conteggi['file_esaminati'] += 1
        if t is None:
            # file binari: sequenze stampabili di almeno 12 caratteri e, per i PDF, il testo estratto con pdftotext se disponibile
            conteggi['file_binari'] += 1
            pezzi = [x.decode('ascii') for x in re.findall(rb'[\x20-\x7e]{12,}', b)]
            if p.endswith('.pdf'):
                try: pezzi += subprocess.run(['pdftotext', '-q', p, '-'], capture_output=True, text=True, encoding='utf-8', errors='replace').stdout.split('\n')
                except OSError: note['pdftotext'] = 'non disponibile: PDF controllati solo nelle sequenze stampabili'
            for i, r in enumerate(pezzi, 1):
                for nome, rx in (('percorso assoluto (unita\' disco)', UNITA), ('percorso UNC', UNC), ('percorso Unix', UNIX),
                                 ('variabile d\'ambiente di percorso', AMB), ('nome utente', UTENTE), ('dato personale', PERSONA)):
                    if rx.search(r): prob('(b) ' + nome + ' in file binario', p, dett='sequenza n. %d' % i)
            continue
        righe = t.split('\n')
        for i, r in enumerate(righe, 1):
            for nome, rx in (('percorso assoluto (unita\' disco)', UNITA), ('percorso UNC', UNC), ('percorso Unix', UNIX),
                             ('variabile d\'ambiente di percorso', AMB), ('nome utente', UTENTE), ('dato personale', PERSONA)):
                if rx.search(r): prob('(b) ' + nome, p, i)
        parole = re.findall(r'\S+', t)
        for i in range(0, max(0, len(parole) - nparole + 1)):
            if sha(' '.join(parole[i:i + nparole]).encode())[:16] in finestre:
                prob('(b) blocco di file esterno al progetto', p, dett='finestra di %d parole n. %d' % (nparole, i)); break
        # (a) solo per le evidenze del manifest
        if p not in man: continue
        for i, r in enumerate(righe, 1):
            for h in HEX.findall(r):
                h = h.lower(); conteggi['impronte_citate'] += 1
                if h in per_sha: continue
                if h in originali or h in derivati: continue
                if h in storia: continue
                prob('(a) impronta citata non risolta', p, i, h)
            for c1, c2 in CORTO.findall(r):
                ok = any(k.startswith(c1) and k.endswith(c2) for k in list(per_sha) + list(storia) + list(originali) + list(derivati))
                if not ok: prob('(a) impronta abbreviata non risolta', p, i, c1 + '…' + c2)
            r2 = SEGNAPOSTO_EST.sub(' ', r)        # percorsi sotto segnaposto esterni: file fuori dal progetto, contenuto non nel dossier
            r2 = SEGNAPOSTO_TEMP.sub(' ', r2)      # percorsi delle cartelle di lavoro: resta il nome del file, cercato nel manifest
            for q in PERCORSO.findall(r2):
                conteggi['percorsi_citati'] += 1; base = os.path.basename(q)
                qn = re.sub(r'^(?:\./|\.\./|[ab]/)+', '', q)
                if qn in man or any(k.endswith('/' + qn) or k == qn for k in man): continue
                if any(k.endswith(qn) for k in man) or any(k.endswith(qn) for k in ESCLUSI): continue  # frammento di riga spezzata nei log
                if base in esterni_omessi: continue  # file esterni letti nei log, contenuto omesso e dichiarato negli indici
                if base in nomi_lavoro: continue  # file delle cartelle di lavoro, dichiarati uno per uno in lavoro/indice.json
                if qn.startswith('cap08/') and qn in tracciati: continue  # altro file normativo del repository, citato come fuori scope
                if base in ALIAS and (ALIAS[base] in man or ALIAS[base] in FUORI_MANIFEST): continue
                if qn in FUORI_MANIFEST or any(k.endswith('/' + qn) for k in FUORI_MANIFEST): continue
                if q in vocab or qn in vocab: continue  # riferimenti al repository nel testo congelato di procedura e catalogo
                if re.fullmatch(r'\./indice-[\w.-]+\.md', q) and 'cap08/' + q[2:] in tracciati: continue  # collegamento di navigazione del testo normativo
                if base in ESCLUSI or base in GOVERNO or base in CARTELLA_G7: continue
                if re.fullmatch(r'(fase[12]|G7)-log\.txt', base): continue  # nomi degli originali, dichiarati negli indici
                if q == 'AGENTS.md' or q.endswith('/AGENTS.md'): continue  # file del workspace letto dal verificatore nei tentativi 1-3, contenuto omesso
                prob('(a) file citato non nel manifest', p, i, q)
    # (c) URL degli atti
    vt = open(V, encoding='utf-8').read(); g1 = open(R + '/g1/ricontrollo-20261022.json', encoding='utf-8').read()
    for u in URL_ATTI:
        if u not in vt: prob('(c) URL dell\'atto assente nel verbale', V, dett=u)
        if u not in g1: prob('(c) URL dell\'atto assente nel ricontrollo G1', R + '/g1/ricontrollo-20261022.json', dett=u)
    g1j = json.load(open(R + '/g1/ricontrollo-20261022.json', encoding='utf-8'))
    for k, u in g1j.get('url_consultati', {}).items():
        if u not in vt: prob('(c) URL consultato nel G1 assente nel verbale', V, dett=k)
    esito = {'controllo': 'controllo-dossier.py', 'sha256_script': sha(open(os.path.abspath(__file__), 'rb').read()), 'modo': a.modo,
             'insieme': 'lista-manifest.json con impronte vive' if a.modo == 'pre' else 'manifest-rilascio.json',
             'file_nel_insieme': len(man), **conteggi, 'problemi': len(problemi), 'elenco': problemi, 'note': note,
             'esclusi_per_costruzione': ESCLUSI}
    open(R + '/' + nome_esito, 'w', encoding='utf-8', newline='\n').write(json.dumps(esito, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps({k: esito[k] for k in ('modo', 'file_nel_insieme', 'file_esaminati', 'file_binari', 'impronte_citate', 'percorsi_citati', 'problemi')}, ensure_ascii=False))
    for x in problemi[:400]: print(json.dumps(x, ensure_ascii=False))
    sys.exit(1 if problemi else 0)
if __name__ == '__main__':
    main()
