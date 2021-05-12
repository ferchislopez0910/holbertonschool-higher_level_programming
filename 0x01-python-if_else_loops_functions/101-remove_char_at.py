#!/usr/bin/python3
def remove_char_at(str, n):
    copy_str = ""
    for i in range(len(str)):
        if i != n:
            copy_str += str[i]
    return(copy_str)
