"""
Literature Review — Paper Tracking, Gap Analysis, Contribution Positioning
Doctorate-level AI curriculum — Agentic PhD
"""
from typing import List, Dict
import hashlib
from datetime import datetime, timezone


class PaperTracker:
    """Track papers for systematic literature review."""

    def __init__(self):
        self.papers: List[Dict] = []

    def add(self, title: str, authors: List[str], venue: str, year: int, tags: List[str], url: str = ""):
        self.papers.append({
            "id": hashlib.md5(title.encode()).hexdigest()[:8],
            "title": title, "authors": authors, "venue": venue,
            "year": year, "tags": tags, "url": url,
            "added": datetime.now(timezone.utc).isoformat(),
        })

    def search(self, keyword: str) -> List[Dict]:
        kw = keyword.lower()
        return [p for p in self.papers if kw in p["title"].lower() or any(kw in t.lower() for t in p["tags"])]

    def by_venue(self, venue: str) -> List[Dict]:
        return [p for p in self.papers if p["venue"] == venue]

    def by_year(self, year: int) -> List[Dict]:
        return [p for p in self.papers if p["year"] == year]

    def gap_analysis(self, topic: str) -> Dict:
        relevant = self.search(topic)
        venues = {}
        for p in relevant:
            venues[p["venue"]] = venues.get(p["venue"], 0) + 1
        years = sorted(set(p["year"] for p in relevant))
        return {
            "topic": topic,
            "total_papers": len(relevant),
            "venues": venues,
            "year_range": (min(years), max(years)) if years else (None, None),
            "tags": list(set(t for p in relevant for t in p["tags"])),
        }

    def summary(self) -> Dict:
        venues = {}
        for p in self.papers:
            venues[p["venue"]] = venues.get(p["venue"], 0) + 1
        return {"total": len(self.papers), "venues": venues, "years": sorted(set(p["year"] for p in self.papers))}


if __name__ == "__main__":
    print("=== Literature Review: Paper Tracker ===")
    tracker = PaperTracker()
    tracker.add("Attention Is All You Need", ["Vaswani et al."], "NeurIPS", 2017, ["transformers", "attention"], "https://arxiv.org/abs/1706.03762")
    tracker.add("ReAct: Synergizing Reasoning and Acting", ["Yao et al."], "ICLR", 2023, ["agents", "reasoning"], "https://arxiv.org/abs/2210.03629")
    tracker.add("Reflexion", ["Shinn et al."], "NeurIPS", 2023, ["agents", "reflection"], "https://arxiv.org/abs/2303.11366")
    tracker.add("Tree of Thoughts", ["Yao et al."], "NeurIPS", 2023, ["reasoning", "planning"], "https://arxiv.org/abs/2305.10601")
    print(f"Summary: {tracker.summary()}")
    print(f"Agent papers: {[p['title'] for p in tracker.search('agent')]}")
    gap = tracker.gap_analysis("agent")
    print(f"Gap analysis (agents): {gap['total_papers']} papers, venues={gap['venues']}")
    print("✓ Literature module complete.")
