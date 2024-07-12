#!/usr/bin/python3
"""
comparing instance of an object
"""


def inherits_from(obj, a_class):
    """
    Return true if obj is instance of a class
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
