"""Regression tests for source-identified coding skill integration and original tracker reuse."""
from __future__ import annotations

import importlib.util
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts/code_intelligence_router.py"
ROUTES = ROOT / "resources/research/code_intelligence_routes.json"
CATALOG = ROOT / "resources/research/frontier_sources.json"
SPEC = importlib.util.spec_from_file_location("code_intelligence_router", SCRIPT)
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


class CodingIntelligenceIntegrationTests(unittest.TestCase):
    def test_uploaded_skill_and_reference_match_pinned_package(self):
        result = MODULE.validate_routes()
        self.assertTrue(result["source_package_hashes_verified"])
        self.assertTrue(result["existing_tracker_reused"])
        self.assertEqual(result["package_version"], "0.1.35")
        self.assertGreaterEqual(result["catalog_sources"], 61)
        self.assertEqual(result["routes"], 7)

    def test_exact_skill_routes_to_canonical_methods(self):
        skill = (ROOT / "skills/code-intelligence/SKILL.md").read_text(encoding="utf-8")
        methods = (ROOT / "references/code-intelligence-methods.md").read_text(encoding="utf-8")
        self.assertIn("name: code-intelligence", skill)
        self.assertIn("references/code-intelligence-methods.md", skill)
        self.assertIn("code:refactor", methods)
        self.assertIn("code:fix", methods)
        self.assertIn("not LLM agent coding intelligence evaluation", methods)

    def test_routes_have_real_research_ids_not_fake_experiments(self):
        for mode in ("symbol_refactor", "state_receipts", "concurrent_effect",
                     "security_flow", "stale_code", "parser_transform", "agent_evaluation"):
            result = MODULE.select_route(mode)
            self.assertEqual(result["mode"], mode)
            self.assertEqual(result["runtime_owner"], "GlacierEQ/pro-code")
            self.assertEqual(result["spiral_owner"], "GlacierEQ/spiral-engine")
            self.assertEqual(result["execution_status"], "research_method_guidance_only_not_executed")
            self.assertTrue(result["method"]["acceptance"])
            self.assertTrue(result["research_sources"])
            for source in result["research_sources"]:
                self.assertEqual(source["implementation_status"], "proposed_lab_not_run")
                self.assertTrue(source["url"].startswith("https://"))

    def test_symbol_routing_is_semantic_not_unscoped_replace(self):
        result = MODULE.select_route("symbol_refactor")
        self.assertIn("code:knowledge", result["method"]["owner_tools"])
        self.assertIn("code:refactor", result["method"]["owner_tools"])
        self.assertIn("C02", result["method"]["source_ids"])
        self.assertIn("same-named", result["method"]["experiment"])

    def test_harness_evaluation_does_not_masquerade_as_model_evaluation(self):
        result = MODULE.select_route("agent_evaluation")
        self.assertIn("eval:harness", result["method"]["owner_tools"])
        self.assertIn("not LLM", result["method"]["risk"])

    def test_cli_select_outputs_research_and_explicit_execution_status(self):
        run = subprocess.run([sys.executable, str(SCRIPT), "select", "parser_transform"],
                             capture_output=True, text=True, check=True)
        result = json.loads(run.stdout)
        self.assertEqual(result["mode"], "parser_transform")
        self.assertIn("C04", result["method"]["source_ids"])
        self.assertTrue(result["research_sources"])
        self.assertEqual(result["execution_status"], "research_method_guidance_only_not_executed")

    def test_cli_rejects_unknown_route(self):
        run = subprocess.run([sys.executable, str(SCRIPT), "select", "magical_autofix"],
                             capture_output=True, text=True)
        self.assertNotEqual(run.returncode, 0)
        self.assertIn("Unknown code-intelligence mode", run.stderr)

    def _invalid(self, mutate):
        data = json.loads(ROUTES.read_text(encoding="utf-8"))
        mutate(data)
        with tempfile.TemporaryDirectory() as folder:
            file = Path(folder) / "routes.json"
            file.write_text(json.dumps(data), encoding="utf-8")
            with self.assertRaises(ValueError):
                MODULE.validate_routes(routes_path=file)

    def test_reject_missing_source(self):
        self._invalid(lambda d: d["routes"][0]["source_ids"].append("C-NOT-A-REAL-SOURCE"))

    def test_reject_duplicate_mode(self):
        self._invalid(lambda d: d["routes"][1].update(mode=d["routes"][0]["mode"]))

    def test_reject_fake_execution_receipt(self):
        self._invalid(lambda d: d.update(execution_status="verified_production"))

    def test_reject_unrecognized_new_tool_instead_of_inventing(self):
        self._invalid(lambda d: d["routes"][0]["owner_tools"].append("model_weights_train"))

    def test_reject_source_path_escape(self):
        self._invalid(lambda d: d["package"].update(skill_path="../outside-repository"))


if __name__ == "__main__":
    unittest.main()
