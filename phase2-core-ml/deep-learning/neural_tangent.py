"""
Deep Learning Theory — Neural Tangent Kernel, Double Descent
Doctorate-level AI curriculum — Agentic PhD
"""
import math
from typing import List


def ntk_kernel(x: float, y: float) -> float:
    """NTK kernel for ReLU: (1/2pi)(sin(theta) + (pi-theta)cos(theta))."""
    if abs(x) < 1e-12 or abs(y) < 1e-12:
        return 0.0
    cos_theta = (x * y) / (abs(x) * abs(y))
    cos_theta = max(-1.0, min(1.0, cos_theta))
    theta = math.acos(cos_theta)
    return (1.0 / (2 * math.pi)) * (math.sin(theta) + (math.pi - theta) * cos_theta)


def double_descent_risk(n_params: int, n_samples: int, noise: float = 0.1) -> float:
    """Simplified double descent: risk peaks at n_params ≈ n_samples."""
    ratio = n_params / n_samples
    if abs(ratio - 1.0) < 0.01:
        return 10.0  # interpolation threshold peak
    return noise * (1 + 1 / abs(ratio - 1.0)) if ratio != 1.0 else 10.0


def grokking_loss(train_loss: float, val_loss: float, epoch: int, grok_epoch: int = 1000) -> Tuple[float, float]:
    """Simulate grokking: train loss drops fast, val loss drops late."""
    if epoch < grok_epoch:
        return (0.01, 1.0)  # memorization phase
    progress = (epoch - grok_epoch) / grok_epoch
    val = 1.0 * math.exp(-2 * progress)
    return (0.01, max(0.01, val))


def universal_approximation_error(width: int, depth: int) -> float:
    """Approximation error decreases with width and depth."""
    return 1.0 / (width * depth)


if __name__ == "__main__":
    print("=== Deep Learning Theory: NTK, Double Descent, Grokking ===")
    print(f"NTK kernel K(1.0, 0.5): {ntk_kernel(1.0, 0.5):.6f}")
    for np_ in [50, 100, 101, 200]:
        print(f"  Double descent (params={np_}, samples=100): {double_descent_risk(np_, 100):.4f}")
    tl, vl = grokking_loss(0.01, 1.0, 500)
    print(f"  Grokking (epoch 500): train={tl:.4f}, val={vl:.4f}")
    tl, vl = grokking_loss(0.01, 1.0, 1500)
    print(f"  Grokking (epoch 1500): train={tl:.4f}, val={vl:.4f}")
    print(f"Universal approx error (w=100, d=5): {universal_approximation_error(100, 5):.6f}")
    print("✓ Deep Learning Theory module complete.")
