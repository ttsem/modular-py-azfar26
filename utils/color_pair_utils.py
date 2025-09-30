from constants.colors import MAJOR_COLORS, MINOR_COLORS


def color_pair_to_string(major_color: str, minor_color: str) -> str:
    return f"{major_color} {minor_color}"


def get_color_from_pair_number(pair_number: int) -> tuple[str, str]:
    zero_based_pair_number = pair_number - 1
    major_index = zero_based_pair_number // len(MINOR_COLORS)
    if major_index >= len(MAJOR_COLORS):
        raise ValueError("Major index out of range")
    minor_index = zero_based_pair_number % len(MINOR_COLORS)
    if minor_index >= len(MINOR_COLORS):
        raise ValueError("Minor index out of range")
    return MAJOR_COLORS[major_index], MINOR_COLORS[minor_index]


def get_pair_number_from_color(major_color: str, minor_color: str) -> int:
    try:
        major_index = MAJOR_COLORS.index(major_color)
    except ValueError:
        raise ValueError("Major index out of range")
    try:
        minor_index = MINOR_COLORS.index(minor_color)
    except ValueError:
        raise ValueError("Minor index out of range")
    return major_index * len(MINOR_COLORS) + minor_index + 1
