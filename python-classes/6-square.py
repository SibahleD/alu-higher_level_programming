#!/usr/bin/python3
"""
Instantiating a Square class
"""


class Square:
    """
    Create new class named Square

    """
    def __init__(self, size=0, position=(0, 0)):
        """
        Returns a value size (Default is 0)

        Raises a ValueError if size is not an integer
        Raises a TypeError if size is less than 0
        """
        self.__size = size
        self.__position = position
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        """
        areaval = self.__size ** 2
        return areaval

    @property
    def size(self):
        """
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def my_print(self):
        """
        """
         if self.__size == 0:
            print()
            return

        for _ in range(self.__position[1]):
            print()

        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)

    @property
    def position(self):
        """
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        """
        if isinstance(value, tuple) and type(value) == int:
            self.__position = value
        else:
            raise TypeError("position must be a tuple of 2 positive integers")
