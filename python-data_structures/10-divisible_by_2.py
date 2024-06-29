#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if not my_list:
        return False
    for number in my_list:
        mod = my_list[number]
        if mod == 0:
            return True
        else:
            return False
