from constants.colors import MAJOR_COLORS, MINOR_COLORS
from utils.color_pair_utils import get_color_from_pair_number


def generate_reference_manual() -> dict:
    color_manual = {}
    max_pairs = len(MAJOR_COLORS) * len(MINOR_COLORS)
    for pair_number in range(1, max_pairs + 1):
        major, minor = get_color_from_pair_number(pair_number)
        color_manual[f"{major} {minor}"] = pair_number
    return color_manual
