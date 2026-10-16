"""CDX: estrazione riproducibile delle prove fonte del solo 8.6/C8.6."""
from pathlib import Path
import hashlib
import json
import shutil
import fitz

HERE = Path(__file__).resolve().parent
DOSSIER = HERE.parent
ROOT = DOSSIER.parent.parent

def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

sources = [
    ('ntc', 'GU-2018-42-SO8-DM-17-01-2018.pdf', 297, (65, 427, 535, 500), 'dda1e397d56d71aa0f5bc457c3ba9b77064a468699dfc37bd056ac6c47105a46'),
    ('circ', 'GU-2019-35-SO5-Circolare-7-2019.pdf', 269, (65, 398, 535, 683), 'f7c3b8d1f443aadb6b3e020b6b6c19813683492ecaadd2c15bf6bf1939aaed7c'),
]
records = []
for label, name, number, coords, expected in sources:
    path = ROOT / 'verifica-conformita/fonte-ufficiale' / name
    actual = sha(path)
    assert actual == expected, (name, actual)
    doc = fitz.open(path)
    page = doc[number - 1]
    clip = fitz.Rect(coords)
    page_path = HERE / f'{label}-p{number}-200dpi.png'
    crop_path = HERE / f'{label}-8.6-600dpi.png'
    page.get_pixmap(dpi=200, alpha=False).save(page_path)
    page.get_pixmap(dpi=600, clip=clip, alpha=False).save(crop_path)
    text_path = HERE / f'{label}-8.6-testo-ausiliario.txt'
    text_path.write_text(page.get_text(clip=clip), encoding='utf-8')
    vector_path = HERE / f'{label}-8.6-codifica.json'
    vector_path.write_text(json.dumps(page.get_text('dict', clip=clip), ensure_ascii=False, indent=2, default=lambda value: {'bytes': len(value), 'sha256': hashlib.sha256(value).hexdigest()}), encoding='utf-8')
    if label == 'circ':
        page.get_pixmap(dpi=600, clip=fitz.Rect(70, 623, 135, 637), alpha=False).save(HERE / 'circ-e-apostrofo-600dpi.png')
        page.get_pixmap(dpi=600, clip=fitz.Rect(70, 397, 198, 416), alpha=False).save(HERE / 'circ-rubrica-600dpi.png')
    records.append({'fonte': label, 'pdf': str(path.relative_to(ROOT)).replace('\\', '/'), 'sha256': actual, 'pagine_totali': len(doc), 'pagina_fisica': number, 'bbox_scope_pt': coords, 'metodo': 'PyMuPDF; pagina vettoriale, rasterizzazione diretta 200 dpi e ritaglio 600 dpi', 'pagina_png': page_path.name, 'ritaglio_png': crop_path.name, 'testo_ausiliario': text_path.name, 'codifica': vector_path.name})
target = ROOT / 'cap08/8.6-materiali.md'
shutil.copyfile(target, DOSSIER / 'target-iniziale.md')
shutil.copyfile(ROOT / 'verifica-conformita/normalizzazioni-dichiarate-NTC2018.md', DOSSIER / 'catalogo-congelato.md')
metadata = {'firma': 'Codex (CDX)', 'scope': '8.6', 'data': '2026-10-16', 'fonti': records, 'target': 'cap08/8.6-materiali.md', 'target_sha256': sha(target), 'target_modificato': False}
(DOSSIER / 'snapshot-iniziale.json').write_text(json.dumps(metadata, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
print(json.dumps(metadata, ensure_ascii=False))
