#!/usr/bin/python3
def common_elements(set_1, set_2):
    new_list = []
    for j in set_1:
        if j in set_2:
            new_list.append(j)
    return new_list
