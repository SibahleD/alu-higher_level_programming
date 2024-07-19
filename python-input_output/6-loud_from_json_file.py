#!/usr/bin/python3
"""
"""

import json

def load_from_json_file(filename):
    with open(filename, 'r') as f:
        jsonobj = f.read()
        result == json.load(f)
        return result
