#!/usr/bin/python3
"""
Finding the instance of an object
"""
def is_same_class(obj, a_class):
    """Return true if obj is instance of a class"""
    if isinstance(obj, a_class):
        return True
    else:
        return False
