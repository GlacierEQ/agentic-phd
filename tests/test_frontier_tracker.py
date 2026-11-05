"""Existing paper tracker can now retrieve actionable sources without replacing papers."""
from __future__ import annotations
import importlib.util
import json
from pathlib import Path
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "glaciereq_agentic_phd_tracker",
    ROOT / "phase4-research/literature/tracker.py",
)
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


class FrontierTrackerTests(unittest.TestCase):
    def setUp(self):
        self.tracker = MODULE.PaperTracker()

    def test_load_full_catalog_preserves_paper_tracker(self):
        self.tracker.add("Own research", ["Scholar"], "Peer-reviewed", 2026, ["agents"])
        baseline = self.tracker.summary()
        loaded = self.tracker.load_frontier_library()
        self.assertEqual(loaded["loaded"], 40)
        self.assertEqual(len(loaded["domains"]), 7)
        self.assertEqual(self.tracker.summary(), baseline)

    def test_retrieve_source_technique_experiment_and_status(self):
        self.tracker.load_frontier_library()
        candidate = self.tracker.source_by_id("M02")
        self.assertIn("LongMemEval", candidate["title"])
        self.assertTrue(candidate["url"].startswith("https://"))
        self.assertIn("Evaluate", candidate["experiment"])
        self.assertEqual(candidate["implementation_status"], "proposed_lab_not_run")

    def test_search_technique_and_domain_without_mutating_sources(self):
        self.tracker.load_frontier_library()
        results = self.tracker.search_sources("tool", area="Tools and runtime")
        self.assertTrue(results)
        self.assertTrue(all(x["area"] == "Tools and runtime" for x in results))
        self.assertFalse(self.tracker.search_sources(""))

    def test_schema_rejects_unknown_catalog_without_losing_loaded_sources(self):
        self.tracker.load_frontier_library()
        existing = self.tracker.source_by_id("A01")
        with tempfile.TemporaryDirectory() as folder:
            target = Path(folder) / "bad.json"
            target.write_text(json.dumps({"schema": "unknown", "sources": []}))
            with self.assertRaises(ValueError):
                self.tracker.load_frontier_library(target)
        self.assertEqual(self.tracker.source_by_id("A01"), existing)

    def test_duplicate_source_id_fails_closed(self):
        raw = json.loads((ROOT / "resources/research/frontier_sources.json").read_text())
        raw["sources"][1]["id"] = raw["sources"][0]["id"]
        with tempfile.TemporaryDirectory() as folder:
            target = Path(folder) / "bad.json"
            target.write_text(json.dumps(raw))
            with self.assertRaises(ValueError):
                self.tracker.load_frontier_library(target)


if __name__ == "__main__":
    unittest.main()
