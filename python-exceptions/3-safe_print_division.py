#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        division = int(a) / int(b)
    except ZeroDivisionError:
        division = None
    finally:
        if division is None:
            print("Inside result: None")
        else:
            print("Inside result: {:.1f}".format(division))
    return division
