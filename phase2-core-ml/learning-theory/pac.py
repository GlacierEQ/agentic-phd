"""
Learning Theory — PAC, VC Dimension, Rademacher Complexity
Doctorate-level AI curriculum — Agentic PhD
"""
import math
from typing import List, Callable


def pac_sample_complexity(epsilon: float, delta: float, vc_dim: int) -> int:
    """m >= (1/eps)(VCdim*log(1/eps) + log(1/delta))."""
    return math.ceil((1 / epsilon) * (vc_dim * math.log(1 / epsilon) + math.log(1 / delta)))


def vc_dimension_thresholds() -> int:
    """VC dimension of threshold functions on R is 1."""
    return 1


def vc_dimension_intervals() -> int:
    """VC dimension of intervals on R is 2."""
    return 2


def rademacher_complexity(n: int, complexity: float) -> float:
    """Simplified Rademacher complexity bound: R_n(F) <= complexity / sqrt(n)."""
    return complexity / math.sqrt(n)


def generalization_bound(empirical_risk: float, rademacher: float, n: int, delta: float) -> float:
    """Generalization bound: R(f) <= R_emp(f) + 2*R_n(F) + sqrt(log(1/delta)/(2n))."""
    return empirical_risk + 2 * rademacher + math.sqrt(math.log(1 / delta) / (2 * n))


def bias_variance_decomposition(bias2: float, variance: float, noise: float) -> float:
    """Expected prediction error = bias^2 + variance + irreducible noise."""
    return bias2 + variance + noise


if __name__ == "__main__":
    print("=== Learning Theory: PAC, VC, Rademacher ===")
    print(f"PAC sample complexity (eps=0.1, delta=0.05, VCdim=10): {pac_sample_complexity(0.1, 0.05, 10)}")
    print(f"VC dim (thresholds): {vc_dimension_thresholds()}")
    print(f"VC dim (intervals): {vc_dimension_intervals()}")
    rc = rademacher_complexity(1000, 1.0)
    print(f"Rademacher complexity (n=1000): {rc:.6f}")
    gb = generalization_bound(0.1, rc, 1000, 0.05)
    print(f"Generalization bound: {gb:.4f}")
    print(f"Bias-variance (0.04, 0.02, 0.01): {bias_variance_decomposition(0.04, 0.02, 0.01):.4f}")
    print("✓ Learning Theory module complete.")
