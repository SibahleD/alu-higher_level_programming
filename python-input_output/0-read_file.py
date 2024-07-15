#!/usr/bin/python3
"""
Reading a text document
"""


def read_file(filename=""):
    """Reads  the textfile and returns a sting"""
    with open(filename, encoding="utf-8") as f:
        read_data = f.read()
    print(read_data)
