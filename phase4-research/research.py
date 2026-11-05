"""
Phase 4: Research & Dissertation
Doctorate-level AI curriculum — Agentic PhD
"""
import json
import hashlib
from datetime import datetime, timezone
from typing import List, Dict


# ─── 1. Literature Review: Paper Tracking ───────────────────────────────────

class PaperTracker:
    """Track papers for literature review."""

    def __init__(self):
        self.papers: List[Dict] = []

    def add(self, title: str, authors: List[str], venue: str, year: int, tags: List[str]):
        self.papers.append({
            "title": title, "authors": authors, "venue": venue,
            "year": year, "tags": tags, "added": datetime.now(timezone.utc).isoformat(),
        })

    def search(self, keyword: str) -> List[Dict]:
        kw = keyword.lower()
        return [p for p in self.papers if kw in p["title"].lower() or any(kw in t.lower() for t in p["tags"])]

    def by_venue(self, venue: str) -> List[Dict]:
        return [p for p in self.papers if p["venue"] == venue]

    def summary(self) -> Dict:
        venues = {}
        for p in self.papers:
            venues[p["venue"]] = venues.get(p["venue"], 0) + 1
        return {"total": len(self.papers), "venues": venues, "years": sorted(set(p["year"] for p in self.papers))}


# ─── 2. Experiment Tracking ──────────────────────────────────────────────────

class ExperimentLog:
    """Track experiments with reproducibility metadata."""

    def __init__(self):
        self.experiments: List[Dict] = []

    def log(self, name: str, params: Dict, metrics: Dict, seed: int = 42):
        exp = {
            "name": name, "params": params, "metrics": metrics,
            "seed": seed, "timestamp": datetime.now(timezone.utc).isoformat(),
            "hash": hashlib.sha256(json.dumps(params, sort_keys=True).encode()).hexdigest()[:12],
        }
        self.experiments.append(exp)
        return exp

    def best(self, metric: str, higher_is_better: bool = True) -> Dict:
        if not self.experiments:
            return {}
        return (max if higher_is_better else min)(self.experiments, key=lambda e: e["metrics"].get(metric, 0))

    def compare(self, metric: str) -> List[Dict]:
        return sorted(self.experiments, key=lambda e: e["metrics"].get(metric, 0), reverse=True)


# ─── 3. Dissertation Structure ───────────────────────────────────────────────

DISSERTATION_TEMPLATE = {
    "title": "",
    "abstract": "",
    "chapters": [
        {"num": 1, "title": "Introduction", "sections": ["Motivation", "Problem Statement", "Contributions", "Thesis Outline"]},
        {"num": 2, "title": "Background & Related Work", "sections": ["Foundations", "Prior Art", "Gap Analysis"]},
        {"num": 3, "title": "Methodology", "sections": ["Approach", "Architecture", "Algorithms"]},
        {"num": 4, "title": "Experiments", "sections": ["Setup", "Baselines", "Results", "Ablation Studies"]},
        {"num": 5, "title": "Analysis & Discussion", "sections": ["Interpretation", "Limitations", "Failure Modes"]},
        {"num": 6, "title": "Conclusion & Future Work", "sections": ["Summary", "Impact", "Open Questions"]},
    ],
    "appendices": ["Code", "Data", "Extended Results"],
}


def generate_dissertation_outline(title: str) -> Dict:
    outline = dict(DISSERTATION_TEMPLATE)
    outline["title"] = title
    outline["created"] = datetime.now(timezone.utc).isoformat()
    return outline


# ─── 4. Qualifying Exam Checklist ───────────────────────────────────────────

QUALIFYING_EXAM_TOPICS = {
    "Mathematics": ["Linear Algebra", "Probability", "Optimization", "Information Theory"],
    "Core ML": ["Learning Theory", "Deep Learning", "RL", "Causal Inference"],
    "Agentic AI": ["LLM Foundations", "Agent Architectures", "Evaluation", "Safety"],
    "Research Methods": ["Experimental Design", "Statistical Testing", "Reproducibility"],
}


def check_qualifying_readiness(completed: List[str]) -> Dict:
    all_topics = [t for topics in QUALIFYING_EXAM_TOPICS.values() for t in topics]
    missing = [t for t in all_topics if t not in completed]
    return {
        "total": len(all_topics),
        "completed": len(completed),
        "missing": missing,
        "ready": len(missing) == 0,
        "progress": f"{len(completed)}/{len(all_topics)}",
    }


# ─── Demo ────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    print("=== Phase 4: Research & Dissertation ===\n")

    # Paper Tracker
    tracker = PaperTracker()
    tracker.add("Attention Is All You Need", ["Vaswani et al."], "NeurIPS", 2017, ["transformers", "attention"])
    tracker.add("ReAct: Synergizing Reasoning and Acting", ["Yao et al."], "ICLR", 2023, ["agents", "reasoning"])
    tracker.add("Reflexion: Language Agents with Verbal Reinforcement Learning", ["Shinn et al."], "NeurIPS", 2023, ["agents", "reflection"])
    print(f"Paper summary: {tracker.summary()}")
    print(f"Agent papers: {[p['title'] for p in tracker.search('agent')]}")

    # Experiment Log
    log = ExperimentLog()
    log.log("baseline", {"lr": 0.001, "batch": 32}, {"accuracy": 0.85, "f1": 0.82})
    log.log("improved", {"lr": 0.0005, "batch": 64}, {"accuracy": 0.91, "f1": 0.89})
    print(f"Best by accuracy: {log.best('accuracy')['name']}")
    print(f"Ranked: {[e['name'] for e in log.compare('accuracy')]}")

    # Dissertation Outline
    outline = generate_dissertation_outline("Scalable Safety Guarantees for Multi-Agent Autonomous Systems")
    print(f"\nDissertation: {outline['title']}")
    for ch in outline["chapters"]:
        print(f"  Ch {ch['num']}: {ch['title']}")

    # Qualifying Exam Readiness
    completed = ["Linear Algebra", "Probability", "Learning Theory", "LLM Foundations", "Agent Architectures"]
    readiness = check_qualifying_readiness(completed)
    print(f"\nQualifying exam: {readiness['progress']} — Ready: {readiness['ready']}")
    if readiness["missing"]:
        print(f"  Missing: {readiness['missing']}")

    print("\n✓ Phase 4 complete.")
