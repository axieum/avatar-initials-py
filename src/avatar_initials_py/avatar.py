from __future__ import annotations

import random
from typing import TYPE_CHECKING, Any, Optional

from PIL import Image, ImageDraw, ImageFont

from avatar_initials_py.colors import lighten, lightness, random_hex_color
from avatar_initials_py.text import initials as get_initials

if TYPE_CHECKING:
    from PIL.ImageFont import FreeTypeFont


def create_avatar(
    name: Optional[str] = None,
    initials: Optional[str] = None,
    background: Optional[str] = None,
    foreground: Optional[str] = None,
    height: int = 256,
    font: Optional[FreeTypeFont] = None,
    initial_count: int = 2,
    seed: Optional[Any] = None,
) -> Image.Image:
    """
    Generates and returns a new avatar using a person's initials.

    :param name: full name used to derive initials to print on the avatar
    :param initials: optional initials override to print on the avatar
    :param background: optional background hex colour override
    :param foreground: optional foreground hex colour override
    :param height: height (and width) of the image (1:1 ratio)
    :param font: optional font override
    :param initial_count: maximum number of initials (will trim middle) used when `name` is provided
    :param seed: the seed used to randomly choose a `background` colour (defaults to `name or initials`)
    :return: generated avatar image
    :raise ValueError: if neither `name` nor `initials` are provided; or invalid colours are provided
    """

    # Set the initials
    if not initials:
        if name:
            initials = get_initials(name, count=initial_count)
        else:
            raise ValueError("at least one of `name` or `initials` is required")

    # Choose a background colour
    if not background:
        if foreground:
            background = lighten(foreground, -80 if lightness(foreground) < 165 else 80)
        else:
            background = random_hex_color(random.Random(seed or name or initials))

    # Choose a foreground colour
    if not foreground:
        foreground = lighten(background, 80 if lightness(background) < 165 else -80)

    # Set the font
    if not font:
        font = ImageFont.truetype("arialbd.ttf", size=int(height / 2.5))

    # Create the image with the background colour
    img: Image.Image = Image.new("RGB", (height, height), background)

    # Draw the initials onto the image
    draw: ImageDraw.ImageDraw = ImageDraw.Draw(img)
    draw.text((height / 2, height / 2), initials, fill=foreground, font=font, anchor="mm")

    # Return the avatar
    return img
