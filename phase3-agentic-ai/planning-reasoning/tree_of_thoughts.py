"""
Planning & Reasoning — Tree of Thoughts, MCTS, Chain-of-Thought
Doctorate-level AI curriculum — Agentic PhD
"""
import math
import random
from typing import List, Callable, Tuple


def chain_of_thought(prompt: str, steps: List[str]) -> str:
    """Chain-of-Thought: decompose reasoning into steps."""
    reasoning = f"Question: {prompt}\n"
    for i, step in enumerate(steps, 1):
        reasoning += f"Step {i}: {step}\n"
    return reasoning


def tree_of_thoughts(initial: str, expand: Callable, evaluate: Callable, depth: int = 3, breadth: int = 3) -> Tuple[str, float]:
    """Tree of Thoughts search with pruning."""
    current = [(initial, 0.0)]
    best_state, best_score = initial, float('-inf')
    for d in range(depth):
        next_level = []
        for state, _ in current:
            for child in expand(state):
                score = evaluate(child)
                next_level.append((child, score))
                if score > best_score:
                    best_score = score
                    best_state = child
        next_level.sort(key=lambda x: -x[1])
        current = next_level[:breadth]
    return best_state, best_score


def mcts_select(node_value: float, node_visits: int, parent_visits: int, c: float = 1.414) -> float:
    """UCT selection: value + c * sqrt(ln(parent_visits) / node_visits)."""
    if node_visits == 0:
        return float('inf')
    exploitation = node_value / node_visits
    exploration = c * math.sqrt(math.log(parent_visits + 1) / node_visits)
    return exploitation + exploration


def self_consistency(votes: List[str]) -> str:
    """Self-consistency: majority vote over multiple reasoning paths."""
    from collections import Counter
    return Counter(votes).most_common(1)[0][0]


if __name__ == "__main__":
    print("=== Planning & Reasoning ===")
    cot = chain_of_thought("What is 15*23?", ["15*20=300", "15*3=45", "300+45=345"])
    print(cot)

    def expand(s): return [s + "a", s + "b", s + "c"]
    def evaluate(s): return len(s) + random.random()
    best, score = tree_of_thoughts("x", expand, evaluate, depth=2, breadth=2)
    print(f"ToT best: {best} (score={score:.4f})")

    uct = mcts_select(10.0, 5, 20)
    print(f"MCTS UCT: {uct:.4f}")

    sc = self_consistency(["42", "42", "37", "42", "37"])
    print(f"Self-consistency: {sc}")
    print("✓ Planning & Reasoning module complete.")
