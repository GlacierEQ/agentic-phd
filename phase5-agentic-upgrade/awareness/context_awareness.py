"""
Awareness — Context Window Management, Attention Allocation, Situational Awareness
Agentic Upgrade for AI Agent Capability Enhancement
"""
from typing import List, Dict, Tuple


def context_budget(total_tokens: int, system: int, history: int, tools: int, reserved: int = 1000) -> Dict:
    """Allocate context window budget."""
    used = system + history + tools
    available = total_tokens - used - reserved
    return {
        "total": total_tokens,
        "system": system,
        "history": history,
        "tools": tools,
        "reserved": reserved,
        "available": max(0, available),
        "utilization": used / total_tokens,
    }


def attention_allocation(items: List[Dict], total_budget: int) -> List[Dict]:
    """Allocate attention budget across items by priority."""
    items_sorted = sorted(items, key=lambda x: -x.get("priority", 1))
    remaining = total_budget
    result = []
    for item in items_sorted:
        cost = item.get("cost", 100)
        if cost <= remaining:
            result.append({**item, "allocated": True, "budget_used": cost})
            remaining -= cost
        else:
            result.append({**item, "allocated": False, "budget_used": 0})
    return result


def staleness_check(last_updated: float, current_time: float, max_age: float) -> bool:
    """Check if information is stale."""
    return (current_time - last_updated) > max_age


def situation_summary(context: Dict) -> str:
    """Generate a situational awareness summary."""
    parts = []
    if context.get("task"):
        parts.append(f"Task: {context['task']}")
    if context.get("errors"):
        parts.append(f"Errors: {len(context['errors'])} active")
    if context.get("progress"):
        parts.append(f"Progress: {context['progress']}")
    if context.get("blockers"):
        parts.append(f"Blockers: {', '.join(context['blockers'])}")
    return " | ".join(parts) if parts else "No context available"


def priority_queue(items: List[Dict]) -> List[Dict]:
    """Sort items by priority (urgent first, then by deadline)."""
    return sorted(items, key=lambda x: (-x.get("urgent", 0), x.get("deadline", float('inf'))))


if __name__ == "__main__":
    print("=== Awareness: Context & Situational ===")
    budget = context_budget(128000, 2000, 50000, 5000, 1000)
    print(f"  Context budget: {budget['available']} available, {budget['utilization']:.1%} utilized")
    alloc = attention_allocation([
        {"name": "critical_task", "priority": 10, "cost": 500},
        {"name": "background", "priority": 2, "cost": 200},
        {"name": "nice_to_have", "priority": 1, "cost": 1000},
    ], 1000)
    for a in alloc:
        print(f"  {a['name']}: allocated={a['allocated']}")
    print(f"  Stale check (100s ago, max 60s): {staleness_check(0, 100, 60)}")
    summary = situation_summary({"task": "build agent", "progress": "60%", "errors": ["timeout"], "blockers": []})
    print(f"  Situation: {summary}")
    print("✓ Awareness module complete.")
