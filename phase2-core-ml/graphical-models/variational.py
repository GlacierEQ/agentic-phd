"""
Probabilistic Graphical Models — Variational Inference, VAEs
Doctorate-level AI curriculum — Agentic PhD
"""
import math
from typing import List


def elbo(reconstruction: float, kl_divergence: float) -> float:
    """ELBO = E[log p(x|z)] - KL(q(z|x) || p(z))."""
    return reconstruction - kl_divergence


def kl_gaussian(mu_q: float, logvar_q: float, mu_p: float = 0.0, logvar_p: float = 0.0) -> float:
    """KL(N(mu_q, exp(logvar_q)) || N(mu_p, exp(logvar_p)))."""
    var_q = math.exp(logvar_q)
    var_p = math.exp(logvar_p)
    return 0.5 * (logvar_p - logvar_q + (var_q + (mu_q - mu_p)**2) / var_p - 1)


def reparameterize(mu: float, logvar: float, epsilon: float) -> float:
    """z = mu + exp(0.5 * logvar) * epsilon."""
    return mu + math.exp(0.5 * logvar) * epsilon


def mean_field_update(q_params: List[float], likelihood_grad: List[float], lr: float) -> List[float]:
    """Mean-field variational update: q_i <- q_i + lr * grad."""
    return [q + lr * g for q, g in zip(q_params, likelihood_grad)]


def bethe_free_energy(energy: float, entropy: float, temperature: float = 1.0) -> float:
    """Bethe free energy: F = E - T*S."""
    return energy - temperature * entropy


if __name__ == "__main__":
    print("=== Probabilistic Graphical Models: Variational Inference ===")
    print(f"ELBO (recon=0.9, kl=0.3): {elbo(0.9, 0.3):.4f}")
    print(f"KL(q||p): {kl_gaussian(0.5, 0.0):.4f}")
    z = reparameterize(0.0, 0.0, 1.0)
    print(f"Reparameterized z: {z:.4f}")
    mf = mean_field_update([0.5, 0.3], [0.1, -0.2], 0.01)
    print(f"Mean-field update: {[round(x, 4) for x in mf]}")
    print(f"Bethe free energy: {bethe_free_energy(1.0, 0.5):.4f}")
    print("✓ Graphical Models module complete.")
