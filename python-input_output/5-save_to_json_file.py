#!/usr/bin/python3
"""Saves python oject to a json file"""


import json

def save_to_json_file(my_obj, filename):
    """
    Saves a python object to a file in json format
    """
    with open(filename, 'w' ) as f:
        json_obj = json.dumps(my_obj)
        f.write(json_obj)
