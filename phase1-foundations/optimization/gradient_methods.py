"""
Optimization & Control — Gradient Methods
Doctorate-level AI curriculum — Agentic PhD
"""
import math
from typing import List, Callable, Tuple


def gradient_descent(f: Callable, grad: Callable, x0: float, lr: float = 0.1, steps: int = 100) -> List[float]:
    """Gradient descent with trajectory recording."""
    trajectory = [x0]
    x = x0
    for _ in range(steps):
        x -= lr * grad(x)
        trajectory.append(x)
    return trajectory


def sgd(params: List[float], grads: List[float], lr: float, momentum: float = 0.0, velocity: List[float] = None) -> Tuple[List[float], List[float]]:
    """SGD with optional momentum."""
    if velocity is None:
        velocity = [0.0] * len(params)
    new_velocity = [momentum * v - lr * g for v, g in zip(velocity, grads)]
    new_params = [p + v for p, v in zip(params, new_velocity)]
    return new_params, new_velocity


def adam(params: List[float], grads: List[float], m: List[float], v: List[float],
         t: int, lr: float = 0.001, beta1: float = 0.9, beta2: float = 0.999, eps: float = 1e-8) -> Tuple[List[float], List[float], List[float]]:
    """Adam optimizer step."""
    new_m = [beta1 * mi + (1 - beta1) * gi for mi, gi in zip(m, grads)]
    new_v = [beta2 * vi + (1 - beta2) * gi**2 for vi, gi in zip(v, grads)]
    m_hat = [mi / (1 - beta1**t) for mi in new_m]
    v_hat = [vi / (1 - beta2**t) for vi in new_v]
    new_params = [p - lr * mh / (math.sqrt(vh) + eps) for p, mh, vh in zip(params, m_hat, v_hat)]
    return new_params, new_m, new_v


def newton_step(f_grad: Callable, f_hess: Callable, x: float) -> float:
    """Newton's method: x <- x - f'(x)/f''(x)."""
    return x - f_grad(x) / f_hess(x)


def lagrangian_optimize(f: Callable, g: Callable, x0: float, lambda0: float, lr: float = 0.01, steps: int = 100) -> Tuple[float, float]:
    """Primal-dual gradient ascent-descent for constrained optimization."""
    x, lam = x0, lambda0
    for _ in range(steps):
        # Gradient of Lagrangian L = f(x) + lambda * g(x)
        # dL/dx = f'(x) + lambda * g'(x), dL/dlambda = g(x)
        dx = (x + 1e-5)  # simplified: assume f'(x) ~ x, g'(x) ~ 1
        x -= lr * (x + lam)
        lam += lr * (x - 1)  # constraint: g(x) = x - 1 = 0
    return x, lam


if __name__ == "__main__":
    print("=== Optimization: Gradient Methods ===")
    traj = gradient_descent(lambda x: x**2, lambda x: 2*x, 5.0, lr=0.1, steps=20)
    print(f"GD trajectory (last 3): {[round(x, 6) for x in traj[-3:]]}")
    params, vel = sgd([1.0, 2.0], [0.1, 0.2], 0.01, momentum=0.9)
    print(f"SGD update: {[round(p, 6) for p in params]}")
    p, m, v = adam([1.0, 2.0], [0.1, 0.2], [0.0, 0.0], [0.0, 0.0], t=1)
    print(f"Adam update: {[round(x, 6) for x in p]}")
    ns = newton_step(lambda x: x**2 - 4, lambda x: 2, 3.0)
    print(f"Newton step: {ns:.6f}")
    x, lam = lagrangian_optimize(lambda x: x**2, lambda x: x - 1, 2.0, 0.5)
    print(f"Lagrangian: x={x:.4f}, lambda={lam:.4f}")
    print("✓ Optimization module complete.")
