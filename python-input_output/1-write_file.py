#!/usr/bin/python3
""" writing content into a text file"""


def write_file(filename="", text=""):
    """writes the given text to a file with the specified filename"""
    with open(filename, 'w', encoding="utf-8") as f:
        f.write(text)
    print(len(text))
