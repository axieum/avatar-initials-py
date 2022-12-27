import random

import pytest
from PIL import ImageColor

from avatar_initials_py.colors import lightness, random_hex_color, lighten


@pytest.mark.parametrize(
    "color, expected",
    [
        ("#ffffff", 255),
        ("#ff0000", 54.21),
        ("#00ff00", 182.38),
        ("#0000ff", 18.41),
        ("#888888", 136),
        ("#000000", 0),
    ],
)
def test_lightness(color: str, expected: float) -> None:
    """
    Tests that the correct lightness for a given colour is returned.

    :param color: hex colour
    :param expected: expected lightness
    """

    assert round(lightness(color), 2) == expected


@pytest.mark.parametrize(
    "color, amount, expected",
    [
        ("#0af182", 80, "#5affd2"),
        ("#8dc6c2", 120, "#ffffff"),
        ("#0388e6", -80, "#003896"),
        ("#ffffff", 42, "#ffffff"),
        ("#3a3a3a", 20, "#4e4e4e"),
        ("#000000", -80, "#000000"),
    ]
)
def test_lighten(color: str, amount: int, expected: str) -> None:
    """
    Tests that colours are correctly lightened or darkened.

    :param color: hex colour
    :param amount: lighten amount
    :param expected: expected lightened colour
    """

    assert lighten(color, amount) == expected


def test_random_color() -> None:
    """Tests the validity of randomly generated hex colour codes"""

    for _ in range(200):
        ImageColor.getrgb(random_hex_color())


def test_random_color_with_custom_random() -> None:
    """Tests randomly generating hex colour codes with a custom random instance"""

    rand: random.Random = random.Random(99)
    assert random_hex_color(rand) == "#ced636"
    assert random_hex_color(rand) == "#c2f202"
