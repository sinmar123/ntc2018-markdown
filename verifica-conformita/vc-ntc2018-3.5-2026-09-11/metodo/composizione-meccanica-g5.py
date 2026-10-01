from pathlib import Path
import hashlib
import json
import re
import runpy
import shutil

root = Path('C:/Users/sandro/ag_oc/workspace/normativa/ntc2018--norme-costruzioni')
out = root / '_tmp_render/cap03/vc-3.5-20260911-cdx/g5-cdx-r02'
out.mkdir(exist_ok=False)
depura = runpy.run_path(str(root / 'strumenti/prepara-scope-g6.py'))['depura']
files = [root / 'cap03/3.5-introduzione.md'] + sorted((root / 'cap03').glob('3.5.*-*.md'))
assert len(files) == 8
ntc, circ, sources = [], [], []
for path in files:
    parts = path.read_text(encoding='utf-8').split('## Circolare', 1)
    ntc.append(depura(parts[0]).strip())
    if len(parts) == 2:
        body = re.sub(r'(?m)^\*Circolare 21/01/2019[^\n]*\n?', '', parts[1])
        circ.append(depura(body).strip())
    sources.append(path.relative_to(root).as_posix())
text = '\n\n'.join(x for x in ntc + circ if x) + '\n'
(out / 'target-scope.md').write_text(text, encoding='utf-8', newline='\n')
assets = ['cap03/img/fig-3.5.1-zone-temperatura-mappa.png', 'cap03/img/fig-3.5.2-temperatura-elemento-schema.png']
for asset in assets:
    target = out / 'img' / Path(asset).name
    target.parent.mkdir(exist_ok=True)
    shutil.copyfile(root / asset, target)
    assert (root / asset).read_bytes() == target.read_bytes()
(out / 'lista-snapshot.json').write_text(json.dumps(sources + assets, indent=2) + '\n', encoding='utf-8')
proof = {'firma': 'Codex / CDX, script meccanico', 'sorgenti': sources, 'righe': len(text.splitlines()), 'righe_non_vuote': sum(bool(x.strip()) for x in text.splitlines()), 'sha256_composito': hashlib.sha256((out/'target-scope.md').read_bytes()).hexdigest(), 'metodo': 'depura comune; Norma in ordine degli otto file, poi Circolare; esclusa riga editoriale Circolare 21/01/2019; rimozione meccanica rinvii annotazioni', 'mappa_pagine_righe': {'ntc:63': [1,8], 'ntc:64': [9,61], 'ntc:65': [62,112], 'ntc:66': [113,129], 'circ:81': [130,136]}}
assert proof['righe'] == 136
(out / 'composizione.json').write_text(json.dumps(proof, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
print(json.dumps({'destinazione': str(out), **proof}, ensure_ascii=True))
