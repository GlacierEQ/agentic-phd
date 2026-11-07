"""Tests for the sequential reasoning module."""

import importlib
import pytest

# Handle hyphenated package directory names
_seq = importlib.import_module("phase5_agentic_upgrade.sequential_thinking.sequential_reasons")
SequentialReasoner = _seq.SequentialReasoner
run_reasoning = _seq.run_reasoning


def test_reasoner_creation():
    r = SequentialReasoner()
    assert r is not None
    assert r.unique_id


def test_reason_success():
    result = run_reasoning(
        problem="What is 2+2?",
        steps=[
            "Define the problem: calculate 2+2",
            "Evaluate the arithmetic expression",
            "Verify the result is correct",
        ],
    )
    assert result.total_steps == 3
    assert result.verification_summary
    assert result.final_answer
    assert result.elapsed_seconds >= 0


def test_reason_output_is_not_empty():
    result = run_reasoning(
        problem="Test purpose",
        steps=["Check that output is non-empty", "Verify the output length",],
    )
    assert len(str(result.final_answer)) > 0


def test_reason_step_structure():
    result = run_reasoning(
        problem="Structure test",
        steps=["Step one", "Step two", "Step three"],
    )
    assert len(result.steps) == 3
    for step in result.steps:
        assert step.step_number >= 1
        assert step.verified is not None
        assert step.confidence >= 0
        assert step.confidence <= 1
        assert step.rationale


def test_reason_invalid_steps():
    result = run_reasoning(
        problem="",
        steps=[""],
    )
    assert result.total_steps > 0


def test_run_reasoning_shortcut():
    result = run_reasoning(
        problem="Shortcut test",
        steps=["Test that shortcut works"],
    )
    assert result
    assert result.steps


def test_sequential_reasoner_max_steps():
    r = SequentialReasoner(max_steps=5)
    result = r.reason(
        problem="Max steps",
        steps=["s1", "s2", "s3", "s4", "s5", "s6"],
    )
    assert result.total_steps <= 5


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
