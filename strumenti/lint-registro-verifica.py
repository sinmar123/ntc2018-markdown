#!/usr/bin/env python3
"""Controlla il registro VC compatto contro file e indici attivi."""

from __future__ import annotations

import csv
import re
from collections import Counter
from datetime import date
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REGISTER = ROOT / "registro-verifica-conformita-ntc2018.csv"
FIELDS = [
    "paragrafo",
    "titolo",
    "n.",
    "apri_md",
    "pagine_pdf_ntc",
    "pagine_pdf_circolare",
    "stato_vc",
    "data_ultima_vc",
    "prossima_azione",
    "evidenza_vc",
    "note",
    "procedura_vc",
    "agente_vc",
]
STATES = {"VC-OK", "IN-CORSO", "DA-RICONFERMARE", "DA-RIFARE", "MAI-FATTA"}
VC_OK_NEXT_ACTION = "Nessuna sul file: VC conclusa sullo snapshot registrato."
FILE_RE = re.compile(r"^(c?\d+(?:\.\d+){0,2})-.+\.md$", re.I)
FILE_XYZ = re.compile(r"^(c?\d+\.\d+\.\d+)-.+\.md$", re.I)
LINK_RE = re.compile(r"\]\(([^)]+\.md)(?:#[^)]*)?\)")
PAGE_RE = re.compile(r"^\d+(?:-\d+)?(?:, \d+(?:-\d+)?)*$")
TOC_START = "<!-- INDICE-INTERNO:INIZIO -->"
TOC_END = "<!-- INDICE-INTERNO:FINE -->"


def indexed_files() -> set[str]:
    found: set[str] = set()
    indexes = list(ROOT.glob("indice-*.md")) + list(ROOT.glob("cap??/indice-*.md"))
    for index in indexes:
        text = index.read_text(encoding="utf-8-sig")
        for target in LINK_RE.findall(text):
            path = (index.parent / target.split("#", 1)[0]).resolve()
            try:
                relative = path.relative_to(ROOT.resolve()).as_posix()
            except ValueError:
                continue
            parts = Path(relative).parts
            if (
                len(parts) == 2
                and parts[0].startswith("cap")
                and FILE_RE.match(Path(relative).name)
            ):
                found.add(relative)
    return found


def title_from_file(path: Path, paragraph: str) -> str:
    text = path.read_text(encoding="utf-8-sig")
    heading = next(
        (line[2:].strip() for line in text.splitlines() if line.startswith("# ")),
        "",
    )
    heading = re.sub(r"[*_`]", "", heading).strip()
    return re.sub(
        rf"^{re.escape(paragraph)}\s*\.?\s*",
        "",
        heading,
        flags=re.I,
    ).strip()


def valid_pages(value: str) -> bool:
    if not PAGE_RE.fullmatch(value):
        return False
    previous = 0
    for token in value.split(", "):
        parts = [int(part) for part in token.split("-")]
        start = parts[0]
        end = parts[-1]
        if start <= 0 or end < start or start <= previous:
            return False
        previous = end
    return True


def main() -> int:
    errors: list[str] = []
    warnings: list[str] = []
    with REGISTER.open("r", encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle, delimiter=";")
        if reader.fieldnames not in (FIELDS, FIELDS[:-1], FIELDS[:-2]):
            errors.append(f"intestazione inattesa: {reader.fieldnames}")
        rows = list(reader)

    registered = [row.get("apri_md", "") for row in rows]
    duplicates = [path for path, count in Counter(registered).items() if count > 1]
    if duplicates:
        errors.append(f"file duplicati nel registro: {duplicates}")
    indexed = indexed_files()
    registered_set = set(registered)
    if len(rows) != len(indexed):
        errors.append(f"righe: {len(rows)}, attese {len(indexed)} dai file indicizzati")
    if registered_set != indexed:
        missing = sorted(indexed - registered_set)
        extra = sorted(registered_set - indexed)
        errors.append(f"scarto registro/indici: mancanti={missing}, extra={extra}")

    for position, row in enumerate(rows, start=1):
        label = f"riga {position + 1}"
        if row.get("n.") != str(position):
            errors.append(f"{label}: n.={row.get('n.')!r}, atteso {position}")
        file_md = row.get("apri_md", "")
        path = ROOT / file_md
        if not path.is_file():
            errors.append(f"{label}: file inesistente {file_md!r}")
            continue
        match = FILE_RE.match(path.name)
        if not match:
            errors.append(f"{label}: nome non conforme x / x.y / x.y.z {file_md!r}")
        else:
            section = match.group(1)
            section = "C" + section[1:] if section.lower().startswith("c") else section
            if row.get("paragrafo") != section:
                errors.append(
                    f"{label}: paragrafo {row.get('paragrafo')!r}, atteso {section!r}"
                )
        expected_title = title_from_file(path, row.get("paragrafo", ""))
        if row.get("titolo") != expected_title:
            errors.append(
                f"{label}: titolo {row.get('titolo')!r}, atteso {expected_title!r}"
            )
        text = path.read_text(encoding="utf-8-sig")
        if FILE_XYZ.match(path.name):
            if text.count(TOC_START) != 1 or text.count(TOC_END) != 1:
                errors.append(f"{label}: indice interno assente o duplicato in {file_md}")
        elif TOC_START in text or TOC_END in text:
            if text.count(TOC_START) != 1 or text.count(TOC_END) != 1:
                errors.append(f"{label}: indice interno duplicato o incompleto in {file_md}")

        for field in ("pagine_pdf_ntc", "pagine_pdf_circolare"):
            value = row.get(field, "")
            if value and not valid_pages(value):
                errors.append(f"{label}: {field} non valido: {value!r}")
        state = row.get("stato_vc", "")
        if state not in STATES:
            errors.append(f"{label}: stato_vc non valido {state!r}")
        date_value = row.get("data_ultima_vc", "")
        if date_value:
            try:
                date.fromisoformat(date_value)
            except ValueError:
                errors.append(f"{label}: data_ultima_vc non ISO {date_value!r}")
        evidence = row.get("evidenza_vc", "")
        if evidence and not (ROOT / evidence).is_file():
            errors.append(f"{label}: evidenza_vc inesistente {evidence!r}")
        if state in {"VC-OK", "DA-RICONFERMARE"} and (not date_value or not evidence):
            errors.append(f"{label}: {state} richiede data_ultima_vc ed evidenza_vc")
        if state in {"DA-RIFARE", "IN-CORSO"} and not evidence:
            errors.append(f"{label}: {state} richiede evidenza_vc")
        if state == "MAI-FATTA" and (date_value or evidence):
            errors.append(f"{label}: MAI-FATTA non deve avere data o evidenza")
        if not row.get("prossima_azione", "").strip():
            errors.append(f"{label}: prossima_azione vuota")
        if state == "VC-OK" and row.get("prossima_azione", "").strip() != VC_OK_NEXT_ACTION:
            errors.append(
                f"{label}: VC-OK richiede prossima_azione {VC_OK_NEXT_ACTION!r}"
            )
        if re.search(r"\b(?!https?://)[a-z][a-z0-9+.-]*://", " ".join(row.values()), re.I):
            errors.append(f"{label}: collegamento a un'applicazione non ammesso, solo pagine web")
        if (
            "## Circolare" in text
            and not row.get("pagine_pdf_circolare")
            and "Pagine della Circolare non rilevate" not in row.get("note", "")
        ):
            warnings.append(f"{label}: pagina Circolare vuota senza nota")

    disk_files = {
        path.relative_to(ROOT).as_posix()
        for path in ROOT.glob("cap??/*.md")
        if FILE_RE.match(path.name)
    }
    unindexed = sorted(disk_files - indexed)
    if unindexed:
        warnings.append(
            "file in cartella non indicizzati (residui pre-ricomposizione): "
            f"{len(unindexed)}"
        )

    print(f"Registro: {len(rows)} righe, {len(rows[0]) if rows else len(FIELDS)} colonne")
    print("Stati: " + ", ".join(f"{key}={value}" for key, value in sorted(Counter(row.get('stato_vc', '') for row in rows).items())))
    print(f"Errori: {len(errors)}; avvisi: {len(warnings)}")
    for message in errors:
        print(f"ERRORE: {message}")
    for message in warnings:
        print(f"AVVISO: {message}")
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
