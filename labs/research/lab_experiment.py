"""Lab: Experiment tracking and reproducibility."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'phase4-research', 'experimentation'))
from reproducibility import ExperimentLog, ReproducibilityChecker

def main():
    print("Lab: Experiment Tracking")
    log = ExperimentLog()
    log.log("run1", {"lr": 0.01}, {"acc": 0.8}, seed=42)
    log.log("run2", {"lr": 0.001}, {"acc": 0.9}, seed=42)
    best = log.best("acc")
    print(f"  Best: {best['name']} (acc={best['metrics']['acc']})")
    assert best["name"] == "run2"
    rc = ReproducibilityChecker()
    rc.check("seed", True)
    rc.check("hash", True)
    print(f"  Reproducibility: {rc.summary()}")
    print("✓ Lab passed.")

if __name__ == "__main__":
    main()
