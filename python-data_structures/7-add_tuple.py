#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    # Ensure both tuples have at least 2 elements by padding with zeros if necessary
    if len(tuple_a) < 2:
        tuple_a = tuple_a + (0,) * (2 - len(tuple_a))
    if len(tuple_b) < 2:
        tuple_b = tuple_b + (0,) * (2 - len(tuple_b))

    res = []
    for i in range(2):
        if len(tuple_a) <= i and len(tuple_b) <=i :
            res.append(tuple_a[i] + tuple_b[i])
        else:
            res.append(0)

    return tuple(res)
