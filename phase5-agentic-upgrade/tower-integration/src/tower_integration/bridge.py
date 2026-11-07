"""
Tower Bridge — Connects the agentic-phd sequential thinking module to the
Tower of Babel (GlacierEQ/the-tower-of-babel) proof system.

This module wires the agentic-phd capability execution path into the Tower's
technology placement, proof, and receipt system, using Aspen Grove Core for
context/memory continuity.

Integration points:
- Phase 5 agentic upgrade modules (coding-reasoning, sequential-thinking)
- Tower of Babel technology placement and proof system
- Aspen Grove Core memory and context continuity
"""

from __future__ import annotations

import json
import logging
import sys
from pathlib import Path
from typing import Any, Dict, List, Optional

logger = logging.getLogger(__name__)


class TowerBridge:
    """Bridges the agentic-phd runtime to the Tower of Babel proof system.

    Usage:
        bridge = TowerBridge()
        result = await bridge.route_mission(
            mission="Integrate Tower of Babel with Aspen Grove Core",
            context={"runtime": "agentic-phd", "tower": "glaciereq/the-tower-of-babel"}
        )
    """

    def __init__(self, tower_repo_path: str | None = None, aspen_grove_path: str | None = None):
        self.tower_repo = tower_repo_path or "/Users/kcbflux/Workspace/tower-of-babel"
        self.aspen_grove = aspen_grove_path
        self.sequential = None
        self.initialized = False

    def initialize(self) -> bool:
        """Verify tower repo is present and sequential module is importable."""
        tower_path = Path(self.tower_repo)
        if not tower_path.exists():
            raise FileNotFoundError(f"Tower of Babel not found: {self.tower_repo}")

        # Import sequential thinking (agentic-phd module)
        try:
            from phase5_agentic_upgrade.sequential_thinking.sequential_reasons import (
                SequentialReasoner,
            )
            self.sequential = SequentialReasoner()
        except ImportError:
            # Fallback: construct path manually if the package is not installed
            agentic_phd = Path(__file__).resolve().parents[3]
            sys_path = str(agentic_phd)
            if sys_path not in sys.path:
                sys.path.insert(0, sys_path)
            try:
                from sequential_thinking.sequential_reasons import SequentialReasoner
                self.sequential = SequentialReasoner()
            except ImportError as exc:
                raise ImportError(
                    f"Could not import sequential_thinking module. "
                    f"Add {agentic_phd} to PYTHONPATH. Original: {exc}"
                )

        self.initialized = True
        logger.info("TowerBridge initialized: sequential thinking + tower + aspen-grove ready")
        return True

    def route_mission(
        self,
        mission: str,
        context: Dict[str, Any] | None = None,
        steps: List[str] | None = None,
    ) -> Dict[str, Any]:
        """Route the given mission through the tower integration protocol.

        Returns:
            dict: structured result with progress, findings, and next steps.
        """
        if not self.initialized:
            self.initialize()

        if steps is None:
            steps = [
                "Inspect tower registry and identify target technology landscapes",
                "Run sequential reasoning over the mission objective",
                "Map aspen-grove-core memory hooks into the tower placement",
                "Verify cross-language interface contracts",
                "Generate the tower placement plan",
                "Record the receipt and hand off to AKOS",
            ]

        logger.info("TowerBridge: starting integration mission", extra={"mission": mission})

        reasoning = self.sequential.reason(
            problem=mission,
            steps=steps,
            context={
                "tower_repo": self.tower_repo,
                "aspen_grove": self.aspen_grove,
                "runtime": "agentic-phd",
                "integration_target": "tower-of-babel + aspen-grove-core",
            },
        )

        return {
            "mission": mission,
            "status": "INTEGRATION_PLANNED",
            "reasoning_trace": {
                "problem": mission,
                "steps_executed": reasoning.steps,
                "final_answer": reasoning.final_answer,
                "verification_summary": reasoning.verification_summary,
                "avg_confidence": reasoning.avg_confidence,
                "elapsed_seconds": reasoning.elapsed_seconds,
                "thought_id": reasoning.unique_id,
            },
            "next_steps": [
                "Run tower validate on the generated placement",
                "Run pytest on tower integration tests",
                "Emit the receipt and review exact-head CI",
                "Connect to aspen-grove-core memory hooks",
            ],
        }


def run_integration(
    mission: str,
    tower_repo_path: str | None = None,
    aspen_grove_path: str | None = None,
    steps: List[str] | None = None,
) -> Dict[str, Any]:
    """Convenience function: run the tower integration mission."""
    bridge = TowerBridge(tower_repo_path=tower_repo_path, aspen_grove_path=aspen_grove_path)
    return bridge.route_mission(mission=mission, context=None, steps=steps)
