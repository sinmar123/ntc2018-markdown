"""Test comportamentali degli errori di confezionamento e contabilità VC.

Usa solo fixture sintetiche in TemporaryDirectory, nessuna VC reale.
"""
import importlib.util
import json
import csv
import io
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

import fitz

SPEC = importlib.util.spec_from_file_location("vc_supporto", Path(__file__).with_name("vc-supporto.py"))
VC = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(VC)


class SupportoTest(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix="vc-supporto-test-")
        self.root = Path(self.temp.name)
        self.pdf = self.root / "fonte.pdf"
        with fitz.open() as pdf:
            for n in (1, 2):
                pdf.new_page(width=200, height=200).insert_text((10, 30), f"Fonte sintetica pagina {n}")
            pdf.save(self.pdf)
        self.target = self.root / "norma.md"
        self.target.write_text("# Norma sintetica\n\nUn testo da confrontare.\n", encoding="utf-8")
        self.config = self.root / "config.json"
        self.destination = self.root / "pacchetti"
        self.cfg = {"scope": "prova", "target": "norma.md",
                    "fonti": [{"id": "ntc", "pdf": "fonte.pdf", "sha256": VC.sha(self.pdf), "pagine": [1, 2]}],
                    "blocchi": [{"id": "b01", "pagine": ["ntc:1", "ntc:2"], "righe": [[1, 3]],
                                 "limiti": "Intere pagine della fonte sintetica."}]}
        self.save_config()

    def tearDown(self):
        self.temp.cleanup()

    def save_config(self):
        self.config.write_text(json.dumps(self.cfg), encoding="utf-8")

    def prepare(self):
        return VC.prepare(self.config, self.destination)

    def inventory(self):
        value = {"firma": "V/test", "esito_provvisorio": "LEGGIBILE", "esclusioni": [],
                 "elementi": [{"id": "p1", "pagina": "ntc:1", "riferimento": "titolo e capoverso"},
                              {"id": "p2", "pagina": "ntc:2", "riferimento": "capoverso"}]}
        (self.destination / "b01/inventario.json").write_text(json.dumps(value), encoding="utf-8")

    def test_source_only_then_freeze_before_target(self):
        result = self.prepare()
        folder = self.destination / "b01"
        self.assertEqual(result["fase"], "FONTE")
        self.assertFalse((folder / "testo.md").exists())
        self.assertFalse((folder / "congelamento.json").exists())
        self.inventory()
        original = VC.write_new

        def observe(path, text):
            if Path(path).name == "testo.md":
                self.assertTrue((folder / "congelamento.json").is_file())
            return original(path, text)

        with patch.object(VC, "write_new", side_effect=observe):
            answer = VC.reveal(self.destination, "b01")
        self.assertEqual(answer["integrita"], "OK")
        self.assertEqual(answer["giudizio_vc"], "NON_EMESSO")
        self.assertEqual((folder / "testo.md").read_text(encoding="utf-8"), VC.clean_target(self.target))

    def test_no_reveal_without_inventory(self):
        self.prepare()
        with self.assertRaises(FileNotFoundError):
            VC.reveal(self.destination, "b01")
        self.assertFalse((self.destination / "b01/testo.md").exists())

    def test_missing_markdown_even_with_rewritten_manifest(self):
        self.prepare()
        self.inventory()
        VC.reveal(self.destination, "b01")
        folder = self.destination / "b01"
        (folder / "testo.md").write_text("# PERIMETRO\n", encoding="utf-8")
        manifest = VC.read_json(folder / "input-confronto.json")
        manifest["files"] = VC.records(folder, [r["path"] for r in manifest["files"]])
        (folder / "input-confronto.json").write_text(json.dumps(manifest), encoding="utf-8")
        with self.assertRaisesRegex(ValueError, "diverso dal target"):
            VC.verify_package(self.destination, "b01")

    def test_inventory_cannot_omit_source_page(self):
        self.prepare()
        self.inventory()
        path = self.destination / "b01/inventario.json"
        inv = VC.read_json(path)
        inv["elementi"].pop()
        path.write_text(json.dumps(inv), encoding="utf-8")
        with self.assertRaisesRegex(ValueError, "tutte le pagine"):
            VC.reveal(self.destination, "b01")

    def test_changed_target_cannot_be_revealed(self):
        self.prepare()
        self.inventory()
        self.target.write_text("# Un altro snapshot\n", encoding="utf-8")
        with self.assertRaisesRegex(ValueError, "Target vivo cambiato"):
            VC.reveal(self.destination, "b01")

    def test_wrong_source_hash_blocks_before_creating_directory(self):
        self.cfg["fonti"][0]["sha256"] = "0" * 64
        self.save_config()
        with self.assertRaisesRegex(ValueError, "Hash fonte errato"):
            self.prepare()
        self.assertFalse(self.destination.exists())

    def test_line_gap_and_page_overlap_block_preparation(self):
        self.cfg["blocchi"][0]["righe"] = [[1, 2]]
        self.save_config()
        with self.assertRaisesRegex(ValueError, "Copertura righe"):
            self.prepare()
        self.cfg["blocchi"][0]["righe"] = [[1, 3]]
        self.cfg["blocchi"][0]["pagine"].append("ntc:2")
        self.save_config()
        with self.assertRaisesRegex(ValueError, "Collisione|Copertura pagine"):
            self.prepare()
        self.assertFalse(self.destination.exists())

    def test_case_collisions_and_paths_outside_root_rejected(self):
        with self.assertRaisesRegex(ValueError, "Collisione"):
            VC.unique_names(["scope.md", "SCOPE.md"])
        for name in ("../segreto.md", "C:/file", "cartella/CON.txt", "file. "):
            with self.assertRaises(ValueError):
                VC.inside(self.root, name)

    def test_asset_revealed_only_after_freeze_and_checked(self):
        asset = self.root / "img/fig.png"
        asset.parent.mkdir()
        asset.write_bytes(b"fixture asset")
        self.target.write_text("# Norma sintetica\n\n![Figura](img/fig.png)\n", encoding="utf-8")
        self.prepare()
        self.assertFalse((self.destination / "b01/img").exists())
        self.inventory()
        VC.reveal(self.destination, "b01")
        revealed = self.destination / "b01/img/fig.png"
        self.assertEqual(VC.sha(revealed), VC.sha(asset))
        revealed.write_bytes(b"alterato")
        with self.assertRaisesRegex(ValueError, "Asset diverso"):
            VC.verify_package(self.destination, "b01")

    def test_explicit_target_evidence_is_hidden_until_freeze_and_hash_checked(self):
        render = self.root / "render-target.pdf"
        render.write_bytes(b"fixture render canonico")
        self.cfg["blocchi"][0]["assets"] = [{"name": "resa-target/render.pdf",
                                                  "source": "render-target.pdf",
                                                  "sha256": VC.sha(render)}]
        self.save_config()
        self.prepare()
        folder = self.destination / "b01"
        self.assertFalse((folder / "resa-target").exists())
        self.assertNotIn("render-target.pdf", (folder / "input-fonte.json").read_text(encoding="utf-8"))
        self.inventory()
        VC.reveal(self.destination, "b01")
        revealed = folder / "resa-target/render.pdf"
        self.assertEqual(VC.sha(revealed), VC.sha(render))
        manifest = VC.read_json(folder / "input-confronto.json")
        self.assertIn("resa-target/render.pdf", {r["path"] for r in manifest["files"]})

    def test_explicit_target_evidence_wrong_hash_blocks_before_writes(self):
        render = self.root / "render-target.png"
        render.write_bytes(b"fixture render canonico")
        self.cfg["blocchi"][0]["assets"] = [{"name": "resa-target/render.png",
                                                  "source": "render-target.png",
                                                  "sha256": "0" * 64}]
        self.save_config()
        with self.assertRaisesRegex(ValueError, "Hash asset esplicito"):
            self.prepare()
        self.assertFalse(self.destination.exists())

    def test_frozen_inventory_and_manifest_membership_checked(self):
        self.prepare()
        self.inventory()
        VC.reveal(self.destination, "b01")
        folder = self.destination / "b01"
        path = folder / "input-confronto.json"
        manifest = VC.read_json(path)
        manifest["files"] = [r for r in manifest["files"] if r["path"] != "testo.md"]
        path.write_text(json.dumps(manifest), encoding="utf-8")
        with self.assertRaisesRegex(ValueError, "omessi o estranei"):
            VC.verify_package(self.destination, "b01")

    def test_manifest_is_verified_and_never_overwritten(self):
        listing = self.root / "lista.json"
        listing.write_text('["norma.md", "fonte.pdf"]', encoding="utf-8")
        manifest = self.root / "manifest.json"
        result = VC.make_manifest(self.root, listing, manifest)
        self.assertEqual(result["files"], 2)
        self.assertEqual(result["manifest_sha256"], VC.sha(manifest))
        with self.assertRaises(FileExistsError):
            VC.make_manifest(self.root, listing, manifest)
        self.target.write_text("alterato", encoding="utf-8")
        with self.assertRaisesRegex(ValueError, "non coincidente"):
            VC.verify_records(self.root, VC.read_json(manifest)["files"])

    def test_neutral_canone_keeps_all_rules_without_scope_examples(self):
        canone = VC.neutral_canone()
        for phrase in ("600 dpi", "non tocca cifre", "Mai tolto", "testate", "corpo",
                       "risoluzione nativa", "non applicabilità documentata dei codepoint"):
            self.assertIn(phrase, canone)
        self.assertNotIn("Casi noti", canone)
        self.assertNotIn("Caso noto", canone)
        self.assertNotIn("AF-3.3-", canone)
        self.assertNotIn("C4.1.10", canone)
        import re
        self.assertEqual(len(re.findall(r"(?m)^\d+\. ", canone)), 18)

    def test_usage_uses_last_counter_and_excludes_parent(self):
        for sid, source in (("child", {"subagent": {"thread_spawn": {"agent_path": "/root/prova"}}}), ("parent", "cli")):
            events = [{"payload": {"id": sid, "source": source}},
                      {"type": "turn_context", "payload": {"model": "test", "effort": "medium"}}]
            for total in (100, 200, 200):
                events.append({"type": "event_msg", "payload": {"type": "token_count", "info": {"total_token_usage":
                               {"input_tokens": total - 10, "cached_input_tokens": 80, "output_tokens": 10,
                                "reasoning_output_tokens": 3, "total_tokens": total}}}})
            (self.root / f"{sid}.jsonl").write_text("\n".join(json.dumps(e) for e in events), encoding="utf-8")
        result = VC.usage(self.root, "prova")
        self.assertEqual(result["sessioni"], 1)
        self.assertEqual(result["totali"]["total_tokens"], 200)
        self.assertEqual(result["totali"]["output_tokens"], 10)

    def test_usage_refuses_decreasing_cumulative_counter(self):
        events = [{"payload": {"id": "child", "source": {
            "subagent": {"thread_spawn": {"agent_path": "/root/prova"}}}}}]
        for total in (200, 100):
            events.append({"type": "event_msg", "payload": {"type": "token_count",
                          "info": {"total_token_usage": {"input_tokens": total - 10,
                          "output_tokens": 10, "total_tokens": total}}}})
        (self.root / "child.jsonl").write_text("\n".join(json.dumps(e) for e in events), encoding="utf-8")
        with self.assertRaisesRegex(ValueError, "decrescente"):
            VC.usage(self.root, "prova")

    def test_usage_refuses_duplicate_sessions(self):
        events = [{"payload": {"id": "same-id", "source": {
            "subagent": {"thread_spawn": {"agent_path": "/root/prova"}}}}},
            {"type": "event_msg", "payload": {"type": "token_count", "info": {
            "total_token_usage": {"input_tokens": 90, "output_tokens": 10, "total_tokens": 100}}}}]
        for name in ("originale.jsonl", "copia.jsonl"):
            (self.root / name).write_text("\n".join(json.dumps(e) for e in events), encoding="utf-8")
        with self.assertRaisesRegex(ValueError, "Sessione duplicata"):
            VC.usage(self.root, "prova")

    def test_invalid_inventory_can_be_fixed_before_freeze_without_repackaging(self):
        self.prepare(); self.inventory()
        folder = self.destination / "b01"
        self.assertTrue((folder / "ISTRUZIONI-V.md").is_file())
        inv = VC.read_json(folder / "inventario.json")
        inv["elementi"][0]["riferimento_puntuale"] = inv["elementi"][0].pop("riferimento")
        (folder / "inventario.json").write_text(json.dumps(inv), encoding="utf-8")
        with self.assertRaisesRegex(ValueError, "riferimento"):
            VC.inventory_check(folder)
        self.assertFalse((folder / "congelamento.json").exists())
        self.assertFalse((folder / "testo.md").exists())
        self.inventory()
        self.assertEqual(VC.reveal(self.destination, "b01")["integrita"], "OK")

    def test_duplicate_inventory_ids_block_reveal(self):
        self.prepare(); self.inventory()
        p = self.destination / "b01/inventario.json"
        inv = VC.read_json(p); inv["elementi"][1]["id"] = "p1"
        p.write_text(json.dumps(inv), encoding="utf-8")
        with self.assertRaisesRegex(ValueError, "ID"):
            VC.reveal(self.destination, "b01")
        self.assertFalse((p.parent / "testo.md").exists())

    def test_g6_compact_report_must_cover_all_ids_and_have_zero_open_findings(self):
        self.prepare(); self.inventory(); VC.reveal(self.destination, "b01")
        folder = self.destination / "b01"; p = folder / "rapporto-g6.json"
        report = {"firma": "V/test", "esito": "OK", "coperti": ["p1"], "rilievi": []}
        p.write_text(json.dumps(report), encoding="utf-8")
        with self.assertRaisesRegex(ValueError, "Copertura"):
            VC.g6_check(folder, p)
        report["coperti"].append("p2"); report["rilievi"] = [{"classe": "DUBBIO"}]
        p.write_text(json.dumps(report), encoding="utf-8")
        with self.assertRaisesRegex(ValueError, "rilievi aperti"):
            VC.g6_check(folder, p)
        report["rilievi"] = []; p.write_text(json.dumps(report), encoding="utf-8")
        self.assertEqual(VC.g6_check(folder, p)["coperti"], 2)

    def test_historical_resolution_uses_exact_frozen_procedure_never_target(self):
        proc = self.root / "PROCEDURA-VC.md"; proc.write_text("revisione 1", encoding="utf-8")
        frozen = self.root / "PROCEDURA-VC-congelata.md"; frozen.write_bytes(proc.read_bytes())
        listing = self.root / "lista.json"
        listing.write_text(json.dumps(["PROCEDURA-VC.md", frozen.name, "norma.md"]), encoding="utf-8")
        manifest = self.root / "manifest.json"; VC.make_manifest(self.root, listing, manifest)
        proc.write_text("revisione 2", encoding="utf-8")
        with self.assertRaises(ValueError):
            VC.verify_records(self.root, VC.read_json(manifest)["files"])
        answer = VC.verify_historical(self.root, manifest)
        self.assertEqual(len(answer["riferimenti_storici"]), 1)
        self.target.write_text("target modificato", encoding="utf-8")
        with self.assertRaises(ValueError):
            VC.verify_historical(self.root, manifest)

    def registration_fixture(self):
        row = {"paragrafo": "prova", "titolo": "Norma sintetica", "n.": "1", "apri_md": "norma.md",
               "pagine_pdf_ntc": "1-2", "pagine_pdf_circolare": "", "stato_vc": "IN-CORSO",
               "data_ultima_vc": "", "prossima_azione": "Completare", "evidenza_vc": "", "note": ""}
        registry = self.root / "registro-verifica-conformita-ntc2018.csv"
        with registry.open("w", encoding="utf-8-sig", newline="") as stream:
            writer = csv.DictWriter(stream, fieldnames=list(row), delimiter=";"); writer.writeheader(); writer.writerow(row)
        (self.root / "strumenti").mkdir()
        (self.root / "strumenti/lint-registro-verifica.py").write_bytes((VC.ROOT / "strumenti/lint-registro-verifica.py").read_bytes())
        changes = []
        for name in ["README.md", "TODO.md", "CHANGELOG.md", "indice-ntc2018.md",
                     "verifica-conformita/scheda-scope-ntc2018-prova.md"]:
            p = self.root / name; p.parent.mkdir(exist_ok=True)
            p.write_text("stato: IN-CORSO\nagente: CDX\ngiro_g6: 1\nmax_giri: 3\ngate: {G7: IN_CORSO}\nprossimo_passo: Finire\nsnapshot_sha256: "
                         + VC.sha(self.target) + "\nPrima\n", encoding="utf-8")
            changes.append({"path": name, "prima": "Prima", "dopo": "{{nota}}"})
        listing = self.root / "lista.json"; listing.write_text('["norma.md"]', encoding="utf-8")
        manifest = self.root / "manifest.json"; VC.make_manifest(self.root, listing, manifest)
        report = self.root / "g7.json"
        report.write_text(json.dumps({"giudizio_g7": "OK", "scope": "prova", "firma": "V indipendente",
             "gate": {f"G{i}": "OK" for i in range(8)}, "rilievi_aperti": [],
             "snapshot_sha256": VC.sha(self.target), "manifest_sha256": VC.sha(manifest)}), encoding="utf-8")
        verbale = self.root / "verbale.md"; verbale.write_text("Esito già giudicato da V", encoding="utf-8")
        cfg = {"scope": "prova", "agente": "CDX", "g7": "g7.json", "g7_sha256": VC.sha(report),
               "manifest": "manifest.json", "verbale": "verbale.md", "verbale_sha256": VC.sha(verbale),
               "data": "2026-09-05", "nota": "Verifica conclusa: qualità e fedeltà", "prossima_azione": "nessuna",
               "modifiche": changes, "master_non_pertinente": "fixture senza master"}
        path = self.root / "chiusura.json"; path.write_text(json.dumps(cfg), encoding="utf-8")
        return path, cfg, registry

    def test_registration_plan_and_apply_preserve_accents_and_target(self):
        config, cfg, registry = self.registration_fixture(); original = registry.read_bytes(); target = VC.sha(self.target)
        with patch.object(VC, "ROOT", self.root):
            self.assertEqual(VC.registration(config)["fase"], "PIANO")
            self.assertEqual(original, registry.read_bytes())
            result = VC.registration(config, True, run_checks=False)
            self.assertEqual(result["fase"], "SCRITTO")
            self.assertIn("qualità e fedeltà", (self.root / "README.md").read_text(encoding="utf-8"))
            self.assertEqual(VC.sha(self.target), target)
            self.assertIn("stato: CHIUSO", (self.root / "verifica-conformita/scheda-scope-ntc2018-prova.md").read_text(encoding="utf-8"))

            self.assertEqual(VC.read_json(config.with_suffix(".eseguito.json"))["fase"], "SCRITTO")
            with self.assertRaises(ValueError):
                VC.registration(config, True, run_checks=False)

    def test_registration_adds_procedure_without_relabeling_history(self):
        config, cfg, registry = self.registration_fixture()
        sheet = self.root / "verifica-conformita/scheda-scope-ntc2018-prova.md"
        sheet.write_text("procedura: VC-NTC/4\n" + sheet.read_text(encoding="utf-8"), encoding="utf-8")
        with registry.open(encoding="utf-8-sig", newline="") as stream:
            rows = list(csv.DictReader(stream, delimiter=";"))
        historical = {**rows[0], "paragrafo": "storico", "stato_vc": "VC-OK", "note": "nota; conservata"}
        with registry.open("w", encoding="utf-8-sig", newline="") as stream:
            writer = csv.DictWriter(stream, fieldnames=list(rows[0]), delimiter=";")
            writer.writeheader(); writer.writerows(rows + [historical])
        before = registry.read_bytes()
        cfg["procedura_vc"] = "VC-NTC/3 - semplificata"
        config.write_text(json.dumps(cfg), encoding="utf-8")
        with patch.object(VC, "ROOT", self.root):
            with self.assertRaisesRegex(ValueError, "Procedura VC diversa"):
                VC.registration(config, True, run_checks=False)
            self.assertEqual(registry.read_bytes(), before)
            self.assertFalse(config.with_suffix(".eseguito.json").exists())
            cfg["procedura_vc"] = "VC-NTC/4 - semplificata"
            config.write_text(json.dumps(cfg), encoding="utf-8")
            VC.registration(config, True, run_checks=False)
        with registry.open(encoding="utf-8-sig", newline="") as stream:
            actual = list(csv.DictReader(stream, delimiter=";"))
        self.assertEqual(actual[0]["procedura_vc"], "VC-NTC/4 - semplificata")
        self.assertEqual(actual[0]["agente_vc"], "Codex (CDX)")
        self.assertEqual(actual[1], {**historical, "procedura_vc": "", "agente_vc": ""})
        self.assertEqual(len(actual[0]), 13)

    def test_registration_attributes_other_agent_only_from_matching_sheet(self):
        config, cfg, registry = self.registration_fixture()
        with registry.open(encoding="utf-8-sig", newline="") as stream:
            rows = list(csv.DictReader(stream, delimiter=";"))
        historical = {**rows[0], "paragrafo": "8.1", "stato_vc": "VC-OK", "note": "GROK; conservata"}
        with registry.open("w", encoding="utf-8-sig", newline="") as stream:
            writer = csv.DictWriter(stream, fieldnames=list(rows[0]), delimiter=";")
            writer.writeheader(); writer.writerows(rows + [historical])
        evidence = self.root / "verifica-conformita/scheda-scope-ntc2018-8.1.md"
        evidence.write_text("agente: GROK\n", encoding="utf-8")
        before = registry.read_bytes()
        cfg["agenti_vc_da_schede"] = {"8.1": "CC"}
        config.write_text(json.dumps(cfg), encoding="utf-8")
        with patch.object(VC, "ROOT", self.root):
            with self.assertRaisesRegex(ValueError, "Agente VC diverso dalla scheda"):
                VC.registration(config, True, run_checks=False)
            self.assertEqual(registry.read_bytes(), before)
            cfg["agenti_vc_da_schede"] = {"8.1": "GROK"}
            config.write_text(json.dumps(cfg), encoding="utf-8")
            VC.registration(config, True, run_checks=False)
        with registry.open(encoding="utf-8-sig", newline="") as stream:
            actual = list(csv.DictReader(stream, delimiter=";"))
        self.assertEqual(actual[1], {**historical, "procedura_vc": "", "agente_vc": "Grok (GROK)"})

    def test_registration_rejects_stale_government_before_any_write(self):
        config, cfg, registry = self.registration_fixture(); original = registry.read_bytes()
        (self.root / "TODO.md").write_text("Modifica concorrente", encoding="utf-8")
        with patch.object(VC, "ROOT", self.root), self.assertRaisesRegex(ValueError, "non univoco"):
            VC.registration(config, True, run_checks=False)
        self.assertEqual(registry.read_bytes(), original)
        self.assertFalse(config.with_suffix(".eseguito.json").exists())

    def test_registration_rejects_nonpositive_g7_and_changed_snapshot(self):
        config, cfg, registry = self.registration_fixture(); original = registry.read_bytes()
        report = self.root / "g7.json"; data = VC.read_json(report); data["gate"]["G6"] = "KO"
        report.write_text(json.dumps(data), encoding="utf-8"); cfg["g7_sha256"] = VC.sha(report)
        config.write_text(json.dumps(cfg), encoding="utf-8")
        with patch.object(VC, "ROOT", self.root), self.assertRaisesRegex(ValueError, "non tutti OK"):
            VC.registration(config, True, run_checks=False)
        self.assertEqual(registry.read_bytes(), original)
        data["gate"]["G6"] = "OK"; report.write_text(json.dumps(data), encoding="utf-8")
        cfg["g7_sha256"] = VC.sha(report); config.write_text(json.dumps(cfg), encoding="utf-8")
        self.target.write_text("Modificato", encoding="utf-8")
        with patch.object(VC, "ROOT", self.root), self.assertRaises(ValueError):
            VC.registration(config, True, run_checks=False)
        self.assertEqual(registry.read_bytes(), original)

    def test_bootstrap_does_not_open_a_closed_or_ambiguous_scope(self):
        config, cfg, registry = self.registration_fixture()
        for name in ("README.md", "TODO.md", "CHANGELOG.md"):
            (self.root / name).write_text("# Titolo\n\n## Corrente\nScope prova.\n", encoding="utf-8")
        before = registry.read_bytes()
        with patch.object(VC, "ROOT", self.root):
            result = VC.bootstrap()
            self.assertEqual(result["registro"]["paragrafo"], "prova")
            self.assertEqual(registry.read_bytes(), before)
            registry.write_bytes(before.replace(b"IN-CORSO", b"VC-OK"))
            self.assertEqual(VC.bootstrap()["selezione"], "NON_UNIVOCA")
            # Una richiesta esplicita legge lo stato chiuso senza riaprirlo.
            self.assertEqual(VC.bootstrap("prova")["registro"]["stato_vc"], "VC-OK")

    def test_registration_rejects_other_agent_and_counter_change(self):
        config, cfg, registry = self.registration_fixture(); original = registry.read_bytes()
        cfg["agente"] = "ALTRO"; config.write_text(json.dumps(cfg), encoding="utf-8")
        with patch.object(VC, "ROOT", self.root), self.assertRaisesRegex(ValueError, "altro agente"):
            VC.registration(config, True, run_checks=False)
        cfg["agente"] = "CDX"
        cfg["modifiche"][-1].update(prima="giro_g6: 1", dopo="giro_g6: 0")
        config.write_text(json.dumps(cfg), encoding="utf-8")
        with patch.object(VC, "ROOT", self.root), self.assertRaisesRegex(ValueError, "protetto"):
            VC.registration(config, True, run_checks=False)
        self.assertEqual(registry.read_bytes(), original)

    def test_take_aggregate_scope_updates_all_rows_and_creates_one_lock(self):
        fields = ["paragrafo", "titolo", "n.", "apri_md", "pagine_pdf_ntc", "pagine_pdf_circolare",
                  "stato_vc", "data_ultima_vc", "prossima_azione", "evidenza_vc", "note"]
        rows = [
            {**dict.fromkeys(fields, ""), "paragrafo": "3.5.1", "titolo": "Uno", "n.": "1",
             "apri_md": "uno.md", "stato_vc": "MAI-FATTA", "prossima_azione": "Avviare la VC."},
            {**dict.fromkeys(fields, ""), "paragrafo": "3.5.2", "titolo": "Due", "n.": "2",
             "apri_md": "due.md", "stato_vc": "MAI-FATTA", "prossima_azione": "Avviare la VC."},
        ]
        registry = self.root / "registro-verifica-conformita-ntc2018.csv"
        (self.root / "uno.md").write_text("# 3.5.1. TITOLO UNO\n", encoding="utf-8")
        (self.root / "due.md").write_text("# 3.5.2. TITOLO DUE\n", encoding="utf-8")
        with registry.open("w", encoding="utf-8-sig", newline="") as stream:
            writer = csv.DictWriter(stream, fieldnames=fields, delimiter=";"); writer.writeheader(); writer.writerows(rows)
        cfg = {"scope": "3.5", "righe": ["3.5.1", "3.5.2"], "agente": "HRM",
               "scheda": "verifica-conformita/scheda-scope-ntc2018-3.5.md",
               "scheda_contenuto": "---\nscope_id: ntc2018-3.5\nstato: IN-CORSO\nagente: HRM\n---\n",
               "prossima_azione": "Completare G0-G5.", "nota": "Scope aggregato autorizzato."}
        config = self.root / "presa.json"; config.write_text(json.dumps(cfg), encoding="utf-8")
        before = registry.read_bytes()
        with patch.object(VC, "ROOT", self.root):
            self.assertEqual(VC.take_scope(config)["fase"], "PIANO")
            self.assertEqual(registry.read_bytes(), before)
            self.assertFalse((self.root / cfg["scheda"]).exists())
            result = VC.take_scope(config, apply=True, run_checks=False)
        self.assertEqual(result["fase"], "SCRITTO")
        with registry.open(encoding="utf-8-sig", newline="") as stream:
            actual = list(csv.DictReader(stream, delimiter=";"))
        self.assertEqual([r["stato_vc"] for r in actual], ["IN-CORSO", "IN-CORSO"])
        self.assertTrue((self.root / cfg["scheda"]).is_file())
        self.assertTrue(config.with_suffix(".eseguito.json").is_file())
        (self.root / "strumenti").mkdir(exist_ok=True)
        (self.root / "strumenti/lint-registro-verifica.py").write_bytes(
            (VC.ROOT / "strumenti/lint-registro-verifica.py").read_bytes())
        sync = self.root / "sincronizza.json"; sync.write_text(json.dumps({
            "scope": "3.5", "righe": ["3.5.1", "3.5.2"], "agente": "HRM"}), encoding="utf-8")
        with patch.object(VC, "ROOT", self.root):
            plan = VC.sync_titles(sync)
            self.assertEqual(plan["titoli_aggiornati"], 2)
            VC.sync_titles(sync, apply=True, run_checks=False)
        with registry.open(encoding="utf-8-sig", newline="") as stream:
            actual = list(csv.DictReader(stream, delimiter=";"))
        self.assertEqual([r["titolo"] for r in actual], ["TITOLO UNO", "TITOLO DUE"])

    def test_take_disjoint_scope_preserves_active_scope_and_rejects_shared_target(self):
        fields = ["paragrafo", "apri_md", "stato_vc", "prossima_azione", "evidenza_vc", "note"]
        active = dict.fromkeys(fields, "")
        active.update(paragrafo="8.1", apri_md="active.md", stato_vc="IN-CORSO", note="Altro agente")
        pending = dict.fromkeys(fields, "")
        pending.update(paragrafo="3.1", apri_md="active.md", stato_vc="MAI-FATTA")
        registry = self.root / "registro-verifica-conformita-ntc2018.csv"
        for name in ("active.md", "pending.md"):
            (self.root / name).write_text("Testo\n", encoding="utf-8")
        def save():
            with registry.open("w", encoding="utf-8-sig", newline="") as stream:
                writer = csv.DictWriter(stream, fieldnames=fields, delimiter=";")
                writer.writeheader(); writer.writerows([active, pending])
        cfg = {"scope": "3.1", "righe": ["3.1"], "agente": "CDX",
               "scheda": "verifica-conformita/scheda-scope-ntc2018-3.1.md",
               "scheda_contenuto": "---\nscope_id: ntc2018-3.1\nstato: IN-CORSO\nagente: CDX\n---\n",
               "prossima_azione": "Confrontare", "nota": "Autorizzato"}
        config = self.root / "presa-disgiunta.json"
        config.write_text(json.dumps(cfg), encoding="utf-8")
        save(); before = registry.read_bytes()
        with patch.object(VC, "ROOT", self.root):
            with self.assertRaisesRegex(ValueError, "Target condiviso"):
                VC.take_scope(config, apply=True, run_checks=False)
            self.assertEqual(registry.read_bytes(), before)
            self.assertFalse((self.root / cfg["scheda"]).exists())
            self.assertFalse(config.with_suffix(".eseguito.json").exists())
            pending["apri_md"] = "pending.md"; save()
            VC.take_scope(config, apply=True, run_checks=False)
        with registry.open(encoding="utf-8-sig", newline="") as stream:
            actual = list(csv.DictReader(stream, delimiter=";"))
        self.assertEqual(actual[0], active)
        self.assertEqual(actual[1]["stato_vc"], "IN-CORSO")

    def test_registration_accepts_aggregate_scope_manifest_and_updates_all_rows(self):
        config, cfg, registry = self.registration_fixture()
        with registry.open(encoding="utf-8-sig", newline="") as stream:
            rows = list(csv.DictReader(stream, delimiter=";"))
            fields = list(rows[0])
        rows[0].update({"paragrafo": "3.5.1", "titolo": "Vecchio uno", "n.": "1"})
        second = dict(rows[0])
        second.update({"paragrafo": "3.5.2", "titolo": "Vecchio due", "n.": "2",
                       "apri_md": "p2-target.md"})
        (self.root / "p2-target.md").write_text("# 3.5.2. TITOLO DUE\n\nTesto.\n", encoding="utf-8")
        rows.append(second)
        buffer = io.StringIO(newline="")
        writer = csv.DictWriter(buffer, fieldnames=fields, delimiter=";", lineterminator="\n")
        writer.writeheader(); writer.writerows(rows)
        registry.write_bytes(b"\xef\xbb\xbf" + buffer.getvalue().encode("utf-8"))
        manifest = self.root / "snapshot-scope.json"
        manifest.write_text(json.dumps({"files": VC.records(self.root, ["norma.md", "p2-target.md"])}), encoding="utf-8")
        snapshot = VC.sha(manifest)
        final_list = self.root / "lista-finale.json"
        final_list.write_text(json.dumps(["norma.md", "p2-target.md", "snapshot-scope.json"]), encoding="utf-8")
        final_manifest = self.root / "manifest-finale.json"
        VC.make_manifest(self.root, final_list, final_manifest)
        g7 = json.loads((self.root / "g7.json").read_text(encoding="utf-8"))
        g7.update({"scope": "3.5", "snapshot_sha256": snapshot,
                   "manifest_sha256": VC.sha(final_manifest)})
        (self.root / "g7.json").write_text(json.dumps(g7), encoding="utf-8")
        old_sheet = self.root / "verifica-conformita/scheda-scope-ntc2018-prova.md"
        new_sheet = self.root / "verifica-conformita/scheda-scope-ntc2018-3.5.md"
        text = old_sheet.read_text(encoding="utf-8").replace(VC.sha(self.target), snapshot)
        new_sheet.write_text(text, encoding="utf-8"); old_sheet.unlink()
        for edit in cfg["modifiche"]:
            if edit["path"] == "verifica-conformita/scheda-scope-ntc2018-prova.md":
                edit["path"] = "verifica-conformita/scheda-scope-ntc2018-3.5.md"
        cfg.update({"scope": "3.5", "righe": ["3.5.1", "3.5.2"],
                    "g7_sha256": VC.sha(self.root / "g7.json"), "manifest": "manifest-finale.json",
                    "snapshot_manifest": "snapshot-scope.json", "snapshot_sha256": snapshot})
        config.write_text(json.dumps(cfg), encoding="utf-8")
        with patch.object(VC, "ROOT", self.root):
            plan = VC.registration(config, False, run_checks=False)
            self.assertEqual(plan["righe"], ["3.5.1", "3.5.2"])
            VC.registration(config, True, run_checks=False)
        with registry.open(encoding="utf-8-sig", newline="") as stream:
            updated = list(csv.DictReader(stream, delimiter=";"))
        self.assertEqual([row["stato_vc"] for row in updated], ["VC-OK", "VC-OK"])
        self.assertEqual(updated[1]["titolo"], "TITOLO DUE")


if __name__ == "__main__":
    unittest.main()
