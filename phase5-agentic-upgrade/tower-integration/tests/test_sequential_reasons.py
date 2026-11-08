"""Tests for the sequential reasoning module."""

import importlib.util
import sys
import unittest
from pathlib import Path

# The sequential module lives under a hyphenated, non-importable directory,
# so load it by absolute path.
_REPO_ROOT = Path(__file__).resolve().parents[3]
_SEQUENTIAL_PATH = (
    _REPO_ROOT / "phase5-agentic-upgrade" / "sequential-thinking" / "sequential_reasons.py"
)
if not _SEQUENTIAL_PATH.exists():
    raise FileNotFoundError(f"Sequential module not found: {_SEQUENTIAL_PATH}")
_spec = importlib.util.spec_from_file_location("agentic_phd_sequential_reasons", _SEQUENTIAL_PATH)
if _spec is None or _spec.loader is None:
    raise ImportError(f"Cannot load sequential module from: {_SEQUENTIAL_PATH}")
_seq = importlib.util.module_from_spec(_spec)
sys.modules.setdefault(_spec.name, _seq)
_spec.loader.exec_module(_seq)
SequentialReasoner = _seq.SequentialReasoner
run_reasoning = _seq.run_reasoning


class SequentialReasonsTests(unittest.TestCase):
    def test_reasoner_creation(self):
        r = SequentialReasoner()
        self.assertIsNotNone(r)
        self.assertTrue(r.unique_id)

    def test_reason_success(self):
        result = run_reasoning(
            problem="What is 2+2?",
            steps=[
                "Define the problem: calculate 2+2",
                "Evaluate the arithmetic expression",
                "Verify the result is correct",
            ],
        )
        self.assertEqual(result.total_steps, 3)
        self.assertTrue(result.verification_summary)
        self.assertTrue(result.final_answer)
        self.assertGreaterEqual(result.elapsed_seconds, 0)

    def test_reason_output_is_not_empty(self):
        result = run_reasoning(
            problem="Test purpose",
            steps=["Check that output is non-empty", "Verify the output length"],
        )
        self.assertGreater(len(str(result.final_answer)), 0)

    def test_reason_step_structure(self):
        result = run_reasoning(
            problem="Structure test",
            steps=["Step one", "Step two", "Step three"],
        )
        self.assertEqual(len(result.steps), 3)
        for step in result.steps:
            self.assertGreaterEqual(step.step_number, 1)
            self.assertIsNotNone(step.verified)
            self.assertGreaterEqual(step.confidence, 0)
            self.assertLessEqual(step.confidence, 1)
            self.assertTrue(step.rationale)

    def test_reason_invalid_steps(self):
        result = run_reasoning(
            problem="",
            steps=[""],
        )
        self.assertGreater(result.total_steps, 0)

    def test_run_reasoning_shortcut(self):
        result = run_reasoning(
            problem="Shortcut test",
            steps=["Test that shortcut works"],
        )
        self.assertTrue(result)
        self.assertTrue(result.steps)

    def test_sequential_reasoner_max_steps(self):
        r = SequentialReasoner(max_steps=5)
        result = r.reason(
            problem="Max steps",
            steps=["s1", "s2", "s3", "s4", "s5", "s6"],
        )
        self.assertLessEqual(result.total_steps, 5)


if __name__ == "__main__":
    unittest.main(verbosity=2)
