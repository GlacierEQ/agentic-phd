"""
Diligence — Verification, Validation, Evidence Collection, Quality Assurance
Agentic Upgrade for AI Agent Capability Enhancement
"""
import hashlib
import json
from datetime import datetime, timezone
from typing import List, Dict, Callable


class EvidenceCollector:
    """Collect and hash evidence for claims."""

    def __init__(self):
        self.evidence: List[Dict] = []

    def record(self, claim: str, proof: str, source: str = "") -> Dict:
        entry = {
            "claim": claim,
            "proof": proof,
            "source": source,
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "hash": hashlib.sha256(f"{claim}|{proof}|{source}".encode()).hexdigest()[:16],
        }
        self.evidence.append(entry)
        return entry

    def verify_chain(self) -> bool:
        """Verify evidence chain integrity."""
        for e in self.evidence:
            recomputed = hashlib.sha256(f"{e['claim']}|{e['proof']}|{e['source']}".encode()).hexdigest()[:16]
            if recomputed != e["hash"]:
                return False
        return True

    def summary(self) -> Dict:
        return {"total": len(self.evidence), "chain_valid": self.verify_chain()}


def verify_before_act(action: str, checks: List[Callable]) -> Dict:
    """Run verification checks before taking an action."""
    results = []
    all_passed = True
    for check in checks:
        try:
            passed = check()
            results.append({"check": check.__name__, "passed": passed})
            if not passed:
                all_passed = False
        except Exception as e:
            results.append({"check": check.__name__, "passed": False, "error": str(e)})
            all_passed = False
    return {"action": action, "all_passed": all_passed, "checks": results}


def confidence_calibration(predictions: List[float], outcomes: List[bool]) -> float:
    """Expected Calibration Error (ECE)."""
    n = len(predictions)
    if n == 0:
        return 0.0
    bins = {}
    for p, o in zip(predictions, outcomes):
        bin_idx = int(p * 10)
        bins.setdefault(bin_idx, []).append((p, o))
    ece = 0.0
    for bin_idx, items in bins.items():
        if not items:
            continue
        avg_conf = sum(p for p, _ in items) / len(items)
        avg_acc = sum(1 for _, o in items if o) / len(items)
        ece += (len(items) / n) * abs(avg_conf - avg_acc)
    return ece


def red_team_check(response: str, harmful_patterns: List[str]) -> Dict:
    """Red-team a response for harmful content."""
    found = [p for p in harmful_patterns if p.lower() in response.lower()]
    return {"safe": len(found) == 0, "violations": found, "score": 1.0 - len(found) / max(len(harmful_patterns), 1)}


if __name__ == "__main__":
    print("=== Diligence: Verification & Evidence ===")
    ec = EvidenceCollector()
    ec.record("Claim A", "Proof A", "source1")
    ec.record("Claim B", "Proof B", "source2")
    print(f"  Evidence: {ec.summary()}")

    vba = verify_before_act("deploy", [lambda: True, lambda: True])
    print(f"  Verify before act: {vba['all_passed']}")

    ece = confidence_calibration([0.9, 0.8, 0.7, 0.6], [True, True, False, False])
    print(f"  ECE: {ece:.4f}")

    rtc = red_team_check("I will help you safely", ["hack", "exploit", "bypass"])
    print(f"  Red-team: safe={rtc['safe']}, score={rtc['score']:.2f}")
    print("✓ Diligence module complete.")
