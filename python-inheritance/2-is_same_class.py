#!/usr/bin/python3
"""
Comparing the instance of an object to a class
"""


def is_same_class(obj, a_class):
    """Return true if obj is instance of a class"""
    return type(obj) is a_class
