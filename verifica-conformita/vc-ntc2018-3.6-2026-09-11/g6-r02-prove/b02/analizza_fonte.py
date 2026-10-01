import hashlib
import json
from pathlib import Path

import fitz


PROVE = Path(r"C:\Users\sandro\AppData\Local\Temp\vc36-prove-v-r02-20260911\b02")
FONTI = Path(r"C:\Users\sandro\AppData\Local\Temp\vc36-fonti-vettoriali-r02-20260911\b02")

PDFS = {
    "ntc": FONTI / "fonte-ntc-vettoriale.pdf",
    "circ": FONTI / "fonte-circ-vettoriale.pdf",
}


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def chars_of(page):
    out = []
    raw = page.get_text("rawdict")
    for block in raw.get("blocks", []):
        if block.get("type") != 0:
            continue
        for line in block.get("lines", []):
            for span in line.get("spans", []):
                chars = span.get("chars", [])
                text = "".join(c.get("c", "") for c in chars)
                out.append(
                    {
                        "text": text,
                        "font": span.get("font"),
                        "size": span.get("size"),
                        "flags": span.get("flags"),
                        "bbox": span.get("bbox"),
                        "chars": [
                            {
                                "c": c.get("c", ""),
                                "codepoint": f"U+{ord(c.get('c', ' ')):04X}",
                                "bbox": c.get("bbox"),
                                "origin": c.get("origin"),
                            }
                            for c in chars
                        ],
                    }
                )
    return out


layout = {
    "firma": "CDX, verificatore V indipendente G6, modello effettivo gpt-5.6-sol xhigh",
    "metodo": "PyMuPDF 1.27.1, get_text(rawdict); coordinate PDF in punti dall'angolo superiore sinistro",
    "fonti": [],
}

for atto, pdf_path in PDFS.items():
    doc = fitz.open(pdf_path)
    src = {
        "atto": atto,
        "pdf": str(pdf_path),
        "sha256": sha256(pdf_path),
        "pagine": [],
    }
    for i, page in enumerate(doc):
        pagina_fisica = (70 + i) if atto == "ntc" else (81 + i)
        src["pagine"].append(
            {
                "chiave": f"{atto}:{pagina_fisica}",
                "indice_pdf": i,
                "mediabox": list(page.rect),
                "spans": chars_of(page),
            }
        )
    layout["fonti"].append(src)

out = PROVE / "layout-vettoriale.json"
out.write_text(json.dumps(layout, ensure_ascii=False, indent=2), encoding="utf-8")
print(out)
print(sha256(out))
