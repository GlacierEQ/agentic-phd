"""Lab 2: Build a ReAct agent that uses tools."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'phase3-agentic-ai'))
from agentic import ReActAgent

if __name__ == "__main__":
    def search(q): return f"Found: {q} is a city in Hawaii"
    def calc(expr): return str(eval(expr))
    agent = ReActAgent(tools={"search": search, "calc": calc})
    obs = agent.run([
        ("Need to find where Honolulu is", "search", "Honolulu"),
        ("Calculate area", "calc", "10 * 20"),
    ])
    print("Lab 2: ReAct Agent")
    for o in obs:
        print(f"  {o}")
    assert "Hawaii" in obs[0]
    print("✓ Lab 2 passed.")
