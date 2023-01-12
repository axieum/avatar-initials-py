import re


def initials(name: str, count: int = 2) -> str:
    """
    Returns the initials for a given person's full name. It supports names in the
    following formats:
        - First [Middle] [Last]
        - Last, First [Middle]

    :param name: full name
    :param count: maximum number of initials (will trim middle)
    :return: uppercase initials
    """

    # Reverse any names with surname first, e.g. 'DOE, John'
    name = " ".join(name.split(",", 1)[::-1])

    # Collect the first letter of each word/name
    letters: str = "".join(word[0] for word in re.split(r"\s+", name) if word).upper()

    # Truncate the initials to the desired length, removing letters from the middle
    return letters[: min(count, len(letters)) - 1] + letters[-1] if count != 1 else letters[0]
