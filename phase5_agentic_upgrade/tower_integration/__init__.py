"""Tower of Babel integration for the agentic-phd runtime.

This module bridges:
- Agentic-phd sequential thinking module
- The Tower of Babel (GlacierEQ/the-tower-of-babel)
- Aspen Grove Core (memory and context continuity)

The directories are hyphenated and not import-safe, so load the bridge by path:

    import importlib.util
    spec = importlib.util.spec_from_file_location(
        "tower_integration_bridge",
        "phase5-agentic-upgrade/tower-integration/src/tower_integration/bridge.py",
    )
    bridge = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(bridge)
    integration = bridge.TowerBridge()
    result = integration.route_mission(mission="...")
"""
