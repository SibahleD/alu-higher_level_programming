#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    string = argv[1:]
    arg_num = len(argv) - 1
    if arg_num > 1:
        print("{} arguments:".format(arg_num))
        for index in range(arg_num):
            value = index + 1
            print("{}: {}".format(value, string[index]), end="\n")
    elif arg_num == 1:
        print("1 argument:")
        value = 0
        print("{}: {}".format(arg_num, string[value]), end="\n")
    else:
        print("0 arguments.")
