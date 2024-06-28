#!/usr/bin/python3
def uppercase(string):
    leng = len(string)
    result = ""
    for char in range(leng):
        ascii_old = ord(string[char])
        if 97 <= ascii_old <= 122:
            ascii_new = ascii_old - 32
            result += chr(ascii_new)
        else:
            result += chr(ascii_old)
    print("{}".format(result))
