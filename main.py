import json

from tests.test_color_pair_number import (
    test_number_to_pair,
    test_pair_to_number,
)
from utils.reference_manual import generate_reference_manual

if __name__ == "__main__":
    test_number_to_pair(4, "White", "Brown")
    test_number_to_pair(5, "White", "Slate")
    test_pair_to_number("Black", "Orange", 12)
    test_pair_to_number("Violet", "Slate", 25)
    test_pair_to_number("Red", "Orange", 7)
    print(json.dumps(generate_reference_manual(), indent=4))
