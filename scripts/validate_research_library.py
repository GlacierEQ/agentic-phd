#!/usr/bin/env python3
"""Deterministic, offline validation of the authoritative research source index."""
from __future__ import annotations
import json
import sys
from collections import Counter
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]
CATALOG = ROOT / "resources/research/frontier_sources.json"


def validate(path: Path = CATALOG) -> dict:
    raw = json.loads(path.read_text(encoding="utf-8"))
    if raw.get("schema") != "glaciereq.agentic-phd.research-library.v1":
        raise ValueError("Unknown library schema")
    entries = raw.get("sources")
    if not isinstance(entries, list) or len(entries) < 30:
        raise ValueError("Research library requires at least 30 sourced items")
    ids, urls, areas = set(), set(), Counter()
    for index, row in enumerate(entries):
        if not isinstance(row, dict):
            raise ValueError(f"Source {index} must be a record")
        required = ("id", "area", "title", "url", "type", "technique", "experiment", "review_status", "implementation_status")
        if any(not isinstance(row.get(k), str) or not row[k].strip() for k in required):
            raise ValueError(f"Missing typed provenance or experiment at source {index}")
        parsed = urlparse(row["url"])
        if parsed.scheme != "https" or not parsed.netloc or parsed.username or parsed.password:
            raise ValueError(f"Untrusted or malformed HTTPS source: {index}")
        if row["id"] in ids or row["url"] in urls:
            raise ValueError(f"Duplicate identity or URL: {index}")
        if row["review_status"] not in {"public_source_checked_2026-11-05", "canonical_url_requires_live_recheck"}:
            raise ValueError(f"Invalid provenance status: {index}")
        if row["implementation_status"] != "proposed_lab_not_run":
            raise ValueError(f"Catalog may not claim unsupported lab execution: {index}")
        ids.add(row["id"]); urls.add(row["url"]); areas[row["area"]] += 1
    if len(areas) < 7:
        raise ValueError("Research domains insufficiently broad")
    return {"schema":raw["schema"], "count":len(entries), "domains":dict(areas), "unique_ids":len(ids), "unique_urls":len(urls), "verified_source_checks":sum(s["review_status"].startswith("public_source_checked") for s in entries)}


if __name__ == "__main__":
    try:
        print(json.dumps(validate(), sort_keys=True, indent=2))
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        print(f"RESEARCH_LIBRARY_VALIDATION_FAILED: {exc}", file=sys.stderr)
        raise SystemExit(1)
