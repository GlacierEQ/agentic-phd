"""
Phase 3: Agentic AI & Frontier Research
Doctorate-level AI curriculum — Agentic PhD
"""
import math
import random
from typing import List, Dict, Callable, Tuple


# ─── 1. LLM Foundations: Attention ──────────────────────────────────────────

def softmax(scores: List[float]) -> List[float]:
    """Softmax normalization."""
    exps = [math.exp(s) for s in scores]
    total = sum(exps)
    return [e / total for e in exps]


def attention(Q: List[List[float]], K: List[List[float]], V: List[List[float]]) -> List[List[float]]:
    """Scaled dot-product attention: softmax(QK^T / sqrt(dk)) V."""
    dk = len(Q[0]) if Q else 1
    scale = math.sqrt(dk)
    result = []
    for q in Q:
        scores = [sum(q[i] * k[i] for i in range(dk)) / scale for k in K]
        weights = softmax(scores)
        out = [sum(weights[j] * V[j][i] for j in range(len(V))) for i in range(len(V[0]))]
        result.append(out)
    return result


# ─── 2. Agentic Systems: ReAct Loop ─────────────────────────────────────────

class ReActAgent:
    """Simplified ReAct agent: Thought -> Action -> Observation loop."""

    def __init__(self, tools: Dict[str, Callable]):
        self.tools = tools
        self.history: List[Dict] = []

    def step(self, thought: str, action: str, action_input: str) -> str:
        """Execute one ReAct step."""
        if action in self.tools:
            obs = self.tools[action](action_input)
        else:
            obs = f"Unknown tool: {action}"
        self.history.append({"thought": thought, "action": action, "input": action_input, "observation": obs})
        return obs

    def run(self, steps: List[Tuple[str, str, str]]) -> List[str]:
        """Run multiple ReAct steps."""
        observations = []
        for thought, action, inp in steps:
            obs = self.step(thought, action, inp)
            observations.append(obs)
        return observations


# ─── 3. Memory: Episodic Memory ─────────────────────────────────────────────

class EpisodicMemory:
    """Simple episodic memory with recency-based retrieval."""

    def __init__(self, capacity: int = 100):
        self.capacity = capacity
        self.episodes: List[Dict] = []

    def store(self, episode: Dict):
        self.episodes.append(episode)
        if len(self.episodes) > self.capacity:
            self.episodes.pop(0)

    def retrieve(self, query: str, top_k: int = 3) -> List[Dict]:
        """Retrieve most recent episodes matching query keywords."""
        scored = []
        for ep in self.episodes:
            text = str(ep).lower()
            score = sum(1 for w in query.lower().split() if w in text)
            scored.append((score, ep))
        scored.sort(key=lambda x: (-x[0], -self.episodes.index(x[1])))
        return [ep for _, ep in scored[:top_k]]


# ─── 4. Evaluation: Evals as Infrastructure ──────────────────────────────────

def exact_match(pred: str, gold: str) -> float:
    return 1.0 if pred.strip().lower() == gold.strip().lower() else 0.0


def pass_at_k(results: List[bool], k: int) -> float:
    """pass@k metric: probability that at least one of k samples is correct."""
    n = len(results)
    c = sum(results)
    if n - c < k:
        return 1.0
    return 1.0 - (math.comb(n - c, k) / math.comb(n, k))


def llm_judge_score(response: str, rubric: Dict[str, float]) -> float:
    """Simple rubric-based scoring (placeholder for LLM-as-judge)."""
    score = 0.0
    for criterion, weight in rubric.items():
        if criterion.lower() in response.lower():
            score += weight
    return min(1.0, score)


# ─── 5. Planning: Tree of Thoughts ───────────────────────────────────────────

def tot_search(initial_state: str, expand_fn: Callable, eval_fn: Callable, depth: int = 3, breadth: int = 3) -> str:
    """Simplified Tree of Thoughts search."""
    current = [(initial_state, 0.0)]
    best_state, best_score = initial_state, -float('inf')
    for d in range(depth):
        next_level = []
        for state, _ in current:
            for child in expand_fn(state):
                score = eval_fn(child)
                next_level.append((child, score))
                if score > best_score:
                    best_score = score
                    best_state = child
        next_level.sort(key=lambda x: -x[1])
        current = next_level[:breadth]
    return best_state


# ─── 6. Multi-Agent: Debate ──────────────────────────────────────────────────

def debate_round(proposal: str, critique_fn: Callable, revise_fn: Callable) -> str:
    """One round of debate: critique then revise."""
    critique = critique_fn(proposal)
    revised = revise_fn(proposal, critique)
    return revised


# ─── Demo ────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    print("=== Phase 3: Agentic AI & Frontier Research ===\n")

    # Attention
    Q = [[1.0, 0.0], [0.0, 1.0]]
    K = [[1.0, 0.0], [0.0, 1.0]]
    V = [[1.0, 2.0], [3.0, 4.0]]
    attn = attention(Q, K, V)
    print(f"Attention output: {attn}")

    # ReAct
    agent = ReActAgent(tools={
        "search": lambda x: f"Results for: {x}",
        "calc": lambda x: str(eval(x)),
    })
    obs = agent.run([
        ("Need to find info", "search", "quantum computing"),
        ("Now calculate", "calc", "2**10"),
    ])
    print(f"ReAct observations: {obs}")

    # Episodic Memory
    mem = EpisodicMemory(capacity=5)
    mem.store({"task": "debug auth", "outcome": "fixed token expiry"})
    mem.store({"task": "optimize query", "outcome": "added index"})
    retrieved = mem.retrieve("auth token")
    print(f"Retrieved episodes: {retrieved}")

    # Evals
    print(f"Exact match: {exact_match('Hello', 'hello')}")
    print(f"pass@3: {pass_at_k([True, False, False], 3):.4f}")
    print(f"LLM judge score: {llm_judge_score('The answer is correct and complete', {'correct': 0.5, 'complete': 0.5}):.2f}")

    # Tree of Thoughts
    def expand(s): return [s + "a", s + "b"]
    def evaluate(s): return len(s)
    best = tot_search("x", expand, evaluate, depth=2, breadth=2)
    print(f"ToT best: {best}")

    # Debate
    revised = debate_round(
        "Use microservices",
        lambda p: "Microservices add complexity",
        lambda p, c: p + " (revised: start monolith, split later)",
    )
    print(f"Debate revised: {revised}")

    print("\n✓ Phase 3 complete.")
