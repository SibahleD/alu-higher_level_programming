#!/usr/bin/python3

def append_write(filename="", text=""):
    with open(filename, 'w', encoding="utf-8") as f:
        f.write(text)
    chara = len(text)
    return chara
