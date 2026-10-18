"""Rende in PDF un file normativo del corpus, con la resa dei tag della Gazzetta.

Motivo di esistere: la convenzione LaTeX `\tag{4.1.36}` stampa `(4.1.36)` con le
parentesi tonde, mentre la Gazzetta stampa `[4.1.36]` con le quadre. La difformita'
non e' nel Markdown ma nel documento reso, e riguarda tutti i capitoli. Si corregge
ridefinendo una macro, non riscrivendo le formule.

Chiunque produca un render del corpus deve usare questo script: un render fatto a
mano con pandoc reintroduce la difformita' e nessun verificatore se ne accorge,
perche' i verificatori leggono il sorgente. Vedi
`skills/conversione-normativa/references/ciclo-conversione-verifica.md` § 5.

Uso:
    python strumenti/render-capitolo.py cap04/4.1-calcestruzzo.md [destinazione.pdf]
"""
import subprocess
import sys
import re
import tempfile
from pathlib import Path

PROGETTO = Path(__file__).resolve().parent.parent

# Ridefinisce il formato dei tag di formula: [4.1.36] invece di (4.1.36).
PREAMBOLO = r"""
\usepackage{newunicodechar}
\usepackage{graphicx}
\newunicodechar{ξ}{\ensuremath{\xi}}
\newunicodechar{η}{\ensuremath{\eta}}
\newunicodechar{Θ}{\ensuremath{\Theta}}
\newunicodechar{α}{\ensuremath{\alpha}}
\newunicodechar{φ}{\ensuremath{\varphi}}
\newunicodechar{≤}{\ensuremath{\leq}}
\newunicodechar{≥}{\ensuremath{\geq}}
\newunicodechar{⁵}{\textsuperscript{5}}
\newunicodechar{⁶}{\textsuperscript{6}}
\newunicodechar{⁷}{\textsuperscript{7}}
\newunicodechar{⁻}{\textsuperscript{\ensuremath{-}}}
\makeatletter
\renewcommand{\tagform@}[1]{\maketag@@@{[#1]}}
\makeatother
"""


def rendi(sorgente: Path, destinazione: Path) -> None:
    preambolo = destinazione.parent / "_preambolo-tag.tex"
    preambolo.write_text(PREAMBOLO, encoding="utf-8")
    testo = sorgente.read_text(encoding="utf-8")
    testo_render = re.sub(
        r'(?m)^(<a id="toc-ntc2018-[^"]+"></a>)\r?\n(?=#{1,6} )',
        r"\1\n\n",
        testo,
    )
    # Rinvii alle note redazionali e block ID sono apparati del Markdown:
    # restano nel file interrogabile, ma non appartengono al testo della fonte
    # e non devono comparire nel render usato per il controllo visivo.
    testo_render = re.sub(
        r"\s+\[\d+\]\(\./annotazioni/[^)]+\)",
        "",
        testo_render,
    )
    testo_render = re.sub(r"(?m)\s+\^[A-Za-z0-9_-]+\s*$", "", testo_render)

    # Una tabella a pipe può seguire subito la propria didascalia nel Markdown
    # interrogabile. Pandoc richiede una riga vuota per riconoscerla in modo
    # affidabile: la inseriamo soltanto nella copia temporanea di render.
    testo_render = re.sub(
        r"(?m)^([^\r\n|][^\r\n]*)\r?\n(?=\|[^\r\n]*\|\s*$)",
        r"\1\n\n",
        testo_render,
    )

    # Le immagini autonome restano apparati senza didascalia automatica, ma
    # vengono rese in un blocco LaTeX esplicito. Con alcune PNG panoramiche
    # `\pandocbounded` può conservare la posizione orizzontale corrente e far
    # uscire parte del raster dal margine destro. Il blocco centrato limita
    # invece entrambe le dimensioni, senza ritagliare né alterare il file.
    def immagine_limitata(match: re.Match[str]) -> str:
        percorso = (sorgente.parent / match.group("path")).resolve().as_posix()
        return (
            "\\begin{center}\n"
            "\\includegraphics[width=\\linewidth,height=0.75\\textheight,keepaspectratio]"
            f"{{{percorso}}}\n"
            "\\end{center}"
        )

    testo_render = re.sub(
        r"(?m)^!\[[^\]]*\]\((?P<path>[^)]+\.png)\)\s*$",
        immagine_limitata,
        testo_render,
    )
    # Note a piè di pagina Markdown `[^n]` (catalogo, voce 25): LaTeX numera le
    # note da 1, mentre la fonte stampa il proprio numero (per esempio 4 nel
    # § C8.7.1.3.2). Nella sola copia di render si allinea il contatore al numero
    # dell'etichetta, così il PDF canonico stampa lo stesso apice della Gazzetta.
    testo_render = re.sub(
        r"\[\^(\d+)\](?!:)",
        lambda m: f"\\setcounter{{footnote}}{{{int(m.group(1)) - 1}}}[^{m.group(1)}]",
        testo_render,
    )
    sorgente_render = sorgente
    temporaneo = None
    if testo_render != testo:
        with tempfile.NamedTemporaryFile(
            mode="w",
            suffix=".md",
            prefix="_sorgente-render-",
            dir=destinazione.parent,
            delete=False,
            encoding="utf-8",
        ) as tmp:
            tmp.write(testo_render)
            temporaneo = Path(tmp.name)
            sorgente_render = temporaneo
    comando = [
        "pandoc",
        # Disabilita implicit_figures: altrimenti ogni ![alt](img) diventa
        # una Figure con didascalia automatica, duplicando le didascalie
        # esplicite e chiamando Figure anche le tabelle raster (ERR-AUDIT).
        "-f",
        "markdown-implicit_figures",
        str(sorgente_render),
        "-o",
        str(destinazione),
        "--pdf-engine=xelatex",
        "--include-in-header",
        str(preambolo),
        "-V",
        "geometry:margin=2cm",
        # Le rubriche di livello 4 e 5 (\paragraph e \subparagraph) sono
        # «run-in» nella classe article: senza questa variabile il capoverso
        # seguente parte sulla stessa riga della rubrica, mentre la Gazzetta le
        # stampa su riga propria. Decisione di Sandro del 2026-10-18 (G6 § 8.7.1).
        "-V",
        "block-headings",
        "--resource-path",
        str(sorgente.parent),
    ]
    try:
        esito = subprocess.run(
            comando,
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",
            cwd=PROGETTO,
        )
    finally:
        preambolo.unlink(missing_ok=True)
        if temporaneo is not None:
            temporaneo.unlink(missing_ok=True)
    if esito.returncode != 0:
        sys.exit(f"render fallito:\n{esito.stderr[-2000:]}")
    print(f"reso: {destinazione}")


def _testo_pdf(pdf: Path) -> str:
    """Estrae il testo del PDF (PyMuPDF se disponibile, altrimenti pdftotext)."""
    try:
        import fitz

        doc = fitz.open(pdf)
        testo = "".join(p.get_text() for p in doc)
        doc.close()
        return testo
    except ImportError:
        esito = subprocess.run(
            ["pdftotext", "-layout", str(pdf), "-"],
            capture_output=True,
            text=True,
            check=False,
        )
        if esito.returncode != 0:
            sys.exit(f"estrazione testo PDF fallita:\n{esito.stderr[-1000:]}")
        return esito.stdout


def verifica_tag(pdf: Path) -> None:
    """Controllo bloccante: i tag devono uscire con le parentesi quadre."""
    import re

    testo = _testo_pdf(pdf)
    tonde = re.findall(r"\((?:C?\d+\.\d+\.\d+[a-z.]*)\)", testo)
    if tonde:
        sys.exit(
            f"CONTROLLO FALLITO: {len(tonde)} tag resi con parentesi tonde, "
            f"per esempio {tonde[:3]}. La macro del preambolo non ha avuto effetto."
        )
    print("controllo tag: nessun tag reso con parentesi tonde")


def verifica_didascalie_automatiche(pdf: Path) -> None:
    """Controllo bloccante anti-ERR-AUDIT: niente didascalie Figure N: / Figura N:.

    Con pandoc implicit_figures attivo ogni immagine diventa una Figure con
    didascalia automatica (anche le tabelle raster). Con -f markdown-implicit_figures
    tali didascalie devono essere assenti.
    """
    import re

    testo = _testo_pdf(pdf)
    auto = re.findall(r"(?:Figure|Figura)\s+\d+\s*:", testo)
    if auto:
        sys.exit(
            f"CONTROLLO FALLITO: {len(auto)} didascalie automatiche tipo "
            f"'Figure N:' / 'Figura N:' nel PDF (es. {auto[:5]}). "
            f"Verificare che pandoc sia invocato con -f markdown-implicit_figures."
        )
    print("controllo didascalie: nessuna didascalia automatica Figure/Figura N:")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    src = (PROGETTO / sys.argv[1]).resolve()
    dst = Path(sys.argv[2]).resolve() if len(sys.argv) > 2 else src.with_suffix(".pdf")
    rendi(src, dst)
    verifica_tag(dst)
    verifica_didascalie_automatiche(dst)
