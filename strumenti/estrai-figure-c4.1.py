"""Estrae le 13 figure del §C4.1 dalla Circolare 2019 e le salva in cap04/img/.
Usa altezze custom per figura per clip piu' aderenti, e gestisce Fig. C4.1.10
che e' a cavallo di due pagine."""
import fitz
import os
from PIL import Image
from io import BytesIO

BASE = r"C:\Users\sandro\ag_oc\workspace\normativa\ntc2018"
pdf_path = os.path.join(BASE, "Circ_MIT_21_01_2019_7_rid.pdf")
img_dir = os.path.join(BASE, "cap04", "img")
os.makedirs(img_dir, exist_ok=True)

doc = fitz.open(pdf_path)
zoom = 3.0
mat = fitz.Matrix(zoom, zoom)

# label -> (slug, altezza_clip_pt)
fig_specs = {
    "C4.1.1":  ("ridistribuzione-travi-continue", 180),
    "C4.1.2":  ("momenti-nodo-discordi", 220),
    "C4.1.3":  ("momenti-nodo-concordi", 190),
    "C4.1.4":  ("ridistribuzione-travi-opposto", 170),
    "C4.1.5":  ("ridistribuzione-travi-concorde", 150),
    "C4.1.6":  ("diagrammi-momenti-ridistribuzione", 210),
    "C4.1.7":  ("pressione-laterale-confinamento", 320),
    "C4.1.8":  ("volume-confinato-staffe", 210),
    "C4.1.9":  ("sigma-epsilon-cls-confinato", 360),
    "C4.1.11": ("ampiezza-fessure", 210),
    "C4.1.12": ("momento-curvatura-duttilita", 210),
    "C4.1.13": ("sigma-epsilon-cls-leggero", 150),
}

def find_caption(label):
    patterns = [
        f"Figura {label} -",
        f"Figura {label}-",
        f"Figura {label} \u2013",
        f"Figura {label}\u2013",
        f"Figura {label} ",
    ]
    for p in range(len(doc)):
        page = doc[p]
        for pat in patterns:
            areas = page.search_for(pat)
            if areas:
                return p, areas[0]
    return None

# Figure "normali"
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
    print(f"SAVED: {fname}  (page {page_idx+1}, clip y {y_top:.0f}-{rect.y1:.0f})")

# Figura C4.1.10: combina sub-figure a/b (pag 87 fondo) + sub-figura c + didascalia (pag 88 inizio)
label = "C4.1.10"
slug = "area-tesa-efficace"
res = find_caption(label)
if res:
    didasc_page_idx, rect_didasc = res
    # Parte 1: fondo pag 87 (indice didasc-1): sub-figure a) e b)
    # Cerco nella pagina didasc-1 il punto in cui inizia il contenuto di Fig. 4.1.10
    # Uso come riferimento la label "Legenda" o prendo una fascia dal basso
    page_prev = doc[didasc_page_idx - 1]
    prev_rect = page_prev.rect
    # clip fondo pag: ultimi ~280 pt
    clip1 = fitz.Rect(prev_rect.x0 + 30, prev_rect.y1 - 300, prev_rect.x1 - 30, prev_rect.y1 - 50)
    pix1 = page_prev.get_pixmap(matrix=mat, clip=clip1)
    img1 = Image.open(BytesIO(pix1.tobytes("png")))

    # Parte 2: inizio pag 88 fino a didascalia
    page_cur = doc[didasc_page_idx]
    cur_rect = page_cur.rect
    clip2 = fitz.Rect(cur_rect.x0 + 30, cur_rect.y0 + 30, cur_rect.x1 - 30, rect_didasc.y1 + 8)
    pix2 = page_cur.get_pixmap(matrix=mat, clip=clip2)
    img2 = Image.open(BytesIO(pix2.tobytes("png")))

    # Concatena verticalmente
    W = max(img1.width, img2.width)
    H = img1.height + img2.height + 10
    combined = Image.new("RGB", (W, H), "white")
    combined.paste(img1, ((W - img1.width) // 2, 0))
    combined.paste(img2, ((W - img2.width) // 2, img1.height + 10))
    fname = f"fig-{label.lower()}-{slug}.png"
    combined.save(os.path.join(img_dir, fname))
    print(f"SAVED (combined): {fname}  (pp. {didasc_page_idx}-{didasc_page_idx+1})")

doc.close()
print("Done.")
