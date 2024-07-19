#!/usr/bin/python3
"""
Decoding a file's json string representation
"""
import json


def from_json_string(my_obj):
    """
    Decodes a file's json string representation
    """
    return json.loads(my_obj)
