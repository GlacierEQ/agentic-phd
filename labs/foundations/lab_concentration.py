"""Lab: Concentration inequalities."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'phase1-foundations', 'probability'))
from concentration import hoeffding_bound, chernoff_bound, sample_complexity_pac

def main():
    print("Lab: Concentration Inequalities")
    hb = hoeffding_bound(1000, 0.05)
    print(f"  Hoeffding: {hb:.6f}")
    cb = chernoff_bound(100, 0.1, 0.5)
    print(f"  Chernoff: {cb:.6f}")
    sc = sample_complexity_pac(0.1, 0.05, 10)
    print(f"  PAC sample complexity: {sc}")
    assert hb < 0.1
    print("✓ Lab passed.")

if __name__ == "__main__":
    main()
