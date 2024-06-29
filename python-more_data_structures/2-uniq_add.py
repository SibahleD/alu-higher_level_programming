#!/usr/bin/python3
def uniq_add(my_list=[]):
    my_set = set(my_list)
    value = 0
    for i in map(int, my_set):
        value += i
    return value
