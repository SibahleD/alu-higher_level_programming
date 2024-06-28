#!/usr/bin/python3
def no_c(my_string):
    leng = len(my_string)
    result = ""
    for char in range(leng):
        oldval = my_string[char]
        if oldval == 'c' or oldval == 'C':
            new_val = ""
            result += new_val
        else:
            result += oldval
    return result
