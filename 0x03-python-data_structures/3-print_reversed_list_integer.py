#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    rev_list = my_list[::-1]
    for i in range(len(rev_list)):
        print("{}".format(rev_list[i]))
