#!/usr/bin/env python3
"""Source-verified, task-selected coding methods for the existing Agentic PhD tracker.

This selects research-backed techniques. It never performs a mutation, runs
model inference, certifies software, or replaces the existing Spiral Engine.
"""
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ROUTES = ROOT / "resources/research/code_intelligence_routes.json"
CATALOG = ROOT / "resources/research/frontier_sources.json"
TRACKER = ROOT / "phase4-research/literature/tracker.py"
EXPECTED_SCHEMA = "glaciereq.agentic-phd.code-intelligence.routes.v1"
KNOWN_TOOLS = {"code:inspect", "code:knowledge", "code:refactor", "code:fix", "eval:harness"}


def _tracker(catalog_path: Path):
    """Reuse the existing research tracker rather than creating a second catalog."""
    spec = importlib.util.spec_from_file_location("agentic_phd_paper_tracker", TRACKER)
    if spec is None or spec.loader is None:
        raise ValueError("Original research tracker cannot be loaded")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    tracker = module.PaperTracker()
    tracker.load_frontier_library(catalog_path)
    return tracker


def _checked_path(root: Path, candidate: object) -> Path:
    if not isinstance(candidate, str) or not candidate:
        raise ValueError("Missing source-package path")
    p = Path(candidate)
    if p.is_absolute() or ".." in p.parts:
        raise ValueError("Source-package path escapes repository")
    resolved = (root / p).resolve()
    if not resolved.is_relative_to(root.resolve()) or not resolved.is_file():
        raise ValueError("Source-package file missing or outside repository")
    return resolved


def validate_routes(
    routes_path: Path = ROUTES,
    catalog_path: Path = CATALOG,
    package_root: Path = ROOT,
) -> dict:
    """Validate import integrity, route identities and original tracker links."""
    raw = json.loads(Path(routes_path).read_text(encoding="utf-8"))
    if raw.get("schema") != EXPECTED_SCHEMA:
        raise ValueError("Unknown code-intelligence route schema")
    if raw.get("execution_status") != "research_method_guidance_only_not_executed":
        raise ValueError("Guidance cannot self-certify execution")
    if raw.get("runtime_owner") != "GlacierEQ/pro-code" or raw.get("spiral_owner") != "GlacierEQ/spiral-engine":
        raise ValueError("Existing runtime and Spiral owners must remain separate")
    package = raw.get("package", {})
    if package.get("name") != "glaciereq-intelligence-harness" or package.get("version") != "0.1.35":
        raise ValueError("Unexpected pinned source package")
    for stem in ("skill", "methods"):
        source = _checked_path(Path(package_root), package.get(stem + "_path"))
        actual = hashlib.sha256(source.read_bytes()).hexdigest()
        if actual != package.get(stem + "_sha256"):
            raise ValueError("Imported source differs from pinned uploaded package: " + stem)
    tracker = _tracker(Path(catalog_path))
    routes = raw.get("routes")
    if not isinstance(routes, list) or len(routes) < 6:
        raise ValueError("Too few concrete coding decision routes")
    seen = set()
    cited = set()
    for row in routes:
        if not isinstance(row, dict):
            raise ValueError("Route must be a record")
        required = ("mode", "problem", "first_probe", "experiment", "acceptance", "risk")
        if any(not isinstance(row.get(k), str) or not row[k].strip() for k in required):
            raise ValueError("Route missing executable method or acceptance criterion")
        mode = row["mode"]
        if not mode.replace("_", "").isalnum() or mode in seen:
            raise ValueError("Duplicate or invalid coding mode")
        seen.add(mode)
        tools = row.get("owner_tools")
        source_ids = row.get("source_ids")
        if not isinstance(tools, list) or not tools or any(t not in KNOWN_TOOLS for t in tools):
            raise ValueError("Unsupported or missing existing owner tool")
        if not isinstance(source_ids, list) or not source_ids or len(set(source_ids)) != len(source_ids):
            raise ValueError("Missing/duplicate primary source IDs")
        for source_id in source_ids:
            source = tracker.source_by_id(source_id)
            if source is None:
                raise ValueError("Unknown catalog source: " + str(source_id))
            if source["implementation_status"] != "proposed_lab_not_run":
                raise ValueError("Catalog source improperly claims experiment success")
            cited.add(source_id)
    return {
        "schema": EXPECTED_SCHEMA, "routes": len(routes), "source_ids": len(cited),
        "catalog_sources": len(tracker.catalog_sources),
        "package_version": package["version"], "source_package_hashes_verified": True,
        "existing_tracker_reused": True,
        "execution_status": raw["execution_status"],
    }


def select_route(
    mode: str, *, routes_path: Path = ROUTES,
    catalog_path: Path = CATALOG,
    package_root: Path = ROOT,
) -> dict:
    validated = validate_routes(routes_path, catalog_path, package_root)
    routes = json.loads(Path(routes_path).read_text(encoding="utf-8"))
    selected = next((row for row in routes["routes"] if row["mode"] == mode), None)
    if selected is None:
        raise ValueError("Unknown code-intelligence mode: " + mode)
    tracker = _tracker(Path(catalog_path))
    return {
        "mode": mode, "method": dict(selected),
        "research_sources": [tracker.source_by_id(sid) for sid in selected["source_ids"]],
        "source_package_version": validated["package_version"],
        "runtime_owner": routes["runtime_owner"],
        "spiral_owner": routes["spiral_owner"],
        "execution_status": validated["execution_status"],
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Select a verifiable coding method; never execute it implicitly.")
    sub = parser.add_subparsers(dest="command", required=True)
    sub.add_parser("validate")
    sub.add_parser("list")
    sub.add_parser("select").add_argument("mode")
    args = parser.parse_args(argv)
    try:
        report = validate_routes()
        if args.command == "validate":
            output = report
        elif args.command == "list":
            raw = json.loads(ROUTES.read_text(encoding="utf-8"))
            output = [{"mode": r["mode"], "problem": r["problem"]} for r in raw["routes"]]
        else:
            output = select_route(args.mode)
        print(json.dumps(output, indent=2, sort_keys=True))
        return 0
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        print("CODE_INTELLIGENCE_VALIDATION_FAILED: " + str(exc), file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
