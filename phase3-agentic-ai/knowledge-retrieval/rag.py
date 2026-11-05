"""
Knowledge & Retrieval — RAG, GNNs, Neuro-symbolic AI
Doctorate-level AI curriculum — Agentic PhD
"""
import math
from typing import List, Dict, Tuple


def cosine_similarity(a: List[float], b: List[float]) -> float:
    dot = sum(x * y for x, y in zip(a, b))
    na = math.sqrt(sum(x * x for x in a))
    nb = math.sqrt(sum(x * x for x in b))
    return dot / (na * nb) if na > 0 and nb > 0 else 0.0


def retrieve_top_k(query_emb: List[float], doc_embs: List[List[float]], k: int = 3) -> List[int]:
    """Retrieve top-k documents by cosine similarity."""
    scores = [(cosine_similarity(query_emb, de), i) for i, de in enumerate(doc_embs)]
    scores.sort(reverse=True)
    return [i for _, i in scores[:k]]


def rrf_score(rankings: List[List[int]], k: int = 60) -> Dict[int, float]:
    """Reciprocal Rank Fusion across multiple rankings."""
    scores = {}
    for ranking in rankings:
        for rank, doc_id in enumerate(ranking, 1):
            scores[doc_id] = scores.get(doc_id, 0) + 1 / (k + rank)
    return scores


def chunk_text(text: str, chunk_size: int = 512, overlap: int = 50) -> List[str]:
    """Split text into overlapping chunks."""
    chunks = []
    start = 0
    while start < len(text):
        end = start + chunk_size
        chunks.append(text[start:end])
        start = end - overlap
        if start >= len(text):
            break
    return chunks


def gnn_message_passing(node_features: List[List[float]], adjacency: List[List[int]], weights: List[List[float]]) -> List[List[float]]:
    """Simple GNN: h_v' = sigma(W * (h_v + sum_{u in N(v)} h_u))."""
    result = []
    for v in range(len(node_features)):
        agg = list(node_features[v])
        for u in adjacency[v]:
            for i in range(len(agg)):
                agg[i] += node_features[u][i]
        out = [sum(weights[i][j] * agg[j] for j in range(len(agg))) for i in range(len(weights))]
        result.append([1 / (1 + math.exp(-x)) for x in out])  # sigmoid
    return result


if __name__ == "__main__":
    print("=== Knowledge & Retrieval: RAG, GNNs ===")
    q = [1.0, 0.0, 0.0]
    docs = [[1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.5, 0.5, 0.0]]
    top = retrieve_top_k(q, docs, k=2)
    print(f"Top-2 retrieved: {top}")
    rrf = rrf_score([[0, 1, 2], [2, 0, 1]])
    print(f"RRF scores: {rrf}")
    chunks = chunk_text("a" * 1200, chunk_size=512, overlap=50)
    print(f"Chunks: {len(chunks)}, sizes: {[len(c) for c in chunks]}")
    print("✓ Knowledge & Retrieval module complete.")
