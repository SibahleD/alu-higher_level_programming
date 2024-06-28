#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for s in matrix:
        line = " ".join("{:d}".format(no) for no in s)
        print(line)
