"""
Coding Reasoning — Code Analysis, Refactoring Patterns, Structural Thinking
Agentic Upgrade for AI Agent Capability Enhancement
"""
import ast
import re
from typing import List, Dict, Tuple


def cyclomatic_complexity(code: str) -> int:
    """Estimate cyclomatic complexity via AST branch counting."""
    try:
        tree = ast.parse(code)
    except SyntaxError:
        return -1
    complexity = 1
    for node in ast.walk(tree):
        if isinstance(node, (ast.If, ast.For, ast.While, ast.ExceptHandler, ast.With, ast.Assert)):
            complexity += 1
        elif isinstance(node, ast.BoolOp):
            complexity += len(node.values) - 1
    return complexity


def extract_dependencies(code: str) -> List[str]:
    """Extract import statements from Python code."""
    deps = []
    try:
        tree = ast.parse(code)
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                for alias in node.names:
                    deps.append(alias.name)
            elif isinstance(node, ast.ImportFrom):
                if node.module:
                    deps.append(node.module)
    except SyntaxError:
        pass
    return list(set(deps))


def identify_patterns(code: str) -> List[str]:
    """Identify common design patterns in code."""
    patterns = []
    if "class " in code and "__init__" in code:
        patterns.append("Class-based OOP")
    if "def " in code and "yield" in code:
        patterns.append("Generator")
    if "async def" in code:
        patterns.append("Async/Await")
    if "try:" in code and "except" in code:
        patterns.append("Error Handling")
    if "lambda " in code:
        patterns.append("Functional (Lambda)")
    if "decorator" in code.lower() or "@" in code:
        patterns.append("Decorator")
    return patterns


def code_smell_detector(code: str) -> List[str]:
    """Detect common code smells."""
    smells = []
    lines = code.split('\n')
    if len(lines) > 300:
        smells.append("Long file (>300 lines)")
    for i, line in enumerate(lines, 1):
        if len(line) > 120:
            smells.append(f"Long line {i} ({len(line)} chars)")
        if line.strip().startswith("except:"):
            smells.append(f"Bare except at line {i}")
    if code.count("TODO") > 3:
        smells.append("Multiple TODOs")
    if "eval(" in code or "exec(" in code:
        smells.append("Dangerous eval/exec usage")
    return smells


def refactoring_suggestion(complexity: int, smells: List[str]) -> str:
    """Suggest refactoring based on analysis."""
    if complexity > 15:
        return "HIGH: Extract methods, reduce branching. Consider state machine or strategy pattern."
    if complexity > 8:
        return "MEDIUM: Simplify conditionals, extract helper functions."
    if smells:
        return f"LOW: Address code smells: {', '.join(smells[:3])}"
    return "NONE: Code structure is clean."


if __name__ == "__main__":
    print("=== Coding Reasoning: Code Analysis ===")
    sample = '''
def process(data):
    if data.get("type") == "A":
        for item in data["items"]:
            if item > 0:
                try:
                    result = item / 2
                except:
                    result = 0
            else:
                result = -1
    elif data.get("type") == "B":
        result = sum(data["items"])
    else:
        result = None
    return result
'''
    cc = cyclomatic_complexity(sample)
    print(f"  Cyclomatic complexity: {cc}")
    deps = extract_dependencies("import os\nfrom typing import List\nimport json")
    print(f"  Dependencies: {deps}")
    patterns = identify_patterns(sample)
    print(f"  Patterns: {patterns}")
    smells = code_smell_detector(sample)
    print(f"  Smells: {smells}")
    suggestion = refactoring_suggestion(cc, smells)
    print(f"  Suggestion: {suggestion}")
    print("✓ Coding Reasoning module complete.")
