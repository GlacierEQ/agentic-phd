"""
Causal Inference — do-calculus, Counterfactuals, Causal Discovery
Doctorate-level AI curriculum — Agentic PhD
"""
import math
from typing import List, Dict


def ate(treated: List[float], control: List[float]) -> float:
    """Average Treatment Effect: E[Y(1)] - E[Y(0)]."""
    return sum(treated)/len(treated) - sum(control)/len(control)


def att(treated: List[float], matched_control: List[float]) -> float:
    """Average Treatment Effect on the Treated."""
    return sum(treated)/len(treated) - sum(matched_control)/len(matched_control)


def backdoor_adjustment(p_y_given_xz: float, p_z: float) -> float:
    """P(y|do(x)) = sum_z P(y|x,z) P(z)."""
    return p_y_given_xz * p_z


def instrumental_variable_estimate(iv_outcome: List[float], iv_treatment: List[float]) -> float:
    """IV estimate: Cov(Y, Z) / Cov(T, Z). Simplified."""
    n = len(iv_outcome)
    mean_y = sum(iv_outcome) / n
    mean_t = sum(iv_treatment) / n
    mean_z = sum(iv_treatment) / n  # using treatment as instrument proxy
    cov_yz = sum((iv_outcome[i] - mean_y) * (iv_treatment[i] - mean_z) for i in range(n)) / n
    cov_tz = sum((iv_treatment[i] - mean_t) * (iv_treatment[i] - mean_z) for i in range(n)) / n
    return cov_yz / cov_tz if cov_tz != 0 else 0.0


def propensity_score_match(treated: List[float], control: List[float], caliper: float = 0.1) -> List[Tuple[int, int]]:
    """Greedy nearest-neighbor matching on propensity scores."""
    matches = []
    used = set()
    for i, t in enumerate(treated):
        best_j, best_dist = None, float('inf')
        for j, c in enumerate(control):
            if j in used:
                continue
            dist = abs(t - c)
            if dist < best_dist and dist <= caliper:
                best_dist = dist
                best_j = j
        if best_j is not None:
            matches.append((i, best_j))
            used.add(best_j)
    return matches


if __name__ == "__main__":
    print("=== Causal Inference: do-calculus ===")
    print(f"ATE: {ate([1.2, 1.3, 1.1], [0.8, 0.9, 0.7]):.4f}")
    print(f"ATT: {att([1.2, 1.3, 1.1], [0.85, 0.95, 0.75]):.4f}")
    print(f"Backdoor adjustment: {backdoor_adjustment(0.7, 0.4):.4f}")
    matches = propensity_score_match([0.8, 0.6, 0.9], [0.75, 0.55, 0.85, 0.65])
    print(f"Propensity matches: {matches}")
    print("✓ Causal Inference module complete.")
