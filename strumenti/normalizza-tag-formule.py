#!/usr/bin/env python3
"""Porta dentro il blocco matematico i tag scritti dopo i `$$` di chiusura.

`$$X$$ \\tag{n}` diventa `$$X \\tag{n}$$`, anche quando la riga chiude un
blocco su più righe (`\\end{cases}$$ \\tag{n}`). Pandoc e MathJax non rendono
il tag lasciato fuori. Lo script sposta soltanto i delimitatori: dopo la
sostituzione ogni riga deve contenere gli stessi caratteri, spazi esclusi,
altrimenti si ferma senza scrivere.

Uso: python strumenti/normalizza-tag-formule.py [--applica] [file ...]
Senza --applica elenca le righe da correggere. Senza file esamina cap*/.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

RADICE = Path(__file__).resolve().parent.parent
RE_TAG_FUORI = re.compile(r"^(?P<testa>.*?)\$\$[ \t]+(?P<tag>\\tag\{[^{}]*\})[ \t]*(?P<cr>\r?)$")


def correggi(riga: str) -> str | None:
    m = RE_TAG_FUORI.match(riga)
    if not m or "\\tag" in m["testa"]:
        return None
    return f"{m['testa']} {m['tag']}$${m['cr']}"


def senza_spazi(s: str) -> str:
    return re.sub(r"\s", "", s)


def main() -> int:
    applica = "--applica" in sys.argv
    nomi = [a for a in sys.argv[1:] if a != "--applica"]
    files = [RADICE / n for n in nomi] or sorted(
        p for p in RADICE.glob("cap*/**/*.md") if re.match(r"cap\d\d$", p.relative_to(RADICE).parts[0]))
    totale = 0
    for f in files:
        dati = f.read_bytes()
        righe = dati.decode("utf-8").split("\n")
        modifiche = 0
        for i, riga in enumerate(righe):
            nuova = correggi(riga)
            if nuova is None:
                continue
            if sorted(senza_spazi(nuova)) != sorted(senza_spazi(riga)):
                sys.exit(f"{f.relative_to(RADICE)}:{i + 1}: la sostituzione cambierebbe altri caratteri")
            print(f"{f.relative_to(RADICE)}:{i + 1}: {riga.strip()}  ->  {nuova.strip()}")
            righe[i] = nuova
            modifiche += 1
        if modifiche and applica:
            f.write_bytes("\n".join(righe).encode("utf-8"))
        totale += modifiche
    print(f"righe {'corrette' if applica else 'da correggere'}: {totale}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
