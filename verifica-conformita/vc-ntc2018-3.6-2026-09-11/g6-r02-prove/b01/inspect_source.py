import hashlib
import json
from pathlib import Path

import fitz


SOURCE = Path(r"C:\Users\sandro\AppData\Local\Temp\vc36-fonti-vettoriali-r02-20260911\b01\fonte-ntc-vettoriale.pdf")
OUT = Path(r"C:\Users\sandro\AppData\Local\Temp\vc36-prove-v-r02-20260911\b01")
PHYSICAL = [66, 67, 68, 69]


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


doc = fitz.open(SOURCE)
dump = {
    "source": str(SOURCE),
    "source_sha256": sha256(SOURCE),
    "method": "PyMuPDF get_text('dict'); coordinate PDF in points, origin upper left",
    "pages": [],
}

for page_index, page in enumerate(doc):
    page_data = page.get_text("dict", flags=fitz.TEXTFLAGS_DICT)
    spans = []
    for block_index, block in enumerate(page_data.get("blocks", [])):
        if block.get("type") != 0:
            spans.append({
                "block": block_index,
                "type": block.get("type"),
                "bbox": block.get("bbox"),
                "width": block.get("width"),
                "height": block.get("height"),
                "ext": block.get("ext"),
            })
            continue
        for line_index, line in enumerate(block.get("lines", [])):
            for span_index, span in enumerate(line.get("spans", [])):
                text = span.get("text", "")
                spans.append({
                    "block": block_index,
                    "line": line_index,
                    "span": span_index,
                    "bbox": span.get("bbox"),
                    "font": span.get("font"),
                    "size": span.get("size"),
                    "flags": span.get("flags"),
                    "text": text,
                    "codepoints": [f"U+{ord(ch):04X}" for ch in text],
                })
    dump["pages"].append({
        "pdf_page": page_index + 1,
        "physical_page": PHYSICAL[page_index],
        "rect": list(page.rect),
        "spans": spans,
    })

(OUT / "pdf-spans.json").write_text(json.dumps(dump, ensure_ascii=False, indent=2), encoding="utf-8")

with (OUT / "pdf-lines.txt").open("w", encoding="utf-8") as f:
    for page_index, page in enumerate(doc):
        f.write(f"=== physical {PHYSICAL[page_index]} / pdf {page_index + 1} ===\n")
        blocks = page.get_text("blocks", sort=True)
        for b in blocks:
            x0, y0, x1, y1, text, *_ = b
            clean = " ".join(text.split())
            f.write(f"[{x0:.2f},{y0:.2f},{x1:.2f},{y1:.2f}] {clean}\n")

# Ritagli di tutti gli apparati matematici, con contesto immediato, a 600 dpi.
# Coordinate in punti PDF; i rettangoli includono tag/condizioni/definizioni.
crops = {
    "p66-formula-3.6.1": (0, (70, 690, 480, 736)),
    "p67-dove-3.6.1": (1, (75, 84, 530, 205)),
    "p68-formula-3.6.2": (2, (70, 236, 500, 278)),
    "p68-formula-3.6.3": (2, (70, 288, 500, 318)),
    "p68-formula-3.6.4": (2, (70, 327, 500, 356)),
    "p69-formule-3.6.5ab": (3, (145, 329, 496, 390)),
    "p69-dove-3.6.5ab": (3, (67, 375, 527, 473)),
    "p69-formula-3.6.6": (3, (70, 440, 490, 473)),
    "p69-inline-pd20": (3, (67, 520, 529, 599)),
}

matrix = fitz.Matrix(600 / 72, 600 / 72)
crop_manifest = []
for name, (page_index, coords) in crops.items():
    page = doc[page_index]
    clip = fitz.Rect(*coords) & page.rect
    pix = page.get_pixmap(matrix=matrix, clip=clip, alpha=False)
    target = OUT / f"{name}-600dpi.png"
    pix.save(target)
    crop_manifest.append({
        "name": name,
        "source": str(SOURCE),
        "source_sha256": sha256(SOURCE),
        "pdf_page": page_index + 1,
        "physical_page": PHYSICAL[page_index],
        "clip_points": list(clip),
        "dpi": 600,
        "pixels": [pix.width, pix.height],
        "method": "PyMuPDF get_pixmap, direct render from vector PDF",
        "path": str(target),
        "sha256": sha256(target),
    })

(OUT / "crop-manifest.json").write_text(json.dumps(crop_manifest, ensure_ascii=False, indent=2), encoding="utf-8")

# Sottoinsieme vettoriale esatto per gli apparati ritagliati.
apparati = []
for crop in crop_manifest:
    page_info = dump["pages"][crop["pdf_page"] - 1]
    clip = fitz.Rect(*crop["clip_points"])
    contained = []
    for span in page_info["spans"]:
        if "text" not in span:
            continue
        bbox = fitz.Rect(*span["bbox"])
        if bbox.intersects(clip):
            contained.append(span)
    apparati.append({**crop, "vector_spans": contained})

(OUT / "apparati-vettoriali.json").write_text(json.dumps(apparati, ensure_ascii=False, indent=2), encoding="utf-8")
