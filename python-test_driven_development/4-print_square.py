#!/usr/bin/python3


"""
    Prints a square with the character #

    :param size: The size length of the square (integer)
    :raises TypeError: If size is not an integer
    or if size is a float less than 0
    :raises ValueError: If size is less than 0
"""


def print_square(size):
    """
    Prints a square with the character #
    """
    if not isinstance(size, int):
        if isinstance(size, float) and size >= 0:
            raise TypeError("size must be an integer")
        else:
            raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for _ in range(size):
        print("#" * size)
