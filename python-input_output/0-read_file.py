#!/usr/bin/python3
"""
Reading a text document
"""

def read_file(filename=""):
    """Prints text from file"""
    with open(filename, "r", encoding="utf-8") as f:
        print(f.read(), end="")
