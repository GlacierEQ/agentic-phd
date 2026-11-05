"""
Reinforcement Learning — Q-Learning, Policy Gradients, Offline RL
Doctorate-level AI curriculum — Agentic PhD
"""
import math
import random
from typing import List, Dict, Tuple


def q_learning_update(q: float, reward: float, next_max_q: float, alpha: float, gamma: float) -> float:
    """Q(s,a) <- Q(s,a) + alpha * (r + gamma * max_a' Q(s',a') - Q(s,a))."""
    return q + alpha * (reward + gamma * next_max_q - q)


def sarsa_update(q: float, reward: float, next_q: float, alpha: float, gamma: float) -> float:
    """SARSA: Q(s,a) <- Q(s,a) + alpha * (r + gamma * Q(s',a') - Q(s,a))."""
    return q + alpha * (reward + gamma * next_q - q)


def policy_gradient_loss(log_prob: float, advantage: float) -> float:
    """Policy gradient: -log_prob * advantage."""
    return -log_prob * advantage


def ppo_clip_loss(log_prob_ratio: float, advantage: float, epsilon: float = 0.2) -> float:
    """PPO clipped objective."""
    clipped = min(max(log_prob_ratio, 1 - epsilon), 1 + epsilon)
    return -min(log_prob_ratio * advantage, clipped * advantage)


def bellman_residual(v: float, reward: float, next_v: float, gamma: float) -> float:
    """Bellman residual: |V(s) - (r + gamma * V(s'))|."""
    return abs(v - (reward + gamma * next_v))


def td_lambda_update(q: float, reward: float, next_q: float, trace: float, alpha: float, gamma: float, lam: float) -> float:
    """TD(lambda) update."""
    delta = reward + gamma * next_q - q
    return q + alpha * delta * trace


if __name__ == "__main__":
    print("=== Reinforcement Learning ===")
    print(f"Q-learning update: {q_learning_update(0.5, 1.0, 0.8, 0.1, 0.9):.4f}")
    print(f"SARSA update: {sarsa_update(0.5, 1.0, 0.7, 0.1, 0.9):.4f}")
    print(f"Policy gradient loss: {policy_gradient_loss(-0.5, 2.0):.4f}")
    print(f"PPO clip loss: {ppo_clip_loss(1.1, 0.5):.4f}")
    print(f"Bellman residual: {bellman_residual(0.8, 1.0, 0.7, 0.9):.4f}")
    print(f"TD(lambda) update: {td_lambda_update(0.5, 1.0, 0.8, 0.9, 0.1, 0.9, 0.8):.4f}")
    print("✓ RL module complete.")
