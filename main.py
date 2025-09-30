import json

from tests.test_color_pair_utils import (
    test_number_to_pair,
    test_pair_to_number,
)
from tests.test_reference_manual import test_mapping, test_number_of_entries
from utils.reference_manual_generator import generate_reference_manual

if __name__ == "__main__":
    # Run tests on color pair utils
    test_number_to_pair(4, "White", "Brown")
    test_number_to_pair(5, "White", "Slate")
    test_pair_to_number("Black", "Orange", 12)
    test_pair_to_number("Violet", "Slate", 25)
    test_pair_to_number("Red", "Orange", 7)

    # Run tests on reference manual generation
    test_number_of_entries()
    test_mapping()
    print("All tests passed!")

    # Print reference manual
    print(json.dumps(generate_reference_manual(), indent=4))
