#!/usr/bin/python3
def uppercase(n):
    # findng the length of the input
    vi = len(n)
    # loop to check each character and convert to uppercase
    for i in range(0, vi):
         #finding the ascii value of the character
        x = ord(n[i])
        if 'a' <= n[i] <= 'z':
            #finding the new ascii value of the uppercase
            newx = x - 32
            #printing thr new character
            print("{}".format(chr(newx)), end="")
        else:
            print("{}".format(chr(x)), end="")
    print('')
