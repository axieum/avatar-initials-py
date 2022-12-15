import pytest

from avatar_initials_py.text import initials


@pytest.mark.parametrize(
    "name, count, expected",
    [
        ("John", 2, "J"),
        ("John Doe", 1, "J"),
        ("John Doe", 2, "JD"),
        ("John Doe", 3, "JD"),
        ("John Matthew Doe", 2, "JD"),
        ("John Matthew Doe", 3, "JMD"),
        ("DOE, John", 1, "J"),
        ("DOE, John", 2, "JD"),
        ("DOE, John", 3, "JD"),
        ("DOE, John Matthew", 2, "JD"),
        ("DOE, John Matthew", 3, "JMD"),
    ],
)
def test_initials(name: str, count: int, expected: str) -> None:
    """
    Tests that a person's initials are returned from their full name.

    :param name: full name
    :param expected: expected initials
    """

    assert initials(name, count=count) == expected
