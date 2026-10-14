#!/usr/bin/env python3
"""Costruisce la sorgente del sito MkDocs in `_sito/` a partire da `cap*/` e dal registro.

I file di `cap*/` non si modificano mai: le VC misurano la loro impronta SHA-256.
Lo script li copia in `_sito/docs/` e soltanto nella copia:

- aggiunge in testa a ogni pagina il riquadro con lo stato di verifica letto dal
  registro tramite `apri_md` («stato non registrato» se la pagina non c'è);
- fa puntare i rimandi a `../indice-ntc2018.md` alla pagina generata con quel nome;
- trasforma i collegamenti a file del repository fuori dai capitoli (per esempio i
  verbali in `verifica-conformita/`) in collegamenti al file su GitHub, e lascia come
  testo semplice quelli a cartelle escluse dal repository (`_tmp_render/`);
- sostituisce le figure che mancano nel repository con un avviso testuale;
- porta a capo il rimando alla nota scritto dopo i `$$` di chiusura di una formula,
  che altrimenti uscirebbe in linea fra due «$».

Genera inoltre la pagina iniziale dal registro, `mkdocs.yml` con la navigazione e
`rapporto-costruzione.json` con i conteggi usati dai controlli.

Uso: python strumenti/costruisci-sito.py  ->  poi  mkdocs build --strict -f _sito/mkdocs.yml
"""
from __future__ import annotations

import csv
import html
import json
import re
import shutil
import sys
from collections import Counter, defaultdict
from pathlib import Path
from urllib.parse import quote, unquote

RADICE = Path(__file__).resolve().parent.parent
SITO = RADICE / "_sito"
DOCS = SITO / "docs"
RISORSE = RADICE / "strumenti" / "sito"
REGISTRO = RADICE / "registro-verifica-conformita-ntc2018.csv"

REPO_URL = "https://github.com/sinmar123/ntc2018-markdown"
SEGNALA_URL = REPO_URL + "/issues/new?template=errore-di-trascrizione.yml"

RE_CAPITOLO = re.compile(r"^cap\d\d$")
RE_IMMAGINE = re.compile(r'!\[([^\]]*)\]\(([^)\s]+)(\s+"[^"]*")?\)')
RE_LINK = re.compile(r'(?<!!)\[([^\]]*)\]\(([^)\s]+)(\s+"[^"]*")?\)')
# Formula display seguita, sulla stessa riga, dal rimando a una nota redazionale:
# arithmatex la leggerebbe come formula in linea fra due «$». Nella copia la nota va a capo.
RE_FORMULA_NOTA = re.compile(r'(?m)^(\$\$[^$\n]+\$\$)[ \t]+(\[\[?\d+\]?\]\([^)\s]+\))[ \t]*(\r?)$')

MESI = ["gennaio", "febbraio", "marzo", "aprile", "maggio", "giugno", "luglio",
        "agosto", "settembre", "ottobre", "novembre", "dicembre"]

# stato_vc -> (classe dell'admonition, etichetta breve per le tabelle)
STATI = {
    "VC-OK": ("success", "Verificato"),
    "DA-RICONFERMARE": ("warning", "Da riconfermare"),
    "DA-RIFARE": ("danger", "Da rifare"),
    "IN-CORSO": ("info", "In corso"),
    "MAI-FATTA": ("warning", "Non ancora verificato"),
}
NON_REGISTRATO = "NON-REGISTRATO"
ORDINE_STATI = ["VC-OK", "DA-RICONFERMARE", "DA-RIFARE", "IN-CORSO", "MAI-FATTA"]

AVVERTENZA = "Fa fede soltanto il testo pubblicato in Gazzetta Ufficiale."


def data_italiana(iso: str) -> str:
    m = re.fullmatch(r"(\d{4})-(\d{2})-(\d{2})", iso.strip())
    if not m:
        return iso.strip()
    anno, mese, giorno = m.groups()
    return f"{int(giorno)} {MESI[int(mese) - 1]} {anno}"


def chiave_naturale(testo: str):
    return [int(p) if p.isdigit() else p.lower() for p in re.split(r"(\d+)", testo)]


def leggi_registro() -> list[dict]:
    with REGISTRO.open(encoding="utf-8-sig", newline="") as f:
        righe = list(csv.DictReader(f, delimiter=";"))
    for r in righe:
        if r["stato_vc"] not in STATI:
            sys.exit(f"stato_vc sconosciuto per {r['paragrafo']}: {r['stato_vc']!r}")
        if not (RADICE / r["apri_md"]).is_file():
            sys.exit(f"apri_md inesistente per {r['paragrafo']}: {r['apri_md']}")
    doppi = [k for k, v in Counter(r["apri_md"] for r in righe).items() if v > 1]
    if doppi:
        sys.exit(f"apri_md ripetuti nel registro: {doppi}")
    return sorted(righe, key=lambda r: int(r["n."]))


def riquadro(riga: dict | None) -> str:
    if riga is None:
        return (
            '!!! note stato-vc stato-vc-non-registrato "Stato non registrato"\n\n'
            "    Questa pagina non compare nel registro delle verifiche: è un indice, una raccolta "
            "o una nota di lavoro. Il testo normativo che contiene non è garantito. "
            f"{AVVERTENZA}\n\n"
            f"    [Segnala un errore di trascrizione]({SEGNALA_URL})\n\n"
        )
    stato = riga["stato_vc"]
    classe, _ = STATI[stato]
    data = data_italiana(riga["data_ultima_vc"]) if riga["data_ultima_vc"].strip() else ""
    if stato == "VC-OK":
        titolo = f"Verificato il {data}" if data else "Verificato"
        testo = ("Il testo di questa pagina è stato confrontato con la Gazzetta Ufficiale "
                 "secondo la procedura di verifica del progetto.")
    elif stato == "DA-RICONFERMARE":
        titolo = "Da riconfermare"
        testo = ("Il testo aveva superato la verifica su una versione precedente dei file"
                 + (f" (ultima verifica: {data})" if data else "")
                 + ". Dopo la riorganizzazione dei file la verifica va riconfermata. "
                 "Può contenere errori di trascrizione.")
    elif stato == "DA-RIFARE":
        titolo = "Verifica da rifare"
        testo = ("La verifica di questa pagina è stata sospesa, è scaduta o si è chiusa "
                 "con rilievi, e va rifatta. Può contenere errori di trascrizione.")
    elif stato == "IN-CORSO":
        titolo = "Verifica in corso"
        testo = ("La verifica di questa pagina è in corso e non è conclusa. "
                 "Può contenere errori di trascrizione.")
    else:
        titolo = "Non ancora verificato"
        testo = ("Il testo è stato convertito con strumenti di intelligenza artificiale "
                 "e non è ancora stato confrontato con la Gazzetta Ufficiale. "
                 "Può contenere errori di trascrizione.")
    slug = stato.lower()
    segnala = SEGNALA_URL + "&paragrafo=" + quote(riga["paragrafo"])
    return (
        f'!!! {classe} stato-vc stato-vc-{slug} "{titolo}"\n\n'
        f"    {testo} {AVVERTENZA}\n\n"
        f"    [Segnala un errore di trascrizione]({segnala})\n\n"
    )


def separa_front_matter(testo: str) -> tuple[str, str]:
    if testo.startswith("---\n") or testo.startswith("---\r\n"):
        m = re.match(r"---\r?\n.*?\r?\n---\r?\n", testo, re.S)
        if m:
            return testo[: m.end()], testo[m.end():]
    return "", testo


def relativo_alla_radice(pagina: Path, destinazione: str) -> Path:
    """Percorso del bersaglio rispetto alla radice del repository, normalizzato."""
    base = pagina.parent.relative_to(DOCS)
    parti: list[str] = []
    for p in (base / unquote(destinazione)).parts:
        if p == "..":
            if parti:
                parti.pop()
            else:
                parti.append("..")
        elif p != ".":
            parti.append(p)
    return Path(*parti) if parti else Path(".")


def trasforma(pagina: Path, testo: str, rapporto: dict) -> str:
    rel_pagina = str(pagina.relative_to(DOCS))

    def immagine(m: re.Match) -> str:
        alt, dest = m.group(1), m.group(2)
        if re.match(r"[a-z]+:", dest):
            return m.group(0)
        bersaglio = relativo_alla_radice(pagina, dest.split("#")[0])
        if (RADICE / bersaglio).is_file():
            return m.group(0)
        rapporto["figure_mancanti"].append({"pagina": rel_pagina, "figura": dest,
                                            "file": bersaglio.as_posix()})
        return ('<span class="figura-mancante">Figura non presente nel repository '
                f"(<code>{html.escape(dest)}</code>): {html.escape(alt)}. "
                "Si consulti la Gazzetta Ufficiale.</span>")

    def collegamento(m: re.Match) -> str:
        etichetta, dest, titolo = m.group(1), m.group(2), m.group(3) or ""
        if re.match(r"[a-z]+:", dest) or dest.startswith("#"):
            return m.group(0)
        percorso, _, ancora = dest.partition("#")
        bersaglio = relativo_alla_radice(pagina, percorso)
        if bersaglio.parts and RE_CAPITOLO.match(bersaglio.parts[0]) \
                and not (RADICE / bersaglio).is_dir() and not percorso.endswith("/"):
            return m.group(0)
        if str(bersaglio) == "indice-ntc2018.md":
            return m.group(0)  # la pagina con questo nome la genera lo script
        if (RADICE / bersaglio).exists() and bersaglio.parts[0] != "..":
            tipo = "tree/main/" if (RADICE / bersaglio).is_dir() else "blob/main/"
            url = REPO_URL + "/" + tipo + quote(bersaglio.as_posix()) + (f"#{ancora}" if ancora else "")
            rapporto["collegamenti_github"].append({"pagina": rel_pagina, "bersaglio": dest})
            return f"[{etichetta}]({url}{titolo})"
        rapporto["collegamenti_tolti"].append({"pagina": rel_pagina, "bersaglio": dest})
        return etichetta

    testo, n = RE_FORMULA_NOTA.subn(r"\1\3\n\3\n\2\3\n{: .rimando-nota }\3", testo)
    rapporto["formule_con_nota"] += n
    testo = RE_IMMAGINE.sub(immagine, testo)
    return RE_LINK.sub(collegamento, testo)


def titolo_h1(testo: str, ripiego: str) -> str:
    m = re.search(r"^#\s+(.+?)\s*$", testo, re.M)
    if not m:
        return ripiego
    t = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", m.group(1))
    return t.replace("*", "").strip() or ripiego


def cella(testo: str) -> str:
    return testo.replace("|", "\\|").strip()


def pagina_iniziale(righe: list[dict], titoli_cap: dict[str, str]) -> str:
    conteggi = Counter(r["stato_vc"] for r in righe)
    out = [
        "# NTC 2018 e Circolare 2019 in Markdown",
        "",
        "Trascrizione in Markdown delle Norme tecniche per le costruzioni "
        "(D.M. 17 gennaio 2018, G.U. n. 42 del 20 febbraio 2018, S.O. n. 8) e della "
        "Circolare 21 gennaio 2019 n. 7 C.S.LL.PP. (G.U. n. 35 dell'11 febbraio 2019, "
        "S.O. n. 5), paragrafo per paragrafo.",
        "",
        f"!!! warning \"{AVVERTENZA}\"",
        "",
        "    La conversione è stata fatta con strumenti di intelligenza artificiale e la "
        "verifica sulla Gazzetta è in corso. Un paragrafo non verificato può contenere "
        "errori di trascrizione. Ogni pagina riporta in testa il proprio stato. Se una "
        "figura mancasse dal repository, al suo posto c'è un avviso.",
        "",
        f"    [Segnala un errore di trascrizione]({SEGNALA_URL})",
        "",
        "## Stato delle verifiche",
        "",
        f"Paragrafi nel registro: **{len(righe)}**.",
        "",
        "| Stato | Significato | Paragrafi |",
        "|---|---|--:|",
    ]
    significati = {
        "VC-OK": "confrontato con la Gazzetta Ufficiale, verifica conclusa",
        "DA-RICONFERMARE": "verificato su una versione precedente dei file, da riconfermare",
        "DA-RIFARE": "verifica sospesa, scaduta o chiusa con rilievi, da rifare",
        "IN-CORSO": "verifica aperta, non conclusa",
        "MAI-FATTA": "convertito, non ancora confrontato con la Gazzetta",
    }
    for s in ORDINE_STATI:
        out.append(f"| {STATI[s][1]} | {significati[s]} | {conteggi.get(s, 0)} |")
    out += ["", "Le pagine che non compaiono nel registro (indici, raccolte, annotazioni) "
            "portano la dicitura «stato non registrato».", ""]

    per_cap: dict[str, list[dict]] = defaultdict(list)
    for r in righe:
        per_cap[r["apri_md"].split("/")[0]].append(r)
    out += ["## Paragrafi per capitolo", ""]
    for cap in sorted(per_cap):
        out += [f"### {titoli_cap.get(cap, cap)}", "",
                "| Paragrafo | Titolo | Stato | Ultima verifica |", "|---|---|---|---|"]
        for r in per_cap[cap]:
            data = r["data_ultima_vc"].strip()
            out.append(f"| [{cella(r['paragrafo'])}]({r['apri_md']}) | {cella(r['titolo'])} "
                       f"| {STATI[r['stato_vc']][1]} | {data} |")
        out.append("")
    return "\n".join(out)


def etichetta_altra(pagina: Path, titolo: str) -> str:
    """Gli indici di paragrafo hanno lo stesso titolo della raccolta: si distinguono qui."""
    m = re.fullmatch(r"indice-(\d+(?:\.\d+)*)\.md", pagina.name)
    if not m:
        return titolo
    resto = re.sub(r"^\s*" + re.escape(m.group(1)) + r"\.?\s*", "", titolo)
    return f"Indice del § {m.group(1)}" + (f" – {resto}" if resto else "")


def nav_capitolo(cap: str, pagine: list[Path], per_md: dict[str, dict],
                 titoli: dict[str, str]) -> list:
    indice = f"{cap}/indice-{cap}.md"
    registrate = sorted((p for p in pagine if p.as_posix() in per_md),
                        key=lambda p: int(per_md[p.as_posix()]["n."]))
    annotazioni = sorted((p for p in pagine if p.parts[1] == "annotazioni"),
                         key=lambda p: chiave_naturale(p.name))
    altre = sorted((p for p in pagine if p.as_posix() not in per_md
                    and p.parts[1] != "annotazioni" and p.as_posix() != indice),
                   key=lambda p: chiave_naturale(p.name))
    voci: list = []
    if any(p.as_posix() == indice for p in pagine):
        voci.append(indice)
    for p in registrate:
        r = per_md[p.as_posix()]
        voci.append({f"{r['paragrafo']} {r['titolo']}": p.as_posix()})
    if altre:
        voci.append({"Altre pagine": [{etichetta_altra(p, titoli[p.as_posix()]): p.as_posix()}
                                      for p in altre]})
    if annotazioni:
        voci.append({"Annotazioni": [{titoli[p.as_posix()]: p.as_posix()} for p in annotazioni]})
    return voci


def main() -> None:
    import yaml  # dipendenza di mkdocs

    righe = leggi_registro()
    per_md = {r["apri_md"]: r for r in righe}

    if SITO.exists():
        shutil.rmtree(SITO)
    DOCS.mkdir(parents=True)

    capitoli = sorted(p.name for p in RADICE.iterdir() if p.is_dir() and RE_CAPITOLO.match(p.name))
    for cap in capitoli:
        shutil.copytree(RADICE / cap, DOCS / cap)

    rapporto: dict = {"pagine_capitoli": 0, "riquadri": Counter(), "figure_mancanti": [],
                      "collegamenti_github": [], "collegamenti_tolti": [], "formule_con_nota": 0}
    titoli: dict[str, str] = {}
    pagine_per_cap: dict[str, list[Path]] = defaultdict(list)
    for pagina in sorted(DOCS.rglob("*.md")):
        rel = pagina.relative_to(DOCS)
        testo = pagina.read_text(encoding="utf-8-sig")
        front, corpo = separa_front_matter(testo)
        riga = per_md.get(rel.as_posix())
        rapporto["riquadri"][riga["stato_vc"] if riga else NON_REGISTRATO] += 1
        rapporto["pagine_capitoli"] += 1
        titoli[rel.as_posix()] = titolo_h1(corpo, pagina.stem)
        corpo = trasforma(pagina, corpo, rapporto)
        pagina.write_text(front + riquadro(riga) + corpo.lstrip("\n"), encoding="utf-8")
        pagine_per_cap[rel.parts[0]].append(rel)

    mancanti = [r["apri_md"] for r in righe if not (DOCS / r["apri_md"]).is_file()]
    if mancanti:
        sys.exit(f"pagine del registro non copiate: {mancanti}")

    titoli_cap = {cap: titoli.get(f"{cap}/indice-{cap}.md", cap) for cap in capitoli}
    (DOCS / "index.md").write_text(pagina_iniziale(righe, titoli_cap), encoding="utf-8")
    (DOCS / "indice-ntc2018.md").write_text(
        "# Indice generale\n\nL'indice generale, con lo stato di verifica di ogni paragrafo, "
        "è nella [pagina iniziale](index.md).\n", encoding="utf-8")

    for nome, dest in [("stile.css", "stylesheets"), ("mathjax.js", "javascripts")]:
        (DOCS / dest).mkdir(exist_ok=True)
        shutil.copy2(RISORSE / nome, DOCS / dest / nome)

    nav: list = [{"Pagina iniziale": "index.md"}]
    for cap in capitoli:
        nav.append({titoli_cap[cap]: nav_capitolo(cap, pagine_per_cap[cap], per_md, titoli)})
    config = (RISORSE / "mkdocs.yml").read_text(encoding="utf-8")
    config += "\n" + yaml.safe_dump({"nav": nav}, allow_unicode=True, sort_keys=False, width=1000)
    (SITO / "mkdocs.yml").write_text(config, encoding="utf-8")

    rapporto["riquadri"] = dict(rapporto["riquadri"])
    rapporto["registro"] = dict(Counter(r["stato_vc"] for r in righe))
    (SITO / "rapporto-costruzione.json").write_text(
        json.dumps(rapporto, ensure_ascii=False, indent=1), encoding="utf-8")

    print(f"pagine dei capitoli copiate: {rapporto['pagine_capitoli']}")
    print(f"riquadri per stato: {rapporto['riquadri']}")
    print(f"registro per stato: {rapporto['registro']}")
    print(f"figure mancanti sostituite da avviso: {len(rapporto['figure_mancanti'])} riferimenti, "
          f"{len({f['file'] for f in rapporto['figure_mancanti']})} file distinti")
    print(f"collegamenti portati su GitHub: {len(rapporto['collegamenti_github'])}")
    print(f"collegamenti tolti (bersaglio escluso dal repository): {len(rapporto['collegamenti_tolti'])}")
    print(f"formule display con rimando a nota portato a capo: {rapporto['formule_con_nota']}")


if __name__ == "__main__":
    main()
