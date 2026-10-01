#!/usr/bin/env python3
"""Genera e verifica gli indici interni dei file naturali x.y.z.

Gli indici usano link Markdown nello stesso documento e ancore HTML esplicite.
Il blocco e le ancore hanno marcatori stabili, così l'apparato di navigazione
può essere escluso meccanicamente dai futuri pacchetti di confronto G6.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import re
import shutil
import sys
import unicodedata
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CAPITOLI = tuple(ROOT / f"cap{numero:02d}" for numero in range(1, 13))
REGISTRO = ROOT / "registro-verifica-conformita-ntc2018.csv"
FILE_ANY = re.compile(r"^(c?\d+(?:\.\d+){0,2})-.+\.md$", re.IGNORECASE)
FILE_RE = re.compile(r"^(c?\d+\.\d+\.\d+)-.+\.md$", re.IGNORECASE)
XYZ_ATTESI = 311
HEADING_RE = re.compile(r"^(#{1,6})[ \t]+(.+?)[ \t]*$")
FENCE_RE = re.compile(r"^[ \t]*(```+|~~~+)")
NUMERO_RE = re.compile(r"^\*{0,2}(C?\d+(?:\.\d+)+)\.?\*{0,2}(?:\s|$)", re.IGNORECASE)
INIZIO = "<!-- INDICE-INTERNO:INIZIO -->"
FINE = "<!-- INDICE-INTERNO:FINE -->"
ANCORA_RE = re.compile(r'^<a id="(toc-ntc2018-[a-z0-9-]+)"></a>$')
ANCORA_PRECEDENTE_RE = re.compile(r'^<a id="sec-[a-z0-9-]+"></a>$')
LINK_RE = re.compile(r"^\s*- \[.*\]\(#(toc-ntc2018-[a-z0-9-]+)\)\s*$")


@dataclass(frozen=True)
class Titolo:
    indice_riga: int
    livello: int
    testo: str
    ancora: str
    profondita_indice: int


def file_naturali() -> list[Path]:
    """Usa il registro compatto come elenco canonico dei file attivi.

    Il ripiego sul glob serve solo ad avviare lo strumento prima che il
    registro esista. In esercizio evita che vecchie copie ripristinate dalla
    sincronizzazione rientrino automaticamente negli indici interni.
    """
    if REGISTRO.is_file():
        with REGISTRO.open("r", encoding="utf-8-sig", newline="") as handle:
            reader = csv.DictReader(handle, delimiter=";")
            if reader.fieldnames and "apri_md" in reader.fieldnames:
                files = [ROOT / row["apri_md"] for row in reader if row["apri_md"]]
                invalid = [path for path in files if not FILE_ANY.match(path.name)]
                missing = [path for path in files if not path.is_file()]
                if invalid or missing:
                    raise RuntimeError(
                        f"registro con file non conformi={invalid} o mancanti={missing}"
                    )
                return [path for path in files if FILE_RE.match(path.name)]

    files: list[Path] = []
    for capitolo in CAPITOLI:
        if not capitolo.is_dir():
            continue
        files.extend(
            path for path in sorted(capitolo.glob("*.md")) if FILE_RE.match(path.name)
        )
    return files


def leggi(path: Path) -> tuple[list[str], bool, bool]:
    dati = path.read_bytes()
    bom = dati.startswith(b"\xef\xbb\xbf")
    if bom:
        dati = dati[3:]
    testo = dati.decode("utf-8")
    return testo.splitlines(), bom, testo.endswith("\n")


def codifica(righe: list[str], bom: bool, newline_finale: bool) -> bytes:
    testo = "\n".join(righe)
    if newline_finale:
        testo += "\n"
    dati = testo.encode("utf-8")
    return (b"\xef\xbb\xbf" + dati) if bom else dati


def sha256(dati: bytes) -> str:
    return hashlib.sha256(dati).hexdigest()


def rimuovi_apparato(righe: list[str]) -> list[str]:
    aveva_blocco = INIZIO in righe or FINE in righe
    fuori: list[str] = []
    dentro = False
    dopo_blocco = False
    for riga in righe:
        if riga == INIZIO:
            if dentro:
                raise ValueError("marcatore iniziale dell'indice duplicato")
            dentro = True
            continue
        if riga == FINE:
            if not dentro:
                raise ValueError("marcatore finale dell'indice senza apertura")
            dentro = False
            dopo_blocco = True
            continue
        if dentro:
            continue
        if dopo_blocco and not riga:
            continue
        dopo_blocco = False
        if ANCORA_RE.match(riga):
            continue
        if aveva_blocco and ANCORA_PRECEDENTE_RE.match(riga):
            continue
        fuori.append(riga)
    if dentro:
        raise ValueError("indice interno non chiuso")
    return fuori


def testo_per_slug(testo: str) -> str:
    testo = re.sub(r"<[^>]+>", " ", testo)
    testo = testo.replace("$", " ").replace("\\", " ")
    testo = unicodedata.normalize("NFKD", testo)
    testo = "".join(carattere for carattere in testo if not unicodedata.combining(carattere))
    testo = testo.lower()
    testo = re.sub(r"[^a-z0-9]+", "-", testo).strip("-")
    return testo or "sezione"


def base_ancora(file_id: str, testo: str) -> str:
    pulito = testo.strip().strip("*").strip()
    numero = NUMERO_RE.match(pulito)
    if numero:
        parte = numero.group(1).lower().replace(".", "-")
    elif pulito.lower() == "norma":
        parte = f"{file_id.lower().replace('.', '-')}-norma"
    elif pulito.lower() == "circolare":
        solo_numero = file_id.lower().removeprefix("c").replace(".", "-")
        parte = f"c{solo_numero}-circolare"
    else:
        parte = f"{file_id.lower().replace('.', '-')}-{testo_per_slug(pulito)}"
    return f"toc-ntc2018-{parte}"


def trova_titoli(righe: list[str], file_id: str) -> list[Titolo]:
    provvisori: list[tuple[int, int, str, str]] = []
    occorrenze: dict[str, int] = {}
    recinto: str | None = None
    for indice, riga in enumerate(righe):
        fence = FENCE_RE.match(riga)
        if fence:
            simbolo = fence.group(1)[0]
            recinto = None if recinto == simbolo else simbolo
            continue
        if recinto:
            continue
        match = HEADING_RE.match(riga)
        if not match:
            continue
        livello = len(match.group(1))
        if livello == 1:
            continue
        testo = match.group(2).strip()
        base = base_ancora(file_id, testo)
        occorrenze[base] = occorrenze.get(base, 0) + 1
        ancora = base if occorrenze[base] == 1 else f"{base}-{occorrenze[base]}"
        provvisori.append((indice, livello, testo, ancora))

    pila: list[int] = []
    titoli: list[Titolo] = []
    for indice, livello, testo, ancora in provvisori:
        while pila and livello <= pila[-1]:
            pila.pop()
        profondita = len(pila)
        pila.append(livello)
        titoli.append(Titolo(indice, livello, testo, ancora, profondita))
    return titoli


def genera(path: Path) -> tuple[bytes, int, str]:
    righe_originali, bom, newline_finale = leggi(path)
    corpo = rimuovi_apparato(righe_originali)
    match_file = FILE_RE.match(path.name)
    if not match_file:
        raise ValueError("nome non conforme al modello x.y.z")
    file_id = match_file.group(1)
    titoli = trova_titoli(corpo, file_id)
    if not titoli:
        raise ValueError("nessuna intestazione interna trovata")

    per_riga = {titolo.indice_riga: titolo.ancora for titolo in titoli}
    con_ancore: list[str] = []
    for indice, riga in enumerate(corpo):
        if indice in per_riga:
            con_ancore.append(f'<a id="{per_riga[indice]}"></a>')
        con_ancore.append(riga)

    indice_h1 = next(
        (indice for indice, riga in enumerate(con_ancore) if re.match(r"^#\s+", riga)),
        None,
    )
    if indice_h1 is None:
        raise ValueError("titolo principale H1 non trovato")
    inserimento = indice_h1 + 1
    while inserimento < len(con_ancore) and con_ancore[inserimento] == "":
        inserimento += 1

    blocco = [INIZIO, "**Indice interno**", ""]
    for titolo in titoli:
        rientro = "  " * titolo.profondita_indice
        blocco.append(f"{rientro}- [{titolo.testo}](#{titolo.ancora})")
    blocco.append(FINE)
    finali = con_ancore[:inserimento] + blocco + [""] + con_ancore[inserimento:]
    corpo_hash = sha256(codifica(corpo, bom, newline_finale))
    return codifica(finali, bom, newline_finale), len(titoli), corpo_hash


def verifica_file(path: Path) -> list[str]:
    errori: list[str] = []
    righe, _, _ = leggi(path)
    if righe.count(INIZIO) != 1 or righe.count(FINE) != 1:
        return ["numero dei marcatori dell'indice diverso da uno"]
    inizio = righe.index(INIZIO)
    fine = righe.index(FINE)
    if fine <= inizio:
        return ["ordine dei marcatori dell'indice non valido"]
    link = [match.group(1) for riga in righe[inizio + 1 : fine] if (match := LINK_RE.match(riga))]
    ancore = [match.group(1) for riga in righe if (match := ANCORA_RE.match(riga))]
    if not link:
        errori.append("indice privo di collegamenti")
    if len(link) != len(ancore):
        errori.append(f"collegamenti {len(link)} diversi dalle ancore {len(ancore)}")
    mancanti = sorted(set(link) - set(ancore))
    if mancanti:
        errori.append(f"destinazioni mancanti: {', '.join(mancanti[:3])}")
    duplicati = sorted({ancora for ancora in ancore if ancore.count(ancora) > 1})
    if duplicati:
        errori.append(f"ancore duplicate: {', '.join(duplicati[:3])}")
    if any(ANCORA_PRECEDENTE_RE.match(riga) for riga in righe):
        errori.append("ancora del modello sperimentale ancora presente")
    return errori


def corpo_senza_apparati(path: Path) -> bytes:
    righe, bom, newline_finale = leggi(path)
    return codifica(rimuovi_apparato(righe), bom, newline_finale)


def prepara_snapshot(snapshot: Path, files: list[Path]) -> None:
    snapshot = snapshot.resolve()
    radice_audit = (ROOT / "_tmp_render").resolve()
    if snapshot != radice_audit and radice_audit not in snapshot.parents:
        raise ValueError("lo snapshot deve stare dentro _tmp_render")
    if snapshot.exists() and any(snapshot.iterdir()):
        raise ValueError(f"la cartella snapshot non è vuota: {snapshot}")
    for path in files:
        destinazione = snapshot / "pre" / path.relative_to(ROOT)
        destinazione.parent.mkdir(parents=True, exist_ok=True)
        # Lo snapshot certifica i byte; i metadati temporali non fanno parte del manifest.
        # Su filesystem WSL condivisi copystat può fallire con EPERM.
        shutil.copyfile(path, destinazione)


def scrivi_manifest(snapshot: Path, righe: list[dict[str, object]]) -> None:
    snapshot.mkdir(parents=True, exist_ok=True)
    path = snapshot / "manifest.csv"
    campi = [
        "file",
        "sha256_pre",
        "sha256_post",
        "sha256_corpo_senza_apparati",
        "intestazioni_interne",
    ]
    with path.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=campi, delimiter=";", lineterminator="\n")
        writer.writeheader()
        writer.writerows(righe)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--applica", action="store_true", help="Scrive gli indici nei file.")
    parser.add_argument("--verifica", action="store_true", help="Controlla tutti i file dopo la generazione.")
    parser.add_argument("--snapshot", type=Path, help="Cartella di audit sotto _tmp_render.")
    args = parser.parse_args()

    files = file_naturali()
    if len(files) != XYZ_ATTESI:
        print(
            f"ERRORE: trovati {len(files)} file x.y.z, attesi {XYZ_ATTESI}.",
            file=sys.stderr,
        )
        return 1

    if args.applica:
        if not args.snapshot:
            print("ERRORE: --applica richiede --snapshot.", file=sys.stderr)
            return 1
        snapshot = args.snapshot if args.snapshot.is_absolute() else ROOT / args.snapshot
        candidati: list[tuple[Path, bytes, bytes, int, str]] = []
        for path in files:
            pre = path.read_bytes()
            nuovi, quanti, corpo_hash = genera(path)
            candidati.append((path, pre, nuovi, quanti, corpo_hash))
        prepara_snapshot(snapshot, files)
        manifest: list[dict[str, object]] = []
        for path, pre, nuovi, quanti, corpo_hash in candidati:
            temporaneo = path.with_suffix(path.suffix + ".tmp-indice")
            temporaneo.write_bytes(nuovi)
            temporaneo.replace(path)
            manifest.append(
                {
                    "file": path.relative_to(ROOT).as_posix(),
                    "sha256_pre": sha256(pre),
                    "sha256_post": sha256(nuovi),
                    "sha256_corpo_senza_apparati": corpo_hash,
                    "intestazioni_interne": quanti,
                }
            )
        scrivi_manifest(snapshot, manifest)
        print(f"Applicati indici interni a {len(files)} file.")
        print(f"Manifest e copie recuperabili: {snapshot}")

    if args.verifica or not args.applica:
        rilievi: list[str] = []
        collegamenti = 0
        corpi_confrontati = 0
        snapshot_verifica = None
        if args.snapshot:
            snapshot_verifica = args.snapshot if args.snapshot.is_absolute() else ROOT / args.snapshot
        for path in files:
            errori = verifica_file(path)
            atteso, _, _ = genera(path)
            if path.read_bytes() != atteso:
                errori.append("indice presente ma non allineato alla forma canonica")
            rilievi.extend(f"{path.relative_to(ROOT).as_posix()}: {errore}" for errore in errori)
            righe, _, _ = leggi(path)
            collegamenti += sum(1 for riga in righe if LINK_RE.match(riga))
            if snapshot_verifica:
                precedente = snapshot_verifica / "pre" / path.relative_to(ROOT)
                if not precedente.is_file():
                    rilievi.append(
                        f"{path.relative_to(ROOT).as_posix()}: copia precedente mancante"
                    )
                elif corpo_senza_apparati(path) != corpo_senza_apparati(precedente):
                    rilievi.append(
                        f"{path.relative_to(ROOT).as_posix()}: corpo diverso fuori dagli apparati"
                    )
                else:
                    corpi_confrontati += 1
        if rilievi:
            for rilievo in rilievi[:30]:
                print(f"ERRORE: {rilievo}", file=sys.stderr)
            print(f"Verifica fallita: {len(rilievi)} rilievi.", file=sys.stderr)
            return 1
        dettaglio = f", {corpi_confrontati} corpi invariati" if snapshot_verifica else ""
        print(
            f"Verifica superata: {len(files)} file, {collegamenti} collegamenti interni"
            f"{dettaglio}."
        )
    return 0


if __name__ == "__main__":
    sys.exit(main())
