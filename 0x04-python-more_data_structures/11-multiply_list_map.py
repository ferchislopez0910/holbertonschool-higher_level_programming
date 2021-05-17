#!/usr/bin/python3
def multiply_list_map(my_list=[], number=0):
    new_list = my_list; return(list(map(lambda x, y:  x * number, my_list, new_list)))
