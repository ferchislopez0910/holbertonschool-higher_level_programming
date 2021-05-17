#!/usr/bin/python3
def multiply_list_map(my_list=[], number=0):
    n_l = my_list; return(list(map(lambda x, y:  x * number, n_l, my_list)))
