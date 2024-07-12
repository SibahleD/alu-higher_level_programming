#!/usr/bin/python3
"""
importing methods from BaseGeometry
"""
Rectangle = __import__('8-rectangle').Rectangle

class Square(Rectangle):
    """
    New class Square imports methods from Rectangle
    """
    def __init__(self, size):
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        result = self.__size ** 2
        return result
