"""Lab 4: Track experiments with reproducibility."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'phase4-research'))
from research import ExperimentLog

if __name__ == "__main__":
    log = ExperimentLog()
    log.log("run1", {"lr": 0.01, "epochs": 10}, {"loss": 0.5, "acc": 0.8})
    log.log("run2", {"lr": 0.001, "epochs": 20}, {"loss": 0.3, "acc": 0.9})
    print("Lab 4: Experiment Tracking")
    best = log.best("acc")
    print(f"  Best: {best['name']} (acc={best['metrics']['acc']})")
    assert best["name"] == "run2"
    print("✓ Lab 4 passed.")
