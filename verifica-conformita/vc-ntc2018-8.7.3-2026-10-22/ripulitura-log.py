"""Ripulitura dei log di Codex CLI per il dossier VC 8.7.3 (GBOT-verifica-ntc, 2026-10-22).

Un log originale (UTF-16 LE con BOM, scritto da PowerShell) diventa una copia UTF-8 senza BOM:
1. il contenuto di file letti fuori dalla cartella di lavoro e dal progetto (AGENTS.md del workspace,
   documentazione dei plugin di Codex) e' sostituito da una riga
   <contenuto di ... omesso: N righe, sha256 H>, dove H e' l'impronta del testo omesso (UTF-8, finali di riga inclusi);
2. ogni percorso assoluto e' sostituito da un segnaposto: <temp>, <npm>, <codex-home>, <workspace>, <home>,
   <powershell>, <sistema>, <unita>.
Nient'altro cambia: finali di riga e caratteri gia' mal convertiti da PowerShell restano come nell'originale.
"""
import re, hashlib
SEP = r'[\\/]+'
COMP = r'[^\\/\s\'"`<>|:*?]+'
D = r'(?<![A-Za-z0-9])[A-Za-z]:' + SEP
SOST = [
    ('profilo', re.compile(r'(?i)' + D + 'Users' + SEP + r'(?:<utente>|' + COMP + r')(?:' + SEP + r'(AppData' + SEP + r'Local' + SEP + r'Temp|AppData' + SEP + r'Roaming' + SEP + r'npm|\.codex|ag_oc' + SEP + r'workspace))?(?![A-Za-z0-9_])')),
    ('powershell', re.compile(r'(?i)' + D + 'WINDOWS' + SEP + 'System32' + SEP + 'WindowsPowerShell' + SEP + r'v1\.0' + SEP + r'powershell\.exe')),
    ('sistema', re.compile(r'(?i)' + D + r'WINDOWS(?![A-Za-z0-9_])')),
    ('unita', re.compile(D)),
]
SEGNA = {'appdata/local/temp': '<temp>', 'appdata/roaming/npm': '<npm>', '.codex': '<codex-home>', 'ag_oc/workspace': '<workspace>'}
DESCR = {'<temp>': 'cartella temporanea del profilo utente (unita\', Users, nome utente, AppData, Local, Temp)',
         '<npm>': 'cartella npm del profilo utente (lanciatore di Codex)', '<codex-home>': 'cartella di configurazione di Codex nel profilo utente',
         '<workspace>': 'workspace dell\'utente', '<home>': 'profilo utente (unita\', Users, nome utente)',
         '<powershell>': 'eseguibile di Windows PowerShell nella cartella di sistema', '<sistema>': 'cartella di sistema di Windows',
         '<unita>': 'lettera di unita\' disco di un altro percorso assoluto'}
MARCATORI = {'exec', 'codex', 'user', 'thinking', 'tokens used'}
ESTERNO = re.compile(r'(?i)(?:ag_oc' + SEP + r'workspace|' + SEP + r'\.codex' + SEP + r')')
sha = lambda s: hashlib.sha256(s.encode('utf-8')).hexdigest()

def omissioni(t):
    """sostituisce l'output dei comandi che leggono file esterni; restituisce testo e annotazioni"""
    righe = t.split('\n'); out = []; note = []; i = 0
    while i < len(righe):
        if righe[i].rstrip('\r') != 'exec':
            out.append(righe[i]); i += 1; continue
        j = i + 1
        while j < len(righe) and not re.match(r'^ (succeeded|failed|exited)\b.*:\r?$', righe[j]): j += 1
        if j >= len(righe): out.extend(righe[i:]); break
        head = '\n'.join(righe[i + 1:j]); out.extend(righe[i:j + 1])
        k = j + 1
        while k < len(righe) and righe[k].rstrip('\r') not in MARCATORI: k += 1
        corpo = righe[j + 1:k]
        if ESTERNO.search(head):
            fine = next((n for n, r in enumerate(corpo) if r.startswith('# Consegna al verificatore')), len(corpo))
            est = corpo[:fine]
            while est and est[-1].rstrip('\r') == '': est = est[:-1]
            if est:
                cosa = 'AGENTS.md del workspace' if re.search(r'(?i)AGENTS\.md', head) else 'file della documentazione dei plugin di Codex'
                testo = '\n'.join(est) + ('\n' if est else '')
                cr = '\r' if est[0].endswith('\r') else ''
                riga = '<contenuto di %s omesso: %d righe, sha256 %s>' % (cosa, len(est), sha(testo))
                letti = sorted(set(re.findall(r'(?i)(?:ag_oc' + SEP + r'workspace|\.codex)[^\'"]*?[\\/]([A-Za-z0-9_.-]+\.(?:md|json|txt|py))', head)))
                note.append({'cosa': cosa, 'righe': len(est), 'sha256_blocco': sha(testo), 'riga_nella_copia': len(out) + 1, 'file_letti': letti, '_testo': testo})
                out.append(riga + cr); out.extend(corpo[len(est):])
            else:
                out.extend(corpo)
        else:
            out.extend(corpo)
        i = k
    return '\n'.join(out), note

def percorsi(t):
    cont = {}
    def rep_profilo(m):
        suf = (m.group(1) or '').lower().replace('\\', '/'); suf = re.sub('/+', '/', suf)
        seg = SEGNA.get(suf, '<home>'); cont[seg] = cont.get(seg, 0) + 1; return seg
    t = SOST[0][1].sub(rep_profilo, t)
    for nome, rx in SOST[1:]:
        seg = '<%s>' % nome
        def rep(m, seg=seg):
            cont[seg] = cont.get(seg, 0) + 1
            return seg + (m.group(0)[-1] if nome == 'unita' else '')
        t = rx.sub(rep, t)
    return t, [{'da': DESCR[k], 'a': k, 'occorrenze': v} for k, v in cont.items()]

def ripulisci(b):
    assert b[:2] == b'\xff\xfe', 'atteso UTF-16 LE con BOM'
    t = b[2:].decode('utf-16-le'); prima = sha(t)
    t, om = omissioni(t); t, so = percorsi(t)
    return t, prima, om, so
