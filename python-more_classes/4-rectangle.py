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
        self._Rectangle__width = 0
        self._Rectangle__height = 0
        self.width = width
        self.height = height

    @property
    def width(self):
        return self._Rectangle__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self._Rectangle__width = value

    @property
    def height(self):
        return self._Rectangle__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self._Rectangle__height = value

    def area(self):
        areaval = self._Rectangle__height * self._Rectangle__width
        return areaval

    def perimeter(self):
        wid = self._Rectangle__width
        leng = self._Rectangle__height
        if wid == 0 or leng == 0:
            return 0
        else:
            return (wid + leng) * 2

    def __str__(self):
        wid = self._Rectangle__width
        hei = self._Rectangle__height
        if wid == 0 or hei == 0:
            return ""
        return "\n".join(["#" * wid for _ in range(hei)])

    def __print__(self):
        wid = self._Rectangle__width
        hei = self._Rectangle__height
        return "Rectangle({}, {})".format(wid, hei)

    def __repr__(self):
        return "Rectangle({}, {})".format(self._Rectangle__width, self._Rectangle__height)
