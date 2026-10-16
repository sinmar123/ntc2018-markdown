"""CDX: prepara proposte e piano di presa. Non modifica il testo normativo."""
from pathlib import Path
from datetime import datetime
import difflib
import hashlib
import json
import re

D = Path(__file__).resolve().parent.parent
R = D.parent.parent
FILE = 'cap08/8.6-materiali.md'
original = (R / FILE).read_text(encoding='utf-8-sig')
snapshot = json.loads((D / 'snapshot-iniziale.json').read_text(encoding='utf-8'))
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def save(name, obj): (D / name).write_text(json.dumps(obj, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
rows = []
def add(before, after, note, y, proof='c/circ-8.6-600dpi.png'):
    rows.append({'id': f'L{len(rows)+1:02d}', 'file': FILE, 'riga_iniziale': 15 if not rows else 16, 'pagina_fisica': 269, 'pagina_stampata': 265, 'y_pt': y, 'prova': proof, 'attuale': before, 'proposto': after, 'classe': 'ERR-MD', 'effetto': 'sola presentazione/grafia; nessun valore o contenuto tecnico modificato', 'nota': note, 'decisione': 'DA_APPROVARE', 'esito': 'NON_APPLICATA'})
add('## C8.6. Materiali', '## C8.6 MATERIALI\n', 'Rubrica come nella fonte: senza punto dopo il numero e in maiuscolo; riga vuota prima del testo.', 401.5, 'c/circ-rubrica-600dpi.png')
for before, y in [
    ('costruzioni esistenti. I casi di incompatibilità', 441.0),
    ('chimiche tra di essi. Le differenze di rigidezza', 464.6),
    ('è estremamente variabile. Si ricorda che i valori', 498.8),
    ('sollecitazioni nei materiali. Differenze di comportamento termico', 533.0),
    ('termiche e/o igrometriche. Anche i fenomeni di ritiro', 577.7),
    ('stati di coazione. Infine vanno adeguatamente', 612.0),
    ('incompatibilità chimiche. È pertanto necessaria', 625.1),
    ('materiali di apporto. Per quanto riguarda', 648.7),
]:
    add(before, before.replace('. ', '.\n\n', 1), 'Ripristino di un confine di capoverso presente nella fonte; otto confini riportano il testo a nove capoversi.', y)
add('È pertanto necessaria,', 'E’ pertanto necessaria,', 'Conservazione letterale della grafia E + apostrofo della fonte. Non è equivalenza Unicode canonica con È e il catalogo non la autorizza espressamente. Nessuna AF-COR introdotta.', 625.1, 'c/circ-e-apostrofo-600dpi.png')
proposed = original
for row in rows:
    assert proposed.count(row['attuale']) == 1, row['id']
    proposed = proposed.replace(row['attuale'], row['proposto'], 1)
save('lista-correzioni-c.json', rows)
(D / 'diff-proposto.patch').write_text(''.join(difflib.unified_diff(original.splitlines(True), proposed.splitlines(True), fromfile=FILE+' (attuale)', tofile=FILE+' (proposta non applicata)')), encoding='utf-8')
def norm(s): return ' '.join(re.sub(r'(?<=\w)-\s*\n(?=\w)', '', s).split())
ntc_source = re.sub(r'^8\.6\.\s*MATERIALI\s*', '', (D/'c/ntc-8.6-testo-ausiliario.txt').read_text(encoding='utf-8'))
circ_source = re.sub(r'^C8\.6\s*MATERIALI\s*', '', (D/'c/circ-8.6-testo-ausiliario.txt').read_text(encoding='utf-8'))
ntc_target = original.split('## Norma',1)[1].split('---',1)[0]
circ_target = original.split('## C8.6. Materiali',1)[1]
circ_proposed = proposed.split('## C8.6 MATERIALI',1)[1]
assert norm(ntc_source) == norm(ntc_target), 'Differenza residua nella Norma'
assert norm(circ_source) == norm(circ_proposed), 'Differenza residua nella Circolare proposta'
assert norm(circ_source) == norm(circ_target).replace('È pertanto necessaria,', 'E’ pertanto necessaria,'), 'Differenza non censita nel testo iniziale'
save('confronto-testuale.json', {'firma':'Codex (CDX)', 'metodo':'Confronto integrale del testo estratto, spazi e sillabazione a fine riga normalizzati; controllo visivo separato sulle pagine e sui ritagli.', 'norma_testo':'IDENTICO', 'circolare_unica_differenza_testuale':'E’ nella fonte, È nel target', 'capoversi_circolare_fonte':9, 'capoversi_circolare_target':1, 'proposta_solo_in_memoria':'IDENTICA al testo fonte dopo le normalizzazioni dichiarate', 'target_sha256_invariato':sha(R/FILE), 'liste':len(rows)})
table = ['# § 8.6 e C8.6: elenco delle non conformità', '', 'Firma: Codex (CDX), 2026-10-16. Proposte non applicate.', '', 'Fonte: Circolare, pagina fisica 269, stampata 265. Norma a pagina fisica 297, stampata 293: nessun rilievo. Tutto il testo della Norma e della Circolare è stato confrontato; nessun apparato numerico nello scope.', '', '| ID | Posizione | Attuale | Proposto | Prova e motivo |', '|---|---|---|---|---|']
for row in rows:
    before = row['attuale'].replace('\n', ' ⏎ ')
    after = row['proposto'].replace('\n\n', ' ⏎⏎ ').replace('\n', ' ⏎ ')
    table.append(f"| {row['id']} | riga {row['riga_iniziale']}; y={row['y_pt']} pt | `{before}` | `{after}` | [{row['nota']}]({row['prova']}) |")
table += ['', 'Le righe L02-L09 introducono otto separazioni, ottenendo i nove capoversi della fonte. L10 conserva la grafia stampata, senza correggere editorialmente la fonte. Tutte le voci sono ERR-MD di presentazione/grafia; nessun valore o prescrizione cambia. Decisione: da approvare. Esito: non applicate.', '', '[Lista eseguibile](lista-correzioni-c.json) · [Diff completo proposto](diff-proposto.patch) · [Pagina ufficiale completa](c/circ-p269-200dpi.png)', '', 'La VC resta aperta: G5, G6 indipendente e G7 seguiranno dopo la decisione sulle correzioni. Un solo blocco G6 coprirà le due porzioni di pagina.', '', 'Prossima azione: decisione di Sandro sulla lista L01-L10; poi correzioni approvate e un blocco G6.']
(D/'lista-correzioni-c.md').write_text('\n'.join(table)+'\n', encoding='utf-8')
proc = D/'procedura-congelata-lettura-web.md'
save('provenienza-procedura.json', {'firma':'Codex (CDX)', 'url':'https://raw.githubusercontent.com/sinmar123/ntc2018-markdown/main/PROCEDURA-VC.md', 'revisione':9, 'data_lettura':'2026-10-16', 'metodo':'Lettura web completa, righe 0-188 del lettore; copia testuale ricostruita dalle righe, senza intestazioni del lettore.', 'sha256_copia_testuale':sha(proc), 'limite':'Non è attestata identità byte per byte con il file remoto. Prima del rilascio acquisire il file originale e sincronizzare il ramo con main. La base Git locale è 2f9fb3a, revisione 8; il § 2 della revisione 9 è adottato per delimitare il solo 8.6.'})
now = datetime.now().astimezone().isoformat(timespec='seconds')
next_action = 'Decisione di Sandro sulla lista L01-L10; poi correzioni approvate e un blocco G6. Prima del rilascio sincronizzare Git e aprire la pull request.'
sheet = f'''---
scope_id: ntc2018-8.6
stato: IN-CORSO
agente: CDX
presa_in_carico: {now}
procedura: VC-NTC/9
procedura_sha256: {sha(proc)}
procedura_copia: vc-ntc2018-8.6-2026-10-16/procedura-congelata-lettura-web.md
catalogo_sha256: {sha(D/'catalogo-congelato.md')}
file_markdown: [cap08/8.6-materiali.md]
righe_registro: ["8.6"]
snapshot_sha256: {snapshot['target_sha256']}
giro_g6: 0
max_giri: 3
rilievi_aperti: 10
gate: {{G0: OK, G1: OK, G2: OK, G3: KO, G4: OK, G5: DA_FARE, G6: DA_FARE, G7: DA_FARE}}
attesa_decisione: [L01, L02, L03, L04, L05, L06, L07, L08, L09, L10]
routing_effettivo:
  C: "Codex (CDX), GPT-6; identificativo specifico del modello non esposto"
  preparazione: "Script locali; nessun modello leggero necessario"
  E: non_attivato
  V: "Previsto gpt-5.6-sol xhigh in contesto nuovo; non ancora avviato"
---

# Scheda scope § 8.6

## 2026-10-16 - Presa locale e confronto completo, CDX

Autorizzazione di Sandro: «fai 8.6». Solo `cap08/8.6-materiali.md`, da 8.6 a prima di 8.7 nelle NTC (p. fisica 297) e da C8.6 a prima di C8.7 nella Circolare (p. fisica 269). Un solo blocco G6 previsto. Esclusi tutti gli altri paragrafi delle pagine condivise.

Ramo `cdx/vc-8.6-261016`, worktree separata. Presa nel CSV di questo ramo soltanto: nessun lucchetto pubblicato su GitHub, perché il collegamento Git HTTPS non è disponibile. Base locale `2f9fb3a`. Testo remoto consultato tramite lettore web; identità byte per byte con main non attestata. Prima del rilascio sincronizzare e ricontrollare il perimetro se sono intervenute modifiche.

Adottata VC-NTC/9 letta integralmente da GitHub; copia testuale e limite di acquisizione in [provenienza](vc-ntc2018-8.6-2026-10-16/provenienza-procedura.json). Catalogo congelato identico alla copia locale.

Confronto completo di C: Norma conforme; Circolare, una rubrica, otto confini di capoverso e la grafia E’/È. Nove capoversi fonte contro uno nel target. Lo script ha trovato sette degli otto confini: quello prima di E’ è stato recuperato dal controllo visivo. Nessuna formula, tabella o figura nello scope; richiami 8.5.3, 8.6, C.8.5.I e Capitolo 12 riscontrati. Prove a 600 dpi e codifica PDF nel dossier. Target invariato. Lista unica [L01-L10](vc-ntc2018-8.6-2026-10-16/lista-correzioni-c.md).

G1: riuso della ricognizione del 2026-10-13 e ricontrollo web del 2026-10-16; applicabilità e limiti nel dossier G1. G5-G7 non avviati. G3 resta KO fino alla decisione e all'applicazione delle correzioni approvate.

Prossima azione: {next_action}
'''
save('presa.json', {'scope':'8.6', 'righe':['8.6'], 'agente':'CDX', 'scheda':'verifica-conformita/scheda-scope-ntc2018-8.6.md', 'scheda_contenuto':sheet, 'nota':'VC locale del solo 8.6/C8.6 autorizzata da Sandro il 2026-10-16. Ramo CDX separato; confronto completo con 10 rilievi di presentazione/grafia da approvare; target invariato. Presa non ancora pubblicata su GitHub.', 'prossima_azione':next_action})
print(json.dumps({'proposte':len(rows), 'norma':'testo conforme', 'circolare':'nove capoversi, rubrica e grafia documentati', 'target_invariato':sha(R/FILE)==snapshot['target_sha256']}, ensure_ascii=False))
