#!/usr/bin/python3

import sys

def print_arguments():
    arguments = sys.argv[1:]
    num_arguments = len(arguments)

    print("Number of argument(s):", num_arguments, end="")
    if num_arguments == 0:
        print(".")
    else:
        print(" argument" if num_arguments == 1 else " arguments")
        for i, arg in enumerate(arguments, start=1):
            print("{}: {}".format(i, arg))

if __name__ == "__main__":
    print_arguments()
