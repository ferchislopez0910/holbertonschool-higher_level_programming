#!/usr/bin/python3
"""
created a class
"""


class BaseGeometry:
    """Class base geo"""
    def area(self):
        """Class base geo"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Class base geo"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
