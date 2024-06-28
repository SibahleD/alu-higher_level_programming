#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    res = []
    if len(tuple_a) > len(tuple_b):
        total = len(tuple_a)
    else:
        total = len(tuple_b)
    for i in range(total):
        if i == len(tuple_b):
            res.append(tuple_a[i])
        elif i > len(tuple_b):
            res.append(tuple_a[i])
        else:
            res.append(tuple_a[i]+tuple_b[i])
    res = tuple(res)
    return res
