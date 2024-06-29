#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    res = []
    if len(tuple_a) > len(tuple_b):
        more = (tuple_a)
        less = (tuple_b)
    else:
        less = (tuple_a)
        more = (tuple_b)
    for i in range(2):
        if i >= len(less):
            res.append(more[i])
        else:
            res.append(tuple_a[i]+tuple_b[i])
    res = tuple(res)
    return re
