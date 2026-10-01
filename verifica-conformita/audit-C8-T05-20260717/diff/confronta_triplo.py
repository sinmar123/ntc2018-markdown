# -*- coding: utf-8 -*-
"""Confronto triplo A / B / Markdown per la Tabella C8.7.6.3.II (lotto C8-T05).
Sola lettura sul markdown vivo: estrae la tabella, confronta con le trascrizioni
indipendenti A (Opus) e B (Sonnet). Emette confronto-triplo.csv e stampa il verdetto.
"""
import csv, re, sys, unicodedata

BASE = "verifica-conformita/audit-C8-T05-20260717"
MD = "cap08/8-esistenti.md"

def norm(s):
    if s is None:
        return ""
    s = s.strip()
    # apostrofi e virgolette tipografiche -> ASCII (normalizzazioni NORM documentate)
    s = s.replace("’", "'").replace("‘", "'")
    s = s.replace("“", '"').replace("”", '"')
    s = s.replace("VUOTA", "")
    s = re.sub(r"\s+", " ", s).strip()
    return s

def parse_ab(path):
    cells = {}
    cap = None
    heads = []
    with open(path, encoding="utf-8") as f:
        for line in f:
            m = re.match(r"^R(\d)\s*\|\s*C(\d)\s*\|\s*(.*)$", line.strip())
            if m:
                cells[(int(m.group(1)), int(m.group(2)))] = norm(m.group(3))
                continue
            mh = re.match(r"^\d\)\s*(.*)$", line.strip())
            if mh:
                heads.append(norm(mh.group(1)))
                continue
            if line.strip().startswith("Tabella C8.7.6.3.II"):
                cap = norm(line)
    return cap, heads, cells

def parse_md():
    with open(MD, encoding="utf-8") as f:
        lines = f.readlines()
    cap = None
    tbl = []
    for i, ln in enumerate(lines):
        if re.match(r"^\*\*Tabella C8\.7\.6\.3\.II", ln.strip()):
            cap = norm(ln.replace("**", ""))
            # la tabella markdown segue: header, separatore, 5 righe dati
            j = i + 1
            while j < len(lines) and not lines[j].lstrip().startswith("|"):
                j += 1
            # raccogli righe che iniziano con |
            while j < len(lines) and lines[j].lstrip().startswith("|"):
                tbl.append(lines[j])
                j += 1
            break
    def split_row(r):
        parts = [p for p in r.strip().strip("|").split("|")]
        return [norm(p) for p in parts]
    header = split_row(tbl[0])            # 7 intestazioni
    data = [split_row(r) for r in tbl[2:]]  # salta separatore
    heads = header                         # 7 -> C? mapping: idx0=Criterio, idx1..6 = C1..C6
    cells = {}
    for ri, row in enumerate(data, start=1):
        for ci in range(1, 7):
            cells[(ri, ci)] = row[ci] if ci < len(row) else ""
    return cap, heads, cells

capA, headA, cellsA = parse_ab(BASE + "/passaggio-a/trascrizione-tabII.md")
capB, headB, cellsB = parse_ab(BASE + "/passaggio-b/trascrizione-tabII.md")
capM, headM, cellsM = parse_md()

rows = []
diff_ab = diff_md = 0

# didascalia (confronto SENZA punto finale per isolare il refuso di punteggiatura)
def strip_dot(s):
    return s.rstrip(".").strip()
cap_ab = "IDENTICA" if norm(capA) == norm(capB) else "DIVERSA"
cap_md_raw = "IDENTICA" if norm(capA) == norm(capM) else "DIVERSA"
cap_md_nodot = "IDENTICA" if strip_dot(norm(capA)) == strip_dot(norm(capM)) else "DIVERSA"
rows.append(["DIDASCALIA", "", capA, capB, capM, cap_ab,
             cap_md_raw + (" (identica senza punto finale)" if cap_md_raw == "DIVERSA" and cap_md_nodot == "IDENTICA" else "")])
if cap_ab != "IDENTICA":
    diff_ab += 1
if cap_md_raw != "IDENTICA":
    diff_md += 1

# intestazioni (7)
for idx in range(7):
    a = headA[idx] if idx < len(headA) else ""
    b = headB[idx] if idx < len(headB) else ""
    m = headM[idx] if idx < len(headM) else ""
    e_ab = "IDENTICA" if a == b else "DIVERSA"
    e_md = "IDENTICA" if a == m else "DIVERSA"
    rows.append([f"HEADER", f"col{idx+1}", a, b, m, e_ab, e_md])
    if e_ab != "IDENTICA":
        diff_ab += 1
    if e_md != "IDENTICA":
        diff_md += 1

# 30 celle dati
for ri in range(1, 6):
    for ci in range(1, 7):
        a = cellsA.get((ri, ci), "")
        b = cellsB.get((ri, ci), "")
        m = cellsM.get((ri, ci), "")
        e_ab = "IDENTICA" if a == b else "DIVERSA"
        e_md = "IDENTICA" if a == m else "DIVERSA"
        rows.append([f"R{ri}", f"C{ci}", a, b, m, e_ab, e_md])
        if e_ab != "IDENTICA":
            diff_ab += 1
        if e_md != "IDENTICA":
            diff_md += 1

with open(BASE + "/diff/confronto-triplo.csv", "w", encoding="utf-8", newline="") as f:
    w = csv.writer(f, delimiter=";")
    w.writerow(["riga", "campo", "valore_A", "valore_B", "valore_MD", "esito_A_vs_B", "esito_A_vs_MD"])
    w.writerows(rows)

tot = len(rows)
print(f"Confrontate {tot} posizioni logiche (1 didascalia + 7 header + 30 celle).")
print(f"A vs B  : {tot - diff_ab}/{tot} IDENTICHE, {diff_ab} diverse.")
print(f"A vs MD : {tot - diff_md}/{tot} IDENTICHE, {diff_md} diverse.")
if diff_md:
    print("\n--- Difformita' A vs MD ---")
    for r in rows:
        if r[6] != "IDENTICA":
            print(f"[{r[0]} {r[1]}] A={r[2][:60]!r}  MD={r[4][:60]!r}  -> {r[6]}")
