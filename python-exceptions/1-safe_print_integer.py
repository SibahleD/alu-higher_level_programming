#!/usr/bin/python3
def safe_print_integer(value):
    try:
        if not isinstance(value, int):
            return False
        print("{:d}".format(value))
        return True
    except ValueError as ve:
        print(f"ValueError: {ve}")
    except Exception as e:
        print(f"An unknown error occured: {e}")
    return False
