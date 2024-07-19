#!/usr/bin/python3
"""
Returning dictionary into a siiple data structure
"""


def class_to_json(obj):
    """
    Returns dictionary into simple data structure
    """
    return obj.__dict__

