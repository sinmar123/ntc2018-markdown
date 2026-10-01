import hashlib
import json
from pathlib import Path

import fitz


SOURCE = Path(r"C:\Users\sandro\AppData\Local\Temp\vc36-g6-r02-20260911\b01\resa-target\target-blocco.pdf")
OUT = Path(r"C:\Users\sandro\AppData\Local\Temp\vc36-prove-v-r02-20260911\b01")


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

with (OUT / "target-lines.txt").open("w", encoding="utf-8") as line_out:
    for page_index, page in enumerate(doc):
        page_data = page.get_text("dict", flags=fitz.TEXTFLAGS_DICT)
        spans = []
        for block_index, block in enumerate(page_data.get("blocks", [])):
            if block.get("type") != 0:
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
        dump["pages"].append({"pdf_page": page_index + 1, "rect": list(page.rect), "spans": spans})
        line_out.write(f"=== target page {page_index + 1} ===\n")
        for b in page.get_text("blocks", sort=True):
            x0, y0, x1, y1, text, *_ = b
            line_out.write(f"[{x0:.2f},{y0:.2f},{x1:.2f},{y1:.2f}] {' '.join(text.split())}\n")

(OUT / "target-spans.json").write_text(json.dumps(dump, ensure_ascii=False, indent=2), encoding="utf-8")

# Prova del possibile taglio in testa alla pagina 4: il rettangolo include anche
# coordinate negative, che PyMuPDF interseca con la MediaBox per la resa.
page = doc[3]
clip = fitz.Rect(0, 0, 595, 105)
matrix = fitz.Matrix(600 / 72, 600 / 72)
pix = page.get_pixmap(matrix=matrix, clip=clip, alpha=False)
target = OUT / "target-p04-top-600dpi.png"
pix.save(target)

relevant = [s for s in dump["pages"][3]["spans"] if fitz.Rect(*s["bbox"]).intersects(clip)]
proof = {
    "source": str(SOURCE),
    "source_sha256": sha256(SOURCE),
    "pdf_page": 4,
    "page_rect_points": list(page.rect),
    "clip_points": list(clip),
    "dpi": 600,
    "pixels": [pix.width, pix.height],
    "path": str(target),
    "sha256": sha256(target),
    "method": "PyMuPDF get_pixmap from target vector PDF",
    "vector_spans_intersecting_clip": relevant,
}
(OUT / "target-p04-top-proof.json").write_text(json.dumps(proof, ensure_ascii=False, indent=2), encoding="utf-8")

# Resa effettiva degli apparati matematici numerati e del blocco definitorio
# successivo alla [3.6.1], sempre dal PDF canonico vettoriale.
formula_manifest = []
for page_index, page in enumerate(doc):
    for tag in ("3.6.1", "3.6.2", "3.6.3", "3.6.4", "3.6.5a", "3.6.5b", "3.6.6"):
        hits = page.search_for(f"[{tag}]")
        for hit_index, hit in enumerate(hits, start=1):
            clip = fitz.Rect(45, max(0, hit.y0 - 22), min(page.rect.x1 - 45, 570), min(page.rect.y1, hit.y1 + 18))
            pix = page.get_pixmap(matrix=matrix, clip=clip, alpha=False)
            name = f"target-p{page_index + 1:02d}-formula-{tag}-{hit_index}-600dpi.png"
            path = OUT / name
            pix.save(path)
            formula_manifest.append({
                "tag": tag,
                "pdf_page": page_index + 1,
                "tag_bbox_points": list(hit),
                "clip_points": list(clip),
                "dpi": 600,
                "path": str(path),
                "sha256": sha256(path),
            })

page = doc[1]
clip = fitz.Rect(45, 45, 570, 170)
pix = page.get_pixmap(matrix=matrix, clip=clip, alpha=False)
path = OUT / "target-p02-dove-3.6.1-600dpi.png"
pix.save(path)
formula_manifest.append({
    "tag": "dove-3.6.1",
    "pdf_page": 2,
    "clip_points": list(clip),
    "dpi": 600,
    "path": str(path),
    "sha256": sha256(path),
})

(OUT / "target-formula-crop-manifest.json").write_text(json.dumps(formula_manifest, ensure_ascii=False, indent=2), encoding="utf-8")
