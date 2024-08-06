#!/usr/bin/python3
"""Prints a square with the character #"""


def print_square(size):
    """Prints a square with '#'.

    Args:
        size: The size of the square.
    Raises:
        TypeError: If the size is not an integer
        ValueError: The size is less than 0
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    print("{}".format(("#" * size + "\n") * size), end="")
