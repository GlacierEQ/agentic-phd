"""
Phase 1: Mathematical & Computational Foundations
Doctorate-level AI curriculum — Agentic PhD
"""
import math
import random
from typing import List, Tuple


# ─── 1. Linear Algebra: Spectral Theory ─────────────────────────────────────

def eigenvalues_2x2(a: float, b: float, c: float, d: float) -> Tuple[complex, complex]:
    """Compute eigenvalues of [[a,b],[c,d]]."""
    trace = a + d
    det = a * d - b * c
    disc = trace**2 - 4 * det
    if disc >= 0:
        return ((trace + math.sqrt(disc)) / 2, (trace - math.sqrt(disc)) / 2)
    else:
        real = trace / 2
        imag = math.sqrt(-disc) / 2
        return (complex(real, imag), complex(real, -imag))


def matrix_rank_approx(mat: List[List[float]], tol: float = 1e-9) -> int:
    """Approximate rank via Gaussian elimination."""
    rows = [row[:] for row in mat]
    m, n = len(rows), len(rows[0]) if rows else 0
    rank = 0
    for col in range(n):
        pivot = None
        for r in range(rank, m):
            if abs(rows[r][col]) > tol:
                pivot = r
                break
        if pivot is None:
            continue
        rows[rank], rows[pivot] = rows[pivot], rows[rank]
        pv = rows[rank][col]
        rows[rank] = [x / pv for x in rows[rank]]
        for r in range(m):
            if r != rank and abs(rows[r][col]) > tol:
                factor = rows[r][col]
                rows[r] = [rows[r][j] - factor * rows[rank][j] for j in range(n)]
        rank += 1
        if rank == m:
            break
    return rank


# ─── 2. Probability: Concentration Inequalities ─────────────────────────────

def hoeffding_bound(n: int, epsilon: float, a: float = 0.0, b: float = 1.0) -> float:
    """Hoeffding's inequality: P(|Xbar - E[X]| >= eps) <= 2*exp(-2*n*eps^2/(b-a)^2)."""
    return 2 * math.exp(-2 * n * epsilon**2 / (b - a)**2)


def chernoff_bound(n: int, epsilon: float, p: float) -> float:
    """Chernoff bound for sum of Bernoulli(p) variables."""
    mu = n * p
    if epsilon >= 1:
        return math.exp(-mu * epsilon**2 / 3)
    return math.exp(-mu * epsilon**2 / (2 + epsilon))


# ─── 3. Optimization: Gradient Descent ──────────────────────────────────────

def gradient_descent(f, grad, x0: float, lr: float = 0.1, steps: int = 100) -> float:
    """Simple 1D gradient descent."""
    x = x0
    for _ in range(steps):
        x -= lr * grad(x)
    return x


def sgd_step(params: List[float], grads: List[float], lr: float) -> List[float]:
    """Stochastic gradient descent update."""
    return [p - lr * g for p, g in zip(params, grads)]


# ─── 4. Information Theory ───────────────────────────────────────────────────

def entropy(probs: List[float]) -> float:
    """Shannon entropy H(X) = -sum p_i log2(p_i)."""
    return -sum(p * math.log2(p) for p in probs if p > 0)


def mutual_information(px: List[float], py: List[float], joint: List[List[float]]) -> float:
    """I(X;Y) = H(X) + H(Y) - H(X,Y)."""
    hx = entropy(px)
    hy = entropy(py)
    hxy = -sum(joint[i][j] * math.log2(joint[i][j])
                for i in range(len(px)) for j in range(len(py)) if joint[i][j] > 0)
    return hx + hy - hxy


# ─── 5. Theoretical CS: Complexity ──────────────────────────────────────────

def is_prime(n: int) -> bool:
    """Trial division primality (O(sqrt(n)))."""
    if n < 2:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True


def fibonacci(n: int) -> int:
    """O(2^n) naive recursion — demonstrates exponential complexity."""
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


# ─── Demo ────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    print("=== Phase 1: Mathematical & Computational Foundations ===\n")

    # Linear Algebra
    ev = eigenvalues_2x2(3, 1, 2, 4)
    print(f"Eigenvalues of [[3,1],[2,4]]: {ev}")
    rank = matrix_rank_approx([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    print(f"Rank of singular 3x3 matrix: {rank}")

    # Probability
    hb = hoeffding_bound(1000, 0.05)
    print(f"Hoeffding bound (n=1000, eps=0.05): {hb:.6f}")
    cb = chernoff_bound(100, 0.1, 0.5)
    print(f"Chernoff bound (n=100, eps=0.1, p=0.5): {cb:.6f}")

    # Optimization
    x_opt = gradient_descent(lambda x: x**2, lambda x: 2*x, 5.0, lr=0.1, steps=50)
    print(f"Gradient descent min of x^2 from 5.0: {x_opt:.6f}")

    # Information Theory
    h = entropy([0.5, 0.5])
    print(f"Entropy of fair coin: {h:.4f} bits")
    joint = [[0.25, 0.25], [0.25, 0.25]]
    mi = mutual_information([0.5, 0.5], [0.5, 0.5], joint)
    print(f"Mutual information (independent): {mi:.4f}")

    # Complexity
    print(f"Is 97 prime? {is_prime(97)}")
    print(f"Fibonacci(10) = {fibonacci(10)}")

    print("\n✓ Phase 1 complete.")
