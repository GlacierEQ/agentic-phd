"""
Literature Review — Paper Tracking, Gap Analysis, Contribution Positioning
Doctorate-level AI curriculum — Agentic PhD
"""
from typing import List, Dict
import hashlib
from datetime import datetime, timezone
from pathlib import Path
import json


class PaperTracker:
    """Track papers for systematic literature review."""

    def __init__(self):
        self.papers: List[Dict] = []
        self.catalog_sources: List[Dict] = []

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

    def load_frontier_library(self, path=None) -> Dict:
        """Load the repo's source-identified, status-aware frontier catalog.

        Do not replace existing paper records, create new citations, or treat
        catalog inclusion as a completed experiment.
        """
        target = Path(path) if path is not None else (
            Path(__file__).resolve().parents[2] /
            "resources/research/frontier_sources.json"
        )
        raw = json.loads(target.read_text(encoding="utf-8"))
        if raw.get("schema") != "glaciereq.agentic-phd.research-library.v1":
            raise ValueError("Unknown source library schema")
        sources = raw.get("sources")
        if not isinstance(sources, list) or not sources or any(
            not isinstance(row, dict) or
            not all(isinstance(row.get(k), str) and row[k].strip()
                    for k in ("id", "title", "url", "technique", "experiment",
                              "area", "review_status", "implementation_status"))
            for row in sources
        ):
            raise ValueError("Missing source provenance or technique")
        keys = [row["id"] for row in sources]
        if len(set(keys)) != len(keys):
            raise ValueError("Duplicate source identifiers")
        self.catalog_sources = [dict(row) for row in sources]
        return {"loaded": len(keys),
                "domains": sorted(set(x["area"] for x in sources))}

    def source_by_id(self, source_id: str) -> Dict | None:
        """Resolve exactly one study source without erasing its provenance."""
        return next((dict(s) for s in self.catalog_sources
                     if s["id"] == source_id), None)

    def search_sources(self, query: str, *, area: str | None = None) -> List[Dict]:
        """Retrieve actionable technique/lab instructions with source URLs."""
        needle = query.casefold().strip()
        if not needle:
            return []
        fields = ("title", "technique", "experiment", "area", "type")
        return [dict(s) for s in self.catalog_sources
                if (area is None or s["area"].casefold() == area.casefold())
                and any(needle in s.get(f, "").casefold() for f in fields)]

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
