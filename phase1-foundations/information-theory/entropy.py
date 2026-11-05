"""
Information Theory — Entropy & Mutual Information
Doctorate-level AI curriculum — Agentic PhD
"""
import math
from typing import List


def entropy(probs: List[float]) -> float:
    """Shannon entropy H(X) = -sum p_i log2(p_i)."""
    return -sum(p * math.log2(p) for p in probs if p > 0)


def joint_entropy(joint: List[List[float]]) -> float:
    """H(X,Y) = -sum_{x,y} p(x,y) log2 p(x,y)."""
    return -sum(joint[i][j] * math.log2(joint[i][j])
                for i in range(len(joint)) for j in range(len(joint[0])) if joint[i][j] > 0)


def mutual_information(px: List[float], py: List[float], joint: List[List[float]]) -> float:
    """I(X;Y) = H(X) + H(Y) - H(X,Y)."""
    return entropy(px) + entropy(py) - joint_entropy(joint)


def kl_divergence(p: List[float], q: List[float]) -> float:
    """KL(P||Q) = sum p_i log(p_i/q_i)."""
    return sum(p[i] * math.log(p[i] / q[i]) for i in range(len(p)) if p[i] > 0 and q[i] > 0)


def cross_entropy(p: List[float], q: List[float]) -> float:
    """H(P,Q) = -sum p_i log q_i."""
    return -sum(p[i] * math.log(q[i]) for i in range(len(p)) if p[i] > 0 and q[i] > 0)


def channel_capacity_bsc(p: float) -> float:
    """Capacity of binary symmetric channel: C = 1 - H(p)."""
    h = -p * math.log2(p) - (1 - p) * math.log2(1 - p) if 0 < p < 1 else 0.0
    return 1 - h


def rate_distortion_gaussian(sigma2: float, d: float) -> float:
    """Rate-distortion for Gaussian source: R(D) = 0.5 * log2(sigma2/D)."""
    if d <= 0 or d >= sigma2:
        return 0.0
    return 0.5 * math.log2(sigma2 / d)


if __name__ == "__main__":
    print("=== Information Theory ===")
    print(f"Entropy [0.5,0.5]: {entropy([0.5, 0.5]):.4f} bits")
    joint = [[0.25, 0.25], [0.25, 0.25]]
    print(f"Mutual info (independent): {mutual_information([0.5,0.5],[0.5,0.5],joint):.4f}")
    print(f"KL([0.5,0.5]||[0.25,0.75]): {kl_divergence([0.5,0.5],[0.25,0.75]):.4f}")
    print(f"Cross-entropy: {cross_entropy([0.5,0.5],[0.25,0.75]):.4f}")
    print(f"BSC capacity (p=0.1): {channel_capacity_bsc(0.1):.4f}")
    print(f"Rate-distortion (sigma2=1, D=0.1): {rate_distortion_gaussian(1.0, 0.1):.4f}")
    print("✓ Information Theory module complete.")
