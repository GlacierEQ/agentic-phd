"""
Innovation Patterns — Creative Problem Solving, Novel Approaches, Synthesis
Agentic Upgrade for AI Agent Capability Enhancement
"""
from typing import List, Dict, Callable, Tuple
import random


def lateral_thinking(problem: str, constraints: List[str]) -> List[str]:
    """Generate lateral thinking approaches by relaxing constraints."""
    approaches = []
    for c in constraints:
        approaches.append(f"Relax '{c}': What if we ignore this constraint?")
    approaches.append(f"Invert: What if we do the opposite of the obvious solution?")
    approaches.append(f"Analogy: What other domain solves a similar problem?")
    approaches.append(f"Decompose: Break '{problem}' into 3 smaller sub-problems")
    approaches.append(f"Combine: Merge two unrelated existing solutions")
    return approaches


def cross_domain_transfer(source_domain: str, target_domain: str, concept: str) -> str:
    """Transfer a concept from one domain to another."""
    transfers = {
        ("biology", "software"): {"evolution": "genetic algorithms", "immune system": "anomaly detection", "neural plasticity": "online learning"},
        ("physics", "ml"): {"thermodynamics": "simulated annealing", "optics": "attention mechanisms", "mechanics": "gradient descent"},
        ("economics", "ai"): {"market equilibrium": "Nash equilibrium in multi-agent", "supply/demand": "resource allocation in scheduling", "auctions": "task allocation"},
    }
    key = (source_domain.lower(), target_domain.lower())
    if key in transfers and concept.lower() in transfers[key]:
        return transfers[key][concept.lower()]
    return f"Transfer '{concept}' from {source_domain} to {target_domain}: explore structural analogies"


def innovation_score(novelty: float, feasibility: float, impact: float, risk: float) -> float:
    """Score an innovation idea: (novelty * impact * feasibility) / (1 + risk)."""
    return (novelty * impact * feasibility) / (1 + risk)


def brainstorm(topic: str, n: int = 5) -> List[Dict]:
    """Generate brainstorming ideas with innovation scores."""
    ideas = []
    templates = [
        "Apply {topic} to a completely different industry",
        "Remove the most expensive component of {topic}",
        "Make {topic} 10x faster by changing the data structure",
        "Combine {topic} with a feedback loop",
        "Invert {topic}: instead of X, do anti-X",
    ]
    for i, t in enumerate(templates[:n]):
        idea = t.format(topic=topic)
        score = innovation_score(
            novelty=random.uniform(0.5, 1.0),
            feasibility=random.uniform(0.3, 0.9),
            impact=random.uniform(0.4, 1.0),
            risk=random.uniform(0.1, 0.5),
        )
        ideas.append({"idea": idea, "score": round(score, 4)})
    ideas.sort(key=lambda x: -x["score"])
    return ideas


if __name__ == "__main__":
    print("=== Innovation Patterns ===")
    approaches = lateral_thinking("reduce latency", ["budget", "accuracy", "compatibility"])
    print("Lateral thinking approaches:")
    for a in approaches:
        print(f"  - {a}")
    transfer = cross_domain_transfer("physics", "ml", "optics")
    print(f"  Cross-domain transfer: {transfer}")
    ideas = brainstorm("agent memory", n=3)
    print("  Brainstorm ideas:")
    for idea in ideas:
        print(f"    [{idea['score']}] {idea['idea']}")
    print("✓ Innovation Patterns module complete.")
