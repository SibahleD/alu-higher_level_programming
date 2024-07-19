#!/usr/python3
"""Saves text to a textfile"""


import json
def save_to_json_file(my_obj, filename):
    with open(filename, 'w' ) as f:
        json_obj = json.dumps(my_obj)
        f.write(json_obj)
