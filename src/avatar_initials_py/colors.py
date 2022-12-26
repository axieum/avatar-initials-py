import random

from PIL import ImageColor


def lightness(color: str) -> float:
    """
    Returns the lightness of a given colour.

    :param color: hex colour
    :return: lightness between 0 and 255
    :raise ValueError: if the `color` is invalid
    """

    rgb: tuple[int, ...] = ImageColor.getrgb(color)
    return rgb[0] * 0.2126 + rgb[1] * 0.7152 + rgb[2] * 0.0722


def lighten(color: str, amount: int) -> str:
    """
    Lightens a colour by adding an amount to all three red, green & blue channels.

    :param color: hex colour
    :param amount: amount to lighten (negative value to darken)
    :return: lightened colour in format '#139adf'
    """

    rgb: tuple[int, ...] = ImageColor.getrgb(color)
    r, g, b = (
        min(max(rgb[0] + amount, 0), 255),
        min(max(rgb[1] + amount, 0), 255),
        min(max(rgb[2] + amount, 0), 255),
    )
    return f"#{r:02x}{g:02x}{b:02x}"


def random_hex_color() -> str:
    """
    Returns a random 6-character hex colour code.

    :return: hex colour in format '#139adf'
    """

    return f"#{random.randint(0x000000, 0xFFFFFF):06x}"
