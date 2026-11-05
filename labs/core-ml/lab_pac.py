"""Lab: PAC learning and VC dimension."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'phase2-core-ml', 'learning-theory'))
from pac import pac_sample_complexity, vc_dimension_intervals, generalization_bound, rademacher_complexity

def main():
    print("Lab: PAC Learning")
    m = pac_sample_complexity(0.1, 0.05, 10)
    print(f"  Sample complexity: {m}")
    rc = rademacher_complexity(1000, 1.0)
    gb = generalization_bound(0.1, rc, 1000, 0.05)
    print(f"  Generalization bound: {gb:.4f}")
    assert m > 0 and gb < 1.0
    print("✓ Lab passed.")

if __name__ == "__main__":
    main()
