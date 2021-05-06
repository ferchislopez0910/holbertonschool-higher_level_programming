#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    ln = len(my_list) - 1
    if idx < 0:
        return my_list
    elif idx > ln:
        return my_list
    else:
        new_list = my_list.copy()
        new_list[idx] = element
        return new_list
