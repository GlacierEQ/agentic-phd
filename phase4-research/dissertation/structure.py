"""
Dissertation — Structure, Writing, Defense Preparation
Doctorate-level AI curriculum — Agentic PhD
"""
from typing import List, Dict
from datetime import datetime, timezone


DISSERTATION_TEMPLATE = {
    "title": "",
    "abstract": "",
    "chapters": [
        {"num": 1, "title": "Introduction", "sections": ["Motivation", "Problem Statement", "Contributions", "Thesis Outline"]},
        {"num": 2, "title": "Background & Related Work", "sections": ["Foundations", "Prior Art", "Gap Analysis"]},
        {"num": 3, "title": "Methodology", "sections": ["Approach", "Architecture", "Algorithms", "Theoretical Analysis"]},
        {"num": 4, "title": "Experiments", "sections": ["Setup", "Baselines", "Results", "Ablation Studies", "Statistical Tests"]},
        {"num": 5, "title": "Analysis & Discussion", "sections": ["Interpretation", "Limitations", "Failure Modes", "Ethical Considerations"]},
        {"num": 6, "title": "Conclusion & Future Work", "sections": ["Summary", "Impact", "Open Questions", "Future Directions"]},
    ],
    "appendices": ["Code", "Data", "Extended Results", "Proofs"],
}


def generate_outline(title: str) -> Dict:
    outline = dict(DISSERTATION_TEMPLATE)
    outline["title"] = title
    outline["created"] = datetime.now(timezone.utc).isoformat()
    return outline


def defense_checklist() -> List[str]:
    return [
        "Slides prepared (45 min presentation)",
        "Backup slides for anticipated questions",
        "Practice talk completed (2+ times)",
        "Committee feedback incorporated",
        "Dissertation formatted per university guidelines",
        "Code and data archived (reproducibility)",
        "Extended abstract / summary prepared",
    ]


def word_count_estimate(chapters: List[Dict], words_per_section: int = 1500) -> int:
    total_sections = sum(len(ch["sections"]) for ch in chapters)
    return total_sections * words_per_section


if __name__ == "__main__":
    print("=== Dissertation Structure ===")
    outline = generate_outline("Scalable Safety Guarantees for Multi-Agent Autonomous Systems")
    print(f"Title: {outline['title']}")
    for ch in outline["chapters"]:
        print(f"  Ch {ch['num']}: {ch['title']} ({len(ch['sections'])} sections)")
    wc = word_count_estimate(outline["chapters"])
    print(f"Estimated word count: {wc:,} (~{wc//250} pages)")
    print(f"\nDefense checklist ({len(defense_checklist())} items):")
    for item in defense_checklist():
        print(f"  [ ] {item}")
    print("✓ Dissertation module complete.")
