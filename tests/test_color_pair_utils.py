from utils.color_pair_utils import (
    get_color_from_pair_number,
    get_pair_number_from_color,
)


def test_number_to_pair(
    pair_number: int, expected_major_color: str, expected_minor_color: str
):
    major_color, minor_color = get_color_from_pair_number(pair_number)
    assert major_color == expected_major_color
    assert minor_color == expected_minor_color


def test_pair_to_number(
    major_color: str, minor_color: str, expected_pair_number: int
):
    pair_number = get_pair_number_from_color(major_color, minor_color)
    assert pair_number == expected_pair_number
