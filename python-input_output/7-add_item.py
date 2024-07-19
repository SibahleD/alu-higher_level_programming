#!/usr/bin/python3
"""
Adds all arguments to a python list and saves to a json file
"""

import sys
import json


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


if __name__ == "__main__":
    filename = "add_item.json"

    try:
        items = load_from_json_file(filename)
    except (FileNotFoundError, json.JSONDecodeError):
        items = []

    items.extend(sys.argv[1:])
    save_to_json_file(items, filename)
