#!/usr/bin/python3
"""
Instantiating a Square class
"""


class Square:
    """
    Create new class named Square

    """
    def __init__(self, size=0):
        """
        Returns a value size (Default is 0)

        Raises a ValueError if size is not an integer
        Raises a TypeError if size is less than 0
        """
        self.__size = size
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
