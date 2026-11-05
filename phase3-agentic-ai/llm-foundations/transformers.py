"""
LLM Foundations — Transformers, Attention, Scaling Laws
Doctorate-level AI curriculum — Agentic PhD
"""
import math
from typing import List


def softmax(scores: List[float]) -> List[float]:
    exps = [math.exp(s - max(scores)) for s in scores]
    total = sum(exps)
    return [e / total for e in exps]


def scaled_dot_product_attention(Q, K, V):
    """Attention(Q,K,V) = softmax(QK^T / sqrt(dk)) V."""
    dk = len(Q[0]) if Q else 1
    scale = math.sqrt(dk)
    result = []
    for q in Q:
        scores = [sum(q[i] * k[i] for i in range(dk)) / scale for k in K]
        weights = softmax(scores)
        out = [sum(weights[j] * V[j][i] for j in range(len(V))) for i in range(len(V[0]))]
        result.append(out)
    return result


def positional_encoding(pos: int, d_model: int) -> List[float]:
    """Sinusoidal positional encoding."""
    pe = []
    for i in range(d_model):
        if i % 2 == 0:
            pe.append(math.sin(pos / (10000 ** (i / d_model))))
        else:
            pe.append(math.cos(pos / (10000 ** ((i - 1) / d_model))))
    return pe


def scaling_law_loss(N: float, D: float, C: float, alpha: float = 0.34, beta: float = 0.28, gamma: float = 1.0) -> float:
    """Chinchilla scaling: L(N,D) = A/N^alpha + B/D^beta + L_irreducible."""
    A, B, E = 406.4, 410.7, 1.69
    return A / (N ** alpha) + B / (D ** beta) + E


def kv_cache_memory(seq_len: int, n_layers: int, d_model: int, n_heads: int, bytes_per: int = 2) -> int:
    """KV cache memory in bytes."""
    head_dim = d_model // n_heads
    return 2 * n_layers * seq_len * n_heads * head_dim * bytes_per


def rope_encoding(pos: int, dim: int, base: float = 10000.0) -> Tuple:
    """Rotary Position Embedding angles."""
    import math
    angles = []
    for i in range(0, dim, 2):
        theta = pos / (base ** (i / dim))
        angles.append((math.cos(theta), math.sin(theta)))
    return angles


if __name__ == "__main__":
    print("=== LLM Foundations: Transformers ===")
    Q, K, V = [[1.0, 0.0]], [[1.0, 0.0], [0.0, 1.0]], [[1.0, 2.0], [3.0, 4.0]]
    attn = scaled_dot_product_attention(Q, K, V)
    print(f"Attention: {attn}")
    pe = positional_encoding(5, 4)
    print(f"Positional encoding (pos=5, d=4): {[round(x, 4) for x in pe]}")
    loss = scaling_law_loss(1e9, 1e10, 1e20)
    print(f"Scaling law loss (N=1e9, D=1e10): {loss:.4f}")
    mem = kv_cache_memory(4096, 32, 4096, 32)
    print(f"KV cache memory (4096 tokens): {mem / 1e9:.2f} GB")
    print("✓ LLM Foundations module complete.")
