"""Meccanica VC NTC: stato, pacchetti fonte-prima, manifest e consumi.

Non decide conformità, non modifica il corpus e non esegue modelli.
Specifiche: vc-supporto.md. Procedura: ../PROCEDURA-VC.md.
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import json
import io
import os
import re
import runpy
import shutil
import subprocess
import sys
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path, PurePosixPath

ROOT = Path(__file__).resolve().parent.parent
DEPURA = runpy.run_path(str(ROOT / "strumenti/prepara-scope-g6.py"))["depura"]
PROCEDURA = ROOT / "PROCEDURA-VC.md"
CATALOGO = ROOT / "verifica-conformita/normalizzazioni-dichiarate-NTC2018.md"
AGENT_LABELS = {"CDX": "Codex (CDX)", "CC": "Claude Code (CC)", "CCC": "CC cloud (CCC)", "OC": "OpenClaw (OC)",
                "GROK": "Grok (GROK)", "GBOT": "Grok Bot (GBOT)", "HRM": "Hermes (HRM)"}

V_INSTRUCTIONS = '''# Consegna al verificatore

Leggere solo questa cartella e le integrazioni fonte espressamente consegnate.
Non aprire coordinamento.json, workspace o altri rapporti. Isolamento istruttivo,
salvo sandbox effettivamente documentata. Il canone.md contiene tutti i criteri.

1. FONTE-PRIMA: osservare integralmente le pagine del PERIMETRO.md e i dettagli
necessari. Scrivere inventario.json con firma effettiva, esito_provvisorio
(LEGGIBILE o DUBBIO), elementi ed esclusioni. Ogni elemento richiede id univoco,
pagina (una chiave di input-fonte.json) e riferimento preciso; ogni esclusione
richiede pagina e riferimento. Non copiare la prosa o tutte le celle:
localizzare capoversi e rettangoli di celle, dichiarando estensione e controllo
integrale. Registrare separatamente formule, condizioni, figure e dubbi.
Schema dei campi: {"firma":"identità effettiva", "esito_provvisorio":"LEGGIBILE",
"elementi":[{"id":"ID scelto da V", "pagina":"chiave fonte", "riferimento":"posizione"}],
"esclusioni":[], "dubbi":[]}.
Il coordinatore valida lo schema prima del congelamento; eventuali difetti
di forma si correggono nello stesso contesto prima di ogni rivelazione.
Fermarsi dopo l'inventario: nessun accesso al target prima del via del coordinatore.

2. CONFRONTO: dopo il congelamento e il via leggere tutto testo.md e gli asset
rivelati. Scrivere rapporto-g6.json: firma, esito (OK o KO), coperti (tutti gli
id verificati), normalizzazioni (numeri del catalogo), rilievi, letture (percorsi),
isolamento. Ogni rilievo specifica id, pagina/posizione, prova e classe proposta.
Con zero rilievi bastano gli ID coperti e l'attestazione di confronto integrale,
senza ricopiare inventario e motivazione OK per ciascuna cella. Un gruppo coperto
significa controllo di TUTTI i suoi componenti, mai campionamento.
Niente correzioni degli input. Richiedere prove ulteriori con domanda aperta.
Fermarsi dopo G6; G7 arriverà nello stesso contesto quando le evidenze sono pronte.

Prosa ordinaria entro 300 parole per fase, oltre a ID e rilievi necessari.
Il limite non tronca copertura, dubbi o prove: motivare l'eventuale superamento
nel rapporto stesso. Non riscrivere hash calcolabili o creare rapporti aggiuntivi.
'''


def require(condition, message):
    if not condition:
        raise ValueError(message)


def read_json(path):
    return json.loads(Path(path).read_text(encoding="utf-8-sig"))


def write_new(path, text):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("x", encoding="utf-8", newline="\n") as stream:
        stream.write(text)


def json_new(path, value):
    write_new(path, json.dumps(value, ensure_ascii=False, indent=2) + "\n")


def sha(path):
    digest = hashlib.sha256()
    with Path(path).open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def digest_text(text):
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def portable(name):
    require(isinstance(name, str) and name and "\\" not in name, "Percorso non portabile")
    path = PurePosixPath(name)
    require(not path.is_absolute() and ".." not in path.parts, f"Percorso non relativo: {name}")
    require(all(re.fullmatch(r"[^<>:\"|?*\x00-\x1f]+", part) and part.rstrip(" .") == part
                for part in path.parts), f"Nome Windows non valido: {name}")
    reserved = {"con", "prn", "aux", "nul"} | {f"{p}{i}" for p in ("com", "lpt") for i in range(1, 10)}
    require(all(part.split(".")[0].casefold() not in reserved for part in path.parts), f"Nome riservato: {name}")
    return path.as_posix()


def inside(root, relative):
    root = Path(root).resolve()
    path = (root / portable(relative)).resolve()
    require(path.is_relative_to(root), f"Percorso esterno alla radice: {relative}")
    return path


def unique_names(names):
    keys = [portable(name).casefold() for name in names]
    require(len(keys) == len(set(keys)), "Collisione fra nomi, anche per maiuscole/minuscole")


def records(root, names):
    unique_names(names)
    result = []
    for name in sorted(names):
        path = inside(root, name)
        require(path.is_file(), f"File mancante: {name}")
        result.append({"path": name, "bytes": path.stat().st_size, "sha256": sha(path)})
    return result


def verify_records(root, rows):
    require(isinstance(rows, list) and rows, "Manifest vuoto")
    expected = {row["path"]: row for row in rows}
    actual = records(root, [row["path"] for row in rows])
    for row in actual:
        require(row == expected[row["path"]], f"Impronta o dimensione non coincidente: {row['path']}")
    return len(actual)


def neutral_canone():
    procedure = PROCEDURA.read_text(encoding="utf-8")
    start, end = "<!-- CANONE-G6:INIZIO -->", "<!-- CANONE-G6:FINE -->"
    require(procedure.count(start) == procedure.count(end) == 1, "Marcatori del canone non univoci")
    body = procedure.split(start)[1].split(end)[0].strip()
    catalogue = CATALOGO.read_text(encoding="utf-8")
    # Si estraggono solo le 18 voci prescrittive, eliminando esempi e cronologia.
    rules = re.findall(r"(?m)^\d+\. .+(?:\n(?!\n|\d+\. |#).+)*", catalogue)
    require([int(re.match(r"\d+", rule)[0]) for rule in rules] == list(range(1, 19)),
            "Catalogo cambiato: aggiornare e collaudare l'estrazione neutra")
    clean = []
    for rule in rules:
        rule = re.split(r" Cas[oi] not[oi]:", rule)[0]
        rule = re.sub(r" Vedi `AF-[^\n]+", "", rule)
        rule = re.sub(r"[:.]? [Dd]eciso da Sandro[^\n]+", ".", rule)
        rule = re.sub(r" per esempio `[^`]+`[^\n]*", "", rule)
        rule = re.sub(r": `\[C4\.1\.10 \]` reso `\[C4\.1\.10\]`\.", ".", rule)
        clean.append(rule)
    return body + "\n\n## Catalogo delle normalizzazioni, estratto neutro\n\n" + "\n\n".join(clean) + "\n"


def clean_target(path):
    return DEPURA(Path(path).read_text(encoding="utf-8-sig"))


def slice_lines(text, ranges):
    lines = text.splitlines(keepends=True)
    selected = []
    for start, end in ranges:
        require(isinstance(start, int) and isinstance(end, int) and 1 <= start <= end <= len(lines),
                "Intervallo di righe non valido")
        selected.extend(range(start, end + 1))
    require(selected == sorted(set(selected)), "Righe duplicate o fuori ordine nel blocco")
    return "".join(lines[index - 1] for index in selected), selected


def inventory_check(folder):
    """Solo input del blocco: nessun accesso al coordinamento o al target vivo."""
    folder = Path(folder)
    source = read_json(folder / "input-fonte.json")
    verify_records(folder, source["files"])
    inv = read_json(folder / "inventario.json")
    require(inv.get("firma") and inv.get("esito_provvisorio") in {"LEGGIBILE", "DUBBIO"},
            "Firma/esito provvisorio mancanti")
    require(isinstance(inv.get("elementi"), list) and inv["elementi"], "Inventario fonte vuoto")
    require(isinstance(inv.get("esclusioni"), list), "Esclusioni fonte non dichiarate")
    entries = inv["elementi"] + inv["esclusioni"]
    require(all(isinstance(e, dict) and e.get("pagina") in source["pagine"]
                and isinstance(e.get("riferimento"), str) and e["riferimento"].strip() for e in entries),
            "Pagina/riferimento degli elementi non valido")
    require(set(e["pagina"] for e in entries) == set(source["pagine"]),
            "Inventario senza copertura di tutte le pagine")
    if source.get("schema_inventario") == 2:
        ids = [e.get("id") for e in inv["elementi"]]
        require(all(isinstance(i, str) and i.strip() for i in ids) and len(ids) == len(set(ids)),
                "ID inventario mancanti o duplicati")
    return {"schema": "OK", "elementi": len(inv["elementi"]), "pagine": len(source["pagine"]),
            "giudizio_vc": "NON_EMESSO"}


def g6_check(folder, report_path):
    folder = Path(folder)
    inv = read_json(folder / "inventario.json")
    frozen = read_json(folder / "congelamento.json")
    require(sha(folder / "inventario.json") == frozen["inventario_sha256"], "Inventario congelato alterato")
    require(sha(folder / "canone.md") == frozen["criterio_canone_sha256"], "Canone congelato alterato")
    verify_records(folder, read_json(folder / "input-confronto.json")["files"])
    report = read_json(report_path)
    ids = [e.get("id") for e in inv["elementi"]]
    require(all(isinstance(i, str) and i for i in ids) and len(ids) == len(set(ids)), "ID inventario non validi")
    covered = report.get("coperti", [])
    require(isinstance(covered, list) and all(isinstance(i, str) for i in covered)
            and len(covered) == len(set(covered)) and set(covered) == set(ids), "Copertura ID incompleta o duplicata")
    require(report.get("firma") and report.get("esito") in {"OK", "KO"}, "Firma/esito G6 mancanti")
    require(isinstance(report.get("rilievi"), list), "Rilievi non dichiarati")
    require(report["esito"] != "OK" or not report["rilievi"], "Esito OK con rilievi aperti")
    return {"schema": "OK", "coperti": len(covered), "rilievi": len(report["rilievi"]),
            "esito_dichiarato_da_V": report["esito"], "giudizio_vc": "NON_EMESSO"}


def bootstrap(scope=None):
    with (ROOT / "registro-verifica-conformita-ntc2018.csv").open(encoding="utf-8-sig", newline="") as stream:
        rows = list(csv.DictReader(stream, delimiter=";"))
    chosen = [r for r in rows if r["paragrafo"].casefold() == scope.casefold()] if scope else [r for r in rows if r["stato_vc"] == "IN-CORSO"]
    if len(chosen) != 1:
        return {"selezione": "NON_UNIVOCA", "in_corso": [r["paragrafo"] for r in rows if r["stato_vc"] == "IN-CORSO"],
                "azione": "Chiarire lo scope; nessuna presa in carico automatica"}
    row = chosen[0]
    sheet = ROOT / f"verifica-conformita/scheda-scope-ntc2018-{row['paragrafo'].lower()}.md"
    text = sheet.read_text(encoding="utf-8") if sheet.exists() else ""
    header = text.split("---", 2)[1].strip() if text.startswith("---") else ""
    fragments = {}
    for name in ["README.md", "TODO.md", "CHANGELOG.md"]:
        content = (ROOT / name).read_text(encoding="utf-8")
        sections = re.split(r"(?m)(?=^## )", content)
        matches = [s for s in sections if re.search(rf"(?<![\w.]){re.escape(row['paragrafo'])}(?![\w.])", s)]
        # Un solo tratto pertinente per file. Il taglio viene dichiarato, mai spacciato per lettura integrale.
        selected = matches[0] if matches else sections[0]
        fragments[name] = {"testo": selected[:1800], "troncato": len(selected) > 1800}
    return {"registro": row, "scheda": str(sheet.relative_to(ROOT)), "lucchetto": header,
            "ultima_nota_scheda": text.rsplit("\n## ", 1)[-1][-1400:], "governo": fragments,
            "procedura_sha256": sha(PROCEDURA), "target_sha256": sha(inside(ROOT, row["apri_md"])),
            "nota": "Sola lettura; verificare autorizzazione, lucchetto e voci troncate pertinenti. Nessuna VC avviata."}


def take_scope(config_path, apply=False, run_checks=True):
    """Prende in carico più righe naturali con un solo lucchetto di sezione."""
    cfg = read_json(config_path)
    scope = cfg.get("scope")
    row_ids = cfg.get("righe")
    agent = cfg.get("agente")
    require(isinstance(scope, str) and scope and isinstance(agent, str) and agent, "Scope/agente mancanti")
    require(isinstance(row_ids, list) and row_ids and all(isinstance(x, str) and x for x in row_ids),
            "Elenco righe mancante o non valido")
    require(len(row_ids) == len(set(row_ids)), "Righe duplicate nella presa in carico")
    require(cfg.get("nota", "").strip() and cfg.get("prossima_azione", "").strip(),
            "Nota/prossima azione mancanti")
    registry = ROOT / "registro-verifica-conformita-ntc2018.csv"
    before_csv = registry.read_bytes()
    rows = list(csv.DictReader(io.StringIO(before_csv.decode("utf-8-sig")), delimiter=";"))
    selected = [r for r in rows if r["paragrafo"] in row_ids]
    require(len(selected) == len(row_ids) and {r["paragrafo"] for r in selected} == set(row_ids),
            "Righe dello scope assenti o non univoche")
    # Una riga VC-OK si riapre soltanto per una correzione localizzata (§ 8 della procedura),
    # con motivo e autorizzazione di Sandro dichiarati nella presa e copiati nella ricevuta.
    reopening = cfg.get("riapertura_vc_ok")
    if reopening is not None:
        require(isinstance(reopening, dict) and all(isinstance(reopening.get(k), str) and reopening[k].strip()
                                                    for k in ("motivo", "autorizzazione")),
                "Riapertura VC-OK senza motivo o autorizzazione")
    allowed_states = {"MAI-FATTA", "DA-RIFARE", "DA-RICONFERMARE"} | ({"VC-OK"} if reopening else set())
    require(all(r["stato_vc"] in allowed_states for r in selected),
            "Una o più righe non sono prendibili in carico")
    require(all(inside(ROOT, r["apri_md"]).is_file() for r in selected), "Target registrato mancante")
    active_targets = {inside(ROOT, r["apri_md"]) for r in rows if r["stato_vc"] == "IN-CORSO"}
    require(not any(inside(ROOT, r["apri_md"]) in active_targets for r in selected),
            "Target condiviso con uno scope IN-CORSO")
    expected_sheet = f"verifica-conformita/scheda-scope-ntc2018-{scope.lower()}.md"
    require(cfg.get("scheda") == expected_sheet, "Percorso della scheda non canonico")
    sheet = inside(ROOT, expected_sheet)
    require(not sheet.exists(), "Scheda/lucchetto già esistente")
    content = cfg.get("scheda_contenuto")
    require(isinstance(content, str) and content.endswith("\n"), "Contenuto scheda mancante o senza a capo finale")
    require(re.search(rf"(?m)^scope_id: ntc2018-{re.escape(scope)}\s*$", content), "Scope della scheda non allineato")
    require(re.search(r"(?m)^stato: IN-CORSO\s*$", content), "Scheda non in corso")
    require(re.search(rf"(?m)^agente: {re.escape(agent)}\s*$", content), "Agente della scheda non allineato")
    reopened = [r["paragrafo"] for r in selected if r["stato_vc"] == "VC-OK"]
    for row in selected:
        row.update(stato_vc="IN-CORSO", prossima_azione=cfg["prossima_azione"],
                   evidenza_vc=expected_sheet, note=cfg["nota"])
    stream = io.StringIO(newline="")
    writer = csv.DictWriter(stream, fieldnames=list(rows[0]), delimiter=";")
    writer.writeheader(); writer.writerows(rows)
    after_csv = stream.getvalue().encode("utf-8-sig")
    summary = {"fase": "PIANO", "scope": scope, "righe": row_ids,
               "file": [str(registry.relative_to(ROOT)), expected_sheet],
               "nota": "Presa aggregata; nessun giudizio VC emesso"}
    if reopening:
        summary["riapertura_vc_ok"] = {"righe": reopened, **reopening}
    if not apply:
        return summary
    receipt = Path(config_path).resolve().with_suffix(".eseguito.json")
    require(not receipt.exists(), "Presa già tentata: controllare ricevuta e stato")
    json_new(receipt, {**summary, "fase": "IN_CORSO"})
    write_new(sheet, content)
    require(registry.read_bytes() == before_csv, "Registro cambiato durante la presa in carico")
    temporary = registry.with_name(registry.name + ".vc-nuovo")
    with temporary.open("xb") as output:
        output.write(after_csv)
    os.replace(temporary, registry)
    if run_checks:
        for script in ("lint-registro-verifica.py",):
            checked = subprocess.run([sys.executable, "-X", "utf8", str(ROOT / "strumenti" / script)],
                                     cwd=ROOT, text=True, encoding="utf-8", capture_output=True)
            require(checked.returncode == 0, f"Presa scritta; controllo {script} fallito: {checked.stdout}{checked.stderr}")
    result = {**summary, "fase": "SCRITTO", "controlli": "OK" if run_checks else "fixture"}
    receipt.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return result


def sync_titles(config_path, apply=False, run_checks=True):
    """Sincronizza soltanto i titoli di righe già IN-CORSO, sotto lo stesso lucchetto."""
    cfg = read_json(config_path)
    row_ids = cfg.get("righe")
    require(isinstance(row_ids, list) and row_ids and all(isinstance(x, str) and x for x in row_ids)
            and len(row_ids) == len(set(row_ids)), "Righe da sincronizzare mancanti o duplicate")
    require(cfg.get("scope") and cfg.get("agente"), "Scope/agente mancanti")
    sheet = inside(ROOT, f"verifica-conformita/scheda-scope-ntc2018-{cfg['scope'].lower()}.md")
    text = sheet.read_text(encoding="utf-8")
    require(re.search(r"(?m)^stato: IN-CORSO\s*$", text), "Scheda non in corso")
    require(re.search(rf"(?m)^agente: {re.escape(cfg['agente'])}\s*$", text), "Lucchetto di altro agente")
    registry = ROOT / "registro-verifica-conformita-ntc2018.csv"
    before = registry.read_bytes()
    rows = list(csv.DictReader(io.StringIO(before.decode("utf-8-sig")), delimiter=";"))
    selected = [r for r in rows if r["paragrafo"] in row_ids]
    require(len(selected) == len(row_ids) and {r["paragrafo"] for r in selected} == set(row_ids)
            and all(r["stato_vc"] == "IN-CORSO" for r in selected), "Righe non tutte IN-CORSO")
    title_from_file = runpy.run_path(str(ROOT / "strumenti/lint-registro-verifica.py"))["title_from_file"]
    changed = 0
    for row in selected:
        title = title_from_file(inside(ROOT, row["apri_md"]), row["paragrafo"])
        if row["titolo"] != title:
            row["titolo"] = title
            changed += 1
    require(changed, "Nessun titolo da sincronizzare")
    stream = io.StringIO(newline="")
    writer = csv.DictWriter(stream, fieldnames=list(rows[0]), delimiter=";")
    writer.writeheader(); writer.writerows(rows)
    after = stream.getvalue().encode("utf-8-sig")
    summary = {"fase": "PIANO", "scope": cfg["scope"], "righe": row_ids,
               "titoli_aggiornati": changed, "file": str(registry.relative_to(ROOT))}
    if not apply:
        return summary
    receipt = Path(config_path).resolve().with_suffix(".eseguito.json")
    require(not receipt.exists(), "Sincronizzazione già tentata: controllare la ricevuta")
    json_new(receipt, {**summary, "fase": "IN_CORSO", "prima": hashlib.sha256(before).hexdigest(),
                       "dopo": hashlib.sha256(after).hexdigest()})
    require(registry.read_bytes() == before, "Registro cambiato durante la sincronizzazione")
    temporary = registry.with_name(registry.name + ".vc-nuovo")
    with temporary.open("xb") as output:
        output.write(after)
    os.replace(temporary, registry)
    if run_checks:
        checked = subprocess.run([sys.executable, "-X", "utf8", str(ROOT / "strumenti/lint-registro-verifica.py")],
                                 cwd=ROOT, text=True, encoding="utf-8", capture_output=True)
        require(checked.returncode == 0, "Titoli scritti; lint fallito: " + checked.stdout + checked.stderr)
    result = {**summary, "fase": "SCRITTO", "controlli": "OK" if run_checks else "fixture"}
    receipt.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return result


def verify_historical(root, manifest):
    """Risoluzione esplicita delle sole procedure vive mediante copie GIÀ nel manifest."""
    root = Path(root)
    rows = read_json(manifest)["files"]
    replacements = []
    selected = []
    allowed = {"PROCEDURA-VC.md", "verifica-conformita/normalizzazioni-dichiarate-NTC2018.md"}
    for row in rows:
        actual = inside(root, row["path"])
        if row["path"] in allowed and (not actual.is_file() or sha(actual) != row["sha256"]):
            candidates = [r for r in rows if r["path"] != row["path"] and r["sha256"] == row["sha256"]
                          and r["bytes"] == row["bytes"] and "congelat" in Path(r["path"]).name.lower()]
            require(candidates, "Copia congelata non presente nel manifest: " + row["path"])
            verify_records(root, [candidates[0]])
            replacements.append({"riferimento_vivo": row["path"], "copia_congelata": candidates[0]["path"],
                                 "sha256": row["sha256"]})
        else:
            selected.append(row)
    verify_records(root, selected)
    unique_names([r["path"] for r in rows])
    return {"files": len(rows), "integrita_snapshot": "OK", "riferimenti_storici": replacements,
            "giudizio_vc": "NON_EMESSO", "nota": "Non verifica la vigenza odierna; nessuna sostituzione di target o fonte normativa"}


def registration(config_path, apply=False, run_checks=True):
    """Copia nei registri un giudizio già emesso: prima piano verificato, poi scritture vincolate."""
    cfg = read_json(config_path)
    report = inside(ROOT, cfg["g7"])
    require(sha(report) == cfg["g7_sha256"], "Rapporto G7 diverso da quello approvato")
    g7 = read_json(report)
    require(g7.get("giudizio_g7") == "OK" and g7.get("scope") == cfg["scope"], "G7 non positivo o scope diverso")
    require(g7.get("firma") and g7.get("rilievi_aperti") == [], "G7 senza firma o con rilievi non chiusi")
    require(all(g7.get("gate", {}).get(f"G{i}") == "OK" for i in range(8)), "Gate G0-G7 non tutti OK")
    manifest = inside(ROOT, cfg["manifest"])
    require(sha(manifest) == g7.get("manifest_sha256"), "Manifest diverso da quello giudicato in G7")
    manifest_rows = read_json(manifest)["files"]
    verify_records(ROOT, manifest_rows)
    registry = ROOT / "registro-verifica-conformita-ntc2018.csv"
    before_csv = registry.read_bytes()
    rows = list(csv.DictReader(io.StringIO(before_csv.decode("utf-8-sig")), delimiter=";"))
    row_ids = cfg.get("righe", [cfg["scope"]])
    require(isinstance(row_ids, list) and row_ids and all(isinstance(x, str) and x for x in row_ids)
            and len(row_ids) == len(set(row_ids)), "Righe aggregate mancanti o duplicate")
    matches = [r for r in rows if r["paragrafo"] in row_ids]
    require(len(matches) == len(row_ids) and {r["paragrafo"] for r in matches} == set(row_ids)
            and all(r["stato_vc"] == "IN-CORSO" for r in matches),
            "Scope non in corso: nessuna registrazione automatica")
    targets = [(row, inside(ROOT, row["apri_md"])) for row in matches]
    if len(row_ids) == 1 and row_ids[0] == cfg["scope"]:
        snapshot_sha = sha(targets[0][1])
        require(snapshot_sha == g7.get("snapshot_sha256"), "Snapshot diverso da quello giudicato in G7")
        snapshot_paths = {targets[0][0]["apri_md"]: snapshot_sha}
        snapshot_manifest = None
    else:
        snapshot_manifest = inside(ROOT, cfg["snapshot_manifest"])
        snapshot_sha = sha(snapshot_manifest)
        require(snapshot_sha == cfg.get("snapshot_sha256") == g7.get("snapshot_sha256"),
                "Snapshot aggregato diverso da quello giudicato in G7")
        snapshot_rows = read_json(snapshot_manifest).get("files")
        verify_records(ROOT, snapshot_rows)
        snapshot_paths = {item["path"]: item["sha256"] for item in snapshot_rows}
        require(all(snapshot_paths.get(row["apri_md"]) == sha(target) for row, target in targets),
                "Uno o più target vivi sono assenti dallo snapshot aggregato")
        require(any(r["path"] == cfg["snapshot_manifest"] and r["sha256"] == snapshot_sha for r in manifest_rows),
                "Manifest dello snapshot aggregato assente dal manifest finale")
    sheet_path = inside(ROOT, f"verifica-conformita/scheda-scope-ntc2018-{cfg['scope'].lower()}.md")
    sheet = sheet_path.read_text(encoding="utf-8")
    require(re.search(r"(?m)^stato: IN-CORSO\s*$", sheet), "Scheda non in corso")
    require(re.search(rf"(?m)^agente: {re.escape(cfg['agente'])}\s*$", sheet), "Lucchetto di altro agente")
    require(re.search(rf"(?m)^snapshot_sha256: {snapshot_sha}\s*$", sheet), "Snapshot della scheda non allineato")
    counters = [re.search(rf"(?m)^{name}: (\d+)\s*$", sheet) for name in ("giro_g6", "max_giri")]
    require(all(counters) and 1 <= int(counters[0][1]) <= int(counters[1][1]), "Contatore G6 mancante o oltre il limite")
    require(all(any(r["path"] == row["apri_md"] and r["sha256"] == sha(target) for r in manifest_rows)
                for row, target in targets), "Uno o più target giudicati sono assenti dal manifest")
    verbale = inside(ROOT, cfg["verbale"])
    require(verbale.is_file() and sha(verbale) == cfg["verbale_sha256"], "Verbale mancante o cambiato")
    datetime.strptime(cfg["data"], "%Y-%m-%d")
    require(cfg["prossima_azione"].strip() and cfg["nota"].strip(), "Nota/prossima azione mancanti")
    used_procedure = re.search(r"(?m)^procedura: (VC-NTC/\d+)\s*$", sheet)
    procedure_label = cfg.get("procedura_vc")
    if procedure_label is None:
        procedure_label = used_procedure[1] if used_procedure else ""
        if procedure_label in {"VC-NTC/4", "VC-NTC/5"}:
            procedure_label += " - semplificata"
    require(isinstance(procedure_label, str), "Procedura VC non testuale")
    if procedure_label:
        label_version = re.fullmatch(r"(VC-NTC/\d+)(?: - .+)?", procedure_label)
        require(label_version and used_procedure and label_version[1] == used_procedure[1],
                "Procedura VC diversa dalla scheda")
    # Migrazione additiva: nessuna attribuzione retroattiva ai file degli altri scope.
    for row in rows:
        row.setdefault("procedura_vc", "")
        row.setdefault("agente_vc", "")
    require(cfg["agente"] in AGENT_LABELS, "Agente VC non riconosciuto")
    # Attribuzioni pregresse solo esplicite e riscontrate nella scheda dello scope.
    for row_id, agent in cfg.get("agenti_vc_da_schede", {}).items():
        historical = [r for r in rows if r["paragrafo"] == row_id]
        require(len(historical) == 1 and row_id not in row_ids and agent in AGENT_LABELS,
                "Attribuzione agente VC non valida")
        evidence = inside(ROOT, f"verifica-conformita/scheda-scope-ntc2018-{row_id.lower()}.md")
        require(evidence.is_file() and re.search(rf"(?m)^agente: {re.escape(agent)}\s*$",
                evidence.read_text(encoding="utf-8")), "Agente VC diverso dalla scheda storica")
        require(historical[0]["agente_vc"] in ("", AGENT_LABELS[agent]),
                "Attribuzione agente VC precedente discordante")
        historical[0]["agente_vc"] = AGENT_LABELS[agent]
    title_from_file = runpy.run_path(str(ROOT / "strumenti/lint-registro-verifica.py"))["title_from_file"]
    for row, target in targets:
        title = title_from_file(target, row["paragrafo"])
        row.update(titolo=title, stato_vc="VC-OK", data_ultima_vc=cfg["data"],
                   prossima_azione="Nessuna sul file: VC conclusa sullo snapshot registrato.",
                   evidenza_vc=cfg["verbale"], note=cfg["nota"], procedura_vc=procedure_label,
                   agente_vc=AGENT_LABELS[cfg["agente"]])
    stream = io.StringIO(newline="")
    writer = csv.DictWriter(stream, fieldnames=list(rows[0]), delimiter=";")
    writer.writeheader(); writer.writerows(rows)
    changes = [(registry, before_csv, stream.getvalue().encode("utf-8-sig"))]
    frozen_paths = {inside(ROOT, r["path"]) for r in manifest_rows} | {report, verbale, manifest}
    if snapshot_manifest:
        frozen_paths.add(snapshot_manifest)
    allowed = {"README.md", "TODO.md", "CHANGELOG.md", "indice-ntc2018.md",
               f"verifica-conformita/scheda-scope-ntc2018-{cfg['scope'].lower()}.md"}
    for _, target in targets:
        allowed.update(p.relative_to(ROOT).as_posix() for p in target.parent.glob("*-revisione.md"))
    supplied = [m["path"] for m in cfg["modifiche"]]
    unique_names(supplied)
    require(set(supplied) == allowed, "Occorre allineare tutti e soli i file di governo previsti")
    values = {k: cfg[k] for k in ("scope", "nota", "prossima_azione", "verbale", "data")}
    for edit in cfg["modifiche"]:
        path = inside(ROOT, edit["path"])
        require(path not in frozen_paths, "Non si modifica un input congelato durante la registrazione")
        old = path.read_bytes()
        text = old.decode("utf-8")
        require(edit["prima"] and text.count(edit["prima"]) == 1, "Testo atteso non univoco: " + edit["path"])
        replacement = edit["dopo"]
        for key, value in values.items():
            replacement = replacement.replace("{{" + key + "}}", value)
        require(not re.search(r"\{\{[^}]+\}\}", replacement), "Segnaposto non risolto")
        updated = text.replace(edit["prima"], replacement, 1)
        if path == sheet_path:
            for field in ("giro_g6", "max_giri", "snapshot_sha256", "agente"):
                original_field = re.search(rf"(?m)^{field}: .+$", sheet)[0]
                require(original_field in updated, "Campo protetto della scheda alterato: " + field)
            updated = re.sub(r"(?m)^stato: IN-CORSO\s*$", "stato: CHIUSO", updated, count=1)
            updated = re.sub(r"(?m)^gate: .+$", "gate: {" + ", ".join(f"G{i}: OK" for i in range(8)) + "}", updated, count=1)
            require(re.search(r"(?m)^stato: CHIUSO$", updated) and re.search(r"(?m)^gate: \{G0: OK", updated),
                    "Stato/gate della scheda non aggiornabili")
            updated = re.sub(r"(?m)^prossimo_passo: .+$", "prossimo_passo: " + json.dumps(cfg["prossima_azione"], ensure_ascii=False),
                             updated, count=1)
        changes.append((path, old, updated.encode("utf-8")))
    if cfg.get("master"):
        path = ROOT.parent / "_registro-verifica-conformita.csv"
        old = path.read_bytes()
        master = list(csv.DictReader(io.StringIO(old.decode("utf-8-sig")), delimiter=";"))
        edit = cfg["master"]
        found = [r for r in master if r["id"] == edit["id"] and r["id"].startswith(ROOT.name)]
        require(len(found) == 1, "Riga master non univoca o estranea al progetto")
        require(set(edit["attesi"]) == set(edit["valori"]) <= set(found[0]), "Campi master non validi")
        require(all(found[0][k] == v for k, v in edit["attesi"].items()), "Master cambiato dopo la preparazione")
        found[0].update(edit["valori"])
        stream = io.StringIO(newline="")
        writer = csv.DictWriter(stream, fieldnames=list(master[0]), delimiter=";")
        writer.writeheader(); writer.writerows(master)
        changes.append((path, old, stream.getvalue().encode("utf-8-sig")))
    else:
        require(cfg.get("master_non_pertinente"), "Dichiarare aggiornamento master o motivo di non pertinenza")
    summary = {"fase": "PIANO", "scope": cfg["scope"], "righe": row_ids,
               "file": [str(p.relative_to(ROOT.parent)) for p, _, _ in changes],
               "nota": "Giudizio di V già presente; nessun nuovo giudizio emesso dallo script"}
    if not apply:
        return summary
    receipt = Path(config_path).resolve().with_suffix(".eseguito.json")
    require(not receipt.exists(), "Registrazione già tentata: controllare ricevuta e delta, non ripetere alla cieca")
    # Tutte le precondizioni precedono qualsiasi scrittura. Ricevuta conservata anche se un controllo finale fallisce.
    receipt_data = {**summary, "fase": "IN_CORSO", "impronte": [
        {"path": str(p), "prima": hashlib.sha256(a).hexdigest(), "dopo": hashlib.sha256(z).hexdigest()}
        for p, a, z in changes]}
    json_new(receipt, receipt_data)
    for path, old, new in changes:
        require(path.read_bytes() == old, "File cambiato durante la registrazione: " + str(path))
        temporary = path.with_name(path.name + ".vc-nuovo")
        with temporary.open("xb") as stream:
            stream.write(new)
        os.replace(temporary, path)
    if run_checks:
        for script in ("lint-registro-verifica.py",):
            checked = subprocess.run([sys.executable, "-X", "utf8", str(ROOT / "strumenti" / script)],
                                     cwd=ROOT, text=True, encoding="utf-8", capture_output=True)
            require(checked.returncode == 0, f"Registrazioni scritte; controllo {script} fallito: {checked.stdout}{checked.stderr}")
    result = {**receipt_data, "fase": "SCRITTO", "controlli": "OK" if run_checks else "fixture",
              "giornale": "Usare una volta diario/nuova-voce.py con nota e prossima_azione del JSON"}
    receipt.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return result


def prepare(config_path, destination):
    import fitz

    config_path, destination = Path(config_path).resolve(), Path(destination).resolve()
    cfg = read_json(config_path)
    require(not destination.exists(), "Destinazione già esistente: usare una nuova revisione")
    target = (config_path.parent / cfg["target"]).resolve()
    cleaned = clean_target(target)
    require(cleaned.strip(), "Target normativo vuoto")
    canone = neutral_canone()
    sources = {}
    for source in cfg["fonti"]:
        sid = source["id"]
        require(re.fullmatch(r"[a-z0-9_-]+", sid) and sid not in sources, "ID fonte duplicato/non valido")
        pdf = (config_path.parent / source["pdf"]).resolve()
        require(sha(pdf) == source["sha256"].lower(), f"Hash fonte errato: {sid}")
        pages = source["pagine"]
        with fitz.open(pdf) as document:
            require(pages and all(type(p) is int and 1 <= p <= len(document) for p in pages), "Pagine PDF non valide")
        require(len(set(pages)) == len(pages), "Pagina fonte duplicata")
        sources[sid] = {**source, "pdf": str(pdf)}
    require(sources, "Nessuna fonte")
    all_pages, all_lines, blocks = [], [], []
    for block in cfg["blocchi"]:
        bid = block["id"]
        require(re.fullmatch(r"[a-z0-9_-]+", bid), "ID blocco non valido")
        text, line_ids = slice_lines(cleaned, block["righe"])
        require(text.strip(), "Blocco privo di testo normativo")
        pages = block["pagine"]
        require(pages and isinstance(block["limiti"], str) and block["limiti"].strip(), "Pagine o limiti mancanti")
        for key in pages:
            sid, page = key.split(":")
            require(sid in sources and int(page) in sources[sid]["pagine"], f"Pagina fuori scope: {key}")
            require(key == f"{sid}:{int(page)}", "Identificativo pagina non canonico")
        assets = []
        for name in re.findall(r"!\[[^\]]*\]\(([^)]+)\)", text):
            name = name.removeprefix("./")
            portable(name)
            path = inside(target.parent, name)
            assets.append({"name": name, "source": str(path), "sha256": sha(path)})
        assets = list({a["name"]: a for a in assets}.values())
        for asset in block.get("assets", []):
            require(isinstance(asset, dict), "Asset esplicito non valido")
            name = asset.get("name")
            source = asset.get("source")
            expected = asset.get("sha256")
            require(isinstance(name, str) and isinstance(source, str) and
                    isinstance(expected, str) and re.fullmatch(r"[0-9a-fA-F]{64}", expected),
                    "Asset esplicito: servono name, source e sha256")
            portable(name)
            path = (config_path.parent / source).resolve()
            if config_path.is_relative_to(ROOT):
                require(path.is_relative_to(ROOT), "Asset esplicito esterno al progetto: " + name)
            require(sha(path) == expected.lower(), "Hash asset esplicito errato: " + name)
            assets.append({"name": name, "source": str(path), "sha256": expected.lower()})
        unique_names([a["name"] for a in assets])
        unique_names([a["name"] for a in assets] + ["testo.md", "canone.md", "PERIMETRO.md", "input-fonte.json",
                     "inventario.json", "congelamento.json", "input-confronto.json", "ISTRUZIONI-V.md"] +
                     ["fonte-" + key.replace(":", "-") + ".png" for key in pages])
        blocks.append({**block, "target_sha256": digest_text(text), "assets": assets})
        all_pages.extend(pages)
        all_lines.extend(line_ids)
    unique_names([b["id"] for b in blocks])
    expected_pages = [f"{sid}:{p}" for sid, source in sources.items() for p in source["pagine"]]
    require(Counter(all_pages) == Counter(expected_pages), "Copertura pagine incompleta o sovrapposta")
    require(all_lines == list(range(1, len(cleaned.splitlines()) + 1)), "Copertura righe incompleta, sovrapposta o fuori ordine")
    dpi = cfg.get("dpi", 200)
    require(type(dpi) is int and 200 <= dpi <= 1200, "DPI fuori intervallo 200-1200")
    # Tutti i controlli di perimetro precedono le scritture.
    destination.mkdir(parents=True)
    for block in blocks:
        folder = destination / block["id"]
        folder.mkdir()
        write_new(folder / "canone.md", canone)
        write_new(folder / "PERIMETRO.md", f"# Perimetro {cfg['scope']} / {block['id']}\n\n{block['limiti']}\n")
        write_new(folder / "ISTRUZIONI-V.md", V_INSTRUCTIONS)
        for key in block["pagine"]:
            sid, page = key.split(":")
            with fitz.open(sources[sid]["pdf"]) as document:
                document[int(page) - 1].get_pixmap(dpi=dpi).save(folder / ("fonte-" + key.replace(":", "-") + ".png"))
        names = [p.name for p in folder.iterdir() if p.is_file()]
        json_new(folder / "input-fonte.json", {"versione": 2, "schema_inventario": 2,
                                              "pagine": block["pagine"], "files": records(folder, names)})
        block["manifest_fonte_sha256"] = sha(folder / "input-fonte.json")
    plan = {"versione": 1, "scope": cfg["scope"], "target": str(target), "snapshot_sha256": sha(target),
            "clean_sha256": digest_text(cleaned), "procedura_sha256": sha(PROCEDURA), "catalogo_sha256": sha(CATALOGO),
            "fonti": sources, "blocchi": blocks}
    for source in sources.values():
        require(sha(source["pdf"]) == source["sha256"].lower(), "Fonte cambiata durante il render")
    json_new(destination / "coordinamento.json", plan)
    return {"fase": "FONTE", "cartella_coordinatore": str(destination), "blocchi": [b["id"] for b in blocks],
            "nota": "Consegnare a ciascun V solo la sottocartella del suo blocco; nessun target ancora rivelato"}


def reveal(destination, block_id):
    destination = Path(destination).resolve()
    plan = read_json(destination / "coordinamento.json")
    matches = [b for b in plan["blocchi"] if b["id"] == block_id]
    require(len(matches) == 1, "Blocco non trovato")
    block, folder = matches[0], inside(destination, block_id)
    require(not (folder / "testo.md").exists() and not (folder / "congelamento.json").exists(), "Blocco già rivelato/congelato")
    require(sha(folder / "input-fonte.json") == block["manifest_fonte_sha256"], "Manifest fonte cambiato")
    verify_records(folder, read_json(folder / "input-fonte.json")["files"])
    inventory_check(folder)
    inventory = read_json(folder / "inventario.json")
    require(read_json(folder / "input-fonte.json")["pagine"] == block["pagine"], "Mappa fonte incoerente")
    target = Path(plan["target"])
    require(sha(target) == plan["snapshot_sha256"], "Target vivo cambiato dopo la preparazione")
    cleaned = clean_target(target)
    require(digest_text(cleaned) == plan["clean_sha256"], "Depurazione cambiata")
    text, _ = slice_lines(cleaned, block["righe"])
    require(digest_text(text) == block["target_sha256"], "Estratto diverso dal target preparato")
    for asset in block["assets"]:
        require(sha(asset["source"]) == asset["sha256"], "Asset cambiato: " + asset["name"])
        require(not inside(folder, asset["name"]).exists(), "Destinazione asset già presente")
    for source in plan["fonti"].values():
        require(sha(source["pdf"]) == source["sha256"].lower(), "Fonte PDF cambiata dopo la preparazione")
    # La traccia si scrive e si riapre PRIMA di creare testo.md o gli asset.
    freeze = {"versione": 1, "data_utc": datetime.now(timezone.utc).isoformat(), "firma": inventory["firma"],
              "inventario_sha256": sha(folder / "inventario.json"), "esito_provvisorio": inventory["esito_provvisorio"],
              "criterio_canone_sha256": sha(folder / "canone.md"), "manifest_fonte_sha256": sha(folder / "input-fonte.json")}
    json_new(folder / "congelamento.json", freeze)
    require(read_json(folder / "congelamento.json") == freeze, "Congelamento non riletto")
    write_new(folder / "testo.md", text)
    for asset in block["assets"]:
        path = inside(folder, asset["name"])
        path.parent.mkdir(parents=True, exist_ok=True)
        with Path(asset["source"]).open("rb") as source, path.open("xb") as output:
            shutil.copyfileobj(source, output)
        require(sha(path) == asset["sha256"], "Asset cambiato durante la copia")
    names = [p.relative_to(folder).as_posix() for p in folder.rglob("*") if p.is_file()]
    json_new(folder / "input-confronto.json", {"versione": 1, "files": records(folder, names)})
    return verify_package(destination, block_id)


def verify_package(destination, block_id):
    destination = Path(destination).resolve()
    plan = read_json(destination / "coordinamento.json")
    block = next(b for b in plan["blocchi"] if b["id"] == block_id)
    folder = inside(destination, block_id)
    require(sha(folder / "input-fonte.json") == block["manifest_fonte_sha256"], "Manifest fonte cambiato")
    verify_records(folder, read_json(folder / "input-fonte.json")["files"])
    require(sha(folder / "testo.md") == block["target_sha256"], "Testo mancante o diverso dal target: possibile collisione di nomi")
    freeze = read_json(folder / "congelamento.json")
    require(sha(folder / "inventario.json") == freeze["inventario_sha256"], "Inventario congelato alterato")
    require(sha(folder / "canone.md") == freeze["criterio_canone_sha256"], "Canone congelato alterato")
    require(sha(folder / "input-fonte.json") == freeze["manifest_fonte_sha256"], "Fonte congelata alterata")
    comparison = read_json(folder / "input-confronto.json")["files"]
    expected_names = {r["path"] for r in read_json(folder / "input-fonte.json")["files"]}
    expected_names.update({"input-fonte.json", "inventario.json", "congelamento.json", "testo.md"})
    expected_names.update(a["name"] for a in block["assets"])
    require({r["path"] for r in comparison} == expected_names, "Manifest confronto con input omessi o estranei")
    for asset in block["assets"]:
        require(sha(inside(folder, asset["name"])) == asset["sha256"], "Asset diverso dal target preparato")
    count = verify_records(folder, comparison)
    return {"blocco": block_id, "integrita": "OK", "files": count, "giudizio_vc": "NON_EMESSO"}


def make_manifest(root, list_path, output):
    names = read_json(list_path)
    require(isinstance(names, list) and names, "Servono percorsi espliciti, non una cartella ricorsiva")
    root, output = Path(root).resolve(), Path(output).resolve()
    require(all(inside(root, n) != output for n in names), "Il manifest non può includere sé stesso")
    value = {"versione": 1, "files": records(root, names)}
    json_new(output, value)
    count = verify_records(root, read_json(output)["files"])
    return {"files": count, "manifest_sha256": sha(output), "integrita": "OK", "giudizio_vc": "NON_EMESSO"}


def usage(folder, contains):
    rows = []
    for path in sorted(Path(folder).glob("*.jsonl")):
        with path.open(encoding="utf-8-sig") as stream:
            meta = json.loads(next(stream))["payload"]
            source = meta.get("source")
            spawn = source.get("subagent", {}).get("thread_spawn", {}) if isinstance(source, dict) else {}
            agent = spawn.get("agent_path", "")
            if not agent or contains not in agent:
                continue
            latest, model, effort, prior, reset = None, None, None, 0, False
            for line in stream:
                if "token_count" not in line and "turn_context" not in line:
                    continue
                event = json.loads(line)
                payload = event.get("payload", {})
                if event.get("type") == "turn_context":
                    current = payload.get("model")
                    require(model in (None, current), f"Cambio modello nella sessione {path.name}: separare i periodi")
                    model, effort = current, payload.get("effort")
                if event.get("type") == "event_msg" and payload.get("type") == "token_count" and payload.get("info"):
                    total = payload["info"]["total_token_usage"]
                    reset |= total["total_tokens"] < prior
                    latest, prior = total, total["total_tokens"]
            require(not reset, f"Contatore cumulativo decrescente in {path.name}: aggregazione non sicura")
            if latest:
                require(latest["input_tokens"] >= latest.get("cached_input_tokens", 0), "Cache maggiore degli ingressi")
                rows.append({"sessione": meta.get("id"), "agente": agent, "modello": model, "ragionamento": effort, **latest})
    require(rows, "Nessuna sessione figlia corrispondente")
    require(len({r["sessione"] for r in rows}) == len(rows), "Sessione duplicata: non sommare due copie dello stesso log")
    fields = ("input_tokens", "cached_input_tokens", "output_tokens", "reasoning_output_tokens", "total_tokens")
    return {"perimetro": "sole sessioni figlie corrispondenti; coordinatori esclusi", "sessioni": len(rows),
            "totali": {k: sum(r.get(k, 0) for r in rows) for k in fields}, "dettaglio": rows,
            "nota": "Cache inclusa negli input; reasoning incluso negli output. Non è un costo API né una quota di abbonamento."}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    state = commands.add_parser("stato", help="Legge una sola riga del CSV")
    state.add_argument("scope")
    start = commands.add_parser("avvio", help="Riga, lucchetto e soli estratti pertinenti, senza scritture")
    start.add_argument("scope", nargs="?")
    take = commands.add_parser("prendi", help="Prende più righe naturali con un solo lucchetto di sezione")
    take.add_argument("config")
    take.add_argument("--applica", action="store_true")
    sync = commands.add_parser("sincronizza-titoli", help="Allinea i titoli delle sole righe IN-CORSO al target vivo")
    sync.add_argument("config")
    sync.add_argument("--applica", action="store_true")
    inv = commands.add_parser("valida-inventario", help="Controlla il formato prima del congelamento, senza target")
    inv.add_argument("blocco")
    g6 = commands.add_parser("valida-g6", help="Controlla copertura ID e formato del rapporto, senza giudicare la fonte")
    g6.add_argument("blocco")
    g6.add_argument("rapporto")
    close = commands.add_parser("registra", help="Prepara/allinea i registri dopo G7 positivo, senza modificare input verificati")
    close.add_argument("config")
    close.add_argument("--applica", action="store_true")
    prep = commands.add_parser("prepara", help="Crea blocchi con sole fonti, senza target")
    prep.add_argument("config")
    prep.add_argument("destinazione")
    for name in ("rivela", "verifica-pacchetto"):
        cmd = commands.add_parser(name)
        cmd.add_argument("cartella")
        cmd.add_argument("blocco")
    manifest = commands.add_parser("manifest")
    manifest.add_argument("radice")
    manifest.add_argument("lista")
    manifest.add_argument("output")
    verify = commands.add_parser("verifica-manifest")
    verify.add_argument("radice")
    verify.add_argument("manifest")
    verify.add_argument("--congelati", action="store_true", help="Solo dipendenze procedurali storiche già congelate nel manifest")
    costs = commands.add_parser("consumi")
    costs.add_argument("cartella_log")
    costs.add_argument("--contiene", required=True, help="Filtro identificativo del ruolo, es. _343")
    args = parser.parse_args()
    try:
        if args.command == "stato":
            with (ROOT / "registro-verifica-conformita-ntc2018.csv").open(encoding="utf-8-sig", newline="") as stream:
                result = [r for r in csv.DictReader(stream, delimiter=";") if r["paragrafo"].casefold() == args.scope.casefold()]
            require(len(result) == 1, "Scope non univoco o assente nel registro")
            result = result[0]
        elif args.command == "avvio":
            result = bootstrap(args.scope)
        elif args.command == "prendi":
            result = take_scope(args.config, args.applica)
        elif args.command == "sincronizza-titoli":
            result = sync_titles(args.config, args.applica)
        elif args.command == "valida-inventario":
            result = inventory_check(args.blocco)
        elif args.command == "valida-g6":
            result = g6_check(args.blocco, args.rapporto)
        elif args.command == "registra":
            result = registration(args.config, args.applica)
        elif args.command == "prepara":
            result = prepare(args.config, args.destinazione)
        elif args.command == "rivela":
            result = reveal(args.cartella, args.blocco)
        elif args.command == "verifica-pacchetto":
            result = verify_package(args.cartella, args.blocco)
        elif args.command == "manifest":
            result = make_manifest(args.radice, args.lista, args.output)
        elif args.command == "verifica-manifest":
            result = verify_historical(args.radice, args.manifest) if args.congelati else {
                "files": verify_records(args.radice, read_json(args.manifest)["files"]), "integrita": "OK", "giudizio_vc": "NON_EMESSO"}
        else:
            result = usage(args.cartella_log, args.contiene)
    except (ValueError, OSError, KeyError, StopIteration, TypeError) as error:
        parser.exit(1, f"ERRORE VC: {error}\n")
    print(json.dumps(result, ensure_ascii=False))


if __name__ == "__main__":
    main()
