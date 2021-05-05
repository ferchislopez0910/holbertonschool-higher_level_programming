#!/usr/bin/python3
def print_list_integer(my_list=[]):
    ln = len(my_list)
    for i in range(0, ln):
        print("{:d}".format(my_list[i]))
