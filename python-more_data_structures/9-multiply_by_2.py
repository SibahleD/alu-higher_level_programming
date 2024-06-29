#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dict = {}
    for key in a_dictionary:
        val = a_dictionary[key]
        new_dict[key] = int(val) * 2
    return new_dict
