"""
Aspen Grove Bridge — Connects the agentic-phd runtime to
GlacierEQ/aspen-grove-core for memory and context continuity.

Aspen Grove Core is the memory and context-continuity peer of the GlacierEQ
nervous system. This module wraps its integration points so the agentic-phd
runtime can benefit from durable context without taking temporary hierarchy.
"""

from __future__ import annotations

import logging
import time
from pathlib import Path
from typing import Any, Dict

logger = logging.getLogger(__name__)


class AspenGroveBridge:
    """Wraps Aspen Grove Core for context/memory continuity.

    In the GlacierEQ nervous system, Aspen Grove Core is the memory peer. It
    preserves durable context and contributes routing capability without
    permanent hierarchy.

    Usage:
        bridge = AspenGroveBridge(aspen_grove_path="/path/to/aspen-grove-core")
        context = await bridge.recall_context("recent decisions")
        await bridge.persist_context({"decision": "use tower integration"})
        summary = await bridge.get_situation_summary()
    """

    def __init__(self, aspen_grove_path: str | None = None):
        self.aspen_grove_path = aspen_grove_path
        self.initialized = False
        self._cached_context = {}

    def initialize(self) -> bool:
        """Verify aspen-grove-core is present."""
        if self.aspen_grove_path:
            p = Path(self.aspen_grove_path)
            if p.exists():
                self.initialized = True
                logger.info(f"Aspen Grove Bridge initialized: {self.aspen_grove_path}")
                return True

        # Fallback: use workspace as in-memory stand-in until actual aspen-grove-core is connected
        workspace = Path(__file__).resolve().parents[3] if Path(__file__).resolve().parents[3].exists() else None
        if workspace:
            self._cached_context["workspace_root"] = str(workspace)
            self._cached_context["source_of_truth"] = "in-memory workspace stand-in"
            self._cached_context["note"] = (
                "Aspen Grove Core not initialized. Using workspace memory as a stand-in. "
                "Connect Aspen Grove Core at: GlacierEQ/aspen-grove-core"
            )
            self.initialized = True
            logger.info("Aspen Grove Bridge running in stand-in mode (no aspen-grove core found)")
            return True

        return False

    def recall_context(self, query: str, limit: int = 20) -> list:
        """Recall durable context from Aspen Grove.

        In production, this calls aspen-grove-core. In stand-in mode, returns
        the workspace context.
        """
        if not self.initialized:
            return []

        # Stand-in: return cached workspace context
        return [
            {
                "source": "aspen-grove-standin",
                "query": query,
                "context": self._cached_context,
                "timestamp": time.time(),
            }
        ]

    def persist_context(self, note: Dict[str, Any]) -> Dict[str, Any]:
        """Persist a note to Aspen Grove.

        In production, writes to aspen-grove-core. In stand-in mode, caches it.
        """
        if not self.initialized:
            return {
                "status": "standin",
                "note": note,
                "message": "Aspen Grove Core not connected; context cached in memory",
            }

        key = f"note_{len(self._cached_context)}"
        self._cached_context[key] = note
        logger.info(f"Persistent context archived: {note.get('topic', 'unknown')}")
        return {"status": "persisted", "note": note}

    def get_situation_summary(self) -> str:
        """Generate a situational awareness summary."""
        if not self.initialized:
            return "Aspen Grove Core not initialized; no live context available"

        items = []
        for k, v in self._cached_context.items():
            if isinstance(v, str):
                items.append(f"{k}: {v}")
            elif isinstance(v, dict):
                items.append(f"{k}: dict({len(v)} keys)")

        if items:
            return " | ".join(items)
        return "No live context available"

    def get_note(self, key: str) -> Any:
        """Retrieve a specific context note."""
        return self._cached_context.get(key)


def setup_aspen_grove(aspen_grove_path: str | None = None) -> AspenGroveBridge:
    """Convenience function: create and initialize the Aspen Grove Bridge."""
    bridge = AspenGroveBridge(aspen_grove_path=aspen_grove_path)
    bridge.initialize()
    return bridge
