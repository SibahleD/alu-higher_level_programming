#!/usr/bin/python3
"""Adding text to a text file"""
def append_write(filename="", text=""):
    """Appends given text to a file with the specified filename and prints the length of the text"""
    with open(filename, 'w', encoding="utf-8") as f:
        f.write(text)
    chara = len(text)
    return chara
