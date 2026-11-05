"""
Experimentation — Reproducible Experiments, Ablation Studies
Doctorate-level AI curriculum — Agentic PhD
"""
import json
import hashlib
import random
from datetime import datetime, timezone
from typing import List, Dict


class ExperimentLog:
    """Track experiments with reproducibility metadata."""

    def __init__(self):
        self.experiments: List[Dict] = []

    def log(self, name: str, params: Dict, metrics: Dict, seed: int = 42, code_hash: str = ""):
        exp = {
            "name": name, "params": params, "metrics": metrics,
            "seed": seed, "code_hash": code_hash,
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "param_hash": hashlib.sha256(json.dumps(params, sort_keys=True).encode()).hexdigest()[:12],
        }
        self.experiments.append(exp)
        return exp

    def best(self, metric: str, higher_is_better: bool = True) -> Dict:
        if not self.experiments:
            return {}
        return (max if higher_is_better else min)(self.experiments, key=lambda e: e["metrics"].get(metric, 0))

    def compare(self, metric: str) -> List[Dict]:
        return sorted(self.experiments, key=lambda e: e["metrics"].get(metric, 0), reverse=True)

    def ablation(self, base_name: str, ablated: str, metric: str) -> Dict:
        base = next((e for e in self.experiments if e["name"] == base_name), None)
        abl = next((e for e in self.experiments if e["name"] == ablated), None)
        if not base or not abl:
            return {}
        delta = abl["metrics"].get(metric, 0) - base["metrics"].get(metric, 0)
        return {"base": base["metrics"].get(metric), "ablated": abl["metrics"].get(metric), "delta": delta, "significant": abs(delta) > 0.01}


class ReproducibilityChecker:
    """Check reproducibility of experiments."""

    def __init__(self):
        self.checks: List[Dict] = []

    def check(self, name: str, condition: bool, detail: str = ""):
        self.checks.append({"name": name, "passed": condition, "detail": detail})

    def summary(self) -> Dict:
        passed = sum(1 for c in self.checks if c["passed"])
        return {"total": len(self.checks), "passed": passed, "failed": len(self.checks) - passed, "all_passed": passed == len(self.checks)}


if __name__ == "__main__":
    print("=== Experimentation: Reproducibility ===")
    log = ExperimentLog()
    log.log("baseline", {"lr": 0.001, "batch": 32}, {"accuracy": 0.85, "f1": 0.82}, seed=42)
    log.log("improved", {"lr": 0.0005, "batch": 64}, {"accuracy": 0.91, "f1": 0.89}, seed=42)
    log.log("no_attention", {"lr": 0.0005, "batch": 64, "attention": False}, {"accuracy": 0.83, "f1": 0.80}, seed=42)
    print(f"Best by accuracy: {log.best('accuracy')['name']}")
    abl = log.ablation("improved", "no_attention", "accuracy")
    print(f"Ablation (remove attention): {abl}")
    rc = ReproducibilityChecker()
    rc.check("seed_fixed", True, "seed=42 used")
    rc.check("code_hashed", False, "code hash not recorded")
    print(f"Reproducibility: {rc.summary()}")
    print("✓ Experimentation module complete.")
