#!/usr/bin/python3
"""
Write a function that returns True if the object is an instance
"""


def inherits_from(obj, a_class):
    """ Write a function that returns True if the object is an instance"""
    return (type(obj) is not a_class and issubclass(type(obj), a_class))
