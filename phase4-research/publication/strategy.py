"""
Publication Strategy — Venue Selection, Peer Review, Impact
Doctorate-level AI curriculum — Agentic PhD
"""
from typing import List, Dict


VENUES = {
    "NeurIPS": {"tier": 1, "focus": "ML theory, deep learning, RL", "deadline_month": 5},
    "ICML": {"tier": 1, "focus": "ML theory, optimization, applications", "deadline_month": 1},
    "ICLR": {"tier": 1, "focus": "Representation learning, deep learning", "deadline_month": 9},
    "AAAI": {"tier": 1, "focus": "AI broadly, agents, planning, NLP", "deadline_month": 8},
    "ACL": {"tier": 1, "focus": "NLP, language models, dialogue", "deadline_month": 2},
    "AAMAS": {"tier": 2, "focus": "Multi-agent systems, agents", "deadline_month": 10},
    "EMNLP": {"tier": 1, "focus": "NLP, empirical methods", "deadline_month": 6},
    "CoRL": {"tier": 2, "focus": "Robot learning, RL", "deadline_month": 6},
}


def recommend_venue(topic: str, has_theory: bool = False, has_empirical: bool = False) -> List[Dict]:
    """Recommend venues based on topic and contribution type."""
    results = []
    for name, info in VENUES.items():
        score = 0
        if "agent" in topic.lower() and "agent" in info["focus"].lower():
            score += 2
        if has_theory and "theory" in info["focus"].lower():
            score += 1
        if has_empirical and "empirical" in info["focus"].lower():
            score += 1
        if info["tier"] == 1:
            score += 1
        results.append({"venue": name, "score": score, **info})
    results.sort(key=lambda x: -x["score"])
    return results[:4]


def review_checklist() -> List[str]:
    return [
        "Novelty: Is the contribution clearly new?",
        "Significance: Does it advance the field?",
        "Soundness: Are methods and proofs correct?",
        "Clarity: Is the writing clear and well-organized?",
        "Reproducibility: Can results be reproduced?",
        "Related work: Is prior work adequately cited?",
        "Experiments: Are baselines and ablations sufficient?",
        "Limitations: Are limitations honestly discussed?",
    ]


if __name__ == "__main__":
    print("=== Publication Strategy ===")
    recs = recommend_venue("multi-agent safety", has_theory=True, has_empirical=True)
    print("Recommended venues:")
    for r in recs:
        print(f"  {r['venue']} (tier {r['tier']}, score={r['score']}) — {r['focus']}")
    print(f"\nReview checklist ({len(review_checklist())} items):")
    for item in review_checklist():
        print(f"  [ ] {item}")
    print("✓ Publication module complete.")
