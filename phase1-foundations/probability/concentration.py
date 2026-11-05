"""
Probability & Statistics — Concentration Inequalities
Doctorate-level AI curriculum — Agentic PhD
"""
import math
from typing import List


def hoeffding_bound(n: int, epsilon: float, a: float = 0.0, b: float = 1.0) -> float:
    """P(|Xbar - E[X]| >= eps) <= 2*exp(-2*n*eps^2/(b-a)^2)."""
    return 2 * math.exp(-2 * n * epsilon**2 / (b - a)**2)


def chernoff_bound(n: int, epsilon: float, p: float) -> float:
    """Chernoff bound for sum of Bernoulli(p)."""
    mu = n * p
    if epsilon >= 1:
        return math.exp(-mu * epsilon**2 / 3)
    return math.exp(-mu * epsilon**2 / (2 + epsilon))


def mcdiarmid_bound(n: int, epsilon: float, c: float) -> float:
    """McDiarmid's inequality for functions with bounded differences."""
    return math.exp(-2 * n * epsilon**2 / (n * c**2)) if c > 0 else 0.0


def kl_divergence_bernoulli(p: float, q: float) -> float:
    """KL(p||q) for Bernoulli distributions."""
    if p == 0:
        return (1 - p) * math.log((1 - p) / (1 - q)) if q < 1 else 0.0
    if p == 1:
        return p * math.log(p / q) if q > 0 else float('inf')
    return p * math.log(p / q) + (1 - p) * math.log((1 - p) / (1 - q))


def sample_complexity_pac(epsilon: float, delta: float, vc_dim: int) -> int:
    """PAC sample complexity: m >= (1/eps)(VCdim*log(1/eps) + log(1/delta))."""
    return math.ceil((1 / epsilon) * (vc_dim * math.log(1 / epsilon) + math.log(1 / delta)))


if __name__ == "__main__":
    print("=== Probability: Concentration Inequalities ===")
    print(f"Hoeffding (n=1000, eps=0.05): {hoeffding_bound(1000, 0.05):.6f}")
    print(f"Chernoff (n=100, eps=0.1, p=0.5): {chernoff_bound(100, 0.1, 0.5):.6f}")
    print(f"McDiarmid (n=50, eps=0.1, c=1): {mcdiarmid_bound(50, 0.1, 1):.6f}")
    print(f"KL(Bernoulli 0.3 || 0.5): {kl_divergence_bernoulli(0.3, 0.5):.6f}")
    print(f"PAC sample complexity (eps=0.1, delta=0.05, VCdim=10): {sample_complexity_pac(0.1, 0.05, 10)}")
    print("✓ Probability module complete.")
