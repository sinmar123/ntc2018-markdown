import hashlib
import json
from pathlib import Path

import fitz


PROVE = Path(r"C:\Users\sandro\AppData\Local\Temp\vc36-prove-v-r02-20260911\b02")
FONTI = Path(r"C:\Users\sandro\AppData\Local\Temp\vc36-fonti-vettoriali-r02-20260911\b02")

SPECS = [
    ("ntc", "fonte-ntc-vettoriale.pdf", 0, "ntc-70-tab-3.6.II.png", (65, 224, 380, 286), "Tabella 3.6.II: didascalia, testata e tre righe"),
    ("ntc", "fonte-ntc-vettoriale.pdf", 0, "ntc-70-formula-3.6.7.png", (175, 375, 380, 398), "Formula [3.6.7], inclusi pedici e parentesi del tag"),
    ("ntc", "fonte-ntc-vettoriale.pdf", 0, "ntc-70-tab-3.6.III.png", (65, 413, 380, 526), "Tabella 3.6.III: didascalia, testata e tutte le righe/celle"),
    ("ntc", "fonte-ntc-vettoriale.pdf", 0, "ntc-70-formula-3.6.8.png", (190, 607, 380, 630), "Formula [3.6.8], inclusi pedici e parentesi del tag"),
    ("ntc", "fonte-ntc-vettoriale.pdf", 0, "ntc-70-formula-3.6.9.png", (195, 696, 380, 718), "Formula [3.6.9], incluse parentesi del tag"),
    ("ntc", "fonte-ntc-vettoriale.pdf", 1, "ntc-71-condizioni-distanza.png", (65, 291, 405, 383), "Tre condizioni sulla distanza d e quattro valori di forza"),
    ("circ", "fonte-circ-vettoriale.pdf", 0, "circ-81-inline-qfd.png", (320, 678, 365, 697), "Notazione inline q con pedice f,d"),
    ("circ", "fonte-circ-vettoriale.pdf", 1, "circ-82-rubrica-C3.6.1.5.1.png", (65, 566, 280, 585), "Rubrica C3.6.1.5.1"),
    ("circ", "fonte-circ-vettoriale.pdf", 1, "circ-82-rubrica-C3.6.1.5.3.png", (65, 712, 300, 731), "Rubrica C3.6.1.5.3"),
    ("circ", "fonte-circ-vettoriale.pdf", 2, "circ-83-rubrica-C3.6.1.5.4.png", (65, 203, 250, 222), "Rubrica C3.6.1.5.4"),
]


def digest(path):
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


docs = {}
items = []
scale = 600 / 72
for atto, pdf_name, page_index, out_name, rect, oggetto in SPECS:
    pdf_path = FONTI / pdf_name
    doc = docs.setdefault(pdf_name, fitz.open(pdf_path))
    page = doc[page_index]
    clip = fitz.Rect(rect)
    pix = page.get_pixmap(matrix=fitz.Matrix(scale, scale), clip=clip, alpha=False)
    pix.set_dpi(600, 600)
    out = PROVE / out_name
    pix.save(out)
    page_physical = (70 + page_index) if atto == "ntc" else (81 + page_index)
    items.append(
        {
            "pagina": f"{atto}:{page_physical}",
            "indice_pdf_zero_based": page_index,
            "oggetto": oggetto,
            "clip_pdf_pt": list(rect),
            "dpi": 600,
            "file": str(out),
            "pixel": [pix.width, pix.height],
            "sha256": digest(out),
        }
    )

manifest = {
    "firma": "CDX, verificatore V indipendente G6, modello effettivo gpt-5.6-sol xhigh",
    "metodo": "PyMuPDF 1.27.1, rasterizzazione diretta del PDF vettoriale con matrice 600/72 e clip in coordinate PDF",
    "ritagli": items,
}
manifest_path = PROVE / "provenienza-ritagli.json"
manifest_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")
print(manifest_path)
print(digest(manifest_path))
