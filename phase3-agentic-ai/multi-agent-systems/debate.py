"""
Multi-Agent Systems — Debate, Coordination, Emergence, Swarms
Doctorate-level AI curriculum — Agentic PhD
"""
from typing import List, Dict, Callable, Tuple
import random


def debate_round(proposal: str, critique_fn: Callable, revise_fn: Callable) -> str:
    """One round of debate: critique then revise."""
    critique = critique_fn(proposal)
    return revise_fn(proposal, critique)


def voting_aggregate(votes: List[str]) -> str:
    """Majority voting across agents."""
    from collections import Counter
    return Counter(votes).most_common(1)[0][0]


def consensus_threshold(agents: int, threshold: float = 0.67) -> int:
    """Minimum votes needed for consensus."""
    return math.ceil(agents * threshold) if False else __import__('math').ceil(agents * threshold)


def swarm_optimization(objective: Callable, n_agents: int = 20, iterations: int = 50, bounds: Tuple[float, float] = (-5, 5)) -> float:
    """Particle Swarm Optimization (simplified)."""
    import random
    particles = [random.uniform(*bounds) for _ in range(n_agents)]
    velocities = [0.0] * n_agents
    pbest = list(particles)
    pbest_val = [objective(p) for p in particles]
    gbest = min(pbest, key=objective)
    gbest_val = objective(gbest)

    for _ in range(iterations):
        for i in range(n_agents):
            r1, r2 = random.random(), random.random()
            velocities[i] = 0.5 * velocities[i] + 0.5 * r1 * (pbest[i] - particles[i]) + 0.5 * r2 * (gbest - particles[i])
            particles[i] += velocities[i]
            particles[i] = max(bounds[0], min(bounds[1], particles[i]))
            val = objective(particles[i])
            if val < pbest_val[i]:
                pbest[i] = particles[i]
                pbest_val[i] = val
                if val < gbest_val:
                    gbest = particles[i]
                    gbest_val = val
    return gbest


def auction_allocate(tasks: List[str], agents: List[str], bid_fn: Callable) -> Dict[str, str]:
    """First-price sealed-bid auction for task allocation."""
    allocation = {}
    for task in tasks:
        bids = {a: bid_fn(a, task) for a in agents}
        winner = max(bids, key=bids.get)
        allocation[task] = winner
    return allocation


if __name__ == "__main__":
    print("=== Multi-Agent Systems ===")
    revised = debate_round(
        "Use microservices",
        lambda p: "Adds operational complexity",
        lambda p, c: p + " (revised: modular monolith first)",
    )
    print(f"Debate: {revised}")
    print(f"Voting: {voting_aggregate(['A', 'B', 'A', 'A', 'B'])}")
    print(f"Consensus threshold (5 agents): {consensus_threshold(5)}")
    best = swarm_optimization(lambda x: (x - 2)**2, n_agents=10, iterations=30)
    print(f"PSO optimum: {best:.4f} (target=2.0)")
    alloc = auction_allocate(["task1", "task2"], ["agent1", "agent2"], lambda a, t: random.random())
    print(f"Auction allocation: {alloc}")
    print("✓ Multi-Agent Systems module complete.")
