#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    total = len(my_list)
    if idx < 0:
        return my_list
    elif idx >= total:
        return my_list
    else:
        my_list[idx] = element
        return my_list
