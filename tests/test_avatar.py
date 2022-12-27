from io import BytesIO
from typing import Optional, Any

import pytest
from PIL import ImageFont
from PIL.ImageFont import FreeTypeFont
from syrupy import SnapshotAssertion
from syrupy.extensions.image import PNGImageSnapshotExtension

from avatar_initials_py.avatar import create_avatar


def test_name_or_initials_is_required() -> None:
    """Tests that at least one of `name` or `initials` is required when generating an avatar"""

    with pytest.raises(ValueError, match="at least one of `name` or `initials` is required"):
        create_avatar(name=None, initials="")

    create_avatar(name="John Doe")
    create_avatar(initials="JD")


def test_avatar_size() -> None:
    """Tests that generated avatars are of expected height and width"""

    assert create_avatar("John Doe", height=64).size == (64, 64)
    assert create_avatar("John Doe", height=72).size == (72, 72)
    assert create_avatar("John Doe", height=128).size == (128, 128)
    assert create_avatar("John Doe").size == (256, 256)


def test_avatar_seed() -> None:
    """Tests that generated avatars with a fixed seed are reproducible"""

    assert create_avatar("John Doe", seed=9) == create_avatar("John Doe", seed=9)


@pytest.mark.parametrize(
    "name, initials, background, foreground, height, font, initial_count, seed",
    [
        (None, "QHD", None, None, 256, None, 2, None),
        ("Karl Lopez", None, None, None, 256, None, 2, None),
        ("John Doe", None, None, None, 256, None, 2, "@john.doe"),
        ("Ruby Torres Peck", None, None, None, 256, None, 2, None),
        ("Amanda Barry Carter", None, None, None, 256, None, 3, None),
        ("Carolyn Bishop", "BC", None, None, 256, None, 2, None),
        ("Letitia Gordon", None, "#0388e6", None, 256, None, 2, None),
        ("Brandon Grant", None, None, "#8dc6c2", 256, None, 2, None),
        ("Levi Reyes", None, "#0388e6", "#ffffff", 256, None, 2, None),
        ("Adam O'Reilly", None, None, None, 64, None, 2, None),
        ("Ralph Graham", None, None, None, 256, ImageFont.truetype("arialbi.ttf", size=90), 2, None),
    ],
)
def test_create_avatar(
    name: Optional[str],
    initials: Optional[str],
    background: Optional[str],
    foreground: Optional[str],
    height: int,
    font: Optional[FreeTypeFont],
    initial_count: int,
    seed: Any,
    snapshot: SnapshotAssertion,
) -> None:
    """
    Tests the generation of known avatars with varying arguments.

    :param name: full name used to derive initials to print on the avatar
    :param initials: optional initials override to print on the avatar
    :param background: optional background hex colour override
    :param foreground: optional foreground hex colour override
    :param height: height (and width) of the image (1:1 ratio)
    :param font: optional font override
    :param initial_count: maximum number of initials (will trim middle) used when `name` is provided
    :param seed: the seed used to randomly choose a `background` colour (defaults to `name or initials`)
    :param snapshot: snapshot assertions
    """

    create_avatar(
        name=name,
        initials=initials,
        background=background,
        foreground=foreground,
        height=height,
        font=font,
        initial_count=initial_count,
        seed=seed,
    ).save(buf := BytesIO(), format="png")
    assert buf.getvalue() == snapshot(extension_class=PNGImageSnapshotExtension)
