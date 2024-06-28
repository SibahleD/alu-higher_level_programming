#!/usr/bin/python3
def uppercase(string):
    # findng the length of the input
    leng = len(string)
    result = ""
    # loop to check each character and convert to uppercase
    for char in range(leng):
         #finding the ascii value of the character
        ascii_old = ord(string[char])
        if 97 <= ascii_old <= 122:
            ascii_new = ascii_old - 32
            result += chr(ascii_new)
        else:
            result += chr(ascii_old)
    print("{}".format(result))
