#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    values = argv[1:]
    value = 0
    arg_num = len(argv) - 1
    if arg_num == 1:
        print("{}".format(values[0]), end="\n")
    elif arg_num > 1:
        for index in range(arg_num):
            value = value + int(values[index])
        print("{}".format(value), end="\n")
    elif arg_num == 0:
        print(0)
