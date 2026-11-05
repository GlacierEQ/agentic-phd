"""
Complexity Theory — P vs NP, Reductions, Game Theory
Doctorate-level AI curriculum — Agentic PhD
"""
import math
from typing import List, Set, Tuple


def is_prime_trial(n: int) -> bool:
    """O(sqrt(n)) primality test."""
    if n < 2:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True


def fibonacci_naive(n: int) -> int:
    """O(2^n) — exponential, demonstrates intractability."""
    if n <= 1:
        return n
    return fibonacci_naive(n - 1) + fibonacci_naive(n - 2)


def fibonacci_dp(n: int) -> int:
    """O(n) — dynamic programming."""
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b


def subset_sum_exists(nums: List[int], target: int) -> bool:
    """NP-complete subset sum (exponential brute force)."""
    n = len(nums)
    for mask in range(1 << n):
        s = sum(nums[i] for i in range(n) if mask & (1 << i))
        if s == target:
            return True
    return False


def nash_equilibrium_2x2(payoff_a: List[List[float]], payoff_b: List[List[float]]) -> List[Tuple[int, int]]:
    """Find pure strategy Nash equilibria in 2x2 games."""
    equilibria = []
    for i in range(2):
        for j in range(2):
            # i's best response to j
            a_best = max(range(2), key=lambda ii: payoff_a[ii][j])
            b_best = max(range(2), key=lambda jj: payoff_b[i][jj])
            if a_best == i and b_best == j:
                equilibria.append((i, j))
    return equilibria


def shapley_value(players: List[int], v: Callable, i: int) -> float:
    """Shapley value for player i."""
    from itertools import permutations
    n = len(players)
    total = 0.0
    for perm in permutations(players):
        idx = perm.index(i)
        predecessors = set(perm[:idx])
        marginal = v(predecessors | {i}) - v(predecessors)
        total += marginal / math.factorial(n)
    return total


if __name__ == "__main__":
    print("=== Complexity Theory ===")
    print(f"Is 97 prime? {is_prime_trial(97)}")
    print(f"Fibonacci(30) naive: (skipped, exponential)")
    print(f"Fibonacci(30) DP: {fibonacci_dp(30)}")
    print(f"Subset sum [3,34,4,12,5,2] target 9: {subset_sum_exists([3,34,4,12,5,2], 9)}")
    # Prisoner's dilemma
    pa = [[-1, -3], [0, -2]]
    pb = [[-1, 0], [-3, -2]]
    ne = nash_equilibrium_2x2(pa, pb)
    print(f"Nash equilibria (PD): {ne}")
    # Shapley value
    def v(S):
        return 1.0 if len(S) >= 2 else 0.0
    sv = shapley_value([0, 1, 2], v, 0)
    print(f"Shapley value player 0: {sv:.4f}")
    print("✓ Complexity Theory module complete.")
