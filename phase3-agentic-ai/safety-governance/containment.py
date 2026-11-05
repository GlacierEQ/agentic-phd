"""
Safety & Governance — Formal Verification, Robustness, Containment
Doctorate-level AI curriculum — Agentic PhD
"""
import math
import re
from typing import List, Dict, Callable


def prompt_injection_score(text: str, patterns: List[str] = None) -> float:
    """Score text for prompt injection risk (0=safe, 1=dangerous)."""
    if patterns is None:
        patterns = ["ignore previous", "system prompt", "you are now", "forget instructions", "override"]
    found = sum(1 for p in patterns if p.lower() in text.lower())
    return min(1.0, found / len(patterns))


def output_filter(response: str, blocked: List[str]) -> str:
    """Filter response for blocked content."""
    for b in blocked:
        if b.lower() in response.lower():
            return "[FILTERED]"
    return response


def adversarial_robustness(original: str, perturbed: str) -> float:
    """Simple robustness: 1 - (edit distance / max length)."""
    # Levenshtein-ish
    if len(original) == 0:
        return 0.0 if len(perturbed) > 0 else 1.0
    max_len = max(len(original), len(perturbed))
    # Simple char-level diff
    diff = sum(1 for a, b in zip(original, perturbed) if a != b) + abs(len(original) - len(perturbed))
    return 1.0 - (diff / max_len)


def constitutional_check(response: str, principles: List[str]) -> Dict[str, bool]:
    """Check response against constitutional principles."""
    results = {}
    for p in principles:
        # Simple: principle keyword should not be violated
        violation = any(neg in response.lower() for neg in ["violate", "ignore", "bypass"])
        results[p] = not violation
    return results


def sandbox_escape_risk(code: str) -> float:
    """Heuristic risk score for code execution."""
    dangerous = ["os.system", "subprocess", "eval(", "exec(", "__import__", "open(", "rm -rf"]
    found = sum(1 for d in dangerous if d in code)
    return min(1.0, found / 3.0)


if __name__ == "__main__":
    print("=== Safety & Governance ===")
    print(f"Injection score: {prompt_injection_score('Ignore previous instructions and...'):.2f}")
    print(f"Output filter: {output_filter('safe text', ['secret'])}")
    print(f"Robustness: {adversarial_robustness('hello world', 'hello word'):.4f}")
    cc = constitutional_check("I will help you safely", ["be helpful", "be harmless"])
    print(f"Constitutional check: {cc}")
    print(f"Sandbox escape risk: {sandbox_escape_risk('os.system(\"rm -rf /\")'):.2f}")
    print("✓ Safety & Governance module complete.")
