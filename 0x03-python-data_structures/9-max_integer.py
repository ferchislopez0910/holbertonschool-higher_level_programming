#!/usr/bin/python3
def max_integer(my_list=[]):
    ln = len(my_list)
    if not ln:
        my_list = None
    if my_list:
        my_list = sorted(my_list)
        my_list = my_list[-1]
    return(my_list)
