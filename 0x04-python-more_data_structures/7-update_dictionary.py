#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    new_dic = {key: value}
    a_dictionary.update(new_dic)
    return a_dictionary
