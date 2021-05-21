#!/usr/bin/python3
"""empty class Square that defines a square"""


class Rectangle:
    """empty class Square that

    defines a square"""
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        # Created the module
        if isinstance(height, int):
            self.__height = height
            if height < 0:
                raise ValueError("height must be >= 0")
        else:
            raise TypeError("height must be an integer")

        if isinstance(width, int):
            self.__width = width
            if width < 0:
                raise ValueError("width must be >= 0")
        else:
            raise TypeError("width must be an integer")
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Def del width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Def del height"""
        if isinstance(value, int):
            self.__width = value
            if value < 0:
                raise ValueError("width must be >= 0")
        else:
            raise TypeError("width must be an integer")

    @property
    def height(self):
        """Def del height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Def del height"""
        if isinstance(value, int):
            self.__height = value
            if value < 0:
                raise ValueError("height must be >= 0")
        else:
            raise TypeError("height must be an integer")

    def area(self):
        # Def del area
        return self.__height * self.__width

    def perimeter(self):
        # Def del area
        if self.__height == 0 or self.__width == 0:
            return 0
        else:
            return ((self.__height + self.__width) * 2)

    def __str__(self):
        rect = ""
        if self.__height == 0 or self.__width == 0:
            return rect

        for i in range(self.__height):
            for j in range(self.__width):
                rect += '#'
            if i < self.__height - 1:
                rect += '\n'
        return rect

    def __repr__(self):
        # print str with repr
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
