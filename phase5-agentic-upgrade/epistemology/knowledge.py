"""
Epistemology — Knowledge, Belief, Evidence, Truth, Uncertainty Quantification
Agentic Upgrade for AI Agent Capability Enhancement
"""
import math
from typing import List, Dict, Tuple


def bayesian_update(prior: float, likelihood: float, evidence_prob: float) -> float:
    """Bayes' theorem: P(H|E) = P(E|H) * P(H) / P(E)."""
    if evidence_prob == 0:
        return 0.0
    return (likelihood * prior) / evidence_prob


def entropy_of_belief(probs: List[float]) -> float:
    """Shannon entropy of belief distribution (uncertainty measure)."""
    return -sum(p * math.log2(p) for p in probs if p > 0)


def confidence_interval_wilson(successes: int, trials: int, z: float = 1.96) -> Tuple[float, float]:
    """Wilson score interval for binomial proportion."""
    if trials == 0:
        return (0.0, 1.0)
    p_hat = successes / trials
    denom = 1 + z**2 / trials
    center = (p_hat + z**2 / (2 * trials)) / denom
    margin = z * math.sqrt(p_hat * (1 - p_hat) / trials + z**2 / (4 * trials**2)) / denom
    return (max(0, center - margin), min(1, center + margin))


def evidence_weight(sources: List[Dict]) -> float:
    """Combine evidence from multiple sources with weights."""
    if not sources:
        return 0.0
    total_weight = sum(s.get("weight", 1.0) for s in sources)
    weighted_sum = sum(s.get("confidence", 0.5) * s.get("weight", 1.0) for s in sources)
    return weighted_sum / total_weight if total_weight > 0 else 0.0


def knowledge_graph_confidence(facts: List[Dict]) -> float:
    """Aggregate confidence across knowledge graph facts."""
    if not facts:
        return 0.0
    # Combine with noisy-OR: P(at least one true) = 1 - prod(1 - p_i)
    prob_none = 1.0
    for f in facts:
        prob_none *= (1 - f.get("confidence", 0.5))
    return 1 - prob_none


def epistemic_vs_aleatoric(total_uncertainty: float, model_uncertainty: float) -> Tuple[float, float]:
    """Decompose uncertainty into epistemic (reducible) and aleatoric (irreducible)."""
    epistemic = model_uncertainty
    aleatoric = total_uncertainty - model_uncertainty
    return (max(0, epistemic), max(0, aleatoric))


if __name__ == "__main__":
    print("=== Epistemology: Knowledge & Uncertainty ===")
    post = bayesian_update(prior=0.5, likelihood=0.8, evidence_prob=0.6)
    print(f"  Bayesian update: {post:.4f}")
    print(f"  Belief entropy [0.5,0.5]: {entropy_of_belief([0.5, 0.5]):.4f}")
    ci = confidence_interval_wilson(8, 10)
    print(f"  Wilson CI (8/10): ({ci[0]:.4f}, {ci[1]:.4f})")
    ew = evidence_weight([{"confidence": 0.9, "weight": 2}, {"confidence": 0.7, "weight": 1}])
    print(f"  Evidence weight: {ew:.4f}")
    kg = knowledge_graph_confidence([{"confidence": 0.8}, {"confidence": 0.7}, {"confidence": 0.9}])
    print(f"  Knowledge graph confidence: {kg:.4f}")
    ep, al = epistemic_vs_aleatoric(0.5, 0.2)
    print(f"  Epistemic: {ep:.4f}, Aleatoric: {al:.4f}")
    print("✓ Epistemology module complete.")
