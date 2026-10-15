#!/usr/bin/env python3
"""Candidati di struttura dalla codifica del PDF: capoversi uniti ed enfasi perse nel target.

Legge le righe di testo del PDF nel perimetro (tabelle escluse), ricostruisce i capoversi
dalla interlinea, dal rientro e dalle righe corte, e i tratti in grassetto, corsivo e grassetto
corsivo. Poi li cerca nei Markdown del target e segnala:

- `capoversi`: inizi di capoverso della fonte che nel target stanno a metà di un paragrafo;
- `enfasi`: tratti in enfasi della fonte che nel target non hanno marcatori `*`.

Sono **candidati** per il coordinatore C, non correzioni: ricerche ripetute, righe di
continuazione delle note e simboli matematici danno falsi positivi, che C scarta prima di
scrivere la lista per Sandro (PROCEDURA-VC.md, § 6 e § 8). Lo script non scrive nel corpus.

Uso:
    python strumenti/vc-struttura-fonte.py --pdf FONTE.pdf --pagine 257-269 \\
        --inizio "^C8\\.5" --fine "^C8\\.6" --target cap08/8.5*.md --uscita candidati.json
Opzioni: --senza-tabelle 265 (pagine dove il riconoscimento delle tabelle sbaglia),
--interlinea 4.2 (soglia in punti fra due capoversi).
Richiede PyMuPDF. Nato dagli script della VC del § 8.5, 2026-10-14.
"""
from __future__ import annotations

import argparse
import glob
import json
import re
import sys
from pathlib import Path

import pymupdf as fitz

MARGINE_ALTO, MARGINE_BASSO = 70, 740
NOTA = re.compile(r"^(\(\*+\)|\([a-z]\)|\d+\s*[A-Z])")
RUBRICA = re.compile(r"^(C?\d+(\.\d+)*\.?\s*[A-Z]|Tabella|Figura|Fig\.)")


def stile(font: str) -> str:
    if "Symbol" in font or "Cambria" in font:
        return "simbolo"
    if "BoldIta" in font or "BoldItalic" in font:
        return "grassetto corsivo"
    if "Bold" in font:
        return "grassetto"
    if "Italic" in font:
        return "corsivo"
    return ""


def righe_pdf(pdf: str, pagine: list[int], senza_tabelle: set[int]) -> list[dict]:
    documento = fitz.open(pdf)
    righe = []
    for p in pagine:
        pagina = documento[p - 1]
        tabelle = [] if p in senza_tabelle else [t.bbox for t in pagina.find_tables().tables]
        for blocco in pagina.get_text("dict")["blocks"]:
            for riga in blocco.get("lines", []):
                x0, y0, x1, y1 = riga["bbox"]
                if y0 < MARGINE_ALTO or y0 > MARGINE_BASSO:
                    continue
                if any(t[1] - 2 <= y0 <= t[3] + 2 and t[0] - 2 <= x0 <= t[2] + 2 for t in tabelle):
                    continue
                spans = [(s["text"], stile(s["font"])) for s in riga["spans"] if s["text"]]
                testo = "".join(s[0] for s in spans)
                if testo.strip():
                    righe.append({"p": p, "x0": x0, "x1": x1, "y0": y0, "y1": y1, "t": testo, "spans": spans})
    righe.sort(key=lambda r: (r["p"], round(r["y0"]), r["x0"]))
    return righe


def taglia(righe: list[dict], inizio: str, fine: str) -> list[dict]:
    i = next((k for k, r in enumerate(righe) if re.search(inizio, r["t"])), None)
    if i is None:
        sys.exit(f"Inizio del perimetro non trovato: {inizio}")
    j = next((k for k, r in enumerate(righe) if k > i and re.search(fine, r["t"])), len(righe)) if fine else len(righe)
    return righe[i:j]


def capoversi(righe: list[dict], soglia: float) -> list[dict]:
    margine_destro = max((r["x1"] for r in righe), default=0)
    out, prec = [], None
    for r in righe:
        if prec is None:
            nuovo, criterio = True, "inizio"
        elif abs(r["y0"] - prec["y0"]) < 2 and r["p"] == prec["p"]:
            nuovo, criterio = False, ""
        elif r["p"] != prec["p"]:
            nuovo, criterio = prec["x1"] < margine_destro - 20, "riga corta a fine pagina"
        elif (r["x0"] > prec["x0"] + 8 and r["y0"] - prec["y1"] <= soglia
              and NOTA.match(out[-1]["righe"][0]["t"].strip())):
            nuovo, criterio = False, ""  # riga di continuazione rientrata di una nota
        elif r["x0"] > prec["x0"] + 8 or r["x0"] < prec["x0"] - 8:
            nuovo, criterio = True, "rientro"
        elif r["y0"] - prec["y1"] > soglia:
            nuovo, criterio = True, "interlinea"
        elif prec["x1"] < margine_destro - 40:
            nuovo, criterio = True, "riga precedente corta"
        else:
            nuovo, criterio = False, ""
        if nuovo:
            out.append({"pagina": r["p"], "y_pt": round(r["y0"], 1), "x_pt": round(r["x0"], 1),
                        "criterio": criterio, "righe": [r]})
        else:
            out[-1]["righe"].append(r)
        prec = r
    for c in out:
        c["testo"] = " ".join(x["t"].strip() for x in c["righe"])
        c["spans"] = [s for x in c["righe"] for s in x["spans"]]
    return out


def lettere(testo: str) -> tuple[str, list[int]]:
    chars, pos = [], []
    for i, ch in enumerate(testo):
        if ch.isalnum():
            chars.append(ch.casefold())
            pos.append(i)
    return "".join(chars), pos


def candidati_capoversi(caps: list[dict], target: dict[str, str]) -> list[dict]:
    out, visti = [], set()
    for c in caps:
        chiave = lettere(c["testo"])[0][:40]
        if len(chiave) < 15:
            continue
        for nome, testo in target.items():
            norm, pos = lettere(testo)
            k = norm.find(chiave)
            while k >= 0:
                i = pos[k]
                j = i
                while j > 0 and testo[j - 1] in "*_":
                    j -= 1
                inizio_riga = testo.rfind("\n", 0, j) + 1
                riga = testo[inizio_riga:testo.find("\n", j) if "\n" in testo[j:] else len(testo)]
                prima = testo[inizio_riga:j]
                prima = prima[2:] if prima.startswith("- ") else prima
                prima = re.sub(r"^\(\*+\)\s*|^\([a-z]\)\s*|^\*\*Nota\s*", "", prima)
                iniziale = next(ch for ch in c["testo"] if ch.isalnum())
                if (not riga.startswith(("#", "<", "  ", "- [", "[Torna")) and prima.strip(" *")
                        and testo[i] == iniziale and testo[j - 1] == " " and (nome, j) not in visti):
                    visti.add((nome, j))
                    out.append({"pagina": c["pagina"], "y_pt": c["y_pt"], "criterio": c["criterio"], "file": nome,
                                "riga": testo.count("\n", 0, j) + 1,
                                "contesto": testo[max(0, j - 40):j] + "⏎⏎" + testo[j:j + 40]})
                k = norm.find(chiave, k + 1)
    return out


def candidati_enfasi(caps: list[dict], target: dict[str, str]) -> list[dict]:
    out = []
    for c in caps:
        if RUBRICA.match(c["testo"]):
            continue  # rubriche e didascalie hanno convenzioni proprie (procedura, § 4)
        tratti = []
        for testo, st in c["spans"]:
            if tratti and tratti[-1][1] == st:
                tratti[-1][0] += testo
            else:
                tratti.append([testo, st])
        for testo, st in tratti:
            t = testo.strip()
            if st not in ("grassetto", "corsivo", "grassetto corsivo") or len(lettere(t)[0]) < 2:
                continue
            esiti = []
            for nome, md in target.items():
                for m in re.finditer(re.escape(t), md):
                    intorno = md[max(0, m.start() - 3):m.start()] + md[m.end():m.end() + 3]
                    esiti.append(("*" in intorno, nome, md.count("\n", 0, m.start()) + 1))
            stato = ("non trovato come testo semplice (simbolo o testo diviso)" if not esiti
                     else "presente" if any(e[0] for e in esiti) else "assente")
            if stato != "presente":
                out.append({"pagina": c["pagina"], "y_pt": c["y_pt"], "stile": st, "testo": t, "stato": stato,
                            "occorrenze": [{"file": e[1], "riga": e[2]} for e in esiti]})
    return out


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--pdf", required=True)
    ap.add_argument("--pagine", required=True, help="intervallo fisico, es. 257-269")
    ap.add_argument("--inizio", required=True, help="regex della prima riga del perimetro")
    ap.add_argument("--fine", default="", help="regex della prima riga fuori perimetro")
    ap.add_argument("--target", nargs="+", required=True, help="file o glob Markdown del target")
    ap.add_argument("--senza-tabelle", default="", help="pagine senza riconoscimento delle tabelle, es. 265,266")
    ap.add_argument("--interlinea", type=float, default=4.2)
    ap.add_argument("--uscita", required=True)
    a = ap.parse_args()
    p1, _, p2 = a.pagine.partition("-")
    pagine = list(range(int(p1), int(p2 or p1) + 1))
    senza = {int(x) for x in a.senza_tabelle.split(",") if x}
    files = sorted({f for g in a.target for f in glob.glob(g)})
    if not files:
        sys.exit("Nessun file del target")
    target = {f: Path(f).read_text(encoding="utf-8-sig") for f in files}
    caps = capoversi(taglia(righe_pdf(a.pdf, pagine, senza), a.inizio, a.fine), a.interlinea)
    risultato = {
        "pdf": a.pdf, "pagine": a.pagine, "target": files,
        "nota": "Candidati da vagliare: non sono correzioni approvate.",
        "capoversi_fonte": [{k: c[k] for k in ("pagina", "y_pt", "x_pt", "criterio")} | {"inizio": c["testo"][:80]}
                            for c in caps],
        "capoversi": candidati_capoversi(caps, target),
        "enfasi": candidati_enfasi(caps, target),
    }
    Path(a.uscita).write_text(json.dumps(risultato, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(json.dumps({"capoversi_fonte": len(caps), "candidati_capoversi": len(risultato["capoversi"]),
                      "candidati_enfasi": len(risultato["enfasi"]), "uscita": a.uscita}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    sys.exit(main())
