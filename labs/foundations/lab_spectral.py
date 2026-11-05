"""Lab: Spectral decomposition and matrix rank."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'phase1-foundations', 'linear-algebra'))
from spectral import eigenvalues_2x2, matrix_rank, frobenius_norm, spectral_norm_approx

def main():
    print("Lab: Spectral Decomposition")
    ev = eigenvalues_2x2(4, 2, 1, 3)
    print(f"  Eigenvalues: {ev}")
    r = matrix_rank([[1,2,3],[4,5,6],[7,8,9]])
    print(f"  Rank: {r}")
    fn = frobenius_norm([[1,2],[3,4]])
    print(f"  Frobenius norm: {fn:.4f}")
    sn = spectral_norm_approx([[1,2],[3,4]])
    print(f"  Spectral norm: {sn:.4f}")
    assert r == 2
    print("✓ Lab passed.")

if __name__ == "__main__":
    main()
