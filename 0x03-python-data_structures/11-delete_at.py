#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    for idx in my_list:
        if idx < 0:
            return my_list
        return(my_list.remove(idx))
