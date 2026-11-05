"""Lab: Build a ReAct agent."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'phase3-agentic-ai', 'agent-architectures'))
from react import ReActAgent

def main():
    print("Lab: ReAct Agent")
    agent = ReActAgent(tools={
        "search": lambda x: f"Found: {x}",
        "calc": lambda x: str(eval(x)),
    })
    obs = agent.run([
        ("Find info", "search", "AI agents"),
        ("Calculate", "calc", "2**8"),
    ])
    for o in obs:
        print(f"  {o}")
    assert "AI agents" in obs[0]
    print("✓ Lab passed.")

if __name__ == "__main__":
    main()
