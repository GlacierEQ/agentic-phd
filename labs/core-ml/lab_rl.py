"""Lab: Q-learning and policy gradients."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'phase2-core-ml', 'reinforcement-learning'))
from q_learning import q_learning_update, policy_gradient_loss, ppo_clip_loss

def main():
    print("Lab: Reinforcement Learning")
    q = q_learning_update(0.5, 1.0, 0.8, 0.1, 0.9)
    print(f"  Q-update: {q:.4f}")
    pg = policy_gradient_loss(-0.5, 2.0)
    print(f"  PG loss: {pg:.4f}")
    ppo = ppo_clip_loss(1.1, 0.5)
    print(f"  PPO loss: {ppo:.4f}")
    assert q > 0.5
    print("✓ Lab passed.")

if __name__ == "__main__":
    main()
