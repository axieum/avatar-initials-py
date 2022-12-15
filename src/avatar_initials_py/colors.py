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
