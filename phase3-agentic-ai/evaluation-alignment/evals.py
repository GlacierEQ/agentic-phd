"""
Evaluation & Alignment — Evals, Red-teaming, RLHF/DPO
Doctorate-level AI curriculum — Agentic PhD
"""
import math
from typing import List, Dict, Callable


def exact_match(pred: str, gold: str) -> float:
    return 1.0 if pred.strip().lower() == gold.strip().lower() else 0.0


def pass_at_k(results: List[bool], k: int) -> float:
    """pass@k: probability at least one of k samples is correct."""
    n = len(results)
    c = sum(results)
    if n - c < k:
        return 1.0
    return 1.0 - (math.comb(n - c, k) / math.comb(n, k))


def f1_score(pred_tokens: List[str], gold_tokens: List[str]) -> float:
    pred_set = set(pred_tokens)
    gold_set = set(gold_tokens)
    tp = len(pred_set & gold_set)
    precision = tp / len(pred_set) if pred_set else 0.0
    recall = tp / len(gold_set) if gold_set else 0.0
    if precision + recall == 0:
        return 0.0
    return 2 * precision * recall / (precision + recall)


def rlhf_reward(r: float, kl_penalty: float, beta: float = 0.1) -> float:
    """RLHF reward with KL penalty: R = r - beta * KL."""
    return r - beta * kl_penalty


def dpo_loss(log_prob_ratio_w: float, log_prob_ratio_l: float, beta: float = 0.1) -> float:
    """DPO loss: -log sigmoid(beta * (log_ratio_w - log_ratio_l))."""
    import math
    diff = beta * (log_prob_ratio_w - log_prob_ratio_l)
    return -math.log(1 / (1 + math.exp(-diff))) if diff > -100 else 0.0


def red_team_score(response: str, harmful_patterns: List[str]) -> float:
    """Red-team score: fraction of harmful patterns NOT present."""
    found = sum(1 for p in harmful_patterns if p.lower() in response.lower())
    return 1.0 - (found / len(harmful_patterns)) if harmful_patterns else 1.0


if __name__ == "__main__":
    print("=== Evaluation & Alignment ===")
    print(f"Exact match: {exact_match('Hello World', 'hello world')}")
    print(f"pass@5 (3/10): {pass_at_k([True]*3 + [False]*7, 5):.4f}")
    print(f"F1 score: {f1_score(['a','b','c'], ['b','c','d']):.4f}")
    print(f"RLHF reward: {rlhf_reward(0.9, 0.2):.4f}")
    print(f"DPO loss: {dpo_loss(2.0, 0.5):.4f}")
    print(f"Red-team score: {red_team_score('safe response', ['hack', 'exploit']):.4f}")
    print("✓ Evaluation & Alignment module complete.")
