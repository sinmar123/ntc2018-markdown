"""Estrae figure C4.2.7-C4.2.13 dalla Circolare 2019 e le salva in cap04/img/.
Altezze clip custom per ogni figura. Lo script NON carica le immagini nel
contesto dell'agente: le scrive su disco con PyMuPDF."""
import fitz
import os

BASE = r"C:\Users\sandro\ag_oc\workspace\normativa\ntc2018"
pdf_path = os.path.join(BASE, "Circ_MIT_21_01_2019_7_rid.pdf")
img_dir = os.path.join(BASE, "cap04", "img")
os.makedirs(img_dir, exist_ok=True)

doc = fitz.open(pdf_path)
zoom = 2.5
mat = fitz.Matrix(zoom, zoom)

fig_specs = {
    "C4.2.7":  ("aste-composte-due-correnti", 260),
    "C4.2.8":  ("lunghezza-inflessione-correnti-tralicciate", 280),
    "C4.2.9":  ("schema-asta-calastrellata", 300),
    "C4.2.10": ("tipologie-elementi-ravvicinati", 250),
    "C4.2.11": ("trave-momenti-estremita", 260),
    "C4.2.12": ("irrigidimenti-longitudinali-anima", 260),
    "C4.2.13": ("luci-equivalenti-travi-continue", 260),
}

def find_caption(label):
    """Trova la didascalia: prima occorrenza di 'Figura <label>' come inizio riga
    su una pagina. Restituisce (page_idx, rect_didasc)."""
    patterns = [
        f"Figura {label}-",
        f"Figura {label} -",
        f"Figura {label} \u2013",
        f"Figura {label}\u2013",
        f"Figura {label}.",
        f"Figura {label} ",
    ]
    for p in range(len(doc)):
        page = doc[p]
        for pat in patterns:
            areas = page.search_for(pat)
            if areas:
                return p, areas[0]
    return None

for label, (slug, h) in fig_specs.items():
    res = find_caption(label)
    if res is None:
        print(f"NOT FOUND: {label}")
        continue
    page_idx, rect = res
    page = doc[page_idx]
    page_rect = page.rect
    y_top = max(page_rect.y0 + 20, rect.y0 - h)
    clip = fitz.Rect(page_rect.x0 + 30, y_top, page_rect.x1 - 30, rect.y1 + 8)
    pix = page.get_pixmap(matrix=mat, clip=clip)
    fname = f"fig-{label.lower()}-{slug}.png"
    pix.save(os.path.join(img_dir, fname))
    print(f"SAVED: {fname}  (page {page_idx+1}, clip y {y_top:.0f}-{rect.y1:.0f}, size {pix.width}x{pix.height})")

doc.close()
print("Done.")
