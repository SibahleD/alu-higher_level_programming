#!/usr/bin/python3
def element_at(my_list, idx):
    total = len(my_list)
    if idx < 0 or idx > total:
        return None
    else:
        value = my_list[idx]
        return value

