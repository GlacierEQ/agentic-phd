"""Lab 3: Implement pass@k and exact-match evals."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'phase3-agentic-ai'))
from agentic import exact_match, pass_at_k, llm_judge_score

if __name__ == "__main__":
    print("Lab 3: Evals")
    assert exact_match("Hello World", "hello world") == 1.0
    assert exact_match("Hello", "World") == 0.0
    print(f"  pass@5 (3/10 correct): {pass_at_k([True]*3 + [False]*7, 5):.4f}")
    score = llm_judge_score("The answer is correct and complete", {"correct": 0.5, "complete": 0.5})
    print(f"  LLM judge score: {score:.2f}")
    assert score == 1.0
    print("✓ Lab 3 passed.")
