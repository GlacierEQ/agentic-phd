"""
Error Handling — Resilience, Recovery, Graceful Degradation, Retry Strategies
Agentic Upgrade for AI Agent Capability Enhancement
"""
import time
import random
from typing import List, Dict, Callable, Tuple
from functools import wraps


def retry_with_backoff(fn: Callable, max_retries: int = 3, base_delay: float = 0.1, max_delay: float = 10.0) -> Dict:
    """Retry with exponential backoff and jitter."""
    for attempt in range(max_retries):
        try:
            result = fn()
            return {"status": "success", "result": result, "attempts": attempt + 1}
        except Exception as e:
            if attempt == max_retries - 1:
                return {"status": "failed", "error": str(e), "attempts": max_retries}
            delay = min(base_delay * (2 ** attempt), max_delay)
            jitter = random.uniform(0, delay * 0.1)
            time.sleep(delay + jitter)
    return {"status": "failed", "attempts": max_retries}


def circuit_breaker(fn: Callable, failure_threshold: int = 5, recovery_timeout: float = 30.0) -> Callable:
    """Circuit breaker pattern: open after N failures, half-open after timeout."""
    state = {"failures": 0, "state": "closed", "last_failure": 0.0}

    def wrapper(*args, **kwargs):
        now = time.time()
        if state["state"] == "open":
            if now - state["last_failure"] > recovery_timeout:
                state["state"] = "half-open"
            else:
                raise Exception("Circuit breaker is OPEN")
        try:
            result = fn(*args, **kwargs)
            state["failures"] = 0
            state["state"] = "closed"
            return result
        except Exception as e:
            state["failures"] += 1
            state["last_failure"] = now
            if state["failures"] >= failure_threshold:
                state["state"] = "open"
            raise e
    return wrapper


def graceful_degradation(primary: Callable, fallback: Callable, default=None) -> Callable:
    """Try primary, fall back gracefully."""
    def wrapper(*args, **kwargs):
        try:
            return primary(*args, **kwargs)
        except Exception:
            try:
                return fallback(*args, **kwargs)
            except Exception:
                return default
    return wrapper


def bulkhead(fn: Callable, max_concurrent: int = 10) -> Callable:
    """Bulkhead pattern: limit concurrent executions."""
    import threading
    semaphore = threading.Semaphore(max_concurrent)

    def wrapper(*args, **kwargs):
        with semaphore:
            return fn(*args, **kwargs)
    return wrapper


def error_classification(error: Exception) -> str:
    """Classify errors for appropriate handling."""
    error_type = type(error).__name__
    if "Timeout" in error_type or "timeout" in str(error).lower():
        return "TRANSIENT"
    if "Connection" in error_type or "Network" in error_type:
        return "TRANSIENT"
    if "Auth" in error_type or "Permission" in error_type:
        return "PERMANENT"
    if "Value" in error_type or "Type" in error_type:
        return "CLIENT_ERROR"
    return "UNKNOWN"


if __name__ == "__main__":
    print("=== Error Handling: Resilience ===")
    # Retry
    attempts = [0]
    def flaky():
        attempts[0] += 1
        if attempts[0] < 3:
            raise Exception("transient failure")
        return "success"
    r = retry_with_backoff(flaky, max_retries=5, base_delay=0.01)
    print(f"  Retry: {r}")

    # Circuit breaker
    cb = circuit_breaker(lambda: (_ for _ in ()).throw(Exception("fail")), failure_threshold=2)
    for i in range(3):
        try:
            cb()
        except Exception as e:
            print(f"  Circuit breaker attempt {i+1}: {e}")

    # Graceful degradation
    gd = graceful_degradation(lambda: (_ for _ in ()).throw(Exception("fail")), lambda: "fallback", default="default")
    print(f"  Graceful degradation: {gd()}")

    # Error classification
    print(f"  TimeoutError -> {error_classification(TimeoutError('timed out'))}")
    print(f"  ValueError -> {error_classification(ValueError('bad value'))}")
    print("✓ Error Handling module complete.")
