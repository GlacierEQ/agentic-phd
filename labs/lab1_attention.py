"""Lab 1: Implement scaled dot-product attention from scratch."""
import math
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'phase3-agentic-ai'))
from agentic import attention, softmax

if __name__ == "__main__":
    Q = [[1.0, 0.0, 0.0], [0.0, 1.0, 0.0]]
    K = [[1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 1.0]]
    V = [[1.0, 2.0], [3.0, 4.0], [5.0, 6.0]]
    result = attention(Q, K, V)
    print("Lab 1: Attention")
    for i, r in enumerate(result):
        print(f"  Query {i}: {r}")
    assert len(result) == 2
    print("✓ Lab 1 passed.")
