"""
Qualifying Exams — Comprehensive Coverage of Phases 1-3
Doctorate-level AI curriculum — Agentic PhD
"""
from typing import List, Dict


QUALIFYING_TOPICS = {
    "Mathematics": ["Linear Algebra", "Probability", "Optimization", "Information Theory", "Complexity Theory"],
    "Core ML": ["Learning Theory", "Deep Learning Theory", "Graphical Models", "Reinforcement Learning", "Causal Inference"],
    "Agentic AI": ["LLM Foundations", "Agent Architectures", "Memory Systems", "Planning & Reasoning", "Evaluation & Alignment", "Knowledge & Retrieval", "Safety & Governance", "Multi-Agent Systems"],
    "Research Methods": ["Experimental Design", "Statistical Testing", "Reproducibility", "Literature Review"],
}


def check_readiness(completed: List[str]) -> Dict:
    all_topics = [t for topics in QUALIFYING_TOPICS.values() for t in topics]
    missing = [t for t in all_topics if t not in completed]
    by_category = {}
    for cat, topics in QUALIFYING_TOPICS.items():
        done = [t for t in topics if t in completed]
        by_category[cat] = f"{len(done)}/{len(topics)}"
    return {
        "total": len(all_topics),
        "completed": len(completed),
        "missing": missing,
        "ready": len(missing) == 0,
        "progress": f"{len(completed)}/{len(all_topics)}",
        "by_category": by_category,
    }


def study_plan(weeks: int = 12, topics_per_week: int = 3) -> List[Dict]:
    all_topics = [t for topics in QUALIFYING_TOPICS.values() for t in topics]
    plan = []
    for w in range(weeks):
        start = w * topics_per_week
        end = start + topics_per_week
        week_topics = all_topics[start:end]
        if not week_topics:
            break
        plan.append({"week": w + 1, "topics": week_topics})
    return plan


if __name__ == "__main__":
    print("=== Qualifying Exams ===")
    completed = ["Linear Algebra", "Probability", "Learning Theory", "LLM Foundations", "Agent Architectures"]
    r = check_readiness(completed)
    print(f"Progress: {r['progress']} — Ready: {r['ready']}")
    for cat, prog in r["by_category"].items():
        print(f"  {cat}: {prog}")
    if r["missing"]:
        print(f"  Missing: {r['missing'][:5]}...")
    plan = study_plan(weeks=5, topics_per_week=3)
    print(f"\nStudy plan ({len(plan)} weeks):")
    for w in plan:
        print(f"  Week {w['week']}: {w['topics']}")
    print("✓ Qualifying module complete.")
