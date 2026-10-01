"""Prepara un frammento normativo pulito per il pacchetto cieco G6.

Rimuove soltanto gli apparati locali del corpus: collegamenti di ritorno,
indice interno, ancore HTML, contenitori ``Norma``/``Circolare`` e separatore
fra i due atti. Il testo normativo, le tabelle, le formule e le immagini non
vengono riscritti.

Uso:
    python strumenti/prepara-scope-g6.py sorgente.md destinazione.md
"""

import re
import sys
from pathlib import Path


INIZIO = "<!-- INDICE-INTERNO:INIZIO -->"
FINE = "<!-- INDICE-INTERNO:FINE -->"


def depura(testo: str) -> str:
    testo = testo.lstrip("\ufeff")
    testo = re.sub(
        rf"(?s){re.escape(INIZIO)}.*?{re.escape(FINE)}\s*",
        "",
        testo,
    )
    testo = re.sub(r"(?m)^\[Torna (?:all'indice|al sommario)[^\n]*\n?", "", testo)
    testo = re.sub(r"(?m)^\[\[[^\n|]+\|Torna (?:all'indice|al sommario)[^\n]*\]\]\s*\n?", "", testo)
    testo = re.sub(r'(?m)^<a id="toc-ntc2018-[^"]+"></a>\s*$', "", testo)
    testo = re.sub(r"(?m)^## (?:Norma|Circolare)\s*$", "", testo)
    testo = re.sub(r"(?m)^---\s*$", "", testo)
    testo = re.sub(r"\s+\[\d+\]\(\./annotazioni/[^)]+\)", "", testo)
    testo = re.sub(r"\s+\[\[[^\n|]+\|\[\d+\]\]\]", "", testo)
    testo = re.sub(r"(?m)\s+\^[A-Za-z0-9_-]+\s*$", "", testo)
    testo = re.sub(r"\n{3,}", "\n\n", testo)
    return testo.strip() + "\n"


def main() -> None:
    if len(sys.argv) != 3:
        sys.exit(__doc__)
    sorgente = Path(sys.argv[1]).resolve()
    destinazione = Path(sys.argv[2]).resolve()
    destinazione.parent.mkdir(parents=True, exist_ok=True)
    destinazione.write_text(depura(sorgente.read_text(encoding="utf-8")), encoding="utf-8")
    print(f"scope G6 preparato: {destinazione}")


if __name__ == "__main__":
    main()
