#!/usr/bin/python3
"""
function that adds 2 integers.
return a + b

"""


def add_integer(a, b=98):
    """
    return that adds 2 integers.
    """
    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)
    if type(a) is not int:
        raise TypeError("a must be an integer")
    if type(b) is not int:
        raise TypeError("b must be an integer")
    else:
        return a + b
