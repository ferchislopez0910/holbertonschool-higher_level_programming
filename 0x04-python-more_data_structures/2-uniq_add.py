#!/usr/bin/python3
def uniq_add(my_list=[]):
    nw_list = list(set(my_list))
    add = 0
    for i in nw_list:
        add += i
    return add
