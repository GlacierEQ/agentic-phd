"""Lab: Dissertation outline generation."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'phase4-research', 'dissertation'))
from structure import generate_outline, word_count_estimate, defense_checklist

def main():
    print("Lab: Dissertation")
    outline = generate_outline("Test Thesis")
    print(f"  Title: {outline['title']}")
    print(f"  Chapters: {len(outline['chapters'])}")
    wc = word_count_estimate(outline["chapters"])
    print(f"  Est. words: {wc:,}")
    assert len(outline["chapters"]) == 6
    print("✓ Lab passed.")

if __name__ == "__main__":
    main()
