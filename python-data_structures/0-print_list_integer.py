#!/usr/bin/python3

def print_list_integer(my_list=[]):
    total = len(my_list)
    for case in range(total):
        val = my_list[case]
        print("{}".format(val), end="\n")
