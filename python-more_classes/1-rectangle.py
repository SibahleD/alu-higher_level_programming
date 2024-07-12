#!/usr/bin/python3
"""
This module contains a Rectangle class

Attributes:
    width
    height
"""


class Rectangle:
    """empty class"""
    
    def __init__(self, width=0, height=0):
        """
        Returns a width and height value
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.width

    @width.setter
    def width(self, width):
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        self.width = width

    @property
    def height(self):
        return self.height

    @height.setter
    def height(self, height):
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.height = height
