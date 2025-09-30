from constants.colors import MAJOR_COLORS, MINOR_COLORS
from utils.reference_manual_generator import generate_reference_manual


def test_number_of_entries():
    reference_manual = generate_reference_manual()
    expected_count = len(MAJOR_COLORS) * len(MINOR_COLORS)
    assert len(reference_manual) == expected_count


def test_mapping(self):
    reference_manual = generate_reference_manual()
    assert reference_manual.get("White Blue") == 1
    assert reference_manual.get("Red Blue") == 6
    assert reference_manual.get("violet Slate") == 25
