#!/usr/bin/env python3
"""Controlli sul sito generato, dopo costruisci-sito.py e `mkdocs build --strict`.

Esce con codice 1 se:
- le pagine HTML generate dai capitoli non sono tante quante i file .md di `cap*/`;
- i riquadri per stato nell'HTML non coincidono con i conteggi del registro;
- una pagina HTML ha un'immagine che non trova il suo file nel sito.

Riporta senza bloccare, perché si correggono nei capitoli con la procedura VC:
- le figure citate nei capitoli che mancano nel repository (nel sito c'è un avviso);
- le formule con `\\tag` fuori dai `$$` e altri `$` rimasti fuori da arithmatex.

Uso: python strumenti/controlla-sito.py [--dettaglio]
"""
from __future__ import annotations

import csv
import json
import re
import sys
from collections import Counter
from pathlib import Path
from urllib.parse import unquote

RADICE = Path(__file__).resolve().parent.parent
SITO = RADICE / "_sito"
HTML = SITO / "site"
REGISTRO = RADICE / "registro-verifica-conformita-ntc2018.csv"

RE_RIQUADRO = re.compile(r'class="admonition [a-z]+ stato-vc stato-vc-([a-z-]+)"')
RE_ARITHMATEX = re.compile(r'<(span|div) class="arithmatex">.*?</\1>', re.S)
RE_CODICE = re.compile(r"<code>.*?</code>", re.S)
RE_IMG = re.compile(r'<img[^>]*\ssrc="([^"]+)"')


def articolo(html: str) -> str:
    parti = html.split("<article", 1)
    return parti[1].split("</article>", 1)[0] if len(parti) == 2 else ""


def main() -> int:
    dettaglio = "--dettaglio" in sys.argv
    errori: list[str] = []

    sorgenti = sorted(p.relative_to(RADICE) for p in RADICE.glob("cap*/**/*.md")
                      if re.match(r"cap\d\d$", p.relative_to(RADICE).parts[0]))
    # MkDocs pubblica README.md e index.md come pagina indice della loro cartella
    pagine = {s: HTML / (s.parent if s.stem.lower() in ("readme", "index") else s.with_suffix(""))
              / "index.html" for s in sorgenti}
    assenti = [str(s) for s, h in pagine.items() if not h.is_file()]
    generate = len(sorgenti) - len(assenti)
    print(f"[pagine] file .md in cap*/: {len(sorgenti)}; pagine HTML generate: {generate}")
    if assenti:
        errori.append(f"pagine non generate: {assenti[:10]}")

    with REGISTRO.open(encoding="utf-8-sig", newline="") as f:
        registro = Counter(r["stato_vc"].lower() for r in csv.DictReader(f, delimiter=";"))
    riquadri: Counter = Counter()
    pagine_con_formule = blocchi = 0
    tag_fuori: list[str] = []
    altri_dollari: list[str] = []
    img_rotte: list[str] = []
    for sorgente, html_path in pagine.items():
        if not html_path.is_file():
            continue
        art = articolo(html_path.read_text(encoding="utf-8"))
        trovati = RE_RIQUADRO.findall(art)
        if len(trovati) != 1:
            errori.append(f"{sorgente}: {len(trovati)} riquadri di stato invece di 1")
        riquadri.update(trovati)
        n = len(RE_ARITHMATEX.findall(art))
        blocchi += n
        pagine_con_formule += bool(n)
        resto = RE_CODICE.sub("", RE_ARITHMATEX.sub("", art))
        for m in re.finditer(r"[^\n]{0,50}\$[^\n]{0,50}", resto):
            (tag_fuori if re.search(r"\$\s*\\tag\{", m.group(0)) else altri_dollari).append(
                f"{sorgente}: {m.group(0).strip()}")
        for src in RE_IMG.findall(art):
            if re.match(r"[a-z]+:", src):
                continue
            if not (html_path.parent / unquote(src)).resolve().is_file():
                img_rotte.append(f"{sorgente}: {src}")

    attesi = dict(registro)
    attesi["non-registrato"] = len(sorgenti) - sum(registro.values())
    print(f"[riquadri] nell'HTML: {dict(riquadri)}")
    print(f"[riquadri] attesi dal registro: {attesi}")
    if dict(riquadri) != {k: v for k, v in attesi.items() if v}:
        errori.append("i riquadri per stato non coincidono con il registro")

    print(f"[immagini] <img> del sito senza file: {len(img_rotte)}")
    errori += [f"immagine rotta: {x}" for x in img_rotte]

    rapporto_path = SITO / "rapporto-costruzione.json"
    if rapporto_path.is_file():
        rapporto = json.loads(rapporto_path.read_text(encoding="utf-8"))
        mancanti = rapporto["figure_mancanti"]
        print(f"[figure] riferimenti a figure assenti dal repository: {len(mancanti)} "
              f"({len({m['file'] for m in mancanti})} file distinti), nel sito sostituiti da avviso")
        if dettaglio:
            for f in sorted({m["file"] for m in mancanti}):
                print(f"    {f}")

    print(f"[formule] pagine con formule: {pagine_con_formule}; blocchi arithmatex: {blocchi}")
    print(f"[formule] \\tag fuori dai $$ (difetto nei capitoli): {len(tag_fuori)}")
    print(f"[formule] altri $ fuori da arithmatex e dal codice: {len(altri_dollari)}")
    if dettaglio:
        for x in tag_fuori + altri_dollari:
            print(f"    {x}")

    for e in errori:
        print(f"ERRORE: {e}")
    print("esito:", "ERRORI" if errori else "OK")
    return 1 if errori else 0


if __name__ == "__main__":
    sys.exit(main())
