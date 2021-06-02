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
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """ class Rectangle that inherits from BaseGeometry """
    def __init__(self, width, height):
        """rectangle"""
        self.__width = width
        self.__heigth = height
        self.integer_validator("width", self.__width)
        self.integer_validator("height", self.__heigth)
