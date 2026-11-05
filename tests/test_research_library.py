"""Adversarial verification for research library, source identity and truthful status."""
import json
import tempfile
import unittest
from pathlib import Path
from scripts.validate_research_library import CATALOG, validate


class ResearchLibraryTests(unittest.TestCase):
    def setUp(self):
        self.data = json.loads(CATALOG.read_text(encoding="utf-8"))

    def check_bad(self, modify):
        modified = json.loads(json.dumps(self.data))
        modify(modified)
        with tempfile.TemporaryDirectory() as folder:
            candidate = Path(folder) / "sources.json"
            candidate.write_text(json.dumps(modified), encoding="utf-8")
            with self.assertRaises(ValueError):
                validate(candidate)

    def test_valid_full_catalog(self):
        result = validate()
        self.assertGreaterEqual(result["count"], 30)
        self.assertGreaterEqual(len(result["domains"]), 7)
        self.assertEqual(result["unique_ids"], result["unique_urls"])

    def test_no_duplicate_paper_identity(self):
        self.check_bad(lambda d: d["sources"][1].update(id=d["sources"][0]["id"]))

    def test_no_duplicate_url(self):
        self.check_bad(lambda d: d["sources"][1].update(url=d["sources"][0]["url"]))

    def test_no_untrusted_source_scheme(self):
        self.check_bad(lambda d: d["sources"][0].update(url="http://example.org/fake"))

    def test_no_claim_of_completed_lab(self):
        self.check_bad(lambda d: d["sources"][0].update(implementation_status="PASSED"))

    def test_no_unsupported_review_status(self):
        self.check_bad(lambda d: d["sources"][0].update(review_status="peer_reviewed_by_us"))

    def test_missing_experiment_fails(self):
        self.check_bad(lambda d: d["sources"][0].update(experiment=""))

    def test_domain_coverage_fails_closed(self):
        self.check_bad(lambda d: [s.update(area="single") for s in d["sources"]])


if __name__ == "__main__":
    unittest.main()
