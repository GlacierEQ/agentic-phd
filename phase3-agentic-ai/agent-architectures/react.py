"""
Agent Architectures — ReAct, Reflexion, LATS, Tool Use
Doctorate-level AI curriculum — Agentic PhD
"""
from typing import List, Dict, Callable, Tuple


class ReActAgent:
    """ReAct: Reasoning + Acting in interleaved loops."""

    def __init__(self, tools: Dict[str, Callable]):
        self.tools = tools
        self.trace: List[Dict] = []

    def step(self, thought: str, action: str, action_input: str) -> str:
        obs = self.tools.get(action, lambda x: f"Unknown tool: {action}")(action_input)
        self.trace.append({"thought": thought, "action": action, "input": action_input, "observation": obs})
        return obs

    def run(self, steps: List[Tuple[str, str, str]]) -> List[str]:
        return [self.step(t, a, i) for t, a, i in steps]


class ReflexionAgent:
    """Reflexion: agent reflects on failures and improves."""

    def __init__(self, actor: Callable, evaluator: Callable, reflector: Callable):
        self.actor = actor
        self.evaluator = evaluator
        self.reflector = reflector
        self.reflections: List[str] = []

    def run(self, task: str, max_trials: int = 3) -> str:
        for trial in range(max_trials):
            output = self.actor(task, self.reflections)
            score = self.evaluator(output)
            if score >= 1.0:
                return output
            reflection = self.reflector(output, score)
            self.reflections.append(reflection)
        return output


def tool_selection_score(tool_desc: str, query: str) -> float:
    """Simple keyword overlap for tool selection."""
    q_words = set(query.lower().split())
    t_words = set(tool_desc.lower().split())
    return len(q_words & t_words) / max(len(q_words), 1)


if __name__ == "__main__":
    print("=== Agent Architectures: ReAct, Reflexion ===")
    agent = ReActAgent(tools={
        "search": lambda x: f"Results for: {x}",
        "calc": lambda x: str(eval(x)),
    })
    obs = agent.run([
        ("Need info about X", "search", "quantum computing"),
        ("Calculate 2^10", "calc", "2**10"),
    ])
    print(f"ReAct observations: {obs}")

    reflexion = ReflexionAgent(
        actor=lambda task, refs: f"Answer for {task} (attempt {len(refs)+1})",
        evaluator=lambda out: 0.5 if "attempt 1" in out else 1.0,
        reflector=lambda out, score: f"Failed with score {score}, try harder",
    )
    result = reflexion.run("What is 2+2?")
    print(f"Reflexion result: {result}")
    print(f"Reflections: {reflexion.reflections}")

    score = tool_selection_score("search the web for information", "find information about AI")
    print(f"Tool selection score: {score:.4f}")
    print("✓ Agent Architectures module complete.")
