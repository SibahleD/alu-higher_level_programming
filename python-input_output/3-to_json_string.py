#!/usr/bin/python3
"""
Viewing a file's json string representation
"""


import json

def to_json_string(my_obj):
    """Views a file's json string representation"""
    jsonout = json.dumps(my_obj)
    return jsonout
