#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    total = len(my_list)
    for id in range(total - 1, -1, -1):
        value = my_list[id]
        print("{:d}".format(value), end="\n")
