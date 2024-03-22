#!/usr/bin/python3
from sys import argv

num_of_arg = len(argv) - 1
if num_of_arg == 1:
    print(num_of_arg, "argument")
else:
    print(num_of_arg, "arguments")
    if num_of_arg == 0:
        print(".")
    else:
        print(":")
        for index, arg in enumerate(argv[1:], start=1):
            print(f"{index}: {arg}")
