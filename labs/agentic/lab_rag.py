"""Lab: RAG retrieval."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'phase3-agentic-ai', 'knowledge-retrieval'))
from rag import retrieve_top_k, cosine_similarity, chunk_text

def main():
    print("Lab: RAG Retrieval")
    q = [1.0, 0.0, 0.0]
    docs = [[1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.5, 0.5, 0.0]]
    top = retrieve_top_k(q, docs, k=2)
    print(f"  Top-2: {top}")
    assert 0 in top
    chunks = chunk_text("a" * 1200, 512, 50)
    print(f"  Chunks: {len(chunks)}")
    print("✓ Lab passed.")

if __name__ == "__main__":
    main()
