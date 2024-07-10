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
        Raises a TypeError if size is not an integer
        Raises a ValueError if size is less than 0
        """
            self.__size = size
        if not isinstance(size, int):
            raise TypeError("size must be >= 0")
        if size < 0:
            raise ValueError("size must be an integer")
