#!/usr/bin/python3
"""
making an object from a json file
"""

import json

def load_from_json_file(filename):
    """
    Makes an object from a json file
    """
    with open(filename, 'r') as f:
        jsonobj = f.read()
        result == json.load(f)
        return result
