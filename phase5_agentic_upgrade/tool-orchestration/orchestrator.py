"""
Tool Orchestration — Tool Selection, Chaining, Fallback, Parallel Dispatch
Agentic Upgrade for AI Agent Capability Enhancement
"""
from typing import List, Dict, Callable, Tuple
import concurrent.futures
import time


def tool_relevance(tool_desc: str, query: str) -> float:
    """Score tool relevance to query via keyword overlap + specificity."""
    q_words = set(query.lower().split())
    t_words = set(tool_desc.lower().split())
    overlap = len(q_words & t_words)
    specificity = len(t_words) / max(len(q_words), 1)
    return (overlap / max(len(q_words), 1)) * (1 + 0.1 * specificity)


def select_best_tool(query: str, tools: Dict[str, str]) -> str:
    """Select the best tool for a query."""
    scores = {name: tool_relevance(desc, query) for name, desc in tools.items()}
    return max(scores, key=scores.get)


def tool_chain(steps: List[Tuple[str, Callable, Dict]]) -> List:
    """Execute a chain of tools, passing output forward."""
    results = []
    context = {}
    for name, fn, params in steps:
        merged = {**params, **context}
        result = fn(merged)
        results.append({"tool": name, "result": result})
        context[f"{name}_output"] = result
    return results


def parallel_dispatch(tasks: List[Tuple[str, Callable, Dict]], max_workers: int = 4) -> List[Dict]:
    """Dispatch multiple tool calls in parallel."""
    results = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
        future_to_task = {executor.submit(fn, params): (name, params) for name, fn, params in tasks}
        for future in concurrent.futures.as_completed(future_to_task):
            name, params = future_to_task[future]
            try:
                result = future.result()
                results.append({"tool": name, "status": "success", "result": result})
            except Exception as e:
                results.append({"tool": name, "status": "error", "error": str(e)})
    return results


def fallback_chain(primary: Callable, fallbacks: List[Callable], params: Dict) -> Dict:
    """Try primary, then fallbacks until one succeeds."""
    for fn in [primary] + fallbacks:
        try:
            return {"status": "success", "result": fn(params)}
        except Exception as e:
            last_error = str(e)
    return {"status": "failed", "error": last_error}


def retry_with_backoff(fn: Callable, params: Dict, max_retries: int = 3, base_delay: float = 0.1) -> Dict:
    """Retry with exponential backoff."""
    for attempt in range(max_retries):
        try:
            return {"status": "success", "result": fn(params), "attempts": attempt + 1}
        except Exception as e:
            if attempt == max_retries - 1:
                return {"status": "failed", "error": str(e), "attempts": max_retries}
            time.sleep(base_delay * (2 ** attempt))
    return {"status": "failed", "attempts": max_retries}


if __name__ == "__main__":
    print("=== Tool Orchestration ===")
    tools = {
        "search": "search the web for information and documents",
        "calc": "calculate mathematical expressions",
        "read_file": "read contents of a file",
    }
    best = select_best_tool("find information about AI", tools)
    print(f"  Best tool: {best}")

    chain_results = tool_chain([
        ("search", lambda p: f"results for {p.get('query', '')}", {"query": "AI agents"}),
        ("summarize", lambda p: f"summary of {p.get('search_output', '')}", {}),
    ])
    print(f"  Chain: {[r['tool'] for r in chain_results]}")

    parallel = parallel_dispatch([
        ("task1", lambda p: "result1", {}),
        ("task2", lambda p: "result2", {}),
    ])
    print(f"  Parallel: {[(r['tool'], r['status']) for r in parallel]}")

    fb = fallback_chain(lambda p: (_ for _ in ()).throw(Exception("fail")), [lambda p: "fallback ok"], {})
    print(f"  Fallback: {fb}")

    retry = retry_with_backoff(lambda p: "ok", {}, max_retries=2)
    print(f"  Retry: {retry}")
    print("✓ Tool Orchestration module complete.")
