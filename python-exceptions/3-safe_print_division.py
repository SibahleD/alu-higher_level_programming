#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        division = int(a) / int(b)
        print("Inside result: {:1f}".format(division))
        return division
    except ZeroDivisionError:
        print("Inside result: None")
    return None
