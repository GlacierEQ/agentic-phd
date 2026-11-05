"""
Memory Systems — Episodic, Semantic, Working, Graph Memory
Doctorate-level AI curriculum — Agentic PhD
"""
from typing import List, Dict, Optional
import math


class EpisodicMemory:
    """Episodic memory with recency-weighted retrieval."""

    def __init__(self, capacity: int = 1000):
        self.capacity = capacity
        self.episodes: List[Dict] = []

    def store(self, episode: Dict):
        self.episodes.append(episode)
        if len(self.episodes) > self.capacity:
            self.episodes.pop(0)

    def retrieve(self, query: str, top_k: int = 5) -> List[Dict]:
        scored = []
        for i, ep in enumerate(self.episodes):
            text = str(ep).lower()
            score = sum(1 for w in query.lower().split() if w in text)
            recency = i / max(len(self.episodes), 1)
            scored.append((score + 0.1 * recency, ep))
        scored.sort(key=lambda x: -x[0])
        return [ep for _, ep in scored[:top_k]]


class SemanticMemory:
    """Semantic memory: key-value store with similarity search."""

    def __init__(self):
        self.facts: Dict[str, str] = {}

    def store(self, key: str, value: str):
        self.facts[key] = value

    def retrieve(self, key: str) -> Optional[str]:
        return self.facts.get(key)

    def search(self, query: str) -> List[str]:
        return [v for k, v in self.facts.items() if query.lower() in k.lower() or query.lower() in v.lower()]


class WorkingMemory:
    """Working memory with limited capacity (Miller's 7±2)."""

    def __init__(self, capacity: int = 7):
        self.capacity = capacity
        self.items: List = []

    def push(self, item):
        if len(self.items) >= self.capacity:
            self.items.pop(0)
        self.items.append(item)

    def get_all(self) -> List:
        return list(self.items)

    def clear(self):
        self.items.clear()


class GraphMemory:
    """Graph-based memory: entities and relations."""

    def __init__(self):
        self.entities: Dict[str, Dict] = {}
        self.relations: List[Tuple] = []

    def add_entity(self, name: str, attrs: Dict = None):
        self.entities[name] = attrs or {}

    def add_relation(self, src: str, rel: str, dst: str):
        self.relations.append((src, rel, dst))

    def neighbors(self, entity: str, relation: str = None) -> List[str]:
        result = []
        for s, r, d in self.relations:
            if s == entity and (relation is None or r == relation):
                result.append(d)
        return result

    def path(self, src: str, dst: str, max_depth: int = 3) -> List[str]:
        """BFS path finding."""
        from collections import deque
        visited = {src}
        queue = deque([(src, [src])])
        while queue:
            node, path = queue.popleft()
            if node == dst:
                return path
            if len(path) > max_depth:
                continue
            for nxt in self.neighbors(node):
                if nxt not in visited:
                    visited.add(nxt)
                    queue.append((nxt, path + [nxt]))
        return []


if __name__ == "__main__":
    print("=== Memory Systems ===")
    em = EpisodicMemory(capacity=5)
    em.store({"task": "debug auth", "outcome": "fixed token"})
    em.store({"task": "optimize query", "outcome": "added index"})
    print(f"Episodic retrieve 'auth': {em.retrieve('auth')}")

    sm = SemanticMemory()
    sm.store("python", "A programming language")
    print(f"Semantic search 'python': {sm.search('python')}")

    wm = WorkingMemory(capacity=3)
    for i in range(5):
        wm.push(i)
    print(f"Working memory (cap=3): {wm.get_all()}")

    gm = GraphMemory()
    gm.add_entity("Alice")
    gm.add_entity("Bob")
    gm.add_relation("Alice", "knows", "Bob")
    gm.add_relation("Bob", "works_at", "Acme")
    print(f"Neighbors of Alice: {gm.neighbors('Alice')}")
    print(f"Path Alice->Acme: {gm.path('Alice', 'Acme')}")
    print("✓ Memory Systems module complete.")
