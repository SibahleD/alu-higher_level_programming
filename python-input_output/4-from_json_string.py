#!/usr/bin/python3
"""
Decoding a file's json string representation
"""


import json


def to_json_string(my_obj):
    """Decoding a file's json string representation"""

    jsonout = json.load(my_obj)
    return jsonout
