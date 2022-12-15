import pytest

from avatar_initials_py.colors import lightness


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
