#!/usr/bin/python3
def uppercase(n):
    # findng the length of the input
    vi = len(n)
    result = ""
    # loop to check each character and convert to uppercase
    for i in range(vi):
         #finding the ascii value of the character
        x = ord(n[i])
        if 'a' <= n[i] <= 'z':
            #finding the new ascii value of the uppercase
            newx = x - 32
            #printing the new character
            result = "{}{}".format(result, chr(newx))
        else:
            result = "{}{}".format(result, chr(x))
        print("{}".format(result), end="")
